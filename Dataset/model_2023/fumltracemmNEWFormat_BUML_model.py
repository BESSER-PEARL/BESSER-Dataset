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
umlTrace_Trace = Class(name="umlTrace_Trace")
umlTrace_State = Class(name="umlTrace_State")
Steps = Class(name="Steps")
TracedObjects = Class(name="TracedObjects")
Locus_factory_Value = Class(name="Locus_factory_Value")
Locus_extensionalValues_Value = Class(name="Locus_extensionalValues_Value")
Locus_executor_Value = Class(name="Locus_executor_Value")
ObjectNodeActivation_offeredTokenCount_Value = Class(name="ObjectNodeActivation_offeredTokenCount_Value")
SemanticVisitor_runtimeModelElement_Value = Class(name="SemanticVisitor_runtimeModelElement_Value")
SmallStep = Class(name="SmallStep")
BigStep = Class(name="BigStep")
Object_types_Value = Class(name="Object_types_Value")
Reference_referent_Value = Class(name="Reference_referent_Value")
IntegerValue_value_IntegerValue_Value = Class(name="IntegerValue_value_IntegerValue_Value")
ForkedToken_remainingOffersCount_Value = Class(name="ForkedToken_remainingOffersCount_Value")
ForkedToken_baseToken_Value = Class(name="ForkedToken_baseToken_Value")
ForkedToken_baseTokenIsWithdrawn_Value = Class(name="ForkedToken_baseTokenIsWithdrawn_Value")
ExecutionFactory_builtInTypes_Value = Class(name="ExecutionFactory_builtInTypes_Value")
ExecutionFactory_primitiveBehaviorPrototypes_Value = Class(name="ExecutionFactory_primitiveBehaviorPrototypes_Value")
ExecutionFactory_locus_ExecutionFactory_Value = Class(name="ExecutionFactory_locus_ExecutionFactory_Value")
ActivityNodeActivationGroup_activityExecution_Value = Class(name="ActivityNodeActivationGroup_activityExecution_Value")
ActivityNodeActivationGroup_edgeInstances_Value = Class(name="ActivityNodeActivationGroup_edgeInstances_Value")
Executor_locus_Executor_Value = Class(name="Executor_locus_Executor_Value")
PrimitiveValue_type_Value = Class(name="PrimitiveValue_type_Value")
ParameterValue_values_ParameterValue_Value = Class(name="ParameterValue_values_ParameterValue_Value")
ParameterValue_parameter_ParameterValue_Value = Class(name="ParameterValue_parameter_ParameterValue_Value")
ActionActivation_pinActivations_Value = Class(name="ActionActivation_pinActivations_Value")
ActionActivation_firing_Value = Class(name="ActionActivation_firing_Value")
Execution_parameterValues_Value = Class(name="Execution_parameterValues_Value")
Execution_context_Value = Class(name="Execution_context_Value")
Element_semanticVisitor_Value = Class(name="Element_semanticVisitor_Value")
ActivityNodeActivationGroup_nodeActivations_Value = Class(name="ActivityNodeActivationGroup_nodeActivations_Value")
FeatureValue_feature_Value = Class(name="FeatureValue_feature_Value")
FeatureValue_position_Value = Class(name="FeatureValue_position_Value")
PinActivation_actionActivation_Value = Class(name="PinActivation_actionActivation_Value")
Evaluation_specification_Evaluation_Value = Class(name="Evaluation_specification_Evaluation_Value")
Evaluation_locus_Evaluation_Value = Class(name="Evaluation_locus_Evaluation_Value")
BooleanValue_value_BooleanValue_Value = Class(name="BooleanValue_value_BooleanValue_Value")
ObjectToken_value_Value = Class(name="ObjectToken_value_Value")
CallActionActivation_callExecutions_Value = Class(name="CallActionActivation_callExecutions_Value")
CompoundValue_featureValues_Value = Class(name="CompoundValue_featureValues_Value")
Token_holder_Value = Class(name="Token_holder_Value")
Offer_offeredTokens_Value = Class(name="Offer_offeredTokens_Value")
FeatureValue_values_FeatureValue_Value = Class(name="FeatureValue_values_FeatureValue_Value")
ActivityNodeActivation_node_ActivityNodeActivation_Value = Class(name="ActivityNodeActivation_node_ActivityNodeActivation_Value")
ActivityNodeActivation_running_Value = Class(name="ActivityNodeActivation_running_Value")
ActivityNodeActivation_isRunning_Value = Class(name="ActivityNodeActivation_isRunning_Value")
PinActivation_count_temp_Value = Class(name="PinActivation_count_temp_Value")
ActivityEdgeInstance_group_ActivityEdgeInstance_Value = Class(name="ActivityEdgeInstance_group_ActivityEdgeInstance_Value")
ActivityEdgeInstance_offers_Value = Class(name="ActivityEdgeInstance_offers_Value")
ActivityEdgeInstance_target_Value = Class(name="ActivityEdgeInstance_target_Value")
ActivityEdgeInstance_edge_ActivityEdgeInstance_Value = Class(name="ActivityEdgeInstance_edge_ActivityEdgeInstance_Value")
ActivityEdgeInstance_source_Value = Class(name="ActivityEdgeInstance_source_Value")
InputParameterValues_name_Value = Class(name="InputParameterValues_name_Value")
InputParameterValues_parameterValues_Value = Class(name="InputParameterValues_parameterValues_Value")
ActivityNodeActivation_heldTokens_Value = Class(name="ActivityNodeActivation_heldTokens_Value")
umlTrace_Values_Object_types_Value = Class(name="umlTrace_Values_Object_types_Value")
uml_TracedClass = Class(name="uml_TracedClass")
Kernel_TracedObject = Class(name="Kernel_TracedObject")
Values_umlTrace_State = Class(name="Values_umlTrace_State")
ActivityNodeActivation_outgoingEdges_Value = Class(name="ActivityNodeActivation_outgoingEdges_Value")
ActivityNodeActivation_incomingEdges_Value = Class(name="ActivityNodeActivation_incomingEdges_Value")
ActivityNodeActivation_group_ActivityNodeActivation_Value = Class(name="ActivityNodeActivation_group_ActivityNodeActivation_Value")
ExtensionalValue_locus_ExtensionalValue_Value = Class(name="ExtensionalValue_locus_ExtensionalValue_Value")
ActivityExecution_activationGroup_Value = Class(name="ActivityExecution_activationGroup_Value")
ExecutionEnvironment_locus_ExecutionEnvironment_Value = Class(name="ExecutionEnvironment_locus_ExecutionEnvironment_Value")
umlTrace_Steps_SmallStep = Class(name="umlTrace_Steps_SmallStep", is_abstract=True)
Steps_umlTrace_State = Class(name="Steps_umlTrace_State")
umlTrace_Steps_Steps = Class(name="umlTrace_Steps_Steps")
umlTrace_Steps_BigStep = Class(name="umlTrace_Steps_BigStep", is_abstract=True)
umlTrace_Values_ForkedToken_baseToken_Value = Class(name="umlTrace_Values_ForkedToken_baseToken_Value")
IntermediateActivities_TracedToken = Class(name="IntermediateActivities_TracedToken")
umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value = Class(name="umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value")
umlTrace_Values_Reference_referent_Value = Class(name="umlTrace_Values_Reference_referent_Value")
Kernel_TracedReference = Class(name="Kernel_TracedReference")
umlTrace_Values_IntegerValue_value_IntegerValue_Value = Class(name="umlTrace_Values_IntegerValue_value_IntegerValue_Value")
Kernel_TracedIntegerValue = Class(name="Kernel_TracedIntegerValue")
umlTrace_Values_ForkedToken_remainingOffersCount_Value = Class(name="umlTrace_Values_ForkedToken_remainingOffersCount_Value")
IntermediateActivities_TracedForkedToken = Class(name="IntermediateActivities_TracedForkedToken")
umlTrace_Values_Locus_factory_Value = Class(name="umlTrace_Values_Locus_factory_Value")
umlTrace_Values_Locus_extensionalValues_Value = Class(name="umlTrace_Values_Locus_extensionalValues_Value")
Kernel_TracedExtensionalValue = Class(name="Kernel_TracedExtensionalValue")
umlTrace_Values_ExecutionFactory_builtInTypes_Value = Class(name="umlTrace_Values_ExecutionFactory_builtInTypes_Value")
uml_TracedPrimitiveType = Class(name="uml_TracedPrimitiveType")
Loci_TracedExecutionFactory = Class(name="Loci_TracedExecutionFactory")
umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value = Class(name="umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value")
BasicBehaviors_TracedOpaqueBehaviorExecution = Class(name="BasicBehaviors_TracedOpaqueBehaviorExecution")
umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value = Class(name="umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value")
Loci_TracedLocus = Class(name="Loci_TracedLocus")
uml_TracedElement = Class(name="uml_TracedElement")
Loci_TracedSemanticVisitor = Class(name="Loci_TracedSemanticVisitor")
umlTrace_Values_ParameterValue_values_ParameterValue_Value = Class(name="umlTrace_Values_ParameterValue_values_ParameterValue_Value")
umlTrace_Values_Locus_executor_Value = Class(name="umlTrace_Values_Locus_executor_Value")
Loci_TracedExecutor = Class(name="Loci_TracedExecutor")
umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value = Class(name="umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value")
IntermediateActivities_TracedObjectNodeActivation = Class(name="IntermediateActivities_TracedObjectNodeActivation")
umlTrace_Values_ActionActivation_firing_Value = Class(name="umlTrace_Values_ActionActivation_firing_Value")
umlTrace_Values_SemanticVisitor_runtimeModelElement_Value = Class(name="umlTrace_Values_SemanticVisitor_runtimeModelElement_Value")
umlTrace_Values_Execution_parameterValues_Value = Class(name="umlTrace_Values_Execution_parameterValues_Value")
Kernel_TracedValue = Class(name="Kernel_TracedValue")
BasicBehaviors_TracedParameterValue = Class(name="BasicBehaviors_TracedParameterValue")
umlTrace_Values_ParameterValue_parameter_ParameterValue_Value = Class(name="umlTrace_Values_ParameterValue_parameter_ParameterValue_Value")
uml_TracedParameter = Class(name="uml_TracedParameter")
umlTrace_Values_ActionActivation_pinActivations_Value = Class(name="umlTrace_Values_ActionActivation_pinActivations_Value")
BasicActions_TracedPinActivation = Class(name="BasicActions_TracedPinActivation")
BasicActions_TracedActionActivation = Class(name="BasicActions_TracedActionActivation")
umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value = Class(name="umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value")
IntermediateActivities_TracedActivityNodeActivation = Class(name="IntermediateActivities_TracedActivityNodeActivation")
IntermediateActivities_TracedActivityNodeActivationGroup = Class(name="IntermediateActivities_TracedActivityNodeActivationGroup")
BasicBehaviors_TracedExecution = Class(name="BasicBehaviors_TracedExecution")
umlTrace_Values_Execution_context_Value = Class(name="umlTrace_Values_Execution_context_Value")
umlTrace_Values_Element_semanticVisitor_Value = Class(name="umlTrace_Values_Element_semanticVisitor_Value")
umlTrace_Values_PrimitiveValue_type_Value = Class(name="umlTrace_Values_PrimitiveValue_type_Value")
Kernel_TracedPrimitiveValue = Class(name="Kernel_TracedPrimitiveValue")
umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value = Class(name="umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value")
IntermediateActivities_TracedActivityExecution = Class(name="IntermediateActivities_TracedActivityExecution")
umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value = Class(name="umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value")
IntermediateActivities_TracedActivityEdgeInstance = Class(name="IntermediateActivities_TracedActivityEdgeInstance")
umlTrace_Values_Executor_locus_Executor_Value = Class(name="umlTrace_Values_Executor_locus_Executor_Value")
umlTrace_Values_ObjectToken_value_Value = Class(name="umlTrace_Values_ObjectToken_value_Value")
IntermediateActivities_TracedObjectToken = Class(name="IntermediateActivities_TracedObjectToken")
umlTrace_Values_Evaluation_specification_Evaluation_Value = Class(name="umlTrace_Values_Evaluation_specification_Evaluation_Value")
uml_TracedValueSpecification = Class(name="uml_TracedValueSpecification")
Kernel_TracedEvaluation = Class(name="Kernel_TracedEvaluation")
umlTrace_Values_Evaluation_locus_Evaluation_Value = Class(name="umlTrace_Values_Evaluation_locus_Evaluation_Value")
umlTrace_Values_BooleanValue_value_BooleanValue_Value = Class(name="umlTrace_Values_BooleanValue_value_BooleanValue_Value")
Kernel_TracedBooleanValue = Class(name="Kernel_TracedBooleanValue")
umlTrace_Values_Offer_offeredTokens_Value = Class(name="umlTrace_Values_Offer_offeredTokens_Value")
IntermediateActivities_TracedOffer = Class(name="IntermediateActivities_TracedOffer")
umlTrace_Values_CallActionActivation_callExecutions_Value = Class(name="umlTrace_Values_CallActionActivation_callExecutions_Value")
BasicActions_TracedCallActionActivation = Class(name="BasicActions_TracedCallActionActivation")
umlTrace_Values_CompoundValue_featureValues_Value = Class(name="umlTrace_Values_CompoundValue_featureValues_Value")
Kernel_TracedFeatureValue = Class(name="Kernel_TracedFeatureValue")
Kernel_TracedCompoundValue = Class(name="Kernel_TracedCompoundValue")
umlTrace_Values_Token_holder_Value = Class(name="umlTrace_Values_Token_holder_Value")
umlTrace_Values_PinActivation_actionActivation_Value = Class(name="umlTrace_Values_PinActivation_actionActivation_Value")
umlTrace_Values_FeatureValue_values_FeatureValue_Value = Class(name="umlTrace_Values_FeatureValue_values_FeatureValue_Value")
umlTrace_Values_FeatureValue_feature_Value = Class(name="umlTrace_Values_FeatureValue_feature_Value")
uml_TracedStructuralFeature = Class(name="uml_TracedStructuralFeature")
umlTrace_Values_FeatureValue_position_Value = Class(name="umlTrace_Values_FeatureValue_position_Value")
umlTrace_Values_ActivityEdgeInstance_offers_Value = Class(name="umlTrace_Values_ActivityEdgeInstance_offers_Value")
umlTrace_Values_PinActivation_count_temp_Value = Class(name="umlTrace_Values_PinActivation_count_temp_Value")
umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value = Class(name="umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value")
umlTrace_Values_ActivityEdgeInstance_source_Value = Class(name="umlTrace_Values_ActivityEdgeInstance_source_Value")
umlTrace_Values_ActivityEdgeInstance_target_Value = Class(name="umlTrace_Values_ActivityEdgeInstance_target_Value")
umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value = Class(name="umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value")
uml_TracedActivityEdge = Class(name="uml_TracedActivityEdge")
umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value = Class(name="umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value")
uml_TracedActivityNode = Class(name="uml_TracedActivityNode")
umlTrace_Values_ActivityNodeActivation_running_Value = Class(name="umlTrace_Values_ActivityNodeActivation_running_Value")
umlTrace_Values_InputParameterValues_name_Value = Class(name="umlTrace_Values_InputParameterValues_name_Value")
Input_TracedInputParameterValues = Class(name="Input_TracedInputParameterValues")
umlTrace_Values_InputParameterValues_parameterValues_Value = Class(name="umlTrace_Values_InputParameterValues_parameterValues_Value")
umlTrace_Values_ActivityNodeActivation_heldTokens_Value = Class(name="umlTrace_Values_ActivityNodeActivation_heldTokens_Value")
umlTrace_Values_ActivityNodeActivation_incomingEdges_Value = Class(name="umlTrace_Values_ActivityNodeActivation_incomingEdges_Value")
umlTrace_Values_ActivityNodeActivation_isRunning_Value = Class(name="umlTrace_Values_ActivityNodeActivation_isRunning_Value")
umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value = Class(name="umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value")
umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value = Class(name="umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value")
Loci_TracedExecutionEnvironment = Class(name="Loci_TracedExecutionEnvironment")
umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value = Class(name="umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value")
umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value = Class(name="umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value")
umlTrace_Values_ActivityExecution_activationGroup_Value = Class(name="umlTrace_Values_ActivityExecution_activationGroup_Value")
uml_TracedOpaqueBehavior = Class(name="uml_TracedOpaqueBehavior")
uml_TracedArtifact = Class(name="uml_TracedArtifact")
umlTrace_Traced_TracedObjects = Class(name="umlTrace_Traced_TracedObjects")
uml_TracedConnector = Class(name="uml_TracedConnector")
uml_TracedOpaqueAction = Class(name="uml_TracedOpaqueAction")
uml_TracedDataType = Class(name="uml_TracedDataType")
uml_TracedCommunicationPath = Class(name="uml_TracedCommunicationPath")
uml_TracedProperty = Class(name="uml_TracedProperty")
uml_TracedContinuation = Class(name="uml_TracedContinuation")
uml_TracedRemoveStructuralFeatureValueAction = Class(name="uml_TracedRemoveStructuralFeatureValueAction")
uml_TracedSendSignalAction = Class(name="uml_TracedSendSignalAction")
uml_TracedExpression = Class(name="uml_TracedExpression")
uml_TracedConsiderIgnoreFragment = Class(name="uml_TracedConsiderIgnoreFragment")
uml_TracedDataStoreNode = Class(name="uml_TracedDataStoreNode")
uml_TracedFlowFinalNode = Class(name="uml_TracedFlowFinalNode")
uml_TracedInformationItem = Class(name="uml_TracedInformationItem")
IntermediateActivities_TracedJoinNodeActivation = Class(name="IntermediateActivities_TracedJoinNodeActivation")
uml_TracedTimeConstraint = Class(name="uml_TracedTimeConstraint")
uml_TracedInterfaceRealization = Class(name="uml_TracedInterfaceRealization")
uml_TracedActivityFinalNode = Class(name="uml_TracedActivityFinalNode")
uml_TracedDurationObservation = Class(name="uml_TracedDurationObservation")
IntermediateActivities_TracedInitialNodeActivation = Class(name="IntermediateActivities_TracedInitialNodeActivation")
uml_TracedAcceptEventAction = Class(name="uml_TracedAcceptEventAction")
uml_TracedEnumerationLiteral = Class(name="uml_TracedEnumerationLiteral")
uml_TracedAddStructuralFeatureValueAction = Class(name="uml_TracedAddStructuralFeatureValueAction")
uml_TracedReadLinkAction = Class(name="uml_TracedReadLinkAction")
uml_TracedProtocolTransition = Class(name="uml_TracedProtocolTransition")
IntermediateActivities_TracedActivityFinalNodeActivation = Class(name="IntermediateActivities_TracedActivityFinalNodeActivation")
uml_TracedPackage = Class(name="uml_TracedPackage")
uml_TracedCollaboration = Class(name="uml_TracedCollaboration")
uml_TracedTemplateSignature = Class(name="uml_TracedTemplateSignature")
uml_TracedBroadcastSignalAction = Class(name="uml_TracedBroadcastSignalAction")
uml_TracedDeployment = Class(name="uml_TracedDeployment")
uml_TracedPort = Class(name="uml_TracedPort")
uml_TracedTimeInterval = Class(name="uml_TracedTimeInterval")
uml_TracedExtension = Class(name="uml_TracedExtension")
uml_TracedTimeEvent = Class(name="uml_TracedTimeEvent")
uml_TracedSlot = Class(name="uml_TracedSlot")
uml_TracedSignalEvent = Class(name="uml_TracedSignalEvent")
uml_TracedExtensionPoint = Class(name="uml_TracedExtensionPoint")
uml_TracedJoinNode = Class(name="uml_TracedJoinNode")
uml_TracedConstraint = Class(name="uml_TracedConstraint")
uml_TracedGeneralizationSet = Class(name="uml_TracedGeneralizationSet")
uml_TracedReduceAction = Class(name="uml_TracedReduceAction")
uml_TracedInputPin = Class(name="uml_TracedInputPin")
uml_TracedSequenceNode = Class(name="uml_TracedSequenceNode")
uml_TracedInteractionConstraint = Class(name="uml_TracedInteractionConstraint")
uml_TracedComponentRealization = Class(name="uml_TracedComponentRealization")
uml_TracedAssociationClass = Class(name="uml_TracedAssociationClass")
IntermediateActions_TracedValueSpecificationActionActivation = Class(name="IntermediateActions_TracedValueSpecificationActionActivation")
uml_TracedStringExpression = Class(name="uml_TracedStringExpression")
IntermediateActions_TracedReadStructuralFeatureActionActivation = Class(name="IntermediateActions_TracedReadStructuralFeatureActionActivation")
BasicActions_TracedOutputPinActivation = Class(name="BasicActions_TracedOutputPinActivation")
uml_TracedStartObjectBehaviorAction = Class(name="uml_TracedStartObjectBehaviorAction")
uml_TracedElementImport = Class(name="uml_TracedElementImport")
uml_TracedCreateObjectAction = Class(name="uml_TracedCreateObjectAction")
uml_TracedExecutionEnvironment = Class(name="uml_TracedExecutionEnvironment")
uml_TracedOccurrenceSpecification = Class(name="uml_TracedOccurrenceSpecification")
uml_TracedStateMachine = Class(name="uml_TracedStateMachine")
IntermediateActivities_TracedMergeNodeActivation = Class(name="IntermediateActivities_TracedMergeNodeActivation")
uml_TracedInteraction = Class(name="uml_TracedInteraction")
uml_TracedLiteralString = Class(name="uml_TracedLiteralString")
uml_TracedStereotype = Class(name="uml_TracedStereotype")
uml_TracedInterface = Class(name="uml_TracedInterface")
uml_TracedConditionalNode = Class(name="uml_TracedConditionalNode")
uml_TracedReadLinkObjectEndAction = Class(name="uml_TracedReadLinkObjectEndAction")
uml_TracedAnyReceiveEvent = Class(name="uml_TracedAnyReceiveEvent")
uml_TracedComponent = Class(name="uml_TracedComponent")
uml_TracedExtensionEnd = Class(name="uml_TracedExtensionEnd")
uml_TracedTimeObservation = Class(name="uml_TracedTimeObservation")
IntermediateActivities_TracedControlToken = Class(name="IntermediateActivities_TracedControlToken")
uml_TracedCreateLinkObjectAction = Class(name="uml_TracedCreateLinkObjectAction")
uml_TracedRealization = Class(name="uml_TracedRealization")
uml_TracedStartClassifierBehaviorAction = Class(name="uml_TracedStartClassifierBehaviorAction")
uml_TracedCallEvent = Class(name="uml_TracedCallEvent")
uml_TracedConnectableElementTemplateParameter = Class(name="uml_TracedConnectableElementTemplateParameter")
uml_TracedSendObjectAction = Class(name="uml_TracedSendObjectAction")
uml_TracedLifeline = Class(name="uml_TracedLifeline")
uml_TracedEnumeration = Class(name="uml_TracedEnumeration")
uml_TracedCollaborationUse = Class(name="uml_TracedCollaborationUse")
uml_TracedActivityPartition = Class(name="uml_TracedActivityPartition")
uml_TracedExpansionRegion = Class(name="uml_TracedExpansionRegion")
uml_TracedLoopNode = Class(name="uml_TracedLoopNode")
uml_TracedProtocolConformance = Class(name="uml_TracedProtocolConformance")
BasicActions_TracedCallBehaviorActionActivation = Class(name="BasicActions_TracedCallBehaviorActionActivation")
IntermediateActions_TracedAddStructuralFeatureValueActionActivation = Class(name="IntermediateActions_TracedAddStructuralFeatureValueActionActivation")
uml_TracedClassifierTemplateParameter = Class(name="uml_TracedClassifierTemplateParameter")
uml_TracedLinkEndDestructionData = Class(name="uml_TracedLinkEndDestructionData")
uml_TracedDurationInterval = Class(name="uml_TracedDurationInterval")
uml_TracedInclude = Class(name="uml_TracedInclude")
uml_TracedDestructionOccurrenceSpecification = Class(name="uml_TracedDestructionOccurrenceSpecification")
uml_TracedState = Class(name="uml_TracedState")
uml_TracedLiteralUnlimitedNatural = Class(name="uml_TracedLiteralUnlimitedNatural")
uml_TracedStructuredActivityNode = Class(name="uml_TracedStructuredActivityNode")
uml_TracedAbstraction = Class(name="uml_TracedAbstraction")
uml_TracedActivityParameterNode = Class(name="uml_TracedActivityParameterNode")
IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution = Class(name="IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution")
uml_TracedParameterSet = Class(name="uml_TracedParameterSet")
uml_TracedDuration = Class(name="uml_TracedDuration")
uml_TracedUsage = Class(name="uml_TracedUsage")
uml_TracedCreateLinkAction = Class(name="uml_TracedCreateLinkAction")
uml_TracedGeneralization = Class(name="uml_TracedGeneralization")
uml_TracedPartDecomposition = Class(name="uml_TracedPartDecomposition")
BasicActions_TracedOpaqueActionActivation = Class(name="BasicActions_TracedOpaqueActionActivation")
Kernel_TracedLiteralBooleanEvaluation = Class(name="Kernel_TracedLiteralBooleanEvaluation")
uml_TracedReadStructuralFeatureAction = Class(name="uml_TracedReadStructuralFeatureAction")
uml_TracedMergeNode = Class(name="uml_TracedMergeNode")
uml_TracedRedefinableTemplateSignature = Class(name="uml_TracedRedefinableTemplateSignature")
uml_TracedMessage = Class(name="uml_TracedMessage")
uml_TracedLiteralBoolean = Class(name="uml_TracedLiteralBoolean")
uml_TracedQualifierValue = Class(name="uml_TracedQualifierValue")
uml_TracedOperationTemplateParameter = Class(name="uml_TracedOperationTemplateParameter")
uml_TracedReadLinkObjectEndQualifierAction = Class(name="uml_TracedReadLinkObjectEndQualifierAction")
uml_TracedTemplateParameterSubstitution = Class(name="uml_TracedTemplateParameterSubstitution")
uml_TracedExtend = Class(name="uml_TracedExtend")
uml_TracedReadVariableAction = Class(name="uml_TracedReadVariableAction")
IntermediateActivities_TracedDecisionNodeActivation = Class(name="IntermediateActivities_TracedDecisionNodeActivation")
uml_TracedProfileApplication = Class(name="uml_TracedProfileApplication")
uml_TracedInitialNode = Class(name="uml_TracedInitialNode")
uml_TracedLiteralInteger = Class(name="uml_TracedLiteralInteger")
uml_TracedClearVariableAction = Class(name="uml_TracedClearVariableAction")
uml_TracedActionInputPin = Class(name="uml_TracedActionInputPin")
uml_TracedTemplateParameter = Class(name="uml_TracedTemplateParameter")
uml_TracedConnectorEnd = Class(name="uml_TracedConnectorEnd")
uml_TracedMessageOccurrenceSpecification = Class(name="uml_TracedMessageOccurrenceSpecification")
uml_TracedDurationConstraint = Class(name="uml_TracedDurationConstraint")
uml_TracedImage = Class(name="uml_TracedImage")
uml_TracedIntervalConstraint = Class(name="uml_TracedIntervalConstraint")
uml_TracedTrigger = Class(name="uml_TracedTrigger")
uml_TracedCallOperationAction = Class(name="uml_TracedCallOperationAction")
uml_TracedProfile = Class(name="uml_TracedProfile")
uml_TracedInterval = Class(name="uml_TracedInterval")
IntermediateActivities_TracedForkNodeActivation = Class(name="IntermediateActivities_TracedForkNodeActivation")
uml_TracedProtocolStateMachine = Class(name="uml_TracedProtocolStateMachine")
uml_TracedOutputPin = Class(name="uml_TracedOutputPin")
uml_TracedInstanceSpecification = Class(name="uml_TracedInstanceSpecification")
uml_TracedValuePin = Class(name="uml_TracedValuePin")
IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution = Class(name="IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution")
uml_TracedReadIsClassifiedObjectAction = Class(name="uml_TracedReadIsClassifiedObjectAction")
uml_TracedInterruptibleActivityRegion = Class(name="uml_TracedInterruptibleActivityRegion")
uml_TracedDestroyLinkAction = Class(name="uml_TracedDestroyLinkAction")
IntermediateActivities_TracedActivityParameterNodeActivation = Class(name="IntermediateActivities_TracedActivityParameterNodeActivation")
uml_TracedDecisionNode = Class(name="uml_TracedDecisionNode")
uml_TracedValueSpecificationAction = Class(name="uml_TracedValueSpecificationAction")
uml_TracedRegion = Class(name="uml_TracedRegion")
uml_TracedPseudostate = Class(name="uml_TracedPseudostate")
uml_TracedUseCase = Class(name="uml_TracedUseCase")
uml_TracedFinalState = Class(name="uml_TracedFinalState")
IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution = Class(name="IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution")
uml_TracedInteractionOperand = Class(name="uml_TracedInteractionOperand")
uml_TracedInformationFlow = Class(name="uml_TracedInformationFlow")
uml_TracedDependency = Class(name="uml_TracedDependency")
uml_TracedTimeExpression = Class(name="uml_TracedTimeExpression")
uml_TracedReplyAction = Class(name="uml_TracedReplyAction")
IntermediateActions_TracedCreateObjectActionActivation = Class(name="IntermediateActions_TracedCreateObjectActionActivation")
uml_TracedCombinedFragment = Class(name="uml_TracedCombinedFragment")
uml_TracedClause = Class(name="uml_TracedClause")
uml_TracedInstanceValue = Class(name="uml_TracedInstanceValue")
uml_TracedTransition = Class(name="uml_TracedTransition")
uml_TracedLinkEndData = Class(name="uml_TracedLinkEndData")
uml_TracedManifestation = Class(name="uml_TracedManifestation")
uml_TracedReadExtentAction = Class(name="uml_TracedReadExtentAction")
BasicActions_TracedInputPinActivation = Class(name="BasicActions_TracedInputPinActivation")
uml_TracedObjectFlow = Class(name="uml_TracedObjectFlow")
uml_TracedChangeEvent = Class(name="uml_TracedChangeEvent")
uml_TracedDestroyObjectAction = Class(name="uml_TracedDestroyObjectAction")
uml_TracedNode = Class(name="uml_TracedNode")
uml_TracedPackageMerge = Class(name="uml_TracedPackageMerge")
uml_TracedModel = Class(name="uml_TracedModel")
uml_TracedForkNode = Class(name="uml_TracedForkNode")
uml_TracedReception = Class(name="uml_TracedReception")
uml_TracedRaiseExceptionAction = Class(name="uml_TracedRaiseExceptionAction")
uml_TracedSignal = Class(name="uml_TracedSignal")
uml_TracedComment = Class(name="uml_TracedComment")
uml_TracedLiteralNull = Class(name="uml_TracedLiteralNull")
uml_TracedExpansionNode = Class(name="uml_TracedExpansionNode")
uml_TracedControlFlow = Class(name="uml_TracedControlFlow")
uml_TracedOperation = Class(name="uml_TracedOperation")
uml_TracedAddVariableValueAction = Class(name="uml_TracedAddVariableValueAction")
uml_TracedClearAssociationAction = Class(name="uml_TracedClearAssociationAction")
uml_TracedTestIdentityAction = Class(name="uml_TracedTestIdentityAction")
uml_TracedExceptionHandler = Class(name="uml_TracedExceptionHandler")
uml_TracedPackageImport = Class(name="uml_TracedPackageImport")
uml_TracedExecutionOccurrenceSpecification = Class(name="uml_TracedExecutionOccurrenceSpecification")
uml_TracedLiteralReal = Class(name="uml_TracedLiteralReal")
uml_TracedRemoveVariableValueAction = Class(name="uml_TracedRemoveVariableValueAction")
uml_TracedVariable = Class(name="uml_TracedVariable")
uml_TracedInteractionUse = Class(name="uml_TracedInteractionUse")
uml_TracedAssociation = Class(name="uml_TracedAssociation")
uml_TracedStateInvariant = Class(name="uml_TracedStateInvariant")
uml_TracedGeneralOrdering = Class(name="uml_TracedGeneralOrdering")
uml_TracedCallBehaviorAction = Class(name="uml_TracedCallBehaviorAction")
uml_TracedReclassifyObjectAction = Class(name="uml_TracedReclassifyObjectAction")
uml_TracedDevice = Class(name="uml_TracedDevice")
uml_TracedSubstitution = Class(name="uml_TracedSubstitution")
uml_TracedGate = Class(name="uml_TracedGate")
uml_TracedReadSelfAction = Class(name="uml_TracedReadSelfAction")
uml_TracedAcceptCallAction = Class(name="uml_TracedAcceptCallAction")
uml_TracedActivity = Class(name="uml_TracedActivity")
uml_TracedConnectionPointReference = Class(name="uml_TracedConnectionPointReference")
uml_TracedActionExecutionSpecification = Class(name="uml_TracedActionExecutionSpecification")
uml_TracedLinkEndCreationData = Class(name="uml_TracedLinkEndCreationData")
uml_TracedTemplateBinding = Class(name="uml_TracedTemplateBinding")
uml_TracedOpaqueExpression = Class(name="uml_TracedOpaqueExpression")
uml_TracedFunctionBehavior = Class(name="uml_TracedFunctionBehavior")
uml_TracedClearStructuralFeatureAction = Class(name="uml_TracedClearStructuralFeatureAction")
Kernel_TracedLiteralIntegerEvaluation = Class(name="Kernel_TracedLiteralIntegerEvaluation")
uml_TracedUnmarshallAction = Class(name="uml_TracedUnmarshallAction")
uml_TracedCentralBufferNode = Class(name="uml_TracedCentralBufferNode")
umlTrace_Kernel_TracedObject = Class(name="umlTrace_Kernel_TracedObject")
TracedExtensionalValue = Class(name="TracedExtensionalValue")
uml_TracedDeploymentSpecification = Class(name="uml_TracedDeploymentSpecification")
uml_TracedActor = Class(name="uml_TracedActor")
uml_TracedBehaviorExecutionSpecification = Class(name="uml_TracedBehaviorExecutionSpecification")
umlTrace_Kernel_TracedEvaluation = Class(name="umlTrace_Kernel_TracedEvaluation", is_abstract=True)
umlTrace_Kernel_TracedBooleanValue = Class(name="umlTrace_Kernel_TracedBooleanValue")
umlTrace_Kernel_TracedLiteralBooleanEvaluation = Class(name="umlTrace_Kernel_TracedLiteralBooleanEvaluation")
TracedLiteralEvaluation = Class(name="TracedLiteralEvaluation")
umlTrace_Kernel_TracedStructuredValue = Class(name="umlTrace_Kernel_TracedStructuredValue", is_abstract=True)
umlTrace_Kernel_TracedReference = Class(name="umlTrace_Kernel_TracedReference")
TracedStructuredValue = Class(name="TracedStructuredValue")
umlTrace_Kernel_TracedIntegerValue = Class(name="umlTrace_Kernel_TracedIntegerValue")
TracedPrimitiveValue = Class(name="TracedPrimitiveValue")
umlTrace_Kernel_TracedLiteralEvaluation = Class(name="umlTrace_Kernel_TracedLiteralEvaluation", is_abstract=True)
TracedEvaluation = Class(name="TracedEvaluation")
umlTrace_Kernel_TracedValue = Class(name="umlTrace_Kernel_TracedValue", is_abstract=True)
TracedSemanticVisitor = Class(name="TracedSemanticVisitor")
umlTrace_Kernel_TracedPrimitiveValue = Class(name="umlTrace_Kernel_TracedPrimitiveValue", is_abstract=True)
TracedValue = Class(name="TracedValue")
umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution = Class(name="umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution", is_abstract=True)
TracedExecution = Class(name="TracedExecution")
umlTrace_BasicBehaviors_TracedParameterValue = Class(name="umlTrace_BasicBehaviors_TracedParameterValue")
umlTrace_BasicBehaviors_TracedExecution = Class(name="umlTrace_BasicBehaviors_TracedExecution", is_abstract=True)
TracedObject = Class(name="TracedObject")
umlTrace_Kernel_TracedCompoundValue = Class(name="umlTrace_Kernel_TracedCompoundValue", is_abstract=True)
umlTrace_Kernel_TracedFeatureValue = Class(name="umlTrace_Kernel_TracedFeatureValue", is_abstract=True)
umlTrace_Kernel_TracedExtensionalValue = Class(name="umlTrace_Kernel_TracedExtensionalValue", is_abstract=True)
TracedCompoundValue = Class(name="TracedCompoundValue")
umlTrace_Kernel_TracedLiteralIntegerEvaluation = Class(name="umlTrace_Kernel_TracedLiteralIntegerEvaluation")
umlTrace_IntermediateActivities_TracedMergeNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedMergeNodeActivation")
umlTrace_IntermediateActivities_TracedControlToken = Class(name="umlTrace_IntermediateActivities_TracedControlToken")
umlTrace_IntermediateActivities_TracedObjectToken = Class(name="umlTrace_IntermediateActivities_TracedObjectToken")
umlTrace_IntermediateActivities_TracedDecisionNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedDecisionNodeActivation")
umlTrace_IntermediateActivities_TracedForkedToken = Class(name="umlTrace_IntermediateActivities_TracedForkedToken")
TracedToken = Class(name="TracedToken")
umlTrace_IntermediateActivities_TracedJoinNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedJoinNodeActivation")
TracedControlNodeActivation = Class(name="TracedControlNodeActivation")
umlTrace_IntermediateActivities_TracedInitialNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedInitialNodeActivation")
umlTrace_IntermediateActivities_TracedObjectNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedObjectNodeActivation", is_abstract=True)
TracedActivityNodeActivation = Class(name="TracedActivityNodeActivation")
umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation")
umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup = Class(name="umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup")
umlTrace_IntermediateActivities_TracedActivityNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedActivityNodeActivation")
umlTrace_IntermediateActivities_TracedForkNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedForkNodeActivation")
umlTrace_IntermediateActivities_TracedToken = Class(name="umlTrace_IntermediateActivities_TracedToken")
umlTrace_IntermediateActivities_TracedOffer = Class(name="umlTrace_IntermediateActivities_TracedOffer")
umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation")
TracedObjectNodeActivation = Class(name="TracedObjectNodeActivation")
umlTrace_IntermediateActivities_TracedActivityEdgeInstance = Class(name="umlTrace_IntermediateActivities_TracedActivityEdgeInstance")
umlTrace_Loci_TracedSemanticVisitor = Class(name="umlTrace_Loci_TracedSemanticVisitor")
umlTrace_Loci_TracedExecutor = Class(name="umlTrace_Loci_TracedExecutor")
umlTrace_Loci_TracedExecutionEnvironment = Class(name="umlTrace_Loci_TracedExecutionEnvironment")
umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation = Class(name="umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation", is_abstract=True)
TracedActionActivation = Class(name="TracedActionActivation")
umlTrace_IntermediateActions_TracedValueSpecificationActionActivation = Class(name="umlTrace_IntermediateActions_TracedValueSpecificationActionActivation")
umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation = Class(name="umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation")
TracedStructuralFeatureActionActivation = Class(name="TracedStructuralFeatureActionActivation")
umlTrace_IntermediateActivities_TracedControlNodeActivation = Class(name="umlTrace_IntermediateActivities_TracedControlNodeActivation", is_abstract=True)
umlTrace_IntermediateActivities_TracedActivityExecution = Class(name="umlTrace_IntermediateActivities_TracedActivityExecution")
umlTrace_Loci_TracedExecutionFactory = Class(name="umlTrace_Loci_TracedExecutionFactory")
umlTrace_Loci_TracedLocus = Class(name="umlTrace_Loci_TracedLocus")
umlTrace_BasicActions_TracedCallActionActivation = Class(name="umlTrace_BasicActions_TracedCallActionActivation", is_abstract=True)
TracedInvocationActionActivation = Class(name="TracedInvocationActionActivation")
umlTrace_BasicActions_TracedPinActivation = Class(name="umlTrace_BasicActions_TracedPinActivation", is_abstract=True)
umlTrace_BasicActions_TracedInputPinActivation = Class(name="umlTrace_BasicActions_TracedInputPinActivation")
umlTrace_BasicActions_TracedInvocationActionActivation = Class(name="umlTrace_BasicActions_TracedInvocationActionActivation", is_abstract=True)
umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution = Class(name="umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution")
TracedOpaqueBehaviorExecution = Class(name="TracedOpaqueBehaviorExecution")
umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation = Class(name="umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation")
TracedWriteStructuralFeatureActionActivation = Class(name="TracedWriteStructuralFeatureActionActivation")
umlTrace_IntermediateActions_TracedCreateObjectActionActivation = Class(name="umlTrace_IntermediateActions_TracedCreateObjectActionActivation")
umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation = Class(name="umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation", is_abstract=True)
umlTrace_BasicActions_TracedActionActivation = Class(name="umlTrace_BasicActions_TracedActionActivation", is_abstract=True)
umlTrace_BasicActions_TracedOutputPinActivation = Class(name="umlTrace_BasicActions_TracedOutputPinActivation")
TracedPinActivation = Class(name="TracedPinActivation")
umlTrace_BasicActions_TracedCallBehaviorActionActivation = Class(name="umlTrace_BasicActions_TracedCallBehaviorActionActivation")
TracedCallActionActivation = Class(name="TracedCallActionActivation")
umlTrace_BasicActions_TracedOpaqueActionActivation = Class(name="umlTrace_BasicActions_TracedOpaqueActionActivation")
umlTrace_uml_TracedOpaqueAction = Class(name="umlTrace_uml_TracedOpaqueAction")
TracedAction = Class(name="TracedAction")
uml_umlTrace_OpaqueAction = Class(name="uml_umlTrace_OpaqueAction")
umlTrace_uml_TracedDataType = Class(name="umlTrace_uml_TracedDataType")
TracedClassifier = Class(name="TracedClassifier")
uml_umlTrace_DataType = Class(name="uml_umlTrace_DataType")
umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution = Class(name="umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution")
umlTrace_uml_TracedCommunicationPath = Class(name="umlTrace_uml_TracedCommunicationPath")
TracedAssociation = Class(name="TracedAssociation")
umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution = Class(name="umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution")
umlTrace_uml_TracedLinkAction = Class(name="umlTrace_uml_TracedLinkAction", is_abstract=True)
umlTrace_Input_TracedInputParameterValues = Class(name="umlTrace_Input_TracedInputParameterValues")
umlTrace_uml_TracedStructuralFeature = Class(name="umlTrace_uml_TracedStructuralFeature", is_abstract=True)
uml_TracedFeature = Class(name="uml_TracedFeature")
uml_TracedTypedElement = Class(name="uml_TracedTypedElement")
uml_TracedMultiplicityElement = Class(name="uml_TracedMultiplicityElement")
umlTrace_uml_TracedConnector = Class(name="umlTrace_uml_TracedConnector")
TracedFeature = Class(name="TracedFeature")
uml_TracedBehavior = Class(name="uml_TracedBehavior")
uml_umlTrace_Connector = Class(name="uml_umlTrace_Connector")
uml_umlTrace_Property = Class(name="uml_umlTrace_Property")
umlTrace_uml_TracedContinuation = Class(name="umlTrace_uml_TracedContinuation")
TracedInteractionFragment = Class(name="TracedInteractionFragment")
uml_umlTrace_Continuation = Class(name="uml_umlTrace_Continuation")
umlTrace_uml_TracedRemoveStructuralFeatureValueAction = Class(name="umlTrace_uml_TracedRemoveStructuralFeatureValueAction")
umlTrace_uml_TracedProperty = Class(name="umlTrace_uml_TracedProperty")
uml_TracedConnectableElement = Class(name="uml_TracedConnectableElement")
uml_TracedDeploymentTarget = Class(name="uml_TracedDeploymentTarget")
uml_umlTrace_Artifact = Class(name="uml_umlTrace_Artifact")
umlTrace_uml_TracedTimeConstraint = Class(name="umlTrace_uml_TracedTimeConstraint")
TracedIntervalConstraint = Class(name="TracedIntervalConstraint")
umlTrace_uml_TracedInterfaceRealization = Class(name="umlTrace_uml_TracedInterfaceRealization")
TracedRealization = Class(name="TracedRealization")
uml_TracedBehavioredClassifier = Class(name="uml_TracedBehavioredClassifier")
umlTrace_uml_TracedObjectNode = Class(name="umlTrace_uml_TracedObjectNode", is_abstract=True)
TracedWriteStructuralFeatureAction = Class(name="TracedWriteStructuralFeatureAction")
uml_umlTrace_RemoveStructuralFeatureValueAction = Class(name="uml_umlTrace_RemoveStructuralFeatureValueAction")
umlTrace_uml_TracedSendSignalAction = Class(name="umlTrace_uml_TracedSendSignalAction")
TracedInvocationAction = Class(name="TracedInvocationAction")
uml_umlTrace_SendSignalAction = Class(name="uml_umlTrace_SendSignalAction")
umlTrace_uml_TracedOpaqueBehavior = Class(name="umlTrace_uml_TracedOpaqueBehavior")
TracedBehavior = Class(name="TracedBehavior")
umlTrace_uml_TracedArtifact = Class(name="umlTrace_uml_TracedArtifact")
uml_TracedClassifier = Class(name="uml_TracedClassifier")
uml_TracedDeployedArtifact = Class(name="uml_TracedDeployedArtifact")
uml_umlTrace_AcceptEventAction = Class(name="uml_umlTrace_AcceptEventAction")
umlTrace_uml_TracedEnumerationLiteral = Class(name="umlTrace_uml_TracedEnumerationLiteral")
TracedInstanceSpecification = Class(name="TracedInstanceSpecification")
umlTrace_uml_TracedAddStructuralFeatureValueAction = Class(name="umlTrace_uml_TracedAddStructuralFeatureValueAction")
uml_umlTrace_AddStructuralFeatureValueAction = Class(name="uml_umlTrace_AddStructuralFeatureValueAction")
umlTrace_uml_TracedReadLinkAction = Class(name="umlTrace_uml_TracedReadLinkAction")
TracedLinkAction = Class(name="TracedLinkAction")
umlTrace_uml_TracedActivityFinalNode = Class(name="umlTrace_uml_TracedActivityFinalNode")
TracedFinalNode = Class(name="TracedFinalNode")
uml_umlTrace_ActivityFinalNode = Class(name="uml_umlTrace_ActivityFinalNode")
umlTrace_uml_TracedDurationObservation = Class(name="umlTrace_uml_TracedDurationObservation")
TracedObservation = Class(name="TracedObservation")
uml_TracedNamedElement = Class(name="uml_TracedNamedElement")
uml_umlTrace_DurationObservation = Class(name="uml_umlTrace_DurationObservation")
umlTrace_uml_TracedAcceptEventAction = Class(name="umlTrace_uml_TracedAcceptEventAction")
umlTrace_uml_TracedDataStoreNode = Class(name="umlTrace_uml_TracedDataStoreNode")
TracedCentralBufferNode = Class(name="TracedCentralBufferNode")
umlTrace_uml_TracedFlowFinalNode = Class(name="umlTrace_uml_TracedFlowFinalNode")
uml_umlTrace_FlowFinalNode = Class(name="uml_umlTrace_FlowFinalNode")
umlTrace_uml_TracedInteractionFragment = Class(name="umlTrace_uml_TracedInteractionFragment", is_abstract=True)
TracedNamedElement = Class(name="TracedNamedElement")
umlTrace_uml_TracedClassifier = Class(name="umlTrace_uml_TracedClassifier", is_abstract=True)
uml_TracedNamespace = Class(name="uml_TracedNamespace")
uml_TracedRedefinableElement = Class(name="uml_TracedRedefinableElement")
uml_TracedType = Class(name="uml_TracedType")
uml_TracedTemplateableElement = Class(name="uml_TracedTemplateableElement")
uml_umlTrace_ReadLinkAction = Class(name="uml_umlTrace_ReadLinkAction")
umlTrace_uml_TracedExpression = Class(name="umlTrace_uml_TracedExpression")
TracedValueSpecification = Class(name="TracedValueSpecification")
uml_umlTrace_Expression = Class(name="uml_umlTrace_Expression")
umlTrace_uml_TracedConsiderIgnoreFragment = Class(name="umlTrace_uml_TracedConsiderIgnoreFragment")
TracedCombinedFragment = Class(name="TracedCombinedFragment")
umlTrace_uml_TracedInformationItem = Class(name="umlTrace_uml_TracedInformationItem")
uml_umlTrace_Collaboration = Class(name="uml_umlTrace_Collaboration")
umlTrace_uml_TracedMessageEnd = Class(name="umlTrace_uml_TracedMessageEnd", is_abstract=True)
umlTrace_uml_TracedTemplateSignature = Class(name="umlTrace_uml_TracedTemplateSignature")
TracedElement = Class(name="TracedElement")
uml_umlTrace_InformationItem = Class(name="uml_umlTrace_InformationItem")
umlTrace_uml_TracedCollaboration = Class(name="umlTrace_uml_TracedCollaboration")
uml_TracedStructuredClassifier = Class(name="uml_TracedStructuredClassifier")
umlTrace_uml_TracedPort = Class(name="umlTrace_uml_TracedPort")
TracedProperty = Class(name="TracedProperty")
umlTrace_uml_TracedTimeInterval = Class(name="umlTrace_uml_TracedTimeInterval")
TracedInterval = Class(name="TracedInterval")
umlTrace_uml_TracedAction = Class(name="umlTrace_uml_TracedAction", is_abstract=True)
TracedExecutableNode = Class(name="TracedExecutableNode")
uml_umlTrace_TemplateSignature = Class(name="uml_umlTrace_TemplateSignature")
umlTrace_uml_TracedBroadcastSignalAction = Class(name="umlTrace_uml_TracedBroadcastSignalAction")
uml_umlTrace_BroadcastSignalAction = Class(name="uml_umlTrace_BroadcastSignalAction")
umlTrace_uml_TracedDeployment = Class(name="umlTrace_uml_TracedDeployment")
TracedDependency = Class(name="TracedDependency")
umlTrace_uml_TracedDirectedRelationship = Class(name="umlTrace_uml_TracedDirectedRelationship", is_abstract=True)
TracedRelationship = Class(name="TracedRelationship")
umlTrace_uml_TracedTimeEvent = Class(name="umlTrace_uml_TracedTimeEvent")
TracedEvent = Class(name="TracedEvent")
uml_umlTrace_TimeEvent = Class(name="uml_umlTrace_TimeEvent")
umlTrace_uml_TracedPackageableElement = Class(name="umlTrace_uml_TracedPackageableElement", is_abstract=True)
uml_TracedParameterableElement = Class(name="uml_TracedParameterableElement")
umlTrace_uml_TracedType = Class(name="umlTrace_uml_TracedType", is_abstract=True)
TracedPackageableElement = Class(name="TracedPackageableElement")
umlTrace_uml_TracedExtension = Class(name="umlTrace_uml_TracedExtension")
umlTrace_uml_TracedProtocolTransition = Class(name="umlTrace_uml_TracedProtocolTransition")
TracedTransition = Class(name="TracedTransition")
umlTrace_uml_TracedPackage = Class(name="umlTrace_uml_TracedPackage")
uml_TracedPackageableElement = Class(name="uml_TracedPackageableElement")
umlTrace_uml_TracedConstraint = Class(name="umlTrace_uml_TracedConstraint")
uml_umlTrace_Constraint = Class(name="uml_umlTrace_Constraint")
umlTrace_uml_TracedMultiplicityElement = Class(name="umlTrace_uml_TracedMultiplicityElement", is_abstract=True)
umlTrace_uml_TracedLiteralSpecification = Class(name="umlTrace_uml_TracedLiteralSpecification", is_abstract=True)
uml_umlTrace_Package = Class(name="uml_umlTrace_Package")
umlTrace_uml_TracedBehavioredClassifier = Class(name="umlTrace_uml_TracedBehavioredClassifier", is_abstract=True)
umlTrace_uml_TracedStructuralFeatureAction = Class(name="umlTrace_uml_TracedStructuralFeatureAction", is_abstract=True)
uml_umlTrace_ReduceAction = Class(name="uml_umlTrace_ReduceAction")
umlTrace_uml_TracedInputPin = Class(name="umlTrace_uml_TracedInputPin")
TracedPin = Class(name="TracedPin")
uml_umlTrace_InputPin = Class(name="uml_umlTrace_InputPin")
umlTrace_uml_TracedSequenceNode = Class(name="umlTrace_uml_TracedSequenceNode")
TracedStructuredActivityNode = Class(name="TracedStructuredActivityNode")
uml_TracedExecutableNode = Class(name="uml_TracedExecutableNode")
umlTrace_uml_TracedFeature = Class(name="umlTrace_uml_TracedFeature", is_abstract=True)
TracedRedefinableElement = Class(name="TracedRedefinableElement")
umlTrace_uml_TracedInteractionConstraint = Class(name="umlTrace_uml_TracedInteractionConstraint")
TracedConstraint = Class(name="TracedConstraint")
umlTrace_uml_TracedGeneralizationSet = Class(name="umlTrace_uml_TracedGeneralizationSet")
uml_umlTrace_GeneralizationSet = Class(name="uml_umlTrace_GeneralizationSet")
umlTrace_uml_TracedReduceAction = Class(name="umlTrace_uml_TracedReduceAction")
umlTrace_uml_TracedComponentRealization = Class(name="umlTrace_uml_TracedComponentRealization")
umlTrace_uml_TracedAssociationClass = Class(name="umlTrace_uml_TracedAssociationClass")
umlTrace_uml_TracedSlot = Class(name="umlTrace_uml_TracedSlot")
umlTrace_uml_TracedWriteStructuralFeatureAction = Class(name="umlTrace_uml_TracedWriteStructuralFeatureAction", is_abstract=True)
TracedStructuralFeatureAction = Class(name="TracedStructuralFeatureAction")
umlTrace_uml_TracedElement = Class(name="umlTrace_uml_TracedElement", is_abstract=True)
TracedEModelElement = Class(name="TracedEModelElement")
umlTrace_uml_TracedJoinNode = Class(name="umlTrace_uml_TracedJoinNode")
TracedControlNode = Class(name="TracedControlNode")
uml_umlTrace_JoinNode = Class(name="uml_umlTrace_JoinNode")
umlTrace_uml_TracedStartObjectBehaviorAction = Class(name="umlTrace_uml_TracedStartObjectBehaviorAction")
TracedCallAction = Class(name="TracedCallAction")
uml_umlTrace_StartObjectBehaviorAction = Class(name="uml_umlTrace_StartObjectBehaviorAction")
umlTrace_uml_TracedElementImport = Class(name="umlTrace_uml_TracedElementImport")
TracedDirectedRelationship = Class(name="TracedDirectedRelationship")
uml_umlTrace_ElementImport = Class(name="uml_umlTrace_ElementImport")
uml_umlTrace_Slot = Class(name="uml_umlTrace_Slot")
umlTrace_uml_TracedSignalEvent = Class(name="umlTrace_uml_TracedSignalEvent")
TracedMessageEvent = Class(name="TracedMessageEvent")
uml_umlTrace_SignalEvent = Class(name="uml_umlTrace_SignalEvent")
umlTrace_uml_TracedExtensionPoint = Class(name="umlTrace_uml_TracedExtensionPoint")
uml_umlTrace_ExtensionPoint = Class(name="uml_umlTrace_ExtensionPoint")
uml_umlTrace_OccurrenceSpecification = Class(name="uml_umlTrace_OccurrenceSpecification")
umlTrace_uml_TracedStringExpression = Class(name="umlTrace_uml_TracedStringExpression")
umlTrace_uml_TracedDeployedArtifact = Class(name="umlTrace_uml_TracedDeployedArtifact", is_abstract=True)
umlTrace_uml_TracedStereotype = Class(name="umlTrace_uml_TracedStereotype")
TracedClass = Class(name="TracedClass")
umlTrace_uml_TracedInterface = Class(name="umlTrace_uml_TracedInterface")
umlTrace_uml_TracedCreateObjectAction = Class(name="umlTrace_uml_TracedCreateObjectAction")
uml_umlTrace_CreateObjectAction = Class(name="uml_umlTrace_CreateObjectAction")
umlTrace_uml_TracedExecutionEnvironment = Class(name="umlTrace_uml_TracedExecutionEnvironment")
TracedNode = Class(name="TracedNode")
umlTrace_uml_TracedOccurrenceSpecification = Class(name="umlTrace_uml_TracedOccurrenceSpecification")
umlTrace_uml_TracedConditionalNode = Class(name="umlTrace_uml_TracedConditionalNode")
umlTrace_uml_TracedReadLinkObjectEndAction = Class(name="umlTrace_uml_TracedReadLinkObjectEndAction")
uml_umlTrace_Interface = Class(name="uml_umlTrace_Interface")
uml_umlTrace_ReadLinkObjectEndAction = Class(name="uml_umlTrace_ReadLinkObjectEndAction")
umlTrace_uml_TracedAnyReceiveEvent = Class(name="umlTrace_uml_TracedAnyReceiveEvent")
uml_umlTrace_AnyReceiveEvent = Class(name="uml_umlTrace_AnyReceiveEvent")
umlTrace_uml_TracedNamedElement = Class(name="umlTrace_uml_TracedNamedElement", is_abstract=True)
umlTrace_uml_TracedComponent = Class(name="umlTrace_uml_TracedComponent")
umlTrace_uml_TracedLiteralString = Class(name="umlTrace_uml_TracedLiteralString")
TracedLiteralSpecification = Class(name="TracedLiteralSpecification")
uml_umlTrace_LiteralString = Class(name="uml_umlTrace_LiteralString")
umlTrace_uml_TracedRealization = Class(name="umlTrace_uml_TracedRealization")
TracedAbstraction = Class(name="TracedAbstraction")
umlTrace_uml_TracedStartClassifierBehaviorAction = Class(name="umlTrace_uml_TracedStartClassifierBehaviorAction")
umlTrace_uml_TracedExtensionEnd = Class(name="umlTrace_uml_TracedExtensionEnd")
umlTrace_uml_TracedStateMachine = Class(name="umlTrace_uml_TracedStateMachine")
umlTrace_uml_TracedValueSpecification = Class(name="umlTrace_uml_TracedValueSpecification", is_abstract=True)
umlTrace_uml_TracedInteraction = Class(name="umlTrace_uml_TracedInteraction")
uml_TracedInteractionFragment = Class(name="uml_TracedInteractionFragment")
uml_TracedAction = Class(name="uml_TracedAction")
uml_umlTrace_SendObjectAction = Class(name="uml_umlTrace_SendObjectAction")
umlTrace_uml_TracedLifeline = Class(name="umlTrace_uml_TracedLifeline")
uml_umlTrace_StartClassifierBehaviorAction = Class(name="uml_umlTrace_StartClassifierBehaviorAction")
umlTrace_uml_TracedMessageEvent = Class(name="umlTrace_uml_TracedMessageEvent", is_abstract=True)
umlTrace_uml_TracedCallEvent = Class(name="umlTrace_uml_TracedCallEvent")
uml_umlTrace_CallEvent = Class(name="uml_umlTrace_CallEvent")
umlTrace_uml_TracedConnectableElementTemplateParameter = Class(name="umlTrace_uml_TracedConnectableElementTemplateParameter")
TracedTemplateParameter = Class(name="TracedTemplateParameter")
umlTrace_uml_TracedRelationship = Class(name="umlTrace_uml_TracedRelationship", is_abstract=True)
umlTrace_uml_TracedSendObjectAction = Class(name="umlTrace_uml_TracedSendObjectAction")
umlTrace_uml_TracedExpansionRegion = Class(name="umlTrace_uml_TracedExpansionRegion")
umlTrace_uml_TracedWriteVariableAction = Class(name="umlTrace_uml_TracedWriteVariableAction", is_abstract=True)
TracedVariableAction = Class(name="TracedVariableAction")
uml_umlTrace_Lifeline = Class(name="uml_umlTrace_Lifeline")
umlTrace_uml_TracedExecutionSpecification = Class(name="umlTrace_uml_TracedExecutionSpecification", is_abstract=True)
umlTrace_uml_TracedTimeObservation = Class(name="umlTrace_uml_TracedTimeObservation")
uml_umlTrace_TimeObservation = Class(name="uml_umlTrace_TimeObservation")
umlTrace_uml_TracedCreateLinkObjectAction = Class(name="umlTrace_uml_TracedCreateLinkObjectAction")
TracedCreateLinkAction = Class(name="TracedCreateLinkAction")
umlTrace_uml_TracedProtocolConformance = Class(name="umlTrace_uml_TracedProtocolConformance")
uml_umlTrace_ProtocolConformance = Class(name="uml_umlTrace_ProtocolConformance")
umlTrace_uml_TracedLoopNode = Class(name="umlTrace_uml_TracedLoopNode")
umlTrace_uml_TracedPrimitiveType = Class(name="umlTrace_uml_TracedPrimitiveType")
TracedDataType = Class(name="TracedDataType")
umlTrace_uml_TracedEnumeration = Class(name="umlTrace_uml_TracedEnumeration")
umlTrace_uml_TracedCollaborationUse = Class(name="umlTrace_uml_TracedCollaborationUse")
uml_umlTrace_CollaborationUse = Class(name="uml_umlTrace_CollaborationUse")
umlTrace_uml_TracedActivityPartition = Class(name="umlTrace_uml_TracedActivityPartition")
TracedActivityGroup = Class(name="TracedActivityGroup")
ActivityContent = Class(name="ActivityContent")
uml_TracedActivityGroup = Class(name="uml_TracedActivityGroup")
uml_umlTrace_ActivityPartition = Class(name="uml_umlTrace_ActivityPartition")
umlTrace_uml_TracedVariableAction = Class(name="umlTrace_uml_TracedVariableAction", is_abstract=True)
umlTrace_uml_TracedLinkEndDestructionData = Class(name="umlTrace_uml_TracedLinkEndDestructionData")
TracedLinkEndData = Class(name="TracedLinkEndData")
umlTrace_uml_TracedDurationInterval = Class(name="umlTrace_uml_TracedDurationInterval")
umlTrace_uml_TracedInclude = Class(name="umlTrace_uml_TracedInclude")
uml_TracedDirectedRelationship = Class(name="uml_TracedDirectedRelationship")
uml_umlTrace_Include = Class(name="uml_umlTrace_Include")
umlTrace_uml_TracedActivityNode = Class(name="umlTrace_uml_TracedActivityNode", is_abstract=True)
umlTrace_uml_TracedDestructionOccurrenceSpecification = Class(name="umlTrace_uml_TracedDestructionOccurrenceSpecification")
TracedMessageOccurrenceSpecification = Class(name="TracedMessageOccurrenceSpecification")
umlTrace_uml_TracedState = Class(name="umlTrace_uml_TracedState")
uml_TracedVertex = Class(name="uml_TracedVertex")
umlTrace_uml_TracedBehavior = Class(name="umlTrace_uml_TracedBehavior", is_abstract=True)
uml_TracedBehavioralFeature = Class(name="uml_TracedBehavioralFeature")
uml_umlTrace_State = Class(name="uml_umlTrace_State")
umlTrace_uml_TracedCallAction = Class(name="umlTrace_uml_TracedCallAction", is_abstract=True)
umlTrace_uml_TracedTemplateableElement = Class(name="umlTrace_uml_TracedTemplateableElement", is_abstract=True)
uml_umlTrace_ActivityParameterNode = Class(name="uml_umlTrace_ActivityParameterNode")
umlTrace_uml_TracedParameterSet = Class(name="umlTrace_uml_TracedParameterSet")
umlTrace_uml_TracedClassifierTemplateParameter = Class(name="umlTrace_uml_TracedClassifierTemplateParameter")
umlTrace_uml_TracedActivityParameterNode = Class(name="umlTrace_uml_TracedActivityParameterNode")
TracedObjectNode = Class(name="TracedObjectNode")
uml_umlTrace_Class = Class(name="uml_umlTrace_Class")
umlTrace_uml_TracedUsage = Class(name="umlTrace_uml_TracedUsage")
umlTrace_uml_TracedLiteralUnlimitedNatural = Class(name="umlTrace_uml_TracedLiteralUnlimitedNatural")
uml_umlTrace_LiteralUnlimitedNatural = Class(name="uml_umlTrace_LiteralUnlimitedNatural")
uml_umlTrace_ParameterSet = Class(name="uml_umlTrace_ParameterSet")
umlTrace_uml_TracedDuration = Class(name="umlTrace_uml_TracedDuration")
uml_TracedObservation = Class(name="uml_TracedObservation")
uml_umlTrace_Duration = Class(name="uml_umlTrace_Duration")
umlTrace_uml_TracedClass = Class(name="umlTrace_uml_TracedClass")
uml_TracedEncapsulatedClassifier = Class(name="uml_TracedEncapsulatedClassifier")
umlTrace_uml_TracedReadStructuralFeatureAction = Class(name="umlTrace_uml_TracedReadStructuralFeatureAction")
uml_umlTrace_ReadStructuralFeatureAction = Class(name="uml_umlTrace_ReadStructuralFeatureAction")
umlTrace_uml_TracedMergeNode = Class(name="umlTrace_uml_TracedMergeNode")
uml_umlTrace_MergeNode = Class(name="uml_umlTrace_MergeNode")
umlTrace_uml_TracedStructuredActivityNode = Class(name="umlTrace_uml_TracedStructuredActivityNode")
uml_umlTrace_StructuredActivityNode = Class(name="uml_umlTrace_StructuredActivityNode")
umlTrace_uml_TracedAbstraction = Class(name="umlTrace_uml_TracedAbstraction")
uml_umlTrace_Generalization = Class(name="uml_umlTrace_Generalization")
umlTrace_uml_TracedPartDecomposition = Class(name="umlTrace_uml_TracedPartDecomposition")
TracedInteractionUse = Class(name="TracedInteractionUse")
umlTrace_uml_TracedTypedElement = Class(name="umlTrace_uml_TracedTypedElement", is_abstract=True)
umlTrace_uml_TracedRedefinableTemplateSignature = Class(name="umlTrace_uml_TracedRedefinableTemplateSignature")
umlTrace_uml_TracedCreateLinkAction = Class(name="umlTrace_uml_TracedCreateLinkAction")
TracedWriteLinkAction = Class(name="TracedWriteLinkAction")
uml_umlTrace_CreateLinkAction = Class(name="uml_umlTrace_CreateLinkAction")
umlTrace_uml_TracedGeneralization = Class(name="umlTrace_uml_TracedGeneralization")
uml_umlTrace_TemplateParameterSubstitution = Class(name="uml_umlTrace_TemplateParameterSubstitution")
umlTrace_uml_TracedExtend = Class(name="umlTrace_uml_TracedExtend")
umlTrace_uml_TracedOperationTemplateParameter = Class(name="umlTrace_uml_TracedOperationTemplateParameter")
umlTrace_uml_TracedReadLinkObjectEndQualifierAction = Class(name="umlTrace_uml_TracedReadLinkObjectEndQualifierAction")
uml_umlTrace_ReadLinkObjectEndQualifierAction = Class(name="uml_umlTrace_ReadLinkObjectEndQualifierAction")
umlTrace_uml_TracedTemplateParameterSubstitution = Class(name="umlTrace_uml_TracedTemplateParameterSubstitution")
uml_TracedMessageEnd = Class(name="uml_TracedMessageEnd")
uml_umlTrace_Extend = Class(name="uml_umlTrace_Extend")
umlTrace_uml_TracedReadVariableAction = Class(name="umlTrace_uml_TracedReadVariableAction")
uml_umlTrace_ReadVariableAction = Class(name="uml_umlTrace_ReadVariableAction")
umlTrace_uml_TracedMessage = Class(name="umlTrace_uml_TracedMessage")
umlTrace_uml_TracedProfileApplication = Class(name="umlTrace_uml_TracedProfileApplication")
uml_umlTrace_Message = Class(name="uml_umlTrace_Message")
umlTrace_uml_TracedLiteralBoolean = Class(name="umlTrace_uml_TracedLiteralBoolean")
uml_umlTrace_LiteralBoolean = Class(name="uml_umlTrace_LiteralBoolean")
umlTrace_uml_TracedQualifierValue = Class(name="umlTrace_uml_TracedQualifierValue")
uml_umlTrace_QualifierValue = Class(name="uml_umlTrace_QualifierValue")
umlTrace_uml_TracedInitialNode = Class(name="umlTrace_uml_TracedInitialNode")
uml_umlTrace_InitialNode = Class(name="uml_umlTrace_InitialNode")
umlTrace_uml_TracedLiteralInteger = Class(name="umlTrace_uml_TracedLiteralInteger")
uml_umlTrace_LiteralInteger = Class(name="uml_umlTrace_LiteralInteger")
umlTrace_uml_TracedClearVariableAction = Class(name="umlTrace_uml_TracedClearVariableAction")
uml_umlTrace_ClearVariableAction = Class(name="uml_umlTrace_ClearVariableAction")
uml_umlTrace_TemplateParameter = Class(name="uml_umlTrace_TemplateParameter")
umlTrace_uml_TracedConnectorEnd = Class(name="umlTrace_uml_TracedConnectorEnd")
TracedMultiplicityElement = Class(name="TracedMultiplicityElement")
uml_umlTrace_ProfileApplication = Class(name="uml_umlTrace_ProfileApplication")
umlTrace_uml_TracedParameterableElement = Class(name="umlTrace_uml_TracedParameterableElement", is_abstract=True)
umlTrace_uml_TracedTemplateParameter = Class(name="umlTrace_uml_TracedTemplateParameter")
uml_umlTrace_Parameter = Class(name="uml_umlTrace_Parameter")
umlTrace_uml_TracedActionInputPin = Class(name="umlTrace_uml_TracedActionInputPin")
TracedInputPin = Class(name="TracedInputPin")
umlTrace_uml_TracedTrigger = Class(name="umlTrace_uml_TracedTrigger")
uml_TracedEvent = Class(name="uml_TracedEvent")
uml_umlTrace_ConnectorEnd = Class(name="uml_umlTrace_ConnectorEnd")
umlTrace_uml_TracedMessageOccurrenceSpecification = Class(name="umlTrace_uml_TracedMessageOccurrenceSpecification")
umlTrace_uml_TracedDurationConstraint = Class(name="umlTrace_uml_TracedDurationConstraint")
umlTrace_uml_TracedImage = Class(name="umlTrace_uml_TracedImage")
uml_umlTrace_Image = Class(name="uml_umlTrace_Image")
umlTrace_uml_TracedEncapsulatedClassifier = Class(name="umlTrace_uml_TracedEncapsulatedClassifier", is_abstract=True)
TracedStructuredClassifier = Class(name="TracedStructuredClassifier")
umlTrace_uml_TracedParameter = Class(name="umlTrace_uml_TracedParameter")
uml_umlTrace_Interval = Class(name="uml_umlTrace_Interval")
umlTrace_uml_TracedIntervalConstraint = Class(name="umlTrace_uml_TracedIntervalConstraint")
umlTrace_uml_TracedInstanceSpecification = Class(name="umlTrace_uml_TracedInstanceSpecification")
uml_umlTrace_Trigger = Class(name="uml_umlTrace_Trigger")
umlTrace_uml_TracedCallOperationAction = Class(name="umlTrace_uml_TracedCallOperationAction")
uml_umlTrace_CallOperationAction = Class(name="uml_umlTrace_CallOperationAction")
umlTrace_uml_TracedProfile = Class(name="umlTrace_uml_TracedProfile")
TracedPackage = Class(name="TracedPackage")
umlTrace_uml_TracedInterval = Class(name="umlTrace_uml_TracedInterval")
uml_umlTrace_ReadIsClassifiedObjectAction = Class(name="uml_umlTrace_ReadIsClassifiedObjectAction")
umlTrace_uml_TracedProtocolStateMachine = Class(name="umlTrace_uml_TracedProtocolStateMachine")
TracedStateMachine = Class(name="TracedStateMachine")
umlTrace_uml_TracedOutputPin = Class(name="umlTrace_uml_TracedOutputPin")
uml_umlTrace_OutputPin = Class(name="uml_umlTrace_OutputPin")
uml_umlTrace_InstanceSpecification = Class(name="uml_umlTrace_InstanceSpecification")
umlTrace_uml_TracedValuePin = Class(name="umlTrace_uml_TracedValuePin")
umlTrace_uml_TracedReadIsClassifiedObjectAction = Class(name="umlTrace_uml_TracedReadIsClassifiedObjectAction")
uml_umlTrace_ValueSpecificationAction = Class(name="uml_umlTrace_ValueSpecificationAction")
umlTrace_uml_TracedRegion = Class(name="umlTrace_uml_TracedRegion")
umlTrace_uml_TracedDecisionNode = Class(name="umlTrace_uml_TracedDecisionNode")
uml_umlTrace_DecisionNode = Class(name="uml_umlTrace_DecisionNode")
umlTrace_uml_TracedValueSpecificationAction = Class(name="umlTrace_uml_TracedValueSpecificationAction")
uml_umlTrace_InterruptibleActivityRegion = Class(name="uml_umlTrace_InterruptibleActivityRegion")
umlTrace_uml_TracedDestroyLinkAction = Class(name="umlTrace_uml_TracedDestroyLinkAction")
uml_umlTrace_DestroyLinkAction = Class(name="uml_umlTrace_DestroyLinkAction")
umlTrace_uml_TracedFinalState = Class(name="umlTrace_uml_TracedFinalState")
TracedState = Class(name="TracedState")
umlTrace_uml_TracedActivityGroup = Class(name="umlTrace_uml_TracedActivityGroup", is_abstract=True)
uml_umlTrace_Region = Class(name="uml_umlTrace_Region")
umlTrace_uml_TracedInterruptibleActivityRegion = Class(name="umlTrace_uml_TracedInterruptibleActivityRegion")
uml_umlTrace_InteractionOperand = Class(name="uml_umlTrace_InteractionOperand")
umlTrace_uml_TracedActivityEdge = Class(name="umlTrace_uml_TracedActivityEdge", is_abstract=True)
umlTrace_uml_TracedInteractionOperand = Class(name="umlTrace_uml_TracedInteractionOperand")
umlTrace_uml_TracedInformationFlow = Class(name="umlTrace_uml_TracedInformationFlow")
uml_umlTrace_Pseudostate = Class(name="uml_umlTrace_Pseudostate")
umlTrace_uml_TracedControlNode = Class(name="umlTrace_uml_TracedControlNode", is_abstract=True)
TracedActivityNode = Class(name="TracedActivityNode")
umlTrace_uml_TracedUseCase = Class(name="umlTrace_uml_TracedUseCase")
TracedBehavioredClassifier = Class(name="TracedBehavioredClassifier")
uml_TracedRelationship = Class(name="uml_TracedRelationship")
uml_umlTrace_InformationFlow = Class(name="uml_umlTrace_InformationFlow")
umlTrace_uml_TracedPseudostate = Class(name="umlTrace_uml_TracedPseudostate")
TracedVertex = Class(name="TracedVertex")
umlTrace_uml_TracedCombinedFragment = Class(name="umlTrace_uml_TracedCombinedFragment")
uml_umlTrace_CombinedFragment = Class(name="uml_umlTrace_CombinedFragment")
uml_umlTrace_UseCase = Class(name="uml_umlTrace_UseCase")
umlTrace_uml_TracedReplyAction = Class(name="umlTrace_uml_TracedReplyAction")
uml_umlTrace_ReplyAction = Class(name="uml_umlTrace_ReplyAction")
umlTrace_uml_TracedDependency = Class(name="umlTrace_uml_TracedDependency")
umlTrace_uml_TracedWriteLinkAction = Class(name="umlTrace_uml_TracedWriteLinkAction", is_abstract=True)
umlTrace_uml_TracedClause = Class(name="umlTrace_uml_TracedClause")
uml_umlTrace_Clause = Class(name="uml_umlTrace_Clause")
umlTrace_uml_TracedInstanceValue = Class(name="umlTrace_uml_TracedInstanceValue")
uml_umlTrace_InstanceValue = Class(name="uml_umlTrace_InstanceValue")
uml_umlTrace_ReadExtentAction = Class(name="uml_umlTrace_ReadExtentAction")
umlTrace_uml_TracedTransition = Class(name="umlTrace_uml_TracedTransition")
uml_umlTrace_Dependency = Class(name="uml_umlTrace_Dependency")
umlTrace_uml_TracedTimeExpression = Class(name="umlTrace_uml_TracedTimeExpression")
uml_umlTrace_TimeExpression = Class(name="uml_umlTrace_TimeExpression")
umlTrace_uml_TracedManifestation = Class(name="umlTrace_uml_TracedManifestation")
umlTrace_uml_TracedReadExtentAction = Class(name="umlTrace_uml_TracedReadExtentAction")
uml_umlTrace_LinkEndData = Class(name="uml_umlTrace_LinkEndData")
umlTrace_uml_TracedNode = Class(name="umlTrace_uml_TracedNode")
uml_umlTrace_Transition = Class(name="uml_umlTrace_Transition")
umlTrace_uml_TracedLinkEndData = Class(name="umlTrace_uml_TracedLinkEndData")
uml_umlTrace_ChangeEvent = Class(name="uml_umlTrace_ChangeEvent")
umlTrace_uml_TracedRedefinableElement = Class(name="umlTrace_uml_TracedRedefinableElement", is_abstract=True)
umlTrace_uml_TracedPackageMerge = Class(name="umlTrace_uml_TracedPackageMerge")
uml_umlTrace_PackageMerge = Class(name="uml_umlTrace_PackageMerge")
umlTrace_uml_TracedModel = Class(name="umlTrace_uml_TracedModel")
umlTrace_uml_TracedObjectFlow = Class(name="umlTrace_uml_TracedObjectFlow")
TracedActivityEdge = Class(name="TracedActivityEdge")
uml_umlTrace_ObjectFlow = Class(name="uml_umlTrace_ObjectFlow")
umlTrace_uml_TracedEvent = Class(name="umlTrace_uml_TracedEvent", is_abstract=True)
umlTrace_uml_TracedChangeEvent = Class(name="umlTrace_uml_TracedChangeEvent")
uml_umlTrace_Comment = Class(name="uml_umlTrace_Comment")
umlTrace_uml_TracedStructuredClassifier = Class(name="umlTrace_uml_TracedStructuredClassifier", is_abstract=True)
umlTrace_uml_TracedDestroyObjectAction = Class(name="umlTrace_uml_TracedDestroyObjectAction")
uml_umlTrace_DestroyObjectAction = Class(name="uml_umlTrace_DestroyObjectAction")
umlTrace_uml_TracedForkNode = Class(name="umlTrace_uml_TracedForkNode")
uml_umlTrace_ForkNode = Class(name="uml_umlTrace_ForkNode")
umlTrace_uml_TracedFinalNode = Class(name="umlTrace_uml_TracedFinalNode", is_abstract=True)
umlTrace_uml_TracedSignal = Class(name="umlTrace_uml_TracedSignal")
uml_umlTrace_Signal = Class(name="uml_umlTrace_Signal")
umlTrace_uml_TracedComment = Class(name="umlTrace_uml_TracedComment")
uml_umlTrace_Reception = Class(name="uml_umlTrace_Reception")
umlTrace_uml_TracedRaiseExceptionAction = Class(name="umlTrace_uml_TracedRaiseExceptionAction")
uml_umlTrace_RaiseExceptionAction = Class(name="uml_umlTrace_RaiseExceptionAction")
umlTrace_uml_TracedLiteralNull = Class(name="umlTrace_uml_TracedLiteralNull")
uml_umlTrace_LiteralNull = Class(name="uml_umlTrace_LiteralNull")
umlTrace_uml_TracedExpansionNode = Class(name="umlTrace_uml_TracedExpansionNode")
uml_umlTrace_ExpansionNode = Class(name="uml_umlTrace_ExpansionNode")
umlTrace_uml_TracedReception = Class(name="umlTrace_uml_TracedReception")
TracedBehavioralFeature = Class(name="TracedBehavioralFeature")
uml_umlTrace_ClearAssociationAction = Class(name="uml_umlTrace_ClearAssociationAction")
umlTrace_uml_TracedPin = Class(name="umlTrace_uml_TracedPin", is_abstract=True)
uml_TracedObjectNode = Class(name="uml_TracedObjectNode")
umlTrace_uml_TracedTestIdentityAction = Class(name="umlTrace_uml_TracedTestIdentityAction")
umlTrace_uml_TracedBehavioralFeature = Class(name="umlTrace_uml_TracedBehavioralFeature", is_abstract=True)
umlTrace_uml_TracedAddVariableValueAction = Class(name="umlTrace_uml_TracedAddVariableValueAction")
TracedWriteVariableAction = Class(name="TracedWriteVariableAction")
uml_umlTrace_AddVariableValueAction = Class(name="uml_umlTrace_AddVariableValueAction")
umlTrace_uml_TracedClearAssociationAction = Class(name="umlTrace_uml_TracedClearAssociationAction")
uml_umlTrace_TestIdentityAction = Class(name="uml_umlTrace_TestIdentityAction")
umlTrace_uml_TracedControlFlow = Class(name="umlTrace_uml_TracedControlFlow")
uml_umlTrace_ControlFlow = Class(name="uml_umlTrace_ControlFlow")
umlTrace_uml_TracedOperation = Class(name="umlTrace_uml_TracedOperation")
umlTrace_uml_TracedObservation = Class(name="umlTrace_uml_TracedObservation", is_abstract=True)
umlTrace_uml_TracedNamespace = Class(name="umlTrace_uml_TracedNamespace", is_abstract=True)
uml_umlTrace_Operation = Class(name="uml_umlTrace_Operation")
umlTrace_uml_TracedConnectableElement = Class(name="umlTrace_uml_TracedConnectableElement", is_abstract=True)
umlTrace_uml_TracedVertex = Class(name="umlTrace_uml_TracedVertex", is_abstract=True)
umlTrace_uml_TracedPackageImport = Class(name="umlTrace_uml_TracedPackageImport")
umlTrace_uml_TracedInteractionUse = Class(name="umlTrace_uml_TracedInteractionUse")
uml_umlTrace_PackageImport = Class(name="uml_umlTrace_PackageImport")
umlTrace_uml_TracedExecutionOccurrenceSpecification = Class(name="umlTrace_uml_TracedExecutionOccurrenceSpecification")
TracedOccurrenceSpecification = Class(name="TracedOccurrenceSpecification")
uml_TracedExecutionSpecification = Class(name="uml_TracedExecutionSpecification")
umlTrace_uml_TracedExceptionHandler = Class(name="umlTrace_uml_TracedExceptionHandler")
uml_umlTrace_ExceptionHandler = Class(name="uml_umlTrace_ExceptionHandler")
umlTrace_uml_TracedVariable = Class(name="umlTrace_uml_TracedVariable")
uml_umlTrace_Variable = Class(name="uml_umlTrace_Variable")
uml_umlTrace_Association = Class(name="uml_umlTrace_Association")
umlTrace_uml_TracedStateInvariant = Class(name="umlTrace_uml_TracedStateInvariant")
uml_umlTrace_StateInvariant = Class(name="uml_umlTrace_StateInvariant")
uml_umlTrace_InteractionUse = Class(name="uml_umlTrace_InteractionUse")
umlTrace_uml_TracedAssociation = Class(name="umlTrace_uml_TracedAssociation")
umlTrace_uml_TracedDevice = Class(name="umlTrace_uml_TracedDevice")
umlTrace_uml_TracedSubstitution = Class(name="umlTrace_uml_TracedSubstitution")
umlTrace_uml_TracedLiteralReal = Class(name="umlTrace_uml_TracedLiteralReal")
uml_umlTrace_LiteralReal = Class(name="uml_umlTrace_LiteralReal")
umlTrace_uml_TracedInvocationAction = Class(name="umlTrace_uml_TracedInvocationAction", is_abstract=True)
umlTrace_uml_TracedRemoveVariableValueAction = Class(name="umlTrace_uml_TracedRemoveVariableValueAction")
uml_umlTrace_RemoveVariableValueAction = Class(name="uml_umlTrace_RemoveVariableValueAction")
uml_umlTrace_ReclassifyObjectAction = Class(name="uml_umlTrace_ReclassifyObjectAction")
umlTrace_uml_TracedGate = Class(name="umlTrace_uml_TracedGate")
TracedMessageEnd = Class(name="TracedMessageEnd")
uml_umlTrace_Gate = Class(name="uml_umlTrace_Gate")
umlTrace_uml_TracedDeploymentTarget = Class(name="umlTrace_uml_TracedDeploymentTarget", is_abstract=True)
umlTrace_uml_TracedGeneralOrdering = Class(name="umlTrace_uml_TracedGeneralOrdering")
uml_umlTrace_GeneralOrdering = Class(name="uml_umlTrace_GeneralOrdering")
umlTrace_uml_TracedCallBehaviorAction = Class(name="umlTrace_uml_TracedCallBehaviorAction")
uml_umlTrace_CallBehaviorAction = Class(name="uml_umlTrace_CallBehaviorAction")
umlTrace_uml_TracedReclassifyObjectAction = Class(name="umlTrace_uml_TracedReclassifyObjectAction")
umlTrace_uml_TracedConnectionPointReference = Class(name="umlTrace_uml_TracedConnectionPointReference")
umlTrace_uml_TracedActivity = Class(name="umlTrace_uml_TracedActivity")
umlTrace_uml_TracedLinkEndCreationData = Class(name="umlTrace_uml_TracedLinkEndCreationData")
umlTrace_uml_TracedTemplateBinding = Class(name="umlTrace_uml_TracedTemplateBinding")
uml_umlTrace_ConnectionPointReference = Class(name="uml_umlTrace_ConnectionPointReference")
umlTrace_uml_TracedActionExecutionSpecification = Class(name="umlTrace_uml_TracedActionExecutionSpecification")
TracedExecutionSpecification = Class(name="TracedExecutionSpecification")
uml_umlTrace_ActionExecutionSpecification = Class(name="uml_umlTrace_ActionExecutionSpecification")
umlTrace_uml_TracedReadSelfAction = Class(name="umlTrace_uml_TracedReadSelfAction")
uml_umlTrace_ReadSelfAction = Class(name="uml_umlTrace_ReadSelfAction")
umlTrace_uml_TracedAcceptCallAction = Class(name="umlTrace_uml_TracedAcceptCallAction")
TracedAcceptEventAction = Class(name="TracedAcceptEventAction")
umlTrace_uml_TracedActor = Class(name="umlTrace_uml_TracedActor")
uml_umlTrace_Actor = Class(name="uml_umlTrace_Actor")
umlTrace_uml_TracedBehaviorExecutionSpecification = Class(name="umlTrace_uml_TracedBehaviorExecutionSpecification")
uml_umlTrace_BehaviorExecutionSpecification = Class(name="uml_umlTrace_BehaviorExecutionSpecification")
umlTrace_uml_TracedExecutableNode = Class(name="umlTrace_uml_TracedExecutableNode", is_abstract=True)
uml_umlTrace_TemplateBinding = Class(name="uml_umlTrace_TemplateBinding")
umlTrace_uml_TracedClearStructuralFeatureAction = Class(name="umlTrace_uml_TracedClearStructuralFeatureAction")
uml_umlTrace_ClearStructuralFeatureAction = Class(name="uml_umlTrace_ClearStructuralFeatureAction")
umlTrace_uml_TracedOpaqueExpression = Class(name="umlTrace_uml_TracedOpaqueExpression")
uml_umlTrace_OpaqueExpression = Class(name="uml_umlTrace_OpaqueExpression")
umlTrace_uml_TracedFunctionBehavior = Class(name="umlTrace_uml_TracedFunctionBehavior")
TracedOpaqueBehavior = Class(name="TracedOpaqueBehavior")
umlTrace_uml_TracedDeploymentSpecification = Class(name="umlTrace_uml_TracedDeploymentSpecification")
TracedArtifact = Class(name="TracedArtifact")
umlTrace_uml_TracedUnmarshallAction = Class(name="umlTrace_uml_TracedUnmarshallAction")
uml_umlTrace_UnmarshallAction = Class(name="uml_umlTrace_UnmarshallAction")
umlTrace_uml_TracedCentralBufferNode = Class(name="umlTrace_uml_TracedCentralBufferNode")
uml_umlTrace_CentralBufferNode = Class(name="uml_umlTrace_CentralBufferNode")
umlTrace_ecore_TracedEModelElement = Class(name="umlTrace_ecore_TracedEModelElement", is_abstract=True)
ecore_umlTrace_EAnnotation = Class(name="ecore_umlTrace_EAnnotation")

# umlTrace_Trace class attributes and methods

# umlTrace_State class attributes and methods

# Steps class attributes and methods

# TracedObjects class attributes and methods

# Locus_factory_Value class attributes and methods

# Locus_extensionalValues_Value class attributes and methods

# Locus_executor_Value class attributes and methods

# ObjectNodeActivation_offeredTokenCount_Value class attributes and methods

# SemanticVisitor_runtimeModelElement_Value class attributes and methods

# SmallStep class attributes and methods

# BigStep class attributes and methods

# Object_types_Value class attributes and methods

# Reference_referent_Value class attributes and methods

# IntegerValue_value_IntegerValue_Value class attributes and methods

# ForkedToken_remainingOffersCount_Value class attributes and methods

# ForkedToken_baseToken_Value class attributes and methods

# ForkedToken_baseTokenIsWithdrawn_Value class attributes and methods

# ExecutionFactory_builtInTypes_Value class attributes and methods

# ExecutionFactory_primitiveBehaviorPrototypes_Value class attributes and methods

# ExecutionFactory_locus_ExecutionFactory_Value class attributes and methods

# ActivityNodeActivationGroup_activityExecution_Value class attributes and methods

# ActivityNodeActivationGroup_edgeInstances_Value class attributes and methods

# Executor_locus_Executor_Value class attributes and methods

# PrimitiveValue_type_Value class attributes and methods

# ParameterValue_values_ParameterValue_Value class attributes and methods

# ParameterValue_parameter_ParameterValue_Value class attributes and methods

# ActionActivation_pinActivations_Value class attributes and methods

# ActionActivation_firing_Value class attributes and methods

# Execution_parameterValues_Value class attributes and methods

# Execution_context_Value class attributes and methods

# Element_semanticVisitor_Value class attributes and methods

# ActivityNodeActivationGroup_nodeActivations_Value class attributes and methods

# FeatureValue_feature_Value class attributes and methods

# FeatureValue_position_Value class attributes and methods

# PinActivation_actionActivation_Value class attributes and methods

# Evaluation_specification_Evaluation_Value class attributes and methods

# Evaluation_locus_Evaluation_Value class attributes and methods

# BooleanValue_value_BooleanValue_Value class attributes and methods

# ObjectToken_value_Value class attributes and methods

# CallActionActivation_callExecutions_Value class attributes and methods

# CompoundValue_featureValues_Value class attributes and methods

# Token_holder_Value class attributes and methods

# Offer_offeredTokens_Value class attributes and methods

# FeatureValue_values_FeatureValue_Value class attributes and methods

# ActivityNodeActivation_node_ActivityNodeActivation_Value class attributes and methods

# ActivityNodeActivation_running_Value class attributes and methods

# ActivityNodeActivation_isRunning_Value class attributes and methods

# PinActivation_count_temp_Value class attributes and methods

# ActivityEdgeInstance_group_ActivityEdgeInstance_Value class attributes and methods

# ActivityEdgeInstance_offers_Value class attributes and methods

# ActivityEdgeInstance_target_Value class attributes and methods

# ActivityEdgeInstance_edge_ActivityEdgeInstance_Value class attributes and methods

# ActivityEdgeInstance_source_Value class attributes and methods

# InputParameterValues_name_Value class attributes and methods

# InputParameterValues_parameterValues_Value class attributes and methods

# ActivityNodeActivation_heldTokens_Value class attributes and methods

# umlTrace_Values_Object_types_Value class attributes and methods

# uml_TracedClass class attributes and methods

# Kernel_TracedObject class attributes and methods

# Values_umlTrace_State class attributes and methods

# ActivityNodeActivation_outgoingEdges_Value class attributes and methods

# ActivityNodeActivation_incomingEdges_Value class attributes and methods

# ActivityNodeActivation_group_ActivityNodeActivation_Value class attributes and methods

# ExtensionalValue_locus_ExtensionalValue_Value class attributes and methods

# ActivityExecution_activationGroup_Value class attributes and methods

# ExecutionEnvironment_locus_ExecutionEnvironment_Value class attributes and methods

# umlTrace_Steps_SmallStep class attributes and methods

# Steps_umlTrace_State class attributes and methods

# umlTrace_Steps_Steps class attributes and methods

# umlTrace_Steps_BigStep class attributes and methods

# umlTrace_Values_ForkedToken_baseToken_Value class attributes and methods

# IntermediateActivities_TracedToken class attributes and methods

# umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value class attributes and methods
umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value_baseTokenIsWithdrawn: Property = Property(name="baseTokenIsWithdrawn", type=BooleanType)
umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value.attributes={umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value_baseTokenIsWithdrawn}

# umlTrace_Values_Reference_referent_Value class attributes and methods

# Kernel_TracedReference class attributes and methods

# umlTrace_Values_IntegerValue_value_IntegerValue_Value class attributes and methods
umlTrace_Values_IntegerValue_value_IntegerValue_Value_value_IntegerValue: Property = Property(name="value_IntegerValue", type=IntegerType)
umlTrace_Values_IntegerValue_value_IntegerValue_Value.attributes={umlTrace_Values_IntegerValue_value_IntegerValue_Value_value_IntegerValue}

# Kernel_TracedIntegerValue class attributes and methods

# umlTrace_Values_ForkedToken_remainingOffersCount_Value class attributes and methods
umlTrace_Values_ForkedToken_remainingOffersCount_Value_remainingOffersCount: Property = Property(name="remainingOffersCount", type=IntegerType)
umlTrace_Values_ForkedToken_remainingOffersCount_Value.attributes={umlTrace_Values_ForkedToken_remainingOffersCount_Value_remainingOffersCount}

# IntermediateActivities_TracedForkedToken class attributes and methods

# umlTrace_Values_Locus_factory_Value class attributes and methods

# umlTrace_Values_Locus_extensionalValues_Value class attributes and methods

# Kernel_TracedExtensionalValue class attributes and methods

# umlTrace_Values_ExecutionFactory_builtInTypes_Value class attributes and methods

# uml_TracedPrimitiveType class attributes and methods

# Loci_TracedExecutionFactory class attributes and methods

# umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value class attributes and methods

# BasicBehaviors_TracedOpaqueBehaviorExecution class attributes and methods

# umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value class attributes and methods

# Loci_TracedLocus class attributes and methods

# uml_TracedElement class attributes and methods

# Loci_TracedSemanticVisitor class attributes and methods

# umlTrace_Values_ParameterValue_values_ParameterValue_Value class attributes and methods

# umlTrace_Values_Locus_executor_Value class attributes and methods

# Loci_TracedExecutor class attributes and methods

# umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value class attributes and methods
umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value_offeredTokenCount: Property = Property(name="offeredTokenCount", type=IntegerType)
umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value.attributes={umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value_offeredTokenCount}

# IntermediateActivities_TracedObjectNodeActivation class attributes and methods

# umlTrace_Values_ActionActivation_firing_Value class attributes and methods
umlTrace_Values_ActionActivation_firing_Value_firing: Property = Property(name="firing", type=BooleanType)
umlTrace_Values_ActionActivation_firing_Value.attributes={umlTrace_Values_ActionActivation_firing_Value_firing}

# umlTrace_Values_SemanticVisitor_runtimeModelElement_Value class attributes and methods

# umlTrace_Values_Execution_parameterValues_Value class attributes and methods

# Kernel_TracedValue class attributes and methods

# BasicBehaviors_TracedParameterValue class attributes and methods

# umlTrace_Values_ParameterValue_parameter_ParameterValue_Value class attributes and methods

# uml_TracedParameter class attributes and methods

# umlTrace_Values_ActionActivation_pinActivations_Value class attributes and methods

# BasicActions_TracedPinActivation class attributes and methods

# BasicActions_TracedActionActivation class attributes and methods

# umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value class attributes and methods

# IntermediateActivities_TracedActivityNodeActivation class attributes and methods

# IntermediateActivities_TracedActivityNodeActivationGroup class attributes and methods

# BasicBehaviors_TracedExecution class attributes and methods

# umlTrace_Values_Execution_context_Value class attributes and methods

# umlTrace_Values_Element_semanticVisitor_Value class attributes and methods

# umlTrace_Values_PrimitiveValue_type_Value class attributes and methods

# Kernel_TracedPrimitiveValue class attributes and methods

# umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value class attributes and methods

# IntermediateActivities_TracedActivityExecution class attributes and methods

# umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value class attributes and methods

# IntermediateActivities_TracedActivityEdgeInstance class attributes and methods

# umlTrace_Values_Executor_locus_Executor_Value class attributes and methods

# umlTrace_Values_ObjectToken_value_Value class attributes and methods

# IntermediateActivities_TracedObjectToken class attributes and methods

# umlTrace_Values_Evaluation_specification_Evaluation_Value class attributes and methods

# uml_TracedValueSpecification class attributes and methods

# Kernel_TracedEvaluation class attributes and methods

# umlTrace_Values_Evaluation_locus_Evaluation_Value class attributes and methods

# umlTrace_Values_BooleanValue_value_BooleanValue_Value class attributes and methods
umlTrace_Values_BooleanValue_value_BooleanValue_Value_value_BooleanValue: Property = Property(name="value_BooleanValue", type=BooleanType)
umlTrace_Values_BooleanValue_value_BooleanValue_Value.attributes={umlTrace_Values_BooleanValue_value_BooleanValue_Value_value_BooleanValue}

# Kernel_TracedBooleanValue class attributes and methods

# umlTrace_Values_Offer_offeredTokens_Value class attributes and methods

# IntermediateActivities_TracedOffer class attributes and methods

# umlTrace_Values_CallActionActivation_callExecutions_Value class attributes and methods

# BasicActions_TracedCallActionActivation class attributes and methods

# umlTrace_Values_CompoundValue_featureValues_Value class attributes and methods

# Kernel_TracedFeatureValue class attributes and methods

# Kernel_TracedCompoundValue class attributes and methods

# umlTrace_Values_Token_holder_Value class attributes and methods

# umlTrace_Values_PinActivation_actionActivation_Value class attributes and methods

# umlTrace_Values_FeatureValue_values_FeatureValue_Value class attributes and methods

# umlTrace_Values_FeatureValue_feature_Value class attributes and methods

# uml_TracedStructuralFeature class attributes and methods

# umlTrace_Values_FeatureValue_position_Value class attributes and methods
umlTrace_Values_FeatureValue_position_Value_position: Property = Property(name="position", type=IntegerType)
umlTrace_Values_FeatureValue_position_Value.attributes={umlTrace_Values_FeatureValue_position_Value_position}

# umlTrace_Values_ActivityEdgeInstance_offers_Value class attributes and methods

# umlTrace_Values_PinActivation_count_temp_Value class attributes and methods
umlTrace_Values_PinActivation_count_temp_Value_count_temp: Property = Property(name="count_temp", type=IntegerType)
umlTrace_Values_PinActivation_count_temp_Value.attributes={umlTrace_Values_PinActivation_count_temp_Value_count_temp}

# umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value class attributes and methods

# umlTrace_Values_ActivityEdgeInstance_source_Value class attributes and methods

# umlTrace_Values_ActivityEdgeInstance_target_Value class attributes and methods

# umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value class attributes and methods

# uml_TracedActivityEdge class attributes and methods

# umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value class attributes and methods

# uml_TracedActivityNode class attributes and methods

# umlTrace_Values_ActivityNodeActivation_running_Value class attributes and methods
umlTrace_Values_ActivityNodeActivation_running_Value_running: Property = Property(name="running", type=BooleanType)
umlTrace_Values_ActivityNodeActivation_running_Value.attributes={umlTrace_Values_ActivityNodeActivation_running_Value_running}

# umlTrace_Values_InputParameterValues_name_Value class attributes and methods
umlTrace_Values_InputParameterValues_name_Value_name: Property = Property(name="name", type=StringType)
umlTrace_Values_InputParameterValues_name_Value.attributes={umlTrace_Values_InputParameterValues_name_Value_name}

# Input_TracedInputParameterValues class attributes and methods

# umlTrace_Values_InputParameterValues_parameterValues_Value class attributes and methods

# umlTrace_Values_ActivityNodeActivation_heldTokens_Value class attributes and methods

# umlTrace_Values_ActivityNodeActivation_incomingEdges_Value class attributes and methods

# umlTrace_Values_ActivityNodeActivation_isRunning_Value class attributes and methods
umlTrace_Values_ActivityNodeActivation_isRunning_Value_isRunning: Property = Property(name="isRunning", type=BooleanType)
umlTrace_Values_ActivityNodeActivation_isRunning_Value.attributes={umlTrace_Values_ActivityNodeActivation_isRunning_Value_isRunning}

# umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value class attributes and methods

# umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value class attributes and methods

# Loci_TracedExecutionEnvironment class attributes and methods

# umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value class attributes and methods

# umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value class attributes and methods

# umlTrace_Values_ActivityExecution_activationGroup_Value class attributes and methods

# uml_TracedOpaqueBehavior class attributes and methods

# uml_TracedArtifact class attributes and methods

# umlTrace_Traced_TracedObjects class attributes and methods

# uml_TracedConnector class attributes and methods

# uml_TracedOpaqueAction class attributes and methods

# uml_TracedDataType class attributes and methods

# uml_TracedCommunicationPath class attributes and methods

# uml_TracedProperty class attributes and methods

# uml_TracedContinuation class attributes and methods

# uml_TracedRemoveStructuralFeatureValueAction class attributes and methods

# uml_TracedSendSignalAction class attributes and methods

# uml_TracedExpression class attributes and methods

# uml_TracedConsiderIgnoreFragment class attributes and methods

# uml_TracedDataStoreNode class attributes and methods

# uml_TracedFlowFinalNode class attributes and methods

# uml_TracedInformationItem class attributes and methods

# IntermediateActivities_TracedJoinNodeActivation class attributes and methods

# uml_TracedTimeConstraint class attributes and methods

# uml_TracedInterfaceRealization class attributes and methods

# uml_TracedActivityFinalNode class attributes and methods

# uml_TracedDurationObservation class attributes and methods

# IntermediateActivities_TracedInitialNodeActivation class attributes and methods

# uml_TracedAcceptEventAction class attributes and methods

# uml_TracedEnumerationLiteral class attributes and methods

# uml_TracedAddStructuralFeatureValueAction class attributes and methods

# uml_TracedReadLinkAction class attributes and methods

# uml_TracedProtocolTransition class attributes and methods

# IntermediateActivities_TracedActivityFinalNodeActivation class attributes and methods

# uml_TracedPackage class attributes and methods

# uml_TracedCollaboration class attributes and methods

# uml_TracedTemplateSignature class attributes and methods

# uml_TracedBroadcastSignalAction class attributes and methods

# uml_TracedDeployment class attributes and methods

# uml_TracedPort class attributes and methods

# uml_TracedTimeInterval class attributes and methods

# uml_TracedExtension class attributes and methods

# uml_TracedTimeEvent class attributes and methods

# uml_TracedSlot class attributes and methods

# uml_TracedSignalEvent class attributes and methods

# uml_TracedExtensionPoint class attributes and methods

# uml_TracedJoinNode class attributes and methods

# uml_TracedConstraint class attributes and methods

# uml_TracedGeneralizationSet class attributes and methods

# uml_TracedReduceAction class attributes and methods

# uml_TracedInputPin class attributes and methods

# uml_TracedSequenceNode class attributes and methods

# uml_TracedInteractionConstraint class attributes and methods

# uml_TracedComponentRealization class attributes and methods

# uml_TracedAssociationClass class attributes and methods

# IntermediateActions_TracedValueSpecificationActionActivation class attributes and methods

# uml_TracedStringExpression class attributes and methods

# IntermediateActions_TracedReadStructuralFeatureActionActivation class attributes and methods

# BasicActions_TracedOutputPinActivation class attributes and methods

# uml_TracedStartObjectBehaviorAction class attributes and methods

# uml_TracedElementImport class attributes and methods

# uml_TracedCreateObjectAction class attributes and methods

# uml_TracedExecutionEnvironment class attributes and methods

# uml_TracedOccurrenceSpecification class attributes and methods

# uml_TracedStateMachine class attributes and methods

# IntermediateActivities_TracedMergeNodeActivation class attributes and methods

# uml_TracedInteraction class attributes and methods

# uml_TracedLiteralString class attributes and methods

# uml_TracedStereotype class attributes and methods

# uml_TracedInterface class attributes and methods

# uml_TracedConditionalNode class attributes and methods

# uml_TracedReadLinkObjectEndAction class attributes and methods

# uml_TracedAnyReceiveEvent class attributes and methods

# uml_TracedComponent class attributes and methods

# uml_TracedExtensionEnd class attributes and methods

# uml_TracedTimeObservation class attributes and methods

# IntermediateActivities_TracedControlToken class attributes and methods

# uml_TracedCreateLinkObjectAction class attributes and methods

# uml_TracedRealization class attributes and methods

# uml_TracedStartClassifierBehaviorAction class attributes and methods

# uml_TracedCallEvent class attributes and methods

# uml_TracedConnectableElementTemplateParameter class attributes and methods

# uml_TracedSendObjectAction class attributes and methods

# uml_TracedLifeline class attributes and methods

# uml_TracedEnumeration class attributes and methods

# uml_TracedCollaborationUse class attributes and methods

# uml_TracedActivityPartition class attributes and methods

# uml_TracedExpansionRegion class attributes and methods

# uml_TracedLoopNode class attributes and methods

# uml_TracedProtocolConformance class attributes and methods

# BasicActions_TracedCallBehaviorActionActivation class attributes and methods

# IntermediateActions_TracedAddStructuralFeatureValueActionActivation class attributes and methods

# uml_TracedClassifierTemplateParameter class attributes and methods

# uml_TracedLinkEndDestructionData class attributes and methods

# uml_TracedDurationInterval class attributes and methods

# uml_TracedInclude class attributes and methods

# uml_TracedDestructionOccurrenceSpecification class attributes and methods

# uml_TracedState class attributes and methods

# uml_TracedLiteralUnlimitedNatural class attributes and methods

# uml_TracedStructuredActivityNode class attributes and methods

# uml_TracedAbstraction class attributes and methods

# uml_TracedActivityParameterNode class attributes and methods

# IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution class attributes and methods

# uml_TracedParameterSet class attributes and methods

# uml_TracedDuration class attributes and methods

# uml_TracedUsage class attributes and methods

# uml_TracedCreateLinkAction class attributes and methods

# uml_TracedGeneralization class attributes and methods

# uml_TracedPartDecomposition class attributes and methods

# BasicActions_TracedOpaqueActionActivation class attributes and methods

# Kernel_TracedLiteralBooleanEvaluation class attributes and methods

# uml_TracedReadStructuralFeatureAction class attributes and methods

# uml_TracedMergeNode class attributes and methods

# uml_TracedRedefinableTemplateSignature class attributes and methods

# uml_TracedMessage class attributes and methods

# uml_TracedLiteralBoolean class attributes and methods

# uml_TracedQualifierValue class attributes and methods

# uml_TracedOperationTemplateParameter class attributes and methods

# uml_TracedReadLinkObjectEndQualifierAction class attributes and methods

# uml_TracedTemplateParameterSubstitution class attributes and methods

# uml_TracedExtend class attributes and methods

# uml_TracedReadVariableAction class attributes and methods

# IntermediateActivities_TracedDecisionNodeActivation class attributes and methods

# uml_TracedProfileApplication class attributes and methods

# uml_TracedInitialNode class attributes and methods

# uml_TracedLiteralInteger class attributes and methods

# uml_TracedClearVariableAction class attributes and methods

# uml_TracedActionInputPin class attributes and methods

# uml_TracedTemplateParameter class attributes and methods

# uml_TracedConnectorEnd class attributes and methods

# uml_TracedMessageOccurrenceSpecification class attributes and methods

# uml_TracedDurationConstraint class attributes and methods

# uml_TracedImage class attributes and methods

# uml_TracedIntervalConstraint class attributes and methods

# uml_TracedTrigger class attributes and methods

# uml_TracedCallOperationAction class attributes and methods

# uml_TracedProfile class attributes and methods

# uml_TracedInterval class attributes and methods

# IntermediateActivities_TracedForkNodeActivation class attributes and methods

# uml_TracedProtocolStateMachine class attributes and methods

# uml_TracedOutputPin class attributes and methods

# uml_TracedInstanceSpecification class attributes and methods

# uml_TracedValuePin class attributes and methods

# IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution class attributes and methods

# uml_TracedReadIsClassifiedObjectAction class attributes and methods

# uml_TracedInterruptibleActivityRegion class attributes and methods

# uml_TracedDestroyLinkAction class attributes and methods

# IntermediateActivities_TracedActivityParameterNodeActivation class attributes and methods

# uml_TracedDecisionNode class attributes and methods

# uml_TracedValueSpecificationAction class attributes and methods

# uml_TracedRegion class attributes and methods

# uml_TracedPseudostate class attributes and methods

# uml_TracedUseCase class attributes and methods

# uml_TracedFinalState class attributes and methods

# IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution class attributes and methods

# uml_TracedInteractionOperand class attributes and methods

# uml_TracedInformationFlow class attributes and methods

# uml_TracedDependency class attributes and methods

# uml_TracedTimeExpression class attributes and methods

# uml_TracedReplyAction class attributes and methods

# IntermediateActions_TracedCreateObjectActionActivation class attributes and methods

# uml_TracedCombinedFragment class attributes and methods

# uml_TracedClause class attributes and methods

# uml_TracedInstanceValue class attributes and methods

# uml_TracedTransition class attributes and methods

# uml_TracedLinkEndData class attributes and methods

# uml_TracedManifestation class attributes and methods

# uml_TracedReadExtentAction class attributes and methods

# BasicActions_TracedInputPinActivation class attributes and methods

# uml_TracedObjectFlow class attributes and methods

# uml_TracedChangeEvent class attributes and methods

# uml_TracedDestroyObjectAction class attributes and methods

# uml_TracedNode class attributes and methods

# uml_TracedPackageMerge class attributes and methods

# uml_TracedModel class attributes and methods

# uml_TracedForkNode class attributes and methods

# uml_TracedReception class attributes and methods

# uml_TracedRaiseExceptionAction class attributes and methods

# uml_TracedSignal class attributes and methods

# uml_TracedComment class attributes and methods

# uml_TracedLiteralNull class attributes and methods

# uml_TracedExpansionNode class attributes and methods

# uml_TracedControlFlow class attributes and methods

# uml_TracedOperation class attributes and methods

# uml_TracedAddVariableValueAction class attributes and methods

# uml_TracedClearAssociationAction class attributes and methods

# uml_TracedTestIdentityAction class attributes and methods

# uml_TracedExceptionHandler class attributes and methods

# uml_TracedPackageImport class attributes and methods

# uml_TracedExecutionOccurrenceSpecification class attributes and methods

# uml_TracedLiteralReal class attributes and methods

# uml_TracedRemoveVariableValueAction class attributes and methods

# uml_TracedVariable class attributes and methods

# uml_TracedInteractionUse class attributes and methods

# uml_TracedAssociation class attributes and methods

# uml_TracedStateInvariant class attributes and methods

# uml_TracedGeneralOrdering class attributes and methods

# uml_TracedCallBehaviorAction class attributes and methods

# uml_TracedReclassifyObjectAction class attributes and methods

# uml_TracedDevice class attributes and methods

# uml_TracedSubstitution class attributes and methods

# uml_TracedGate class attributes and methods

# uml_TracedReadSelfAction class attributes and methods

# uml_TracedAcceptCallAction class attributes and methods

# uml_TracedActivity class attributes and methods

# uml_TracedConnectionPointReference class attributes and methods

# uml_TracedActionExecutionSpecification class attributes and methods

# uml_TracedLinkEndCreationData class attributes and methods

# uml_TracedTemplateBinding class attributes and methods

# uml_TracedOpaqueExpression class attributes and methods

# uml_TracedFunctionBehavior class attributes and methods

# uml_TracedClearStructuralFeatureAction class attributes and methods

# Kernel_TracedLiteralIntegerEvaluation class attributes and methods

# uml_TracedUnmarshallAction class attributes and methods

# uml_TracedCentralBufferNode class attributes and methods

# umlTrace_Kernel_TracedObject class attributes and methods

# TracedExtensionalValue class attributes and methods

# uml_TracedDeploymentSpecification class attributes and methods

# uml_TracedActor class attributes and methods

# uml_TracedBehaviorExecutionSpecification class attributes and methods

# umlTrace_Kernel_TracedEvaluation class attributes and methods

# umlTrace_Kernel_TracedBooleanValue class attributes and methods

# umlTrace_Kernel_TracedLiteralBooleanEvaluation class attributes and methods

# TracedLiteralEvaluation class attributes and methods

# umlTrace_Kernel_TracedStructuredValue class attributes and methods

# umlTrace_Kernel_TracedReference class attributes and methods

# TracedStructuredValue class attributes and methods

# umlTrace_Kernel_TracedIntegerValue class attributes and methods

# TracedPrimitiveValue class attributes and methods

# umlTrace_Kernel_TracedLiteralEvaluation class attributes and methods

# TracedEvaluation class attributes and methods

# umlTrace_Kernel_TracedValue class attributes and methods

# TracedSemanticVisitor class attributes and methods

# umlTrace_Kernel_TracedPrimitiveValue class attributes and methods

# TracedValue class attributes and methods

# umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution class attributes and methods

# TracedExecution class attributes and methods

# umlTrace_BasicBehaviors_TracedParameterValue class attributes and methods

# umlTrace_BasicBehaviors_TracedExecution class attributes and methods

# TracedObject class attributes and methods

# umlTrace_Kernel_TracedCompoundValue class attributes and methods

# umlTrace_Kernel_TracedFeatureValue class attributes and methods

# umlTrace_Kernel_TracedExtensionalValue class attributes and methods

# TracedCompoundValue class attributes and methods

# umlTrace_Kernel_TracedLiteralIntegerEvaluation class attributes and methods

# umlTrace_IntermediateActivities_TracedMergeNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedControlToken class attributes and methods

# umlTrace_IntermediateActivities_TracedObjectToken class attributes and methods

# umlTrace_IntermediateActivities_TracedDecisionNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedForkedToken class attributes and methods

# TracedToken class attributes and methods

# umlTrace_IntermediateActivities_TracedJoinNodeActivation class attributes and methods

# TracedControlNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedInitialNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedObjectNodeActivation class attributes and methods

# TracedActivityNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedForkNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedToken class attributes and methods

# umlTrace_IntermediateActivities_TracedOffer class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation class attributes and methods

# TracedObjectNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityEdgeInstance class attributes and methods

# umlTrace_Loci_TracedSemanticVisitor class attributes and methods

# umlTrace_Loci_TracedExecutor class attributes and methods

# umlTrace_Loci_TracedExecutionEnvironment class attributes and methods

# umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation class attributes and methods

# TracedActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedValueSpecificationActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation class attributes and methods

# TracedStructuralFeatureActionActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedControlNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityExecution class attributes and methods

# umlTrace_Loci_TracedExecutionFactory class attributes and methods

# umlTrace_Loci_TracedLocus class attributes and methods

# umlTrace_BasicActions_TracedCallActionActivation class attributes and methods

# TracedInvocationActionActivation class attributes and methods

# umlTrace_BasicActions_TracedPinActivation class attributes and methods

# umlTrace_BasicActions_TracedInputPinActivation class attributes and methods

# umlTrace_BasicActions_TracedInvocationActionActivation class attributes and methods

# umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution class attributes and methods

# TracedOpaqueBehaviorExecution class attributes and methods

# umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation class attributes and methods

# TracedWriteStructuralFeatureActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedCreateObjectActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation class attributes and methods

# umlTrace_BasicActions_TracedActionActivation class attributes and methods

# umlTrace_BasicActions_TracedOutputPinActivation class attributes and methods

# TracedPinActivation class attributes and methods

# umlTrace_BasicActions_TracedCallBehaviorActionActivation class attributes and methods

# TracedCallActionActivation class attributes and methods

# umlTrace_BasicActions_TracedOpaqueActionActivation class attributes and methods

# umlTrace_uml_TracedOpaqueAction class attributes and methods

# TracedAction class attributes and methods

# uml_umlTrace_OpaqueAction class attributes and methods

# umlTrace_uml_TracedDataType class attributes and methods

# TracedClassifier class attributes and methods

# uml_umlTrace_DataType class attributes and methods

# umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution class attributes and methods

# umlTrace_uml_TracedCommunicationPath class attributes and methods

# TracedAssociation class attributes and methods

# umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution class attributes and methods

# umlTrace_uml_TracedLinkAction class attributes and methods

# umlTrace_Input_TracedInputParameterValues class attributes and methods

# umlTrace_uml_TracedStructuralFeature class attributes and methods

# uml_TracedFeature class attributes and methods

# uml_TracedTypedElement class attributes and methods

# uml_TracedMultiplicityElement class attributes and methods

# umlTrace_uml_TracedConnector class attributes and methods

# TracedFeature class attributes and methods

# uml_TracedBehavior class attributes and methods

# uml_umlTrace_Connector class attributes and methods

# uml_umlTrace_Property class attributes and methods

# umlTrace_uml_TracedContinuation class attributes and methods

# TracedInteractionFragment class attributes and methods

# uml_umlTrace_Continuation class attributes and methods

# umlTrace_uml_TracedRemoveStructuralFeatureValueAction class attributes and methods

# umlTrace_uml_TracedProperty class attributes and methods

# uml_TracedConnectableElement class attributes and methods

# uml_TracedDeploymentTarget class attributes and methods

# uml_umlTrace_Artifact class attributes and methods

# umlTrace_uml_TracedTimeConstraint class attributes and methods

# TracedIntervalConstraint class attributes and methods

# umlTrace_uml_TracedInterfaceRealization class attributes and methods

# TracedRealization class attributes and methods

# uml_TracedBehavioredClassifier class attributes and methods

# umlTrace_uml_TracedObjectNode class attributes and methods

# TracedWriteStructuralFeatureAction class attributes and methods

# uml_umlTrace_RemoveStructuralFeatureValueAction class attributes and methods

# umlTrace_uml_TracedSendSignalAction class attributes and methods

# TracedInvocationAction class attributes and methods

# uml_umlTrace_SendSignalAction class attributes and methods

# umlTrace_uml_TracedOpaqueBehavior class attributes and methods

# TracedBehavior class attributes and methods

# umlTrace_uml_TracedArtifact class attributes and methods

# uml_TracedClassifier class attributes and methods

# uml_TracedDeployedArtifact class attributes and methods

# uml_umlTrace_AcceptEventAction class attributes and methods

# umlTrace_uml_TracedEnumerationLiteral class attributes and methods

# TracedInstanceSpecification class attributes and methods

# umlTrace_uml_TracedAddStructuralFeatureValueAction class attributes and methods

# uml_umlTrace_AddStructuralFeatureValueAction class attributes and methods

# umlTrace_uml_TracedReadLinkAction class attributes and methods

# TracedLinkAction class attributes and methods

# umlTrace_uml_TracedActivityFinalNode class attributes and methods

# TracedFinalNode class attributes and methods

# uml_umlTrace_ActivityFinalNode class attributes and methods

# umlTrace_uml_TracedDurationObservation class attributes and methods

# TracedObservation class attributes and methods

# uml_TracedNamedElement class attributes and methods

# uml_umlTrace_DurationObservation class attributes and methods

# umlTrace_uml_TracedAcceptEventAction class attributes and methods

# umlTrace_uml_TracedDataStoreNode class attributes and methods

# TracedCentralBufferNode class attributes and methods

# umlTrace_uml_TracedFlowFinalNode class attributes and methods

# uml_umlTrace_FlowFinalNode class attributes and methods

# umlTrace_uml_TracedInteractionFragment class attributes and methods

# TracedNamedElement class attributes and methods

# umlTrace_uml_TracedClassifier class attributes and methods

# uml_TracedNamespace class attributes and methods

# uml_TracedRedefinableElement class attributes and methods

# uml_TracedType class attributes and methods

# uml_TracedTemplateableElement class attributes and methods

# uml_umlTrace_ReadLinkAction class attributes and methods

# umlTrace_uml_TracedExpression class attributes and methods

# TracedValueSpecification class attributes and methods

# uml_umlTrace_Expression class attributes and methods

# umlTrace_uml_TracedConsiderIgnoreFragment class attributes and methods

# TracedCombinedFragment class attributes and methods

# umlTrace_uml_TracedInformationItem class attributes and methods

# uml_umlTrace_Collaboration class attributes and methods

# umlTrace_uml_TracedMessageEnd class attributes and methods

# umlTrace_uml_TracedTemplateSignature class attributes and methods

# TracedElement class attributes and methods

# uml_umlTrace_InformationItem class attributes and methods

# umlTrace_uml_TracedCollaboration class attributes and methods

# uml_TracedStructuredClassifier class attributes and methods

# umlTrace_uml_TracedPort class attributes and methods

# TracedProperty class attributes and methods

# umlTrace_uml_TracedTimeInterval class attributes and methods

# TracedInterval class attributes and methods

# umlTrace_uml_TracedAction class attributes and methods

# TracedExecutableNode class attributes and methods

# uml_umlTrace_TemplateSignature class attributes and methods

# umlTrace_uml_TracedBroadcastSignalAction class attributes and methods

# uml_umlTrace_BroadcastSignalAction class attributes and methods

# umlTrace_uml_TracedDeployment class attributes and methods

# TracedDependency class attributes and methods

# umlTrace_uml_TracedDirectedRelationship class attributes and methods

# TracedRelationship class attributes and methods

# umlTrace_uml_TracedTimeEvent class attributes and methods

# TracedEvent class attributes and methods

# uml_umlTrace_TimeEvent class attributes and methods

# umlTrace_uml_TracedPackageableElement class attributes and methods

# uml_TracedParameterableElement class attributes and methods

# umlTrace_uml_TracedType class attributes and methods

# TracedPackageableElement class attributes and methods

# umlTrace_uml_TracedExtension class attributes and methods

# umlTrace_uml_TracedProtocolTransition class attributes and methods

# TracedTransition class attributes and methods

# umlTrace_uml_TracedPackage class attributes and methods

# uml_TracedPackageableElement class attributes and methods

# umlTrace_uml_TracedConstraint class attributes and methods

# uml_umlTrace_Constraint class attributes and methods

# umlTrace_uml_TracedMultiplicityElement class attributes and methods

# umlTrace_uml_TracedLiteralSpecification class attributes and methods

# uml_umlTrace_Package class attributes and methods

# umlTrace_uml_TracedBehavioredClassifier class attributes and methods

# umlTrace_uml_TracedStructuralFeatureAction class attributes and methods

# uml_umlTrace_ReduceAction class attributes and methods

# umlTrace_uml_TracedInputPin class attributes and methods

# TracedPin class attributes and methods

# uml_umlTrace_InputPin class attributes and methods

# umlTrace_uml_TracedSequenceNode class attributes and methods

# TracedStructuredActivityNode class attributes and methods

# uml_TracedExecutableNode class attributes and methods

# umlTrace_uml_TracedFeature class attributes and methods

# TracedRedefinableElement class attributes and methods

# umlTrace_uml_TracedInteractionConstraint class attributes and methods

# TracedConstraint class attributes and methods

# umlTrace_uml_TracedGeneralizationSet class attributes and methods

# uml_umlTrace_GeneralizationSet class attributes and methods

# umlTrace_uml_TracedReduceAction class attributes and methods

# umlTrace_uml_TracedComponentRealization class attributes and methods

# umlTrace_uml_TracedAssociationClass class attributes and methods

# umlTrace_uml_TracedSlot class attributes and methods

# umlTrace_uml_TracedWriteStructuralFeatureAction class attributes and methods

# TracedStructuralFeatureAction class attributes and methods

# umlTrace_uml_TracedElement class attributes and methods

# TracedEModelElement class attributes and methods

# umlTrace_uml_TracedJoinNode class attributes and methods

# TracedControlNode class attributes and methods

# uml_umlTrace_JoinNode class attributes and methods

# umlTrace_uml_TracedStartObjectBehaviorAction class attributes and methods

# TracedCallAction class attributes and methods

# uml_umlTrace_StartObjectBehaviorAction class attributes and methods

# umlTrace_uml_TracedElementImport class attributes and methods

# TracedDirectedRelationship class attributes and methods

# uml_umlTrace_ElementImport class attributes and methods

# uml_umlTrace_Slot class attributes and methods

# umlTrace_uml_TracedSignalEvent class attributes and methods

# TracedMessageEvent class attributes and methods

# uml_umlTrace_SignalEvent class attributes and methods

# umlTrace_uml_TracedExtensionPoint class attributes and methods

# uml_umlTrace_ExtensionPoint class attributes and methods

# uml_umlTrace_OccurrenceSpecification class attributes and methods

# umlTrace_uml_TracedStringExpression class attributes and methods

# umlTrace_uml_TracedDeployedArtifact class attributes and methods

# umlTrace_uml_TracedStereotype class attributes and methods

# TracedClass class attributes and methods

# umlTrace_uml_TracedInterface class attributes and methods

# umlTrace_uml_TracedCreateObjectAction class attributes and methods

# uml_umlTrace_CreateObjectAction class attributes and methods

# umlTrace_uml_TracedExecutionEnvironment class attributes and methods

# TracedNode class attributes and methods

# umlTrace_uml_TracedOccurrenceSpecification class attributes and methods

# umlTrace_uml_TracedConditionalNode class attributes and methods

# umlTrace_uml_TracedReadLinkObjectEndAction class attributes and methods

# uml_umlTrace_Interface class attributes and methods

# uml_umlTrace_ReadLinkObjectEndAction class attributes and methods

# umlTrace_uml_TracedAnyReceiveEvent class attributes and methods

# uml_umlTrace_AnyReceiveEvent class attributes and methods

# umlTrace_uml_TracedNamedElement class attributes and methods

# umlTrace_uml_TracedComponent class attributes and methods

# umlTrace_uml_TracedLiteralString class attributes and methods

# TracedLiteralSpecification class attributes and methods

# uml_umlTrace_LiteralString class attributes and methods

# umlTrace_uml_TracedRealization class attributes and methods

# TracedAbstraction class attributes and methods

# umlTrace_uml_TracedStartClassifierBehaviorAction class attributes and methods

# umlTrace_uml_TracedExtensionEnd class attributes and methods

# umlTrace_uml_TracedStateMachine class attributes and methods

# umlTrace_uml_TracedValueSpecification class attributes and methods

# umlTrace_uml_TracedInteraction class attributes and methods

# uml_TracedInteractionFragment class attributes and methods

# uml_TracedAction class attributes and methods

# uml_umlTrace_SendObjectAction class attributes and methods

# umlTrace_uml_TracedLifeline class attributes and methods

# uml_umlTrace_StartClassifierBehaviorAction class attributes and methods

# umlTrace_uml_TracedMessageEvent class attributes and methods

# umlTrace_uml_TracedCallEvent class attributes and methods

# uml_umlTrace_CallEvent class attributes and methods

# umlTrace_uml_TracedConnectableElementTemplateParameter class attributes and methods

# TracedTemplateParameter class attributes and methods

# umlTrace_uml_TracedRelationship class attributes and methods

# umlTrace_uml_TracedSendObjectAction class attributes and methods

# umlTrace_uml_TracedExpansionRegion class attributes and methods

# umlTrace_uml_TracedWriteVariableAction class attributes and methods

# TracedVariableAction class attributes and methods

# uml_umlTrace_Lifeline class attributes and methods

# umlTrace_uml_TracedExecutionSpecification class attributes and methods

# umlTrace_uml_TracedTimeObservation class attributes and methods

# uml_umlTrace_TimeObservation class attributes and methods

# umlTrace_uml_TracedCreateLinkObjectAction class attributes and methods

# TracedCreateLinkAction class attributes and methods

# umlTrace_uml_TracedProtocolConformance class attributes and methods

# uml_umlTrace_ProtocolConformance class attributes and methods

# umlTrace_uml_TracedLoopNode class attributes and methods

# umlTrace_uml_TracedPrimitiveType class attributes and methods

# TracedDataType class attributes and methods

# umlTrace_uml_TracedEnumeration class attributes and methods

# umlTrace_uml_TracedCollaborationUse class attributes and methods

# uml_umlTrace_CollaborationUse class attributes and methods

# umlTrace_uml_TracedActivityPartition class attributes and methods

# TracedActivityGroup class attributes and methods

# ActivityContent class attributes and methods

# uml_TracedActivityGroup class attributes and methods

# uml_umlTrace_ActivityPartition class attributes and methods

# umlTrace_uml_TracedVariableAction class attributes and methods

# umlTrace_uml_TracedLinkEndDestructionData class attributes and methods

# TracedLinkEndData class attributes and methods

# umlTrace_uml_TracedDurationInterval class attributes and methods

# umlTrace_uml_TracedInclude class attributes and methods

# uml_TracedDirectedRelationship class attributes and methods

# uml_umlTrace_Include class attributes and methods

# umlTrace_uml_TracedActivityNode class attributes and methods

# umlTrace_uml_TracedDestructionOccurrenceSpecification class attributes and methods

# TracedMessageOccurrenceSpecification class attributes and methods

# umlTrace_uml_TracedState class attributes and methods

# uml_TracedVertex class attributes and methods

# umlTrace_uml_TracedBehavior class attributes and methods

# uml_TracedBehavioralFeature class attributes and methods

# uml_umlTrace_State class attributes and methods

# umlTrace_uml_TracedCallAction class attributes and methods

# umlTrace_uml_TracedTemplateableElement class attributes and methods

# uml_umlTrace_ActivityParameterNode class attributes and methods

# umlTrace_uml_TracedParameterSet class attributes and methods

# umlTrace_uml_TracedClassifierTemplateParameter class attributes and methods

# umlTrace_uml_TracedActivityParameterNode class attributes and methods

# TracedObjectNode class attributes and methods

# uml_umlTrace_Class class attributes and methods

# umlTrace_uml_TracedUsage class attributes and methods

# umlTrace_uml_TracedLiteralUnlimitedNatural class attributes and methods

# uml_umlTrace_LiteralUnlimitedNatural class attributes and methods

# uml_umlTrace_ParameterSet class attributes and methods

# umlTrace_uml_TracedDuration class attributes and methods

# uml_TracedObservation class attributes and methods

# uml_umlTrace_Duration class attributes and methods

# umlTrace_uml_TracedClass class attributes and methods

# uml_TracedEncapsulatedClassifier class attributes and methods

# umlTrace_uml_TracedReadStructuralFeatureAction class attributes and methods

# uml_umlTrace_ReadStructuralFeatureAction class attributes and methods

# umlTrace_uml_TracedMergeNode class attributes and methods

# uml_umlTrace_MergeNode class attributes and methods

# umlTrace_uml_TracedStructuredActivityNode class attributes and methods

# uml_umlTrace_StructuredActivityNode class attributes and methods

# umlTrace_uml_TracedAbstraction class attributes and methods

# uml_umlTrace_Generalization class attributes and methods

# umlTrace_uml_TracedPartDecomposition class attributes and methods

# TracedInteractionUse class attributes and methods

# umlTrace_uml_TracedTypedElement class attributes and methods

# umlTrace_uml_TracedRedefinableTemplateSignature class attributes and methods

# umlTrace_uml_TracedCreateLinkAction class attributes and methods

# TracedWriteLinkAction class attributes and methods

# uml_umlTrace_CreateLinkAction class attributes and methods

# umlTrace_uml_TracedGeneralization class attributes and methods

# uml_umlTrace_TemplateParameterSubstitution class attributes and methods

# umlTrace_uml_TracedExtend class attributes and methods

# umlTrace_uml_TracedOperationTemplateParameter class attributes and methods

# umlTrace_uml_TracedReadLinkObjectEndQualifierAction class attributes and methods

# uml_umlTrace_ReadLinkObjectEndQualifierAction class attributes and methods

# umlTrace_uml_TracedTemplateParameterSubstitution class attributes and methods

# uml_TracedMessageEnd class attributes and methods

# uml_umlTrace_Extend class attributes and methods

# umlTrace_uml_TracedReadVariableAction class attributes and methods

# uml_umlTrace_ReadVariableAction class attributes and methods

# umlTrace_uml_TracedMessage class attributes and methods

# umlTrace_uml_TracedProfileApplication class attributes and methods

# uml_umlTrace_Message class attributes and methods

# umlTrace_uml_TracedLiteralBoolean class attributes and methods

# uml_umlTrace_LiteralBoolean class attributes and methods

# umlTrace_uml_TracedQualifierValue class attributes and methods

# uml_umlTrace_QualifierValue class attributes and methods

# umlTrace_uml_TracedInitialNode class attributes and methods

# uml_umlTrace_InitialNode class attributes and methods

# umlTrace_uml_TracedLiteralInteger class attributes and methods

# uml_umlTrace_LiteralInteger class attributes and methods

# umlTrace_uml_TracedClearVariableAction class attributes and methods

# uml_umlTrace_ClearVariableAction class attributes and methods

# uml_umlTrace_TemplateParameter class attributes and methods

# umlTrace_uml_TracedConnectorEnd class attributes and methods

# TracedMultiplicityElement class attributes and methods

# uml_umlTrace_ProfileApplication class attributes and methods

# umlTrace_uml_TracedParameterableElement class attributes and methods

# umlTrace_uml_TracedTemplateParameter class attributes and methods

# uml_umlTrace_Parameter class attributes and methods

# umlTrace_uml_TracedActionInputPin class attributes and methods

# TracedInputPin class attributes and methods

# umlTrace_uml_TracedTrigger class attributes and methods

# uml_TracedEvent class attributes and methods

# uml_umlTrace_ConnectorEnd class attributes and methods

# umlTrace_uml_TracedMessageOccurrenceSpecification class attributes and methods

# umlTrace_uml_TracedDurationConstraint class attributes and methods

# umlTrace_uml_TracedImage class attributes and methods

# uml_umlTrace_Image class attributes and methods

# umlTrace_uml_TracedEncapsulatedClassifier class attributes and methods

# TracedStructuredClassifier class attributes and methods

# umlTrace_uml_TracedParameter class attributes and methods

# uml_umlTrace_Interval class attributes and methods

# umlTrace_uml_TracedIntervalConstraint class attributes and methods

# umlTrace_uml_TracedInstanceSpecification class attributes and methods

# uml_umlTrace_Trigger class attributes and methods

# umlTrace_uml_TracedCallOperationAction class attributes and methods

# uml_umlTrace_CallOperationAction class attributes and methods

# umlTrace_uml_TracedProfile class attributes and methods

# TracedPackage class attributes and methods

# umlTrace_uml_TracedInterval class attributes and methods

# uml_umlTrace_ReadIsClassifiedObjectAction class attributes and methods

# umlTrace_uml_TracedProtocolStateMachine class attributes and methods

# TracedStateMachine class attributes and methods

# umlTrace_uml_TracedOutputPin class attributes and methods

# uml_umlTrace_OutputPin class attributes and methods

# uml_umlTrace_InstanceSpecification class attributes and methods

# umlTrace_uml_TracedValuePin class attributes and methods

# umlTrace_uml_TracedReadIsClassifiedObjectAction class attributes and methods

# uml_umlTrace_ValueSpecificationAction class attributes and methods

# umlTrace_uml_TracedRegion class attributes and methods

# umlTrace_uml_TracedDecisionNode class attributes and methods

# uml_umlTrace_DecisionNode class attributes and methods

# umlTrace_uml_TracedValueSpecificationAction class attributes and methods

# uml_umlTrace_InterruptibleActivityRegion class attributes and methods

# umlTrace_uml_TracedDestroyLinkAction class attributes and methods

# uml_umlTrace_DestroyLinkAction class attributes and methods

# umlTrace_uml_TracedFinalState class attributes and methods

# TracedState class attributes and methods

# umlTrace_uml_TracedActivityGroup class attributes and methods

# uml_umlTrace_Region class attributes and methods

# umlTrace_uml_TracedInterruptibleActivityRegion class attributes and methods

# uml_umlTrace_InteractionOperand class attributes and methods

# umlTrace_uml_TracedActivityEdge class attributes and methods

# umlTrace_uml_TracedInteractionOperand class attributes and methods

# umlTrace_uml_TracedInformationFlow class attributes and methods

# uml_umlTrace_Pseudostate class attributes and methods

# umlTrace_uml_TracedControlNode class attributes and methods

# TracedActivityNode class attributes and methods

# umlTrace_uml_TracedUseCase class attributes and methods

# TracedBehavioredClassifier class attributes and methods

# uml_TracedRelationship class attributes and methods

# uml_umlTrace_InformationFlow class attributes and methods

# umlTrace_uml_TracedPseudostate class attributes and methods

# TracedVertex class attributes and methods

# umlTrace_uml_TracedCombinedFragment class attributes and methods

# uml_umlTrace_CombinedFragment class attributes and methods

# uml_umlTrace_UseCase class attributes and methods

# umlTrace_uml_TracedReplyAction class attributes and methods

# uml_umlTrace_ReplyAction class attributes and methods

# umlTrace_uml_TracedDependency class attributes and methods

# umlTrace_uml_TracedWriteLinkAction class attributes and methods

# umlTrace_uml_TracedClause class attributes and methods

# uml_umlTrace_Clause class attributes and methods

# umlTrace_uml_TracedInstanceValue class attributes and methods

# uml_umlTrace_InstanceValue class attributes and methods

# uml_umlTrace_ReadExtentAction class attributes and methods

# umlTrace_uml_TracedTransition class attributes and methods

# uml_umlTrace_Dependency class attributes and methods

# umlTrace_uml_TracedTimeExpression class attributes and methods

# uml_umlTrace_TimeExpression class attributes and methods

# umlTrace_uml_TracedManifestation class attributes and methods

# umlTrace_uml_TracedReadExtentAction class attributes and methods

# uml_umlTrace_LinkEndData class attributes and methods

# umlTrace_uml_TracedNode class attributes and methods

# uml_umlTrace_Transition class attributes and methods

# umlTrace_uml_TracedLinkEndData class attributes and methods

# uml_umlTrace_ChangeEvent class attributes and methods

# umlTrace_uml_TracedRedefinableElement class attributes and methods

# umlTrace_uml_TracedPackageMerge class attributes and methods

# uml_umlTrace_PackageMerge class attributes and methods

# umlTrace_uml_TracedModel class attributes and methods

# umlTrace_uml_TracedObjectFlow class attributes and methods

# TracedActivityEdge class attributes and methods

# uml_umlTrace_ObjectFlow class attributes and methods

# umlTrace_uml_TracedEvent class attributes and methods

# umlTrace_uml_TracedChangeEvent class attributes and methods

# uml_umlTrace_Comment class attributes and methods

# umlTrace_uml_TracedStructuredClassifier class attributes and methods

# umlTrace_uml_TracedDestroyObjectAction class attributes and methods

# uml_umlTrace_DestroyObjectAction class attributes and methods

# umlTrace_uml_TracedForkNode class attributes and methods

# uml_umlTrace_ForkNode class attributes and methods

# umlTrace_uml_TracedFinalNode class attributes and methods

# umlTrace_uml_TracedSignal class attributes and methods

# uml_umlTrace_Signal class attributes and methods

# umlTrace_uml_TracedComment class attributes and methods

# uml_umlTrace_Reception class attributes and methods

# umlTrace_uml_TracedRaiseExceptionAction class attributes and methods

# uml_umlTrace_RaiseExceptionAction class attributes and methods

# umlTrace_uml_TracedLiteralNull class attributes and methods

# uml_umlTrace_LiteralNull class attributes and methods

# umlTrace_uml_TracedExpansionNode class attributes and methods

# uml_umlTrace_ExpansionNode class attributes and methods

# umlTrace_uml_TracedReception class attributes and methods

# TracedBehavioralFeature class attributes and methods

# uml_umlTrace_ClearAssociationAction class attributes and methods

# umlTrace_uml_TracedPin class attributes and methods

# uml_TracedObjectNode class attributes and methods

# umlTrace_uml_TracedTestIdentityAction class attributes and methods

# umlTrace_uml_TracedBehavioralFeature class attributes and methods

# umlTrace_uml_TracedAddVariableValueAction class attributes and methods

# TracedWriteVariableAction class attributes and methods

# uml_umlTrace_AddVariableValueAction class attributes and methods

# umlTrace_uml_TracedClearAssociationAction class attributes and methods

# uml_umlTrace_TestIdentityAction class attributes and methods

# umlTrace_uml_TracedControlFlow class attributes and methods

# uml_umlTrace_ControlFlow class attributes and methods

# umlTrace_uml_TracedOperation class attributes and methods

# umlTrace_uml_TracedObservation class attributes and methods

# umlTrace_uml_TracedNamespace class attributes and methods

# uml_umlTrace_Operation class attributes and methods

# umlTrace_uml_TracedConnectableElement class attributes and methods

# umlTrace_uml_TracedVertex class attributes and methods

# umlTrace_uml_TracedPackageImport class attributes and methods

# umlTrace_uml_TracedInteractionUse class attributes and methods

# uml_umlTrace_PackageImport class attributes and methods

# umlTrace_uml_TracedExecutionOccurrenceSpecification class attributes and methods

# TracedOccurrenceSpecification class attributes and methods

# uml_TracedExecutionSpecification class attributes and methods

# umlTrace_uml_TracedExceptionHandler class attributes and methods

# uml_umlTrace_ExceptionHandler class attributes and methods

# umlTrace_uml_TracedVariable class attributes and methods

# uml_umlTrace_Variable class attributes and methods

# uml_umlTrace_Association class attributes and methods

# umlTrace_uml_TracedStateInvariant class attributes and methods

# uml_umlTrace_StateInvariant class attributes and methods

# uml_umlTrace_InteractionUse class attributes and methods

# umlTrace_uml_TracedAssociation class attributes and methods

# umlTrace_uml_TracedDevice class attributes and methods

# umlTrace_uml_TracedSubstitution class attributes and methods

# umlTrace_uml_TracedLiteralReal class attributes and methods

# uml_umlTrace_LiteralReal class attributes and methods

# umlTrace_uml_TracedInvocationAction class attributes and methods

# umlTrace_uml_TracedRemoveVariableValueAction class attributes and methods

# uml_umlTrace_RemoveVariableValueAction class attributes and methods

# uml_umlTrace_ReclassifyObjectAction class attributes and methods

# umlTrace_uml_TracedGate class attributes and methods

# TracedMessageEnd class attributes and methods

# uml_umlTrace_Gate class attributes and methods

# umlTrace_uml_TracedDeploymentTarget class attributes and methods

# umlTrace_uml_TracedGeneralOrdering class attributes and methods

# uml_umlTrace_GeneralOrdering class attributes and methods

# umlTrace_uml_TracedCallBehaviorAction class attributes and methods

# uml_umlTrace_CallBehaviorAction class attributes and methods

# umlTrace_uml_TracedReclassifyObjectAction class attributes and methods

# umlTrace_uml_TracedConnectionPointReference class attributes and methods

# umlTrace_uml_TracedActivity class attributes and methods

# umlTrace_uml_TracedLinkEndCreationData class attributes and methods

# umlTrace_uml_TracedTemplateBinding class attributes and methods

# uml_umlTrace_ConnectionPointReference class attributes and methods

# umlTrace_uml_TracedActionExecutionSpecification class attributes and methods

# TracedExecutionSpecification class attributes and methods

# uml_umlTrace_ActionExecutionSpecification class attributes and methods

# umlTrace_uml_TracedReadSelfAction class attributes and methods

# uml_umlTrace_ReadSelfAction class attributes and methods

# umlTrace_uml_TracedAcceptCallAction class attributes and methods

# TracedAcceptEventAction class attributes and methods

# umlTrace_uml_TracedActor class attributes and methods

# uml_umlTrace_Actor class attributes and methods

# umlTrace_uml_TracedBehaviorExecutionSpecification class attributes and methods

# uml_umlTrace_BehaviorExecutionSpecification class attributes and methods

# umlTrace_uml_TracedExecutableNode class attributes and methods

# uml_umlTrace_TemplateBinding class attributes and methods

# umlTrace_uml_TracedClearStructuralFeatureAction class attributes and methods

# uml_umlTrace_ClearStructuralFeatureAction class attributes and methods

# umlTrace_uml_TracedOpaqueExpression class attributes and methods

# uml_umlTrace_OpaqueExpression class attributes and methods

# umlTrace_uml_TracedFunctionBehavior class attributes and methods

# TracedOpaqueBehavior class attributes and methods

# umlTrace_uml_TracedDeploymentSpecification class attributes and methods

# TracedArtifact class attributes and methods

# umlTrace_uml_TracedUnmarshallAction class attributes and methods

# uml_umlTrace_UnmarshallAction class attributes and methods

# umlTrace_uml_TracedCentralBufferNode class attributes and methods

# uml_umlTrace_CentralBufferNode class attributes and methods

# umlTrace_ecore_TracedEModelElement class attributes and methods

# ecore_umlTrace_EAnnotation class attributes and methods

# Relationships
statesTrace0: BinaryAssociation = BinaryAssociation(
    name="statesTrace0",
    ends={
        Property(name="umlTrace_State", type=umlTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Trace", type=umlTrace_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps1: BinaryAssociation = BinaryAssociation(
    name="steps1",
    ends={
        Property(name="Steps", type=umlTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Trace2", type=Steps, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
executionFactory_locus_ExecutionFactory_Values24: BinaryAssociation = BinaryAssociation(
    name="executionFactory_locus_ExecutionFactory_Values24",
    ends={
        Property(name="ExecutionFactory_locus_ExecutionFactory_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states25", type=ExecutionFactory_locus_ExecutionFactory_Value, multiplicity=Multiplicity(0, 9999))
    }
)
locus_factory_Values26: BinaryAssociation = BinaryAssociation(
    name="locus_factory_Values26",
    ends={
        Property(name="Locus_factory_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states27", type=Locus_factory_Value, multiplicity=Multiplicity(0, 9999))
    }
)
locus_extensionalValues_Values28: BinaryAssociation = BinaryAssociation(
    name="locus_extensionalValues_Values28",
    ends={
        Property(name="Locus_extensionalValues_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states29", type=Locus_extensionalValues_Value, multiplicity=Multiplicity(0, 9999))
    }
)
locus_executor_Values30: BinaryAssociation = BinaryAssociation(
    name="locus_executor_Values30",
    ends={
        Property(name="Locus_executor_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states31", type=Locus_executor_Value, multiplicity=Multiplicity(0, 9999))
    }
)
objectNodeActivation_offeredTokenCount_Values32: BinaryAssociation = BinaryAssociation(
    name="objectNodeActivation_offeredTokenCount_Values32",
    ends={
        Property(name="ObjectNodeActivation_offeredTokenCount_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states33", type=ObjectNodeActivation_offeredTokenCount_Value, multiplicity=Multiplicity(0, 9999))
    }
)
tracedObjects3: BinaryAssociation = BinaryAssociation(
    name="tracedObjects3",
    ends={
        Property(name="TracedObjects", type=umlTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Trace4", type=TracedObjects, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
semanticVisitor_runtimeModelElement_Values34: BinaryAssociation = BinaryAssociation(
    name="semanticVisitor_runtimeModelElement_Values34",
    ends={
        Property(name="SemanticVisitor_runtimeModelElement_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states35", type=SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(0, 9999))
    }
)
followingStep5: BinaryAssociation = BinaryAssociation(
    name="followingStep5",
    ends={
        Property(name="SmallStep", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="precedingState", type=SmallStep, multiplicity=Multiplicity(0, 1))
    }
)
startedBigSteps6: BinaryAssociation = BinaryAssociation(
    name="startedBigSteps6",
    ends={
        Property(name="BigStep", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="startingState", type=BigStep, multiplicity=Multiplicity(0, 9999))
    }
)
endedBigSteps7: BinaryAssociation = BinaryAssociation(
    name="endedBigSteps7",
    ends={
        Property(name="BigStep8", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="endingState", type=BigStep, multiplicity=Multiplicity(0, 9999))
    }
)
object_types_Values9: BinaryAssociation = BinaryAssociation(
    name="object_types_Values9",
    ends={
        Property(name="Object_types_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=Object_types_Value, multiplicity=Multiplicity(0, 9999))
    }
)
reference_referent_Values10: BinaryAssociation = BinaryAssociation(
    name="reference_referent_Values10",
    ends={
        Property(name="Reference_referent_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states11", type=Reference_referent_Value, multiplicity=Multiplicity(0, 9999))
    }
)
integerValue_value_IntegerValue_Values12: BinaryAssociation = BinaryAssociation(
    name="integerValue_value_IntegerValue_Values12",
    ends={
        Property(name="IntegerValue_value_IntegerValue_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states13", type=IntegerValue_value_IntegerValue_Value, multiplicity=Multiplicity(0, 9999))
    }
)
forkedToken_remainingOffersCount_Values14: BinaryAssociation = BinaryAssociation(
    name="forkedToken_remainingOffersCount_Values14",
    ends={
        Property(name="ForkedToken_remainingOffersCount_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states15", type=ForkedToken_remainingOffersCount_Value, multiplicity=Multiplicity(0, 9999))
    }
)
forkedToken_baseToken_Values16: BinaryAssociation = BinaryAssociation(
    name="forkedToken_baseToken_Values16",
    ends={
        Property(name="ForkedToken_baseToken_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states17", type=ForkedToken_baseToken_Value, multiplicity=Multiplicity(0, 9999))
    }
)
forkedToken_baseTokenIsWithdrawn_Values18: BinaryAssociation = BinaryAssociation(
    name="forkedToken_baseTokenIsWithdrawn_Values18",
    ends={
        Property(name="ForkedToken_baseTokenIsWithdrawn_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states19", type=ForkedToken_baseTokenIsWithdrawn_Value, multiplicity=Multiplicity(0, 9999))
    }
)
executionFactory_builtInTypes_Values20: BinaryAssociation = BinaryAssociation(
    name="executionFactory_builtInTypes_Values20",
    ends={
        Property(name="ExecutionFactory_builtInTypes_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states21", type=ExecutionFactory_builtInTypes_Value, multiplicity=Multiplicity(0, 9999))
    }
)
executionFactory_primitiveBehaviorPrototypes_Values22: BinaryAssociation = BinaryAssociation(
    name="executionFactory_primitiveBehaviorPrototypes_Values22",
    ends={
        Property(name="ExecutionFactory_primitiveBehaviorPrototypes_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states23", type=ExecutionFactory_primitiveBehaviorPrototypes_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivationGroup_activityExecution_Values52: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivationGroup_activityExecution_Values52",
    ends={
        Property(name="ActivityNodeActivationGroup_activityExecution_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states53", type=ActivityNodeActivationGroup_activityExecution_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivationGroup_edgeInstances_Values54: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivationGroup_edgeInstances_Values54",
    ends={
        Property(name="ActivityNodeActivationGroup_edgeInstances_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states55", type=ActivityNodeActivationGroup_edgeInstances_Value, multiplicity=Multiplicity(0, 9999))
    }
)
executor_locus_Executor_Values56: BinaryAssociation = BinaryAssociation(
    name="executor_locus_Executor_Values56",
    ends={
        Property(name="Executor_locus_Executor_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states57", type=Executor_locus_Executor_Value, multiplicity=Multiplicity(0, 9999))
    }
)
primitiveValue_type_Values58: BinaryAssociation = BinaryAssociation(
    name="primitiveValue_type_Values58",
    ends={
        Property(name="PrimitiveValue_type_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states59", type=PrimitiveValue_type_Value, multiplicity=Multiplicity(0, 9999))
    }
)
parameterValue_values_ParameterValue_Values36: BinaryAssociation = BinaryAssociation(
    name="parameterValue_values_ParameterValue_Values36",
    ends={
        Property(name="ParameterValue_values_ParameterValue_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states37", type=ParameterValue_values_ParameterValue_Value, multiplicity=Multiplicity(0, 9999))
    }
)
parameterValue_parameter_ParameterValue_Values38: BinaryAssociation = BinaryAssociation(
    name="parameterValue_parameter_ParameterValue_Values38",
    ends={
        Property(name="ParameterValue_parameter_ParameterValue_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states39", type=ParameterValue_parameter_ParameterValue_Value, multiplicity=Multiplicity(0, 9999))
    }
)
actionActivation_pinActivations_Values40: BinaryAssociation = BinaryAssociation(
    name="actionActivation_pinActivations_Values40",
    ends={
        Property(name="ActionActivation_pinActivations_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states41", type=ActionActivation_pinActivations_Value, multiplicity=Multiplicity(0, 9999))
    }
)
actionActivation_firing_Values42: BinaryAssociation = BinaryAssociation(
    name="actionActivation_firing_Values42",
    ends={
        Property(name="ActionActivation_firing_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states43", type=ActionActivation_firing_Value, multiplicity=Multiplicity(0, 9999))
    }
)
execution_parameterValues_Values44: BinaryAssociation = BinaryAssociation(
    name="execution_parameterValues_Values44",
    ends={
        Property(name="Execution_parameterValues_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states45", type=Execution_parameterValues_Value, multiplicity=Multiplicity(0, 9999))
    }
)
execution_context_Values46: BinaryAssociation = BinaryAssociation(
    name="execution_context_Values46",
    ends={
        Property(name="Execution_context_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states47", type=Execution_context_Value, multiplicity=Multiplicity(0, 9999))
    }
)
element_semanticVisitor_Values48: BinaryAssociation = BinaryAssociation(
    name="element_semanticVisitor_Values48",
    ends={
        Property(name="Element_semanticVisitor_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states49", type=Element_semanticVisitor_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivationGroup_nodeActivations_Values50: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivationGroup_nodeActivations_Values50",
    ends={
        Property(name="ActivityNodeActivationGroup_nodeActivations_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states51", type=ActivityNodeActivationGroup_nodeActivations_Value, multiplicity=Multiplicity(0, 9999))
    }
)
featureValue_feature_Values78: BinaryAssociation = BinaryAssociation(
    name="featureValue_feature_Values78",
    ends={
        Property(name="FeatureValue_feature_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states79", type=FeatureValue_feature_Value, multiplicity=Multiplicity(0, 9999))
    }
)
featureValue_position_Values80: BinaryAssociation = BinaryAssociation(
    name="featureValue_position_Values80",
    ends={
        Property(name="FeatureValue_position_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states81", type=FeatureValue_position_Value, multiplicity=Multiplicity(0, 9999))
    }
)
pinActivation_actionActivation_Values82: BinaryAssociation = BinaryAssociation(
    name="pinActivation_actionActivation_Values82",
    ends={
        Property(name="PinActivation_actionActivation_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states83", type=PinActivation_actionActivation_Value, multiplicity=Multiplicity(0, 9999))
    }
)
evaluation_specification_Evaluation_Values60: BinaryAssociation = BinaryAssociation(
    name="evaluation_specification_Evaluation_Values60",
    ends={
        Property(name="Evaluation_specification_Evaluation_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states61", type=Evaluation_specification_Evaluation_Value, multiplicity=Multiplicity(0, 9999))
    }
)
evaluation_locus_Evaluation_Values62: BinaryAssociation = BinaryAssociation(
    name="evaluation_locus_Evaluation_Values62",
    ends={
        Property(name="Evaluation_locus_Evaluation_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states63", type=Evaluation_locus_Evaluation_Value, multiplicity=Multiplicity(0, 9999))
    }
)
booleanValue_value_BooleanValue_Values64: BinaryAssociation = BinaryAssociation(
    name="booleanValue_value_BooleanValue_Values64",
    ends={
        Property(name="BooleanValue_value_BooleanValue_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states65", type=BooleanValue_value_BooleanValue_Value, multiplicity=Multiplicity(0, 9999))
    }
)
objectToken_value_Values66: BinaryAssociation = BinaryAssociation(
    name="objectToken_value_Values66",
    ends={
        Property(name="ObjectToken_value_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states67", type=ObjectToken_value_Value, multiplicity=Multiplicity(0, 9999))
    }
)
callActionActivation_callExecutions_Values68: BinaryAssociation = BinaryAssociation(
    name="callActionActivation_callExecutions_Values68",
    ends={
        Property(name="CallActionActivation_callExecutions_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states69", type=CallActionActivation_callExecutions_Value, multiplicity=Multiplicity(0, 9999))
    }
)
compoundValue_featureValues_Values70: BinaryAssociation = BinaryAssociation(
    name="compoundValue_featureValues_Values70",
    ends={
        Property(name="CompoundValue_featureValues_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states71", type=CompoundValue_featureValues_Value, multiplicity=Multiplicity(0, 9999))
    }
)
token_holder_Values72: BinaryAssociation = BinaryAssociation(
    name="token_holder_Values72",
    ends={
        Property(name="Token_holder_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states73", type=Token_holder_Value, multiplicity=Multiplicity(0, 9999))
    }
)
offer_offeredTokens_Values74: BinaryAssociation = BinaryAssociation(
    name="offer_offeredTokens_Values74",
    ends={
        Property(name="Offer_offeredTokens_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states75", type=Offer_offeredTokens_Value, multiplicity=Multiplicity(0, 9999))
    }
)
featureValue_values_FeatureValue_Values76: BinaryAssociation = BinaryAssociation(
    name="featureValue_values_FeatureValue_Values76",
    ends={
        Property(name="FeatureValue_values_FeatureValue_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states77", type=FeatureValue_values_FeatureValue_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_node_ActivityNodeActivation_Values102: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_node_ActivityNodeActivation_Values102",
    ends={
        Property(name="ActivityNodeActivation_node_ActivityNodeActivation_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states103", type=ActivityNodeActivation_node_ActivityNodeActivation_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_running_Values104: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_running_Values104",
    ends={
        Property(name="ActivityNodeActivation_running_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states105", type=ActivityNodeActivation_running_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_isRunning_Values106: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_isRunning_Values106",
    ends={
        Property(name="ActivityNodeActivation_isRunning_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states107", type=ActivityNodeActivation_isRunning_Value, multiplicity=Multiplicity(0, 9999))
    }
)
pinActivation_count_temp_Values84: BinaryAssociation = BinaryAssociation(
    name="pinActivation_count_temp_Values84",
    ends={
        Property(name="PinActivation_count_temp_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states85", type=PinActivation_count_temp_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityEdgeInstance_group_ActivityEdgeInstance_Values86: BinaryAssociation = BinaryAssociation(
    name="activityEdgeInstance_group_ActivityEdgeInstance_Values86",
    ends={
        Property(name="ActivityEdgeInstance_group_ActivityEdgeInstance_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states87", type=ActivityEdgeInstance_group_ActivityEdgeInstance_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityEdgeInstance_offers_Values88: BinaryAssociation = BinaryAssociation(
    name="activityEdgeInstance_offers_Values88",
    ends={
        Property(name="ActivityEdgeInstance_offers_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states89", type=ActivityEdgeInstance_offers_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityEdgeInstance_target_Values90: BinaryAssociation = BinaryAssociation(
    name="activityEdgeInstance_target_Values90",
    ends={
        Property(name="ActivityEdgeInstance_target_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states91", type=ActivityEdgeInstance_target_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityEdgeInstance_edge_ActivityEdgeInstance_Values92: BinaryAssociation = BinaryAssociation(
    name="activityEdgeInstance_edge_ActivityEdgeInstance_Values92",
    ends={
        Property(name="ActivityEdgeInstance_edge_ActivityEdgeInstance_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states93", type=ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityEdgeInstance_source_Values94: BinaryAssociation = BinaryAssociation(
    name="activityEdgeInstance_source_Values94",
    ends={
        Property(name="ActivityEdgeInstance_source_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states95", type=ActivityEdgeInstance_source_Value, multiplicity=Multiplicity(0, 9999))
    }
)
inputParameterValues_name_Values96: BinaryAssociation = BinaryAssociation(
    name="inputParameterValues_name_Values96",
    ends={
        Property(name="InputParameterValues_name_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states97", type=InputParameterValues_name_Value, multiplicity=Multiplicity(0, 9999))
    }
)
inputParameterValues_parameterValues_Values98: BinaryAssociation = BinaryAssociation(
    name="inputParameterValues_parameterValues_Values98",
    ends={
        Property(name="InputParameterValues_parameterValues_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states99", type=InputParameterValues_parameterValues_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_heldTokens_Values100: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_heldTokens_Values100",
    ends={
        Property(name="ActivityNodeActivation_heldTokens_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states101", type=ActivityNodeActivation_heldTokens_Value, multiplicity=Multiplicity(0, 9999))
    }
)
types125: BinaryAssociation = BinaryAssociation(
    name="types125",
    ends={
        Property(name="uml_TracedClass", type=umlTrace_Values_Object_types_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Object_types_Value", type=uml_TracedClass, multiplicity=Multiplicity(0, 9999))
    }
)
parent126: BinaryAssociation = BinaryAssociation(
    name="parent126",
    ends={
        Property(name="TracedObject", type=umlTrace_Values_Object_types_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="typesTrace", type=Kernel_TracedObject, multiplicity=Multiplicity(1, 1))
    }
)
states127: BinaryAssociation = BinaryAssociation(
    name="states127",
    ends={
        Property(name="State128", type=umlTrace_Values_Object_types_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="object_types_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
activityNodeActivation_outgoingEdges_Values108: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_outgoingEdges_Values108",
    ends={
        Property(name="ActivityNodeActivation_outgoingEdges_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states109", type=ActivityNodeActivation_outgoingEdges_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_incomingEdges_Values110: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_incomingEdges_Values110",
    ends={
        Property(name="ActivityNodeActivation_incomingEdges_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states111", type=ActivityNodeActivation_incomingEdges_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_group_ActivityNodeActivation_Values112: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_group_ActivityNodeActivation_Values112",
    ends={
        Property(name="ActivityNodeActivation_group_ActivityNodeActivation_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states113", type=ActivityNodeActivation_group_ActivityNodeActivation_Value, multiplicity=Multiplicity(0, 9999))
    }
)
extensionalValue_locus_ExtensionalValue_Values114: BinaryAssociation = BinaryAssociation(
    name="extensionalValue_locus_ExtensionalValue_Values114",
    ends={
        Property(name="ExtensionalValue_locus_ExtensionalValue_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states115", type=ExtensionalValue_locus_ExtensionalValue_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityExecution_activationGroup_Values116: BinaryAssociation = BinaryAssociation(
    name="activityExecution_activationGroup_Values116",
    ends={
        Property(name="ActivityExecution_activationGroup_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states117", type=ActivityExecution_activationGroup_Value, multiplicity=Multiplicity(0, 9999))
    }
)
executionEnvironment_locus_ExecutionEnvironment_Values118: BinaryAssociation = BinaryAssociation(
    name="executionEnvironment_locus_ExecutionEnvironment_Values118",
    ends={
        Property(name="ExecutionEnvironment_locus_ExecutionEnvironment_Value", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states119", type=ExecutionEnvironment_locus_ExecutionEnvironment_Value, multiplicity=Multiplicity(0, 9999))
    }
)
precedingState120: BinaryAssociation = BinaryAssociation(
    name="precedingState120",
    ends={
        Property(name="State", type=umlTrace_Steps_SmallStep, multiplicity=Multiplicity(1, 1)),
        Property(name="followingStep", type=Steps_umlTrace_State, multiplicity=Multiplicity(1, 1))
    }
)
startingState121: BinaryAssociation = BinaryAssociation(
    name="startingState121",
    ends={
        Property(name="State122", type=umlTrace_Steps_BigStep, multiplicity=Multiplicity(1, 1)),
        Property(name="startedBigSteps", type=Steps_umlTrace_State, multiplicity=Multiplicity(1, 1))
    }
)
endingState123: BinaryAssociation = BinaryAssociation(
    name="endingState123",
    ends={
        Property(name="State124", type=umlTrace_Steps_BigStep, multiplicity=Multiplicity(1, 1)),
        Property(name="endedBigSteps", type=Steps_umlTrace_State, multiplicity=Multiplicity(0, 1))
    }
)
baseToken139: BinaryAssociation = BinaryAssociation(
    name="baseToken139",
    ends={
        Property(name="IntermediateActivities_TracedToken", type=umlTrace_Values_ForkedToken_baseToken_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ForkedToken_baseToken_Value", type=IntermediateActivities_TracedToken, multiplicity=Multiplicity(1, 1))
    }
)
parent140: BinaryAssociation = BinaryAssociation(
    name="parent140",
    ends={
        Property(name="TracedForkedToken141", type=umlTrace_Values_ForkedToken_baseToken_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="baseTokenTrace", type=IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(1, 1))
    }
)
states142: BinaryAssociation = BinaryAssociation(
    name="states142",
    ends={
        Property(name="State143", type=umlTrace_Values_ForkedToken_baseToken_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="forkedToken_baseToken_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
referent129: BinaryAssociation = BinaryAssociation(
    name="referent129",
    ends={
        Property(name="Kernel_TracedObject", type=umlTrace_Values_Reference_referent_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Reference_referent_Value", type=Kernel_TracedObject, multiplicity=Multiplicity(1, 1))
    }
)
parent130: BinaryAssociation = BinaryAssociation(
    name="parent130",
    ends={
        Property(name="TracedReference", type=umlTrace_Values_Reference_referent_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="referentTrace", type=Kernel_TracedReference, multiplicity=Multiplicity(1, 1))
    }
)
states131: BinaryAssociation = BinaryAssociation(
    name="states131",
    ends={
        Property(name="State132", type=umlTrace_Values_Reference_referent_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_referent_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent133: BinaryAssociation = BinaryAssociation(
    name="parent133",
    ends={
        Property(name="TracedIntegerValue", type=umlTrace_Values_IntegerValue_value_IntegerValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="value_IntegerValueTrace", type=Kernel_TracedIntegerValue, multiplicity=Multiplicity(1, 1))
    }
)
states134: BinaryAssociation = BinaryAssociation(
    name="states134",
    ends={
        Property(name="State135", type=umlTrace_Values_IntegerValue_value_IntegerValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="integerValue_value_IntegerValue_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent136: BinaryAssociation = BinaryAssociation(
    name="parent136",
    ends={
        Property(name="TracedForkedToken", type=umlTrace_Values_ForkedToken_remainingOffersCount_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="remainingOffersCountTrace", type=IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(1, 1))
    }
)
states137: BinaryAssociation = BinaryAssociation(
    name="states137",
    ends={
        Property(name="State138", type=umlTrace_Values_ForkedToken_remainingOffersCount_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="forkedToken_remainingOffersCount_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
states160: BinaryAssociation = BinaryAssociation(
    name="states160",
    ends={
        Property(name="State161", type=umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="executionFactory_locus_ExecutionFactory_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
factory162: BinaryAssociation = BinaryAssociation(
    name="factory162",
    ends={
        Property(name="Loci_TracedExecutionFactory", type=umlTrace_Values_Locus_factory_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Locus_factory_Value", type=Loci_TracedExecutionFactory, multiplicity=Multiplicity(0, 1))
    }
)
parent163: BinaryAssociation = BinaryAssociation(
    name="parent163",
    ends={
        Property(name="TracedLocus", type=umlTrace_Values_Locus_factory_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="factoryTrace", type=Loci_TracedLocus, multiplicity=Multiplicity(1, 1))
    }
)
states164: BinaryAssociation = BinaryAssociation(
    name="states164",
    ends={
        Property(name="State165", type=umlTrace_Values_Locus_factory_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="locus_factory_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
extensionalValues166: BinaryAssociation = BinaryAssociation(
    name="extensionalValues166",
    ends={
        Property(name="Kernel_TracedExtensionalValue", type=umlTrace_Values_Locus_extensionalValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Locus_extensionalValues_Value", type=Kernel_TracedExtensionalValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent144: BinaryAssociation = BinaryAssociation(
    name="parent144",
    ends={
        Property(name="TracedForkedToken145", type=umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="baseTokenIsWithdrawnTrace", type=IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(1, 1))
    }
)
states146: BinaryAssociation = BinaryAssociation(
    name="states146",
    ends={
        Property(name="State147", type=umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="forkedToken_baseTokenIsWithdrawn_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
builtInTypes148: BinaryAssociation = BinaryAssociation(
    name="builtInTypes148",
    ends={
        Property(name="uml_TracedPrimitiveType", type=umlTrace_Values_ExecutionFactory_builtInTypes_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ExecutionFactory_builtInTypes_Value", type=uml_TracedPrimitiveType, multiplicity=Multiplicity(0, 9999))
    }
)
parent149: BinaryAssociation = BinaryAssociation(
    name="parent149",
    ends={
        Property(name="TracedExecutionFactory", type=umlTrace_Values_ExecutionFactory_builtInTypes_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="builtInTypesTrace", type=Loci_TracedExecutionFactory, multiplicity=Multiplicity(1, 1))
    }
)
states150: BinaryAssociation = BinaryAssociation(
    name="states150",
    ends={
        Property(name="State151", type=umlTrace_Values_ExecutionFactory_builtInTypes_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="executionFactory_builtInTypes_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
primitiveBehaviorPrototypes152: BinaryAssociation = BinaryAssociation(
    name="primitiveBehaviorPrototypes152",
    ends={
        Property(name="BasicBehaviors_TracedOpaqueBehaviorExecution", type=umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value", type=BasicBehaviors_TracedOpaqueBehaviorExecution, multiplicity=Multiplicity(0, 9999))
    }
)
parent153: BinaryAssociation = BinaryAssociation(
    name="parent153",
    ends={
        Property(name="TracedExecutionFactory154", type=umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="primitiveBehaviorPrototypesTrace", type=Loci_TracedExecutionFactory, multiplicity=Multiplicity(1, 1))
    }
)
states155: BinaryAssociation = BinaryAssociation(
    name="states155",
    ends={
        Property(name="State156", type=umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="executionFactory_primitiveBehaviorPrototypes_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
locus_ExecutionFactory157: BinaryAssociation = BinaryAssociation(
    name="locus_ExecutionFactory157",
    ends={
        Property(name="Loci_TracedLocus", type=umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value", type=Loci_TracedLocus, multiplicity=Multiplicity(0, 1))
    }
)
parent158: BinaryAssociation = BinaryAssociation(
    name="parent158",
    ends={
        Property(name="TracedExecutionFactory159", type=umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="locus_ExecutionFactoryTrace", type=Loci_TracedExecutionFactory, multiplicity=Multiplicity(1, 1))
    }
)
runtimeModelElement179: BinaryAssociation = BinaryAssociation(
    name="runtimeModelElement179",
    ends={
        Property(name="uml_TracedElement", type=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_SemanticVisitor_runtimeModelElement_Value", type=uml_TracedElement, multiplicity=Multiplicity(0, 1))
    }
)
parent180: BinaryAssociation = BinaryAssociation(
    name="parent180",
    ends={
        Property(name="TracedSemanticVisitor", type=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="runtimeModelElementTrace", type=Loci_TracedSemanticVisitor, multiplicity=Multiplicity(1, 1))
    }
)
states181: BinaryAssociation = BinaryAssociation(
    name="states181",
    ends={
        Property(name="State182", type=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="semanticVisitor_runtimeModelElement_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent167: BinaryAssociation = BinaryAssociation(
    name="parent167",
    ends={
        Property(name="TracedLocus168", type=umlTrace_Values_Locus_extensionalValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionalValuesTrace", type=Loci_TracedLocus, multiplicity=Multiplicity(1, 1))
    }
)
states169: BinaryAssociation = BinaryAssociation(
    name="states169",
    ends={
        Property(name="State170", type=umlTrace_Values_Locus_extensionalValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="locus_extensionalValues_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
executor171: BinaryAssociation = BinaryAssociation(
    name="executor171",
    ends={
        Property(name="Loci_TracedExecutor", type=umlTrace_Values_Locus_executor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Locus_executor_Value", type=Loci_TracedExecutor, multiplicity=Multiplicity(0, 1))
    }
)
parent172: BinaryAssociation = BinaryAssociation(
    name="parent172",
    ends={
        Property(name="TracedLocus173", type=umlTrace_Values_Locus_executor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="executorTrace", type=Loci_TracedLocus, multiplicity=Multiplicity(1, 1))
    }
)
states174: BinaryAssociation = BinaryAssociation(
    name="states174",
    ends={
        Property(name="State175", type=umlTrace_Values_Locus_executor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="locus_executor_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent176: BinaryAssociation = BinaryAssociation(
    name="parent176",
    ends={
        Property(name="TracedObjectNodeActivation", type=umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="offeredTokenCountTrace", type=IntermediateActivities_TracedObjectNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states177: BinaryAssociation = BinaryAssociation(
    name="states177",
    ends={
        Property(name="State178", type=umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="objectNodeActivation_offeredTokenCount_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent196: BinaryAssociation = BinaryAssociation(
    name="parent196",
    ends={
        Property(name="TracedActionActivation197", type=umlTrace_Values_ActionActivation_firing_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="firingTrace", type=BasicActions_TracedActionActivation, multiplicity=Multiplicity(1, 1))
    }
)
states198: BinaryAssociation = BinaryAssociation(
    name="states198",
    ends={
        Property(name="State199", type=umlTrace_Values_ActionActivation_firing_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="actionActivation_firing_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
values_ParameterValue183: BinaryAssociation = BinaryAssociation(
    name="values_ParameterValue183",
    ends={
        Property(name="Kernel_TracedValue", type=umlTrace_Values_ParameterValue_values_ParameterValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ParameterValue_values_ParameterValue_Value", type=Kernel_TracedValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent184: BinaryAssociation = BinaryAssociation(
    name="parent184",
    ends={
        Property(name="TracedParameterValue", type=umlTrace_Values_ParameterValue_values_ParameterValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="values_ParameterValueTrace", type=BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(1, 1))
    }
)
states185: BinaryAssociation = BinaryAssociation(
    name="states185",
    ends={
        Property(name="State186", type=umlTrace_Values_ParameterValue_values_ParameterValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterValue_values_ParameterValue_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parameter_ParameterValue187: BinaryAssociation = BinaryAssociation(
    name="parameter_ParameterValue187",
    ends={
        Property(name="uml_TracedParameter", type=umlTrace_Values_ParameterValue_parameter_ParameterValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ParameterValue_parameter_ParameterValue_Value", type=uml_TracedParameter, multiplicity=Multiplicity(1, 1))
    }
)
parent188: BinaryAssociation = BinaryAssociation(
    name="parent188",
    ends={
        Property(name="TracedParameterValue189", type=umlTrace_Values_ParameterValue_parameter_ParameterValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter_ParameterValueTrace", type=BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(1, 1))
    }
)
states190: BinaryAssociation = BinaryAssociation(
    name="states190",
    ends={
        Property(name="State191", type=umlTrace_Values_ParameterValue_parameter_ParameterValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterValue_parameter_ParameterValue_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
pinActivations192: BinaryAssociation = BinaryAssociation(
    name="pinActivations192",
    ends={
        Property(name="BasicActions_TracedPinActivation", type=umlTrace_Values_ActionActivation_pinActivations_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActionActivation_pinActivations_Value", type=BasicActions_TracedPinActivation, multiplicity=Multiplicity(0, 9999))
    }
)
parent193: BinaryAssociation = BinaryAssociation(
    name="parent193",
    ends={
        Property(name="TracedActionActivation", type=umlTrace_Values_ActionActivation_pinActivations_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="pinActivationsTrace", type=BasicActions_TracedActionActivation, multiplicity=Multiplicity(1, 1))
    }
)
states194: BinaryAssociation = BinaryAssociation(
    name="states194",
    ends={
        Property(name="State195", type=umlTrace_Values_ActionActivation_pinActivations_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="actionActivation_pinActivations_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
nodeActivations214: BinaryAssociation = BinaryAssociation(
    name="nodeActivations214",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivation", type=umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(0, 9999))
    }
)
parent215: BinaryAssociation = BinaryAssociation(
    name="parent215",
    ends={
        Property(name="TracedActivityNodeActivationGroup", type=umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="nodeActivationsTrace", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1))
    }
)
parameterValues200: BinaryAssociation = BinaryAssociation(
    name="parameterValues200",
    ends={
        Property(name="BasicBehaviors_TracedParameterValue", type=umlTrace_Values_Execution_parameterValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Execution_parameterValues_Value", type=BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent201: BinaryAssociation = BinaryAssociation(
    name="parent201",
    ends={
        Property(name="TracedExecution", type=umlTrace_Values_Execution_parameterValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterValuesTrace", type=BasicBehaviors_TracedExecution, multiplicity=Multiplicity(1, 1))
    }
)
states202: BinaryAssociation = BinaryAssociation(
    name="states202",
    ends={
        Property(name="State203", type=umlTrace_Values_Execution_parameterValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="execution_parameterValues_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
context204: BinaryAssociation = BinaryAssociation(
    name="context204",
    ends={
        Property(name="Kernel_TracedObject205", type=umlTrace_Values_Execution_context_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Execution_context_Value", type=Kernel_TracedObject, multiplicity=Multiplicity(1, 1))
    }
)
parent206: BinaryAssociation = BinaryAssociation(
    name="parent206",
    ends={
        Property(name="TracedExecution207", type=umlTrace_Values_Execution_context_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="contextTrace", type=BasicBehaviors_TracedExecution, multiplicity=Multiplicity(1, 1))
    }
)
states208: BinaryAssociation = BinaryAssociation(
    name="states208",
    ends={
        Property(name="State209", type=umlTrace_Values_Execution_context_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="execution_context_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
semanticVisitor210: BinaryAssociation = BinaryAssociation(
    name="semanticVisitor210",
    ends={
        Property(name="Loci_TracedSemanticVisitor", type=umlTrace_Values_Element_semanticVisitor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Element_semanticVisitor_Value", type=Loci_TracedSemanticVisitor, multiplicity=Multiplicity(0, 9999))
    }
)
parent211: BinaryAssociation = BinaryAssociation(
    name="parent211",
    ends={
        Property(name="TracedElement", type=umlTrace_Values_Element_semanticVisitor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="semanticVisitorTrace", type=uml_TracedElement, multiplicity=Multiplicity(1, 1))
    }
)
states212: BinaryAssociation = BinaryAssociation(
    name="states212",
    ends={
        Property(name="State213", type=umlTrace_Values_Element_semanticVisitor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="element_semanticVisitor_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent230: BinaryAssociation = BinaryAssociation(
    name="parent230",
    ends={
        Property(name="TracedExecutor", type=umlTrace_Values_Executor_locus_Executor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="locus_ExecutorTrace", type=Loci_TracedExecutor, multiplicity=Multiplicity(1, 1))
    }
)
states231: BinaryAssociation = BinaryAssociation(
    name="states231",
    ends={
        Property(name="State232", type=umlTrace_Values_Executor_locus_Executor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="executor_locus_Executor_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
type233: BinaryAssociation = BinaryAssociation(
    name="type233",
    ends={
        Property(name="uml_TracedPrimitiveType234", type=umlTrace_Values_PrimitiveValue_type_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_PrimitiveValue_type_Value", type=uml_TracedPrimitiveType, multiplicity=Multiplicity(1, 1))
    }
)
parent235: BinaryAssociation = BinaryAssociation(
    name="parent235",
    ends={
        Property(name="TracedPrimitiveValue", type=umlTrace_Values_PrimitiveValue_type_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="typeTrace", type=Kernel_TracedPrimitiveValue, multiplicity=Multiplicity(1, 1))
    }
)
states216: BinaryAssociation = BinaryAssociation(
    name="states216",
    ends={
        Property(name="State217", type=umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivationGroup_nodeActivations_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
activityExecution218: BinaryAssociation = BinaryAssociation(
    name="activityExecution218",
    ends={
        Property(name="IntermediateActivities_TracedActivityExecution", type=umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value", type=IntermediateActivities_TracedActivityExecution, multiplicity=Multiplicity(0, 1))
    }
)
parent219: BinaryAssociation = BinaryAssociation(
    name="parent219",
    ends={
        Property(name="TracedActivityNodeActivationGroup220", type=umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityExecutionTrace", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1))
    }
)
states221: BinaryAssociation = BinaryAssociation(
    name="states221",
    ends={
        Property(name="State222", type=umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivationGroup_activityExecution_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
edgeInstances223: BinaryAssociation = BinaryAssociation(
    name="edgeInstances223",
    ends={
        Property(name="IntermediateActivities_TracedActivityEdgeInstance", type=umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(0, 9999))
    }
)
parent224: BinaryAssociation = BinaryAssociation(
    name="parent224",
    ends={
        Property(name="TracedActivityNodeActivationGroup225", type=umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="edgeInstancesTrace", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1))
    }
)
states226: BinaryAssociation = BinaryAssociation(
    name="states226",
    ends={
        Property(name="State227", type=umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivationGroup_edgeInstances_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
locus_Executor228: BinaryAssociation = BinaryAssociation(
    name="locus_Executor228",
    ends={
        Property(name="Loci_TracedLocus229", type=umlTrace_Values_Executor_locus_Executor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Executor_locus_Executor_Value", type=Loci_TracedLocus, multiplicity=Multiplicity(0, 1))
    }
)
states249: BinaryAssociation = BinaryAssociation(
    name="states249",
    ends={
        Property(name="State250", type=umlTrace_Values_BooleanValue_value_BooleanValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="booleanValue_value_BooleanValue_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
value251: BinaryAssociation = BinaryAssociation(
    name="value251",
    ends={
        Property(name="Kernel_TracedValue252", type=umlTrace_Values_ObjectToken_value_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ObjectToken_value_Value", type=Kernel_TracedValue, multiplicity=Multiplicity(0, 1))
    }
)
parent253: BinaryAssociation = BinaryAssociation(
    name="parent253",
    ends={
        Property(name="TracedObjectToken", type=umlTrace_Values_ObjectToken_value_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="valueTrace", type=IntermediateActivities_TracedObjectToken, multiplicity=Multiplicity(1, 1))
    }
)
states254: BinaryAssociation = BinaryAssociation(
    name="states254",
    ends={
        Property(name="State255", type=umlTrace_Values_ObjectToken_value_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="objectToken_value_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
states236: BinaryAssociation = BinaryAssociation(
    name="states236",
    ends={
        Property(name="State237", type=umlTrace_Values_PrimitiveValue_type_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="primitiveValue_type_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
specification_Evaluation238: BinaryAssociation = BinaryAssociation(
    name="specification_Evaluation238",
    ends={
        Property(name="uml_TracedValueSpecification", type=umlTrace_Values_Evaluation_specification_Evaluation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Evaluation_specification_Evaluation_Value", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
parent239: BinaryAssociation = BinaryAssociation(
    name="parent239",
    ends={
        Property(name="TracedEvaluation", type=umlTrace_Values_Evaluation_specification_Evaluation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="specification_EvaluationTrace", type=Kernel_TracedEvaluation, multiplicity=Multiplicity(1, 1))
    }
)
states240: BinaryAssociation = BinaryAssociation(
    name="states240",
    ends={
        Property(name="State241", type=umlTrace_Values_Evaluation_specification_Evaluation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluation_specification_Evaluation_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
locus_Evaluation242: BinaryAssociation = BinaryAssociation(
    name="locus_Evaluation242",
    ends={
        Property(name="Loci_TracedLocus243", type=umlTrace_Values_Evaluation_locus_Evaluation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Evaluation_locus_Evaluation_Value", type=Loci_TracedLocus, multiplicity=Multiplicity(1, 1))
    }
)
parent244: BinaryAssociation = BinaryAssociation(
    name="parent244",
    ends={
        Property(name="TracedEvaluation245", type=umlTrace_Values_Evaluation_locus_Evaluation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="locus_EvaluationTrace", type=Kernel_TracedEvaluation, multiplicity=Multiplicity(1, 1))
    }
)
states246: BinaryAssociation = BinaryAssociation(
    name="states246",
    ends={
        Property(name="State247", type=umlTrace_Values_Evaluation_locus_Evaluation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluation_locus_Evaluation_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent248: BinaryAssociation = BinaryAssociation(
    name="parent248",
    ends={
        Property(name="TracedBooleanValue", type=umlTrace_Values_BooleanValue_value_BooleanValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="value_BooleanValueTrace", type=Kernel_TracedBooleanValue, multiplicity=Multiplicity(1, 1))
    }
)
offeredTokens269: BinaryAssociation = BinaryAssociation(
    name="offeredTokens269",
    ends={
        Property(name="IntermediateActivities_TracedToken270", type=umlTrace_Values_Offer_offeredTokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Offer_offeredTokens_Value", type=IntermediateActivities_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
parent271: BinaryAssociation = BinaryAssociation(
    name="parent271",
    ends={
        Property(name="TracedOffer", type=umlTrace_Values_Offer_offeredTokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="offeredTokensTrace", type=IntermediateActivities_TracedOffer, multiplicity=Multiplicity(1, 1))
    }
)
states272: BinaryAssociation = BinaryAssociation(
    name="states272",
    ends={
        Property(name="State273", type=umlTrace_Values_Offer_offeredTokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="offer_offeredTokens_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
callExecutions256: BinaryAssociation = BinaryAssociation(
    name="callExecutions256",
    ends={
        Property(name="BasicBehaviors_TracedExecution", type=umlTrace_Values_CallActionActivation_callExecutions_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_CallActionActivation_callExecutions_Value", type=BasicBehaviors_TracedExecution, multiplicity=Multiplicity(0, 9999))
    }
)
parent257: BinaryAssociation = BinaryAssociation(
    name="parent257",
    ends={
        Property(name="TracedCallActionActivation", type=umlTrace_Values_CallActionActivation_callExecutions_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="callExecutionsTrace", type=BasicActions_TracedCallActionActivation, multiplicity=Multiplicity(1, 1))
    }
)
states258: BinaryAssociation = BinaryAssociation(
    name="states258",
    ends={
        Property(name="State259", type=umlTrace_Values_CallActionActivation_callExecutions_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="callActionActivation_callExecutions_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
featureValues260: BinaryAssociation = BinaryAssociation(
    name="featureValues260",
    ends={
        Property(name="Kernel_TracedFeatureValue", type=umlTrace_Values_CompoundValue_featureValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_CompoundValue_featureValues_Value", type=Kernel_TracedFeatureValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent261: BinaryAssociation = BinaryAssociation(
    name="parent261",
    ends={
        Property(name="TracedCompoundValue", type=umlTrace_Values_CompoundValue_featureValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="featureValuesTrace", type=Kernel_TracedCompoundValue, multiplicity=Multiplicity(1, 1))
    }
)
states262: BinaryAssociation = BinaryAssociation(
    name="states262",
    ends={
        Property(name="State263", type=umlTrace_Values_CompoundValue_featureValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="compoundValue_featureValues_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
holder264: BinaryAssociation = BinaryAssociation(
    name="holder264",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivation265", type=umlTrace_Values_Token_holder_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Token_holder_Value", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(0, 1))
    }
)
parent266: BinaryAssociation = BinaryAssociation(
    name="parent266",
    ends={
        Property(name="TracedToken", type=umlTrace_Values_Token_holder_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="holderTrace", type=IntermediateActivities_TracedToken, multiplicity=Multiplicity(1, 1))
    }
)
states267: BinaryAssociation = BinaryAssociation(
    name="states267",
    ends={
        Property(name="State268", type=umlTrace_Values_Token_holder_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="token_holder_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
states286: BinaryAssociation = BinaryAssociation(
    name="states286",
    ends={
        Property(name="State287", type=umlTrace_Values_FeatureValue_position_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="featureValue_position_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
actionActivation288: BinaryAssociation = BinaryAssociation(
    name="actionActivation288",
    ends={
        Property(name="BasicActions_TracedActionActivation", type=umlTrace_Values_PinActivation_actionActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_PinActivation_actionActivation_Value", type=BasicActions_TracedActionActivation, multiplicity=Multiplicity(0, 1))
    }
)
parent289: BinaryAssociation = BinaryAssociation(
    name="parent289",
    ends={
        Property(name="TracedPinActivation", type=umlTrace_Values_PinActivation_actionActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="actionActivationTrace", type=BasicActions_TracedPinActivation, multiplicity=Multiplicity(1, 1))
    }
)
values_FeatureValue274: BinaryAssociation = BinaryAssociation(
    name="values_FeatureValue274",
    ends={
        Property(name="Kernel_TracedValue275", type=umlTrace_Values_FeatureValue_values_FeatureValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_FeatureValue_values_FeatureValue_Value", type=Kernel_TracedValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent276: BinaryAssociation = BinaryAssociation(
    name="parent276",
    ends={
        Property(name="TracedFeatureValue", type=umlTrace_Values_FeatureValue_values_FeatureValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="values_FeatureValueTrace", type=Kernel_TracedFeatureValue, multiplicity=Multiplicity(1, 1))
    }
)
states277: BinaryAssociation = BinaryAssociation(
    name="states277",
    ends={
        Property(name="State278", type=umlTrace_Values_FeatureValue_values_FeatureValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="featureValue_values_FeatureValue_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
feature279: BinaryAssociation = BinaryAssociation(
    name="feature279",
    ends={
        Property(name="uml_TracedStructuralFeature", type=umlTrace_Values_FeatureValue_feature_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_FeatureValue_feature_Value", type=uml_TracedStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
parent280: BinaryAssociation = BinaryAssociation(
    name="parent280",
    ends={
        Property(name="TracedFeatureValue281", type=umlTrace_Values_FeatureValue_feature_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="featureTrace", type=Kernel_TracedFeatureValue, multiplicity=Multiplicity(1, 1))
    }
)
states282: BinaryAssociation = BinaryAssociation(
    name="states282",
    ends={
        Property(name="State283", type=umlTrace_Values_FeatureValue_feature_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="featureValue_feature_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent284: BinaryAssociation = BinaryAssociation(
    name="parent284",
    ends={
        Property(name="TracedFeatureValue285", type=umlTrace_Values_FeatureValue_position_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="positionTrace", type=Kernel_TracedFeatureValue, multiplicity=Multiplicity(1, 1))
    }
)
offers300: BinaryAssociation = BinaryAssociation(
    name="offers300",
    ends={
        Property(name="IntermediateActivities_TracedOffer", type=umlTrace_Values_ActivityEdgeInstance_offers_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityEdgeInstance_offers_Value", type=IntermediateActivities_TracedOffer, multiplicity=Multiplicity(0, 9999))
    }
)
parent301: BinaryAssociation = BinaryAssociation(
    name="parent301",
    ends={
        Property(name="TracedActivityEdgeInstance302", type=umlTrace_Values_ActivityEdgeInstance_offers_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="offersTrace", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1))
    }
)
states290: BinaryAssociation = BinaryAssociation(
    name="states290",
    ends={
        Property(name="State291", type=umlTrace_Values_PinActivation_actionActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="pinActivation_actionActivation_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent292: BinaryAssociation = BinaryAssociation(
    name="parent292",
    ends={
        Property(name="TracedPinActivation293", type=umlTrace_Values_PinActivation_count_temp_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="count_tempTrace", type=BasicActions_TracedPinActivation, multiplicity=Multiplicity(1, 1))
    }
)
states294: BinaryAssociation = BinaryAssociation(
    name="states294",
    ends={
        Property(name="State295", type=umlTrace_Values_PinActivation_count_temp_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="pinActivation_count_temp_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
group_ActivityEdgeInstance296: BinaryAssociation = BinaryAssociation(
    name="group_ActivityEdgeInstance296",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivationGroup", type=umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1))
    }
)
parent297: BinaryAssociation = BinaryAssociation(
    name="parent297",
    ends={
        Property(name="TracedActivityEdgeInstance", type=umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="group_ActivityEdgeInstanceTrace", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1))
    }
)
states298: BinaryAssociation = BinaryAssociation(
    name="states298",
    ends={
        Property(name="State299", type=umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityEdgeInstance_group_ActivityEdgeInstance_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
states314: BinaryAssociation = BinaryAssociation(
    name="states314",
    ends={
        Property(name="State315", type=umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityEdgeInstance_edge_ActivityEdgeInstance_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
source316: BinaryAssociation = BinaryAssociation(
    name="source316",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivation317", type=umlTrace_Values_ActivityEdgeInstance_source_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityEdgeInstance_source_Value", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
parent318: BinaryAssociation = BinaryAssociation(
    name="parent318",
    ends={
        Property(name="TracedActivityEdgeInstance319", type=umlTrace_Values_ActivityEdgeInstance_source_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceTrace", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1))
    }
)
states320: BinaryAssociation = BinaryAssociation(
    name="states320",
    ends={
        Property(name="State321", type=umlTrace_Values_ActivityEdgeInstance_source_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityEdgeInstance_source_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
states303: BinaryAssociation = BinaryAssociation(
    name="states303",
    ends={
        Property(name="State304", type=umlTrace_Values_ActivityEdgeInstance_offers_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityEdgeInstance_offers_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
target305: BinaryAssociation = BinaryAssociation(
    name="target305",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivation306", type=umlTrace_Values_ActivityEdgeInstance_target_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityEdgeInstance_target_Value", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
parent307: BinaryAssociation = BinaryAssociation(
    name="parent307",
    ends={
        Property(name="TracedActivityEdgeInstance308", type=umlTrace_Values_ActivityEdgeInstance_target_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="targetTrace", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1))
    }
)
states309: BinaryAssociation = BinaryAssociation(
    name="states309",
    ends={
        Property(name="State310", type=umlTrace_Values_ActivityEdgeInstance_target_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityEdgeInstance_target_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
edge_ActivityEdgeInstance311: BinaryAssociation = BinaryAssociation(
    name="edge_ActivityEdgeInstance311",
    ends={
        Property(name="uml_TracedActivityEdge", type=umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 1))
    }
)
parent312: BinaryAssociation = BinaryAssociation(
    name="parent312",
    ends={
        Property(name="TracedActivityEdgeInstance313", type=umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="edge_ActivityEdgeInstanceTrace", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1))
    }
)
states335: BinaryAssociation = BinaryAssociation(
    name="states335",
    ends={
        Property(name="State336", type=umlTrace_Values_ActivityNodeActivation_heldTokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_heldTokens_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
node_ActivityNodeActivation337: BinaryAssociation = BinaryAssociation(
    name="node_ActivityNodeActivation337",
    ends={
        Property(name="uml_TracedActivityNode", type=umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
parent338: BinaryAssociation = BinaryAssociation(
    name="parent338",
    ends={
        Property(name="TracedActivityNodeActivation339", type=umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="node_ActivityNodeActivationTrace", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states340: BinaryAssociation = BinaryAssociation(
    name="states340",
    ends={
        Property(name="State341", type=umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_node_ActivityNodeActivation_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent322: BinaryAssociation = BinaryAssociation(
    name="parent322",
    ends={
        Property(name="TracedInputParameterValues", type=umlTrace_Values_InputParameterValues_name_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="nameTrace", type=Input_TracedInputParameterValues, multiplicity=Multiplicity(1, 1))
    }
)
states323: BinaryAssociation = BinaryAssociation(
    name="states323",
    ends={
        Property(name="State324", type=umlTrace_Values_InputParameterValues_name_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="inputParameterValues_name_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parameterValues325: BinaryAssociation = BinaryAssociation(
    name="parameterValues325",
    ends={
        Property(name="BasicBehaviors_TracedParameterValue326", type=umlTrace_Values_InputParameterValues_parameterValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_InputParameterValues_parameterValues_Value", type=BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent327: BinaryAssociation = BinaryAssociation(
    name="parent327",
    ends={
        Property(name="TracedInputParameterValues329", type=umlTrace_Values_InputParameterValues_parameterValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterValuesTrace328", type=Input_TracedInputParameterValues, multiplicity=Multiplicity(1, 1))
    }
)
states330: BinaryAssociation = BinaryAssociation(
    name="states330",
    ends={
        Property(name="State331", type=umlTrace_Values_InputParameterValues_parameterValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="inputParameterValues_parameterValues_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
heldTokens332: BinaryAssociation = BinaryAssociation(
    name="heldTokens332",
    ends={
        Property(name="IntermediateActivities_TracedToken333", type=umlTrace_Values_ActivityNodeActivation_heldTokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivation_heldTokens_Value", type=IntermediateActivities_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
parent334: BinaryAssociation = BinaryAssociation(
    name="parent334",
    ends={
        Property(name="TracedActivityNodeActivation", type=umlTrace_Values_ActivityNodeActivation_heldTokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="heldTokensTrace", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states354: BinaryAssociation = BinaryAssociation(
    name="states354",
    ends={
        Property(name="State355", type=umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_outgoingEdges_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
incomingEdges356: BinaryAssociation = BinaryAssociation(
    name="incomingEdges356",
    ends={
        Property(name="IntermediateActivities_TracedActivityEdgeInstance357", type=umlTrace_Values_ActivityNodeActivation_incomingEdges_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivation_incomingEdges_Value", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(0, 9999))
    }
)
parent358: BinaryAssociation = BinaryAssociation(
    name="parent358",
    ends={
        Property(name="TracedActivityNodeActivation359", type=umlTrace_Values_ActivityNodeActivation_incomingEdges_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdgesTrace", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states360: BinaryAssociation = BinaryAssociation(
    name="states360",
    ends={
        Property(name="State361", type=umlTrace_Values_ActivityNodeActivation_incomingEdges_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_incomingEdges_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent342: BinaryAssociation = BinaryAssociation(
    name="parent342",
    ends={
        Property(name="TracedActivityNodeActivation343", type=umlTrace_Values_ActivityNodeActivation_running_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="runningTrace", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states344: BinaryAssociation = BinaryAssociation(
    name="states344",
    ends={
        Property(name="State345", type=umlTrace_Values_ActivityNodeActivation_running_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_running_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent346: BinaryAssociation = BinaryAssociation(
    name="parent346",
    ends={
        Property(name="TracedActivityNodeActivation347", type=umlTrace_Values_ActivityNodeActivation_isRunning_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="isRunningTrace", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states348: BinaryAssociation = BinaryAssociation(
    name="states348",
    ends={
        Property(name="State349", type=umlTrace_Values_ActivityNodeActivation_isRunning_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_isRunning_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
outgoingEdges350: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges350",
    ends={
        Property(name="IntermediateActivities_TracedActivityEdgeInstance351", type=umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(0, 9999))
    }
)
parent352: BinaryAssociation = BinaryAssociation(
    name="parent352",
    ends={
        Property(name="TracedActivityNodeActivation353", type=umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdgesTrace", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states376: BinaryAssociation = BinaryAssociation(
    name="states376",
    ends={
        Property(name="State377", type=umlTrace_Values_ActivityExecution_activationGroup_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityExecution_activationGroup_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
locus_ExecutionEnvironment378: BinaryAssociation = BinaryAssociation(
    name="locus_ExecutionEnvironment378",
    ends={
        Property(name="Loci_TracedLocus379", type=umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value", type=Loci_TracedLocus, multiplicity=Multiplicity(1, 1))
    }
)
parent380: BinaryAssociation = BinaryAssociation(
    name="parent380",
    ends={
        Property(name="TracedExecutionEnvironment", type=umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="locus_ExecutionEnvironmentTrace", type=Loci_TracedExecutionEnvironment, multiplicity=Multiplicity(1, 1))
    }
)
states381: BinaryAssociation = BinaryAssociation(
    name="states381",
    ends={
        Property(name="State382", type=umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="executionEnvironment_locus_ExecutionEnvironment_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
group_ActivityNodeActivation362: BinaryAssociation = BinaryAssociation(
    name="group_ActivityNodeActivation362",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivationGroup363", type=umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(0, 1))
    }
)
parent364: BinaryAssociation = BinaryAssociation(
    name="parent364",
    ends={
        Property(name="TracedActivityNodeActivation365", type=umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="group_ActivityNodeActivationTrace", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states366: BinaryAssociation = BinaryAssociation(
    name="states366",
    ends={
        Property(name="State367", type=umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_group_ActivityNodeActivation_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
locus_ExtensionalValue368: BinaryAssociation = BinaryAssociation(
    name="locus_ExtensionalValue368",
    ends={
        Property(name="Loci_TracedLocus369", type=umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value", type=Loci_TracedLocus, multiplicity=Multiplicity(0, 1))
    }
)
parent370: BinaryAssociation = BinaryAssociation(
    name="parent370",
    ends={
        Property(name="TracedExtensionalValue", type=umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="locus_ExtensionalValueTrace", type=Kernel_TracedExtensionalValue, multiplicity=Multiplicity(1, 1))
    }
)
states371: BinaryAssociation = BinaryAssociation(
    name="states371",
    ends={
        Property(name="State372", type=umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionalValue_locus_ExtensionalValue_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
activationGroup373: BinaryAssociation = BinaryAssociation(
    name="activationGroup373",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivationGroup374", type=umlTrace_Values_ActivityExecution_activationGroup_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityExecution_activationGroup_Value", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1))
    }
)
parent375: BinaryAssociation = BinaryAssociation(
    name="parent375",
    ends={
        Property(name="TracedActivityExecution", type=umlTrace_Values_ActivityExecution_activationGroup_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activationGroupTrace", type=IntermediateActivities_TracedActivityExecution, multiplicity=Multiplicity(1, 1))
    }
)
kernel_tracedIntegerValues403: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedIntegerValues403",
    ends={
        Property(name="Kernel_TracedIntegerValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects404", type=Kernel_TracedIntegerValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedForkedTokens405: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedForkedTokens405",
    ends={
        Property(name="IntermediateActivities_TracedForkedToken", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects406", type=IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOpaqueBehaviors407: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOpaqueBehaviors407",
    ends={
        Property(name="uml_TracedOpaqueBehavior", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects408", type=uml_TracedOpaqueBehavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loci_tracedExecutionFactorys409: BinaryAssociation = BinaryAssociation(
    name="loci_tracedExecutionFactorys409",
    ends={
        Property(name="Loci_TracedExecutionFactory411", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects410", type=Loci_TracedExecutionFactory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loci_tracedLocuss412: BinaryAssociation = BinaryAssociation(
    name="loci_tracedLocuss412",
    ends={
        Property(name="Loci_TracedLocus414", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects413", type=Loci_TracedLocus, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedArtifacts415: BinaryAssociation = BinaryAssociation(
    name="uml_tracedArtifacts415",
    ends={
        Property(name="uml_TracedArtifact", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects416", type=uml_TracedArtifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedObjects383: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedObjects383",
    ends={
        Property(name="Kernel_TracedObject384", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects", type=Kernel_TracedObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectors385: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectors385",
    ends={
        Property(name="uml_TracedConnector", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects386", type=uml_TracedConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOpaqueActions387: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOpaqueActions387",
    ends={
        Property(name="uml_TracedOpaqueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects388", type=uml_TracedOpaqueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDataTypes389: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDataTypes389",
    ends={
        Property(name="uml_TracedDataType", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects390", type=uml_TracedDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCommunicationPaths391: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCommunicationPaths391",
    ends={
        Property(name="uml_TracedCommunicationPath", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects392", type=uml_TracedCommunicationPath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedReferences393: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedReferences393",
    ends={
        Property(name="Kernel_TracedReference", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects394", type=Kernel_TracedReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPropertys395: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPropertys395",
    ends={
        Property(name="uml_TracedProperty", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects396", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedContinuations397: BinaryAssociation = BinaryAssociation(
    name="uml_tracedContinuations397",
    ends={
        Property(name="uml_TracedContinuation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects398", type=uml_TracedContinuation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRemoveStructuralFeatureValueActions399: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRemoveStructuralFeatureValueActions399",
    ends={
        Property(name="uml_TracedRemoveStructuralFeatureValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects400", type=uml_TracedRemoveStructuralFeatureValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSendSignalActions401: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSendSignalActions401",
    ends={
        Property(name="uml_TracedSendSignalAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects402", type=uml_TracedSendSignalAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExpressions437: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExpressions437",
    ends={
        Property(name="uml_TracedExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects438", type=uml_TracedExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConsiderIgnoreFragments439: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConsiderIgnoreFragments439",
    ends={
        Property(name="uml_TracedConsiderIgnoreFragment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects440", type=uml_TracedConsiderIgnoreFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDataStoreNodes441: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDataStoreNodes441",
    ends={
        Property(name="uml_TracedDataStoreNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects442", type=uml_TracedDataStoreNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedFlowFinalNodes443: BinaryAssociation = BinaryAssociation(
    name="uml_tracedFlowFinalNodes443",
    ends={
        Property(name="uml_TracedFlowFinalNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects444", type=uml_TracedFlowFinalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInformationItems445: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInformationItems445",
    ends={
        Property(name="uml_TracedInformationItem", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects446", type=uml_TracedInformationItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedJoinNodeActivations417: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedJoinNodeActivations417",
    ends={
        Property(name="IntermediateActivities_TracedJoinNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects418", type=IntermediateActivities_TracedJoinNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeConstraints419: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeConstraints419",
    ends={
        Property(name="uml_TracedTimeConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects420", type=uml_TracedTimeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInterfaceRealizations421: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInterfaceRealizations421",
    ends={
        Property(name="uml_TracedInterfaceRealization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects422", type=uml_TracedInterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivityFinalNodes423: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivityFinalNodes423",
    ends={
        Property(name="uml_TracedActivityFinalNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects424", type=uml_TracedActivityFinalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurationObservations425: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurationObservations425",
    ends={
        Property(name="uml_TracedDurationObservation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects426", type=uml_TracedDurationObservation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedInitialNodeActivations427: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedInitialNodeActivations427",
    ends={
        Property(name="IntermediateActivities_TracedInitialNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects428", type=IntermediateActivities_TracedInitialNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAcceptEventActions429: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAcceptEventActions429",
    ends={
        Property(name="uml_TracedAcceptEventAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects430", type=uml_TracedAcceptEventAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedEnumerationLiterals431: BinaryAssociation = BinaryAssociation(
    name="uml_tracedEnumerationLiterals431",
    ends={
        Property(name="uml_TracedEnumerationLiteral", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects432", type=uml_TracedEnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAddStructuralFeatureValueActions433: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAddStructuralFeatureValueActions433",
    ends={
        Property(name="uml_TracedAddStructuralFeatureValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects434", type=uml_TracedAddStructuralFeatureValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadLinkActions435: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadLinkActions435",
    ends={
        Property(name="uml_TracedReadLinkAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects436", type=uml_TracedReadLinkAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeEvents464: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeEvents464",
    ends={
        Property(name="uml_TracedTimeEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects465", type=uml_TracedTimeEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicBehaviors_tracedParameterValues466: BinaryAssociation = BinaryAssociation(
    name="basicBehaviors_tracedParameterValues466",
    ends={
        Property(name="BasicBehaviors_TracedParameterValue468", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects467", type=BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProtocolTransitions469: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProtocolTransitions469",
    ends={
        Property(name="uml_TracedProtocolTransition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects470", type=uml_TracedProtocolTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityFinalNodeActivations471: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityFinalNodeActivations471",
    ends={
        Property(name="IntermediateActivities_TracedActivityFinalNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects472", type=IntermediateActivities_TracedActivityFinalNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPackages473: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPackages473",
    ends={
        Property(name="uml_TracedPackage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects474", type=uml_TracedPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCollaborations447: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCollaborations447",
    ends={
        Property(name="uml_TracedCollaboration", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects448", type=uml_TracedCollaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateSignatures449: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateSignatures449",
    ends={
        Property(name="uml_TracedTemplateSignature", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects450", type=uml_TracedTemplateSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedBroadcastSignalActions451: BinaryAssociation = BinaryAssociation(
    name="uml_tracedBroadcastSignalActions451",
    ends={
        Property(name="uml_TracedBroadcastSignalAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects452", type=uml_TracedBroadcastSignalAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDeployments453: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDeployments453",
    ends={
        Property(name="uml_TracedDeployment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects454", type=uml_TracedDeployment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPorts455: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPorts455",
    ends={
        Property(name="uml_TracedPort", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects456", type=uml_TracedPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeIntervals457: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeIntervals457",
    ends={
        Property(name="uml_TracedTimeInterval", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects458", type=uml_TracedTimeInterval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtensions459: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtensions459",
    ends={
        Property(name="uml_TracedExtension", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects460", type=uml_TracedExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loci_tracedSemanticVisitors461: BinaryAssociation = BinaryAssociation(
    name="loci_tracedSemanticVisitors461",
    ends={
        Property(name="Loci_TracedSemanticVisitor463", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects462", type=Loci_TracedSemanticVisitor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSlots491: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSlots491",
    ends={
        Property(name="uml_TracedSlot", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects492", type=uml_TracedSlot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSignalEvents493: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSignalEvents493",
    ends={
        Property(name="uml_TracedSignalEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects494", type=uml_TracedSignalEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtensionPoints495: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtensionPoints495",
    ends={
        Property(name="uml_TracedExtensionPoint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects496", type=uml_TracedExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedJoinNodes497: BinaryAssociation = BinaryAssociation(
    name="uml_tracedJoinNodes497",
    ends={
        Property(name="uml_TracedJoinNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects498", type=uml_TracedJoinNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConstraints475: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConstraints475",
    ends={
        Property(name="uml_TracedConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects476", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGeneralizationSets477: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGeneralizationSets477",
    ends={
        Property(name="uml_TracedGeneralizationSet", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects478", type=uml_TracedGeneralizationSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReduceActions479: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReduceActions479",
    ends={
        Property(name="uml_TracedReduceAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects480", type=uml_TracedReduceAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInputPins481: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInputPins481",
    ends={
        Property(name="uml_TracedInputPin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects482", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSequenceNodes483: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSequenceNodes483",
    ends={
        Property(name="uml_TracedSequenceNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects484", type=uml_TracedSequenceNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractionConstraints485: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractionConstraints485",
    ends={
        Property(name="uml_TracedInteractionConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects486", type=uml_TracedInteractionConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedComponentRealizations487: BinaryAssociation = BinaryAssociation(
    name="uml_tracedComponentRealizations487",
    ends={
        Property(name="uml_TracedComponentRealization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects488", type=uml_TracedComponentRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAssociationClasss489: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAssociationClasss489",
    ends={
        Property(name="uml_TracedAssociationClass", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects490", type=uml_TracedAssociationClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedValueSpecificationActionActivations514: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedValueSpecificationActionActivations514",
    ends={
        Property(name="IntermediateActions_TracedValueSpecificationActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects515", type=IntermediateActions_TracedValueSpecificationActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStringExpressions516: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStringExpressions516",
    ends={
        Property(name="uml_TracedStringExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects517", type=uml_TracedStringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loci_tracedExecutors518: BinaryAssociation = BinaryAssociation(
    name="loci_tracedExecutors518",
    ends={
        Property(name="Loci_TracedExecutor520", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects519", type=Loci_TracedExecutor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedReadStructuralFeatureActionActivations521: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedReadStructuralFeatureActionActivations521",
    ends={
        Property(name="IntermediateActions_TracedReadStructuralFeatureActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects522", type=IntermediateActions_TracedReadStructuralFeatureActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedOutputPinActivations499: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedOutputPinActivations499",
    ends={
        Property(name="BasicActions_TracedOutputPinActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects500", type=BasicActions_TracedOutputPinActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStartObjectBehaviorActions501: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStartObjectBehaviorActions501",
    ends={
        Property(name="uml_TracedStartObjectBehaviorAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects502", type=uml_TracedStartObjectBehaviorAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedElementImports503: BinaryAssociation = BinaryAssociation(
    name="uml_tracedElementImports503",
    ends={
        Property(name="uml_TracedElementImport", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects504", type=uml_TracedElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCreateObjectActions505: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCreateObjectActions505",
    ends={
        Property(name="uml_TracedCreateObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects506", type=uml_TracedCreateObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExecutionEnvironments507: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExecutionEnvironments507",
    ends={
        Property(name="uml_TracedExecutionEnvironment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects508", type=uml_TracedExecutionEnvironment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOccurrenceSpecifications509: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOccurrenceSpecifications509",
    ends={
        Property(name="uml_TracedOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects510", type=uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityNodeActivationGroups511: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityNodeActivationGroups511",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivationGroup513", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects512", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStateMachines537: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStateMachines537",
    ends={
        Property(name="uml_TracedStateMachine", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects538", type=uml_TracedStateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedMergeNodeActivations539: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedMergeNodeActivations539",
    ends={
        Property(name="IntermediateActivities_TracedMergeNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects540", type=IntermediateActivities_TracedMergeNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractions541: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractions541",
    ends={
        Property(name="uml_TracedInteraction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects542", type=uml_TracedInteraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStereotypes523: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStereotypes523",
    ends={
        Property(name="uml_TracedStereotype", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects524", type=uml_TracedStereotype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInterfaces525: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInterfaces525",
    ends={
        Property(name="uml_TracedInterface", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects526", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConditionalNodes527: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConditionalNodes527",
    ends={
        Property(name="uml_TracedConditionalNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects528", type=uml_TracedConditionalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadLinkObjectEndActions529: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadLinkObjectEndActions529",
    ends={
        Property(name="uml_TracedReadLinkObjectEndAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects530", type=uml_TracedReadLinkObjectEndAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAnyReceiveEvents531: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAnyReceiveEvents531",
    ends={
        Property(name="uml_TracedAnyReceiveEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects532", type=uml_TracedAnyReceiveEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedComponents533: BinaryAssociation = BinaryAssociation(
    name="uml_tracedComponents533",
    ends={
        Property(name="uml_TracedComponent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects534", type=uml_TracedComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtensionEnds535: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtensionEnds535",
    ends={
        Property(name="uml_TracedExtensionEnd", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects536", type=uml_TracedExtensionEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLifelines555: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLifelines555",
    ends={
        Property(name="uml_TracedLifeline", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects556", type=uml_TracedLifeline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeObservations557: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeObservations557",
    ends={
        Property(name="uml_TracedTimeObservation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects558", type=uml_TracedTimeObservation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedControlTokens559: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedControlTokens559",
    ends={
        Property(name="IntermediateActivities_TracedControlToken", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects560", type=IntermediateActivities_TracedControlToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCreateLinkObjectActions561: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCreateLinkObjectActions561",
    ends={
        Property(name="uml_TracedCreateLinkObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects562", type=uml_TracedCreateLinkObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralStrings543: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralStrings543",
    ends={
        Property(name="uml_TracedLiteralString", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects544", type=uml_TracedLiteralString, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRealizations545: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRealizations545",
    ends={
        Property(name="uml_TracedRealization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects546", type=uml_TracedRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStartClassifierBehaviorActions547: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStartClassifierBehaviorActions547",
    ends={
        Property(name="uml_TracedStartClassifierBehaviorAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects548", type=uml_TracedStartClassifierBehaviorAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCallEvents549: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCallEvents549",
    ends={
        Property(name="uml_TracedCallEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects550", type=uml_TracedCallEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectableElementTemplateParameters551: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectableElementTemplateParameters551",
    ends={
        Property(name="uml_TracedConnectableElementTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects552", type=uml_TracedConnectableElementTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSendObjectActions553: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSendObjectActions553",
    ends={
        Property(name="uml_TracedSendObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects554", type=uml_TracedSendObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedEnumerations574: BinaryAssociation = BinaryAssociation(
    name="uml_tracedEnumerations574",
    ends={
        Property(name="uml_TracedEnumeration", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects575", type=uml_TracedEnumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCollaborationUses576: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCollaborationUses576",
    ends={
        Property(name="uml_TracedCollaborationUse", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects577", type=uml_TracedCollaborationUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivityPartitions578: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivityPartitions578",
    ends={
        Property(name="uml_TracedActivityPartition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects579", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExpansionRegions563: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExpansionRegions563",
    ends={
        Property(name="uml_TracedExpansionRegion", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects564", type=uml_TracedExpansionRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedBooleanValues565: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedBooleanValues565",
    ends={
        Property(name="Kernel_TracedBooleanValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects566", type=Kernel_TracedBooleanValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLoopNodes567: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLoopNodes567",
    ends={
        Property(name="uml_TracedLoopNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects568", type=uml_TracedLoopNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPrimitiveTypes569: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPrimitiveTypes569",
    ends={
        Property(name="uml_TracedPrimitiveType571", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects570", type=uml_TracedPrimitiveType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProtocolConformances572: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProtocolConformances572",
    ends={
        Property(name="uml_TracedProtocolConformance", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects573", type=uml_TracedProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedCallBehaviorActionActivations592: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedCallBehaviorActionActivations592",
    ends={
        Property(name="BasicActions_TracedCallBehaviorActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects593", type=BasicActions_TracedCallBehaviorActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedAddStructuralFeatureValueActionActivations594: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedAddStructuralFeatureValueActionActivations594",
    ends={
        Property(name="IntermediateActions_TracedAddStructuralFeatureValueActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects595", type=IntermediateActions_TracedAddStructuralFeatureValueActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClassifierTemplateParameters596: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClassifierTemplateParameters596",
    ends={
        Property(name="uml_TracedClassifierTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects597", type=uml_TracedClassifierTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLinkEndDestructionDatas580: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLinkEndDestructionDatas580",
    ends={
        Property(name="uml_TracedLinkEndDestructionData", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects581", type=uml_TracedLinkEndDestructionData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurationIntervals582: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurationIntervals582",
    ends={
        Property(name="uml_TracedDurationInterval", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects583", type=uml_TracedDurationInterval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedIncludes584: BinaryAssociation = BinaryAssociation(
    name="uml_tracedIncludes584",
    ends={
        Property(name="uml_TracedInclude", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects585", type=uml_TracedInclude, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDestructionOccurrenceSpecifications586: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDestructionOccurrenceSpecifications586",
    ends={
        Property(name="uml_TracedDestructionOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects587", type=uml_TracedDestructionOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStates588: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStates588",
    ends={
        Property(name="uml_TracedState", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects589", type=uml_TracedState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedObjectTokens590: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedObjectTokens590",
    ends={
        Property(name="IntermediateActivities_TracedObjectToken", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects591", type=IntermediateActivities_TracedObjectToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralUnlimitedNaturals611: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralUnlimitedNaturals611",
    ends={
        Property(name="uml_TracedLiteralUnlimitedNatural", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects612", type=uml_TracedLiteralUnlimitedNatural, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStructuredActivityNodes613: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStructuredActivityNodes613",
    ends={
        Property(name="uml_TracedStructuredActivityNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects614", type=uml_TracedStructuredActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAbstractions615: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAbstractions615",
    ends={
        Property(name="uml_TracedAbstraction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects616", type=uml_TracedAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivityParameterNodes598: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivityParameterNodes598",
    ends={
        Property(name="uml_TracedActivityParameterNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects599", type=uml_TracedActivityParameterNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integerFunctions_tracedIntegerLessFunctionBehaviorExecutions600: BinaryAssociation = BinaryAssociation(
    name="integerFunctions_tracedIntegerLessFunctionBehaviorExecutions600",
    ends={
        Property(name="IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects601", type=IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedParameterSets602: BinaryAssociation = BinaryAssociation(
    name="uml_tracedParameterSets602",
    ends={
        Property(name="uml_TracedParameterSet", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects603", type=uml_TracedParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurations604: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurations604",
    ends={
        Property(name="uml_TracedDuration", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects605", type=uml_TracedDuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClasss606: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClasss606",
    ends={
        Property(name="uml_TracedClass608", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects607", type=uml_TracedClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedUsages609: BinaryAssociation = BinaryAssociation(
    name="uml_tracedUsages609",
    ends={
        Property(name="uml_TracedUsage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects610", type=uml_TracedUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCreateLinkActions627: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCreateLinkActions627",
    ends={
        Property(name="uml_TracedCreateLinkAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects628", type=uml_TracedCreateLinkAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGeneralizations629: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGeneralizations629",
    ends={
        Property(name="uml_TracedGeneralization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects630", type=uml_TracedGeneralization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPartDecompositions631: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPartDecompositions631",
    ends={
        Property(name="uml_TracedPartDecomposition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects632", type=uml_TracedPartDecomposition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedOpaqueActionActivations617: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedOpaqueActionActivations617",
    ends={
        Property(name="BasicActions_TracedOpaqueActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects618", type=BasicActions_TracedOpaqueActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedLiteralBooleanEvaluations619: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedLiteralBooleanEvaluations619",
    ends={
        Property(name="Kernel_TracedLiteralBooleanEvaluation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects620", type=Kernel_TracedLiteralBooleanEvaluation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadStructuralFeatureActions621: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadStructuralFeatureActions621",
    ends={
        Property(name="uml_TracedReadStructuralFeatureAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects622", type=uml_TracedReadStructuralFeatureAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedMergeNodes623: BinaryAssociation = BinaryAssociation(
    name="uml_tracedMergeNodes623",
    ends={
        Property(name="uml_TracedMergeNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects624", type=uml_TracedMergeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRedefinableTemplateSignatures625: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRedefinableTemplateSignatures625",
    ends={
        Property(name="uml_TracedRedefinableTemplateSignature", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects626", type=uml_TracedRedefinableTemplateSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedMessages643: BinaryAssociation = BinaryAssociation(
    name="uml_tracedMessages643",
    ends={
        Property(name="uml_TracedMessage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects644", type=uml_TracedMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralBooleans645: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralBooleans645",
    ends={
        Property(name="uml_TracedLiteralBoolean", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects646", type=uml_TracedLiteralBoolean, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOperationTemplateParameters633: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOperationTemplateParameters633",
    ends={
        Property(name="uml_TracedOperationTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects634", type=uml_TracedOperationTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadLinkObjectEndQualifierActions635: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadLinkObjectEndQualifierActions635",
    ends={
        Property(name="uml_TracedReadLinkObjectEndQualifierAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects636", type=uml_TracedReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateParameterSubstitutions637: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateParameterSubstitutions637",
    ends={
        Property(name="uml_TracedTemplateParameterSubstitution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects638", type=uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtends639: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtends639",
    ends={
        Property(name="uml_TracedExtend", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects640", type=uml_TracedExtend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadVariableActions641: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadVariableActions641",
    ends={
        Property(name="uml_TracedReadVariableAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects642", type=uml_TracedReadVariableAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedDecisionNodeActivations655: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedDecisionNodeActivations655",
    ends={
        Property(name="IntermediateActivities_TracedDecisionNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects656", type=IntermediateActivities_TracedDecisionNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProfileApplications657: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProfileApplications657",
    ends={
        Property(name="uml_TracedProfileApplication", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects658", type=uml_TracedProfileApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedQualifierValues647: BinaryAssociation = BinaryAssociation(
    name="uml_tracedQualifierValues647",
    ends={
        Property(name="uml_TracedQualifierValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects648", type=uml_TracedQualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInitialNodes649: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInitialNodes649",
    ends={
        Property(name="uml_TracedInitialNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects650", type=uml_TracedInitialNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralIntegers651: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralIntegers651",
    ends={
        Property(name="uml_TracedLiteralInteger", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects652", type=uml_TracedLiteralInteger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClearVariableActions653: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClearVariableActions653",
    ends={
        Property(name="uml_TracedClearVariableAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects654", type=uml_TracedClearVariableAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedParameters669: BinaryAssociation = BinaryAssociation(
    name="uml_tracedParameters669",
    ends={
        Property(name="uml_TracedParameter671", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects670", type=uml_TracedParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActionInputPins672: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActionInputPins672",
    ends={
        Property(name="uml_TracedActionInputPin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects673", type=uml_TracedActionInputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateParameters659: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateParameters659",
    ends={
        Property(name="uml_TracedTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects660", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectorEnds661: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectorEnds661",
    ends={
        Property(name="uml_TracedConnectorEnd", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects662", type=uml_TracedConnectorEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedMessageOccurrenceSpecifications663: BinaryAssociation = BinaryAssociation(
    name="uml_tracedMessageOccurrenceSpecifications663",
    ends={
        Property(name="uml_TracedMessageOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects664", type=uml_TracedMessageOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurationConstraints665: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurationConstraints665",
    ends={
        Property(name="uml_TracedDurationConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects666", type=uml_TracedDurationConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedImages667: BinaryAssociation = BinaryAssociation(
    name="uml_tracedImages667",
    ends={
        Property(name="uml_TracedImage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects668", type=uml_TracedImage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedForkNodeActivations682: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedForkNodeActivations682",
    ends={
        Property(name="IntermediateActivities_TracedForkNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects683", type=IntermediateActivities_TracedForkNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedIntervalConstraints684: BinaryAssociation = BinaryAssociation(
    name="uml_tracedIntervalConstraints684",
    ends={
        Property(name="uml_TracedIntervalConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects685", type=uml_TracedIntervalConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedTokens686: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedTokens686",
    ends={
        Property(name="IntermediateActivities_TracedToken688", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects687", type=IntermediateActivities_TracedToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTriggers674: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTriggers674",
    ends={
        Property(name="uml_TracedTrigger", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects675", type=uml_TracedTrigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCallOperationActions676: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCallOperationActions676",
    ends={
        Property(name="uml_TracedCallOperationAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects677", type=uml_TracedCallOperationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProfiles678: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProfiles678",
    ends={
        Property(name="uml_TracedProfile", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects679", type=uml_TracedProfile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedIntervals680: BinaryAssociation = BinaryAssociation(
    name="uml_tracedIntervals680",
    ends={
        Property(name="uml_TracedInterval", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects681", type=uml_TracedInterval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProtocolStateMachines697: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProtocolStateMachines697",
    ends={
        Property(name="uml_TracedProtocolStateMachine", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects698", type=uml_TracedProtocolStateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOutputPins699: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOutputPins699",
    ends={
        Property(name="uml_TracedOutputPin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects700", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInstanceSpecifications689: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInstanceSpecifications689",
    ends={
        Property(name="uml_TracedInstanceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects690", type=uml_TracedInstanceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedValuePins691: BinaryAssociation = BinaryAssociation(
    name="uml_tracedValuePins691",
    ends={
        Property(name="uml_TracedValuePin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects692", type=uml_TracedValuePin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integerFunctions_tracedIntegerGreaterFunctionBehaviorExecutions693: BinaryAssociation = BinaryAssociation(
    name="integerFunctions_tracedIntegerGreaterFunctionBehaviorExecutions693",
    ends={
        Property(name="IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects694", type=IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadIsClassifiedObjectActions695: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadIsClassifiedObjectActions695",
    ends={
        Property(name="uml_TracedReadIsClassifiedObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects696", type=uml_TracedReadIsClassifiedObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInterruptibleActivityRegions712: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInterruptibleActivityRegions712",
    ends={
        Property(name="uml_TracedInterruptibleActivityRegion", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects713", type=uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDestroyLinkActions714: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDestroyLinkActions714",
    ends={
        Property(name="uml_TracedDestroyLinkAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects715", type=uml_TracedDestroyLinkAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedOffers701: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedOffers701",
    ends={
        Property(name="IntermediateActivities_TracedOffer703", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects702", type=IntermediateActivities_TracedOffer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityParameterNodeActivations704: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityParameterNodeActivations704",
    ends={
        Property(name="IntermediateActivities_TracedActivityParameterNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects705", type=IntermediateActivities_TracedActivityParameterNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDecisionNodes706: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDecisionNodes706",
    ends={
        Property(name="uml_TracedDecisionNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects707", type=uml_TracedDecisionNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedValueSpecificationActions708: BinaryAssociation = BinaryAssociation(
    name="uml_tracedValueSpecificationActions708",
    ends={
        Property(name="uml_TracedValueSpecificationAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects709", type=uml_TracedValueSpecificationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRegions710: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRegions710",
    ends={
        Property(name="uml_TracedRegion", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects711", type=uml_TracedRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPseudostates724: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPseudostates724",
    ends={
        Property(name="uml_TracedPseudostate", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects725", type=uml_TracedPseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedUseCases726: BinaryAssociation = BinaryAssociation(
    name="uml_tracedUseCases726",
    ends={
        Property(name="uml_TracedUseCase", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects727", type=uml_TracedUseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedFinalStates716: BinaryAssociation = BinaryAssociation(
    name="uml_tracedFinalStates716",
    ends={
        Property(name="uml_TracedFinalState", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects717", type=uml_TracedFinalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integerFunctions_tracedIntegerPlusFunctionBehaviorExecutions718: BinaryAssociation = BinaryAssociation(
    name="integerFunctions_tracedIntegerPlusFunctionBehaviorExecutions718",
    ends={
        Property(name="IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects719", type=IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractionOperands720: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractionOperands720",
    ends={
        Property(name="uml_TracedInteractionOperand", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects721", type=uml_TracedInteractionOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInformationFlows722: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInformationFlows722",
    ends={
        Property(name="uml_TracedInformationFlow", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects723", type=uml_TracedInformationFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInstanceValues736: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInstanceValues736",
    ends={
        Property(name="uml_TracedInstanceValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects737", type=uml_TracedInstanceValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDependencys738: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDependencys738",
    ends={
        Property(name="uml_TracedDependency", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects739", type=uml_TracedDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeExpressions740: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeExpressions740",
    ends={
        Property(name="uml_TracedTimeExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects741", type=uml_TracedTimeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReplyActions728: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReplyActions728",
    ends={
        Property(name="uml_TracedReplyAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects729", type=uml_TracedReplyAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedCreateObjectActionActivations730: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedCreateObjectActionActivations730",
    ends={
        Property(name="IntermediateActions_TracedCreateObjectActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects731", type=IntermediateActions_TracedCreateObjectActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCombinedFragments732: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCombinedFragments732",
    ends={
        Property(name="uml_TracedCombinedFragment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects733", type=uml_TracedCombinedFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClauses734: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClauses734",
    ends={
        Property(name="uml_TracedClause", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects735", type=uml_TracedClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTransitions751: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTransitions751",
    ends={
        Property(name="uml_TracedTransition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects752", type=uml_TracedTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLinkEndDatas753: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLinkEndDatas753",
    ends={
        Property(name="uml_TracedLinkEndData", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects754", type=uml_TracedLinkEndData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityEdgeInstances742: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityEdgeInstances742",
    ends={
        Property(name="IntermediateActivities_TracedActivityEdgeInstance744", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects743", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedManifestations745: BinaryAssociation = BinaryAssociation(
    name="uml_tracedManifestations745",
    ends={
        Property(name="uml_TracedManifestation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects746", type=uml_TracedManifestation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadExtentActions747: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadExtentActions747",
    ends={
        Property(name="uml_TracedReadExtentAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects748", type=uml_TracedReadExtentAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedInputPinActivations749: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedInputPinActivations749",
    ends={
        Property(name="BasicActions_TracedInputPinActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects750", type=BasicActions_TracedInputPinActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedObjectFlows763: BinaryAssociation = BinaryAssociation(
    name="uml_tracedObjectFlows763",
    ends={
        Property(name="uml_TracedObjectFlow", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects764", type=uml_TracedObjectFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedChangeEvents765: BinaryAssociation = BinaryAssociation(
    name="uml_tracedChangeEvents765",
    ends={
        Property(name="uml_TracedChangeEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects766", type=uml_TracedChangeEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDestroyObjectActions767: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDestroyObjectActions767",
    ends={
        Property(name="uml_TracedDestroyObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects768", type=uml_TracedDestroyObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input_tracedInputParameterValuess755: BinaryAssociation = BinaryAssociation(
    name="input_tracedInputParameterValuess755",
    ends={
        Property(name="Input_TracedInputParameterValues", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects756", type=Input_TracedInputParameterValues, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedNodes757: BinaryAssociation = BinaryAssociation(
    name="uml_tracedNodes757",
    ends={
        Property(name="uml_TracedNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects758", type=uml_TracedNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPackageMerges759: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPackageMerges759",
    ends={
        Property(name="uml_TracedPackageMerge", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects760", type=uml_TracedPackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedModels761: BinaryAssociation = BinaryAssociation(
    name="uml_tracedModels761",
    ends={
        Property(name="uml_TracedModel", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects762", type=uml_TracedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedForkNodes769: BinaryAssociation = BinaryAssociation(
    name="uml_tracedForkNodes769",
    ends={
        Property(name="uml_TracedForkNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects770", type=uml_TracedForkNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReceptions779: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReceptions779",
    ends={
        Property(name="uml_TracedReception", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects780", type=uml_TracedReception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRaiseExceptionActions781: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRaiseExceptionActions781",
    ends={
        Property(name="uml_TracedRaiseExceptionAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects782", type=uml_TracedRaiseExceptionAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSignals771: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSignals771",
    ends={
        Property(name="uml_TracedSignal", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects772", type=uml_TracedSignal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedComments773: BinaryAssociation = BinaryAssociation(
    name="uml_tracedComments773",
    ends={
        Property(name="uml_TracedComment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects774", type=uml_TracedComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralNulls775: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralNulls775",
    ends={
        Property(name="uml_TracedLiteralNull", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects776", type=uml_TracedLiteralNull, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExpansionNodes777: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExpansionNodes777",
    ends={
        Property(name="uml_TracedExpansionNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects778", type=uml_TracedExpansionNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTestIdentityActions790: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTestIdentityActions790",
    ends={
        Property(name="uml_TracedTestIdentityAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects791", type=uml_TracedTestIdentityAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedControlFlows792: BinaryAssociation = BinaryAssociation(
    name="uml_tracedControlFlows792",
    ends={
        Property(name="uml_TracedControlFlow", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects793", type=uml_TracedControlFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOperations794: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOperations794",
    ends={
        Property(name="uml_TracedOperation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects795", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityNodeActivations783: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityNodeActivations783",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivation785", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects784", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAddVariableValueActions786: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAddVariableValueActions786",
    ends={
        Property(name="uml_TracedAddVariableValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects787", type=uml_TracedAddVariableValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClearAssociationActions788: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClearAssociationActions788",
    ends={
        Property(name="uml_TracedClearAssociationAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects789", type=uml_TracedClearAssociationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExceptionHandlers800: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExceptionHandlers800",
    ends={
        Property(name="uml_TracedExceptionHandler", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects801", type=uml_TracedExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPackageImports796: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPackageImports796",
    ends={
        Property(name="uml_TracedPackageImport", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects797", type=uml_TracedPackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExecutionOccurrenceSpecifications798: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExecutionOccurrenceSpecifications798",
    ends={
        Property(name="uml_TracedExecutionOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects799", type=uml_TracedExecutionOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStateInvariants808: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStateInvariants808",
    ends={
        Property(name="uml_TracedStateInvariant", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects809", type=uml_TracedStateInvariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralReals810: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralReals810",
    ends={
        Property(name="uml_TracedLiteralReal", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects811", type=uml_TracedLiteralReal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRemoveVariableValueActions812: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRemoveVariableValueActions812",
    ends={
        Property(name="uml_TracedRemoveVariableValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects813", type=uml_TracedRemoveVariableValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedVariables802: BinaryAssociation = BinaryAssociation(
    name="uml_tracedVariables802",
    ends={
        Property(name="uml_TracedVariable", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects803", type=uml_TracedVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractionUses804: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractionUses804",
    ends={
        Property(name="uml_TracedInteractionUse", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects805", type=uml_TracedInteractionUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAssociations806: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAssociations806",
    ends={
        Property(name="uml_TracedAssociation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects807", type=uml_TracedAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGeneralOrderings820: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGeneralOrderings820",
    ends={
        Property(name="uml_TracedGeneralOrdering", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects821", type=uml_TracedGeneralOrdering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCallBehaviorActions822: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCallBehaviorActions822",
    ends={
        Property(name="uml_TracedCallBehaviorAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects823", type=uml_TracedCallBehaviorAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReclassifyObjectActions824: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReclassifyObjectActions824",
    ends={
        Property(name="uml_TracedReclassifyObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects825", type=uml_TracedReclassifyObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDevices814: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDevices814",
    ends={
        Property(name="uml_TracedDevice", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects815", type=uml_TracedDevice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSubstitutions816: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSubstitutions816",
    ends={
        Property(name="uml_TracedSubstitution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects817", type=uml_TracedSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGates818: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGates818",
    ends={
        Property(name="uml_TracedGate", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects819", type=uml_TracedGate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadSelfActions832: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadSelfActions832",
    ends={
        Property(name="uml_TracedReadSelfAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects833", type=uml_TracedReadSelfAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAcceptCallActions834: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAcceptCallActions834",
    ends={
        Property(name="uml_TracedAcceptCallAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects835", type=uml_TracedAcceptCallAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivitys826: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivitys826",
    ends={
        Property(name="uml_TracedActivity", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects827", type=uml_TracedActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectionPointReferences828: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectionPointReferences828",
    ends={
        Property(name="uml_TracedConnectionPointReference", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects829", type=uml_TracedConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActionExecutionSpecifications830: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActionExecutionSpecifications830",
    ends={
        Property(name="uml_TracedActionExecutionSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects831", type=uml_TracedActionExecutionSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLinkEndCreationDatas836: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLinkEndCreationDatas836",
    ends={
        Property(name="uml_TracedLinkEndCreationData", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects837", type=uml_TracedLinkEndCreationData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityExecutions838: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityExecutions838",
    ends={
        Property(name="IntermediateActivities_TracedActivityExecution840", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects839", type=IntermediateActivities_TracedActivityExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateBindings841: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateBindings841",
    ends={
        Property(name="uml_TracedTemplateBinding", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects842", type=uml_TracedTemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOpaqueExpressions849: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOpaqueExpressions849",
    ends={
        Property(name="uml_TracedOpaqueExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects850", type=uml_TracedOpaqueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClearStructuralFeatureActions843: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClearStructuralFeatureActions843",
    ends={
        Property(name="uml_TracedClearStructuralFeatureAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects844", type=uml_TracedClearStructuralFeatureAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loci_tracedExecutionEnvironments845: BinaryAssociation = BinaryAssociation(
    name="loci_tracedExecutionEnvironments845",
    ends={
        Property(name="Loci_TracedExecutionEnvironment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects846", type=Loci_TracedExecutionEnvironment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedLiteralIntegerEvaluations847: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedLiteralIntegerEvaluations847",
    ends={
        Property(name="Kernel_TracedLiteralIntegerEvaluation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects848", type=Kernel_TracedLiteralIntegerEvaluation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedUnmarshallActions859: BinaryAssociation = BinaryAssociation(
    name="uml_tracedUnmarshallActions859",
    ends={
        Property(name="uml_TracedUnmarshallAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects860", type=uml_TracedUnmarshallAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCentralBufferNodes861: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCentralBufferNodes861",
    ends={
        Property(name="uml_TracedCentralBufferNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects862", type=uml_TracedCentralBufferNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedFunctionBehaviors851: BinaryAssociation = BinaryAssociation(
    name="uml_tracedFunctionBehaviors851",
    ends={
        Property(name="uml_TracedFunctionBehavior", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects852", type=uml_TracedFunctionBehavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDeploymentSpecifications853: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDeploymentSpecifications853",
    ends={
        Property(name="uml_TracedDeploymentSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects854", type=uml_TracedDeploymentSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActors855: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActors855",
    ends={
        Property(name="uml_TracedActor", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects856", type=uml_TracedActor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedBehaviorExecutionSpecifications857: BinaryAssociation = BinaryAssociation(
    name="uml_tracedBehaviorExecutionSpecifications857",
    ends={
        Property(name="uml_TracedBehaviorExecutionSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects858", type=uml_TracedBehaviorExecutionSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeTrace871: BinaryAssociation = BinaryAssociation(
    name="typeTrace871",
    ends={
        Property(name="PrimitiveValue_type_Value873", type=umlTrace_Kernel_TracedPrimitiveValue, multiplicity=Multiplicity(1, 1)),
        Property(name="parent872", type=PrimitiveValue_type_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification_EvaluationTrace874: BinaryAssociation = BinaryAssociation(
    name="specification_EvaluationTrace874",
    ends={
        Property(name="Evaluation_specification_Evaluation_Value876", type=umlTrace_Kernel_TracedEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent875", type=Evaluation_specification_Evaluation_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locus_EvaluationTrace877: BinaryAssociation = BinaryAssociation(
    name="locus_EvaluationTrace877",
    ends={
        Property(name="Evaluation_locus_Evaluation_Value879", type=umlTrace_Kernel_TracedEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent878", type=Evaluation_locus_Evaluation_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value_BooleanValueTrace880: BinaryAssociation = BinaryAssociation(
    name="value_BooleanValueTrace880",
    ends={
        Property(name="BooleanValue_value_BooleanValue_Value882", type=umlTrace_Kernel_TracedBooleanValue, multiplicity=Multiplicity(1, 1)),
        Property(name="parent881", type=BooleanValue_value_BooleanValue_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typesTrace863: BinaryAssociation = BinaryAssociation(
    name="typesTrace863",
    ends={
        Property(name="Object_types_Value864", type=umlTrace_Kernel_TracedObject, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=Object_types_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referentTrace865: BinaryAssociation = BinaryAssociation(
    name="referentTrace865",
    ends={
        Property(name="Reference_referent_Value867", type=umlTrace_Kernel_TracedReference, multiplicity=Multiplicity(1, 1)),
        Property(name="parent866", type=Reference_referent_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value_IntegerValueTrace868: BinaryAssociation = BinaryAssociation(
    name="value_IntegerValueTrace868",
    ends={
        Property(name="IntegerValue_value_IntegerValue_Value870", type=umlTrace_Kernel_TracedIntegerValue, multiplicity=Multiplicity(1, 1)),
        Property(name="parent869", type=IntegerValue_value_IntegerValue_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values_ParameterValueTrace898: BinaryAssociation = BinaryAssociation(
    name="values_ParameterValueTrace898",
    ends={
        Property(name="ParameterValue_values_ParameterValue_Value900", type=umlTrace_BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="parent899", type=ParameterValue_values_ParameterValue_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter_ParameterValueTrace901: BinaryAssociation = BinaryAssociation(
    name="parameter_ParameterValueTrace901",
    ends={
        Property(name="ParameterValue_parameter_ParameterValue_Value903", type=umlTrace_BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="parent902", type=ParameterValue_parameter_ParameterValue_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterValuesTrace904: BinaryAssociation = BinaryAssociation(
    name="parameterValuesTrace904",
    ends={
        Property(name="Execution_parameterValues_Value906", type=umlTrace_BasicBehaviors_TracedExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="parent905", type=Execution_parameterValues_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contextTrace907: BinaryAssociation = BinaryAssociation(
    name="contextTrace907",
    ends={
        Property(name="Execution_context_Value909", type=umlTrace_BasicBehaviors_TracedExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="parent908", type=Execution_context_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureValuesTrace883: BinaryAssociation = BinaryAssociation(
    name="featureValuesTrace883",
    ends={
        Property(name="CompoundValue_featureValues_Value885", type=umlTrace_Kernel_TracedCompoundValue, multiplicity=Multiplicity(1, 1)),
        Property(name="parent884", type=CompoundValue_featureValues_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values_FeatureValueTrace886: BinaryAssociation = BinaryAssociation(
    name="values_FeatureValueTrace886",
    ends={
        Property(name="FeatureValue_values_FeatureValue_Value888", type=umlTrace_Kernel_TracedFeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="parent887", type=FeatureValue_values_FeatureValue_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureTrace889: BinaryAssociation = BinaryAssociation(
    name="featureTrace889",
    ends={
        Property(name="FeatureValue_feature_Value891", type=umlTrace_Kernel_TracedFeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="parent890", type=FeatureValue_feature_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
positionTrace892: BinaryAssociation = BinaryAssociation(
    name="positionTrace892",
    ends={
        Property(name="FeatureValue_position_Value894", type=umlTrace_Kernel_TracedFeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="parent893", type=FeatureValue_position_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locus_ExtensionalValueTrace895: BinaryAssociation = BinaryAssociation(
    name="locus_ExtensionalValueTrace895",
    ends={
        Property(name="ExtensionalValue_locus_ExtensionalValue_Value897", type=umlTrace_Kernel_TracedExtensionalValue, multiplicity=Multiplicity(1, 1)),
        Property(name="parent896", type=ExtensionalValue_locus_ExtensionalValue_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeActivationsTrace922: BinaryAssociation = BinaryAssociation(
    name="nodeActivationsTrace922",
    ends={
        Property(name="ActivityNodeActivationGroup_nodeActivations_Value924", type=umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="parent923", type=ActivityNodeActivationGroup_nodeActivations_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activityExecutionTrace925: BinaryAssociation = BinaryAssociation(
    name="activityExecutionTrace925",
    ends={
        Property(name="ActivityNodeActivationGroup_activityExecution_Value927", type=umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="parent926", type=ActivityNodeActivationGroup_activityExecution_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeInstancesTrace928: BinaryAssociation = BinaryAssociation(
    name="edgeInstancesTrace928",
    ends={
        Property(name="ActivityNodeActivationGroup_edgeInstances_Value930", type=umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="parent929", type=ActivityNodeActivationGroup_edgeInstances_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueTrace931: BinaryAssociation = BinaryAssociation(
    name="valueTrace931",
    ends={
        Property(name="ObjectToken_value_Value933", type=umlTrace_IntermediateActivities_TracedObjectToken, multiplicity=Multiplicity(1, 1)),
        Property(name="parent932", type=ObjectToken_value_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
remainingOffersCountTrace910: BinaryAssociation = BinaryAssociation(
    name="remainingOffersCountTrace910",
    ends={
        Property(name="ForkedToken_remainingOffersCount_Value912", type=umlTrace_IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="parent911", type=ForkedToken_remainingOffersCount_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseTokenTrace913: BinaryAssociation = BinaryAssociation(
    name="baseTokenTrace913",
    ends={
        Property(name="ForkedToken_baseToken_Value915", type=umlTrace_IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="parent914", type=ForkedToken_baseToken_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseTokenIsWithdrawnTrace916: BinaryAssociation = BinaryAssociation(
    name="baseTokenIsWithdrawnTrace916",
    ends={
        Property(name="ForkedToken_baseTokenIsWithdrawn_Value918", type=umlTrace_IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="parent917", type=ForkedToken_baseTokenIsWithdrawn_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
offeredTokenCountTrace919: BinaryAssociation = BinaryAssociation(
    name="offeredTokenCountTrace919",
    ends={
        Property(name="ObjectNodeActivation_offeredTokenCount_Value921", type=umlTrace_IntermediateActivities_TracedObjectNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent920", type=ObjectNodeActivation_offeredTokenCount_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceTrace952: BinaryAssociation = BinaryAssociation(
    name="sourceTrace952",
    ends={
        Property(name="ActivityEdgeInstance_source_Value954", type=umlTrace_IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="parent953", type=ActivityEdgeInstance_source_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
heldTokensTrace955: BinaryAssociation = BinaryAssociation(
    name="heldTokensTrace955",
    ends={
        Property(name="ActivityNodeActivation_heldTokens_Value957", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent956", type=ActivityNodeActivation_heldTokens_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node_ActivityNodeActivationTrace958: BinaryAssociation = BinaryAssociation(
    name="node_ActivityNodeActivationTrace958",
    ends={
        Property(name="ActivityNodeActivation_node_ActivityNodeActivation_Value960", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent959", type=ActivityNodeActivation_node_ActivityNodeActivation_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
runningTrace961: BinaryAssociation = BinaryAssociation(
    name="runningTrace961",
    ends={
        Property(name="ActivityNodeActivation_running_Value963", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent962", type=ActivityNodeActivation_running_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isRunningTrace964: BinaryAssociation = BinaryAssociation(
    name="isRunningTrace964",
    ends={
        Property(name="ActivityNodeActivation_isRunning_Value966", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent965", type=ActivityNodeActivation_isRunning_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingEdgesTrace967: BinaryAssociation = BinaryAssociation(
    name="outgoingEdgesTrace967",
    ends={
        Property(name="ActivityNodeActivation_outgoingEdges_Value969", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent968", type=ActivityNodeActivation_outgoingEdges_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingEdgesTrace970: BinaryAssociation = BinaryAssociation(
    name="incomingEdgesTrace970",
    ends={
        Property(name="ActivityNodeActivation_incomingEdges_Value972", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent971", type=ActivityNodeActivation_incomingEdges_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
holderTrace934: BinaryAssociation = BinaryAssociation(
    name="holderTrace934",
    ends={
        Property(name="Token_holder_Value936", type=umlTrace_IntermediateActivities_TracedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="parent935", type=Token_holder_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
offeredTokensTrace937: BinaryAssociation = BinaryAssociation(
    name="offeredTokensTrace937",
    ends={
        Property(name="Offer_offeredTokens_Value939", type=umlTrace_IntermediateActivities_TracedOffer, multiplicity=Multiplicity(1, 1)),
        Property(name="parent938", type=Offer_offeredTokens_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group_ActivityEdgeInstanceTrace940: BinaryAssociation = BinaryAssociation(
    name="group_ActivityEdgeInstanceTrace940",
    ends={
        Property(name="ActivityEdgeInstance_group_ActivityEdgeInstance_Value942", type=umlTrace_IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="parent941", type=ActivityEdgeInstance_group_ActivityEdgeInstance_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
offersTrace943: BinaryAssociation = BinaryAssociation(
    name="offersTrace943",
    ends={
        Property(name="ActivityEdgeInstance_offers_Value945", type=umlTrace_IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="parent944", type=ActivityEdgeInstance_offers_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetTrace946: BinaryAssociation = BinaryAssociation(
    name="targetTrace946",
    ends={
        Property(name="ActivityEdgeInstance_target_Value948", type=umlTrace_IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="parent947", type=ActivityEdgeInstance_target_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge_ActivityEdgeInstanceTrace949: BinaryAssociation = BinaryAssociation(
    name="edge_ActivityEdgeInstanceTrace949",
    ends={
        Property(name="ActivityEdgeInstance_edge_ActivityEdgeInstance_Value951", type=umlTrace_IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="parent950", type=ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executorTrace994: BinaryAssociation = BinaryAssociation(
    name="executorTrace994",
    ends={
        Property(name="Locus_executor_Value996", type=umlTrace_Loci_TracedLocus, multiplicity=Multiplicity(1, 1)),
        Property(name="parent995", type=Locus_executor_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
runtimeModelElementTrace997: BinaryAssociation = BinaryAssociation(
    name="runtimeModelElementTrace997",
    ends={
        Property(name="SemanticVisitor_runtimeModelElement_Value999", type=umlTrace_Loci_TracedSemanticVisitor, multiplicity=Multiplicity(1, 1)),
        Property(name="parent998", type=SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locus_ExecutorTrace1000: BinaryAssociation = BinaryAssociation(
    name="locus_ExecutorTrace1000",
    ends={
        Property(name="Executor_locus_Executor_Value1002", type=umlTrace_Loci_TracedExecutor, multiplicity=Multiplicity(1, 1)),
        Property(name="parent1001", type=Executor_locus_Executor_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locus_ExecutionEnvironmentTrace1003: BinaryAssociation = BinaryAssociation(
    name="locus_ExecutionEnvironmentTrace1003",
    ends={
        Property(name="ExecutionEnvironment_locus_ExecutionEnvironment_Value1005", type=umlTrace_Loci_TracedExecutionEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="parent1004", type=ExecutionEnvironment_locus_ExecutionEnvironment_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group_ActivityNodeActivationTrace973: BinaryAssociation = BinaryAssociation(
    name="group_ActivityNodeActivationTrace973",
    ends={
        Property(name="ActivityNodeActivation_group_ActivityNodeActivation_Value975", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent974", type=ActivityNodeActivation_group_ActivityNodeActivation_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activationGroupTrace976: BinaryAssociation = BinaryAssociation(
    name="activationGroupTrace976",
    ends={
        Property(name="ActivityExecution_activationGroup_Value978", type=umlTrace_IntermediateActivities_TracedActivityExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="parent977", type=ActivityExecution_activationGroup_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
builtInTypesTrace979: BinaryAssociation = BinaryAssociation(
    name="builtInTypesTrace979",
    ends={
        Property(name="ExecutionFactory_builtInTypes_Value981", type=umlTrace_Loci_TracedExecutionFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="parent980", type=ExecutionFactory_builtInTypes_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveBehaviorPrototypesTrace982: BinaryAssociation = BinaryAssociation(
    name="primitiveBehaviorPrototypesTrace982",
    ends={
        Property(name="ExecutionFactory_primitiveBehaviorPrototypes_Value984", type=umlTrace_Loci_TracedExecutionFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="parent983", type=ExecutionFactory_primitiveBehaviorPrototypes_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locus_ExecutionFactoryTrace985: BinaryAssociation = BinaryAssociation(
    name="locus_ExecutionFactoryTrace985",
    ends={
        Property(name="ExecutionFactory_locus_ExecutionFactory_Value987", type=umlTrace_Loci_TracedExecutionFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="parent986", type=ExecutionFactory_locus_ExecutionFactory_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
factoryTrace988: BinaryAssociation = BinaryAssociation(
    name="factoryTrace988",
    ends={
        Property(name="Locus_factory_Value990", type=umlTrace_Loci_TracedLocus, multiplicity=Multiplicity(1, 1)),
        Property(name="parent989", type=Locus_factory_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionalValuesTrace991: BinaryAssociation = BinaryAssociation(
    name="extensionalValuesTrace991",
    ends={
        Property(name="Locus_extensionalValues_Value993", type=umlTrace_Loci_TracedLocus, multiplicity=Multiplicity(1, 1)),
        Property(name="parent992", type=Locus_extensionalValues_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callExecutionsTrace1012: BinaryAssociation = BinaryAssociation(
    name="callExecutionsTrace1012",
    ends={
        Property(name="CallActionActivation_callExecutions_Value1014", type=umlTrace_BasicActions_TracedCallActionActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent1013", type=CallActionActivation_callExecutions_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionActivationTrace1015: BinaryAssociation = BinaryAssociation(
    name="actionActivationTrace1015",
    ends={
        Property(name="PinActivation_actionActivation_Value1017", type=umlTrace_BasicActions_TracedPinActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent1016", type=PinActivation_actionActivation_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
count_tempTrace1018: BinaryAssociation = BinaryAssociation(
    name="count_tempTrace1018",
    ends={
        Property(name="PinActivation_count_temp_Value1020", type=umlTrace_BasicActions_TracedPinActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent1019", type=PinActivation_count_temp_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pinActivationsTrace1006: BinaryAssociation = BinaryAssociation(
    name="pinActivationsTrace1006",
    ends={
        Property(name="ActionActivation_pinActivations_Value1008", type=umlTrace_BasicActions_TracedActionActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent1007", type=ActionActivation_pinActivations_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firingTrace1009: BinaryAssociation = BinaryAssociation(
    name="firingTrace1009",
    ends={
        Property(name="ActionActivation_firing_Value1011", type=umlTrace_BasicActions_TracedActionActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="parent1010", type=ActionActivation_firing_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalObject1037: BinaryAssociation = BinaryAssociation(
    name="originalObject1037",
    ends={
        Property(name="uml_umlTrace_Connector", type=umlTrace_uml_TracedConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnector1038", type=uml_umlTrace_Connector, multiplicity=Multiplicity(0, 1))
    }
)
inputValue1039: BinaryAssociation = BinaryAssociation(
    name="inputValue1039",
    ends={
        Property(name="uml_TracedInputPin1040", type=umlTrace_uml_TracedOpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOpaqueAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999))
    }
)
outputValue1041: BinaryAssociation = BinaryAssociation(
    name="outputValue1041",
    ends={
        Property(name="uml_TracedOutputPin1043", type=umlTrace_uml_TracedOpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOpaqueAction1042", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1044: BinaryAssociation = BinaryAssociation(
    name="originalObject1044",
    ends={
        Property(name="uml_umlTrace_OpaqueAction", type=umlTrace_uml_TracedOpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOpaqueAction1045", type=uml_umlTrace_OpaqueAction, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute1046: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute1046",
    ends={
        Property(name="uml_TracedProperty1047", type=umlTrace_uml_TracedDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDataType", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
ownedOperation1048: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1048",
    ends={
        Property(name="uml_TracedOperation1050", type=umlTrace_uml_TracedDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDataType1049", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_DataType1051: BinaryAssociation = BinaryAssociation(
    name="originalObject_DataType1051",
    ends={
        Property(name="uml_umlTrace_DataType", type=umlTrace_uml_TracedDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDataType1052", type=uml_umlTrace_DataType, multiplicity=Multiplicity(0, 1))
    }
)
nameTrace1021: BinaryAssociation = BinaryAssociation(
    name="nameTrace1021",
    ends={
        Property(name="InputParameterValues_name_Value1023", type=umlTrace_Input_TracedInputParameterValues, multiplicity=Multiplicity(1, 1)),
        Property(name="parent1022", type=InputParameterValues_name_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterValuesTrace1024: BinaryAssociation = BinaryAssociation(
    name="parameterValuesTrace1024",
    ends={
        Property(name="InputParameterValues_parameterValues_Value1026", type=umlTrace_Input_TracedInputParameterValues, multiplicity=Multiplicity(1, 1)),
        Property(name="parent1025", type=InputParameterValues_parameterValues_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contract1027: BinaryAssociation = BinaryAssociation(
    name="contract1027",
    ends={
        Property(name="uml_TracedBehavior", type=umlTrace_uml_TracedConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnector", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 9999))
    }
)
end1028: BinaryAssociation = BinaryAssociation(
    name="end1028",
    ends={
        Property(name="uml_TracedConnectorEnd1030", type=umlTrace_uml_TracedConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnector1029", type=uml_TracedConnectorEnd, multiplicity=Multiplicity(2, 9999))
    }
)
redefinedConnector1031: BinaryAssociation = BinaryAssociation(
    name="redefinedConnector1031",
    ends={
        Property(name="uml_TracedConnector1033", type=umlTrace_uml_TracedConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnector1032", type=uml_TracedConnector, multiplicity=Multiplicity(0, 9999))
    }
)
type1034: BinaryAssociation = BinaryAssociation(
    name="type1034",
    ends={
        Property(name="uml_TracedAssociation1036", type=umlTrace_uml_TracedConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnector1035", type=uml_TracedAssociation, multiplicity=Multiplicity(0, 1))
    }
)
class_1069: BinaryAssociation = BinaryAssociation(
    name="class_1069",
    ends={
        Property(name="uml_TracedClass1071", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1070", type=uml_TracedClass, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue1072: BinaryAssociation = BinaryAssociation(
    name="defaultValue1072",
    ends={
        Property(name="uml_TracedValueSpecification1074", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1073", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
opposite1075: BinaryAssociation = BinaryAssociation(
    name="opposite1075",
    ends={
        Property(name="uml_TracedProperty1077", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1076", type=uml_TracedProperty, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation1078: BinaryAssociation = BinaryAssociation(
    name="owningAssociation1078",
    ends={
        Property(name="uml_TracedAssociation1080", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1079", type=uml_TracedAssociation, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty1081: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty1081",
    ends={
        Property(name="uml_TracedProperty1083", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1082", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
subsettedProperty1084: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty1084",
    ends={
        Property(name="uml_TracedProperty1086", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1085", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
association1087: BinaryAssociation = BinaryAssociation(
    name="association1087",
    ends={
        Property(name="uml_TracedAssociation1089", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1088", type=uml_TracedAssociation, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_Property1090: BinaryAssociation = BinaryAssociation(
    name="originalObject_Property1090",
    ends={
        Property(name="uml_umlTrace_Property", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1091", type=uml_umlTrace_Property, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1092: BinaryAssociation = BinaryAssociation(
    name="originalObject1092",
    ends={
        Property(name="uml_umlTrace_Continuation", type=umlTrace_uml_TracedContinuation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedContinuation", type=uml_umlTrace_Continuation, multiplicity=Multiplicity(0, 1))
    }
)
endData1053: BinaryAssociation = BinaryAssociation(
    name="endData1053",
    ends={
        Property(name="uml_TracedLinkEndData1054", type=umlTrace_uml_TracedLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkAction", type=uml_TracedLinkEndData, multiplicity=Multiplicity(2, 9999))
    }
)
inputValue1055: BinaryAssociation = BinaryAssociation(
    name="inputValue1055",
    ends={
        Property(name="uml_TracedInputPin1057", type=umlTrace_uml_TracedLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkAction1056", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 9999))
    }
)
datatype1058: BinaryAssociation = BinaryAssociation(
    name="datatype1058",
    ends={
        Property(name="uml_TracedDataType1059", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty", type=uml_TracedDataType, multiplicity=Multiplicity(0, 1))
    }
)
interface1060: BinaryAssociation = BinaryAssociation(
    name="interface1060",
    ends={
        Property(name="uml_TracedInterface1062", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1061", type=uml_TracedInterface, multiplicity=Multiplicity(0, 1))
    }
)
associationEnd1063: BinaryAssociation = BinaryAssociation(
    name="associationEnd1063",
    ends={
        Property(name="uml_TracedProperty1065", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1064", type=uml_TracedProperty, multiplicity=Multiplicity(0, 1))
    }
)
qualifier1066: BinaryAssociation = BinaryAssociation(
    name="qualifier1066",
    ends={
        Property(name="uml_TracedProperty1068", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1067", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
nestedArtifact1106: BinaryAssociation = BinaryAssociation(
    name="nestedArtifact1106",
    ends={
        Property(name="uml_TracedArtifact1108", type=umlTrace_uml_TracedArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedArtifact1107", type=uml_TracedArtifact, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute1109: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute1109",
    ends={
        Property(name="uml_TracedProperty1111", type=umlTrace_uml_TracedArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedArtifact1110", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
ownedOperation1112: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1112",
    ends={
        Property(name="uml_TracedOperation1114", type=umlTrace_uml_TracedArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedArtifact1113", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_Artifact1115: BinaryAssociation = BinaryAssociation(
    name="originalObject_Artifact1115",
    ends={
        Property(name="uml_umlTrace_Artifact", type=umlTrace_uml_TracedArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedArtifact1116", type=uml_umlTrace_Artifact, multiplicity=Multiplicity(0, 1))
    }
)
contract1117: BinaryAssociation = BinaryAssociation(
    name="contract1117",
    ends={
        Property(name="uml_TracedInterface1118", type=umlTrace_uml_TracedInterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterfaceRealization", type=uml_TracedInterface, multiplicity=Multiplicity(1, 1))
    }
)
implementingClassifier1119: BinaryAssociation = BinaryAssociation(
    name="implementingClassifier1119",
    ends={
        Property(name="uml_TracedBehavioredClassifier", type=umlTrace_uml_TracedInterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterfaceRealization1120", type=uml_TracedBehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
inState1121: BinaryAssociation = BinaryAssociation(
    name="inState1121",
    ends={
        Property(name="uml_TracedState1122", type=umlTrace_uml_TracedObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedObjectNode", type=uml_TracedState, multiplicity=Multiplicity(0, 9999))
    }
)
selection1123: BinaryAssociation = BinaryAssociation(
    name="selection1123",
    ends={
        Property(name="uml_TracedBehavior1125", type=umlTrace_uml_TracedObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedObjectNode1124", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
upperBound1126: BinaryAssociation = BinaryAssociation(
    name="upperBound1126",
    ends={
        Property(name="uml_TracedValueSpecification1128", type=umlTrace_uml_TracedObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedObjectNode1127", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
removeAt1093: BinaryAssociation = BinaryAssociation(
    name="removeAt1093",
    ends={
        Property(name="uml_TracedInputPin1094", type=umlTrace_uml_TracedRemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRemoveStructuralFeatureValueAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1095: BinaryAssociation = BinaryAssociation(
    name="originalObject1095",
    ends={
        Property(name="uml_umlTrace_RemoveStructuralFeatureValueAction", type=umlTrace_uml_TracedRemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRemoveStructuralFeatureValueAction1096", type=uml_umlTrace_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(0, 1))
    }
)
signal1097: BinaryAssociation = BinaryAssociation(
    name="signal1097",
    ends={
        Property(name="uml_TracedSignal1098", type=umlTrace_uml_TracedSendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSendSignalAction", type=uml_TracedSignal, multiplicity=Multiplicity(1, 1))
    }
)
target1099: BinaryAssociation = BinaryAssociation(
    name="target1099",
    ends={
        Property(name="uml_TracedInputPin1101", type=umlTrace_uml_TracedSendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSendSignalAction1100", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1102: BinaryAssociation = BinaryAssociation(
    name="originalObject1102",
    ends={
        Property(name="uml_umlTrace_SendSignalAction", type=umlTrace_uml_TracedSendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSendSignalAction1103", type=uml_umlTrace_SendSignalAction, multiplicity=Multiplicity(0, 1))
    }
)
manifestation1104: BinaryAssociation = BinaryAssociation(
    name="manifestation1104",
    ends={
        Property(name="uml_TracedManifestation1105", type=umlTrace_uml_TracedArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedArtifact", type=uml_TracedManifestation, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_AcceptEventAction1138: BinaryAssociation = BinaryAssociation(
    name="originalObject_AcceptEventAction1138",
    ends={
        Property(name="uml_umlTrace_AcceptEventAction", type=umlTrace_uml_TracedAcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAcceptEventAction1139", type=uml_umlTrace_AcceptEventAction, multiplicity=Multiplicity(0, 1))
    }
)
enumeration1140: BinaryAssociation = BinaryAssociation(
    name="enumeration1140",
    ends={
        Property(name="uml_TracedEnumeration1141", type=umlTrace_uml_TracedEnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedEnumerationLiteral", type=uml_TracedEnumeration, multiplicity=Multiplicity(1, 1))
    }
)
insertAt1142: BinaryAssociation = BinaryAssociation(
    name="insertAt1142",
    ends={
        Property(name="uml_TracedInputPin1143", type=umlTrace_uml_TracedAddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAddStructuralFeatureValueAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1144: BinaryAssociation = BinaryAssociation(
    name="originalObject1144",
    ends={
        Property(name="uml_umlTrace_AddStructuralFeatureValueAction", type=umlTrace_uml_TracedAddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAddStructuralFeatureValueAction1145", type=uml_umlTrace_AddStructuralFeatureValueAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1129: BinaryAssociation = BinaryAssociation(
    name="originalObject1129",
    ends={
        Property(name="uml_umlTrace_ActivityFinalNode", type=umlTrace_uml_TracedActivityFinalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityFinalNode", type=uml_umlTrace_ActivityFinalNode, multiplicity=Multiplicity(0, 1))
    }
)
event1130: BinaryAssociation = BinaryAssociation(
    name="event1130",
    ends={
        Property(name="uml_TracedNamedElement", type=umlTrace_uml_TracedDurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDurationObservation", type=uml_TracedNamedElement, multiplicity=Multiplicity(1, 2))
    }
)
originalObject1131: BinaryAssociation = BinaryAssociation(
    name="originalObject1131",
    ends={
        Property(name="uml_umlTrace_DurationObservation", type=umlTrace_uml_TracedDurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDurationObservation1132", type=uml_umlTrace_DurationObservation, multiplicity=Multiplicity(0, 1))
    }
)
result1133: BinaryAssociation = BinaryAssociation(
    name="result1133",
    ends={
        Property(name="uml_TracedOutputPin1134", type=umlTrace_uml_TracedAcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAcceptEventAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
trigger1135: BinaryAssociation = BinaryAssociation(
    name="trigger1135",
    ends={
        Property(name="uml_TracedTrigger1137", type=umlTrace_uml_TracedAcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAcceptEventAction1136", type=uml_TracedTrigger, multiplicity=Multiplicity(1, 9999))
    }
)
originalObject1156: BinaryAssociation = BinaryAssociation(
    name="originalObject1156",
    ends={
        Property(name="uml_umlTrace_FlowFinalNode", type=umlTrace_uml_TracedFlowFinalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedFlowFinalNode", type=uml_umlTrace_FlowFinalNode, multiplicity=Multiplicity(0, 1))
    }
)
covered1157: BinaryAssociation = BinaryAssociation(
    name="covered1157",
    ends={
        Property(name="uml_TracedLifeline1158", type=umlTrace_uml_TracedInteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionFragment", type=uml_TracedLifeline, multiplicity=Multiplicity(0, 9999))
    }
)
enclosingOperand1159: BinaryAssociation = BinaryAssociation(
    name="enclosingOperand1159",
    ends={
        Property(name="uml_TracedInteractionOperand1161", type=umlTrace_uml_TracedInteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionFragment1160", type=uml_TracedInteractionOperand, multiplicity=Multiplicity(0, 1))
    }
)
enclosingInteraction1162: BinaryAssociation = BinaryAssociation(
    name="enclosingInteraction1162",
    ends={
        Property(name="uml_TracedInteraction1164", type=umlTrace_uml_TracedInteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionFragment1163", type=uml_TracedInteraction, multiplicity=Multiplicity(0, 1))
    }
)
generalOrdering1165: BinaryAssociation = BinaryAssociation(
    name="generalOrdering1165",
    ends={
        Property(name="uml_TracedGeneralOrdering1167", type=umlTrace_uml_TracedInteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionFragment1166", type=uml_TracedGeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
result1146: BinaryAssociation = BinaryAssociation(
    name="result1146",
    ends={
        Property(name="uml_TracedOutputPin1147", type=umlTrace_uml_TracedReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1148: BinaryAssociation = BinaryAssociation(
    name="originalObject1148",
    ends={
        Property(name="uml_umlTrace_ReadLinkAction", type=umlTrace_uml_TracedReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkAction1149", type=uml_umlTrace_ReadLinkAction, multiplicity=Multiplicity(0, 1))
    }
)
operand1150: BinaryAssociation = BinaryAssociation(
    name="operand1150",
    ends={
        Property(name="uml_TracedValueSpecification1151", type=umlTrace_uml_TracedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpression", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_Expression1152: BinaryAssociation = BinaryAssociation(
    name="originalObject_Expression1152",
    ends={
        Property(name="uml_umlTrace_Expression", type=umlTrace_uml_TracedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpression1153", type=uml_umlTrace_Expression, multiplicity=Multiplicity(0, 1))
    }
)
message1154: BinaryAssociation = BinaryAssociation(
    name="message1154",
    ends={
        Property(name="uml_TracedNamedElement1155", type=umlTrace_uml_TracedConsiderIgnoreFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConsiderIgnoreFragment", type=uml_TracedNamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
powertypeExtent1180: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent1180",
    ends={
        Property(name="uml_TracedGeneralizationSet1182", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1181", type=uml_TracedGeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember1183: BinaryAssociation = BinaryAssociation(
    name="inheritedMember1183",
    ends={
        Property(name="uml_TracedNamedElement1185", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1184", type=uml_TracedNamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedUseCase1186: BinaryAssociation = BinaryAssociation(
    name="ownedUseCase1186",
    ends={
        Property(name="uml_TracedUseCase1188", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1187", type=uml_TracedUseCase, multiplicity=Multiplicity(0, 9999))
    }
)
useCase1189: BinaryAssociation = BinaryAssociation(
    name="useCase1189",
    ends={
        Property(name="uml_TracedUseCase1191", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1190", type=uml_TracedUseCase, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier1192: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier1192",
    ends={
        Property(name="uml_TracedClassifier1194", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1193", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
representation1195: BinaryAssociation = BinaryAssociation(
    name="representation1195",
    ends={
        Property(name="uml_TracedCollaborationUse1197", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1196", type=uml_TracedCollaborationUse, multiplicity=Multiplicity(0, 1))
    }
)
substitution1198: BinaryAssociation = BinaryAssociation(
    name="substitution1198",
    ends={
        Property(name="uml_TracedSubstitution1200", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1199", type=uml_TracedSubstitution, multiplicity=Multiplicity(0, 9999))
    }
)
feature1168: BinaryAssociation = BinaryAssociation(
    name="feature1168",
    ends={
        Property(name="uml_TracedFeature", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier", type=uml_TracedFeature, multiplicity=Multiplicity(0, 9999))
    }
)
attribute1169: BinaryAssociation = BinaryAssociation(
    name="attribute1169",
    ends={
        Property(name="uml_TracedProperty1171", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1170", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
collaborationUse1172: BinaryAssociation = BinaryAssociation(
    name="collaborationUse1172",
    ends={
        Property(name="uml_TracedCollaborationUse1174", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1173", type=uml_TracedCollaborationUse, multiplicity=Multiplicity(0, 9999))
    }
)
general1175: BinaryAssociation = BinaryAssociation(
    name="general1175",
    ends={
        Property(name="uml_TracedClassifier", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1176", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization1177: BinaryAssociation = BinaryAssociation(
    name="generalization1177",
    ends={
        Property(name="uml_TracedGeneralization1179", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1178", type=uml_TracedGeneralization, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1206: BinaryAssociation = BinaryAssociation(
    name="originalObject1206",
    ends={
        Property(name="uml_umlTrace_Collaboration", type=umlTrace_uml_TracedCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCollaboration1207", type=uml_umlTrace_Collaboration, multiplicity=Multiplicity(0, 1))
    }
)
message1208: BinaryAssociation = BinaryAssociation(
    name="message1208",
    ends={
        Property(name="uml_TracedMessage1209", type=umlTrace_uml_TracedMessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessageEnd", type=uml_TracedMessage, multiplicity=Multiplicity(0, 1))
    }
)
parameter1210: BinaryAssociation = BinaryAssociation(
    name="parameter1210",
    ends={
        Property(name="uml_TracedTemplateParameter1211", type=umlTrace_uml_TracedTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateSignature", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 9999))
    }
)
template1212: BinaryAssociation = BinaryAssociation(
    name="template1212",
    ends={
        Property(name="uml_TracedTemplateableElement", type=umlTrace_uml_TracedTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateSignature1213", type=uml_TracedTemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter1214: BinaryAssociation = BinaryAssociation(
    name="ownedParameter1214",
    ends={
        Property(name="uml_TracedTemplateParameter1216", type=umlTrace_uml_TracedTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateSignature1215", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(0, 9999))
    }
)
represented1201: BinaryAssociation = BinaryAssociation(
    name="represented1201",
    ends={
        Property(name="uml_TracedClassifier1202", type=umlTrace_uml_TracedInformationItem, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationItem", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1203: BinaryAssociation = BinaryAssociation(
    name="originalObject1203",
    ends={
        Property(name="uml_umlTrace_InformationItem", type=umlTrace_uml_TracedInformationItem, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationItem1204", type=uml_umlTrace_InformationItem, multiplicity=Multiplicity(0, 1))
    }
)
deployedArtifact1225: BinaryAssociation = BinaryAssociation(
    name="deployedArtifact1225",
    ends={
        Property(name="uml_TracedDeployedArtifact", type=umlTrace_uml_TracedDeployment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDeployment1226", type=uml_TracedDeployedArtifact, multiplicity=Multiplicity(0, 9999))
    }
)
collaborationRole1205: BinaryAssociation = BinaryAssociation(
    name="collaborationRole1205",
    ends={
        Property(name="uml_TracedConnectableElement", type=umlTrace_uml_TracedCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCollaboration", type=uml_TracedConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
location1227: BinaryAssociation = BinaryAssociation(
    name="location1227",
    ends={
        Property(name="uml_TracedDeploymentTarget", type=umlTrace_uml_TracedDeployment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDeployment1228", type=uml_TracedDeploymentTarget, multiplicity=Multiplicity(1, 1))
    }
)
protocol1229: BinaryAssociation = BinaryAssociation(
    name="protocol1229",
    ends={
        Property(name="uml_TracedProtocolStateMachine1230", type=umlTrace_uml_TracedPort, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPort", type=uml_TracedProtocolStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
provided1231: BinaryAssociation = BinaryAssociation(
    name="provided1231",
    ends={
        Property(name="uml_TracedInterface1233", type=umlTrace_uml_TracedPort, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPort1232", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedPort1234: BinaryAssociation = BinaryAssociation(
    name="redefinedPort1234",
    ends={
        Property(name="uml_TracedPort1236", type=umlTrace_uml_TracedPort, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPort1235", type=uml_TracedPort, multiplicity=Multiplicity(0, 9999))
    }
)
required1237: BinaryAssociation = BinaryAssociation(
    name="required1237",
    ends={
        Property(name="uml_TracedInterface1239", type=umlTrace_uml_TracedPort, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPort1238", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_TemplateSignature1217: BinaryAssociation = BinaryAssociation(
    name="originalObject_TemplateSignature1217",
    ends={
        Property(name="uml_umlTrace_TemplateSignature", type=umlTrace_uml_TracedTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateSignature1218", type=uml_umlTrace_TemplateSignature, multiplicity=Multiplicity(0, 1))
    }
)
signal1219: BinaryAssociation = BinaryAssociation(
    name="signal1219",
    ends={
        Property(name="uml_TracedSignal1220", type=umlTrace_uml_TracedBroadcastSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBroadcastSignalAction", type=uml_TracedSignal, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1221: BinaryAssociation = BinaryAssociation(
    name="originalObject1221",
    ends={
        Property(name="uml_umlTrace_BroadcastSignalAction", type=umlTrace_uml_TracedBroadcastSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBroadcastSignalAction1222", type=uml_umlTrace_BroadcastSignalAction, multiplicity=Multiplicity(0, 1))
    }
)
configuration1223: BinaryAssociation = BinaryAssociation(
    name="configuration1223",
    ends={
        Property(name="uml_TracedDeploymentSpecification1224", type=umlTrace_uml_TracedDeployment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDeployment", type=uml_TracedDeploymentSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
metaclass1254: BinaryAssociation = BinaryAssociation(
    name="metaclass1254",
    ends={
        Property(name="uml_TracedClass1255", type=umlTrace_uml_TracedExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtension", type=uml_TracedClass, multiplicity=Multiplicity(1, 1))
    }
)
source1256: BinaryAssociation = BinaryAssociation(
    name="source1256",
    ends={
        Property(name="uml_TracedElement1257", type=umlTrace_uml_TracedDirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDirectedRelationship", type=uml_TracedElement, multiplicity=Multiplicity(1, 9999))
    }
)
target1258: BinaryAssociation = BinaryAssociation(
    name="target1258",
    ends={
        Property(name="uml_TracedElement1260", type=umlTrace_uml_TracedDirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDirectedRelationship1259", type=uml_TracedElement, multiplicity=Multiplicity(1, 9999))
    }
)
when1261: BinaryAssociation = BinaryAssociation(
    name="when1261",
    ends={
        Property(name="uml_TracedTimeExpression1262", type=umlTrace_uml_TracedTimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeEvent", type=uml_TracedTimeExpression, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1263: BinaryAssociation = BinaryAssociation(
    name="originalObject1263",
    ends={
        Property(name="uml_umlTrace_TimeEvent", type=umlTrace_uml_TracedTimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeEvent1264", type=uml_umlTrace_TimeEvent, multiplicity=Multiplicity(0, 1))
    }
)
context1240: BinaryAssociation = BinaryAssociation(
    name="context1240",
    ends={
        Property(name="uml_TracedClassifier1241", type=umlTrace_uml_TracedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAction", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 1))
    }
)
input1242: BinaryAssociation = BinaryAssociation(
    name="input1242",
    ends={
        Property(name="uml_TracedInputPin1244", type=umlTrace_uml_TracedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAction1243", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999))
    }
)
localPostcondition1245: BinaryAssociation = BinaryAssociation(
    name="localPostcondition1245",
    ends={
        Property(name="uml_TracedConstraint1247", type=umlTrace_uml_TracedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAction1246", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
localPrecondition1248: BinaryAssociation = BinaryAssociation(
    name="localPrecondition1248",
    ends={
        Property(name="uml_TracedConstraint1250", type=umlTrace_uml_TracedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAction1249", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
output1251: BinaryAssociation = BinaryAssociation(
    name="output1251",
    ends={
        Property(name="uml_TracedOutputPin1253", type=umlTrace_uml_TracedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAction1252", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage1277: BinaryAssociation = BinaryAssociation(
    name="nestingPackage1277",
    ends={
        Property(name="uml_TracedPackage1279", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1278", type=uml_TracedPackage, multiplicity=Multiplicity(0, 1))
    }
)
ownedStereotype1280: BinaryAssociation = BinaryAssociation(
    name="ownedStereotype1280",
    ends={
        Property(name="uml_TracedStereotype1282", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1281", type=uml_TracedStereotype, multiplicity=Multiplicity(0, 9999))
    }
)
ownedType1283: BinaryAssociation = BinaryAssociation(
    name="ownedType1283",
    ends={
        Property(name="uml_TracedType", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1284", type=uml_TracedType, multiplicity=Multiplicity(0, 9999))
    }
)
packageMerge1285: BinaryAssociation = BinaryAssociation(
    name="packageMerge1285",
    ends={
        Property(name="uml_TracedPackageMerge1287", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1286", type=uml_TracedPackageMerge, multiplicity=Multiplicity(0, 9999))
    }
)
packagedElement1288: BinaryAssociation = BinaryAssociation(
    name="packagedElement1288",
    ends={
        Property(name="uml_TracedPackageableElement", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1289", type=uml_TracedPackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
profileApplication1290: BinaryAssociation = BinaryAssociation(
    name="profileApplication1290",
    ends={
        Property(name="uml_TracedProfileApplication1292", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1291", type=uml_TracedProfileApplication, multiplicity=Multiplicity(0, 9999))
    }
)
package1265: BinaryAssociation = BinaryAssociation(
    name="package1265",
    ends={
        Property(name="uml_TracedPackage1266", type=umlTrace_uml_TracedType, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedType", type=uml_TracedPackage, multiplicity=Multiplicity(0, 1))
    }
)
postCondition1267: BinaryAssociation = BinaryAssociation(
    name="postCondition1267",
    ends={
        Property(name="uml_TracedConstraint1268", type=umlTrace_uml_TracedProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolTransition", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 1))
    }
)
preCondition1269: BinaryAssociation = BinaryAssociation(
    name="preCondition1269",
    ends={
        Property(name="uml_TracedConstraint1271", type=umlTrace_uml_TracedProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolTransition1270", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 1))
    }
)
referred1272: BinaryAssociation = BinaryAssociation(
    name="referred1272",
    ends={
        Property(name="uml_TracedOperation1274", type=umlTrace_uml_TracedProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolTransition1273", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage1275: BinaryAssociation = BinaryAssociation(
    name="nestedPackage1275",
    ends={
        Property(name="uml_TracedPackage1276", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage", type=uml_TracedPackage, multiplicity=Multiplicity(0, 9999))
    }
)
structuralFeature1305: BinaryAssociation = BinaryAssociation(
    name="structuralFeature1305",
    ends={
        Property(name="uml_TracedStructuralFeature1307", type=umlTrace_uml_TracedStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuralFeatureAction1306", type=uml_TracedStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
constrainedElement1308: BinaryAssociation = BinaryAssociation(
    name="constrainedElement1308",
    ends={
        Property(name="uml_TracedElement1309", type=umlTrace_uml_TracedConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConstraint", type=uml_TracedElement, multiplicity=Multiplicity(0, 9999))
    }
)
context1310: BinaryAssociation = BinaryAssociation(
    name="context1310",
    ends={
        Property(name="uml_TracedNamespace", type=umlTrace_uml_TracedConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConstraint1311", type=uml_TracedNamespace, multiplicity=Multiplicity(0, 1))
    }
)
specification1312: BinaryAssociation = BinaryAssociation(
    name="specification1312",
    ends={
        Property(name="uml_TracedValueSpecification1314", type=umlTrace_uml_TracedConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConstraint1313", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject_Constraint1315: BinaryAssociation = BinaryAssociation(
    name="originalObject_Constraint1315",
    ends={
        Property(name="uml_umlTrace_Constraint", type=umlTrace_uml_TracedConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConstraint1316", type=uml_umlTrace_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
lowerValue1317: BinaryAssociation = BinaryAssociation(
    name="lowerValue1317",
    ends={
        Property(name="uml_TracedValueSpecification1318", type=umlTrace_uml_TracedMultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMultiplicityElement", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
upperValue1319: BinaryAssociation = BinaryAssociation(
    name="upperValue1319",
    ends={
        Property(name="uml_TracedValueSpecification1321", type=umlTrace_uml_TracedMultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMultiplicityElement1320", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_Package1293: BinaryAssociation = BinaryAssociation(
    name="originalObject_Package1293",
    ends={
        Property(name="uml_umlTrace_Package", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1294", type=uml_umlTrace_Package, multiplicity=Multiplicity(0, 1))
    }
)
classifierBehavior1295: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior1295",
    ends={
        Property(name="uml_TracedBehavior1296", type=umlTrace_uml_TracedBehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioredClassifier", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
interfaceRealization1297: BinaryAssociation = BinaryAssociation(
    name="interfaceRealization1297",
    ends={
        Property(name="uml_TracedInterfaceRealization1299", type=umlTrace_uml_TracedBehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioredClassifier1298", type=uml_TracedInterfaceRealization, multiplicity=Multiplicity(0, 9999))
    }
)
ownedBehavior1300: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior1300",
    ends={
        Property(name="uml_TracedBehavior1302", type=umlTrace_uml_TracedBehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioredClassifier1301", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 9999))
    }
)
object1303: BinaryAssociation = BinaryAssociation(
    name="object1303",
    ends={
        Property(name="uml_TracedInputPin1304", type=umlTrace_uml_TracedStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuralFeatureAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1337: BinaryAssociation = BinaryAssociation(
    name="originalObject1337",
    ends={
        Property(name="uml_umlTrace_ReduceAction", type=umlTrace_uml_TracedReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReduceAction1338", type=uml_umlTrace_ReduceAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_InputPin1339: BinaryAssociation = BinaryAssociation(
    name="originalObject_InputPin1339",
    ends={
        Property(name="uml_umlTrace_InputPin", type=umlTrace_uml_TracedInputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInputPin", type=uml_umlTrace_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
executableNode1340: BinaryAssociation = BinaryAssociation(
    name="executableNode1340",
    ends={
        Property(name="uml_TracedExecutableNode", type=umlTrace_uml_TracedSequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSequenceNode", type=uml_TracedExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
featuringClassifier1341: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier1341",
    ends={
        Property(name="uml_TracedClassifier1342", type=umlTrace_uml_TracedFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedFeature", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
maxint1343: BinaryAssociation = BinaryAssociation(
    name="maxint1343",
    ends={
        Property(name="uml_TracedValueSpecification1344", type=umlTrace_uml_TracedInteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionConstraint", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
powertype1322: BinaryAssociation = BinaryAssociation(
    name="powertype1322",
    ends={
        Property(name="uml_TracedClassifier1323", type=umlTrace_uml_TracedGeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralizationSet", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization1324: BinaryAssociation = BinaryAssociation(
    name="generalization1324",
    ends={
        Property(name="uml_TracedGeneralization1326", type=umlTrace_uml_TracedGeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralizationSet1325", type=uml_TracedGeneralization, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1327: BinaryAssociation = BinaryAssociation(
    name="originalObject1327",
    ends={
        Property(name="uml_umlTrace_GeneralizationSet", type=umlTrace_uml_TracedGeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralizationSet1328", type=uml_umlTrace_GeneralizationSet, multiplicity=Multiplicity(0, 1))
    }
)
collection1329: BinaryAssociation = BinaryAssociation(
    name="collection1329",
    ends={
        Property(name="uml_TracedInputPin1330", type=umlTrace_uml_TracedReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReduceAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
reducer1331: BinaryAssociation = BinaryAssociation(
    name="reducer1331",
    ends={
        Property(name="uml_TracedBehavior1333", type=umlTrace_uml_TracedReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReduceAction1332", type=uml_TracedBehavior, multiplicity=Multiplicity(1, 1))
    }
)
result1334: BinaryAssociation = BinaryAssociation(
    name="result1334",
    ends={
        Property(name="uml_TracedOutputPin1336", type=umlTrace_uml_TracedReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReduceAction1335", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
owner1358: BinaryAssociation = BinaryAssociation(
    name="owner1358",
    ends={
        Property(name="uml_TracedElement1360", type=umlTrace_uml_TracedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedElement1359", type=uml_TracedElement, multiplicity=Multiplicity(0, 1))
    }
)
semanticVisitorTrace1361: BinaryAssociation = BinaryAssociation(
    name="semanticVisitorTrace1361",
    ends={
        Property(name="Element_semanticVisitor_Value1363", type=umlTrace_uml_TracedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent1362", type=Element_semanticVisitor_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizingClassifier1364: BinaryAssociation = BinaryAssociation(
    name="realizingClassifier1364",
    ends={
        Property(name="uml_TracedClassifier1365", type=umlTrace_uml_TracedComponentRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComponentRealization", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 9999))
    }
)
abstraction1366: BinaryAssociation = BinaryAssociation(
    name="abstraction1366",
    ends={
        Property(name="uml_TracedComponent1368", type=umlTrace_uml_TracedComponentRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComponentRealization1367", type=uml_TracedComponent, multiplicity=Multiplicity(0, 1))
    }
)
definingFeature1369: BinaryAssociation = BinaryAssociation(
    name="definingFeature1369",
    ends={
        Property(name="uml_TracedStructuralFeature1370", type=umlTrace_uml_TracedSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSlot", type=uml_TracedStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value1371: BinaryAssociation = BinaryAssociation(
    name="value1371",
    ends={
        Property(name="uml_TracedValueSpecification1373", type=umlTrace_uml_TracedSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSlot1372", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
minint1345: BinaryAssociation = BinaryAssociation(
    name="minint1345",
    ends={
        Property(name="uml_TracedValueSpecification1347", type=umlTrace_uml_TracedInteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionConstraint1346", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
result1348: BinaryAssociation = BinaryAssociation(
    name="result1348",
    ends={
        Property(name="uml_TracedOutputPin1349", type=umlTrace_uml_TracedWriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedWriteStructuralFeatureAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 1))
    }
)
value1350: BinaryAssociation = BinaryAssociation(
    name="value1350",
    ends={
        Property(name="uml_TracedInputPin1352", type=umlTrace_uml_TracedWriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedWriteStructuralFeatureAction1351", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment1353: BinaryAssociation = BinaryAssociation(
    name="ownedComment1353",
    ends={
        Property(name="uml_TracedComment1354", type=umlTrace_uml_TracedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedElement", type=uml_TracedComment, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElement1355: BinaryAssociation = BinaryAssociation(
    name="ownedElement1355",
    ends={
        Property(name="uml_TracedElement1357", type=umlTrace_uml_TracedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedElement1356", type=uml_TracedElement, multiplicity=Multiplicity(0, 9999))
    }
)
joinSpec1387: BinaryAssociation = BinaryAssociation(
    name="joinSpec1387",
    ends={
        Property(name="uml_TracedValueSpecification1388", type=umlTrace_uml_TracedJoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedJoinNode", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1389: BinaryAssociation = BinaryAssociation(
    name="originalObject1389",
    ends={
        Property(name="uml_umlTrace_JoinNode", type=umlTrace_uml_TracedJoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedJoinNode1390", type=uml_umlTrace_JoinNode, multiplicity=Multiplicity(0, 1))
    }
)
object1391: BinaryAssociation = BinaryAssociation(
    name="object1391",
    ends={
        Property(name="uml_TracedInputPin1392", type=umlTrace_uml_TracedStartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStartObjectBehaviorAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1393: BinaryAssociation = BinaryAssociation(
    name="originalObject1393",
    ends={
        Property(name="uml_umlTrace_StartObjectBehaviorAction", type=umlTrace_uml_TracedStartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStartObjectBehaviorAction1394", type=uml_umlTrace_StartObjectBehaviorAction, multiplicity=Multiplicity(0, 1))
    }
)
importedElement1395: BinaryAssociation = BinaryAssociation(
    name="importedElement1395",
    ends={
        Property(name="uml_TracedPackageableElement1396", type=umlTrace_uml_TracedElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedElementImport", type=uml_TracedPackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace1397: BinaryAssociation = BinaryAssociation(
    name="importingNamespace1397",
    ends={
        Property(name="uml_TracedNamespace1399", type=umlTrace_uml_TracedElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedElementImport1398", type=uml_TracedNamespace, multiplicity=Multiplicity(1, 1))
    }
)
owningInstance1374: BinaryAssociation = BinaryAssociation(
    name="owningInstance1374",
    ends={
        Property(name="uml_TracedInstanceSpecification1376", type=umlTrace_uml_TracedSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSlot1375", type=uml_TracedInstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1377: BinaryAssociation = BinaryAssociation(
    name="originalObject1377",
    ends={
        Property(name="uml_umlTrace_Slot", type=umlTrace_uml_TracedSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSlot1378", type=uml_umlTrace_Slot, multiplicity=Multiplicity(0, 1))
    }
)
signal1379: BinaryAssociation = BinaryAssociation(
    name="signal1379",
    ends={
        Property(name="uml_TracedSignal1380", type=umlTrace_uml_TracedSignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSignalEvent", type=uml_TracedSignal, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1381: BinaryAssociation = BinaryAssociation(
    name="originalObject1381",
    ends={
        Property(name="uml_umlTrace_SignalEvent", type=umlTrace_uml_TracedSignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSignalEvent1382", type=uml_umlTrace_SignalEvent, multiplicity=Multiplicity(0, 1))
    }
)
useCase1383: BinaryAssociation = BinaryAssociation(
    name="useCase1383",
    ends={
        Property(name="uml_TracedUseCase1384", type=umlTrace_uml_TracedExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtensionPoint", type=uml_TracedUseCase, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1385: BinaryAssociation = BinaryAssociation(
    name="originalObject1385",
    ends={
        Property(name="uml_umlTrace_ExtensionPoint", type=umlTrace_uml_TracedExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtensionPoint1386", type=uml_umlTrace_ExtensionPoint, multiplicity=Multiplicity(0, 1))
    }
)
toBefore1411: BinaryAssociation = BinaryAssociation(
    name="toBefore1411",
    ends={
        Property(name="uml_TracedGeneralOrdering1413", type=umlTrace_uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOccurrenceSpecification1412", type=uml_TracedGeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_OccurrenceSpecification1414: BinaryAssociation = BinaryAssociation(
    name="originalObject_OccurrenceSpecification1414",
    ends={
        Property(name="uml_umlTrace_OccurrenceSpecification", type=umlTrace_uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOccurrenceSpecification1415", type=uml_umlTrace_OccurrenceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
owningExpression1416: BinaryAssociation = BinaryAssociation(
    name="owningExpression1416",
    ends={
        Property(name="uml_TracedStringExpression1417", type=umlTrace_uml_TracedStringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStringExpression", type=uml_TracedStringExpression, multiplicity=Multiplicity(0, 1))
    }
)
subExpression1418: BinaryAssociation = BinaryAssociation(
    name="subExpression1418",
    ends={
        Property(name="uml_TracedStringExpression1420", type=umlTrace_uml_TracedStringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStringExpression1419", type=uml_TracedStringExpression, multiplicity=Multiplicity(0, 9999))
    }
)
icon1421: BinaryAssociation = BinaryAssociation(
    name="icon1421",
    ends={
        Property(name="uml_TracedImage1422", type=umlTrace_uml_TracedStereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStereotype", type=uml_TracedImage, multiplicity=Multiplicity(0, 9999))
    }
)
profile1423: BinaryAssociation = BinaryAssociation(
    name="profile1423",
    ends={
        Property(name="uml_TracedProfile1425", type=umlTrace_uml_TracedStereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStereotype1424", type=uml_TracedProfile, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1400: BinaryAssociation = BinaryAssociation(
    name="originalObject1400",
    ends={
        Property(name="uml_umlTrace_ElementImport", type=umlTrace_uml_TracedElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedElementImport1401", type=uml_umlTrace_ElementImport, multiplicity=Multiplicity(0, 1))
    }
)
classifier1402: BinaryAssociation = BinaryAssociation(
    name="classifier1402",
    ends={
        Property(name="uml_TracedClassifier1403", type=umlTrace_uml_TracedCreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCreateObjectAction", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
result1404: BinaryAssociation = BinaryAssociation(
    name="result1404",
    ends={
        Property(name="uml_TracedOutputPin1406", type=umlTrace_uml_TracedCreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCreateObjectAction1405", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1407: BinaryAssociation = BinaryAssociation(
    name="originalObject1407",
    ends={
        Property(name="uml_umlTrace_CreateObjectAction", type=umlTrace_uml_TracedCreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCreateObjectAction1408", type=uml_umlTrace_CreateObjectAction, multiplicity=Multiplicity(0, 1))
    }
)
toAfter1409: BinaryAssociation = BinaryAssociation(
    name="toAfter1409",
    ends={
        Property(name="uml_TracedGeneralOrdering1410", type=umlTrace_uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOccurrenceSpecification", type=uml_TracedGeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1443: BinaryAssociation = BinaryAssociation(
    name="originalObject1443",
    ends={
        Property(name="umlTrace_uml_TracedInterface1444", type=uml_umlTrace_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="uml_umlTrace_Interface", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1))
    }
)
clause1445: BinaryAssociation = BinaryAssociation(
    name="clause1445",
    ends={
        Property(name="uml_TracedClause1446", type=umlTrace_uml_TracedConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConditionalNode", type=uml_TracedClause, multiplicity=Multiplicity(1, 9999))
    }
)
result1447: BinaryAssociation = BinaryAssociation(
    name="result1447",
    ends={
        Property(name="uml_TracedOutputPin1449", type=umlTrace_uml_TracedConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConditionalNode1448", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier1426: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier1426",
    ends={
        Property(name="uml_TracedClassifier1427", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute1428: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute1428",
    ends={
        Property(name="uml_TracedProperty1430", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface1429", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
packagedElement1469: BinaryAssociation = BinaryAssociation(
    name="packagedElement1469",
    ends={
        Property(name="uml_TracedPackageableElement1470", type=umlTrace_uml_TracedComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComponent", type=uml_TracedPackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception1431: BinaryAssociation = BinaryAssociation(
    name="ownedReception1431",
    ends={
        Property(name="uml_TracedReception1433", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface1432", type=uml_TracedReception, multiplicity=Multiplicity(0, 9999))
    }
)
provided1471: BinaryAssociation = BinaryAssociation(
    name="provided1471",
    ends={
        Property(name="uml_TracedInterface1473", type=umlTrace_uml_TracedComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComponent1472", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999))
    }
)
protocol1434: BinaryAssociation = BinaryAssociation(
    name="protocol1434",
    ends={
        Property(name="uml_TracedProtocolStateMachine1436", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface1435", type=uml_TracedProtocolStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
realization1474: BinaryAssociation = BinaryAssociation(
    name="realization1474",
    ends={
        Property(name="uml_TracedComponentRealization1476", type=umlTrace_uml_TracedComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComponent1475", type=uml_TracedComponentRealization, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedInterface1437: BinaryAssociation = BinaryAssociation(
    name="redefinedInterface1437",
    ends={
        Property(name="uml_TracedInterface1439", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface1438", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999))
    }
)
required1477: BinaryAssociation = BinaryAssociation(
    name="required1477",
    ends={
        Property(name="uml_TracedInterface1479", type=umlTrace_uml_TracedComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComponent1478", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999))
    }
)
end1450: BinaryAssociation = BinaryAssociation(
    name="end1450",
    ends={
        Property(name="uml_TracedProperty1451", type=umlTrace_uml_TracedReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndAction", type=uml_TracedProperty, multiplicity=Multiplicity(1, 1))
    }
)
ownedOperation1440: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1440",
    ends={
        Property(name="uml_TracedOperation1442", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface1441", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999))
    }
)
object1452: BinaryAssociation = BinaryAssociation(
    name="object1452",
    ends={
        Property(name="uml_TracedInputPin1454", type=umlTrace_uml_TracedReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndAction1453", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
result1455: BinaryAssociation = BinaryAssociation(
    name="result1455",
    ends={
        Property(name="uml_TracedOutputPin1457", type=umlTrace_uml_TracedReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndAction1456", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1458: BinaryAssociation = BinaryAssociation(
    name="originalObject1458",
    ends={
        Property(name="uml_umlTrace_ReadLinkObjectEndAction", type=umlTrace_uml_TracedReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndAction1459", type=uml_umlTrace_ReadLinkObjectEndAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1460: BinaryAssociation = BinaryAssociation(
    name="originalObject1460",
    ends={
        Property(name="uml_umlTrace_AnyReceiveEvent", type=umlTrace_uml_TracedAnyReceiveEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAnyReceiveEvent", type=uml_umlTrace_AnyReceiveEvent, multiplicity=Multiplicity(0, 1))
    }
)
clientDependency1461: BinaryAssociation = BinaryAssociation(
    name="clientDependency1461",
    ends={
        Property(name="uml_TracedDependency1462", type=umlTrace_uml_TracedNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamedElement", type=uml_TracedDependency, multiplicity=Multiplicity(0, 9999))
    }
)
nameExpression1463: BinaryAssociation = BinaryAssociation(
    name="nameExpression1463",
    ends={
        Property(name="uml_TracedStringExpression1465", type=umlTrace_uml_TracedNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamedElement1464", type=uml_TracedStringExpression, multiplicity=Multiplicity(0, 1))
    }
)
namespace1466: BinaryAssociation = BinaryAssociation(
    name="namespace1466",
    ends={
        Property(name="uml_TracedNamespace1468", type=umlTrace_uml_TracedNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamedElement1467", type=uml_TracedNamespace, multiplicity=Multiplicity(0, 1))
    }
)
formalGate1497: BinaryAssociation = BinaryAssociation(
    name="formalGate1497",
    ends={
        Property(name="uml_TracedGate1499", type=umlTrace_uml_TracedInteraction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteraction1498", type=uml_TracedGate, multiplicity=Multiplicity(0, 9999))
    }
)
message1500: BinaryAssociation = BinaryAssociation(
    name="message1500",
    ends={
        Property(name="uml_TracedMessage1502", type=umlTrace_uml_TracedInteraction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteraction1501", type=uml_TracedMessage, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1503: BinaryAssociation = BinaryAssociation(
    name="originalObject1503",
    ends={
        Property(name="uml_umlTrace_LiteralString", type=umlTrace_uml_TracedLiteralString, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLiteralString", type=uml_umlTrace_LiteralString, multiplicity=Multiplicity(0, 1))
    }
)
connectionPoint1480: BinaryAssociation = BinaryAssociation(
    name="connectionPoint1480",
    ends={
        Property(name="uml_TracedPseudostate1481", type=umlTrace_uml_TracedStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStateMachine", type=uml_TracedPseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
submachineState1482: BinaryAssociation = BinaryAssociation(
    name="submachineState1482",
    ends={
        Property(name="uml_TracedState1484", type=umlTrace_uml_TracedStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStateMachine1483", type=uml_TracedState, multiplicity=Multiplicity(0, 9999))
    }
)
region1485: BinaryAssociation = BinaryAssociation(
    name="region1485",
    ends={
        Property(name="uml_TracedRegion1487", type=umlTrace_uml_TracedStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStateMachine1486", type=uml_TracedRegion, multiplicity=Multiplicity(1, 9999))
    }
)
extendedStateMachine1488: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine1488",
    ends={
        Property(name="uml_TracedStateMachine1490", type=umlTrace_uml_TracedStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStateMachine1489", type=uml_TracedStateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
lifeline1491: BinaryAssociation = BinaryAssociation(
    name="lifeline1491",
    ends={
        Property(name="uml_TracedLifeline1492", type=umlTrace_uml_TracedInteraction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteraction", type=uml_TracedLifeline, multiplicity=Multiplicity(0, 9999))
    }
)
fragment1493: BinaryAssociation = BinaryAssociation(
    name="fragment1493",
    ends={
        Property(name="uml_TracedInteractionFragment", type=umlTrace_uml_TracedInteraction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteraction1494", type=uml_TracedInteractionFragment, multiplicity=Multiplicity(0, 9999))
    }
)
action1495: BinaryAssociation = BinaryAssociation(
    name="action1495",
    ends={
        Property(name="uml_TracedAction", type=umlTrace_uml_TracedInteraction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteraction1496", type=uml_TracedAction, multiplicity=Multiplicity(0, 9999))
    }
)
target1516: BinaryAssociation = BinaryAssociation(
    name="target1516",
    ends={
        Property(name="uml_TracedInputPin1518", type=umlTrace_uml_TracedSendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSendObjectAction1517", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1519: BinaryAssociation = BinaryAssociation(
    name="originalObject1519",
    ends={
        Property(name="uml_umlTrace_SendObjectAction", type=umlTrace_uml_TracedSendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSendObjectAction1520", type=uml_umlTrace_SendObjectAction, multiplicity=Multiplicity(0, 1))
    }
)
decomposedAs1521: BinaryAssociation = BinaryAssociation(
    name="decomposedAs1521",
    ends={
        Property(name="uml_TracedPartDecomposition1522", type=umlTrace_uml_TracedLifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLifeline", type=uml_TracedPartDecomposition, multiplicity=Multiplicity(0, 1))
    }
)
interaction1523: BinaryAssociation = BinaryAssociation(
    name="interaction1523",
    ends={
        Property(name="uml_TracedInteraction1525", type=umlTrace_uml_TracedLifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLifeline1524", type=uml_TracedInteraction, multiplicity=Multiplicity(1, 1))
    }
)
object1504: BinaryAssociation = BinaryAssociation(
    name="object1504",
    ends={
        Property(name="uml_TracedInputPin1505", type=umlTrace_uml_TracedStartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStartClassifierBehaviorAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1506: BinaryAssociation = BinaryAssociation(
    name="originalObject1506",
    ends={
        Property(name="uml_umlTrace_StartClassifierBehaviorAction", type=umlTrace_uml_TracedStartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStartClassifierBehaviorAction1507", type=uml_umlTrace_StartClassifierBehaviorAction, multiplicity=Multiplicity(0, 1))
    }
)
operation1508: BinaryAssociation = BinaryAssociation(
    name="operation1508",
    ends={
        Property(name="uml_TracedOperation1509", type=umlTrace_uml_TracedCallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallEvent", type=uml_TracedOperation, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1510: BinaryAssociation = BinaryAssociation(
    name="originalObject1510",
    ends={
        Property(name="uml_umlTrace_CallEvent", type=umlTrace_uml_TracedCallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallEvent1511", type=uml_umlTrace_CallEvent, multiplicity=Multiplicity(0, 1))
    }
)
relatedElement1512: BinaryAssociation = BinaryAssociation(
    name="relatedElement1512",
    ends={
        Property(name="uml_TracedElement1513", type=umlTrace_uml_TracedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRelationship", type=uml_TracedElement, multiplicity=Multiplicity(1, 9999))
    }
)
request1514: BinaryAssociation = BinaryAssociation(
    name="request1514",
    ends={
        Property(name="uml_TracedInputPin1515", type=umlTrace_uml_TracedSendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSendObjectAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
outputElement1548: BinaryAssociation = BinaryAssociation(
    name="outputElement1548",
    ends={
        Property(name="uml_TracedExpansionNode1549", type=umlTrace_uml_TracedExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpansionRegion", type=uml_TracedExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
inputElement1550: BinaryAssociation = BinaryAssociation(
    name="inputElement1550",
    ends={
        Property(name="uml_TracedExpansionNode1552", type=umlTrace_uml_TracedExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpansionRegion1551", type=uml_TracedExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
value1553: BinaryAssociation = BinaryAssociation(
    name="value1553",
    ends={
        Property(name="uml_TracedInputPin1554", type=umlTrace_uml_TracedWriteVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedWriteVariableAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
represents1526: BinaryAssociation = BinaryAssociation(
    name="represents1526",
    ends={
        Property(name="uml_TracedConnectableElement1528", type=umlTrace_uml_TracedLifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLifeline1527", type=uml_TracedConnectableElement, multiplicity=Multiplicity(0, 1))
    }
)
selector1529: BinaryAssociation = BinaryAssociation(
    name="selector1529",
    ends={
        Property(name="uml_TracedValueSpecification1531", type=umlTrace_uml_TracedLifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLifeline1530", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
coveredBy1532: BinaryAssociation = BinaryAssociation(
    name="coveredBy1532",
    ends={
        Property(name="uml_TracedInteractionFragment1534", type=umlTrace_uml_TracedLifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLifeline1533", type=uml_TracedInteractionFragment, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1535: BinaryAssociation = BinaryAssociation(
    name="originalObject1535",
    ends={
        Property(name="uml_umlTrace_Lifeline", type=umlTrace_uml_TracedLifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLifeline1536", type=uml_umlTrace_Lifeline, multiplicity=Multiplicity(0, 1))
    }
)
finish1537: BinaryAssociation = BinaryAssociation(
    name="finish1537",
    ends={
        Property(name="uml_TracedOccurrenceSpecification1538", type=umlTrace_uml_TracedExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExecutionSpecification", type=uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
start1539: BinaryAssociation = BinaryAssociation(
    name="start1539",
    ends={
        Property(name="uml_TracedOccurrenceSpecification1541", type=umlTrace_uml_TracedExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExecutionSpecification1540", type=uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
event1542: BinaryAssociation = BinaryAssociation(
    name="event1542",
    ends={
        Property(name="uml_TracedNamedElement1543", type=umlTrace_uml_TracedTimeObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeObservation", type=uml_TracedNamedElement, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1544: BinaryAssociation = BinaryAssociation(
    name="originalObject1544",
    ends={
        Property(name="uml_umlTrace_TimeObservation", type=umlTrace_uml_TracedTimeObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeObservation1545", type=uml_umlTrace_TimeObservation, multiplicity=Multiplicity(0, 1))
    }
)
result1546: BinaryAssociation = BinaryAssociation(
    name="result1546",
    ends={
        Property(name="uml_TracedOutputPin1547", type=umlTrace_uml_TracedCreateLinkObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCreateLinkObjectAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
generalMachine1578: BinaryAssociation = BinaryAssociation(
    name="generalMachine1578",
    ends={
        Property(name="uml_TracedProtocolStateMachine1579", type=umlTrace_uml_TracedProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolConformance", type=uml_TracedProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
specificMachine1580: BinaryAssociation = BinaryAssociation(
    name="specificMachine1580",
    ends={
        Property(name="uml_TracedProtocolStateMachine1582", type=umlTrace_uml_TracedProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolConformance1581", type=uml_TracedProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
bodyOutput1555: BinaryAssociation = BinaryAssociation(
    name="bodyOutput1555",
    ends={
        Property(name="uml_TracedOutputPin1556", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
bodyPart1557: BinaryAssociation = BinaryAssociation(
    name="bodyPart1557",
    ends={
        Property(name="uml_TracedExecutableNode1559", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1558", type=uml_TracedExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
decider1560: BinaryAssociation = BinaryAssociation(
    name="decider1560",
    ends={
        Property(name="uml_TracedOutputPin1562", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1561", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
loopVariable1563: BinaryAssociation = BinaryAssociation(
    name="loopVariable1563",
    ends={
        Property(name="uml_TracedOutputPin1565", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1564", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput1566: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput1566",
    ends={
        Property(name="uml_TracedInputPin1568", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1567", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999))
    }
)
result1569: BinaryAssociation = BinaryAssociation(
    name="result1569",
    ends={
        Property(name="uml_TracedOutputPin1571", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1570", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
setupPart1572: BinaryAssociation = BinaryAssociation(
    name="setupPart1572",
    ends={
        Property(name="uml_TracedExecutableNode1574", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1573", type=uml_TracedExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
test1575: BinaryAssociation = BinaryAssociation(
    name="test1575",
    ends={
        Property(name="uml_TracedExecutableNode1577", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1576", type=uml_TracedExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
subpartition1599: BinaryAssociation = BinaryAssociation(
    name="subpartition1599",
    ends={
        Property(name="uml_TracedActivityPartition1601", type=umlTrace_uml_TracedActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityPartition1600", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
superPartition1602: BinaryAssociation = BinaryAssociation(
    name="superPartition1602",
    ends={
        Property(name="uml_TracedActivityPartition1604", type=umlTrace_uml_TracedActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityPartition1603", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
edge1605: BinaryAssociation = BinaryAssociation(
    name="edge1605",
    ends={
        Property(name="uml_TracedActivityEdge1607", type=umlTrace_uml_TracedActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityPartition1606", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1583: BinaryAssociation = BinaryAssociation(
    name="originalObject1583",
    ends={
        Property(name="uml_umlTrace_ProtocolConformance", type=umlTrace_uml_TracedProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolConformance1584", type=uml_umlTrace_ProtocolConformance, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiteral1585: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral1585",
    ends={
        Property(name="uml_TracedEnumerationLiteral1586", type=umlTrace_uml_TracedEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedEnumeration", type=uml_TracedEnumerationLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
roleBinding1587: BinaryAssociation = BinaryAssociation(
    name="roleBinding1587",
    ends={
        Property(name="uml_TracedDependency1588", type=umlTrace_uml_TracedCollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCollaborationUse", type=uml_TracedDependency, multiplicity=Multiplicity(0, 9999))
    }
)
type1589: BinaryAssociation = BinaryAssociation(
    name="type1589",
    ends={
        Property(name="uml_TracedCollaboration1591", type=umlTrace_uml_TracedCollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCollaborationUse1590", type=uml_TracedCollaboration, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1592: BinaryAssociation = BinaryAssociation(
    name="originalObject1592",
    ends={
        Property(name="uml_umlTrace_CollaborationUse", type=umlTrace_uml_TracedCollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCollaborationUse1593", type=uml_umlTrace_CollaborationUse, multiplicity=Multiplicity(0, 1))
    }
)
node1594: BinaryAssociation = BinaryAssociation(
    name="node1594",
    ends={
        Property(name="uml_TracedActivityNode1595", type=umlTrace_uml_TracedActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityPartition", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
represents1596: BinaryAssociation = BinaryAssociation(
    name="represents1596",
    ends={
        Property(name="uml_TracedElement1598", type=umlTrace_uml_TracedActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityPartition1597", type=uml_TracedElement, multiplicity=Multiplicity(0, 1))
    }
)
activity1621: BinaryAssociation = BinaryAssociation(
    name="activity1621",
    ends={
        Property(name="uml_TracedActivity1622", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode", type=uml_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
inGroup1623: BinaryAssociation = BinaryAssociation(
    name="inGroup1623",
    ends={
        Property(name="uml_TracedActivityGroup", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1624", type=uml_TracedActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
inInterruptibleRegion1625: BinaryAssociation = BinaryAssociation(
    name="inInterruptibleRegion1625",
    ends={
        Property(name="uml_TracedInterruptibleActivityRegion1627", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1626", type=uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1608: BinaryAssociation = BinaryAssociation(
    name="originalObject1608",
    ends={
        Property(name="uml_umlTrace_ActivityPartition", type=umlTrace_uml_TracedActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityPartition1609", type=uml_umlTrace_ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
variable1610: BinaryAssociation = BinaryAssociation(
    name="variable1610",
    ends={
        Property(name="uml_TracedVariable1611", type=umlTrace_uml_TracedVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVariableAction", type=uml_TracedVariable, multiplicity=Multiplicity(1, 1))
    }
)
destroyAt1612: BinaryAssociation = BinaryAssociation(
    name="destroyAt1612",
    ends={
        Property(name="uml_TracedInputPin1613", type=umlTrace_uml_TracedLinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkEndDestructionData", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
addition1614: BinaryAssociation = BinaryAssociation(
    name="addition1614",
    ends={
        Property(name="uml_TracedUseCase1615", type=umlTrace_uml_TracedInclude, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInclude", type=uml_TracedUseCase, multiplicity=Multiplicity(1, 1))
    }
)
includingCase1616: BinaryAssociation = BinaryAssociation(
    name="includingCase1616",
    ends={
        Property(name="uml_TracedUseCase1618", type=umlTrace_uml_TracedInclude, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInclude1617", type=uml_TracedUseCase, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1619: BinaryAssociation = BinaryAssociation(
    name="originalObject1619",
    ends={
        Property(name="uml_umlTrace_Include", type=umlTrace_uml_TracedInclude, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInclude1620", type=uml_umlTrace_Include, multiplicity=Multiplicity(0, 1))
    }
)
deferrableTrigger1648: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger1648",
    ends={
        Property(name="uml_TracedTrigger1650", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1649", type=uml_TracedTrigger, multiplicity=Multiplicity(0, 9999))
    }
)
doActivity1651: BinaryAssociation = BinaryAssociation(
    name="doActivity1651",
    ends={
        Property(name="uml_TracedBehavior1653", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1652", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
entry1654: BinaryAssociation = BinaryAssociation(
    name="entry1654",
    ends={
        Property(name="uml_TracedBehavior1656", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1655", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode1628: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode1628",
    ends={
        Property(name="uml_TracedStructuredActivityNode1630", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1629", type=uml_TracedStructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
incoming1631: BinaryAssociation = BinaryAssociation(
    name="incoming1631",
    ends={
        Property(name="uml_TracedActivityEdge1633", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1632", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing1634: BinaryAssociation = BinaryAssociation(
    name="outgoing1634",
    ends={
        Property(name="uml_TracedActivityEdge1636", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1635", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedNode1637: BinaryAssociation = BinaryAssociation(
    name="redefinedNode1637",
    ends={
        Property(name="uml_TracedActivityNode1639", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1638", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
inPartition1640: BinaryAssociation = BinaryAssociation(
    name="inPartition1640",
    ends={
        Property(name="uml_TracedActivityPartition1642", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1641", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
connection1643: BinaryAssociation = BinaryAssociation(
    name="connection1643",
    ends={
        Property(name="uml_TracedConnectionPointReference1644", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState", type=uml_TracedConnectionPointReference, multiplicity=Multiplicity(0, 9999))
    }
)
connectionPoint1645: BinaryAssociation = BinaryAssociation(
    name="connectionPoint1645",
    ends={
        Property(name="uml_TracedPseudostate1647", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1646", type=uml_TracedPseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
ownedTemplateSignature1678: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateSignature1678",
    ends={
        Property(name="uml_TracedTemplateSignature1680", type=umlTrace_uml_TracedTemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateableElement1679", type=uml_TracedTemplateSignature, multiplicity=Multiplicity(0, 1))
    }
)
specification1681: BinaryAssociation = BinaryAssociation(
    name="specification1681",
    ends={
        Property(name="uml_TracedBehavioralFeature", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior", type=uml_TracedBehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
context1682: BinaryAssociation = BinaryAssociation(
    name="context1682",
    ends={
        Property(name="uml_TracedBehavioredClassifier1684", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior1683", type=uml_TracedBehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
exit1657: BinaryAssociation = BinaryAssociation(
    name="exit1657",
    ends={
        Property(name="uml_TracedBehavior1659", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1658", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
redefinedState1660: BinaryAssociation = BinaryAssociation(
    name="redefinedState1660",
    ends={
        Property(name="uml_TracedState1662", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1661", type=uml_TracedState, multiplicity=Multiplicity(0, 1))
    }
)
stateInvariant1663: BinaryAssociation = BinaryAssociation(
    name="stateInvariant1663",
    ends={
        Property(name="uml_TracedConstraint1665", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1664", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 1))
    }
)
submachine1666: BinaryAssociation = BinaryAssociation(
    name="submachine1666",
    ends={
        Property(name="uml_TracedStateMachine1668", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1667", type=uml_TracedStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
region1669: BinaryAssociation = BinaryAssociation(
    name="region1669",
    ends={
        Property(name="uml_TracedRegion1671", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1670", type=uml_TracedRegion, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_State1672: BinaryAssociation = BinaryAssociation(
    name="originalObject_State1672",
    ends={
        Property(name="uml_umlTrace_State", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1673", type=uml_umlTrace_State, multiplicity=Multiplicity(0, 1))
    }
)
result1674: BinaryAssociation = BinaryAssociation(
    name="result1674",
    ends={
        Property(name="uml_TracedOutputPin1675", type=umlTrace_uml_TracedCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
templateBinding1676: BinaryAssociation = BinaryAssociation(
    name="templateBinding1676",
    ends={
        Property(name="uml_TracedTemplateBinding1677", type=umlTrace_uml_TracedTemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateableElement", type=uml_TracedTemplateBinding, multiplicity=Multiplicity(0, 9999))
    }
)
parameter1702: BinaryAssociation = BinaryAssociation(
    name="parameter1702",
    ends={
        Property(name="uml_TracedParameter1703", type=umlTrace_uml_TracedActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityParameterNode", type=uml_TracedParameter, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1704: BinaryAssociation = BinaryAssociation(
    name="originalObject1704",
    ends={
        Property(name="uml_umlTrace_ActivityParameterNode", type=umlTrace_uml_TracedActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityParameterNode1705", type=uml_umlTrace_ActivityParameterNode, multiplicity=Multiplicity(0, 1))
    }
)
condition1706: BinaryAssociation = BinaryAssociation(
    name="condition1706",
    ends={
        Property(name="uml_TracedConstraint1707", type=umlTrace_uml_TracedParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameterSet", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
parameter1708: BinaryAssociation = BinaryAssociation(
    name="parameter1708",
    ends={
        Property(name="uml_TracedParameter1710", type=umlTrace_uml_TracedParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameterSet1709", type=uml_TracedParameter, multiplicity=Multiplicity(1, 9999))
    }
)
ownedParameter1685: BinaryAssociation = BinaryAssociation(
    name="ownedParameter1685",
    ends={
        Property(name="uml_TracedParameter1687", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior1686", type=uml_TracedParameter, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameterSet1688: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet1688",
    ends={
        Property(name="uml_TracedParameterSet1690", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior1689", type=uml_TracedParameterSet, multiplicity=Multiplicity(0, 9999))
    }
)
postcondition1691: BinaryAssociation = BinaryAssociation(
    name="postcondition1691",
    ends={
        Property(name="uml_TracedConstraint1693", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior1692", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
precondition1694: BinaryAssociation = BinaryAssociation(
    name="precondition1694",
    ends={
        Property(name="uml_TracedConstraint1696", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior1695", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedBehavior1697: BinaryAssociation = BinaryAssociation(
    name="redefinedBehavior1697",
    ends={
        Property(name="uml_TracedBehavior1699", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior1698", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 9999))
    }
)
constrainingClassifier1700: BinaryAssociation = BinaryAssociation(
    name="constrainingClassifier1700",
    ends={
        Property(name="uml_TracedClassifier1701", type=umlTrace_uml_TracedClassifierTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifierTemplateParameter", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
superClass1730: BinaryAssociation = BinaryAssociation(
    name="superClass1730",
    ends={
        Property(name="uml_TracedClass1732", type=umlTrace_uml_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClass1731", type=uml_TracedClass, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_Class1733: BinaryAssociation = BinaryAssociation(
    name="originalObject_Class1733",
    ends={
        Property(name="uml_umlTrace_Class", type=umlTrace_uml_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClass1734", type=uml_umlTrace_Class, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1711: BinaryAssociation = BinaryAssociation(
    name="originalObject1711",
    ends={
        Property(name="uml_umlTrace_ParameterSet", type=umlTrace_uml_TracedParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameterSet1712", type=uml_umlTrace_ParameterSet, multiplicity=Multiplicity(0, 1))
    }
)
expr1713: BinaryAssociation = BinaryAssociation(
    name="expr1713",
    ends={
        Property(name="uml_TracedValueSpecification1714", type=umlTrace_uml_TracedDuration, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDuration", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
observation1715: BinaryAssociation = BinaryAssociation(
    name="observation1715",
    ends={
        Property(name="uml_TracedObservation", type=umlTrace_uml_TracedDuration, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDuration1716", type=uml_TracedObservation, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1717: BinaryAssociation = BinaryAssociation(
    name="originalObject1717",
    ends={
        Property(name="uml_umlTrace_Duration", type=umlTrace_uml_TracedDuration, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDuration1718", type=uml_umlTrace_Duration, multiplicity=Multiplicity(0, 1))
    }
)
ownedOperation1719: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1719",
    ends={
        Property(name="uml_TracedOperation1720", type=umlTrace_uml_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClass", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999))
    }
)
extension1721: BinaryAssociation = BinaryAssociation(
    name="extension1721",
    ends={
        Property(name="uml_TracedExtension1723", type=umlTrace_uml_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClass1722", type=uml_TracedExtension, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier1724: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier1724",
    ends={
        Property(name="uml_TracedClassifier1726", type=umlTrace_uml_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClass1725", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception1727: BinaryAssociation = BinaryAssociation(
    name="ownedReception1727",
    ends={
        Property(name="uml_TracedReception1729", type=umlTrace_uml_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClass1728", type=uml_TracedReception, multiplicity=Multiplicity(0, 9999))
    }
)
mapping1752: BinaryAssociation = BinaryAssociation(
    name="mapping1752",
    ends={
        Property(name="uml_TracedOpaqueExpression1753", type=umlTrace_uml_TracedAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAbstraction", type=uml_TracedOpaqueExpression, multiplicity=Multiplicity(0, 1))
    }
)
result1754: BinaryAssociation = BinaryAssociation(
    name="result1754",
    ends={
        Property(name="uml_TracedOutputPin1755", type=umlTrace_uml_TracedReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadStructuralFeatureAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1756: BinaryAssociation = BinaryAssociation(
    name="originalObject1756",
    ends={
        Property(name="uml_umlTrace_ReadStructuralFeatureAction", type=umlTrace_uml_TracedReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadStructuralFeatureAction1757", type=uml_umlTrace_ReadStructuralFeatureAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1735: BinaryAssociation = BinaryAssociation(
    name="originalObject1735",
    ends={
        Property(name="uml_umlTrace_LiteralUnlimitedNatural", type=umlTrace_uml_TracedLiteralUnlimitedNatural, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLiteralUnlimitedNatural", type=uml_umlTrace_LiteralUnlimitedNatural, multiplicity=Multiplicity(0, 1))
    }
)
edge1736: BinaryAssociation = BinaryAssociation(
    name="edge1736",
    ends={
        Property(name="uml_TracedActivityEdge1737", type=umlTrace_uml_TracedStructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredActivityNode", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNodeInput1738: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput1738",
    ends={
        Property(name="uml_TracedInputPin1740", type=umlTrace_uml_TracedStructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredActivityNode1739", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNodeOutput1741: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput1741",
    ends={
        Property(name="uml_TracedOutputPin1743", type=umlTrace_uml_TracedStructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredActivityNode1742", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
variable1744: BinaryAssociation = BinaryAssociation(
    name="variable1744",
    ends={
        Property(name="uml_TracedVariable1746", type=umlTrace_uml_TracedStructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredActivityNode1745", type=uml_TracedVariable, multiplicity=Multiplicity(0, 9999))
    }
)
node1747: BinaryAssociation = BinaryAssociation(
    name="node1747",
    ends={
        Property(name="uml_TracedActivityNode1749", type=umlTrace_uml_TracedStructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredActivityNode1748", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_StructuredActivityNode1750: BinaryAssociation = BinaryAssociation(
    name="originalObject_StructuredActivityNode1750",
    ends={
        Property(name="uml_umlTrace_StructuredActivityNode", type=umlTrace_uml_TracedStructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredActivityNode1751", type=uml_umlTrace_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
specific1773: BinaryAssociation = BinaryAssociation(
    name="specific1773",
    ends={
        Property(name="uml_TracedClassifier1775", type=umlTrace_uml_TracedGeneralization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralization1774", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1776: BinaryAssociation = BinaryAssociation(
    name="originalObject1776",
    ends={
        Property(name="uml_umlTrace_Generalization", type=umlTrace_uml_TracedGeneralization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralization1777", type=uml_umlTrace_Generalization, multiplicity=Multiplicity(0, 1))
    }
)
type1778: BinaryAssociation = BinaryAssociation(
    name="type1778",
    ends={
        Property(name="uml_TracedType1779", type=umlTrace_uml_TracedTypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTypedElement", type=uml_TracedType, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1758: BinaryAssociation = BinaryAssociation(
    name="originalObject1758",
    ends={
        Property(name="uml_umlTrace_MergeNode", type=umlTrace_uml_TracedMergeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMergeNode", type=uml_umlTrace_MergeNode, multiplicity=Multiplicity(0, 1))
    }
)
extendedSignature1759: BinaryAssociation = BinaryAssociation(
    name="extendedSignature1759",
    ends={
        Property(name="uml_TracedRedefinableTemplateSignature1760", type=umlTrace_uml_TracedRedefinableTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRedefinableTemplateSignature", type=uml_TracedRedefinableTemplateSignature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedParameter1761: BinaryAssociation = BinaryAssociation(
    name="inheritedParameter1761",
    ends={
        Property(name="uml_TracedTemplateParameter1763", type=umlTrace_uml_TracedRedefinableTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRedefinableTemplateSignature1762", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(0, 9999))
    }
)
classifier1764: BinaryAssociation = BinaryAssociation(
    name="classifier1764",
    ends={
        Property(name="uml_TracedClassifier1766", type=umlTrace_uml_TracedRedefinableTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRedefinableTemplateSignature1765", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
originalObject_CreateLinkAction1767: BinaryAssociation = BinaryAssociation(
    name="originalObject_CreateLinkAction1767",
    ends={
        Property(name="uml_umlTrace_CreateLinkAction", type=umlTrace_uml_TracedCreateLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCreateLinkAction", type=uml_umlTrace_CreateLinkAction, multiplicity=Multiplicity(0, 1))
    }
)
general1768: BinaryAssociation = BinaryAssociation(
    name="general1768",
    ends={
        Property(name="uml_TracedClassifier1769", type=umlTrace_uml_TracedGeneralization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralization", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet1770: BinaryAssociation = BinaryAssociation(
    name="generalizationSet1770",
    ends={
        Property(name="uml_TracedGeneralizationSet1772", type=umlTrace_uml_TracedGeneralization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralization1771", type=uml_TracedGeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
templateBinding1797: BinaryAssociation = BinaryAssociation(
    name="templateBinding1797",
    ends={
        Property(name="uml_TracedTemplateBinding1799", type=umlTrace_uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameterSubstitution1798", type=uml_TracedTemplateBinding, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1800: BinaryAssociation = BinaryAssociation(
    name="originalObject1800",
    ends={
        Property(name="uml_umlTrace_TemplateParameterSubstitution", type=umlTrace_uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameterSubstitution1801", type=uml_umlTrace_TemplateParameterSubstitution, multiplicity=Multiplicity(0, 1))
    }
)
condition1802: BinaryAssociation = BinaryAssociation(
    name="condition1802",
    ends={
        Property(name="uml_TracedConstraint1803", type=umlTrace_uml_TracedExtend, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtend", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 1))
    }
)
object1780: BinaryAssociation = BinaryAssociation(
    name="object1780",
    ends={
        Property(name="uml_TracedInputPin1781", type=umlTrace_uml_TracedReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndQualifierAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
qualifier1782: BinaryAssociation = BinaryAssociation(
    name="qualifier1782",
    ends={
        Property(name="uml_TracedProperty1784", type=umlTrace_uml_TracedReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndQualifierAction1783", type=uml_TracedProperty, multiplicity=Multiplicity(1, 1))
    }
)
result1785: BinaryAssociation = BinaryAssociation(
    name="result1785",
    ends={
        Property(name="uml_TracedOutputPin1787", type=umlTrace_uml_TracedReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndQualifierAction1786", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1788: BinaryAssociation = BinaryAssociation(
    name="originalObject1788",
    ends={
        Property(name="uml_umlTrace_ReadLinkObjectEndQualifierAction", type=umlTrace_uml_TracedReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndQualifierAction1789", type=uml_umlTrace_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(0, 1))
    }
)
actual1790: BinaryAssociation = BinaryAssociation(
    name="actual1790",
    ends={
        Property(name="uml_TracedParameterableElement", type=umlTrace_uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameterSubstitution", type=uml_TracedParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
formal1791: BinaryAssociation = BinaryAssociation(
    name="formal1791",
    ends={
        Property(name="uml_TracedTemplateParameter1793", type=umlTrace_uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameterSubstitution1792", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1))
    }
)
ownedActual1794: BinaryAssociation = BinaryAssociation(
    name="ownedActual1794",
    ends={
        Property(name="uml_TracedParameterableElement1796", type=umlTrace_uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameterSubstitution1795", type=uml_TracedParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
connector1821: BinaryAssociation = BinaryAssociation(
    name="connector1821",
    ends={
        Property(name="uml_TracedConnector1823", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage1822", type=uml_TracedConnector, multiplicity=Multiplicity(0, 1))
    }
)
interaction1824: BinaryAssociation = BinaryAssociation(
    name="interaction1824",
    ends={
        Property(name="uml_TracedInteraction1826", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage1825", type=uml_TracedInteraction, multiplicity=Multiplicity(1, 1))
    }
)
receiveEvent1827: BinaryAssociation = BinaryAssociation(
    name="receiveEvent1827",
    ends={
        Property(name="uml_TracedMessageEnd", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage1828", type=uml_TracedMessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
sendEvent1829: BinaryAssociation = BinaryAssociation(
    name="sendEvent1829",
    ends={
        Property(name="uml_TracedMessageEnd1831", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage1830", type=uml_TracedMessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
extendedCase1804: BinaryAssociation = BinaryAssociation(
    name="extendedCase1804",
    ends={
        Property(name="uml_TracedUseCase1806", type=umlTrace_uml_TracedExtend, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtend1805", type=uml_TracedUseCase, multiplicity=Multiplicity(1, 1))
    }
)
extensionLocation1807: BinaryAssociation = BinaryAssociation(
    name="extensionLocation1807",
    ends={
        Property(name="uml_TracedExtensionPoint1809", type=umlTrace_uml_TracedExtend, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtend1808", type=uml_TracedExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
extension1810: BinaryAssociation = BinaryAssociation(
    name="extension1810",
    ends={
        Property(name="uml_TracedUseCase1812", type=umlTrace_uml_TracedExtend, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtend1811", type=uml_TracedUseCase, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1813: BinaryAssociation = BinaryAssociation(
    name="originalObject1813",
    ends={
        Property(name="uml_umlTrace_Extend", type=umlTrace_uml_TracedExtend, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtend1814", type=uml_umlTrace_Extend, multiplicity=Multiplicity(0, 1))
    }
)
result1815: BinaryAssociation = BinaryAssociation(
    name="result1815",
    ends={
        Property(name="uml_TracedOutputPin1816", type=umlTrace_uml_TracedReadVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadVariableAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1817: BinaryAssociation = BinaryAssociation(
    name="originalObject1817",
    ends={
        Property(name="uml_umlTrace_ReadVariableAction", type=umlTrace_uml_TracedReadVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadVariableAction1818", type=uml_umlTrace_ReadVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
argument1819: BinaryAssociation = BinaryAssociation(
    name="argument1819",
    ends={
        Property(name="uml_TracedValueSpecification1820", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1847: BinaryAssociation = BinaryAssociation(
    name="originalObject1847",
    ends={
        Property(name="uml_umlTrace_ClearVariableAction", type=umlTrace_uml_TracedClearVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClearVariableAction", type=uml_umlTrace_ClearVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
appliedProfile1848: BinaryAssociation = BinaryAssociation(
    name="appliedProfile1848",
    ends={
        Property(name="uml_TracedProfile1849", type=umlTrace_uml_TracedProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProfileApplication", type=uml_TracedProfile, multiplicity=Multiplicity(1, 1))
    }
)
applyingPackage1850: BinaryAssociation = BinaryAssociation(
    name="applyingPackage1850",
    ends={
        Property(name="uml_TracedPackage1852", type=umlTrace_uml_TracedProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProfileApplication1851", type=uml_TracedPackage, multiplicity=Multiplicity(1, 1))
    }
)
signature1832: BinaryAssociation = BinaryAssociation(
    name="signature1832",
    ends={
        Property(name="uml_TracedNamedElement1834", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage1833", type=uml_TracedNamedElement, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1835: BinaryAssociation = BinaryAssociation(
    name="originalObject1835",
    ends={
        Property(name="uml_umlTrace_Message", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage1836", type=uml_umlTrace_Message, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1837: BinaryAssociation = BinaryAssociation(
    name="originalObject1837",
    ends={
        Property(name="uml_umlTrace_LiteralBoolean", type=umlTrace_uml_TracedLiteralBoolean, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLiteralBoolean", type=uml_umlTrace_LiteralBoolean, multiplicity=Multiplicity(0, 1))
    }
)
qualifier1838: BinaryAssociation = BinaryAssociation(
    name="qualifier1838",
    ends={
        Property(name="uml_TracedProperty1839", type=umlTrace_uml_TracedQualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedQualifierValue", type=uml_TracedProperty, multiplicity=Multiplicity(1, 1))
    }
)
value1840: BinaryAssociation = BinaryAssociation(
    name="value1840",
    ends={
        Property(name="uml_TracedInputPin1842", type=umlTrace_uml_TracedQualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedQualifierValue1841", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1843: BinaryAssociation = BinaryAssociation(
    name="originalObject1843",
    ends={
        Property(name="uml_umlTrace_QualifierValue", type=umlTrace_uml_TracedQualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedQualifierValue1844", type=uml_umlTrace_QualifierValue, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1845: BinaryAssociation = BinaryAssociation(
    name="originalObject1845",
    ends={
        Property(name="uml_umlTrace_InitialNode", type=umlTrace_uml_TracedInitialNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInitialNode", type=uml_umlTrace_InitialNode, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1846: BinaryAssociation = BinaryAssociation(
    name="originalObject1846",
    ends={
        Property(name="uml_umlTrace_LiteralInteger", type=umlTrace_uml_TracedLiteralInteger, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLiteralInteger", type=uml_umlTrace_LiteralInteger, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_TemplateParameter1874: BinaryAssociation = BinaryAssociation(
    name="originalObject_TemplateParameter1874",
    ends={
        Property(name="uml_umlTrace_TemplateParameter", type=umlTrace_uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameter1875", type=uml_umlTrace_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
definingEnd1876: BinaryAssociation = BinaryAssociation(
    name="definingEnd1876",
    ends={
        Property(name="uml_TracedProperty1877", type=umlTrace_uml_TracedConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectorEnd", type=uml_TracedProperty, multiplicity=Multiplicity(0, 1))
    }
)
partWithPort1878: BinaryAssociation = BinaryAssociation(
    name="partWithPort1878",
    ends={
        Property(name="uml_TracedProperty1880", type=umlTrace_uml_TracedConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectorEnd1879", type=uml_TracedProperty, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1853: BinaryAssociation = BinaryAssociation(
    name="originalObject1853",
    ends={
        Property(name="uml_umlTrace_ProfileApplication", type=umlTrace_uml_TracedProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProfileApplication1854", type=uml_umlTrace_ProfileApplication, multiplicity=Multiplicity(0, 1))
    }
)
owningTemplateParameter1855: BinaryAssociation = BinaryAssociation(
    name="owningTemplateParameter1855",
    ends={
        Property(name="uml_TracedTemplateParameter1856", type=umlTrace_uml_TracedParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameterableElement", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
templateParameter1857: BinaryAssociation = BinaryAssociation(
    name="templateParameter1857",
    ends={
        Property(name="uml_TracedTemplateParameter1859", type=umlTrace_uml_TracedParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameterableElement1858", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
default1860: BinaryAssociation = BinaryAssociation(
    name="default1860",
    ends={
        Property(name="uml_TracedParameterableElement1861", type=umlTrace_uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameter", type=uml_TracedParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
ownedDefault1862: BinaryAssociation = BinaryAssociation(
    name="ownedDefault1862",
    ends={
        Property(name="uml_TracedParameterableElement1864", type=umlTrace_uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameter1863", type=uml_TracedParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
parameteredElement1865: BinaryAssociation = BinaryAssociation(
    name="parameteredElement1865",
    ends={
        Property(name="uml_TracedParameterableElement1867", type=umlTrace_uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameter1866", type=uml_TracedParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
signature1868: BinaryAssociation = BinaryAssociation(
    name="signature1868",
    ends={
        Property(name="uml_TracedTemplateSignature1870", type=umlTrace_uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameter1869", type=uml_TracedTemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameteredElement1871: BinaryAssociation = BinaryAssociation(
    name="ownedParameteredElement1871",
    ends={
        Property(name="uml_TracedParameterableElement1873", type=umlTrace_uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameter1872", type=uml_TracedParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1897: BinaryAssociation = BinaryAssociation(
    name="originalObject1897",
    ends={
        Property(name="uml_umlTrace_Parameter", type=umlTrace_uml_TracedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameter1898", type=uml_umlTrace_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
fromAction1899: BinaryAssociation = BinaryAssociation(
    name="fromAction1899",
    ends={
        Property(name="uml_TracedAction1900", type=umlTrace_uml_TracedActionInputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActionInputPin", type=uml_TracedAction, multiplicity=Multiplicity(1, 1))
    }
)
event1901: BinaryAssociation = BinaryAssociation(
    name="event1901",
    ends={
        Property(name="uml_TracedEvent", type=umlTrace_uml_TracedTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTrigger", type=uml_TracedEvent, multiplicity=Multiplicity(1, 1))
    }
)
role1881: BinaryAssociation = BinaryAssociation(
    name="role1881",
    ends={
        Property(name="uml_TracedConnectableElement1883", type=umlTrace_uml_TracedConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectorEnd1882", type=uml_TracedConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1884: BinaryAssociation = BinaryAssociation(
    name="originalObject1884",
    ends={
        Property(name="uml_umlTrace_ConnectorEnd", type=umlTrace_uml_TracedConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectorEnd1885", type=uml_umlTrace_ConnectorEnd, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1886: BinaryAssociation = BinaryAssociation(
    name="originalObject1886",
    ends={
        Property(name="uml_umlTrace_Image", type=umlTrace_uml_TracedImage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedImage", type=uml_umlTrace_Image, multiplicity=Multiplicity(0, 1))
    }
)
ownedPort1887: BinaryAssociation = BinaryAssociation(
    name="ownedPort1887",
    ends={
        Property(name="uml_TracedPort1888", type=umlTrace_uml_TracedEncapsulatedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedEncapsulatedClassifier", type=uml_TracedPort, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue1889: BinaryAssociation = BinaryAssociation(
    name="defaultValue1889",
    ends={
        Property(name="uml_TracedValueSpecification1890", type=umlTrace_uml_TracedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameter", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
operation1891: BinaryAssociation = BinaryAssociation(
    name="operation1891",
    ends={
        Property(name="uml_TracedOperation1893", type=umlTrace_uml_TracedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameter1892", type=uml_TracedOperation, multiplicity=Multiplicity(0, 1))
    }
)
parameterSet1894: BinaryAssociation = BinaryAssociation(
    name="parameterSet1894",
    ends={
        Property(name="uml_TracedParameterSet1896", type=umlTrace_uml_TracedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameter1895", type=uml_TracedParameterSet, multiplicity=Multiplicity(0, 9999))
    }
)
min1921: BinaryAssociation = BinaryAssociation(
    name="min1921",
    ends={
        Property(name="uml_TracedValueSpecification1923", type=umlTrace_uml_TracedInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterval1922", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject_Interval1924: BinaryAssociation = BinaryAssociation(
    name="originalObject_Interval1924",
    ends={
        Property(name="uml_umlTrace_Interval", type=umlTrace_uml_TracedInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterval1925", type=uml_umlTrace_Interval, multiplicity=Multiplicity(0, 1))
    }
)
classifier1926: BinaryAssociation = BinaryAssociation(
    name="classifier1926",
    ends={
        Property(name="uml_TracedClassifier1927", type=umlTrace_uml_TracedInstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInstanceSpecification", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
port1902: BinaryAssociation = BinaryAssociation(
    name="port1902",
    ends={
        Property(name="uml_TracedPort1904", type=umlTrace_uml_TracedTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTrigger1903", type=uml_TracedPort, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1905: BinaryAssociation = BinaryAssociation(
    name="originalObject1905",
    ends={
        Property(name="uml_umlTrace_Trigger", type=umlTrace_uml_TracedTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTrigger1906", type=uml_umlTrace_Trigger, multiplicity=Multiplicity(0, 1))
    }
)
operation1907: BinaryAssociation = BinaryAssociation(
    name="operation1907",
    ends={
        Property(name="uml_TracedOperation1908", type=umlTrace_uml_TracedCallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallOperationAction", type=uml_TracedOperation, multiplicity=Multiplicity(1, 1))
    }
)
target1909: BinaryAssociation = BinaryAssociation(
    name="target1909",
    ends={
        Property(name="uml_TracedInputPin1911", type=umlTrace_uml_TracedCallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallOperationAction1910", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1912: BinaryAssociation = BinaryAssociation(
    name="originalObject1912",
    ends={
        Property(name="uml_umlTrace_CallOperationAction", type=umlTrace_uml_TracedCallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallOperationAction1913", type=uml_umlTrace_CallOperationAction, multiplicity=Multiplicity(0, 1))
    }
)
metaclassReference1914: BinaryAssociation = BinaryAssociation(
    name="metaclassReference1914",
    ends={
        Property(name="uml_TracedElementImport1915", type=umlTrace_uml_TracedProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProfile", type=uml_TracedElementImport, multiplicity=Multiplicity(0, 9999))
    }
)
metamodelReference1916: BinaryAssociation = BinaryAssociation(
    name="metamodelReference1916",
    ends={
        Property(name="uml_TracedPackageImport1918", type=umlTrace_uml_TracedProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProfile1917", type=uml_TracedPackageImport, multiplicity=Multiplicity(0, 9999))
    }
)
max1919: BinaryAssociation = BinaryAssociation(
    name="max1919",
    ends={
        Property(name="uml_TracedValueSpecification1920", type=umlTrace_uml_TracedInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterval", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1946: BinaryAssociation = BinaryAssociation(
    name="originalObject1946",
    ends={
        Property(name="uml_umlTrace_ReadIsClassifiedObjectAction", type=umlTrace_uml_TracedReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadIsClassifiedObjectAction1947", type=uml_umlTrace_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(0, 1))
    }
)
conformance1948: BinaryAssociation = BinaryAssociation(
    name="conformance1948",
    ends={
        Property(name="uml_TracedProtocolConformance1949", type=umlTrace_uml_TracedProtocolStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolStateMachine", type=uml_TracedProtocolConformance, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1950: BinaryAssociation = BinaryAssociation(
    name="originalObject1950",
    ends={
        Property(name="uml_umlTrace_OutputPin", type=umlTrace_uml_TracedOutputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOutputPin", type=uml_umlTrace_OutputPin, multiplicity=Multiplicity(0, 1))
    }
)
slot1928: BinaryAssociation = BinaryAssociation(
    name="slot1928",
    ends={
        Property(name="uml_TracedSlot1930", type=umlTrace_uml_TracedInstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInstanceSpecification1929", type=uml_TracedSlot, multiplicity=Multiplicity(0, 9999))
    }
)
specification1931: BinaryAssociation = BinaryAssociation(
    name="specification1931",
    ends={
        Property(name="uml_TracedValueSpecification1933", type=umlTrace_uml_TracedInstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInstanceSpecification1932", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_InstanceSpecification1934: BinaryAssociation = BinaryAssociation(
    name="originalObject_InstanceSpecification1934",
    ends={
        Property(name="uml_umlTrace_InstanceSpecification", type=umlTrace_uml_TracedInstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInstanceSpecification1935", type=uml_umlTrace_InstanceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
value1936: BinaryAssociation = BinaryAssociation(
    name="value1936",
    ends={
        Property(name="uml_TracedValueSpecification1937", type=umlTrace_uml_TracedValuePin, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedValuePin", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
classifier1938: BinaryAssociation = BinaryAssociation(
    name="classifier1938",
    ends={
        Property(name="uml_TracedClassifier1939", type=umlTrace_uml_TracedReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadIsClassifiedObjectAction", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
object1940: BinaryAssociation = BinaryAssociation(
    name="object1940",
    ends={
        Property(name="uml_TracedInputPin1942", type=umlTrace_uml_TracedReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadIsClassifiedObjectAction1941", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
result1943: BinaryAssociation = BinaryAssociation(
    name="result1943",
    ends={
        Property(name="uml_TracedOutputPin1945", type=umlTrace_uml_TracedReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadIsClassifiedObjectAction1944", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1963: BinaryAssociation = BinaryAssociation(
    name="originalObject1963",
    ends={
        Property(name="uml_umlTrace_ValueSpecificationAction", type=umlTrace_uml_TracedValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedValueSpecificationAction1964", type=uml_umlTrace_ValueSpecificationAction, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion1965: BinaryAssociation = BinaryAssociation(
    name="extendedRegion1965",
    ends={
        Property(name="uml_TracedRegion1966", type=umlTrace_uml_TracedRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRegion", type=uml_TracedRegion, multiplicity=Multiplicity(0, 1))
    }
)
decisionInput1951: BinaryAssociation = BinaryAssociation(
    name="decisionInput1951",
    ends={
        Property(name="uml_TracedBehavior1952", type=umlTrace_uml_TracedDecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDecisionNode", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
decisionInputFlow1953: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow1953",
    ends={
        Property(name="uml_TracedObjectFlow1955", type=umlTrace_uml_TracedDecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDecisionNode1954", type=uml_TracedObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1956: BinaryAssociation = BinaryAssociation(
    name="originalObject1956",
    ends={
        Property(name="uml_umlTrace_DecisionNode", type=umlTrace_uml_TracedDecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDecisionNode1957", type=uml_umlTrace_DecisionNode, multiplicity=Multiplicity(0, 1))
    }
)
result1958: BinaryAssociation = BinaryAssociation(
    name="result1958",
    ends={
        Property(name="uml_TracedOutputPin1959", type=umlTrace_uml_TracedValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedValueSpecificationAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
value1960: BinaryAssociation = BinaryAssociation(
    name="value1960",
    ends={
        Property(name="uml_TracedValueSpecification1962", type=umlTrace_uml_TracedValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedValueSpecificationAction1961", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1985: BinaryAssociation = BinaryAssociation(
    name="originalObject1985",
    ends={
        Property(name="uml_umlTrace_InterruptibleActivityRegion", type=umlTrace_uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterruptibleActivityRegion1986", type=uml_umlTrace_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1987: BinaryAssociation = BinaryAssociation(
    name="originalObject1987",
    ends={
        Property(name="uml_umlTrace_DestroyLinkAction", type=umlTrace_uml_TracedDestroyLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDestroyLinkAction", type=uml_umlTrace_DestroyLinkAction, multiplicity=Multiplicity(0, 1))
    }
)
state1967: BinaryAssociation = BinaryAssociation(
    name="state1967",
    ends={
        Property(name="uml_TracedState1969", type=umlTrace_uml_TracedRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRegion1968", type=uml_TracedState, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine1970: BinaryAssociation = BinaryAssociation(
    name="stateMachine1970",
    ends={
        Property(name="uml_TracedStateMachine1972", type=umlTrace_uml_TracedRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRegion1971", type=uml_TracedStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
transition1973: BinaryAssociation = BinaryAssociation(
    name="transition1973",
    ends={
        Property(name="uml_TracedTransition1975", type=umlTrace_uml_TracedRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRegion1974", type=uml_TracedTransition, multiplicity=Multiplicity(0, 9999))
    }
)
subvertex1976: BinaryAssociation = BinaryAssociation(
    name="subvertex1976",
    ends={
        Property(name="uml_TracedVertex", type=umlTrace_uml_TracedRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRegion1977", type=uml_TracedVertex, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1978: BinaryAssociation = BinaryAssociation(
    name="originalObject1978",
    ends={
        Property(name="uml_umlTrace_Region", type=umlTrace_uml_TracedRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRegion1979", type=uml_umlTrace_Region, multiplicity=Multiplicity(0, 1))
    }
)
interruptingEdge1980: BinaryAssociation = BinaryAssociation(
    name="interruptingEdge1980",
    ends={
        Property(name="uml_TracedActivityEdge1981", type=umlTrace_uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterruptibleActivityRegion", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
node1982: BinaryAssociation = BinaryAssociation(
    name="node1982",
    ends={
        Property(name="uml_TracedActivityNode1984", type=umlTrace_uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterruptibleActivityRegion1983", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
guard2004: BinaryAssociation = BinaryAssociation(
    name="guard2004",
    ends={
        Property(name="uml_TracedInteractionConstraint2006", type=umlTrace_uml_TracedInteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionOperand2005", type=uml_TracedInteractionConstraint, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2007: BinaryAssociation = BinaryAssociation(
    name="originalObject2007",
    ends={
        Property(name="uml_umlTrace_InteractionOperand", type=umlTrace_uml_TracedInteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionOperand2008", type=uml_umlTrace_InteractionOperand, multiplicity=Multiplicity(0, 1))
    }
)
containedEdge1988: BinaryAssociation = BinaryAssociation(
    name="containedEdge1988",
    ends={
        Property(name="uml_TracedActivityEdge1989", type=umlTrace_uml_TracedActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityGroup", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
containedNode1990: BinaryAssociation = BinaryAssociation(
    name="containedNode1990",
    ends={
        Property(name="uml_TracedActivityNode1992", type=umlTrace_uml_TracedActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityGroup1991", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
inActivity1993: BinaryAssociation = BinaryAssociation(
    name="inActivity1993",
    ends={
        Property(name="uml_TracedActivity1995", type=umlTrace_uml_TracedActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityGroup1994", type=uml_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
subgroup1996: BinaryAssociation = BinaryAssociation(
    name="subgroup1996",
    ends={
        Property(name="uml_TracedActivityGroup1998", type=umlTrace_uml_TracedActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityGroup1997", type=uml_TracedActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
superGroup1999: BinaryAssociation = BinaryAssociation(
    name="superGroup1999",
    ends={
        Property(name="uml_TracedActivityGroup2001", type=umlTrace_uml_TracedActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityGroup2000", type=uml_TracedActivityGroup, multiplicity=Multiplicity(0, 1))
    }
)
fragment2002: BinaryAssociation = BinaryAssociation(
    name="fragment2002",
    ends={
        Property(name="uml_TracedInteractionFragment2003", type=umlTrace_uml_TracedInteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionOperand", type=uml_TracedInteractionFragment, multiplicity=Multiplicity(0, 9999))
    }
)
weight2032: BinaryAssociation = BinaryAssociation(
    name="weight2032",
    ends={
        Property(name="uml_TracedValueSpecification2034", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2033", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
inGroup2035: BinaryAssociation = BinaryAssociation(
    name="inGroup2035",
    ends={
        Property(name="uml_TracedActivityGroup2037", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2036", type=uml_TracedActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
conveyed2038: BinaryAssociation = BinaryAssociation(
    name="conveyed2038",
    ends={
        Property(name="uml_TracedClassifier2039", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 9999))
    }
)
activity2009: BinaryAssociation = BinaryAssociation(
    name="activity2009",
    ends={
        Property(name="uml_TracedActivity2010", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge", type=uml_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
guard2011: BinaryAssociation = BinaryAssociation(
    name="guard2011",
    ends={
        Property(name="uml_TracedValueSpecification2013", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2012", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
inPartition2014: BinaryAssociation = BinaryAssociation(
    name="inPartition2014",
    ends={
        Property(name="uml_TracedActivityPartition2016", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2015", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
interrupts2017: BinaryAssociation = BinaryAssociation(
    name="interrupts2017",
    ends={
        Property(name="uml_TracedInterruptibleActivityRegion2019", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2018", type=uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode2020: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode2020",
    ends={
        Property(name="uml_TracedStructuredActivityNode2022", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2021", type=uml_TracedStructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
target2023: BinaryAssociation = BinaryAssociation(
    name="target2023",
    ends={
        Property(name="uml_TracedActivityNode2025", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2024", type=uml_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
source2026: BinaryAssociation = BinaryAssociation(
    name="source2026",
    ends={
        Property(name="uml_TracedActivityNode2028", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2027", type=uml_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
redefinedEdge2029: BinaryAssociation = BinaryAssociation(
    name="redefinedEdge2029",
    ends={
        Property(name="uml_TracedActivityEdge2031", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2030", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
stateMachine2061: BinaryAssociation = BinaryAssociation(
    name="stateMachine2061",
    ends={
        Property(name="uml_TracedStateMachine2063", type=umlTrace_uml_TracedPseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPseudostate2062", type=uml_TracedStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2064: BinaryAssociation = BinaryAssociation(
    name="originalObject2064",
    ends={
        Property(name="uml_umlTrace_Pseudostate", type=umlTrace_uml_TracedPseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPseudostate2065", type=uml_umlTrace_Pseudostate, multiplicity=Multiplicity(0, 1))
    }
)
extend2066: BinaryAssociation = BinaryAssociation(
    name="extend2066",
    ends={
        Property(name="uml_TracedExtend2067", type=umlTrace_uml_TracedUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUseCase", type=uml_TracedExtend, multiplicity=Multiplicity(0, 9999))
    }
)
informationSource2040: BinaryAssociation = BinaryAssociation(
    name="informationSource2040",
    ends={
        Property(name="uml_TracedNamedElement2042", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2041", type=uml_TracedNamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
informationTarget2043: BinaryAssociation = BinaryAssociation(
    name="informationTarget2043",
    ends={
        Property(name="uml_TracedNamedElement2045", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2044", type=uml_TracedNamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
realization2046: BinaryAssociation = BinaryAssociation(
    name="realization2046",
    ends={
        Property(name="uml_TracedRelationship", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2047", type=uml_TracedRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
realizingActivityEdge2048: BinaryAssociation = BinaryAssociation(
    name="realizingActivityEdge2048",
    ends={
        Property(name="uml_TracedActivityEdge2050", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2049", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
realizingConnector2051: BinaryAssociation = BinaryAssociation(
    name="realizingConnector2051",
    ends={
        Property(name="uml_TracedConnector2053", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2052", type=uml_TracedConnector, multiplicity=Multiplicity(0, 9999))
    }
)
realizingMessage2054: BinaryAssociation = BinaryAssociation(
    name="realizingMessage2054",
    ends={
        Property(name="uml_TracedMessage2056", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2055", type=uml_TracedMessage, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2057: BinaryAssociation = BinaryAssociation(
    name="originalObject2057",
    ends={
        Property(name="uml_umlTrace_InformationFlow", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2058", type=uml_umlTrace_InformationFlow, multiplicity=Multiplicity(0, 1))
    }
)
state2059: BinaryAssociation = BinaryAssociation(
    name="state2059",
    ends={
        Property(name="uml_TracedState2060", type=umlTrace_uml_TracedPseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPseudostate", type=uml_TracedState, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2087: BinaryAssociation = BinaryAssociation(
    name="originalObject2087",
    ends={
        Property(name="uml_umlTrace_ReplyAction", type=umlTrace_uml_TracedReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReplyAction2088", type=uml_umlTrace_ReplyAction, multiplicity=Multiplicity(0, 1))
    }
)
cfragmentGate2089: BinaryAssociation = BinaryAssociation(
    name="cfragmentGate2089",
    ends={
        Property(name="uml_TracedGate2090", type=umlTrace_uml_TracedCombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCombinedFragment", type=uml_TracedGate, multiplicity=Multiplicity(0, 9999))
    }
)
operand2091: BinaryAssociation = BinaryAssociation(
    name="operand2091",
    ends={
        Property(name="uml_TracedInteractionOperand2093", type=umlTrace_uml_TracedCombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCombinedFragment2092", type=uml_TracedInteractionOperand, multiplicity=Multiplicity(1, 9999))
    }
)
originalObject_CombinedFragment2094: BinaryAssociation = BinaryAssociation(
    name="originalObject_CombinedFragment2094",
    ends={
        Property(name="uml_umlTrace_CombinedFragment", type=umlTrace_uml_TracedCombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCombinedFragment2095", type=uml_umlTrace_CombinedFragment, multiplicity=Multiplicity(0, 1))
    }
)
extensionPoint2068: BinaryAssociation = BinaryAssociation(
    name="extensionPoint2068",
    ends={
        Property(name="uml_TracedExtensionPoint2070", type=umlTrace_uml_TracedUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUseCase2069", type=uml_TracedExtensionPoint, multiplicity=Multiplicity(0, 9999))
    }
)
include2071: BinaryAssociation = BinaryAssociation(
    name="include2071",
    ends={
        Property(name="uml_TracedInclude2073", type=umlTrace_uml_TracedUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUseCase2072", type=uml_TracedInclude, multiplicity=Multiplicity(0, 9999))
    }
)
subject2074: BinaryAssociation = BinaryAssociation(
    name="subject2074",
    ends={
        Property(name="uml_TracedClassifier2076", type=umlTrace_uml_TracedUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUseCase2075", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2077: BinaryAssociation = BinaryAssociation(
    name="originalObject2077",
    ends={
        Property(name="uml_umlTrace_UseCase", type=umlTrace_uml_TracedUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUseCase2078", type=uml_umlTrace_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
replyToCall2079: BinaryAssociation = BinaryAssociation(
    name="replyToCall2079",
    ends={
        Property(name="uml_TracedTrigger2080", type=umlTrace_uml_TracedReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReplyAction", type=uml_TracedTrigger, multiplicity=Multiplicity(1, 1))
    }
)
replyValue2081: BinaryAssociation = BinaryAssociation(
    name="replyValue2081",
    ends={
        Property(name="uml_TracedInputPin2083", type=umlTrace_uml_TracedReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReplyAction2082", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999))
    }
)
returnInformation2084: BinaryAssociation = BinaryAssociation(
    name="returnInformation2084",
    ends={
        Property(name="uml_TracedInputPin2086", type=umlTrace_uml_TracedReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReplyAction2085", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2117: BinaryAssociation = BinaryAssociation(
    name="originalObject2117",
    ends={
        Property(name="uml_umlTrace_InstanceValue", type=umlTrace_uml_TracedInstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInstanceValue2118", type=uml_umlTrace_InstanceValue, multiplicity=Multiplicity(0, 1))
    }
)
client2119: BinaryAssociation = BinaryAssociation(
    name="client2119",
    ends={
        Property(name="uml_TracedNamedElement2120", type=umlTrace_uml_TracedDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDependency", type=uml_TracedNamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
supplier2121: BinaryAssociation = BinaryAssociation(
    name="supplier2121",
    ends={
        Property(name="uml_TracedNamedElement2123", type=umlTrace_uml_TracedDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDependency2122", type=uml_TracedNamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
body2096: BinaryAssociation = BinaryAssociation(
    name="body2096",
    ends={
        Property(name="uml_TracedExecutableNode2097", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause", type=uml_TracedExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
bodyOutput2098: BinaryAssociation = BinaryAssociation(
    name="bodyOutput2098",
    ends={
        Property(name="uml_TracedOutputPin2100", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause2099", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
decider2101: BinaryAssociation = BinaryAssociation(
    name="decider2101",
    ends={
        Property(name="uml_TracedOutputPin2103", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause2102", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
predecessorClause2104: BinaryAssociation = BinaryAssociation(
    name="predecessorClause2104",
    ends={
        Property(name="uml_TracedClause2106", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause2105", type=uml_TracedClause, multiplicity=Multiplicity(0, 9999))
    }
)
successorClause2107: BinaryAssociation = BinaryAssociation(
    name="successorClause2107",
    ends={
        Property(name="uml_TracedClause2109", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause2108", type=uml_TracedClause, multiplicity=Multiplicity(0, 9999))
    }
)
test2110: BinaryAssociation = BinaryAssociation(
    name="test2110",
    ends={
        Property(name="uml_TracedExecutableNode2112", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause2111", type=uml_TracedExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
originalObject2113: BinaryAssociation = BinaryAssociation(
    name="originalObject2113",
    ends={
        Property(name="uml_umlTrace_Clause", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause2114", type=uml_umlTrace_Clause, multiplicity=Multiplicity(0, 1))
    }
)
instance2115: BinaryAssociation = BinaryAssociation(
    name="instance2115",
    ends={
        Property(name="uml_TracedInstanceSpecification2116", type=umlTrace_uml_TracedInstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInstanceValue", type=uml_TracedInstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2140: BinaryAssociation = BinaryAssociation(
    name="originalObject2140",
    ends={
        Property(name="uml_umlTrace_ReadExtentAction", type=umlTrace_uml_TracedReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadExtentAction2141", type=uml_umlTrace_ReadExtentAction, multiplicity=Multiplicity(0, 1))
    }
)
effect2142: BinaryAssociation = BinaryAssociation(
    name="effect2142",
    ends={
        Property(name="uml_TracedBehavior2143", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
guard2144: BinaryAssociation = BinaryAssociation(
    name="guard2144",
    ends={
        Property(name="uml_TracedConstraint2146", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2145", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_Dependency2124: BinaryAssociation = BinaryAssociation(
    name="originalObject_Dependency2124",
    ends={
        Property(name="uml_umlTrace_Dependency", type=umlTrace_uml_TracedDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDependency2125", type=uml_umlTrace_Dependency, multiplicity=Multiplicity(0, 1))
    }
)
expr2126: BinaryAssociation = BinaryAssociation(
    name="expr2126",
    ends={
        Property(name="uml_TracedValueSpecification2127", type=umlTrace_uml_TracedTimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeExpression", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
observation2128: BinaryAssociation = BinaryAssociation(
    name="observation2128",
    ends={
        Property(name="uml_TracedObservation2130", type=umlTrace_uml_TracedTimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeExpression2129", type=uml_TracedObservation, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2131: BinaryAssociation = BinaryAssociation(
    name="originalObject2131",
    ends={
        Property(name="uml_umlTrace_TimeExpression", type=umlTrace_uml_TracedTimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeExpression2132", type=uml_umlTrace_TimeExpression, multiplicity=Multiplicity(0, 1))
    }
)
utilizedElement2133: BinaryAssociation = BinaryAssociation(
    name="utilizedElement2133",
    ends={
        Property(name="uml_TracedPackageableElement2134", type=umlTrace_uml_TracedManifestation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedManifestation", type=uml_TracedPackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
classifier2135: BinaryAssociation = BinaryAssociation(
    name="classifier2135",
    ends={
        Property(name="uml_TracedClassifier2136", type=umlTrace_uml_TracedReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadExtentAction", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
result2137: BinaryAssociation = BinaryAssociation(
    name="result2137",
    ends={
        Property(name="uml_TracedOutputPin2139", type=umlTrace_uml_TracedReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadExtentAction2138", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
qualifier2166: BinaryAssociation = BinaryAssociation(
    name="qualifier2166",
    ends={
        Property(name="umlTrace_uml_TracedLinkEndData2167", type=uml_TracedQualifierValue, multiplicity=Multiplicity(0, 9999)),
        Property(name="uml_TracedQualifierValue2168", type=umlTrace_uml_TracedLinkEndData, multiplicity=Multiplicity(1, 1))
    }
)
value2169: BinaryAssociation = BinaryAssociation(
    name="value2169",
    ends={
        Property(name="uml_TracedInputPin2171", type=umlTrace_uml_TracedLinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkEndData2170", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_LinkEndData2172: BinaryAssociation = BinaryAssociation(
    name="originalObject_LinkEndData2172",
    ends={
        Property(name="uml_umlTrace_LinkEndData", type=umlTrace_uml_TracedLinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkEndData2173", type=uml_umlTrace_LinkEndData, multiplicity=Multiplicity(0, 1))
    }
)
nestedNode2174: BinaryAssociation = BinaryAssociation(
    name="nestedNode2174",
    ends={
        Property(name="uml_TracedNode2175", type=umlTrace_uml_TracedNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNode", type=uml_TracedNode, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedTransition2147: BinaryAssociation = BinaryAssociation(
    name="redefinedTransition2147",
    ends={
        Property(name="uml_TracedTransition2149", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2148", type=uml_TracedTransition, multiplicity=Multiplicity(0, 1))
    }
)
source2150: BinaryAssociation = BinaryAssociation(
    name="source2150",
    ends={
        Property(name="uml_TracedVertex2152", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2151", type=uml_TracedVertex, multiplicity=Multiplicity(1, 1))
    }
)
target2153: BinaryAssociation = BinaryAssociation(
    name="target2153",
    ends={
        Property(name="uml_TracedVertex2155", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2154", type=uml_TracedVertex, multiplicity=Multiplicity(1, 1))
    }
)
trigger2156: BinaryAssociation = BinaryAssociation(
    name="trigger2156",
    ends={
        Property(name="uml_TracedTrigger2158", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2157", type=uml_TracedTrigger, multiplicity=Multiplicity(0, 9999))
    }
)
container2159: BinaryAssociation = BinaryAssociation(
    name="container2159",
    ends={
        Property(name="uml_TracedRegion2161", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2160", type=uml_TracedRegion, multiplicity=Multiplicity(1, 1))
    }
)
originalObject_Transition2162: BinaryAssociation = BinaryAssociation(
    name="originalObject_Transition2162",
    ends={
        Property(name="uml_umlTrace_Transition", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2163", type=uml_umlTrace_Transition, multiplicity=Multiplicity(0, 1))
    }
)
end2164: BinaryAssociation = BinaryAssociation(
    name="end2164",
    ends={
        Property(name="uml_TracedProperty2165", type=umlTrace_uml_TracedLinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkEndData", type=uml_TracedProperty, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2192: BinaryAssociation = BinaryAssociation(
    name="originalObject2192",
    ends={
        Property(name="uml_umlTrace_ChangeEvent", type=umlTrace_uml_TracedChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedChangeEvent2193", type=uml_umlTrace_ChangeEvent, multiplicity=Multiplicity(0, 1))
    }
)
redefinedElement2194: BinaryAssociation = BinaryAssociation(
    name="redefinedElement2194",
    ends={
        Property(name="uml_TracedRedefinableElement", type=umlTrace_uml_TracedRedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRedefinableElement", type=uml_TracedRedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
mergedPackage2176: BinaryAssociation = BinaryAssociation(
    name="mergedPackage2176",
    ends={
        Property(name="uml_TracedPackage2177", type=umlTrace_uml_TracedPackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackageMerge", type=uml_TracedPackage, multiplicity=Multiplicity(1, 1))
    }
)
receivingPackage2178: BinaryAssociation = BinaryAssociation(
    name="receivingPackage2178",
    ends={
        Property(name="uml_TracedPackage2180", type=umlTrace_uml_TracedPackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackageMerge2179", type=uml_TracedPackage, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2181: BinaryAssociation = BinaryAssociation(
    name="originalObject2181",
    ends={
        Property(name="uml_umlTrace_PackageMerge", type=umlTrace_uml_TracedPackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackageMerge2182", type=uml_umlTrace_PackageMerge, multiplicity=Multiplicity(0, 1))
    }
)
selection2183: BinaryAssociation = BinaryAssociation(
    name="selection2183",
    ends={
        Property(name="uml_TracedBehavior2184", type=umlTrace_uml_TracedObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedObjectFlow", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
transformation2185: BinaryAssociation = BinaryAssociation(
    name="transformation2185",
    ends={
        Property(name="uml_TracedBehavior2187", type=umlTrace_uml_TracedObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedObjectFlow2186", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2188: BinaryAssociation = BinaryAssociation(
    name="originalObject2188",
    ends={
        Property(name="uml_umlTrace_ObjectFlow", type=umlTrace_uml_TracedObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedObjectFlow2189", type=uml_umlTrace_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
changeExpression2190: BinaryAssociation = BinaryAssociation(
    name="changeExpression2190",
    ends={
        Property(name="uml_TracedValueSpecification2191", type=umlTrace_uml_TracedChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedChangeEvent", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
annotatedElement2207: BinaryAssociation = BinaryAssociation(
    name="annotatedElement2207",
    ends={
        Property(name="uml_TracedElement2208", type=umlTrace_uml_TracedComment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComment", type=uml_TracedElement, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2209: BinaryAssociation = BinaryAssociation(
    name="originalObject2209",
    ends={
        Property(name="uml_umlTrace_Comment", type=umlTrace_uml_TracedComment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComment2210", type=uml_umlTrace_Comment, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute2211: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute2211",
    ends={
        Property(name="uml_TracedProperty2212", type=umlTrace_uml_TracedStructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredClassifier", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext2195: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext2195",
    ends={
        Property(name="uml_TracedClassifier2197", type=umlTrace_uml_TracedRedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRedefinableElement2196", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
target2198: BinaryAssociation = BinaryAssociation(
    name="target2198",
    ends={
        Property(name="uml_TracedInputPin2199", type=umlTrace_uml_TracedDestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDestroyObjectAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2200: BinaryAssociation = BinaryAssociation(
    name="originalObject2200",
    ends={
        Property(name="uml_umlTrace_DestroyObjectAction", type=umlTrace_uml_TracedDestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDestroyObjectAction2201", type=uml_umlTrace_DestroyObjectAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2202: BinaryAssociation = BinaryAssociation(
    name="originalObject2202",
    ends={
        Property(name="uml_umlTrace_ForkNode", type=umlTrace_uml_TracedForkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedForkNode", type=uml_umlTrace_ForkNode, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute2203: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute2203",
    ends={
        Property(name="uml_TracedProperty2204", type=umlTrace_uml_TracedSignal, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSignal", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2205: BinaryAssociation = BinaryAssociation(
    name="originalObject2205",
    ends={
        Property(name="uml_umlTrace_Signal", type=umlTrace_uml_TracedSignal, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSignal2206", type=uml_umlTrace_Signal, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2232: BinaryAssociation = BinaryAssociation(
    name="originalObject2232",
    ends={
        Property(name="uml_umlTrace_Reception", type=umlTrace_uml_TracedReception, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReception2233", type=uml_umlTrace_Reception, multiplicity=Multiplicity(0, 1))
    }
)
exception2234: BinaryAssociation = BinaryAssociation(
    name="exception2234",
    ends={
        Property(name="uml_TracedInputPin2235", type=umlTrace_uml_TracedRaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRaiseExceptionAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2236: BinaryAssociation = BinaryAssociation(
    name="originalObject2236",
    ends={
        Property(name="uml_umlTrace_RaiseExceptionAction", type=umlTrace_uml_TracedRaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRaiseExceptionAction2237", type=uml_umlTrace_RaiseExceptionAction, multiplicity=Multiplicity(0, 1))
    }
)
ownedConnector2213: BinaryAssociation = BinaryAssociation(
    name="ownedConnector2213",
    ends={
        Property(name="uml_TracedConnector2215", type=umlTrace_uml_TracedStructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredClassifier2214", type=uml_TracedConnector, multiplicity=Multiplicity(0, 9999))
    }
)
part2216: BinaryAssociation = BinaryAssociation(
    name="part2216",
    ends={
        Property(name="uml_TracedProperty2218", type=umlTrace_uml_TracedStructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredClassifier2217", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
role2219: BinaryAssociation = BinaryAssociation(
    name="role2219",
    ends={
        Property(name="uml_TracedConnectableElement2221", type=umlTrace_uml_TracedStructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredClassifier2220", type=uml_TracedConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2222: BinaryAssociation = BinaryAssociation(
    name="originalObject2222",
    ends={
        Property(name="uml_umlTrace_LiteralNull", type=umlTrace_uml_TracedLiteralNull, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLiteralNull", type=uml_umlTrace_LiteralNull, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput2223: BinaryAssociation = BinaryAssociation(
    name="regionAsInput2223",
    ends={
        Property(name="uml_TracedExpansionRegion2224", type=umlTrace_uml_TracedExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpansionNode", type=uml_TracedExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsOutput2225: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput2225",
    ends={
        Property(name="uml_TracedExpansionRegion2227", type=umlTrace_uml_TracedExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpansionNode2226", type=uml_TracedExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2228: BinaryAssociation = BinaryAssociation(
    name="originalObject2228",
    ends={
        Property(name="uml_umlTrace_ExpansionNode", type=umlTrace_uml_TracedExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpansionNode2229", type=uml_umlTrace_ExpansionNode, multiplicity=Multiplicity(0, 1))
    }
)
signal2230: BinaryAssociation = BinaryAssociation(
    name="signal2230",
    ends={
        Property(name="uml_TracedSignal2231", type=umlTrace_uml_TracedReception, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReception", type=uml_TracedSignal, multiplicity=Multiplicity(1, 1))
    }
)
object2255: BinaryAssociation = BinaryAssociation(
    name="object2255",
    ends={
        Property(name="umlTrace_uml_TracedClearAssociationAction2256", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TracedInputPin2257", type=umlTrace_uml_TracedClearAssociationAction, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2258: BinaryAssociation = BinaryAssociation(
    name="originalObject2258",
    ends={
        Property(name="uml_umlTrace_ClearAssociationAction", type=umlTrace_uml_TracedClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClearAssociationAction2259", type=uml_umlTrace_ClearAssociationAction, multiplicity=Multiplicity(0, 1))
    }
)
first2260: BinaryAssociation = BinaryAssociation(
    name="first2260",
    ends={
        Property(name="uml_TracedInputPin2261", type=umlTrace_uml_TracedTestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTestIdentityAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
method2238: BinaryAssociation = BinaryAssociation(
    name="method2238",
    ends={
        Property(name="uml_TracedBehavior2239", type=umlTrace_uml_TracedBehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioralFeature", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter2240: BinaryAssociation = BinaryAssociation(
    name="ownedParameter2240",
    ends={
        Property(name="uml_TracedParameter2242", type=umlTrace_uml_TracedBehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioralFeature2241", type=uml_TracedParameter, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameterSet2243: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet2243",
    ends={
        Property(name="uml_TracedParameterSet2245", type=umlTrace_uml_TracedBehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioralFeature2244", type=uml_TracedParameterSet, multiplicity=Multiplicity(0, 9999))
    }
)
raisedException2246: BinaryAssociation = BinaryAssociation(
    name="raisedException2246",
    ends={
        Property(name="uml_TracedType2248", type=umlTrace_uml_TracedBehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioralFeature2247", type=uml_TracedType, multiplicity=Multiplicity(0, 9999))
    }
)
insertAt2249: BinaryAssociation = BinaryAssociation(
    name="insertAt2249",
    ends={
        Property(name="uml_TracedInputPin2250", type=umlTrace_uml_TracedAddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAddVariableValueAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2251: BinaryAssociation = BinaryAssociation(
    name="originalObject2251",
    ends={
        Property(name="uml_umlTrace_AddVariableValueAction", type=umlTrace_uml_TracedAddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAddVariableValueAction2252", type=uml_umlTrace_AddVariableValueAction, multiplicity=Multiplicity(0, 1))
    }
)
association2253: BinaryAssociation = BinaryAssociation(
    name="association2253",
    ends={
        Property(name="uml_TracedAssociation2254", type=umlTrace_uml_TracedClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClearAssociationAction", type=uml_TracedAssociation, multiplicity=Multiplicity(1, 1))
    }
)
datatype2276: BinaryAssociation = BinaryAssociation(
    name="datatype2276",
    ends={
        Property(name="uml_TracedDataType2278", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2277", type=uml_TracedDataType, multiplicity=Multiplicity(0, 1))
    }
)
interface2279: BinaryAssociation = BinaryAssociation(
    name="interface2279",
    ends={
        Property(name="uml_TracedInterface2281", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2280", type=uml_TracedInterface, multiplicity=Multiplicity(0, 1))
    }
)
postcondition2282: BinaryAssociation = BinaryAssociation(
    name="postcondition2282",
    ends={
        Property(name="uml_TracedConstraint2284", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2283", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
precondition2285: BinaryAssociation = BinaryAssociation(
    name="precondition2285",
    ends={
        Property(name="uml_TracedConstraint2287", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2286", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
result2262: BinaryAssociation = BinaryAssociation(
    name="result2262",
    ends={
        Property(name="uml_TracedOutputPin2264", type=umlTrace_uml_TracedTestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTestIdentityAction2263", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
second2265: BinaryAssociation = BinaryAssociation(
    name="second2265",
    ends={
        Property(name="uml_TracedInputPin2267", type=umlTrace_uml_TracedTestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTestIdentityAction2266", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2268: BinaryAssociation = BinaryAssociation(
    name="originalObject2268",
    ends={
        Property(name="uml_umlTrace_TestIdentityAction", type=umlTrace_uml_TracedTestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTestIdentityAction2269", type=uml_umlTrace_TestIdentityAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2270: BinaryAssociation = BinaryAssociation(
    name="originalObject2270",
    ends={
        Property(name="uml_umlTrace_ControlFlow", type=umlTrace_uml_TracedControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedControlFlow", type=uml_umlTrace_ControlFlow, multiplicity=Multiplicity(0, 1))
    }
)
bodyCondition2271: BinaryAssociation = BinaryAssociation(
    name="bodyCondition2271",
    ends={
        Property(name="uml_TracedConstraint2272", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 1))
    }
)
class_2273: BinaryAssociation = BinaryAssociation(
    name="class_2273",
    ends={
        Property(name="uml_TracedClass2275", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2274", type=uml_TracedClass, multiplicity=Multiplicity(0, 1))
    }
)
ownedRule2306: BinaryAssociation = BinaryAssociation(
    name="ownedRule2306",
    ends={
        Property(name="uml_TracedConstraint2307", type=umlTrace_uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamespace", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
elementImport2308: BinaryAssociation = BinaryAssociation(
    name="elementImport2308",
    ends={
        Property(name="uml_TracedElementImport2310", type=umlTrace_uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamespace2309", type=uml_TracedElementImport, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedOperation2288: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation2288",
    ends={
        Property(name="uml_TracedOperation2290", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2289", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999))
    }
)
type2291: BinaryAssociation = BinaryAssociation(
    name="type2291",
    ends={
        Property(name="uml_TracedType2293", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2292", type=uml_TracedType, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2294: BinaryAssociation = BinaryAssociation(
    name="originalObject2294",
    ends={
        Property(name="uml_umlTrace_Operation", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2295", type=uml_umlTrace_Operation, multiplicity=Multiplicity(0, 1))
    }
)
end2296: BinaryAssociation = BinaryAssociation(
    name="end2296",
    ends={
        Property(name="uml_TracedConnectorEnd2297", type=umlTrace_uml_TracedConnectableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectableElement", type=uml_TracedConnectorEnd, multiplicity=Multiplicity(0, 9999))
    }
)
container2298: BinaryAssociation = BinaryAssociation(
    name="container2298",
    ends={
        Property(name="uml_TracedRegion2299", type=umlTrace_uml_TracedVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVertex", type=uml_TracedRegion, multiplicity=Multiplicity(0, 1))
    }
)
incoming2300: BinaryAssociation = BinaryAssociation(
    name="incoming2300",
    ends={
        Property(name="uml_TracedTransition2302", type=umlTrace_uml_TracedVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVertex2301", type=uml_TracedTransition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing2303: BinaryAssociation = BinaryAssociation(
    name="outgoing2303",
    ends={
        Property(name="uml_TracedTransition2305", type=umlTrace_uml_TracedVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVertex2304", type=uml_TracedTransition, multiplicity=Multiplicity(0, 9999))
    }
)
importingNamespace2325: BinaryAssociation = BinaryAssociation(
    name="importingNamespace2325",
    ends={
        Property(name="uml_TracedNamespace2327", type=umlTrace_uml_TracedPackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackageImport2326", type=uml_TracedNamespace, multiplicity=Multiplicity(1, 1))
    }
)
packageImport2311: BinaryAssociation = BinaryAssociation(
    name="packageImport2311",
    ends={
        Property(name="uml_TracedPackageImport2313", type=umlTrace_uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamespace2312", type=uml_TracedPackageImport, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember2314: BinaryAssociation = BinaryAssociation(
    name="ownedMember2314",
    ends={
        Property(name="uml_TracedNamedElement2316", type=umlTrace_uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamespace2315", type=uml_TracedNamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedMember2317: BinaryAssociation = BinaryAssociation(
    name="importedMember2317",
    ends={
        Property(name="uml_TracedPackageableElement2319", type=umlTrace_uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamespace2318", type=uml_TracedPackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
member2320: BinaryAssociation = BinaryAssociation(
    name="member2320",
    ends={
        Property(name="uml_TracedNamedElement2322", type=umlTrace_uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamespace2321", type=uml_TracedNamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2348: BinaryAssociation = BinaryAssociation(
    name="originalObject2348",
    ends={
        Property(name="uml_umlTrace_Variable", type=umlTrace_uml_TracedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVariable2349", type=uml_umlTrace_Variable, multiplicity=Multiplicity(0, 1))
    }
)
importedPackage2323: BinaryAssociation = BinaryAssociation(
    name="importedPackage2323",
    ends={
        Property(name="uml_TracedPackage2324", type=umlTrace_uml_TracedPackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackageImport", type=uml_TracedPackage, multiplicity=Multiplicity(1, 1))
    }
)
actualGate2350: BinaryAssociation = BinaryAssociation(
    name="actualGate2350",
    ends={
        Property(name="uml_TracedGate2351", type=umlTrace_uml_TracedInteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionUse", type=uml_TracedGate, multiplicity=Multiplicity(0, 9999))
    }
)
argument2352: BinaryAssociation = BinaryAssociation(
    name="argument2352",
    ends={
        Property(name="uml_TracedValueSpecification2354", type=umlTrace_uml_TracedInteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionUse2353", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
refersTo2355: BinaryAssociation = BinaryAssociation(
    name="refersTo2355",
    ends={
        Property(name="uml_TracedInteraction2357", type=umlTrace_uml_TracedInteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionUse2356", type=uml_TracedInteraction, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2328: BinaryAssociation = BinaryAssociation(
    name="originalObject2328",
    ends={
        Property(name="uml_umlTrace_PackageImport", type=umlTrace_uml_TracedPackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackageImport2329", type=uml_umlTrace_PackageImport, multiplicity=Multiplicity(0, 1))
    }
)
execution2330: BinaryAssociation = BinaryAssociation(
    name="execution2330",
    ends={
        Property(name="uml_TracedExecutionSpecification", type=umlTrace_uml_TracedExecutionOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExecutionOccurrenceSpecification", type=uml_TracedExecutionSpecification, multiplicity=Multiplicity(1, 1))
    }
)
exceptionInput2331: BinaryAssociation = BinaryAssociation(
    name="exceptionInput2331",
    ends={
        Property(name="uml_TracedObjectNode", type=umlTrace_uml_TracedExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExceptionHandler", type=uml_TracedObjectNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionType2332: BinaryAssociation = BinaryAssociation(
    name="exceptionType2332",
    ends={
        Property(name="uml_TracedClassifier2334", type=umlTrace_uml_TracedExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExceptionHandler2333", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 9999))
    }
)
handlerBody2335: BinaryAssociation = BinaryAssociation(
    name="handlerBody2335",
    ends={
        Property(name="uml_TracedExecutableNode2337", type=umlTrace_uml_TracedExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExceptionHandler2336", type=uml_TracedExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
protectedNode2338: BinaryAssociation = BinaryAssociation(
    name="protectedNode2338",
    ends={
        Property(name="uml_TracedExecutableNode2340", type=umlTrace_uml_TracedExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExceptionHandler2339", type=uml_TracedExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2341: BinaryAssociation = BinaryAssociation(
    name="originalObject2341",
    ends={
        Property(name="uml_umlTrace_ExceptionHandler", type=umlTrace_uml_TracedExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExceptionHandler2342", type=uml_umlTrace_ExceptionHandler, multiplicity=Multiplicity(0, 1))
    }
)
activityScope2343: BinaryAssociation = BinaryAssociation(
    name="activityScope2343",
    ends={
        Property(name="uml_TracedActivity2344", type=umlTrace_uml_TracedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVariable", type=uml_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
scope2345: BinaryAssociation = BinaryAssociation(
    name="scope2345",
    ends={
        Property(name="uml_TracedStructuredActivityNode2347", type=umlTrace_uml_TracedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVariable2346", type=uml_TracedStructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_Association2377: BinaryAssociation = BinaryAssociation(
    name="originalObject_Association2377",
    ends={
        Property(name="uml_umlTrace_Association", type=umlTrace_uml_TracedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAssociation2378", type=uml_umlTrace_Association, multiplicity=Multiplicity(0, 1))
    }
)
invariant2379: BinaryAssociation = BinaryAssociation(
    name="invariant2379",
    ends={
        Property(name="uml_TracedConstraint2380", type=umlTrace_uml_TracedStateInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStateInvariant", type=uml_TracedConstraint, multiplicity=Multiplicity(1, 1))
    }
)
returnValue2358: BinaryAssociation = BinaryAssociation(
    name="returnValue2358",
    ends={
        Property(name="uml_TracedValueSpecification2360", type=umlTrace_uml_TracedInteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionUse2359", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
returnValueRecipient2361: BinaryAssociation = BinaryAssociation(
    name="returnValueRecipient2361",
    ends={
        Property(name="uml_TracedProperty2363", type=umlTrace_uml_TracedInteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionUse2362", type=uml_TracedProperty, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_InteractionUse2364: BinaryAssociation = BinaryAssociation(
    name="originalObject_InteractionUse2364",
    ends={
        Property(name="uml_umlTrace_InteractionUse", type=umlTrace_uml_TracedInteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionUse2365", type=uml_umlTrace_InteractionUse, multiplicity=Multiplicity(0, 1))
    }
)
endType2366: BinaryAssociation = BinaryAssociation(
    name="endType2366",
    ends={
        Property(name="uml_TracedType2367", type=umlTrace_uml_TracedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAssociation", type=uml_TracedType, multiplicity=Multiplicity(1, 9999))
    }
)
memberEnd2368: BinaryAssociation = BinaryAssociation(
    name="memberEnd2368",
    ends={
        Property(name="uml_TracedProperty2370", type=umlTrace_uml_TracedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAssociation2369", type=uml_TracedProperty, multiplicity=Multiplicity(2, 9999))
    }
)
ownedEnd2371: BinaryAssociation = BinaryAssociation(
    name="ownedEnd2371",
    ends={
        Property(name="uml_TracedProperty2373", type=umlTrace_uml_TracedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAssociation2372", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
navigableOwnedEnd2374: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd2374",
    ends={
        Property(name="uml_TracedProperty2376", type=umlTrace_uml_TracedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAssociation2375", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
contract2393: BinaryAssociation = BinaryAssociation(
    name="contract2393",
    ends={
        Property(name="uml_TracedClassifier2394", type=umlTrace_uml_TracedSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSubstitution", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2381: BinaryAssociation = BinaryAssociation(
    name="originalObject2381",
    ends={
        Property(name="uml_umlTrace_StateInvariant", type=umlTrace_uml_TracedStateInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStateInvariant2382", type=uml_umlTrace_StateInvariant, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2383: BinaryAssociation = BinaryAssociation(
    name="originalObject2383",
    ends={
        Property(name="uml_umlTrace_LiteralReal", type=umlTrace_uml_TracedLiteralReal, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLiteralReal", type=uml_umlTrace_LiteralReal, multiplicity=Multiplicity(0, 1))
    }
)
argument2384: BinaryAssociation = BinaryAssociation(
    name="argument2384",
    ends={
        Property(name="uml_TracedInputPin2385", type=umlTrace_uml_TracedInvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInvocationAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999))
    }
)
onPort2386: BinaryAssociation = BinaryAssociation(
    name="onPort2386",
    ends={
        Property(name="uml_TracedPort2388", type=umlTrace_uml_TracedInvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInvocationAction2387", type=uml_TracedPort, multiplicity=Multiplicity(0, 1))
    }
)
removeAt2389: BinaryAssociation = BinaryAssociation(
    name="removeAt2389",
    ends={
        Property(name="uml_TracedInputPin2390", type=umlTrace_uml_TracedRemoveVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRemoveVariableValueAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
newClassifier2415: BinaryAssociation = BinaryAssociation(
    name="newClassifier2415",
    ends={
        Property(name="uml_TracedClassifier2416", type=umlTrace_uml_TracedReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReclassifyObjectAction", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2391: BinaryAssociation = BinaryAssociation(
    name="originalObject2391",
    ends={
        Property(name="uml_umlTrace_RemoveVariableValueAction", type=umlTrace_uml_TracedRemoveVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRemoveVariableValueAction2392", type=uml_umlTrace_RemoveVariableValueAction, multiplicity=Multiplicity(0, 1))
    }
)
object2417: BinaryAssociation = BinaryAssociation(
    name="object2417",
    ends={
        Property(name="uml_TracedInputPin2419", type=umlTrace_uml_TracedReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReclassifyObjectAction2418", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
oldClassifier2420: BinaryAssociation = BinaryAssociation(
    name="oldClassifier2420",
    ends={
        Property(name="uml_TracedClassifier2422", type=umlTrace_uml_TracedReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReclassifyObjectAction2421", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
substitutingClassifier2395: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier2395",
    ends={
        Property(name="uml_TracedClassifier2397", type=umlTrace_uml_TracedSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSubstitution2396", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2398: BinaryAssociation = BinaryAssociation(
    name="originalObject2398",
    ends={
        Property(name="uml_umlTrace_Gate", type=umlTrace_uml_TracedGate, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGate", type=uml_umlTrace_Gate, multiplicity=Multiplicity(0, 1))
    }
)
deployedElement2399: BinaryAssociation = BinaryAssociation(
    name="deployedElement2399",
    ends={
        Property(name="uml_TracedPackageableElement2400", type=umlTrace_uml_TracedDeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDeploymentTarget", type=uml_TracedPackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
deployment2401: BinaryAssociation = BinaryAssociation(
    name="deployment2401",
    ends={
        Property(name="uml_TracedDeployment2403", type=umlTrace_uml_TracedDeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDeploymentTarget2402", type=uml_TracedDeployment, multiplicity=Multiplicity(0, 9999))
    }
)
after2404: BinaryAssociation = BinaryAssociation(
    name="after2404",
    ends={
        Property(name="uml_TracedOccurrenceSpecification2405", type=umlTrace_uml_TracedGeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralOrdering", type=uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
before2406: BinaryAssociation = BinaryAssociation(
    name="before2406",
    ends={
        Property(name="uml_TracedOccurrenceSpecification2408", type=umlTrace_uml_TracedGeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralOrdering2407", type=uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2409: BinaryAssociation = BinaryAssociation(
    name="originalObject2409",
    ends={
        Property(name="uml_umlTrace_GeneralOrdering", type=umlTrace_uml_TracedGeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralOrdering2410", type=uml_umlTrace_GeneralOrdering, multiplicity=Multiplicity(0, 1))
    }
)
behavior2411: BinaryAssociation = BinaryAssociation(
    name="behavior2411",
    ends={
        Property(name="uml_TracedBehavior2412", type=umlTrace_uml_TracedCallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallBehaviorAction", type=uml_TracedBehavior, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2413: BinaryAssociation = BinaryAssociation(
    name="originalObject2413",
    ends={
        Property(name="uml_umlTrace_CallBehaviorAction", type=umlTrace_uml_TracedCallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallBehaviorAction2414", type=uml_umlTrace_CallBehaviorAction, multiplicity=Multiplicity(0, 1))
    }
)
partition2442: BinaryAssociation = BinaryAssociation(
    name="partition2442",
    ends={
        Property(name="uml_TracedActivityPartition2444", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2443", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNode2445: BinaryAssociation = BinaryAssociation(
    name="structuredNode2445",
    ends={
        Property(name="uml_TracedStructuredActivityNode2447", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2446", type=uml_TracedStructuredActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
entry2448: BinaryAssociation = BinaryAssociation(
    name="entry2448",
    ends={
        Property(name="uml_TracedPseudostate2449", type=umlTrace_uml_TracedConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectionPointReference", type=uml_TracedPseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2423: BinaryAssociation = BinaryAssociation(
    name="originalObject2423",
    ends={
        Property(name="uml_umlTrace_ReclassifyObjectAction", type=umlTrace_uml_TracedReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReclassifyObjectAction2424", type=uml_umlTrace_ReclassifyObjectAction, multiplicity=Multiplicity(0, 1))
    }
)
ownedGroup2425: BinaryAssociation = BinaryAssociation(
    name="ownedGroup2425",
    ends={
        Property(name="uml_TracedActivityGroup2426", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity", type=uml_TracedActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
edge2427: BinaryAssociation = BinaryAssociation(
    name="edge2427",
    ends={
        Property(name="uml_TracedActivityEdge2429", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2428", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
node2430: BinaryAssociation = BinaryAssociation(
    name="node2430",
    ends={
        Property(name="uml_TracedActivityNode2432", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2431", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
variable2433: BinaryAssociation = BinaryAssociation(
    name="variable2433",
    ends={
        Property(name="uml_TracedVariable2435", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2434", type=uml_TracedVariable, multiplicity=Multiplicity(0, 9999))
    }
)
group2436: BinaryAssociation = BinaryAssociation(
    name="group2436",
    ends={
        Property(name="uml_TracedActivityGroup2438", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2437", type=uml_TracedActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
ownedNode2439: BinaryAssociation = BinaryAssociation(
    name="ownedNode2439",
    ends={
        Property(name="uml_TracedActivityNode2441", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2440", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
insertAt2468: BinaryAssociation = BinaryAssociation(
    name="insertAt2468",
    ends={
        Property(name="uml_TracedInputPin2469", type=umlTrace_uml_TracedLinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkEndCreationData", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
parameterSubstitution2470: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution2470",
    ends={
        Property(name="uml_TracedTemplateParameterSubstitution2471", type=umlTrace_uml_TracedTemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateBinding", type=uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999))
    }
)
signature2472: BinaryAssociation = BinaryAssociation(
    name="signature2472",
    ends={
        Property(name="uml_TracedTemplateSignature2474", type=umlTrace_uml_TracedTemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateBinding2473", type=uml_TracedTemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
exit2450: BinaryAssociation = BinaryAssociation(
    name="exit2450",
    ends={
        Property(name="uml_TracedPseudostate2452", type=umlTrace_uml_TracedConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectionPointReference2451", type=uml_TracedPseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
state2453: BinaryAssociation = BinaryAssociation(
    name="state2453",
    ends={
        Property(name="uml_TracedState2455", type=umlTrace_uml_TracedConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectionPointReference2454", type=uml_TracedState, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2456: BinaryAssociation = BinaryAssociation(
    name="originalObject2456",
    ends={
        Property(name="uml_umlTrace_ConnectionPointReference", type=umlTrace_uml_TracedConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectionPointReference2457", type=uml_umlTrace_ConnectionPointReference, multiplicity=Multiplicity(0, 1))
    }
)
action2458: BinaryAssociation = BinaryAssociation(
    name="action2458",
    ends={
        Property(name="uml_TracedAction2459", type=umlTrace_uml_TracedActionExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActionExecutionSpecification", type=uml_TracedAction, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2460: BinaryAssociation = BinaryAssociation(
    name="originalObject2460",
    ends={
        Property(name="uml_umlTrace_ActionExecutionSpecification", type=umlTrace_uml_TracedActionExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActionExecutionSpecification2461", type=uml_umlTrace_ActionExecutionSpecification, multiplicity=Multiplicity(0, 1))
    }
)
result2462: BinaryAssociation = BinaryAssociation(
    name="result2462",
    ends={
        Property(name="uml_TracedOutputPin2463", type=umlTrace_uml_TracedReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadSelfAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2464: BinaryAssociation = BinaryAssociation(
    name="originalObject2464",
    ends={
        Property(name="uml_umlTrace_ReadSelfAction", type=umlTrace_uml_TracedReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadSelfAction2465", type=uml_umlTrace_ReadSelfAction, multiplicity=Multiplicity(0, 1))
    }
)
returnInformation2466: BinaryAssociation = BinaryAssociation(
    name="returnInformation2466",
    ends={
        Property(name="uml_TracedOutputPin2467", type=umlTrace_uml_TracedAcceptCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAcceptCallAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2493: BinaryAssociation = BinaryAssociation(
    name="originalObject2493",
    ends={
        Property(name="uml_umlTrace_Actor", type=umlTrace_uml_TracedActor, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActor", type=uml_umlTrace_Actor, multiplicity=Multiplicity(0, 1))
    }
)
behavior2494: BinaryAssociation = BinaryAssociation(
    name="behavior2494",
    ends={
        Property(name="uml_TracedBehavior2495", type=umlTrace_uml_TracedBehaviorExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehaviorExecutionSpecification", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2496: BinaryAssociation = BinaryAssociation(
    name="originalObject2496",
    ends={
        Property(name="uml_umlTrace_BehaviorExecutionSpecification", type=umlTrace_uml_TracedBehaviorExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehaviorExecutionSpecification2497", type=uml_umlTrace_BehaviorExecutionSpecification, multiplicity=Multiplicity(0, 1))
    }
)
boundElement2475: BinaryAssociation = BinaryAssociation(
    name="boundElement2475",
    ends={
        Property(name="uml_TracedTemplateableElement2477", type=umlTrace_uml_TracedTemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateBinding2476", type=uml_TracedTemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2478: BinaryAssociation = BinaryAssociation(
    name="originalObject2478",
    ends={
        Property(name="uml_umlTrace_TemplateBinding", type=umlTrace_uml_TracedTemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateBinding2479", type=uml_umlTrace_TemplateBinding, multiplicity=Multiplicity(0, 1))
    }
)
result2480: BinaryAssociation = BinaryAssociation(
    name="result2480",
    ends={
        Property(name="uml_TracedOutputPin2481", type=umlTrace_uml_TracedClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClearStructuralFeatureAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2482: BinaryAssociation = BinaryAssociation(
    name="originalObject2482",
    ends={
        Property(name="uml_umlTrace_ClearStructuralFeatureAction", type=umlTrace_uml_TracedClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClearStructuralFeatureAction2483", type=uml_umlTrace_ClearStructuralFeatureAction, multiplicity=Multiplicity(0, 1))
    }
)
behavior2484: BinaryAssociation = BinaryAssociation(
    name="behavior2484",
    ends={
        Property(name="uml_TracedBehavior2485", type=umlTrace_uml_TracedOpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOpaqueExpression", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
result2486: BinaryAssociation = BinaryAssociation(
    name="result2486",
    ends={
        Property(name="uml_TracedParameter2488", type=umlTrace_uml_TracedOpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOpaqueExpression2487", type=uml_TracedParameter, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2489: BinaryAssociation = BinaryAssociation(
    name="originalObject2489",
    ends={
        Property(name="uml_umlTrace_OpaqueExpression", type=umlTrace_uml_TracedOpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOpaqueExpression2490", type=uml_umlTrace_OpaqueExpression, multiplicity=Multiplicity(0, 1))
    }
)
deployment2491: BinaryAssociation = BinaryAssociation(
    name="deployment2491",
    ends={
        Property(name="uml_TracedDeployment2492", type=umlTrace_uml_TracedDeploymentSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDeploymentSpecification", type=uml_TracedDeployment, multiplicity=Multiplicity(0, 1))
    }
)
handler2498: BinaryAssociation = BinaryAssociation(
    name="handler2498",
    ends={
        Property(name="uml_TracedExceptionHandler2499", type=umlTrace_uml_TracedExecutableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExecutableNode", type=uml_TracedExceptionHandler, multiplicity=Multiplicity(0, 9999))
    }
)
object2500: BinaryAssociation = BinaryAssociation(
    name="object2500",
    ends={
        Property(name="uml_TracedInputPin2501", type=umlTrace_uml_TracedUnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUnmarshallAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
result2502: BinaryAssociation = BinaryAssociation(
    name="result2502",
    ends={
        Property(name="uml_TracedOutputPin2504", type=umlTrace_uml_TracedUnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUnmarshallAction2503", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 9999))
    }
)
unmarshallType2505: BinaryAssociation = BinaryAssociation(
    name="unmarshallType2505",
    ends={
        Property(name="uml_TracedClassifier2507", type=umlTrace_uml_TracedUnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUnmarshallAction2506", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2508: BinaryAssociation = BinaryAssociation(
    name="originalObject2508",
    ends={
        Property(name="uml_umlTrace_UnmarshallAction", type=umlTrace_uml_TracedUnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUnmarshallAction2509", type=uml_umlTrace_UnmarshallAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_CentralBufferNode2510: BinaryAssociation = BinaryAssociation(
    name="originalObject_CentralBufferNode2510",
    ends={
        Property(name="uml_umlTrace_CentralBufferNode", type=umlTrace_uml_TracedCentralBufferNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCentralBufferNode", type=uml_umlTrace_CentralBufferNode, multiplicity=Multiplicity(0, 1))
    }
)
eAnnotations2511: BinaryAssociation = BinaryAssociation(
    name="eAnnotations2511",
    ends={
        Property(name="ecore_umlTrace_EAnnotation", type=umlTrace_ecore_TracedEModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_ecore_TracedEModelElement", type=ecore_umlTrace_EAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_umlTrace_Kernel_TracedEvaluation_TracedSemanticVisitor = Generalization(general=TracedSemanticVisitor, specific=umlTrace_Kernel_TracedEvaluation)
gen_umlTrace_Kernel_TracedBooleanValue_TracedPrimitiveValue = Generalization(general=TracedPrimitiveValue, specific=umlTrace_Kernel_TracedBooleanValue)
gen_umlTrace_Kernel_TracedLiteralBooleanEvaluation_TracedLiteralEvaluation = Generalization(general=TracedLiteralEvaluation, specific=umlTrace_Kernel_TracedLiteralBooleanEvaluation)
gen_umlTrace_Kernel_TracedStructuredValue_TracedValue = Generalization(general=TracedValue, specific=umlTrace_Kernel_TracedStructuredValue)
gen_umlTrace_Kernel_TracedObject_TracedExtensionalValue = Generalization(general=TracedExtensionalValue, specific=umlTrace_Kernel_TracedObject)
gen_umlTrace_Kernel_TracedReference_TracedStructuredValue = Generalization(general=TracedStructuredValue, specific=umlTrace_Kernel_TracedReference)
gen_umlTrace_Kernel_TracedIntegerValue_TracedPrimitiveValue = Generalization(general=TracedPrimitiveValue, specific=umlTrace_Kernel_TracedIntegerValue)
gen_umlTrace_Kernel_TracedLiteralEvaluation_TracedEvaluation = Generalization(general=TracedEvaluation, specific=umlTrace_Kernel_TracedLiteralEvaluation)
gen_umlTrace_Kernel_TracedValue_TracedSemanticVisitor = Generalization(general=TracedSemanticVisitor, specific=umlTrace_Kernel_TracedValue)
gen_umlTrace_Kernel_TracedPrimitiveValue_TracedValue = Generalization(general=TracedValue, specific=umlTrace_Kernel_TracedPrimitiveValue)
gen_umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution_TracedExecution = Generalization(general=TracedExecution, specific=umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution)
gen_umlTrace_BasicBehaviors_TracedExecution_TracedObject = Generalization(general=TracedObject, specific=umlTrace_BasicBehaviors_TracedExecution)
gen_umlTrace_Kernel_TracedCompoundValue_TracedStructuredValue = Generalization(general=TracedStructuredValue, specific=umlTrace_Kernel_TracedCompoundValue)
gen_umlTrace_Kernel_TracedExtensionalValue_TracedCompoundValue = Generalization(general=TracedCompoundValue, specific=umlTrace_Kernel_TracedExtensionalValue)
gen_umlTrace_Kernel_TracedLiteralIntegerEvaluation_TracedLiteralEvaluation = Generalization(general=TracedLiteralEvaluation, specific=umlTrace_Kernel_TracedLiteralIntegerEvaluation)
gen_umlTrace_IntermediateActivities_TracedMergeNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedMergeNodeActivation)
gen_umlTrace_IntermediateActivities_TracedControlToken_TracedToken = Generalization(general=TracedToken, specific=umlTrace_IntermediateActivities_TracedControlToken)
gen_umlTrace_IntermediateActivities_TracedObjectToken_TracedToken = Generalization(general=TracedToken, specific=umlTrace_IntermediateActivities_TracedObjectToken)
gen_umlTrace_IntermediateActivities_TracedDecisionNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedDecisionNodeActivation)
gen_umlTrace_IntermediateActivities_TracedForkedToken_TracedToken = Generalization(general=TracedToken, specific=umlTrace_IntermediateActivities_TracedForkedToken)
gen_umlTrace_IntermediateActivities_TracedJoinNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedJoinNodeActivation)
gen_umlTrace_IntermediateActivities_TracedInitialNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedInitialNodeActivation)
gen_umlTrace_IntermediateActivities_TracedObjectNodeActivation_TracedActivityNodeActivation = Generalization(general=TracedActivityNodeActivation, specific=umlTrace_IntermediateActivities_TracedObjectNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityNodeActivation_TracedSemanticVisitor = Generalization(general=TracedSemanticVisitor, specific=umlTrace_IntermediateActivities_TracedActivityNodeActivation)
gen_umlTrace_IntermediateActivities_TracedForkNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedForkNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation_TracedObjectNodeActivation = Generalization(general=TracedObjectNodeActivation, specific=umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation)
gen_umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation)
gen_umlTrace_IntermediateActions_TracedValueSpecificationActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_IntermediateActions_TracedValueSpecificationActionActivation)
gen_umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation = Generalization(general=TracedStructuralFeatureActionActivation, specific=umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation)
gen_umlTrace_IntermediateActivities_TracedControlNodeActivation_TracedActivityNodeActivation = Generalization(general=TracedActivityNodeActivation, specific=umlTrace_IntermediateActivities_TracedControlNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityExecution_TracedExecution = Generalization(general=TracedExecution, specific=umlTrace_IntermediateActivities_TracedActivityExecution)
gen_umlTrace_BasicActions_TracedCallActionActivation_TracedInvocationActionActivation = Generalization(general=TracedInvocationActionActivation, specific=umlTrace_BasicActions_TracedCallActionActivation)
gen_umlTrace_BasicActions_TracedPinActivation_TracedObjectNodeActivation = Generalization(general=TracedObjectNodeActivation, specific=umlTrace_BasicActions_TracedPinActivation)
gen_umlTrace_BasicActions_TracedInputPinActivation_TracedPinActivation = Generalization(general=TracedPinActivation, specific=umlTrace_BasicActions_TracedInputPinActivation)
gen_umlTrace_BasicActions_TracedInvocationActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_BasicActions_TracedInvocationActionActivation)
gen_umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_TracedOpaqueBehaviorExecution = Generalization(general=TracedOpaqueBehaviorExecution, specific=umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution)
gen_umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation_TracedWriteStructuralFeatureActionActivation = Generalization(general=TracedWriteStructuralFeatureActionActivation, specific=umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation)
gen_umlTrace_IntermediateActions_TracedCreateObjectActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_IntermediateActions_TracedCreateObjectActionActivation)
gen_umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation = Generalization(general=TracedStructuralFeatureActionActivation, specific=umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation)
gen_umlTrace_BasicActions_TracedActionActivation_TracedActivityNodeActivation = Generalization(general=TracedActivityNodeActivation, specific=umlTrace_BasicActions_TracedActionActivation)
gen_umlTrace_BasicActions_TracedOutputPinActivation_TracedPinActivation = Generalization(general=TracedPinActivation, specific=umlTrace_BasicActions_TracedOutputPinActivation)
gen_umlTrace_BasicActions_TracedCallBehaviorActionActivation_TracedCallActionActivation = Generalization(general=TracedCallActionActivation, specific=umlTrace_BasicActions_TracedCallBehaviorActionActivation)
gen_umlTrace_BasicActions_TracedOpaqueActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_BasicActions_TracedOpaqueActionActivation)
gen_umlTrace_uml_TracedOpaqueAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedOpaqueAction)
gen_umlTrace_uml_TracedDataType_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedDataType)
gen_umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_TracedOpaqueBehaviorExecution = Generalization(general=TracedOpaqueBehaviorExecution, specific=umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution)
gen_umlTrace_uml_TracedCommunicationPath_TracedAssociation = Generalization(general=TracedAssociation, specific=umlTrace_uml_TracedCommunicationPath)
gen_umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_TracedOpaqueBehaviorExecution = Generalization(general=TracedOpaqueBehaviorExecution, specific=umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution)
gen_umlTrace_uml_TracedLinkAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedLinkAction)
gen_umlTrace_uml_TracedStructuralFeature_uml_TracedFeature = Generalization(general=uml_TracedFeature, specific=umlTrace_uml_TracedStructuralFeature)
gen_umlTrace_uml_TracedStructuralFeature_uml_TracedTypedElement = Generalization(general=uml_TracedTypedElement, specific=umlTrace_uml_TracedStructuralFeature)
gen_umlTrace_uml_TracedStructuralFeature_uml_TracedMultiplicityElement = Generalization(general=uml_TracedMultiplicityElement, specific=umlTrace_uml_TracedStructuralFeature)
gen_umlTrace_uml_TracedConnector_TracedFeature = Generalization(general=TracedFeature, specific=umlTrace_uml_TracedConnector)
gen_umlTrace_uml_TracedContinuation_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedContinuation)
gen_umlTrace_uml_TracedProperty_uml_TracedStructuralFeature = Generalization(general=uml_TracedStructuralFeature, specific=umlTrace_uml_TracedProperty)
gen_umlTrace_uml_TracedProperty_uml_TracedConnectableElement = Generalization(general=uml_TracedConnectableElement, specific=umlTrace_uml_TracedProperty)
gen_umlTrace_uml_TracedProperty_uml_TracedDeploymentTarget = Generalization(general=uml_TracedDeploymentTarget, specific=umlTrace_uml_TracedProperty)
gen_umlTrace_uml_TracedTimeConstraint_TracedIntervalConstraint = Generalization(general=TracedIntervalConstraint, specific=umlTrace_uml_TracedTimeConstraint)
gen_umlTrace_uml_TracedInterfaceRealization_TracedRealization = Generalization(general=TracedRealization, specific=umlTrace_uml_TracedInterfaceRealization)
gen_umlTrace_uml_TracedObjectNode_uml_TracedActivityNode = Generalization(general=uml_TracedActivityNode, specific=umlTrace_uml_TracedObjectNode)
gen_umlTrace_uml_TracedObjectNode_uml_TracedTypedElement = Generalization(general=uml_TracedTypedElement, specific=umlTrace_uml_TracedObjectNode)
gen_umlTrace_uml_TracedRemoveStructuralFeatureValueAction_TracedWriteStructuralFeatureAction = Generalization(general=TracedWriteStructuralFeatureAction, specific=umlTrace_uml_TracedRemoveStructuralFeatureValueAction)
gen_umlTrace_uml_TracedSendSignalAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedSendSignalAction)
gen_umlTrace_uml_TracedOpaqueBehavior_TracedBehavior = Generalization(general=TracedBehavior, specific=umlTrace_uml_TracedOpaqueBehavior)
gen_umlTrace_uml_TracedArtifact_uml_TracedClassifier = Generalization(general=uml_TracedClassifier, specific=umlTrace_uml_TracedArtifact)
gen_umlTrace_uml_TracedArtifact_uml_TracedDeployedArtifact = Generalization(general=uml_TracedDeployedArtifact, specific=umlTrace_uml_TracedArtifact)
gen_umlTrace_uml_TracedEnumerationLiteral_TracedInstanceSpecification = Generalization(general=TracedInstanceSpecification, specific=umlTrace_uml_TracedEnumerationLiteral)
gen_umlTrace_uml_TracedAddStructuralFeatureValueAction_TracedWriteStructuralFeatureAction = Generalization(general=TracedWriteStructuralFeatureAction, specific=umlTrace_uml_TracedAddStructuralFeatureValueAction)
gen_umlTrace_uml_TracedReadLinkAction_TracedLinkAction = Generalization(general=TracedLinkAction, specific=umlTrace_uml_TracedReadLinkAction)
gen_umlTrace_uml_TracedActivityFinalNode_TracedFinalNode = Generalization(general=TracedFinalNode, specific=umlTrace_uml_TracedActivityFinalNode)
gen_umlTrace_uml_TracedDurationObservation_TracedObservation = Generalization(general=TracedObservation, specific=umlTrace_uml_TracedDurationObservation)
gen_umlTrace_uml_TracedAcceptEventAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedAcceptEventAction)
gen_umlTrace_uml_TracedDataStoreNode_TracedCentralBufferNode = Generalization(general=TracedCentralBufferNode, specific=umlTrace_uml_TracedDataStoreNode)
gen_umlTrace_uml_TracedFlowFinalNode_TracedFinalNode = Generalization(general=TracedFinalNode, specific=umlTrace_uml_TracedFlowFinalNode)
gen_umlTrace_uml_TracedInteractionFragment_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedInteractionFragment)
gen_umlTrace_uml_TracedClassifier_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedClassifier)
gen_umlTrace_uml_TracedClassifier_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedClassifier)
gen_umlTrace_uml_TracedClassifier_uml_TracedType = Generalization(general=uml_TracedType, specific=umlTrace_uml_TracedClassifier)
gen_umlTrace_uml_TracedClassifier_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedClassifier)
gen_umlTrace_uml_TracedExpression_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedExpression)
gen_umlTrace_uml_TracedConsiderIgnoreFragment_TracedCombinedFragment = Generalization(general=TracedCombinedFragment, specific=umlTrace_uml_TracedConsiderIgnoreFragment)
gen_umlTrace_uml_TracedInformationItem_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedInformationItem)
gen_umlTrace_uml_TracedMessageEnd_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedMessageEnd)
gen_umlTrace_uml_TracedTemplateSignature_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateSignature)
gen_umlTrace_uml_TracedCollaboration_uml_TracedStructuredClassifier = Generalization(general=uml_TracedStructuredClassifier, specific=umlTrace_uml_TracedCollaboration)
gen_umlTrace_uml_TracedCollaboration_uml_TracedBehavioredClassifier = Generalization(general=uml_TracedBehavioredClassifier, specific=umlTrace_uml_TracedCollaboration)
gen_umlTrace_uml_TracedPort_TracedProperty = Generalization(general=TracedProperty, specific=umlTrace_uml_TracedPort)
gen_umlTrace_uml_TracedTimeInterval_TracedInterval = Generalization(general=TracedInterval, specific=umlTrace_uml_TracedTimeInterval)
gen_umlTrace_uml_TracedAction_TracedExecutableNode = Generalization(general=TracedExecutableNode, specific=umlTrace_uml_TracedAction)
gen_umlTrace_uml_TracedBroadcastSignalAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedBroadcastSignalAction)
gen_umlTrace_uml_TracedDeployment_TracedDependency = Generalization(general=TracedDependency, specific=umlTrace_uml_TracedDeployment)
gen_umlTrace_uml_TracedDirectedRelationship_TracedRelationship = Generalization(general=TracedRelationship, specific=umlTrace_uml_TracedDirectedRelationship)
gen_umlTrace_uml_TracedTimeEvent_TracedEvent = Generalization(general=TracedEvent, specific=umlTrace_uml_TracedTimeEvent)
gen_umlTrace_uml_TracedPackageableElement_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedPackageableElement)
gen_umlTrace_uml_TracedPackageableElement_uml_TracedParameterableElement = Generalization(general=uml_TracedParameterableElement, specific=umlTrace_uml_TracedPackageableElement)
gen_umlTrace_uml_TracedType_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedType)
gen_umlTrace_uml_TracedExtension_TracedAssociation = Generalization(general=TracedAssociation, specific=umlTrace_uml_TracedExtension)
gen_umlTrace_uml_TracedProtocolTransition_TracedTransition = Generalization(general=TracedTransition, specific=umlTrace_uml_TracedProtocolTransition)
gen_umlTrace_uml_TracedPackage_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedPackage)
gen_umlTrace_uml_TracedPackage_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedPackage)
gen_umlTrace_uml_TracedPackage_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedPackage)
gen_umlTrace_uml_TracedConstraint_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedConstraint)
gen_umlTrace_uml_TracedMultiplicityElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedMultiplicityElement)
gen_umlTrace_uml_TracedLiteralSpecification_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedLiteralSpecification)
gen_umlTrace_uml_TracedBehavioredClassifier_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedBehavioredClassifier)
gen_umlTrace_uml_TracedStructuralFeatureAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedStructuralFeatureAction)
gen_umlTrace_uml_TracedInputPin_TracedPin = Generalization(general=TracedPin, specific=umlTrace_uml_TracedInputPin)
gen_umlTrace_uml_TracedSequenceNode_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedSequenceNode)
gen_umlTrace_uml_TracedFeature_TracedRedefinableElement = Generalization(general=TracedRedefinableElement, specific=umlTrace_uml_TracedFeature)
gen_umlTrace_uml_TracedInteractionConstraint_TracedConstraint = Generalization(general=TracedConstraint, specific=umlTrace_uml_TracedInteractionConstraint)
gen_umlTrace_uml_TracedGeneralizationSet_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedGeneralizationSet)
gen_umlTrace_uml_TracedReduceAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReduceAction)
gen_umlTrace_uml_TracedComponentRealization_TracedRealization = Generalization(general=TracedRealization, specific=umlTrace_uml_TracedComponentRealization)
gen_umlTrace_uml_TracedAssociationClass_uml_TracedClass = Generalization(general=uml_TracedClass, specific=umlTrace_uml_TracedAssociationClass)
gen_umlTrace_uml_TracedAssociationClass_uml_TracedAssociation = Generalization(general=uml_TracedAssociation, specific=umlTrace_uml_TracedAssociationClass)
gen_umlTrace_uml_TracedSlot_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedSlot)
gen_umlTrace_uml_TracedWriteStructuralFeatureAction_TracedStructuralFeatureAction = Generalization(general=TracedStructuralFeatureAction, specific=umlTrace_uml_TracedWriteStructuralFeatureAction)
gen_umlTrace_uml_TracedElement_TracedEModelElement = Generalization(general=TracedEModelElement, specific=umlTrace_uml_TracedElement)
gen_umlTrace_uml_TracedJoinNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedJoinNode)
gen_umlTrace_uml_TracedStartObjectBehaviorAction_TracedCallAction = Generalization(general=TracedCallAction, specific=umlTrace_uml_TracedStartObjectBehaviorAction)
gen_umlTrace_uml_TracedElementImport_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedElementImport)
gen_umlTrace_uml_TracedSignalEvent_TracedMessageEvent = Generalization(general=TracedMessageEvent, specific=umlTrace_uml_TracedSignalEvent)
gen_umlTrace_uml_TracedExtensionPoint_TracedRedefinableElement = Generalization(general=TracedRedefinableElement, specific=umlTrace_uml_TracedExtensionPoint)
gen_umlTrace_uml_TracedStringExpression_uml_TracedExpression = Generalization(general=uml_TracedExpression, specific=umlTrace_uml_TracedStringExpression)
gen_umlTrace_uml_TracedStringExpression_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedStringExpression)
gen_umlTrace_uml_TracedDeployedArtifact_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedDeployedArtifact)
gen_umlTrace_uml_TracedStereotype_TracedClass = Generalization(general=TracedClass, specific=umlTrace_uml_TracedStereotype)
gen_umlTrace_uml_TracedInterface_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedInterface)
gen_umlTrace_uml_TracedCreateObjectAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedCreateObjectAction)
gen_umlTrace_uml_TracedExecutionEnvironment_TracedNode = Generalization(general=TracedNode, specific=umlTrace_uml_TracedExecutionEnvironment)
gen_umlTrace_uml_TracedOccurrenceSpecification_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedOccurrenceSpecification)
gen_umlTrace_uml_TracedConditionalNode_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedConditionalNode)
gen_umlTrace_uml_TracedReadLinkObjectEndAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadLinkObjectEndAction)
gen_umlTrace_uml_TracedAnyReceiveEvent_TracedMessageEvent = Generalization(general=TracedMessageEvent, specific=umlTrace_uml_TracedAnyReceiveEvent)
gen_umlTrace_uml_TracedNamedElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedNamedElement)
gen_umlTrace_uml_TracedComponent_TracedClass = Generalization(general=TracedClass, specific=umlTrace_uml_TracedComponent)
gen_umlTrace_uml_TracedLiteralString_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralString)
gen_umlTrace_uml_TracedRealization_TracedAbstraction = Generalization(general=TracedAbstraction, specific=umlTrace_uml_TracedRealization)
gen_umlTrace_uml_TracedStartClassifierBehaviorAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedStartClassifierBehaviorAction)
gen_umlTrace_uml_TracedExtensionEnd_TracedProperty = Generalization(general=TracedProperty, specific=umlTrace_uml_TracedExtensionEnd)
gen_umlTrace_uml_TracedStateMachine_TracedBehavior = Generalization(general=TracedBehavior, specific=umlTrace_uml_TracedStateMachine)
gen_umlTrace_uml_TracedValueSpecification_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedValueSpecification)
gen_umlTrace_uml_TracedValueSpecification_uml_TracedTypedElement = Generalization(general=uml_TracedTypedElement, specific=umlTrace_uml_TracedValueSpecification)
gen_umlTrace_uml_TracedInteraction_uml_TracedBehavior = Generalization(general=uml_TracedBehavior, specific=umlTrace_uml_TracedInteraction)
gen_umlTrace_uml_TracedInteraction_uml_TracedInteractionFragment = Generalization(general=uml_TracedInteractionFragment, specific=umlTrace_uml_TracedInteraction)
gen_umlTrace_uml_TracedLifeline_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedLifeline)
gen_umlTrace_uml_TracedMessageEvent_TracedEvent = Generalization(general=TracedEvent, specific=umlTrace_uml_TracedMessageEvent)
gen_umlTrace_uml_TracedCallEvent_TracedMessageEvent = Generalization(general=TracedMessageEvent, specific=umlTrace_uml_TracedCallEvent)
gen_umlTrace_uml_TracedConnectableElementTemplateParameter_TracedTemplateParameter = Generalization(general=TracedTemplateParameter, specific=umlTrace_uml_TracedConnectableElementTemplateParameter)
gen_umlTrace_uml_TracedRelationship_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedRelationship)
gen_umlTrace_uml_TracedSendObjectAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedSendObjectAction)
gen_umlTrace_uml_TracedExpansionRegion_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedExpansionRegion)
gen_umlTrace_uml_TracedWriteVariableAction_TracedVariableAction = Generalization(general=TracedVariableAction, specific=umlTrace_uml_TracedWriteVariableAction)
gen_umlTrace_uml_TracedExecutionSpecification_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedExecutionSpecification)
gen_umlTrace_uml_TracedTimeObservation_TracedObservation = Generalization(general=TracedObservation, specific=umlTrace_uml_TracedTimeObservation)
gen_umlTrace_uml_TracedCreateLinkObjectAction_TracedCreateLinkAction = Generalization(general=TracedCreateLinkAction, specific=umlTrace_uml_TracedCreateLinkObjectAction)
gen_umlTrace_uml_TracedPrimitiveType_TracedDataType = Generalization(general=TracedDataType, specific=umlTrace_uml_TracedPrimitiveType)
gen_umlTrace_uml_TracedProtocolConformance_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedProtocolConformance)
gen_umlTrace_uml_TracedLoopNode_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedLoopNode)
gen_umlTrace_uml_TracedEnumeration_TracedDataType = Generalization(general=TracedDataType, specific=umlTrace_uml_TracedEnumeration)
gen_umlTrace_uml_TracedCollaborationUse_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedCollaborationUse)
gen_umlTrace_uml_TracedActivityPartition_TracedActivityGroup = Generalization(general=TracedActivityGroup, specific=umlTrace_uml_TracedActivityPartition)
gen_umlTrace_uml_TracedActivityNode_ActivityContent = Generalization(general=ActivityContent, specific=umlTrace_uml_TracedActivityNode)
gen_umlTrace_uml_TracedVariableAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedVariableAction)
gen_umlTrace_uml_TracedLinkEndDestructionData_TracedLinkEndData = Generalization(general=TracedLinkEndData, specific=umlTrace_uml_TracedLinkEndDestructionData)
gen_umlTrace_uml_TracedDurationInterval_TracedInterval = Generalization(general=TracedInterval, specific=umlTrace_uml_TracedDurationInterval)
gen_umlTrace_uml_TracedInclude_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedInclude)
gen_umlTrace_uml_TracedInclude_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedInclude)
gen_umlTrace_uml_TracedActivityNode_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedActivityNode)
gen_umlTrace_uml_TracedDestructionOccurrenceSpecification_TracedMessageOccurrenceSpecification = Generalization(general=TracedMessageOccurrenceSpecification, specific=umlTrace_uml_TracedDestructionOccurrenceSpecification)
gen_umlTrace_uml_TracedState_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedState)
gen_umlTrace_uml_TracedState_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedState)
gen_umlTrace_uml_TracedState_uml_TracedVertex = Generalization(general=uml_TracedVertex, specific=umlTrace_uml_TracedState)
gen_umlTrace_uml_TracedBehavior_TracedClass = Generalization(general=TracedClass, specific=umlTrace_uml_TracedBehavior)
gen_umlTrace_uml_TracedCallAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedCallAction)
gen_umlTrace_uml_TracedTemplateableElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateableElement)
gen_umlTrace_uml_TracedParameterSet_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedParameterSet)
gen_umlTrace_uml_TracedClassifierTemplateParameter_TracedTemplateParameter = Generalization(general=TracedTemplateParameter, specific=umlTrace_uml_TracedClassifierTemplateParameter)
gen_umlTrace_uml_TracedActivityParameterNode_TracedObjectNode = Generalization(general=TracedObjectNode, specific=umlTrace_uml_TracedActivityParameterNode)
gen_umlTrace_uml_TracedUsage_TracedDependency = Generalization(general=TracedDependency, specific=umlTrace_uml_TracedUsage)
gen_umlTrace_uml_TracedLiteralUnlimitedNatural_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralUnlimitedNatural)
gen_umlTrace_uml_TracedDuration_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedDuration)
gen_umlTrace_uml_TracedClass_uml_TracedEncapsulatedClassifier = Generalization(general=uml_TracedEncapsulatedClassifier, specific=umlTrace_uml_TracedClass)
gen_umlTrace_uml_TracedClass_uml_TracedBehavioredClassifier = Generalization(general=uml_TracedBehavioredClassifier, specific=umlTrace_uml_TracedClass)
gen_umlTrace_uml_TracedReadStructuralFeatureAction_TracedStructuralFeatureAction = Generalization(general=TracedStructuralFeatureAction, specific=umlTrace_uml_TracedReadStructuralFeatureAction)
gen_umlTrace_uml_TracedMergeNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedMergeNode)
gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedAction = Generalization(general=uml_TracedAction, specific=umlTrace_uml_TracedStructuredActivityNode)
gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedStructuredActivityNode)
gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedActivityGroup = Generalization(general=uml_TracedActivityGroup, specific=umlTrace_uml_TracedStructuredActivityNode)
gen_umlTrace_uml_TracedAbstraction_TracedDependency = Generalization(general=TracedDependency, specific=umlTrace_uml_TracedAbstraction)
gen_umlTrace_uml_TracedPartDecomposition_TracedInteractionUse = Generalization(general=TracedInteractionUse, specific=umlTrace_uml_TracedPartDecomposition)
gen_umlTrace_uml_TracedTypedElement_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedTypedElement)
gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedRedefinableTemplateSignature)
gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedTemplateSignature = Generalization(general=uml_TracedTemplateSignature, specific=umlTrace_uml_TracedRedefinableTemplateSignature)
gen_umlTrace_uml_TracedCreateLinkAction_TracedWriteLinkAction = Generalization(general=TracedWriteLinkAction, specific=umlTrace_uml_TracedCreateLinkAction)
gen_umlTrace_uml_TracedGeneralization_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedGeneralization)
gen_umlTrace_uml_TracedExtend_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedExtend)
gen_umlTrace_uml_TracedExtend_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedExtend)
gen_umlTrace_uml_TracedOperationTemplateParameter_TracedTemplateParameter = Generalization(general=TracedTemplateParameter, specific=umlTrace_uml_TracedOperationTemplateParameter)
gen_umlTrace_uml_TracedReadLinkObjectEndQualifierAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadLinkObjectEndQualifierAction)
gen_umlTrace_uml_TracedTemplateParameterSubstitution_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateParameterSubstitution)
gen_umlTrace_uml_TracedReadVariableAction_TracedVariableAction = Generalization(general=TracedVariableAction, specific=umlTrace_uml_TracedReadVariableAction)
gen_umlTrace_uml_TracedMessage_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedMessage)
gen_umlTrace_uml_TracedProfileApplication_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedProfileApplication)
gen_umlTrace_uml_TracedLiteralBoolean_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralBoolean)
gen_umlTrace_uml_TracedQualifierValue_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedQualifierValue)
gen_umlTrace_uml_TracedInitialNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedInitialNode)
gen_umlTrace_uml_TracedLiteralInteger_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralInteger)
gen_umlTrace_uml_TracedClearVariableAction_TracedVariableAction = Generalization(general=TracedVariableAction, specific=umlTrace_uml_TracedClearVariableAction)
gen_umlTrace_uml_TracedConnectorEnd_TracedMultiplicityElement = Generalization(general=TracedMultiplicityElement, specific=umlTrace_uml_TracedConnectorEnd)
gen_umlTrace_uml_TracedParameterableElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedParameterableElement)
gen_umlTrace_uml_TracedTemplateParameter_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateParameter)
gen_umlTrace_uml_TracedActionInputPin_TracedInputPin = Generalization(general=TracedInputPin, specific=umlTrace_uml_TracedActionInputPin)
gen_umlTrace_uml_TracedTrigger_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedTrigger)
gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedOccurrenceSpecification = Generalization(general=uml_TracedOccurrenceSpecification, specific=umlTrace_uml_TracedMessageOccurrenceSpecification)
gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedMessageEnd = Generalization(general=uml_TracedMessageEnd, specific=umlTrace_uml_TracedMessageOccurrenceSpecification)
gen_umlTrace_uml_TracedDurationConstraint_TracedIntervalConstraint = Generalization(general=TracedIntervalConstraint, specific=umlTrace_uml_TracedDurationConstraint)
gen_umlTrace_uml_TracedImage_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedImage)
gen_umlTrace_uml_TracedEncapsulatedClassifier_TracedStructuredClassifier = Generalization(general=TracedStructuredClassifier, specific=umlTrace_uml_TracedEncapsulatedClassifier)
gen_umlTrace_uml_TracedParameter_uml_TracedConnectableElement = Generalization(general=uml_TracedConnectableElement, specific=umlTrace_uml_TracedParameter)
gen_umlTrace_uml_TracedParameter_uml_TracedMultiplicityElement = Generalization(general=uml_TracedMultiplicityElement, specific=umlTrace_uml_TracedParameter)
gen_umlTrace_uml_TracedIntervalConstraint_TracedConstraint = Generalization(general=TracedConstraint, specific=umlTrace_uml_TracedIntervalConstraint)
gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeploymentTarget = Generalization(general=uml_TracedDeploymentTarget, specific=umlTrace_uml_TracedInstanceSpecification)
gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedInstanceSpecification)
gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeployedArtifact = Generalization(general=uml_TracedDeployedArtifact, specific=umlTrace_uml_TracedInstanceSpecification)
gen_umlTrace_uml_TracedCallOperationAction_TracedCallAction = Generalization(general=TracedCallAction, specific=umlTrace_uml_TracedCallOperationAction)
gen_umlTrace_uml_TracedProfile_TracedPackage = Generalization(general=TracedPackage, specific=umlTrace_uml_TracedProfile)
gen_umlTrace_uml_TracedInterval_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedInterval)
gen_umlTrace_uml_TracedProtocolStateMachine_TracedStateMachine = Generalization(general=TracedStateMachine, specific=umlTrace_uml_TracedProtocolStateMachine)
gen_umlTrace_uml_TracedOutputPin_TracedPin = Generalization(general=TracedPin, specific=umlTrace_uml_TracedOutputPin)
gen_umlTrace_uml_TracedValuePin_TracedInputPin = Generalization(general=TracedInputPin, specific=umlTrace_uml_TracedValuePin)
gen_umlTrace_uml_TracedReadIsClassifiedObjectAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadIsClassifiedObjectAction)
gen_umlTrace_uml_TracedRegion_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedRegion)
gen_umlTrace_uml_TracedRegion_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedRegion)
gen_umlTrace_uml_TracedDecisionNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedDecisionNode)
gen_umlTrace_uml_TracedValueSpecificationAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedValueSpecificationAction)
gen_umlTrace_uml_TracedDestroyLinkAction_TracedWriteLinkAction = Generalization(general=TracedWriteLinkAction, specific=umlTrace_uml_TracedDestroyLinkAction)
gen_umlTrace_uml_TracedFinalState_TracedState = Generalization(general=TracedState, specific=umlTrace_uml_TracedFinalState)
gen_umlTrace_uml_TracedActivityGroup_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedActivityGroup)
gen_umlTrace_uml_TracedInterruptibleActivityRegion_TracedActivityGroup = Generalization(general=TracedActivityGroup, specific=umlTrace_uml_TracedInterruptibleActivityRegion)
gen_umlTrace_uml_TracedActivityGroup_ActivityContent = Generalization(general=ActivityContent, specific=umlTrace_uml_TracedActivityGroup)
gen_umlTrace_uml_TracedActivityEdge_TracedRedefinableElement = Generalization(general=TracedRedefinableElement, specific=umlTrace_uml_TracedActivityEdge)
gen_umlTrace_uml_TracedInteractionOperand_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedInteractionOperand)
gen_umlTrace_uml_TracedInteractionOperand_uml_TracedInteractionFragment = Generalization(general=uml_TracedInteractionFragment, specific=umlTrace_uml_TracedInteractionOperand)
gen_umlTrace_uml_TracedInformationFlow_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedInformationFlow)
gen_umlTrace_uml_TracedInformationFlow_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedInformationFlow)
gen_umlTrace_uml_TracedControlNode_TracedActivityNode = Generalization(general=TracedActivityNode, specific=umlTrace_uml_TracedControlNode)
gen_umlTrace_uml_TracedUseCase_TracedBehavioredClassifier = Generalization(general=TracedBehavioredClassifier, specific=umlTrace_uml_TracedUseCase)
gen_umlTrace_uml_TracedPseudostate_TracedVertex = Generalization(general=TracedVertex, specific=umlTrace_uml_TracedPseudostate)
gen_umlTrace_uml_TracedCombinedFragment_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedCombinedFragment)
gen_umlTrace_uml_TracedReplyAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReplyAction)
gen_umlTrace_uml_TracedDependency_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedDependency)
gen_umlTrace_uml_TracedDependency_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedDependency)
gen_umlTrace_uml_TracedWriteLinkAction_TracedLinkAction = Generalization(general=TracedLinkAction, specific=umlTrace_uml_TracedWriteLinkAction)
gen_umlTrace_uml_TracedClause_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedClause)
gen_umlTrace_uml_TracedInstanceValue_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedInstanceValue)
gen_umlTrace_uml_TracedTransition_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedTransition)
gen_umlTrace_uml_TracedTransition_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedTransition)
gen_umlTrace_uml_TracedTimeExpression_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedTimeExpression)
gen_umlTrace_uml_TracedManifestation_TracedAbstraction = Generalization(general=TracedAbstraction, specific=umlTrace_uml_TracedManifestation)
gen_umlTrace_uml_TracedReadExtentAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadExtentAction)
gen_umlTrace_uml_TracedNode_uml_TracedClass = Generalization(general=uml_TracedClass, specific=umlTrace_uml_TracedNode)
gen_umlTrace_uml_TracedNode_uml_TracedDeploymentTarget = Generalization(general=uml_TracedDeploymentTarget, specific=umlTrace_uml_TracedNode)
gen_umlTrace_uml_TracedLinkEndData_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedLinkEndData)
gen_umlTrace_uml_TracedRedefinableElement_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedRedefinableElement)
gen_umlTrace_uml_TracedPackageMerge_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedPackageMerge)
gen_umlTrace_uml_TracedModel_TracedPackage = Generalization(general=TracedPackage, specific=umlTrace_uml_TracedModel)
gen_umlTrace_uml_TracedObjectFlow_TracedActivityEdge = Generalization(general=TracedActivityEdge, specific=umlTrace_uml_TracedObjectFlow)
gen_umlTrace_uml_TracedEvent_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedEvent)
gen_umlTrace_uml_TracedChangeEvent_TracedEvent = Generalization(general=TracedEvent, specific=umlTrace_uml_TracedChangeEvent)
gen_umlTrace_uml_TracedStructuredClassifier_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedStructuredClassifier)
gen_umlTrace_uml_TracedDestroyObjectAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedDestroyObjectAction)
gen_umlTrace_uml_TracedForkNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedForkNode)
gen_umlTrace_uml_TracedFinalNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedFinalNode)
gen_umlTrace_uml_TracedSignal_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedSignal)
gen_umlTrace_uml_TracedComment_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedComment)
gen_umlTrace_uml_TracedRaiseExceptionAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedRaiseExceptionAction)
gen_umlTrace_uml_TracedLiteralNull_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralNull)
gen_umlTrace_uml_TracedExpansionNode_TracedObjectNode = Generalization(general=TracedObjectNode, specific=umlTrace_uml_TracedExpansionNode)
gen_umlTrace_uml_TracedReception_TracedBehavioralFeature = Generalization(general=TracedBehavioralFeature, specific=umlTrace_uml_TracedReception)
gen_umlTrace_uml_TracedPin_uml_TracedObjectNode = Generalization(general=uml_TracedObjectNode, specific=umlTrace_uml_TracedPin)
gen_umlTrace_uml_TracedPin_uml_TracedMultiplicityElement = Generalization(general=uml_TracedMultiplicityElement, specific=umlTrace_uml_TracedPin)
gen_umlTrace_uml_TracedTestIdentityAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedTestIdentityAction)
gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedBehavioralFeature)
gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedFeature = Generalization(general=uml_TracedFeature, specific=umlTrace_uml_TracedBehavioralFeature)
gen_umlTrace_uml_TracedAddVariableValueAction_TracedWriteVariableAction = Generalization(general=TracedWriteVariableAction, specific=umlTrace_uml_TracedAddVariableValueAction)
gen_umlTrace_uml_TracedClearAssociationAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedClearAssociationAction)
gen_umlTrace_uml_TracedControlFlow_TracedActivityEdge = Generalization(general=TracedActivityEdge, specific=umlTrace_uml_TracedControlFlow)
gen_umlTrace_uml_TracedOperation_uml_TracedBehavioralFeature = Generalization(general=uml_TracedBehavioralFeature, specific=umlTrace_uml_TracedOperation)
gen_umlTrace_uml_TracedOperation_uml_TracedParameterableElement = Generalization(general=uml_TracedParameterableElement, specific=umlTrace_uml_TracedOperation)
gen_umlTrace_uml_TracedOperation_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedOperation)
gen_umlTrace_uml_TracedObservation_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedObservation)
gen_umlTrace_uml_TracedNamespace_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedNamespace)
gen_umlTrace_uml_TracedConnectableElement_uml_TracedTypedElement = Generalization(general=uml_TracedTypedElement, specific=umlTrace_uml_TracedConnectableElement)
gen_umlTrace_uml_TracedConnectableElement_uml_TracedParameterableElement = Generalization(general=uml_TracedParameterableElement, specific=umlTrace_uml_TracedConnectableElement)
gen_umlTrace_uml_TracedVertex_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedVertex)
gen_umlTrace_uml_TracedPackageImport_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedPackageImport)
gen_umlTrace_uml_TracedInteractionUse_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedInteractionUse)
gen_umlTrace_uml_TracedExecutionOccurrenceSpecification_TracedOccurrenceSpecification = Generalization(general=TracedOccurrenceSpecification, specific=umlTrace_uml_TracedExecutionOccurrenceSpecification)
gen_umlTrace_uml_TracedExceptionHandler_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedExceptionHandler)
gen_umlTrace_uml_TracedVariable_uml_TracedConnectableElement = Generalization(general=uml_TracedConnectableElement, specific=umlTrace_uml_TracedVariable)
gen_umlTrace_uml_TracedVariable_uml_TracedMultiplicityElement = Generalization(general=uml_TracedMultiplicityElement, specific=umlTrace_uml_TracedVariable)
gen_umlTrace_uml_TracedStateInvariant_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedStateInvariant)
gen_umlTrace_uml_TracedAssociation_uml_TracedClassifier = Generalization(general=uml_TracedClassifier, specific=umlTrace_uml_TracedAssociation)
gen_umlTrace_uml_TracedAssociation_uml_TracedRelationship = Generalization(general=uml_TracedRelationship, specific=umlTrace_uml_TracedAssociation)
gen_umlTrace_uml_TracedDevice_TracedNode = Generalization(general=TracedNode, specific=umlTrace_uml_TracedDevice)
gen_umlTrace_uml_TracedSubstitution_TracedRealization = Generalization(general=TracedRealization, specific=umlTrace_uml_TracedSubstitution)
gen_umlTrace_uml_TracedLiteralReal_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralReal)
gen_umlTrace_uml_TracedInvocationAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedInvocationAction)
gen_umlTrace_uml_TracedRemoveVariableValueAction_TracedWriteVariableAction = Generalization(general=TracedWriteVariableAction, specific=umlTrace_uml_TracedRemoveVariableValueAction)
gen_umlTrace_uml_TracedGate_TracedMessageEnd = Generalization(general=TracedMessageEnd, specific=umlTrace_uml_TracedGate)
gen_umlTrace_uml_TracedDeploymentTarget_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedDeploymentTarget)
gen_umlTrace_uml_TracedGeneralOrdering_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedGeneralOrdering)
gen_umlTrace_uml_TracedCallBehaviorAction_TracedCallAction = Generalization(general=TracedCallAction, specific=umlTrace_uml_TracedCallBehaviorAction)
gen_umlTrace_uml_TracedReclassifyObjectAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReclassifyObjectAction)
gen_umlTrace_uml_TracedConnectionPointReference_TracedVertex = Generalization(general=TracedVertex, specific=umlTrace_uml_TracedConnectionPointReference)
gen_umlTrace_uml_TracedActivity_TracedBehavior = Generalization(general=TracedBehavior, specific=umlTrace_uml_TracedActivity)
gen_umlTrace_uml_TracedLinkEndCreationData_TracedLinkEndData = Generalization(general=TracedLinkEndData, specific=umlTrace_uml_TracedLinkEndCreationData)
gen_umlTrace_uml_TracedTemplateBinding_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedTemplateBinding)
gen_umlTrace_uml_TracedActionExecutionSpecification_TracedExecutionSpecification = Generalization(general=TracedExecutionSpecification, specific=umlTrace_uml_TracedActionExecutionSpecification)
gen_umlTrace_uml_TracedReadSelfAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadSelfAction)
gen_umlTrace_uml_TracedAcceptCallAction_TracedAcceptEventAction = Generalization(general=TracedAcceptEventAction, specific=umlTrace_uml_TracedAcceptCallAction)
gen_umlTrace_uml_TracedActor_TracedBehavioredClassifier = Generalization(general=TracedBehavioredClassifier, specific=umlTrace_uml_TracedActor)
gen_umlTrace_uml_TracedBehaviorExecutionSpecification_TracedExecutionSpecification = Generalization(general=TracedExecutionSpecification, specific=umlTrace_uml_TracedBehaviorExecutionSpecification)
gen_umlTrace_uml_TracedExecutableNode_TracedActivityNode = Generalization(general=TracedActivityNode, specific=umlTrace_uml_TracedExecutableNode)
gen_umlTrace_uml_TracedClearStructuralFeatureAction_TracedStructuralFeatureAction = Generalization(general=TracedStructuralFeatureAction, specific=umlTrace_uml_TracedClearStructuralFeatureAction)
gen_umlTrace_uml_TracedOpaqueExpression_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedOpaqueExpression)
gen_umlTrace_uml_TracedFunctionBehavior_TracedOpaqueBehavior = Generalization(general=TracedOpaqueBehavior, specific=umlTrace_uml_TracedFunctionBehavior)
gen_umlTrace_uml_TracedDeploymentSpecification_TracedArtifact = Generalization(general=TracedArtifact, specific=umlTrace_uml_TracedDeploymentSpecification)
gen_umlTrace_uml_TracedUnmarshallAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedUnmarshallAction)
gen_umlTrace_uml_TracedCentralBufferNode_TracedObjectNode = Generalization(general=TracedObjectNode, specific=umlTrace_uml_TracedCentralBufferNode)

# Domain Model
domain_model = DomainModel(
    name="umlTrace",
    types={umlTrace_Trace, umlTrace_State, Steps, TracedObjects, Locus_factory_Value, Locus_extensionalValues_Value, Locus_executor_Value, ObjectNodeActivation_offeredTokenCount_Value, SemanticVisitor_runtimeModelElement_Value, SmallStep, BigStep, Object_types_Value, Reference_referent_Value, IntegerValue_value_IntegerValue_Value, ForkedToken_remainingOffersCount_Value, ForkedToken_baseToken_Value, ForkedToken_baseTokenIsWithdrawn_Value, ExecutionFactory_builtInTypes_Value, ExecutionFactory_primitiveBehaviorPrototypes_Value, ExecutionFactory_locus_ExecutionFactory_Value, ActivityNodeActivationGroup_activityExecution_Value, ActivityNodeActivationGroup_edgeInstances_Value, Executor_locus_Executor_Value, PrimitiveValue_type_Value, ParameterValue_values_ParameterValue_Value, ParameterValue_parameter_ParameterValue_Value, ActionActivation_pinActivations_Value, ActionActivation_firing_Value, Execution_parameterValues_Value, Execution_context_Value, Element_semanticVisitor_Value, ActivityNodeActivationGroup_nodeActivations_Value, FeatureValue_feature_Value, FeatureValue_position_Value, PinActivation_actionActivation_Value, Evaluation_specification_Evaluation_Value, Evaluation_locus_Evaluation_Value, BooleanValue_value_BooleanValue_Value, ObjectToken_value_Value, CallActionActivation_callExecutions_Value, CompoundValue_featureValues_Value, Token_holder_Value, Offer_offeredTokens_Value, FeatureValue_values_FeatureValue_Value, ActivityNodeActivation_node_ActivityNodeActivation_Value, ActivityNodeActivation_running_Value, ActivityNodeActivation_isRunning_Value, PinActivation_count_temp_Value, ActivityEdgeInstance_group_ActivityEdgeInstance_Value, ActivityEdgeInstance_offers_Value, ActivityEdgeInstance_target_Value, ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, ActivityEdgeInstance_source_Value, InputParameterValues_name_Value, InputParameterValues_parameterValues_Value, ActivityNodeActivation_heldTokens_Value, umlTrace_Values_Object_types_Value, uml_TracedClass, Kernel_TracedObject, Values_umlTrace_State, ActivityNodeActivation_outgoingEdges_Value, ActivityNodeActivation_incomingEdges_Value, ActivityNodeActivation_group_ActivityNodeActivation_Value, ExtensionalValue_locus_ExtensionalValue_Value, ActivityExecution_activationGroup_Value, ExecutionEnvironment_locus_ExecutionEnvironment_Value, umlTrace_Steps_SmallStep, Steps_umlTrace_State, umlTrace_Steps_Steps, umlTrace_Steps_BigStep, umlTrace_Values_ForkedToken_baseToken_Value, IntermediateActivities_TracedToken, umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value, umlTrace_Values_Reference_referent_Value, Kernel_TracedReference, umlTrace_Values_IntegerValue_value_IntegerValue_Value, Kernel_TracedIntegerValue, umlTrace_Values_ForkedToken_remainingOffersCount_Value, IntermediateActivities_TracedForkedToken, umlTrace_Values_Locus_factory_Value, umlTrace_Values_Locus_extensionalValues_Value, Kernel_TracedExtensionalValue, umlTrace_Values_ExecutionFactory_builtInTypes_Value, uml_TracedPrimitiveType, Loci_TracedExecutionFactory, umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value, BasicBehaviors_TracedOpaqueBehaviorExecution, umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value, Loci_TracedLocus, uml_TracedElement, Loci_TracedSemanticVisitor, umlTrace_Values_ParameterValue_values_ParameterValue_Value, umlTrace_Values_Locus_executor_Value, Loci_TracedExecutor, umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value, IntermediateActivities_TracedObjectNodeActivation, umlTrace_Values_ActionActivation_firing_Value, umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, umlTrace_Values_Execution_parameterValues_Value, Kernel_TracedValue, BasicBehaviors_TracedParameterValue, umlTrace_Values_ParameterValue_parameter_ParameterValue_Value, uml_TracedParameter, umlTrace_Values_ActionActivation_pinActivations_Value, BasicActions_TracedPinActivation, BasicActions_TracedActionActivation, umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value, IntermediateActivities_TracedActivityNodeActivation, IntermediateActivities_TracedActivityNodeActivationGroup, BasicBehaviors_TracedExecution, umlTrace_Values_Execution_context_Value, umlTrace_Values_Element_semanticVisitor_Value, umlTrace_Values_PrimitiveValue_type_Value, Kernel_TracedPrimitiveValue, umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value, IntermediateActivities_TracedActivityExecution, umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value, IntermediateActivities_TracedActivityEdgeInstance, umlTrace_Values_Executor_locus_Executor_Value, umlTrace_Values_ObjectToken_value_Value, IntermediateActivities_TracedObjectToken, umlTrace_Values_Evaluation_specification_Evaluation_Value, uml_TracedValueSpecification, Kernel_TracedEvaluation, umlTrace_Values_Evaluation_locus_Evaluation_Value, umlTrace_Values_BooleanValue_value_BooleanValue_Value, Kernel_TracedBooleanValue, umlTrace_Values_Offer_offeredTokens_Value, IntermediateActivities_TracedOffer, umlTrace_Values_CallActionActivation_callExecutions_Value, BasicActions_TracedCallActionActivation, umlTrace_Values_CompoundValue_featureValues_Value, Kernel_TracedFeatureValue, Kernel_TracedCompoundValue, umlTrace_Values_Token_holder_Value, umlTrace_Values_PinActivation_actionActivation_Value, umlTrace_Values_FeatureValue_values_FeatureValue_Value, umlTrace_Values_FeatureValue_feature_Value, uml_TracedStructuralFeature, umlTrace_Values_FeatureValue_position_Value, umlTrace_Values_ActivityEdgeInstance_offers_Value, umlTrace_Values_PinActivation_count_temp_Value, umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value, umlTrace_Values_ActivityEdgeInstance_source_Value, umlTrace_Values_ActivityEdgeInstance_target_Value, umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, uml_TracedActivityEdge, umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value, uml_TracedActivityNode, umlTrace_Values_ActivityNodeActivation_running_Value, umlTrace_Values_InputParameterValues_name_Value, Input_TracedInputParameterValues, umlTrace_Values_InputParameterValues_parameterValues_Value, umlTrace_Values_ActivityNodeActivation_heldTokens_Value, umlTrace_Values_ActivityNodeActivation_incomingEdges_Value, umlTrace_Values_ActivityNodeActivation_isRunning_Value, umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value, umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value, Loci_TracedExecutionEnvironment, umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value, umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value, umlTrace_Values_ActivityExecution_activationGroup_Value, uml_TracedOpaqueBehavior, uml_TracedArtifact, umlTrace_Traced_TracedObjects, uml_TracedConnector, uml_TracedOpaqueAction, uml_TracedDataType, uml_TracedCommunicationPath, uml_TracedProperty, uml_TracedContinuation, uml_TracedRemoveStructuralFeatureValueAction, uml_TracedSendSignalAction, uml_TracedExpression, uml_TracedConsiderIgnoreFragment, uml_TracedDataStoreNode, uml_TracedFlowFinalNode, uml_TracedInformationItem, IntermediateActivities_TracedJoinNodeActivation, uml_TracedTimeConstraint, uml_TracedInterfaceRealization, uml_TracedActivityFinalNode, uml_TracedDurationObservation, IntermediateActivities_TracedInitialNodeActivation, uml_TracedAcceptEventAction, uml_TracedEnumerationLiteral, uml_TracedAddStructuralFeatureValueAction, uml_TracedReadLinkAction, uml_TracedProtocolTransition, IntermediateActivities_TracedActivityFinalNodeActivation, uml_TracedPackage, uml_TracedCollaboration, uml_TracedTemplateSignature, uml_TracedBroadcastSignalAction, uml_TracedDeployment, uml_TracedPort, uml_TracedTimeInterval, uml_TracedExtension, uml_TracedTimeEvent, uml_TracedSlot, uml_TracedSignalEvent, uml_TracedExtensionPoint, uml_TracedJoinNode, uml_TracedConstraint, uml_TracedGeneralizationSet, uml_TracedReduceAction, uml_TracedInputPin, uml_TracedSequenceNode, uml_TracedInteractionConstraint, uml_TracedComponentRealization, uml_TracedAssociationClass, IntermediateActions_TracedValueSpecificationActionActivation, uml_TracedStringExpression, IntermediateActions_TracedReadStructuralFeatureActionActivation, BasicActions_TracedOutputPinActivation, uml_TracedStartObjectBehaviorAction, uml_TracedElementImport, uml_TracedCreateObjectAction, uml_TracedExecutionEnvironment, uml_TracedOccurrenceSpecification, uml_TracedStateMachine, IntermediateActivities_TracedMergeNodeActivation, uml_TracedInteraction, uml_TracedLiteralString, uml_TracedStereotype, uml_TracedInterface, uml_TracedConditionalNode, uml_TracedReadLinkObjectEndAction, uml_TracedAnyReceiveEvent, uml_TracedComponent, uml_TracedExtensionEnd, uml_TracedTimeObservation, IntermediateActivities_TracedControlToken, uml_TracedCreateLinkObjectAction, uml_TracedRealization, uml_TracedStartClassifierBehaviorAction, uml_TracedCallEvent, uml_TracedConnectableElementTemplateParameter, uml_TracedSendObjectAction, uml_TracedLifeline, uml_TracedEnumeration, uml_TracedCollaborationUse, uml_TracedActivityPartition, uml_TracedExpansionRegion, uml_TracedLoopNode, uml_TracedProtocolConformance, BasicActions_TracedCallBehaviorActionActivation, IntermediateActions_TracedAddStructuralFeatureValueActionActivation, uml_TracedClassifierTemplateParameter, uml_TracedLinkEndDestructionData, uml_TracedDurationInterval, uml_TracedInclude, uml_TracedDestructionOccurrenceSpecification, uml_TracedState, uml_TracedLiteralUnlimitedNatural, uml_TracedStructuredActivityNode, uml_TracedAbstraction, uml_TracedActivityParameterNode, IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution, uml_TracedParameterSet, uml_TracedDuration, uml_TracedUsage, uml_TracedCreateLinkAction, uml_TracedGeneralization, uml_TracedPartDecomposition, BasicActions_TracedOpaqueActionActivation, Kernel_TracedLiteralBooleanEvaluation, uml_TracedReadStructuralFeatureAction, uml_TracedMergeNode, uml_TracedRedefinableTemplateSignature, uml_TracedMessage, uml_TracedLiteralBoolean, uml_TracedQualifierValue, uml_TracedOperationTemplateParameter, uml_TracedReadLinkObjectEndQualifierAction, uml_TracedTemplateParameterSubstitution, uml_TracedExtend, uml_TracedReadVariableAction, IntermediateActivities_TracedDecisionNodeActivation, uml_TracedProfileApplication, uml_TracedInitialNode, uml_TracedLiteralInteger, uml_TracedClearVariableAction, uml_TracedActionInputPin, uml_TracedTemplateParameter, uml_TracedConnectorEnd, uml_TracedMessageOccurrenceSpecification, uml_TracedDurationConstraint, uml_TracedImage, uml_TracedIntervalConstraint, uml_TracedTrigger, uml_TracedCallOperationAction, uml_TracedProfile, uml_TracedInterval, IntermediateActivities_TracedForkNodeActivation, uml_TracedProtocolStateMachine, uml_TracedOutputPin, uml_TracedInstanceSpecification, uml_TracedValuePin, IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution, uml_TracedReadIsClassifiedObjectAction, uml_TracedInterruptibleActivityRegion, uml_TracedDestroyLinkAction, IntermediateActivities_TracedActivityParameterNodeActivation, uml_TracedDecisionNode, uml_TracedValueSpecificationAction, uml_TracedRegion, uml_TracedPseudostate, uml_TracedUseCase, uml_TracedFinalState, IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution, uml_TracedInteractionOperand, uml_TracedInformationFlow, uml_TracedDependency, uml_TracedTimeExpression, uml_TracedReplyAction, IntermediateActions_TracedCreateObjectActionActivation, uml_TracedCombinedFragment, uml_TracedClause, uml_TracedInstanceValue, uml_TracedTransition, uml_TracedLinkEndData, uml_TracedManifestation, uml_TracedReadExtentAction, BasicActions_TracedInputPinActivation, uml_TracedObjectFlow, uml_TracedChangeEvent, uml_TracedDestroyObjectAction, uml_TracedNode, uml_TracedPackageMerge, uml_TracedModel, uml_TracedForkNode, uml_TracedReception, uml_TracedRaiseExceptionAction, uml_TracedSignal, uml_TracedComment, uml_TracedLiteralNull, uml_TracedExpansionNode, uml_TracedControlFlow, uml_TracedOperation, uml_TracedAddVariableValueAction, uml_TracedClearAssociationAction, uml_TracedTestIdentityAction, uml_TracedExceptionHandler, uml_TracedPackageImport, uml_TracedExecutionOccurrenceSpecification, uml_TracedLiteralReal, uml_TracedRemoveVariableValueAction, uml_TracedVariable, uml_TracedInteractionUse, uml_TracedAssociation, uml_TracedStateInvariant, uml_TracedGeneralOrdering, uml_TracedCallBehaviorAction, uml_TracedReclassifyObjectAction, uml_TracedDevice, uml_TracedSubstitution, uml_TracedGate, uml_TracedReadSelfAction, uml_TracedAcceptCallAction, uml_TracedActivity, uml_TracedConnectionPointReference, uml_TracedActionExecutionSpecification, uml_TracedLinkEndCreationData, uml_TracedTemplateBinding, uml_TracedOpaqueExpression, uml_TracedFunctionBehavior, uml_TracedClearStructuralFeatureAction, Kernel_TracedLiteralIntegerEvaluation, uml_TracedUnmarshallAction, uml_TracedCentralBufferNode, umlTrace_Kernel_TracedObject, TracedExtensionalValue, uml_TracedDeploymentSpecification, uml_TracedActor, uml_TracedBehaviorExecutionSpecification, umlTrace_Kernel_TracedEvaluation, umlTrace_Kernel_TracedBooleanValue, umlTrace_Kernel_TracedLiteralBooleanEvaluation, TracedLiteralEvaluation, umlTrace_Kernel_TracedStructuredValue, umlTrace_Kernel_TracedReference, TracedStructuredValue, umlTrace_Kernel_TracedIntegerValue, TracedPrimitiveValue, umlTrace_Kernel_TracedLiteralEvaluation, TracedEvaluation, umlTrace_Kernel_TracedValue, TracedSemanticVisitor, umlTrace_Kernel_TracedPrimitiveValue, TracedValue, umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution, TracedExecution, umlTrace_BasicBehaviors_TracedParameterValue, umlTrace_BasicBehaviors_TracedExecution, TracedObject, umlTrace_Kernel_TracedCompoundValue, umlTrace_Kernel_TracedFeatureValue, umlTrace_Kernel_TracedExtensionalValue, TracedCompoundValue, umlTrace_Kernel_TracedLiteralIntegerEvaluation, umlTrace_IntermediateActivities_TracedMergeNodeActivation, umlTrace_IntermediateActivities_TracedControlToken, umlTrace_IntermediateActivities_TracedObjectToken, umlTrace_IntermediateActivities_TracedDecisionNodeActivation, umlTrace_IntermediateActivities_TracedForkedToken, TracedToken, umlTrace_IntermediateActivities_TracedJoinNodeActivation, TracedControlNodeActivation, umlTrace_IntermediateActivities_TracedInitialNodeActivation, umlTrace_IntermediateActivities_TracedObjectNodeActivation, TracedActivityNodeActivation, umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation, umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup, umlTrace_IntermediateActivities_TracedActivityNodeActivation, umlTrace_IntermediateActivities_TracedForkNodeActivation, umlTrace_IntermediateActivities_TracedToken, umlTrace_IntermediateActivities_TracedOffer, umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation, TracedObjectNodeActivation, umlTrace_IntermediateActivities_TracedActivityEdgeInstance, umlTrace_Loci_TracedSemanticVisitor, umlTrace_Loci_TracedExecutor, umlTrace_Loci_TracedExecutionEnvironment, umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation, TracedActionActivation, umlTrace_IntermediateActions_TracedValueSpecificationActionActivation, umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation, TracedStructuralFeatureActionActivation, umlTrace_IntermediateActivities_TracedControlNodeActivation, umlTrace_IntermediateActivities_TracedActivityExecution, umlTrace_Loci_TracedExecutionFactory, umlTrace_Loci_TracedLocus, umlTrace_BasicActions_TracedCallActionActivation, TracedInvocationActionActivation, umlTrace_BasicActions_TracedPinActivation, umlTrace_BasicActions_TracedInputPinActivation, umlTrace_BasicActions_TracedInvocationActionActivation, umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution, TracedOpaqueBehaviorExecution, umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation, TracedWriteStructuralFeatureActionActivation, umlTrace_IntermediateActions_TracedCreateObjectActionActivation, umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation, umlTrace_BasicActions_TracedActionActivation, umlTrace_BasicActions_TracedOutputPinActivation, TracedPinActivation, umlTrace_BasicActions_TracedCallBehaviorActionActivation, TracedCallActionActivation, umlTrace_BasicActions_TracedOpaqueActionActivation, umlTrace_uml_TracedOpaqueAction, TracedAction, uml_umlTrace_OpaqueAction, umlTrace_uml_TracedDataType, TracedClassifier, uml_umlTrace_DataType, umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution, umlTrace_uml_TracedCommunicationPath, TracedAssociation, umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution, umlTrace_uml_TracedLinkAction, umlTrace_Input_TracedInputParameterValues, umlTrace_uml_TracedStructuralFeature, uml_TracedFeature, uml_TracedTypedElement, uml_TracedMultiplicityElement, umlTrace_uml_TracedConnector, TracedFeature, uml_TracedBehavior, uml_umlTrace_Connector, uml_umlTrace_Property, umlTrace_uml_TracedContinuation, TracedInteractionFragment, uml_umlTrace_Continuation, umlTrace_uml_TracedRemoveStructuralFeatureValueAction, umlTrace_uml_TracedProperty, uml_TracedConnectableElement, uml_TracedDeploymentTarget, uml_umlTrace_Artifact, umlTrace_uml_TracedTimeConstraint, TracedIntervalConstraint, umlTrace_uml_TracedInterfaceRealization, TracedRealization, uml_TracedBehavioredClassifier, umlTrace_uml_TracedObjectNode, TracedWriteStructuralFeatureAction, uml_umlTrace_RemoveStructuralFeatureValueAction, umlTrace_uml_TracedSendSignalAction, TracedInvocationAction, uml_umlTrace_SendSignalAction, umlTrace_uml_TracedOpaqueBehavior, TracedBehavior, umlTrace_uml_TracedArtifact, uml_TracedClassifier, uml_TracedDeployedArtifact, uml_umlTrace_AcceptEventAction, umlTrace_uml_TracedEnumerationLiteral, TracedInstanceSpecification, umlTrace_uml_TracedAddStructuralFeatureValueAction, uml_umlTrace_AddStructuralFeatureValueAction, umlTrace_uml_TracedReadLinkAction, TracedLinkAction, umlTrace_uml_TracedActivityFinalNode, TracedFinalNode, uml_umlTrace_ActivityFinalNode, umlTrace_uml_TracedDurationObservation, TracedObservation, uml_TracedNamedElement, uml_umlTrace_DurationObservation, umlTrace_uml_TracedAcceptEventAction, umlTrace_uml_TracedDataStoreNode, TracedCentralBufferNode, umlTrace_uml_TracedFlowFinalNode, uml_umlTrace_FlowFinalNode, umlTrace_uml_TracedInteractionFragment, TracedNamedElement, umlTrace_uml_TracedClassifier, uml_TracedNamespace, uml_TracedRedefinableElement, uml_TracedType, uml_TracedTemplateableElement, uml_umlTrace_ReadLinkAction, umlTrace_uml_TracedExpression, TracedValueSpecification, uml_umlTrace_Expression, umlTrace_uml_TracedConsiderIgnoreFragment, TracedCombinedFragment, umlTrace_uml_TracedInformationItem, uml_umlTrace_Collaboration, umlTrace_uml_TracedMessageEnd, umlTrace_uml_TracedTemplateSignature, TracedElement, uml_umlTrace_InformationItem, umlTrace_uml_TracedCollaboration, uml_TracedStructuredClassifier, umlTrace_uml_TracedPort, TracedProperty, umlTrace_uml_TracedTimeInterval, TracedInterval, umlTrace_uml_TracedAction, TracedExecutableNode, uml_umlTrace_TemplateSignature, umlTrace_uml_TracedBroadcastSignalAction, uml_umlTrace_BroadcastSignalAction, umlTrace_uml_TracedDeployment, TracedDependency, umlTrace_uml_TracedDirectedRelationship, TracedRelationship, umlTrace_uml_TracedTimeEvent, TracedEvent, uml_umlTrace_TimeEvent, umlTrace_uml_TracedPackageableElement, uml_TracedParameterableElement, umlTrace_uml_TracedType, TracedPackageableElement, umlTrace_uml_TracedExtension, umlTrace_uml_TracedProtocolTransition, TracedTransition, umlTrace_uml_TracedPackage, uml_TracedPackageableElement, umlTrace_uml_TracedConstraint, uml_umlTrace_Constraint, umlTrace_uml_TracedMultiplicityElement, umlTrace_uml_TracedLiteralSpecification, uml_umlTrace_Package, umlTrace_uml_TracedBehavioredClassifier, umlTrace_uml_TracedStructuralFeatureAction, uml_umlTrace_ReduceAction, umlTrace_uml_TracedInputPin, TracedPin, uml_umlTrace_InputPin, umlTrace_uml_TracedSequenceNode, TracedStructuredActivityNode, uml_TracedExecutableNode, umlTrace_uml_TracedFeature, TracedRedefinableElement, umlTrace_uml_TracedInteractionConstraint, TracedConstraint, umlTrace_uml_TracedGeneralizationSet, uml_umlTrace_GeneralizationSet, umlTrace_uml_TracedReduceAction, umlTrace_uml_TracedComponentRealization, umlTrace_uml_TracedAssociationClass, umlTrace_uml_TracedSlot, umlTrace_uml_TracedWriteStructuralFeatureAction, TracedStructuralFeatureAction, umlTrace_uml_TracedElement, TracedEModelElement, umlTrace_uml_TracedJoinNode, TracedControlNode, uml_umlTrace_JoinNode, umlTrace_uml_TracedStartObjectBehaviorAction, TracedCallAction, uml_umlTrace_StartObjectBehaviorAction, umlTrace_uml_TracedElementImport, TracedDirectedRelationship, uml_umlTrace_ElementImport, uml_umlTrace_Slot, umlTrace_uml_TracedSignalEvent, TracedMessageEvent, uml_umlTrace_SignalEvent, umlTrace_uml_TracedExtensionPoint, uml_umlTrace_ExtensionPoint, uml_umlTrace_OccurrenceSpecification, umlTrace_uml_TracedStringExpression, umlTrace_uml_TracedDeployedArtifact, umlTrace_uml_TracedStereotype, TracedClass, umlTrace_uml_TracedInterface, umlTrace_uml_TracedCreateObjectAction, uml_umlTrace_CreateObjectAction, umlTrace_uml_TracedExecutionEnvironment, TracedNode, umlTrace_uml_TracedOccurrenceSpecification, umlTrace_uml_TracedConditionalNode, umlTrace_uml_TracedReadLinkObjectEndAction, uml_umlTrace_Interface, uml_umlTrace_ReadLinkObjectEndAction, umlTrace_uml_TracedAnyReceiveEvent, uml_umlTrace_AnyReceiveEvent, umlTrace_uml_TracedNamedElement, umlTrace_uml_TracedComponent, umlTrace_uml_TracedLiteralString, TracedLiteralSpecification, uml_umlTrace_LiteralString, umlTrace_uml_TracedRealization, TracedAbstraction, umlTrace_uml_TracedStartClassifierBehaviorAction, umlTrace_uml_TracedExtensionEnd, umlTrace_uml_TracedStateMachine, umlTrace_uml_TracedValueSpecification, umlTrace_uml_TracedInteraction, uml_TracedInteractionFragment, uml_TracedAction, uml_umlTrace_SendObjectAction, umlTrace_uml_TracedLifeline, uml_umlTrace_StartClassifierBehaviorAction, umlTrace_uml_TracedMessageEvent, umlTrace_uml_TracedCallEvent, uml_umlTrace_CallEvent, umlTrace_uml_TracedConnectableElementTemplateParameter, TracedTemplateParameter, umlTrace_uml_TracedRelationship, umlTrace_uml_TracedSendObjectAction, umlTrace_uml_TracedExpansionRegion, umlTrace_uml_TracedWriteVariableAction, TracedVariableAction, uml_umlTrace_Lifeline, umlTrace_uml_TracedExecutionSpecification, umlTrace_uml_TracedTimeObservation, uml_umlTrace_TimeObservation, umlTrace_uml_TracedCreateLinkObjectAction, TracedCreateLinkAction, umlTrace_uml_TracedProtocolConformance, uml_umlTrace_ProtocolConformance, umlTrace_uml_TracedLoopNode, umlTrace_uml_TracedPrimitiveType, TracedDataType, umlTrace_uml_TracedEnumeration, umlTrace_uml_TracedCollaborationUse, uml_umlTrace_CollaborationUse, umlTrace_uml_TracedActivityPartition, TracedActivityGroup, ActivityContent, uml_TracedActivityGroup, uml_umlTrace_ActivityPartition, umlTrace_uml_TracedVariableAction, umlTrace_uml_TracedLinkEndDestructionData, TracedLinkEndData, umlTrace_uml_TracedDurationInterval, umlTrace_uml_TracedInclude, uml_TracedDirectedRelationship, uml_umlTrace_Include, umlTrace_uml_TracedActivityNode, umlTrace_uml_TracedDestructionOccurrenceSpecification, TracedMessageOccurrenceSpecification, umlTrace_uml_TracedState, uml_TracedVertex, umlTrace_uml_TracedBehavior, uml_TracedBehavioralFeature, uml_umlTrace_State, umlTrace_uml_TracedCallAction, umlTrace_uml_TracedTemplateableElement, uml_umlTrace_ActivityParameterNode, umlTrace_uml_TracedParameterSet, umlTrace_uml_TracedClassifierTemplateParameter, umlTrace_uml_TracedActivityParameterNode, TracedObjectNode, uml_umlTrace_Class, umlTrace_uml_TracedUsage, umlTrace_uml_TracedLiteralUnlimitedNatural, uml_umlTrace_LiteralUnlimitedNatural, uml_umlTrace_ParameterSet, umlTrace_uml_TracedDuration, uml_TracedObservation, uml_umlTrace_Duration, umlTrace_uml_TracedClass, uml_TracedEncapsulatedClassifier, umlTrace_uml_TracedReadStructuralFeatureAction, uml_umlTrace_ReadStructuralFeatureAction, umlTrace_uml_TracedMergeNode, uml_umlTrace_MergeNode, umlTrace_uml_TracedStructuredActivityNode, uml_umlTrace_StructuredActivityNode, umlTrace_uml_TracedAbstraction, uml_umlTrace_Generalization, umlTrace_uml_TracedPartDecomposition, TracedInteractionUse, umlTrace_uml_TracedTypedElement, umlTrace_uml_TracedRedefinableTemplateSignature, umlTrace_uml_TracedCreateLinkAction, TracedWriteLinkAction, uml_umlTrace_CreateLinkAction, umlTrace_uml_TracedGeneralization, uml_umlTrace_TemplateParameterSubstitution, umlTrace_uml_TracedExtend, umlTrace_uml_TracedOperationTemplateParameter, umlTrace_uml_TracedReadLinkObjectEndQualifierAction, uml_umlTrace_ReadLinkObjectEndQualifierAction, umlTrace_uml_TracedTemplateParameterSubstitution, uml_TracedMessageEnd, uml_umlTrace_Extend, umlTrace_uml_TracedReadVariableAction, uml_umlTrace_ReadVariableAction, umlTrace_uml_TracedMessage, umlTrace_uml_TracedProfileApplication, uml_umlTrace_Message, umlTrace_uml_TracedLiteralBoolean, uml_umlTrace_LiteralBoolean, umlTrace_uml_TracedQualifierValue, uml_umlTrace_QualifierValue, umlTrace_uml_TracedInitialNode, uml_umlTrace_InitialNode, umlTrace_uml_TracedLiteralInteger, uml_umlTrace_LiteralInteger, umlTrace_uml_TracedClearVariableAction, uml_umlTrace_ClearVariableAction, uml_umlTrace_TemplateParameter, umlTrace_uml_TracedConnectorEnd, TracedMultiplicityElement, uml_umlTrace_ProfileApplication, umlTrace_uml_TracedParameterableElement, umlTrace_uml_TracedTemplateParameter, uml_umlTrace_Parameter, umlTrace_uml_TracedActionInputPin, TracedInputPin, umlTrace_uml_TracedTrigger, uml_TracedEvent, uml_umlTrace_ConnectorEnd, umlTrace_uml_TracedMessageOccurrenceSpecification, umlTrace_uml_TracedDurationConstraint, umlTrace_uml_TracedImage, uml_umlTrace_Image, umlTrace_uml_TracedEncapsulatedClassifier, TracedStructuredClassifier, umlTrace_uml_TracedParameter, uml_umlTrace_Interval, umlTrace_uml_TracedIntervalConstraint, umlTrace_uml_TracedInstanceSpecification, uml_umlTrace_Trigger, umlTrace_uml_TracedCallOperationAction, uml_umlTrace_CallOperationAction, umlTrace_uml_TracedProfile, TracedPackage, umlTrace_uml_TracedInterval, uml_umlTrace_ReadIsClassifiedObjectAction, umlTrace_uml_TracedProtocolStateMachine, TracedStateMachine, umlTrace_uml_TracedOutputPin, uml_umlTrace_OutputPin, uml_umlTrace_InstanceSpecification, umlTrace_uml_TracedValuePin, umlTrace_uml_TracedReadIsClassifiedObjectAction, uml_umlTrace_ValueSpecificationAction, umlTrace_uml_TracedRegion, umlTrace_uml_TracedDecisionNode, uml_umlTrace_DecisionNode, umlTrace_uml_TracedValueSpecificationAction, uml_umlTrace_InterruptibleActivityRegion, umlTrace_uml_TracedDestroyLinkAction, uml_umlTrace_DestroyLinkAction, umlTrace_uml_TracedFinalState, TracedState, umlTrace_uml_TracedActivityGroup, uml_umlTrace_Region, umlTrace_uml_TracedInterruptibleActivityRegion, uml_umlTrace_InteractionOperand, umlTrace_uml_TracedActivityEdge, umlTrace_uml_TracedInteractionOperand, umlTrace_uml_TracedInformationFlow, uml_umlTrace_Pseudostate, umlTrace_uml_TracedControlNode, TracedActivityNode, umlTrace_uml_TracedUseCase, TracedBehavioredClassifier, uml_TracedRelationship, uml_umlTrace_InformationFlow, umlTrace_uml_TracedPseudostate, TracedVertex, umlTrace_uml_TracedCombinedFragment, uml_umlTrace_CombinedFragment, uml_umlTrace_UseCase, umlTrace_uml_TracedReplyAction, uml_umlTrace_ReplyAction, umlTrace_uml_TracedDependency, umlTrace_uml_TracedWriteLinkAction, umlTrace_uml_TracedClause, uml_umlTrace_Clause, umlTrace_uml_TracedInstanceValue, uml_umlTrace_InstanceValue, uml_umlTrace_ReadExtentAction, umlTrace_uml_TracedTransition, uml_umlTrace_Dependency, umlTrace_uml_TracedTimeExpression, uml_umlTrace_TimeExpression, umlTrace_uml_TracedManifestation, umlTrace_uml_TracedReadExtentAction, uml_umlTrace_LinkEndData, umlTrace_uml_TracedNode, uml_umlTrace_Transition, umlTrace_uml_TracedLinkEndData, uml_umlTrace_ChangeEvent, umlTrace_uml_TracedRedefinableElement, umlTrace_uml_TracedPackageMerge, uml_umlTrace_PackageMerge, umlTrace_uml_TracedModel, umlTrace_uml_TracedObjectFlow, TracedActivityEdge, uml_umlTrace_ObjectFlow, umlTrace_uml_TracedEvent, umlTrace_uml_TracedChangeEvent, uml_umlTrace_Comment, umlTrace_uml_TracedStructuredClassifier, umlTrace_uml_TracedDestroyObjectAction, uml_umlTrace_DestroyObjectAction, umlTrace_uml_TracedForkNode, uml_umlTrace_ForkNode, umlTrace_uml_TracedFinalNode, umlTrace_uml_TracedSignal, uml_umlTrace_Signal, umlTrace_uml_TracedComment, uml_umlTrace_Reception, umlTrace_uml_TracedRaiseExceptionAction, uml_umlTrace_RaiseExceptionAction, umlTrace_uml_TracedLiteralNull, uml_umlTrace_LiteralNull, umlTrace_uml_TracedExpansionNode, uml_umlTrace_ExpansionNode, umlTrace_uml_TracedReception, TracedBehavioralFeature, uml_umlTrace_ClearAssociationAction, umlTrace_uml_TracedPin, uml_TracedObjectNode, umlTrace_uml_TracedTestIdentityAction, umlTrace_uml_TracedBehavioralFeature, umlTrace_uml_TracedAddVariableValueAction, TracedWriteVariableAction, uml_umlTrace_AddVariableValueAction, umlTrace_uml_TracedClearAssociationAction, uml_umlTrace_TestIdentityAction, umlTrace_uml_TracedControlFlow, uml_umlTrace_ControlFlow, umlTrace_uml_TracedOperation, umlTrace_uml_TracedObservation, umlTrace_uml_TracedNamespace, uml_umlTrace_Operation, umlTrace_uml_TracedConnectableElement, umlTrace_uml_TracedVertex, umlTrace_uml_TracedPackageImport, umlTrace_uml_TracedInteractionUse, uml_umlTrace_PackageImport, umlTrace_uml_TracedExecutionOccurrenceSpecification, TracedOccurrenceSpecification, uml_TracedExecutionSpecification, umlTrace_uml_TracedExceptionHandler, uml_umlTrace_ExceptionHandler, umlTrace_uml_TracedVariable, uml_umlTrace_Variable, uml_umlTrace_Association, umlTrace_uml_TracedStateInvariant, uml_umlTrace_StateInvariant, uml_umlTrace_InteractionUse, umlTrace_uml_TracedAssociation, umlTrace_uml_TracedDevice, umlTrace_uml_TracedSubstitution, umlTrace_uml_TracedLiteralReal, uml_umlTrace_LiteralReal, umlTrace_uml_TracedInvocationAction, umlTrace_uml_TracedRemoveVariableValueAction, uml_umlTrace_RemoveVariableValueAction, uml_umlTrace_ReclassifyObjectAction, umlTrace_uml_TracedGate, TracedMessageEnd, uml_umlTrace_Gate, umlTrace_uml_TracedDeploymentTarget, umlTrace_uml_TracedGeneralOrdering, uml_umlTrace_GeneralOrdering, umlTrace_uml_TracedCallBehaviorAction, uml_umlTrace_CallBehaviorAction, umlTrace_uml_TracedReclassifyObjectAction, umlTrace_uml_TracedConnectionPointReference, umlTrace_uml_TracedActivity, umlTrace_uml_TracedLinkEndCreationData, umlTrace_uml_TracedTemplateBinding, uml_umlTrace_ConnectionPointReference, umlTrace_uml_TracedActionExecutionSpecification, TracedExecutionSpecification, uml_umlTrace_ActionExecutionSpecification, umlTrace_uml_TracedReadSelfAction, uml_umlTrace_ReadSelfAction, umlTrace_uml_TracedAcceptCallAction, TracedAcceptEventAction, umlTrace_uml_TracedActor, uml_umlTrace_Actor, umlTrace_uml_TracedBehaviorExecutionSpecification, uml_umlTrace_BehaviorExecutionSpecification, umlTrace_uml_TracedExecutableNode, uml_umlTrace_TemplateBinding, umlTrace_uml_TracedClearStructuralFeatureAction, uml_umlTrace_ClearStructuralFeatureAction, umlTrace_uml_TracedOpaqueExpression, uml_umlTrace_OpaqueExpression, umlTrace_uml_TracedFunctionBehavior, TracedOpaqueBehavior, umlTrace_uml_TracedDeploymentSpecification, TracedArtifact, umlTrace_uml_TracedUnmarshallAction, uml_umlTrace_UnmarshallAction, umlTrace_uml_TracedCentralBufferNode, uml_umlTrace_CentralBufferNode, umlTrace_ecore_TracedEModelElement, ecore_umlTrace_EAnnotation},
    associations={statesTrace0, steps1, executionFactory_locus_ExecutionFactory_Values24, locus_factory_Values26, locus_extensionalValues_Values28, locus_executor_Values30, objectNodeActivation_offeredTokenCount_Values32, tracedObjects3, semanticVisitor_runtimeModelElement_Values34, followingStep5, startedBigSteps6, endedBigSteps7, object_types_Values9, reference_referent_Values10, integerValue_value_IntegerValue_Values12, forkedToken_remainingOffersCount_Values14, forkedToken_baseToken_Values16, forkedToken_baseTokenIsWithdrawn_Values18, executionFactory_builtInTypes_Values20, executionFactory_primitiveBehaviorPrototypes_Values22, activityNodeActivationGroup_activityExecution_Values52, activityNodeActivationGroup_edgeInstances_Values54, executor_locus_Executor_Values56, primitiveValue_type_Values58, parameterValue_values_ParameterValue_Values36, parameterValue_parameter_ParameterValue_Values38, actionActivation_pinActivations_Values40, actionActivation_firing_Values42, execution_parameterValues_Values44, execution_context_Values46, element_semanticVisitor_Values48, activityNodeActivationGroup_nodeActivations_Values50, featureValue_feature_Values78, featureValue_position_Values80, pinActivation_actionActivation_Values82, evaluation_specification_Evaluation_Values60, evaluation_locus_Evaluation_Values62, booleanValue_value_BooleanValue_Values64, objectToken_value_Values66, callActionActivation_callExecutions_Values68, compoundValue_featureValues_Values70, token_holder_Values72, offer_offeredTokens_Values74, featureValue_values_FeatureValue_Values76, activityNodeActivation_node_ActivityNodeActivation_Values102, activityNodeActivation_running_Values104, activityNodeActivation_isRunning_Values106, pinActivation_count_temp_Values84, activityEdgeInstance_group_ActivityEdgeInstance_Values86, activityEdgeInstance_offers_Values88, activityEdgeInstance_target_Values90, activityEdgeInstance_edge_ActivityEdgeInstance_Values92, activityEdgeInstance_source_Values94, inputParameterValues_name_Values96, inputParameterValues_parameterValues_Values98, activityNodeActivation_heldTokens_Values100, types125, parent126, states127, activityNodeActivation_outgoingEdges_Values108, activityNodeActivation_incomingEdges_Values110, activityNodeActivation_group_ActivityNodeActivation_Values112, extensionalValue_locus_ExtensionalValue_Values114, activityExecution_activationGroup_Values116, executionEnvironment_locus_ExecutionEnvironment_Values118, precedingState120, startingState121, endingState123, baseToken139, parent140, states142, referent129, parent130, states131, parent133, states134, parent136, states137, states160, factory162, parent163, states164, extensionalValues166, parent144, states146, builtInTypes148, parent149, states150, primitiveBehaviorPrototypes152, parent153, states155, locus_ExecutionFactory157, parent158, runtimeModelElement179, parent180, states181, parent167, states169, executor171, parent172, states174, parent176, states177, parent196, states198, values_ParameterValue183, parent184, states185, parameter_ParameterValue187, parent188, states190, pinActivations192, parent193, states194, nodeActivations214, parent215, parameterValues200, parent201, states202, context204, parent206, states208, semanticVisitor210, parent211, states212, parent230, states231, type233, parent235, states216, activityExecution218, parent219, states221, edgeInstances223, parent224, states226, locus_Executor228, states249, value251, parent253, states254, states236, specification_Evaluation238, parent239, states240, locus_Evaluation242, parent244, states246, parent248, offeredTokens269, parent271, states272, callExecutions256, parent257, states258, featureValues260, parent261, states262, holder264, parent266, states267, states286, actionActivation288, parent289, values_FeatureValue274, parent276, states277, feature279, parent280, states282, parent284, offers300, parent301, states290, parent292, states294, group_ActivityEdgeInstance296, parent297, states298, states314, source316, parent318, states320, states303, target305, parent307, states309, edge_ActivityEdgeInstance311, parent312, states335, node_ActivityNodeActivation337, parent338, states340, parent322, states323, parameterValues325, parent327, states330, heldTokens332, parent334, states354, incomingEdges356, parent358, states360, parent342, states344, parent346, states348, outgoingEdges350, parent352, states376, locus_ExecutionEnvironment378, parent380, states381, group_ActivityNodeActivation362, parent364, states366, locus_ExtensionalValue368, parent370, states371, activationGroup373, parent375, kernel_tracedIntegerValues403, intermediateActivities_tracedForkedTokens405, uml_tracedOpaqueBehaviors407, loci_tracedExecutionFactorys409, loci_tracedLocuss412, uml_tracedArtifacts415, kernel_tracedObjects383, uml_tracedConnectors385, uml_tracedOpaqueActions387, uml_tracedDataTypes389, uml_tracedCommunicationPaths391, kernel_tracedReferences393, uml_tracedPropertys395, uml_tracedContinuations397, uml_tracedRemoveStructuralFeatureValueActions399, uml_tracedSendSignalActions401, uml_tracedExpressions437, uml_tracedConsiderIgnoreFragments439, uml_tracedDataStoreNodes441, uml_tracedFlowFinalNodes443, uml_tracedInformationItems445, intermediateActivities_tracedJoinNodeActivations417, uml_tracedTimeConstraints419, uml_tracedInterfaceRealizations421, uml_tracedActivityFinalNodes423, uml_tracedDurationObservations425, intermediateActivities_tracedInitialNodeActivations427, uml_tracedAcceptEventActions429, uml_tracedEnumerationLiterals431, uml_tracedAddStructuralFeatureValueActions433, uml_tracedReadLinkActions435, uml_tracedTimeEvents464, basicBehaviors_tracedParameterValues466, uml_tracedProtocolTransitions469, intermediateActivities_tracedActivityFinalNodeActivations471, uml_tracedPackages473, uml_tracedCollaborations447, uml_tracedTemplateSignatures449, uml_tracedBroadcastSignalActions451, uml_tracedDeployments453, uml_tracedPorts455, uml_tracedTimeIntervals457, uml_tracedExtensions459, loci_tracedSemanticVisitors461, uml_tracedSlots491, uml_tracedSignalEvents493, uml_tracedExtensionPoints495, uml_tracedJoinNodes497, uml_tracedConstraints475, uml_tracedGeneralizationSets477, uml_tracedReduceActions479, uml_tracedInputPins481, uml_tracedSequenceNodes483, uml_tracedInteractionConstraints485, uml_tracedComponentRealizations487, uml_tracedAssociationClasss489, intermediateActions_tracedValueSpecificationActionActivations514, uml_tracedStringExpressions516, loci_tracedExecutors518, intermediateActions_tracedReadStructuralFeatureActionActivations521, basicActions_tracedOutputPinActivations499, uml_tracedStartObjectBehaviorActions501, uml_tracedElementImports503, uml_tracedCreateObjectActions505, uml_tracedExecutionEnvironments507, uml_tracedOccurrenceSpecifications509, intermediateActivities_tracedActivityNodeActivationGroups511, uml_tracedStateMachines537, intermediateActivities_tracedMergeNodeActivations539, uml_tracedInteractions541, uml_tracedStereotypes523, uml_tracedInterfaces525, uml_tracedConditionalNodes527, uml_tracedReadLinkObjectEndActions529, uml_tracedAnyReceiveEvents531, uml_tracedComponents533, uml_tracedExtensionEnds535, uml_tracedLifelines555, uml_tracedTimeObservations557, intermediateActivities_tracedControlTokens559, uml_tracedCreateLinkObjectActions561, uml_tracedLiteralStrings543, uml_tracedRealizations545, uml_tracedStartClassifierBehaviorActions547, uml_tracedCallEvents549, uml_tracedConnectableElementTemplateParameters551, uml_tracedSendObjectActions553, uml_tracedEnumerations574, uml_tracedCollaborationUses576, uml_tracedActivityPartitions578, uml_tracedExpansionRegions563, kernel_tracedBooleanValues565, uml_tracedLoopNodes567, uml_tracedPrimitiveTypes569, uml_tracedProtocolConformances572, basicActions_tracedCallBehaviorActionActivations592, intermediateActions_tracedAddStructuralFeatureValueActionActivations594, uml_tracedClassifierTemplateParameters596, uml_tracedLinkEndDestructionDatas580, uml_tracedDurationIntervals582, uml_tracedIncludes584, uml_tracedDestructionOccurrenceSpecifications586, uml_tracedStates588, intermediateActivities_tracedObjectTokens590, uml_tracedLiteralUnlimitedNaturals611, uml_tracedStructuredActivityNodes613, uml_tracedAbstractions615, uml_tracedActivityParameterNodes598, integerFunctions_tracedIntegerLessFunctionBehaviorExecutions600, uml_tracedParameterSets602, uml_tracedDurations604, uml_tracedClasss606, uml_tracedUsages609, uml_tracedCreateLinkActions627, uml_tracedGeneralizations629, uml_tracedPartDecompositions631, basicActions_tracedOpaqueActionActivations617, kernel_tracedLiteralBooleanEvaluations619, uml_tracedReadStructuralFeatureActions621, uml_tracedMergeNodes623, uml_tracedRedefinableTemplateSignatures625, uml_tracedMessages643, uml_tracedLiteralBooleans645, uml_tracedOperationTemplateParameters633, uml_tracedReadLinkObjectEndQualifierActions635, uml_tracedTemplateParameterSubstitutions637, uml_tracedExtends639, uml_tracedReadVariableActions641, intermediateActivities_tracedDecisionNodeActivations655, uml_tracedProfileApplications657, uml_tracedQualifierValues647, uml_tracedInitialNodes649, uml_tracedLiteralIntegers651, uml_tracedClearVariableActions653, uml_tracedParameters669, uml_tracedActionInputPins672, uml_tracedTemplateParameters659, uml_tracedConnectorEnds661, uml_tracedMessageOccurrenceSpecifications663, uml_tracedDurationConstraints665, uml_tracedImages667, intermediateActivities_tracedForkNodeActivations682, uml_tracedIntervalConstraints684, intermediateActivities_tracedTokens686, uml_tracedTriggers674, uml_tracedCallOperationActions676, uml_tracedProfiles678, uml_tracedIntervals680, uml_tracedProtocolStateMachines697, uml_tracedOutputPins699, uml_tracedInstanceSpecifications689, uml_tracedValuePins691, integerFunctions_tracedIntegerGreaterFunctionBehaviorExecutions693, uml_tracedReadIsClassifiedObjectActions695, uml_tracedInterruptibleActivityRegions712, uml_tracedDestroyLinkActions714, intermediateActivities_tracedOffers701, intermediateActivities_tracedActivityParameterNodeActivations704, uml_tracedDecisionNodes706, uml_tracedValueSpecificationActions708, uml_tracedRegions710, uml_tracedPseudostates724, uml_tracedUseCases726, uml_tracedFinalStates716, integerFunctions_tracedIntegerPlusFunctionBehaviorExecutions718, uml_tracedInteractionOperands720, uml_tracedInformationFlows722, uml_tracedInstanceValues736, uml_tracedDependencys738, uml_tracedTimeExpressions740, uml_tracedReplyActions728, intermediateActions_tracedCreateObjectActionActivations730, uml_tracedCombinedFragments732, uml_tracedClauses734, uml_tracedTransitions751, uml_tracedLinkEndDatas753, intermediateActivities_tracedActivityEdgeInstances742, uml_tracedManifestations745, uml_tracedReadExtentActions747, basicActions_tracedInputPinActivations749, uml_tracedObjectFlows763, uml_tracedChangeEvents765, uml_tracedDestroyObjectActions767, input_tracedInputParameterValuess755, uml_tracedNodes757, uml_tracedPackageMerges759, uml_tracedModels761, uml_tracedForkNodes769, uml_tracedReceptions779, uml_tracedRaiseExceptionActions781, uml_tracedSignals771, uml_tracedComments773, uml_tracedLiteralNulls775, uml_tracedExpansionNodes777, uml_tracedTestIdentityActions790, uml_tracedControlFlows792, uml_tracedOperations794, intermediateActivities_tracedActivityNodeActivations783, uml_tracedAddVariableValueActions786, uml_tracedClearAssociationActions788, uml_tracedExceptionHandlers800, uml_tracedPackageImports796, uml_tracedExecutionOccurrenceSpecifications798, uml_tracedStateInvariants808, uml_tracedLiteralReals810, uml_tracedRemoveVariableValueActions812, uml_tracedVariables802, uml_tracedInteractionUses804, uml_tracedAssociations806, uml_tracedGeneralOrderings820, uml_tracedCallBehaviorActions822, uml_tracedReclassifyObjectActions824, uml_tracedDevices814, uml_tracedSubstitutions816, uml_tracedGates818, uml_tracedReadSelfActions832, uml_tracedAcceptCallActions834, uml_tracedActivitys826, uml_tracedConnectionPointReferences828, uml_tracedActionExecutionSpecifications830, uml_tracedLinkEndCreationDatas836, intermediateActivities_tracedActivityExecutions838, uml_tracedTemplateBindings841, uml_tracedOpaqueExpressions849, uml_tracedClearStructuralFeatureActions843, loci_tracedExecutionEnvironments845, kernel_tracedLiteralIntegerEvaluations847, uml_tracedUnmarshallActions859, uml_tracedCentralBufferNodes861, uml_tracedFunctionBehaviors851, uml_tracedDeploymentSpecifications853, uml_tracedActors855, uml_tracedBehaviorExecutionSpecifications857, typeTrace871, specification_EvaluationTrace874, locus_EvaluationTrace877, value_BooleanValueTrace880, typesTrace863, referentTrace865, value_IntegerValueTrace868, values_ParameterValueTrace898, parameter_ParameterValueTrace901, parameterValuesTrace904, contextTrace907, featureValuesTrace883, values_FeatureValueTrace886, featureTrace889, positionTrace892, locus_ExtensionalValueTrace895, nodeActivationsTrace922, activityExecutionTrace925, edgeInstancesTrace928, valueTrace931, remainingOffersCountTrace910, baseTokenTrace913, baseTokenIsWithdrawnTrace916, offeredTokenCountTrace919, sourceTrace952, heldTokensTrace955, node_ActivityNodeActivationTrace958, runningTrace961, isRunningTrace964, outgoingEdgesTrace967, incomingEdgesTrace970, holderTrace934, offeredTokensTrace937, group_ActivityEdgeInstanceTrace940, offersTrace943, targetTrace946, edge_ActivityEdgeInstanceTrace949, executorTrace994, runtimeModelElementTrace997, locus_ExecutorTrace1000, locus_ExecutionEnvironmentTrace1003, group_ActivityNodeActivationTrace973, activationGroupTrace976, builtInTypesTrace979, primitiveBehaviorPrototypesTrace982, locus_ExecutionFactoryTrace985, factoryTrace988, extensionalValuesTrace991, callExecutionsTrace1012, actionActivationTrace1015, count_tempTrace1018, pinActivationsTrace1006, firingTrace1009, originalObject1037, inputValue1039, outputValue1041, originalObject1044, ownedAttribute1046, ownedOperation1048, originalObject_DataType1051, nameTrace1021, parameterValuesTrace1024, contract1027, end1028, redefinedConnector1031, type1034, class_1069, defaultValue1072, opposite1075, owningAssociation1078, redefinedProperty1081, subsettedProperty1084, association1087, originalObject_Property1090, originalObject1092, endData1053, inputValue1055, datatype1058, interface1060, associationEnd1063, qualifier1066, nestedArtifact1106, ownedAttribute1109, ownedOperation1112, originalObject_Artifact1115, contract1117, implementingClassifier1119, inState1121, selection1123, upperBound1126, removeAt1093, originalObject1095, signal1097, target1099, originalObject1102, manifestation1104, originalObject_AcceptEventAction1138, enumeration1140, insertAt1142, originalObject1144, originalObject1129, event1130, originalObject1131, result1133, trigger1135, originalObject1156, covered1157, enclosingOperand1159, enclosingInteraction1162, generalOrdering1165, result1146, originalObject1148, operand1150, originalObject_Expression1152, message1154, powertypeExtent1180, inheritedMember1183, ownedUseCase1186, useCase1189, redefinedClassifier1192, representation1195, substitution1198, feature1168, attribute1169, collaborationUse1172, general1175, generalization1177, originalObject1206, message1208, parameter1210, template1212, ownedParameter1214, represented1201, originalObject1203, deployedArtifact1225, collaborationRole1205, location1227, protocol1229, provided1231, redefinedPort1234, required1237, originalObject_TemplateSignature1217, signal1219, originalObject1221, configuration1223, metaclass1254, source1256, target1258, when1261, originalObject1263, context1240, input1242, localPostcondition1245, localPrecondition1248, output1251, nestingPackage1277, ownedStereotype1280, ownedType1283, packageMerge1285, packagedElement1288, profileApplication1290, package1265, postCondition1267, preCondition1269, referred1272, nestedPackage1275, structuralFeature1305, constrainedElement1308, context1310, specification1312, originalObject_Constraint1315, lowerValue1317, upperValue1319, originalObject_Package1293, classifierBehavior1295, interfaceRealization1297, ownedBehavior1300, object1303, originalObject1337, originalObject_InputPin1339, executableNode1340, featuringClassifier1341, maxint1343, powertype1322, generalization1324, originalObject1327, collection1329, reducer1331, result1334, owner1358, semanticVisitorTrace1361, realizingClassifier1364, abstraction1366, definingFeature1369, value1371, minint1345, result1348, value1350, ownedComment1353, ownedElement1355, joinSpec1387, originalObject1389, object1391, originalObject1393, importedElement1395, importingNamespace1397, owningInstance1374, originalObject1377, signal1379, originalObject1381, useCase1383, originalObject1385, toBefore1411, originalObject_OccurrenceSpecification1414, owningExpression1416, subExpression1418, icon1421, profile1423, originalObject1400, classifier1402, result1404, originalObject1407, toAfter1409, originalObject1443, clause1445, result1447, nestedClassifier1426, ownedAttribute1428, packagedElement1469, ownedReception1431, provided1471, protocol1434, realization1474, redefinedInterface1437, required1477, end1450, ownedOperation1440, object1452, result1455, originalObject1458, originalObject1460, clientDependency1461, nameExpression1463, namespace1466, formalGate1497, message1500, originalObject1503, connectionPoint1480, submachineState1482, region1485, extendedStateMachine1488, lifeline1491, fragment1493, action1495, target1516, originalObject1519, decomposedAs1521, interaction1523, object1504, originalObject1506, operation1508, originalObject1510, relatedElement1512, request1514, outputElement1548, inputElement1550, value1553, represents1526, selector1529, coveredBy1532, originalObject1535, finish1537, start1539, event1542, originalObject1544, result1546, generalMachine1578, specificMachine1580, bodyOutput1555, bodyPart1557, decider1560, loopVariable1563, loopVariableInput1566, result1569, setupPart1572, test1575, subpartition1599, superPartition1602, edge1605, originalObject1583, ownedLiteral1585, roleBinding1587, type1589, originalObject1592, node1594, represents1596, activity1621, inGroup1623, inInterruptibleRegion1625, originalObject1608, variable1610, destroyAt1612, addition1614, includingCase1616, originalObject1619, deferrableTrigger1648, doActivity1651, entry1654, inStructuredNode1628, incoming1631, outgoing1634, redefinedNode1637, inPartition1640, connection1643, connectionPoint1645, ownedTemplateSignature1678, specification1681, context1682, exit1657, redefinedState1660, stateInvariant1663, submachine1666, region1669, originalObject_State1672, result1674, templateBinding1676, parameter1702, originalObject1704, condition1706, parameter1708, ownedParameter1685, ownedParameterSet1688, postcondition1691, precondition1694, redefinedBehavior1697, constrainingClassifier1700, superClass1730, originalObject_Class1733, originalObject1711, expr1713, observation1715, originalObject1717, ownedOperation1719, extension1721, nestedClassifier1724, ownedReception1727, mapping1752, result1754, originalObject1756, originalObject1735, edge1736, structuredNodeInput1738, structuredNodeOutput1741, variable1744, node1747, originalObject_StructuredActivityNode1750, specific1773, originalObject1776, type1778, originalObject1758, extendedSignature1759, inheritedParameter1761, classifier1764, originalObject_CreateLinkAction1767, general1768, generalizationSet1770, templateBinding1797, originalObject1800, condition1802, object1780, qualifier1782, result1785, originalObject1788, actual1790, formal1791, ownedActual1794, connector1821, interaction1824, receiveEvent1827, sendEvent1829, extendedCase1804, extensionLocation1807, extension1810, originalObject1813, result1815, originalObject1817, argument1819, originalObject1847, appliedProfile1848, applyingPackage1850, signature1832, originalObject1835, originalObject1837, qualifier1838, value1840, originalObject1843, originalObject1845, originalObject1846, originalObject_TemplateParameter1874, definingEnd1876, partWithPort1878, originalObject1853, owningTemplateParameter1855, templateParameter1857, default1860, ownedDefault1862, parameteredElement1865, signature1868, ownedParameteredElement1871, originalObject1897, fromAction1899, event1901, role1881, originalObject1884, originalObject1886, ownedPort1887, defaultValue1889, operation1891, parameterSet1894, min1921, originalObject_Interval1924, classifier1926, port1902, originalObject1905, operation1907, target1909, originalObject1912, metaclassReference1914, metamodelReference1916, max1919, originalObject1946, conformance1948, originalObject1950, slot1928, specification1931, originalObject_InstanceSpecification1934, value1936, classifier1938, object1940, result1943, originalObject1963, extendedRegion1965, decisionInput1951, decisionInputFlow1953, originalObject1956, result1958, value1960, originalObject1985, originalObject1987, state1967, stateMachine1970, transition1973, subvertex1976, originalObject1978, interruptingEdge1980, node1982, guard2004, originalObject2007, containedEdge1988, containedNode1990, inActivity1993, subgroup1996, superGroup1999, fragment2002, weight2032, inGroup2035, conveyed2038, activity2009, guard2011, inPartition2014, interrupts2017, inStructuredNode2020, target2023, source2026, redefinedEdge2029, stateMachine2061, originalObject2064, extend2066, informationSource2040, informationTarget2043, realization2046, realizingActivityEdge2048, realizingConnector2051, realizingMessage2054, originalObject2057, state2059, originalObject2087, cfragmentGate2089, operand2091, originalObject_CombinedFragment2094, extensionPoint2068, include2071, subject2074, originalObject2077, replyToCall2079, replyValue2081, returnInformation2084, originalObject2117, client2119, supplier2121, body2096, bodyOutput2098, decider2101, predecessorClause2104, successorClause2107, test2110, originalObject2113, instance2115, originalObject2140, effect2142, guard2144, originalObject_Dependency2124, expr2126, observation2128, originalObject2131, utilizedElement2133, classifier2135, result2137, qualifier2166, value2169, originalObject_LinkEndData2172, nestedNode2174, redefinedTransition2147, source2150, target2153, trigger2156, container2159, originalObject_Transition2162, end2164, originalObject2192, redefinedElement2194, mergedPackage2176, receivingPackage2178, originalObject2181, selection2183, transformation2185, originalObject2188, changeExpression2190, annotatedElement2207, originalObject2209, ownedAttribute2211, redefinitionContext2195, target2198, originalObject2200, originalObject2202, ownedAttribute2203, originalObject2205, originalObject2232, exception2234, originalObject2236, ownedConnector2213, part2216, role2219, originalObject2222, regionAsInput2223, regionAsOutput2225, originalObject2228, signal2230, object2255, originalObject2258, first2260, method2238, ownedParameter2240, ownedParameterSet2243, raisedException2246, insertAt2249, originalObject2251, association2253, datatype2276, interface2279, postcondition2282, precondition2285, result2262, second2265, originalObject2268, originalObject2270, bodyCondition2271, class_2273, ownedRule2306, elementImport2308, redefinedOperation2288, type2291, originalObject2294, end2296, container2298, incoming2300, outgoing2303, importingNamespace2325, packageImport2311, ownedMember2314, importedMember2317, member2320, originalObject2348, importedPackage2323, actualGate2350, argument2352, refersTo2355, originalObject2328, execution2330, exceptionInput2331, exceptionType2332, handlerBody2335, protectedNode2338, originalObject2341, activityScope2343, scope2345, originalObject_Association2377, invariant2379, returnValue2358, returnValueRecipient2361, originalObject_InteractionUse2364, endType2366, memberEnd2368, ownedEnd2371, navigableOwnedEnd2374, contract2393, originalObject2381, originalObject2383, argument2384, onPort2386, removeAt2389, newClassifier2415, originalObject2391, object2417, oldClassifier2420, substitutingClassifier2395, originalObject2398, deployedElement2399, deployment2401, after2404, before2406, originalObject2409, behavior2411, originalObject2413, partition2442, structuredNode2445, entry2448, originalObject2423, ownedGroup2425, edge2427, node2430, variable2433, group2436, ownedNode2439, insertAt2468, parameterSubstitution2470, signature2472, exit2450, state2453, originalObject2456, action2458, originalObject2460, result2462, originalObject2464, returnInformation2466, originalObject2493, behavior2494, originalObject2496, boundElement2475, originalObject2478, result2480, originalObject2482, behavior2484, result2486, originalObject2489, deployment2491, handler2498, object2500, result2502, unmarshallType2505, originalObject2508, originalObject_CentralBufferNode2510, eAnnotations2511},
    generalizations={gen_umlTrace_Kernel_TracedEvaluation_TracedSemanticVisitor, gen_umlTrace_Kernel_TracedBooleanValue_TracedPrimitiveValue, gen_umlTrace_Kernel_TracedLiteralBooleanEvaluation_TracedLiteralEvaluation, gen_umlTrace_Kernel_TracedStructuredValue_TracedValue, gen_umlTrace_Kernel_TracedObject_TracedExtensionalValue, gen_umlTrace_Kernel_TracedReference_TracedStructuredValue, gen_umlTrace_Kernel_TracedIntegerValue_TracedPrimitiveValue, gen_umlTrace_Kernel_TracedLiteralEvaluation_TracedEvaluation, gen_umlTrace_Kernel_TracedValue_TracedSemanticVisitor, gen_umlTrace_Kernel_TracedPrimitiveValue_TracedValue, gen_umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution_TracedExecution, gen_umlTrace_BasicBehaviors_TracedExecution_TracedObject, gen_umlTrace_Kernel_TracedCompoundValue_TracedStructuredValue, gen_umlTrace_Kernel_TracedExtensionalValue_TracedCompoundValue, gen_umlTrace_Kernel_TracedLiteralIntegerEvaluation_TracedLiteralEvaluation, gen_umlTrace_IntermediateActivities_TracedMergeNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedControlToken_TracedToken, gen_umlTrace_IntermediateActivities_TracedObjectToken_TracedToken, gen_umlTrace_IntermediateActivities_TracedDecisionNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedForkedToken_TracedToken, gen_umlTrace_IntermediateActivities_TracedJoinNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedInitialNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedObjectNodeActivation_TracedActivityNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityNodeActivation_TracedSemanticVisitor, gen_umlTrace_IntermediateActivities_TracedForkNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation_TracedObjectNodeActivation, gen_umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation_TracedActionActivation, gen_umlTrace_IntermediateActions_TracedValueSpecificationActionActivation_TracedActionActivation, gen_umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation, gen_umlTrace_IntermediateActivities_TracedControlNodeActivation_TracedActivityNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityExecution_TracedExecution, gen_umlTrace_BasicActions_TracedCallActionActivation_TracedInvocationActionActivation, gen_umlTrace_BasicActions_TracedPinActivation_TracedObjectNodeActivation, gen_umlTrace_BasicActions_TracedInputPinActivation_TracedPinActivation, gen_umlTrace_BasicActions_TracedInvocationActionActivation_TracedActionActivation, gen_umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_TracedOpaqueBehaviorExecution, gen_umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation_TracedWriteStructuralFeatureActionActivation, gen_umlTrace_IntermediateActions_TracedCreateObjectActionActivation_TracedActionActivation, gen_umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation, gen_umlTrace_BasicActions_TracedActionActivation_TracedActivityNodeActivation, gen_umlTrace_BasicActions_TracedOutputPinActivation_TracedPinActivation, gen_umlTrace_BasicActions_TracedCallBehaviorActionActivation_TracedCallActionActivation, gen_umlTrace_BasicActions_TracedOpaqueActionActivation_TracedActionActivation, gen_umlTrace_uml_TracedOpaqueAction_TracedAction, gen_umlTrace_uml_TracedDataType_TracedClassifier, gen_umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_TracedOpaqueBehaviorExecution, gen_umlTrace_uml_TracedCommunicationPath_TracedAssociation, gen_umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_TracedOpaqueBehaviorExecution, gen_umlTrace_uml_TracedLinkAction_TracedAction, gen_umlTrace_uml_TracedStructuralFeature_uml_TracedFeature, gen_umlTrace_uml_TracedStructuralFeature_uml_TracedTypedElement, gen_umlTrace_uml_TracedStructuralFeature_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedConnector_TracedFeature, gen_umlTrace_uml_TracedContinuation_TracedInteractionFragment, gen_umlTrace_uml_TracedProperty_uml_TracedStructuralFeature, gen_umlTrace_uml_TracedProperty_uml_TracedConnectableElement, gen_umlTrace_uml_TracedProperty_uml_TracedDeploymentTarget, gen_umlTrace_uml_TracedTimeConstraint_TracedIntervalConstraint, gen_umlTrace_uml_TracedInterfaceRealization_TracedRealization, gen_umlTrace_uml_TracedObjectNode_uml_TracedActivityNode, gen_umlTrace_uml_TracedObjectNode_uml_TracedTypedElement, gen_umlTrace_uml_TracedRemoveStructuralFeatureValueAction_TracedWriteStructuralFeatureAction, gen_umlTrace_uml_TracedSendSignalAction_TracedInvocationAction, gen_umlTrace_uml_TracedOpaqueBehavior_TracedBehavior, gen_umlTrace_uml_TracedArtifact_uml_TracedClassifier, gen_umlTrace_uml_TracedArtifact_uml_TracedDeployedArtifact, gen_umlTrace_uml_TracedEnumerationLiteral_TracedInstanceSpecification, gen_umlTrace_uml_TracedAddStructuralFeatureValueAction_TracedWriteStructuralFeatureAction, gen_umlTrace_uml_TracedReadLinkAction_TracedLinkAction, gen_umlTrace_uml_TracedActivityFinalNode_TracedFinalNode, gen_umlTrace_uml_TracedDurationObservation_TracedObservation, gen_umlTrace_uml_TracedAcceptEventAction_TracedAction, gen_umlTrace_uml_TracedDataStoreNode_TracedCentralBufferNode, gen_umlTrace_uml_TracedFlowFinalNode_TracedFinalNode, gen_umlTrace_uml_TracedInteractionFragment_TracedNamedElement, gen_umlTrace_uml_TracedClassifier_uml_TracedNamespace, gen_umlTrace_uml_TracedClassifier_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedClassifier_uml_TracedType, gen_umlTrace_uml_TracedClassifier_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedExpression_TracedValueSpecification, gen_umlTrace_uml_TracedConsiderIgnoreFragment_TracedCombinedFragment, gen_umlTrace_uml_TracedInformationItem_TracedClassifier, gen_umlTrace_uml_TracedMessageEnd_TracedNamedElement, gen_umlTrace_uml_TracedTemplateSignature_TracedElement, gen_umlTrace_uml_TracedCollaboration_uml_TracedStructuredClassifier, gen_umlTrace_uml_TracedCollaboration_uml_TracedBehavioredClassifier, gen_umlTrace_uml_TracedPort_TracedProperty, gen_umlTrace_uml_TracedTimeInterval_TracedInterval, gen_umlTrace_uml_TracedAction_TracedExecutableNode, gen_umlTrace_uml_TracedBroadcastSignalAction_TracedInvocationAction, gen_umlTrace_uml_TracedDeployment_TracedDependency, gen_umlTrace_uml_TracedDirectedRelationship_TracedRelationship, gen_umlTrace_uml_TracedTimeEvent_TracedEvent, gen_umlTrace_uml_TracedPackageableElement_uml_TracedNamedElement, gen_umlTrace_uml_TracedPackageableElement_uml_TracedParameterableElement, gen_umlTrace_uml_TracedType_TracedPackageableElement, gen_umlTrace_uml_TracedExtension_TracedAssociation, gen_umlTrace_uml_TracedProtocolTransition_TracedTransition, gen_umlTrace_uml_TracedPackage_uml_TracedNamespace, gen_umlTrace_uml_TracedPackage_uml_TracedPackageableElement, gen_umlTrace_uml_TracedPackage_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedConstraint_TracedPackageableElement, gen_umlTrace_uml_TracedMultiplicityElement_TracedElement, gen_umlTrace_uml_TracedLiteralSpecification_TracedValueSpecification, gen_umlTrace_uml_TracedBehavioredClassifier_TracedClassifier, gen_umlTrace_uml_TracedStructuralFeatureAction_TracedAction, gen_umlTrace_uml_TracedInputPin_TracedPin, gen_umlTrace_uml_TracedSequenceNode_TracedStructuredActivityNode, gen_umlTrace_uml_TracedFeature_TracedRedefinableElement, gen_umlTrace_uml_TracedInteractionConstraint_TracedConstraint, gen_umlTrace_uml_TracedGeneralizationSet_TracedPackageableElement, gen_umlTrace_uml_TracedReduceAction_TracedAction, gen_umlTrace_uml_TracedComponentRealization_TracedRealization, gen_umlTrace_uml_TracedAssociationClass_uml_TracedClass, gen_umlTrace_uml_TracedAssociationClass_uml_TracedAssociation, gen_umlTrace_uml_TracedSlot_TracedElement, gen_umlTrace_uml_TracedWriteStructuralFeatureAction_TracedStructuralFeatureAction, gen_umlTrace_uml_TracedElement_TracedEModelElement, gen_umlTrace_uml_TracedJoinNode_TracedControlNode, gen_umlTrace_uml_TracedStartObjectBehaviorAction_TracedCallAction, gen_umlTrace_uml_TracedElementImport_TracedDirectedRelationship, gen_umlTrace_uml_TracedSignalEvent_TracedMessageEvent, gen_umlTrace_uml_TracedExtensionPoint_TracedRedefinableElement, gen_umlTrace_uml_TracedStringExpression_uml_TracedExpression, gen_umlTrace_uml_TracedStringExpression_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedDeployedArtifact_TracedNamedElement, gen_umlTrace_uml_TracedStereotype_TracedClass, gen_umlTrace_uml_TracedInterface_TracedClassifier, gen_umlTrace_uml_TracedCreateObjectAction_TracedAction, gen_umlTrace_uml_TracedExecutionEnvironment_TracedNode, gen_umlTrace_uml_TracedOccurrenceSpecification_TracedInteractionFragment, gen_umlTrace_uml_TracedConditionalNode_TracedStructuredActivityNode, gen_umlTrace_uml_TracedReadLinkObjectEndAction_TracedAction, gen_umlTrace_uml_TracedAnyReceiveEvent_TracedMessageEvent, gen_umlTrace_uml_TracedNamedElement_TracedElement, gen_umlTrace_uml_TracedComponent_TracedClass, gen_umlTrace_uml_TracedLiteralString_TracedLiteralSpecification, gen_umlTrace_uml_TracedRealization_TracedAbstraction, gen_umlTrace_uml_TracedStartClassifierBehaviorAction_TracedAction, gen_umlTrace_uml_TracedExtensionEnd_TracedProperty, gen_umlTrace_uml_TracedStateMachine_TracedBehavior, gen_umlTrace_uml_TracedValueSpecification_uml_TracedPackageableElement, gen_umlTrace_uml_TracedValueSpecification_uml_TracedTypedElement, gen_umlTrace_uml_TracedInteraction_uml_TracedBehavior, gen_umlTrace_uml_TracedInteraction_uml_TracedInteractionFragment, gen_umlTrace_uml_TracedLifeline_TracedNamedElement, gen_umlTrace_uml_TracedMessageEvent_TracedEvent, gen_umlTrace_uml_TracedCallEvent_TracedMessageEvent, gen_umlTrace_uml_TracedConnectableElementTemplateParameter_TracedTemplateParameter, gen_umlTrace_uml_TracedRelationship_TracedElement, gen_umlTrace_uml_TracedSendObjectAction_TracedInvocationAction, gen_umlTrace_uml_TracedExpansionRegion_TracedStructuredActivityNode, gen_umlTrace_uml_TracedWriteVariableAction_TracedVariableAction, gen_umlTrace_uml_TracedExecutionSpecification_TracedInteractionFragment, gen_umlTrace_uml_TracedTimeObservation_TracedObservation, gen_umlTrace_uml_TracedCreateLinkObjectAction_TracedCreateLinkAction, gen_umlTrace_uml_TracedPrimitiveType_TracedDataType, gen_umlTrace_uml_TracedProtocolConformance_TracedDirectedRelationship, gen_umlTrace_uml_TracedLoopNode_TracedStructuredActivityNode, gen_umlTrace_uml_TracedEnumeration_TracedDataType, gen_umlTrace_uml_TracedCollaborationUse_TracedNamedElement, gen_umlTrace_uml_TracedActivityPartition_TracedActivityGroup, gen_umlTrace_uml_TracedActivityNode_ActivityContent, gen_umlTrace_uml_TracedVariableAction_TracedAction, gen_umlTrace_uml_TracedLinkEndDestructionData_TracedLinkEndData, gen_umlTrace_uml_TracedDurationInterval_TracedInterval, gen_umlTrace_uml_TracedInclude_uml_TracedNamedElement, gen_umlTrace_uml_TracedInclude_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedActivityNode_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedDestructionOccurrenceSpecification_TracedMessageOccurrenceSpecification, gen_umlTrace_uml_TracedState_uml_TracedNamespace, gen_umlTrace_uml_TracedState_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedState_uml_TracedVertex, gen_umlTrace_uml_TracedBehavior_TracedClass, gen_umlTrace_uml_TracedCallAction_TracedInvocationAction, gen_umlTrace_uml_TracedTemplateableElement_TracedElement, gen_umlTrace_uml_TracedParameterSet_TracedNamedElement, gen_umlTrace_uml_TracedClassifierTemplateParameter_TracedTemplateParameter, gen_umlTrace_uml_TracedActivityParameterNode_TracedObjectNode, gen_umlTrace_uml_TracedUsage_TracedDependency, gen_umlTrace_uml_TracedLiteralUnlimitedNatural_TracedLiteralSpecification, gen_umlTrace_uml_TracedDuration_TracedValueSpecification, gen_umlTrace_uml_TracedClass_uml_TracedEncapsulatedClassifier, gen_umlTrace_uml_TracedClass_uml_TracedBehavioredClassifier, gen_umlTrace_uml_TracedReadStructuralFeatureAction_TracedStructuralFeatureAction, gen_umlTrace_uml_TracedMergeNode_TracedControlNode, gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedAction, gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedNamespace, gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedActivityGroup, gen_umlTrace_uml_TracedAbstraction_TracedDependency, gen_umlTrace_uml_TracedPartDecomposition_TracedInteractionUse, gen_umlTrace_uml_TracedTypedElement_TracedNamedElement, gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedTemplateSignature, gen_umlTrace_uml_TracedCreateLinkAction_TracedWriteLinkAction, gen_umlTrace_uml_TracedGeneralization_TracedDirectedRelationship, gen_umlTrace_uml_TracedExtend_uml_TracedNamedElement, gen_umlTrace_uml_TracedExtend_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedOperationTemplateParameter_TracedTemplateParameter, gen_umlTrace_uml_TracedReadLinkObjectEndQualifierAction_TracedAction, gen_umlTrace_uml_TracedTemplateParameterSubstitution_TracedElement, gen_umlTrace_uml_TracedReadVariableAction_TracedVariableAction, gen_umlTrace_uml_TracedMessage_TracedNamedElement, gen_umlTrace_uml_TracedProfileApplication_TracedDirectedRelationship, gen_umlTrace_uml_TracedLiteralBoolean_TracedLiteralSpecification, gen_umlTrace_uml_TracedQualifierValue_TracedElement, gen_umlTrace_uml_TracedInitialNode_TracedControlNode, gen_umlTrace_uml_TracedLiteralInteger_TracedLiteralSpecification, gen_umlTrace_uml_TracedClearVariableAction_TracedVariableAction, gen_umlTrace_uml_TracedConnectorEnd_TracedMultiplicityElement, gen_umlTrace_uml_TracedParameterableElement_TracedElement, gen_umlTrace_uml_TracedTemplateParameter_TracedElement, gen_umlTrace_uml_TracedActionInputPin_TracedInputPin, gen_umlTrace_uml_TracedTrigger_TracedNamedElement, gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedOccurrenceSpecification, gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedMessageEnd, gen_umlTrace_uml_TracedDurationConstraint_TracedIntervalConstraint, gen_umlTrace_uml_TracedImage_TracedElement, gen_umlTrace_uml_TracedEncapsulatedClassifier_TracedStructuredClassifier, gen_umlTrace_uml_TracedParameter_uml_TracedConnectableElement, gen_umlTrace_uml_TracedParameter_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedIntervalConstraint_TracedConstraint, gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeploymentTarget, gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedPackageableElement, gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeployedArtifact, gen_umlTrace_uml_TracedCallOperationAction_TracedCallAction, gen_umlTrace_uml_TracedProfile_TracedPackage, gen_umlTrace_uml_TracedInterval_TracedValueSpecification, gen_umlTrace_uml_TracedProtocolStateMachine_TracedStateMachine, gen_umlTrace_uml_TracedOutputPin_TracedPin, gen_umlTrace_uml_TracedValuePin_TracedInputPin, gen_umlTrace_uml_TracedReadIsClassifiedObjectAction_TracedAction, gen_umlTrace_uml_TracedRegion_uml_TracedNamespace, gen_umlTrace_uml_TracedRegion_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedDecisionNode_TracedControlNode, gen_umlTrace_uml_TracedValueSpecificationAction_TracedAction, gen_umlTrace_uml_TracedDestroyLinkAction_TracedWriteLinkAction, gen_umlTrace_uml_TracedFinalState_TracedState, gen_umlTrace_uml_TracedActivityGroup_uml_TracedNamedElement, gen_umlTrace_uml_TracedInterruptibleActivityRegion_TracedActivityGroup, gen_umlTrace_uml_TracedActivityGroup_ActivityContent, gen_umlTrace_uml_TracedActivityEdge_TracedRedefinableElement, gen_umlTrace_uml_TracedInteractionOperand_uml_TracedNamespace, gen_umlTrace_uml_TracedInteractionOperand_uml_TracedInteractionFragment, gen_umlTrace_uml_TracedInformationFlow_uml_TracedPackageableElement, gen_umlTrace_uml_TracedInformationFlow_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedControlNode_TracedActivityNode, gen_umlTrace_uml_TracedUseCase_TracedBehavioredClassifier, gen_umlTrace_uml_TracedPseudostate_TracedVertex, gen_umlTrace_uml_TracedCombinedFragment_TracedInteractionFragment, gen_umlTrace_uml_TracedReplyAction_TracedAction, gen_umlTrace_uml_TracedDependency_uml_TracedPackageableElement, gen_umlTrace_uml_TracedDependency_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedWriteLinkAction_TracedLinkAction, gen_umlTrace_uml_TracedClause_TracedElement, gen_umlTrace_uml_TracedInstanceValue_TracedValueSpecification, gen_umlTrace_uml_TracedTransition_uml_TracedNamespace, gen_umlTrace_uml_TracedTransition_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedTimeExpression_TracedValueSpecification, gen_umlTrace_uml_TracedManifestation_TracedAbstraction, gen_umlTrace_uml_TracedReadExtentAction_TracedAction, gen_umlTrace_uml_TracedNode_uml_TracedClass, gen_umlTrace_uml_TracedNode_uml_TracedDeploymentTarget, gen_umlTrace_uml_TracedLinkEndData_TracedElement, gen_umlTrace_uml_TracedRedefinableElement_TracedNamedElement, gen_umlTrace_uml_TracedPackageMerge_TracedDirectedRelationship, gen_umlTrace_uml_TracedModel_TracedPackage, gen_umlTrace_uml_TracedObjectFlow_TracedActivityEdge, gen_umlTrace_uml_TracedEvent_TracedPackageableElement, gen_umlTrace_uml_TracedChangeEvent_TracedEvent, gen_umlTrace_uml_TracedStructuredClassifier_TracedClassifier, gen_umlTrace_uml_TracedDestroyObjectAction_TracedAction, gen_umlTrace_uml_TracedForkNode_TracedControlNode, gen_umlTrace_uml_TracedFinalNode_TracedControlNode, gen_umlTrace_uml_TracedSignal_TracedClassifier, gen_umlTrace_uml_TracedComment_TracedElement, gen_umlTrace_uml_TracedRaiseExceptionAction_TracedAction, gen_umlTrace_uml_TracedLiteralNull_TracedLiteralSpecification, gen_umlTrace_uml_TracedExpansionNode_TracedObjectNode, gen_umlTrace_uml_TracedReception_TracedBehavioralFeature, gen_umlTrace_uml_TracedPin_uml_TracedObjectNode, gen_umlTrace_uml_TracedPin_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedTestIdentityAction_TracedAction, gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedNamespace, gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedFeature, gen_umlTrace_uml_TracedAddVariableValueAction_TracedWriteVariableAction, gen_umlTrace_uml_TracedClearAssociationAction_TracedAction, gen_umlTrace_uml_TracedControlFlow_TracedActivityEdge, gen_umlTrace_uml_TracedOperation_uml_TracedBehavioralFeature, gen_umlTrace_uml_TracedOperation_uml_TracedParameterableElement, gen_umlTrace_uml_TracedOperation_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedObservation_TracedPackageableElement, gen_umlTrace_uml_TracedNamespace_TracedNamedElement, gen_umlTrace_uml_TracedConnectableElement_uml_TracedTypedElement, gen_umlTrace_uml_TracedConnectableElement_uml_TracedParameterableElement, gen_umlTrace_uml_TracedVertex_TracedNamedElement, gen_umlTrace_uml_TracedPackageImport_TracedDirectedRelationship, gen_umlTrace_uml_TracedInteractionUse_TracedInteractionFragment, gen_umlTrace_uml_TracedExecutionOccurrenceSpecification_TracedOccurrenceSpecification, gen_umlTrace_uml_TracedExceptionHandler_TracedElement, gen_umlTrace_uml_TracedVariable_uml_TracedConnectableElement, gen_umlTrace_uml_TracedVariable_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedStateInvariant_TracedInteractionFragment, gen_umlTrace_uml_TracedAssociation_uml_TracedClassifier, gen_umlTrace_uml_TracedAssociation_uml_TracedRelationship, gen_umlTrace_uml_TracedDevice_TracedNode, gen_umlTrace_uml_TracedSubstitution_TracedRealization, gen_umlTrace_uml_TracedLiteralReal_TracedLiteralSpecification, gen_umlTrace_uml_TracedInvocationAction_TracedAction, gen_umlTrace_uml_TracedRemoveVariableValueAction_TracedWriteVariableAction, gen_umlTrace_uml_TracedGate_TracedMessageEnd, gen_umlTrace_uml_TracedDeploymentTarget_TracedNamedElement, gen_umlTrace_uml_TracedGeneralOrdering_TracedNamedElement, gen_umlTrace_uml_TracedCallBehaviorAction_TracedCallAction, gen_umlTrace_uml_TracedReclassifyObjectAction_TracedAction, gen_umlTrace_uml_TracedConnectionPointReference_TracedVertex, gen_umlTrace_uml_TracedActivity_TracedBehavior, gen_umlTrace_uml_TracedLinkEndCreationData_TracedLinkEndData, gen_umlTrace_uml_TracedTemplateBinding_TracedDirectedRelationship, gen_umlTrace_uml_TracedActionExecutionSpecification_TracedExecutionSpecification, gen_umlTrace_uml_TracedReadSelfAction_TracedAction, gen_umlTrace_uml_TracedAcceptCallAction_TracedAcceptEventAction, gen_umlTrace_uml_TracedActor_TracedBehavioredClassifier, gen_umlTrace_uml_TracedBehaviorExecutionSpecification_TracedExecutionSpecification, gen_umlTrace_uml_TracedExecutableNode_TracedActivityNode, gen_umlTrace_uml_TracedClearStructuralFeatureAction_TracedStructuralFeatureAction, gen_umlTrace_uml_TracedOpaqueExpression_TracedValueSpecification, gen_umlTrace_uml_TracedFunctionBehavior_TracedOpaqueBehavior, gen_umlTrace_uml_TracedDeploymentSpecification_TracedArtifact, gen_umlTrace_uml_TracedUnmarshallAction_TracedAction, gen_umlTrace_uml_TracedCentralBufferNode_TracedObjectNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)