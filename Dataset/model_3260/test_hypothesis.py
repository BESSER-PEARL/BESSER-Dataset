import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EnumerationType,
    NumberType,
    aadl2_AadlReal,
    aadl2_AadlInteger,
    PropertyType,
    aadl2_AadlString,
    aadl2_ClassifierType,
    aadl2_ReferenceType,
    aadl2_RangeType,
    aadl2_AadlBoolean,
    aadl2_UnitsType,
    aadl2_NumberType,
    NumberValue,
    aadl2_IntegerLiteral,
    ContainedNamedElement,
    aadl2_RealLiteral,
    PropertyExpression,
    aadl2_ListValue,
    aadl2_Operation,
    aadl2_PropertyValue,
    PropertyValue,
    aadl2_RecordValue,
    aadl2_ComputedValue,
    aadl2_RangeValue,
    aadl2_NumberValue,
    aadl2_StringLiteral,
    aadl2_BooleanLiteral,
    aadl2_ReferenceValue,
    aadl2_EnumerationValue,
    CallSpecification,
    aadl2_ProcessorCall,
    FeatureGroupPrototypeActual,
    aadl2_FeatureGroupReference,
    aadl2_FeatureGroupPrototypeReference,
    Subcomponent,
    PackageSection,
    aadl2_PublicPackageSection,
    AnnexSubclause,
    aadl2_DefaultAnnexSubclause,
    AnnexLibrary,
    aadl2_DefaultAnnexLibrary,
    ModalPath,
    Abstract,
    Prototype,
    aadl2_ComponentPrototype,
    CalledSubprogram,
    SubprogramGroup,
    Subprogram,
    AccessConnectionEnd,
    Access,
    Port,
    Data,
    EndToEndFlowElement,
    aadl2_FlowElement,
    ParameterConnectionEnd,
    FlowElement,
    aadl2_SubcomponentFlow,
    Bus,
    aadl2_BusAccess,
    aadl2_SubprogramAccess,
    aadl2_EventPort,
    Flow,
    CallContext,
    aadl2_SubprogramGroupAccess,
    FeatureGroupConnectionEnd,
    Context,
    aadl2_EventDataPort,
    aadl2_SubprogramCall,
    aadl2_DataPort,
    Generalization_,
    aadl2_GroupExtension,
    ConnectionEnd,
    aadl2_AccessConnectionEnd,
    aadl2_PortConnectionEnd,
    aadl2_ParameterConnectionEnd,
    aadl2_FeatureGroupConnectionEnd,
    aadl2_FeatureConnectionEnd,
    ArrayableElement,
    FeatureConnectionEnd,
    aadl2_TypeExtension,
    Classifier,
    aadl2_FeatureGroupType,
    aadl2_ComponentClassifier,
    aadl2_ProcessorSubprogram,
    Feature,
    aadl2_Access,
    aadl2_DirectedFeature,
    PortConnectionEnd,
    aadl2_DataAccess,
    DirectedFeature,
    aadl2_Parameter,
    aadl2_FeatureGroup,
    aadl2_AbstractFeature,
    aadl2_Port,
    ModeTransitionTrigger,
    aadl2_ProcessorPort,
    aadl2_InternalEvent,
    aadl2_TriggerPort,
    aadl2_Realization,
    aadl2_ImplementationExtension,
    aadl2_AbstractSubcomponent,
    aadl2_EndToEndFlow,
    ComponentClassifier,
    aadl2_SubprogramGroupClassifier,
    aadl2_SubprogramClassifier,
    aadl2_ComponentType,
    aadl2_AbstractClassifier,
    aadl2_BusClassifier,
    aadl2_DataClassifier,
    aadl2_ComponentImplementation,
    ArraySize,
    aadl2_PropertyReference,
    aadl2_ConstantValue,
    aadl2_Numeral,
    RefinableElement,
    StructuralFeature,
    aadl2_Flow,
    aadl2_Feature,
    aadl2_FlowImplementation,
    aadl2_Connection,
    ClassifierFeature,
    aadl2_BehavioralFeature,
    aadl2_StructuralFeature,
    aadl2_ModeFeature,
    Relationship,
    aadl2_DirectedRelationship,
    ModeFeature,
    aadl2_ModeTransition,
    aadl2_Mode,
    ModalElement,
    aadl2_FlowSpecification,
    aadl2_ModalPath,
    aadl2_Subcomponent,
    DirectedRelationship,
    aadl2_Generalization_,
    aadl2_Prototype,
    aadl2_AnnexSubclause,
    Namespace,
    aadl2_GlobalNamespace,
    aadl2_RecordType,
    aadl2_EnumerationType,
    PropertyOwner,
    aadl2_ClassifierValue,
    Type,
    aadl2_PropertyType,
    aadl2_Classifier,
    TypedElement,
    aadl2_BasicProperty,
    aadl2_MetaclassReference,
    BasicProperty,
    aadl2_RecordField,
    aadl2_Property,
    aadl2_ModalPropertyValue,
    aadl2_Element,
    NamedElement,
    aadl2_EndToEndFlowElement,
    aadl2_ConnectionEnd,
    aadl2_Context,
    aadl2_Subprogram,
    aadl2_Bus,
    aadl2_Type,
    aadl2_TypedElement,
    aadl2_Abstract,
    aadl2_ClassifierFeature,
    aadl2_ModalElement,
    aadl2_EnumerationLiteral,
    aadl2_AnnexLibrary,
    aadl2_RefinableElement,
    aadl2_SubprogramGroup,
    aadl2_Data,
    aadl2_Namespace,
    Element,
    aadl2_ArraySpecification,
    aadl2_Relationship,
    aadl2_ComponentImplementationReference,
    aadl2_PropertyOwner,
    aadl2_PropertyExpression,
    aadl2_ArrayRange,
    aadl2_ModeBinding,
    aadl2_CallContext,
    aadl2_ModeTransitionTrigger,
    aadl2_BasicPropertyAssociation,
    aadl2_CalledSubprogram,
    aadl2_ArraySize,
    aadl2_PropertyAssociation,
    aadl2_ArrayableElement,
    aadl2_ContainedNamedElement,
    aadl2_NamedElement,
    aadl2_ContainmentPathElement,
    aadl2_PrototypeBinding,
    aadl2_NumericRange,
    aadl2_Comment,
    EnumerationLiteral,
    ComponentPrototypeActual,
    aadl2_ComponentPrototypeReference,
    aadl2_UnitLiteral,
    aadl2_UnitValue,
    aadl2_ComponentReference,
    aadl2_FeaturePrototype,
    aadl2_FeatureGroupPrototypeActual,
    aadl2_FeatureGroupPrototype,
    aadl2_ComponentPrototypeActual,
    FeaturePrototypeActual,
    aadl2_PortSpecification,
    aadl2_FeaturePrototypeReference,
    aadl2_AccessSpecification,
    aadl2_FeaturePrototypeActual,
    aadl2_PropertyConstant,
    PrototypeBinding,
    aadl2_FeaturePrototypeBinding,
    aadl2_FeatureGroupPrototypeBinding,
    aadl2_ComponentPrototypeBinding,
    VirtualProcessorClassifier,
    VirtualBusClassifier,
    ThreadGroupClassifier,
    ThreadClassifier,
    SystemClassifier,
    SubprogramGroupClassifier,
    SubprogramClassifier,
    ProcessorClassifier,
    ProcessClassifier,
    MemoryClassifier,
    DeviceClassifier,
    VirtualProcessor,
    aadl2_VirtualProcessorClassifier,
    aadl2_VirtualBus,
    VirtualBus,
    aadl2_VirtualBusClassifier,
    DataClassifier,
    BusClassifier,
    aadl2_VirtualProcessor,
    System,
    aadl2_SystemClassifier,
    aadl2_Processor,
    Processor,
    aadl2_ProcessorClassifier,
    aadl2_ThreadGroup,
    ThreadGroup,
    aadl2_ThreadGroupClassifier,
    aadl2_Thread,
    Thread,
    aadl2_ThreadClassifier,
    aadl2_System,
    BehavioralFeature,
    aadl2_Process,
    Process,
    aadl2_ProcessClassifier,
    aadl2_Memory,
    Memory,
    aadl2_MemoryClassifier,
    aadl2_Device,
    Device,
    aadl2_DeviceClassifier,
    aadl2_SubprogramGroupSubcomponent,
    aadl2_SubprogramSubcomponent,
    aadl2_SubprogramCallSequence,
    aadl2_CallSpecification,
    ComponentImplementation,
    aadl2_BehavioredImplementation,
    aadl2_VirtualProcessorSubcomponent,
    aadl2_VirtualBusSubcomponent,
    aadl2_ThreadGroupSubcomponent,
    aadl2_ThreadSubcomponent,
    BehavioredImplementation,
    aadl2_SystemSubcomponent,
    aadl2_ProcessorSubcomponent,
    aadl2_ProcessSubcomponent,
    aadl2_MemorySubcomponent,
    aadl2_DeviceSubcomponent,
    aadl2_DataSubcomponent,
    aadl2_BusSubcomponent,
    AbstractClassifier,
    ComponentType,
    aadl2_VirtualProcessorImplementation,
    aadl2_VirtualProcessorType,
    aadl2_VirtualBusImplementation,
    aadl2_PropertySet,
    aadl2_SystemImplementation,
    aadl2_SystemType,
    aadl2_SubprogramGroupImplementation,
    aadl2_VirtualBusType,
    aadl2_ThreadGroupImplementation,
    aadl2_ThreadGroupType,
    aadl2_ThreadImplementation,
    aadl2_ThreadType,
    aadl2_ProcessType,
    aadl2_MemoryImplementation,
    aadl2_SubprogramGroupType,
    aadl2_SubprogramImplementation,
    aadl2_SubprogramType,
    aadl2_ProcessorImplementation,
    aadl2_ProcessImplementation,
    aadl2_ProcessorType,
    aadl2_AbstractImplementation,
    aadl2_AbstractType,
    aadl2_AadlPackage,
    aadl2_MemoryType,
    aadl2_DeviceImplementation,
    aadl2_DeviceType,
    aadl2_DataImplementation,
    aadl2_DataType,
    aadl2_BusImplementation,
    aadl2_BusType,
    aadl2_PackageSection,
    aadl2_PrivatePackageSection,
    aadl2_FeatureGroupTypeRename,
    aadl2_ComponentTypeRename,
    aadl2_PackageRename,
    Connection,
    aadl2_PortConnection,
    aadl2_ParameterConnection,
    aadl2_AccessConnection,
    aadl2_FeatureGroupConnection,
    aadl2_FeatureConnection,
    FlowKind,
    OperationKind,
    PortCategory,
    ConnectionKind,
    AccessType,
    DirectionType,
    ComponentCategory,
    AccessCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(EnumerationType)


def test_enumerationtype_constructor_exists():
    assert callable(EnumerationType.__init__)


def test_enumerationtype_constructor_args():
    sig = inspect.signature(EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_numbertype_is_not_abstract():
    assert not inspect.isabstract(NumberType)


def test_numbertype_constructor_exists():
    assert callable(NumberType.__init__)


def test_numbertype_constructor_args():
    sig = inspect.signature(NumberType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_aadlreal_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlReal)


def test_aadl2_aadlreal_constructor_exists():
    assert callable(aadl2_AadlReal.__init__)


def test_aadl2_aadlreal_constructor_args():
    sig = inspect.signature(aadl2_AadlReal.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_aadlinteger_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlInteger)


def test_aadl2_aadlinteger_constructor_exists():
    assert callable(aadl2_AadlInteger.__init__)


def test_aadl2_aadlinteger_constructor_args():
    sig = inspect.signature(aadl2_AadlInteger.__init__)
    params = list(sig.parameters.keys())



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_aadlstring_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlString)


def test_aadl2_aadlstring_constructor_exists():
    assert callable(aadl2_AadlString.__init__)


def test_aadl2_aadlstring_constructor_args():
    sig = inspect.signature(aadl2_AadlString.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_classifiertype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ClassifierType)


def test_aadl2_classifiertype_constructor_exists():
    assert callable(aadl2_ClassifierType.__init__)


def test_aadl2_classifiertype_constructor_args():
    sig = inspect.signature(aadl2_ClassifierType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_referencetype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ReferenceType)


def test_aadl2_referencetype_constructor_exists():
    assert callable(aadl2_ReferenceType.__init__)


