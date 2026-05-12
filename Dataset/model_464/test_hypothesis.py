import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fUML_LociL1_SemanticVisitor,
    SemanticVisitor,
    fUML_Kernel_Value,
    Kernel_FeatureValue,
    CompoundValue,
    fUML_Kernel_DataValue,
    fUML_Kernel_ExtensionalValue,
    ExtensionalValue,
    fUML_Kernel_Link,
    fUML_Kernel_Object,
    Kernel_Object,
    StructuredValue,
    fUML_Kernel_CompoundValue,
    fUML_Kernel_Reference,
    Kernel_PrimitiveType,
    PrimitiveValue,
    fUML_Kernel_IntegerValue,
    fUML_Kernel_BooleanValue,
    fUML_Kernel_UnlimitedNaturalValue,
    Kernel_Value,
    fUML_Kernel_FeatureValue,
    Value,
    fUML_Kernel_PrimitiveValue,
    fUML_Kernel_EnumerationValue,
    fUML_Kernel_StructuredValue,
    fUML_Kernel_StringValue,
    InvocationAction,
    fUML_BasicActions_SendSignalAction,
    fUML_BasicActions_CallAction,
    IntermediateActivities_ObjectNode,
    Pin,
    fUML_BasicActions_OutputPin,
    fUML_BasicActions_InputPin,
    ExecutableNode,
    fUML_BasicActions_Action,
    Communications_Trigger,
    CallAction,
    fUML_BasicActions_CallBehaviorAction,
    fUML_BasicActions_CallOperationAction,
    fUML_CompleteActions_StartObjectBehaviorAction,
    WriteLinkAction,
    fUML_IntermediateActions_DestroyLinkAction,
    fUML_IntermediateActions_CreateLinkAction,
    LinkEndData,
    fUML_IntermediateActions_LinkEndDestructionData,
    fUML_IntermediateActions_LinkEndCreationData,
    WriteStructuralFeatureAction,
    fUML_IntermediateActions_AddStructuralFeatureValueAction,
    fUML_IntermediateActions_RemoveStructuralFeatureValueAction,
    StructuralFeatureAction,
    fUML_IntermediateActions_ClearStructuralFeatureAction,
    fUML_IntermediateActions_ReadStructuralFeatureAction,
    fUML_IntermediateActions_WriteStructuralFeatureAction,
    IntermediateActions_LinkEndData,
    ExtraStructuredActivities_ExpansionNode,
    LinkAction,
    fUML_IntermediateActions_ReadLinkAction,
    fUML_IntermediateActions_WriteLinkAction,
    ExtraStructuredActivities_ExpansionRegion,
    Action,
    fUML_IntermediateActions_CreateObjectAction,
    fUML_BasicActions_InvocationAction,
    fUML_CompleteActions_ReadExtentAction,
    fUML_IntermediateActions_ValueSpecificationAction,
    fUML_IntermediateActions_LinkAction,
    fUML_IntermediateActions_DestroyObjectAction,
    fUML_IntermediateActions_ClearAssociationAction,
    fUML_IntermediateActions_StructuralFeatureAction,
    fUML_IntermediateActions_TestIdentityAction,
    fUML_CompleteActions_StartClassifierBehaviorAction,
    fUML_CompleteActions_ReclassifyObjectAction,
    fUML_IntermediateActions_ReadSelfAction,
    fUML_CompleteActions_ReduceAction,
    fUML_CompleteActions_ReadIsClassifiedObjectAction,
    fUML_CompleteActions_AcceptEventAction,
    fUML_CompleteStructuredActivities_StructuredActivityNode,
    BasicActions_InputPin,
    CompleteStructuredActivities_ExecutableNode,
    BasicActions_OutputPin,
    StructuredActivityNode,
    fUML_CompleteStructuredActivities_ConditionalNode,
    fUML_ExtraStructuredActivities_ExpansionRegion,
    fUML_CompleteStructuredActivities_LoopNode,
    ObjectNode,
    fUML_ExtraStructuredActivities_ExpansionNode,
    fUML_IntermediateActivities_ActivityParameterNode,
    CompleteStructuredActivities_Clause,
    ActivityNode,
    fUML_CompleteStructuredActivities_ExecutableNode,
    fUML_IntermediateActivities_ControlNode,
    ControlNode,
    fUML_IntermediateActivities_ForkNode,
    fUML_IntermediateActivities_InitialNode,
    fUML_IntermediateActivities_DecisionNode,
    fUML_IntermediateActivities_FinalNode,
    fUML_IntermediateActivities_JoinNode,
    fUML_IntermediateActivities_MergeNode,
    IntermediateActivities_ActivityEdge,
    FinalNode,
    fUML_IntermediateActivities_ActivityFinalNode,
    IntermediateActivities_ObjectFlow,
    CompleteStructuredActivities_StructuredActivityNode,
    IntermediateActivities_ActivityNode,
    IntermediateActivities_Activity,
    ActivityEdge,
    fUML_IntermediateActivities_ControlFlow,
    fUML_IntermediateActivities_ObjectFlow,
    Communications_Reception,
    BehavioredClassifier,
    fUML_Kernel_Class,
    Kernel_Enumeration,
    InstanceSpecification,
    fUML_Kernel_EnumerationLiteral,
    Kernel_EnumerationLiteral,
    LiteralSpecification,
    fUML_Kernel_LiteralInteger,
    fUML_Kernel_LiteralString,
    fUML_Kernel_LiteralUnlimitedNatural,
    fUML_Kernel_LiteralNull,
    fUML_Kernel_LiteralBoolean,
    ValueSpecification,
    fUML_Kernel_LiteralSpecification,
    fUML_Kernel_InstanceValue,
    Kernel_InstanceSpecification,
    Kernel_StructuralFeature,
    Kernel_Slot,
    Kernel_Operation,
    DataType,
    fUML_Kernel_Enumeration,
    fUML_Kernel_PrimitiveType,
    Feature,
    fUML_Kernel_BehavioralFeature,
    Kernel_ValueSpecification,
    Kernel_Class,
    Kernel_DataType,
    Kernel_Association,
    StructuralFeature,
    fUML_Kernel_Property,
    Kernel_Generalization,
    Kernel_RedefinableElement,
    Kernel_Classifier,
    RedefinableElement,
    fUML_IntermediateActivities_ActivityEdge,
    fUML_IntermediateActivities_ActivityNode,
    fUML_Kernel_Feature,
    Kernel_TypedElement,
    fUML_IntermediateActivities_ObjectNode,
    Kernel_MultiplicityElement,
    fUML_Kernel_Parameter,
    fUML_BasicActions_Pin,
    Kernel_Feature,
    fUML_Kernel_StructuralFeature,
    fUML_Kernel_Element,
    Kernel_Package,
    Kernel_PackageableElement,
    Kernel_PackageImport,
    Kernel_ElementImport,
    Kernel_NamedElement,
    fUML_Kernel_Comment,
    Kernel_Comment,
    Kernel_Element,
    Kernel_Namespace,
    fUML_Kernel_Package,
    Element,
    fUML_Kernel_ElementImport,
    fUML_Kernel_PackageImport,
    fUML_Kernel_Generalization,
    fUML_CompleteStructuredActivities_Clause,
    fUML_IntermediateActions_LinkEndData,
    fUML_Kernel_MultiplicityElement,
    fUML_Kernel_Slot,
    fUML_Kernel_NamedElement,
    Kernel_Type,
    fUML_Kernel_Classifier,
    TypedElement,
    fUML_Kernel_ValueSpecification,
    BehavioralFeature,
    fUML_Kernel_Operation,
    fUML_Communications_Reception,
    Event,
    fUML_Communications_MessageEvent,
    Communications_Signal,
    MessageEvent,
    fUML_Communications_SignalEvent,
    Kernel_Property,
    PackageableElement,
    fUML_Kernel_Type,
    fUML_Communications_Event,
    Communications_Event,
    NamedElement,
    fUML_Kernel_PackageableElement,
    fUML_Kernel_InstanceSpecification,
    fUML_Kernel_TypedElement,
    fUML_Kernel_Namespace,
    fUML_Kernel_RedefinableElement,
    fUML_Communications_Trigger,
    OpaqueBehavior,
    fUML_BasicBehaviors_FunctionBehavior,
    BasicBehaviors_Behavior,
    Classifier,
    fUML_Communications_Signal,
    fUML_Kernel_Association,
    fUML_Kernel_DataType,
    fUML_BasicBehaviors_BehavioredClassifier,
    BasicBehaviors_BehavioredClassifier,
    Kernel_Parameter,
    Kernel_BehavioralFeature,
    Class,
    fUML_BasicBehaviors_Behavior,
    Behavior,
    fUML_IntermediateActivities_Activity,
    fUML_BasicBehaviors_OpaqueBehavior,
    ExpansionKind,
    ParameterDirectionKind,
    AggregationKind,
    CallConcurrencyKind,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fuml_locil1_semanticvisitor_is_not_abstract():
    assert not inspect.isabstract(fUML_LociL1_SemanticVisitor)


def test_fuml_locil1_semanticvisitor_constructor_exists():
    assert callable(fUML_LociL1_SemanticVisitor.__init__)


def test_fuml_locil1_semanticvisitor_constructor_args():
    sig = inspect.signature(fUML_LociL1_SemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_semanticvisitor_is_not_abstract():
    assert not inspect.isabstract(SemanticVisitor)


def test_semanticvisitor_constructor_exists():
    assert callable(SemanticVisitor.__init__)


def test_semanticvisitor_constructor_args():
    sig = inspect.signature(SemanticVisitor.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_value_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Value)


def test_fuml_kernel_value_constructor_exists():
    assert callable(fUML_Kernel_Value.__init__)


def test_fuml_kernel_value_constructor_args():
    sig = inspect.signature(fUML_Kernel_Value.__init__)
    params = list(sig.parameters.keys())



def test_kernel_featurevalue_is_not_abstract():
    assert not inspect.isabstract(Kernel_FeatureValue)


def test_kernel_featurevalue_constructor_exists():
    assert callable(Kernel_FeatureValue.__init__)


def test_kernel_featurevalue_constructor_args():
    sig = inspect.signature(Kernel_FeatureValue.__init__)
    params = list(sig.parameters.keys())



def test_compoundvalue_is_not_abstract():
    assert not inspect.isabstract(CompoundValue)


def test_compoundvalue_constructor_exists():
    assert callable(CompoundValue.__init__)


def test_compoundvalue_constructor_args():
    sig = inspect.signature(CompoundValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_datavalue_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_DataValue)


def test_fuml_kernel_datavalue_constructor_exists():
    assert callable(fUML_Kernel_DataValue.__init__)


def test_fuml_kernel_datavalue_constructor_args():
    sig = inspect.signature(fUML_Kernel_DataValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_extensionalvalue_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_ExtensionalValue)


def test_fuml_kernel_extensionalvalue_constructor_exists():
    assert callable(fUML_Kernel_ExtensionalValue.__init__)


def test_fuml_kernel_extensionalvalue_constructor_args():
    sig = inspect.signature(fUML_Kernel_ExtensionalValue.__init__)
    params = list(sig.parameters.keys())



def test_extensionalvalue_is_not_abstract():
    assert not inspect.isabstract(ExtensionalValue)


def test_extensionalvalue_constructor_exists():
    assert callable(ExtensionalValue.__init__)


def test_extensionalvalue_constructor_args():
    sig = inspect.signature(ExtensionalValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_link_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Link)


def test_fuml_kernel_link_constructor_exists():
    assert callable(fUML_Kernel_Link.__init__)


def test_fuml_kernel_link_constructor_args():
    sig = inspect.signature(fUML_Kernel_Link.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_object_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Object)


def test_fuml_kernel_object_constructor_exists():
    assert callable(fUML_Kernel_Object.__init__)


def test_fuml_kernel_object_constructor_args():
    sig = inspect.signature(fUML_Kernel_Object.__init__)
    params = list(sig.parameters.keys())



def test_kernel_object_is_not_abstract():
    assert not inspect.isabstract(Kernel_Object)


def test_kernel_object_constructor_exists():
    assert callable(Kernel_Object.__init__)


def test_kernel_object_constructor_args():
    sig = inspect.signature(Kernel_Object.__init__)
    params = list(sig.parameters.keys())



def test_structuredvalue_is_not_abstract():
    assert not inspect.isabstract(StructuredValue)


def test_structuredvalue_constructor_exists():
    assert callable(StructuredValue.__init__)


def test_structuredvalue_constructor_args():
    sig = inspect.signature(StructuredValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_compoundvalue_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_CompoundValue)


def test_fuml_kernel_compoundvalue_constructor_exists():
    assert callable(fUML_Kernel_CompoundValue.__init__)


def test_fuml_kernel_compoundvalue_constructor_args():
    sig = inspect.signature(fUML_Kernel_CompoundValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_reference_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Reference)


def test_fuml_kernel_reference_constructor_exists():
    assert callable(fUML_Kernel_Reference.__init__)


def test_fuml_kernel_reference_constructor_args():
    sig = inspect.signature(fUML_Kernel_Reference.__init__)
    params = list(sig.parameters.keys())



def test_kernel_primitivetype_is_not_abstract():
    assert not inspect.isabstract(Kernel_PrimitiveType)


def test_kernel_primitivetype_constructor_exists():
    assert callable(Kernel_PrimitiveType.__init__)


def test_kernel_primitivetype_constructor_args():
    sig = inspect.signature(Kernel_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_primitivevalue_is_not_abstract():
    assert not inspect.isabstract(PrimitiveValue)


def test_primitivevalue_constructor_exists():
    assert callable(PrimitiveValue.__init__)


def test_primitivevalue_constructor_args():
    sig = inspect.signature(PrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_integervalue_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_IntegerValue)


def test_fuml_kernel_integervalue_constructor_exists():
    assert callable(fUML_Kernel_IntegerValue.__init__)


def test_fuml_kernel_integervalue_constructor_args():
    sig = inspect.signature(fUML_Kernel_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml_kernel_integervalue_has_value():
    assert hasattr(fUML_Kernel_IntegerValue, "value")
    descriptor = None
    for klass in fUML_Kernel_IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml_kernel_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_BooleanValue)


def test_fuml_kernel_booleanvalue_constructor_exists():
    assert callable(fUML_Kernel_BooleanValue.__init__)


def test_fuml_kernel_booleanvalue_constructor_args():
    sig = inspect.signature(fUML_Kernel_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml_kernel_booleanvalue_has_value():
    assert hasattr(fUML_Kernel_BooleanValue, "value")
    descriptor = None
    for klass in fUML_Kernel_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml_kernel_unlimitednaturalvalue_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_UnlimitedNaturalValue)


def test_fuml_kernel_unlimitednaturalvalue_constructor_exists():
    assert callable(fUML_Kernel_UnlimitedNaturalValue.__init__)


def test_fuml_kernel_unlimitednaturalvalue_constructor_args():
    sig = inspect.signature(fUML_Kernel_UnlimitedNaturalValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml_kernel_unlimitednaturalvalue_has_value():
    assert hasattr(fUML_Kernel_UnlimitedNaturalValue, "value")
    descriptor = None
    for klass in fUML_Kernel_UnlimitedNaturalValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kernel_value_is_not_abstract():
    assert not inspect.isabstract(Kernel_Value)


def test_kernel_value_constructor_exists():
    assert callable(Kernel_Value.__init__)


def test_kernel_value_constructor_args():
    sig = inspect.signature(Kernel_Value.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_featurevalue_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_FeatureValue)


def test_fuml_kernel_featurevalue_constructor_exists():
    assert callable(fUML_Kernel_FeatureValue.__init__)


def test_fuml_kernel_featurevalue_constructor_args():
    sig = inspect.signature(fUML_Kernel_FeatureValue.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_fuml_kernel_featurevalue_has_position():
    assert hasattr(fUML_Kernel_FeatureValue, "position")
    descriptor = None
    for klass in fUML_Kernel_FeatureValue.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_primitivevalue_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_PrimitiveValue)


def test_fuml_kernel_primitivevalue_constructor_exists():
    assert callable(fUML_Kernel_PrimitiveValue.__init__)


def test_fuml_kernel_primitivevalue_constructor_args():
    sig = inspect.signature(fUML_Kernel_PrimitiveValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_enumerationvalue_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_EnumerationValue)


def test_fuml_kernel_enumerationvalue_constructor_exists():
    assert callable(fUML_Kernel_EnumerationValue.__init__)


def test_fuml_kernel_enumerationvalue_constructor_args():
    sig = inspect.signature(fUML_Kernel_EnumerationValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_structuredvalue_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_StructuredValue)


def test_fuml_kernel_structuredvalue_constructor_exists():
    assert callable(fUML_Kernel_StructuredValue.__init__)


def test_fuml_kernel_structuredvalue_constructor_args():
    sig = inspect.signature(fUML_Kernel_StructuredValue.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_stringvalue_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_StringValue)


def test_fuml_kernel_stringvalue_constructor_exists():
    assert callable(fUML_Kernel_StringValue.__init__)


def test_fuml_kernel_stringvalue_constructor_args():
    sig = inspect.signature(fUML_Kernel_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml_kernel_stringvalue_has_value():
    assert hasattr(fUML_Kernel_StringValue, "value")
    descriptor = None
    for klass in fUML_Kernel_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_basicactions_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicActions_SendSignalAction)


def test_fuml_basicactions_sendsignalaction_constructor_exists():
    assert callable(fUML_BasicActions_SendSignalAction.__init__)


def test_fuml_basicactions_sendsignalaction_constructor_args():
    sig = inspect.signature(fUML_BasicActions_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_basicactions_callaction_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicActions_CallAction)


def test_fuml_basicactions_callaction_constructor_exists():
    assert callable(fUML_BasicActions_CallAction.__init__)


def test_fuml_basicactions_callaction_constructor_args():
    sig = inspect.signature(fUML_BasicActions_CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "synchronous" in params, "Missing parameter 'synchronous'"

def test_fuml_basicactions_callaction_has_synchronous():
    assert hasattr(fUML_BasicActions_CallAction, "synchronous")
    descriptor = None
    for klass in fUML_BasicActions_CallAction.__mro__:
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



def test_fuml_basicactions_outputpin_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicActions_OutputPin)


def test_fuml_basicactions_outputpin_constructor_exists():
    assert callable(fUML_BasicActions_OutputPin.__init__)


def test_fuml_basicactions_outputpin_constructor_args():
    sig = inspect.signature(fUML_BasicActions_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_fuml_basicactions_inputpin_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicActions_InputPin)


def test_fuml_basicactions_inputpin_constructor_exists():
    assert callable(fUML_BasicActions_InputPin.__init__)


def test_fuml_basicactions_inputpin_constructor_args():
    sig = inspect.signature(fUML_BasicActions_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml_basicactions_action_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicActions_Action)


def test_fuml_basicactions_action_constructor_exists():
    assert callable(fUML_BasicActions_Action.__init__)


def test_fuml_basicactions_action_constructor_args():
    sig = inspect.signature(fUML_BasicActions_Action.__init__)
    params = list(sig.parameters.keys())
    assert "locallyReentrant" in params, "Missing parameter 'locallyReentrant'"

def test_fuml_basicactions_action_has_locallyReentrant():
    assert hasattr(fUML_BasicActions_Action, "locallyReentrant")
    descriptor = None
    for klass in fUML_BasicActions_Action.__mro__:
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



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_basicactions_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicActions_CallBehaviorAction)


def test_fuml_basicactions_callbehavioraction_constructor_exists():
    assert callable(fUML_BasicActions_CallBehaviorAction.__init__)


def test_fuml_basicactions_callbehavioraction_constructor_args():
    sig = inspect.signature(fUML_BasicActions_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_basicactions_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicActions_CallOperationAction)


def test_fuml_basicactions_calloperationaction_constructor_exists():
    assert callable(fUML_BasicActions_CallOperationAction.__init__)


def test_fuml_basicactions_calloperationaction_constructor_args():
    sig = inspect.signature(fUML_BasicActions_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_completeactions_startobjectbehavioraction_is_not_abstract():
    assert not inspect.isabstract(fUML_CompleteActions_StartObjectBehaviorAction)


def test_fuml_completeactions_startobjectbehavioraction_constructor_exists():
    assert callable(fUML_CompleteActions_StartObjectBehaviorAction.__init__)


def test_fuml_completeactions_startobjectbehavioraction_constructor_args():
    sig = inspect.signature(fUML_CompleteActions_StartObjectBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_DestroyLinkAction)


def test_fuml_intermediateactions_destroylinkaction_constructor_exists():
    assert callable(fUML_IntermediateActions_DestroyLinkAction.__init__)


def test_fuml_intermediateactions_destroylinkaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_CreateLinkAction)


def test_fuml_intermediateactions_createlinkaction_constructor_exists():
    assert callable(fUML_IntermediateActions_CreateLinkAction.__init__)


def test_fuml_intermediateactions_createlinkaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_LinkEndDestructionData)


def test_fuml_intermediateactions_linkenddestructiondata_constructor_exists():
    assert callable(fUML_IntermediateActions_LinkEndDestructionData.__init__)


def test_fuml_intermediateactions_linkenddestructiondata_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "destroyDuplicates" in params, "Missing parameter 'destroyDuplicates'"

def test_fuml_intermediateactions_linkenddestructiondata_has_destroyDuplicates():
    assert hasattr(fUML_IntermediateActions_LinkEndDestructionData, "destroyDuplicates")
    descriptor = None
    for klass in fUML_IntermediateActions_LinkEndDestructionData.__mro__:
        if "destroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["destroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_fuml_intermediateactions_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_LinkEndCreationData)


