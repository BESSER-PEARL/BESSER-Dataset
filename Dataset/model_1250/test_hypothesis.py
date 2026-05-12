import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EParameter,
    xmof_Kernel_DirectedParameter,
    EClass,
    OpaqueBehavior,
    xmof_BasicBehaviors_FunctionBehavior,
    BasicBehaviors_Behavior,
    EClassifier,
    xmof_BasicBehaviors_BehavioredClassifier,
    Communications_xmof_EAttribute,
    xmof_Communications_Signal,
    Communications_Event,
    ENamedElement,
    xmof_Communications_Event,
    xmof_Communications_Trigger,
    BehavioredEClass,
    xmof_BasicBehaviors_Behavior,
    Behavior,
    xmof_BasicBehaviors_OpaqueBehavior,
    BasicBehaviors_BehavioredClassifier,
    xmof_Kernel_BehavioredEClass,
    Kernel_DirectedParameter,
    Kernel_BehavioredEOperation,
    BasicBehaviors_ParameterValue,
    xmof_BasicBehaviors_ParameterValueDefinition,
    Kernel_Value,
    xmof_BasicBehaviors_ParameterValue,
    PrimitiveValue,
    xmof_Kernel_IntegerValue,
    xmof_Kernel_StringValue,
    Kernel_PrimitiveType,
    Value,
    xmof_Kernel_EnumerationValue,
    xmof_Kernel_PrimitiveValue,
    xmof_LociL1_SemanticVisitor,
    Kernel_xmof_EObject,
    xmof_Kernel_ObjectValue,
    SemanticVisitor,
    xmof_Kernel_Value,
    xmof_Kernel_BooleanValue,
    Kernel_xmof_EEnum,
    InvocationAction,
    xmof_BasicActions_CallAction,
    IntermediateActivities_ObjectNode,
    Pin,
    xmof_BasicActions_OutputPin,
    xmof_BasicActions_InputPin,
    xmof_BasicActions_SendSignalAction,
    BasicActions_xmof_EClassifier,
    ExecutableNode,
    xmof_BasicActions_Action,
    Communications_Trigger,
    CompleteActions_xmof_EClassifier,
    WriteLinkAction,
    xmof_IntermediateActions_CreateLinkAction,
    CallAction,
    xmof_BasicActions_CallOperationAction,
    xmof_BasicActions_CallBehaviorAction,
    xmof_CompleteActions_StartObjectBehaviorAction,
    xmof_IntermediateActions_DestroyLinkAction,
    IntermediateActions_xmof_EClassifier,
    WriteStructuralFeatureAction,
    xmof_IntermediateActions_AddStructuralFeatureValueAction,
    xmof_IntermediateActions_RemoveStructuralFeatureValueAction,
    StructuralFeatureAction,
    xmof_IntermediateActions_ClearStructuralFeatureAction,
    xmof_IntermediateActions_WriteStructuralFeatureAction,
    IntermediateActions_xmof_EReference,
    LinkEndData,
    xmof_IntermediateActions_LinkEndDestructionData,
    xmof_IntermediateActions_LinkEndCreationData,
    xmof_IntermediateActions_ReadStructuralFeatureAction,
    IntermediateActions_xmof_EStructuralFeature,
    IntermediateActions_LinkEndData,
    LinkAction,
    xmof_IntermediateActions_ReadLinkAction,
    xmof_IntermediateActions_WriteLinkAction,
    Action,
    xmof_CompleteActions_ReduceAction,
    xmof_IntermediateActions_ClearAssociationAction,
    xmof_BasicActions_InvocationAction,
    xmof_CompleteActions_ReadIsClassifiedObjectAction,
    xmof_IntermediateActions_StructuralFeatureAction,
    xmof_IntermediateActions_CreateObjectAction,
    xmof_IntermediateActions_DestroyObjectAction,
    xmof_IntermediateActions_ValueSpecificationAction,
    xmof_CompleteActions_ReclassifyObjectAction,
    xmof_IntermediateActions_TestIdentityAction,
    xmof_IntermediateActions_LinkAction,
    xmof_CompleteActions_StartClassifierBehaviorAction,
    xmof_CompleteActions_AcceptEventAction,
    xmof_CompleteActions_ReadExtentAction,
    xmof_IntermediateActions_ReadSelfAction,
    xmof_CompleteStructuredActivities_StructuredActivityNode,
    ExtraStructuredActivities_ExpansionNode,
    ExtraStructuredActivities_ExpansionRegion,
    CompleteStructuredActivities_Clause,
    ActivityNode,
    xmof_CompleteStructuredActivities_ExecutableNode,
    xmof_IntermediateActivities_ControlNode,
    ControlNode,
    xmof_IntermediateActivities_JoinNode,
    xmof_IntermediateActivities_FinalNode,
    xmof_IntermediateActivities_DecisionNode,
    xmof_IntermediateActivities_InitialNode,
    xmof_IntermediateActivities_ForkNode,
    xmof_IntermediateActivities_MergeNode,
    BasicActions_InputPin,
    CompleteStructuredActivities_ExecutableNode,
    BasicActions_OutputPin,
    StructuredActivityNode,
    xmof_ExtraStructuredActivities_ExpansionRegion,
    xmof_CompleteStructuredActivities_ConditionalNode,
    xmof_CompleteStructuredActivities_LoopNode,
    ObjectNode,
    xmof_ExtraStructuredActivities_ExpansionNode,
    xmof_IntermediateActivities_ActivityParameterNode,
    FinalNode,
    xmof_IntermediateActivities_ActivityFinalNode,
    IntermediateActivities_ObjectFlow,
    CompleteStructuredActivities_StructuredActivityNode,
    IntermediateActivities_ActivityNode,
    IntermediateActivities_Activity,
    xmof_IntermediateActivities_ActivityEdge,
    ActivityEdge,
    xmof_IntermediateActivities_ControlFlow,
    xmof_IntermediateActivities_ObjectFlow,
    xmof_IntermediateActivities_ActivityNode,
    IntermediateActivities_ActivityEdge,
    xmof_IntermediateActivities_Activity,
    Kernel_InstanceSpecification,
    Kernel_ValueSpecification,
    EDataType,
    xmof_Kernel_PrimitiveType,
    LiteralSpecification,
    xmof_Kernel_LiteralUnlimitedNatural,
    xmof_Kernel_LiteralInteger,
    xmof_Kernel_LiteralString,
    xmof_Kernel_LiteralNull,
    xmof_Kernel_LiteralBoolean,
    Kernel_Slot,
    Kernel_xmof_EClassifier,
    xmof_Kernel_InstanceSpecification,
    Kernel_xmof_EStructuralFeature,
    EModelElement,
    xmof_IntermediateActions_LinkEndData,
    xmof_CompleteStructuredActivities_Clause,
    xmof_Kernel_Slot,
    EOperation,
    xmof_Kernel_BehavioredEOperation,
    BehavioredEOperation,
    xmof_Communications_Reception,
    Event,
    xmof_Communications_MessageEvent,
    Communications_Signal,
    MessageEvent,
    xmof_Communications_SignalEvent,
    ETypedElement,
    xmof_IntermediateActivities_ObjectNode,
    xmof_BasicActions_Pin,
    xmof_Kernel_ValueSpecification,
    Kernel_EEnumLiteralSpecification,
    ValueSpecification,
    xmof_Kernel_InstanceValue,
    xmof_Kernel_LiteralSpecification,
    xmof_Kernel_EnumValue,
    Kernel_xmof_EEnumLiteral,
    InstanceSpecification,
    xmof_Kernel_EEnumLiteralSpecification,
    CallConcurrencyKind,
    ExpansionKind,
    ParameterDirectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eparameter_is_not_abstract():
    assert not inspect.isabstract(EParameter)


def test_eparameter_constructor_exists():
    assert callable(EParameter.__init__)


def test_eparameter_constructor_args():
    sig = inspect.signature(EParameter.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_directedparameter_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_DirectedParameter)


def test_xmof_kernel_directedparameter_constructor_exists():
    assert callable(xmof_Kernel_DirectedParameter.__init__)


def test_xmof_kernel_directedparameter_constructor_args():
    sig = inspect.signature(xmof_Kernel_DirectedParameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_xmof_kernel_directedparameter_has_direction():
    assert hasattr(xmof_Kernel_DirectedParameter, "direction")
    descriptor = None
    for klass in xmof_Kernel_DirectedParameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicbehaviors_functionbehavior_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicBehaviors_FunctionBehavior)


def test_xmof_basicbehaviors_functionbehavior_constructor_exists():
    assert callable(xmof_BasicBehaviors_FunctionBehavior.__init__)


def test_xmof_basicbehaviors_functionbehavior_constructor_args():
    sig = inspect.signature(xmof_BasicBehaviors_FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_basicbehaviors_behavior_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors_Behavior)


def test_basicbehaviors_behavior_constructor_exists():
    assert callable(BasicBehaviors_Behavior.__init__)