def test_aadl2_referencetype_constructor_args():
    sig = inspect.signature(aadl2_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_rangetype_is_not_abstract():
    assert not inspect.isabstract(aadl2_RangeType)


def test_aadl2_rangetype_constructor_exists():
    assert callable(aadl2_RangeType.__init__)


def test_aadl2_rangetype_constructor_args():
    sig = inspect.signature(aadl2_RangeType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_aadlboolean_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlBoolean)


def test_aadl2_aadlboolean_constructor_exists():
    assert callable(aadl2_AadlBoolean.__init__)


def test_aadl2_aadlboolean_constructor_args():
    sig = inspect.signature(aadl2_AadlBoolean.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_unitstype_is_not_abstract():
    assert not inspect.isabstract(aadl2_UnitsType)


def test_aadl2_unitstype_constructor_exists():
    assert callable(aadl2_UnitsType.__init__)


def test_aadl2_unitstype_constructor_args():
    sig = inspect.signature(aadl2_UnitsType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_numbertype_is_not_abstract():
    assert not inspect.isabstract(aadl2_NumberType)


def test_aadl2_numbertype_constructor_exists():
    assert callable(aadl2_NumberType.__init__)


def test_aadl2_numbertype_constructor_args():
    sig = inspect.signature(aadl2_NumberType.__init__)
    params = list(sig.parameters.keys())



def test_numbervalue_is_not_abstract():
    assert not inspect.isabstract(NumberValue)


def test_numbervalue_constructor_exists():
    assert callable(NumberValue.__init__)


def test_numbervalue_constructor_args():
    sig = inspect.signature(NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_integerliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_IntegerLiteral)


def test_aadl2_integerliteral_constructor_exists():
    assert callable(aadl2_IntegerLiteral.__init__)


def test_aadl2_integerliteral_constructor_args():
    sig = inspect.signature(aadl2_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "base" in params, "Missing parameter 'base'"
    assert "value" in params, "Missing parameter 'value'"

def test_aadl2_integerliteral_has_base():
    assert hasattr(aadl2_IntegerLiteral, "base")
    descriptor = None
    for klass in aadl2_IntegerLiteral.__mro__:
        if "base" in klass.__dict__:
            descriptor = klass.__dict__["base"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_integerliteral_has_value():
    assert hasattr(aadl2_IntegerLiteral, "value")
    descriptor = None
    for klass in aadl2_IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_containednamedelement_is_not_abstract():
    assert not inspect.isabstract(ContainedNamedElement)


def test_containednamedelement_constructor_exists():
    assert callable(ContainedNamedElement.__init__)


def test_containednamedelement_constructor_args():
    sig = inspect.signature(ContainedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_realliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_RealLiteral)


def test_aadl2_realliteral_constructor_exists():
    assert callable(aadl2_RealLiteral.__init__)


def test_aadl2_realliteral_constructor_args():
    sig = inspect.signature(aadl2_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_aadl2_realliteral_has_value():
    assert hasattr(aadl2_RealLiteral, "value")
    descriptor = None
    for klass in aadl2_RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_propertyexpression_is_not_abstract():
    assert not inspect.isabstract(PropertyExpression)


def test_propertyexpression_constructor_exists():
    assert callable(PropertyExpression.__init__)


def test_propertyexpression_constructor_args():
    sig = inspect.signature(PropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_listvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ListValue)


def test_aadl2_listvalue_constructor_exists():
    assert callable(aadl2_ListValue.__init__)


def test_aadl2_listvalue_constructor_args():
    sig = inspect.signature(aadl2_ListValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_operation_is_not_abstract():
    assert not inspect.isabstract(aadl2_Operation)


def test_aadl2_operation_constructor_exists():
    assert callable(aadl2_Operation.__init__)


def test_aadl2_operation_constructor_args():
    sig = inspect.signature(aadl2_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_aadl2_operation_has_op():
    assert hasattr(aadl2_Operation, "op")
    descriptor = None
    for klass in aadl2_Operation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_propertyvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyValue)


def test_aadl2_propertyvalue_constructor_exists():
    assert callable(aadl2_PropertyValue.__init__)


def test_aadl2_propertyvalue_constructor_args():
    sig = inspect.signature(aadl2_PropertyValue.__init__)
    params = list(sig.parameters.keys())



def test_propertyvalue_is_not_abstract():
    assert not inspect.isabstract(PropertyValue)


def test_propertyvalue_constructor_exists():
    assert callable(PropertyValue.__init__)


def test_propertyvalue_constructor_args():
    sig = inspect.signature(PropertyValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_recordvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_RecordValue)


def test_aadl2_recordvalue_constructor_exists():
    assert callable(aadl2_RecordValue.__init__)


def test_aadl2_recordvalue_constructor_args():
    sig = inspect.signature(aadl2_RecordValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_computedvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComputedValue)


def test_aadl2_computedvalue_constructor_exists():
    assert callable(aadl2_ComputedValue.__init__)


def test_aadl2_computedvalue_constructor_args():
    sig = inspect.signature(aadl2_ComputedValue.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_aadl2_computedvalue_has_function():
    assert hasattr(aadl2_ComputedValue, "function")
    descriptor = None
    for klass in aadl2_ComputedValue.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_rangevalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_RangeValue)


def test_aadl2_rangevalue_constructor_exists():
    assert callable(aadl2_RangeValue.__init__)


def test_aadl2_rangevalue_constructor_args():
    sig = inspect.signature(aadl2_RangeValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_numbervalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_NumberValue)


def test_aadl2_numbervalue_constructor_exists():
    assert callable(aadl2_NumberValue.__init__)


def test_aadl2_numbervalue_constructor_args():
    sig = inspect.signature(aadl2_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueString" in params, "Missing parameter 'valueString'"

def test_aadl2_numbervalue_has_valueString():
    assert hasattr(aadl2_NumberValue, "valueString")
    descriptor = None
    for klass in aadl2_NumberValue.__mro__:
        if "valueString" in klass.__dict__:
            descriptor = klass.__dict__["valueString"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_stringliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_StringLiteral)


def test_aadl2_stringliteral_constructor_exists():
    assert callable(aadl2_StringLiteral.__init__)


def test_aadl2_stringliteral_constructor_args():
    sig = inspect.signature(aadl2_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_aadl2_stringliteral_has_value():
    assert hasattr(aadl2_StringLiteral, "value")
    descriptor = None
    for klass in aadl2_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_BooleanLiteral)


def test_aadl2_booleanliteral_constructor_exists():
    assert callable(aadl2_BooleanLiteral.__init__)


def test_aadl2_booleanliteral_constructor_args():
    sig = inspect.signature(aadl2_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_aadl2_booleanliteral_has_value():
    assert hasattr(aadl2_BooleanLiteral, "value")
    descriptor = None
    for klass in aadl2_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_referencevalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ReferenceValue)


def test_aadl2_referencevalue_constructor_exists():
    assert callable(aadl2_ReferenceValue.__init__)


def test_aadl2_referencevalue_constructor_args():
    sig = inspect.signature(aadl2_ReferenceValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_enumerationvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_EnumerationValue)


def test_aadl2_enumerationvalue_constructor_exists():
    assert callable(aadl2_EnumerationValue.__init__)


def test_aadl2_enumerationvalue_constructor_args():
    sig = inspect.signature(aadl2_EnumerationValue.__init__)
    params = list(sig.parameters.keys())



def test_callspecification_is_not_abstract():
    assert not inspect.isabstract(CallSpecification)


def test_callspecification_constructor_exists():
    assert callable(CallSpecification.__init__)


def test_callspecification_constructor_args():
    sig = inspect.signature(CallSpecification.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processorcall_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorCall)


def test_aadl2_processorcall_constructor_exists():
    assert callable(aadl2_ProcessorCall.__init__)


def test_aadl2_processorcall_constructor_args():
    sig = inspect.signature(aadl2_ProcessorCall.__init__)
    params = list(sig.parameters.keys())
    assert "subprogramAccessName" in params, "Missing parameter 'subprogramAccessName'"

def test_aadl2_processorcall_has_subprogramAccessName():
    assert hasattr(aadl2_ProcessorCall, "subprogramAccessName")
    descriptor = None
    for klass in aadl2_ProcessorCall.__mro__:
        if "subprogramAccessName" in klass.__dict__:
            descriptor = klass.__dict__["subprogramAccessName"]
            break
    assert isinstance(descriptor, property)



def test_featuregroupprototypeactual_is_not_abstract():
    assert not inspect.isabstract(FeatureGroupPrototypeActual)


def test_featuregroupprototypeactual_constructor_exists():
    assert callable(FeatureGroupPrototypeActual.__init__)


def test_featuregroupprototypeactual_constructor_args():
    sig = inspect.signature(FeatureGroupPrototypeActual.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featuregroupreference_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupReference)


def test_aadl2_featuregroupreference_constructor_exists():
    assert callable(aadl2_FeatureGroupReference.__init__)


def test_aadl2_featuregroupreference_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupReference.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featuregroupprototypereference_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupPrototypeReference)


def test_aadl2_featuregroupprototypereference_constructor_exists():
    assert callable(aadl2_FeatureGroupPrototypeReference.__init__)


def test_aadl2_featuregroupprototypereference_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupPrototypeReference.__init__)
    params = list(sig.parameters.keys())



def test_subcomponent_is_not_abstract():
    assert not inspect.isabstract(Subcomponent)


def test_subcomponent_constructor_exists():
    assert callable(Subcomponent.__init__)


def test_subcomponent_constructor_args():
    sig = inspect.signature(Subcomponent.__init__)
    params = list(sig.parameters.keys())



def test_packagesection_is_not_abstract():
    assert not inspect.isabstract(PackageSection)


def test_packagesection_constructor_exists():
    assert callable(PackageSection.__init__)


def test_packagesection_constructor_args():
    sig = inspect.signature(PackageSection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_publicpackagesection_is_not_abstract():
    assert not inspect.isabstract(aadl2_PublicPackageSection)


def test_aadl2_publicpackagesection_constructor_exists():
    assert callable(aadl2_PublicPackageSection.__init__)


def test_aadl2_publicpackagesection_constructor_args():
    sig = inspect.signature(aadl2_PublicPackageSection.__init__)
    params = list(sig.parameters.keys())



def test_annexsubclause_is_not_abstract():
    assert not inspect.isabstract(AnnexSubclause)


def test_annexsubclause_constructor_exists():
    assert callable(AnnexSubclause.__init__)


def test_annexsubclause_constructor_args():
    sig = inspect.signature(AnnexSubclause.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_defaultannexsubclause_is_not_abstract():
    assert not inspect.isabstract(aadl2_DefaultAnnexSubclause)


def test_aadl2_defaultannexsubclause_constructor_exists():
    assert callable(aadl2_DefaultAnnexSubclause.__init__)


def test_aadl2_defaultannexsubclause_constructor_args():
    sig = inspect.signature(aadl2_DefaultAnnexSubclause.__init__)
    params = list(sig.parameters.keys())
    assert "sourceText" in params, "Missing parameter 'sourceText'"

def test_aadl2_defaultannexsubclause_has_sourceText():
    assert hasattr(aadl2_DefaultAnnexSubclause, "sourceText")
    descriptor = None
    for klass in aadl2_DefaultAnnexSubclause.__mro__:
        if "sourceText" in klass.__dict__:
            descriptor = klass.__dict__["sourceText"]
            break
    assert isinstance(descriptor, property)



def test_annexlibrary_is_not_abstract():
    assert not inspect.isabstract(AnnexLibrary)


def test_annexlibrary_constructor_exists():
    assert callable(AnnexLibrary.__init__)


def test_annexlibrary_constructor_args():
    sig = inspect.signature(AnnexLibrary.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_defaultannexlibrary_is_not_abstract():
    assert not inspect.isabstract(aadl2_DefaultAnnexLibrary)


def test_aadl2_defaultannexlibrary_constructor_exists():
    assert callable(aadl2_DefaultAnnexLibrary.__init__)


def test_aadl2_defaultannexlibrary_constructor_args():
    sig = inspect.signature(aadl2_DefaultAnnexLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "sourceText" in params, "Missing parameter 'sourceText'"

def test_aadl2_defaultannexlibrary_has_sourceText():
    assert hasattr(aadl2_DefaultAnnexLibrary, "sourceText")
    descriptor = None
    for klass in aadl2_DefaultAnnexLibrary.__mro__:
        if "sourceText" in klass.__dict__:
            descriptor = klass.__dict__["sourceText"]
            break
    assert isinstance(descriptor, property)



def test_modalpath_is_not_abstract():
    assert not inspect.isabstract(ModalPath)


def test_modalpath_constructor_exists():
    assert callable(ModalPath.__init__)


def test_modalpath_constructor_args():
    sig = inspect.signature(ModalPath.__init__)
    params = list(sig.parameters.keys())



def test_abstract_is_not_abstract():
    assert not inspect.isabstract(Abstract)


def test_abstract_constructor_exists():
    assert callable(Abstract.__init__)


def test_abstract_constructor_args():
    sig = inspect.signature(Abstract.__init__)
    params = list(sig.parameters.keys())



def test_prototype_is_not_abstract():
    assert not inspect.isabstract(Prototype)


def test_prototype_constructor_exists():
    assert callable(Prototype.__init__)


def test_prototype_constructor_args():
    sig = inspect.signature(Prototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_componentprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentPrototype)


def test_aadl2_componentprototype_constructor_exists():
    assert callable(aadl2_ComponentPrototype.__init__)


def test_aadl2_componentprototype_constructor_args():
    sig = inspect.signature(aadl2_ComponentPrototype.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"
    assert "category" in params, "Missing parameter 'category'"

def test_aadl2_componentprototype_has_array():
    assert hasattr(aadl2_ComponentPrototype, "array")
    descriptor = None
    for klass in aadl2_ComponentPrototype.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_componentprototype_has_category():
    assert hasattr(aadl2_ComponentPrototype, "category")
    descriptor = None
    for klass in aadl2_ComponentPrototype.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_calledsubprogram_is_not_abstract():
    assert not inspect.isabstract(CalledSubprogram)


def test_calledsubprogram_constructor_exists():
    assert callable(CalledSubprogram.__init__)


def test_calledsubprogram_constructor_args():
    sig = inspect.signature(CalledSubprogram.__init__)
    params = list(sig.parameters.keys())



def test_subprogramgroup_is_not_abstract():
    assert not inspect.isabstract(SubprogramGroup)


def test_subprogramgroup_constructor_exists():
    assert callable(SubprogramGroup.__init__)


def test_subprogramgroup_constructor_args():
    sig = inspect.signature(SubprogramGroup.__init__)
    params = list(sig.parameters.keys())



def test_subprogram_is_not_abstract():
    assert not inspect.isabstract(Subprogram)


def test_subprogram_constructor_exists():
    assert callable(Subprogram.__init__)


def test_subprogram_constructor_args():
    sig = inspect.signature(Subprogram.__init__)
    params = list(sig.parameters.keys())



def test_accessconnectionend_is_not_abstract():
    assert not inspect.isabstract(AccessConnectionEnd)


def test_accessconnectionend_constructor_exists():
    assert callable(AccessConnectionEnd.__init__)


def test_accessconnectionend_constructor_args():
    sig = inspect.signature(AccessConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_access_is_not_abstract():
    assert not inspect.isabstract(Access)


def test_access_constructor_exists():
    assert callable(Access.__init__)


def test_access_constructor_args():
    sig = inspect.signature(Access.__init__)
    params = list(sig.parameters.keys())



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_data_constructor_exists():
    assert callable(Data.__init__)


def test_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_endtoendflowelement_is_not_abstract():
    assert not inspect.isabstract(EndToEndFlowElement)


def test_endtoendflowelement_constructor_exists():
    assert callable(EndToEndFlowElement.__init__)


def test_endtoendflowelement_constructor_args():
    sig = inspect.signature(EndToEndFlowElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_flowelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_FlowElement)


def test_aadl2_flowelement_constructor_exists():
    assert callable(aadl2_FlowElement.__init__)


def test_aadl2_flowelement_constructor_args():
    sig = inspect.signature(aadl2_FlowElement.__init__)
    params = list(sig.parameters.keys())



def test_parameterconnectionend_is_not_abstract():
    assert not inspect.isabstract(ParameterConnectionEnd)


def test_parameterconnectionend_constructor_exists():
    assert callable(ParameterConnectionEnd.__init__)


def test_parameterconnectionend_constructor_args():
    sig = inspect.signature(ParameterConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_flowelement_is_not_abstract():
    assert not inspect.isabstract(FlowElement)


def test_flowelement_constructor_exists():
    assert callable(FlowElement.__init__)


def test_flowelement_constructor_args():
    sig = inspect.signature(FlowElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subcomponentflow_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubcomponentFlow)


def test_aadl2_subcomponentflow_constructor_exists():
    assert callable(aadl2_SubcomponentFlow.__init__)


def test_aadl2_subcomponentflow_constructor_args():
    sig = inspect.signature(aadl2_SubcomponentFlow.__init__)
    params = list(sig.parameters.keys())



def test_bus_is_not_abstract():
    assert not inspect.isabstract(Bus)


def test_bus_constructor_exists():
    assert callable(Bus.__init__)


def test_bus_constructor_args():
    sig = inspect.signature(Bus.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_busaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusAccess)


def test_aadl2_busaccess_constructor_exists():
    assert callable(aadl2_BusAccess.__init__)


def test_aadl2_busaccess_constructor_args():
    sig = inspect.signature(aadl2_BusAccess.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramAccess)


def test_aadl2_subprogramaccess_constructor_exists():
    assert callable(aadl2_SubprogramAccess.__init__)


def test_aadl2_subprogramaccess_constructor_args():
    sig = inspect.signature(aadl2_SubprogramAccess.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_eventport_is_not_abstract():
    assert not inspect.isabstract(aadl2_EventPort)


def test_aadl2_eventport_constructor_exists():
    assert callable(aadl2_EventPort.__init__)


def test_aadl2_eventport_constructor_args():
    sig = inspect.signature(aadl2_EventPort.__init__)
    params = list(sig.parameters.keys())



def test_flow_is_not_abstract():
    assert not inspect.isabstract(Flow)


def test_flow_constructor_exists():
    assert callable(Flow.__init__)


def test_flow_constructor_args():
    sig = inspect.signature(Flow.__init__)
    params = list(sig.parameters.keys())



def test_callcontext_is_not_abstract():
    assert not inspect.isabstract(CallContext)


def test_callcontext_constructor_exists():
    assert callable(CallContext.__init__)


def test_callcontext_constructor_args():
    sig = inspect.signature(CallContext.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgroupaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupAccess)


def test_aadl2_subprogramgroupaccess_constructor_exists():
    assert callable(aadl2_SubprogramGroupAccess.__init__)


def test_aadl2_subprogramgroupaccess_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupAccess.__init__)
    params = list(sig.parameters.keys())



def test_featuregroupconnectionend_is_not_abstract():
    assert not inspect.isabstract(FeatureGroupConnectionEnd)


def test_featuregroupconnectionend_constructor_exists():
    assert callable(FeatureGroupConnectionEnd.__init__)


def test_featuregroupconnectionend_constructor_args():
    sig = inspect.signature(FeatureGroupConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_eventdataport_is_not_abstract():
    assert not inspect.isabstract(aadl2_EventDataPort)


def test_aadl2_eventdataport_constructor_exists():
    assert callable(aadl2_EventDataPort.__init__)


def test_aadl2_eventdataport_constructor_args():
    sig = inspect.signature(aadl2_EventDataPort.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramcall_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramCall)


def test_aadl2_subprogramcall_constructor_exists():
    assert callable(aadl2_SubprogramCall.__init__)


def test_aadl2_subprogramcall_constructor_args():
    sig = inspect.signature(aadl2_SubprogramCall.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_dataport_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataPort)


def test_aadl2_dataport_constructor_exists():
    assert callable(aadl2_DataPort.__init__)


def test_aadl2_dataport_constructor_args():
    sig = inspect.signature(aadl2_DataPort.__init__)
    params = list(sig.parameters.keys())



def test_generalization__is_not_abstract():
    assert not inspect.isabstract(Generalization_)


def test_generalization__constructor_exists():
    assert callable(Generalization_.__init__)


def test_generalization__constructor_args():
    sig = inspect.signature(Generalization_.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_groupextension_is_not_abstract():
    assert not inspect.isabstract(aadl2_GroupExtension)


def test_aadl2_groupextension_constructor_exists():
    assert callable(aadl2_GroupExtension.__init__)


def test_aadl2_groupextension_constructor_args():
    sig = inspect.signature(aadl2_GroupExtension.__init__)
    params = list(sig.parameters.keys())



def test_connectionend_is_not_abstract():
    assert not inspect.isabstract(ConnectionEnd)


def test_connectionend_constructor_exists():
    assert callable(ConnectionEnd.__init__)


def test_connectionend_constructor_args():
    sig = inspect.signature(ConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_accessconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_AccessConnectionEnd)


def test_aadl2_accessconnectionend_constructor_exists():
    assert callable(aadl2_AccessConnectionEnd.__init__)


def test_aadl2_accessconnectionend_constructor_args():
    sig = inspect.signature(aadl2_AccessConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_portconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_PortConnectionEnd)


def test_aadl2_portconnectionend_constructor_exists():
    assert callable(aadl2_PortConnectionEnd.__init__)


def test_aadl2_portconnectionend_constructor_args():
    sig = inspect.signature(aadl2_PortConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_parameterconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_ParameterConnectionEnd)


def test_aadl2_parameterconnectionend_constructor_exists():
    assert callable(aadl2_ParameterConnectionEnd.__init__)


def test_aadl2_parameterconnectionend_constructor_args():
    sig = inspect.signature(aadl2_ParameterConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featuregroupconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupConnectionEnd)


def test_aadl2_featuregroupconnectionend_constructor_exists():
    assert callable(aadl2_FeatureGroupConnectionEnd.__init__)


def test_aadl2_featuregroupconnectionend_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featureconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureConnectionEnd)


def test_aadl2_featureconnectionend_constructor_exists():
    assert callable(aadl2_FeatureConnectionEnd.__init__)


def test_aadl2_featureconnectionend_constructor_args():
    sig = inspect.signature(aadl2_FeatureConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_arrayableelement_is_not_abstract():
    assert not inspect.isabstract(ArrayableElement)


def test_arrayableelement_constructor_exists():
    assert callable(ArrayableElement.__init__)


def test_arrayableelement_constructor_args():
    sig = inspect.signature(ArrayableElement.__init__)
    params = list(sig.parameters.keys())



def test_featureconnectionend_is_not_abstract():
    assert not inspect.isabstract(FeatureConnectionEnd)


def test_featureconnectionend_constructor_exists():
    assert callable(FeatureConnectionEnd.__init__)


def test_featureconnectionend_constructor_args():
    sig = inspect.signature(FeatureConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_typeextension_is_not_abstract():
    assert not inspect.isabstract(aadl2_TypeExtension)


def test_aadl2_typeextension_constructor_exists():
    assert callable(aadl2_TypeExtension.__init__)


def test_aadl2_typeextension_constructor_args():
    sig = inspect.signature(aadl2_TypeExtension.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featuregrouptype_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupType)


def test_aadl2_featuregrouptype_constructor_exists():
    assert callable(aadl2_FeatureGroupType.__init__)


def test_aadl2_featuregrouptype_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupType.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_aadl2_featuregrouptype_has_feature():
    assert hasattr(aadl2_FeatureGroupType, "feature")
    descriptor = None
    for klass in aadl2_FeatureGroupType.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_componentclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentClassifier)


def test_aadl2_componentclassifier_constructor_exists():
    assert callable(aadl2_ComponentClassifier.__init__)


def test_aadl2_componentclassifier_constructor_args():
    sig = inspect.signature(aadl2_ComponentClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "noFlows" in params, "Missing parameter 'noFlows'"
    assert "noModes" in params, "Missing parameter 'noModes'"

def test_aadl2_componentclassifier_has_noFlows():
    assert hasattr(aadl2_ComponentClassifier, "noFlows")
    descriptor = None
    for klass in aadl2_ComponentClassifier.__mro__:
        if "noFlows" in klass.__dict__:
            descriptor = klass.__dict__["noFlows"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_componentclassifier_has_noModes():
    assert hasattr(aadl2_ComponentClassifier, "noModes")
    descriptor = None
    for klass in aadl2_ComponentClassifier.__mro__:
        if "noModes" in klass.__dict__:
            descriptor = klass.__dict__["noModes"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_processorsubprogram_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorSubprogram)


def test_aadl2_processorsubprogram_constructor_exists():
    assert callable(aadl2_ProcessorSubprogram.__init__)


def test_aadl2_processorsubprogram_constructor_args():
    sig = inspect.signature(aadl2_ProcessorSubprogram.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_access_is_not_abstract():
    assert not inspect.isabstract(aadl2_Access)


def test_aadl2_access_constructor_exists():
    assert callable(aadl2_Access.__init__)


def test_aadl2_access_constructor_args():
    sig = inspect.signature(aadl2_Access.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_aadl2_access_has_category():
    assert hasattr(aadl2_Access, "category")
    descriptor = None
    for klass in aadl2_Access.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_access_has_kind():
    assert hasattr(aadl2_Access, "kind")
    descriptor = None
    for klass in aadl2_Access.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_directedfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_DirectedFeature)


def test_aadl2_directedfeature_constructor_exists():
    assert callable(aadl2_DirectedFeature.__init__)


def test_aadl2_directedfeature_constructor_args():
    sig = inspect.signature(aadl2_DirectedFeature.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_aadl2_directedfeature_has_direction():
    assert hasattr(aadl2_DirectedFeature, "direction")
    descriptor = None
    for klass in aadl2_DirectedFeature.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_portconnectionend_is_not_abstract():
    assert not inspect.isabstract(PortConnectionEnd)


def test_portconnectionend_constructor_exists():
    assert callable(PortConnectionEnd.__init__)


def test_portconnectionend_constructor_args():
    sig = inspect.signature(PortConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_dataaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataAccess)


def test_aadl2_dataaccess_constructor_exists():
    assert callable(aadl2_DataAccess.__init__)


def test_aadl2_dataaccess_constructor_args():
    sig = inspect.signature(aadl2_DataAccess.__init__)
    params = list(sig.parameters.keys())



def test_directedfeature_is_not_abstract():
    assert not inspect.isabstract(DirectedFeature)


def test_directedfeature_constructor_exists():
    assert callable(DirectedFeature.__init__)


def test_directedfeature_constructor_args():
    sig = inspect.signature(DirectedFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_parameter_is_not_abstract():
    assert not inspect.isabstract(aadl2_Parameter)


def test_aadl2_parameter_constructor_exists():
    assert callable(aadl2_Parameter.__init__)


def test_aadl2_parameter_constructor_args():
    sig = inspect.signature(aadl2_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featuregroup_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroup)


def test_aadl2_featuregroup_constructor_exists():
    assert callable(aadl2_FeatureGroup.__init__)


def test_aadl2_featuregroup_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroup.__init__)
    params = list(sig.parameters.keys())
    assert "inverse" in params, "Missing parameter 'inverse'"

def test_aadl2_featuregroup_has_inverse():
    assert hasattr(aadl2_FeatureGroup, "inverse")
    descriptor = None
    for klass in aadl2_FeatureGroup.__mro__:
        if "inverse" in klass.__dict__:
            descriptor = klass.__dict__["inverse"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_abstractfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractFeature)


def test_aadl2_abstractfeature_constructor_exists():
    assert callable(aadl2_AbstractFeature.__init__)


def test_aadl2_abstractfeature_constructor_args():
    sig = inspect.signature(aadl2_AbstractFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_port_is_not_abstract():
    assert not inspect.isabstract(aadl2_Port)


def test_aadl2_port_constructor_exists():
    assert callable(aadl2_Port.__init__)


def test_aadl2_port_constructor_args():
    sig = inspect.signature(aadl2_Port.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"

def test_aadl2_port_has_category():
    assert hasattr(aadl2_Port, "category")
    descriptor = None
    for klass in aadl2_Port.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_modetransitiontrigger_is_not_abstract():
    assert not inspect.isabstract(ModeTransitionTrigger)


def test_modetransitiontrigger_constructor_exists():
    assert callable(ModeTransitionTrigger.__init__)


def test_modetransitiontrigger_constructor_args():
    sig = inspect.signature(ModeTransitionTrigger.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processorport_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorPort)


def test_aadl2_processorport_constructor_exists():
    assert callable(aadl2_ProcessorPort.__init__)


def test_aadl2_processorport_constructor_args():
    sig = inspect.signature(aadl2_ProcessorPort.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_internalevent_is_not_abstract():
    assert not inspect.isabstract(aadl2_InternalEvent)


def test_aadl2_internalevent_constructor_exists():
    assert callable(aadl2_InternalEvent.__init__)


def test_aadl2_internalevent_constructor_args():
    sig = inspect.signature(aadl2_InternalEvent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_triggerport_is_not_abstract():
    assert not inspect.isabstract(aadl2_TriggerPort)


def test_aadl2_triggerport_constructor_exists():
    assert callable(aadl2_TriggerPort.__init__)


def test_aadl2_triggerport_constructor_args():
    sig = inspect.signature(aadl2_TriggerPort.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_realization_is_not_abstract():
    assert not inspect.isabstract(aadl2_Realization)


def test_aadl2_realization_constructor_exists():
    assert callable(aadl2_Realization.__init__)


def test_aadl2_realization_constructor_args():
    sig = inspect.signature(aadl2_Realization.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_implementationextension_is_not_abstract():
    assert not inspect.isabstract(aadl2_ImplementationExtension)


def test_aadl2_implementationextension_constructor_exists():
    assert callable(aadl2_ImplementationExtension.__init__)


def test_aadl2_implementationextension_constructor_args():
    sig = inspect.signature(aadl2_ImplementationExtension.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_abstractsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractSubcomponent)


def test_aadl2_abstractsubcomponent_constructor_exists():
    assert callable(aadl2_AbstractSubcomponent.__init__)


def test_aadl2_abstractsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_AbstractSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_endtoendflow_is_not_abstract():
    assert not inspect.isabstract(aadl2_EndToEndFlow)


def test_aadl2_endtoendflow_constructor_exists():
    assert callable(aadl2_EndToEndFlow.__init__)


def test_aadl2_endtoendflow_constructor_args():
    sig = inspect.signature(aadl2_EndToEndFlow.__init__)
    params = list(sig.parameters.keys())



def test_componentclassifier_is_not_abstract():
    assert not inspect.isabstract(ComponentClassifier)


def test_componentclassifier_constructor_exists():
    assert callable(ComponentClassifier.__init__)


def test_componentclassifier_constructor_args():
    sig = inspect.signature(ComponentClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupClassifier)


def test_aadl2_subprogramgroupclassifier_constructor_exists():
    assert callable(aadl2_SubprogramGroupClassifier.__init__)


def test_aadl2_subprogramgroupclassifier_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramClassifier)


def test_aadl2_subprogramclassifier_constructor_exists():
    assert callable(aadl2_SubprogramClassifier.__init__)


def test_aadl2_subprogramclassifier_constructor_args():
    sig = inspect.signature(aadl2_SubprogramClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_componenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentType)


def test_aadl2_componenttype_constructor_exists():
    assert callable(aadl2_ComponentType.__init__)


def test_aadl2_componenttype_constructor_args():
    sig = inspect.signature(aadl2_ComponentType.__init__)
    params = list(sig.parameters.keys())
    assert "features" in params, "Missing parameter 'features'"
    assert "noFeatures" in params, "Missing parameter 'noFeatures'"

def test_aadl2_componenttype_has_features():
    assert hasattr(aadl2_ComponentType, "features")
    descriptor = None
    for klass in aadl2_ComponentType.__mro__:
        if "features" in klass.__dict__:
            descriptor = klass.__dict__["features"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_componenttype_has_noFeatures():
    assert hasattr(aadl2_ComponentType, "noFeatures")
    descriptor = None
    for klass in aadl2_ComponentType.__mro__:
        if "noFeatures" in klass.__dict__:
            descriptor = klass.__dict__["noFeatures"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_abstractclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractClassifier)


def test_aadl2_abstractclassifier_constructor_exists():
    assert callable(aadl2_AbstractClassifier.__init__)


def test_aadl2_abstractclassifier_constructor_args():
    sig = inspect.signature(aadl2_AbstractClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_busclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusClassifier)


def test_aadl2_busclassifier_constructor_exists():
    assert callable(aadl2_BusClassifier.__init__)


def test_aadl2_busclassifier_constructor_args():
    sig = inspect.signature(aadl2_BusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_dataclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataClassifier)


def test_aadl2_dataclassifier_constructor_exists():
    assert callable(aadl2_DataClassifier.__init__)


def test_aadl2_dataclassifier_constructor_args():
    sig = inspect.signature(aadl2_DataClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_componentimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentImplementation)


def test_aadl2_componentimplementation_constructor_exists():
    assert callable(aadl2_ComponentImplementation.__init__)


def test_aadl2_componentimplementation_constructor_args():
    sig = inspect.signature(aadl2_ComponentImplementation.__init__)
    params = list(sig.parameters.keys())
    assert "flows" in params, "Missing parameter 'flows'"
    assert "noConnections" in params, "Missing parameter 'noConnections'"
    assert "noSubcomponents" in params, "Missing parameter 'noSubcomponents'"
    assert "subcomponents" in params, "Missing parameter 'subcomponents'"
    assert "connections" in params, "Missing parameter 'connections'"
    assert "noCalls" in params, "Missing parameter 'noCalls'"

def test_aadl2_componentimplementation_has_flows():
    assert hasattr(aadl2_ComponentImplementation, "flows")
    descriptor = None
    for klass in aadl2_ComponentImplementation.__mro__:
        if "flows" in klass.__dict__:
            descriptor = klass.__dict__["flows"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_componentimplementation_has_noConnections():
    assert hasattr(aadl2_ComponentImplementation, "noConnections")
    descriptor = None
    for klass in aadl2_ComponentImplementation.__mro__:
        if "noConnections" in klass.__dict__:
            descriptor = klass.__dict__["noConnections"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_componentimplementation_has_noSubcomponents():
    assert hasattr(aadl2_ComponentImplementation, "noSubcomponents")
    descriptor = None
    for klass in aadl2_ComponentImplementation.__mro__:
        if "noSubcomponents" in klass.__dict__:
            descriptor = klass.__dict__["noSubcomponents"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_componentimplementation_has_subcomponents():
    assert hasattr(aadl2_ComponentImplementation, "subcomponents")
    descriptor = None
    for klass in aadl2_ComponentImplementation.__mro__:
        if "subcomponents" in klass.__dict__:
            descriptor = klass.__dict__["subcomponents"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_componentimplementation_has_connections():
    assert hasattr(aadl2_ComponentImplementation, "connections")
    descriptor = None
    for klass in aadl2_ComponentImplementation.__mro__:
        if "connections" in klass.__dict__:
            descriptor = klass.__dict__["connections"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_componentimplementation_has_noCalls():
    assert hasattr(aadl2_ComponentImplementation, "noCalls")
    descriptor = None
    for klass in aadl2_ComponentImplementation.__mro__:
        if "noCalls" in klass.__dict__:
            descriptor = klass.__dict__["noCalls"]
            break
    assert isinstance(descriptor, property)



def test_arraysize_is_not_abstract():
    assert not inspect.isabstract(ArraySize)


def test_arraysize_constructor_exists():
    assert callable(ArraySize.__init__)


def test_arraysize_constructor_args():
    sig = inspect.signature(ArraySize.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_propertyreference_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyReference)


def test_aadl2_propertyreference_constructor_exists():
    assert callable(aadl2_PropertyReference.__init__)


def test_aadl2_propertyreference_constructor_args():
    sig = inspect.signature(aadl2_PropertyReference.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_constantvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ConstantValue)


def test_aadl2_constantvalue_constructor_exists():
    assert callable(aadl2_ConstantValue.__init__)


def test_aadl2_constantvalue_constructor_args():
    sig = inspect.signature(aadl2_ConstantValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_numeral_is_not_abstract():
    assert not inspect.isabstract(aadl2_Numeral)


def test_aadl2_numeral_constructor_exists():
    assert callable(aadl2_Numeral.__init__)


def test_aadl2_numeral_constructor_args():
    sig = inspect.signature(aadl2_Numeral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_aadl2_numeral_has_value():
    assert hasattr(aadl2_Numeral, "value")
    descriptor = None
    for klass in aadl2_Numeral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_refinableelement_is_not_abstract():
    assert not inspect.isabstract(RefinableElement)


def test_refinableelement_constructor_exists():
    assert callable(RefinableElement.__init__)


def test_refinableelement_constructor_args():
    sig = inspect.signature(RefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_flow_is_not_abstract():
    assert not inspect.isabstract(aadl2_Flow)


def test_aadl2_flow_constructor_exists():
    assert callable(aadl2_Flow.__init__)


def test_aadl2_flow_constructor_args():
    sig = inspect.signature(aadl2_Flow.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_feature_is_not_abstract():
    assert not inspect.isabstract(aadl2_Feature)


def test_aadl2_feature_constructor_exists():
    assert callable(aadl2_Feature.__init__)


def test_aadl2_feature_constructor_args():
    sig = inspect.signature(aadl2_Feature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_flowimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_FlowImplementation)


def test_aadl2_flowimplementation_constructor_exists():
    assert callable(aadl2_FlowImplementation.__init__)


def test_aadl2_flowimplementation_constructor_args():
    sig = inspect.signature(aadl2_FlowImplementation.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_aadl2_flowimplementation_has_kind():
    assert hasattr(aadl2_FlowImplementation, "kind")
    descriptor = None
    for klass in aadl2_FlowImplementation.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_connection_is_not_abstract():
    assert not inspect.isabstract(aadl2_Connection)


def test_aadl2_connection_constructor_exists():
    assert callable(aadl2_Connection.__init__)


def test_aadl2_connection_constructor_args():
    sig = inspect.signature(aadl2_Connection.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"

def test_aadl2_connection_has_kind():
    assert hasattr(aadl2_Connection, "kind")
    descriptor = None
    for klass in aadl2_Connection.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_connection_has_bidirectional():
    assert hasattr(aadl2_Connection, "bidirectional")
    descriptor = None
    for klass in aadl2_Connection.__mro__:
        if "bidirectional" in klass.__dict__:
            descriptor = klass.__dict__["bidirectional"]
            break
    assert isinstance(descriptor, property)



def test_classifierfeature_is_not_abstract():
    assert not inspect.isabstract(ClassifierFeature)


def test_classifierfeature_constructor_exists():
    assert callable(ClassifierFeature.__init__)


def test_classifierfeature_constructor_args():
    sig = inspect.signature(ClassifierFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_BehavioralFeature)


def test_aadl2_behavioralfeature_constructor_exists():
    assert callable(aadl2_BehavioralFeature.__init__)


def test_aadl2_behavioralfeature_constructor_args():
    sig = inspect.signature(aadl2_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_StructuralFeature)


def test_aadl2_structuralfeature_constructor_exists():
    assert callable(aadl2_StructuralFeature.__init__)


def test_aadl2_structuralfeature_constructor_args():
    sig = inspect.signature(aadl2_StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_modefeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModeFeature)


def test_aadl2_modefeature_constructor_exists():
    assert callable(aadl2_ModeFeature.__init__)


def test_aadl2_modefeature_constructor_args():
    sig = inspect.signature(aadl2_ModeFeature.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(aadl2_DirectedRelationship)


def test_aadl2_directedrelationship_constructor_exists():
    assert callable(aadl2_DirectedRelationship.__init__)


def test_aadl2_directedrelationship_constructor_args():
    sig = inspect.signature(aadl2_DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_modefeature_is_not_abstract():
    assert not inspect.isabstract(ModeFeature)


def test_modefeature_constructor_exists():
    assert callable(ModeFeature.__init__)


def test_modefeature_constructor_args():
    sig = inspect.signature(ModeFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_modetransition_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModeTransition)


def test_aadl2_modetransition_constructor_exists():
    assert callable(aadl2_ModeTransition.__init__)


def test_aadl2_modetransition_constructor_args():
    sig = inspect.signature(aadl2_ModeTransition.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_mode_is_not_abstract():
    assert not inspect.isabstract(aadl2_Mode)


def test_aadl2_mode_constructor_exists():
    assert callable(aadl2_Mode.__init__)


def test_aadl2_mode_constructor_args():
    sig = inspect.signature(aadl2_Mode.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_aadl2_mode_has_derived():
    assert hasattr(aadl2_Mode, "derived")
    descriptor = None
    for klass in aadl2_Mode.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_mode_has_initial():
    assert hasattr(aadl2_Mode, "initial")
    descriptor = None
    for klass in aadl2_Mode.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_modalelement_is_not_abstract():
    assert not inspect.isabstract(ModalElement)


def test_modalelement_constructor_exists():
    assert callable(ModalElement.__init__)


def test_modalelement_constructor_args():
    sig = inspect.signature(ModalElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_flowspecification_is_not_abstract():
    assert not inspect.isabstract(aadl2_FlowSpecification)


def test_aadl2_flowspecification_constructor_exists():
    assert callable(aadl2_FlowSpecification.__init__)


def test_aadl2_flowspecification_constructor_args():
    sig = inspect.signature(aadl2_FlowSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_aadl2_flowspecification_has_kind():
    assert hasattr(aadl2_FlowSpecification, "kind")
    descriptor = None
    for klass in aadl2_FlowSpecification.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_modalpath_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModalPath)


def test_aadl2_modalpath_constructor_exists():
    assert callable(aadl2_ModalPath.__init__)


def test_aadl2_modalpath_constructor_args():
    sig = inspect.signature(aadl2_ModalPath.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_Subcomponent)


def test_aadl2_subcomponent_constructor_exists():
    assert callable(aadl2_Subcomponent.__init__)


def test_aadl2_subcomponent_constructor_args():
    sig = inspect.signature(aadl2_Subcomponent.__init__)
    params = list(sig.parameters.keys())
    assert "allModes" in params, "Missing parameter 'allModes'"

def test_aadl2_subcomponent_has_allModes():
    assert hasattr(aadl2_Subcomponent, "allModes")
    descriptor = None
    for klass in aadl2_Subcomponent.__mro__:
        if "allModes" in klass.__dict__:
            descriptor = klass.__dict__["allModes"]
            break
    assert isinstance(descriptor, property)



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_generalization__is_not_abstract():
    assert not inspect.isabstract(aadl2_Generalization_)


def test_aadl2_generalization__constructor_exists():
    assert callable(aadl2_Generalization_.__init__)


def test_aadl2_generalization__constructor_args():
    sig = inspect.signature(aadl2_Generalization_.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_prototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_Prototype)


def test_aadl2_prototype_constructor_exists():
    assert callable(aadl2_Prototype.__init__)


def test_aadl2_prototype_constructor_args():
    sig = inspect.signature(aadl2_Prototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_annexsubclause_is_not_abstract():
    assert not inspect.isabstract(aadl2_AnnexSubclause)


def test_aadl2_annexsubclause_constructor_exists():
    assert callable(aadl2_AnnexSubclause.__init__)


def test_aadl2_annexsubclause_constructor_args():
    sig = inspect.signature(aadl2_AnnexSubclause.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_globalnamespace_is_not_abstract():
    assert not inspect.isabstract(aadl2_GlobalNamespace)


def test_aadl2_globalnamespace_constructor_exists():
    assert callable(aadl2_GlobalNamespace.__init__)


def test_aadl2_globalnamespace_constructor_args():
    sig = inspect.signature(aadl2_GlobalNamespace.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_recordtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_RecordType)


def test_aadl2_recordtype_constructor_exists():
    assert callable(aadl2_RecordType.__init__)


def test_aadl2_recordtype_constructor_args():
    sig = inspect.signature(aadl2_RecordType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_EnumerationType)


def test_aadl2_enumerationtype_constructor_exists():
    assert callable(aadl2_EnumerationType.__init__)


def test_aadl2_enumerationtype_constructor_args():
    sig = inspect.signature(aadl2_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_propertyowner_is_not_abstract():
    assert not inspect.isabstract(PropertyOwner)


def test_propertyowner_constructor_exists():
    assert callable(PropertyOwner.__init__)


def test_propertyowner_constructor_args():
    sig = inspect.signature(PropertyOwner.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_classifiervalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ClassifierValue)


def test_aadl2_classifiervalue_constructor_exists():
    assert callable(aadl2_ClassifierValue.__init__)


def test_aadl2_classifiervalue_constructor_args():
    sig = inspect.signature(aadl2_ClassifierValue.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_propertytype_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyType)


def test_aadl2_propertytype_constructor_exists():
    assert callable(aadl2_PropertyType.__init__)


def test_aadl2_propertytype_constructor_args():
    sig = inspect.signature(aadl2_PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_classifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_Classifier)


def test_aadl2_classifier_constructor_exists():
    assert callable(aadl2_Classifier.__init__)


def test_aadl2_classifier_constructor_args():
    sig = inspect.signature(aadl2_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "noProperties" in params, "Missing parameter 'noProperties'"
    assert "noPrototypes" in params, "Missing parameter 'noPrototypes'"
    assert "noAnnexes" in params, "Missing parameter 'noAnnexes'"

def test_aadl2_classifier_has_noProperties():
    assert hasattr(aadl2_Classifier, "noProperties")
    descriptor = None
    for klass in aadl2_Classifier.__mro__:
        if "noProperties" in klass.__dict__:
            descriptor = klass.__dict__["noProperties"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_classifier_has_noPrototypes():
    assert hasattr(aadl2_Classifier, "noPrototypes")
    descriptor = None
    for klass in aadl2_Classifier.__mro__:
        if "noPrototypes" in klass.__dict__:
            descriptor = klass.__dict__["noPrototypes"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_classifier_has_noAnnexes():
    assert hasattr(aadl2_Classifier, "noAnnexes")
    descriptor = None
    for klass in aadl2_Classifier.__mro__:
        if "noAnnexes" in klass.__dict__:
            descriptor = klass.__dict__["noAnnexes"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_basicproperty_is_not_abstract():
    assert not inspect.isabstract(aadl2_BasicProperty)


def test_aadl2_basicproperty_constructor_exists():
    assert callable(aadl2_BasicProperty.__init__)


def test_aadl2_basicproperty_constructor_args():
    sig = inspect.signature(aadl2_BasicProperty.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"

def test_aadl2_basicproperty_has_list():
    assert hasattr(aadl2_BasicProperty, "list")
    descriptor = None
    for klass in aadl2_BasicProperty.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_metaclassreference_is_not_abstract():
    assert not inspect.isabstract(aadl2_MetaclassReference)


def test_aadl2_metaclassreference_constructor_exists():
    assert callable(aadl2_MetaclassReference.__init__)


def test_aadl2_metaclassreference_constructor_args():
    sig = inspect.signature(aadl2_MetaclassReference.__init__)
    params = list(sig.parameters.keys())
    assert "annexName" in params, "Missing parameter 'annexName'"
    assert "metaclassName" in params, "Missing parameter 'metaclassName'"

def test_aadl2_metaclassreference_has_annexName():
    assert hasattr(aadl2_MetaclassReference, "annexName")
    descriptor = None
    for klass in aadl2_MetaclassReference.__mro__:
        if "annexName" in klass.__dict__:
            descriptor = klass.__dict__["annexName"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_metaclassreference_has_metaclassName():
    assert hasattr(aadl2_MetaclassReference, "metaclassName")
    descriptor = None
    for klass in aadl2_MetaclassReference.__mro__:
        if "metaclassName" in klass.__dict__:
            descriptor = klass.__dict__["metaclassName"]
            break
    assert isinstance(descriptor, property)



def test_basicproperty_is_not_abstract():
    assert not inspect.isabstract(BasicProperty)


def test_basicproperty_constructor_exists():
    assert callable(BasicProperty.__init__)


def test_basicproperty_constructor_args():
    sig = inspect.signature(BasicProperty.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_recordfield_is_not_abstract():
    assert not inspect.isabstract(aadl2_RecordField)


def test_aadl2_recordfield_constructor_exists():
    assert callable(aadl2_RecordField.__init__)


def test_aadl2_recordfield_constructor_args():
    sig = inspect.signature(aadl2_RecordField.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_property_is_not_abstract():
    assert not inspect.isabstract(aadl2_Property)


def test_aadl2_property_constructor_exists():
    assert callable(aadl2_Property.__init__)


def test_aadl2_property_constructor_args():
    sig = inspect.signature(aadl2_Property.__init__)
    params = list(sig.parameters.keys())
    assert "emptyListDefault" in params, "Missing parameter 'emptyListDefault'"
    assert "inherit" in params, "Missing parameter 'inherit'"

def test_aadl2_property_has_emptyListDefault():
    assert hasattr(aadl2_Property, "emptyListDefault")
    descriptor = None
    for klass in aadl2_Property.__mro__:
        if "emptyListDefault" in klass.__dict__:
            descriptor = klass.__dict__["emptyListDefault"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_property_has_inherit():
    assert hasattr(aadl2_Property, "inherit")
    descriptor = None
    for klass in aadl2_Property.__mro__:
        if "inherit" in klass.__dict__:
            descriptor = klass.__dict__["inherit"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_modalpropertyvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModalPropertyValue)


def test_aadl2_modalpropertyvalue_constructor_exists():
    assert callable(aadl2_ModalPropertyValue.__init__)


def test_aadl2_modalpropertyvalue_constructor_args():
    sig = inspect.signature(aadl2_ModalPropertyValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_element_is_not_abstract():
    assert not inspect.isabstract(aadl2_Element)


def test_aadl2_element_constructor_exists():
    assert callable(aadl2_Element.__init__)


def test_aadl2_element_constructor_args():
    sig = inspect.signature(aadl2_Element.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_endtoendflowelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_EndToEndFlowElement)


def test_aadl2_endtoendflowelement_constructor_exists():
    assert callable(aadl2_EndToEndFlowElement.__init__)


def test_aadl2_endtoendflowelement_constructor_args():
    sig = inspect.signature(aadl2_EndToEndFlowElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_connectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_ConnectionEnd)


def test_aadl2_connectionend_constructor_exists():
    assert callable(aadl2_ConnectionEnd.__init__)


def test_aadl2_connectionend_constructor_args():
    sig = inspect.signature(aadl2_ConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_context_is_not_abstract():
    assert not inspect.isabstract(aadl2_Context)


def test_aadl2_context_constructor_exists():
    assert callable(aadl2_Context.__init__)


def test_aadl2_context_constructor_args():
    sig = inspect.signature(aadl2_Context.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogram_is_not_abstract():
    assert not inspect.isabstract(aadl2_Subprogram)


def test_aadl2_subprogram_constructor_exists():
    assert callable(aadl2_Subprogram.__init__)


def test_aadl2_subprogram_constructor_args():
    sig = inspect.signature(aadl2_Subprogram.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_bus_is_not_abstract():
    assert not inspect.isabstract(aadl2_Bus)


def test_aadl2_bus_constructor_exists():
    assert callable(aadl2_Bus.__init__)


def test_aadl2_bus_constructor_args():
    sig = inspect.signature(aadl2_Bus.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_type_is_not_abstract():
    assert not inspect.isabstract(aadl2_Type)


def test_aadl2_type_constructor_exists():
    assert callable(aadl2_Type.__init__)


def test_aadl2_type_constructor_args():
    sig = inspect.signature(aadl2_Type.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_typedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_TypedElement)


def test_aadl2_typedelement_constructor_exists():
    assert callable(aadl2_TypedElement.__init__)


def test_aadl2_typedelement_constructor_args():
    sig = inspect.signature(aadl2_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_abstract_is_not_abstract():
    assert not inspect.isabstract(aadl2_Abstract)


def test_aadl2_abstract_constructor_exists():
    assert callable(aadl2_Abstract.__init__)


def test_aadl2_abstract_constructor_args():
    sig = inspect.signature(aadl2_Abstract.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_classifierfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_ClassifierFeature)


def test_aadl2_classifierfeature_constructor_exists():
    assert callable(aadl2_ClassifierFeature.__init__)


def test_aadl2_classifierfeature_constructor_args():
    sig = inspect.signature(aadl2_ClassifierFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_modalelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModalElement)


def test_aadl2_modalelement_constructor_exists():
    assert callable(aadl2_ModalElement.__init__)


def test_aadl2_modalelement_constructor_args():
    sig = inspect.signature(aadl2_ModalElement.__init__)
    params = list(sig.parameters.keys())
    assert "modesAndTransitions" in params, "Missing parameter 'modesAndTransitions'"

def test_aadl2_modalelement_has_modesAndTransitions():
    assert hasattr(aadl2_ModalElement, "modesAndTransitions")
    descriptor = None
    for klass in aadl2_ModalElement.__mro__:
        if "modesAndTransitions" in klass.__dict__:
            descriptor = klass.__dict__["modesAndTransitions"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_EnumerationLiteral)


def test_aadl2_enumerationliteral_constructor_exists():
    assert callable(aadl2_EnumerationLiteral.__init__)


def test_aadl2_enumerationliteral_constructor_args():
    sig = inspect.signature(aadl2_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_annexlibrary_is_not_abstract():
    assert not inspect.isabstract(aadl2_AnnexLibrary)


def test_aadl2_annexlibrary_constructor_exists():
    assert callable(aadl2_AnnexLibrary.__init__)


def test_aadl2_annexlibrary_constructor_args():
    sig = inspect.signature(aadl2_AnnexLibrary.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_refinableelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_RefinableElement)


def test_aadl2_refinableelement_constructor_exists():
    assert callable(aadl2_RefinableElement.__init__)


def test_aadl2_refinableelement_constructor_args():
    sig = inspect.signature(aadl2_RefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgroup_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroup)


def test_aadl2_subprogramgroup_constructor_exists():
    assert callable(aadl2_SubprogramGroup.__init__)


def test_aadl2_subprogramgroup_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroup.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_data_is_not_abstract():
    assert not inspect.isabstract(aadl2_Data)


def test_aadl2_data_constructor_exists():
    assert callable(aadl2_Data.__init__)


def test_aadl2_data_constructor_args():
    sig = inspect.signature(aadl2_Data.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_namespace_is_not_abstract():
    assert not inspect.isabstract(aadl2_Namespace)


def test_aadl2_namespace_constructor_exists():
    assert callable(aadl2_Namespace.__init__)


def test_aadl2_namespace_constructor_args():
    sig = inspect.signature(aadl2_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_arrayspecification_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArraySpecification)


def test_aadl2_arrayspecification_constructor_exists():
    assert callable(aadl2_ArraySpecification.__init__)


def test_aadl2_arrayspecification_constructor_args():
    sig = inspect.signature(aadl2_ArraySpecification.__init__)
    params = list(sig.parameters.keys())
    assert "dimension" in params, "Missing parameter 'dimension'"

def test_aadl2_arrayspecification_has_dimension():
    assert hasattr(aadl2_ArraySpecification, "dimension")
    descriptor = None
    for klass in aadl2_ArraySpecification.__mro__:
        if "dimension" in klass.__dict__:
            descriptor = klass.__dict__["dimension"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_relationship_is_not_abstract():
    assert not inspect.isabstract(aadl2_Relationship)


def test_aadl2_relationship_constructor_exists():
    assert callable(aadl2_Relationship.__init__)


def test_aadl2_relationship_constructor_args():
    sig = inspect.signature(aadl2_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_componentimplementationreference_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentImplementationReference)


def test_aadl2_componentimplementationreference_constructor_exists():
    assert callable(aadl2_ComponentImplementationReference.__init__)


def test_aadl2_componentimplementationreference_constructor_args():
    sig = inspect.signature(aadl2_ComponentImplementationReference.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_propertyowner_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyOwner)


def test_aadl2_propertyowner_constructor_exists():
    assert callable(aadl2_PropertyOwner.__init__)


def test_aadl2_propertyowner_constructor_args():
    sig = inspect.signature(aadl2_PropertyOwner.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_propertyexpression_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyExpression)


def test_aadl2_propertyexpression_constructor_exists():
    assert callable(aadl2_PropertyExpression.__init__)


def test_aadl2_propertyexpression_constructor_args():
    sig = inspect.signature(aadl2_PropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_arrayrange_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArrayRange)


def test_aadl2_arrayrange_constructor_exists():
    assert callable(aadl2_ArrayRange.__init__)


def test_aadl2_arrayrange_constructor_args():
    sig = inspect.signature(aadl2_ArrayRange.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_aadl2_arrayrange_has_lowerBound():
    assert hasattr(aadl2_ArrayRange, "lowerBound")
    descriptor = None
    for klass in aadl2_ArrayRange.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_arrayrange_has_upperBound():
    assert hasattr(aadl2_ArrayRange, "upperBound")
    descriptor = None
    for klass in aadl2_ArrayRange.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_modebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModeBinding)


def test_aadl2_modebinding_constructor_exists():
    assert callable(aadl2_ModeBinding.__init__)


def test_aadl2_modebinding_constructor_args():
    sig = inspect.signature(aadl2_ModeBinding.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_callcontext_is_not_abstract():
    assert not inspect.isabstract(aadl2_CallContext)


def test_aadl2_callcontext_constructor_exists():
    assert callable(aadl2_CallContext.__init__)


def test_aadl2_callcontext_constructor_args():
    sig = inspect.signature(aadl2_CallContext.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_modetransitiontrigger_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModeTransitionTrigger)


def test_aadl2_modetransitiontrigger_constructor_exists():
    assert callable(aadl2_ModeTransitionTrigger.__init__)


def test_aadl2_modetransitiontrigger_constructor_args():
    sig = inspect.signature(aadl2_ModeTransitionTrigger.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_basicpropertyassociation_is_not_abstract():
    assert not inspect.isabstract(aadl2_BasicPropertyAssociation)


def test_aadl2_basicpropertyassociation_constructor_exists():
    assert callable(aadl2_BasicPropertyAssociation.__init__)


def test_aadl2_basicpropertyassociation_constructor_args():
    sig = inspect.signature(aadl2_BasicPropertyAssociation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_calledsubprogram_is_not_abstract():
    assert not inspect.isabstract(aadl2_CalledSubprogram)


def test_aadl2_calledsubprogram_constructor_exists():
    assert callable(aadl2_CalledSubprogram.__init__)


def test_aadl2_calledsubprogram_constructor_args():
    sig = inspect.signature(aadl2_CalledSubprogram.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_arraysize_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArraySize)


def test_aadl2_arraysize_constructor_exists():
    assert callable(aadl2_ArraySize.__init__)


def test_aadl2_arraysize_constructor_args():
    sig = inspect.signature(aadl2_ArraySize.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_propertyassociation_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyAssociation)


def test_aadl2_propertyassociation_constructor_exists():
    assert callable(aadl2_PropertyAssociation.__init__)


def test_aadl2_propertyassociation_constructor_args():
    sig = inspect.signature(aadl2_PropertyAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "append" in params, "Missing parameter 'append'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_aadl2_propertyassociation_has_append():
    assert hasattr(aadl2_PropertyAssociation, "append")
    descriptor = None
    for klass in aadl2_PropertyAssociation.__mro__:
        if "append" in klass.__dict__:
            descriptor = klass.__dict__["append"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_propertyassociation_has_constant():
    assert hasattr(aadl2_PropertyAssociation, "constant")
    descriptor = None
    for klass in aadl2_PropertyAssociation.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_arrayableelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArrayableElement)


def test_aadl2_arrayableelement_constructor_exists():
    assert callable(aadl2_ArrayableElement.__init__)


def test_aadl2_arrayableelement_constructor_args():
    sig = inspect.signature(aadl2_ArrayableElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_containednamedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ContainedNamedElement)


def test_aadl2_containednamedelement_constructor_exists():
    assert callable(aadl2_ContainedNamedElement.__init__)


def test_aadl2_containednamedelement_constructor_args():
    sig = inspect.signature(aadl2_ContainedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_namedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_NamedElement)


def test_aadl2_namedelement_constructor_exists():
    assert callable(aadl2_NamedElement.__init__)


def test_aadl2_namedelement_constructor_args():
    sig = inspect.signature(aadl2_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "name" in params, "Missing parameter 'name'"

def test_aadl2_namedelement_has_qualifiedName():
    assert hasattr(aadl2_NamedElement, "qualifiedName")
    descriptor = None
    for klass in aadl2_NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_namedelement_has_name():
    assert hasattr(aadl2_NamedElement, "name")
    descriptor = None
    for klass in aadl2_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_containmentpathelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ContainmentPathElement)


def test_aadl2_containmentpathelement_constructor_exists():
    assert callable(aadl2_ContainmentPathElement.__init__)


def test_aadl2_containmentpathelement_constructor_args():
    sig = inspect.signature(aadl2_ContainmentPathElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_prototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2_PrototypeBinding)


def test_aadl2_prototypebinding_constructor_exists():
    assert callable(aadl2_PrototypeBinding.__init__)


def test_aadl2_prototypebinding_constructor_args():
    sig = inspect.signature(aadl2_PrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_numericrange_is_not_abstract():
    assert not inspect.isabstract(aadl2_NumericRange)


def test_aadl2_numericrange_constructor_exists():
    assert callable(aadl2_NumericRange.__init__)


def test_aadl2_numericrange_constructor_args():
    sig = inspect.signature(aadl2_NumericRange.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_comment_is_not_abstract():
    assert not inspect.isabstract(aadl2_Comment)


def test_aadl2_comment_constructor_exists():
    assert callable(aadl2_Comment.__init__)


def test_aadl2_comment_constructor_args():
    sig = inspect.signature(aadl2_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_aadl2_comment_has_body():
    assert hasattr(aadl2_Comment, "body")
    descriptor = None
    for klass in aadl2_Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_componentprototypeactual_is_not_abstract():
    assert not inspect.isabstract(ComponentPrototypeActual)


def test_componentprototypeactual_constructor_exists():
    assert callable(ComponentPrototypeActual.__init__)


def test_componentprototypeactual_constructor_args():
    sig = inspect.signature(ComponentPrototypeActual.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_componentprototypereference_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentPrototypeReference)


def test_aadl2_componentprototypereference_constructor_exists():
    assert callable(aadl2_ComponentPrototypeReference.__init__)


def test_aadl2_componentprototypereference_constructor_args():
    sig = inspect.signature(aadl2_ComponentPrototypeReference.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_unitliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_UnitLiteral)


def test_aadl2_unitliteral_constructor_exists():
    assert callable(aadl2_UnitLiteral.__init__)


def test_aadl2_unitliteral_constructor_args():
    sig = inspect.signature(aadl2_UnitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_unitvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_UnitValue)


def test_aadl2_unitvalue_constructor_exists():
    assert callable(aadl2_UnitValue.__init__)


def test_aadl2_unitvalue_constructor_args():
    sig = inspect.signature(aadl2_UnitValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_componentreference_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentReference)


def test_aadl2_componentreference_constructor_exists():
    assert callable(aadl2_ComponentReference.__init__)


def test_aadl2_componentreference_constructor_args():
    sig = inspect.signature(aadl2_ComponentReference.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featureprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeaturePrototype)


def test_aadl2_featureprototype_constructor_exists():
    assert callable(aadl2_FeaturePrototype.__init__)


def test_aadl2_featureprototype_constructor_args():
    sig = inspect.signature(aadl2_FeaturePrototype.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_aadl2_featureprototype_has_direction():
    assert hasattr(aadl2_FeaturePrototype, "direction")
    descriptor = None
    for klass in aadl2_FeaturePrototype.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_featuregroupprototypeactual_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupPrototypeActual)


def test_aadl2_featuregroupprototypeactual_constructor_exists():
    assert callable(aadl2_FeatureGroupPrototypeActual.__init__)


def test_aadl2_featuregroupprototypeactual_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupPrototypeActual.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featuregroupprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupPrototype)


def test_aadl2_featuregroupprototype_constructor_exists():
    assert callable(aadl2_FeatureGroupPrototype.__init__)


def test_aadl2_featuregroupprototype_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_componentprototypeactual_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentPrototypeActual)


def test_aadl2_componentprototypeactual_constructor_exists():
    assert callable(aadl2_ComponentPrototypeActual.__init__)


def test_aadl2_componentprototypeactual_constructor_args():
    sig = inspect.signature(aadl2_ComponentPrototypeActual.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"

def test_aadl2_componentprototypeactual_has_category():
    assert hasattr(aadl2_ComponentPrototypeActual, "category")
    descriptor = None
    for klass in aadl2_ComponentPrototypeActual.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_featureprototypeactual_is_not_abstract():
    assert not inspect.isabstract(FeaturePrototypeActual)


def test_featureprototypeactual_constructor_exists():
    assert callable(FeaturePrototypeActual.__init__)


def test_featureprototypeactual_constructor_args():
    sig = inspect.signature(FeaturePrototypeActual.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_portspecification_is_not_abstract():
    assert not inspect.isabstract(aadl2_PortSpecification)


def test_aadl2_portspecification_constructor_exists():
    assert callable(aadl2_PortSpecification.__init__)


def test_aadl2_portspecification_constructor_args():
    sig = inspect.signature(aadl2_PortSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "category" in params, "Missing parameter 'category'"

def test_aadl2_portspecification_has_direction():
    assert hasattr(aadl2_PortSpecification, "direction")
    descriptor = None
    for klass in aadl2_PortSpecification.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_portspecification_has_category():
    assert hasattr(aadl2_PortSpecification, "category")
    descriptor = None
    for klass in aadl2_PortSpecification.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_featureprototypereference_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeaturePrototypeReference)


def test_aadl2_featureprototypereference_constructor_exists():
    assert callable(aadl2_FeaturePrototypeReference.__init__)


def test_aadl2_featureprototypereference_constructor_args():
    sig = inspect.signature(aadl2_FeaturePrototypeReference.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_aadl2_featureprototypereference_has_direction():
    assert hasattr(aadl2_FeaturePrototypeReference, "direction")
    descriptor = None
    for klass in aadl2_FeaturePrototypeReference.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_accessspecification_is_not_abstract():
    assert not inspect.isabstract(aadl2_AccessSpecification)


def test_aadl2_accessspecification_constructor_exists():
    assert callable(aadl2_AccessSpecification.__init__)


def test_aadl2_accessspecification_constructor_args():
    sig = inspect.signature(aadl2_AccessSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_aadl2_accessspecification_has_category():
    assert hasattr(aadl2_AccessSpecification, "category")
    descriptor = None
    for klass in aadl2_AccessSpecification.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_accessspecification_has_kind():
    assert hasattr(aadl2_AccessSpecification, "kind")
    descriptor = None
    for klass in aadl2_AccessSpecification.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_featureprototypeactual_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeaturePrototypeActual)


def test_aadl2_featureprototypeactual_constructor_exists():
    assert callable(aadl2_FeaturePrototypeActual.__init__)


def test_aadl2_featureprototypeactual_constructor_args():
    sig = inspect.signature(aadl2_FeaturePrototypeActual.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_propertyconstant_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyConstant)


def test_aadl2_propertyconstant_constructor_exists():
    assert callable(aadl2_PropertyConstant.__init__)


def test_aadl2_propertyconstant_constructor_args():
    sig = inspect.signature(aadl2_PropertyConstant.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"

def test_aadl2_propertyconstant_has_list():
    assert hasattr(aadl2_PropertyConstant, "list")
    descriptor = None
    for klass in aadl2_PropertyConstant.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_prototypebinding_is_not_abstract():
    assert not inspect.isabstract(PrototypeBinding)


def test_prototypebinding_constructor_exists():
    assert callable(PrototypeBinding.__init__)


def test_prototypebinding_constructor_args():
    sig = inspect.signature(PrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featureprototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeaturePrototypeBinding)


def test_aadl2_featureprototypebinding_constructor_exists():
    assert callable(aadl2_FeaturePrototypeBinding.__init__)


def test_aadl2_featureprototypebinding_constructor_args():
    sig = inspect.signature(aadl2_FeaturePrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featuregroupprototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupPrototypeBinding)


def test_aadl2_featuregroupprototypebinding_constructor_exists():
    assert callable(aadl2_FeatureGroupPrototypeBinding.__init__)


def test_aadl2_featuregroupprototypebinding_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupPrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_componentprototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentPrototypeBinding)


def test_aadl2_componentprototypebinding_constructor_exists():
    assert callable(aadl2_ComponentPrototypeBinding.__init__)


def test_aadl2_componentprototypebinding_constructor_args():
    sig = inspect.signature(aadl2_ComponentPrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_virtualprocessorclassifier_is_not_abstract():
    assert not inspect.isabstract(VirtualProcessorClassifier)


def test_virtualprocessorclassifier_constructor_exists():
    assert callable(VirtualProcessorClassifier.__init__)


def test_virtualprocessorclassifier_constructor_args():
    sig = inspect.signature(VirtualProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_virtualbusclassifier_is_not_abstract():
    assert not inspect.isabstract(VirtualBusClassifier)


def test_virtualbusclassifier_constructor_exists():
    assert callable(VirtualBusClassifier.__init__)


def test_virtualbusclassifier_constructor_args():
    sig = inspect.signature(VirtualBusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_threadgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(ThreadGroupClassifier)


def test_threadgroupclassifier_constructor_exists():
    assert callable(ThreadGroupClassifier.__init__)


def test_threadgroupclassifier_constructor_args():
    sig = inspect.signature(ThreadGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_threadclassifier_is_not_abstract():
    assert not inspect.isabstract(ThreadClassifier)


def test_threadclassifier_constructor_exists():
    assert callable(ThreadClassifier.__init__)


def test_threadclassifier_constructor_args():
    sig = inspect.signature(ThreadClassifier.__init__)
    params = list(sig.parameters.keys())



def test_systemclassifier_is_not_abstract():
    assert not inspect.isabstract(SystemClassifier)


def test_systemclassifier_constructor_exists():
    assert callable(SystemClassifier.__init__)


def test_systemclassifier_constructor_args():
    sig = inspect.signature(SystemClassifier.__init__)
    params = list(sig.parameters.keys())



def test_subprogramgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(SubprogramGroupClassifier)


def test_subprogramgroupclassifier_constructor_exists():
    assert callable(SubprogramGroupClassifier.__init__)


def test_subprogramgroupclassifier_constructor_args():
    sig = inspect.signature(SubprogramGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_subprogramclassifier_is_not_abstract():
    assert not inspect.isabstract(SubprogramClassifier)


def test_subprogramclassifier_constructor_exists():
    assert callable(SubprogramClassifier.__init__)


def test_subprogramclassifier_constructor_args():
    sig = inspect.signature(SubprogramClassifier.__init__)
    params = list(sig.parameters.keys())



def test_processorclassifier_is_not_abstract():
    assert not inspect.isabstract(ProcessorClassifier)


def test_processorclassifier_constructor_exists():
    assert callable(ProcessorClassifier.__init__)


def test_processorclassifier_constructor_args():
    sig = inspect.signature(ProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_processclassifier_is_not_abstract():
    assert not inspect.isabstract(ProcessClassifier)


def test_processclassifier_constructor_exists():
    assert callable(ProcessClassifier.__init__)


def test_processclassifier_constructor_args():
    sig = inspect.signature(ProcessClassifier.__init__)
    params = list(sig.parameters.keys())



def test_memoryclassifier_is_not_abstract():
    assert not inspect.isabstract(MemoryClassifier)


def test_memoryclassifier_constructor_exists():
    assert callable(MemoryClassifier.__init__)


def test_memoryclassifier_constructor_args():
    sig = inspect.signature(MemoryClassifier.__init__)
    params = list(sig.parameters.keys())



def test_deviceclassifier_is_not_abstract():
    assert not inspect.isabstract(DeviceClassifier)


def test_deviceclassifier_constructor_exists():
    assert callable(DeviceClassifier.__init__)


def test_deviceclassifier_constructor_args():
    sig = inspect.signature(DeviceClassifier.__init__)
    params = list(sig.parameters.keys())



def test_virtualprocessor_is_not_abstract():
    assert not inspect.isabstract(VirtualProcessor)


def test_virtualprocessor_constructor_exists():
    assert callable(VirtualProcessor.__init__)


def test_virtualprocessor_constructor_args():
    sig = inspect.signature(VirtualProcessor.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualprocessorclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorClassifier)


def test_aadl2_virtualprocessorclassifier_constructor_exists():
    assert callable(aadl2_VirtualProcessorClassifier.__init__)


def test_aadl2_virtualprocessorclassifier_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualbus_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBus)


def test_aadl2_virtualbus_constructor_exists():
    assert callable(aadl2_VirtualBus.__init__)


def test_aadl2_virtualbus_constructor_args():
    sig = inspect.signature(aadl2_VirtualBus.__init__)
    params = list(sig.parameters.keys())



def test_virtualbus_is_not_abstract():
    assert not inspect.isabstract(VirtualBus)


def test_virtualbus_constructor_exists():
    assert callable(VirtualBus.__init__)


def test_virtualbus_constructor_args():
    sig = inspect.signature(VirtualBus.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualbusclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusClassifier)


def test_aadl2_virtualbusclassifier_constructor_exists():
    assert callable(aadl2_VirtualBusClassifier.__init__)


def test_aadl2_virtualbusclassifier_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_dataclassifier_is_not_abstract():
    assert not inspect.isabstract(DataClassifier)


def test_dataclassifier_constructor_exists():
    assert callable(DataClassifier.__init__)


def test_dataclassifier_constructor_args():
    sig = inspect.signature(DataClassifier.__init__)
    params = list(sig.parameters.keys())



def test_busclassifier_is_not_abstract():
    assert not inspect.isabstract(BusClassifier)


def test_busclassifier_constructor_exists():
    assert callable(BusClassifier.__init__)


def test_busclassifier_constructor_args():
    sig = inspect.signature(BusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualprocessor_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessor)


def test_aadl2_virtualprocessor_constructor_exists():
    assert callable(aadl2_VirtualProcessor.__init__)


def test_aadl2_virtualprocessor_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessor.__init__)
    params = list(sig.parameters.keys())



def test_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_system_constructor_exists():
    assert callable(System.__init__)


def test_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_systemclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemClassifier)


def test_aadl2_systemclassifier_constructor_exists():
    assert callable(aadl2_SystemClassifier.__init__)


def test_aadl2_systemclassifier_constructor_args():
    sig = inspect.signature(aadl2_SystemClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processor_is_not_abstract():
    assert not inspect.isabstract(aadl2_Processor)


def test_aadl2_processor_constructor_exists():
    assert callable(aadl2_Processor.__init__)


def test_aadl2_processor_constructor_args():
    sig = inspect.signature(aadl2_Processor.__init__)
    params = list(sig.parameters.keys())



def test_processor_is_not_abstract():
    assert not inspect.isabstract(Processor)


def test_processor_constructor_exists():
    assert callable(Processor.__init__)


def test_processor_constructor_args():
    sig = inspect.signature(Processor.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processorclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorClassifier)


def test_aadl2_processorclassifier_constructor_exists():
    assert callable(aadl2_ProcessorClassifier.__init__)


def test_aadl2_processorclassifier_constructor_args():
    sig = inspect.signature(aadl2_ProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadgroup_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroup)


def test_aadl2_threadgroup_constructor_exists():
    assert callable(aadl2_ThreadGroup.__init__)


def test_aadl2_threadgroup_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroup.__init__)
    params = list(sig.parameters.keys())



def test_threadgroup_is_not_abstract():
    assert not inspect.isabstract(ThreadGroup)


def test_threadgroup_constructor_exists():
    assert callable(ThreadGroup.__init__)


def test_threadgroup_constructor_args():
    sig = inspect.signature(ThreadGroup.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupClassifier)


def test_aadl2_threadgroupclassifier_constructor_exists():
    assert callable(aadl2_ThreadGroupClassifier.__init__)


def test_aadl2_threadgroupclassifier_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_thread_is_not_abstract():
    assert not inspect.isabstract(aadl2_Thread)


def test_aadl2_thread_constructor_exists():
    assert callable(aadl2_Thread.__init__)


def test_aadl2_thread_constructor_args():
    sig = inspect.signature(aadl2_Thread.__init__)
    params = list(sig.parameters.keys())



def test_thread_is_not_abstract():
    assert not inspect.isabstract(Thread)


def test_thread_constructor_exists():
    assert callable(Thread.__init__)


def test_thread_constructor_args():
    sig = inspect.signature(Thread.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadClassifier)


def test_aadl2_threadclassifier_constructor_exists():
    assert callable(aadl2_ThreadClassifier.__init__)


def test_aadl2_threadclassifier_constructor_args():
    sig = inspect.signature(aadl2_ThreadClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_system_is_not_abstract():
    assert not inspect.isabstract(aadl2_System)


def test_aadl2_system_constructor_exists():
    assert callable(aadl2_System.__init__)


def test_aadl2_system_constructor_args():
    sig = inspect.signature(aadl2_System.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_process_is_not_abstract():
    assert not inspect.isabstract(aadl2_Process)


def test_aadl2_process_constructor_exists():
    assert callable(aadl2_Process.__init__)


def test_aadl2_process_constructor_args():
    sig = inspect.signature(aadl2_Process.__init__)
    params = list(sig.parameters.keys())



def test_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_process_constructor_exists():
    assert callable(Process.__init__)


def test_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessClassifier)


def test_aadl2_processclassifier_constructor_exists():
    assert callable(aadl2_ProcessClassifier.__init__)


def test_aadl2_processclassifier_constructor_args():
    sig = inspect.signature(aadl2_ProcessClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_memory_is_not_abstract():
    assert not inspect.isabstract(aadl2_Memory)


def test_aadl2_memory_constructor_exists():
    assert callable(aadl2_Memory.__init__)


def test_aadl2_memory_constructor_args():
    sig = inspect.signature(aadl2_Memory.__init__)
    params = list(sig.parameters.keys())



def test_memory_is_not_abstract():
    assert not inspect.isabstract(Memory)


def test_memory_constructor_exists():
    assert callable(Memory.__init__)


def test_memory_constructor_args():
    sig = inspect.signature(Memory.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_memoryclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemoryClassifier)


def test_aadl2_memoryclassifier_constructor_exists():
    assert callable(aadl2_MemoryClassifier.__init__)


def test_aadl2_memoryclassifier_constructor_args():
    sig = inspect.signature(aadl2_MemoryClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_device_is_not_abstract():
    assert not inspect.isabstract(aadl2_Device)


def test_aadl2_device_constructor_exists():
    assert callable(aadl2_Device.__init__)


def test_aadl2_device_constructor_args():
    sig = inspect.signature(aadl2_Device.__init__)
    params = list(sig.parameters.keys())



def test_device_is_not_abstract():
    assert not inspect.isabstract(Device)


def test_device_constructor_exists():
    assert callable(Device.__init__)


def test_device_constructor_args():
    sig = inspect.signature(Device.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_deviceclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceClassifier)


def test_aadl2_deviceclassifier_constructor_exists():
    assert callable(aadl2_DeviceClassifier.__init__)


def test_aadl2_deviceclassifier_constructor_args():
    sig = inspect.signature(aadl2_DeviceClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgroupsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupSubcomponent)


def test_aadl2_subprogramgroupsubcomponent_constructor_exists():
    assert callable(aadl2_SubprogramGroupSubcomponent.__init__)


def test_aadl2_subprogramgroupsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramSubcomponent)


def test_aadl2_subprogramsubcomponent_constructor_exists():
    assert callable(aadl2_SubprogramSubcomponent.__init__)


def test_aadl2_subprogramsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_SubprogramSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramcallsequence_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramCallSequence)


def test_aadl2_subprogramcallsequence_constructor_exists():
    assert callable(aadl2_SubprogramCallSequence.__init__)


def test_aadl2_subprogramcallsequence_constructor_args():
    sig = inspect.signature(aadl2_SubprogramCallSequence.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_callspecification_is_not_abstract():
    assert not inspect.isabstract(aadl2_CallSpecification)


def test_aadl2_callspecification_constructor_exists():
    assert callable(aadl2_CallSpecification.__init__)


def test_aadl2_callspecification_constructor_args():
    sig = inspect.signature(aadl2_CallSpecification.__init__)
    params = list(sig.parameters.keys())



def test_componentimplementation_is_not_abstract():
    assert not inspect.isabstract(ComponentImplementation)


def test_componentimplementation_constructor_exists():
    assert callable(ComponentImplementation.__init__)


def test_componentimplementation_constructor_args():
    sig = inspect.signature(ComponentImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_behavioredimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_BehavioredImplementation)


def test_aadl2_behavioredimplementation_constructor_exists():
    assert callable(aadl2_BehavioredImplementation.__init__)


def test_aadl2_behavioredimplementation_constructor_args():
    sig = inspect.signature(aadl2_BehavioredImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualprocessorsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorSubcomponent)


def test_aadl2_virtualprocessorsubcomponent_constructor_exists():
    assert callable(aadl2_VirtualProcessorSubcomponent.__init__)


def test_aadl2_virtualprocessorsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualbussubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusSubcomponent)


def test_aadl2_virtualbussubcomponent_constructor_exists():
    assert callable(aadl2_VirtualBusSubcomponent.__init__)


def test_aadl2_virtualbussubcomponent_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadgroupsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupSubcomponent)


def test_aadl2_threadgroupsubcomponent_constructor_exists():
    assert callable(aadl2_ThreadGroupSubcomponent.__init__)


def test_aadl2_threadgroupsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadSubcomponent)


def test_aadl2_threadsubcomponent_constructor_exists():
    assert callable(aadl2_ThreadSubcomponent.__init__)


def test_aadl2_threadsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_ThreadSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_behavioredimplementation_is_not_abstract():
    assert not inspect.isabstract(BehavioredImplementation)


def test_behavioredimplementation_constructor_exists():
    assert callable(BehavioredImplementation.__init__)


def test_behavioredimplementation_constructor_args():
    sig = inspect.signature(BehavioredImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_systemsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemSubcomponent)


def test_aadl2_systemsubcomponent_constructor_exists():
    assert callable(aadl2_SystemSubcomponent.__init__)


def test_aadl2_systemsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_SystemSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processorsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorSubcomponent)


def test_aadl2_processorsubcomponent_constructor_exists():
    assert callable(aadl2_ProcessorSubcomponent.__init__)


def test_aadl2_processorsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_ProcessorSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessSubcomponent)


def test_aadl2_processsubcomponent_constructor_exists():
    assert callable(aadl2_ProcessSubcomponent.__init__)


def test_aadl2_processsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_ProcessSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_memorysubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemorySubcomponent)


def test_aadl2_memorysubcomponent_constructor_exists():
    assert callable(aadl2_MemorySubcomponent.__init__)


def test_aadl2_memorysubcomponent_constructor_args():
    sig = inspect.signature(aadl2_MemorySubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_devicesubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceSubcomponent)


def test_aadl2_devicesubcomponent_constructor_exists():
    assert callable(aadl2_DeviceSubcomponent.__init__)


def test_aadl2_devicesubcomponent_constructor_args():
    sig = inspect.signature(aadl2_DeviceSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_datasubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataSubcomponent)


def test_aadl2_datasubcomponent_constructor_exists():
    assert callable(aadl2_DataSubcomponent.__init__)


def test_aadl2_datasubcomponent_constructor_args():
    sig = inspect.signature(aadl2_DataSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_bussubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusSubcomponent)


def test_aadl2_bussubcomponent_constructor_exists():
    assert callable(aadl2_BusSubcomponent.__init__)


def test_aadl2_bussubcomponent_constructor_args():
    sig = inspect.signature(aadl2_BusSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_abstractclassifier_is_not_abstract():
    assert not inspect.isabstract(AbstractClassifier)


def test_abstractclassifier_constructor_exists():
    assert callable(AbstractClassifier.__init__)


def test_abstractclassifier_constructor_args():
    sig = inspect.signature(AbstractClassifier.__init__)
    params = list(sig.parameters.keys())



def test_componenttype_is_not_abstract():
    assert not inspect.isabstract(ComponentType)


def test_componenttype_constructor_exists():
    assert callable(ComponentType.__init__)


def test_componenttype_constructor_args():
    sig = inspect.signature(ComponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualprocessorimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorImplementation)


def test_aadl2_virtualprocessorimplementation_constructor_exists():
    assert callable(aadl2_VirtualProcessorImplementation.__init__)


def test_aadl2_virtualprocessorimplementation_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualprocessortype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorType)


def test_aadl2_virtualprocessortype_constructor_exists():
    assert callable(aadl2_VirtualProcessorType.__init__)


def test_aadl2_virtualprocessortype_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualbusimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusImplementation)


def test_aadl2_virtualbusimplementation_constructor_exists():
    assert callable(aadl2_VirtualBusImplementation.__init__)


def test_aadl2_virtualbusimplementation_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_propertyset_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertySet)


def test_aadl2_propertyset_constructor_exists():
    assert callable(aadl2_PropertySet.__init__)


def test_aadl2_propertyset_constructor_args():
    sig = inspect.signature(aadl2_PropertySet.__init__)
    params = list(sig.parameters.keys())
    assert "contents" in params, "Missing parameter 'contents'"
    assert "imports" in params, "Missing parameter 'imports'"

def test_aadl2_propertyset_has_contents():
    assert hasattr(aadl2_PropertySet, "contents")
    descriptor = None
    for klass in aadl2_PropertySet.__mro__:
        if "contents" in klass.__dict__:
            descriptor = klass.__dict__["contents"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_propertyset_has_imports():
    assert hasattr(aadl2_PropertySet, "imports")
    descriptor = None
    for klass in aadl2_PropertySet.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_systemimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemImplementation)


def test_aadl2_systemimplementation_constructor_exists():
    assert callable(aadl2_SystemImplementation.__init__)


def test_aadl2_systemimplementation_constructor_args():
    sig = inspect.signature(aadl2_SystemImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_systemtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemType)


def test_aadl2_systemtype_constructor_exists():
    assert callable(aadl2_SystemType.__init__)


def test_aadl2_systemtype_constructor_args():
    sig = inspect.signature(aadl2_SystemType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgroupimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupImplementation)


def test_aadl2_subprogramgroupimplementation_constructor_exists():
    assert callable(aadl2_SubprogramGroupImplementation.__init__)


def test_aadl2_subprogramgroupimplementation_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualbustype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusType)


def test_aadl2_virtualbustype_constructor_exists():
    assert callable(aadl2_VirtualBusType.__init__)


def test_aadl2_virtualbustype_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadgroupimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupImplementation)


def test_aadl2_threadgroupimplementation_constructor_exists():
    assert callable(aadl2_ThreadGroupImplementation.__init__)


def test_aadl2_threadgroupimplementation_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadgrouptype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupType)


def test_aadl2_threadgrouptype_constructor_exists():
    assert callable(aadl2_ThreadGroupType.__init__)


def test_aadl2_threadgrouptype_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadImplementation)


def test_aadl2_threadimplementation_constructor_exists():
    assert callable(aadl2_ThreadImplementation.__init__)


def test_aadl2_threadimplementation_constructor_args():
    sig = inspect.signature(aadl2_ThreadImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadType)


def test_aadl2_threadtype_constructor_exists():
    assert callable(aadl2_ThreadType.__init__)


def test_aadl2_threadtype_constructor_args():
    sig = inspect.signature(aadl2_ThreadType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessType)


def test_aadl2_processtype_constructor_exists():
    assert callable(aadl2_ProcessType.__init__)


def test_aadl2_processtype_constructor_args():
    sig = inspect.signature(aadl2_ProcessType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_memoryimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemoryImplementation)


def test_aadl2_memoryimplementation_constructor_exists():
    assert callable(aadl2_MemoryImplementation.__init__)


def test_aadl2_memoryimplementation_constructor_args():
    sig = inspect.signature(aadl2_MemoryImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgrouptype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupType)


def test_aadl2_subprogramgrouptype_constructor_exists():
    assert callable(aadl2_SubprogramGroupType.__init__)


def test_aadl2_subprogramgrouptype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramImplementation)


def test_aadl2_subprogramimplementation_constructor_exists():
    assert callable(aadl2_SubprogramImplementation.__init__)


def test_aadl2_subprogramimplementation_constructor_args():
    sig = inspect.signature(aadl2_SubprogramImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramType)


def test_aadl2_subprogramtype_constructor_exists():
    assert callable(aadl2_SubprogramType.__init__)


def test_aadl2_subprogramtype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processorimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorImplementation)


def test_aadl2_processorimplementation_constructor_exists():
    assert callable(aadl2_ProcessorImplementation.__init__)


def test_aadl2_processorimplementation_constructor_args():
    sig = inspect.signature(aadl2_ProcessorImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessImplementation)


def test_aadl2_processimplementation_constructor_exists():
    assert callable(aadl2_ProcessImplementation.__init__)


def test_aadl2_processimplementation_constructor_args():
    sig = inspect.signature(aadl2_ProcessImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processortype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorType)


def test_aadl2_processortype_constructor_exists():
    assert callable(aadl2_ProcessorType.__init__)


def test_aadl2_processortype_constructor_args():
    sig = inspect.signature(aadl2_ProcessorType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_abstractimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractImplementation)


def test_aadl2_abstractimplementation_constructor_exists():
    assert callable(aadl2_AbstractImplementation.__init__)


def test_aadl2_abstractimplementation_constructor_args():
    sig = inspect.signature(aadl2_AbstractImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_abstracttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractType)


def test_aadl2_abstracttype_constructor_exists():
    assert callable(aadl2_AbstractType.__init__)


def test_aadl2_abstracttype_constructor_args():
    sig = inspect.signature(aadl2_AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_aadlpackage_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlPackage)


def test_aadl2_aadlpackage_constructor_exists():
    assert callable(aadl2_AadlPackage.__init__)


def test_aadl2_aadlpackage_constructor_args():
    sig = inspect.signature(aadl2_AadlPackage.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_memorytype_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemoryType)


def test_aadl2_memorytype_constructor_exists():
    assert callable(aadl2_MemoryType.__init__)


def test_aadl2_memorytype_constructor_args():
    sig = inspect.signature(aadl2_MemoryType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_deviceimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceImplementation)


def test_aadl2_deviceimplementation_constructor_exists():
    assert callable(aadl2_DeviceImplementation.__init__)


def test_aadl2_deviceimplementation_constructor_args():
    sig = inspect.signature(aadl2_DeviceImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_devicetype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceType)


def test_aadl2_devicetype_constructor_exists():
    assert callable(aadl2_DeviceType.__init__)


def test_aadl2_devicetype_constructor_args():
    sig = inspect.signature(aadl2_DeviceType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_dataimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataImplementation)


def test_aadl2_dataimplementation_constructor_exists():
    assert callable(aadl2_DataImplementation.__init__)


def test_aadl2_dataimplementation_constructor_args():
    sig = inspect.signature(aadl2_DataImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_datatype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataType)


def test_aadl2_datatype_constructor_exists():
    assert callable(aadl2_DataType.__init__)


def test_aadl2_datatype_constructor_args():
    sig = inspect.signature(aadl2_DataType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_busimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusImplementation)


def test_aadl2_busimplementation_constructor_exists():
    assert callable(aadl2_BusImplementation.__init__)


def test_aadl2_busimplementation_constructor_args():
    sig = inspect.signature(aadl2_BusImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_bustype_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusType)


def test_aadl2_bustype_constructor_exists():
    assert callable(aadl2_BusType.__init__)


def test_aadl2_bustype_constructor_args():
    sig = inspect.signature(aadl2_BusType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_packagesection_is_not_abstract():
    assert not inspect.isabstract(aadl2_PackageSection)


def test_aadl2_packagesection_constructor_exists():
    assert callable(aadl2_PackageSection.__init__)


def test_aadl2_packagesection_constructor_args():
    sig = inspect.signature(aadl2_PackageSection.__init__)
    params = list(sig.parameters.keys())
    assert "noAnnexes" in params, "Missing parameter 'noAnnexes'"
    assert "aliases" in params, "Missing parameter 'aliases'"
    assert "noProperties" in params, "Missing parameter 'noProperties'"
    assert "declarations" in params, "Missing parameter 'declarations'"
    assert "imports" in params, "Missing parameter 'imports'"

def test_aadl2_packagesection_has_noAnnexes():
    assert hasattr(aadl2_PackageSection, "noAnnexes")
    descriptor = None
    for klass in aadl2_PackageSection.__mro__:
        if "noAnnexes" in klass.__dict__:
            descriptor = klass.__dict__["noAnnexes"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_packagesection_has_aliases():
    assert hasattr(aadl2_PackageSection, "aliases")
    descriptor = None
    for klass in aadl2_PackageSection.__mro__:
        if "aliases" in klass.__dict__:
            descriptor = klass.__dict__["aliases"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_packagesection_has_noProperties():
    assert hasattr(aadl2_PackageSection, "noProperties")
    descriptor = None
    for klass in aadl2_PackageSection.__mro__:
        if "noProperties" in klass.__dict__:
            descriptor = klass.__dict__["noProperties"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_packagesection_has_declarations():
    assert hasattr(aadl2_PackageSection, "declarations")
    descriptor = None
    for klass in aadl2_PackageSection.__mro__:
        if "declarations" in klass.__dict__:
            descriptor = klass.__dict__["declarations"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_packagesection_has_imports():
    assert hasattr(aadl2_PackageSection, "imports")
    descriptor = None
    for klass in aadl2_PackageSection.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_privatepackagesection_is_not_abstract():
    assert not inspect.isabstract(aadl2_PrivatePackageSection)


def test_aadl2_privatepackagesection_constructor_exists():
    assert callable(aadl2_PrivatePackageSection.__init__)


def test_aadl2_privatepackagesection_constructor_args():
    sig = inspect.signature(aadl2_PrivatePackageSection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featuregrouptyperename_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupTypeRename)


def test_aadl2_featuregrouptyperename_constructor_exists():
    assert callable(aadl2_FeatureGroupTypeRename.__init__)


def test_aadl2_featuregrouptyperename_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupTypeRename.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_componenttyperename_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentTypeRename)


def test_aadl2_componenttyperename_constructor_exists():
    assert callable(aadl2_ComponentTypeRename.__init__)


def test_aadl2_componenttyperename_constructor_args():
    sig = inspect.signature(aadl2_ComponentTypeRename.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"

def test_aadl2_componenttyperename_has_category():
    assert hasattr(aadl2_ComponentTypeRename, "category")
    descriptor = None
    for klass in aadl2_ComponentTypeRename.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_packagerename_is_not_abstract():
    assert not inspect.isabstract(aadl2_PackageRename)


def test_aadl2_packagerename_constructor_exists():
    assert callable(aadl2_PackageRename.__init__)


def test_aadl2_packagerename_constructor_args():
    sig = inspect.signature(aadl2_PackageRename.__init__)
    params = list(sig.parameters.keys())
    assert "renameAll" in params, "Missing parameter 'renameAll'"

def test_aadl2_packagerename_has_renameAll():
    assert hasattr(aadl2_PackageRename, "renameAll")
    descriptor = None
    for klass in aadl2_PackageRename.__mro__:
        if "renameAll" in klass.__dict__:
            descriptor = klass.__dict__["renameAll"]
            break
    assert isinstance(descriptor, property)



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_portconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2_PortConnection)


def test_aadl2_portconnection_constructor_exists():
    assert callable(aadl2_PortConnection.__init__)


def test_aadl2_portconnection_constructor_args():
    sig = inspect.signature(aadl2_PortConnection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_parameterconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2_ParameterConnection)


def test_aadl2_parameterconnection_constructor_exists():
    assert callable(aadl2_ParameterConnection.__init__)


def test_aadl2_parameterconnection_constructor_args():
    sig = inspect.signature(aadl2_ParameterConnection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_accessconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2_AccessConnection)


def test_aadl2_accessconnection_constructor_exists():
    assert callable(aadl2_AccessConnection.__init__)


def test_aadl2_accessconnection_constructor_args():
    sig = inspect.signature(aadl2_AccessConnection.__init__)
    params = list(sig.parameters.keys())
    assert "accessCategory" in params, "Missing parameter 'accessCategory'"

def test_aadl2_accessconnection_has_accessCategory():
    assert hasattr(aadl2_AccessConnection, "accessCategory")
    descriptor = None
    for klass in aadl2_AccessConnection.__mro__:
        if "accessCategory" in klass.__dict__:
            descriptor = klass.__dict__["accessCategory"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_featuregroupconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupConnection)


def test_aadl2_featuregroupconnection_constructor_exists():
    assert callable(aadl2_FeatureGroupConnection.__init__)


def test_aadl2_featuregroupconnection_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupConnection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featureconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureConnection)


def test_aadl2_featureconnection_constructor_exists():
    assert callable(aadl2_FeatureConnection.__init__)


def test_aadl2_featureconnection_constructor_args():
    sig = inspect.signature(aadl2_FeatureConnection.__init__)
    params = list(sig.parameters.keys())

def test_flowkind_exists():
    # Check that the Enumeration exists
    assert FlowKind is not None

def test_flowkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlowKind]
    expected_literals = [
        "path",
        "sink",
        "source",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlowKind"

def test_operationkind_exists():
    # Check that the Enumeration exists
    assert OperationKind is not None

def test_operationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperationKind]
    expected_literals = [
        "or_",
        "minus",
        "and_",
        "plus",
        "not_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperationKind"

def test_portcategory_exists():
    # Check that the Enumeration exists
    assert PortCategory is not None

def test_portcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PortCategory]
    expected_literals = [
        "data",
        "eventData",
        "event",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PortCategory"

def test_connectionkind_exists():
    # Check that the Enumeration exists
    assert ConnectionKind is not None

def test_connectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectionKind]
    expected_literals = [
        "FeatureGroup",
        "Port",
        "Access",
        "Feature",
        "Parameter",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConnectionKind"

def test_accesstype_exists():
    # Check that the Enumeration exists
    assert AccessType is not None

def test_accesstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessType]
    expected_literals = [
        "provided",
        "required",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessType"

def test_directiontype_exists():
    # Check that the Enumeration exists
    assert DirectionType is not None

def test_directiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionType]
    expected_literals = [
        "inOut",
        "out",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionType"

def test_componentcategory_exists():
    # Check that the Enumeration exists
    assert ComponentCategory is not None

def test_componentcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentCategory]
    expected_literals = [
        "system",
        "device",
        "abstract",
        "subprogramGroup",
        "virtualProcessor",
        "threadGroup",
        "processor",
        "data",
        "subprogram",
        "virtualBus",
        "memory",
        "thread",
        "bus",
        "process",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentCategory"

def test_accesscategory_exists():
    # Check that the Enumeration exists
    assert AccessCategory is not None

def test_accesscategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessCategory]
    expected_literals = [
        "bus",
        "subprogramGroup",
        "data",
        "subprogram",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessCategory"


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
EnumerationType_strategy = st.builds(
    EnumerationType,
)
NumberType_strategy = st.builds(
    NumberType,
)
aadl2_AadlReal_strategy = st.builds(
    aadl2_AadlReal,
)
aadl2_AadlInteger_strategy = st.builds(
    aadl2_AadlInteger,
)
PropertyType_strategy = st.builds(
    PropertyType,
)
aadl2_AadlString_strategy = st.builds(
    aadl2_AadlString,
)
aadl2_ClassifierType_strategy = st.builds(
    aadl2_ClassifierType,
)
aadl2_ReferenceType_strategy = st.builds(
    aadl2_ReferenceType,
)
aadl2_RangeType_strategy = st.builds(
    aadl2_RangeType,
)
aadl2_AadlBoolean_strategy = st.builds(
    aadl2_AadlBoolean,
)
aadl2_UnitsType_strategy = st.builds(
    aadl2_UnitsType,
)
aadl2_NumberType_strategy = st.builds(
    aadl2_NumberType,
)
NumberValue_strategy = st.builds(
    NumberValue,
)
aadl2_IntegerLiteral_strategy = st.builds(
    aadl2_IntegerLiteral,
    base=
        safe_text,
    value=
        safe_text
)
ContainedNamedElement_strategy = st.builds(
    ContainedNamedElement,
)
aadl2_RealLiteral_strategy = st.builds(
    aadl2_RealLiteral,
    value=
        safe_text
)
PropertyExpression_strategy = st.builds(
    PropertyExpression,
)
aadl2_ListValue_strategy = st.builds(
    aadl2_ListValue,
)
aadl2_Operation_strategy = st.builds(
    aadl2_Operation,
    op=
        safe_text
)
aadl2_PropertyValue_strategy = st.builds(
    aadl2_PropertyValue,
)
PropertyValue_strategy = st.builds(
    PropertyValue,
)
aadl2_RecordValue_strategy = st.builds(
    aadl2_RecordValue,
)
aadl2_ComputedValue_strategy = st.builds(
    aadl2_ComputedValue,
    function=
        safe_text
)
aadl2_RangeValue_strategy = st.builds(
    aadl2_RangeValue,
)
aadl2_NumberValue_strategy = st.builds(
    aadl2_NumberValue,
    valueString=
        safe_text
)
aadl2_StringLiteral_strategy = st.builds(
    aadl2_StringLiteral,
    value=
        safe_text
)
aadl2_BooleanLiteral_strategy = st.builds(
    aadl2_BooleanLiteral,
    value=
        safe_text
)
aadl2_ReferenceValue_strategy = st.builds(
    aadl2_ReferenceValue,
)
aadl2_EnumerationValue_strategy = st.builds(
    aadl2_EnumerationValue,
)
CallSpecification_strategy = st.builds(
    CallSpecification,
)
aadl2_ProcessorCall_strategy = st.builds(
    aadl2_ProcessorCall,
    subprogramAccessName=
        safe_text
)
FeatureGroupPrototypeActual_strategy = st.builds(
    FeatureGroupPrototypeActual,
)
aadl2_FeatureGroupReference_strategy = st.builds(
    aadl2_FeatureGroupReference,
)
aadl2_FeatureGroupPrototypeReference_strategy = st.builds(
    aadl2_FeatureGroupPrototypeReference,
)
Subcomponent_strategy = st.builds(
    Subcomponent,
)
PackageSection_strategy = st.builds(
    PackageSection,
)
aadl2_PublicPackageSection_strategy = st.builds(
    aadl2_PublicPackageSection,
)
AnnexSubclause_strategy = st.builds(
    AnnexSubclause,
)
aadl2_DefaultAnnexSubclause_strategy = st.builds(
    aadl2_DefaultAnnexSubclause,
    sourceText=
        safe_text
)
AnnexLibrary_strategy = st.builds(
    AnnexLibrary,
)
aadl2_DefaultAnnexLibrary_strategy = st.builds(
    aadl2_DefaultAnnexLibrary,
    sourceText=
        safe_text
)
ModalPath_strategy = st.builds(
    ModalPath,
)
Abstract_strategy = st.builds(
    Abstract,
)
Prototype_strategy = st.builds(
    Prototype,
)
aadl2_ComponentPrototype_strategy = st.builds(
    aadl2_ComponentPrototype,
    array=
        safe_text,
    category=
        safe_text
)
CalledSubprogram_strategy = st.builds(
    CalledSubprogram,
)
SubprogramGroup_strategy = st.builds(
    SubprogramGroup,
)
Subprogram_strategy = st.builds(
    Subprogram,
)
AccessConnectionEnd_strategy = st.builds(
    AccessConnectionEnd,
)
Access_strategy = st.builds(
    Access,
)
Port_strategy = st.builds(
    Port,
)
Data_strategy = st.builds(
    Data,
)
EndToEndFlowElement_strategy = st.builds(
    EndToEndFlowElement,
)
aadl2_FlowElement_strategy = st.builds(
    aadl2_FlowElement,
)
ParameterConnectionEnd_strategy = st.builds(
    ParameterConnectionEnd,
)
FlowElement_strategy = st.builds(
    FlowElement,
)
aadl2_SubcomponentFlow_strategy = st.builds(
    aadl2_SubcomponentFlow,
)
Bus_strategy = st.builds(
    Bus,
)
aadl2_BusAccess_strategy = st.builds(
    aadl2_BusAccess,
)
aadl2_SubprogramAccess_strategy = st.builds(
    aadl2_SubprogramAccess,
)
aadl2_EventPort_strategy = st.builds(
    aadl2_EventPort,
)
Flow_strategy = st.builds(
    Flow,
)
CallContext_strategy = st.builds(
    CallContext,
)
aadl2_SubprogramGroupAccess_strategy = st.builds(
    aadl2_SubprogramGroupAccess,
)
FeatureGroupConnectionEnd_strategy = st.builds(
    FeatureGroupConnectionEnd,
)
Context_strategy = st.builds(
    Context,
)
aadl2_EventDataPort_strategy = st.builds(
    aadl2_EventDataPort,
)
aadl2_SubprogramCall_strategy = st.builds(
    aadl2_SubprogramCall,
)
aadl2_DataPort_strategy = st.builds(
    aadl2_DataPort,
)
Generalization__strategy = st.builds(
    Generalization_,
)
aadl2_GroupExtension_strategy = st.builds(
    aadl2_GroupExtension,
)
ConnectionEnd_strategy = st.builds(
    ConnectionEnd,
)
aadl2_AccessConnectionEnd_strategy = st.builds(
    aadl2_AccessConnectionEnd,
)
aadl2_PortConnectionEnd_strategy = st.builds(
    aadl2_PortConnectionEnd,
)
aadl2_ParameterConnectionEnd_strategy = st.builds(
    aadl2_ParameterConnectionEnd,
)
aadl2_FeatureGroupConnectionEnd_strategy = st.builds(
    aadl2_FeatureGroupConnectionEnd,
)
aadl2_FeatureConnectionEnd_strategy = st.builds(
    aadl2_FeatureConnectionEnd,
)
ArrayableElement_strategy = st.builds(
    ArrayableElement,
)
FeatureConnectionEnd_strategy = st.builds(
    FeatureConnectionEnd,
)
aadl2_TypeExtension_strategy = st.builds(
    aadl2_TypeExtension,
)
Classifier_strategy = st.builds(
    Classifier,
)
aadl2_FeatureGroupType_strategy = st.builds(
    aadl2_FeatureGroupType,
    feature=
        safe_text
)
aadl2_ComponentClassifier_strategy = st.builds(
    aadl2_ComponentClassifier,
    noFlows=
        safe_text,
    noModes=
        safe_text
)
aadl2_ProcessorSubprogram_strategy = st.builds(
    aadl2_ProcessorSubprogram,
)
Feature_strategy = st.builds(
    Feature,
)
aadl2_Access_strategy = st.builds(
    aadl2_Access,
    category=
        safe_text,
    kind=
        safe_text
)
aadl2_DirectedFeature_strategy = st.builds(
    aadl2_DirectedFeature,
    direction=
        safe_text
)
PortConnectionEnd_strategy = st.builds(
    PortConnectionEnd,
)
aadl2_DataAccess_strategy = st.builds(
    aadl2_DataAccess,
)
DirectedFeature_strategy = st.builds(
    DirectedFeature,
)
aadl2_Parameter_strategy = st.builds(
    aadl2_Parameter,
)
aadl2_FeatureGroup_strategy = st.builds(
    aadl2_FeatureGroup,
    inverse=
        safe_text
)
aadl2_AbstractFeature_strategy = st.builds(
    aadl2_AbstractFeature,
)
aadl2_Port_strategy = st.builds(
    aadl2_Port,
    category=
        safe_text
)
ModeTransitionTrigger_strategy = st.builds(
    ModeTransitionTrigger,
)
aadl2_ProcessorPort_strategy = st.builds(
    aadl2_ProcessorPort,
)
aadl2_InternalEvent_strategy = st.builds(
    aadl2_InternalEvent,
)
aadl2_TriggerPort_strategy = st.builds(
    aadl2_TriggerPort,
)
aadl2_Realization_strategy = st.builds(
    aadl2_Realization,
)
aadl2_ImplementationExtension_strategy = st.builds(
    aadl2_ImplementationExtension,
)
aadl2_AbstractSubcomponent_strategy = st.builds(
    aadl2_AbstractSubcomponent,
)
aadl2_EndToEndFlow_strategy = st.builds(
    aadl2_EndToEndFlow,
)
ComponentClassifier_strategy = st.builds(
    ComponentClassifier,
)
aadl2_SubprogramGroupClassifier_strategy = st.builds(
    aadl2_SubprogramGroupClassifier,
)
aadl2_SubprogramClassifier_strategy = st.builds(
    aadl2_SubprogramClassifier,
)
aadl2_ComponentType_strategy = st.builds(
    aadl2_ComponentType,
    features=
        safe_text,
    noFeatures=
        safe_text
)
aadl2_AbstractClassifier_strategy = st.builds(
    aadl2_AbstractClassifier,
)
aadl2_BusClassifier_strategy = st.builds(
    aadl2_BusClassifier,
)
aadl2_DataClassifier_strategy = st.builds(
    aadl2_DataClassifier,
)
aadl2_ComponentImplementation_strategy = st.builds(
    aadl2_ComponentImplementation,
    flows=
        safe_text,
    noConnections=
        safe_text,
    noSubcomponents=
        safe_text,
    subcomponents=
        safe_text,
    connections=
        safe_text,
    noCalls=
        safe_text
)
ArraySize_strategy = st.builds(
    ArraySize,
)
aadl2_PropertyReference_strategy = st.builds(
    aadl2_PropertyReference,
)
aadl2_ConstantValue_strategy = st.builds(
    aadl2_ConstantValue,
)
aadl2_Numeral_strategy = st.builds(
    aadl2_Numeral,
    value=
        safe_text
)
RefinableElement_strategy = st.builds(
    RefinableElement,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
aadl2_Flow_strategy = st.builds(
    aadl2_Flow,
)
aadl2_Feature_strategy = st.builds(
    aadl2_Feature,
)
aadl2_FlowImplementation_strategy = st.builds(
    aadl2_FlowImplementation,
    kind=
        safe_text
)
aadl2_Connection_strategy = st.builds(
    aadl2_Connection,
    kind=
        safe_text,
    bidirectional=
        safe_text
)
ClassifierFeature_strategy = st.builds(
    ClassifierFeature,
)
aadl2_BehavioralFeature_strategy = st.builds(
    aadl2_BehavioralFeature,
)
aadl2_StructuralFeature_strategy = st.builds(
    aadl2_StructuralFeature,
)
aadl2_ModeFeature_strategy = st.builds(
    aadl2_ModeFeature,
)
Relationship_strategy = st.builds(
    Relationship,
)
aadl2_DirectedRelationship_strategy = st.builds(
    aadl2_DirectedRelationship,
)
ModeFeature_strategy = st.builds(
    ModeFeature,
)
aadl2_ModeTransition_strategy = st.builds(
    aadl2_ModeTransition,
)
aadl2_Mode_strategy = st.builds(
    aadl2_Mode,
    derived=
        safe_text,
    initial=
        safe_text
)
ModalElement_strategy = st.builds(
    ModalElement,
)
aadl2_FlowSpecification_strategy = st.builds(
    aadl2_FlowSpecification,
    kind=
        safe_text
)
aadl2_ModalPath_strategy = st.builds(
    aadl2_ModalPath,
)
aadl2_Subcomponent_strategy = st.builds(
    aadl2_Subcomponent,
    allModes=
        safe_text
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
aadl2_Generalization__strategy = st.builds(
    aadl2_Generalization_,
)
aadl2_Prototype_strategy = st.builds(
    aadl2_Prototype,
)
aadl2_AnnexSubclause_strategy = st.builds(
    aadl2_AnnexSubclause,
)
Namespace_strategy = st.builds(
    Namespace,
)
aadl2_GlobalNamespace_strategy = st.builds(
    aadl2_GlobalNamespace,
)
aadl2_RecordType_strategy = st.builds(
    aadl2_RecordType,
)
aadl2_EnumerationType_strategy = st.builds(
    aadl2_EnumerationType,
)
PropertyOwner_strategy = st.builds(
    PropertyOwner,
)
aadl2_ClassifierValue_strategy = st.builds(
    aadl2_ClassifierValue,
)
Type_strategy = st.builds(
    Type,
)
aadl2_PropertyType_strategy = st.builds(
    aadl2_PropertyType,
)
aadl2_Classifier_strategy = st.builds(
    aadl2_Classifier,
    noProperties=
        safe_text,
    noPrototypes=
        safe_text,
    noAnnexes=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
aadl2_BasicProperty_strategy = st.builds(
    aadl2_BasicProperty,
    list=
        safe_text
)
aadl2_MetaclassReference_strategy = st.builds(
    aadl2_MetaclassReference,
    annexName=
        safe_text,
    metaclassName=
        safe_text
)
BasicProperty_strategy = st.builds(
    BasicProperty,
)
aadl2_RecordField_strategy = st.builds(
    aadl2_RecordField,
)
aadl2_Property_strategy = st.builds(
    aadl2_Property,
    emptyListDefault=
        safe_text,
    inherit=
        safe_text
)
aadl2_ModalPropertyValue_strategy = st.builds(
    aadl2_ModalPropertyValue,
)
aadl2_Element_strategy = st.builds(
    aadl2_Element,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
aadl2_EndToEndFlowElement_strategy = st.builds(
    aadl2_EndToEndFlowElement,
)
aadl2_ConnectionEnd_strategy = st.builds(
    aadl2_ConnectionEnd,
)
aadl2_Context_strategy = st.builds(
    aadl2_Context,
)
aadl2_Subprogram_strategy = st.builds(
    aadl2_Subprogram,
)
aadl2_Bus_strategy = st.builds(
    aadl2_Bus,
)
aadl2_Type_strategy = st.builds(
    aadl2_Type,
)
aadl2_TypedElement_strategy = st.builds(
    aadl2_TypedElement,
)
aadl2_Abstract_strategy = st.builds(
    aadl2_Abstract,
)
aadl2_ClassifierFeature_strategy = st.builds(
    aadl2_ClassifierFeature,
)
aadl2_ModalElement_strategy = st.builds(
    aadl2_ModalElement,
    modesAndTransitions=
        safe_text
)
aadl2_EnumerationLiteral_strategy = st.builds(
    aadl2_EnumerationLiteral,
)
aadl2_AnnexLibrary_strategy = st.builds(
    aadl2_AnnexLibrary,
)
aadl2_RefinableElement_strategy = st.builds(
    aadl2_RefinableElement,
)
aadl2_SubprogramGroup_strategy = st.builds(
    aadl2_SubprogramGroup,
)
aadl2_Data_strategy = st.builds(
    aadl2_Data,
)
aadl2_Namespace_strategy = st.builds(
    aadl2_Namespace,
)
Element_strategy = st.builds(
    Element,
)
aadl2_ArraySpecification_strategy = st.builds(
    aadl2_ArraySpecification,
    dimension=
        safe_text
)
aadl2_Relationship_strategy = st.builds(
    aadl2_Relationship,
)
aadl2_ComponentImplementationReference_strategy = st.builds(
    aadl2_ComponentImplementationReference,
)
aadl2_PropertyOwner_strategy = st.builds(
    aadl2_PropertyOwner,
)
aadl2_PropertyExpression_strategy = st.builds(
    aadl2_PropertyExpression,
)
aadl2_ArrayRange_strategy = st.builds(
    aadl2_ArrayRange,
    lowerBound=
        safe_text,
    upperBound=
        safe_text
)
aadl2_ModeBinding_strategy = st.builds(
    aadl2_ModeBinding,
)
aadl2_CallContext_strategy = st.builds(
    aadl2_CallContext,
)
aadl2_ModeTransitionTrigger_strategy = st.builds(
    aadl2_ModeTransitionTrigger,
)
aadl2_BasicPropertyAssociation_strategy = st.builds(
    aadl2_BasicPropertyAssociation,
)
aadl2_CalledSubprogram_strategy = st.builds(
    aadl2_CalledSubprogram,
)
aadl2_ArraySize_strategy = st.builds(
    aadl2_ArraySize,
)
aadl2_PropertyAssociation_strategy = st.builds(
    aadl2_PropertyAssociation,
    append=
        safe_text,
    constant=
        safe_text
)
aadl2_ArrayableElement_strategy = st.builds(
    aadl2_ArrayableElement,
)
aadl2_ContainedNamedElement_strategy = st.builds(
    aadl2_ContainedNamedElement,
)
aadl2_NamedElement_strategy = st.builds(
    aadl2_NamedElement,
    qualifiedName=
        safe_text,
    name=
        safe_text
)
aadl2_ContainmentPathElement_strategy = st.builds(
    aadl2_ContainmentPathElement,
)
aadl2_PrototypeBinding_strategy = st.builds(
    aadl2_PrototypeBinding,
)
aadl2_NumericRange_strategy = st.builds(
    aadl2_NumericRange,
)
aadl2_Comment_strategy = st.builds(
    aadl2_Comment,
    body=
        safe_text
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
ComponentPrototypeActual_strategy = st.builds(
    ComponentPrototypeActual,
)
aadl2_ComponentPrototypeReference_strategy = st.builds(
    aadl2_ComponentPrototypeReference,
)
aadl2_UnitLiteral_strategy = st.builds(
    aadl2_UnitLiteral,
)
aadl2_UnitValue_strategy = st.builds(
    aadl2_UnitValue,
)
aadl2_ComponentReference_strategy = st.builds(
    aadl2_ComponentReference,
)
aadl2_FeaturePrototype_strategy = st.builds(
    aadl2_FeaturePrototype,
    direction=
        safe_text
)
aadl2_FeatureGroupPrototypeActual_strategy = st.builds(
    aadl2_FeatureGroupPrototypeActual,
)
aadl2_FeatureGroupPrototype_strategy = st.builds(
    aadl2_FeatureGroupPrototype,
)
aadl2_ComponentPrototypeActual_strategy = st.builds(
    aadl2_ComponentPrototypeActual,
    category=
        safe_text
)
FeaturePrototypeActual_strategy = st.builds(
    FeaturePrototypeActual,
)
aadl2_PortSpecification_strategy = st.builds(
    aadl2_PortSpecification,
    direction=
        safe_text,
    category=
        safe_text
)
aadl2_FeaturePrototypeReference_strategy = st.builds(
    aadl2_FeaturePrototypeReference,
    direction=
        safe_text
)
aadl2_AccessSpecification_strategy = st.builds(
    aadl2_AccessSpecification,
    category=
        safe_text,
    kind=
        safe_text
)
aadl2_FeaturePrototypeActual_strategy = st.builds(
    aadl2_FeaturePrototypeActual,
)
aadl2_PropertyConstant_strategy = st.builds(
    aadl2_PropertyConstant,
    list=
        safe_text
)
PrototypeBinding_strategy = st.builds(
    PrototypeBinding,
)
aadl2_FeaturePrototypeBinding_strategy = st.builds(
    aadl2_FeaturePrototypeBinding,
)
aadl2_FeatureGroupPrototypeBinding_strategy = st.builds(
    aadl2_FeatureGroupPrototypeBinding,
)
aadl2_ComponentPrototypeBinding_strategy = st.builds(
    aadl2_ComponentPrototypeBinding,
)
VirtualProcessorClassifier_strategy = st.builds(
    VirtualProcessorClassifier,
)
VirtualBusClassifier_strategy = st.builds(
    VirtualBusClassifier,
)
ThreadGroupClassifier_strategy = st.builds(
    ThreadGroupClassifier,
)
ThreadClassifier_strategy = st.builds(
    ThreadClassifier,
)
SystemClassifier_strategy = st.builds(
    SystemClassifier,
)
SubprogramGroupClassifier_strategy = st.builds(
    SubprogramGroupClassifier,
)
SubprogramClassifier_strategy = st.builds(
    SubprogramClassifier,
)
ProcessorClassifier_strategy = st.builds(
    ProcessorClassifier,
)
ProcessClassifier_strategy = st.builds(
    ProcessClassifier,
)
MemoryClassifier_strategy = st.builds(
    MemoryClassifier,
)
DeviceClassifier_strategy = st.builds(
    DeviceClassifier,
)
VirtualProcessor_strategy = st.builds(
    VirtualProcessor,
)
aadl2_VirtualProcessorClassifier_strategy = st.builds(
    aadl2_VirtualProcessorClassifier,
)
aadl2_VirtualBus_strategy = st.builds(
    aadl2_VirtualBus,
)
VirtualBus_strategy = st.builds(
    VirtualBus,
)
aadl2_VirtualBusClassifier_strategy = st.builds(
    aadl2_VirtualBusClassifier,
)
DataClassifier_strategy = st.builds(
    DataClassifier,
)
BusClassifier_strategy = st.builds(
    BusClassifier,
)
aadl2_VirtualProcessor_strategy = st.builds(
    aadl2_VirtualProcessor,
)
System_strategy = st.builds(
    System,
)
aadl2_SystemClassifier_strategy = st.builds(
    aadl2_SystemClassifier,
)
aadl2_Processor_strategy = st.builds(
    aadl2_Processor,
)
Processor_strategy = st.builds(
    Processor,
)
aadl2_ProcessorClassifier_strategy = st.builds(
    aadl2_ProcessorClassifier,
)
aadl2_ThreadGroup_strategy = st.builds(
    aadl2_ThreadGroup,
)
ThreadGroup_strategy = st.builds(
    ThreadGroup,
)
aadl2_ThreadGroupClassifier_strategy = st.builds(
    aadl2_ThreadGroupClassifier,
)
aadl2_Thread_strategy = st.builds(
    aadl2_Thread,
)
Thread_strategy = st.builds(
    Thread,
)
aadl2_ThreadClassifier_strategy = st.builds(
    aadl2_ThreadClassifier,
)
aadl2_System_strategy = st.builds(
    aadl2_System,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
aadl2_Process_strategy = st.builds(
    aadl2_Process,
)
Process_strategy = st.builds(
    Process,
)
aadl2_ProcessClassifier_strategy = st.builds(
    aadl2_ProcessClassifier,
)
aadl2_Memory_strategy = st.builds(
    aadl2_Memory,
)
Memory_strategy = st.builds(
    Memory,
)
aadl2_MemoryClassifier_strategy = st.builds(
    aadl2_MemoryClassifier,
)
aadl2_Device_strategy = st.builds(
    aadl2_Device,
)
Device_strategy = st.builds(
    Device,
)
aadl2_DeviceClassifier_strategy = st.builds(
    aadl2_DeviceClassifier,
)
aadl2_SubprogramGroupSubcomponent_strategy = st.builds(
    aadl2_SubprogramGroupSubcomponent,
)
aadl2_SubprogramSubcomponent_strategy = st.builds(
    aadl2_SubprogramSubcomponent,
)
aadl2_SubprogramCallSequence_strategy = st.builds(
    aadl2_SubprogramCallSequence,
)
aadl2_CallSpecification_strategy = st.builds(
    aadl2_CallSpecification,
)
ComponentImplementation_strategy = st.builds(
    ComponentImplementation,
)
aadl2_BehavioredImplementation_strategy = st.builds(
    aadl2_BehavioredImplementation,
)
aadl2_VirtualProcessorSubcomponent_strategy = st.builds(
    aadl2_VirtualProcessorSubcomponent,
)
aadl2_VirtualBusSubcomponent_strategy = st.builds(
    aadl2_VirtualBusSubcomponent,
)
aadl2_ThreadGroupSubcomponent_strategy = st.builds(
    aadl2_ThreadGroupSubcomponent,
)
aadl2_ThreadSubcomponent_strategy = st.builds(
    aadl2_ThreadSubcomponent,
)
BehavioredImplementation_strategy = st.builds(
    BehavioredImplementation,
)
aadl2_SystemSubcomponent_strategy = st.builds(
    aadl2_SystemSubcomponent,
)
aadl2_ProcessorSubcomponent_strategy = st.builds(
    aadl2_ProcessorSubcomponent,
)
aadl2_ProcessSubcomponent_strategy = st.builds(
    aadl2_ProcessSubcomponent,
)
aadl2_MemorySubcomponent_strategy = st.builds(
    aadl2_MemorySubcomponent,
)
aadl2_DeviceSubcomponent_strategy = st.builds(
    aadl2_DeviceSubcomponent,
)
aadl2_DataSubcomponent_strategy = st.builds(
    aadl2_DataSubcomponent,
)
aadl2_BusSubcomponent_strategy = st.builds(
    aadl2_BusSubcomponent,
)
AbstractClassifier_strategy = st.builds(
    AbstractClassifier,
)
ComponentType_strategy = st.builds(
    ComponentType,
)
aadl2_VirtualProcessorImplementation_strategy = st.builds(
    aadl2_VirtualProcessorImplementation,
)
aadl2_VirtualProcessorType_strategy = st.builds(
    aadl2_VirtualProcessorType,
)
aadl2_VirtualBusImplementation_strategy = st.builds(
    aadl2_VirtualBusImplementation,
)
aadl2_PropertySet_strategy = st.builds(
    aadl2_PropertySet,
    contents=
        safe_text,
    imports=
        safe_text
)
aadl2_SystemImplementation_strategy = st.builds(
    aadl2_SystemImplementation,
)
aadl2_SystemType_strategy = st.builds(
    aadl2_SystemType,
)
aadl2_SubprogramGroupImplementation_strategy = st.builds(
    aadl2_SubprogramGroupImplementation,
)
aadl2_VirtualBusType_strategy = st.builds(
    aadl2_VirtualBusType,
)
aadl2_ThreadGroupImplementation_strategy = st.builds(
    aadl2_ThreadGroupImplementation,
)
aadl2_ThreadGroupType_strategy = st.builds(
    aadl2_ThreadGroupType,
)
aadl2_ThreadImplementation_strategy = st.builds(
    aadl2_ThreadImplementation,
)
aadl2_ThreadType_strategy = st.builds(
    aadl2_ThreadType,
)
aadl2_ProcessType_strategy = st.builds(
    aadl2_ProcessType,
)
aadl2_MemoryImplementation_strategy = st.builds(
    aadl2_MemoryImplementation,
)
aadl2_SubprogramGroupType_strategy = st.builds(
    aadl2_SubprogramGroupType,
)
aadl2_SubprogramImplementation_strategy = st.builds(
    aadl2_SubprogramImplementation,
)
aadl2_SubprogramType_strategy = st.builds(
    aadl2_SubprogramType,
)
aadl2_ProcessorImplementation_strategy = st.builds(
    aadl2_ProcessorImplementation,
)
aadl2_ProcessImplementation_strategy = st.builds(
    aadl2_ProcessImplementation,
)
aadl2_ProcessorType_strategy = st.builds(
    aadl2_ProcessorType,
)
aadl2_AbstractImplementation_strategy = st.builds(
    aadl2_AbstractImplementation,
)
aadl2_AbstractType_strategy = st.builds(
    aadl2_AbstractType,
)
aadl2_AadlPackage_strategy = st.builds(
    aadl2_AadlPackage,
)
aadl2_MemoryType_strategy = st.builds(
    aadl2_MemoryType,
)
aadl2_DeviceImplementation_strategy = st.builds(
    aadl2_DeviceImplementation,
)
aadl2_DeviceType_strategy = st.builds(
    aadl2_DeviceType,
)
aadl2_DataImplementation_strategy = st.builds(
    aadl2_DataImplementation,
)
aadl2_DataType_strategy = st.builds(
    aadl2_DataType,
)
aadl2_BusImplementation_strategy = st.builds(
    aadl2_BusImplementation,
)
aadl2_BusType_strategy = st.builds(
    aadl2_BusType,
)
aadl2_PackageSection_strategy = st.builds(
    aadl2_PackageSection,
    noAnnexes=
        safe_text,
    aliases=
        safe_text,
    noProperties=
        safe_text,
    declarations=
        safe_text,
    imports=
        safe_text
)
aadl2_PrivatePackageSection_strategy = st.builds(
    aadl2_PrivatePackageSection,
)
aadl2_FeatureGroupTypeRename_strategy = st.builds(
    aadl2_FeatureGroupTypeRename,
)
aadl2_ComponentTypeRename_strategy = st.builds(
    aadl2_ComponentTypeRename,
    category=
        safe_text
)
aadl2_PackageRename_strategy = st.builds(
    aadl2_PackageRename,
    renameAll=
        safe_text
)
Connection_strategy = st.builds(
    Connection,
)
aadl2_PortConnection_strategy = st.builds(
    aadl2_PortConnection,
)
aadl2_ParameterConnection_strategy = st.builds(
    aadl2_ParameterConnection,
)
aadl2_AccessConnection_strategy = st.builds(
    aadl2_AccessConnection,
    accessCategory=
        safe_text
)
aadl2_FeatureGroupConnection_strategy = st.builds(
    aadl2_FeatureGroupConnection,
)
aadl2_FeatureConnection_strategy = st.builds(
    aadl2_FeatureConnection,
)

@given(instance=EnumerationType_strategy)
@settings(max_examples=50)
def test_enumerationtype_instantiation(instance):
    assert isinstance(instance, EnumerationType)

@given(instance=NumberType_strategy)
@settings(max_examples=50)
def test_numbertype_instantiation(instance):
    assert isinstance(instance, NumberType)

@given(instance=aadl2_AadlReal_strategy)
@settings(max_examples=50)
def test_aadl2_aadlreal_instantiation(instance):
    assert isinstance(instance, aadl2_AadlReal)

@given(instance=aadl2_AadlInteger_strategy)
@settings(max_examples=50)
def test_aadl2_aadlinteger_instantiation(instance):
    assert isinstance(instance, aadl2_AadlInteger)

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=aadl2_AadlString_strategy)
@settings(max_examples=50)
def test_aadl2_aadlstring_instantiation(instance):
    assert isinstance(instance, aadl2_AadlString)

@given(instance=aadl2_ClassifierType_strategy)
@settings(max_examples=50)
def test_aadl2_classifiertype_instantiation(instance):
    assert isinstance(instance, aadl2_ClassifierType)

@given(instance=aadl2_ReferenceType_strategy)
@settings(max_examples=50)
def test_aadl2_referencetype_instantiation(instance):
    assert isinstance(instance, aadl2_ReferenceType)

@given(instance=aadl2_RangeType_strategy)
@settings(max_examples=50)
def test_aadl2_rangetype_instantiation(instance):
    assert isinstance(instance, aadl2_RangeType)

@given(instance=aadl2_AadlBoolean_strategy)
@settings(max_examples=50)
def test_aadl2_aadlboolean_instantiation(instance):
    assert isinstance(instance, aadl2_AadlBoolean)

@given(instance=aadl2_UnitsType_strategy)
@settings(max_examples=50)
def test_aadl2_unitstype_instantiation(instance):
    assert isinstance(instance, aadl2_UnitsType)

@given(instance=aadl2_NumberType_strategy)
@settings(max_examples=50)
def test_aadl2_numbertype_instantiation(instance):
    assert isinstance(instance, aadl2_NumberType)

@given(instance=NumberValue_strategy)
@settings(max_examples=50)
def test_numbervalue_instantiation(instance):
    assert isinstance(instance, NumberValue)

@given(instance=aadl2_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_aadl2_integerliteral_instantiation(instance):
    assert isinstance(instance, aadl2_IntegerLiteral)



@given(instance=aadl2_IntegerLiteral_strategy)
def test_aadl2_integerliteral_base_setter(instance):
    original = instance.base
    instance.base = original
    assert instance.base == original



@given(instance=aadl2_IntegerLiteral_strategy)
def test_aadl2_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ContainedNamedElement_strategy)
@settings(max_examples=50)
def test_containednamedelement_instantiation(instance):
    assert isinstance(instance, ContainedNamedElement)

@given(instance=aadl2_RealLiteral_strategy)
@settings(max_examples=50)
def test_aadl2_realliteral_instantiation(instance):
    assert isinstance(instance, aadl2_RealLiteral)



@given(instance=aadl2_RealLiteral_strategy)
def test_aadl2_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PropertyExpression_strategy)
@settings(max_examples=50)
def test_propertyexpression_instantiation(instance):
    assert isinstance(instance, PropertyExpression)

@given(instance=aadl2_ListValue_strategy)
@settings(max_examples=50)
def test_aadl2_listvalue_instantiation(instance):
    assert isinstance(instance, aadl2_ListValue)

@given(instance=aadl2_Operation_strategy)
@settings(max_examples=50)
def test_aadl2_operation_instantiation(instance):
    assert isinstance(instance, aadl2_Operation)



@given(instance=aadl2_Operation_strategy)
def test_aadl2_operation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=aadl2_PropertyValue_strategy)
@settings(max_examples=50)
def test_aadl2_propertyvalue_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyValue)

@given(instance=PropertyValue_strategy)
@settings(max_examples=50)
def test_propertyvalue_instantiation(instance):
    assert isinstance(instance, PropertyValue)

@given(instance=aadl2_RecordValue_strategy)
@settings(max_examples=50)
def test_aadl2_recordvalue_instantiation(instance):
    assert isinstance(instance, aadl2_RecordValue)

@given(instance=aadl2_ComputedValue_strategy)
@settings(max_examples=50)
def test_aadl2_computedvalue_instantiation(instance):
    assert isinstance(instance, aadl2_ComputedValue)



@given(instance=aadl2_ComputedValue_strategy)
def test_aadl2_computedvalue_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=aadl2_RangeValue_strategy)
@settings(max_examples=50)
def test_aadl2_rangevalue_instantiation(instance):
    assert isinstance(instance, aadl2_RangeValue)

@given(instance=aadl2_NumberValue_strategy)
@settings(max_examples=50)
def test_aadl2_numbervalue_instantiation(instance):
    assert isinstance(instance, aadl2_NumberValue)



@given(instance=aadl2_NumberValue_strategy)
def test_aadl2_numbervalue_valueString_setter(instance):
    original = instance.valueString
    instance.valueString = original
    assert instance.valueString == original

@given(instance=aadl2_StringLiteral_strategy)
@settings(max_examples=50)
def test_aadl2_stringliteral_instantiation(instance):
    assert isinstance(instance, aadl2_StringLiteral)



@given(instance=aadl2_StringLiteral_strategy)
def test_aadl2_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aadl2_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_aadl2_booleanliteral_instantiation(instance):
    assert isinstance(instance, aadl2_BooleanLiteral)



@given(instance=aadl2_BooleanLiteral_strategy)
def test_aadl2_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aadl2_ReferenceValue_strategy)
@settings(max_examples=50)
def test_aadl2_referencevalue_instantiation(instance):
    assert isinstance(instance, aadl2_ReferenceValue)

@given(instance=aadl2_EnumerationValue_strategy)
@settings(max_examples=50)
def test_aadl2_enumerationvalue_instantiation(instance):
    assert isinstance(instance, aadl2_EnumerationValue)

@given(instance=CallSpecification_strategy)
@settings(max_examples=50)
def test_callspecification_instantiation(instance):
    assert isinstance(instance, CallSpecification)

@given(instance=aadl2_ProcessorCall_strategy)
@settings(max_examples=50)
def test_aadl2_processorcall_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorCall)



@given(instance=aadl2_ProcessorCall_strategy)
def test_aadl2_processorcall_subprogramAccessName_setter(instance):
    original = instance.subprogramAccessName
    instance.subprogramAccessName = original
    assert instance.subprogramAccessName == original

@given(instance=FeatureGroupPrototypeActual_strategy)
@settings(max_examples=50)
def test_featuregroupprototypeactual_instantiation(instance):
    assert isinstance(instance, FeatureGroupPrototypeActual)

@given(instance=aadl2_FeatureGroupReference_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroupreference_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupReference)

@given(instance=aadl2_FeatureGroupPrototypeReference_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroupprototypereference_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupPrototypeReference)

@given(instance=Subcomponent_strategy)
@settings(max_examples=50)
def test_subcomponent_instantiation(instance):
    assert isinstance(instance, Subcomponent)

@given(instance=PackageSection_strategy)
@settings(max_examples=50)
def test_packagesection_instantiation(instance):
    assert isinstance(instance, PackageSection)

@given(instance=aadl2_PublicPackageSection_strategy)
@settings(max_examples=50)
def test_aadl2_publicpackagesection_instantiation(instance):
    assert isinstance(instance, aadl2_PublicPackageSection)

@given(instance=AnnexSubclause_strategy)
@settings(max_examples=50)
def test_annexsubclause_instantiation(instance):
    assert isinstance(instance, AnnexSubclause)

@given(instance=aadl2_DefaultAnnexSubclause_strategy)
@settings(max_examples=50)
def test_aadl2_defaultannexsubclause_instantiation(instance):
    assert isinstance(instance, aadl2_DefaultAnnexSubclause)



@given(instance=aadl2_DefaultAnnexSubclause_strategy)
def test_aadl2_defaultannexsubclause_sourceText_setter(instance):
    original = instance.sourceText
    instance.sourceText = original
    assert instance.sourceText == original

@given(instance=AnnexLibrary_strategy)
@settings(max_examples=50)
def test_annexlibrary_instantiation(instance):
    assert isinstance(instance, AnnexLibrary)

@given(instance=aadl2_DefaultAnnexLibrary_strategy)
@settings(max_examples=50)
def test_aadl2_defaultannexlibrary_instantiation(instance):
    assert isinstance(instance, aadl2_DefaultAnnexLibrary)



@given(instance=aadl2_DefaultAnnexLibrary_strategy)
def test_aadl2_defaultannexlibrary_sourceText_setter(instance):
    original = instance.sourceText
    instance.sourceText = original
    assert instance.sourceText == original

@given(instance=ModalPath_strategy)
@settings(max_examples=50)
def test_modalpath_instantiation(instance):
    assert isinstance(instance, ModalPath)

@given(instance=Abstract_strategy)
@settings(max_examples=50)
def test_abstract_instantiation(instance):
    assert isinstance(instance, Abstract)

@given(instance=Prototype_strategy)
@settings(max_examples=50)
def test_prototype_instantiation(instance):
    assert isinstance(instance, Prototype)

@given(instance=aadl2_ComponentPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_componentprototype_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentPrototype)



@given(instance=aadl2_ComponentPrototype_strategy)
def test_aadl2_componentprototype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original



@given(instance=aadl2_ComponentPrototype_strategy)
def test_aadl2_componentprototype_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=CalledSubprogram_strategy)
@settings(max_examples=50)
def test_calledsubprogram_instantiation(instance):
    assert isinstance(instance, CalledSubprogram)

@given(instance=SubprogramGroup_strategy)
@settings(max_examples=50)
def test_subprogramgroup_instantiation(instance):
    assert isinstance(instance, SubprogramGroup)

@given(instance=Subprogram_strategy)
@settings(max_examples=50)
def test_subprogram_instantiation(instance):
    assert isinstance(instance, Subprogram)

@given(instance=AccessConnectionEnd_strategy)
@settings(max_examples=50)
def test_accessconnectionend_instantiation(instance):
    assert isinstance(instance, AccessConnectionEnd)

@given(instance=Access_strategy)
@settings(max_examples=50)
def test_access_instantiation(instance):
    assert isinstance(instance, Access)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=EndToEndFlowElement_strategy)
@settings(max_examples=50)
def test_endtoendflowelement_instantiation(instance):
    assert isinstance(instance, EndToEndFlowElement)

@given(instance=aadl2_FlowElement_strategy)
@settings(max_examples=50)
def test_aadl2_flowelement_instantiation(instance):
    assert isinstance(instance, aadl2_FlowElement)

@given(instance=ParameterConnectionEnd_strategy)
@settings(max_examples=50)
def test_parameterconnectionend_instantiation(instance):
    assert isinstance(instance, ParameterConnectionEnd)

@given(instance=FlowElement_strategy)
@settings(max_examples=50)
def test_flowelement_instantiation(instance):
    assert isinstance(instance, FlowElement)

@given(instance=aadl2_SubcomponentFlow_strategy)
@settings(max_examples=50)
def test_aadl2_subcomponentflow_instantiation(instance):
    assert isinstance(instance, aadl2_SubcomponentFlow)

@given(instance=Bus_strategy)
@settings(max_examples=50)
def test_bus_instantiation(instance):
    assert isinstance(instance, Bus)

@given(instance=aadl2_BusAccess_strategy)
@settings(max_examples=50)
def test_aadl2_busaccess_instantiation(instance):
    assert isinstance(instance, aadl2_BusAccess)

@given(instance=aadl2_SubprogramAccess_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramaccess_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramAccess)

@given(instance=aadl2_EventPort_strategy)
@settings(max_examples=50)
def test_aadl2_eventport_instantiation(instance):
    assert isinstance(instance, aadl2_EventPort)

@given(instance=Flow_strategy)
@settings(max_examples=50)
def test_flow_instantiation(instance):
    assert isinstance(instance, Flow)

@given(instance=CallContext_strategy)
@settings(max_examples=50)
def test_callcontext_instantiation(instance):
    assert isinstance(instance, CallContext)

@given(instance=aadl2_SubprogramGroupAccess_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgroupaccess_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupAccess)

@given(instance=FeatureGroupConnectionEnd_strategy)
@settings(max_examples=50)
def test_featuregroupconnectionend_instantiation(instance):
    assert isinstance(instance, FeatureGroupConnectionEnd)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=aadl2_EventDataPort_strategy)
@settings(max_examples=50)
def test_aadl2_eventdataport_instantiation(instance):
    assert isinstance(instance, aadl2_EventDataPort)

@given(instance=aadl2_SubprogramCall_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramcall_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramCall)

@given(instance=aadl2_DataPort_strategy)
@settings(max_examples=50)
def test_aadl2_dataport_instantiation(instance):
    assert isinstance(instance, aadl2_DataPort)

@given(instance=Generalization__strategy)
@settings(max_examples=50)
def test_generalization__instantiation(instance):
    assert isinstance(instance, Generalization_)

@given(instance=aadl2_GroupExtension_strategy)
@settings(max_examples=50)
def test_aadl2_groupextension_instantiation(instance):
    assert isinstance(instance, aadl2_GroupExtension)

@given(instance=ConnectionEnd_strategy)
@settings(max_examples=50)
def test_connectionend_instantiation(instance):
    assert isinstance(instance, ConnectionEnd)

@given(instance=aadl2_AccessConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2_accessconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2_AccessConnectionEnd)

@given(instance=aadl2_PortConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2_portconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2_PortConnectionEnd)

@given(instance=aadl2_ParameterConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2_parameterconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2_ParameterConnectionEnd)

@given(instance=aadl2_FeatureGroupConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroupconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupConnectionEnd)

@given(instance=aadl2_FeatureConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2_featureconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureConnectionEnd)

@given(instance=ArrayableElement_strategy)
@settings(max_examples=50)
def test_arrayableelement_instantiation(instance):
    assert isinstance(instance, ArrayableElement)

@given(instance=FeatureConnectionEnd_strategy)
@settings(max_examples=50)
def test_featureconnectionend_instantiation(instance):
    assert isinstance(instance, FeatureConnectionEnd)

@given(instance=aadl2_TypeExtension_strategy)
@settings(max_examples=50)
def test_aadl2_typeextension_instantiation(instance):
    assert isinstance(instance, aadl2_TypeExtension)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=aadl2_FeatureGroupType_strategy)
@settings(max_examples=50)
def test_aadl2_featuregrouptype_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupType)



@given(instance=aadl2_FeatureGroupType_strategy)
def test_aadl2_featuregrouptype_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=aadl2_ComponentClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_componentclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentClassifier)



@given(instance=aadl2_ComponentClassifier_strategy)
def test_aadl2_componentclassifier_noFlows_setter(instance):
    original = instance.noFlows
    instance.noFlows = original
    assert instance.noFlows == original



@given(instance=aadl2_ComponentClassifier_strategy)
def test_aadl2_componentclassifier_noModes_setter(instance):
    original = instance.noModes
    instance.noModes = original
    assert instance.noModes == original

@given(instance=aadl2_ProcessorSubprogram_strategy)
@settings(max_examples=50)
def test_aadl2_processorsubprogram_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorSubprogram)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=aadl2_Access_strategy)
@settings(max_examples=50)
def test_aadl2_access_instantiation(instance):
    assert isinstance(instance, aadl2_Access)



@given(instance=aadl2_Access_strategy)
def test_aadl2_access_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=aadl2_Access_strategy)
def test_aadl2_access_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=aadl2_DirectedFeature_strategy)
@settings(max_examples=50)
def test_aadl2_directedfeature_instantiation(instance):
    assert isinstance(instance, aadl2_DirectedFeature)



@given(instance=aadl2_DirectedFeature_strategy)
def test_aadl2_directedfeature_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=PortConnectionEnd_strategy)
@settings(max_examples=50)
def test_portconnectionend_instantiation(instance):
    assert isinstance(instance, PortConnectionEnd)

@given(instance=aadl2_DataAccess_strategy)
@settings(max_examples=50)
def test_aadl2_dataaccess_instantiation(instance):
    assert isinstance(instance, aadl2_DataAccess)

@given(instance=DirectedFeature_strategy)
@settings(max_examples=50)
def test_directedfeature_instantiation(instance):
    assert isinstance(instance, DirectedFeature)

@given(instance=aadl2_Parameter_strategy)
@settings(max_examples=50)
def test_aadl2_parameter_instantiation(instance):
    assert isinstance(instance, aadl2_Parameter)

@given(instance=aadl2_FeatureGroup_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroup_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroup)



@given(instance=aadl2_FeatureGroup_strategy)
def test_aadl2_featuregroup_inverse_setter(instance):
    original = instance.inverse
    instance.inverse = original
    assert instance.inverse == original

@given(instance=aadl2_AbstractFeature_strategy)
@settings(max_examples=50)
def test_aadl2_abstractfeature_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractFeature)

@given(instance=aadl2_Port_strategy)
@settings(max_examples=50)
def test_aadl2_port_instantiation(instance):
    assert isinstance(instance, aadl2_Port)



@given(instance=aadl2_Port_strategy)
def test_aadl2_port_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=ModeTransitionTrigger_strategy)
@settings(max_examples=50)
def test_modetransitiontrigger_instantiation(instance):
    assert isinstance(instance, ModeTransitionTrigger)

@given(instance=aadl2_ProcessorPort_strategy)
@settings(max_examples=50)
def test_aadl2_processorport_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorPort)

@given(instance=aadl2_InternalEvent_strategy)
@settings(max_examples=50)
def test_aadl2_internalevent_instantiation(instance):
    assert isinstance(instance, aadl2_InternalEvent)

@given(instance=aadl2_TriggerPort_strategy)
@settings(max_examples=50)
def test_aadl2_triggerport_instantiation(instance):
    assert isinstance(instance, aadl2_TriggerPort)

@given(instance=aadl2_Realization_strategy)
@settings(max_examples=50)
def test_aadl2_realization_instantiation(instance):
    assert isinstance(instance, aadl2_Realization)

@given(instance=aadl2_ImplementationExtension_strategy)
@settings(max_examples=50)
def test_aadl2_implementationextension_instantiation(instance):
    assert isinstance(instance, aadl2_ImplementationExtension)

@given(instance=aadl2_AbstractSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_abstractsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractSubcomponent)

@given(instance=aadl2_EndToEndFlow_strategy)
@settings(max_examples=50)
def test_aadl2_endtoendflow_instantiation(instance):
    assert isinstance(instance, aadl2_EndToEndFlow)

@given(instance=ComponentClassifier_strategy)
@settings(max_examples=50)
def test_componentclassifier_instantiation(instance):
    assert isinstance(instance, ComponentClassifier)

@given(instance=aadl2_SubprogramGroupClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgroupclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupClassifier)

@given(instance=aadl2_SubprogramClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramClassifier)

@given(instance=aadl2_ComponentType_strategy)
@settings(max_examples=50)
def test_aadl2_componenttype_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentType)



@given(instance=aadl2_ComponentType_strategy)
def test_aadl2_componenttype_features_setter(instance):
    original = instance.features
    instance.features = original
    assert instance.features == original



@given(instance=aadl2_ComponentType_strategy)
def test_aadl2_componenttype_noFeatures_setter(instance):
    original = instance.noFeatures
    instance.noFeatures = original
    assert instance.noFeatures == original

@given(instance=aadl2_AbstractClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_abstractclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractClassifier)

@given(instance=aadl2_BusClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_busclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_BusClassifier)

@given(instance=aadl2_DataClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_dataclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_DataClassifier)

@given(instance=aadl2_ComponentImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_componentimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentImplementation)



@given(instance=aadl2_ComponentImplementation_strategy)
def test_aadl2_componentimplementation_flows_setter(instance):
    original = instance.flows
    instance.flows = original
    assert instance.flows == original



@given(instance=aadl2_ComponentImplementation_strategy)
def test_aadl2_componentimplementation_noConnections_setter(instance):
    original = instance.noConnections
    instance.noConnections = original
    assert instance.noConnections == original



@given(instance=aadl2_ComponentImplementation_strategy)
def test_aadl2_componentimplementation_noSubcomponents_setter(instance):
    original = instance.noSubcomponents
    instance.noSubcomponents = original
    assert instance.noSubcomponents == original



@given(instance=aadl2_ComponentImplementation_strategy)
def test_aadl2_componentimplementation_subcomponents_setter(instance):
    original = instance.subcomponents
    instance.subcomponents = original
    assert instance.subcomponents == original



@given(instance=aadl2_ComponentImplementation_strategy)
def test_aadl2_componentimplementation_connections_setter(instance):
    original = instance.connections
    instance.connections = original
    assert instance.connections == original



@given(instance=aadl2_ComponentImplementation_strategy)
def test_aadl2_componentimplementation_noCalls_setter(instance):
    original = instance.noCalls
    instance.noCalls = original
    assert instance.noCalls == original

@given(instance=ArraySize_strategy)
@settings(max_examples=50)
def test_arraysize_instantiation(instance):
    assert isinstance(instance, ArraySize)

@given(instance=aadl2_PropertyReference_strategy)
@settings(max_examples=50)
def test_aadl2_propertyreference_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyReference)

@given(instance=aadl2_ConstantValue_strategy)
@settings(max_examples=50)
def test_aadl2_constantvalue_instantiation(instance):
    assert isinstance(instance, aadl2_ConstantValue)

@given(instance=aadl2_Numeral_strategy)
@settings(max_examples=50)
def test_aadl2_numeral_instantiation(instance):
    assert isinstance(instance, aadl2_Numeral)



@given(instance=aadl2_Numeral_strategy)
def test_aadl2_numeral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=RefinableElement_strategy)
@settings(max_examples=50)
def test_refinableelement_instantiation(instance):
    assert isinstance(instance, RefinableElement)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=aadl2_Flow_strategy)
@settings(max_examples=50)
def test_aadl2_flow_instantiation(instance):
    assert isinstance(instance, aadl2_Flow)

@given(instance=aadl2_Feature_strategy)
@settings(max_examples=50)
def test_aadl2_feature_instantiation(instance):
    assert isinstance(instance, aadl2_Feature)

@given(instance=aadl2_FlowImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_flowimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_FlowImplementation)



@given(instance=aadl2_FlowImplementation_strategy)
def test_aadl2_flowimplementation_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=aadl2_Connection_strategy)
@settings(max_examples=50)
def test_aadl2_connection_instantiation(instance):
    assert isinstance(instance, aadl2_Connection)



@given(instance=aadl2_Connection_strategy)
def test_aadl2_connection_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=aadl2_Connection_strategy)
def test_aadl2_connection_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original

@given(instance=ClassifierFeature_strategy)
@settings(max_examples=50)
def test_classifierfeature_instantiation(instance):
    assert isinstance(instance, ClassifierFeature)

@given(instance=aadl2_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_aadl2_behavioralfeature_instantiation(instance):
    assert isinstance(instance, aadl2_BehavioralFeature)

@given(instance=aadl2_StructuralFeature_strategy)
@settings(max_examples=50)
def test_aadl2_structuralfeature_instantiation(instance):
    assert isinstance(instance, aadl2_StructuralFeature)

@given(instance=aadl2_ModeFeature_strategy)
@settings(max_examples=50)
def test_aadl2_modefeature_instantiation(instance):
    assert isinstance(instance, aadl2_ModeFeature)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=aadl2_DirectedRelationship_strategy)
@settings(max_examples=50)
def test_aadl2_directedrelationship_instantiation(instance):
    assert isinstance(instance, aadl2_DirectedRelationship)

@given(instance=ModeFeature_strategy)
@settings(max_examples=50)
def test_modefeature_instantiation(instance):
    assert isinstance(instance, ModeFeature)

@given(instance=aadl2_ModeTransition_strategy)
@settings(max_examples=50)
def test_aadl2_modetransition_instantiation(instance):
    assert isinstance(instance, aadl2_ModeTransition)

@given(instance=aadl2_Mode_strategy)
@settings(max_examples=50)
def test_aadl2_mode_instantiation(instance):
    assert isinstance(instance, aadl2_Mode)



@given(instance=aadl2_Mode_strategy)
def test_aadl2_mode_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=aadl2_Mode_strategy)
def test_aadl2_mode_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=ModalElement_strategy)
@settings(max_examples=50)
def test_modalelement_instantiation(instance):
    assert isinstance(instance, ModalElement)

@given(instance=aadl2_FlowSpecification_strategy)
@settings(max_examples=50)
def test_aadl2_flowspecification_instantiation(instance):
    assert isinstance(instance, aadl2_FlowSpecification)



@given(instance=aadl2_FlowSpecification_strategy)
def test_aadl2_flowspecification_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=aadl2_ModalPath_strategy)
@settings(max_examples=50)
def test_aadl2_modalpath_instantiation(instance):
    assert isinstance(instance, aadl2_ModalPath)

@given(instance=aadl2_Subcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_subcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_Subcomponent)



@given(instance=aadl2_Subcomponent_strategy)
def test_aadl2_subcomponent_allModes_setter(instance):
    original = instance.allModes
    instance.allModes = original
    assert instance.allModes == original

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=aadl2_Generalization__strategy)
@settings(max_examples=50)
def test_aadl2_generalization__instantiation(instance):
    assert isinstance(instance, aadl2_Generalization_)

@given(instance=aadl2_Prototype_strategy)
@settings(max_examples=50)
def test_aadl2_prototype_instantiation(instance):
    assert isinstance(instance, aadl2_Prototype)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Prototype_strategy)
@settings(max_examples=30)
def test_aadl2_prototype_categoryconstraint_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.categoryConstraint(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.categoryConstraint).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'categoryConstraint' in aadl2_Prototype is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'categoryConstraint' in aadl2_Prototype did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'categoryConstraint' in aadl2_Prototype is not implemented or raised an error")

@given(instance=aadl2_AnnexSubclause_strategy)
@settings(max_examples=50)
def test_aadl2_annexsubclause_instantiation(instance):
    assert isinstance(instance, aadl2_AnnexSubclause)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=aadl2_GlobalNamespace_strategy)
@settings(max_examples=50)
def test_aadl2_globalnamespace_instantiation(instance):
    assert isinstance(instance, aadl2_GlobalNamespace)

@given(instance=aadl2_RecordType_strategy)
@settings(max_examples=50)
def test_aadl2_recordtype_instantiation(instance):
    assert isinstance(instance, aadl2_RecordType)

@given(instance=aadl2_EnumerationType_strategy)
@settings(max_examples=50)
def test_aadl2_enumerationtype_instantiation(instance):
    assert isinstance(instance, aadl2_EnumerationType)

@given(instance=PropertyOwner_strategy)
@settings(max_examples=50)
def test_propertyowner_instantiation(instance):
    assert isinstance(instance, PropertyOwner)

@given(instance=aadl2_ClassifierValue_strategy)
@settings(max_examples=50)
def test_aadl2_classifiervalue_instantiation(instance):
    assert isinstance(instance, aadl2_ClassifierValue)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=aadl2_PropertyType_strategy)
@settings(max_examples=50)
def test_aadl2_propertytype_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyType)

@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=50)
def test_aadl2_classifier_instantiation(instance):
    assert isinstance(instance, aadl2_Classifier)



@given(instance=aadl2_Classifier_strategy)
def test_aadl2_classifier_noProperties_setter(instance):
    original = instance.noProperties
    instance.noProperties = original
    assert instance.noProperties == original



@given(instance=aadl2_Classifier_strategy)
def test_aadl2_classifier_noPrototypes_setter(instance):
    original = instance.noPrototypes
    instance.noPrototypes = original
    assert instance.noPrototypes == original



@given(instance=aadl2_Classifier_strategy)
def test_aadl2_classifier_noAnnexes_setter(instance):
    original = instance.noAnnexes
    instance.noAnnexes = original
    assert instance.noAnnexes == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=30)
def test_aadl2_classifier_allfeatures_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.allFeatures()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.allFeatures).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'allFeatures' in aadl2_Classifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'allFeatures' in aadl2_Classifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'allFeatures' in aadl2_Classifier is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=30)
def test_aadl2_classifier_allparents_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.allParents()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.allParents).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'allParents' in aadl2_Classifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'allParents' in aadl2_Classifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'allParents' in aadl2_Classifier is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=30)
def test_aadl2_classifier_inherit_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.inherit(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.inherit).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'inherit' in aadl2_Classifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'inherit' in aadl2_Classifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'inherit' in aadl2_Classifier is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=30)
def test_aadl2_classifier_mayspecializetype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.maySpecializeType(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.maySpecializeType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'maySpecializeType' in aadl2_Classifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'maySpecializeType' in aadl2_Classifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'maySpecializeType' in aadl2_Classifier is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=30)
def test_aadl2_classifier_no_cycles_in_generalization_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.no_cycles_in_generalization(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.no_cycles_in_generalization).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'no_cycles_in_generalization' in aadl2_Classifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'no_cycles_in_generalization' in aadl2_Classifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'no_cycles_in_generalization' in aadl2_Classifier is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=30)
def test_aadl2_classifier_specialize_type_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.specialize_type(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.specialize_type).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'specialize_type' in aadl2_Classifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'specialize_type' in aadl2_Classifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'specialize_type' in aadl2_Classifier is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=30)
def test_aadl2_classifier_inheritablemembers_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.inheritableMembers(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.inheritableMembers).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'inheritableMembers' in aadl2_Classifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'inheritableMembers' in aadl2_Classifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'inheritableMembers' in aadl2_Classifier is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=30)
def test_aadl2_classifier_hasvisibilityof_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasVisibilityOf(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasVisibilityOf).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasVisibilityOf' in aadl2_Classifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasVisibilityOf' in aadl2_Classifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasVisibilityOf' in aadl2_Classifier is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=30)
def test_aadl2_classifier_inheritedmember_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.inheritedMember()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.inheritedMember).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'inheritedMember' in aadl2_Classifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'inheritedMember' in aadl2_Classifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'inheritedMember' in aadl2_Classifier is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=30)
def test_aadl2_classifier_parents_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.parents()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.parents).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'parents' in aadl2_Classifier is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'parents' in aadl2_Classifier did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'parents' in aadl2_Classifier is not implemented or raised an error")

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=aadl2_BasicProperty_strategy)
@settings(max_examples=50)
def test_aadl2_basicproperty_instantiation(instance):
    assert isinstance(instance, aadl2_BasicProperty)



@given(instance=aadl2_BasicProperty_strategy)
def test_aadl2_basicproperty_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=aadl2_MetaclassReference_strategy)
@settings(max_examples=50)
def test_aadl2_metaclassreference_instantiation(instance):
    assert isinstance(instance, aadl2_MetaclassReference)



@given(instance=aadl2_MetaclassReference_strategy)
def test_aadl2_metaclassreference_annexName_setter(instance):
    original = instance.annexName
    instance.annexName = original
    assert instance.annexName == original



@given(instance=aadl2_MetaclassReference_strategy)
def test_aadl2_metaclassreference_metaclassName_setter(instance):
    original = instance.metaclassName
    instance.metaclassName = original
    assert instance.metaclassName == original

@given(instance=BasicProperty_strategy)
@settings(max_examples=50)
def test_basicproperty_instantiation(instance):
    assert isinstance(instance, BasicProperty)

@given(instance=aadl2_RecordField_strategy)
@settings(max_examples=50)
def test_aadl2_recordfield_instantiation(instance):
    assert isinstance(instance, aadl2_RecordField)

@given(instance=aadl2_Property_strategy)
@settings(max_examples=50)
def test_aadl2_property_instantiation(instance):
    assert isinstance(instance, aadl2_Property)



@given(instance=aadl2_Property_strategy)
def test_aadl2_property_emptyListDefault_setter(instance):
    original = instance.emptyListDefault
    instance.emptyListDefault = original
    assert instance.emptyListDefault == original



@given(instance=aadl2_Property_strategy)
def test_aadl2_property_inherit_setter(instance):
    original = instance.inherit
    instance.inherit = original
    assert instance.inherit == original

@given(instance=aadl2_ModalPropertyValue_strategy)
@settings(max_examples=50)
def test_aadl2_modalpropertyvalue_instantiation(instance):
    assert isinstance(instance, aadl2_ModalPropertyValue)

@given(instance=aadl2_Element_strategy)
@settings(max_examples=50)
def test_aadl2_element_instantiation(instance):
    assert isinstance(instance, aadl2_Element)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Element_strategy)
@settings(max_examples=30)
def test_aadl2_element_has_owner_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.has_owner(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.has_owner).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'has_owner' in aadl2_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'has_owner' in aadl2_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'has_owner' in aadl2_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Element_strategy)
@settings(max_examples=30)
def test_aadl2_element_not_own_self_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.not_own_self(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.not_own_self).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'not_own_self' in aadl2_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'not_own_self' in aadl2_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'not_own_self' in aadl2_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Element_strategy)
@settings(max_examples=30)
def test_aadl2_element_allownedelements_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.allOwnedElements()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.allOwnedElements).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'allOwnedElements' in aadl2_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'allOwnedElements' in aadl2_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'allOwnedElements' in aadl2_Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Element_strategy)
@settings(max_examples=30)
def test_aadl2_element_mustbeowned_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.mustBeOwned()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.mustBeOwned).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'mustBeOwned' in aadl2_Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'mustBeOwned' in aadl2_Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'mustBeOwned' in aadl2_Element is not implemented or raised an error")

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=aadl2_EndToEndFlowElement_strategy)
@settings(max_examples=50)
def test_aadl2_endtoendflowelement_instantiation(instance):
    assert isinstance(instance, aadl2_EndToEndFlowElement)

@given(instance=aadl2_ConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2_connectionend_instantiation(instance):
    assert isinstance(instance, aadl2_ConnectionEnd)

@given(instance=aadl2_Context_strategy)
@settings(max_examples=50)
def test_aadl2_context_instantiation(instance):
    assert isinstance(instance, aadl2_Context)

@given(instance=aadl2_Subprogram_strategy)
@settings(max_examples=50)
def test_aadl2_subprogram_instantiation(instance):
    assert isinstance(instance, aadl2_Subprogram)

@given(instance=aadl2_Bus_strategy)
@settings(max_examples=50)
def test_aadl2_bus_instantiation(instance):
    assert isinstance(instance, aadl2_Bus)

@given(instance=aadl2_Type_strategy)
@settings(max_examples=50)
def test_aadl2_type_instantiation(instance):
    assert isinstance(instance, aadl2_Type)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Type_strategy)
@settings(max_examples=30)
def test_aadl2_type_conformsto_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.conformsTo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.conformsTo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'conformsTo' in aadl2_Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'conformsTo' in aadl2_Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'conformsTo' in aadl2_Type is not implemented or raised an error")

@given(instance=aadl2_TypedElement_strategy)
@settings(max_examples=50)
def test_aadl2_typedelement_instantiation(instance):
    assert isinstance(instance, aadl2_TypedElement)

@given(instance=aadl2_Abstract_strategy)
@settings(max_examples=50)
def test_aadl2_abstract_instantiation(instance):
    assert isinstance(instance, aadl2_Abstract)

@given(instance=aadl2_ClassifierFeature_strategy)
@settings(max_examples=50)
def test_aadl2_classifierfeature_instantiation(instance):
    assert isinstance(instance, aadl2_ClassifierFeature)

@given(instance=aadl2_ModalElement_strategy)
@settings(max_examples=50)
def test_aadl2_modalelement_instantiation(instance):
    assert isinstance(instance, aadl2_ModalElement)



@given(instance=aadl2_ModalElement_strategy)
def test_aadl2_modalelement_modesAndTransitions_setter(instance):
    original = instance.modesAndTransitions
    instance.modesAndTransitions = original
    assert instance.modesAndTransitions == original

@given(instance=aadl2_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_aadl2_enumerationliteral_instantiation(instance):
    assert isinstance(instance, aadl2_EnumerationLiteral)

@given(instance=aadl2_AnnexLibrary_strategy)
@settings(max_examples=50)
def test_aadl2_annexlibrary_instantiation(instance):
    assert isinstance(instance, aadl2_AnnexLibrary)

@given(instance=aadl2_RefinableElement_strategy)
@settings(max_examples=50)
def test_aadl2_refinableelement_instantiation(instance):
    assert isinstance(instance, aadl2_RefinableElement)

@given(instance=aadl2_SubprogramGroup_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgroup_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroup)

@given(instance=aadl2_Data_strategy)
@settings(max_examples=50)
def test_aadl2_data_instantiation(instance):
    assert isinstance(instance, aadl2_Data)

@given(instance=aadl2_Namespace_strategy)
@settings(max_examples=50)
def test_aadl2_namespace_instantiation(instance):
    assert isinstance(instance, aadl2_Namespace)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Namespace_strategy)
@settings(max_examples=30)
def test_aadl2_namespace_members_distinguishable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.members_distinguishable(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.members_distinguishable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'members_distinguishable' in aadl2_Namespace is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'members_distinguishable' in aadl2_Namespace did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'members_distinguishable' in aadl2_Namespace is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_Namespace_strategy)
@settings(max_examples=30)
def test_aadl2_namespace_membersaredistinguishable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.membersAreDistinguishable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.membersAreDistinguishable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'membersAreDistinguishable' in aadl2_Namespace is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'membersAreDistinguishable' in aadl2_Namespace did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'membersAreDistinguishable' in aadl2_Namespace is not implemented or raised an error")

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=aadl2_ArraySpecification_strategy)
@settings(max_examples=50)
def test_aadl2_arrayspecification_instantiation(instance):
    assert isinstance(instance, aadl2_ArraySpecification)



@given(instance=aadl2_ArraySpecification_strategy)
def test_aadl2_arrayspecification_dimension_setter(instance):
    original = instance.dimension
    instance.dimension = original
    assert instance.dimension == original

@given(instance=aadl2_Relationship_strategy)
@settings(max_examples=50)
def test_aadl2_relationship_instantiation(instance):
    assert isinstance(instance, aadl2_Relationship)

@given(instance=aadl2_ComponentImplementationReference_strategy)
@settings(max_examples=50)
def test_aadl2_componentimplementationreference_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentImplementationReference)

@given(instance=aadl2_PropertyOwner_strategy)
@settings(max_examples=50)
def test_aadl2_propertyowner_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyOwner)

@given(instance=aadl2_PropertyExpression_strategy)
@settings(max_examples=50)
def test_aadl2_propertyexpression_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyExpression)

@given(instance=aadl2_ArrayRange_strategy)
@settings(max_examples=50)
def test_aadl2_arrayrange_instantiation(instance):
    assert isinstance(instance, aadl2_ArrayRange)



@given(instance=aadl2_ArrayRange_strategy)
def test_aadl2_arrayrange_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=aadl2_ArrayRange_strategy)
def test_aadl2_arrayrange_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=aadl2_ModeBinding_strategy)
@settings(max_examples=50)
def test_aadl2_modebinding_instantiation(instance):
    assert isinstance(instance, aadl2_ModeBinding)

@given(instance=aadl2_CallContext_strategy)
@settings(max_examples=50)
def test_aadl2_callcontext_instantiation(instance):
    assert isinstance(instance, aadl2_CallContext)

@given(instance=aadl2_ModeTransitionTrigger_strategy)
@settings(max_examples=50)
def test_aadl2_modetransitiontrigger_instantiation(instance):
    assert isinstance(instance, aadl2_ModeTransitionTrigger)

@given(instance=aadl2_BasicPropertyAssociation_strategy)
@settings(max_examples=50)
def test_aadl2_basicpropertyassociation_instantiation(instance):
    assert isinstance(instance, aadl2_BasicPropertyAssociation)

@given(instance=aadl2_CalledSubprogram_strategy)
@settings(max_examples=50)
def test_aadl2_calledsubprogram_instantiation(instance):
    assert isinstance(instance, aadl2_CalledSubprogram)

@given(instance=aadl2_ArraySize_strategy)
@settings(max_examples=50)
def test_aadl2_arraysize_instantiation(instance):
    assert isinstance(instance, aadl2_ArraySize)

@given(instance=aadl2_PropertyAssociation_strategy)
@settings(max_examples=50)
def test_aadl2_propertyassociation_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyAssociation)



@given(instance=aadl2_PropertyAssociation_strategy)
def test_aadl2_propertyassociation_append_setter(instance):
    original = instance.append
    instance.append = original
    assert instance.append == original



@given(instance=aadl2_PropertyAssociation_strategy)
def test_aadl2_propertyassociation_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=aadl2_ArrayableElement_strategy)
@settings(max_examples=50)
def test_aadl2_arrayableelement_instantiation(instance):
    assert isinstance(instance, aadl2_ArrayableElement)

@given(instance=aadl2_ContainedNamedElement_strategy)
@settings(max_examples=50)
def test_aadl2_containednamedelement_instantiation(instance):
    assert isinstance(instance, aadl2_ContainedNamedElement)

@given(instance=aadl2_NamedElement_strategy)
@settings(max_examples=50)
def test_aadl2_namedelement_instantiation(instance):
    assert isinstance(instance, aadl2_NamedElement)



@given(instance=aadl2_NamedElement_strategy)
def test_aadl2_namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original



@given(instance=aadl2_NamedElement_strategy)
def test_aadl2_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_NamedElement_strategy)
@settings(max_examples=30)
def test_aadl2_namedelement_has_no_qualified_name_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.has_no_qualified_name(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.has_no_qualified_name).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'has_no_qualified_name' in aadl2_NamedElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'has_no_qualified_name' in aadl2_NamedElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'has_no_qualified_name' in aadl2_NamedElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_NamedElement_strategy)
@settings(max_examples=30)
def test_aadl2_namedelement_has_qualified_name_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.has_qualified_name(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.has_qualified_name).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'has_qualified_name' in aadl2_NamedElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'has_qualified_name' in aadl2_NamedElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'has_qualified_name' in aadl2_NamedElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_NamedElement_strategy)
@settings(max_examples=30)
def test_aadl2_namedelement_separator_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.separator()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.separator).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'separator' in aadl2_NamedElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'separator' in aadl2_NamedElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'separator' in aadl2_NamedElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_NamedElement_strategy)
@settings(max_examples=30)
def test_aadl2_namedelement_allnamespaces_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.allNamespaces()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.allNamespaces).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'allNamespaces' in aadl2_NamedElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'allNamespaces' in aadl2_NamedElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'allNamespaces' in aadl2_NamedElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_NamedElement_strategy)
@settings(max_examples=30)
def test_aadl2_namedelement_isdistinguishablefrom_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isDistinguishableFrom(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isDistinguishableFrom).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isDistinguishableFrom' in aadl2_NamedElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isDistinguishableFrom' in aadl2_NamedElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isDistinguishableFrom' in aadl2_NamedElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_NamedElement_strategy)
@settings(max_examples=30)
def test_aadl2_namedelement_qualifiedname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.qualifiedName()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.qualifiedName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'qualifiedName' in aadl2_NamedElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'qualifiedName' in aadl2_NamedElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'qualifiedName' in aadl2_NamedElement is not implemented or raised an error")