def test_fuml_intermediateactions_linkendcreationdata_constructor_exists():
    assert callable(fUML_IntermediateActions_LinkEndCreationData.__init__)


def test_fuml_intermediateactions_linkendcreationdata_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_fuml_intermediateactions_linkendcreationdata_has_replaceAll():
    assert hasattr(fUML_IntermediateActions_LinkEndCreationData, "replaceAll")
    descriptor = None
    for klass in fUML_IntermediateActions_LinkEndCreationData.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_AddStructuralFeatureValueAction)


def test_fuml_intermediateactions_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(fUML_IntermediateActions_AddStructuralFeatureValueAction.__init__)


def test_fuml_intermediateactions_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_fuml_intermediateactions_addstructuralfeaturevalueaction_has_replaceAll():
    assert hasattr(fUML_IntermediateActions_AddStructuralFeatureValueAction, "replaceAll")
    descriptor = None
    for klass in fUML_IntermediateActions_AddStructuralFeatureValueAction.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_fuml_intermediateactions_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_RemoveStructuralFeatureValueAction)


def test_fuml_intermediateactions_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(fUML_IntermediateActions_RemoveStructuralFeatureValueAction.__init__)


def test_fuml_intermediateactions_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "removeDuplicates" in params, "Missing parameter 'removeDuplicates'"

def test_fuml_intermediateactions_removestructuralfeaturevalueaction_has_removeDuplicates():
    assert hasattr(fUML_IntermediateActions_RemoveStructuralFeatureValueAction, "removeDuplicates")
    descriptor = None
    for klass in fUML_IntermediateActions_RemoveStructuralFeatureValueAction.__mro__:
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



def test_fuml_intermediateactions_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_ClearStructuralFeatureAction)


def test_fuml_intermediateactions_clearstructuralfeatureaction_constructor_exists():
    assert callable(fUML_IntermediateActions_ClearStructuralFeatureAction.__init__)


def test_fuml_intermediateactions_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_ReadStructuralFeatureAction)


def test_fuml_intermediateactions_readstructuralfeatureaction_constructor_exists():
    assert callable(fUML_IntermediateActions_ReadStructuralFeatureAction.__init__)


def test_fuml_intermediateactions_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_WriteStructuralFeatureAction)


def test_fuml_intermediateactions_writestructuralfeatureaction_constructor_exists():
    assert callable(fUML_IntermediateActions_WriteStructuralFeatureAction.__init__)


def test_fuml_intermediateactions_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactions_linkenddata_is_not_abstract():
    assert not inspect.isabstract(IntermediateActions_LinkEndData)


def test_intermediateactions_linkenddata_constructor_exists():
    assert callable(IntermediateActions_LinkEndData.__init__)


def test_intermediateactions_linkenddata_constructor_args():
    sig = inspect.signature(IntermediateActions_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_extrastructuredactivities_expansionnode_is_not_abstract():
    assert not inspect.isabstract(ExtraStructuredActivities_ExpansionNode)


def test_extrastructuredactivities_expansionnode_constructor_exists():
    assert callable(ExtraStructuredActivities_ExpansionNode.__init__)


def test_extrastructuredactivities_expansionnode_constructor_args():
    sig = inspect.signature(ExtraStructuredActivities_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_ReadLinkAction)


def test_fuml_intermediateactions_readlinkaction_constructor_exists():
    assert callable(fUML_IntermediateActions_ReadLinkAction.__init__)


def test_fuml_intermediateactions_readlinkaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_WriteLinkAction)


def test_fuml_intermediateactions_writelinkaction_constructor_exists():
    assert callable(fUML_IntermediateActions_WriteLinkAction.__init__)


def test_fuml_intermediateactions_writelinkaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_extrastructuredactivities_expansionregion_is_not_abstract():
    assert not inspect.isabstract(ExtraStructuredActivities_ExpansionRegion)


def test_extrastructuredactivities_expansionregion_constructor_exists():
    assert callable(ExtraStructuredActivities_ExpansionRegion.__init__)


def test_extrastructuredactivities_expansionregion_constructor_args():
    sig = inspect.signature(ExtraStructuredActivities_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_CreateObjectAction)


def test_fuml_intermediateactions_createobjectaction_constructor_exists():
    assert callable(fUML_IntermediateActions_CreateObjectAction.__init__)


def test_fuml_intermediateactions_createobjectaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_basicactions_invocationaction_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicActions_InvocationAction)


def test_fuml_basicactions_invocationaction_constructor_exists():
    assert callable(fUML_BasicActions_InvocationAction.__init__)


def test_fuml_basicactions_invocationaction_constructor_args():
    sig = inspect.signature(fUML_BasicActions_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_completeactions_readextentaction_is_not_abstract():
    assert not inspect.isabstract(fUML_CompleteActions_ReadExtentAction)


def test_fuml_completeactions_readextentaction_constructor_exists():
    assert callable(fUML_CompleteActions_ReadExtentAction.__init__)


def test_fuml_completeactions_readextentaction_constructor_args():
    sig = inspect.signature(fUML_CompleteActions_ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_ValueSpecificationAction)


def test_fuml_intermediateactions_valuespecificationaction_constructor_exists():
    assert callable(fUML_IntermediateActions_ValueSpecificationAction.__init__)


def test_fuml_intermediateactions_valuespecificationaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_linkaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_LinkAction)


def test_fuml_intermediateactions_linkaction_constructor_exists():
    assert callable(fUML_IntermediateActions_LinkAction.__init__)


def test_fuml_intermediateactions_linkaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_DestroyObjectAction)


def test_fuml_intermediateactions_destroyobjectaction_constructor_exists():
    assert callable(fUML_IntermediateActions_DestroyObjectAction.__init__)


def test_fuml_intermediateactions_destroyobjectaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "destroyOwnedObjects" in params, "Missing parameter 'destroyOwnedObjects'"
    assert "destroyLinks" in params, "Missing parameter 'destroyLinks'"

def test_fuml_intermediateactions_destroyobjectaction_has_destroyOwnedObjects():
    assert hasattr(fUML_IntermediateActions_DestroyObjectAction, "destroyOwnedObjects")
    descriptor = None
    for klass in fUML_IntermediateActions_DestroyObjectAction.__mro__:
        if "destroyOwnedObjects" in klass.__dict__:
            descriptor = klass.__dict__["destroyOwnedObjects"]
            break
    assert isinstance(descriptor, property)

def test_fuml_intermediateactions_destroyobjectaction_has_destroyLinks():
    assert hasattr(fUML_IntermediateActions_DestroyObjectAction, "destroyLinks")
    descriptor = None
    for klass in fUML_IntermediateActions_DestroyObjectAction.__mro__:
        if "destroyLinks" in klass.__dict__:
            descriptor = klass.__dict__["destroyLinks"]
            break
    assert isinstance(descriptor, property)



def test_fuml_intermediateactions_clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_ClearAssociationAction)


def test_fuml_intermediateactions_clearassociationaction_constructor_exists():
    assert callable(fUML_IntermediateActions_ClearAssociationAction.__init__)


def test_fuml_intermediateactions_clearassociationaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_StructuralFeatureAction)


def test_fuml_intermediateactions_structuralfeatureaction_constructor_exists():
    assert callable(fUML_IntermediateActions_StructuralFeatureAction.__init__)


def test_fuml_intermediateactions_structuralfeatureaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_TestIdentityAction)


def test_fuml_intermediateactions_testidentityaction_constructor_exists():
    assert callable(fUML_IntermediateActions_TestIdentityAction.__init__)


def test_fuml_intermediateactions_testidentityaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_completeactions_startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(fUML_CompleteActions_StartClassifierBehaviorAction)


def test_fuml_completeactions_startclassifierbehavioraction_constructor_exists():
    assert callable(fUML_CompleteActions_StartClassifierBehaviorAction.__init__)


