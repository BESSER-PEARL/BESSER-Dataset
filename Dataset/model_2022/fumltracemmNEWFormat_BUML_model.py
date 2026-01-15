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
umlTrace_Trace = Class(name="umlTrace::Trace")
umlTrace_State = Class(name="umlTrace::State")
Steps = Class(name="Steps")
TracedObjects = Class(name="TracedObjects")
SmallStep = Class(name="SmallStep")
BigStep = Class(name="BigStep")
IntegerValue_value_IntegerValue_Value = Class(name="IntegerValue::value::IntegerValue::Value")
ForkedToken_remainingOffersCount_Value = Class(name="ForkedToken::remainingOffersCount::Value")
ForkedToken_baseToken_Value = Class(name="ForkedToken::baseToken::Value")
ForkedToken_baseTokenIsWithdrawn_Value = Class(name="ForkedToken::baseTokenIsWithdrawn::Value")
ExecutionFactory_builtInTypes_Value = Class(name="ExecutionFactory::builtInTypes::Value")
ExecutionFactory_primitiveBehaviorPrototypes_Value = Class(name="ExecutionFactory::primitiveBehaviorPrototypes::Value")
ExecutionFactory_locus_ExecutionFactory_Value = Class(name="ExecutionFactory::locus::ExecutionFactory::Value")
Locus_factory_Value = Class(name="Locus::factory::Value")
Locus_extensionalValues_Value = Class(name="Locus::extensionalValues::Value")
Locus_executor_Value = Class(name="Locus::executor::Value")
ObjectNodeActivation_offeredTokenCount_Value = Class(name="ObjectNodeActivation::offeredTokenCount::Value")
SemanticVisitor_runtimeModelElement_Value = Class(name="SemanticVisitor::runtimeModelElement::Value")
ParameterValue_values_ParameterValue_Value = Class(name="ParameterValue::values::ParameterValue::Value")
Object_types_Value = Class(name="Object::types::Value")
Reference_referent_Value = Class(name="Reference::referent::Value")
Execution_parameterValues_Value = Class(name="Execution::parameterValues::Value")
Execution_context_Value = Class(name="Execution::context::Value")
Element_semanticVisitor_Value = Class(name="Element::semanticVisitor::Value")
ActivityNodeActivationGroup_nodeActivations_Value = Class(name="ActivityNodeActivationGroup::nodeActivations::Value")
ActivityNodeActivationGroup_activityExecution_Value = Class(name="ActivityNodeActivationGroup::activityExecution::Value")
ActivityNodeActivationGroup_edgeInstances_Value = Class(name="ActivityNodeActivationGroup::edgeInstances::Value")
Executor_locus_Executor_Value = Class(name="Executor::locus::Executor::Value")
PrimitiveValue_type_Value = Class(name="PrimitiveValue::type::Value")
Evaluation_specification_Evaluation_Value = Class(name="Evaluation::specification::Evaluation::Value")
Evaluation_locus_Evaluation_Value = Class(name="Evaluation::locus::Evaluation::Value")
BooleanValue_value_BooleanValue_Value = Class(name="BooleanValue::value::BooleanValue::Value")
ParameterValue_parameter_ParameterValue_Value = Class(name="ParameterValue::parameter::ParameterValue::Value")
ActionActivation_pinActivations_Value = Class(name="ActionActivation::pinActivations::Value")
ActionActivation_firing_Value = Class(name="ActionActivation::firing::Value")
Token_holder_Value = Class(name="Token::holder::Value")
Offer_offeredTokens_Value = Class(name="Offer::offeredTokens::Value")
FeatureValue_values_FeatureValue_Value = Class(name="FeatureValue::values::FeatureValue::Value")
FeatureValue_feature_Value = Class(name="FeatureValue::feature::Value")
FeatureValue_position_Value = Class(name="FeatureValue::position::Value")
PinActivation_actionActivation_Value = Class(name="PinActivation::actionActivation::Value")
PinActivation_count_temp_Value = Class(name="PinActivation::count::temp::Value")
ActivityEdgeInstance_group_ActivityEdgeInstance_Value = Class(name="ActivityEdgeInstance::group::ActivityEdgeInstance::Value")
ActivityEdgeInstance_offers_Value = Class(name="ActivityEdgeInstance::offers::Value")
ActivityEdgeInstance_target_Value = Class(name="ActivityEdgeInstance::target::Value")
ObjectToken_value_Value = Class(name="ObjectToken::value::Value")
CallActionActivation_callExecutions_Value = Class(name="CallActionActivation::callExecutions::Value")
CompoundValue_featureValues_Value = Class(name="CompoundValue::featureValues::Value")
InputParameterValues_name_Value = Class(name="InputParameterValues::name::Value")
InputParameterValues_parameterValues_Value = Class(name="InputParameterValues::parameterValues::Value")
ActivityNodeActivation_heldTokens_Value = Class(name="ActivityNodeActivation::heldTokens::Value")
ActivityNodeActivation_node_ActivityNodeActivation_Value = Class(name="ActivityNodeActivation::node::ActivityNodeActivation::Value")
ActivityNodeActivation_running_Value = Class(name="ActivityNodeActivation::running::Value")
ActivityNodeActivation_isRunning_Value = Class(name="ActivityNodeActivation::isRunning::Value")
ActivityNodeActivation_outgoingEdges_Value = Class(name="ActivityNodeActivation::outgoingEdges::Value")
ActivityNodeActivation_incomingEdges_Value = Class(name="ActivityNodeActivation::incomingEdges::Value")
ActivityNodeActivation_group_ActivityNodeActivation_Value = Class(name="ActivityNodeActivation::group::ActivityNodeActivation::Value")
ExtensionalValue_locus_ExtensionalValue_Value = Class(name="ExtensionalValue::locus::ExtensionalValue::Value")
ActivityEdgeInstance_edge_ActivityEdgeInstance_Value = Class(name="ActivityEdgeInstance::edge::ActivityEdgeInstance::Value")
ActivityEdgeInstance_source_Value = Class(name="ActivityEdgeInstance::source::Value")
ActivityExecution_activationGroup_Value = Class(name="ActivityExecution::activationGroup::Value")
ExecutionEnvironment_locus_ExecutionEnvironment_Value = Class(name="ExecutionEnvironment::locus::ExecutionEnvironment::Value")
umlTrace_Steps_SmallStep = Class(name="umlTrace::Steps::SmallStep", is_abstract=True)
Steps_umlTrace_State = Class(name="Steps::umlTrace::State")
umlTrace_Steps_Steps = Class(name="umlTrace::Steps::Steps")
umlTrace_Steps_BigStep = Class(name="umlTrace::Steps::BigStep", is_abstract=True)
umlTrace_Values_Object_types_Value = Class(name="umlTrace::Values::Object::types::Value")
uml_TracedClass = Class(name="uml::TracedClass")
Kernel_TracedObject = Class(name="Kernel::TracedObject")
Values_umlTrace_State = Class(name="Values::umlTrace::State")
umlTrace_Values_Reference_referent_Value = Class(name="umlTrace::Values::Reference::referent::Value")
umlTrace_Values_IntegerValue_value_IntegerValue_Value = Class(name="umlTrace::Values::IntegerValue::value::IntegerValue::Value")
Kernel_TracedIntegerValue = Class(name="Kernel::TracedIntegerValue")
umlTrace_Values_ForkedToken_remainingOffersCount_Value = Class(name="umlTrace::Values::ForkedToken::remainingOffersCount::Value")
IntermediateActivities_TracedForkedToken = Class(name="IntermediateActivities::TracedForkedToken")
umlTrace_Values_ForkedToken_baseToken_Value = Class(name="umlTrace::Values::ForkedToken::baseToken::Value")
IntermediateActivities_TracedToken = Class(name="IntermediateActivities::TracedToken")
umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value = Class(name="umlTrace::Values::ForkedToken::baseTokenIsWithdrawn::Value")
Kernel_TracedReference = Class(name="Kernel::TracedReference")
umlTrace_Values_ExecutionFactory_builtInTypes_Value = Class(name="umlTrace::Values::ExecutionFactory::builtInTypes::Value")
uml_TracedPrimitiveType = Class(name="uml::TracedPrimitiveType")
Loci_TracedExecutionFactory = Class(name="Loci::TracedExecutionFactory")
umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value = Class(name="umlTrace::Values::ExecutionFactory::primitiveBehaviorPrototypes::Value")
BasicBehaviors_TracedOpaqueBehaviorExecution = Class(name="BasicBehaviors::TracedOpaqueBehaviorExecution")
umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value = Class(name="umlTrace::Values::ExecutionFactory::locus::ExecutionFactory::Value")
Loci_TracedLocus = Class(name="Loci::TracedLocus")
umlTrace_Values_Locus_factory_Value = Class(name="umlTrace::Values::Locus::factory::Value")
umlTrace_Values_Locus_extensionalValues_Value = Class(name="umlTrace::Values::Locus::extensionalValues::Value")
Kernel_TracedExtensionalValue = Class(name="Kernel::TracedExtensionalValue")
umlTrace_Values_Locus_executor_Value = Class(name="umlTrace::Values::Locus::executor::Value")
Loci_TracedExecutor = Class(name="Loci::TracedExecutor")
umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value = Class(name="umlTrace::Values::ObjectNodeActivation::offeredTokenCount::Value")
IntermediateActivities_TracedObjectNodeActivation = Class(name="IntermediateActivities::TracedObjectNodeActivation")
umlTrace_Values_SemanticVisitor_runtimeModelElement_Value = Class(name="umlTrace::Values::SemanticVisitor::runtimeModelElement::Value")
uml_TracedElement = Class(name="uml::TracedElement")
umlTrace_Values_ParameterValue_values_ParameterValue_Value = Class(name="umlTrace::Values::ParameterValue::values::ParameterValue::Value")
Kernel_TracedValue = Class(name="Kernel::TracedValue")
BasicBehaviors_TracedParameterValue = Class(name="BasicBehaviors::TracedParameterValue")
umlTrace_Values_ParameterValue_parameter_ParameterValue_Value = Class(name="umlTrace::Values::ParameterValue::parameter::ParameterValue::Value")
uml_TracedParameter = Class(name="uml::TracedParameter")
umlTrace_Values_ActionActivation_pinActivations_Value = Class(name="umlTrace::Values::ActionActivation::pinActivations::Value")
BasicActions_TracedPinActivation = Class(name="BasicActions::TracedPinActivation")
BasicActions_TracedActionActivation = Class(name="BasicActions::TracedActionActivation")
Loci_TracedSemanticVisitor = Class(name="Loci::TracedSemanticVisitor")
umlTrace_Values_Execution_parameterValues_Value = Class(name="umlTrace::Values::Execution::parameterValues::Value")
BasicBehaviors_TracedExecution = Class(name="BasicBehaviors::TracedExecution")
umlTrace_Values_Execution_context_Value = Class(name="umlTrace::Values::Execution::context::Value")
umlTrace_Values_Element_semanticVisitor_Value = Class(name="umlTrace::Values::Element::semanticVisitor::Value")
umlTrace_Values_ActionActivation_firing_Value = Class(name="umlTrace::Values::ActionActivation::firing::Value")
IntermediateActivities_TracedActivityNodeActivationGroup = Class(name="IntermediateActivities::TracedActivityNodeActivationGroup")
umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value = Class(name="umlTrace::Values::ActivityNodeActivationGroup::activityExecution::Value")
IntermediateActivities_TracedActivityExecution = Class(name="IntermediateActivities::TracedActivityExecution")
umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value = Class(name="umlTrace::Values::ActivityNodeActivationGroup::edgeInstances::Value")
IntermediateActivities_TracedActivityEdgeInstance = Class(name="IntermediateActivities::TracedActivityEdgeInstance")
umlTrace_Values_Executor_locus_Executor_Value = Class(name="umlTrace::Values::Executor::locus::Executor::Value")
umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value = Class(name="umlTrace::Values::ActivityNodeActivationGroup::nodeActivations::Value")
IntermediateActivities_TracedActivityNodeActivation = Class(name="IntermediateActivities::TracedActivityNodeActivation")
Kernel_TracedPrimitiveValue = Class(name="Kernel::TracedPrimitiveValue")
umlTrace_Values_Evaluation_specification_Evaluation_Value = Class(name="umlTrace::Values::Evaluation::specification::Evaluation::Value")
uml_TracedValueSpecification = Class(name="uml::TracedValueSpecification")
Kernel_TracedEvaluation = Class(name="Kernel::TracedEvaluation")
umlTrace_Values_Evaluation_locus_Evaluation_Value = Class(name="umlTrace::Values::Evaluation::locus::Evaluation::Value")
umlTrace_Values_BooleanValue_value_BooleanValue_Value = Class(name="umlTrace::Values::BooleanValue::value::BooleanValue::Value")
Kernel_TracedBooleanValue = Class(name="Kernel::TracedBooleanValue")
umlTrace_Values_PrimitiveValue_type_Value = Class(name="umlTrace::Values::PrimitiveValue::type::Value")
IntermediateActivities_TracedObjectToken = Class(name="IntermediateActivities::TracedObjectToken")
umlTrace_Values_CallActionActivation_callExecutions_Value = Class(name="umlTrace::Values::CallActionActivation::callExecutions::Value")
BasicActions_TracedCallActionActivation = Class(name="BasicActions::TracedCallActionActivation")
umlTrace_Values_CompoundValue_featureValues_Value = Class(name="umlTrace::Values::CompoundValue::featureValues::Value")
Kernel_TracedFeatureValue = Class(name="Kernel::TracedFeatureValue")
Kernel_TracedCompoundValue = Class(name="Kernel::TracedCompoundValue")
umlTrace_Values_Token_holder_Value = Class(name="umlTrace::Values::Token::holder::Value")
umlTrace_Values_ObjectToken_value_Value = Class(name="umlTrace::Values::ObjectToken::value::Value")
IntermediateActivities_TracedOffer = Class(name="IntermediateActivities::TracedOffer")
umlTrace_Values_FeatureValue_values_FeatureValue_Value = Class(name="umlTrace::Values::FeatureValue::values::FeatureValue::Value")
umlTrace_Values_FeatureValue_feature_Value = Class(name="umlTrace::Values::FeatureValue::feature::Value")
uml_TracedStructuralFeature = Class(name="uml::TracedStructuralFeature")
umlTrace_Values_FeatureValue_position_Value = Class(name="umlTrace::Values::FeatureValue::position::Value")
umlTrace_Values_Offer_offeredTokens_Value = Class(name="umlTrace::Values::Offer::offeredTokens::Value")
umlTrace_Values_PinActivation_count_temp_Value = Class(name="umlTrace::Values::PinActivation::count::temp::Value")
umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value = Class(name="umlTrace::Values::ActivityEdgeInstance::group::ActivityEdgeInstance::Value")
umlTrace_Values_ActivityEdgeInstance_offers_Value = Class(name="umlTrace::Values::ActivityEdgeInstance::offers::Value")
umlTrace_Values_PinActivation_actionActivation_Value = Class(name="umlTrace::Values::PinActivation::actionActivation::Value")
umlTrace_Values_ActivityEdgeInstance_target_Value = Class(name="umlTrace::Values::ActivityEdgeInstance::target::Value")
umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value = Class(name="umlTrace::Values::ActivityEdgeInstance::edge::ActivityEdgeInstance::Value")
uml_TracedActivityEdge = Class(name="uml::TracedActivityEdge")
umlTrace_Values_ActivityEdgeInstance_source_Value = Class(name="umlTrace::Values::ActivityEdgeInstance::source::Value")
umlTrace_Values_InputParameterValues_parameterValues_Value = Class(name="umlTrace::Values::InputParameterValues::parameterValues::Value")
umlTrace_Values_ActivityNodeActivation_heldTokens_Value = Class(name="umlTrace::Values::ActivityNodeActivation::heldTokens::Value")
umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value = Class(name="umlTrace::Values::ActivityNodeActivation::node::ActivityNodeActivation::Value")
uml_TracedActivityNode = Class(name="uml::TracedActivityNode")
umlTrace_Values_InputParameterValues_name_Value = Class(name="umlTrace::Values::InputParameterValues::name::Value")
Input_TracedInputParameterValues = Class(name="Input::TracedInputParameterValues")
umlTrace_Values_ActivityNodeActivation_isRunning_Value = Class(name="umlTrace::Values::ActivityNodeActivation::isRunning::Value")
umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value = Class(name="umlTrace::Values::ActivityNodeActivation::outgoingEdges::Value")
umlTrace_Values_ActivityNodeActivation_incomingEdges_Value = Class(name="umlTrace::Values::ActivityNodeActivation::incomingEdges::Value")
umlTrace_Values_ActivityNodeActivation_running_Value = Class(name="umlTrace::Values::ActivityNodeActivation::running::Value")
umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value = Class(name="umlTrace::Values::ExtensionalValue::locus::ExtensionalValue::Value")
umlTrace_Values_ActivityExecution_activationGroup_Value = Class(name="umlTrace::Values::ActivityExecution::activationGroup::Value")
umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value = Class(name="umlTrace::Values::ExecutionEnvironment::locus::ExecutionEnvironment::Value")
umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value = Class(name="umlTrace::Values::ActivityNodeActivation::group::ActivityNodeActivation::Value")
umlTrace_Traced_TracedObjects = Class(name="umlTrace::Traced::TracedObjects")
uml_TracedConnector = Class(name="uml::TracedConnector")
uml_TracedOpaqueAction = Class(name="uml::TracedOpaqueAction")
uml_TracedDataType = Class(name="uml::TracedDataType")
uml_TracedCommunicationPath = Class(name="uml::TracedCommunicationPath")
uml_TracedProperty = Class(name="uml::TracedProperty")
uml_TracedContinuation = Class(name="uml::TracedContinuation")
uml_TracedRemoveStructuralFeatureValueAction = Class(name="uml::TracedRemoveStructuralFeatureValueAction")
uml_TracedSendSignalAction = Class(name="uml::TracedSendSignalAction")
Loci_TracedExecutionEnvironment = Class(name="Loci::TracedExecutionEnvironment")
uml_TracedArtifact = Class(name="uml::TracedArtifact")
IntermediateActivities_TracedJoinNodeActivation = Class(name="IntermediateActivities::TracedJoinNodeActivation")
uml_TracedTimeConstraint = Class(name="uml::TracedTimeConstraint")
uml_TracedInterfaceRealization = Class(name="uml::TracedInterfaceRealization")
uml_TracedActivityFinalNode = Class(name="uml::TracedActivityFinalNode")
uml_TracedDurationObservation = Class(name="uml::TracedDurationObservation")
IntermediateActivities_TracedInitialNodeActivation = Class(name="IntermediateActivities::TracedInitialNodeActivation")
uml_TracedAcceptEventAction = Class(name="uml::TracedAcceptEventAction")
uml_TracedEnumerationLiteral = Class(name="uml::TracedEnumerationLiteral")
uml_TracedAddStructuralFeatureValueAction = Class(name="uml::TracedAddStructuralFeatureValueAction")
uml_TracedOpaqueBehavior = Class(name="uml::TracedOpaqueBehavior")
uml_TracedConsiderIgnoreFragment = Class(name="uml::TracedConsiderIgnoreFragment")
uml_TracedDataStoreNode = Class(name="uml::TracedDataStoreNode")
uml_TracedFlowFinalNode = Class(name="uml::TracedFlowFinalNode")
uml_TracedInformationItem = Class(name="uml::TracedInformationItem")
uml_TracedCollaboration = Class(name="uml::TracedCollaboration")
uml_TracedTemplateSignature = Class(name="uml::TracedTemplateSignature")
uml_TracedBroadcastSignalAction = Class(name="uml::TracedBroadcastSignalAction")
uml_TracedDeployment = Class(name="uml::TracedDeployment")
uml_TracedPort = Class(name="uml::TracedPort")
uml_TracedTimeInterval = Class(name="uml::TracedTimeInterval")
uml_TracedExtension = Class(name="uml::TracedExtension")
uml_TracedReadLinkAction = Class(name="uml::TracedReadLinkAction")
uml_TracedExpression = Class(name="uml::TracedExpression")
uml_TracedProtocolTransition = Class(name="uml::TracedProtocolTransition")
IntermediateActivities_TracedActivityFinalNodeActivation = Class(name="IntermediateActivities::TracedActivityFinalNodeActivation")
uml_TracedPackage = Class(name="uml::TracedPackage")
uml_TracedConstraint = Class(name="uml::TracedConstraint")
uml_TracedGeneralizationSet = Class(name="uml::TracedGeneralizationSet")
uml_TracedReduceAction = Class(name="uml::TracedReduceAction")
uml_TracedInputPin = Class(name="uml::TracedInputPin")
uml_TracedSequenceNode = Class(name="uml::TracedSequenceNode")
uml_TracedTimeEvent = Class(name="uml::TracedTimeEvent")
uml_TracedAssociationClass = Class(name="uml::TracedAssociationClass")
uml_TracedSlot = Class(name="uml::TracedSlot")
uml_TracedSignalEvent = Class(name="uml::TracedSignalEvent")
uml_TracedExtensionPoint = Class(name="uml::TracedExtensionPoint")
uml_TracedJoinNode = Class(name="uml::TracedJoinNode")
BasicActions_TracedOutputPinActivation = Class(name="BasicActions::TracedOutputPinActivation")
uml_TracedStartObjectBehaviorAction = Class(name="uml::TracedStartObjectBehaviorAction")
uml_TracedElementImport = Class(name="uml::TracedElementImport")
uml_TracedCreateObjectAction = Class(name="uml::TracedCreateObjectAction")
uml_TracedInteractionConstraint = Class(name="uml::TracedInteractionConstraint")
uml_TracedComponentRealization = Class(name="uml::TracedComponentRealization")
IntermediateActions_TracedValueSpecificationActionActivation = Class(name="IntermediateActions::TracedValueSpecificationActionActivation")
uml_TracedStringExpression = Class(name="uml::TracedStringExpression")
IntermediateActions_TracedReadStructuralFeatureActionActivation = Class(name="IntermediateActions::TracedReadStructuralFeatureActionActivation")
uml_TracedStereotype = Class(name="uml::TracedStereotype")
uml_TracedInterface = Class(name="uml::TracedInterface")
uml_TracedConditionalNode = Class(name="uml::TracedConditionalNode")
uml_TracedExecutionEnvironment = Class(name="uml::TracedExecutionEnvironment")
uml_TracedOccurrenceSpecification = Class(name="uml::TracedOccurrenceSpecification")
uml_TracedComponent = Class(name="uml::TracedComponent")
uml_TracedExtensionEnd = Class(name="uml::TracedExtensionEnd")
uml_TracedStateMachine = Class(name="uml::TracedStateMachine")
IntermediateActivities_TracedMergeNodeActivation = Class(name="IntermediateActivities::TracedMergeNodeActivation")
uml_TracedInteraction = Class(name="uml::TracedInteraction")
uml_TracedLiteralString = Class(name="uml::TracedLiteralString")
uml_TracedRealization = Class(name="uml::TracedRealization")
uml_TracedReadLinkObjectEndAction = Class(name="uml::TracedReadLinkObjectEndAction")
uml_TracedAnyReceiveEvent = Class(name="uml::TracedAnyReceiveEvent")
uml_TracedConnectableElementTemplateParameter = Class(name="uml::TracedConnectableElementTemplateParameter")
uml_TracedSendObjectAction = Class(name="uml::TracedSendObjectAction")
uml_TracedLifeline = Class(name="uml::TracedLifeline")
uml_TracedTimeObservation = Class(name="uml::TracedTimeObservation")
IntermediateActivities_TracedControlToken = Class(name="IntermediateActivities::TracedControlToken")
uml_TracedCreateLinkObjectAction = Class(name="uml::TracedCreateLinkObjectAction")
uml_TracedExpansionRegion = Class(name="uml::TracedExpansionRegion")
uml_TracedStartClassifierBehaviorAction = Class(name="uml::TracedStartClassifierBehaviorAction")
uml_TracedCallEvent = Class(name="uml::TracedCallEvent")
uml_TracedProtocolConformance = Class(name="uml::TracedProtocolConformance")
uml_TracedEnumeration = Class(name="uml::TracedEnumeration")
uml_TracedCollaborationUse = Class(name="uml::TracedCollaborationUse")
uml_TracedActivityPartition = Class(name="uml::TracedActivityPartition")
uml_TracedLinkEndDestructionData = Class(name="uml::TracedLinkEndDestructionData")
uml_TracedDurationInterval = Class(name="uml::TracedDurationInterval")
uml_TracedLoopNode = Class(name="uml::TracedLoopNode")
uml_TracedState = Class(name="uml::TracedState")
BasicActions_TracedCallBehaviorActionActivation = Class(name="BasicActions::TracedCallBehaviorActionActivation")
IntermediateActions_TracedAddStructuralFeatureValueActionActivation = Class(name="IntermediateActions::TracedAddStructuralFeatureValueActionActivation")
uml_TracedClassifierTemplateParameter = Class(name="uml::TracedClassifierTemplateParameter")
uml_TracedActivityParameterNode = Class(name="uml::TracedActivityParameterNode")
IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution = Class(name="IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution")
uml_TracedInclude = Class(name="uml::TracedInclude")
uml_TracedDestructionOccurrenceSpecification = Class(name="uml::TracedDestructionOccurrenceSpecification")
uml_TracedDuration = Class(name="uml::TracedDuration")
uml_TracedUsage = Class(name="uml::TracedUsage")
uml_TracedLiteralUnlimitedNatural = Class(name="uml::TracedLiteralUnlimitedNatural")
uml_TracedStructuredActivityNode = Class(name="uml::TracedStructuredActivityNode")
uml_TracedAbstraction = Class(name="uml::TracedAbstraction")
BasicActions_TracedOpaqueActionActivation = Class(name="BasicActions::TracedOpaqueActionActivation")
uml_TracedParameterSet = Class(name="uml::TracedParameterSet")
uml_TracedReadStructuralFeatureAction = Class(name="uml::TracedReadStructuralFeatureAction")
uml_TracedMergeNode = Class(name="uml::TracedMergeNode")
uml_TracedRedefinableTemplateSignature = Class(name="uml::TracedRedefinableTemplateSignature")
uml_TracedCreateLinkAction = Class(name="uml::TracedCreateLinkAction")
uml_TracedGeneralization = Class(name="uml::TracedGeneralization")
uml_TracedPartDecomposition = Class(name="uml::TracedPartDecomposition")
Kernel_TracedLiteralBooleanEvaluation = Class(name="Kernel::TracedLiteralBooleanEvaluation")
uml_TracedReadLinkObjectEndQualifierAction = Class(name="uml::TracedReadLinkObjectEndQualifierAction")
uml_TracedTemplateParameterSubstitution = Class(name="uml::TracedTemplateParameterSubstitution")
uml_TracedExtend = Class(name="uml::TracedExtend")
uml_TracedReadVariableAction = Class(name="uml::TracedReadVariableAction")
uml_TracedMessage = Class(name="uml::TracedMessage")
uml_TracedOperationTemplateParameter = Class(name="uml::TracedOperationTemplateParameter")
uml_TracedInitialNode = Class(name="uml::TracedInitialNode")
uml_TracedLiteralInteger = Class(name="uml::TracedLiteralInteger")
uml_TracedClearVariableAction = Class(name="uml::TracedClearVariableAction")
IntermediateActivities_TracedDecisionNodeActivation = Class(name="IntermediateActivities::TracedDecisionNodeActivation")
uml_TracedProfileApplication = Class(name="uml::TracedProfileApplication")
uml_TracedTemplateParameter = Class(name="uml::TracedTemplateParameter")
uml_TracedLiteralBoolean = Class(name="uml::TracedLiteralBoolean")
uml_TracedQualifierValue = Class(name="uml::TracedQualifierValue")
uml_TracedMessageOccurrenceSpecification = Class(name="uml::TracedMessageOccurrenceSpecification")
uml_TracedDurationConstraint = Class(name="uml::TracedDurationConstraint")
uml_TracedImage = Class(name="uml::TracedImage")
uml_TracedActionInputPin = Class(name="uml::TracedActionInputPin")
uml_TracedTrigger = Class(name="uml::TracedTrigger")
uml_TracedConnectorEnd = Class(name="uml::TracedConnectorEnd")
uml_TracedProfile = Class(name="uml::TracedProfile")
uml_TracedInterval = Class(name="uml::TracedInterval")
IntermediateActivities_TracedForkNodeActivation = Class(name="IntermediateActivities::TracedForkNodeActivation")
uml_TracedIntervalConstraint = Class(name="uml::TracedIntervalConstraint")
uml_TracedInstanceSpecification = Class(name="uml::TracedInstanceSpecification")
uml_TracedCallOperationAction = Class(name="uml::TracedCallOperationAction")
IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution = Class(name="IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution")
uml_TracedReadIsClassifiedObjectAction = Class(name="uml::TracedReadIsClassifiedObjectAction")
uml_TracedProtocolStateMachine = Class(name="uml::TracedProtocolStateMachine")
uml_TracedOutputPin = Class(name="uml::TracedOutputPin")
uml_TracedValuePin = Class(name="uml::TracedValuePin")
uml_TracedDecisionNode = Class(name="uml::TracedDecisionNode")
uml_TracedValueSpecificationAction = Class(name="uml::TracedValueSpecificationAction")
uml_TracedRegion = Class(name="uml::TracedRegion")
uml_TracedInterruptibleActivityRegion = Class(name="uml::TracedInterruptibleActivityRegion")
uml_TracedDestroyLinkAction = Class(name="uml::TracedDestroyLinkAction")
IntermediateActivities_TracedActivityParameterNodeActivation = Class(name="IntermediateActivities::TracedActivityParameterNodeActivation")
uml_TracedInteractionOperand = Class(name="uml::TracedInteractionOperand")
uml_TracedInformationFlow = Class(name="uml::TracedInformationFlow")
uml_TracedPseudostate = Class(name="uml::TracedPseudostate")
uml_TracedUseCase = Class(name="uml::TracedUseCase")
uml_TracedReplyAction = Class(name="uml::TracedReplyAction")
uml_TracedFinalState = Class(name="uml::TracedFinalState")
IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution = Class(name="IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution")
uml_TracedCombinedFragment = Class(name="uml::TracedCombinedFragment")
uml_TracedClause = Class(name="uml::TracedClause")
uml_TracedInstanceValue = Class(name="uml::TracedInstanceValue")
uml_TracedDependency = Class(name="uml::TracedDependency")
uml_TracedTimeExpression = Class(name="uml::TracedTimeExpression")
IntermediateActions_TracedCreateObjectActionActivation = Class(name="IntermediateActions::TracedCreateObjectActionActivation")
uml_TracedManifestation = Class(name="uml::TracedManifestation")
uml_TracedReadExtentAction = Class(name="uml::TracedReadExtentAction")
BasicActions_TracedInputPinActivation = Class(name="BasicActions::TracedInputPinActivation")
uml_TracedTransition = Class(name="uml::TracedTransition")
uml_TracedLinkEndData = Class(name="uml::TracedLinkEndData")
uml_TracedNode = Class(name="uml::TracedNode")
uml_TracedPackageMerge = Class(name="uml::TracedPackageMerge")
uml_TracedModel = Class(name="uml::TracedModel")
uml_TracedObjectFlow = Class(name="uml::TracedObjectFlow")
uml_TracedChangeEvent = Class(name="uml::TracedChangeEvent")
uml_TracedForkNode = Class(name="uml::TracedForkNode")
uml_TracedSignal = Class(name="uml::TracedSignal")
uml_TracedComment = Class(name="uml::TracedComment")
uml_TracedLiteralNull = Class(name="uml::TracedLiteralNull")
uml_TracedExpansionNode = Class(name="uml::TracedExpansionNode")
uml_TracedDestroyObjectAction = Class(name="uml::TracedDestroyObjectAction")
uml_TracedRaiseExceptionAction = Class(name="uml::TracedRaiseExceptionAction")
uml_TracedAddVariableValueAction = Class(name="uml::TracedAddVariableValueAction")
uml_TracedClearAssociationAction = Class(name="uml::TracedClearAssociationAction")
uml_TracedTestIdentityAction = Class(name="uml::TracedTestIdentityAction")
uml_TracedReception = Class(name="uml::TracedReception")
uml_TracedOperation = Class(name="uml::TracedOperation")
uml_TracedPackageImport = Class(name="uml::TracedPackageImport")
uml_TracedExecutionOccurrenceSpecification = Class(name="uml::TracedExecutionOccurrenceSpecification")
uml_TracedExceptionHandler = Class(name="uml::TracedExceptionHandler")
uml_TracedVariable = Class(name="uml::TracedVariable")
uml_TracedControlFlow = Class(name="uml::TracedControlFlow")
uml_TracedAssociation = Class(name="uml::TracedAssociation")
uml_TracedStateInvariant = Class(name="uml::TracedStateInvariant")
uml_TracedLiteralReal = Class(name="uml::TracedLiteralReal")
uml_TracedRemoveVariableValueAction = Class(name="uml::TracedRemoveVariableValueAction")
uml_TracedInteractionUse = Class(name="uml::TracedInteractionUse")
uml_TracedGate = Class(name="uml::TracedGate")
uml_TracedGeneralOrdering = Class(name="uml::TracedGeneralOrdering")
uml_TracedCallBehaviorAction = Class(name="uml::TracedCallBehaviorAction")
uml_TracedReclassifyObjectAction = Class(name="uml::TracedReclassifyObjectAction")
uml_TracedDevice = Class(name="uml::TracedDevice")
uml_TracedSubstitution = Class(name="uml::TracedSubstitution")
uml_TracedConnectionPointReference = Class(name="uml::TracedConnectionPointReference")
uml_TracedActionExecutionSpecification = Class(name="uml::TracedActionExecutionSpecification")
uml_TracedReadSelfAction = Class(name="uml::TracedReadSelfAction")
uml_TracedAcceptCallAction = Class(name="uml::TracedAcceptCallAction")
uml_TracedActivity = Class(name="uml::TracedActivity")
uml_TracedTemplateBinding = Class(name="uml::TracedTemplateBinding")
uml_TracedClearStructuralFeatureAction = Class(name="uml::TracedClearStructuralFeatureAction")
uml_TracedLinkEndCreationData = Class(name="uml::TracedLinkEndCreationData")
Kernel_TracedLiteralIntegerEvaluation = Class(name="Kernel::TracedLiteralIntegerEvaluation")
uml_TracedOpaqueExpression = Class(name="uml::TracedOpaqueExpression")
uml_TracedFunctionBehavior = Class(name="uml::TracedFunctionBehavior")
uml_TracedDeploymentSpecification = Class(name="uml::TracedDeploymentSpecification")
uml_TracedBehaviorExecutionSpecification = Class(name="uml::TracedBehaviorExecutionSpecification")
uml_TracedUnmarshallAction = Class(name="uml::TracedUnmarshallAction")
uml_TracedCentralBufferNode = Class(name="uml::TracedCentralBufferNode")
umlTrace_Kernel_TracedObject = Class(name="umlTrace::Kernel::TracedObject")
TracedExtensionalValue = Class(name="TracedExtensionalValue")
uml_TracedActor = Class(name="uml::TracedActor")
umlTrace_Kernel_TracedIntegerValue = Class(name="umlTrace::Kernel::TracedIntegerValue")
TracedPrimitiveValue = Class(name="TracedPrimitiveValue")
umlTrace_Kernel_TracedLiteralEvaluation = Class(name="umlTrace::Kernel::TracedLiteralEvaluation", is_abstract=True)
TracedEvaluation = Class(name="TracedEvaluation")
umlTrace_Kernel_TracedValue = Class(name="umlTrace::Kernel::TracedValue", is_abstract=True)
TracedSemanticVisitor = Class(name="TracedSemanticVisitor")
umlTrace_Kernel_TracedPrimitiveValue = Class(name="umlTrace::Kernel::TracedPrimitiveValue", is_abstract=True)
TracedValue = Class(name="TracedValue")
umlTrace_Kernel_TracedEvaluation = Class(name="umlTrace::Kernel::TracedEvaluation", is_abstract=True)
umlTrace_Kernel_TracedBooleanValue = Class(name="umlTrace::Kernel::TracedBooleanValue")
umlTrace_Kernel_TracedLiteralBooleanEvaluation = Class(name="umlTrace::Kernel::TracedLiteralBooleanEvaluation")
TracedLiteralEvaluation = Class(name="TracedLiteralEvaluation")
umlTrace_Kernel_TracedReference = Class(name="umlTrace::Kernel::TracedReference")
TracedStructuredValue = Class(name="TracedStructuredValue")
umlTrace_Kernel_TracedCompoundValue = Class(name="umlTrace::Kernel::TracedCompoundValue", is_abstract=True)
umlTrace_Kernel_TracedFeatureValue = Class(name="umlTrace::Kernel::TracedFeatureValue", is_abstract=True)
umlTrace_Kernel_TracedStructuredValue = Class(name="umlTrace::Kernel::TracedStructuredValue", is_abstract=True)
umlTrace_Kernel_TracedExtensionalValue = Class(name="umlTrace::Kernel::TracedExtensionalValue", is_abstract=True)
TracedCompoundValue = Class(name="TracedCompoundValue")
umlTrace_Kernel_TracedLiteralIntegerEvaluation = Class(name="umlTrace::Kernel::TracedLiteralIntegerEvaluation")
umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution = Class(name="umlTrace::BasicBehaviors::TracedOpaqueBehaviorExecution", is_abstract=True)
TracedExecution = Class(name="TracedExecution")
umlTrace_BasicBehaviors_TracedParameterValue = Class(name="umlTrace::BasicBehaviors::TracedParameterValue")
umlTrace_BasicBehaviors_TracedExecution = Class(name="umlTrace::BasicBehaviors::TracedExecution", is_abstract=True)
TracedObject = Class(name="TracedObject")
umlTrace_IntermediateActivities_TracedForkedToken = Class(name="umlTrace::IntermediateActivities::TracedForkedToken")
TracedToken = Class(name="TracedToken")
umlTrace_IntermediateActivities_TracedJoinNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedJoinNodeActivation")
TracedControlNodeActivation = Class(name="TracedControlNodeActivation")
umlTrace_IntermediateActivities_TracedInitialNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedInitialNodeActivation")
umlTrace_IntermediateActivities_TracedObjectNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedObjectNodeActivation", is_abstract=True)
TracedActivityNodeActivation = Class(name="TracedActivityNodeActivation")
umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedActivityFinalNodeActivation")
umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup = Class(name="umlTrace::IntermediateActivities::TracedActivityNodeActivationGroup")
umlTrace_IntermediateActivities_TracedMergeNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedMergeNodeActivation")
umlTrace_IntermediateActivities_TracedControlToken = Class(name="umlTrace::IntermediateActivities::TracedControlToken")
umlTrace_IntermediateActivities_TracedObjectToken = Class(name="umlTrace::IntermediateActivities::TracedObjectToken")
umlTrace_IntermediateActivities_TracedDecisionNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedDecisionNodeActivation")
umlTrace_IntermediateActivities_TracedOffer = Class(name="umlTrace::IntermediateActivities::TracedOffer")
umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedActivityParameterNodeActivation")
TracedObjectNodeActivation = Class(name="TracedObjectNodeActivation")
umlTrace_IntermediateActivities_TracedActivityEdgeInstance = Class(name="umlTrace::IntermediateActivities::TracedActivityEdgeInstance")
umlTrace_IntermediateActivities_TracedActivityNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedActivityNodeActivation")
umlTrace_IntermediateActivities_TracedForkNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedForkNodeActivation")
umlTrace_IntermediateActivities_TracedToken = Class(name="umlTrace::IntermediateActivities::TracedToken")
umlTrace_IntermediateActivities_TracedActivityExecution = Class(name="umlTrace::IntermediateActivities::TracedActivityExecution")
umlTrace_Loci_TracedExecutionFactory = Class(name="umlTrace::Loci::TracedExecutionFactory")
umlTrace_Loci_TracedLocus = Class(name="umlTrace::Loci::TracedLocus")
umlTrace_Loci_TracedSemanticVisitor = Class(name="umlTrace::Loci::TracedSemanticVisitor")
umlTrace_Loci_TracedExecutor = Class(name="umlTrace::Loci::TracedExecutor")
umlTrace_IntermediateActivities_TracedControlNodeActivation = Class(name="umlTrace::IntermediateActivities::TracedControlNodeActivation", is_abstract=True)
umlTrace_IntermediateActions_TracedValueSpecificationActionActivation = Class(name="umlTrace::IntermediateActions::TracedValueSpecificationActionActivation")
umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation = Class(name="umlTrace::IntermediateActions::TracedReadStructuralFeatureActionActivation")
TracedStructuralFeatureActionActivation = Class(name="TracedStructuralFeatureActionActivation")
umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation = Class(name="umlTrace::IntermediateActions::TracedAddStructuralFeatureValueActionActivation")
TracedWriteStructuralFeatureActionActivation = Class(name="TracedWriteStructuralFeatureActionActivation")
umlTrace_IntermediateActions_TracedCreateObjectActionActivation = Class(name="umlTrace::IntermediateActions::TracedCreateObjectActionActivation")
umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation = Class(name="umlTrace::IntermediateActions::TracedWriteStructuralFeatureActionActivation", is_abstract=True)
umlTrace_BasicActions_TracedActionActivation = Class(name="umlTrace::BasicActions::TracedActionActivation", is_abstract=True)
umlTrace_BasicActions_TracedOutputPinActivation = Class(name="umlTrace::BasicActions::TracedOutputPinActivation")
TracedPinActivation = Class(name="TracedPinActivation")
umlTrace_BasicActions_TracedCallBehaviorActionActivation = Class(name="umlTrace::BasicActions::TracedCallBehaviorActionActivation")
TracedCallActionActivation = Class(name="TracedCallActionActivation")
umlTrace_BasicActions_TracedOpaqueActionActivation = Class(name="umlTrace::BasicActions::TracedOpaqueActionActivation")
umlTrace_BasicActions_TracedCallActionActivation = Class(name="umlTrace::BasicActions::TracedCallActionActivation", is_abstract=True)
TracedInvocationActionActivation = Class(name="TracedInvocationActionActivation")
umlTrace_Loci_TracedExecutionEnvironment = Class(name="umlTrace::Loci::TracedExecutionEnvironment")
umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation = Class(name="umlTrace::IntermediateActions::TracedStructuralFeatureActionActivation", is_abstract=True)
TracedActionActivation = Class(name="TracedActionActivation")
umlTrace_BasicActions_TracedPinActivation = Class(name="umlTrace::BasicActions::TracedPinActivation", is_abstract=True)
umlTrace_BasicActions_TracedInputPinActivation = Class(name="umlTrace::BasicActions::TracedInputPinActivation")
umlTrace_BasicActions_TracedInvocationActionActivation = Class(name="umlTrace::BasicActions::TracedInvocationActionActivation", is_abstract=True)
umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution = Class(name="umlTrace::IntegerFunctions::TracedIntegerPlusFunctionBehaviorExecution")
umlTrace_Input_TracedInputParameterValues = Class(name="umlTrace::Input::TracedInputParameterValues")
umlTrace_uml_TracedStructuralFeature = Class(name="umlTrace::uml::TracedStructuralFeature", is_abstract=True)
uml_TracedFeature = Class(name="uml::TracedFeature")
uml_TracedTypedElement = Class(name="uml::TracedTypedElement")
uml_TracedMultiplicityElement = Class(name="uml::TracedMultiplicityElement")
umlTrace_uml_TracedConnector = Class(name="umlTrace::uml::TracedConnector")
TracedFeature = Class(name="TracedFeature")
uml_TracedBehavior = Class(name="uml::TracedBehavior")
uml_umlTrace_Connector = Class(name="uml::umlTrace::Connector")
umlTrace_uml_TracedOpaqueAction = Class(name="umlTrace::uml::TracedOpaqueAction")
TracedAction = Class(name="TracedAction")
umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution = Class(name="umlTrace::IntegerFunctions::TracedIntegerLessFunctionBehaviorExecution")
TracedOpaqueBehaviorExecution = Class(name="TracedOpaqueBehaviorExecution")
umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution = Class(name="umlTrace::IntegerFunctions::TracedIntegerGreaterFunctionBehaviorExecution")
umlTrace_uml_TracedDataType = Class(name="umlTrace::uml::TracedDataType")
TracedClassifier = Class(name="TracedClassifier")
uml_umlTrace_DataType = Class(name="uml::umlTrace::DataType")
umlTrace_uml_TracedCommunicationPath = Class(name="umlTrace::uml::TracedCommunicationPath")
TracedAssociation = Class(name="TracedAssociation")
umlTrace_uml_TracedLinkAction = Class(name="umlTrace::uml::TracedLinkAction", is_abstract=True)
umlTrace_uml_TracedProperty = Class(name="umlTrace::uml::TracedProperty")
uml_TracedConnectableElement = Class(name="uml::TracedConnectableElement")
uml_TracedDeploymentTarget = Class(name="uml::TracedDeploymentTarget")
uml_umlTrace_OpaqueAction = Class(name="uml::umlTrace::OpaqueAction")
uml_umlTrace_Property = Class(name="uml::umlTrace::Property")
umlTrace_uml_TracedContinuation = Class(name="umlTrace::uml::TracedContinuation")
TracedInteractionFragment = Class(name="TracedInteractionFragment")
uml_umlTrace_Continuation = Class(name="uml::umlTrace::Continuation")
umlTrace_uml_TracedRemoveStructuralFeatureValueAction = Class(name="umlTrace::uml::TracedRemoveStructuralFeatureValueAction")
TracedWriteStructuralFeatureAction = Class(name="TracedWriteStructuralFeatureAction")
uml_umlTrace_RemoveStructuralFeatureValueAction = Class(name="uml::umlTrace::RemoveStructuralFeatureValueAction")
umlTrace_uml_TracedSendSignalAction = Class(name="umlTrace::uml::TracedSendSignalAction")
TracedInvocationAction = Class(name="TracedInvocationAction")
umlTrace_uml_TracedOpaqueBehavior = Class(name="umlTrace::uml::TracedOpaqueBehavior")
TracedBehavior = Class(name="TracedBehavior")
umlTrace_uml_TracedArtifact = Class(name="umlTrace::uml::TracedArtifact")
uml_TracedClassifier = Class(name="uml::TracedClassifier")
uml_TracedDeployedArtifact = Class(name="uml::TracedDeployedArtifact")
uml_umlTrace_Artifact = Class(name="uml::umlTrace::Artifact")
umlTrace_uml_TracedTimeConstraint = Class(name="umlTrace::uml::TracedTimeConstraint")
TracedIntervalConstraint = Class(name="TracedIntervalConstraint")
umlTrace_uml_TracedInterfaceRealization = Class(name="umlTrace::uml::TracedInterfaceRealization")
TracedRealization = Class(name="TracedRealization")
uml_TracedBehavioredClassifier = Class(name="uml::TracedBehavioredClassifier")
umlTrace_uml_TracedObjectNode = Class(name="umlTrace::uml::TracedObjectNode", is_abstract=True)
uml_umlTrace_SendSignalAction = Class(name="uml::umlTrace::SendSignalAction")
umlTrace_uml_TracedActivityFinalNode = Class(name="umlTrace::uml::TracedActivityFinalNode")
TracedFinalNode = Class(name="TracedFinalNode")
uml_umlTrace_ActivityFinalNode = Class(name="uml::umlTrace::ActivityFinalNode")
umlTrace_uml_TracedDurationObservation = Class(name="umlTrace::uml::TracedDurationObservation")
TracedObservation = Class(name="TracedObservation")
uml_TracedNamedElement = Class(name="uml::TracedNamedElement")
uml_umlTrace_DurationObservation = Class(name="uml::umlTrace::DurationObservation")
umlTrace_uml_TracedAcceptEventAction = Class(name="umlTrace::uml::TracedAcceptEventAction")
uml_umlTrace_AcceptEventAction = Class(name="uml::umlTrace::AcceptEventAction")
umlTrace_uml_TracedEnumerationLiteral = Class(name="umlTrace::uml::TracedEnumerationLiteral")
TracedInstanceSpecification = Class(name="TracedInstanceSpecification")
umlTrace_uml_TracedAddStructuralFeatureValueAction = Class(name="umlTrace::uml::TracedAddStructuralFeatureValueAction")
uml_umlTrace_AddStructuralFeatureValueAction = Class(name="uml::umlTrace::AddStructuralFeatureValueAction")
umlTrace_uml_TracedExpression = Class(name="umlTrace::uml::TracedExpression")
TracedValueSpecification = Class(name="TracedValueSpecification")
uml_umlTrace_Expression = Class(name="uml::umlTrace::Expression")
umlTrace_uml_TracedConsiderIgnoreFragment = Class(name="umlTrace::uml::TracedConsiderIgnoreFragment")
TracedCombinedFragment = Class(name="TracedCombinedFragment")
umlTrace_uml_TracedDataStoreNode = Class(name="umlTrace::uml::TracedDataStoreNode")
TracedCentralBufferNode = Class(name="TracedCentralBufferNode")
umlTrace_uml_TracedFlowFinalNode = Class(name="umlTrace::uml::TracedFlowFinalNode")
uml_umlTrace_FlowFinalNode = Class(name="uml::umlTrace::FlowFinalNode")
umlTrace_uml_TracedInteractionFragment = Class(name="umlTrace::uml::TracedInteractionFragment", is_abstract=True)
TracedNamedElement = Class(name="TracedNamedElement")
umlTrace_uml_TracedClassifier = Class(name="umlTrace::uml::TracedClassifier", is_abstract=True)
umlTrace_uml_TracedReadLinkAction = Class(name="umlTrace::uml::TracedReadLinkAction")
TracedLinkAction = Class(name="TracedLinkAction")
uml_umlTrace_ReadLinkAction = Class(name="uml::umlTrace::ReadLinkAction")
uml_TracedNamespace = Class(name="uml::TracedNamespace")
uml_TracedRedefinableElement = Class(name="uml::TracedRedefinableElement")
uml_TracedType = Class(name="uml::TracedType")
uml_TracedTemplateableElement = Class(name="uml::TracedTemplateableElement")
umlTrace_uml_TracedInformationItem = Class(name="umlTrace::uml::TracedInformationItem")
uml_umlTrace_InformationItem = Class(name="uml::umlTrace::InformationItem")
umlTrace_uml_TracedCollaboration = Class(name="umlTrace::uml::TracedCollaboration")
uml_TracedStructuredClassifier = Class(name="uml::TracedStructuredClassifier")
uml_umlTrace_Collaboration = Class(name="uml::umlTrace::Collaboration")
umlTrace_uml_TracedMessageEnd = Class(name="umlTrace::uml::TracedMessageEnd", is_abstract=True)
umlTrace_uml_TracedTemplateSignature = Class(name="umlTrace::uml::TracedTemplateSignature")
TracedElement = Class(name="TracedElement")
uml_umlTrace_TemplateSignature = Class(name="uml::umlTrace::TemplateSignature")
umlTrace_uml_TracedBroadcastSignalAction = Class(name="umlTrace::uml::TracedBroadcastSignalAction")
uml_umlTrace_BroadcastSignalAction = Class(name="uml::umlTrace::BroadcastSignalAction")
umlTrace_uml_TracedDeployment = Class(name="umlTrace::uml::TracedDeployment")
TracedDependency = Class(name="TracedDependency")
umlTrace_uml_TracedPort = Class(name="umlTrace::uml::TracedPort")
TracedProperty = Class(name="TracedProperty")
umlTrace_uml_TracedTimeInterval = Class(name="umlTrace::uml::TracedTimeInterval")
TracedInterval = Class(name="TracedInterval")
umlTrace_uml_TracedAction = Class(name="umlTrace::uml::TracedAction", is_abstract=True)
TracedExecutableNode = Class(name="TracedExecutableNode")
umlTrace_uml_TracedExtension = Class(name="umlTrace::uml::TracedExtension")
umlTrace_uml_TracedDirectedRelationship = Class(name="umlTrace::uml::TracedDirectedRelationship", is_abstract=True)
TracedRelationship = Class(name="TracedRelationship")
umlTrace_uml_TracedTimeEvent = Class(name="umlTrace::uml::TracedTimeEvent")
TracedEvent = Class(name="TracedEvent")
uml_umlTrace_TimeEvent = Class(name="uml::umlTrace::TimeEvent")
umlTrace_uml_TracedPackageableElement = Class(name="umlTrace::uml::TracedPackageableElement", is_abstract=True)
uml_TracedParameterableElement = Class(name="uml::TracedParameterableElement")
umlTrace_uml_TracedType = Class(name="umlTrace::uml::TracedType", is_abstract=True)
TracedPackageableElement = Class(name="TracedPackageableElement")
umlTrace_uml_TracedProtocolTransition = Class(name="umlTrace::uml::TracedProtocolTransition")
TracedTransition = Class(name="TracedTransition")
umlTrace_uml_TracedPackage = Class(name="umlTrace::uml::TracedPackage")
uml_TracedPackageableElement = Class(name="uml::TracedPackageableElement")
uml_umlTrace_Package = Class(name="uml::umlTrace::Package")
umlTrace_uml_TracedBehavioredClassifier = Class(name="umlTrace::uml::TracedBehavioredClassifier", is_abstract=True)
umlTrace_uml_TracedStructuralFeatureAction = Class(name="umlTrace::uml::TracedStructuralFeatureAction", is_abstract=True)
umlTrace_uml_TracedConstraint = Class(name="umlTrace::uml::TracedConstraint")
uml_umlTrace_Constraint = Class(name="uml::umlTrace::Constraint")
umlTrace_uml_TracedMultiplicityElement = Class(name="umlTrace::uml::TracedMultiplicityElement", is_abstract=True)
umlTrace_uml_TracedLiteralSpecification = Class(name="umlTrace::uml::TracedLiteralSpecification", is_abstract=True)
umlTrace_uml_TracedGeneralizationSet = Class(name="umlTrace::uml::TracedGeneralizationSet")
umlTrace_uml_TracedReduceAction = Class(name="umlTrace::uml::TracedReduceAction")
uml_umlTrace_ReduceAction = Class(name="uml::umlTrace::ReduceAction")
umlTrace_uml_TracedInputPin = Class(name="umlTrace::uml::TracedInputPin")
TracedPin = Class(name="TracedPin")
uml_umlTrace_InputPin = Class(name="uml::umlTrace::InputPin")
umlTrace_uml_TracedSequenceNode = Class(name="umlTrace::uml::TracedSequenceNode")
TracedStructuredActivityNode = Class(name="TracedStructuredActivityNode")
uml_TracedExecutableNode = Class(name="uml::TracedExecutableNode")
umlTrace_uml_TracedFeature = Class(name="umlTrace::uml::TracedFeature", is_abstract=True)
TracedRedefinableElement = Class(name="TracedRedefinableElement")
umlTrace_uml_TracedInteractionConstraint = Class(name="umlTrace::uml::TracedInteractionConstraint")
TracedConstraint = Class(name="TracedConstraint")
uml_umlTrace_GeneralizationSet = Class(name="uml::umlTrace::GeneralizationSet")
umlTrace_uml_TracedElement = Class(name="umlTrace::uml::TracedElement", is_abstract=True)
TracedEModelElement = Class(name="TracedEModelElement")
umlTrace_uml_TracedComponentRealization = Class(name="umlTrace::uml::TracedComponentRealization")
umlTrace_uml_TracedAssociationClass = Class(name="umlTrace::uml::TracedAssociationClass")
umlTrace_uml_TracedSlot = Class(name="umlTrace::uml::TracedSlot")
umlTrace_uml_TracedWriteStructuralFeatureAction = Class(name="umlTrace::uml::TracedWriteStructuralFeatureAction", is_abstract=True)
TracedStructuralFeatureAction = Class(name="TracedStructuralFeatureAction")
uml_umlTrace_Slot = Class(name="uml::umlTrace::Slot")
umlTrace_uml_TracedSignalEvent = Class(name="umlTrace::uml::TracedSignalEvent")
TracedMessageEvent = Class(name="TracedMessageEvent")
uml_umlTrace_SignalEvent = Class(name="uml::umlTrace::SignalEvent")
umlTrace_uml_TracedExtensionPoint = Class(name="umlTrace::uml::TracedExtensionPoint")
uml_umlTrace_ExtensionPoint = Class(name="uml::umlTrace::ExtensionPoint")
umlTrace_uml_TracedJoinNode = Class(name="umlTrace::uml::TracedJoinNode")
TracedControlNode = Class(name="TracedControlNode")
uml_umlTrace_JoinNode = Class(name="uml::umlTrace::JoinNode")
umlTrace_uml_TracedStartObjectBehaviorAction = Class(name="umlTrace::uml::TracedStartObjectBehaviorAction")
TracedCallAction = Class(name="TracedCallAction")
uml_umlTrace_StartObjectBehaviorAction = Class(name="uml::umlTrace::StartObjectBehaviorAction")
uml_umlTrace_ElementImport = Class(name="uml::umlTrace::ElementImport")
umlTrace_uml_TracedCreateObjectAction = Class(name="umlTrace::uml::TracedCreateObjectAction")
uml_umlTrace_CreateObjectAction = Class(name="uml::umlTrace::CreateObjectAction")
umlTrace_uml_TracedExecutionEnvironment = Class(name="umlTrace::uml::TracedExecutionEnvironment")
TracedNode = Class(name="TracedNode")
umlTrace_uml_TracedOccurrenceSpecification = Class(name="umlTrace::uml::TracedOccurrenceSpecification")
uml_umlTrace_OccurrenceSpecification = Class(name="uml::umlTrace::OccurrenceSpecification")
umlTrace_uml_TracedStringExpression = Class(name="umlTrace::uml::TracedStringExpression")
umlTrace_uml_TracedElementImport = Class(name="umlTrace::uml::TracedElementImport")
TracedDirectedRelationship = Class(name="TracedDirectedRelationship")
umlTrace_uml_TracedInterface = Class(name="umlTrace::uml::TracedInterface")
uml_umlTrace_Interface = Class(name="uml::umlTrace::Interface")
umlTrace_uml_TracedConditionalNode = Class(name="umlTrace::uml::TracedConditionalNode")
umlTrace_uml_TracedDeployedArtifact = Class(name="umlTrace::uml::TracedDeployedArtifact", is_abstract=True)
umlTrace_uml_TracedStereotype = Class(name="umlTrace::uml::TracedStereotype")
TracedClass = Class(name="TracedClass")
uml_umlTrace_ReadLinkObjectEndAction = Class(name="uml::umlTrace::ReadLinkObjectEndAction")
umlTrace_uml_TracedAnyReceiveEvent = Class(name="umlTrace::uml::TracedAnyReceiveEvent")
uml_umlTrace_AnyReceiveEvent = Class(name="uml::umlTrace::AnyReceiveEvent")
umlTrace_uml_TracedNamedElement = Class(name="umlTrace::uml::TracedNamedElement", is_abstract=True)
umlTrace_uml_TracedComponent = Class(name="umlTrace::uml::TracedComponent")
umlTrace_uml_TracedReadLinkObjectEndAction = Class(name="umlTrace::uml::TracedReadLinkObjectEndAction")
umlTrace_uml_TracedExtensionEnd = Class(name="umlTrace::uml::TracedExtensionEnd")
umlTrace_uml_TracedStateMachine = Class(name="umlTrace::uml::TracedStateMachine")
umlTrace_uml_TracedValueSpecification = Class(name="umlTrace::uml::TracedValueSpecification", is_abstract=True)
umlTrace_uml_TracedInteraction = Class(name="umlTrace::uml::TracedInteraction")
uml_TracedInteractionFragment = Class(name="uml::TracedInteractionFragment")
umlTrace_uml_TracedLiteralString = Class(name="umlTrace::uml::TracedLiteralString")
TracedLiteralSpecification = Class(name="TracedLiteralSpecification")
uml_umlTrace_LiteralString = Class(name="uml::umlTrace::LiteralString")
umlTrace_uml_TracedRealization = Class(name="umlTrace::uml::TracedRealization")
TracedAbstraction = Class(name="TracedAbstraction")
umlTrace_uml_TracedStartClassifierBehaviorAction = Class(name="umlTrace::uml::TracedStartClassifierBehaviorAction")
uml_umlTrace_StartClassifierBehaviorAction = Class(name="uml::umlTrace::StartClassifierBehaviorAction")
umlTrace_uml_TracedMessageEvent = Class(name="umlTrace::uml::TracedMessageEvent", is_abstract=True)
umlTrace_uml_TracedCallEvent = Class(name="umlTrace::uml::TracedCallEvent")
uml_umlTrace_CallEvent = Class(name="uml::umlTrace::CallEvent")
umlTrace_uml_TracedConnectableElementTemplateParameter = Class(name="umlTrace::uml::TracedConnectableElementTemplateParameter")
TracedTemplateParameter = Class(name="TracedTemplateParameter")
umlTrace_uml_TracedRelationship = Class(name="umlTrace::uml::TracedRelationship", is_abstract=True)
umlTrace_uml_TracedSendObjectAction = Class(name="umlTrace::uml::TracedSendObjectAction")
uml_TracedAction = Class(name="uml::TracedAction")
umlTrace_uml_TracedLifeline = Class(name="umlTrace::uml::TracedLifeline")
uml_umlTrace_Lifeline = Class(name="uml::umlTrace::Lifeline")
umlTrace_uml_TracedExecutionSpecification = Class(name="umlTrace::uml::TracedExecutionSpecification", is_abstract=True)
umlTrace_uml_TracedTimeObservation = Class(name="umlTrace::uml::TracedTimeObservation")
uml_umlTrace_SendObjectAction = Class(name="uml::umlTrace::SendObjectAction")
umlTrace_uml_TracedExpansionRegion = Class(name="umlTrace::uml::TracedExpansionRegion")
umlTrace_uml_TracedWriteVariableAction = Class(name="umlTrace::uml::TracedWriteVariableAction", is_abstract=True)
TracedVariableAction = Class(name="TracedVariableAction")
umlTrace_uml_TracedLoopNode = Class(name="umlTrace::uml::TracedLoopNode")
uml_umlTrace_TimeObservation = Class(name="uml::umlTrace::TimeObservation")
umlTrace_uml_TracedCreateLinkObjectAction = Class(name="umlTrace::uml::TracedCreateLinkObjectAction")
TracedCreateLinkAction = Class(name="TracedCreateLinkAction")
umlTrace_uml_TracedPrimitiveType = Class(name="umlTrace::uml::TracedPrimitiveType")
TracedDataType = Class(name="TracedDataType")
umlTrace_uml_TracedProtocolConformance = Class(name="umlTrace::uml::TracedProtocolConformance")
uml_umlTrace_ProtocolConformance = Class(name="uml::umlTrace::ProtocolConformance")
umlTrace_uml_TracedEnumeration = Class(name="umlTrace::uml::TracedEnumeration")
umlTrace_uml_TracedCollaborationUse = Class(name="umlTrace::uml::TracedCollaborationUse")
umlTrace_uml_TracedActivityPartition = Class(name="umlTrace::uml::TracedActivityPartition")
TracedActivityGroup = Class(name="TracedActivityGroup")
uml_umlTrace_ActivityPartition = Class(name="uml::umlTrace::ActivityPartition")
umlTrace_uml_TracedVariableAction = Class(name="umlTrace::uml::TracedVariableAction", is_abstract=True)
umlTrace_uml_TracedLinkEndDestructionData = Class(name="umlTrace::uml::TracedLinkEndDestructionData")
TracedLinkEndData = Class(name="TracedLinkEndData")
umlTrace_uml_TracedDurationInterval = Class(name="umlTrace::uml::TracedDurationInterval")
umlTrace_uml_TracedInclude = Class(name="umlTrace::uml::TracedInclude")
uml_TracedDirectedRelationship = Class(name="uml::TracedDirectedRelationship")
uml_umlTrace_CollaborationUse = Class(name="uml::umlTrace::CollaborationUse")
uml_umlTrace_Include = Class(name="uml::umlTrace::Include")
umlTrace_uml_TracedActivityNode = Class(name="umlTrace::uml::TracedActivityNode", is_abstract=True)
ActivityContent = Class(name="ActivityContent")
uml_TracedActivityGroup = Class(name="uml::TracedActivityGroup")
umlTrace_uml_TracedDestructionOccurrenceSpecification = Class(name="umlTrace::uml::TracedDestructionOccurrenceSpecification")
TracedMessageOccurrenceSpecification = Class(name="TracedMessageOccurrenceSpecification")
umlTrace_uml_TracedState = Class(name="umlTrace::uml::TracedState")
uml_TracedVertex = Class(name="uml::TracedVertex")
umlTrace_uml_TracedCallAction = Class(name="umlTrace::uml::TracedCallAction", is_abstract=True)
umlTrace_uml_TracedTemplateableElement = Class(name="umlTrace::uml::TracedTemplateableElement", is_abstract=True)
umlTrace_uml_TracedBehavior = Class(name="umlTrace::uml::TracedBehavior", is_abstract=True)
uml_TracedBehavioralFeature = Class(name="uml::TracedBehavioralFeature")
uml_umlTrace_State = Class(name="uml::umlTrace::State")
umlTrace_uml_TracedClassifierTemplateParameter = Class(name="umlTrace::uml::TracedClassifierTemplateParameter")
umlTrace_uml_TracedActivityParameterNode = Class(name="umlTrace::uml::TracedActivityParameterNode")
TracedObjectNode = Class(name="TracedObjectNode")
uml_umlTrace_ActivityParameterNode = Class(name="uml::umlTrace::ActivityParameterNode")
umlTrace_uml_TracedParameterSet = Class(name="umlTrace::uml::TracedParameterSet")
uml_umlTrace_ParameterSet = Class(name="uml::umlTrace::ParameterSet")
umlTrace_uml_TracedDuration = Class(name="umlTrace::uml::TracedDuration")
uml_TracedObservation = Class(name="uml::TracedObservation")
uml_umlTrace_Class = Class(name="uml::umlTrace::Class")
umlTrace_uml_TracedUsage = Class(name="umlTrace::uml::TracedUsage")
umlTrace_uml_TracedLiteralUnlimitedNatural = Class(name="umlTrace::uml::TracedLiteralUnlimitedNatural")
uml_umlTrace_LiteralUnlimitedNatural = Class(name="uml::umlTrace::LiteralUnlimitedNatural")
umlTrace_uml_TracedStructuredActivityNode = Class(name="umlTrace::uml::TracedStructuredActivityNode")
uml_umlTrace_Duration = Class(name="uml::umlTrace::Duration")
umlTrace_uml_TracedClass = Class(name="umlTrace::uml::TracedClass")
uml_TracedEncapsulatedClassifier = Class(name="uml::TracedEncapsulatedClassifier")
uml_umlTrace_StructuredActivityNode = Class(name="uml::umlTrace::StructuredActivityNode")
umlTrace_uml_TracedAbstraction = Class(name="umlTrace::uml::TracedAbstraction")
umlTrace_uml_TracedReadStructuralFeatureAction = Class(name="umlTrace::uml::TracedReadStructuralFeatureAction")
uml_umlTrace_ReadStructuralFeatureAction = Class(name="uml::umlTrace::ReadStructuralFeatureAction")
umlTrace_uml_TracedMergeNode = Class(name="umlTrace::uml::TracedMergeNode")
uml_umlTrace_MergeNode = Class(name="uml::umlTrace::MergeNode")
umlTrace_uml_TracedRedefinableTemplateSignature = Class(name="umlTrace::uml::TracedRedefinableTemplateSignature")
umlTrace_uml_TracedCreateLinkAction = Class(name="umlTrace::uml::TracedCreateLinkAction")
TracedWriteLinkAction = Class(name="TracedWriteLinkAction")
uml_umlTrace_CreateLinkAction = Class(name="uml::umlTrace::CreateLinkAction")
umlTrace_uml_TracedGeneralization = Class(name="umlTrace::uml::TracedGeneralization")
uml_umlTrace_Generalization = Class(name="uml::umlTrace::Generalization")
umlTrace_uml_TracedPartDecomposition = Class(name="umlTrace::uml::TracedPartDecomposition")
TracedInteractionUse = Class(name="TracedInteractionUse")
umlTrace_uml_TracedTypedElement = Class(name="umlTrace::uml::TracedTypedElement", is_abstract=True)
umlTrace_uml_TracedOperationTemplateParameter = Class(name="umlTrace::uml::TracedOperationTemplateParameter")
umlTrace_uml_TracedReadLinkObjectEndQualifierAction = Class(name="umlTrace::uml::TracedReadLinkObjectEndQualifierAction")
uml_umlTrace_ReadLinkObjectEndQualifierAction = Class(name="uml::umlTrace::ReadLinkObjectEndQualifierAction")
umlTrace_uml_TracedTemplateParameterSubstitution = Class(name="umlTrace::uml::TracedTemplateParameterSubstitution")
uml_umlTrace_TemplateParameterSubstitution = Class(name="uml::umlTrace::TemplateParameterSubstitution")
umlTrace_uml_TracedExtend = Class(name="umlTrace::uml::TracedExtend")
uml_umlTrace_Extend = Class(name="uml::umlTrace::Extend")
umlTrace_uml_TracedReadVariableAction = Class(name="umlTrace::uml::TracedReadVariableAction")
uml_umlTrace_ReadVariableAction = Class(name="uml::umlTrace::ReadVariableAction")
umlTrace_uml_TracedMessage = Class(name="umlTrace::uml::TracedMessage")
uml_TracedMessageEnd = Class(name="uml::TracedMessageEnd")
umlTrace_uml_TracedQualifierValue = Class(name="umlTrace::uml::TracedQualifierValue")
uml_umlTrace_QualifierValue = Class(name="uml::umlTrace::QualifierValue")
umlTrace_uml_TracedInitialNode = Class(name="umlTrace::uml::TracedInitialNode")
uml_umlTrace_InitialNode = Class(name="uml::umlTrace::InitialNode")
umlTrace_uml_TracedLiteralInteger = Class(name="umlTrace::uml::TracedLiteralInteger")
uml_umlTrace_LiteralInteger = Class(name="uml::umlTrace::LiteralInteger")
umlTrace_uml_TracedClearVariableAction = Class(name="umlTrace::uml::TracedClearVariableAction")
uml_umlTrace_ClearVariableAction = Class(name="uml::umlTrace::ClearVariableAction")
umlTrace_uml_TracedProfileApplication = Class(name="umlTrace::uml::TracedProfileApplication")
uml_umlTrace_Message = Class(name="uml::umlTrace::Message")
umlTrace_uml_TracedLiteralBoolean = Class(name="umlTrace::uml::TracedLiteralBoolean")
uml_umlTrace_LiteralBoolean = Class(name="uml::umlTrace::LiteralBoolean")
umlTrace_uml_TracedTemplateParameter = Class(name="umlTrace::uml::TracedTemplateParameter")
uml_umlTrace_TemplateParameter = Class(name="uml::umlTrace::TemplateParameter")
umlTrace_uml_TracedConnectorEnd = Class(name="umlTrace::uml::TracedConnectorEnd")
TracedMultiplicityElement = Class(name="TracedMultiplicityElement")
uml_umlTrace_ProfileApplication = Class(name="uml::umlTrace::ProfileApplication")
umlTrace_uml_TracedParameterableElement = Class(name="umlTrace::uml::TracedParameterableElement", is_abstract=True)
umlTrace_uml_TracedMessageOccurrenceSpecification = Class(name="umlTrace::uml::TracedMessageOccurrenceSpecification")
umlTrace_uml_TracedDurationConstraint = Class(name="umlTrace::uml::TracedDurationConstraint")
umlTrace_uml_TracedImage = Class(name="umlTrace::uml::TracedImage")
uml_umlTrace_Image = Class(name="uml::umlTrace::Image")
umlTrace_uml_TracedEncapsulatedClassifier = Class(name="umlTrace::uml::TracedEncapsulatedClassifier", is_abstract=True)
TracedStructuredClassifier = Class(name="TracedStructuredClassifier")
umlTrace_uml_TracedParameter = Class(name="umlTrace::uml::TracedParameter")
uml_umlTrace_Parameter = Class(name="uml::umlTrace::Parameter")
umlTrace_uml_TracedActionInputPin = Class(name="umlTrace::uml::TracedActionInputPin")
TracedInputPin = Class(name="TracedInputPin")
uml_umlTrace_ConnectorEnd = Class(name="uml::umlTrace::ConnectorEnd")
uml_umlTrace_Trigger = Class(name="uml::umlTrace::Trigger")
umlTrace_uml_TracedCallOperationAction = Class(name="umlTrace::uml::TracedCallOperationAction")
uml_umlTrace_CallOperationAction = Class(name="uml::umlTrace::CallOperationAction")
umlTrace_uml_TracedProfile = Class(name="umlTrace::uml::TracedProfile")
TracedPackage = Class(name="TracedPackage")
umlTrace_uml_TracedInterval = Class(name="umlTrace::uml::TracedInterval")
uml_umlTrace_Interval = Class(name="uml::umlTrace::Interval")
umlTrace_uml_TracedTrigger = Class(name="umlTrace::uml::TracedTrigger")
uml_TracedEvent = Class(name="uml::TracedEvent")
uml_umlTrace_InstanceSpecification = Class(name="uml::umlTrace::InstanceSpecification")
umlTrace_uml_TracedValuePin = Class(name="umlTrace::uml::TracedValuePin")
umlTrace_uml_TracedReadIsClassifiedObjectAction = Class(name="umlTrace::uml::TracedReadIsClassifiedObjectAction")
uml_umlTrace_ReadIsClassifiedObjectAction = Class(name="uml::umlTrace::ReadIsClassifiedObjectAction")
umlTrace_uml_TracedIntervalConstraint = Class(name="umlTrace::uml::TracedIntervalConstraint")
umlTrace_uml_TracedInstanceSpecification = Class(name="umlTrace::uml::TracedInstanceSpecification")
uml_umlTrace_OutputPin = Class(name="uml::umlTrace::OutputPin")
umlTrace_uml_TracedDecisionNode = Class(name="umlTrace::uml::TracedDecisionNode")
uml_umlTrace_DecisionNode = Class(name="uml::umlTrace::DecisionNode")
umlTrace_uml_TracedValueSpecificationAction = Class(name="umlTrace::uml::TracedValueSpecificationAction")
uml_umlTrace_ValueSpecificationAction = Class(name="uml::umlTrace::ValueSpecificationAction")
umlTrace_uml_TracedRegion = Class(name="umlTrace::uml::TracedRegion")
umlTrace_uml_TracedProtocolStateMachine = Class(name="umlTrace::uml::TracedProtocolStateMachine")
TracedStateMachine = Class(name="TracedStateMachine")
umlTrace_uml_TracedOutputPin = Class(name="umlTrace::uml::TracedOutputPin")
uml_umlTrace_Region = Class(name="uml::umlTrace::Region")
umlTrace_uml_TracedInterruptibleActivityRegion = Class(name="umlTrace::uml::TracedInterruptibleActivityRegion")
uml_umlTrace_InterruptibleActivityRegion = Class(name="uml::umlTrace::InterruptibleActivityRegion")
umlTrace_uml_TracedDestroyLinkAction = Class(name="umlTrace::uml::TracedDestroyLinkAction")
uml_umlTrace_DestroyLinkAction = Class(name="uml::umlTrace::DestroyLinkAction")
umlTrace_uml_TracedFinalState = Class(name="umlTrace::uml::TracedFinalState")
TracedState = Class(name="TracedState")
umlTrace_uml_TracedActivityGroup = Class(name="umlTrace::uml::TracedActivityGroup", is_abstract=True)
umlTrace_uml_TracedInteractionOperand = Class(name="umlTrace::uml::TracedInteractionOperand")
uml_umlTrace_InteractionOperand = Class(name="uml::umlTrace::InteractionOperand")
umlTrace_uml_TracedActivityEdge = Class(name="umlTrace::uml::TracedActivityEdge", is_abstract=True)
umlTrace_uml_TracedInformationFlow = Class(name="umlTrace::uml::TracedInformationFlow")
uml_TracedRelationship = Class(name="uml::TracedRelationship")
uml_umlTrace_InformationFlow = Class(name="uml::umlTrace::InformationFlow")
umlTrace_uml_TracedPseudostate = Class(name="umlTrace::uml::TracedPseudostate")
TracedVertex = Class(name="TracedVertex")
uml_umlTrace_Pseudostate = Class(name="uml::umlTrace::Pseudostate")
umlTrace_uml_TracedControlNode = Class(name="umlTrace::uml::TracedControlNode", is_abstract=True)
TracedActivityNode = Class(name="TracedActivityNode")
umlTrace_uml_TracedUseCase = Class(name="umlTrace::uml::TracedUseCase")
TracedBehavioredClassifier = Class(name="TracedBehavioredClassifier")
uml_umlTrace_UseCase = Class(name="uml::umlTrace::UseCase")
umlTrace_uml_TracedReplyAction = Class(name="umlTrace::uml::TracedReplyAction")
uml_umlTrace_ReplyAction = Class(name="uml::umlTrace::ReplyAction")
umlTrace_uml_TracedCombinedFragment = Class(name="umlTrace::uml::TracedCombinedFragment")
uml_umlTrace_CombinedFragment = Class(name="uml::umlTrace::CombinedFragment")
umlTrace_uml_TracedWriteLinkAction = Class(name="umlTrace::uml::TracedWriteLinkAction", is_abstract=True)
umlTrace_uml_TracedClause = Class(name="umlTrace::uml::TracedClause")
uml_umlTrace_Clause = Class(name="uml::umlTrace::Clause")
umlTrace_uml_TracedInstanceValue = Class(name="umlTrace::uml::TracedInstanceValue")
uml_umlTrace_InstanceValue = Class(name="uml::umlTrace::InstanceValue")
umlTrace_uml_TracedDependency = Class(name="umlTrace::uml::TracedDependency")
uml_umlTrace_Dependency = Class(name="uml::umlTrace::Dependency")
umlTrace_uml_TracedTimeExpression = Class(name="umlTrace::uml::TracedTimeExpression")
uml_umlTrace_TimeExpression = Class(name="uml::umlTrace::TimeExpression")
umlTrace_uml_TracedManifestation = Class(name="umlTrace::uml::TracedManifestation")
umlTrace_uml_TracedReadExtentAction = Class(name="umlTrace::uml::TracedReadExtentAction")
uml_umlTrace_ReadExtentAction = Class(name="uml::umlTrace::ReadExtentAction")
umlTrace_uml_TracedTransition = Class(name="umlTrace::uml::TracedTransition")
uml_umlTrace_Transition = Class(name="uml::umlTrace::Transition")
umlTrace_uml_TracedLinkEndData = Class(name="umlTrace::uml::TracedLinkEndData")
uml_umlTrace_ObjectFlow = Class(name="uml::umlTrace::ObjectFlow")
uml_umlTrace_LinkEndData = Class(name="uml::umlTrace::LinkEndData")
umlTrace_uml_TracedNode = Class(name="umlTrace::uml::TracedNode")
umlTrace_uml_TracedPackageMerge = Class(name="umlTrace::uml::TracedPackageMerge")
uml_umlTrace_PackageMerge = Class(name="uml::umlTrace::PackageMerge")
umlTrace_uml_TracedModel = Class(name="umlTrace::uml::TracedModel")
umlTrace_uml_TracedObjectFlow = Class(name="umlTrace::uml::TracedObjectFlow")
TracedActivityEdge = Class(name="TracedActivityEdge")
umlTrace_uml_TracedEvent = Class(name="umlTrace::uml::TracedEvent", is_abstract=True)
umlTrace_uml_TracedChangeEvent = Class(name="umlTrace::uml::TracedChangeEvent")
uml_umlTrace_ChangeEvent = Class(name="uml::umlTrace::ChangeEvent")
umlTrace_uml_TracedRedefinableElement = Class(name="umlTrace::uml::TracedRedefinableElement", is_abstract=True)
umlTrace_uml_TracedDestroyObjectAction = Class(name="umlTrace::uml::TracedDestroyObjectAction")
uml_umlTrace_DestroyObjectAction = Class(name="uml::umlTrace::DestroyObjectAction")
umlTrace_uml_TracedForkNode = Class(name="umlTrace::uml::TracedForkNode")
uml_umlTrace_ForkNode = Class(name="uml::umlTrace::ForkNode")
umlTrace_uml_TracedFinalNode = Class(name="umlTrace::uml::TracedFinalNode", is_abstract=True)
umlTrace_uml_TracedSignal = Class(name="umlTrace::uml::TracedSignal")
uml_umlTrace_Signal = Class(name="uml::umlTrace::Signal")
umlTrace_uml_TracedComment = Class(name="umlTrace::uml::TracedComment")
uml_umlTrace_Comment = Class(name="uml::umlTrace::Comment")
umlTrace_uml_TracedStructuredClassifier = Class(name="umlTrace::uml::TracedStructuredClassifier", is_abstract=True)
umlTrace_uml_TracedLiteralNull = Class(name="umlTrace::uml::TracedLiteralNull")
uml_umlTrace_LiteralNull = Class(name="uml::umlTrace::LiteralNull")
umlTrace_uml_TracedExpansionNode = Class(name="umlTrace::uml::TracedExpansionNode")
uml_umlTrace_ExpansionNode = Class(name="uml::umlTrace::ExpansionNode")
umlTrace_uml_TracedReception = Class(name="umlTrace::uml::TracedReception")
TracedBehavioralFeature = Class(name="TracedBehavioralFeature")
uml_umlTrace_Reception = Class(name="uml::umlTrace::Reception")
umlTrace_uml_TracedRaiseExceptionAction = Class(name="umlTrace::uml::TracedRaiseExceptionAction")
uml_umlTrace_RaiseExceptionAction = Class(name="uml::umlTrace::RaiseExceptionAction")
umlTrace_uml_TracedBehavioralFeature = Class(name="umlTrace::uml::TracedBehavioralFeature", is_abstract=True)
umlTrace_uml_TracedAddVariableValueAction = Class(name="umlTrace::uml::TracedAddVariableValueAction")
TracedWriteVariableAction = Class(name="TracedWriteVariableAction")
uml_umlTrace_AddVariableValueAction = Class(name="uml::umlTrace::AddVariableValueAction")
umlTrace_uml_TracedClearAssociationAction = Class(name="umlTrace::uml::TracedClearAssociationAction")
uml_umlTrace_ClearAssociationAction = Class(name="uml::umlTrace::ClearAssociationAction")
umlTrace_uml_TracedPin = Class(name="umlTrace::uml::TracedPin", is_abstract=True)
uml_TracedObjectNode = Class(name="uml::TracedObjectNode")
umlTrace_uml_TracedTestIdentityAction = Class(name="umlTrace::uml::TracedTestIdentityAction")
uml_umlTrace_TestIdentityAction = Class(name="uml::umlTrace::TestIdentityAction")
umlTrace_uml_TracedControlFlow = Class(name="umlTrace::uml::TracedControlFlow")
uml_umlTrace_ControlFlow = Class(name="uml::umlTrace::ControlFlow")
umlTrace_uml_TracedOperation = Class(name="umlTrace::uml::TracedOperation")
uml_umlTrace_Operation = Class(name="uml::umlTrace::Operation")
umlTrace_uml_TracedConnectableElement = Class(name="umlTrace::uml::TracedConnectableElement", is_abstract=True)
umlTrace_uml_TracedVertex = Class(name="umlTrace::uml::TracedVertex", is_abstract=True)
umlTrace_uml_TracedObservation = Class(name="umlTrace::uml::TracedObservation", is_abstract=True)
umlTrace_uml_TracedNamespace = Class(name="umlTrace::uml::TracedNamespace", is_abstract=True)
umlTrace_uml_TracedPackageImport = Class(name="umlTrace::uml::TracedPackageImport")
uml_umlTrace_PackageImport = Class(name="uml::umlTrace::PackageImport")
umlTrace_uml_TracedExecutionOccurrenceSpecification = Class(name="umlTrace::uml::TracedExecutionOccurrenceSpecification")
TracedOccurrenceSpecification = Class(name="TracedOccurrenceSpecification")
uml_TracedExecutionSpecification = Class(name="uml::TracedExecutionSpecification")
umlTrace_uml_TracedExceptionHandler = Class(name="umlTrace::uml::TracedExceptionHandler")
uml_umlTrace_ExceptionHandler = Class(name="uml::umlTrace::ExceptionHandler")
umlTrace_uml_TracedVariable = Class(name="umlTrace::uml::TracedVariable")
uml_umlTrace_Variable = Class(name="uml::umlTrace::Variable")
umlTrace_uml_TracedInteractionUse = Class(name="umlTrace::uml::TracedInteractionUse")
uml_umlTrace_InteractionUse = Class(name="uml::umlTrace::InteractionUse")
umlTrace_uml_TracedAssociation = Class(name="umlTrace::uml::TracedAssociation")
uml_umlTrace_Association = Class(name="uml::umlTrace::Association")
umlTrace_uml_TracedStateInvariant = Class(name="umlTrace::uml::TracedStateInvariant")
uml_umlTrace_StateInvariant = Class(name="uml::umlTrace::StateInvariant")
umlTrace_uml_TracedLiteralReal = Class(name="umlTrace::uml::TracedLiteralReal")
uml_umlTrace_LiteralReal = Class(name="uml::umlTrace::LiteralReal")
umlTrace_uml_TracedInvocationAction = Class(name="umlTrace::uml::TracedInvocationAction", is_abstract=True)
umlTrace_uml_TracedRemoveVariableValueAction = Class(name="umlTrace::uml::TracedRemoveVariableValueAction")
uml_umlTrace_RemoveVariableValueAction = Class(name="uml::umlTrace::RemoveVariableValueAction")
umlTrace_uml_TracedDevice = Class(name="umlTrace::uml::TracedDevice")
umlTrace_uml_TracedSubstitution = Class(name="umlTrace::uml::TracedSubstitution")
umlTrace_uml_TracedGate = Class(name="umlTrace::uml::TracedGate")
TracedMessageEnd = Class(name="TracedMessageEnd")
uml_umlTrace_Gate = Class(name="uml::umlTrace::Gate")
umlTrace_uml_TracedDeploymentTarget = Class(name="umlTrace::uml::TracedDeploymentTarget", is_abstract=True)
umlTrace_uml_TracedGeneralOrdering = Class(name="umlTrace::uml::TracedGeneralOrdering")
uml_umlTrace_GeneralOrdering = Class(name="uml::umlTrace::GeneralOrdering")
umlTrace_uml_TracedCallBehaviorAction = Class(name="umlTrace::uml::TracedCallBehaviorAction")
uml_umlTrace_CallBehaviorAction = Class(name="uml::umlTrace::CallBehaviorAction")
umlTrace_uml_TracedReclassifyObjectAction = Class(name="umlTrace::uml::TracedReclassifyObjectAction")
uml_umlTrace_ReclassifyObjectAction = Class(name="uml::umlTrace::ReclassifyObjectAction")
umlTrace_uml_TracedActivity = Class(name="umlTrace::uml::TracedActivity")
umlTrace_uml_TracedConnectionPointReference = Class(name="umlTrace::uml::TracedConnectionPointReference")
uml_umlTrace_ConnectionPointReference = Class(name="uml::umlTrace::ConnectionPointReference")
umlTrace_uml_TracedActionExecutionSpecification = Class(name="umlTrace::uml::TracedActionExecutionSpecification")
TracedExecutionSpecification = Class(name="TracedExecutionSpecification")
uml_umlTrace_ActionExecutionSpecification = Class(name="uml::umlTrace::ActionExecutionSpecification")
umlTrace_uml_TracedReadSelfAction = Class(name="umlTrace::uml::TracedReadSelfAction")
uml_umlTrace_ReadSelfAction = Class(name="uml::umlTrace::ReadSelfAction")
umlTrace_uml_TracedAcceptCallAction = Class(name="umlTrace::uml::TracedAcceptCallAction")
TracedAcceptEventAction = Class(name="TracedAcceptEventAction")
umlTrace_uml_TracedLinkEndCreationData = Class(name="umlTrace::uml::TracedLinkEndCreationData")
umlTrace_uml_TracedTemplateBinding = Class(name="umlTrace::uml::TracedTemplateBinding")
uml_umlTrace_TemplateBinding = Class(name="uml::umlTrace::TemplateBinding")
umlTrace_uml_TracedClearStructuralFeatureAction = Class(name="umlTrace::uml::TracedClearStructuralFeatureAction")
uml_umlTrace_ClearStructuralFeatureAction = Class(name="uml::umlTrace::ClearStructuralFeatureAction")
umlTrace_uml_TracedOpaqueExpression = Class(name="umlTrace::uml::TracedOpaqueExpression")
uml_umlTrace_OpaqueExpression = Class(name="uml::umlTrace::OpaqueExpression")
umlTrace_uml_TracedFunctionBehavior = Class(name="umlTrace::uml::TracedFunctionBehavior")
TracedOpaqueBehavior = Class(name="TracedOpaqueBehavior")
umlTrace_uml_TracedDeploymentSpecification = Class(name="umlTrace::uml::TracedDeploymentSpecification")
TracedArtifact = Class(name="TracedArtifact")
umlTrace_uml_TracedActor = Class(name="umlTrace::uml::TracedActor")
uml_umlTrace_Actor = Class(name="uml::umlTrace::Actor")
umlTrace_uml_TracedBehaviorExecutionSpecification = Class(name="umlTrace::uml::TracedBehaviorExecutionSpecification")
uml_umlTrace_BehaviorExecutionSpecification = Class(name="uml::umlTrace::BehaviorExecutionSpecification")
umlTrace_uml_TracedExecutableNode = Class(name="umlTrace::uml::TracedExecutableNode", is_abstract=True)
umlTrace_uml_TracedUnmarshallAction = Class(name="umlTrace::uml::TracedUnmarshallAction")
uml_umlTrace_UnmarshallAction = Class(name="uml::umlTrace::UnmarshallAction")
umlTrace_uml_TracedCentralBufferNode = Class(name="umlTrace::uml::TracedCentralBufferNode")
uml_umlTrace_CentralBufferNode = Class(name="uml::umlTrace::CentralBufferNode")
umlTrace_ecore_TracedEModelElement = Class(name="umlTrace::ecore::TracedEModelElement", is_abstract=True)
ecore_umlTrace_EAnnotation = Class(name="ecore::umlTrace::EAnnotation")

# umlTrace_Trace class attributes and methods

# umlTrace_State class attributes and methods

# Steps class attributes and methods

# TracedObjects class attributes and methods

# SmallStep class attributes and methods

# BigStep class attributes and methods

# IntegerValue_value_IntegerValue_Value class attributes and methods

# ForkedToken_remainingOffersCount_Value class attributes and methods

# ForkedToken_baseToken_Value class attributes and methods

# ForkedToken_baseTokenIsWithdrawn_Value class attributes and methods

# ExecutionFactory_builtInTypes_Value class attributes and methods

# ExecutionFactory_primitiveBehaviorPrototypes_Value class attributes and methods

# ExecutionFactory_locus_ExecutionFactory_Value class attributes and methods

# Locus_factory_Value class attributes and methods

# Locus_extensionalValues_Value class attributes and methods

# Locus_executor_Value class attributes and methods

# ObjectNodeActivation_offeredTokenCount_Value class attributes and methods

# SemanticVisitor_runtimeModelElement_Value class attributes and methods

# ParameterValue_values_ParameterValue_Value class attributes and methods

# Object_types_Value class attributes and methods

# Reference_referent_Value class attributes and methods

# Execution_parameterValues_Value class attributes and methods

# Execution_context_Value class attributes and methods

# Element_semanticVisitor_Value class attributes and methods

# ActivityNodeActivationGroup_nodeActivations_Value class attributes and methods

# ActivityNodeActivationGroup_activityExecution_Value class attributes and methods

# ActivityNodeActivationGroup_edgeInstances_Value class attributes and methods

# Executor_locus_Executor_Value class attributes and methods

# PrimitiveValue_type_Value class attributes and methods

# Evaluation_specification_Evaluation_Value class attributes and methods

# Evaluation_locus_Evaluation_Value class attributes and methods

# BooleanValue_value_BooleanValue_Value class attributes and methods

# ParameterValue_parameter_ParameterValue_Value class attributes and methods

# ActionActivation_pinActivations_Value class attributes and methods

# ActionActivation_firing_Value class attributes and methods

# Token_holder_Value class attributes and methods

# Offer_offeredTokens_Value class attributes and methods

# FeatureValue_values_FeatureValue_Value class attributes and methods

# FeatureValue_feature_Value class attributes and methods

# FeatureValue_position_Value class attributes and methods

# PinActivation_actionActivation_Value class attributes and methods

# PinActivation_count_temp_Value class attributes and methods

# ActivityEdgeInstance_group_ActivityEdgeInstance_Value class attributes and methods

# ActivityEdgeInstance_offers_Value class attributes and methods

# ActivityEdgeInstance_target_Value class attributes and methods

# ObjectToken_value_Value class attributes and methods

# CallActionActivation_callExecutions_Value class attributes and methods

# CompoundValue_featureValues_Value class attributes and methods

# InputParameterValues_name_Value class attributes and methods

# InputParameterValues_parameterValues_Value class attributes and methods

# ActivityNodeActivation_heldTokens_Value class attributes and methods

# ActivityNodeActivation_node_ActivityNodeActivation_Value class attributes and methods

# ActivityNodeActivation_running_Value class attributes and methods

# ActivityNodeActivation_isRunning_Value class attributes and methods

# ActivityNodeActivation_outgoingEdges_Value class attributes and methods

# ActivityNodeActivation_incomingEdges_Value class attributes and methods

# ActivityNodeActivation_group_ActivityNodeActivation_Value class attributes and methods

# ExtensionalValue_locus_ExtensionalValue_Value class attributes and methods

# ActivityEdgeInstance_edge_ActivityEdgeInstance_Value class attributes and methods

# ActivityEdgeInstance_source_Value class attributes and methods

# ActivityExecution_activationGroup_Value class attributes and methods

# ExecutionEnvironment_locus_ExecutionEnvironment_Value class attributes and methods

# umlTrace_Steps_SmallStep class attributes and methods

# Steps_umlTrace_State class attributes and methods

# umlTrace_Steps_Steps class attributes and methods

# umlTrace_Steps_BigStep class attributes and methods

# umlTrace_Values_Object_types_Value class attributes and methods

# uml_TracedClass class attributes and methods

# Kernel_TracedObject class attributes and methods

# Values_umlTrace_State class attributes and methods

# umlTrace_Values_Reference_referent_Value class attributes and methods

# umlTrace_Values_IntegerValue_value_IntegerValue_Value class attributes and methods
umlTrace_Values_IntegerValue_value_IntegerValue_Value_value_IntegerValue: Property = Property(name="value_IntegerValue", type=IntegerType)
umlTrace_Values_IntegerValue_value_IntegerValue_Value.attributes={umlTrace_Values_IntegerValue_value_IntegerValue_Value_value_IntegerValue}

# Kernel_TracedIntegerValue class attributes and methods

# umlTrace_Values_ForkedToken_remainingOffersCount_Value class attributes and methods
umlTrace_Values_ForkedToken_remainingOffersCount_Value_remainingOffersCount: Property = Property(name="remainingOffersCount", type=IntegerType)
umlTrace_Values_ForkedToken_remainingOffersCount_Value.attributes={umlTrace_Values_ForkedToken_remainingOffersCount_Value_remainingOffersCount}

# IntermediateActivities_TracedForkedToken class attributes and methods

# umlTrace_Values_ForkedToken_baseToken_Value class attributes and methods

# IntermediateActivities_TracedToken class attributes and methods

# umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value class attributes and methods
umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value_baseTokenIsWithdrawn: Property = Property(name="baseTokenIsWithdrawn", type=BooleanType)
umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value.attributes={umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value_baseTokenIsWithdrawn}

# Kernel_TracedReference class attributes and methods

# umlTrace_Values_ExecutionFactory_builtInTypes_Value class attributes and methods

# uml_TracedPrimitiveType class attributes and methods

# Loci_TracedExecutionFactory class attributes and methods

# umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value class attributes and methods

# BasicBehaviors_TracedOpaqueBehaviorExecution class attributes and methods

# umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value class attributes and methods

# Loci_TracedLocus class attributes and methods

# umlTrace_Values_Locus_factory_Value class attributes and methods

# umlTrace_Values_Locus_extensionalValues_Value class attributes and methods

# Kernel_TracedExtensionalValue class attributes and methods

# umlTrace_Values_Locus_executor_Value class attributes and methods

# Loci_TracedExecutor class attributes and methods

# umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value class attributes and methods
umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value_offeredTokenCount: Property = Property(name="offeredTokenCount", type=IntegerType)
umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value.attributes={umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value_offeredTokenCount}

# IntermediateActivities_TracedObjectNodeActivation class attributes and methods

# umlTrace_Values_SemanticVisitor_runtimeModelElement_Value class attributes and methods

# uml_TracedElement class attributes and methods

# umlTrace_Values_ParameterValue_values_ParameterValue_Value class attributes and methods

# Kernel_TracedValue class attributes and methods

# BasicBehaviors_TracedParameterValue class attributes and methods

# umlTrace_Values_ParameterValue_parameter_ParameterValue_Value class attributes and methods

# uml_TracedParameter class attributes and methods

# umlTrace_Values_ActionActivation_pinActivations_Value class attributes and methods

# BasicActions_TracedPinActivation class attributes and methods

# BasicActions_TracedActionActivation class attributes and methods

# Loci_TracedSemanticVisitor class attributes and methods

# umlTrace_Values_Execution_parameterValues_Value class attributes and methods

# BasicBehaviors_TracedExecution class attributes and methods

# umlTrace_Values_Execution_context_Value class attributes and methods

# umlTrace_Values_Element_semanticVisitor_Value class attributes and methods

# umlTrace_Values_ActionActivation_firing_Value class attributes and methods
umlTrace_Values_ActionActivation_firing_Value_firing: Property = Property(name="firing", type=BooleanType)
umlTrace_Values_ActionActivation_firing_Value.attributes={umlTrace_Values_ActionActivation_firing_Value_firing}

# IntermediateActivities_TracedActivityNodeActivationGroup class attributes and methods

# umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value class attributes and methods

# IntermediateActivities_TracedActivityExecution class attributes and methods

# umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value class attributes and methods

# IntermediateActivities_TracedActivityEdgeInstance class attributes and methods

# umlTrace_Values_Executor_locus_Executor_Value class attributes and methods

# umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value class attributes and methods

# IntermediateActivities_TracedActivityNodeActivation class attributes and methods

# Kernel_TracedPrimitiveValue class attributes and methods

# umlTrace_Values_Evaluation_specification_Evaluation_Value class attributes and methods

# uml_TracedValueSpecification class attributes and methods

# Kernel_TracedEvaluation class attributes and methods

# umlTrace_Values_Evaluation_locus_Evaluation_Value class attributes and methods

# umlTrace_Values_BooleanValue_value_BooleanValue_Value class attributes and methods
umlTrace_Values_BooleanValue_value_BooleanValue_Value_value_BooleanValue: Property = Property(name="value_BooleanValue", type=BooleanType)
umlTrace_Values_BooleanValue_value_BooleanValue_Value.attributes={umlTrace_Values_BooleanValue_value_BooleanValue_Value_value_BooleanValue}

# Kernel_TracedBooleanValue class attributes and methods

# umlTrace_Values_PrimitiveValue_type_Value class attributes and methods

# IntermediateActivities_TracedObjectToken class attributes and methods

# umlTrace_Values_CallActionActivation_callExecutions_Value class attributes and methods

# BasicActions_TracedCallActionActivation class attributes and methods

# umlTrace_Values_CompoundValue_featureValues_Value class attributes and methods

# Kernel_TracedFeatureValue class attributes and methods

# Kernel_TracedCompoundValue class attributes and methods

# umlTrace_Values_Token_holder_Value class attributes and methods

# umlTrace_Values_ObjectToken_value_Value class attributes and methods

# IntermediateActivities_TracedOffer class attributes and methods

# umlTrace_Values_FeatureValue_values_FeatureValue_Value class attributes and methods

# umlTrace_Values_FeatureValue_feature_Value class attributes and methods

# uml_TracedStructuralFeature class attributes and methods

# umlTrace_Values_FeatureValue_position_Value class attributes and methods
umlTrace_Values_FeatureValue_position_Value_position: Property = Property(name="position", type=IntegerType)
umlTrace_Values_FeatureValue_position_Value.attributes={umlTrace_Values_FeatureValue_position_Value_position}

# umlTrace_Values_Offer_offeredTokens_Value class attributes and methods

# umlTrace_Values_PinActivation_count_temp_Value class attributes and methods
umlTrace_Values_PinActivation_count_temp_Value_count_temp: Property = Property(name="count_temp", type=IntegerType)
umlTrace_Values_PinActivation_count_temp_Value.attributes={umlTrace_Values_PinActivation_count_temp_Value_count_temp}

# umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value class attributes and methods

# umlTrace_Values_ActivityEdgeInstance_offers_Value class attributes and methods

# umlTrace_Values_PinActivation_actionActivation_Value class attributes and methods

# umlTrace_Values_ActivityEdgeInstance_target_Value class attributes and methods

# umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value class attributes and methods

# uml_TracedActivityEdge class attributes and methods

# umlTrace_Values_ActivityEdgeInstance_source_Value class attributes and methods

# umlTrace_Values_InputParameterValues_parameterValues_Value class attributes and methods

# umlTrace_Values_ActivityNodeActivation_heldTokens_Value class attributes and methods

# umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value class attributes and methods

# uml_TracedActivityNode class attributes and methods

# umlTrace_Values_InputParameterValues_name_Value class attributes and methods
umlTrace_Values_InputParameterValues_name_Value_name: Property = Property(name="name", type=StringType)
umlTrace_Values_InputParameterValues_name_Value.attributes={umlTrace_Values_InputParameterValues_name_Value_name}

# Input_TracedInputParameterValues class attributes and methods

# umlTrace_Values_ActivityNodeActivation_isRunning_Value class attributes and methods
umlTrace_Values_ActivityNodeActivation_isRunning_Value_isRunning: Property = Property(name="isRunning", type=BooleanType)
umlTrace_Values_ActivityNodeActivation_isRunning_Value.attributes={umlTrace_Values_ActivityNodeActivation_isRunning_Value_isRunning}

# umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value class attributes and methods

# umlTrace_Values_ActivityNodeActivation_incomingEdges_Value class attributes and methods

# umlTrace_Values_ActivityNodeActivation_running_Value class attributes and methods
umlTrace_Values_ActivityNodeActivation_running_Value_running: Property = Property(name="running", type=BooleanType)
umlTrace_Values_ActivityNodeActivation_running_Value.attributes={umlTrace_Values_ActivityNodeActivation_running_Value_running}

# umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value class attributes and methods

# umlTrace_Values_ActivityExecution_activationGroup_Value class attributes and methods

# umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value class attributes and methods

# umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value class attributes and methods

# umlTrace_Traced_TracedObjects class attributes and methods

# uml_TracedConnector class attributes and methods

# uml_TracedOpaqueAction class attributes and methods

# uml_TracedDataType class attributes and methods

# uml_TracedCommunicationPath class attributes and methods

# uml_TracedProperty class attributes and methods

# uml_TracedContinuation class attributes and methods

# uml_TracedRemoveStructuralFeatureValueAction class attributes and methods

# uml_TracedSendSignalAction class attributes and methods

# Loci_TracedExecutionEnvironment class attributes and methods

# uml_TracedArtifact class attributes and methods

# IntermediateActivities_TracedJoinNodeActivation class attributes and methods

# uml_TracedTimeConstraint class attributes and methods

# uml_TracedInterfaceRealization class attributes and methods

# uml_TracedActivityFinalNode class attributes and methods

# uml_TracedDurationObservation class attributes and methods

# IntermediateActivities_TracedInitialNodeActivation class attributes and methods

# uml_TracedAcceptEventAction class attributes and methods

# uml_TracedEnumerationLiteral class attributes and methods

# uml_TracedAddStructuralFeatureValueAction class attributes and methods

# uml_TracedOpaqueBehavior class attributes and methods

# uml_TracedConsiderIgnoreFragment class attributes and methods

# uml_TracedDataStoreNode class attributes and methods

# uml_TracedFlowFinalNode class attributes and methods

# uml_TracedInformationItem class attributes and methods

# uml_TracedCollaboration class attributes and methods

# uml_TracedTemplateSignature class attributes and methods

# uml_TracedBroadcastSignalAction class attributes and methods

# uml_TracedDeployment class attributes and methods

# uml_TracedPort class attributes and methods

# uml_TracedTimeInterval class attributes and methods

# uml_TracedExtension class attributes and methods

# uml_TracedReadLinkAction class attributes and methods

# uml_TracedExpression class attributes and methods

# uml_TracedProtocolTransition class attributes and methods

# IntermediateActivities_TracedActivityFinalNodeActivation class attributes and methods

# uml_TracedPackage class attributes and methods

# uml_TracedConstraint class attributes and methods

# uml_TracedGeneralizationSet class attributes and methods

# uml_TracedReduceAction class attributes and methods

# uml_TracedInputPin class attributes and methods

# uml_TracedSequenceNode class attributes and methods

# uml_TracedTimeEvent class attributes and methods

# uml_TracedAssociationClass class attributes and methods

# uml_TracedSlot class attributes and methods

# uml_TracedSignalEvent class attributes and methods

# uml_TracedExtensionPoint class attributes and methods

# uml_TracedJoinNode class attributes and methods

# BasicActions_TracedOutputPinActivation class attributes and methods

# uml_TracedStartObjectBehaviorAction class attributes and methods

# uml_TracedElementImport class attributes and methods

# uml_TracedCreateObjectAction class attributes and methods

# uml_TracedInteractionConstraint class attributes and methods

# uml_TracedComponentRealization class attributes and methods

# IntermediateActions_TracedValueSpecificationActionActivation class attributes and methods

# uml_TracedStringExpression class attributes and methods

# IntermediateActions_TracedReadStructuralFeatureActionActivation class attributes and methods

# uml_TracedStereotype class attributes and methods

# uml_TracedInterface class attributes and methods

# uml_TracedConditionalNode class attributes and methods

# uml_TracedExecutionEnvironment class attributes and methods

# uml_TracedOccurrenceSpecification class attributes and methods

# uml_TracedComponent class attributes and methods

# uml_TracedExtensionEnd class attributes and methods

# uml_TracedStateMachine class attributes and methods

# IntermediateActivities_TracedMergeNodeActivation class attributes and methods

# uml_TracedInteraction class attributes and methods

# uml_TracedLiteralString class attributes and methods

# uml_TracedRealization class attributes and methods

# uml_TracedReadLinkObjectEndAction class attributes and methods

# uml_TracedAnyReceiveEvent class attributes and methods

# uml_TracedConnectableElementTemplateParameter class attributes and methods

# uml_TracedSendObjectAction class attributes and methods

# uml_TracedLifeline class attributes and methods

# uml_TracedTimeObservation class attributes and methods

# IntermediateActivities_TracedControlToken class attributes and methods

# uml_TracedCreateLinkObjectAction class attributes and methods

# uml_TracedExpansionRegion class attributes and methods

# uml_TracedStartClassifierBehaviorAction class attributes and methods

# uml_TracedCallEvent class attributes and methods

# uml_TracedProtocolConformance class attributes and methods

# uml_TracedEnumeration class attributes and methods

# uml_TracedCollaborationUse class attributes and methods

# uml_TracedActivityPartition class attributes and methods

# uml_TracedLinkEndDestructionData class attributes and methods

# uml_TracedDurationInterval class attributes and methods

# uml_TracedLoopNode class attributes and methods

# uml_TracedState class attributes and methods

# BasicActions_TracedCallBehaviorActionActivation class attributes and methods

# IntermediateActions_TracedAddStructuralFeatureValueActionActivation class attributes and methods

# uml_TracedClassifierTemplateParameter class attributes and methods

# uml_TracedActivityParameterNode class attributes and methods

# IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution class attributes and methods

# uml_TracedInclude class attributes and methods

# uml_TracedDestructionOccurrenceSpecification class attributes and methods

# uml_TracedDuration class attributes and methods

# uml_TracedUsage class attributes and methods

# uml_TracedLiteralUnlimitedNatural class attributes and methods

# uml_TracedStructuredActivityNode class attributes and methods

# uml_TracedAbstraction class attributes and methods

# BasicActions_TracedOpaqueActionActivation class attributes and methods

# uml_TracedParameterSet class attributes and methods

# uml_TracedReadStructuralFeatureAction class attributes and methods

# uml_TracedMergeNode class attributes and methods

# uml_TracedRedefinableTemplateSignature class attributes and methods

# uml_TracedCreateLinkAction class attributes and methods

# uml_TracedGeneralization class attributes and methods

# uml_TracedPartDecomposition class attributes and methods

# Kernel_TracedLiteralBooleanEvaluation class attributes and methods

# uml_TracedReadLinkObjectEndQualifierAction class attributes and methods

# uml_TracedTemplateParameterSubstitution class attributes and methods

# uml_TracedExtend class attributes and methods

# uml_TracedReadVariableAction class attributes and methods

# uml_TracedMessage class attributes and methods

# uml_TracedOperationTemplateParameter class attributes and methods

# uml_TracedInitialNode class attributes and methods

# uml_TracedLiteralInteger class attributes and methods

# uml_TracedClearVariableAction class attributes and methods

# IntermediateActivities_TracedDecisionNodeActivation class attributes and methods

# uml_TracedProfileApplication class attributes and methods

# uml_TracedTemplateParameter class attributes and methods

# uml_TracedLiteralBoolean class attributes and methods

# uml_TracedQualifierValue class attributes and methods

# uml_TracedMessageOccurrenceSpecification class attributes and methods

# uml_TracedDurationConstraint class attributes and methods

# uml_TracedImage class attributes and methods

# uml_TracedActionInputPin class attributes and methods

# uml_TracedTrigger class attributes and methods

# uml_TracedConnectorEnd class attributes and methods

# uml_TracedProfile class attributes and methods

# uml_TracedInterval class attributes and methods

# IntermediateActivities_TracedForkNodeActivation class attributes and methods

# uml_TracedIntervalConstraint class attributes and methods

# uml_TracedInstanceSpecification class attributes and methods

# uml_TracedCallOperationAction class attributes and methods

# IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution class attributes and methods

# uml_TracedReadIsClassifiedObjectAction class attributes and methods

# uml_TracedProtocolStateMachine class attributes and methods

# uml_TracedOutputPin class attributes and methods

# uml_TracedValuePin class attributes and methods

# uml_TracedDecisionNode class attributes and methods

# uml_TracedValueSpecificationAction class attributes and methods

# uml_TracedRegion class attributes and methods

# uml_TracedInterruptibleActivityRegion class attributes and methods

# uml_TracedDestroyLinkAction class attributes and methods

# IntermediateActivities_TracedActivityParameterNodeActivation class attributes and methods

# uml_TracedInteractionOperand class attributes and methods

# uml_TracedInformationFlow class attributes and methods

# uml_TracedPseudostate class attributes and methods

# uml_TracedUseCase class attributes and methods

# uml_TracedReplyAction class attributes and methods

# uml_TracedFinalState class attributes and methods

# IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution class attributes and methods

# uml_TracedCombinedFragment class attributes and methods

# uml_TracedClause class attributes and methods

# uml_TracedInstanceValue class attributes and methods

# uml_TracedDependency class attributes and methods

# uml_TracedTimeExpression class attributes and methods

# IntermediateActions_TracedCreateObjectActionActivation class attributes and methods

# uml_TracedManifestation class attributes and methods

# uml_TracedReadExtentAction class attributes and methods

# BasicActions_TracedInputPinActivation class attributes and methods

# uml_TracedTransition class attributes and methods

# uml_TracedLinkEndData class attributes and methods

# uml_TracedNode class attributes and methods

# uml_TracedPackageMerge class attributes and methods

# uml_TracedModel class attributes and methods

# uml_TracedObjectFlow class attributes and methods

# uml_TracedChangeEvent class attributes and methods

# uml_TracedForkNode class attributes and methods

# uml_TracedSignal class attributes and methods

# uml_TracedComment class attributes and methods

# uml_TracedLiteralNull class attributes and methods

# uml_TracedExpansionNode class attributes and methods

# uml_TracedDestroyObjectAction class attributes and methods

# uml_TracedRaiseExceptionAction class attributes and methods

# uml_TracedAddVariableValueAction class attributes and methods

# uml_TracedClearAssociationAction class attributes and methods

# uml_TracedTestIdentityAction class attributes and methods

# uml_TracedReception class attributes and methods

# uml_TracedOperation class attributes and methods

# uml_TracedPackageImport class attributes and methods

# uml_TracedExecutionOccurrenceSpecification class attributes and methods

# uml_TracedExceptionHandler class attributes and methods

# uml_TracedVariable class attributes and methods

# uml_TracedControlFlow class attributes and methods

# uml_TracedAssociation class attributes and methods

# uml_TracedStateInvariant class attributes and methods

# uml_TracedLiteralReal class attributes and methods

# uml_TracedRemoveVariableValueAction class attributes and methods

# uml_TracedInteractionUse class attributes and methods

# uml_TracedGate class attributes and methods

# uml_TracedGeneralOrdering class attributes and methods

# uml_TracedCallBehaviorAction class attributes and methods

# uml_TracedReclassifyObjectAction class attributes and methods

# uml_TracedDevice class attributes and methods

# uml_TracedSubstitution class attributes and methods

# uml_TracedConnectionPointReference class attributes and methods

# uml_TracedActionExecutionSpecification class attributes and methods

# uml_TracedReadSelfAction class attributes and methods

# uml_TracedAcceptCallAction class attributes and methods

# uml_TracedActivity class attributes and methods

# uml_TracedTemplateBinding class attributes and methods

# uml_TracedClearStructuralFeatureAction class attributes and methods

# uml_TracedLinkEndCreationData class attributes and methods

# Kernel_TracedLiteralIntegerEvaluation class attributes and methods

# uml_TracedOpaqueExpression class attributes and methods

# uml_TracedFunctionBehavior class attributes and methods

# uml_TracedDeploymentSpecification class attributes and methods

# uml_TracedBehaviorExecutionSpecification class attributes and methods

# uml_TracedUnmarshallAction class attributes and methods

# uml_TracedCentralBufferNode class attributes and methods

# umlTrace_Kernel_TracedObject class attributes and methods

# TracedExtensionalValue class attributes and methods

# uml_TracedActor class attributes and methods

# umlTrace_Kernel_TracedIntegerValue class attributes and methods

# TracedPrimitiveValue class attributes and methods

# umlTrace_Kernel_TracedLiteralEvaluation class attributes and methods

# TracedEvaluation class attributes and methods

# umlTrace_Kernel_TracedValue class attributes and methods

# TracedSemanticVisitor class attributes and methods

# umlTrace_Kernel_TracedPrimitiveValue class attributes and methods

# TracedValue class attributes and methods

# umlTrace_Kernel_TracedEvaluation class attributes and methods

# umlTrace_Kernel_TracedBooleanValue class attributes and methods

# umlTrace_Kernel_TracedLiteralBooleanEvaluation class attributes and methods

# TracedLiteralEvaluation class attributes and methods

# umlTrace_Kernel_TracedReference class attributes and methods

# TracedStructuredValue class attributes and methods

# umlTrace_Kernel_TracedCompoundValue class attributes and methods

# umlTrace_Kernel_TracedFeatureValue class attributes and methods

# umlTrace_Kernel_TracedStructuredValue class attributes and methods

# umlTrace_Kernel_TracedExtensionalValue class attributes and methods

# TracedCompoundValue class attributes and methods

# umlTrace_Kernel_TracedLiteralIntegerEvaluation class attributes and methods

# umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution class attributes and methods

# TracedExecution class attributes and methods

# umlTrace_BasicBehaviors_TracedParameterValue class attributes and methods

# umlTrace_BasicBehaviors_TracedExecution class attributes and methods

# TracedObject class attributes and methods

# umlTrace_IntermediateActivities_TracedForkedToken class attributes and methods

# TracedToken class attributes and methods

# umlTrace_IntermediateActivities_TracedJoinNodeActivation class attributes and methods

# TracedControlNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedInitialNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedObjectNodeActivation class attributes and methods

# TracedActivityNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup class attributes and methods

# umlTrace_IntermediateActivities_TracedMergeNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedControlToken class attributes and methods

# umlTrace_IntermediateActivities_TracedObjectToken class attributes and methods

# umlTrace_IntermediateActivities_TracedDecisionNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedOffer class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation class attributes and methods

# TracedObjectNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityEdgeInstance class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedForkNodeActivation class attributes and methods

# umlTrace_IntermediateActivities_TracedToken class attributes and methods

# umlTrace_IntermediateActivities_TracedActivityExecution class attributes and methods

# umlTrace_Loci_TracedExecutionFactory class attributes and methods

# umlTrace_Loci_TracedLocus class attributes and methods

# umlTrace_Loci_TracedSemanticVisitor class attributes and methods

# umlTrace_Loci_TracedExecutor class attributes and methods

# umlTrace_IntermediateActivities_TracedControlNodeActivation class attributes and methods

# umlTrace_IntermediateActions_TracedValueSpecificationActionActivation class attributes and methods

# umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation class attributes and methods

# TracedStructuralFeatureActionActivation class attributes and methods

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

# umlTrace_BasicActions_TracedCallActionActivation class attributes and methods

# TracedInvocationActionActivation class attributes and methods

# umlTrace_Loci_TracedExecutionEnvironment class attributes and methods

# umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation class attributes and methods

# TracedActionActivation class attributes and methods

# umlTrace_BasicActions_TracedPinActivation class attributes and methods

# umlTrace_BasicActions_TracedInputPinActivation class attributes and methods

# umlTrace_BasicActions_TracedInvocationActionActivation class attributes and methods

# umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution class attributes and methods

# umlTrace_Input_TracedInputParameterValues class attributes and methods

# umlTrace_uml_TracedStructuralFeature class attributes and methods

# uml_TracedFeature class attributes and methods

# uml_TracedTypedElement class attributes and methods

# uml_TracedMultiplicityElement class attributes and methods

# umlTrace_uml_TracedConnector class attributes and methods

# TracedFeature class attributes and methods

# uml_TracedBehavior class attributes and methods

# uml_umlTrace_Connector class attributes and methods

# umlTrace_uml_TracedOpaqueAction class attributes and methods

# TracedAction class attributes and methods

# umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution class attributes and methods

# TracedOpaqueBehaviorExecution class attributes and methods

# umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution class attributes and methods

# umlTrace_uml_TracedDataType class attributes and methods

# TracedClassifier class attributes and methods

# uml_umlTrace_DataType class attributes and methods

# umlTrace_uml_TracedCommunicationPath class attributes and methods

# TracedAssociation class attributes and methods

# umlTrace_uml_TracedLinkAction class attributes and methods

# umlTrace_uml_TracedProperty class attributes and methods

# uml_TracedConnectableElement class attributes and methods

# uml_TracedDeploymentTarget class attributes and methods

# uml_umlTrace_OpaqueAction class attributes and methods

# uml_umlTrace_Property class attributes and methods

# umlTrace_uml_TracedContinuation class attributes and methods

# TracedInteractionFragment class attributes and methods

# uml_umlTrace_Continuation class attributes and methods

# umlTrace_uml_TracedRemoveStructuralFeatureValueAction class attributes and methods

# TracedWriteStructuralFeatureAction class attributes and methods

# uml_umlTrace_RemoveStructuralFeatureValueAction class attributes and methods

# umlTrace_uml_TracedSendSignalAction class attributes and methods

# TracedInvocationAction class attributes and methods

# umlTrace_uml_TracedOpaqueBehavior class attributes and methods

# TracedBehavior class attributes and methods

# umlTrace_uml_TracedArtifact class attributes and methods

# uml_TracedClassifier class attributes and methods

# uml_TracedDeployedArtifact class attributes and methods

# uml_umlTrace_Artifact class attributes and methods

# umlTrace_uml_TracedTimeConstraint class attributes and methods

# TracedIntervalConstraint class attributes and methods

# umlTrace_uml_TracedInterfaceRealization class attributes and methods

# TracedRealization class attributes and methods

# uml_TracedBehavioredClassifier class attributes and methods

# umlTrace_uml_TracedObjectNode class attributes and methods

# uml_umlTrace_SendSignalAction class attributes and methods

# umlTrace_uml_TracedActivityFinalNode class attributes and methods

# TracedFinalNode class attributes and methods

# uml_umlTrace_ActivityFinalNode class attributes and methods

# umlTrace_uml_TracedDurationObservation class attributes and methods

# TracedObservation class attributes and methods

# uml_TracedNamedElement class attributes and methods

# uml_umlTrace_DurationObservation class attributes and methods

# umlTrace_uml_TracedAcceptEventAction class attributes and methods

# uml_umlTrace_AcceptEventAction class attributes and methods

# umlTrace_uml_TracedEnumerationLiteral class attributes and methods

# TracedInstanceSpecification class attributes and methods

# umlTrace_uml_TracedAddStructuralFeatureValueAction class attributes and methods

# uml_umlTrace_AddStructuralFeatureValueAction class attributes and methods

# umlTrace_uml_TracedExpression class attributes and methods

# TracedValueSpecification class attributes and methods

# uml_umlTrace_Expression class attributes and methods

# umlTrace_uml_TracedConsiderIgnoreFragment class attributes and methods

# TracedCombinedFragment class attributes and methods

# umlTrace_uml_TracedDataStoreNode class attributes and methods

# TracedCentralBufferNode class attributes and methods

# umlTrace_uml_TracedFlowFinalNode class attributes and methods

# uml_umlTrace_FlowFinalNode class attributes and methods

# umlTrace_uml_TracedInteractionFragment class attributes and methods

# TracedNamedElement class attributes and methods

# umlTrace_uml_TracedClassifier class attributes and methods

# umlTrace_uml_TracedReadLinkAction class attributes and methods

# TracedLinkAction class attributes and methods

# uml_umlTrace_ReadLinkAction class attributes and methods

# uml_TracedNamespace class attributes and methods

# uml_TracedRedefinableElement class attributes and methods

# uml_TracedType class attributes and methods

# uml_TracedTemplateableElement class attributes and methods

# umlTrace_uml_TracedInformationItem class attributes and methods

# uml_umlTrace_InformationItem class attributes and methods

# umlTrace_uml_TracedCollaboration class attributes and methods

# uml_TracedStructuredClassifier class attributes and methods

# uml_umlTrace_Collaboration class attributes and methods

# umlTrace_uml_TracedMessageEnd class attributes and methods

# umlTrace_uml_TracedTemplateSignature class attributes and methods

# TracedElement class attributes and methods

# uml_umlTrace_TemplateSignature class attributes and methods

# umlTrace_uml_TracedBroadcastSignalAction class attributes and methods

# uml_umlTrace_BroadcastSignalAction class attributes and methods

# umlTrace_uml_TracedDeployment class attributes and methods

# TracedDependency class attributes and methods

# umlTrace_uml_TracedPort class attributes and methods

# TracedProperty class attributes and methods

# umlTrace_uml_TracedTimeInterval class attributes and methods

# TracedInterval class attributes and methods

# umlTrace_uml_TracedAction class attributes and methods

# TracedExecutableNode class attributes and methods

# umlTrace_uml_TracedExtension class attributes and methods

# umlTrace_uml_TracedDirectedRelationship class attributes and methods

# TracedRelationship class attributes and methods

# umlTrace_uml_TracedTimeEvent class attributes and methods

# TracedEvent class attributes and methods

# uml_umlTrace_TimeEvent class attributes and methods

# umlTrace_uml_TracedPackageableElement class attributes and methods

# uml_TracedParameterableElement class attributes and methods

# umlTrace_uml_TracedType class attributes and methods

# TracedPackageableElement class attributes and methods

# umlTrace_uml_TracedProtocolTransition class attributes and methods

# TracedTransition class attributes and methods

# umlTrace_uml_TracedPackage class attributes and methods

# uml_TracedPackageableElement class attributes and methods

# uml_umlTrace_Package class attributes and methods

# umlTrace_uml_TracedBehavioredClassifier class attributes and methods

# umlTrace_uml_TracedStructuralFeatureAction class attributes and methods

# umlTrace_uml_TracedConstraint class attributes and methods

# uml_umlTrace_Constraint class attributes and methods

# umlTrace_uml_TracedMultiplicityElement class attributes and methods

# umlTrace_uml_TracedLiteralSpecification class attributes and methods

# umlTrace_uml_TracedGeneralizationSet class attributes and methods

# umlTrace_uml_TracedReduceAction class attributes and methods

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

# uml_umlTrace_GeneralizationSet class attributes and methods

# umlTrace_uml_TracedElement class attributes and methods

# TracedEModelElement class attributes and methods

# umlTrace_uml_TracedComponentRealization class attributes and methods

# umlTrace_uml_TracedAssociationClass class attributes and methods

# umlTrace_uml_TracedSlot class attributes and methods

# umlTrace_uml_TracedWriteStructuralFeatureAction class attributes and methods

# TracedStructuralFeatureAction class attributes and methods

# uml_umlTrace_Slot class attributes and methods

# umlTrace_uml_TracedSignalEvent class attributes and methods

# TracedMessageEvent class attributes and methods

# uml_umlTrace_SignalEvent class attributes and methods

# umlTrace_uml_TracedExtensionPoint class attributes and methods

# uml_umlTrace_ExtensionPoint class attributes and methods

# umlTrace_uml_TracedJoinNode class attributes and methods

# TracedControlNode class attributes and methods

# uml_umlTrace_JoinNode class attributes and methods

# umlTrace_uml_TracedStartObjectBehaviorAction class attributes and methods

# TracedCallAction class attributes and methods

# uml_umlTrace_StartObjectBehaviorAction class attributes and methods

# uml_umlTrace_ElementImport class attributes and methods

# umlTrace_uml_TracedCreateObjectAction class attributes and methods

# uml_umlTrace_CreateObjectAction class attributes and methods

# umlTrace_uml_TracedExecutionEnvironment class attributes and methods

# TracedNode class attributes and methods

# umlTrace_uml_TracedOccurrenceSpecification class attributes and methods

# uml_umlTrace_OccurrenceSpecification class attributes and methods

# umlTrace_uml_TracedStringExpression class attributes and methods

# umlTrace_uml_TracedElementImport class attributes and methods

# TracedDirectedRelationship class attributes and methods

# umlTrace_uml_TracedInterface class attributes and methods

# uml_umlTrace_Interface class attributes and methods

# umlTrace_uml_TracedConditionalNode class attributes and methods

# umlTrace_uml_TracedDeployedArtifact class attributes and methods

# umlTrace_uml_TracedStereotype class attributes and methods

# TracedClass class attributes and methods

# uml_umlTrace_ReadLinkObjectEndAction class attributes and methods

# umlTrace_uml_TracedAnyReceiveEvent class attributes and methods

# uml_umlTrace_AnyReceiveEvent class attributes and methods

# umlTrace_uml_TracedNamedElement class attributes and methods

# umlTrace_uml_TracedComponent class attributes and methods

# umlTrace_uml_TracedReadLinkObjectEndAction class attributes and methods

# umlTrace_uml_TracedExtensionEnd class attributes and methods

# umlTrace_uml_TracedStateMachine class attributes and methods

# umlTrace_uml_TracedValueSpecification class attributes and methods

# umlTrace_uml_TracedInteraction class attributes and methods

# uml_TracedInteractionFragment class attributes and methods

# umlTrace_uml_TracedLiteralString class attributes and methods

# TracedLiteralSpecification class attributes and methods

# uml_umlTrace_LiteralString class attributes and methods

# umlTrace_uml_TracedRealization class attributes and methods

# TracedAbstraction class attributes and methods

# umlTrace_uml_TracedStartClassifierBehaviorAction class attributes and methods

# uml_umlTrace_StartClassifierBehaviorAction class attributes and methods

# umlTrace_uml_TracedMessageEvent class attributes and methods

# umlTrace_uml_TracedCallEvent class attributes and methods

# uml_umlTrace_CallEvent class attributes and methods

# umlTrace_uml_TracedConnectableElementTemplateParameter class attributes and methods

# TracedTemplateParameter class attributes and methods

# umlTrace_uml_TracedRelationship class attributes and methods

# umlTrace_uml_TracedSendObjectAction class attributes and methods

# uml_TracedAction class attributes and methods

# umlTrace_uml_TracedLifeline class attributes and methods

# uml_umlTrace_Lifeline class attributes and methods

# umlTrace_uml_TracedExecutionSpecification class attributes and methods

# umlTrace_uml_TracedTimeObservation class attributes and methods

# uml_umlTrace_SendObjectAction class attributes and methods

# umlTrace_uml_TracedExpansionRegion class attributes and methods

# umlTrace_uml_TracedWriteVariableAction class attributes and methods

# TracedVariableAction class attributes and methods

# umlTrace_uml_TracedLoopNode class attributes and methods

# uml_umlTrace_TimeObservation class attributes and methods

# umlTrace_uml_TracedCreateLinkObjectAction class attributes and methods

# TracedCreateLinkAction class attributes and methods

# umlTrace_uml_TracedPrimitiveType class attributes and methods

# TracedDataType class attributes and methods

# umlTrace_uml_TracedProtocolConformance class attributes and methods

# uml_umlTrace_ProtocolConformance class attributes and methods

# umlTrace_uml_TracedEnumeration class attributes and methods

# umlTrace_uml_TracedCollaborationUse class attributes and methods

# umlTrace_uml_TracedActivityPartition class attributes and methods

# TracedActivityGroup class attributes and methods

# uml_umlTrace_ActivityPartition class attributes and methods

# umlTrace_uml_TracedVariableAction class attributes and methods

# umlTrace_uml_TracedLinkEndDestructionData class attributes and methods

# TracedLinkEndData class attributes and methods

# umlTrace_uml_TracedDurationInterval class attributes and methods

# umlTrace_uml_TracedInclude class attributes and methods

# uml_TracedDirectedRelationship class attributes and methods

# uml_umlTrace_CollaborationUse class attributes and methods

# uml_umlTrace_Include class attributes and methods

# umlTrace_uml_TracedActivityNode class attributes and methods

# ActivityContent class attributes and methods

# uml_TracedActivityGroup class attributes and methods

# umlTrace_uml_TracedDestructionOccurrenceSpecification class attributes and methods

# TracedMessageOccurrenceSpecification class attributes and methods

# umlTrace_uml_TracedState class attributes and methods

# uml_TracedVertex class attributes and methods

# umlTrace_uml_TracedCallAction class attributes and methods

# umlTrace_uml_TracedTemplateableElement class attributes and methods

# umlTrace_uml_TracedBehavior class attributes and methods

# uml_TracedBehavioralFeature class attributes and methods

# uml_umlTrace_State class attributes and methods

# umlTrace_uml_TracedClassifierTemplateParameter class attributes and methods

# umlTrace_uml_TracedActivityParameterNode class attributes and methods

# TracedObjectNode class attributes and methods

# uml_umlTrace_ActivityParameterNode class attributes and methods

# umlTrace_uml_TracedParameterSet class attributes and methods

# uml_umlTrace_ParameterSet class attributes and methods

# umlTrace_uml_TracedDuration class attributes and methods

# uml_TracedObservation class attributes and methods

# uml_umlTrace_Class class attributes and methods

# umlTrace_uml_TracedUsage class attributes and methods

# umlTrace_uml_TracedLiteralUnlimitedNatural class attributes and methods

# uml_umlTrace_LiteralUnlimitedNatural class attributes and methods

# umlTrace_uml_TracedStructuredActivityNode class attributes and methods

# uml_umlTrace_Duration class attributes and methods

# umlTrace_uml_TracedClass class attributes and methods

# uml_TracedEncapsulatedClassifier class attributes and methods

# uml_umlTrace_StructuredActivityNode class attributes and methods

# umlTrace_uml_TracedAbstraction class attributes and methods

# umlTrace_uml_TracedReadStructuralFeatureAction class attributes and methods

# uml_umlTrace_ReadStructuralFeatureAction class attributes and methods

# umlTrace_uml_TracedMergeNode class attributes and methods

# uml_umlTrace_MergeNode class attributes and methods

# umlTrace_uml_TracedRedefinableTemplateSignature class attributes and methods

# umlTrace_uml_TracedCreateLinkAction class attributes and methods

# TracedWriteLinkAction class attributes and methods

# uml_umlTrace_CreateLinkAction class attributes and methods

# umlTrace_uml_TracedGeneralization class attributes and methods

# uml_umlTrace_Generalization class attributes and methods

# umlTrace_uml_TracedPartDecomposition class attributes and methods

# TracedInteractionUse class attributes and methods

# umlTrace_uml_TracedTypedElement class attributes and methods

# umlTrace_uml_TracedOperationTemplateParameter class attributes and methods

# umlTrace_uml_TracedReadLinkObjectEndQualifierAction class attributes and methods

# uml_umlTrace_ReadLinkObjectEndQualifierAction class attributes and methods

# umlTrace_uml_TracedTemplateParameterSubstitution class attributes and methods

# uml_umlTrace_TemplateParameterSubstitution class attributes and methods

# umlTrace_uml_TracedExtend class attributes and methods

# uml_umlTrace_Extend class attributes and methods

# umlTrace_uml_TracedReadVariableAction class attributes and methods

# uml_umlTrace_ReadVariableAction class attributes and methods

# umlTrace_uml_TracedMessage class attributes and methods

# uml_TracedMessageEnd class attributes and methods

# umlTrace_uml_TracedQualifierValue class attributes and methods

# uml_umlTrace_QualifierValue class attributes and methods

# umlTrace_uml_TracedInitialNode class attributes and methods

# uml_umlTrace_InitialNode class attributes and methods

# umlTrace_uml_TracedLiteralInteger class attributes and methods

# uml_umlTrace_LiteralInteger class attributes and methods

# umlTrace_uml_TracedClearVariableAction class attributes and methods

# uml_umlTrace_ClearVariableAction class attributes and methods

# umlTrace_uml_TracedProfileApplication class attributes and methods

# uml_umlTrace_Message class attributes and methods

# umlTrace_uml_TracedLiteralBoolean class attributes and methods

# uml_umlTrace_LiteralBoolean class attributes and methods

# umlTrace_uml_TracedTemplateParameter class attributes and methods

# uml_umlTrace_TemplateParameter class attributes and methods

# umlTrace_uml_TracedConnectorEnd class attributes and methods

# TracedMultiplicityElement class attributes and methods

# uml_umlTrace_ProfileApplication class attributes and methods

# umlTrace_uml_TracedParameterableElement class attributes and methods

# umlTrace_uml_TracedMessageOccurrenceSpecification class attributes and methods

# umlTrace_uml_TracedDurationConstraint class attributes and methods

# umlTrace_uml_TracedImage class attributes and methods

# uml_umlTrace_Image class attributes and methods

# umlTrace_uml_TracedEncapsulatedClassifier class attributes and methods

# TracedStructuredClassifier class attributes and methods

# umlTrace_uml_TracedParameter class attributes and methods

# uml_umlTrace_Parameter class attributes and methods

# umlTrace_uml_TracedActionInputPin class attributes and methods

# TracedInputPin class attributes and methods

# uml_umlTrace_ConnectorEnd class attributes and methods

# uml_umlTrace_Trigger class attributes and methods

# umlTrace_uml_TracedCallOperationAction class attributes and methods

# uml_umlTrace_CallOperationAction class attributes and methods

# umlTrace_uml_TracedProfile class attributes and methods

# TracedPackage class attributes and methods

# umlTrace_uml_TracedInterval class attributes and methods

# uml_umlTrace_Interval class attributes and methods

# umlTrace_uml_TracedTrigger class attributes and methods

# uml_TracedEvent class attributes and methods

# uml_umlTrace_InstanceSpecification class attributes and methods

# umlTrace_uml_TracedValuePin class attributes and methods

# umlTrace_uml_TracedReadIsClassifiedObjectAction class attributes and methods

# uml_umlTrace_ReadIsClassifiedObjectAction class attributes and methods

# umlTrace_uml_TracedIntervalConstraint class attributes and methods

# umlTrace_uml_TracedInstanceSpecification class attributes and methods

# uml_umlTrace_OutputPin class attributes and methods

# umlTrace_uml_TracedDecisionNode class attributes and methods

# uml_umlTrace_DecisionNode class attributes and methods

# umlTrace_uml_TracedValueSpecificationAction class attributes and methods

# uml_umlTrace_ValueSpecificationAction class attributes and methods

# umlTrace_uml_TracedRegion class attributes and methods

# umlTrace_uml_TracedProtocolStateMachine class attributes and methods

# TracedStateMachine class attributes and methods

# umlTrace_uml_TracedOutputPin class attributes and methods

# uml_umlTrace_Region class attributes and methods

# umlTrace_uml_TracedInterruptibleActivityRegion class attributes and methods

# uml_umlTrace_InterruptibleActivityRegion class attributes and methods

# umlTrace_uml_TracedDestroyLinkAction class attributes and methods

# uml_umlTrace_DestroyLinkAction class attributes and methods

# umlTrace_uml_TracedFinalState class attributes and methods

# TracedState class attributes and methods

# umlTrace_uml_TracedActivityGroup class attributes and methods

# umlTrace_uml_TracedInteractionOperand class attributes and methods

# uml_umlTrace_InteractionOperand class attributes and methods

# umlTrace_uml_TracedActivityEdge class attributes and methods

# umlTrace_uml_TracedInformationFlow class attributes and methods

# uml_TracedRelationship class attributes and methods

# uml_umlTrace_InformationFlow class attributes and methods

# umlTrace_uml_TracedPseudostate class attributes and methods

# TracedVertex class attributes and methods

# uml_umlTrace_Pseudostate class attributes and methods

# umlTrace_uml_TracedControlNode class attributes and methods

# TracedActivityNode class attributes and methods

# umlTrace_uml_TracedUseCase class attributes and methods

# TracedBehavioredClassifier class attributes and methods

# uml_umlTrace_UseCase class attributes and methods

# umlTrace_uml_TracedReplyAction class attributes and methods

# uml_umlTrace_ReplyAction class attributes and methods

# umlTrace_uml_TracedCombinedFragment class attributes and methods

# uml_umlTrace_CombinedFragment class attributes and methods

# umlTrace_uml_TracedWriteLinkAction class attributes and methods

# umlTrace_uml_TracedClause class attributes and methods

# uml_umlTrace_Clause class attributes and methods

# umlTrace_uml_TracedInstanceValue class attributes and methods

# uml_umlTrace_InstanceValue class attributes and methods

# umlTrace_uml_TracedDependency class attributes and methods

# uml_umlTrace_Dependency class attributes and methods

# umlTrace_uml_TracedTimeExpression class attributes and methods

# uml_umlTrace_TimeExpression class attributes and methods

# umlTrace_uml_TracedManifestation class attributes and methods

# umlTrace_uml_TracedReadExtentAction class attributes and methods

# uml_umlTrace_ReadExtentAction class attributes and methods

# umlTrace_uml_TracedTransition class attributes and methods

# uml_umlTrace_Transition class attributes and methods

# umlTrace_uml_TracedLinkEndData class attributes and methods

# uml_umlTrace_ObjectFlow class attributes and methods

# uml_umlTrace_LinkEndData class attributes and methods

# umlTrace_uml_TracedNode class attributes and methods

# umlTrace_uml_TracedPackageMerge class attributes and methods

# uml_umlTrace_PackageMerge class attributes and methods

# umlTrace_uml_TracedModel class attributes and methods

# umlTrace_uml_TracedObjectFlow class attributes and methods

# TracedActivityEdge class attributes and methods

# umlTrace_uml_TracedEvent class attributes and methods

# umlTrace_uml_TracedChangeEvent class attributes and methods

# uml_umlTrace_ChangeEvent class attributes and methods

# umlTrace_uml_TracedRedefinableElement class attributes and methods

# umlTrace_uml_TracedDestroyObjectAction class attributes and methods

# uml_umlTrace_DestroyObjectAction class attributes and methods

# umlTrace_uml_TracedForkNode class attributes and methods

# uml_umlTrace_ForkNode class attributes and methods

# umlTrace_uml_TracedFinalNode class attributes and methods

# umlTrace_uml_TracedSignal class attributes and methods

# uml_umlTrace_Signal class attributes and methods

# umlTrace_uml_TracedComment class attributes and methods

# uml_umlTrace_Comment class attributes and methods

# umlTrace_uml_TracedStructuredClassifier class attributes and methods

# umlTrace_uml_TracedLiteralNull class attributes and methods

# uml_umlTrace_LiteralNull class attributes and methods

# umlTrace_uml_TracedExpansionNode class attributes and methods

# uml_umlTrace_ExpansionNode class attributes and methods

# umlTrace_uml_TracedReception class attributes and methods

# TracedBehavioralFeature class attributes and methods

# uml_umlTrace_Reception class attributes and methods

# umlTrace_uml_TracedRaiseExceptionAction class attributes and methods

# uml_umlTrace_RaiseExceptionAction class attributes and methods

# umlTrace_uml_TracedBehavioralFeature class attributes and methods

# umlTrace_uml_TracedAddVariableValueAction class attributes and methods

# TracedWriteVariableAction class attributes and methods

# uml_umlTrace_AddVariableValueAction class attributes and methods

# umlTrace_uml_TracedClearAssociationAction class attributes and methods

# uml_umlTrace_ClearAssociationAction class attributes and methods

# umlTrace_uml_TracedPin class attributes and methods

# uml_TracedObjectNode class attributes and methods

# umlTrace_uml_TracedTestIdentityAction class attributes and methods

# uml_umlTrace_TestIdentityAction class attributes and methods

# umlTrace_uml_TracedControlFlow class attributes and methods

# uml_umlTrace_ControlFlow class attributes and methods

# umlTrace_uml_TracedOperation class attributes and methods

# uml_umlTrace_Operation class attributes and methods

# umlTrace_uml_TracedConnectableElement class attributes and methods

# umlTrace_uml_TracedVertex class attributes and methods

# umlTrace_uml_TracedObservation class attributes and methods

# umlTrace_uml_TracedNamespace class attributes and methods

# umlTrace_uml_TracedPackageImport class attributes and methods

# uml_umlTrace_PackageImport class attributes and methods

# umlTrace_uml_TracedExecutionOccurrenceSpecification class attributes and methods

# TracedOccurrenceSpecification class attributes and methods

# uml_TracedExecutionSpecification class attributes and methods

# umlTrace_uml_TracedExceptionHandler class attributes and methods

# uml_umlTrace_ExceptionHandler class attributes and methods

# umlTrace_uml_TracedVariable class attributes and methods

# uml_umlTrace_Variable class attributes and methods

# umlTrace_uml_TracedInteractionUse class attributes and methods

# uml_umlTrace_InteractionUse class attributes and methods

# umlTrace_uml_TracedAssociation class attributes and methods

# uml_umlTrace_Association class attributes and methods

# umlTrace_uml_TracedStateInvariant class attributes and methods

# uml_umlTrace_StateInvariant class attributes and methods

# umlTrace_uml_TracedLiteralReal class attributes and methods

# uml_umlTrace_LiteralReal class attributes and methods

# umlTrace_uml_TracedInvocationAction class attributes and methods

# umlTrace_uml_TracedRemoveVariableValueAction class attributes and methods

# uml_umlTrace_RemoveVariableValueAction class attributes and methods

# umlTrace_uml_TracedDevice class attributes and methods

# umlTrace_uml_TracedSubstitution class attributes and methods

# umlTrace_uml_TracedGate class attributes and methods

# TracedMessageEnd class attributes and methods

# uml_umlTrace_Gate class attributes and methods

# umlTrace_uml_TracedDeploymentTarget class attributes and methods

# umlTrace_uml_TracedGeneralOrdering class attributes and methods

# uml_umlTrace_GeneralOrdering class attributes and methods

# umlTrace_uml_TracedCallBehaviorAction class attributes and methods

# uml_umlTrace_CallBehaviorAction class attributes and methods

# umlTrace_uml_TracedReclassifyObjectAction class attributes and methods

# uml_umlTrace_ReclassifyObjectAction class attributes and methods

# umlTrace_uml_TracedActivity class attributes and methods

# umlTrace_uml_TracedConnectionPointReference class attributes and methods

# uml_umlTrace_ConnectionPointReference class attributes and methods

# umlTrace_uml_TracedActionExecutionSpecification class attributes and methods

# TracedExecutionSpecification class attributes and methods

# uml_umlTrace_ActionExecutionSpecification class attributes and methods

# umlTrace_uml_TracedReadSelfAction class attributes and methods

# uml_umlTrace_ReadSelfAction class attributes and methods

# umlTrace_uml_TracedAcceptCallAction class attributes and methods

# TracedAcceptEventAction class attributes and methods

# umlTrace_uml_TracedLinkEndCreationData class attributes and methods

# umlTrace_uml_TracedTemplateBinding class attributes and methods

# uml_umlTrace_TemplateBinding class attributes and methods

# umlTrace_uml_TracedClearStructuralFeatureAction class attributes and methods

# uml_umlTrace_ClearStructuralFeatureAction class attributes and methods

# umlTrace_uml_TracedOpaqueExpression class attributes and methods

# uml_umlTrace_OpaqueExpression class attributes and methods

# umlTrace_uml_TracedFunctionBehavior class attributes and methods

# TracedOpaqueBehavior class attributes and methods

# umlTrace_uml_TracedDeploymentSpecification class attributes and methods

# TracedArtifact class attributes and methods

# umlTrace_uml_TracedActor class attributes and methods

# uml_umlTrace_Actor class attributes and methods

# umlTrace_uml_TracedBehaviorExecutionSpecification class attributes and methods

# uml_umlTrace_BehaviorExecutionSpecification class attributes and methods

# umlTrace_uml_TracedExecutableNode class attributes and methods

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
tracedObjects3: BinaryAssociation = BinaryAssociation(
    name="tracedObjects3",
    ends={
        Property(name="TracedObjects", type=umlTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Trace4", type=TracedObjects, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
followingStep5: BinaryAssociation = BinaryAssociation(
    name="followingStep5",
    ends={
        Property(name="Steps6", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="SmallStep", type=SmallStep, multiplicity=Multiplicity(0, 1))
    }
)
integerValue_value_IntegerValue_Values15: BinaryAssociation = BinaryAssociation(
    name="integerValue_value_IntegerValue_Values15",
    ends={
        Property(name="Values16", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="IntegerValue_value_IntegerValue_Value", type=IntegerValue_value_IntegerValue_Value, multiplicity=Multiplicity(0, 9999))
    }
)
forkedToken_remainingOffersCount_Values17: BinaryAssociation = BinaryAssociation(
    name="forkedToken_remainingOffersCount_Values17",
    ends={
        Property(name="Values18", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_remainingOffersCount_Value", type=ForkedToken_remainingOffersCount_Value, multiplicity=Multiplicity(0, 9999))
    }
)
forkedToken_baseToken_Values19: BinaryAssociation = BinaryAssociation(
    name="forkedToken_baseToken_Values19",
    ends={
        Property(name="Values20", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_baseToken_Value", type=ForkedToken_baseToken_Value, multiplicity=Multiplicity(0, 9999))
    }
)
forkedToken_baseTokenIsWithdrawn_Values21: BinaryAssociation = BinaryAssociation(
    name="forkedToken_baseTokenIsWithdrawn_Values21",
    ends={
        Property(name="Values22", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_baseTokenIsWithdrawn_Value", type=ForkedToken_baseTokenIsWithdrawn_Value, multiplicity=Multiplicity(0, 9999))
    }
)
executionFactory_builtInTypes_Values23: BinaryAssociation = BinaryAssociation(
    name="executionFactory_builtInTypes_Values23",
    ends={
        Property(name="Values24", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ExecutionFactory_builtInTypes_Value", type=ExecutionFactory_builtInTypes_Value, multiplicity=Multiplicity(0, 9999))
    }
)
executionFactory_primitiveBehaviorPrototypes_Values25: BinaryAssociation = BinaryAssociation(
    name="executionFactory_primitiveBehaviorPrototypes_Values25",
    ends={
        Property(name="Values26", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ExecutionFactory_primitiveBehaviorPrototypes_Value", type=ExecutionFactory_primitiveBehaviorPrototypes_Value, multiplicity=Multiplicity(0, 9999))
    }
)
executionFactory_locus_ExecutionFactory_Values27: BinaryAssociation = BinaryAssociation(
    name="executionFactory_locus_ExecutionFactory_Values27",
    ends={
        Property(name="Values28", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ExecutionFactory_locus_ExecutionFactory_Value", type=ExecutionFactory_locus_ExecutionFactory_Value, multiplicity=Multiplicity(0, 9999))
    }
)
locus_factory_Values29: BinaryAssociation = BinaryAssociation(
    name="locus_factory_Values29",
    ends={
        Property(name="Values30", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Locus_factory_Value", type=Locus_factory_Value, multiplicity=Multiplicity(0, 9999))
    }
)
locus_extensionalValues_Values31: BinaryAssociation = BinaryAssociation(
    name="locus_extensionalValues_Values31",
    ends={
        Property(name="Values32", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Locus_extensionalValues_Value", type=Locus_extensionalValues_Value, multiplicity=Multiplicity(0, 9999))
    }
)
locus_executor_Values33: BinaryAssociation = BinaryAssociation(
    name="locus_executor_Values33",
    ends={
        Property(name="Values34", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Locus_executor_Value", type=Locus_executor_Value, multiplicity=Multiplicity(0, 9999))
    }
)
objectNodeActivation_offeredTokenCount_Values35: BinaryAssociation = BinaryAssociation(
    name="objectNodeActivation_offeredTokenCount_Values35",
    ends={
        Property(name="Values36", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjectNodeActivation_offeredTokenCount_Value", type=ObjectNodeActivation_offeredTokenCount_Value, multiplicity=Multiplicity(0, 9999))
    }
)
semanticVisitor_runtimeModelElement_Values37: BinaryAssociation = BinaryAssociation(
    name="semanticVisitor_runtimeModelElement_Values37",
    ends={
        Property(name="Values38", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="SemanticVisitor_runtimeModelElement_Value", type=SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(0, 9999))
    }
)
parameterValue_values_ParameterValue_Values39: BinaryAssociation = BinaryAssociation(
    name="parameterValue_values_ParameterValue_Values39",
    ends={
        Property(name="Values40", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ParameterValue_values_ParameterValue_Value", type=ParameterValue_values_ParameterValue_Value, multiplicity=Multiplicity(0, 9999))
    }
)
startedBigSteps7: BinaryAssociation = BinaryAssociation(
    name="startedBigSteps7",
    ends={
        Property(name="Steps8", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="BigStep", type=BigStep, multiplicity=Multiplicity(0, 9999))
    }
)
endedBigSteps9: BinaryAssociation = BinaryAssociation(
    name="endedBigSteps9",
    ends={
        Property(name="Steps11", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="BigStep10", type=BigStep, multiplicity=Multiplicity(0, 9999))
    }
)
object_types_Values12: BinaryAssociation = BinaryAssociation(
    name="object_types_Values12",
    ends={
        Property(name="Values", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Object_types_Value", type=Object_types_Value, multiplicity=Multiplicity(0, 9999))
    }
)
reference_referent_Values13: BinaryAssociation = BinaryAssociation(
    name="reference_referent_Values13",
    ends={
        Property(name="Values14", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Reference_referent_Value", type=Reference_referent_Value, multiplicity=Multiplicity(0, 9999))
    }
)
actionActivation_firing_Values45: BinaryAssociation = BinaryAssociation(
    name="actionActivation_firing_Values45",
    ends={
        Property(name="Values46", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionActivation_firing_Value", type=ActionActivation_firing_Value, multiplicity=Multiplicity(0, 9999))
    }
)
execution_parameterValues_Values47: BinaryAssociation = BinaryAssociation(
    name="execution_parameterValues_Values47",
    ends={
        Property(name="Values48", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Execution_parameterValues_Value", type=Execution_parameterValues_Value, multiplicity=Multiplicity(0, 9999))
    }
)
execution_context_Values49: BinaryAssociation = BinaryAssociation(
    name="execution_context_Values49",
    ends={
        Property(name="Values50", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Execution_context_Value", type=Execution_context_Value, multiplicity=Multiplicity(0, 9999))
    }
)
element_semanticVisitor_Values51: BinaryAssociation = BinaryAssociation(
    name="element_semanticVisitor_Values51",
    ends={
        Property(name="Values52", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Element_semanticVisitor_Value", type=Element_semanticVisitor_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivationGroup_nodeActivations_Values53: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivationGroup_nodeActivations_Values53",
    ends={
        Property(name="Values54", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivationGroup_nodeActivations_Value", type=ActivityNodeActivationGroup_nodeActivations_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivationGroup_activityExecution_Values55: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivationGroup_activityExecution_Values55",
    ends={
        Property(name="Values56", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivationGroup_activityExecution_Value", type=ActivityNodeActivationGroup_activityExecution_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivationGroup_edgeInstances_Values57: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivationGroup_edgeInstances_Values57",
    ends={
        Property(name="Values58", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivationGroup_edgeInstances_Value", type=ActivityNodeActivationGroup_edgeInstances_Value, multiplicity=Multiplicity(0, 9999))
    }
)
executor_locus_Executor_Values59: BinaryAssociation = BinaryAssociation(
    name="executor_locus_Executor_Values59",
    ends={
        Property(name="Values60", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Executor_locus_Executor_Value", type=Executor_locus_Executor_Value, multiplicity=Multiplicity(0, 9999))
    }
)
primitiveValue_type_Values61: BinaryAssociation = BinaryAssociation(
    name="primitiveValue_type_Values61",
    ends={
        Property(name="Values62", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="PrimitiveValue_type_Value", type=PrimitiveValue_type_Value, multiplicity=Multiplicity(0, 9999))
    }
)
evaluation_specification_Evaluation_Values63: BinaryAssociation = BinaryAssociation(
    name="evaluation_specification_Evaluation_Values63",
    ends={
        Property(name="Values64", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Evaluation_specification_Evaluation_Value", type=Evaluation_specification_Evaluation_Value, multiplicity=Multiplicity(0, 9999))
    }
)
evaluation_locus_Evaluation_Values65: BinaryAssociation = BinaryAssociation(
    name="evaluation_locus_Evaluation_Values65",
    ends={
        Property(name="Values66", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Evaluation_locus_Evaluation_Value", type=Evaluation_locus_Evaluation_Value, multiplicity=Multiplicity(0, 9999))
    }
)
booleanValue_value_BooleanValue_Values67: BinaryAssociation = BinaryAssociation(
    name="booleanValue_value_BooleanValue_Values67",
    ends={
        Property(name="Values68", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="BooleanValue_value_BooleanValue_Value", type=BooleanValue_value_BooleanValue_Value, multiplicity=Multiplicity(0, 9999))
    }
)
parameterValue_parameter_ParameterValue_Values41: BinaryAssociation = BinaryAssociation(
    name="parameterValue_parameter_ParameterValue_Values41",
    ends={
        Property(name="Values42", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ParameterValue_parameter_ParameterValue_Value", type=ParameterValue_parameter_ParameterValue_Value, multiplicity=Multiplicity(0, 9999))
    }
)
actionActivation_pinActivations_Values43: BinaryAssociation = BinaryAssociation(
    name="actionActivation_pinActivations_Values43",
    ends={
        Property(name="Values44", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionActivation_pinActivations_Value", type=ActionActivation_pinActivations_Value, multiplicity=Multiplicity(0, 9999))
    }
)
token_holder_Values75: BinaryAssociation = BinaryAssociation(
    name="token_holder_Values75",
    ends={
        Property(name="Values76", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Token_holder_Value", type=Token_holder_Value, multiplicity=Multiplicity(0, 9999))
    }
)
offer_offeredTokens_Values77: BinaryAssociation = BinaryAssociation(
    name="offer_offeredTokens_Values77",
    ends={
        Property(name="Values78", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Offer_offeredTokens_Value", type=Offer_offeredTokens_Value, multiplicity=Multiplicity(0, 9999))
    }
)
featureValue_values_FeatureValue_Values79: BinaryAssociation = BinaryAssociation(
    name="featureValue_values_FeatureValue_Values79",
    ends={
        Property(name="Values80", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureValue_values_FeatureValue_Value", type=FeatureValue_values_FeatureValue_Value, multiplicity=Multiplicity(0, 9999))
    }
)
featureValue_feature_Values81: BinaryAssociation = BinaryAssociation(
    name="featureValue_feature_Values81",
    ends={
        Property(name="Values82", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureValue_feature_Value", type=FeatureValue_feature_Value, multiplicity=Multiplicity(0, 9999))
    }
)
featureValue_position_Values83: BinaryAssociation = BinaryAssociation(
    name="featureValue_position_Values83",
    ends={
        Property(name="Values84", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureValue_position_Value", type=FeatureValue_position_Value, multiplicity=Multiplicity(0, 9999))
    }
)
pinActivation_actionActivation_Values85: BinaryAssociation = BinaryAssociation(
    name="pinActivation_actionActivation_Values85",
    ends={
        Property(name="Values86", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="PinActivation_actionActivation_Value", type=PinActivation_actionActivation_Value, multiplicity=Multiplicity(0, 9999))
    }
)
pinActivation_count_temp_Values87: BinaryAssociation = BinaryAssociation(
    name="pinActivation_count_temp_Values87",
    ends={
        Property(name="Values88", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="PinActivation_count_temp_Value", type=PinActivation_count_temp_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityEdgeInstance_group_ActivityEdgeInstance_Values89: BinaryAssociation = BinaryAssociation(
    name="activityEdgeInstance_group_ActivityEdgeInstance_Values89",
    ends={
        Property(name="Values90", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdgeInstance_group_ActivityEdgeInstance_Value", type=ActivityEdgeInstance_group_ActivityEdgeInstance_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityEdgeInstance_offers_Values91: BinaryAssociation = BinaryAssociation(
    name="activityEdgeInstance_offers_Values91",
    ends={
        Property(name="Values92", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdgeInstance_offers_Value", type=ActivityEdgeInstance_offers_Value, multiplicity=Multiplicity(0, 9999))
    }
)
objectToken_value_Values69: BinaryAssociation = BinaryAssociation(
    name="objectToken_value_Values69",
    ends={
        Property(name="Values70", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjectToken_value_Value", type=ObjectToken_value_Value, multiplicity=Multiplicity(0, 9999))
    }
)
callActionActivation_callExecutions_Values71: BinaryAssociation = BinaryAssociation(
    name="callActionActivation_callExecutions_Values71",
    ends={
        Property(name="Values72", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CallActionActivation_callExecutions_Value", type=CallActionActivation_callExecutions_Value, multiplicity=Multiplicity(0, 9999))
    }
)
compoundValue_featureValues_Values73: BinaryAssociation = BinaryAssociation(
    name="compoundValue_featureValues_Values73",
    ends={
        Property(name="Values74", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompoundValue_featureValues_Value", type=CompoundValue_featureValues_Value, multiplicity=Multiplicity(0, 9999))
    }
)
inputParameterValues_name_Values99: BinaryAssociation = BinaryAssociation(
    name="inputParameterValues_name_Values99",
    ends={
        Property(name="Values100", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="InputParameterValues_name_Value", type=InputParameterValues_name_Value, multiplicity=Multiplicity(0, 9999))
    }
)
inputParameterValues_parameterValues_Values101: BinaryAssociation = BinaryAssociation(
    name="inputParameterValues_parameterValues_Values101",
    ends={
        Property(name="Values102", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="InputParameterValues_parameterValues_Value", type=InputParameterValues_parameterValues_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_heldTokens_Values103: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_heldTokens_Values103",
    ends={
        Property(name="Values104", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_heldTokens_Value", type=ActivityNodeActivation_heldTokens_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_node_ActivityNodeActivation_Values105: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_node_ActivityNodeActivation_Values105",
    ends={
        Property(name="Values106", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_node_ActivityNodeActivation_Value", type=ActivityNodeActivation_node_ActivityNodeActivation_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_running_Values107: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_running_Values107",
    ends={
        Property(name="Values108", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_running_Value", type=ActivityNodeActivation_running_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_isRunning_Values109: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_isRunning_Values109",
    ends={
        Property(name="Values110", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_isRunning_Value", type=ActivityNodeActivation_isRunning_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_outgoingEdges_Values111: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_outgoingEdges_Values111",
    ends={
        Property(name="Values112", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_outgoingEdges_Value", type=ActivityNodeActivation_outgoingEdges_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_incomingEdges_Values113: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_incomingEdges_Values113",
    ends={
        Property(name="Values114", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_incomingEdges_Value", type=ActivityNodeActivation_incomingEdges_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityNodeActivation_group_ActivityNodeActivation_Values115: BinaryAssociation = BinaryAssociation(
    name="activityNodeActivation_group_ActivityNodeActivation_Values115",
    ends={
        Property(name="Values116", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_group_ActivityNodeActivation_Value", type=ActivityNodeActivation_group_ActivityNodeActivation_Value, multiplicity=Multiplicity(0, 9999))
    }
)
extensionalValue_locus_ExtensionalValue_Values117: BinaryAssociation = BinaryAssociation(
    name="extensionalValue_locus_ExtensionalValue_Values117",
    ends={
        Property(name="Values118", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ExtensionalValue_locus_ExtensionalValue_Value", type=ExtensionalValue_locus_ExtensionalValue_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityEdgeInstance_target_Values93: BinaryAssociation = BinaryAssociation(
    name="activityEdgeInstance_target_Values93",
    ends={
        Property(name="Values94", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdgeInstance_target_Value", type=ActivityEdgeInstance_target_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityEdgeInstance_edge_ActivityEdgeInstance_Values95: BinaryAssociation = BinaryAssociation(
    name="activityEdgeInstance_edge_ActivityEdgeInstance_Values95",
    ends={
        Property(name="Values96", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdgeInstance_edge_ActivityEdgeInstance_Value", type=ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityEdgeInstance_source_Values97: BinaryAssociation = BinaryAssociation(
    name="activityEdgeInstance_source_Values97",
    ends={
        Property(name="Values98", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdgeInstance_source_Value", type=ActivityEdgeInstance_source_Value, multiplicity=Multiplicity(0, 9999))
    }
)
activityExecution_activationGroup_Values119: BinaryAssociation = BinaryAssociation(
    name="activityExecution_activationGroup_Values119",
    ends={
        Property(name="Values120", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityExecution_activationGroup_Value", type=ActivityExecution_activationGroup_Value, multiplicity=Multiplicity(0, 9999))
    }
)
executionEnvironment_locus_ExecutionEnvironment_Values121: BinaryAssociation = BinaryAssociation(
    name="executionEnvironment_locus_ExecutionEnvironment_Values121",
    ends={
        Property(name="Values122", type=umlTrace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ExecutionEnvironment_locus_ExecutionEnvironment_Value", type=ExecutionEnvironment_locus_ExecutionEnvironment_Value, multiplicity=Multiplicity(0, 9999))
    }
)
precedingState123: BinaryAssociation = BinaryAssociation(
    name="precedingState123",
    ends={
        Property(name="State", type=umlTrace_Steps_SmallStep, multiplicity=Multiplicity(1, 1)),
        Property(name="followingStep", type=Steps_umlTrace_State, multiplicity=Multiplicity(1, 1))
    }
)
startingState124: BinaryAssociation = BinaryAssociation(
    name="startingState124",
    ends={
        Property(name="State125", type=umlTrace_Steps_BigStep, multiplicity=Multiplicity(1, 1)),
        Property(name="startedBigSteps", type=Steps_umlTrace_State, multiplicity=Multiplicity(1, 1))
    }
)
endingState126: BinaryAssociation = BinaryAssociation(
    name="endingState126",
    ends={
        Property(name="State127", type=umlTrace_Steps_BigStep, multiplicity=Multiplicity(1, 1)),
        Property(name="endedBigSteps", type=Steps_umlTrace_State, multiplicity=Multiplicity(0, 1))
    }
)
types128: BinaryAssociation = BinaryAssociation(
    name="types128",
    ends={
        Property(name="uml_TracedClass", type=umlTrace_Values_Object_types_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Object_types_Value", type=uml_TracedClass, multiplicity=Multiplicity(0, 9999))
    }
)
parent129: BinaryAssociation = BinaryAssociation(
    name="parent129",
    ends={
        Property(name="Traced", type=umlTrace_Values_Object_types_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration", type=Kernel_TracedObject, multiplicity=Multiplicity(1, 1))
    }
)
states130: BinaryAssociation = BinaryAssociation(
    name="states130",
    ends={
        Property(name="State131", type=umlTrace_Values_Object_types_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="object_types_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent138: BinaryAssociation = BinaryAssociation(
    name="parent138",
    ends={
        Property(name="Traced140", type=umlTrace_Values_IntegerValue_value_IntegerValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration139", type=Kernel_TracedIntegerValue, multiplicity=Multiplicity(1, 1))
    }
)
states141: BinaryAssociation = BinaryAssociation(
    name="states141",
    ends={
        Property(name="State142", type=umlTrace_Values_IntegerValue_value_IntegerValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="integerValue_value_IntegerValue_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent143: BinaryAssociation = BinaryAssociation(
    name="parent143",
    ends={
        Property(name="Traced145", type=umlTrace_Values_ForkedToken_remainingOffersCount_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration144", type=IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(1, 1))
    }
)
states146: BinaryAssociation = BinaryAssociation(
    name="states146",
    ends={
        Property(name="State147", type=umlTrace_Values_ForkedToken_remainingOffersCount_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="forkedToken_remainingOffersCount_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
baseToken148: BinaryAssociation = BinaryAssociation(
    name="baseToken148",
    ends={
        Property(name="IntermediateActivities_TracedToken", type=umlTrace_Values_ForkedToken_baseToken_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ForkedToken_baseToken_Value", type=IntermediateActivities_TracedToken, multiplicity=Multiplicity(1, 1))
    }
)
parent149: BinaryAssociation = BinaryAssociation(
    name="parent149",
    ends={
        Property(name="Traced151", type=umlTrace_Values_ForkedToken_baseToken_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration150", type=IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(1, 1))
    }
)
states152: BinaryAssociation = BinaryAssociation(
    name="states152",
    ends={
        Property(name="State153", type=umlTrace_Values_ForkedToken_baseToken_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="forkedToken_baseToken_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
referent132: BinaryAssociation = BinaryAssociation(
    name="referent132",
    ends={
        Property(name="Kernel_TracedObject", type=umlTrace_Values_Reference_referent_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Reference_referent_Value", type=Kernel_TracedObject, multiplicity=Multiplicity(1, 1))
    }
)
parent133: BinaryAssociation = BinaryAssociation(
    name="parent133",
    ends={
        Property(name="Traced135", type=umlTrace_Values_Reference_referent_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration134", type=Kernel_TracedReference, multiplicity=Multiplicity(1, 1))
    }
)
states136: BinaryAssociation = BinaryAssociation(
    name="states136",
    ends={
        Property(name="State137", type=umlTrace_Values_Reference_referent_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="reference_referent_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
states157: BinaryAssociation = BinaryAssociation(
    name="states157",
    ends={
        Property(name="forkedToken_baseTokenIsWithdrawn_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999)),
        Property(name="State158", type=umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value, multiplicity=Multiplicity(1, 1))
    }
)
builtInTypes159: BinaryAssociation = BinaryAssociation(
    name="builtInTypes159",
    ends={
        Property(name="uml_TracedPrimitiveType", type=umlTrace_Values_ExecutionFactory_builtInTypes_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ExecutionFactory_builtInTypes_Value", type=uml_TracedPrimitiveType, multiplicity=Multiplicity(0, 9999))
    }
)
parent160: BinaryAssociation = BinaryAssociation(
    name="parent160",
    ends={
        Property(name="Traced162", type=umlTrace_Values_ExecutionFactory_builtInTypes_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration161", type=Loci_TracedExecutionFactory, multiplicity=Multiplicity(1, 1))
    }
)
states163: BinaryAssociation = BinaryAssociation(
    name="states163",
    ends={
        Property(name="State164", type=umlTrace_Values_ExecutionFactory_builtInTypes_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="executionFactory_builtInTypes_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
primitiveBehaviorPrototypes165: BinaryAssociation = BinaryAssociation(
    name="primitiveBehaviorPrototypes165",
    ends={
        Property(name="BasicBehaviors_TracedOpaqueBehaviorExecution", type=umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value", type=BasicBehaviors_TracedOpaqueBehaviorExecution, multiplicity=Multiplicity(0, 9999))
    }
)
parent166: BinaryAssociation = BinaryAssociation(
    name="parent166",
    ends={
        Property(name="Traced168", type=umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration167", type=Loci_TracedExecutionFactory, multiplicity=Multiplicity(1, 1))
    }
)
states169: BinaryAssociation = BinaryAssociation(
    name="states169",
    ends={
        Property(name="State170", type=umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="executionFactory_primitiveBehaviorPrototypes_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
locus_ExecutionFactory171: BinaryAssociation = BinaryAssociation(
    name="locus_ExecutionFactory171",
    ends={
        Property(name="Loci_TracedLocus", type=umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value", type=Loci_TracedLocus, multiplicity=Multiplicity(0, 1))
    }
)
parent172: BinaryAssociation = BinaryAssociation(
    name="parent172",
    ends={
        Property(name="Traced174", type=umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration173", type=Loci_TracedExecutionFactory, multiplicity=Multiplicity(1, 1))
    }
)
states175: BinaryAssociation = BinaryAssociation(
    name="states175",
    ends={
        Property(name="State176", type=umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="executionFactory_locus_ExecutionFactory_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent154: BinaryAssociation = BinaryAssociation(
    name="parent154",
    ends={
        Property(name="Traced156", type=umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration155", type=IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(1, 1))
    }
)
extensionalValues183: BinaryAssociation = BinaryAssociation(
    name="extensionalValues183",
    ends={
        Property(name="Kernel_TracedExtensionalValue", type=umlTrace_Values_Locus_extensionalValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Locus_extensionalValues_Value", type=Kernel_TracedExtensionalValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent184: BinaryAssociation = BinaryAssociation(
    name="parent184",
    ends={
        Property(name="Traced186", type=umlTrace_Values_Locus_extensionalValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration185", type=Loci_TracedLocus, multiplicity=Multiplicity(1, 1))
    }
)
states187: BinaryAssociation = BinaryAssociation(
    name="states187",
    ends={
        Property(name="State188", type=umlTrace_Values_Locus_extensionalValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="locus_extensionalValues_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
executor189: BinaryAssociation = BinaryAssociation(
    name="executor189",
    ends={
        Property(name="Loci_TracedExecutor", type=umlTrace_Values_Locus_executor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Locus_executor_Value", type=Loci_TracedExecutor, multiplicity=Multiplicity(0, 1))
    }
)
parent190: BinaryAssociation = BinaryAssociation(
    name="parent190",
    ends={
        Property(name="Traced192", type=umlTrace_Values_Locus_executor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration191", type=Loci_TracedLocus, multiplicity=Multiplicity(1, 1))
    }
)
states193: BinaryAssociation = BinaryAssociation(
    name="states193",
    ends={
        Property(name="State194", type=umlTrace_Values_Locus_executor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="locus_executor_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent195: BinaryAssociation = BinaryAssociation(
    name="parent195",
    ends={
        Property(name="Traced197", type=umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration196", type=IntermediateActivities_TracedObjectNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states198: BinaryAssociation = BinaryAssociation(
    name="states198",
    ends={
        Property(name="State199", type=umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="objectNodeActivation_offeredTokenCount_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
factory177: BinaryAssociation = BinaryAssociation(
    name="factory177",
    ends={
        Property(name="Loci_TracedExecutionFactory", type=umlTrace_Values_Locus_factory_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Locus_factory_Value", type=Loci_TracedExecutionFactory, multiplicity=Multiplicity(0, 1))
    }
)
parent178: BinaryAssociation = BinaryAssociation(
    name="parent178",
    ends={
        Property(name="Traced180", type=umlTrace_Values_Locus_factory_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration179", type=Loci_TracedLocus, multiplicity=Multiplicity(1, 1))
    }
)
states181: BinaryAssociation = BinaryAssociation(
    name="states181",
    ends={
        Property(name="State182", type=umlTrace_Values_Locus_factory_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="locus_factory_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
values_ParameterValue206: BinaryAssociation = BinaryAssociation(
    name="values_ParameterValue206",
    ends={
        Property(name="Kernel_TracedValue", type=umlTrace_Values_ParameterValue_values_ParameterValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ParameterValue_values_ParameterValue_Value", type=Kernel_TracedValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent207: BinaryAssociation = BinaryAssociation(
    name="parent207",
    ends={
        Property(name="Traced209", type=umlTrace_Values_ParameterValue_values_ParameterValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration208", type=BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(1, 1))
    }
)
states210: BinaryAssociation = BinaryAssociation(
    name="states210",
    ends={
        Property(name="State211", type=umlTrace_Values_ParameterValue_values_ParameterValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterValue_values_ParameterValue_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parameter_ParameterValue212: BinaryAssociation = BinaryAssociation(
    name="parameter_ParameterValue212",
    ends={
        Property(name="uml_TracedParameter", type=umlTrace_Values_ParameterValue_parameter_ParameterValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ParameterValue_parameter_ParameterValue_Value", type=uml_TracedParameter, multiplicity=Multiplicity(1, 1))
    }
)
parent213: BinaryAssociation = BinaryAssociation(
    name="parent213",
    ends={
        Property(name="Traced215", type=umlTrace_Values_ParameterValue_parameter_ParameterValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration214", type=BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(1, 1))
    }
)
states216: BinaryAssociation = BinaryAssociation(
    name="states216",
    ends={
        Property(name="State217", type=umlTrace_Values_ParameterValue_parameter_ParameterValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterValue_parameter_ParameterValue_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
pinActivations218: BinaryAssociation = BinaryAssociation(
    name="pinActivations218",
    ends={
        Property(name="BasicActions_TracedPinActivation", type=umlTrace_Values_ActionActivation_pinActivations_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActionActivation_pinActivations_Value", type=BasicActions_TracedPinActivation, multiplicity=Multiplicity(0, 9999))
    }
)
parent219: BinaryAssociation = BinaryAssociation(
    name="parent219",
    ends={
        Property(name="Traced221", type=umlTrace_Values_ActionActivation_pinActivations_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration220", type=BasicActions_TracedActionActivation, multiplicity=Multiplicity(1, 1))
    }
)
states222: BinaryAssociation = BinaryAssociation(
    name="states222",
    ends={
        Property(name="State223", type=umlTrace_Values_ActionActivation_pinActivations_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="actionActivation_pinActivations_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
runtimeModelElement200: BinaryAssociation = BinaryAssociation(
    name="runtimeModelElement200",
    ends={
        Property(name="uml_TracedElement", type=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_SemanticVisitor_runtimeModelElement_Value", type=uml_TracedElement, multiplicity=Multiplicity(0, 1))
    }
)
parent201: BinaryAssociation = BinaryAssociation(
    name="parent201",
    ends={
        Property(name="Traced203", type=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration202", type=Loci_TracedSemanticVisitor, multiplicity=Multiplicity(1, 1))
    }
)
states204: BinaryAssociation = BinaryAssociation(
    name="states204",
    ends={
        Property(name="State205", type=umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="semanticVisitor_runtimeModelElement_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent224: BinaryAssociation = BinaryAssociation(
    name="parent224",
    ends={
        Property(name="Traced226", type=umlTrace_Values_ActionActivation_firing_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration225", type=BasicActions_TracedActionActivation, multiplicity=Multiplicity(1, 1))
    }
)
states227: BinaryAssociation = BinaryAssociation(
    name="states227",
    ends={
        Property(name="State228", type=umlTrace_Values_ActionActivation_firing_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="actionActivation_firing_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parameterValues229: BinaryAssociation = BinaryAssociation(
    name="parameterValues229",
    ends={
        Property(name="BasicBehaviors_TracedParameterValue", type=umlTrace_Values_Execution_parameterValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Execution_parameterValues_Value", type=BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent230: BinaryAssociation = BinaryAssociation(
    name="parent230",
    ends={
        Property(name="Traced232", type=umlTrace_Values_Execution_parameterValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration231", type=BasicBehaviors_TracedExecution, multiplicity=Multiplicity(1, 1))
    }
)
states233: BinaryAssociation = BinaryAssociation(
    name="states233",
    ends={
        Property(name="State234", type=umlTrace_Values_Execution_parameterValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="execution_parameterValues_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
context235: BinaryAssociation = BinaryAssociation(
    name="context235",
    ends={
        Property(name="Kernel_TracedObject236", type=umlTrace_Values_Execution_context_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Execution_context_Value", type=Kernel_TracedObject, multiplicity=Multiplicity(1, 1))
    }
)
parent237: BinaryAssociation = BinaryAssociation(
    name="parent237",
    ends={
        Property(name="Traced239", type=umlTrace_Values_Execution_context_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration238", type=BasicBehaviors_TracedExecution, multiplicity=Multiplicity(1, 1))
    }
)
states240: BinaryAssociation = BinaryAssociation(
    name="states240",
    ends={
        Property(name="State241", type=umlTrace_Values_Execution_context_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="execution_context_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
semanticVisitor242: BinaryAssociation = BinaryAssociation(
    name="semanticVisitor242",
    ends={
        Property(name="Loci_TracedSemanticVisitor", type=umlTrace_Values_Element_semanticVisitor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Element_semanticVisitor_Value", type=Loci_TracedSemanticVisitor, multiplicity=Multiplicity(0, 9999))
    }
)
parent248: BinaryAssociation = BinaryAssociation(
    name="parent248",
    ends={
        Property(name="Traced250", type=umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration249", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1))
    }
)
states251: BinaryAssociation = BinaryAssociation(
    name="states251",
    ends={
        Property(name="State252", type=umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivationGroup_nodeActivations_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
activityExecution253: BinaryAssociation = BinaryAssociation(
    name="activityExecution253",
    ends={
        Property(name="IntermediateActivities_TracedActivityExecution", type=umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value", type=IntermediateActivities_TracedActivityExecution, multiplicity=Multiplicity(0, 1))
    }
)
parent254: BinaryAssociation = BinaryAssociation(
    name="parent254",
    ends={
        Property(name="Traced256", type=umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration255", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1))
    }
)
states257: BinaryAssociation = BinaryAssociation(
    name="states257",
    ends={
        Property(name="State258", type=umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivationGroup_activityExecution_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
edgeInstances259: BinaryAssociation = BinaryAssociation(
    name="edgeInstances259",
    ends={
        Property(name="IntermediateActivities_TracedActivityEdgeInstance", type=umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(0, 9999))
    }
)
parent260: BinaryAssociation = BinaryAssociation(
    name="parent260",
    ends={
        Property(name="Traced262", type=umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration261", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1))
    }
)
states263: BinaryAssociation = BinaryAssociation(
    name="states263",
    ends={
        Property(name="State264", type=umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivationGroup_edgeInstances_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
locus_Executor265: BinaryAssociation = BinaryAssociation(
    name="locus_Executor265",
    ends={
        Property(name="Loci_TracedLocus266", type=umlTrace_Values_Executor_locus_Executor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Executor_locus_Executor_Value", type=Loci_TracedLocus, multiplicity=Multiplicity(0, 1))
    }
)
parent243: BinaryAssociation = BinaryAssociation(
    name="parent243",
    ends={
        Property(name="Traced244", type=umlTrace_Values_Element_semanticVisitor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="uml", type=uml_TracedElement, multiplicity=Multiplicity(1, 1))
    }
)
parent267: BinaryAssociation = BinaryAssociation(
    name="parent267",
    ends={
        Property(name="Traced269", type=umlTrace_Values_Executor_locus_Executor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration268", type=Loci_TracedExecutor, multiplicity=Multiplicity(1, 1))
    }
)
states245: BinaryAssociation = BinaryAssociation(
    name="states245",
    ends={
        Property(name="State246", type=umlTrace_Values_Element_semanticVisitor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="element_semanticVisitor_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
nodeActivations247: BinaryAssociation = BinaryAssociation(
    name="nodeActivations247",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivation", type=umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(0, 9999))
    }
)
type272: BinaryAssociation = BinaryAssociation(
    name="type272",
    ends={
        Property(name="umlTrace_Values_PrimitiveValue_type_Value", type=uml_TracedPrimitiveType, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TracedPrimitiveType273", type=umlTrace_Values_PrimitiveValue_type_Value, multiplicity=Multiplicity(1, 1))
    }
)
parent274: BinaryAssociation = BinaryAssociation(
    name="parent274",
    ends={
        Property(name="Traced276", type=umlTrace_Values_PrimitiveValue_type_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration275", type=Kernel_TracedPrimitiveValue, multiplicity=Multiplicity(1, 1))
    }
)
states277: BinaryAssociation = BinaryAssociation(
    name="states277",
    ends={
        Property(name="State278", type=umlTrace_Values_PrimitiveValue_type_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="primitiveValue_type_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
specification_Evaluation279: BinaryAssociation = BinaryAssociation(
    name="specification_Evaluation279",
    ends={
        Property(name="uml_TracedValueSpecification", type=umlTrace_Values_Evaluation_specification_Evaluation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Evaluation_specification_Evaluation_Value", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
parent280: BinaryAssociation = BinaryAssociation(
    name="parent280",
    ends={
        Property(name="Traced282", type=umlTrace_Values_Evaluation_specification_Evaluation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration281", type=Kernel_TracedEvaluation, multiplicity=Multiplicity(1, 1))
    }
)
states283: BinaryAssociation = BinaryAssociation(
    name="states283",
    ends={
        Property(name="State284", type=umlTrace_Values_Evaluation_specification_Evaluation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluation_specification_Evaluation_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
locus_Evaluation285: BinaryAssociation = BinaryAssociation(
    name="locus_Evaluation285",
    ends={
        Property(name="Loci_TracedLocus286", type=umlTrace_Values_Evaluation_locus_Evaluation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Evaluation_locus_Evaluation_Value", type=Loci_TracedLocus, multiplicity=Multiplicity(1, 1))
    }
)
parent287: BinaryAssociation = BinaryAssociation(
    name="parent287",
    ends={
        Property(name="Traced289", type=umlTrace_Values_Evaluation_locus_Evaluation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration288", type=Kernel_TracedEvaluation, multiplicity=Multiplicity(1, 1))
    }
)
states290: BinaryAssociation = BinaryAssociation(
    name="states290",
    ends={
        Property(name="State291", type=umlTrace_Values_Evaluation_locus_Evaluation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluation_locus_Evaluation_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent292: BinaryAssociation = BinaryAssociation(
    name="parent292",
    ends={
        Property(name="Traced294", type=umlTrace_Values_BooleanValue_value_BooleanValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration293", type=Kernel_TracedBooleanValue, multiplicity=Multiplicity(1, 1))
    }
)
states270: BinaryAssociation = BinaryAssociation(
    name="states270",
    ends={
        Property(name="State271", type=umlTrace_Values_Executor_locus_Executor_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="executor_locus_Executor_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent299: BinaryAssociation = BinaryAssociation(
    name="parent299",
    ends={
        Property(name="Traced301", type=umlTrace_Values_ObjectToken_value_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration300", type=IntermediateActivities_TracedObjectToken, multiplicity=Multiplicity(1, 1))
    }
)
states302: BinaryAssociation = BinaryAssociation(
    name="states302",
    ends={
        Property(name="State303", type=umlTrace_Values_ObjectToken_value_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="objectToken_value_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
callExecutions304: BinaryAssociation = BinaryAssociation(
    name="callExecutions304",
    ends={
        Property(name="BasicBehaviors_TracedExecution", type=umlTrace_Values_CallActionActivation_callExecutions_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_CallActionActivation_callExecutions_Value", type=BasicBehaviors_TracedExecution, multiplicity=Multiplicity(0, 9999))
    }
)
parent305: BinaryAssociation = BinaryAssociation(
    name="parent305",
    ends={
        Property(name="Traced307", type=umlTrace_Values_CallActionActivation_callExecutions_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration306", type=BasicActions_TracedCallActionActivation, multiplicity=Multiplicity(1, 1))
    }
)
states308: BinaryAssociation = BinaryAssociation(
    name="states308",
    ends={
        Property(name="State309", type=umlTrace_Values_CallActionActivation_callExecutions_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="callActionActivation_callExecutions_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
featureValues310: BinaryAssociation = BinaryAssociation(
    name="featureValues310",
    ends={
        Property(name="Kernel_TracedFeatureValue", type=umlTrace_Values_CompoundValue_featureValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_CompoundValue_featureValues_Value", type=Kernel_TracedFeatureValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent311: BinaryAssociation = BinaryAssociation(
    name="parent311",
    ends={
        Property(name="Traced313", type=umlTrace_Values_CompoundValue_featureValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration312", type=Kernel_TracedCompoundValue, multiplicity=Multiplicity(1, 1))
    }
)
states314: BinaryAssociation = BinaryAssociation(
    name="states314",
    ends={
        Property(name="State315", type=umlTrace_Values_CompoundValue_featureValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="compoundValue_featureValues_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
holder316: BinaryAssociation = BinaryAssociation(
    name="holder316",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivation317", type=umlTrace_Values_Token_holder_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Token_holder_Value", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(0, 1))
    }
)
parent318: BinaryAssociation = BinaryAssociation(
    name="parent318",
    ends={
        Property(name="Traced320", type=umlTrace_Values_Token_holder_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration319", type=IntermediateActivities_TracedToken, multiplicity=Multiplicity(1, 1))
    }
)
states295: BinaryAssociation = BinaryAssociation(
    name="states295",
    ends={
        Property(name="State296", type=umlTrace_Values_BooleanValue_value_BooleanValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="booleanValue_value_BooleanValue_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
value297: BinaryAssociation = BinaryAssociation(
    name="value297",
    ends={
        Property(name="Kernel_TracedValue298", type=umlTrace_Values_ObjectToken_value_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ObjectToken_value_Value", type=Kernel_TracedValue, multiplicity=Multiplicity(0, 1))
    }
)
offeredTokens323: BinaryAssociation = BinaryAssociation(
    name="offeredTokens323",
    ends={
        Property(name="IntermediateActivities_TracedToken324", type=umlTrace_Values_Offer_offeredTokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_Offer_offeredTokens_Value", type=IntermediateActivities_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
parent325: BinaryAssociation = BinaryAssociation(
    name="parent325",
    ends={
        Property(name="Traced327", type=umlTrace_Values_Offer_offeredTokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration326", type=IntermediateActivities_TracedOffer, multiplicity=Multiplicity(1, 1))
    }
)
states328: BinaryAssociation = BinaryAssociation(
    name="states328",
    ends={
        Property(name="State329", type=umlTrace_Values_Offer_offeredTokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="offer_offeredTokens_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
values_FeatureValue330: BinaryAssociation = BinaryAssociation(
    name="values_FeatureValue330",
    ends={
        Property(name="Kernel_TracedValue331", type=umlTrace_Values_FeatureValue_values_FeatureValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_FeatureValue_values_FeatureValue_Value", type=Kernel_TracedValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent332: BinaryAssociation = BinaryAssociation(
    name="parent332",
    ends={
        Property(name="Traced334", type=umlTrace_Values_FeatureValue_values_FeatureValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration333", type=Kernel_TracedFeatureValue, multiplicity=Multiplicity(1, 1))
    }
)
states335: BinaryAssociation = BinaryAssociation(
    name="states335",
    ends={
        Property(name="State336", type=umlTrace_Values_FeatureValue_values_FeatureValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="featureValue_values_FeatureValue_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
feature337: BinaryAssociation = BinaryAssociation(
    name="feature337",
    ends={
        Property(name="uml_TracedStructuralFeature", type=umlTrace_Values_FeatureValue_feature_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_FeatureValue_feature_Value", type=uml_TracedStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
parent338: BinaryAssociation = BinaryAssociation(
    name="parent338",
    ends={
        Property(name="Traced340", type=umlTrace_Values_FeatureValue_feature_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration339", type=Kernel_TracedFeatureValue, multiplicity=Multiplicity(1, 1))
    }
)
states341: BinaryAssociation = BinaryAssociation(
    name="states341",
    ends={
        Property(name="State342", type=umlTrace_Values_FeatureValue_feature_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="featureValue_feature_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
states321: BinaryAssociation = BinaryAssociation(
    name="states321",
    ends={
        Property(name="State322", type=umlTrace_Values_Token_holder_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="token_holder_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
actionActivation348: BinaryAssociation = BinaryAssociation(
    name="actionActivation348",
    ends={
        Property(name="BasicActions_TracedActionActivation", type=umlTrace_Values_PinActivation_actionActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_PinActivation_actionActivation_Value", type=BasicActions_TracedActionActivation, multiplicity=Multiplicity(0, 1))
    }
)
parent349: BinaryAssociation = BinaryAssociation(
    name="parent349",
    ends={
        Property(name="Traced351", type=umlTrace_Values_PinActivation_actionActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration350", type=BasicActions_TracedPinActivation, multiplicity=Multiplicity(1, 1))
    }
)
states352: BinaryAssociation = BinaryAssociation(
    name="states352",
    ends={
        Property(name="State353", type=umlTrace_Values_PinActivation_actionActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="pinActivation_actionActivation_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent354: BinaryAssociation = BinaryAssociation(
    name="parent354",
    ends={
        Property(name="Traced356", type=umlTrace_Values_PinActivation_count_temp_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration355", type=BasicActions_TracedPinActivation, multiplicity=Multiplicity(1, 1))
    }
)
states357: BinaryAssociation = BinaryAssociation(
    name="states357",
    ends={
        Property(name="State358", type=umlTrace_Values_PinActivation_count_temp_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="pinActivation_count_temp_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
group_ActivityEdgeInstance359: BinaryAssociation = BinaryAssociation(
    name="group_ActivityEdgeInstance359",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivationGroup", type=umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1))
    }
)
parent360: BinaryAssociation = BinaryAssociation(
    name="parent360",
    ends={
        Property(name="Traced362", type=umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration361", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1))
    }
)
states363: BinaryAssociation = BinaryAssociation(
    name="states363",
    ends={
        Property(name="State364", type=umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityEdgeInstance_group_ActivityEdgeInstance_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent343: BinaryAssociation = BinaryAssociation(
    name="parent343",
    ends={
        Property(name="Traced345", type=umlTrace_Values_FeatureValue_position_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration344", type=Kernel_TracedFeatureValue, multiplicity=Multiplicity(1, 1))
    }
)
states346: BinaryAssociation = BinaryAssociation(
    name="states346",
    ends={
        Property(name="State347", type=umlTrace_Values_FeatureValue_position_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="featureValue_position_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
target371: BinaryAssociation = BinaryAssociation(
    name="target371",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivation372", type=umlTrace_Values_ActivityEdgeInstance_target_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityEdgeInstance_target_Value", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
parent373: BinaryAssociation = BinaryAssociation(
    name="parent373",
    ends={
        Property(name="Traced375", type=umlTrace_Values_ActivityEdgeInstance_target_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration374", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1))
    }
)
states376: BinaryAssociation = BinaryAssociation(
    name="states376",
    ends={
        Property(name="State377", type=umlTrace_Values_ActivityEdgeInstance_target_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityEdgeInstance_target_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
edge_ActivityEdgeInstance378: BinaryAssociation = BinaryAssociation(
    name="edge_ActivityEdgeInstance378",
    ends={
        Property(name="uml_TracedActivityEdge", type=umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 1))
    }
)
parent379: BinaryAssociation = BinaryAssociation(
    name="parent379",
    ends={
        Property(name="Traced381", type=umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration380", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1))
    }
)
states382: BinaryAssociation = BinaryAssociation(
    name="states382",
    ends={
        Property(name="State383", type=umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityEdgeInstance_edge_ActivityEdgeInstance_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
source384: BinaryAssociation = BinaryAssociation(
    name="source384",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivation385", type=umlTrace_Values_ActivityEdgeInstance_source_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityEdgeInstance_source_Value", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
parent386: BinaryAssociation = BinaryAssociation(
    name="parent386",
    ends={
        Property(name="Traced388", type=umlTrace_Values_ActivityEdgeInstance_source_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration387", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1))
    }
)
offers365: BinaryAssociation = BinaryAssociation(
    name="offers365",
    ends={
        Property(name="IntermediateActivities_TracedOffer", type=umlTrace_Values_ActivityEdgeInstance_offers_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityEdgeInstance_offers_Value", type=IntermediateActivities_TracedOffer, multiplicity=Multiplicity(0, 9999))
    }
)
states389: BinaryAssociation = BinaryAssociation(
    name="states389",
    ends={
        Property(name="State390", type=umlTrace_Values_ActivityEdgeInstance_source_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityEdgeInstance_source_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent366: BinaryAssociation = BinaryAssociation(
    name="parent366",
    ends={
        Property(name="Traced368", type=umlTrace_Values_ActivityEdgeInstance_offers_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration367", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1))
    }
)
states369: BinaryAssociation = BinaryAssociation(
    name="states369",
    ends={
        Property(name="State370", type=umlTrace_Values_ActivityEdgeInstance_offers_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityEdgeInstance_offers_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent391: BinaryAssociation = BinaryAssociation(
    name="parent391",
    ends={
        Property(name="Traced393", type=umlTrace_Values_InputParameterValues_name_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration392", type=Input_TracedInputParameterValues, multiplicity=Multiplicity(1, 1))
    }
)
states394: BinaryAssociation = BinaryAssociation(
    name="states394",
    ends={
        Property(name="State395", type=umlTrace_Values_InputParameterValues_name_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="inputParameterValues_name_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parameterValues396: BinaryAssociation = BinaryAssociation(
    name="parameterValues396",
    ends={
        Property(name="BasicBehaviors_TracedParameterValue397", type=umlTrace_Values_InputParameterValues_parameterValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_InputParameterValues_parameterValues_Value", type=BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent398: BinaryAssociation = BinaryAssociation(
    name="parent398",
    ends={
        Property(name="Traced400", type=umlTrace_Values_InputParameterValues_parameterValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration399", type=Input_TracedInputParameterValues, multiplicity=Multiplicity(1, 1))
    }
)
states401: BinaryAssociation = BinaryAssociation(
    name="states401",
    ends={
        Property(name="State402", type=umlTrace_Values_InputParameterValues_parameterValues_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="inputParameterValues_parameterValues_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
heldTokens403: BinaryAssociation = BinaryAssociation(
    name="heldTokens403",
    ends={
        Property(name="IntermediateActivities_TracedToken404", type=umlTrace_Values_ActivityNodeActivation_heldTokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivation_heldTokens_Value", type=IntermediateActivities_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
parent405: BinaryAssociation = BinaryAssociation(
    name="parent405",
    ends={
        Property(name="Traced407", type=umlTrace_Values_ActivityNodeActivation_heldTokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration406", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states408: BinaryAssociation = BinaryAssociation(
    name="states408",
    ends={
        Property(name="State409", type=umlTrace_Values_ActivityNodeActivation_heldTokens_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_heldTokens_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
node_ActivityNodeActivation410: BinaryAssociation = BinaryAssociation(
    name="node_ActivityNodeActivation410",
    ends={
        Property(name="uml_TracedActivityNode", type=umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
parent411: BinaryAssociation = BinaryAssociation(
    name="parent411",
    ends={
        Property(name="Traced413", type=umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration412", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
parent416: BinaryAssociation = BinaryAssociation(
    name="parent416",
    ends={
        Property(name="Traced418", type=umlTrace_Values_ActivityNodeActivation_running_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration417", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states419: BinaryAssociation = BinaryAssociation(
    name="states419",
    ends={
        Property(name="State420", type=umlTrace_Values_ActivityNodeActivation_running_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_running_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent421: BinaryAssociation = BinaryAssociation(
    name="parent421",
    ends={
        Property(name="Traced423", type=umlTrace_Values_ActivityNodeActivation_isRunning_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration422", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states424: BinaryAssociation = BinaryAssociation(
    name="states424",
    ends={
        Property(name="State425", type=umlTrace_Values_ActivityNodeActivation_isRunning_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_isRunning_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
outgoingEdges426: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges426",
    ends={
        Property(name="IntermediateActivities_TracedActivityEdgeInstance427", type=umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(0, 9999))
    }
)
parent428: BinaryAssociation = BinaryAssociation(
    name="parent428",
    ends={
        Property(name="Traced430", type=umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration429", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states431: BinaryAssociation = BinaryAssociation(
    name="states431",
    ends={
        Property(name="State432", type=umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_outgoingEdges_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
incomingEdges433: BinaryAssociation = BinaryAssociation(
    name="incomingEdges433",
    ends={
        Property(name="IntermediateActivities_TracedActivityEdgeInstance434", type=umlTrace_Values_ActivityNodeActivation_incomingEdges_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivation_incomingEdges_Value", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(0, 9999))
    }
)
states414: BinaryAssociation = BinaryAssociation(
    name="states414",
    ends={
        Property(name="State415", type=umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_node_ActivityNodeActivation_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
group_ActivityNodeActivation440: BinaryAssociation = BinaryAssociation(
    name="group_ActivityNodeActivation440",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivationGroup441", type=umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(0, 1))
    }
)
parent442: BinaryAssociation = BinaryAssociation(
    name="parent442",
    ends={
        Property(name="Traced444", type=umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration443", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states445: BinaryAssociation = BinaryAssociation(
    name="states445",
    ends={
        Property(name="State446", type=umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_group_ActivityNodeActivation_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
locus_ExtensionalValue447: BinaryAssociation = BinaryAssociation(
    name="locus_ExtensionalValue447",
    ends={
        Property(name="Loci_TracedLocus448", type=umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value", type=Loci_TracedLocus, multiplicity=Multiplicity(0, 1))
    }
)
parent449: BinaryAssociation = BinaryAssociation(
    name="parent449",
    ends={
        Property(name="Traced451", type=umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration450", type=Kernel_TracedExtensionalValue, multiplicity=Multiplicity(1, 1))
    }
)
states452: BinaryAssociation = BinaryAssociation(
    name="states452",
    ends={
        Property(name="State453", type=umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionalValue_locus_ExtensionalValue_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
activationGroup454: BinaryAssociation = BinaryAssociation(
    name="activationGroup454",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivationGroup455", type=umlTrace_Values_ActivityExecution_activationGroup_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ActivityExecution_activationGroup_Value", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1))
    }
)
parent456: BinaryAssociation = BinaryAssociation(
    name="parent456",
    ends={
        Property(name="Traced458", type=umlTrace_Values_ActivityExecution_activationGroup_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration457", type=IntermediateActivities_TracedActivityExecution, multiplicity=Multiplicity(1, 1))
    }
)
states459: BinaryAssociation = BinaryAssociation(
    name="states459",
    ends={
        Property(name="State460", type=umlTrace_Values_ActivityExecution_activationGroup_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityExecution_activationGroup_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
parent435: BinaryAssociation = BinaryAssociation(
    name="parent435",
    ends={
        Property(name="Traced437", type=umlTrace_Values_ActivityNodeActivation_incomingEdges_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration436", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1))
    }
)
states438: BinaryAssociation = BinaryAssociation(
    name="states438",
    ends={
        Property(name="State439", type=umlTrace_Values_ActivityNodeActivation_incomingEdges_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNodeActivation_incomingEdges_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
kernel_tracedObjects468: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedObjects468",
    ends={
        Property(name="Kernel_TracedObject469", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects", type=Kernel_TracedObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectors470: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectors470",
    ends={
        Property(name="uml_TracedConnector", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects471", type=uml_TracedConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOpaqueActions472: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOpaqueActions472",
    ends={
        Property(name="uml_TracedOpaqueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects473", type=uml_TracedOpaqueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDataTypes474: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDataTypes474",
    ends={
        Property(name="uml_TracedDataType", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects475", type=uml_TracedDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCommunicationPaths476: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCommunicationPaths476",
    ends={
        Property(name="uml_TracedCommunicationPath", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects477", type=uml_TracedCommunicationPath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedReferences478: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedReferences478",
    ends={
        Property(name="Kernel_TracedReference", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects479", type=Kernel_TracedReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPropertys480: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPropertys480",
    ends={
        Property(name="uml_TracedProperty", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects481", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedContinuations482: BinaryAssociation = BinaryAssociation(
    name="uml_tracedContinuations482",
    ends={
        Property(name="uml_TracedContinuation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects483", type=uml_TracedContinuation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRemoveStructuralFeatureValueActions484: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRemoveStructuralFeatureValueActions484",
    ends={
        Property(name="uml_TracedRemoveStructuralFeatureValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects485", type=uml_TracedRemoveStructuralFeatureValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSendSignalActions486: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSendSignalActions486",
    ends={
        Property(name="uml_TracedSendSignalAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects487", type=uml_TracedSendSignalAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedIntegerValues488: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedIntegerValues488",
    ends={
        Property(name="Kernel_TracedIntegerValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects489", type=Kernel_TracedIntegerValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locus_ExecutionEnvironment461: BinaryAssociation = BinaryAssociation(
    name="locus_ExecutionEnvironment461",
    ends={
        Property(name="Loci_TracedLocus462", type=umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value", type=Loci_TracedLocus, multiplicity=Multiplicity(1, 1))
    }
)
parent463: BinaryAssociation = BinaryAssociation(
    name="parent463",
    ends={
        Property(name="Traced465", type=umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="fumlConfiguration464", type=Loci_TracedExecutionEnvironment, multiplicity=Multiplicity(1, 1))
    }
)
states466: BinaryAssociation = BinaryAssociation(
    name="states466",
    ends={
        Property(name="State467", type=umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="executionEnvironment_locus_ExecutionEnvironment_Values", type=Values_umlTrace_State, multiplicity=Multiplicity(1, 9999))
    }
)
loci_tracedLocuss497: BinaryAssociation = BinaryAssociation(
    name="loci_tracedLocuss497",
    ends={
        Property(name="Loci_TracedLocus499", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects498", type=Loci_TracedLocus, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedArtifacts500: BinaryAssociation = BinaryAssociation(
    name="uml_tracedArtifacts500",
    ends={
        Property(name="uml_TracedArtifact", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects501", type=uml_TracedArtifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedJoinNodeActivations502: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedJoinNodeActivations502",
    ends={
        Property(name="IntermediateActivities_TracedJoinNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects503", type=IntermediateActivities_TracedJoinNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeConstraints504: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeConstraints504",
    ends={
        Property(name="uml_TracedTimeConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects505", type=uml_TracedTimeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInterfaceRealizations506: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInterfaceRealizations506",
    ends={
        Property(name="uml_TracedInterfaceRealization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects507", type=uml_TracedInterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivityFinalNodes508: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivityFinalNodes508",
    ends={
        Property(name="uml_TracedActivityFinalNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects509", type=uml_TracedActivityFinalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurationObservations510: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurationObservations510",
    ends={
        Property(name="uml_TracedDurationObservation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects511", type=uml_TracedDurationObservation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedInitialNodeActivations512: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedInitialNodeActivations512",
    ends={
        Property(name="IntermediateActivities_TracedInitialNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects513", type=IntermediateActivities_TracedInitialNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAcceptEventActions514: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAcceptEventActions514",
    ends={
        Property(name="uml_TracedAcceptEventAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects515", type=uml_TracedAcceptEventAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedEnumerationLiterals516: BinaryAssociation = BinaryAssociation(
    name="uml_tracedEnumerationLiterals516",
    ends={
        Property(name="uml_TracedEnumerationLiteral", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects517", type=uml_TracedEnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAddStructuralFeatureValueActions518: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAddStructuralFeatureValueActions518",
    ends={
        Property(name="uml_TracedAddStructuralFeatureValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects519", type=uml_TracedAddStructuralFeatureValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedForkedTokens490: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedForkedTokens490",
    ends={
        Property(name="IntermediateActivities_TracedForkedToken", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects491", type=IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOpaqueBehaviors492: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOpaqueBehaviors492",
    ends={
        Property(name="uml_TracedOpaqueBehavior", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects493", type=uml_TracedOpaqueBehavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loci_tracedExecutionFactorys494: BinaryAssociation = BinaryAssociation(
    name="loci_tracedExecutionFactorys494",
    ends={
        Property(name="Loci_TracedExecutionFactory496", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects495", type=Loci_TracedExecutionFactory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConsiderIgnoreFragments524: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConsiderIgnoreFragments524",
    ends={
        Property(name="uml_TracedConsiderIgnoreFragment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects525", type=uml_TracedConsiderIgnoreFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDataStoreNodes526: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDataStoreNodes526",
    ends={
        Property(name="uml_TracedDataStoreNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects527", type=uml_TracedDataStoreNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedFlowFinalNodes528: BinaryAssociation = BinaryAssociation(
    name="uml_tracedFlowFinalNodes528",
    ends={
        Property(name="uml_TracedFlowFinalNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects529", type=uml_TracedFlowFinalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInformationItems530: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInformationItems530",
    ends={
        Property(name="uml_TracedInformationItem", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects531", type=uml_TracedInformationItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCollaborations532: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCollaborations532",
    ends={
        Property(name="uml_TracedCollaboration", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects533", type=uml_TracedCollaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateSignatures534: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateSignatures534",
    ends={
        Property(name="uml_TracedTemplateSignature", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects535", type=uml_TracedTemplateSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedBroadcastSignalActions536: BinaryAssociation = BinaryAssociation(
    name="uml_tracedBroadcastSignalActions536",
    ends={
        Property(name="uml_TracedBroadcastSignalAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects537", type=uml_TracedBroadcastSignalAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDeployments538: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDeployments538",
    ends={
        Property(name="uml_TracedDeployment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects539", type=uml_TracedDeployment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPorts540: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPorts540",
    ends={
        Property(name="uml_TracedPort", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects541", type=uml_TracedPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeIntervals542: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeIntervals542",
    ends={
        Property(name="uml_TracedTimeInterval", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects543", type=uml_TracedTimeInterval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadLinkActions520: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadLinkActions520",
    ends={
        Property(name="uml_TracedReadLinkAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects521", type=uml_TracedReadLinkAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExpressions522: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExpressions522",
    ends={
        Property(name="uml_TracedExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects523", type=uml_TracedExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeEvents549: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeEvents549",
    ends={
        Property(name="umlTrace_Traced_TracedObjects550", type=uml_TracedTimeEvent, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="uml_TracedTimeEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1))
    }
)
basicBehaviors_tracedParameterValues551: BinaryAssociation = BinaryAssociation(
    name="basicBehaviors_tracedParameterValues551",
    ends={
        Property(name="BasicBehaviors_TracedParameterValue553", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects552", type=BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProtocolTransitions554: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProtocolTransitions554",
    ends={
        Property(name="uml_TracedProtocolTransition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects555", type=uml_TracedProtocolTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityFinalNodeActivations556: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityFinalNodeActivations556",
    ends={
        Property(name="IntermediateActivities_TracedActivityFinalNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects557", type=IntermediateActivities_TracedActivityFinalNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPackages558: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPackages558",
    ends={
        Property(name="uml_TracedPackage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects559", type=uml_TracedPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConstraints560: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConstraints560",
    ends={
        Property(name="uml_TracedConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects561", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGeneralizationSets562: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGeneralizationSets562",
    ends={
        Property(name="uml_TracedGeneralizationSet", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects563", type=uml_TracedGeneralizationSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReduceActions564: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReduceActions564",
    ends={
        Property(name="uml_TracedReduceAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects565", type=uml_TracedReduceAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInputPins566: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInputPins566",
    ends={
        Property(name="uml_TracedInputPin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects567", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtensions544: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtensions544",
    ends={
        Property(name="uml_TracedExtension", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects545", type=uml_TracedExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loci_tracedSemanticVisitors546: BinaryAssociation = BinaryAssociation(
    name="loci_tracedSemanticVisitors546",
    ends={
        Property(name="Loci_TracedSemanticVisitor548", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects547", type=Loci_TracedSemanticVisitor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedComponentRealizations572: BinaryAssociation = BinaryAssociation(
    name="uml_tracedComponentRealizations572",
    ends={
        Property(name="uml_TracedComponentRealization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects573", type=uml_TracedComponentRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAssociationClasss574: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAssociationClasss574",
    ends={
        Property(name="uml_TracedAssociationClass", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects575", type=uml_TracedAssociationClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSlots576: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSlots576",
    ends={
        Property(name="uml_TracedSlot", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects577", type=uml_TracedSlot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSignalEvents578: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSignalEvents578",
    ends={
        Property(name="uml_TracedSignalEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects579", type=uml_TracedSignalEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtensionPoints580: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtensionPoints580",
    ends={
        Property(name="uml_TracedExtensionPoint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects581", type=uml_TracedExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedJoinNodes582: BinaryAssociation = BinaryAssociation(
    name="uml_tracedJoinNodes582",
    ends={
        Property(name="uml_TracedJoinNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects583", type=uml_TracedJoinNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedOutputPinActivations584: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedOutputPinActivations584",
    ends={
        Property(name="BasicActions_TracedOutputPinActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects585", type=BasicActions_TracedOutputPinActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStartObjectBehaviorActions586: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStartObjectBehaviorActions586",
    ends={
        Property(name="uml_TracedStartObjectBehaviorAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects587", type=uml_TracedStartObjectBehaviorAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedElementImports588: BinaryAssociation = BinaryAssociation(
    name="uml_tracedElementImports588",
    ends={
        Property(name="uml_TracedElementImport", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects589", type=uml_TracedElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSequenceNodes568: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSequenceNodes568",
    ends={
        Property(name="uml_TracedSequenceNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects569", type=uml_TracedSequenceNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractionConstraints570: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractionConstraints570",
    ends={
        Property(name="uml_TracedInteractionConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects571", type=uml_TracedInteractionConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOccurrenceSpecifications594: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOccurrenceSpecifications594",
    ends={
        Property(name="uml_TracedOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects595", type=uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityNodeActivationGroups596: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityNodeActivationGroups596",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivationGroup598", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects597", type=IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedValueSpecificationActionActivations599: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedValueSpecificationActionActivations599",
    ends={
        Property(name="IntermediateActions_TracedValueSpecificationActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects600", type=IntermediateActions_TracedValueSpecificationActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStringExpressions601: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStringExpressions601",
    ends={
        Property(name="uml_TracedStringExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects602", type=uml_TracedStringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loci_tracedExecutors603: BinaryAssociation = BinaryAssociation(
    name="loci_tracedExecutors603",
    ends={
        Property(name="Loci_TracedExecutor605", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects604", type=Loci_TracedExecutor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedReadStructuralFeatureActionActivations606: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedReadStructuralFeatureActionActivations606",
    ends={
        Property(name="IntermediateActions_TracedReadStructuralFeatureActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects607", type=IntermediateActions_TracedReadStructuralFeatureActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStereotypes608: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStereotypes608",
    ends={
        Property(name="uml_TracedStereotype", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects609", type=uml_TracedStereotype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInterfaces610: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInterfaces610",
    ends={
        Property(name="uml_TracedInterface", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects611", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConditionalNodes612: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConditionalNodes612",
    ends={
        Property(name="uml_TracedConditionalNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects613", type=uml_TracedConditionalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCreateObjectActions590: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCreateObjectActions590",
    ends={
        Property(name="uml_TracedCreateObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects591", type=uml_TracedCreateObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExecutionEnvironments592: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExecutionEnvironments592",
    ends={
        Property(name="uml_TracedExecutionEnvironment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects593", type=uml_TracedExecutionEnvironment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedComponents618: BinaryAssociation = BinaryAssociation(
    name="uml_tracedComponents618",
    ends={
        Property(name="uml_TracedComponent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects619", type=uml_TracedComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtensionEnds620: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtensionEnds620",
    ends={
        Property(name="uml_TracedExtensionEnd", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects621", type=uml_TracedExtensionEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStateMachines622: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStateMachines622",
    ends={
        Property(name="uml_TracedStateMachine", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects623", type=uml_TracedStateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedMergeNodeActivations624: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedMergeNodeActivations624",
    ends={
        Property(name="IntermediateActivities_TracedMergeNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects625", type=IntermediateActivities_TracedMergeNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractions626: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractions626",
    ends={
        Property(name="uml_TracedInteraction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects627", type=uml_TracedInteraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralStrings628: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralStrings628",
    ends={
        Property(name="uml_TracedLiteralString", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects629", type=uml_TracedLiteralString, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRealizations630: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRealizations630",
    ends={
        Property(name="uml_TracedRealization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects631", type=uml_TracedRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadLinkObjectEndActions614: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadLinkObjectEndActions614",
    ends={
        Property(name="uml_TracedReadLinkObjectEndAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects615", type=uml_TracedReadLinkObjectEndAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAnyReceiveEvents616: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAnyReceiveEvents616",
    ends={
        Property(name="uml_TracedAnyReceiveEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects617", type=uml_TracedAnyReceiveEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectableElementTemplateParameters636: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectableElementTemplateParameters636",
    ends={
        Property(name="uml_TracedConnectableElementTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects637", type=uml_TracedConnectableElementTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSendObjectActions638: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSendObjectActions638",
    ends={
        Property(name="uml_TracedSendObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects639", type=uml_TracedSendObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLifelines640: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLifelines640",
    ends={
        Property(name="uml_TracedLifeline", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects641", type=uml_TracedLifeline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeObservations642: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeObservations642",
    ends={
        Property(name="uml_TracedTimeObservation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects643", type=uml_TracedTimeObservation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedControlTokens644: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedControlTokens644",
    ends={
        Property(name="IntermediateActivities_TracedControlToken", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects645", type=IntermediateActivities_TracedControlToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCreateLinkObjectActions646: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCreateLinkObjectActions646",
    ends={
        Property(name="uml_TracedCreateLinkObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects647", type=uml_TracedCreateLinkObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExpansionRegions648: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExpansionRegions648",
    ends={
        Property(name="uml_TracedExpansionRegion", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects649", type=uml_TracedExpansionRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStartClassifierBehaviorActions632: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStartClassifierBehaviorActions632",
    ends={
        Property(name="uml_TracedStartClassifierBehaviorAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects633", type=uml_TracedStartClassifierBehaviorAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCallEvents634: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCallEvents634",
    ends={
        Property(name="uml_TracedCallEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects635", type=uml_TracedCallEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPrimitiveTypes654: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPrimitiveTypes654",
    ends={
        Property(name="uml_TracedPrimitiveType656", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects655", type=uml_TracedPrimitiveType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProtocolConformances657: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProtocolConformances657",
    ends={
        Property(name="uml_TracedProtocolConformance", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects658", type=uml_TracedProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedEnumerations659: BinaryAssociation = BinaryAssociation(
    name="uml_tracedEnumerations659",
    ends={
        Property(name="uml_TracedEnumeration", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects660", type=uml_TracedEnumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCollaborationUses661: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCollaborationUses661",
    ends={
        Property(name="uml_TracedCollaborationUse", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects662", type=uml_TracedCollaborationUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivityPartitions663: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivityPartitions663",
    ends={
        Property(name="uml_TracedActivityPartition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects664", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLinkEndDestructionDatas665: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLinkEndDestructionDatas665",
    ends={
        Property(name="uml_TracedLinkEndDestructionData", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects666", type=uml_TracedLinkEndDestructionData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurationIntervals667: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurationIntervals667",
    ends={
        Property(name="uml_TracedDurationInterval", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects668", type=uml_TracedDurationInterval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedBooleanValues650: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedBooleanValues650",
    ends={
        Property(name="Kernel_TracedBooleanValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects651", type=Kernel_TracedBooleanValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLoopNodes652: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLoopNodes652",
    ends={
        Property(name="uml_TracedLoopNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects653", type=uml_TracedLoopNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStates673: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStates673",
    ends={
        Property(name="uml_TracedState", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects674", type=uml_TracedState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedObjectTokens675: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedObjectTokens675",
    ends={
        Property(name="IntermediateActivities_TracedObjectToken", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects676", type=IntermediateActivities_TracedObjectToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedCallBehaviorActionActivations677: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedCallBehaviorActionActivations677",
    ends={
        Property(name="BasicActions_TracedCallBehaviorActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects678", type=BasicActions_TracedCallBehaviorActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedAddStructuralFeatureValueActionActivations679: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedAddStructuralFeatureValueActionActivations679",
    ends={
        Property(name="IntermediateActions_TracedAddStructuralFeatureValueActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects680", type=IntermediateActions_TracedAddStructuralFeatureValueActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClassifierTemplateParameters681: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClassifierTemplateParameters681",
    ends={
        Property(name="uml_TracedClassifierTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects682", type=uml_TracedClassifierTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivityParameterNodes683: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivityParameterNodes683",
    ends={
        Property(name="uml_TracedActivityParameterNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects684", type=uml_TracedActivityParameterNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integerFunctions_tracedIntegerLessFunctionBehaviorExecutions685: BinaryAssociation = BinaryAssociation(
    name="integerFunctions_tracedIntegerLessFunctionBehaviorExecutions685",
    ends={
        Property(name="IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects686", type=IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedIncludes669: BinaryAssociation = BinaryAssociation(
    name="uml_tracedIncludes669",
    ends={
        Property(name="uml_TracedInclude", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects670", type=uml_TracedInclude, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDestructionOccurrenceSpecifications671: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDestructionOccurrenceSpecifications671",
    ends={
        Property(name="uml_TracedDestructionOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects672", type=uml_TracedDestructionOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurations689: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurations689",
    ends={
        Property(name="uml_TracedDuration", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects690", type=uml_TracedDuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClasss691: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClasss691",
    ends={
        Property(name="uml_TracedClass693", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects692", type=uml_TracedClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedUsages694: BinaryAssociation = BinaryAssociation(
    name="uml_tracedUsages694",
    ends={
        Property(name="uml_TracedUsage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects695", type=uml_TracedUsage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralUnlimitedNaturals696: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralUnlimitedNaturals696",
    ends={
        Property(name="uml_TracedLiteralUnlimitedNatural", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects697", type=uml_TracedLiteralUnlimitedNatural, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStructuredActivityNodes698: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStructuredActivityNodes698",
    ends={
        Property(name="uml_TracedStructuredActivityNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects699", type=uml_TracedStructuredActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAbstractions700: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAbstractions700",
    ends={
        Property(name="uml_TracedAbstraction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects701", type=uml_TracedAbstraction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedParameterSets687: BinaryAssociation = BinaryAssociation(
    name="uml_tracedParameterSets687",
    ends={
        Property(name="uml_TracedParameterSet", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects688", type=uml_TracedParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadStructuralFeatureActions706: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadStructuralFeatureActions706",
    ends={
        Property(name="uml_TracedReadStructuralFeatureAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects707", type=uml_TracedReadStructuralFeatureAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedMergeNodes708: BinaryAssociation = BinaryAssociation(
    name="uml_tracedMergeNodes708",
    ends={
        Property(name="uml_TracedMergeNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects709", type=uml_TracedMergeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRedefinableTemplateSignatures710: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRedefinableTemplateSignatures710",
    ends={
        Property(name="uml_TracedRedefinableTemplateSignature", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects711", type=uml_TracedRedefinableTemplateSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCreateLinkActions712: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCreateLinkActions712",
    ends={
        Property(name="uml_TracedCreateLinkAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects713", type=uml_TracedCreateLinkAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGeneralizations714: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGeneralizations714",
    ends={
        Property(name="uml_TracedGeneralization", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects715", type=uml_TracedGeneralization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPartDecompositions716: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPartDecompositions716",
    ends={
        Property(name="uml_TracedPartDecomposition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects717", type=uml_TracedPartDecomposition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedOpaqueActionActivations702: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedOpaqueActionActivations702",
    ends={
        Property(name="BasicActions_TracedOpaqueActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects703", type=BasicActions_TracedOpaqueActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedLiteralBooleanEvaluations704: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedLiteralBooleanEvaluations704",
    ends={
        Property(name="Kernel_TracedLiteralBooleanEvaluation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects705", type=Kernel_TracedLiteralBooleanEvaluation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOperationTemplateParameters718: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOperationTemplateParameters718",
    ends={
        Property(name="uml_TracedOperationTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects719", type=uml_TracedOperationTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadLinkObjectEndQualifierActions720: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadLinkObjectEndQualifierActions720",
    ends={
        Property(name="uml_TracedReadLinkObjectEndQualifierAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects721", type=uml_TracedReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateParameterSubstitutions722: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateParameterSubstitutions722",
    ends={
        Property(name="uml_TracedTemplateParameterSubstitution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects723", type=uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExtends724: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExtends724",
    ends={
        Property(name="uml_TracedExtend", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects725", type=uml_TracedExtend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadVariableActions726: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadVariableActions726",
    ends={
        Property(name="uml_TracedReadVariableAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects727", type=uml_TracedReadVariableAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedMessages728: BinaryAssociation = BinaryAssociation(
    name="uml_tracedMessages728",
    ends={
        Property(name="uml_TracedMessage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects729", type=uml_TracedMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInitialNodes734: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInitialNodes734",
    ends={
        Property(name="uml_TracedInitialNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects735", type=uml_TracedInitialNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralIntegers736: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralIntegers736",
    ends={
        Property(name="uml_TracedLiteralInteger", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects737", type=uml_TracedLiteralInteger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClearVariableActions738: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClearVariableActions738",
    ends={
        Property(name="uml_TracedClearVariableAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects739", type=uml_TracedClearVariableAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedDecisionNodeActivations740: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedDecisionNodeActivations740",
    ends={
        Property(name="IntermediateActivities_TracedDecisionNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects741", type=IntermediateActivities_TracedDecisionNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProfileApplications742: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProfileApplications742",
    ends={
        Property(name="uml_TracedProfileApplication", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects743", type=uml_TracedProfileApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralBooleans730: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralBooleans730",
    ends={
        Property(name="uml_TracedLiteralBoolean", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects731", type=uml_TracedLiteralBoolean, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedQualifierValues732: BinaryAssociation = BinaryAssociation(
    name="uml_tracedQualifierValues732",
    ends={
        Property(name="uml_TracedQualifierValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects733", type=uml_TracedQualifierValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedMessageOccurrenceSpecifications748: BinaryAssociation = BinaryAssociation(
    name="uml_tracedMessageOccurrenceSpecifications748",
    ends={
        Property(name="uml_TracedMessageOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects749", type=uml_TracedMessageOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDurationConstraints750: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDurationConstraints750",
    ends={
        Property(name="uml_TracedDurationConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects751", type=uml_TracedDurationConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedImages752: BinaryAssociation = BinaryAssociation(
    name="uml_tracedImages752",
    ends={
        Property(name="uml_TracedImage", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects753", type=uml_TracedImage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedParameters754: BinaryAssociation = BinaryAssociation(
    name="uml_tracedParameters754",
    ends={
        Property(name="uml_TracedParameter756", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects755", type=uml_TracedParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActionInputPins757: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActionInputPins757",
    ends={
        Property(name="uml_TracedActionInputPin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects758", type=uml_TracedActionInputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTriggers759: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTriggers759",
    ends={
        Property(name="uml_TracedTrigger", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects760", type=uml_TracedTrigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateParameters744: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateParameters744",
    ends={
        Property(name="uml_TracedTemplateParameter", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects745", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectorEnds746: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectorEnds746",
    ends={
        Property(name="uml_TracedConnectorEnd", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects747", type=uml_TracedConnectorEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProfiles763: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProfiles763",
    ends={
        Property(name="uml_TracedProfile", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects764", type=uml_TracedProfile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedIntervals765: BinaryAssociation = BinaryAssociation(
    name="uml_tracedIntervals765",
    ends={
        Property(name="uml_TracedInterval", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects766", type=uml_TracedInterval, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedForkNodeActivations767: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedForkNodeActivations767",
    ends={
        Property(name="IntermediateActivities_TracedForkNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects768", type=IntermediateActivities_TracedForkNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedIntervalConstraints769: BinaryAssociation = BinaryAssociation(
    name="uml_tracedIntervalConstraints769",
    ends={
        Property(name="uml_TracedIntervalConstraint", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects770", type=uml_TracedIntervalConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedTokens771: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedTokens771",
    ends={
        Property(name="IntermediateActivities_TracedToken773", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects772", type=IntermediateActivities_TracedToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCallOperationActions761: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCallOperationActions761",
    ends={
        Property(name="uml_TracedCallOperationAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects762", type=uml_TracedCallOperationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integerFunctions_tracedIntegerGreaterFunctionBehaviorExecutions778: BinaryAssociation = BinaryAssociation(
    name="integerFunctions_tracedIntegerGreaterFunctionBehaviorExecutions778",
    ends={
        Property(name="IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects779", type=IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadIsClassifiedObjectActions780: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadIsClassifiedObjectActions780",
    ends={
        Property(name="uml_TracedReadIsClassifiedObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects781", type=uml_TracedReadIsClassifiedObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedProtocolStateMachines782: BinaryAssociation = BinaryAssociation(
    name="uml_tracedProtocolStateMachines782",
    ends={
        Property(name="uml_TracedProtocolStateMachine", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects783", type=uml_TracedProtocolStateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOutputPins784: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOutputPins784",
    ends={
        Property(name="uml_TracedOutputPin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects785", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedOffers786: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedOffers786",
    ends={
        Property(name="IntermediateActivities_TracedOffer788", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects787", type=IntermediateActivities_TracedOffer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInstanceSpecifications774: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInstanceSpecifications774",
    ends={
        Property(name="uml_TracedInstanceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects775", type=uml_TracedInstanceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedValuePins776: BinaryAssociation = BinaryAssociation(
    name="uml_tracedValuePins776",
    ends={
        Property(name="uml_TracedValuePin", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects777", type=uml_TracedValuePin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDecisionNodes791: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDecisionNodes791",
    ends={
        Property(name="uml_TracedDecisionNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects792", type=uml_TracedDecisionNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedValueSpecificationActions793: BinaryAssociation = BinaryAssociation(
    name="uml_tracedValueSpecificationActions793",
    ends={
        Property(name="uml_TracedValueSpecificationAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects794", type=uml_TracedValueSpecificationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRegions795: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRegions795",
    ends={
        Property(name="uml_TracedRegion", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects796", type=uml_TracedRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInterruptibleActivityRegions797: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInterruptibleActivityRegions797",
    ends={
        Property(name="uml_TracedInterruptibleActivityRegion", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects798", type=uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDestroyLinkActions799: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDestroyLinkActions799",
    ends={
        Property(name="uml_TracedDestroyLinkAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects800", type=uml_TracedDestroyLinkAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityParameterNodeActivations789: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityParameterNodeActivations789",
    ends={
        Property(name="IntermediateActivities_TracedActivityParameterNodeActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects790", type=IntermediateActivities_TracedActivityParameterNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractionOperands805: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractionOperands805",
    ends={
        Property(name="uml_TracedInteractionOperand", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects806", type=uml_TracedInteractionOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInformationFlows807: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInformationFlows807",
    ends={
        Property(name="uml_TracedInformationFlow", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects808", type=uml_TracedInformationFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPseudostates809: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPseudostates809",
    ends={
        Property(name="uml_TracedPseudostate", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects810", type=uml_TracedPseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedUseCases811: BinaryAssociation = BinaryAssociation(
    name="uml_tracedUseCases811",
    ends={
        Property(name="uml_TracedUseCase", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects812", type=uml_TracedUseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReplyActions813: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReplyActions813",
    ends={
        Property(name="uml_TracedReplyAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects814", type=uml_TracedReplyAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedFinalStates801: BinaryAssociation = BinaryAssociation(
    name="uml_tracedFinalStates801",
    ends={
        Property(name="uml_TracedFinalState", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects802", type=uml_TracedFinalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integerFunctions_tracedIntegerPlusFunctionBehaviorExecutions803: BinaryAssociation = BinaryAssociation(
    name="integerFunctions_tracedIntegerPlusFunctionBehaviorExecutions803",
    ends={
        Property(name="IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects804", type=IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCombinedFragments817: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCombinedFragments817",
    ends={
        Property(name="uml_TracedCombinedFragment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects818", type=uml_TracedCombinedFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClauses819: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClauses819",
    ends={
        Property(name="uml_TracedClause", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects820", type=uml_TracedClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInstanceValues821: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInstanceValues821",
    ends={
        Property(name="uml_TracedInstanceValue", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects822", type=uml_TracedInstanceValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDependencys823: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDependencys823",
    ends={
        Property(name="uml_TracedDependency", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects824", type=uml_TracedDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTimeExpressions825: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTimeExpressions825",
    ends={
        Property(name="uml_TracedTimeExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects826", type=uml_TracedTimeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActions_tracedCreateObjectActionActivations815: BinaryAssociation = BinaryAssociation(
    name="intermediateActions_tracedCreateObjectActionActivations815",
    ends={
        Property(name="IntermediateActions_TracedCreateObjectActionActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects816", type=IntermediateActions_TracedCreateObjectActionActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedManifestations830: BinaryAssociation = BinaryAssociation(
    name="uml_tracedManifestations830",
    ends={
        Property(name="uml_TracedManifestation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects831", type=uml_TracedManifestation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadExtentActions832: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadExtentActions832",
    ends={
        Property(name="uml_TracedReadExtentAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects833", type=uml_TracedReadExtentAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicActions_tracedInputPinActivations834: BinaryAssociation = BinaryAssociation(
    name="basicActions_tracedInputPinActivations834",
    ends={
        Property(name="BasicActions_TracedInputPinActivation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects835", type=BasicActions_TracedInputPinActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTransitions836: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTransitions836",
    ends={
        Property(name="uml_TracedTransition", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects837", type=uml_TracedTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLinkEndDatas838: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLinkEndDatas838",
    ends={
        Property(name="uml_TracedLinkEndData", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects839", type=uml_TracedLinkEndData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityEdgeInstances827: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityEdgeInstances827",
    ends={
        Property(name="IntermediateActivities_TracedActivityEdgeInstance829", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects828", type=IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedNodes842: BinaryAssociation = BinaryAssociation(
    name="uml_tracedNodes842",
    ends={
        Property(name="uml_TracedNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects843", type=uml_TracedNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPackageMerges844: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPackageMerges844",
    ends={
        Property(name="uml_TracedPackageMerge", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects845", type=uml_TracedPackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedModels846: BinaryAssociation = BinaryAssociation(
    name="uml_tracedModels846",
    ends={
        Property(name="uml_TracedModel", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects847", type=uml_TracedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedObjectFlows848: BinaryAssociation = BinaryAssociation(
    name="uml_tracedObjectFlows848",
    ends={
        Property(name="uml_TracedObjectFlow", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects849", type=uml_TracedObjectFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedChangeEvents850: BinaryAssociation = BinaryAssociation(
    name="uml_tracedChangeEvents850",
    ends={
        Property(name="uml_TracedChangeEvent", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects851", type=uml_TracedChangeEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input_tracedInputParameterValuess840: BinaryAssociation = BinaryAssociation(
    name="input_tracedInputParameterValuess840",
    ends={
        Property(name="Input_TracedInputParameterValues", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects841", type=Input_TracedInputParameterValues, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedForkNodes854: BinaryAssociation = BinaryAssociation(
    name="uml_tracedForkNodes854",
    ends={
        Property(name="uml_TracedForkNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects855", type=uml_TracedForkNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSignals856: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSignals856",
    ends={
        Property(name="uml_TracedSignal", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects857", type=uml_TracedSignal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedComments858: BinaryAssociation = BinaryAssociation(
    name="uml_tracedComments858",
    ends={
        Property(name="uml_TracedComment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects859", type=uml_TracedComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralNulls860: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralNulls860",
    ends={
        Property(name="uml_TracedLiteralNull", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects861", type=uml_TracedLiteralNull, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExpansionNodes862: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExpansionNodes862",
    ends={
        Property(name="uml_TracedExpansionNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects863", type=uml_TracedExpansionNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDestroyObjectActions852: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDestroyObjectActions852",
    ends={
        Property(name="uml_TracedDestroyObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects853", type=uml_TracedDestroyObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRaiseExceptionActions866: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRaiseExceptionActions866",
    ends={
        Property(name="uml_TracedRaiseExceptionAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects867", type=uml_TracedRaiseExceptionAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityNodeActivations868: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityNodeActivations868",
    ends={
        Property(name="IntermediateActivities_TracedActivityNodeActivation870", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects869", type=IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAddVariableValueActions871: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAddVariableValueActions871",
    ends={
        Property(name="uml_TracedAddVariableValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects872", type=uml_TracedAddVariableValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClearAssociationActions873: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClearAssociationActions873",
    ends={
        Property(name="uml_TracedClearAssociationAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects874", type=uml_TracedClearAssociationAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTestIdentityActions875: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTestIdentityActions875",
    ends={
        Property(name="uml_TracedTestIdentityAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects876", type=uml_TracedTestIdentityAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReceptions864: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReceptions864",
    ends={
        Property(name="uml_TracedReception", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects865", type=uml_TracedReception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOperations879: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOperations879",
    ends={
        Property(name="uml_TracedOperation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects880", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedPackageImports881: BinaryAssociation = BinaryAssociation(
    name="uml_tracedPackageImports881",
    ends={
        Property(name="uml_TracedPackageImport", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects882", type=uml_TracedPackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExecutionOccurrenceSpecifications883: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExecutionOccurrenceSpecifications883",
    ends={
        Property(name="uml_TracedExecutionOccurrenceSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects884", type=uml_TracedExecutionOccurrenceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedExceptionHandlers885: BinaryAssociation = BinaryAssociation(
    name="uml_tracedExceptionHandlers885",
    ends={
        Property(name="uml_TracedExceptionHandler", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects886", type=uml_TracedExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedVariables887: BinaryAssociation = BinaryAssociation(
    name="uml_tracedVariables887",
    ends={
        Property(name="uml_TracedVariable", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects888", type=uml_TracedVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedControlFlows877: BinaryAssociation = BinaryAssociation(
    name="uml_tracedControlFlows877",
    ends={
        Property(name="uml_TracedControlFlow", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects878", type=uml_TracedControlFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAssociations891: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAssociations891",
    ends={
        Property(name="uml_TracedAssociation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects892", type=uml_TracedAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedStateInvariants893: BinaryAssociation = BinaryAssociation(
    name="uml_tracedStateInvariants893",
    ends={
        Property(name="uml_TracedStateInvariant", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects894", type=uml_TracedStateInvariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLiteralReals895: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLiteralReals895",
    ends={
        Property(name="uml_TracedLiteralReal", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects896", type=uml_TracedLiteralReal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedRemoveVariableValueActions897: BinaryAssociation = BinaryAssociation(
    name="uml_tracedRemoveVariableValueActions897",
    ends={
        Property(name="uml_TracedRemoveVariableValueAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects898", type=uml_TracedRemoveVariableValueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedInteractionUses889: BinaryAssociation = BinaryAssociation(
    name="uml_tracedInteractionUses889",
    ends={
        Property(name="uml_TracedInteractionUse", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects890", type=uml_TracedInteractionUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedSubstitutions901: BinaryAssociation = BinaryAssociation(
    name="uml_tracedSubstitutions901",
    ends={
        Property(name="uml_TracedSubstitution", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects902", type=uml_TracedSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGates903: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGates903",
    ends={
        Property(name="uml_TracedGate", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects904", type=uml_TracedGate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedGeneralOrderings905: BinaryAssociation = BinaryAssociation(
    name="uml_tracedGeneralOrderings905",
    ends={
        Property(name="uml_TracedGeneralOrdering", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects906", type=uml_TracedGeneralOrdering, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCallBehaviorActions907: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCallBehaviorActions907",
    ends={
        Property(name="uml_TracedCallBehaviorAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects908", type=uml_TracedCallBehaviorAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReclassifyObjectActions909: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReclassifyObjectActions909",
    ends={
        Property(name="uml_TracedReclassifyObjectAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects910", type=uml_TracedReclassifyObjectAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDevices899: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDevices899",
    ends={
        Property(name="uml_TracedDevice", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects900", type=uml_TracedDevice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedConnectionPointReferences913: BinaryAssociation = BinaryAssociation(
    name="uml_tracedConnectionPointReferences913",
    ends={
        Property(name="uml_TracedConnectionPointReference", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects914", type=uml_TracedConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActionExecutionSpecifications915: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActionExecutionSpecifications915",
    ends={
        Property(name="uml_TracedActionExecutionSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects916", type=uml_TracedActionExecutionSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedReadSelfActions917: BinaryAssociation = BinaryAssociation(
    name="uml_tracedReadSelfActions917",
    ends={
        Property(name="uml_TracedReadSelfAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects918", type=uml_TracedReadSelfAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedAcceptCallActions919: BinaryAssociation = BinaryAssociation(
    name="uml_tracedAcceptCallActions919",
    ends={
        Property(name="uml_TracedAcceptCallAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects920", type=uml_TracedAcceptCallAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActivitys911: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActivitys911",
    ends={
        Property(name="uml_TracedActivity", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects912", type=uml_TracedActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intermediateActivities_tracedActivityExecutions923: BinaryAssociation = BinaryAssociation(
    name="intermediateActivities_tracedActivityExecutions923",
    ends={
        Property(name="IntermediateActivities_TracedActivityExecution925", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects924", type=IntermediateActivities_TracedActivityExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedTemplateBindings926: BinaryAssociation = BinaryAssociation(
    name="uml_tracedTemplateBindings926",
    ends={
        Property(name="uml_TracedTemplateBinding", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects927", type=uml_TracedTemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedClearStructuralFeatureActions928: BinaryAssociation = BinaryAssociation(
    name="uml_tracedClearStructuralFeatureActions928",
    ends={
        Property(name="uml_TracedClearStructuralFeatureAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects929", type=uml_TracedClearStructuralFeatureAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedLinkEndCreationDatas921: BinaryAssociation = BinaryAssociation(
    name="uml_tracedLinkEndCreationDatas921",
    ends={
        Property(name="uml_TracedLinkEndCreationData", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects922", type=uml_TracedLinkEndCreationData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kernel_tracedLiteralIntegerEvaluations932: BinaryAssociation = BinaryAssociation(
    name="kernel_tracedLiteralIntegerEvaluations932",
    ends={
        Property(name="Kernel_TracedLiteralIntegerEvaluation", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects933", type=Kernel_TracedLiteralIntegerEvaluation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedOpaqueExpressions934: BinaryAssociation = BinaryAssociation(
    name="uml_tracedOpaqueExpressions934",
    ends={
        Property(name="uml_TracedOpaqueExpression", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects935", type=uml_TracedOpaqueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedFunctionBehaviors936: BinaryAssociation = BinaryAssociation(
    name="uml_tracedFunctionBehaviors936",
    ends={
        Property(name="uml_TracedFunctionBehavior", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects937", type=uml_TracedFunctionBehavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedDeploymentSpecifications938: BinaryAssociation = BinaryAssociation(
    name="uml_tracedDeploymentSpecifications938",
    ends={
        Property(name="uml_TracedDeploymentSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects939", type=uml_TracedDeploymentSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loci_tracedExecutionEnvironments930: BinaryAssociation = BinaryAssociation(
    name="loci_tracedExecutionEnvironments930",
    ends={
        Property(name="Loci_TracedExecutionEnvironment", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects931", type=Loci_TracedExecutionEnvironment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedBehaviorExecutionSpecifications942: BinaryAssociation = BinaryAssociation(
    name="uml_tracedBehaviorExecutionSpecifications942",
    ends={
        Property(name="uml_TracedBehaviorExecutionSpecification", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects943", type=uml_TracedBehaviorExecutionSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedUnmarshallActions944: BinaryAssociation = BinaryAssociation(
    name="uml_tracedUnmarshallActions944",
    ends={
        Property(name="uml_TracedUnmarshallAction", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects945", type=uml_TracedUnmarshallAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedCentralBufferNodes946: BinaryAssociation = BinaryAssociation(
    name="uml_tracedCentralBufferNodes946",
    ends={
        Property(name="uml_TracedCentralBufferNode", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects947", type=uml_TracedCentralBufferNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uml_tracedActors940: BinaryAssociation = BinaryAssociation(
    name="uml_tracedActors940",
    ends={
        Property(name="uml_TracedActor", type=umlTrace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_Traced_TracedObjects941", type=uml_TracedActor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value_IntegerValueTrace954: BinaryAssociation = BinaryAssociation(
    name="value_IntegerValueTrace954",
    ends={
        Property(name="Values956", type=umlTrace_Kernel_TracedIntegerValue, multiplicity=Multiplicity(1, 1)),
        Property(name="IntegerValue_value_IntegerValue_Value955", type=IntegerValue_value_IntegerValue_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeTrace957: BinaryAssociation = BinaryAssociation(
    name="typeTrace957",
    ends={
        Property(name="Values959", type=umlTrace_Kernel_TracedPrimitiveValue, multiplicity=Multiplicity(1, 1)),
        Property(name="PrimitiveValue_type_Value958", type=PrimitiveValue_type_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification_EvaluationTrace960: BinaryAssociation = BinaryAssociation(
    name="specification_EvaluationTrace960",
    ends={
        Property(name="Values962", type=umlTrace_Kernel_TracedEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="Evaluation_specification_Evaluation_Value961", type=Evaluation_specification_Evaluation_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locus_EvaluationTrace963: BinaryAssociation = BinaryAssociation(
    name="locus_EvaluationTrace963",
    ends={
        Property(name="Values965", type=umlTrace_Kernel_TracedEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="Evaluation_locus_Evaluation_Value964", type=Evaluation_locus_Evaluation_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value_BooleanValueTrace966: BinaryAssociation = BinaryAssociation(
    name="value_BooleanValueTrace966",
    ends={
        Property(name="Values968", type=umlTrace_Kernel_TracedBooleanValue, multiplicity=Multiplicity(1, 1)),
        Property(name="BooleanValue_value_BooleanValue_Value967", type=BooleanValue_value_BooleanValue_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typesTrace948: BinaryAssociation = BinaryAssociation(
    name="typesTrace948",
    ends={
        Property(name="Values950", type=umlTrace_Kernel_TracedObject, multiplicity=Multiplicity(1, 1)),
        Property(name="Object_types_Value949", type=Object_types_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referentTrace951: BinaryAssociation = BinaryAssociation(
    name="referentTrace951",
    ends={
        Property(name="Values953", type=umlTrace_Kernel_TracedReference, multiplicity=Multiplicity(1, 1)),
        Property(name="Reference_referent_Value952", type=Reference_referent_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureValuesTrace969: BinaryAssociation = BinaryAssociation(
    name="featureValuesTrace969",
    ends={
        Property(name="Values971", type=umlTrace_Kernel_TracedCompoundValue, multiplicity=Multiplicity(1, 1)),
        Property(name="CompoundValue_featureValues_Value970", type=CompoundValue_featureValues_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values_FeatureValueTrace972: BinaryAssociation = BinaryAssociation(
    name="values_FeatureValueTrace972",
    ends={
        Property(name="Values974", type=umlTrace_Kernel_TracedFeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureValue_values_FeatureValue_Value973", type=FeatureValue_values_FeatureValue_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureTrace975: BinaryAssociation = BinaryAssociation(
    name="featureTrace975",
    ends={
        Property(name="Values977", type=umlTrace_Kernel_TracedFeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureValue_feature_Value976", type=FeatureValue_feature_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locus_ExtensionalValueTrace981: BinaryAssociation = BinaryAssociation(
    name="locus_ExtensionalValueTrace981",
    ends={
        Property(name="Values983", type=umlTrace_Kernel_TracedExtensionalValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ExtensionalValue_locus_ExtensionalValue_Value982", type=ExtensionalValue_locus_ExtensionalValue_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values_ParameterValueTrace984: BinaryAssociation = BinaryAssociation(
    name="values_ParameterValueTrace984",
    ends={
        Property(name="Values986", type=umlTrace_BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ParameterValue_values_ParameterValue_Value985", type=ParameterValue_values_ParameterValue_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter_ParameterValueTrace987: BinaryAssociation = BinaryAssociation(
    name="parameter_ParameterValueTrace987",
    ends={
        Property(name="Values989", type=umlTrace_BasicBehaviors_TracedParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ParameterValue_parameter_ParameterValue_Value988", type=ParameterValue_parameter_ParameterValue_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterValuesTrace990: BinaryAssociation = BinaryAssociation(
    name="parameterValuesTrace990",
    ends={
        Property(name="Values992", type=umlTrace_BasicBehaviors_TracedExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="Execution_parameterValues_Value991", type=Execution_parameterValues_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contextTrace993: BinaryAssociation = BinaryAssociation(
    name="contextTrace993",
    ends={
        Property(name="Values995", type=umlTrace_BasicBehaviors_TracedExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="Execution_context_Value994", type=Execution_context_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
positionTrace978: BinaryAssociation = BinaryAssociation(
    name="positionTrace978",
    ends={
        Property(name="Values980", type=umlTrace_Kernel_TracedFeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureValue_position_Value979", type=FeatureValue_position_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
offeredTokenCountTrace1005: BinaryAssociation = BinaryAssociation(
    name="offeredTokenCountTrace1005",
    ends={
        Property(name="Values1007", type=umlTrace_IntermediateActivities_TracedObjectNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjectNodeActivation_offeredTokenCount_Value1006", type=ObjectNodeActivation_offeredTokenCount_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeActivationsTrace1008: BinaryAssociation = BinaryAssociation(
    name="nodeActivationsTrace1008",
    ends={
        Property(name="Values1010", type=umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivationGroup_nodeActivations_Value1009", type=ActivityNodeActivationGroup_nodeActivations_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activityExecutionTrace1011: BinaryAssociation = BinaryAssociation(
    name="activityExecutionTrace1011",
    ends={
        Property(name="Values1013", type=umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivationGroup_activityExecution_Value1012", type=ActivityNodeActivationGroup_activityExecution_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeInstancesTrace1014: BinaryAssociation = BinaryAssociation(
    name="edgeInstancesTrace1014",
    ends={
        Property(name="Values1016", type=umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivationGroup_edgeInstances_Value1015", type=ActivityNodeActivationGroup_edgeInstances_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueTrace1017: BinaryAssociation = BinaryAssociation(
    name="valueTrace1017",
    ends={
        Property(name="Values1019", type=umlTrace_IntermediateActivities_TracedObjectToken, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjectToken_value_Value1018", type=ObjectToken_value_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
remainingOffersCountTrace996: BinaryAssociation = BinaryAssociation(
    name="remainingOffersCountTrace996",
    ends={
        Property(name="Values998", type=umlTrace_IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_remainingOffersCount_Value997", type=ForkedToken_remainingOffersCount_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseTokenTrace999: BinaryAssociation = BinaryAssociation(
    name="baseTokenTrace999",
    ends={
        Property(name="Values1001", type=umlTrace_IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_baseToken_Value1000", type=ForkedToken_baseToken_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseTokenIsWithdrawnTrace1002: BinaryAssociation = BinaryAssociation(
    name="baseTokenIsWithdrawnTrace1002",
    ends={
        Property(name="Values1004", type=umlTrace_IntermediateActivities_TracedForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_baseTokenIsWithdrawn_Value1003", type=ForkedToken_baseTokenIsWithdrawn_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
offeredTokensTrace1023: BinaryAssociation = BinaryAssociation(
    name="offeredTokensTrace1023",
    ends={
        Property(name="Values1025", type=umlTrace_IntermediateActivities_TracedOffer, multiplicity=Multiplicity(1, 1)),
        Property(name="Offer_offeredTokens_Value1024", type=Offer_offeredTokens_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group_ActivityEdgeInstanceTrace1026: BinaryAssociation = BinaryAssociation(
    name="group_ActivityEdgeInstanceTrace1026",
    ends={
        Property(name="Values1028", type=umlTrace_IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdgeInstance_group_ActivityEdgeInstance_Value1027", type=ActivityEdgeInstance_group_ActivityEdgeInstance_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
offersTrace1029: BinaryAssociation = BinaryAssociation(
    name="offersTrace1029",
    ends={
        Property(name="Values1031", type=umlTrace_IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdgeInstance_offers_Value1030", type=ActivityEdgeInstance_offers_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetTrace1032: BinaryAssociation = BinaryAssociation(
    name="targetTrace1032",
    ends={
        Property(name="Values1034", type=umlTrace_IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdgeInstance_target_Value1033", type=ActivityEdgeInstance_target_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge_ActivityEdgeInstanceTrace1035: BinaryAssociation = BinaryAssociation(
    name="edge_ActivityEdgeInstanceTrace1035",
    ends={
        Property(name="Values1037", type=umlTrace_IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdgeInstance_edge_ActivityEdgeInstance_Value1036", type=ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceTrace1038: BinaryAssociation = BinaryAssociation(
    name="sourceTrace1038",
    ends={
        Property(name="Values1040", type=umlTrace_IntermediateActivities_TracedActivityEdgeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdgeInstance_source_Value1039", type=ActivityEdgeInstance_source_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
heldTokensTrace1041: BinaryAssociation = BinaryAssociation(
    name="heldTokensTrace1041",
    ends={
        Property(name="Values1043", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_heldTokens_Value1042", type=ActivityNodeActivation_heldTokens_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node_ActivityNodeActivationTrace1044: BinaryAssociation = BinaryAssociation(
    name="node_ActivityNodeActivationTrace1044",
    ends={
        Property(name="Values1046", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_node_ActivityNodeActivation_Value1045", type=ActivityNodeActivation_node_ActivityNodeActivation_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
runningTrace1047: BinaryAssociation = BinaryAssociation(
    name="runningTrace1047",
    ends={
        Property(name="Values1049", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_running_Value1048", type=ActivityNodeActivation_running_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isRunningTrace1050: BinaryAssociation = BinaryAssociation(
    name="isRunningTrace1050",
    ends={
        Property(name="Values1052", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_isRunning_Value1051", type=ActivityNodeActivation_isRunning_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
holderTrace1020: BinaryAssociation = BinaryAssociation(
    name="holderTrace1020",
    ends={
        Property(name="Values1022", type=umlTrace_IntermediateActivities_TracedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="Token_holder_Value1021", type=Token_holder_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activationGroupTrace1062: BinaryAssociation = BinaryAssociation(
    name="activationGroupTrace1062",
    ends={
        Property(name="Values1064", type=umlTrace_IntermediateActivities_TracedActivityExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityExecution_activationGroup_Value1063", type=ActivityExecution_activationGroup_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
builtInTypesTrace1065: BinaryAssociation = BinaryAssociation(
    name="builtInTypesTrace1065",
    ends={
        Property(name="Values1067", type=umlTrace_Loci_TracedExecutionFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ExecutionFactory_builtInTypes_Value1066", type=ExecutionFactory_builtInTypes_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveBehaviorPrototypesTrace1068: BinaryAssociation = BinaryAssociation(
    name="primitiveBehaviorPrototypesTrace1068",
    ends={
        Property(name="Values1070", type=umlTrace_Loci_TracedExecutionFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ExecutionFactory_primitiveBehaviorPrototypes_Value1069", type=ExecutionFactory_primitiveBehaviorPrototypes_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locus_ExecutionFactoryTrace1071: BinaryAssociation = BinaryAssociation(
    name="locus_ExecutionFactoryTrace1071",
    ends={
        Property(name="Values1073", type=umlTrace_Loci_TracedExecutionFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ExecutionFactory_locus_ExecutionFactory_Value1072", type=ExecutionFactory_locus_ExecutionFactory_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
factoryTrace1074: BinaryAssociation = BinaryAssociation(
    name="factoryTrace1074",
    ends={
        Property(name="Values1076", type=umlTrace_Loci_TracedLocus, multiplicity=Multiplicity(1, 1)),
        Property(name="Locus_factory_Value1075", type=Locus_factory_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionalValuesTrace1077: BinaryAssociation = BinaryAssociation(
    name="extensionalValuesTrace1077",
    ends={
        Property(name="Values1079", type=umlTrace_Loci_TracedLocus, multiplicity=Multiplicity(1, 1)),
        Property(name="Locus_extensionalValues_Value1078", type=Locus_extensionalValues_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executorTrace1080: BinaryAssociation = BinaryAssociation(
    name="executorTrace1080",
    ends={
        Property(name="Values1082", type=umlTrace_Loci_TracedLocus, multiplicity=Multiplicity(1, 1)),
        Property(name="Locus_executor_Value1081", type=Locus_executor_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
runtimeModelElementTrace1083: BinaryAssociation = BinaryAssociation(
    name="runtimeModelElementTrace1083",
    ends={
        Property(name="Values1085", type=umlTrace_Loci_TracedSemanticVisitor, multiplicity=Multiplicity(1, 1)),
        Property(name="SemanticVisitor_runtimeModelElement_Value1084", type=SemanticVisitor_runtimeModelElement_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locus_ExecutorTrace1086: BinaryAssociation = BinaryAssociation(
    name="locus_ExecutorTrace1086",
    ends={
        Property(name="Values1088", type=umlTrace_Loci_TracedExecutor, multiplicity=Multiplicity(1, 1)),
        Property(name="Executor_locus_Executor_Value1087", type=Executor_locus_Executor_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingEdgesTrace1053: BinaryAssociation = BinaryAssociation(
    name="outgoingEdgesTrace1053",
    ends={
        Property(name="Values1055", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_outgoingEdges_Value1054", type=ActivityNodeActivation_outgoingEdges_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingEdgesTrace1056: BinaryAssociation = BinaryAssociation(
    name="incomingEdgesTrace1056",
    ends={
        Property(name="Values1058", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_incomingEdges_Value1057", type=ActivityNodeActivation_incomingEdges_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group_ActivityNodeActivationTrace1059: BinaryAssociation = BinaryAssociation(
    name="group_ActivityNodeActivationTrace1059",
    ends={
        Property(name="Values1061", type=umlTrace_IntermediateActivities_TracedActivityNodeActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNodeActivation_group_ActivityNodeActivation_Value1060", type=ActivityNodeActivation_group_ActivityNodeActivation_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pinActivationsTrace1092: BinaryAssociation = BinaryAssociation(
    name="pinActivationsTrace1092",
    ends={
        Property(name="Values1094", type=umlTrace_BasicActions_TracedActionActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionActivation_pinActivations_Value1093", type=ActionActivation_pinActivations_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firingTrace1095: BinaryAssociation = BinaryAssociation(
    name="firingTrace1095",
    ends={
        Property(name="Values1097", type=umlTrace_BasicActions_TracedActionActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="ActionActivation_firing_Value1096", type=ActionActivation_firing_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locus_ExecutionEnvironmentTrace1089: BinaryAssociation = BinaryAssociation(
    name="locus_ExecutionEnvironmentTrace1089",
    ends={
        Property(name="Values1091", type=umlTrace_Loci_TracedExecutionEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="ExecutionEnvironment_locus_ExecutionEnvironment_Value1090", type=ExecutionEnvironment_locus_ExecutionEnvironment_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionActivationTrace1101: BinaryAssociation = BinaryAssociation(
    name="actionActivationTrace1101",
    ends={
        Property(name="Values1103", type=umlTrace_BasicActions_TracedPinActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="PinActivation_actionActivation_Value1102", type=PinActivation_actionActivation_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
count_tempTrace1104: BinaryAssociation = BinaryAssociation(
    name="count_tempTrace1104",
    ends={
        Property(name="Values1106", type=umlTrace_BasicActions_TracedPinActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="PinActivation_count_temp_Value1105", type=PinActivation_count_temp_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callExecutionsTrace1098: BinaryAssociation = BinaryAssociation(
    name="callExecutionsTrace1098",
    ends={
        Property(name="Values1100", type=umlTrace_BasicActions_TracedCallActionActivation, multiplicity=Multiplicity(1, 1)),
        Property(name="CallActionActivation_callExecutions_Value1099", type=CallActionActivation_callExecutions_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameTrace1107: BinaryAssociation = BinaryAssociation(
    name="nameTrace1107",
    ends={
        Property(name="Values1109", type=umlTrace_Input_TracedInputParameterValues, multiplicity=Multiplicity(1, 1)),
        Property(name="InputParameterValues_name_Value1108", type=InputParameterValues_name_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterValuesTrace1110: BinaryAssociation = BinaryAssociation(
    name="parameterValuesTrace1110",
    ends={
        Property(name="Values1112", type=umlTrace_Input_TracedInputParameterValues, multiplicity=Multiplicity(1, 1)),
        Property(name="InputParameterValues_parameterValues_Value1111", type=InputParameterValues_parameterValues_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contract1113: BinaryAssociation = BinaryAssociation(
    name="contract1113",
    ends={
        Property(name="uml_TracedBehavior", type=umlTrace_uml_TracedConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnector", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 9999))
    }
)
end1114: BinaryAssociation = BinaryAssociation(
    name="end1114",
    ends={
        Property(name="uml_TracedConnectorEnd1116", type=umlTrace_uml_TracedConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnector1115", type=uml_TracedConnectorEnd, multiplicity=Multiplicity(2, 9999))
    }
)
redefinedConnector1117: BinaryAssociation = BinaryAssociation(
    name="redefinedConnector1117",
    ends={
        Property(name="uml_TracedConnector1119", type=umlTrace_uml_TracedConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnector1118", type=uml_TracedConnector, multiplicity=Multiplicity(0, 9999))
    }
)
type1120: BinaryAssociation = BinaryAssociation(
    name="type1120",
    ends={
        Property(name="uml_TracedAssociation1122", type=umlTrace_uml_TracedConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnector1121", type=uml_TracedAssociation, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1123: BinaryAssociation = BinaryAssociation(
    name="originalObject1123",
    ends={
        Property(name="uml_umlTrace_Connector", type=umlTrace_uml_TracedConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnector1124", type=uml_umlTrace_Connector, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute1132: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute1132",
    ends={
        Property(name="uml_TracedProperty1133", type=umlTrace_uml_TracedDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDataType", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
ownedOperation1134: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1134",
    ends={
        Property(name="uml_TracedOperation1136", type=umlTrace_uml_TracedDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDataType1135", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_DataType1137: BinaryAssociation = BinaryAssociation(
    name="originalObject_DataType1137",
    ends={
        Property(name="uml_umlTrace_DataType", type=umlTrace_uml_TracedDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDataType1138", type=uml_umlTrace_DataType, multiplicity=Multiplicity(0, 1))
    }
)
endData1139: BinaryAssociation = BinaryAssociation(
    name="endData1139",
    ends={
        Property(name="uml_TracedLinkEndData1140", type=umlTrace_uml_TracedLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkAction", type=uml_TracedLinkEndData, multiplicity=Multiplicity(2, 9999))
    }
)
inputValue1141: BinaryAssociation = BinaryAssociation(
    name="inputValue1141",
    ends={
        Property(name="uml_TracedInputPin1143", type=umlTrace_uml_TracedLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkAction1142", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 9999))
    }
)
datatype1144: BinaryAssociation = BinaryAssociation(
    name="datatype1144",
    ends={
        Property(name="uml_TracedDataType1145", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty", type=uml_TracedDataType, multiplicity=Multiplicity(0, 1))
    }
)
interface1146: BinaryAssociation = BinaryAssociation(
    name="interface1146",
    ends={
        Property(name="uml_TracedInterface1148", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1147", type=uml_TracedInterface, multiplicity=Multiplicity(0, 1))
    }
)
associationEnd1149: BinaryAssociation = BinaryAssociation(
    name="associationEnd1149",
    ends={
        Property(name="uml_TracedProperty1151", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1150", type=uml_TracedProperty, multiplicity=Multiplicity(0, 1))
    }
)
inputValue1125: BinaryAssociation = BinaryAssociation(
    name="inputValue1125",
    ends={
        Property(name="uml_TracedInputPin1126", type=umlTrace_uml_TracedOpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOpaqueAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999))
    }
)
outputValue1127: BinaryAssociation = BinaryAssociation(
    name="outputValue1127",
    ends={
        Property(name="uml_TracedOutputPin1129", type=umlTrace_uml_TracedOpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOpaqueAction1128", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1130: BinaryAssociation = BinaryAssociation(
    name="originalObject1130",
    ends={
        Property(name="uml_umlTrace_OpaqueAction", type=umlTrace_uml_TracedOpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOpaqueAction1131", type=uml_umlTrace_OpaqueAction, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue1158: BinaryAssociation = BinaryAssociation(
    name="defaultValue1158",
    ends={
        Property(name="umlTrace_uml_TracedProperty1159", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1)),
        Property(name="uml_TracedValueSpecification1160", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1))
    }
)
opposite1161: BinaryAssociation = BinaryAssociation(
    name="opposite1161",
    ends={
        Property(name="uml_TracedProperty1163", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1162", type=uml_TracedProperty, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation1164: BinaryAssociation = BinaryAssociation(
    name="owningAssociation1164",
    ends={
        Property(name="uml_TracedAssociation1166", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1165", type=uml_TracedAssociation, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty1167: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty1167",
    ends={
        Property(name="uml_TracedProperty1169", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1168", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
subsettedProperty1170: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty1170",
    ends={
        Property(name="uml_TracedProperty1172", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1171", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
association1173: BinaryAssociation = BinaryAssociation(
    name="association1173",
    ends={
        Property(name="uml_TracedAssociation1175", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1174", type=uml_TracedAssociation, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_Property1176: BinaryAssociation = BinaryAssociation(
    name="originalObject_Property1176",
    ends={
        Property(name="uml_umlTrace_Property", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1177", type=uml_umlTrace_Property, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1178: BinaryAssociation = BinaryAssociation(
    name="originalObject1178",
    ends={
        Property(name="uml_umlTrace_Continuation", type=umlTrace_uml_TracedContinuation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedContinuation", type=uml_umlTrace_Continuation, multiplicity=Multiplicity(0, 1))
    }
)
removeAt1179: BinaryAssociation = BinaryAssociation(
    name="removeAt1179",
    ends={
        Property(name="uml_TracedInputPin1180", type=umlTrace_uml_TracedRemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRemoveStructuralFeatureValueAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1181: BinaryAssociation = BinaryAssociation(
    name="originalObject1181",
    ends={
        Property(name="uml_umlTrace_RemoveStructuralFeatureValueAction", type=umlTrace_uml_TracedRemoveStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRemoveStructuralFeatureValueAction1182", type=uml_umlTrace_RemoveStructuralFeatureValueAction, multiplicity=Multiplicity(0, 1))
    }
)
qualifier1152: BinaryAssociation = BinaryAssociation(
    name="qualifier1152",
    ends={
        Property(name="uml_TracedProperty1154", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1153", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
class1155: BinaryAssociation = BinaryAssociation(
    name="class1155",
    ends={
        Property(name="uml_TracedClass1157", type=umlTrace_uml_TracedProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProperty1156", type=uml_TracedClass, multiplicity=Multiplicity(0, 1))
    }
)
manifestation1190: BinaryAssociation = BinaryAssociation(
    name="manifestation1190",
    ends={
        Property(name="uml_TracedManifestation1191", type=umlTrace_uml_TracedArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedArtifact", type=uml_TracedManifestation, multiplicity=Multiplicity(0, 9999))
    }
)
nestedArtifact1192: BinaryAssociation = BinaryAssociation(
    name="nestedArtifact1192",
    ends={
        Property(name="uml_TracedArtifact1194", type=umlTrace_uml_TracedArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedArtifact1193", type=uml_TracedArtifact, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute1195: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute1195",
    ends={
        Property(name="uml_TracedProperty1197", type=umlTrace_uml_TracedArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedArtifact1196", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
ownedOperation1198: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1198",
    ends={
        Property(name="uml_TracedOperation1200", type=umlTrace_uml_TracedArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedArtifact1199", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_Artifact1201: BinaryAssociation = BinaryAssociation(
    name="originalObject_Artifact1201",
    ends={
        Property(name="uml_umlTrace_Artifact", type=umlTrace_uml_TracedArtifact, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedArtifact1202", type=uml_umlTrace_Artifact, multiplicity=Multiplicity(0, 1))
    }
)
contract1203: BinaryAssociation = BinaryAssociation(
    name="contract1203",
    ends={
        Property(name="uml_TracedInterface1204", type=umlTrace_uml_TracedInterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterfaceRealization", type=uml_TracedInterface, multiplicity=Multiplicity(1, 1))
    }
)
implementingClassifier1205: BinaryAssociation = BinaryAssociation(
    name="implementingClassifier1205",
    ends={
        Property(name="uml_TracedBehavioredClassifier", type=umlTrace_uml_TracedInterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterfaceRealization1206", type=uml_TracedBehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
signal1183: BinaryAssociation = BinaryAssociation(
    name="signal1183",
    ends={
        Property(name="uml_TracedSignal1184", type=umlTrace_uml_TracedSendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSendSignalAction", type=uml_TracedSignal, multiplicity=Multiplicity(1, 1))
    }
)
target1185: BinaryAssociation = BinaryAssociation(
    name="target1185",
    ends={
        Property(name="uml_TracedInputPin1187", type=umlTrace_uml_TracedSendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSendSignalAction1186", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1188: BinaryAssociation = BinaryAssociation(
    name="originalObject1188",
    ends={
        Property(name="uml_umlTrace_SendSignalAction", type=umlTrace_uml_TracedSendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSendSignalAction1189", type=uml_umlTrace_SendSignalAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1215: BinaryAssociation = BinaryAssociation(
    name="originalObject1215",
    ends={
        Property(name="uml_umlTrace_ActivityFinalNode", type=umlTrace_uml_TracedActivityFinalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityFinalNode", type=uml_umlTrace_ActivityFinalNode, multiplicity=Multiplicity(0, 1))
    }
)
event1216: BinaryAssociation = BinaryAssociation(
    name="event1216",
    ends={
        Property(name="uml_TracedNamedElement", type=umlTrace_uml_TracedDurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDurationObservation", type=uml_TracedNamedElement, multiplicity=Multiplicity(1, 2))
    }
)
originalObject1217: BinaryAssociation = BinaryAssociation(
    name="originalObject1217",
    ends={
        Property(name="uml_umlTrace_DurationObservation", type=umlTrace_uml_TracedDurationObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDurationObservation1218", type=uml_umlTrace_DurationObservation, multiplicity=Multiplicity(0, 1))
    }
)
result1219: BinaryAssociation = BinaryAssociation(
    name="result1219",
    ends={
        Property(name="uml_TracedOutputPin1220", type=umlTrace_uml_TracedAcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAcceptEventAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
trigger1221: BinaryAssociation = BinaryAssociation(
    name="trigger1221",
    ends={
        Property(name="uml_TracedTrigger1223", type=umlTrace_uml_TracedAcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAcceptEventAction1222", type=uml_TracedTrigger, multiplicity=Multiplicity(1, 9999))
    }
)
originalObject_AcceptEventAction1224: BinaryAssociation = BinaryAssociation(
    name="originalObject_AcceptEventAction1224",
    ends={
        Property(name="uml_umlTrace_AcceptEventAction", type=umlTrace_uml_TracedAcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAcceptEventAction1225", type=uml_umlTrace_AcceptEventAction, multiplicity=Multiplicity(0, 1))
    }
)
enumeration1226: BinaryAssociation = BinaryAssociation(
    name="enumeration1226",
    ends={
        Property(name="uml_TracedEnumeration1227", type=umlTrace_uml_TracedEnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedEnumerationLiteral", type=uml_TracedEnumeration, multiplicity=Multiplicity(1, 1))
    }
)
insertAt1228: BinaryAssociation = BinaryAssociation(
    name="insertAt1228",
    ends={
        Property(name="uml_TracedInputPin1229", type=umlTrace_uml_TracedAddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAddStructuralFeatureValueAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1230: BinaryAssociation = BinaryAssociation(
    name="originalObject1230",
    ends={
        Property(name="uml_umlTrace_AddStructuralFeatureValueAction", type=umlTrace_uml_TracedAddStructuralFeatureValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAddStructuralFeatureValueAction1231", type=uml_umlTrace_AddStructuralFeatureValueAction, multiplicity=Multiplicity(0, 1))
    }
)
inState1207: BinaryAssociation = BinaryAssociation(
    name="inState1207",
    ends={
        Property(name="uml_TracedState1208", type=umlTrace_uml_TracedObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedObjectNode", type=uml_TracedState, multiplicity=Multiplicity(0, 9999))
    }
)
selection1209: BinaryAssociation = BinaryAssociation(
    name="selection1209",
    ends={
        Property(name="uml_TracedBehavior1211", type=umlTrace_uml_TracedObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedObjectNode1210", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
upperBound1212: BinaryAssociation = BinaryAssociation(
    name="upperBound1212",
    ends={
        Property(name="uml_TracedValueSpecification1214", type=umlTrace_uml_TracedObjectNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedObjectNode1213", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1234: BinaryAssociation = BinaryAssociation(
    name="originalObject1234",
    ends={
        Property(name="uml_umlTrace_ReadLinkAction", type=umlTrace_uml_TracedReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkAction1235", type=uml_umlTrace_ReadLinkAction, multiplicity=Multiplicity(0, 1))
    }
)
operand1236: BinaryAssociation = BinaryAssociation(
    name="operand1236",
    ends={
        Property(name="uml_TracedValueSpecification1237", type=umlTrace_uml_TracedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpression", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_Expression1238: BinaryAssociation = BinaryAssociation(
    name="originalObject_Expression1238",
    ends={
        Property(name="uml_umlTrace_Expression", type=umlTrace_uml_TracedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpression1239", type=uml_umlTrace_Expression, multiplicity=Multiplicity(0, 1))
    }
)
message1240: BinaryAssociation = BinaryAssociation(
    name="message1240",
    ends={
        Property(name="uml_TracedNamedElement1241", type=umlTrace_uml_TracedConsiderIgnoreFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConsiderIgnoreFragment", type=uml_TracedNamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1242: BinaryAssociation = BinaryAssociation(
    name="originalObject1242",
    ends={
        Property(name="uml_umlTrace_FlowFinalNode", type=umlTrace_uml_TracedFlowFinalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedFlowFinalNode", type=uml_umlTrace_FlowFinalNode, multiplicity=Multiplicity(0, 1))
    }
)
covered1243: BinaryAssociation = BinaryAssociation(
    name="covered1243",
    ends={
        Property(name="uml_TracedLifeline1244", type=umlTrace_uml_TracedInteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionFragment", type=uml_TracedLifeline, multiplicity=Multiplicity(0, 9999))
    }
)
enclosingOperand1245: BinaryAssociation = BinaryAssociation(
    name="enclosingOperand1245",
    ends={
        Property(name="uml_TracedInteractionOperand1247", type=umlTrace_uml_TracedInteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionFragment1246", type=uml_TracedInteractionOperand, multiplicity=Multiplicity(0, 1))
    }
)
enclosingInteraction1248: BinaryAssociation = BinaryAssociation(
    name="enclosingInteraction1248",
    ends={
        Property(name="uml_TracedInteraction1250", type=umlTrace_uml_TracedInteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionFragment1249", type=uml_TracedInteraction, multiplicity=Multiplicity(0, 1))
    }
)
generalOrdering1251: BinaryAssociation = BinaryAssociation(
    name="generalOrdering1251",
    ends={
        Property(name="uml_TracedGeneralOrdering1253", type=umlTrace_uml_TracedInteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionFragment1252", type=uml_TracedGeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
result1232: BinaryAssociation = BinaryAssociation(
    name="result1232",
    ends={
        Property(name="uml_TracedOutputPin1233", type=umlTrace_uml_TracedReadLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
attribute1255: BinaryAssociation = BinaryAssociation(
    name="attribute1255",
    ends={
        Property(name="uml_TracedProperty1257", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1256", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
collaborationUse1258: BinaryAssociation = BinaryAssociation(
    name="collaborationUse1258",
    ends={
        Property(name="uml_TracedCollaborationUse1260", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1259", type=uml_TracedCollaborationUse, multiplicity=Multiplicity(0, 9999))
    }
)
general1261: BinaryAssociation = BinaryAssociation(
    name="general1261",
    ends={
        Property(name="uml_TracedClassifier", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1262", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization1263: BinaryAssociation = BinaryAssociation(
    name="generalization1263",
    ends={
        Property(name="uml_TracedGeneralization1265", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1264", type=uml_TracedGeneralization, multiplicity=Multiplicity(0, 9999))
    }
)
powertypeExtent1266: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent1266",
    ends={
        Property(name="uml_TracedGeneralizationSet1268", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1267", type=uml_TracedGeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember1269: BinaryAssociation = BinaryAssociation(
    name="inheritedMember1269",
    ends={
        Property(name="uml_TracedNamedElement1271", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1270", type=uml_TracedNamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedUseCase1272: BinaryAssociation = BinaryAssociation(
    name="ownedUseCase1272",
    ends={
        Property(name="uml_TracedUseCase1274", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1273", type=uml_TracedUseCase, multiplicity=Multiplicity(0, 9999))
    }
)
useCase1275: BinaryAssociation = BinaryAssociation(
    name="useCase1275",
    ends={
        Property(name="uml_TracedUseCase1277", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1276", type=uml_TracedUseCase, multiplicity=Multiplicity(0, 9999))
    }
)
feature1254: BinaryAssociation = BinaryAssociation(
    name="feature1254",
    ends={
        Property(name="uml_TracedFeature", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier", type=uml_TracedFeature, multiplicity=Multiplicity(0, 9999))
    }
)
substitution1284: BinaryAssociation = BinaryAssociation(
    name="substitution1284",
    ends={
        Property(name="uml_TracedSubstitution1286", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1285", type=uml_TracedSubstitution, multiplicity=Multiplicity(0, 9999))
    }
)
represented1287: BinaryAssociation = BinaryAssociation(
    name="represented1287",
    ends={
        Property(name="uml_TracedClassifier1288", type=umlTrace_uml_TracedInformationItem, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationItem", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1289: BinaryAssociation = BinaryAssociation(
    name="originalObject1289",
    ends={
        Property(name="uml_umlTrace_InformationItem", type=umlTrace_uml_TracedInformationItem, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationItem1290", type=uml_umlTrace_InformationItem, multiplicity=Multiplicity(0, 1))
    }
)
collaborationRole1291: BinaryAssociation = BinaryAssociation(
    name="collaborationRole1291",
    ends={
        Property(name="uml_TracedConnectableElement", type=umlTrace_uml_TracedCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCollaboration", type=uml_TracedConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1292: BinaryAssociation = BinaryAssociation(
    name="originalObject1292",
    ends={
        Property(name="uml_umlTrace_Collaboration", type=umlTrace_uml_TracedCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCollaboration1293", type=uml_umlTrace_Collaboration, multiplicity=Multiplicity(0, 1))
    }
)
message1294: BinaryAssociation = BinaryAssociation(
    name="message1294",
    ends={
        Property(name="uml_TracedMessage1295", type=umlTrace_uml_TracedMessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessageEnd", type=uml_TracedMessage, multiplicity=Multiplicity(0, 1))
    }
)
parameter1296: BinaryAssociation = BinaryAssociation(
    name="parameter1296",
    ends={
        Property(name="uml_TracedTemplateParameter1297", type=umlTrace_uml_TracedTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateSignature", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 9999))
    }
)
template1298: BinaryAssociation = BinaryAssociation(
    name="template1298",
    ends={
        Property(name="uml_TracedTemplateableElement", type=umlTrace_uml_TracedTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateSignature1299", type=uml_TracedTemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
redefinedClassifier1278: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier1278",
    ends={
        Property(name="uml_TracedClassifier1280", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1279", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
representation1281: BinaryAssociation = BinaryAssociation(
    name="representation1281",
    ends={
        Property(name="uml_TracedCollaborationUse1283", type=umlTrace_uml_TracedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifier1282", type=uml_TracedCollaborationUse, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_TemplateSignature1303: BinaryAssociation = BinaryAssociation(
    name="originalObject_TemplateSignature1303",
    ends={
        Property(name="uml_umlTrace_TemplateSignature", type=umlTrace_uml_TracedTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateSignature1304", type=uml_umlTrace_TemplateSignature, multiplicity=Multiplicity(0, 1))
    }
)
signal1305: BinaryAssociation = BinaryAssociation(
    name="signal1305",
    ends={
        Property(name="uml_TracedSignal1306", type=umlTrace_uml_TracedBroadcastSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBroadcastSignalAction", type=uml_TracedSignal, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1307: BinaryAssociation = BinaryAssociation(
    name="originalObject1307",
    ends={
        Property(name="uml_umlTrace_BroadcastSignalAction", type=umlTrace_uml_TracedBroadcastSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBroadcastSignalAction1308", type=uml_umlTrace_BroadcastSignalAction, multiplicity=Multiplicity(0, 1))
    }
)
configuration1309: BinaryAssociation = BinaryAssociation(
    name="configuration1309",
    ends={
        Property(name="uml_TracedDeploymentSpecification1310", type=umlTrace_uml_TracedDeployment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDeployment", type=uml_TracedDeploymentSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
deployedArtifact1311: BinaryAssociation = BinaryAssociation(
    name="deployedArtifact1311",
    ends={
        Property(name="uml_TracedDeployedArtifact", type=umlTrace_uml_TracedDeployment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDeployment1312", type=uml_TracedDeployedArtifact, multiplicity=Multiplicity(0, 9999))
    }
)
location1313: BinaryAssociation = BinaryAssociation(
    name="location1313",
    ends={
        Property(name="uml_TracedDeploymentTarget", type=umlTrace_uml_TracedDeployment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDeployment1314", type=uml_TracedDeploymentTarget, multiplicity=Multiplicity(1, 1))
    }
)
protocol1315: BinaryAssociation = BinaryAssociation(
    name="protocol1315",
    ends={
        Property(name="uml_TracedProtocolStateMachine1316", type=umlTrace_uml_TracedPort, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPort", type=uml_TracedProtocolStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
provided1317: BinaryAssociation = BinaryAssociation(
    name="provided1317",
    ends={
        Property(name="uml_TracedInterface1319", type=umlTrace_uml_TracedPort, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPort1318", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter1300: BinaryAssociation = BinaryAssociation(
    name="ownedParameter1300",
    ends={
        Property(name="uml_TracedTemplateParameter1302", type=umlTrace_uml_TracedTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateSignature1301", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(0, 9999))
    }
)
required1323: BinaryAssociation = BinaryAssociation(
    name="required1323",
    ends={
        Property(name="uml_TracedInterface1325", type=umlTrace_uml_TracedPort, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPort1324", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999))
    }
)
context1326: BinaryAssociation = BinaryAssociation(
    name="context1326",
    ends={
        Property(name="uml_TracedClassifier1327", type=umlTrace_uml_TracedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAction", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 1))
    }
)
input1328: BinaryAssociation = BinaryAssociation(
    name="input1328",
    ends={
        Property(name="uml_TracedInputPin1330", type=umlTrace_uml_TracedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAction1329", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999))
    }
)
localPostcondition1331: BinaryAssociation = BinaryAssociation(
    name="localPostcondition1331",
    ends={
        Property(name="uml_TracedConstraint1333", type=umlTrace_uml_TracedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAction1332", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
localPrecondition1334: BinaryAssociation = BinaryAssociation(
    name="localPrecondition1334",
    ends={
        Property(name="uml_TracedConstraint1336", type=umlTrace_uml_TracedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAction1335", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
output1337: BinaryAssociation = BinaryAssociation(
    name="output1337",
    ends={
        Property(name="uml_TracedOutputPin1339", type=umlTrace_uml_TracedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAction1338", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
metaclass1340: BinaryAssociation = BinaryAssociation(
    name="metaclass1340",
    ends={
        Property(name="uml_TracedClass1341", type=umlTrace_uml_TracedExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtension", type=uml_TracedClass, multiplicity=Multiplicity(1, 1))
    }
)
redefinedPort1320: BinaryAssociation = BinaryAssociation(
    name="redefinedPort1320",
    ends={
        Property(name="uml_TracedPort1322", type=umlTrace_uml_TracedPort, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPort1321", type=uml_TracedPort, multiplicity=Multiplicity(0, 9999))
    }
)
when1347: BinaryAssociation = BinaryAssociation(
    name="when1347",
    ends={
        Property(name="uml_TracedTimeExpression1348", type=umlTrace_uml_TracedTimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeEvent", type=uml_TracedTimeExpression, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1349: BinaryAssociation = BinaryAssociation(
    name="originalObject1349",
    ends={
        Property(name="uml_umlTrace_TimeEvent", type=umlTrace_uml_TracedTimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeEvent1350", type=uml_umlTrace_TimeEvent, multiplicity=Multiplicity(0, 1))
    }
)
package1351: BinaryAssociation = BinaryAssociation(
    name="package1351",
    ends={
        Property(name="uml_TracedPackage1352", type=umlTrace_uml_TracedType, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedType", type=uml_TracedPackage, multiplicity=Multiplicity(0, 1))
    }
)
postCondition1353: BinaryAssociation = BinaryAssociation(
    name="postCondition1353",
    ends={
        Property(name="uml_TracedConstraint1354", type=umlTrace_uml_TracedProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolTransition", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 1))
    }
)
preCondition1355: BinaryAssociation = BinaryAssociation(
    name="preCondition1355",
    ends={
        Property(name="uml_TracedConstraint1357", type=umlTrace_uml_TracedProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolTransition1356", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 1))
    }
)
referred1358: BinaryAssociation = BinaryAssociation(
    name="referred1358",
    ends={
        Property(name="uml_TracedOperation1360", type=umlTrace_uml_TracedProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolTransition1359", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage1361: BinaryAssociation = BinaryAssociation(
    name="nestedPackage1361",
    ends={
        Property(name="uml_TracedPackage1362", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage", type=uml_TracedPackage, multiplicity=Multiplicity(0, 9999))
    }
)
source1342: BinaryAssociation = BinaryAssociation(
    name="source1342",
    ends={
        Property(name="uml_TracedElement1343", type=umlTrace_uml_TracedDirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDirectedRelationship", type=uml_TracedElement, multiplicity=Multiplicity(1, 9999))
    }
)
target1344: BinaryAssociation = BinaryAssociation(
    name="target1344",
    ends={
        Property(name="uml_TracedElement1346", type=umlTrace_uml_TracedDirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDirectedRelationship1345", type=uml_TracedElement, multiplicity=Multiplicity(1, 9999))
    }
)
ownedStereotype1366: BinaryAssociation = BinaryAssociation(
    name="ownedStereotype1366",
    ends={
        Property(name="uml_TracedStereotype1368", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1367", type=uml_TracedStereotype, multiplicity=Multiplicity(0, 9999))
    }
)
ownedType1369: BinaryAssociation = BinaryAssociation(
    name="ownedType1369",
    ends={
        Property(name="uml_TracedType", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1370", type=uml_TracedType, multiplicity=Multiplicity(0, 9999))
    }
)
packageMerge1371: BinaryAssociation = BinaryAssociation(
    name="packageMerge1371",
    ends={
        Property(name="uml_TracedPackageMerge1373", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1372", type=uml_TracedPackageMerge, multiplicity=Multiplicity(0, 9999))
    }
)
packagedElement1374: BinaryAssociation = BinaryAssociation(
    name="packagedElement1374",
    ends={
        Property(name="uml_TracedPackageableElement", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1375", type=uml_TracedPackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
profileApplication1376: BinaryAssociation = BinaryAssociation(
    name="profileApplication1376",
    ends={
        Property(name="uml_TracedProfileApplication1378", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1377", type=uml_TracedProfileApplication, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_Package1379: BinaryAssociation = BinaryAssociation(
    name="originalObject_Package1379",
    ends={
        Property(name="uml_umlTrace_Package", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1380", type=uml_umlTrace_Package, multiplicity=Multiplicity(0, 1))
    }
)
classifierBehavior1381: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior1381",
    ends={
        Property(name="uml_TracedBehavior1382", type=umlTrace_uml_TracedBehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioredClassifier", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
interfaceRealization1383: BinaryAssociation = BinaryAssociation(
    name="interfaceRealization1383",
    ends={
        Property(name="uml_TracedInterfaceRealization1385", type=umlTrace_uml_TracedBehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioredClassifier1384", type=uml_TracedInterfaceRealization, multiplicity=Multiplicity(0, 9999))
    }
)
ownedBehavior1386: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior1386",
    ends={
        Property(name="uml_TracedBehavior1388", type=umlTrace_uml_TracedBehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioredClassifier1387", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage1363: BinaryAssociation = BinaryAssociation(
    name="nestingPackage1363",
    ends={
        Property(name="uml_TracedPackage1365", type=umlTrace_uml_TracedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackage1364", type=uml_TracedPackage, multiplicity=Multiplicity(0, 1))
    }
)
structuralFeature1391: BinaryAssociation = BinaryAssociation(
    name="structuralFeature1391",
    ends={
        Property(name="uml_TracedStructuralFeature1393", type=umlTrace_uml_TracedStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuralFeatureAction1392", type=uml_TracedStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
constrainedElement1394: BinaryAssociation = BinaryAssociation(
    name="constrainedElement1394",
    ends={
        Property(name="uml_TracedElement1395", type=umlTrace_uml_TracedConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConstraint", type=uml_TracedElement, multiplicity=Multiplicity(0, 9999))
    }
)
context1396: BinaryAssociation = BinaryAssociation(
    name="context1396",
    ends={
        Property(name="uml_TracedNamespace", type=umlTrace_uml_TracedConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConstraint1397", type=uml_TracedNamespace, multiplicity=Multiplicity(0, 1))
    }
)
specification1398: BinaryAssociation = BinaryAssociation(
    name="specification1398",
    ends={
        Property(name="uml_TracedValueSpecification1400", type=umlTrace_uml_TracedConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConstraint1399", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject_Constraint1401: BinaryAssociation = BinaryAssociation(
    name="originalObject_Constraint1401",
    ends={
        Property(name="uml_umlTrace_Constraint", type=umlTrace_uml_TracedConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConstraint1402", type=uml_umlTrace_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
lowerValue1403: BinaryAssociation = BinaryAssociation(
    name="lowerValue1403",
    ends={
        Property(name="uml_TracedValueSpecification1404", type=umlTrace_uml_TracedMultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMultiplicityElement", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
upperValue1405: BinaryAssociation = BinaryAssociation(
    name="upperValue1405",
    ends={
        Property(name="uml_TracedValueSpecification1407", type=umlTrace_uml_TracedMultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMultiplicityElement1406", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
object1389: BinaryAssociation = BinaryAssociation(
    name="object1389",
    ends={
        Property(name="uml_TracedInputPin1390", type=umlTrace_uml_TracedStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuralFeatureAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
collection1415: BinaryAssociation = BinaryAssociation(
    name="collection1415",
    ends={
        Property(name="uml_TracedInputPin1416", type=umlTrace_uml_TracedReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReduceAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
reducer1417: BinaryAssociation = BinaryAssociation(
    name="reducer1417",
    ends={
        Property(name="uml_TracedBehavior1419", type=umlTrace_uml_TracedReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReduceAction1418", type=uml_TracedBehavior, multiplicity=Multiplicity(1, 1))
    }
)
result1420: BinaryAssociation = BinaryAssociation(
    name="result1420",
    ends={
        Property(name="uml_TracedOutputPin1422", type=umlTrace_uml_TracedReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReduceAction1421", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1423: BinaryAssociation = BinaryAssociation(
    name="originalObject1423",
    ends={
        Property(name="uml_umlTrace_ReduceAction", type=umlTrace_uml_TracedReduceAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReduceAction1424", type=uml_umlTrace_ReduceAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_InputPin1425: BinaryAssociation = BinaryAssociation(
    name="originalObject_InputPin1425",
    ends={
        Property(name="uml_umlTrace_InputPin", type=umlTrace_uml_TracedInputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInputPin", type=uml_umlTrace_InputPin, multiplicity=Multiplicity(0, 1))
    }
)
executableNode1426: BinaryAssociation = BinaryAssociation(
    name="executableNode1426",
    ends={
        Property(name="uml_TracedExecutableNode", type=umlTrace_uml_TracedSequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSequenceNode", type=uml_TracedExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
featuringClassifier1427: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier1427",
    ends={
        Property(name="uml_TracedClassifier1428", type=umlTrace_uml_TracedFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedFeature", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
maxint1429: BinaryAssociation = BinaryAssociation(
    name="maxint1429",
    ends={
        Property(name="uml_TracedValueSpecification1430", type=umlTrace_uml_TracedInteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionConstraint", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
powertype1408: BinaryAssociation = BinaryAssociation(
    name="powertype1408",
    ends={
        Property(name="uml_TracedClassifier1409", type=umlTrace_uml_TracedGeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralizationSet", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization1410: BinaryAssociation = BinaryAssociation(
    name="generalization1410",
    ends={
        Property(name="uml_TracedGeneralization1412", type=umlTrace_uml_TracedGeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralizationSet1411", type=uml_TracedGeneralization, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1413: BinaryAssociation = BinaryAssociation(
    name="originalObject1413",
    ends={
        Property(name="uml_umlTrace_GeneralizationSet", type=umlTrace_uml_TracedGeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralizationSet1414", type=uml_umlTrace_GeneralizationSet, multiplicity=Multiplicity(0, 1))
    }
)
value1436: BinaryAssociation = BinaryAssociation(
    name="value1436",
    ends={
        Property(name="uml_TracedInputPin1438", type=umlTrace_uml_TracedWriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedWriteStructuralFeatureAction1437", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment1439: BinaryAssociation = BinaryAssociation(
    name="ownedComment1439",
    ends={
        Property(name="uml_TracedComment1440", type=umlTrace_uml_TracedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedElement", type=uml_TracedComment, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElement1441: BinaryAssociation = BinaryAssociation(
    name="ownedElement1441",
    ends={
        Property(name="uml_TracedElement1443", type=umlTrace_uml_TracedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedElement1442", type=uml_TracedElement, multiplicity=Multiplicity(0, 9999))
    }
)
owner1444: BinaryAssociation = BinaryAssociation(
    name="owner1444",
    ends={
        Property(name="uml_TracedElement1446", type=umlTrace_uml_TracedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedElement1445", type=uml_TracedElement, multiplicity=Multiplicity(0, 1))
    }
)
semanticVisitorTrace1447: BinaryAssociation = BinaryAssociation(
    name="semanticVisitorTrace1447",
    ends={
        Property(name="Values1449", type=umlTrace_uml_TracedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Element_semanticVisitor_Value1448", type=Element_semanticVisitor_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizingClassifier1450: BinaryAssociation = BinaryAssociation(
    name="realizingClassifier1450",
    ends={
        Property(name="uml_TracedClassifier1451", type=umlTrace_uml_TracedComponentRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComponentRealization", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 9999))
    }
)
abstraction1452: BinaryAssociation = BinaryAssociation(
    name="abstraction1452",
    ends={
        Property(name="uml_TracedComponent1454", type=umlTrace_uml_TracedComponentRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComponentRealization1453", type=uml_TracedComponent, multiplicity=Multiplicity(0, 1))
    }
)
minint1431: BinaryAssociation = BinaryAssociation(
    name="minint1431",
    ends={
        Property(name="uml_TracedValueSpecification1433", type=umlTrace_uml_TracedInteractionConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionConstraint1432", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
result1434: BinaryAssociation = BinaryAssociation(
    name="result1434",
    ends={
        Property(name="uml_TracedOutputPin1435", type=umlTrace_uml_TracedWriteStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedWriteStructuralFeatureAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 1))
    }
)
owningInstance1460: BinaryAssociation = BinaryAssociation(
    name="owningInstance1460",
    ends={
        Property(name="uml_TracedInstanceSpecification1462", type=umlTrace_uml_TracedSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSlot1461", type=uml_TracedInstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1463: BinaryAssociation = BinaryAssociation(
    name="originalObject1463",
    ends={
        Property(name="uml_umlTrace_Slot", type=umlTrace_uml_TracedSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSlot1464", type=uml_umlTrace_Slot, multiplicity=Multiplicity(0, 1))
    }
)
signal1465: BinaryAssociation = BinaryAssociation(
    name="signal1465",
    ends={
        Property(name="uml_TracedSignal1466", type=umlTrace_uml_TracedSignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSignalEvent", type=uml_TracedSignal, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1467: BinaryAssociation = BinaryAssociation(
    name="originalObject1467",
    ends={
        Property(name="uml_umlTrace_SignalEvent", type=umlTrace_uml_TracedSignalEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSignalEvent1468", type=uml_umlTrace_SignalEvent, multiplicity=Multiplicity(0, 1))
    }
)
useCase1469: BinaryAssociation = BinaryAssociation(
    name="useCase1469",
    ends={
        Property(name="uml_TracedUseCase1470", type=umlTrace_uml_TracedExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtensionPoint", type=uml_TracedUseCase, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1471: BinaryAssociation = BinaryAssociation(
    name="originalObject1471",
    ends={
        Property(name="uml_umlTrace_ExtensionPoint", type=umlTrace_uml_TracedExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtensionPoint1472", type=uml_umlTrace_ExtensionPoint, multiplicity=Multiplicity(0, 1))
    }
)
joinSpec1473: BinaryAssociation = BinaryAssociation(
    name="joinSpec1473",
    ends={
        Property(name="uml_TracedValueSpecification1474", type=umlTrace_uml_TracedJoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedJoinNode", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1475: BinaryAssociation = BinaryAssociation(
    name="originalObject1475",
    ends={
        Property(name="uml_umlTrace_JoinNode", type=umlTrace_uml_TracedJoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedJoinNode1476", type=uml_umlTrace_JoinNode, multiplicity=Multiplicity(0, 1))
    }
)
object1477: BinaryAssociation = BinaryAssociation(
    name="object1477",
    ends={
        Property(name="uml_TracedInputPin1478", type=umlTrace_uml_TracedStartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStartObjectBehaviorAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
definingFeature1455: BinaryAssociation = BinaryAssociation(
    name="definingFeature1455",
    ends={
        Property(name="uml_TracedStructuralFeature1456", type=umlTrace_uml_TracedSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSlot", type=uml_TracedStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value1457: BinaryAssociation = BinaryAssociation(
    name="value1457",
    ends={
        Property(name="uml_TracedValueSpecification1459", type=umlTrace_uml_TracedSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSlot1458", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
importingNamespace1483: BinaryAssociation = BinaryAssociation(
    name="importingNamespace1483",
    ends={
        Property(name="umlTrace_uml_TracedElementImport1484", type=uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_TracedNamespace1485", type=umlTrace_uml_TracedElementImport, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1486: BinaryAssociation = BinaryAssociation(
    name="originalObject1486",
    ends={
        Property(name="uml_umlTrace_ElementImport", type=umlTrace_uml_TracedElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedElementImport1487", type=uml_umlTrace_ElementImport, multiplicity=Multiplicity(0, 1))
    }
)
classifier1488: BinaryAssociation = BinaryAssociation(
    name="classifier1488",
    ends={
        Property(name="uml_TracedClassifier1489", type=umlTrace_uml_TracedCreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCreateObjectAction", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
result1490: BinaryAssociation = BinaryAssociation(
    name="result1490",
    ends={
        Property(name="uml_TracedOutputPin1492", type=umlTrace_uml_TracedCreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCreateObjectAction1491", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1493: BinaryAssociation = BinaryAssociation(
    name="originalObject1493",
    ends={
        Property(name="uml_umlTrace_CreateObjectAction", type=umlTrace_uml_TracedCreateObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCreateObjectAction1494", type=uml_umlTrace_CreateObjectAction, multiplicity=Multiplicity(0, 1))
    }
)
toAfter1495: BinaryAssociation = BinaryAssociation(
    name="toAfter1495",
    ends={
        Property(name="uml_TracedGeneralOrdering1496", type=umlTrace_uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOccurrenceSpecification", type=uml_TracedGeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
toBefore1497: BinaryAssociation = BinaryAssociation(
    name="toBefore1497",
    ends={
        Property(name="uml_TracedGeneralOrdering1499", type=umlTrace_uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOccurrenceSpecification1498", type=uml_TracedGeneralOrdering, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_OccurrenceSpecification1500: BinaryAssociation = BinaryAssociation(
    name="originalObject_OccurrenceSpecification1500",
    ends={
        Property(name="uml_umlTrace_OccurrenceSpecification", type=umlTrace_uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOccurrenceSpecification1501", type=uml_umlTrace_OccurrenceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
owningExpression1502: BinaryAssociation = BinaryAssociation(
    name="owningExpression1502",
    ends={
        Property(name="uml_TracedStringExpression1503", type=umlTrace_uml_TracedStringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStringExpression", type=uml_TracedStringExpression, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1479: BinaryAssociation = BinaryAssociation(
    name="originalObject1479",
    ends={
        Property(name="uml_umlTrace_StartObjectBehaviorAction", type=umlTrace_uml_TracedStartObjectBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStartObjectBehaviorAction1480", type=uml_umlTrace_StartObjectBehaviorAction, multiplicity=Multiplicity(0, 1))
    }
)
importedElement1481: BinaryAssociation = BinaryAssociation(
    name="importedElement1481",
    ends={
        Property(name="uml_TracedPackageableElement1482", type=umlTrace_uml_TracedElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedElementImport", type=uml_TracedPackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
profile1509: BinaryAssociation = BinaryAssociation(
    name="profile1509",
    ends={
        Property(name="uml_TracedProfile1511", type=umlTrace_uml_TracedStereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStereotype1510", type=uml_TracedProfile, multiplicity=Multiplicity(1, 1))
    }
)
nestedClassifier1512: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier1512",
    ends={
        Property(name="uml_TracedClassifier1513", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute1514: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute1514",
    ends={
        Property(name="uml_TracedProperty1516", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface1515", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception1517: BinaryAssociation = BinaryAssociation(
    name="ownedReception1517",
    ends={
        Property(name="uml_TracedReception1519", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface1518", type=uml_TracedReception, multiplicity=Multiplicity(0, 9999))
    }
)
protocol1520: BinaryAssociation = BinaryAssociation(
    name="protocol1520",
    ends={
        Property(name="uml_TracedProtocolStateMachine1522", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface1521", type=uml_TracedProtocolStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
redefinedInterface1523: BinaryAssociation = BinaryAssociation(
    name="redefinedInterface1523",
    ends={
        Property(name="uml_TracedInterface1525", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface1524", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedOperation1526: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1526",
    ends={
        Property(name="uml_TracedOperation1528", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface1527", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1529: BinaryAssociation = BinaryAssociation(
    name="originalObject1529",
    ends={
        Property(name="uml_umlTrace_Interface", type=umlTrace_uml_TracedInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterface1530", type=uml_umlTrace_Interface, multiplicity=Multiplicity(0, 1))
    }
)
clause1531: BinaryAssociation = BinaryAssociation(
    name="clause1531",
    ends={
        Property(name="uml_TracedClause1532", type=umlTrace_uml_TracedConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConditionalNode", type=uml_TracedClause, multiplicity=Multiplicity(1, 9999))
    }
)
subExpression1504: BinaryAssociation = BinaryAssociation(
    name="subExpression1504",
    ends={
        Property(name="uml_TracedStringExpression1506", type=umlTrace_uml_TracedStringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStringExpression1505", type=uml_TracedStringExpression, multiplicity=Multiplicity(0, 9999))
    }
)
icon1507: BinaryAssociation = BinaryAssociation(
    name="icon1507",
    ends={
        Property(name="uml_TracedImage1508", type=umlTrace_uml_TracedStereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStereotype", type=uml_TracedImage, multiplicity=Multiplicity(0, 9999))
    }
)
object1538: BinaryAssociation = BinaryAssociation(
    name="object1538",
    ends={
        Property(name="uml_TracedInputPin1540", type=umlTrace_uml_TracedReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndAction1539", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
result1541: BinaryAssociation = BinaryAssociation(
    name="result1541",
    ends={
        Property(name="uml_TracedOutputPin1543", type=umlTrace_uml_TracedReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndAction1542", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1544: BinaryAssociation = BinaryAssociation(
    name="originalObject1544",
    ends={
        Property(name="uml_umlTrace_ReadLinkObjectEndAction", type=umlTrace_uml_TracedReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndAction1545", type=uml_umlTrace_ReadLinkObjectEndAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1546: BinaryAssociation = BinaryAssociation(
    name="originalObject1546",
    ends={
        Property(name="uml_umlTrace_AnyReceiveEvent", type=umlTrace_uml_TracedAnyReceiveEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAnyReceiveEvent", type=uml_umlTrace_AnyReceiveEvent, multiplicity=Multiplicity(0, 1))
    }
)
clientDependency1547: BinaryAssociation = BinaryAssociation(
    name="clientDependency1547",
    ends={
        Property(name="uml_TracedDependency1548", type=umlTrace_uml_TracedNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamedElement", type=uml_TracedDependency, multiplicity=Multiplicity(0, 9999))
    }
)
nameExpression1549: BinaryAssociation = BinaryAssociation(
    name="nameExpression1549",
    ends={
        Property(name="uml_TracedStringExpression1551", type=umlTrace_uml_TracedNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamedElement1550", type=uml_TracedStringExpression, multiplicity=Multiplicity(0, 1))
    }
)
namespace1552: BinaryAssociation = BinaryAssociation(
    name="namespace1552",
    ends={
        Property(name="uml_TracedNamespace1554", type=umlTrace_uml_TracedNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamedElement1553", type=uml_TracedNamespace, multiplicity=Multiplicity(0, 1))
    }
)
result1533: BinaryAssociation = BinaryAssociation(
    name="result1533",
    ends={
        Property(name="uml_TracedOutputPin1535", type=umlTrace_uml_TracedConditionalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConditionalNode1534", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
end1536: BinaryAssociation = BinaryAssociation(
    name="end1536",
    ends={
        Property(name="uml_TracedProperty1537", type=umlTrace_uml_TracedReadLinkObjectEndAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndAction", type=uml_TracedProperty, multiplicity=Multiplicity(1, 1))
    }
)
required1563: BinaryAssociation = BinaryAssociation(
    name="required1563",
    ends={
        Property(name="uml_TracedInterface1565", type=umlTrace_uml_TracedComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComponent1564", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999))
    }
)
connectionPoint1566: BinaryAssociation = BinaryAssociation(
    name="connectionPoint1566",
    ends={
        Property(name="uml_TracedPseudostate1567", type=umlTrace_uml_TracedStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStateMachine", type=uml_TracedPseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
submachineState1568: BinaryAssociation = BinaryAssociation(
    name="submachineState1568",
    ends={
        Property(name="uml_TracedState1570", type=umlTrace_uml_TracedStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStateMachine1569", type=uml_TracedState, multiplicity=Multiplicity(0, 9999))
    }
)
region1571: BinaryAssociation = BinaryAssociation(
    name="region1571",
    ends={
        Property(name="uml_TracedRegion1573", type=umlTrace_uml_TracedStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStateMachine1572", type=uml_TracedRegion, multiplicity=Multiplicity(1, 9999))
    }
)
extendedStateMachine1574: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine1574",
    ends={
        Property(name="uml_TracedStateMachine1576", type=umlTrace_uml_TracedStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStateMachine1575", type=uml_TracedStateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
lifeline1577: BinaryAssociation = BinaryAssociation(
    name="lifeline1577",
    ends={
        Property(name="uml_TracedLifeline1578", type=umlTrace_uml_TracedInteraction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteraction", type=uml_TracedLifeline, multiplicity=Multiplicity(0, 9999))
    }
)
fragment1579: BinaryAssociation = BinaryAssociation(
    name="fragment1579",
    ends={
        Property(name="uml_TracedInteractionFragment", type=umlTrace_uml_TracedInteraction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteraction1580", type=uml_TracedInteractionFragment, multiplicity=Multiplicity(0, 9999))
    }
)
packagedElement1555: BinaryAssociation = BinaryAssociation(
    name="packagedElement1555",
    ends={
        Property(name="uml_TracedPackageableElement1556", type=umlTrace_uml_TracedComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComponent", type=uml_TracedPackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
provided1557: BinaryAssociation = BinaryAssociation(
    name="provided1557",
    ends={
        Property(name="uml_TracedInterface1559", type=umlTrace_uml_TracedComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComponent1558", type=uml_TracedInterface, multiplicity=Multiplicity(0, 9999))
    }
)
realization1560: BinaryAssociation = BinaryAssociation(
    name="realization1560",
    ends={
        Property(name="uml_TracedComponentRealization1562", type=umlTrace_uml_TracedComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComponent1561", type=uml_TracedComponentRealization, multiplicity=Multiplicity(0, 9999))
    }
)
message1586: BinaryAssociation = BinaryAssociation(
    name="message1586",
    ends={
        Property(name="uml_TracedMessage1588", type=umlTrace_uml_TracedInteraction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteraction1587", type=uml_TracedMessage, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1589: BinaryAssociation = BinaryAssociation(
    name="originalObject1589",
    ends={
        Property(name="uml_umlTrace_LiteralString", type=umlTrace_uml_TracedLiteralString, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLiteralString", type=uml_umlTrace_LiteralString, multiplicity=Multiplicity(0, 1))
    }
)
object1590: BinaryAssociation = BinaryAssociation(
    name="object1590",
    ends={
        Property(name="uml_TracedInputPin1591", type=umlTrace_uml_TracedStartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStartClassifierBehaviorAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1592: BinaryAssociation = BinaryAssociation(
    name="originalObject1592",
    ends={
        Property(name="uml_umlTrace_StartClassifierBehaviorAction", type=umlTrace_uml_TracedStartClassifierBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStartClassifierBehaviorAction1593", type=uml_umlTrace_StartClassifierBehaviorAction, multiplicity=Multiplicity(0, 1))
    }
)
operation1594: BinaryAssociation = BinaryAssociation(
    name="operation1594",
    ends={
        Property(name="uml_TracedOperation1595", type=umlTrace_uml_TracedCallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallEvent", type=uml_TracedOperation, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1596: BinaryAssociation = BinaryAssociation(
    name="originalObject1596",
    ends={
        Property(name="uml_umlTrace_CallEvent", type=umlTrace_uml_TracedCallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallEvent1597", type=uml_umlTrace_CallEvent, multiplicity=Multiplicity(0, 1))
    }
)
relatedElement1598: BinaryAssociation = BinaryAssociation(
    name="relatedElement1598",
    ends={
        Property(name="uml_TracedElement1599", type=umlTrace_uml_TracedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRelationship", type=uml_TracedElement, multiplicity=Multiplicity(1, 9999))
    }
)
action1581: BinaryAssociation = BinaryAssociation(
    name="action1581",
    ends={
        Property(name="uml_TracedAction", type=umlTrace_uml_TracedInteraction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteraction1582", type=uml_TracedAction, multiplicity=Multiplicity(0, 9999))
    }
)
formalGate1583: BinaryAssociation = BinaryAssociation(
    name="formalGate1583",
    ends={
        Property(name="uml_TracedGate1585", type=umlTrace_uml_TracedInteraction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteraction1584", type=uml_TracedGate, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1605: BinaryAssociation = BinaryAssociation(
    name="originalObject1605",
    ends={
        Property(name="uml_umlTrace_SendObjectAction", type=umlTrace_uml_TracedSendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSendObjectAction1606", type=uml_umlTrace_SendObjectAction, multiplicity=Multiplicity(0, 1))
    }
)
decomposedAs1607: BinaryAssociation = BinaryAssociation(
    name="decomposedAs1607",
    ends={
        Property(name="uml_TracedPartDecomposition1608", type=umlTrace_uml_TracedLifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLifeline", type=uml_TracedPartDecomposition, multiplicity=Multiplicity(0, 1))
    }
)
interaction1609: BinaryAssociation = BinaryAssociation(
    name="interaction1609",
    ends={
        Property(name="uml_TracedInteraction1611", type=umlTrace_uml_TracedLifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLifeline1610", type=uml_TracedInteraction, multiplicity=Multiplicity(1, 1))
    }
)
represents1612: BinaryAssociation = BinaryAssociation(
    name="represents1612",
    ends={
        Property(name="uml_TracedConnectableElement1614", type=umlTrace_uml_TracedLifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLifeline1613", type=uml_TracedConnectableElement, multiplicity=Multiplicity(0, 1))
    }
)
selector1615: BinaryAssociation = BinaryAssociation(
    name="selector1615",
    ends={
        Property(name="uml_TracedValueSpecification1617", type=umlTrace_uml_TracedLifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLifeline1616", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
coveredBy1618: BinaryAssociation = BinaryAssociation(
    name="coveredBy1618",
    ends={
        Property(name="uml_TracedInteractionFragment1620", type=umlTrace_uml_TracedLifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLifeline1619", type=uml_TracedInteractionFragment, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1621: BinaryAssociation = BinaryAssociation(
    name="originalObject1621",
    ends={
        Property(name="uml_umlTrace_Lifeline", type=umlTrace_uml_TracedLifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLifeline1622", type=uml_umlTrace_Lifeline, multiplicity=Multiplicity(0, 1))
    }
)
finish1623: BinaryAssociation = BinaryAssociation(
    name="finish1623",
    ends={
        Property(name="uml_TracedOccurrenceSpecification1624", type=umlTrace_uml_TracedExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExecutionSpecification", type=uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
start1625: BinaryAssociation = BinaryAssociation(
    name="start1625",
    ends={
        Property(name="uml_TracedOccurrenceSpecification1627", type=umlTrace_uml_TracedExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExecutionSpecification1626", type=uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
event1628: BinaryAssociation = BinaryAssociation(
    name="event1628",
    ends={
        Property(name="uml_TracedNamedElement1629", type=umlTrace_uml_TracedTimeObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeObservation", type=uml_TracedNamedElement, multiplicity=Multiplicity(1, 1))
    }
)
request1600: BinaryAssociation = BinaryAssociation(
    name="request1600",
    ends={
        Property(name="uml_TracedInputPin1601", type=umlTrace_uml_TracedSendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSendObjectAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
target1602: BinaryAssociation = BinaryAssociation(
    name="target1602",
    ends={
        Property(name="uml_TracedInputPin1604", type=umlTrace_uml_TracedSendObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSendObjectAction1603", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
outputElement1634: BinaryAssociation = BinaryAssociation(
    name="outputElement1634",
    ends={
        Property(name="uml_TracedExpansionNode1635", type=umlTrace_uml_TracedExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpansionRegion", type=uml_TracedExpansionNode, multiplicity=Multiplicity(0, 9999))
    }
)
inputElement1636: BinaryAssociation = BinaryAssociation(
    name="inputElement1636",
    ends={
        Property(name="uml_TracedExpansionNode1638", type=umlTrace_uml_TracedExpansionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpansionRegion1637", type=uml_TracedExpansionNode, multiplicity=Multiplicity(1, 9999))
    }
)
value1639: BinaryAssociation = BinaryAssociation(
    name="value1639",
    ends={
        Property(name="uml_TracedInputPin1640", type=umlTrace_uml_TracedWriteVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedWriteVariableAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
bodyOutput1641: BinaryAssociation = BinaryAssociation(
    name="bodyOutput1641",
    ends={
        Property(name="uml_TracedOutputPin1642", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
bodyPart1643: BinaryAssociation = BinaryAssociation(
    name="bodyPart1643",
    ends={
        Property(name="uml_TracedExecutableNode1645", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1644", type=uml_TracedExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
decider1646: BinaryAssociation = BinaryAssociation(
    name="decider1646",
    ends={
        Property(name="uml_TracedOutputPin1648", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1647", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
loopVariable1649: BinaryAssociation = BinaryAssociation(
    name="loopVariable1649",
    ends={
        Property(name="uml_TracedOutputPin1651", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1650", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
loopVariableInput1652: BinaryAssociation = BinaryAssociation(
    name="loopVariableInput1652",
    ends={
        Property(name="uml_TracedInputPin1654", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1653", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1630: BinaryAssociation = BinaryAssociation(
    name="originalObject1630",
    ends={
        Property(name="uml_umlTrace_TimeObservation", type=umlTrace_uml_TracedTimeObservation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeObservation1631", type=uml_umlTrace_TimeObservation, multiplicity=Multiplicity(0, 1))
    }
)
result1632: BinaryAssociation = BinaryAssociation(
    name="result1632",
    ends={
        Property(name="uml_TracedOutputPin1633", type=umlTrace_uml_TracedCreateLinkObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCreateLinkObjectAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
setupPart1658: BinaryAssociation = BinaryAssociation(
    name="setupPart1658",
    ends={
        Property(name="uml_TracedExecutableNode1660", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1659", type=uml_TracedExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
test1661: BinaryAssociation = BinaryAssociation(
    name="test1661",
    ends={
        Property(name="uml_TracedExecutableNode1663", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1662", type=uml_TracedExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
generalMachine1664: BinaryAssociation = BinaryAssociation(
    name="generalMachine1664",
    ends={
        Property(name="uml_TracedProtocolStateMachine1665", type=umlTrace_uml_TracedProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolConformance", type=uml_TracedProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
specificMachine1666: BinaryAssociation = BinaryAssociation(
    name="specificMachine1666",
    ends={
        Property(name="uml_TracedProtocolStateMachine1668", type=umlTrace_uml_TracedProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolConformance1667", type=uml_TracedProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1669: BinaryAssociation = BinaryAssociation(
    name="originalObject1669",
    ends={
        Property(name="uml_umlTrace_ProtocolConformance", type=umlTrace_uml_TracedProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolConformance1670", type=uml_umlTrace_ProtocolConformance, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiteral1671: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral1671",
    ends={
        Property(name="uml_TracedEnumerationLiteral1672", type=umlTrace_uml_TracedEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedEnumeration", type=uml_TracedEnumerationLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
result1655: BinaryAssociation = BinaryAssociation(
    name="result1655",
    ends={
        Property(name="uml_TracedOutputPin1657", type=umlTrace_uml_TracedLoopNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLoopNode1656", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
node1680: BinaryAssociation = BinaryAssociation(
    name="node1680",
    ends={
        Property(name="uml_TracedActivityNode1681", type=umlTrace_uml_TracedActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityPartition", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
represents1682: BinaryAssociation = BinaryAssociation(
    name="represents1682",
    ends={
        Property(name="uml_TracedElement1684", type=umlTrace_uml_TracedActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityPartition1683", type=uml_TracedElement, multiplicity=Multiplicity(0, 1))
    }
)
subpartition1685: BinaryAssociation = BinaryAssociation(
    name="subpartition1685",
    ends={
        Property(name="uml_TracedActivityPartition1687", type=umlTrace_uml_TracedActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityPartition1686", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
superPartition1688: BinaryAssociation = BinaryAssociation(
    name="superPartition1688",
    ends={
        Property(name="uml_TracedActivityPartition1690", type=umlTrace_uml_TracedActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityPartition1689", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
edge1691: BinaryAssociation = BinaryAssociation(
    name="edge1691",
    ends={
        Property(name="uml_TracedActivityEdge1693", type=umlTrace_uml_TracedActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityPartition1692", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1694: BinaryAssociation = BinaryAssociation(
    name="originalObject1694",
    ends={
        Property(name="uml_umlTrace_ActivityPartition", type=umlTrace_uml_TracedActivityPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityPartition1695", type=uml_umlTrace_ActivityPartition, multiplicity=Multiplicity(0, 1))
    }
)
variable1696: BinaryAssociation = BinaryAssociation(
    name="variable1696",
    ends={
        Property(name="uml_TracedVariable1697", type=umlTrace_uml_TracedVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVariableAction", type=uml_TracedVariable, multiplicity=Multiplicity(1, 1))
    }
)
destroyAt1698: BinaryAssociation = BinaryAssociation(
    name="destroyAt1698",
    ends={
        Property(name="uml_TracedInputPin1699", type=umlTrace_uml_TracedLinkEndDestructionData, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkEndDestructionData", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
roleBinding1673: BinaryAssociation = BinaryAssociation(
    name="roleBinding1673",
    ends={
        Property(name="uml_TracedDependency1674", type=umlTrace_uml_TracedCollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCollaborationUse", type=uml_TracedDependency, multiplicity=Multiplicity(0, 9999))
    }
)
type1675: BinaryAssociation = BinaryAssociation(
    name="type1675",
    ends={
        Property(name="uml_TracedCollaboration1677", type=umlTrace_uml_TracedCollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCollaborationUse1676", type=uml_TracedCollaboration, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1678: BinaryAssociation = BinaryAssociation(
    name="originalObject1678",
    ends={
        Property(name="uml_umlTrace_CollaborationUse", type=umlTrace_uml_TracedCollaborationUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCollaborationUse1679", type=uml_umlTrace_CollaborationUse, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1705: BinaryAssociation = BinaryAssociation(
    name="originalObject1705",
    ends={
        Property(name="uml_umlTrace_Include", type=umlTrace_uml_TracedInclude, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInclude1706", type=uml_umlTrace_Include, multiplicity=Multiplicity(0, 1))
    }
)
activity1707: BinaryAssociation = BinaryAssociation(
    name="activity1707",
    ends={
        Property(name="uml_TracedActivity1708", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode", type=uml_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
inGroup1709: BinaryAssociation = BinaryAssociation(
    name="inGroup1709",
    ends={
        Property(name="uml_TracedActivityGroup", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1710", type=uml_TracedActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
inInterruptibleRegion1711: BinaryAssociation = BinaryAssociation(
    name="inInterruptibleRegion1711",
    ends={
        Property(name="uml_TracedInterruptibleActivityRegion1713", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1712", type=uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(0, 9999))
    }
)
inStructuredNode1714: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode1714",
    ends={
        Property(name="uml_TracedStructuredActivityNode1716", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1715", type=uml_TracedStructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
incoming1717: BinaryAssociation = BinaryAssociation(
    name="incoming1717",
    ends={
        Property(name="uml_TracedActivityEdge1719", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1718", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing1720: BinaryAssociation = BinaryAssociation(
    name="outgoing1720",
    ends={
        Property(name="uml_TracedActivityEdge1722", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1721", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedNode1723: BinaryAssociation = BinaryAssociation(
    name="redefinedNode1723",
    ends={
        Property(name="uml_TracedActivityNode1725", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1724", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
addition1700: BinaryAssociation = BinaryAssociation(
    name="addition1700",
    ends={
        Property(name="uml_TracedUseCase1701", type=umlTrace_uml_TracedInclude, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInclude", type=uml_TracedUseCase, multiplicity=Multiplicity(1, 1))
    }
)
includingCase1702: BinaryAssociation = BinaryAssociation(
    name="includingCase1702",
    ends={
        Property(name="uml_TracedUseCase1704", type=umlTrace_uml_TracedInclude, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInclude1703", type=uml_TracedUseCase, multiplicity=Multiplicity(1, 1))
    }
)
connection1729: BinaryAssociation = BinaryAssociation(
    name="connection1729",
    ends={
        Property(name="uml_TracedConnectionPointReference1730", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState", type=uml_TracedConnectionPointReference, multiplicity=Multiplicity(0, 9999))
    }
)
connectionPoint1731: BinaryAssociation = BinaryAssociation(
    name="connectionPoint1731",
    ends={
        Property(name="uml_TracedPseudostate1733", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1732", type=uml_TracedPseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
deferrableTrigger1734: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger1734",
    ends={
        Property(name="uml_TracedTrigger1736", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1735", type=uml_TracedTrigger, multiplicity=Multiplicity(0, 9999))
    }
)
doActivity1737: BinaryAssociation = BinaryAssociation(
    name="doActivity1737",
    ends={
        Property(name="uml_TracedBehavior1739", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1738", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
entry1740: BinaryAssociation = BinaryAssociation(
    name="entry1740",
    ends={
        Property(name="uml_TracedBehavior1742", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1741", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
exit1743: BinaryAssociation = BinaryAssociation(
    name="exit1743",
    ends={
        Property(name="uml_TracedBehavior1745", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1744", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
redefinedState1746: BinaryAssociation = BinaryAssociation(
    name="redefinedState1746",
    ends={
        Property(name="uml_TracedState1748", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1747", type=uml_TracedState, multiplicity=Multiplicity(0, 1))
    }
)
stateInvariant1749: BinaryAssociation = BinaryAssociation(
    name="stateInvariant1749",
    ends={
        Property(name="uml_TracedConstraint1751", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1750", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 1))
    }
)
submachine1752: BinaryAssociation = BinaryAssociation(
    name="submachine1752",
    ends={
        Property(name="uml_TracedStateMachine1754", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1753", type=uml_TracedStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
inPartition1726: BinaryAssociation = BinaryAssociation(
    name="inPartition1726",
    ends={
        Property(name="uml_TracedActivityPartition1728", type=umlTrace_uml_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityNode1727", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
result1760: BinaryAssociation = BinaryAssociation(
    name="result1760",
    ends={
        Property(name="uml_TracedOutputPin1761", type=umlTrace_uml_TracedCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
templateBinding1762: BinaryAssociation = BinaryAssociation(
    name="templateBinding1762",
    ends={
        Property(name="uml_TracedTemplateBinding1763", type=umlTrace_uml_TracedTemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateableElement", type=uml_TracedTemplateBinding, multiplicity=Multiplicity(0, 9999))
    }
)
ownedTemplateSignature1764: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateSignature1764",
    ends={
        Property(name="uml_TracedTemplateSignature1766", type=umlTrace_uml_TracedTemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateableElement1765", type=uml_TracedTemplateSignature, multiplicity=Multiplicity(0, 1))
    }
)
specification1767: BinaryAssociation = BinaryAssociation(
    name="specification1767",
    ends={
        Property(name="uml_TracedBehavioralFeature", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior", type=uml_TracedBehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
context1768: BinaryAssociation = BinaryAssociation(
    name="context1768",
    ends={
        Property(name="uml_TracedBehavioredClassifier1770", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior1769", type=uml_TracedBehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter1771: BinaryAssociation = BinaryAssociation(
    name="ownedParameter1771",
    ends={
        Property(name="uml_TracedParameter1773", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior1772", type=uml_TracedParameter, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameterSet1774: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet1774",
    ends={
        Property(name="uml_TracedParameterSet1776", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior1775", type=uml_TracedParameterSet, multiplicity=Multiplicity(0, 9999))
    }
)
postcondition1777: BinaryAssociation = BinaryAssociation(
    name="postcondition1777",
    ends={
        Property(name="uml_TracedConstraint1779", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior1778", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
region1755: BinaryAssociation = BinaryAssociation(
    name="region1755",
    ends={
        Property(name="uml_TracedRegion1757", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1756", type=uml_TracedRegion, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_State1758: BinaryAssociation = BinaryAssociation(
    name="originalObject_State1758",
    ends={
        Property(name="uml_umlTrace_State", type=umlTrace_uml_TracedState, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedState1759", type=uml_umlTrace_State, multiplicity=Multiplicity(0, 1))
    }
)
constrainingClassifier1786: BinaryAssociation = BinaryAssociation(
    name="constrainingClassifier1786",
    ends={
        Property(name="uml_TracedClassifier1787", type=umlTrace_uml_TracedClassifierTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClassifierTemplateParameter", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
parameter1788: BinaryAssociation = BinaryAssociation(
    name="parameter1788",
    ends={
        Property(name="uml_TracedParameter1789", type=umlTrace_uml_TracedActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityParameterNode", type=uml_TracedParameter, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1790: BinaryAssociation = BinaryAssociation(
    name="originalObject1790",
    ends={
        Property(name="uml_umlTrace_ActivityParameterNode", type=umlTrace_uml_TracedActivityParameterNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityParameterNode1791", type=uml_umlTrace_ActivityParameterNode, multiplicity=Multiplicity(0, 1))
    }
)
condition1792: BinaryAssociation = BinaryAssociation(
    name="condition1792",
    ends={
        Property(name="uml_TracedConstraint1793", type=umlTrace_uml_TracedParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameterSet", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
parameter1794: BinaryAssociation = BinaryAssociation(
    name="parameter1794",
    ends={
        Property(name="uml_TracedParameter1796", type=umlTrace_uml_TracedParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameterSet1795", type=uml_TracedParameter, multiplicity=Multiplicity(1, 9999))
    }
)
originalObject1797: BinaryAssociation = BinaryAssociation(
    name="originalObject1797",
    ends={
        Property(name="uml_umlTrace_ParameterSet", type=umlTrace_uml_TracedParameterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameterSet1798", type=uml_umlTrace_ParameterSet, multiplicity=Multiplicity(0, 1))
    }
)
expr1799: BinaryAssociation = BinaryAssociation(
    name="expr1799",
    ends={
        Property(name="uml_TracedValueSpecification1800", type=umlTrace_uml_TracedDuration, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDuration", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
observation1801: BinaryAssociation = BinaryAssociation(
    name="observation1801",
    ends={
        Property(name="uml_TracedObservation", type=umlTrace_uml_TracedDuration, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDuration1802", type=uml_TracedObservation, multiplicity=Multiplicity(0, 9999))
    }
)
precondition1780: BinaryAssociation = BinaryAssociation(
    name="precondition1780",
    ends={
        Property(name="uml_TracedConstraint1782", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior1781", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedBehavior1783: BinaryAssociation = BinaryAssociation(
    name="redefinedBehavior1783",
    ends={
        Property(name="uml_TracedBehavior1785", type=umlTrace_uml_TracedBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavior1784", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 9999))
    }
)
extension1807: BinaryAssociation = BinaryAssociation(
    name="extension1807",
    ends={
        Property(name="uml_TracedExtension1809", type=umlTrace_uml_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClass1808", type=uml_TracedExtension, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier1810: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier1810",
    ends={
        Property(name="uml_TracedClassifier1812", type=umlTrace_uml_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClass1811", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
ownedReception1813: BinaryAssociation = BinaryAssociation(
    name="ownedReception1813",
    ends={
        Property(name="uml_TracedReception1815", type=umlTrace_uml_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClass1814", type=uml_TracedReception, multiplicity=Multiplicity(0, 9999))
    }
)
superClass1816: BinaryAssociation = BinaryAssociation(
    name="superClass1816",
    ends={
        Property(name="uml_TracedClass1818", type=umlTrace_uml_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClass1817", type=uml_TracedClass, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_Class1819: BinaryAssociation = BinaryAssociation(
    name="originalObject_Class1819",
    ends={
        Property(name="uml_umlTrace_Class", type=umlTrace_uml_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClass1820", type=uml_umlTrace_Class, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1821: BinaryAssociation = BinaryAssociation(
    name="originalObject1821",
    ends={
        Property(name="uml_umlTrace_LiteralUnlimitedNatural", type=umlTrace_uml_TracedLiteralUnlimitedNatural, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLiteralUnlimitedNatural", type=uml_umlTrace_LiteralUnlimitedNatural, multiplicity=Multiplicity(0, 1))
    }
)
edge1822: BinaryAssociation = BinaryAssociation(
    name="edge1822",
    ends={
        Property(name="uml_TracedActivityEdge1823", type=umlTrace_uml_TracedStructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredActivityNode", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1803: BinaryAssociation = BinaryAssociation(
    name="originalObject1803",
    ends={
        Property(name="uml_umlTrace_Duration", type=umlTrace_uml_TracedDuration, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDuration1804", type=uml_umlTrace_Duration, multiplicity=Multiplicity(0, 1))
    }
)
ownedOperation1805: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1805",
    ends={
        Property(name="uml_TracedOperation1806", type=umlTrace_uml_TracedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClass", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999))
    }
)
variable1830: BinaryAssociation = BinaryAssociation(
    name="variable1830",
    ends={
        Property(name="uml_TracedVariable1832", type=umlTrace_uml_TracedStructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredActivityNode1831", type=uml_TracedVariable, multiplicity=Multiplicity(0, 9999))
    }
)
node1833: BinaryAssociation = BinaryAssociation(
    name="node1833",
    ends={
        Property(name="uml_TracedActivityNode1835", type=umlTrace_uml_TracedStructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredActivityNode1834", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_StructuredActivityNode1836: BinaryAssociation = BinaryAssociation(
    name="originalObject_StructuredActivityNode1836",
    ends={
        Property(name="uml_umlTrace_StructuredActivityNode", type=umlTrace_uml_TracedStructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredActivityNode1837", type=uml_umlTrace_StructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
mapping1838: BinaryAssociation = BinaryAssociation(
    name="mapping1838",
    ends={
        Property(name="uml_TracedOpaqueExpression1839", type=umlTrace_uml_TracedAbstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAbstraction", type=uml_TracedOpaqueExpression, multiplicity=Multiplicity(0, 1))
    }
)
result1840: BinaryAssociation = BinaryAssociation(
    name="result1840",
    ends={
        Property(name="uml_TracedOutputPin1841", type=umlTrace_uml_TracedReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadStructuralFeatureAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1842: BinaryAssociation = BinaryAssociation(
    name="originalObject1842",
    ends={
        Property(name="uml_umlTrace_ReadStructuralFeatureAction", type=umlTrace_uml_TracedReadStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadStructuralFeatureAction1843", type=uml_umlTrace_ReadStructuralFeatureAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1844: BinaryAssociation = BinaryAssociation(
    name="originalObject1844",
    ends={
        Property(name="uml_umlTrace_MergeNode", type=umlTrace_uml_TracedMergeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMergeNode", type=uml_umlTrace_MergeNode, multiplicity=Multiplicity(0, 1))
    }
)
extendedSignature1845: BinaryAssociation = BinaryAssociation(
    name="extendedSignature1845",
    ends={
        Property(name="uml_TracedRedefinableTemplateSignature1846", type=umlTrace_uml_TracedRedefinableTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRedefinableTemplateSignature", type=uml_TracedRedefinableTemplateSignature, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNodeInput1824: BinaryAssociation = BinaryAssociation(
    name="structuredNodeInput1824",
    ends={
        Property(name="uml_TracedInputPin1826", type=umlTrace_uml_TracedStructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredActivityNode1825", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNodeOutput1827: BinaryAssociation = BinaryAssociation(
    name="structuredNodeOutput1827",
    ends={
        Property(name="uml_TracedOutputPin1829", type=umlTrace_uml_TracedStructuredActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredActivityNode1828", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
classifier1850: BinaryAssociation = BinaryAssociation(
    name="classifier1850",
    ends={
        Property(name="uml_TracedClassifier1852", type=umlTrace_uml_TracedRedefinableTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRedefinableTemplateSignature1851", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
originalObject_CreateLinkAction1853: BinaryAssociation = BinaryAssociation(
    name="originalObject_CreateLinkAction1853",
    ends={
        Property(name="uml_umlTrace_CreateLinkAction", type=umlTrace_uml_TracedCreateLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCreateLinkAction", type=uml_umlTrace_CreateLinkAction, multiplicity=Multiplicity(0, 1))
    }
)
general1854: BinaryAssociation = BinaryAssociation(
    name="general1854",
    ends={
        Property(name="uml_TracedClassifier1855", type=umlTrace_uml_TracedGeneralization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralization", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet1856: BinaryAssociation = BinaryAssociation(
    name="generalizationSet1856",
    ends={
        Property(name="uml_TracedGeneralizationSet1858", type=umlTrace_uml_TracedGeneralization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralization1857", type=uml_TracedGeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
specific1859: BinaryAssociation = BinaryAssociation(
    name="specific1859",
    ends={
        Property(name="uml_TracedClassifier1861", type=umlTrace_uml_TracedGeneralization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralization1860", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1862: BinaryAssociation = BinaryAssociation(
    name="originalObject1862",
    ends={
        Property(name="uml_umlTrace_Generalization", type=umlTrace_uml_TracedGeneralization, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralization1863", type=uml_umlTrace_Generalization, multiplicity=Multiplicity(0, 1))
    }
)
type1864: BinaryAssociation = BinaryAssociation(
    name="type1864",
    ends={
        Property(name="uml_TracedType1865", type=umlTrace_uml_TracedTypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTypedElement", type=uml_TracedType, multiplicity=Multiplicity(0, 1))
    }
)
inheritedParameter1847: BinaryAssociation = BinaryAssociation(
    name="inheritedParameter1847",
    ends={
        Property(name="uml_TracedTemplateParameter1849", type=umlTrace_uml_TracedRedefinableTemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRedefinableTemplateSignature1848", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(0, 9999))
    }
)
result1871: BinaryAssociation = BinaryAssociation(
    name="result1871",
    ends={
        Property(name="uml_TracedOutputPin1873", type=umlTrace_uml_TracedReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndQualifierAction1872", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1874: BinaryAssociation = BinaryAssociation(
    name="originalObject1874",
    ends={
        Property(name="uml_umlTrace_ReadLinkObjectEndQualifierAction", type=umlTrace_uml_TracedReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndQualifierAction1875", type=uml_umlTrace_ReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(0, 1))
    }
)
actual1876: BinaryAssociation = BinaryAssociation(
    name="actual1876",
    ends={
        Property(name="uml_TracedParameterableElement", type=umlTrace_uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameterSubstitution", type=uml_TracedParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
formal1877: BinaryAssociation = BinaryAssociation(
    name="formal1877",
    ends={
        Property(name="uml_TracedTemplateParameter1879", type=umlTrace_uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameterSubstitution1878", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1))
    }
)
ownedActual1880: BinaryAssociation = BinaryAssociation(
    name="ownedActual1880",
    ends={
        Property(name="uml_TracedParameterableElement1882", type=umlTrace_uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameterSubstitution1881", type=uml_TracedParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
templateBinding1883: BinaryAssociation = BinaryAssociation(
    name="templateBinding1883",
    ends={
        Property(name="uml_TracedTemplateBinding1885", type=umlTrace_uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameterSubstitution1884", type=uml_TracedTemplateBinding, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1886: BinaryAssociation = BinaryAssociation(
    name="originalObject1886",
    ends={
        Property(name="uml_umlTrace_TemplateParameterSubstitution", type=umlTrace_uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameterSubstitution1887", type=uml_umlTrace_TemplateParameterSubstitution, multiplicity=Multiplicity(0, 1))
    }
)
condition1888: BinaryAssociation = BinaryAssociation(
    name="condition1888",
    ends={
        Property(name="uml_TracedConstraint1889", type=umlTrace_uml_TracedExtend, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtend", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 1))
    }
)
extendedCase1890: BinaryAssociation = BinaryAssociation(
    name="extendedCase1890",
    ends={
        Property(name="uml_TracedUseCase1892", type=umlTrace_uml_TracedExtend, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtend1891", type=uml_TracedUseCase, multiplicity=Multiplicity(1, 1))
    }
)
object1866: BinaryAssociation = BinaryAssociation(
    name="object1866",
    ends={
        Property(name="uml_TracedInputPin1867", type=umlTrace_uml_TracedReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndQualifierAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
qualifier1868: BinaryAssociation = BinaryAssociation(
    name="qualifier1868",
    ends={
        Property(name="uml_TracedProperty1870", type=umlTrace_uml_TracedReadLinkObjectEndQualifierAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadLinkObjectEndQualifierAction1869", type=uml_TracedProperty, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1899: BinaryAssociation = BinaryAssociation(
    name="originalObject1899",
    ends={
        Property(name="uml_umlTrace_Extend", type=umlTrace_uml_TracedExtend, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtend1900", type=uml_umlTrace_Extend, multiplicity=Multiplicity(0, 1))
    }
)
result1901: BinaryAssociation = BinaryAssociation(
    name="result1901",
    ends={
        Property(name="uml_TracedOutputPin1902", type=umlTrace_uml_TracedReadVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadVariableAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1903: BinaryAssociation = BinaryAssociation(
    name="originalObject1903",
    ends={
        Property(name="uml_umlTrace_ReadVariableAction", type=umlTrace_uml_TracedReadVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadVariableAction1904", type=uml_umlTrace_ReadVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
argument1905: BinaryAssociation = BinaryAssociation(
    name="argument1905",
    ends={
        Property(name="uml_TracedValueSpecification1906", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
connector1907: BinaryAssociation = BinaryAssociation(
    name="connector1907",
    ends={
        Property(name="uml_TracedConnector1909", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage1908", type=uml_TracedConnector, multiplicity=Multiplicity(0, 1))
    }
)
interaction1910: BinaryAssociation = BinaryAssociation(
    name="interaction1910",
    ends={
        Property(name="uml_TracedInteraction1912", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage1911", type=uml_TracedInteraction, multiplicity=Multiplicity(1, 1))
    }
)
receiveEvent1913: BinaryAssociation = BinaryAssociation(
    name="receiveEvent1913",
    ends={
        Property(name="uml_TracedMessageEnd", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage1914", type=uml_TracedMessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
sendEvent1915: BinaryAssociation = BinaryAssociation(
    name="sendEvent1915",
    ends={
        Property(name="uml_TracedMessageEnd1917", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage1916", type=uml_TracedMessageEnd, multiplicity=Multiplicity(0, 1))
    }
)
extensionLocation1893: BinaryAssociation = BinaryAssociation(
    name="extensionLocation1893",
    ends={
        Property(name="uml_TracedExtensionPoint1895", type=umlTrace_uml_TracedExtend, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtend1894", type=uml_TracedExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
extension1896: BinaryAssociation = BinaryAssociation(
    name="extension1896",
    ends={
        Property(name="uml_TracedUseCase1898", type=umlTrace_uml_TracedExtend, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExtend1897", type=uml_TracedUseCase, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1923: BinaryAssociation = BinaryAssociation(
    name="originalObject1923",
    ends={
        Property(name="uml_umlTrace_LiteralBoolean", type=umlTrace_uml_TracedLiteralBoolean, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLiteralBoolean", type=uml_umlTrace_LiteralBoolean, multiplicity=Multiplicity(0, 1))
    }
)
qualifier1924: BinaryAssociation = BinaryAssociation(
    name="qualifier1924",
    ends={
        Property(name="uml_TracedProperty1925", type=umlTrace_uml_TracedQualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedQualifierValue", type=uml_TracedProperty, multiplicity=Multiplicity(1, 1))
    }
)
value1926: BinaryAssociation = BinaryAssociation(
    name="value1926",
    ends={
        Property(name="uml_TracedInputPin1928", type=umlTrace_uml_TracedQualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedQualifierValue1927", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1929: BinaryAssociation = BinaryAssociation(
    name="originalObject1929",
    ends={
        Property(name="uml_umlTrace_QualifierValue", type=umlTrace_uml_TracedQualifierValue, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedQualifierValue1930", type=uml_umlTrace_QualifierValue, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1931: BinaryAssociation = BinaryAssociation(
    name="originalObject1931",
    ends={
        Property(name="uml_umlTrace_InitialNode", type=umlTrace_uml_TracedInitialNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInitialNode", type=uml_umlTrace_InitialNode, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1932: BinaryAssociation = BinaryAssociation(
    name="originalObject1932",
    ends={
        Property(name="uml_umlTrace_LiteralInteger", type=umlTrace_uml_TracedLiteralInteger, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLiteralInteger", type=uml_umlTrace_LiteralInteger, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1933: BinaryAssociation = BinaryAssociation(
    name="originalObject1933",
    ends={
        Property(name="uml_umlTrace_ClearVariableAction", type=umlTrace_uml_TracedClearVariableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClearVariableAction", type=uml_umlTrace_ClearVariableAction, multiplicity=Multiplicity(0, 1))
    }
)
appliedProfile1934: BinaryAssociation = BinaryAssociation(
    name="appliedProfile1934",
    ends={
        Property(name="uml_TracedProfile1935", type=umlTrace_uml_TracedProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProfileApplication", type=uml_TracedProfile, multiplicity=Multiplicity(1, 1))
    }
)
applyingPackage1936: BinaryAssociation = BinaryAssociation(
    name="applyingPackage1936",
    ends={
        Property(name="uml_TracedPackage1938", type=umlTrace_uml_TracedProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProfileApplication1937", type=uml_TracedPackage, multiplicity=Multiplicity(1, 1))
    }
)
signature1918: BinaryAssociation = BinaryAssociation(
    name="signature1918",
    ends={
        Property(name="uml_TracedNamedElement1920", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage1919", type=uml_TracedNamedElement, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1921: BinaryAssociation = BinaryAssociation(
    name="originalObject1921",
    ends={
        Property(name="uml_umlTrace_Message", type=umlTrace_uml_TracedMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedMessage1922", type=uml_umlTrace_Message, multiplicity=Multiplicity(0, 1))
    }
)
templateParameter1943: BinaryAssociation = BinaryAssociation(
    name="templateParameter1943",
    ends={
        Property(name="uml_TracedTemplateParameter1945", type=umlTrace_uml_TracedParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameterableElement1944", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
default1946: BinaryAssociation = BinaryAssociation(
    name="default1946",
    ends={
        Property(name="uml_TracedParameterableElement1947", type=umlTrace_uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameter", type=uml_TracedParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
ownedDefault1948: BinaryAssociation = BinaryAssociation(
    name="ownedDefault1948",
    ends={
        Property(name="uml_TracedParameterableElement1950", type=umlTrace_uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameter1949", type=uml_TracedParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
parameteredElement1951: BinaryAssociation = BinaryAssociation(
    name="parameteredElement1951",
    ends={
        Property(name="uml_TracedParameterableElement1953", type=umlTrace_uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameter1952", type=uml_TracedParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
signature1954: BinaryAssociation = BinaryAssociation(
    name="signature1954",
    ends={
        Property(name="uml_TracedTemplateSignature1956", type=umlTrace_uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameter1955", type=uml_TracedTemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameteredElement1957: BinaryAssociation = BinaryAssociation(
    name="ownedParameteredElement1957",
    ends={
        Property(name="uml_TracedParameterableElement1959", type=umlTrace_uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameter1958", type=uml_TracedParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_TemplateParameter1960: BinaryAssociation = BinaryAssociation(
    name="originalObject_TemplateParameter1960",
    ends={
        Property(name="uml_umlTrace_TemplateParameter", type=umlTrace_uml_TracedTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateParameter1961", type=uml_umlTrace_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
definingEnd1962: BinaryAssociation = BinaryAssociation(
    name="definingEnd1962",
    ends={
        Property(name="uml_TracedProperty1963", type=umlTrace_uml_TracedConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectorEnd", type=uml_TracedProperty, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1939: BinaryAssociation = BinaryAssociation(
    name="originalObject1939",
    ends={
        Property(name="uml_umlTrace_ProfileApplication", type=umlTrace_uml_TracedProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProfileApplication1940", type=uml_umlTrace_ProfileApplication, multiplicity=Multiplicity(0, 1))
    }
)
owningTemplateParameter1941: BinaryAssociation = BinaryAssociation(
    name="owningTemplateParameter1941",
    ends={
        Property(name="uml_TracedTemplateParameter1942", type=umlTrace_uml_TracedParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameterableElement", type=uml_TracedTemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
originalObject1972: BinaryAssociation = BinaryAssociation(
    name="originalObject1972",
    ends={
        Property(name="uml_umlTrace_Image", type=umlTrace_uml_TracedImage, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedImage", type=uml_umlTrace_Image, multiplicity=Multiplicity(0, 1))
    }
)
ownedPort1973: BinaryAssociation = BinaryAssociation(
    name="ownedPort1973",
    ends={
        Property(name="uml_TracedPort1974", type=umlTrace_uml_TracedEncapsulatedClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedEncapsulatedClassifier", type=uml_TracedPort, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue1975: BinaryAssociation = BinaryAssociation(
    name="defaultValue1975",
    ends={
        Property(name="uml_TracedValueSpecification1976", type=umlTrace_uml_TracedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameter", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
operation1977: BinaryAssociation = BinaryAssociation(
    name="operation1977",
    ends={
        Property(name="uml_TracedOperation1979", type=umlTrace_uml_TracedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameter1978", type=uml_TracedOperation, multiplicity=Multiplicity(0, 1))
    }
)
parameterSet1980: BinaryAssociation = BinaryAssociation(
    name="parameterSet1980",
    ends={
        Property(name="uml_TracedParameterSet1982", type=umlTrace_uml_TracedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameter1981", type=uml_TracedParameterSet, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1983: BinaryAssociation = BinaryAssociation(
    name="originalObject1983",
    ends={
        Property(name="uml_umlTrace_Parameter", type=umlTrace_uml_TracedParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedParameter1984", type=uml_umlTrace_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
partWithPort1964: BinaryAssociation = BinaryAssociation(
    name="partWithPort1964",
    ends={
        Property(name="uml_TracedProperty1966", type=umlTrace_uml_TracedConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectorEnd1965", type=uml_TracedProperty, multiplicity=Multiplicity(0, 1))
    }
)
role1967: BinaryAssociation = BinaryAssociation(
    name="role1967",
    ends={
        Property(name="uml_TracedConnectableElement1969", type=umlTrace_uml_TracedConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectorEnd1968", type=uml_TracedConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1970: BinaryAssociation = BinaryAssociation(
    name="originalObject1970",
    ends={
        Property(name="uml_umlTrace_ConnectorEnd", type=umlTrace_uml_TracedConnectorEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectorEnd1971", type=uml_umlTrace_ConnectorEnd, multiplicity=Multiplicity(0, 1))
    }
)
port1988: BinaryAssociation = BinaryAssociation(
    name="port1988",
    ends={
        Property(name="uml_TracedPort1990", type=umlTrace_uml_TracedTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTrigger1989", type=uml_TracedPort, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject1991: BinaryAssociation = BinaryAssociation(
    name="originalObject1991",
    ends={
        Property(name="uml_umlTrace_Trigger", type=umlTrace_uml_TracedTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTrigger1992", type=uml_umlTrace_Trigger, multiplicity=Multiplicity(0, 1))
    }
)
operation1993: BinaryAssociation = BinaryAssociation(
    name="operation1993",
    ends={
        Property(name="uml_TracedOperation1994", type=umlTrace_uml_TracedCallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallOperationAction", type=uml_TracedOperation, multiplicity=Multiplicity(1, 1))
    }
)
target1995: BinaryAssociation = BinaryAssociation(
    name="target1995",
    ends={
        Property(name="uml_TracedInputPin1997", type=umlTrace_uml_TracedCallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallOperationAction1996", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject1998: BinaryAssociation = BinaryAssociation(
    name="originalObject1998",
    ends={
        Property(name="uml_umlTrace_CallOperationAction", type=umlTrace_uml_TracedCallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallOperationAction1999", type=uml_umlTrace_CallOperationAction, multiplicity=Multiplicity(0, 1))
    }
)
metaclassReference2000: BinaryAssociation = BinaryAssociation(
    name="metaclassReference2000",
    ends={
        Property(name="uml_TracedElementImport2001", type=umlTrace_uml_TracedProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProfile", type=uml_TracedElementImport, multiplicity=Multiplicity(0, 9999))
    }
)
metamodelReference2002: BinaryAssociation = BinaryAssociation(
    name="metamodelReference2002",
    ends={
        Property(name="uml_TracedPackageImport2004", type=umlTrace_uml_TracedProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProfile2003", type=uml_TracedPackageImport, multiplicity=Multiplicity(0, 9999))
    }
)
max2005: BinaryAssociation = BinaryAssociation(
    name="max2005",
    ends={
        Property(name="uml_TracedValueSpecification2006", type=umlTrace_uml_TracedInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterval", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
min2007: BinaryAssociation = BinaryAssociation(
    name="min2007",
    ends={
        Property(name="uml_TracedValueSpecification2009", type=umlTrace_uml_TracedInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterval2008", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
fromAction1985: BinaryAssociation = BinaryAssociation(
    name="fromAction1985",
    ends={
        Property(name="uml_TracedAction1986", type=umlTrace_uml_TracedActionInputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActionInputPin", type=uml_TracedAction, multiplicity=Multiplicity(1, 1))
    }
)
event1987: BinaryAssociation = BinaryAssociation(
    name="event1987",
    ends={
        Property(name="uml_TracedEvent", type=umlTrace_uml_TracedTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTrigger", type=uml_TracedEvent, multiplicity=Multiplicity(1, 1))
    }
)
classifier2012: BinaryAssociation = BinaryAssociation(
    name="classifier2012",
    ends={
        Property(name="umlTrace_uml_TracedInstanceSpecification", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999)),
        Property(name="uml_TracedClassifier2013", type=umlTrace_uml_TracedInstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
slot2014: BinaryAssociation = BinaryAssociation(
    name="slot2014",
    ends={
        Property(name="uml_TracedSlot2016", type=umlTrace_uml_TracedInstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInstanceSpecification2015", type=uml_TracedSlot, multiplicity=Multiplicity(0, 9999))
    }
)
specification2017: BinaryAssociation = BinaryAssociation(
    name="specification2017",
    ends={
        Property(name="uml_TracedValueSpecification2019", type=umlTrace_uml_TracedInstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInstanceSpecification2018", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_InstanceSpecification2020: BinaryAssociation = BinaryAssociation(
    name="originalObject_InstanceSpecification2020",
    ends={
        Property(name="uml_umlTrace_InstanceSpecification", type=umlTrace_uml_TracedInstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInstanceSpecification2021", type=uml_umlTrace_InstanceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
value2022: BinaryAssociation = BinaryAssociation(
    name="value2022",
    ends={
        Property(name="uml_TracedValueSpecification2023", type=umlTrace_uml_TracedValuePin, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedValuePin", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
classifier2024: BinaryAssociation = BinaryAssociation(
    name="classifier2024",
    ends={
        Property(name="uml_TracedClassifier2025", type=umlTrace_uml_TracedReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadIsClassifiedObjectAction", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
object2026: BinaryAssociation = BinaryAssociation(
    name="object2026",
    ends={
        Property(name="uml_TracedInputPin2028", type=umlTrace_uml_TracedReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadIsClassifiedObjectAction2027", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
result2029: BinaryAssociation = BinaryAssociation(
    name="result2029",
    ends={
        Property(name="uml_TracedOutputPin2031", type=umlTrace_uml_TracedReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadIsClassifiedObjectAction2030", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject_Interval2010: BinaryAssociation = BinaryAssociation(
    name="originalObject_Interval2010",
    ends={
        Property(name="uml_umlTrace_Interval", type=umlTrace_uml_TracedInterval, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterval2011", type=uml_umlTrace_Interval, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2036: BinaryAssociation = BinaryAssociation(
    name="originalObject2036",
    ends={
        Property(name="uml_umlTrace_OutputPin", type=umlTrace_uml_TracedOutputPin, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOutputPin", type=uml_umlTrace_OutputPin, multiplicity=Multiplicity(0, 1))
    }
)
decisionInput2037: BinaryAssociation = BinaryAssociation(
    name="decisionInput2037",
    ends={
        Property(name="uml_TracedBehavior2038", type=umlTrace_uml_TracedDecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDecisionNode", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
decisionInputFlow2039: BinaryAssociation = BinaryAssociation(
    name="decisionInputFlow2039",
    ends={
        Property(name="uml_TracedObjectFlow2041", type=umlTrace_uml_TracedDecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDecisionNode2040", type=uml_TracedObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2042: BinaryAssociation = BinaryAssociation(
    name="originalObject2042",
    ends={
        Property(name="uml_umlTrace_DecisionNode", type=umlTrace_uml_TracedDecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDecisionNode2043", type=uml_umlTrace_DecisionNode, multiplicity=Multiplicity(0, 1))
    }
)
result2044: BinaryAssociation = BinaryAssociation(
    name="result2044",
    ends={
        Property(name="uml_TracedOutputPin2045", type=umlTrace_uml_TracedValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedValueSpecificationAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
value2046: BinaryAssociation = BinaryAssociation(
    name="value2046",
    ends={
        Property(name="uml_TracedValueSpecification2048", type=umlTrace_uml_TracedValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedValueSpecificationAction2047", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2049: BinaryAssociation = BinaryAssociation(
    name="originalObject2049",
    ends={
        Property(name="uml_umlTrace_ValueSpecificationAction", type=umlTrace_uml_TracedValueSpecificationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedValueSpecificationAction2050", type=uml_umlTrace_ValueSpecificationAction, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion2051: BinaryAssociation = BinaryAssociation(
    name="extendedRegion2051",
    ends={
        Property(name="uml_TracedRegion2052", type=umlTrace_uml_TracedRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRegion", type=uml_TracedRegion, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2032: BinaryAssociation = BinaryAssociation(
    name="originalObject2032",
    ends={
        Property(name="uml_umlTrace_ReadIsClassifiedObjectAction", type=umlTrace_uml_TracedReadIsClassifiedObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadIsClassifiedObjectAction2033", type=uml_umlTrace_ReadIsClassifiedObjectAction, multiplicity=Multiplicity(0, 1))
    }
)
conformance2034: BinaryAssociation = BinaryAssociation(
    name="conformance2034",
    ends={
        Property(name="uml_TracedProtocolConformance2035", type=umlTrace_uml_TracedProtocolStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedProtocolStateMachine", type=uml_TracedProtocolConformance, multiplicity=Multiplicity(0, 9999))
    }
)
transition2059: BinaryAssociation = BinaryAssociation(
    name="transition2059",
    ends={
        Property(name="uml_TracedTransition2061", type=umlTrace_uml_TracedRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRegion2060", type=uml_TracedTransition, multiplicity=Multiplicity(0, 9999))
    }
)
subvertex2062: BinaryAssociation = BinaryAssociation(
    name="subvertex2062",
    ends={
        Property(name="uml_TracedVertex", type=umlTrace_uml_TracedRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRegion2063", type=uml_TracedVertex, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2064: BinaryAssociation = BinaryAssociation(
    name="originalObject2064",
    ends={
        Property(name="uml_umlTrace_Region", type=umlTrace_uml_TracedRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRegion2065", type=uml_umlTrace_Region, multiplicity=Multiplicity(0, 1))
    }
)
interruptingEdge2066: BinaryAssociation = BinaryAssociation(
    name="interruptingEdge2066",
    ends={
        Property(name="uml_TracedActivityEdge2067", type=umlTrace_uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterruptibleActivityRegion", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
node2068: BinaryAssociation = BinaryAssociation(
    name="node2068",
    ends={
        Property(name="uml_TracedActivityNode2070", type=umlTrace_uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterruptibleActivityRegion2069", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2071: BinaryAssociation = BinaryAssociation(
    name="originalObject2071",
    ends={
        Property(name="uml_umlTrace_InterruptibleActivityRegion", type=umlTrace_uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInterruptibleActivityRegion2072", type=uml_umlTrace_InterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2073: BinaryAssociation = BinaryAssociation(
    name="originalObject2073",
    ends={
        Property(name="uml_umlTrace_DestroyLinkAction", type=umlTrace_uml_TracedDestroyLinkAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDestroyLinkAction", type=uml_umlTrace_DestroyLinkAction, multiplicity=Multiplicity(0, 1))
    }
)
state2053: BinaryAssociation = BinaryAssociation(
    name="state2053",
    ends={
        Property(name="uml_TracedState2055", type=umlTrace_uml_TracedRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRegion2054", type=uml_TracedState, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine2056: BinaryAssociation = BinaryAssociation(
    name="stateMachine2056",
    ends={
        Property(name="uml_TracedStateMachine2058", type=umlTrace_uml_TracedRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRegion2057", type=uml_TracedStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
inActivity2079: BinaryAssociation = BinaryAssociation(
    name="inActivity2079",
    ends={
        Property(name="uml_TracedActivity2081", type=umlTrace_uml_TracedActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityGroup2080", type=uml_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
subgroup2082: BinaryAssociation = BinaryAssociation(
    name="subgroup2082",
    ends={
        Property(name="uml_TracedActivityGroup2084", type=umlTrace_uml_TracedActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityGroup2083", type=uml_TracedActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
superGroup2085: BinaryAssociation = BinaryAssociation(
    name="superGroup2085",
    ends={
        Property(name="uml_TracedActivityGroup2087", type=umlTrace_uml_TracedActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityGroup2086", type=uml_TracedActivityGroup, multiplicity=Multiplicity(0, 1))
    }
)
fragment2088: BinaryAssociation = BinaryAssociation(
    name="fragment2088",
    ends={
        Property(name="uml_TracedInteractionFragment2089", type=umlTrace_uml_TracedInteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionOperand", type=uml_TracedInteractionFragment, multiplicity=Multiplicity(0, 9999))
    }
)
guard2090: BinaryAssociation = BinaryAssociation(
    name="guard2090",
    ends={
        Property(name="uml_TracedInteractionConstraint2092", type=umlTrace_uml_TracedInteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionOperand2091", type=uml_TracedInteractionConstraint, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2093: BinaryAssociation = BinaryAssociation(
    name="originalObject2093",
    ends={
        Property(name="uml_umlTrace_InteractionOperand", type=umlTrace_uml_TracedInteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionOperand2094", type=uml_umlTrace_InteractionOperand, multiplicity=Multiplicity(0, 1))
    }
)
activity2095: BinaryAssociation = BinaryAssociation(
    name="activity2095",
    ends={
        Property(name="uml_TracedActivity2096", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge", type=uml_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
guard2097: BinaryAssociation = BinaryAssociation(
    name="guard2097",
    ends={
        Property(name="uml_TracedValueSpecification2099", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2098", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
containedEdge2074: BinaryAssociation = BinaryAssociation(
    name="containedEdge2074",
    ends={
        Property(name="uml_TracedActivityEdge2075", type=umlTrace_uml_TracedActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityGroup", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inPartition2100: BinaryAssociation = BinaryAssociation(
    name="inPartition2100",
    ends={
        Property(name="uml_TracedActivityPartition2102", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2101", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
containedNode2076: BinaryAssociation = BinaryAssociation(
    name="containedNode2076",
    ends={
        Property(name="uml_TracedActivityNode2078", type=umlTrace_uml_TracedActivityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityGroup2077", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
interrupts2103: BinaryAssociation = BinaryAssociation(
    name="interrupts2103",
    ends={
        Property(name="uml_TracedInterruptibleActivityRegion2105", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2104", type=uml_TracedInterruptibleActivityRegion, multiplicity=Multiplicity(0, 1))
    }
)
inStructuredNode2106: BinaryAssociation = BinaryAssociation(
    name="inStructuredNode2106",
    ends={
        Property(name="uml_TracedStructuredActivityNode2108", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2107", type=uml_TracedStructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
target2109: BinaryAssociation = BinaryAssociation(
    name="target2109",
    ends={
        Property(name="uml_TracedActivityNode2111", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2110", type=uml_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
source2112: BinaryAssociation = BinaryAssociation(
    name="source2112",
    ends={
        Property(name="uml_TracedActivityNode2114", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2113", type=uml_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
redefinedEdge2115: BinaryAssociation = BinaryAssociation(
    name="redefinedEdge2115",
    ends={
        Property(name="uml_TracedActivityEdge2117", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2116", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
weight2118: BinaryAssociation = BinaryAssociation(
    name="weight2118",
    ends={
        Property(name="uml_TracedValueSpecification2120", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2119", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
inGroup2121: BinaryAssociation = BinaryAssociation(
    name="inGroup2121",
    ends={
        Property(name="uml_TracedActivityGroup2123", type=umlTrace_uml_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivityEdge2122", type=uml_TracedActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
conveyed2124: BinaryAssociation = BinaryAssociation(
    name="conveyed2124",
    ends={
        Property(name="uml_TracedClassifier2125", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 9999))
    }
)
informationSource2126: BinaryAssociation = BinaryAssociation(
    name="informationSource2126",
    ends={
        Property(name="uml_TracedNamedElement2128", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2127", type=uml_TracedNamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
informationTarget2129: BinaryAssociation = BinaryAssociation(
    name="informationTarget2129",
    ends={
        Property(name="uml_TracedNamedElement2131", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2130", type=uml_TracedNamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
realization2132: BinaryAssociation = BinaryAssociation(
    name="realization2132",
    ends={
        Property(name="uml_TracedRelationship", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2133", type=uml_TracedRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
realizingActivityEdge2134: BinaryAssociation = BinaryAssociation(
    name="realizingActivityEdge2134",
    ends={
        Property(name="uml_TracedActivityEdge2136", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2135", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
realizingConnector2137: BinaryAssociation = BinaryAssociation(
    name="realizingConnector2137",
    ends={
        Property(name="uml_TracedConnector2139", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2138", type=uml_TracedConnector, multiplicity=Multiplicity(0, 9999))
    }
)
realizingMessage2140: BinaryAssociation = BinaryAssociation(
    name="realizingMessage2140",
    ends={
        Property(name="uml_TracedMessage2142", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2141", type=uml_TracedMessage, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2143: BinaryAssociation = BinaryAssociation(
    name="originalObject2143",
    ends={
        Property(name="uml_umlTrace_InformationFlow", type=umlTrace_uml_TracedInformationFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInformationFlow2144", type=uml_umlTrace_InformationFlow, multiplicity=Multiplicity(0, 1))
    }
)
state2145: BinaryAssociation = BinaryAssociation(
    name="state2145",
    ends={
        Property(name="uml_TracedState2146", type=umlTrace_uml_TracedPseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPseudostate", type=uml_TracedState, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine2147: BinaryAssociation = BinaryAssociation(
    name="stateMachine2147",
    ends={
        Property(name="uml_TracedStateMachine2149", type=umlTrace_uml_TracedPseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPseudostate2148", type=uml_TracedStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2150: BinaryAssociation = BinaryAssociation(
    name="originalObject2150",
    ends={
        Property(name="uml_umlTrace_Pseudostate", type=umlTrace_uml_TracedPseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPseudostate2151", type=uml_umlTrace_Pseudostate, multiplicity=Multiplicity(0, 1))
    }
)
extend2152: BinaryAssociation = BinaryAssociation(
    name="extend2152",
    ends={
        Property(name="uml_TracedExtend2153", type=umlTrace_uml_TracedUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUseCase", type=uml_TracedExtend, multiplicity=Multiplicity(0, 9999))
    }
)
extensionPoint2154: BinaryAssociation = BinaryAssociation(
    name="extensionPoint2154",
    ends={
        Property(name="uml_TracedExtensionPoint2156", type=umlTrace_uml_TracedUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUseCase2155", type=uml_TracedExtensionPoint, multiplicity=Multiplicity(0, 9999))
    }
)
include2157: BinaryAssociation = BinaryAssociation(
    name="include2157",
    ends={
        Property(name="uml_TracedInclude2159", type=umlTrace_uml_TracedUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUseCase2158", type=uml_TracedInclude, multiplicity=Multiplicity(0, 9999))
    }
)
subject2160: BinaryAssociation = BinaryAssociation(
    name="subject2160",
    ends={
        Property(name="uml_TracedClassifier2162", type=umlTrace_uml_TracedUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUseCase2161", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2163: BinaryAssociation = BinaryAssociation(
    name="originalObject2163",
    ends={
        Property(name="uml_umlTrace_UseCase", type=umlTrace_uml_TracedUseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUseCase2164", type=uml_umlTrace_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
replyToCall2165: BinaryAssociation = BinaryAssociation(
    name="replyToCall2165",
    ends={
        Property(name="uml_TracedTrigger2166", type=umlTrace_uml_TracedReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReplyAction", type=uml_TracedTrigger, multiplicity=Multiplicity(1, 1))
    }
)
replyValue2167: BinaryAssociation = BinaryAssociation(
    name="replyValue2167",
    ends={
        Property(name="uml_TracedInputPin2169", type=umlTrace_uml_TracedReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReplyAction2168", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999))
    }
)
returnInformation2170: BinaryAssociation = BinaryAssociation(
    name="returnInformation2170",
    ends={
        Property(name="uml_TracedInputPin2172", type=umlTrace_uml_TracedReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReplyAction2171", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2173: BinaryAssociation = BinaryAssociation(
    name="originalObject2173",
    ends={
        Property(name="uml_umlTrace_ReplyAction", type=umlTrace_uml_TracedReplyAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReplyAction2174", type=uml_umlTrace_ReplyAction, multiplicity=Multiplicity(0, 1))
    }
)
cfragmentGate2175: BinaryAssociation = BinaryAssociation(
    name="cfragmentGate2175",
    ends={
        Property(name="uml_TracedGate2176", type=umlTrace_uml_TracedCombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCombinedFragment", type=uml_TracedGate, multiplicity=Multiplicity(0, 9999))
    }
)
operand2177: BinaryAssociation = BinaryAssociation(
    name="operand2177",
    ends={
        Property(name="uml_TracedInteractionOperand2179", type=umlTrace_uml_TracedCombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCombinedFragment2178", type=uml_TracedInteractionOperand, multiplicity=Multiplicity(1, 9999))
    }
)
originalObject_CombinedFragment2180: BinaryAssociation = BinaryAssociation(
    name="originalObject_CombinedFragment2180",
    ends={
        Property(name="uml_umlTrace_CombinedFragment", type=umlTrace_uml_TracedCombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCombinedFragment2181", type=uml_umlTrace_CombinedFragment, multiplicity=Multiplicity(0, 1))
    }
)
body2182: BinaryAssociation = BinaryAssociation(
    name="body2182",
    ends={
        Property(name="uml_TracedExecutableNode2183", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause", type=uml_TracedExecutableNode, multiplicity=Multiplicity(0, 9999))
    }
)
bodyOutput2184: BinaryAssociation = BinaryAssociation(
    name="bodyOutput2184",
    ends={
        Property(name="uml_TracedOutputPin2186", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause2185", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 9999))
    }
)
decider2187: BinaryAssociation = BinaryAssociation(
    name="decider2187",
    ends={
        Property(name="uml_TracedOutputPin2189", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause2188", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
predecessorClause2190: BinaryAssociation = BinaryAssociation(
    name="predecessorClause2190",
    ends={
        Property(name="uml_TracedClause2192", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause2191", type=uml_TracedClause, multiplicity=Multiplicity(0, 9999))
    }
)
successorClause2193: BinaryAssociation = BinaryAssociation(
    name="successorClause2193",
    ends={
        Property(name="uml_TracedClause2195", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause2194", type=uml_TracedClause, multiplicity=Multiplicity(0, 9999))
    }
)
test2196: BinaryAssociation = BinaryAssociation(
    name="test2196",
    ends={
        Property(name="uml_TracedExecutableNode2198", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause2197", type=uml_TracedExecutableNode, multiplicity=Multiplicity(1, 9999))
    }
)
originalObject2199: BinaryAssociation = BinaryAssociation(
    name="originalObject2199",
    ends={
        Property(name="uml_umlTrace_Clause", type=umlTrace_uml_TracedClause, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClause2200", type=uml_umlTrace_Clause, multiplicity=Multiplicity(0, 1))
    }
)
instance2201: BinaryAssociation = BinaryAssociation(
    name="instance2201",
    ends={
        Property(name="uml_TracedInstanceSpecification2202", type=umlTrace_uml_TracedInstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInstanceValue", type=uml_TracedInstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2203: BinaryAssociation = BinaryAssociation(
    name="originalObject2203",
    ends={
        Property(name="uml_umlTrace_InstanceValue", type=umlTrace_uml_TracedInstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInstanceValue2204", type=uml_umlTrace_InstanceValue, multiplicity=Multiplicity(0, 1))
    }
)
client2205: BinaryAssociation = BinaryAssociation(
    name="client2205",
    ends={
        Property(name="uml_TracedNamedElement2206", type=umlTrace_uml_TracedDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDependency", type=uml_TracedNamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
supplier2207: BinaryAssociation = BinaryAssociation(
    name="supplier2207",
    ends={
        Property(name="uml_TracedNamedElement2209", type=umlTrace_uml_TracedDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDependency2208", type=uml_TracedNamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
originalObject_Dependency2210: BinaryAssociation = BinaryAssociation(
    name="originalObject_Dependency2210",
    ends={
        Property(name="uml_umlTrace_Dependency", type=umlTrace_uml_TracedDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDependency2211", type=uml_umlTrace_Dependency, multiplicity=Multiplicity(0, 1))
    }
)
expr2212: BinaryAssociation = BinaryAssociation(
    name="expr2212",
    ends={
        Property(name="uml_TracedValueSpecification2213", type=umlTrace_uml_TracedTimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeExpression", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
observation2214: BinaryAssociation = BinaryAssociation(
    name="observation2214",
    ends={
        Property(name="uml_TracedObservation2216", type=umlTrace_uml_TracedTimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeExpression2215", type=uml_TracedObservation, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2217: BinaryAssociation = BinaryAssociation(
    name="originalObject2217",
    ends={
        Property(name="uml_umlTrace_TimeExpression", type=umlTrace_uml_TracedTimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTimeExpression2218", type=uml_umlTrace_TimeExpression, multiplicity=Multiplicity(0, 1))
    }
)
utilizedElement2219: BinaryAssociation = BinaryAssociation(
    name="utilizedElement2219",
    ends={
        Property(name="uml_TracedPackageableElement2220", type=umlTrace_uml_TracedManifestation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedManifestation", type=uml_TracedPackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
classifier2221: BinaryAssociation = BinaryAssociation(
    name="classifier2221",
    ends={
        Property(name="uml_TracedClassifier2222", type=umlTrace_uml_TracedReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadExtentAction", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
result2223: BinaryAssociation = BinaryAssociation(
    name="result2223",
    ends={
        Property(name="uml_TracedOutputPin2225", type=umlTrace_uml_TracedReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadExtentAction2224", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2226: BinaryAssociation = BinaryAssociation(
    name="originalObject2226",
    ends={
        Property(name="uml_umlTrace_ReadExtentAction", type=umlTrace_uml_TracedReadExtentAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadExtentAction2227", type=uml_umlTrace_ReadExtentAction, multiplicity=Multiplicity(0, 1))
    }
)
effect2228: BinaryAssociation = BinaryAssociation(
    name="effect2228",
    ends={
        Property(name="uml_TracedBehavior2229", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
guard2230: BinaryAssociation = BinaryAssociation(
    name="guard2230",
    ends={
        Property(name="uml_TracedConstraint2232", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2231", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 1))
    }
)
redefinedTransition2233: BinaryAssociation = BinaryAssociation(
    name="redefinedTransition2233",
    ends={
        Property(name="uml_TracedTransition2235", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2234", type=uml_TracedTransition, multiplicity=Multiplicity(0, 1))
    }
)
source2236: BinaryAssociation = BinaryAssociation(
    name="source2236",
    ends={
        Property(name="uml_TracedVertex2238", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2237", type=uml_TracedVertex, multiplicity=Multiplicity(1, 1))
    }
)
target2239: BinaryAssociation = BinaryAssociation(
    name="target2239",
    ends={
        Property(name="uml_TracedVertex2241", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2240", type=uml_TracedVertex, multiplicity=Multiplicity(1, 1))
    }
)
trigger2242: BinaryAssociation = BinaryAssociation(
    name="trigger2242",
    ends={
        Property(name="uml_TracedTrigger2244", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2243", type=uml_TracedTrigger, multiplicity=Multiplicity(0, 9999))
    }
)
container2245: BinaryAssociation = BinaryAssociation(
    name="container2245",
    ends={
        Property(name="uml_TracedRegion2247", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2246", type=uml_TracedRegion, multiplicity=Multiplicity(1, 1))
    }
)
originalObject_Transition2248: BinaryAssociation = BinaryAssociation(
    name="originalObject_Transition2248",
    ends={
        Property(name="uml_umlTrace_Transition", type=umlTrace_uml_TracedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTransition2249", type=uml_umlTrace_Transition, multiplicity=Multiplicity(0, 1))
    }
)
end2250: BinaryAssociation = BinaryAssociation(
    name="end2250",
    ends={
        Property(name="uml_TracedProperty2251", type=umlTrace_uml_TracedLinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkEndData", type=uml_TracedProperty, multiplicity=Multiplicity(1, 1))
    }
)
qualifier2252: BinaryAssociation = BinaryAssociation(
    name="qualifier2252",
    ends={
        Property(name="uml_TracedQualifierValue2254", type=umlTrace_uml_TracedLinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkEndData2253", type=uml_TracedQualifierValue, multiplicity=Multiplicity(0, 9999))
    }
)
value2255: BinaryAssociation = BinaryAssociation(
    name="value2255",
    ends={
        Property(name="uml_TracedInputPin2257", type=umlTrace_uml_TracedLinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkEndData2256", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_LinkEndData2258: BinaryAssociation = BinaryAssociation(
    name="originalObject_LinkEndData2258",
    ends={
        Property(name="uml_umlTrace_LinkEndData", type=umlTrace_uml_TracedLinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkEndData2259", type=uml_umlTrace_LinkEndData, multiplicity=Multiplicity(0, 1))
    }
)
nestedNode2260: BinaryAssociation = BinaryAssociation(
    name="nestedNode2260",
    ends={
        Property(name="uml_TracedNode2261", type=umlTrace_uml_TracedNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNode", type=uml_TracedNode, multiplicity=Multiplicity(0, 9999))
    }
)
mergedPackage2262: BinaryAssociation = BinaryAssociation(
    name="mergedPackage2262",
    ends={
        Property(name="uml_TracedPackage2263", type=umlTrace_uml_TracedPackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackageMerge", type=uml_TracedPackage, multiplicity=Multiplicity(1, 1))
    }
)
receivingPackage2264: BinaryAssociation = BinaryAssociation(
    name="receivingPackage2264",
    ends={
        Property(name="uml_TracedPackage2266", type=umlTrace_uml_TracedPackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackageMerge2265", type=uml_TracedPackage, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2267: BinaryAssociation = BinaryAssociation(
    name="originalObject2267",
    ends={
        Property(name="uml_umlTrace_PackageMerge", type=umlTrace_uml_TracedPackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackageMerge2268", type=uml_umlTrace_PackageMerge, multiplicity=Multiplicity(0, 1))
    }
)
selection2269: BinaryAssociation = BinaryAssociation(
    name="selection2269",
    ends={
        Property(name="uml_TracedBehavior2270", type=umlTrace_uml_TracedObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedObjectFlow", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
transformation2271: BinaryAssociation = BinaryAssociation(
    name="transformation2271",
    ends={
        Property(name="uml_TracedBehavior2273", type=umlTrace_uml_TracedObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedObjectFlow2272", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2274: BinaryAssociation = BinaryAssociation(
    name="originalObject2274",
    ends={
        Property(name="uml_umlTrace_ObjectFlow", type=umlTrace_uml_TracedObjectFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedObjectFlow2275", type=uml_umlTrace_ObjectFlow, multiplicity=Multiplicity(0, 1))
    }
)
changeExpression2276: BinaryAssociation = BinaryAssociation(
    name="changeExpression2276",
    ends={
        Property(name="uml_TracedValueSpecification2277", type=umlTrace_uml_TracedChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedChangeEvent", type=uml_TracedValueSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2278: BinaryAssociation = BinaryAssociation(
    name="originalObject2278",
    ends={
        Property(name="uml_umlTrace_ChangeEvent", type=umlTrace_uml_TracedChangeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedChangeEvent2279", type=uml_umlTrace_ChangeEvent, multiplicity=Multiplicity(0, 1))
    }
)
redefinedElement2280: BinaryAssociation = BinaryAssociation(
    name="redefinedElement2280",
    ends={
        Property(name="uml_TracedRedefinableElement", type=umlTrace_uml_TracedRedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRedefinableElement", type=uml_TracedRedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext2281: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext2281",
    ends={
        Property(name="uml_TracedClassifier2283", type=umlTrace_uml_TracedRedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRedefinableElement2282", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
target2284: BinaryAssociation = BinaryAssociation(
    name="target2284",
    ends={
        Property(name="uml_TracedInputPin2285", type=umlTrace_uml_TracedDestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDestroyObjectAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2286: BinaryAssociation = BinaryAssociation(
    name="originalObject2286",
    ends={
        Property(name="uml_umlTrace_DestroyObjectAction", type=umlTrace_uml_TracedDestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDestroyObjectAction2287", type=uml_umlTrace_DestroyObjectAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2288: BinaryAssociation = BinaryAssociation(
    name="originalObject2288",
    ends={
        Property(name="uml_umlTrace_ForkNode", type=umlTrace_uml_TracedForkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedForkNode", type=uml_umlTrace_ForkNode, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute2289: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute2289",
    ends={
        Property(name="uml_TracedProperty2290", type=umlTrace_uml_TracedSignal, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSignal", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2291: BinaryAssociation = BinaryAssociation(
    name="originalObject2291",
    ends={
        Property(name="uml_umlTrace_Signal", type=umlTrace_uml_TracedSignal, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSignal2292", type=uml_umlTrace_Signal, multiplicity=Multiplicity(0, 1))
    }
)
annotatedElement2293: BinaryAssociation = BinaryAssociation(
    name="annotatedElement2293",
    ends={
        Property(name="uml_TracedElement2294", type=umlTrace_uml_TracedComment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComment", type=uml_TracedElement, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2295: BinaryAssociation = BinaryAssociation(
    name="originalObject2295",
    ends={
        Property(name="uml_umlTrace_Comment", type=umlTrace_uml_TracedComment, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedComment2296", type=uml_umlTrace_Comment, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute2297: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute2297",
    ends={
        Property(name="uml_TracedProperty2298", type=umlTrace_uml_TracedStructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredClassifier", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
ownedConnector2299: BinaryAssociation = BinaryAssociation(
    name="ownedConnector2299",
    ends={
        Property(name="uml_TracedConnector2301", type=umlTrace_uml_TracedStructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredClassifier2300", type=uml_TracedConnector, multiplicity=Multiplicity(0, 9999))
    }
)
part2302: BinaryAssociation = BinaryAssociation(
    name="part2302",
    ends={
        Property(name="uml_TracedProperty2304", type=umlTrace_uml_TracedStructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredClassifier2303", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
role2305: BinaryAssociation = BinaryAssociation(
    name="role2305",
    ends={
        Property(name="uml_TracedConnectableElement2307", type=umlTrace_uml_TracedStructuredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStructuredClassifier2306", type=uml_TracedConnectableElement, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2308: BinaryAssociation = BinaryAssociation(
    name="originalObject2308",
    ends={
        Property(name="uml_umlTrace_LiteralNull", type=umlTrace_uml_TracedLiteralNull, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLiteralNull", type=uml_umlTrace_LiteralNull, multiplicity=Multiplicity(0, 1))
    }
)
regionAsInput2309: BinaryAssociation = BinaryAssociation(
    name="regionAsInput2309",
    ends={
        Property(name="uml_TracedExpansionRegion2310", type=umlTrace_uml_TracedExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpansionNode", type=uml_TracedExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
regionAsOutput2311: BinaryAssociation = BinaryAssociation(
    name="regionAsOutput2311",
    ends={
        Property(name="uml_TracedExpansionRegion2313", type=umlTrace_uml_TracedExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpansionNode2312", type=uml_TracedExpansionRegion, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2314: BinaryAssociation = BinaryAssociation(
    name="originalObject2314",
    ends={
        Property(name="uml_umlTrace_ExpansionNode", type=umlTrace_uml_TracedExpansionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExpansionNode2315", type=uml_umlTrace_ExpansionNode, multiplicity=Multiplicity(0, 1))
    }
)
signal2316: BinaryAssociation = BinaryAssociation(
    name="signal2316",
    ends={
        Property(name="uml_TracedSignal2317", type=umlTrace_uml_TracedReception, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReception", type=uml_TracedSignal, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2318: BinaryAssociation = BinaryAssociation(
    name="originalObject2318",
    ends={
        Property(name="uml_umlTrace_Reception", type=umlTrace_uml_TracedReception, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReception2319", type=uml_umlTrace_Reception, multiplicity=Multiplicity(0, 1))
    }
)
exception2320: BinaryAssociation = BinaryAssociation(
    name="exception2320",
    ends={
        Property(name="uml_TracedInputPin2321", type=umlTrace_uml_TracedRaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRaiseExceptionAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2322: BinaryAssociation = BinaryAssociation(
    name="originalObject2322",
    ends={
        Property(name="uml_umlTrace_RaiseExceptionAction", type=umlTrace_uml_TracedRaiseExceptionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRaiseExceptionAction2323", type=uml_umlTrace_RaiseExceptionAction, multiplicity=Multiplicity(0, 1))
    }
)
method2324: BinaryAssociation = BinaryAssociation(
    name="method2324",
    ends={
        Property(name="uml_TracedBehavior2325", type=umlTrace_uml_TracedBehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioralFeature", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter2326: BinaryAssociation = BinaryAssociation(
    name="ownedParameter2326",
    ends={
        Property(name="uml_TracedParameter2328", type=umlTrace_uml_TracedBehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioralFeature2327", type=uml_TracedParameter, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameterSet2329: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet2329",
    ends={
        Property(name="uml_TracedParameterSet2331", type=umlTrace_uml_TracedBehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioralFeature2330", type=uml_TracedParameterSet, multiplicity=Multiplicity(0, 9999))
    }
)
raisedException2332: BinaryAssociation = BinaryAssociation(
    name="raisedException2332",
    ends={
        Property(name="uml_TracedType2334", type=umlTrace_uml_TracedBehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehavioralFeature2333", type=uml_TracedType, multiplicity=Multiplicity(0, 9999))
    }
)
insertAt2335: BinaryAssociation = BinaryAssociation(
    name="insertAt2335",
    ends={
        Property(name="uml_TracedInputPin2336", type=umlTrace_uml_TracedAddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAddVariableValueAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2337: BinaryAssociation = BinaryAssociation(
    name="originalObject2337",
    ends={
        Property(name="uml_umlTrace_AddVariableValueAction", type=umlTrace_uml_TracedAddVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAddVariableValueAction2338", type=uml_umlTrace_AddVariableValueAction, multiplicity=Multiplicity(0, 1))
    }
)
association2339: BinaryAssociation = BinaryAssociation(
    name="association2339",
    ends={
        Property(name="uml_TracedAssociation2340", type=umlTrace_uml_TracedClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClearAssociationAction", type=uml_TracedAssociation, multiplicity=Multiplicity(1, 1))
    }
)
object2341: BinaryAssociation = BinaryAssociation(
    name="object2341",
    ends={
        Property(name="uml_TracedInputPin2343", type=umlTrace_uml_TracedClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClearAssociationAction2342", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2344: BinaryAssociation = BinaryAssociation(
    name="originalObject2344",
    ends={
        Property(name="uml_umlTrace_ClearAssociationAction", type=umlTrace_uml_TracedClearAssociationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClearAssociationAction2345", type=uml_umlTrace_ClearAssociationAction, multiplicity=Multiplicity(0, 1))
    }
)
first2346: BinaryAssociation = BinaryAssociation(
    name="first2346",
    ends={
        Property(name="uml_TracedInputPin2347", type=umlTrace_uml_TracedTestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTestIdentityAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
result2348: BinaryAssociation = BinaryAssociation(
    name="result2348",
    ends={
        Property(name="uml_TracedOutputPin2350", type=umlTrace_uml_TracedTestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTestIdentityAction2349", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
second2351: BinaryAssociation = BinaryAssociation(
    name="second2351",
    ends={
        Property(name="uml_TracedInputPin2353", type=umlTrace_uml_TracedTestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTestIdentityAction2352", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2354: BinaryAssociation = BinaryAssociation(
    name="originalObject2354",
    ends={
        Property(name="uml_umlTrace_TestIdentityAction", type=umlTrace_uml_TracedTestIdentityAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTestIdentityAction2355", type=uml_umlTrace_TestIdentityAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2356: BinaryAssociation = BinaryAssociation(
    name="originalObject2356",
    ends={
        Property(name="uml_umlTrace_ControlFlow", type=umlTrace_uml_TracedControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedControlFlow", type=uml_umlTrace_ControlFlow, multiplicity=Multiplicity(0, 1))
    }
)
bodyCondition2357: BinaryAssociation = BinaryAssociation(
    name="bodyCondition2357",
    ends={
        Property(name="uml_TracedConstraint2358", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 1))
    }
)
class2359: BinaryAssociation = BinaryAssociation(
    name="class2359",
    ends={
        Property(name="uml_TracedClass2361", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2360", type=uml_TracedClass, multiplicity=Multiplicity(0, 1))
    }
)
datatype2362: BinaryAssociation = BinaryAssociation(
    name="datatype2362",
    ends={
        Property(name="uml_TracedDataType2364", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2363", type=uml_TracedDataType, multiplicity=Multiplicity(0, 1))
    }
)
interface2365: BinaryAssociation = BinaryAssociation(
    name="interface2365",
    ends={
        Property(name="uml_TracedInterface2367", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2366", type=uml_TracedInterface, multiplicity=Multiplicity(0, 1))
    }
)
postcondition2368: BinaryAssociation = BinaryAssociation(
    name="postcondition2368",
    ends={
        Property(name="uml_TracedConstraint2370", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2369", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
precondition2371: BinaryAssociation = BinaryAssociation(
    name="precondition2371",
    ends={
        Property(name="uml_TracedConstraint2373", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2372", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedOperation2374: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation2374",
    ends={
        Property(name="uml_TracedOperation2376", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2375", type=uml_TracedOperation, multiplicity=Multiplicity(0, 9999))
    }
)
type2377: BinaryAssociation = BinaryAssociation(
    name="type2377",
    ends={
        Property(name="uml_TracedType2379", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2378", type=uml_TracedType, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2380: BinaryAssociation = BinaryAssociation(
    name="originalObject2380",
    ends={
        Property(name="uml_umlTrace_Operation", type=umlTrace_uml_TracedOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOperation2381", type=uml_umlTrace_Operation, multiplicity=Multiplicity(0, 1))
    }
)
end2382: BinaryAssociation = BinaryAssociation(
    name="end2382",
    ends={
        Property(name="uml_TracedConnectorEnd2383", type=umlTrace_uml_TracedConnectableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectableElement", type=uml_TracedConnectorEnd, multiplicity=Multiplicity(0, 9999))
    }
)
container2384: BinaryAssociation = BinaryAssociation(
    name="container2384",
    ends={
        Property(name="uml_TracedRegion2385", type=umlTrace_uml_TracedVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVertex", type=uml_TracedRegion, multiplicity=Multiplicity(0, 1))
    }
)
incoming2386: BinaryAssociation = BinaryAssociation(
    name="incoming2386",
    ends={
        Property(name="uml_TracedTransition2388", type=umlTrace_uml_TracedVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVertex2387", type=uml_TracedTransition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing2389: BinaryAssociation = BinaryAssociation(
    name="outgoing2389",
    ends={
        Property(name="uml_TracedTransition2391", type=umlTrace_uml_TracedVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVertex2390", type=uml_TracedTransition, multiplicity=Multiplicity(0, 9999))
    }
)
ownedRule2392: BinaryAssociation = BinaryAssociation(
    name="ownedRule2392",
    ends={
        Property(name="uml_TracedConstraint2393", type=umlTrace_uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamespace", type=uml_TracedConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
elementImport2394: BinaryAssociation = BinaryAssociation(
    name="elementImport2394",
    ends={
        Property(name="uml_TracedElementImport2396", type=umlTrace_uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamespace2395", type=uml_TracedElementImport, multiplicity=Multiplicity(0, 9999))
    }
)
packageImport2397: BinaryAssociation = BinaryAssociation(
    name="packageImport2397",
    ends={
        Property(name="uml_TracedPackageImport2399", type=umlTrace_uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamespace2398", type=uml_TracedPackageImport, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember2400: BinaryAssociation = BinaryAssociation(
    name="ownedMember2400",
    ends={
        Property(name="uml_TracedNamedElement2402", type=umlTrace_uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamespace2401", type=uml_TracedNamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedMember2403: BinaryAssociation = BinaryAssociation(
    name="importedMember2403",
    ends={
        Property(name="uml_TracedPackageableElement2405", type=umlTrace_uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamespace2404", type=uml_TracedPackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
member2406: BinaryAssociation = BinaryAssociation(
    name="member2406",
    ends={
        Property(name="uml_TracedNamedElement2408", type=umlTrace_uml_TracedNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedNamespace2407", type=uml_TracedNamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedPackage2409: BinaryAssociation = BinaryAssociation(
    name="importedPackage2409",
    ends={
        Property(name="uml_TracedPackage2410", type=umlTrace_uml_TracedPackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackageImport", type=uml_TracedPackage, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2414: BinaryAssociation = BinaryAssociation(
    name="originalObject2414",
    ends={
        Property(name="uml_umlTrace_PackageImport", type=umlTrace_uml_TracedPackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackageImport2415", type=uml_umlTrace_PackageImport, multiplicity=Multiplicity(0, 1))
    }
)
execution2416: BinaryAssociation = BinaryAssociation(
    name="execution2416",
    ends={
        Property(name="uml_TracedExecutionSpecification", type=umlTrace_uml_TracedExecutionOccurrenceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExecutionOccurrenceSpecification", type=uml_TracedExecutionSpecification, multiplicity=Multiplicity(1, 1))
    }
)
exceptionInput2417: BinaryAssociation = BinaryAssociation(
    name="exceptionInput2417",
    ends={
        Property(name="uml_TracedObjectNode", type=umlTrace_uml_TracedExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExceptionHandler", type=uml_TracedObjectNode, multiplicity=Multiplicity(1, 1))
    }
)
exceptionType2418: BinaryAssociation = BinaryAssociation(
    name="exceptionType2418",
    ends={
        Property(name="uml_TracedClassifier2420", type=umlTrace_uml_TracedExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExceptionHandler2419", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 9999))
    }
)
handlerBody2421: BinaryAssociation = BinaryAssociation(
    name="handlerBody2421",
    ends={
        Property(name="uml_TracedExecutableNode2423", type=umlTrace_uml_TracedExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExceptionHandler2422", type=uml_TracedExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
protectedNode2424: BinaryAssociation = BinaryAssociation(
    name="protectedNode2424",
    ends={
        Property(name="uml_TracedExecutableNode2426", type=umlTrace_uml_TracedExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExceptionHandler2425", type=uml_TracedExecutableNode, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2427: BinaryAssociation = BinaryAssociation(
    name="originalObject2427",
    ends={
        Property(name="uml_umlTrace_ExceptionHandler", type=umlTrace_uml_TracedExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExceptionHandler2428", type=uml_umlTrace_ExceptionHandler, multiplicity=Multiplicity(0, 1))
    }
)
activityScope2429: BinaryAssociation = BinaryAssociation(
    name="activityScope2429",
    ends={
        Property(name="uml_TracedActivity2430", type=umlTrace_uml_TracedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVariable", type=uml_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
importingNamespace2411: BinaryAssociation = BinaryAssociation(
    name="importingNamespace2411",
    ends={
        Property(name="uml_TracedNamespace2413", type=umlTrace_uml_TracedPackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedPackageImport2412", type=uml_TracedNamespace, multiplicity=Multiplicity(1, 1))
    }
)
scope2431: BinaryAssociation = BinaryAssociation(
    name="scope2431",
    ends={
        Property(name="uml_TracedStructuredActivityNode2433", type=umlTrace_uml_TracedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVariable2432", type=uml_TracedStructuredActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2434: BinaryAssociation = BinaryAssociation(
    name="originalObject2434",
    ends={
        Property(name="uml_umlTrace_Variable", type=umlTrace_uml_TracedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedVariable2435", type=uml_umlTrace_Variable, multiplicity=Multiplicity(0, 1))
    }
)
actualGate2436: BinaryAssociation = BinaryAssociation(
    name="actualGate2436",
    ends={
        Property(name="uml_TracedGate2437", type=umlTrace_uml_TracedInteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionUse", type=uml_TracedGate, multiplicity=Multiplicity(0, 9999))
    }
)
argument2438: BinaryAssociation = BinaryAssociation(
    name="argument2438",
    ends={
        Property(name="uml_TracedValueSpecification2440", type=umlTrace_uml_TracedInteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionUse2439", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
refersTo2441: BinaryAssociation = BinaryAssociation(
    name="refersTo2441",
    ends={
        Property(name="uml_TracedInteraction2443", type=umlTrace_uml_TracedInteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionUse2442", type=uml_TracedInteraction, multiplicity=Multiplicity(1, 1))
    }
)
returnValue2444: BinaryAssociation = BinaryAssociation(
    name="returnValue2444",
    ends={
        Property(name="uml_TracedValueSpecification2446", type=umlTrace_uml_TracedInteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionUse2445", type=uml_TracedValueSpecification, multiplicity=Multiplicity(0, 1))
    }
)
returnValueRecipient2447: BinaryAssociation = BinaryAssociation(
    name="returnValueRecipient2447",
    ends={
        Property(name="uml_TracedProperty2449", type=umlTrace_uml_TracedInteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionUse2448", type=uml_TracedProperty, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_InteractionUse2450: BinaryAssociation = BinaryAssociation(
    name="originalObject_InteractionUse2450",
    ends={
        Property(name="uml_umlTrace_InteractionUse", type=umlTrace_uml_TracedInteractionUse, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInteractionUse2451", type=uml_umlTrace_InteractionUse, multiplicity=Multiplicity(0, 1))
    }
)
endType2452: BinaryAssociation = BinaryAssociation(
    name="endType2452",
    ends={
        Property(name="uml_TracedType2453", type=umlTrace_uml_TracedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAssociation", type=uml_TracedType, multiplicity=Multiplicity(1, 9999))
    }
)
memberEnd2454: BinaryAssociation = BinaryAssociation(
    name="memberEnd2454",
    ends={
        Property(name="uml_TracedProperty2456", type=umlTrace_uml_TracedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAssociation2455", type=uml_TracedProperty, multiplicity=Multiplicity(2, 9999))
    }
)
ownedEnd2457: BinaryAssociation = BinaryAssociation(
    name="ownedEnd2457",
    ends={
        Property(name="uml_TracedProperty2459", type=umlTrace_uml_TracedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAssociation2458", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
navigableOwnedEnd2460: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd2460",
    ends={
        Property(name="uml_TracedProperty2462", type=umlTrace_uml_TracedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAssociation2461", type=uml_TracedProperty, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject_Association2463: BinaryAssociation = BinaryAssociation(
    name="originalObject_Association2463",
    ends={
        Property(name="uml_umlTrace_Association", type=umlTrace_uml_TracedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAssociation2464", type=uml_umlTrace_Association, multiplicity=Multiplicity(0, 1))
    }
)
invariant2465: BinaryAssociation = BinaryAssociation(
    name="invariant2465",
    ends={
        Property(name="uml_TracedConstraint2466", type=umlTrace_uml_TracedStateInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStateInvariant", type=uml_TracedConstraint, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2467: BinaryAssociation = BinaryAssociation(
    name="originalObject2467",
    ends={
        Property(name="uml_umlTrace_StateInvariant", type=umlTrace_uml_TracedStateInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedStateInvariant2468", type=uml_umlTrace_StateInvariant, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2469: BinaryAssociation = BinaryAssociation(
    name="originalObject2469",
    ends={
        Property(name="uml_umlTrace_LiteralReal", type=umlTrace_uml_TracedLiteralReal, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLiteralReal", type=uml_umlTrace_LiteralReal, multiplicity=Multiplicity(0, 1))
    }
)
argument2470: BinaryAssociation = BinaryAssociation(
    name="argument2470",
    ends={
        Property(name="uml_TracedInputPin2471", type=umlTrace_uml_TracedInvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInvocationAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 9999))
    }
)
onPort2472: BinaryAssociation = BinaryAssociation(
    name="onPort2472",
    ends={
        Property(name="uml_TracedPort2474", type=umlTrace_uml_TracedInvocationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedInvocationAction2473", type=uml_TracedPort, multiplicity=Multiplicity(0, 1))
    }
)
removeAt2475: BinaryAssociation = BinaryAssociation(
    name="removeAt2475",
    ends={
        Property(name="uml_TracedInputPin2476", type=umlTrace_uml_TracedRemoveVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRemoveVariableValueAction", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2477: BinaryAssociation = BinaryAssociation(
    name="originalObject2477",
    ends={
        Property(name="uml_umlTrace_RemoveVariableValueAction", type=umlTrace_uml_TracedRemoveVariableValueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedRemoveVariableValueAction2478", type=uml_umlTrace_RemoveVariableValueAction, multiplicity=Multiplicity(0, 1))
    }
)
contract2479: BinaryAssociation = BinaryAssociation(
    name="contract2479",
    ends={
        Property(name="uml_TracedClassifier2480", type=umlTrace_uml_TracedSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSubstitution", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
substitutingClassifier2481: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier2481",
    ends={
        Property(name="uml_TracedClassifier2483", type=umlTrace_uml_TracedSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedSubstitution2482", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2484: BinaryAssociation = BinaryAssociation(
    name="originalObject2484",
    ends={
        Property(name="uml_umlTrace_Gate", type=umlTrace_uml_TracedGate, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGate", type=uml_umlTrace_Gate, multiplicity=Multiplicity(0, 1))
    }
)
deployedElement2485: BinaryAssociation = BinaryAssociation(
    name="deployedElement2485",
    ends={
        Property(name="uml_TracedPackageableElement2486", type=umlTrace_uml_TracedDeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDeploymentTarget", type=uml_TracedPackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
deployment2487: BinaryAssociation = BinaryAssociation(
    name="deployment2487",
    ends={
        Property(name="uml_TracedDeployment2489", type=umlTrace_uml_TracedDeploymentTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDeploymentTarget2488", type=uml_TracedDeployment, multiplicity=Multiplicity(0, 9999))
    }
)
before2492: BinaryAssociation = BinaryAssociation(
    name="before2492",
    ends={
        Property(name="uml_TracedOccurrenceSpecification2494", type=umlTrace_uml_TracedGeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralOrdering2493", type=uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2495: BinaryAssociation = BinaryAssociation(
    name="originalObject2495",
    ends={
        Property(name="uml_umlTrace_GeneralOrdering", type=umlTrace_uml_TracedGeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralOrdering2496", type=uml_umlTrace_GeneralOrdering, multiplicity=Multiplicity(0, 1))
    }
)
behavior2497: BinaryAssociation = BinaryAssociation(
    name="behavior2497",
    ends={
        Property(name="uml_TracedBehavior2498", type=umlTrace_uml_TracedCallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallBehaviorAction", type=uml_TracedBehavior, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2499: BinaryAssociation = BinaryAssociation(
    name="originalObject2499",
    ends={
        Property(name="uml_umlTrace_CallBehaviorAction", type=umlTrace_uml_TracedCallBehaviorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCallBehaviorAction2500", type=uml_umlTrace_CallBehaviorAction, multiplicity=Multiplicity(0, 1))
    }
)
newClassifier2501: BinaryAssociation = BinaryAssociation(
    name="newClassifier2501",
    ends={
        Property(name="uml_TracedClassifier2502", type=umlTrace_uml_TracedReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReclassifyObjectAction", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
object2503: BinaryAssociation = BinaryAssociation(
    name="object2503",
    ends={
        Property(name="uml_TracedInputPin2505", type=umlTrace_uml_TracedReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReclassifyObjectAction2504", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
oldClassifier2506: BinaryAssociation = BinaryAssociation(
    name="oldClassifier2506",
    ends={
        Property(name="uml_TracedClassifier2508", type=umlTrace_uml_TracedReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReclassifyObjectAction2507", type=uml_TracedClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject2509: BinaryAssociation = BinaryAssociation(
    name="originalObject2509",
    ends={
        Property(name="uml_umlTrace_ReclassifyObjectAction", type=umlTrace_uml_TracedReclassifyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReclassifyObjectAction2510", type=uml_umlTrace_ReclassifyObjectAction, multiplicity=Multiplicity(0, 1))
    }
)
ownedGroup2511: BinaryAssociation = BinaryAssociation(
    name="ownedGroup2511",
    ends={
        Property(name="uml_TracedActivityGroup2512", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity", type=uml_TracedActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
after2490: BinaryAssociation = BinaryAssociation(
    name="after2490",
    ends={
        Property(name="uml_TracedOccurrenceSpecification2491", type=umlTrace_uml_TracedGeneralOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedGeneralOrdering", type=uml_TracedOccurrenceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
edge2513: BinaryAssociation = BinaryAssociation(
    name="edge2513",
    ends={
        Property(name="uml_TracedActivityEdge2515", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2514", type=uml_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
node2516: BinaryAssociation = BinaryAssociation(
    name="node2516",
    ends={
        Property(name="uml_TracedActivityNode2518", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2517", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
variable2519: BinaryAssociation = BinaryAssociation(
    name="variable2519",
    ends={
        Property(name="uml_TracedVariable2521", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2520", type=uml_TracedVariable, multiplicity=Multiplicity(0, 9999))
    }
)
group2522: BinaryAssociation = BinaryAssociation(
    name="group2522",
    ends={
        Property(name="uml_TracedActivityGroup2524", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2523", type=uml_TracedActivityGroup, multiplicity=Multiplicity(0, 9999))
    }
)
ownedNode2525: BinaryAssociation = BinaryAssociation(
    name="ownedNode2525",
    ends={
        Property(name="uml_TracedActivityNode2527", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2526", type=uml_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
partition2528: BinaryAssociation = BinaryAssociation(
    name="partition2528",
    ends={
        Property(name="uml_TracedActivityPartition2530", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2529", type=uml_TracedActivityPartition, multiplicity=Multiplicity(0, 9999))
    }
)
structuredNode2531: BinaryAssociation = BinaryAssociation(
    name="structuredNode2531",
    ends={
        Property(name="uml_TracedStructuredActivityNode2533", type=umlTrace_uml_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActivity2532", type=uml_TracedStructuredActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
entry2534: BinaryAssociation = BinaryAssociation(
    name="entry2534",
    ends={
        Property(name="uml_TracedPseudostate2535", type=umlTrace_uml_TracedConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectionPointReference", type=uml_TracedPseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
exit2536: BinaryAssociation = BinaryAssociation(
    name="exit2536",
    ends={
        Property(name="uml_TracedPseudostate2538", type=umlTrace_uml_TracedConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectionPointReference2537", type=uml_TracedPseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
state2539: BinaryAssociation = BinaryAssociation(
    name="state2539",
    ends={
        Property(name="uml_TracedState2541", type=umlTrace_uml_TracedConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectionPointReference2540", type=uml_TracedState, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2542: BinaryAssociation = BinaryAssociation(
    name="originalObject2542",
    ends={
        Property(name="uml_umlTrace_ConnectionPointReference", type=umlTrace_uml_TracedConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedConnectionPointReference2543", type=uml_umlTrace_ConnectionPointReference, multiplicity=Multiplicity(0, 1))
    }
)
action2544: BinaryAssociation = BinaryAssociation(
    name="action2544",
    ends={
        Property(name="uml_TracedAction2545", type=umlTrace_uml_TracedActionExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActionExecutionSpecification", type=uml_TracedAction, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2546: BinaryAssociation = BinaryAssociation(
    name="originalObject2546",
    ends={
        Property(name="uml_umlTrace_ActionExecutionSpecification", type=umlTrace_uml_TracedActionExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActionExecutionSpecification2547", type=uml_umlTrace_ActionExecutionSpecification, multiplicity=Multiplicity(0, 1))
    }
)
result2548: BinaryAssociation = BinaryAssociation(
    name="result2548",
    ends={
        Property(name="uml_TracedOutputPin2549", type=umlTrace_uml_TracedReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadSelfAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2550: BinaryAssociation = BinaryAssociation(
    name="originalObject2550",
    ends={
        Property(name="uml_umlTrace_ReadSelfAction", type=umlTrace_uml_TracedReadSelfAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedReadSelfAction2551", type=uml_umlTrace_ReadSelfAction, multiplicity=Multiplicity(0, 1))
    }
)
returnInformation2552: BinaryAssociation = BinaryAssociation(
    name="returnInformation2552",
    ends={
        Property(name="uml_TracedOutputPin2553", type=umlTrace_uml_TracedAcceptCallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedAcceptCallAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 1))
    }
)
insertAt2554: BinaryAssociation = BinaryAssociation(
    name="insertAt2554",
    ends={
        Property(name="uml_TracedInputPin2555", type=umlTrace_uml_TracedLinkEndCreationData, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedLinkEndCreationData", type=uml_TracedInputPin, multiplicity=Multiplicity(0, 1))
    }
)
parameterSubstitution2556: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution2556",
    ends={
        Property(name="uml_TracedTemplateParameterSubstitution2557", type=umlTrace_uml_TracedTemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateBinding", type=uml_TracedTemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999))
    }
)
signature2558: BinaryAssociation = BinaryAssociation(
    name="signature2558",
    ends={
        Property(name="uml_TracedTemplateSignature2560", type=umlTrace_uml_TracedTemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateBinding2559", type=uml_TracedTemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
boundElement2561: BinaryAssociation = BinaryAssociation(
    name="boundElement2561",
    ends={
        Property(name="uml_TracedTemplateableElement2563", type=umlTrace_uml_TracedTemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateBinding2562", type=uml_TracedTemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2564: BinaryAssociation = BinaryAssociation(
    name="originalObject2564",
    ends={
        Property(name="uml_umlTrace_TemplateBinding", type=umlTrace_uml_TracedTemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedTemplateBinding2565", type=uml_umlTrace_TemplateBinding, multiplicity=Multiplicity(0, 1))
    }
)
result2566: BinaryAssociation = BinaryAssociation(
    name="result2566",
    ends={
        Property(name="uml_TracedOutputPin2567", type=umlTrace_uml_TracedClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClearStructuralFeatureAction", type=uml_TracedOutputPin, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2568: BinaryAssociation = BinaryAssociation(
    name="originalObject2568",
    ends={
        Property(name="uml_umlTrace_ClearStructuralFeatureAction", type=umlTrace_uml_TracedClearStructuralFeatureAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedClearStructuralFeatureAction2569", type=uml_umlTrace_ClearStructuralFeatureAction, multiplicity=Multiplicity(0, 1))
    }
)
behavior2570: BinaryAssociation = BinaryAssociation(
    name="behavior2570",
    ends={
        Property(name="uml_TracedBehavior2571", type=umlTrace_uml_TracedOpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOpaqueExpression", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
result2572: BinaryAssociation = BinaryAssociation(
    name="result2572",
    ends={
        Property(name="uml_TracedParameter2574", type=umlTrace_uml_TracedOpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOpaqueExpression2573", type=uml_TracedParameter, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2575: BinaryAssociation = BinaryAssociation(
    name="originalObject2575",
    ends={
        Property(name="uml_umlTrace_OpaqueExpression", type=umlTrace_uml_TracedOpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedOpaqueExpression2576", type=uml_umlTrace_OpaqueExpression, multiplicity=Multiplicity(0, 1))
    }
)
deployment2577: BinaryAssociation = BinaryAssociation(
    name="deployment2577",
    ends={
        Property(name="uml_TracedDeployment2578", type=umlTrace_uml_TracedDeploymentSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedDeploymentSpecification", type=uml_TracedDeployment, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2579: BinaryAssociation = BinaryAssociation(
    name="originalObject2579",
    ends={
        Property(name="uml_umlTrace_Actor", type=umlTrace_uml_TracedActor, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedActor", type=uml_umlTrace_Actor, multiplicity=Multiplicity(0, 1))
    }
)
behavior2580: BinaryAssociation = BinaryAssociation(
    name="behavior2580",
    ends={
        Property(name="uml_TracedBehavior2581", type=umlTrace_uml_TracedBehaviorExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehaviorExecutionSpecification", type=uml_TracedBehavior, multiplicity=Multiplicity(0, 1))
    }
)
originalObject2582: BinaryAssociation = BinaryAssociation(
    name="originalObject2582",
    ends={
        Property(name="uml_umlTrace_BehaviorExecutionSpecification", type=umlTrace_uml_TracedBehaviorExecutionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedBehaviorExecutionSpecification2583", type=uml_umlTrace_BehaviorExecutionSpecification, multiplicity=Multiplicity(0, 1))
    }
)
handler2584: BinaryAssociation = BinaryAssociation(
    name="handler2584",
    ends={
        Property(name="uml_TracedExceptionHandler2585", type=umlTrace_uml_TracedExecutableNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedExecutableNode", type=uml_TracedExceptionHandler, multiplicity=Multiplicity(0, 9999))
    }
)
object2586: BinaryAssociation = BinaryAssociation(
    name="object2586",
    ends={
        Property(name="uml_TracedInputPin2587", type=umlTrace_uml_TracedUnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUnmarshallAction", type=uml_TracedInputPin, multiplicity=Multiplicity(1, 1))
    }
)
result2588: BinaryAssociation = BinaryAssociation(
    name="result2588",
    ends={
        Property(name="uml_TracedOutputPin2590", type=umlTrace_uml_TracedUnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUnmarshallAction2589", type=uml_TracedOutputPin, multiplicity=Multiplicity(1, 9999))
    }
)
unmarshallType2591: BinaryAssociation = BinaryAssociation(
    name="unmarshallType2591",
    ends={
        Property(name="uml_TracedClassifier2593", type=umlTrace_uml_TracedUnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUnmarshallAction2592", type=uml_TracedClassifier, multiplicity=Multiplicity(1, 1))
    }
)
originalObject2594: BinaryAssociation = BinaryAssociation(
    name="originalObject2594",
    ends={
        Property(name="uml_umlTrace_UnmarshallAction", type=umlTrace_uml_TracedUnmarshallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedUnmarshallAction2595", type=uml_umlTrace_UnmarshallAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject_CentralBufferNode2596: BinaryAssociation = BinaryAssociation(
    name="originalObject_CentralBufferNode2596",
    ends={
        Property(name="uml_umlTrace_CentralBufferNode", type=umlTrace_uml_TracedCentralBufferNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_uml_TracedCentralBufferNode", type=uml_umlTrace_CentralBufferNode, multiplicity=Multiplicity(0, 1))
    }
)
eAnnotations2597: BinaryAssociation = BinaryAssociation(
    name="eAnnotations2597",
    ends={
        Property(name="ecore_umlTrace_EAnnotation", type=umlTrace_ecore_TracedEModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="umlTrace_ecore_TracedEModelElement", type=ecore_umlTrace_EAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_umlTrace_Kernel_TracedObject_TracedExtensionalValue = Generalization(general=TracedExtensionalValue, specific=umlTrace_Kernel_TracedObject)
gen_umlTrace_Kernel_TracedIntegerValue_TracedPrimitiveValue = Generalization(general=TracedPrimitiveValue, specific=umlTrace_Kernel_TracedIntegerValue)
gen_umlTrace_Kernel_TracedLiteralEvaluation_TracedEvaluation = Generalization(general=TracedEvaluation, specific=umlTrace_Kernel_TracedLiteralEvaluation)
gen_umlTrace_Kernel_TracedValue_TracedSemanticVisitor = Generalization(general=TracedSemanticVisitor, specific=umlTrace_Kernel_TracedValue)
gen_umlTrace_Kernel_TracedPrimitiveValue_TracedValue = Generalization(general=TracedValue, specific=umlTrace_Kernel_TracedPrimitiveValue)
gen_umlTrace_Kernel_TracedEvaluation_TracedSemanticVisitor = Generalization(general=TracedSemanticVisitor, specific=umlTrace_Kernel_TracedEvaluation)
gen_umlTrace_Kernel_TracedBooleanValue_TracedPrimitiveValue = Generalization(general=TracedPrimitiveValue, specific=umlTrace_Kernel_TracedBooleanValue)
gen_umlTrace_Kernel_TracedLiteralBooleanEvaluation_TracedLiteralEvaluation = Generalization(general=TracedLiteralEvaluation, specific=umlTrace_Kernel_TracedLiteralBooleanEvaluation)
gen_umlTrace_Kernel_TracedReference_TracedStructuredValue = Generalization(general=TracedStructuredValue, specific=umlTrace_Kernel_TracedReference)
gen_umlTrace_Kernel_TracedCompoundValue_TracedStructuredValue = Generalization(general=TracedStructuredValue, specific=umlTrace_Kernel_TracedCompoundValue)
gen_umlTrace_Kernel_TracedStructuredValue_TracedValue = Generalization(general=TracedValue, specific=umlTrace_Kernel_TracedStructuredValue)
gen_umlTrace_Kernel_TracedExtensionalValue_TracedCompoundValue = Generalization(general=TracedCompoundValue, specific=umlTrace_Kernel_TracedExtensionalValue)
gen_umlTrace_Kernel_TracedLiteralIntegerEvaluation_TracedLiteralEvaluation = Generalization(general=TracedLiteralEvaluation, specific=umlTrace_Kernel_TracedLiteralIntegerEvaluation)
gen_umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution_TracedExecution = Generalization(general=TracedExecution, specific=umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution)
gen_umlTrace_BasicBehaviors_TracedExecution_TracedObject = Generalization(general=TracedObject, specific=umlTrace_BasicBehaviors_TracedExecution)
gen_umlTrace_IntermediateActivities_TracedForkedToken_TracedToken = Generalization(general=TracedToken, specific=umlTrace_IntermediateActivities_TracedForkedToken)
gen_umlTrace_IntermediateActivities_TracedJoinNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedJoinNodeActivation)
gen_umlTrace_IntermediateActivities_TracedInitialNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedInitialNodeActivation)
gen_umlTrace_IntermediateActivities_TracedObjectNodeActivation_TracedActivityNodeActivation = Generalization(general=TracedActivityNodeActivation, specific=umlTrace_IntermediateActivities_TracedObjectNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation)
gen_umlTrace_IntermediateActivities_TracedMergeNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedMergeNodeActivation)
gen_umlTrace_IntermediateActivities_TracedControlToken_TracedToken = Generalization(general=TracedToken, specific=umlTrace_IntermediateActivities_TracedControlToken)
gen_umlTrace_IntermediateActivities_TracedObjectToken_TracedToken = Generalization(general=TracedToken, specific=umlTrace_IntermediateActivities_TracedObjectToken)
gen_umlTrace_IntermediateActivities_TracedDecisionNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedDecisionNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation_TracedObjectNodeActivation = Generalization(general=TracedObjectNodeActivation, specific=umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityNodeActivation_TracedSemanticVisitor = Generalization(general=TracedSemanticVisitor, specific=umlTrace_IntermediateActivities_TracedActivityNodeActivation)
gen_umlTrace_IntermediateActivities_TracedForkNodeActivation_TracedControlNodeActivation = Generalization(general=TracedControlNodeActivation, specific=umlTrace_IntermediateActivities_TracedForkNodeActivation)
gen_umlTrace_IntermediateActivities_TracedActivityExecution_TracedExecution = Generalization(general=TracedExecution, specific=umlTrace_IntermediateActivities_TracedActivityExecution)
gen_umlTrace_IntermediateActivities_TracedControlNodeActivation_TracedActivityNodeActivation = Generalization(general=TracedActivityNodeActivation, specific=umlTrace_IntermediateActivities_TracedControlNodeActivation)
gen_umlTrace_IntermediateActions_TracedValueSpecificationActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_IntermediateActions_TracedValueSpecificationActionActivation)
gen_umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation = Generalization(general=TracedStructuralFeatureActionActivation, specific=umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation)
gen_umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation_TracedWriteStructuralFeatureActionActivation = Generalization(general=TracedWriteStructuralFeatureActionActivation, specific=umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation)
gen_umlTrace_IntermediateActions_TracedCreateObjectActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_IntermediateActions_TracedCreateObjectActionActivation)
gen_umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation = Generalization(general=TracedStructuralFeatureActionActivation, specific=umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation)
gen_umlTrace_BasicActions_TracedActionActivation_TracedActivityNodeActivation = Generalization(general=TracedActivityNodeActivation, specific=umlTrace_BasicActions_TracedActionActivation)
gen_umlTrace_BasicActions_TracedOutputPinActivation_TracedPinActivation = Generalization(general=TracedPinActivation, specific=umlTrace_BasicActions_TracedOutputPinActivation)
gen_umlTrace_BasicActions_TracedCallBehaviorActionActivation_TracedCallActionActivation = Generalization(general=TracedCallActionActivation, specific=umlTrace_BasicActions_TracedCallBehaviorActionActivation)
gen_umlTrace_BasicActions_TracedOpaqueActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_BasicActions_TracedOpaqueActionActivation)
gen_umlTrace_BasicActions_TracedCallActionActivation_TracedInvocationActionActivation = Generalization(general=TracedInvocationActionActivation, specific=umlTrace_BasicActions_TracedCallActionActivation)
gen_umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation)
gen_umlTrace_BasicActions_TracedPinActivation_TracedObjectNodeActivation = Generalization(general=TracedObjectNodeActivation, specific=umlTrace_BasicActions_TracedPinActivation)
gen_umlTrace_BasicActions_TracedInputPinActivation_TracedPinActivation = Generalization(general=TracedPinActivation, specific=umlTrace_BasicActions_TracedInputPinActivation)
gen_umlTrace_BasicActions_TracedInvocationActionActivation_TracedActionActivation = Generalization(general=TracedActionActivation, specific=umlTrace_BasicActions_TracedInvocationActionActivation)
gen_umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_TracedOpaqueBehaviorExecution = Generalization(general=TracedOpaqueBehaviorExecution, specific=umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution)
gen_umlTrace_uml_TracedStructuralFeature_uml_TracedFeature = Generalization(general=uml_TracedFeature, specific=umlTrace_uml_TracedStructuralFeature)
gen_umlTrace_uml_TracedStructuralFeature_uml_TracedTypedElement = Generalization(general=uml_TracedTypedElement, specific=umlTrace_uml_TracedStructuralFeature)
gen_umlTrace_uml_TracedStructuralFeature_uml_TracedMultiplicityElement = Generalization(general=uml_TracedMultiplicityElement, specific=umlTrace_uml_TracedStructuralFeature)
gen_umlTrace_uml_TracedConnector_TracedFeature = Generalization(general=TracedFeature, specific=umlTrace_uml_TracedConnector)
gen_umlTrace_uml_TracedOpaqueAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedOpaqueAction)
gen_umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_TracedOpaqueBehaviorExecution = Generalization(general=TracedOpaqueBehaviorExecution, specific=umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution)
gen_umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_TracedOpaqueBehaviorExecution = Generalization(general=TracedOpaqueBehaviorExecution, specific=umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution)
gen_umlTrace_uml_TracedDataType_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedDataType)
gen_umlTrace_uml_TracedCommunicationPath_TracedAssociation = Generalization(general=TracedAssociation, specific=umlTrace_uml_TracedCommunicationPath)
gen_umlTrace_uml_TracedLinkAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedLinkAction)
gen_umlTrace_uml_TracedProperty_uml_TracedStructuralFeature = Generalization(general=uml_TracedStructuralFeature, specific=umlTrace_uml_TracedProperty)
gen_umlTrace_uml_TracedProperty_uml_TracedConnectableElement = Generalization(general=uml_TracedConnectableElement, specific=umlTrace_uml_TracedProperty)
gen_umlTrace_uml_TracedProperty_uml_TracedDeploymentTarget = Generalization(general=uml_TracedDeploymentTarget, specific=umlTrace_uml_TracedProperty)
gen_umlTrace_uml_TracedContinuation_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedContinuation)
gen_umlTrace_uml_TracedRemoveStructuralFeatureValueAction_TracedWriteStructuralFeatureAction = Generalization(general=TracedWriteStructuralFeatureAction, specific=umlTrace_uml_TracedRemoveStructuralFeatureValueAction)
gen_umlTrace_uml_TracedSendSignalAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedSendSignalAction)
gen_umlTrace_uml_TracedOpaqueBehavior_TracedBehavior = Generalization(general=TracedBehavior, specific=umlTrace_uml_TracedOpaqueBehavior)
gen_umlTrace_uml_TracedArtifact_uml_TracedClassifier = Generalization(general=uml_TracedClassifier, specific=umlTrace_uml_TracedArtifact)
gen_umlTrace_uml_TracedArtifact_uml_TracedDeployedArtifact = Generalization(general=uml_TracedDeployedArtifact, specific=umlTrace_uml_TracedArtifact)
gen_umlTrace_uml_TracedTimeConstraint_TracedIntervalConstraint = Generalization(general=TracedIntervalConstraint, specific=umlTrace_uml_TracedTimeConstraint)
gen_umlTrace_uml_TracedInterfaceRealization_TracedRealization = Generalization(general=TracedRealization, specific=umlTrace_uml_TracedInterfaceRealization)
gen_umlTrace_uml_TracedObjectNode_uml_TracedActivityNode = Generalization(general=uml_TracedActivityNode, specific=umlTrace_uml_TracedObjectNode)
gen_umlTrace_uml_TracedObjectNode_uml_TracedTypedElement = Generalization(general=uml_TracedTypedElement, specific=umlTrace_uml_TracedObjectNode)
gen_umlTrace_uml_TracedActivityFinalNode_TracedFinalNode = Generalization(general=TracedFinalNode, specific=umlTrace_uml_TracedActivityFinalNode)
gen_umlTrace_uml_TracedDurationObservation_TracedObservation = Generalization(general=TracedObservation, specific=umlTrace_uml_TracedDurationObservation)
gen_umlTrace_uml_TracedAcceptEventAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedAcceptEventAction)
gen_umlTrace_uml_TracedEnumerationLiteral_TracedInstanceSpecification = Generalization(general=TracedInstanceSpecification, specific=umlTrace_uml_TracedEnumerationLiteral)
gen_umlTrace_uml_TracedAddStructuralFeatureValueAction_TracedWriteStructuralFeatureAction = Generalization(general=TracedWriteStructuralFeatureAction, specific=umlTrace_uml_TracedAddStructuralFeatureValueAction)
gen_umlTrace_uml_TracedExpression_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedExpression)
gen_umlTrace_uml_TracedConsiderIgnoreFragment_TracedCombinedFragment = Generalization(general=TracedCombinedFragment, specific=umlTrace_uml_TracedConsiderIgnoreFragment)
gen_umlTrace_uml_TracedDataStoreNode_TracedCentralBufferNode = Generalization(general=TracedCentralBufferNode, specific=umlTrace_uml_TracedDataStoreNode)
gen_umlTrace_uml_TracedFlowFinalNode_TracedFinalNode = Generalization(general=TracedFinalNode, specific=umlTrace_uml_TracedFlowFinalNode)
gen_umlTrace_uml_TracedInteractionFragment_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedInteractionFragment)
gen_umlTrace_uml_TracedReadLinkAction_TracedLinkAction = Generalization(general=TracedLinkAction, specific=umlTrace_uml_TracedReadLinkAction)
gen_umlTrace_uml_TracedClassifier_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedClassifier)
gen_umlTrace_uml_TracedClassifier_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedClassifier)
gen_umlTrace_uml_TracedClassifier_uml_TracedType = Generalization(general=uml_TracedType, specific=umlTrace_uml_TracedClassifier)
gen_umlTrace_uml_TracedClassifier_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedClassifier)
gen_umlTrace_uml_TracedInformationItem_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedInformationItem)
gen_umlTrace_uml_TracedCollaboration_uml_TracedStructuredClassifier = Generalization(general=uml_TracedStructuredClassifier, specific=umlTrace_uml_TracedCollaboration)
gen_umlTrace_uml_TracedCollaboration_uml_TracedBehavioredClassifier = Generalization(general=uml_TracedBehavioredClassifier, specific=umlTrace_uml_TracedCollaboration)
gen_umlTrace_uml_TracedMessageEnd_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedMessageEnd)
gen_umlTrace_uml_TracedTemplateSignature_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateSignature)
gen_umlTrace_uml_TracedBroadcastSignalAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedBroadcastSignalAction)
gen_umlTrace_uml_TracedDeployment_TracedDependency = Generalization(general=TracedDependency, specific=umlTrace_uml_TracedDeployment)
gen_umlTrace_uml_TracedPort_TracedProperty = Generalization(general=TracedProperty, specific=umlTrace_uml_TracedPort)
gen_umlTrace_uml_TracedTimeInterval_TracedInterval = Generalization(general=TracedInterval, specific=umlTrace_uml_TracedTimeInterval)
gen_umlTrace_uml_TracedAction_TracedExecutableNode = Generalization(general=TracedExecutableNode, specific=umlTrace_uml_TracedAction)
gen_umlTrace_uml_TracedExtension_TracedAssociation = Generalization(general=TracedAssociation, specific=umlTrace_uml_TracedExtension)
gen_umlTrace_uml_TracedDirectedRelationship_TracedRelationship = Generalization(general=TracedRelationship, specific=umlTrace_uml_TracedDirectedRelationship)
gen_umlTrace_uml_TracedTimeEvent_TracedEvent = Generalization(general=TracedEvent, specific=umlTrace_uml_TracedTimeEvent)
gen_umlTrace_uml_TracedPackageableElement_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedPackageableElement)
gen_umlTrace_uml_TracedPackageableElement_uml_TracedParameterableElement = Generalization(general=uml_TracedParameterableElement, specific=umlTrace_uml_TracedPackageableElement)
gen_umlTrace_uml_TracedType_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedType)
gen_umlTrace_uml_TracedProtocolTransition_TracedTransition = Generalization(general=TracedTransition, specific=umlTrace_uml_TracedProtocolTransition)
gen_umlTrace_uml_TracedPackage_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedPackage)
gen_umlTrace_uml_TracedPackage_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedPackage)
gen_umlTrace_uml_TracedPackage_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedPackage)
gen_umlTrace_uml_TracedBehavioredClassifier_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedBehavioredClassifier)
gen_umlTrace_uml_TracedStructuralFeatureAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedStructuralFeatureAction)
gen_umlTrace_uml_TracedConstraint_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedConstraint)
gen_umlTrace_uml_TracedMultiplicityElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedMultiplicityElement)
gen_umlTrace_uml_TracedLiteralSpecification_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedLiteralSpecification)
gen_umlTrace_uml_TracedGeneralizationSet_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedGeneralizationSet)
gen_umlTrace_uml_TracedReduceAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReduceAction)
gen_umlTrace_uml_TracedInputPin_TracedPin = Generalization(general=TracedPin, specific=umlTrace_uml_TracedInputPin)
gen_umlTrace_uml_TracedSequenceNode_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedSequenceNode)
gen_umlTrace_uml_TracedFeature_TracedRedefinableElement = Generalization(general=TracedRedefinableElement, specific=umlTrace_uml_TracedFeature)
gen_umlTrace_uml_TracedInteractionConstraint_TracedConstraint = Generalization(general=TracedConstraint, specific=umlTrace_uml_TracedInteractionConstraint)
gen_umlTrace_uml_TracedElement_TracedEModelElement = Generalization(general=TracedEModelElement, specific=umlTrace_uml_TracedElement)
gen_umlTrace_uml_TracedComponentRealization_TracedRealization = Generalization(general=TracedRealization, specific=umlTrace_uml_TracedComponentRealization)
gen_umlTrace_uml_TracedAssociationClass_uml_TracedClass = Generalization(general=uml_TracedClass, specific=umlTrace_uml_TracedAssociationClass)
gen_umlTrace_uml_TracedAssociationClass_uml_TracedAssociation = Generalization(general=uml_TracedAssociation, specific=umlTrace_uml_TracedAssociationClass)
gen_umlTrace_uml_TracedSlot_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedSlot)
gen_umlTrace_uml_TracedWriteStructuralFeatureAction_TracedStructuralFeatureAction = Generalization(general=TracedStructuralFeatureAction, specific=umlTrace_uml_TracedWriteStructuralFeatureAction)
gen_umlTrace_uml_TracedSignalEvent_TracedMessageEvent = Generalization(general=TracedMessageEvent, specific=umlTrace_uml_TracedSignalEvent)
gen_umlTrace_uml_TracedExtensionPoint_TracedRedefinableElement = Generalization(general=TracedRedefinableElement, specific=umlTrace_uml_TracedExtensionPoint)
gen_umlTrace_uml_TracedJoinNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedJoinNode)
gen_umlTrace_uml_TracedStartObjectBehaviorAction_TracedCallAction = Generalization(general=TracedCallAction, specific=umlTrace_uml_TracedStartObjectBehaviorAction)
gen_umlTrace_uml_TracedCreateObjectAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedCreateObjectAction)
gen_umlTrace_uml_TracedExecutionEnvironment_TracedNode = Generalization(general=TracedNode, specific=umlTrace_uml_TracedExecutionEnvironment)
gen_umlTrace_uml_TracedOccurrenceSpecification_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedOccurrenceSpecification)
gen_umlTrace_uml_TracedStringExpression_uml_TracedExpression = Generalization(general=uml_TracedExpression, specific=umlTrace_uml_TracedStringExpression)
gen_umlTrace_uml_TracedStringExpression_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedStringExpression)
gen_umlTrace_uml_TracedElementImport_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedElementImport)
gen_umlTrace_uml_TracedInterface_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedInterface)
gen_umlTrace_uml_TracedConditionalNode_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedConditionalNode)
gen_umlTrace_uml_TracedDeployedArtifact_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedDeployedArtifact)
gen_umlTrace_uml_TracedStereotype_TracedClass = Generalization(general=TracedClass, specific=umlTrace_uml_TracedStereotype)
gen_umlTrace_uml_TracedAnyReceiveEvent_TracedMessageEvent = Generalization(general=TracedMessageEvent, specific=umlTrace_uml_TracedAnyReceiveEvent)
gen_umlTrace_uml_TracedNamedElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedNamedElement)
gen_umlTrace_uml_TracedComponent_TracedClass = Generalization(general=TracedClass, specific=umlTrace_uml_TracedComponent)
gen_umlTrace_uml_TracedReadLinkObjectEndAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadLinkObjectEndAction)
gen_umlTrace_uml_TracedExtensionEnd_TracedProperty = Generalization(general=TracedProperty, specific=umlTrace_uml_TracedExtensionEnd)
gen_umlTrace_uml_TracedStateMachine_TracedBehavior = Generalization(general=TracedBehavior, specific=umlTrace_uml_TracedStateMachine)
gen_umlTrace_uml_TracedValueSpecification_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedValueSpecification)
gen_umlTrace_uml_TracedValueSpecification_uml_TracedTypedElement = Generalization(general=uml_TracedTypedElement, specific=umlTrace_uml_TracedValueSpecification)
gen_umlTrace_uml_TracedInteraction_uml_TracedBehavior = Generalization(general=uml_TracedBehavior, specific=umlTrace_uml_TracedInteraction)
gen_umlTrace_uml_TracedInteraction_uml_TracedInteractionFragment = Generalization(general=uml_TracedInteractionFragment, specific=umlTrace_uml_TracedInteraction)
gen_umlTrace_uml_TracedLiteralString_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralString)
gen_umlTrace_uml_TracedRealization_TracedAbstraction = Generalization(general=TracedAbstraction, specific=umlTrace_uml_TracedRealization)
gen_umlTrace_uml_TracedStartClassifierBehaviorAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedStartClassifierBehaviorAction)
gen_umlTrace_uml_TracedMessageEvent_TracedEvent = Generalization(general=TracedEvent, specific=umlTrace_uml_TracedMessageEvent)
gen_umlTrace_uml_TracedCallEvent_TracedMessageEvent = Generalization(general=TracedMessageEvent, specific=umlTrace_uml_TracedCallEvent)
gen_umlTrace_uml_TracedConnectableElementTemplateParameter_TracedTemplateParameter = Generalization(general=TracedTemplateParameter, specific=umlTrace_uml_TracedConnectableElementTemplateParameter)
gen_umlTrace_uml_TracedRelationship_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedRelationship)
gen_umlTrace_uml_TracedSendObjectAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedSendObjectAction)
gen_umlTrace_uml_TracedLifeline_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedLifeline)
gen_umlTrace_uml_TracedExecutionSpecification_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedExecutionSpecification)
gen_umlTrace_uml_TracedTimeObservation_TracedObservation = Generalization(general=TracedObservation, specific=umlTrace_uml_TracedTimeObservation)
gen_umlTrace_uml_TracedExpansionRegion_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedExpansionRegion)
gen_umlTrace_uml_TracedWriteVariableAction_TracedVariableAction = Generalization(general=TracedVariableAction, specific=umlTrace_uml_TracedWriteVariableAction)
gen_umlTrace_uml_TracedLoopNode_TracedStructuredActivityNode = Generalization(general=TracedStructuredActivityNode, specific=umlTrace_uml_TracedLoopNode)
gen_umlTrace_uml_TracedCreateLinkObjectAction_TracedCreateLinkAction = Generalization(general=TracedCreateLinkAction, specific=umlTrace_uml_TracedCreateLinkObjectAction)
gen_umlTrace_uml_TracedPrimitiveType_TracedDataType = Generalization(general=TracedDataType, specific=umlTrace_uml_TracedPrimitiveType)
gen_umlTrace_uml_TracedProtocolConformance_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedProtocolConformance)
gen_umlTrace_uml_TracedEnumeration_TracedDataType = Generalization(general=TracedDataType, specific=umlTrace_uml_TracedEnumeration)
gen_umlTrace_uml_TracedCollaborationUse_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedCollaborationUse)
gen_umlTrace_uml_TracedActivityPartition_TracedActivityGroup = Generalization(general=TracedActivityGroup, specific=umlTrace_uml_TracedActivityPartition)
gen_umlTrace_uml_TracedVariableAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedVariableAction)
gen_umlTrace_uml_TracedLinkEndDestructionData_TracedLinkEndData = Generalization(general=TracedLinkEndData, specific=umlTrace_uml_TracedLinkEndDestructionData)
gen_umlTrace_uml_TracedDurationInterval_TracedInterval = Generalization(general=TracedInterval, specific=umlTrace_uml_TracedDurationInterval)
gen_umlTrace_uml_TracedInclude_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedInclude)
gen_umlTrace_uml_TracedInclude_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedInclude)
gen_umlTrace_uml_TracedActivityNode_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedActivityNode)
gen_umlTrace_uml_TracedActivityNode_ActivityContent = Generalization(general=ActivityContent, specific=umlTrace_uml_TracedActivityNode)
gen_umlTrace_uml_TracedDestructionOccurrenceSpecification_TracedMessageOccurrenceSpecification = Generalization(general=TracedMessageOccurrenceSpecification, specific=umlTrace_uml_TracedDestructionOccurrenceSpecification)
gen_umlTrace_uml_TracedState_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedState)
gen_umlTrace_uml_TracedState_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedState)
gen_umlTrace_uml_TracedState_uml_TracedVertex = Generalization(general=uml_TracedVertex, specific=umlTrace_uml_TracedState)
gen_umlTrace_uml_TracedCallAction_TracedInvocationAction = Generalization(general=TracedInvocationAction, specific=umlTrace_uml_TracedCallAction)
gen_umlTrace_uml_TracedTemplateableElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateableElement)
gen_umlTrace_uml_TracedBehavior_TracedClass = Generalization(general=TracedClass, specific=umlTrace_uml_TracedBehavior)
gen_umlTrace_uml_TracedClassifierTemplateParameter_TracedTemplateParameter = Generalization(general=TracedTemplateParameter, specific=umlTrace_uml_TracedClassifierTemplateParameter)
gen_umlTrace_uml_TracedActivityParameterNode_TracedObjectNode = Generalization(general=TracedObjectNode, specific=umlTrace_uml_TracedActivityParameterNode)
gen_umlTrace_uml_TracedParameterSet_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedParameterSet)
gen_umlTrace_uml_TracedDuration_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedDuration)
gen_umlTrace_uml_TracedUsage_TracedDependency = Generalization(general=TracedDependency, specific=umlTrace_uml_TracedUsage)
gen_umlTrace_uml_TracedLiteralUnlimitedNatural_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralUnlimitedNatural)
gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedAction = Generalization(general=uml_TracedAction, specific=umlTrace_uml_TracedStructuredActivityNode)
gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedStructuredActivityNode)
gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedActivityGroup = Generalization(general=uml_TracedActivityGroup, specific=umlTrace_uml_TracedStructuredActivityNode)
gen_umlTrace_uml_TracedClass_uml_TracedEncapsulatedClassifier = Generalization(general=uml_TracedEncapsulatedClassifier, specific=umlTrace_uml_TracedClass)
gen_umlTrace_uml_TracedClass_uml_TracedBehavioredClassifier = Generalization(general=uml_TracedBehavioredClassifier, specific=umlTrace_uml_TracedClass)
gen_umlTrace_uml_TracedAbstraction_TracedDependency = Generalization(general=TracedDependency, specific=umlTrace_uml_TracedAbstraction)
gen_umlTrace_uml_TracedReadStructuralFeatureAction_TracedStructuralFeatureAction = Generalization(general=TracedStructuralFeatureAction, specific=umlTrace_uml_TracedReadStructuralFeatureAction)
gen_umlTrace_uml_TracedMergeNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedMergeNode)
gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedRedefinableTemplateSignature)
gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedTemplateSignature = Generalization(general=uml_TracedTemplateSignature, specific=umlTrace_uml_TracedRedefinableTemplateSignature)
gen_umlTrace_uml_TracedCreateLinkAction_TracedWriteLinkAction = Generalization(general=TracedWriteLinkAction, specific=umlTrace_uml_TracedCreateLinkAction)
gen_umlTrace_uml_TracedGeneralization_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedGeneralization)
gen_umlTrace_uml_TracedPartDecomposition_TracedInteractionUse = Generalization(general=TracedInteractionUse, specific=umlTrace_uml_TracedPartDecomposition)
gen_umlTrace_uml_TracedTypedElement_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedTypedElement)
gen_umlTrace_uml_TracedOperationTemplateParameter_TracedTemplateParameter = Generalization(general=TracedTemplateParameter, specific=umlTrace_uml_TracedOperationTemplateParameter)
gen_umlTrace_uml_TracedReadLinkObjectEndQualifierAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadLinkObjectEndQualifierAction)
gen_umlTrace_uml_TracedTemplateParameterSubstitution_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateParameterSubstitution)
gen_umlTrace_uml_TracedExtend_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedExtend)
gen_umlTrace_uml_TracedExtend_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedExtend)
gen_umlTrace_uml_TracedReadVariableAction_TracedVariableAction = Generalization(general=TracedVariableAction, specific=umlTrace_uml_TracedReadVariableAction)
gen_umlTrace_uml_TracedMessage_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedMessage)
gen_umlTrace_uml_TracedQualifierValue_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedQualifierValue)
gen_umlTrace_uml_TracedInitialNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedInitialNode)
gen_umlTrace_uml_TracedLiteralInteger_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralInteger)
gen_umlTrace_uml_TracedClearVariableAction_TracedVariableAction = Generalization(general=TracedVariableAction, specific=umlTrace_uml_TracedClearVariableAction)
gen_umlTrace_uml_TracedProfileApplication_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedProfileApplication)
gen_umlTrace_uml_TracedLiteralBoolean_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralBoolean)
gen_umlTrace_uml_TracedTemplateParameter_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedTemplateParameter)
gen_umlTrace_uml_TracedConnectorEnd_TracedMultiplicityElement = Generalization(general=TracedMultiplicityElement, specific=umlTrace_uml_TracedConnectorEnd)
gen_umlTrace_uml_TracedParameterableElement_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedParameterableElement)
gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedOccurrenceSpecification = Generalization(general=uml_TracedOccurrenceSpecification, specific=umlTrace_uml_TracedMessageOccurrenceSpecification)
gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedMessageEnd = Generalization(general=uml_TracedMessageEnd, specific=umlTrace_uml_TracedMessageOccurrenceSpecification)
gen_umlTrace_uml_TracedDurationConstraint_TracedIntervalConstraint = Generalization(general=TracedIntervalConstraint, specific=umlTrace_uml_TracedDurationConstraint)
gen_umlTrace_uml_TracedImage_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedImage)
gen_umlTrace_uml_TracedEncapsulatedClassifier_TracedStructuredClassifier = Generalization(general=TracedStructuredClassifier, specific=umlTrace_uml_TracedEncapsulatedClassifier)
gen_umlTrace_uml_TracedParameter_uml_TracedConnectableElement = Generalization(general=uml_TracedConnectableElement, specific=umlTrace_uml_TracedParameter)
gen_umlTrace_uml_TracedParameter_uml_TracedMultiplicityElement = Generalization(general=uml_TracedMultiplicityElement, specific=umlTrace_uml_TracedParameter)
gen_umlTrace_uml_TracedActionInputPin_TracedInputPin = Generalization(general=TracedInputPin, specific=umlTrace_uml_TracedActionInputPin)
gen_umlTrace_uml_TracedCallOperationAction_TracedCallAction = Generalization(general=TracedCallAction, specific=umlTrace_uml_TracedCallOperationAction)
gen_umlTrace_uml_TracedProfile_TracedPackage = Generalization(general=TracedPackage, specific=umlTrace_uml_TracedProfile)
gen_umlTrace_uml_TracedInterval_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedInterval)
gen_umlTrace_uml_TracedTrigger_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedTrigger)
gen_umlTrace_uml_TracedValuePin_TracedInputPin = Generalization(general=TracedInputPin, specific=umlTrace_uml_TracedValuePin)
gen_umlTrace_uml_TracedReadIsClassifiedObjectAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadIsClassifiedObjectAction)
gen_umlTrace_uml_TracedIntervalConstraint_TracedConstraint = Generalization(general=TracedConstraint, specific=umlTrace_uml_TracedIntervalConstraint)
gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeploymentTarget = Generalization(general=uml_TracedDeploymentTarget, specific=umlTrace_uml_TracedInstanceSpecification)
gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedInstanceSpecification)
gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeployedArtifact = Generalization(general=uml_TracedDeployedArtifact, specific=umlTrace_uml_TracedInstanceSpecification)
gen_umlTrace_uml_TracedDecisionNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedDecisionNode)
gen_umlTrace_uml_TracedValueSpecificationAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedValueSpecificationAction)
gen_umlTrace_uml_TracedRegion_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedRegion)
gen_umlTrace_uml_TracedRegion_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedRegion)
gen_umlTrace_uml_TracedProtocolStateMachine_TracedStateMachine = Generalization(general=TracedStateMachine, specific=umlTrace_uml_TracedProtocolStateMachine)
gen_umlTrace_uml_TracedOutputPin_TracedPin = Generalization(general=TracedPin, specific=umlTrace_uml_TracedOutputPin)
gen_umlTrace_uml_TracedInterruptibleActivityRegion_TracedActivityGroup = Generalization(general=TracedActivityGroup, specific=umlTrace_uml_TracedInterruptibleActivityRegion)
gen_umlTrace_uml_TracedDestroyLinkAction_TracedWriteLinkAction = Generalization(general=TracedWriteLinkAction, specific=umlTrace_uml_TracedDestroyLinkAction)
gen_umlTrace_uml_TracedFinalState_TracedState = Generalization(general=TracedState, specific=umlTrace_uml_TracedFinalState)
gen_umlTrace_uml_TracedActivityGroup_uml_TracedNamedElement = Generalization(general=uml_TracedNamedElement, specific=umlTrace_uml_TracedActivityGroup)
gen_umlTrace_uml_TracedActivityGroup_ActivityContent = Generalization(general=ActivityContent, specific=umlTrace_uml_TracedActivityGroup)
gen_umlTrace_uml_TracedInteractionOperand_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedInteractionOperand)
gen_umlTrace_uml_TracedInteractionOperand_uml_TracedInteractionFragment = Generalization(general=uml_TracedInteractionFragment, specific=umlTrace_uml_TracedInteractionOperand)
gen_umlTrace_uml_TracedActivityEdge_TracedRedefinableElement = Generalization(general=TracedRedefinableElement, specific=umlTrace_uml_TracedActivityEdge)
gen_umlTrace_uml_TracedInformationFlow_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedInformationFlow)
gen_umlTrace_uml_TracedInformationFlow_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedInformationFlow)
gen_umlTrace_uml_TracedPseudostate_TracedVertex = Generalization(general=TracedVertex, specific=umlTrace_uml_TracedPseudostate)
gen_umlTrace_uml_TracedControlNode_TracedActivityNode = Generalization(general=TracedActivityNode, specific=umlTrace_uml_TracedControlNode)
gen_umlTrace_uml_TracedUseCase_TracedBehavioredClassifier = Generalization(general=TracedBehavioredClassifier, specific=umlTrace_uml_TracedUseCase)
gen_umlTrace_uml_TracedReplyAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReplyAction)
gen_umlTrace_uml_TracedCombinedFragment_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedCombinedFragment)
gen_umlTrace_uml_TracedWriteLinkAction_TracedLinkAction = Generalization(general=TracedLinkAction, specific=umlTrace_uml_TracedWriteLinkAction)
gen_umlTrace_uml_TracedClause_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedClause)
gen_umlTrace_uml_TracedInstanceValue_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedInstanceValue)
gen_umlTrace_uml_TracedDependency_uml_TracedPackageableElement = Generalization(general=uml_TracedPackageableElement, specific=umlTrace_uml_TracedDependency)
gen_umlTrace_uml_TracedDependency_uml_TracedDirectedRelationship = Generalization(general=uml_TracedDirectedRelationship, specific=umlTrace_uml_TracedDependency)
gen_umlTrace_uml_TracedTimeExpression_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedTimeExpression)
gen_umlTrace_uml_TracedManifestation_TracedAbstraction = Generalization(general=TracedAbstraction, specific=umlTrace_uml_TracedManifestation)
gen_umlTrace_uml_TracedReadExtentAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadExtentAction)
gen_umlTrace_uml_TracedTransition_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedTransition)
gen_umlTrace_uml_TracedTransition_uml_TracedRedefinableElement = Generalization(general=uml_TracedRedefinableElement, specific=umlTrace_uml_TracedTransition)
gen_umlTrace_uml_TracedLinkEndData_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedLinkEndData)
gen_umlTrace_uml_TracedNode_uml_TracedClass = Generalization(general=uml_TracedClass, specific=umlTrace_uml_TracedNode)
gen_umlTrace_uml_TracedNode_uml_TracedDeploymentTarget = Generalization(general=uml_TracedDeploymentTarget, specific=umlTrace_uml_TracedNode)
gen_umlTrace_uml_TracedPackageMerge_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedPackageMerge)
gen_umlTrace_uml_TracedModel_TracedPackage = Generalization(general=TracedPackage, specific=umlTrace_uml_TracedModel)
gen_umlTrace_uml_TracedObjectFlow_TracedActivityEdge = Generalization(general=TracedActivityEdge, specific=umlTrace_uml_TracedObjectFlow)
gen_umlTrace_uml_TracedEvent_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedEvent)
gen_umlTrace_uml_TracedChangeEvent_TracedEvent = Generalization(general=TracedEvent, specific=umlTrace_uml_TracedChangeEvent)
gen_umlTrace_uml_TracedRedefinableElement_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedRedefinableElement)
gen_umlTrace_uml_TracedDestroyObjectAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedDestroyObjectAction)
gen_umlTrace_uml_TracedForkNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedForkNode)
gen_umlTrace_uml_TracedFinalNode_TracedControlNode = Generalization(general=TracedControlNode, specific=umlTrace_uml_TracedFinalNode)
gen_umlTrace_uml_TracedSignal_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedSignal)
gen_umlTrace_uml_TracedComment_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedComment)
gen_umlTrace_uml_TracedStructuredClassifier_TracedClassifier = Generalization(general=TracedClassifier, specific=umlTrace_uml_TracedStructuredClassifier)
gen_umlTrace_uml_TracedLiteralNull_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralNull)
gen_umlTrace_uml_TracedExpansionNode_TracedObjectNode = Generalization(general=TracedObjectNode, specific=umlTrace_uml_TracedExpansionNode)
gen_umlTrace_uml_TracedReception_TracedBehavioralFeature = Generalization(general=TracedBehavioralFeature, specific=umlTrace_uml_TracedReception)
gen_umlTrace_uml_TracedRaiseExceptionAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedRaiseExceptionAction)
gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedNamespace = Generalization(general=uml_TracedNamespace, specific=umlTrace_uml_TracedBehavioralFeature)
gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedFeature = Generalization(general=uml_TracedFeature, specific=umlTrace_uml_TracedBehavioralFeature)
gen_umlTrace_uml_TracedAddVariableValueAction_TracedWriteVariableAction = Generalization(general=TracedWriteVariableAction, specific=umlTrace_uml_TracedAddVariableValueAction)
gen_umlTrace_uml_TracedClearAssociationAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedClearAssociationAction)
gen_umlTrace_uml_TracedPin_uml_TracedObjectNode = Generalization(general=uml_TracedObjectNode, specific=umlTrace_uml_TracedPin)
gen_umlTrace_uml_TracedPin_uml_TracedMultiplicityElement = Generalization(general=uml_TracedMultiplicityElement, specific=umlTrace_uml_TracedPin)
gen_umlTrace_uml_TracedTestIdentityAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedTestIdentityAction)
gen_umlTrace_uml_TracedControlFlow_TracedActivityEdge = Generalization(general=TracedActivityEdge, specific=umlTrace_uml_TracedControlFlow)
gen_umlTrace_uml_TracedOperation_uml_TracedBehavioralFeature = Generalization(general=uml_TracedBehavioralFeature, specific=umlTrace_uml_TracedOperation)
gen_umlTrace_uml_TracedOperation_uml_TracedParameterableElement = Generalization(general=uml_TracedParameterableElement, specific=umlTrace_uml_TracedOperation)
gen_umlTrace_uml_TracedOperation_uml_TracedTemplateableElement = Generalization(general=uml_TracedTemplateableElement, specific=umlTrace_uml_TracedOperation)
gen_umlTrace_uml_TracedConnectableElement_uml_TracedTypedElement = Generalization(general=uml_TracedTypedElement, specific=umlTrace_uml_TracedConnectableElement)
gen_umlTrace_uml_TracedConnectableElement_uml_TracedParameterableElement = Generalization(general=uml_TracedParameterableElement, specific=umlTrace_uml_TracedConnectableElement)
gen_umlTrace_uml_TracedVertex_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedVertex)
gen_umlTrace_uml_TracedObservation_TracedPackageableElement = Generalization(general=TracedPackageableElement, specific=umlTrace_uml_TracedObservation)
gen_umlTrace_uml_TracedNamespace_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedNamespace)
gen_umlTrace_uml_TracedPackageImport_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedPackageImport)
gen_umlTrace_uml_TracedExecutionOccurrenceSpecification_TracedOccurrenceSpecification = Generalization(general=TracedOccurrenceSpecification, specific=umlTrace_uml_TracedExecutionOccurrenceSpecification)
gen_umlTrace_uml_TracedExceptionHandler_TracedElement = Generalization(general=TracedElement, specific=umlTrace_uml_TracedExceptionHandler)
gen_umlTrace_uml_TracedVariable_uml_TracedConnectableElement = Generalization(general=uml_TracedConnectableElement, specific=umlTrace_uml_TracedVariable)
gen_umlTrace_uml_TracedVariable_uml_TracedMultiplicityElement = Generalization(general=uml_TracedMultiplicityElement, specific=umlTrace_uml_TracedVariable)
gen_umlTrace_uml_TracedInteractionUse_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedInteractionUse)
gen_umlTrace_uml_TracedAssociation_uml_TracedClassifier = Generalization(general=uml_TracedClassifier, specific=umlTrace_uml_TracedAssociation)
gen_umlTrace_uml_TracedAssociation_uml_TracedRelationship = Generalization(general=uml_TracedRelationship, specific=umlTrace_uml_TracedAssociation)
gen_umlTrace_uml_TracedStateInvariant_TracedInteractionFragment = Generalization(general=TracedInteractionFragment, specific=umlTrace_uml_TracedStateInvariant)
gen_umlTrace_uml_TracedLiteralReal_TracedLiteralSpecification = Generalization(general=TracedLiteralSpecification, specific=umlTrace_uml_TracedLiteralReal)
gen_umlTrace_uml_TracedInvocationAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedInvocationAction)
gen_umlTrace_uml_TracedRemoveVariableValueAction_TracedWriteVariableAction = Generalization(general=TracedWriteVariableAction, specific=umlTrace_uml_TracedRemoveVariableValueAction)
gen_umlTrace_uml_TracedDevice_TracedNode = Generalization(general=TracedNode, specific=umlTrace_uml_TracedDevice)
gen_umlTrace_uml_TracedSubstitution_TracedRealization = Generalization(general=TracedRealization, specific=umlTrace_uml_TracedSubstitution)
gen_umlTrace_uml_TracedGate_TracedMessageEnd = Generalization(general=TracedMessageEnd, specific=umlTrace_uml_TracedGate)
gen_umlTrace_uml_TracedDeploymentTarget_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedDeploymentTarget)
gen_umlTrace_uml_TracedGeneralOrdering_TracedNamedElement = Generalization(general=TracedNamedElement, specific=umlTrace_uml_TracedGeneralOrdering)
gen_umlTrace_uml_TracedCallBehaviorAction_TracedCallAction = Generalization(general=TracedCallAction, specific=umlTrace_uml_TracedCallBehaviorAction)
gen_umlTrace_uml_TracedReclassifyObjectAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReclassifyObjectAction)
gen_umlTrace_uml_TracedActivity_TracedBehavior = Generalization(general=TracedBehavior, specific=umlTrace_uml_TracedActivity)
gen_umlTrace_uml_TracedConnectionPointReference_TracedVertex = Generalization(general=TracedVertex, specific=umlTrace_uml_TracedConnectionPointReference)
gen_umlTrace_uml_TracedActionExecutionSpecification_TracedExecutionSpecification = Generalization(general=TracedExecutionSpecification, specific=umlTrace_uml_TracedActionExecutionSpecification)
gen_umlTrace_uml_TracedReadSelfAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedReadSelfAction)
gen_umlTrace_uml_TracedAcceptCallAction_TracedAcceptEventAction = Generalization(general=TracedAcceptEventAction, specific=umlTrace_uml_TracedAcceptCallAction)
gen_umlTrace_uml_TracedLinkEndCreationData_TracedLinkEndData = Generalization(general=TracedLinkEndData, specific=umlTrace_uml_TracedLinkEndCreationData)
gen_umlTrace_uml_TracedTemplateBinding_TracedDirectedRelationship = Generalization(general=TracedDirectedRelationship, specific=umlTrace_uml_TracedTemplateBinding)
gen_umlTrace_uml_TracedClearStructuralFeatureAction_TracedStructuralFeatureAction = Generalization(general=TracedStructuralFeatureAction, specific=umlTrace_uml_TracedClearStructuralFeatureAction)
gen_umlTrace_uml_TracedOpaqueExpression_TracedValueSpecification = Generalization(general=TracedValueSpecification, specific=umlTrace_uml_TracedOpaqueExpression)
gen_umlTrace_uml_TracedFunctionBehavior_TracedOpaqueBehavior = Generalization(general=TracedOpaqueBehavior, specific=umlTrace_uml_TracedFunctionBehavior)
gen_umlTrace_uml_TracedDeploymentSpecification_TracedArtifact = Generalization(general=TracedArtifact, specific=umlTrace_uml_TracedDeploymentSpecification)
gen_umlTrace_uml_TracedActor_TracedBehavioredClassifier = Generalization(general=TracedBehavioredClassifier, specific=umlTrace_uml_TracedActor)
gen_umlTrace_uml_TracedBehaviorExecutionSpecification_TracedExecutionSpecification = Generalization(general=TracedExecutionSpecification, specific=umlTrace_uml_TracedBehaviorExecutionSpecification)
gen_umlTrace_uml_TracedExecutableNode_TracedActivityNode = Generalization(general=TracedActivityNode, specific=umlTrace_uml_TracedExecutableNode)
gen_umlTrace_uml_TracedUnmarshallAction_TracedAction = Generalization(general=TracedAction, specific=umlTrace_uml_TracedUnmarshallAction)
gen_umlTrace_uml_TracedCentralBufferNode_TracedObjectNode = Generalization(general=TracedObjectNode, specific=umlTrace_uml_TracedCentralBufferNode)

# Domain Model
domain_model = DomainModel(
    name="umlTrace",
    types={umlTrace_Trace, umlTrace_State, Steps, TracedObjects, SmallStep, BigStep, IntegerValue_value_IntegerValue_Value, ForkedToken_remainingOffersCount_Value, ForkedToken_baseToken_Value, ForkedToken_baseTokenIsWithdrawn_Value, ExecutionFactory_builtInTypes_Value, ExecutionFactory_primitiveBehaviorPrototypes_Value, ExecutionFactory_locus_ExecutionFactory_Value, Locus_factory_Value, Locus_extensionalValues_Value, Locus_executor_Value, ObjectNodeActivation_offeredTokenCount_Value, SemanticVisitor_runtimeModelElement_Value, ParameterValue_values_ParameterValue_Value, Object_types_Value, Reference_referent_Value, Execution_parameterValues_Value, Execution_context_Value, Element_semanticVisitor_Value, ActivityNodeActivationGroup_nodeActivations_Value, ActivityNodeActivationGroup_activityExecution_Value, ActivityNodeActivationGroup_edgeInstances_Value, Executor_locus_Executor_Value, PrimitiveValue_type_Value, Evaluation_specification_Evaluation_Value, Evaluation_locus_Evaluation_Value, BooleanValue_value_BooleanValue_Value, ParameterValue_parameter_ParameterValue_Value, ActionActivation_pinActivations_Value, ActionActivation_firing_Value, Token_holder_Value, Offer_offeredTokens_Value, FeatureValue_values_FeatureValue_Value, FeatureValue_feature_Value, FeatureValue_position_Value, PinActivation_actionActivation_Value, PinActivation_count_temp_Value, ActivityEdgeInstance_group_ActivityEdgeInstance_Value, ActivityEdgeInstance_offers_Value, ActivityEdgeInstance_target_Value, ObjectToken_value_Value, CallActionActivation_callExecutions_Value, CompoundValue_featureValues_Value, InputParameterValues_name_Value, InputParameterValues_parameterValues_Value, ActivityNodeActivation_heldTokens_Value, ActivityNodeActivation_node_ActivityNodeActivation_Value, ActivityNodeActivation_running_Value, ActivityNodeActivation_isRunning_Value, ActivityNodeActivation_outgoingEdges_Value, ActivityNodeActivation_incomingEdges_Value, ActivityNodeActivation_group_ActivityNodeActivation_Value, ExtensionalValue_locus_ExtensionalValue_Value, ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, ActivityEdgeInstance_source_Value, ActivityExecution_activationGroup_Value, ExecutionEnvironment_locus_ExecutionEnvironment_Value, umlTrace_Steps_SmallStep, Steps_umlTrace_State, umlTrace_Steps_Steps, umlTrace_Steps_BigStep, umlTrace_Values_Object_types_Value, uml_TracedClass, Kernel_TracedObject, Values_umlTrace_State, umlTrace_Values_Reference_referent_Value, umlTrace_Values_IntegerValue_value_IntegerValue_Value, Kernel_TracedIntegerValue, umlTrace_Values_ForkedToken_remainingOffersCount_Value, IntermediateActivities_TracedForkedToken, umlTrace_Values_ForkedToken_baseToken_Value, IntermediateActivities_TracedToken, umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value, Kernel_TracedReference, umlTrace_Values_ExecutionFactory_builtInTypes_Value, uml_TracedPrimitiveType, Loci_TracedExecutionFactory, umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value, BasicBehaviors_TracedOpaqueBehaviorExecution, umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value, Loci_TracedLocus, umlTrace_Values_Locus_factory_Value, umlTrace_Values_Locus_extensionalValues_Value, Kernel_TracedExtensionalValue, umlTrace_Values_Locus_executor_Value, Loci_TracedExecutor, umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value, IntermediateActivities_TracedObjectNodeActivation, umlTrace_Values_SemanticVisitor_runtimeModelElement_Value, uml_TracedElement, umlTrace_Values_ParameterValue_values_ParameterValue_Value, Kernel_TracedValue, BasicBehaviors_TracedParameterValue, umlTrace_Values_ParameterValue_parameter_ParameterValue_Value, uml_TracedParameter, umlTrace_Values_ActionActivation_pinActivations_Value, BasicActions_TracedPinActivation, BasicActions_TracedActionActivation, Loci_TracedSemanticVisitor, umlTrace_Values_Execution_parameterValues_Value, BasicBehaviors_TracedExecution, umlTrace_Values_Execution_context_Value, umlTrace_Values_Element_semanticVisitor_Value, umlTrace_Values_ActionActivation_firing_Value, IntermediateActivities_TracedActivityNodeActivationGroup, umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value, IntermediateActivities_TracedActivityExecution, umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value, IntermediateActivities_TracedActivityEdgeInstance, umlTrace_Values_Executor_locus_Executor_Value, umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value, IntermediateActivities_TracedActivityNodeActivation, Kernel_TracedPrimitiveValue, umlTrace_Values_Evaluation_specification_Evaluation_Value, uml_TracedValueSpecification, Kernel_TracedEvaluation, umlTrace_Values_Evaluation_locus_Evaluation_Value, umlTrace_Values_BooleanValue_value_BooleanValue_Value, Kernel_TracedBooleanValue, umlTrace_Values_PrimitiveValue_type_Value, IntermediateActivities_TracedObjectToken, umlTrace_Values_CallActionActivation_callExecutions_Value, BasicActions_TracedCallActionActivation, umlTrace_Values_CompoundValue_featureValues_Value, Kernel_TracedFeatureValue, Kernel_TracedCompoundValue, umlTrace_Values_Token_holder_Value, umlTrace_Values_ObjectToken_value_Value, IntermediateActivities_TracedOffer, umlTrace_Values_FeatureValue_values_FeatureValue_Value, umlTrace_Values_FeatureValue_feature_Value, uml_TracedStructuralFeature, umlTrace_Values_FeatureValue_position_Value, umlTrace_Values_Offer_offeredTokens_Value, umlTrace_Values_PinActivation_count_temp_Value, umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value, umlTrace_Values_ActivityEdgeInstance_offers_Value, umlTrace_Values_PinActivation_actionActivation_Value, umlTrace_Values_ActivityEdgeInstance_target_Value, umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value, uml_TracedActivityEdge, umlTrace_Values_ActivityEdgeInstance_source_Value, umlTrace_Values_InputParameterValues_parameterValues_Value, umlTrace_Values_ActivityNodeActivation_heldTokens_Value, umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value, uml_TracedActivityNode, umlTrace_Values_InputParameterValues_name_Value, Input_TracedInputParameterValues, umlTrace_Values_ActivityNodeActivation_isRunning_Value, umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value, umlTrace_Values_ActivityNodeActivation_incomingEdges_Value, umlTrace_Values_ActivityNodeActivation_running_Value, umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value, umlTrace_Values_ActivityExecution_activationGroup_Value, umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value, umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value, umlTrace_Traced_TracedObjects, uml_TracedConnector, uml_TracedOpaqueAction, uml_TracedDataType, uml_TracedCommunicationPath, uml_TracedProperty, uml_TracedContinuation, uml_TracedRemoveStructuralFeatureValueAction, uml_TracedSendSignalAction, Loci_TracedExecutionEnvironment, uml_TracedArtifact, IntermediateActivities_TracedJoinNodeActivation, uml_TracedTimeConstraint, uml_TracedInterfaceRealization, uml_TracedActivityFinalNode, uml_TracedDurationObservation, IntermediateActivities_TracedInitialNodeActivation, uml_TracedAcceptEventAction, uml_TracedEnumerationLiteral, uml_TracedAddStructuralFeatureValueAction, uml_TracedOpaqueBehavior, uml_TracedConsiderIgnoreFragment, uml_TracedDataStoreNode, uml_TracedFlowFinalNode, uml_TracedInformationItem, uml_TracedCollaboration, uml_TracedTemplateSignature, uml_TracedBroadcastSignalAction, uml_TracedDeployment, uml_TracedPort, uml_TracedTimeInterval, uml_TracedExtension, uml_TracedReadLinkAction, uml_TracedExpression, uml_TracedProtocolTransition, IntermediateActivities_TracedActivityFinalNodeActivation, uml_TracedPackage, uml_TracedConstraint, uml_TracedGeneralizationSet, uml_TracedReduceAction, uml_TracedInputPin, uml_TracedSequenceNode, uml_TracedTimeEvent, uml_TracedAssociationClass, uml_TracedSlot, uml_TracedSignalEvent, uml_TracedExtensionPoint, uml_TracedJoinNode, BasicActions_TracedOutputPinActivation, uml_TracedStartObjectBehaviorAction, uml_TracedElementImport, uml_TracedCreateObjectAction, uml_TracedInteractionConstraint, uml_TracedComponentRealization, IntermediateActions_TracedValueSpecificationActionActivation, uml_TracedStringExpression, IntermediateActions_TracedReadStructuralFeatureActionActivation, uml_TracedStereotype, uml_TracedInterface, uml_TracedConditionalNode, uml_TracedExecutionEnvironment, uml_TracedOccurrenceSpecification, uml_TracedComponent, uml_TracedExtensionEnd, uml_TracedStateMachine, IntermediateActivities_TracedMergeNodeActivation, uml_TracedInteraction, uml_TracedLiteralString, uml_TracedRealization, uml_TracedReadLinkObjectEndAction, uml_TracedAnyReceiveEvent, uml_TracedConnectableElementTemplateParameter, uml_TracedSendObjectAction, uml_TracedLifeline, uml_TracedTimeObservation, IntermediateActivities_TracedControlToken, uml_TracedCreateLinkObjectAction, uml_TracedExpansionRegion, uml_TracedStartClassifierBehaviorAction, uml_TracedCallEvent, uml_TracedProtocolConformance, uml_TracedEnumeration, uml_TracedCollaborationUse, uml_TracedActivityPartition, uml_TracedLinkEndDestructionData, uml_TracedDurationInterval, uml_TracedLoopNode, uml_TracedState, BasicActions_TracedCallBehaviorActionActivation, IntermediateActions_TracedAddStructuralFeatureValueActionActivation, uml_TracedClassifierTemplateParameter, uml_TracedActivityParameterNode, IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution, uml_TracedInclude, uml_TracedDestructionOccurrenceSpecification, uml_TracedDuration, uml_TracedUsage, uml_TracedLiteralUnlimitedNatural, uml_TracedStructuredActivityNode, uml_TracedAbstraction, BasicActions_TracedOpaqueActionActivation, uml_TracedParameterSet, uml_TracedReadStructuralFeatureAction, uml_TracedMergeNode, uml_TracedRedefinableTemplateSignature, uml_TracedCreateLinkAction, uml_TracedGeneralization, uml_TracedPartDecomposition, Kernel_TracedLiteralBooleanEvaluation, uml_TracedReadLinkObjectEndQualifierAction, uml_TracedTemplateParameterSubstitution, uml_TracedExtend, uml_TracedReadVariableAction, uml_TracedMessage, uml_TracedOperationTemplateParameter, uml_TracedInitialNode, uml_TracedLiteralInteger, uml_TracedClearVariableAction, IntermediateActivities_TracedDecisionNodeActivation, uml_TracedProfileApplication, uml_TracedTemplateParameter, uml_TracedLiteralBoolean, uml_TracedQualifierValue, uml_TracedMessageOccurrenceSpecification, uml_TracedDurationConstraint, uml_TracedImage, uml_TracedActionInputPin, uml_TracedTrigger, uml_TracedConnectorEnd, uml_TracedProfile, uml_TracedInterval, IntermediateActivities_TracedForkNodeActivation, uml_TracedIntervalConstraint, uml_TracedInstanceSpecification, uml_TracedCallOperationAction, IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution, uml_TracedReadIsClassifiedObjectAction, uml_TracedProtocolStateMachine, uml_TracedOutputPin, uml_TracedValuePin, uml_TracedDecisionNode, uml_TracedValueSpecificationAction, uml_TracedRegion, uml_TracedInterruptibleActivityRegion, uml_TracedDestroyLinkAction, IntermediateActivities_TracedActivityParameterNodeActivation, uml_TracedInteractionOperand, uml_TracedInformationFlow, uml_TracedPseudostate, uml_TracedUseCase, uml_TracedReplyAction, uml_TracedFinalState, IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution, uml_TracedCombinedFragment, uml_TracedClause, uml_TracedInstanceValue, uml_TracedDependency, uml_TracedTimeExpression, IntermediateActions_TracedCreateObjectActionActivation, uml_TracedManifestation, uml_TracedReadExtentAction, BasicActions_TracedInputPinActivation, uml_TracedTransition, uml_TracedLinkEndData, uml_TracedNode, uml_TracedPackageMerge, uml_TracedModel, uml_TracedObjectFlow, uml_TracedChangeEvent, uml_TracedForkNode, uml_TracedSignal, uml_TracedComment, uml_TracedLiteralNull, uml_TracedExpansionNode, uml_TracedDestroyObjectAction, uml_TracedRaiseExceptionAction, uml_TracedAddVariableValueAction, uml_TracedClearAssociationAction, uml_TracedTestIdentityAction, uml_TracedReception, uml_TracedOperation, uml_TracedPackageImport, uml_TracedExecutionOccurrenceSpecification, uml_TracedExceptionHandler, uml_TracedVariable, uml_TracedControlFlow, uml_TracedAssociation, uml_TracedStateInvariant, uml_TracedLiteralReal, uml_TracedRemoveVariableValueAction, uml_TracedInteractionUse, uml_TracedGate, uml_TracedGeneralOrdering, uml_TracedCallBehaviorAction, uml_TracedReclassifyObjectAction, uml_TracedDevice, uml_TracedSubstitution, uml_TracedConnectionPointReference, uml_TracedActionExecutionSpecification, uml_TracedReadSelfAction, uml_TracedAcceptCallAction, uml_TracedActivity, uml_TracedTemplateBinding, uml_TracedClearStructuralFeatureAction, uml_TracedLinkEndCreationData, Kernel_TracedLiteralIntegerEvaluation, uml_TracedOpaqueExpression, uml_TracedFunctionBehavior, uml_TracedDeploymentSpecification, uml_TracedBehaviorExecutionSpecification, uml_TracedUnmarshallAction, uml_TracedCentralBufferNode, umlTrace_Kernel_TracedObject, TracedExtensionalValue, uml_TracedActor, umlTrace_Kernel_TracedIntegerValue, TracedPrimitiveValue, umlTrace_Kernel_TracedLiteralEvaluation, TracedEvaluation, umlTrace_Kernel_TracedValue, TracedSemanticVisitor, umlTrace_Kernel_TracedPrimitiveValue, TracedValue, umlTrace_Kernel_TracedEvaluation, umlTrace_Kernel_TracedBooleanValue, umlTrace_Kernel_TracedLiteralBooleanEvaluation, TracedLiteralEvaluation, umlTrace_Kernel_TracedReference, TracedStructuredValue, umlTrace_Kernel_TracedCompoundValue, umlTrace_Kernel_TracedFeatureValue, umlTrace_Kernel_TracedStructuredValue, umlTrace_Kernel_TracedExtensionalValue, TracedCompoundValue, umlTrace_Kernel_TracedLiteralIntegerEvaluation, umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution, TracedExecution, umlTrace_BasicBehaviors_TracedParameterValue, umlTrace_BasicBehaviors_TracedExecution, TracedObject, umlTrace_IntermediateActivities_TracedForkedToken, TracedToken, umlTrace_IntermediateActivities_TracedJoinNodeActivation, TracedControlNodeActivation, umlTrace_IntermediateActivities_TracedInitialNodeActivation, umlTrace_IntermediateActivities_TracedObjectNodeActivation, TracedActivityNodeActivation, umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation, umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup, umlTrace_IntermediateActivities_TracedMergeNodeActivation, umlTrace_IntermediateActivities_TracedControlToken, umlTrace_IntermediateActivities_TracedObjectToken, umlTrace_IntermediateActivities_TracedDecisionNodeActivation, umlTrace_IntermediateActivities_TracedOffer, umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation, TracedObjectNodeActivation, umlTrace_IntermediateActivities_TracedActivityEdgeInstance, umlTrace_IntermediateActivities_TracedActivityNodeActivation, umlTrace_IntermediateActivities_TracedForkNodeActivation, umlTrace_IntermediateActivities_TracedToken, umlTrace_IntermediateActivities_TracedActivityExecution, umlTrace_Loci_TracedExecutionFactory, umlTrace_Loci_TracedLocus, umlTrace_Loci_TracedSemanticVisitor, umlTrace_Loci_TracedExecutor, umlTrace_IntermediateActivities_TracedControlNodeActivation, umlTrace_IntermediateActions_TracedValueSpecificationActionActivation, umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation, TracedStructuralFeatureActionActivation, umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation, TracedWriteStructuralFeatureActionActivation, umlTrace_IntermediateActions_TracedCreateObjectActionActivation, umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation, umlTrace_BasicActions_TracedActionActivation, umlTrace_BasicActions_TracedOutputPinActivation, TracedPinActivation, umlTrace_BasicActions_TracedCallBehaviorActionActivation, TracedCallActionActivation, umlTrace_BasicActions_TracedOpaqueActionActivation, umlTrace_BasicActions_TracedCallActionActivation, TracedInvocationActionActivation, umlTrace_Loci_TracedExecutionEnvironment, umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation, TracedActionActivation, umlTrace_BasicActions_TracedPinActivation, umlTrace_BasicActions_TracedInputPinActivation, umlTrace_BasicActions_TracedInvocationActionActivation, umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution, umlTrace_Input_TracedInputParameterValues, umlTrace_uml_TracedStructuralFeature, uml_TracedFeature, uml_TracedTypedElement, uml_TracedMultiplicityElement, umlTrace_uml_TracedConnector, TracedFeature, uml_TracedBehavior, uml_umlTrace_Connector, umlTrace_uml_TracedOpaqueAction, TracedAction, umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution, TracedOpaqueBehaviorExecution, umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution, umlTrace_uml_TracedDataType, TracedClassifier, uml_umlTrace_DataType, umlTrace_uml_TracedCommunicationPath, TracedAssociation, umlTrace_uml_TracedLinkAction, umlTrace_uml_TracedProperty, uml_TracedConnectableElement, uml_TracedDeploymentTarget, uml_umlTrace_OpaqueAction, uml_umlTrace_Property, umlTrace_uml_TracedContinuation, TracedInteractionFragment, uml_umlTrace_Continuation, umlTrace_uml_TracedRemoveStructuralFeatureValueAction, TracedWriteStructuralFeatureAction, uml_umlTrace_RemoveStructuralFeatureValueAction, umlTrace_uml_TracedSendSignalAction, TracedInvocationAction, umlTrace_uml_TracedOpaqueBehavior, TracedBehavior, umlTrace_uml_TracedArtifact, uml_TracedClassifier, uml_TracedDeployedArtifact, uml_umlTrace_Artifact, umlTrace_uml_TracedTimeConstraint, TracedIntervalConstraint, umlTrace_uml_TracedInterfaceRealization, TracedRealization, uml_TracedBehavioredClassifier, umlTrace_uml_TracedObjectNode, uml_umlTrace_SendSignalAction, umlTrace_uml_TracedActivityFinalNode, TracedFinalNode, uml_umlTrace_ActivityFinalNode, umlTrace_uml_TracedDurationObservation, TracedObservation, uml_TracedNamedElement, uml_umlTrace_DurationObservation, umlTrace_uml_TracedAcceptEventAction, uml_umlTrace_AcceptEventAction, umlTrace_uml_TracedEnumerationLiteral, TracedInstanceSpecification, umlTrace_uml_TracedAddStructuralFeatureValueAction, uml_umlTrace_AddStructuralFeatureValueAction, umlTrace_uml_TracedExpression, TracedValueSpecification, uml_umlTrace_Expression, umlTrace_uml_TracedConsiderIgnoreFragment, TracedCombinedFragment, umlTrace_uml_TracedDataStoreNode, TracedCentralBufferNode, umlTrace_uml_TracedFlowFinalNode, uml_umlTrace_FlowFinalNode, umlTrace_uml_TracedInteractionFragment, TracedNamedElement, umlTrace_uml_TracedClassifier, umlTrace_uml_TracedReadLinkAction, TracedLinkAction, uml_umlTrace_ReadLinkAction, uml_TracedNamespace, uml_TracedRedefinableElement, uml_TracedType, uml_TracedTemplateableElement, umlTrace_uml_TracedInformationItem, uml_umlTrace_InformationItem, umlTrace_uml_TracedCollaboration, uml_TracedStructuredClassifier, uml_umlTrace_Collaboration, umlTrace_uml_TracedMessageEnd, umlTrace_uml_TracedTemplateSignature, TracedElement, uml_umlTrace_TemplateSignature, umlTrace_uml_TracedBroadcastSignalAction, uml_umlTrace_BroadcastSignalAction, umlTrace_uml_TracedDeployment, TracedDependency, umlTrace_uml_TracedPort, TracedProperty, umlTrace_uml_TracedTimeInterval, TracedInterval, umlTrace_uml_TracedAction, TracedExecutableNode, umlTrace_uml_TracedExtension, umlTrace_uml_TracedDirectedRelationship, TracedRelationship, umlTrace_uml_TracedTimeEvent, TracedEvent, uml_umlTrace_TimeEvent, umlTrace_uml_TracedPackageableElement, uml_TracedParameterableElement, umlTrace_uml_TracedType, TracedPackageableElement, umlTrace_uml_TracedProtocolTransition, TracedTransition, umlTrace_uml_TracedPackage, uml_TracedPackageableElement, uml_umlTrace_Package, umlTrace_uml_TracedBehavioredClassifier, umlTrace_uml_TracedStructuralFeatureAction, umlTrace_uml_TracedConstraint, uml_umlTrace_Constraint, umlTrace_uml_TracedMultiplicityElement, umlTrace_uml_TracedLiteralSpecification, umlTrace_uml_TracedGeneralizationSet, umlTrace_uml_TracedReduceAction, uml_umlTrace_ReduceAction, umlTrace_uml_TracedInputPin, TracedPin, uml_umlTrace_InputPin, umlTrace_uml_TracedSequenceNode, TracedStructuredActivityNode, uml_TracedExecutableNode, umlTrace_uml_TracedFeature, TracedRedefinableElement, umlTrace_uml_TracedInteractionConstraint, TracedConstraint, uml_umlTrace_GeneralizationSet, umlTrace_uml_TracedElement, TracedEModelElement, umlTrace_uml_TracedComponentRealization, umlTrace_uml_TracedAssociationClass, umlTrace_uml_TracedSlot, umlTrace_uml_TracedWriteStructuralFeatureAction, TracedStructuralFeatureAction, uml_umlTrace_Slot, umlTrace_uml_TracedSignalEvent, TracedMessageEvent, uml_umlTrace_SignalEvent, umlTrace_uml_TracedExtensionPoint, uml_umlTrace_ExtensionPoint, umlTrace_uml_TracedJoinNode, TracedControlNode, uml_umlTrace_JoinNode, umlTrace_uml_TracedStartObjectBehaviorAction, TracedCallAction, uml_umlTrace_StartObjectBehaviorAction, uml_umlTrace_ElementImport, umlTrace_uml_TracedCreateObjectAction, uml_umlTrace_CreateObjectAction, umlTrace_uml_TracedExecutionEnvironment, TracedNode, umlTrace_uml_TracedOccurrenceSpecification, uml_umlTrace_OccurrenceSpecification, umlTrace_uml_TracedStringExpression, umlTrace_uml_TracedElementImport, TracedDirectedRelationship, umlTrace_uml_TracedInterface, uml_umlTrace_Interface, umlTrace_uml_TracedConditionalNode, umlTrace_uml_TracedDeployedArtifact, umlTrace_uml_TracedStereotype, TracedClass, uml_umlTrace_ReadLinkObjectEndAction, umlTrace_uml_TracedAnyReceiveEvent, uml_umlTrace_AnyReceiveEvent, umlTrace_uml_TracedNamedElement, umlTrace_uml_TracedComponent, umlTrace_uml_TracedReadLinkObjectEndAction, umlTrace_uml_TracedExtensionEnd, umlTrace_uml_TracedStateMachine, umlTrace_uml_TracedValueSpecification, umlTrace_uml_TracedInteraction, uml_TracedInteractionFragment, umlTrace_uml_TracedLiteralString, TracedLiteralSpecification, uml_umlTrace_LiteralString, umlTrace_uml_TracedRealization, TracedAbstraction, umlTrace_uml_TracedStartClassifierBehaviorAction, uml_umlTrace_StartClassifierBehaviorAction, umlTrace_uml_TracedMessageEvent, umlTrace_uml_TracedCallEvent, uml_umlTrace_CallEvent, umlTrace_uml_TracedConnectableElementTemplateParameter, TracedTemplateParameter, umlTrace_uml_TracedRelationship, umlTrace_uml_TracedSendObjectAction, uml_TracedAction, umlTrace_uml_TracedLifeline, uml_umlTrace_Lifeline, umlTrace_uml_TracedExecutionSpecification, umlTrace_uml_TracedTimeObservation, uml_umlTrace_SendObjectAction, umlTrace_uml_TracedExpansionRegion, umlTrace_uml_TracedWriteVariableAction, TracedVariableAction, umlTrace_uml_TracedLoopNode, uml_umlTrace_TimeObservation, umlTrace_uml_TracedCreateLinkObjectAction, TracedCreateLinkAction, umlTrace_uml_TracedPrimitiveType, TracedDataType, umlTrace_uml_TracedProtocolConformance, uml_umlTrace_ProtocolConformance, umlTrace_uml_TracedEnumeration, umlTrace_uml_TracedCollaborationUse, umlTrace_uml_TracedActivityPartition, TracedActivityGroup, uml_umlTrace_ActivityPartition, umlTrace_uml_TracedVariableAction, umlTrace_uml_TracedLinkEndDestructionData, TracedLinkEndData, umlTrace_uml_TracedDurationInterval, umlTrace_uml_TracedInclude, uml_TracedDirectedRelationship, uml_umlTrace_CollaborationUse, uml_umlTrace_Include, umlTrace_uml_TracedActivityNode, ActivityContent, uml_TracedActivityGroup, umlTrace_uml_TracedDestructionOccurrenceSpecification, TracedMessageOccurrenceSpecification, umlTrace_uml_TracedState, uml_TracedVertex, umlTrace_uml_TracedCallAction, umlTrace_uml_TracedTemplateableElement, umlTrace_uml_TracedBehavior, uml_TracedBehavioralFeature, uml_umlTrace_State, umlTrace_uml_TracedClassifierTemplateParameter, umlTrace_uml_TracedActivityParameterNode, TracedObjectNode, uml_umlTrace_ActivityParameterNode, umlTrace_uml_TracedParameterSet, uml_umlTrace_ParameterSet, umlTrace_uml_TracedDuration, uml_TracedObservation, uml_umlTrace_Class, umlTrace_uml_TracedUsage, umlTrace_uml_TracedLiteralUnlimitedNatural, uml_umlTrace_LiteralUnlimitedNatural, umlTrace_uml_TracedStructuredActivityNode, uml_umlTrace_Duration, umlTrace_uml_TracedClass, uml_TracedEncapsulatedClassifier, uml_umlTrace_StructuredActivityNode, umlTrace_uml_TracedAbstraction, umlTrace_uml_TracedReadStructuralFeatureAction, uml_umlTrace_ReadStructuralFeatureAction, umlTrace_uml_TracedMergeNode, uml_umlTrace_MergeNode, umlTrace_uml_TracedRedefinableTemplateSignature, umlTrace_uml_TracedCreateLinkAction, TracedWriteLinkAction, uml_umlTrace_CreateLinkAction, umlTrace_uml_TracedGeneralization, uml_umlTrace_Generalization, umlTrace_uml_TracedPartDecomposition, TracedInteractionUse, umlTrace_uml_TracedTypedElement, umlTrace_uml_TracedOperationTemplateParameter, umlTrace_uml_TracedReadLinkObjectEndQualifierAction, uml_umlTrace_ReadLinkObjectEndQualifierAction, umlTrace_uml_TracedTemplateParameterSubstitution, uml_umlTrace_TemplateParameterSubstitution, umlTrace_uml_TracedExtend, uml_umlTrace_Extend, umlTrace_uml_TracedReadVariableAction, uml_umlTrace_ReadVariableAction, umlTrace_uml_TracedMessage, uml_TracedMessageEnd, umlTrace_uml_TracedQualifierValue, uml_umlTrace_QualifierValue, umlTrace_uml_TracedInitialNode, uml_umlTrace_InitialNode, umlTrace_uml_TracedLiteralInteger, uml_umlTrace_LiteralInteger, umlTrace_uml_TracedClearVariableAction, uml_umlTrace_ClearVariableAction, umlTrace_uml_TracedProfileApplication, uml_umlTrace_Message, umlTrace_uml_TracedLiteralBoolean, uml_umlTrace_LiteralBoolean, umlTrace_uml_TracedTemplateParameter, uml_umlTrace_TemplateParameter, umlTrace_uml_TracedConnectorEnd, TracedMultiplicityElement, uml_umlTrace_ProfileApplication, umlTrace_uml_TracedParameterableElement, umlTrace_uml_TracedMessageOccurrenceSpecification, umlTrace_uml_TracedDurationConstraint, umlTrace_uml_TracedImage, uml_umlTrace_Image, umlTrace_uml_TracedEncapsulatedClassifier, TracedStructuredClassifier, umlTrace_uml_TracedParameter, uml_umlTrace_Parameter, umlTrace_uml_TracedActionInputPin, TracedInputPin, uml_umlTrace_ConnectorEnd, uml_umlTrace_Trigger, umlTrace_uml_TracedCallOperationAction, uml_umlTrace_CallOperationAction, umlTrace_uml_TracedProfile, TracedPackage, umlTrace_uml_TracedInterval, uml_umlTrace_Interval, umlTrace_uml_TracedTrigger, uml_TracedEvent, uml_umlTrace_InstanceSpecification, umlTrace_uml_TracedValuePin, umlTrace_uml_TracedReadIsClassifiedObjectAction, uml_umlTrace_ReadIsClassifiedObjectAction, umlTrace_uml_TracedIntervalConstraint, umlTrace_uml_TracedInstanceSpecification, uml_umlTrace_OutputPin, umlTrace_uml_TracedDecisionNode, uml_umlTrace_DecisionNode, umlTrace_uml_TracedValueSpecificationAction, uml_umlTrace_ValueSpecificationAction, umlTrace_uml_TracedRegion, umlTrace_uml_TracedProtocolStateMachine, TracedStateMachine, umlTrace_uml_TracedOutputPin, uml_umlTrace_Region, umlTrace_uml_TracedInterruptibleActivityRegion, uml_umlTrace_InterruptibleActivityRegion, umlTrace_uml_TracedDestroyLinkAction, uml_umlTrace_DestroyLinkAction, umlTrace_uml_TracedFinalState, TracedState, umlTrace_uml_TracedActivityGroup, umlTrace_uml_TracedInteractionOperand, uml_umlTrace_InteractionOperand, umlTrace_uml_TracedActivityEdge, umlTrace_uml_TracedInformationFlow, uml_TracedRelationship, uml_umlTrace_InformationFlow, umlTrace_uml_TracedPseudostate, TracedVertex, uml_umlTrace_Pseudostate, umlTrace_uml_TracedControlNode, TracedActivityNode, umlTrace_uml_TracedUseCase, TracedBehavioredClassifier, uml_umlTrace_UseCase, umlTrace_uml_TracedReplyAction, uml_umlTrace_ReplyAction, umlTrace_uml_TracedCombinedFragment, uml_umlTrace_CombinedFragment, umlTrace_uml_TracedWriteLinkAction, umlTrace_uml_TracedClause, uml_umlTrace_Clause, umlTrace_uml_TracedInstanceValue, uml_umlTrace_InstanceValue, umlTrace_uml_TracedDependency, uml_umlTrace_Dependency, umlTrace_uml_TracedTimeExpression, uml_umlTrace_TimeExpression, umlTrace_uml_TracedManifestation, umlTrace_uml_TracedReadExtentAction, uml_umlTrace_ReadExtentAction, umlTrace_uml_TracedTransition, uml_umlTrace_Transition, umlTrace_uml_TracedLinkEndData, uml_umlTrace_ObjectFlow, uml_umlTrace_LinkEndData, umlTrace_uml_TracedNode, umlTrace_uml_TracedPackageMerge, uml_umlTrace_PackageMerge, umlTrace_uml_TracedModel, umlTrace_uml_TracedObjectFlow, TracedActivityEdge, umlTrace_uml_TracedEvent, umlTrace_uml_TracedChangeEvent, uml_umlTrace_ChangeEvent, umlTrace_uml_TracedRedefinableElement, umlTrace_uml_TracedDestroyObjectAction, uml_umlTrace_DestroyObjectAction, umlTrace_uml_TracedForkNode, uml_umlTrace_ForkNode, umlTrace_uml_TracedFinalNode, umlTrace_uml_TracedSignal, uml_umlTrace_Signal, umlTrace_uml_TracedComment, uml_umlTrace_Comment, umlTrace_uml_TracedStructuredClassifier, umlTrace_uml_TracedLiteralNull, uml_umlTrace_LiteralNull, umlTrace_uml_TracedExpansionNode, uml_umlTrace_ExpansionNode, umlTrace_uml_TracedReception, TracedBehavioralFeature, uml_umlTrace_Reception, umlTrace_uml_TracedRaiseExceptionAction, uml_umlTrace_RaiseExceptionAction, umlTrace_uml_TracedBehavioralFeature, umlTrace_uml_TracedAddVariableValueAction, TracedWriteVariableAction, uml_umlTrace_AddVariableValueAction, umlTrace_uml_TracedClearAssociationAction, uml_umlTrace_ClearAssociationAction, umlTrace_uml_TracedPin, uml_TracedObjectNode, umlTrace_uml_TracedTestIdentityAction, uml_umlTrace_TestIdentityAction, umlTrace_uml_TracedControlFlow, uml_umlTrace_ControlFlow, umlTrace_uml_TracedOperation, uml_umlTrace_Operation, umlTrace_uml_TracedConnectableElement, umlTrace_uml_TracedVertex, umlTrace_uml_TracedObservation, umlTrace_uml_TracedNamespace, umlTrace_uml_TracedPackageImport, uml_umlTrace_PackageImport, umlTrace_uml_TracedExecutionOccurrenceSpecification, TracedOccurrenceSpecification, uml_TracedExecutionSpecification, umlTrace_uml_TracedExceptionHandler, uml_umlTrace_ExceptionHandler, umlTrace_uml_TracedVariable, uml_umlTrace_Variable, umlTrace_uml_TracedInteractionUse, uml_umlTrace_InteractionUse, umlTrace_uml_TracedAssociation, uml_umlTrace_Association, umlTrace_uml_TracedStateInvariant, uml_umlTrace_StateInvariant, umlTrace_uml_TracedLiteralReal, uml_umlTrace_LiteralReal, umlTrace_uml_TracedInvocationAction, umlTrace_uml_TracedRemoveVariableValueAction, uml_umlTrace_RemoveVariableValueAction, umlTrace_uml_TracedDevice, umlTrace_uml_TracedSubstitution, umlTrace_uml_TracedGate, TracedMessageEnd, uml_umlTrace_Gate, umlTrace_uml_TracedDeploymentTarget, umlTrace_uml_TracedGeneralOrdering, uml_umlTrace_GeneralOrdering, umlTrace_uml_TracedCallBehaviorAction, uml_umlTrace_CallBehaviorAction, umlTrace_uml_TracedReclassifyObjectAction, uml_umlTrace_ReclassifyObjectAction, umlTrace_uml_TracedActivity, umlTrace_uml_TracedConnectionPointReference, uml_umlTrace_ConnectionPointReference, umlTrace_uml_TracedActionExecutionSpecification, TracedExecutionSpecification, uml_umlTrace_ActionExecutionSpecification, umlTrace_uml_TracedReadSelfAction, uml_umlTrace_ReadSelfAction, umlTrace_uml_TracedAcceptCallAction, TracedAcceptEventAction, umlTrace_uml_TracedLinkEndCreationData, umlTrace_uml_TracedTemplateBinding, uml_umlTrace_TemplateBinding, umlTrace_uml_TracedClearStructuralFeatureAction, uml_umlTrace_ClearStructuralFeatureAction, umlTrace_uml_TracedOpaqueExpression, uml_umlTrace_OpaqueExpression, umlTrace_uml_TracedFunctionBehavior, TracedOpaqueBehavior, umlTrace_uml_TracedDeploymentSpecification, TracedArtifact, umlTrace_uml_TracedActor, uml_umlTrace_Actor, umlTrace_uml_TracedBehaviorExecutionSpecification, uml_umlTrace_BehaviorExecutionSpecification, umlTrace_uml_TracedExecutableNode, umlTrace_uml_TracedUnmarshallAction, uml_umlTrace_UnmarshallAction, umlTrace_uml_TracedCentralBufferNode, uml_umlTrace_CentralBufferNode, umlTrace_ecore_TracedEModelElement, ecore_umlTrace_EAnnotation},
    associations={statesTrace0, steps1, tracedObjects3, followingStep5, integerValue_value_IntegerValue_Values15, forkedToken_remainingOffersCount_Values17, forkedToken_baseToken_Values19, forkedToken_baseTokenIsWithdrawn_Values21, executionFactory_builtInTypes_Values23, executionFactory_primitiveBehaviorPrototypes_Values25, executionFactory_locus_ExecutionFactory_Values27, locus_factory_Values29, locus_extensionalValues_Values31, locus_executor_Values33, objectNodeActivation_offeredTokenCount_Values35, semanticVisitor_runtimeModelElement_Values37, parameterValue_values_ParameterValue_Values39, startedBigSteps7, endedBigSteps9, object_types_Values12, reference_referent_Values13, actionActivation_firing_Values45, execution_parameterValues_Values47, execution_context_Values49, element_semanticVisitor_Values51, activityNodeActivationGroup_nodeActivations_Values53, activityNodeActivationGroup_activityExecution_Values55, activityNodeActivationGroup_edgeInstances_Values57, executor_locus_Executor_Values59, primitiveValue_type_Values61, evaluation_specification_Evaluation_Values63, evaluation_locus_Evaluation_Values65, booleanValue_value_BooleanValue_Values67, parameterValue_parameter_ParameterValue_Values41, actionActivation_pinActivations_Values43, token_holder_Values75, offer_offeredTokens_Values77, featureValue_values_FeatureValue_Values79, featureValue_feature_Values81, featureValue_position_Values83, pinActivation_actionActivation_Values85, pinActivation_count_temp_Values87, activityEdgeInstance_group_ActivityEdgeInstance_Values89, activityEdgeInstance_offers_Values91, objectToken_value_Values69, callActionActivation_callExecutions_Values71, compoundValue_featureValues_Values73, inputParameterValues_name_Values99, inputParameterValues_parameterValues_Values101, activityNodeActivation_heldTokens_Values103, activityNodeActivation_node_ActivityNodeActivation_Values105, activityNodeActivation_running_Values107, activityNodeActivation_isRunning_Values109, activityNodeActivation_outgoingEdges_Values111, activityNodeActivation_incomingEdges_Values113, activityNodeActivation_group_ActivityNodeActivation_Values115, extensionalValue_locus_ExtensionalValue_Values117, activityEdgeInstance_target_Values93, activityEdgeInstance_edge_ActivityEdgeInstance_Values95, activityEdgeInstance_source_Values97, activityExecution_activationGroup_Values119, executionEnvironment_locus_ExecutionEnvironment_Values121, precedingState123, startingState124, endingState126, types128, parent129, states130, parent138, states141, parent143, states146, baseToken148, parent149, states152, referent132, parent133, states136, states157, builtInTypes159, parent160, states163, primitiveBehaviorPrototypes165, parent166, states169, locus_ExecutionFactory171, parent172, states175, parent154, extensionalValues183, parent184, states187, executor189, parent190, states193, parent195, states198, factory177, parent178, states181, values_ParameterValue206, parent207, states210, parameter_ParameterValue212, parent213, states216, pinActivations218, parent219, states222, runtimeModelElement200, parent201, states204, parent224, states227, parameterValues229, parent230, states233, context235, parent237, states240, semanticVisitor242, parent248, states251, activityExecution253, parent254, states257, edgeInstances259, parent260, states263, locus_Executor265, parent243, parent267, states245, nodeActivations247, type272, parent274, states277, specification_Evaluation279, parent280, states283, locus_Evaluation285, parent287, states290, parent292, states270, parent299, states302, callExecutions304, parent305, states308, featureValues310, parent311, states314, holder316, parent318, states295, value297, offeredTokens323, parent325, states328, values_FeatureValue330, parent332, states335, feature337, parent338, states341, states321, actionActivation348, parent349, states352, parent354, states357, group_ActivityEdgeInstance359, parent360, states363, parent343, states346, target371, parent373, states376, edge_ActivityEdgeInstance378, parent379, states382, source384, parent386, offers365, states389, parent366, states369, parent391, states394, parameterValues396, parent398, states401, heldTokens403, parent405, states408, node_ActivityNodeActivation410, parent411, parent416, states419, parent421, states424, outgoingEdges426, parent428, states431, incomingEdges433, states414, group_ActivityNodeActivation440, parent442, states445, locus_ExtensionalValue447, parent449, states452, activationGroup454, parent456, states459, parent435, states438, kernel_tracedObjects468, uml_tracedConnectors470, uml_tracedOpaqueActions472, uml_tracedDataTypes474, uml_tracedCommunicationPaths476, kernel_tracedReferences478, uml_tracedPropertys480, uml_tracedContinuations482, uml_tracedRemoveStructuralFeatureValueActions484, uml_tracedSendSignalActions486, kernel_tracedIntegerValues488, locus_ExecutionEnvironment461, parent463, states466, loci_tracedLocuss497, uml_tracedArtifacts500, intermediateActivities_tracedJoinNodeActivations502, uml_tracedTimeConstraints504, uml_tracedInterfaceRealizations506, uml_tracedActivityFinalNodes508, uml_tracedDurationObservations510, intermediateActivities_tracedInitialNodeActivations512, uml_tracedAcceptEventActions514, uml_tracedEnumerationLiterals516, uml_tracedAddStructuralFeatureValueActions518, intermediateActivities_tracedForkedTokens490, uml_tracedOpaqueBehaviors492, loci_tracedExecutionFactorys494, uml_tracedConsiderIgnoreFragments524, uml_tracedDataStoreNodes526, uml_tracedFlowFinalNodes528, uml_tracedInformationItems530, uml_tracedCollaborations532, uml_tracedTemplateSignatures534, uml_tracedBroadcastSignalActions536, uml_tracedDeployments538, uml_tracedPorts540, uml_tracedTimeIntervals542, uml_tracedReadLinkActions520, uml_tracedExpressions522, uml_tracedTimeEvents549, basicBehaviors_tracedParameterValues551, uml_tracedProtocolTransitions554, intermediateActivities_tracedActivityFinalNodeActivations556, uml_tracedPackages558, uml_tracedConstraints560, uml_tracedGeneralizationSets562, uml_tracedReduceActions564, uml_tracedInputPins566, uml_tracedExtensions544, loci_tracedSemanticVisitors546, uml_tracedComponentRealizations572, uml_tracedAssociationClasss574, uml_tracedSlots576, uml_tracedSignalEvents578, uml_tracedExtensionPoints580, uml_tracedJoinNodes582, basicActions_tracedOutputPinActivations584, uml_tracedStartObjectBehaviorActions586, uml_tracedElementImports588, uml_tracedSequenceNodes568, uml_tracedInteractionConstraints570, uml_tracedOccurrenceSpecifications594, intermediateActivities_tracedActivityNodeActivationGroups596, intermediateActions_tracedValueSpecificationActionActivations599, uml_tracedStringExpressions601, loci_tracedExecutors603, intermediateActions_tracedReadStructuralFeatureActionActivations606, uml_tracedStereotypes608, uml_tracedInterfaces610, uml_tracedConditionalNodes612, uml_tracedCreateObjectActions590, uml_tracedExecutionEnvironments592, uml_tracedComponents618, uml_tracedExtensionEnds620, uml_tracedStateMachines622, intermediateActivities_tracedMergeNodeActivations624, uml_tracedInteractions626, uml_tracedLiteralStrings628, uml_tracedRealizations630, uml_tracedReadLinkObjectEndActions614, uml_tracedAnyReceiveEvents616, uml_tracedConnectableElementTemplateParameters636, uml_tracedSendObjectActions638, uml_tracedLifelines640, uml_tracedTimeObservations642, intermediateActivities_tracedControlTokens644, uml_tracedCreateLinkObjectActions646, uml_tracedExpansionRegions648, uml_tracedStartClassifierBehaviorActions632, uml_tracedCallEvents634, uml_tracedPrimitiveTypes654, uml_tracedProtocolConformances657, uml_tracedEnumerations659, uml_tracedCollaborationUses661, uml_tracedActivityPartitions663, uml_tracedLinkEndDestructionDatas665, uml_tracedDurationIntervals667, kernel_tracedBooleanValues650, uml_tracedLoopNodes652, uml_tracedStates673, intermediateActivities_tracedObjectTokens675, basicActions_tracedCallBehaviorActionActivations677, intermediateActions_tracedAddStructuralFeatureValueActionActivations679, uml_tracedClassifierTemplateParameters681, uml_tracedActivityParameterNodes683, integerFunctions_tracedIntegerLessFunctionBehaviorExecutions685, uml_tracedIncludes669, uml_tracedDestructionOccurrenceSpecifications671, uml_tracedDurations689, uml_tracedClasss691, uml_tracedUsages694, uml_tracedLiteralUnlimitedNaturals696, uml_tracedStructuredActivityNodes698, uml_tracedAbstractions700, uml_tracedParameterSets687, uml_tracedReadStructuralFeatureActions706, uml_tracedMergeNodes708, uml_tracedRedefinableTemplateSignatures710, uml_tracedCreateLinkActions712, uml_tracedGeneralizations714, uml_tracedPartDecompositions716, basicActions_tracedOpaqueActionActivations702, kernel_tracedLiteralBooleanEvaluations704, uml_tracedOperationTemplateParameters718, uml_tracedReadLinkObjectEndQualifierActions720, uml_tracedTemplateParameterSubstitutions722, uml_tracedExtends724, uml_tracedReadVariableActions726, uml_tracedMessages728, uml_tracedInitialNodes734, uml_tracedLiteralIntegers736, uml_tracedClearVariableActions738, intermediateActivities_tracedDecisionNodeActivations740, uml_tracedProfileApplications742, uml_tracedLiteralBooleans730, uml_tracedQualifierValues732, uml_tracedMessageOccurrenceSpecifications748, uml_tracedDurationConstraints750, uml_tracedImages752, uml_tracedParameters754, uml_tracedActionInputPins757, uml_tracedTriggers759, uml_tracedTemplateParameters744, uml_tracedConnectorEnds746, uml_tracedProfiles763, uml_tracedIntervals765, intermediateActivities_tracedForkNodeActivations767, uml_tracedIntervalConstraints769, intermediateActivities_tracedTokens771, uml_tracedCallOperationActions761, integerFunctions_tracedIntegerGreaterFunctionBehaviorExecutions778, uml_tracedReadIsClassifiedObjectActions780, uml_tracedProtocolStateMachines782, uml_tracedOutputPins784, intermediateActivities_tracedOffers786, uml_tracedInstanceSpecifications774, uml_tracedValuePins776, uml_tracedDecisionNodes791, uml_tracedValueSpecificationActions793, uml_tracedRegions795, uml_tracedInterruptibleActivityRegions797, uml_tracedDestroyLinkActions799, intermediateActivities_tracedActivityParameterNodeActivations789, uml_tracedInteractionOperands805, uml_tracedInformationFlows807, uml_tracedPseudostates809, uml_tracedUseCases811, uml_tracedReplyActions813, uml_tracedFinalStates801, integerFunctions_tracedIntegerPlusFunctionBehaviorExecutions803, uml_tracedCombinedFragments817, uml_tracedClauses819, uml_tracedInstanceValues821, uml_tracedDependencys823, uml_tracedTimeExpressions825, intermediateActions_tracedCreateObjectActionActivations815, uml_tracedManifestations830, uml_tracedReadExtentActions832, basicActions_tracedInputPinActivations834, uml_tracedTransitions836, uml_tracedLinkEndDatas838, intermediateActivities_tracedActivityEdgeInstances827, uml_tracedNodes842, uml_tracedPackageMerges844, uml_tracedModels846, uml_tracedObjectFlows848, uml_tracedChangeEvents850, input_tracedInputParameterValuess840, uml_tracedForkNodes854, uml_tracedSignals856, uml_tracedComments858, uml_tracedLiteralNulls860, uml_tracedExpansionNodes862, uml_tracedDestroyObjectActions852, uml_tracedRaiseExceptionActions866, intermediateActivities_tracedActivityNodeActivations868, uml_tracedAddVariableValueActions871, uml_tracedClearAssociationActions873, uml_tracedTestIdentityActions875, uml_tracedReceptions864, uml_tracedOperations879, uml_tracedPackageImports881, uml_tracedExecutionOccurrenceSpecifications883, uml_tracedExceptionHandlers885, uml_tracedVariables887, uml_tracedControlFlows877, uml_tracedAssociations891, uml_tracedStateInvariants893, uml_tracedLiteralReals895, uml_tracedRemoveVariableValueActions897, uml_tracedInteractionUses889, uml_tracedSubstitutions901, uml_tracedGates903, uml_tracedGeneralOrderings905, uml_tracedCallBehaviorActions907, uml_tracedReclassifyObjectActions909, uml_tracedDevices899, uml_tracedConnectionPointReferences913, uml_tracedActionExecutionSpecifications915, uml_tracedReadSelfActions917, uml_tracedAcceptCallActions919, uml_tracedActivitys911, intermediateActivities_tracedActivityExecutions923, uml_tracedTemplateBindings926, uml_tracedClearStructuralFeatureActions928, uml_tracedLinkEndCreationDatas921, kernel_tracedLiteralIntegerEvaluations932, uml_tracedOpaqueExpressions934, uml_tracedFunctionBehaviors936, uml_tracedDeploymentSpecifications938, loci_tracedExecutionEnvironments930, uml_tracedBehaviorExecutionSpecifications942, uml_tracedUnmarshallActions944, uml_tracedCentralBufferNodes946, uml_tracedActors940, value_IntegerValueTrace954, typeTrace957, specification_EvaluationTrace960, locus_EvaluationTrace963, value_BooleanValueTrace966, typesTrace948, referentTrace951, featureValuesTrace969, values_FeatureValueTrace972, featureTrace975, locus_ExtensionalValueTrace981, values_ParameterValueTrace984, parameter_ParameterValueTrace987, parameterValuesTrace990, contextTrace993, positionTrace978, offeredTokenCountTrace1005, nodeActivationsTrace1008, activityExecutionTrace1011, edgeInstancesTrace1014, valueTrace1017, remainingOffersCountTrace996, baseTokenTrace999, baseTokenIsWithdrawnTrace1002, offeredTokensTrace1023, group_ActivityEdgeInstanceTrace1026, offersTrace1029, targetTrace1032, edge_ActivityEdgeInstanceTrace1035, sourceTrace1038, heldTokensTrace1041, node_ActivityNodeActivationTrace1044, runningTrace1047, isRunningTrace1050, holderTrace1020, activationGroupTrace1062, builtInTypesTrace1065, primitiveBehaviorPrototypesTrace1068, locus_ExecutionFactoryTrace1071, factoryTrace1074, extensionalValuesTrace1077, executorTrace1080, runtimeModelElementTrace1083, locus_ExecutorTrace1086, outgoingEdgesTrace1053, incomingEdgesTrace1056, group_ActivityNodeActivationTrace1059, pinActivationsTrace1092, firingTrace1095, locus_ExecutionEnvironmentTrace1089, actionActivationTrace1101, count_tempTrace1104, callExecutionsTrace1098, nameTrace1107, parameterValuesTrace1110, contract1113, end1114, redefinedConnector1117, type1120, originalObject1123, ownedAttribute1132, ownedOperation1134, originalObject_DataType1137, endData1139, inputValue1141, datatype1144, interface1146, associationEnd1149, inputValue1125, outputValue1127, originalObject1130, defaultValue1158, opposite1161, owningAssociation1164, redefinedProperty1167, subsettedProperty1170, association1173, originalObject_Property1176, originalObject1178, removeAt1179, originalObject1181, qualifier1152, class1155, manifestation1190, nestedArtifact1192, ownedAttribute1195, ownedOperation1198, originalObject_Artifact1201, contract1203, implementingClassifier1205, signal1183, target1185, originalObject1188, originalObject1215, event1216, originalObject1217, result1219, trigger1221, originalObject_AcceptEventAction1224, enumeration1226, insertAt1228, originalObject1230, inState1207, selection1209, upperBound1212, originalObject1234, operand1236, originalObject_Expression1238, message1240, originalObject1242, covered1243, enclosingOperand1245, enclosingInteraction1248, generalOrdering1251, result1232, attribute1255, collaborationUse1258, general1261, generalization1263, powertypeExtent1266, inheritedMember1269, ownedUseCase1272, useCase1275, feature1254, substitution1284, represented1287, originalObject1289, collaborationRole1291, originalObject1292, message1294, parameter1296, template1298, redefinedClassifier1278, representation1281, originalObject_TemplateSignature1303, signal1305, originalObject1307, configuration1309, deployedArtifact1311, location1313, protocol1315, provided1317, ownedParameter1300, required1323, context1326, input1328, localPostcondition1331, localPrecondition1334, output1337, metaclass1340, redefinedPort1320, when1347, originalObject1349, package1351, postCondition1353, preCondition1355, referred1358, nestedPackage1361, source1342, target1344, ownedStereotype1366, ownedType1369, packageMerge1371, packagedElement1374, profileApplication1376, originalObject_Package1379, classifierBehavior1381, interfaceRealization1383, ownedBehavior1386, nestingPackage1363, structuralFeature1391, constrainedElement1394, context1396, specification1398, originalObject_Constraint1401, lowerValue1403, upperValue1405, object1389, collection1415, reducer1417, result1420, originalObject1423, originalObject_InputPin1425, executableNode1426, featuringClassifier1427, maxint1429, powertype1408, generalization1410, originalObject1413, value1436, ownedComment1439, ownedElement1441, owner1444, semanticVisitorTrace1447, realizingClassifier1450, abstraction1452, minint1431, result1434, owningInstance1460, originalObject1463, signal1465, originalObject1467, useCase1469, originalObject1471, joinSpec1473, originalObject1475, object1477, definingFeature1455, value1457, importingNamespace1483, originalObject1486, classifier1488, result1490, originalObject1493, toAfter1495, toBefore1497, originalObject_OccurrenceSpecification1500, owningExpression1502, originalObject1479, importedElement1481, profile1509, nestedClassifier1512, ownedAttribute1514, ownedReception1517, protocol1520, redefinedInterface1523, ownedOperation1526, originalObject1529, clause1531, subExpression1504, icon1507, object1538, result1541, originalObject1544, originalObject1546, clientDependency1547, nameExpression1549, namespace1552, result1533, end1536, required1563, connectionPoint1566, submachineState1568, region1571, extendedStateMachine1574, lifeline1577, fragment1579, packagedElement1555, provided1557, realization1560, message1586, originalObject1589, object1590, originalObject1592, operation1594, originalObject1596, relatedElement1598, action1581, formalGate1583, originalObject1605, decomposedAs1607, interaction1609, represents1612, selector1615, coveredBy1618, originalObject1621, finish1623, start1625, event1628, request1600, target1602, outputElement1634, inputElement1636, value1639, bodyOutput1641, bodyPart1643, decider1646, loopVariable1649, loopVariableInput1652, originalObject1630, result1632, setupPart1658, test1661, generalMachine1664, specificMachine1666, originalObject1669, ownedLiteral1671, result1655, node1680, represents1682, subpartition1685, superPartition1688, edge1691, originalObject1694, variable1696, destroyAt1698, roleBinding1673, type1675, originalObject1678, originalObject1705, activity1707, inGroup1709, inInterruptibleRegion1711, inStructuredNode1714, incoming1717, outgoing1720, redefinedNode1723, addition1700, includingCase1702, connection1729, connectionPoint1731, deferrableTrigger1734, doActivity1737, entry1740, exit1743, redefinedState1746, stateInvariant1749, submachine1752, inPartition1726, result1760, templateBinding1762, ownedTemplateSignature1764, specification1767, context1768, ownedParameter1771, ownedParameterSet1774, postcondition1777, region1755, originalObject_State1758, constrainingClassifier1786, parameter1788, originalObject1790, condition1792, parameter1794, originalObject1797, expr1799, observation1801, precondition1780, redefinedBehavior1783, extension1807, nestedClassifier1810, ownedReception1813, superClass1816, originalObject_Class1819, originalObject1821, edge1822, originalObject1803, ownedOperation1805, variable1830, node1833, originalObject_StructuredActivityNode1836, mapping1838, result1840, originalObject1842, originalObject1844, extendedSignature1845, structuredNodeInput1824, structuredNodeOutput1827, classifier1850, originalObject_CreateLinkAction1853, general1854, generalizationSet1856, specific1859, originalObject1862, type1864, inheritedParameter1847, result1871, originalObject1874, actual1876, formal1877, ownedActual1880, templateBinding1883, originalObject1886, condition1888, extendedCase1890, object1866, qualifier1868, originalObject1899, result1901, originalObject1903, argument1905, connector1907, interaction1910, receiveEvent1913, sendEvent1915, extensionLocation1893, extension1896, originalObject1923, qualifier1924, value1926, originalObject1929, originalObject1931, originalObject1932, originalObject1933, appliedProfile1934, applyingPackage1936, signature1918, originalObject1921, templateParameter1943, default1946, ownedDefault1948, parameteredElement1951, signature1954, ownedParameteredElement1957, originalObject_TemplateParameter1960, definingEnd1962, originalObject1939, owningTemplateParameter1941, originalObject1972, ownedPort1973, defaultValue1975, operation1977, parameterSet1980, originalObject1983, partWithPort1964, role1967, originalObject1970, port1988, originalObject1991, operation1993, target1995, originalObject1998, metaclassReference2000, metamodelReference2002, max2005, min2007, fromAction1985, event1987, classifier2012, slot2014, specification2017, originalObject_InstanceSpecification2020, value2022, classifier2024, object2026, result2029, originalObject_Interval2010, originalObject2036, decisionInput2037, decisionInputFlow2039, originalObject2042, result2044, value2046, originalObject2049, extendedRegion2051, originalObject2032, conformance2034, transition2059, subvertex2062, originalObject2064, interruptingEdge2066, node2068, originalObject2071, originalObject2073, state2053, stateMachine2056, inActivity2079, subgroup2082, superGroup2085, fragment2088, guard2090, originalObject2093, activity2095, guard2097, containedEdge2074, inPartition2100, containedNode2076, interrupts2103, inStructuredNode2106, target2109, source2112, redefinedEdge2115, weight2118, inGroup2121, conveyed2124, informationSource2126, informationTarget2129, realization2132, realizingActivityEdge2134, realizingConnector2137, realizingMessage2140, originalObject2143, state2145, stateMachine2147, originalObject2150, extend2152, extensionPoint2154, include2157, subject2160, originalObject2163, replyToCall2165, replyValue2167, returnInformation2170, originalObject2173, cfragmentGate2175, operand2177, originalObject_CombinedFragment2180, body2182, bodyOutput2184, decider2187, predecessorClause2190, successorClause2193, test2196, originalObject2199, instance2201, originalObject2203, client2205, supplier2207, originalObject_Dependency2210, expr2212, observation2214, originalObject2217, utilizedElement2219, classifier2221, result2223, originalObject2226, effect2228, guard2230, redefinedTransition2233, source2236, target2239, trigger2242, container2245, originalObject_Transition2248, end2250, qualifier2252, value2255, originalObject_LinkEndData2258, nestedNode2260, mergedPackage2262, receivingPackage2264, originalObject2267, selection2269, transformation2271, originalObject2274, changeExpression2276, originalObject2278, redefinedElement2280, redefinitionContext2281, target2284, originalObject2286, originalObject2288, ownedAttribute2289, originalObject2291, annotatedElement2293, originalObject2295, ownedAttribute2297, ownedConnector2299, part2302, role2305, originalObject2308, regionAsInput2309, regionAsOutput2311, originalObject2314, signal2316, originalObject2318, exception2320, originalObject2322, method2324, ownedParameter2326, ownedParameterSet2329, raisedException2332, insertAt2335, originalObject2337, association2339, object2341, originalObject2344, first2346, result2348, second2351, originalObject2354, originalObject2356, bodyCondition2357, class2359, datatype2362, interface2365, postcondition2368, precondition2371, redefinedOperation2374, type2377, originalObject2380, end2382, container2384, incoming2386, outgoing2389, ownedRule2392, elementImport2394, packageImport2397, ownedMember2400, importedMember2403, member2406, importedPackage2409, originalObject2414, execution2416, exceptionInput2417, exceptionType2418, handlerBody2421, protectedNode2424, originalObject2427, activityScope2429, importingNamespace2411, scope2431, originalObject2434, actualGate2436, argument2438, refersTo2441, returnValue2444, returnValueRecipient2447, originalObject_InteractionUse2450, endType2452, memberEnd2454, ownedEnd2457, navigableOwnedEnd2460, originalObject_Association2463, invariant2465, originalObject2467, originalObject2469, argument2470, onPort2472, removeAt2475, originalObject2477, contract2479, substitutingClassifier2481, originalObject2484, deployedElement2485, deployment2487, before2492, originalObject2495, behavior2497, originalObject2499, newClassifier2501, object2503, oldClassifier2506, originalObject2509, ownedGroup2511, after2490, edge2513, node2516, variable2519, group2522, ownedNode2525, partition2528, structuredNode2531, entry2534, exit2536, state2539, originalObject2542, action2544, originalObject2546, result2548, originalObject2550, returnInformation2552, insertAt2554, parameterSubstitution2556, signature2558, boundElement2561, originalObject2564, result2566, originalObject2568, behavior2570, result2572, originalObject2575, deployment2577, originalObject2579, behavior2580, originalObject2582, handler2584, object2586, result2588, unmarshallType2591, originalObject2594, originalObject_CentralBufferNode2596, eAnnotations2597},
    generalizations={gen_umlTrace_Kernel_TracedObject_TracedExtensionalValue, gen_umlTrace_Kernel_TracedIntegerValue_TracedPrimitiveValue, gen_umlTrace_Kernel_TracedLiteralEvaluation_TracedEvaluation, gen_umlTrace_Kernel_TracedValue_TracedSemanticVisitor, gen_umlTrace_Kernel_TracedPrimitiveValue_TracedValue, gen_umlTrace_Kernel_TracedEvaluation_TracedSemanticVisitor, gen_umlTrace_Kernel_TracedBooleanValue_TracedPrimitiveValue, gen_umlTrace_Kernel_TracedLiteralBooleanEvaluation_TracedLiteralEvaluation, gen_umlTrace_Kernel_TracedReference_TracedStructuredValue, gen_umlTrace_Kernel_TracedCompoundValue_TracedStructuredValue, gen_umlTrace_Kernel_TracedStructuredValue_TracedValue, gen_umlTrace_Kernel_TracedExtensionalValue_TracedCompoundValue, gen_umlTrace_Kernel_TracedLiteralIntegerEvaluation_TracedLiteralEvaluation, gen_umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution_TracedExecution, gen_umlTrace_BasicBehaviors_TracedExecution_TracedObject, gen_umlTrace_IntermediateActivities_TracedForkedToken_TracedToken, gen_umlTrace_IntermediateActivities_TracedJoinNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedInitialNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedObjectNodeActivation_TracedActivityNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedMergeNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedControlToken_TracedToken, gen_umlTrace_IntermediateActivities_TracedObjectToken_TracedToken, gen_umlTrace_IntermediateActivities_TracedDecisionNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation_TracedObjectNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityNodeActivation_TracedSemanticVisitor, gen_umlTrace_IntermediateActivities_TracedForkNodeActivation_TracedControlNodeActivation, gen_umlTrace_IntermediateActivities_TracedActivityExecution_TracedExecution, gen_umlTrace_IntermediateActivities_TracedControlNodeActivation_TracedActivityNodeActivation, gen_umlTrace_IntermediateActions_TracedValueSpecificationActionActivation_TracedActionActivation, gen_umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation, gen_umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation_TracedWriteStructuralFeatureActionActivation, gen_umlTrace_IntermediateActions_TracedCreateObjectActionActivation_TracedActionActivation, gen_umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation_TracedStructuralFeatureActionActivation, gen_umlTrace_BasicActions_TracedActionActivation_TracedActivityNodeActivation, gen_umlTrace_BasicActions_TracedOutputPinActivation_TracedPinActivation, gen_umlTrace_BasicActions_TracedCallBehaviorActionActivation_TracedCallActionActivation, gen_umlTrace_BasicActions_TracedOpaqueActionActivation_TracedActionActivation, gen_umlTrace_BasicActions_TracedCallActionActivation_TracedInvocationActionActivation, gen_umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation_TracedActionActivation, gen_umlTrace_BasicActions_TracedPinActivation_TracedObjectNodeActivation, gen_umlTrace_BasicActions_TracedInputPinActivation_TracedPinActivation, gen_umlTrace_BasicActions_TracedInvocationActionActivation_TracedActionActivation, gen_umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution_TracedOpaqueBehaviorExecution, gen_umlTrace_uml_TracedStructuralFeature_uml_TracedFeature, gen_umlTrace_uml_TracedStructuralFeature_uml_TracedTypedElement, gen_umlTrace_uml_TracedStructuralFeature_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedConnector_TracedFeature, gen_umlTrace_uml_TracedOpaqueAction_TracedAction, gen_umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution_TracedOpaqueBehaviorExecution, gen_umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution_TracedOpaqueBehaviorExecution, gen_umlTrace_uml_TracedDataType_TracedClassifier, gen_umlTrace_uml_TracedCommunicationPath_TracedAssociation, gen_umlTrace_uml_TracedLinkAction_TracedAction, gen_umlTrace_uml_TracedProperty_uml_TracedStructuralFeature, gen_umlTrace_uml_TracedProperty_uml_TracedConnectableElement, gen_umlTrace_uml_TracedProperty_uml_TracedDeploymentTarget, gen_umlTrace_uml_TracedContinuation_TracedInteractionFragment, gen_umlTrace_uml_TracedRemoveStructuralFeatureValueAction_TracedWriteStructuralFeatureAction, gen_umlTrace_uml_TracedSendSignalAction_TracedInvocationAction, gen_umlTrace_uml_TracedOpaqueBehavior_TracedBehavior, gen_umlTrace_uml_TracedArtifact_uml_TracedClassifier, gen_umlTrace_uml_TracedArtifact_uml_TracedDeployedArtifact, gen_umlTrace_uml_TracedTimeConstraint_TracedIntervalConstraint, gen_umlTrace_uml_TracedInterfaceRealization_TracedRealization, gen_umlTrace_uml_TracedObjectNode_uml_TracedActivityNode, gen_umlTrace_uml_TracedObjectNode_uml_TracedTypedElement, gen_umlTrace_uml_TracedActivityFinalNode_TracedFinalNode, gen_umlTrace_uml_TracedDurationObservation_TracedObservation, gen_umlTrace_uml_TracedAcceptEventAction_TracedAction, gen_umlTrace_uml_TracedEnumerationLiteral_TracedInstanceSpecification, gen_umlTrace_uml_TracedAddStructuralFeatureValueAction_TracedWriteStructuralFeatureAction, gen_umlTrace_uml_TracedExpression_TracedValueSpecification, gen_umlTrace_uml_TracedConsiderIgnoreFragment_TracedCombinedFragment, gen_umlTrace_uml_TracedDataStoreNode_TracedCentralBufferNode, gen_umlTrace_uml_TracedFlowFinalNode_TracedFinalNode, gen_umlTrace_uml_TracedInteractionFragment_TracedNamedElement, gen_umlTrace_uml_TracedReadLinkAction_TracedLinkAction, gen_umlTrace_uml_TracedClassifier_uml_TracedNamespace, gen_umlTrace_uml_TracedClassifier_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedClassifier_uml_TracedType, gen_umlTrace_uml_TracedClassifier_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedInformationItem_TracedClassifier, gen_umlTrace_uml_TracedCollaboration_uml_TracedStructuredClassifier, gen_umlTrace_uml_TracedCollaboration_uml_TracedBehavioredClassifier, gen_umlTrace_uml_TracedMessageEnd_TracedNamedElement, gen_umlTrace_uml_TracedTemplateSignature_TracedElement, gen_umlTrace_uml_TracedBroadcastSignalAction_TracedInvocationAction, gen_umlTrace_uml_TracedDeployment_TracedDependency, gen_umlTrace_uml_TracedPort_TracedProperty, gen_umlTrace_uml_TracedTimeInterval_TracedInterval, gen_umlTrace_uml_TracedAction_TracedExecutableNode, gen_umlTrace_uml_TracedExtension_TracedAssociation, gen_umlTrace_uml_TracedDirectedRelationship_TracedRelationship, gen_umlTrace_uml_TracedTimeEvent_TracedEvent, gen_umlTrace_uml_TracedPackageableElement_uml_TracedNamedElement, gen_umlTrace_uml_TracedPackageableElement_uml_TracedParameterableElement, gen_umlTrace_uml_TracedType_TracedPackageableElement, gen_umlTrace_uml_TracedProtocolTransition_TracedTransition, gen_umlTrace_uml_TracedPackage_uml_TracedNamespace, gen_umlTrace_uml_TracedPackage_uml_TracedPackageableElement, gen_umlTrace_uml_TracedPackage_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedBehavioredClassifier_TracedClassifier, gen_umlTrace_uml_TracedStructuralFeatureAction_TracedAction, gen_umlTrace_uml_TracedConstraint_TracedPackageableElement, gen_umlTrace_uml_TracedMultiplicityElement_TracedElement, gen_umlTrace_uml_TracedLiteralSpecification_TracedValueSpecification, gen_umlTrace_uml_TracedGeneralizationSet_TracedPackageableElement, gen_umlTrace_uml_TracedReduceAction_TracedAction, gen_umlTrace_uml_TracedInputPin_TracedPin, gen_umlTrace_uml_TracedSequenceNode_TracedStructuredActivityNode, gen_umlTrace_uml_TracedFeature_TracedRedefinableElement, gen_umlTrace_uml_TracedInteractionConstraint_TracedConstraint, gen_umlTrace_uml_TracedElement_TracedEModelElement, gen_umlTrace_uml_TracedComponentRealization_TracedRealization, gen_umlTrace_uml_TracedAssociationClass_uml_TracedClass, gen_umlTrace_uml_TracedAssociationClass_uml_TracedAssociation, gen_umlTrace_uml_TracedSlot_TracedElement, gen_umlTrace_uml_TracedWriteStructuralFeatureAction_TracedStructuralFeatureAction, gen_umlTrace_uml_TracedSignalEvent_TracedMessageEvent, gen_umlTrace_uml_TracedExtensionPoint_TracedRedefinableElement, gen_umlTrace_uml_TracedJoinNode_TracedControlNode, gen_umlTrace_uml_TracedStartObjectBehaviorAction_TracedCallAction, gen_umlTrace_uml_TracedCreateObjectAction_TracedAction, gen_umlTrace_uml_TracedExecutionEnvironment_TracedNode, gen_umlTrace_uml_TracedOccurrenceSpecification_TracedInteractionFragment, gen_umlTrace_uml_TracedStringExpression_uml_TracedExpression, gen_umlTrace_uml_TracedStringExpression_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedElementImport_TracedDirectedRelationship, gen_umlTrace_uml_TracedInterface_TracedClassifier, gen_umlTrace_uml_TracedConditionalNode_TracedStructuredActivityNode, gen_umlTrace_uml_TracedDeployedArtifact_TracedNamedElement, gen_umlTrace_uml_TracedStereotype_TracedClass, gen_umlTrace_uml_TracedAnyReceiveEvent_TracedMessageEvent, gen_umlTrace_uml_TracedNamedElement_TracedElement, gen_umlTrace_uml_TracedComponent_TracedClass, gen_umlTrace_uml_TracedReadLinkObjectEndAction_TracedAction, gen_umlTrace_uml_TracedExtensionEnd_TracedProperty, gen_umlTrace_uml_TracedStateMachine_TracedBehavior, gen_umlTrace_uml_TracedValueSpecification_uml_TracedPackageableElement, gen_umlTrace_uml_TracedValueSpecification_uml_TracedTypedElement, gen_umlTrace_uml_TracedInteraction_uml_TracedBehavior, gen_umlTrace_uml_TracedInteraction_uml_TracedInteractionFragment, gen_umlTrace_uml_TracedLiteralString_TracedLiteralSpecification, gen_umlTrace_uml_TracedRealization_TracedAbstraction, gen_umlTrace_uml_TracedStartClassifierBehaviorAction_TracedAction, gen_umlTrace_uml_TracedMessageEvent_TracedEvent, gen_umlTrace_uml_TracedCallEvent_TracedMessageEvent, gen_umlTrace_uml_TracedConnectableElementTemplateParameter_TracedTemplateParameter, gen_umlTrace_uml_TracedRelationship_TracedElement, gen_umlTrace_uml_TracedSendObjectAction_TracedInvocationAction, gen_umlTrace_uml_TracedLifeline_TracedNamedElement, gen_umlTrace_uml_TracedExecutionSpecification_TracedInteractionFragment, gen_umlTrace_uml_TracedTimeObservation_TracedObservation, gen_umlTrace_uml_TracedExpansionRegion_TracedStructuredActivityNode, gen_umlTrace_uml_TracedWriteVariableAction_TracedVariableAction, gen_umlTrace_uml_TracedLoopNode_TracedStructuredActivityNode, gen_umlTrace_uml_TracedCreateLinkObjectAction_TracedCreateLinkAction, gen_umlTrace_uml_TracedPrimitiveType_TracedDataType, gen_umlTrace_uml_TracedProtocolConformance_TracedDirectedRelationship, gen_umlTrace_uml_TracedEnumeration_TracedDataType, gen_umlTrace_uml_TracedCollaborationUse_TracedNamedElement, gen_umlTrace_uml_TracedActivityPartition_TracedActivityGroup, gen_umlTrace_uml_TracedVariableAction_TracedAction, gen_umlTrace_uml_TracedLinkEndDestructionData_TracedLinkEndData, gen_umlTrace_uml_TracedDurationInterval_TracedInterval, gen_umlTrace_uml_TracedInclude_uml_TracedNamedElement, gen_umlTrace_uml_TracedInclude_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedActivityNode_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedActivityNode_ActivityContent, gen_umlTrace_uml_TracedDestructionOccurrenceSpecification_TracedMessageOccurrenceSpecification, gen_umlTrace_uml_TracedState_uml_TracedNamespace, gen_umlTrace_uml_TracedState_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedState_uml_TracedVertex, gen_umlTrace_uml_TracedCallAction_TracedInvocationAction, gen_umlTrace_uml_TracedTemplateableElement_TracedElement, gen_umlTrace_uml_TracedBehavior_TracedClass, gen_umlTrace_uml_TracedClassifierTemplateParameter_TracedTemplateParameter, gen_umlTrace_uml_TracedActivityParameterNode_TracedObjectNode, gen_umlTrace_uml_TracedParameterSet_TracedNamedElement, gen_umlTrace_uml_TracedDuration_TracedValueSpecification, gen_umlTrace_uml_TracedUsage_TracedDependency, gen_umlTrace_uml_TracedLiteralUnlimitedNatural_TracedLiteralSpecification, gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedAction, gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedNamespace, gen_umlTrace_uml_TracedStructuredActivityNode_uml_TracedActivityGroup, gen_umlTrace_uml_TracedClass_uml_TracedEncapsulatedClassifier, gen_umlTrace_uml_TracedClass_uml_TracedBehavioredClassifier, gen_umlTrace_uml_TracedAbstraction_TracedDependency, gen_umlTrace_uml_TracedReadStructuralFeatureAction_TracedStructuralFeatureAction, gen_umlTrace_uml_TracedMergeNode_TracedControlNode, gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedRedefinableTemplateSignature_uml_TracedTemplateSignature, gen_umlTrace_uml_TracedCreateLinkAction_TracedWriteLinkAction, gen_umlTrace_uml_TracedGeneralization_TracedDirectedRelationship, gen_umlTrace_uml_TracedPartDecomposition_TracedInteractionUse, gen_umlTrace_uml_TracedTypedElement_TracedNamedElement, gen_umlTrace_uml_TracedOperationTemplateParameter_TracedTemplateParameter, gen_umlTrace_uml_TracedReadLinkObjectEndQualifierAction_TracedAction, gen_umlTrace_uml_TracedTemplateParameterSubstitution_TracedElement, gen_umlTrace_uml_TracedExtend_uml_TracedNamedElement, gen_umlTrace_uml_TracedExtend_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedReadVariableAction_TracedVariableAction, gen_umlTrace_uml_TracedMessage_TracedNamedElement, gen_umlTrace_uml_TracedQualifierValue_TracedElement, gen_umlTrace_uml_TracedInitialNode_TracedControlNode, gen_umlTrace_uml_TracedLiteralInteger_TracedLiteralSpecification, gen_umlTrace_uml_TracedClearVariableAction_TracedVariableAction, gen_umlTrace_uml_TracedProfileApplication_TracedDirectedRelationship, gen_umlTrace_uml_TracedLiteralBoolean_TracedLiteralSpecification, gen_umlTrace_uml_TracedTemplateParameter_TracedElement, gen_umlTrace_uml_TracedConnectorEnd_TracedMultiplicityElement, gen_umlTrace_uml_TracedParameterableElement_TracedElement, gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedOccurrenceSpecification, gen_umlTrace_uml_TracedMessageOccurrenceSpecification_uml_TracedMessageEnd, gen_umlTrace_uml_TracedDurationConstraint_TracedIntervalConstraint, gen_umlTrace_uml_TracedImage_TracedElement, gen_umlTrace_uml_TracedEncapsulatedClassifier_TracedStructuredClassifier, gen_umlTrace_uml_TracedParameter_uml_TracedConnectableElement, gen_umlTrace_uml_TracedParameter_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedActionInputPin_TracedInputPin, gen_umlTrace_uml_TracedCallOperationAction_TracedCallAction, gen_umlTrace_uml_TracedProfile_TracedPackage, gen_umlTrace_uml_TracedInterval_TracedValueSpecification, gen_umlTrace_uml_TracedTrigger_TracedNamedElement, gen_umlTrace_uml_TracedValuePin_TracedInputPin, gen_umlTrace_uml_TracedReadIsClassifiedObjectAction_TracedAction, gen_umlTrace_uml_TracedIntervalConstraint_TracedConstraint, gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeploymentTarget, gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedPackageableElement, gen_umlTrace_uml_TracedInstanceSpecification_uml_TracedDeployedArtifact, gen_umlTrace_uml_TracedDecisionNode_TracedControlNode, gen_umlTrace_uml_TracedValueSpecificationAction_TracedAction, gen_umlTrace_uml_TracedRegion_uml_TracedNamespace, gen_umlTrace_uml_TracedRegion_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedProtocolStateMachine_TracedStateMachine, gen_umlTrace_uml_TracedOutputPin_TracedPin, gen_umlTrace_uml_TracedInterruptibleActivityRegion_TracedActivityGroup, gen_umlTrace_uml_TracedDestroyLinkAction_TracedWriteLinkAction, gen_umlTrace_uml_TracedFinalState_TracedState, gen_umlTrace_uml_TracedActivityGroup_uml_TracedNamedElement, gen_umlTrace_uml_TracedActivityGroup_ActivityContent, gen_umlTrace_uml_TracedInteractionOperand_uml_TracedNamespace, gen_umlTrace_uml_TracedInteractionOperand_uml_TracedInteractionFragment, gen_umlTrace_uml_TracedActivityEdge_TracedRedefinableElement, gen_umlTrace_uml_TracedInformationFlow_uml_TracedPackageableElement, gen_umlTrace_uml_TracedInformationFlow_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedPseudostate_TracedVertex, gen_umlTrace_uml_TracedControlNode_TracedActivityNode, gen_umlTrace_uml_TracedUseCase_TracedBehavioredClassifier, gen_umlTrace_uml_TracedReplyAction_TracedAction, gen_umlTrace_uml_TracedCombinedFragment_TracedInteractionFragment, gen_umlTrace_uml_TracedWriteLinkAction_TracedLinkAction, gen_umlTrace_uml_TracedClause_TracedElement, gen_umlTrace_uml_TracedInstanceValue_TracedValueSpecification, gen_umlTrace_uml_TracedDependency_uml_TracedPackageableElement, gen_umlTrace_uml_TracedDependency_uml_TracedDirectedRelationship, gen_umlTrace_uml_TracedTimeExpression_TracedValueSpecification, gen_umlTrace_uml_TracedManifestation_TracedAbstraction, gen_umlTrace_uml_TracedReadExtentAction_TracedAction, gen_umlTrace_uml_TracedTransition_uml_TracedNamespace, gen_umlTrace_uml_TracedTransition_uml_TracedRedefinableElement, gen_umlTrace_uml_TracedLinkEndData_TracedElement, gen_umlTrace_uml_TracedNode_uml_TracedClass, gen_umlTrace_uml_TracedNode_uml_TracedDeploymentTarget, gen_umlTrace_uml_TracedPackageMerge_TracedDirectedRelationship, gen_umlTrace_uml_TracedModel_TracedPackage, gen_umlTrace_uml_TracedObjectFlow_TracedActivityEdge, gen_umlTrace_uml_TracedEvent_TracedPackageableElement, gen_umlTrace_uml_TracedChangeEvent_TracedEvent, gen_umlTrace_uml_TracedRedefinableElement_TracedNamedElement, gen_umlTrace_uml_TracedDestroyObjectAction_TracedAction, gen_umlTrace_uml_TracedForkNode_TracedControlNode, gen_umlTrace_uml_TracedFinalNode_TracedControlNode, gen_umlTrace_uml_TracedSignal_TracedClassifier, gen_umlTrace_uml_TracedComment_TracedElement, gen_umlTrace_uml_TracedStructuredClassifier_TracedClassifier, gen_umlTrace_uml_TracedLiteralNull_TracedLiteralSpecification, gen_umlTrace_uml_TracedExpansionNode_TracedObjectNode, gen_umlTrace_uml_TracedReception_TracedBehavioralFeature, gen_umlTrace_uml_TracedRaiseExceptionAction_TracedAction, gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedNamespace, gen_umlTrace_uml_TracedBehavioralFeature_uml_TracedFeature, gen_umlTrace_uml_TracedAddVariableValueAction_TracedWriteVariableAction, gen_umlTrace_uml_TracedClearAssociationAction_TracedAction, gen_umlTrace_uml_TracedPin_uml_TracedObjectNode, gen_umlTrace_uml_TracedPin_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedTestIdentityAction_TracedAction, gen_umlTrace_uml_TracedControlFlow_TracedActivityEdge, gen_umlTrace_uml_TracedOperation_uml_TracedBehavioralFeature, gen_umlTrace_uml_TracedOperation_uml_TracedParameterableElement, gen_umlTrace_uml_TracedOperation_uml_TracedTemplateableElement, gen_umlTrace_uml_TracedConnectableElement_uml_TracedTypedElement, gen_umlTrace_uml_TracedConnectableElement_uml_TracedParameterableElement, gen_umlTrace_uml_TracedVertex_TracedNamedElement, gen_umlTrace_uml_TracedObservation_TracedPackageableElement, gen_umlTrace_uml_TracedNamespace_TracedNamedElement, gen_umlTrace_uml_TracedPackageImport_TracedDirectedRelationship, gen_umlTrace_uml_TracedExecutionOccurrenceSpecification_TracedOccurrenceSpecification, gen_umlTrace_uml_TracedExceptionHandler_TracedElement, gen_umlTrace_uml_TracedVariable_uml_TracedConnectableElement, gen_umlTrace_uml_TracedVariable_uml_TracedMultiplicityElement, gen_umlTrace_uml_TracedInteractionUse_TracedInteractionFragment, gen_umlTrace_uml_TracedAssociation_uml_TracedClassifier, gen_umlTrace_uml_TracedAssociation_uml_TracedRelationship, gen_umlTrace_uml_TracedStateInvariant_TracedInteractionFragment, gen_umlTrace_uml_TracedLiteralReal_TracedLiteralSpecification, gen_umlTrace_uml_TracedInvocationAction_TracedAction, gen_umlTrace_uml_TracedRemoveVariableValueAction_TracedWriteVariableAction, gen_umlTrace_uml_TracedDevice_TracedNode, gen_umlTrace_uml_TracedSubstitution_TracedRealization, gen_umlTrace_uml_TracedGate_TracedMessageEnd, gen_umlTrace_uml_TracedDeploymentTarget_TracedNamedElement, gen_umlTrace_uml_TracedGeneralOrdering_TracedNamedElement, gen_umlTrace_uml_TracedCallBehaviorAction_TracedCallAction, gen_umlTrace_uml_TracedReclassifyObjectAction_TracedAction, gen_umlTrace_uml_TracedActivity_TracedBehavior, gen_umlTrace_uml_TracedConnectionPointReference_TracedVertex, gen_umlTrace_uml_TracedActionExecutionSpecification_TracedExecutionSpecification, gen_umlTrace_uml_TracedReadSelfAction_TracedAction, gen_umlTrace_uml_TracedAcceptCallAction_TracedAcceptEventAction, gen_umlTrace_uml_TracedLinkEndCreationData_TracedLinkEndData, gen_umlTrace_uml_TracedTemplateBinding_TracedDirectedRelationship, gen_umlTrace_uml_TracedClearStructuralFeatureAction_TracedStructuralFeatureAction, gen_umlTrace_uml_TracedOpaqueExpression_TracedValueSpecification, gen_umlTrace_uml_TracedFunctionBehavior_TracedOpaqueBehavior, gen_umlTrace_uml_TracedDeploymentSpecification_TracedArtifact, gen_umlTrace_uml_TracedActor_TracedBehavioredClassifier, gen_umlTrace_uml_TracedBehaviorExecutionSpecification_TracedExecutionSpecification, gen_umlTrace_uml_TracedExecutableNode_TracedActivityNode, gen_umlTrace_uml_TracedUnmarshallAction_TracedAction, gen_umlTrace_uml_TracedCentralBufferNode_TracedObjectNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)