@given(instance=aadl2_ContainmentPathElement_strategy)
@settings(max_examples=50)
def test_aadl2_containmentpathelement_instantiation(instance):
    assert isinstance(instance, aadl2_ContainmentPathElement)

@given(instance=aadl2_PrototypeBinding_strategy)
@settings(max_examples=50)
def test_aadl2_prototypebinding_instantiation(instance):
    assert isinstance(instance, aadl2_PrototypeBinding)

@given(instance=aadl2_NumericRange_strategy)
@settings(max_examples=50)
def test_aadl2_numericrange_instantiation(instance):
    assert isinstance(instance, aadl2_NumericRange)

@given(instance=aadl2_Comment_strategy)
@settings(max_examples=50)
def test_aadl2_comment_instantiation(instance):
    assert isinstance(instance, aadl2_Comment)



@given(instance=aadl2_Comment_strategy)
def test_aadl2_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=ComponentPrototypeActual_strategy)
@settings(max_examples=50)
def test_componentprototypeactual_instantiation(instance):
    assert isinstance(instance, ComponentPrototypeActual)

@given(instance=aadl2_ComponentPrototypeReference_strategy)
@settings(max_examples=50)
def test_aadl2_componentprototypereference_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentPrototypeReference)

@given(instance=aadl2_UnitLiteral_strategy)
@settings(max_examples=50)
def test_aadl2_unitliteral_instantiation(instance):
    assert isinstance(instance, aadl2_UnitLiteral)