def test_fuml_completeactions_startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(fUML_CompleteActions_StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_completeactions_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(fUML_CompleteActions_ReclassifyObjectAction)


def test_fuml_completeactions_reclassifyobjectaction_constructor_exists():
    assert callable(fUML_CompleteActions_ReclassifyObjectAction.__init__)


def test_fuml_completeactions_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(fUML_CompleteActions_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "replaceAll" in params, "Missing parameter 'replaceAll'"

def test_fuml_completeactions_reclassifyobjectaction_has_replaceAll():
    assert hasattr(fUML_CompleteActions_ReclassifyObjectAction, "replaceAll")
    descriptor = None
    for klass in fUML_CompleteActions_ReclassifyObjectAction.__mro__:
        if "replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["replaceAll"]
            break
    assert isinstance(descriptor, property)



def test_fuml_intermediateactions_readselfaction_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_ReadSelfAction)


def test_fuml_intermediateactions_readselfaction_constructor_exists():
    assert callable(fUML_IntermediateActions_ReadSelfAction.__init__)


def test_fuml_intermediateactions_readselfaction_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_fuml_completeactions_reduceaction_is_not_abstract():
    assert not inspect.isabstract(fUML_CompleteActions_ReduceAction)


def test_fuml_completeactions_reduceaction_constructor_exists():
    assert callable(fUML_CompleteActions_ReduceAction.__init__)


def test_fuml_completeactions_reduceaction_constructor_args():
    sig = inspect.signature(fUML_CompleteActions_ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"

def test_fuml_completeactions_reduceaction_has_ordered():
    assert hasattr(fUML_CompleteActions_ReduceAction, "ordered")
    descriptor = None
    for klass in fUML_CompleteActions_ReduceAction.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)



def test_fuml_completeactions_readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(fUML_CompleteActions_ReadIsClassifiedObjectAction)


def test_fuml_completeactions_readisclassifiedobjectaction_constructor_exists():
    assert callable(fUML_CompleteActions_ReadIsClassifiedObjectAction.__init__)


def test_fuml_completeactions_readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(fUML_CompleteActions_ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "direct" in params, "Missing parameter 'direct'"

def test_fuml_completeactions_readisclassifiedobjectaction_has_direct():
    assert hasattr(fUML_CompleteActions_ReadIsClassifiedObjectAction, "direct")
    descriptor = None
    for klass in fUML_CompleteActions_ReadIsClassifiedObjectAction.__mro__:
        if "direct" in klass.__dict__:
            descriptor = klass.__dict__["direct"]
            break
    assert isinstance(descriptor, property)



def test_fuml_completeactions_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(fUML_CompleteActions_AcceptEventAction)


def test_fuml_completeactions_accepteventaction_constructor_exists():
    assert callable(fUML_CompleteActions_AcceptEventAction.__init__)


def test_fuml_completeactions_accepteventaction_constructor_args():
    sig = inspect.signature(fUML_CompleteActions_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "unmarshall" in params, "Missing parameter 'unmarshall'"

def test_fuml_completeactions_accepteventaction_has_unmarshall():
    assert hasattr(fUML_CompleteActions_AcceptEventAction, "unmarshall")
    descriptor = None
    for klass in fUML_CompleteActions_AcceptEventAction.__mro__:
        if "unmarshall" in klass.__dict__:
            descriptor = klass.__dict__["unmarshall"]
            break
    assert isinstance(descriptor, property)



def test_fuml_completestructuredactivities_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(fUML_CompleteStructuredActivities_StructuredActivityNode)


def test_fuml_completestructuredactivities_structuredactivitynode_constructor_exists():
    assert callable(fUML_CompleteStructuredActivities_StructuredActivityNode.__init__)


def test_fuml_completestructuredactivities_structuredactivitynode_constructor_args():
    sig = inspect.signature(fUML_CompleteStructuredActivities_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_fuml_completestructuredactivities_structuredactivitynode_has_mustIsolate():
    assert hasattr(fUML_CompleteStructuredActivities_StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in fUML_CompleteStructuredActivities_StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



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



def test_fuml_completestructuredactivities_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(fUML_CompleteStructuredActivities_ConditionalNode)


def test_fuml_completestructuredactivities_conditionalnode_constructor_exists():
    assert callable(fUML_CompleteStructuredActivities_ConditionalNode.__init__)


def test_fuml_completestructuredactivities_conditionalnode_constructor_args():
    sig = inspect.signature(fUML_CompleteStructuredActivities_ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "determinate" in params, "Missing parameter 'determinate'"
    assert "assured" in params, "Missing parameter 'assured'"

def test_fuml_completestructuredactivities_conditionalnode_has_determinate():
    assert hasattr(fUML_CompleteStructuredActivities_ConditionalNode, "determinate")
    descriptor = None
    for klass in fUML_CompleteStructuredActivities_ConditionalNode.__mro__:
        if "determinate" in klass.__dict__:
            descriptor = klass.__dict__["determinate"]
            break
    assert isinstance(descriptor, property)

def test_fuml_completestructuredactivities_conditionalnode_has_assured():
    assert hasattr(fUML_CompleteStructuredActivities_ConditionalNode, "assured")
    descriptor = None
    for klass in fUML_CompleteStructuredActivities_ConditionalNode.__mro__:
        if "assured" in klass.__dict__:
            descriptor = klass.__dict__["assured"]
            break
    assert isinstance(descriptor, property)



def test_fuml_extrastructuredactivities_expansionregion_is_not_abstract():
    assert not inspect.isabstract(fUML_ExtraStructuredActivities_ExpansionRegion)


def test_fuml_extrastructuredactivities_expansionregion_constructor_exists():
    assert callable(fUML_ExtraStructuredActivities_ExpansionRegion.__init__)


def test_fuml_extrastructuredactivities_expansionregion_constructor_args():
    sig = inspect.signature(fUML_ExtraStructuredActivities_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_fuml_extrastructuredactivities_expansionregion_has_mode():
    assert hasattr(fUML_ExtraStructuredActivities_ExpansionRegion, "mode")
    descriptor = None
    for klass in fUML_ExtraStructuredActivities_ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_fuml_completestructuredactivities_loopnode_is_not_abstract():
    assert not inspect.isabstract(fUML_CompleteStructuredActivities_LoopNode)


def test_fuml_completestructuredactivities_loopnode_constructor_exists():
    assert callable(fUML_CompleteStructuredActivities_LoopNode.__init__)


def test_fuml_completestructuredactivities_loopnode_constructor_args():
    sig = inspect.signature(fUML_CompleteStructuredActivities_LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "testedFirst" in params, "Missing parameter 'testedFirst'"

def test_fuml_completestructuredactivities_loopnode_has_testedFirst():
    assert hasattr(fUML_CompleteStructuredActivities_LoopNode, "testedFirst")
    descriptor = None
    for klass in fUML_CompleteStructuredActivities_LoopNode.__mro__:
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



def test_fuml_extrastructuredactivities_expansionnode_is_not_abstract():
    assert not inspect.isabstract(fUML_ExtraStructuredActivities_ExpansionNode)


def test_fuml_extrastructuredactivities_expansionnode_constructor_exists():
    assert callable(fUML_ExtraStructuredActivities_ExpansionNode.__init__)


def test_fuml_extrastructuredactivities_expansionnode_constructor_args():
    sig = inspect.signature(fUML_ExtraStructuredActivities_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_ActivityParameterNode)


def test_fuml_intermediateactivities_activityparameternode_constructor_exists():
    assert callable(fUML_IntermediateActivities_ActivityParameterNode.__init__)


def test_fuml_intermediateactivities_activityparameternode_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_ActivityParameterNode.__init__)
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



def test_fuml_completestructuredactivities_executablenode_is_not_abstract():
    assert not inspect.isabstract(fUML_CompleteStructuredActivities_ExecutableNode)


def test_fuml_completestructuredactivities_executablenode_constructor_exists():
    assert callable(fUML_CompleteStructuredActivities_ExecutableNode.__init__)


def test_fuml_completestructuredactivities_executablenode_constructor_args():
    sig = inspect.signature(fUML_CompleteStructuredActivities_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_controlnode_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_ControlNode)


def test_fuml_intermediateactivities_controlnode_constructor_exists():
    assert callable(fUML_IntermediateActivities_ControlNode.__init__)


def test_fuml_intermediateactivities_controlnode_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_forknode_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_ForkNode)


def test_fuml_intermediateactivities_forknode_constructor_exists():
    assert callable(fUML_IntermediateActivities_ForkNode.__init__)


def test_fuml_intermediateactivities_forknode_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_initialnode_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_InitialNode)


def test_fuml_intermediateactivities_initialnode_constructor_exists():
    assert callable(fUML_IntermediateActivities_InitialNode.__init__)


def test_fuml_intermediateactivities_initialnode_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_decisionnode_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_DecisionNode)


def test_fuml_intermediateactivities_decisionnode_constructor_exists():
    assert callable(fUML_IntermediateActivities_DecisionNode.__init__)


def test_fuml_intermediateactivities_decisionnode_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_finalnode_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_FinalNode)


def test_fuml_intermediateactivities_finalnode_constructor_exists():
    assert callable(fUML_IntermediateActivities_FinalNode.__init__)


def test_fuml_intermediateactivities_finalnode_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_joinnode_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_JoinNode)


def test_fuml_intermediateactivities_joinnode_constructor_exists():
    assert callable(fUML_IntermediateActivities_JoinNode.__init__)


def test_fuml_intermediateactivities_joinnode_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_mergenode_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_MergeNode)


def test_fuml_intermediateactivities_mergenode_constructor_exists():
    assert callable(fUML_IntermediateActivities_MergeNode.__init__)


def test_fuml_intermediateactivities_mergenode_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_activityedge_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_ActivityEdge)


def test_intermediateactivities_activityedge_constructor_exists():
    assert callable(IntermediateActivities_ActivityEdge.__init__)


def test_intermediateactivities_activityedge_constructor_args():
    sig = inspect.signature(IntermediateActivities_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_ActivityFinalNode)


def test_fuml_intermediateactivities_activityfinalnode_constructor_exists():
    assert callable(fUML_IntermediateActivities_ActivityFinalNode.__init__)


def test_fuml_intermediateactivities_activityfinalnode_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_ActivityFinalNode.__init__)
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



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_controlflow_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_ControlFlow)


def test_fuml_intermediateactivities_controlflow_constructor_exists():
    assert callable(fUML_IntermediateActivities_ControlFlow.__init__)


def test_fuml_intermediateactivities_controlflow_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_objectflow_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_ObjectFlow)


def test_fuml_intermediateactivities_objectflow_constructor_exists():
    assert callable(fUML_IntermediateActivities_ObjectFlow.__init__)


def test_fuml_intermediateactivities_objectflow_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_communications_reception_is_not_abstract():
    assert not inspect.isabstract(Communications_Reception)


def test_communications_reception_constructor_exists():
    assert callable(Communications_Reception.__init__)


def test_communications_reception_constructor_args():
    sig = inspect.signature(Communications_Reception.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_class_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Class)


def test_fuml_kernel_class_constructor_exists():
    assert callable(fUML_Kernel_Class.__init__)


