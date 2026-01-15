from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class uml_TracedElement:

    pass
class umlTrace_Values_SemanticVisitor_runtimeModelElement_Value:

    pass
class TracedOpaqueBehaviorExecution:

    pass
class umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution(TracedOpaqueBehaviorExecution):

    pass
class umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution(TracedOpaqueBehaviorExecution):

    pass
class umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution(TracedOpaqueBehaviorExecution):

    pass
class TracedLiteralEvaluation:

    pass
class umlTrace_Kernel_TracedLiteralIntegerEvaluation(TracedLiteralEvaluation):

    pass
class umlTrace_Kernel_TracedLiteralBooleanEvaluation(TracedLiteralEvaluation):

    pass
class uml_ActivityContent(ABC):

    pass
class BasicActions_TracedActionActivation:

    pass
class umlTrace_Values_ActionActivation_firing_Value:

    def __init__(self, firing: str, 0460: set["State"] = None, 0463: "BasicActions_TracedActionActivation" = None):
        self.firing = firing
        self.0460 = 0460 if 0460 is not None else set()
        self.0463 = 0463
        
    @property
    def firing(self) -> str:
        return self.__firing

    @firing.setter
    def firing(self, firing: str):
        self.__firing = firing

    @property
    def 0463(self):
        return self.__0463

    @0463.setter
    def 0463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ActionActivation_firing_Value__0463", None)
        self.__0463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "464"):
                opp_val = getattr(old_value, "464", None)
                if opp_val == self:
                    setattr(old_value, "464", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "464"):
                opp_val = getattr(value, "464", None)
                setattr(value, "464", self)

    @property
    def 0460(self):
        return self.__0460

    @0460.setter
    def 0460(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTrace_Values_ActionActivation_firing_Value__0460", None)
        self.__0460 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "461"):
                    opp_val = getattr(item, "461", None)
                    
                    if opp_val == self:
                        setattr(item, "461", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "461"):
                    opp_val = getattr(item, "461", None)
                    
                    setattr(item, "461", self)
                    

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
class TracedCallActionActivation:

    pass
class umlTrace_BasicActions_TracedCallBehaviorActionActivation(TracedCallActionActivation):

    pass
class TracedPinActivation:

    pass
class umlTrace_BasicActions_TracedOutputPinActivation(TracedPinActivation):

    pass
class umlTrace_BasicActions_TracedInputPinActivation(TracedPinActivation):

    pass
class TracedInvocationActionActivation:

    pass
class umlTrace_BasicActions_TracedCallActionActivation(TracedInvocationActionActivation):

    pass
class TracedActionActivation:

    pass
class umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation(TracedActionActivation):

    pass
class umlTrace_BasicActions_TracedOpaqueActionActivation(TracedActionActivation):

    pass
class umlTrace_IntermediateActions_TracedValueSpecificationActionActivation(TracedActionActivation):

    pass
class umlTrace_BasicActions_TracedInvocationActionActivation(TracedActionActivation):

    pass
class TracedPrimitiveValue:

    pass
class umlTrace_Kernel_TracedBooleanValue(TracedPrimitiveValue):

    pass
class umlTrace_Kernel_TracedIntegerValue(TracedPrimitiveValue):

    pass
class TracedEvaluation:

    pass
class umlTrace_Kernel_TracedLiteralEvaluation(TracedEvaluation):

    pass
class TracedValue:

    pass
class umlTrace_Kernel_TracedPrimitiveValue(TracedValue):

    pass
class umlTrace_Kernel_TracedStructuredValue(TracedValue):

    pass
class TracedStructuredValue:

    pass
class umlTrace_Kernel_TracedReference(TracedStructuredValue):

    pass
class umlTrace_Kernel_TracedCompoundValue(TracedStructuredValue):

    pass
class TracedCompoundValue:

    pass
class umlTrace_Kernel_TracedExtensionalValue(TracedCompoundValue):

    pass
class TracedExtensionalValue:

    pass
class umlTrace_Kernel_TracedObject(TracedExtensionalValue):

    pass
class TracedObject:

    pass
class umlTrace_BasicBehaviors_TracedExecution(TracedObject):

    pass
class umlTrace_IntermediateActions_TracedCreateObjectActionActivation(TracedActionActivation):

    pass
class TracedSemanticVisitor:

    pass
class umlTrace_Kernel_TracedEvaluation(TracedSemanticVisitor):

    pass
class umlTrace_Kernel_TracedValue(TracedSemanticVisitor):

    pass
class umlTrace_IntermediateActivities_TracedActivityNodeActivation(TracedSemanticVisitor):

    pass
class TracedActivityNodeActivation:

    pass
class umlTrace_IntermediateActivities_TracedControlNodeActivation(TracedActivityNodeActivation):

    pass
class TracedControlNodeActivation:

    pass
class umlTrace_IntermediateActivities_TracedForkNodeActivation(TracedControlNodeActivation):

    pass
class umlTrace_ecore_TracedEModelElement(ABC):

    pass
class TracedMessageEnd:

    pass
class umlTrace_uml_TracedGate(TracedMessageEnd):

    pass
class umlTrace_BasicActions_TracedActionActivation(TracedActivityNodeActivation):

    pass
class umlTrace_Loci_TracedSemanticVisitor:

    pass