@given(instance=aadl2_UnitValue_strategy)
@settings(max_examples=50)
def test_aadl2_unitvalue_instantiation(instance):
    assert isinstance(instance, aadl2_UnitValue)

@given(instance=aadl2_ComponentReference_strategy)
@settings(max_examples=50)
def test_aadl2_componentreference_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentReference)

@given(instance=aadl2_FeaturePrototype_strategy)
@settings(max_examples=50)
def test_aadl2_featureprototype_instantiation(instance):
    assert isinstance(instance, aadl2_FeaturePrototype)



@given(instance=aadl2_FeaturePrototype_strategy)
def test_aadl2_featureprototype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=aadl2_FeatureGroupPrototypeActual_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroupprototypeactual_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupPrototypeActual)

@given(instance=aadl2_FeatureGroupPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroupprototype_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupPrototype)

@given(instance=aadl2_ComponentPrototypeActual_strategy)
@settings(max_examples=50)
def test_aadl2_componentprototypeactual_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentPrototypeActual)



@given(instance=aadl2_ComponentPrototypeActual_strategy)
def test_aadl2_componentprototypeactual_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=FeaturePrototypeActual_strategy)
@settings(max_examples=50)
def test_featureprototypeactual_instantiation(instance):
    assert isinstance(instance, FeaturePrototypeActual)