def test_basicbehaviors_behavior_constructor_args():
    sig = inspect.signature(BasicBehaviors_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_eclassifier_is_not_abstract():
    assert not inspect.isabstract(EClassifier)


def test_eclassifier_constructor_exists():
    assert callable(EClassifier.__init__)


def test_eclassifier_constructor_args():
    sig = inspect.signature(EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicbehaviors_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicBehaviors_BehavioredClassifier)


def test_xmof_basicbehaviors_behavioredclassifier_constructor_exists():
    assert callable(xmof_BasicBehaviors_BehavioredClassifier.__init__)


def test_xmof_basicbehaviors_behavioredclassifier_constructor_args():
    sig = inspect.signature(xmof_BasicBehaviors_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_communications_xmof_eattribute_is_not_abstract():
    assert not inspect.isabstract(Communications_xmof_EAttribute)


def test_communications_xmof_eattribute_constructor_exists():
    assert callable(Communications_xmof_EAttribute.__init__)


def test_communications_xmof_eattribute_constructor_args():
    sig = inspect.signature(Communications_xmof_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_xmof_communications_signal_is_not_abstract():
    assert not inspect.isabstract(xmof_Communications_Signal)


def test_xmof_communications_signal_constructor_exists():
    assert callable(xmof_Communications_Signal.__init__)


def test_xmof_communications_signal_constructor_args():
    sig = inspect.signature(xmof_Communications_Signal.__init__)
    params = list(sig.parameters.keys())



def test_communications_event_is_not_abstract():
    assert not inspect.isabstract(Communications_Event)


def test_communications_event_constructor_exists():
    assert callable(Communications_Event.__init__)


def test_communications_event_constructor_args():
    sig = inspect.signature(Communications_Event.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_xmof_communications_event_is_not_abstract():
    assert not inspect.isabstract(xmof_Communications_Event)


def test_xmof_communications_event_constructor_exists():
    assert callable(xmof_Communications_Event.__init__)


def test_xmof_communications_event_constructor_args():
    sig = inspect.signature(xmof_Communications_Event.__init__)
    params = list(sig.parameters.keys())



def test_xmof_communications_trigger_is_not_abstract():
    assert not inspect.isabstract(xmof_Communications_Trigger)


def test_xmof_communications_trigger_constructor_exists():
    assert callable(xmof_Communications_Trigger.__init__)


def test_xmof_communications_trigger_constructor_args():
    sig = inspect.signature(xmof_Communications_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_behavioredeclass_is_not_abstract():
    assert not inspect.isabstract(BehavioredEClass)


def test_behavioredeclass_constructor_exists():
    assert callable(BehavioredEClass.__init__)


def test_behavioredeclass_constructor_args():
    sig = inspect.signature(BehavioredEClass.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicbehaviors_behavior_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicBehaviors_Behavior)


def test_xmof_basicbehaviors_behavior_constructor_exists():
    assert callable(xmof_BasicBehaviors_Behavior.__init__)


def test_xmof_basicbehaviors_behavior_constructor_args():
    sig = inspect.signature(xmof_BasicBehaviors_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "reentrant" in params, "Missing parameter 'reentrant'"

def test_xmof_basicbehaviors_behavior_has_reentrant():
    assert hasattr(xmof_BasicBehaviors_Behavior, "reentrant")
    descriptor = None
    for klass in xmof_BasicBehaviors_Behavior.__mro__:
        if "reentrant" in klass.__dict__:
            descriptor = klass.__dict__["reentrant"]
            break
    assert isinstance(descriptor, property)



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicbehaviors_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicBehaviors_OpaqueBehavior)


def test_xmof_basicbehaviors_opaquebehavior_constructor_exists():
    assert callable(xmof_BasicBehaviors_OpaqueBehavior.__init__)


def test_xmof_basicbehaviors_opaquebehavior_constructor_args():
    sig = inspect.signature(xmof_BasicBehaviors_OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_xmof_basicbehaviors_opaquebehavior_has_language():
    assert hasattr(xmof_BasicBehaviors_OpaqueBehavior, "language")
    descriptor = None
    for klass in xmof_BasicBehaviors_OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_xmof_basicbehaviors_opaquebehavior_has_body():
    assert hasattr(xmof_BasicBehaviors_OpaqueBehavior, "body")
    descriptor = None
    for klass in xmof_BasicBehaviors_OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_basicbehaviors_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors_BehavioredClassifier)


def test_basicbehaviors_behavioredclassifier_constructor_exists():
    assert callable(BasicBehaviors_BehavioredClassifier.__init__)


def test_basicbehaviors_behavioredclassifier_constructor_args():
    sig = inspect.signature(BasicBehaviors_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_behavioredeclass_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_BehavioredEClass)


def test_xmof_kernel_behavioredeclass_constructor_exists():
    assert callable(xmof_Kernel_BehavioredEClass.__init__)


def test_xmof_kernel_behavioredeclass_constructor_args():
    sig = inspect.signature(xmof_Kernel_BehavioredEClass.__init__)
    params = list(sig.parameters.keys())



def test_kernel_directedparameter_is_not_abstract():
    assert not inspect.isabstract(Kernel_DirectedParameter)


def test_kernel_directedparameter_constructor_exists():
    assert callable(Kernel_DirectedParameter.__init__)


def test_kernel_directedparameter_constructor_args():
    sig = inspect.signature(Kernel_DirectedParameter.__init__)
    params = list(sig.parameters.keys())



def test_kernel_behavioredeoperation_is_not_abstract():
    assert not inspect.isabstract(Kernel_BehavioredEOperation)


def test_kernel_behavioredeoperation_constructor_exists():
    assert callable(Kernel_BehavioredEOperation.__init__)


def test_kernel_behavioredeoperation_constructor_args():
    sig = inspect.signature(Kernel_BehavioredEOperation.__init__)
    params = list(sig.parameters.keys())



def test_basicbehaviors_parametervalue_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors_ParameterValue)


def test_basicbehaviors_parametervalue_constructor_exists():
    assert callable(BasicBehaviors_ParameterValue.__init__)


def test_basicbehaviors_parametervalue_constructor_args():
    sig = inspect.signature(BasicBehaviors_ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicbehaviors_parametervaluedefinition_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicBehaviors_ParameterValueDefinition)


def test_xmof_basicbehaviors_parametervaluedefinition_constructor_exists():
    assert callable(xmof_BasicBehaviors_ParameterValueDefinition.__init__)


def test_xmof_basicbehaviors_parametervaluedefinition_constructor_args():
    sig = inspect.signature(xmof_BasicBehaviors_ParameterValueDefinition.__init__)
    params = list(sig.parameters.keys())



def test_kernel_value_is_not_abstract():
    assert not inspect.isabstract(Kernel_Value)


def test_kernel_value_constructor_exists():
    assert callable(Kernel_Value.__init__)


def test_kernel_value_constructor_args():
    sig = inspect.signature(Kernel_Value.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicbehaviors_parametervalue_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicBehaviors_ParameterValue)


def test_xmof_basicbehaviors_parametervalue_constructor_exists():
    assert callable(xmof_BasicBehaviors_ParameterValue.__init__)


def test_xmof_basicbehaviors_parametervalue_constructor_args():
    sig = inspect.signature(xmof_BasicBehaviors_ParameterValue.__init__)
    params = list(sig.parameters.keys())



def test_primitivevalue_is_not_abstract():
    assert not inspect.isabstract(PrimitiveValue)


def test_primitivevalue_constructor_exists():
    assert callable(PrimitiveValue.__init__)


def test_primitivevalue_constructor_args():
    sig = inspect.signature(PrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_integervalue_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_IntegerValue)


def test_xmof_kernel_integervalue_constructor_exists():
    assert callable(xmof_Kernel_IntegerValue.__init__)


def test_xmof_kernel_integervalue_constructor_args():
    sig = inspect.signature(xmof_Kernel_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof_kernel_integervalue_has_value():
    assert hasattr(xmof_Kernel_IntegerValue, "value")
    descriptor = None
    for klass in xmof_Kernel_IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xmof_kernel_stringvalue_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_StringValue)


def test_xmof_kernel_stringvalue_constructor_exists():
    assert callable(xmof_Kernel_StringValue.__init__)


def test_xmof_kernel_stringvalue_constructor_args():
    sig = inspect.signature(xmof_Kernel_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof_kernel_stringvalue_has_value():
    assert hasattr(xmof_Kernel_StringValue, "value")
    descriptor = None
    for klass in xmof_Kernel_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kernel_primitivetype_is_not_abstract():
    assert not inspect.isabstract(Kernel_PrimitiveType)


def test_kernel_primitivetype_constructor_exists():
    assert callable(Kernel_PrimitiveType.__init__)


def test_kernel_primitivetype_constructor_args():
    sig = inspect.signature(Kernel_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_enumerationvalue_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_EnumerationValue)


def test_xmof_kernel_enumerationvalue_constructor_exists():
    assert callable(xmof_Kernel_EnumerationValue.__init__)


def test_xmof_kernel_enumerationvalue_constructor_args():
    sig = inspect.signature(xmof_Kernel_EnumerationValue.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_primitivevalue_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_PrimitiveValue)


def test_xmof_kernel_primitivevalue_constructor_exists():
    assert callable(xmof_Kernel_PrimitiveValue.__init__)


def test_xmof_kernel_primitivevalue_constructor_args():
    sig = inspect.signature(xmof_Kernel_PrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_xmof_locil1_semanticvisitor_is_not_abstract():
    assert not inspect.isabstract(xmof_LociL1_SemanticVisitor)


def test_xmof_locil1_semanticvisitor_constructor_exists():
    assert callable(xmof_LociL1_SemanticVisitor.__init__)


def test_xmof_locil1_semanticvisitor_constructor_args():
    sig = inspect.signature(xmof_LociL1_SemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_kernel_xmof_eobject_is_not_abstract():
    assert not inspect.isabstract(Kernel_xmof_EObject)


def test_kernel_xmof_eobject_constructor_exists():
    assert callable(Kernel_xmof_EObject.__init__)


def test_kernel_xmof_eobject_constructor_args():
    sig = inspect.signature(Kernel_xmof_EObject.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_objectvalue_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_ObjectValue)


def test_xmof_kernel_objectvalue_constructor_exists():
    assert callable(xmof_Kernel_ObjectValue.__init__)


def test_xmof_kernel_objectvalue_constructor_args():
    sig = inspect.signature(xmof_Kernel_ObjectValue.__init__)
    params = list(sig.parameters.keys())



def test_semanticvisitor_is_not_abstract():
    assert not inspect.isabstract(SemanticVisitor)


def test_semanticvisitor_constructor_exists():
    assert callable(SemanticVisitor.__init__)


def test_semanticvisitor_constructor_args():
    sig = inspect.signature(SemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_value_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_Value)


def test_xmof_kernel_value_constructor_exists():
    assert callable(xmof_Kernel_Value.__init__)


def test_xmof_kernel_value_constructor_args():
    sig = inspect.signature(xmof_Kernel_Value.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_BooleanValue)


def test_xmof_kernel_booleanvalue_constructor_exists():
    assert callable(xmof_Kernel_BooleanValue.__init__)


def test_xmof_kernel_booleanvalue_constructor_args():
    sig = inspect.signature(xmof_Kernel_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof_kernel_booleanvalue_has_value():
    assert hasattr(xmof_Kernel_BooleanValue, "value")
    descriptor = None
    for klass in xmof_Kernel_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kernel_xmof_eenum_is_not_abstract():
    assert not inspect.isabstract(Kernel_xmof_EEnum)


def test_kernel_xmof_eenum_constructor_exists():
    assert callable(Kernel_xmof_EEnum.__init__)


def test_kernel_xmof_eenum_constructor_args():
    sig = inspect.signature(Kernel_xmof_EEnum.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicactions_callaction_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_CallAction)


def test_xmof_basicactions_callaction_constructor_exists():
    assert callable(xmof_BasicActions_CallAction.__init__)


def test_xmof_basicactions_callaction_constructor_args():
    sig = inspect.signature(xmof_BasicActions_CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "synchronous" in params, "Missing parameter 'synchronous'"

def test_xmof_basicactions_callaction_has_synchronous():
    assert hasattr(xmof_BasicActions_CallAction, "synchronous")
    descriptor = None
    for klass in xmof_BasicActions_CallAction.__mro__:
        if "synchronous" in klass.__dict__:
            descriptor = klass.__dict__["synchronous"]
            break
    assert isinstance(descriptor, property)



def test_intermediateactivities_objectnode_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_ObjectNode)


def test_intermediateactivities_objectnode_constructor_exists():
    assert callable(IntermediateActivities_ObjectNode.__init__)


def test_intermediateactivities_objectnode_constructor_args():
    sig = inspect.signature(IntermediateActivities_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicactions_outputpin_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_OutputPin)


def test_xmof_basicactions_outputpin_constructor_exists():
    assert callable(xmof_BasicActions_OutputPin.__init__)


def test_xmof_basicactions_outputpin_constructor_args():
    sig = inspect.signature(xmof_BasicActions_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicactions_inputpin_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_InputPin)


def test_xmof_basicactions_inputpin_constructor_exists():
    assert callable(xmof_BasicActions_InputPin.__init__)


def test_xmof_basicactions_inputpin_constructor_args():
    sig = inspect.signature(xmof_BasicActions_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicactions_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_SendSignalAction)


def test_xmof_basicactions_sendsignalaction_constructor_exists():
    assert callable(xmof_BasicActions_SendSignalAction.__init__)


def test_xmof_basicactions_sendsignalaction_constructor_args():
    sig = inspect.signature(xmof_BasicActions_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_xmof_eclassifier_is_not_abstract():
    assert not inspect.isabstract(BasicActions_xmof_EClassifier)


def test_basicactions_xmof_eclassifier_constructor_exists():
    assert callable(BasicActions_xmof_EClassifier.__init__)


def test_basicactions_xmof_eclassifier_constructor_args():
    sig = inspect.signature(BasicActions_xmof_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicactions_action_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_Action)


def test_xmof_basicactions_action_constructor_exists():
    assert callable(xmof_BasicActions_Action.__init__)


def test_xmof_basicactions_action_constructor_args():
    sig = inspect.signature(xmof_BasicActions_Action.__init__)
    params = list(sig.parameters.keys())
    assert "locallyReentrant" in params, "Missing parameter 'locallyReentrant'"

def test_xmof_basicactions_action_has_locallyReentrant():
    assert hasattr(xmof_BasicActions_Action, "locallyReentrant")
    descriptor = None
    for klass in xmof_BasicActions_Action.__mro__:
        if "locallyReentrant" in klass.__dict__:
            descriptor = klass.__dict__["locallyReentrant"]
            break
    assert isinstance(descriptor, property)



def test_communications_trigger_is_not_abstract():
    assert not inspect.isabstract(Communications_Trigger)


def test_communications_trigger_constructor_exists():
    assert callable(Communications_Trigger.__init__)


def test_communications_trigger_constructor_args():
    sig = inspect.signature(Communications_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_completeactions_xmof_eclassifier_is_not_abstract():
    assert not inspect.isabstract(CompleteActions_xmof_EClassifier)


def test_completeactions_xmof_eclassifier_constructor_exists():
    assert callable(CompleteActions_xmof_EClassifier.__init__)


def test_completeactions_xmof_eclassifier_constructor_args():
    sig = inspect.signature(CompleteActions_xmof_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_CreateLinkAction)


def test_xmof_intermediateactions_createlinkaction_constructor_exists():
    assert callable(xmof_IntermediateActions_CreateLinkAction.__init__)


def test_xmof_intermediateactions_createlinkaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicactions_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_CallOperationAction)


def test_xmof_basicactions_calloperationaction_constructor_exists():
    assert callable(xmof_BasicActions_CallOperationAction.__init__)


def test_xmof_basicactions_calloperationaction_constructor_args():
    sig = inspect.signature(xmof_BasicActions_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicactions_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_CallBehaviorAction)


def test_xmof_basicactions_callbehavioraction_constructor_exists():
    assert callable(xmof_BasicActions_CallBehaviorAction.__init__)


def test_xmof_basicactions_callbehavioraction_constructor_args():
    sig = inspect.signature(xmof_BasicActions_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_completeactions_startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_StartObjectBehaviorAction)


def test_xmof_completeactions_startobjectbehavioraction_constructor_exists():
    assert callable(xmof_CompleteActions_StartObjectBehaviorAction.__init__)


def test_xmof_completeactions_startobjectbehavioraction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_DestroyLinkAction)


def test_xmof_intermediateactions_destroylinkaction_constructor_exists():
    assert callable(xmof_IntermediateActions_DestroyLinkAction.__init__)


def test_xmof_intermediateactions_destroylinkaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_xmof_eclassifier_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_xmof_EClassifier)


def test_intermediateactions_xmof_eclassifier_constructor_exists():
    assert callable(IntermediateActions_xmof_EClassifier.__init__)


def test_intermediateactions_xmof_eclassifier_constructor_args():
    sig = inspect.signature(IntermediateActions_xmof_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_AddStructuralFeatureValueAction)


def test_xmof_intermediateactions_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(xmof_IntermediateActions_AddStructuralFeatureValueAction.__init__)


def test_xmof_intermediateactions_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_xmof_intermediateactions_addstructuralfeaturevalueaction_has_replaceAll():
    assert hasattr(xmof_IntermediateActions_AddStructuralFeatureValueAction, "replaceAll")
    descriptor = None
    for klass in xmof_IntermediateActions_AddStructuralFeatureValueAction.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_xmof_intermediateactions_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_RemoveStructuralFeatureValueAction)


def test_xmof_intermediateactions_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(xmof_IntermediateActions_RemoveStructuralFeatureValueAction.__init__)


def test_xmof_intermediateactions_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "removeDuplicates" in params, "Missing parameter 'removeDuplicates'"

def test_xmof_intermediateactions_removestructuralfeaturevalueaction_has_removeDuplicates():
    assert hasattr(xmof_IntermediateActions_RemoveStructuralFeatureValueAction, "removeDuplicates")
    descriptor = None
    for klass in xmof_IntermediateActions_RemoveStructuralFeatureValueAction.__mro__:
        if "removeDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["removeDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_ClearStructuralFeatureAction)


def test_xmof_intermediateactions_clearstructuralfeatureaction_constructor_exists():
    assert callable(xmof_IntermediateActions_ClearStructuralFeatureAction.__init__)


def test_xmof_intermediateactions_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_WriteStructuralFeatureAction)


def test_xmof_intermediateactions_writestructuralfeatureaction_constructor_exists():
    assert callable(xmof_IntermediateActions_WriteStructuralFeatureAction.__init__)


def test_xmof_intermediateactions_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_xmof_ereference_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_xmof_EReference)


def test_intermediateactions_xmof_ereference_constructor_exists():
    assert callable(IntermediateActions_xmof_EReference.__init__)


def test_intermediateactions_xmof_ereference_constructor_args():
    sig = inspect.signature(IntermediateActions_xmof_EReference.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_LinkEndDestructionData)


def test_xmof_intermediateactions_linkenddestructiondata_constructor_exists():
    assert callable(xmof_IntermediateActions_LinkEndDestructionData.__init__)


def test_xmof_intermediateactions_linkenddestructiondata_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "destroyDuplicates" in params, "Missing parameter 'destroyDuplicates'"

def test_xmof_intermediateactions_linkenddestructiondata_has_destroyDuplicates():
    assert hasattr(xmof_IntermediateActions_LinkEndDestructionData, "destroyDuplicates")
    descriptor = None
    for klass in xmof_IntermediateActions_LinkEndDestructionData.__mro__:
        if "destroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["destroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_xmof_intermediateactions_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_LinkEndCreationData)


def test_xmof_intermediateactions_linkendcreationdata_constructor_exists():
    assert callable(xmof_IntermediateActions_LinkEndCreationData.__init__)


def test_xmof_intermediateactions_linkendcreationdata_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_xmof_intermediateactions_linkendcreationdata_has_replaceAll():
    assert hasattr(xmof_IntermediateActions_LinkEndCreationData, "replaceAll")
    descriptor = None
    for klass in xmof_IntermediateActions_LinkEndCreationData.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_xmof_intermediateactions_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_ReadStructuralFeatureAction)


def test_xmof_intermediateactions_readstructuralfeatureaction_constructor_exists():
    assert callable(xmof_IntermediateActions_ReadStructuralFeatureAction.__init__)


def test_xmof_intermediateactions_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_xmof_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_xmof_EStructuralFeature)