def test_fuml_kernel_class_constructor_args():
    sig = inspect.signature(fUML_Kernel_Class.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_fuml_kernel_class_has_active():
    assert hasattr(fUML_Kernel_Class, "active")
    descriptor = None
    for klass in fUML_Kernel_Class.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_kernel_enumeration_is_not_abstract():
    assert not inspect.isabstract(Kernel_Enumeration)


def test_kernel_enumeration_constructor_exists():
    assert callable(Kernel_Enumeration.__init__)


def test_kernel_enumeration_constructor_args():
    sig = inspect.signature(Kernel_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_EnumerationLiteral)


def test_fuml_kernel_enumerationliteral_constructor_exists():
    assert callable(fUML_Kernel_EnumerationLiteral.__init__)


def test_fuml_kernel_enumerationliteral_constructor_args():
    sig = inspect.signature(fUML_Kernel_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_kernel_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(Kernel_EnumerationLiteral)


def test_kernel_enumerationliteral_constructor_exists():
    assert callable(Kernel_EnumerationLiteral.__init__)


def test_kernel_enumerationliteral_constructor_args():
    sig = inspect.signature(Kernel_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_literalinteger_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_LiteralInteger)


def test_fuml_kernel_literalinteger_constructor_exists():
    assert callable(fUML_Kernel_LiteralInteger.__init__)


def test_fuml_kernel_literalinteger_constructor_args():
    sig = inspect.signature(fUML_Kernel_LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml_kernel_literalinteger_has_value():
    assert hasattr(fUML_Kernel_LiteralInteger, "value")
    descriptor = None
    for klass in fUML_Kernel_LiteralInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml_kernel_literalstring_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_LiteralString)


def test_fuml_kernel_literalstring_constructor_exists():
    assert callable(fUML_Kernel_LiteralString.__init__)


def test_fuml_kernel_literalstring_constructor_args():
    sig = inspect.signature(fUML_Kernel_LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml_kernel_literalstring_has_value():
    assert hasattr(fUML_Kernel_LiteralString, "value")
    descriptor = None
    for klass in fUML_Kernel_LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml_kernel_literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_LiteralUnlimitedNatural)


def test_fuml_kernel_literalunlimitednatural_constructor_exists():
    assert callable(fUML_Kernel_LiteralUnlimitedNatural.__init__)


def test_fuml_kernel_literalunlimitednatural_constructor_args():
    sig = inspect.signature(fUML_Kernel_LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml_kernel_literalunlimitednatural_has_value():
    assert hasattr(fUML_Kernel_LiteralUnlimitedNatural, "value")
    descriptor = None
    for klass in fUML_Kernel_LiteralUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fuml_kernel_literalnull_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_LiteralNull)


def test_fuml_kernel_literalnull_constructor_exists():
    assert callable(fUML_Kernel_LiteralNull.__init__)


def test_fuml_kernel_literalnull_constructor_args():
    sig = inspect.signature(fUML_Kernel_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_literalboolean_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_LiteralBoolean)


def test_fuml_kernel_literalboolean_constructor_exists():
    assert callable(fUML_Kernel_LiteralBoolean.__init__)


def test_fuml_kernel_literalboolean_constructor_args():
    sig = inspect.signature(fUML_Kernel_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fuml_kernel_literalboolean_has_value():
    assert hasattr(fUML_Kernel_LiteralBoolean, "value")
    descriptor = None
    for klass in fUML_Kernel_LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_literalspecification_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_LiteralSpecification)


def test_fuml_kernel_literalspecification_constructor_exists():
    assert callable(fUML_Kernel_LiteralSpecification.__init__)


def test_fuml_kernel_literalspecification_constructor_args():
    sig = inspect.signature(fUML_Kernel_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_instancevalue_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_InstanceValue)


def test_fuml_kernel_instancevalue_constructor_exists():
    assert callable(fUML_Kernel_InstanceValue.__init__)


def test_fuml_kernel_instancevalue_constructor_args():
    sig = inspect.signature(fUML_Kernel_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_kernel_instancespecification_is_not_abstract():
    assert not inspect.isabstract(Kernel_InstanceSpecification)


def test_kernel_instancespecification_constructor_exists():
    assert callable(Kernel_InstanceSpecification.__init__)


def test_kernel_instancespecification_constructor_args():
    sig = inspect.signature(Kernel_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_kernel_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(Kernel_StructuralFeature)


def test_kernel_structuralfeature_constructor_exists():
    assert callable(Kernel_StructuralFeature.__init__)


def test_kernel_structuralfeature_constructor_args():
    sig = inspect.signature(Kernel_StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_kernel_slot_is_not_abstract():
    assert not inspect.isabstract(Kernel_Slot)


def test_kernel_slot_constructor_exists():
    assert callable(Kernel_Slot.__init__)


def test_kernel_slot_constructor_args():
    sig = inspect.signature(Kernel_Slot.__init__)
    params = list(sig.parameters.keys())



def test_kernel_operation_is_not_abstract():
    assert not inspect.isabstract(Kernel_Operation)


def test_kernel_operation_constructor_exists():
    assert callable(Kernel_Operation.__init__)


def test_kernel_operation_constructor_args():
    sig = inspect.signature(Kernel_Operation.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_enumeration_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Enumeration)


def test_fuml_kernel_enumeration_constructor_exists():
    assert callable(fUML_Kernel_Enumeration.__init__)


def test_fuml_kernel_enumeration_constructor_args():
    sig = inspect.signature(fUML_Kernel_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_primitivetype_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_PrimitiveType)


def test_fuml_kernel_primitivetype_constructor_exists():
    assert callable(fUML_Kernel_PrimitiveType.__init__)


def test_fuml_kernel_primitivetype_constructor_args():
    sig = inspect.signature(fUML_Kernel_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_BehavioralFeature)


def test_fuml_kernel_behavioralfeature_constructor_exists():
    assert callable(fUML_Kernel_BehavioralFeature.__init__)


def test_fuml_kernel_behavioralfeature_constructor_args():
    sig = inspect.signature(fUML_Kernel_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "concurrency" in params, "Missing parameter 'concurrency'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_fuml_kernel_behavioralfeature_has_concurrency():
    assert hasattr(fUML_Kernel_BehavioralFeature, "concurrency")
    descriptor = None
    for klass in fUML_Kernel_BehavioralFeature.__mro__:
        if "concurrency" in klass.__dict__:
            descriptor = klass.__dict__["concurrency"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_behavioralfeature_has_abstract():
    assert hasattr(fUML_Kernel_BehavioralFeature, "abstract")
    descriptor = None
    for klass in fUML_Kernel_BehavioralFeature.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_kernel_valuespecification_is_not_abstract():
    assert not inspect.isabstract(Kernel_ValueSpecification)


def test_kernel_valuespecification_constructor_exists():
    assert callable(Kernel_ValueSpecification.__init__)


def test_kernel_valuespecification_constructor_args():
    sig = inspect.signature(Kernel_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_kernel_class_is_not_abstract():
    assert not inspect.isabstract(Kernel_Class)


def test_kernel_class_constructor_exists():
    assert callable(Kernel_Class.__init__)


def test_kernel_class_constructor_args():
    sig = inspect.signature(Kernel_Class.__init__)
    params = list(sig.parameters.keys())



def test_kernel_datatype_is_not_abstract():
    assert not inspect.isabstract(Kernel_DataType)


def test_kernel_datatype_constructor_exists():
    assert callable(Kernel_DataType.__init__)


def test_kernel_datatype_constructor_args():
    sig = inspect.signature(Kernel_DataType.__init__)
    params = list(sig.parameters.keys())



def test_kernel_association_is_not_abstract():
    assert not inspect.isabstract(Kernel_Association)


def test_kernel_association_constructor_exists():
    assert callable(Kernel_Association.__init__)


def test_kernel_association_constructor_args():
    sig = inspect.signature(Kernel_Association.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_property_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Property)


def test_fuml_kernel_property_constructor_exists():
    assert callable(fUML_Kernel_Property.__init__)


def test_fuml_kernel_property_constructor_args():
    sig = inspect.signature(fUML_Kernel_Property.__init__)
    params = list(sig.parameters.keys())
    assert "composite" in params, "Missing parameter 'composite'"
    assert "derivedUnion" in params, "Missing parameter 'derivedUnion'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "derived" in params, "Missing parameter 'derived'"

def test_fuml_kernel_property_has_composite():
    assert hasattr(fUML_Kernel_Property, "composite")
    descriptor = None
    for klass in fUML_Kernel_Property.__mro__:
        if "composite" in klass.__dict__:
            descriptor = klass.__dict__["composite"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_property_has_derivedUnion():
    assert hasattr(fUML_Kernel_Property, "derivedUnion")
    descriptor = None
    for klass in fUML_Kernel_Property.__mro__:
        if "derivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["derivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_property_has_aggregation():
    assert hasattr(fUML_Kernel_Property, "aggregation")
    descriptor = None
    for klass in fUML_Kernel_Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_property_has_derived():
    assert hasattr(fUML_Kernel_Property, "derived")
    descriptor = None
    for klass in fUML_Kernel_Property.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)



def test_kernel_generalization_is_not_abstract():
    assert not inspect.isabstract(Kernel_Generalization)


def test_kernel_generalization_constructor_exists():
    assert callable(Kernel_Generalization.__init__)


def test_kernel_generalization_constructor_args():
    sig = inspect.signature(Kernel_Generalization.__init__)
    params = list(sig.parameters.keys())



def test_kernel_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(Kernel_RedefinableElement)


def test_kernel_redefinableelement_constructor_exists():
    assert callable(Kernel_RedefinableElement.__init__)


def test_kernel_redefinableelement_constructor_args():
    sig = inspect.signature(Kernel_RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_kernel_classifier_is_not_abstract():
    assert not inspect.isabstract(Kernel_Classifier)


def test_kernel_classifier_constructor_exists():
    assert callable(Kernel_Classifier.__init__)


def test_kernel_classifier_constructor_args():
    sig = inspect.signature(Kernel_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_activityedge_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_ActivityEdge)


def test_fuml_intermediateactivities_activityedge_constructor_exists():
    assert callable(fUML_IntermediateActivities_ActivityEdge.__init__)


def test_fuml_intermediateactivities_activityedge_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_activitynode_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_ActivityNode)


def test_fuml_intermediateactivities_activitynode_constructor_exists():
    assert callable(fUML_IntermediateActivities_ActivityNode.__init__)


def test_fuml_intermediateactivities_activitynode_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_feature_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Feature)


def test_fuml_kernel_feature_constructor_exists():
    assert callable(fUML_Kernel_Feature.__init__)


def test_fuml_kernel_feature_constructor_args():
    sig = inspect.signature(fUML_Kernel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_fuml_kernel_feature_has_static():
    assert hasattr(fUML_Kernel_Feature, "static")
    descriptor = None
    for klass in fUML_Kernel_Feature.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_kernel_typedelement_is_not_abstract():
    assert not inspect.isabstract(Kernel_TypedElement)


def test_kernel_typedelement_constructor_exists():
    assert callable(Kernel_TypedElement.__init__)


def test_kernel_typedelement_constructor_args():
    sig = inspect.signature(Kernel_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactivities_objectnode_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_ObjectNode)


def test_fuml_intermediateactivities_objectnode_constructor_exists():
    assert callable(fUML_IntermediateActivities_ObjectNode.__init__)


def test_fuml_intermediateactivities_objectnode_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_kernel_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(Kernel_MultiplicityElement)


def test_kernel_multiplicityelement_constructor_exists():
    assert callable(Kernel_MultiplicityElement.__init__)


def test_kernel_multiplicityelement_constructor_args():
    sig = inspect.signature(Kernel_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_parameter_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Parameter)


def test_fuml_kernel_parameter_constructor_exists():
    assert callable(fUML_Kernel_Parameter.__init__)


def test_fuml_kernel_parameter_constructor_args():
    sig = inspect.signature(fUML_Kernel_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_fuml_kernel_parameter_has_direction():
    assert hasattr(fUML_Kernel_Parameter, "direction")
    descriptor = None
    for klass in fUML_Kernel_Parameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_fuml_basicactions_pin_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicActions_Pin)


def test_fuml_basicactions_pin_constructor_exists():
    assert callable(fUML_BasicActions_Pin.__init__)


def test_fuml_basicactions_pin_constructor_args():
    sig = inspect.signature(fUML_BasicActions_Pin.__init__)
    params = list(sig.parameters.keys())



def test_kernel_feature_is_not_abstract():
    assert not inspect.isabstract(Kernel_Feature)


def test_kernel_feature_constructor_exists():
    assert callable(Kernel_Feature.__init__)


def test_kernel_feature_constructor_args():
    sig = inspect.signature(Kernel_Feature.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_StructuralFeature)


def test_fuml_kernel_structuralfeature_constructor_exists():
    assert callable(fUML_Kernel_StructuralFeature.__init__)


def test_fuml_kernel_structuralfeature_constructor_args():
    sig = inspect.signature(fUML_Kernel_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_fuml_kernel_structuralfeature_has_readOnly():
    assert hasattr(fUML_Kernel_StructuralFeature, "readOnly")
    descriptor = None
    for klass in fUML_Kernel_StructuralFeature.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_fuml_kernel_element_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Element)


def test_fuml_kernel_element_constructor_exists():
    assert callable(fUML_Kernel_Element.__init__)


def test_fuml_kernel_element_constructor_args():
    sig = inspect.signature(fUML_Kernel_Element.__init__)
    params = list(sig.parameters.keys())



def test_kernel_package_is_not_abstract():
    assert not inspect.isabstract(Kernel_Package)


def test_kernel_package_constructor_exists():
    assert callable(Kernel_Package.__init__)


def test_kernel_package_constructor_args():
    sig = inspect.signature(Kernel_Package.__init__)
    params = list(sig.parameters.keys())



def test_kernel_packageableelement_is_not_abstract():
    assert not inspect.isabstract(Kernel_PackageableElement)


def test_kernel_packageableelement_constructor_exists():
    assert callable(Kernel_PackageableElement.__init__)


def test_kernel_packageableelement_constructor_args():
    sig = inspect.signature(Kernel_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_kernel_packageimport_is_not_abstract():
    assert not inspect.isabstract(Kernel_PackageImport)


def test_kernel_packageimport_constructor_exists():
    assert callable(Kernel_PackageImport.__init__)


def test_kernel_packageimport_constructor_args():
    sig = inspect.signature(Kernel_PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_kernel_elementimport_is_not_abstract():
    assert not inspect.isabstract(Kernel_ElementImport)


def test_kernel_elementimport_constructor_exists():
    assert callable(Kernel_ElementImport.__init__)


def test_kernel_elementimport_constructor_args():
    sig = inspect.signature(Kernel_ElementImport.__init__)
    params = list(sig.parameters.keys())



def test_kernel_namedelement_is_not_abstract():
    assert not inspect.isabstract(Kernel_NamedElement)


def test_kernel_namedelement_constructor_exists():
    assert callable(Kernel_NamedElement.__init__)


def test_kernel_namedelement_constructor_args():
    sig = inspect.signature(Kernel_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_comment_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Comment)


def test_fuml_kernel_comment_constructor_exists():
    assert callable(fUML_Kernel_Comment.__init__)


def test_fuml_kernel_comment_constructor_args():
    sig = inspect.signature(fUML_Kernel_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_fuml_kernel_comment_has_body():
    assert hasattr(fUML_Kernel_Comment, "body")
    descriptor = None
    for klass in fUML_Kernel_Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_kernel_comment_is_not_abstract():
    assert not inspect.isabstract(Kernel_Comment)


def test_kernel_comment_constructor_exists():
    assert callable(Kernel_Comment.__init__)


def test_kernel_comment_constructor_args():
    sig = inspect.signature(Kernel_Comment.__init__)
    params = list(sig.parameters.keys())



def test_kernel_element_is_not_abstract():
    assert not inspect.isabstract(Kernel_Element)


def test_kernel_element_constructor_exists():
    assert callable(Kernel_Element.__init__)


def test_kernel_element_constructor_args():
    sig = inspect.signature(Kernel_Element.__init__)
    params = list(sig.parameters.keys())



def test_kernel_namespace_is_not_abstract():
    assert not inspect.isabstract(Kernel_Namespace)


def test_kernel_namespace_constructor_exists():
    assert callable(Kernel_Namespace.__init__)


def test_kernel_namespace_constructor_args():
    sig = inspect.signature(Kernel_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_package_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Package)


def test_fuml_kernel_package_constructor_exists():
    assert callable(fUML_Kernel_Package.__init__)


def test_fuml_kernel_package_constructor_args():
    sig = inspect.signature(fUML_Kernel_Package.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_elementimport_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_ElementImport)


def test_fuml_kernel_elementimport_constructor_exists():
    assert callable(fUML_Kernel_ElementImport.__init__)


def test_fuml_kernel_elementimport_constructor_args():
    sig = inspect.signature(fUML_Kernel_ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_fuml_kernel_elementimport_has_alias():
    assert hasattr(fUML_Kernel_ElementImport, "alias")
    descriptor = None
    for klass in fUML_Kernel_ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_elementimport_has_visibility():
    assert hasattr(fUML_Kernel_ElementImport, "visibility")
    descriptor = None
    for klass in fUML_Kernel_ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_fuml_kernel_packageimport_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_PackageImport)


def test_fuml_kernel_packageimport_constructor_exists():
    assert callable(fUML_Kernel_PackageImport.__init__)


def test_fuml_kernel_packageimport_constructor_args():
    sig = inspect.signature(fUML_Kernel_PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_fuml_kernel_packageimport_has_visibility():
    assert hasattr(fUML_Kernel_PackageImport, "visibility")
    descriptor = None
    for klass in fUML_Kernel_PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_fuml_kernel_generalization_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Generalization)


def test_fuml_kernel_generalization_constructor_exists():
    assert callable(fUML_Kernel_Generalization.__init__)


def test_fuml_kernel_generalization_constructor_args():
    sig = inspect.signature(fUML_Kernel_Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "substitutable" in params, "Missing parameter 'substitutable'"

def test_fuml_kernel_generalization_has_substitutable():
    assert hasattr(fUML_Kernel_Generalization, "substitutable")
    descriptor = None
    for klass in fUML_Kernel_Generalization.__mro__:
        if "substitutable" in klass.__dict__:
            descriptor = klass.__dict__["substitutable"]
            break
    assert isinstance(descriptor, property)



def test_fuml_completestructuredactivities_clause_is_not_abstract():
    assert not inspect.isabstract(fUML_CompleteStructuredActivities_Clause)


def test_fuml_completestructuredactivities_clause_constructor_exists():
    assert callable(fUML_CompleteStructuredActivities_Clause.__init__)


def test_fuml_completestructuredactivities_clause_constructor_args():
    sig = inspect.signature(fUML_CompleteStructuredActivities_Clause.__init__)
    params = list(sig.parameters.keys())



def test_fuml_intermediateactions_linkenddata_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActions_LinkEndData)


def test_fuml_intermediateactions_linkenddata_constructor_exists():
    assert callable(fUML_IntermediateActions_LinkEndData.__init__)


def test_fuml_intermediateactions_linkenddata_constructor_args():
    sig = inspect.signature(fUML_IntermediateActions_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_MultiplicityElement)


def test_fuml_kernel_multiplicityelement_constructor_exists():
    assert callable(fUML_Kernel_MultiplicityElement.__init__)


def test_fuml_kernel_multiplicityelement_constructor_args():
    sig = inspect.signature(fUML_Kernel_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "ordered" in params, "Missing parameter 'ordered'"

def test_fuml_kernel_multiplicityelement_has_lower():
    assert hasattr(fUML_Kernel_MultiplicityElement, "lower")
    descriptor = None
    for klass in fUML_Kernel_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_multiplicityelement_has_upper():
    assert hasattr(fUML_Kernel_MultiplicityElement, "upper")
    descriptor = None
    for klass in fUML_Kernel_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_multiplicityelement_has_unique():
    assert hasattr(fUML_Kernel_MultiplicityElement, "unique")
    descriptor = None
    for klass in fUML_Kernel_MultiplicityElement.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_multiplicityelement_has_ordered():
    assert hasattr(fUML_Kernel_MultiplicityElement, "ordered")
    descriptor = None
    for klass in fUML_Kernel_MultiplicityElement.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)



def test_fuml_kernel_slot_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Slot)


def test_fuml_kernel_slot_constructor_exists():
    assert callable(fUML_Kernel_Slot.__init__)


def test_fuml_kernel_slot_constructor_args():
    sig = inspect.signature(fUML_Kernel_Slot.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_namedelement_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_NamedElement)


def test_fuml_kernel_namedelement_constructor_exists():
    assert callable(fUML_Kernel_NamedElement.__init__)


def test_fuml_kernel_namedelement_constructor_args():
    sig = inspect.signature(fUML_Kernel_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_fuml_kernel_namedelement_has_name():
    assert hasattr(fUML_Kernel_NamedElement, "name")
    descriptor = None
    for klass in fUML_Kernel_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_namedelement_has_visibility():
    assert hasattr(fUML_Kernel_NamedElement, "visibility")
    descriptor = None
    for klass in fUML_Kernel_NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_namedelement_has_qualifiedName():
    assert hasattr(fUML_Kernel_NamedElement, "qualifiedName")
    descriptor = None
    for klass in fUML_Kernel_NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_kernel_type_is_not_abstract():
    assert not inspect.isabstract(Kernel_Type)


def test_kernel_type_constructor_exists():
    assert callable(Kernel_Type.__init__)


def test_kernel_type_constructor_args():
    sig = inspect.signature(Kernel_Type.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_classifier_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Classifier)


def test_fuml_kernel_classifier_constructor_exists():
    assert callable(fUML_Kernel_Classifier.__init__)


def test_fuml_kernel_classifier_constructor_args():
    sig = inspect.signature(fUML_Kernel_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "finalSpecialization" in params, "Missing parameter 'finalSpecialization'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_fuml_kernel_classifier_has_finalSpecialization():
    assert hasattr(fUML_Kernel_Classifier, "finalSpecialization")
    descriptor = None
    for klass in fUML_Kernel_Classifier.__mro__:
        if "finalSpecialization" in klass.__dict__:
            descriptor = klass.__dict__["finalSpecialization"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_classifier_has_abstract():
    assert hasattr(fUML_Kernel_Classifier, "abstract")
    descriptor = None
    for klass in fUML_Kernel_Classifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_valuespecification_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_ValueSpecification)


def test_fuml_kernel_valuespecification_constructor_exists():
    assert callable(fUML_Kernel_ValueSpecification.__init__)


def test_fuml_kernel_valuespecification_constructor_args():
    sig = inspect.signature(fUML_Kernel_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_operation_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Operation)


def test_fuml_kernel_operation_constructor_exists():
    assert callable(fUML_Kernel_Operation.__init__)


def test_fuml_kernel_operation_constructor_args():
    sig = inspect.signature(fUML_Kernel_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "query" in params, "Missing parameter 'query'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "unique" in params, "Missing parameter 'unique'"

def test_fuml_kernel_operation_has_ordered():
    assert hasattr(fUML_Kernel_Operation, "ordered")
    descriptor = None
    for klass in fUML_Kernel_Operation.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_operation_has_query():
    assert hasattr(fUML_Kernel_Operation, "query")
    descriptor = None
    for klass in fUML_Kernel_Operation.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_operation_has_lower():
    assert hasattr(fUML_Kernel_Operation, "lower")
    descriptor = None
    for klass in fUML_Kernel_Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_operation_has_upper():
    assert hasattr(fUML_Kernel_Operation, "upper")
    descriptor = None
    for klass in fUML_Kernel_Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_fuml_kernel_operation_has_unique():
    assert hasattr(fUML_Kernel_Operation, "unique")
    descriptor = None
    for klass in fUML_Kernel_Operation.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_fuml_communications_reception_is_not_abstract():
    assert not inspect.isabstract(fUML_Communications_Reception)


def test_fuml_communications_reception_constructor_exists():
    assert callable(fUML_Communications_Reception.__init__)


def test_fuml_communications_reception_constructor_args():
    sig = inspect.signature(fUML_Communications_Reception.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_fuml_communications_messageevent_is_not_abstract():
    assert not inspect.isabstract(fUML_Communications_MessageEvent)


def test_fuml_communications_messageevent_constructor_exists():
    assert callable(fUML_Communications_MessageEvent.__init__)


def test_fuml_communications_messageevent_constructor_args():
    sig = inspect.signature(fUML_Communications_MessageEvent.__init__)
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



def test_fuml_communications_signalevent_is_not_abstract():
    assert not inspect.isabstract(fUML_Communications_SignalEvent)


def test_fuml_communications_signalevent_constructor_exists():
    assert callable(fUML_Communications_SignalEvent.__init__)


def test_fuml_communications_signalevent_constructor_args():
    sig = inspect.signature(fUML_Communications_SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_kernel_property_is_not_abstract():
    assert not inspect.isabstract(Kernel_Property)


def test_kernel_property_constructor_exists():
    assert callable(Kernel_Property.__init__)


def test_kernel_property_constructor_args():
    sig = inspect.signature(Kernel_Property.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_type_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Type)


def test_fuml_kernel_type_constructor_exists():
    assert callable(fUML_Kernel_Type.__init__)


def test_fuml_kernel_type_constructor_args():
    sig = inspect.signature(fUML_Kernel_Type.__init__)
    params = list(sig.parameters.keys())



def test_fuml_communications_event_is_not_abstract():
    assert not inspect.isabstract(fUML_Communications_Event)


def test_fuml_communications_event_constructor_exists():
    assert callable(fUML_Communications_Event.__init__)


def test_fuml_communications_event_constructor_args():
    sig = inspect.signature(fUML_Communications_Event.__init__)
    params = list(sig.parameters.keys())



def test_communications_event_is_not_abstract():
    assert not inspect.isabstract(Communications_Event)


def test_communications_event_constructor_exists():
    assert callable(Communications_Event.__init__)


def test_communications_event_constructor_args():
    sig = inspect.signature(Communications_Event.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_packageableelement_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_PackageableElement)


def test_fuml_kernel_packageableelement_constructor_exists():
    assert callable(fUML_Kernel_PackageableElement.__init__)


def test_fuml_kernel_packageableelement_constructor_args():
    sig = inspect.signature(fUML_Kernel_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_instancespecification_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_InstanceSpecification)


def test_fuml_kernel_instancespecification_constructor_exists():
    assert callable(fUML_Kernel_InstanceSpecification.__init__)


def test_fuml_kernel_instancespecification_constructor_args():
    sig = inspect.signature(fUML_Kernel_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_typedelement_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_TypedElement)


def test_fuml_kernel_typedelement_constructor_exists():
    assert callable(fUML_Kernel_TypedElement.__init__)


def test_fuml_kernel_typedelement_constructor_args():
    sig = inspect.signature(fUML_Kernel_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_namespace_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Namespace)


def test_fuml_kernel_namespace_constructor_exists():
    assert callable(fUML_Kernel_Namespace.__init__)


def test_fuml_kernel_namespace_constructor_args():
    sig = inspect.signature(fUML_Kernel_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_RedefinableElement)


def test_fuml_kernel_redefinableelement_constructor_exists():
    assert callable(fUML_Kernel_RedefinableElement.__init__)


def test_fuml_kernel_redefinableelement_constructor_args():
    sig = inspect.signature(fUML_Kernel_RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "leaf" in params, "Missing parameter 'leaf'"

def test_fuml_kernel_redefinableelement_has_leaf():
    assert hasattr(fUML_Kernel_RedefinableElement, "leaf")
    descriptor = None
    for klass in fUML_Kernel_RedefinableElement.__mro__:
        if "leaf" in klass.__dict__:
            descriptor = klass.__dict__["leaf"]
            break
    assert isinstance(descriptor, property)



def test_fuml_communications_trigger_is_not_abstract():
    assert not inspect.isabstract(fUML_Communications_Trigger)


def test_fuml_communications_trigger_constructor_exists():
    assert callable(fUML_Communications_Trigger.__init__)


def test_fuml_communications_trigger_constructor_args():
    sig = inspect.signature(fUML_Communications_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_fuml_basicbehaviors_functionbehavior_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicBehaviors_FunctionBehavior)


def test_fuml_basicbehaviors_functionbehavior_constructor_exists():
    assert callable(fUML_BasicBehaviors_FunctionBehavior.__init__)


def test_fuml_basicbehaviors_functionbehavior_constructor_args():
    sig = inspect.signature(fUML_BasicBehaviors_FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_basicbehaviors_behavior_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors_Behavior)


def test_basicbehaviors_behavior_constructor_exists():
    assert callable(BasicBehaviors_Behavior.__init__)


def test_basicbehaviors_behavior_constructor_args():
    sig = inspect.signature(BasicBehaviors_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_fuml_communications_signal_is_not_abstract():
    assert not inspect.isabstract(fUML_Communications_Signal)


def test_fuml_communications_signal_constructor_exists():
    assert callable(fUML_Communications_Signal.__init__)


def test_fuml_communications_signal_constructor_args():
    sig = inspect.signature(fUML_Communications_Signal.__init__)
    params = list(sig.parameters.keys())



def test_fuml_kernel_association_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_Association)


def test_fuml_kernel_association_constructor_exists():
    assert callable(fUML_Kernel_Association.__init__)


def test_fuml_kernel_association_constructor_args():
    sig = inspect.signature(fUML_Kernel_Association.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"

def test_fuml_kernel_association_has_derived():
    assert hasattr(fUML_Kernel_Association, "derived")
    descriptor = None
    for klass in fUML_Kernel_Association.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)



def test_fuml_kernel_datatype_is_not_abstract():
    assert not inspect.isabstract(fUML_Kernel_DataType)


def test_fuml_kernel_datatype_constructor_exists():
    assert callable(fUML_Kernel_DataType.__init__)


def test_fuml_kernel_datatype_constructor_args():
    sig = inspect.signature(fUML_Kernel_DataType.__init__)
    params = list(sig.parameters.keys())



def test_fuml_basicbehaviors_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicBehaviors_BehavioredClassifier)


def test_fuml_basicbehaviors_behavioredclassifier_constructor_exists():
    assert callable(fUML_BasicBehaviors_BehavioredClassifier.__init__)


def test_fuml_basicbehaviors_behavioredclassifier_constructor_args():
    sig = inspect.signature(fUML_BasicBehaviors_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_basicbehaviors_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BasicBehaviors_BehavioredClassifier)


def test_basicbehaviors_behavioredclassifier_constructor_exists():
    assert callable(BasicBehaviors_BehavioredClassifier.__init__)


def test_basicbehaviors_behavioredclassifier_constructor_args():
    sig = inspect.signature(BasicBehaviors_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_kernel_parameter_is_not_abstract():
    assert not inspect.isabstract(Kernel_Parameter)


def test_kernel_parameter_constructor_exists():
    assert callable(Kernel_Parameter.__init__)


def test_kernel_parameter_constructor_args():
    sig = inspect.signature(Kernel_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_kernel_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(Kernel_BehavioralFeature)


def test_kernel_behavioralfeature_constructor_exists():
    assert callable(Kernel_BehavioralFeature.__init__)


def test_kernel_behavioralfeature_constructor_args():
    sig = inspect.signature(Kernel_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_fuml_basicbehaviors_behavior_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicBehaviors_Behavior)


def test_fuml_basicbehaviors_behavior_constructor_exists():
    assert callable(fUML_BasicBehaviors_Behavior.__init__)


def test_fuml_basicbehaviors_behavior_constructor_args():
    sig = inspect.signature(fUML_BasicBehaviors_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "reentrant" in params, "Missing parameter 'reentrant'"

def test_fuml_basicbehaviors_behavior_has_reentrant():
    assert hasattr(fUML_BasicBehaviors_Behavior, "reentrant")
    descriptor = None
    for klass in fUML_BasicBehaviors_Behavior.__mro__:
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



def test_fuml_intermediateactivities_activity_is_not_abstract():
    assert not inspect.isabstract(fUML_IntermediateActivities_Activity)


def test_fuml_intermediateactivities_activity_constructor_exists():
    assert callable(fUML_IntermediateActivities_Activity.__init__)


def test_fuml_intermediateactivities_activity_constructor_args():
    sig = inspect.signature(fUML_IntermediateActivities_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_fuml_intermediateactivities_activity_has_readOnly():
    assert hasattr(fUML_IntermediateActivities_Activity, "readOnly")
    descriptor = None
    for klass in fUML_IntermediateActivities_Activity.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_fuml_basicbehaviors_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(fUML_BasicBehaviors_OpaqueBehavior)


def test_fuml_basicbehaviors_opaquebehavior_constructor_exists():
    assert callable(fUML_BasicBehaviors_OpaqueBehavior.__init__)


def test_fuml_basicbehaviors_opaquebehavior_constructor_args():
    sig = inspect.signature(fUML_BasicBehaviors_OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_fuml_basicbehaviors_opaquebehavior_has_body():
    assert hasattr(fUML_BasicBehaviors_OpaqueBehavior, "body")
    descriptor = None
    for klass in fUML_BasicBehaviors_OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_fuml_basicbehaviors_opaquebehavior_has_language():
    assert hasattr(fUML_BasicBehaviors_OpaqueBehavior, "language")
    descriptor = None
    for klass in fUML_BasicBehaviors_OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

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
        "out",
        "in_",
        "return_",
        "inout",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"

def test_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "shared",
        "composite",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationKind"

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

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "package",
        "public",
        "private",
        "protected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"


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
fUML_LociL1_SemanticVisitor_strategy = st.builds(
    fUML_LociL1_SemanticVisitor,
)
SemanticVisitor_strategy = st.builds(
    SemanticVisitor,
)
fUML_Kernel_Value_strategy = st.builds(
    fUML_Kernel_Value,
)
Kernel_FeatureValue_strategy = st.builds(
    Kernel_FeatureValue,
)
CompoundValue_strategy = st.builds(
    CompoundValue,
)
fUML_Kernel_DataValue_strategy = st.builds(
    fUML_Kernel_DataValue,
)
fUML_Kernel_ExtensionalValue_strategy = st.builds(
    fUML_Kernel_ExtensionalValue,
)
ExtensionalValue_strategy = st.builds(
    ExtensionalValue,
)
fUML_Kernel_Link_strategy = st.builds(
    fUML_Kernel_Link,
)
fUML_Kernel_Object_strategy = st.builds(
    fUML_Kernel_Object,
)
Kernel_Object_strategy = st.builds(
    Kernel_Object,
)
StructuredValue_strategy = st.builds(
    StructuredValue,
)
fUML_Kernel_CompoundValue_strategy = st.builds(
    fUML_Kernel_CompoundValue,
)
fUML_Kernel_Reference_strategy = st.builds(
    fUML_Kernel_Reference,
)
Kernel_PrimitiveType_strategy = st.builds(
    Kernel_PrimitiveType,
)
PrimitiveValue_strategy = st.builds(
    PrimitiveValue,
)
fUML_Kernel_IntegerValue_strategy = st.builds(
    fUML_Kernel_IntegerValue,
    value=
        st.integers()
)
fUML_Kernel_BooleanValue_strategy = st.builds(
    fUML_Kernel_BooleanValue,
    value=
        st.booleans()
)
fUML_Kernel_UnlimitedNaturalValue_strategy = st.builds(
    fUML_Kernel_UnlimitedNaturalValue,
    value=
        st.integers()
)
Kernel_Value_strategy = st.builds(
    Kernel_Value,
)
fUML_Kernel_FeatureValue_strategy = st.builds(
    fUML_Kernel_FeatureValue,
    position=
        st.integers()
)
Value_strategy = st.builds(
    Value,
)
fUML_Kernel_PrimitiveValue_strategy = st.builds(
    fUML_Kernel_PrimitiveValue,
)
fUML_Kernel_EnumerationValue_strategy = st.builds(
    fUML_Kernel_EnumerationValue,
)
fUML_Kernel_StructuredValue_strategy = st.builds(
    fUML_Kernel_StructuredValue,
)
fUML_Kernel_StringValue_strategy = st.builds(
    fUML_Kernel_StringValue,
    value=
        safe_text
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
fUML_BasicActions_SendSignalAction_strategy = st.builds(
    fUML_BasicActions_SendSignalAction,
)
fUML_BasicActions_CallAction_strategy = st.builds(
    fUML_BasicActions_CallAction,
    synchronous=
        st.booleans()
)
IntermediateActivities_ObjectNode_strategy = st.builds(
    IntermediateActivities_ObjectNode,
)
Pin_strategy = st.builds(
    Pin,
)
fUML_BasicActions_OutputPin_strategy = st.builds(
    fUML_BasicActions_OutputPin,
)
fUML_BasicActions_InputPin_strategy = st.builds(
    fUML_BasicActions_InputPin,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
fUML_BasicActions_Action_strategy = st.builds(
    fUML_BasicActions_Action,
    locallyReentrant=
        st.booleans()
)
Communications_Trigger_strategy = st.builds(
    Communications_Trigger,
)
CallAction_strategy = st.builds(
    CallAction,
)
fUML_BasicActions_CallBehaviorAction_strategy = st.builds(
    fUML_BasicActions_CallBehaviorAction,
)
fUML_BasicActions_CallOperationAction_strategy = st.builds(
    fUML_BasicActions_CallOperationAction,
)
fUML_CompleteActions_StartObjectBehaviorAction_strategy = st.builds(
    fUML_CompleteActions_StartObjectBehaviorAction,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
fUML_IntermediateActions_DestroyLinkAction_strategy = st.builds(
    fUML_IntermediateActions_DestroyLinkAction,
)
fUML_IntermediateActions_CreateLinkAction_strategy = st.builds(
    fUML_IntermediateActions_CreateLinkAction,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
fUML_IntermediateActions_LinkEndDestructionData_strategy = st.builds(
    fUML_IntermediateActions_LinkEndDestructionData,
    destroyDuplicates=
        st.booleans()
)
fUML_IntermediateActions_LinkEndCreationData_strategy = st.builds(
    fUML_IntermediateActions_LinkEndCreationData,
    replaceAll=
        st.booleans()
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
fUML_IntermediateActions_AddStructuralFeatureValueAction_strategy = st.builds(
    fUML_IntermediateActions_AddStructuralFeatureValueAction,
    replaceAll=
        st.booleans()
)
fUML_IntermediateActions_RemoveStructuralFeatureValueAction_strategy = st.builds(
    fUML_IntermediateActions_RemoveStructuralFeatureValueAction,
    removeDuplicates=
        st.booleans()
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
fUML_IntermediateActions_ClearStructuralFeatureAction_strategy = st.builds(
    fUML_IntermediateActions_ClearStructuralFeatureAction,
)
fUML_IntermediateActions_ReadStructuralFeatureAction_strategy = st.builds(
    fUML_IntermediateActions_ReadStructuralFeatureAction,
)
fUML_IntermediateActions_WriteStructuralFeatureAction_strategy = st.builds(
    fUML_IntermediateActions_WriteStructuralFeatureAction,
)
IntermediateActions_LinkEndData_strategy = st.builds(
    IntermediateActions_LinkEndData,
)
ExtraStructuredActivities_ExpansionNode_strategy = st.builds(
    ExtraStructuredActivities_ExpansionNode,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
fUML_IntermediateActions_ReadLinkAction_strategy = st.builds(
    fUML_IntermediateActions_ReadLinkAction,
)
fUML_IntermediateActions_WriteLinkAction_strategy = st.builds(
    fUML_IntermediateActions_WriteLinkAction,
)
ExtraStructuredActivities_ExpansionRegion_strategy = st.builds(
    ExtraStructuredActivities_ExpansionRegion,
)
Action_strategy = st.builds(
    Action,
)
fUML_IntermediateActions_CreateObjectAction_strategy = st.builds(
    fUML_IntermediateActions_CreateObjectAction,
)
fUML_BasicActions_InvocationAction_strategy = st.builds(
    fUML_BasicActions_InvocationAction,
)
fUML_CompleteActions_ReadExtentAction_strategy = st.builds(
    fUML_CompleteActions_ReadExtentAction,
)
fUML_IntermediateActions_ValueSpecificationAction_strategy = st.builds(
    fUML_IntermediateActions_ValueSpecificationAction,
)
fUML_IntermediateActions_LinkAction_strategy = st.builds(
    fUML_IntermediateActions_LinkAction,
)
fUML_IntermediateActions_DestroyObjectAction_strategy = st.builds(
    fUML_IntermediateActions_DestroyObjectAction,
    destroyOwnedObjects=
        st.booleans(),
    destroyLinks=
        st.booleans()
)
fUML_IntermediateActions_ClearAssociationAction_strategy = st.builds(
    fUML_IntermediateActions_ClearAssociationAction,
)
fUML_IntermediateActions_StructuralFeatureAction_strategy = st.builds(
    fUML_IntermediateActions_StructuralFeatureAction,
)
fUML_IntermediateActions_TestIdentityAction_strategy = st.builds(
    fUML_IntermediateActions_TestIdentityAction,
)
fUML_CompleteActions_StartClassifierBehaviorAction_strategy = st.builds(
    fUML_CompleteActions_StartClassifierBehaviorAction,
)
fUML_CompleteActions_ReclassifyObjectAction_strategy = st.builds(
    fUML_CompleteActions_ReclassifyObjectAction,
    replaceAll=
        st.booleans()
)
fUML_IntermediateActions_ReadSelfAction_strategy = st.builds(
    fUML_IntermediateActions_ReadSelfAction,
)
fUML_CompleteActions_ReduceAction_strategy = st.builds(
    fUML_CompleteActions_ReduceAction,
    ordered=
        st.booleans()
)
fUML_CompleteActions_ReadIsClassifiedObjectAction_strategy = st.builds(
    fUML_CompleteActions_ReadIsClassifiedObjectAction,
    direct=
        st.booleans()
)
fUML_CompleteActions_AcceptEventAction_strategy = st.builds(
    fUML_CompleteActions_AcceptEventAction,
    unmarshall=
        st.booleans()
)
fUML_CompleteStructuredActivities_StructuredActivityNode_strategy = st.builds(
    fUML_CompleteStructuredActivities_StructuredActivityNode,
    mustIsolate=
        st.booleans()
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
fUML_CompleteStructuredActivities_ConditionalNode_strategy = st.builds(
    fUML_CompleteStructuredActivities_ConditionalNode,
    determinate=
        st.booleans(),
    assured=
        st.booleans()
)
fUML_ExtraStructuredActivities_ExpansionRegion_strategy = st.builds(
    fUML_ExtraStructuredActivities_ExpansionRegion,
    mode=
        safe_text
)
fUML_CompleteStructuredActivities_LoopNode_strategy = st.builds(
    fUML_CompleteStructuredActivities_LoopNode,
    testedFirst=
        st.booleans()
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
fUML_ExtraStructuredActivities_ExpansionNode_strategy = st.builds(
    fUML_ExtraStructuredActivities_ExpansionNode,
)
fUML_IntermediateActivities_ActivityParameterNode_strategy = st.builds(
    fUML_IntermediateActivities_ActivityParameterNode,
)
CompleteStructuredActivities_Clause_strategy = st.builds(
    CompleteStructuredActivities_Clause,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
fUML_CompleteStructuredActivities_ExecutableNode_strategy = st.builds(
    fUML_CompleteStructuredActivities_ExecutableNode,
)
fUML_IntermediateActivities_ControlNode_strategy = st.builds(
    fUML_IntermediateActivities_ControlNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
fUML_IntermediateActivities_ForkNode_strategy = st.builds(
    fUML_IntermediateActivities_ForkNode,
)
fUML_IntermediateActivities_InitialNode_strategy = st.builds(
    fUML_IntermediateActivities_InitialNode,
)
fUML_IntermediateActivities_DecisionNode_strategy = st.builds(
    fUML_IntermediateActivities_DecisionNode,
)
fUML_IntermediateActivities_FinalNode_strategy = st.builds(
    fUML_IntermediateActivities_FinalNode,
)
fUML_IntermediateActivities_JoinNode_strategy = st.builds(
    fUML_IntermediateActivities_JoinNode,
)
fUML_IntermediateActivities_MergeNode_strategy = st.builds(
    fUML_IntermediateActivities_MergeNode,
)
IntermediateActivities_ActivityEdge_strategy = st.builds(
    IntermediateActivities_ActivityEdge,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
fUML_IntermediateActivities_ActivityFinalNode_strategy = st.builds(
    fUML_IntermediateActivities_ActivityFinalNode,
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
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
fUML_IntermediateActivities_ControlFlow_strategy = st.builds(
    fUML_IntermediateActivities_ControlFlow,
)
fUML_IntermediateActivities_ObjectFlow_strategy = st.builds(
    fUML_IntermediateActivities_ObjectFlow,
)
Communications_Reception_strategy = st.builds(
    Communications_Reception,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
fUML_Kernel_Class_strategy = st.builds(
    fUML_Kernel_Class,
    active=
        st.booleans()
)
Kernel_Enumeration_strategy = st.builds(
    Kernel_Enumeration,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
fUML_Kernel_EnumerationLiteral_strategy = st.builds(
    fUML_Kernel_EnumerationLiteral,
)
Kernel_EnumerationLiteral_strategy = st.builds(
    Kernel_EnumerationLiteral,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
fUML_Kernel_LiteralInteger_strategy = st.builds(
    fUML_Kernel_LiteralInteger,
    value=
        st.integers()
)
fUML_Kernel_LiteralString_strategy = st.builds(
    fUML_Kernel_LiteralString,
    value=
        safe_text
)
fUML_Kernel_LiteralUnlimitedNatural_strategy = st.builds(
    fUML_Kernel_LiteralUnlimitedNatural,
    value=
        st.integers()
)
fUML_Kernel_LiteralNull_strategy = st.builds(
    fUML_Kernel_LiteralNull,
)
fUML_Kernel_LiteralBoolean_strategy = st.builds(
    fUML_Kernel_LiteralBoolean,
    value=
        st.booleans()
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
fUML_Kernel_LiteralSpecification_strategy = st.builds(
    fUML_Kernel_LiteralSpecification,
)
fUML_Kernel_InstanceValue_strategy = st.builds(
    fUML_Kernel_InstanceValue,
)
Kernel_InstanceSpecification_strategy = st.builds(
    Kernel_InstanceSpecification,
)
Kernel_StructuralFeature_strategy = st.builds(
    Kernel_StructuralFeature,
)
Kernel_Slot_strategy = st.builds(
    Kernel_Slot,
)
Kernel_Operation_strategy = st.builds(
    Kernel_Operation,
)
DataType_strategy = st.builds(
    DataType,
)
fUML_Kernel_Enumeration_strategy = st.builds(
    fUML_Kernel_Enumeration,
)
fUML_Kernel_PrimitiveType_strategy = st.builds(
    fUML_Kernel_PrimitiveType,
)
Feature_strategy = st.builds(
    Feature,
)
fUML_Kernel_BehavioralFeature_strategy = st.builds(
    fUML_Kernel_BehavioralFeature,
    concurrency=
        safe_text,
    abstract=
        st.booleans()
)
Kernel_ValueSpecification_strategy = st.builds(
    Kernel_ValueSpecification,
)
Kernel_Class_strategy = st.builds(
    Kernel_Class,
)
Kernel_DataType_strategy = st.builds(
    Kernel_DataType,
)
Kernel_Association_strategy = st.builds(
    Kernel_Association,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
fUML_Kernel_Property_strategy = st.builds(
    fUML_Kernel_Property,
    composite=
        st.booleans(),
    derivedUnion=
        st.booleans(),
    aggregation=
        safe_text,
    derived=
        st.booleans()
)
Kernel_Generalization_strategy = st.builds(
    Kernel_Generalization,
)
Kernel_RedefinableElement_strategy = st.builds(
    Kernel_RedefinableElement,
)
Kernel_Classifier_strategy = st.builds(
    Kernel_Classifier,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
fUML_IntermediateActivities_ActivityEdge_strategy = st.builds(
    fUML_IntermediateActivities_ActivityEdge,
)
fUML_IntermediateActivities_ActivityNode_strategy = st.builds(
    fUML_IntermediateActivities_ActivityNode,
)
fUML_Kernel_Feature_strategy = st.builds(
    fUML_Kernel_Feature,
    static=
        st.booleans()
)
Kernel_TypedElement_strategy = st.builds(
    Kernel_TypedElement,
)
fUML_IntermediateActivities_ObjectNode_strategy = st.builds(
    fUML_IntermediateActivities_ObjectNode,
)
Kernel_MultiplicityElement_strategy = st.builds(
    Kernel_MultiplicityElement,
)
fUML_Kernel_Parameter_strategy = st.builds(
    fUML_Kernel_Parameter,
    direction=
        safe_text
)
fUML_BasicActions_Pin_strategy = st.builds(
    fUML_BasicActions_Pin,
)
Kernel_Feature_strategy = st.builds(
    Kernel_Feature,
)
fUML_Kernel_StructuralFeature_strategy = st.builds(
    fUML_Kernel_StructuralFeature,
    readOnly=
        st.booleans()
)
fUML_Kernel_Element_strategy = st.builds(
    fUML_Kernel_Element,
)
Kernel_Package_strategy = st.builds(
    Kernel_Package,
)
Kernel_PackageableElement_strategy = st.builds(
    Kernel_PackageableElement,
)
Kernel_PackageImport_strategy = st.builds(
    Kernel_PackageImport,
)
Kernel_ElementImport_strategy = st.builds(
    Kernel_ElementImport,
)
Kernel_NamedElement_strategy = st.builds(
    Kernel_NamedElement,
)
fUML_Kernel_Comment_strategy = st.builds(
    fUML_Kernel_Comment,
    body=
        safe_text
)
Kernel_Comment_strategy = st.builds(
    Kernel_Comment,
)
Kernel_Element_strategy = st.builds(
    Kernel_Element,
)
Kernel_Namespace_strategy = st.builds(
    Kernel_Namespace,
)
fUML_Kernel_Package_strategy = st.builds(
    fUML_Kernel_Package,
)
Element_strategy = st.builds(
    Element,
)
fUML_Kernel_ElementImport_strategy = st.builds(
    fUML_Kernel_ElementImport,
    alias=
        safe_text,
    visibility=
        safe_text
)
fUML_Kernel_PackageImport_strategy = st.builds(
    fUML_Kernel_PackageImport,
    visibility=
        safe_text
)
fUML_Kernel_Generalization_strategy = st.builds(
    fUML_Kernel_Generalization,
    substitutable=
        st.booleans()
)
fUML_CompleteStructuredActivities_Clause_strategy = st.builds(
    fUML_CompleteStructuredActivities_Clause,
)
fUML_IntermediateActions_LinkEndData_strategy = st.builds(
    fUML_IntermediateActions_LinkEndData,
)
fUML_Kernel_MultiplicityElement_strategy = st.builds(
    fUML_Kernel_MultiplicityElement,
    lower=
        st.integers(),
    upper=
        st.integers(),
    unique=
        st.booleans(),
    ordered=
        st.booleans()
)
fUML_Kernel_Slot_strategy = st.builds(
    fUML_Kernel_Slot,
)
fUML_Kernel_NamedElement_strategy = st.builds(
    fUML_Kernel_NamedElement,
    name=
        safe_text,
    visibility=
        safe_text,
    qualifiedName=
        safe_text
)
Kernel_Type_strategy = st.builds(
    Kernel_Type,
)
fUML_Kernel_Classifier_strategy = st.builds(
    fUML_Kernel_Classifier,
    finalSpecialization=
        st.booleans(),
    abstract=
        st.booleans()
)
TypedElement_strategy = st.builds(
    TypedElement,
)
fUML_Kernel_ValueSpecification_strategy = st.builds(
    fUML_Kernel_ValueSpecification,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
fUML_Kernel_Operation_strategy = st.builds(
    fUML_Kernel_Operation,
    ordered=
        st.booleans(),
    query=
        st.booleans(),
    lower=
        st.integers(),
    upper=
        st.integers(),
    unique=
        st.booleans()
)
fUML_Communications_Reception_strategy = st.builds(
    fUML_Communications_Reception,
)
Event_strategy = st.builds(
    Event,
)
fUML_Communications_MessageEvent_strategy = st.builds(
    fUML_Communications_MessageEvent,
)
Communications_Signal_strategy = st.builds(
    Communications_Signal,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
fUML_Communications_SignalEvent_strategy = st.builds(
    fUML_Communications_SignalEvent,
)
Kernel_Property_strategy = st.builds(
    Kernel_Property,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
fUML_Kernel_Type_strategy = st.builds(
    fUML_Kernel_Type,
)
fUML_Communications_Event_strategy = st.builds(
    fUML_Communications_Event,
)
Communications_Event_strategy = st.builds(
    Communications_Event,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fUML_Kernel_PackageableElement_strategy = st.builds(
    fUML_Kernel_PackageableElement,
)
fUML_Kernel_InstanceSpecification_strategy = st.builds(
    fUML_Kernel_InstanceSpecification,
)
fUML_Kernel_TypedElement_strategy = st.builds(
    fUML_Kernel_TypedElement,
)
fUML_Kernel_Namespace_strategy = st.builds(
    fUML_Kernel_Namespace,
)
fUML_Kernel_RedefinableElement_strategy = st.builds(
    fUML_Kernel_RedefinableElement,
    leaf=
        st.booleans()
)
fUML_Communications_Trigger_strategy = st.builds(
    fUML_Communications_Trigger,
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
fUML_BasicBehaviors_FunctionBehavior_strategy = st.builds(
    fUML_BasicBehaviors_FunctionBehavior,
)
BasicBehaviors_Behavior_strategy = st.builds(
    BasicBehaviors_Behavior,
)
Classifier_strategy = st.builds(
    Classifier,
)
fUML_Communications_Signal_strategy = st.builds(
    fUML_Communications_Signal,
)
fUML_Kernel_Association_strategy = st.builds(
    fUML_Kernel_Association,
    derived=
        st.booleans()
)
fUML_Kernel_DataType_strategy = st.builds(
    fUML_Kernel_DataType,
)
fUML_BasicBehaviors_BehavioredClassifier_strategy = st.builds(
    fUML_BasicBehaviors_BehavioredClassifier,
)
BasicBehaviors_BehavioredClassifier_strategy = st.builds(
    BasicBehaviors_BehavioredClassifier,
)
Kernel_Parameter_strategy = st.builds(
    Kernel_Parameter,
)
Kernel_BehavioralFeature_strategy = st.builds(
    Kernel_BehavioralFeature,
)
Class_strategy = st.builds(
    Class,
)
fUML_BasicBehaviors_Behavior_strategy = st.builds(
    fUML_BasicBehaviors_Behavior,
    reentrant=
        st.booleans()
)
Behavior_strategy = st.builds(
    Behavior,
)
fUML_IntermediateActivities_Activity_strategy = st.builds(
    fUML_IntermediateActivities_Activity,
    readOnly=
        st.booleans()
)
fUML_BasicBehaviors_OpaqueBehavior_strategy = st.builds(
    fUML_BasicBehaviors_OpaqueBehavior,
    body=
        safe_text,
    language=
        safe_text
)

@given(instance=fUML_LociL1_SemanticVisitor_strategy)
@settings(max_examples=50)
def test_fuml_locil1_semanticvisitor_instantiation(instance):
    assert isinstance(instance, fUML_LociL1_SemanticVisitor)

@given(instance=SemanticVisitor_strategy)
@settings(max_examples=50)
def test_semanticvisitor_instantiation(instance):
    assert isinstance(instance, SemanticVisitor)

@given(instance=fUML_Kernel_Value_strategy)
@settings(max_examples=50)
def test_fuml_kernel_value_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Value)

@given(instance=Kernel_FeatureValue_strategy)
@settings(max_examples=50)
def test_kernel_featurevalue_instantiation(instance):
    assert isinstance(instance, Kernel_FeatureValue)

@given(instance=CompoundValue_strategy)
@settings(max_examples=50)
def test_compoundvalue_instantiation(instance):
    assert isinstance(instance, CompoundValue)

@given(instance=fUML_Kernel_DataValue_strategy)
@settings(max_examples=50)
def test_fuml_kernel_datavalue_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_DataValue)

@given(instance=fUML_Kernel_ExtensionalValue_strategy)
@settings(max_examples=50)
def test_fuml_kernel_extensionalvalue_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_ExtensionalValue)

@given(instance=ExtensionalValue_strategy)
@settings(max_examples=50)
def test_extensionalvalue_instantiation(instance):
    assert isinstance(instance, ExtensionalValue)

@given(instance=fUML_Kernel_Link_strategy)
@settings(max_examples=50)
def test_fuml_kernel_link_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Link)

@given(instance=fUML_Kernel_Object_strategy)
@settings(max_examples=50)
def test_fuml_kernel_object_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Object)

@given(instance=Kernel_Object_strategy)
@settings(max_examples=50)
def test_kernel_object_instantiation(instance):
    assert isinstance(instance, Kernel_Object)

@given(instance=StructuredValue_strategy)
@settings(max_examples=50)
def test_structuredvalue_instantiation(instance):
    assert isinstance(instance, StructuredValue)

@given(instance=fUML_Kernel_CompoundValue_strategy)
@settings(max_examples=50)
def test_fuml_kernel_compoundvalue_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_CompoundValue)

@given(instance=fUML_Kernel_Reference_strategy)
@settings(max_examples=50)
def test_fuml_kernel_reference_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Reference)

@given(instance=Kernel_PrimitiveType_strategy)
@settings(max_examples=50)
def test_kernel_primitivetype_instantiation(instance):
    assert isinstance(instance, Kernel_PrimitiveType)

@given(instance=PrimitiveValue_strategy)
@settings(max_examples=50)
def test_primitivevalue_instantiation(instance):
    assert isinstance(instance, PrimitiveValue)

@given(instance=fUML_Kernel_IntegerValue_strategy)
@settings(max_examples=50)
def test_fuml_kernel_integervalue_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_IntegerValue)



@given(instance=fUML_Kernel_IntegerValue_strategy)
def test_fuml_kernel_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fUML_Kernel_BooleanValue_strategy)
@settings(max_examples=50)
def test_fuml_kernel_booleanvalue_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_BooleanValue)



@given(instance=fUML_Kernel_BooleanValue_strategy)
def test_fuml_kernel_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fUML_Kernel_UnlimitedNaturalValue_strategy)
@settings(max_examples=50)
def test_fuml_kernel_unlimitednaturalvalue_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_UnlimitedNaturalValue)



@given(instance=fUML_Kernel_UnlimitedNaturalValue_strategy)
def test_fuml_kernel_unlimitednaturalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Kernel_Value_strategy)
@settings(max_examples=50)
def test_kernel_value_instantiation(instance):
    assert isinstance(instance, Kernel_Value)

@given(instance=fUML_Kernel_FeatureValue_strategy)
@settings(max_examples=50)
def test_fuml_kernel_featurevalue_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_FeatureValue)



@given(instance=fUML_Kernel_FeatureValue_strategy)
def test_fuml_kernel_featurevalue_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=fUML_Kernel_PrimitiveValue_strategy)
@settings(max_examples=50)
def test_fuml_kernel_primitivevalue_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_PrimitiveValue)

@given(instance=fUML_Kernel_EnumerationValue_strategy)
@settings(max_examples=50)
def test_fuml_kernel_enumerationvalue_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_EnumerationValue)

@given(instance=fUML_Kernel_StructuredValue_strategy)
@settings(max_examples=50)
def test_fuml_kernel_structuredvalue_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_StructuredValue)

@given(instance=fUML_Kernel_StringValue_strategy)
@settings(max_examples=50)
def test_fuml_kernel_stringvalue_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_StringValue)



@given(instance=fUML_Kernel_StringValue_strategy)
def test_fuml_kernel_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=fUML_BasicActions_SendSignalAction_strategy)
@settings(max_examples=50)
def test_fuml_basicactions_sendsignalaction_instantiation(instance):
    assert isinstance(instance, fUML_BasicActions_SendSignalAction)

@given(instance=fUML_BasicActions_CallAction_strategy)
@settings(max_examples=50)
def test_fuml_basicactions_callaction_instantiation(instance):
    assert isinstance(instance, fUML_BasicActions_CallAction)



@given(instance=fUML_BasicActions_CallAction_strategy)
def test_fuml_basicactions_callaction_synchronous_setter(instance):
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

@given(instance=fUML_BasicActions_OutputPin_strategy)
@settings(max_examples=50)
def test_fuml_basicactions_outputpin_instantiation(instance):
    assert isinstance(instance, fUML_BasicActions_OutputPin)

@given(instance=fUML_BasicActions_InputPin_strategy)
@settings(max_examples=50)
def test_fuml_basicactions_inputpin_instantiation(instance):
    assert isinstance(instance, fUML_BasicActions_InputPin)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=fUML_BasicActions_Action_strategy)
@settings(max_examples=50)
def test_fuml_basicactions_action_instantiation(instance):
    assert isinstance(instance, fUML_BasicActions_Action)



@given(instance=fUML_BasicActions_Action_strategy)
def test_fuml_basicactions_action_locallyReentrant_setter(instance):
    original = instance.locallyReentrant
    instance.locallyReentrant = original
    assert instance.locallyReentrant == original

@given(instance=Communications_Trigger_strategy)
@settings(max_examples=50)
def test_communications_trigger_instantiation(instance):
    assert isinstance(instance, Communications_Trigger)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=fUML_BasicActions_CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_fuml_basicactions_callbehavioraction_instantiation(instance):
    assert isinstance(instance, fUML_BasicActions_CallBehaviorAction)

@given(instance=fUML_BasicActions_CallOperationAction_strategy)
@settings(max_examples=50)
def test_fuml_basicactions_calloperationaction_instantiation(instance):
    assert isinstance(instance, fUML_BasicActions_CallOperationAction)

@given(instance=fUML_CompleteActions_StartObjectBehaviorAction_strategy)
@settings(max_examples=50)
def test_fuml_completeactions_startobjectbehavioraction_instantiation(instance):
    assert isinstance(instance, fUML_CompleteActions_StartObjectBehaviorAction)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=fUML_IntermediateActions_DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_destroylinkaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_DestroyLinkAction)

@given(instance=fUML_IntermediateActions_CreateLinkAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_createlinkaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_CreateLinkAction)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=fUML_IntermediateActions_LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_LinkEndDestructionData)



@given(instance=fUML_IntermediateActions_LinkEndDestructionData_strategy)
def test_fuml_intermediateactions_linkenddestructiondata_destroyDuplicates_setter(instance):
    original = instance.destroyDuplicates
    instance.destroyDuplicates = original
    assert instance.destroyDuplicates == original

@given(instance=fUML_IntermediateActions_LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_linkendcreationdata_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_LinkEndCreationData)



@given(instance=fUML_IntermediateActions_LinkEndCreationData_strategy)
def test_fuml_intermediateactions_linkendcreationdata_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=fUML_IntermediateActions_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_AddStructuralFeatureValueAction)



@given(instance=fUML_IntermediateActions_AddStructuralFeatureValueAction_strategy)
def test_fuml_intermediateactions_addstructuralfeaturevalueaction_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=fUML_IntermediateActions_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_RemoveStructuralFeatureValueAction)



@given(instance=fUML_IntermediateActions_RemoveStructuralFeatureValueAction_strategy)
def test_fuml_intermediateactions_removestructuralfeaturevalueaction_removeDuplicates_setter(instance):
    original = instance.removeDuplicates
    instance.removeDuplicates = original
    assert instance.removeDuplicates == original

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=fUML_IntermediateActions_ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_ClearStructuralFeatureAction)

@given(instance=fUML_IntermediateActions_ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_ReadStructuralFeatureAction)

@given(instance=fUML_IntermediateActions_WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_WriteStructuralFeatureAction)

@given(instance=IntermediateActions_LinkEndData_strategy)
@settings(max_examples=50)
def test_intermediateactions_linkenddata_instantiation(instance):
    assert isinstance(instance, IntermediateActions_LinkEndData)

@given(instance=ExtraStructuredActivities_ExpansionNode_strategy)
@settings(max_examples=50)
def test_extrastructuredactivities_expansionnode_instantiation(instance):
    assert isinstance(instance, ExtraStructuredActivities_ExpansionNode)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=fUML_IntermediateActions_ReadLinkAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_readlinkaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_ReadLinkAction)

@given(instance=fUML_IntermediateActions_WriteLinkAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_writelinkaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_WriteLinkAction)

@given(instance=ExtraStructuredActivities_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_extrastructuredactivities_expansionregion_instantiation(instance):
    assert isinstance(instance, ExtraStructuredActivities_ExpansionRegion)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=fUML_IntermediateActions_CreateObjectAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_createobjectaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_CreateObjectAction)

@given(instance=fUML_BasicActions_InvocationAction_strategy)
@settings(max_examples=50)
def test_fuml_basicactions_invocationaction_instantiation(instance):
    assert isinstance(instance, fUML_BasicActions_InvocationAction)

@given(instance=fUML_CompleteActions_ReadExtentAction_strategy)
@settings(max_examples=50)
def test_fuml_completeactions_readextentaction_instantiation(instance):
    assert isinstance(instance, fUML_CompleteActions_ReadExtentAction)

@given(instance=fUML_IntermediateActions_ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_valuespecificationaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_ValueSpecificationAction)

@given(instance=fUML_IntermediateActions_LinkAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_linkaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_LinkAction)

@given(instance=fUML_IntermediateActions_DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_destroyobjectaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_DestroyObjectAction)



@given(instance=fUML_IntermediateActions_DestroyObjectAction_strategy)
def test_fuml_intermediateactions_destroyobjectaction_destroyOwnedObjects_setter(instance):
    original = instance.destroyOwnedObjects
    instance.destroyOwnedObjects = original
    assert instance.destroyOwnedObjects == original



@given(instance=fUML_IntermediateActions_DestroyObjectAction_strategy)
def test_fuml_intermediateactions_destroyobjectaction_destroyLinks_setter(instance):
    original = instance.destroyLinks
    instance.destroyLinks = original
    assert instance.destroyLinks == original

@given(instance=fUML_IntermediateActions_ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_clearassociationaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_ClearAssociationAction)

@given(instance=fUML_IntermediateActions_StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_StructuralFeatureAction)

@given(instance=fUML_IntermediateActions_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_testidentityaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_TestIdentityAction)

@given(instance=fUML_CompleteActions_StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_fuml_completeactions_startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, fUML_CompleteActions_StartClassifierBehaviorAction)

@given(instance=fUML_CompleteActions_ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_fuml_completeactions_reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, fUML_CompleteActions_ReclassifyObjectAction)



@given(instance=fUML_CompleteActions_ReclassifyObjectAction_strategy)
def test_fuml_completeactions_reclassifyobjectaction_replaceAll_setter(instance):
    original = instance.replaceAll
    instance.replaceAll = original
    assert instance.replaceAll == original

@given(instance=fUML_IntermediateActions_ReadSelfAction_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_readselfaction_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_ReadSelfAction)

@given(instance=fUML_CompleteActions_ReduceAction_strategy)
@settings(max_examples=50)
def test_fuml_completeactions_reduceaction_instantiation(instance):
    assert isinstance(instance, fUML_CompleteActions_ReduceAction)



@given(instance=fUML_CompleteActions_ReduceAction_strategy)
def test_fuml_completeactions_reduceaction_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=fUML_CompleteActions_ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_fuml_completeactions_readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, fUML_CompleteActions_ReadIsClassifiedObjectAction)



@given(instance=fUML_CompleteActions_ReadIsClassifiedObjectAction_strategy)
def test_fuml_completeactions_readisclassifiedobjectaction_direct_setter(instance):
    original = instance.direct
    instance.direct = original
    assert instance.direct == original

@given(instance=fUML_CompleteActions_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_fuml_completeactions_accepteventaction_instantiation(instance):
    assert isinstance(instance, fUML_CompleteActions_AcceptEventAction)



@given(instance=fUML_CompleteActions_AcceptEventAction_strategy)
def test_fuml_completeactions_accepteventaction_unmarshall_setter(instance):
    original = instance.unmarshall
    instance.unmarshall = original
    assert instance.unmarshall == original

@given(instance=fUML_CompleteStructuredActivities_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_fuml_completestructuredactivities_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, fUML_CompleteStructuredActivities_StructuredActivityNode)



@given(instance=fUML_CompleteStructuredActivities_StructuredActivityNode_strategy)
def test_fuml_completestructuredactivities_structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

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

@given(instance=fUML_CompleteStructuredActivities_ConditionalNode_strategy)
@settings(max_examples=50)
def test_fuml_completestructuredactivities_conditionalnode_instantiation(instance):
    assert isinstance(instance, fUML_CompleteStructuredActivities_ConditionalNode)



@given(instance=fUML_CompleteStructuredActivities_ConditionalNode_strategy)
def test_fuml_completestructuredactivities_conditionalnode_determinate_setter(instance):
    original = instance.determinate
    instance.determinate = original
    assert instance.determinate == original



@given(instance=fUML_CompleteStructuredActivities_ConditionalNode_strategy)
def test_fuml_completestructuredactivities_conditionalnode_assured_setter(instance):
    original = instance.assured
    instance.assured = original
    assert instance.assured == original

@given(instance=fUML_ExtraStructuredActivities_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_fuml_extrastructuredactivities_expansionregion_instantiation(instance):
    assert isinstance(instance, fUML_ExtraStructuredActivities_ExpansionRegion)



@given(instance=fUML_ExtraStructuredActivities_ExpansionRegion_strategy)
def test_fuml_extrastructuredactivities_expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=fUML_CompleteStructuredActivities_LoopNode_strategy)
@settings(max_examples=50)
def test_fuml_completestructuredactivities_loopnode_instantiation(instance):
    assert isinstance(instance, fUML_CompleteStructuredActivities_LoopNode)



@given(instance=fUML_CompleteStructuredActivities_LoopNode_strategy)
def test_fuml_completestructuredactivities_loopnode_testedFirst_setter(instance):
    original = instance.testedFirst
    instance.testedFirst = original
    assert instance.testedFirst == original

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=fUML_ExtraStructuredActivities_ExpansionNode_strategy)
@settings(max_examples=50)
def test_fuml_extrastructuredactivities_expansionnode_instantiation(instance):
    assert isinstance(instance, fUML_ExtraStructuredActivities_ExpansionNode)

@given(instance=fUML_IntermediateActivities_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_activityparameternode_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_ActivityParameterNode)

@given(instance=CompleteStructuredActivities_Clause_strategy)
@settings(max_examples=50)
def test_completestructuredactivities_clause_instantiation(instance):
    assert isinstance(instance, CompleteStructuredActivities_Clause)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=fUML_CompleteStructuredActivities_ExecutableNode_strategy)
@settings(max_examples=50)
def test_fuml_completestructuredactivities_executablenode_instantiation(instance):
    assert isinstance(instance, fUML_CompleteStructuredActivities_ExecutableNode)

@given(instance=fUML_IntermediateActivities_ControlNode_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_controlnode_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_ControlNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=fUML_IntermediateActivities_ForkNode_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_forknode_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_ForkNode)

@given(instance=fUML_IntermediateActivities_InitialNode_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_initialnode_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_InitialNode)

@given(instance=fUML_IntermediateActivities_DecisionNode_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_decisionnode_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_DecisionNode)

@given(instance=fUML_IntermediateActivities_FinalNode_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_finalnode_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_FinalNode)

@given(instance=fUML_IntermediateActivities_JoinNode_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_joinnode_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_JoinNode)

@given(instance=fUML_IntermediateActivities_MergeNode_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_mergenode_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_MergeNode)

@given(instance=IntermediateActivities_ActivityEdge_strategy)
@settings(max_examples=50)
def test_intermediateactivities_activityedge_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_ActivityEdge)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=fUML_IntermediateActivities_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_activityfinalnode_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_ActivityFinalNode)

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

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=fUML_IntermediateActivities_ControlFlow_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_controlflow_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_ControlFlow)

@given(instance=fUML_IntermediateActivities_ObjectFlow_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_objectflow_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_ObjectFlow)

@given(instance=Communications_Reception_strategy)
@settings(max_examples=50)
def test_communications_reception_instantiation(instance):
    assert isinstance(instance, Communications_Reception)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=fUML_Kernel_Class_strategy)
@settings(max_examples=50)
def test_fuml_kernel_class_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Class)



@given(instance=fUML_Kernel_Class_strategy)
def test_fuml_kernel_class_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=Kernel_Enumeration_strategy)
@settings(max_examples=50)
def test_kernel_enumeration_instantiation(instance):
    assert isinstance(instance, Kernel_Enumeration)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=fUML_Kernel_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_fuml_kernel_enumerationliteral_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_EnumerationLiteral)

@given(instance=Kernel_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_kernel_enumerationliteral_instantiation(instance):
    assert isinstance(instance, Kernel_EnumerationLiteral)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=fUML_Kernel_LiteralInteger_strategy)
@settings(max_examples=50)
def test_fuml_kernel_literalinteger_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_LiteralInteger)



@given(instance=fUML_Kernel_LiteralInteger_strategy)
def test_fuml_kernel_literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fUML_Kernel_LiteralString_strategy)
@settings(max_examples=50)
def test_fuml_kernel_literalstring_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_LiteralString)



@given(instance=fUML_Kernel_LiteralString_strategy)
def test_fuml_kernel_literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fUML_Kernel_LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_fuml_kernel_literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_LiteralUnlimitedNatural)



@given(instance=fUML_Kernel_LiteralUnlimitedNatural_strategy)
def test_fuml_kernel_literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=fUML_Kernel_LiteralNull_strategy)
@settings(max_examples=50)
def test_fuml_kernel_literalnull_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_LiteralNull)

@given(instance=fUML_Kernel_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_fuml_kernel_literalboolean_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_LiteralBoolean)



@given(instance=fUML_Kernel_LiteralBoolean_strategy)
def test_fuml_kernel_literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=fUML_Kernel_LiteralSpecification_strategy)
@settings(max_examples=50)
def test_fuml_kernel_literalspecification_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_LiteralSpecification)