class umlTrace_IntermediateActivities_TracedDecisionNodeActivation(TracedControlNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation(TracedControlNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedJoinNodeActivation(TracedControlNodeActivation):

    pass
class TracedObjectNodeActivation:

    pass
class umlTrace_BasicActions_TracedPinActivation(TracedObjectNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation(TracedObjectNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedMergeNodeActivation(TracedControlNodeActivation):

    pass
class TracedExecution:

    pass
class umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution(TracedExecution):

    pass
class umlTrace_IntermediateActivities_TracedActivityExecution(TracedExecution):

    pass
class umlTrace_IntermediateActivities_TracedInitialNodeActivation(TracedControlNodeActivation):

    pass
class umlTrace_IntermediateActivities_TracedObjectNodeActivation(TracedActivityNodeActivation):

    pass
class uml_TracedVertex:

    pass
class TracedState:

    pass
class umlTrace_uml_TracedFinalState(TracedState):

    pass
class TracedExecutionSpecification:

    pass
class umlTrace_uml_TracedActionExecutionSpecification(TracedExecutionSpecification):

    pass
class umlTrace_uml_TracedBehaviorExecutionSpecification(TracedExecutionSpecification):

    pass
class TracedOccurrenceSpecification:

    pass
class umlTrace_uml_TracedExecutionOccurrenceSpecification(TracedOccurrenceSpecification):

    pass
class uml_TracedStructuredClassifier:

    pass
class TracedMultiplicityElement:

    pass
class umlTrace_uml_TracedConnectorEnd(TracedMultiplicityElement):

    pass
class TracedBehavioralFeature:

    pass
class umlTrace_uml_TracedReception(TracedBehavioralFeature):

    pass
class TracedObjectNode:

    pass
class umlTrace_uml_TracedExpansionNode(TracedObjectNode):

    pass
class umlTrace_uml_TracedActivityParameterNode(TracedObjectNode):

    pass
class umlTrace_uml_TracedCentralBufferNode(TracedObjectNode):

    pass
class TracedCentralBufferNode:

    pass
class umlTrace_uml_TracedDataStoreNode(TracedCentralBufferNode):

    pass
class TracedDataType:

    pass
class umlTrace_uml_TracedEnumeration(TracedDataType):

    pass
class umlTrace_uml_TracedPrimitiveType(TracedDataType):

    pass
class TracedMessageEvent:

    pass
class umlTrace_uml_TracedCallEvent(TracedMessageEvent):

    pass
class umlTrace_uml_TracedAnyReceiveEvent(TracedMessageEvent):

    pass
class uml_TracedBehavioralFeature:

    pass
class TracedOpaqueBehavior:

    pass
class umlTrace_uml_TracedFunctionBehavior(TracedOpaqueBehavior):

    pass
class TracedObservation:

    pass
class umlTrace_uml_TracedTimeObservation(TracedObservation):

    pass
class umlTrace_uml_TracedDurationObservation(TracedObservation):

    pass
class TracedInterval:

    pass
class umlTrace_uml_TracedDurationInterval(TracedInterval):

    pass
class umlTrace_uml_TracedTimeInterval(TracedInterval):

    pass
class umlTrace_uml_TracedSignalEvent(TracedMessageEvent):

    pass
class TracedActivityEdge:

    pass
class umlTrace_uml_TracedControlFlow(TracedActivityEdge):

    pass
class umlTrace_uml_TracedObjectFlow(TracedActivityEdge):

    pass
class TracedStateMachine:

    pass
class umlTrace_uml_TracedProtocolStateMachine(TracedStateMachine):

    pass
class TracedBehavior:

    pass
class umlTrace_uml_TracedOpaqueBehavior(TracedBehavior):

    pass
class umlTrace_uml_TracedActivity(TracedBehavior):

    pass
class umlTrace_uml_TracedStateMachine(TracedBehavior):

    pass
class TracedActivityGroup:

    pass
class umlTrace_uml_TracedActivityPartition(TracedActivityGroup):

    pass
class TracedDependency:

    pass
class umlTrace_uml_TracedDeployment(TracedDependency):

    pass
class umlTrace_uml_TracedUsage(TracedDependency):

    pass
class umlTrace_uml_TracedAbstraction(TracedDependency):

    pass
class TracedAbstraction:

    pass
class umlTrace_uml_TracedManifestation(TracedAbstraction):

    pass
class umlTrace_uml_TracedRealization(TracedAbstraction):

    pass
class TracedTemplateParameter:

    pass
class umlTrace_uml_TracedOperationTemplateParameter(TracedTemplateParameter):

    pass
class umlTrace_uml_TracedConnectableElementTemplateParameter(TracedTemplateParameter):

    pass
class umlTrace_uml_TracedClassifierTemplateParameter(TracedTemplateParameter):

    pass
class TracedPackage:

    pass
class umlTrace_uml_TracedProfile(TracedPackage):

    pass
class umlTrace_uml_TracedModel(TracedPackage):

    pass
class TracedTransition:

    pass
class umlTrace_uml_TracedProtocolTransition(TracedTransition):

    pass
class TracedWriteVariableAction:

    pass
class umlTrace_uml_TracedRemoveVariableValueAction(TracedWriteVariableAction):

    pass
class umlTrace_uml_TracedAddVariableValueAction(TracedWriteVariableAction):

    pass
class umlTrace_uml_TracedInterruptibleActivityRegion(TracedActivityGroup):

    pass
class TracedInteractionUse:

    pass
class umlTrace_uml_TracedPartDecomposition(TracedInteractionUse):

    pass
class uml_TracedInteractionFragment:

    pass
class uml_TracedBehavior:

    pass
class umlTrace_uml_TracedInteraction(uml_TracedInteractionFragment, uml_TracedBehavior):

    pass
class TracedValueSpecification:

    pass
class umlTrace_uml_TracedDuration(TracedValueSpecification):

    pass
class umlTrace_uml_TracedInterval(TracedValueSpecification):

    pass
class umlTrace_uml_TracedExpression(TracedValueSpecification):

    pass
class umlTrace_uml_TracedTimeExpression(TracedValueSpecification):

    pass
class umlTrace_uml_TracedInstanceValue(TracedValueSpecification):

    pass
class umlTrace_uml_TracedLiteralSpecification(TracedValueSpecification):

    pass
class TracedLiteralSpecification:

    pass
class umlTrace_uml_TracedLiteralReal(TracedLiteralSpecification):

    pass
class umlTrace_uml_TracedLiteralBoolean(TracedLiteralSpecification):

    pass
class umlTrace_uml_TracedLiteralUnlimitedNatural(TracedLiteralSpecification):

    pass
class umlTrace_uml_TracedLiteralInteger(TracedLiteralSpecification):

    pass
class umlTrace_uml_TracedLiteralString(TracedLiteralSpecification):

    pass
class TracedVariableAction:

    pass
class umlTrace_uml_TracedWriteVariableAction(TracedVariableAction):

    pass
class umlTrace_uml_TracedReadVariableAction(TracedVariableAction):

    pass
class umlTrace_uml_TracedClearVariableAction(TracedVariableAction):

    pass
class TracedCombinedFragment:

    pass
class umlTrace_uml_TracedConsiderIgnoreFragment(TracedCombinedFragment):

    pass
class TracedNode:

    pass
class umlTrace_uml_TracedDevice(TracedNode):

    pass
class umlTrace_uml_TracedExecutionEnvironment(TracedNode):

    pass
class uml_TracedRelationship:

    pass
class TracedAssociation:

    pass
class umlTrace_uml_TracedCommunicationPath(TracedAssociation):

    pass
class umlTrace_uml_TracedExtension(TracedAssociation):

    pass
class TracedRealization:

    pass
class umlTrace_uml_TracedInterfaceRealization(TracedRealization):

    pass
class umlTrace_uml_TracedComponentRealization(TracedRealization):

    pass
class umlTrace_uml_TracedSubstitution(TracedRealization):

    pass
class TracedInstanceSpecification:

    pass
class umlTrace_uml_TracedEnumerationLiteral(TracedInstanceSpecification):

    pass
class TracedAcceptEventAction:

    pass
class umlTrace_uml_TracedAcceptCallAction(TracedAcceptEventAction):

    pass
class TracedLinkEndData:

    pass
class umlTrace_uml_TracedLinkEndCreationData(TracedLinkEndData):

    pass
class umlTrace_uml_TracedLinkEndDestructionData(TracedLinkEndData):

    pass
class umlTrace_uml_TracedOpaqueExpression(TracedValueSpecification):

    pass
class umlTrace_uml_TracedLiteralNull(TracedLiteralSpecification):

    pass
class TracedClass:

    pass
class umlTrace_uml_TracedComponent(TracedClass):

    pass
class umlTrace_uml_TracedStereotype(TracedClass):

    pass
class umlTrace_uml_TracedBehavior(TracedClass):

    pass
class TracedInputPin:

    pass
class umlTrace_uml_TracedActionInputPin(TracedInputPin):

    pass
class umlTrace_uml_TracedValuePin(TracedInputPin):

    pass
class uml_TracedMultiplicityElement:

    pass
class uml_TracedTypedElement:

    pass
class uml_TracedFeature:

    pass
class umlTrace_uml_TracedStructuralFeature(uml_TracedMultiplicityElement, uml_TracedFeature, uml_TracedTypedElement):

    pass
class uml_TracedDeploymentTarget:

    pass
class uml_TracedConnectableElement:

    pass
class umlTrace_uml_TracedVariable(uml_TracedConnectableElement, uml_TracedMultiplicityElement):

    pass
class umlTrace_uml_TracedParameter(uml_TracedConnectableElement, uml_TracedMultiplicityElement):

    pass
class uml_TracedStructuralFeature:

    pass
class umlTrace_uml_TracedProperty(uml_TracedConnectableElement, uml_TracedDeploymentTarget, uml_TracedStructuralFeature):

    pass
class TracedProperty:

    pass
class umlTrace_uml_TracedExtensionEnd(TracedProperty):

    pass
class umlTrace_uml_TracedPort(TracedProperty):

    pass
class uml_TracedDirectedRelationship:

    pass
class TracedEvent:

    pass
class umlTrace_uml_TracedMessageEvent(TracedEvent):

    pass
class umlTrace_uml_TracedTimeEvent(TracedEvent):

    pass
class umlTrace_uml_TracedChangeEvent(TracedEvent):

    pass
class TracedStructuralFeatureAction:

    pass
class umlTrace_uml_TracedReadStructuralFeatureAction(TracedStructuralFeatureAction):

    pass
class umlTrace_uml_TracedClearStructuralFeatureAction(TracedStructuralFeatureAction):

    pass
class umlTrace_uml_TracedWriteStructuralFeatureAction(TracedStructuralFeatureAction):

    pass
class TracedWriteStructuralFeatureAction:

    pass
class umlTrace_uml_TracedAddStructuralFeatureValueAction(TracedWriteStructuralFeatureAction):

    pass
class umlTrace_uml_TracedRemoveStructuralFeatureValueAction(TracedWriteStructuralFeatureAction):

    pass
class TracedBehavioredClassifier:

    pass
class umlTrace_uml_TracedActor(TracedBehavioredClassifier):

    pass
class umlTrace_uml_TracedUseCase(TracedBehavioredClassifier):

    pass
class uml_TracedDeployedArtifact:

    pass
class uml_TracedClassifier:

    pass
class umlTrace_uml_TracedAssociation(uml_TracedClassifier, uml_TracedRelationship):

    pass
class umlTrace_uml_TracedArtifact(uml_TracedDeployedArtifact, uml_TracedClassifier):

    pass
class TracedArtifact:

    pass
class umlTrace_uml_TracedDeploymentSpecification(TracedArtifact):

    pass
class uml_TracedActivityNode:

    pass
class umlTrace_uml_TracedObjectNode(uml_TracedActivityNode, uml_TracedTypedElement):

    pass
class uml_TracedObjectNode:

    pass
class umlTrace_uml_TracedPin(uml_TracedMultiplicityElement, uml_TracedObjectNode):

    pass
class TracedPin:

    pass
class umlTrace_uml_TracedOutputPin(TracedPin):

    pass
class umlTrace_uml_TracedInputPin(TracedPin):

    pass
class TracedInvocationAction:

    pass
class umlTrace_uml_TracedSendSignalAction(TracedInvocationAction):

    pass
class umlTrace_uml_TracedBroadcastSignalAction(TracedInvocationAction):

    pass
class umlTrace_uml_TracedSendObjectAction(TracedInvocationAction):

    pass
class TracedRedefinableElement:

    pass
class umlTrace_uml_TracedActivityEdge(TracedRedefinableElement):

    pass
class umlTrace_uml_TracedExtensionPoint(TracedRedefinableElement):

    pass
class umlTrace_uml_TracedFeature(TracedRedefinableElement):

    pass
class TracedFeature:

    pass
class umlTrace_uml_TracedConnector(TracedFeature):

    pass
class uml_TracedTemplateableElement:

    pass
class uml_TracedPackageableElement:

    pass
class umlTrace_uml_TracedDependency(uml_TracedPackageableElement, uml_TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedInformationFlow(uml_TracedPackageableElement, uml_TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedInstanceSpecification(uml_TracedDeploymentTarget, uml_TracedDeployedArtifact, uml_TracedPackageableElement):

    pass
class umlTrace_uml_TracedValueSpecification(uml_TracedPackageableElement, uml_TracedTypedElement):

    pass
class uml_TracedMessageEnd:

    pass
class TracedMessageOccurrenceSpecification:

    pass
class umlTrace_uml_TracedDestructionOccurrenceSpecification(TracedMessageOccurrenceSpecification):

    pass
class TracedVertex:

    pass
class umlTrace_uml_TracedConnectionPointReference(TracedVertex):

    pass
class umlTrace_uml_TracedPseudostate(TracedVertex):

    pass
class uml_TracedParameterableElement:

    pass
class umlTrace_uml_TracedConnectableElement(uml_TracedParameterableElement, uml_TracedTypedElement):

    pass
class umlTrace_uml_TracedOperation(uml_TracedParameterableElement, uml_TracedTemplateableElement, uml_TracedBehavioralFeature):

    pass
class uml_TracedType:

    pass
class TracedClassifier:

    pass
class umlTrace_uml_TracedDataType(TracedClassifier):

    pass
class umlTrace_uml_TracedSignal(TracedClassifier):

    pass
class umlTrace_uml_TracedInformationItem(TracedClassifier):

    pass
class umlTrace_uml_TracedBehavioredClassifier(TracedClassifier):

    pass
class umlTrace_uml_TracedInterface(TracedClassifier):

    pass
class umlTrace_uml_TracedStructuredClassifier(TracedClassifier):

    pass
class TracedStructuredClassifier:

    pass
class umlTrace_uml_TracedEncapsulatedClassifier(TracedStructuredClassifier):

    pass
class uml_TracedBehavioredClassifier:

    pass
class umlTrace_uml_TracedCollaboration(uml_TracedBehavioredClassifier, uml_TracedStructuredClassifier):

    pass
class uml_TracedEncapsulatedClassifier:

    pass
class umlTrace_uml_TracedClass(uml_TracedBehavioredClassifier, uml_TracedEncapsulatedClassifier):

    pass
class umlTrace_uml_TracedCallAction(TracedInvocationAction):

    pass
class TracedCallAction:

    pass
class umlTrace_uml_TracedStartObjectBehaviorAction(TracedCallAction):

    pass
class umlTrace_uml_TracedCallOperationAction(TracedCallAction):

    pass
class umlTrace_uml_TracedCallBehaviorAction(TracedCallAction):

    pass
class TracedRelationship:

    pass
class umlTrace_uml_TracedDirectedRelationship(TracedRelationship):

    pass
class TracedDirectedRelationship:

    pass
class umlTrace_uml_TracedGeneralization(TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedElementImport(TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedPackageImport(TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedTemplateBinding(TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedPackageMerge(TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedProfileApplication(TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedProtocolConformance(TracedDirectedRelationship):

    pass
class ActivityContent:

    pass
class uml_TracedRedefinableElement:

    pass
class umlTrace_uml_TracedActivityNode(ActivityContent, uml_TracedRedefinableElement):

    pass
class TracedActivityNode:

    pass
class umlTrace_uml_TracedExecutableNode(TracedActivityNode):

    pass
class TracedExecutableNode:

    pass
class umlTrace_uml_TracedAction(TracedExecutableNode):

    pass
class uml_TracedActivityGroup:

    pass
class uml_TracedNamespace:

    pass
class umlTrace_uml_TracedPackage(uml_TracedNamespace, uml_TracedPackageableElement, uml_TracedTemplateableElement):

    pass
class umlTrace_uml_TracedTransition(uml_TracedNamespace, uml_TracedRedefinableElement):

    pass
class umlTrace_uml_TracedBehavioralFeature(uml_TracedNamespace, uml_TracedFeature):

    pass
class umlTrace_uml_TracedState(uml_TracedVertex, uml_TracedNamespace, uml_TracedRedefinableElement):

    pass
class umlTrace_uml_TracedClassifier(uml_TracedType, uml_TracedNamespace, uml_TracedRedefinableElement, uml_TracedTemplateableElement):

    pass
class umlTrace_uml_TracedRegion(uml_TracedNamespace, uml_TracedRedefinableElement):

    pass
class umlTrace_uml_TracedInteractionOperand(uml_TracedNamespace, uml_TracedInteractionFragment):

    pass
class uml_TracedAction:

    pass
class umlTrace_uml_TracedStructuredActivityNode(uml_TracedActivityGroup, uml_TracedAction, uml_TracedNamespace):

    pass
class TracedStructuredActivityNode:

    pass
class umlTrace_uml_TracedSequenceNode(TracedStructuredActivityNode):

    pass
class umlTrace_uml_TracedLoopNode(TracedStructuredActivityNode):

    pass
class umlTrace_uml_TracedConditionalNode(TracedStructuredActivityNode):

    pass
class TracedEModelElement:

    pass
class umlTrace_uml_TracedElement(TracedEModelElement):

    pass
class TracedElement:

    pass
class umlTrace_uml_TracedTemplateSignature(TracedElement):

    pass
class umlTrace_uml_TracedComment(TracedElement):

    pass
class umlTrace_uml_TracedQualifierValue(TracedElement):

    pass
class umlTrace_uml_TracedTemplateParameter(TracedElement):

    pass
class umlTrace_uml_TracedSlot(TracedElement):

    pass
class umlTrace_uml_TracedRelationship(TracedElement):

    pass
class umlTrace_uml_TracedParameterableElement(TracedElement):

    pass
class umlTrace_uml_TracedClause(TracedElement):

    pass
class umlTrace_uml_TracedTemplateParameterSubstitution(TracedElement):

    pass
class umlTrace_uml_TracedImage(TracedElement):

    pass
class umlTrace_uml_TracedLinkEndData(TracedElement):

    pass
class umlTrace_uml_TracedMultiplicityElement(TracedElement):

    pass
class umlTrace_uml_TracedExceptionHandler(TracedElement):

    pass
class umlTrace_uml_TracedTemplateableElement(TracedElement):

    pass
class umlTrace_uml_TracedNamedElement(TracedElement):

    pass
class TracedNamedElement:

    pass
class umlTrace_uml_TracedMessage(TracedNamedElement):

    pass
class umlTrace_uml_TracedCollaborationUse(TracedNamedElement):

    pass
class umlTrace_uml_TracedParameterSet(TracedNamedElement):

    pass
class umlTrace_uml_TracedDeploymentTarget(TracedNamedElement):

    pass
class umlTrace_uml_TracedTrigger(TracedNamedElement):

    pass
class umlTrace_uml_TracedDeployedArtifact(TracedNamedElement):

    pass
class umlTrace_uml_TracedMessageEnd(TracedNamedElement):

    pass
class umlTrace_uml_TracedGeneralOrdering(TracedNamedElement):

    pass
class umlTrace_uml_TracedVertex(TracedNamedElement):

    pass
class umlTrace_uml_TracedTypedElement(TracedNamedElement):

    pass
class umlTrace_uml_TracedInteractionFragment(TracedNamedElement):

    pass
class TracedInteractionFragment:

    pass
class umlTrace_uml_TracedInteractionUse(TracedInteractionFragment):

    pass
class umlTrace_uml_TracedContinuation(TracedInteractionFragment):

    pass
class umlTrace_uml_TracedStateInvariant(TracedInteractionFragment):

    pass
class umlTrace_uml_TracedOccurrenceSpecification(TracedInteractionFragment):

    pass
class umlTrace_uml_TracedExecutionSpecification(TracedInteractionFragment):

    pass
class umlTrace_uml_TracedCombinedFragment(TracedInteractionFragment):

    pass
class TracedPackageableElement:

    pass
class umlTrace_uml_TracedEvent(TracedPackageableElement):

    pass
class umlTrace_uml_TracedType(TracedPackageableElement):

    pass
class umlTrace_uml_TracedGeneralizationSet(TracedPackageableElement):

    pass
class umlTrace_uml_TracedObservation(TracedPackageableElement):

    pass
class umlTrace_uml_TracedConstraint(TracedPackageableElement):

    pass
class TracedConstraint:

    pass
class umlTrace_uml_TracedInteractionConstraint(TracedConstraint):

    pass
class umlTrace_uml_TracedIntervalConstraint(TracedConstraint):

    pass
class TracedIntervalConstraint:

    pass
class umlTrace_uml_TracedTimeConstraint(TracedIntervalConstraint):

    pass
class umlTrace_uml_TracedDurationConstraint(TracedIntervalConstraint):

    pass
class umlTrace_uml_TracedLifeline(TracedNamedElement):

    pass
class umlTrace_uml_TracedExpansionRegion(TracedStructuredActivityNode):

    pass
class TracedFinalNode:

    pass
class umlTrace_uml_TracedActivityFinalNode(TracedFinalNode):

    pass
class umlTrace_uml_TracedFlowFinalNode(TracedFinalNode):

    pass
class umlTrace_uml_TracedControlNode(TracedActivityNode):

    pass
class TracedControlNode:

    pass
class umlTrace_uml_TracedForkNode(TracedControlNode):

    pass
class umlTrace_uml_TracedFinalNode(TracedControlNode):

    pass
class umlTrace_uml_TracedJoinNode(TracedControlNode):

    pass
class umlTrace_uml_TracedDecisionNode(TracedControlNode):

    pass
class umlTrace_uml_TracedMergeNode(TracedControlNode):

    pass
class umlTrace_uml_TracedInitialNode(TracedControlNode):

    pass
class TracedAction:

    pass
class umlTrace_uml_TracedUnmarshallAction(TracedAction):

    pass
class umlTrace_uml_TracedReadLinkObjectEndQualifierAction(TracedAction):

    pass
class umlTrace_uml_TracedRaiseExceptionAction(TracedAction):

    pass
class umlTrace_uml_TracedAcceptEventAction(TracedAction):

    pass
class umlTrace_uml_TracedReplyAction(TracedAction):

    pass
class umlTrace_uml_TracedStartClassifierBehaviorAction(TracedAction):

    pass
class umlTrace_uml_TracedReduceAction(TracedAction):

    pass
class umlTrace_uml_TracedReclassifyObjectAction(TracedAction):

    pass
class umlTrace_uml_TracedReadSelfAction(TracedAction):

    pass
class umlTrace_uml_TracedClearAssociationAction(TracedAction):

    pass
class umlTrace_uml_TracedStructuralFeatureAction(TracedAction):

    pass
class umlTrace_uml_TracedDestroyObjectAction(TracedAction):

    pass
class umlTrace_uml_TracedCreateObjectAction(TracedAction):

    pass
class umlTrace_uml_TracedOpaqueAction(TracedAction):

    pass
class umlTrace_uml_TracedReadLinkObjectEndAction(TracedAction):

    pass
class umlTrace_uml_TracedTestIdentityAction(TracedAction):

    pass
class umlTrace_uml_TracedVariableAction(TracedAction):

    pass
class umlTrace_uml_TracedValueSpecificationAction(TracedAction):

    pass
class umlTrace_uml_TracedInvocationAction(TracedAction):

    pass
class umlTrace_uml_TracedReadIsClassifiedObjectAction(TracedAction):

    pass
class umlTrace_uml_TracedReadExtentAction(TracedAction):

    pass
class umlTrace_uml_TracedLinkAction(TracedAction):

    pass
class TracedLinkAction:

    pass
class umlTrace_uml_TracedReadLinkAction(TracedLinkAction):

    pass
class umlTrace_uml_TracedWriteLinkAction(TracedLinkAction):

    pass
class TracedWriteLinkAction:

    pass
class umlTrace_uml_TracedDestroyLinkAction(TracedWriteLinkAction):

    pass
class umlTrace_uml_TracedCreateLinkAction(TracedWriteLinkAction):

    pass
class TracedCreateLinkAction:

    pass
class umlTrace_uml_TracedCreateLinkObjectAction(TracedCreateLinkAction):

    pass
class uml_TracedNamedElement:

    pass
class umlTrace_uml_TracedExtend(uml_TracedNamedElement, uml_TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedInclude(uml_TracedNamedElement, uml_TracedDirectedRelationship):

    pass
class umlTrace_uml_TracedPackageableElement(uml_TracedParameterableElement, uml_TracedNamedElement):

    pass
class umlTrace_uml_TracedActivityGroup(ActivityContent, uml_TracedNamedElement):

    pass
class umlTrace_uml_TracedNamespace(TracedNamedElement):

    pass
class umlTrace_uml_TracedRedefinableElement(TracedNamedElement):

    pass
class uml_TracedActivityFinalNode:

    pass
class uml_TracedClassifierTemplateParameter:

    pass
class uml_TracedComponent:

    pass
class uml_TracedGeneralOrdering:

    pass
class uml_TracedControlFlow:

    pass
class uml_TracedTimeObservation:

    pass
class uml_TracedGate:

    pass
class uml_TracedLinkEndCreationData:

    pass
class uml_TracedPseudostate:

    pass
class IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution:

    pass
class uml_TracedElementImport:

    pass
class uml_TracedMergeNode:

    pass
class uml_TracedClearAssociationAction:

    pass
class uml_TracedAbstraction:

    pass
class uml_TracedTimeExpression:

    pass
class IntermediateActivities_TracedMergeNodeActivation:

    pass
class uml_TracedTemplateParameter:

    pass
class uml_TracedReadIsClassifiedObjectAction:

    pass
class uml_TracedManifestation:

    pass
class uml_TracedActor:

    pass
class uml_TracedRemoveVariableValueAction:

    pass
class uml_TracedValueSpecificationAction:

    pass
class uml_TracedFunctionBehavior:

    pass
class uml_TracedSendSignalAction:

    pass
class uml_TracedInterfaceRealization:

    pass
class uml_TracedSlot:

    pass
class uml_TracedUnmarshallAction:

    pass
class uml_TracedProfile:

    pass
class uml_TracedTestIdentityAction:

    pass
class uml_TracedCollaboration:

    pass
class IntermediateActions_TracedCreateObjectActionActivation:

    pass
class uml_TracedLiteralReal:

    pass
class uml_TracedExpression:

    pass
class umlTrace_uml_TracedStringExpression(uml_TracedExpression, uml_TracedTemplateableElement):

    pass
class uml_TracedAssociation:

    pass
class uml_TracedClearStructuralFeatureAction:

    pass
class uml_TracedAddVariableValueAction:

    pass
class IntermediateActions_TracedValueSpecificationActionActivation:

    pass
class uml_TracedStartObjectBehaviorAction:

    pass
class uml_TracedLiteralBoolean:

    pass
class uml_TracedInclude:

    pass
class uml_TracedRegion:

    pass
class uml_TracedState:

    pass
class uml_TracedLiteralNull:

    pass
class uml_TracedPrimitiveType:

    pass
class uml_TracedStringExpression:

    pass
class uml_TracedLinkEndDestructionData:

    pass
class uml_TracedReadLinkAction:

    pass
class uml_TracedRaiseExceptionAction:

    pass
class uml_TracedCommunicationPath:

    pass
class Kernel_TracedLiteralBooleanEvaluation:

    pass
class uml_TracedEnumeration:

    pass
class uml_TracedReadLinkObjectEndAction:

    pass
class uml_TracedCallBehaviorAction:

    pass
class uml_TracedReadExtentAction:

    pass
class BasicActions_TracedOutputPinActivation:

    pass
class uml_TracedTemplateSignature:

    pass
class umlTrace_uml_TracedRedefinableTemplateSignature(uml_TracedTemplateSignature, uml_TracedRedefinableElement):

    pass
class uml_TracedLiteralUnlimitedNatural:

    pass
class uml_TracedDurationObservation:

    pass
class uml_TracedBehaviorExecutionSpecification:

    pass
class uml_TracedVariable:

    pass
class uml_TracedConnectorEnd:

    pass
class uml_TracedArtifact:

    pass
class uml_TracedCallOperationAction:

    pass
class uml_TracedProfileApplication:

    pass
class uml_TracedExtensionEnd:

    pass
class uml_TracedProperty:

    pass
class uml_TracedDevice:

    pass
class uml_TracedActivityParameterNode:

    pass
class uml_TracedExpansionNode:

    pass
class uml_TracedAddStructuralFeatureValueAction:

    pass
class uml_TracedQualifierValue:

    pass
class uml_TracedImage:

    pass
class uml_TracedOutputPin:

    pass
class uml_TracedActionExecutionSpecification:

    pass
class uml_TracedInformationItem:

    pass
class uml_TracedOpaqueAction:

    pass
class uml_TracedFinalState:

    pass
class uml_TracedReduceAction:

    pass
class uml_TracedDuration:

    pass
class uml_TracedTemplateParameterSubstitution:

    pass
class uml_TracedTrigger:

    pass
class uml_TracedReplyAction:

    pass
class uml_TracedClause:

    pass
class uml_TracedOperationTemplateParameter:

    pass
class uml_TracedConnectableElementTemplateParameter:

    pass
class uml_TracedLinkEndData:

    pass
class uml_TracedDurationInterval:

    pass
class uml_TracedTransition:

    pass
class uml_TracedParameterSet:

    pass
class uml_TracedOccurrenceSpecification:

    pass
class umlTrace_uml_TracedMessageOccurrenceSpecification(uml_TracedOccurrenceSpecification, uml_TracedMessageEnd):

    pass
class uml_TracedAcceptEventAction:

    pass
class uml_TracedPackageMerge:

    pass
class uml_TracedDecisionNode:

    pass
class IntermediateActions_TracedReadStructuralFeatureActionActivation:

    pass
class uml_TracedReadSelfAction:

    pass
class uml_TracedOperation:

    pass
class uml_TracedObjectFlow:

    pass
class uml_TracedProtocolConformance:

    pass
class uml_TracedOpaqueBehavior:

    pass
class uml_TracedInterface:

    pass
class uml_TracedComponentRealization:

    pass
class uml_TracedDataType:

    pass
class uml_TracedComment:

    pass
class uml_TracedLoopNode:

    pass
class uml_TracedCallEvent:

    pass
class uml_TracedPackage:

    pass
class uml_TracedCreateLinkAction:

    pass
class Kernel_TracedLiteralIntegerEvaluation:

    pass
class uml_TracedCentralBufferNode:

    pass
class IntermediateActivities_TracedDecisionNodeActivation:

    pass
class uml_TracedInteractionConstraint:

    pass
class uml_TracedTimeInterval:

    pass
class uml_TracedExecutionOccurrenceSpecification:

    pass
class uml_TracedSignal:

    pass
class uml_TracedExtensionPoint:

    pass
class uml_TracedConditionalNode:

    pass
class Kernel_TracedBooleanValue:

    pass
class uml_TracedSignalEvent:

    pass
class uml_TracedModel:

    pass
class uml_TracedRedefinableTemplateSignature:

    pass
class uml_TracedJoinNode:

    pass
class BasicActions_TracedOpaqueActionActivation:

    pass
class uml_TracedReadLinkObjectEndQualifierAction:

    pass
class uml_TracedRealization:

    pass
class uml_TracedConnectionPointReference:

    pass
class uml_TracedTemplateBinding:

    pass
class uml_TracedMessageOccurrenceSpecification:

    pass
class uml_TracedReception:

    pass
class uml_TracedProtocolStateMachine:

    pass
class uml_TracedLiteralInteger:

    pass
class uml_TracedDestroyLinkAction:

    pass
class IntermediateActivities_TracedActivityFinalNodeActivation:

    pass
class uml_TracedReadVariableAction:

    pass
class uml_TracedActionInputPin:

    pass
class uml_TracedUsage:

    pass
class uml_TracedDeploymentSpecification:

    pass
class uml_TracedInteractionOperand:

    pass
class uml_TracedProtocolTransition:

    pass
class uml_TracedInterruptibleActivityRegion:

    pass
class uml_TracedPartDecomposition:

    pass
class uml_TracedDataStoreNode:

    pass
class uml_TracedReadStructuralFeatureAction:

    pass
class uml_TracedAnyReceiveEvent:

    pass
class Kernel_TracedIntegerValue:

    pass
class uml_TracedInterval:

    pass
class uml_TracedRemoveStructuralFeatureValueAction:

    pass
class uml_TracedInstanceValue:

    pass
class uml_TracedGeneralization:

    pass
class IntermediateActions_TracedAddStructuralFeatureValueActionActivation:

    pass
class Kernel_TracedReference:

    pass
class uml_TracedForkNode:

    pass
class uml_TracedActivity:

    pass
class uml_TracedTimeEvent:

    pass
class Loci_TracedSemanticVisitor:

    pass
class Kernel_TracedObject:

    pass
class IntermediateActivities_TracedJoinNodeActivation:

    pass
class uml_TracedUseCase:

    pass
class uml_TracedReclassifyObjectAction:

    pass
class uml_TracedAssociationClass:

    pass
class uml_TracedInformationFlow:

    pass
class uml_TracedSubstitution:

    pass
class uml_TracedEnumerationLiteral:

    pass
class uml_TracedStereotype:

    pass
class uml_TracedDeployment:

    pass
class uml_TracedMessage:

    pass
class uml_TracedStateMachine:

    pass
class uml_TracedActivityPartition:

    pass
class IntermediateActivities_TracedActivityParameterNodeActivation:

    pass
class BasicActions_TracedCallBehaviorActionActivation:

    pass
class uml_TracedDestroyObjectAction:

    pass
class IntermediateActivities_TracedActivityNodeActivation:

    pass
class uml_TracedInteraction:

    pass
class uml_TracedBroadcastSignalAction:

    pass
class uml_TracedConstraint:

    pass
class uml_TracedClearVariableAction:

    pass
class uml_TracedAcceptCallAction:

    pass
class uml_TracedInstanceSpecification:

    pass
class IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution:

    pass
class uml_TracedStateInvariant:

    pass
class BasicActions_TracedInputPinActivation:

    pass
class uml_TracedLiteralString:

    pass
class uml_TracedOpaqueExpression:

    pass
class uml_TracedParameter:

    pass
class uml_TracedStartClassifierBehaviorAction:

    pass
class uml_TracedSequenceNode:

    pass
class uml_TracedExceptionHandler:

    pass
class uml_TracedNode:

    pass
class uml_TracedValuePin:

    pass
class uml_TracedInputPin:

    pass
class uml_TracedTimeConstraint:

    pass
class uml_TracedContinuation:

    pass
class uml_TracedConsiderIgnoreFragment:

    pass
class uml_TracedIntervalConstraint:

    pass
class uml_TracedExecutionEnvironment:

    pass
class uml_TracedStructuredActivityNode:

    pass
class uml_TracedExtension:

    pass
class IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution:

    pass
class uml_TracedExtend:

    pass
class uml_TracedConnector:

    pass
class uml_TracedDestructionOccurrenceSpecification:

    pass
class uml_TracedDurationConstraint:

    pass
class IntermediateActivities_TracedForkNodeActivation:

    pass
class uml_TracedLifeline:

    pass
class uml_TracedCreateObjectAction:

    pass
class IntermediateActivities_TracedActivityExecution:

    pass
class uml_TracedCollaborationUse:

    pass
class IntermediateActivities_TracedInitialNodeActivation:

    pass
class uml_TracedPort:

    pass
class uml_TracedDependency:

    pass
class uml_TracedChangeEvent:

    pass
class uml_TracedGeneralizationSet:

    pass
class uml_TracedInteractionUse:

    pass
class uml_TracedClass:

    pass
class umlTrace_uml_TracedNode(uml_TracedDeploymentTarget, uml_TracedClass):

    pass
class umlTrace_uml_TracedAssociationClass(uml_TracedAssociation, uml_TracedClass):

    pass
class uml_TracedPackageImport:

    pass
class uml_TracedSendObjectAction:

    pass
class uml_TracedExpansionRegion:

    pass
class uml_TracedFlowFinalNode:

    pass
class uml_TracedInitialNode:

    pass
class uml_TracedCreateLinkObjectAction:

    pass
class uml_TracedCombinedFragment:

    pass
class umlTrace_Traced_TracedObjects:

    pass
class Traced_TracedObjects:

    pass
class State:

    pass
class umlTrace_Trace:

    pass
class Values_SemanticVisitor_runtimeModelElement_Value:

    pass
class Values_ActionActivation_firing_Value:

    pass
class umlTrace_State:

    pass