def test_intermediateactions_xmof_estructuralfeature_constructor_exists():
    assert callable(IntermediateActions_xmof_EStructuralFeature.__init__)


def test_intermediateactions_xmof_estructuralfeature_constructor_args():
    sig = inspect.signature(IntermediateActions_xmof_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_linkenddata_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_LinkEndData)


def test_intermediateactions_linkenddata_constructor_exists():
    assert callable(IntermediateActions_LinkEndData.__init__)


def test_intermediateactions_linkenddata_constructor_args():
    sig = inspect.signature(IntermediateActions_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_ReadLinkAction)


def test_xmof_intermediateactions_readlinkaction_constructor_exists():
    assert callable(xmof_IntermediateActions_ReadLinkAction.__init__)


def test_xmof_intermediateactions_readlinkaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_WriteLinkAction)


def test_xmof_intermediateactions_writelinkaction_constructor_exists():
    assert callable(xmof_IntermediateActions_WriteLinkAction.__init__)


def test_xmof_intermediateactions_writelinkaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_xmof_completeactions_reduceaction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_ReduceAction)


def test_xmof_completeactions_reduceaction_constructor_exists():
    assert callable(xmof_CompleteActions_ReduceAction.__init__)


def test_xmof_completeactions_reduceaction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"

def test_xmof_completeactions_reduceaction_has_ordered():
    assert hasattr(xmof_CompleteActions_ReduceAction, "ordered")
    descriptor = None
    for klass in xmof_CompleteActions_ReduceAction.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)



def test_xmof_intermediateactions_clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_ClearAssociationAction)


def test_xmof_intermediateactions_clearassociationaction_constructor_exists():
    assert callable(xmof_IntermediateActions_ClearAssociationAction.__init__)


def test_xmof_intermediateactions_clearassociationaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicactions_invocationaction_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_InvocationAction)


def test_xmof_basicactions_invocationaction_constructor_exists():
    assert callable(xmof_BasicActions_InvocationAction.__init__)


def test_xmof_basicactions_invocationaction_constructor_args():
    sig = inspect.signature(xmof_BasicActions_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_completeactions_readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_ReadIsClassifiedObjectAction)


def test_xmof_completeactions_readisclassifiedobjectaction_constructor_exists():
    assert callable(xmof_CompleteActions_ReadIsClassifiedObjectAction.__init__)


def test_xmof_completeactions_readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "direct" in params, "Missing parameter 'direct'"

def test_xmof_completeactions_readisclassifiedobjectaction_has_direct():
    assert hasattr(xmof_CompleteActions_ReadIsClassifiedObjectAction, "direct")
    descriptor = None
    for klass in xmof_CompleteActions_ReadIsClassifiedObjectAction.__mro__:
        if "direct" in klass.__dict__:
            descriptor = klass.__dict__["direct"]
            break
    assert isinstance(descriptor, property)



def test_xmof_intermediateactions_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_StructuralFeatureAction)


def test_xmof_intermediateactions_structuralfeatureaction_constructor_exists():
    assert callable(xmof_IntermediateActions_StructuralFeatureAction.__init__)


def test_xmof_intermediateactions_structuralfeatureaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_CreateObjectAction)


def test_xmof_intermediateactions_createobjectaction_constructor_exists():
    assert callable(xmof_IntermediateActions_CreateObjectAction.__init__)


def test_xmof_intermediateactions_createobjectaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_DestroyObjectAction)


def test_xmof_intermediateactions_destroyobjectaction_constructor_exists():
    assert callable(xmof_IntermediateActions_DestroyObjectAction.__init__)


def test_xmof_intermediateactions_destroyobjectaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "destroyLinks" in params, "Missing parameter 'destroyLinks'"
    assert "destroyOwnedObjects" in params, "Missing parameter 'destroyOwnedObjects'"

def test_xmof_intermediateactions_destroyobjectaction_has_destroyLinks():
    assert hasattr(xmof_IntermediateActions_DestroyObjectAction, "destroyLinks")
    descriptor = None
    for klass in xmof_IntermediateActions_DestroyObjectAction.__mro__:
        if "destroyLinks" in klass.__dict__:
            descriptor = klass.__dict__["destroyLinks"]
            break
    assert isinstance(descriptor, property)

def test_xmof_intermediateactions_destroyobjectaction_has_destroyOwnedObjects():
    assert hasattr(xmof_IntermediateActions_DestroyObjectAction, "destroyOwnedObjects")
    descriptor = None
    for klass in xmof_IntermediateActions_DestroyObjectAction.__mro__:
        if "destroyOwnedObjects" in klass.__dict__:
            descriptor = klass.__dict__["destroyOwnedObjects"]
            break
    assert isinstance(descriptor, property)



def test_xmof_intermediateactions_valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_ValueSpecificationAction)


def test_xmof_intermediateactions_valuespecificationaction_constructor_exists():
    assert callable(xmof_IntermediateActions_ValueSpecificationAction.__init__)


def test_xmof_intermediateactions_valuespecificationaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_completeactions_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_ReclassifyObjectAction)


def test_xmof_completeactions_reclassifyobjectaction_constructor_exists():
    assert callable(xmof_CompleteActions_ReclassifyObjectAction.__init__)


def test_xmof_completeactions_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_xmof_completeactions_reclassifyobjectaction_has_replaceAll():
    assert hasattr(xmof_CompleteActions_ReclassifyObjectAction, "replaceAll")
    descriptor = None
    for klass in xmof_CompleteActions_ReclassifyObjectAction.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_xmof_intermediateactions_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_TestIdentityAction)


def test_xmof_intermediateactions_testidentityaction_constructor_exists():
    assert callable(xmof_IntermediateActions_TestIdentityAction.__init__)


def test_xmof_intermediateactions_testidentityaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_linkaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_LinkAction)


def test_xmof_intermediateactions_linkaction_constructor_exists():
    assert callable(xmof_IntermediateActions_LinkAction.__init__)


def test_xmof_intermediateactions_linkaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_completeactions_startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_StartClassifierBehaviorAction)


def test_xmof_completeactions_startclassifierbehavioraction_constructor_exists():
    assert callable(xmof_CompleteActions_StartClassifierBehaviorAction.__init__)


def test_xmof_completeactions_startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_completeactions_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_AcceptEventAction)


def test_xmof_completeactions_accepteventaction_constructor_exists():
    assert callable(xmof_CompleteActions_AcceptEventAction.__init__)


def test_xmof_completeactions_accepteventaction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "unmarshall" in params, "Missing parameter 'unmarshall'"

def test_xmof_completeactions_accepteventaction_has_unmarshall():
    assert hasattr(xmof_CompleteActions_AcceptEventAction, "unmarshall")
    descriptor = None
    for klass in xmof_CompleteActions_AcceptEventAction.__mro__:
        if "unmarshall" in klass.__dict__:
            descriptor = klass.__dict__["unmarshall"]
            break
    assert isinstance(descriptor, property)



def test_xmof_completeactions_readextentaction_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteActions_ReadExtentAction)


def test_xmof_completeactions_readextentaction_constructor_exists():
    assert callable(xmof_CompleteActions_ReadExtentAction.__init__)


def test_xmof_completeactions_readextentaction_constructor_args():
    sig = inspect.signature(xmof_CompleteActions_ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_readselfaction_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_ReadSelfAction)


def test_xmof_intermediateactions_readselfaction_constructor_exists():
    assert callable(xmof_IntermediateActions_ReadSelfAction.__init__)


def test_xmof_intermediateactions_readselfaction_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_xmof_completestructuredactivities_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteStructuredActivities_StructuredActivityNode)


def test_xmof_completestructuredactivities_structuredactivitynode_constructor_exists():
    assert callable(xmof_CompleteStructuredActivities_StructuredActivityNode.__init__)


def test_xmof_completestructuredactivities_structuredactivitynode_constructor_args():
    sig = inspect.signature(xmof_CompleteStructuredActivities_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_xmof_completestructuredactivities_structuredactivitynode_has_mustIsolate():
    assert hasattr(xmof_CompleteStructuredActivities_StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in xmof_CompleteStructuredActivities_StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_extrastructuredactivities_expansionnode_is_not_abstract():
    assert not inspect.isabstract(ExtraStructuredActivities_ExpansionNode)


def test_extrastructuredactivities_expansionnode_constructor_exists():
    assert callable(ExtraStructuredActivities_ExpansionNode.__init__)


def test_extrastructuredactivities_expansionnode_constructor_args():
    sig = inspect.signature(ExtraStructuredActivities_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_extrastructuredactivities_expansionregion_is_not_abstract():
    assert not inspect.isabstract(ExtraStructuredActivities_ExpansionRegion)


def test_extrastructuredactivities_expansionregion_constructor_exists():
    assert callable(ExtraStructuredActivities_ExpansionRegion.__init__)


def test_extrastructuredactivities_expansionregion_constructor_args():
    sig = inspect.signature(ExtraStructuredActivities_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_completestructuredactivities_clause_is_not_abstract():
    assert not inspect.isabstract(CompleteStructuredActivities_Clause)


def test_completestructuredactivities_clause_constructor_exists():
    assert callable(CompleteStructuredActivities_Clause.__init__)


def test_completestructuredactivities_clause_constructor_args():
    sig = inspect.signature(CompleteStructuredActivities_Clause.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_completestructuredactivities_executablenode_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteStructuredActivities_ExecutableNode)


def test_xmof_completestructuredactivities_executablenode_constructor_exists():
    assert callable(xmof_CompleteStructuredActivities_ExecutableNode.__init__)


def test_xmof_completestructuredactivities_executablenode_constructor_args():
    sig = inspect.signature(xmof_CompleteStructuredActivities_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_controlnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ControlNode)


def test_xmof_intermediateactivities_controlnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_ControlNode.__init__)


def test_xmof_intermediateactivities_controlnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_joinnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_JoinNode)


def test_xmof_intermediateactivities_joinnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_JoinNode.__init__)


def test_xmof_intermediateactivities_joinnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_finalnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_FinalNode)


def test_xmof_intermediateactivities_finalnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_FinalNode.__init__)


def test_xmof_intermediateactivities_finalnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_decisionnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_DecisionNode)


def test_xmof_intermediateactivities_decisionnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_DecisionNode.__init__)


def test_xmof_intermediateactivities_decisionnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_initialnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_InitialNode)