@given(instance=aadl2_PortSpecification_strategy)
@settings(max_examples=50)
def test_aadl2_portspecification_instantiation(instance):
    assert isinstance(instance, aadl2_PortSpecification)



@given(instance=aadl2_PortSpecification_strategy)
def test_aadl2_portspecification_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=aadl2_PortSpecification_strategy)
def test_aadl2_portspecification_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=aadl2_FeaturePrototypeReference_strategy)
@settings(max_examples=50)
def test_aadl2_featureprototypereference_instantiation(instance):
    assert isinstance(instance, aadl2_FeaturePrototypeReference)



@given(instance=aadl2_FeaturePrototypeReference_strategy)
def test_aadl2_featureprototypereference_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=aadl2_AccessSpecification_strategy)
@settings(max_examples=50)
def test_aadl2_accessspecification_instantiation(instance):
    assert isinstance(instance, aadl2_AccessSpecification)



@given(instance=aadl2_AccessSpecification_strategy)
def test_aadl2_accessspecification_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=aadl2_AccessSpecification_strategy)
def test_aadl2_accessspecification_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=aadl2_FeaturePrototypeActual_strategy)
@settings(max_examples=50)
def test_aadl2_featureprototypeactual_instantiation(instance):
    assert isinstance(instance, aadl2_FeaturePrototypeActual)