@given(instance=fUML_Kernel_InstanceValue_strategy)
@settings(max_examples=50)
def test_fuml_kernel_instancevalue_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_InstanceValue)

@given(instance=Kernel_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_kernel_instancespecification_instantiation(instance):
    assert isinstance(instance, Kernel_InstanceSpecification)

@given(instance=Kernel_StructuralFeature_strategy)
@settings(max_examples=50)
def test_kernel_structuralfeature_instantiation(instance):
    assert isinstance(instance, Kernel_StructuralFeature)

@given(instance=Kernel_Slot_strategy)
@settings(max_examples=50)
def test_kernel_slot_instantiation(instance):
    assert isinstance(instance, Kernel_Slot)

@given(instance=Kernel_Operation_strategy)
@settings(max_examples=50)
def test_kernel_operation_instantiation(instance):
    assert isinstance(instance, Kernel_Operation)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=fUML_Kernel_Enumeration_strategy)
@settings(max_examples=50)
def test_fuml_kernel_enumeration_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Enumeration)

@given(instance=fUML_Kernel_PrimitiveType_strategy)
@settings(max_examples=50)
def test_fuml_kernel_primitivetype_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_PrimitiveType)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=fUML_Kernel_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_fuml_kernel_behavioralfeature_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_BehavioralFeature)