def test_xmof_intermediateactivities_initialnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_InitialNode.__init__)


def test_xmof_intermediateactivities_initialnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_forknode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ForkNode)


def test_xmof_intermediateactivities_forknode_constructor_exists():
    assert callable(xmof_IntermediateActivities_ForkNode.__init__)


def test_xmof_intermediateactivities_forknode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_mergenode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_MergeNode)


def test_xmof_intermediateactivities_mergenode_constructor_exists():
    assert callable(xmof_IntermediateActivities_MergeNode.__init__)


def test_xmof_intermediateactivities_mergenode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_inputpin_is_not_abstract():
    assert not inspect.isabstract(BasicActions_InputPin)


def test_basicactions_inputpin_constructor_exists():
    assert callable(BasicActions_InputPin.__init__)


def test_basicactions_inputpin_constructor_args():
    sig = inspect.signature(BasicActions_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_completestructuredactivities_executablenode_is_not_abstract():
    assert not inspect.isabstract(CompleteStructuredActivities_ExecutableNode)


def test_completestructuredactivities_executablenode_constructor_exists():
    assert callable(CompleteStructuredActivities_ExecutableNode.__init__)


def test_completestructuredactivities_executablenode_constructor_args():
    sig = inspect.signature(CompleteStructuredActivities_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_basicactions_outputpin_is_not_abstract():
    assert not inspect.isabstract(BasicActions_OutputPin)


def test_basicactions_outputpin_constructor_exists():
    assert callable(BasicActions_OutputPin.__init__)


def test_basicactions_outputpin_constructor_args():
    sig = inspect.signature(BasicActions_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_extrastructuredactivities_expansionregion_is_not_abstract():
    assert not inspect.isabstract(xmof_ExtraStructuredActivities_ExpansionRegion)


def test_xmof_extrastructuredactivities_expansionregion_constructor_exists():
    assert callable(xmof_ExtraStructuredActivities_ExpansionRegion.__init__)


def test_xmof_extrastructuredactivities_expansionregion_constructor_args():
    sig = inspect.signature(xmof_ExtraStructuredActivities_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_xmof_extrastructuredactivities_expansionregion_has_mode():
    assert hasattr(xmof_ExtraStructuredActivities_ExpansionRegion, "mode")
    descriptor = None
    for klass in xmof_ExtraStructuredActivities_ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_xmof_completestructuredactivities_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteStructuredActivities_ConditionalNode)


def test_xmof_completestructuredactivities_conditionalnode_constructor_exists():
    assert callable(xmof_CompleteStructuredActivities_ConditionalNode.__init__)


def test_xmof_completestructuredactivities_conditionalnode_constructor_args():
    sig = inspect.signature(xmof_CompleteStructuredActivities_ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "determinate" in params, "Missing parameter 'determinate'"
    assert "assured" in params, "Missing parameter 'assured'"

def test_xmof_completestructuredactivities_conditionalnode_has_determinate():
    assert hasattr(xmof_CompleteStructuredActivities_ConditionalNode, "determinate")
    descriptor = None
    for klass in xmof_CompleteStructuredActivities_ConditionalNode.__mro__:
        if "determinate" in klass.__dict__:
            descriptor = klass.__dict__["determinate"]
            break
    assert isinstance(descriptor, property)

def test_xmof_completestructuredactivities_conditionalnode_has_assured():
    assert hasattr(xmof_CompleteStructuredActivities_ConditionalNode, "assured")
    descriptor = None
    for klass in xmof_CompleteStructuredActivities_ConditionalNode.__mro__:
        if "assured" in klass.__dict__:
            descriptor = klass.__dict__["assured"]
            break
    assert isinstance(descriptor, property)



def test_xmof_completestructuredactivities_loopnode_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteStructuredActivities_LoopNode)


def test_xmof_completestructuredactivities_loopnode_constructor_exists():
    assert callable(xmof_CompleteStructuredActivities_LoopNode.__init__)


def test_xmof_completestructuredactivities_loopnode_constructor_args():
    sig = inspect.signature(xmof_CompleteStructuredActivities_LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "testedFirst" in params, "Missing parameter 'testedFirst'"

def test_xmof_completestructuredactivities_loopnode_has_testedFirst():
    assert hasattr(xmof_CompleteStructuredActivities_LoopNode, "testedFirst")
    descriptor = None
    for klass in xmof_CompleteStructuredActivities_LoopNode.__mro__:
        if "testedFirst" in klass.__dict__:
            descriptor = klass.__dict__["testedFirst"]
            break
    assert isinstance(descriptor, property)



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_extrastructuredactivities_expansionnode_is_not_abstract():
    assert not inspect.isabstract(xmof_ExtraStructuredActivities_ExpansionNode)


def test_xmof_extrastructuredactivities_expansionnode_constructor_exists():
    assert callable(xmof_ExtraStructuredActivities_ExpansionNode.__init__)


def test_xmof_extrastructuredactivities_expansionnode_constructor_args():
    sig = inspect.signature(xmof_ExtraStructuredActivities_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ActivityParameterNode)


def test_xmof_intermediateactivities_activityparameternode_constructor_exists():
    assert callable(xmof_IntermediateActivities_ActivityParameterNode.__init__)


def test_xmof_intermediateactivities_activityparameternode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ActivityFinalNode)


def test_xmof_intermediateactivities_activityfinalnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_ActivityFinalNode.__init__)


def test_xmof_intermediateactivities_activityfinalnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_objectflow_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_ObjectFlow)


def test_intermediateactivities_objectflow_constructor_exists():
    assert callable(IntermediateActivities_ObjectFlow.__init__)


def test_intermediateactivities_objectflow_constructor_args():
    sig = inspect.signature(IntermediateActivities_ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_completestructuredactivities_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(CompleteStructuredActivities_StructuredActivityNode)


def test_completestructuredactivities_structuredactivitynode_constructor_exists():
    assert callable(CompleteStructuredActivities_StructuredActivityNode.__init__)


def test_completestructuredactivities_structuredactivitynode_constructor_args():
    sig = inspect.signature(CompleteStructuredActivities_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_activitynode_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_ActivityNode)


def test_intermediateactivities_activitynode_constructor_exists():
    assert callable(IntermediateActivities_ActivityNode.__init__)


def test_intermediateactivities_activitynode_constructor_args():
    sig = inspect.signature(IntermediateActivities_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_activity_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_Activity)


def test_intermediateactivities_activity_constructor_exists():
    assert callable(IntermediateActivities_Activity.__init__)


def test_intermediateactivities_activity_constructor_args():
    sig = inspect.signature(IntermediateActivities_Activity.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_activityedge_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ActivityEdge)


def test_xmof_intermediateactivities_activityedge_constructor_exists():
    assert callable(xmof_IntermediateActivities_ActivityEdge.__init__)


def test_xmof_intermediateactivities_activityedge_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_controlflow_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ControlFlow)


def test_xmof_intermediateactivities_controlflow_constructor_exists():
    assert callable(xmof_IntermediateActivities_ControlFlow.__init__)


def test_xmof_intermediateactivities_controlflow_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_objectflow_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ObjectFlow)


def test_xmof_intermediateactivities_objectflow_constructor_exists():
    assert callable(xmof_IntermediateActivities_ObjectFlow.__init__)


def test_xmof_intermediateactivities_objectflow_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_activitynode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ActivityNode)


def test_xmof_intermediateactivities_activitynode_constructor_exists():
    assert callable(xmof_IntermediateActivities_ActivityNode.__init__)


def test_xmof_intermediateactivities_activitynode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_activityedge_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_ActivityEdge)


def test_intermediateactivities_activityedge_constructor_exists():
    assert callable(IntermediateActivities_ActivityEdge.__init__)


def test_intermediateactivities_activityedge_constructor_args():
    sig = inspect.signature(IntermediateActivities_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_activity_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_Activity)


def test_xmof_intermediateactivities_activity_constructor_exists():
    assert callable(xmof_IntermediateActivities_Activity.__init__)


def test_xmof_intermediateactivities_activity_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_xmof_intermediateactivities_activity_has_readOnly():
    assert hasattr(xmof_IntermediateActivities_Activity, "readOnly")
    descriptor = None
    for klass in xmof_IntermediateActivities_Activity.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_kernel_instancespecification_is_not_abstract():
    assert not inspect.isabstract(Kernel_InstanceSpecification)


def test_kernel_instancespecification_constructor_exists():
    assert callable(Kernel_InstanceSpecification.__init__)