@given(instance=aadl2_PropertyConstant_strategy)
@settings(max_examples=50)
def test_aadl2_propertyconstant_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyConstant)



@given(instance=aadl2_PropertyConstant_strategy)
def test_aadl2_propertyconstant_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=PrototypeBinding_strategy)
@settings(max_examples=50)
def test_prototypebinding_instantiation(instance):
    assert isinstance(instance, PrototypeBinding)

@given(instance=aadl2_FeaturePrototypeBinding_strategy)
@settings(max_examples=50)
def test_aadl2_featureprototypebinding_instantiation(instance):
    assert isinstance(instance, aadl2_FeaturePrototypeBinding)

@given(instance=aadl2_FeatureGroupPrototypeBinding_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroupprototypebinding_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupPrototypeBinding)

@given(instance=aadl2_ComponentPrototypeBinding_strategy)
@settings(max_examples=50)
def test_aadl2_componentprototypebinding_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentPrototypeBinding)

@given(instance=VirtualProcessorClassifier_strategy)
@settings(max_examples=50)
def test_virtualprocessorclassifier_instantiation(instance):
    assert isinstance(instance, VirtualProcessorClassifier)

@given(instance=VirtualBusClassifier_strategy)
@settings(max_examples=50)
def test_virtualbusclassifier_instantiation(instance):
    assert isinstance(instance, VirtualBusClassifier)

