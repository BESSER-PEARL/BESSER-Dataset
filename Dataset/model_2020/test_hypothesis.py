import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    uml::ActivityContent,
    BasicActions::TracedActionActivation,
    umlTrace::Values::ActionActivation::firing::Value,
    TracedLiteralEvaluation,
    umlTrace::Kernel::TracedLiteralIntegerEvaluation,
    umlTrace::Kernel::TracedLiteralBooleanEvaluation,
    TracedPrimitiveValue,
    umlTrace::Kernel::TracedBooleanValue,
    umlTrace::Kernel::TracedIntegerValue,
    TracedEvaluation,
    umlTrace::Kernel::TracedLiteralEvaluation,
    TracedValue,
    umlTrace::Kernel::TracedPrimitiveValue,
    umlTrace::Kernel::TracedStructuredValue,
    TracedStructuredValue,
    umlTrace::Kernel::TracedReference,
    umlTrace::Kernel::TracedCompoundValue,
    TracedCompoundValue,
    umlTrace::Kernel::TracedExtensionalValue,
    TracedExtensionalValue,
    umlTrace::Kernel::TracedObject,
    TracedObject,
    umlTrace::BasicBehaviors::TracedExecution,
    uml::TracedElement,
    umlTrace::Values::SemanticVisitor::runtimeModelElement::Value,
    TracedOpaqueBehaviorExecution,
    umlTrace::IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution,
    umlTrace::IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution,
    umlTrace::IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution,
    TracedCallActionActivation,
    umlTrace::BasicActions::TracedCallBehaviorActionActivation,
    TracedPinActivation,
    umlTrace::BasicActions::TracedOutputPinActivation,
    umlTrace::BasicActions::TracedInputPinActivation,
    TracedInvocationActionActivation,
    umlTrace::BasicActions::TracedCallActionActivation,
    TracedActionActivation,
    umlTrace::BasicActions::TracedOpaqueActionActivation,
    umlTrace::BasicActions::TracedInvocationActionActivation,
    umlTrace::Loci::TracedSemanticVisitor,
    TracedObjectNodeActivation,
    umlTrace::BasicActions::TracedPinActivation,
    umlTrace::IntermediateActivities::TracedActivityParameterNodeActivation,
    umlTrace::IntermediateActions::TracedCreateObjectActionActivation,
    umlTrace::IntermediateActions::TracedValueSpecificationActionActivation,
    TracedWriteStructuralFeatureActionActivation,
    umlTrace::IntermediateActions::TracedAddStructuralFeatureValueActionActivation,
    TracedStructuralFeatureActionActivation,
    umlTrace::IntermediateActions::TracedWriteStructuralFeatureActionActivation,
    umlTrace::IntermediateActions::TracedReadStructuralFeatureActionActivation,
    umlTrace::IntermediateActions::TracedStructuralFeatureActionActivation,
    umlTrace::ecore::TracedEModelElement,
    TracedMessageEnd,
    umlTrace::uml::TracedGate,
    TracedExecution,
    umlTrace::BasicBehaviors::TracedOpaqueBehaviorExecution,
    TracedExecutionSpecification,
    umlTrace::uml::TracedBehaviorExecutionSpecification,
    TracedOccurrenceSpecification,
    umlTrace::uml::TracedExecutionOccurrenceSpecification,
    TracedOpaqueBehavior,
    umlTrace::uml::TracedFunctionBehavior,
    uml::TracedStructuredClassifier,
    TracedMultiplicityElement,
    umlTrace::uml::TracedConnectorEnd,
    umlTrace::uml::TracedActionExecutionSpecification,
    TracedObjectNode,
    umlTrace::uml::TracedExpansionNode,
    umlTrace::uml::TracedActivityParameterNode,
    umlTrace::uml::TracedCentralBufferNode,
    TracedCentralBufferNode,
    umlTrace::uml::TracedDataStoreNode,
    TracedDataType,
    umlTrace::uml::TracedEnumeration,
    umlTrace::uml::TracedPrimitiveType,
    TracedMessageEvent,
    umlTrace::uml::TracedCallEvent,
    umlTrace::uml::TracedAnyReceiveEvent,
    uml::TracedBehavioralFeature,
    TracedTemplateParameter,
    umlTrace::uml::TracedConnectableElementTemplateParameter,
    umlTrace::uml::TracedClassifierTemplateParameter,
    TracedPackage,
    umlTrace::uml::TracedProfile,
    umlTrace::uml::TracedModel,
    TracedTransition,
    umlTrace::uml::TracedProtocolTransition,
    TracedWriteVariableAction,
    umlTrace::uml::TracedRemoveVariableValueAction,
    umlTrace::uml::TracedAddVariableValueAction,
    TracedInteractionUse,
    umlTrace::uml::TracedPartDecomposition,
    TracedObservation,
    umlTrace::uml::TracedTimeObservation,
    umlTrace::uml::TracedDurationObservation,
    umlTrace::uml::TracedOperationTemplateParameter,
    TracedInterval,
    umlTrace::uml::TracedDurationInterval,
    umlTrace::uml::TracedTimeInterval,
    umlTrace::uml::TracedSignalEvent,
    TracedBehavioralFeature,
    umlTrace::uml::TracedReception,
    TracedDependency,
    umlTrace::uml::TracedUsage,
    umlTrace::uml::TracedAbstraction,
    TracedAbstraction,
    umlTrace::uml::TracedManifestation,
    umlTrace::uml::TracedRealization,
    TracedRealization,
    umlTrace::uml::TracedComponentRealization,
    umlTrace::uml::TracedInterfaceRealization,
    umlTrace::uml::TracedSubstitution,
    TracedInstanceSpecification,
    umlTrace::uml::TracedEnumerationLiteral,
    TracedAcceptEventAction,
    umlTrace::uml::TracedAcceptCallAction,
    TracedLinkEndData,
    umlTrace::uml::TracedLinkEndCreationData,
    umlTrace::uml::TracedLinkEndDestructionData,
    TracedClass,
    umlTrace::uml::TracedComponent,
    umlTrace::uml::TracedStereotype,
    umlTrace::uml::TracedBehavior,
    uml::TracedInteractionFragment,
    uml::TracedBehavior,
    umlTrace::uml::TracedInteraction,
    TracedActivityEdge,
    umlTrace::uml::TracedControlFlow,
    umlTrace::uml::TracedObjectFlow,
    TracedStateMachine,
    umlTrace::uml::TracedProtocolStateMachine,
    umlTrace::uml::TracedDeployment,
    TracedBehavior,
    umlTrace::uml::TracedOpaqueBehavior,
    umlTrace::uml::TracedActivity,
    umlTrace::uml::TracedStateMachine,
    TracedActivityGroup,
    umlTrace::uml::TracedInterruptibleActivityRegion,
    umlTrace::uml::TracedActivityPartition,
    uml::TracedRelationship,
    umlTrace::IntermediateActivities::TracedActivityExecution,
    TracedSemanticVisitor,
    umlTrace::Kernel::TracedEvaluation,
    umlTrace::Kernel::TracedValue,
    umlTrace::IntermediateActivities::TracedActivityNodeActivation,
    TracedActivityNodeActivation,
    umlTrace::BasicActions::TracedActionActivation,
    umlTrace::IntermediateActivities::TracedObjectNodeActivation,
    umlTrace::IntermediateActivities::TracedControlNodeActivation,
    TracedControlNodeActivation,
    umlTrace::IntermediateActivities::TracedInitialNodeActivation,
    umlTrace::IntermediateActivities::TracedActivityFinalNodeActivation,
    umlTrace::IntermediateActivities::TracedDecisionNodeActivation,
    umlTrace::IntermediateActivities::TracedJoinNodeActivation,
    umlTrace::IntermediateActivities::TracedMergeNodeActivation,
    umlTrace::IntermediateActivities::TracedForkNodeActivation,
    uml::TracedVertex,
    TracedState,
    umlTrace::uml::TracedFinalState,
    uml::TracedActivityFinalNode,
    uml::TracedClassifierTemplateParameter,
    TracedInteractionFragment,
    umlTrace::uml::TracedStateInvariant,
    umlTrace::uml::TracedExecutionSpecification,
    umlTrace::uml::TracedCombinedFragment,
    uml::TracedGeneralOrdering,
    uml::TracedElementImport,
    uml::TracedMergeNode,
    uml::TracedClearAssociationAction,
    uml::TracedLinkEndCreationData,
    uml::TracedPseudostate,
    uml::TracedComponent,
    uml::TracedReadIsClassifiedObjectAction,
    uml::TracedAbstraction,
    uml::TracedTimeExpression,
    uml::TracedValueSpecificationAction,
    uml::TracedFunctionBehavior,
    IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution,
    IntermediateActivities::TracedMergeNodeActivation,
    uml::TracedTemplateParameter,
    uml::TracedManifestation,
    uml::TracedActor,
    uml::TracedRemoveVariableValueAction,
    uml::TracedProfile,
    uml::TracedTestIdentityAction,
    uml::TracedCollaboration,
    uml::TracedSendSignalAction,
    uml::TracedInterfaceRealization,
    uml::TracedUnmarshallAction,
    uml::TracedExpression,
    uml::TracedAssociation,
    uml::TracedClearStructuralFeatureAction,
    uml::TracedAddVariableValueAction,
    uml::TracedLiteralReal,
    IntermediateActions::TracedCreateObjectActionActivation,
    uml::TracedSlot,
    uml::TracedLiteralNull,
    IntermediateActions::TracedValueSpecificationActionActivation,
    uml::TracedStartObjectBehaviorAction,
    uml::TracedLiteralBoolean,
    uml::TracedReadLinkAction,
    uml::TracedInclude,
    uml::TracedRegion,
    uml::TracedState,
    uml::TracedPrimitiveType,
    uml::TracedStringExpression,
    uml::TracedLinkEndDestructionData,
    uml::TracedReadExtentAction,
    BasicActions::TracedOutputPinActivation,
    uml::TracedTemplateSignature,
    uml::TracedRaiseExceptionAction,
    uml::TracedCommunicationPath,
    Kernel::TracedLiteralBooleanEvaluation,
    uml::TracedEnumeration,
    uml::TracedReadLinkObjectEndAction,
    uml::TracedCallBehaviorAction,
    uml::TracedVariable,
    uml::TracedConnectorEnd,
    uml::TracedArtifact,
    uml::TracedCallOperationAction,
    uml::TracedLiteralUnlimitedNatural,
    uml::TracedDurationObservation,
    uml::TracedBehaviorExecutionSpecification,
    uml::TracedActivityParameterNode,
    uml::TracedExpansionNode,
    uml::TracedProfileApplication,
    uml::TracedAddStructuralFeatureValueAction,
    uml::TracedQualifierValue,
    uml::TracedImage,
    uml::TracedExtensionEnd,
    uml::TracedProperty,
    uml::TracedDevice,
    uml::TracedOpaqueAction,
    uml::TracedFinalState,
    uml::TracedReduceAction,
    uml::TracedDuration,
    uml::TracedTemplateParameterSubstitution,
    uml::TracedOutputPin,
    uml::TracedActionExecutionSpecification,
    uml::TracedInformationItem,
    uml::TracedOperationTemplateParameter,
    uml::TracedConnectableElementTemplateParameter,
    uml::TracedLinkEndData,
    uml::TracedDurationInterval,
    uml::TracedTransition,
    uml::TracedTrigger,
    uml::TracedReplyAction,
    uml::TracedClause,
    uml::TracedPackageMerge,
    uml::TracedDecisionNode,
    IntermediateActions::TracedReadStructuralFeatureActionActivation,
    uml::TracedReadSelfAction,
    uml::TracedOperation,
    uml::TracedObjectFlow,
    uml::TracedParameterSet,
    uml::TracedOccurrenceSpecification,
    uml::TracedAcceptEventAction,
    uml::TracedComponentRealization,
    uml::TracedDataType,
    uml::TracedComment,
    uml::TracedLoopNode,
    uml::TracedCallEvent,
    uml::TracedPackage,
    uml::TracedProtocolConformance,
    uml::TracedOpaqueBehavior,
    uml::TracedInterface,
    IntermediateActivities::TracedDecisionNodeActivation,
    uml::TracedInteractionConstraint,
    uml::TracedTimeInterval,
    uml::TracedExecutionOccurrenceSpecification,
    uml::TracedSignal,
    uml::TracedExtensionPoint,
    uml::TracedCreateLinkAction,
    Kernel::TracedLiteralIntegerEvaluation,
    uml::TracedCentralBufferNode,
    uml::TracedModel,
    uml::TracedRedefinableTemplateSignature,
    uml::TracedJoinNode,
    BasicActions::TracedOpaqueActionActivation,
    uml::TracedReadLinkObjectEndQualifierAction,
    uml::TracedRealization,
    uml::TracedConnectionPointReference,
    uml::TracedConditionalNode,
    Kernel::TracedBooleanValue,
    uml::TracedSignalEvent,
    uml::TracedLiteralInteger,
    uml::TracedDestroyLinkAction,
    IntermediateActivities::TracedActivityFinalNodeActivation,
    uml::TracedReadVariableAction,
    uml::TracedActionInputPin,
    uml::TracedUsage,
    uml::TracedDeploymentSpecification,
    uml::TracedTemplateBinding,
    TracedAssociation,
    umlTrace::uml::TracedCommunicationPath,
    umlTrace::uml::TracedExtension,
    TracedStructuralFeatureAction,
    umlTrace::uml::TracedClearStructuralFeatureAction,
    umlTrace::uml::TracedReadStructuralFeatureAction,
    uml::TracedMessageOccurrenceSpecification,
    umlTrace::uml::TracedWriteStructuralFeatureAction,
    uml::TracedReception,
    TracedWriteStructuralFeatureAction,
    umlTrace::uml::TracedAddStructuralFeatureValueAction,
    umlTrace::uml::TracedRemoveStructuralFeatureValueAction,
    TracedBehavioredClassifier,
    umlTrace::uml::TracedActor,
    umlTrace::uml::TracedUseCase,
    uml::TracedDeployedArtifact,
    uml::TracedClassifier,
    umlTrace::uml::TracedAssociation,
    umlTrace::uml::TracedArtifact,
    TracedArtifact,
    umlTrace::uml::TracedDeploymentSpecification,
    uml::TracedActivityNode,
    uml::TracedObjectNode,
    TracedPin,
    umlTrace::uml::TracedOutputPin,
    umlTrace::uml::TracedInputPin,
    TracedInputPin,
    umlTrace::uml::TracedActionInputPin,
    umlTrace::uml::TracedValuePin,
    uml::TracedMultiplicityElement,
    umlTrace::uml::TracedPin,
    uml::TracedTypedElement,
    umlTrace::uml::TracedObjectNode,
    uml::TracedFeature,
    umlTrace::uml::TracedStructuralFeature,
    TracedValueSpecification,
    umlTrace::uml::TracedExpression,
    umlTrace::uml::TracedDuration,
    umlTrace::uml::TracedInstanceValue,
    umlTrace::uml::TracedOpaqueExpression,
    umlTrace::uml::TracedInterval,
    umlTrace::uml::TracedTimeExpression,
    umlTrace::uml::TracedLiteralSpecification,
    TracedLiteralSpecification,
    umlTrace::uml::TracedLiteralBoolean,
    umlTrace::uml::TracedLiteralNull,
    umlTrace::uml::TracedLiteralReal,
    umlTrace::uml::TracedLiteralInteger,
    umlTrace::uml::TracedLiteralUnlimitedNatural,
    umlTrace::uml::TracedLiteralString,
    TracedVariableAction,
    umlTrace::uml::TracedReadVariableAction,
    umlTrace::uml::TracedWriteVariableAction,
    umlTrace::uml::TracedClearVariableAction,
    umlTrace::uml::TracedContinuation,
    TracedCombinedFragment,
    umlTrace::uml::TracedConsiderIgnoreFragment,
    TracedNode,
    umlTrace::uml::TracedExecutionEnvironment,
    umlTrace::uml::TracedDevice,
    uml::TracedType,
    TracedClassifier,
    umlTrace::uml::TracedBehavioredClassifier,
    umlTrace::uml::TracedInformationItem,
    umlTrace::uml::TracedDataType,
    umlTrace::uml::TracedInterface,
    umlTrace::uml::TracedStructuredClassifier,
    TracedStructuredClassifier,
    umlTrace::uml::TracedEncapsulatedClassifier,
    uml::TracedBehavioredClassifier,
    umlTrace::uml::TracedCollaboration,
    uml::TracedEncapsulatedClassifier,
    umlTrace::uml::TracedClass,
    TracedCallAction,
    umlTrace::uml::TracedStartObjectBehaviorAction,
    umlTrace::uml::TracedCallOperationAction,
    umlTrace::uml::TracedCallBehaviorAction,
    TracedRelationship,
    umlTrace::uml::TracedDirectedRelationship,
    TracedDirectedRelationship,
    umlTrace::uml::TracedGeneralization,
    umlTrace::uml::TracedTemplateBinding,
    umlTrace::uml::TracedProfileApplication,
    umlTrace::uml::TracedPackageImport,
    umlTrace::uml::TracedElementImport,
    umlTrace::uml::TracedPackageMerge,
    umlTrace::uml::TracedProtocolConformance,
    TracedInvocationAction,
    umlTrace::uml::TracedBroadcastSignalAction,
    umlTrace::uml::TracedSendSignalAction,
    umlTrace::uml::TracedCallAction,
    umlTrace::uml::TracedSendObjectAction,
    TracedRedefinableElement,
    umlTrace::uml::TracedExtensionPoint,
    umlTrace::uml::TracedActivityEdge,
    umlTrace::uml::TracedFeature,
    TracedFeature,
    umlTrace::uml::TracedConnector,
    uml::TracedTemplateableElement,
    umlTrace::uml::TracedStringExpression,
    uml::TracedPackageableElement,
    umlTrace::uml::TracedValueSpecification,
    uml::TracedDeploymentTarget,
    umlTrace::uml::TracedInstanceSpecification,
    uml::TracedConnectableElement,
    umlTrace::uml::TracedParameter,
    umlTrace::uml::TracedVariable,
    uml::TracedStructuralFeature,
    umlTrace::uml::TracedProperty,
    TracedProperty,
    umlTrace::uml::TracedExtensionEnd,
    umlTrace::uml::TracedPort,
    uml::TracedDirectedRelationship,
    umlTrace::uml::TracedInformationFlow,
    umlTrace::uml::TracedDependency,
    TracedEvent,
    umlTrace::uml::TracedTimeEvent,
    umlTrace::uml::TracedMessageEvent,
    umlTrace::uml::TracedChangeEvent,
    umlTrace::uml::TracedSignal,
    umlTrace::uml::TracedInteractionUse,
    TracedFinalNode,
    umlTrace::uml::TracedActivityFinalNode,
    umlTrace::uml::TracedFlowFinalNode,
    TracedControlNode,
    umlTrace::uml::TracedJoinNode,
    umlTrace::uml::TracedMergeNode,
    umlTrace::uml::TracedForkNode,
    umlTrace::uml::TracedFinalNode,
    umlTrace::uml::TracedDecisionNode,
    umlTrace::uml::TracedInitialNode,
    TracedAction,
    umlTrace::uml::TracedAcceptEventAction,
    umlTrace::uml::TracedStartClassifierBehaviorAction,
    umlTrace::uml::TracedStructuralFeatureAction,
    umlTrace::uml::TracedReduceAction,
    umlTrace::uml::TracedValueSpecificationAction,
    umlTrace::uml::TracedOpaqueAction,
    umlTrace::uml::TracedUnmarshallAction,
    umlTrace::uml::TracedReadSelfAction,
    umlTrace::uml::TracedReadIsClassifiedObjectAction,
    umlTrace::uml::TracedDestroyObjectAction,
    umlTrace::uml::TracedVariableAction,
    umlTrace::uml::TracedReadLinkObjectEndQualifierAction,
    umlTrace::uml::TracedInvocationAction,
    umlTrace::uml::TracedRaiseExceptionAction,
    umlTrace::uml::TracedReadLinkObjectEndAction,
    umlTrace::uml::TracedClearAssociationAction,
    umlTrace::uml::TracedReadExtentAction,
    umlTrace::uml::TracedReplyAction,
    umlTrace::uml::TracedTestIdentityAction,
    umlTrace::uml::TracedCreateObjectAction,
    umlTrace::uml::TracedReclassifyObjectAction,
    umlTrace::uml::TracedLinkAction,
    TracedLinkAction,
    umlTrace::uml::TracedReadLinkAction,
    umlTrace::uml::TracedWriteLinkAction,
    TracedWriteLinkAction,
    umlTrace::uml::TracedDestroyLinkAction,
    umlTrace::uml::TracedCreateLinkAction,
    TracedCreateLinkAction,
    umlTrace::uml::TracedCreateLinkObjectAction,
    uml::TracedNamedElement,
    umlTrace::uml::TracedInclude,
    umlTrace::uml::TracedExtend,
    ActivityContent,
    umlTrace::uml::TracedActivityGroup,
    uml::TracedRedefinableElement,
    umlTrace::uml::TracedRedefinableTemplateSignature,
    umlTrace::uml::TracedActivityNode,
    TracedActivityNode,
    umlTrace::uml::TracedControlNode,
    umlTrace::uml::TracedExecutableNode,
    TracedExecutableNode,
    umlTrace::uml::TracedAction,
    uml::TracedActivityGroup,
    uml::TracedNamespace,
    umlTrace::uml::TracedTransition,
    umlTrace::uml::TracedInteractionOperand,
    umlTrace::uml::TracedRegion,
    umlTrace::uml::TracedPackage,
    umlTrace::uml::TracedState,
    umlTrace::uml::TracedBehavioralFeature,
    umlTrace::uml::TracedClassifier,
    uml::TracedAction,
    umlTrace::uml::TracedStructuredActivityNode,
    TracedStructuredActivityNode,
    umlTrace::uml::TracedExpansionRegion,
    umlTrace::uml::TracedLoopNode,
    umlTrace::uml::TracedSequenceNode,
    umlTrace::uml::TracedConditionalNode,
    TracedEModelElement,
    umlTrace::uml::TracedElement,
    TracedElement,
    umlTrace::uml::TracedTemplateParameter,
    umlTrace::uml::TracedRelationship,
    umlTrace::uml::TracedLinkEndData,
    umlTrace::uml::TracedExceptionHandler,
    umlTrace::uml::TracedSlot,
    umlTrace::uml::TracedTemplateParameterSubstitution,
    umlTrace::uml::TracedTemplateSignature,
    umlTrace::uml::TracedComment,
    umlTrace::uml::TracedMultiplicityElement,
    umlTrace::uml::TracedTemplateableElement,
    umlTrace::uml::TracedClause,
    umlTrace::uml::TracedImage,
    umlTrace::uml::TracedQualifierValue,
    umlTrace::uml::TracedNamedElement,
    TracedNamedElement,
    umlTrace::uml::TracedTypedElement,
    umlTrace::uml::TracedNamespace,
    umlTrace::uml::TracedRedefinableElement,
    umlTrace::uml::TracedDeploymentTarget,
    umlTrace::uml::TracedMessage,
    umlTrace::uml::TracedCollaborationUse,
    umlTrace::uml::TracedMessageEnd,
    umlTrace::uml::TracedGeneralOrdering,
    umlTrace::uml::TracedParameterSet,
    umlTrace::uml::TracedTrigger,
    umlTrace::uml::TracedLifeline,
    umlTrace::uml::TracedDeployedArtifact,
    umlTrace::uml::TracedInteractionFragment,
    umlTrace::uml::TracedOccurrenceSpecification,
    uml::TracedMessageEnd,
    umlTrace::uml::TracedMessageOccurrenceSpecification,
    TracedMessageOccurrenceSpecification,
    umlTrace::uml::TracedDestructionOccurrenceSpecification,
    umlTrace::uml::TracedVertex,
    TracedVertex,
    umlTrace::uml::TracedConnectionPointReference,
    umlTrace::uml::TracedPseudostate,
    umlTrace::uml::TracedParameterableElement,
    uml::TracedParameterableElement,
    umlTrace::uml::TracedConnectableElement,
    umlTrace::uml::TracedOperation,
    umlTrace::uml::TracedPackageableElement,
    TracedPackageableElement,
    umlTrace::uml::TracedObservation,
    umlTrace::uml::TracedEvent,
    umlTrace::uml::TracedGeneralizationSet,
    umlTrace::uml::TracedType,
    umlTrace::uml::TracedConstraint,
    TracedConstraint,
    umlTrace::uml::TracedInteractionConstraint,
    umlTrace::uml::TracedIntervalConstraint,
    TracedIntervalConstraint,
    umlTrace::uml::TracedTimeConstraint,
    umlTrace::uml::TracedDurationConstraint,
    uml::TracedControlFlow,
    uml::TracedTimeObservation,
    uml::TracedGate,
    uml::TracedProtocolStateMachine,
    uml::TracedDataStoreNode,
    uml::TracedReadStructuralFeatureAction,
    uml::TracedAnyReceiveEvent,
    Kernel::TracedIntegerValue,
    uml::TracedInterval,
    uml::TracedRemoveStructuralFeatureValueAction,
    uml::TracedGeneralization,
    uml::TracedInteractionOperand,
    uml::TracedProtocolTransition,
    uml::TracedInterruptibleActivityRegion,
    uml::TracedPartDecomposition,
    uml::TracedTimeEvent,
    uml::TracedDeployment,
    Loci::TracedSemanticVisitor,
    Kernel::TracedObject,
    IntermediateActivities::TracedJoinNodeActivation,
    uml::TracedUseCase,
    uml::TracedReclassifyObjectAction,
    uml::TracedInstanceValue,
    IntermediateActions::TracedAddStructuralFeatureValueActionActivation,
    Kernel::TracedReference,
    uml::TracedForkNode,
    uml::TracedActivity,
    uml::TracedMessage,
    uml::TracedStateMachine,
    uml::TracedActivityPartition,
    IntermediateActivities::TracedActivityParameterNodeActivation,
    BasicActions::TracedCallBehaviorActionActivation,
    uml::TracedDestroyObjectAction,
    uml::TracedAssociationClass,
    uml::TracedInformationFlow,
    uml::TracedSubstitution,
    uml::TracedEnumerationLiteral,
    uml::TracedStereotype,
    uml::TracedAcceptCallAction,
    uml::TracedInstanceSpecification,
    IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution,
    uml::TracedStateInvariant,
    BasicActions::TracedInputPinActivation,
    uml::TracedLiteralString,
    uml::TracedOpaqueExpression,
    uml::TracedParameter,
    IntermediateActivities::TracedActivityNodeActivation,
    uml::TracedInteraction,
    uml::TracedBroadcastSignalAction,
    uml::TracedConstraint,
    uml::TracedClearVariableAction,
    uml::TracedInputPin,
    uml::TracedTimeConstraint,
    uml::TracedContinuation,
    uml::TracedConsiderIgnoreFragment,
    uml::TracedIntervalConstraint,
    uml::TracedExecutionEnvironment,
    uml::TracedStructuredActivityNode,
    uml::TracedExtension,
    IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution,
    uml::TracedExtend,
    uml::TracedStartClassifierBehaviorAction,
    uml::TracedSequenceNode,
    uml::TracedExceptionHandler,
    uml::TracedNode,
    uml::TracedValuePin,
    IntermediateActivities::TracedActivityExecution,
    uml::TracedCollaborationUse,
    IntermediateActivities::TracedInitialNodeActivation,
    uml::TracedPort,
    uml::TracedDependency,
    uml::TracedChangeEvent,
    uml::TracedGeneralizationSet,
    uml::TracedInteractionUse,
    uml::TracedClass,
    umlTrace::uml::TracedNode,
    umlTrace::uml::TracedAssociationClass,
    uml::TracedPackageImport,
    uml::TracedSendObjectAction,
    uml::TracedConnector,
    uml::TracedDestructionOccurrenceSpecification,
    uml::TracedDurationConstraint,
    IntermediateActivities::TracedForkNodeActivation,
    uml::TracedLifeline,
    uml::TracedCreateObjectAction,
    uml::TracedExpansionRegion,
    uml::TracedFlowFinalNode,
    uml::TracedInitialNode,
    uml::TracedCreateLinkObjectAction,
    uml::TracedCombinedFragment,
    umlTrace::Traced::TracedObjects,
    Traced::TracedObjects,
    State,
    umlTrace::Trace,
    Values::SemanticVisitor::runtimeModelElement::Value,
    Values::ActionActivation::firing::Value,
    umlTrace::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml::activitycontent_is_not_abstract():
    assert not inspect.isabstract(uml::ActivityContent)


def test_uml::activitycontent_constructor_exists():
    assert callable(uml::ActivityContent.__init__)


def test_uml::activitycontent_constructor_args():
    sig = inspect.signature(uml::ActivityContent.__init__)
    params = list(sig.parameters.keys())



def test_basicactions::tracedactionactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions::TracedActionActivation)


def test_basicactions::tracedactionactivation_constructor_exists():
    assert callable(BasicActions::TracedActionActivation.__init__)


def test_basicactions::tracedactionactivation_constructor_args():
    sig = inspect.signature(BasicActions::TracedActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::values::actionactivation::firing::value_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Values::ActionActivation::firing::Value)


def test_umltrace::values::actionactivation::firing::value_constructor_exists():
    assert callable(umlTrace::Values::ActionActivation::firing::Value.__init__)


def test_umltrace::values::actionactivation::firing::value_constructor_args():
    sig = inspect.signature(umlTrace::Values::ActionActivation::firing::Value.__init__)
    params = list(sig.parameters.keys())
    assert "firing" in params, "Missing parameter 'firing'"

def test_umltrace::values::actionactivation::firing::value_has_firing():
    assert hasattr(umlTrace::Values::ActionActivation::firing::Value, "firing")
    descriptor = None
    for klass in umlTrace::Values::ActionActivation::firing::Value.__mro__:
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



def test_umltrace::kernel::tracedliteralintegerevaluation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedLiteralIntegerEvaluation)


def test_umltrace::kernel::tracedliteralintegerevaluation_constructor_exists():
    assert callable(umlTrace::Kernel::TracedLiteralIntegerEvaluation.__init__)


def test_umltrace::kernel::tracedliteralintegerevaluation_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedLiteralIntegerEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::kernel::tracedliteralbooleanevaluation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedLiteralBooleanEvaluation)


def test_umltrace::kernel::tracedliteralbooleanevaluation_constructor_exists():
    assert callable(umlTrace::Kernel::TracedLiteralBooleanEvaluation.__init__)


def test_umltrace::kernel::tracedliteralbooleanevaluation_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedLiteralBooleanEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_tracedprimitivevalue_is_not_abstract():
    assert not inspect.isabstract(TracedPrimitiveValue)


def test_tracedprimitivevalue_constructor_exists():
    assert callable(TracedPrimitiveValue.__init__)


def test_tracedprimitivevalue_constructor_args():
    sig = inspect.signature(TracedPrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::kernel::tracedbooleanvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedBooleanValue)


def test_umltrace::kernel::tracedbooleanvalue_constructor_exists():
    assert callable(umlTrace::Kernel::TracedBooleanValue.__init__)


def test_umltrace::kernel::tracedbooleanvalue_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedBooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::kernel::tracedintegervalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedIntegerValue)


def test_umltrace::kernel::tracedintegervalue_constructor_exists():
    assert callable(umlTrace::Kernel::TracedIntegerValue.__init__)


def test_umltrace::kernel::tracedintegervalue_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedIntegerValue.__init__)
    params = list(sig.parameters.keys())



def test_tracedevaluation_is_not_abstract():
    assert not inspect.isabstract(TracedEvaluation)


def test_tracedevaluation_constructor_exists():
    assert callable(TracedEvaluation.__init__)


def test_tracedevaluation_constructor_args():
    sig = inspect.signature(TracedEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::kernel::tracedliteralevaluation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedLiteralEvaluation)


def test_umltrace::kernel::tracedliteralevaluation_constructor_exists():
    assert callable(umlTrace::Kernel::TracedLiteralEvaluation.__init__)


def test_umltrace::kernel::tracedliteralevaluation_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedLiteralEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_tracedvalue_is_not_abstract():
    assert not inspect.isabstract(TracedValue)


def test_tracedvalue_constructor_exists():
    assert callable(TracedValue.__init__)


def test_tracedvalue_constructor_args():
    sig = inspect.signature(TracedValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::kernel::tracedprimitivevalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedPrimitiveValue)


def test_umltrace::kernel::tracedprimitivevalue_constructor_exists():
    assert callable(umlTrace::Kernel::TracedPrimitiveValue.__init__)


def test_umltrace::kernel::tracedprimitivevalue_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedPrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::kernel::tracedstructuredvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedStructuredValue)


def test_umltrace::kernel::tracedstructuredvalue_constructor_exists():
    assert callable(umlTrace::Kernel::TracedStructuredValue.__init__)


def test_umltrace::kernel::tracedstructuredvalue_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedStructuredValue.__init__)
    params = list(sig.parameters.keys())



def test_tracedstructuredvalue_is_not_abstract():
    assert not inspect.isabstract(TracedStructuredValue)


def test_tracedstructuredvalue_constructor_exists():
    assert callable(TracedStructuredValue.__init__)


def test_tracedstructuredvalue_constructor_args():
    sig = inspect.signature(TracedStructuredValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::kernel::tracedreference_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedReference)


def test_umltrace::kernel::tracedreference_constructor_exists():
    assert callable(umlTrace::Kernel::TracedReference.__init__)


def test_umltrace::kernel::tracedreference_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedReference.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::kernel::tracedcompoundvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedCompoundValue)


def test_umltrace::kernel::tracedcompoundvalue_constructor_exists():
    assert callable(umlTrace::Kernel::TracedCompoundValue.__init__)


def test_umltrace::kernel::tracedcompoundvalue_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedCompoundValue.__init__)
    params = list(sig.parameters.keys())



def test_tracedcompoundvalue_is_not_abstract():
    assert not inspect.isabstract(TracedCompoundValue)


def test_tracedcompoundvalue_constructor_exists():
    assert callable(TracedCompoundValue.__init__)


def test_tracedcompoundvalue_constructor_args():
    sig = inspect.signature(TracedCompoundValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::kernel::tracedextensionalvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedExtensionalValue)


def test_umltrace::kernel::tracedextensionalvalue_constructor_exists():
    assert callable(umlTrace::Kernel::TracedExtensionalValue.__init__)


def test_umltrace::kernel::tracedextensionalvalue_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedExtensionalValue.__init__)
    params = list(sig.parameters.keys())



def test_tracedextensionalvalue_is_not_abstract():
    assert not inspect.isabstract(TracedExtensionalValue)


def test_tracedextensionalvalue_constructor_exists():
    assert callable(TracedExtensionalValue.__init__)


def test_tracedextensionalvalue_constructor_args():
    sig = inspect.signature(TracedExtensionalValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::kernel::tracedobject_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedObject)


def test_umltrace::kernel::tracedobject_constructor_exists():
    assert callable(umlTrace::Kernel::TracedObject.__init__)


def test_umltrace::kernel::tracedobject_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedObject.__init__)
    params = list(sig.parameters.keys())



def test_tracedobject_is_not_abstract():
    assert not inspect.isabstract(TracedObject)


def test_tracedobject_constructor_exists():
    assert callable(TracedObject.__init__)


def test_tracedobject_constructor_args():
    sig = inspect.signature(TracedObject.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::basicbehaviors::tracedexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace::BasicBehaviors::TracedExecution)


def test_umltrace::basicbehaviors::tracedexecution_constructor_exists():
    assert callable(umlTrace::BasicBehaviors::TracedExecution.__init__)


def test_umltrace::basicbehaviors::tracedexecution_constructor_args():
    sig = inspect.signature(umlTrace::BasicBehaviors::TracedExecution.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedelement_is_not_abstract():
    assert not inspect.isabstract(uml::TracedElement)


def test_uml::tracedelement_constructor_exists():
    assert callable(uml::TracedElement.__init__)


def test_uml::tracedelement_constructor_args():
    sig = inspect.signature(uml::TracedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::values::semanticvisitor::runtimemodelelement::value_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Values::SemanticVisitor::runtimeModelElement::Value)


def test_umltrace::values::semanticvisitor::runtimemodelelement::value_constructor_exists():
    assert callable(umlTrace::Values::SemanticVisitor::runtimeModelElement::Value.__init__)


def test_umltrace::values::semanticvisitor::runtimemodelelement::value_constructor_args():
    sig = inspect.signature(umlTrace::Values::SemanticVisitor::runtimeModelElement::Value.__init__)
    params = list(sig.parameters.keys())



def test_tracedopaquebehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(TracedOpaqueBehaviorExecution)


def test_tracedopaquebehaviorexecution_constructor_exists():
    assert callable(TracedOpaqueBehaviorExecution.__init__)


def test_tracedopaquebehaviorexecution_constructor_args():
    sig = inspect.signature(TracedOpaqueBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::integerfunctions::tracedintegergreaterfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution)


def test_umltrace::integerfunctions::tracedintegergreaterfunctionbehaviorexecution_constructor_exists():
    assert callable(umlTrace::IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution.__init__)


def test_umltrace::integerfunctions::tracedintegergreaterfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(umlTrace::IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::integerfunctions::tracedintegerlessfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution)


def test_umltrace::integerfunctions::tracedintegerlessfunctionbehaviorexecution_constructor_exists():
    assert callable(umlTrace::IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution.__init__)


def test_umltrace::integerfunctions::tracedintegerlessfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(umlTrace::IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::integerfunctions::tracedintegerplusfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution)


def test_umltrace::integerfunctions::tracedintegerplusfunctionbehaviorexecution_constructor_exists():
    assert callable(umlTrace::IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution.__init__)


def test_umltrace::integerfunctions::tracedintegerplusfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(umlTrace::IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_tracedcallactionactivation_is_not_abstract():
    assert not inspect.isabstract(TracedCallActionActivation)


def test_tracedcallactionactivation_constructor_exists():
    assert callable(TracedCallActionActivation.__init__)


def test_tracedcallactionactivation_constructor_args():
    sig = inspect.signature(TracedCallActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::basicactions::tracedcallbehavioractionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::BasicActions::TracedCallBehaviorActionActivation)


def test_umltrace::basicactions::tracedcallbehavioractionactivation_constructor_exists():
    assert callable(umlTrace::BasicActions::TracedCallBehaviorActionActivation.__init__)


def test_umltrace::basicactions::tracedcallbehavioractionactivation_constructor_args():
    sig = inspect.signature(umlTrace::BasicActions::TracedCallBehaviorActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedpinactivation_is_not_abstract():
    assert not inspect.isabstract(TracedPinActivation)


def test_tracedpinactivation_constructor_exists():
    assert callable(TracedPinActivation.__init__)


def test_tracedpinactivation_constructor_args():
    sig = inspect.signature(TracedPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::basicactions::tracedoutputpinactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::BasicActions::TracedOutputPinActivation)


def test_umltrace::basicactions::tracedoutputpinactivation_constructor_exists():
    assert callable(umlTrace::BasicActions::TracedOutputPinActivation.__init__)


def test_umltrace::basicactions::tracedoutputpinactivation_constructor_args():
    sig = inspect.signature(umlTrace::BasicActions::TracedOutputPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::basicactions::tracedinputpinactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::BasicActions::TracedInputPinActivation)


def test_umltrace::basicactions::tracedinputpinactivation_constructor_exists():
    assert callable(umlTrace::BasicActions::TracedInputPinActivation.__init__)


def test_umltrace::basicactions::tracedinputpinactivation_constructor_args():
    sig = inspect.signature(umlTrace::BasicActions::TracedInputPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedinvocationactionactivation_is_not_abstract():
    assert not inspect.isabstract(TracedInvocationActionActivation)


def test_tracedinvocationactionactivation_constructor_exists():
    assert callable(TracedInvocationActionActivation.__init__)


def test_tracedinvocationactionactivation_constructor_args():
    sig = inspect.signature(TracedInvocationActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::basicactions::tracedcallactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::BasicActions::TracedCallActionActivation)


def test_umltrace::basicactions::tracedcallactionactivation_constructor_exists():
    assert callable(umlTrace::BasicActions::TracedCallActionActivation.__init__)


def test_umltrace::basicactions::tracedcallactionactivation_constructor_args():
    sig = inspect.signature(umlTrace::BasicActions::TracedCallActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedactionactivation_is_not_abstract():
    assert not inspect.isabstract(TracedActionActivation)


def test_tracedactionactivation_constructor_exists():
    assert callable(TracedActionActivation.__init__)


def test_tracedactionactivation_constructor_args():
    sig = inspect.signature(TracedActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::basicactions::tracedopaqueactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::BasicActions::TracedOpaqueActionActivation)


def test_umltrace::basicactions::tracedopaqueactionactivation_constructor_exists():
    assert callable(umlTrace::BasicActions::TracedOpaqueActionActivation.__init__)


def test_umltrace::basicactions::tracedopaqueactionactivation_constructor_args():
    sig = inspect.signature(umlTrace::BasicActions::TracedOpaqueActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::basicactions::tracedinvocationactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::BasicActions::TracedInvocationActionActivation)


def test_umltrace::basicactions::tracedinvocationactionactivation_constructor_exists():
    assert callable(umlTrace::BasicActions::TracedInvocationActionActivation.__init__)


def test_umltrace::basicactions::tracedinvocationactionactivation_constructor_args():
    sig = inspect.signature(umlTrace::BasicActions::TracedInvocationActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::loci::tracedsemanticvisitor_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Loci::TracedSemanticVisitor)


def test_umltrace::loci::tracedsemanticvisitor_constructor_exists():
    assert callable(umlTrace::Loci::TracedSemanticVisitor.__init__)


def test_umltrace::loci::tracedsemanticvisitor_constructor_args():
    sig = inspect.signature(umlTrace::Loci::TracedSemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_tracedobjectnodeactivation_is_not_abstract():
    assert not inspect.isabstract(TracedObjectNodeActivation)


def test_tracedobjectnodeactivation_constructor_exists():
    assert callable(TracedObjectNodeActivation.__init__)


def test_tracedobjectnodeactivation_constructor_args():
    sig = inspect.signature(TracedObjectNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::basicactions::tracedpinactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::BasicActions::TracedPinActivation)


def test_umltrace::basicactions::tracedpinactivation_constructor_exists():
    assert callable(umlTrace::BasicActions::TracedPinActivation.__init__)


def test_umltrace::basicactions::tracedpinactivation_constructor_args():
    sig = inspect.signature(umlTrace::BasicActions::TracedPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactivities::tracedactivityparameternodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActivities::TracedActivityParameterNodeActivation)


def test_umltrace::intermediateactivities::tracedactivityparameternodeactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActivities::TracedActivityParameterNodeActivation.__init__)


def test_umltrace::intermediateactivities::tracedactivityparameternodeactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActivities::TracedActivityParameterNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactions::tracedcreateobjectactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActions::TracedCreateObjectActionActivation)


def test_umltrace::intermediateactions::tracedcreateobjectactionactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActions::TracedCreateObjectActionActivation.__init__)


def test_umltrace::intermediateactions::tracedcreateobjectactionactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActions::TracedCreateObjectActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactions::tracedvaluespecificationactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActions::TracedValueSpecificationActionActivation)


def test_umltrace::intermediateactions::tracedvaluespecificationactionactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActions::TracedValueSpecificationActionActivation.__init__)


def test_umltrace::intermediateactions::tracedvaluespecificationactionactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActions::TracedValueSpecificationActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedwritestructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(TracedWriteStructuralFeatureActionActivation)


def test_tracedwritestructuralfeatureactionactivation_constructor_exists():
    assert callable(TracedWriteStructuralFeatureActionActivation.__init__)


def test_tracedwritestructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(TracedWriteStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactions::tracedaddstructuralfeaturevalueactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActions::TracedAddStructuralFeatureValueActionActivation)


def test_umltrace::intermediateactions::tracedaddstructuralfeaturevalueactionactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActions::TracedAddStructuralFeatureValueActionActivation.__init__)


def test_umltrace::intermediateactions::tracedaddstructuralfeaturevalueactionactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActions::TracedAddStructuralFeatureValueActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedstructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(TracedStructuralFeatureActionActivation)


def test_tracedstructuralfeatureactionactivation_constructor_exists():
    assert callable(TracedStructuralFeatureActionActivation.__init__)


def test_tracedstructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(TracedStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactions::tracedwritestructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActions::TracedWriteStructuralFeatureActionActivation)


def test_umltrace::intermediateactions::tracedwritestructuralfeatureactionactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActions::TracedWriteStructuralFeatureActionActivation.__init__)


def test_umltrace::intermediateactions::tracedwritestructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActions::TracedWriteStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactions::tracedreadstructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActions::TracedReadStructuralFeatureActionActivation)


def test_umltrace::intermediateactions::tracedreadstructuralfeatureactionactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActions::TracedReadStructuralFeatureActionActivation.__init__)


def test_umltrace::intermediateactions::tracedreadstructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActions::TracedReadStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactions::tracedstructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActions::TracedStructuralFeatureActionActivation)


def test_umltrace::intermediateactions::tracedstructuralfeatureactionactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActions::TracedStructuralFeatureActionActivation.__init__)


def test_umltrace::intermediateactions::tracedstructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActions::TracedStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::ecore::tracedemodelelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace::ecore::TracedEModelElement)


def test_umltrace::ecore::tracedemodelelement_constructor_exists():
    assert callable(umlTrace::ecore::TracedEModelElement.__init__)


def test_umltrace::ecore::tracedemodelelement_constructor_args():
    sig = inspect.signature(umlTrace::ecore::TracedEModelElement.__init__)
    params = list(sig.parameters.keys())



def test_tracedmessageend_is_not_abstract():
    assert not inspect.isabstract(TracedMessageEnd)


def test_tracedmessageend_constructor_exists():
    assert callable(TracedMessageEnd.__init__)


def test_tracedmessageend_constructor_args():
    sig = inspect.signature(TracedMessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedgate_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedGate)


def test_umltrace::uml::tracedgate_constructor_exists():
    assert callable(umlTrace::uml::TracedGate.__init__)


def test_umltrace::uml::tracedgate_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedGate.__init__)
    params = list(sig.parameters.keys())



def test_tracedexecution_is_not_abstract():
    assert not inspect.isabstract(TracedExecution)


def test_tracedexecution_constructor_exists():
    assert callable(TracedExecution.__init__)


def test_tracedexecution_constructor_args():
    sig = inspect.signature(TracedExecution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::basicbehaviors::tracedopaquebehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace::BasicBehaviors::TracedOpaqueBehaviorExecution)


def test_umltrace::basicbehaviors::tracedopaquebehaviorexecution_constructor_exists():
    assert callable(umlTrace::BasicBehaviors::TracedOpaqueBehaviorExecution.__init__)


def test_umltrace::basicbehaviors::tracedopaquebehaviorexecution_constructor_args():
    sig = inspect.signature(umlTrace::BasicBehaviors::TracedOpaqueBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_tracedexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(TracedExecutionSpecification)


def test_tracedexecutionspecification_constructor_exists():
    assert callable(TracedExecutionSpecification.__init__)


def test_tracedexecutionspecification_constructor_args():
    sig = inspect.signature(TracedExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedbehaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedBehaviorExecutionSpecification)


def test_umltrace::uml::tracedbehaviorexecutionspecification_constructor_exists():
    assert callable(umlTrace::uml::TracedBehaviorExecutionSpecification.__init__)


def test_umltrace::uml::tracedbehaviorexecutionspecification_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedBehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_tracedoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(TracedOccurrenceSpecification)


def test_tracedoccurrencespecification_constructor_exists():
    assert callable(TracedOccurrenceSpecification.__init__)


def test_tracedoccurrencespecification_constructor_args():
    sig = inspect.signature(TracedOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedexecutionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedExecutionOccurrenceSpecification)


def test_umltrace::uml::tracedexecutionoccurrencespecification_constructor_exists():
    assert callable(umlTrace::uml::TracedExecutionOccurrenceSpecification.__init__)


def test_umltrace::uml::tracedexecutionoccurrencespecification_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_tracedopaquebehavior_is_not_abstract():
    assert not inspect.isabstract(TracedOpaqueBehavior)


def test_tracedopaquebehavior_constructor_exists():
    assert callable(TracedOpaqueBehavior.__init__)


def test_tracedopaquebehavior_constructor_args():
    sig = inspect.signature(TracedOpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedfunctionbehavior_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedFunctionBehavior)


def test_umltrace::uml::tracedfunctionbehavior_constructor_exists():
    assert callable(umlTrace::uml::TracedFunctionBehavior.__init__)


def test_umltrace::uml::tracedfunctionbehavior_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedFunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedstructuredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml::TracedStructuredClassifier)


def test_uml::tracedstructuredclassifier_constructor_exists():
    assert callable(uml::TracedStructuredClassifier.__init__)


def test_uml::tracedstructuredclassifier_constructor_args():
    sig = inspect.signature(uml::TracedStructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_tracedmultiplicityelement_is_not_abstract():
    assert not inspect.isabstract(TracedMultiplicityElement)


def test_tracedmultiplicityelement_constructor_exists():
    assert callable(TracedMultiplicityElement.__init__)


def test_tracedmultiplicityelement_constructor_args():
    sig = inspect.signature(TracedMultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedconnectorend_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedConnectorEnd)


def test_umltrace::uml::tracedconnectorend_constructor_exists():
    assert callable(umlTrace::uml::TracedConnectorEnd.__init__)


def test_umltrace::uml::tracedconnectorend_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedactionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedActionExecutionSpecification)


def test_umltrace::uml::tracedactionexecutionspecification_constructor_exists():
    assert callable(umlTrace::uml::TracedActionExecutionSpecification.__init__)


def test_umltrace::uml::tracedactionexecutionspecification_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_tracedobjectnode_is_not_abstract():
    assert not inspect.isabstract(TracedObjectNode)


def test_tracedobjectnode_constructor_exists():
    assert callable(TracedObjectNode.__init__)


def test_tracedobjectnode_constructor_args():
    sig = inspect.signature(TracedObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedexpansionnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedExpansionNode)


def test_umltrace::uml::tracedexpansionnode_constructor_exists():
    assert callable(umlTrace::uml::TracedExpansionNode.__init__)


def test_umltrace::uml::tracedexpansionnode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedactivityparameternode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedActivityParameterNode)


def test_umltrace::uml::tracedactivityparameternode_constructor_exists():
    assert callable(umlTrace::uml::TracedActivityParameterNode.__init__)


def test_umltrace::uml::tracedactivityparameternode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcentralbuffernode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedCentralBufferNode)


def test_umltrace::uml::tracedcentralbuffernode_constructor_exists():
    assert callable(umlTrace::uml::TracedCentralBufferNode.__init__)


def test_umltrace::uml::tracedcentralbuffernode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedCentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedcentralbuffernode_is_not_abstract():
    assert not inspect.isabstract(TracedCentralBufferNode)


def test_tracedcentralbuffernode_constructor_exists():
    assert callable(TracedCentralBufferNode.__init__)


def test_tracedcentralbuffernode_constructor_args():
    sig = inspect.signature(TracedCentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddatastorenode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDataStoreNode)


def test_umltrace::uml::traceddatastorenode_constructor_exists():
    assert callable(umlTrace::uml::TracedDataStoreNode.__init__)


def test_umltrace::uml::traceddatastorenode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_traceddatatype_is_not_abstract():
    assert not inspect.isabstract(TracedDataType)


def test_traceddatatype_constructor_exists():
    assert callable(TracedDataType.__init__)


def test_traceddatatype_constructor_args():
    sig = inspect.signature(TracedDataType.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedenumeration_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedEnumeration)


def test_umltrace::uml::tracedenumeration_constructor_exists():
    assert callable(umlTrace::uml::TracedEnumeration.__init__)


def test_umltrace::uml::tracedenumeration_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedprimitivetype_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedPrimitiveType)


def test_umltrace::uml::tracedprimitivetype_constructor_exists():
    assert callable(umlTrace::uml::TracedPrimitiveType.__init__)


def test_umltrace::uml::tracedprimitivetype_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_tracedmessageevent_is_not_abstract():
    assert not inspect.isabstract(TracedMessageEvent)


def test_tracedmessageevent_constructor_exists():
    assert callable(TracedMessageEvent.__init__)


def test_tracedmessageevent_constructor_args():
    sig = inspect.signature(TracedMessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcallevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedCallEvent)


def test_umltrace::uml::tracedcallevent_constructor_exists():
    assert callable(umlTrace::uml::TracedCallEvent.__init__)


def test_umltrace::uml::tracedcallevent_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedCallEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedanyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedAnyReceiveEvent)


def test_umltrace::uml::tracedanyreceiveevent_constructor_exists():
    assert callable(umlTrace::uml::TracedAnyReceiveEvent.__init__)


def test_umltrace::uml::tracedanyreceiveevent_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedAnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedbehavioralfeature_is_not_abstract():
    assert not inspect.isabstract(uml::TracedBehavioralFeature)


def test_uml::tracedbehavioralfeature_constructor_exists():
    assert callable(uml::TracedBehavioralFeature.__init__)


def test_uml::tracedbehavioralfeature_constructor_args():
    sig = inspect.signature(uml::TracedBehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_tracedtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(TracedTemplateParameter)


def test_tracedtemplateparameter_constructor_exists():
    assert callable(TracedTemplateParameter.__init__)


def test_tracedtemplateparameter_constructor_args():
    sig = inspect.signature(TracedTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedconnectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedConnectableElementTemplateParameter)


def test_umltrace::uml::tracedconnectableelementtemplateparameter_constructor_exists():
    assert callable(umlTrace::uml::TracedConnectableElementTemplateParameter.__init__)


def test_umltrace::uml::tracedconnectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedclassifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedClassifierTemplateParameter)


def test_umltrace::uml::tracedclassifiertemplateparameter_constructor_exists():
    assert callable(umlTrace::uml::TracedClassifierTemplateParameter.__init__)


def test_umltrace::uml::tracedclassifiertemplateparameter_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_tracedpackage_is_not_abstract():
    assert not inspect.isabstract(TracedPackage)


def test_tracedpackage_constructor_exists():
    assert callable(TracedPackage.__init__)


def test_tracedpackage_constructor_args():
    sig = inspect.signature(TracedPackage.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedprofile_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedProfile)


def test_umltrace::uml::tracedprofile_constructor_exists():
    assert callable(umlTrace::uml::TracedProfile.__init__)


def test_umltrace::uml::tracedprofile_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedProfile.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedmodel_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedModel)


def test_umltrace::uml::tracedmodel_constructor_exists():
    assert callable(umlTrace::uml::TracedModel.__init__)


def test_umltrace::uml::tracedmodel_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedModel.__init__)
    params = list(sig.parameters.keys())



def test_tracedtransition_is_not_abstract():
    assert not inspect.isabstract(TracedTransition)


def test_tracedtransition_constructor_exists():
    assert callable(TracedTransition.__init__)


def test_tracedtransition_constructor_args():
    sig = inspect.signature(TracedTransition.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedprotocoltransition_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedProtocolTransition)


def test_umltrace::uml::tracedprotocoltransition_constructor_exists():
    assert callable(umlTrace::uml::TracedProtocolTransition.__init__)


def test_umltrace::uml::tracedprotocoltransition_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_tracedwritevariableaction_is_not_abstract():
    assert not inspect.isabstract(TracedWriteVariableAction)


def test_tracedwritevariableaction_constructor_exists():
    assert callable(TracedWriteVariableAction.__init__)


def test_tracedwritevariableaction_constructor_args():
    sig = inspect.signature(TracedWriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedremovevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedRemoveVariableValueAction)


def test_umltrace::uml::tracedremovevariablevalueaction_constructor_exists():
    assert callable(umlTrace::uml::TracedRemoveVariableValueAction.__init__)


def test_umltrace::uml::tracedremovevariablevalueaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedRemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedaddvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedAddVariableValueAction)


def test_umltrace::uml::tracedaddvariablevalueaction_constructor_exists():
    assert callable(umlTrace::uml::TracedAddVariableValueAction.__init__)


def test_umltrace::uml::tracedaddvariablevalueaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedAddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedinteractionuse_is_not_abstract():
    assert not inspect.isabstract(TracedInteractionUse)


def test_tracedinteractionuse_constructor_exists():
    assert callable(TracedInteractionUse.__init__)


def test_tracedinteractionuse_constructor_args():
    sig = inspect.signature(TracedInteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedpartdecomposition_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedPartDecomposition)


def test_umltrace::uml::tracedpartdecomposition_constructor_exists():
    assert callable(umlTrace::uml::TracedPartDecomposition.__init__)


def test_umltrace::uml::tracedpartdecomposition_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedPartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_tracedobservation_is_not_abstract():
    assert not inspect.isabstract(TracedObservation)


def test_tracedobservation_constructor_exists():
    assert callable(TracedObservation.__init__)


def test_tracedobservation_constructor_args():
    sig = inspect.signature(TracedObservation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtimeobservation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTimeObservation)


def test_umltrace::uml::tracedtimeobservation_constructor_exists():
    assert callable(umlTrace::uml::TracedTimeObservation.__init__)


def test_umltrace::uml::tracedtimeobservation_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTimeObservation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddurationobservation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDurationObservation)


def test_umltrace::uml::traceddurationobservation_constructor_exists():
    assert callable(umlTrace::uml::TracedDurationObservation.__init__)


def test_umltrace::uml::traceddurationobservation_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDurationObservation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedoperationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedOperationTemplateParameter)


def test_umltrace::uml::tracedoperationtemplateparameter_constructor_exists():
    assert callable(umlTrace::uml::TracedOperationTemplateParameter.__init__)


def test_umltrace::uml::tracedoperationtemplateparameter_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedOperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_tracedinterval_is_not_abstract():
    assert not inspect.isabstract(TracedInterval)


def test_tracedinterval_constructor_exists():
    assert callable(TracedInterval.__init__)


def test_tracedinterval_constructor_args():
    sig = inspect.signature(TracedInterval.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddurationinterval_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDurationInterval)


def test_umltrace::uml::traceddurationinterval_constructor_exists():
    assert callable(umlTrace::uml::TracedDurationInterval.__init__)


def test_umltrace::uml::traceddurationinterval_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtimeinterval_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTimeInterval)


def test_umltrace::uml::tracedtimeinterval_constructor_exists():
    assert callable(umlTrace::uml::TracedTimeInterval.__init__)


def test_umltrace::uml::tracedtimeinterval_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedsignalevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedSignalEvent)


def test_umltrace::uml::tracedsignalevent_constructor_exists():
    assert callable(umlTrace::uml::TracedSignalEvent.__init__)


def test_umltrace::uml::tracedsignalevent_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_tracedbehavioralfeature_is_not_abstract():
    assert not inspect.isabstract(TracedBehavioralFeature)


def test_tracedbehavioralfeature_constructor_exists():
    assert callable(TracedBehavioralFeature.__init__)


def test_tracedbehavioralfeature_constructor_args():
    sig = inspect.signature(TracedBehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedreception_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedReception)


def test_umltrace::uml::tracedreception_constructor_exists():
    assert callable(umlTrace::uml::TracedReception.__init__)


def test_umltrace::uml::tracedreception_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedReception.__init__)
    params = list(sig.parameters.keys())



def test_traceddependency_is_not_abstract():
    assert not inspect.isabstract(TracedDependency)


def test_traceddependency_constructor_exists():
    assert callable(TracedDependency.__init__)


def test_traceddependency_constructor_args():
    sig = inspect.signature(TracedDependency.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedusage_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedUsage)


def test_umltrace::uml::tracedusage_constructor_exists():
    assert callable(umlTrace::uml::TracedUsage.__init__)


def test_umltrace::uml::tracedusage_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedUsage.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedabstraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedAbstraction)


def test_umltrace::uml::tracedabstraction_constructor_exists():
    assert callable(umlTrace::uml::TracedAbstraction.__init__)


def test_umltrace::uml::tracedabstraction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedAbstraction.__init__)
    params = list(sig.parameters.keys())



def test_tracedabstraction_is_not_abstract():
    assert not inspect.isabstract(TracedAbstraction)


def test_tracedabstraction_constructor_exists():
    assert callable(TracedAbstraction.__init__)


def test_tracedabstraction_constructor_args():
    sig = inspect.signature(TracedAbstraction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedmanifestation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedManifestation)


def test_umltrace::uml::tracedmanifestation_constructor_exists():
    assert callable(umlTrace::uml::TracedManifestation.__init__)


def test_umltrace::uml::tracedmanifestation_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedManifestation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedrealization_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedRealization)


def test_umltrace::uml::tracedrealization_constructor_exists():
    assert callable(umlTrace::uml::TracedRealization.__init__)


def test_umltrace::uml::tracedrealization_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedRealization.__init__)
    params = list(sig.parameters.keys())



def test_tracedrealization_is_not_abstract():
    assert not inspect.isabstract(TracedRealization)


def test_tracedrealization_constructor_exists():
    assert callable(TracedRealization.__init__)


def test_tracedrealization_constructor_args():
    sig = inspect.signature(TracedRealization.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcomponentrealization_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedComponentRealization)


def test_umltrace::uml::tracedcomponentrealization_constructor_exists():
    assert callable(umlTrace::uml::TracedComponentRealization.__init__)


def test_umltrace::uml::tracedcomponentrealization_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinterfacerealization_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInterfaceRealization)


def test_umltrace::uml::tracedinterfacerealization_constructor_exists():
    assert callable(umlTrace::uml::TracedInterfaceRealization.__init__)


def test_umltrace::uml::tracedinterfacerealization_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedsubstitution_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedSubstitution)


def test_umltrace::uml::tracedsubstitution_constructor_exists():
    assert callable(umlTrace::uml::TracedSubstitution.__init__)


def test_umltrace::uml::tracedsubstitution_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_tracedinstancespecification_is_not_abstract():
    assert not inspect.isabstract(TracedInstanceSpecification)


def test_tracedinstancespecification_constructor_exists():
    assert callable(TracedInstanceSpecification.__init__)


def test_tracedinstancespecification_constructor_args():
    sig = inspect.signature(TracedInstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedenumerationliteral_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedEnumerationLiteral)


def test_umltrace::uml::tracedenumerationliteral_constructor_exists():
    assert callable(umlTrace::uml::TracedEnumerationLiteral.__init__)


def test_umltrace::uml::tracedenumerationliteral_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedEnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_tracedaccepteventaction_is_not_abstract():
    assert not inspect.isabstract(TracedAcceptEventAction)


def test_tracedaccepteventaction_constructor_exists():
    assert callable(TracedAcceptEventAction.__init__)


def test_tracedaccepteventaction_constructor_args():
    sig = inspect.signature(TracedAcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedacceptcallaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedAcceptCallAction)


def test_umltrace::uml::tracedacceptcallaction_constructor_exists():
    assert callable(umlTrace::uml::TracedAcceptCallAction.__init__)


def test_umltrace::uml::tracedacceptcallaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedAcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedlinkenddata_is_not_abstract():
    assert not inspect.isabstract(TracedLinkEndData)


def test_tracedlinkenddata_constructor_exists():
    assert callable(TracedLinkEndData.__init__)


def test_tracedlinkenddata_constructor_args():
    sig = inspect.signature(TracedLinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedlinkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLinkEndCreationData)


def test_umltrace::uml::tracedlinkendcreationdata_constructor_exists():
    assert callable(umlTrace::uml::TracedLinkEndCreationData.__init__)


def test_umltrace::uml::tracedlinkendcreationdata_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLinkEndCreationData.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedlinkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLinkEndDestructionData)


def test_umltrace::uml::tracedlinkenddestructiondata_constructor_exists():
    assert callable(umlTrace::uml::TracedLinkEndDestructionData.__init__)


def test_umltrace::uml::tracedlinkenddestructiondata_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())



def test_tracedclass_is_not_abstract():
    assert not inspect.isabstract(TracedClass)


def test_tracedclass_constructor_exists():
    assert callable(TracedClass.__init__)


def test_tracedclass_constructor_args():
    sig = inspect.signature(TracedClass.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcomponent_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedComponent)


def test_umltrace::uml::tracedcomponent_constructor_exists():
    assert callable(umlTrace::uml::TracedComponent.__init__)


def test_umltrace::uml::tracedcomponent_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedComponent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedstereotype_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedStereotype)


def test_umltrace::uml::tracedstereotype_constructor_exists():
    assert callable(umlTrace::uml::TracedStereotype.__init__)


def test_umltrace::uml::tracedstereotype_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedStereotype.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedbehavior_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedBehavior)


def test_umltrace::uml::tracedbehavior_constructor_exists():
    assert callable(umlTrace::uml::TracedBehavior.__init__)


def test_umltrace::uml::tracedbehavior_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedBehavior.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinteractionfragment_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInteractionFragment)


def test_uml::tracedinteractionfragment_constructor_exists():
    assert callable(uml::TracedInteractionFragment.__init__)


def test_uml::tracedinteractionfragment_constructor_args():
    sig = inspect.signature(uml::TracedInteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedbehavior_is_not_abstract():
    assert not inspect.isabstract(uml::TracedBehavior)


def test_uml::tracedbehavior_constructor_exists():
    assert callable(uml::TracedBehavior.__init__)


def test_uml::tracedbehavior_constructor_args():
    sig = inspect.signature(uml::TracedBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinteraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInteraction)


def test_umltrace::uml::tracedinteraction_constructor_exists():
    assert callable(umlTrace::uml::TracedInteraction.__init__)


def test_umltrace::uml::tracedinteraction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInteraction.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(TracedActivityEdge)


def test_tracedactivityedge_constructor_exists():
    assert callable(TracedActivityEdge.__init__)


def test_tracedactivityedge_constructor_args():
    sig = inspect.signature(TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcontrolflow_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedControlFlow)


def test_umltrace::uml::tracedcontrolflow_constructor_exists():
    assert callable(umlTrace::uml::TracedControlFlow.__init__)


def test_umltrace::uml::tracedcontrolflow_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedobjectflow_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedObjectFlow)


def test_umltrace::uml::tracedobjectflow_constructor_exists():
    assert callable(umlTrace::uml::TracedObjectFlow.__init__)


def test_umltrace::uml::tracedobjectflow_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_tracedstatemachine_is_not_abstract():
    assert not inspect.isabstract(TracedStateMachine)


def test_tracedstatemachine_constructor_exists():
    assert callable(TracedStateMachine.__init__)


def test_tracedstatemachine_constructor_args():
    sig = inspect.signature(TracedStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedprotocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedProtocolStateMachine)


def test_umltrace::uml::tracedprotocolstatemachine_constructor_exists():
    assert callable(umlTrace::uml::TracedProtocolStateMachine.__init__)


def test_umltrace::uml::tracedprotocolstatemachine_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddeployment_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDeployment)


def test_umltrace::uml::traceddeployment_constructor_exists():
    assert callable(umlTrace::uml::TracedDeployment.__init__)


def test_umltrace::uml::traceddeployment_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDeployment.__init__)
    params = list(sig.parameters.keys())



def test_tracedbehavior_is_not_abstract():
    assert not inspect.isabstract(TracedBehavior)


def test_tracedbehavior_constructor_exists():
    assert callable(TracedBehavior.__init__)


def test_tracedbehavior_constructor_args():
    sig = inspect.signature(TracedBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedopaquebehavior_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedOpaqueBehavior)


def test_umltrace::uml::tracedopaquebehavior_constructor_exists():
    assert callable(umlTrace::uml::TracedOpaqueBehavior.__init__)


def test_umltrace::uml::tracedopaquebehavior_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedOpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedactivity_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedActivity)


def test_umltrace::uml::tracedactivity_constructor_exists():
    assert callable(umlTrace::uml::TracedActivity.__init__)


def test_umltrace::uml::tracedactivity_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedActivity.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedstatemachine_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedStateMachine)


def test_umltrace::uml::tracedstatemachine_constructor_exists():
    assert callable(umlTrace::uml::TracedStateMachine.__init__)


def test_umltrace::uml::tracedstatemachine_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivitygroup_is_not_abstract():
    assert not inspect.isabstract(TracedActivityGroup)


def test_tracedactivitygroup_constructor_exists():
    assert callable(TracedActivityGroup.__init__)


def test_tracedactivitygroup_constructor_args():
    sig = inspect.signature(TracedActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinterruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInterruptibleActivityRegion)


def test_umltrace::uml::tracedinterruptibleactivityregion_constructor_exists():
    assert callable(umlTrace::uml::TracedInterruptibleActivityRegion.__init__)


def test_umltrace::uml::tracedinterruptibleactivityregion_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedactivitypartition_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedActivityPartition)


def test_umltrace::uml::tracedactivitypartition_constructor_exists():
    assert callable(umlTrace::uml::TracedActivityPartition.__init__)


def test_umltrace::uml::tracedactivitypartition_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedrelationship_is_not_abstract():
    assert not inspect.isabstract(uml::TracedRelationship)


def test_uml::tracedrelationship_constructor_exists():
    assert callable(uml::TracedRelationship.__init__)


def test_uml::tracedrelationship_constructor_args():
    sig = inspect.signature(uml::TracedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactivities::tracedactivityexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActivities::TracedActivityExecution)


def test_umltrace::intermediateactivities::tracedactivityexecution_constructor_exists():
    assert callable(umlTrace::IntermediateActivities::TracedActivityExecution.__init__)


def test_umltrace::intermediateactivities::tracedactivityexecution_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActivities::TracedActivityExecution.__init__)
    params = list(sig.parameters.keys())



def test_tracedsemanticvisitor_is_not_abstract():
    assert not inspect.isabstract(TracedSemanticVisitor)


def test_tracedsemanticvisitor_constructor_exists():
    assert callable(TracedSemanticVisitor.__init__)


def test_tracedsemanticvisitor_constructor_args():
    sig = inspect.signature(TracedSemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::kernel::tracedevaluation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedEvaluation)


def test_umltrace::kernel::tracedevaluation_constructor_exists():
    assert callable(umlTrace::Kernel::TracedEvaluation.__init__)


def test_umltrace::kernel::tracedevaluation_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::kernel::tracedvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Kernel::TracedValue)


def test_umltrace::kernel::tracedvalue_constructor_exists():
    assert callable(umlTrace::Kernel::TracedValue.__init__)


def test_umltrace::kernel::tracedvalue_constructor_args():
    sig = inspect.signature(umlTrace::Kernel::TracedValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactivities::tracedactivitynodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActivities::TracedActivityNodeActivation)


def test_umltrace::intermediateactivities::tracedactivitynodeactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActivities::TracedActivityNodeActivation.__init__)


def test_umltrace::intermediateactivities::tracedactivitynodeactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActivities::TracedActivityNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivitynodeactivation_is_not_abstract():
    assert not inspect.isabstract(TracedActivityNodeActivation)


def test_tracedactivitynodeactivation_constructor_exists():
    assert callable(TracedActivityNodeActivation.__init__)


def test_tracedactivitynodeactivation_constructor_args():
    sig = inspect.signature(TracedActivityNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::basicactions::tracedactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::BasicActions::TracedActionActivation)


def test_umltrace::basicactions::tracedactionactivation_constructor_exists():
    assert callable(umlTrace::BasicActions::TracedActionActivation.__init__)


def test_umltrace::basicactions::tracedactionactivation_constructor_args():
    sig = inspect.signature(umlTrace::BasicActions::TracedActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactivities::tracedobjectnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActivities::TracedObjectNodeActivation)


def test_umltrace::intermediateactivities::tracedobjectnodeactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActivities::TracedObjectNodeActivation.__init__)


def test_umltrace::intermediateactivities::tracedobjectnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActivities::TracedObjectNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactivities::tracedcontrolnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActivities::TracedControlNodeActivation)


def test_umltrace::intermediateactivities::tracedcontrolnodeactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActivities::TracedControlNodeActivation.__init__)


def test_umltrace::intermediateactivities::tracedcontrolnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActivities::TracedControlNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedcontrolnodeactivation_is_not_abstract():
    assert not inspect.isabstract(TracedControlNodeActivation)


def test_tracedcontrolnodeactivation_constructor_exists():
    assert callable(TracedControlNodeActivation.__init__)


def test_tracedcontrolnodeactivation_constructor_args():
    sig = inspect.signature(TracedControlNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactivities::tracedinitialnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActivities::TracedInitialNodeActivation)


def test_umltrace::intermediateactivities::tracedinitialnodeactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActivities::TracedInitialNodeActivation.__init__)


def test_umltrace::intermediateactivities::tracedinitialnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActivities::TracedInitialNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactivities::tracedactivityfinalnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActivities::TracedActivityFinalNodeActivation)


def test_umltrace::intermediateactivities::tracedactivityfinalnodeactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActivities::TracedActivityFinalNodeActivation.__init__)


def test_umltrace::intermediateactivities::tracedactivityfinalnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActivities::TracedActivityFinalNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactivities::traceddecisionnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActivities::TracedDecisionNodeActivation)


def test_umltrace::intermediateactivities::traceddecisionnodeactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActivities::TracedDecisionNodeActivation.__init__)


def test_umltrace::intermediateactivities::traceddecisionnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActivities::TracedDecisionNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactivities::tracedjoinnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActivities::TracedJoinNodeActivation)


def test_umltrace::intermediateactivities::tracedjoinnodeactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActivities::TracedJoinNodeActivation.__init__)


def test_umltrace::intermediateactivities::tracedjoinnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActivities::TracedJoinNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactivities::tracedmergenodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActivities::TracedMergeNodeActivation)


def test_umltrace::intermediateactivities::tracedmergenodeactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActivities::TracedMergeNodeActivation.__init__)


def test_umltrace::intermediateactivities::tracedmergenodeactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActivities::TracedMergeNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::intermediateactivities::tracedforknodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::IntermediateActivities::TracedForkNodeActivation)


def test_umltrace::intermediateactivities::tracedforknodeactivation_constructor_exists():
    assert callable(umlTrace::IntermediateActivities::TracedForkNodeActivation.__init__)


def test_umltrace::intermediateactivities::tracedforknodeactivation_constructor_args():
    sig = inspect.signature(umlTrace::IntermediateActivities::TracedForkNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedvertex_is_not_abstract():
    assert not inspect.isabstract(uml::TracedVertex)


def test_uml::tracedvertex_constructor_exists():
    assert callable(uml::TracedVertex.__init__)


def test_uml::tracedvertex_constructor_args():
    sig = inspect.signature(uml::TracedVertex.__init__)
    params = list(sig.parameters.keys())



def test_tracedstate_is_not_abstract():
    assert not inspect.isabstract(TracedState)


def test_tracedstate_constructor_exists():
    assert callable(TracedState.__init__)


def test_tracedstate_constructor_args():
    sig = inspect.signature(TracedState.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedfinalstate_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedFinalState)


def test_umltrace::uml::tracedfinalstate_constructor_exists():
    assert callable(umlTrace::uml::TracedFinalState.__init__)


def test_umltrace::uml::tracedfinalstate_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedFinalState.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedactivityfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedActivityFinalNode)


def test_uml::tracedactivityfinalnode_constructor_exists():
    assert callable(uml::TracedActivityFinalNode.__init__)


def test_uml::tracedactivityfinalnode_constructor_args():
    sig = inspect.signature(uml::TracedActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedclassifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml::TracedClassifierTemplateParameter)


def test_uml::tracedclassifiertemplateparameter_constructor_exists():
    assert callable(uml::TracedClassifierTemplateParameter.__init__)


def test_uml::tracedclassifiertemplateparameter_constructor_args():
    sig = inspect.signature(uml::TracedClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_tracedinteractionfragment_is_not_abstract():
    assert not inspect.isabstract(TracedInteractionFragment)


def test_tracedinteractionfragment_constructor_exists():
    assert callable(TracedInteractionFragment.__init__)


def test_tracedinteractionfragment_constructor_args():
    sig = inspect.signature(TracedInteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedstateinvariant_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedStateInvariant)


def test_umltrace::uml::tracedstateinvariant_constructor_exists():
    assert callable(umlTrace::uml::TracedStateInvariant.__init__)


def test_umltrace::uml::tracedstateinvariant_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedStateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedExecutionSpecification)


def test_umltrace::uml::tracedexecutionspecification_constructor_exists():
    assert callable(umlTrace::uml::TracedExecutionSpecification.__init__)


def test_umltrace::uml::tracedexecutionspecification_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcombinedfragment_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedCombinedFragment)


def test_umltrace::uml::tracedcombinedfragment_constructor_exists():
    assert callable(umlTrace::uml::TracedCombinedFragment.__init__)


def test_umltrace::uml::tracedcombinedfragment_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedCombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedgeneralordering_is_not_abstract():
    assert not inspect.isabstract(uml::TracedGeneralOrdering)


def test_uml::tracedgeneralordering_constructor_exists():
    assert callable(uml::TracedGeneralOrdering.__init__)


def test_uml::tracedgeneralordering_constructor_args():
    sig = inspect.signature(uml::TracedGeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedelementimport_is_not_abstract():
    assert not inspect.isabstract(uml::TracedElementImport)


def test_uml::tracedelementimport_constructor_exists():
    assert callable(uml::TracedElementImport.__init__)


def test_uml::tracedelementimport_constructor_args():
    sig = inspect.signature(uml::TracedElementImport.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedmergenode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedMergeNode)


def test_uml::tracedmergenode_constructor_exists():
    assert callable(uml::TracedMergeNode.__init__)


def test_uml::tracedmergenode_constructor_args():
    sig = inspect.signature(uml::TracedMergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedclearassociationaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedClearAssociationAction)


def test_uml::tracedclearassociationaction_constructor_exists():
    assert callable(uml::TracedClearAssociationAction.__init__)


def test_uml::tracedclearassociationaction_constructor_args():
    sig = inspect.signature(uml::TracedClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedlinkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(uml::TracedLinkEndCreationData)


def test_uml::tracedlinkendcreationdata_constructor_exists():
    assert callable(uml::TracedLinkEndCreationData.__init__)


def test_uml::tracedlinkendcreationdata_constructor_args():
    sig = inspect.signature(uml::TracedLinkEndCreationData.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedpseudostate_is_not_abstract():
    assert not inspect.isabstract(uml::TracedPseudostate)


def test_uml::tracedpseudostate_constructor_exists():
    assert callable(uml::TracedPseudostate.__init__)


def test_uml::tracedpseudostate_constructor_args():
    sig = inspect.signature(uml::TracedPseudostate.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcomponent_is_not_abstract():
    assert not inspect.isabstract(uml::TracedComponent)


def test_uml::tracedcomponent_constructor_exists():
    assert callable(uml::TracedComponent.__init__)


def test_uml::tracedcomponent_constructor_args():
    sig = inspect.signature(uml::TracedComponent.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedreadisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedReadIsClassifiedObjectAction)


def test_uml::tracedreadisclassifiedobjectaction_constructor_exists():
    assert callable(uml::TracedReadIsClassifiedObjectAction.__init__)


def test_uml::tracedreadisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(uml::TracedReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedabstraction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedAbstraction)


def test_uml::tracedabstraction_constructor_exists():
    assert callable(uml::TracedAbstraction.__init__)


def test_uml::tracedabstraction_constructor_args():
    sig = inspect.signature(uml::TracedAbstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtimeexpression_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTimeExpression)


def test_uml::tracedtimeexpression_constructor_exists():
    assert callable(uml::TracedTimeExpression.__init__)


def test_uml::tracedtimeexpression_constructor_args():
    sig = inspect.signature(uml::TracedTimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedvaluespecificationaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedValueSpecificationAction)


def test_uml::tracedvaluespecificationaction_constructor_exists():
    assert callable(uml::TracedValueSpecificationAction.__init__)


def test_uml::tracedvaluespecificationaction_constructor_args():
    sig = inspect.signature(uml::TracedValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedfunctionbehavior_is_not_abstract():
    assert not inspect.isabstract(uml::TracedFunctionBehavior)


def test_uml::tracedfunctionbehavior_constructor_exists():
    assert callable(uml::TracedFunctionBehavior.__init__)


def test_uml::tracedfunctionbehavior_constructor_args():
    sig = inspect.signature(uml::TracedFunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_integerfunctions::tracedintegergreaterfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution)


def test_integerfunctions::tracedintegergreaterfunctionbehaviorexecution_constructor_exists():
    assert callable(IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution.__init__)


def test_integerfunctions::tracedintegergreaterfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::tracedmergenodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::TracedMergeNodeActivation)


def test_intermediateactivities::tracedmergenodeactivation_constructor_exists():
    assert callable(IntermediateActivities::TracedMergeNodeActivation.__init__)


def test_intermediateactivities::tracedmergenodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities::TracedMergeNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTemplateParameter)


def test_uml::tracedtemplateparameter_constructor_exists():
    assert callable(uml::TracedTemplateParameter.__init__)


def test_uml::tracedtemplateparameter_constructor_args():
    sig = inspect.signature(uml::TracedTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedmanifestation_is_not_abstract():
    assert not inspect.isabstract(uml::TracedManifestation)


def test_uml::tracedmanifestation_constructor_exists():
    assert callable(uml::TracedManifestation.__init__)


def test_uml::tracedmanifestation_constructor_args():
    sig = inspect.signature(uml::TracedManifestation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedactor_is_not_abstract():
    assert not inspect.isabstract(uml::TracedActor)


def test_uml::tracedactor_constructor_exists():
    assert callable(uml::TracedActor.__init__)


def test_uml::tracedactor_constructor_args():
    sig = inspect.signature(uml::TracedActor.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedremovevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedRemoveVariableValueAction)


def test_uml::tracedremovevariablevalueaction_constructor_exists():
    assert callable(uml::TracedRemoveVariableValueAction.__init__)


def test_uml::tracedremovevariablevalueaction_constructor_args():
    sig = inspect.signature(uml::TracedRemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedprofile_is_not_abstract():
    assert not inspect.isabstract(uml::TracedProfile)


def test_uml::tracedprofile_constructor_exists():
    assert callable(uml::TracedProfile.__init__)


def test_uml::tracedprofile_constructor_args():
    sig = inspect.signature(uml::TracedProfile.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtestidentityaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTestIdentityAction)


def test_uml::tracedtestidentityaction_constructor_exists():
    assert callable(uml::TracedTestIdentityAction.__init__)


def test_uml::tracedtestidentityaction_constructor_args():
    sig = inspect.signature(uml::TracedTestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcollaboration_is_not_abstract():
    assert not inspect.isabstract(uml::TracedCollaboration)


def test_uml::tracedcollaboration_constructor_exists():
    assert callable(uml::TracedCollaboration.__init__)


def test_uml::tracedcollaboration_constructor_args():
    sig = inspect.signature(uml::TracedCollaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedsendsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedSendSignalAction)


def test_uml::tracedsendsignalaction_constructor_exists():
    assert callable(uml::TracedSendSignalAction.__init__)


def test_uml::tracedsendsignalaction_constructor_args():
    sig = inspect.signature(uml::TracedSendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinterfacerealization_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInterfaceRealization)


def test_uml::tracedinterfacerealization_constructor_exists():
    assert callable(uml::TracedInterfaceRealization.__init__)


def test_uml::tracedinterfacerealization_constructor_args():
    sig = inspect.signature(uml::TracedInterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedunmarshallaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedUnmarshallAction)


def test_uml::tracedunmarshallaction_constructor_exists():
    assert callable(uml::TracedUnmarshallAction.__init__)


def test_uml::tracedunmarshallaction_constructor_args():
    sig = inspect.signature(uml::TracedUnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedexpression_is_not_abstract():
    assert not inspect.isabstract(uml::TracedExpression)


def test_uml::tracedexpression_constructor_exists():
    assert callable(uml::TracedExpression.__init__)


def test_uml::tracedexpression_constructor_args():
    sig = inspect.signature(uml::TracedExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedassociation_is_not_abstract():
    assert not inspect.isabstract(uml::TracedAssociation)


def test_uml::tracedassociation_constructor_exists():
    assert callable(uml::TracedAssociation.__init__)


def test_uml::tracedassociation_constructor_args():
    sig = inspect.signature(uml::TracedAssociation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedclearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedClearStructuralFeatureAction)


def test_uml::tracedclearstructuralfeatureaction_constructor_exists():
    assert callable(uml::TracedClearStructuralFeatureAction.__init__)


def test_uml::tracedclearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml::TracedClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedaddvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedAddVariableValueAction)


def test_uml::tracedaddvariablevalueaction_constructor_exists():
    assert callable(uml::TracedAddVariableValueAction.__init__)


def test_uml::tracedaddvariablevalueaction_constructor_args():
    sig = inspect.signature(uml::TracedAddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedliteralreal_is_not_abstract():
    assert not inspect.isabstract(uml::TracedLiteralReal)


def test_uml::tracedliteralreal_constructor_exists():
    assert callable(uml::TracedLiteralReal.__init__)


def test_uml::tracedliteralreal_constructor_args():
    sig = inspect.signature(uml::TracedLiteralReal.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions::tracedcreateobjectactionactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions::TracedCreateObjectActionActivation)


def test_intermediateactions::tracedcreateobjectactionactivation_constructor_exists():
    assert callable(IntermediateActions::TracedCreateObjectActionActivation.__init__)


def test_intermediateactions::tracedcreateobjectactionactivation_constructor_args():
    sig = inspect.signature(IntermediateActions::TracedCreateObjectActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedslot_is_not_abstract():
    assert not inspect.isabstract(uml::TracedSlot)


def test_uml::tracedslot_constructor_exists():
    assert callable(uml::TracedSlot.__init__)


def test_uml::tracedslot_constructor_args():
    sig = inspect.signature(uml::TracedSlot.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedliteralnull_is_not_abstract():
    assert not inspect.isabstract(uml::TracedLiteralNull)


def test_uml::tracedliteralnull_constructor_exists():
    assert callable(uml::TracedLiteralNull.__init__)


def test_uml::tracedliteralnull_constructor_args():
    sig = inspect.signature(uml::TracedLiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions::tracedvaluespecificationactionactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions::TracedValueSpecificationActionActivation)


def test_intermediateactions::tracedvaluespecificationactionactivation_constructor_exists():
    assert callable(IntermediateActions::TracedValueSpecificationActionActivation.__init__)


def test_intermediateactions::tracedvaluespecificationactionactivation_constructor_args():
    sig = inspect.signature(IntermediateActions::TracedValueSpecificationActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedstartobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedStartObjectBehaviorAction)


def test_uml::tracedstartobjectbehavioraction_constructor_exists():
    assert callable(uml::TracedStartObjectBehaviorAction.__init__)


def test_uml::tracedstartobjectbehavioraction_constructor_args():
    sig = inspect.signature(uml::TracedStartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedliteralboolean_is_not_abstract():
    assert not inspect.isabstract(uml::TracedLiteralBoolean)


def test_uml::tracedliteralboolean_constructor_exists():
    assert callable(uml::TracedLiteralBoolean.__init__)


def test_uml::tracedliteralboolean_constructor_args():
    sig = inspect.signature(uml::TracedLiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedreadlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedReadLinkAction)


def test_uml::tracedreadlinkaction_constructor_exists():
    assert callable(uml::TracedReadLinkAction.__init__)


def test_uml::tracedreadlinkaction_constructor_args():
    sig = inspect.signature(uml::TracedReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinclude_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInclude)


def test_uml::tracedinclude_constructor_exists():
    assert callable(uml::TracedInclude.__init__)


def test_uml::tracedinclude_constructor_args():
    sig = inspect.signature(uml::TracedInclude.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedregion_is_not_abstract():
    assert not inspect.isabstract(uml::TracedRegion)


def test_uml::tracedregion_constructor_exists():
    assert callable(uml::TracedRegion.__init__)


def test_uml::tracedregion_constructor_args():
    sig = inspect.signature(uml::TracedRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedstate_is_not_abstract():
    assert not inspect.isabstract(uml::TracedState)


def test_uml::tracedstate_constructor_exists():
    assert callable(uml::TracedState.__init__)


def test_uml::tracedstate_constructor_args():
    sig = inspect.signature(uml::TracedState.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedprimitivetype_is_not_abstract():
    assert not inspect.isabstract(uml::TracedPrimitiveType)


def test_uml::tracedprimitivetype_constructor_exists():
    assert callable(uml::TracedPrimitiveType.__init__)


def test_uml::tracedprimitivetype_constructor_args():
    sig = inspect.signature(uml::TracedPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedstringexpression_is_not_abstract():
    assert not inspect.isabstract(uml::TracedStringExpression)


def test_uml::tracedstringexpression_constructor_exists():
    assert callable(uml::TracedStringExpression.__init__)


def test_uml::tracedstringexpression_constructor_args():
    sig = inspect.signature(uml::TracedStringExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedlinkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(uml::TracedLinkEndDestructionData)


def test_uml::tracedlinkenddestructiondata_constructor_exists():
    assert callable(uml::TracedLinkEndDestructionData.__init__)


def test_uml::tracedlinkenddestructiondata_constructor_args():
    sig = inspect.signature(uml::TracedLinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedreadextentaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedReadExtentAction)


def test_uml::tracedreadextentaction_constructor_exists():
    assert callable(uml::TracedReadExtentAction.__init__)


def test_uml::tracedreadextentaction_constructor_args():
    sig = inspect.signature(uml::TracedReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_basicactions::tracedoutputpinactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions::TracedOutputPinActivation)


def test_basicactions::tracedoutputpinactivation_constructor_exists():
    assert callable(BasicActions::TracedOutputPinActivation.__init__)


def test_basicactions::tracedoutputpinactivation_constructor_args():
    sig = inspect.signature(BasicActions::TracedOutputPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtemplatesignature_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTemplateSignature)


def test_uml::tracedtemplatesignature_constructor_exists():
    assert callable(uml::TracedTemplateSignature.__init__)


def test_uml::tracedtemplatesignature_constructor_args():
    sig = inspect.signature(uml::TracedTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedraiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedRaiseExceptionAction)


def test_uml::tracedraiseexceptionaction_constructor_exists():
    assert callable(uml::TracedRaiseExceptionAction.__init__)


def test_uml::tracedraiseexceptionaction_constructor_args():
    sig = inspect.signature(uml::TracedRaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcommunicationpath_is_not_abstract():
    assert not inspect.isabstract(uml::TracedCommunicationPath)


def test_uml::tracedcommunicationpath_constructor_exists():
    assert callable(uml::TracedCommunicationPath.__init__)


def test_uml::tracedcommunicationpath_constructor_args():
    sig = inspect.signature(uml::TracedCommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_kernel::tracedliteralbooleanevaluation_is_not_abstract():
    assert not inspect.isabstract(Kernel::TracedLiteralBooleanEvaluation)


def test_kernel::tracedliteralbooleanevaluation_constructor_exists():
    assert callable(Kernel::TracedLiteralBooleanEvaluation.__init__)


def test_kernel::tracedliteralbooleanevaluation_constructor_args():
    sig = inspect.signature(Kernel::TracedLiteralBooleanEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedenumeration_is_not_abstract():
    assert not inspect.isabstract(uml::TracedEnumeration)


def test_uml::tracedenumeration_constructor_exists():
    assert callable(uml::TracedEnumeration.__init__)


def test_uml::tracedenumeration_constructor_args():
    sig = inspect.signature(uml::TracedEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedreadlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedReadLinkObjectEndAction)


def test_uml::tracedreadlinkobjectendaction_constructor_exists():
    assert callable(uml::TracedReadLinkObjectEndAction.__init__)


def test_uml::tracedreadlinkobjectendaction_constructor_args():
    sig = inspect.signature(uml::TracedReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcallbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedCallBehaviorAction)


def test_uml::tracedcallbehavioraction_constructor_exists():
    assert callable(uml::TracedCallBehaviorAction.__init__)


def test_uml::tracedcallbehavioraction_constructor_args():
    sig = inspect.signature(uml::TracedCallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedvariable_is_not_abstract():
    assert not inspect.isabstract(uml::TracedVariable)


def test_uml::tracedvariable_constructor_exists():
    assert callable(uml::TracedVariable.__init__)


def test_uml::tracedvariable_constructor_args():
    sig = inspect.signature(uml::TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedconnectorend_is_not_abstract():
    assert not inspect.isabstract(uml::TracedConnectorEnd)


def test_uml::tracedconnectorend_constructor_exists():
    assert callable(uml::TracedConnectorEnd.__init__)


def test_uml::tracedconnectorend_constructor_args():
    sig = inspect.signature(uml::TracedConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedartifact_is_not_abstract():
    assert not inspect.isabstract(uml::TracedArtifact)


def test_uml::tracedartifact_constructor_exists():
    assert callable(uml::TracedArtifact.__init__)


def test_uml::tracedartifact_constructor_args():
    sig = inspect.signature(uml::TracedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcalloperationaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedCallOperationAction)


def test_uml::tracedcalloperationaction_constructor_exists():
    assert callable(uml::TracedCallOperationAction.__init__)


def test_uml::tracedcalloperationaction_constructor_args():
    sig = inspect.signature(uml::TracedCallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedliteralunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(uml::TracedLiteralUnlimitedNatural)


def test_uml::tracedliteralunlimitednatural_constructor_exists():
    assert callable(uml::TracedLiteralUnlimitedNatural.__init__)


def test_uml::tracedliteralunlimitednatural_constructor_args():
    sig = inspect.signature(uml::TracedLiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddurationobservation_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDurationObservation)


def test_uml::traceddurationobservation_constructor_exists():
    assert callable(uml::TracedDurationObservation.__init__)


def test_uml::traceddurationobservation_constructor_args():
    sig = inspect.signature(uml::TracedDurationObservation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedbehaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml::TracedBehaviorExecutionSpecification)


def test_uml::tracedbehaviorexecutionspecification_constructor_exists():
    assert callable(uml::TracedBehaviorExecutionSpecification.__init__)


def test_uml::tracedbehaviorexecutionspecification_constructor_args():
    sig = inspect.signature(uml::TracedBehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedactivityparameternode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedActivityParameterNode)


def test_uml::tracedactivityparameternode_constructor_exists():
    assert callable(uml::TracedActivityParameterNode.__init__)


def test_uml::tracedactivityparameternode_constructor_args():
    sig = inspect.signature(uml::TracedActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedexpansionnode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedExpansionNode)


def test_uml::tracedexpansionnode_constructor_exists():
    assert callable(uml::TracedExpansionNode.__init__)


def test_uml::tracedexpansionnode_constructor_args():
    sig = inspect.signature(uml::TracedExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedprofileapplication_is_not_abstract():
    assert not inspect.isabstract(uml::TracedProfileApplication)


def test_uml::tracedprofileapplication_constructor_exists():
    assert callable(uml::TracedProfileApplication.__init__)


def test_uml::tracedprofileapplication_constructor_args():
    sig = inspect.signature(uml::TracedProfileApplication.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedaddstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedAddStructuralFeatureValueAction)


def test_uml::tracedaddstructuralfeaturevalueaction_constructor_exists():
    assert callable(uml::TracedAddStructuralFeatureValueAction.__init__)


def test_uml::tracedaddstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml::TracedAddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedqualifiervalue_is_not_abstract():
    assert not inspect.isabstract(uml::TracedQualifierValue)


def test_uml::tracedqualifiervalue_constructor_exists():
    assert callable(uml::TracedQualifierValue.__init__)


def test_uml::tracedqualifiervalue_constructor_args():
    sig = inspect.signature(uml::TracedQualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedimage_is_not_abstract():
    assert not inspect.isabstract(uml::TracedImage)


def test_uml::tracedimage_constructor_exists():
    assert callable(uml::TracedImage.__init__)


def test_uml::tracedimage_constructor_args():
    sig = inspect.signature(uml::TracedImage.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedextensionend_is_not_abstract():
    assert not inspect.isabstract(uml::TracedExtensionEnd)


def test_uml::tracedextensionend_constructor_exists():
    assert callable(uml::TracedExtensionEnd.__init__)


def test_uml::tracedextensionend_constructor_args():
    sig = inspect.signature(uml::TracedExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedproperty_is_not_abstract():
    assert not inspect.isabstract(uml::TracedProperty)


def test_uml::tracedproperty_constructor_exists():
    assert callable(uml::TracedProperty.__init__)


def test_uml::tracedproperty_constructor_args():
    sig = inspect.signature(uml::TracedProperty.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddevice_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDevice)


def test_uml::traceddevice_constructor_exists():
    assert callable(uml::TracedDevice.__init__)


def test_uml::traceddevice_constructor_args():
    sig = inspect.signature(uml::TracedDevice.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedopaqueaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedOpaqueAction)


def test_uml::tracedopaqueaction_constructor_exists():
    assert callable(uml::TracedOpaqueAction.__init__)


def test_uml::tracedopaqueaction_constructor_args():
    sig = inspect.signature(uml::TracedOpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedfinalstate_is_not_abstract():
    assert not inspect.isabstract(uml::TracedFinalState)


def test_uml::tracedfinalstate_constructor_exists():
    assert callable(uml::TracedFinalState.__init__)


def test_uml::tracedfinalstate_constructor_args():
    sig = inspect.signature(uml::TracedFinalState.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedreduceaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedReduceAction)


def test_uml::tracedreduceaction_constructor_exists():
    assert callable(uml::TracedReduceAction.__init__)


def test_uml::tracedreduceaction_constructor_args():
    sig = inspect.signature(uml::TracedReduceAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedduration_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDuration)


def test_uml::tracedduration_constructor_exists():
    assert callable(uml::TracedDuration.__init__)


def test_uml::tracedduration_constructor_args():
    sig = inspect.signature(uml::TracedDuration.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtemplateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTemplateParameterSubstitution)


def test_uml::tracedtemplateparametersubstitution_constructor_exists():
    assert callable(uml::TracedTemplateParameterSubstitution.__init__)


def test_uml::tracedtemplateparametersubstitution_constructor_args():
    sig = inspect.signature(uml::TracedTemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedoutputpin_is_not_abstract():
    assert not inspect.isabstract(uml::TracedOutputPin)


def test_uml::tracedoutputpin_constructor_exists():
    assert callable(uml::TracedOutputPin.__init__)


def test_uml::tracedoutputpin_constructor_args():
    sig = inspect.signature(uml::TracedOutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedactionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml::TracedActionExecutionSpecification)


def test_uml::tracedactionexecutionspecification_constructor_exists():
    assert callable(uml::TracedActionExecutionSpecification.__init__)


def test_uml::tracedactionexecutionspecification_constructor_args():
    sig = inspect.signature(uml::TracedActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinformationitem_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInformationItem)


def test_uml::tracedinformationitem_constructor_exists():
    assert callable(uml::TracedInformationItem.__init__)


def test_uml::tracedinformationitem_constructor_args():
    sig = inspect.signature(uml::TracedInformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedoperationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml::TracedOperationTemplateParameter)


def test_uml::tracedoperationtemplateparameter_constructor_exists():
    assert callable(uml::TracedOperationTemplateParameter.__init__)


def test_uml::tracedoperationtemplateparameter_constructor_args():
    sig = inspect.signature(uml::TracedOperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedconnectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml::TracedConnectableElementTemplateParameter)


def test_uml::tracedconnectableelementtemplateparameter_constructor_exists():
    assert callable(uml::TracedConnectableElementTemplateParameter.__init__)


def test_uml::tracedconnectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(uml::TracedConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedlinkenddata_is_not_abstract():
    assert not inspect.isabstract(uml::TracedLinkEndData)


def test_uml::tracedlinkenddata_constructor_exists():
    assert callable(uml::TracedLinkEndData.__init__)


def test_uml::tracedlinkenddata_constructor_args():
    sig = inspect.signature(uml::TracedLinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddurationinterval_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDurationInterval)


def test_uml::traceddurationinterval_constructor_exists():
    assert callable(uml::TracedDurationInterval.__init__)


def test_uml::traceddurationinterval_constructor_args():
    sig = inspect.signature(uml::TracedDurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtransition_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTransition)


def test_uml::tracedtransition_constructor_exists():
    assert callable(uml::TracedTransition.__init__)


def test_uml::tracedtransition_constructor_args():
    sig = inspect.signature(uml::TracedTransition.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtrigger_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTrigger)


def test_uml::tracedtrigger_constructor_exists():
    assert callable(uml::TracedTrigger.__init__)


def test_uml::tracedtrigger_constructor_args():
    sig = inspect.signature(uml::TracedTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedreplyaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedReplyAction)


def test_uml::tracedreplyaction_constructor_exists():
    assert callable(uml::TracedReplyAction.__init__)


def test_uml::tracedreplyaction_constructor_args():
    sig = inspect.signature(uml::TracedReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedclause_is_not_abstract():
    assert not inspect.isabstract(uml::TracedClause)


def test_uml::tracedclause_constructor_exists():
    assert callable(uml::TracedClause.__init__)


def test_uml::tracedclause_constructor_args():
    sig = inspect.signature(uml::TracedClause.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedpackagemerge_is_not_abstract():
    assert not inspect.isabstract(uml::TracedPackageMerge)


def test_uml::tracedpackagemerge_constructor_exists():
    assert callable(uml::TracedPackageMerge.__init__)


def test_uml::tracedpackagemerge_constructor_args():
    sig = inspect.signature(uml::TracedPackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddecisionnode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDecisionNode)


def test_uml::traceddecisionnode_constructor_exists():
    assert callable(uml::TracedDecisionNode.__init__)


def test_uml::traceddecisionnode_constructor_args():
    sig = inspect.signature(uml::TracedDecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions::tracedreadstructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions::TracedReadStructuralFeatureActionActivation)


def test_intermediateactions::tracedreadstructuralfeatureactionactivation_constructor_exists():
    assert callable(IntermediateActions::TracedReadStructuralFeatureActionActivation.__init__)


def test_intermediateactions::tracedreadstructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(IntermediateActions::TracedReadStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedreadselfaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedReadSelfAction)


def test_uml::tracedreadselfaction_constructor_exists():
    assert callable(uml::TracedReadSelfAction.__init__)


def test_uml::tracedreadselfaction_constructor_args():
    sig = inspect.signature(uml::TracedReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedoperation_is_not_abstract():
    assert not inspect.isabstract(uml::TracedOperation)


def test_uml::tracedoperation_constructor_exists():
    assert callable(uml::TracedOperation.__init__)


def test_uml::tracedoperation_constructor_args():
    sig = inspect.signature(uml::TracedOperation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedobjectflow_is_not_abstract():
    assert not inspect.isabstract(uml::TracedObjectFlow)


def test_uml::tracedobjectflow_constructor_exists():
    assert callable(uml::TracedObjectFlow.__init__)


def test_uml::tracedobjectflow_constructor_args():
    sig = inspect.signature(uml::TracedObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedparameterset_is_not_abstract():
    assert not inspect.isabstract(uml::TracedParameterSet)


def test_uml::tracedparameterset_constructor_exists():
    assert callable(uml::TracedParameterSet.__init__)


def test_uml::tracedparameterset_constructor_args():
    sig = inspect.signature(uml::TracedParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml::TracedOccurrenceSpecification)


def test_uml::tracedoccurrencespecification_constructor_exists():
    assert callable(uml::TracedOccurrenceSpecification.__init__)


def test_uml::tracedoccurrencespecification_constructor_args():
    sig = inspect.signature(uml::TracedOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedaccepteventaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedAcceptEventAction)


def test_uml::tracedaccepteventaction_constructor_exists():
    assert callable(uml::TracedAcceptEventAction.__init__)


def test_uml::tracedaccepteventaction_constructor_args():
    sig = inspect.signature(uml::TracedAcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcomponentrealization_is_not_abstract():
    assert not inspect.isabstract(uml::TracedComponentRealization)


def test_uml::tracedcomponentrealization_constructor_exists():
    assert callable(uml::TracedComponentRealization.__init__)


def test_uml::tracedcomponentrealization_constructor_args():
    sig = inspect.signature(uml::TracedComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddatatype_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDataType)


def test_uml::traceddatatype_constructor_exists():
    assert callable(uml::TracedDataType.__init__)


def test_uml::traceddatatype_constructor_args():
    sig = inspect.signature(uml::TracedDataType.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcomment_is_not_abstract():
    assert not inspect.isabstract(uml::TracedComment)


def test_uml::tracedcomment_constructor_exists():
    assert callable(uml::TracedComment.__init__)


def test_uml::tracedcomment_constructor_args():
    sig = inspect.signature(uml::TracedComment.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedloopnode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedLoopNode)


def test_uml::tracedloopnode_constructor_exists():
    assert callable(uml::TracedLoopNode.__init__)


def test_uml::tracedloopnode_constructor_args():
    sig = inspect.signature(uml::TracedLoopNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcallevent_is_not_abstract():
    assert not inspect.isabstract(uml::TracedCallEvent)


def test_uml::tracedcallevent_constructor_exists():
    assert callable(uml::TracedCallEvent.__init__)


def test_uml::tracedcallevent_constructor_args():
    sig = inspect.signature(uml::TracedCallEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedpackage_is_not_abstract():
    assert not inspect.isabstract(uml::TracedPackage)


def test_uml::tracedpackage_constructor_exists():
    assert callable(uml::TracedPackage.__init__)


def test_uml::tracedpackage_constructor_args():
    sig = inspect.signature(uml::TracedPackage.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedprotocolconformance_is_not_abstract():
    assert not inspect.isabstract(uml::TracedProtocolConformance)


def test_uml::tracedprotocolconformance_constructor_exists():
    assert callable(uml::TracedProtocolConformance.__init__)


def test_uml::tracedprotocolconformance_constructor_args():
    sig = inspect.signature(uml::TracedProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedopaquebehavior_is_not_abstract():
    assert not inspect.isabstract(uml::TracedOpaqueBehavior)


def test_uml::tracedopaquebehavior_constructor_exists():
    assert callable(uml::TracedOpaqueBehavior.__init__)


def test_uml::tracedopaquebehavior_constructor_args():
    sig = inspect.signature(uml::TracedOpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinterface_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInterface)


def test_uml::tracedinterface_constructor_exists():
    assert callable(uml::TracedInterface.__init__)


def test_uml::tracedinterface_constructor_args():
    sig = inspect.signature(uml::TracedInterface.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::traceddecisionnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::TracedDecisionNodeActivation)


def test_intermediateactivities::traceddecisionnodeactivation_constructor_exists():
    assert callable(IntermediateActivities::TracedDecisionNodeActivation.__init__)


def test_intermediateactivities::traceddecisionnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities::TracedDecisionNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinteractionconstraint_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInteractionConstraint)


def test_uml::tracedinteractionconstraint_constructor_exists():
    assert callable(uml::TracedInteractionConstraint.__init__)


def test_uml::tracedinteractionconstraint_constructor_args():
    sig = inspect.signature(uml::TracedInteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtimeinterval_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTimeInterval)


def test_uml::tracedtimeinterval_constructor_exists():
    assert callable(uml::TracedTimeInterval.__init__)


def test_uml::tracedtimeinterval_constructor_args():
    sig = inspect.signature(uml::TracedTimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedexecutionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml::TracedExecutionOccurrenceSpecification)


def test_uml::tracedexecutionoccurrencespecification_constructor_exists():
    assert callable(uml::TracedExecutionOccurrenceSpecification.__init__)


def test_uml::tracedexecutionoccurrencespecification_constructor_args():
    sig = inspect.signature(uml::TracedExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedsignal_is_not_abstract():
    assert not inspect.isabstract(uml::TracedSignal)


def test_uml::tracedsignal_constructor_exists():
    assert callable(uml::TracedSignal.__init__)


def test_uml::tracedsignal_constructor_args():
    sig = inspect.signature(uml::TracedSignal.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedextensionpoint_is_not_abstract():
    assert not inspect.isabstract(uml::TracedExtensionPoint)


def test_uml::tracedextensionpoint_constructor_exists():
    assert callable(uml::TracedExtensionPoint.__init__)


def test_uml::tracedextensionpoint_constructor_args():
    sig = inspect.signature(uml::TracedExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcreatelinkaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedCreateLinkAction)


def test_uml::tracedcreatelinkaction_constructor_exists():
    assert callable(uml::TracedCreateLinkAction.__init__)


def test_uml::tracedcreatelinkaction_constructor_args():
    sig = inspect.signature(uml::TracedCreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_kernel::tracedliteralintegerevaluation_is_not_abstract():
    assert not inspect.isabstract(Kernel::TracedLiteralIntegerEvaluation)


def test_kernel::tracedliteralintegerevaluation_constructor_exists():
    assert callable(Kernel::TracedLiteralIntegerEvaluation.__init__)


def test_kernel::tracedliteralintegerevaluation_constructor_args():
    sig = inspect.signature(Kernel::TracedLiteralIntegerEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcentralbuffernode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedCentralBufferNode)


def test_uml::tracedcentralbuffernode_constructor_exists():
    assert callable(uml::TracedCentralBufferNode.__init__)


def test_uml::tracedcentralbuffernode_constructor_args():
    sig = inspect.signature(uml::TracedCentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedmodel_is_not_abstract():
    assert not inspect.isabstract(uml::TracedModel)


def test_uml::tracedmodel_constructor_exists():
    assert callable(uml::TracedModel.__init__)


def test_uml::tracedmodel_constructor_args():
    sig = inspect.signature(uml::TracedModel.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedredefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(uml::TracedRedefinableTemplateSignature)


def test_uml::tracedredefinabletemplatesignature_constructor_exists():
    assert callable(uml::TracedRedefinableTemplateSignature.__init__)


def test_uml::tracedredefinabletemplatesignature_constructor_args():
    sig = inspect.signature(uml::TracedRedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedjoinnode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedJoinNode)


def test_uml::tracedjoinnode_constructor_exists():
    assert callable(uml::TracedJoinNode.__init__)


def test_uml::tracedjoinnode_constructor_args():
    sig = inspect.signature(uml::TracedJoinNode.__init__)
    params = list(sig.parameters.keys())



def test_basicactions::tracedopaqueactionactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions::TracedOpaqueActionActivation)


def test_basicactions::tracedopaqueactionactivation_constructor_exists():
    assert callable(BasicActions::TracedOpaqueActionActivation.__init__)


def test_basicactions::tracedopaqueactionactivation_constructor_args():
    sig = inspect.signature(BasicActions::TracedOpaqueActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedreadlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedReadLinkObjectEndQualifierAction)


def test_uml::tracedreadlinkobjectendqualifieraction_constructor_exists():
    assert callable(uml::TracedReadLinkObjectEndQualifierAction.__init__)


def test_uml::tracedreadlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(uml::TracedReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedrealization_is_not_abstract():
    assert not inspect.isabstract(uml::TracedRealization)


def test_uml::tracedrealization_constructor_exists():
    assert callable(uml::TracedRealization.__init__)


def test_uml::tracedrealization_constructor_args():
    sig = inspect.signature(uml::TracedRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedconnectionpointreference_is_not_abstract():
    assert not inspect.isabstract(uml::TracedConnectionPointReference)


def test_uml::tracedconnectionpointreference_constructor_exists():
    assert callable(uml::TracedConnectionPointReference.__init__)


def test_uml::tracedconnectionpointreference_constructor_args():
    sig = inspect.signature(uml::TracedConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedconditionalnode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedConditionalNode)


def test_uml::tracedconditionalnode_constructor_exists():
    assert callable(uml::TracedConditionalNode.__init__)


def test_uml::tracedconditionalnode_constructor_args():
    sig = inspect.signature(uml::TracedConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_kernel::tracedbooleanvalue_is_not_abstract():
    assert not inspect.isabstract(Kernel::TracedBooleanValue)


def test_kernel::tracedbooleanvalue_constructor_exists():
    assert callable(Kernel::TracedBooleanValue.__init__)


def test_kernel::tracedbooleanvalue_constructor_args():
    sig = inspect.signature(Kernel::TracedBooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedsignalevent_is_not_abstract():
    assert not inspect.isabstract(uml::TracedSignalEvent)


def test_uml::tracedsignalevent_constructor_exists():
    assert callable(uml::TracedSignalEvent.__init__)


def test_uml::tracedsignalevent_constructor_args():
    sig = inspect.signature(uml::TracedSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedliteralinteger_is_not_abstract():
    assert not inspect.isabstract(uml::TracedLiteralInteger)


def test_uml::tracedliteralinteger_constructor_exists():
    assert callable(uml::TracedLiteralInteger.__init__)


def test_uml::tracedliteralinteger_constructor_args():
    sig = inspect.signature(uml::TracedLiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddestroylinkaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDestroyLinkAction)


def test_uml::traceddestroylinkaction_constructor_exists():
    assert callable(uml::TracedDestroyLinkAction.__init__)


def test_uml::traceddestroylinkaction_constructor_args():
    sig = inspect.signature(uml::TracedDestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::tracedactivityfinalnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::TracedActivityFinalNodeActivation)


def test_intermediateactivities::tracedactivityfinalnodeactivation_constructor_exists():
    assert callable(IntermediateActivities::TracedActivityFinalNodeActivation.__init__)


def test_intermediateactivities::tracedactivityfinalnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities::TracedActivityFinalNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedreadvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedReadVariableAction)


def test_uml::tracedreadvariableaction_constructor_exists():
    assert callable(uml::TracedReadVariableAction.__init__)


def test_uml::tracedreadvariableaction_constructor_args():
    sig = inspect.signature(uml::TracedReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedactioninputpin_is_not_abstract():
    assert not inspect.isabstract(uml::TracedActionInputPin)


def test_uml::tracedactioninputpin_constructor_exists():
    assert callable(uml::TracedActionInputPin.__init__)


def test_uml::tracedactioninputpin_constructor_args():
    sig = inspect.signature(uml::TracedActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedusage_is_not_abstract():
    assert not inspect.isabstract(uml::TracedUsage)


def test_uml::tracedusage_constructor_exists():
    assert callable(uml::TracedUsage.__init__)


def test_uml::tracedusage_constructor_args():
    sig = inspect.signature(uml::TracedUsage.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddeploymentspecification_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDeploymentSpecification)


def test_uml::traceddeploymentspecification_constructor_exists():
    assert callable(uml::TracedDeploymentSpecification.__init__)


def test_uml::traceddeploymentspecification_constructor_args():
    sig = inspect.signature(uml::TracedDeploymentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtemplatebinding_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTemplateBinding)


def test_uml::tracedtemplatebinding_constructor_exists():
    assert callable(uml::TracedTemplateBinding.__init__)


def test_uml::tracedtemplatebinding_constructor_args():
    sig = inspect.signature(uml::TracedTemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_tracedassociation_is_not_abstract():
    assert not inspect.isabstract(TracedAssociation)


def test_tracedassociation_constructor_exists():
    assert callable(TracedAssociation.__init__)


def test_tracedassociation_constructor_args():
    sig = inspect.signature(TracedAssociation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcommunicationpath_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedCommunicationPath)


def test_umltrace::uml::tracedcommunicationpath_constructor_exists():
    assert callable(umlTrace::uml::TracedCommunicationPath.__init__)


def test_umltrace::uml::tracedcommunicationpath_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedCommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedextension_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedExtension)


def test_umltrace::uml::tracedextension_constructor_exists():
    assert callable(umlTrace::uml::TracedExtension.__init__)


def test_umltrace::uml::tracedextension_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedExtension.__init__)
    params = list(sig.parameters.keys())



def test_tracedstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(TracedStructuralFeatureAction)


def test_tracedstructuralfeatureaction_constructor_exists():
    assert callable(TracedStructuralFeatureAction.__init__)


def test_tracedstructuralfeatureaction_constructor_args():
    sig = inspect.signature(TracedStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedclearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedClearStructuralFeatureAction)


def test_umltrace::uml::tracedclearstructuralfeatureaction_constructor_exists():
    assert callable(umlTrace::uml::TracedClearStructuralFeatureAction.__init__)


def test_umltrace::uml::tracedclearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedreadstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedReadStructuralFeatureAction)


def test_umltrace::uml::tracedreadstructuralfeatureaction_constructor_exists():
    assert callable(umlTrace::uml::TracedReadStructuralFeatureAction.__init__)


def test_umltrace::uml::tracedreadstructuralfeatureaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedmessageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml::TracedMessageOccurrenceSpecification)


def test_uml::tracedmessageoccurrencespecification_constructor_exists():
    assert callable(uml::TracedMessageOccurrenceSpecification.__init__)


def test_uml::tracedmessageoccurrencespecification_constructor_args():
    sig = inspect.signature(uml::TracedMessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedwritestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedWriteStructuralFeatureAction)


def test_umltrace::uml::tracedwritestructuralfeatureaction_constructor_exists():
    assert callable(umlTrace::uml::TracedWriteStructuralFeatureAction.__init__)


def test_umltrace::uml::tracedwritestructuralfeatureaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedWriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedreception_is_not_abstract():
    assert not inspect.isabstract(uml::TracedReception)


def test_uml::tracedreception_constructor_exists():
    assert callable(uml::TracedReception.__init__)


def test_uml::tracedreception_constructor_args():
    sig = inspect.signature(uml::TracedReception.__init__)
    params = list(sig.parameters.keys())



def test_tracedwritestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(TracedWriteStructuralFeatureAction)


def test_tracedwritestructuralfeatureaction_constructor_exists():
    assert callable(TracedWriteStructuralFeatureAction.__init__)


def test_tracedwritestructuralfeatureaction_constructor_args():
    sig = inspect.signature(TracedWriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedaddstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedAddStructuralFeatureValueAction)


def test_umltrace::uml::tracedaddstructuralfeaturevalueaction_constructor_exists():
    assert callable(umlTrace::uml::TracedAddStructuralFeatureValueAction.__init__)


def test_umltrace::uml::tracedaddstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedAddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedremovestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedRemoveStructuralFeatureValueAction)


def test_umltrace::uml::tracedremovestructuralfeaturevalueaction_constructor_exists():
    assert callable(umlTrace::uml::TracedRemoveStructuralFeatureValueAction.__init__)


def test_umltrace::uml::tracedremovestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedRemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedbehavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(TracedBehavioredClassifier)


def test_tracedbehavioredclassifier_constructor_exists():
    assert callable(TracedBehavioredClassifier.__init__)


def test_tracedbehavioredclassifier_constructor_args():
    sig = inspect.signature(TracedBehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedactor_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedActor)


def test_umltrace::uml::tracedactor_constructor_exists():
    assert callable(umlTrace::uml::TracedActor.__init__)


def test_umltrace::uml::tracedactor_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedActor.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedusecase_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedUseCase)


def test_umltrace::uml::tracedusecase_constructor_exists():
    assert callable(umlTrace::uml::TracedUseCase.__init__)


def test_umltrace::uml::tracedusecase_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedUseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddeployedartifact_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDeployedArtifact)


def test_uml::traceddeployedartifact_constructor_exists():
    assert callable(uml::TracedDeployedArtifact.__init__)


def test_uml::traceddeployedartifact_constructor_args():
    sig = inspect.signature(uml::TracedDeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedclassifier_is_not_abstract():
    assert not inspect.isabstract(uml::TracedClassifier)


def test_uml::tracedclassifier_constructor_exists():
    assert callable(uml::TracedClassifier.__init__)


def test_uml::tracedclassifier_constructor_args():
    sig = inspect.signature(uml::TracedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedassociation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedAssociation)


def test_umltrace::uml::tracedassociation_constructor_exists():
    assert callable(umlTrace::uml::TracedAssociation.__init__)


def test_umltrace::uml::tracedassociation_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedAssociation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedartifact_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedArtifact)


def test_umltrace::uml::tracedartifact_constructor_exists():
    assert callable(umlTrace::uml::TracedArtifact.__init__)


def test_umltrace::uml::tracedartifact_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_tracedartifact_is_not_abstract():
    assert not inspect.isabstract(TracedArtifact)


def test_tracedartifact_constructor_exists():
    assert callable(TracedArtifact.__init__)


def test_tracedartifact_constructor_args():
    sig = inspect.signature(TracedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddeploymentspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDeploymentSpecification)


def test_umltrace::uml::traceddeploymentspecification_constructor_exists():
    assert callable(umlTrace::uml::TracedDeploymentSpecification.__init__)


def test_umltrace::uml::traceddeploymentspecification_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDeploymentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedActivityNode)


def test_uml::tracedactivitynode_constructor_exists():
    assert callable(uml::TracedActivityNode.__init__)


def test_uml::tracedactivitynode_constructor_args():
    sig = inspect.signature(uml::TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedobjectnode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedObjectNode)


def test_uml::tracedobjectnode_constructor_exists():
    assert callable(uml::TracedObjectNode.__init__)


def test_uml::tracedobjectnode_constructor_args():
    sig = inspect.signature(uml::TracedObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedpin_is_not_abstract():
    assert not inspect.isabstract(TracedPin)


def test_tracedpin_constructor_exists():
    assert callable(TracedPin.__init__)


def test_tracedpin_constructor_args():
    sig = inspect.signature(TracedPin.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedoutputpin_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedOutputPin)


def test_umltrace::uml::tracedoutputpin_constructor_exists():
    assert callable(umlTrace::uml::TracedOutputPin.__init__)


def test_umltrace::uml::tracedoutputpin_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedOutputPin.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinputpin_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInputPin)


def test_umltrace::uml::tracedinputpin_constructor_exists():
    assert callable(umlTrace::uml::TracedInputPin.__init__)


def test_umltrace::uml::tracedinputpin_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInputPin.__init__)
    params = list(sig.parameters.keys())



def test_tracedinputpin_is_not_abstract():
    assert not inspect.isabstract(TracedInputPin)


def test_tracedinputpin_constructor_exists():
    assert callable(TracedInputPin.__init__)


def test_tracedinputpin_constructor_args():
    sig = inspect.signature(TracedInputPin.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedactioninputpin_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedActionInputPin)


def test_umltrace::uml::tracedactioninputpin_constructor_exists():
    assert callable(umlTrace::uml::TracedActionInputPin.__init__)


def test_umltrace::uml::tracedactioninputpin_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedvaluepin_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedValuePin)


def test_umltrace::uml::tracedvaluepin_constructor_exists():
    assert callable(umlTrace::uml::TracedValuePin.__init__)


def test_umltrace::uml::tracedvaluepin_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedValuePin.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedmultiplicityelement_is_not_abstract():
    assert not inspect.isabstract(uml::TracedMultiplicityElement)


def test_uml::tracedmultiplicityelement_constructor_exists():
    assert callable(uml::TracedMultiplicityElement.__init__)


def test_uml::tracedmultiplicityelement_constructor_args():
    sig = inspect.signature(uml::TracedMultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedpin_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedPin)


def test_umltrace::uml::tracedpin_constructor_exists():
    assert callable(umlTrace::uml::TracedPin.__init__)


def test_umltrace::uml::tracedpin_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedPin.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtypedelement_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTypedElement)


def test_uml::tracedtypedelement_constructor_exists():
    assert callable(uml::TracedTypedElement.__init__)


def test_uml::tracedtypedelement_constructor_args():
    sig = inspect.signature(uml::TracedTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedobjectnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedObjectNode)


def test_umltrace::uml::tracedobjectnode_constructor_exists():
    assert callable(umlTrace::uml::TracedObjectNode.__init__)


def test_umltrace::uml::tracedobjectnode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedfeature_is_not_abstract():
    assert not inspect.isabstract(uml::TracedFeature)


def test_uml::tracedfeature_constructor_exists():
    assert callable(uml::TracedFeature.__init__)


def test_uml::tracedfeature_constructor_args():
    sig = inspect.signature(uml::TracedFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedstructuralfeature_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedStructuralFeature)


def test_umltrace::uml::tracedstructuralfeature_constructor_exists():
    assert callable(umlTrace::uml::TracedStructuralFeature.__init__)


def test_umltrace::uml::tracedstructuralfeature_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_tracedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(TracedValueSpecification)


def test_tracedvaluespecification_constructor_exists():
    assert callable(TracedValueSpecification.__init__)


def test_tracedvaluespecification_constructor_args():
    sig = inspect.signature(TracedValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedexpression_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedExpression)


def test_umltrace::uml::tracedexpression_constructor_exists():
    assert callable(umlTrace::uml::TracedExpression.__init__)


def test_umltrace::uml::tracedexpression_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedExpression.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedduration_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDuration)


def test_umltrace::uml::tracedduration_constructor_exists():
    assert callable(umlTrace::uml::TracedDuration.__init__)


def test_umltrace::uml::tracedduration_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDuration.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinstancevalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInstanceValue)


def test_umltrace::uml::tracedinstancevalue_constructor_exists():
    assert callable(umlTrace::uml::TracedInstanceValue.__init__)


def test_umltrace::uml::tracedinstancevalue_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedopaqueexpression_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedOpaqueExpression)


def test_umltrace::uml::tracedopaqueexpression_constructor_exists():
    assert callable(umlTrace::uml::TracedOpaqueExpression.__init__)


def test_umltrace::uml::tracedopaqueexpression_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedOpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinterval_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInterval)


def test_umltrace::uml::tracedinterval_constructor_exists():
    assert callable(umlTrace::uml::TracedInterval.__init__)


def test_umltrace::uml::tracedinterval_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInterval.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtimeexpression_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTimeExpression)


def test_umltrace::uml::tracedtimeexpression_constructor_exists():
    assert callable(umlTrace::uml::TracedTimeExpression.__init__)


def test_umltrace::uml::tracedtimeexpression_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedliteralspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLiteralSpecification)


def test_umltrace::uml::tracedliteralspecification_constructor_exists():
    assert callable(umlTrace::uml::TracedLiteralSpecification.__init__)


def test_umltrace::uml::tracedliteralspecification_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_tracedliteralspecification_is_not_abstract():
    assert not inspect.isabstract(TracedLiteralSpecification)


def test_tracedliteralspecification_constructor_exists():
    assert callable(TracedLiteralSpecification.__init__)


def test_tracedliteralspecification_constructor_args():
    sig = inspect.signature(TracedLiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedliteralboolean_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLiteralBoolean)


def test_umltrace::uml::tracedliteralboolean_constructor_exists():
    assert callable(umlTrace::uml::TracedLiteralBoolean.__init__)


def test_umltrace::uml::tracedliteralboolean_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedliteralnull_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLiteralNull)


def test_umltrace::uml::tracedliteralnull_constructor_exists():
    assert callable(umlTrace::uml::TracedLiteralNull.__init__)


def test_umltrace::uml::tracedliteralnull_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedliteralreal_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLiteralReal)


def test_umltrace::uml::tracedliteralreal_constructor_exists():
    assert callable(umlTrace::uml::TracedLiteralReal.__init__)


def test_umltrace::uml::tracedliteralreal_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLiteralReal.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedliteralinteger_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLiteralInteger)


def test_umltrace::uml::tracedliteralinteger_constructor_exists():
    assert callable(umlTrace::uml::TracedLiteralInteger.__init__)


def test_umltrace::uml::tracedliteralinteger_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedliteralunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLiteralUnlimitedNatural)


def test_umltrace::uml::tracedliteralunlimitednatural_constructor_exists():
    assert callable(umlTrace::uml::TracedLiteralUnlimitedNatural.__init__)


def test_umltrace::uml::tracedliteralunlimitednatural_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedliteralstring_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLiteralString)


def test_umltrace::uml::tracedliteralstring_constructor_exists():
    assert callable(umlTrace::uml::TracedLiteralString.__init__)


def test_umltrace::uml::tracedliteralstring_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLiteralString.__init__)
    params = list(sig.parameters.keys())



def test_tracedvariableaction_is_not_abstract():
    assert not inspect.isabstract(TracedVariableAction)


def test_tracedvariableaction_constructor_exists():
    assert callable(TracedVariableAction.__init__)


def test_tracedvariableaction_constructor_args():
    sig = inspect.signature(TracedVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedreadvariableaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedReadVariableAction)


def test_umltrace::uml::tracedreadvariableaction_constructor_exists():
    assert callable(umlTrace::uml::TracedReadVariableAction.__init__)


def test_umltrace::uml::tracedreadvariableaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedwritevariableaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedWriteVariableAction)


def test_umltrace::uml::tracedwritevariableaction_constructor_exists():
    assert callable(umlTrace::uml::TracedWriteVariableAction.__init__)


def test_umltrace::uml::tracedwritevariableaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedWriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedclearvariableaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedClearVariableAction)


def test_umltrace::uml::tracedclearvariableaction_constructor_exists():
    assert callable(umlTrace::uml::TracedClearVariableAction.__init__)


def test_umltrace::uml::tracedclearvariableaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcontinuation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedContinuation)


def test_umltrace::uml::tracedcontinuation_constructor_exists():
    assert callable(umlTrace::uml::TracedContinuation.__init__)


def test_umltrace::uml::tracedcontinuation_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedContinuation.__init__)
    params = list(sig.parameters.keys())



def test_tracedcombinedfragment_is_not_abstract():
    assert not inspect.isabstract(TracedCombinedFragment)


def test_tracedcombinedfragment_constructor_exists():
    assert callable(TracedCombinedFragment.__init__)


def test_tracedcombinedfragment_constructor_args():
    sig = inspect.signature(TracedCombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedconsiderignorefragment_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedConsiderIgnoreFragment)


def test_umltrace::uml::tracedconsiderignorefragment_constructor_exists():
    assert callable(umlTrace::uml::TracedConsiderIgnoreFragment.__init__)


def test_umltrace::uml::tracedconsiderignorefragment_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_tracednode_is_not_abstract():
    assert not inspect.isabstract(TracedNode)


def test_tracednode_constructor_exists():
    assert callable(TracedNode.__init__)


def test_tracednode_constructor_args():
    sig = inspect.signature(TracedNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedexecutionenvironment_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedExecutionEnvironment)


def test_umltrace::uml::tracedexecutionenvironment_constructor_exists():
    assert callable(umlTrace::uml::TracedExecutionEnvironment.__init__)


def test_umltrace::uml::tracedexecutionenvironment_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddevice_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDevice)


def test_umltrace::uml::traceddevice_constructor_exists():
    assert callable(umlTrace::uml::TracedDevice.__init__)


def test_umltrace::uml::traceddevice_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDevice.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtype_is_not_abstract():
    assert not inspect.isabstract(uml::TracedType)


def test_uml::tracedtype_constructor_exists():
    assert callable(uml::TracedType.__init__)


def test_uml::tracedtype_constructor_args():
    sig = inspect.signature(uml::TracedType.__init__)
    params = list(sig.parameters.keys())



def test_tracedclassifier_is_not_abstract():
    assert not inspect.isabstract(TracedClassifier)


def test_tracedclassifier_constructor_exists():
    assert callable(TracedClassifier.__init__)


def test_tracedclassifier_constructor_args():
    sig = inspect.signature(TracedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedbehavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedBehavioredClassifier)


def test_umltrace::uml::tracedbehavioredclassifier_constructor_exists():
    assert callable(umlTrace::uml::TracedBehavioredClassifier.__init__)


def test_umltrace::uml::tracedbehavioredclassifier_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedBehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinformationitem_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInformationItem)


def test_umltrace::uml::tracedinformationitem_constructor_exists():
    assert callable(umlTrace::uml::TracedInformationItem.__init__)


def test_umltrace::uml::tracedinformationitem_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInformationItem.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddatatype_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDataType)


def test_umltrace::uml::traceddatatype_constructor_exists():
    assert callable(umlTrace::uml::TracedDataType.__init__)


def test_umltrace::uml::traceddatatype_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDataType.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinterface_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInterface)


def test_umltrace::uml::tracedinterface_constructor_exists():
    assert callable(umlTrace::uml::TracedInterface.__init__)


def test_umltrace::uml::tracedinterface_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInterface.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedstructuredclassifier_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedStructuredClassifier)


def test_umltrace::uml::tracedstructuredclassifier_constructor_exists():
    assert callable(umlTrace::uml::TracedStructuredClassifier.__init__)


def test_umltrace::uml::tracedstructuredclassifier_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedStructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_tracedstructuredclassifier_is_not_abstract():
    assert not inspect.isabstract(TracedStructuredClassifier)


def test_tracedstructuredclassifier_constructor_exists():
    assert callable(TracedStructuredClassifier.__init__)


def test_tracedstructuredclassifier_constructor_args():
    sig = inspect.signature(TracedStructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedencapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedEncapsulatedClassifier)


def test_umltrace::uml::tracedencapsulatedclassifier_constructor_exists():
    assert callable(umlTrace::uml::TracedEncapsulatedClassifier.__init__)


def test_umltrace::uml::tracedencapsulatedclassifier_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedEncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedbehavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml::TracedBehavioredClassifier)


def test_uml::tracedbehavioredclassifier_constructor_exists():
    assert callable(uml::TracedBehavioredClassifier.__init__)


def test_uml::tracedbehavioredclassifier_constructor_args():
    sig = inspect.signature(uml::TracedBehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcollaboration_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedCollaboration)


def test_umltrace::uml::tracedcollaboration_constructor_exists():
    assert callable(umlTrace::uml::TracedCollaboration.__init__)


def test_umltrace::uml::tracedcollaboration_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedCollaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedencapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(uml::TracedEncapsulatedClassifier)


def test_uml::tracedencapsulatedclassifier_constructor_exists():
    assert callable(uml::TracedEncapsulatedClassifier.__init__)


def test_uml::tracedencapsulatedclassifier_constructor_args():
    sig = inspect.signature(uml::TracedEncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedclass_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedClass)


def test_umltrace::uml::tracedclass_constructor_exists():
    assert callable(umlTrace::uml::TracedClass.__init__)


def test_umltrace::uml::tracedclass_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedClass.__init__)
    params = list(sig.parameters.keys())



def test_tracedcallaction_is_not_abstract():
    assert not inspect.isabstract(TracedCallAction)


def test_tracedcallaction_constructor_exists():
    assert callable(TracedCallAction.__init__)


def test_tracedcallaction_constructor_args():
    sig = inspect.signature(TracedCallAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedstartobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedStartObjectBehaviorAction)


def test_umltrace::uml::tracedstartobjectbehavioraction_constructor_exists():
    assert callable(umlTrace::uml::TracedStartObjectBehaviorAction.__init__)


def test_umltrace::uml::tracedstartobjectbehavioraction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedStartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcalloperationaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedCallOperationAction)


def test_umltrace::uml::tracedcalloperationaction_constructor_exists():
    assert callable(umlTrace::uml::TracedCallOperationAction.__init__)


def test_umltrace::uml::tracedcalloperationaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedCallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcallbehavioraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedCallBehaviorAction)


def test_umltrace::uml::tracedcallbehavioraction_constructor_exists():
    assert callable(umlTrace::uml::TracedCallBehaviorAction.__init__)


def test_umltrace::uml::tracedcallbehavioraction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedCallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedrelationship_is_not_abstract():
    assert not inspect.isabstract(TracedRelationship)


def test_tracedrelationship_constructor_exists():
    assert callable(TracedRelationship.__init__)


def test_tracedrelationship_constructor_args():
    sig = inspect.signature(TracedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddirectedrelationship_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDirectedRelationship)


def test_umltrace::uml::traceddirectedrelationship_constructor_exists():
    assert callable(umlTrace::uml::TracedDirectedRelationship.__init__)


def test_umltrace::uml::traceddirectedrelationship_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_traceddirectedrelationship_is_not_abstract():
    assert not inspect.isabstract(TracedDirectedRelationship)


def test_traceddirectedrelationship_constructor_exists():
    assert callable(TracedDirectedRelationship.__init__)


def test_traceddirectedrelationship_constructor_args():
    sig = inspect.signature(TracedDirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedgeneralization_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedGeneralization)


def test_umltrace::uml::tracedgeneralization_constructor_exists():
    assert callable(umlTrace::uml::TracedGeneralization.__init__)


def test_umltrace::uml::tracedgeneralization_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedGeneralization.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtemplatebinding_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTemplateBinding)


def test_umltrace::uml::tracedtemplatebinding_constructor_exists():
    assert callable(umlTrace::uml::TracedTemplateBinding.__init__)


def test_umltrace::uml::tracedtemplatebinding_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedprofileapplication_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedProfileApplication)


def test_umltrace::uml::tracedprofileapplication_constructor_exists():
    assert callable(umlTrace::uml::TracedProfileApplication.__init__)


def test_umltrace::uml::tracedprofileapplication_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedProfileApplication.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedpackageimport_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedPackageImport)


def test_umltrace::uml::tracedpackageimport_constructor_exists():
    assert callable(umlTrace::uml::TracedPackageImport.__init__)


def test_umltrace::uml::tracedpackageimport_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedPackageImport.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedelementimport_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedElementImport)


def test_umltrace::uml::tracedelementimport_constructor_exists():
    assert callable(umlTrace::uml::TracedElementImport.__init__)


def test_umltrace::uml::tracedelementimport_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedElementImport.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedpackagemerge_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedPackageMerge)


def test_umltrace::uml::tracedpackagemerge_constructor_exists():
    assert callable(umlTrace::uml::TracedPackageMerge.__init__)


def test_umltrace::uml::tracedpackagemerge_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedPackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedprotocolconformance_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedProtocolConformance)


def test_umltrace::uml::tracedprotocolconformance_constructor_exists():
    assert callable(umlTrace::uml::TracedProtocolConformance.__init__)


def test_umltrace::uml::tracedprotocolconformance_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_tracedinvocationaction_is_not_abstract():
    assert not inspect.isabstract(TracedInvocationAction)


def test_tracedinvocationaction_constructor_exists():
    assert callable(TracedInvocationAction.__init__)


def test_tracedinvocationaction_constructor_args():
    sig = inspect.signature(TracedInvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedbroadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedBroadcastSignalAction)


def test_umltrace::uml::tracedbroadcastsignalaction_constructor_exists():
    assert callable(umlTrace::uml::TracedBroadcastSignalAction.__init__)


def test_umltrace::uml::tracedbroadcastsignalaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedBroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedsendsignalaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedSendSignalAction)


def test_umltrace::uml::tracedsendsignalaction_constructor_exists():
    assert callable(umlTrace::uml::TracedSendSignalAction.__init__)


def test_umltrace::uml::tracedsendsignalaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedSendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcallaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedCallAction)


def test_umltrace::uml::tracedcallaction_constructor_exists():
    assert callable(umlTrace::uml::TracedCallAction.__init__)


def test_umltrace::uml::tracedcallaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedCallAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedsendobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedSendObjectAction)


def test_umltrace::uml::tracedsendobjectaction_constructor_exists():
    assert callable(umlTrace::uml::TracedSendObjectAction.__init__)


def test_umltrace::uml::tracedsendobjectaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedSendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedredefinableelement_is_not_abstract():
    assert not inspect.isabstract(TracedRedefinableElement)


def test_tracedredefinableelement_constructor_exists():
    assert callable(TracedRedefinableElement.__init__)


def test_tracedredefinableelement_constructor_args():
    sig = inspect.signature(TracedRedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedextensionpoint_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedExtensionPoint)


def test_umltrace::uml::tracedextensionpoint_constructor_exists():
    assert callable(umlTrace::uml::TracedExtensionPoint.__init__)


def test_umltrace::uml::tracedextensionpoint_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedActivityEdge)


def test_umltrace::uml::tracedactivityedge_constructor_exists():
    assert callable(umlTrace::uml::TracedActivityEdge.__init__)


def test_umltrace::uml::tracedactivityedge_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedfeature_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedFeature)


def test_umltrace::uml::tracedfeature_constructor_exists():
    assert callable(umlTrace::uml::TracedFeature.__init__)


def test_umltrace::uml::tracedfeature_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedFeature.__init__)
    params = list(sig.parameters.keys())



def test_tracedfeature_is_not_abstract():
    assert not inspect.isabstract(TracedFeature)


def test_tracedfeature_constructor_exists():
    assert callable(TracedFeature.__init__)


def test_tracedfeature_constructor_args():
    sig = inspect.signature(TracedFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedconnector_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedConnector)


def test_umltrace::uml::tracedconnector_constructor_exists():
    assert callable(umlTrace::uml::TracedConnector.__init__)


def test_umltrace::uml::tracedconnector_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedConnector.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtemplateableelement_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTemplateableElement)


def test_uml::tracedtemplateableelement_constructor_exists():
    assert callable(uml::TracedTemplateableElement.__init__)


def test_uml::tracedtemplateableelement_constructor_args():
    sig = inspect.signature(uml::TracedTemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedstringexpression_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedStringExpression)


def test_umltrace::uml::tracedstringexpression_constructor_exists():
    assert callable(umlTrace::uml::TracedStringExpression.__init__)


def test_umltrace::uml::tracedstringexpression_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedStringExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedpackageableelement_is_not_abstract():
    assert not inspect.isabstract(uml::TracedPackageableElement)


def test_uml::tracedpackageableelement_constructor_exists():
    assert callable(uml::TracedPackageableElement.__init__)


def test_uml::tracedpackageableelement_constructor_args():
    sig = inspect.signature(uml::TracedPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedValueSpecification)


def test_umltrace::uml::tracedvaluespecification_constructor_exists():
    assert callable(umlTrace::uml::TracedValueSpecification.__init__)


def test_umltrace::uml::tracedvaluespecification_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddeploymenttarget_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDeploymentTarget)


def test_uml::traceddeploymenttarget_constructor_exists():
    assert callable(uml::TracedDeploymentTarget.__init__)


def test_uml::traceddeploymenttarget_constructor_args():
    sig = inspect.signature(uml::TracedDeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinstancespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInstanceSpecification)


def test_umltrace::uml::tracedinstancespecification_constructor_exists():
    assert callable(umlTrace::uml::TracedInstanceSpecification.__init__)


def test_umltrace::uml::tracedinstancespecification_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedconnectableelement_is_not_abstract():
    assert not inspect.isabstract(uml::TracedConnectableElement)


def test_uml::tracedconnectableelement_constructor_exists():
    assert callable(uml::TracedConnectableElement.__init__)


def test_uml::tracedconnectableelement_constructor_args():
    sig = inspect.signature(uml::TracedConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedParameter)


def test_umltrace::uml::tracedparameter_constructor_exists():
    assert callable(umlTrace::uml::TracedParameter.__init__)


def test_umltrace::uml::tracedparameter_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedParameter.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedvariable_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedVariable)


def test_umltrace::uml::tracedvariable_constructor_exists():
    assert callable(umlTrace::uml::TracedVariable.__init__)


def test_umltrace::uml::tracedvariable_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedstructuralfeature_is_not_abstract():
    assert not inspect.isabstract(uml::TracedStructuralFeature)


def test_uml::tracedstructuralfeature_constructor_exists():
    assert callable(uml::TracedStructuralFeature.__init__)


def test_uml::tracedstructuralfeature_constructor_args():
    sig = inspect.signature(uml::TracedStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedproperty_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedProperty)


def test_umltrace::uml::tracedproperty_constructor_exists():
    assert callable(umlTrace::uml::TracedProperty.__init__)


def test_umltrace::uml::tracedproperty_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedProperty.__init__)
    params = list(sig.parameters.keys())



def test_tracedproperty_is_not_abstract():
    assert not inspect.isabstract(TracedProperty)


def test_tracedproperty_constructor_exists():
    assert callable(TracedProperty.__init__)


def test_tracedproperty_constructor_args():
    sig = inspect.signature(TracedProperty.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedextensionend_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedExtensionEnd)


def test_umltrace::uml::tracedextensionend_constructor_exists():
    assert callable(umlTrace::uml::TracedExtensionEnd.__init__)


def test_umltrace::uml::tracedextensionend_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedport_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedPort)


def test_umltrace::uml::tracedport_constructor_exists():
    assert callable(umlTrace::uml::TracedPort.__init__)


def test_umltrace::uml::tracedport_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedPort.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddirectedrelationship_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDirectedRelationship)


def test_uml::traceddirectedrelationship_constructor_exists():
    assert callable(uml::TracedDirectedRelationship.__init__)


def test_uml::traceddirectedrelationship_constructor_args():
    sig = inspect.signature(uml::TracedDirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinformationflow_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInformationFlow)


def test_umltrace::uml::tracedinformationflow_constructor_exists():
    assert callable(umlTrace::uml::TracedInformationFlow.__init__)


def test_umltrace::uml::tracedinformationflow_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddependency_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDependency)


def test_umltrace::uml::traceddependency_constructor_exists():
    assert callable(umlTrace::uml::TracedDependency.__init__)


def test_umltrace::uml::traceddependency_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDependency.__init__)
    params = list(sig.parameters.keys())



def test_tracedevent_is_not_abstract():
    assert not inspect.isabstract(TracedEvent)


def test_tracedevent_constructor_exists():
    assert callable(TracedEvent.__init__)


def test_tracedevent_constructor_args():
    sig = inspect.signature(TracedEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtimeevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTimeEvent)


def test_umltrace::uml::tracedtimeevent_constructor_exists():
    assert callable(umlTrace::uml::TracedTimeEvent.__init__)


def test_umltrace::uml::tracedtimeevent_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedmessageevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedMessageEvent)


def test_umltrace::uml::tracedmessageevent_constructor_exists():
    assert callable(umlTrace::uml::TracedMessageEvent.__init__)


def test_umltrace::uml::tracedmessageevent_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedMessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedchangeevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedChangeEvent)


def test_umltrace::uml::tracedchangeevent_constructor_exists():
    assert callable(umlTrace::uml::TracedChangeEvent.__init__)


def test_umltrace::uml::tracedchangeevent_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedsignal_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedSignal)


def test_umltrace::uml::tracedsignal_constructor_exists():
    assert callable(umlTrace::uml::TracedSignal.__init__)


def test_umltrace::uml::tracedsignal_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedSignal.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinteractionuse_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInteractionUse)


def test_umltrace::uml::tracedinteractionuse_constructor_exists():
    assert callable(umlTrace::uml::TracedInteractionUse.__init__)


def test_umltrace::uml::tracedinteractionuse_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_tracedfinalnode_is_not_abstract():
    assert not inspect.isabstract(TracedFinalNode)


def test_tracedfinalnode_constructor_exists():
    assert callable(TracedFinalNode.__init__)


def test_tracedfinalnode_constructor_args():
    sig = inspect.signature(TracedFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedactivityfinalnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedActivityFinalNode)


def test_umltrace::uml::tracedactivityfinalnode_constructor_exists():
    assert callable(umlTrace::uml::TracedActivityFinalNode.__init__)


def test_umltrace::uml::tracedactivityfinalnode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedflowfinalnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedFlowFinalNode)


def test_umltrace::uml::tracedflowfinalnode_constructor_exists():
    assert callable(umlTrace::uml::TracedFlowFinalNode.__init__)


def test_umltrace::uml::tracedflowfinalnode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedFlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(TracedControlNode)


def test_tracedcontrolnode_constructor_exists():
    assert callable(TracedControlNode.__init__)


def test_tracedcontrolnode_constructor_args():
    sig = inspect.signature(TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedjoinnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedJoinNode)


def test_umltrace::uml::tracedjoinnode_constructor_exists():
    assert callable(umlTrace::uml::TracedJoinNode.__init__)


def test_umltrace::uml::tracedjoinnode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedJoinNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedmergenode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedMergeNode)


def test_umltrace::uml::tracedmergenode_constructor_exists():
    assert callable(umlTrace::uml::TracedMergeNode.__init__)


def test_umltrace::uml::tracedmergenode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedMergeNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedforknode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedForkNode)


def test_umltrace::uml::tracedforknode_constructor_exists():
    assert callable(umlTrace::uml::TracedForkNode.__init__)


def test_umltrace::uml::tracedforknode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedForkNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedfinalnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedFinalNode)


def test_umltrace::uml::tracedfinalnode_constructor_exists():
    assert callable(umlTrace::uml::TracedFinalNode.__init__)


def test_umltrace::uml::tracedfinalnode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddecisionnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDecisionNode)


def test_umltrace::uml::traceddecisionnode_constructor_exists():
    assert callable(umlTrace::uml::TracedDecisionNode.__init__)


def test_umltrace::uml::traceddecisionnode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinitialnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInitialNode)


def test_umltrace::uml::tracedinitialnode_constructor_exists():
    assert callable(umlTrace::uml::TracedInitialNode.__init__)


def test_umltrace::uml::tracedinitialnode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedaction_is_not_abstract():
    assert not inspect.isabstract(TracedAction)


def test_tracedaction_constructor_exists():
    assert callable(TracedAction.__init__)


def test_tracedaction_constructor_args():
    sig = inspect.signature(TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedaccepteventaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedAcceptEventAction)


def test_umltrace::uml::tracedaccepteventaction_constructor_exists():
    assert callable(umlTrace::uml::TracedAcceptEventAction.__init__)


def test_umltrace::uml::tracedaccepteventaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedAcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedstartclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedStartClassifierBehaviorAction)


def test_umltrace::uml::tracedstartclassifierbehavioraction_constructor_exists():
    assert callable(umlTrace::uml::TracedStartClassifierBehaviorAction.__init__)


def test_umltrace::uml::tracedstartclassifierbehavioraction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedStartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedStructuralFeatureAction)


def test_umltrace::uml::tracedstructuralfeatureaction_constructor_exists():
    assert callable(umlTrace::uml::TracedStructuralFeatureAction.__init__)


def test_umltrace::uml::tracedstructuralfeatureaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedreduceaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedReduceAction)


def test_umltrace::uml::tracedreduceaction_constructor_exists():
    assert callable(umlTrace::uml::TracedReduceAction.__init__)


def test_umltrace::uml::tracedreduceaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedReduceAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedvaluespecificationaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedValueSpecificationAction)


def test_umltrace::uml::tracedvaluespecificationaction_constructor_exists():
    assert callable(umlTrace::uml::TracedValueSpecificationAction.__init__)


def test_umltrace::uml::tracedvaluespecificationaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedopaqueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedOpaqueAction)


def test_umltrace::uml::tracedopaqueaction_constructor_exists():
    assert callable(umlTrace::uml::TracedOpaqueAction.__init__)


def test_umltrace::uml::tracedopaqueaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedOpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedunmarshallaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedUnmarshallAction)


def test_umltrace::uml::tracedunmarshallaction_constructor_exists():
    assert callable(umlTrace::uml::TracedUnmarshallAction.__init__)


def test_umltrace::uml::tracedunmarshallaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedUnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedreadselfaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedReadSelfAction)


def test_umltrace::uml::tracedreadselfaction_constructor_exists():
    assert callable(umlTrace::uml::TracedReadSelfAction.__init__)


def test_umltrace::uml::tracedreadselfaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedreadisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedReadIsClassifiedObjectAction)


def test_umltrace::uml::tracedreadisclassifiedobjectaction_constructor_exists():
    assert callable(umlTrace::uml::TracedReadIsClassifiedObjectAction.__init__)


def test_umltrace::uml::tracedreadisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddestroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDestroyObjectAction)


def test_umltrace::uml::traceddestroyobjectaction_constructor_exists():
    assert callable(umlTrace::uml::TracedDestroyObjectAction.__init__)


def test_umltrace::uml::traceddestroyobjectaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedvariableaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedVariableAction)


def test_umltrace::uml::tracedvariableaction_constructor_exists():
    assert callable(umlTrace::uml::TracedVariableAction.__init__)


def test_umltrace::uml::tracedvariableaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedreadlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedReadLinkObjectEndQualifierAction)


def test_umltrace::uml::tracedreadlinkobjectendqualifieraction_constructor_exists():
    assert callable(umlTrace::uml::TracedReadLinkObjectEndQualifierAction.__init__)


def test_umltrace::uml::tracedreadlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinvocationaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInvocationAction)


def test_umltrace::uml::tracedinvocationaction_constructor_exists():
    assert callable(umlTrace::uml::TracedInvocationAction.__init__)


def test_umltrace::uml::tracedinvocationaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedraiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedRaiseExceptionAction)


def test_umltrace::uml::tracedraiseexceptionaction_constructor_exists():
    assert callable(umlTrace::uml::TracedRaiseExceptionAction.__init__)


def test_umltrace::uml::tracedraiseexceptionaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedRaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedreadlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedReadLinkObjectEndAction)


def test_umltrace::uml::tracedreadlinkobjectendaction_constructor_exists():
    assert callable(umlTrace::uml::TracedReadLinkObjectEndAction.__init__)


def test_umltrace::uml::tracedreadlinkobjectendaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedclearassociationaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedClearAssociationAction)


def test_umltrace::uml::tracedclearassociationaction_constructor_exists():
    assert callable(umlTrace::uml::TracedClearAssociationAction.__init__)


def test_umltrace::uml::tracedclearassociationaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedreadextentaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedReadExtentAction)


def test_umltrace::uml::tracedreadextentaction_constructor_exists():
    assert callable(umlTrace::uml::TracedReadExtentAction.__init__)


def test_umltrace::uml::tracedreadextentaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedreplyaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedReplyAction)


def test_umltrace::uml::tracedreplyaction_constructor_exists():
    assert callable(umlTrace::uml::TracedReplyAction.__init__)


def test_umltrace::uml::tracedreplyaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtestidentityaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTestIdentityAction)


def test_umltrace::uml::tracedtestidentityaction_constructor_exists():
    assert callable(umlTrace::uml::TracedTestIdentityAction.__init__)


def test_umltrace::uml::tracedtestidentityaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcreateobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedCreateObjectAction)


def test_umltrace::uml::tracedcreateobjectaction_constructor_exists():
    assert callable(umlTrace::uml::TracedCreateObjectAction.__init__)


def test_umltrace::uml::tracedcreateobjectaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedCreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedreclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedReclassifyObjectAction)


def test_umltrace::uml::tracedreclassifyobjectaction_constructor_exists():
    assert callable(umlTrace::uml::TracedReclassifyObjectAction.__init__)


def test_umltrace::uml::tracedreclassifyobjectaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedlinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLinkAction)


def test_umltrace::uml::tracedlinkaction_constructor_exists():
    assert callable(umlTrace::uml::TracedLinkAction.__init__)


def test_umltrace::uml::tracedlinkaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedlinkaction_is_not_abstract():
    assert not inspect.isabstract(TracedLinkAction)


def test_tracedlinkaction_constructor_exists():
    assert callable(TracedLinkAction.__init__)


def test_tracedlinkaction_constructor_args():
    sig = inspect.signature(TracedLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedreadlinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedReadLinkAction)


def test_umltrace::uml::tracedreadlinkaction_constructor_exists():
    assert callable(umlTrace::uml::TracedReadLinkAction.__init__)


def test_umltrace::uml::tracedreadlinkaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedwritelinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedWriteLinkAction)


def test_umltrace::uml::tracedwritelinkaction_constructor_exists():
    assert callable(umlTrace::uml::TracedWriteLinkAction.__init__)


def test_umltrace::uml::tracedwritelinkaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedWriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedwritelinkaction_is_not_abstract():
    assert not inspect.isabstract(TracedWriteLinkAction)


def test_tracedwritelinkaction_constructor_exists():
    assert callable(TracedWriteLinkAction.__init__)


def test_tracedwritelinkaction_constructor_args():
    sig = inspect.signature(TracedWriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddestroylinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDestroyLinkAction)


def test_umltrace::uml::traceddestroylinkaction_constructor_exists():
    assert callable(umlTrace::uml::TracedDestroyLinkAction.__init__)


def test_umltrace::uml::traceddestroylinkaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcreatelinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedCreateLinkAction)


def test_umltrace::uml::tracedcreatelinkaction_constructor_exists():
    assert callable(umlTrace::uml::TracedCreateLinkAction.__init__)


def test_umltrace::uml::tracedcreatelinkaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedCreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedcreatelinkaction_is_not_abstract():
    assert not inspect.isabstract(TracedCreateLinkAction)


def test_tracedcreatelinkaction_constructor_exists():
    assert callable(TracedCreateLinkAction.__init__)


def test_tracedcreatelinkaction_constructor_args():
    sig = inspect.signature(TracedCreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcreatelinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedCreateLinkObjectAction)


def test_umltrace::uml::tracedcreatelinkobjectaction_constructor_exists():
    assert callable(umlTrace::uml::TracedCreateLinkObjectAction.__init__)


def test_umltrace::uml::tracedcreatelinkobjectaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedCreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(uml::TracedNamedElement)


def test_uml::tracednamedelement_constructor_exists():
    assert callable(uml::TracedNamedElement.__init__)


def test_uml::tracednamedelement_constructor_args():
    sig = inspect.signature(uml::TracedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinclude_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInclude)


def test_umltrace::uml::tracedinclude_constructor_exists():
    assert callable(umlTrace::uml::TracedInclude.__init__)


def test_umltrace::uml::tracedinclude_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInclude.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedextend_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedExtend)


def test_umltrace::uml::tracedextend_constructor_exists():
    assert callable(umlTrace::uml::TracedExtend.__init__)


def test_umltrace::uml::tracedextend_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedExtend.__init__)
    params = list(sig.parameters.keys())



def test_activitycontent_is_not_abstract():
    assert not inspect.isabstract(ActivityContent)


def test_activitycontent_constructor_exists():
    assert callable(ActivityContent.__init__)


def test_activitycontent_constructor_args():
    sig = inspect.signature(ActivityContent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedactivitygroup_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedActivityGroup)


def test_umltrace::uml::tracedactivitygroup_constructor_exists():
    assert callable(umlTrace::uml::TracedActivityGroup.__init__)


def test_umltrace::uml::tracedactivitygroup_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedredefinableelement_is_not_abstract():
    assert not inspect.isabstract(uml::TracedRedefinableElement)


def test_uml::tracedredefinableelement_constructor_exists():
    assert callable(uml::TracedRedefinableElement.__init__)


def test_uml::tracedredefinableelement_constructor_args():
    sig = inspect.signature(uml::TracedRedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedredefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedRedefinableTemplateSignature)


def test_umltrace::uml::tracedredefinabletemplatesignature_constructor_exists():
    assert callable(umlTrace::uml::TracedRedefinableTemplateSignature.__init__)


def test_umltrace::uml::tracedredefinabletemplatesignature_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedRedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedActivityNode)


def test_umltrace::uml::tracedactivitynode_constructor_exists():
    assert callable(umlTrace::uml::TracedActivityNode.__init__)


def test_umltrace::uml::tracedactivitynode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(TracedActivityNode)


def test_tracedactivitynode_constructor_exists():
    assert callable(TracedActivityNode.__init__)


def test_tracedactivitynode_constructor_args():
    sig = inspect.signature(TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedControlNode)


def test_umltrace::uml::tracedcontrolnode_constructor_exists():
    assert callable(umlTrace::uml::TracedControlNode.__init__)


def test_umltrace::uml::tracedcontrolnode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedexecutablenode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedExecutableNode)


def test_umltrace::uml::tracedexecutablenode_constructor_exists():
    assert callable(umlTrace::uml::TracedExecutableNode.__init__)


def test_umltrace::uml::tracedexecutablenode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedexecutablenode_is_not_abstract():
    assert not inspect.isabstract(TracedExecutableNode)


def test_tracedexecutablenode_constructor_exists():
    assert callable(TracedExecutableNode.__init__)


def test_tracedexecutablenode_constructor_args():
    sig = inspect.signature(TracedExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedAction)


def test_umltrace::uml::tracedaction_constructor_exists():
    assert callable(umlTrace::uml::TracedAction.__init__)


def test_umltrace::uml::tracedaction_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedactivitygroup_is_not_abstract():
    assert not inspect.isabstract(uml::TracedActivityGroup)


def test_uml::tracedactivitygroup_constructor_exists():
    assert callable(uml::TracedActivityGroup.__init__)


def test_uml::tracedactivitygroup_constructor_args():
    sig = inspect.signature(uml::TracedActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracednamespace_is_not_abstract():
    assert not inspect.isabstract(uml::TracedNamespace)


def test_uml::tracednamespace_constructor_exists():
    assert callable(uml::TracedNamespace.__init__)


def test_uml::tracednamespace_constructor_args():
    sig = inspect.signature(uml::TracedNamespace.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtransition_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTransition)


def test_umltrace::uml::tracedtransition_constructor_exists():
    assert callable(umlTrace::uml::TracedTransition.__init__)


def test_umltrace::uml::tracedtransition_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTransition.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinteractionoperand_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInteractionOperand)


def test_umltrace::uml::tracedinteractionoperand_constructor_exists():
    assert callable(umlTrace::uml::TracedInteractionOperand.__init__)


def test_umltrace::uml::tracedinteractionoperand_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedregion_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedRegion)


def test_umltrace::uml::tracedregion_constructor_exists():
    assert callable(umlTrace::uml::TracedRegion.__init__)


def test_umltrace::uml::tracedregion_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedRegion.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedpackage_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedPackage)


def test_umltrace::uml::tracedpackage_constructor_exists():
    assert callable(umlTrace::uml::TracedPackage.__init__)


def test_umltrace::uml::tracedpackage_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedPackage.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedstate_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedState)


def test_umltrace::uml::tracedstate_constructor_exists():
    assert callable(umlTrace::uml::TracedState.__init__)


def test_umltrace::uml::tracedstate_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedState.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedbehavioralfeature_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedBehavioralFeature)


def test_umltrace::uml::tracedbehavioralfeature_constructor_exists():
    assert callable(umlTrace::uml::TracedBehavioralFeature.__init__)


def test_umltrace::uml::tracedbehavioralfeature_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedBehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedclassifier_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedClassifier)


def test_umltrace::uml::tracedclassifier_constructor_exists():
    assert callable(umlTrace::uml::TracedClassifier.__init__)


def test_umltrace::uml::tracedclassifier_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedAction)


def test_uml::tracedaction_constructor_exists():
    assert callable(uml::TracedAction.__init__)


def test_uml::tracedaction_constructor_args():
    sig = inspect.signature(uml::TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedstructuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedStructuredActivityNode)


def test_umltrace::uml::tracedstructuredactivitynode_constructor_exists():
    assert callable(umlTrace::uml::TracedStructuredActivityNode.__init__)


def test_umltrace::uml::tracedstructuredactivitynode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedStructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedstructuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(TracedStructuredActivityNode)


def test_tracedstructuredactivitynode_constructor_exists():
    assert callable(TracedStructuredActivityNode.__init__)


def test_tracedstructuredactivitynode_constructor_args():
    sig = inspect.signature(TracedStructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedexpansionregion_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedExpansionRegion)


def test_umltrace::uml::tracedexpansionregion_constructor_exists():
    assert callable(umlTrace::uml::TracedExpansionRegion.__init__)


def test_umltrace::uml::tracedexpansionregion_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedloopnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLoopNode)


def test_umltrace::uml::tracedloopnode_constructor_exists():
    assert callable(umlTrace::uml::TracedLoopNode.__init__)


def test_umltrace::uml::tracedloopnode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLoopNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedsequencenode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedSequenceNode)


def test_umltrace::uml::tracedsequencenode_constructor_exists():
    assert callable(umlTrace::uml::TracedSequenceNode.__init__)


def test_umltrace::uml::tracedsequencenode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedSequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedconditionalnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedConditionalNode)


def test_umltrace::uml::tracedconditionalnode_constructor_exists():
    assert callable(umlTrace::uml::TracedConditionalNode.__init__)


def test_umltrace::uml::tracedconditionalnode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedemodelelement_is_not_abstract():
    assert not inspect.isabstract(TracedEModelElement)


def test_tracedemodelelement_constructor_exists():
    assert callable(TracedEModelElement.__init__)


def test_tracedemodelelement_constructor_args():
    sig = inspect.signature(TracedEModelElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedElement)


def test_umltrace::uml::tracedelement_constructor_exists():
    assert callable(umlTrace::uml::TracedElement.__init__)


def test_umltrace::uml::tracedelement_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedElement.__init__)
    params = list(sig.parameters.keys())



def test_tracedelement_is_not_abstract():
    assert not inspect.isabstract(TracedElement)


def test_tracedelement_constructor_exists():
    assert callable(TracedElement.__init__)


def test_tracedelement_constructor_args():
    sig = inspect.signature(TracedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTemplateParameter)


def test_umltrace::uml::tracedtemplateparameter_constructor_exists():
    assert callable(umlTrace::uml::TracedTemplateParameter.__init__)


def test_umltrace::uml::tracedtemplateparameter_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedrelationship_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedRelationship)


def test_umltrace::uml::tracedrelationship_constructor_exists():
    assert callable(umlTrace::uml::TracedRelationship.__init__)


def test_umltrace::uml::tracedrelationship_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedlinkenddata_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLinkEndData)


def test_umltrace::uml::tracedlinkenddata_constructor_exists():
    assert callable(umlTrace::uml::TracedLinkEndData.__init__)


def test_umltrace::uml::tracedlinkenddata_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedexceptionhandler_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedExceptionHandler)


def test_umltrace::uml::tracedexceptionhandler_constructor_exists():
    assert callable(umlTrace::uml::TracedExceptionHandler.__init__)


def test_umltrace::uml::tracedexceptionhandler_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedslot_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedSlot)


def test_umltrace::uml::tracedslot_constructor_exists():
    assert callable(umlTrace::uml::TracedSlot.__init__)


def test_umltrace::uml::tracedslot_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedSlot.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtemplateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTemplateParameterSubstitution)


def test_umltrace::uml::tracedtemplateparametersubstitution_constructor_exists():
    assert callable(umlTrace::uml::TracedTemplateParameterSubstitution.__init__)


def test_umltrace::uml::tracedtemplateparametersubstitution_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtemplatesignature_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTemplateSignature)


def test_umltrace::uml::tracedtemplatesignature_constructor_exists():
    assert callable(umlTrace::uml::TracedTemplateSignature.__init__)


def test_umltrace::uml::tracedtemplatesignature_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcomment_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedComment)


def test_umltrace::uml::tracedcomment_constructor_exists():
    assert callable(umlTrace::uml::TracedComment.__init__)


def test_umltrace::uml::tracedcomment_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedComment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedmultiplicityelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedMultiplicityElement)


def test_umltrace::uml::tracedmultiplicityelement_constructor_exists():
    assert callable(umlTrace::uml::TracedMultiplicityElement.__init__)


def test_umltrace::uml::tracedmultiplicityelement_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedMultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtemplateableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTemplateableElement)


def test_umltrace::uml::tracedtemplateableelement_constructor_exists():
    assert callable(umlTrace::uml::TracedTemplateableElement.__init__)


def test_umltrace::uml::tracedtemplateableelement_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedclause_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedClause)


def test_umltrace::uml::tracedclause_constructor_exists():
    assert callable(umlTrace::uml::TracedClause.__init__)


def test_umltrace::uml::tracedclause_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedClause.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedimage_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedImage)


def test_umltrace::uml::tracedimage_constructor_exists():
    assert callable(umlTrace::uml::TracedImage.__init__)


def test_umltrace::uml::tracedimage_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedImage.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedqualifiervalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedQualifierValue)


def test_umltrace::uml::tracedqualifiervalue_constructor_exists():
    assert callable(umlTrace::uml::TracedQualifierValue.__init__)


def test_umltrace::uml::tracedqualifiervalue_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedQualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedNamedElement)


def test_umltrace::uml::tracednamedelement_constructor_exists():
    assert callable(umlTrace::uml::TracedNamedElement.__init__)


def test_umltrace::uml::tracednamedelement_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(TracedNamedElement)


def test_tracednamedelement_constructor_exists():
    assert callable(TracedNamedElement.__init__)


def test_tracednamedelement_constructor_args():
    sig = inspect.signature(TracedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtypedelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTypedElement)


def test_umltrace::uml::tracedtypedelement_constructor_exists():
    assert callable(umlTrace::uml::TracedTypedElement.__init__)


def test_umltrace::uml::tracedtypedelement_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracednamespace_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedNamespace)


def test_umltrace::uml::tracednamespace_constructor_exists():
    assert callable(umlTrace::uml::TracedNamespace.__init__)


def test_umltrace::uml::tracednamespace_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedNamespace.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedredefinableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedRedefinableElement)


def test_umltrace::uml::tracedredefinableelement_constructor_exists():
    assert callable(umlTrace::uml::TracedRedefinableElement.__init__)


def test_umltrace::uml::tracedredefinableelement_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedRedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddeploymenttarget_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDeploymentTarget)


def test_umltrace::uml::traceddeploymenttarget_constructor_exists():
    assert callable(umlTrace::uml::TracedDeploymentTarget.__init__)


def test_umltrace::uml::traceddeploymenttarget_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedmessage_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedMessage)


def test_umltrace::uml::tracedmessage_constructor_exists():
    assert callable(umlTrace::uml::TracedMessage.__init__)


def test_umltrace::uml::tracedmessage_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedMessage.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedcollaborationuse_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedCollaborationUse)


def test_umltrace::uml::tracedcollaborationuse_constructor_exists():
    assert callable(umlTrace::uml::TracedCollaborationUse.__init__)


def test_umltrace::uml::tracedcollaborationuse_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedCollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedmessageend_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedMessageEnd)


def test_umltrace::uml::tracedmessageend_constructor_exists():
    assert callable(umlTrace::uml::TracedMessageEnd.__init__)


def test_umltrace::uml::tracedmessageend_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedMessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedgeneralordering_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedGeneralOrdering)


def test_umltrace::uml::tracedgeneralordering_constructor_exists():
    assert callable(umlTrace::uml::TracedGeneralOrdering.__init__)


def test_umltrace::uml::tracedgeneralordering_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedGeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedparameterset_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedParameterSet)


def test_umltrace::uml::tracedparameterset_constructor_exists():
    assert callable(umlTrace::uml::TracedParameterSet.__init__)


def test_umltrace::uml::tracedparameterset_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtrigger_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTrigger)


def test_umltrace::uml::tracedtrigger_constructor_exists():
    assert callable(umlTrace::uml::TracedTrigger.__init__)


def test_umltrace::uml::tracedtrigger_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTrigger.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedlifeline_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedLifeline)


def test_umltrace::uml::tracedlifeline_constructor_exists():
    assert callable(umlTrace::uml::TracedLifeline.__init__)


def test_umltrace::uml::tracedlifeline_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedLifeline.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddeployedartifact_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDeployedArtifact)


def test_umltrace::uml::traceddeployedartifact_constructor_exists():
    assert callable(umlTrace::uml::TracedDeployedArtifact.__init__)


def test_umltrace::uml::traceddeployedartifact_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinteractionfragment_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInteractionFragment)


def test_umltrace::uml::tracedinteractionfragment_constructor_exists():
    assert callable(umlTrace::uml::TracedInteractionFragment.__init__)


def test_umltrace::uml::tracedinteractionfragment_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedOccurrenceSpecification)


def test_umltrace::uml::tracedoccurrencespecification_constructor_exists():
    assert callable(umlTrace::uml::TracedOccurrenceSpecification.__init__)


def test_umltrace::uml::tracedoccurrencespecification_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedmessageend_is_not_abstract():
    assert not inspect.isabstract(uml::TracedMessageEnd)


def test_uml::tracedmessageend_constructor_exists():
    assert callable(uml::TracedMessageEnd.__init__)


def test_uml::tracedmessageend_constructor_args():
    sig = inspect.signature(uml::TracedMessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedmessageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedMessageOccurrenceSpecification)


def test_umltrace::uml::tracedmessageoccurrencespecification_constructor_exists():
    assert callable(umlTrace::uml::TracedMessageOccurrenceSpecification.__init__)


def test_umltrace::uml::tracedmessageoccurrencespecification_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedMessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_tracedmessageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(TracedMessageOccurrenceSpecification)


def test_tracedmessageoccurrencespecification_constructor_exists():
    assert callable(TracedMessageOccurrenceSpecification.__init__)


def test_tracedmessageoccurrencespecification_constructor_args():
    sig = inspect.signature(TracedMessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddestructionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDestructionOccurrenceSpecification)


def test_umltrace::uml::traceddestructionoccurrencespecification_constructor_exists():
    assert callable(umlTrace::uml::TracedDestructionOccurrenceSpecification.__init__)


def test_umltrace::uml::traceddestructionoccurrencespecification_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDestructionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedvertex_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedVertex)


def test_umltrace::uml::tracedvertex_constructor_exists():
    assert callable(umlTrace::uml::TracedVertex.__init__)


def test_umltrace::uml::tracedvertex_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedVertex.__init__)
    params = list(sig.parameters.keys())



def test_tracedvertex_is_not_abstract():
    assert not inspect.isabstract(TracedVertex)


def test_tracedvertex_constructor_exists():
    assert callable(TracedVertex.__init__)


def test_tracedvertex_constructor_args():
    sig = inspect.signature(TracedVertex.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedconnectionpointreference_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedConnectionPointReference)


def test_umltrace::uml::tracedconnectionpointreference_constructor_exists():
    assert callable(umlTrace::uml::TracedConnectionPointReference.__init__)


def test_umltrace::uml::tracedconnectionpointreference_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedpseudostate_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedPseudostate)


def test_umltrace::uml::tracedpseudostate_constructor_exists():
    assert callable(umlTrace::uml::TracedPseudostate.__init__)


def test_umltrace::uml::tracedpseudostate_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedPseudostate.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedparameterableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedParameterableElement)


def test_umltrace::uml::tracedparameterableelement_constructor_exists():
    assert callable(umlTrace::uml::TracedParameterableElement.__init__)


def test_umltrace::uml::tracedparameterableelement_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedparameterableelement_is_not_abstract():
    assert not inspect.isabstract(uml::TracedParameterableElement)


def test_uml::tracedparameterableelement_constructor_exists():
    assert callable(uml::TracedParameterableElement.__init__)


def test_uml::tracedparameterableelement_constructor_args():
    sig = inspect.signature(uml::TracedParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedconnectableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedConnectableElement)


def test_umltrace::uml::tracedconnectableelement_constructor_exists():
    assert callable(umlTrace::uml::TracedConnectableElement.__init__)


def test_umltrace::uml::tracedconnectableelement_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedoperation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedOperation)


def test_umltrace::uml::tracedoperation_constructor_exists():
    assert callable(umlTrace::uml::TracedOperation.__init__)


def test_umltrace::uml::tracedoperation_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedOperation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedpackageableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedPackageableElement)


def test_umltrace::uml::tracedpackageableelement_constructor_exists():
    assert callable(umlTrace::uml::TracedPackageableElement.__init__)


def test_umltrace::uml::tracedpackageableelement_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_tracedpackageableelement_is_not_abstract():
    assert not inspect.isabstract(TracedPackageableElement)


def test_tracedpackageableelement_constructor_exists():
    assert callable(TracedPackageableElement.__init__)


def test_tracedpackageableelement_constructor_args():
    sig = inspect.signature(TracedPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedobservation_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedObservation)


def test_umltrace::uml::tracedobservation_constructor_exists():
    assert callable(umlTrace::uml::TracedObservation.__init__)


def test_umltrace::uml::tracedobservation_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedObservation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedEvent)


def test_umltrace::uml::tracedevent_constructor_exists():
    assert callable(umlTrace::uml::TracedEvent.__init__)


def test_umltrace::uml::tracedevent_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedgeneralizationset_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedGeneralizationSet)


def test_umltrace::uml::tracedgeneralizationset_constructor_exists():
    assert callable(umlTrace::uml::TracedGeneralizationSet.__init__)


def test_umltrace::uml::tracedgeneralizationset_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedGeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtype_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedType)


def test_umltrace::uml::tracedtype_constructor_exists():
    assert callable(umlTrace::uml::TracedType.__init__)


def test_umltrace::uml::tracedtype_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedType.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedConstraint)


def test_umltrace::uml::tracedconstraint_constructor_exists():
    assert callable(umlTrace::uml::TracedConstraint.__init__)


def test_umltrace::uml::tracedconstraint_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tracedconstraint_is_not_abstract():
    assert not inspect.isabstract(TracedConstraint)


def test_tracedconstraint_constructor_exists():
    assert callable(TracedConstraint.__init__)


def test_tracedconstraint_constructor_args():
    sig = inspect.signature(TracedConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedinteractionconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedInteractionConstraint)


def test_umltrace::uml::tracedinteractionconstraint_constructor_exists():
    assert callable(umlTrace::uml::TracedInteractionConstraint.__init__)


def test_umltrace::uml::tracedinteractionconstraint_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedInteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedintervalconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedIntervalConstraint)


def test_umltrace::uml::tracedintervalconstraint_constructor_exists():
    assert callable(umlTrace::uml::TracedIntervalConstraint.__init__)


def test_umltrace::uml::tracedintervalconstraint_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedIntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tracedintervalconstraint_is_not_abstract():
    assert not inspect.isabstract(TracedIntervalConstraint)


def test_tracedintervalconstraint_constructor_exists():
    assert callable(TracedIntervalConstraint.__init__)


def test_tracedintervalconstraint_constructor_args():
    sig = inspect.signature(TracedIntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedtimeconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedTimeConstraint)


def test_umltrace::uml::tracedtimeconstraint_constructor_exists():
    assert callable(umlTrace::uml::TracedTimeConstraint.__init__)


def test_umltrace::uml::tracedtimeconstraint_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedTimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::traceddurationconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedDurationConstraint)


def test_umltrace::uml::traceddurationconstraint_constructor_exists():
    assert callable(umlTrace::uml::TracedDurationConstraint.__init__)


def test_umltrace::uml::traceddurationconstraint_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedDurationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcontrolflow_is_not_abstract():
    assert not inspect.isabstract(uml::TracedControlFlow)


def test_uml::tracedcontrolflow_constructor_exists():
    assert callable(uml::TracedControlFlow.__init__)


def test_uml::tracedcontrolflow_constructor_args():
    sig = inspect.signature(uml::TracedControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtimeobservation_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTimeObservation)


def test_uml::tracedtimeobservation_constructor_exists():
    assert callable(uml::TracedTimeObservation.__init__)


def test_uml::tracedtimeobservation_constructor_args():
    sig = inspect.signature(uml::TracedTimeObservation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedgate_is_not_abstract():
    assert not inspect.isabstract(uml::TracedGate)


def test_uml::tracedgate_constructor_exists():
    assert callable(uml::TracedGate.__init__)


def test_uml::tracedgate_constructor_args():
    sig = inspect.signature(uml::TracedGate.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedprotocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(uml::TracedProtocolStateMachine)


def test_uml::tracedprotocolstatemachine_constructor_exists():
    assert callable(uml::TracedProtocolStateMachine.__init__)


def test_uml::tracedprotocolstatemachine_constructor_args():
    sig = inspect.signature(uml::TracedProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddatastorenode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDataStoreNode)


def test_uml::traceddatastorenode_constructor_exists():
    assert callable(uml::TracedDataStoreNode.__init__)


def test_uml::traceddatastorenode_constructor_args():
    sig = inspect.signature(uml::TracedDataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedreadstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedReadStructuralFeatureAction)


def test_uml::tracedreadstructuralfeatureaction_constructor_exists():
    assert callable(uml::TracedReadStructuralFeatureAction.__init__)


def test_uml::tracedreadstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml::TracedReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedanyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(uml::TracedAnyReceiveEvent)


def test_uml::tracedanyreceiveevent_constructor_exists():
    assert callable(uml::TracedAnyReceiveEvent.__init__)


def test_uml::tracedanyreceiveevent_constructor_args():
    sig = inspect.signature(uml::TracedAnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_kernel::tracedintegervalue_is_not_abstract():
    assert not inspect.isabstract(Kernel::TracedIntegerValue)


def test_kernel::tracedintegervalue_constructor_exists():
    assert callable(Kernel::TracedIntegerValue.__init__)


def test_kernel::tracedintegervalue_constructor_args():
    sig = inspect.signature(Kernel::TracedIntegerValue.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinterval_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInterval)


def test_uml::tracedinterval_constructor_exists():
    assert callable(uml::TracedInterval.__init__)


def test_uml::tracedinterval_constructor_args():
    sig = inspect.signature(uml::TracedInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedremovestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedRemoveStructuralFeatureValueAction)


def test_uml::tracedremovestructuralfeaturevalueaction_constructor_exists():
    assert callable(uml::TracedRemoveStructuralFeatureValueAction.__init__)


def test_uml::tracedremovestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml::TracedRemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedgeneralization_is_not_abstract():
    assert not inspect.isabstract(uml::TracedGeneralization)


def test_uml::tracedgeneralization_constructor_exists():
    assert callable(uml::TracedGeneralization.__init__)


def test_uml::tracedgeneralization_constructor_args():
    sig = inspect.signature(uml::TracedGeneralization.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinteractionoperand_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInteractionOperand)


def test_uml::tracedinteractionoperand_constructor_exists():
    assert callable(uml::TracedInteractionOperand.__init__)


def test_uml::tracedinteractionoperand_constructor_args():
    sig = inspect.signature(uml::TracedInteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedprotocoltransition_is_not_abstract():
    assert not inspect.isabstract(uml::TracedProtocolTransition)


def test_uml::tracedprotocoltransition_constructor_exists():
    assert callable(uml::TracedProtocolTransition.__init__)


def test_uml::tracedprotocoltransition_constructor_args():
    sig = inspect.signature(uml::TracedProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinterruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInterruptibleActivityRegion)


def test_uml::tracedinterruptibleactivityregion_constructor_exists():
    assert callable(uml::TracedInterruptibleActivityRegion.__init__)


def test_uml::tracedinterruptibleactivityregion_constructor_args():
    sig = inspect.signature(uml::TracedInterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedpartdecomposition_is_not_abstract():
    assert not inspect.isabstract(uml::TracedPartDecomposition)


def test_uml::tracedpartdecomposition_constructor_exists():
    assert callable(uml::TracedPartDecomposition.__init__)


def test_uml::tracedpartdecomposition_constructor_args():
    sig = inspect.signature(uml::TracedPartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtimeevent_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTimeEvent)


def test_uml::tracedtimeevent_constructor_exists():
    assert callable(uml::TracedTimeEvent.__init__)


def test_uml::tracedtimeevent_constructor_args():
    sig = inspect.signature(uml::TracedTimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddeployment_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDeployment)


def test_uml::traceddeployment_constructor_exists():
    assert callable(uml::TracedDeployment.__init__)


def test_uml::traceddeployment_constructor_args():
    sig = inspect.signature(uml::TracedDeployment.__init__)
    params = list(sig.parameters.keys())



def test_loci::tracedsemanticvisitor_is_not_abstract():
    assert not inspect.isabstract(Loci::TracedSemanticVisitor)


def test_loci::tracedsemanticvisitor_constructor_exists():
    assert callable(Loci::TracedSemanticVisitor.__init__)


def test_loci::tracedsemanticvisitor_constructor_args():
    sig = inspect.signature(Loci::TracedSemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_kernel::tracedobject_is_not_abstract():
    assert not inspect.isabstract(Kernel::TracedObject)


def test_kernel::tracedobject_constructor_exists():
    assert callable(Kernel::TracedObject.__init__)


def test_kernel::tracedobject_constructor_args():
    sig = inspect.signature(Kernel::TracedObject.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::tracedjoinnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::TracedJoinNodeActivation)


def test_intermediateactivities::tracedjoinnodeactivation_constructor_exists():
    assert callable(IntermediateActivities::TracedJoinNodeActivation.__init__)


def test_intermediateactivities::tracedjoinnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities::TracedJoinNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedusecase_is_not_abstract():
    assert not inspect.isabstract(uml::TracedUseCase)


def test_uml::tracedusecase_constructor_exists():
    assert callable(uml::TracedUseCase.__init__)


def test_uml::tracedusecase_constructor_args():
    sig = inspect.signature(uml::TracedUseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedreclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedReclassifyObjectAction)


def test_uml::tracedreclassifyobjectaction_constructor_exists():
    assert callable(uml::TracedReclassifyObjectAction.__init__)


def test_uml::tracedreclassifyobjectaction_constructor_args():
    sig = inspect.signature(uml::TracedReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinstancevalue_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInstanceValue)


def test_uml::tracedinstancevalue_constructor_exists():
    assert callable(uml::TracedInstanceValue.__init__)


def test_uml::tracedinstancevalue_constructor_args():
    sig = inspect.signature(uml::TracedInstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions::tracedaddstructuralfeaturevalueactionactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions::TracedAddStructuralFeatureValueActionActivation)


def test_intermediateactions::tracedaddstructuralfeaturevalueactionactivation_constructor_exists():
    assert callable(IntermediateActions::TracedAddStructuralFeatureValueActionActivation.__init__)


def test_intermediateactions::tracedaddstructuralfeaturevalueactionactivation_constructor_args():
    sig = inspect.signature(IntermediateActions::TracedAddStructuralFeatureValueActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_kernel::tracedreference_is_not_abstract():
    assert not inspect.isabstract(Kernel::TracedReference)


def test_kernel::tracedreference_constructor_exists():
    assert callable(Kernel::TracedReference.__init__)


def test_kernel::tracedreference_constructor_args():
    sig = inspect.signature(Kernel::TracedReference.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedforknode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedForkNode)


def test_uml::tracedforknode_constructor_exists():
    assert callable(uml::TracedForkNode.__init__)


def test_uml::tracedforknode_constructor_args():
    sig = inspect.signature(uml::TracedForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedactivity_is_not_abstract():
    assert not inspect.isabstract(uml::TracedActivity)


def test_uml::tracedactivity_constructor_exists():
    assert callable(uml::TracedActivity.__init__)


def test_uml::tracedactivity_constructor_args():
    sig = inspect.signature(uml::TracedActivity.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedmessage_is_not_abstract():
    assert not inspect.isabstract(uml::TracedMessage)


def test_uml::tracedmessage_constructor_exists():
    assert callable(uml::TracedMessage.__init__)


def test_uml::tracedmessage_constructor_args():
    sig = inspect.signature(uml::TracedMessage.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedstatemachine_is_not_abstract():
    assert not inspect.isabstract(uml::TracedStateMachine)


def test_uml::tracedstatemachine_constructor_exists():
    assert callable(uml::TracedStateMachine.__init__)


def test_uml::tracedstatemachine_constructor_args():
    sig = inspect.signature(uml::TracedStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedactivitypartition_is_not_abstract():
    assert not inspect.isabstract(uml::TracedActivityPartition)


def test_uml::tracedactivitypartition_constructor_exists():
    assert callable(uml::TracedActivityPartition.__init__)


def test_uml::tracedactivitypartition_constructor_args():
    sig = inspect.signature(uml::TracedActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::tracedactivityparameternodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::TracedActivityParameterNodeActivation)


def test_intermediateactivities::tracedactivityparameternodeactivation_constructor_exists():
    assert callable(IntermediateActivities::TracedActivityParameterNodeActivation.__init__)


def test_intermediateactivities::tracedactivityparameternodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities::TracedActivityParameterNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_basicactions::tracedcallbehavioractionactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions::TracedCallBehaviorActionActivation)


def test_basicactions::tracedcallbehavioractionactivation_constructor_exists():
    assert callable(BasicActions::TracedCallBehaviorActionActivation.__init__)


def test_basicactions::tracedcallbehavioractionactivation_constructor_args():
    sig = inspect.signature(BasicActions::TracedCallBehaviorActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddestroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDestroyObjectAction)


def test_uml::traceddestroyobjectaction_constructor_exists():
    assert callable(uml::TracedDestroyObjectAction.__init__)


def test_uml::traceddestroyobjectaction_constructor_args():
    sig = inspect.signature(uml::TracedDestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedassociationclass_is_not_abstract():
    assert not inspect.isabstract(uml::TracedAssociationClass)


def test_uml::tracedassociationclass_constructor_exists():
    assert callable(uml::TracedAssociationClass.__init__)


def test_uml::tracedassociationclass_constructor_args():
    sig = inspect.signature(uml::TracedAssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinformationflow_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInformationFlow)


def test_uml::tracedinformationflow_constructor_exists():
    assert callable(uml::TracedInformationFlow.__init__)


def test_uml::tracedinformationflow_constructor_args():
    sig = inspect.signature(uml::TracedInformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedsubstitution_is_not_abstract():
    assert not inspect.isabstract(uml::TracedSubstitution)


def test_uml::tracedsubstitution_constructor_exists():
    assert callable(uml::TracedSubstitution.__init__)


def test_uml::tracedsubstitution_constructor_args():
    sig = inspect.signature(uml::TracedSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedenumerationliteral_is_not_abstract():
    assert not inspect.isabstract(uml::TracedEnumerationLiteral)


def test_uml::tracedenumerationliteral_constructor_exists():
    assert callable(uml::TracedEnumerationLiteral.__init__)


def test_uml::tracedenumerationliteral_constructor_args():
    sig = inspect.signature(uml::TracedEnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedstereotype_is_not_abstract():
    assert not inspect.isabstract(uml::TracedStereotype)


def test_uml::tracedstereotype_constructor_exists():
    assert callable(uml::TracedStereotype.__init__)


def test_uml::tracedstereotype_constructor_args():
    sig = inspect.signature(uml::TracedStereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedacceptcallaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedAcceptCallAction)


def test_uml::tracedacceptcallaction_constructor_exists():
    assert callable(uml::TracedAcceptCallAction.__init__)


def test_uml::tracedacceptcallaction_constructor_args():
    sig = inspect.signature(uml::TracedAcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinstancespecification_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInstanceSpecification)


def test_uml::tracedinstancespecification_constructor_exists():
    assert callable(uml::TracedInstanceSpecification.__init__)


def test_uml::tracedinstancespecification_constructor_args():
    sig = inspect.signature(uml::TracedInstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_integerfunctions::tracedintegerlessfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution)


def test_integerfunctions::tracedintegerlessfunctionbehaviorexecution_constructor_exists():
    assert callable(IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution.__init__)


def test_integerfunctions::tracedintegerlessfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedstateinvariant_is_not_abstract():
    assert not inspect.isabstract(uml::TracedStateInvariant)


def test_uml::tracedstateinvariant_constructor_exists():
    assert callable(uml::TracedStateInvariant.__init__)


def test_uml::tracedstateinvariant_constructor_args():
    sig = inspect.signature(uml::TracedStateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_basicactions::tracedinputpinactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions::TracedInputPinActivation)


def test_basicactions::tracedinputpinactivation_constructor_exists():
    assert callable(BasicActions::TracedInputPinActivation.__init__)


def test_basicactions::tracedinputpinactivation_constructor_args():
    sig = inspect.signature(BasicActions::TracedInputPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedliteralstring_is_not_abstract():
    assert not inspect.isabstract(uml::TracedLiteralString)


def test_uml::tracedliteralstring_constructor_exists():
    assert callable(uml::TracedLiteralString.__init__)


def test_uml::tracedliteralstring_constructor_args():
    sig = inspect.signature(uml::TracedLiteralString.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedopaqueexpression_is_not_abstract():
    assert not inspect.isabstract(uml::TracedOpaqueExpression)


def test_uml::tracedopaqueexpression_constructor_exists():
    assert callable(uml::TracedOpaqueExpression.__init__)


def test_uml::tracedopaqueexpression_constructor_args():
    sig = inspect.signature(uml::TracedOpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedparameter_is_not_abstract():
    assert not inspect.isabstract(uml::TracedParameter)


def test_uml::tracedparameter_constructor_exists():
    assert callable(uml::TracedParameter.__init__)


def test_uml::tracedparameter_constructor_args():
    sig = inspect.signature(uml::TracedParameter.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::tracedactivitynodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::TracedActivityNodeActivation)


def test_intermediateactivities::tracedactivitynodeactivation_constructor_exists():
    assert callable(IntermediateActivities::TracedActivityNodeActivation.__init__)


def test_intermediateactivities::tracedactivitynodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities::TracedActivityNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinteraction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInteraction)


def test_uml::tracedinteraction_constructor_exists():
    assert callable(uml::TracedInteraction.__init__)


def test_uml::tracedinteraction_constructor_args():
    sig = inspect.signature(uml::TracedInteraction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedbroadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedBroadcastSignalAction)


def test_uml::tracedbroadcastsignalaction_constructor_exists():
    assert callable(uml::TracedBroadcastSignalAction.__init__)


def test_uml::tracedbroadcastsignalaction_constructor_args():
    sig = inspect.signature(uml::TracedBroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedconstraint_is_not_abstract():
    assert not inspect.isabstract(uml::TracedConstraint)


def test_uml::tracedconstraint_constructor_exists():
    assert callable(uml::TracedConstraint.__init__)


def test_uml::tracedconstraint_constructor_args():
    sig = inspect.signature(uml::TracedConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedclearvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedClearVariableAction)


def test_uml::tracedclearvariableaction_constructor_exists():
    assert callable(uml::TracedClearVariableAction.__init__)


def test_uml::tracedclearvariableaction_constructor_args():
    sig = inspect.signature(uml::TracedClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinputpin_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInputPin)


def test_uml::tracedinputpin_constructor_exists():
    assert callable(uml::TracedInputPin.__init__)


def test_uml::tracedinputpin_constructor_args():
    sig = inspect.signature(uml::TracedInputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedtimeconstraint_is_not_abstract():
    assert not inspect.isabstract(uml::TracedTimeConstraint)


def test_uml::tracedtimeconstraint_constructor_exists():
    assert callable(uml::TracedTimeConstraint.__init__)


def test_uml::tracedtimeconstraint_constructor_args():
    sig = inspect.signature(uml::TracedTimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcontinuation_is_not_abstract():
    assert not inspect.isabstract(uml::TracedContinuation)


def test_uml::tracedcontinuation_constructor_exists():
    assert callable(uml::TracedContinuation.__init__)


def test_uml::tracedcontinuation_constructor_args():
    sig = inspect.signature(uml::TracedContinuation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedconsiderignorefragment_is_not_abstract():
    assert not inspect.isabstract(uml::TracedConsiderIgnoreFragment)


def test_uml::tracedconsiderignorefragment_constructor_exists():
    assert callable(uml::TracedConsiderIgnoreFragment.__init__)


def test_uml::tracedconsiderignorefragment_constructor_args():
    sig = inspect.signature(uml::TracedConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedintervalconstraint_is_not_abstract():
    assert not inspect.isabstract(uml::TracedIntervalConstraint)


def test_uml::tracedintervalconstraint_constructor_exists():
    assert callable(uml::TracedIntervalConstraint.__init__)


def test_uml::tracedintervalconstraint_constructor_args():
    sig = inspect.signature(uml::TracedIntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedexecutionenvironment_is_not_abstract():
    assert not inspect.isabstract(uml::TracedExecutionEnvironment)


def test_uml::tracedexecutionenvironment_constructor_exists():
    assert callable(uml::TracedExecutionEnvironment.__init__)


def test_uml::tracedexecutionenvironment_constructor_args():
    sig = inspect.signature(uml::TracedExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedstructuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedStructuredActivityNode)


def test_uml::tracedstructuredactivitynode_constructor_exists():
    assert callable(uml::TracedStructuredActivityNode.__init__)


def test_uml::tracedstructuredactivitynode_constructor_args():
    sig = inspect.signature(uml::TracedStructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedextension_is_not_abstract():
    assert not inspect.isabstract(uml::TracedExtension)


def test_uml::tracedextension_constructor_exists():
    assert callable(uml::TracedExtension.__init__)


def test_uml::tracedextension_constructor_args():
    sig = inspect.signature(uml::TracedExtension.__init__)
    params = list(sig.parameters.keys())



def test_integerfunctions::tracedintegerplusfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution)


def test_integerfunctions::tracedintegerplusfunctionbehaviorexecution_constructor_exists():
    assert callable(IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution.__init__)


def test_integerfunctions::tracedintegerplusfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedextend_is_not_abstract():
    assert not inspect.isabstract(uml::TracedExtend)


def test_uml::tracedextend_constructor_exists():
    assert callable(uml::TracedExtend.__init__)


def test_uml::tracedextend_constructor_args():
    sig = inspect.signature(uml::TracedExtend.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedstartclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedStartClassifierBehaviorAction)


def test_uml::tracedstartclassifierbehavioraction_constructor_exists():
    assert callable(uml::TracedStartClassifierBehaviorAction.__init__)


def test_uml::tracedstartclassifierbehavioraction_constructor_args():
    sig = inspect.signature(uml::TracedStartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedsequencenode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedSequenceNode)


def test_uml::tracedsequencenode_constructor_exists():
    assert callable(uml::TracedSequenceNode.__init__)


def test_uml::tracedsequencenode_constructor_args():
    sig = inspect.signature(uml::TracedSequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedexceptionhandler_is_not_abstract():
    assert not inspect.isabstract(uml::TracedExceptionHandler)


def test_uml::tracedexceptionhandler_constructor_exists():
    assert callable(uml::TracedExceptionHandler.__init__)


def test_uml::tracedexceptionhandler_constructor_args():
    sig = inspect.signature(uml::TracedExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracednode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedNode)


def test_uml::tracednode_constructor_exists():
    assert callable(uml::TracedNode.__init__)


def test_uml::tracednode_constructor_args():
    sig = inspect.signature(uml::TracedNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedvaluepin_is_not_abstract():
    assert not inspect.isabstract(uml::TracedValuePin)


def test_uml::tracedvaluepin_constructor_exists():
    assert callable(uml::TracedValuePin.__init__)


def test_uml::tracedvaluepin_constructor_args():
    sig = inspect.signature(uml::TracedValuePin.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::tracedactivityexecution_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::TracedActivityExecution)


def test_intermediateactivities::tracedactivityexecution_constructor_exists():
    assert callable(IntermediateActivities::TracedActivityExecution.__init__)


def test_intermediateactivities::tracedactivityexecution_constructor_args():
    sig = inspect.signature(IntermediateActivities::TracedActivityExecution.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcollaborationuse_is_not_abstract():
    assert not inspect.isabstract(uml::TracedCollaborationUse)


def test_uml::tracedcollaborationuse_constructor_exists():
    assert callable(uml::TracedCollaborationUse.__init__)


def test_uml::tracedcollaborationuse_constructor_args():
    sig = inspect.signature(uml::TracedCollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::tracedinitialnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::TracedInitialNodeActivation)


def test_intermediateactivities::tracedinitialnodeactivation_constructor_exists():
    assert callable(IntermediateActivities::TracedInitialNodeActivation.__init__)


def test_intermediateactivities::tracedinitialnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities::TracedInitialNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedport_is_not_abstract():
    assert not inspect.isabstract(uml::TracedPort)


def test_uml::tracedport_constructor_exists():
    assert callable(uml::TracedPort.__init__)


def test_uml::tracedport_constructor_args():
    sig = inspect.signature(uml::TracedPort.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddependency_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDependency)


def test_uml::traceddependency_constructor_exists():
    assert callable(uml::TracedDependency.__init__)


def test_uml::traceddependency_constructor_args():
    sig = inspect.signature(uml::TracedDependency.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedchangeevent_is_not_abstract():
    assert not inspect.isabstract(uml::TracedChangeEvent)


def test_uml::tracedchangeevent_constructor_exists():
    assert callable(uml::TracedChangeEvent.__init__)


def test_uml::tracedchangeevent_constructor_args():
    sig = inspect.signature(uml::TracedChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedgeneralizationset_is_not_abstract():
    assert not inspect.isabstract(uml::TracedGeneralizationSet)


def test_uml::tracedgeneralizationset_constructor_exists():
    assert callable(uml::TracedGeneralizationSet.__init__)


def test_uml::tracedgeneralizationset_constructor_args():
    sig = inspect.signature(uml::TracedGeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinteractionuse_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInteractionUse)


def test_uml::tracedinteractionuse_constructor_exists():
    assert callable(uml::TracedInteractionUse.__init__)


def test_uml::tracedinteractionuse_constructor_args():
    sig = inspect.signature(uml::TracedInteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedclass_is_not_abstract():
    assert not inspect.isabstract(uml::TracedClass)


def test_uml::tracedclass_constructor_exists():
    assert callable(uml::TracedClass.__init__)


def test_uml::tracedclass_constructor_args():
    sig = inspect.signature(uml::TracedClass.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracednode_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedNode)


def test_umltrace::uml::tracednode_constructor_exists():
    assert callable(umlTrace::uml::TracedNode.__init__)


def test_umltrace::uml::tracednode_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::uml::tracedassociationclass_is_not_abstract():
    assert not inspect.isabstract(umlTrace::uml::TracedAssociationClass)


def test_umltrace::uml::tracedassociationclass_constructor_exists():
    assert callable(umlTrace::uml::TracedAssociationClass.__init__)


def test_umltrace::uml::tracedassociationclass_constructor_args():
    sig = inspect.signature(umlTrace::uml::TracedAssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedpackageimport_is_not_abstract():
    assert not inspect.isabstract(uml::TracedPackageImport)


def test_uml::tracedpackageimport_constructor_exists():
    assert callable(uml::TracedPackageImport.__init__)


def test_uml::tracedpackageimport_constructor_args():
    sig = inspect.signature(uml::TracedPackageImport.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedsendobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedSendObjectAction)


def test_uml::tracedsendobjectaction_constructor_exists():
    assert callable(uml::TracedSendObjectAction.__init__)


def test_uml::tracedsendobjectaction_constructor_args():
    sig = inspect.signature(uml::TracedSendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedconnector_is_not_abstract():
    assert not inspect.isabstract(uml::TracedConnector)


def test_uml::tracedconnector_constructor_exists():
    assert callable(uml::TracedConnector.__init__)


def test_uml::tracedconnector_constructor_args():
    sig = inspect.signature(uml::TracedConnector.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddestructionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDestructionOccurrenceSpecification)


def test_uml::traceddestructionoccurrencespecification_constructor_exists():
    assert callable(uml::TracedDestructionOccurrenceSpecification.__init__)


def test_uml::traceddestructionoccurrencespecification_constructor_args():
    sig = inspect.signature(uml::TracedDestructionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml::traceddurationconstraint_is_not_abstract():
    assert not inspect.isabstract(uml::TracedDurationConstraint)


def test_uml::traceddurationconstraint_constructor_exists():
    assert callable(uml::TracedDurationConstraint.__init__)


def test_uml::traceddurationconstraint_constructor_args():
    sig = inspect.signature(uml::TracedDurationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities::tracedforknodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities::TracedForkNodeActivation)


def test_intermediateactivities::tracedforknodeactivation_constructor_exists():
    assert callable(IntermediateActivities::TracedForkNodeActivation.__init__)


def test_intermediateactivities::tracedforknodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities::TracedForkNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedlifeline_is_not_abstract():
    assert not inspect.isabstract(uml::TracedLifeline)


def test_uml::tracedlifeline_constructor_exists():
    assert callable(uml::TracedLifeline.__init__)


def test_uml::tracedlifeline_constructor_args():
    sig = inspect.signature(uml::TracedLifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcreateobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedCreateObjectAction)


def test_uml::tracedcreateobjectaction_constructor_exists():
    assert callable(uml::TracedCreateObjectAction.__init__)


def test_uml::tracedcreateobjectaction_constructor_args():
    sig = inspect.signature(uml::TracedCreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedexpansionregion_is_not_abstract():
    assert not inspect.isabstract(uml::TracedExpansionRegion)


def test_uml::tracedexpansionregion_constructor_exists():
    assert callable(uml::TracedExpansionRegion.__init__)


def test_uml::tracedexpansionregion_constructor_args():
    sig = inspect.signature(uml::TracedExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedflowfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedFlowFinalNode)


def test_uml::tracedflowfinalnode_constructor_exists():
    assert callable(uml::TracedFlowFinalNode.__init__)


def test_uml::tracedflowfinalnode_constructor_args():
    sig = inspect.signature(uml::TracedFlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedinitialnode_is_not_abstract():
    assert not inspect.isabstract(uml::TracedInitialNode)


def test_uml::tracedinitialnode_constructor_exists():
    assert callable(uml::TracedInitialNode.__init__)


def test_uml::tracedinitialnode_constructor_args():
    sig = inspect.signature(uml::TracedInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcreatelinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml::TracedCreateLinkObjectAction)


def test_uml::tracedcreatelinkobjectaction_constructor_exists():
    assert callable(uml::TracedCreateLinkObjectAction.__init__)


def test_uml::tracedcreatelinkobjectaction_constructor_args():
    sig = inspect.signature(uml::TracedCreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::tracedcombinedfragment_is_not_abstract():
    assert not inspect.isabstract(uml::TracedCombinedFragment)


def test_uml::tracedcombinedfragment_constructor_exists():
    assert callable(uml::TracedCombinedFragment.__init__)


def test_uml::tracedcombinedfragment_constructor_args():
    sig = inspect.signature(uml::TracedCombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::traced::tracedobjects_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Traced::TracedObjects)


def test_umltrace::traced::tracedobjects_constructor_exists():
    assert callable(umlTrace::Traced::TracedObjects.__init__)


def test_umltrace::traced::tracedobjects_constructor_args():
    sig = inspect.signature(umlTrace::Traced::TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_traced::tracedobjects_is_not_abstract():
    assert not inspect.isabstract(Traced::TracedObjects)


def test_traced::tracedobjects_constructor_exists():
    assert callable(Traced::TracedObjects.__init__)


def test_traced::tracedobjects_constructor_args():
    sig = inspect.signature(Traced::TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::trace_is_not_abstract():
    assert not inspect.isabstract(umlTrace::Trace)


def test_umltrace::trace_constructor_exists():
    assert callable(umlTrace::Trace.__init__)


def test_umltrace::trace_constructor_args():
    sig = inspect.signature(umlTrace::Trace.__init__)
    params = list(sig.parameters.keys())



def test_values::semanticvisitor::runtimemodelelement::value_is_not_abstract():
    assert not inspect.isabstract(Values::SemanticVisitor::runtimeModelElement::Value)


def test_values::semanticvisitor::runtimemodelelement::value_constructor_exists():
    assert callable(Values::SemanticVisitor::runtimeModelElement::Value.__init__)


def test_values::semanticvisitor::runtimemodelelement::value_constructor_args():
    sig = inspect.signature(Values::SemanticVisitor::runtimeModelElement::Value.__init__)
    params = list(sig.parameters.keys())



def test_values::actionactivation::firing::value_is_not_abstract():
    assert not inspect.isabstract(Values::ActionActivation::firing::Value)


def test_values::actionactivation::firing::value_constructor_exists():
    assert callable(Values::ActionActivation::firing::Value.__init__)


def test_values::actionactivation::firing::value_constructor_args():
    sig = inspect.signature(Values::ActionActivation::firing::Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace::state_is_not_abstract():
    assert not inspect.isabstract(umlTrace::State)


def test_umltrace::state_constructor_exists():
    assert callable(umlTrace::State.__init__)


def test_umltrace::state_constructor_args():
    sig = inspect.signature(umlTrace::State.__init__)
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
uml::ActivityContent_strategy = st.builds(
    uml::ActivityContent,
)
BasicActions::TracedActionActivation_strategy = st.builds(
    BasicActions::TracedActionActivation,
)
umlTrace::Values::ActionActivation::firing::Value_strategy = st.builds(
    umlTrace::Values::ActionActivation::firing::Value,
    firing=
        safe_text
)
TracedLiteralEvaluation_strategy = st.builds(
    TracedLiteralEvaluation,
)
umlTrace::Kernel::TracedLiteralIntegerEvaluation_strategy = st.builds(
    umlTrace::Kernel::TracedLiteralIntegerEvaluation,
)
umlTrace::Kernel::TracedLiteralBooleanEvaluation_strategy = st.builds(
    umlTrace::Kernel::TracedLiteralBooleanEvaluation,
)
TracedPrimitiveValue_strategy = st.builds(
    TracedPrimitiveValue,
)
umlTrace::Kernel::TracedBooleanValue_strategy = st.builds(
    umlTrace::Kernel::TracedBooleanValue,
)
umlTrace::Kernel::TracedIntegerValue_strategy = st.builds(
    umlTrace::Kernel::TracedIntegerValue,
)
TracedEvaluation_strategy = st.builds(
    TracedEvaluation,
)
umlTrace::Kernel::TracedLiteralEvaluation_strategy = st.builds(
    umlTrace::Kernel::TracedLiteralEvaluation,
)
TracedValue_strategy = st.builds(
    TracedValue,
)
umlTrace::Kernel::TracedPrimitiveValue_strategy = st.builds(
    umlTrace::Kernel::TracedPrimitiveValue,
)
umlTrace::Kernel::TracedStructuredValue_strategy = st.builds(
    umlTrace::Kernel::TracedStructuredValue,
)
TracedStructuredValue_strategy = st.builds(
    TracedStructuredValue,
)
umlTrace::Kernel::TracedReference_strategy = st.builds(
    umlTrace::Kernel::TracedReference,
)
umlTrace::Kernel::TracedCompoundValue_strategy = st.builds(
    umlTrace::Kernel::TracedCompoundValue,
)
TracedCompoundValue_strategy = st.builds(
    TracedCompoundValue,
)
umlTrace::Kernel::TracedExtensionalValue_strategy = st.builds(
    umlTrace::Kernel::TracedExtensionalValue,
)
TracedExtensionalValue_strategy = st.builds(
    TracedExtensionalValue,
)
umlTrace::Kernel::TracedObject_strategy = st.builds(
    umlTrace::Kernel::TracedObject,
)
TracedObject_strategy = st.builds(
    TracedObject,
)
umlTrace::BasicBehaviors::TracedExecution_strategy = st.builds(
    umlTrace::BasicBehaviors::TracedExecution,
)
uml::TracedElement_strategy = st.builds(
    uml::TracedElement,
)
umlTrace::Values::SemanticVisitor::runtimeModelElement::Value_strategy = st.builds(
    umlTrace::Values::SemanticVisitor::runtimeModelElement::Value,
)
TracedOpaqueBehaviorExecution_strategy = st.builds(
    TracedOpaqueBehaviorExecution,
)
umlTrace::IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution_strategy = st.builds(
    umlTrace::IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution,
)
umlTrace::IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution_strategy = st.builds(
    umlTrace::IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution,
)
umlTrace::IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution_strategy = st.builds(
    umlTrace::IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution,
)
TracedCallActionActivation_strategy = st.builds(
    TracedCallActionActivation,
)
umlTrace::BasicActions::TracedCallBehaviorActionActivation_strategy = st.builds(
    umlTrace::BasicActions::TracedCallBehaviorActionActivation,
)
TracedPinActivation_strategy = st.builds(
    TracedPinActivation,
)
umlTrace::BasicActions::TracedOutputPinActivation_strategy = st.builds(
    umlTrace::BasicActions::TracedOutputPinActivation,
)
umlTrace::BasicActions::TracedInputPinActivation_strategy = st.builds(
    umlTrace::BasicActions::TracedInputPinActivation,
)
TracedInvocationActionActivation_strategy = st.builds(
    TracedInvocationActionActivation,
)
umlTrace::BasicActions::TracedCallActionActivation_strategy = st.builds(
    umlTrace::BasicActions::TracedCallActionActivation,
)
TracedActionActivation_strategy = st.builds(
    TracedActionActivation,
)
umlTrace::BasicActions::TracedOpaqueActionActivation_strategy = st.builds(
    umlTrace::BasicActions::TracedOpaqueActionActivation,
)
umlTrace::BasicActions::TracedInvocationActionActivation_strategy = st.builds(
    umlTrace::BasicActions::TracedInvocationActionActivation,
)
umlTrace::Loci::TracedSemanticVisitor_strategy = st.builds(
    umlTrace::Loci::TracedSemanticVisitor,
)
TracedObjectNodeActivation_strategy = st.builds(
    TracedObjectNodeActivation,
)
umlTrace::BasicActions::TracedPinActivation_strategy = st.builds(
    umlTrace::BasicActions::TracedPinActivation,
)
umlTrace::IntermediateActivities::TracedActivityParameterNodeActivation_strategy = st.builds(
    umlTrace::IntermediateActivities::TracedActivityParameterNodeActivation,
)
umlTrace::IntermediateActions::TracedCreateObjectActionActivation_strategy = st.builds(
    umlTrace::IntermediateActions::TracedCreateObjectActionActivation,
)
umlTrace::IntermediateActions::TracedValueSpecificationActionActivation_strategy = st.builds(
    umlTrace::IntermediateActions::TracedValueSpecificationActionActivation,
)
TracedWriteStructuralFeatureActionActivation_strategy = st.builds(
    TracedWriteStructuralFeatureActionActivation,
)
umlTrace::IntermediateActions::TracedAddStructuralFeatureValueActionActivation_strategy = st.builds(
    umlTrace::IntermediateActions::TracedAddStructuralFeatureValueActionActivation,
)
TracedStructuralFeatureActionActivation_strategy = st.builds(
    TracedStructuralFeatureActionActivation,
)
umlTrace::IntermediateActions::TracedWriteStructuralFeatureActionActivation_strategy = st.builds(
    umlTrace::IntermediateActions::TracedWriteStructuralFeatureActionActivation,
)
umlTrace::IntermediateActions::TracedReadStructuralFeatureActionActivation_strategy = st.builds(
    umlTrace::IntermediateActions::TracedReadStructuralFeatureActionActivation,
)
umlTrace::IntermediateActions::TracedStructuralFeatureActionActivation_strategy = st.builds(
    umlTrace::IntermediateActions::TracedStructuralFeatureActionActivation,
)
umlTrace::ecore::TracedEModelElement_strategy = st.builds(
    umlTrace::ecore::TracedEModelElement,
)
TracedMessageEnd_strategy = st.builds(
    TracedMessageEnd,
)
umlTrace::uml::TracedGate_strategy = st.builds(
    umlTrace::uml::TracedGate,
)
TracedExecution_strategy = st.builds(
    TracedExecution,
)
umlTrace::BasicBehaviors::TracedOpaqueBehaviorExecution_strategy = st.builds(
    umlTrace::BasicBehaviors::TracedOpaqueBehaviorExecution,
)
TracedExecutionSpecification_strategy = st.builds(
    TracedExecutionSpecification,
)
umlTrace::uml::TracedBehaviorExecutionSpecification_strategy = st.builds(
    umlTrace::uml::TracedBehaviorExecutionSpecification,
)
TracedOccurrenceSpecification_strategy = st.builds(
    TracedOccurrenceSpecification,
)
umlTrace::uml::TracedExecutionOccurrenceSpecification_strategy = st.builds(
    umlTrace::uml::TracedExecutionOccurrenceSpecification,
)
TracedOpaqueBehavior_strategy = st.builds(
    TracedOpaqueBehavior,
)
umlTrace::uml::TracedFunctionBehavior_strategy = st.builds(
    umlTrace::uml::TracedFunctionBehavior,
)
uml::TracedStructuredClassifier_strategy = st.builds(
    uml::TracedStructuredClassifier,
)
TracedMultiplicityElement_strategy = st.builds(
    TracedMultiplicityElement,
)
umlTrace::uml::TracedConnectorEnd_strategy = st.builds(
    umlTrace::uml::TracedConnectorEnd,
)
umlTrace::uml::TracedActionExecutionSpecification_strategy = st.builds(
    umlTrace::uml::TracedActionExecutionSpecification,
)
TracedObjectNode_strategy = st.builds(
    TracedObjectNode,
)
umlTrace::uml::TracedExpansionNode_strategy = st.builds(
    umlTrace::uml::TracedExpansionNode,
)
umlTrace::uml::TracedActivityParameterNode_strategy = st.builds(
    umlTrace::uml::TracedActivityParameterNode,
)
umlTrace::uml::TracedCentralBufferNode_strategy = st.builds(
    umlTrace::uml::TracedCentralBufferNode,
)
TracedCentralBufferNode_strategy = st.builds(
    TracedCentralBufferNode,
)
umlTrace::uml::TracedDataStoreNode_strategy = st.builds(
    umlTrace::uml::TracedDataStoreNode,
)
TracedDataType_strategy = st.builds(
    TracedDataType,
)
umlTrace::uml::TracedEnumeration_strategy = st.builds(
    umlTrace::uml::TracedEnumeration,
)
umlTrace::uml::TracedPrimitiveType_strategy = st.builds(
    umlTrace::uml::TracedPrimitiveType,
)
TracedMessageEvent_strategy = st.builds(
    TracedMessageEvent,
)
umlTrace::uml::TracedCallEvent_strategy = st.builds(
    umlTrace::uml::TracedCallEvent,
)
umlTrace::uml::TracedAnyReceiveEvent_strategy = st.builds(
    umlTrace::uml::TracedAnyReceiveEvent,
)
uml::TracedBehavioralFeature_strategy = st.builds(
    uml::TracedBehavioralFeature,
)
TracedTemplateParameter_strategy = st.builds(
    TracedTemplateParameter,
)
umlTrace::uml::TracedConnectableElementTemplateParameter_strategy = st.builds(
    umlTrace::uml::TracedConnectableElementTemplateParameter,
)
umlTrace::uml::TracedClassifierTemplateParameter_strategy = st.builds(
    umlTrace::uml::TracedClassifierTemplateParameter,
)
TracedPackage_strategy = st.builds(
    TracedPackage,
)
umlTrace::uml::TracedProfile_strategy = st.builds(
    umlTrace::uml::TracedProfile,
)
umlTrace::uml::TracedModel_strategy = st.builds(
    umlTrace::uml::TracedModel,
)
TracedTransition_strategy = st.builds(
    TracedTransition,
)
umlTrace::uml::TracedProtocolTransition_strategy = st.builds(
    umlTrace::uml::TracedProtocolTransition,
)
TracedWriteVariableAction_strategy = st.builds(
    TracedWriteVariableAction,
)
umlTrace::uml::TracedRemoveVariableValueAction_strategy = st.builds(
    umlTrace::uml::TracedRemoveVariableValueAction,
)
umlTrace::uml::TracedAddVariableValueAction_strategy = st.builds(
    umlTrace::uml::TracedAddVariableValueAction,
)
TracedInteractionUse_strategy = st.builds(
    TracedInteractionUse,
)
umlTrace::uml::TracedPartDecomposition_strategy = st.builds(
    umlTrace::uml::TracedPartDecomposition,
)
TracedObservation_strategy = st.builds(
    TracedObservation,
)
umlTrace::uml::TracedTimeObservation_strategy = st.builds(
    umlTrace::uml::TracedTimeObservation,
)
umlTrace::uml::TracedDurationObservation_strategy = st.builds(
    umlTrace::uml::TracedDurationObservation,
)
umlTrace::uml::TracedOperationTemplateParameter_strategy = st.builds(
    umlTrace::uml::TracedOperationTemplateParameter,
)
TracedInterval_strategy = st.builds(
    TracedInterval,
)
umlTrace::uml::TracedDurationInterval_strategy = st.builds(
    umlTrace::uml::TracedDurationInterval,
)
umlTrace::uml::TracedTimeInterval_strategy = st.builds(
    umlTrace::uml::TracedTimeInterval,
)
umlTrace::uml::TracedSignalEvent_strategy = st.builds(
    umlTrace::uml::TracedSignalEvent,
)
TracedBehavioralFeature_strategy = st.builds(
    TracedBehavioralFeature,
)
umlTrace::uml::TracedReception_strategy = st.builds(
    umlTrace::uml::TracedReception,
)
TracedDependency_strategy = st.builds(
    TracedDependency,
)
umlTrace::uml::TracedUsage_strategy = st.builds(
    umlTrace::uml::TracedUsage,
)
umlTrace::uml::TracedAbstraction_strategy = st.builds(
    umlTrace::uml::TracedAbstraction,
)
TracedAbstraction_strategy = st.builds(
    TracedAbstraction,
)
umlTrace::uml::TracedManifestation_strategy = st.builds(
    umlTrace::uml::TracedManifestation,
)
umlTrace::uml::TracedRealization_strategy = st.builds(
    umlTrace::uml::TracedRealization,
)
TracedRealization_strategy = st.builds(
    TracedRealization,
)
umlTrace::uml::TracedComponentRealization_strategy = st.builds(
    umlTrace::uml::TracedComponentRealization,
)
umlTrace::uml::TracedInterfaceRealization_strategy = st.builds(
    umlTrace::uml::TracedInterfaceRealization,
)
umlTrace::uml::TracedSubstitution_strategy = st.builds(
    umlTrace::uml::TracedSubstitution,
)
TracedInstanceSpecification_strategy = st.builds(
    TracedInstanceSpecification,
)
umlTrace::uml::TracedEnumerationLiteral_strategy = st.builds(
    umlTrace::uml::TracedEnumerationLiteral,
)
TracedAcceptEventAction_strategy = st.builds(
    TracedAcceptEventAction,
)
umlTrace::uml::TracedAcceptCallAction_strategy = st.builds(
    umlTrace::uml::TracedAcceptCallAction,
)
TracedLinkEndData_strategy = st.builds(
    TracedLinkEndData,
)
umlTrace::uml::TracedLinkEndCreationData_strategy = st.builds(
    umlTrace::uml::TracedLinkEndCreationData,
)
umlTrace::uml::TracedLinkEndDestructionData_strategy = st.builds(
    umlTrace::uml::TracedLinkEndDestructionData,
)
TracedClass_strategy = st.builds(
    TracedClass,
)
umlTrace::uml::TracedComponent_strategy = st.builds(
    umlTrace::uml::TracedComponent,
)
umlTrace::uml::TracedStereotype_strategy = st.builds(
    umlTrace::uml::TracedStereotype,
)
umlTrace::uml::TracedBehavior_strategy = st.builds(
    umlTrace::uml::TracedBehavior,
)
uml::TracedInteractionFragment_strategy = st.builds(
    uml::TracedInteractionFragment,
)
uml::TracedBehavior_strategy = st.builds(
    uml::TracedBehavior,
)
umlTrace::uml::TracedInteraction_strategy = st.builds(
    umlTrace::uml::TracedInteraction,
)
TracedActivityEdge_strategy = st.builds(
    TracedActivityEdge,
)
umlTrace::uml::TracedControlFlow_strategy = st.builds(
    umlTrace::uml::TracedControlFlow,
)
umlTrace::uml::TracedObjectFlow_strategy = st.builds(
    umlTrace::uml::TracedObjectFlow,
)
TracedStateMachine_strategy = st.builds(
    TracedStateMachine,
)
umlTrace::uml::TracedProtocolStateMachine_strategy = st.builds(
    umlTrace::uml::TracedProtocolStateMachine,
)
umlTrace::uml::TracedDeployment_strategy = st.builds(
    umlTrace::uml::TracedDeployment,
)
TracedBehavior_strategy = st.builds(
    TracedBehavior,
)
umlTrace::uml::TracedOpaqueBehavior_strategy = st.builds(
    umlTrace::uml::TracedOpaqueBehavior,
)
umlTrace::uml::TracedActivity_strategy = st.builds(
    umlTrace::uml::TracedActivity,
)
umlTrace::uml::TracedStateMachine_strategy = st.builds(
    umlTrace::uml::TracedStateMachine,
)
TracedActivityGroup_strategy = st.builds(
    TracedActivityGroup,
)
umlTrace::uml::TracedInterruptibleActivityRegion_strategy = st.builds(
    umlTrace::uml::TracedInterruptibleActivityRegion,
)
umlTrace::uml::TracedActivityPartition_strategy = st.builds(
    umlTrace::uml::TracedActivityPartition,
)
uml::TracedRelationship_strategy = st.builds(
    uml::TracedRelationship,
)
umlTrace::IntermediateActivities::TracedActivityExecution_strategy = st.builds(
    umlTrace::IntermediateActivities::TracedActivityExecution,
)
TracedSemanticVisitor_strategy = st.builds(
    TracedSemanticVisitor,
)
umlTrace::Kernel::TracedEvaluation_strategy = st.builds(
    umlTrace::Kernel::TracedEvaluation,
)
umlTrace::Kernel::TracedValue_strategy = st.builds(
    umlTrace::Kernel::TracedValue,
)
umlTrace::IntermediateActivities::TracedActivityNodeActivation_strategy = st.builds(
    umlTrace::IntermediateActivities::TracedActivityNodeActivation,
)
TracedActivityNodeActivation_strategy = st.builds(
    TracedActivityNodeActivation,
)
umlTrace::BasicActions::TracedActionActivation_strategy = st.builds(
    umlTrace::BasicActions::TracedActionActivation,
)
umlTrace::IntermediateActivities::TracedObjectNodeActivation_strategy = st.builds(
    umlTrace::IntermediateActivities::TracedObjectNodeActivation,
)
umlTrace::IntermediateActivities::TracedControlNodeActivation_strategy = st.builds(
    umlTrace::IntermediateActivities::TracedControlNodeActivation,
)
TracedControlNodeActivation_strategy = st.builds(
    TracedControlNodeActivation,
)
umlTrace::IntermediateActivities::TracedInitialNodeActivation_strategy = st.builds(
    umlTrace::IntermediateActivities::TracedInitialNodeActivation,
)
umlTrace::IntermediateActivities::TracedActivityFinalNodeActivation_strategy = st.builds(
    umlTrace::IntermediateActivities::TracedActivityFinalNodeActivation,
)
umlTrace::IntermediateActivities::TracedDecisionNodeActivation_strategy = st.builds(
    umlTrace::IntermediateActivities::TracedDecisionNodeActivation,
)
umlTrace::IntermediateActivities::TracedJoinNodeActivation_strategy = st.builds(
    umlTrace::IntermediateActivities::TracedJoinNodeActivation,
)
umlTrace::IntermediateActivities::TracedMergeNodeActivation_strategy = st.builds(
    umlTrace::IntermediateActivities::TracedMergeNodeActivation,
)
umlTrace::IntermediateActivities::TracedForkNodeActivation_strategy = st.builds(
    umlTrace::IntermediateActivities::TracedForkNodeActivation,
)
uml::TracedVertex_strategy = st.builds(
    uml::TracedVertex,
)
TracedState_strategy = st.builds(
    TracedState,
)
umlTrace::uml::TracedFinalState_strategy = st.builds(
    umlTrace::uml::TracedFinalState,
)
uml::TracedActivityFinalNode_strategy = st.builds(
    uml::TracedActivityFinalNode,
)
uml::TracedClassifierTemplateParameter_strategy = st.builds(
    uml::TracedClassifierTemplateParameter,
)
TracedInteractionFragment_strategy = st.builds(
    TracedInteractionFragment,
)
umlTrace::uml::TracedStateInvariant_strategy = st.builds(
    umlTrace::uml::TracedStateInvariant,
)
umlTrace::uml::TracedExecutionSpecification_strategy = st.builds(
    umlTrace::uml::TracedExecutionSpecification,
)
umlTrace::uml::TracedCombinedFragment_strategy = st.builds(
    umlTrace::uml::TracedCombinedFragment,
)
uml::TracedGeneralOrdering_strategy = st.builds(
    uml::TracedGeneralOrdering,
)
uml::TracedElementImport_strategy = st.builds(
    uml::TracedElementImport,
)
uml::TracedMergeNode_strategy = st.builds(
    uml::TracedMergeNode,
)
uml::TracedClearAssociationAction_strategy = st.builds(
    uml::TracedClearAssociationAction,
)
uml::TracedLinkEndCreationData_strategy = st.builds(
    uml::TracedLinkEndCreationData,
)
uml::TracedPseudostate_strategy = st.builds(
    uml::TracedPseudostate,
)
uml::TracedComponent_strategy = st.builds(
    uml::TracedComponent,
)
uml::TracedReadIsClassifiedObjectAction_strategy = st.builds(
    uml::TracedReadIsClassifiedObjectAction,
)
uml::TracedAbstraction_strategy = st.builds(
    uml::TracedAbstraction,
)
uml::TracedTimeExpression_strategy = st.builds(
    uml::TracedTimeExpression,
)
uml::TracedValueSpecificationAction_strategy = st.builds(
    uml::TracedValueSpecificationAction,
)
uml::TracedFunctionBehavior_strategy = st.builds(
    uml::TracedFunctionBehavior,
)
IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution_strategy = st.builds(
    IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution,
)
IntermediateActivities::TracedMergeNodeActivation_strategy = st.builds(
    IntermediateActivities::TracedMergeNodeActivation,
)
uml::TracedTemplateParameter_strategy = st.builds(
    uml::TracedTemplateParameter,
)
uml::TracedManifestation_strategy = st.builds(
    uml::TracedManifestation,
)
uml::TracedActor_strategy = st.builds(
    uml::TracedActor,
)
uml::TracedRemoveVariableValueAction_strategy = st.builds(
    uml::TracedRemoveVariableValueAction,
)
uml::TracedProfile_strategy = st.builds(
    uml::TracedProfile,
)
uml::TracedTestIdentityAction_strategy = st.builds(
    uml::TracedTestIdentityAction,
)
uml::TracedCollaboration_strategy = st.builds(
    uml::TracedCollaboration,
)
uml::TracedSendSignalAction_strategy = st.builds(
    uml::TracedSendSignalAction,
)
uml::TracedInterfaceRealization_strategy = st.builds(
    uml::TracedInterfaceRealization,
)
uml::TracedUnmarshallAction_strategy = st.builds(
    uml::TracedUnmarshallAction,
)
uml::TracedExpression_strategy = st.builds(
    uml::TracedExpression,
)
uml::TracedAssociation_strategy = st.builds(
    uml::TracedAssociation,
)
uml::TracedClearStructuralFeatureAction_strategy = st.builds(
    uml::TracedClearStructuralFeatureAction,
)
uml::TracedAddVariableValueAction_strategy = st.builds(
    uml::TracedAddVariableValueAction,
)
uml::TracedLiteralReal_strategy = st.builds(
    uml::TracedLiteralReal,
)
IntermediateActions::TracedCreateObjectActionActivation_strategy = st.builds(
    IntermediateActions::TracedCreateObjectActionActivation,
)
uml::TracedSlot_strategy = st.builds(
    uml::TracedSlot,
)
uml::TracedLiteralNull_strategy = st.builds(
    uml::TracedLiteralNull,
)
IntermediateActions::TracedValueSpecificationActionActivation_strategy = st.builds(
    IntermediateActions::TracedValueSpecificationActionActivation,
)
uml::TracedStartObjectBehaviorAction_strategy = st.builds(
    uml::TracedStartObjectBehaviorAction,
)
uml::TracedLiteralBoolean_strategy = st.builds(
    uml::TracedLiteralBoolean,
)
uml::TracedReadLinkAction_strategy = st.builds(
    uml::TracedReadLinkAction,
)
uml::TracedInclude_strategy = st.builds(
    uml::TracedInclude,
)
uml::TracedRegion_strategy = st.builds(
    uml::TracedRegion,
)
uml::TracedState_strategy = st.builds(
    uml::TracedState,
)
uml::TracedPrimitiveType_strategy = st.builds(
    uml::TracedPrimitiveType,
)
uml::TracedStringExpression_strategy = st.builds(
    uml::TracedStringExpression,
)
uml::TracedLinkEndDestructionData_strategy = st.builds(
    uml::TracedLinkEndDestructionData,
)
uml::TracedReadExtentAction_strategy = st.builds(
    uml::TracedReadExtentAction,
)
BasicActions::TracedOutputPinActivation_strategy = st.builds(
    BasicActions::TracedOutputPinActivation,
)
uml::TracedTemplateSignature_strategy = st.builds(
    uml::TracedTemplateSignature,
)
uml::TracedRaiseExceptionAction_strategy = st.builds(
    uml::TracedRaiseExceptionAction,
)
uml::TracedCommunicationPath_strategy = st.builds(
    uml::TracedCommunicationPath,
)
Kernel::TracedLiteralBooleanEvaluation_strategy = st.builds(
    Kernel::TracedLiteralBooleanEvaluation,
)
uml::TracedEnumeration_strategy = st.builds(
    uml::TracedEnumeration,
)
uml::TracedReadLinkObjectEndAction_strategy = st.builds(
    uml::TracedReadLinkObjectEndAction,
)
uml::TracedCallBehaviorAction_strategy = st.builds(
    uml::TracedCallBehaviorAction,
)
uml::TracedVariable_strategy = st.builds(
    uml::TracedVariable,
)
uml::TracedConnectorEnd_strategy = st.builds(
    uml::TracedConnectorEnd,
)
uml::TracedArtifact_strategy = st.builds(
    uml::TracedArtifact,
)
uml::TracedCallOperationAction_strategy = st.builds(
    uml::TracedCallOperationAction,
)
uml::TracedLiteralUnlimitedNatural_strategy = st.builds(
    uml::TracedLiteralUnlimitedNatural,
)
uml::TracedDurationObservation_strategy = st.builds(
    uml::TracedDurationObservation,
)
uml::TracedBehaviorExecutionSpecification_strategy = st.builds(
    uml::TracedBehaviorExecutionSpecification,
)
uml::TracedActivityParameterNode_strategy = st.builds(
    uml::TracedActivityParameterNode,
)
uml::TracedExpansionNode_strategy = st.builds(
    uml::TracedExpansionNode,
)
uml::TracedProfileApplication_strategy = st.builds(
    uml::TracedProfileApplication,
)
uml::TracedAddStructuralFeatureValueAction_strategy = st.builds(
    uml::TracedAddStructuralFeatureValueAction,
)
uml::TracedQualifierValue_strategy = st.builds(
    uml::TracedQualifierValue,
)
uml::TracedImage_strategy = st.builds(
    uml::TracedImage,
)
uml::TracedExtensionEnd_strategy = st.builds(
    uml::TracedExtensionEnd,
)
uml::TracedProperty_strategy = st.builds(
    uml::TracedProperty,
)
uml::TracedDevice_strategy = st.builds(
    uml::TracedDevice,
)
uml::TracedOpaqueAction_strategy = st.builds(
    uml::TracedOpaqueAction,
)
uml::TracedFinalState_strategy = st.builds(
    uml::TracedFinalState,
)
uml::TracedReduceAction_strategy = st.builds(
    uml::TracedReduceAction,
)
uml::TracedDuration_strategy = st.builds(
    uml::TracedDuration,
)
uml::TracedTemplateParameterSubstitution_strategy = st.builds(
    uml::TracedTemplateParameterSubstitution,
)
uml::TracedOutputPin_strategy = st.builds(
    uml::TracedOutputPin,
)
uml::TracedActionExecutionSpecification_strategy = st.builds(
    uml::TracedActionExecutionSpecification,
)
uml::TracedInformationItem_strategy = st.builds(
    uml::TracedInformationItem,
)
uml::TracedOperationTemplateParameter_strategy = st.builds(
    uml::TracedOperationTemplateParameter,
)
uml::TracedConnectableElementTemplateParameter_strategy = st.builds(
    uml::TracedConnectableElementTemplateParameter,
)
uml::TracedLinkEndData_strategy = st.builds(
    uml::TracedLinkEndData,
)
uml::TracedDurationInterval_strategy = st.builds(
    uml::TracedDurationInterval,
)
uml::TracedTransition_strategy = st.builds(
    uml::TracedTransition,
)
uml::TracedTrigger_strategy = st.builds(
    uml::TracedTrigger,
)
uml::TracedReplyAction_strategy = st.builds(
    uml::TracedReplyAction,
)
uml::TracedClause_strategy = st.builds(
    uml::TracedClause,
)
uml::TracedPackageMerge_strategy = st.builds(
    uml::TracedPackageMerge,
)
uml::TracedDecisionNode_strategy = st.builds(
    uml::TracedDecisionNode,
)
IntermediateActions::TracedReadStructuralFeatureActionActivation_strategy = st.builds(
    IntermediateActions::TracedReadStructuralFeatureActionActivation,
)
uml::TracedReadSelfAction_strategy = st.builds(
    uml::TracedReadSelfAction,
)
uml::TracedOperation_strategy = st.builds(
    uml::TracedOperation,
)
uml::TracedObjectFlow_strategy = st.builds(
    uml::TracedObjectFlow,
)
uml::TracedParameterSet_strategy = st.builds(
    uml::TracedParameterSet,
)
uml::TracedOccurrenceSpecification_strategy = st.builds(
    uml::TracedOccurrenceSpecification,
)
uml::TracedAcceptEventAction_strategy = st.builds(
    uml::TracedAcceptEventAction,
)
uml::TracedComponentRealization_strategy = st.builds(
    uml::TracedComponentRealization,
)
uml::TracedDataType_strategy = st.builds(
    uml::TracedDataType,
)
uml::TracedComment_strategy = st.builds(
    uml::TracedComment,
)
uml::TracedLoopNode_strategy = st.builds(
    uml::TracedLoopNode,
)
uml::TracedCallEvent_strategy = st.builds(
    uml::TracedCallEvent,
)
uml::TracedPackage_strategy = st.builds(
    uml::TracedPackage,
)
uml::TracedProtocolConformance_strategy = st.builds(
    uml::TracedProtocolConformance,
)
uml::TracedOpaqueBehavior_strategy = st.builds(
    uml::TracedOpaqueBehavior,
)
uml::TracedInterface_strategy = st.builds(
    uml::TracedInterface,
)
IntermediateActivities::TracedDecisionNodeActivation_strategy = st.builds(
    IntermediateActivities::TracedDecisionNodeActivation,
)
uml::TracedInteractionConstraint_strategy = st.builds(
    uml::TracedInteractionConstraint,
)
uml::TracedTimeInterval_strategy = st.builds(
    uml::TracedTimeInterval,
)
uml::TracedExecutionOccurrenceSpecification_strategy = st.builds(
    uml::TracedExecutionOccurrenceSpecification,
)
uml::TracedSignal_strategy = st.builds(
    uml::TracedSignal,
)
uml::TracedExtensionPoint_strategy = st.builds(
    uml::TracedExtensionPoint,
)
uml::TracedCreateLinkAction_strategy = st.builds(
    uml::TracedCreateLinkAction,
)
Kernel::TracedLiteralIntegerEvaluation_strategy = st.builds(
    Kernel::TracedLiteralIntegerEvaluation,
)
uml::TracedCentralBufferNode_strategy = st.builds(
    uml::TracedCentralBufferNode,
)
uml::TracedModel_strategy = st.builds(
    uml::TracedModel,
)
uml::TracedRedefinableTemplateSignature_strategy = st.builds(
    uml::TracedRedefinableTemplateSignature,
)
uml::TracedJoinNode_strategy = st.builds(
    uml::TracedJoinNode,
)
BasicActions::TracedOpaqueActionActivation_strategy = st.builds(
    BasicActions::TracedOpaqueActionActivation,
)
uml::TracedReadLinkObjectEndQualifierAction_strategy = st.builds(
    uml::TracedReadLinkObjectEndQualifierAction,
)
uml::TracedRealization_strategy = st.builds(
    uml::TracedRealization,
)
uml::TracedConnectionPointReference_strategy = st.builds(
    uml::TracedConnectionPointReference,
)
uml::TracedConditionalNode_strategy = st.builds(
    uml::TracedConditionalNode,
)
Kernel::TracedBooleanValue_strategy = st.builds(
    Kernel::TracedBooleanValue,
)
uml::TracedSignalEvent_strategy = st.builds(
    uml::TracedSignalEvent,
)
uml::TracedLiteralInteger_strategy = st.builds(
    uml::TracedLiteralInteger,
)
uml::TracedDestroyLinkAction_strategy = st.builds(
    uml::TracedDestroyLinkAction,
)
IntermediateActivities::TracedActivityFinalNodeActivation_strategy = st.builds(
    IntermediateActivities::TracedActivityFinalNodeActivation,
)
uml::TracedReadVariableAction_strategy = st.builds(
    uml::TracedReadVariableAction,
)
uml::TracedActionInputPin_strategy = st.builds(
    uml::TracedActionInputPin,
)
uml::TracedUsage_strategy = st.builds(
    uml::TracedUsage,
)
uml::TracedDeploymentSpecification_strategy = st.builds(
    uml::TracedDeploymentSpecification,
)
uml::TracedTemplateBinding_strategy = st.builds(
    uml::TracedTemplateBinding,
)
TracedAssociation_strategy = st.builds(
    TracedAssociation,
)
umlTrace::uml::TracedCommunicationPath_strategy = st.builds(
    umlTrace::uml::TracedCommunicationPath,
)
umlTrace::uml::TracedExtension_strategy = st.builds(
    umlTrace::uml::TracedExtension,
)
TracedStructuralFeatureAction_strategy = st.builds(
    TracedStructuralFeatureAction,
)
umlTrace::uml::TracedClearStructuralFeatureAction_strategy = st.builds(
    umlTrace::uml::TracedClearStructuralFeatureAction,
)
umlTrace::uml::TracedReadStructuralFeatureAction_strategy = st.builds(
    umlTrace::uml::TracedReadStructuralFeatureAction,
)
uml::TracedMessageOccurrenceSpecification_strategy = st.builds(
    uml::TracedMessageOccurrenceSpecification,
)
umlTrace::uml::TracedWriteStructuralFeatureAction_strategy = st.builds(
    umlTrace::uml::TracedWriteStructuralFeatureAction,
)
uml::TracedReception_strategy = st.builds(
    uml::TracedReception,
)
TracedWriteStructuralFeatureAction_strategy = st.builds(
    TracedWriteStructuralFeatureAction,
)
umlTrace::uml::TracedAddStructuralFeatureValueAction_strategy = st.builds(
    umlTrace::uml::TracedAddStructuralFeatureValueAction,
)
umlTrace::uml::TracedRemoveStructuralFeatureValueAction_strategy = st.builds(
    umlTrace::uml::TracedRemoveStructuralFeatureValueAction,
)
TracedBehavioredClassifier_strategy = st.builds(
    TracedBehavioredClassifier,
)
umlTrace::uml::TracedActor_strategy = st.builds(
    umlTrace::uml::TracedActor,
)
umlTrace::uml::TracedUseCase_strategy = st.builds(
    umlTrace::uml::TracedUseCase,
)
uml::TracedDeployedArtifact_strategy = st.builds(
    uml::TracedDeployedArtifact,
)
uml::TracedClassifier_strategy = st.builds(
    uml::TracedClassifier,
)
umlTrace::uml::TracedAssociation_strategy = st.builds(
    umlTrace::uml::TracedAssociation,
)
umlTrace::uml::TracedArtifact_strategy = st.builds(
    umlTrace::uml::TracedArtifact,
)
TracedArtifact_strategy = st.builds(
    TracedArtifact,
)
umlTrace::uml::TracedDeploymentSpecification_strategy = st.builds(
    umlTrace::uml::TracedDeploymentSpecification,
)
uml::TracedActivityNode_strategy = st.builds(
    uml::TracedActivityNode,
)
uml::TracedObjectNode_strategy = st.builds(
    uml::TracedObjectNode,
)
TracedPin_strategy = st.builds(
    TracedPin,
)
umlTrace::uml::TracedOutputPin_strategy = st.builds(
    umlTrace::uml::TracedOutputPin,
)
umlTrace::uml::TracedInputPin_strategy = st.builds(
    umlTrace::uml::TracedInputPin,
)
TracedInputPin_strategy = st.builds(
    TracedInputPin,
)
umlTrace::uml::TracedActionInputPin_strategy = st.builds(
    umlTrace::uml::TracedActionInputPin,
)
umlTrace::uml::TracedValuePin_strategy = st.builds(
    umlTrace::uml::TracedValuePin,
)
uml::TracedMultiplicityElement_strategy = st.builds(
    uml::TracedMultiplicityElement,
)
umlTrace::uml::TracedPin_strategy = st.builds(
    umlTrace::uml::TracedPin,
)
uml::TracedTypedElement_strategy = st.builds(
    uml::TracedTypedElement,
)
umlTrace::uml::TracedObjectNode_strategy = st.builds(
    umlTrace::uml::TracedObjectNode,
)
uml::TracedFeature_strategy = st.builds(
    uml::TracedFeature,
)
umlTrace::uml::TracedStructuralFeature_strategy = st.builds(
    umlTrace::uml::TracedStructuralFeature,
)
TracedValueSpecification_strategy = st.builds(
    TracedValueSpecification,
)
umlTrace::uml::TracedExpression_strategy = st.builds(
    umlTrace::uml::TracedExpression,
)
umlTrace::uml::TracedDuration_strategy = st.builds(
    umlTrace::uml::TracedDuration,
)
umlTrace::uml::TracedInstanceValue_strategy = st.builds(
    umlTrace::uml::TracedInstanceValue,
)
umlTrace::uml::TracedOpaqueExpression_strategy = st.builds(
    umlTrace::uml::TracedOpaqueExpression,
)
umlTrace::uml::TracedInterval_strategy = st.builds(
    umlTrace::uml::TracedInterval,
)
umlTrace::uml::TracedTimeExpression_strategy = st.builds(
    umlTrace::uml::TracedTimeExpression,
)
umlTrace::uml::TracedLiteralSpecification_strategy = st.builds(
    umlTrace::uml::TracedLiteralSpecification,
)
TracedLiteralSpecification_strategy = st.builds(
    TracedLiteralSpecification,
)
umlTrace::uml::TracedLiteralBoolean_strategy = st.builds(
    umlTrace::uml::TracedLiteralBoolean,
)
umlTrace::uml::TracedLiteralNull_strategy = st.builds(
    umlTrace::uml::TracedLiteralNull,
)
umlTrace::uml::TracedLiteralReal_strategy = st.builds(
    umlTrace::uml::TracedLiteralReal,
)
umlTrace::uml::TracedLiteralInteger_strategy = st.builds(
    umlTrace::uml::TracedLiteralInteger,
)
umlTrace::uml::TracedLiteralUnlimitedNatural_strategy = st.builds(
    umlTrace::uml::TracedLiteralUnlimitedNatural,
)
umlTrace::uml::TracedLiteralString_strategy = st.builds(
    umlTrace::uml::TracedLiteralString,
)
TracedVariableAction_strategy = st.builds(
    TracedVariableAction,
)
umlTrace::uml::TracedReadVariableAction_strategy = st.builds(
    umlTrace::uml::TracedReadVariableAction,
)
umlTrace::uml::TracedWriteVariableAction_strategy = st.builds(
    umlTrace::uml::TracedWriteVariableAction,
)
umlTrace::uml::TracedClearVariableAction_strategy = st.builds(
    umlTrace::uml::TracedClearVariableAction,
)
umlTrace::uml::TracedContinuation_strategy = st.builds(
    umlTrace::uml::TracedContinuation,
)
TracedCombinedFragment_strategy = st.builds(
    TracedCombinedFragment,
)
umlTrace::uml::TracedConsiderIgnoreFragment_strategy = st.builds(
    umlTrace::uml::TracedConsiderIgnoreFragment,
)
TracedNode_strategy = st.builds(
    TracedNode,
)
umlTrace::uml::TracedExecutionEnvironment_strategy = st.builds(
    umlTrace::uml::TracedExecutionEnvironment,
)
umlTrace::uml::TracedDevice_strategy = st.builds(
    umlTrace::uml::TracedDevice,
)
uml::TracedType_strategy = st.builds(
    uml::TracedType,
)
TracedClassifier_strategy = st.builds(
    TracedClassifier,
)
umlTrace::uml::TracedBehavioredClassifier_strategy = st.builds(
    umlTrace::uml::TracedBehavioredClassifier,
)
umlTrace::uml::TracedInformationItem_strategy = st.builds(
    umlTrace::uml::TracedInformationItem,
)
umlTrace::uml::TracedDataType_strategy = st.builds(
    umlTrace::uml::TracedDataType,
)
umlTrace::uml::TracedInterface_strategy = st.builds(
    umlTrace::uml::TracedInterface,
)
umlTrace::uml::TracedStructuredClassifier_strategy = st.builds(
    umlTrace::uml::TracedStructuredClassifier,
)
TracedStructuredClassifier_strategy = st.builds(
    TracedStructuredClassifier,
)
umlTrace::uml::TracedEncapsulatedClassifier_strategy = st.builds(
    umlTrace::uml::TracedEncapsulatedClassifier,
)
uml::TracedBehavioredClassifier_strategy = st.builds(
    uml::TracedBehavioredClassifier,
)
umlTrace::uml::TracedCollaboration_strategy = st.builds(
    umlTrace::uml::TracedCollaboration,
)
uml::TracedEncapsulatedClassifier_strategy = st.builds(
    uml::TracedEncapsulatedClassifier,
)
umlTrace::uml::TracedClass_strategy = st.builds(
    umlTrace::uml::TracedClass,
)
TracedCallAction_strategy = st.builds(
    TracedCallAction,
)
umlTrace::uml::TracedStartObjectBehaviorAction_strategy = st.builds(
    umlTrace::uml::TracedStartObjectBehaviorAction,
)
umlTrace::uml::TracedCallOperationAction_strategy = st.builds(
    umlTrace::uml::TracedCallOperationAction,
)
umlTrace::uml::TracedCallBehaviorAction_strategy = st.builds(
    umlTrace::uml::TracedCallBehaviorAction,
)
TracedRelationship_strategy = st.builds(
    TracedRelationship,
)
umlTrace::uml::TracedDirectedRelationship_strategy = st.builds(
    umlTrace::uml::TracedDirectedRelationship,
)
TracedDirectedRelationship_strategy = st.builds(
    TracedDirectedRelationship,
)
umlTrace::uml::TracedGeneralization_strategy = st.builds(
    umlTrace::uml::TracedGeneralization,
)
umlTrace::uml::TracedTemplateBinding_strategy = st.builds(
    umlTrace::uml::TracedTemplateBinding,
)
umlTrace::uml::TracedProfileApplication_strategy = st.builds(
    umlTrace::uml::TracedProfileApplication,
)
umlTrace::uml::TracedPackageImport_strategy = st.builds(
    umlTrace::uml::TracedPackageImport,
)
umlTrace::uml::TracedElementImport_strategy = st.builds(
    umlTrace::uml::TracedElementImport,
)
umlTrace::uml::TracedPackageMerge_strategy = st.builds(
    umlTrace::uml::TracedPackageMerge,
)
umlTrace::uml::TracedProtocolConformance_strategy = st.builds(
    umlTrace::uml::TracedProtocolConformance,
)
TracedInvocationAction_strategy = st.builds(
    TracedInvocationAction,
)
umlTrace::uml::TracedBroadcastSignalAction_strategy = st.builds(
    umlTrace::uml::TracedBroadcastSignalAction,
)
umlTrace::uml::TracedSendSignalAction_strategy = st.builds(
    umlTrace::uml::TracedSendSignalAction,
)
umlTrace::uml::TracedCallAction_strategy = st.builds(
    umlTrace::uml::TracedCallAction,
)
umlTrace::uml::TracedSendObjectAction_strategy = st.builds(
    umlTrace::uml::TracedSendObjectAction,
)
TracedRedefinableElement_strategy = st.builds(
    TracedRedefinableElement,
)
umlTrace::uml::TracedExtensionPoint_strategy = st.builds(
    umlTrace::uml::TracedExtensionPoint,
)
umlTrace::uml::TracedActivityEdge_strategy = st.builds(
    umlTrace::uml::TracedActivityEdge,
)
umlTrace::uml::TracedFeature_strategy = st.builds(
    umlTrace::uml::TracedFeature,
)
TracedFeature_strategy = st.builds(
    TracedFeature,
)
umlTrace::uml::TracedConnector_strategy = st.builds(
    umlTrace::uml::TracedConnector,
)
uml::TracedTemplateableElement_strategy = st.builds(
    uml::TracedTemplateableElement,
)
umlTrace::uml::TracedStringExpression_strategy = st.builds(
    umlTrace::uml::TracedStringExpression,
)
uml::TracedPackageableElement_strategy = st.builds(
    uml::TracedPackageableElement,
)
umlTrace::uml::TracedValueSpecification_strategy = st.builds(
    umlTrace::uml::TracedValueSpecification,
)
uml::TracedDeploymentTarget_strategy = st.builds(
    uml::TracedDeploymentTarget,
)
umlTrace::uml::TracedInstanceSpecification_strategy = st.builds(
    umlTrace::uml::TracedInstanceSpecification,
)
uml::TracedConnectableElement_strategy = st.builds(
    uml::TracedConnectableElement,
)
umlTrace::uml::TracedParameter_strategy = st.builds(
    umlTrace::uml::TracedParameter,
)
umlTrace::uml::TracedVariable_strategy = st.builds(
    umlTrace::uml::TracedVariable,
)
uml::TracedStructuralFeature_strategy = st.builds(
    uml::TracedStructuralFeature,
)
umlTrace::uml::TracedProperty_strategy = st.builds(
    umlTrace::uml::TracedProperty,
)
TracedProperty_strategy = st.builds(
    TracedProperty,
)
umlTrace::uml::TracedExtensionEnd_strategy = st.builds(
    umlTrace::uml::TracedExtensionEnd,
)
umlTrace::uml::TracedPort_strategy = st.builds(
    umlTrace::uml::TracedPort,
)
uml::TracedDirectedRelationship_strategy = st.builds(
    uml::TracedDirectedRelationship,
)
umlTrace::uml::TracedInformationFlow_strategy = st.builds(
    umlTrace::uml::TracedInformationFlow,
)
umlTrace::uml::TracedDependency_strategy = st.builds(
    umlTrace::uml::TracedDependency,
)
TracedEvent_strategy = st.builds(
    TracedEvent,
)
umlTrace::uml::TracedTimeEvent_strategy = st.builds(
    umlTrace::uml::TracedTimeEvent,
)
umlTrace::uml::TracedMessageEvent_strategy = st.builds(
    umlTrace::uml::TracedMessageEvent,
)
umlTrace::uml::TracedChangeEvent_strategy = st.builds(
    umlTrace::uml::TracedChangeEvent,
)
umlTrace::uml::TracedSignal_strategy = st.builds(
    umlTrace::uml::TracedSignal,
)
umlTrace::uml::TracedInteractionUse_strategy = st.builds(
    umlTrace::uml::TracedInteractionUse,
)
TracedFinalNode_strategy = st.builds(
    TracedFinalNode,
)
umlTrace::uml::TracedActivityFinalNode_strategy = st.builds(
    umlTrace::uml::TracedActivityFinalNode,
)
umlTrace::uml::TracedFlowFinalNode_strategy = st.builds(
    umlTrace::uml::TracedFlowFinalNode,
)
TracedControlNode_strategy = st.builds(
    TracedControlNode,
)
umlTrace::uml::TracedJoinNode_strategy = st.builds(
    umlTrace::uml::TracedJoinNode,
)
umlTrace::uml::TracedMergeNode_strategy = st.builds(
    umlTrace::uml::TracedMergeNode,
)
umlTrace::uml::TracedForkNode_strategy = st.builds(
    umlTrace::uml::TracedForkNode,
)
umlTrace::uml::TracedFinalNode_strategy = st.builds(
    umlTrace::uml::TracedFinalNode,
)
umlTrace::uml::TracedDecisionNode_strategy = st.builds(
    umlTrace::uml::TracedDecisionNode,
)
umlTrace::uml::TracedInitialNode_strategy = st.builds(
    umlTrace::uml::TracedInitialNode,
)
TracedAction_strategy = st.builds(
    TracedAction,
)
umlTrace::uml::TracedAcceptEventAction_strategy = st.builds(
    umlTrace::uml::TracedAcceptEventAction,
)
umlTrace::uml::TracedStartClassifierBehaviorAction_strategy = st.builds(
    umlTrace::uml::TracedStartClassifierBehaviorAction,
)
umlTrace::uml::TracedStructuralFeatureAction_strategy = st.builds(
    umlTrace::uml::TracedStructuralFeatureAction,
)
umlTrace::uml::TracedReduceAction_strategy = st.builds(
    umlTrace::uml::TracedReduceAction,
)
umlTrace::uml::TracedValueSpecificationAction_strategy = st.builds(
    umlTrace::uml::TracedValueSpecificationAction,
)
umlTrace::uml::TracedOpaqueAction_strategy = st.builds(
    umlTrace::uml::TracedOpaqueAction,
)
umlTrace::uml::TracedUnmarshallAction_strategy = st.builds(
    umlTrace::uml::TracedUnmarshallAction,
)
umlTrace::uml::TracedReadSelfAction_strategy = st.builds(
    umlTrace::uml::TracedReadSelfAction,
)
umlTrace::uml::TracedReadIsClassifiedObjectAction_strategy = st.builds(
    umlTrace::uml::TracedReadIsClassifiedObjectAction,
)
umlTrace::uml::TracedDestroyObjectAction_strategy = st.builds(
    umlTrace::uml::TracedDestroyObjectAction,
)
umlTrace::uml::TracedVariableAction_strategy = st.builds(
    umlTrace::uml::TracedVariableAction,
)
umlTrace::uml::TracedReadLinkObjectEndQualifierAction_strategy = st.builds(
    umlTrace::uml::TracedReadLinkObjectEndQualifierAction,
)
umlTrace::uml::TracedInvocationAction_strategy = st.builds(
    umlTrace::uml::TracedInvocationAction,
)
umlTrace::uml::TracedRaiseExceptionAction_strategy = st.builds(
    umlTrace::uml::TracedRaiseExceptionAction,
)
umlTrace::uml::TracedReadLinkObjectEndAction_strategy = st.builds(
    umlTrace::uml::TracedReadLinkObjectEndAction,
)
umlTrace::uml::TracedClearAssociationAction_strategy = st.builds(
    umlTrace::uml::TracedClearAssociationAction,
)
umlTrace::uml::TracedReadExtentAction_strategy = st.builds(
    umlTrace::uml::TracedReadExtentAction,
)
umlTrace::uml::TracedReplyAction_strategy = st.builds(
    umlTrace::uml::TracedReplyAction,
)
umlTrace::uml::TracedTestIdentityAction_strategy = st.builds(
    umlTrace::uml::TracedTestIdentityAction,
)
umlTrace::uml::TracedCreateObjectAction_strategy = st.builds(
    umlTrace::uml::TracedCreateObjectAction,
)
umlTrace::uml::TracedReclassifyObjectAction_strategy = st.builds(
    umlTrace::uml::TracedReclassifyObjectAction,
)
umlTrace::uml::TracedLinkAction_strategy = st.builds(
    umlTrace::uml::TracedLinkAction,
)
TracedLinkAction_strategy = st.builds(
    TracedLinkAction,
)
umlTrace::uml::TracedReadLinkAction_strategy = st.builds(
    umlTrace::uml::TracedReadLinkAction,
)
umlTrace::uml::TracedWriteLinkAction_strategy = st.builds(
    umlTrace::uml::TracedWriteLinkAction,
)
TracedWriteLinkAction_strategy = st.builds(
    TracedWriteLinkAction,
)
umlTrace::uml::TracedDestroyLinkAction_strategy = st.builds(
    umlTrace::uml::TracedDestroyLinkAction,
)
umlTrace::uml::TracedCreateLinkAction_strategy = st.builds(
    umlTrace::uml::TracedCreateLinkAction,
)
TracedCreateLinkAction_strategy = st.builds(
    TracedCreateLinkAction,
)
umlTrace::uml::TracedCreateLinkObjectAction_strategy = st.builds(
    umlTrace::uml::TracedCreateLinkObjectAction,
)
uml::TracedNamedElement_strategy = st.builds(
    uml::TracedNamedElement,
)
umlTrace::uml::TracedInclude_strategy = st.builds(
    umlTrace::uml::TracedInclude,
)
umlTrace::uml::TracedExtend_strategy = st.builds(
    umlTrace::uml::TracedExtend,
)
ActivityContent_strategy = st.builds(
    ActivityContent,
)
umlTrace::uml::TracedActivityGroup_strategy = st.builds(
    umlTrace::uml::TracedActivityGroup,
)
uml::TracedRedefinableElement_strategy = st.builds(
    uml::TracedRedefinableElement,
)
umlTrace::uml::TracedRedefinableTemplateSignature_strategy = st.builds(
    umlTrace::uml::TracedRedefinableTemplateSignature,
)
umlTrace::uml::TracedActivityNode_strategy = st.builds(
    umlTrace::uml::TracedActivityNode,
)
TracedActivityNode_strategy = st.builds(
    TracedActivityNode,
)
umlTrace::uml::TracedControlNode_strategy = st.builds(
    umlTrace::uml::TracedControlNode,
)
umlTrace::uml::TracedExecutableNode_strategy = st.builds(
    umlTrace::uml::TracedExecutableNode,
)
TracedExecutableNode_strategy = st.builds(
    TracedExecutableNode,
)
umlTrace::uml::TracedAction_strategy = st.builds(
    umlTrace::uml::TracedAction,
)
uml::TracedActivityGroup_strategy = st.builds(
    uml::TracedActivityGroup,
)
uml::TracedNamespace_strategy = st.builds(
    uml::TracedNamespace,
)
umlTrace::uml::TracedTransition_strategy = st.builds(
    umlTrace::uml::TracedTransition,
)
umlTrace::uml::TracedInteractionOperand_strategy = st.builds(
    umlTrace::uml::TracedInteractionOperand,
)
umlTrace::uml::TracedRegion_strategy = st.builds(
    umlTrace::uml::TracedRegion,
)
umlTrace::uml::TracedPackage_strategy = st.builds(
    umlTrace::uml::TracedPackage,
)
umlTrace::uml::TracedState_strategy = st.builds(
    umlTrace::uml::TracedState,
)
umlTrace::uml::TracedBehavioralFeature_strategy = st.builds(
    umlTrace::uml::TracedBehavioralFeature,
)
umlTrace::uml::TracedClassifier_strategy = st.builds(
    umlTrace::uml::TracedClassifier,
)
uml::TracedAction_strategy = st.builds(
    uml::TracedAction,
)
umlTrace::uml::TracedStructuredActivityNode_strategy = st.builds(
    umlTrace::uml::TracedStructuredActivityNode,
)
TracedStructuredActivityNode_strategy = st.builds(
    TracedStructuredActivityNode,
)
umlTrace::uml::TracedExpansionRegion_strategy = st.builds(
    umlTrace::uml::TracedExpansionRegion,
)
umlTrace::uml::TracedLoopNode_strategy = st.builds(
    umlTrace::uml::TracedLoopNode,
)
umlTrace::uml::TracedSequenceNode_strategy = st.builds(
    umlTrace::uml::TracedSequenceNode,
)
umlTrace::uml::TracedConditionalNode_strategy = st.builds(
    umlTrace::uml::TracedConditionalNode,
)
TracedEModelElement_strategy = st.builds(
    TracedEModelElement,
)
umlTrace::uml::TracedElement_strategy = st.builds(
    umlTrace::uml::TracedElement,
)
TracedElement_strategy = st.builds(
    TracedElement,
)
umlTrace::uml::TracedTemplateParameter_strategy = st.builds(
    umlTrace::uml::TracedTemplateParameter,
)
umlTrace::uml::TracedRelationship_strategy = st.builds(
    umlTrace::uml::TracedRelationship,
)
umlTrace::uml::TracedLinkEndData_strategy = st.builds(
    umlTrace::uml::TracedLinkEndData,
)
umlTrace::uml::TracedExceptionHandler_strategy = st.builds(
    umlTrace::uml::TracedExceptionHandler,
)
umlTrace::uml::TracedSlot_strategy = st.builds(
    umlTrace::uml::TracedSlot,
)
umlTrace::uml::TracedTemplateParameterSubstitution_strategy = st.builds(
    umlTrace::uml::TracedTemplateParameterSubstitution,
)
umlTrace::uml::TracedTemplateSignature_strategy = st.builds(
    umlTrace::uml::TracedTemplateSignature,
)
umlTrace::uml::TracedComment_strategy = st.builds(
    umlTrace::uml::TracedComment,
)
umlTrace::uml::TracedMultiplicityElement_strategy = st.builds(
    umlTrace::uml::TracedMultiplicityElement,
)
umlTrace::uml::TracedTemplateableElement_strategy = st.builds(
    umlTrace::uml::TracedTemplateableElement,
)
umlTrace::uml::TracedClause_strategy = st.builds(
    umlTrace::uml::TracedClause,
)
umlTrace::uml::TracedImage_strategy = st.builds(
    umlTrace::uml::TracedImage,
)
umlTrace::uml::TracedQualifierValue_strategy = st.builds(
    umlTrace::uml::TracedQualifierValue,
)
umlTrace::uml::TracedNamedElement_strategy = st.builds(
    umlTrace::uml::TracedNamedElement,
)
TracedNamedElement_strategy = st.builds(
    TracedNamedElement,
)
umlTrace::uml::TracedTypedElement_strategy = st.builds(
    umlTrace::uml::TracedTypedElement,
)
umlTrace::uml::TracedNamespace_strategy = st.builds(
    umlTrace::uml::TracedNamespace,
)
umlTrace::uml::TracedRedefinableElement_strategy = st.builds(
    umlTrace::uml::TracedRedefinableElement,
)
umlTrace::uml::TracedDeploymentTarget_strategy = st.builds(
    umlTrace::uml::TracedDeploymentTarget,
)
umlTrace::uml::TracedMessage_strategy = st.builds(
    umlTrace::uml::TracedMessage,
)
umlTrace::uml::TracedCollaborationUse_strategy = st.builds(
    umlTrace::uml::TracedCollaborationUse,
)
umlTrace::uml::TracedMessageEnd_strategy = st.builds(
    umlTrace::uml::TracedMessageEnd,
)
umlTrace::uml::TracedGeneralOrdering_strategy = st.builds(
    umlTrace::uml::TracedGeneralOrdering,
)
umlTrace::uml::TracedParameterSet_strategy = st.builds(
    umlTrace::uml::TracedParameterSet,
)
umlTrace::uml::TracedTrigger_strategy = st.builds(
    umlTrace::uml::TracedTrigger,
)
umlTrace::uml::TracedLifeline_strategy = st.builds(
    umlTrace::uml::TracedLifeline,
)
umlTrace::uml::TracedDeployedArtifact_strategy = st.builds(
    umlTrace::uml::TracedDeployedArtifact,
)
umlTrace::uml::TracedInteractionFragment_strategy = st.builds(
    umlTrace::uml::TracedInteractionFragment,
)
umlTrace::uml::TracedOccurrenceSpecification_strategy = st.builds(
    umlTrace::uml::TracedOccurrenceSpecification,
)
uml::TracedMessageEnd_strategy = st.builds(
    uml::TracedMessageEnd,
)
umlTrace::uml::TracedMessageOccurrenceSpecification_strategy = st.builds(
    umlTrace::uml::TracedMessageOccurrenceSpecification,
)
TracedMessageOccurrenceSpecification_strategy = st.builds(
    TracedMessageOccurrenceSpecification,
)
umlTrace::uml::TracedDestructionOccurrenceSpecification_strategy = st.builds(
    umlTrace::uml::TracedDestructionOccurrenceSpecification,
)
umlTrace::uml::TracedVertex_strategy = st.builds(
    umlTrace::uml::TracedVertex,
)
TracedVertex_strategy = st.builds(
    TracedVertex,
)
umlTrace::uml::TracedConnectionPointReference_strategy = st.builds(
    umlTrace::uml::TracedConnectionPointReference,
)
umlTrace::uml::TracedPseudostate_strategy = st.builds(
    umlTrace::uml::TracedPseudostate,
)
umlTrace::uml::TracedParameterableElement_strategy = st.builds(
    umlTrace::uml::TracedParameterableElement,
)
uml::TracedParameterableElement_strategy = st.builds(
    uml::TracedParameterableElement,
)
umlTrace::uml::TracedConnectableElement_strategy = st.builds(
    umlTrace::uml::TracedConnectableElement,
)
umlTrace::uml::TracedOperation_strategy = st.builds(
    umlTrace::uml::TracedOperation,
)
umlTrace::uml::TracedPackageableElement_strategy = st.builds(
    umlTrace::uml::TracedPackageableElement,
)
TracedPackageableElement_strategy = st.builds(
    TracedPackageableElement,
)
umlTrace::uml::TracedObservation_strategy = st.builds(
    umlTrace::uml::TracedObservation,
)
umlTrace::uml::TracedEvent_strategy = st.builds(
    umlTrace::uml::TracedEvent,
)
umlTrace::uml::TracedGeneralizationSet_strategy = st.builds(
    umlTrace::uml::TracedGeneralizationSet,
)
umlTrace::uml::TracedType_strategy = st.builds(
    umlTrace::uml::TracedType,
)
umlTrace::uml::TracedConstraint_strategy = st.builds(
    umlTrace::uml::TracedConstraint,
)
TracedConstraint_strategy = st.builds(
    TracedConstraint,
)
umlTrace::uml::TracedInteractionConstraint_strategy = st.builds(
    umlTrace::uml::TracedInteractionConstraint,
)
umlTrace::uml::TracedIntervalConstraint_strategy = st.builds(
    umlTrace::uml::TracedIntervalConstraint,
)
TracedIntervalConstraint_strategy = st.builds(
    TracedIntervalConstraint,
)
umlTrace::uml::TracedTimeConstraint_strategy = st.builds(
    umlTrace::uml::TracedTimeConstraint,
)
umlTrace::uml::TracedDurationConstraint_strategy = st.builds(
    umlTrace::uml::TracedDurationConstraint,
)
uml::TracedControlFlow_strategy = st.builds(
    uml::TracedControlFlow,
)
uml::TracedTimeObservation_strategy = st.builds(
    uml::TracedTimeObservation,
)
uml::TracedGate_strategy = st.builds(
    uml::TracedGate,
)
uml::TracedProtocolStateMachine_strategy = st.builds(
    uml::TracedProtocolStateMachine,
)
uml::TracedDataStoreNode_strategy = st.builds(
    uml::TracedDataStoreNode,
)
uml::TracedReadStructuralFeatureAction_strategy = st.builds(
    uml::TracedReadStructuralFeatureAction,
)
uml::TracedAnyReceiveEvent_strategy = st.builds(
    uml::TracedAnyReceiveEvent,
)
Kernel::TracedIntegerValue_strategy = st.builds(
    Kernel::TracedIntegerValue,
)
uml::TracedInterval_strategy = st.builds(
    uml::TracedInterval,
)
uml::TracedRemoveStructuralFeatureValueAction_strategy = st.builds(
    uml::TracedRemoveStructuralFeatureValueAction,
)
uml::TracedGeneralization_strategy = st.builds(
    uml::TracedGeneralization,
)
uml::TracedInteractionOperand_strategy = st.builds(
    uml::TracedInteractionOperand,
)
uml::TracedProtocolTransition_strategy = st.builds(
    uml::TracedProtocolTransition,
)
uml::TracedInterruptibleActivityRegion_strategy = st.builds(
    uml::TracedInterruptibleActivityRegion,
)
uml::TracedPartDecomposition_strategy = st.builds(
    uml::TracedPartDecomposition,
)
uml::TracedTimeEvent_strategy = st.builds(
    uml::TracedTimeEvent,
)
uml::TracedDeployment_strategy = st.builds(
    uml::TracedDeployment,
)
Loci::TracedSemanticVisitor_strategy = st.builds(
    Loci::TracedSemanticVisitor,
)
Kernel::TracedObject_strategy = st.builds(
    Kernel::TracedObject,
)
IntermediateActivities::TracedJoinNodeActivation_strategy = st.builds(
    IntermediateActivities::TracedJoinNodeActivation,
)
uml::TracedUseCase_strategy = st.builds(
    uml::TracedUseCase,
)
uml::TracedReclassifyObjectAction_strategy = st.builds(
    uml::TracedReclassifyObjectAction,
)
uml::TracedInstanceValue_strategy = st.builds(
    uml::TracedInstanceValue,
)
IntermediateActions::TracedAddStructuralFeatureValueActionActivation_strategy = st.builds(
    IntermediateActions::TracedAddStructuralFeatureValueActionActivation,
)
Kernel::TracedReference_strategy = st.builds(
    Kernel::TracedReference,
)
uml::TracedForkNode_strategy = st.builds(
    uml::TracedForkNode,
)
uml::TracedActivity_strategy = st.builds(
    uml::TracedActivity,
)
uml::TracedMessage_strategy = st.builds(
    uml::TracedMessage,
)
uml::TracedStateMachine_strategy = st.builds(
    uml::TracedStateMachine,
)
uml::TracedActivityPartition_strategy = st.builds(
    uml::TracedActivityPartition,
)
IntermediateActivities::TracedActivityParameterNodeActivation_strategy = st.builds(
    IntermediateActivities::TracedActivityParameterNodeActivation,
)
BasicActions::TracedCallBehaviorActionActivation_strategy = st.builds(
    BasicActions::TracedCallBehaviorActionActivation,
)
uml::TracedDestroyObjectAction_strategy = st.builds(
    uml::TracedDestroyObjectAction,
)
uml::TracedAssociationClass_strategy = st.builds(
    uml::TracedAssociationClass,
)
uml::TracedInformationFlow_strategy = st.builds(
    uml::TracedInformationFlow,
)
uml::TracedSubstitution_strategy = st.builds(
    uml::TracedSubstitution,
)
uml::TracedEnumerationLiteral_strategy = st.builds(
    uml::TracedEnumerationLiteral,
)
uml::TracedStereotype_strategy = st.builds(
    uml::TracedStereotype,
)
uml::TracedAcceptCallAction_strategy = st.builds(
    uml::TracedAcceptCallAction,
)
uml::TracedInstanceSpecification_strategy = st.builds(
    uml::TracedInstanceSpecification,
)
IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution_strategy = st.builds(
    IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution,
)
uml::TracedStateInvariant_strategy = st.builds(
    uml::TracedStateInvariant,
)
BasicActions::TracedInputPinActivation_strategy = st.builds(
    BasicActions::TracedInputPinActivation,
)
uml::TracedLiteralString_strategy = st.builds(
    uml::TracedLiteralString,
)
uml::TracedOpaqueExpression_strategy = st.builds(
    uml::TracedOpaqueExpression,
)
uml::TracedParameter_strategy = st.builds(
    uml::TracedParameter,
)
IntermediateActivities::TracedActivityNodeActivation_strategy = st.builds(
    IntermediateActivities::TracedActivityNodeActivation,
)
uml::TracedInteraction_strategy = st.builds(
    uml::TracedInteraction,
)
uml::TracedBroadcastSignalAction_strategy = st.builds(
    uml::TracedBroadcastSignalAction,
)
uml::TracedConstraint_strategy = st.builds(
    uml::TracedConstraint,
)
uml::TracedClearVariableAction_strategy = st.builds(
    uml::TracedClearVariableAction,
)
uml::TracedInputPin_strategy = st.builds(
    uml::TracedInputPin,
)
uml::TracedTimeConstraint_strategy = st.builds(
    uml::TracedTimeConstraint,
)
uml::TracedContinuation_strategy = st.builds(
    uml::TracedContinuation,
)
uml::TracedConsiderIgnoreFragment_strategy = st.builds(
    uml::TracedConsiderIgnoreFragment,
)
uml::TracedIntervalConstraint_strategy = st.builds(
    uml::TracedIntervalConstraint,
)
uml::TracedExecutionEnvironment_strategy = st.builds(
    uml::TracedExecutionEnvironment,
)
uml::TracedStructuredActivityNode_strategy = st.builds(
    uml::TracedStructuredActivityNode,
)
uml::TracedExtension_strategy = st.builds(
    uml::TracedExtension,
)
IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution_strategy = st.builds(
    IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution,
)
uml::TracedExtend_strategy = st.builds(
    uml::TracedExtend,
)
uml::TracedStartClassifierBehaviorAction_strategy = st.builds(
    uml::TracedStartClassifierBehaviorAction,
)
uml::TracedSequenceNode_strategy = st.builds(
    uml::TracedSequenceNode,
)
uml::TracedExceptionHandler_strategy = st.builds(
    uml::TracedExceptionHandler,
)
uml::TracedNode_strategy = st.builds(
    uml::TracedNode,
)
uml::TracedValuePin_strategy = st.builds(
    uml::TracedValuePin,
)
IntermediateActivities::TracedActivityExecution_strategy = st.builds(
    IntermediateActivities::TracedActivityExecution,
)
uml::TracedCollaborationUse_strategy = st.builds(
    uml::TracedCollaborationUse,
)
IntermediateActivities::TracedInitialNodeActivation_strategy = st.builds(
    IntermediateActivities::TracedInitialNodeActivation,
)
uml::TracedPort_strategy = st.builds(
    uml::TracedPort,
)
uml::TracedDependency_strategy = st.builds(
    uml::TracedDependency,
)
uml::TracedChangeEvent_strategy = st.builds(
    uml::TracedChangeEvent,
)
uml::TracedGeneralizationSet_strategy = st.builds(
    uml::TracedGeneralizationSet,
)
uml::TracedInteractionUse_strategy = st.builds(
    uml::TracedInteractionUse,
)
uml::TracedClass_strategy = st.builds(
    uml::TracedClass,
)
umlTrace::uml::TracedNode_strategy = st.builds(
    umlTrace::uml::TracedNode,
)
umlTrace::uml::TracedAssociationClass_strategy = st.builds(
    umlTrace::uml::TracedAssociationClass,
)
uml::TracedPackageImport_strategy = st.builds(
    uml::TracedPackageImport,
)
uml::TracedSendObjectAction_strategy = st.builds(
    uml::TracedSendObjectAction,
)
uml::TracedConnector_strategy = st.builds(
    uml::TracedConnector,
)
uml::TracedDestructionOccurrenceSpecification_strategy = st.builds(
    uml::TracedDestructionOccurrenceSpecification,
)
uml::TracedDurationConstraint_strategy = st.builds(
    uml::TracedDurationConstraint,
)
IntermediateActivities::TracedForkNodeActivation_strategy = st.builds(
    IntermediateActivities::TracedForkNodeActivation,
)
uml::TracedLifeline_strategy = st.builds(
    uml::TracedLifeline,
)
uml::TracedCreateObjectAction_strategy = st.builds(
    uml::TracedCreateObjectAction,
)
uml::TracedExpansionRegion_strategy = st.builds(
    uml::TracedExpansionRegion,
)
uml::TracedFlowFinalNode_strategy = st.builds(
    uml::TracedFlowFinalNode,
)
uml::TracedInitialNode_strategy = st.builds(
    uml::TracedInitialNode,
)
uml::TracedCreateLinkObjectAction_strategy = st.builds(
    uml::TracedCreateLinkObjectAction,
)
uml::TracedCombinedFragment_strategy = st.builds(
    uml::TracedCombinedFragment,
)
umlTrace::Traced::TracedObjects_strategy = st.builds(
    umlTrace::Traced::TracedObjects,
)
Traced::TracedObjects_strategy = st.builds(
    Traced::TracedObjects,
)
State_strategy = st.builds(
    State,
)
umlTrace::Trace_strategy = st.builds(
    umlTrace::Trace,
)
Values::SemanticVisitor::runtimeModelElement::Value_strategy = st.builds(
    Values::SemanticVisitor::runtimeModelElement::Value,
)
Values::ActionActivation::firing::Value_strategy = st.builds(
    Values::ActionActivation::firing::Value,
)
umlTrace::State_strategy = st.builds(
    umlTrace::State,
)

@given(instance=uml::ActivityContent_strategy)
@settings(max_examples=50)
def test_uml::activitycontent_instantiation(instance):
    assert isinstance(instance, uml::ActivityContent)

@given(instance=BasicActions::TracedActionActivation_strategy)
@settings(max_examples=50)
def test_basicactions::tracedactionactivation_instantiation(instance):
    assert isinstance(instance, BasicActions::TracedActionActivation)

@given(instance=umlTrace::Values::ActionActivation::firing::Value_strategy)
@settings(max_examples=50)
def test_umltrace::values::actionactivation::firing::value_instantiation(instance):
    assert isinstance(instance, umlTrace::Values::ActionActivation::firing::Value)

@given(instance=umlTrace::Values::ActionActivation::firing::Value_strategy)
def test_umltrace::values::actionactivation::firing::value_firing_type(instance):
    assert isinstance(instance.firing, str)


@given(instance=umlTrace::Values::ActionActivation::firing::Value_strategy)
def test_umltrace::values::actionactivation::firing::value_firing_setter(instance):
    original = instance.firing
    instance.firing = original
    assert instance.firing == original

@given(instance=TracedLiteralEvaluation_strategy)
@settings(max_examples=50)
def test_tracedliteralevaluation_instantiation(instance):
    assert isinstance(instance, TracedLiteralEvaluation)

@given(instance=umlTrace::Kernel::TracedLiteralIntegerEvaluation_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedliteralintegerevaluation_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedLiteralIntegerEvaluation)

@given(instance=umlTrace::Kernel::TracedLiteralBooleanEvaluation_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedliteralbooleanevaluation_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedLiteralBooleanEvaluation)

@given(instance=TracedPrimitiveValue_strategy)
@settings(max_examples=50)
def test_tracedprimitivevalue_instantiation(instance):
    assert isinstance(instance, TracedPrimitiveValue)

@given(instance=umlTrace::Kernel::TracedBooleanValue_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedbooleanvalue_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedBooleanValue)

@given(instance=umlTrace::Kernel::TracedIntegerValue_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedintegervalue_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedIntegerValue)

@given(instance=TracedEvaluation_strategy)
@settings(max_examples=50)
def test_tracedevaluation_instantiation(instance):
    assert isinstance(instance, TracedEvaluation)

@given(instance=umlTrace::Kernel::TracedLiteralEvaluation_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedliteralevaluation_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedLiteralEvaluation)

@given(instance=TracedValue_strategy)
@settings(max_examples=50)
def test_tracedvalue_instantiation(instance):
    assert isinstance(instance, TracedValue)

@given(instance=umlTrace::Kernel::TracedPrimitiveValue_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedprimitivevalue_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedPrimitiveValue)

@given(instance=umlTrace::Kernel::TracedStructuredValue_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedstructuredvalue_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedStructuredValue)

@given(instance=TracedStructuredValue_strategy)
@settings(max_examples=50)
def test_tracedstructuredvalue_instantiation(instance):
    assert isinstance(instance, TracedStructuredValue)

@given(instance=umlTrace::Kernel::TracedReference_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedreference_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedReference)

@given(instance=umlTrace::Kernel::TracedCompoundValue_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedcompoundvalue_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedCompoundValue)

@given(instance=TracedCompoundValue_strategy)
@settings(max_examples=50)
def test_tracedcompoundvalue_instantiation(instance):
    assert isinstance(instance, TracedCompoundValue)

@given(instance=umlTrace::Kernel::TracedExtensionalValue_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedextensionalvalue_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedExtensionalValue)

@given(instance=TracedExtensionalValue_strategy)
@settings(max_examples=50)
def test_tracedextensionalvalue_instantiation(instance):
    assert isinstance(instance, TracedExtensionalValue)

@given(instance=umlTrace::Kernel::TracedObject_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedobject_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedObject)

@given(instance=TracedObject_strategy)
@settings(max_examples=50)
def test_tracedobject_instantiation(instance):
    assert isinstance(instance, TracedObject)

@given(instance=umlTrace::BasicBehaviors::TracedExecution_strategy)
@settings(max_examples=50)
def test_umltrace::basicbehaviors::tracedexecution_instantiation(instance):
    assert isinstance(instance, umlTrace::BasicBehaviors::TracedExecution)

@given(instance=uml::TracedElement_strategy)
@settings(max_examples=50)
def test_uml::tracedelement_instantiation(instance):
    assert isinstance(instance, uml::TracedElement)

@given(instance=umlTrace::Values::SemanticVisitor::runtimeModelElement::Value_strategy)
@settings(max_examples=50)
def test_umltrace::values::semanticvisitor::runtimemodelelement::value_instantiation(instance):
    assert isinstance(instance, umlTrace::Values::SemanticVisitor::runtimeModelElement::Value)

@given(instance=TracedOpaqueBehaviorExecution_strategy)
@settings(max_examples=50)
def test_tracedopaquebehaviorexecution_instantiation(instance):
    assert isinstance(instance, TracedOpaqueBehaviorExecution)

@given(instance=umlTrace::IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_umltrace::integerfunctions::tracedintegergreaterfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, umlTrace::IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution)

@given(instance=umlTrace::IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_umltrace::integerfunctions::tracedintegerlessfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, umlTrace::IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution)

@given(instance=umlTrace::IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_umltrace::integerfunctions::tracedintegerplusfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, umlTrace::IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution)

@given(instance=TracedCallActionActivation_strategy)
@settings(max_examples=50)
def test_tracedcallactionactivation_instantiation(instance):
    assert isinstance(instance, TracedCallActionActivation)

@given(instance=umlTrace::BasicActions::TracedCallBehaviorActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace::basicactions::tracedcallbehavioractionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::BasicActions::TracedCallBehaviorActionActivation)

@given(instance=TracedPinActivation_strategy)
@settings(max_examples=50)
def test_tracedpinactivation_instantiation(instance):
    assert isinstance(instance, TracedPinActivation)

@given(instance=umlTrace::BasicActions::TracedOutputPinActivation_strategy)
@settings(max_examples=50)
def test_umltrace::basicactions::tracedoutputpinactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::BasicActions::TracedOutputPinActivation)

@given(instance=umlTrace::BasicActions::TracedInputPinActivation_strategy)
@settings(max_examples=50)
def test_umltrace::basicactions::tracedinputpinactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::BasicActions::TracedInputPinActivation)

@given(instance=TracedInvocationActionActivation_strategy)
@settings(max_examples=50)
def test_tracedinvocationactionactivation_instantiation(instance):
    assert isinstance(instance, TracedInvocationActionActivation)

@given(instance=umlTrace::BasicActions::TracedCallActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace::basicactions::tracedcallactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::BasicActions::TracedCallActionActivation)

@given(instance=TracedActionActivation_strategy)
@settings(max_examples=50)
def test_tracedactionactivation_instantiation(instance):
    assert isinstance(instance, TracedActionActivation)

@given(instance=umlTrace::BasicActions::TracedOpaqueActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace::basicactions::tracedopaqueactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::BasicActions::TracedOpaqueActionActivation)

@given(instance=umlTrace::BasicActions::TracedInvocationActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace::basicactions::tracedinvocationactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::BasicActions::TracedInvocationActionActivation)

@given(instance=umlTrace::Loci::TracedSemanticVisitor_strategy)
@settings(max_examples=50)
def test_umltrace::loci::tracedsemanticvisitor_instantiation(instance):
    assert isinstance(instance, umlTrace::Loci::TracedSemanticVisitor)

@given(instance=TracedObjectNodeActivation_strategy)
@settings(max_examples=50)
def test_tracedobjectnodeactivation_instantiation(instance):
    assert isinstance(instance, TracedObjectNodeActivation)

@given(instance=umlTrace::BasicActions::TracedPinActivation_strategy)
@settings(max_examples=50)
def test_umltrace::basicactions::tracedpinactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::BasicActions::TracedPinActivation)

@given(instance=umlTrace::IntermediateActivities::TracedActivityParameterNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactivities::tracedactivityparameternodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActivities::TracedActivityParameterNodeActivation)

@given(instance=umlTrace::IntermediateActions::TracedCreateObjectActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactions::tracedcreateobjectactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActions::TracedCreateObjectActionActivation)

@given(instance=umlTrace::IntermediateActions::TracedValueSpecificationActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactions::tracedvaluespecificationactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActions::TracedValueSpecificationActionActivation)

@given(instance=TracedWriteStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_tracedwritestructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, TracedWriteStructuralFeatureActionActivation)

@given(instance=umlTrace::IntermediateActions::TracedAddStructuralFeatureValueActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactions::tracedaddstructuralfeaturevalueactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActions::TracedAddStructuralFeatureValueActionActivation)

@given(instance=TracedStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_tracedstructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, TracedStructuralFeatureActionActivation)

@given(instance=umlTrace::IntermediateActions::TracedWriteStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactions::tracedwritestructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActions::TracedWriteStructuralFeatureActionActivation)

@given(instance=umlTrace::IntermediateActions::TracedReadStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactions::tracedreadstructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActions::TracedReadStructuralFeatureActionActivation)

@given(instance=umlTrace::IntermediateActions::TracedStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactions::tracedstructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActions::TracedStructuralFeatureActionActivation)

@given(instance=umlTrace::ecore::TracedEModelElement_strategy)
@settings(max_examples=50)
def test_umltrace::ecore::tracedemodelelement_instantiation(instance):
    assert isinstance(instance, umlTrace::ecore::TracedEModelElement)

@given(instance=TracedMessageEnd_strategy)
@settings(max_examples=50)
def test_tracedmessageend_instantiation(instance):
    assert isinstance(instance, TracedMessageEnd)

@given(instance=umlTrace::uml::TracedGate_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedgate_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedGate)

@given(instance=TracedExecution_strategy)
@settings(max_examples=50)
def test_tracedexecution_instantiation(instance):
    assert isinstance(instance, TracedExecution)

@given(instance=umlTrace::BasicBehaviors::TracedOpaqueBehaviorExecution_strategy)
@settings(max_examples=50)
def test_umltrace::basicbehaviors::tracedopaquebehaviorexecution_instantiation(instance):
    assert isinstance(instance, umlTrace::BasicBehaviors::TracedOpaqueBehaviorExecution)

@given(instance=TracedExecutionSpecification_strategy)
@settings(max_examples=50)
def test_tracedexecutionspecification_instantiation(instance):
    assert isinstance(instance, TracedExecutionSpecification)

@given(instance=umlTrace::uml::TracedBehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedbehaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedBehaviorExecutionSpecification)

@given(instance=TracedOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_tracedoccurrencespecification_instantiation(instance):
    assert isinstance(instance, TracedOccurrenceSpecification)

@given(instance=umlTrace::uml::TracedExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedexecutionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedExecutionOccurrenceSpecification)

@given(instance=TracedOpaqueBehavior_strategy)
@settings(max_examples=50)
def test_tracedopaquebehavior_instantiation(instance):
    assert isinstance(instance, TracedOpaqueBehavior)

@given(instance=umlTrace::uml::TracedFunctionBehavior_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedfunctionbehavior_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedFunctionBehavior)

@given(instance=uml::TracedStructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml::tracedstructuredclassifier_instantiation(instance):
    assert isinstance(instance, uml::TracedStructuredClassifier)

@given(instance=TracedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_tracedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, TracedMultiplicityElement)

@given(instance=umlTrace::uml::TracedConnectorEnd_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedconnectorend_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedConnectorEnd)

@given(instance=umlTrace::uml::TracedActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedactionexecutionspecification_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedActionExecutionSpecification)

@given(instance=TracedObjectNode_strategy)
@settings(max_examples=50)
def test_tracedobjectnode_instantiation(instance):
    assert isinstance(instance, TracedObjectNode)

@given(instance=umlTrace::uml::TracedExpansionNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedexpansionnode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedExpansionNode)

@given(instance=umlTrace::uml::TracedActivityParameterNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedactivityparameternode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedActivityParameterNode)

@given(instance=umlTrace::uml::TracedCentralBufferNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcentralbuffernode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedCentralBufferNode)

@given(instance=TracedCentralBufferNode_strategy)
@settings(max_examples=50)
def test_tracedcentralbuffernode_instantiation(instance):
    assert isinstance(instance, TracedCentralBufferNode)

@given(instance=umlTrace::uml::TracedDataStoreNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddatastorenode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDataStoreNode)

@given(instance=TracedDataType_strategy)
@settings(max_examples=50)
def test_traceddatatype_instantiation(instance):
    assert isinstance(instance, TracedDataType)

@given(instance=umlTrace::uml::TracedEnumeration_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedenumeration_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedEnumeration)

@given(instance=umlTrace::uml::TracedPrimitiveType_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedprimitivetype_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedPrimitiveType)

@given(instance=TracedMessageEvent_strategy)
@settings(max_examples=50)
def test_tracedmessageevent_instantiation(instance):
    assert isinstance(instance, TracedMessageEvent)

@given(instance=umlTrace::uml::TracedCallEvent_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcallevent_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedCallEvent)

@given(instance=umlTrace::uml::TracedAnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedanyreceiveevent_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedAnyReceiveEvent)

@given(instance=uml::TracedBehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml::tracedbehavioralfeature_instantiation(instance):
    assert isinstance(instance, uml::TracedBehavioralFeature)

@given(instance=TracedTemplateParameter_strategy)
@settings(max_examples=50)
def test_tracedtemplateparameter_instantiation(instance):
    assert isinstance(instance, TracedTemplateParameter)

@given(instance=umlTrace::uml::TracedConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedconnectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedConnectableElementTemplateParameter)

@given(instance=umlTrace::uml::TracedClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedclassifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedClassifierTemplateParameter)

@given(instance=TracedPackage_strategy)
@settings(max_examples=50)
def test_tracedpackage_instantiation(instance):
    assert isinstance(instance, TracedPackage)

@given(instance=umlTrace::uml::TracedProfile_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedprofile_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedProfile)

@given(instance=umlTrace::uml::TracedModel_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedmodel_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedModel)

@given(instance=TracedTransition_strategy)
@settings(max_examples=50)
def test_tracedtransition_instantiation(instance):
    assert isinstance(instance, TracedTransition)

@given(instance=umlTrace::uml::TracedProtocolTransition_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedprotocoltransition_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedProtocolTransition)

@given(instance=TracedWriteVariableAction_strategy)
@settings(max_examples=50)
def test_tracedwritevariableaction_instantiation(instance):
    assert isinstance(instance, TracedWriteVariableAction)

@given(instance=umlTrace::uml::TracedRemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedremovevariablevalueaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedRemoveVariableValueAction)

@given(instance=umlTrace::uml::TracedAddVariableValueAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedaddvariablevalueaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedAddVariableValueAction)

@given(instance=TracedInteractionUse_strategy)
@settings(max_examples=50)
def test_tracedinteractionuse_instantiation(instance):
    assert isinstance(instance, TracedInteractionUse)

@given(instance=umlTrace::uml::TracedPartDecomposition_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedpartdecomposition_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedPartDecomposition)

@given(instance=TracedObservation_strategy)
@settings(max_examples=50)
def test_tracedobservation_instantiation(instance):
    assert isinstance(instance, TracedObservation)

@given(instance=umlTrace::uml::TracedTimeObservation_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtimeobservation_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTimeObservation)

@given(instance=umlTrace::uml::TracedDurationObservation_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddurationobservation_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDurationObservation)

@given(instance=umlTrace::uml::TracedOperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedoperationtemplateparameter_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedOperationTemplateParameter)

@given(instance=TracedInterval_strategy)
@settings(max_examples=50)
def test_tracedinterval_instantiation(instance):
    assert isinstance(instance, TracedInterval)

@given(instance=umlTrace::uml::TracedDurationInterval_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddurationinterval_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDurationInterval)

@given(instance=umlTrace::uml::TracedTimeInterval_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtimeinterval_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTimeInterval)

@given(instance=umlTrace::uml::TracedSignalEvent_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedsignalevent_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedSignalEvent)

@given(instance=TracedBehavioralFeature_strategy)
@settings(max_examples=50)
def test_tracedbehavioralfeature_instantiation(instance):
    assert isinstance(instance, TracedBehavioralFeature)

@given(instance=umlTrace::uml::TracedReception_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedreception_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedReception)

@given(instance=TracedDependency_strategy)
@settings(max_examples=50)
def test_traceddependency_instantiation(instance):
    assert isinstance(instance, TracedDependency)

@given(instance=umlTrace::uml::TracedUsage_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedusage_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedUsage)

@given(instance=umlTrace::uml::TracedAbstraction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedabstraction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedAbstraction)

@given(instance=TracedAbstraction_strategy)
@settings(max_examples=50)
def test_tracedabstraction_instantiation(instance):
    assert isinstance(instance, TracedAbstraction)

@given(instance=umlTrace::uml::TracedManifestation_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedmanifestation_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedManifestation)

@given(instance=umlTrace::uml::TracedRealization_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedrealization_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedRealization)

@given(instance=TracedRealization_strategy)
@settings(max_examples=50)
def test_tracedrealization_instantiation(instance):
    assert isinstance(instance, TracedRealization)

@given(instance=umlTrace::uml::TracedComponentRealization_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcomponentrealization_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedComponentRealization)

@given(instance=umlTrace::uml::TracedInterfaceRealization_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinterfacerealization_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInterfaceRealization)

@given(instance=umlTrace::uml::TracedSubstitution_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedsubstitution_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedSubstitution)

@given(instance=TracedInstanceSpecification_strategy)
@settings(max_examples=50)
def test_tracedinstancespecification_instantiation(instance):
    assert isinstance(instance, TracedInstanceSpecification)

@given(instance=umlTrace::uml::TracedEnumerationLiteral_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedenumerationliteral_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedEnumerationLiteral)

@given(instance=TracedAcceptEventAction_strategy)
@settings(max_examples=50)
def test_tracedaccepteventaction_instantiation(instance):
    assert isinstance(instance, TracedAcceptEventAction)

@given(instance=umlTrace::uml::TracedAcceptCallAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedacceptcallaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedAcceptCallAction)

@given(instance=TracedLinkEndData_strategy)
@settings(max_examples=50)
def test_tracedlinkenddata_instantiation(instance):
    assert isinstance(instance, TracedLinkEndData)

@given(instance=umlTrace::uml::TracedLinkEndCreationData_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedlinkendcreationdata_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLinkEndCreationData)

@given(instance=umlTrace::uml::TracedLinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedlinkenddestructiondata_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLinkEndDestructionData)

@given(instance=TracedClass_strategy)
@settings(max_examples=50)
def test_tracedclass_instantiation(instance):
    assert isinstance(instance, TracedClass)

@given(instance=umlTrace::uml::TracedComponent_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcomponent_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedComponent)

@given(instance=umlTrace::uml::TracedStereotype_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedstereotype_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedStereotype)

@given(instance=umlTrace::uml::TracedBehavior_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedbehavior_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedBehavior)

@given(instance=uml::TracedInteractionFragment_strategy)
@settings(max_examples=50)
def test_uml::tracedinteractionfragment_instantiation(instance):
    assert isinstance(instance, uml::TracedInteractionFragment)

@given(instance=uml::TracedBehavior_strategy)
@settings(max_examples=50)
def test_uml::tracedbehavior_instantiation(instance):
    assert isinstance(instance, uml::TracedBehavior)

@given(instance=umlTrace::uml::TracedInteraction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinteraction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInteraction)

@given(instance=TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_tracedactivityedge_instantiation(instance):
    assert isinstance(instance, TracedActivityEdge)

@given(instance=umlTrace::uml::TracedControlFlow_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcontrolflow_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedControlFlow)

@given(instance=umlTrace::uml::TracedObjectFlow_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedobjectflow_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedObjectFlow)

@given(instance=TracedStateMachine_strategy)
@settings(max_examples=50)
def test_tracedstatemachine_instantiation(instance):
    assert isinstance(instance, TracedStateMachine)

@given(instance=umlTrace::uml::TracedProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedprotocolstatemachine_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedProtocolStateMachine)

@given(instance=umlTrace::uml::TracedDeployment_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddeployment_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDeployment)

@given(instance=TracedBehavior_strategy)
@settings(max_examples=50)
def test_tracedbehavior_instantiation(instance):
    assert isinstance(instance, TracedBehavior)

@given(instance=umlTrace::uml::TracedOpaqueBehavior_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedopaquebehavior_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedOpaqueBehavior)

@given(instance=umlTrace::uml::TracedActivity_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedactivity_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedActivity)

@given(instance=umlTrace::uml::TracedStateMachine_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedstatemachine_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedStateMachine)

@given(instance=TracedActivityGroup_strategy)
@settings(max_examples=50)
def test_tracedactivitygroup_instantiation(instance):
    assert isinstance(instance, TracedActivityGroup)

@given(instance=umlTrace::uml::TracedInterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinterruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInterruptibleActivityRegion)

@given(instance=umlTrace::uml::TracedActivityPartition_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedactivitypartition_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedActivityPartition)

@given(instance=uml::TracedRelationship_strategy)
@settings(max_examples=50)
def test_uml::tracedrelationship_instantiation(instance):
    assert isinstance(instance, uml::TracedRelationship)

@given(instance=umlTrace::IntermediateActivities::TracedActivityExecution_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactivities::tracedactivityexecution_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActivities::TracedActivityExecution)

@given(instance=TracedSemanticVisitor_strategy)
@settings(max_examples=50)
def test_tracedsemanticvisitor_instantiation(instance):
    assert isinstance(instance, TracedSemanticVisitor)

@given(instance=umlTrace::Kernel::TracedEvaluation_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedevaluation_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedEvaluation)

@given(instance=umlTrace::Kernel::TracedValue_strategy)
@settings(max_examples=50)
def test_umltrace::kernel::tracedvalue_instantiation(instance):
    assert isinstance(instance, umlTrace::Kernel::TracedValue)

@given(instance=umlTrace::IntermediateActivities::TracedActivityNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactivities::tracedactivitynodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActivities::TracedActivityNodeActivation)

@given(instance=TracedActivityNodeActivation_strategy)
@settings(max_examples=50)
def test_tracedactivitynodeactivation_instantiation(instance):
    assert isinstance(instance, TracedActivityNodeActivation)

@given(instance=umlTrace::BasicActions::TracedActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace::basicactions::tracedactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::BasicActions::TracedActionActivation)

@given(instance=umlTrace::IntermediateActivities::TracedObjectNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactivities::tracedobjectnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActivities::TracedObjectNodeActivation)

@given(instance=umlTrace::IntermediateActivities::TracedControlNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactivities::tracedcontrolnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActivities::TracedControlNodeActivation)

@given(instance=TracedControlNodeActivation_strategy)
@settings(max_examples=50)
def test_tracedcontrolnodeactivation_instantiation(instance):
    assert isinstance(instance, TracedControlNodeActivation)

@given(instance=umlTrace::IntermediateActivities::TracedInitialNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactivities::tracedinitialnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActivities::TracedInitialNodeActivation)

@given(instance=umlTrace::IntermediateActivities::TracedActivityFinalNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactivities::tracedactivityfinalnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActivities::TracedActivityFinalNodeActivation)

@given(instance=umlTrace::IntermediateActivities::TracedDecisionNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactivities::traceddecisionnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActivities::TracedDecisionNodeActivation)

@given(instance=umlTrace::IntermediateActivities::TracedJoinNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactivities::tracedjoinnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActivities::TracedJoinNodeActivation)

@given(instance=umlTrace::IntermediateActivities::TracedMergeNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactivities::tracedmergenodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActivities::TracedMergeNodeActivation)

@given(instance=umlTrace::IntermediateActivities::TracedForkNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace::intermediateactivities::tracedforknodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace::IntermediateActivities::TracedForkNodeActivation)

@given(instance=uml::TracedVertex_strategy)
@settings(max_examples=50)
def test_uml::tracedvertex_instantiation(instance):
    assert isinstance(instance, uml::TracedVertex)

@given(instance=TracedState_strategy)
@settings(max_examples=50)
def test_tracedstate_instantiation(instance):
    assert isinstance(instance, TracedState)

@given(instance=umlTrace::uml::TracedFinalState_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedfinalstate_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedFinalState)

@given(instance=uml::TracedActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml::tracedactivityfinalnode_instantiation(instance):
    assert isinstance(instance, uml::TracedActivityFinalNode)

@given(instance=uml::TracedClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml::tracedclassifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, uml::TracedClassifierTemplateParameter)

@given(instance=TracedInteractionFragment_strategy)
@settings(max_examples=50)
def test_tracedinteractionfragment_instantiation(instance):
    assert isinstance(instance, TracedInteractionFragment)

@given(instance=umlTrace::uml::TracedStateInvariant_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedstateinvariant_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedStateInvariant)

@given(instance=umlTrace::uml::TracedExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedexecutionspecification_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedExecutionSpecification)

@given(instance=umlTrace::uml::TracedCombinedFragment_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcombinedfragment_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedCombinedFragment)

@given(instance=uml::TracedGeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml::tracedgeneralordering_instantiation(instance):
    assert isinstance(instance, uml::TracedGeneralOrdering)

@given(instance=uml::TracedElementImport_strategy)
@settings(max_examples=50)
def test_uml::tracedelementimport_instantiation(instance):
    assert isinstance(instance, uml::TracedElementImport)

@given(instance=uml::TracedMergeNode_strategy)
@settings(max_examples=50)
def test_uml::tracedmergenode_instantiation(instance):
    assert isinstance(instance, uml::TracedMergeNode)

@given(instance=uml::TracedClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml::tracedclearassociationaction_instantiation(instance):
    assert isinstance(instance, uml::TracedClearAssociationAction)

@given(instance=uml::TracedLinkEndCreationData_strategy)
@settings(max_examples=50)
def test_uml::tracedlinkendcreationdata_instantiation(instance):
    assert isinstance(instance, uml::TracedLinkEndCreationData)

@given(instance=uml::TracedPseudostate_strategy)
@settings(max_examples=50)
def test_uml::tracedpseudostate_instantiation(instance):
    assert isinstance(instance, uml::TracedPseudostate)

@given(instance=uml::TracedComponent_strategy)
@settings(max_examples=50)
def test_uml::tracedcomponent_instantiation(instance):
    assert isinstance(instance, uml::TracedComponent)

@given(instance=uml::TracedReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml::tracedreadisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, uml::TracedReadIsClassifiedObjectAction)

@given(instance=uml::TracedAbstraction_strategy)
@settings(max_examples=50)
def test_uml::tracedabstraction_instantiation(instance):
    assert isinstance(instance, uml::TracedAbstraction)

@given(instance=uml::TracedTimeExpression_strategy)
@settings(max_examples=50)
def test_uml::tracedtimeexpression_instantiation(instance):
    assert isinstance(instance, uml::TracedTimeExpression)

@given(instance=uml::TracedValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_uml::tracedvaluespecificationaction_instantiation(instance):
    assert isinstance(instance, uml::TracedValueSpecificationAction)

@given(instance=uml::TracedFunctionBehavior_strategy)
@settings(max_examples=50)
def test_uml::tracedfunctionbehavior_instantiation(instance):
    assert isinstance(instance, uml::TracedFunctionBehavior)

@given(instance=IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_integerfunctions::tracedintegergreaterfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution)

@given(instance=IntermediateActivities::TracedMergeNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities::tracedmergenodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::TracedMergeNodeActivation)

@given(instance=uml::TracedTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml::tracedtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml::TracedTemplateParameter)

@given(instance=uml::TracedManifestation_strategy)
@settings(max_examples=50)
def test_uml::tracedmanifestation_instantiation(instance):
    assert isinstance(instance, uml::TracedManifestation)

@given(instance=uml::TracedActor_strategy)
@settings(max_examples=50)
def test_uml::tracedactor_instantiation(instance):
    assert isinstance(instance, uml::TracedActor)

@given(instance=uml::TracedRemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml::tracedremovevariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml::TracedRemoveVariableValueAction)

@given(instance=uml::TracedProfile_strategy)
@settings(max_examples=50)
def test_uml::tracedprofile_instantiation(instance):
    assert isinstance(instance, uml::TracedProfile)

@given(instance=uml::TracedTestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml::tracedtestidentityaction_instantiation(instance):
    assert isinstance(instance, uml::TracedTestIdentityAction)

@given(instance=uml::TracedCollaboration_strategy)
@settings(max_examples=50)
def test_uml::tracedcollaboration_instantiation(instance):
    assert isinstance(instance, uml::TracedCollaboration)

@given(instance=uml::TracedSendSignalAction_strategy)
@settings(max_examples=50)
def test_uml::tracedsendsignalaction_instantiation(instance):
    assert isinstance(instance, uml::TracedSendSignalAction)

@given(instance=uml::TracedInterfaceRealization_strategy)
@settings(max_examples=50)
def test_uml::tracedinterfacerealization_instantiation(instance):
    assert isinstance(instance, uml::TracedInterfaceRealization)

@given(instance=uml::TracedUnmarshallAction_strategy)
@settings(max_examples=50)
def test_uml::tracedunmarshallaction_instantiation(instance):
    assert isinstance(instance, uml::TracedUnmarshallAction)

@given(instance=uml::TracedExpression_strategy)
@settings(max_examples=50)
def test_uml::tracedexpression_instantiation(instance):
    assert isinstance(instance, uml::TracedExpression)

@given(instance=uml::TracedAssociation_strategy)
@settings(max_examples=50)
def test_uml::tracedassociation_instantiation(instance):
    assert isinstance(instance, uml::TracedAssociation)

@given(instance=uml::TracedClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml::tracedclearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml::TracedClearStructuralFeatureAction)

@given(instance=uml::TracedAddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml::tracedaddvariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml::TracedAddVariableValueAction)

@given(instance=uml::TracedLiteralReal_strategy)
@settings(max_examples=50)
def test_uml::tracedliteralreal_instantiation(instance):
    assert isinstance(instance, uml::TracedLiteralReal)

@given(instance=IntermediateActions::TracedCreateObjectActionActivation_strategy)
@settings(max_examples=50)
def test_intermediateactions::tracedcreateobjectactionactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActions::TracedCreateObjectActionActivation)

@given(instance=uml::TracedSlot_strategy)
@settings(max_examples=50)
def test_uml::tracedslot_instantiation(instance):
    assert isinstance(instance, uml::TracedSlot)

@given(instance=uml::TracedLiteralNull_strategy)
@settings(max_examples=50)
def test_uml::tracedliteralnull_instantiation(instance):
    assert isinstance(instance, uml::TracedLiteralNull)

@given(instance=IntermediateActions::TracedValueSpecificationActionActivation_strategy)
@settings(max_examples=50)
def test_intermediateactions::tracedvaluespecificationactionactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActions::TracedValueSpecificationActionActivation)

@given(instance=uml::TracedStartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml::tracedstartobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, uml::TracedStartObjectBehaviorAction)

@given(instance=uml::TracedLiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml::tracedliteralboolean_instantiation(instance):
    assert isinstance(instance, uml::TracedLiteralBoolean)

@given(instance=uml::TracedReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml::tracedreadlinkaction_instantiation(instance):
    assert isinstance(instance, uml::TracedReadLinkAction)

@given(instance=uml::TracedInclude_strategy)
@settings(max_examples=50)
def test_uml::tracedinclude_instantiation(instance):
    assert isinstance(instance, uml::TracedInclude)

@given(instance=uml::TracedRegion_strategy)
@settings(max_examples=50)
def test_uml::tracedregion_instantiation(instance):
    assert isinstance(instance, uml::TracedRegion)

@given(instance=uml::TracedState_strategy)
@settings(max_examples=50)
def test_uml::tracedstate_instantiation(instance):
    assert isinstance(instance, uml::TracedState)

@given(instance=uml::TracedPrimitiveType_strategy)
@settings(max_examples=50)
def test_uml::tracedprimitivetype_instantiation(instance):
    assert isinstance(instance, uml::TracedPrimitiveType)

@given(instance=uml::TracedStringExpression_strategy)
@settings(max_examples=50)
def test_uml::tracedstringexpression_instantiation(instance):
    assert isinstance(instance, uml::TracedStringExpression)

@given(instance=uml::TracedLinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_uml::tracedlinkenddestructiondata_instantiation(instance):
    assert isinstance(instance, uml::TracedLinkEndDestructionData)

@given(instance=uml::TracedReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml::tracedreadextentaction_instantiation(instance):
    assert isinstance(instance, uml::TracedReadExtentAction)

@given(instance=BasicActions::TracedOutputPinActivation_strategy)
@settings(max_examples=50)
def test_basicactions::tracedoutputpinactivation_instantiation(instance):
    assert isinstance(instance, BasicActions::TracedOutputPinActivation)

@given(instance=uml::TracedTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml::tracedtemplatesignature_instantiation(instance):
    assert isinstance(instance, uml::TracedTemplateSignature)

@given(instance=uml::TracedRaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml::tracedraiseexceptionaction_instantiation(instance):
    assert isinstance(instance, uml::TracedRaiseExceptionAction)

@given(instance=uml::TracedCommunicationPath_strategy)
@settings(max_examples=50)
def test_uml::tracedcommunicationpath_instantiation(instance):
    assert isinstance(instance, uml::TracedCommunicationPath)

@given(instance=Kernel::TracedLiteralBooleanEvaluation_strategy)
@settings(max_examples=50)
def test_kernel::tracedliteralbooleanevaluation_instantiation(instance):
    assert isinstance(instance, Kernel::TracedLiteralBooleanEvaluation)

@given(instance=uml::TracedEnumeration_strategy)
@settings(max_examples=50)
def test_uml::tracedenumeration_instantiation(instance):
    assert isinstance(instance, uml::TracedEnumeration)

@given(instance=uml::TracedReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml::tracedreadlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, uml::TracedReadLinkObjectEndAction)

@given(instance=uml::TracedCallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml::tracedcallbehavioraction_instantiation(instance):
    assert isinstance(instance, uml::TracedCallBehaviorAction)

@given(instance=uml::TracedVariable_strategy)
@settings(max_examples=50)
def test_uml::tracedvariable_instantiation(instance):
    assert isinstance(instance, uml::TracedVariable)

@given(instance=uml::TracedConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml::tracedconnectorend_instantiation(instance):
    assert isinstance(instance, uml::TracedConnectorEnd)

@given(instance=uml::TracedArtifact_strategy)
@settings(max_examples=50)
def test_uml::tracedartifact_instantiation(instance):
    assert isinstance(instance, uml::TracedArtifact)

@given(instance=uml::TracedCallOperationAction_strategy)
@settings(max_examples=50)
def test_uml::tracedcalloperationaction_instantiation(instance):
    assert isinstance(instance, uml::TracedCallOperationAction)

@given(instance=uml::TracedLiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml::tracedliteralunlimitednatural_instantiation(instance):
    assert isinstance(instance, uml::TracedLiteralUnlimitedNatural)

@given(instance=uml::TracedDurationObservation_strategy)
@settings(max_examples=50)
def test_uml::traceddurationobservation_instantiation(instance):
    assert isinstance(instance, uml::TracedDurationObservation)

@given(instance=uml::TracedBehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml::tracedbehaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml::TracedBehaviorExecutionSpecification)

@given(instance=uml::TracedActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml::tracedactivityparameternode_instantiation(instance):
    assert isinstance(instance, uml::TracedActivityParameterNode)

@given(instance=uml::TracedExpansionNode_strategy)
@settings(max_examples=50)
def test_uml::tracedexpansionnode_instantiation(instance):
    assert isinstance(instance, uml::TracedExpansionNode)

@given(instance=uml::TracedProfileApplication_strategy)
@settings(max_examples=50)
def test_uml::tracedprofileapplication_instantiation(instance):
    assert isinstance(instance, uml::TracedProfileApplication)

@given(instance=uml::TracedAddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml::tracedaddstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml::TracedAddStructuralFeatureValueAction)

@given(instance=uml::TracedQualifierValue_strategy)
@settings(max_examples=50)
def test_uml::tracedqualifiervalue_instantiation(instance):
    assert isinstance(instance, uml::TracedQualifierValue)

@given(instance=uml::TracedImage_strategy)
@settings(max_examples=50)
def test_uml::tracedimage_instantiation(instance):
    assert isinstance(instance, uml::TracedImage)

@given(instance=uml::TracedExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml::tracedextensionend_instantiation(instance):
    assert isinstance(instance, uml::TracedExtensionEnd)

@given(instance=uml::TracedProperty_strategy)
@settings(max_examples=50)
def test_uml::tracedproperty_instantiation(instance):
    assert isinstance(instance, uml::TracedProperty)

@given(instance=uml::TracedDevice_strategy)
@settings(max_examples=50)
def test_uml::traceddevice_instantiation(instance):
    assert isinstance(instance, uml::TracedDevice)

@given(instance=uml::TracedOpaqueAction_strategy)
@settings(max_examples=50)
def test_uml::tracedopaqueaction_instantiation(instance):
    assert isinstance(instance, uml::TracedOpaqueAction)

@given(instance=uml::TracedFinalState_strategy)
@settings(max_examples=50)
def test_uml::tracedfinalstate_instantiation(instance):
    assert isinstance(instance, uml::TracedFinalState)

@given(instance=uml::TracedReduceAction_strategy)
@settings(max_examples=50)
def test_uml::tracedreduceaction_instantiation(instance):
    assert isinstance(instance, uml::TracedReduceAction)

@given(instance=uml::TracedDuration_strategy)
@settings(max_examples=50)
def test_uml::tracedduration_instantiation(instance):
    assert isinstance(instance, uml::TracedDuration)

@given(instance=uml::TracedTemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_uml::tracedtemplateparametersubstitution_instantiation(instance):
    assert isinstance(instance, uml::TracedTemplateParameterSubstitution)

@given(instance=uml::TracedOutputPin_strategy)
@settings(max_examples=50)
def test_uml::tracedoutputpin_instantiation(instance):
    assert isinstance(instance, uml::TracedOutputPin)

@given(instance=uml::TracedActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml::tracedactionexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml::TracedActionExecutionSpecification)

@given(instance=uml::TracedInformationItem_strategy)
@settings(max_examples=50)
def test_uml::tracedinformationitem_instantiation(instance):
    assert isinstance(instance, uml::TracedInformationItem)

@given(instance=uml::TracedOperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml::tracedoperationtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml::TracedOperationTemplateParameter)

@given(instance=uml::TracedConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml::tracedconnectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml::TracedConnectableElementTemplateParameter)

@given(instance=uml::TracedLinkEndData_strategy)
@settings(max_examples=50)
def test_uml::tracedlinkenddata_instantiation(instance):
    assert isinstance(instance, uml::TracedLinkEndData)

@given(instance=uml::TracedDurationInterval_strategy)
@settings(max_examples=50)
def test_uml::traceddurationinterval_instantiation(instance):
    assert isinstance(instance, uml::TracedDurationInterval)

@given(instance=uml::TracedTransition_strategy)
@settings(max_examples=50)
def test_uml::tracedtransition_instantiation(instance):
    assert isinstance(instance, uml::TracedTransition)

@given(instance=uml::TracedTrigger_strategy)
@settings(max_examples=50)
def test_uml::tracedtrigger_instantiation(instance):
    assert isinstance(instance, uml::TracedTrigger)

@given(instance=uml::TracedReplyAction_strategy)
@settings(max_examples=50)
def test_uml::tracedreplyaction_instantiation(instance):
    assert isinstance(instance, uml::TracedReplyAction)

@given(instance=uml::TracedClause_strategy)
@settings(max_examples=50)
def test_uml::tracedclause_instantiation(instance):
    assert isinstance(instance, uml::TracedClause)

@given(instance=uml::TracedPackageMerge_strategy)
@settings(max_examples=50)
def test_uml::tracedpackagemerge_instantiation(instance):
    assert isinstance(instance, uml::TracedPackageMerge)

@given(instance=uml::TracedDecisionNode_strategy)
@settings(max_examples=50)
def test_uml::traceddecisionnode_instantiation(instance):
    assert isinstance(instance, uml::TracedDecisionNode)

@given(instance=IntermediateActions::TracedReadStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_intermediateactions::tracedreadstructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActions::TracedReadStructuralFeatureActionActivation)

@given(instance=uml::TracedReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml::tracedreadselfaction_instantiation(instance):
    assert isinstance(instance, uml::TracedReadSelfAction)

@given(instance=uml::TracedOperation_strategy)
@settings(max_examples=50)
def test_uml::tracedoperation_instantiation(instance):
    assert isinstance(instance, uml::TracedOperation)

@given(instance=uml::TracedObjectFlow_strategy)
@settings(max_examples=50)
def test_uml::tracedobjectflow_instantiation(instance):
    assert isinstance(instance, uml::TracedObjectFlow)

@given(instance=uml::TracedParameterSet_strategy)
@settings(max_examples=50)
def test_uml::tracedparameterset_instantiation(instance):
    assert isinstance(instance, uml::TracedParameterSet)

@given(instance=uml::TracedOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml::tracedoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml::TracedOccurrenceSpecification)

@given(instance=uml::TracedAcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml::tracedaccepteventaction_instantiation(instance):
    assert isinstance(instance, uml::TracedAcceptEventAction)

@given(instance=uml::TracedComponentRealization_strategy)
@settings(max_examples=50)
def test_uml::tracedcomponentrealization_instantiation(instance):
    assert isinstance(instance, uml::TracedComponentRealization)

@given(instance=uml::TracedDataType_strategy)
@settings(max_examples=50)
def test_uml::traceddatatype_instantiation(instance):
    assert isinstance(instance, uml::TracedDataType)

@given(instance=uml::TracedComment_strategy)
@settings(max_examples=50)
def test_uml::tracedcomment_instantiation(instance):
    assert isinstance(instance, uml::TracedComment)

@given(instance=uml::TracedLoopNode_strategy)
@settings(max_examples=50)
def test_uml::tracedloopnode_instantiation(instance):
    assert isinstance(instance, uml::TracedLoopNode)

@given(instance=uml::TracedCallEvent_strategy)
@settings(max_examples=50)
def test_uml::tracedcallevent_instantiation(instance):
    assert isinstance(instance, uml::TracedCallEvent)

@given(instance=uml::TracedPackage_strategy)
@settings(max_examples=50)
def test_uml::tracedpackage_instantiation(instance):
    assert isinstance(instance, uml::TracedPackage)

@given(instance=uml::TracedProtocolConformance_strategy)
@settings(max_examples=50)
def test_uml::tracedprotocolconformance_instantiation(instance):
    assert isinstance(instance, uml::TracedProtocolConformance)

@given(instance=uml::TracedOpaqueBehavior_strategy)
@settings(max_examples=50)
def test_uml::tracedopaquebehavior_instantiation(instance):
    assert isinstance(instance, uml::TracedOpaqueBehavior)

@given(instance=uml::TracedInterface_strategy)
@settings(max_examples=50)
def test_uml::tracedinterface_instantiation(instance):
    assert isinstance(instance, uml::TracedInterface)

@given(instance=IntermediateActivities::TracedDecisionNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities::traceddecisionnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::TracedDecisionNodeActivation)

@given(instance=uml::TracedInteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml::tracedinteractionconstraint_instantiation(instance):
    assert isinstance(instance, uml::TracedInteractionConstraint)

@given(instance=uml::TracedTimeInterval_strategy)
@settings(max_examples=50)
def test_uml::tracedtimeinterval_instantiation(instance):
    assert isinstance(instance, uml::TracedTimeInterval)

@given(instance=uml::TracedExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml::tracedexecutionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml::TracedExecutionOccurrenceSpecification)

@given(instance=uml::TracedSignal_strategy)
@settings(max_examples=50)
def test_uml::tracedsignal_instantiation(instance):
    assert isinstance(instance, uml::TracedSignal)

@given(instance=uml::TracedExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml::tracedextensionpoint_instantiation(instance):
    assert isinstance(instance, uml::TracedExtensionPoint)

@given(instance=uml::TracedCreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml::tracedcreatelinkaction_instantiation(instance):
    assert isinstance(instance, uml::TracedCreateLinkAction)

@given(instance=Kernel::TracedLiteralIntegerEvaluation_strategy)
@settings(max_examples=50)
def test_kernel::tracedliteralintegerevaluation_instantiation(instance):
    assert isinstance(instance, Kernel::TracedLiteralIntegerEvaluation)

@given(instance=uml::TracedCentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml::tracedcentralbuffernode_instantiation(instance):
    assert isinstance(instance, uml::TracedCentralBufferNode)

@given(instance=uml::TracedModel_strategy)
@settings(max_examples=50)
def test_uml::tracedmodel_instantiation(instance):
    assert isinstance(instance, uml::TracedModel)

@given(instance=uml::TracedRedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml::tracedredefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, uml::TracedRedefinableTemplateSignature)

@given(instance=uml::TracedJoinNode_strategy)
@settings(max_examples=50)
def test_uml::tracedjoinnode_instantiation(instance):
    assert isinstance(instance, uml::TracedJoinNode)

@given(instance=BasicActions::TracedOpaqueActionActivation_strategy)
@settings(max_examples=50)
def test_basicactions::tracedopaqueactionactivation_instantiation(instance):
    assert isinstance(instance, BasicActions::TracedOpaqueActionActivation)

@given(instance=uml::TracedReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml::tracedreadlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, uml::TracedReadLinkObjectEndQualifierAction)

@given(instance=uml::TracedRealization_strategy)
@settings(max_examples=50)
def test_uml::tracedrealization_instantiation(instance):
    assert isinstance(instance, uml::TracedRealization)

@given(instance=uml::TracedConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml::tracedconnectionpointreference_instantiation(instance):
    assert isinstance(instance, uml::TracedConnectionPointReference)

@given(instance=uml::TracedConditionalNode_strategy)
@settings(max_examples=50)
def test_uml::tracedconditionalnode_instantiation(instance):
    assert isinstance(instance, uml::TracedConditionalNode)

@given(instance=Kernel::TracedBooleanValue_strategy)
@settings(max_examples=50)
def test_kernel::tracedbooleanvalue_instantiation(instance):
    assert isinstance(instance, Kernel::TracedBooleanValue)

@given(instance=uml::TracedSignalEvent_strategy)
@settings(max_examples=50)
def test_uml::tracedsignalevent_instantiation(instance):
    assert isinstance(instance, uml::TracedSignalEvent)

@given(instance=uml::TracedLiteralInteger_strategy)
@settings(max_examples=50)
def test_uml::tracedliteralinteger_instantiation(instance):
    assert isinstance(instance, uml::TracedLiteralInteger)

@given(instance=uml::TracedDestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml::traceddestroylinkaction_instantiation(instance):
    assert isinstance(instance, uml::TracedDestroyLinkAction)

@given(instance=IntermediateActivities::TracedActivityFinalNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities::tracedactivityfinalnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::TracedActivityFinalNodeActivation)

@given(instance=uml::TracedReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml::tracedreadvariableaction_instantiation(instance):
    assert isinstance(instance, uml::TracedReadVariableAction)

@given(instance=uml::TracedActionInputPin_strategy)
@settings(max_examples=50)
def test_uml::tracedactioninputpin_instantiation(instance):
    assert isinstance(instance, uml::TracedActionInputPin)

@given(instance=uml::TracedUsage_strategy)
@settings(max_examples=50)
def test_uml::tracedusage_instantiation(instance):
    assert isinstance(instance, uml::TracedUsage)

@given(instance=uml::TracedDeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml::traceddeploymentspecification_instantiation(instance):
    assert isinstance(instance, uml::TracedDeploymentSpecification)

@given(instance=uml::TracedTemplateBinding_strategy)
@settings(max_examples=50)
def test_uml::tracedtemplatebinding_instantiation(instance):
    assert isinstance(instance, uml::TracedTemplateBinding)

@given(instance=TracedAssociation_strategy)
@settings(max_examples=50)
def test_tracedassociation_instantiation(instance):
    assert isinstance(instance, TracedAssociation)

@given(instance=umlTrace::uml::TracedCommunicationPath_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcommunicationpath_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedCommunicationPath)

@given(instance=umlTrace::uml::TracedExtension_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedextension_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedExtension)

@given(instance=TracedStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_tracedstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, TracedStructuralFeatureAction)

@given(instance=umlTrace::uml::TracedClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedclearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedClearStructuralFeatureAction)

@given(instance=umlTrace::uml::TracedReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedreadstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedReadStructuralFeatureAction)

@given(instance=uml::TracedMessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml::tracedmessageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml::TracedMessageOccurrenceSpecification)

@given(instance=umlTrace::uml::TracedWriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedwritestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedWriteStructuralFeatureAction)

@given(instance=uml::TracedReception_strategy)
@settings(max_examples=50)
def test_uml::tracedreception_instantiation(instance):
    assert isinstance(instance, uml::TracedReception)

@given(instance=TracedWriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_tracedwritestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, TracedWriteStructuralFeatureAction)

@given(instance=umlTrace::uml::TracedAddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedaddstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedAddStructuralFeatureValueAction)

@given(instance=umlTrace::uml::TracedRemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedremovestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedRemoveStructuralFeatureValueAction)

@given(instance=TracedBehavioredClassifier_strategy)
@settings(max_examples=50)
def test_tracedbehavioredclassifier_instantiation(instance):
    assert isinstance(instance, TracedBehavioredClassifier)

@given(instance=umlTrace::uml::TracedActor_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedactor_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedActor)

@given(instance=umlTrace::uml::TracedUseCase_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedusecase_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedUseCase)

@given(instance=uml::TracedDeployedArtifact_strategy)
@settings(max_examples=50)
def test_uml::traceddeployedartifact_instantiation(instance):
    assert isinstance(instance, uml::TracedDeployedArtifact)

@given(instance=uml::TracedClassifier_strategy)
@settings(max_examples=50)
def test_uml::tracedclassifier_instantiation(instance):
    assert isinstance(instance, uml::TracedClassifier)

@given(instance=umlTrace::uml::TracedAssociation_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedassociation_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedAssociation)

@given(instance=umlTrace::uml::TracedArtifact_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedartifact_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedArtifact)

@given(instance=TracedArtifact_strategy)
@settings(max_examples=50)
def test_tracedartifact_instantiation(instance):
    assert isinstance(instance, TracedArtifact)

@given(instance=umlTrace::uml::TracedDeploymentSpecification_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddeploymentspecification_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDeploymentSpecification)

@given(instance=uml::TracedActivityNode_strategy)
@settings(max_examples=50)
def test_uml::tracedactivitynode_instantiation(instance):
    assert isinstance(instance, uml::TracedActivityNode)

@given(instance=uml::TracedObjectNode_strategy)
@settings(max_examples=50)
def test_uml::tracedobjectnode_instantiation(instance):
    assert isinstance(instance, uml::TracedObjectNode)

@given(instance=TracedPin_strategy)
@settings(max_examples=50)
def test_tracedpin_instantiation(instance):
    assert isinstance(instance, TracedPin)

@given(instance=umlTrace::uml::TracedOutputPin_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedoutputpin_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedOutputPin)

@given(instance=umlTrace::uml::TracedInputPin_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinputpin_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInputPin)

@given(instance=TracedInputPin_strategy)
@settings(max_examples=50)
def test_tracedinputpin_instantiation(instance):
    assert isinstance(instance, TracedInputPin)

@given(instance=umlTrace::uml::TracedActionInputPin_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedactioninputpin_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedActionInputPin)

@given(instance=umlTrace::uml::TracedValuePin_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedvaluepin_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedValuePin)

@given(instance=uml::TracedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_uml::tracedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, uml::TracedMultiplicityElement)

@given(instance=umlTrace::uml::TracedPin_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedpin_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedPin)

@given(instance=uml::TracedTypedElement_strategy)
@settings(max_examples=50)
def test_uml::tracedtypedelement_instantiation(instance):
    assert isinstance(instance, uml::TracedTypedElement)

@given(instance=umlTrace::uml::TracedObjectNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedobjectnode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedObjectNode)

@given(instance=uml::TracedFeature_strategy)
@settings(max_examples=50)
def test_uml::tracedfeature_instantiation(instance):
    assert isinstance(instance, uml::TracedFeature)

@given(instance=umlTrace::uml::TracedStructuralFeature_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedstructuralfeature_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedStructuralFeature)

@given(instance=TracedValueSpecification_strategy)
@settings(max_examples=50)
def test_tracedvaluespecification_instantiation(instance):
    assert isinstance(instance, TracedValueSpecification)

@given(instance=umlTrace::uml::TracedExpression_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedexpression_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedExpression)

@given(instance=umlTrace::uml::TracedDuration_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedduration_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDuration)

@given(instance=umlTrace::uml::TracedInstanceValue_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinstancevalue_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInstanceValue)

@given(instance=umlTrace::uml::TracedOpaqueExpression_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedopaqueexpression_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedOpaqueExpression)

@given(instance=umlTrace::uml::TracedInterval_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinterval_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInterval)

@given(instance=umlTrace::uml::TracedTimeExpression_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtimeexpression_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTimeExpression)

@given(instance=umlTrace::uml::TracedLiteralSpecification_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedliteralspecification_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLiteralSpecification)

@given(instance=TracedLiteralSpecification_strategy)
@settings(max_examples=50)
def test_tracedliteralspecification_instantiation(instance):
    assert isinstance(instance, TracedLiteralSpecification)

@given(instance=umlTrace::uml::TracedLiteralBoolean_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedliteralboolean_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLiteralBoolean)

@given(instance=umlTrace::uml::TracedLiteralNull_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedliteralnull_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLiteralNull)

@given(instance=umlTrace::uml::TracedLiteralReal_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedliteralreal_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLiteralReal)

@given(instance=umlTrace::uml::TracedLiteralInteger_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedliteralinteger_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLiteralInteger)

@given(instance=umlTrace::uml::TracedLiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedliteralunlimitednatural_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLiteralUnlimitedNatural)

@given(instance=umlTrace::uml::TracedLiteralString_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedliteralstring_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLiteralString)

@given(instance=TracedVariableAction_strategy)
@settings(max_examples=50)
def test_tracedvariableaction_instantiation(instance):
    assert isinstance(instance, TracedVariableAction)

@given(instance=umlTrace::uml::TracedReadVariableAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedreadvariableaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedReadVariableAction)

@given(instance=umlTrace::uml::TracedWriteVariableAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedwritevariableaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedWriteVariableAction)

@given(instance=umlTrace::uml::TracedClearVariableAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedclearvariableaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedClearVariableAction)

@given(instance=umlTrace::uml::TracedContinuation_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcontinuation_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedContinuation)

@given(instance=TracedCombinedFragment_strategy)
@settings(max_examples=50)
def test_tracedcombinedfragment_instantiation(instance):
    assert isinstance(instance, TracedCombinedFragment)

@given(instance=umlTrace::uml::TracedConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedconsiderignorefragment_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedConsiderIgnoreFragment)

@given(instance=TracedNode_strategy)
@settings(max_examples=50)
def test_tracednode_instantiation(instance):
    assert isinstance(instance, TracedNode)

@given(instance=umlTrace::uml::TracedExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedexecutionenvironment_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedExecutionEnvironment)

@given(instance=umlTrace::uml::TracedDevice_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddevice_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDevice)

@given(instance=uml::TracedType_strategy)
@settings(max_examples=50)
def test_uml::tracedtype_instantiation(instance):
    assert isinstance(instance, uml::TracedType)

@given(instance=TracedClassifier_strategy)
@settings(max_examples=50)
def test_tracedclassifier_instantiation(instance):
    assert isinstance(instance, TracedClassifier)

@given(instance=umlTrace::uml::TracedBehavioredClassifier_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedbehavioredclassifier_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedBehavioredClassifier)

@given(instance=umlTrace::uml::TracedInformationItem_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinformationitem_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInformationItem)

@given(instance=umlTrace::uml::TracedDataType_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddatatype_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDataType)

@given(instance=umlTrace::uml::TracedInterface_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinterface_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInterface)

@given(instance=umlTrace::uml::TracedStructuredClassifier_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedstructuredclassifier_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedStructuredClassifier)

@given(instance=TracedStructuredClassifier_strategy)
@settings(max_examples=50)
def test_tracedstructuredclassifier_instantiation(instance):
    assert isinstance(instance, TracedStructuredClassifier)

@given(instance=umlTrace::uml::TracedEncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedencapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedEncapsulatedClassifier)

@given(instance=uml::TracedBehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml::tracedbehavioredclassifier_instantiation(instance):
    assert isinstance(instance, uml::TracedBehavioredClassifier)

@given(instance=umlTrace::uml::TracedCollaboration_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcollaboration_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedCollaboration)

@given(instance=uml::TracedEncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml::tracedencapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, uml::TracedEncapsulatedClassifier)

@given(instance=umlTrace::uml::TracedClass_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedclass_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedClass)

@given(instance=TracedCallAction_strategy)
@settings(max_examples=50)
def test_tracedcallaction_instantiation(instance):
    assert isinstance(instance, TracedCallAction)

@given(instance=umlTrace::uml::TracedStartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedstartobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedStartObjectBehaviorAction)

@given(instance=umlTrace::uml::TracedCallOperationAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcalloperationaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedCallOperationAction)

@given(instance=umlTrace::uml::TracedCallBehaviorAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcallbehavioraction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedCallBehaviorAction)

@given(instance=TracedRelationship_strategy)
@settings(max_examples=50)
def test_tracedrelationship_instantiation(instance):
    assert isinstance(instance, TracedRelationship)

@given(instance=umlTrace::uml::TracedDirectedRelationship_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddirectedrelationship_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDirectedRelationship)

@given(instance=TracedDirectedRelationship_strategy)
@settings(max_examples=50)
def test_traceddirectedrelationship_instantiation(instance):
    assert isinstance(instance, TracedDirectedRelationship)

@given(instance=umlTrace::uml::TracedGeneralization_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedgeneralization_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedGeneralization)

@given(instance=umlTrace::uml::TracedTemplateBinding_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtemplatebinding_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTemplateBinding)

@given(instance=umlTrace::uml::TracedProfileApplication_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedprofileapplication_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedProfileApplication)

@given(instance=umlTrace::uml::TracedPackageImport_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedpackageimport_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedPackageImport)

@given(instance=umlTrace::uml::TracedElementImport_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedelementimport_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedElementImport)

@given(instance=umlTrace::uml::TracedPackageMerge_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedpackagemerge_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedPackageMerge)

@given(instance=umlTrace::uml::TracedProtocolConformance_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedprotocolconformance_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedProtocolConformance)

@given(instance=TracedInvocationAction_strategy)
@settings(max_examples=50)
def test_tracedinvocationaction_instantiation(instance):
    assert isinstance(instance, TracedInvocationAction)

@given(instance=umlTrace::uml::TracedBroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedbroadcastsignalaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedBroadcastSignalAction)

@given(instance=umlTrace::uml::TracedSendSignalAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedsendsignalaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedSendSignalAction)

@given(instance=umlTrace::uml::TracedCallAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcallaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedCallAction)

@given(instance=umlTrace::uml::TracedSendObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedsendobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedSendObjectAction)

@given(instance=TracedRedefinableElement_strategy)
@settings(max_examples=50)
def test_tracedredefinableelement_instantiation(instance):
    assert isinstance(instance, TracedRedefinableElement)

@given(instance=umlTrace::uml::TracedExtensionPoint_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedextensionpoint_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedExtensionPoint)

@given(instance=umlTrace::uml::TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedactivityedge_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedActivityEdge)

@given(instance=umlTrace::uml::TracedFeature_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedfeature_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedFeature)

@given(instance=TracedFeature_strategy)
@settings(max_examples=50)
def test_tracedfeature_instantiation(instance):
    assert isinstance(instance, TracedFeature)

@given(instance=umlTrace::uml::TracedConnector_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedconnector_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedConnector)

@given(instance=uml::TracedTemplateableElement_strategy)
@settings(max_examples=50)
def test_uml::tracedtemplateableelement_instantiation(instance):
    assert isinstance(instance, uml::TracedTemplateableElement)

@given(instance=umlTrace::uml::TracedStringExpression_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedstringexpression_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedStringExpression)

@given(instance=uml::TracedPackageableElement_strategy)
@settings(max_examples=50)
def test_uml::tracedpackageableelement_instantiation(instance):
    assert isinstance(instance, uml::TracedPackageableElement)

@given(instance=umlTrace::uml::TracedValueSpecification_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedvaluespecification_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedValueSpecification)

@given(instance=uml::TracedDeploymentTarget_strategy)
@settings(max_examples=50)
def test_uml::traceddeploymenttarget_instantiation(instance):
    assert isinstance(instance, uml::TracedDeploymentTarget)

@given(instance=umlTrace::uml::TracedInstanceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinstancespecification_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInstanceSpecification)

@given(instance=uml::TracedConnectableElement_strategy)
@settings(max_examples=50)
def test_uml::tracedconnectableelement_instantiation(instance):
    assert isinstance(instance, uml::TracedConnectableElement)

@given(instance=umlTrace::uml::TracedParameter_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedparameter_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedParameter)

@given(instance=umlTrace::uml::TracedVariable_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedvariable_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedVariable)

@given(instance=uml::TracedStructuralFeature_strategy)
@settings(max_examples=50)
def test_uml::tracedstructuralfeature_instantiation(instance):
    assert isinstance(instance, uml::TracedStructuralFeature)

@given(instance=umlTrace::uml::TracedProperty_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedproperty_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedProperty)

@given(instance=TracedProperty_strategy)
@settings(max_examples=50)
def test_tracedproperty_instantiation(instance):
    assert isinstance(instance, TracedProperty)

@given(instance=umlTrace::uml::TracedExtensionEnd_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedextensionend_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedExtensionEnd)

@given(instance=umlTrace::uml::TracedPort_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedport_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedPort)

@given(instance=uml::TracedDirectedRelationship_strategy)
@settings(max_examples=50)
def test_uml::traceddirectedrelationship_instantiation(instance):
    assert isinstance(instance, uml::TracedDirectedRelationship)

@given(instance=umlTrace::uml::TracedInformationFlow_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinformationflow_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInformationFlow)

@given(instance=umlTrace::uml::TracedDependency_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddependency_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDependency)

@given(instance=TracedEvent_strategy)
@settings(max_examples=50)
def test_tracedevent_instantiation(instance):
    assert isinstance(instance, TracedEvent)

@given(instance=umlTrace::uml::TracedTimeEvent_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtimeevent_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTimeEvent)

@given(instance=umlTrace::uml::TracedMessageEvent_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedmessageevent_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedMessageEvent)

@given(instance=umlTrace::uml::TracedChangeEvent_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedchangeevent_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedChangeEvent)

@given(instance=umlTrace::uml::TracedSignal_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedsignal_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedSignal)

@given(instance=umlTrace::uml::TracedInteractionUse_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinteractionuse_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInteractionUse)

@given(instance=TracedFinalNode_strategy)
@settings(max_examples=50)
def test_tracedfinalnode_instantiation(instance):
    assert isinstance(instance, TracedFinalNode)

@given(instance=umlTrace::uml::TracedActivityFinalNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedactivityfinalnode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedActivityFinalNode)

@given(instance=umlTrace::uml::TracedFlowFinalNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedflowfinalnode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedFlowFinalNode)

@given(instance=TracedControlNode_strategy)
@settings(max_examples=50)
def test_tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, TracedControlNode)

@given(instance=umlTrace::uml::TracedJoinNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedjoinnode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedJoinNode)

@given(instance=umlTrace::uml::TracedMergeNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedmergenode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedMergeNode)

@given(instance=umlTrace::uml::TracedForkNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedforknode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedForkNode)

@given(instance=umlTrace::uml::TracedFinalNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedfinalnode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedFinalNode)

@given(instance=umlTrace::uml::TracedDecisionNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddecisionnode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDecisionNode)

@given(instance=umlTrace::uml::TracedInitialNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinitialnode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInitialNode)

@given(instance=TracedAction_strategy)
@settings(max_examples=50)
def test_tracedaction_instantiation(instance):
    assert isinstance(instance, TracedAction)

@given(instance=umlTrace::uml::TracedAcceptEventAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedaccepteventaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedAcceptEventAction)

@given(instance=umlTrace::uml::TracedStartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedstartclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedStartClassifierBehaviorAction)

@given(instance=umlTrace::uml::TracedStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedStructuralFeatureAction)

@given(instance=umlTrace::uml::TracedReduceAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedreduceaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedReduceAction)

@given(instance=umlTrace::uml::TracedValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedvaluespecificationaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedValueSpecificationAction)

@given(instance=umlTrace::uml::TracedOpaqueAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedopaqueaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedOpaqueAction)

@given(instance=umlTrace::uml::TracedUnmarshallAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedunmarshallaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedUnmarshallAction)

@given(instance=umlTrace::uml::TracedReadSelfAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedreadselfaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedReadSelfAction)

@given(instance=umlTrace::uml::TracedReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedreadisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedReadIsClassifiedObjectAction)

@given(instance=umlTrace::uml::TracedDestroyObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddestroyobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDestroyObjectAction)

@given(instance=umlTrace::uml::TracedVariableAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedvariableaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedVariableAction)

@given(instance=umlTrace::uml::TracedReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedreadlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedReadLinkObjectEndQualifierAction)

@given(instance=umlTrace::uml::TracedInvocationAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinvocationaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInvocationAction)

@given(instance=umlTrace::uml::TracedRaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedraiseexceptionaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedRaiseExceptionAction)

@given(instance=umlTrace::uml::TracedReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedreadlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedReadLinkObjectEndAction)

@given(instance=umlTrace::uml::TracedClearAssociationAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedclearassociationaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedClearAssociationAction)

@given(instance=umlTrace::uml::TracedReadExtentAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedreadextentaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedReadExtentAction)

@given(instance=umlTrace::uml::TracedReplyAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedreplyaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedReplyAction)

@given(instance=umlTrace::uml::TracedTestIdentityAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtestidentityaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTestIdentityAction)

@given(instance=umlTrace::uml::TracedCreateObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcreateobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedCreateObjectAction)

@given(instance=umlTrace::uml::TracedReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedreclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedReclassifyObjectAction)

@given(instance=umlTrace::uml::TracedLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedlinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLinkAction)

@given(instance=TracedLinkAction_strategy)
@settings(max_examples=50)
def test_tracedlinkaction_instantiation(instance):
    assert isinstance(instance, TracedLinkAction)

@given(instance=umlTrace::uml::TracedReadLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedreadlinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedReadLinkAction)

@given(instance=umlTrace::uml::TracedWriteLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedwritelinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedWriteLinkAction)

@given(instance=TracedWriteLinkAction_strategy)
@settings(max_examples=50)
def test_tracedwritelinkaction_instantiation(instance):
    assert isinstance(instance, TracedWriteLinkAction)

@given(instance=umlTrace::uml::TracedDestroyLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddestroylinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDestroyLinkAction)

@given(instance=umlTrace::uml::TracedCreateLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcreatelinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedCreateLinkAction)

@given(instance=TracedCreateLinkAction_strategy)
@settings(max_examples=50)
def test_tracedcreatelinkaction_instantiation(instance):
    assert isinstance(instance, TracedCreateLinkAction)

@given(instance=umlTrace::uml::TracedCreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcreatelinkobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedCreateLinkObjectAction)

@given(instance=uml::TracedNamedElement_strategy)
@settings(max_examples=50)
def test_uml::tracednamedelement_instantiation(instance):
    assert isinstance(instance, uml::TracedNamedElement)

@given(instance=umlTrace::uml::TracedInclude_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinclude_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInclude)

@given(instance=umlTrace::uml::TracedExtend_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedextend_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedExtend)

@given(instance=ActivityContent_strategy)
@settings(max_examples=50)
def test_activitycontent_instantiation(instance):
    assert isinstance(instance, ActivityContent)

@given(instance=umlTrace::uml::TracedActivityGroup_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedactivitygroup_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedActivityGroup)

@given(instance=uml::TracedRedefinableElement_strategy)
@settings(max_examples=50)
def test_uml::tracedredefinableelement_instantiation(instance):
    assert isinstance(instance, uml::TracedRedefinableElement)

@given(instance=umlTrace::uml::TracedRedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedredefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedRedefinableTemplateSignature)

@given(instance=umlTrace::uml::TracedActivityNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedactivitynode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedActivityNode)

@given(instance=TracedActivityNode_strategy)
@settings(max_examples=50)
def test_tracedactivitynode_instantiation(instance):
    assert isinstance(instance, TracedActivityNode)

@given(instance=umlTrace::uml::TracedControlNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedControlNode)

@given(instance=umlTrace::uml::TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedExecutableNode)

@given(instance=TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, TracedExecutableNode)

@given(instance=umlTrace::uml::TracedAction_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedaction_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedAction)

@given(instance=uml::TracedActivityGroup_strategy)
@settings(max_examples=50)
def test_uml::tracedactivitygroup_instantiation(instance):
    assert isinstance(instance, uml::TracedActivityGroup)

@given(instance=uml::TracedNamespace_strategy)
@settings(max_examples=50)
def test_uml::tracednamespace_instantiation(instance):
    assert isinstance(instance, uml::TracedNamespace)

@given(instance=umlTrace::uml::TracedTransition_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtransition_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTransition)

@given(instance=umlTrace::uml::TracedInteractionOperand_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinteractionoperand_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInteractionOperand)

@given(instance=umlTrace::uml::TracedRegion_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedregion_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedRegion)

@given(instance=umlTrace::uml::TracedPackage_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedpackage_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedPackage)

@given(instance=umlTrace::uml::TracedState_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedstate_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedState)

@given(instance=umlTrace::uml::TracedBehavioralFeature_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedbehavioralfeature_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedBehavioralFeature)

@given(instance=umlTrace::uml::TracedClassifier_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedclassifier_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedClassifier)

@given(instance=uml::TracedAction_strategy)
@settings(max_examples=50)
def test_uml::tracedaction_instantiation(instance):
    assert isinstance(instance, uml::TracedAction)

@given(instance=umlTrace::uml::TracedStructuredActivityNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedstructuredactivitynode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedStructuredActivityNode)

@given(instance=TracedStructuredActivityNode_strategy)
@settings(max_examples=50)
def test_tracedstructuredactivitynode_instantiation(instance):
    assert isinstance(instance, TracedStructuredActivityNode)

@given(instance=umlTrace::uml::TracedExpansionRegion_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedexpansionregion_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedExpansionRegion)

@given(instance=umlTrace::uml::TracedLoopNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedloopnode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLoopNode)

@given(instance=umlTrace::uml::TracedSequenceNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedsequencenode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedSequenceNode)

@given(instance=umlTrace::uml::TracedConditionalNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedconditionalnode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedConditionalNode)

@given(instance=TracedEModelElement_strategy)
@settings(max_examples=50)
def test_tracedemodelelement_instantiation(instance):
    assert isinstance(instance, TracedEModelElement)

@given(instance=umlTrace::uml::TracedElement_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedelement_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedElement)

@given(instance=TracedElement_strategy)
@settings(max_examples=50)
def test_tracedelement_instantiation(instance):
    assert isinstance(instance, TracedElement)

@given(instance=umlTrace::uml::TracedTemplateParameter_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtemplateparameter_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTemplateParameter)

@given(instance=umlTrace::uml::TracedRelationship_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedrelationship_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedRelationship)

@given(instance=umlTrace::uml::TracedLinkEndData_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedlinkenddata_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLinkEndData)

@given(instance=umlTrace::uml::TracedExceptionHandler_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedexceptionhandler_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedExceptionHandler)

@given(instance=umlTrace::uml::TracedSlot_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedslot_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedSlot)

@given(instance=umlTrace::uml::TracedTemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtemplateparametersubstitution_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTemplateParameterSubstitution)

@given(instance=umlTrace::uml::TracedTemplateSignature_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtemplatesignature_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTemplateSignature)

@given(instance=umlTrace::uml::TracedComment_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcomment_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedComment)

@given(instance=umlTrace::uml::TracedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedMultiplicityElement)

@given(instance=umlTrace::uml::TracedTemplateableElement_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtemplateableelement_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTemplateableElement)

@given(instance=umlTrace::uml::TracedClause_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedclause_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedClause)

@given(instance=umlTrace::uml::TracedImage_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedimage_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedImage)

@given(instance=umlTrace::uml::TracedQualifierValue_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedqualifiervalue_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedQualifierValue)

@given(instance=umlTrace::uml::TracedNamedElement_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracednamedelement_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedNamedElement)

@given(instance=TracedNamedElement_strategy)
@settings(max_examples=50)
def test_tracednamedelement_instantiation(instance):
    assert isinstance(instance, TracedNamedElement)

@given(instance=umlTrace::uml::TracedTypedElement_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtypedelement_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTypedElement)

@given(instance=umlTrace::uml::TracedNamespace_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracednamespace_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedNamespace)

@given(instance=umlTrace::uml::TracedRedefinableElement_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedredefinableelement_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedRedefinableElement)

@given(instance=umlTrace::uml::TracedDeploymentTarget_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddeploymenttarget_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDeploymentTarget)

@given(instance=umlTrace::uml::TracedMessage_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedmessage_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedMessage)

@given(instance=umlTrace::uml::TracedCollaborationUse_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedcollaborationuse_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedCollaborationUse)

@given(instance=umlTrace::uml::TracedMessageEnd_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedmessageend_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedMessageEnd)

@given(instance=umlTrace::uml::TracedGeneralOrdering_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedgeneralordering_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedGeneralOrdering)

@given(instance=umlTrace::uml::TracedParameterSet_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedparameterset_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedParameterSet)

@given(instance=umlTrace::uml::TracedTrigger_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtrigger_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTrigger)

@given(instance=umlTrace::uml::TracedLifeline_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedlifeline_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedLifeline)

@given(instance=umlTrace::uml::TracedDeployedArtifact_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddeployedartifact_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDeployedArtifact)

@given(instance=umlTrace::uml::TracedInteractionFragment_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinteractionfragment_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInteractionFragment)

@given(instance=umlTrace::uml::TracedOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedoccurrencespecification_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedOccurrenceSpecification)

@given(instance=uml::TracedMessageEnd_strategy)
@settings(max_examples=50)
def test_uml::tracedmessageend_instantiation(instance):
    assert isinstance(instance, uml::TracedMessageEnd)

@given(instance=umlTrace::uml::TracedMessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedmessageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedMessageOccurrenceSpecification)

@given(instance=TracedMessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_tracedmessageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, TracedMessageOccurrenceSpecification)

@given(instance=umlTrace::uml::TracedDestructionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddestructionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDestructionOccurrenceSpecification)

@given(instance=umlTrace::uml::TracedVertex_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedvertex_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedVertex)

@given(instance=TracedVertex_strategy)
@settings(max_examples=50)
def test_tracedvertex_instantiation(instance):
    assert isinstance(instance, TracedVertex)

@given(instance=umlTrace::uml::TracedConnectionPointReference_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedconnectionpointreference_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedConnectionPointReference)

@given(instance=umlTrace::uml::TracedPseudostate_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedpseudostate_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedPseudostate)

@given(instance=umlTrace::uml::TracedParameterableElement_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedparameterableelement_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedParameterableElement)

@given(instance=uml::TracedParameterableElement_strategy)
@settings(max_examples=50)
def test_uml::tracedparameterableelement_instantiation(instance):
    assert isinstance(instance, uml::TracedParameterableElement)

@given(instance=umlTrace::uml::TracedConnectableElement_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedconnectableelement_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedConnectableElement)

@given(instance=umlTrace::uml::TracedOperation_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedoperation_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedOperation)

@given(instance=umlTrace::uml::TracedPackageableElement_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedpackageableelement_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedPackageableElement)

@given(instance=TracedPackageableElement_strategy)
@settings(max_examples=50)
def test_tracedpackageableelement_instantiation(instance):
    assert isinstance(instance, TracedPackageableElement)

@given(instance=umlTrace::uml::TracedObservation_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedobservation_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedObservation)

@given(instance=umlTrace::uml::TracedEvent_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedevent_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedEvent)

@given(instance=umlTrace::uml::TracedGeneralizationSet_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedgeneralizationset_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedGeneralizationSet)

@given(instance=umlTrace::uml::TracedType_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtype_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedType)

@given(instance=umlTrace::uml::TracedConstraint_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedConstraint)

@given(instance=TracedConstraint_strategy)
@settings(max_examples=50)
def test_tracedconstraint_instantiation(instance):
    assert isinstance(instance, TracedConstraint)

@given(instance=umlTrace::uml::TracedInteractionConstraint_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedinteractionconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedInteractionConstraint)

@given(instance=umlTrace::uml::TracedIntervalConstraint_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedintervalconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedIntervalConstraint)

@given(instance=TracedIntervalConstraint_strategy)
@settings(max_examples=50)
def test_tracedintervalconstraint_instantiation(instance):
    assert isinstance(instance, TracedIntervalConstraint)

@given(instance=umlTrace::uml::TracedTimeConstraint_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedtimeconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedTimeConstraint)

@given(instance=umlTrace::uml::TracedDurationConstraint_strategy)
@settings(max_examples=50)
def test_umltrace::uml::traceddurationconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedDurationConstraint)

@given(instance=uml::TracedControlFlow_strategy)
@settings(max_examples=50)
def test_uml::tracedcontrolflow_instantiation(instance):
    assert isinstance(instance, uml::TracedControlFlow)

@given(instance=uml::TracedTimeObservation_strategy)
@settings(max_examples=50)
def test_uml::tracedtimeobservation_instantiation(instance):
    assert isinstance(instance, uml::TracedTimeObservation)

@given(instance=uml::TracedGate_strategy)
@settings(max_examples=50)
def test_uml::tracedgate_instantiation(instance):
    assert isinstance(instance, uml::TracedGate)

@given(instance=uml::TracedProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml::tracedprotocolstatemachine_instantiation(instance):
    assert isinstance(instance, uml::TracedProtocolStateMachine)

@given(instance=uml::TracedDataStoreNode_strategy)
@settings(max_examples=50)
def test_uml::traceddatastorenode_instantiation(instance):
    assert isinstance(instance, uml::TracedDataStoreNode)

@given(instance=uml::TracedReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml::tracedreadstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml::TracedReadStructuralFeatureAction)

@given(instance=uml::TracedAnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_uml::tracedanyreceiveevent_instantiation(instance):
    assert isinstance(instance, uml::TracedAnyReceiveEvent)

@given(instance=Kernel::TracedIntegerValue_strategy)
@settings(max_examples=50)
def test_kernel::tracedintegervalue_instantiation(instance):
    assert isinstance(instance, Kernel::TracedIntegerValue)

@given(instance=uml::TracedInterval_strategy)
@settings(max_examples=50)
def test_uml::tracedinterval_instantiation(instance):
    assert isinstance(instance, uml::TracedInterval)

@given(instance=uml::TracedRemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml::tracedremovestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml::TracedRemoveStructuralFeatureValueAction)

@given(instance=uml::TracedGeneralization_strategy)
@settings(max_examples=50)
def test_uml::tracedgeneralization_instantiation(instance):
    assert isinstance(instance, uml::TracedGeneralization)

@given(instance=uml::TracedInteractionOperand_strategy)
@settings(max_examples=50)
def test_uml::tracedinteractionoperand_instantiation(instance):
    assert isinstance(instance, uml::TracedInteractionOperand)

@given(instance=uml::TracedProtocolTransition_strategy)
@settings(max_examples=50)
def test_uml::tracedprotocoltransition_instantiation(instance):
    assert isinstance(instance, uml::TracedProtocolTransition)

@given(instance=uml::TracedInterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_uml::tracedinterruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, uml::TracedInterruptibleActivityRegion)

@given(instance=uml::TracedPartDecomposition_strategy)
@settings(max_examples=50)
def test_uml::tracedpartdecomposition_instantiation(instance):
    assert isinstance(instance, uml::TracedPartDecomposition)

@given(instance=uml::TracedTimeEvent_strategy)
@settings(max_examples=50)
def test_uml::tracedtimeevent_instantiation(instance):
    assert isinstance(instance, uml::TracedTimeEvent)

@given(instance=uml::TracedDeployment_strategy)
@settings(max_examples=50)
def test_uml::traceddeployment_instantiation(instance):
    assert isinstance(instance, uml::TracedDeployment)

@given(instance=Loci::TracedSemanticVisitor_strategy)
@settings(max_examples=50)
def test_loci::tracedsemanticvisitor_instantiation(instance):
    assert isinstance(instance, Loci::TracedSemanticVisitor)

@given(instance=Kernel::TracedObject_strategy)
@settings(max_examples=50)
def test_kernel::tracedobject_instantiation(instance):
    assert isinstance(instance, Kernel::TracedObject)

@given(instance=IntermediateActivities::TracedJoinNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities::tracedjoinnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::TracedJoinNodeActivation)

@given(instance=uml::TracedUseCase_strategy)
@settings(max_examples=50)
def test_uml::tracedusecase_instantiation(instance):
    assert isinstance(instance, uml::TracedUseCase)

@given(instance=uml::TracedReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml::tracedreclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, uml::TracedReclassifyObjectAction)

@given(instance=uml::TracedInstanceValue_strategy)
@settings(max_examples=50)
def test_uml::tracedinstancevalue_instantiation(instance):
    assert isinstance(instance, uml::TracedInstanceValue)

@given(instance=IntermediateActions::TracedAddStructuralFeatureValueActionActivation_strategy)
@settings(max_examples=50)
def test_intermediateactions::tracedaddstructuralfeaturevalueactionactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActions::TracedAddStructuralFeatureValueActionActivation)

@given(instance=Kernel::TracedReference_strategy)
@settings(max_examples=50)
def test_kernel::tracedreference_instantiation(instance):
    assert isinstance(instance, Kernel::TracedReference)

@given(instance=uml::TracedForkNode_strategy)
@settings(max_examples=50)
def test_uml::tracedforknode_instantiation(instance):
    assert isinstance(instance, uml::TracedForkNode)

@given(instance=uml::TracedActivity_strategy)
@settings(max_examples=50)
def test_uml::tracedactivity_instantiation(instance):
    assert isinstance(instance, uml::TracedActivity)

@given(instance=uml::TracedMessage_strategy)
@settings(max_examples=50)
def test_uml::tracedmessage_instantiation(instance):
    assert isinstance(instance, uml::TracedMessage)

@given(instance=uml::TracedStateMachine_strategy)
@settings(max_examples=50)
def test_uml::tracedstatemachine_instantiation(instance):
    assert isinstance(instance, uml::TracedStateMachine)

@given(instance=uml::TracedActivityPartition_strategy)
@settings(max_examples=50)
def test_uml::tracedactivitypartition_instantiation(instance):
    assert isinstance(instance, uml::TracedActivityPartition)

@given(instance=IntermediateActivities::TracedActivityParameterNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities::tracedactivityparameternodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::TracedActivityParameterNodeActivation)

@given(instance=BasicActions::TracedCallBehaviorActionActivation_strategy)
@settings(max_examples=50)
def test_basicactions::tracedcallbehavioractionactivation_instantiation(instance):
    assert isinstance(instance, BasicActions::TracedCallBehaviorActionActivation)

@given(instance=uml::TracedDestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml::traceddestroyobjectaction_instantiation(instance):
    assert isinstance(instance, uml::TracedDestroyObjectAction)

@given(instance=uml::TracedAssociationClass_strategy)
@settings(max_examples=50)
def test_uml::tracedassociationclass_instantiation(instance):
    assert isinstance(instance, uml::TracedAssociationClass)

@given(instance=uml::TracedInformationFlow_strategy)
@settings(max_examples=50)
def test_uml::tracedinformationflow_instantiation(instance):
    assert isinstance(instance, uml::TracedInformationFlow)

@given(instance=uml::TracedSubstitution_strategy)
@settings(max_examples=50)
def test_uml::tracedsubstitution_instantiation(instance):
    assert isinstance(instance, uml::TracedSubstitution)

@given(instance=uml::TracedEnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml::tracedenumerationliteral_instantiation(instance):
    assert isinstance(instance, uml::TracedEnumerationLiteral)

@given(instance=uml::TracedStereotype_strategy)
@settings(max_examples=50)
def test_uml::tracedstereotype_instantiation(instance):
    assert isinstance(instance, uml::TracedStereotype)

@given(instance=uml::TracedAcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml::tracedacceptcallaction_instantiation(instance):
    assert isinstance(instance, uml::TracedAcceptCallAction)

@given(instance=uml::TracedInstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml::tracedinstancespecification_instantiation(instance):
    assert isinstance(instance, uml::TracedInstanceSpecification)

@given(instance=IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_integerfunctions::tracedintegerlessfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution)

@given(instance=uml::TracedStateInvariant_strategy)
@settings(max_examples=50)
def test_uml::tracedstateinvariant_instantiation(instance):
    assert isinstance(instance, uml::TracedStateInvariant)

@given(instance=BasicActions::TracedInputPinActivation_strategy)
@settings(max_examples=50)
def test_basicactions::tracedinputpinactivation_instantiation(instance):
    assert isinstance(instance, BasicActions::TracedInputPinActivation)

@given(instance=uml::TracedLiteralString_strategy)
@settings(max_examples=50)
def test_uml::tracedliteralstring_instantiation(instance):
    assert isinstance(instance, uml::TracedLiteralString)

@given(instance=uml::TracedOpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml::tracedopaqueexpression_instantiation(instance):
    assert isinstance(instance, uml::TracedOpaqueExpression)

@given(instance=uml::TracedParameter_strategy)
@settings(max_examples=50)
def test_uml::tracedparameter_instantiation(instance):
    assert isinstance(instance, uml::TracedParameter)

@given(instance=IntermediateActivities::TracedActivityNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities::tracedactivitynodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::TracedActivityNodeActivation)

@given(instance=uml::TracedInteraction_strategy)
@settings(max_examples=50)
def test_uml::tracedinteraction_instantiation(instance):
    assert isinstance(instance, uml::TracedInteraction)

@given(instance=uml::TracedBroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml::tracedbroadcastsignalaction_instantiation(instance):
    assert isinstance(instance, uml::TracedBroadcastSignalAction)

@given(instance=uml::TracedConstraint_strategy)
@settings(max_examples=50)
def test_uml::tracedconstraint_instantiation(instance):
    assert isinstance(instance, uml::TracedConstraint)

@given(instance=uml::TracedClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml::tracedclearvariableaction_instantiation(instance):
    assert isinstance(instance, uml::TracedClearVariableAction)

@given(instance=uml::TracedInputPin_strategy)
@settings(max_examples=50)
def test_uml::tracedinputpin_instantiation(instance):
    assert isinstance(instance, uml::TracedInputPin)

@given(instance=uml::TracedTimeConstraint_strategy)
@settings(max_examples=50)
def test_uml::tracedtimeconstraint_instantiation(instance):
    assert isinstance(instance, uml::TracedTimeConstraint)

@given(instance=uml::TracedContinuation_strategy)
@settings(max_examples=50)
def test_uml::tracedcontinuation_instantiation(instance):
    assert isinstance(instance, uml::TracedContinuation)

@given(instance=uml::TracedConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_uml::tracedconsiderignorefragment_instantiation(instance):
    assert isinstance(instance, uml::TracedConsiderIgnoreFragment)

@given(instance=uml::TracedIntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml::tracedintervalconstraint_instantiation(instance):
    assert isinstance(instance, uml::TracedIntervalConstraint)

@given(instance=uml::TracedExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml::tracedexecutionenvironment_instantiation(instance):
    assert isinstance(instance, uml::TracedExecutionEnvironment)

@given(instance=uml::TracedStructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml::tracedstructuredactivitynode_instantiation(instance):
    assert isinstance(instance, uml::TracedStructuredActivityNode)

@given(instance=uml::TracedExtension_strategy)
@settings(max_examples=50)
def test_uml::tracedextension_instantiation(instance):
    assert isinstance(instance, uml::TracedExtension)

@given(instance=IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_integerfunctions::tracedintegerplusfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution)

@given(instance=uml::TracedExtend_strategy)
@settings(max_examples=50)
def test_uml::tracedextend_instantiation(instance):
    assert isinstance(instance, uml::TracedExtend)

@given(instance=uml::TracedStartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml::tracedstartclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, uml::TracedStartClassifierBehaviorAction)

@given(instance=uml::TracedSequenceNode_strategy)
@settings(max_examples=50)
def test_uml::tracedsequencenode_instantiation(instance):
    assert isinstance(instance, uml::TracedSequenceNode)

@given(instance=uml::TracedExceptionHandler_strategy)
@settings(max_examples=50)
def test_uml::tracedexceptionhandler_instantiation(instance):
    assert isinstance(instance, uml::TracedExceptionHandler)

@given(instance=uml::TracedNode_strategy)
@settings(max_examples=50)
def test_uml::tracednode_instantiation(instance):
    assert isinstance(instance, uml::TracedNode)

@given(instance=uml::TracedValuePin_strategy)
@settings(max_examples=50)
def test_uml::tracedvaluepin_instantiation(instance):
    assert isinstance(instance, uml::TracedValuePin)

@given(instance=IntermediateActivities::TracedActivityExecution_strategy)
@settings(max_examples=50)
def test_intermediateactivities::tracedactivityexecution_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::TracedActivityExecution)

@given(instance=uml::TracedCollaborationUse_strategy)
@settings(max_examples=50)
def test_uml::tracedcollaborationuse_instantiation(instance):
    assert isinstance(instance, uml::TracedCollaborationUse)

@given(instance=IntermediateActivities::TracedInitialNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities::tracedinitialnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::TracedInitialNodeActivation)

@given(instance=uml::TracedPort_strategy)
@settings(max_examples=50)
def test_uml::tracedport_instantiation(instance):
    assert isinstance(instance, uml::TracedPort)

@given(instance=uml::TracedDependency_strategy)
@settings(max_examples=50)
def test_uml::traceddependency_instantiation(instance):
    assert isinstance(instance, uml::TracedDependency)

@given(instance=uml::TracedChangeEvent_strategy)
@settings(max_examples=50)
def test_uml::tracedchangeevent_instantiation(instance):
    assert isinstance(instance, uml::TracedChangeEvent)

@given(instance=uml::TracedGeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml::tracedgeneralizationset_instantiation(instance):
    assert isinstance(instance, uml::TracedGeneralizationSet)

@given(instance=uml::TracedInteractionUse_strategy)
@settings(max_examples=50)
def test_uml::tracedinteractionuse_instantiation(instance):
    assert isinstance(instance, uml::TracedInteractionUse)

@given(instance=uml::TracedClass_strategy)
@settings(max_examples=50)
def test_uml::tracedclass_instantiation(instance):
    assert isinstance(instance, uml::TracedClass)

@given(instance=umlTrace::uml::TracedNode_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracednode_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedNode)

@given(instance=umlTrace::uml::TracedAssociationClass_strategy)
@settings(max_examples=50)
def test_umltrace::uml::tracedassociationclass_instantiation(instance):
    assert isinstance(instance, umlTrace::uml::TracedAssociationClass)

@given(instance=uml::TracedPackageImport_strategy)
@settings(max_examples=50)
def test_uml::tracedpackageimport_instantiation(instance):
    assert isinstance(instance, uml::TracedPackageImport)

@given(instance=uml::TracedSendObjectAction_strategy)
@settings(max_examples=50)
def test_uml::tracedsendobjectaction_instantiation(instance):
    assert isinstance(instance, uml::TracedSendObjectAction)

@given(instance=uml::TracedConnector_strategy)
@settings(max_examples=50)
def test_uml::tracedconnector_instantiation(instance):
    assert isinstance(instance, uml::TracedConnector)

@given(instance=uml::TracedDestructionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml::traceddestructionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml::TracedDestructionOccurrenceSpecification)

@given(instance=uml::TracedDurationConstraint_strategy)
@settings(max_examples=50)
def test_uml::traceddurationconstraint_instantiation(instance):
    assert isinstance(instance, uml::TracedDurationConstraint)

@given(instance=IntermediateActivities::TracedForkNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities::tracedforknodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities::TracedForkNodeActivation)

@given(instance=uml::TracedLifeline_strategy)
@settings(max_examples=50)
def test_uml::tracedlifeline_instantiation(instance):
    assert isinstance(instance, uml::TracedLifeline)

@given(instance=uml::TracedCreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml::tracedcreateobjectaction_instantiation(instance):
    assert isinstance(instance, uml::TracedCreateObjectAction)

@given(instance=uml::TracedExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml::tracedexpansionregion_instantiation(instance):
    assert isinstance(instance, uml::TracedExpansionRegion)

@given(instance=uml::TracedFlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml::tracedflowfinalnode_instantiation(instance):
    assert isinstance(instance, uml::TracedFlowFinalNode)

@given(instance=uml::TracedInitialNode_strategy)
@settings(max_examples=50)
def test_uml::tracedinitialnode_instantiation(instance):
    assert isinstance(instance, uml::TracedInitialNode)

@given(instance=uml::TracedCreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml::tracedcreatelinkobjectaction_instantiation(instance):
    assert isinstance(instance, uml::TracedCreateLinkObjectAction)

@given(instance=uml::TracedCombinedFragment_strategy)
@settings(max_examples=50)
def test_uml::tracedcombinedfragment_instantiation(instance):
    assert isinstance(instance, uml::TracedCombinedFragment)

@given(instance=umlTrace::Traced::TracedObjects_strategy)
@settings(max_examples=50)
def test_umltrace::traced::tracedobjects_instantiation(instance):
    assert isinstance(instance, umlTrace::Traced::TracedObjects)

@given(instance=Traced::TracedObjects_strategy)
@settings(max_examples=50)
def test_traced::tracedobjects_instantiation(instance):
    assert isinstance(instance, Traced::TracedObjects)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=umlTrace::Trace_strategy)
@settings(max_examples=50)
def test_umltrace::trace_instantiation(instance):
    assert isinstance(instance, umlTrace::Trace)

@given(instance=Values::SemanticVisitor::runtimeModelElement::Value_strategy)
@settings(max_examples=50)
def test_values::semanticvisitor::runtimemodelelement::value_instantiation(instance):
    assert isinstance(instance, Values::SemanticVisitor::runtimeModelElement::Value)

@given(instance=Values::ActionActivation::firing::Value_strategy)
@settings(max_examples=50)
def test_values::actionactivation::firing::value_instantiation(instance):
    assert isinstance(instance, Values::ActionActivation::firing::Value)

@given(instance=umlTrace::State_strategy)
@settings(max_examples=50)
def test_umltrace::state_instantiation(instance):
    assert isinstance(instance, umlTrace::State)