def test_kernel_instancespecification_constructor_args():
    sig = inspect.signature(Kernel_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_kernel_valuespecification_is_not_abstract():
    assert not inspect.isabstract(Kernel_ValueSpecification)


def test_kernel_valuespecification_constructor_exists():
    assert callable(Kernel_ValueSpecification.__init__)


def test_kernel_valuespecification_constructor_args():
    sig = inspect.signature(Kernel_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_primitivetype_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_PrimitiveType)


def test_xmof_kernel_primitivetype_constructor_exists():
    assert callable(xmof_Kernel_PrimitiveType.__init__)


def test_xmof_kernel_primitivetype_constructor_args():
    sig = inspect.signature(xmof_Kernel_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_LiteralUnlimitedNatural)


def test_xmof_kernel_literalunlimitednatural_constructor_exists():
    assert callable(xmof_Kernel_LiteralUnlimitedNatural.__init__)


def test_xmof_kernel_literalunlimitednatural_constructor_args():
    sig = inspect.signature(xmof_Kernel_LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof_kernel_literalunlimitednatural_has_value():
    assert hasattr(xmof_Kernel_LiteralUnlimitedNatural, "value")
    descriptor = None
    for klass in xmof_Kernel_LiteralUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xmof_kernel_literalinteger_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_LiteralInteger)


def test_xmof_kernel_literalinteger_constructor_exists():
    assert callable(xmof_Kernel_LiteralInteger.__init__)


def test_xmof_kernel_literalinteger_constructor_args():
    sig = inspect.signature(xmof_Kernel_LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof_kernel_literalinteger_has_value():
    assert hasattr(xmof_Kernel_LiteralInteger, "value")
    descriptor = None
    for klass in xmof_Kernel_LiteralInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xmof_kernel_literalstring_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_LiteralString)


def test_xmof_kernel_literalstring_constructor_exists():
    assert callable(xmof_Kernel_LiteralString.__init__)


def test_xmof_kernel_literalstring_constructor_args():
    sig = inspect.signature(xmof_Kernel_LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof_kernel_literalstring_has_value():
    assert hasattr(xmof_Kernel_LiteralString, "value")
    descriptor = None
    for klass in xmof_Kernel_LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xmof_kernel_literalnull_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_LiteralNull)


def test_xmof_kernel_literalnull_constructor_exists():
    assert callable(xmof_Kernel_LiteralNull.__init__)


def test_xmof_kernel_literalnull_constructor_args():
    sig = inspect.signature(xmof_Kernel_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_literalboolean_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_LiteralBoolean)


def test_xmof_kernel_literalboolean_constructor_exists():
    assert callable(xmof_Kernel_LiteralBoolean.__init__)


def test_xmof_kernel_literalboolean_constructor_args():
    sig = inspect.signature(xmof_Kernel_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xmof_kernel_literalboolean_has_value():
    assert hasattr(xmof_Kernel_LiteralBoolean, "value")
    descriptor = None
    for klass in xmof_Kernel_LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kernel_slot_is_not_abstract():
    assert not inspect.isabstract(Kernel_Slot)


def test_kernel_slot_constructor_exists():
    assert callable(Kernel_Slot.__init__)


def test_kernel_slot_constructor_args():
    sig = inspect.signature(Kernel_Slot.__init__)
    params = list(sig.parameters.keys())



def test_kernel_xmof_eclassifier_is_not_abstract():
    assert not inspect.isabstract(Kernel_xmof_EClassifier)


def test_kernel_xmof_eclassifier_constructor_exists():
    assert callable(Kernel_xmof_EClassifier.__init__)


def test_kernel_xmof_eclassifier_constructor_args():
    sig = inspect.signature(Kernel_xmof_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_instancespecification_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_InstanceSpecification)


def test_xmof_kernel_instancespecification_constructor_exists():
    assert callable(xmof_Kernel_InstanceSpecification.__init__)


def test_xmof_kernel_instancespecification_constructor_args():
    sig = inspect.signature(xmof_Kernel_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_kernel_xmof_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(Kernel_xmof_EStructuralFeature)


def test_kernel_xmof_estructuralfeature_constructor_exists():
    assert callable(Kernel_xmof_EStructuralFeature.__init__)


def test_kernel_xmof_estructuralfeature_constructor_args():
    sig = inspect.signature(Kernel_xmof_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactions_linkenddata_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActions_LinkEndData)


def test_xmof_intermediateactions_linkenddata_constructor_exists():
    assert callable(xmof_IntermediateActions_LinkEndData.__init__)


def test_xmof_intermediateactions_linkenddata_constructor_args():
    sig = inspect.signature(xmof_IntermediateActions_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_xmof_completestructuredactivities_clause_is_not_abstract():
    assert not inspect.isabstract(xmof_CompleteStructuredActivities_Clause)


def test_xmof_completestructuredactivities_clause_constructor_exists():
    assert callable(xmof_CompleteStructuredActivities_Clause.__init__)


def test_xmof_completestructuredactivities_clause_constructor_args():
    sig = inspect.signature(xmof_CompleteStructuredActivities_Clause.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_slot_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_Slot)


def test_xmof_kernel_slot_constructor_exists():
    assert callable(xmof_Kernel_Slot.__init__)


def test_xmof_kernel_slot_constructor_args():
    sig = inspect.signature(xmof_Kernel_Slot.__init__)
    params = list(sig.parameters.keys())



def test_eoperation_is_not_abstract():
    assert not inspect.isabstract(EOperation)


def test_eoperation_constructor_exists():
    assert callable(EOperation.__init__)


def test_eoperation_constructor_args():
    sig = inspect.signature(EOperation.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_behavioredeoperation_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_BehavioredEOperation)


def test_xmof_kernel_behavioredeoperation_constructor_exists():
    assert callable(xmof_Kernel_BehavioredEOperation.__init__)


def test_xmof_kernel_behavioredeoperation_constructor_args():
    sig = inspect.signature(xmof_Kernel_BehavioredEOperation.__init__)
    params = list(sig.parameters.keys())



def test_behavioredeoperation_is_not_abstract():
    assert not inspect.isabstract(BehavioredEOperation)


def test_behavioredeoperation_constructor_exists():
    assert callable(BehavioredEOperation.__init__)


def test_behavioredeoperation_constructor_args():
    sig = inspect.signature(BehavioredEOperation.__init__)
    params = list(sig.parameters.keys())



def test_xmof_communications_reception_is_not_abstract():
    assert not inspect.isabstract(xmof_Communications_Reception)


def test_xmof_communications_reception_constructor_exists():
    assert callable(xmof_Communications_Reception.__init__)


def test_xmof_communications_reception_constructor_args():
    sig = inspect.signature(xmof_Communications_Reception.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_xmof_communications_messageevent_is_not_abstract():
    assert not inspect.isabstract(xmof_Communications_MessageEvent)


def test_xmof_communications_messageevent_constructor_exists():
    assert callable(xmof_Communications_MessageEvent.__init__)


def test_xmof_communications_messageevent_constructor_args():
    sig = inspect.signature(xmof_Communications_MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_communications_signal_is_not_abstract():
    assert not inspect.isabstract(Communications_Signal)


def test_communications_signal_constructor_exists():
    assert callable(Communications_Signal.__init__)


def test_communications_signal_constructor_args():
    sig = inspect.signature(Communications_Signal.__init__)
    params = list(sig.parameters.keys())



def test_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_xmof_communications_signalevent_is_not_abstract():
    assert not inspect.isabstract(xmof_Communications_SignalEvent)


def test_xmof_communications_signalevent_constructor_exists():
    assert callable(xmof_Communications_SignalEvent.__init__)


def test_xmof_communications_signalevent_constructor_args():
    sig = inspect.signature(xmof_Communications_SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_etypedelement_is_not_abstract():
    assert not inspect.isabstract(ETypedElement)


def test_etypedelement_constructor_exists():
    assert callable(ETypedElement.__init__)


def test_etypedelement_constructor_args():
    sig = inspect.signature(ETypedElement.__init__)
    params = list(sig.parameters.keys())



def test_xmof_intermediateactivities_objectnode_is_not_abstract():
    assert not inspect.isabstract(xmof_IntermediateActivities_ObjectNode)


def test_xmof_intermediateactivities_objectnode_constructor_exists():
    assert callable(xmof_IntermediateActivities_ObjectNode.__init__)


def test_xmof_intermediateactivities_objectnode_constructor_args():
    sig = inspect.signature(xmof_IntermediateActivities_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_xmof_basicactions_pin_is_not_abstract():
    assert not inspect.isabstract(xmof_BasicActions_Pin)


def test_xmof_basicactions_pin_constructor_exists():
    assert callable(xmof_BasicActions_Pin.__init__)


def test_xmof_basicactions_pin_constructor_args():
    sig = inspect.signature(xmof_BasicActions_Pin.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_valuespecification_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_ValueSpecification)


def test_xmof_kernel_valuespecification_constructor_exists():
    assert callable(xmof_Kernel_ValueSpecification.__init__)


def test_xmof_kernel_valuespecification_constructor_args():
    sig = inspect.signature(xmof_Kernel_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_kernel_eenumliteralspecification_is_not_abstract():
    assert not inspect.isabstract(Kernel_EEnumLiteralSpecification)


def test_kernel_eenumliteralspecification_constructor_exists():
    assert callable(Kernel_EEnumLiteralSpecification.__init__)


def test_kernel_eenumliteralspecification_constructor_args():
    sig = inspect.signature(Kernel_EEnumLiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_instancevalue_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_InstanceValue)


def test_xmof_kernel_instancevalue_constructor_exists():
    assert callable(xmof_Kernel_InstanceValue.__init__)


def test_xmof_kernel_instancevalue_constructor_args():
    sig = inspect.signature(xmof_Kernel_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_literalspecification_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_LiteralSpecification)


def test_xmof_kernel_literalspecification_constructor_exists():
    assert callable(xmof_Kernel_LiteralSpecification.__init__)


def test_xmof_kernel_literalspecification_constructor_args():
    sig = inspect.signature(xmof_Kernel_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_enumvalue_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_EnumValue)


def test_xmof_kernel_enumvalue_constructor_exists():
    assert callable(xmof_Kernel_EnumValue.__init__)


def test_xmof_kernel_enumvalue_constructor_args():
    sig = inspect.signature(xmof_Kernel_EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_kernel_xmof_eenumliteral_is_not_abstract():
    assert not inspect.isabstract(Kernel_xmof_EEnumLiteral)


def test_kernel_xmof_eenumliteral_constructor_exists():
    assert callable(Kernel_xmof_EEnumLiteral.__init__)


def test_kernel_xmof_eenumliteral_constructor_args():
    sig = inspect.signature(Kernel_xmof_EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_xmof_kernel_eenumliteralspecification_is_not_abstract():
    assert not inspect.isabstract(xmof_Kernel_EEnumLiteralSpecification)


def test_xmof_kernel_eenumliteralspecification_constructor_exists():
    assert callable(xmof_Kernel_EEnumLiteralSpecification.__init__)


def test_xmof_kernel_eenumliteralspecification_constructor_args():
    sig = inspect.signature(xmof_Kernel_EEnumLiteralSpecification.__init__)
    params = list(sig.parameters.keys())

def test_callconcurrencykind_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyKind is not None

def test_callconcurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyKind]
    expected_literals = [
        "sequential",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyKind"

def test_expansionkind_exists():
    # Check that the Enumeration exists
    assert ExpansionKind is not None

def test_expansionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpansionKind]
    expected_literals = [
        "stream",
        "iterative",
        "parallel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionKind"

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "inout",
        "in_",
        "out",
        "return_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"


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
EParameter_strategy = st.builds(
    EParameter,
)
xmof_Kernel_DirectedParameter_strategy = st.builds(
    xmof_Kernel_DirectedParameter,
    direction=
        safe_text
)
EClass_strategy = st.builds(
    EClass,
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
xmof_BasicBehaviors_FunctionBehavior_strategy = st.builds(
    xmof_BasicBehaviors_FunctionBehavior,
)
BasicBehaviors_Behavior_strategy = st.builds(
    BasicBehaviors_Behavior,
)
EClassifier_strategy = st.builds(
    EClassifier,
)
xmof_BasicBehaviors_BehavioredClassifier_strategy = st.builds(
    xmof_BasicBehaviors_BehavioredClassifier,
)
Communications_xmof_EAttribute_strategy = st.builds(
    Communications_xmof_EAttribute,
)
xmof_Communications_Signal_strategy = st.builds(
    xmof_Communications_Signal,
)
Communications_Event_strategy = st.builds(
    Communications_Event,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
xmof_Communications_Event_strategy = st.builds(
    xmof_Communications_Event,
)
xmof_Communications_Trigger_strategy = st.builds(
    xmof_Communications_Trigger,
)
BehavioredEClass_strategy = st.builds(
    BehavioredEClass,
)
xmof_BasicBehaviors_Behavior_strategy = st.builds(
    xmof_BasicBehaviors_Behavior,
    reentrant=
        st.booleans()
)
Behavior_strategy = st.builds(
    Behavior,
)
xmof_BasicBehaviors_OpaqueBehavior_strategy = st.builds(
    xmof_BasicBehaviors_OpaqueBehavior,
    language=
        safe_text,
    body=
        safe_text
)
BasicBehaviors_BehavioredClassifier_strategy = st.builds(
    BasicBehaviors_BehavioredClassifier,
)
xmof_Kernel_BehavioredEClass_strategy = st.builds(
    xmof_Kernel_BehavioredEClass,
)
Kernel_DirectedParameter_strategy = st.builds(
    Kernel_DirectedParameter,
)
Kernel_BehavioredEOperation_strategy = st.builds(
    Kernel_BehavioredEOperation,
)
BasicBehaviors_ParameterValue_strategy = st.builds(
    BasicBehaviors_ParameterValue,
)
xmof_BasicBehaviors_ParameterValueDefinition_strategy = st.builds(
    xmof_BasicBehaviors_ParameterValueDefinition,
)
Kernel_Value_strategy = st.builds(
    Kernel_Value,
)
xmof_BasicBehaviors_ParameterValue_strategy = st.builds(
    xmof_BasicBehaviors_ParameterValue,
)
PrimitiveValue_strategy = st.builds(
    PrimitiveValue,
)
xmof_Kernel_IntegerValue_strategy = st.builds(
    xmof_Kernel_IntegerValue,
    value=
        st.integers()
)
xmof_Kernel_StringValue_strategy = st.builds(
    xmof_Kernel_StringValue,
    value=
        safe_text
)
Kernel_PrimitiveType_strategy = st.builds(
    Kernel_PrimitiveType,
)
Value_strategy = st.builds(
    Value,
)
xmof_Kernel_EnumerationValue_strategy = st.builds(
    xmof_Kernel_EnumerationValue,
)
xmof_Kernel_PrimitiveValue_strategy = st.builds(
    xmof_Kernel_PrimitiveValue,
)
xmof_LociL1_SemanticVisitor_strategy = st.builds(
    xmof_LociL1_SemanticVisitor,
)
Kernel_xmof_EObject_strategy = st.builds(
    Kernel_xmof_EObject,
)
xmof_Kernel_ObjectValue_strategy = st.builds(
    xmof_Kernel_ObjectValue,
)
SemanticVisitor_strategy = st.builds(
    SemanticVisitor,
)
xmof_Kernel_Value_strategy = st.builds(
    xmof_Kernel_Value,
)
xmof_Kernel_BooleanValue_strategy = st.builds(
    xmof_Kernel_BooleanValue,
    value=
        st.booleans()
)
Kernel_xmof_EEnum_strategy = st.builds(
    Kernel_xmof_EEnum,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
xmof_BasicActions_CallAction_strategy = st.builds(
    xmof_BasicActions_CallAction,
    synchronous=
        st.booleans()
)
IntermediateActivities_ObjectNode_strategy = st.builds(
    IntermediateActivities_ObjectNode,
)
Pin_strategy = st.builds(
    Pin,
)
xmof_BasicActions_OutputPin_strategy = st.builds(
    xmof_BasicActions_OutputPin,
)
xmof_BasicActions_InputPin_strategy = st.builds(
    xmof_BasicActions_InputPin,
)
xmof_BasicActions_SendSignalAction_strategy = st.builds(
    xmof_BasicActions_SendSignalAction,
)
BasicActions_xmof_EClassifier_strategy = st.builds(
    BasicActions_xmof_EClassifier,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
xmof_BasicActions_Action_strategy = st.builds(
    xmof_BasicActions_Action,
    locallyReentrant=
        st.booleans()
)
Communications_Trigger_strategy = st.builds(
    Communications_Trigger,
)
CompleteActions_xmof_EClassifier_strategy = st.builds(
    CompleteActions_xmof_EClassifier,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
xmof_IntermediateActions_CreateLinkAction_strategy = st.builds(
    xmof_IntermediateActions_CreateLinkAction,
)
CallAction_strategy = st.builds(
    CallAction,
)
xmof_BasicActions_CallOperationAction_strategy = st.builds(
    xmof_BasicActions_CallOperationAction,
)
xmof_BasicActions_CallBehaviorAction_strategy = st.builds(
    xmof_BasicActions_CallBehaviorAction,
)
xmof_CompleteActions_StartObjectBehaviorAction_strategy = st.builds(
    xmof_CompleteActions_StartObjectBehaviorAction,
)
xmof_IntermediateActions_DestroyLinkAction_strategy = st.builds(
    xmof_IntermediateActions_DestroyLinkAction,
)
IntermediateActions_xmof_EClassifier_strategy = st.builds(
    IntermediateActions_xmof_EClassifier,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
xmof_IntermediateActions_AddStructuralFeatureValueAction_strategy = st.builds(
    xmof_IntermediateActions_AddStructuralFeatureValueAction,
    replaceAll=
        st.booleans()
)
xmof_IntermediateActions_RemoveStructuralFeatureValueAction_strategy = st.builds(
    xmof_IntermediateActions_RemoveStructuralFeatureValueAction,
    removeDuplicates=
        st.booleans()
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
xmof_IntermediateActions_ClearStructuralFeatureAction_strategy = st.builds(
    xmof_IntermediateActions_ClearStructuralFeatureAction,
)
xmof_IntermediateActions_WriteStructuralFeatureAction_strategy = st.builds(
    xmof_IntermediateActions_WriteStructuralFeatureAction,
)
IntermediateActions_xmof_EReference_strategy = st.builds(
    IntermediateActions_xmof_EReference,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
xmof_IntermediateActions_LinkEndDestructionData_strategy = st.builds(
    xmof_IntermediateActions_LinkEndDestructionData,
    destroyDuplicates=
        st.booleans()
)
xmof_IntermediateActions_LinkEndCreationData_strategy = st.builds(
    xmof_IntermediateActions_LinkEndCreationData,
    replaceAll=
        st.booleans()
)
xmof_IntermediateActions_ReadStructuralFeatureAction_strategy = st.builds(
    xmof_IntermediateActions_ReadStructuralFeatureAction,
)
IntermediateActions_xmof_EStructuralFeature_strategy = st.builds(
    IntermediateActions_xmof_EStructuralFeature,
)
IntermediateActions_LinkEndData_strategy = st.builds(
    IntermediateActions_LinkEndData,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
xmof_IntermediateActions_ReadLinkAction_strategy = st.builds(
    xmof_IntermediateActions_ReadLinkAction,
)
xmof_IntermediateActions_WriteLinkAction_strategy = st.builds(
    xmof_IntermediateActions_WriteLinkAction,
)
Action_strategy = st.builds(
    Action,
)
xmof_CompleteActions_ReduceAction_strategy = st.builds(
    xmof_CompleteActions_ReduceAction,
    ordered=
        st.booleans()
)
xmof_IntermediateActions_ClearAssociationAction_strategy = st.builds(
    xmof_IntermediateActions_ClearAssociationAction,
)
xmof_BasicActions_InvocationAction_strategy = st.builds(
    xmof_BasicActions_InvocationAction,
)
xmof_CompleteActions_ReadIsClassifiedObjectAction_strategy = st.builds(
    xmof_CompleteActions_ReadIsClassifiedObjectAction,
    direct=
        st.booleans()
)
xmof_IntermediateActions_StructuralFeatureAction_strategy = st.builds(
    xmof_IntermediateActions_StructuralFeatureAction,
)
xmof_IntermediateActions_CreateObjectAction_strategy = st.builds(
    xmof_IntermediateActions_CreateObjectAction,
)
xmof_IntermediateActions_DestroyObjectAction_strategy = st.builds(
    xmof_IntermediateActions_DestroyObjectAction,
    destroyLinks=
        st.booleans(),
    destroyOwnedObjects=
        st.booleans()
)
xmof_IntermediateActions_ValueSpecificationAction_strategy = st.builds(
    xmof_IntermediateActions_ValueSpecificationAction,
)
xmof_CompleteActions_ReclassifyObjectAction_strategy = st.builds(
    xmof_CompleteActions_ReclassifyObjectAction,
    replaceAll=
        st.booleans()
)
xmof_IntermediateActions_TestIdentityAction_strategy = st.builds(
    xmof_IntermediateActions_TestIdentityAction,
)
xmof_IntermediateActions_LinkAction_strategy = st.builds(
    xmof_IntermediateActions_LinkAction,
)
xmof_CompleteActions_StartClassifierBehaviorAction_strategy = st.builds(
    xmof_CompleteActions_StartClassifierBehaviorAction,
)
xmof_CompleteActions_AcceptEventAction_strategy = st.builds(
    xmof_CompleteActions_AcceptEventAction,
    unmarshall=
        st.booleans()
)
xmof_CompleteActions_ReadExtentAction_strategy = st.builds(
    xmof_CompleteActions_ReadExtentAction,
)
xmof_IntermediateActions_ReadSelfAction_strategy = st.builds(
    xmof_IntermediateActions_ReadSelfAction,
)
xmof_CompleteStructuredActivities_StructuredActivityNode_strategy = st.builds(
    xmof_CompleteStructuredActivities_StructuredActivityNode,
    mustIsolate=
        st.booleans()
)
ExtraStructuredActivities_ExpansionNode_strategy = st.builds(
    ExtraStructuredActivities_ExpansionNode,
)
ExtraStructuredActivities_ExpansionRegion_strategy = st.builds(
    ExtraStructuredActivities_ExpansionRegion,
)
CompleteStructuredActivities_Clause_strategy = st.builds(
    CompleteStructuredActivities_Clause,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
xmof_CompleteStructuredActivities_ExecutableNode_strategy = st.builds(
    xmof_CompleteStructuredActivities_ExecutableNode,
)
xmof_IntermediateActivities_ControlNode_strategy = st.builds(
    xmof_IntermediateActivities_ControlNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
xmof_IntermediateActivities_JoinNode_strategy = st.builds(
    xmof_IntermediateActivities_JoinNode,
)
xmof_IntermediateActivities_FinalNode_strategy = st.builds(
    xmof_IntermediateActivities_FinalNode,
)
xmof_IntermediateActivities_DecisionNode_strategy = st.builds(
    xmof_IntermediateActivities_DecisionNode,
)
xmof_IntermediateActivities_InitialNode_strategy = st.builds(
    xmof_IntermediateActivities_InitialNode,
)
xmof_IntermediateActivities_ForkNode_strategy = st.builds(
    xmof_IntermediateActivities_ForkNode,
)
xmof_IntermediateActivities_MergeNode_strategy = st.builds(
    xmof_IntermediateActivities_MergeNode,
)
BasicActions_InputPin_strategy = st.builds(
    BasicActions_InputPin,
)
CompleteStructuredActivities_ExecutableNode_strategy = st.builds(
    CompleteStructuredActivities_ExecutableNode,
)
BasicActions_OutputPin_strategy = st.builds(
    BasicActions_OutputPin,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
xmof_ExtraStructuredActivities_ExpansionRegion_strategy = st.builds(
    xmof_ExtraStructuredActivities_ExpansionRegion,
    mode=
        safe_text
)
xmof_CompleteStructuredActivities_ConditionalNode_strategy = st.builds(
    xmof_CompleteStructuredActivities_ConditionalNode,
    determinate=
        st.booleans(),
    assured=
        st.booleans()
)
xmof_CompleteStructuredActivities_LoopNode_strategy = st.builds(
    xmof_CompleteStructuredActivities_LoopNode,
    testedFirst=
        st.booleans()
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
xmof_ExtraStructuredActivities_ExpansionNode_strategy = st.builds(
    xmof_ExtraStructuredActivities_ExpansionNode,
)
xmof_IntermediateActivities_ActivityParameterNode_strategy = st.builds(
    xmof_IntermediateActivities_ActivityParameterNode,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
xmof_IntermediateActivities_ActivityFinalNode_strategy = st.builds(
    xmof_IntermediateActivities_ActivityFinalNode,
)
IntermediateActivities_ObjectFlow_strategy = st.builds(
    IntermediateActivities_ObjectFlow,
)
CompleteStructuredActivities_StructuredActivityNode_strategy = st.builds(
    CompleteStructuredActivities_StructuredActivityNode,
)
IntermediateActivities_ActivityNode_strategy = st.builds(
    IntermediateActivities_ActivityNode,
)
IntermediateActivities_Activity_strategy = st.builds(
    IntermediateActivities_Activity,
)
xmof_IntermediateActivities_ActivityEdge_strategy = st.builds(
    xmof_IntermediateActivities_ActivityEdge,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
xmof_IntermediateActivities_ControlFlow_strategy = st.builds(
    xmof_IntermediateActivities_ControlFlow,
)
xmof_IntermediateActivities_ObjectFlow_strategy = st.builds(
    xmof_IntermediateActivities_ObjectFlow,
)
xmof_IntermediateActivities_ActivityNode_strategy = st.builds(
    xmof_IntermediateActivities_ActivityNode,
)
IntermediateActivities_ActivityEdge_strategy = st.builds(
    IntermediateActivities_ActivityEdge,
)
xmof_IntermediateActivities_Activity_strategy = st.builds(
    xmof_IntermediateActivities_Activity,
    readOnly=
        st.booleans()
)
Kernel_InstanceSpecification_strategy = st.builds(
    Kernel_InstanceSpecification,
)
Kernel_ValueSpecification_strategy = st.builds(
    Kernel_ValueSpecification,
)
EDataType_strategy = st.builds(
    EDataType,
)
xmof_Kernel_PrimitiveType_strategy = st.builds(
    xmof_Kernel_PrimitiveType,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
xmof_Kernel_LiteralUnlimitedNatural_strategy = st.builds(
    xmof_Kernel_LiteralUnlimitedNatural,
    value=
        st.integers()
)
xmof_Kernel_LiteralInteger_strategy = st.builds(
    xmof_Kernel_LiteralInteger,
    value=
        st.integers()
)
xmof_Kernel_LiteralString_strategy = st.builds(
    xmof_Kernel_LiteralString,
    value=
        safe_text
)
xmof_Kernel_LiteralNull_strategy = st.builds(
    xmof_Kernel_LiteralNull,
)
xmof_Kernel_LiteralBoolean_strategy = st.builds(
    xmof_Kernel_LiteralBoolean,
    value=
        st.booleans()
)
Kernel_Slot_strategy = st.builds(
    Kernel_Slot,
)
Kernel_xmof_EClassifier_strategy = st.builds(
    Kernel_xmof_EClassifier,
)
xmof_Kernel_InstanceSpecification_strategy = st.builds(
    xmof_Kernel_InstanceSpecification,
)
Kernel_xmof_EStructuralFeature_strategy = st.builds(
    Kernel_xmof_EStructuralFeature,
)
EModelElement_strategy = st.builds(
    EModelElement,
)
xmof_IntermediateActions_LinkEndData_strategy = st.builds(
    xmof_IntermediateActions_LinkEndData,
)
xmof_CompleteStructuredActivities_Clause_strategy = st.builds(
    xmof_CompleteStructuredActivities_Clause,
)
xmof_Kernel_Slot_strategy = st.builds(
    xmof_Kernel_Slot,
)
EOperation_strategy = st.builds(
    EOperation,
)
xmof_Kernel_BehavioredEOperation_strategy = st.builds(
    xmof_Kernel_BehavioredEOperation,
)
BehavioredEOperation_strategy = st.builds(
    BehavioredEOperation,
)
xmof_Communications_Reception_strategy = st.builds(
    xmof_Communications_Reception,
)
Event_strategy = st.builds(
    Event,
)
xmof_Communications_MessageEvent_strategy = st.builds(
    xmof_Communications_MessageEvent,
)
Communications_Signal_strategy = st.builds(
    Communications_Signal,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
xmof_Communications_SignalEvent_strategy = st.builds(
    xmof_Communications_SignalEvent,
)
ETypedElement_strategy = st.builds(
    ETypedElement,
)
xmof_IntermediateActivities_ObjectNode_strategy = st.builds(
    xmof_IntermediateActivities_ObjectNode,
)
xmof_BasicActions_Pin_strategy = st.builds(
    xmof_BasicActions_Pin,
)
xmof_Kernel_ValueSpecification_strategy = st.builds(
    xmof_Kernel_ValueSpecification,
)
Kernel_EEnumLiteralSpecification_strategy = st.builds(
    Kernel_EEnumLiteralSpecification,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
xmof_Kernel_InstanceValue_strategy = st.builds(
    xmof_Kernel_InstanceValue,
)
xmof_Kernel_LiteralSpecification_strategy = st.builds(
    xmof_Kernel_LiteralSpecification,
)
xmof_Kernel_EnumValue_strategy = st.builds(
    xmof_Kernel_EnumValue,
)
Kernel_xmof_EEnumLiteral_strategy = st.builds(
    Kernel_xmof_EEnumLiteral,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
xmof_Kernel_EEnumLiteralSpecification_strategy = st.builds(
    xmof_Kernel_EEnumLiteralSpecification,
)

@given(instance=EParameter_strategy)
@settings(max_examples=50)
def test_eparameter_instantiation(instance):
    assert isinstance(instance, EParameter)

@given(instance=xmof_Kernel_DirectedParameter_strategy)
@settings(max_examples=50)
def test_xmof_kernel_directedparameter_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_DirectedParameter)



@given(instance=xmof_Kernel_DirectedParameter_strategy)
def test_xmof_kernel_directedparameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=xmof_BasicBehaviors_FunctionBehavior_strategy)
@settings(max_examples=50)
def test_xmof_basicbehaviors_functionbehavior_instantiation(instance):
    assert isinstance(instance, xmof_BasicBehaviors_FunctionBehavior)

@given(instance=BasicBehaviors_Behavior_strategy)
@settings(max_examples=50)
def test_basicbehaviors_behavior_instantiation(instance):
    assert isinstance(instance, BasicBehaviors_Behavior)

@given(instance=EClassifier_strategy)
@settings(max_examples=50)
def test_eclassifier_instantiation(instance):
    assert isinstance(instance, EClassifier)

@given(instance=xmof_BasicBehaviors_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_xmof_basicbehaviors_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, xmof_BasicBehaviors_BehavioredClassifier)

@given(instance=Communications_xmof_EAttribute_strategy)
@settings(max_examples=50)
def test_communications_xmof_eattribute_instantiation(instance):
    assert isinstance(instance, Communications_xmof_EAttribute)

@given(instance=xmof_Communications_Signal_strategy)
@settings(max_examples=50)
def test_xmof_communications_signal_instantiation(instance):
    assert isinstance(instance, xmof_Communications_Signal)

@given(instance=Communications_Event_strategy)
@settings(max_examples=50)
def test_communications_event_instantiation(instance):
    assert isinstance(instance, Communications_Event)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=xmof_Communications_Event_strategy)
@settings(max_examples=50)
def test_xmof_communications_event_instantiation(instance):
    assert isinstance(instance, xmof_Communications_Event)

@given(instance=xmof_Communications_Trigger_strategy)
@settings(max_examples=50)
def test_xmof_communications_trigger_instantiation(instance):
    assert isinstance(instance, xmof_Communications_Trigger)

@given(instance=BehavioredEClass_strategy)
@settings(max_examples=50)
def test_behavioredeclass_instantiation(instance):
    assert isinstance(instance, BehavioredEClass)

@given(instance=xmof_BasicBehaviors_Behavior_strategy)
@settings(max_examples=50)
def test_xmof_basicbehaviors_behavior_instantiation(instance):
    assert isinstance(instance, xmof_BasicBehaviors_Behavior)



@given(instance=xmof_BasicBehaviors_Behavior_strategy)
def test_xmof_basicbehaviors_behavior_reentrant_setter(instance):
    original = instance.reentrant
    instance.reentrant = original
    assert instance.reentrant == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=xmof_BasicBehaviors_OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_xmof_basicbehaviors_opaquebehavior_instantiation(instance):
    assert isinstance(instance, xmof_BasicBehaviors_OpaqueBehavior)



@given(instance=xmof_BasicBehaviors_OpaqueBehavior_strategy)
def test_xmof_basicbehaviors_opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=xmof_BasicBehaviors_OpaqueBehavior_strategy)
def test_xmof_basicbehaviors_opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=BasicBehaviors_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_basicbehaviors_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BasicBehaviors_BehavioredClassifier)

@given(instance=xmof_Kernel_BehavioredEClass_strategy)
@settings(max_examples=50)
def test_xmof_kernel_behavioredeclass_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_BehavioredEClass)

@given(instance=Kernel_DirectedParameter_strategy)
@settings(max_examples=50)
def test_kernel_directedparameter_instantiation(instance):
    assert isinstance(instance, Kernel_DirectedParameter)

@given(instance=Kernel_BehavioredEOperation_strategy)
@settings(max_examples=50)
def test_kernel_behavioredeoperation_instantiation(instance):
    assert isinstance(instance, Kernel_BehavioredEOperation)

@given(instance=BasicBehaviors_ParameterValue_strategy)
@settings(max_examples=50)
def test_basicbehaviors_parametervalue_instantiation(instance):
    assert isinstance(instance, BasicBehaviors_ParameterValue)

@given(instance=xmof_BasicBehaviors_ParameterValueDefinition_strategy)
@settings(max_examples=50)
def test_xmof_basicbehaviors_parametervaluedefinition_instantiation(instance):
    assert isinstance(instance, xmof_BasicBehaviors_ParameterValueDefinition)

@given(instance=Kernel_Value_strategy)
@settings(max_examples=50)
def test_kernel_value_instantiation(instance):
    assert isinstance(instance, Kernel_Value)

@given(instance=xmof_BasicBehaviors_ParameterValue_strategy)
@settings(max_examples=50)
def test_xmof_basicbehaviors_parametervalue_instantiation(instance):
    assert isinstance(instance, xmof_BasicBehaviors_ParameterValue)

@given(instance=PrimitiveValue_strategy)
@settings(max_examples=50)
def test_primitivevalue_instantiation(instance):
    assert isinstance(instance, PrimitiveValue)

@given(instance=xmof_Kernel_IntegerValue_strategy)
@settings(max_examples=50)
def test_xmof_kernel_integervalue_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_IntegerValue)



@given(instance=xmof_Kernel_IntegerValue_strategy)
def test_xmof_kernel_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xmof_Kernel_StringValue_strategy)
@settings(max_examples=50)
def test_xmof_kernel_stringvalue_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_StringValue)



@given(instance=xmof_Kernel_StringValue_strategy)
def test_xmof_kernel_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Kernel_PrimitiveType_strategy)
@settings(max_examples=50)
def test_kernel_primitivetype_instantiation(instance):
    assert isinstance(instance, Kernel_PrimitiveType)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=xmof_Kernel_EnumerationValue_strategy)
@settings(max_examples=50)
def test_xmof_kernel_enumerationvalue_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_EnumerationValue)

@given(instance=xmof_Kernel_PrimitiveValue_strategy)
@settings(max_examples=50)
def test_xmof_kernel_primitivevalue_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_PrimitiveValue)

@given(instance=xmof_LociL1_SemanticVisitor_strategy)
@settings(max_examples=50)
def test_xmof_locil1_semanticvisitor_instantiation(instance):
    assert isinstance(instance, xmof_LociL1_SemanticVisitor)

@given(instance=Kernel_xmof_EObject_strategy)
@settings(max_examples=50)
def test_kernel_xmof_eobject_instantiation(instance):
    assert isinstance(instance, Kernel_xmof_EObject)

@given(instance=xmof_Kernel_ObjectValue_strategy)
@settings(max_examples=50)
def test_xmof_kernel_objectvalue_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_ObjectValue)

@given(instance=SemanticVisitor_strategy)
@settings(max_examples=50)
def test_semanticvisitor_instantiation(instance):
    assert isinstance(instance, SemanticVisitor)

@given(instance=xmof_Kernel_Value_strategy)
@settings(max_examples=50)
def test_xmof_kernel_value_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_Value)

@given(instance=xmof_Kernel_BooleanValue_strategy)
@settings(max_examples=50)
def test_xmof_kernel_booleanvalue_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_BooleanValue)



@given(instance=xmof_Kernel_BooleanValue_strategy)
def test_xmof_kernel_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Kernel_xmof_EEnum_strategy)
@settings(max_examples=50)
def test_kernel_xmof_eenum_instantiation(instance):
    assert isinstance(instance, Kernel_xmof_EEnum)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=xmof_BasicActions_CallAction_strategy)
@settings(max_examples=50)
def test_xmof_basicactions_callaction_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_CallAction)



@given(instance=xmof_BasicActions_CallAction_strategy)
def test_xmof_basicactions_callaction_synchronous_setter(instance):
    original = instance.synchronous
    instance.synchronous = original
    assert instance.synchronous == original

@given(instance=IntermediateActivities_ObjectNode_strategy)
@settings(max_examples=50)
def test_intermediateactivities_objectnode_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_ObjectNode)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=xmof_BasicActions_OutputPin_strategy)
@settings(max_examples=50)
def test_xmof_basicactions_outputpin_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_OutputPin)

@given(instance=xmof_BasicActions_InputPin_strategy)
@settings(max_examples=50)
def test_xmof_basicactions_inputpin_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_InputPin)

@given(instance=xmof_BasicActions_SendSignalAction_strategy)
@settings(max_examples=50)
def test_xmof_basicactions_sendsignalaction_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_SendSignalAction)

@given(instance=BasicActions_xmof_EClassifier_strategy)
@settings(max_examples=50)
def test_basicactions_xmof_eclassifier_instantiation(instance):
    assert isinstance(instance, BasicActions_xmof_EClassifier)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=xmof_BasicActions_Action_strategy)
@settings(max_examples=50)
def test_xmof_basicactions_action_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_Action)



@given(instance=xmof_BasicActions_Action_strategy)
def test_xmof_basicactions_action_locallyReentrant_setter(instance):
    original = instance.locallyReentrant
    instance.locallyReentrant = original
    assert instance.locallyReentrant == original

@given(instance=Communications_Trigger_strategy)
@settings(max_examples=50)
def test_communications_trigger_instantiation(instance):
    assert isinstance(instance, Communications_Trigger)

@given(instance=CompleteActions_xmof_EClassifier_strategy)
@settings(max_examples=50)
def test_completeactions_xmof_eclassifier_instantiation(instance):
    assert isinstance(instance, CompleteActions_xmof_EClassifier)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=xmof_IntermediateActions_CreateLinkAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_createlinkaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_CreateLinkAction)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=xmof_BasicActions_CallOperationAction_strategy)
@settings(max_examples=50)
def test_xmof_basicactions_calloperationaction_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_CallOperationAction)

@given(instance=xmof_BasicActions_CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_xmof_basicactions_callbehavioraction_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_CallBehaviorAction)

@given(instance=xmof_CompleteActions_StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_xmof_completeactions_startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_StartObjectBehaviorAction)

@given(instance=xmof_IntermediateActions_DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_destroylinkaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_DestroyLinkAction)

@given(instance=IntermediateActions_xmof_EClassifier_strategy)
@settings(max_examples=50)
def test_intermediateactions_xmof_eclassifier_instantiation(instance):
    assert isinstance(instance, IntermediateActions_xmof_EClassifier)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=xmof_IntermediateActions_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_AddStructuralFeatureValueAction)



