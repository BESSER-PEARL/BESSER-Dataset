import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    uml_umlTrace_ControlFlow,
    uml_umlTrace_TestIdentityAction,
    uml_umlTrace_AddVariableValueAction,
    TracedWriteVariableAction,
    umlTrace_uml_TracedAddVariableValueAction,
    uml_TracedObjectNode,
    uml_umlTrace_ClearAssociationAction,
    TracedBehavioralFeature,
    umlTrace_uml_TracedReception,
    uml_umlTrace_ExpansionNode,
    uml_umlTrace_LiteralNull,
    uml_umlTrace_RaiseExceptionAction,
    uml_umlTrace_Reception,
    uml_umlTrace_Signal,
    uml_umlTrace_ForkNode,
    uml_umlTrace_DestroyObjectAction,
    uml_umlTrace_Comment,
    uml_umlTrace_ObjectFlow,
    TracedActivityEdge,
    umlTrace_uml_TracedControlFlow,
    umlTrace_uml_TracedObjectFlow,
    uml_umlTrace_PackageMerge,
    uml_umlTrace_ChangeEvent,
    uml_umlTrace_Transition,
    uml_umlTrace_LinkEndData,
    uml_umlTrace_TimeExpression,
    uml_umlTrace_Dependency,
    uml_umlTrace_ReadExtentAction,
    uml_umlTrace_InstanceValue,
    uml_umlTrace_Clause,
    uml_umlTrace_ReplyAction,
    uml_umlTrace_UseCase,
    uml_umlTrace_CombinedFragment,
    TracedVertex,
    umlTrace_uml_TracedPseudostate,
    uml_umlTrace_InformationFlow,
    uml_TracedRelationship,
    TracedBehavioredClassifier,
    umlTrace_uml_TracedUseCase,
    TracedActivityNode,
    umlTrace_uml_TracedControlNode,
    uml_umlTrace_Pseudostate,
    uml_umlTrace_InteractionOperand,
    uml_umlTrace_Region,
    TracedState,
    umlTrace_uml_TracedFinalState,
    uml_umlTrace_DestroyLinkAction,
    uml_umlTrace_InterruptibleActivityRegion,
    uml_umlTrace_DecisionNode,
    uml_umlTrace_ValueSpecificationAction,
    uml_umlTrace_InstanceSpecification,
    uml_umlTrace_OutputPin,
    TracedStateMachine,
    umlTrace_uml_TracedProtocolStateMachine,
    uml_umlTrace_ReadIsClassifiedObjectAction,
    TracedPackage,
    umlTrace_uml_TracedModel,
    umlTrace_uml_TracedProfile,
    uml_umlTrace_CallOperationAction,
    uml_umlTrace_Trigger,
    uml_umlTrace_Interval,
    TracedStructuredClassifier,
    umlTrace_uml_TracedEncapsulatedClassifier,
    uml_umlTrace_Image,
    uml_umlTrace_ConnectorEnd,
    uml_TracedEvent,
    TracedInputPin,
    umlTrace_uml_TracedValuePin,
    umlTrace_uml_TracedActionInputPin,
    uml_umlTrace_Parameter,
    uml_umlTrace_ProfileApplication,
    TracedMultiplicityElement,
    umlTrace_uml_TracedConnectorEnd,
    uml_umlTrace_TemplateParameter,
    uml_umlTrace_ClearVariableAction,
    uml_umlTrace_LiteralInteger,
    uml_umlTrace_InitialNode,
    uml_umlTrace_QualifierValue,
    uml_umlTrace_LiteralBoolean,
    uml_umlTrace_Message,
    uml_umlTrace_ReadVariableAction,
    uml_umlTrace_Extend,
    uml_TracedMessageEnd,
    uml_umlTrace_ReadLinkObjectEndQualifierAction,
    uml_umlTrace_TemplateParameterSubstitution,
    uml_umlTrace_CreateLinkAction,
    TracedWriteLinkAction,
    umlTrace_uml_TracedDestroyLinkAction,
    umlTrace_uml_TracedCreateLinkAction,
    TracedInteractionUse,
    umlTrace_uml_TracedPartDecomposition,
    uml_umlTrace_Generalization,
    uml_umlTrace_StructuredActivityNode,
    uml_umlTrace_MergeNode,
    uml_umlTrace_ReadStructuralFeatureAction,
    uml_TracedEncapsulatedClassifier,
    uml_umlTrace_Duration,
    uml_TracedObservation,
    uml_umlTrace_ParameterSet,
    uml_umlTrace_LiteralUnlimitedNatural,
    uml_umlTrace_Class,
    TracedObjectNode,
    umlTrace_uml_TracedExpansionNode,
    umlTrace_uml_TracedActivityParameterNode,
    uml_umlTrace_ActivityParameterNode,
    uml_umlTrace_State,
    uml_TracedBehavioralFeature,
    uml_TracedVertex,
    ecore_umlTrace_EAnnotation,
    umlTrace_ecore_TracedEModelElement,
    uml_umlTrace_CentralBufferNode,
    umlTrace_uml_TracedCentralBufferNode,
    uml_umlTrace_UnmarshallAction,
    TracedArtifact,
    umlTrace_uml_TracedDeploymentSpecification,
    TracedOpaqueBehavior,
    umlTrace_uml_TracedFunctionBehavior,
    uml_umlTrace_OpaqueExpression,
    uml_umlTrace_ClearStructuralFeatureAction,
    uml_umlTrace_TemplateBinding,
    umlTrace_uml_TracedExecutableNode,
    uml_umlTrace_BehaviorExecutionSpecification,
    uml_umlTrace_Actor,
    umlTrace_uml_TracedActor,
    TracedAcceptEventAction,
    umlTrace_uml_TracedAcceptCallAction,
    uml_umlTrace_ReadSelfAction,
    uml_umlTrace_ActionExecutionSpecification,
    TracedExecutionSpecification,
    umlTrace_uml_TracedBehaviorExecutionSpecification,
    umlTrace_uml_TracedActionExecutionSpecification,
    uml_umlTrace_ConnectionPointReference,
    umlTrace_uml_TracedConnectionPointReference,
    uml_umlTrace_CallBehaviorAction,
    uml_umlTrace_GeneralOrdering,
    uml_umlTrace_Gate,
    TracedMessageEnd,
    TracedInterval,
    umlTrace_uml_TracedGate,
    uml_umlTrace_ReclassifyObjectAction,
    umlTrace_uml_TracedTimeInterval,
    uml_umlTrace_RemoveVariableValueAction,
    TracedProperty,
    umlTrace_uml_TracedRemoveVariableValueAction,
    umlTrace_uml_TracedPort,
    uml_umlTrace_LiteralReal,
    uml_TracedStructuredClassifier,
    uml_umlTrace_InformationItem,
    uml_umlTrace_InteractionUse,
    TracedElement,
    umlTrace_uml_TracedTemplateableElement,
    umlTrace_uml_TracedQualifierValue,
    umlTrace_uml_TracedClause,
    umlTrace_uml_TracedImage,
    umlTrace_uml_TracedParameterableElement,
    umlTrace_uml_TracedTemplateParameterSubstitution,
    umlTrace_uml_TracedTemplateParameter,
    umlTrace_uml_TracedLinkEndData,
    umlTrace_uml_TracedComment,
    umlTrace_uml_TracedTemplateSignature,
    uml_umlTrace_StateInvariant,
    uml_umlTrace_Association,
    uml_umlTrace_Collaboration,
    uml_umlTrace_Variable,
    uml_umlTrace_ExceptionHandler,
    TracedCombinedFragment,
    umlTrace_uml_TracedExceptionHandler,
    umlTrace_uml_TracedConsiderIgnoreFragment,
    uml_TracedExecutionSpecification,
    uml_umlTrace_Expression,
    TracedOccurrenceSpecification,
    TracedValueSpecification,
    umlTrace_uml_TracedInterval,
    umlTrace_uml_TracedDuration,
    umlTrace_uml_TracedOpaqueExpression,
    umlTrace_uml_TracedInstanceValue,
    umlTrace_uml_TracedTimeExpression,
    umlTrace_uml_TracedExecutionOccurrenceSpecification,
    umlTrace_uml_TracedExpression,
    uml_umlTrace_PackageImport,
    uml_umlTrace_ReadLinkAction,
    uml_TracedTemplateableElement,
    uml_TracedType,
    uml_TracedRedefinableElement,
    uml_umlTrace_Operation,
    uml_TracedNamespace,
    umlTrace_uml_TracedState,
    umlTrace_uml_TracedTransition,
    umlTrace_uml_TracedRegion,
    umlTrace_uml_TracedClassifier,
    TracedNamedElement,
    umlTrace_uml_TracedTrigger,
    umlTrace_uml_TracedVertex,
    umlTrace_uml_TracedParameterSet,
    umlTrace_uml_TracedDeploymentTarget,
    umlTrace_uml_TracedNamespace,
    umlTrace_uml_TracedGeneralOrdering,
    umlTrace_uml_TracedTypedElement,
    umlTrace_uml_TracedRedefinableElement,
    umlTrace_uml_TracedMessage,
    umlTrace_uml_TracedMessageEnd,
    umlTrace_uml_TracedInteractionFragment,
    uml_umlTrace_FlowFinalNode,
    TracedCentralBufferNode,
    umlTrace_uml_TracedDataStoreNode,
    uml_umlTrace_DurationObservation,
    uml_TracedNamedElement,
    TracedObservation,
    umlTrace_uml_TracedDurationObservation,
    uml_umlTrace_ActivityFinalNode,
    TracedFinalNode,
    umlTrace_uml_TracedFlowFinalNode,
    umlTrace_uml_TracedActivityFinalNode,
    TracedLinkAction,
    umlTrace_uml_TracedWriteLinkAction,
    umlTrace_uml_TracedReadLinkAction,
    uml_umlTrace_AddStructuralFeatureValueAction,
    TracedInstanceSpecification,
    umlTrace_uml_TracedEnumerationLiteral,
    uml_umlTrace_AcceptEventAction,
    uml_TracedDeployedArtifact,
    uml_TracedClassifier,
    umlTrace_uml_TracedAssociation,
    umlTrace_uml_TracedArtifact,
    TracedBehavior,
    umlTrace_uml_TracedActivity,
    umlTrace_uml_TracedOpaqueBehavior,
    uml_umlTrace_SendSignalAction,
    TracedInvocationAction,
    umlTrace_uml_TracedCallAction,
    umlTrace_uml_TracedSendSignalAction,
    uml_umlTrace_RemoveStructuralFeatureValueAction,
    TracedWriteStructuralFeatureAction,
    umlTrace_uml_TracedAddStructuralFeatureValueAction,
    uml_TracedBehavioredClassifier,
    umlTrace_uml_TracedClass,
    umlTrace_uml_TracedCollaboration,
    TracedRealization,
    umlTrace_uml_TracedSubstitution,
    umlTrace_uml_TracedInterfaceRealization,
    TracedIntervalConstraint,
    umlTrace_uml_TracedDurationConstraint,
    umlTrace_uml_TracedTimeConstraint,
    uml_umlTrace_Artifact,
    uml_TracedDeploymentTarget,
    uml_TracedConnectableElement,
    umlTrace_uml_TracedRemoveStructuralFeatureValueAction,
    uml_umlTrace_Continuation,
    TracedInteractionFragment,
    umlTrace_uml_TracedStateInvariant,
    umlTrace_uml_TracedCombinedFragment,
    umlTrace_uml_TracedInteractionUse,
    umlTrace_uml_TracedContinuation,
    uml_umlTrace_Property,
    uml_umlTrace_Connector,
    uml_TracedBehavior,
    TracedFeature,
    umlTrace_uml_TracedConnector,
    uml_TracedMultiplicityElement,
    umlTrace_uml_TracedParameter,
    umlTrace_uml_TracedVariable,
    umlTrace_uml_TracedPin,
    uml_TracedTypedElement,
    uml_TracedFeature,
    umlTrace_uml_TracedBehavioralFeature,
    umlTrace_uml_TracedStructuralFeature,
    umlTrace_Input_TracedInputParameterValues,
    TracedAssociation,
    umlTrace_uml_TracedCommunicationPath,
    uml_umlTrace_DataType,
    TracedClassifier,
    umlTrace_uml_TracedStructuredClassifier,
    umlTrace_uml_TracedSignal,
    umlTrace_uml_TracedInformationItem,
    umlTrace_uml_TracedDataType,
    uml_umlTrace_OpaqueAction,
    TracedAction,
    umlTrace_uml_TracedReadIsClassifiedObjectAction,
    umlTrace_uml_TracedReclassifyObjectAction,
    umlTrace_uml_TracedInvocationAction,
    umlTrace_uml_TracedReplyAction,
    umlTrace_uml_TracedTestIdentityAction,
    umlTrace_uml_TracedLinkAction,
    umlTrace_uml_TracedReadSelfAction,
    umlTrace_uml_TracedDestroyObjectAction,
    umlTrace_uml_TracedClearAssociationAction,
    umlTrace_uml_TracedRaiseExceptionAction,
    umlTrace_uml_TracedReadExtentAction,
    umlTrace_uml_TracedReadLinkObjectEndQualifierAction,
    umlTrace_uml_TracedUnmarshallAction,
    umlTrace_uml_TracedAcceptEventAction,
    umlTrace_uml_TracedValueSpecificationAction,
    umlTrace_uml_TracedOpaqueAction,
    TracedCallActionActivation,
    umlTrace_BasicActions_TracedCallBehaviorActionActivation,
    TracedPinActivation,
    umlTrace_BasicActions_TracedOutputPinActivation,
    TracedWriteStructuralFeatureActionActivation,
    umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation,
    TracedOpaqueBehaviorExecution,
    umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution,
    umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution,
    umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution,
    umlTrace_BasicActions_TracedInputPinActivation,
    TracedInvocationActionActivation,
    umlTrace_BasicActions_TracedCallActionActivation,
    TracedMessageOccurrenceSpecification,
    umlTrace_uml_TracedDestructionOccurrenceSpecification,
    uml_umlTrace_Include,
    uml_TracedDirectedRelationship,
    umlTrace_uml_TracedExtend,
    umlTrace_uml_TracedInclude,
    umlTrace_uml_TracedDurationInterval,
    TracedLinkEndData,
    umlTrace_uml_TracedLinkEndCreationData,
    umlTrace_uml_TracedLinkEndDestructionData,
    umlTrace_uml_TracedVariableAction,
    uml_umlTrace_ActivityPartition,
    uml_TracedActivityGroup,
    ActivityContent,
    umlTrace_uml_TracedActivityGroup,
    umlTrace_uml_TracedActivityNode,
    TracedActivityGroup,
    umlTrace_uml_TracedInterruptibleActivityRegion,
    umlTrace_uml_TracedActivityPartition,
    uml_umlTrace_CollaborationUse,
    umlTrace_uml_TracedCollaborationUse,
    TracedDataType,
    umlTrace_uml_TracedEnumeration,
    umlTrace_uml_TracedPrimitiveType,
    uml_umlTrace_ProtocolConformance,
    TracedCreateLinkAction,
    umlTrace_uml_TracedCreateLinkObjectAction,
    uml_umlTrace_TimeObservation,
    umlTrace_uml_TracedTimeObservation,
    umlTrace_uml_TracedExecutionSpecification,
    uml_umlTrace_Lifeline,
    TracedVariableAction,
    umlTrace_uml_TracedClearVariableAction,
    umlTrace_uml_TracedReadVariableAction,
    umlTrace_uml_TracedWriteVariableAction,
    umlTrace_uml_TracedSendObjectAction,
    umlTrace_uml_TracedRelationship,
    TracedTemplateParameter,
    umlTrace_uml_TracedOperationTemplateParameter,
    umlTrace_uml_TracedClassifierTemplateParameter,
    umlTrace_uml_TracedConnectableElementTemplateParameter,
    uml_umlTrace_CallEvent,
    uml_umlTrace_StartClassifierBehaviorAction,
    umlTrace_uml_TracedLifeline,
    uml_umlTrace_SendObjectAction,
    uml_TracedAction,
    umlTrace_uml_TracedStructuredActivityNode,
    uml_TracedInteractionFragment,
    umlTrace_uml_TracedInteractionOperand,
    umlTrace_uml_TracedInteraction,
    umlTrace_uml_TracedStateMachine,
    umlTrace_uml_TracedExtensionEnd,
    umlTrace_uml_TracedStartClassifierBehaviorAction,
    TracedAbstraction,
    umlTrace_uml_TracedManifestation,
    umlTrace_uml_TracedRealization,
    uml_umlTrace_LiteralString,
    TracedLiteralSpecification,
    umlTrace_uml_TracedLiteralUnlimitedNatural,
    umlTrace_uml_TracedLiteralInteger,
    umlTrace_uml_TracedLiteralReal,
    umlTrace_uml_TracedLiteralBoolean,
    umlTrace_uml_TracedLiteralNull,
    umlTrace_uml_TracedLiteralString,
    umlTrace_uml_TracedNamedElement,
    uml_umlTrace_AnyReceiveEvent,
    uml_umlTrace_ReadLinkObjectEndAction,
    uml_umlTrace_Interface,
    umlTrace_uml_TracedReadLinkObjectEndAction,
    umlTrace_uml_TracedOccurrenceSpecification,
    TracedNode,
    umlTrace_uml_TracedDevice,
    umlTrace_uml_TracedExecutionEnvironment,
    uml_umlTrace_CreateObjectAction,
    umlTrace_uml_TracedCreateObjectAction,
    umlTrace_uml_TracedInterface,
    TracedClass,
    umlTrace_uml_TracedBehavior,
    umlTrace_uml_TracedComponent,
    umlTrace_uml_TracedStereotype,
    umlTrace_uml_TracedDeployedArtifact,
    uml_umlTrace_OccurrenceSpecification,
    uml_umlTrace_ExtensionPoint,
    uml_umlTrace_SignalEvent,
    TracedMessageEvent,
    umlTrace_uml_TracedAnyReceiveEvent,
    umlTrace_uml_TracedCallEvent,
    umlTrace_uml_TracedSignalEvent,
    uml_umlTrace_Slot,
    uml_umlTrace_ElementImport,
    TracedDirectedRelationship,
    umlTrace_uml_TracedPackageImport,
    umlTrace_uml_TracedProfileApplication,
    umlTrace_uml_TracedTemplateBinding,
    umlTrace_uml_TracedProtocolConformance,
    umlTrace_uml_TracedGeneralization,
    umlTrace_uml_TracedPackageMerge,
    umlTrace_uml_TracedElementImport,
    uml_umlTrace_StartObjectBehaviorAction,
    TracedCallAction,
    umlTrace_uml_TracedCallOperationAction,
    umlTrace_uml_TracedCallBehaviorAction,
    umlTrace_uml_TracedStartObjectBehaviorAction,
    uml_umlTrace_JoinNode,
    TracedControlNode,
    umlTrace_uml_TracedForkNode,
    umlTrace_uml_TracedDecisionNode,
    umlTrace_uml_TracedFinalNode,
    umlTrace_uml_TracedMergeNode,
    umlTrace_uml_TracedInitialNode,
    umlTrace_uml_TracedJoinNode,
    TracedEModelElement,
    umlTrace_uml_TracedElement,
    TracedStructuralFeatureAction,
    umlTrace_uml_TracedClearStructuralFeatureAction,
    umlTrace_uml_TracedReadStructuralFeatureAction,
    umlTrace_uml_TracedWriteStructuralFeatureAction,
    umlTrace_uml_TracedSlot,
    umlTrace_uml_TracedComponentRealization,
    umlTrace_uml_TracedReduceAction,
    uml_umlTrace_GeneralizationSet,
    TracedConstraint,
    umlTrace_uml_TracedIntervalConstraint,
    umlTrace_uml_TracedInteractionConstraint,
    TracedRedefinableElement,
    umlTrace_uml_TracedExtensionPoint,
    umlTrace_uml_TracedActivityEdge,
    umlTrace_uml_TracedFeature,
    uml_TracedExecutableNode,
    TracedStructuredActivityNode,
    umlTrace_uml_TracedExpansionRegion,
    umlTrace_uml_TracedConditionalNode,
    umlTrace_uml_TracedLoopNode,
    umlTrace_uml_TracedSequenceNode,
    uml_umlTrace_InputPin,
    TracedPin,
    umlTrace_uml_TracedOutputPin,
    umlTrace_uml_TracedInputPin,
    uml_umlTrace_ReduceAction,
    umlTrace_uml_TracedStructuralFeatureAction,
    umlTrace_uml_TracedBehavioredClassifier,
    uml_umlTrace_Package,
    umlTrace_uml_TracedLiteralSpecification,
    umlTrace_uml_TracedMultiplicityElement,
    uml_umlTrace_Constraint,
    uml_TracedPackageableElement,
    umlTrace_uml_TracedValueSpecification,
    umlTrace_uml_TracedInstanceSpecification,
    umlTrace_uml_TracedInformationFlow,
    umlTrace_uml_TracedDependency,
    umlTrace_uml_TracedPackage,
    TracedTransition,
    umlTrace_uml_TracedProtocolTransition,
    umlTrace_uml_TracedExtension,
    TracedPackageableElement,
    umlTrace_uml_TracedObservation,
    umlTrace_uml_TracedGeneralizationSet,
    umlTrace_uml_TracedEvent,
    umlTrace_uml_TracedConstraint,
    umlTrace_uml_TracedType,
    uml_TracedParameterableElement,
    umlTrace_uml_TracedConnectableElement,
    umlTrace_uml_TracedOperation,
    umlTrace_uml_TracedPackageableElement,
    uml_umlTrace_TimeEvent,
    TracedEvent,
    umlTrace_uml_TracedMessageEvent,
    umlTrace_uml_TracedChangeEvent,
    umlTrace_uml_TracedTimeEvent,
    TracedRelationship,
    umlTrace_uml_TracedDirectedRelationship,
    TracedDependency,
    umlTrace_uml_TracedAbstraction,
    umlTrace_uml_TracedUsage,
    umlTrace_uml_TracedDeployment,
    uml_umlTrace_BroadcastSignalAction,
    umlTrace_uml_TracedBroadcastSignalAction,
    uml_umlTrace_TemplateSignature,
    TracedExecutableNode,
    umlTrace_uml_TracedAction,
    uml_TracedLinkEndDestructionData,
    uml_TracedClassifierTemplateParameter,
    IntermediateActions_TracedAddStructuralFeatureValueActionActivation,
    BasicActions_TracedCallBehaviorActionActivation,
    uml_TracedProtocolConformance,
    uml_TracedLoopNode,
    uml_TracedExpansionRegion,
    uml_TracedActivityPartition,
    uml_TracedCollaborationUse,
    uml_TracedEnumeration,
    uml_TracedLifeline,
    uml_TracedSendObjectAction,
    uml_TracedConnectableElementTemplateParameter,
    uml_TracedCallEvent,
    uml_TracedStartClassifierBehaviorAction,
    uml_TracedRealization,
    uml_TracedCreateLinkObjectAction,
    IntermediateActivities_TracedControlToken,
    uml_TracedTimeObservation,
    uml_TracedExtensionEnd,
    uml_TracedComponent,
    uml_TracedAnyReceiveEvent,
    uml_TracedReadLinkObjectEndAction,
    uml_TracedConditionalNode,
    uml_TracedInterface,
    uml_TracedStereotype,
    uml_TracedLiteralString,
    uml_TracedInteraction,
    IntermediateActivities_TracedMergeNodeActivation,
    uml_TracedStateMachine,
    uml_TracedOccurrenceSpecification,
    umlTrace_uml_TracedMessageOccurrenceSpecification,
    uml_TracedExecutionEnvironment,
    umlTrace_Loci_TracedLocus,
    umlTrace_Loci_TracedExecutionFactory,
    TracedStructuralFeatureActionActivation,
    umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation,
    umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation,
    TracedActionActivation,
    umlTrace_IntermediateActions_TracedCreateObjectActionActivation,
    umlTrace_BasicActions_TracedInvocationActionActivation,
    umlTrace_BasicActions_TracedOpaqueActionActivation,
    umlTrace_IntermediateActions_TracedValueSpecificationActionActivation,
    umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation,
    umlTrace_Loci_TracedExecutionEnvironment,
    umlTrace_Loci_TracedExecutor,
    umlTrace_Loci_TracedSemanticVisitor,
    umlTrace_IntermediateActivities_TracedActivityEdgeInstance,
    TracedObjectNodeActivation,
    umlTrace_BasicActions_TracedPinActivation,
    umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation,
    umlTrace_IntermediateActivities_TracedOffer,
    umlTrace_IntermediateActivities_TracedToken,
    umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup,
    TracedActivityNodeActivation,
    umlTrace_IntermediateActivities_TracedControlNodeActivation,
    umlTrace_BasicActions_TracedActionActivation,
    umlTrace_IntermediateActivities_TracedObjectNodeActivation,
    TracedControlNodeActivation,
    umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation,
    umlTrace_IntermediateActivities_TracedForkNodeActivation,
    umlTrace_IntermediateActivities_TracedInitialNodeActivation,
    umlTrace_IntermediateActivities_TracedJoinNodeActivation,
    TracedToken,
    umlTrace_IntermediateActivities_TracedForkedToken,
    umlTrace_IntermediateActivities_TracedDecisionNodeActivation,
    umlTrace_IntermediateActivities_TracedObjectToken,
    umlTrace_IntermediateActivities_TracedControlToken,
    umlTrace_IntermediateActivities_TracedMergeNodeActivation,
    TracedCompoundValue,
    umlTrace_Kernel_TracedExtensionalValue,
    umlTrace_Kernel_TracedFeatureValue,
    TracedObject,
    umlTrace_BasicBehaviors_TracedExecution,
    umlTrace_BasicBehaviors_TracedParameterValue,
    TracedExecution,
    umlTrace_IntermediateActivities_TracedActivityExecution,
    umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution,
    TracedValue,
    umlTrace_Kernel_TracedPrimitiveValue,
    TracedSemanticVisitor,
    umlTrace_IntermediateActivities_TracedActivityNodeActivation,
    umlTrace_Kernel_TracedValue,
    TracedEvaluation,
    umlTrace_Kernel_TracedLiteralEvaluation,
    TracedPrimitiveValue,
    umlTrace_Kernel_TracedIntegerValue,
    TracedStructuredValue,
    umlTrace_Kernel_TracedCompoundValue,
    umlTrace_Kernel_TracedReference,
    umlTrace_Kernel_TracedStructuredValue,
    TracedLiteralEvaluation,
    umlTrace_Kernel_TracedLiteralIntegerEvaluation,
    umlTrace_Kernel_TracedLiteralBooleanEvaluation,
    umlTrace_Kernel_TracedBooleanValue,
    umlTrace_Kernel_TracedEvaluation,
    uml_TracedBehaviorExecutionSpecification,
    uml_TracedActor,
    uml_TracedDeploymentSpecification,
    TracedExtensionalValue,
    umlTrace_Kernel_TracedObject,
    uml_TracedCentralBufferNode,
    uml_TracedUnmarshallAction,
    Kernel_TracedLiteralIntegerEvaluation,
    uml_TracedClearStructuralFeatureAction,
    uml_TracedFunctionBehavior,
    uml_TracedOpaqueExpression,
    uml_TracedTemplateBinding,
    uml_TracedLinkEndCreationData,
    uml_TracedActionExecutionSpecification,
    uml_TracedConnectionPointReference,
    uml_TracedActivity,
    uml_TracedAcceptCallAction,
    uml_TracedReadSelfAction,
    uml_TracedGate,
    uml_TracedSubstitution,
    uml_TracedDevice,
    uml_TracedReclassifyObjectAction,
    uml_TracedCallBehaviorAction,
    uml_TracedGeneralOrdering,
    uml_TracedStateInvariant,
    uml_TracedAssociation,
    uml_TracedInteractionUse,
    uml_TracedVariable,
    uml_TracedRemoveVariableValueAction,
    uml_TracedLiteralReal,
    uml_TracedExecutionOccurrenceSpecification,
    uml_TracedPackageImport,
    uml_TracedExceptionHandler,
    uml_TracedTestIdentityAction,
    uml_TracedClearAssociationAction,
    uml_TracedAddVariableValueAction,
    uml_TracedOperation,
    uml_TracedControlFlow,
    uml_TracedExpansionNode,
    uml_TracedLiteralNull,
    uml_TracedComment,
    uml_TracedSignal,
    uml_TracedRaiseExceptionAction,
    uml_TracedReception,
    uml_TracedForkNode,
    uml_TracedModel,
    uml_TracedPackageMerge,
    uml_TracedNode,
    uml_TracedDestroyObjectAction,
    uml_TracedChangeEvent,
    uml_TracedObjectFlow,
    BasicActions_TracedInputPinActivation,
    uml_TracedReadExtentAction,
    uml_TracedManifestation,
    uml_TracedLinkEndData,
    uml_TracedTransition,
    uml_TracedInstanceValue,
    uml_TracedClause,
    uml_TracedCombinedFragment,
    IntermediateActions_TracedCreateObjectActionActivation,
    uml_TracedReplyAction,
    uml_TracedTimeExpression,
    uml_TracedDependency,
    uml_TracedInformationFlow,
    uml_TracedInteractionOperand,
    IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution,
    uml_TracedFinalState,
    uml_TracedUseCase,
    uml_TracedPseudostate,
    uml_TracedRegion,
    uml_TracedValueSpecificationAction,
    uml_TracedDecisionNode,
    IntermediateActivities_TracedActivityParameterNodeActivation,
    uml_TracedDestroyLinkAction,
    uml_TracedInterruptibleActivityRegion,
    uml_TracedReadIsClassifiedObjectAction,
    IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution,
    uml_TracedValuePin,
    uml_TracedInstanceSpecification,
    uml_TracedOutputPin,
    uml_TracedProtocolStateMachine,
    IntermediateActivities_TracedForkNodeActivation,
    uml_TracedInterval,
    uml_TracedProfile,
    uml_TracedCallOperationAction,
    uml_TracedTrigger,
    uml_TracedIntervalConstraint,
    uml_TracedImage,
    uml_TracedDurationConstraint,
    uml_TracedMessageOccurrenceSpecification,
    uml_TracedConnectorEnd,
    uml_TracedTemplateParameter,
    uml_TracedActionInputPin,
    uml_TracedClearVariableAction,
    uml_TracedLiteralInteger,
    uml_TracedInitialNode,
    uml_TracedProfileApplication,
    IntermediateActivities_TracedDecisionNodeActivation,
    uml_TracedReadVariableAction,
    uml_TracedExtend,
    uml_TracedTemplateParameterSubstitution,
    uml_TracedReadLinkObjectEndQualifierAction,
    uml_TracedOperationTemplateParameter,
    uml_TracedQualifierValue,
    uml_TracedLiteralBoolean,
    uml_TracedMessage,
    uml_TracedRedefinableTemplateSignature,
    uml_TracedMergeNode,
    uml_TracedReadStructuralFeatureAction,
    Kernel_TracedLiteralBooleanEvaluation,
    BasicActions_TracedOpaqueActionActivation,
    uml_TracedPartDecomposition,
    uml_TracedGeneralization,
    uml_TracedCreateLinkAction,
    uml_TracedUsage,
    uml_TracedDuration,
    uml_TracedParameterSet,
    IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution,
    uml_TracedActivityParameterNode,
    uml_TracedAbstraction,
    uml_TracedStructuredActivityNode,
    uml_TracedLiteralUnlimitedNatural,
    uml_TracedState,
    uml_TracedDestructionOccurrenceSpecification,
    uml_TracedInclude,
    uml_TracedDurationInterval,
    uml_TracedCreateObjectAction,
    uml_TracedElementImport,
    uml_TracedStartObjectBehaviorAction,
    BasicActions_TracedOutputPinActivation,
    IntermediateActions_TracedReadStructuralFeatureActionActivation,
    uml_TracedStringExpression,
    IntermediateActions_TracedValueSpecificationActionActivation,
    uml_TracedAssociationClass,
    uml_TracedComponentRealization,
    uml_TracedInteractionConstraint,
    uml_TracedSequenceNode,
    uml_TracedInputPin,
    uml_TracedReduceAction,
    uml_TracedGeneralizationSet,
    uml_TracedConstraint,
    uml_TracedJoinNode,
    uml_TracedExtensionPoint,
    uml_TracedSignalEvent,
    uml_TracedSlot,
    uml_TracedTimeEvent,
    uml_TracedExtension,
    uml_TracedTimeInterval,
    uml_TracedPort,
    uml_TracedDeployment,
    uml_TracedBroadcastSignalAction,
    uml_TracedTemplateSignature,
    umlTrace_uml_TracedRedefinableTemplateSignature,
    uml_TracedCollaboration,
    uml_TracedPackage,
    IntermediateActivities_TracedActivityFinalNodeActivation,
    uml_TracedProtocolTransition,
    uml_TracedReadLinkAction,
    uml_TracedAddStructuralFeatureValueAction,
    ForkedToken_baseTokenIsWithdrawn_Value,
    ForkedToken_baseToken_Value,
    ForkedToken_remainingOffersCount_Value,
    IntegerValue_value_IntegerValue_Value,
    Reference_referent_Value,
    Object_types_Value,
    BigStep,
    SmallStep,
    SemanticVisitor_runtimeModelElement_Value,
    ObjectNodeActivation_offeredTokenCount_Value,
    Locus_executor_Value,
    Locus_extensionalValues_Value,
    Locus_factory_Value,
    TracedObjects,
    Steps,
    umlTrace_State,
    umlTrace_Trace,
    uml_TracedEnumerationLiteral,
    uml_TracedAcceptEventAction,
    IntermediateActivities_TracedInitialNodeActivation,
    uml_TracedDurationObservation,
    uml_TracedActivityFinalNode,
    uml_TracedInterfaceRealization,
    uml_TracedTimeConstraint,
    IntermediateActivities_TracedJoinNodeActivation,
    uml_TracedInformationItem,
    uml_TracedFlowFinalNode,
    uml_TracedDataStoreNode,
    uml_TracedConsiderIgnoreFragment,
    uml_TracedExpression,
    umlTrace_uml_TracedStringExpression,
    uml_TracedSendSignalAction,
    uml_TracedRemoveStructuralFeatureValueAction,
    uml_TracedContinuation,
    uml_TracedProperty,
    uml_TracedCommunicationPath,
    uml_TracedDataType,
    uml_TracedOpaqueAction,
    uml_TracedConnector,
    umlTrace_Traced_TracedObjects,
    uml_TracedArtifact,
    uml_TracedOpaqueBehavior,
    umlTrace_Values_ActivityExecution_activationGroup_Value,
    umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value,
    umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value,
    Loci_TracedExecutionEnvironment,
    umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value,
    umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value,
    umlTrace_Values_ActivityNodeActivation_isRunning_Value,
    umlTrace_Values_ActivityNodeActivation_incomingEdges_Value,
    umlTrace_Values_ActivityNodeActivation_heldTokens_Value,
    umlTrace_Values_InputParameterValues_parameterValues_Value,
    Input_TracedInputParameterValues,
    umlTrace_Values_InputParameterValues_name_Value,
    umlTrace_Values_ActivityNodeActivation_running_Value,
    uml_TracedActivityNode,
    umlTrace_uml_TracedObjectNode,
    umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value,
    uml_TracedActivityEdge,
    umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value,
    umlTrace_Values_ActivityEdgeInstance_target_Value,
    umlTrace_Values_ActivityEdgeInstance_source_Value,
    umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value,
    umlTrace_Values_PinActivation_count_temp_Value,
    umlTrace_Values_ActivityEdgeInstance_offers_Value,
    umlTrace_Values_FeatureValue_position_Value,
    uml_TracedStructuralFeature,
    umlTrace_uml_TracedProperty,
    umlTrace_Values_FeatureValue_feature_Value,
    umlTrace_Values_FeatureValue_values_FeatureValue_Value,
    umlTrace_Values_PinActivation_actionActivation_Value,
    umlTrace_Values_Token_holder_Value,
    Kernel_TracedCompoundValue,
    Kernel_TracedFeatureValue,
    umlTrace_Values_CompoundValue_featureValues_Value,
    BasicActions_TracedCallActionActivation,
    umlTrace_Values_CallActionActivation_callExecutions_Value,
    IntermediateActivities_TracedOffer,
    umlTrace_Values_Offer_offeredTokens_Value,
    Kernel_TracedBooleanValue,
    umlTrace_Values_BooleanValue_value_BooleanValue_Value,
    umlTrace_Values_Evaluation_locus_Evaluation_Value,
    Kernel_TracedEvaluation,
    uml_TracedValueSpecification,
    umlTrace_Values_Evaluation_specification_Evaluation_Value,
    IntermediateActivities_TracedObjectToken,
    umlTrace_Values_ObjectToken_value_Value,
    umlTrace_Values_Executor_locus_Executor_Value,
    IntermediateActivities_TracedActivityEdgeInstance,
    umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value,
    IntermediateActivities_TracedActivityExecution,
    umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value,
    Kernel_TracedPrimitiveValue,
    umlTrace_Values_PrimitiveValue_type_Value,
    umlTrace_Values_Element_semanticVisitor_Value,
    umlTrace_Values_Execution_context_Value,
    BasicBehaviors_TracedExecution,
    IntermediateActivities_TracedActivityNodeActivationGroup,
    IntermediateActivities_TracedActivityNodeActivation,
    umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value,
    BasicActions_TracedActionActivation,
    BasicActions_TracedPinActivation,
    umlTrace_Values_ActionActivation_pinActivations_Value,
    uml_TracedParameter,
    umlTrace_Values_ParameterValue_parameter_ParameterValue_Value,
    BasicBehaviors_TracedParameterValue,
    Kernel_TracedValue,
    umlTrace_Values_Execution_parameterValues_Value,
    umlTrace_Values_SemanticVisitor_runtimeModelElement_Value,
    umlTrace_Values_ActionActivation_firing_Value,
    IntermediateActivities_TracedObjectNodeActivation,
    umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value,
    Loci_TracedExecutor,
    umlTrace_Values_Locus_executor_Value,
    umlTrace_Values_ParameterValue_values_ParameterValue_Value,
    Loci_TracedSemanticVisitor,
    uml_TracedElement,
    Loci_TracedLocus,
    umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value,
    BasicBehaviors_TracedOpaqueBehaviorExecution,
    umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value,
    Loci_TracedExecutionFactory,
    uml_TracedPrimitiveType,
    umlTrace_Values_ExecutionFactory_builtInTypes_Value,
    Kernel_TracedExtensionalValue,
    umlTrace_Values_Locus_extensionalValues_Value,
    umlTrace_Values_Locus_factory_Value,
    IntermediateActivities_TracedForkedToken,
    umlTrace_Values_ForkedToken_remainingOffersCount_Value,
    Kernel_TracedIntegerValue,
    umlTrace_Values_IntegerValue_value_IntegerValue_Value,
    Kernel_TracedReference,
    umlTrace_Values_Reference_referent_Value,
    umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value,
    IntermediateActivities_TracedToken,
    umlTrace_Values_ForkedToken_baseToken_Value,
    umlTrace_Steps_BigStep,
    umlTrace_Steps_Steps,
    Steps_umlTrace_State,
    umlTrace_Steps_SmallStep,
    ExecutionEnvironment_locus_ExecutionEnvironment_Value,
    ActivityExecution_activationGroup_Value,
    ExtensionalValue_locus_ExtensionalValue_Value,
    ActivityNodeActivation_group_ActivityNodeActivation_Value,
    ActivityNodeActivation_incomingEdges_Value,
    ActivityNodeActivation_outgoingEdges_Value,
    Values_umlTrace_State,
    Kernel_TracedObject,
    uml_TracedClass,
    umlTrace_uml_TracedNode,
    umlTrace_uml_TracedAssociationClass,
    umlTrace_Values_Object_types_Value,
    ActivityNodeActivation_heldTokens_Value,
    InputParameterValues_parameterValues_Value,
    InputParameterValues_name_Value,
    ActivityEdgeInstance_source_Value,
    ActivityEdgeInstance_edge_ActivityEdgeInstance_Value,
    ActivityEdgeInstance_target_Value,
    ActivityEdgeInstance_offers_Value,
    ActivityEdgeInstance_group_ActivityEdgeInstance_Value,
    PinActivation_count_temp_Value,
    ActivityNodeActivation_isRunning_Value,
    ActivityNodeActivation_running_Value,
    ActivityNodeActivation_node_ActivityNodeActivation_Value,
    FeatureValue_values_FeatureValue_Value,
    Offer_offeredTokens_Value,
    Token_holder_Value,
    CompoundValue_featureValues_Value,
    CallActionActivation_callExecutions_Value,
    ObjectToken_value_Value,
    BooleanValue_value_BooleanValue_Value,
    Evaluation_locus_Evaluation_Value,
    Evaluation_specification_Evaluation_Value,
    PinActivation_actionActivation_Value,
    FeatureValue_position_Value,
    FeatureValue_feature_Value,
    ActivityNodeActivationGroup_nodeActivations_Value,
    Element_semanticVisitor_Value,
    Execution_context_Value,
    Execution_parameterValues_Value,
    ActionActivation_firing_Value,
    ActionActivation_pinActivations_Value,
    ParameterValue_parameter_ParameterValue_Value,
    ParameterValue_values_ParameterValue_Value,
    PrimitiveValue_type_Value,
    Executor_locus_Executor_Value,
    ActivityNodeActivationGroup_edgeInstances_Value,
    ActivityNodeActivationGroup_activityExecution_Value,
    ExecutionFactory_locus_ExecutionFactory_Value,
    ExecutionFactory_primitiveBehaviorPrototypes_Value,
    ExecutionFactory_builtInTypes_Value,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uml_umltrace_controlflow_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ControlFlow)


def test_uml_umltrace_controlflow_constructor_exists():
    assert callable(uml_umlTrace_ControlFlow.__init__)


def test_uml_umltrace_controlflow_constructor_args():
    sig = inspect.signature(uml_umlTrace_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_TestIdentityAction)


def test_uml_umltrace_testidentityaction_constructor_exists():
    assert callable(uml_umlTrace_TestIdentityAction.__init__)


def test_uml_umltrace_testidentityaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_AddVariableValueAction)


def test_uml_umltrace_addvariablevalueaction_constructor_exists():
    assert callable(uml_umlTrace_AddVariableValueAction.__init__)


def test_uml_umltrace_addvariablevalueaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedwritevariableaction_is_not_abstract():
    assert not inspect.isabstract(TracedWriteVariableAction)


def test_tracedwritevariableaction_constructor_exists():
    assert callable(TracedWriteVariableAction.__init__)


def test_tracedwritevariableaction_constructor_args():
    sig = inspect.signature(TracedWriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedaddvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAddVariableValueAction)


def test_umltrace_uml_tracedaddvariablevalueaction_constructor_exists():
    assert callable(umlTrace_uml_TracedAddVariableValueAction.__init__)


def test_umltrace_uml_tracedaddvariablevalueaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedobjectnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedObjectNode)


def test_uml_tracedobjectnode_constructor_exists():
    assert callable(uml_TracedObjectNode.__init__)


def test_uml_tracedobjectnode_constructor_args():
    sig = inspect.signature(uml_TracedObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ClearAssociationAction)


def test_uml_umltrace_clearassociationaction_constructor_exists():
    assert callable(uml_umlTrace_ClearAssociationAction.__init__)


def test_uml_umltrace_clearassociationaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ClearAssociationAction.__init__)
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



def test_uml_umltrace_expansionnode_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ExpansionNode)


def test_uml_umltrace_expansionnode_constructor_exists():
    assert callable(uml_umlTrace_ExpansionNode.__init__)


def test_uml_umltrace_expansionnode_constructor_args():
    sig = inspect.signature(uml_umlTrace_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_literalnull_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_LiteralNull)


def test_uml_umltrace_literalnull_constructor_exists():
    assert callable(uml_umlTrace_LiteralNull.__init__)


def test_uml_umltrace_literalnull_constructor_args():
    sig = inspect.signature(uml_umlTrace_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_RaiseExceptionAction)


def test_uml_umltrace_raiseexceptionaction_constructor_exists():
    assert callable(uml_umlTrace_RaiseExceptionAction.__init__)


def test_uml_umltrace_raiseexceptionaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_reception_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Reception)


def test_uml_umltrace_reception_constructor_exists():
    assert callable(uml_umlTrace_Reception.__init__)


def test_uml_umltrace_reception_constructor_args():
    sig = inspect.signature(uml_umlTrace_Reception.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_signal_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Signal)


def test_uml_umltrace_signal_constructor_exists():
    assert callable(uml_umlTrace_Signal.__init__)


def test_uml_umltrace_signal_constructor_args():
    sig = inspect.signature(uml_umlTrace_Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_forknode_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ForkNode)


def test_uml_umltrace_forknode_constructor_exists():
    assert callable(uml_umlTrace_ForkNode.__init__)


def test_uml_umltrace_forknode_constructor_args():
    sig = inspect.signature(uml_umlTrace_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_DestroyObjectAction)


def test_uml_umltrace_destroyobjectaction_constructor_exists():
    assert callable(uml_umlTrace_DestroyObjectAction.__init__)


def test_uml_umltrace_destroyobjectaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_comment_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Comment)


def test_uml_umltrace_comment_constructor_exists():
    assert callable(uml_umlTrace_Comment.__init__)


def test_uml_umltrace_comment_constructor_args():
    sig = inspect.signature(uml_umlTrace_Comment.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_objectflow_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ObjectFlow)


def test_uml_umltrace_objectflow_constructor_exists():
    assert callable(uml_umlTrace_ObjectFlow.__init__)


def test_uml_umltrace_objectflow_constructor_args():
    sig = inspect.signature(uml_umlTrace_ObjectFlow.__init__)
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



def test_uml_umltrace_packagemerge_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_PackageMerge)


def test_uml_umltrace_packagemerge_constructor_exists():
    assert callable(uml_umlTrace_PackageMerge.__init__)


def test_uml_umltrace_packagemerge_constructor_args():
    sig = inspect.signature(uml_umlTrace_PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_changeevent_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ChangeEvent)


def test_uml_umltrace_changeevent_constructor_exists():
    assert callable(uml_umlTrace_ChangeEvent.__init__)


def test_uml_umltrace_changeevent_constructor_args():
    sig = inspect.signature(uml_umlTrace_ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_transition_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Transition)


def test_uml_umltrace_transition_constructor_exists():
    assert callable(uml_umlTrace_Transition.__init__)


def test_uml_umltrace_transition_constructor_args():
    sig = inspect.signature(uml_umlTrace_Transition.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_linkenddata_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_LinkEndData)


def test_uml_umltrace_linkenddata_constructor_exists():
    assert callable(uml_umlTrace_LinkEndData.__init__)


def test_uml_umltrace_linkenddata_constructor_args():
    sig = inspect.signature(uml_umlTrace_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_timeexpression_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_TimeExpression)


def test_uml_umltrace_timeexpression_constructor_exists():
    assert callable(uml_umlTrace_TimeExpression.__init__)


def test_uml_umltrace_timeexpression_constructor_args():
    sig = inspect.signature(uml_umlTrace_TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_dependency_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Dependency)


def test_uml_umltrace_dependency_constructor_exists():
    assert callable(uml_umlTrace_Dependency.__init__)


def test_uml_umltrace_dependency_constructor_args():
    sig = inspect.signature(uml_umlTrace_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_readextentaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ReadExtentAction)


def test_uml_umltrace_readextentaction_constructor_exists():
    assert callable(uml_umlTrace_ReadExtentAction.__init__)


def test_uml_umltrace_readextentaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_instancevalue_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_InstanceValue)


def test_uml_umltrace_instancevalue_constructor_exists():
    assert callable(uml_umlTrace_InstanceValue.__init__)


def test_uml_umltrace_instancevalue_constructor_args():
    sig = inspect.signature(uml_umlTrace_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_clause_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Clause)


def test_uml_umltrace_clause_constructor_exists():
    assert callable(uml_umlTrace_Clause.__init__)


def test_uml_umltrace_clause_constructor_args():
    sig = inspect.signature(uml_umlTrace_Clause.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_replyaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ReplyAction)


def test_uml_umltrace_replyaction_constructor_exists():
    assert callable(uml_umlTrace_ReplyAction.__init__)


def test_uml_umltrace_replyaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_usecase_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_UseCase)


def test_uml_umltrace_usecase_constructor_exists():
    assert callable(uml_umlTrace_UseCase.__init__)


def test_uml_umltrace_usecase_constructor_args():
    sig = inspect.signature(uml_umlTrace_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_CombinedFragment)


def test_uml_umltrace_combinedfragment_constructor_exists():
    assert callable(uml_umlTrace_CombinedFragment.__init__)


def test_uml_umltrace_combinedfragment_constructor_args():
    sig = inspect.signature(uml_umlTrace_CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_tracedvertex_is_not_abstract():
    assert not inspect.isabstract(TracedVertex)


def test_tracedvertex_constructor_exists():
    assert callable(TracedVertex.__init__)


def test_tracedvertex_constructor_args():
    sig = inspect.signature(TracedVertex.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedpseudostate_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPseudostate)


def test_umltrace_uml_tracedpseudostate_constructor_exists():
    assert callable(umlTrace_uml_TracedPseudostate.__init__)


def test_umltrace_uml_tracedpseudostate_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPseudostate.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_informationflow_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_InformationFlow)


def test_uml_umltrace_informationflow_constructor_exists():
    assert callable(uml_umlTrace_InformationFlow.__init__)


def test_uml_umltrace_informationflow_constructor_args():
    sig = inspect.signature(uml_umlTrace_InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedrelationship_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRelationship)


def test_uml_tracedrelationship_constructor_exists():
    assert callable(uml_TracedRelationship.__init__)


def test_uml_tracedrelationship_constructor_args():
    sig = inspect.signature(uml_TracedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_tracedbehavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(TracedBehavioredClassifier)


def test_tracedbehavioredclassifier_constructor_exists():
    assert callable(TracedBehavioredClassifier.__init__)


def test_tracedbehavioredclassifier_constructor_args():
    sig = inspect.signature(TracedBehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedusecase_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedUseCase)


def test_umltrace_uml_tracedusecase_constructor_exists():
    assert callable(umlTrace_uml_TracedUseCase.__init__)


def test_umltrace_uml_tracedusecase_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedUseCase.__init__)
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



def test_uml_umltrace_pseudostate_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Pseudostate)


def test_uml_umltrace_pseudostate_constructor_exists():
    assert callable(uml_umlTrace_Pseudostate.__init__)


def test_uml_umltrace_pseudostate_constructor_args():
    sig = inspect.signature(uml_umlTrace_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_interactionoperand_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_InteractionOperand)


def test_uml_umltrace_interactionoperand_constructor_exists():
    assert callable(uml_umlTrace_InteractionOperand.__init__)


def test_uml_umltrace_interactionoperand_constructor_args():
    sig = inspect.signature(uml_umlTrace_InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_region_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Region)


def test_uml_umltrace_region_constructor_exists():
    assert callable(uml_umlTrace_Region.__init__)


def test_uml_umltrace_region_constructor_args():
    sig = inspect.signature(uml_umlTrace_Region.__init__)
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



def test_uml_umltrace_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_DestroyLinkAction)


def test_uml_umltrace_destroylinkaction_constructor_exists():
    assert callable(uml_umlTrace_DestroyLinkAction.__init__)


def test_uml_umltrace_destroylinkaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_InterruptibleActivityRegion)


def test_uml_umltrace_interruptibleactivityregion_constructor_exists():
    assert callable(uml_umlTrace_InterruptibleActivityRegion.__init__)


def test_uml_umltrace_interruptibleactivityregion_constructor_args():
    sig = inspect.signature(uml_umlTrace_InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_decisionnode_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_DecisionNode)


def test_uml_umltrace_decisionnode_constructor_exists():
    assert callable(uml_umlTrace_DecisionNode.__init__)


def test_uml_umltrace_decisionnode_constructor_args():
    sig = inspect.signature(uml_umlTrace_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ValueSpecificationAction)


def test_uml_umltrace_valuespecificationaction_constructor_exists():
    assert callable(uml_umlTrace_ValueSpecificationAction.__init__)


def test_uml_umltrace_valuespecificationaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_instancespecification_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_InstanceSpecification)


def test_uml_umltrace_instancespecification_constructor_exists():
    assert callable(uml_umlTrace_InstanceSpecification.__init__)


def test_uml_umltrace_instancespecification_constructor_args():
    sig = inspect.signature(uml_umlTrace_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_outputpin_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_OutputPin)


def test_uml_umltrace_outputpin_constructor_exists():
    assert callable(uml_umlTrace_OutputPin.__init__)


def test_uml_umltrace_outputpin_constructor_args():
    sig = inspect.signature(uml_umlTrace_OutputPin.__init__)
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



def test_uml_umltrace_readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ReadIsClassifiedObjectAction)


def test_uml_umltrace_readisclassifiedobjectaction_constructor_exists():
    assert callable(uml_umlTrace_ReadIsClassifiedObjectAction.__init__)


def test_uml_umltrace_readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedpackage_is_not_abstract():
    assert not inspect.isabstract(TracedPackage)


def test_tracedpackage_constructor_exists():
    assert callable(TracedPackage.__init__)


def test_tracedpackage_constructor_args():
    sig = inspect.signature(TracedPackage.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedmodel_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedModel)


def test_umltrace_uml_tracedmodel_constructor_exists():
    assert callable(umlTrace_uml_TracedModel.__init__)


def test_umltrace_uml_tracedmodel_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedModel.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedprofile_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedProfile)


def test_umltrace_uml_tracedprofile_constructor_exists():
    assert callable(umlTrace_uml_TracedProfile.__init__)


def test_umltrace_uml_tracedprofile_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedProfile.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_CallOperationAction)


def test_uml_umltrace_calloperationaction_constructor_exists():
    assert callable(uml_umlTrace_CallOperationAction.__init__)


def test_uml_umltrace_calloperationaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_trigger_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Trigger)


def test_uml_umltrace_trigger_constructor_exists():
    assert callable(uml_umlTrace_Trigger.__init__)


def test_uml_umltrace_trigger_constructor_args():
    sig = inspect.signature(uml_umlTrace_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_interval_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Interval)


def test_uml_umltrace_interval_constructor_exists():
    assert callable(uml_umlTrace_Interval.__init__)


def test_uml_umltrace_interval_constructor_args():
    sig = inspect.signature(uml_umlTrace_Interval.__init__)
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



def test_uml_umltrace_image_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Image)


def test_uml_umltrace_image_constructor_exists():
    assert callable(uml_umlTrace_Image.__init__)


def test_uml_umltrace_image_constructor_args():
    sig = inspect.signature(uml_umlTrace_Image.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_connectorend_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ConnectorEnd)


def test_uml_umltrace_connectorend_constructor_exists():
    assert callable(uml_umlTrace_ConnectorEnd.__init__)


def test_uml_umltrace_connectorend_constructor_args():
    sig = inspect.signature(uml_umlTrace_ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedevent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedEvent)


def test_uml_tracedevent_constructor_exists():
    assert callable(uml_TracedEvent.__init__)


def test_uml_tracedevent_constructor_args():
    sig = inspect.signature(uml_TracedEvent.__init__)
    params = list(sig.parameters.keys())



def test_tracedinputpin_is_not_abstract():
    assert not inspect.isabstract(TracedInputPin)


def test_tracedinputpin_constructor_exists():
    assert callable(TracedInputPin.__init__)


def test_tracedinputpin_constructor_args():
    sig = inspect.signature(TracedInputPin.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedvaluepin_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedValuePin)


def test_umltrace_uml_tracedvaluepin_constructor_exists():
    assert callable(umlTrace_uml_TracedValuePin.__init__)


def test_umltrace_uml_tracedvaluepin_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedValuePin.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactioninputpin_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActionInputPin)


def test_umltrace_uml_tracedactioninputpin_constructor_exists():
    assert callable(umlTrace_uml_TracedActionInputPin.__init__)


def test_umltrace_uml_tracedactioninputpin_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_parameter_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Parameter)


def test_uml_umltrace_parameter_constructor_exists():
    assert callable(uml_umlTrace_Parameter.__init__)


def test_uml_umltrace_parameter_constructor_args():
    sig = inspect.signature(uml_umlTrace_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_profileapplication_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ProfileApplication)


def test_uml_umltrace_profileapplication_constructor_exists():
    assert callable(uml_umlTrace_ProfileApplication.__init__)


def test_uml_umltrace_profileapplication_constructor_args():
    sig = inspect.signature(uml_umlTrace_ProfileApplication.__init__)
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



def test_uml_umltrace_templateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_TemplateParameter)


def test_uml_umltrace_templateparameter_constructor_exists():
    assert callable(uml_umlTrace_TemplateParameter.__init__)


def test_uml_umltrace_templateparameter_constructor_args():
    sig = inspect.signature(uml_umlTrace_TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ClearVariableAction)


def test_uml_umltrace_clearvariableaction_constructor_exists():
    assert callable(uml_umlTrace_ClearVariableAction.__init__)


def test_uml_umltrace_clearvariableaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_literalinteger_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_LiteralInteger)


def test_uml_umltrace_literalinteger_constructor_exists():
    assert callable(uml_umlTrace_LiteralInteger.__init__)


def test_uml_umltrace_literalinteger_constructor_args():
    sig = inspect.signature(uml_umlTrace_LiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_initialnode_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_InitialNode)


def test_uml_umltrace_initialnode_constructor_exists():
    assert callable(uml_umlTrace_InitialNode.__init__)


def test_uml_umltrace_initialnode_constructor_args():
    sig = inspect.signature(uml_umlTrace_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_QualifierValue)


def test_uml_umltrace_qualifiervalue_constructor_exists():
    assert callable(uml_umlTrace_QualifierValue.__init__)


def test_uml_umltrace_qualifiervalue_constructor_args():
    sig = inspect.signature(uml_umlTrace_QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_literalboolean_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_LiteralBoolean)


def test_uml_umltrace_literalboolean_constructor_exists():
    assert callable(uml_umlTrace_LiteralBoolean.__init__)


def test_uml_umltrace_literalboolean_constructor_args():
    sig = inspect.signature(uml_umlTrace_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_message_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Message)


def test_uml_umltrace_message_constructor_exists():
    assert callable(uml_umlTrace_Message.__init__)


def test_uml_umltrace_message_constructor_args():
    sig = inspect.signature(uml_umlTrace_Message.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_readvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ReadVariableAction)


def test_uml_umltrace_readvariableaction_constructor_exists():
    assert callable(uml_umlTrace_ReadVariableAction.__init__)


def test_uml_umltrace_readvariableaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_extend_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Extend)


def test_uml_umltrace_extend_constructor_exists():
    assert callable(uml_umlTrace_Extend.__init__)


def test_uml_umltrace_extend_constructor_args():
    sig = inspect.signature(uml_umlTrace_Extend.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmessageend_is_not_abstract():
    assert not inspect.isabstract(uml_TracedMessageEnd)


def test_uml_tracedmessageend_constructor_exists():
    assert callable(uml_TracedMessageEnd.__init__)


def test_uml_tracedmessageend_constructor_args():
    sig = inspect.signature(uml_TracedMessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ReadLinkObjectEndQualifierAction)


def test_uml_umltrace_readlinkobjectendqualifieraction_constructor_exists():
    assert callable(uml_umlTrace_ReadLinkObjectEndQualifierAction.__init__)


def test_uml_umltrace_readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_TemplateParameterSubstitution)


def test_uml_umltrace_templateparametersubstitution_constructor_exists():
    assert callable(uml_umlTrace_TemplateParameterSubstitution.__init__)


def test_uml_umltrace_templateparametersubstitution_constructor_args():
    sig = inspect.signature(uml_umlTrace_TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_CreateLinkAction)


def test_uml_umltrace_createlinkaction_constructor_exists():
    assert callable(uml_umlTrace_CreateLinkAction.__init__)


def test_uml_umltrace_createlinkaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_CreateLinkAction.__init__)
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



def test_uml_umltrace_generalization_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Generalization)


def test_uml_umltrace_generalization_constructor_exists():
    assert callable(uml_umlTrace_Generalization.__init__)


def test_uml_umltrace_generalization_constructor_args():
    sig = inspect.signature(uml_umlTrace_Generalization.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_StructuredActivityNode)


def test_uml_umltrace_structuredactivitynode_constructor_exists():
    assert callable(uml_umlTrace_StructuredActivityNode.__init__)


def test_uml_umltrace_structuredactivitynode_constructor_args():
    sig = inspect.signature(uml_umlTrace_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_mergenode_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_MergeNode)


def test_uml_umltrace_mergenode_constructor_exists():
    assert callable(uml_umlTrace_MergeNode.__init__)


def test_uml_umltrace_mergenode_constructor_args():
    sig = inspect.signature(uml_umlTrace_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ReadStructuralFeatureAction)


def test_uml_umltrace_readstructuralfeatureaction_constructor_exists():
    assert callable(uml_umlTrace_ReadStructuralFeatureAction.__init__)


def test_uml_umltrace_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedencapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_TracedEncapsulatedClassifier)


def test_uml_tracedencapsulatedclassifier_constructor_exists():
    assert callable(uml_TracedEncapsulatedClassifier.__init__)


def test_uml_tracedencapsulatedclassifier_constructor_args():
    sig = inspect.signature(uml_TracedEncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_duration_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Duration)


def test_uml_umltrace_duration_constructor_exists():
    assert callable(uml_umlTrace_Duration.__init__)


def test_uml_umltrace_duration_constructor_args():
    sig = inspect.signature(uml_umlTrace_Duration.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedobservation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedObservation)


def test_uml_tracedobservation_constructor_exists():
    assert callable(uml_TracedObservation.__init__)


def test_uml_tracedobservation_constructor_args():
    sig = inspect.signature(uml_TracedObservation.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_parameterset_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ParameterSet)


def test_uml_umltrace_parameterset_constructor_exists():
    assert callable(uml_umlTrace_ParameterSet.__init__)


def test_uml_umltrace_parameterset_constructor_args():
    sig = inspect.signature(uml_umlTrace_ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_LiteralUnlimitedNatural)


def test_uml_umltrace_literalunlimitednatural_constructor_exists():
    assert callable(uml_umlTrace_LiteralUnlimitedNatural.__init__)


def test_uml_umltrace_literalunlimitednatural_constructor_args():
    sig = inspect.signature(uml_umlTrace_LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_class_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Class)


def test_uml_umltrace_class_constructor_exists():
    assert callable(uml_umlTrace_Class.__init__)


def test_uml_umltrace_class_constructor_args():
    sig = inspect.signature(uml_umlTrace_Class.__init__)
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



def test_uml_umltrace_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ActivityParameterNode)


def test_uml_umltrace_activityparameternode_constructor_exists():
    assert callable(uml_umlTrace_ActivityParameterNode.__init__)


def test_uml_umltrace_activityparameternode_constructor_args():
    sig = inspect.signature(uml_umlTrace_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_state_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_State)


def test_uml_umltrace_state_constructor_exists():
    assert callable(uml_umlTrace_State.__init__)


def test_uml_umltrace_state_constructor_args():
    sig = inspect.signature(uml_umlTrace_State.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedbehavioralfeature_is_not_abstract():
    assert not inspect.isabstract(uml_TracedBehavioralFeature)


def test_uml_tracedbehavioralfeature_constructor_exists():
    assert callable(uml_TracedBehavioralFeature.__init__)


def test_uml_tracedbehavioralfeature_constructor_args():
    sig = inspect.signature(uml_TracedBehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedvertex_is_not_abstract():
    assert not inspect.isabstract(uml_TracedVertex)


def test_uml_tracedvertex_constructor_exists():
    assert callable(uml_TracedVertex.__init__)


def test_uml_tracedvertex_constructor_args():
    sig = inspect.signature(uml_TracedVertex.__init__)
    params = list(sig.parameters.keys())



def test_ecore_umltrace_eannotation_is_not_abstract():
    assert not inspect.isabstract(ecore_umlTrace_EAnnotation)


def test_ecore_umltrace_eannotation_constructor_exists():
    assert callable(ecore_umlTrace_EAnnotation.__init__)


def test_ecore_umltrace_eannotation_constructor_args():
    sig = inspect.signature(ecore_umlTrace_EAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_ecore_tracedemodelelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_ecore_TracedEModelElement)


def test_umltrace_ecore_tracedemodelelement_constructor_exists():
    assert callable(umlTrace_ecore_TracedEModelElement.__init__)


def test_umltrace_ecore_tracedemodelelement_constructor_args():
    sig = inspect.signature(umlTrace_ecore_TracedEModelElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_CentralBufferNode)


def test_uml_umltrace_centralbuffernode_constructor_exists():
    assert callable(uml_umlTrace_CentralBufferNode.__init__)


def test_uml_umltrace_centralbuffernode_constructor_args():
    sig = inspect.signature(uml_umlTrace_CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcentralbuffernode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCentralBufferNode)


def test_umltrace_uml_tracedcentralbuffernode_constructor_exists():
    assert callable(umlTrace_uml_TracedCentralBufferNode.__init__)


def test_umltrace_uml_tracedcentralbuffernode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_UnmarshallAction)


def test_uml_umltrace_unmarshallaction_constructor_exists():
    assert callable(uml_umlTrace_UnmarshallAction.__init__)


def test_uml_umltrace_unmarshallaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_UnmarshallAction.__init__)
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



def test_uml_umltrace_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_OpaqueExpression)


def test_uml_umltrace_opaqueexpression_constructor_exists():
    assert callable(uml_umlTrace_OpaqueExpression.__init__)


def test_uml_umltrace_opaqueexpression_constructor_args():
    sig = inspect.signature(uml_umlTrace_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ClearStructuralFeatureAction)


def test_uml_umltrace_clearstructuralfeatureaction_constructor_exists():
    assert callable(uml_umlTrace_ClearStructuralFeatureAction.__init__)


def test_uml_umltrace_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_templatebinding_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_TemplateBinding)


def test_uml_umltrace_templatebinding_constructor_exists():
    assert callable(uml_umlTrace_TemplateBinding.__init__)


def test_uml_umltrace_templatebinding_constructor_args():
    sig = inspect.signature(uml_umlTrace_TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexecutablenode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExecutableNode)


def test_umltrace_uml_tracedexecutablenode_constructor_exists():
    assert callable(umlTrace_uml_TracedExecutableNode.__init__)


def test_umltrace_uml_tracedexecutablenode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_behaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_BehaviorExecutionSpecification)


def test_uml_umltrace_behaviorexecutionspecification_constructor_exists():
    assert callable(uml_umlTrace_BehaviorExecutionSpecification.__init__)


def test_uml_umltrace_behaviorexecutionspecification_constructor_args():
    sig = inspect.signature(uml_umlTrace_BehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_actor_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Actor)


def test_uml_umltrace_actor_constructor_exists():
    assert callable(uml_umlTrace_Actor.__init__)


def test_uml_umltrace_actor_constructor_args():
    sig = inspect.signature(uml_umlTrace_Actor.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactor_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActor)


def test_umltrace_uml_tracedactor_constructor_exists():
    assert callable(umlTrace_uml_TracedActor.__init__)


def test_umltrace_uml_tracedactor_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActor.__init__)
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



def test_uml_umltrace_readselfaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ReadSelfAction)


def test_uml_umltrace_readselfaction_constructor_exists():
    assert callable(uml_umlTrace_ReadSelfAction.__init__)


def test_uml_umltrace_readselfaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_actionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ActionExecutionSpecification)


def test_uml_umltrace_actionexecutionspecification_constructor_exists():
    assert callable(uml_umlTrace_ActionExecutionSpecification.__init__)


def test_uml_umltrace_actionexecutionspecification_constructor_args():
    sig = inspect.signature(uml_umlTrace_ActionExecutionSpecification.__init__)
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



def test_umltrace_uml_tracedactionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActionExecutionSpecification)


def test_umltrace_uml_tracedactionexecutionspecification_constructor_exists():
    assert callable(umlTrace_uml_TracedActionExecutionSpecification.__init__)


def test_umltrace_uml_tracedactionexecutionspecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ConnectionPointReference)


def test_uml_umltrace_connectionpointreference_constructor_exists():
    assert callable(uml_umlTrace_ConnectionPointReference.__init__)


def test_uml_umltrace_connectionpointreference_constructor_args():
    sig = inspect.signature(uml_umlTrace_ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconnectionpointreference_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConnectionPointReference)


def test_umltrace_uml_tracedconnectionpointreference_constructor_exists():
    assert callable(umlTrace_uml_TracedConnectionPointReference.__init__)


def test_umltrace_uml_tracedconnectionpointreference_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_CallBehaviorAction)


def test_uml_umltrace_callbehavioraction_constructor_exists():
    assert callable(uml_umlTrace_CallBehaviorAction.__init__)


def test_uml_umltrace_callbehavioraction_constructor_args():
    sig = inspect.signature(uml_umlTrace_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_generalordering_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_GeneralOrdering)


def test_uml_umltrace_generalordering_constructor_exists():
    assert callable(uml_umlTrace_GeneralOrdering.__init__)


def test_uml_umltrace_generalordering_constructor_args():
    sig = inspect.signature(uml_umlTrace_GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_gate_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Gate)


def test_uml_umltrace_gate_constructor_exists():
    assert callable(uml_umlTrace_Gate.__init__)


def test_uml_umltrace_gate_constructor_args():
    sig = inspect.signature(uml_umlTrace_Gate.__init__)
    params = list(sig.parameters.keys())



def test_tracedmessageend_is_not_abstract():
    assert not inspect.isabstract(TracedMessageEnd)


def test_tracedmessageend_constructor_exists():
    assert callable(TracedMessageEnd.__init__)


def test_tracedmessageend_constructor_args():
    sig = inspect.signature(TracedMessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_tracedinterval_is_not_abstract():
    assert not inspect.isabstract(TracedInterval)


def test_tracedinterval_constructor_exists():
    assert callable(TracedInterval.__init__)


def test_tracedinterval_constructor_args():
    sig = inspect.signature(TracedInterval.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedgate_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedGate)


def test_umltrace_uml_tracedgate_constructor_exists():
    assert callable(umlTrace_uml_TracedGate.__init__)


def test_umltrace_uml_tracedgate_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedGate.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ReclassifyObjectAction)


def test_uml_umltrace_reclassifyobjectaction_constructor_exists():
    assert callable(uml_umlTrace_ReclassifyObjectAction.__init__)


def test_uml_umltrace_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtimeinterval_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTimeInterval)


def test_umltrace_uml_tracedtimeinterval_constructor_exists():
    assert callable(umlTrace_uml_TracedTimeInterval.__init__)


def test_umltrace_uml_tracedtimeinterval_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_RemoveVariableValueAction)


def test_uml_umltrace_removevariablevalueaction_constructor_exists():
    assert callable(uml_umlTrace_RemoveVariableValueAction.__init__)


def test_uml_umltrace_removevariablevalueaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedproperty_is_not_abstract():
    assert not inspect.isabstract(TracedProperty)


def test_tracedproperty_constructor_exists():
    assert callable(TracedProperty.__init__)


def test_tracedproperty_constructor_args():
    sig = inspect.signature(TracedProperty.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedremovevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRemoveVariableValueAction)


def test_umltrace_uml_tracedremovevariablevalueaction_constructor_exists():
    assert callable(umlTrace_uml_TracedRemoveVariableValueAction.__init__)


def test_umltrace_uml_tracedremovevariablevalueaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedport_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPort)


def test_umltrace_uml_tracedport_constructor_exists():
    assert callable(umlTrace_uml_TracedPort.__init__)


def test_umltrace_uml_tracedport_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPort.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_literalreal_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_LiteralReal)


def test_uml_umltrace_literalreal_constructor_exists():
    assert callable(uml_umlTrace_LiteralReal.__init__)


def test_uml_umltrace_literalreal_constructor_args():
    sig = inspect.signature(uml_umlTrace_LiteralReal.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstructuredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStructuredClassifier)


def test_uml_tracedstructuredclassifier_constructor_exists():
    assert callable(uml_TracedStructuredClassifier.__init__)


def test_uml_tracedstructuredclassifier_constructor_args():
    sig = inspect.signature(uml_TracedStructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_informationitem_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_InformationItem)


def test_uml_umltrace_informationitem_constructor_exists():
    assert callable(uml_umlTrace_InformationItem.__init__)


def test_uml_umltrace_informationitem_constructor_args():
    sig = inspect.signature(uml_umlTrace_InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_interactionuse_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_InteractionUse)


def test_uml_umltrace_interactionuse_constructor_exists():
    assert callable(uml_umlTrace_InteractionUse.__init__)


def test_uml_umltrace_interactionuse_constructor_args():
    sig = inspect.signature(uml_umlTrace_InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_tracedelement_is_not_abstract():
    assert not inspect.isabstract(TracedElement)


def test_tracedelement_constructor_exists():
    assert callable(TracedElement.__init__)


def test_tracedelement_constructor_args():
    sig = inspect.signature(TracedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtemplateableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTemplateableElement)


def test_umltrace_uml_tracedtemplateableelement_constructor_exists():
    assert callable(umlTrace_uml_TracedTemplateableElement.__init__)


def test_umltrace_uml_tracedtemplateableelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedqualifiervalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedQualifierValue)


def test_umltrace_uml_tracedqualifiervalue_constructor_exists():
    assert callable(umlTrace_uml_TracedQualifierValue.__init__)


def test_umltrace_uml_tracedqualifiervalue_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedQualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclause_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClause)


def test_umltrace_uml_tracedclause_constructor_exists():
    assert callable(umlTrace_uml_TracedClause.__init__)


def test_umltrace_uml_tracedclause_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClause.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedimage_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedImage)


def test_umltrace_uml_tracedimage_constructor_exists():
    assert callable(umlTrace_uml_TracedImage.__init__)


def test_umltrace_uml_tracedimage_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedImage.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedparameterableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedParameterableElement)


def test_umltrace_uml_tracedparameterableelement_constructor_exists():
    assert callable(umlTrace_uml_TracedParameterableElement.__init__)


def test_umltrace_uml_tracedparameterableelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtemplateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTemplateParameterSubstitution)


def test_umltrace_uml_tracedtemplateparametersubstitution_constructor_exists():
    assert callable(umlTrace_uml_TracedTemplateParameterSubstitution.__init__)


def test_umltrace_uml_tracedtemplateparametersubstitution_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTemplateParameter)


def test_umltrace_uml_tracedtemplateparameter_constructor_exists():
    assert callable(umlTrace_uml_TracedTemplateParameter.__init__)


def test_umltrace_uml_tracedtemplateparameter_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedlinkenddata_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLinkEndData)


def test_umltrace_uml_tracedlinkenddata_constructor_exists():
    assert callable(umlTrace_uml_TracedLinkEndData.__init__)


def test_umltrace_uml_tracedlinkenddata_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcomment_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedComment)


def test_umltrace_uml_tracedcomment_constructor_exists():
    assert callable(umlTrace_uml_TracedComment.__init__)


def test_umltrace_uml_tracedcomment_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedComment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtemplatesignature_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTemplateSignature)


def test_umltrace_uml_tracedtemplatesignature_constructor_exists():
    assert callable(umlTrace_uml_TracedTemplateSignature.__init__)


def test_umltrace_uml_tracedtemplatesignature_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_stateinvariant_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_StateInvariant)


def test_uml_umltrace_stateinvariant_constructor_exists():
    assert callable(uml_umlTrace_StateInvariant.__init__)


def test_uml_umltrace_stateinvariant_constructor_args():
    sig = inspect.signature(uml_umlTrace_StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_association_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Association)


def test_uml_umltrace_association_constructor_exists():
    assert callable(uml_umlTrace_Association.__init__)


def test_uml_umltrace_association_constructor_args():
    sig = inspect.signature(uml_umlTrace_Association.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_collaboration_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Collaboration)


def test_uml_umltrace_collaboration_constructor_exists():
    assert callable(uml_umlTrace_Collaboration.__init__)


def test_uml_umltrace_collaboration_constructor_args():
    sig = inspect.signature(uml_umlTrace_Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_variable_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Variable)


def test_uml_umltrace_variable_constructor_exists():
    assert callable(uml_umlTrace_Variable.__init__)


def test_uml_umltrace_variable_constructor_args():
    sig = inspect.signature(uml_umlTrace_Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ExceptionHandler)


def test_uml_umltrace_exceptionhandler_constructor_exists():
    assert callable(uml_umlTrace_ExceptionHandler.__init__)


def test_uml_umltrace_exceptionhandler_constructor_args():
    sig = inspect.signature(uml_umlTrace_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_tracedcombinedfragment_is_not_abstract():
    assert not inspect.isabstract(TracedCombinedFragment)


def test_tracedcombinedfragment_constructor_exists():
    assert callable(TracedCombinedFragment.__init__)


def test_tracedcombinedfragment_constructor_args():
    sig = inspect.signature(TracedCombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexceptionhandler_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExceptionHandler)


def test_umltrace_uml_tracedexceptionhandler_constructor_exists():
    assert callable(umlTrace_uml_TracedExceptionHandler.__init__)


def test_umltrace_uml_tracedexceptionhandler_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconsiderignorefragment_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConsiderIgnoreFragment)


def test_umltrace_uml_tracedconsiderignorefragment_constructor_exists():
    assert callable(umlTrace_uml_TracedConsiderIgnoreFragment.__init__)


def test_umltrace_uml_tracedconsiderignorefragment_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExecutionSpecification)


def test_uml_tracedexecutionspecification_constructor_exists():
    assert callable(uml_TracedExecutionSpecification.__init__)


def test_uml_tracedexecutionspecification_constructor_args():
    sig = inspect.signature(uml_TracedExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_expression_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Expression)


def test_uml_umltrace_expression_constructor_exists():
    assert callable(uml_umlTrace_Expression.__init__)


def test_uml_umltrace_expression_constructor_args():
    sig = inspect.signature(uml_umlTrace_Expression.__init__)
    params = list(sig.parameters.keys())



def test_tracedoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(TracedOccurrenceSpecification)


def test_tracedoccurrencespecification_constructor_exists():
    assert callable(TracedOccurrenceSpecification.__init__)


def test_tracedoccurrencespecification_constructor_args():
    sig = inspect.signature(TracedOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_tracedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(TracedValueSpecification)


def test_tracedvaluespecification_constructor_exists():
    assert callable(TracedValueSpecification.__init__)


def test_tracedvaluespecification_constructor_args():
    sig = inspect.signature(TracedValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinterval_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInterval)


def test_umltrace_uml_tracedinterval_constructor_exists():
    assert callable(umlTrace_uml_TracedInterval.__init__)


def test_umltrace_uml_tracedinterval_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInterval.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedduration_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDuration)


def test_umltrace_uml_tracedduration_constructor_exists():
    assert callable(umlTrace_uml_TracedDuration.__init__)


def test_umltrace_uml_tracedduration_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDuration.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedopaqueexpression_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOpaqueExpression)


def test_umltrace_uml_tracedopaqueexpression_constructor_exists():
    assert callable(umlTrace_uml_TracedOpaqueExpression.__init__)


def test_umltrace_uml_tracedopaqueexpression_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinstancevalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInstanceValue)


def test_umltrace_uml_tracedinstancevalue_constructor_exists():
    assert callable(umlTrace_uml_TracedInstanceValue.__init__)


def test_umltrace_uml_tracedinstancevalue_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtimeexpression_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTimeExpression)


def test_umltrace_uml_tracedtimeexpression_constructor_exists():
    assert callable(umlTrace_uml_TracedTimeExpression.__init__)


def test_umltrace_uml_tracedtimeexpression_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexecutionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExecutionOccurrenceSpecification)


def test_umltrace_uml_tracedexecutionoccurrencespecification_constructor_exists():
    assert callable(umlTrace_uml_TracedExecutionOccurrenceSpecification.__init__)


def test_umltrace_uml_tracedexecutionoccurrencespecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexpression_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExpression)


def test_umltrace_uml_tracedexpression_constructor_exists():
    assert callable(umlTrace_uml_TracedExpression.__init__)


def test_umltrace_uml_tracedexpression_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_packageimport_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_PackageImport)


def test_uml_umltrace_packageimport_constructor_exists():
    assert callable(uml_umlTrace_PackageImport.__init__)


def test_uml_umltrace_packageimport_constructor_args():
    sig = inspect.signature(uml_umlTrace_PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ReadLinkAction)


def test_uml_umltrace_readlinkaction_constructor_exists():
    assert callable(uml_umlTrace_ReadLinkAction.__init__)


def test_uml_umltrace_readlinkaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtemplateableelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTemplateableElement)


def test_uml_tracedtemplateableelement_constructor_exists():
    assert callable(uml_TracedTemplateableElement.__init__)


def test_uml_tracedtemplateableelement_constructor_args():
    sig = inspect.signature(uml_TracedTemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtype_is_not_abstract():
    assert not inspect.isabstract(uml_TracedType)


def test_uml_tracedtype_constructor_exists():
    assert callable(uml_TracedType.__init__)


def test_uml_tracedtype_constructor_args():
    sig = inspect.signature(uml_TracedType.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedredefinableelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRedefinableElement)


def test_uml_tracedredefinableelement_constructor_exists():
    assert callable(uml_TracedRedefinableElement.__init__)


def test_uml_tracedredefinableelement_constructor_args():
    sig = inspect.signature(uml_TracedRedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_operation_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Operation)


def test_uml_umltrace_operation_constructor_exists():
    assert callable(uml_umlTrace_Operation.__init__)


def test_uml_umltrace_operation_constructor_args():
    sig = inspect.signature(uml_umlTrace_Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracednamespace_is_not_abstract():
    assert not inspect.isabstract(uml_TracedNamespace)


def test_uml_tracednamespace_constructor_exists():
    assert callable(uml_TracedNamespace.__init__)


def test_uml_tracednamespace_constructor_args():
    sig = inspect.signature(uml_TracedNamespace.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstate_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedState)


def test_umltrace_uml_tracedstate_constructor_exists():
    assert callable(umlTrace_uml_TracedState.__init__)


def test_umltrace_uml_tracedstate_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedState.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtransition_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTransition)


def test_umltrace_uml_tracedtransition_constructor_exists():
    assert callable(umlTrace_uml_TracedTransition.__init__)


def test_umltrace_uml_tracedtransition_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTransition.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedregion_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRegion)


def test_umltrace_uml_tracedregion_constructor_exists():
    assert callable(umlTrace_uml_TracedRegion.__init__)


def test_umltrace_uml_tracedregion_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRegion.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclassifier_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClassifier)


def test_umltrace_uml_tracedclassifier_constructor_exists():
    assert callable(umlTrace_uml_TracedClassifier.__init__)


def test_umltrace_uml_tracedclassifier_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(TracedNamedElement)


def test_tracednamedelement_constructor_exists():
    assert callable(TracedNamedElement.__init__)


def test_tracednamedelement_constructor_args():
    sig = inspect.signature(TracedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtrigger_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTrigger)


def test_umltrace_uml_tracedtrigger_constructor_exists():
    assert callable(umlTrace_uml_TracedTrigger.__init__)


def test_umltrace_uml_tracedtrigger_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTrigger.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedvertex_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedVertex)


def test_umltrace_uml_tracedvertex_constructor_exists():
    assert callable(umlTrace_uml_TracedVertex.__init__)


def test_umltrace_uml_tracedvertex_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedVertex.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedparameterset_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedParameterSet)


def test_umltrace_uml_tracedparameterset_constructor_exists():
    assert callable(umlTrace_uml_TracedParameterSet.__init__)


def test_umltrace_uml_tracedparameterset_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddeploymenttarget_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDeploymentTarget)


def test_umltrace_uml_traceddeploymenttarget_constructor_exists():
    assert callable(umlTrace_uml_TracedDeploymentTarget.__init__)


def test_umltrace_uml_traceddeploymenttarget_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracednamespace_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedNamespace)


def test_umltrace_uml_tracednamespace_constructor_exists():
    assert callable(umlTrace_uml_TracedNamespace.__init__)


def test_umltrace_uml_tracednamespace_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedNamespace.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedgeneralordering_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedGeneralOrdering)


def test_umltrace_uml_tracedgeneralordering_constructor_exists():
    assert callable(umlTrace_uml_TracedGeneralOrdering.__init__)


def test_umltrace_uml_tracedgeneralordering_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedGeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtypedelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTypedElement)


def test_umltrace_uml_tracedtypedelement_constructor_exists():
    assert callable(umlTrace_uml_TracedTypedElement.__init__)


def test_umltrace_uml_tracedtypedelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedredefinableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRedefinableElement)


def test_umltrace_uml_tracedredefinableelement_constructor_exists():
    assert callable(umlTrace_uml_TracedRedefinableElement.__init__)


def test_umltrace_uml_tracedredefinableelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedmessage_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedMessage)


def test_umltrace_uml_tracedmessage_constructor_exists():
    assert callable(umlTrace_uml_TracedMessage.__init__)


def test_umltrace_uml_tracedmessage_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedMessage.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedmessageend_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedMessageEnd)


def test_umltrace_uml_tracedmessageend_constructor_exists():
    assert callable(umlTrace_uml_TracedMessageEnd.__init__)


def test_umltrace_uml_tracedmessageend_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedMessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinteractionfragment_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInteractionFragment)


def test_umltrace_uml_tracedinteractionfragment_constructor_exists():
    assert callable(umlTrace_uml_TracedInteractionFragment.__init__)


def test_umltrace_uml_tracedinteractionfragment_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_FlowFinalNode)


def test_uml_umltrace_flowfinalnode_constructor_exists():
    assert callable(uml_umlTrace_FlowFinalNode.__init__)


def test_uml_umltrace_flowfinalnode_constructor_args():
    sig = inspect.signature(uml_umlTrace_FlowFinalNode.__init__)
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



def test_uml_umltrace_durationobservation_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_DurationObservation)


def test_uml_umltrace_durationobservation_constructor_exists():
    assert callable(uml_umlTrace_DurationObservation.__init__)


def test_uml_umltrace_durationobservation_constructor_args():
    sig = inspect.signature(uml_umlTrace_DurationObservation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedNamedElement)


def test_uml_tracednamedelement_constructor_exists():
    assert callable(uml_TracedNamedElement.__init__)


def test_uml_tracednamedelement_constructor_args():
    sig = inspect.signature(uml_TracedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tracedobservation_is_not_abstract():
    assert not inspect.isabstract(TracedObservation)


def test_tracedobservation_constructor_exists():
    assert callable(TracedObservation.__init__)


def test_tracedobservation_constructor_args():
    sig = inspect.signature(TracedObservation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddurationobservation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDurationObservation)


def test_umltrace_uml_traceddurationobservation_constructor_exists():
    assert callable(umlTrace_uml_TracedDurationObservation.__init__)


def test_umltrace_uml_traceddurationobservation_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDurationObservation.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ActivityFinalNode)


def test_uml_umltrace_activityfinalnode_constructor_exists():
    assert callable(uml_umlTrace_ActivityFinalNode.__init__)


def test_uml_umltrace_activityfinalnode_constructor_args():
    sig = inspect.signature(uml_umlTrace_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedfinalnode_is_not_abstract():
    assert not inspect.isabstract(TracedFinalNode)


def test_tracedfinalnode_constructor_exists():
    assert callable(TracedFinalNode.__init__)


def test_tracedfinalnode_constructor_args():
    sig = inspect.signature(TracedFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedflowfinalnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedFlowFinalNode)


def test_umltrace_uml_tracedflowfinalnode_constructor_exists():
    assert callable(umlTrace_uml_TracedFlowFinalNode.__init__)


def test_umltrace_uml_tracedflowfinalnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedFlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactivityfinalnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActivityFinalNode)


def test_umltrace_uml_tracedactivityfinalnode_constructor_exists():
    assert callable(umlTrace_uml_TracedActivityFinalNode.__init__)


def test_umltrace_uml_tracedactivityfinalnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedlinkaction_is_not_abstract():
    assert not inspect.isabstract(TracedLinkAction)


def test_tracedlinkaction_constructor_exists():
    assert callable(TracedLinkAction.__init__)


def test_tracedlinkaction_constructor_args():
    sig = inspect.signature(TracedLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedwritelinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedWriteLinkAction)


def test_umltrace_uml_tracedwritelinkaction_constructor_exists():
    assert callable(umlTrace_uml_TracedWriteLinkAction.__init__)


def test_umltrace_uml_tracedwritelinkaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedWriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadlinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadLinkAction)


def test_umltrace_uml_tracedreadlinkaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadLinkAction.__init__)


def test_umltrace_uml_tracedreadlinkaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_AddStructuralFeatureValueAction)


def test_uml_umltrace_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(uml_umlTrace_AddStructuralFeatureValueAction.__init__)


def test_uml_umltrace_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_AddStructuralFeatureValueAction.__init__)
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



def test_uml_umltrace_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_AcceptEventAction)


def test_uml_umltrace_accepteventaction_constructor_exists():
    assert callable(uml_umlTrace_AcceptEventAction.__init__)


def test_uml_umltrace_accepteventaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_AcceptEventAction.__init__)
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



def test_tracedbehavior_is_not_abstract():
    assert not inspect.isabstract(TracedBehavior)


def test_tracedbehavior_constructor_exists():
    assert callable(TracedBehavior.__init__)


def test_tracedbehavior_constructor_args():
    sig = inspect.signature(TracedBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedactivity_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActivity)


def test_umltrace_uml_tracedactivity_constructor_exists():
    assert callable(umlTrace_uml_TracedActivity.__init__)


def test_umltrace_uml_tracedactivity_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActivity.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedopaquebehavior_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOpaqueBehavior)


def test_umltrace_uml_tracedopaquebehavior_constructor_exists():
    assert callable(umlTrace_uml_TracedOpaqueBehavior.__init__)


def test_umltrace_uml_tracedopaquebehavior_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_SendSignalAction)


def test_uml_umltrace_sendsignalaction_constructor_exists():
    assert callable(uml_umlTrace_SendSignalAction.__init__)


def test_uml_umltrace_sendsignalaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_SendSignalAction.__init__)
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



def test_umltrace_uml_tracedsendsignalaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSendSignalAction)


def test_umltrace_uml_tracedsendsignalaction_constructor_exists():
    assert callable(umlTrace_uml_TracedSendSignalAction.__init__)


def test_umltrace_uml_tracedsendsignalaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_RemoveStructuralFeatureValueAction)


def test_uml_umltrace_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(uml_umlTrace_RemoveStructuralFeatureValueAction.__init__)


def test_uml_umltrace_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_RemoveStructuralFeatureValueAction.__init__)
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



def test_uml_tracedbehavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(uml_TracedBehavioredClassifier)


def test_uml_tracedbehavioredclassifier_constructor_exists():
    assert callable(uml_TracedBehavioredClassifier.__init__)


def test_uml_tracedbehavioredclassifier_constructor_args():
    sig = inspect.signature(uml_TracedBehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclass_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClass)


def test_umltrace_uml_tracedclass_constructor_exists():
    assert callable(umlTrace_uml_TracedClass.__init__)


def test_umltrace_uml_tracedclass_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClass.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcollaboration_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCollaboration)


def test_umltrace_uml_tracedcollaboration_constructor_exists():
    assert callable(umlTrace_uml_TracedCollaboration.__init__)


def test_umltrace_uml_tracedcollaboration_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCollaboration.__init__)
    params = list(sig.parameters.keys())



def test_tracedrealization_is_not_abstract():
    assert not inspect.isabstract(TracedRealization)


def test_tracedrealization_constructor_exists():
    assert callable(TracedRealization.__init__)


def test_tracedrealization_constructor_args():
    sig = inspect.signature(TracedRealization.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedsubstitution_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSubstitution)


def test_umltrace_uml_tracedsubstitution_constructor_exists():
    assert callable(umlTrace_uml_TracedSubstitution.__init__)


def test_umltrace_uml_tracedsubstitution_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinterfacerealization_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInterfaceRealization)


def test_umltrace_uml_tracedinterfacerealization_constructor_exists():
    assert callable(umlTrace_uml_TracedInterfaceRealization.__init__)


def test_umltrace_uml_tracedinterfacerealization_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInterfaceRealization.__init__)
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



def test_umltrace_uml_tracedtimeconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTimeConstraint)


def test_umltrace_uml_tracedtimeconstraint_constructor_exists():
    assert callable(umlTrace_uml_TracedTimeConstraint.__init__)


def test_umltrace_uml_tracedtimeconstraint_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_artifact_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Artifact)


def test_uml_umltrace_artifact_constructor_exists():
    assert callable(uml_umlTrace_Artifact.__init__)


def test_uml_umltrace_artifact_constructor_args():
    sig = inspect.signature(uml_umlTrace_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddeploymenttarget_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDeploymentTarget)


def test_uml_traceddeploymenttarget_constructor_exists():
    assert callable(uml_TracedDeploymentTarget.__init__)


def test_uml_traceddeploymenttarget_constructor_args():
    sig = inspect.signature(uml_TracedDeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconnectableelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConnectableElement)


def test_uml_tracedconnectableelement_constructor_exists():
    assert callable(uml_TracedConnectableElement.__init__)


def test_uml_tracedconnectableelement_constructor_args():
    sig = inspect.signature(uml_TracedConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedremovestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRemoveStructuralFeatureValueAction)


def test_umltrace_uml_tracedremovestructuralfeaturevalueaction_constructor_exists():
    assert callable(umlTrace_uml_TracedRemoveStructuralFeatureValueAction.__init__)


def test_umltrace_uml_tracedremovestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_continuation_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Continuation)


def test_uml_umltrace_continuation_constructor_exists():
    assert callable(uml_umlTrace_Continuation.__init__)


def test_uml_umltrace_continuation_constructor_args():
    sig = inspect.signature(uml_umlTrace_Continuation.__init__)
    params = list(sig.parameters.keys())



def test_tracedinteractionfragment_is_not_abstract():
    assert not inspect.isabstract(TracedInteractionFragment)


def test_tracedinteractionfragment_constructor_exists():
    assert callable(TracedInteractionFragment.__init__)


def test_tracedinteractionfragment_constructor_args():
    sig = inspect.signature(TracedInteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstateinvariant_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStateInvariant)


def test_umltrace_uml_tracedstateinvariant_constructor_exists():
    assert callable(umlTrace_uml_TracedStateInvariant.__init__)


def test_umltrace_uml_tracedstateinvariant_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcombinedfragment_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCombinedFragment)


def test_umltrace_uml_tracedcombinedfragment_constructor_exists():
    assert callable(umlTrace_uml_TracedCombinedFragment.__init__)


def test_umltrace_uml_tracedcombinedfragment_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinteractionuse_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInteractionUse)


def test_umltrace_uml_tracedinteractionuse_constructor_exists():
    assert callable(umlTrace_uml_TracedInteractionUse.__init__)


def test_umltrace_uml_tracedinteractionuse_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcontinuation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedContinuation)


def test_umltrace_uml_tracedcontinuation_constructor_exists():
    assert callable(umlTrace_uml_TracedContinuation.__init__)


def test_umltrace_uml_tracedcontinuation_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedContinuation.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_property_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Property)


def test_uml_umltrace_property_constructor_exists():
    assert callable(uml_umlTrace_Property.__init__)


def test_uml_umltrace_property_constructor_args():
    sig = inspect.signature(uml_umlTrace_Property.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_connector_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Connector)


def test_uml_umltrace_connector_constructor_exists():
    assert callable(uml_umlTrace_Connector.__init__)


def test_uml_umltrace_connector_constructor_args():
    sig = inspect.signature(uml_umlTrace_Connector.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedbehavior_is_not_abstract():
    assert not inspect.isabstract(uml_TracedBehavior)


def test_uml_tracedbehavior_constructor_exists():
    assert callable(uml_TracedBehavior.__init__)


def test_uml_tracedbehavior_constructor_args():
    sig = inspect.signature(uml_TracedBehavior.__init__)
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



def test_uml_tracedmultiplicityelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedMultiplicityElement)


def test_uml_tracedmultiplicityelement_constructor_exists():
    assert callable(uml_TracedMultiplicityElement.__init__)


def test_uml_tracedmultiplicityelement_constructor_args():
    sig = inspect.signature(uml_TracedMultiplicityElement.__init__)
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



def test_uml_tracedfeature_is_not_abstract():
    assert not inspect.isabstract(uml_TracedFeature)


def test_uml_tracedfeature_constructor_exists():
    assert callable(uml_TracedFeature.__init__)


def test_uml_tracedfeature_constructor_args():
    sig = inspect.signature(uml_TracedFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedbehavioralfeature_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedBehavioralFeature)


def test_umltrace_uml_tracedbehavioralfeature_constructor_exists():
    assert callable(umlTrace_uml_TracedBehavioralFeature.__init__)


def test_umltrace_uml_tracedbehavioralfeature_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedBehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstructuralfeature_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStructuralFeature)


def test_umltrace_uml_tracedstructuralfeature_constructor_exists():
    assert callable(umlTrace_uml_TracedStructuralFeature.__init__)


def test_umltrace_uml_tracedstructuralfeature_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_input_tracedinputparametervalues_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Input_TracedInputParameterValues)


def test_umltrace_input_tracedinputparametervalues_constructor_exists():
    assert callable(umlTrace_Input_TracedInputParameterValues.__init__)


def test_umltrace_input_tracedinputparametervalues_constructor_args():
    sig = inspect.signature(umlTrace_Input_TracedInputParameterValues.__init__)
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



def test_uml_umltrace_datatype_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_DataType)


def test_uml_umltrace_datatype_constructor_exists():
    assert callable(uml_umlTrace_DataType.__init__)


def test_uml_umltrace_datatype_constructor_args():
    sig = inspect.signature(uml_umlTrace_DataType.__init__)
    params = list(sig.parameters.keys())



def test_tracedclassifier_is_not_abstract():
    assert not inspect.isabstract(TracedClassifier)


def test_tracedclassifier_constructor_exists():
    assert callable(TracedClassifier.__init__)


def test_tracedclassifier_constructor_args():
    sig = inspect.signature(TracedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstructuredclassifier_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStructuredClassifier)


def test_umltrace_uml_tracedstructuredclassifier_constructor_exists():
    assert callable(umlTrace_uml_TracedStructuredClassifier.__init__)


def test_umltrace_uml_tracedstructuredclassifier_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedsignal_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSignal)


def test_umltrace_uml_tracedsignal_constructor_exists():
    assert callable(umlTrace_uml_TracedSignal.__init__)


def test_umltrace_uml_tracedsignal_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSignal.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinformationitem_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInformationItem)


def test_umltrace_uml_tracedinformationitem_constructor_exists():
    assert callable(umlTrace_uml_TracedInformationItem.__init__)


def test_umltrace_uml_tracedinformationitem_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInformationItem.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddatatype_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDataType)


def test_umltrace_uml_traceddatatype_constructor_exists():
    assert callable(umlTrace_uml_TracedDataType.__init__)


def test_umltrace_uml_traceddatatype_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDataType.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_OpaqueAction)


def test_uml_umltrace_opaqueaction_constructor_exists():
    assert callable(uml_umlTrace_OpaqueAction.__init__)


def test_uml_umltrace_opaqueaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedaction_is_not_abstract():
    assert not inspect.isabstract(TracedAction)


def test_tracedaction_constructor_exists():
    assert callable(TracedAction.__init__)


def test_tracedaction_constructor_args():
    sig = inspect.signature(TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadIsClassifiedObjectAction)


def test_umltrace_uml_tracedreadisclassifiedobjectaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadIsClassifiedObjectAction.__init__)


def test_umltrace_uml_tracedreadisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReclassifyObjectAction)


def test_umltrace_uml_tracedreclassifyobjectaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReclassifyObjectAction.__init__)


def test_umltrace_uml_tracedreclassifyobjectaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinvocationaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInvocationAction)


def test_umltrace_uml_tracedinvocationaction_constructor_exists():
    assert callable(umlTrace_uml_TracedInvocationAction.__init__)


def test_umltrace_uml_tracedinvocationaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreplyaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReplyAction)


def test_umltrace_uml_tracedreplyaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReplyAction.__init__)


def test_umltrace_uml_tracedreplyaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtestidentityaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTestIdentityAction)


def test_umltrace_uml_tracedtestidentityaction_constructor_exists():
    assert callable(umlTrace_uml_TracedTestIdentityAction.__init__)


def test_umltrace_uml_tracedtestidentityaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedlinkaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLinkAction)


def test_umltrace_uml_tracedlinkaction_constructor_exists():
    assert callable(umlTrace_uml_TracedLinkAction.__init__)


def test_umltrace_uml_tracedlinkaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadselfaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadSelfAction)


def test_umltrace_uml_tracedreadselfaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadSelfAction.__init__)


def test_umltrace_uml_tracedreadselfaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddestroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDestroyObjectAction)


def test_umltrace_uml_traceddestroyobjectaction_constructor_exists():
    assert callable(umlTrace_uml_TracedDestroyObjectAction.__init__)


def test_umltrace_uml_traceddestroyobjectaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclearassociationaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClearAssociationAction)


def test_umltrace_uml_tracedclearassociationaction_constructor_exists():
    assert callable(umlTrace_uml_TracedClearAssociationAction.__init__)


def test_umltrace_uml_tracedclearassociationaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedraiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRaiseExceptionAction)


def test_umltrace_uml_tracedraiseexceptionaction_constructor_exists():
    assert callable(umlTrace_uml_TracedRaiseExceptionAction.__init__)


def test_umltrace_uml_tracedraiseexceptionaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadextentaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadExtentAction)


def test_umltrace_uml_tracedreadextentaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadExtentAction.__init__)


def test_umltrace_uml_tracedreadextentaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadLinkObjectEndQualifierAction)


def test_umltrace_uml_tracedreadlinkobjectendqualifieraction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadLinkObjectEndQualifierAction.__init__)


def test_umltrace_uml_tracedreadlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedunmarshallaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedUnmarshallAction)


def test_umltrace_uml_tracedunmarshallaction_constructor_exists():
    assert callable(umlTrace_uml_TracedUnmarshallAction.__init__)


def test_umltrace_uml_tracedunmarshallaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedUnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedaccepteventaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAcceptEventAction)


def test_umltrace_uml_tracedaccepteventaction_constructor_exists():
    assert callable(umlTrace_uml_TracedAcceptEventAction.__init__)


def test_umltrace_uml_tracedaccepteventaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedvaluespecificationaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedValueSpecificationAction)


def test_umltrace_uml_tracedvaluespecificationaction_constructor_exists():
    assert callable(umlTrace_uml_TracedValueSpecificationAction.__init__)


def test_umltrace_uml_tracedvaluespecificationaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedopaqueaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOpaqueAction)


def test_umltrace_uml_tracedopaqueaction_constructor_exists():
    assert callable(umlTrace_uml_TracedOpaqueAction.__init__)


def test_umltrace_uml_tracedopaqueaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOpaqueAction.__init__)
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



def test_tracedopaquebehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(TracedOpaqueBehaviorExecution)


def test_tracedopaquebehaviorexecution_constructor_exists():
    assert callable(TracedOpaqueBehaviorExecution.__init__)


def test_tracedopaquebehaviorexecution_constructor_args():
    sig = inspect.signature(TracedOpaqueBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_integerfunctions_tracedintegerplusfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution)


def test_umltrace_integerfunctions_tracedintegerplusfunctionbehaviorexecution_constructor_exists():
    assert callable(umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution.__init__)


def test_umltrace_integerfunctions_tracedintegerplusfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution.__init__)
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



def test_uml_umltrace_include_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Include)


def test_uml_umltrace_include_constructor_exists():
    assert callable(uml_umlTrace_Include.__init__)


def test_uml_umltrace_include_constructor_args():
    sig = inspect.signature(uml_umlTrace_Include.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddirectedrelationship_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDirectedRelationship)


def test_uml_traceddirectedrelationship_constructor_exists():
    assert callable(uml_TracedDirectedRelationship.__init__)


def test_uml_traceddirectedrelationship_constructor_args():
    sig = inspect.signature(uml_TracedDirectedRelationship.__init__)
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



def test_umltrace_uml_traceddurationinterval_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDurationInterval)


def test_umltrace_uml_traceddurationinterval_constructor_exists():
    assert callable(umlTrace_uml_TracedDurationInterval.__init__)


def test_umltrace_uml_traceddurationinterval_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDurationInterval.__init__)
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



def test_umltrace_uml_tracedvariableaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedVariableAction)


def test_umltrace_uml_tracedvariableaction_constructor_exists():
    assert callable(umlTrace_uml_TracedVariableAction.__init__)


def test_umltrace_uml_tracedvariableaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_activitypartition_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ActivityPartition)


def test_uml_umltrace_activitypartition_constructor_exists():
    assert callable(uml_umlTrace_ActivityPartition.__init__)


def test_uml_umltrace_activitypartition_constructor_args():
    sig = inspect.signature(uml_umlTrace_ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactivitygroup_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivityGroup)


def test_uml_tracedactivitygroup_constructor_exists():
    assert callable(uml_TracedActivityGroup.__init__)


def test_uml_tracedactivitygroup_constructor_args():
    sig = inspect.signature(uml_TracedActivityGroup.__init__)
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



def test_umltrace_uml_tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedActivityNode)


def test_umltrace_uml_tracedactivitynode_constructor_exists():
    assert callable(umlTrace_uml_TracedActivityNode.__init__)


def test_umltrace_uml_tracedactivitynode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedActivityNode.__init__)
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



def test_uml_umltrace_collaborationuse_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_CollaborationUse)


def test_uml_umltrace_collaborationuse_constructor_exists():
    assert callable(uml_umlTrace_CollaborationUse.__init__)


def test_uml_umltrace_collaborationuse_constructor_args():
    sig = inspect.signature(uml_umlTrace_CollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcollaborationuse_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCollaborationUse)


def test_umltrace_uml_tracedcollaborationuse_constructor_exists():
    assert callable(umlTrace_uml_TracedCollaborationUse.__init__)


def test_umltrace_uml_tracedcollaborationuse_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCollaborationUse.__init__)
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



def test_uml_umltrace_protocolconformance_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ProtocolConformance)


def test_uml_umltrace_protocolconformance_constructor_exists():
    assert callable(uml_umlTrace_ProtocolConformance.__init__)


def test_uml_umltrace_protocolconformance_constructor_args():
    sig = inspect.signature(uml_umlTrace_ProtocolConformance.__init__)
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



def test_uml_umltrace_timeobservation_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_TimeObservation)


def test_uml_umltrace_timeobservation_constructor_exists():
    assert callable(uml_umlTrace_TimeObservation.__init__)


def test_uml_umltrace_timeobservation_constructor_args():
    sig = inspect.signature(uml_umlTrace_TimeObservation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtimeobservation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTimeObservation)


def test_umltrace_uml_tracedtimeobservation_constructor_exists():
    assert callable(umlTrace_uml_TracedTimeObservation.__init__)


def test_umltrace_uml_tracedtimeobservation_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTimeObservation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExecutionSpecification)


def test_umltrace_uml_tracedexecutionspecification_constructor_exists():
    assert callable(umlTrace_uml_TracedExecutionSpecification.__init__)


def test_umltrace_uml_tracedexecutionspecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_lifeline_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Lifeline)


def test_uml_umltrace_lifeline_constructor_exists():
    assert callable(uml_umlTrace_Lifeline.__init__)


def test_uml_umltrace_lifeline_constructor_args():
    sig = inspect.signature(uml_umlTrace_Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_tracedvariableaction_is_not_abstract():
    assert not inspect.isabstract(TracedVariableAction)


def test_tracedvariableaction_constructor_exists():
    assert callable(TracedVariableAction.__init__)


def test_tracedvariableaction_constructor_args():
    sig = inspect.signature(TracedVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclearvariableaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClearVariableAction)


def test_umltrace_uml_tracedclearvariableaction_constructor_exists():
    assert callable(umlTrace_uml_TracedClearVariableAction.__init__)


def test_umltrace_uml_tracedclearvariableaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClearVariableAction.__init__)
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



def test_umltrace_uml_tracedsendobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSendObjectAction)


def test_umltrace_uml_tracedsendobjectaction_constructor_exists():
    assert callable(umlTrace_uml_TracedSendObjectAction.__init__)


def test_umltrace_uml_tracedsendobjectaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedrelationship_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRelationship)


def test_umltrace_uml_tracedrelationship_constructor_exists():
    assert callable(umlTrace_uml_TracedRelationship.__init__)


def test_umltrace_uml_tracedrelationship_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_tracedtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(TracedTemplateParameter)


def test_tracedtemplateparameter_constructor_exists():
    assert callable(TracedTemplateParameter.__init__)


def test_tracedtemplateparameter_constructor_args():
    sig = inspect.signature(TracedTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedoperationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOperationTemplateParameter)


def test_umltrace_uml_tracedoperationtemplateparameter_constructor_exists():
    assert callable(umlTrace_uml_TracedOperationTemplateParameter.__init__)


def test_umltrace_uml_tracedoperationtemplateparameter_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclassifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClassifierTemplateParameter)


def test_umltrace_uml_tracedclassifiertemplateparameter_constructor_exists():
    assert callable(umlTrace_uml_TracedClassifierTemplateParameter.__init__)


def test_umltrace_uml_tracedclassifiertemplateparameter_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconnectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConnectableElementTemplateParameter)


def test_umltrace_uml_tracedconnectableelementtemplateparameter_constructor_exists():
    assert callable(umlTrace_uml_TracedConnectableElementTemplateParameter.__init__)


def test_umltrace_uml_tracedconnectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_callevent_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_CallEvent)


def test_uml_umltrace_callevent_constructor_exists():
    assert callable(uml_umlTrace_CallEvent.__init__)


def test_uml_umltrace_callevent_constructor_args():
    sig = inspect.signature(uml_umlTrace_CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_StartClassifierBehaviorAction)


def test_uml_umltrace_startclassifierbehavioraction_constructor_exists():
    assert callable(uml_umlTrace_StartClassifierBehaviorAction.__init__)


def test_uml_umltrace_startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(uml_umlTrace_StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedlifeline_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLifeline)


def test_umltrace_uml_tracedlifeline_constructor_exists():
    assert callable(umlTrace_uml_TracedLifeline.__init__)


def test_umltrace_uml_tracedlifeline_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_SendObjectAction)


def test_uml_umltrace_sendobjectaction_constructor_exists():
    assert callable(uml_umlTrace_SendObjectAction.__init__)


def test_uml_umltrace_sendobjectaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAction)


def test_uml_tracedaction_constructor_exists():
    assert callable(uml_TracedAction.__init__)


def test_uml_tracedaction_constructor_args():
    sig = inspect.signature(uml_TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstructuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStructuredActivityNode)


def test_umltrace_uml_tracedstructuredactivitynode_constructor_exists():
    assert callable(umlTrace_uml_TracedStructuredActivityNode.__init__)


def test_umltrace_uml_tracedstructuredactivitynode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinteractionfragment_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInteractionFragment)


def test_uml_tracedinteractionfragment_constructor_exists():
    assert callable(uml_TracedInteractionFragment.__init__)


def test_uml_tracedinteractionfragment_constructor_args():
    sig = inspect.signature(uml_TracedInteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinteractionoperand_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInteractionOperand)


def test_umltrace_uml_tracedinteractionoperand_constructor_exists():
    assert callable(umlTrace_uml_TracedInteractionOperand.__init__)


def test_umltrace_uml_tracedinteractionoperand_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinteraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInteraction)


def test_umltrace_uml_tracedinteraction_constructor_exists():
    assert callable(umlTrace_uml_TracedInteraction.__init__)


def test_umltrace_uml_tracedinteraction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInteraction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstatemachine_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStateMachine)


def test_umltrace_uml_tracedstatemachine_constructor_exists():
    assert callable(umlTrace_uml_TracedStateMachine.__init__)


def test_umltrace_uml_tracedstatemachine_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedextensionend_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExtensionEnd)


def test_umltrace_uml_tracedextensionend_constructor_exists():
    assert callable(umlTrace_uml_TracedExtensionEnd.__init__)


def test_umltrace_uml_tracedextensionend_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstartclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStartClassifierBehaviorAction)


def test_umltrace_uml_tracedstartclassifierbehavioraction_constructor_exists():
    assert callable(umlTrace_uml_TracedStartClassifierBehaviorAction.__init__)


def test_umltrace_uml_tracedstartclassifierbehavioraction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStartClassifierBehaviorAction.__init__)
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



def test_uml_umltrace_literalstring_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_LiteralString)


def test_uml_umltrace_literalstring_constructor_exists():
    assert callable(uml_umlTrace_LiteralString.__init__)


def test_uml_umltrace_literalstring_constructor_args():
    sig = inspect.signature(uml_umlTrace_LiteralString.__init__)
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



def test_umltrace_uml_tracedliteralinteger_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLiteralInteger)


def test_umltrace_uml_tracedliteralinteger_constructor_exists():
    assert callable(umlTrace_uml_TracedLiteralInteger.__init__)


def test_umltrace_uml_tracedliteralinteger_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLiteralInteger.__init__)
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



def test_umltrace_uml_tracedliteralnull_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLiteralNull)


def test_umltrace_uml_tracedliteralnull_constructor_exists():
    assert callable(umlTrace_uml_TracedLiteralNull.__init__)


def test_umltrace_uml_tracedliteralnull_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedliteralstring_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLiteralString)


def test_umltrace_uml_tracedliteralstring_constructor_exists():
    assert callable(umlTrace_uml_TracedLiteralString.__init__)


def test_umltrace_uml_tracedliteralstring_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLiteralString.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedNamedElement)


def test_umltrace_uml_tracednamedelement_constructor_exists():
    assert callable(umlTrace_uml_TracedNamedElement.__init__)


def test_umltrace_uml_tracednamedelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_AnyReceiveEvent)


def test_uml_umltrace_anyreceiveevent_constructor_exists():
    assert callable(uml_umlTrace_AnyReceiveEvent.__init__)


def test_uml_umltrace_anyreceiveevent_constructor_args():
    sig = inspect.signature(uml_umlTrace_AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ReadLinkObjectEndAction)


def test_uml_umltrace_readlinkobjectendaction_constructor_exists():
    assert callable(uml_umlTrace_ReadLinkObjectEndAction.__init__)


def test_uml_umltrace_readlinkobjectendaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_interface_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Interface)


def test_uml_umltrace_interface_constructor_exists():
    assert callable(uml_umlTrace_Interface.__init__)


def test_uml_umltrace_interface_constructor_args():
    sig = inspect.signature(uml_umlTrace_Interface.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadLinkObjectEndAction)


def test_umltrace_uml_tracedreadlinkobjectendaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadLinkObjectEndAction.__init__)


def test_umltrace_uml_tracedreadlinkobjectendaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOccurrenceSpecification)


def test_umltrace_uml_tracedoccurrencespecification_constructor_exists():
    assert callable(umlTrace_uml_TracedOccurrenceSpecification.__init__)


def test_umltrace_uml_tracedoccurrencespecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOccurrenceSpecification.__init__)
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



def test_uml_umltrace_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_CreateObjectAction)


def test_uml_umltrace_createobjectaction_constructor_exists():
    assert callable(uml_umlTrace_CreateObjectAction.__init__)


def test_uml_umltrace_createobjectaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcreateobjectaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCreateObjectAction)


def test_umltrace_uml_tracedcreateobjectaction_constructor_exists():
    assert callable(umlTrace_uml_TracedCreateObjectAction.__init__)


def test_umltrace_uml_tracedcreateobjectaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinterface_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInterface)


def test_umltrace_uml_tracedinterface_constructor_exists():
    assert callable(umlTrace_uml_TracedInterface.__init__)


def test_umltrace_uml_tracedinterface_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInterface.__init__)
    params = list(sig.parameters.keys())



def test_tracedclass_is_not_abstract():
    assert not inspect.isabstract(TracedClass)


def test_tracedclass_constructor_exists():
    assert callable(TracedClass.__init__)


def test_tracedclass_constructor_args():
    sig = inspect.signature(TracedClass.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedbehavior_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedBehavior)


def test_umltrace_uml_tracedbehavior_constructor_exists():
    assert callable(umlTrace_uml_TracedBehavior.__init__)


def test_umltrace_uml_tracedbehavior_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcomponent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedComponent)


def test_umltrace_uml_tracedcomponent_constructor_exists():
    assert callable(umlTrace_uml_TracedComponent.__init__)


def test_umltrace_uml_tracedcomponent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedComponent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstereotype_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStereotype)


def test_umltrace_uml_tracedstereotype_constructor_exists():
    assert callable(umlTrace_uml_TracedStereotype.__init__)


def test_umltrace_uml_tracedstereotype_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStereotype.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddeployedartifact_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDeployedArtifact)


def test_umltrace_uml_traceddeployedartifact_constructor_exists():
    assert callable(umlTrace_uml_TracedDeployedArtifact.__init__)


def test_umltrace_uml_traceddeployedartifact_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_OccurrenceSpecification)


def test_uml_umltrace_occurrencespecification_constructor_exists():
    assert callable(uml_umlTrace_OccurrenceSpecification.__init__)


def test_uml_umltrace_occurrencespecification_constructor_args():
    sig = inspect.signature(uml_umlTrace_OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ExtensionPoint)


def test_uml_umltrace_extensionpoint_constructor_exists():
    assert callable(uml_umlTrace_ExtensionPoint.__init__)


def test_uml_umltrace_extensionpoint_constructor_args():
    sig = inspect.signature(uml_umlTrace_ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_signalevent_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_SignalEvent)


def test_uml_umltrace_signalevent_constructor_exists():
    assert callable(uml_umlTrace_SignalEvent.__init__)


def test_uml_umltrace_signalevent_constructor_args():
    sig = inspect.signature(uml_umlTrace_SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_tracedmessageevent_is_not_abstract():
    assert not inspect.isabstract(TracedMessageEvent)


def test_tracedmessageevent_constructor_exists():
    assert callable(TracedMessageEvent.__init__)


def test_tracedmessageevent_constructor_args():
    sig = inspect.signature(TracedMessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedanyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAnyReceiveEvent)


def test_umltrace_uml_tracedanyreceiveevent_constructor_exists():
    assert callable(umlTrace_uml_TracedAnyReceiveEvent.__init__)


def test_umltrace_uml_tracedanyreceiveevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcallevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedCallEvent)


def test_umltrace_uml_tracedcallevent_constructor_exists():
    assert callable(umlTrace_uml_TracedCallEvent.__init__)


def test_umltrace_uml_tracedcallevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedCallEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedsignalevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSignalEvent)


def test_umltrace_uml_tracedsignalevent_constructor_exists():
    assert callable(umlTrace_uml_TracedSignalEvent.__init__)


def test_umltrace_uml_tracedsignalevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_slot_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Slot)


def test_uml_umltrace_slot_constructor_exists():
    assert callable(uml_umlTrace_Slot.__init__)


def test_uml_umltrace_slot_constructor_args():
    sig = inspect.signature(uml_umlTrace_Slot.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_elementimport_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ElementImport)


def test_uml_umltrace_elementimport_constructor_exists():
    assert callable(uml_umlTrace_ElementImport.__init__)


def test_uml_umltrace_elementimport_constructor_args():
    sig = inspect.signature(uml_umlTrace_ElementImport.__init__)
    params = list(sig.parameters.keys())



def test_traceddirectedrelationship_is_not_abstract():
    assert not inspect.isabstract(TracedDirectedRelationship)


def test_traceddirectedrelationship_constructor_exists():
    assert callable(TracedDirectedRelationship.__init__)


def test_traceddirectedrelationship_constructor_args():
    sig = inspect.signature(TracedDirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedpackageimport_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPackageImport)


def test_umltrace_uml_tracedpackageimport_constructor_exists():
    assert callable(umlTrace_uml_TracedPackageImport.__init__)


def test_umltrace_uml_tracedpackageimport_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPackageImport.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedprofileapplication_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedProfileApplication)


def test_umltrace_uml_tracedprofileapplication_constructor_exists():
    assert callable(umlTrace_uml_TracedProfileApplication.__init__)


def test_umltrace_uml_tracedprofileapplication_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedProfileApplication.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtemplatebinding_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTemplateBinding)


def test_umltrace_uml_tracedtemplatebinding_constructor_exists():
    assert callable(umlTrace_uml_TracedTemplateBinding.__init__)


def test_umltrace_uml_tracedtemplatebinding_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedprotocolconformance_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedProtocolConformance)


def test_umltrace_uml_tracedprotocolconformance_constructor_exists():
    assert callable(umlTrace_uml_TracedProtocolConformance.__init__)


def test_umltrace_uml_tracedprotocolconformance_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedgeneralization_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedGeneralization)


def test_umltrace_uml_tracedgeneralization_constructor_exists():
    assert callable(umlTrace_uml_TracedGeneralization.__init__)


def test_umltrace_uml_tracedgeneralization_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedGeneralization.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedpackagemerge_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPackageMerge)


def test_umltrace_uml_tracedpackagemerge_constructor_exists():
    assert callable(umlTrace_uml_TracedPackageMerge.__init__)


def test_umltrace_uml_tracedpackagemerge_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedelementimport_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedElementImport)


def test_umltrace_uml_tracedelementimport_constructor_exists():
    assert callable(umlTrace_uml_TracedElementImport.__init__)


def test_umltrace_uml_tracedelementimport_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedElementImport.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_StartObjectBehaviorAction)


def test_uml_umltrace_startobjectbehavioraction_constructor_exists():
    assert callable(uml_umlTrace_StartObjectBehaviorAction.__init__)


def test_uml_umltrace_startobjectbehavioraction_constructor_args():
    sig = inspect.signature(uml_umlTrace_StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedcallaction_is_not_abstract():
    assert not inspect.isabstract(TracedCallAction)


def test_tracedcallaction_constructor_exists():
    assert callable(TracedCallAction.__init__)


def test_tracedcallaction_constructor_args():
    sig = inspect.signature(TracedCallAction.__init__)
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



def test_umltrace_uml_tracedstartobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStartObjectBehaviorAction)


def test_umltrace_uml_tracedstartobjectbehavioraction_constructor_exists():
    assert callable(umlTrace_uml_TracedStartObjectBehaviorAction.__init__)


def test_umltrace_uml_tracedstartobjectbehavioraction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_joinnode_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_JoinNode)


def test_uml_umltrace_joinnode_constructor_exists():
    assert callable(uml_umlTrace_JoinNode.__init__)


def test_uml_umltrace_joinnode_constructor_args():
    sig = inspect.signature(uml_umlTrace_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(TracedControlNode)


def test_tracedcontrolnode_constructor_exists():
    assert callable(TracedControlNode.__init__)


def test_tracedcontrolnode_constructor_args():
    sig = inspect.signature(TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedforknode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedForkNode)


def test_umltrace_uml_tracedforknode_constructor_exists():
    assert callable(umlTrace_uml_TracedForkNode.__init__)


def test_umltrace_uml_tracedforknode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedForkNode.__init__)
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



def test_umltrace_uml_tracedmergenode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedMergeNode)


def test_umltrace_uml_tracedmergenode_constructor_exists():
    assert callable(umlTrace_uml_TracedMergeNode.__init__)


def test_umltrace_uml_tracedmergenode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedMergeNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinitialnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInitialNode)


def test_umltrace_uml_tracedinitialnode_constructor_exists():
    assert callable(umlTrace_uml_TracedInitialNode.__init__)


def test_umltrace_uml_tracedinitialnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedjoinnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedJoinNode)


def test_umltrace_uml_tracedjoinnode_constructor_exists():
    assert callable(umlTrace_uml_TracedJoinNode.__init__)


def test_umltrace_uml_tracedjoinnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedJoinNode.__init__)
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



def test_tracedstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(TracedStructuralFeatureAction)


def test_tracedstructuralfeatureaction_constructor_exists():
    assert callable(TracedStructuralFeatureAction.__init__)


def test_tracedstructuralfeatureaction_constructor_args():
    sig = inspect.signature(TracedStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedclearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedClearStructuralFeatureAction)


def test_umltrace_uml_tracedclearstructuralfeatureaction_constructor_exists():
    assert callable(umlTrace_uml_TracedClearStructuralFeatureAction.__init__)


def test_umltrace_uml_tracedclearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreadstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReadStructuralFeatureAction)


def test_umltrace_uml_tracedreadstructuralfeatureaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReadStructuralFeatureAction.__init__)


def test_umltrace_uml_tracedreadstructuralfeatureaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedwritestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedWriteStructuralFeatureAction)


def test_umltrace_uml_tracedwritestructuralfeatureaction_constructor_exists():
    assert callable(umlTrace_uml_TracedWriteStructuralFeatureAction.__init__)


def test_umltrace_uml_tracedwritestructuralfeatureaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedWriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedslot_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSlot)


def test_umltrace_uml_tracedslot_constructor_exists():
    assert callable(umlTrace_uml_TracedSlot.__init__)


def test_umltrace_uml_tracedslot_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSlot.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedcomponentrealization_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedComponentRealization)


def test_umltrace_uml_tracedcomponentrealization_constructor_exists():
    assert callable(umlTrace_uml_TracedComponentRealization.__init__)


def test_umltrace_uml_tracedcomponentrealization_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedreduceaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedReduceAction)


def test_umltrace_uml_tracedreduceaction_constructor_exists():
    assert callable(umlTrace_uml_TracedReduceAction.__init__)


def test_umltrace_uml_tracedreduceaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedReduceAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_generalizationset_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_GeneralizationSet)


def test_uml_umltrace_generalizationset_constructor_exists():
    assert callable(uml_umlTrace_GeneralizationSet.__init__)


def test_uml_umltrace_generalizationset_constructor_args():
    sig = inspect.signature(uml_umlTrace_GeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_tracedconstraint_is_not_abstract():
    assert not inspect.isabstract(TracedConstraint)


def test_tracedconstraint_constructor_exists():
    assert callable(TracedConstraint.__init__)


def test_tracedconstraint_constructor_args():
    sig = inspect.signature(TracedConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedintervalconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedIntervalConstraint)


def test_umltrace_uml_tracedintervalconstraint_constructor_exists():
    assert callable(umlTrace_uml_TracedIntervalConstraint.__init__)


def test_umltrace_uml_tracedintervalconstraint_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedIntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedinteractionconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInteractionConstraint)


def test_umltrace_uml_tracedinteractionconstraint_constructor_exists():
    assert callable(umlTrace_uml_TracedInteractionConstraint.__init__)


def test_umltrace_uml_tracedinteractionconstraint_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInteractionConstraint.__init__)
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



def test_uml_tracedexecutablenode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExecutableNode)


def test_uml_tracedexecutablenode_constructor_exists():
    assert callable(uml_TracedExecutableNode.__init__)


def test_uml_tracedexecutablenode_constructor_args():
    sig = inspect.signature(uml_TracedExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedstructuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(TracedStructuredActivityNode)


def test_tracedstructuredactivitynode_constructor_exists():
    assert callable(TracedStructuredActivityNode.__init__)


def test_tracedstructuredactivitynode_constructor_args():
    sig = inspect.signature(TracedStructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedexpansionregion_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExpansionRegion)


def test_umltrace_uml_tracedexpansionregion_constructor_exists():
    assert callable(umlTrace_uml_TracedExpansionRegion.__init__)


def test_umltrace_uml_tracedexpansionregion_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconditionalnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConditionalNode)


def test_umltrace_uml_tracedconditionalnode_constructor_exists():
    assert callable(umlTrace_uml_TracedConditionalNode.__init__)


def test_umltrace_uml_tracedconditionalnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedloopnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLoopNode)


def test_umltrace_uml_tracedloopnode_constructor_exists():
    assert callable(umlTrace_uml_TracedLoopNode.__init__)


def test_umltrace_uml_tracedloopnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLoopNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedsequencenode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedSequenceNode)


def test_umltrace_uml_tracedsequencenode_constructor_exists():
    assert callable(umlTrace_uml_TracedSequenceNode.__init__)


def test_umltrace_uml_tracedsequencenode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedSequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_inputpin_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_InputPin)


def test_uml_umltrace_inputpin_constructor_exists():
    assert callable(uml_umlTrace_InputPin.__init__)


def test_uml_umltrace_inputpin_constructor_args():
    sig = inspect.signature(uml_umlTrace_InputPin.__init__)
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



def test_uml_umltrace_reduceaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_ReduceAction)


def test_uml_umltrace_reduceaction_constructor_exists():
    assert callable(uml_umlTrace_ReduceAction.__init__)


def test_uml_umltrace_reduceaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_ReduceAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStructuralFeatureAction)


def test_umltrace_uml_tracedstructuralfeatureaction_constructor_exists():
    assert callable(umlTrace_uml_TracedStructuralFeatureAction.__init__)


def test_umltrace_uml_tracedstructuralfeatureaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedbehavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedBehavioredClassifier)


def test_umltrace_uml_tracedbehavioredclassifier_constructor_exists():
    assert callable(umlTrace_uml_TracedBehavioredClassifier.__init__)


def test_umltrace_uml_tracedbehavioredclassifier_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedBehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_package_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Package)


def test_uml_umltrace_package_constructor_exists():
    assert callable(uml_umlTrace_Package.__init__)


def test_uml_umltrace_package_constructor_args():
    sig = inspect.signature(uml_umlTrace_Package.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedliteralspecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedLiteralSpecification)


def test_umltrace_uml_tracedliteralspecification_constructor_exists():
    assert callable(umlTrace_uml_TracedLiteralSpecification.__init__)


def test_umltrace_uml_tracedliteralspecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedLiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedmultiplicityelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedMultiplicityElement)


def test_umltrace_uml_tracedmultiplicityelement_constructor_exists():
    assert callable(umlTrace_uml_TracedMultiplicityElement.__init__)


def test_umltrace_uml_tracedmultiplicityelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedMultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_constraint_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_Constraint)


def test_uml_umltrace_constraint_constructor_exists():
    assert callable(uml_umlTrace_Constraint.__init__)


def test_uml_umltrace_constraint_constructor_args():
    sig = inspect.signature(uml_umlTrace_Constraint.__init__)
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



def test_umltrace_uml_tracedinstancespecification_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedInstanceSpecification)


def test_umltrace_uml_tracedinstancespecification_constructor_exists():
    assert callable(umlTrace_uml_TracedInstanceSpecification.__init__)


def test_umltrace_uml_tracedinstancespecification_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedInstanceSpecification.__init__)
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



def test_umltrace_uml_tracedpackage_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPackage)


def test_umltrace_uml_tracedpackage_constructor_exists():
    assert callable(umlTrace_uml_TracedPackage.__init__)


def test_umltrace_uml_tracedpackage_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPackage.__init__)
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



def test_umltrace_uml_tracedextension_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedExtension)


def test_umltrace_uml_tracedextension_constructor_exists():
    assert callable(umlTrace_uml_TracedExtension.__init__)


def test_umltrace_uml_tracedextension_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedExtension.__init__)
    params = list(sig.parameters.keys())



def test_tracedpackageableelement_is_not_abstract():
    assert not inspect.isabstract(TracedPackageableElement)


def test_tracedpackageableelement_constructor_exists():
    assert callable(TracedPackageableElement.__init__)


def test_tracedpackageableelement_constructor_args():
    sig = inspect.signature(TracedPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedobservation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedObservation)


def test_umltrace_uml_tracedobservation_constructor_exists():
    assert callable(umlTrace_uml_TracedObservation.__init__)


def test_umltrace_uml_tracedobservation_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedObservation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedgeneralizationset_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedGeneralizationSet)


def test_umltrace_uml_tracedgeneralizationset_constructor_exists():
    assert callable(umlTrace_uml_TracedGeneralizationSet.__init__)


def test_umltrace_uml_tracedgeneralizationset_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedGeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedEvent)


def test_umltrace_uml_tracedevent_constructor_exists():
    assert callable(umlTrace_uml_TracedEvent.__init__)


def test_umltrace_uml_tracedevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconstraint_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConstraint)


def test_umltrace_uml_tracedconstraint_constructor_exists():
    assert callable(umlTrace_uml_TracedConstraint.__init__)


def test_umltrace_uml_tracedconstraint_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtype_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedType)


def test_umltrace_uml_tracedtype_constructor_exists():
    assert callable(umlTrace_uml_TracedType.__init__)


def test_umltrace_uml_tracedtype_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedType.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedparameterableelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedParameterableElement)


def test_uml_tracedparameterableelement_constructor_exists():
    assert callable(uml_TracedParameterableElement.__init__)


def test_uml_tracedparameterableelement_constructor_args():
    sig = inspect.signature(uml_TracedParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedconnectableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedConnectableElement)


def test_umltrace_uml_tracedconnectableelement_constructor_exists():
    assert callable(umlTrace_uml_TracedConnectableElement.__init__)


def test_umltrace_uml_tracedconnectableelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedoperation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedOperation)


def test_umltrace_uml_tracedoperation_constructor_exists():
    assert callable(umlTrace_uml_TracedOperation.__init__)


def test_umltrace_uml_tracedoperation_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedOperation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedpackageableelement_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedPackageableElement)


def test_umltrace_uml_tracedpackageableelement_constructor_exists():
    assert callable(umlTrace_uml_TracedPackageableElement.__init__)


def test_umltrace_uml_tracedpackageableelement_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_timeevent_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_TimeEvent)


def test_uml_umltrace_timeevent_constructor_exists():
    assert callable(uml_umlTrace_TimeEvent.__init__)


def test_uml_umltrace_timeevent_constructor_args():
    sig = inspect.signature(uml_umlTrace_TimeEvent.__init__)
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



def test_umltrace_uml_tracedchangeevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedChangeEvent)


def test_umltrace_uml_tracedchangeevent_constructor_exists():
    assert callable(umlTrace_uml_TracedChangeEvent.__init__)


def test_umltrace_uml_tracedchangeevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedtimeevent_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedTimeEvent)


def test_umltrace_uml_tracedtimeevent_constructor_exists():
    assert callable(umlTrace_uml_TracedTimeEvent.__init__)


def test_umltrace_uml_tracedtimeevent_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedTimeEvent.__init__)
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



def test_traceddependency_is_not_abstract():
    assert not inspect.isabstract(TracedDependency)


def test_traceddependency_constructor_exists():
    assert callable(TracedDependency.__init__)


def test_traceddependency_constructor_args():
    sig = inspect.signature(TracedDependency.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedabstraction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedAbstraction)


def test_umltrace_uml_tracedabstraction_constructor_exists():
    assert callable(umlTrace_uml_TracedAbstraction.__init__)


def test_umltrace_uml_tracedabstraction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedAbstraction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedusage_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedUsage)


def test_umltrace_uml_tracedusage_constructor_exists():
    assert callable(umlTrace_uml_TracedUsage.__init__)


def test_umltrace_uml_tracedusage_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedUsage.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_traceddeployment_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedDeployment)


def test_umltrace_uml_traceddeployment_constructor_exists():
    assert callable(umlTrace_uml_TracedDeployment.__init__)


def test_umltrace_uml_traceddeployment_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedDeployment.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_BroadcastSignalAction)


def test_uml_umltrace_broadcastsignalaction_constructor_exists():
    assert callable(uml_umlTrace_BroadcastSignalAction.__init__)


def test_uml_umltrace_broadcastsignalaction_constructor_args():
    sig = inspect.signature(uml_umlTrace_BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedbroadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedBroadcastSignalAction)


def test_umltrace_uml_tracedbroadcastsignalaction_constructor_exists():
    assert callable(umlTrace_uml_TracedBroadcastSignalAction.__init__)


def test_umltrace_uml_tracedbroadcastsignalaction_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedBroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_umltrace_templatesignature_is_not_abstract():
    assert not inspect.isabstract(uml_umlTrace_TemplateSignature)


def test_uml_umltrace_templatesignature_constructor_exists():
    assert callable(uml_umlTrace_TemplateSignature.__init__)


def test_uml_umltrace_templatesignature_constructor_args():
    sig = inspect.signature(uml_umlTrace_TemplateSignature.__init__)
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



def test_uml_tracedlinkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLinkEndDestructionData)


def test_uml_tracedlinkenddestructiondata_constructor_exists():
    assert callable(uml_TracedLinkEndDestructionData.__init__)


def test_uml_tracedlinkenddestructiondata_constructor_args():
    sig = inspect.signature(uml_TracedLinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedclassifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_TracedClassifierTemplateParameter)


def test_uml_tracedclassifiertemplateparameter_constructor_exists():
    assert callable(uml_TracedClassifierTemplateParameter.__init__)


def test_uml_tracedclassifiertemplateparameter_constructor_args():
    sig = inspect.signature(uml_TracedClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_TracedAddStructuralFeatureValueActionActivation)


def test_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_constructor_exists():
    assert callable(IntermediateActions_TracedAddStructuralFeatureValueActionActivation.__init__)


def test_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_constructor_args():
    sig = inspect.signature(IntermediateActions_TracedAddStructuralFeatureValueActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_tracedcallbehavioractionactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TracedCallBehaviorActionActivation)


def test_basicactions_tracedcallbehavioractionactivation_constructor_exists():
    assert callable(BasicActions_TracedCallBehaviorActionActivation.__init__)


def test_basicactions_tracedcallbehavioractionactivation_constructor_args():
    sig = inspect.signature(BasicActions_TracedCallBehaviorActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedprotocolconformance_is_not_abstract():
    assert not inspect.isabstract(uml_TracedProtocolConformance)


def test_uml_tracedprotocolconformance_constructor_exists():
    assert callable(uml_TracedProtocolConformance.__init__)


def test_uml_tracedprotocolconformance_constructor_args():
    sig = inspect.signature(uml_TracedProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedloopnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLoopNode)


def test_uml_tracedloopnode_constructor_exists():
    assert callable(uml_TracedLoopNode.__init__)


def test_uml_tracedloopnode_constructor_args():
    sig = inspect.signature(uml_TracedLoopNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedexpansionregion_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExpansionRegion)


def test_uml_tracedexpansionregion_constructor_exists():
    assert callable(uml_TracedExpansionRegion.__init__)


def test_uml_tracedexpansionregion_constructor_args():
    sig = inspect.signature(uml_TracedExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactivitypartition_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivityPartition)


def test_uml_tracedactivitypartition_constructor_exists():
    assert callable(uml_TracedActivityPartition.__init__)


def test_uml_tracedactivitypartition_constructor_args():
    sig = inspect.signature(uml_TracedActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcollaborationuse_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCollaborationUse)


def test_uml_tracedcollaborationuse_constructor_exists():
    assert callable(uml_TracedCollaborationUse.__init__)


def test_uml_tracedcollaborationuse_constructor_args():
    sig = inspect.signature(uml_TracedCollaborationUse.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedenumeration_is_not_abstract():
    assert not inspect.isabstract(uml_TracedEnumeration)


def test_uml_tracedenumeration_constructor_exists():
    assert callable(uml_TracedEnumeration.__init__)


def test_uml_tracedenumeration_constructor_args():
    sig = inspect.signature(uml_TracedEnumeration.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedlifeline_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLifeline)


def test_uml_tracedlifeline_constructor_exists():
    assert callable(uml_TracedLifeline.__init__)


def test_uml_tracedlifeline_constructor_args():
    sig = inspect.signature(uml_TracedLifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedsendobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSendObjectAction)


def test_uml_tracedsendobjectaction_constructor_exists():
    assert callable(uml_TracedSendObjectAction.__init__)


def test_uml_tracedsendobjectaction_constructor_args():
    sig = inspect.signature(uml_TracedSendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconnectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConnectableElementTemplateParameter)


def test_uml_tracedconnectableelementtemplateparameter_constructor_exists():
    assert callable(uml_TracedConnectableElementTemplateParameter.__init__)


def test_uml_tracedconnectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(uml_TracedConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcallevent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCallEvent)


def test_uml_tracedcallevent_constructor_exists():
    assert callable(uml_TracedCallEvent.__init__)


def test_uml_tracedcallevent_constructor_args():
    sig = inspect.signature(uml_TracedCallEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstartclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStartClassifierBehaviorAction)


def test_uml_tracedstartclassifierbehavioraction_constructor_exists():
    assert callable(uml_TracedStartClassifierBehaviorAction.__init__)


def test_uml_tracedstartclassifierbehavioraction_constructor_args():
    sig = inspect.signature(uml_TracedStartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedrealization_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRealization)


def test_uml_tracedrealization_constructor_exists():
    assert callable(uml_TracedRealization.__init__)


def test_uml_tracedrealization_constructor_args():
    sig = inspect.signature(uml_TracedRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcreatelinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCreateLinkObjectAction)


def test_uml_tracedcreatelinkobjectaction_constructor_exists():
    assert callable(uml_TracedCreateLinkObjectAction.__init__)


def test_uml_tracedcreatelinkobjectaction_constructor_args():
    sig = inspect.signature(uml_TracedCreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedcontroltoken_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedControlToken)


def test_intermediateactivities_tracedcontroltoken_constructor_exists():
    assert callable(IntermediateActivities_TracedControlToken.__init__)


def test_intermediateactivities_tracedcontroltoken_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedControlToken.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtimeobservation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTimeObservation)


def test_uml_tracedtimeobservation_constructor_exists():
    assert callable(uml_TracedTimeObservation.__init__)


def test_uml_tracedtimeobservation_constructor_args():
    sig = inspect.signature(uml_TracedTimeObservation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedextensionend_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExtensionEnd)


def test_uml_tracedextensionend_constructor_exists():
    assert callable(uml_TracedExtensionEnd.__init__)


def test_uml_tracedextensionend_constructor_args():
    sig = inspect.signature(uml_TracedExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcomponent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedComponent)


def test_uml_tracedcomponent_constructor_exists():
    assert callable(uml_TracedComponent.__init__)


def test_uml_tracedcomponent_constructor_args():
    sig = inspect.signature(uml_TracedComponent.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedanyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAnyReceiveEvent)


def test_uml_tracedanyreceiveevent_constructor_exists():
    assert callable(uml_TracedAnyReceiveEvent.__init__)


def test_uml_tracedanyreceiveevent_constructor_args():
    sig = inspect.signature(uml_TracedAnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadLinkObjectEndAction)


def test_uml_tracedreadlinkobjectendaction_constructor_exists():
    assert callable(uml_TracedReadLinkObjectEndAction.__init__)


def test_uml_tracedreadlinkobjectendaction_constructor_args():
    sig = inspect.signature(uml_TracedReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconditionalnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConditionalNode)


def test_uml_tracedconditionalnode_constructor_exists():
    assert callable(uml_TracedConditionalNode.__init__)


def test_uml_tracedconditionalnode_constructor_args():
    sig = inspect.signature(uml_TracedConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinterface_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInterface)


def test_uml_tracedinterface_constructor_exists():
    assert callable(uml_TracedInterface.__init__)


def test_uml_tracedinterface_constructor_args():
    sig = inspect.signature(uml_TracedInterface.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstereotype_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStereotype)


def test_uml_tracedstereotype_constructor_exists():
    assert callable(uml_TracedStereotype.__init__)


def test_uml_tracedstereotype_constructor_args():
    sig = inspect.signature(uml_TracedStereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedliteralstring_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLiteralString)


def test_uml_tracedliteralstring_constructor_exists():
    assert callable(uml_TracedLiteralString.__init__)


def test_uml_tracedliteralstring_constructor_args():
    sig = inspect.signature(uml_TracedLiteralString.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinteraction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInteraction)


def test_uml_tracedinteraction_constructor_exists():
    assert callable(uml_TracedInteraction.__init__)


def test_uml_tracedinteraction_constructor_args():
    sig = inspect.signature(uml_TracedInteraction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedmergenodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedMergeNodeActivation)


def test_intermediateactivities_tracedmergenodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedMergeNodeActivation.__init__)


def test_intermediateactivities_tracedmergenodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedMergeNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstatemachine_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStateMachine)


def test_uml_tracedstatemachine_constructor_exists():
    assert callable(uml_TracedStateMachine.__init__)


def test_uml_tracedstatemachine_constructor_args():
    sig = inspect.signature(uml_TracedStateMachine.__init__)
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



def test_uml_tracedexecutionenvironment_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExecutionEnvironment)


def test_uml_tracedexecutionenvironment_constructor_exists():
    assert callable(uml_TracedExecutionEnvironment.__init__)


def test_uml_tracedexecutionenvironment_constructor_args():
    sig = inspect.signature(uml_TracedExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_loci_tracedlocus_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Loci_TracedLocus)


def test_umltrace_loci_tracedlocus_constructor_exists():
    assert callable(umlTrace_Loci_TracedLocus.__init__)


def test_umltrace_loci_tracedlocus_constructor_args():
    sig = inspect.signature(umlTrace_Loci_TracedLocus.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_loci_tracedexecutionfactory_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Loci_TracedExecutionFactory)


def test_umltrace_loci_tracedexecutionfactory_constructor_exists():
    assert callable(umlTrace_Loci_TracedExecutionFactory.__init__)


def test_umltrace_loci_tracedexecutionfactory_constructor_args():
    sig = inspect.signature(umlTrace_Loci_TracedExecutionFactory.__init__)
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



def test_tracedactionactivation_is_not_abstract():
    assert not inspect.isabstract(TracedActionActivation)


def test_tracedactionactivation_constructor_exists():
    assert callable(TracedActionActivation.__init__)


def test_tracedactionactivation_constructor_args():
    sig = inspect.signature(TracedActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactions_tracedcreateobjectactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActions_TracedCreateObjectActionActivation)


def test_umltrace_intermediateactions_tracedcreateobjectactionactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActions_TracedCreateObjectActionActivation.__init__)


def test_umltrace_intermediateactions_tracedcreateobjectactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActions_TracedCreateObjectActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicactions_tracedinvocationactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicActions_TracedInvocationActionActivation)


def test_umltrace_basicactions_tracedinvocationactionactivation_constructor_exists():
    assert callable(umlTrace_BasicActions_TracedInvocationActionActivation.__init__)


def test_umltrace_basicactions_tracedinvocationactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_BasicActions_TracedInvocationActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicactions_tracedopaqueactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicActions_TracedOpaqueActionActivation)


def test_umltrace_basicactions_tracedopaqueactionactivation_constructor_exists():
    assert callable(umlTrace_BasicActions_TracedOpaqueActionActivation.__init__)


def test_umltrace_basicactions_tracedopaqueactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_BasicActions_TracedOpaqueActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactions_tracedvaluespecificationactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActions_TracedValueSpecificationActionActivation)


def test_umltrace_intermediateactions_tracedvaluespecificationactionactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActions_TracedValueSpecificationActionActivation.__init__)


def test_umltrace_intermediateactions_tracedvaluespecificationactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActions_TracedValueSpecificationActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactions_tracedstructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation)


def test_umltrace_intermediateactions_tracedstructuralfeatureactionactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation.__init__)


def test_umltrace_intermediateactions_tracedstructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_loci_tracedexecutionenvironment_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Loci_TracedExecutionEnvironment)


def test_umltrace_loci_tracedexecutionenvironment_constructor_exists():
    assert callable(umlTrace_Loci_TracedExecutionEnvironment.__init__)


def test_umltrace_loci_tracedexecutionenvironment_constructor_args():
    sig = inspect.signature(umlTrace_Loci_TracedExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_loci_tracedexecutor_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Loci_TracedExecutor)


def test_umltrace_loci_tracedexecutor_constructor_exists():
    assert callable(umlTrace_Loci_TracedExecutor.__init__)


def test_umltrace_loci_tracedexecutor_constructor_args():
    sig = inspect.signature(umlTrace_Loci_TracedExecutor.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_loci_tracedsemanticvisitor_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Loci_TracedSemanticVisitor)


def test_umltrace_loci_tracedsemanticvisitor_constructor_exists():
    assert callable(umlTrace_Loci_TracedSemanticVisitor.__init__)


def test_umltrace_loci_tracedsemanticvisitor_constructor_args():
    sig = inspect.signature(umlTrace_Loci_TracedSemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedactivityedgeinstance_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedActivityEdgeInstance)


def test_umltrace_intermediateactivities_tracedactivityedgeinstance_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedActivityEdgeInstance.__init__)


def test_umltrace_intermediateactivities_tracedactivityedgeinstance_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedActivityEdgeInstance.__init__)
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



def test_umltrace_intermediateactivities_tracedoffer_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedOffer)


def test_umltrace_intermediateactivities_tracedoffer_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedOffer.__init__)


def test_umltrace_intermediateactivities_tracedoffer_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedOffer.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedtoken_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedToken)


def test_umltrace_intermediateactivities_tracedtoken_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedToken.__init__)


def test_umltrace_intermediateactivities_tracedtoken_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedactivitynodeactivationgroup_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup)


def test_umltrace_intermediateactivities_tracedactivitynodeactivationgroup_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup.__init__)


def test_umltrace_intermediateactivities_tracedactivitynodeactivationgroup_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivitynodeactivation_is_not_abstract():
    assert not inspect.isabstract(TracedActivityNodeActivation)


def test_tracedactivitynodeactivation_constructor_exists():
    assert callable(TracedActivityNodeActivation.__init__)


def test_tracedactivitynodeactivation_constructor_args():
    sig = inspect.signature(TracedActivityNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedcontrolnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedControlNodeActivation)


def test_umltrace_intermediateactivities_tracedcontrolnodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedControlNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedcontrolnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedControlNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_basicactions_tracedactionactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicActions_TracedActionActivation)


def test_umltrace_basicactions_tracedactionactivation_constructor_exists():
    assert callable(umlTrace_BasicActions_TracedActionActivation.__init__)


def test_umltrace_basicactions_tracedactionactivation_constructor_args():
    sig = inspect.signature(umlTrace_BasicActions_TracedActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedobjectnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedObjectNodeActivation)


def test_umltrace_intermediateactivities_tracedobjectnodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedObjectNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedobjectnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedObjectNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedcontrolnodeactivation_is_not_abstract():
    assert not inspect.isabstract(TracedControlNodeActivation)


def test_tracedcontrolnodeactivation_constructor_exists():
    assert callable(TracedControlNodeActivation.__init__)


def test_tracedcontrolnodeactivation_constructor_args():
    sig = inspect.signature(TracedControlNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedactivityfinalnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation)


def test_umltrace_intermediateactivities_tracedactivityfinalnodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedactivityfinalnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedforknodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedForkNodeActivation)


def test_umltrace_intermediateactivities_tracedforknodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedForkNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedforknodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedForkNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedinitialnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedInitialNodeActivation)


def test_umltrace_intermediateactivities_tracedinitialnodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedInitialNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedinitialnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedInitialNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedjoinnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedJoinNodeActivation)


def test_umltrace_intermediateactivities_tracedjoinnodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedJoinNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedjoinnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedJoinNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_tracedtoken_is_not_abstract():
    assert not inspect.isabstract(TracedToken)


def test_tracedtoken_constructor_exists():
    assert callable(TracedToken.__init__)


def test_tracedtoken_constructor_args():
    sig = inspect.signature(TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedforkedtoken_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedForkedToken)


def test_umltrace_intermediateactivities_tracedforkedtoken_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedForkedToken.__init__)


def test_umltrace_intermediateactivities_tracedforkedtoken_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedForkedToken.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_traceddecisionnodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedDecisionNodeActivation)


def test_umltrace_intermediateactivities_traceddecisionnodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedDecisionNodeActivation.__init__)


def test_umltrace_intermediateactivities_traceddecisionnodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedDecisionNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedobjecttoken_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedObjectToken)


def test_umltrace_intermediateactivities_tracedobjecttoken_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedObjectToken.__init__)


def test_umltrace_intermediateactivities_tracedobjecttoken_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedObjectToken.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedcontroltoken_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedControlToken)


def test_umltrace_intermediateactivities_tracedcontroltoken_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedControlToken.__init__)


def test_umltrace_intermediateactivities_tracedcontroltoken_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedControlToken.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_intermediateactivities_tracedmergenodeactivation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_IntermediateActivities_TracedMergeNodeActivation)


def test_umltrace_intermediateactivities_tracedmergenodeactivation_constructor_exists():
    assert callable(umlTrace_IntermediateActivities_TracedMergeNodeActivation.__init__)


def test_umltrace_intermediateactivities_tracedmergenodeactivation_constructor_args():
    sig = inspect.signature(umlTrace_IntermediateActivities_TracedMergeNodeActivation.__init__)
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



def test_umltrace_kernel_tracedfeaturevalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedFeatureValue)


def test_umltrace_kernel_tracedfeaturevalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedFeatureValue.__init__)


def test_umltrace_kernel_tracedfeaturevalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedFeatureValue.__init__)
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



def test_umltrace_basicbehaviors_tracedparametervalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicBehaviors_TracedParameterValue)


def test_umltrace_basicbehaviors_tracedparametervalue_constructor_exists():
    assert callable(umlTrace_BasicBehaviors_TracedParameterValue.__init__)


def test_umltrace_basicbehaviors_tracedparametervalue_constructor_args():
    sig = inspect.signature(umlTrace_BasicBehaviors_TracedParameterValue.__init__)
    params = list(sig.parameters.keys())



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



def test_umltrace_basicbehaviors_tracedopaquebehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution)


def test_umltrace_basicbehaviors_tracedopaquebehaviorexecution_constructor_exists():
    assert callable(umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution.__init__)


def test_umltrace_basicbehaviors_tracedopaquebehaviorexecution_constructor_args():
    sig = inspect.signature(umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution.__init__)
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



def test_umltrace_kernel_tracedvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedValue)


def test_umltrace_kernel_tracedvalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedValue.__init__)


def test_umltrace_kernel_tracedvalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedValue.__init__)
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



def test_tracedprimitivevalue_is_not_abstract():
    assert not inspect.isabstract(TracedPrimitiveValue)


def test_tracedprimitivevalue_constructor_exists():
    assert callable(TracedPrimitiveValue.__init__)


def test_tracedprimitivevalue_constructor_args():
    sig = inspect.signature(TracedPrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedintegervalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedIntegerValue)


def test_umltrace_kernel_tracedintegervalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedIntegerValue.__init__)


def test_umltrace_kernel_tracedintegervalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedIntegerValue.__init__)
    params = list(sig.parameters.keys())



def test_tracedstructuredvalue_is_not_abstract():
    assert not inspect.isabstract(TracedStructuredValue)


def test_tracedstructuredvalue_constructor_exists():
    assert callable(TracedStructuredValue.__init__)


def test_tracedstructuredvalue_constructor_args():
    sig = inspect.signature(TracedStructuredValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedcompoundvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedCompoundValue)


def test_umltrace_kernel_tracedcompoundvalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedCompoundValue.__init__)


def test_umltrace_kernel_tracedcompoundvalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedCompoundValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedreference_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedReference)


def test_umltrace_kernel_tracedreference_constructor_exists():
    assert callable(umlTrace_Kernel_TracedReference.__init__)


def test_umltrace_kernel_tracedreference_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedReference.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedstructuredvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedStructuredValue)


def test_umltrace_kernel_tracedstructuredvalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedStructuredValue.__init__)


def test_umltrace_kernel_tracedstructuredvalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedStructuredValue.__init__)
    params = list(sig.parameters.keys())



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



def test_umltrace_kernel_tracedbooleanvalue_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedBooleanValue)


def test_umltrace_kernel_tracedbooleanvalue_constructor_exists():
    assert callable(umlTrace_Kernel_TracedBooleanValue.__init__)


def test_umltrace_kernel_tracedbooleanvalue_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedBooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_kernel_tracedevaluation_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Kernel_TracedEvaluation)


def test_umltrace_kernel_tracedevaluation_constructor_exists():
    assert callable(umlTrace_Kernel_TracedEvaluation.__init__)


def test_umltrace_kernel_tracedevaluation_constructor_args():
    sig = inspect.signature(umlTrace_Kernel_TracedEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedbehaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedBehaviorExecutionSpecification)


def test_uml_tracedbehaviorexecutionspecification_constructor_exists():
    assert callable(uml_TracedBehaviorExecutionSpecification.__init__)


def test_uml_tracedbehaviorexecutionspecification_constructor_args():
    sig = inspect.signature(uml_TracedBehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactor_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActor)


def test_uml_tracedactor_constructor_exists():
    assert callable(uml_TracedActor.__init__)


def test_uml_tracedactor_constructor_args():
    sig = inspect.signature(uml_TracedActor.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddeploymentspecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDeploymentSpecification)


def test_uml_traceddeploymentspecification_constructor_exists():
    assert callable(uml_TracedDeploymentSpecification.__init__)


def test_uml_traceddeploymentspecification_constructor_args():
    sig = inspect.signature(uml_TracedDeploymentSpecification.__init__)
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



def test_uml_tracedcentralbuffernode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCentralBufferNode)


def test_uml_tracedcentralbuffernode_constructor_exists():
    assert callable(uml_TracedCentralBufferNode.__init__)


def test_uml_tracedcentralbuffernode_constructor_args():
    sig = inspect.signature(uml_TracedCentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedunmarshallaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedUnmarshallAction)


def test_uml_tracedunmarshallaction_constructor_exists():
    assert callable(uml_TracedUnmarshallAction.__init__)


def test_uml_tracedunmarshallaction_constructor_args():
    sig = inspect.signature(uml_TracedUnmarshallAction.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedliteralintegerevaluation_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedLiteralIntegerEvaluation)


def test_kernel_tracedliteralintegerevaluation_constructor_exists():
    assert callable(Kernel_TracedLiteralIntegerEvaluation.__init__)


def test_kernel_tracedliteralintegerevaluation_constructor_args():
    sig = inspect.signature(Kernel_TracedLiteralIntegerEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedclearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedClearStructuralFeatureAction)


def test_uml_tracedclearstructuralfeatureaction_constructor_exists():
    assert callable(uml_TracedClearStructuralFeatureAction.__init__)


def test_uml_tracedclearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml_TracedClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedfunctionbehavior_is_not_abstract():
    assert not inspect.isabstract(uml_TracedFunctionBehavior)


def test_uml_tracedfunctionbehavior_constructor_exists():
    assert callable(uml_TracedFunctionBehavior.__init__)


def test_uml_tracedfunctionbehavior_constructor_args():
    sig = inspect.signature(uml_TracedFunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedopaqueexpression_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOpaqueExpression)


def test_uml_tracedopaqueexpression_constructor_exists():
    assert callable(uml_TracedOpaqueExpression.__init__)


def test_uml_tracedopaqueexpression_constructor_args():
    sig = inspect.signature(uml_TracedOpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtemplatebinding_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTemplateBinding)


def test_uml_tracedtemplatebinding_constructor_exists():
    assert callable(uml_TracedTemplateBinding.__init__)


def test_uml_tracedtemplatebinding_constructor_args():
    sig = inspect.signature(uml_TracedTemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedlinkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLinkEndCreationData)


def test_uml_tracedlinkendcreationdata_constructor_exists():
    assert callable(uml_TracedLinkEndCreationData.__init__)


def test_uml_tracedlinkendcreationdata_constructor_args():
    sig = inspect.signature(uml_TracedLinkEndCreationData.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActionExecutionSpecification)


def test_uml_tracedactionexecutionspecification_constructor_exists():
    assert callable(uml_TracedActionExecutionSpecification.__init__)


def test_uml_tracedactionexecutionspecification_constructor_args():
    sig = inspect.signature(uml_TracedActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconnectionpointreference_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConnectionPointReference)


def test_uml_tracedconnectionpointreference_constructor_exists():
    assert callable(uml_TracedConnectionPointReference.__init__)


def test_uml_tracedconnectionpointreference_constructor_args():
    sig = inspect.signature(uml_TracedConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactivity_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivity)


def test_uml_tracedactivity_constructor_exists():
    assert callable(uml_TracedActivity.__init__)


def test_uml_tracedactivity_constructor_args():
    sig = inspect.signature(uml_TracedActivity.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedacceptcallaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAcceptCallAction)


def test_uml_tracedacceptcallaction_constructor_exists():
    assert callable(uml_TracedAcceptCallAction.__init__)


def test_uml_tracedacceptcallaction_constructor_args():
    sig = inspect.signature(uml_TracedAcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadselfaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadSelfAction)


def test_uml_tracedreadselfaction_constructor_exists():
    assert callable(uml_TracedReadSelfAction.__init__)


def test_uml_tracedreadselfaction_constructor_args():
    sig = inspect.signature(uml_TracedReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedgate_is_not_abstract():
    assert not inspect.isabstract(uml_TracedGate)


def test_uml_tracedgate_constructor_exists():
    assert callable(uml_TracedGate.__init__)


def test_uml_tracedgate_constructor_args():
    sig = inspect.signature(uml_TracedGate.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedsubstitution_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSubstitution)


def test_uml_tracedsubstitution_constructor_exists():
    assert callable(uml_TracedSubstitution.__init__)


def test_uml_tracedsubstitution_constructor_args():
    sig = inspect.signature(uml_TracedSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddevice_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDevice)


def test_uml_traceddevice_constructor_exists():
    assert callable(uml_TracedDevice.__init__)


def test_uml_traceddevice_constructor_args():
    sig = inspect.signature(uml_TracedDevice.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReclassifyObjectAction)


def test_uml_tracedreclassifyobjectaction_constructor_exists():
    assert callable(uml_TracedReclassifyObjectAction.__init__)


def test_uml_tracedreclassifyobjectaction_constructor_args():
    sig = inspect.signature(uml_TracedReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcallbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCallBehaviorAction)


def test_uml_tracedcallbehavioraction_constructor_exists():
    assert callable(uml_TracedCallBehaviorAction.__init__)


def test_uml_tracedcallbehavioraction_constructor_args():
    sig = inspect.signature(uml_TracedCallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedgeneralordering_is_not_abstract():
    assert not inspect.isabstract(uml_TracedGeneralOrdering)


def test_uml_tracedgeneralordering_constructor_exists():
    assert callable(uml_TracedGeneralOrdering.__init__)


def test_uml_tracedgeneralordering_constructor_args():
    sig = inspect.signature(uml_TracedGeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstateinvariant_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStateInvariant)


def test_uml_tracedstateinvariant_constructor_exists():
    assert callable(uml_TracedStateInvariant.__init__)


def test_uml_tracedstateinvariant_constructor_args():
    sig = inspect.signature(uml_TracedStateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedassociation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAssociation)


def test_uml_tracedassociation_constructor_exists():
    assert callable(uml_TracedAssociation.__init__)


def test_uml_tracedassociation_constructor_args():
    sig = inspect.signature(uml_TracedAssociation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinteractionuse_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInteractionUse)


def test_uml_tracedinteractionuse_constructor_exists():
    assert callable(uml_TracedInteractionUse.__init__)


def test_uml_tracedinteractionuse_constructor_args():
    sig = inspect.signature(uml_TracedInteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedvariable_is_not_abstract():
    assert not inspect.isabstract(uml_TracedVariable)


def test_uml_tracedvariable_constructor_exists():
    assert callable(uml_TracedVariable.__init__)


def test_uml_tracedvariable_constructor_args():
    sig = inspect.signature(uml_TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedremovevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRemoveVariableValueAction)


def test_uml_tracedremovevariablevalueaction_constructor_exists():
    assert callable(uml_TracedRemoveVariableValueAction.__init__)


def test_uml_tracedremovevariablevalueaction_constructor_args():
    sig = inspect.signature(uml_TracedRemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedliteralreal_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLiteralReal)


def test_uml_tracedliteralreal_constructor_exists():
    assert callable(uml_TracedLiteralReal.__init__)


def test_uml_tracedliteralreal_constructor_args():
    sig = inspect.signature(uml_TracedLiteralReal.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedexecutionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExecutionOccurrenceSpecification)


def test_uml_tracedexecutionoccurrencespecification_constructor_exists():
    assert callable(uml_TracedExecutionOccurrenceSpecification.__init__)


def test_uml_tracedexecutionoccurrencespecification_constructor_args():
    sig = inspect.signature(uml_TracedExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedpackageimport_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPackageImport)


def test_uml_tracedpackageimport_constructor_exists():
    assert callable(uml_TracedPackageImport.__init__)


def test_uml_tracedpackageimport_constructor_args():
    sig = inspect.signature(uml_TracedPackageImport.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedexceptionhandler_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExceptionHandler)


def test_uml_tracedexceptionhandler_constructor_exists():
    assert callable(uml_TracedExceptionHandler.__init__)


def test_uml_tracedexceptionhandler_constructor_args():
    sig = inspect.signature(uml_TracedExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtestidentityaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTestIdentityAction)


def test_uml_tracedtestidentityaction_constructor_exists():
    assert callable(uml_TracedTestIdentityAction.__init__)


def test_uml_tracedtestidentityaction_constructor_args():
    sig = inspect.signature(uml_TracedTestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedclearassociationaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedClearAssociationAction)


def test_uml_tracedclearassociationaction_constructor_exists():
    assert callable(uml_TracedClearAssociationAction.__init__)


def test_uml_tracedclearassociationaction_constructor_args():
    sig = inspect.signature(uml_TracedClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedaddvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAddVariableValueAction)


def test_uml_tracedaddvariablevalueaction_constructor_exists():
    assert callable(uml_TracedAddVariableValueAction.__init__)


def test_uml_tracedaddvariablevalueaction_constructor_args():
    sig = inspect.signature(uml_TracedAddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedoperation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOperation)


def test_uml_tracedoperation_constructor_exists():
    assert callable(uml_TracedOperation.__init__)


def test_uml_tracedoperation_constructor_args():
    sig = inspect.signature(uml_TracedOperation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcontrolflow_is_not_abstract():
    assert not inspect.isabstract(uml_TracedControlFlow)


def test_uml_tracedcontrolflow_constructor_exists():
    assert callable(uml_TracedControlFlow.__init__)


def test_uml_tracedcontrolflow_constructor_args():
    sig = inspect.signature(uml_TracedControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedexpansionnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExpansionNode)


def test_uml_tracedexpansionnode_constructor_exists():
    assert callable(uml_TracedExpansionNode.__init__)


def test_uml_tracedexpansionnode_constructor_args():
    sig = inspect.signature(uml_TracedExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedliteralnull_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLiteralNull)


def test_uml_tracedliteralnull_constructor_exists():
    assert callable(uml_TracedLiteralNull.__init__)


def test_uml_tracedliteralnull_constructor_args():
    sig = inspect.signature(uml_TracedLiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcomment_is_not_abstract():
    assert not inspect.isabstract(uml_TracedComment)


def test_uml_tracedcomment_constructor_exists():
    assert callable(uml_TracedComment.__init__)


def test_uml_tracedcomment_constructor_args():
    sig = inspect.signature(uml_TracedComment.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedsignal_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSignal)


def test_uml_tracedsignal_constructor_exists():
    assert callable(uml_TracedSignal.__init__)


def test_uml_tracedsignal_constructor_args():
    sig = inspect.signature(uml_TracedSignal.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedraiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRaiseExceptionAction)


def test_uml_tracedraiseexceptionaction_constructor_exists():
    assert callable(uml_TracedRaiseExceptionAction.__init__)


def test_uml_tracedraiseexceptionaction_constructor_args():
    sig = inspect.signature(uml_TracedRaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreception_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReception)


def test_uml_tracedreception_constructor_exists():
    assert callable(uml_TracedReception.__init__)


def test_uml_tracedreception_constructor_args():
    sig = inspect.signature(uml_TracedReception.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedforknode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedForkNode)


def test_uml_tracedforknode_constructor_exists():
    assert callable(uml_TracedForkNode.__init__)


def test_uml_tracedforknode_constructor_args():
    sig = inspect.signature(uml_TracedForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmodel_is_not_abstract():
    assert not inspect.isabstract(uml_TracedModel)


def test_uml_tracedmodel_constructor_exists():
    assert callable(uml_TracedModel.__init__)


def test_uml_tracedmodel_constructor_args():
    sig = inspect.signature(uml_TracedModel.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedpackagemerge_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPackageMerge)


def test_uml_tracedpackagemerge_constructor_exists():
    assert callable(uml_TracedPackageMerge.__init__)


def test_uml_tracedpackagemerge_constructor_args():
    sig = inspect.signature(uml_TracedPackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracednode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedNode)


def test_uml_tracednode_constructor_exists():
    assert callable(uml_TracedNode.__init__)


def test_uml_tracednode_constructor_args():
    sig = inspect.signature(uml_TracedNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddestroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDestroyObjectAction)


def test_uml_traceddestroyobjectaction_constructor_exists():
    assert callable(uml_TracedDestroyObjectAction.__init__)


def test_uml_traceddestroyobjectaction_constructor_args():
    sig = inspect.signature(uml_TracedDestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedchangeevent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedChangeEvent)


def test_uml_tracedchangeevent_constructor_exists():
    assert callable(uml_TracedChangeEvent.__init__)


def test_uml_tracedchangeevent_constructor_args():
    sig = inspect.signature(uml_TracedChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedobjectflow_is_not_abstract():
    assert not inspect.isabstract(uml_TracedObjectFlow)


def test_uml_tracedobjectflow_constructor_exists():
    assert callable(uml_TracedObjectFlow.__init__)


def test_uml_tracedobjectflow_constructor_args():
    sig = inspect.signature(uml_TracedObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_tracedinputpinactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TracedInputPinActivation)


def test_basicactions_tracedinputpinactivation_constructor_exists():
    assert callable(BasicActions_TracedInputPinActivation.__init__)


def test_basicactions_tracedinputpinactivation_constructor_args():
    sig = inspect.signature(BasicActions_TracedInputPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadextentaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadExtentAction)


def test_uml_tracedreadextentaction_constructor_exists():
    assert callable(uml_TracedReadExtentAction.__init__)


def test_uml_tracedreadextentaction_constructor_args():
    sig = inspect.signature(uml_TracedReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmanifestation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedManifestation)


def test_uml_tracedmanifestation_constructor_exists():
    assert callable(uml_TracedManifestation.__init__)


def test_uml_tracedmanifestation_constructor_args():
    sig = inspect.signature(uml_TracedManifestation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedlinkenddata_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLinkEndData)


def test_uml_tracedlinkenddata_constructor_exists():
    assert callable(uml_TracedLinkEndData.__init__)


def test_uml_tracedlinkenddata_constructor_args():
    sig = inspect.signature(uml_TracedLinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtransition_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTransition)


def test_uml_tracedtransition_constructor_exists():
    assert callable(uml_TracedTransition.__init__)


def test_uml_tracedtransition_constructor_args():
    sig = inspect.signature(uml_TracedTransition.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinstancevalue_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInstanceValue)


def test_uml_tracedinstancevalue_constructor_exists():
    assert callable(uml_TracedInstanceValue.__init__)


def test_uml_tracedinstancevalue_constructor_args():
    sig = inspect.signature(uml_TracedInstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedclause_is_not_abstract():
    assert not inspect.isabstract(uml_TracedClause)


def test_uml_tracedclause_constructor_exists():
    assert callable(uml_TracedClause.__init__)


def test_uml_tracedclause_constructor_args():
    sig = inspect.signature(uml_TracedClause.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcombinedfragment_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCombinedFragment)


def test_uml_tracedcombinedfragment_constructor_exists():
    assert callable(uml_TracedCombinedFragment.__init__)


def test_uml_tracedcombinedfragment_constructor_args():
    sig = inspect.signature(uml_TracedCombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_tracedcreateobjectactionactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_TracedCreateObjectActionActivation)


def test_intermediateactions_tracedcreateobjectactionactivation_constructor_exists():
    assert callable(IntermediateActions_TracedCreateObjectActionActivation.__init__)


def test_intermediateactions_tracedcreateobjectactionactivation_constructor_args():
    sig = inspect.signature(IntermediateActions_TracedCreateObjectActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreplyaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReplyAction)


def test_uml_tracedreplyaction_constructor_exists():
    assert callable(uml_TracedReplyAction.__init__)


def test_uml_tracedreplyaction_constructor_args():
    sig = inspect.signature(uml_TracedReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtimeexpression_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTimeExpression)


def test_uml_tracedtimeexpression_constructor_exists():
    assert callable(uml_TracedTimeExpression.__init__)


def test_uml_tracedtimeexpression_constructor_args():
    sig = inspect.signature(uml_TracedTimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddependency_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDependency)


def test_uml_traceddependency_constructor_exists():
    assert callable(uml_TracedDependency.__init__)


def test_uml_traceddependency_constructor_args():
    sig = inspect.signature(uml_TracedDependency.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinformationflow_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInformationFlow)


def test_uml_tracedinformationflow_constructor_exists():
    assert callable(uml_TracedInformationFlow.__init__)


def test_uml_tracedinformationflow_constructor_args():
    sig = inspect.signature(uml_TracedInformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinteractionoperand_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInteractionOperand)


def test_uml_tracedinteractionoperand_constructor_exists():
    assert callable(uml_TracedInteractionOperand.__init__)


def test_uml_tracedinteractionoperand_constructor_args():
    sig = inspect.signature(uml_TracedInteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_integerfunctions_tracedintegerplusfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution)


def test_integerfunctions_tracedintegerplusfunctionbehaviorexecution_constructor_exists():
    assert callable(IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution.__init__)


def test_integerfunctions_tracedintegerplusfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedfinalstate_is_not_abstract():
    assert not inspect.isabstract(uml_TracedFinalState)


def test_uml_tracedfinalstate_constructor_exists():
    assert callable(uml_TracedFinalState.__init__)


def test_uml_tracedfinalstate_constructor_args():
    sig = inspect.signature(uml_TracedFinalState.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedusecase_is_not_abstract():
    assert not inspect.isabstract(uml_TracedUseCase)


def test_uml_tracedusecase_constructor_exists():
    assert callable(uml_TracedUseCase.__init__)


def test_uml_tracedusecase_constructor_args():
    sig = inspect.signature(uml_TracedUseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedpseudostate_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPseudostate)


def test_uml_tracedpseudostate_constructor_exists():
    assert callable(uml_TracedPseudostate.__init__)


def test_uml_tracedpseudostate_constructor_args():
    sig = inspect.signature(uml_TracedPseudostate.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedregion_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRegion)


def test_uml_tracedregion_constructor_exists():
    assert callable(uml_TracedRegion.__init__)


def test_uml_tracedregion_constructor_args():
    sig = inspect.signature(uml_TracedRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedvaluespecificationaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedValueSpecificationAction)


def test_uml_tracedvaluespecificationaction_constructor_exists():
    assert callable(uml_TracedValueSpecificationAction.__init__)


def test_uml_tracedvaluespecificationaction_constructor_args():
    sig = inspect.signature(uml_TracedValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddecisionnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDecisionNode)


def test_uml_traceddecisionnode_constructor_exists():
    assert callable(uml_TracedDecisionNode.__init__)


def test_uml_traceddecisionnode_constructor_args():
    sig = inspect.signature(uml_TracedDecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedactivityparameternodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedActivityParameterNodeActivation)


def test_intermediateactivities_tracedactivityparameternodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedActivityParameterNodeActivation.__init__)


def test_intermediateactivities_tracedactivityparameternodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedActivityParameterNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddestroylinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDestroyLinkAction)


def test_uml_traceddestroylinkaction_constructor_exists():
    assert callable(uml_TracedDestroyLinkAction.__init__)


def test_uml_traceddestroylinkaction_constructor_args():
    sig = inspect.signature(uml_TracedDestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinterruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInterruptibleActivityRegion)


def test_uml_tracedinterruptibleactivityregion_constructor_exists():
    assert callable(uml_TracedInterruptibleActivityRegion.__init__)


def test_uml_tracedinterruptibleactivityregion_constructor_args():
    sig = inspect.signature(uml_TracedInterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadIsClassifiedObjectAction)


def test_uml_tracedreadisclassifiedobjectaction_constructor_exists():
    assert callable(uml_TracedReadIsClassifiedObjectAction.__init__)


def test_uml_tracedreadisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(uml_TracedReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution)


def test_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_constructor_exists():
    assert callable(IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution.__init__)


def test_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedvaluepin_is_not_abstract():
    assert not inspect.isabstract(uml_TracedValuePin)


def test_uml_tracedvaluepin_constructor_exists():
    assert callable(uml_TracedValuePin.__init__)


def test_uml_tracedvaluepin_constructor_args():
    sig = inspect.signature(uml_TracedValuePin.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinstancespecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInstanceSpecification)


def test_uml_tracedinstancespecification_constructor_exists():
    assert callable(uml_TracedInstanceSpecification.__init__)


def test_uml_tracedinstancespecification_constructor_args():
    sig = inspect.signature(uml_TracedInstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedoutputpin_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOutputPin)


def test_uml_tracedoutputpin_constructor_exists():
    assert callable(uml_TracedOutputPin.__init__)


def test_uml_tracedoutputpin_constructor_args():
    sig = inspect.signature(uml_TracedOutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedprotocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(uml_TracedProtocolStateMachine)


def test_uml_tracedprotocolstatemachine_constructor_exists():
    assert callable(uml_TracedProtocolStateMachine.__init__)


def test_uml_tracedprotocolstatemachine_constructor_args():
    sig = inspect.signature(uml_TracedProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedforknodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedForkNodeActivation)


def test_intermediateactivities_tracedforknodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedForkNodeActivation.__init__)


def test_intermediateactivities_tracedforknodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedForkNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinterval_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInterval)


def test_uml_tracedinterval_constructor_exists():
    assert callable(uml_TracedInterval.__init__)


def test_uml_tracedinterval_constructor_args():
    sig = inspect.signature(uml_TracedInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedprofile_is_not_abstract():
    assert not inspect.isabstract(uml_TracedProfile)


def test_uml_tracedprofile_constructor_exists():
    assert callable(uml_TracedProfile.__init__)


def test_uml_tracedprofile_constructor_args():
    sig = inspect.signature(uml_TracedProfile.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcalloperationaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCallOperationAction)


def test_uml_tracedcalloperationaction_constructor_exists():
    assert callable(uml_TracedCallOperationAction.__init__)


def test_uml_tracedcalloperationaction_constructor_args():
    sig = inspect.signature(uml_TracedCallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtrigger_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTrigger)


def test_uml_tracedtrigger_constructor_exists():
    assert callable(uml_TracedTrigger.__init__)


def test_uml_tracedtrigger_constructor_args():
    sig = inspect.signature(uml_TracedTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedintervalconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_TracedIntervalConstraint)


def test_uml_tracedintervalconstraint_constructor_exists():
    assert callable(uml_TracedIntervalConstraint.__init__)


def test_uml_tracedintervalconstraint_constructor_args():
    sig = inspect.signature(uml_TracedIntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedimage_is_not_abstract():
    assert not inspect.isabstract(uml_TracedImage)


def test_uml_tracedimage_constructor_exists():
    assert callable(uml_TracedImage.__init__)


def test_uml_tracedimage_constructor_args():
    sig = inspect.signature(uml_TracedImage.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddurationconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDurationConstraint)


def test_uml_traceddurationconstraint_constructor_exists():
    assert callable(uml_TracedDurationConstraint.__init__)


def test_uml_traceddurationconstraint_constructor_args():
    sig = inspect.signature(uml_TracedDurationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmessageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedMessageOccurrenceSpecification)


def test_uml_tracedmessageoccurrencespecification_constructor_exists():
    assert callable(uml_TracedMessageOccurrenceSpecification.__init__)


def test_uml_tracedmessageoccurrencespecification_constructor_args():
    sig = inspect.signature(uml_TracedMessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconnectorend_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConnectorEnd)


def test_uml_tracedconnectorend_constructor_exists():
    assert callable(uml_TracedConnectorEnd.__init__)


def test_uml_tracedconnectorend_constructor_args():
    sig = inspect.signature(uml_TracedConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTemplateParameter)


def test_uml_tracedtemplateparameter_constructor_exists():
    assert callable(uml_TracedTemplateParameter.__init__)


def test_uml_tracedtemplateparameter_constructor_args():
    sig = inspect.signature(uml_TracedTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactioninputpin_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActionInputPin)


def test_uml_tracedactioninputpin_constructor_exists():
    assert callable(uml_TracedActionInputPin.__init__)


def test_uml_tracedactioninputpin_constructor_args():
    sig = inspect.signature(uml_TracedActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedclearvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedClearVariableAction)


def test_uml_tracedclearvariableaction_constructor_exists():
    assert callable(uml_TracedClearVariableAction.__init__)


def test_uml_tracedclearvariableaction_constructor_args():
    sig = inspect.signature(uml_TracedClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedliteralinteger_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLiteralInteger)


def test_uml_tracedliteralinteger_constructor_exists():
    assert callable(uml_TracedLiteralInteger.__init__)


def test_uml_tracedliteralinteger_constructor_args():
    sig = inspect.signature(uml_TracedLiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinitialnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInitialNode)


def test_uml_tracedinitialnode_constructor_exists():
    assert callable(uml_TracedInitialNode.__init__)


def test_uml_tracedinitialnode_constructor_args():
    sig = inspect.signature(uml_TracedInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedprofileapplication_is_not_abstract():
    assert not inspect.isabstract(uml_TracedProfileApplication)


def test_uml_tracedprofileapplication_constructor_exists():
    assert callable(uml_TracedProfileApplication.__init__)


def test_uml_tracedprofileapplication_constructor_args():
    sig = inspect.signature(uml_TracedProfileApplication.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_traceddecisionnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedDecisionNodeActivation)


def test_intermediateactivities_traceddecisionnodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedDecisionNodeActivation.__init__)


def test_intermediateactivities_traceddecisionnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedDecisionNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadvariableaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadVariableAction)


def test_uml_tracedreadvariableaction_constructor_exists():
    assert callable(uml_TracedReadVariableAction.__init__)


def test_uml_tracedreadvariableaction_constructor_args():
    sig = inspect.signature(uml_TracedReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedextend_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExtend)


def test_uml_tracedextend_constructor_exists():
    assert callable(uml_TracedExtend.__init__)


def test_uml_tracedextend_constructor_args():
    sig = inspect.signature(uml_TracedExtend.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtemplateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTemplateParameterSubstitution)


def test_uml_tracedtemplateparametersubstitution_constructor_exists():
    assert callable(uml_TracedTemplateParameterSubstitution.__init__)


def test_uml_tracedtemplateparametersubstitution_constructor_args():
    sig = inspect.signature(uml_TracedTemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadLinkObjectEndQualifierAction)


def test_uml_tracedreadlinkobjectendqualifieraction_constructor_exists():
    assert callable(uml_TracedReadLinkObjectEndQualifierAction.__init__)


def test_uml_tracedreadlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(uml_TracedReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedoperationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOperationTemplateParameter)


def test_uml_tracedoperationtemplateparameter_constructor_exists():
    assert callable(uml_TracedOperationTemplateParameter.__init__)


def test_uml_tracedoperationtemplateparameter_constructor_args():
    sig = inspect.signature(uml_TracedOperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedqualifiervalue_is_not_abstract():
    assert not inspect.isabstract(uml_TracedQualifierValue)


def test_uml_tracedqualifiervalue_constructor_exists():
    assert callable(uml_TracedQualifierValue.__init__)


def test_uml_tracedqualifiervalue_constructor_args():
    sig = inspect.signature(uml_TracedQualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedliteralboolean_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLiteralBoolean)


def test_uml_tracedliteralboolean_constructor_exists():
    assert callable(uml_TracedLiteralBoolean.__init__)


def test_uml_tracedliteralboolean_constructor_args():
    sig = inspect.signature(uml_TracedLiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmessage_is_not_abstract():
    assert not inspect.isabstract(uml_TracedMessage)


def test_uml_tracedmessage_constructor_exists():
    assert callable(uml_TracedMessage.__init__)


def test_uml_tracedmessage_constructor_args():
    sig = inspect.signature(uml_TracedMessage.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedredefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRedefinableTemplateSignature)


def test_uml_tracedredefinabletemplatesignature_constructor_exists():
    assert callable(uml_TracedRedefinableTemplateSignature.__init__)


def test_uml_tracedredefinabletemplatesignature_constructor_args():
    sig = inspect.signature(uml_TracedRedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedmergenode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedMergeNode)


def test_uml_tracedmergenode_constructor_exists():
    assert callable(uml_TracedMergeNode.__init__)


def test_uml_tracedmergenode_constructor_args():
    sig = inspect.signature(uml_TracedMergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadStructuralFeatureAction)


def test_uml_tracedreadstructuralfeatureaction_constructor_exists():
    assert callable(uml_TracedReadStructuralFeatureAction.__init__)


def test_uml_tracedreadstructuralfeatureaction_constructor_args():
    sig = inspect.signature(uml_TracedReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedliteralbooleanevaluation_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedLiteralBooleanEvaluation)


def test_kernel_tracedliteralbooleanevaluation_constructor_exists():
    assert callable(Kernel_TracedLiteralBooleanEvaluation.__init__)


def test_kernel_tracedliteralbooleanevaluation_constructor_args():
    sig = inspect.signature(Kernel_TracedLiteralBooleanEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_tracedopaqueactionactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TracedOpaqueActionActivation)


def test_basicactions_tracedopaqueactionactivation_constructor_exists():
    assert callable(BasicActions_TracedOpaqueActionActivation.__init__)


def test_basicactions_tracedopaqueactionactivation_constructor_args():
    sig = inspect.signature(BasicActions_TracedOpaqueActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedpartdecomposition_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPartDecomposition)


def test_uml_tracedpartdecomposition_constructor_exists():
    assert callable(uml_TracedPartDecomposition.__init__)


def test_uml_tracedpartdecomposition_constructor_args():
    sig = inspect.signature(uml_TracedPartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedgeneralization_is_not_abstract():
    assert not inspect.isabstract(uml_TracedGeneralization)


def test_uml_tracedgeneralization_constructor_exists():
    assert callable(uml_TracedGeneralization.__init__)


def test_uml_tracedgeneralization_constructor_args():
    sig = inspect.signature(uml_TracedGeneralization.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcreatelinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCreateLinkAction)


def test_uml_tracedcreatelinkaction_constructor_exists():
    assert callable(uml_TracedCreateLinkAction.__init__)


def test_uml_tracedcreatelinkaction_constructor_args():
    sig = inspect.signature(uml_TracedCreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedusage_is_not_abstract():
    assert not inspect.isabstract(uml_TracedUsage)


def test_uml_tracedusage_constructor_exists():
    assert callable(uml_TracedUsage.__init__)


def test_uml_tracedusage_constructor_args():
    sig = inspect.signature(uml_TracedUsage.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedduration_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDuration)


def test_uml_tracedduration_constructor_exists():
    assert callable(uml_TracedDuration.__init__)


def test_uml_tracedduration_constructor_args():
    sig = inspect.signature(uml_TracedDuration.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedparameterset_is_not_abstract():
    assert not inspect.isabstract(uml_TracedParameterSet)


def test_uml_tracedparameterset_constructor_exists():
    assert callable(uml_TracedParameterSet.__init__)


def test_uml_tracedparameterset_constructor_args():
    sig = inspect.signature(uml_TracedParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_integerfunctions_tracedintegerlessfunctionbehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution)


def test_integerfunctions_tracedintegerlessfunctionbehaviorexecution_constructor_exists():
    assert callable(IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution.__init__)


def test_integerfunctions_tracedintegerlessfunctionbehaviorexecution_constructor_args():
    sig = inspect.signature(IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactivityparameternode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivityParameterNode)


def test_uml_tracedactivityparameternode_constructor_exists():
    assert callable(uml_TracedActivityParameterNode.__init__)


def test_uml_tracedactivityparameternode_constructor_args():
    sig = inspect.signature(uml_TracedActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedabstraction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAbstraction)


def test_uml_tracedabstraction_constructor_exists():
    assert callable(uml_TracedAbstraction.__init__)


def test_uml_tracedabstraction_constructor_args():
    sig = inspect.signature(uml_TracedAbstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstructuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStructuredActivityNode)


def test_uml_tracedstructuredactivitynode_constructor_exists():
    assert callable(uml_TracedStructuredActivityNode.__init__)


def test_uml_tracedstructuredactivitynode_constructor_args():
    sig = inspect.signature(uml_TracedStructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedliteralunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(uml_TracedLiteralUnlimitedNatural)


def test_uml_tracedliteralunlimitednatural_constructor_exists():
    assert callable(uml_TracedLiteralUnlimitedNatural.__init__)


def test_uml_tracedliteralunlimitednatural_constructor_args():
    sig = inspect.signature(uml_TracedLiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstate_is_not_abstract():
    assert not inspect.isabstract(uml_TracedState)


def test_uml_tracedstate_constructor_exists():
    assert callable(uml_TracedState.__init__)


def test_uml_tracedstate_constructor_args():
    sig = inspect.signature(uml_TracedState.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddestructionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDestructionOccurrenceSpecification)


def test_uml_traceddestructionoccurrencespecification_constructor_exists():
    assert callable(uml_TracedDestructionOccurrenceSpecification.__init__)


def test_uml_traceddestructionoccurrencespecification_constructor_args():
    sig = inspect.signature(uml_TracedDestructionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinclude_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInclude)


def test_uml_tracedinclude_constructor_exists():
    assert callable(uml_TracedInclude.__init__)


def test_uml_tracedinclude_constructor_args():
    sig = inspect.signature(uml_TracedInclude.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddurationinterval_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDurationInterval)


def test_uml_traceddurationinterval_constructor_exists():
    assert callable(uml_TracedDurationInterval.__init__)


def test_uml_traceddurationinterval_constructor_args():
    sig = inspect.signature(uml_TracedDurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcreateobjectaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCreateObjectAction)


def test_uml_tracedcreateobjectaction_constructor_exists():
    assert callable(uml_TracedCreateObjectAction.__init__)


def test_uml_tracedcreateobjectaction_constructor_args():
    sig = inspect.signature(uml_TracedCreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedelementimport_is_not_abstract():
    assert not inspect.isabstract(uml_TracedElementImport)


def test_uml_tracedelementimport_constructor_exists():
    assert callable(uml_TracedElementImport.__init__)


def test_uml_tracedelementimport_constructor_args():
    sig = inspect.signature(uml_TracedElementImport.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstartobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStartObjectBehaviorAction)


def test_uml_tracedstartobjectbehavioraction_constructor_exists():
    assert callable(uml_TracedStartObjectBehaviorAction.__init__)


def test_uml_tracedstartobjectbehavioraction_constructor_args():
    sig = inspect.signature(uml_TracedStartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_tracedoutputpinactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TracedOutputPinActivation)


def test_basicactions_tracedoutputpinactivation_constructor_exists():
    assert callable(BasicActions_TracedOutputPinActivation.__init__)


def test_basicactions_tracedoutputpinactivation_constructor_args():
    sig = inspect.signature(BasicActions_TracedOutputPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_tracedreadstructuralfeatureactionactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_TracedReadStructuralFeatureActionActivation)


def test_intermediateactions_tracedreadstructuralfeatureactionactivation_constructor_exists():
    assert callable(IntermediateActions_TracedReadStructuralFeatureActionActivation.__init__)


def test_intermediateactions_tracedreadstructuralfeatureactionactivation_constructor_args():
    sig = inspect.signature(IntermediateActions_TracedReadStructuralFeatureActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedstringexpression_is_not_abstract():
    assert not inspect.isabstract(uml_TracedStringExpression)


def test_uml_tracedstringexpression_constructor_exists():
    assert callable(uml_TracedStringExpression.__init__)


def test_uml_tracedstringexpression_constructor_args():
    sig = inspect.signature(uml_TracedStringExpression.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_tracedvaluespecificationactionactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_TracedValueSpecificationActionActivation)


def test_intermediateactions_tracedvaluespecificationactionactivation_constructor_exists():
    assert callable(IntermediateActions_TracedValueSpecificationActionActivation.__init__)


def test_intermediateactions_tracedvaluespecificationactionactivation_constructor_args():
    sig = inspect.signature(IntermediateActions_TracedValueSpecificationActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedassociationclass_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAssociationClass)


def test_uml_tracedassociationclass_constructor_exists():
    assert callable(uml_TracedAssociationClass.__init__)


def test_uml_tracedassociationclass_constructor_args():
    sig = inspect.signature(uml_TracedAssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcomponentrealization_is_not_abstract():
    assert not inspect.isabstract(uml_TracedComponentRealization)


def test_uml_tracedcomponentrealization_constructor_exists():
    assert callable(uml_TracedComponentRealization.__init__)


def test_uml_tracedcomponentrealization_constructor_args():
    sig = inspect.signature(uml_TracedComponentRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinteractionconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInteractionConstraint)


def test_uml_tracedinteractionconstraint_constructor_exists():
    assert callable(uml_TracedInteractionConstraint.__init__)


def test_uml_tracedinteractionconstraint_constructor_args():
    sig = inspect.signature(uml_TracedInteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedsequencenode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSequenceNode)


def test_uml_tracedsequencenode_constructor_exists():
    assert callable(uml_TracedSequenceNode.__init__)


def test_uml_tracedsequencenode_constructor_args():
    sig = inspect.signature(uml_TracedSequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinputpin_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInputPin)


def test_uml_tracedinputpin_constructor_exists():
    assert callable(uml_TracedInputPin.__init__)


def test_uml_tracedinputpin_constructor_args():
    sig = inspect.signature(uml_TracedInputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreduceaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReduceAction)


def test_uml_tracedreduceaction_constructor_exists():
    assert callable(uml_TracedReduceAction.__init__)


def test_uml_tracedreduceaction_constructor_args():
    sig = inspect.signature(uml_TracedReduceAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedgeneralizationset_is_not_abstract():
    assert not inspect.isabstract(uml_TracedGeneralizationSet)


def test_uml_tracedgeneralizationset_constructor_exists():
    assert callable(uml_TracedGeneralizationSet.__init__)


def test_uml_tracedgeneralizationset_constructor_args():
    sig = inspect.signature(uml_TracedGeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConstraint)


def test_uml_tracedconstraint_constructor_exists():
    assert callable(uml_TracedConstraint.__init__)


def test_uml_tracedconstraint_constructor_args():
    sig = inspect.signature(uml_TracedConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedjoinnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedJoinNode)


def test_uml_tracedjoinnode_constructor_exists():
    assert callable(uml_TracedJoinNode.__init__)


def test_uml_tracedjoinnode_constructor_args():
    sig = inspect.signature(uml_TracedJoinNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedextensionpoint_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExtensionPoint)


def test_uml_tracedextensionpoint_constructor_exists():
    assert callable(uml_TracedExtensionPoint.__init__)


def test_uml_tracedextensionpoint_constructor_args():
    sig = inspect.signature(uml_TracedExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedsignalevent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSignalEvent)


def test_uml_tracedsignalevent_constructor_exists():
    assert callable(uml_TracedSignalEvent.__init__)


def test_uml_tracedsignalevent_constructor_args():
    sig = inspect.signature(uml_TracedSignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedslot_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSlot)


def test_uml_tracedslot_constructor_exists():
    assert callable(uml_TracedSlot.__init__)


def test_uml_tracedslot_constructor_args():
    sig = inspect.signature(uml_TracedSlot.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtimeevent_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTimeEvent)


def test_uml_tracedtimeevent_constructor_exists():
    assert callable(uml_TracedTimeEvent.__init__)


def test_uml_tracedtimeevent_constructor_args():
    sig = inspect.signature(uml_TracedTimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedextension_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExtension)


def test_uml_tracedextension_constructor_exists():
    assert callable(uml_TracedExtension.__init__)


def test_uml_tracedextension_constructor_args():
    sig = inspect.signature(uml_TracedExtension.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtimeinterval_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTimeInterval)


def test_uml_tracedtimeinterval_constructor_exists():
    assert callable(uml_TracedTimeInterval.__init__)


def test_uml_tracedtimeinterval_constructor_args():
    sig = inspect.signature(uml_TracedTimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedport_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPort)


def test_uml_tracedport_constructor_exists():
    assert callable(uml_TracedPort.__init__)


def test_uml_tracedport_constructor_args():
    sig = inspect.signature(uml_TracedPort.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddeployment_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDeployment)


def test_uml_traceddeployment_constructor_exists():
    assert callable(uml_TracedDeployment.__init__)


def test_uml_traceddeployment_constructor_args():
    sig = inspect.signature(uml_TracedDeployment.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedbroadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedBroadcastSignalAction)


def test_uml_tracedbroadcastsignalaction_constructor_exists():
    assert callable(uml_TracedBroadcastSignalAction.__init__)


def test_uml_tracedbroadcastsignalaction_constructor_args():
    sig = inspect.signature(uml_TracedBroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtemplatesignature_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTemplateSignature)


def test_uml_tracedtemplatesignature_constructor_exists():
    assert callable(uml_TracedTemplateSignature.__init__)


def test_uml_tracedtemplatesignature_constructor_args():
    sig = inspect.signature(uml_TracedTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedredefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedRedefinableTemplateSignature)


def test_umltrace_uml_tracedredefinabletemplatesignature_constructor_exists():
    assert callable(umlTrace_uml_TracedRedefinableTemplateSignature.__init__)


def test_umltrace_uml_tracedredefinabletemplatesignature_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedRedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcollaboration_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCollaboration)


def test_uml_tracedcollaboration_constructor_exists():
    assert callable(uml_TracedCollaboration.__init__)


def test_uml_tracedcollaboration_constructor_args():
    sig = inspect.signature(uml_TracedCollaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedpackage_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPackage)


def test_uml_tracedpackage_constructor_exists():
    assert callable(uml_TracedPackage.__init__)


def test_uml_tracedpackage_constructor_args():
    sig = inspect.signature(uml_TracedPackage.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedactivityfinalnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedActivityFinalNodeActivation)


def test_intermediateactivities_tracedactivityfinalnodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedActivityFinalNodeActivation.__init__)


def test_intermediateactivities_tracedactivityfinalnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedActivityFinalNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedprotocoltransition_is_not_abstract():
    assert not inspect.isabstract(uml_TracedProtocolTransition)


def test_uml_tracedprotocoltransition_constructor_exists():
    assert callable(uml_TracedProtocolTransition.__init__)


def test_uml_tracedprotocoltransition_constructor_args():
    sig = inspect.signature(uml_TracedProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedreadlinkaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedReadLinkAction)


def test_uml_tracedreadlinkaction_constructor_exists():
    assert callable(uml_TracedReadLinkAction.__init__)


def test_uml_tracedreadlinkaction_constructor_args():
    sig = inspect.signature(uml_TracedReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedaddstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAddStructuralFeatureValueAction)


def test_uml_tracedaddstructuralfeaturevalueaction_constructor_exists():
    assert callable(uml_TracedAddStructuralFeatureValueAction.__init__)


def test_uml_tracedaddstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml_TracedAddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken_basetokeniswithdrawn_value_is_not_abstract():
    assert not inspect.isabstract(ForkedToken_baseTokenIsWithdrawn_Value)


def test_forkedtoken_basetokeniswithdrawn_value_constructor_exists():
    assert callable(ForkedToken_baseTokenIsWithdrawn_Value.__init__)


def test_forkedtoken_basetokeniswithdrawn_value_constructor_args():
    sig = inspect.signature(ForkedToken_baseTokenIsWithdrawn_Value.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken_basetoken_value_is_not_abstract():
    assert not inspect.isabstract(ForkedToken_baseToken_Value)


def test_forkedtoken_basetoken_value_constructor_exists():
    assert callable(ForkedToken_baseToken_Value.__init__)


def test_forkedtoken_basetoken_value_constructor_args():
    sig = inspect.signature(ForkedToken_baseToken_Value.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken_remainingofferscount_value_is_not_abstract():
    assert not inspect.isabstract(ForkedToken_remainingOffersCount_Value)


def test_forkedtoken_remainingofferscount_value_constructor_exists():
    assert callable(ForkedToken_remainingOffersCount_Value.__init__)


def test_forkedtoken_remainingofferscount_value_constructor_args():
    sig = inspect.signature(ForkedToken_remainingOffersCount_Value.__init__)
    params = list(sig.parameters.keys())



def test_integervalue_value_integervalue_value_is_not_abstract():
    assert not inspect.isabstract(IntegerValue_value_IntegerValue_Value)


def test_integervalue_value_integervalue_value_constructor_exists():
    assert callable(IntegerValue_value_IntegerValue_Value.__init__)


def test_integervalue_value_integervalue_value_constructor_args():
    sig = inspect.signature(IntegerValue_value_IntegerValue_Value.__init__)
    params = list(sig.parameters.keys())



def test_reference_referent_value_is_not_abstract():
    assert not inspect.isabstract(Reference_referent_Value)


def test_reference_referent_value_constructor_exists():
    assert callable(Reference_referent_Value.__init__)


def test_reference_referent_value_constructor_args():
    sig = inspect.signature(Reference_referent_Value.__init__)
    params = list(sig.parameters.keys())



def test_object_types_value_is_not_abstract():
    assert not inspect.isabstract(Object_types_Value)


def test_object_types_value_constructor_exists():
    assert callable(Object_types_Value.__init__)


def test_object_types_value_constructor_args():
    sig = inspect.signature(Object_types_Value.__init__)
    params = list(sig.parameters.keys())



def test_bigstep_is_not_abstract():
    assert not inspect.isabstract(BigStep)


def test_bigstep_constructor_exists():
    assert callable(BigStep.__init__)


def test_bigstep_constructor_args():
    sig = inspect.signature(BigStep.__init__)
    params = list(sig.parameters.keys())



def test_smallstep_is_not_abstract():
    assert not inspect.isabstract(SmallStep)


def test_smallstep_constructor_exists():
    assert callable(SmallStep.__init__)


def test_smallstep_constructor_args():
    sig = inspect.signature(SmallStep.__init__)
    params = list(sig.parameters.keys())



def test_semanticvisitor_runtimemodelelement_value_is_not_abstract():
    assert not inspect.isabstract(SemanticVisitor_runtimeModelElement_Value)


def test_semanticvisitor_runtimemodelelement_value_constructor_exists():
    assert callable(SemanticVisitor_runtimeModelElement_Value.__init__)


def test_semanticvisitor_runtimemodelelement_value_constructor_args():
    sig = inspect.signature(SemanticVisitor_runtimeModelElement_Value.__init__)
    params = list(sig.parameters.keys())



def test_objectnodeactivation_offeredtokencount_value_is_not_abstract():
    assert not inspect.isabstract(ObjectNodeActivation_offeredTokenCount_Value)


def test_objectnodeactivation_offeredtokencount_value_constructor_exists():
    assert callable(ObjectNodeActivation_offeredTokenCount_Value.__init__)


def test_objectnodeactivation_offeredtokencount_value_constructor_args():
    sig = inspect.signature(ObjectNodeActivation_offeredTokenCount_Value.__init__)
    params = list(sig.parameters.keys())



def test_locus_executor_value_is_not_abstract():
    assert not inspect.isabstract(Locus_executor_Value)


def test_locus_executor_value_constructor_exists():
    assert callable(Locus_executor_Value.__init__)


def test_locus_executor_value_constructor_args():
    sig = inspect.signature(Locus_executor_Value.__init__)
    params = list(sig.parameters.keys())



def test_locus_extensionalvalues_value_is_not_abstract():
    assert not inspect.isabstract(Locus_extensionalValues_Value)


def test_locus_extensionalvalues_value_constructor_exists():
    assert callable(Locus_extensionalValues_Value.__init__)


def test_locus_extensionalvalues_value_constructor_args():
    sig = inspect.signature(Locus_extensionalValues_Value.__init__)
    params = list(sig.parameters.keys())



def test_locus_factory_value_is_not_abstract():
    assert not inspect.isabstract(Locus_factory_Value)


def test_locus_factory_value_constructor_exists():
    assert callable(Locus_factory_Value.__init__)


def test_locus_factory_value_constructor_args():
    sig = inspect.signature(Locus_factory_Value.__init__)
    params = list(sig.parameters.keys())



def test_tracedobjects_is_not_abstract():
    assert not inspect.isabstract(TracedObjects)


def test_tracedobjects_constructor_exists():
    assert callable(TracedObjects.__init__)


def test_tracedobjects_constructor_args():
    sig = inspect.signature(TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_steps_is_not_abstract():
    assert not inspect.isabstract(Steps)


def test_steps_constructor_exists():
    assert callable(Steps.__init__)


def test_steps_constructor_args():
    sig = inspect.signature(Steps.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_state_is_not_abstract():
    assert not inspect.isabstract(umlTrace_State)


def test_umltrace_state_constructor_exists():
    assert callable(umlTrace_State.__init__)


def test_umltrace_state_constructor_args():
    sig = inspect.signature(umlTrace_State.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_trace_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Trace)


def test_umltrace_trace_constructor_exists():
    assert callable(umlTrace_Trace.__init__)


def test_umltrace_trace_constructor_args():
    sig = inspect.signature(umlTrace_Trace.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedenumerationliteral_is_not_abstract():
    assert not inspect.isabstract(uml_TracedEnumerationLiteral)


def test_uml_tracedenumerationliteral_constructor_exists():
    assert callable(uml_TracedEnumerationLiteral.__init__)


def test_uml_tracedenumerationliteral_constructor_args():
    sig = inspect.signature(uml_TracedEnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedaccepteventaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedAcceptEventAction)


def test_uml_tracedaccepteventaction_constructor_exists():
    assert callable(uml_TracedAcceptEventAction.__init__)


def test_uml_tracedaccepteventaction_constructor_args():
    sig = inspect.signature(uml_TracedAcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedinitialnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedInitialNodeActivation)


def test_intermediateactivities_tracedinitialnodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedInitialNodeActivation.__init__)


def test_intermediateactivities_tracedinitialnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedInitialNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddurationobservation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDurationObservation)


def test_uml_traceddurationobservation_constructor_exists():
    assert callable(uml_TracedDurationObservation.__init__)


def test_uml_traceddurationobservation_constructor_args():
    sig = inspect.signature(uml_TracedDurationObservation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactivityfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivityFinalNode)


def test_uml_tracedactivityfinalnode_constructor_exists():
    assert callable(uml_TracedActivityFinalNode.__init__)


def test_uml_tracedactivityfinalnode_constructor_args():
    sig = inspect.signature(uml_TracedActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinterfacerealization_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInterfaceRealization)


def test_uml_tracedinterfacerealization_constructor_exists():
    assert callable(uml_TracedInterfaceRealization.__init__)


def test_uml_tracedinterfacerealization_constructor_args():
    sig = inspect.signature(uml_TracedInterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedtimeconstraint_is_not_abstract():
    assert not inspect.isabstract(uml_TracedTimeConstraint)


def test_uml_tracedtimeconstraint_constructor_exists():
    assert callable(uml_TracedTimeConstraint.__init__)


def test_uml_tracedtimeconstraint_constructor_args():
    sig = inspect.signature(uml_TracedTimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedjoinnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedJoinNodeActivation)


def test_intermediateactivities_tracedjoinnodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedJoinNodeActivation.__init__)


def test_intermediateactivities_tracedjoinnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedJoinNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedinformationitem_is_not_abstract():
    assert not inspect.isabstract(uml_TracedInformationItem)


def test_uml_tracedinformationitem_constructor_exists():
    assert callable(uml_TracedInformationItem.__init__)


def test_uml_tracedinformationitem_constructor_args():
    sig = inspect.signature(uml_TracedInformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedflowfinalnode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedFlowFinalNode)


def test_uml_tracedflowfinalnode_constructor_exists():
    assert callable(uml_TracedFlowFinalNode.__init__)


def test_uml_tracedflowfinalnode_constructor_args():
    sig = inspect.signature(uml_TracedFlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddatastorenode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDataStoreNode)


def test_uml_traceddatastorenode_constructor_exists():
    assert callable(uml_TracedDataStoreNode.__init__)


def test_uml_traceddatastorenode_constructor_args():
    sig = inspect.signature(uml_TracedDataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconsiderignorefragment_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConsiderIgnoreFragment)


def test_uml_tracedconsiderignorefragment_constructor_exists():
    assert callable(uml_TracedConsiderIgnoreFragment.__init__)


def test_uml_tracedconsiderignorefragment_constructor_args():
    sig = inspect.signature(uml_TracedConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedexpression_is_not_abstract():
    assert not inspect.isabstract(uml_TracedExpression)


def test_uml_tracedexpression_constructor_exists():
    assert callable(uml_TracedExpression.__init__)


def test_uml_tracedexpression_constructor_args():
    sig = inspect.signature(uml_TracedExpression.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedstringexpression_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedStringExpression)


def test_umltrace_uml_tracedstringexpression_constructor_exists():
    assert callable(umlTrace_uml_TracedStringExpression.__init__)


def test_umltrace_uml_tracedstringexpression_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedStringExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedsendsignalaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedSendSignalAction)


def test_uml_tracedsendsignalaction_constructor_exists():
    assert callable(uml_TracedSendSignalAction.__init__)


def test_uml_tracedsendsignalaction_constructor_args():
    sig = inspect.signature(uml_TracedSendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedremovestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedRemoveStructuralFeatureValueAction)


def test_uml_tracedremovestructuralfeaturevalueaction_constructor_exists():
    assert callable(uml_TracedRemoveStructuralFeatureValueAction.__init__)


def test_uml_tracedremovestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(uml_TracedRemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcontinuation_is_not_abstract():
    assert not inspect.isabstract(uml_TracedContinuation)


def test_uml_tracedcontinuation_constructor_exists():
    assert callable(uml_TracedContinuation.__init__)


def test_uml_tracedcontinuation_constructor_args():
    sig = inspect.signature(uml_TracedContinuation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedproperty_is_not_abstract():
    assert not inspect.isabstract(uml_TracedProperty)


def test_uml_tracedproperty_constructor_exists():
    assert callable(uml_TracedProperty.__init__)


def test_uml_tracedproperty_constructor_args():
    sig = inspect.signature(uml_TracedProperty.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedcommunicationpath_is_not_abstract():
    assert not inspect.isabstract(uml_TracedCommunicationPath)


def test_uml_tracedcommunicationpath_constructor_exists():
    assert callable(uml_TracedCommunicationPath.__init__)


def test_uml_tracedcommunicationpath_constructor_args():
    sig = inspect.signature(uml_TracedCommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_uml_traceddatatype_is_not_abstract():
    assert not inspect.isabstract(uml_TracedDataType)


def test_uml_traceddatatype_constructor_exists():
    assert callable(uml_TracedDataType.__init__)


def test_uml_traceddatatype_constructor_args():
    sig = inspect.signature(uml_TracedDataType.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedopaqueaction_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOpaqueAction)


def test_uml_tracedopaqueaction_constructor_exists():
    assert callable(uml_TracedOpaqueAction.__init__)


def test_uml_tracedopaqueaction_constructor_args():
    sig = inspect.signature(uml_TracedOpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedconnector_is_not_abstract():
    assert not inspect.isabstract(uml_TracedConnector)


def test_uml_tracedconnector_constructor_exists():
    assert callable(uml_TracedConnector.__init__)


def test_uml_tracedconnector_constructor_args():
    sig = inspect.signature(uml_TracedConnector.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_traced_tracedobjects_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Traced_TracedObjects)


def test_umltrace_traced_tracedobjects_constructor_exists():
    assert callable(umlTrace_Traced_TracedObjects.__init__)


def test_umltrace_traced_tracedobjects_constructor_args():
    sig = inspect.signature(umlTrace_Traced_TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedartifact_is_not_abstract():
    assert not inspect.isabstract(uml_TracedArtifact)


def test_uml_tracedartifact_constructor_exists():
    assert callable(uml_TracedArtifact.__init__)


def test_uml_tracedartifact_constructor_args():
    sig = inspect.signature(uml_TracedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedopaquebehavior_is_not_abstract():
    assert not inspect.isabstract(uml_TracedOpaqueBehavior)


def test_uml_tracedopaquebehavior_constructor_exists():
    assert callable(uml_TracedOpaqueBehavior.__init__)


def test_uml_tracedopaquebehavior_constructor_args():
    sig = inspect.signature(uml_TracedOpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activityexecution_activationgroup_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityExecution_activationGroup_Value)


def test_umltrace_values_activityexecution_activationgroup_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityExecution_activationGroup_Value.__init__)


def test_umltrace_values_activityexecution_activationgroup_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityExecution_activationGroup_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_extensionalvalue_locus_extensionalvalue_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value)


def test_umltrace_values_extensionalvalue_locus_extensionalvalue_value_constructor_exists():
    assert callable(umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value.__init__)


def test_umltrace_values_extensionalvalue_locus_extensionalvalue_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activitynodeactivation_group_activitynodeactivation_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value)


def test_umltrace_values_activitynodeactivation_group_activitynodeactivation_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value.__init__)


def test_umltrace_values_activitynodeactivation_group_activitynodeactivation_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value.__init__)
    params = list(sig.parameters.keys())



def test_loci_tracedexecutionenvironment_is_not_abstract():
    assert not inspect.isabstract(Loci_TracedExecutionEnvironment)


def test_loci_tracedexecutionenvironment_constructor_exists():
    assert callable(Loci_TracedExecutionEnvironment.__init__)


def test_loci_tracedexecutionenvironment_constructor_args():
    sig = inspect.signature(Loci_TracedExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_executionenvironment_locus_executionenvironment_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value)


def test_umltrace_values_executionenvironment_locus_executionenvironment_value_constructor_exists():
    assert callable(umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value.__init__)


def test_umltrace_values_executionenvironment_locus_executionenvironment_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activitynodeactivation_outgoingedges_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value)


def test_umltrace_values_activitynodeactivation_outgoingedges_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value.__init__)


def test_umltrace_values_activitynodeactivation_outgoingedges_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activitynodeactivation_isrunning_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityNodeActivation_isRunning_Value)


def test_umltrace_values_activitynodeactivation_isrunning_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityNodeActivation_isRunning_Value.__init__)


def test_umltrace_values_activitynodeactivation_isrunning_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityNodeActivation_isRunning_Value.__init__)
    params = list(sig.parameters.keys())
    assert "isRunning" in params, "Missing parameter 'isRunning'"

def test_umltrace_values_activitynodeactivation_isrunning_value_has_isRunning():
    assert hasattr(umlTrace_Values_ActivityNodeActivation_isRunning_Value, "isRunning")
    descriptor = None
    for klass in umlTrace_Values_ActivityNodeActivation_isRunning_Value.__mro__:
        if "isRunning" in klass.__dict__:
            descriptor = klass.__dict__["isRunning"]
            break
    assert isinstance(descriptor, property)



def test_umltrace_values_activitynodeactivation_incomingedges_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityNodeActivation_incomingEdges_Value)


def test_umltrace_values_activitynodeactivation_incomingedges_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityNodeActivation_incomingEdges_Value.__init__)


def test_umltrace_values_activitynodeactivation_incomingedges_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityNodeActivation_incomingEdges_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activitynodeactivation_heldtokens_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityNodeActivation_heldTokens_Value)


def test_umltrace_values_activitynodeactivation_heldtokens_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityNodeActivation_heldTokens_Value.__init__)


def test_umltrace_values_activitynodeactivation_heldtokens_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityNodeActivation_heldTokens_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_inputparametervalues_parametervalues_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_InputParameterValues_parameterValues_Value)


def test_umltrace_values_inputparametervalues_parametervalues_value_constructor_exists():
    assert callable(umlTrace_Values_InputParameterValues_parameterValues_Value.__init__)


def test_umltrace_values_inputparametervalues_parametervalues_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_InputParameterValues_parameterValues_Value.__init__)
    params = list(sig.parameters.keys())



def test_input_tracedinputparametervalues_is_not_abstract():
    assert not inspect.isabstract(Input_TracedInputParameterValues)


def test_input_tracedinputparametervalues_constructor_exists():
    assert callable(Input_TracedInputParameterValues.__init__)


def test_input_tracedinputparametervalues_constructor_args():
    sig = inspect.signature(Input_TracedInputParameterValues.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_inputparametervalues_name_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_InputParameterValues_name_Value)


def test_umltrace_values_inputparametervalues_name_value_constructor_exists():
    assert callable(umlTrace_Values_InputParameterValues_name_Value.__init__)


def test_umltrace_values_inputparametervalues_name_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_InputParameterValues_name_Value.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umltrace_values_inputparametervalues_name_value_has_name():
    assert hasattr(umlTrace_Values_InputParameterValues_name_Value, "name")
    descriptor = None
    for klass in umlTrace_Values_InputParameterValues_name_Value.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umltrace_values_activitynodeactivation_running_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityNodeActivation_running_Value)


def test_umltrace_values_activitynodeactivation_running_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityNodeActivation_running_Value.__init__)


def test_umltrace_values_activitynodeactivation_running_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityNodeActivation_running_Value.__init__)
    params = list(sig.parameters.keys())
    assert "running" in params, "Missing parameter 'running'"

def test_umltrace_values_activitynodeactivation_running_value_has_running():
    assert hasattr(umlTrace_Values_ActivityNodeActivation_running_Value, "running")
    descriptor = None
    for klass in umlTrace_Values_ActivityNodeActivation_running_Value.__mro__:
        if "running" in klass.__dict__:
            descriptor = klass.__dict__["running"]
            break
    assert isinstance(descriptor, property)



def test_uml_tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivityNode)


def test_uml_tracedactivitynode_constructor_exists():
    assert callable(uml_TracedActivityNode.__init__)


def test_uml_tracedactivitynode_constructor_args():
    sig = inspect.signature(uml_TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_uml_tracedobjectnode_is_not_abstract():
    assert not inspect.isabstract(umlTrace_uml_TracedObjectNode)


def test_umltrace_uml_tracedobjectnode_constructor_exists():
    assert callable(umlTrace_uml_TracedObjectNode.__init__)


def test_umltrace_uml_tracedobjectnode_constructor_args():
    sig = inspect.signature(umlTrace_uml_TracedObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activitynodeactivation_node_activitynodeactivation_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value)


def test_umltrace_values_activitynodeactivation_node_activitynodeactivation_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value.__init__)


def test_umltrace_values_activitynodeactivation_node_activitynodeactivation_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(uml_TracedActivityEdge)


def test_uml_tracedactivityedge_constructor_exists():
    assert callable(uml_TracedActivityEdge.__init__)


def test_uml_tracedactivityedge_constructor_args():
    sig = inspect.signature(uml_TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activityedgeinstance_edge_activityedgeinstance_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value)


def test_umltrace_values_activityedgeinstance_edge_activityedgeinstance_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value.__init__)


def test_umltrace_values_activityedgeinstance_edge_activityedgeinstance_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activityedgeinstance_target_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityEdgeInstance_target_Value)


def test_umltrace_values_activityedgeinstance_target_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityEdgeInstance_target_Value.__init__)


def test_umltrace_values_activityedgeinstance_target_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityEdgeInstance_target_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activityedgeinstance_source_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityEdgeInstance_source_Value)


def test_umltrace_values_activityedgeinstance_source_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityEdgeInstance_source_Value.__init__)


def test_umltrace_values_activityedgeinstance_source_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityEdgeInstance_source_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activityedgeinstance_group_activityedgeinstance_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value)


def test_umltrace_values_activityedgeinstance_group_activityedgeinstance_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value.__init__)


def test_umltrace_values_activityedgeinstance_group_activityedgeinstance_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_pinactivation_count_temp_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_PinActivation_count_temp_Value)


def test_umltrace_values_pinactivation_count_temp_value_constructor_exists():
    assert callable(umlTrace_Values_PinActivation_count_temp_Value.__init__)


def test_umltrace_values_pinactivation_count_temp_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_PinActivation_count_temp_Value.__init__)
    params = list(sig.parameters.keys())
    assert "count_temp" in params, "Missing parameter 'count_temp'"

def test_umltrace_values_pinactivation_count_temp_value_has_count_temp():
    assert hasattr(umlTrace_Values_PinActivation_count_temp_Value, "count_temp")
    descriptor = None
    for klass in umlTrace_Values_PinActivation_count_temp_Value.__mro__:
        if "count_temp" in klass.__dict__:
            descriptor = klass.__dict__["count_temp"]
            break
    assert isinstance(descriptor, property)



def test_umltrace_values_activityedgeinstance_offers_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityEdgeInstance_offers_Value)


def test_umltrace_values_activityedgeinstance_offers_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityEdgeInstance_offers_Value.__init__)


def test_umltrace_values_activityedgeinstance_offers_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityEdgeInstance_offers_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_featurevalue_position_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_FeatureValue_position_Value)


def test_umltrace_values_featurevalue_position_value_constructor_exists():
    assert callable(umlTrace_Values_FeatureValue_position_Value.__init__)


def test_umltrace_values_featurevalue_position_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_FeatureValue_position_Value.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_umltrace_values_featurevalue_position_value_has_position():
    assert hasattr(umlTrace_Values_FeatureValue_position_Value, "position")
    descriptor = None
    for klass in umlTrace_Values_FeatureValue_position_Value.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



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



def test_umltrace_values_featurevalue_feature_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_FeatureValue_feature_Value)


def test_umltrace_values_featurevalue_feature_value_constructor_exists():
    assert callable(umlTrace_Values_FeatureValue_feature_Value.__init__)


def test_umltrace_values_featurevalue_feature_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_FeatureValue_feature_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_featurevalue_values_featurevalue_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_FeatureValue_values_FeatureValue_Value)


def test_umltrace_values_featurevalue_values_featurevalue_value_constructor_exists():
    assert callable(umlTrace_Values_FeatureValue_values_FeatureValue_Value.__init__)


def test_umltrace_values_featurevalue_values_featurevalue_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_FeatureValue_values_FeatureValue_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_pinactivation_actionactivation_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_PinActivation_actionActivation_Value)


def test_umltrace_values_pinactivation_actionactivation_value_constructor_exists():
    assert callable(umlTrace_Values_PinActivation_actionActivation_Value.__init__)


def test_umltrace_values_pinactivation_actionactivation_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_PinActivation_actionActivation_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_token_holder_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Token_holder_Value)


def test_umltrace_values_token_holder_value_constructor_exists():
    assert callable(umlTrace_Values_Token_holder_Value.__init__)


def test_umltrace_values_token_holder_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Token_holder_Value.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedcompoundvalue_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedCompoundValue)


def test_kernel_tracedcompoundvalue_constructor_exists():
    assert callable(Kernel_TracedCompoundValue.__init__)


def test_kernel_tracedcompoundvalue_constructor_args():
    sig = inspect.signature(Kernel_TracedCompoundValue.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedfeaturevalue_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedFeatureValue)


def test_kernel_tracedfeaturevalue_constructor_exists():
    assert callable(Kernel_TracedFeatureValue.__init__)


def test_kernel_tracedfeaturevalue_constructor_args():
    sig = inspect.signature(Kernel_TracedFeatureValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_compoundvalue_featurevalues_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_CompoundValue_featureValues_Value)


def test_umltrace_values_compoundvalue_featurevalues_value_constructor_exists():
    assert callable(umlTrace_Values_CompoundValue_featureValues_Value.__init__)


def test_umltrace_values_compoundvalue_featurevalues_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_CompoundValue_featureValues_Value.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_tracedcallactionactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TracedCallActionActivation)


def test_basicactions_tracedcallactionactivation_constructor_exists():
    assert callable(BasicActions_TracedCallActionActivation.__init__)


def test_basicactions_tracedcallactionactivation_constructor_args():
    sig = inspect.signature(BasicActions_TracedCallActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_callactionactivation_callexecutions_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_CallActionActivation_callExecutions_Value)


def test_umltrace_values_callactionactivation_callexecutions_value_constructor_exists():
    assert callable(umlTrace_Values_CallActionActivation_callExecutions_Value.__init__)


def test_umltrace_values_callactionactivation_callexecutions_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_CallActionActivation_callExecutions_Value.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedoffer_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedOffer)


def test_intermediateactivities_tracedoffer_constructor_exists():
    assert callable(IntermediateActivities_TracedOffer.__init__)


def test_intermediateactivities_tracedoffer_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedOffer.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_offer_offeredtokens_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Offer_offeredTokens_Value)


def test_umltrace_values_offer_offeredtokens_value_constructor_exists():
    assert callable(umlTrace_Values_Offer_offeredTokens_Value.__init__)


def test_umltrace_values_offer_offeredtokens_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Offer_offeredTokens_Value.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedbooleanvalue_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedBooleanValue)


def test_kernel_tracedbooleanvalue_constructor_exists():
    assert callable(Kernel_TracedBooleanValue.__init__)


def test_kernel_tracedbooleanvalue_constructor_args():
    sig = inspect.signature(Kernel_TracedBooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_booleanvalue_value_booleanvalue_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_BooleanValue_value_BooleanValue_Value)


def test_umltrace_values_booleanvalue_value_booleanvalue_value_constructor_exists():
    assert callable(umlTrace_Values_BooleanValue_value_BooleanValue_Value.__init__)


def test_umltrace_values_booleanvalue_value_booleanvalue_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_BooleanValue_value_BooleanValue_Value.__init__)
    params = list(sig.parameters.keys())
    assert "value_BooleanValue" in params, "Missing parameter 'value_BooleanValue'"

def test_umltrace_values_booleanvalue_value_booleanvalue_value_has_value_BooleanValue():
    assert hasattr(umlTrace_Values_BooleanValue_value_BooleanValue_Value, "value_BooleanValue")
    descriptor = None
    for klass in umlTrace_Values_BooleanValue_value_BooleanValue_Value.__mro__:
        if "value_BooleanValue" in klass.__dict__:
            descriptor = klass.__dict__["value_BooleanValue"]
            break
    assert isinstance(descriptor, property)



def test_umltrace_values_evaluation_locus_evaluation_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Evaluation_locus_Evaluation_Value)


def test_umltrace_values_evaluation_locus_evaluation_value_constructor_exists():
    assert callable(umlTrace_Values_Evaluation_locus_Evaluation_Value.__init__)


def test_umltrace_values_evaluation_locus_evaluation_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Evaluation_locus_Evaluation_Value.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedevaluation_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedEvaluation)


def test_kernel_tracedevaluation_constructor_exists():
    assert callable(Kernel_TracedEvaluation.__init__)


def test_kernel_tracedevaluation_constructor_args():
    sig = inspect.signature(Kernel_TracedEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedvaluespecification_is_not_abstract():
    assert not inspect.isabstract(uml_TracedValueSpecification)


def test_uml_tracedvaluespecification_constructor_exists():
    assert callable(uml_TracedValueSpecification.__init__)


def test_uml_tracedvaluespecification_constructor_args():
    sig = inspect.signature(uml_TracedValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_evaluation_specification_evaluation_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Evaluation_specification_Evaluation_Value)


def test_umltrace_values_evaluation_specification_evaluation_value_constructor_exists():
    assert callable(umlTrace_Values_Evaluation_specification_Evaluation_Value.__init__)


def test_umltrace_values_evaluation_specification_evaluation_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Evaluation_specification_Evaluation_Value.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedobjecttoken_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedObjectToken)


def test_intermediateactivities_tracedobjecttoken_constructor_exists():
    assert callable(IntermediateActivities_TracedObjectToken.__init__)


def test_intermediateactivities_tracedobjecttoken_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedObjectToken.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_objecttoken_value_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ObjectToken_value_Value)


def test_umltrace_values_objecttoken_value_value_constructor_exists():
    assert callable(umlTrace_Values_ObjectToken_value_Value.__init__)


def test_umltrace_values_objecttoken_value_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ObjectToken_value_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_executor_locus_executor_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Executor_locus_Executor_Value)


def test_umltrace_values_executor_locus_executor_value_constructor_exists():
    assert callable(umlTrace_Values_Executor_locus_Executor_Value.__init__)


def test_umltrace_values_executor_locus_executor_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Executor_locus_Executor_Value.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedactivityedgeinstance_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedActivityEdgeInstance)


def test_intermediateactivities_tracedactivityedgeinstance_constructor_exists():
    assert callable(IntermediateActivities_TracedActivityEdgeInstance.__init__)


def test_intermediateactivities_tracedactivityedgeinstance_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedActivityEdgeInstance.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activitynodeactivationgroup_edgeinstances_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value)


def test_umltrace_values_activitynodeactivationgroup_edgeinstances_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value.__init__)


def test_umltrace_values_activitynodeactivationgroup_edgeinstances_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedactivityexecution_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedActivityExecution)


def test_intermediateactivities_tracedactivityexecution_constructor_exists():
    assert callable(IntermediateActivities_TracedActivityExecution.__init__)


def test_intermediateactivities_tracedactivityexecution_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedActivityExecution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activitynodeactivationgroup_activityexecution_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value)


def test_umltrace_values_activitynodeactivationgroup_activityexecution_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value.__init__)


def test_umltrace_values_activitynodeactivationgroup_activityexecution_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedprimitivevalue_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedPrimitiveValue)


def test_kernel_tracedprimitivevalue_constructor_exists():
    assert callable(Kernel_TracedPrimitiveValue.__init__)


def test_kernel_tracedprimitivevalue_constructor_args():
    sig = inspect.signature(Kernel_TracedPrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_primitivevalue_type_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_PrimitiveValue_type_Value)


def test_umltrace_values_primitivevalue_type_value_constructor_exists():
    assert callable(umlTrace_Values_PrimitiveValue_type_Value.__init__)


def test_umltrace_values_primitivevalue_type_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_PrimitiveValue_type_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_element_semanticvisitor_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Element_semanticVisitor_Value)


def test_umltrace_values_element_semanticvisitor_value_constructor_exists():
    assert callable(umlTrace_Values_Element_semanticVisitor_Value.__init__)


def test_umltrace_values_element_semanticvisitor_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Element_semanticVisitor_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_execution_context_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Execution_context_Value)


def test_umltrace_values_execution_context_value_constructor_exists():
    assert callable(umlTrace_Values_Execution_context_Value.__init__)


def test_umltrace_values_execution_context_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Execution_context_Value.__init__)
    params = list(sig.parameters.keys())



def test_basicbehaviors_tracedexecution_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors_TracedExecution)


def test_basicbehaviors_tracedexecution_constructor_exists():
    assert callable(BasicBehaviors_TracedExecution.__init__)


def test_basicbehaviors_tracedexecution_constructor_args():
    sig = inspect.signature(BasicBehaviors_TracedExecution.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedactivitynodeactivationgroup_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedActivityNodeActivationGroup)


def test_intermediateactivities_tracedactivitynodeactivationgroup_constructor_exists():
    assert callable(IntermediateActivities_TracedActivityNodeActivationGroup.__init__)


def test_intermediateactivities_tracedactivitynodeactivationgroup_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedActivityNodeActivationGroup.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedactivitynodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedActivityNodeActivation)


def test_intermediateactivities_tracedactivitynodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedActivityNodeActivation.__init__)


def test_intermediateactivities_tracedactivitynodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedActivityNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_activitynodeactivationgroup_nodeactivations_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value)


def test_umltrace_values_activitynodeactivationgroup_nodeactivations_value_constructor_exists():
    assert callable(umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value.__init__)


def test_umltrace_values_activitynodeactivationgroup_nodeactivations_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_tracedactionactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TracedActionActivation)


def test_basicactions_tracedactionactivation_constructor_exists():
    assert callable(BasicActions_TracedActionActivation.__init__)


def test_basicactions_tracedactionactivation_constructor_args():
    sig = inspect.signature(BasicActions_TracedActionActivation.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_tracedpinactivation_is_not_abstract():
    assert not inspect.isabstract(BasicActions_TracedPinActivation)


def test_basicactions_tracedpinactivation_constructor_exists():
    assert callable(BasicActions_TracedPinActivation.__init__)


def test_basicactions_tracedpinactivation_constructor_args():
    sig = inspect.signature(BasicActions_TracedPinActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_actionactivation_pinactivations_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ActionActivation_pinActivations_Value)


def test_umltrace_values_actionactivation_pinactivations_value_constructor_exists():
    assert callable(umlTrace_Values_ActionActivation_pinActivations_Value.__init__)


def test_umltrace_values_actionactivation_pinactivations_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ActionActivation_pinActivations_Value.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedparameter_is_not_abstract():
    assert not inspect.isabstract(uml_TracedParameter)


def test_uml_tracedparameter_constructor_exists():
    assert callable(uml_TracedParameter.__init__)


def test_uml_tracedparameter_constructor_args():
    sig = inspect.signature(uml_TracedParameter.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_parametervalue_parameter_parametervalue_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ParameterValue_parameter_ParameterValue_Value)


def test_umltrace_values_parametervalue_parameter_parametervalue_value_constructor_exists():
    assert callable(umlTrace_Values_ParameterValue_parameter_ParameterValue_Value.__init__)


def test_umltrace_values_parametervalue_parameter_parametervalue_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ParameterValue_parameter_ParameterValue_Value.__init__)
    params = list(sig.parameters.keys())



def test_basicbehaviors_tracedparametervalue_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors_TracedParameterValue)


def test_basicbehaviors_tracedparametervalue_constructor_exists():
    assert callable(BasicBehaviors_TracedParameterValue.__init__)


def test_basicbehaviors_tracedparametervalue_constructor_args():
    sig = inspect.signature(BasicBehaviors_TracedParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedvalue_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedValue)


def test_kernel_tracedvalue_constructor_exists():
    assert callable(Kernel_TracedValue.__init__)


def test_kernel_tracedvalue_constructor_args():
    sig = inspect.signature(Kernel_TracedValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_execution_parametervalues_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Execution_parameterValues_Value)


def test_umltrace_values_execution_parametervalues_value_constructor_exists():
    assert callable(umlTrace_Values_Execution_parameterValues_Value.__init__)


def test_umltrace_values_execution_parametervalues_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Execution_parameterValues_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_semanticvisitor_runtimemodelelement_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_SemanticVisitor_runtimeModelElement_Value)


def test_umltrace_values_semanticvisitor_runtimemodelelement_value_constructor_exists():
    assert callable(umlTrace_Values_SemanticVisitor_runtimeModelElement_Value.__init__)


def test_umltrace_values_semanticvisitor_runtimemodelelement_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_SemanticVisitor_runtimeModelElement_Value.__init__)
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



def test_intermediateactivities_tracedobjectnodeactivation_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedObjectNodeActivation)


def test_intermediateactivities_tracedobjectnodeactivation_constructor_exists():
    assert callable(IntermediateActivities_TracedObjectNodeActivation.__init__)


def test_intermediateactivities_tracedobjectnodeactivation_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedObjectNodeActivation.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_objectnodeactivation_offeredtokencount_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value)


def test_umltrace_values_objectnodeactivation_offeredtokencount_value_constructor_exists():
    assert callable(umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value.__init__)


def test_umltrace_values_objectnodeactivation_offeredtokencount_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value.__init__)
    params = list(sig.parameters.keys())
    assert "offeredTokenCount" in params, "Missing parameter 'offeredTokenCount'"

def test_umltrace_values_objectnodeactivation_offeredtokencount_value_has_offeredTokenCount():
    assert hasattr(umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value, "offeredTokenCount")
    descriptor = None
    for klass in umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value.__mro__:
        if "offeredTokenCount" in klass.__dict__:
            descriptor = klass.__dict__["offeredTokenCount"]
            break
    assert isinstance(descriptor, property)



def test_loci_tracedexecutor_is_not_abstract():
    assert not inspect.isabstract(Loci_TracedExecutor)


def test_loci_tracedexecutor_constructor_exists():
    assert callable(Loci_TracedExecutor.__init__)


def test_loci_tracedexecutor_constructor_args():
    sig = inspect.signature(Loci_TracedExecutor.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_locus_executor_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Locus_executor_Value)


def test_umltrace_values_locus_executor_value_constructor_exists():
    assert callable(umlTrace_Values_Locus_executor_Value.__init__)


def test_umltrace_values_locus_executor_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Locus_executor_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_parametervalue_values_parametervalue_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ParameterValue_values_ParameterValue_Value)


def test_umltrace_values_parametervalue_values_parametervalue_value_constructor_exists():
    assert callable(umlTrace_Values_ParameterValue_values_ParameterValue_Value.__init__)


def test_umltrace_values_parametervalue_values_parametervalue_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ParameterValue_values_ParameterValue_Value.__init__)
    params = list(sig.parameters.keys())



def test_loci_tracedsemanticvisitor_is_not_abstract():
    assert not inspect.isabstract(Loci_TracedSemanticVisitor)


def test_loci_tracedsemanticvisitor_constructor_exists():
    assert callable(Loci_TracedSemanticVisitor.__init__)


def test_loci_tracedsemanticvisitor_constructor_args():
    sig = inspect.signature(Loci_TracedSemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedelement_is_not_abstract():
    assert not inspect.isabstract(uml_TracedElement)


def test_uml_tracedelement_constructor_exists():
    assert callable(uml_TracedElement.__init__)


def test_uml_tracedelement_constructor_args():
    sig = inspect.signature(uml_TracedElement.__init__)
    params = list(sig.parameters.keys())



def test_loci_tracedlocus_is_not_abstract():
    assert not inspect.isabstract(Loci_TracedLocus)


def test_loci_tracedlocus_constructor_exists():
    assert callable(Loci_TracedLocus.__init__)


def test_loci_tracedlocus_constructor_args():
    sig = inspect.signature(Loci_TracedLocus.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_executionfactory_locus_executionfactory_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value)


def test_umltrace_values_executionfactory_locus_executionfactory_value_constructor_exists():
    assert callable(umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value.__init__)


def test_umltrace_values_executionfactory_locus_executionfactory_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value.__init__)
    params = list(sig.parameters.keys())



def test_basicbehaviors_tracedopaquebehaviorexecution_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors_TracedOpaqueBehaviorExecution)


def test_basicbehaviors_tracedopaquebehaviorexecution_constructor_exists():
    assert callable(BasicBehaviors_TracedOpaqueBehaviorExecution.__init__)


def test_basicbehaviors_tracedopaquebehaviorexecution_constructor_args():
    sig = inspect.signature(BasicBehaviors_TracedOpaqueBehaviorExecution.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_executionfactory_primitivebehaviorprototypes_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value)


def test_umltrace_values_executionfactory_primitivebehaviorprototypes_value_constructor_exists():
    assert callable(umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value.__init__)


def test_umltrace_values_executionfactory_primitivebehaviorprototypes_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value.__init__)
    params = list(sig.parameters.keys())



def test_loci_tracedexecutionfactory_is_not_abstract():
    assert not inspect.isabstract(Loci_TracedExecutionFactory)


def test_loci_tracedexecutionfactory_constructor_exists():
    assert callable(Loci_TracedExecutionFactory.__init__)


def test_loci_tracedexecutionfactory_constructor_args():
    sig = inspect.signature(Loci_TracedExecutionFactory.__init__)
    params = list(sig.parameters.keys())



def test_uml_tracedprimitivetype_is_not_abstract():
    assert not inspect.isabstract(uml_TracedPrimitiveType)


def test_uml_tracedprimitivetype_constructor_exists():
    assert callable(uml_TracedPrimitiveType.__init__)


def test_uml_tracedprimitivetype_constructor_args():
    sig = inspect.signature(uml_TracedPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_executionfactory_builtintypes_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ExecutionFactory_builtInTypes_Value)


def test_umltrace_values_executionfactory_builtintypes_value_constructor_exists():
    assert callable(umlTrace_Values_ExecutionFactory_builtInTypes_Value.__init__)


def test_umltrace_values_executionfactory_builtintypes_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ExecutionFactory_builtInTypes_Value.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedextensionalvalue_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedExtensionalValue)


def test_kernel_tracedextensionalvalue_constructor_exists():
    assert callable(Kernel_TracedExtensionalValue.__init__)


def test_kernel_tracedextensionalvalue_constructor_args():
    sig = inspect.signature(Kernel_TracedExtensionalValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_locus_extensionalvalues_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Locus_extensionalValues_Value)


def test_umltrace_values_locus_extensionalvalues_value_constructor_exists():
    assert callable(umlTrace_Values_Locus_extensionalValues_Value.__init__)


def test_umltrace_values_locus_extensionalvalues_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Locus_extensionalValues_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_locus_factory_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Locus_factory_Value)


def test_umltrace_values_locus_factory_value_constructor_exists():
    assert callable(umlTrace_Values_Locus_factory_Value.__init__)


def test_umltrace_values_locus_factory_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Locus_factory_Value.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_tracedforkedtoken_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedForkedToken)


def test_intermediateactivities_tracedforkedtoken_constructor_exists():
    assert callable(IntermediateActivities_TracedForkedToken.__init__)


def test_intermediateactivities_tracedforkedtoken_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedForkedToken.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_forkedtoken_remainingofferscount_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ForkedToken_remainingOffersCount_Value)


def test_umltrace_values_forkedtoken_remainingofferscount_value_constructor_exists():
    assert callable(umlTrace_Values_ForkedToken_remainingOffersCount_Value.__init__)


def test_umltrace_values_forkedtoken_remainingofferscount_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ForkedToken_remainingOffersCount_Value.__init__)
    params = list(sig.parameters.keys())
    assert "remainingOffersCount" in params, "Missing parameter 'remainingOffersCount'"

def test_umltrace_values_forkedtoken_remainingofferscount_value_has_remainingOffersCount():
    assert hasattr(umlTrace_Values_ForkedToken_remainingOffersCount_Value, "remainingOffersCount")
    descriptor = None
    for klass in umlTrace_Values_ForkedToken_remainingOffersCount_Value.__mro__:
        if "remainingOffersCount" in klass.__dict__:
            descriptor = klass.__dict__["remainingOffersCount"]
            break
    assert isinstance(descriptor, property)



def test_kernel_tracedintegervalue_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedIntegerValue)


def test_kernel_tracedintegervalue_constructor_exists():
    assert callable(Kernel_TracedIntegerValue.__init__)


def test_kernel_tracedintegervalue_constructor_args():
    sig = inspect.signature(Kernel_TracedIntegerValue.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_integervalue_value_integervalue_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_IntegerValue_value_IntegerValue_Value)


def test_umltrace_values_integervalue_value_integervalue_value_constructor_exists():
    assert callable(umlTrace_Values_IntegerValue_value_IntegerValue_Value.__init__)


def test_umltrace_values_integervalue_value_integervalue_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_IntegerValue_value_IntegerValue_Value.__init__)
    params = list(sig.parameters.keys())
    assert "value_IntegerValue" in params, "Missing parameter 'value_IntegerValue'"

def test_umltrace_values_integervalue_value_integervalue_value_has_value_IntegerValue():
    assert hasattr(umlTrace_Values_IntegerValue_value_IntegerValue_Value, "value_IntegerValue")
    descriptor = None
    for klass in umlTrace_Values_IntegerValue_value_IntegerValue_Value.__mro__:
        if "value_IntegerValue" in klass.__dict__:
            descriptor = klass.__dict__["value_IntegerValue"]
            break
    assert isinstance(descriptor, property)



def test_kernel_tracedreference_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedReference)


def test_kernel_tracedreference_constructor_exists():
    assert callable(Kernel_TracedReference.__init__)


def test_kernel_tracedreference_constructor_args():
    sig = inspect.signature(Kernel_TracedReference.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_reference_referent_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Reference_referent_Value)


def test_umltrace_values_reference_referent_value_constructor_exists():
    assert callable(umlTrace_Values_Reference_referent_Value.__init__)


def test_umltrace_values_reference_referent_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Reference_referent_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_forkedtoken_basetokeniswithdrawn_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value)


def test_umltrace_values_forkedtoken_basetokeniswithdrawn_value_constructor_exists():
    assert callable(umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value.__init__)


def test_umltrace_values_forkedtoken_basetokeniswithdrawn_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value.__init__)
    params = list(sig.parameters.keys())
    assert "baseTokenIsWithdrawn" in params, "Missing parameter 'baseTokenIsWithdrawn'"

def test_umltrace_values_forkedtoken_basetokeniswithdrawn_value_has_baseTokenIsWithdrawn():
    assert hasattr(umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value, "baseTokenIsWithdrawn")
    descriptor = None
    for klass in umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value.__mro__:
        if "baseTokenIsWithdrawn" in klass.__dict__:
            descriptor = klass.__dict__["baseTokenIsWithdrawn"]
            break
    assert isinstance(descriptor, property)



def test_intermediateactivities_tracedtoken_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_TracedToken)


def test_intermediateactivities_tracedtoken_constructor_exists():
    assert callable(IntermediateActivities_TracedToken.__init__)


def test_intermediateactivities_tracedtoken_constructor_args():
    sig = inspect.signature(IntermediateActivities_TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_values_forkedtoken_basetoken_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_ForkedToken_baseToken_Value)


def test_umltrace_values_forkedtoken_basetoken_value_constructor_exists():
    assert callable(umlTrace_Values_ForkedToken_baseToken_Value.__init__)


def test_umltrace_values_forkedtoken_basetoken_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_ForkedToken_baseToken_Value.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_steps_bigstep_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Steps_BigStep)


def test_umltrace_steps_bigstep_constructor_exists():
    assert callable(umlTrace_Steps_BigStep.__init__)


def test_umltrace_steps_bigstep_constructor_args():
    sig = inspect.signature(umlTrace_Steps_BigStep.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_steps_steps_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Steps_Steps)


def test_umltrace_steps_steps_constructor_exists():
    assert callable(umlTrace_Steps_Steps.__init__)


def test_umltrace_steps_steps_constructor_args():
    sig = inspect.signature(umlTrace_Steps_Steps.__init__)
    params = list(sig.parameters.keys())



def test_steps_umltrace_state_is_not_abstract():
    assert not inspect.isabstract(Steps_umlTrace_State)


def test_steps_umltrace_state_constructor_exists():
    assert callable(Steps_umlTrace_State.__init__)


def test_steps_umltrace_state_constructor_args():
    sig = inspect.signature(Steps_umlTrace_State.__init__)
    params = list(sig.parameters.keys())



def test_umltrace_steps_smallstep_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Steps_SmallStep)


def test_umltrace_steps_smallstep_constructor_exists():
    assert callable(umlTrace_Steps_SmallStep.__init__)


def test_umltrace_steps_smallstep_constructor_args():
    sig = inspect.signature(umlTrace_Steps_SmallStep.__init__)
    params = list(sig.parameters.keys())



def test_executionenvironment_locus_executionenvironment_value_is_not_abstract():
    assert not inspect.isabstract(ExecutionEnvironment_locus_ExecutionEnvironment_Value)


def test_executionenvironment_locus_executionenvironment_value_constructor_exists():
    assert callable(ExecutionEnvironment_locus_ExecutionEnvironment_Value.__init__)


def test_executionenvironment_locus_executionenvironment_value_constructor_args():
    sig = inspect.signature(ExecutionEnvironment_locus_ExecutionEnvironment_Value.__init__)
    params = list(sig.parameters.keys())



def test_activityexecution_activationgroup_value_is_not_abstract():
    assert not inspect.isabstract(ActivityExecution_activationGroup_Value)


def test_activityexecution_activationgroup_value_constructor_exists():
    assert callable(ActivityExecution_activationGroup_Value.__init__)


def test_activityexecution_activationgroup_value_constructor_args():
    sig = inspect.signature(ActivityExecution_activationGroup_Value.__init__)
    params = list(sig.parameters.keys())



def test_extensionalvalue_locus_extensionalvalue_value_is_not_abstract():
    assert not inspect.isabstract(ExtensionalValue_locus_ExtensionalValue_Value)


def test_extensionalvalue_locus_extensionalvalue_value_constructor_exists():
    assert callable(ExtensionalValue_locus_ExtensionalValue_Value.__init__)


def test_extensionalvalue_locus_extensionalvalue_value_constructor_args():
    sig = inspect.signature(ExtensionalValue_locus_ExtensionalValue_Value.__init__)
    params = list(sig.parameters.keys())



def test_activitynodeactivation_group_activitynodeactivation_value_is_not_abstract():
    assert not inspect.isabstract(ActivityNodeActivation_group_ActivityNodeActivation_Value)


def test_activitynodeactivation_group_activitynodeactivation_value_constructor_exists():
    assert callable(ActivityNodeActivation_group_ActivityNodeActivation_Value.__init__)


def test_activitynodeactivation_group_activitynodeactivation_value_constructor_args():
    sig = inspect.signature(ActivityNodeActivation_group_ActivityNodeActivation_Value.__init__)
    params = list(sig.parameters.keys())



def test_activitynodeactivation_incomingedges_value_is_not_abstract():
    assert not inspect.isabstract(ActivityNodeActivation_incomingEdges_Value)


def test_activitynodeactivation_incomingedges_value_constructor_exists():
    assert callable(ActivityNodeActivation_incomingEdges_Value.__init__)


def test_activitynodeactivation_incomingedges_value_constructor_args():
    sig = inspect.signature(ActivityNodeActivation_incomingEdges_Value.__init__)
    params = list(sig.parameters.keys())



def test_activitynodeactivation_outgoingedges_value_is_not_abstract():
    assert not inspect.isabstract(ActivityNodeActivation_outgoingEdges_Value)


def test_activitynodeactivation_outgoingedges_value_constructor_exists():
    assert callable(ActivityNodeActivation_outgoingEdges_Value.__init__)


def test_activitynodeactivation_outgoingedges_value_constructor_args():
    sig = inspect.signature(ActivityNodeActivation_outgoingEdges_Value.__init__)
    params = list(sig.parameters.keys())



def test_values_umltrace_state_is_not_abstract():
    assert not inspect.isabstract(Values_umlTrace_State)


def test_values_umltrace_state_constructor_exists():
    assert callable(Values_umlTrace_State.__init__)


def test_values_umltrace_state_constructor_args():
    sig = inspect.signature(Values_umlTrace_State.__init__)
    params = list(sig.parameters.keys())



def test_kernel_tracedobject_is_not_abstract():
    assert not inspect.isabstract(Kernel_TracedObject)


def test_kernel_tracedobject_constructor_exists():
    assert callable(Kernel_TracedObject.__init__)


def test_kernel_tracedobject_constructor_args():
    sig = inspect.signature(Kernel_TracedObject.__init__)
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



def test_umltrace_values_object_types_value_is_not_abstract():
    assert not inspect.isabstract(umlTrace_Values_Object_types_Value)


def test_umltrace_values_object_types_value_constructor_exists():
    assert callable(umlTrace_Values_Object_types_Value.__init__)


def test_umltrace_values_object_types_value_constructor_args():
    sig = inspect.signature(umlTrace_Values_Object_types_Value.__init__)
    params = list(sig.parameters.keys())



def test_activitynodeactivation_heldtokens_value_is_not_abstract():
    assert not inspect.isabstract(ActivityNodeActivation_heldTokens_Value)


def test_activitynodeactivation_heldtokens_value_constructor_exists():
    assert callable(ActivityNodeActivation_heldTokens_Value.__init__)


def test_activitynodeactivation_heldtokens_value_constructor_args():
    sig = inspect.signature(ActivityNodeActivation_heldTokens_Value.__init__)
    params = list(sig.parameters.keys())



def test_inputparametervalues_parametervalues_value_is_not_abstract():
    assert not inspect.isabstract(InputParameterValues_parameterValues_Value)


def test_inputparametervalues_parametervalues_value_constructor_exists():
    assert callable(InputParameterValues_parameterValues_Value.__init__)


def test_inputparametervalues_parametervalues_value_constructor_args():
    sig = inspect.signature(InputParameterValues_parameterValues_Value.__init__)
    params = list(sig.parameters.keys())



def test_inputparametervalues_name_value_is_not_abstract():
    assert not inspect.isabstract(InputParameterValues_name_Value)


def test_inputparametervalues_name_value_constructor_exists():
    assert callable(InputParameterValues_name_Value.__init__)


def test_inputparametervalues_name_value_constructor_args():
    sig = inspect.signature(InputParameterValues_name_Value.__init__)
    params = list(sig.parameters.keys())



def test_activityedgeinstance_source_value_is_not_abstract():
    assert not inspect.isabstract(ActivityEdgeInstance_source_Value)


def test_activityedgeinstance_source_value_constructor_exists():
    assert callable(ActivityEdgeInstance_source_Value.__init__)


def test_activityedgeinstance_source_value_constructor_args():
    sig = inspect.signature(ActivityEdgeInstance_source_Value.__init__)
    params = list(sig.parameters.keys())



def test_activityedgeinstance_edge_activityedgeinstance_value_is_not_abstract():
    assert not inspect.isabstract(ActivityEdgeInstance_edge_ActivityEdgeInstance_Value)


def test_activityedgeinstance_edge_activityedgeinstance_value_constructor_exists():
    assert callable(ActivityEdgeInstance_edge_ActivityEdgeInstance_Value.__init__)


def test_activityedgeinstance_edge_activityedgeinstance_value_constructor_args():
    sig = inspect.signature(ActivityEdgeInstance_edge_ActivityEdgeInstance_Value.__init__)
    params = list(sig.parameters.keys())



def test_activityedgeinstance_target_value_is_not_abstract():
    assert not inspect.isabstract(ActivityEdgeInstance_target_Value)


def test_activityedgeinstance_target_value_constructor_exists():
    assert callable(ActivityEdgeInstance_target_Value.__init__)


def test_activityedgeinstance_target_value_constructor_args():
    sig = inspect.signature(ActivityEdgeInstance_target_Value.__init__)
    params = list(sig.parameters.keys())



def test_activityedgeinstance_offers_value_is_not_abstract():
    assert not inspect.isabstract(ActivityEdgeInstance_offers_Value)


def test_activityedgeinstance_offers_value_constructor_exists():
    assert callable(ActivityEdgeInstance_offers_Value.__init__)


def test_activityedgeinstance_offers_value_constructor_args():
    sig = inspect.signature(ActivityEdgeInstance_offers_Value.__init__)
    params = list(sig.parameters.keys())



def test_activityedgeinstance_group_activityedgeinstance_value_is_not_abstract():
    assert not inspect.isabstract(ActivityEdgeInstance_group_ActivityEdgeInstance_Value)


def test_activityedgeinstance_group_activityedgeinstance_value_constructor_exists():
    assert callable(ActivityEdgeInstance_group_ActivityEdgeInstance_Value.__init__)


def test_activityedgeinstance_group_activityedgeinstance_value_constructor_args():
    sig = inspect.signature(ActivityEdgeInstance_group_ActivityEdgeInstance_Value.__init__)
    params = list(sig.parameters.keys())



def test_pinactivation_count_temp_value_is_not_abstract():
    assert not inspect.isabstract(PinActivation_count_temp_Value)


def test_pinactivation_count_temp_value_constructor_exists():
    assert callable(PinActivation_count_temp_Value.__init__)


def test_pinactivation_count_temp_value_constructor_args():
    sig = inspect.signature(PinActivation_count_temp_Value.__init__)
    params = list(sig.parameters.keys())



def test_activitynodeactivation_isrunning_value_is_not_abstract():
    assert not inspect.isabstract(ActivityNodeActivation_isRunning_Value)


def test_activitynodeactivation_isrunning_value_constructor_exists():
    assert callable(ActivityNodeActivation_isRunning_Value.__init__)


def test_activitynodeactivation_isrunning_value_constructor_args():
    sig = inspect.signature(ActivityNodeActivation_isRunning_Value.__init__)
    params = list(sig.parameters.keys())



def test_activitynodeactivation_running_value_is_not_abstract():
    assert not inspect.isabstract(ActivityNodeActivation_running_Value)


def test_activitynodeactivation_running_value_constructor_exists():
    assert callable(ActivityNodeActivation_running_Value.__init__)


def test_activitynodeactivation_running_value_constructor_args():
    sig = inspect.signature(ActivityNodeActivation_running_Value.__init__)
    params = list(sig.parameters.keys())



def test_activitynodeactivation_node_activitynodeactivation_value_is_not_abstract():
    assert not inspect.isabstract(ActivityNodeActivation_node_ActivityNodeActivation_Value)


def test_activitynodeactivation_node_activitynodeactivation_value_constructor_exists():
    assert callable(ActivityNodeActivation_node_ActivityNodeActivation_Value.__init__)


def test_activitynodeactivation_node_activitynodeactivation_value_constructor_args():
    sig = inspect.signature(ActivityNodeActivation_node_ActivityNodeActivation_Value.__init__)
    params = list(sig.parameters.keys())



def test_featurevalue_values_featurevalue_value_is_not_abstract():
    assert not inspect.isabstract(FeatureValue_values_FeatureValue_Value)


def test_featurevalue_values_featurevalue_value_constructor_exists():
    assert callable(FeatureValue_values_FeatureValue_Value.__init__)


def test_featurevalue_values_featurevalue_value_constructor_args():
    sig = inspect.signature(FeatureValue_values_FeatureValue_Value.__init__)
    params = list(sig.parameters.keys())



def test_offer_offeredtokens_value_is_not_abstract():
    assert not inspect.isabstract(Offer_offeredTokens_Value)


def test_offer_offeredtokens_value_constructor_exists():
    assert callable(Offer_offeredTokens_Value.__init__)


def test_offer_offeredtokens_value_constructor_args():
    sig = inspect.signature(Offer_offeredTokens_Value.__init__)
    params = list(sig.parameters.keys())



def test_token_holder_value_is_not_abstract():
    assert not inspect.isabstract(Token_holder_Value)


def test_token_holder_value_constructor_exists():
    assert callable(Token_holder_Value.__init__)


def test_token_holder_value_constructor_args():
    sig = inspect.signature(Token_holder_Value.__init__)
    params = list(sig.parameters.keys())



def test_compoundvalue_featurevalues_value_is_not_abstract():
    assert not inspect.isabstract(CompoundValue_featureValues_Value)


def test_compoundvalue_featurevalues_value_constructor_exists():
    assert callable(CompoundValue_featureValues_Value.__init__)


def test_compoundvalue_featurevalues_value_constructor_args():
    sig = inspect.signature(CompoundValue_featureValues_Value.__init__)
    params = list(sig.parameters.keys())



def test_callactionactivation_callexecutions_value_is_not_abstract():
    assert not inspect.isabstract(CallActionActivation_callExecutions_Value)


def test_callactionactivation_callexecutions_value_constructor_exists():
    assert callable(CallActionActivation_callExecutions_Value.__init__)


def test_callactionactivation_callexecutions_value_constructor_args():
    sig = inspect.signature(CallActionActivation_callExecutions_Value.__init__)
    params = list(sig.parameters.keys())



def test_objecttoken_value_value_is_not_abstract():
    assert not inspect.isabstract(ObjectToken_value_Value)


def test_objecttoken_value_value_constructor_exists():
    assert callable(ObjectToken_value_Value.__init__)


def test_objecttoken_value_value_constructor_args():
    sig = inspect.signature(ObjectToken_value_Value.__init__)
    params = list(sig.parameters.keys())



def test_booleanvalue_value_booleanvalue_value_is_not_abstract():
    assert not inspect.isabstract(BooleanValue_value_BooleanValue_Value)


def test_booleanvalue_value_booleanvalue_value_constructor_exists():
    assert callable(BooleanValue_value_BooleanValue_Value.__init__)


def test_booleanvalue_value_booleanvalue_value_constructor_args():
    sig = inspect.signature(BooleanValue_value_BooleanValue_Value.__init__)
    params = list(sig.parameters.keys())



def test_evaluation_locus_evaluation_value_is_not_abstract():
    assert not inspect.isabstract(Evaluation_locus_Evaluation_Value)


def test_evaluation_locus_evaluation_value_constructor_exists():
    assert callable(Evaluation_locus_Evaluation_Value.__init__)


def test_evaluation_locus_evaluation_value_constructor_args():
    sig = inspect.signature(Evaluation_locus_Evaluation_Value.__init__)
    params = list(sig.parameters.keys())



def test_evaluation_specification_evaluation_value_is_not_abstract():
    assert not inspect.isabstract(Evaluation_specification_Evaluation_Value)


def test_evaluation_specification_evaluation_value_constructor_exists():
    assert callable(Evaluation_specification_Evaluation_Value.__init__)


def test_evaluation_specification_evaluation_value_constructor_args():
    sig = inspect.signature(Evaluation_specification_Evaluation_Value.__init__)
    params = list(sig.parameters.keys())



def test_pinactivation_actionactivation_value_is_not_abstract():
    assert not inspect.isabstract(PinActivation_actionActivation_Value)


def test_pinactivation_actionactivation_value_constructor_exists():
    assert callable(PinActivation_actionActivation_Value.__init__)


def test_pinactivation_actionactivation_value_constructor_args():
    sig = inspect.signature(PinActivation_actionActivation_Value.__init__)
    params = list(sig.parameters.keys())



def test_featurevalue_position_value_is_not_abstract():
    assert not inspect.isabstract(FeatureValue_position_Value)


def test_featurevalue_position_value_constructor_exists():
    assert callable(FeatureValue_position_Value.__init__)


def test_featurevalue_position_value_constructor_args():
    sig = inspect.signature(FeatureValue_position_Value.__init__)
    params = list(sig.parameters.keys())



def test_featurevalue_feature_value_is_not_abstract():
    assert not inspect.isabstract(FeatureValue_feature_Value)


def test_featurevalue_feature_value_constructor_exists():
    assert callable(FeatureValue_feature_Value.__init__)


def test_featurevalue_feature_value_constructor_args():
    sig = inspect.signature(FeatureValue_feature_Value.__init__)
    params = list(sig.parameters.keys())



def test_activitynodeactivationgroup_nodeactivations_value_is_not_abstract():
    assert not inspect.isabstract(ActivityNodeActivationGroup_nodeActivations_Value)


def test_activitynodeactivationgroup_nodeactivations_value_constructor_exists():
    assert callable(ActivityNodeActivationGroup_nodeActivations_Value.__init__)


def test_activitynodeactivationgroup_nodeactivations_value_constructor_args():
    sig = inspect.signature(ActivityNodeActivationGroup_nodeActivations_Value.__init__)
    params = list(sig.parameters.keys())



def test_element_semanticvisitor_value_is_not_abstract():
    assert not inspect.isabstract(Element_semanticVisitor_Value)


def test_element_semanticvisitor_value_constructor_exists():
    assert callable(Element_semanticVisitor_Value.__init__)


def test_element_semanticvisitor_value_constructor_args():
    sig = inspect.signature(Element_semanticVisitor_Value.__init__)
    params = list(sig.parameters.keys())



def test_execution_context_value_is_not_abstract():
    assert not inspect.isabstract(Execution_context_Value)


def test_execution_context_value_constructor_exists():
    assert callable(Execution_context_Value.__init__)


def test_execution_context_value_constructor_args():
    sig = inspect.signature(Execution_context_Value.__init__)
    params = list(sig.parameters.keys())



def test_execution_parametervalues_value_is_not_abstract():
    assert not inspect.isabstract(Execution_parameterValues_Value)


def test_execution_parametervalues_value_constructor_exists():
    assert callable(Execution_parameterValues_Value.__init__)


def test_execution_parametervalues_value_constructor_args():
    sig = inspect.signature(Execution_parameterValues_Value.__init__)
    params = list(sig.parameters.keys())



def test_actionactivation_firing_value_is_not_abstract():
    assert not inspect.isabstract(ActionActivation_firing_Value)


def test_actionactivation_firing_value_constructor_exists():
    assert callable(ActionActivation_firing_Value.__init__)


def test_actionactivation_firing_value_constructor_args():
    sig = inspect.signature(ActionActivation_firing_Value.__init__)
    params = list(sig.parameters.keys())



def test_actionactivation_pinactivations_value_is_not_abstract():
    assert not inspect.isabstract(ActionActivation_pinActivations_Value)


def test_actionactivation_pinactivations_value_constructor_exists():
    assert callable(ActionActivation_pinActivations_Value.__init__)


def test_actionactivation_pinactivations_value_constructor_args():
    sig = inspect.signature(ActionActivation_pinActivations_Value.__init__)
    params = list(sig.parameters.keys())



def test_parametervalue_parameter_parametervalue_value_is_not_abstract():
    assert not inspect.isabstract(ParameterValue_parameter_ParameterValue_Value)


def test_parametervalue_parameter_parametervalue_value_constructor_exists():
    assert callable(ParameterValue_parameter_ParameterValue_Value.__init__)


def test_parametervalue_parameter_parametervalue_value_constructor_args():
    sig = inspect.signature(ParameterValue_parameter_ParameterValue_Value.__init__)
    params = list(sig.parameters.keys())



def test_parametervalue_values_parametervalue_value_is_not_abstract():
    assert not inspect.isabstract(ParameterValue_values_ParameterValue_Value)


def test_parametervalue_values_parametervalue_value_constructor_exists():
    assert callable(ParameterValue_values_ParameterValue_Value.__init__)


def test_parametervalue_values_parametervalue_value_constructor_args():
    sig = inspect.signature(ParameterValue_values_ParameterValue_Value.__init__)
    params = list(sig.parameters.keys())



def test_primitivevalue_type_value_is_not_abstract():
    assert not inspect.isabstract(PrimitiveValue_type_Value)


def test_primitivevalue_type_value_constructor_exists():
    assert callable(PrimitiveValue_type_Value.__init__)


def test_primitivevalue_type_value_constructor_args():
    sig = inspect.signature(PrimitiveValue_type_Value.__init__)
    params = list(sig.parameters.keys())



def test_executor_locus_executor_value_is_not_abstract():
    assert not inspect.isabstract(Executor_locus_Executor_Value)


def test_executor_locus_executor_value_constructor_exists():
    assert callable(Executor_locus_Executor_Value.__init__)


def test_executor_locus_executor_value_constructor_args():
    sig = inspect.signature(Executor_locus_Executor_Value.__init__)
    params = list(sig.parameters.keys())



def test_activitynodeactivationgroup_edgeinstances_value_is_not_abstract():
    assert not inspect.isabstract(ActivityNodeActivationGroup_edgeInstances_Value)


def test_activitynodeactivationgroup_edgeinstances_value_constructor_exists():
    assert callable(ActivityNodeActivationGroup_edgeInstances_Value.__init__)


def test_activitynodeactivationgroup_edgeinstances_value_constructor_args():
    sig = inspect.signature(ActivityNodeActivationGroup_edgeInstances_Value.__init__)
    params = list(sig.parameters.keys())



def test_activitynodeactivationgroup_activityexecution_value_is_not_abstract():
    assert not inspect.isabstract(ActivityNodeActivationGroup_activityExecution_Value)


def test_activitynodeactivationgroup_activityexecution_value_constructor_exists():
    assert callable(ActivityNodeActivationGroup_activityExecution_Value.__init__)


def test_activitynodeactivationgroup_activityexecution_value_constructor_args():
    sig = inspect.signature(ActivityNodeActivationGroup_activityExecution_Value.__init__)
    params = list(sig.parameters.keys())



def test_executionfactory_locus_executionfactory_value_is_not_abstract():
    assert not inspect.isabstract(ExecutionFactory_locus_ExecutionFactory_Value)


def test_executionfactory_locus_executionfactory_value_constructor_exists():
    assert callable(ExecutionFactory_locus_ExecutionFactory_Value.__init__)


def test_executionfactory_locus_executionfactory_value_constructor_args():
    sig = inspect.signature(ExecutionFactory_locus_ExecutionFactory_Value.__init__)
    params = list(sig.parameters.keys())



def test_executionfactory_primitivebehaviorprototypes_value_is_not_abstract():
    assert not inspect.isabstract(ExecutionFactory_primitiveBehaviorPrototypes_Value)


def test_executionfactory_primitivebehaviorprototypes_value_constructor_exists():
    assert callable(ExecutionFactory_primitiveBehaviorPrototypes_Value.__init__)


def test_executionfactory_primitivebehaviorprototypes_value_constructor_args():
    sig = inspect.signature(ExecutionFactory_primitiveBehaviorPrototypes_Value.__init__)
    params = list(sig.parameters.keys())



def test_executionfactory_builtintypes_value_is_not_abstract():
    assert not inspect.isabstract(ExecutionFactory_builtInTypes_Value)


def test_executionfactory_builtintypes_value_constructor_exists():
    assert callable(ExecutionFactory_builtInTypes_Value.__init__)


def test_executionfactory_builtintypes_value_constructor_args():
    sig = inspect.signature(ExecutionFactory_builtInTypes_Value.__init__)
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
uml_umlTrace_ControlFlow_strategy = st.builds(
    uml_umlTrace_ControlFlow,
)
uml_umlTrace_TestIdentityAction_strategy = st.builds(
    uml_umlTrace_TestIdentityAction,
)
uml_umlTrace_AddVariableValueAction_strategy = st.builds(
    uml_umlTrace_AddVariableValueAction,
)
TracedWriteVariableAction_strategy = st.builds(
    TracedWriteVariableAction,
)
umlTrace_uml_TracedAddVariableValueAction_strategy = st.builds(
    umlTrace_uml_TracedAddVariableValueAction,
)
uml_TracedObjectNode_strategy = st.builds(
    uml_TracedObjectNode,
)
uml_umlTrace_ClearAssociationAction_strategy = st.builds(
    uml_umlTrace_ClearAssociationAction,
)
TracedBehavioralFeature_strategy = st.builds(
    TracedBehavioralFeature,
)
umlTrace_uml_TracedReception_strategy = st.builds(
    umlTrace_uml_TracedReception,
)
uml_umlTrace_ExpansionNode_strategy = st.builds(
    uml_umlTrace_ExpansionNode,
)
uml_umlTrace_LiteralNull_strategy = st.builds(
    uml_umlTrace_LiteralNull,
)
uml_umlTrace_RaiseExceptionAction_strategy = st.builds(
    uml_umlTrace_RaiseExceptionAction,
)
uml_umlTrace_Reception_strategy = st.builds(
    uml_umlTrace_Reception,
)
uml_umlTrace_Signal_strategy = st.builds(
    uml_umlTrace_Signal,
)
uml_umlTrace_ForkNode_strategy = st.builds(
    uml_umlTrace_ForkNode,
)
uml_umlTrace_DestroyObjectAction_strategy = st.builds(
    uml_umlTrace_DestroyObjectAction,
)
uml_umlTrace_Comment_strategy = st.builds(
    uml_umlTrace_Comment,
)
uml_umlTrace_ObjectFlow_strategy = st.builds(
    uml_umlTrace_ObjectFlow,
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
uml_umlTrace_PackageMerge_strategy = st.builds(
    uml_umlTrace_PackageMerge,
)
uml_umlTrace_ChangeEvent_strategy = st.builds(
    uml_umlTrace_ChangeEvent,
)
uml_umlTrace_Transition_strategy = st.builds(
    uml_umlTrace_Transition,
)
uml_umlTrace_LinkEndData_strategy = st.builds(
    uml_umlTrace_LinkEndData,
)
uml_umlTrace_TimeExpression_strategy = st.builds(
    uml_umlTrace_TimeExpression,
)
uml_umlTrace_Dependency_strategy = st.builds(
    uml_umlTrace_Dependency,
)
uml_umlTrace_ReadExtentAction_strategy = st.builds(
    uml_umlTrace_ReadExtentAction,
)
uml_umlTrace_InstanceValue_strategy = st.builds(
    uml_umlTrace_InstanceValue,
)
uml_umlTrace_Clause_strategy = st.builds(
    uml_umlTrace_Clause,
)
uml_umlTrace_ReplyAction_strategy = st.builds(
    uml_umlTrace_ReplyAction,
)
uml_umlTrace_UseCase_strategy = st.builds(
    uml_umlTrace_UseCase,
)
uml_umlTrace_CombinedFragment_strategy = st.builds(
    uml_umlTrace_CombinedFragment,
)
TracedVertex_strategy = st.builds(
    TracedVertex,
)
umlTrace_uml_TracedPseudostate_strategy = st.builds(
    umlTrace_uml_TracedPseudostate,
)
uml_umlTrace_InformationFlow_strategy = st.builds(
    uml_umlTrace_InformationFlow,
)
uml_TracedRelationship_strategy = st.builds(
    uml_TracedRelationship,
)
TracedBehavioredClassifier_strategy = st.builds(
    TracedBehavioredClassifier,
)
umlTrace_uml_TracedUseCase_strategy = st.builds(
    umlTrace_uml_TracedUseCase,
)
TracedActivityNode_strategy = st.builds(
    TracedActivityNode,
)
umlTrace_uml_TracedControlNode_strategy = st.builds(
    umlTrace_uml_TracedControlNode,
)
uml_umlTrace_Pseudostate_strategy = st.builds(
    uml_umlTrace_Pseudostate,
)
uml_umlTrace_InteractionOperand_strategy = st.builds(
    uml_umlTrace_InteractionOperand,
)
uml_umlTrace_Region_strategy = st.builds(
    uml_umlTrace_Region,
)
TracedState_strategy = st.builds(
    TracedState,
)
umlTrace_uml_TracedFinalState_strategy = st.builds(
    umlTrace_uml_TracedFinalState,
)
uml_umlTrace_DestroyLinkAction_strategy = st.builds(
    uml_umlTrace_DestroyLinkAction,
)
uml_umlTrace_InterruptibleActivityRegion_strategy = st.builds(
    uml_umlTrace_InterruptibleActivityRegion,
)
uml_umlTrace_DecisionNode_strategy = st.builds(
    uml_umlTrace_DecisionNode,
)
uml_umlTrace_ValueSpecificationAction_strategy = st.builds(
    uml_umlTrace_ValueSpecificationAction,
)
uml_umlTrace_InstanceSpecification_strategy = st.builds(
    uml_umlTrace_InstanceSpecification,
)
uml_umlTrace_OutputPin_strategy = st.builds(
    uml_umlTrace_OutputPin,
)
TracedStateMachine_strategy = st.builds(
    TracedStateMachine,
)
umlTrace_uml_TracedProtocolStateMachine_strategy = st.builds(
    umlTrace_uml_TracedProtocolStateMachine,
)
uml_umlTrace_ReadIsClassifiedObjectAction_strategy = st.builds(
    uml_umlTrace_ReadIsClassifiedObjectAction,
)
TracedPackage_strategy = st.builds(
    TracedPackage,
)
umlTrace_uml_TracedModel_strategy = st.builds(
    umlTrace_uml_TracedModel,
)
umlTrace_uml_TracedProfile_strategy = st.builds(
    umlTrace_uml_TracedProfile,
)
uml_umlTrace_CallOperationAction_strategy = st.builds(
    uml_umlTrace_CallOperationAction,
)
uml_umlTrace_Trigger_strategy = st.builds(
    uml_umlTrace_Trigger,
)
uml_umlTrace_Interval_strategy = st.builds(
    uml_umlTrace_Interval,
)
TracedStructuredClassifier_strategy = st.builds(
    TracedStructuredClassifier,
)
umlTrace_uml_TracedEncapsulatedClassifier_strategy = st.builds(
    umlTrace_uml_TracedEncapsulatedClassifier,
)
uml_umlTrace_Image_strategy = st.builds(
    uml_umlTrace_Image,
)
uml_umlTrace_ConnectorEnd_strategy = st.builds(
    uml_umlTrace_ConnectorEnd,
)
uml_TracedEvent_strategy = st.builds(
    uml_TracedEvent,
)
TracedInputPin_strategy = st.builds(
    TracedInputPin,
)
umlTrace_uml_TracedValuePin_strategy = st.builds(
    umlTrace_uml_TracedValuePin,
)
umlTrace_uml_TracedActionInputPin_strategy = st.builds(
    umlTrace_uml_TracedActionInputPin,
)
uml_umlTrace_Parameter_strategy = st.builds(
    uml_umlTrace_Parameter,
)
uml_umlTrace_ProfileApplication_strategy = st.builds(
    uml_umlTrace_ProfileApplication,
)
TracedMultiplicityElement_strategy = st.builds(
    TracedMultiplicityElement,
)
umlTrace_uml_TracedConnectorEnd_strategy = st.builds(
    umlTrace_uml_TracedConnectorEnd,
)
uml_umlTrace_TemplateParameter_strategy = st.builds(
    uml_umlTrace_TemplateParameter,
)
uml_umlTrace_ClearVariableAction_strategy = st.builds(
    uml_umlTrace_ClearVariableAction,
)
uml_umlTrace_LiteralInteger_strategy = st.builds(
    uml_umlTrace_LiteralInteger,
)
uml_umlTrace_InitialNode_strategy = st.builds(
    uml_umlTrace_InitialNode,
)
uml_umlTrace_QualifierValue_strategy = st.builds(
    uml_umlTrace_QualifierValue,
)
uml_umlTrace_LiteralBoolean_strategy = st.builds(
    uml_umlTrace_LiteralBoolean,
)
uml_umlTrace_Message_strategy = st.builds(
    uml_umlTrace_Message,
)
uml_umlTrace_ReadVariableAction_strategy = st.builds(
    uml_umlTrace_ReadVariableAction,
)
uml_umlTrace_Extend_strategy = st.builds(
    uml_umlTrace_Extend,
)
uml_TracedMessageEnd_strategy = st.builds(
    uml_TracedMessageEnd,
)
uml_umlTrace_ReadLinkObjectEndQualifierAction_strategy = st.builds(
    uml_umlTrace_ReadLinkObjectEndQualifierAction,
)
uml_umlTrace_TemplateParameterSubstitution_strategy = st.builds(
    uml_umlTrace_TemplateParameterSubstitution,
)
uml_umlTrace_CreateLinkAction_strategy = st.builds(
    uml_umlTrace_CreateLinkAction,
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
TracedInteractionUse_strategy = st.builds(
    TracedInteractionUse,
)
umlTrace_uml_TracedPartDecomposition_strategy = st.builds(
    umlTrace_uml_TracedPartDecomposition,
)
uml_umlTrace_Generalization_strategy = st.builds(
    uml_umlTrace_Generalization,
)
uml_umlTrace_StructuredActivityNode_strategy = st.builds(
    uml_umlTrace_StructuredActivityNode,
)
uml_umlTrace_MergeNode_strategy = st.builds(
    uml_umlTrace_MergeNode,
)
uml_umlTrace_ReadStructuralFeatureAction_strategy = st.builds(
    uml_umlTrace_ReadStructuralFeatureAction,
)
uml_TracedEncapsulatedClassifier_strategy = st.builds(
    uml_TracedEncapsulatedClassifier,
)
uml_umlTrace_Duration_strategy = st.builds(
    uml_umlTrace_Duration,
)
uml_TracedObservation_strategy = st.builds(
    uml_TracedObservation,
)
uml_umlTrace_ParameterSet_strategy = st.builds(
    uml_umlTrace_ParameterSet,
)
uml_umlTrace_LiteralUnlimitedNatural_strategy = st.builds(
    uml_umlTrace_LiteralUnlimitedNatural,
)
uml_umlTrace_Class_strategy = st.builds(
    uml_umlTrace_Class,
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
uml_umlTrace_ActivityParameterNode_strategy = st.builds(
    uml_umlTrace_ActivityParameterNode,
)
uml_umlTrace_State_strategy = st.builds(
    uml_umlTrace_State,
)
uml_TracedBehavioralFeature_strategy = st.builds(
    uml_TracedBehavioralFeature,
)
uml_TracedVertex_strategy = st.builds(
    uml_TracedVertex,
)
ecore_umlTrace_EAnnotation_strategy = st.builds(
    ecore_umlTrace_EAnnotation,
)
umlTrace_ecore_TracedEModelElement_strategy = st.builds(
    umlTrace_ecore_TracedEModelElement,
)
uml_umlTrace_CentralBufferNode_strategy = st.builds(
    uml_umlTrace_CentralBufferNode,
)
umlTrace_uml_TracedCentralBufferNode_strategy = st.builds(
    umlTrace_uml_TracedCentralBufferNode,
)
uml_umlTrace_UnmarshallAction_strategy = st.builds(
    uml_umlTrace_UnmarshallAction,
)
TracedArtifact_strategy = st.builds(
    TracedArtifact,
)
umlTrace_uml_TracedDeploymentSpecification_strategy = st.builds(
    umlTrace_uml_TracedDeploymentSpecification,
)
TracedOpaqueBehavior_strategy = st.builds(
    TracedOpaqueBehavior,
)
umlTrace_uml_TracedFunctionBehavior_strategy = st.builds(
    umlTrace_uml_TracedFunctionBehavior,
)
uml_umlTrace_OpaqueExpression_strategy = st.builds(
    uml_umlTrace_OpaqueExpression,
)
uml_umlTrace_ClearStructuralFeatureAction_strategy = st.builds(
    uml_umlTrace_ClearStructuralFeatureAction,
)
uml_umlTrace_TemplateBinding_strategy = st.builds(
    uml_umlTrace_TemplateBinding,
)
umlTrace_uml_TracedExecutableNode_strategy = st.builds(
    umlTrace_uml_TracedExecutableNode,
)
uml_umlTrace_BehaviorExecutionSpecification_strategy = st.builds(
    uml_umlTrace_BehaviorExecutionSpecification,
)
uml_umlTrace_Actor_strategy = st.builds(
    uml_umlTrace_Actor,
)
umlTrace_uml_TracedActor_strategy = st.builds(
    umlTrace_uml_TracedActor,
)
TracedAcceptEventAction_strategy = st.builds(
    TracedAcceptEventAction,
)
umlTrace_uml_TracedAcceptCallAction_strategy = st.builds(
    umlTrace_uml_TracedAcceptCallAction,
)
uml_umlTrace_ReadSelfAction_strategy = st.builds(
    uml_umlTrace_ReadSelfAction,
)
uml_umlTrace_ActionExecutionSpecification_strategy = st.builds(
    uml_umlTrace_ActionExecutionSpecification,
)
TracedExecutionSpecification_strategy = st.builds(
    TracedExecutionSpecification,
)
umlTrace_uml_TracedBehaviorExecutionSpecification_strategy = st.builds(
    umlTrace_uml_TracedBehaviorExecutionSpecification,
)
umlTrace_uml_TracedActionExecutionSpecification_strategy = st.builds(
    umlTrace_uml_TracedActionExecutionSpecification,
)
uml_umlTrace_ConnectionPointReference_strategy = st.builds(
    uml_umlTrace_ConnectionPointReference,
)
umlTrace_uml_TracedConnectionPointReference_strategy = st.builds(
    umlTrace_uml_TracedConnectionPointReference,
)
uml_umlTrace_CallBehaviorAction_strategy = st.builds(
    uml_umlTrace_CallBehaviorAction,
)
uml_umlTrace_GeneralOrdering_strategy = st.builds(
    uml_umlTrace_GeneralOrdering,
)
uml_umlTrace_Gate_strategy = st.builds(
    uml_umlTrace_Gate,
)
TracedMessageEnd_strategy = st.builds(
    TracedMessageEnd,
)
TracedInterval_strategy = st.builds(
    TracedInterval,
)
umlTrace_uml_TracedGate_strategy = st.builds(
    umlTrace_uml_TracedGate,
)
uml_umlTrace_ReclassifyObjectAction_strategy = st.builds(
    uml_umlTrace_ReclassifyObjectAction,
)
umlTrace_uml_TracedTimeInterval_strategy = st.builds(
    umlTrace_uml_TracedTimeInterval,
)
uml_umlTrace_RemoveVariableValueAction_strategy = st.builds(
    uml_umlTrace_RemoveVariableValueAction,
)
TracedProperty_strategy = st.builds(
    TracedProperty,
)
umlTrace_uml_TracedRemoveVariableValueAction_strategy = st.builds(
    umlTrace_uml_TracedRemoveVariableValueAction,
)
umlTrace_uml_TracedPort_strategy = st.builds(
    umlTrace_uml_TracedPort,
)
uml_umlTrace_LiteralReal_strategy = st.builds(
    uml_umlTrace_LiteralReal,
)
uml_TracedStructuredClassifier_strategy = st.builds(
    uml_TracedStructuredClassifier,
)
uml_umlTrace_InformationItem_strategy = st.builds(
    uml_umlTrace_InformationItem,
)
uml_umlTrace_InteractionUse_strategy = st.builds(
    uml_umlTrace_InteractionUse,
)
TracedElement_strategy = st.builds(
    TracedElement,
)
umlTrace_uml_TracedTemplateableElement_strategy = st.builds(
    umlTrace_uml_TracedTemplateableElement,
)
umlTrace_uml_TracedQualifierValue_strategy = st.builds(
    umlTrace_uml_TracedQualifierValue,
)
umlTrace_uml_TracedClause_strategy = st.builds(
    umlTrace_uml_TracedClause,
)
umlTrace_uml_TracedImage_strategy = st.builds(
    umlTrace_uml_TracedImage,
)
umlTrace_uml_TracedParameterableElement_strategy = st.builds(
    umlTrace_uml_TracedParameterableElement,
)
umlTrace_uml_TracedTemplateParameterSubstitution_strategy = st.builds(
    umlTrace_uml_TracedTemplateParameterSubstitution,
)
umlTrace_uml_TracedTemplateParameter_strategy = st.builds(
    umlTrace_uml_TracedTemplateParameter,
)
umlTrace_uml_TracedLinkEndData_strategy = st.builds(
    umlTrace_uml_TracedLinkEndData,
)
umlTrace_uml_TracedComment_strategy = st.builds(
    umlTrace_uml_TracedComment,
)
umlTrace_uml_TracedTemplateSignature_strategy = st.builds(
    umlTrace_uml_TracedTemplateSignature,
)
uml_umlTrace_StateInvariant_strategy = st.builds(
    uml_umlTrace_StateInvariant,
)
uml_umlTrace_Association_strategy = st.builds(
    uml_umlTrace_Association,
)
uml_umlTrace_Collaboration_strategy = st.builds(
    uml_umlTrace_Collaboration,
)
uml_umlTrace_Variable_strategy = st.builds(
    uml_umlTrace_Variable,
)
uml_umlTrace_ExceptionHandler_strategy = st.builds(
    uml_umlTrace_ExceptionHandler,
)
TracedCombinedFragment_strategy = st.builds(
    TracedCombinedFragment,
)
umlTrace_uml_TracedExceptionHandler_strategy = st.builds(
    umlTrace_uml_TracedExceptionHandler,
)
umlTrace_uml_TracedConsiderIgnoreFragment_strategy = st.builds(
    umlTrace_uml_TracedConsiderIgnoreFragment,
)
uml_TracedExecutionSpecification_strategy = st.builds(
    uml_TracedExecutionSpecification,
)
uml_umlTrace_Expression_strategy = st.builds(
    uml_umlTrace_Expression,
)
TracedOccurrenceSpecification_strategy = st.builds(
    TracedOccurrenceSpecification,
)
TracedValueSpecification_strategy = st.builds(
    TracedValueSpecification,
)
umlTrace_uml_TracedInterval_strategy = st.builds(
    umlTrace_uml_TracedInterval,
)
umlTrace_uml_TracedDuration_strategy = st.builds(
    umlTrace_uml_TracedDuration,
)
umlTrace_uml_TracedOpaqueExpression_strategy = st.builds(
    umlTrace_uml_TracedOpaqueExpression,
)
umlTrace_uml_TracedInstanceValue_strategy = st.builds(
    umlTrace_uml_TracedInstanceValue,
)
umlTrace_uml_TracedTimeExpression_strategy = st.builds(
    umlTrace_uml_TracedTimeExpression,
)
umlTrace_uml_TracedExecutionOccurrenceSpecification_strategy = st.builds(
    umlTrace_uml_TracedExecutionOccurrenceSpecification,
)
umlTrace_uml_TracedExpression_strategy = st.builds(
    umlTrace_uml_TracedExpression,
)
uml_umlTrace_PackageImport_strategy = st.builds(
    uml_umlTrace_PackageImport,
)
uml_umlTrace_ReadLinkAction_strategy = st.builds(
    uml_umlTrace_ReadLinkAction,
)
uml_TracedTemplateableElement_strategy = st.builds(
    uml_TracedTemplateableElement,
)
uml_TracedType_strategy = st.builds(
    uml_TracedType,
)
uml_TracedRedefinableElement_strategy = st.builds(
    uml_TracedRedefinableElement,
)
uml_umlTrace_Operation_strategy = st.builds(
    uml_umlTrace_Operation,
)
uml_TracedNamespace_strategy = st.builds(
    uml_TracedNamespace,
)
umlTrace_uml_TracedState_strategy = st.builds(
    umlTrace_uml_TracedState,
)
umlTrace_uml_TracedTransition_strategy = st.builds(
    umlTrace_uml_TracedTransition,
)
umlTrace_uml_TracedRegion_strategy = st.builds(
    umlTrace_uml_TracedRegion,
)
umlTrace_uml_TracedClassifier_strategy = st.builds(
    umlTrace_uml_TracedClassifier,
)
TracedNamedElement_strategy = st.builds(
    TracedNamedElement,
)
umlTrace_uml_TracedTrigger_strategy = st.builds(
    umlTrace_uml_TracedTrigger,
)
umlTrace_uml_TracedVertex_strategy = st.builds(
    umlTrace_uml_TracedVertex,
)
umlTrace_uml_TracedParameterSet_strategy = st.builds(
    umlTrace_uml_TracedParameterSet,
)
umlTrace_uml_TracedDeploymentTarget_strategy = st.builds(
    umlTrace_uml_TracedDeploymentTarget,
)
umlTrace_uml_TracedNamespace_strategy = st.builds(
    umlTrace_uml_TracedNamespace,
)
umlTrace_uml_TracedGeneralOrdering_strategy = st.builds(
    umlTrace_uml_TracedGeneralOrdering,
)
umlTrace_uml_TracedTypedElement_strategy = st.builds(
    umlTrace_uml_TracedTypedElement,
)
umlTrace_uml_TracedRedefinableElement_strategy = st.builds(
    umlTrace_uml_TracedRedefinableElement,
)
umlTrace_uml_TracedMessage_strategy = st.builds(
    umlTrace_uml_TracedMessage,
)
umlTrace_uml_TracedMessageEnd_strategy = st.builds(
    umlTrace_uml_TracedMessageEnd,
)
umlTrace_uml_TracedInteractionFragment_strategy = st.builds(
    umlTrace_uml_TracedInteractionFragment,
)
uml_umlTrace_FlowFinalNode_strategy = st.builds(
    uml_umlTrace_FlowFinalNode,
)
TracedCentralBufferNode_strategy = st.builds(
    TracedCentralBufferNode,
)
umlTrace_uml_TracedDataStoreNode_strategy = st.builds(
    umlTrace_uml_TracedDataStoreNode,
)
uml_umlTrace_DurationObservation_strategy = st.builds(
    uml_umlTrace_DurationObservation,
)
uml_TracedNamedElement_strategy = st.builds(
    uml_TracedNamedElement,
)
TracedObservation_strategy = st.builds(
    TracedObservation,
)
umlTrace_uml_TracedDurationObservation_strategy = st.builds(
    umlTrace_uml_TracedDurationObservation,
)
uml_umlTrace_ActivityFinalNode_strategy = st.builds(
    uml_umlTrace_ActivityFinalNode,
)
TracedFinalNode_strategy = st.builds(
    TracedFinalNode,
)
umlTrace_uml_TracedFlowFinalNode_strategy = st.builds(
    umlTrace_uml_TracedFlowFinalNode,
)
umlTrace_uml_TracedActivityFinalNode_strategy = st.builds(
    umlTrace_uml_TracedActivityFinalNode,
)
TracedLinkAction_strategy = st.builds(
    TracedLinkAction,
)
umlTrace_uml_TracedWriteLinkAction_strategy = st.builds(
    umlTrace_uml_TracedWriteLinkAction,
)
umlTrace_uml_TracedReadLinkAction_strategy = st.builds(
    umlTrace_uml_TracedReadLinkAction,
)
uml_umlTrace_AddStructuralFeatureValueAction_strategy = st.builds(
    uml_umlTrace_AddStructuralFeatureValueAction,
)
TracedInstanceSpecification_strategy = st.builds(
    TracedInstanceSpecification,
)
umlTrace_uml_TracedEnumerationLiteral_strategy = st.builds(
    umlTrace_uml_TracedEnumerationLiteral,
)
uml_umlTrace_AcceptEventAction_strategy = st.builds(
    uml_umlTrace_AcceptEventAction,
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
TracedBehavior_strategy = st.builds(
    TracedBehavior,
)
umlTrace_uml_TracedActivity_strategy = st.builds(
    umlTrace_uml_TracedActivity,
)
umlTrace_uml_TracedOpaqueBehavior_strategy = st.builds(
    umlTrace_uml_TracedOpaqueBehavior,
)
uml_umlTrace_SendSignalAction_strategy = st.builds(
    uml_umlTrace_SendSignalAction,
)
TracedInvocationAction_strategy = st.builds(
    TracedInvocationAction,
)
umlTrace_uml_TracedCallAction_strategy = st.builds(
    umlTrace_uml_TracedCallAction,
)
umlTrace_uml_TracedSendSignalAction_strategy = st.builds(
    umlTrace_uml_TracedSendSignalAction,
)
uml_umlTrace_RemoveStructuralFeatureValueAction_strategy = st.builds(
    uml_umlTrace_RemoveStructuralFeatureValueAction,
)
TracedWriteStructuralFeatureAction_strategy = st.builds(
    TracedWriteStructuralFeatureAction,
)
umlTrace_uml_TracedAddStructuralFeatureValueAction_strategy = st.builds(
    umlTrace_uml_TracedAddStructuralFeatureValueAction,
)
uml_TracedBehavioredClassifier_strategy = st.builds(
    uml_TracedBehavioredClassifier,
)
umlTrace_uml_TracedClass_strategy = st.builds(
    umlTrace_uml_TracedClass,
)
umlTrace_uml_TracedCollaboration_strategy = st.builds(
    umlTrace_uml_TracedCollaboration,
)
TracedRealization_strategy = st.builds(
    TracedRealization,
)
umlTrace_uml_TracedSubstitution_strategy = st.builds(
    umlTrace_uml_TracedSubstitution,
)
umlTrace_uml_TracedInterfaceRealization_strategy = st.builds(
    umlTrace_uml_TracedInterfaceRealization,
)
TracedIntervalConstraint_strategy = st.builds(
    TracedIntervalConstraint,
)
umlTrace_uml_TracedDurationConstraint_strategy = st.builds(
    umlTrace_uml_TracedDurationConstraint,
)
umlTrace_uml_TracedTimeConstraint_strategy = st.builds(
    umlTrace_uml_TracedTimeConstraint,
)
uml_umlTrace_Artifact_strategy = st.builds(
    uml_umlTrace_Artifact,
)
uml_TracedDeploymentTarget_strategy = st.builds(
    uml_TracedDeploymentTarget,
)
uml_TracedConnectableElement_strategy = st.builds(
    uml_TracedConnectableElement,
)
umlTrace_uml_TracedRemoveStructuralFeatureValueAction_strategy = st.builds(
    umlTrace_uml_TracedRemoveStructuralFeatureValueAction,
)
uml_umlTrace_Continuation_strategy = st.builds(
    uml_umlTrace_Continuation,
)
TracedInteractionFragment_strategy = st.builds(
    TracedInteractionFragment,
)
umlTrace_uml_TracedStateInvariant_strategy = st.builds(
    umlTrace_uml_TracedStateInvariant,
)
umlTrace_uml_TracedCombinedFragment_strategy = st.builds(
    umlTrace_uml_TracedCombinedFragment,
)
umlTrace_uml_TracedInteractionUse_strategy = st.builds(
    umlTrace_uml_TracedInteractionUse,
)
umlTrace_uml_TracedContinuation_strategy = st.builds(
    umlTrace_uml_TracedContinuation,
)
uml_umlTrace_Property_strategy = st.builds(
    uml_umlTrace_Property,
)
uml_umlTrace_Connector_strategy = st.builds(
    uml_umlTrace_Connector,
)
uml_TracedBehavior_strategy = st.builds(
    uml_TracedBehavior,
)
TracedFeature_strategy = st.builds(
    TracedFeature,
)
umlTrace_uml_TracedConnector_strategy = st.builds(
    umlTrace_uml_TracedConnector,
)
uml_TracedMultiplicityElement_strategy = st.builds(
    uml_TracedMultiplicityElement,
)
umlTrace_uml_TracedParameter_strategy = st.builds(
    umlTrace_uml_TracedParameter,
)
umlTrace_uml_TracedVariable_strategy = st.builds(
    umlTrace_uml_TracedVariable,
)
umlTrace_uml_TracedPin_strategy = st.builds(
    umlTrace_uml_TracedPin,
)
uml_TracedTypedElement_strategy = st.builds(
    uml_TracedTypedElement,
)
uml_TracedFeature_strategy = st.builds(
    uml_TracedFeature,
)
umlTrace_uml_TracedBehavioralFeature_strategy = st.builds(
    umlTrace_uml_TracedBehavioralFeature,
)
umlTrace_uml_TracedStructuralFeature_strategy = st.builds(
    umlTrace_uml_TracedStructuralFeature,
)
umlTrace_Input_TracedInputParameterValues_strategy = st.builds(
    umlTrace_Input_TracedInputParameterValues,
)
TracedAssociation_strategy = st.builds(
    TracedAssociation,
)
umlTrace_uml_TracedCommunicationPath_strategy = st.builds(
    umlTrace_uml_TracedCommunicationPath,
)
uml_umlTrace_DataType_strategy = st.builds(
    uml_umlTrace_DataType,
)
TracedClassifier_strategy = st.builds(
    TracedClassifier,
)
umlTrace_uml_TracedStructuredClassifier_strategy = st.builds(
    umlTrace_uml_TracedStructuredClassifier,
)
umlTrace_uml_TracedSignal_strategy = st.builds(
    umlTrace_uml_TracedSignal,
)
umlTrace_uml_TracedInformationItem_strategy = st.builds(
    umlTrace_uml_TracedInformationItem,
)
umlTrace_uml_TracedDataType_strategy = st.builds(
    umlTrace_uml_TracedDataType,
)
uml_umlTrace_OpaqueAction_strategy = st.builds(
    uml_umlTrace_OpaqueAction,
)
TracedAction_strategy = st.builds(
    TracedAction,
)
umlTrace_uml_TracedReadIsClassifiedObjectAction_strategy = st.builds(
    umlTrace_uml_TracedReadIsClassifiedObjectAction,
)
umlTrace_uml_TracedReclassifyObjectAction_strategy = st.builds(
    umlTrace_uml_TracedReclassifyObjectAction,
)
umlTrace_uml_TracedInvocationAction_strategy = st.builds(
    umlTrace_uml_TracedInvocationAction,
)
umlTrace_uml_TracedReplyAction_strategy = st.builds(
    umlTrace_uml_TracedReplyAction,
)
umlTrace_uml_TracedTestIdentityAction_strategy = st.builds(
    umlTrace_uml_TracedTestIdentityAction,
)
umlTrace_uml_TracedLinkAction_strategy = st.builds(
    umlTrace_uml_TracedLinkAction,
)
umlTrace_uml_TracedReadSelfAction_strategy = st.builds(
    umlTrace_uml_TracedReadSelfAction,
)
umlTrace_uml_TracedDestroyObjectAction_strategy = st.builds(
    umlTrace_uml_TracedDestroyObjectAction,
)
umlTrace_uml_TracedClearAssociationAction_strategy = st.builds(
    umlTrace_uml_TracedClearAssociationAction,
)
umlTrace_uml_TracedRaiseExceptionAction_strategy = st.builds(
    umlTrace_uml_TracedRaiseExceptionAction,
)
umlTrace_uml_TracedReadExtentAction_strategy = st.builds(
    umlTrace_uml_TracedReadExtentAction,
)
umlTrace_uml_TracedReadLinkObjectEndQualifierAction_strategy = st.builds(
    umlTrace_uml_TracedReadLinkObjectEndQualifierAction,
)
umlTrace_uml_TracedUnmarshallAction_strategy = st.builds(
    umlTrace_uml_TracedUnmarshallAction,
)
umlTrace_uml_TracedAcceptEventAction_strategy = st.builds(
    umlTrace_uml_TracedAcceptEventAction,
)
umlTrace_uml_TracedValueSpecificationAction_strategy = st.builds(
    umlTrace_uml_TracedValueSpecificationAction,
)
umlTrace_uml_TracedOpaqueAction_strategy = st.builds(
    umlTrace_uml_TracedOpaqueAction,
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
TracedWriteStructuralFeatureActionActivation_strategy = st.builds(
    TracedWriteStructuralFeatureActionActivation,
)
umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation_strategy = st.builds(
    umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation,
)
TracedOpaqueBehaviorExecution_strategy = st.builds(
    TracedOpaqueBehaviorExecution,
)
umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_strategy = st.builds(
    umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution,
)
umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_strategy = st.builds(
    umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution,
)
umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_strategy = st.builds(
    umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution,
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
TracedMessageOccurrenceSpecification_strategy = st.builds(
    TracedMessageOccurrenceSpecification,
)
umlTrace_uml_TracedDestructionOccurrenceSpecification_strategy = st.builds(
    umlTrace_uml_TracedDestructionOccurrenceSpecification,
)
uml_umlTrace_Include_strategy = st.builds(
    uml_umlTrace_Include,
)
uml_TracedDirectedRelationship_strategy = st.builds(
    uml_TracedDirectedRelationship,
)
umlTrace_uml_TracedExtend_strategy = st.builds(
    umlTrace_uml_TracedExtend,
)
umlTrace_uml_TracedInclude_strategy = st.builds(
    umlTrace_uml_TracedInclude,
)
umlTrace_uml_TracedDurationInterval_strategy = st.builds(
    umlTrace_uml_TracedDurationInterval,
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
umlTrace_uml_TracedVariableAction_strategy = st.builds(
    umlTrace_uml_TracedVariableAction,
)
uml_umlTrace_ActivityPartition_strategy = st.builds(
    uml_umlTrace_ActivityPartition,
)
uml_TracedActivityGroup_strategy = st.builds(
    uml_TracedActivityGroup,
)
ActivityContent_strategy = st.builds(
    ActivityContent,
)
umlTrace_uml_TracedActivityGroup_strategy = st.builds(
    umlTrace_uml_TracedActivityGroup,
)
umlTrace_uml_TracedActivityNode_strategy = st.builds(
    umlTrace_uml_TracedActivityNode,
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
uml_umlTrace_CollaborationUse_strategy = st.builds(
    uml_umlTrace_CollaborationUse,
)
umlTrace_uml_TracedCollaborationUse_strategy = st.builds(
    umlTrace_uml_TracedCollaborationUse,
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
uml_umlTrace_ProtocolConformance_strategy = st.builds(
    uml_umlTrace_ProtocolConformance,
)
TracedCreateLinkAction_strategy = st.builds(
    TracedCreateLinkAction,
)
umlTrace_uml_TracedCreateLinkObjectAction_strategy = st.builds(
    umlTrace_uml_TracedCreateLinkObjectAction,
)
uml_umlTrace_TimeObservation_strategy = st.builds(
    uml_umlTrace_TimeObservation,
)
umlTrace_uml_TracedTimeObservation_strategy = st.builds(
    umlTrace_uml_TracedTimeObservation,
)
umlTrace_uml_TracedExecutionSpecification_strategy = st.builds(
    umlTrace_uml_TracedExecutionSpecification,
)
uml_umlTrace_Lifeline_strategy = st.builds(
    uml_umlTrace_Lifeline,
)
TracedVariableAction_strategy = st.builds(
    TracedVariableAction,
)
umlTrace_uml_TracedClearVariableAction_strategy = st.builds(
    umlTrace_uml_TracedClearVariableAction,
)
umlTrace_uml_TracedReadVariableAction_strategy = st.builds(
    umlTrace_uml_TracedReadVariableAction,
)
umlTrace_uml_TracedWriteVariableAction_strategy = st.builds(
    umlTrace_uml_TracedWriteVariableAction,
)
umlTrace_uml_TracedSendObjectAction_strategy = st.builds(
    umlTrace_uml_TracedSendObjectAction,
)
umlTrace_uml_TracedRelationship_strategy = st.builds(
    umlTrace_uml_TracedRelationship,
)
TracedTemplateParameter_strategy = st.builds(
    TracedTemplateParameter,
)
umlTrace_uml_TracedOperationTemplateParameter_strategy = st.builds(
    umlTrace_uml_TracedOperationTemplateParameter,
)
umlTrace_uml_TracedClassifierTemplateParameter_strategy = st.builds(
    umlTrace_uml_TracedClassifierTemplateParameter,
)
umlTrace_uml_TracedConnectableElementTemplateParameter_strategy = st.builds(
    umlTrace_uml_TracedConnectableElementTemplateParameter,
)
uml_umlTrace_CallEvent_strategy = st.builds(
    uml_umlTrace_CallEvent,
)
uml_umlTrace_StartClassifierBehaviorAction_strategy = st.builds(
    uml_umlTrace_StartClassifierBehaviorAction,
)
umlTrace_uml_TracedLifeline_strategy = st.builds(
    umlTrace_uml_TracedLifeline,
)
uml_umlTrace_SendObjectAction_strategy = st.builds(
    uml_umlTrace_SendObjectAction,
)
uml_TracedAction_strategy = st.builds(
    uml_TracedAction,
)
umlTrace_uml_TracedStructuredActivityNode_strategy = st.builds(
    umlTrace_uml_TracedStructuredActivityNode,
)
uml_TracedInteractionFragment_strategy = st.builds(
    uml_TracedInteractionFragment,
)
umlTrace_uml_TracedInteractionOperand_strategy = st.builds(
    umlTrace_uml_TracedInteractionOperand,
)
umlTrace_uml_TracedInteraction_strategy = st.builds(
    umlTrace_uml_TracedInteraction,
)
umlTrace_uml_TracedStateMachine_strategy = st.builds(
    umlTrace_uml_TracedStateMachine,
)
umlTrace_uml_TracedExtensionEnd_strategy = st.builds(
    umlTrace_uml_TracedExtensionEnd,
)
umlTrace_uml_TracedStartClassifierBehaviorAction_strategy = st.builds(
    umlTrace_uml_TracedStartClassifierBehaviorAction,
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
uml_umlTrace_LiteralString_strategy = st.builds(
    uml_umlTrace_LiteralString,
)
TracedLiteralSpecification_strategy = st.builds(
    TracedLiteralSpecification,
)
umlTrace_uml_TracedLiteralUnlimitedNatural_strategy = st.builds(
    umlTrace_uml_TracedLiteralUnlimitedNatural,
)
umlTrace_uml_TracedLiteralInteger_strategy = st.builds(
    umlTrace_uml_TracedLiteralInteger,
)
umlTrace_uml_TracedLiteralReal_strategy = st.builds(
    umlTrace_uml_TracedLiteralReal,
)
umlTrace_uml_TracedLiteralBoolean_strategy = st.builds(
    umlTrace_uml_TracedLiteralBoolean,
)
umlTrace_uml_TracedLiteralNull_strategy = st.builds(
    umlTrace_uml_TracedLiteralNull,
)
umlTrace_uml_TracedLiteralString_strategy = st.builds(
    umlTrace_uml_TracedLiteralString,
)
umlTrace_uml_TracedNamedElement_strategy = st.builds(
    umlTrace_uml_TracedNamedElement,
)
uml_umlTrace_AnyReceiveEvent_strategy = st.builds(
    uml_umlTrace_AnyReceiveEvent,
)
uml_umlTrace_ReadLinkObjectEndAction_strategy = st.builds(
    uml_umlTrace_ReadLinkObjectEndAction,
)
uml_umlTrace_Interface_strategy = st.builds(
    uml_umlTrace_Interface,
)
umlTrace_uml_TracedReadLinkObjectEndAction_strategy = st.builds(
    umlTrace_uml_TracedReadLinkObjectEndAction,
)
umlTrace_uml_TracedOccurrenceSpecification_strategy = st.builds(
    umlTrace_uml_TracedOccurrenceSpecification,
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
uml_umlTrace_CreateObjectAction_strategy = st.builds(
    uml_umlTrace_CreateObjectAction,
)
umlTrace_uml_TracedCreateObjectAction_strategy = st.builds(
    umlTrace_uml_TracedCreateObjectAction,
)
umlTrace_uml_TracedInterface_strategy = st.builds(
    umlTrace_uml_TracedInterface,
)
TracedClass_strategy = st.builds(
    TracedClass,
)
umlTrace_uml_TracedBehavior_strategy = st.builds(
    umlTrace_uml_TracedBehavior,
)
umlTrace_uml_TracedComponent_strategy = st.builds(
    umlTrace_uml_TracedComponent,
)
umlTrace_uml_TracedStereotype_strategy = st.builds(
    umlTrace_uml_TracedStereotype,
)
umlTrace_uml_TracedDeployedArtifact_strategy = st.builds(
    umlTrace_uml_TracedDeployedArtifact,
)
uml_umlTrace_OccurrenceSpecification_strategy = st.builds(
    uml_umlTrace_OccurrenceSpecification,
)
uml_umlTrace_ExtensionPoint_strategy = st.builds(
    uml_umlTrace_ExtensionPoint,
)
uml_umlTrace_SignalEvent_strategy = st.builds(
    uml_umlTrace_SignalEvent,
)
TracedMessageEvent_strategy = st.builds(
    TracedMessageEvent,
)
umlTrace_uml_TracedAnyReceiveEvent_strategy = st.builds(
    umlTrace_uml_TracedAnyReceiveEvent,
)
umlTrace_uml_TracedCallEvent_strategy = st.builds(
    umlTrace_uml_TracedCallEvent,
)
umlTrace_uml_TracedSignalEvent_strategy = st.builds(
    umlTrace_uml_TracedSignalEvent,
)
uml_umlTrace_Slot_strategy = st.builds(
    uml_umlTrace_Slot,
)
uml_umlTrace_ElementImport_strategy = st.builds(
    uml_umlTrace_ElementImport,
)
TracedDirectedRelationship_strategy = st.builds(
    TracedDirectedRelationship,
)
umlTrace_uml_TracedPackageImport_strategy = st.builds(
    umlTrace_uml_TracedPackageImport,
)
umlTrace_uml_TracedProfileApplication_strategy = st.builds(
    umlTrace_uml_TracedProfileApplication,
)
umlTrace_uml_TracedTemplateBinding_strategy = st.builds(
    umlTrace_uml_TracedTemplateBinding,
)
umlTrace_uml_TracedProtocolConformance_strategy = st.builds(
    umlTrace_uml_TracedProtocolConformance,
)
umlTrace_uml_TracedGeneralization_strategy = st.builds(
    umlTrace_uml_TracedGeneralization,
)
umlTrace_uml_TracedPackageMerge_strategy = st.builds(
    umlTrace_uml_TracedPackageMerge,
)
umlTrace_uml_TracedElementImport_strategy = st.builds(
    umlTrace_uml_TracedElementImport,
)
uml_umlTrace_StartObjectBehaviorAction_strategy = st.builds(
    uml_umlTrace_StartObjectBehaviorAction,
)
TracedCallAction_strategy = st.builds(
    TracedCallAction,
)
umlTrace_uml_TracedCallOperationAction_strategy = st.builds(
    umlTrace_uml_TracedCallOperationAction,
)
umlTrace_uml_TracedCallBehaviorAction_strategy = st.builds(
    umlTrace_uml_TracedCallBehaviorAction,
)
umlTrace_uml_TracedStartObjectBehaviorAction_strategy = st.builds(
    umlTrace_uml_TracedStartObjectBehaviorAction,
)
uml_umlTrace_JoinNode_strategy = st.builds(
    uml_umlTrace_JoinNode,
)
TracedControlNode_strategy = st.builds(
    TracedControlNode,
)
umlTrace_uml_TracedForkNode_strategy = st.builds(
    umlTrace_uml_TracedForkNode,
)
umlTrace_uml_TracedDecisionNode_strategy = st.builds(
    umlTrace_uml_TracedDecisionNode,
)
umlTrace_uml_TracedFinalNode_strategy = st.builds(
    umlTrace_uml_TracedFinalNode,
)
umlTrace_uml_TracedMergeNode_strategy = st.builds(
    umlTrace_uml_TracedMergeNode,
)
umlTrace_uml_TracedInitialNode_strategy = st.builds(
    umlTrace_uml_TracedInitialNode,
)
umlTrace_uml_TracedJoinNode_strategy = st.builds(
    umlTrace_uml_TracedJoinNode,
)
TracedEModelElement_strategy = st.builds(
    TracedEModelElement,
)
umlTrace_uml_TracedElement_strategy = st.builds(
    umlTrace_uml_TracedElement,
)
TracedStructuralFeatureAction_strategy = st.builds(
    TracedStructuralFeatureAction,
)
umlTrace_uml_TracedClearStructuralFeatureAction_strategy = st.builds(
    umlTrace_uml_TracedClearStructuralFeatureAction,
)
umlTrace_uml_TracedReadStructuralFeatureAction_strategy = st.builds(
    umlTrace_uml_TracedReadStructuralFeatureAction,
)
umlTrace_uml_TracedWriteStructuralFeatureAction_strategy = st.builds(
    umlTrace_uml_TracedWriteStructuralFeatureAction,
)
umlTrace_uml_TracedSlot_strategy = st.builds(
    umlTrace_uml_TracedSlot,
)
umlTrace_uml_TracedComponentRealization_strategy = st.builds(
    umlTrace_uml_TracedComponentRealization,
)
umlTrace_uml_TracedReduceAction_strategy = st.builds(
    umlTrace_uml_TracedReduceAction,
)
uml_umlTrace_GeneralizationSet_strategy = st.builds(
    uml_umlTrace_GeneralizationSet,
)
TracedConstraint_strategy = st.builds(
    TracedConstraint,
)
umlTrace_uml_TracedIntervalConstraint_strategy = st.builds(
    umlTrace_uml_TracedIntervalConstraint,
)
umlTrace_uml_TracedInteractionConstraint_strategy = st.builds(
    umlTrace_uml_TracedInteractionConstraint,
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
uml_TracedExecutableNode_strategy = st.builds(
    uml_TracedExecutableNode,
)
TracedStructuredActivityNode_strategy = st.builds(
    TracedStructuredActivityNode,
)
umlTrace_uml_TracedExpansionRegion_strategy = st.builds(
    umlTrace_uml_TracedExpansionRegion,
)
umlTrace_uml_TracedConditionalNode_strategy = st.builds(
    umlTrace_uml_TracedConditionalNode,
)
umlTrace_uml_TracedLoopNode_strategy = st.builds(
    umlTrace_uml_TracedLoopNode,
)
umlTrace_uml_TracedSequenceNode_strategy = st.builds(
    umlTrace_uml_TracedSequenceNode,
)
uml_umlTrace_InputPin_strategy = st.builds(
    uml_umlTrace_InputPin,
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
uml_umlTrace_ReduceAction_strategy = st.builds(
    uml_umlTrace_ReduceAction,
)
umlTrace_uml_TracedStructuralFeatureAction_strategy = st.builds(
    umlTrace_uml_TracedStructuralFeatureAction,
)
umlTrace_uml_TracedBehavioredClassifier_strategy = st.builds(
    umlTrace_uml_TracedBehavioredClassifier,
)
uml_umlTrace_Package_strategy = st.builds(
    uml_umlTrace_Package,
)
umlTrace_uml_TracedLiteralSpecification_strategy = st.builds(
    umlTrace_uml_TracedLiteralSpecification,
)
umlTrace_uml_TracedMultiplicityElement_strategy = st.builds(
    umlTrace_uml_TracedMultiplicityElement,
)
uml_umlTrace_Constraint_strategy = st.builds(
    uml_umlTrace_Constraint,
)
uml_TracedPackageableElement_strategy = st.builds(
    uml_TracedPackageableElement,
)
umlTrace_uml_TracedValueSpecification_strategy = st.builds(
    umlTrace_uml_TracedValueSpecification,
)
umlTrace_uml_TracedInstanceSpecification_strategy = st.builds(
    umlTrace_uml_TracedInstanceSpecification,
)
umlTrace_uml_TracedInformationFlow_strategy = st.builds(
    umlTrace_uml_TracedInformationFlow,
)
umlTrace_uml_TracedDependency_strategy = st.builds(
    umlTrace_uml_TracedDependency,
)
umlTrace_uml_TracedPackage_strategy = st.builds(
    umlTrace_uml_TracedPackage,
)
TracedTransition_strategy = st.builds(
    TracedTransition,
)
umlTrace_uml_TracedProtocolTransition_strategy = st.builds(
    umlTrace_uml_TracedProtocolTransition,
)
umlTrace_uml_TracedExtension_strategy = st.builds(
    umlTrace_uml_TracedExtension,
)
TracedPackageableElement_strategy = st.builds(
    TracedPackageableElement,
)
umlTrace_uml_TracedObservation_strategy = st.builds(
    umlTrace_uml_TracedObservation,
)
umlTrace_uml_TracedGeneralizationSet_strategy = st.builds(
    umlTrace_uml_TracedGeneralizationSet,
)
umlTrace_uml_TracedEvent_strategy = st.builds(
    umlTrace_uml_TracedEvent,
)
umlTrace_uml_TracedConstraint_strategy = st.builds(
    umlTrace_uml_TracedConstraint,
)
umlTrace_uml_TracedType_strategy = st.builds(
    umlTrace_uml_TracedType,
)
uml_TracedParameterableElement_strategy = st.builds(
    uml_TracedParameterableElement,
)
umlTrace_uml_TracedConnectableElement_strategy = st.builds(
    umlTrace_uml_TracedConnectableElement,
)
umlTrace_uml_TracedOperation_strategy = st.builds(
    umlTrace_uml_TracedOperation,
)
umlTrace_uml_TracedPackageableElement_strategy = st.builds(
    umlTrace_uml_TracedPackageableElement,
)
uml_umlTrace_TimeEvent_strategy = st.builds(
    uml_umlTrace_TimeEvent,
)
TracedEvent_strategy = st.builds(
    TracedEvent,
)
umlTrace_uml_TracedMessageEvent_strategy = st.builds(
    umlTrace_uml_TracedMessageEvent,
)
umlTrace_uml_TracedChangeEvent_strategy = st.builds(
    umlTrace_uml_TracedChangeEvent,
)
umlTrace_uml_TracedTimeEvent_strategy = st.builds(
    umlTrace_uml_TracedTimeEvent,
)
TracedRelationship_strategy = st.builds(
    TracedRelationship,
)
umlTrace_uml_TracedDirectedRelationship_strategy = st.builds(
    umlTrace_uml_TracedDirectedRelationship,
)
TracedDependency_strategy = st.builds(
    TracedDependency,
)
umlTrace_uml_TracedAbstraction_strategy = st.builds(
    umlTrace_uml_TracedAbstraction,
)
umlTrace_uml_TracedUsage_strategy = st.builds(
    umlTrace_uml_TracedUsage,
)
umlTrace_uml_TracedDeployment_strategy = st.builds(
    umlTrace_uml_TracedDeployment,
)
uml_umlTrace_BroadcastSignalAction_strategy = st.builds(
    uml_umlTrace_BroadcastSignalAction,
)
umlTrace_uml_TracedBroadcastSignalAction_strategy = st.builds(
    umlTrace_uml_TracedBroadcastSignalAction,
)
uml_umlTrace_TemplateSignature_strategy = st.builds(
    uml_umlTrace_TemplateSignature,
)
TracedExecutableNode_strategy = st.builds(
    TracedExecutableNode,
)
umlTrace_uml_TracedAction_strategy = st.builds(
    umlTrace_uml_TracedAction,
)
uml_TracedLinkEndDestructionData_strategy = st.builds(
    uml_TracedLinkEndDestructionData,
)
uml_TracedClassifierTemplateParameter_strategy = st.builds(
    uml_TracedClassifierTemplateParameter,
)
IntermediateActions_TracedAddStructuralFeatureValueActionActivation_strategy = st.builds(
    IntermediateActions_TracedAddStructuralFeatureValueActionActivation,
)
BasicActions_TracedCallBehaviorActionActivation_strategy = st.builds(
    BasicActions_TracedCallBehaviorActionActivation,
)
uml_TracedProtocolConformance_strategy = st.builds(
    uml_TracedProtocolConformance,
)
uml_TracedLoopNode_strategy = st.builds(
    uml_TracedLoopNode,
)
uml_TracedExpansionRegion_strategy = st.builds(
    uml_TracedExpansionRegion,
)
uml_TracedActivityPartition_strategy = st.builds(
    uml_TracedActivityPartition,
)
uml_TracedCollaborationUse_strategy = st.builds(
    uml_TracedCollaborationUse,
)
uml_TracedEnumeration_strategy = st.builds(
    uml_TracedEnumeration,
)
uml_TracedLifeline_strategy = st.builds(
    uml_TracedLifeline,
)
uml_TracedSendObjectAction_strategy = st.builds(
    uml_TracedSendObjectAction,
)
uml_TracedConnectableElementTemplateParameter_strategy = st.builds(
    uml_TracedConnectableElementTemplateParameter,
)
uml_TracedCallEvent_strategy = st.builds(
    uml_TracedCallEvent,
)
uml_TracedStartClassifierBehaviorAction_strategy = st.builds(
    uml_TracedStartClassifierBehaviorAction,
)
uml_TracedRealization_strategy = st.builds(
    uml_TracedRealization,
)
uml_TracedCreateLinkObjectAction_strategy = st.builds(
    uml_TracedCreateLinkObjectAction,
)
IntermediateActivities_TracedControlToken_strategy = st.builds(
    IntermediateActivities_TracedControlToken,
)
uml_TracedTimeObservation_strategy = st.builds(
    uml_TracedTimeObservation,
)
uml_TracedExtensionEnd_strategy = st.builds(
    uml_TracedExtensionEnd,
)
uml_TracedComponent_strategy = st.builds(
    uml_TracedComponent,
)
uml_TracedAnyReceiveEvent_strategy = st.builds(
    uml_TracedAnyReceiveEvent,
)
uml_TracedReadLinkObjectEndAction_strategy = st.builds(
    uml_TracedReadLinkObjectEndAction,
)
uml_TracedConditionalNode_strategy = st.builds(
    uml_TracedConditionalNode,
)
uml_TracedInterface_strategy = st.builds(
    uml_TracedInterface,
)
uml_TracedStereotype_strategy = st.builds(
    uml_TracedStereotype,
)
uml_TracedLiteralString_strategy = st.builds(
    uml_TracedLiteralString,
)
uml_TracedInteraction_strategy = st.builds(
    uml_TracedInteraction,
)
IntermediateActivities_TracedMergeNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedMergeNodeActivation,
)
uml_TracedStateMachine_strategy = st.builds(
    uml_TracedStateMachine,
)
uml_TracedOccurrenceSpecification_strategy = st.builds(
    uml_TracedOccurrenceSpecification,
)
umlTrace_uml_TracedMessageOccurrenceSpecification_strategy = st.builds(
    umlTrace_uml_TracedMessageOccurrenceSpecification,
)
uml_TracedExecutionEnvironment_strategy = st.builds(
    uml_TracedExecutionEnvironment,
)
umlTrace_Loci_TracedLocus_strategy = st.builds(
    umlTrace_Loci_TracedLocus,
)
umlTrace_Loci_TracedExecutionFactory_strategy = st.builds(
    umlTrace_Loci_TracedExecutionFactory,
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
TracedActionActivation_strategy = st.builds(
    TracedActionActivation,
)
umlTrace_IntermediateActions_TracedCreateObjectActionActivation_strategy = st.builds(
    umlTrace_IntermediateActions_TracedCreateObjectActionActivation,
)
umlTrace_BasicActions_TracedInvocationActionActivation_strategy = st.builds(
    umlTrace_BasicActions_TracedInvocationActionActivation,
)
umlTrace_BasicActions_TracedOpaqueActionActivation_strategy = st.builds(
    umlTrace_BasicActions_TracedOpaqueActionActivation,
)
umlTrace_IntermediateActions_TracedValueSpecificationActionActivation_strategy = st.builds(
    umlTrace_IntermediateActions_TracedValueSpecificationActionActivation,
)
umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation_strategy = st.builds(
    umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation,
)
umlTrace_Loci_TracedExecutionEnvironment_strategy = st.builds(
    umlTrace_Loci_TracedExecutionEnvironment,
)
umlTrace_Loci_TracedExecutor_strategy = st.builds(
    umlTrace_Loci_TracedExecutor,
)
umlTrace_Loci_TracedSemanticVisitor_strategy = st.builds(
    umlTrace_Loci_TracedSemanticVisitor,
)
umlTrace_IntermediateActivities_TracedActivityEdgeInstance_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedActivityEdgeInstance,
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
umlTrace_IntermediateActivities_TracedOffer_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedOffer,
)
umlTrace_IntermediateActivities_TracedToken_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedToken,
)
umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup,
)
TracedActivityNodeActivation_strategy = st.builds(
    TracedActivityNodeActivation,
)
umlTrace_IntermediateActivities_TracedControlNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedControlNodeActivation,
)
umlTrace_BasicActions_TracedActionActivation_strategy = st.builds(
    umlTrace_BasicActions_TracedActionActivation,
)
umlTrace_IntermediateActivities_TracedObjectNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedObjectNodeActivation,
)
TracedControlNodeActivation_strategy = st.builds(
    TracedControlNodeActivation,
)
umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation,
)
umlTrace_IntermediateActivities_TracedForkNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedForkNodeActivation,
)
umlTrace_IntermediateActivities_TracedInitialNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedInitialNodeActivation,
)
umlTrace_IntermediateActivities_TracedJoinNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedJoinNodeActivation,
)
TracedToken_strategy = st.builds(
    TracedToken,
)
umlTrace_IntermediateActivities_TracedForkedToken_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedForkedToken,
)
umlTrace_IntermediateActivities_TracedDecisionNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedDecisionNodeActivation,
)
umlTrace_IntermediateActivities_TracedObjectToken_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedObjectToken,
)
umlTrace_IntermediateActivities_TracedControlToken_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedControlToken,
)
umlTrace_IntermediateActivities_TracedMergeNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedMergeNodeActivation,
)
TracedCompoundValue_strategy = st.builds(
    TracedCompoundValue,
)
umlTrace_Kernel_TracedExtensionalValue_strategy = st.builds(
    umlTrace_Kernel_TracedExtensionalValue,
)
umlTrace_Kernel_TracedFeatureValue_strategy = st.builds(
    umlTrace_Kernel_TracedFeatureValue,
)
TracedObject_strategy = st.builds(
    TracedObject,
)
umlTrace_BasicBehaviors_TracedExecution_strategy = st.builds(
    umlTrace_BasicBehaviors_TracedExecution,
)
umlTrace_BasicBehaviors_TracedParameterValue_strategy = st.builds(
    umlTrace_BasicBehaviors_TracedParameterValue,
)
TracedExecution_strategy = st.builds(
    TracedExecution,
)
umlTrace_IntermediateActivities_TracedActivityExecution_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedActivityExecution,
)
umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution_strategy = st.builds(
    umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution,
)
TracedValue_strategy = st.builds(
    TracedValue,
)
umlTrace_Kernel_TracedPrimitiveValue_strategy = st.builds(
    umlTrace_Kernel_TracedPrimitiveValue,
)
TracedSemanticVisitor_strategy = st.builds(
    TracedSemanticVisitor,
)
umlTrace_IntermediateActivities_TracedActivityNodeActivation_strategy = st.builds(
    umlTrace_IntermediateActivities_TracedActivityNodeActivation,
)
umlTrace_Kernel_TracedValue_strategy = st.builds(
    umlTrace_Kernel_TracedValue,
)
TracedEvaluation_strategy = st.builds(
    TracedEvaluation,
)
umlTrace_Kernel_TracedLiteralEvaluation_strategy = st.builds(
    umlTrace_Kernel_TracedLiteralEvaluation,
)
TracedPrimitiveValue_strategy = st.builds(
    TracedPrimitiveValue,
)
umlTrace_Kernel_TracedIntegerValue_strategy = st.builds(
    umlTrace_Kernel_TracedIntegerValue,
)
TracedStructuredValue_strategy = st.builds(
    TracedStructuredValue,
)
umlTrace_Kernel_TracedCompoundValue_strategy = st.builds(
    umlTrace_Kernel_TracedCompoundValue,
)
umlTrace_Kernel_TracedReference_strategy = st.builds(
    umlTrace_Kernel_TracedReference,
)
umlTrace_Kernel_TracedStructuredValue_strategy = st.builds(
    umlTrace_Kernel_TracedStructuredValue,
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
umlTrace_Kernel_TracedBooleanValue_strategy = st.builds(
    umlTrace_Kernel_TracedBooleanValue,
)
umlTrace_Kernel_TracedEvaluation_strategy = st.builds(
    umlTrace_Kernel_TracedEvaluation,
)
uml_TracedBehaviorExecutionSpecification_strategy = st.builds(
    uml_TracedBehaviorExecutionSpecification,
)
uml_TracedActor_strategy = st.builds(
    uml_TracedActor,
)
uml_TracedDeploymentSpecification_strategy = st.builds(
    uml_TracedDeploymentSpecification,
)
TracedExtensionalValue_strategy = st.builds(
    TracedExtensionalValue,
)
umlTrace_Kernel_TracedObject_strategy = st.builds(
    umlTrace_Kernel_TracedObject,
)
uml_TracedCentralBufferNode_strategy = st.builds(
    uml_TracedCentralBufferNode,
)
uml_TracedUnmarshallAction_strategy = st.builds(
    uml_TracedUnmarshallAction,
)
Kernel_TracedLiteralIntegerEvaluation_strategy = st.builds(
    Kernel_TracedLiteralIntegerEvaluation,
)
uml_TracedClearStructuralFeatureAction_strategy = st.builds(
    uml_TracedClearStructuralFeatureAction,
)
uml_TracedFunctionBehavior_strategy = st.builds(
    uml_TracedFunctionBehavior,
)
uml_TracedOpaqueExpression_strategy = st.builds(
    uml_TracedOpaqueExpression,
)
uml_TracedTemplateBinding_strategy = st.builds(
    uml_TracedTemplateBinding,
)
uml_TracedLinkEndCreationData_strategy = st.builds(
    uml_TracedLinkEndCreationData,
)
uml_TracedActionExecutionSpecification_strategy = st.builds(
    uml_TracedActionExecutionSpecification,
)
uml_TracedConnectionPointReference_strategy = st.builds(
    uml_TracedConnectionPointReference,
)
uml_TracedActivity_strategy = st.builds(
    uml_TracedActivity,
)
uml_TracedAcceptCallAction_strategy = st.builds(
    uml_TracedAcceptCallAction,
)
uml_TracedReadSelfAction_strategy = st.builds(
    uml_TracedReadSelfAction,
)
uml_TracedGate_strategy = st.builds(
    uml_TracedGate,
)
uml_TracedSubstitution_strategy = st.builds(
    uml_TracedSubstitution,
)
uml_TracedDevice_strategy = st.builds(
    uml_TracedDevice,
)
uml_TracedReclassifyObjectAction_strategy = st.builds(
    uml_TracedReclassifyObjectAction,
)
uml_TracedCallBehaviorAction_strategy = st.builds(
    uml_TracedCallBehaviorAction,
)
uml_TracedGeneralOrdering_strategy = st.builds(
    uml_TracedGeneralOrdering,
)
uml_TracedStateInvariant_strategy = st.builds(
    uml_TracedStateInvariant,
)
uml_TracedAssociation_strategy = st.builds(
    uml_TracedAssociation,
)
uml_TracedInteractionUse_strategy = st.builds(
    uml_TracedInteractionUse,
)
uml_TracedVariable_strategy = st.builds(
    uml_TracedVariable,
)
uml_TracedRemoveVariableValueAction_strategy = st.builds(
    uml_TracedRemoveVariableValueAction,
)
uml_TracedLiteralReal_strategy = st.builds(
    uml_TracedLiteralReal,
)
uml_TracedExecutionOccurrenceSpecification_strategy = st.builds(
    uml_TracedExecutionOccurrenceSpecification,
)
uml_TracedPackageImport_strategy = st.builds(
    uml_TracedPackageImport,
)
uml_TracedExceptionHandler_strategy = st.builds(
    uml_TracedExceptionHandler,
)
uml_TracedTestIdentityAction_strategy = st.builds(
    uml_TracedTestIdentityAction,
)
uml_TracedClearAssociationAction_strategy = st.builds(
    uml_TracedClearAssociationAction,
)
uml_TracedAddVariableValueAction_strategy = st.builds(
    uml_TracedAddVariableValueAction,
)
uml_TracedOperation_strategy = st.builds(
    uml_TracedOperation,
)
uml_TracedControlFlow_strategy = st.builds(
    uml_TracedControlFlow,
)
uml_TracedExpansionNode_strategy = st.builds(
    uml_TracedExpansionNode,
)
uml_TracedLiteralNull_strategy = st.builds(
    uml_TracedLiteralNull,
)
uml_TracedComment_strategy = st.builds(
    uml_TracedComment,
)
uml_TracedSignal_strategy = st.builds(
    uml_TracedSignal,
)
uml_TracedRaiseExceptionAction_strategy = st.builds(
    uml_TracedRaiseExceptionAction,
)
uml_TracedReception_strategy = st.builds(
    uml_TracedReception,
)
uml_TracedForkNode_strategy = st.builds(
    uml_TracedForkNode,
)
uml_TracedModel_strategy = st.builds(
    uml_TracedModel,
)
uml_TracedPackageMerge_strategy = st.builds(
    uml_TracedPackageMerge,
)
uml_TracedNode_strategy = st.builds(
    uml_TracedNode,
)
uml_TracedDestroyObjectAction_strategy = st.builds(
    uml_TracedDestroyObjectAction,
)
uml_TracedChangeEvent_strategy = st.builds(
    uml_TracedChangeEvent,
)
uml_TracedObjectFlow_strategy = st.builds(
    uml_TracedObjectFlow,
)
BasicActions_TracedInputPinActivation_strategy = st.builds(
    BasicActions_TracedInputPinActivation,
)
uml_TracedReadExtentAction_strategy = st.builds(
    uml_TracedReadExtentAction,
)
uml_TracedManifestation_strategy = st.builds(
    uml_TracedManifestation,
)
uml_TracedLinkEndData_strategy = st.builds(
    uml_TracedLinkEndData,
)
uml_TracedTransition_strategy = st.builds(
    uml_TracedTransition,
)
uml_TracedInstanceValue_strategy = st.builds(
    uml_TracedInstanceValue,
)
uml_TracedClause_strategy = st.builds(
    uml_TracedClause,
)
uml_TracedCombinedFragment_strategy = st.builds(
    uml_TracedCombinedFragment,
)
IntermediateActions_TracedCreateObjectActionActivation_strategy = st.builds(
    IntermediateActions_TracedCreateObjectActionActivation,
)
uml_TracedReplyAction_strategy = st.builds(
    uml_TracedReplyAction,
)
uml_TracedTimeExpression_strategy = st.builds(
    uml_TracedTimeExpression,
)
uml_TracedDependency_strategy = st.builds(
    uml_TracedDependency,
)
uml_TracedInformationFlow_strategy = st.builds(
    uml_TracedInformationFlow,
)
uml_TracedInteractionOperand_strategy = st.builds(
    uml_TracedInteractionOperand,
)
IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_strategy = st.builds(
    IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution,
)
uml_TracedFinalState_strategy = st.builds(
    uml_TracedFinalState,
)
uml_TracedUseCase_strategy = st.builds(
    uml_TracedUseCase,
)
uml_TracedPseudostate_strategy = st.builds(
    uml_TracedPseudostate,
)
uml_TracedRegion_strategy = st.builds(
    uml_TracedRegion,
)
uml_TracedValueSpecificationAction_strategy = st.builds(
    uml_TracedValueSpecificationAction,
)
uml_TracedDecisionNode_strategy = st.builds(
    uml_TracedDecisionNode,
)
IntermediateActivities_TracedActivityParameterNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedActivityParameterNodeActivation,
)
uml_TracedDestroyLinkAction_strategy = st.builds(
    uml_TracedDestroyLinkAction,
)
uml_TracedInterruptibleActivityRegion_strategy = st.builds(
    uml_TracedInterruptibleActivityRegion,
)
uml_TracedReadIsClassifiedObjectAction_strategy = st.builds(
    uml_TracedReadIsClassifiedObjectAction,
)
IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_strategy = st.builds(
    IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution,
)
uml_TracedValuePin_strategy = st.builds(
    uml_TracedValuePin,
)
uml_TracedInstanceSpecification_strategy = st.builds(
    uml_TracedInstanceSpecification,
)
uml_TracedOutputPin_strategy = st.builds(
    uml_TracedOutputPin,
)
uml_TracedProtocolStateMachine_strategy = st.builds(
    uml_TracedProtocolStateMachine,
)
IntermediateActivities_TracedForkNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedForkNodeActivation,
)
uml_TracedInterval_strategy = st.builds(
    uml_TracedInterval,
)
uml_TracedProfile_strategy = st.builds(
    uml_TracedProfile,
)
uml_TracedCallOperationAction_strategy = st.builds(
    uml_TracedCallOperationAction,
)
uml_TracedTrigger_strategy = st.builds(
    uml_TracedTrigger,
)
uml_TracedIntervalConstraint_strategy = st.builds(
    uml_TracedIntervalConstraint,
)
uml_TracedImage_strategy = st.builds(
    uml_TracedImage,
)
uml_TracedDurationConstraint_strategy = st.builds(
    uml_TracedDurationConstraint,
)
uml_TracedMessageOccurrenceSpecification_strategy = st.builds(
    uml_TracedMessageOccurrenceSpecification,
)
uml_TracedConnectorEnd_strategy = st.builds(
    uml_TracedConnectorEnd,
)
uml_TracedTemplateParameter_strategy = st.builds(
    uml_TracedTemplateParameter,
)
uml_TracedActionInputPin_strategy = st.builds(
    uml_TracedActionInputPin,
)
uml_TracedClearVariableAction_strategy = st.builds(
    uml_TracedClearVariableAction,
)
uml_TracedLiteralInteger_strategy = st.builds(
    uml_TracedLiteralInteger,
)
uml_TracedInitialNode_strategy = st.builds(
    uml_TracedInitialNode,
)
uml_TracedProfileApplication_strategy = st.builds(
    uml_TracedProfileApplication,
)
IntermediateActivities_TracedDecisionNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedDecisionNodeActivation,
)
uml_TracedReadVariableAction_strategy = st.builds(
    uml_TracedReadVariableAction,
)
uml_TracedExtend_strategy = st.builds(
    uml_TracedExtend,
)
uml_TracedTemplateParameterSubstitution_strategy = st.builds(
    uml_TracedTemplateParameterSubstitution,
)
uml_TracedReadLinkObjectEndQualifierAction_strategy = st.builds(
    uml_TracedReadLinkObjectEndQualifierAction,
)
uml_TracedOperationTemplateParameter_strategy = st.builds(
    uml_TracedOperationTemplateParameter,
)
uml_TracedQualifierValue_strategy = st.builds(
    uml_TracedQualifierValue,
)
uml_TracedLiteralBoolean_strategy = st.builds(
    uml_TracedLiteralBoolean,
)
uml_TracedMessage_strategy = st.builds(
    uml_TracedMessage,
)
uml_TracedRedefinableTemplateSignature_strategy = st.builds(
    uml_TracedRedefinableTemplateSignature,
)
uml_TracedMergeNode_strategy = st.builds(
    uml_TracedMergeNode,
)
uml_TracedReadStructuralFeatureAction_strategy = st.builds(
    uml_TracedReadStructuralFeatureAction,
)
Kernel_TracedLiteralBooleanEvaluation_strategy = st.builds(
    Kernel_TracedLiteralBooleanEvaluation,
)
BasicActions_TracedOpaqueActionActivation_strategy = st.builds(
    BasicActions_TracedOpaqueActionActivation,
)
uml_TracedPartDecomposition_strategy = st.builds(
    uml_TracedPartDecomposition,
)
uml_TracedGeneralization_strategy = st.builds(
    uml_TracedGeneralization,
)
uml_TracedCreateLinkAction_strategy = st.builds(
    uml_TracedCreateLinkAction,
)
uml_TracedUsage_strategy = st.builds(
    uml_TracedUsage,
)
uml_TracedDuration_strategy = st.builds(
    uml_TracedDuration,
)
uml_TracedParameterSet_strategy = st.builds(
    uml_TracedParameterSet,
)
IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_strategy = st.builds(
    IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution,
)
uml_TracedActivityParameterNode_strategy = st.builds(
    uml_TracedActivityParameterNode,
)
uml_TracedAbstraction_strategy = st.builds(
    uml_TracedAbstraction,
)
uml_TracedStructuredActivityNode_strategy = st.builds(
    uml_TracedStructuredActivityNode,
)
uml_TracedLiteralUnlimitedNatural_strategy = st.builds(
    uml_TracedLiteralUnlimitedNatural,
)
uml_TracedState_strategy = st.builds(
    uml_TracedState,
)
uml_TracedDestructionOccurrenceSpecification_strategy = st.builds(
    uml_TracedDestructionOccurrenceSpecification,
)
uml_TracedInclude_strategy = st.builds(
    uml_TracedInclude,
)
uml_TracedDurationInterval_strategy = st.builds(
    uml_TracedDurationInterval,
)
uml_TracedCreateObjectAction_strategy = st.builds(
    uml_TracedCreateObjectAction,
)
uml_TracedElementImport_strategy = st.builds(
    uml_TracedElementImport,
)
uml_TracedStartObjectBehaviorAction_strategy = st.builds(
    uml_TracedStartObjectBehaviorAction,
)
BasicActions_TracedOutputPinActivation_strategy = st.builds(
    BasicActions_TracedOutputPinActivation,
)
IntermediateActions_TracedReadStructuralFeatureActionActivation_strategy = st.builds(
    IntermediateActions_TracedReadStructuralFeatureActionActivation,
)
uml_TracedStringExpression_strategy = st.builds(
    uml_TracedStringExpression,
)
IntermediateActions_TracedValueSpecificationActionActivation_strategy = st.builds(
    IntermediateActions_TracedValueSpecificationActionActivation,
)
uml_TracedAssociationClass_strategy = st.builds(
    uml_TracedAssociationClass,
)
uml_TracedComponentRealization_strategy = st.builds(
    uml_TracedComponentRealization,
)
uml_TracedInteractionConstraint_strategy = st.builds(
    uml_TracedInteractionConstraint,
)
uml_TracedSequenceNode_strategy = st.builds(
    uml_TracedSequenceNode,
)
uml_TracedInputPin_strategy = st.builds(
    uml_TracedInputPin,
)
uml_TracedReduceAction_strategy = st.builds(
    uml_TracedReduceAction,
)
uml_TracedGeneralizationSet_strategy = st.builds(
    uml_TracedGeneralizationSet,
)
uml_TracedConstraint_strategy = st.builds(
    uml_TracedConstraint,
)
uml_TracedJoinNode_strategy = st.builds(
    uml_TracedJoinNode,
)
uml_TracedExtensionPoint_strategy = st.builds(
    uml_TracedExtensionPoint,
)
uml_TracedSignalEvent_strategy = st.builds(
    uml_TracedSignalEvent,
)
uml_TracedSlot_strategy = st.builds(
    uml_TracedSlot,
)
uml_TracedTimeEvent_strategy = st.builds(
    uml_TracedTimeEvent,
)
uml_TracedExtension_strategy = st.builds(
    uml_TracedExtension,
)
uml_TracedTimeInterval_strategy = st.builds(
    uml_TracedTimeInterval,
)
uml_TracedPort_strategy = st.builds(
    uml_TracedPort,
)
uml_TracedDeployment_strategy = st.builds(
    uml_TracedDeployment,
)
uml_TracedBroadcastSignalAction_strategy = st.builds(
    uml_TracedBroadcastSignalAction,
)
uml_TracedTemplateSignature_strategy = st.builds(
    uml_TracedTemplateSignature,
)
umlTrace_uml_TracedRedefinableTemplateSignature_strategy = st.builds(
    umlTrace_uml_TracedRedefinableTemplateSignature,
)
uml_TracedCollaboration_strategy = st.builds(
    uml_TracedCollaboration,
)
uml_TracedPackage_strategy = st.builds(
    uml_TracedPackage,
)
IntermediateActivities_TracedActivityFinalNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedActivityFinalNodeActivation,
)
uml_TracedProtocolTransition_strategy = st.builds(
    uml_TracedProtocolTransition,
)
uml_TracedReadLinkAction_strategy = st.builds(
    uml_TracedReadLinkAction,
)
uml_TracedAddStructuralFeatureValueAction_strategy = st.builds(
    uml_TracedAddStructuralFeatureValueAction,
)
ForkedToken_baseTokenIsWithdrawn_Value_strategy = st.builds(
    ForkedToken_baseTokenIsWithdrawn_Value,
)
ForkedToken_baseToken_Value_strategy = st.builds(
    ForkedToken_baseToken_Value,
)
ForkedToken_remainingOffersCount_Value_strategy = st.builds(
    ForkedToken_remainingOffersCount_Value,
)
IntegerValue_value_IntegerValue_Value_strategy = st.builds(
    IntegerValue_value_IntegerValue_Value,
)
Reference_referent_Value_strategy = st.builds(
    Reference_referent_Value,
)
Object_types_Value_strategy = st.builds(
    Object_types_Value,
)
BigStep_strategy = st.builds(
    BigStep,
)
SmallStep_strategy = st.builds(
    SmallStep,
)
SemanticVisitor_runtimeModelElement_Value_strategy = st.builds(
    SemanticVisitor_runtimeModelElement_Value,
)
ObjectNodeActivation_offeredTokenCount_Value_strategy = st.builds(
    ObjectNodeActivation_offeredTokenCount_Value,
)
Locus_executor_Value_strategy = st.builds(
    Locus_executor_Value,
)
Locus_extensionalValues_Value_strategy = st.builds(
    Locus_extensionalValues_Value,
)
Locus_factory_Value_strategy = st.builds(
    Locus_factory_Value,
)
TracedObjects_strategy = st.builds(
    TracedObjects,
)
Steps_strategy = st.builds(
    Steps,
)
umlTrace_State_strategy = st.builds(
    umlTrace_State,
)
umlTrace_Trace_strategy = st.builds(
    umlTrace_Trace,
)
uml_TracedEnumerationLiteral_strategy = st.builds(
    uml_TracedEnumerationLiteral,
)
uml_TracedAcceptEventAction_strategy = st.builds(
    uml_TracedAcceptEventAction,
)
IntermediateActivities_TracedInitialNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedInitialNodeActivation,
)
uml_TracedDurationObservation_strategy = st.builds(
    uml_TracedDurationObservation,
)
uml_TracedActivityFinalNode_strategy = st.builds(
    uml_TracedActivityFinalNode,
)
uml_TracedInterfaceRealization_strategy = st.builds(
    uml_TracedInterfaceRealization,
)
uml_TracedTimeConstraint_strategy = st.builds(
    uml_TracedTimeConstraint,
)
IntermediateActivities_TracedJoinNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedJoinNodeActivation,
)
uml_TracedInformationItem_strategy = st.builds(
    uml_TracedInformationItem,
)
uml_TracedFlowFinalNode_strategy = st.builds(
    uml_TracedFlowFinalNode,
)
uml_TracedDataStoreNode_strategy = st.builds(
    uml_TracedDataStoreNode,
)
uml_TracedConsiderIgnoreFragment_strategy = st.builds(
    uml_TracedConsiderIgnoreFragment,
)
uml_TracedExpression_strategy = st.builds(
    uml_TracedExpression,
)
umlTrace_uml_TracedStringExpression_strategy = st.builds(
    umlTrace_uml_TracedStringExpression,
)
uml_TracedSendSignalAction_strategy = st.builds(
    uml_TracedSendSignalAction,
)
uml_TracedRemoveStructuralFeatureValueAction_strategy = st.builds(
    uml_TracedRemoveStructuralFeatureValueAction,
)
uml_TracedContinuation_strategy = st.builds(
    uml_TracedContinuation,
)
uml_TracedProperty_strategy = st.builds(
    uml_TracedProperty,
)
uml_TracedCommunicationPath_strategy = st.builds(
    uml_TracedCommunicationPath,
)
uml_TracedDataType_strategy = st.builds(
    uml_TracedDataType,
)
uml_TracedOpaqueAction_strategy = st.builds(
    uml_TracedOpaqueAction,
)
uml_TracedConnector_strategy = st.builds(
    uml_TracedConnector,
)
umlTrace_Traced_TracedObjects_strategy = st.builds(
    umlTrace_Traced_TracedObjects,
)
uml_TracedArtifact_strategy = st.builds(
    uml_TracedArtifact,
)
uml_TracedOpaqueBehavior_strategy = st.builds(
    uml_TracedOpaqueBehavior,
)
umlTrace_Values_ActivityExecution_activationGroup_Value_strategy = st.builds(
    umlTrace_Values_ActivityExecution_activationGroup_Value,
)
umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value_strategy = st.builds(
    umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value,
)
umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value_strategy = st.builds(
    umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value,
)
Loci_TracedExecutionEnvironment_strategy = st.builds(
    Loci_TracedExecutionEnvironment,
)
umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value_strategy = st.builds(
    umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value,
)
umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value_strategy = st.builds(
    umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value,
)
umlTrace_Values_ActivityNodeActivation_isRunning_Value_strategy = st.builds(
    umlTrace_Values_ActivityNodeActivation_isRunning_Value,
    isRunning=
        st.booleans()
)
umlTrace_Values_ActivityNodeActivation_incomingEdges_Value_strategy = st.builds(
    umlTrace_Values_ActivityNodeActivation_incomingEdges_Value,
)
umlTrace_Values_ActivityNodeActivation_heldTokens_Value_strategy = st.builds(
    umlTrace_Values_ActivityNodeActivation_heldTokens_Value,
)
umlTrace_Values_InputParameterValues_parameterValues_Value_strategy = st.builds(
    umlTrace_Values_InputParameterValues_parameterValues_Value,
)
Input_TracedInputParameterValues_strategy = st.builds(
    Input_TracedInputParameterValues,
)
umlTrace_Values_InputParameterValues_name_Value_strategy = st.builds(
    umlTrace_Values_InputParameterValues_name_Value,
    name=
        safe_text
)
umlTrace_Values_ActivityNodeActivation_running_Value_strategy = st.builds(
    umlTrace_Values_ActivityNodeActivation_running_Value,
    running=
        st.booleans()
)
uml_TracedActivityNode_strategy = st.builds(
    uml_TracedActivityNode,
)
umlTrace_uml_TracedObjectNode_strategy = st.builds(
    umlTrace_uml_TracedObjectNode,
)
umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value_strategy = st.builds(
    umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value,
)
uml_TracedActivityEdge_strategy = st.builds(
    uml_TracedActivityEdge,
)
umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value_strategy = st.builds(
    umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value,
)
umlTrace_Values_ActivityEdgeInstance_target_Value_strategy = st.builds(
    umlTrace_Values_ActivityEdgeInstance_target_Value,
)
umlTrace_Values_ActivityEdgeInstance_source_Value_strategy = st.builds(
    umlTrace_Values_ActivityEdgeInstance_source_Value,
)
umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value_strategy = st.builds(
    umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value,
)
umlTrace_Values_PinActivation_count_temp_Value_strategy = st.builds(
    umlTrace_Values_PinActivation_count_temp_Value,
    count_temp=
        st.integers()
)
umlTrace_Values_ActivityEdgeInstance_offers_Value_strategy = st.builds(
    umlTrace_Values_ActivityEdgeInstance_offers_Value,
)
umlTrace_Values_FeatureValue_position_Value_strategy = st.builds(
    umlTrace_Values_FeatureValue_position_Value,
    position=
        st.integers()
)
uml_TracedStructuralFeature_strategy = st.builds(
    uml_TracedStructuralFeature,
)
umlTrace_uml_TracedProperty_strategy = st.builds(
    umlTrace_uml_TracedProperty,
)
umlTrace_Values_FeatureValue_feature_Value_strategy = st.builds(
    umlTrace_Values_FeatureValue_feature_Value,
)
umlTrace_Values_FeatureValue_values_FeatureValue_Value_strategy = st.builds(
    umlTrace_Values_FeatureValue_values_FeatureValue_Value,
)
umlTrace_Values_PinActivation_actionActivation_Value_strategy = st.builds(
    umlTrace_Values_PinActivation_actionActivation_Value,
)
umlTrace_Values_Token_holder_Value_strategy = st.builds(
    umlTrace_Values_Token_holder_Value,
)
Kernel_TracedCompoundValue_strategy = st.builds(
    Kernel_TracedCompoundValue,
)
Kernel_TracedFeatureValue_strategy = st.builds(
    Kernel_TracedFeatureValue,
)
umlTrace_Values_CompoundValue_featureValues_Value_strategy = st.builds(
    umlTrace_Values_CompoundValue_featureValues_Value,
)
BasicActions_TracedCallActionActivation_strategy = st.builds(
    BasicActions_TracedCallActionActivation,
)
umlTrace_Values_CallActionActivation_callExecutions_Value_strategy = st.builds(
    umlTrace_Values_CallActionActivation_callExecutions_Value,
)
IntermediateActivities_TracedOffer_strategy = st.builds(
    IntermediateActivities_TracedOffer,
)
umlTrace_Values_Offer_offeredTokens_Value_strategy = st.builds(
    umlTrace_Values_Offer_offeredTokens_Value,
)
Kernel_TracedBooleanValue_strategy = st.builds(
    Kernel_TracedBooleanValue,
)
umlTrace_Values_BooleanValue_value_BooleanValue_Value_strategy = st.builds(
    umlTrace_Values_BooleanValue_value_BooleanValue_Value,
    value_BooleanValue=
        st.booleans()
)
umlTrace_Values_Evaluation_locus_Evaluation_Value_strategy = st.builds(
    umlTrace_Values_Evaluation_locus_Evaluation_Value,
)
Kernel_TracedEvaluation_strategy = st.builds(
    Kernel_TracedEvaluation,
)
uml_TracedValueSpecification_strategy = st.builds(
    uml_TracedValueSpecification,
)
umlTrace_Values_Evaluation_specification_Evaluation_Value_strategy = st.builds(
    umlTrace_Values_Evaluation_specification_Evaluation_Value,
)
IntermediateActivities_TracedObjectToken_strategy = st.builds(
    IntermediateActivities_TracedObjectToken,
)
umlTrace_Values_ObjectToken_value_Value_strategy = st.builds(
    umlTrace_Values_ObjectToken_value_Value,
)
umlTrace_Values_Executor_locus_Executor_Value_strategy = st.builds(
    umlTrace_Values_Executor_locus_Executor_Value,
)
IntermediateActivities_TracedActivityEdgeInstance_strategy = st.builds(
    IntermediateActivities_TracedActivityEdgeInstance,
)
umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value_strategy = st.builds(
    umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value,
)
IntermediateActivities_TracedActivityExecution_strategy = st.builds(
    IntermediateActivities_TracedActivityExecution,
)
umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value_strategy = st.builds(
    umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value,
)
Kernel_TracedPrimitiveValue_strategy = st.builds(
    Kernel_TracedPrimitiveValue,
)
umlTrace_Values_PrimitiveValue_type_Value_strategy = st.builds(
    umlTrace_Values_PrimitiveValue_type_Value,
)
umlTrace_Values_Element_semanticVisitor_Value_strategy = st.builds(
    umlTrace_Values_Element_semanticVisitor_Value,
)
umlTrace_Values_Execution_context_Value_strategy = st.builds(
    umlTrace_Values_Execution_context_Value,
)
BasicBehaviors_TracedExecution_strategy = st.builds(
    BasicBehaviors_TracedExecution,
)
IntermediateActivities_TracedActivityNodeActivationGroup_strategy = st.builds(
    IntermediateActivities_TracedActivityNodeActivationGroup,
)
IntermediateActivities_TracedActivityNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedActivityNodeActivation,
)
umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value_strategy = st.builds(
    umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value,
)
BasicActions_TracedActionActivation_strategy = st.builds(
    BasicActions_TracedActionActivation,
)
BasicActions_TracedPinActivation_strategy = st.builds(
    BasicActions_TracedPinActivation,
)
umlTrace_Values_ActionActivation_pinActivations_Value_strategy = st.builds(
    umlTrace_Values_ActionActivation_pinActivations_Value,
)
uml_TracedParameter_strategy = st.builds(
    uml_TracedParameter,
)
umlTrace_Values_ParameterValue_parameter_ParameterValue_Value_strategy = st.builds(
    umlTrace_Values_ParameterValue_parameter_ParameterValue_Value,
)
BasicBehaviors_TracedParameterValue_strategy = st.builds(
    BasicBehaviors_TracedParameterValue,
)
Kernel_TracedValue_strategy = st.builds(
    Kernel_TracedValue,
)
umlTrace_Values_Execution_parameterValues_Value_strategy = st.builds(
    umlTrace_Values_Execution_parameterValues_Value,
)
umlTrace_Values_SemanticVisitor_runtimeModelElement_Value_strategy = st.builds(
    umlTrace_Values_SemanticVisitor_runtimeModelElement_Value,
)
umlTrace_Values_ActionActivation_firing_Value_strategy = st.builds(
    umlTrace_Values_ActionActivation_firing_Value,
    firing=
        st.booleans()
)
IntermediateActivities_TracedObjectNodeActivation_strategy = st.builds(
    IntermediateActivities_TracedObjectNodeActivation,
)
umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value_strategy = st.builds(
    umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value,
    offeredTokenCount=
        st.integers()
)
Loci_TracedExecutor_strategy = st.builds(
    Loci_TracedExecutor,
)
umlTrace_Values_Locus_executor_Value_strategy = st.builds(
    umlTrace_Values_Locus_executor_Value,
)
umlTrace_Values_ParameterValue_values_ParameterValue_Value_strategy = st.builds(
    umlTrace_Values_ParameterValue_values_ParameterValue_Value,
)
Loci_TracedSemanticVisitor_strategy = st.builds(
    Loci_TracedSemanticVisitor,
)
uml_TracedElement_strategy = st.builds(
    uml_TracedElement,
)
Loci_TracedLocus_strategy = st.builds(
    Loci_TracedLocus,
)
umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value_strategy = st.builds(
    umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value,
)
BasicBehaviors_TracedOpaqueBehaviorExecution_strategy = st.builds(
    BasicBehaviors_TracedOpaqueBehaviorExecution,
)
umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value_strategy = st.builds(
    umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value,
)
Loci_TracedExecutionFactory_strategy = st.builds(
    Loci_TracedExecutionFactory,
)
uml_TracedPrimitiveType_strategy = st.builds(
    uml_TracedPrimitiveType,
)
umlTrace_Values_ExecutionFactory_builtInTypes_Value_strategy = st.builds(
    umlTrace_Values_ExecutionFactory_builtInTypes_Value,
)
Kernel_TracedExtensionalValue_strategy = st.builds(
    Kernel_TracedExtensionalValue,
)
umlTrace_Values_Locus_extensionalValues_Value_strategy = st.builds(
    umlTrace_Values_Locus_extensionalValues_Value,
)
umlTrace_Values_Locus_factory_Value_strategy = st.builds(
    umlTrace_Values_Locus_factory_Value,
)
IntermediateActivities_TracedForkedToken_strategy = st.builds(
    IntermediateActivities_TracedForkedToken,
)
umlTrace_Values_ForkedToken_remainingOffersCount_Value_strategy = st.builds(
    umlTrace_Values_ForkedToken_remainingOffersCount_Value,
    remainingOffersCount=
        st.integers()
)
Kernel_TracedIntegerValue_strategy = st.builds(
    Kernel_TracedIntegerValue,
)
umlTrace_Values_IntegerValue_value_IntegerValue_Value_strategy = st.builds(
    umlTrace_Values_IntegerValue_value_IntegerValue_Value,
    value_IntegerValue=
        st.integers()
)
Kernel_TracedReference_strategy = st.builds(
    Kernel_TracedReference,
)
umlTrace_Values_Reference_referent_Value_strategy = st.builds(
    umlTrace_Values_Reference_referent_Value,
)
umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value_strategy = st.builds(
    umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value,
    baseTokenIsWithdrawn=
        st.booleans()
)
IntermediateActivities_TracedToken_strategy = st.builds(
    IntermediateActivities_TracedToken,
)
umlTrace_Values_ForkedToken_baseToken_Value_strategy = st.builds(
    umlTrace_Values_ForkedToken_baseToken_Value,
)
umlTrace_Steps_BigStep_strategy = st.builds(
    umlTrace_Steps_BigStep,
)
umlTrace_Steps_Steps_strategy = st.builds(
    umlTrace_Steps_Steps,
)
Steps_umlTrace_State_strategy = st.builds(
    Steps_umlTrace_State,
)
umlTrace_Steps_SmallStep_strategy = st.builds(
    umlTrace_Steps_SmallStep,
)
ExecutionEnvironment_locus_ExecutionEnvironment_Value_strategy = st.builds(
    ExecutionEnvironment_locus_ExecutionEnvironment_Value,
)
ActivityExecution_activationGroup_Value_strategy = st.builds(
    ActivityExecution_activationGroup_Value,
)
ExtensionalValue_locus_ExtensionalValue_Value_strategy = st.builds(
    ExtensionalValue_locus_ExtensionalValue_Value,
)
ActivityNodeActivation_group_ActivityNodeActivation_Value_strategy = st.builds(
    ActivityNodeActivation_group_ActivityNodeActivation_Value,
)
ActivityNodeActivation_incomingEdges_Value_strategy = st.builds(
    ActivityNodeActivation_incomingEdges_Value,
)
ActivityNodeActivation_outgoingEdges_Value_strategy = st.builds(
    ActivityNodeActivation_outgoingEdges_Value,
)
Values_umlTrace_State_strategy = st.builds(
    Values_umlTrace_State,
)
Kernel_TracedObject_strategy = st.builds(
    Kernel_TracedObject,
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
umlTrace_Values_Object_types_Value_strategy = st.builds(
    umlTrace_Values_Object_types_Value,
)
ActivityNodeActivation_heldTokens_Value_strategy = st.builds(
    ActivityNodeActivation_heldTokens_Value,
)
InputParameterValues_parameterValues_Value_strategy = st.builds(
    InputParameterValues_parameterValues_Value,
)
InputParameterValues_name_Value_strategy = st.builds(
    InputParameterValues_name_Value,
)
ActivityEdgeInstance_source_Value_strategy = st.builds(
    ActivityEdgeInstance_source_Value,
)
ActivityEdgeInstance_edge_ActivityEdgeInstance_Value_strategy = st.builds(
    ActivityEdgeInstance_edge_ActivityEdgeInstance_Value,
)
ActivityEdgeInstance_target_Value_strategy = st.builds(
    ActivityEdgeInstance_target_Value,
)
ActivityEdgeInstance_offers_Value_strategy = st.builds(
    ActivityEdgeInstance_offers_Value,
)
ActivityEdgeInstance_group_ActivityEdgeInstance_Value_strategy = st.builds(
    ActivityEdgeInstance_group_ActivityEdgeInstance_Value,
)
PinActivation_count_temp_Value_strategy = st.builds(
    PinActivation_count_temp_Value,
)
ActivityNodeActivation_isRunning_Value_strategy = st.builds(
    ActivityNodeActivation_isRunning_Value,
)
ActivityNodeActivation_running_Value_strategy = st.builds(
    ActivityNodeActivation_running_Value,
)
ActivityNodeActivation_node_ActivityNodeActivation_Value_strategy = st.builds(
    ActivityNodeActivation_node_ActivityNodeActivation_Value,
)
FeatureValue_values_FeatureValue_Value_strategy = st.builds(
    FeatureValue_values_FeatureValue_Value,
)
Offer_offeredTokens_Value_strategy = st.builds(
    Offer_offeredTokens_Value,
)
Token_holder_Value_strategy = st.builds(
    Token_holder_Value,
)
CompoundValue_featureValues_Value_strategy = st.builds(
    CompoundValue_featureValues_Value,
)
CallActionActivation_callExecutions_Value_strategy = st.builds(
    CallActionActivation_callExecutions_Value,
)
ObjectToken_value_Value_strategy = st.builds(
    ObjectToken_value_Value,
)
BooleanValue_value_BooleanValue_Value_strategy = st.builds(
    BooleanValue_value_BooleanValue_Value,
)
Evaluation_locus_Evaluation_Value_strategy = st.builds(
    Evaluation_locus_Evaluation_Value,
)
Evaluation_specification_Evaluation_Value_strategy = st.builds(
    Evaluation_specification_Evaluation_Value,
)
PinActivation_actionActivation_Value_strategy = st.builds(
    PinActivation_actionActivation_Value,
)
FeatureValue_position_Value_strategy = st.builds(
    FeatureValue_position_Value,
)
FeatureValue_feature_Value_strategy = st.builds(
    FeatureValue_feature_Value,
)
ActivityNodeActivationGroup_nodeActivations_Value_strategy = st.builds(
    ActivityNodeActivationGroup_nodeActivations_Value,
)
Element_semanticVisitor_Value_strategy = st.builds(
    Element_semanticVisitor_Value,
)
Execution_context_Value_strategy = st.builds(
    Execution_context_Value,
)
Execution_parameterValues_Value_strategy = st.builds(
    Execution_parameterValues_Value,
)
ActionActivation_firing_Value_strategy = st.builds(
    ActionActivation_firing_Value,
)
ActionActivation_pinActivations_Value_strategy = st.builds(
    ActionActivation_pinActivations_Value,
)
ParameterValue_parameter_ParameterValue_Value_strategy = st.builds(
    ParameterValue_parameter_ParameterValue_Value,
)
ParameterValue_values_ParameterValue_Value_strategy = st.builds(
    ParameterValue_values_ParameterValue_Value,
)
PrimitiveValue_type_Value_strategy = st.builds(
    PrimitiveValue_type_Value,
)
Executor_locus_Executor_Value_strategy = st.builds(
    Executor_locus_Executor_Value,
)
ActivityNodeActivationGroup_edgeInstances_Value_strategy = st.builds(
    ActivityNodeActivationGroup_edgeInstances_Value,
)
ActivityNodeActivationGroup_activityExecution_Value_strategy = st.builds(
    ActivityNodeActivationGroup_activityExecution_Value,
)
ExecutionFactory_locus_ExecutionFactory_Value_strategy = st.builds(
    ExecutionFactory_locus_ExecutionFactory_Value,
)
ExecutionFactory_primitiveBehaviorPrototypes_Value_strategy = st.builds(
    ExecutionFactory_primitiveBehaviorPrototypes_Value,
)
ExecutionFactory_builtInTypes_Value_strategy = st.builds(
    ExecutionFactory_builtInTypes_Value,
)

@given(instance=uml_umlTrace_ControlFlow_strategy)
@settings(max_examples=50)
def test_uml_umltrace_controlflow_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ControlFlow)

@given(instance=uml_umlTrace_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_testidentityaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_TestIdentityAction)

@given(instance=uml_umlTrace_AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_AddVariableValueAction)

@given(instance=TracedWriteVariableAction_strategy)
@settings(max_examples=50)
def test_tracedwritevariableaction_instantiation(instance):
    assert isinstance(instance, TracedWriteVariableAction)

@given(instance=umlTrace_uml_TracedAddVariableValueAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedaddvariablevalueaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAddVariableValueAction)

@given(instance=uml_TracedObjectNode_strategy)
@settings(max_examples=50)
def test_uml_tracedobjectnode_instantiation(instance):
    assert isinstance(instance, uml_TracedObjectNode)

@given(instance=uml_umlTrace_ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_clearassociationaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ClearAssociationAction)

@given(instance=TracedBehavioralFeature_strategy)
@settings(max_examples=50)
def test_tracedbehavioralfeature_instantiation(instance):
    assert isinstance(instance, TracedBehavioralFeature)

@given(instance=umlTrace_uml_TracedReception_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreception_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReception)

@given(instance=uml_umlTrace_ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml_umltrace_expansionnode_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ExpansionNode)

@given(instance=uml_umlTrace_LiteralNull_strategy)
@settings(max_examples=50)
def test_uml_umltrace_literalnull_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_LiteralNull)

@given(instance=uml_umlTrace_RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_RaiseExceptionAction)

@given(instance=uml_umlTrace_Reception_strategy)
@settings(max_examples=50)
def test_uml_umltrace_reception_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Reception)

@given(instance=uml_umlTrace_Signal_strategy)
@settings(max_examples=50)
def test_uml_umltrace_signal_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Signal)

@given(instance=uml_umlTrace_ForkNode_strategy)
@settings(max_examples=50)
def test_uml_umltrace_forknode_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ForkNode)

@given(instance=uml_umlTrace_DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_destroyobjectaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_DestroyObjectAction)

@given(instance=uml_umlTrace_Comment_strategy)
@settings(max_examples=50)
def test_uml_umltrace_comment_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Comment)

@given(instance=uml_umlTrace_ObjectFlow_strategy)
@settings(max_examples=50)
def test_uml_umltrace_objectflow_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ObjectFlow)

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

@given(instance=uml_umlTrace_PackageMerge_strategy)
@settings(max_examples=50)
def test_uml_umltrace_packagemerge_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_PackageMerge)

@given(instance=uml_umlTrace_ChangeEvent_strategy)
@settings(max_examples=50)
def test_uml_umltrace_changeevent_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ChangeEvent)

@given(instance=uml_umlTrace_Transition_strategy)
@settings(max_examples=50)
def test_uml_umltrace_transition_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Transition)

@given(instance=uml_umlTrace_LinkEndData_strategy)
@settings(max_examples=50)
def test_uml_umltrace_linkenddata_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_LinkEndData)

@given(instance=uml_umlTrace_TimeExpression_strategy)
@settings(max_examples=50)
def test_uml_umltrace_timeexpression_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_TimeExpression)

@given(instance=uml_umlTrace_Dependency_strategy)
@settings(max_examples=50)
def test_uml_umltrace_dependency_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Dependency)

@given(instance=uml_umlTrace_ReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_readextentaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ReadExtentAction)

@given(instance=uml_umlTrace_InstanceValue_strategy)
@settings(max_examples=50)
def test_uml_umltrace_instancevalue_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_InstanceValue)

@given(instance=uml_umlTrace_Clause_strategy)
@settings(max_examples=50)
def test_uml_umltrace_clause_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Clause)

@given(instance=uml_umlTrace_ReplyAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_replyaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ReplyAction)

@given(instance=uml_umlTrace_UseCase_strategy)
@settings(max_examples=50)
def test_uml_umltrace_usecase_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_UseCase)

@given(instance=uml_umlTrace_CombinedFragment_strategy)
@settings(max_examples=50)
def test_uml_umltrace_combinedfragment_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_CombinedFragment)

@given(instance=TracedVertex_strategy)
@settings(max_examples=50)
def test_tracedvertex_instantiation(instance):
    assert isinstance(instance, TracedVertex)

@given(instance=umlTrace_uml_TracedPseudostate_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpseudostate_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPseudostate)

@given(instance=uml_umlTrace_InformationFlow_strategy)
@settings(max_examples=50)
def test_uml_umltrace_informationflow_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_InformationFlow)

@given(instance=uml_TracedRelationship_strategy)
@settings(max_examples=50)
def test_uml_tracedrelationship_instantiation(instance):
    assert isinstance(instance, uml_TracedRelationship)

@given(instance=TracedBehavioredClassifier_strategy)
@settings(max_examples=50)
def test_tracedbehavioredclassifier_instantiation(instance):
    assert isinstance(instance, TracedBehavioredClassifier)

@given(instance=umlTrace_uml_TracedUseCase_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedusecase_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedUseCase)

@given(instance=TracedActivityNode_strategy)
@settings(max_examples=50)
def test_tracedactivitynode_instantiation(instance):
    assert isinstance(instance, TracedActivityNode)

@given(instance=umlTrace_uml_TracedControlNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedControlNode)

@given(instance=uml_umlTrace_Pseudostate_strategy)
@settings(max_examples=50)
def test_uml_umltrace_pseudostate_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Pseudostate)

@given(instance=uml_umlTrace_InteractionOperand_strategy)
@settings(max_examples=50)
def test_uml_umltrace_interactionoperand_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_InteractionOperand)

@given(instance=uml_umlTrace_Region_strategy)
@settings(max_examples=50)
def test_uml_umltrace_region_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Region)

@given(instance=TracedState_strategy)
@settings(max_examples=50)
def test_tracedstate_instantiation(instance):
    assert isinstance(instance, TracedState)

@given(instance=umlTrace_uml_TracedFinalState_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedfinalstate_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedFinalState)

@given(instance=uml_umlTrace_DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_destroylinkaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_DestroyLinkAction)

@given(instance=uml_umlTrace_InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_uml_umltrace_interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_InterruptibleActivityRegion)

@given(instance=uml_umlTrace_DecisionNode_strategy)
@settings(max_examples=50)
def test_uml_umltrace_decisionnode_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_DecisionNode)

@given(instance=uml_umlTrace_ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_valuespecificationaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ValueSpecificationAction)

@given(instance=uml_umlTrace_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml_umltrace_instancespecification_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_InstanceSpecification)

@given(instance=uml_umlTrace_OutputPin_strategy)
@settings(max_examples=50)
def test_uml_umltrace_outputpin_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_OutputPin)

@given(instance=TracedStateMachine_strategy)
@settings(max_examples=50)
def test_tracedstatemachine_instantiation(instance):
    assert isinstance(instance, TracedStateMachine)

@given(instance=umlTrace_uml_TracedProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedprotocolstatemachine_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedProtocolStateMachine)

@given(instance=uml_umlTrace_ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ReadIsClassifiedObjectAction)

@given(instance=TracedPackage_strategy)
@settings(max_examples=50)
def test_tracedpackage_instantiation(instance):
    assert isinstance(instance, TracedPackage)

@given(instance=umlTrace_uml_TracedModel_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmodel_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedModel)

@given(instance=umlTrace_uml_TracedProfile_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedprofile_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedProfile)

@given(instance=uml_umlTrace_CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_calloperationaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_CallOperationAction)

@given(instance=uml_umlTrace_Trigger_strategy)
@settings(max_examples=50)
def test_uml_umltrace_trigger_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Trigger)

@given(instance=uml_umlTrace_Interval_strategy)
@settings(max_examples=50)
def test_uml_umltrace_interval_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Interval)

@given(instance=TracedStructuredClassifier_strategy)
@settings(max_examples=50)
def test_tracedstructuredclassifier_instantiation(instance):
    assert isinstance(instance, TracedStructuredClassifier)

@given(instance=umlTrace_uml_TracedEncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedencapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedEncapsulatedClassifier)

@given(instance=uml_umlTrace_Image_strategy)
@settings(max_examples=50)
def test_uml_umltrace_image_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Image)

@given(instance=uml_umlTrace_ConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml_umltrace_connectorend_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ConnectorEnd)

@given(instance=uml_TracedEvent_strategy)
@settings(max_examples=50)
def test_uml_tracedevent_instantiation(instance):
    assert isinstance(instance, uml_TracedEvent)

@given(instance=TracedInputPin_strategy)
@settings(max_examples=50)
def test_tracedinputpin_instantiation(instance):
    assert isinstance(instance, TracedInputPin)

@given(instance=umlTrace_uml_TracedValuePin_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedvaluepin_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedValuePin)

@given(instance=umlTrace_uml_TracedActionInputPin_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactioninputpin_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActionInputPin)

@given(instance=uml_umlTrace_Parameter_strategy)
@settings(max_examples=50)
def test_uml_umltrace_parameter_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Parameter)

@given(instance=uml_umlTrace_ProfileApplication_strategy)
@settings(max_examples=50)
def test_uml_umltrace_profileapplication_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ProfileApplication)

@given(instance=TracedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_tracedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, TracedMultiplicityElement)

@given(instance=umlTrace_uml_TracedConnectorEnd_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconnectorend_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConnectorEnd)

@given(instance=uml_umlTrace_TemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_umltrace_templateparameter_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_TemplateParameter)

@given(instance=uml_umlTrace_ClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_clearvariableaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ClearVariableAction)

@given(instance=uml_umlTrace_LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml_umltrace_literalinteger_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_LiteralInteger)

@given(instance=uml_umlTrace_InitialNode_strategy)
@settings(max_examples=50)
def test_uml_umltrace_initialnode_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_InitialNode)

@given(instance=uml_umlTrace_QualifierValue_strategy)
@settings(max_examples=50)
def test_uml_umltrace_qualifiervalue_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_QualifierValue)

@given(instance=uml_umlTrace_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml_umltrace_literalboolean_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_LiteralBoolean)

@given(instance=uml_umlTrace_Message_strategy)
@settings(max_examples=50)
def test_uml_umltrace_message_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Message)

@given(instance=uml_umlTrace_ReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_readvariableaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ReadVariableAction)

@given(instance=uml_umlTrace_Extend_strategy)
@settings(max_examples=50)
def test_uml_umltrace_extend_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Extend)

@given(instance=uml_TracedMessageEnd_strategy)
@settings(max_examples=50)
def test_uml_tracedmessageend_instantiation(instance):
    assert isinstance(instance, uml_TracedMessageEnd)

@given(instance=uml_umlTrace_ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ReadLinkObjectEndQualifierAction)

@given(instance=uml_umlTrace_TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_uml_umltrace_templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_TemplateParameterSubstitution)

@given(instance=uml_umlTrace_CreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_createlinkaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_CreateLinkAction)

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

@given(instance=TracedInteractionUse_strategy)
@settings(max_examples=50)
def test_tracedinteractionuse_instantiation(instance):
    assert isinstance(instance, TracedInteractionUse)

@given(instance=umlTrace_uml_TracedPartDecomposition_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpartdecomposition_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPartDecomposition)

@given(instance=uml_umlTrace_Generalization_strategy)
@settings(max_examples=50)
def test_uml_umltrace_generalization_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Generalization)

@given(instance=uml_umlTrace_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml_umltrace_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_StructuredActivityNode)

@given(instance=uml_umlTrace_MergeNode_strategy)
@settings(max_examples=50)
def test_uml_umltrace_mergenode_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_MergeNode)

@given(instance=uml_umlTrace_ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ReadStructuralFeatureAction)

@given(instance=uml_TracedEncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml_tracedencapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, uml_TracedEncapsulatedClassifier)

@given(instance=uml_umlTrace_Duration_strategy)
@settings(max_examples=50)
def test_uml_umltrace_duration_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Duration)

@given(instance=uml_TracedObservation_strategy)
@settings(max_examples=50)
def test_uml_tracedobservation_instantiation(instance):
    assert isinstance(instance, uml_TracedObservation)

@given(instance=uml_umlTrace_ParameterSet_strategy)
@settings(max_examples=50)
def test_uml_umltrace_parameterset_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ParameterSet)

@given(instance=uml_umlTrace_LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml_umltrace_literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_LiteralUnlimitedNatural)

@given(instance=uml_umlTrace_Class_strategy)
@settings(max_examples=50)
def test_uml_umltrace_class_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Class)

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

@given(instance=uml_umlTrace_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml_umltrace_activityparameternode_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ActivityParameterNode)

@given(instance=uml_umlTrace_State_strategy)
@settings(max_examples=50)
def test_uml_umltrace_state_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_State)

@given(instance=uml_TracedBehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml_tracedbehavioralfeature_instantiation(instance):
    assert isinstance(instance, uml_TracedBehavioralFeature)

@given(instance=uml_TracedVertex_strategy)
@settings(max_examples=50)
def test_uml_tracedvertex_instantiation(instance):
    assert isinstance(instance, uml_TracedVertex)

@given(instance=ecore_umlTrace_EAnnotation_strategy)
@settings(max_examples=50)
def test_ecore_umltrace_eannotation_instantiation(instance):
    assert isinstance(instance, ecore_umlTrace_EAnnotation)

@given(instance=umlTrace_ecore_TracedEModelElement_strategy)
@settings(max_examples=50)
def test_umltrace_ecore_tracedemodelelement_instantiation(instance):
    assert isinstance(instance, umlTrace_ecore_TracedEModelElement)

@given(instance=uml_umlTrace_CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml_umltrace_centralbuffernode_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_CentralBufferNode)

@given(instance=umlTrace_uml_TracedCentralBufferNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcentralbuffernode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCentralBufferNode)

@given(instance=uml_umlTrace_UnmarshallAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_unmarshallaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_UnmarshallAction)

@given(instance=TracedArtifact_strategy)
@settings(max_examples=50)
def test_tracedartifact_instantiation(instance):
    assert isinstance(instance, TracedArtifact)

@given(instance=umlTrace_uml_TracedDeploymentSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddeploymentspecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDeploymentSpecification)

@given(instance=TracedOpaqueBehavior_strategy)
@settings(max_examples=50)
def test_tracedopaquebehavior_instantiation(instance):
    assert isinstance(instance, TracedOpaqueBehavior)

@given(instance=umlTrace_uml_TracedFunctionBehavior_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedfunctionbehavior_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedFunctionBehavior)

@given(instance=uml_umlTrace_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml_umltrace_opaqueexpression_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_OpaqueExpression)

@given(instance=uml_umlTrace_ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ClearStructuralFeatureAction)

@given(instance=uml_umlTrace_TemplateBinding_strategy)
@settings(max_examples=50)
def test_uml_umltrace_templatebinding_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_TemplateBinding)

@given(instance=umlTrace_uml_TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExecutableNode)

@given(instance=uml_umlTrace_BehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml_umltrace_behaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_BehaviorExecutionSpecification)

@given(instance=uml_umlTrace_Actor_strategy)
@settings(max_examples=50)
def test_uml_umltrace_actor_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Actor)

@given(instance=umlTrace_uml_TracedActor_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactor_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActor)

@given(instance=TracedAcceptEventAction_strategy)
@settings(max_examples=50)
def test_tracedaccepteventaction_instantiation(instance):
    assert isinstance(instance, TracedAcceptEventAction)

@given(instance=umlTrace_uml_TracedAcceptCallAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedacceptcallaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAcceptCallAction)

@given(instance=uml_umlTrace_ReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_readselfaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ReadSelfAction)

@given(instance=uml_umlTrace_ActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml_umltrace_actionexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ActionExecutionSpecification)

@given(instance=TracedExecutionSpecification_strategy)
@settings(max_examples=50)
def test_tracedexecutionspecification_instantiation(instance):
    assert isinstance(instance, TracedExecutionSpecification)

@given(instance=umlTrace_uml_TracedBehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedbehaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedBehaviorExecutionSpecification)

@given(instance=umlTrace_uml_TracedActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactionexecutionspecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActionExecutionSpecification)

@given(instance=uml_umlTrace_ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml_umltrace_connectionpointreference_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ConnectionPointReference)

@given(instance=umlTrace_uml_TracedConnectionPointReference_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconnectionpointreference_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConnectionPointReference)

@given(instance=uml_umlTrace_CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_callbehavioraction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_CallBehaviorAction)

@given(instance=uml_umlTrace_GeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml_umltrace_generalordering_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_GeneralOrdering)

@given(instance=uml_umlTrace_Gate_strategy)
@settings(max_examples=50)
def test_uml_umltrace_gate_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Gate)

@given(instance=TracedMessageEnd_strategy)
@settings(max_examples=50)
def test_tracedmessageend_instantiation(instance):
    assert isinstance(instance, TracedMessageEnd)

@given(instance=TracedInterval_strategy)
@settings(max_examples=50)
def test_tracedinterval_instantiation(instance):
    assert isinstance(instance, TracedInterval)

@given(instance=umlTrace_uml_TracedGate_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedgate_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedGate)

@given(instance=uml_umlTrace_ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ReclassifyObjectAction)

@given(instance=umlTrace_uml_TracedTimeInterval_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtimeinterval_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTimeInterval)

@given(instance=uml_umlTrace_RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_RemoveVariableValueAction)

@given(instance=TracedProperty_strategy)
@settings(max_examples=50)
def test_tracedproperty_instantiation(instance):
    assert isinstance(instance, TracedProperty)

@given(instance=umlTrace_uml_TracedRemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedremovevariablevalueaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRemoveVariableValueAction)

@given(instance=umlTrace_uml_TracedPort_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedport_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPort)

@given(instance=uml_umlTrace_LiteralReal_strategy)
@settings(max_examples=50)
def test_uml_umltrace_literalreal_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_LiteralReal)

@given(instance=uml_TracedStructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml_tracedstructuredclassifier_instantiation(instance):
    assert isinstance(instance, uml_TracedStructuredClassifier)

@given(instance=uml_umlTrace_InformationItem_strategy)
@settings(max_examples=50)
def test_uml_umltrace_informationitem_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_InformationItem)

@given(instance=uml_umlTrace_InteractionUse_strategy)
@settings(max_examples=50)
def test_uml_umltrace_interactionuse_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_InteractionUse)

@given(instance=TracedElement_strategy)
@settings(max_examples=50)
def test_tracedelement_instantiation(instance):
    assert isinstance(instance, TracedElement)

@given(instance=umlTrace_uml_TracedTemplateableElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtemplateableelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTemplateableElement)

@given(instance=umlTrace_uml_TracedQualifierValue_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedqualifiervalue_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedQualifierValue)

@given(instance=umlTrace_uml_TracedClause_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclause_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClause)

@given(instance=umlTrace_uml_TracedImage_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedimage_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedImage)

@given(instance=umlTrace_uml_TracedParameterableElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedparameterableelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedParameterableElement)

@given(instance=umlTrace_uml_TracedTemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtemplateparametersubstitution_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTemplateParameterSubstitution)

@given(instance=umlTrace_uml_TracedTemplateParameter_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtemplateparameter_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTemplateParameter)

@given(instance=umlTrace_uml_TracedLinkEndData_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedlinkenddata_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLinkEndData)

@given(instance=umlTrace_uml_TracedComment_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcomment_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedComment)

@given(instance=umlTrace_uml_TracedTemplateSignature_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtemplatesignature_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTemplateSignature)

@given(instance=uml_umlTrace_StateInvariant_strategy)
@settings(max_examples=50)
def test_uml_umltrace_stateinvariant_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_StateInvariant)

@given(instance=uml_umlTrace_Association_strategy)
@settings(max_examples=50)
def test_uml_umltrace_association_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Association)

@given(instance=uml_umlTrace_Collaboration_strategy)
@settings(max_examples=50)
def test_uml_umltrace_collaboration_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Collaboration)

@given(instance=uml_umlTrace_Variable_strategy)
@settings(max_examples=50)
def test_uml_umltrace_variable_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Variable)

@given(instance=uml_umlTrace_ExceptionHandler_strategy)
@settings(max_examples=50)
def test_uml_umltrace_exceptionhandler_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ExceptionHandler)

@given(instance=TracedCombinedFragment_strategy)
@settings(max_examples=50)
def test_tracedcombinedfragment_instantiation(instance):
    assert isinstance(instance, TracedCombinedFragment)

@given(instance=umlTrace_uml_TracedExceptionHandler_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexceptionhandler_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExceptionHandler)

@given(instance=umlTrace_uml_TracedConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconsiderignorefragment_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConsiderIgnoreFragment)

@given(instance=uml_TracedExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml_TracedExecutionSpecification)

@given(instance=uml_umlTrace_Expression_strategy)
@settings(max_examples=50)
def test_uml_umltrace_expression_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Expression)

@given(instance=TracedOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_tracedoccurrencespecification_instantiation(instance):
    assert isinstance(instance, TracedOccurrenceSpecification)

@given(instance=TracedValueSpecification_strategy)
@settings(max_examples=50)
def test_tracedvaluespecification_instantiation(instance):
    assert isinstance(instance, TracedValueSpecification)

@given(instance=umlTrace_uml_TracedInterval_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinterval_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInterval)

@given(instance=umlTrace_uml_TracedDuration_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedduration_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDuration)

@given(instance=umlTrace_uml_TracedOpaqueExpression_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedopaqueexpression_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOpaqueExpression)

@given(instance=umlTrace_uml_TracedInstanceValue_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinstancevalue_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInstanceValue)

@given(instance=umlTrace_uml_TracedTimeExpression_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtimeexpression_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTimeExpression)

@given(instance=umlTrace_uml_TracedExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexecutionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExecutionOccurrenceSpecification)

@given(instance=umlTrace_uml_TracedExpression_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexpression_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExpression)

@given(instance=uml_umlTrace_PackageImport_strategy)
@settings(max_examples=50)
def test_uml_umltrace_packageimport_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_PackageImport)

@given(instance=uml_umlTrace_ReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_readlinkaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ReadLinkAction)

@given(instance=uml_TracedTemplateableElement_strategy)
@settings(max_examples=50)
def test_uml_tracedtemplateableelement_instantiation(instance):
    assert isinstance(instance, uml_TracedTemplateableElement)

@given(instance=uml_TracedType_strategy)
@settings(max_examples=50)
def test_uml_tracedtype_instantiation(instance):
    assert isinstance(instance, uml_TracedType)

@given(instance=uml_TracedRedefinableElement_strategy)
@settings(max_examples=50)
def test_uml_tracedredefinableelement_instantiation(instance):
    assert isinstance(instance, uml_TracedRedefinableElement)

@given(instance=uml_umlTrace_Operation_strategy)
@settings(max_examples=50)
def test_uml_umltrace_operation_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Operation)

@given(instance=uml_TracedNamespace_strategy)
@settings(max_examples=50)
def test_uml_tracednamespace_instantiation(instance):
    assert isinstance(instance, uml_TracedNamespace)

@given(instance=umlTrace_uml_TracedState_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstate_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedState)

@given(instance=umlTrace_uml_TracedTransition_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtransition_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTransition)

@given(instance=umlTrace_uml_TracedRegion_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedregion_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRegion)

@given(instance=umlTrace_uml_TracedClassifier_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclassifier_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClassifier)

@given(instance=TracedNamedElement_strategy)
@settings(max_examples=50)
def test_tracednamedelement_instantiation(instance):
    assert isinstance(instance, TracedNamedElement)

@given(instance=umlTrace_uml_TracedTrigger_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtrigger_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTrigger)

@given(instance=umlTrace_uml_TracedVertex_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedvertex_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedVertex)

@given(instance=umlTrace_uml_TracedParameterSet_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedparameterset_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedParameterSet)

@given(instance=umlTrace_uml_TracedDeploymentTarget_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddeploymenttarget_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDeploymentTarget)

@given(instance=umlTrace_uml_TracedNamespace_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracednamespace_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedNamespace)

@given(instance=umlTrace_uml_TracedGeneralOrdering_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedgeneralordering_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedGeneralOrdering)

@given(instance=umlTrace_uml_TracedTypedElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtypedelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTypedElement)

@given(instance=umlTrace_uml_TracedRedefinableElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedredefinableelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRedefinableElement)

@given(instance=umlTrace_uml_TracedMessage_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmessage_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedMessage)

@given(instance=umlTrace_uml_TracedMessageEnd_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmessageend_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedMessageEnd)

@given(instance=umlTrace_uml_TracedInteractionFragment_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinteractionfragment_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInteractionFragment)

@given(instance=uml_umlTrace_FlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml_umltrace_flowfinalnode_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_FlowFinalNode)

@given(instance=TracedCentralBufferNode_strategy)
@settings(max_examples=50)
def test_tracedcentralbuffernode_instantiation(instance):
    assert isinstance(instance, TracedCentralBufferNode)

@given(instance=umlTrace_uml_TracedDataStoreNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddatastorenode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDataStoreNode)

@given(instance=uml_umlTrace_DurationObservation_strategy)
@settings(max_examples=50)
def test_uml_umltrace_durationobservation_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_DurationObservation)

@given(instance=uml_TracedNamedElement_strategy)
@settings(max_examples=50)
def test_uml_tracednamedelement_instantiation(instance):
    assert isinstance(instance, uml_TracedNamedElement)

@given(instance=TracedObservation_strategy)
@settings(max_examples=50)
def test_tracedobservation_instantiation(instance):
    assert isinstance(instance, TracedObservation)

@given(instance=umlTrace_uml_TracedDurationObservation_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddurationobservation_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDurationObservation)

@given(instance=uml_umlTrace_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml_umltrace_activityfinalnode_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ActivityFinalNode)

@given(instance=TracedFinalNode_strategy)
@settings(max_examples=50)
def test_tracedfinalnode_instantiation(instance):
    assert isinstance(instance, TracedFinalNode)

@given(instance=umlTrace_uml_TracedFlowFinalNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedflowfinalnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedFlowFinalNode)

@given(instance=umlTrace_uml_TracedActivityFinalNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactivityfinalnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActivityFinalNode)

@given(instance=TracedLinkAction_strategy)
@settings(max_examples=50)
def test_tracedlinkaction_instantiation(instance):
    assert isinstance(instance, TracedLinkAction)

@given(instance=umlTrace_uml_TracedWriteLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedwritelinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedWriteLinkAction)

@given(instance=umlTrace_uml_TracedReadLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadlinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadLinkAction)

@given(instance=uml_umlTrace_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_AddStructuralFeatureValueAction)

@given(instance=TracedInstanceSpecification_strategy)
@settings(max_examples=50)
def test_tracedinstancespecification_instantiation(instance):
    assert isinstance(instance, TracedInstanceSpecification)

@given(instance=umlTrace_uml_TracedEnumerationLiteral_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedenumerationliteral_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedEnumerationLiteral)

@given(instance=uml_umlTrace_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_accepteventaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_AcceptEventAction)

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

@given(instance=TracedBehavior_strategy)
@settings(max_examples=50)
def test_tracedbehavior_instantiation(instance):
    assert isinstance(instance, TracedBehavior)

@given(instance=umlTrace_uml_TracedActivity_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactivity_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActivity)

@given(instance=umlTrace_uml_TracedOpaqueBehavior_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedopaquebehavior_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOpaqueBehavior)

@given(instance=uml_umlTrace_SendSignalAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_sendsignalaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_SendSignalAction)

@given(instance=TracedInvocationAction_strategy)
@settings(max_examples=50)
def test_tracedinvocationaction_instantiation(instance):
    assert isinstance(instance, TracedInvocationAction)

@given(instance=umlTrace_uml_TracedCallAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcallaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCallAction)

@given(instance=umlTrace_uml_TracedSendSignalAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedsendsignalaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSendSignalAction)

@given(instance=uml_umlTrace_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_RemoveStructuralFeatureValueAction)

@given(instance=TracedWriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_tracedwritestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, TracedWriteStructuralFeatureAction)

@given(instance=umlTrace_uml_TracedAddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedaddstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAddStructuralFeatureValueAction)

@given(instance=uml_TracedBehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml_tracedbehavioredclassifier_instantiation(instance):
    assert isinstance(instance, uml_TracedBehavioredClassifier)

@given(instance=umlTrace_uml_TracedClass_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclass_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClass)

@given(instance=umlTrace_uml_TracedCollaboration_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcollaboration_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCollaboration)

@given(instance=TracedRealization_strategy)
@settings(max_examples=50)
def test_tracedrealization_instantiation(instance):
    assert isinstance(instance, TracedRealization)

@given(instance=umlTrace_uml_TracedSubstitution_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedsubstitution_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSubstitution)

@given(instance=umlTrace_uml_TracedInterfaceRealization_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinterfacerealization_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInterfaceRealization)

@given(instance=TracedIntervalConstraint_strategy)
@settings(max_examples=50)
def test_tracedintervalconstraint_instantiation(instance):
    assert isinstance(instance, TracedIntervalConstraint)

@given(instance=umlTrace_uml_TracedDurationConstraint_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddurationconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDurationConstraint)

@given(instance=umlTrace_uml_TracedTimeConstraint_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtimeconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTimeConstraint)

@given(instance=uml_umlTrace_Artifact_strategy)
@settings(max_examples=50)
def test_uml_umltrace_artifact_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Artifact)

@given(instance=uml_TracedDeploymentTarget_strategy)
@settings(max_examples=50)
def test_uml_traceddeploymenttarget_instantiation(instance):
    assert isinstance(instance, uml_TracedDeploymentTarget)

@given(instance=uml_TracedConnectableElement_strategy)
@settings(max_examples=50)
def test_uml_tracedconnectableelement_instantiation(instance):
    assert isinstance(instance, uml_TracedConnectableElement)

@given(instance=umlTrace_uml_TracedRemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedremovestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRemoveStructuralFeatureValueAction)

@given(instance=uml_umlTrace_Continuation_strategy)
@settings(max_examples=50)
def test_uml_umltrace_continuation_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Continuation)

@given(instance=TracedInteractionFragment_strategy)
@settings(max_examples=50)
def test_tracedinteractionfragment_instantiation(instance):
    assert isinstance(instance, TracedInteractionFragment)

@given(instance=umlTrace_uml_TracedStateInvariant_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstateinvariant_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStateInvariant)

@given(instance=umlTrace_uml_TracedCombinedFragment_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcombinedfragment_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCombinedFragment)

@given(instance=umlTrace_uml_TracedInteractionUse_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinteractionuse_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInteractionUse)

@given(instance=umlTrace_uml_TracedContinuation_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcontinuation_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedContinuation)

@given(instance=uml_umlTrace_Property_strategy)
@settings(max_examples=50)
def test_uml_umltrace_property_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Property)

@given(instance=uml_umlTrace_Connector_strategy)
@settings(max_examples=50)
def test_uml_umltrace_connector_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Connector)

@given(instance=uml_TracedBehavior_strategy)
@settings(max_examples=50)
def test_uml_tracedbehavior_instantiation(instance):
    assert isinstance(instance, uml_TracedBehavior)

@given(instance=TracedFeature_strategy)
@settings(max_examples=50)
def test_tracedfeature_instantiation(instance):
    assert isinstance(instance, TracedFeature)

@given(instance=umlTrace_uml_TracedConnector_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconnector_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConnector)

@given(instance=uml_TracedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_uml_tracedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, uml_TracedMultiplicityElement)

@given(instance=umlTrace_uml_TracedParameter_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedparameter_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedParameter)

@given(instance=umlTrace_uml_TracedVariable_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedvariable_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedVariable)

@given(instance=umlTrace_uml_TracedPin_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpin_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPin)

@given(instance=uml_TracedTypedElement_strategy)
@settings(max_examples=50)
def test_uml_tracedtypedelement_instantiation(instance):
    assert isinstance(instance, uml_TracedTypedElement)

@given(instance=uml_TracedFeature_strategy)
@settings(max_examples=50)
def test_uml_tracedfeature_instantiation(instance):
    assert isinstance(instance, uml_TracedFeature)

@given(instance=umlTrace_uml_TracedBehavioralFeature_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedbehavioralfeature_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedBehavioralFeature)

@given(instance=umlTrace_uml_TracedStructuralFeature_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstructuralfeature_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStructuralFeature)

@given(instance=umlTrace_Input_TracedInputParameterValues_strategy)
@settings(max_examples=50)
def test_umltrace_input_tracedinputparametervalues_instantiation(instance):
    assert isinstance(instance, umlTrace_Input_TracedInputParameterValues)

@given(instance=TracedAssociation_strategy)
@settings(max_examples=50)
def test_tracedassociation_instantiation(instance):
    assert isinstance(instance, TracedAssociation)

@given(instance=umlTrace_uml_TracedCommunicationPath_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcommunicationpath_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCommunicationPath)

@given(instance=uml_umlTrace_DataType_strategy)
@settings(max_examples=50)
def test_uml_umltrace_datatype_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_DataType)

@given(instance=TracedClassifier_strategy)
@settings(max_examples=50)
def test_tracedclassifier_instantiation(instance):
    assert isinstance(instance, TracedClassifier)

@given(instance=umlTrace_uml_TracedStructuredClassifier_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstructuredclassifier_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStructuredClassifier)

@given(instance=umlTrace_uml_TracedSignal_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedsignal_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSignal)

@given(instance=umlTrace_uml_TracedInformationItem_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinformationitem_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInformationItem)

@given(instance=umlTrace_uml_TracedDataType_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddatatype_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDataType)

@given(instance=uml_umlTrace_OpaqueAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_opaqueaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_OpaqueAction)

@given(instance=TracedAction_strategy)
@settings(max_examples=50)
def test_tracedaction_instantiation(instance):
    assert isinstance(instance, TracedAction)

@given(instance=umlTrace_uml_TracedReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadIsClassifiedObjectAction)

@given(instance=umlTrace_uml_TracedReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReclassifyObjectAction)

@given(instance=umlTrace_uml_TracedInvocationAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinvocationaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInvocationAction)

@given(instance=umlTrace_uml_TracedReplyAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreplyaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReplyAction)

@given(instance=umlTrace_uml_TracedTestIdentityAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtestidentityaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTestIdentityAction)

@given(instance=umlTrace_uml_TracedLinkAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedlinkaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLinkAction)

@given(instance=umlTrace_uml_TracedReadSelfAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadselfaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadSelfAction)

@given(instance=umlTrace_uml_TracedDestroyObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddestroyobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDestroyObjectAction)

@given(instance=umlTrace_uml_TracedClearAssociationAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclearassociationaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClearAssociationAction)

@given(instance=umlTrace_uml_TracedRaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedraiseexceptionaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRaiseExceptionAction)

@given(instance=umlTrace_uml_TracedReadExtentAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadextentaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadExtentAction)

@given(instance=umlTrace_uml_TracedReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadLinkObjectEndQualifierAction)

@given(instance=umlTrace_uml_TracedUnmarshallAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedunmarshallaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedUnmarshallAction)

@given(instance=umlTrace_uml_TracedAcceptEventAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedaccepteventaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAcceptEventAction)

@given(instance=umlTrace_uml_TracedValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedvaluespecificationaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedValueSpecificationAction)

@given(instance=umlTrace_uml_TracedOpaqueAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedopaqueaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOpaqueAction)

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

@given(instance=TracedWriteStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_tracedwritestructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, TracedWriteStructuralFeatureActionActivation)

@given(instance=umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation)

@given(instance=TracedOpaqueBehaviorExecution_strategy)
@settings(max_examples=50)
def test_tracedopaquebehaviorexecution_instantiation(instance):
    assert isinstance(instance, TracedOpaqueBehaviorExecution)

@given(instance=umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_umltrace_integerfunctions_tracedintegerplusfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution)

@given(instance=umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_umltrace_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution)

@given(instance=umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_umltrace_integerfunctions_tracedintegerlessfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution)

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

@given(instance=TracedMessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_tracedmessageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, TracedMessageOccurrenceSpecification)

@given(instance=umlTrace_uml_TracedDestructionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddestructionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDestructionOccurrenceSpecification)

@given(instance=uml_umlTrace_Include_strategy)
@settings(max_examples=50)
def test_uml_umltrace_include_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Include)

@given(instance=uml_TracedDirectedRelationship_strategy)
@settings(max_examples=50)
def test_uml_traceddirectedrelationship_instantiation(instance):
    assert isinstance(instance, uml_TracedDirectedRelationship)

@given(instance=umlTrace_uml_TracedExtend_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedextend_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExtend)

@given(instance=umlTrace_uml_TracedInclude_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinclude_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInclude)

@given(instance=umlTrace_uml_TracedDurationInterval_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddurationinterval_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDurationInterval)

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

@given(instance=umlTrace_uml_TracedVariableAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedvariableaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedVariableAction)

@given(instance=uml_umlTrace_ActivityPartition_strategy)
@settings(max_examples=50)
def test_uml_umltrace_activitypartition_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ActivityPartition)

@given(instance=uml_TracedActivityGroup_strategy)
@settings(max_examples=50)
def test_uml_tracedactivitygroup_instantiation(instance):
    assert isinstance(instance, uml_TracedActivityGroup)

@given(instance=ActivityContent_strategy)
@settings(max_examples=50)
def test_activitycontent_instantiation(instance):
    assert isinstance(instance, ActivityContent)

@given(instance=umlTrace_uml_TracedActivityGroup_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactivitygroup_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActivityGroup)

@given(instance=umlTrace_uml_TracedActivityNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedactivitynode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedActivityNode)

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

@given(instance=uml_umlTrace_CollaborationUse_strategy)
@settings(max_examples=50)
def test_uml_umltrace_collaborationuse_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_CollaborationUse)

@given(instance=umlTrace_uml_TracedCollaborationUse_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcollaborationuse_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCollaborationUse)

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

@given(instance=uml_umlTrace_ProtocolConformance_strategy)
@settings(max_examples=50)
def test_uml_umltrace_protocolconformance_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ProtocolConformance)

@given(instance=TracedCreateLinkAction_strategy)
@settings(max_examples=50)
def test_tracedcreatelinkaction_instantiation(instance):
    assert isinstance(instance, TracedCreateLinkAction)

@given(instance=umlTrace_uml_TracedCreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcreatelinkobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCreateLinkObjectAction)

@given(instance=uml_umlTrace_TimeObservation_strategy)
@settings(max_examples=50)
def test_uml_umltrace_timeobservation_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_TimeObservation)

@given(instance=umlTrace_uml_TracedTimeObservation_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtimeobservation_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTimeObservation)

@given(instance=umlTrace_uml_TracedExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexecutionspecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExecutionSpecification)

@given(instance=uml_umlTrace_Lifeline_strategy)
@settings(max_examples=50)
def test_uml_umltrace_lifeline_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Lifeline)

@given(instance=TracedVariableAction_strategy)
@settings(max_examples=50)
def test_tracedvariableaction_instantiation(instance):
    assert isinstance(instance, TracedVariableAction)

@given(instance=umlTrace_uml_TracedClearVariableAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclearvariableaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClearVariableAction)

@given(instance=umlTrace_uml_TracedReadVariableAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadvariableaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadVariableAction)

@given(instance=umlTrace_uml_TracedWriteVariableAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedwritevariableaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedWriteVariableAction)

@given(instance=umlTrace_uml_TracedSendObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedsendobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSendObjectAction)

@given(instance=umlTrace_uml_TracedRelationship_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedrelationship_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRelationship)

@given(instance=TracedTemplateParameter_strategy)
@settings(max_examples=50)
def test_tracedtemplateparameter_instantiation(instance):
    assert isinstance(instance, TracedTemplateParameter)

@given(instance=umlTrace_uml_TracedOperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedoperationtemplateparameter_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOperationTemplateParameter)

@given(instance=umlTrace_uml_TracedClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclassifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClassifierTemplateParameter)

@given(instance=umlTrace_uml_TracedConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconnectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConnectableElementTemplateParameter)

@given(instance=uml_umlTrace_CallEvent_strategy)
@settings(max_examples=50)
def test_uml_umltrace_callevent_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_CallEvent)

@given(instance=uml_umlTrace_StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_StartClassifierBehaviorAction)

@given(instance=umlTrace_uml_TracedLifeline_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedlifeline_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLifeline)

@given(instance=uml_umlTrace_SendObjectAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_sendobjectaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_SendObjectAction)

@given(instance=uml_TracedAction_strategy)
@settings(max_examples=50)
def test_uml_tracedaction_instantiation(instance):
    assert isinstance(instance, uml_TracedAction)

@given(instance=umlTrace_uml_TracedStructuredActivityNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstructuredactivitynode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStructuredActivityNode)

@given(instance=uml_TracedInteractionFragment_strategy)
@settings(max_examples=50)
def test_uml_tracedinteractionfragment_instantiation(instance):
    assert isinstance(instance, uml_TracedInteractionFragment)

@given(instance=umlTrace_uml_TracedInteractionOperand_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinteractionoperand_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInteractionOperand)

@given(instance=umlTrace_uml_TracedInteraction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinteraction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInteraction)

@given(instance=umlTrace_uml_TracedStateMachine_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstatemachine_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStateMachine)

@given(instance=umlTrace_uml_TracedExtensionEnd_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedextensionend_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExtensionEnd)

@given(instance=umlTrace_uml_TracedStartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstartclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStartClassifierBehaviorAction)

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

@given(instance=uml_umlTrace_LiteralString_strategy)
@settings(max_examples=50)
def test_uml_umltrace_literalstring_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_LiteralString)

@given(instance=TracedLiteralSpecification_strategy)
@settings(max_examples=50)
def test_tracedliteralspecification_instantiation(instance):
    assert isinstance(instance, TracedLiteralSpecification)

@given(instance=umlTrace_uml_TracedLiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralunlimitednatural_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralUnlimitedNatural)

@given(instance=umlTrace_uml_TracedLiteralInteger_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralinteger_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralInteger)

@given(instance=umlTrace_uml_TracedLiteralReal_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralreal_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralReal)

@given(instance=umlTrace_uml_TracedLiteralBoolean_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralboolean_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralBoolean)

@given(instance=umlTrace_uml_TracedLiteralNull_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralnull_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralNull)

@given(instance=umlTrace_uml_TracedLiteralString_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralstring_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralString)

@given(instance=umlTrace_uml_TracedNamedElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracednamedelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedNamedElement)

@given(instance=uml_umlTrace_AnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_uml_umltrace_anyreceiveevent_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_AnyReceiveEvent)

@given(instance=uml_umlTrace_ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ReadLinkObjectEndAction)

@given(instance=uml_umlTrace_Interface_strategy)
@settings(max_examples=50)
def test_uml_umltrace_interface_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Interface)

@given(instance=umlTrace_uml_TracedReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadLinkObjectEndAction)

@given(instance=umlTrace_uml_TracedOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedoccurrencespecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOccurrenceSpecification)

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

@given(instance=uml_umlTrace_CreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_createobjectaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_CreateObjectAction)

@given(instance=umlTrace_uml_TracedCreateObjectAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcreateobjectaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCreateObjectAction)

@given(instance=umlTrace_uml_TracedInterface_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinterface_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInterface)

@given(instance=TracedClass_strategy)
@settings(max_examples=50)
def test_tracedclass_instantiation(instance):
    assert isinstance(instance, TracedClass)

@given(instance=umlTrace_uml_TracedBehavior_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedbehavior_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedBehavior)

@given(instance=umlTrace_uml_TracedComponent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcomponent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedComponent)

@given(instance=umlTrace_uml_TracedStereotype_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstereotype_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStereotype)

@given(instance=umlTrace_uml_TracedDeployedArtifact_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddeployedartifact_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDeployedArtifact)

@given(instance=uml_umlTrace_OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml_umltrace_occurrencespecification_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_OccurrenceSpecification)

@given(instance=uml_umlTrace_ExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml_umltrace_extensionpoint_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ExtensionPoint)

@given(instance=uml_umlTrace_SignalEvent_strategy)
@settings(max_examples=50)
def test_uml_umltrace_signalevent_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_SignalEvent)

@given(instance=TracedMessageEvent_strategy)
@settings(max_examples=50)
def test_tracedmessageevent_instantiation(instance):
    assert isinstance(instance, TracedMessageEvent)

@given(instance=umlTrace_uml_TracedAnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedanyreceiveevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAnyReceiveEvent)

@given(instance=umlTrace_uml_TracedCallEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcallevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCallEvent)

@given(instance=umlTrace_uml_TracedSignalEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedsignalevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSignalEvent)

@given(instance=uml_umlTrace_Slot_strategy)
@settings(max_examples=50)
def test_uml_umltrace_slot_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Slot)

@given(instance=uml_umlTrace_ElementImport_strategy)
@settings(max_examples=50)
def test_uml_umltrace_elementimport_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ElementImport)

@given(instance=TracedDirectedRelationship_strategy)
@settings(max_examples=50)
def test_traceddirectedrelationship_instantiation(instance):
    assert isinstance(instance, TracedDirectedRelationship)

@given(instance=umlTrace_uml_TracedPackageImport_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpackageimport_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPackageImport)

@given(instance=umlTrace_uml_TracedProfileApplication_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedprofileapplication_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedProfileApplication)

@given(instance=umlTrace_uml_TracedTemplateBinding_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtemplatebinding_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTemplateBinding)

@given(instance=umlTrace_uml_TracedProtocolConformance_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedprotocolconformance_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedProtocolConformance)

@given(instance=umlTrace_uml_TracedGeneralization_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedgeneralization_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedGeneralization)

@given(instance=umlTrace_uml_TracedPackageMerge_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpackagemerge_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPackageMerge)

@given(instance=umlTrace_uml_TracedElementImport_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedelementimport_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedElementImport)

@given(instance=uml_umlTrace_StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_StartObjectBehaviorAction)

@given(instance=TracedCallAction_strategy)
@settings(max_examples=50)
def test_tracedcallaction_instantiation(instance):
    assert isinstance(instance, TracedCallAction)

@given(instance=umlTrace_uml_TracedCallOperationAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcalloperationaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCallOperationAction)

@given(instance=umlTrace_uml_TracedCallBehaviorAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcallbehavioraction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedCallBehaviorAction)

@given(instance=umlTrace_uml_TracedStartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstartobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStartObjectBehaviorAction)

@given(instance=uml_umlTrace_JoinNode_strategy)
@settings(max_examples=50)
def test_uml_umltrace_joinnode_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_JoinNode)

@given(instance=TracedControlNode_strategy)
@settings(max_examples=50)
def test_tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, TracedControlNode)

@given(instance=umlTrace_uml_TracedForkNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedforknode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedForkNode)

@given(instance=umlTrace_uml_TracedDecisionNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddecisionnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDecisionNode)

@given(instance=umlTrace_uml_TracedFinalNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedfinalnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedFinalNode)

@given(instance=umlTrace_uml_TracedMergeNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmergenode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedMergeNode)

@given(instance=umlTrace_uml_TracedInitialNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinitialnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInitialNode)

@given(instance=umlTrace_uml_TracedJoinNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedjoinnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedJoinNode)

@given(instance=TracedEModelElement_strategy)
@settings(max_examples=50)
def test_tracedemodelelement_instantiation(instance):
    assert isinstance(instance, TracedEModelElement)

@given(instance=umlTrace_uml_TracedElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedElement)

@given(instance=TracedStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_tracedstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, TracedStructuralFeatureAction)

@given(instance=umlTrace_uml_TracedClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedclearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedClearStructuralFeatureAction)

@given(instance=umlTrace_uml_TracedReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreadstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReadStructuralFeatureAction)

@given(instance=umlTrace_uml_TracedWriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedwritestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedWriteStructuralFeatureAction)

@given(instance=umlTrace_uml_TracedSlot_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedslot_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSlot)

@given(instance=umlTrace_uml_TracedComponentRealization_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedcomponentrealization_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedComponentRealization)

@given(instance=umlTrace_uml_TracedReduceAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedreduceaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedReduceAction)

@given(instance=uml_umlTrace_GeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml_umltrace_generalizationset_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_GeneralizationSet)

@given(instance=TracedConstraint_strategy)
@settings(max_examples=50)
def test_tracedconstraint_instantiation(instance):
    assert isinstance(instance, TracedConstraint)

@given(instance=umlTrace_uml_TracedIntervalConstraint_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedintervalconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedIntervalConstraint)

@given(instance=umlTrace_uml_TracedInteractionConstraint_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinteractionconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInteractionConstraint)

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

@given(instance=uml_TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_uml_tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, uml_TracedExecutableNode)

@given(instance=TracedStructuredActivityNode_strategy)
@settings(max_examples=50)
def test_tracedstructuredactivitynode_instantiation(instance):
    assert isinstance(instance, TracedStructuredActivityNode)

@given(instance=umlTrace_uml_TracedExpansionRegion_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedexpansionregion_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExpansionRegion)

@given(instance=umlTrace_uml_TracedConditionalNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconditionalnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConditionalNode)

@given(instance=umlTrace_uml_TracedLoopNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedloopnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLoopNode)

@given(instance=umlTrace_uml_TracedSequenceNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedsequencenode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedSequenceNode)

@given(instance=uml_umlTrace_InputPin_strategy)
@settings(max_examples=50)
def test_uml_umltrace_inputpin_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_InputPin)

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

@given(instance=uml_umlTrace_ReduceAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_reduceaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_ReduceAction)

@given(instance=umlTrace_uml_TracedStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStructuralFeatureAction)

@given(instance=umlTrace_uml_TracedBehavioredClassifier_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedbehavioredclassifier_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedBehavioredClassifier)

@given(instance=uml_umlTrace_Package_strategy)
@settings(max_examples=50)
def test_uml_umltrace_package_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Package)

@given(instance=umlTrace_uml_TracedLiteralSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedliteralspecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedLiteralSpecification)

@given(instance=umlTrace_uml_TracedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedMultiplicityElement)

@given(instance=uml_umlTrace_Constraint_strategy)
@settings(max_examples=50)
def test_uml_umltrace_constraint_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_Constraint)

@given(instance=uml_TracedPackageableElement_strategy)
@settings(max_examples=50)
def test_uml_tracedpackageableelement_instantiation(instance):
    assert isinstance(instance, uml_TracedPackageableElement)

@given(instance=umlTrace_uml_TracedValueSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedvaluespecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedValueSpecification)

@given(instance=umlTrace_uml_TracedInstanceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinstancespecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInstanceSpecification)

@given(instance=umlTrace_uml_TracedInformationFlow_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedinformationflow_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedInformationFlow)

@given(instance=umlTrace_uml_TracedDependency_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddependency_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDependency)

@given(instance=umlTrace_uml_TracedPackage_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpackage_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPackage)

@given(instance=TracedTransition_strategy)
@settings(max_examples=50)
def test_tracedtransition_instantiation(instance):
    assert isinstance(instance, TracedTransition)

@given(instance=umlTrace_uml_TracedProtocolTransition_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedprotocoltransition_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedProtocolTransition)

@given(instance=umlTrace_uml_TracedExtension_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedextension_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedExtension)

@given(instance=TracedPackageableElement_strategy)
@settings(max_examples=50)
def test_tracedpackageableelement_instantiation(instance):
    assert isinstance(instance, TracedPackageableElement)

@given(instance=umlTrace_uml_TracedObservation_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedobservation_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedObservation)

@given(instance=umlTrace_uml_TracedGeneralizationSet_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedgeneralizationset_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedGeneralizationSet)

@given(instance=umlTrace_uml_TracedEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedEvent)

@given(instance=umlTrace_uml_TracedConstraint_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconstraint_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConstraint)

@given(instance=umlTrace_uml_TracedType_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtype_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedType)

@given(instance=uml_TracedParameterableElement_strategy)
@settings(max_examples=50)
def test_uml_tracedparameterableelement_instantiation(instance):
    assert isinstance(instance, uml_TracedParameterableElement)

@given(instance=umlTrace_uml_TracedConnectableElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedconnectableelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedConnectableElement)

@given(instance=umlTrace_uml_TracedOperation_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedoperation_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedOperation)

@given(instance=umlTrace_uml_TracedPackageableElement_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedpackageableelement_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedPackageableElement)

@given(instance=uml_umlTrace_TimeEvent_strategy)
@settings(max_examples=50)
def test_uml_umltrace_timeevent_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_TimeEvent)

@given(instance=TracedEvent_strategy)
@settings(max_examples=50)
def test_tracedevent_instantiation(instance):
    assert isinstance(instance, TracedEvent)

@given(instance=umlTrace_uml_TracedMessageEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmessageevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedMessageEvent)

@given(instance=umlTrace_uml_TracedChangeEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedchangeevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedChangeEvent)

@given(instance=umlTrace_uml_TracedTimeEvent_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedtimeevent_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedTimeEvent)

@given(instance=TracedRelationship_strategy)
@settings(max_examples=50)
def test_tracedrelationship_instantiation(instance):
    assert isinstance(instance, TracedRelationship)

@given(instance=umlTrace_uml_TracedDirectedRelationship_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddirectedrelationship_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDirectedRelationship)

@given(instance=TracedDependency_strategy)
@settings(max_examples=50)
def test_traceddependency_instantiation(instance):
    assert isinstance(instance, TracedDependency)

@given(instance=umlTrace_uml_TracedAbstraction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedabstraction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAbstraction)

@given(instance=umlTrace_uml_TracedUsage_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedusage_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedUsage)

@given(instance=umlTrace_uml_TracedDeployment_strategy)
@settings(max_examples=50)
def test_umltrace_uml_traceddeployment_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedDeployment)

@given(instance=uml_umlTrace_BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml_umltrace_broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_BroadcastSignalAction)

@given(instance=umlTrace_uml_TracedBroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedbroadcastsignalaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedBroadcastSignalAction)

@given(instance=uml_umlTrace_TemplateSignature_strategy)
@settings(max_examples=50)
def test_uml_umltrace_templatesignature_instantiation(instance):
    assert isinstance(instance, uml_umlTrace_TemplateSignature)

@given(instance=TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, TracedExecutableNode)

@given(instance=umlTrace_uml_TracedAction_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedaction_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedAction)

@given(instance=uml_TracedLinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_uml_tracedlinkenddestructiondata_instantiation(instance):
    assert isinstance(instance, uml_TracedLinkEndDestructionData)

@given(instance=uml_TracedClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_tracedclassifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, uml_TracedClassifierTemplateParameter)

@given(instance=IntermediateActions_TracedAddStructuralFeatureValueActionActivation_strategy)
@settings(max_examples=50)
def test_intermediateactions_tracedaddstructuralfeaturevalueactionactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActions_TracedAddStructuralFeatureValueActionActivation)

@given(instance=BasicActions_TracedCallBehaviorActionActivation_strategy)
@settings(max_examples=50)
def test_basicactions_tracedcallbehavioractionactivation_instantiation(instance):
    assert isinstance(instance, BasicActions_TracedCallBehaviorActionActivation)

@given(instance=uml_TracedProtocolConformance_strategy)
@settings(max_examples=50)
def test_uml_tracedprotocolconformance_instantiation(instance):
    assert isinstance(instance, uml_TracedProtocolConformance)

@given(instance=uml_TracedLoopNode_strategy)
@settings(max_examples=50)
def test_uml_tracedloopnode_instantiation(instance):
    assert isinstance(instance, uml_TracedLoopNode)

@given(instance=uml_TracedExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml_tracedexpansionregion_instantiation(instance):
    assert isinstance(instance, uml_TracedExpansionRegion)

@given(instance=uml_TracedActivityPartition_strategy)
@settings(max_examples=50)
def test_uml_tracedactivitypartition_instantiation(instance):
    assert isinstance(instance, uml_TracedActivityPartition)

@given(instance=uml_TracedCollaborationUse_strategy)
@settings(max_examples=50)
def test_uml_tracedcollaborationuse_instantiation(instance):
    assert isinstance(instance, uml_TracedCollaborationUse)

@given(instance=uml_TracedEnumeration_strategy)
@settings(max_examples=50)
def test_uml_tracedenumeration_instantiation(instance):
    assert isinstance(instance, uml_TracedEnumeration)

@given(instance=uml_TracedLifeline_strategy)
@settings(max_examples=50)
def test_uml_tracedlifeline_instantiation(instance):
    assert isinstance(instance, uml_TracedLifeline)

@given(instance=uml_TracedSendObjectAction_strategy)
@settings(max_examples=50)
def test_uml_tracedsendobjectaction_instantiation(instance):
    assert isinstance(instance, uml_TracedSendObjectAction)

@given(instance=uml_TracedConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_tracedconnectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml_TracedConnectableElementTemplateParameter)

@given(instance=uml_TracedCallEvent_strategy)
@settings(max_examples=50)
def test_uml_tracedcallevent_instantiation(instance):
    assert isinstance(instance, uml_TracedCallEvent)

@given(instance=uml_TracedStartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml_tracedstartclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, uml_TracedStartClassifierBehaviorAction)

@given(instance=uml_TracedRealization_strategy)
@settings(max_examples=50)
def test_uml_tracedrealization_instantiation(instance):
    assert isinstance(instance, uml_TracedRealization)

@given(instance=uml_TracedCreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml_tracedcreatelinkobjectaction_instantiation(instance):
    assert isinstance(instance, uml_TracedCreateLinkObjectAction)

@given(instance=IntermediateActivities_TracedControlToken_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedcontroltoken_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedControlToken)

@given(instance=uml_TracedTimeObservation_strategy)
@settings(max_examples=50)
def test_uml_tracedtimeobservation_instantiation(instance):
    assert isinstance(instance, uml_TracedTimeObservation)

@given(instance=uml_TracedExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml_tracedextensionend_instantiation(instance):
    assert isinstance(instance, uml_TracedExtensionEnd)

@given(instance=uml_TracedComponent_strategy)
@settings(max_examples=50)
def test_uml_tracedcomponent_instantiation(instance):
    assert isinstance(instance, uml_TracedComponent)

@given(instance=uml_TracedAnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_uml_tracedanyreceiveevent_instantiation(instance):
    assert isinstance(instance, uml_TracedAnyReceiveEvent)

@given(instance=uml_TracedReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadLinkObjectEndAction)

@given(instance=uml_TracedConditionalNode_strategy)
@settings(max_examples=50)
def test_uml_tracedconditionalnode_instantiation(instance):
    assert isinstance(instance, uml_TracedConditionalNode)

@given(instance=uml_TracedInterface_strategy)
@settings(max_examples=50)
def test_uml_tracedinterface_instantiation(instance):
    assert isinstance(instance, uml_TracedInterface)

@given(instance=uml_TracedStereotype_strategy)
@settings(max_examples=50)
def test_uml_tracedstereotype_instantiation(instance):
    assert isinstance(instance, uml_TracedStereotype)

@given(instance=uml_TracedLiteralString_strategy)
@settings(max_examples=50)
def test_uml_tracedliteralstring_instantiation(instance):
    assert isinstance(instance, uml_TracedLiteralString)

@given(instance=uml_TracedInteraction_strategy)
@settings(max_examples=50)
def test_uml_tracedinteraction_instantiation(instance):
    assert isinstance(instance, uml_TracedInteraction)

@given(instance=IntermediateActivities_TracedMergeNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedmergenodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedMergeNodeActivation)

@given(instance=uml_TracedStateMachine_strategy)
@settings(max_examples=50)
def test_uml_tracedstatemachine_instantiation(instance):
    assert isinstance(instance, uml_TracedStateMachine)

@given(instance=uml_TracedOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml_TracedOccurrenceSpecification)

@given(instance=umlTrace_uml_TracedMessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedmessageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedMessageOccurrenceSpecification)

@given(instance=uml_TracedExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml_tracedexecutionenvironment_instantiation(instance):
    assert isinstance(instance, uml_TracedExecutionEnvironment)

@given(instance=umlTrace_Loci_TracedLocus_strategy)
@settings(max_examples=50)
def test_umltrace_loci_tracedlocus_instantiation(instance):
    assert isinstance(instance, umlTrace_Loci_TracedLocus)

@given(instance=umlTrace_Loci_TracedExecutionFactory_strategy)
@settings(max_examples=50)
def test_umltrace_loci_tracedexecutionfactory_instantiation(instance):
    assert isinstance(instance, umlTrace_Loci_TracedExecutionFactory)

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

@given(instance=TracedActionActivation_strategy)
@settings(max_examples=50)
def test_tracedactionactivation_instantiation(instance):
    assert isinstance(instance, TracedActionActivation)

@given(instance=umlTrace_IntermediateActions_TracedCreateObjectActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactions_tracedcreateobjectactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActions_TracedCreateObjectActionActivation)

@given(instance=umlTrace_BasicActions_TracedInvocationActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_basicactions_tracedinvocationactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicActions_TracedInvocationActionActivation)

@given(instance=umlTrace_BasicActions_TracedOpaqueActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_basicactions_tracedopaqueactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicActions_TracedOpaqueActionActivation)

@given(instance=umlTrace_IntermediateActions_TracedValueSpecificationActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactions_tracedvaluespecificationactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActions_TracedValueSpecificationActionActivation)

@given(instance=umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactions_tracedstructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation)

@given(instance=umlTrace_Loci_TracedExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_umltrace_loci_tracedexecutionenvironment_instantiation(instance):
    assert isinstance(instance, umlTrace_Loci_TracedExecutionEnvironment)

@given(instance=umlTrace_Loci_TracedExecutor_strategy)
@settings(max_examples=50)
def test_umltrace_loci_tracedexecutor_instantiation(instance):
    assert isinstance(instance, umlTrace_Loci_TracedExecutor)

@given(instance=umlTrace_Loci_TracedSemanticVisitor_strategy)
@settings(max_examples=50)
def test_umltrace_loci_tracedsemanticvisitor_instantiation(instance):
    assert isinstance(instance, umlTrace_Loci_TracedSemanticVisitor)

@given(instance=umlTrace_IntermediateActivities_TracedActivityEdgeInstance_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedactivityedgeinstance_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedActivityEdgeInstance)

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

@given(instance=umlTrace_IntermediateActivities_TracedOffer_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedoffer_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedOffer)

@given(instance=umlTrace_IntermediateActivities_TracedToken_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedtoken_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedToken)

@given(instance=umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedactivitynodeactivationgroup_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup)

@given(instance=TracedActivityNodeActivation_strategy)
@settings(max_examples=50)
def test_tracedactivitynodeactivation_instantiation(instance):
    assert isinstance(instance, TracedActivityNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedControlNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedcontrolnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedControlNodeActivation)

@given(instance=umlTrace_BasicActions_TracedActionActivation_strategy)
@settings(max_examples=50)
def test_umltrace_basicactions_tracedactionactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicActions_TracedActionActivation)

@given(instance=umlTrace_IntermediateActivities_TracedObjectNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedobjectnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedObjectNodeActivation)

@given(instance=TracedControlNodeActivation_strategy)
@settings(max_examples=50)
def test_tracedcontrolnodeactivation_instantiation(instance):
    assert isinstance(instance, TracedControlNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedactivityfinalnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedForkNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedforknodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedForkNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedInitialNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedinitialnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedInitialNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedJoinNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedjoinnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedJoinNodeActivation)

@given(instance=TracedToken_strategy)
@settings(max_examples=50)
def test_tracedtoken_instantiation(instance):
    assert isinstance(instance, TracedToken)

@given(instance=umlTrace_IntermediateActivities_TracedForkedToken_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedforkedtoken_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedForkedToken)

@given(instance=umlTrace_IntermediateActivities_TracedDecisionNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_traceddecisionnodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedDecisionNodeActivation)

@given(instance=umlTrace_IntermediateActivities_TracedObjectToken_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedobjecttoken_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedObjectToken)

@given(instance=umlTrace_IntermediateActivities_TracedControlToken_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedcontroltoken_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedControlToken)

@given(instance=umlTrace_IntermediateActivities_TracedMergeNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedmergenodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedMergeNodeActivation)

@given(instance=TracedCompoundValue_strategy)
@settings(max_examples=50)
def test_tracedcompoundvalue_instantiation(instance):
    assert isinstance(instance, TracedCompoundValue)

@given(instance=umlTrace_Kernel_TracedExtensionalValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedextensionalvalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedExtensionalValue)

@given(instance=umlTrace_Kernel_TracedFeatureValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedfeaturevalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedFeatureValue)

@given(instance=TracedObject_strategy)
@settings(max_examples=50)
def test_tracedobject_instantiation(instance):
    assert isinstance(instance, TracedObject)

@given(instance=umlTrace_BasicBehaviors_TracedExecution_strategy)
@settings(max_examples=50)
def test_umltrace_basicbehaviors_tracedexecution_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicBehaviors_TracedExecution)

@given(instance=umlTrace_BasicBehaviors_TracedParameterValue_strategy)
@settings(max_examples=50)
def test_umltrace_basicbehaviors_tracedparametervalue_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicBehaviors_TracedParameterValue)

@given(instance=TracedExecution_strategy)
@settings(max_examples=50)
def test_tracedexecution_instantiation(instance):
    assert isinstance(instance, TracedExecution)

@given(instance=umlTrace_IntermediateActivities_TracedActivityExecution_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedactivityexecution_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedActivityExecution)

@given(instance=umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution_strategy)
@settings(max_examples=50)
def test_umltrace_basicbehaviors_tracedopaquebehaviorexecution_instantiation(instance):
    assert isinstance(instance, umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution)

@given(instance=TracedValue_strategy)
@settings(max_examples=50)
def test_tracedvalue_instantiation(instance):
    assert isinstance(instance, TracedValue)

@given(instance=umlTrace_Kernel_TracedPrimitiveValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedprimitivevalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedPrimitiveValue)

@given(instance=TracedSemanticVisitor_strategy)
@settings(max_examples=50)
def test_tracedsemanticvisitor_instantiation(instance):
    assert isinstance(instance, TracedSemanticVisitor)

@given(instance=umlTrace_IntermediateActivities_TracedActivityNodeActivation_strategy)
@settings(max_examples=50)
def test_umltrace_intermediateactivities_tracedactivitynodeactivation_instantiation(instance):
    assert isinstance(instance, umlTrace_IntermediateActivities_TracedActivityNodeActivation)

@given(instance=umlTrace_Kernel_TracedValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedvalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedValue)

@given(instance=TracedEvaluation_strategy)
@settings(max_examples=50)
def test_tracedevaluation_instantiation(instance):
    assert isinstance(instance, TracedEvaluation)

@given(instance=umlTrace_Kernel_TracedLiteralEvaluation_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedliteralevaluation_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedLiteralEvaluation)

@given(instance=TracedPrimitiveValue_strategy)
@settings(max_examples=50)
def test_tracedprimitivevalue_instantiation(instance):
    assert isinstance(instance, TracedPrimitiveValue)

@given(instance=umlTrace_Kernel_TracedIntegerValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedintegervalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedIntegerValue)

@given(instance=TracedStructuredValue_strategy)
@settings(max_examples=50)
def test_tracedstructuredvalue_instantiation(instance):
    assert isinstance(instance, TracedStructuredValue)

@given(instance=umlTrace_Kernel_TracedCompoundValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedcompoundvalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedCompoundValue)

@given(instance=umlTrace_Kernel_TracedReference_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedreference_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedReference)

@given(instance=umlTrace_Kernel_TracedStructuredValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedstructuredvalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedStructuredValue)

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

@given(instance=umlTrace_Kernel_TracedBooleanValue_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedbooleanvalue_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedBooleanValue)

@given(instance=umlTrace_Kernel_TracedEvaluation_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedevaluation_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedEvaluation)

@given(instance=uml_TracedBehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedbehaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml_TracedBehaviorExecutionSpecification)

@given(instance=uml_TracedActor_strategy)
@settings(max_examples=50)
def test_uml_tracedactor_instantiation(instance):
    assert isinstance(instance, uml_TracedActor)

@given(instance=uml_TracedDeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml_traceddeploymentspecification_instantiation(instance):
    assert isinstance(instance, uml_TracedDeploymentSpecification)

@given(instance=TracedExtensionalValue_strategy)
@settings(max_examples=50)
def test_tracedextensionalvalue_instantiation(instance):
    assert isinstance(instance, TracedExtensionalValue)

@given(instance=umlTrace_Kernel_TracedObject_strategy)
@settings(max_examples=50)
def test_umltrace_kernel_tracedobject_instantiation(instance):
    assert isinstance(instance, umlTrace_Kernel_TracedObject)

@given(instance=uml_TracedCentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml_tracedcentralbuffernode_instantiation(instance):
    assert isinstance(instance, uml_TracedCentralBufferNode)

@given(instance=uml_TracedUnmarshallAction_strategy)
@settings(max_examples=50)
def test_uml_tracedunmarshallaction_instantiation(instance):
    assert isinstance(instance, uml_TracedUnmarshallAction)

@given(instance=Kernel_TracedLiteralIntegerEvaluation_strategy)
@settings(max_examples=50)
def test_kernel_tracedliteralintegerevaluation_instantiation(instance):
    assert isinstance(instance, Kernel_TracedLiteralIntegerEvaluation)

@given(instance=uml_TracedClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml_tracedclearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml_TracedClearStructuralFeatureAction)

@given(instance=uml_TracedFunctionBehavior_strategy)
@settings(max_examples=50)
def test_uml_tracedfunctionbehavior_instantiation(instance):
    assert isinstance(instance, uml_TracedFunctionBehavior)

@given(instance=uml_TracedOpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml_tracedopaqueexpression_instantiation(instance):
    assert isinstance(instance, uml_TracedOpaqueExpression)

@given(instance=uml_TracedTemplateBinding_strategy)
@settings(max_examples=50)
def test_uml_tracedtemplatebinding_instantiation(instance):
    assert isinstance(instance, uml_TracedTemplateBinding)

@given(instance=uml_TracedLinkEndCreationData_strategy)
@settings(max_examples=50)
def test_uml_tracedlinkendcreationdata_instantiation(instance):
    assert isinstance(instance, uml_TracedLinkEndCreationData)

@given(instance=uml_TracedActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedactionexecutionspecification_instantiation(instance):
    assert isinstance(instance, uml_TracedActionExecutionSpecification)

@given(instance=uml_TracedConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml_tracedconnectionpointreference_instantiation(instance):
    assert isinstance(instance, uml_TracedConnectionPointReference)

@given(instance=uml_TracedActivity_strategy)
@settings(max_examples=50)
def test_uml_tracedactivity_instantiation(instance):
    assert isinstance(instance, uml_TracedActivity)

@given(instance=uml_TracedAcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml_tracedacceptcallaction_instantiation(instance):
    assert isinstance(instance, uml_TracedAcceptCallAction)

@given(instance=uml_TracedReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadselfaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadSelfAction)

@given(instance=uml_TracedGate_strategy)
@settings(max_examples=50)
def test_uml_tracedgate_instantiation(instance):
    assert isinstance(instance, uml_TracedGate)

@given(instance=uml_TracedSubstitution_strategy)
@settings(max_examples=50)
def test_uml_tracedsubstitution_instantiation(instance):
    assert isinstance(instance, uml_TracedSubstitution)

@given(instance=uml_TracedDevice_strategy)
@settings(max_examples=50)
def test_uml_traceddevice_instantiation(instance):
    assert isinstance(instance, uml_TracedDevice)

@given(instance=uml_TracedReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReclassifyObjectAction)

@given(instance=uml_TracedCallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml_tracedcallbehavioraction_instantiation(instance):
    assert isinstance(instance, uml_TracedCallBehaviorAction)

@given(instance=uml_TracedGeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml_tracedgeneralordering_instantiation(instance):
    assert isinstance(instance, uml_TracedGeneralOrdering)

@given(instance=uml_TracedStateInvariant_strategy)
@settings(max_examples=50)
def test_uml_tracedstateinvariant_instantiation(instance):
    assert isinstance(instance, uml_TracedStateInvariant)

@given(instance=uml_TracedAssociation_strategy)
@settings(max_examples=50)
def test_uml_tracedassociation_instantiation(instance):
    assert isinstance(instance, uml_TracedAssociation)

@given(instance=uml_TracedInteractionUse_strategy)
@settings(max_examples=50)
def test_uml_tracedinteractionuse_instantiation(instance):
    assert isinstance(instance, uml_TracedInteractionUse)

@given(instance=uml_TracedVariable_strategy)
@settings(max_examples=50)
def test_uml_tracedvariable_instantiation(instance):
    assert isinstance(instance, uml_TracedVariable)

@given(instance=uml_TracedRemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml_tracedremovevariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml_TracedRemoveVariableValueAction)

@given(instance=uml_TracedLiteralReal_strategy)
@settings(max_examples=50)
def test_uml_tracedliteralreal_instantiation(instance):
    assert isinstance(instance, uml_TracedLiteralReal)

@given(instance=uml_TracedExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedexecutionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml_TracedExecutionOccurrenceSpecification)

@given(instance=uml_TracedPackageImport_strategy)
@settings(max_examples=50)
def test_uml_tracedpackageimport_instantiation(instance):
    assert isinstance(instance, uml_TracedPackageImport)

@given(instance=uml_TracedExceptionHandler_strategy)
@settings(max_examples=50)
def test_uml_tracedexceptionhandler_instantiation(instance):
    assert isinstance(instance, uml_TracedExceptionHandler)

@given(instance=uml_TracedTestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml_tracedtestidentityaction_instantiation(instance):
    assert isinstance(instance, uml_TracedTestIdentityAction)

@given(instance=uml_TracedClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml_tracedclearassociationaction_instantiation(instance):
    assert isinstance(instance, uml_TracedClearAssociationAction)

@given(instance=uml_TracedAddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml_tracedaddvariablevalueaction_instantiation(instance):
    assert isinstance(instance, uml_TracedAddVariableValueAction)

@given(instance=uml_TracedOperation_strategy)
@settings(max_examples=50)
def test_uml_tracedoperation_instantiation(instance):
    assert isinstance(instance, uml_TracedOperation)

@given(instance=uml_TracedControlFlow_strategy)
@settings(max_examples=50)
def test_uml_tracedcontrolflow_instantiation(instance):
    assert isinstance(instance, uml_TracedControlFlow)

@given(instance=uml_TracedExpansionNode_strategy)
@settings(max_examples=50)
def test_uml_tracedexpansionnode_instantiation(instance):
    assert isinstance(instance, uml_TracedExpansionNode)

@given(instance=uml_TracedLiteralNull_strategy)
@settings(max_examples=50)
def test_uml_tracedliteralnull_instantiation(instance):
    assert isinstance(instance, uml_TracedLiteralNull)

@given(instance=uml_TracedComment_strategy)
@settings(max_examples=50)
def test_uml_tracedcomment_instantiation(instance):
    assert isinstance(instance, uml_TracedComment)

@given(instance=uml_TracedSignal_strategy)
@settings(max_examples=50)
def test_uml_tracedsignal_instantiation(instance):
    assert isinstance(instance, uml_TracedSignal)

@given(instance=uml_TracedRaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml_tracedraiseexceptionaction_instantiation(instance):
    assert isinstance(instance, uml_TracedRaiseExceptionAction)

@given(instance=uml_TracedReception_strategy)
@settings(max_examples=50)
def test_uml_tracedreception_instantiation(instance):
    assert isinstance(instance, uml_TracedReception)

@given(instance=uml_TracedForkNode_strategy)
@settings(max_examples=50)
def test_uml_tracedforknode_instantiation(instance):
    assert isinstance(instance, uml_TracedForkNode)

@given(instance=uml_TracedModel_strategy)
@settings(max_examples=50)
def test_uml_tracedmodel_instantiation(instance):
    assert isinstance(instance, uml_TracedModel)

@given(instance=uml_TracedPackageMerge_strategy)
@settings(max_examples=50)
def test_uml_tracedpackagemerge_instantiation(instance):
    assert isinstance(instance, uml_TracedPackageMerge)

@given(instance=uml_TracedNode_strategy)
@settings(max_examples=50)
def test_uml_tracednode_instantiation(instance):
    assert isinstance(instance, uml_TracedNode)

@given(instance=uml_TracedDestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml_traceddestroyobjectaction_instantiation(instance):
    assert isinstance(instance, uml_TracedDestroyObjectAction)

@given(instance=uml_TracedChangeEvent_strategy)
@settings(max_examples=50)
def test_uml_tracedchangeevent_instantiation(instance):
    assert isinstance(instance, uml_TracedChangeEvent)

@given(instance=uml_TracedObjectFlow_strategy)
@settings(max_examples=50)
def test_uml_tracedobjectflow_instantiation(instance):
    assert isinstance(instance, uml_TracedObjectFlow)

@given(instance=BasicActions_TracedInputPinActivation_strategy)
@settings(max_examples=50)
def test_basicactions_tracedinputpinactivation_instantiation(instance):
    assert isinstance(instance, BasicActions_TracedInputPinActivation)

@given(instance=uml_TracedReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadextentaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadExtentAction)

@given(instance=uml_TracedManifestation_strategy)
@settings(max_examples=50)
def test_uml_tracedmanifestation_instantiation(instance):
    assert isinstance(instance, uml_TracedManifestation)

@given(instance=uml_TracedLinkEndData_strategy)
@settings(max_examples=50)
def test_uml_tracedlinkenddata_instantiation(instance):
    assert isinstance(instance, uml_TracedLinkEndData)

@given(instance=uml_TracedTransition_strategy)
@settings(max_examples=50)
def test_uml_tracedtransition_instantiation(instance):
    assert isinstance(instance, uml_TracedTransition)

@given(instance=uml_TracedInstanceValue_strategy)
@settings(max_examples=50)
def test_uml_tracedinstancevalue_instantiation(instance):
    assert isinstance(instance, uml_TracedInstanceValue)

@given(instance=uml_TracedClause_strategy)
@settings(max_examples=50)
def test_uml_tracedclause_instantiation(instance):
    assert isinstance(instance, uml_TracedClause)

@given(instance=uml_TracedCombinedFragment_strategy)
@settings(max_examples=50)
def test_uml_tracedcombinedfragment_instantiation(instance):
    assert isinstance(instance, uml_TracedCombinedFragment)

@given(instance=IntermediateActions_TracedCreateObjectActionActivation_strategy)
@settings(max_examples=50)
def test_intermediateactions_tracedcreateobjectactionactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActions_TracedCreateObjectActionActivation)

@given(instance=uml_TracedReplyAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreplyaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReplyAction)

@given(instance=uml_TracedTimeExpression_strategy)
@settings(max_examples=50)
def test_uml_tracedtimeexpression_instantiation(instance):
    assert isinstance(instance, uml_TracedTimeExpression)

@given(instance=uml_TracedDependency_strategy)
@settings(max_examples=50)
def test_uml_traceddependency_instantiation(instance):
    assert isinstance(instance, uml_TracedDependency)

@given(instance=uml_TracedInformationFlow_strategy)
@settings(max_examples=50)
def test_uml_tracedinformationflow_instantiation(instance):
    assert isinstance(instance, uml_TracedInformationFlow)

@given(instance=uml_TracedInteractionOperand_strategy)
@settings(max_examples=50)
def test_uml_tracedinteractionoperand_instantiation(instance):
    assert isinstance(instance, uml_TracedInteractionOperand)

@given(instance=IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_integerfunctions_tracedintegerplusfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution)

@given(instance=uml_TracedFinalState_strategy)
@settings(max_examples=50)
def test_uml_tracedfinalstate_instantiation(instance):
    assert isinstance(instance, uml_TracedFinalState)

@given(instance=uml_TracedUseCase_strategy)
@settings(max_examples=50)
def test_uml_tracedusecase_instantiation(instance):
    assert isinstance(instance, uml_TracedUseCase)

@given(instance=uml_TracedPseudostate_strategy)
@settings(max_examples=50)
def test_uml_tracedpseudostate_instantiation(instance):
    assert isinstance(instance, uml_TracedPseudostate)

@given(instance=uml_TracedRegion_strategy)
@settings(max_examples=50)
def test_uml_tracedregion_instantiation(instance):
    assert isinstance(instance, uml_TracedRegion)

@given(instance=uml_TracedValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_uml_tracedvaluespecificationaction_instantiation(instance):
    assert isinstance(instance, uml_TracedValueSpecificationAction)

@given(instance=uml_TracedDecisionNode_strategy)
@settings(max_examples=50)
def test_uml_traceddecisionnode_instantiation(instance):
    assert isinstance(instance, uml_TracedDecisionNode)

@given(instance=IntermediateActivities_TracedActivityParameterNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedactivityparameternodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedActivityParameterNodeActivation)

@given(instance=uml_TracedDestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml_traceddestroylinkaction_instantiation(instance):
    assert isinstance(instance, uml_TracedDestroyLinkAction)

@given(instance=uml_TracedInterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_uml_tracedinterruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, uml_TracedInterruptibleActivityRegion)

@given(instance=uml_TracedReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadIsClassifiedObjectAction)

@given(instance=IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_integerfunctions_tracedintegergreaterfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution)

@given(instance=uml_TracedValuePin_strategy)
@settings(max_examples=50)
def test_uml_tracedvaluepin_instantiation(instance):
    assert isinstance(instance, uml_TracedValuePin)

@given(instance=uml_TracedInstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedinstancespecification_instantiation(instance):
    assert isinstance(instance, uml_TracedInstanceSpecification)

@given(instance=uml_TracedOutputPin_strategy)
@settings(max_examples=50)
def test_uml_tracedoutputpin_instantiation(instance):
    assert isinstance(instance, uml_TracedOutputPin)

@given(instance=uml_TracedProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml_tracedprotocolstatemachine_instantiation(instance):
    assert isinstance(instance, uml_TracedProtocolStateMachine)

@given(instance=IntermediateActivities_TracedForkNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedforknodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedForkNodeActivation)

@given(instance=uml_TracedInterval_strategy)
@settings(max_examples=50)
def test_uml_tracedinterval_instantiation(instance):
    assert isinstance(instance, uml_TracedInterval)

@given(instance=uml_TracedProfile_strategy)
@settings(max_examples=50)
def test_uml_tracedprofile_instantiation(instance):
    assert isinstance(instance, uml_TracedProfile)

@given(instance=uml_TracedCallOperationAction_strategy)
@settings(max_examples=50)
def test_uml_tracedcalloperationaction_instantiation(instance):
    assert isinstance(instance, uml_TracedCallOperationAction)

@given(instance=uml_TracedTrigger_strategy)
@settings(max_examples=50)
def test_uml_tracedtrigger_instantiation(instance):
    assert isinstance(instance, uml_TracedTrigger)

@given(instance=uml_TracedIntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml_tracedintervalconstraint_instantiation(instance):
    assert isinstance(instance, uml_TracedIntervalConstraint)

@given(instance=uml_TracedImage_strategy)
@settings(max_examples=50)
def test_uml_tracedimage_instantiation(instance):
    assert isinstance(instance, uml_TracedImage)

@given(instance=uml_TracedDurationConstraint_strategy)
@settings(max_examples=50)
def test_uml_traceddurationconstraint_instantiation(instance):
    assert isinstance(instance, uml_TracedDurationConstraint)

@given(instance=uml_TracedMessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedmessageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml_TracedMessageOccurrenceSpecification)

@given(instance=uml_TracedConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml_tracedconnectorend_instantiation(instance):
    assert isinstance(instance, uml_TracedConnectorEnd)

@given(instance=uml_TracedTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_tracedtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml_TracedTemplateParameter)

@given(instance=uml_TracedActionInputPin_strategy)
@settings(max_examples=50)
def test_uml_tracedactioninputpin_instantiation(instance):
    assert isinstance(instance, uml_TracedActionInputPin)

@given(instance=uml_TracedClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml_tracedclearvariableaction_instantiation(instance):
    assert isinstance(instance, uml_TracedClearVariableAction)

@given(instance=uml_TracedLiteralInteger_strategy)
@settings(max_examples=50)
def test_uml_tracedliteralinteger_instantiation(instance):
    assert isinstance(instance, uml_TracedLiteralInteger)

@given(instance=uml_TracedInitialNode_strategy)
@settings(max_examples=50)
def test_uml_tracedinitialnode_instantiation(instance):
    assert isinstance(instance, uml_TracedInitialNode)

@given(instance=uml_TracedProfileApplication_strategy)
@settings(max_examples=50)
def test_uml_tracedprofileapplication_instantiation(instance):
    assert isinstance(instance, uml_TracedProfileApplication)

@given(instance=IntermediateActivities_TracedDecisionNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_traceddecisionnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedDecisionNodeActivation)

@given(instance=uml_TracedReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadvariableaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadVariableAction)

@given(instance=uml_TracedExtend_strategy)
@settings(max_examples=50)
def test_uml_tracedextend_instantiation(instance):
    assert isinstance(instance, uml_TracedExtend)

@given(instance=uml_TracedTemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_uml_tracedtemplateparametersubstitution_instantiation(instance):
    assert isinstance(instance, uml_TracedTemplateParameterSubstitution)

@given(instance=uml_TracedReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadLinkObjectEndQualifierAction)

@given(instance=uml_TracedOperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml_tracedoperationtemplateparameter_instantiation(instance):
    assert isinstance(instance, uml_TracedOperationTemplateParameter)

@given(instance=uml_TracedQualifierValue_strategy)
@settings(max_examples=50)
def test_uml_tracedqualifiervalue_instantiation(instance):
    assert isinstance(instance, uml_TracedQualifierValue)

@given(instance=uml_TracedLiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml_tracedliteralboolean_instantiation(instance):
    assert isinstance(instance, uml_TracedLiteralBoolean)

@given(instance=uml_TracedMessage_strategy)
@settings(max_examples=50)
def test_uml_tracedmessage_instantiation(instance):
    assert isinstance(instance, uml_TracedMessage)

@given(instance=uml_TracedRedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml_tracedredefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, uml_TracedRedefinableTemplateSignature)

@given(instance=uml_TracedMergeNode_strategy)
@settings(max_examples=50)
def test_uml_tracedmergenode_instantiation(instance):
    assert isinstance(instance, uml_TracedMergeNode)

@given(instance=uml_TracedReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadStructuralFeatureAction)

@given(instance=Kernel_TracedLiteralBooleanEvaluation_strategy)
@settings(max_examples=50)
def test_kernel_tracedliteralbooleanevaluation_instantiation(instance):
    assert isinstance(instance, Kernel_TracedLiteralBooleanEvaluation)

@given(instance=BasicActions_TracedOpaqueActionActivation_strategy)
@settings(max_examples=50)
def test_basicactions_tracedopaqueactionactivation_instantiation(instance):
    assert isinstance(instance, BasicActions_TracedOpaqueActionActivation)

@given(instance=uml_TracedPartDecomposition_strategy)
@settings(max_examples=50)
def test_uml_tracedpartdecomposition_instantiation(instance):
    assert isinstance(instance, uml_TracedPartDecomposition)

@given(instance=uml_TracedGeneralization_strategy)
@settings(max_examples=50)
def test_uml_tracedgeneralization_instantiation(instance):
    assert isinstance(instance, uml_TracedGeneralization)

@given(instance=uml_TracedCreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml_tracedcreatelinkaction_instantiation(instance):
    assert isinstance(instance, uml_TracedCreateLinkAction)

@given(instance=uml_TracedUsage_strategy)
@settings(max_examples=50)
def test_uml_tracedusage_instantiation(instance):
    assert isinstance(instance, uml_TracedUsage)

@given(instance=uml_TracedDuration_strategy)
@settings(max_examples=50)
def test_uml_tracedduration_instantiation(instance):
    assert isinstance(instance, uml_TracedDuration)

@given(instance=uml_TracedParameterSet_strategy)
@settings(max_examples=50)
def test_uml_tracedparameterset_instantiation(instance):
    assert isinstance(instance, uml_TracedParameterSet)

@given(instance=IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_strategy)
@settings(max_examples=50)
def test_integerfunctions_tracedintegerlessfunctionbehaviorexecution_instantiation(instance):
    assert isinstance(instance, IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution)

@given(instance=uml_TracedActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml_tracedactivityparameternode_instantiation(instance):
    assert isinstance(instance, uml_TracedActivityParameterNode)

@given(instance=uml_TracedAbstraction_strategy)
@settings(max_examples=50)
def test_uml_tracedabstraction_instantiation(instance):
    assert isinstance(instance, uml_TracedAbstraction)

@given(instance=uml_TracedStructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml_tracedstructuredactivitynode_instantiation(instance):
    assert isinstance(instance, uml_TracedStructuredActivityNode)

@given(instance=uml_TracedLiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml_tracedliteralunlimitednatural_instantiation(instance):
    assert isinstance(instance, uml_TracedLiteralUnlimitedNatural)

@given(instance=uml_TracedState_strategy)
@settings(max_examples=50)
def test_uml_tracedstate_instantiation(instance):
    assert isinstance(instance, uml_TracedState)

@given(instance=uml_TracedDestructionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_uml_traceddestructionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, uml_TracedDestructionOccurrenceSpecification)

@given(instance=uml_TracedInclude_strategy)
@settings(max_examples=50)
def test_uml_tracedinclude_instantiation(instance):
    assert isinstance(instance, uml_TracedInclude)

@given(instance=uml_TracedDurationInterval_strategy)
@settings(max_examples=50)
def test_uml_traceddurationinterval_instantiation(instance):
    assert isinstance(instance, uml_TracedDurationInterval)

@given(instance=uml_TracedCreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml_tracedcreateobjectaction_instantiation(instance):
    assert isinstance(instance, uml_TracedCreateObjectAction)

@given(instance=uml_TracedElementImport_strategy)
@settings(max_examples=50)
def test_uml_tracedelementimport_instantiation(instance):
    assert isinstance(instance, uml_TracedElementImport)

@given(instance=uml_TracedStartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml_tracedstartobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, uml_TracedStartObjectBehaviorAction)

@given(instance=BasicActions_TracedOutputPinActivation_strategy)
@settings(max_examples=50)
def test_basicactions_tracedoutputpinactivation_instantiation(instance):
    assert isinstance(instance, BasicActions_TracedOutputPinActivation)

@given(instance=IntermediateActions_TracedReadStructuralFeatureActionActivation_strategy)
@settings(max_examples=50)
def test_intermediateactions_tracedreadstructuralfeatureactionactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActions_TracedReadStructuralFeatureActionActivation)

@given(instance=uml_TracedStringExpression_strategy)
@settings(max_examples=50)
def test_uml_tracedstringexpression_instantiation(instance):
    assert isinstance(instance, uml_TracedStringExpression)

@given(instance=IntermediateActions_TracedValueSpecificationActionActivation_strategy)
@settings(max_examples=50)
def test_intermediateactions_tracedvaluespecificationactionactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActions_TracedValueSpecificationActionActivation)

@given(instance=uml_TracedAssociationClass_strategy)
@settings(max_examples=50)
def test_uml_tracedassociationclass_instantiation(instance):
    assert isinstance(instance, uml_TracedAssociationClass)

@given(instance=uml_TracedComponentRealization_strategy)
@settings(max_examples=50)
def test_uml_tracedcomponentrealization_instantiation(instance):
    assert isinstance(instance, uml_TracedComponentRealization)

@given(instance=uml_TracedInteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml_tracedinteractionconstraint_instantiation(instance):
    assert isinstance(instance, uml_TracedInteractionConstraint)

@given(instance=uml_TracedSequenceNode_strategy)
@settings(max_examples=50)
def test_uml_tracedsequencenode_instantiation(instance):
    assert isinstance(instance, uml_TracedSequenceNode)

@given(instance=uml_TracedInputPin_strategy)
@settings(max_examples=50)
def test_uml_tracedinputpin_instantiation(instance):
    assert isinstance(instance, uml_TracedInputPin)

@given(instance=uml_TracedReduceAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreduceaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReduceAction)

@given(instance=uml_TracedGeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml_tracedgeneralizationset_instantiation(instance):
    assert isinstance(instance, uml_TracedGeneralizationSet)

@given(instance=uml_TracedConstraint_strategy)
@settings(max_examples=50)
def test_uml_tracedconstraint_instantiation(instance):
    assert isinstance(instance, uml_TracedConstraint)

@given(instance=uml_TracedJoinNode_strategy)
@settings(max_examples=50)
def test_uml_tracedjoinnode_instantiation(instance):
    assert isinstance(instance, uml_TracedJoinNode)

@given(instance=uml_TracedExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml_tracedextensionpoint_instantiation(instance):
    assert isinstance(instance, uml_TracedExtensionPoint)

@given(instance=uml_TracedSignalEvent_strategy)
@settings(max_examples=50)
def test_uml_tracedsignalevent_instantiation(instance):
    assert isinstance(instance, uml_TracedSignalEvent)

@given(instance=uml_TracedSlot_strategy)
@settings(max_examples=50)
def test_uml_tracedslot_instantiation(instance):
    assert isinstance(instance, uml_TracedSlot)

@given(instance=uml_TracedTimeEvent_strategy)
@settings(max_examples=50)
def test_uml_tracedtimeevent_instantiation(instance):
    assert isinstance(instance, uml_TracedTimeEvent)

@given(instance=uml_TracedExtension_strategy)
@settings(max_examples=50)
def test_uml_tracedextension_instantiation(instance):
    assert isinstance(instance, uml_TracedExtension)

@given(instance=uml_TracedTimeInterval_strategy)
@settings(max_examples=50)
def test_uml_tracedtimeinterval_instantiation(instance):
    assert isinstance(instance, uml_TracedTimeInterval)

@given(instance=uml_TracedPort_strategy)
@settings(max_examples=50)
def test_uml_tracedport_instantiation(instance):
    assert isinstance(instance, uml_TracedPort)

@given(instance=uml_TracedDeployment_strategy)
@settings(max_examples=50)
def test_uml_traceddeployment_instantiation(instance):
    assert isinstance(instance, uml_TracedDeployment)

@given(instance=uml_TracedBroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml_tracedbroadcastsignalaction_instantiation(instance):
    assert isinstance(instance, uml_TracedBroadcastSignalAction)

@given(instance=uml_TracedTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml_tracedtemplatesignature_instantiation(instance):
    assert isinstance(instance, uml_TracedTemplateSignature)

@given(instance=umlTrace_uml_TracedRedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedredefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedRedefinableTemplateSignature)

@given(instance=uml_TracedCollaboration_strategy)
@settings(max_examples=50)
def test_uml_tracedcollaboration_instantiation(instance):
    assert isinstance(instance, uml_TracedCollaboration)

@given(instance=uml_TracedPackage_strategy)
@settings(max_examples=50)
def test_uml_tracedpackage_instantiation(instance):
    assert isinstance(instance, uml_TracedPackage)

@given(instance=IntermediateActivities_TracedActivityFinalNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedactivityfinalnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedActivityFinalNodeActivation)

@given(instance=uml_TracedProtocolTransition_strategy)
@settings(max_examples=50)
def test_uml_tracedprotocoltransition_instantiation(instance):
    assert isinstance(instance, uml_TracedProtocolTransition)

@given(instance=uml_TracedReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml_tracedreadlinkaction_instantiation(instance):
    assert isinstance(instance, uml_TracedReadLinkAction)

@given(instance=uml_TracedAddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml_tracedaddstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml_TracedAddStructuralFeatureValueAction)

@given(instance=ForkedToken_baseTokenIsWithdrawn_Value_strategy)
@settings(max_examples=50)
def test_forkedtoken_basetokeniswithdrawn_value_instantiation(instance):
    assert isinstance(instance, ForkedToken_baseTokenIsWithdrawn_Value)

@given(instance=ForkedToken_baseToken_Value_strategy)
@settings(max_examples=50)
def test_forkedtoken_basetoken_value_instantiation(instance):
    assert isinstance(instance, ForkedToken_baseToken_Value)

@given(instance=ForkedToken_remainingOffersCount_Value_strategy)
@settings(max_examples=50)
def test_forkedtoken_remainingofferscount_value_instantiation(instance):
    assert isinstance(instance, ForkedToken_remainingOffersCount_Value)

@given(instance=IntegerValue_value_IntegerValue_Value_strategy)
@settings(max_examples=50)
def test_integervalue_value_integervalue_value_instantiation(instance):
    assert isinstance(instance, IntegerValue_value_IntegerValue_Value)

@given(instance=Reference_referent_Value_strategy)
@settings(max_examples=50)
def test_reference_referent_value_instantiation(instance):
    assert isinstance(instance, Reference_referent_Value)

@given(instance=Object_types_Value_strategy)
@settings(max_examples=50)
def test_object_types_value_instantiation(instance):
    assert isinstance(instance, Object_types_Value)

@given(instance=BigStep_strategy)
@settings(max_examples=50)
def test_bigstep_instantiation(instance):
    assert isinstance(instance, BigStep)

@given(instance=SmallStep_strategy)
@settings(max_examples=50)
def test_smallstep_instantiation(instance):
    assert isinstance(instance, SmallStep)

@given(instance=SemanticVisitor_runtimeModelElement_Value_strategy)
@settings(max_examples=50)
def test_semanticvisitor_runtimemodelelement_value_instantiation(instance):
    assert isinstance(instance, SemanticVisitor_runtimeModelElement_Value)

@given(instance=ObjectNodeActivation_offeredTokenCount_Value_strategy)
@settings(max_examples=50)
def test_objectnodeactivation_offeredtokencount_value_instantiation(instance):
    assert isinstance(instance, ObjectNodeActivation_offeredTokenCount_Value)

@given(instance=Locus_executor_Value_strategy)
@settings(max_examples=50)
def test_locus_executor_value_instantiation(instance):
    assert isinstance(instance, Locus_executor_Value)

@given(instance=Locus_extensionalValues_Value_strategy)
@settings(max_examples=50)
def test_locus_extensionalvalues_value_instantiation(instance):
    assert isinstance(instance, Locus_extensionalValues_Value)

@given(instance=Locus_factory_Value_strategy)
@settings(max_examples=50)
def test_locus_factory_value_instantiation(instance):
    assert isinstance(instance, Locus_factory_Value)

@given(instance=TracedObjects_strategy)
@settings(max_examples=50)
def test_tracedobjects_instantiation(instance):
    assert isinstance(instance, TracedObjects)

@given(instance=Steps_strategy)
@settings(max_examples=50)
def test_steps_instantiation(instance):
    assert isinstance(instance, Steps)

@given(instance=umlTrace_State_strategy)
@settings(max_examples=50)
def test_umltrace_state_instantiation(instance):
    assert isinstance(instance, umlTrace_State)

@given(instance=umlTrace_Trace_strategy)
@settings(max_examples=50)
def test_umltrace_trace_instantiation(instance):
    assert isinstance(instance, umlTrace_Trace)

@given(instance=uml_TracedEnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml_tracedenumerationliteral_instantiation(instance):
    assert isinstance(instance, uml_TracedEnumerationLiteral)

@given(instance=uml_TracedAcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml_tracedaccepteventaction_instantiation(instance):
    assert isinstance(instance, uml_TracedAcceptEventAction)

@given(instance=IntermediateActivities_TracedInitialNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedinitialnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedInitialNodeActivation)

@given(instance=uml_TracedDurationObservation_strategy)
@settings(max_examples=50)
def test_uml_traceddurationobservation_instantiation(instance):
    assert isinstance(instance, uml_TracedDurationObservation)

@given(instance=uml_TracedActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml_tracedactivityfinalnode_instantiation(instance):
    assert isinstance(instance, uml_TracedActivityFinalNode)

@given(instance=uml_TracedInterfaceRealization_strategy)
@settings(max_examples=50)
def test_uml_tracedinterfacerealization_instantiation(instance):
    assert isinstance(instance, uml_TracedInterfaceRealization)

@given(instance=uml_TracedTimeConstraint_strategy)
@settings(max_examples=50)
def test_uml_tracedtimeconstraint_instantiation(instance):
    assert isinstance(instance, uml_TracedTimeConstraint)

@given(instance=IntermediateActivities_TracedJoinNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedjoinnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedJoinNodeActivation)

@given(instance=uml_TracedInformationItem_strategy)
@settings(max_examples=50)
def test_uml_tracedinformationitem_instantiation(instance):
    assert isinstance(instance, uml_TracedInformationItem)

@given(instance=uml_TracedFlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml_tracedflowfinalnode_instantiation(instance):
    assert isinstance(instance, uml_TracedFlowFinalNode)

@given(instance=uml_TracedDataStoreNode_strategy)
@settings(max_examples=50)
def test_uml_traceddatastorenode_instantiation(instance):
    assert isinstance(instance, uml_TracedDataStoreNode)

@given(instance=uml_TracedConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_uml_tracedconsiderignorefragment_instantiation(instance):
    assert isinstance(instance, uml_TracedConsiderIgnoreFragment)

@given(instance=uml_TracedExpression_strategy)
@settings(max_examples=50)
def test_uml_tracedexpression_instantiation(instance):
    assert isinstance(instance, uml_TracedExpression)

@given(instance=umlTrace_uml_TracedStringExpression_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedstringexpression_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedStringExpression)

@given(instance=uml_TracedSendSignalAction_strategy)
@settings(max_examples=50)
def test_uml_tracedsendsignalaction_instantiation(instance):
    assert isinstance(instance, uml_TracedSendSignalAction)

@given(instance=uml_TracedRemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml_tracedremovestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, uml_TracedRemoveStructuralFeatureValueAction)

@given(instance=uml_TracedContinuation_strategy)
@settings(max_examples=50)
def test_uml_tracedcontinuation_instantiation(instance):
    assert isinstance(instance, uml_TracedContinuation)

@given(instance=uml_TracedProperty_strategy)
@settings(max_examples=50)
def test_uml_tracedproperty_instantiation(instance):
    assert isinstance(instance, uml_TracedProperty)

@given(instance=uml_TracedCommunicationPath_strategy)
@settings(max_examples=50)
def test_uml_tracedcommunicationpath_instantiation(instance):
    assert isinstance(instance, uml_TracedCommunicationPath)

@given(instance=uml_TracedDataType_strategy)
@settings(max_examples=50)
def test_uml_traceddatatype_instantiation(instance):
    assert isinstance(instance, uml_TracedDataType)

@given(instance=uml_TracedOpaqueAction_strategy)
@settings(max_examples=50)
def test_uml_tracedopaqueaction_instantiation(instance):
    assert isinstance(instance, uml_TracedOpaqueAction)

@given(instance=uml_TracedConnector_strategy)
@settings(max_examples=50)
def test_uml_tracedconnector_instantiation(instance):
    assert isinstance(instance, uml_TracedConnector)

@given(instance=umlTrace_Traced_TracedObjects_strategy)
@settings(max_examples=50)
def test_umltrace_traced_tracedobjects_instantiation(instance):
    assert isinstance(instance, umlTrace_Traced_TracedObjects)

@given(instance=uml_TracedArtifact_strategy)
@settings(max_examples=50)
def test_uml_tracedartifact_instantiation(instance):
    assert isinstance(instance, uml_TracedArtifact)

@given(instance=uml_TracedOpaqueBehavior_strategy)
@settings(max_examples=50)
def test_uml_tracedopaquebehavior_instantiation(instance):
    assert isinstance(instance, uml_TracedOpaqueBehavior)

@given(instance=umlTrace_Values_ActivityExecution_activationGroup_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activityexecution_activationgroup_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityExecution_activationGroup_Value)

@given(instance=umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_extensionalvalue_locus_extensionalvalue_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value)

@given(instance=umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activitynodeactivation_group_activitynodeactivation_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value)

@given(instance=Loci_TracedExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_loci_tracedexecutionenvironment_instantiation(instance):
    assert isinstance(instance, Loci_TracedExecutionEnvironment)

@given(instance=umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_executionenvironment_locus_executionenvironment_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value)

@given(instance=umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activitynodeactivation_outgoingedges_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value)

@given(instance=umlTrace_Values_ActivityNodeActivation_isRunning_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activitynodeactivation_isrunning_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityNodeActivation_isRunning_Value)



@given(instance=umlTrace_Values_ActivityNodeActivation_isRunning_Value_strategy)
def test_umltrace_values_activitynodeactivation_isrunning_value_isRunning_setter(instance):
    original = instance.isRunning
    instance.isRunning = original
    assert instance.isRunning == original

@given(instance=umlTrace_Values_ActivityNodeActivation_incomingEdges_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activitynodeactivation_incomingedges_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityNodeActivation_incomingEdges_Value)

@given(instance=umlTrace_Values_ActivityNodeActivation_heldTokens_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activitynodeactivation_heldtokens_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityNodeActivation_heldTokens_Value)

@given(instance=umlTrace_Values_InputParameterValues_parameterValues_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_inputparametervalues_parametervalues_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_InputParameterValues_parameterValues_Value)

@given(instance=Input_TracedInputParameterValues_strategy)
@settings(max_examples=50)
def test_input_tracedinputparametervalues_instantiation(instance):
    assert isinstance(instance, Input_TracedInputParameterValues)

@given(instance=umlTrace_Values_InputParameterValues_name_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_inputparametervalues_name_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_InputParameterValues_name_Value)



@given(instance=umlTrace_Values_InputParameterValues_name_Value_strategy)
def test_umltrace_values_inputparametervalues_name_value_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlTrace_Values_ActivityNodeActivation_running_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activitynodeactivation_running_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityNodeActivation_running_Value)



@given(instance=umlTrace_Values_ActivityNodeActivation_running_Value_strategy)
def test_umltrace_values_activitynodeactivation_running_value_running_setter(instance):
    original = instance.running
    instance.running = original
    assert instance.running == original

@given(instance=uml_TracedActivityNode_strategy)
@settings(max_examples=50)
def test_uml_tracedactivitynode_instantiation(instance):
    assert isinstance(instance, uml_TracedActivityNode)

@given(instance=umlTrace_uml_TracedObjectNode_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedobjectnode_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedObjectNode)

@given(instance=umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activitynodeactivation_node_activitynodeactivation_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value)

@given(instance=uml_TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_uml_tracedactivityedge_instantiation(instance):
    assert isinstance(instance, uml_TracedActivityEdge)

@given(instance=umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activityedgeinstance_edge_activityedgeinstance_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value)

@given(instance=umlTrace_Values_ActivityEdgeInstance_target_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activityedgeinstance_target_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityEdgeInstance_target_Value)

@given(instance=umlTrace_Values_ActivityEdgeInstance_source_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activityedgeinstance_source_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityEdgeInstance_source_Value)

@given(instance=umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activityedgeinstance_group_activityedgeinstance_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value)

@given(instance=umlTrace_Values_PinActivation_count_temp_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_pinactivation_count_temp_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_PinActivation_count_temp_Value)



@given(instance=umlTrace_Values_PinActivation_count_temp_Value_strategy)
def test_umltrace_values_pinactivation_count_temp_value_count_temp_setter(instance):
    original = instance.count_temp
    instance.count_temp = original
    assert instance.count_temp == original

@given(instance=umlTrace_Values_ActivityEdgeInstance_offers_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activityedgeinstance_offers_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityEdgeInstance_offers_Value)

@given(instance=umlTrace_Values_FeatureValue_position_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_featurevalue_position_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_FeatureValue_position_Value)



@given(instance=umlTrace_Values_FeatureValue_position_Value_strategy)
def test_umltrace_values_featurevalue_position_value_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=uml_TracedStructuralFeature_strategy)
@settings(max_examples=50)
def test_uml_tracedstructuralfeature_instantiation(instance):
    assert isinstance(instance, uml_TracedStructuralFeature)

@given(instance=umlTrace_uml_TracedProperty_strategy)
@settings(max_examples=50)
def test_umltrace_uml_tracedproperty_instantiation(instance):
    assert isinstance(instance, umlTrace_uml_TracedProperty)

@given(instance=umlTrace_Values_FeatureValue_feature_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_featurevalue_feature_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_FeatureValue_feature_Value)

@given(instance=umlTrace_Values_FeatureValue_values_FeatureValue_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_featurevalue_values_featurevalue_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_FeatureValue_values_FeatureValue_Value)

@given(instance=umlTrace_Values_PinActivation_actionActivation_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_pinactivation_actionactivation_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_PinActivation_actionActivation_Value)

@given(instance=umlTrace_Values_Token_holder_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_token_holder_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Token_holder_Value)

@given(instance=Kernel_TracedCompoundValue_strategy)
@settings(max_examples=50)
def test_kernel_tracedcompoundvalue_instantiation(instance):
    assert isinstance(instance, Kernel_TracedCompoundValue)

@given(instance=Kernel_TracedFeatureValue_strategy)
@settings(max_examples=50)
def test_kernel_tracedfeaturevalue_instantiation(instance):
    assert isinstance(instance, Kernel_TracedFeatureValue)

@given(instance=umlTrace_Values_CompoundValue_featureValues_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_compoundvalue_featurevalues_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_CompoundValue_featureValues_Value)

@given(instance=BasicActions_TracedCallActionActivation_strategy)
@settings(max_examples=50)
def test_basicactions_tracedcallactionactivation_instantiation(instance):
    assert isinstance(instance, BasicActions_TracedCallActionActivation)

@given(instance=umlTrace_Values_CallActionActivation_callExecutions_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_callactionactivation_callexecutions_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_CallActionActivation_callExecutions_Value)

@given(instance=IntermediateActivities_TracedOffer_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedoffer_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedOffer)

@given(instance=umlTrace_Values_Offer_offeredTokens_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_offer_offeredtokens_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Offer_offeredTokens_Value)

@given(instance=Kernel_TracedBooleanValue_strategy)
@settings(max_examples=50)
def test_kernel_tracedbooleanvalue_instantiation(instance):
    assert isinstance(instance, Kernel_TracedBooleanValue)

@given(instance=umlTrace_Values_BooleanValue_value_BooleanValue_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_booleanvalue_value_booleanvalue_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_BooleanValue_value_BooleanValue_Value)



@given(instance=umlTrace_Values_BooleanValue_value_BooleanValue_Value_strategy)
def test_umltrace_values_booleanvalue_value_booleanvalue_value_value_BooleanValue_setter(instance):
    original = instance.value_BooleanValue
    instance.value_BooleanValue = original
    assert instance.value_BooleanValue == original

@given(instance=umlTrace_Values_Evaluation_locus_Evaluation_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_evaluation_locus_evaluation_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Evaluation_locus_Evaluation_Value)

@given(instance=Kernel_TracedEvaluation_strategy)
@settings(max_examples=50)
def test_kernel_tracedevaluation_instantiation(instance):
    assert isinstance(instance, Kernel_TracedEvaluation)

@given(instance=uml_TracedValueSpecification_strategy)
@settings(max_examples=50)
def test_uml_tracedvaluespecification_instantiation(instance):
    assert isinstance(instance, uml_TracedValueSpecification)

@given(instance=umlTrace_Values_Evaluation_specification_Evaluation_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_evaluation_specification_evaluation_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Evaluation_specification_Evaluation_Value)

@given(instance=IntermediateActivities_TracedObjectToken_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedobjecttoken_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedObjectToken)

@given(instance=umlTrace_Values_ObjectToken_value_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_objecttoken_value_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ObjectToken_value_Value)

@given(instance=umlTrace_Values_Executor_locus_Executor_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_executor_locus_executor_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Executor_locus_Executor_Value)

@given(instance=IntermediateActivities_TracedActivityEdgeInstance_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedactivityedgeinstance_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedActivityEdgeInstance)

@given(instance=umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activitynodeactivationgroup_edgeinstances_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value)

@given(instance=IntermediateActivities_TracedActivityExecution_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedactivityexecution_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedActivityExecution)

@given(instance=umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activitynodeactivationgroup_activityexecution_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value)

@given(instance=Kernel_TracedPrimitiveValue_strategy)
@settings(max_examples=50)
def test_kernel_tracedprimitivevalue_instantiation(instance):
    assert isinstance(instance, Kernel_TracedPrimitiveValue)

@given(instance=umlTrace_Values_PrimitiveValue_type_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_primitivevalue_type_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_PrimitiveValue_type_Value)

@given(instance=umlTrace_Values_Element_semanticVisitor_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_element_semanticvisitor_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Element_semanticVisitor_Value)

@given(instance=umlTrace_Values_Execution_context_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_execution_context_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Execution_context_Value)

@given(instance=BasicBehaviors_TracedExecution_strategy)
@settings(max_examples=50)
def test_basicbehaviors_tracedexecution_instantiation(instance):
    assert isinstance(instance, BasicBehaviors_TracedExecution)

@given(instance=IntermediateActivities_TracedActivityNodeActivationGroup_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedactivitynodeactivationgroup_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedActivityNodeActivationGroup)

@given(instance=IntermediateActivities_TracedActivityNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedactivitynodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedActivityNodeActivation)

@given(instance=umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_activitynodeactivationgroup_nodeactivations_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value)

@given(instance=BasicActions_TracedActionActivation_strategy)
@settings(max_examples=50)
def test_basicactions_tracedactionactivation_instantiation(instance):
    assert isinstance(instance, BasicActions_TracedActionActivation)

@given(instance=BasicActions_TracedPinActivation_strategy)
@settings(max_examples=50)
def test_basicactions_tracedpinactivation_instantiation(instance):
    assert isinstance(instance, BasicActions_TracedPinActivation)

@given(instance=umlTrace_Values_ActionActivation_pinActivations_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_actionactivation_pinactivations_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActionActivation_pinActivations_Value)

@given(instance=uml_TracedParameter_strategy)
@settings(max_examples=50)
def test_uml_tracedparameter_instantiation(instance):
    assert isinstance(instance, uml_TracedParameter)

@given(instance=umlTrace_Values_ParameterValue_parameter_ParameterValue_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_parametervalue_parameter_parametervalue_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ParameterValue_parameter_ParameterValue_Value)

@given(instance=BasicBehaviors_TracedParameterValue_strategy)
@settings(max_examples=50)
def test_basicbehaviors_tracedparametervalue_instantiation(instance):
    assert isinstance(instance, BasicBehaviors_TracedParameterValue)

@given(instance=Kernel_TracedValue_strategy)
@settings(max_examples=50)
def test_kernel_tracedvalue_instantiation(instance):
    assert isinstance(instance, Kernel_TracedValue)

@given(instance=umlTrace_Values_Execution_parameterValues_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_execution_parametervalues_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Execution_parameterValues_Value)

@given(instance=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_semanticvisitor_runtimemodelelement_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_SemanticVisitor_runtimeModelElement_Value)

@given(instance=umlTrace_Values_ActionActivation_firing_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_actionactivation_firing_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ActionActivation_firing_Value)



@given(instance=umlTrace_Values_ActionActivation_firing_Value_strategy)
def test_umltrace_values_actionactivation_firing_value_firing_setter(instance):
    original = instance.firing
    instance.firing = original
    assert instance.firing == original

@given(instance=IntermediateActivities_TracedObjectNodeActivation_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedobjectnodeactivation_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedObjectNodeActivation)

@given(instance=umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_objectnodeactivation_offeredtokencount_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value)



@given(instance=umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value_strategy)
def test_umltrace_values_objectnodeactivation_offeredtokencount_value_offeredTokenCount_setter(instance):
    original = instance.offeredTokenCount
    instance.offeredTokenCount = original
    assert instance.offeredTokenCount == original

@given(instance=Loci_TracedExecutor_strategy)
@settings(max_examples=50)
def test_loci_tracedexecutor_instantiation(instance):
    assert isinstance(instance, Loci_TracedExecutor)

@given(instance=umlTrace_Values_Locus_executor_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_locus_executor_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Locus_executor_Value)

@given(instance=umlTrace_Values_ParameterValue_values_ParameterValue_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_parametervalue_values_parametervalue_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ParameterValue_values_ParameterValue_Value)

@given(instance=Loci_TracedSemanticVisitor_strategy)
@settings(max_examples=50)
def test_loci_tracedsemanticvisitor_instantiation(instance):
    assert isinstance(instance, Loci_TracedSemanticVisitor)

@given(instance=uml_TracedElement_strategy)
@settings(max_examples=50)
def test_uml_tracedelement_instantiation(instance):
    assert isinstance(instance, uml_TracedElement)

@given(instance=Loci_TracedLocus_strategy)
@settings(max_examples=50)
def test_loci_tracedlocus_instantiation(instance):
    assert isinstance(instance, Loci_TracedLocus)

@given(instance=umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_executionfactory_locus_executionfactory_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value)

@given(instance=BasicBehaviors_TracedOpaqueBehaviorExecution_strategy)
@settings(max_examples=50)
def test_basicbehaviors_tracedopaquebehaviorexecution_instantiation(instance):
    assert isinstance(instance, BasicBehaviors_TracedOpaqueBehaviorExecution)

@given(instance=umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_executionfactory_primitivebehaviorprototypes_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value)

@given(instance=Loci_TracedExecutionFactory_strategy)
@settings(max_examples=50)
def test_loci_tracedexecutionfactory_instantiation(instance):
    assert isinstance(instance, Loci_TracedExecutionFactory)

@given(instance=uml_TracedPrimitiveType_strategy)
@settings(max_examples=50)
def test_uml_tracedprimitivetype_instantiation(instance):
    assert isinstance(instance, uml_TracedPrimitiveType)

@given(instance=umlTrace_Values_ExecutionFactory_builtInTypes_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_executionfactory_builtintypes_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ExecutionFactory_builtInTypes_Value)

@given(instance=Kernel_TracedExtensionalValue_strategy)
@settings(max_examples=50)
def test_kernel_tracedextensionalvalue_instantiation(instance):
    assert isinstance(instance, Kernel_TracedExtensionalValue)

@given(instance=umlTrace_Values_Locus_extensionalValues_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_locus_extensionalvalues_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Locus_extensionalValues_Value)

@given(instance=umlTrace_Values_Locus_factory_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_locus_factory_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Locus_factory_Value)

@given(instance=IntermediateActivities_TracedForkedToken_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedforkedtoken_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedForkedToken)

@given(instance=umlTrace_Values_ForkedToken_remainingOffersCount_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_forkedtoken_remainingofferscount_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ForkedToken_remainingOffersCount_Value)



@given(instance=umlTrace_Values_ForkedToken_remainingOffersCount_Value_strategy)
def test_umltrace_values_forkedtoken_remainingofferscount_value_remainingOffersCount_setter(instance):
    original = instance.remainingOffersCount
    instance.remainingOffersCount = original
    assert instance.remainingOffersCount == original

@given(instance=Kernel_TracedIntegerValue_strategy)
@settings(max_examples=50)
def test_kernel_tracedintegervalue_instantiation(instance):
    assert isinstance(instance, Kernel_TracedIntegerValue)

@given(instance=umlTrace_Values_IntegerValue_value_IntegerValue_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_integervalue_value_integervalue_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_IntegerValue_value_IntegerValue_Value)



@given(instance=umlTrace_Values_IntegerValue_value_IntegerValue_Value_strategy)
def test_umltrace_values_integervalue_value_integervalue_value_value_IntegerValue_setter(instance):
    original = instance.value_IntegerValue
    instance.value_IntegerValue = original
    assert instance.value_IntegerValue == original

@given(instance=Kernel_TracedReference_strategy)
@settings(max_examples=50)
def test_kernel_tracedreference_instantiation(instance):
    assert isinstance(instance, Kernel_TracedReference)

@given(instance=umlTrace_Values_Reference_referent_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_reference_referent_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Reference_referent_Value)

@given(instance=umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_forkedtoken_basetokeniswithdrawn_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value)



@given(instance=umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value_strategy)
def test_umltrace_values_forkedtoken_basetokeniswithdrawn_value_baseTokenIsWithdrawn_setter(instance):
    original = instance.baseTokenIsWithdrawn
    instance.baseTokenIsWithdrawn = original
    assert instance.baseTokenIsWithdrawn == original

@given(instance=IntermediateActivities_TracedToken_strategy)
@settings(max_examples=50)
def test_intermediateactivities_tracedtoken_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_TracedToken)

@given(instance=umlTrace_Values_ForkedToken_baseToken_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_forkedtoken_basetoken_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_ForkedToken_baseToken_Value)

@given(instance=umlTrace_Steps_BigStep_strategy)
@settings(max_examples=50)
def test_umltrace_steps_bigstep_instantiation(instance):
    assert isinstance(instance, umlTrace_Steps_BigStep)

@given(instance=umlTrace_Steps_Steps_strategy)
@settings(max_examples=50)
def test_umltrace_steps_steps_instantiation(instance):
    assert isinstance(instance, umlTrace_Steps_Steps)

@given(instance=Steps_umlTrace_State_strategy)
@settings(max_examples=50)
def test_steps_umltrace_state_instantiation(instance):
    assert isinstance(instance, Steps_umlTrace_State)

@given(instance=umlTrace_Steps_SmallStep_strategy)
@settings(max_examples=50)
def test_umltrace_steps_smallstep_instantiation(instance):
    assert isinstance(instance, umlTrace_Steps_SmallStep)

@given(instance=ExecutionEnvironment_locus_ExecutionEnvironment_Value_strategy)
@settings(max_examples=50)
def test_executionenvironment_locus_executionenvironment_value_instantiation(instance):
    assert isinstance(instance, ExecutionEnvironment_locus_ExecutionEnvironment_Value)

@given(instance=ActivityExecution_activationGroup_Value_strategy)
@settings(max_examples=50)
def test_activityexecution_activationgroup_value_instantiation(instance):
    assert isinstance(instance, ActivityExecution_activationGroup_Value)

@given(instance=ExtensionalValue_locus_ExtensionalValue_Value_strategy)
@settings(max_examples=50)
def test_extensionalvalue_locus_extensionalvalue_value_instantiation(instance):
    assert isinstance(instance, ExtensionalValue_locus_ExtensionalValue_Value)

@given(instance=ActivityNodeActivation_group_ActivityNodeActivation_Value_strategy)
@settings(max_examples=50)
def test_activitynodeactivation_group_activitynodeactivation_value_instantiation(instance):
    assert isinstance(instance, ActivityNodeActivation_group_ActivityNodeActivation_Value)

@given(instance=ActivityNodeActivation_incomingEdges_Value_strategy)
@settings(max_examples=50)
def test_activitynodeactivation_incomingedges_value_instantiation(instance):
    assert isinstance(instance, ActivityNodeActivation_incomingEdges_Value)

@given(instance=ActivityNodeActivation_outgoingEdges_Value_strategy)
@settings(max_examples=50)
def test_activitynodeactivation_outgoingedges_value_instantiation(instance):
    assert isinstance(instance, ActivityNodeActivation_outgoingEdges_Value)

@given(instance=Values_umlTrace_State_strategy)
@settings(max_examples=50)
def test_values_umltrace_state_instantiation(instance):
    assert isinstance(instance, Values_umlTrace_State)

@given(instance=Kernel_TracedObject_strategy)
@settings(max_examples=50)
def test_kernel_tracedobject_instantiation(instance):
    assert isinstance(instance, Kernel_TracedObject)

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

@given(instance=umlTrace_Values_Object_types_Value_strategy)
@settings(max_examples=50)
def test_umltrace_values_object_types_value_instantiation(instance):
    assert isinstance(instance, umlTrace_Values_Object_types_Value)

@given(instance=ActivityNodeActivation_heldTokens_Value_strategy)
@settings(max_examples=50)
def test_activitynodeactivation_heldtokens_value_instantiation(instance):
    assert isinstance(instance, ActivityNodeActivation_heldTokens_Value)

@given(instance=InputParameterValues_parameterValues_Value_strategy)
@settings(max_examples=50)
def test_inputparametervalues_parametervalues_value_instantiation(instance):
    assert isinstance(instance, InputParameterValues_parameterValues_Value)

@given(instance=InputParameterValues_name_Value_strategy)
@settings(max_examples=50)
def test_inputparametervalues_name_value_instantiation(instance):
    assert isinstance(instance, InputParameterValues_name_Value)

@given(instance=ActivityEdgeInstance_source_Value_strategy)
@settings(max_examples=50)
def test_activityedgeinstance_source_value_instantiation(instance):
    assert isinstance(instance, ActivityEdgeInstance_source_Value)

@given(instance=ActivityEdgeInstance_edge_ActivityEdgeInstance_Value_strategy)
@settings(max_examples=50)
def test_activityedgeinstance_edge_activityedgeinstance_value_instantiation(instance):
    assert isinstance(instance, ActivityEdgeInstance_edge_ActivityEdgeInstance_Value)

@given(instance=ActivityEdgeInstance_target_Value_strategy)
@settings(max_examples=50)
def test_activityedgeinstance_target_value_instantiation(instance):
    assert isinstance(instance, ActivityEdgeInstance_target_Value)

@given(instance=ActivityEdgeInstance_offers_Value_strategy)
@settings(max_examples=50)
def test_activityedgeinstance_offers_value_instantiation(instance):
    assert isinstance(instance, ActivityEdgeInstance_offers_Value)

@given(instance=ActivityEdgeInstance_group_ActivityEdgeInstance_Value_strategy)
@settings(max_examples=50)
def test_activityedgeinstance_group_activityedgeinstance_value_instantiation(instance):
    assert isinstance(instance, ActivityEdgeInstance_group_ActivityEdgeInstance_Value)

@given(instance=PinActivation_count_temp_Value_strategy)
@settings(max_examples=50)
def test_pinactivation_count_temp_value_instantiation(instance):
    assert isinstance(instance, PinActivation_count_temp_Value)

@given(instance=ActivityNodeActivation_isRunning_Value_strategy)
@settings(max_examples=50)
def test_activitynodeactivation_isrunning_value_instantiation(instance):
    assert isinstance(instance, ActivityNodeActivation_isRunning_Value)

@given(instance=ActivityNodeActivation_running_Value_strategy)
@settings(max_examples=50)
def test_activitynodeactivation_running_value_instantiation(instance):
    assert isinstance(instance, ActivityNodeActivation_running_Value)

@given(instance=ActivityNodeActivation_node_ActivityNodeActivation_Value_strategy)
@settings(max_examples=50)
def test_activitynodeactivation_node_activitynodeactivation_value_instantiation(instance):
    assert isinstance(instance, ActivityNodeActivation_node_ActivityNodeActivation_Value)

@given(instance=FeatureValue_values_FeatureValue_Value_strategy)
@settings(max_examples=50)
def test_featurevalue_values_featurevalue_value_instantiation(instance):
    assert isinstance(instance, FeatureValue_values_FeatureValue_Value)

@given(instance=Offer_offeredTokens_Value_strategy)
@settings(max_examples=50)
def test_offer_offeredtokens_value_instantiation(instance):
    assert isinstance(instance, Offer_offeredTokens_Value)

@given(instance=Token_holder_Value_strategy)
@settings(max_examples=50)
def test_token_holder_value_instantiation(instance):
    assert isinstance(instance, Token_holder_Value)

@given(instance=CompoundValue_featureValues_Value_strategy)
@settings(max_examples=50)
def test_compoundvalue_featurevalues_value_instantiation(instance):
    assert isinstance(instance, CompoundValue_featureValues_Value)

@given(instance=CallActionActivation_callExecutions_Value_strategy)
@settings(max_examples=50)
def test_callactionactivation_callexecutions_value_instantiation(instance):
    assert isinstance(instance, CallActionActivation_callExecutions_Value)

@given(instance=ObjectToken_value_Value_strategy)
@settings(max_examples=50)
def test_objecttoken_value_value_instantiation(instance):
    assert isinstance(instance, ObjectToken_value_Value)

@given(instance=BooleanValue_value_BooleanValue_Value_strategy)
@settings(max_examples=50)
def test_booleanvalue_value_booleanvalue_value_instantiation(instance):
    assert isinstance(instance, BooleanValue_value_BooleanValue_Value)

@given(instance=Evaluation_locus_Evaluation_Value_strategy)
@settings(max_examples=50)
def test_evaluation_locus_evaluation_value_instantiation(instance):
    assert isinstance(instance, Evaluation_locus_Evaluation_Value)

@given(instance=Evaluation_specification_Evaluation_Value_strategy)
@settings(max_examples=50)
def test_evaluation_specification_evaluation_value_instantiation(instance):
    assert isinstance(instance, Evaluation_specification_Evaluation_Value)

@given(instance=PinActivation_actionActivation_Value_strategy)
@settings(max_examples=50)
def test_pinactivation_actionactivation_value_instantiation(instance):
    assert isinstance(instance, PinActivation_actionActivation_Value)

@given(instance=FeatureValue_position_Value_strategy)
@settings(max_examples=50)
def test_featurevalue_position_value_instantiation(instance):
    assert isinstance(instance, FeatureValue_position_Value)

@given(instance=FeatureValue_feature_Value_strategy)
@settings(max_examples=50)
def test_featurevalue_feature_value_instantiation(instance):
    assert isinstance(instance, FeatureValue_feature_Value)

@given(instance=ActivityNodeActivationGroup_nodeActivations_Value_strategy)
@settings(max_examples=50)
def test_activitynodeactivationgroup_nodeactivations_value_instantiation(instance):
    assert isinstance(instance, ActivityNodeActivationGroup_nodeActivations_Value)

@given(instance=Element_semanticVisitor_Value_strategy)
@settings(max_examples=50)
def test_element_semanticvisitor_value_instantiation(instance):
    assert isinstance(instance, Element_semanticVisitor_Value)

@given(instance=Execution_context_Value_strategy)
@settings(max_examples=50)
def test_execution_context_value_instantiation(instance):
    assert isinstance(instance, Execution_context_Value)

@given(instance=Execution_parameterValues_Value_strategy)
@settings(max_examples=50)
def test_execution_parametervalues_value_instantiation(instance):
    assert isinstance(instance, Execution_parameterValues_Value)

@given(instance=ActionActivation_firing_Value_strategy)
@settings(max_examples=50)
def test_actionactivation_firing_value_instantiation(instance):
    assert isinstance(instance, ActionActivation_firing_Value)

@given(instance=ActionActivation_pinActivations_Value_strategy)
@settings(max_examples=50)
def test_actionactivation_pinactivations_value_instantiation(instance):
    assert isinstance(instance, ActionActivation_pinActivations_Value)

@given(instance=ParameterValue_parameter_ParameterValue_Value_strategy)
@settings(max_examples=50)
def test_parametervalue_parameter_parametervalue_value_instantiation(instance):
    assert isinstance(instance, ParameterValue_parameter_ParameterValue_Value)

@given(instance=ParameterValue_values_ParameterValue_Value_strategy)
@settings(max_examples=50)
def test_parametervalue_values_parametervalue_value_instantiation(instance):
    assert isinstance(instance, ParameterValue_values_ParameterValue_Value)

@given(instance=PrimitiveValue_type_Value_strategy)
@settings(max_examples=50)
def test_primitivevalue_type_value_instantiation(instance):
    assert isinstance(instance, PrimitiveValue_type_Value)

@given(instance=Executor_locus_Executor_Value_strategy)
@settings(max_examples=50)
def test_executor_locus_executor_value_instantiation(instance):
    assert isinstance(instance, Executor_locus_Executor_Value)

@given(instance=ActivityNodeActivationGroup_edgeInstances_Value_strategy)
@settings(max_examples=50)
def test_activitynodeactivationgroup_edgeinstances_value_instantiation(instance):
    assert isinstance(instance, ActivityNodeActivationGroup_edgeInstances_Value)

@given(instance=ActivityNodeActivationGroup_activityExecution_Value_strategy)
@settings(max_examples=50)
def test_activitynodeactivationgroup_activityexecution_value_instantiation(instance):
    assert isinstance(instance, ActivityNodeActivationGroup_activityExecution_Value)

@given(instance=ExecutionFactory_locus_ExecutionFactory_Value_strategy)
@settings(max_examples=50)
def test_executionfactory_locus_executionfactory_value_instantiation(instance):
    assert isinstance(instance, ExecutionFactory_locus_ExecutionFactory_Value)

@given(instance=ExecutionFactory_primitiveBehaviorPrototypes_Value_strategy)
@settings(max_examples=50)
def test_executionfactory_primitivebehaviorprototypes_value_instantiation(instance):
    assert isinstance(instance, ExecutionFactory_primitiveBehaviorPrototypes_Value)

@given(instance=ExecutionFactory_builtInTypes_Value_strategy)
@settings(max_examples=50)
def test_executionfactory_builtintypes_value_instantiation(instance):
    assert isinstance(instance, ExecutionFactory_builtInTypes_Value)