@given(instance=fUML_Kernel_BehavioralFeature_strategy)
def test_fuml_kernel_behavioralfeature_concurrency_setter(instance):
    original = instance.concurrency
    instance.concurrency = original
    assert instance.concurrency == original



@given(instance=fUML_Kernel_BehavioralFeature_strategy)
def test_fuml_kernel_behavioralfeature_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=Kernel_ValueSpecification_strategy)
@settings(max_examples=50)
def test_kernel_valuespecification_instantiation(instance):
    assert isinstance(instance, Kernel_ValueSpecification)

@given(instance=Kernel_Class_strategy)
@settings(max_examples=50)
def test_kernel_class_instantiation(instance):
    assert isinstance(instance, Kernel_Class)

@given(instance=Kernel_DataType_strategy)
@settings(max_examples=50)
def test_kernel_datatype_instantiation(instance):
    assert isinstance(instance, Kernel_DataType)

@given(instance=Kernel_Association_strategy)
@settings(max_examples=50)
def test_kernel_association_instantiation(instance):
    assert isinstance(instance, Kernel_Association)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=fUML_Kernel_Property_strategy)
@settings(max_examples=50)
def test_fuml_kernel_property_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Property)



@given(instance=fUML_Kernel_Property_strategy)
def test_fuml_kernel_property_composite_setter(instance):
    original = instance.composite
    instance.composite = original
    assert instance.composite == original