@given(instance=xmof_IntermediateActions_AddStructuralFeatureValueAction_strategy)
def test_xmof_intermediateactions_addstructuralfeaturevalueaction_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=xmof_IntermediateActions_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_RemoveStructuralFeatureValueAction)



@given(instance=xmof_IntermediateActions_RemoveStructuralFeatureValueAction_strategy)
def test_xmof_intermediateactions_removestructuralfeaturevalueaction_removeDuplicates_setter(instance):
    original = instance.removeDuplicates
    instance.removeDuplicates = original
    assert instance.removeDuplicates == original

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=xmof_IntermediateActions_ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_ClearStructuralFeatureAction)

@given(instance=xmof_IntermediateActions_WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_WriteStructuralFeatureAction)

@given(instance=IntermediateActions_xmof_EReference_strategy)
@settings(max_examples=50)
def test_intermediateactions_xmof_ereference_instantiation(instance):
    assert isinstance(instance, IntermediateActions_xmof_EReference)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=xmof_IntermediateActions_LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_LinkEndDestructionData)



@given(instance=xmof_IntermediateActions_LinkEndDestructionData_strategy)
def test_xmof_intermediateactions_linkenddestructiondata_destroyDuplicates_setter(instance):
    original = instance.destroyDuplicates
    instance.destroyDuplicates = original
    assert instance.destroyDuplicates == original