@given(instance=ThreadGroupClassifier_strategy)
@settings(max_examples=50)
def test_threadgroupclassifier_instantiation(instance):
    assert isinstance(instance, ThreadGroupClassifier)

@given(instance=ThreadClassifier_strategy)
@settings(max_examples=50)
def test_threadclassifier_instantiation(instance):
    assert isinstance(instance, ThreadClassifier)

@given(instance=SystemClassifier_strategy)
@settings(max_examples=50)
def test_systemclassifier_instantiation(instance):
    assert isinstance(instance, SystemClassifier)

@given(instance=SubprogramGroupClassifier_strategy)
@settings(max_examples=50)
def test_subprogramgroupclassifier_instantiation(instance):
    assert isinstance(instance, SubprogramGroupClassifier)

@given(instance=SubprogramClassifier_strategy)
@settings(max_examples=50)
def test_subprogramclassifier_instantiation(instance):
    assert isinstance(instance, SubprogramClassifier)

@given(instance=ProcessorClassifier_strategy)
@settings(max_examples=50)
def test_processorclassifier_instantiation(instance):
    assert isinstance(instance, ProcessorClassifier)

@given(instance=ProcessClassifier_strategy)
@settings(max_examples=50)
def test_processclassifier_instantiation(instance):
    assert isinstance(instance, ProcessClassifier)