@given(instance=fUML_Kernel_Property_strategy)
def test_fuml_kernel_property_derivedUnion_setter(instance):
    original = instance.derivedUnion
    instance.derivedUnion = original
    assert instance.derivedUnion == original



@given(instance=fUML_Kernel_Property_strategy)
def test_fuml_kernel_property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original



@given(instance=fUML_Kernel_Property_strategy)
def test_fuml_kernel_property_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=Kernel_Generalization_strategy)
@settings(max_examples=50)
def test_kernel_generalization_instantiation(instance):
    assert isinstance(instance, Kernel_Generalization)

@given(instance=Kernel_RedefinableElement_strategy)
@settings(max_examples=50)
def test_kernel_redefinableelement_instantiation(instance):
    assert isinstance(instance, Kernel_RedefinableElement)

@given(instance=Kernel_Classifier_strategy)
@settings(max_examples=50)
def test_kernel_classifier_instantiation(instance):
    assert isinstance(instance, Kernel_Classifier)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=fUML_IntermediateActivities_ActivityEdge_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_activityedge_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_ActivityEdge)

@given(instance=fUML_IntermediateActivities_ActivityNode_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_activitynode_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_ActivityNode)

@given(instance=fUML_Kernel_Feature_strategy)
@settings(max_examples=50)
def test_fuml_kernel_feature_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Feature)