@given(instance=xmof_IntermediateActions_LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_linkendcreationdata_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_LinkEndCreationData)



@given(instance=xmof_IntermediateActions_LinkEndCreationData_strategy)
def test_xmof_intermediateactions_linkendcreationdata_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=xmof_IntermediateActions_ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_ReadStructuralFeatureAction)

@given(instance=IntermediateActions_xmof_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_intermediateactions_xmof_estructuralfeature_instantiation(instance):
    assert isinstance(instance, IntermediateActions_xmof_EStructuralFeature)

@given(instance=IntermediateActions_LinkEndData_strategy)
@settings(max_examples=50)
def test_intermediateactions_linkenddata_instantiation(instance):
    assert isinstance(instance, IntermediateActions_LinkEndData)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=xmof_IntermediateActions_ReadLinkAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_readlinkaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_ReadLinkAction)

@given(instance=xmof_IntermediateActions_WriteLinkAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_writelinkaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_WriteLinkAction)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=xmof_CompleteActions_ReduceAction_strategy)
@settings(max_examples=50)
def test_xmof_completeactions_reduceaction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_ReduceAction)



@given(instance=xmof_CompleteActions_ReduceAction_strategy)
def test_xmof_completeactions_reduceaction_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=xmof_IntermediateActions_ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_clearassociationaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_ClearAssociationAction)

@given(instance=xmof_BasicActions_InvocationAction_strategy)
@settings(max_examples=50)
def test_xmof_basicactions_invocationaction_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_InvocationAction)

@given(instance=xmof_CompleteActions_ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_xmof_completeactions_readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_ReadIsClassifiedObjectAction)



@given(instance=xmof_CompleteActions_ReadIsClassifiedObjectAction_strategy)
def test_xmof_completeactions_readisclassifiedobjectaction_direct_setter(instance):
    original = instance.direct
    instance.direct = original
    assert instance.direct == original

@given(instance=xmof_IntermediateActions_StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_StructuralFeatureAction)

@given(instance=xmof_IntermediateActions_CreateObjectAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_createobjectaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_CreateObjectAction)

@given(instance=xmof_IntermediateActions_DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_destroyobjectaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_DestroyObjectAction)



@given(instance=xmof_IntermediateActions_DestroyObjectAction_strategy)
def test_xmof_intermediateactions_destroyobjectaction_destroyLinks_setter(instance):
    original = instance.destroyLinks
    instance.destroyLinks = original
    assert instance.destroyLinks == original



@given(instance=xmof_IntermediateActions_DestroyObjectAction_strategy)
def test_xmof_intermediateactions_destroyobjectaction_destroyOwnedObjects_setter(instance):
    original = instance.destroyOwnedObjects
    instance.destroyOwnedObjects = original
    assert instance.destroyOwnedObjects == original

@given(instance=xmof_IntermediateActions_ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_valuespecificationaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_ValueSpecificationAction)

@given(instance=xmof_CompleteActions_ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_xmof_completeactions_reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_ReclassifyObjectAction)