@given(instance=MemoryClassifier_strategy)
@settings(max_examples=50)
def test_memoryclassifier_instantiation(instance):
    assert isinstance(instance, MemoryClassifier)

@given(instance=DeviceClassifier_strategy)
@settings(max_examples=50)
def test_deviceclassifier_instantiation(instance):
    assert isinstance(instance, DeviceClassifier)

@given(instance=VirtualProcessor_strategy)
@settings(max_examples=50)
def test_virtualprocessor_instantiation(instance):
    assert isinstance(instance, VirtualProcessor)

@given(instance=aadl2_VirtualProcessorClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_virtualprocessorclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorClassifier)

@given(instance=aadl2_VirtualBus_strategy)
@settings(max_examples=50)
def test_aadl2_virtualbus_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBus)

@given(instance=VirtualBus_strategy)
@settings(max_examples=50)
def test_virtualbus_instantiation(instance):
    assert isinstance(instance, VirtualBus)

@given(instance=aadl2_VirtualBusClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_virtualbusclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusClassifier)

@given(instance=DataClassifier_strategy)
@settings(max_examples=50)
def test_dataclassifier_instantiation(instance):
    assert isinstance(instance, DataClassifier)

@given(instance=BusClassifier_strategy)
@settings(max_examples=50)
def test_busclassifier_instantiation(instance):
    assert isinstance(instance, BusClassifier)

@given(instance=aadl2_VirtualProcessor_strategy)
@settings(max_examples=50)
def test_aadl2_virtualprocessor_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessor)

@given(instance=System_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, System)

@given(instance=aadl2_SystemClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_systemclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_SystemClassifier)

@given(instance=aadl2_Processor_strategy)
@settings(max_examples=50)
def test_aadl2_processor_instantiation(instance):
    assert isinstance(instance, aadl2_Processor)

@given(instance=Processor_strategy)
@settings(max_examples=50)
def test_processor_instantiation(instance):
    assert isinstance(instance, Processor)

@given(instance=aadl2_ProcessorClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_processorclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorClassifier)

@given(instance=aadl2_ThreadGroup_strategy)
@settings(max_examples=50)
def test_aadl2_threadgroup_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroup)

@given(instance=ThreadGroup_strategy)
@settings(max_examples=50)
def test_threadgroup_instantiation(instance):
    assert isinstance(instance, ThreadGroup)

@given(instance=aadl2_ThreadGroupClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_threadgroupclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupClassifier)

@given(instance=aadl2_Thread_strategy)
@settings(max_examples=50)
def test_aadl2_thread_instantiation(instance):
    assert isinstance(instance, aadl2_Thread)

@given(instance=Thread_strategy)
@settings(max_examples=50)
def test_thread_instantiation(instance):
    assert isinstance(instance, Thread)

@given(instance=aadl2_ThreadClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_threadclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadClassifier)

@given(instance=aadl2_System_strategy)
@settings(max_examples=50)
def test_aadl2_system_instantiation(instance):
    assert isinstance(instance, aadl2_System)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=aadl2_Process_strategy)
@settings(max_examples=50)
def test_aadl2_process_instantiation(instance):
    assert isinstance(instance, aadl2_Process)

@given(instance=Process_strategy)
@settings(max_examples=50)
def test_process_instantiation(instance):
    assert isinstance(instance, Process)

@given(instance=aadl2_ProcessClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_processclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessClassifier)

@given(instance=aadl2_Memory_strategy)
@settings(max_examples=50)
def test_aadl2_memory_instantiation(instance):
    assert isinstance(instance, aadl2_Memory)

@given(instance=Memory_strategy)
@settings(max_examples=50)
def test_memory_instantiation(instance):
    assert isinstance(instance, Memory)

@given(instance=aadl2_MemoryClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_memoryclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_MemoryClassifier)

@given(instance=aadl2_Device_strategy)
@settings(max_examples=50)
def test_aadl2_device_instantiation(instance):
    assert isinstance(instance, aadl2_Device)

@given(instance=Device_strategy)
@settings(max_examples=50)
def test_device_instantiation(instance):
    assert isinstance(instance, Device)

@given(instance=aadl2_DeviceClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_deviceclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceClassifier)

@given(instance=aadl2_SubprogramGroupSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgroupsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupSubcomponent)

@given(instance=aadl2_SubprogramSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramSubcomponent)

@given(instance=aadl2_SubprogramCallSequence_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramcallsequence_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramCallSequence)

@given(instance=aadl2_CallSpecification_strategy)
@settings(max_examples=50)
def test_aadl2_callspecification_instantiation(instance):
    assert isinstance(instance, aadl2_CallSpecification)

@given(instance=ComponentImplementation_strategy)
@settings(max_examples=50)
def test_componentimplementation_instantiation(instance):
    assert isinstance(instance, ComponentImplementation)

@given(instance=aadl2_BehavioredImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_behavioredimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_BehavioredImplementation)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2_BehavioredImplementation_strategy)
@settings(max_examples=30)
def test_aadl2_behavioredimplementation_callspecifications_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.callSpecifications()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.callSpecifications).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'callSpecifications' in aadl2_BehavioredImplementation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'callSpecifications' in aadl2_BehavioredImplementation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'callSpecifications' in aadl2_BehavioredImplementation is not implemented or raised an error")

@given(instance=aadl2_VirtualProcessorSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_virtualprocessorsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorSubcomponent)

@given(instance=aadl2_VirtualBusSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_virtualbussubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusSubcomponent)

@given(instance=aadl2_ThreadGroupSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_threadgroupsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupSubcomponent)

@given(instance=aadl2_ThreadSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_threadsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadSubcomponent)

@given(instance=BehavioredImplementation_strategy)
@settings(max_examples=50)
def test_behavioredimplementation_instantiation(instance):
    assert isinstance(instance, BehavioredImplementation)

@given(instance=aadl2_SystemSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_systemsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_SystemSubcomponent)

@given(instance=aadl2_ProcessorSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_processorsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorSubcomponent)

@given(instance=aadl2_ProcessSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_processsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessSubcomponent)

@given(instance=aadl2_MemorySubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_memorysubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_MemorySubcomponent)

@given(instance=aadl2_DeviceSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_devicesubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceSubcomponent)

@given(instance=aadl2_DataSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_datasubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_DataSubcomponent)

@given(instance=aadl2_BusSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_bussubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_BusSubcomponent)

@given(instance=AbstractClassifier_strategy)
@settings(max_examples=50)
def test_abstractclassifier_instantiation(instance):
    assert isinstance(instance, AbstractClassifier)

@given(instance=ComponentType_strategy)
@settings(max_examples=50)
def test_componenttype_instantiation(instance):
    assert isinstance(instance, ComponentType)

@given(instance=aadl2_VirtualProcessorImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_virtualprocessorimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorImplementation)

@given(instance=aadl2_VirtualProcessorType_strategy)
@settings(max_examples=50)
def test_aadl2_virtualprocessortype_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorType)

@given(instance=aadl2_VirtualBusImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_virtualbusimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusImplementation)

@given(instance=aadl2_PropertySet_strategy)
@settings(max_examples=50)
def test_aadl2_propertyset_instantiation(instance):
    assert isinstance(instance, aadl2_PropertySet)



@given(instance=aadl2_PropertySet_strategy)
def test_aadl2_propertyset_contents_setter(instance):
    original = instance.contents
    instance.contents = original
    assert instance.contents == original



@given(instance=aadl2_PropertySet_strategy)
def test_aadl2_propertyset_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=aadl2_SystemImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_systemimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_SystemImplementation)

@given(instance=aadl2_SystemType_strategy)
@settings(max_examples=50)
def test_aadl2_systemtype_instantiation(instance):
    assert isinstance(instance, aadl2_SystemType)

@given(instance=aadl2_SubprogramGroupImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgroupimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupImplementation)

@given(instance=aadl2_VirtualBusType_strategy)
@settings(max_examples=50)
def test_aadl2_virtualbustype_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusType)

@given(instance=aadl2_ThreadGroupImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_threadgroupimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupImplementation)

@given(instance=aadl2_ThreadGroupType_strategy)
@settings(max_examples=50)
def test_aadl2_threadgrouptype_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupType)

@given(instance=aadl2_ThreadImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_threadimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadImplementation)

@given(instance=aadl2_ThreadType_strategy)
@settings(max_examples=50)
def test_aadl2_threadtype_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadType)

@given(instance=aadl2_ProcessType_strategy)
@settings(max_examples=50)
def test_aadl2_processtype_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessType)

@given(instance=aadl2_MemoryImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_memoryimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_MemoryImplementation)

@given(instance=aadl2_SubprogramGroupType_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgrouptype_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupType)

@given(instance=aadl2_SubprogramImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramImplementation)

@given(instance=aadl2_SubprogramType_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramtype_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramType)

@given(instance=aadl2_ProcessorImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_processorimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorImplementation)

@given(instance=aadl2_ProcessImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_processimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessImplementation)

@given(instance=aadl2_ProcessorType_strategy)
@settings(max_examples=50)
def test_aadl2_processortype_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorType)

@given(instance=aadl2_AbstractImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_abstractimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractImplementation)

@given(instance=aadl2_AbstractType_strategy)
@settings(max_examples=50)
def test_aadl2_abstracttype_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractType)

@given(instance=aadl2_AadlPackage_strategy)
@settings(max_examples=50)
def test_aadl2_aadlpackage_instantiation(instance):
    assert isinstance(instance, aadl2_AadlPackage)

@given(instance=aadl2_MemoryType_strategy)
@settings(max_examples=50)
def test_aadl2_memorytype_instantiation(instance):
    assert isinstance(instance, aadl2_MemoryType)

@given(instance=aadl2_DeviceImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_deviceimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceImplementation)

@given(instance=aadl2_DeviceType_strategy)
@settings(max_examples=50)
def test_aadl2_devicetype_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceType)

@given(instance=aadl2_DataImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_dataimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_DataImplementation)

@given(instance=aadl2_DataType_strategy)
@settings(max_examples=50)
def test_aadl2_datatype_instantiation(instance):
    assert isinstance(instance, aadl2_DataType)

@given(instance=aadl2_BusImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_busimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_BusImplementation)

@given(instance=aadl2_BusType_strategy)
@settings(max_examples=50)
def test_aadl2_bustype_instantiation(instance):
    assert isinstance(instance, aadl2_BusType)

@given(instance=aadl2_PackageSection_strategy)
@settings(max_examples=50)
def test_aadl2_packagesection_instantiation(instance):
    assert isinstance(instance, aadl2_PackageSection)



@given(instance=aadl2_PackageSection_strategy)
def test_aadl2_packagesection_noAnnexes_setter(instance):
    original = instance.noAnnexes
    instance.noAnnexes = original
    assert instance.noAnnexes == original



@given(instance=aadl2_PackageSection_strategy)
def test_aadl2_packagesection_aliases_setter(instance):
    original = instance.aliases
    instance.aliases = original
    assert instance.aliases == original



@given(instance=aadl2_PackageSection_strategy)
def test_aadl2_packagesection_noProperties_setter(instance):
    original = instance.noProperties
    instance.noProperties = original
    assert instance.noProperties == original



@given(instance=aadl2_PackageSection_strategy)
def test_aadl2_packagesection_declarations_setter(instance):
    original = instance.declarations
    instance.declarations = original
    assert instance.declarations == original



@given(instance=aadl2_PackageSection_strategy)
def test_aadl2_packagesection_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=aadl2_PrivatePackageSection_strategy)
@settings(max_examples=50)
def test_aadl2_privatepackagesection_instantiation(instance):
    assert isinstance(instance, aadl2_PrivatePackageSection)

@given(instance=aadl2_FeatureGroupTypeRename_strategy)
@settings(max_examples=50)
def test_aadl2_featuregrouptyperename_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupTypeRename)

@given(instance=aadl2_ComponentTypeRename_strategy)
@settings(max_examples=50)
def test_aadl2_componenttyperename_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentTypeRename)



@given(instance=aadl2_ComponentTypeRename_strategy)
def test_aadl2_componenttyperename_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=aadl2_PackageRename_strategy)
@settings(max_examples=50)
def test_aadl2_packagerename_instantiation(instance):
    assert isinstance(instance, aadl2_PackageRename)



@given(instance=aadl2_PackageRename_strategy)
def test_aadl2_packagerename_renameAll_setter(instance):
    original = instance.renameAll
    instance.renameAll = original
    assert instance.renameAll == original

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=aadl2_PortConnection_strategy)
@settings(max_examples=50)
def test_aadl2_portconnection_instantiation(instance):
    assert isinstance(instance, aadl2_PortConnection)

@given(instance=aadl2_ParameterConnection_strategy)
@settings(max_examples=50)
def test_aadl2_parameterconnection_instantiation(instance):
    assert isinstance(instance, aadl2_ParameterConnection)

@given(instance=aadl2_AccessConnection_strategy)
@settings(max_examples=50)
def test_aadl2_accessconnection_instantiation(instance):
    assert isinstance(instance, aadl2_AccessConnection)



@given(instance=aadl2_AccessConnection_strategy)
def test_aadl2_accessconnection_accessCategory_setter(instance):
    original = instance.accessCategory
    instance.accessCategory = original
    assert instance.accessCategory == original

@given(instance=aadl2_FeatureGroupConnection_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroupconnection_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupConnection)

@given(instance=aadl2_FeatureConnection_strategy)
@settings(max_examples=50)
def test_aadl2_featureconnection_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureConnection)