@given(instance=fUML_Kernel_Feature_strategy)
def test_fuml_kernel_feature_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=Kernel_TypedElement_strategy)
@settings(max_examples=50)
def test_kernel_typedelement_instantiation(instance):
    assert isinstance(instance, Kernel_TypedElement)

@given(instance=fUML_IntermediateActivities_ObjectNode_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_objectnode_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_ObjectNode)

@given(instance=Kernel_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_kernel_multiplicityelement_instantiation(instance):
    assert isinstance(instance, Kernel_MultiplicityElement)

@given(instance=fUML_Kernel_Parameter_strategy)
@settings(max_examples=50)
def test_fuml_kernel_parameter_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Parameter)



@given(instance=fUML_Kernel_Parameter_strategy)
def test_fuml_kernel_parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=fUML_BasicActions_Pin_strategy)
@settings(max_examples=50)
def test_fuml_basicactions_pin_instantiation(instance):
    assert isinstance(instance, fUML_BasicActions_Pin)

@given(instance=Kernel_Feature_strategy)
@settings(max_examples=50)
def test_kernel_feature_instantiation(instance):
    assert isinstance(instance, Kernel_Feature)

@given(instance=fUML_Kernel_StructuralFeature_strategy)
@settings(max_examples=50)
def test_fuml_kernel_structuralfeature_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_StructuralFeature)



@given(instance=fUML_Kernel_StructuralFeature_strategy)
def test_fuml_kernel_structuralfeature_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=fUML_Kernel_Element_strategy)
@settings(max_examples=50)
def test_fuml_kernel_element_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Element)

@given(instance=Kernel_Package_strategy)
@settings(max_examples=50)
def test_kernel_package_instantiation(instance):
    assert isinstance(instance, Kernel_Package)

@given(instance=Kernel_PackageableElement_strategy)
@settings(max_examples=50)
def test_kernel_packageableelement_instantiation(instance):
    assert isinstance(instance, Kernel_PackageableElement)

@given(instance=Kernel_PackageImport_strategy)
@settings(max_examples=50)
def test_kernel_packageimport_instantiation(instance):
    assert isinstance(instance, Kernel_PackageImport)

@given(instance=Kernel_ElementImport_strategy)
@settings(max_examples=50)
def test_kernel_elementimport_instantiation(instance):
    assert isinstance(instance, Kernel_ElementImport)

@given(instance=Kernel_NamedElement_strategy)
@settings(max_examples=50)
def test_kernel_namedelement_instantiation(instance):
    assert isinstance(instance, Kernel_NamedElement)

@given(instance=fUML_Kernel_Comment_strategy)
@settings(max_examples=50)
def test_fuml_kernel_comment_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Comment)



@given(instance=fUML_Kernel_Comment_strategy)
def test_fuml_kernel_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Kernel_Comment_strategy)
@settings(max_examples=50)
def test_kernel_comment_instantiation(instance):
    assert isinstance(instance, Kernel_Comment)

@given(instance=Kernel_Element_strategy)
@settings(max_examples=50)
def test_kernel_element_instantiation(instance):
    assert isinstance(instance, Kernel_Element)

@given(instance=Kernel_Namespace_strategy)
@settings(max_examples=50)
def test_kernel_namespace_instantiation(instance):
    assert isinstance(instance, Kernel_Namespace)

@given(instance=fUML_Kernel_Package_strategy)
@settings(max_examples=50)
def test_fuml_kernel_package_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Package)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=fUML_Kernel_ElementImport_strategy)
@settings(max_examples=50)
def test_fuml_kernel_elementimport_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_ElementImport)



@given(instance=fUML_Kernel_ElementImport_strategy)
def test_fuml_kernel_elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=fUML_Kernel_ElementImport_strategy)
def test_fuml_kernel_elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=fUML_Kernel_PackageImport_strategy)
@settings(max_examples=50)
def test_fuml_kernel_packageimport_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_PackageImport)



@given(instance=fUML_Kernel_PackageImport_strategy)
def test_fuml_kernel_packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=fUML_Kernel_Generalization_strategy)
@settings(max_examples=50)
def test_fuml_kernel_generalization_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Generalization)



@given(instance=fUML_Kernel_Generalization_strategy)
def test_fuml_kernel_generalization_substitutable_setter(instance):
    original = instance.substitutable
    instance.substitutable = original
    assert instance.substitutable == original

@given(instance=fUML_CompleteStructuredActivities_Clause_strategy)
@settings(max_examples=50)
def test_fuml_completestructuredactivities_clause_instantiation(instance):
    assert isinstance(instance, fUML_CompleteStructuredActivities_Clause)

@given(instance=fUML_IntermediateActions_LinkEndData_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactions_linkenddata_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActions_LinkEndData)

@given(instance=fUML_Kernel_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_fuml_kernel_multiplicityelement_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_MultiplicityElement)



@given(instance=fUML_Kernel_MultiplicityElement_strategy)
def test_fuml_kernel_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=fUML_Kernel_MultiplicityElement_strategy)
def test_fuml_kernel_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=fUML_Kernel_MultiplicityElement_strategy)
def test_fuml_kernel_multiplicityelement_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original



@given(instance=fUML_Kernel_MultiplicityElement_strategy)
def test_fuml_kernel_multiplicityelement_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=fUML_Kernel_Slot_strategy)
@settings(max_examples=50)
def test_fuml_kernel_slot_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Slot)

@given(instance=fUML_Kernel_NamedElement_strategy)
@settings(max_examples=50)
def test_fuml_kernel_namedelement_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_NamedElement)



@given(instance=fUML_Kernel_NamedElement_strategy)
def test_fuml_kernel_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fUML_Kernel_NamedElement_strategy)
def test_fuml_kernel_namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=fUML_Kernel_NamedElement_strategy)
def test_fuml_kernel_namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

@given(instance=Kernel_Type_strategy)
@settings(max_examples=50)
def test_kernel_type_instantiation(instance):
    assert isinstance(instance, Kernel_Type)

@given(instance=fUML_Kernel_Classifier_strategy)
@settings(max_examples=50)
def test_fuml_kernel_classifier_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Classifier)



@given(instance=fUML_Kernel_Classifier_strategy)
def test_fuml_kernel_classifier_finalSpecialization_setter(instance):
    original = instance.finalSpecialization
    instance.finalSpecialization = original
    assert instance.finalSpecialization == original



@given(instance=fUML_Kernel_Classifier_strategy)
def test_fuml_kernel_classifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=fUML_Kernel_ValueSpecification_strategy)
@settings(max_examples=50)
def test_fuml_kernel_valuespecification_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_ValueSpecification)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=fUML_Kernel_Operation_strategy)
@settings(max_examples=50)
def test_fuml_kernel_operation_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Operation)



@given(instance=fUML_Kernel_Operation_strategy)
def test_fuml_kernel_operation_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=fUML_Kernel_Operation_strategy)
def test_fuml_kernel_operation_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original



@given(instance=fUML_Kernel_Operation_strategy)
def test_fuml_kernel_operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=fUML_Kernel_Operation_strategy)
def test_fuml_kernel_operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=fUML_Kernel_Operation_strategy)
def test_fuml_kernel_operation_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=fUML_Communications_Reception_strategy)
@settings(max_examples=50)
def test_fuml_communications_reception_instantiation(instance):
    assert isinstance(instance, fUML_Communications_Reception)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=fUML_Communications_MessageEvent_strategy)
@settings(max_examples=50)
def test_fuml_communications_messageevent_instantiation(instance):
    assert isinstance(instance, fUML_Communications_MessageEvent)

@given(instance=Communications_Signal_strategy)
@settings(max_examples=50)
def test_communications_signal_instantiation(instance):
    assert isinstance(instance, Communications_Signal)

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=fUML_Communications_SignalEvent_strategy)
@settings(max_examples=50)
def test_fuml_communications_signalevent_instantiation(instance):
    assert isinstance(instance, fUML_Communications_SignalEvent)

@given(instance=Kernel_Property_strategy)
@settings(max_examples=50)
def test_kernel_property_instantiation(instance):
    assert isinstance(instance, Kernel_Property)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=fUML_Kernel_Type_strategy)
@settings(max_examples=50)
def test_fuml_kernel_type_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Type)

@given(instance=fUML_Communications_Event_strategy)
@settings(max_examples=50)
def test_fuml_communications_event_instantiation(instance):
    assert isinstance(instance, fUML_Communications_Event)

@given(instance=Communications_Event_strategy)
@settings(max_examples=50)
def test_communications_event_instantiation(instance):
    assert isinstance(instance, Communications_Event)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fUML_Kernel_PackageableElement_strategy)
@settings(max_examples=50)
def test_fuml_kernel_packageableelement_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_PackageableElement)

@given(instance=fUML_Kernel_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_fuml_kernel_instancespecification_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_InstanceSpecification)

@given(instance=fUML_Kernel_TypedElement_strategy)
@settings(max_examples=50)
def test_fuml_kernel_typedelement_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_TypedElement)

@given(instance=fUML_Kernel_Namespace_strategy)
@settings(max_examples=50)
def test_fuml_kernel_namespace_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Namespace)

@given(instance=fUML_Kernel_RedefinableElement_strategy)
@settings(max_examples=50)
def test_fuml_kernel_redefinableelement_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_RedefinableElement)



@given(instance=fUML_Kernel_RedefinableElement_strategy)
def test_fuml_kernel_redefinableelement_leaf_setter(instance):
    original = instance.leaf
    instance.leaf = original
    assert instance.leaf == original

@given(instance=fUML_Communications_Trigger_strategy)
@settings(max_examples=50)
def test_fuml_communications_trigger_instantiation(instance):
    assert isinstance(instance, fUML_Communications_Trigger)

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=fUML_BasicBehaviors_FunctionBehavior_strategy)
@settings(max_examples=50)
def test_fuml_basicbehaviors_functionbehavior_instantiation(instance):
    assert isinstance(instance, fUML_BasicBehaviors_FunctionBehavior)

@given(instance=BasicBehaviors_Behavior_strategy)
@settings(max_examples=50)
def test_basicbehaviors_behavior_instantiation(instance):
    assert isinstance(instance, BasicBehaviors_Behavior)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=fUML_Communications_Signal_strategy)
@settings(max_examples=50)
def test_fuml_communications_signal_instantiation(instance):
    assert isinstance(instance, fUML_Communications_Signal)

@given(instance=fUML_Kernel_Association_strategy)
@settings(max_examples=50)
def test_fuml_kernel_association_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_Association)



@given(instance=fUML_Kernel_Association_strategy)
def test_fuml_kernel_association_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=fUML_Kernel_DataType_strategy)
@settings(max_examples=50)
def test_fuml_kernel_datatype_instantiation(instance):
    assert isinstance(instance, fUML_Kernel_DataType)

@given(instance=fUML_BasicBehaviors_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_fuml_basicbehaviors_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, fUML_BasicBehaviors_BehavioredClassifier)

@given(instance=BasicBehaviors_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_basicbehaviors_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BasicBehaviors_BehavioredClassifier)

@given(instance=Kernel_Parameter_strategy)
@settings(max_examples=50)
def test_kernel_parameter_instantiation(instance):
    assert isinstance(instance, Kernel_Parameter)

@given(instance=Kernel_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_kernel_behavioralfeature_instantiation(instance):
    assert isinstance(instance, Kernel_BehavioralFeature)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=fUML_BasicBehaviors_Behavior_strategy)
@settings(max_examples=50)
def test_fuml_basicbehaviors_behavior_instantiation(instance):
    assert isinstance(instance, fUML_BasicBehaviors_Behavior)



@given(instance=fUML_BasicBehaviors_Behavior_strategy)
def test_fuml_basicbehaviors_behavior_reentrant_setter(instance):
    original = instance.reentrant
    instance.reentrant = original
    assert instance.reentrant == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=fUML_IntermediateActivities_Activity_strategy)
@settings(max_examples=50)
def test_fuml_intermediateactivities_activity_instantiation(instance):
    assert isinstance(instance, fUML_IntermediateActivities_Activity)



@given(instance=fUML_IntermediateActivities_Activity_strategy)
def test_fuml_intermediateactivities_activity_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=fUML_BasicBehaviors_OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_fuml_basicbehaviors_opaquebehavior_instantiation(instance):
    assert isinstance(instance, fUML_BasicBehaviors_OpaqueBehavior)



@given(instance=fUML_BasicBehaviors_OpaqueBehavior_strategy)
def test_fuml_basicbehaviors_opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=fUML_BasicBehaviors_OpaqueBehavior_strategy)
def test_fuml_basicbehaviors_opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original