@given(instance=xmof_CompleteActions_ReclassifyObjectAction_strategy)
def test_xmof_completeactions_reclassifyobjectaction_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=xmof_IntermediateActions_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_testidentityaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_TestIdentityAction)

@given(instance=xmof_IntermediateActions_LinkAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_linkaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_LinkAction)

@given(instance=xmof_CompleteActions_StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_xmof_completeactions_startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_StartClassifierBehaviorAction)

@given(instance=xmof_CompleteActions_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_xmof_completeactions_accepteventaction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_AcceptEventAction)



@given(instance=xmof_CompleteActions_AcceptEventAction_strategy)
def test_xmof_completeactions_accepteventaction_unmarshall_setter(instance):
    original = instance.unmarshall
    instance.unmarshall = original
    assert instance.unmarshall == original

@given(instance=xmof_CompleteActions_ReadExtentAction_strategy)
@settings(max_examples=50)
def test_xmof_completeactions_readextentaction_instantiation(instance):
    assert isinstance(instance, xmof_CompleteActions_ReadExtentAction)

@given(instance=xmof_IntermediateActions_ReadSelfAction_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_readselfaction_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_ReadSelfAction)

@given(instance=xmof_CompleteStructuredActivities_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_xmof_completestructuredactivities_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, xmof_CompleteStructuredActivities_StructuredActivityNode)



@given(instance=xmof_CompleteStructuredActivities_StructuredActivityNode_strategy)
def test_xmof_completestructuredactivities_structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=ExtraStructuredActivities_ExpansionNode_strategy)
@settings(max_examples=50)
def test_extrastructuredactivities_expansionnode_instantiation(instance):
    assert isinstance(instance, ExtraStructuredActivities_ExpansionNode)

@given(instance=ExtraStructuredActivities_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_extrastructuredactivities_expansionregion_instantiation(instance):
    assert isinstance(instance, ExtraStructuredActivities_ExpansionRegion)

@given(instance=CompleteStructuredActivities_Clause_strategy)
@settings(max_examples=50)
def test_completestructuredactivities_clause_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities_Clause)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=xmof_CompleteStructuredActivities_ExecutableNode_strategy)
@settings(max_examples=50)
def test_xmof_completestructuredactivities_executablenode_instantiation(instance):
    assert isinstance(instance, xmof_CompleteStructuredActivities_ExecutableNode)

@given(instance=xmof_IntermediateActivities_ControlNode_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_controlnode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ControlNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=xmof_IntermediateActivities_JoinNode_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_joinnode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_JoinNode)

@given(instance=xmof_IntermediateActivities_FinalNode_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_finalnode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_FinalNode)

@given(instance=xmof_IntermediateActivities_DecisionNode_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_decisionnode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_DecisionNode)

@given(instance=xmof_IntermediateActivities_InitialNode_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_initialnode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_InitialNode)

@given(instance=xmof_IntermediateActivities_ForkNode_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_forknode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ForkNode)

@given(instance=xmof_IntermediateActivities_MergeNode_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_mergenode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_MergeNode)

@given(instance=BasicActions_InputPin_strategy)
@settings(max_examples=50)
def test_basicactions_inputpin_instantiation(instance):
    assert isinstance(instance, BasicActions_InputPin)

@given(instance=CompleteStructuredActivities_ExecutableNode_strategy)
@settings(max_examples=50)
def test_completestructuredactivities_executablenode_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities_ExecutableNode)

@given(instance=BasicActions_OutputPin_strategy)
@settings(max_examples=50)
def test_basicactions_outputpin_instantiation(instance):
    assert isinstance(instance, BasicActions_OutputPin)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=xmof_ExtraStructuredActivities_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_xmof_extrastructuredactivities_expansionregion_instantiation(instance):
    assert isinstance(instance, xmof_ExtraStructuredActivities_ExpansionRegion)



@given(instance=xmof_ExtraStructuredActivities_ExpansionRegion_strategy)
def test_xmof_extrastructuredactivities_expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=xmof_CompleteStructuredActivities_ConditionalNode_strategy)
@settings(max_examples=50)
def test_xmof_completestructuredactivities_conditionalnode_instantiation(instance):
    assert isinstance(instance, xmof_CompleteStructuredActivities_ConditionalNode)



@given(instance=xmof_CompleteStructuredActivities_ConditionalNode_strategy)
def test_xmof_completestructuredactivities_conditionalnode_determinate_setter(instance):
    original = instance.determinate
    instance.determinate = original
    assert instance.determinate == original



@given(instance=xmof_CompleteStructuredActivities_ConditionalNode_strategy)
def test_xmof_completestructuredactivities_conditionalnode_assured_setter(instance):
    original = instance.assured
    instance.assured = original
    assert instance.assured == original

@given(instance=xmof_CompleteStructuredActivities_LoopNode_strategy)
@settings(max_examples=50)
def test_xmof_completestructuredactivities_loopnode_instantiation(instance):
    assert isinstance(instance, xmof_CompleteStructuredActivities_LoopNode)



@given(instance=xmof_CompleteStructuredActivities_LoopNode_strategy)
def test_xmof_completestructuredactivities_loopnode_testedFirst_setter(instance):
    original = instance.testedFirst
    instance.testedFirst = original
    assert instance.testedFirst == original

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=xmof_ExtraStructuredActivities_ExpansionNode_strategy)
@settings(max_examples=50)
def test_xmof_extrastructuredactivities_expansionnode_instantiation(instance):
    assert isinstance(instance, xmof_ExtraStructuredActivities_ExpansionNode)

@given(instance=xmof_IntermediateActivities_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_activityparameternode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ActivityParameterNode)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=xmof_IntermediateActivities_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_activityfinalnode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ActivityFinalNode)

@given(instance=IntermediateActivities_ObjectFlow_strategy)
@settings(max_examples=50)
def test_intermediateactivities_objectflow_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_ObjectFlow)

@given(instance=CompleteStructuredActivities_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_completestructuredactivities_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities_StructuredActivityNode)

@given(instance=IntermediateActivities_ActivityNode_strategy)
@settings(max_examples=50)
def test_intermediateactivities_activitynode_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_ActivityNode)

@given(instance=IntermediateActivities_Activity_strategy)
@settings(max_examples=50)
def test_intermediateactivities_activity_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_Activity)

@given(instance=xmof_IntermediateActivities_ActivityEdge_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_activityedge_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ActivityEdge)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=xmof_IntermediateActivities_ControlFlow_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_controlflow_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ControlFlow)

@given(instance=xmof_IntermediateActivities_ObjectFlow_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_objectflow_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ObjectFlow)

@given(instance=xmof_IntermediateActivities_ActivityNode_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_activitynode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ActivityNode)

@given(instance=IntermediateActivities_ActivityEdge_strategy)
@settings(max_examples=50)
def test_intermediateactivities_activityedge_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_ActivityEdge)

@given(instance=xmof_IntermediateActivities_Activity_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_activity_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_Activity)



@given(instance=xmof_IntermediateActivities_Activity_strategy)
def test_xmof_intermediateactivities_activity_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=Kernel_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_kernel_instancespecification_instantiation(instance):
    assert isinstance(instance, Kernel_InstanceSpecification)

@given(instance=Kernel_ValueSpecification_strategy)
@settings(max_examples=50)
def test_kernel_valuespecification_instantiation(instance):
    assert isinstance(instance, Kernel_ValueSpecification)

@given(instance=EDataType_strategy)
@settings(max_examples=50)
def test_edatatype_instantiation(instance):
    assert isinstance(instance, EDataType)

@given(instance=xmof_Kernel_PrimitiveType_strategy)
@settings(max_examples=50)
def test_xmof_kernel_primitivetype_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_PrimitiveType)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=xmof_Kernel_LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_xmof_kernel_literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_LiteralUnlimitedNatural)



@given(instance=xmof_Kernel_LiteralUnlimitedNatural_strategy)
def test_xmof_kernel_literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xmof_Kernel_LiteralInteger_strategy)
@settings(max_examples=50)
def test_xmof_kernel_literalinteger_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_LiteralInteger)



@given(instance=xmof_Kernel_LiteralInteger_strategy)
def test_xmof_kernel_literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xmof_Kernel_LiteralString_strategy)
@settings(max_examples=50)
def test_xmof_kernel_literalstring_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_LiteralString)



@given(instance=xmof_Kernel_LiteralString_strategy)
def test_xmof_kernel_literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xmof_Kernel_LiteralNull_strategy)
@settings(max_examples=50)
def test_xmof_kernel_literalnull_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_LiteralNull)

@given(instance=xmof_Kernel_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_xmof_kernel_literalboolean_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_LiteralBoolean)



@given(instance=xmof_Kernel_LiteralBoolean_strategy)
def test_xmof_kernel_literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Kernel_Slot_strategy)
@settings(max_examples=50)
def test_kernel_slot_instantiation(instance):
    assert isinstance(instance, Kernel_Slot)

@given(instance=Kernel_xmof_EClassifier_strategy)
@settings(max_examples=50)
def test_kernel_xmof_eclassifier_instantiation(instance):
    assert isinstance(instance, Kernel_xmof_EClassifier)

@given(instance=xmof_Kernel_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_xmof_kernel_instancespecification_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_InstanceSpecification)

@given(instance=Kernel_xmof_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_kernel_xmof_estructuralfeature_instantiation(instance):
    assert isinstance(instance, Kernel_xmof_EStructuralFeature)

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=xmof_IntermediateActions_LinkEndData_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactions_linkenddata_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActions_LinkEndData)

@given(instance=xmof_CompleteStructuredActivities_Clause_strategy)
@settings(max_examples=50)
def test_xmof_completestructuredactivities_clause_instantiation(instance):
    assert isinstance(instance, xmof_CompleteStructuredActivities_Clause)

@given(instance=xmof_Kernel_Slot_strategy)
@settings(max_examples=50)
def test_xmof_kernel_slot_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_Slot)

@given(instance=EOperation_strategy)
@settings(max_examples=50)
def test_eoperation_instantiation(instance):
    assert isinstance(instance, EOperation)

@given(instance=xmof_Kernel_BehavioredEOperation_strategy)
@settings(max_examples=50)
def test_xmof_kernel_behavioredeoperation_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_BehavioredEOperation)

@given(instance=BehavioredEOperation_strategy)
@settings(max_examples=50)
def test_behavioredeoperation_instantiation(instance):
    assert isinstance(instance, BehavioredEOperation)

@given(instance=xmof_Communications_Reception_strategy)
@settings(max_examples=50)
def test_xmof_communications_reception_instantiation(instance):
    assert isinstance(instance, xmof_Communications_Reception)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=xmof_Communications_MessageEvent_strategy)
@settings(max_examples=50)
def test_xmof_communications_messageevent_instantiation(instance):
    assert isinstance(instance, xmof_Communications_MessageEvent)

@given(instance=Communications_Signal_strategy)
@settings(max_examples=50)
def test_communications_signal_instantiation(instance):
    assert isinstance(instance, Communications_Signal)

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=xmof_Communications_SignalEvent_strategy)
@settings(max_examples=50)
def test_xmof_communications_signalevent_instantiation(instance):
    assert isinstance(instance, xmof_Communications_SignalEvent)

@given(instance=ETypedElement_strategy)
@settings(max_examples=50)
def test_etypedelement_instantiation(instance):
    assert isinstance(instance, ETypedElement)

@given(instance=xmof_IntermediateActivities_ObjectNode_strategy)
@settings(max_examples=50)
def test_xmof_intermediateactivities_objectnode_instantiation(instance):
    assert isinstance(instance, xmof_IntermediateActivities_ObjectNode)

@given(instance=xmof_BasicActions_Pin_strategy)
@settings(max_examples=50)
def test_xmof_basicactions_pin_instantiation(instance):
    assert isinstance(instance, xmof_BasicActions_Pin)

@given(instance=xmof_Kernel_ValueSpecification_strategy)
@settings(max_examples=50)
def test_xmof_kernel_valuespecification_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_ValueSpecification)

@given(instance=Kernel_EEnumLiteralSpecification_strategy)
@settings(max_examples=50)
def test_kernel_eenumliteralspecification_instantiation(instance):
    assert isinstance(instance, Kernel_EEnumLiteralSpecification)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=xmof_Kernel_InstanceValue_strategy)
@settings(max_examples=50)
def test_xmof_kernel_instancevalue_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_InstanceValue)

@given(instance=xmof_Kernel_LiteralSpecification_strategy)
@settings(max_examples=50)
def test_xmof_kernel_literalspecification_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_LiteralSpecification)

@given(instance=xmof_Kernel_EnumValue_strategy)
@settings(max_examples=50)
def test_xmof_kernel_enumvalue_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_EnumValue)

@given(instance=Kernel_xmof_EEnumLiteral_strategy)
@settings(max_examples=50)
def test_kernel_xmof_eenumliteral_instantiation(instance):
    assert isinstance(instance, Kernel_xmof_EEnumLiteral)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=xmof_Kernel_EEnumLiteralSpecification_strategy)
@settings(max_examples=50)
def test_xmof_kernel_eenumliteralspecification_instantiation(instance):
    assert isinstance(instance, xmof_Kernel_EEnumLiteralSpecification)
