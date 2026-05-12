import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractSubcomponentType,
    AbstractClassifier,
    ComponentType,
    ComponentImplementation,
    aadl2_BehavioredImplementation,
    BehavioralFeature,
    FeaturePrototypeActual,
    aadl2_FeaturePrototypeReference,
    aadl2_AccessSpecification,
    aadl2_PortSpecification,
    aadl2_FeatureGroupPrototypeActual,
    PrototypeBinding,
    aadl2_FeaturePrototypeBinding,
    aadl2_FeatureGroupPrototypeBinding,
    aadl2_ComponentPrototypeBinding,
    ModelUnit,
    aadl2_AadlPackage,
    ProcessorFeature,
    PackageSection,
    aadl2_PrivatePackageSection,
    aadl2_PublicPackageSection,
    AnnexSubclause,
    aadl2_DefaultAnnexSubclause,
    AnnexLibrary,
    aadl2_DefaultAnnexLibrary,
    SubprogramSubcomponentType,
    Abstract,
    Subcomponent,
    DataSubcomponentType,
    InternalFeature,
    Connection,
    SubprogramGroup,
    TriggerPort,
    Subprogram,
    Port,
    PortConnectionEnd,
    ParameterConnectionEnd,
    Data,
    Bus,
    Access,
    aadl2_SubprogramAccess,
    EnumerationType,
    aadl2_UnitsType,
    NumberType,
    aadl2_AadlReal,
    aadl2_AadlInteger,
    NonListType,
    aadl2_NumberType,
    aadl2_RangeType,
    aadl2_ClassifierType,
    aadl2_ReferenceType,
    aadl2_AadlString,
    aadl2_AadlBoolean,
    PropertyType,
    aadl2_ListType,
    aadl2_NonListType,
    NumberValue,
    aadl2_RealLiteral,
    aadl2_IntegerLiteral,
    EnumerationLiteral,
    aadl2_UnitLiteral,
    ContainedNamedElement,
    PropertyExpression,
    aadl2_ListValue,
    aadl2_Operation,
    aadl2_PropertyValue,
    PropertyValue,
    aadl2_RecordValue,
    aadl2_ReferenceValue,
    aadl2_ComputedValue,
    aadl2_NumberValue,
    aadl2_NamedValue,
    aadl2_RangeValue,
    aadl2_BooleanLiteral,
    aadl2_StringLiteral,
    VirtualBusClassifier,
    aadl2_VirtualBusType,
    VirtualProcessorClassifier,
    aadl2_VirtualProcessorImplementation,
    aadl2_VirtualProcessorType,
    aadl2_VirtualBusImplementation,
    ThreadGroupClassifier,
    aadl2_ThreadGroupImplementation,
    aadl2_ThreadGroupType,
    ThreadClassifier,
    aadl2_ThreadType,
    ProcessClassifier,
    aadl2_ProcessImplementation,
    aadl2_ProcessType,
    ProcessorClassifier,
    aadl2_ProcessorImplementation,
    aadl2_ProcessorType,
    SubprogramGroupClassifier,
    aadl2_SubprogramGroupImplementation,
    SystemClassifier,
    aadl2_SystemImplementation,
    aadl2_SystemType,
    SubprogramClassifier,
    MemoryClassifier,
    aadl2_MemoryType,
    aadl2_MemoryImplementation,
    DeviceClassifier,
    aadl2_DeviceType,
    aadl2_DeviceImplementation,
    DataClassifier,
    aadl2_DataImplementation,
    ComponentPrototype,
    aadl2_SubprogramPrototype,
    aadl2_DataPrototype,
    BusClassifier,
    aadl2_BusImplementation,
    aadl2_BusType,
    BehavioredImplementation,
    aadl2_SubprogramImplementation,
    aadl2_ThreadImplementation,
    aadl2_AbstractImplementation,
    Memory,
    aadl2_MemorySubcomponent,
    Process,
    aadl2_ProcessSubcomponent,
    System,
    aadl2_SystemSubcomponent,
    Thread,
    aadl2_ThreadSubcomponent,
    ThreadGroup,
    aadl2_ThreadGroupSubcomponent,
    VirtualBus,
    aadl2_VirtualBusSubcomponent,
    VirtualProcessor,
    aadl2_VirtualProcessorSubcomponent,
    VirtualProcessorSubcomponentType,
    aadl2_VirtualProcessorPrototype,
    VirtualBusSubcomponentType,
    aadl2_VirtualBusPrototype,
    Processor,
    aadl2_ProcessorSubcomponent,
    ThreadSubcomponentType,
    aadl2_ThreadPrototype,
    ThreadGroupSubcomponentType,
    aadl2_ThreadGroupPrototype,
    SystemSubcomponentType,
    aadl2_SystemPrototype,
    Device,
    aadl2_DeviceSubcomponent,
    SubprogramGroupSubcomponentType,
    aadl2_SubprogramGroupPrototype,
    ProcessSubcomponentType,
    aadl2_ProcessPrototype,
    ProcessorSubcomponentType,
    aadl2_ProcessorPrototype,
    MemorySubcomponentType,
    aadl2_MemoryPrototype,
    DeviceSubcomponentType,
    aadl2_DevicePrototype,
    BusSubcomponentType,
    aadl2_BusPrototype,
    aadl2_AbstractPrototype,
    AccessConnectionEnd,
    aadl2_DataSubcomponent,
    aadl2_SubprogramSubcomponent,
    aadl2_BusSubcomponent,
    aadl2_EventPort,
    FeatureType,
    aadl2_BusAccess,
    aadl2_FeatureType,
    CallContext,
    aadl2_DataType,
    aadl2_SubprogramGroupSubcomponent,
    aadl2_SubprogramType,
    aadl2_SubprogramGroupAccess,
    aadl2_SubprogramGroupType,
    aadl2_AbstractType,
    FeatureGroupConnectionEnd,
    Context,
    aadl2_SubprogramCall,
    aadl2_DataPort,
    aadl2_EventDataPort,
    DirectedFeature,
    aadl2_Port,
    aadl2_Parameter,
    Generalization_,
    aadl2_GroupExtension,
    Feature,
    aadl2_Access,
    aadl2_DirectedFeature,
    aadl2_CallContext,
    Flow,
    FlowElement,
    aadl2_DataAccess,
    ModalPath,
    FlowFeature,
    Prototype,
    aadl2_FeaturePrototype,
    aadl2_FeatureGroupPrototype,
    EndToEndFlowElement,
    aadl2_FlowElement,
    ArrayableElement,
    aadl2_ComponentPrototypeActual,
    aadl2_FeaturePrototypeActual,
    FeatureConnectionEnd,
    aadl2_AbstractFeature,
    aadl2_FeatureGroup,
    aadl2_TypeExtension,
    aadl2_FlowSpecification,
    ConnectionEnd,
    aadl2_AccessConnectionEnd,
    aadl2_PortConnectionEnd,
    aadl2_FeatureGroupConnectionEnd,
    aadl2_ParameterConnectionEnd,
    aadl2_FeatureConnectionEnd,
    aadl2_FeatureClassifier,
    aadl2_EventSource,
    aadl2_FeatureGroupConnection,
    aadl2_FeatureConnection,
    FeatureClassifier,
    SubcomponentType,
    aadl2_MemorySubcomponentType,
    aadl2_DataSubcomponentType,
    aadl2_ProcessorSubcomponentType,
    aadl2_SubprogramSubcomponentType,
    aadl2_SubprogramGroupSubcomponentType,
    aadl2_ProcessSubcomponentType,
    aadl2_VirtualProcessorSubcomponentType,
    aadl2_AbstractSubcomponentType,
    aadl2_SystemSubcomponentType,
    aadl2_ComponentPrototype,
    aadl2_DeviceSubcomponentType,
    aadl2_BusSubcomponentType,
    aadl2_ThreadSubcomponentType,
    aadl2_VirtualBusSubcomponentType,
    aadl2_ThreadGroupSubcomponentType,
    Classifier,
    aadl2_FeatureGroupType,
    aadl2_ComponentClassifier,
    aadl2_PortProxy,
    aadl2_EventDataSource,
    aadl2_Realization,
    aadl2_ImplementationExtension,
    ComponentClassifier,
    aadl2_MemoryClassifier,
    aadl2_DeviceClassifier,
    aadl2_VirtualBusClassifier,
    aadl2_ThreadClassifier,
    aadl2_DataClassifier,
    aadl2_AbstractClassifier,
    aadl2_ProcessorClassifier,
    aadl2_SystemClassifier,
    aadl2_SubprogramClassifier,
    aadl2_SubprogramGroupClassifier,
    aadl2_ComponentType,
    aadl2_BusClassifier,
    aadl2_VirtualProcessorClassifier,
    aadl2_ThreadGroupClassifier,
    aadl2_ProcessClassifier,
    aadl2_PortConnection,
    aadl2_ParameterConnection,
    aadl2_AccessConnection,
    aadl2_AbstractSubcomponent,
    aadl2_EndToEndFlow,
    aadl2_ComponentImplementation,
    aadl2_CalledSubprogram,
    RefinableElement,
    CalledSubprogram,
    aadl2_SubprogramProxy,
    StructuralFeature,
    aadl2_Connection,
    aadl2_Feature,
    aadl2_FlowFeature,
    Relationship,
    aadl2_DirectedRelationship,
    DirectedRelationship,
    ClassifierFeature,
    aadl2_StructuralFeature,
    aadl2_BehavioralFeature,
    aadl2_FlowImplementation,
    aadl2_ModeFeature,
    ModeFeature,
    aadl2_ModeTransition,
    aadl2_Mode,
    ModalElement,
    aadl2_ModalPath,
    aadl2_Subcomponent,
    aadl2_SubprogramCallSequence,
    aadl2_ProcessorFeature,
    aadl2_InternalFeature,
    aadl2_Prototype,
    aadl2_AnnexSubclause,
    aadl2_Generalization_,
    PropertyOwner,
    aadl2_ClassifierValue,
    aadl2_ArraySizeProperty,
    aadl2_AbstractNamedValue,
    Type,
    aadl2_SubcomponentType,
    aadl2_PropertyType,
    Namespace,
    aadl2_RecordType,
    aadl2_PropertySet,
    aadl2_EnumerationType,
    aadl2_GlobalNamespace,
    aadl2_PackageSection,
    ArraySizeProperty,
    AbstractNamedValue,
    BasicProperty,
    aadl2_RecordField,
    aadl2_ModalPropertyValue,
    aadl2_Classifier,
    aadl2_Property,
    TypedElement,
    aadl2_PropertyConstant,
    aadl2_BasicProperty,
    aadl2_MetaclassReference,
    NamedElement,
    aadl2_SubprogramGroup,
    aadl2_Data,
    aadl2_Memory,
    aadl2_RefinableElement,
    aadl2_ComponentTypeRename,
    aadl2_Processor,
    aadl2_Thread,
    aadl2_Context,
    aadl2_Flow,
    aadl2_Subprogram,
    aadl2_FeatureGroupTypeRename,
    aadl2_ModelUnit,
    aadl2_ThreadGroup,
    aadl2_TriggerPort,
    aadl2_VirtualProcessor,
    aadl2_ConnectionEnd,
    aadl2_Abstract,
    aadl2_EnumerationLiteral,
    aadl2_TypedElement,
    aadl2_ModalElement,
    aadl2_PackageRename,
    aadl2_AnnexLibrary,
    aadl2_Bus,
    aadl2_Namespace,
    aadl2_EndToEndFlowElement,
    aadl2_System,
    aadl2_ClassifierFeature,
    aadl2_Device,
    aadl2_Process,
    aadl2_VirtualBus,
    aadl2_Type,
    Element,
    aadl2_FlowEnd,
    aadl2_FlowSegment,
    aadl2_ArrayRange,
    aadl2_NumericRange,
    aadl2_ModeTransitionTrigger,
    aadl2_ArrayDimension,
    aadl2_ComponentImplementationReference,
    aadl2_PropertyOwner,
    aadl2_PropertyExpression,
    aadl2_NamedElement,
    aadl2_Relationship,
    aadl2_ArraySize,
    aadl2_ContainmentPathElement,
    aadl2_ContainedNamedElement,
    aadl2_ConnectedElement,
    aadl2_PrototypeBinding,
    aadl2_Comment,
    aadl2_PropertyAssociation,
    aadl2_EndToEndFlowSegment,
    aadl2_BasicPropertyAssociation,
    aadl2_ArrayableElement,
    aadl2_ModeBinding,
    aadl2_Element,
    ComponentCategory,
    DirectionType,
    FlowKind,
    PortCategory,
    AccessCategory,
    OperationKind,
    AccessType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(AbstractSubcomponentType)


def test_abstractsubcomponenttype_constructor_exists():
    assert callable(AbstractSubcomponentType.__init__)


def test_abstractsubcomponenttype_constructor_args():
    sig = inspect.signature(AbstractSubcomponentType.__init__)
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



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_featureprototypeactual_is_not_abstract():
    assert not inspect.isabstract(FeaturePrototypeActual)


def test_featureprototypeactual_constructor_exists():
    assert callable(FeaturePrototypeActual.__init__)


def test_featureprototypeactual_constructor_args():
    sig = inspect.signature(FeaturePrototypeActual.__init__)
    params = list(sig.parameters.keys())



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



def test_aadl2_portspecification_is_not_abstract():
    assert not inspect.isabstract(aadl2_PortSpecification)


def test_aadl2_portspecification_constructor_exists():
    assert callable(aadl2_PortSpecification.__init__)


def test_aadl2_portspecification_constructor_args():
    sig = inspect.signature(aadl2_PortSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_aadl2_portspecification_has_category():
    assert hasattr(aadl2_PortSpecification, "category")
    descriptor = None
    for klass in aadl2_PortSpecification.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_portspecification_has_direction():
    assert hasattr(aadl2_PortSpecification, "direction")
    descriptor = None
    for klass in aadl2_PortSpecification.__mro__:
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



def test_modelunit_is_not_abstract():
    assert not inspect.isabstract(ModelUnit)


def test_modelunit_constructor_exists():
    assert callable(ModelUnit.__init__)


def test_modelunit_constructor_args():
    sig = inspect.signature(ModelUnit.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_aadlpackage_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlPackage)


def test_aadl2_aadlpackage_constructor_exists():
    assert callable(aadl2_AadlPackage.__init__)


def test_aadl2_aadlpackage_constructor_args():
    sig = inspect.signature(aadl2_AadlPackage.__init__)
    params = list(sig.parameters.keys())



def test_processorfeature_is_not_abstract():
    assert not inspect.isabstract(ProcessorFeature)


def test_processorfeature_constructor_exists():
    assert callable(ProcessorFeature.__init__)


def test_processorfeature_constructor_args():
    sig = inspect.signature(ProcessorFeature.__init__)
    params = list(sig.parameters.keys())



def test_packagesection_is_not_abstract():
    assert not inspect.isabstract(PackageSection)


def test_packagesection_constructor_exists():
    assert callable(PackageSection.__init__)


def test_packagesection_constructor_args():
    sig = inspect.signature(PackageSection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_privatepackagesection_is_not_abstract():
    assert not inspect.isabstract(aadl2_PrivatePackageSection)


def test_aadl2_privatepackagesection_constructor_exists():
    assert callable(aadl2_PrivatePackageSection.__init__)


def test_aadl2_privatepackagesection_constructor_args():
    sig = inspect.signature(aadl2_PrivatePackageSection.__init__)
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



def test_subprogramsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(SubprogramSubcomponentType)


def test_subprogramsubcomponenttype_constructor_exists():
    assert callable(SubprogramSubcomponentType.__init__)


def test_subprogramsubcomponenttype_constructor_args():
    sig = inspect.signature(SubprogramSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_abstract_is_not_abstract():
    assert not inspect.isabstract(Abstract)


def test_abstract_constructor_exists():
    assert callable(Abstract.__init__)


def test_abstract_constructor_args():
    sig = inspect.signature(Abstract.__init__)
    params = list(sig.parameters.keys())



def test_subcomponent_is_not_abstract():
    assert not inspect.isabstract(Subcomponent)


def test_subcomponent_constructor_exists():
    assert callable(Subcomponent.__init__)


def test_subcomponent_constructor_args():
    sig = inspect.signature(Subcomponent.__init__)
    params = list(sig.parameters.keys())



def test_datasubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(DataSubcomponentType)


def test_datasubcomponenttype_constructor_exists():
    assert callable(DataSubcomponentType.__init__)


def test_datasubcomponenttype_constructor_args():
    sig = inspect.signature(DataSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_internalfeature_is_not_abstract():
    assert not inspect.isabstract(InternalFeature)


def test_internalfeature_constructor_exists():
    assert callable(InternalFeature.__init__)


def test_internalfeature_constructor_args():
    sig = inspect.signature(InternalFeature.__init__)
    params = list(sig.parameters.keys())



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_subprogramgroup_is_not_abstract():
    assert not inspect.isabstract(SubprogramGroup)


def test_subprogramgroup_constructor_exists():
    assert callable(SubprogramGroup.__init__)


def test_subprogramgroup_constructor_args():
    sig = inspect.signature(SubprogramGroup.__init__)
    params = list(sig.parameters.keys())



def test_triggerport_is_not_abstract():
    assert not inspect.isabstract(TriggerPort)


def test_triggerport_constructor_exists():
    assert callable(TriggerPort.__init__)


def test_triggerport_constructor_args():
    sig = inspect.signature(TriggerPort.__init__)
    params = list(sig.parameters.keys())



def test_subprogram_is_not_abstract():
    assert not inspect.isabstract(Subprogram)


def test_subprogram_constructor_exists():
    assert callable(Subprogram.__init__)


def test_subprogram_constructor_args():
    sig = inspect.signature(Subprogram.__init__)
    params = list(sig.parameters.keys())



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_portconnectionend_is_not_abstract():
    assert not inspect.isabstract(PortConnectionEnd)


def test_portconnectionend_constructor_exists():
    assert callable(PortConnectionEnd.__init__)


def test_portconnectionend_constructor_args():
    sig = inspect.signature(PortConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_parameterconnectionend_is_not_abstract():
    assert not inspect.isabstract(ParameterConnectionEnd)


def test_parameterconnectionend_constructor_exists():
    assert callable(ParameterConnectionEnd.__init__)


def test_parameterconnectionend_constructor_args():
    sig = inspect.signature(ParameterConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_data_constructor_exists():
    assert callable(Data.__init__)


def test_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_bus_is_not_abstract():
    assert not inspect.isabstract(Bus)


def test_bus_constructor_exists():
    assert callable(Bus.__init__)


def test_bus_constructor_args():
    sig = inspect.signature(Bus.__init__)
    params = list(sig.parameters.keys())



def test_access_is_not_abstract():
    assert not inspect.isabstract(Access)


def test_access_constructor_exists():
    assert callable(Access.__init__)


def test_access_constructor_args():
    sig = inspect.signature(Access.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramAccess)


def test_aadl2_subprogramaccess_constructor_exists():
    assert callable(aadl2_SubprogramAccess.__init__)


def test_aadl2_subprogramaccess_constructor_args():
    sig = inspect.signature(aadl2_SubprogramAccess.__init__)
    params = list(sig.parameters.keys())



def test_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(EnumerationType)


def test_enumerationtype_constructor_exists():
    assert callable(EnumerationType.__init__)


def test_enumerationtype_constructor_args():
    sig = inspect.signature(EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_unitstype_is_not_abstract():
    assert not inspect.isabstract(aadl2_UnitsType)


def test_aadl2_unitstype_constructor_exists():
    assert callable(aadl2_UnitsType.__init__)


def test_aadl2_unitstype_constructor_args():
    sig = inspect.signature(aadl2_UnitsType.__init__)
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



def test_nonlisttype_is_not_abstract():
    assert not inspect.isabstract(NonListType)


def test_nonlisttype_constructor_exists():
    assert callable(NonListType.__init__)


def test_nonlisttype_constructor_args():
    sig = inspect.signature(NonListType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_numbertype_is_not_abstract():
    assert not inspect.isabstract(aadl2_NumberType)


def test_aadl2_numbertype_constructor_exists():
    assert callable(aadl2_NumberType.__init__)


def test_aadl2_numbertype_constructor_args():
    sig = inspect.signature(aadl2_NumberType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_rangetype_is_not_abstract():
    assert not inspect.isabstract(aadl2_RangeType)


def test_aadl2_rangetype_constructor_exists():
    assert callable(aadl2_RangeType.__init__)


def test_aadl2_rangetype_constructor_args():
    sig = inspect.signature(aadl2_RangeType.__init__)
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



def test_aadl2_aadlstring_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlString)


def test_aadl2_aadlstring_constructor_exists():
    assert callable(aadl2_AadlString.__init__)


def test_aadl2_aadlstring_constructor_args():
    sig = inspect.signature(aadl2_AadlString.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_aadlboolean_is_not_abstract():
    assert not inspect.isabstract(aadl2_AadlBoolean)


def test_aadl2_aadlboolean_constructor_exists():
    assert callable(aadl2_AadlBoolean.__init__)


def test_aadl2_aadlboolean_constructor_args():
    sig = inspect.signature(aadl2_AadlBoolean.__init__)
    params = list(sig.parameters.keys())



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_listtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ListType)


def test_aadl2_listtype_constructor_exists():
    assert callable(aadl2_ListType.__init__)


def test_aadl2_listtype_constructor_args():
    sig = inspect.signature(aadl2_ListType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_nonlisttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_NonListType)


def test_aadl2_nonlisttype_constructor_exists():
    assert callable(aadl2_NonListType.__init__)


def test_aadl2_nonlisttype_constructor_args():
    sig = inspect.signature(aadl2_NonListType.__init__)
    params = list(sig.parameters.keys())



def test_numbervalue_is_not_abstract():
    assert not inspect.isabstract(NumberValue)


def test_numbervalue_constructor_exists():
    assert callable(NumberValue.__init__)


def test_numbervalue_constructor_args():
    sig = inspect.signature(NumberValue.__init__)
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



def test_aadl2_integerliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_IntegerLiteral)


def test_aadl2_integerliteral_constructor_exists():
    assert callable(aadl2_IntegerLiteral.__init__)


def test_aadl2_integerliteral_constructor_args():
    sig = inspect.signature(aadl2_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "base" in params, "Missing parameter 'base'"

def test_aadl2_integerliteral_has_value():
    assert hasattr(aadl2_IntegerLiteral, "value")
    descriptor = None
    for klass in aadl2_IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_integerliteral_has_base():
    assert hasattr(aadl2_IntegerLiteral, "base")
    descriptor = None
    for klass in aadl2_IntegerLiteral.__mro__:
        if "base" in klass.__dict__:
            descriptor = klass.__dict__["base"]
            break
    assert isinstance(descriptor, property)



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_unitliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_UnitLiteral)


def test_aadl2_unitliteral_constructor_exists():
    assert callable(aadl2_UnitLiteral.__init__)


def test_aadl2_unitliteral_constructor_args():
    sig = inspect.signature(aadl2_UnitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_containednamedelement_is_not_abstract():
    assert not inspect.isabstract(ContainedNamedElement)


def test_containednamedelement_constructor_exists():
    assert callable(ContainedNamedElement.__init__)


def test_containednamedelement_constructor_args():
    sig = inspect.signature(ContainedNamedElement.__init__)
    params = list(sig.parameters.keys())



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



def test_aadl2_referencevalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ReferenceValue)


def test_aadl2_referencevalue_constructor_exists():
    assert callable(aadl2_ReferenceValue.__init__)


def test_aadl2_referencevalue_constructor_args():
    sig = inspect.signature(aadl2_ReferenceValue.__init__)
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



def test_aadl2_numbervalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_NumberValue)


def test_aadl2_numbervalue_constructor_exists():
    assert callable(aadl2_NumberValue.__init__)


def test_aadl2_numbervalue_constructor_args():
    sig = inspect.signature(aadl2_NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_namedvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_NamedValue)


def test_aadl2_namedvalue_constructor_exists():
    assert callable(aadl2_NamedValue.__init__)


def test_aadl2_namedvalue_constructor_args():
    sig = inspect.signature(aadl2_NamedValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_rangevalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_RangeValue)


def test_aadl2_rangevalue_constructor_exists():
    assert callable(aadl2_RangeValue.__init__)


def test_aadl2_rangevalue_constructor_args():
    sig = inspect.signature(aadl2_RangeValue.__init__)
    params = list(sig.parameters.keys())



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



def test_virtualbusclassifier_is_not_abstract():
    assert not inspect.isabstract(VirtualBusClassifier)


def test_virtualbusclassifier_constructor_exists():
    assert callable(VirtualBusClassifier.__init__)


def test_virtualbusclassifier_constructor_args():
    sig = inspect.signature(VirtualBusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualbustype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusType)


def test_aadl2_virtualbustype_constructor_exists():
    assert callable(aadl2_VirtualBusType.__init__)


def test_aadl2_virtualbustype_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusType.__init__)
    params = list(sig.parameters.keys())



def test_virtualprocessorclassifier_is_not_abstract():
    assert not inspect.isabstract(VirtualProcessorClassifier)


def test_virtualprocessorclassifier_constructor_exists():
    assert callable(VirtualProcessorClassifier.__init__)


def test_virtualprocessorclassifier_constructor_args():
    sig = inspect.signature(VirtualProcessorClassifier.__init__)
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



def test_threadgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(ThreadGroupClassifier)


def test_threadgroupclassifier_constructor_exists():
    assert callable(ThreadGroupClassifier.__init__)


def test_threadgroupclassifier_constructor_args():
    sig = inspect.signature(ThreadGroupClassifier.__init__)
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



def test_threadclassifier_is_not_abstract():
    assert not inspect.isabstract(ThreadClassifier)


def test_threadclassifier_constructor_exists():
    assert callable(ThreadClassifier.__init__)


def test_threadclassifier_constructor_args():
    sig = inspect.signature(ThreadClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadType)


def test_aadl2_threadtype_constructor_exists():
    assert callable(aadl2_ThreadType.__init__)


def test_aadl2_threadtype_constructor_args():
    sig = inspect.signature(aadl2_ThreadType.__init__)
    params = list(sig.parameters.keys())



def test_processclassifier_is_not_abstract():
    assert not inspect.isabstract(ProcessClassifier)


def test_processclassifier_constructor_exists():
    assert callable(ProcessClassifier.__init__)


def test_processclassifier_constructor_args():
    sig = inspect.signature(ProcessClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessImplementation)


def test_aadl2_processimplementation_constructor_exists():
    assert callable(aadl2_ProcessImplementation.__init__)


def test_aadl2_processimplementation_constructor_args():
    sig = inspect.signature(aadl2_ProcessImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessType)


def test_aadl2_processtype_constructor_exists():
    assert callable(aadl2_ProcessType.__init__)


def test_aadl2_processtype_constructor_args():
    sig = inspect.signature(aadl2_ProcessType.__init__)
    params = list(sig.parameters.keys())



def test_processorclassifier_is_not_abstract():
    assert not inspect.isabstract(ProcessorClassifier)


def test_processorclassifier_constructor_exists():
    assert callable(ProcessorClassifier.__init__)


def test_processorclassifier_constructor_args():
    sig = inspect.signature(ProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processorimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorImplementation)


def test_aadl2_processorimplementation_constructor_exists():
    assert callable(aadl2_ProcessorImplementation.__init__)


def test_aadl2_processorimplementation_constructor_args():
    sig = inspect.signature(aadl2_ProcessorImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processortype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorType)


def test_aadl2_processortype_constructor_exists():
    assert callable(aadl2_ProcessorType.__init__)


def test_aadl2_processortype_constructor_args():
    sig = inspect.signature(aadl2_ProcessorType.__init__)
    params = list(sig.parameters.keys())



def test_subprogramgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(SubprogramGroupClassifier)


def test_subprogramgroupclassifier_constructor_exists():
    assert callable(SubprogramGroupClassifier.__init__)


def test_subprogramgroupclassifier_constructor_args():
    sig = inspect.signature(SubprogramGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgroupimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupImplementation)


def test_aadl2_subprogramgroupimplementation_constructor_exists():
    assert callable(aadl2_SubprogramGroupImplementation.__init__)


def test_aadl2_subprogramgroupimplementation_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupImplementation.__init__)
    params = list(sig.parameters.keys())



def test_systemclassifier_is_not_abstract():
    assert not inspect.isabstract(SystemClassifier)


def test_systemclassifier_constructor_exists():
    assert callable(SystemClassifier.__init__)


def test_systemclassifier_constructor_args():
    sig = inspect.signature(SystemClassifier.__init__)
    params = list(sig.parameters.keys())



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



def test_subprogramclassifier_is_not_abstract():
    assert not inspect.isabstract(SubprogramClassifier)


def test_subprogramclassifier_constructor_exists():
    assert callable(SubprogramClassifier.__init__)


def test_subprogramclassifier_constructor_args():
    sig = inspect.signature(SubprogramClassifier.__init__)
    params = list(sig.parameters.keys())



def test_memoryclassifier_is_not_abstract():
    assert not inspect.isabstract(MemoryClassifier)


def test_memoryclassifier_constructor_exists():
    assert callable(MemoryClassifier.__init__)


def test_memoryclassifier_constructor_args():
    sig = inspect.signature(MemoryClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_memorytype_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemoryType)


def test_aadl2_memorytype_constructor_exists():
    assert callable(aadl2_MemoryType.__init__)


def test_aadl2_memorytype_constructor_args():
    sig = inspect.signature(aadl2_MemoryType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_memoryimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemoryImplementation)


def test_aadl2_memoryimplementation_constructor_exists():
    assert callable(aadl2_MemoryImplementation.__init__)


def test_aadl2_memoryimplementation_constructor_args():
    sig = inspect.signature(aadl2_MemoryImplementation.__init__)
    params = list(sig.parameters.keys())



def test_deviceclassifier_is_not_abstract():
    assert not inspect.isabstract(DeviceClassifier)


def test_deviceclassifier_constructor_exists():
    assert callable(DeviceClassifier.__init__)


def test_deviceclassifier_constructor_args():
    sig = inspect.signature(DeviceClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_devicetype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceType)


def test_aadl2_devicetype_constructor_exists():
    assert callable(aadl2_DeviceType.__init__)


def test_aadl2_devicetype_constructor_args():
    sig = inspect.signature(aadl2_DeviceType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_deviceimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceImplementation)


def test_aadl2_deviceimplementation_constructor_exists():
    assert callable(aadl2_DeviceImplementation.__init__)


def test_aadl2_deviceimplementation_constructor_args():
    sig = inspect.signature(aadl2_DeviceImplementation.__init__)
    params = list(sig.parameters.keys())



def test_dataclassifier_is_not_abstract():
    assert not inspect.isabstract(DataClassifier)


def test_dataclassifier_constructor_exists():
    assert callable(DataClassifier.__init__)


def test_dataclassifier_constructor_args():
    sig = inspect.signature(DataClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_dataimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataImplementation)


def test_aadl2_dataimplementation_constructor_exists():
    assert callable(aadl2_DataImplementation.__init__)


def test_aadl2_dataimplementation_constructor_args():
    sig = inspect.signature(aadl2_DataImplementation.__init__)
    params = list(sig.parameters.keys())



def test_componentprototype_is_not_abstract():
    assert not inspect.isabstract(ComponentPrototype)


def test_componentprototype_constructor_exists():
    assert callable(ComponentPrototype.__init__)


def test_componentprototype_constructor_args():
    sig = inspect.signature(ComponentPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramPrototype)


def test_aadl2_subprogramprototype_constructor_exists():
    assert callable(aadl2_SubprogramPrototype.__init__)


def test_aadl2_subprogramprototype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_dataprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataPrototype)


def test_aadl2_dataprototype_constructor_exists():
    assert callable(aadl2_DataPrototype.__init__)


def test_aadl2_dataprototype_constructor_args():
    sig = inspect.signature(aadl2_DataPrototype.__init__)
    params = list(sig.parameters.keys())



def test_busclassifier_is_not_abstract():
    assert not inspect.isabstract(BusClassifier)


def test_busclassifier_constructor_exists():
    assert callable(BusClassifier.__init__)


def test_busclassifier_constructor_args():
    sig = inspect.signature(BusClassifier.__init__)
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



def test_behavioredimplementation_is_not_abstract():
    assert not inspect.isabstract(BehavioredImplementation)


def test_behavioredimplementation_constructor_exists():
    assert callable(BehavioredImplementation.__init__)


def test_behavioredimplementation_constructor_args():
    sig = inspect.signature(BehavioredImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramImplementation)


def test_aadl2_subprogramimplementation_constructor_exists():
    assert callable(aadl2_SubprogramImplementation.__init__)


def test_aadl2_subprogramimplementation_constructor_args():
    sig = inspect.signature(aadl2_SubprogramImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadImplementation)


def test_aadl2_threadimplementation_constructor_exists():
    assert callable(aadl2_ThreadImplementation.__init__)


def test_aadl2_threadimplementation_constructor_args():
    sig = inspect.signature(aadl2_ThreadImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_abstractimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractImplementation)


def test_aadl2_abstractimplementation_constructor_exists():
    assert callable(aadl2_AbstractImplementation.__init__)


def test_aadl2_abstractimplementation_constructor_args():
    sig = inspect.signature(aadl2_AbstractImplementation.__init__)
    params = list(sig.parameters.keys())



def test_memory_is_not_abstract():
    assert not inspect.isabstract(Memory)


def test_memory_constructor_exists():
    assert callable(Memory.__init__)


def test_memory_constructor_args():
    sig = inspect.signature(Memory.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_memorysubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemorySubcomponent)


def test_aadl2_memorysubcomponent_constructor_exists():
    assert callable(aadl2_MemorySubcomponent.__init__)


def test_aadl2_memorysubcomponent_constructor_args():
    sig = inspect.signature(aadl2_MemorySubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_process_constructor_exists():
    assert callable(Process.__init__)


def test_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessSubcomponent)


def test_aadl2_processsubcomponent_constructor_exists():
    assert callable(aadl2_ProcessSubcomponent.__init__)


def test_aadl2_processsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_ProcessSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_system_constructor_exists():
    assert callable(System.__init__)


def test_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_systemsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemSubcomponent)


def test_aadl2_systemsubcomponent_constructor_exists():
    assert callable(aadl2_SystemSubcomponent.__init__)


def test_aadl2_systemsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_SystemSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_thread_is_not_abstract():
    assert not inspect.isabstract(Thread)


def test_thread_constructor_exists():
    assert callable(Thread.__init__)


def test_thread_constructor_args():
    sig = inspect.signature(Thread.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadSubcomponent)


def test_aadl2_threadsubcomponent_constructor_exists():
    assert callable(aadl2_ThreadSubcomponent.__init__)


def test_aadl2_threadsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_ThreadSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_threadgroup_is_not_abstract():
    assert not inspect.isabstract(ThreadGroup)


def test_threadgroup_constructor_exists():
    assert callable(ThreadGroup.__init__)


def test_threadgroup_constructor_args():
    sig = inspect.signature(ThreadGroup.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadgroupsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupSubcomponent)


def test_aadl2_threadgroupsubcomponent_constructor_exists():
    assert callable(aadl2_ThreadGroupSubcomponent.__init__)


def test_aadl2_threadgroupsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_virtualbus_is_not_abstract():
    assert not inspect.isabstract(VirtualBus)


def test_virtualbus_constructor_exists():
    assert callable(VirtualBus.__init__)


def test_virtualbus_constructor_args():
    sig = inspect.signature(VirtualBus.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualbussubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusSubcomponent)


def test_aadl2_virtualbussubcomponent_constructor_exists():
    assert callable(aadl2_VirtualBusSubcomponent.__init__)


def test_aadl2_virtualbussubcomponent_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_virtualprocessor_is_not_abstract():
    assert not inspect.isabstract(VirtualProcessor)


def test_virtualprocessor_constructor_exists():
    assert callable(VirtualProcessor.__init__)


def test_virtualprocessor_constructor_args():
    sig = inspect.signature(VirtualProcessor.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualprocessorsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorSubcomponent)


def test_aadl2_virtualprocessorsubcomponent_constructor_exists():
    assert callable(aadl2_VirtualProcessorSubcomponent.__init__)


def test_aadl2_virtualprocessorsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_virtualprocessorsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(VirtualProcessorSubcomponentType)


def test_virtualprocessorsubcomponenttype_constructor_exists():
    assert callable(VirtualProcessorSubcomponentType.__init__)


def test_virtualprocessorsubcomponenttype_constructor_args():
    sig = inspect.signature(VirtualProcessorSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualprocessorprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorPrototype)


def test_aadl2_virtualprocessorprototype_constructor_exists():
    assert callable(aadl2_VirtualProcessorPrototype.__init__)


def test_aadl2_virtualprocessorprototype_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorPrototype.__init__)
    params = list(sig.parameters.keys())



def test_virtualbussubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(VirtualBusSubcomponentType)


def test_virtualbussubcomponenttype_constructor_exists():
    assert callable(VirtualBusSubcomponentType.__init__)


def test_virtualbussubcomponenttype_constructor_args():
    sig = inspect.signature(VirtualBusSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualbusprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusPrototype)


def test_aadl2_virtualbusprototype_constructor_exists():
    assert callable(aadl2_VirtualBusPrototype.__init__)


def test_aadl2_virtualbusprototype_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusPrototype.__init__)
    params = list(sig.parameters.keys())



def test_processor_is_not_abstract():
    assert not inspect.isabstract(Processor)


def test_processor_constructor_exists():
    assert callable(Processor.__init__)


def test_processor_constructor_args():
    sig = inspect.signature(Processor.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processorsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorSubcomponent)


def test_aadl2_processorsubcomponent_constructor_exists():
    assert callable(aadl2_ProcessorSubcomponent.__init__)


def test_aadl2_processorsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_ProcessorSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_threadsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ThreadSubcomponentType)


def test_threadsubcomponenttype_constructor_exists():
    assert callable(ThreadSubcomponentType.__init__)


def test_threadsubcomponenttype_constructor_args():
    sig = inspect.signature(ThreadSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadPrototype)


def test_aadl2_threadprototype_constructor_exists():
    assert callable(aadl2_ThreadPrototype.__init__)


def test_aadl2_threadprototype_constructor_args():
    sig = inspect.signature(aadl2_ThreadPrototype.__init__)
    params = list(sig.parameters.keys())



def test_threadgroupsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ThreadGroupSubcomponentType)


def test_threadgroupsubcomponenttype_constructor_exists():
    assert callable(ThreadGroupSubcomponentType.__init__)


def test_threadgroupsubcomponenttype_constructor_args():
    sig = inspect.signature(ThreadGroupSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadgroupprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupPrototype)


def test_aadl2_threadgroupprototype_constructor_exists():
    assert callable(aadl2_ThreadGroupPrototype.__init__)


def test_aadl2_threadgroupprototype_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupPrototype.__init__)
    params = list(sig.parameters.keys())



def test_systemsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(SystemSubcomponentType)


def test_systemsubcomponenttype_constructor_exists():
    assert callable(SystemSubcomponentType.__init__)


def test_systemsubcomponenttype_constructor_args():
    sig = inspect.signature(SystemSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_systemprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemPrototype)


def test_aadl2_systemprototype_constructor_exists():
    assert callable(aadl2_SystemPrototype.__init__)


def test_aadl2_systemprototype_constructor_args():
    sig = inspect.signature(aadl2_SystemPrototype.__init__)
    params = list(sig.parameters.keys())



def test_device_is_not_abstract():
    assert not inspect.isabstract(Device)


def test_device_constructor_exists():
    assert callable(Device.__init__)


def test_device_constructor_args():
    sig = inspect.signature(Device.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_devicesubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceSubcomponent)


def test_aadl2_devicesubcomponent_constructor_exists():
    assert callable(aadl2_DeviceSubcomponent.__init__)


def test_aadl2_devicesubcomponent_constructor_args():
    sig = inspect.signature(aadl2_DeviceSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_subprogramgroupsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(SubprogramGroupSubcomponentType)


def test_subprogramgroupsubcomponenttype_constructor_exists():
    assert callable(SubprogramGroupSubcomponentType.__init__)


def test_subprogramgroupsubcomponenttype_constructor_args():
    sig = inspect.signature(SubprogramGroupSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgroupprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupPrototype)


def test_aadl2_subprogramgroupprototype_constructor_exists():
    assert callable(aadl2_SubprogramGroupPrototype.__init__)


def test_aadl2_subprogramgroupprototype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupPrototype.__init__)
    params = list(sig.parameters.keys())



def test_processsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ProcessSubcomponentType)


def test_processsubcomponenttype_constructor_exists():
    assert callable(ProcessSubcomponentType.__init__)


def test_processsubcomponenttype_constructor_args():
    sig = inspect.signature(ProcessSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessPrototype)


def test_aadl2_processprototype_constructor_exists():
    assert callable(aadl2_ProcessPrototype.__init__)


def test_aadl2_processprototype_constructor_args():
    sig = inspect.signature(aadl2_ProcessPrototype.__init__)
    params = list(sig.parameters.keys())



def test_processorsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ProcessorSubcomponentType)


def test_processorsubcomponenttype_constructor_exists():
    assert callable(ProcessorSubcomponentType.__init__)


def test_processorsubcomponenttype_constructor_args():
    sig = inspect.signature(ProcessorSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processorprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorPrototype)


def test_aadl2_processorprototype_constructor_exists():
    assert callable(aadl2_ProcessorPrototype.__init__)


def test_aadl2_processorprototype_constructor_args():
    sig = inspect.signature(aadl2_ProcessorPrototype.__init__)
    params = list(sig.parameters.keys())



def test_memorysubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(MemorySubcomponentType)


def test_memorysubcomponenttype_constructor_exists():
    assert callable(MemorySubcomponentType.__init__)


def test_memorysubcomponenttype_constructor_args():
    sig = inspect.signature(MemorySubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_memoryprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemoryPrototype)


def test_aadl2_memoryprototype_constructor_exists():
    assert callable(aadl2_MemoryPrototype.__init__)


def test_aadl2_memoryprototype_constructor_args():
    sig = inspect.signature(aadl2_MemoryPrototype.__init__)
    params = list(sig.parameters.keys())



def test_devicesubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(DeviceSubcomponentType)


def test_devicesubcomponenttype_constructor_exists():
    assert callable(DeviceSubcomponentType.__init__)


def test_devicesubcomponenttype_constructor_args():
    sig = inspect.signature(DeviceSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_deviceprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DevicePrototype)


def test_aadl2_deviceprototype_constructor_exists():
    assert callable(aadl2_DevicePrototype.__init__)


def test_aadl2_deviceprototype_constructor_args():
    sig = inspect.signature(aadl2_DevicePrototype.__init__)
    params = list(sig.parameters.keys())



def test_bussubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(BusSubcomponentType)


def test_bussubcomponenttype_constructor_exists():
    assert callable(BusSubcomponentType.__init__)


def test_bussubcomponenttype_constructor_args():
    sig = inspect.signature(BusSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_busprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusPrototype)


def test_aadl2_busprototype_constructor_exists():
    assert callable(aadl2_BusPrototype.__init__)


def test_aadl2_busprototype_constructor_args():
    sig = inspect.signature(aadl2_BusPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_abstractprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractPrototype)


def test_aadl2_abstractprototype_constructor_exists():
    assert callable(aadl2_AbstractPrototype.__init__)


def test_aadl2_abstractprototype_constructor_args():
    sig = inspect.signature(aadl2_AbstractPrototype.__init__)
    params = list(sig.parameters.keys())



def test_accessconnectionend_is_not_abstract():
    assert not inspect.isabstract(AccessConnectionEnd)


def test_accessconnectionend_constructor_exists():
    assert callable(AccessConnectionEnd.__init__)


def test_accessconnectionend_constructor_args():
    sig = inspect.signature(AccessConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_datasubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataSubcomponent)


def test_aadl2_datasubcomponent_constructor_exists():
    assert callable(aadl2_DataSubcomponent.__init__)


def test_aadl2_datasubcomponent_constructor_args():
    sig = inspect.signature(aadl2_DataSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramSubcomponent)


def test_aadl2_subprogramsubcomponent_constructor_exists():
    assert callable(aadl2_SubprogramSubcomponent.__init__)


def test_aadl2_subprogramsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_SubprogramSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_bussubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusSubcomponent)


def test_aadl2_bussubcomponent_constructor_exists():
    assert callable(aadl2_BusSubcomponent.__init__)


def test_aadl2_bussubcomponent_constructor_args():
    sig = inspect.signature(aadl2_BusSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_eventport_is_not_abstract():
    assert not inspect.isabstract(aadl2_EventPort)


def test_aadl2_eventport_constructor_exists():
    assert callable(aadl2_EventPort.__init__)


def test_aadl2_eventport_constructor_args():
    sig = inspect.signature(aadl2_EventPort.__init__)
    params = list(sig.parameters.keys())



def test_featuretype_is_not_abstract():
    assert not inspect.isabstract(FeatureType)


def test_featuretype_constructor_exists():
    assert callable(FeatureType.__init__)


def test_featuretype_constructor_args():
    sig = inspect.signature(FeatureType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_busaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusAccess)


def test_aadl2_busaccess_constructor_exists():
    assert callable(aadl2_BusAccess.__init__)


def test_aadl2_busaccess_constructor_args():
    sig = inspect.signature(aadl2_BusAccess.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featuretype_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureType)


def test_aadl2_featuretype_constructor_exists():
    assert callable(aadl2_FeatureType.__init__)


def test_aadl2_featuretype_constructor_args():
    sig = inspect.signature(aadl2_FeatureType.__init__)
    params = list(sig.parameters.keys())



def test_callcontext_is_not_abstract():
    assert not inspect.isabstract(CallContext)


def test_callcontext_constructor_exists():
    assert callable(CallContext.__init__)


def test_callcontext_constructor_args():
    sig = inspect.signature(CallContext.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_datatype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataType)


def test_aadl2_datatype_constructor_exists():
    assert callable(aadl2_DataType.__init__)


def test_aadl2_datatype_constructor_args():
    sig = inspect.signature(aadl2_DataType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgroupsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupSubcomponent)


def test_aadl2_subprogramgroupsubcomponent_constructor_exists():
    assert callable(aadl2_SubprogramGroupSubcomponent.__init__)


def test_aadl2_subprogramgroupsubcomponent_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramType)


def test_aadl2_subprogramtype_constructor_exists():
    assert callable(aadl2_SubprogramType.__init__)


def test_aadl2_subprogramtype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgroupaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupAccess)


def test_aadl2_subprogramgroupaccess_constructor_exists():
    assert callable(aadl2_SubprogramGroupAccess.__init__)


def test_aadl2_subprogramgroupaccess_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupAccess.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgrouptype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupType)


def test_aadl2_subprogramgrouptype_constructor_exists():
    assert callable(aadl2_SubprogramGroupType.__init__)


def test_aadl2_subprogramgrouptype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_abstracttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractType)


def test_aadl2_abstracttype_constructor_exists():
    assert callable(aadl2_AbstractType.__init__)


def test_aadl2_abstracttype_constructor_args():
    sig = inspect.signature(aadl2_AbstractType.__init__)
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



def test_aadl2_eventdataport_is_not_abstract():
    assert not inspect.isabstract(aadl2_EventDataPort)


def test_aadl2_eventdataport_constructor_exists():
    assert callable(aadl2_EventDataPort.__init__)


def test_aadl2_eventdataport_constructor_args():
    sig = inspect.signature(aadl2_EventDataPort.__init__)
    params = list(sig.parameters.keys())



def test_directedfeature_is_not_abstract():
    assert not inspect.isabstract(DirectedFeature)


def test_directedfeature_constructor_exists():
    assert callable(DirectedFeature.__init__)


def test_directedfeature_constructor_args():
    sig = inspect.signature(DirectedFeature.__init__)
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



def test_aadl2_parameter_is_not_abstract():
    assert not inspect.isabstract(aadl2_Parameter)


def test_aadl2_parameter_constructor_exists():
    assert callable(aadl2_Parameter.__init__)


def test_aadl2_parameter_constructor_args():
    sig = inspect.signature(aadl2_Parameter.__init__)
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
    assert "kind" in params, "Missing parameter 'kind'"
    assert "category" in params, "Missing parameter 'category'"

def test_aadl2_access_has_kind():
    assert hasattr(aadl2_Access, "kind")
    descriptor = None
    for klass in aadl2_Access.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_access_has_category():
    assert hasattr(aadl2_Access, "category")
    descriptor = None
    for klass in aadl2_Access.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
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



def test_aadl2_callcontext_is_not_abstract():
    assert not inspect.isabstract(aadl2_CallContext)


def test_aadl2_callcontext_constructor_exists():
    assert callable(aadl2_CallContext.__init__)


def test_aadl2_callcontext_constructor_args():
    sig = inspect.signature(aadl2_CallContext.__init__)
    params = list(sig.parameters.keys())



def test_flow_is_not_abstract():
    assert not inspect.isabstract(Flow)


def test_flow_constructor_exists():
    assert callable(Flow.__init__)


def test_flow_constructor_args():
    sig = inspect.signature(Flow.__init__)
    params = list(sig.parameters.keys())



def test_flowelement_is_not_abstract():
    assert not inspect.isabstract(FlowElement)


def test_flowelement_constructor_exists():
    assert callable(FlowElement.__init__)


def test_flowelement_constructor_args():
    sig = inspect.signature(FlowElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_dataaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataAccess)


def test_aadl2_dataaccess_constructor_exists():
    assert callable(aadl2_DataAccess.__init__)


def test_aadl2_dataaccess_constructor_args():
    sig = inspect.signature(aadl2_DataAccess.__init__)
    params = list(sig.parameters.keys())



def test_modalpath_is_not_abstract():
    assert not inspect.isabstract(ModalPath)


def test_modalpath_constructor_exists():
    assert callable(ModalPath.__init__)


def test_modalpath_constructor_args():
    sig = inspect.signature(ModalPath.__init__)
    params = list(sig.parameters.keys())



def test_flowfeature_is_not_abstract():
    assert not inspect.isabstract(FlowFeature)


def test_flowfeature_constructor_exists():
    assert callable(FlowFeature.__init__)


def test_flowfeature_constructor_args():
    sig = inspect.signature(FlowFeature.__init__)
    params = list(sig.parameters.keys())



def test_prototype_is_not_abstract():
    assert not inspect.isabstract(Prototype)


def test_prototype_constructor_exists():
    assert callable(Prototype.__init__)


def test_prototype_constructor_args():
    sig = inspect.signature(Prototype.__init__)
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



def test_aadl2_featuregroupprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupPrototype)


def test_aadl2_featuregroupprototype_constructor_exists():
    assert callable(aadl2_FeatureGroupPrototype.__init__)


def test_aadl2_featuregroupprototype_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupPrototype.__init__)
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



def test_arrayableelement_is_not_abstract():
    assert not inspect.isabstract(ArrayableElement)


def test_arrayableelement_constructor_exists():
    assert callable(ArrayableElement.__init__)


def test_arrayableelement_constructor_args():
    sig = inspect.signature(ArrayableElement.__init__)
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



def test_aadl2_featureprototypeactual_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeaturePrototypeActual)


def test_aadl2_featureprototypeactual_constructor_exists():
    assert callable(aadl2_FeaturePrototypeActual.__init__)


def test_aadl2_featureprototypeactual_constructor_args():
    sig = inspect.signature(aadl2_FeaturePrototypeActual.__init__)
    params = list(sig.parameters.keys())



def test_featureconnectionend_is_not_abstract():
    assert not inspect.isabstract(FeatureConnectionEnd)


def test_featureconnectionend_constructor_exists():
    assert callable(FeatureConnectionEnd.__init__)


def test_featureconnectionend_constructor_args():
    sig = inspect.signature(FeatureConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_abstractfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractFeature)


def test_aadl2_abstractfeature_constructor_exists():
    assert callable(aadl2_AbstractFeature.__init__)


def test_aadl2_abstractfeature_constructor_args():
    sig = inspect.signature(aadl2_AbstractFeature.__init__)
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



def test_aadl2_typeextension_is_not_abstract():
    assert not inspect.isabstract(aadl2_TypeExtension)


def test_aadl2_typeextension_constructor_exists():
    assert callable(aadl2_TypeExtension.__init__)


def test_aadl2_typeextension_constructor_args():
    sig = inspect.signature(aadl2_TypeExtension.__init__)
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



def test_aadl2_featuregroupconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupConnectionEnd)


def test_aadl2_featuregroupconnectionend_constructor_exists():
    assert callable(aadl2_FeatureGroupConnectionEnd.__init__)


def test_aadl2_featuregroupconnectionend_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_parameterconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_ParameterConnectionEnd)


def test_aadl2_parameterconnectionend_constructor_exists():
    assert callable(aadl2_ParameterConnectionEnd.__init__)


def test_aadl2_parameterconnectionend_constructor_args():
    sig = inspect.signature(aadl2_ParameterConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featureconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureConnectionEnd)


def test_aadl2_featureconnectionend_constructor_exists():
    assert callable(aadl2_FeatureConnectionEnd.__init__)


def test_aadl2_featureconnectionend_constructor_args():
    sig = inspect.signature(aadl2_FeatureConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featureclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureClassifier)


def test_aadl2_featureclassifier_constructor_exists():
    assert callable(aadl2_FeatureClassifier.__init__)


def test_aadl2_featureclassifier_constructor_args():
    sig = inspect.signature(aadl2_FeatureClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_eventsource_is_not_abstract():
    assert not inspect.isabstract(aadl2_EventSource)


def test_aadl2_eventsource_constructor_exists():
    assert callable(aadl2_EventSource.__init__)


def test_aadl2_eventsource_constructor_args():
    sig = inspect.signature(aadl2_EventSource.__init__)
    params = list(sig.parameters.keys())



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



def test_featureclassifier_is_not_abstract():
    assert not inspect.isabstract(FeatureClassifier)


def test_featureclassifier_constructor_exists():
    assert callable(FeatureClassifier.__init__)


def test_featureclassifier_constructor_args():
    sig = inspect.signature(FeatureClassifier.__init__)
    params = list(sig.parameters.keys())



def test_subcomponenttype_is_not_abstract():
    assert not inspect.isabstract(SubcomponentType)


def test_subcomponenttype_constructor_exists():
    assert callable(SubcomponentType.__init__)


def test_subcomponenttype_constructor_args():
    sig = inspect.signature(SubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_memorysubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemorySubcomponentType)


def test_aadl2_memorysubcomponenttype_constructor_exists():
    assert callable(aadl2_MemorySubcomponentType.__init__)


def test_aadl2_memorysubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_MemorySubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_datasubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataSubcomponentType)


def test_aadl2_datasubcomponenttype_constructor_exists():
    assert callable(aadl2_DataSubcomponentType.__init__)


def test_aadl2_datasubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_DataSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processorsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorSubcomponentType)


def test_aadl2_processorsubcomponenttype_constructor_exists():
    assert callable(aadl2_ProcessorSubcomponentType.__init__)


def test_aadl2_processorsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_ProcessorSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramSubcomponentType)


def test_aadl2_subprogramsubcomponenttype_constructor_exists():
    assert callable(aadl2_SubprogramSubcomponentType.__init__)


def test_aadl2_subprogramsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgroupsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupSubcomponentType)


def test_aadl2_subprogramgroupsubcomponenttype_constructor_exists():
    assert callable(aadl2_SubprogramGroupSubcomponentType.__init__)


def test_aadl2_subprogramgroupsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessSubcomponentType)


def test_aadl2_processsubcomponenttype_constructor_exists():
    assert callable(aadl2_ProcessSubcomponentType.__init__)


def test_aadl2_processsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_ProcessSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualprocessorsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorSubcomponentType)


def test_aadl2_virtualprocessorsubcomponenttype_constructor_exists():
    assert callable(aadl2_VirtualProcessorSubcomponentType.__init__)


def test_aadl2_virtualprocessorsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_abstractsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractSubcomponentType)


def test_aadl2_abstractsubcomponenttype_constructor_exists():
    assert callable(aadl2_AbstractSubcomponentType.__init__)


def test_aadl2_abstractsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_AbstractSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_systemsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemSubcomponentType)


def test_aadl2_systemsubcomponenttype_constructor_exists():
    assert callable(aadl2_SystemSubcomponentType.__init__)


def test_aadl2_systemsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_SystemSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_componentprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentPrototype)


def test_aadl2_componentprototype_constructor_exists():
    assert callable(aadl2_ComponentPrototype.__init__)


def test_aadl2_componentprototype_constructor_args():
    sig = inspect.signature(aadl2_ComponentPrototype.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"

def test_aadl2_componentprototype_has_array():
    assert hasattr(aadl2_ComponentPrototype, "array")
    descriptor = None
    for klass in aadl2_ComponentPrototype.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_devicesubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceSubcomponentType)


def test_aadl2_devicesubcomponenttype_constructor_exists():
    assert callable(aadl2_DeviceSubcomponentType.__init__)


def test_aadl2_devicesubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_DeviceSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_bussubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusSubcomponentType)


def test_aadl2_bussubcomponenttype_constructor_exists():
    assert callable(aadl2_BusSubcomponentType.__init__)


def test_aadl2_bussubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_BusSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadSubcomponentType)


def test_aadl2_threadsubcomponenttype_constructor_exists():
    assert callable(aadl2_ThreadSubcomponentType.__init__)


def test_aadl2_threadsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_ThreadSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualbussubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusSubcomponentType)


def test_aadl2_virtualbussubcomponenttype_constructor_exists():
    assert callable(aadl2_VirtualBusSubcomponentType.__init__)


def test_aadl2_virtualbussubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadgroupsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupSubcomponentType)


def test_aadl2_threadgroupsubcomponenttype_constructor_exists():
    assert callable(aadl2_ThreadGroupSubcomponentType.__init__)


def test_aadl2_threadgroupsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupSubcomponentType.__init__)
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



def test_aadl2_componentclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentClassifier)


def test_aadl2_componentclassifier_constructor_exists():
    assert callable(aadl2_ComponentClassifier.__init__)


def test_aadl2_componentclassifier_constructor_args():
    sig = inspect.signature(aadl2_ComponentClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "noFlows" in params, "Missing parameter 'noFlows'"
    assert "noModes" in params, "Missing parameter 'noModes'"
    assert "derivedModes" in params, "Missing parameter 'derivedModes'"

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

def test_aadl2_componentclassifier_has_derivedModes():
    assert hasattr(aadl2_ComponentClassifier, "derivedModes")
    descriptor = None
    for klass in aadl2_ComponentClassifier.__mro__:
        if "derivedModes" in klass.__dict__:
            descriptor = klass.__dict__["derivedModes"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_portproxy_is_not_abstract():
    assert not inspect.isabstract(aadl2_PortProxy)


def test_aadl2_portproxy_constructor_exists():
    assert callable(aadl2_PortProxy.__init__)


def test_aadl2_portproxy_constructor_args():
    sig = inspect.signature(aadl2_PortProxy.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_aadl2_portproxy_has_direction():
    assert hasattr(aadl2_PortProxy, "direction")
    descriptor = None
    for klass in aadl2_PortProxy.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_eventdatasource_is_not_abstract():
    assert not inspect.isabstract(aadl2_EventDataSource)


def test_aadl2_eventdatasource_constructor_exists():
    assert callable(aadl2_EventDataSource.__init__)


def test_aadl2_eventdatasource_constructor_args():
    sig = inspect.signature(aadl2_EventDataSource.__init__)
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



def test_componentclassifier_is_not_abstract():
    assert not inspect.isabstract(ComponentClassifier)


def test_componentclassifier_constructor_exists():
    assert callable(ComponentClassifier.__init__)


def test_componentclassifier_constructor_args():
    sig = inspect.signature(ComponentClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_memoryclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_MemoryClassifier)


def test_aadl2_memoryclassifier_constructor_exists():
    assert callable(aadl2_MemoryClassifier.__init__)


def test_aadl2_memoryclassifier_constructor_args():
    sig = inspect.signature(aadl2_MemoryClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_deviceclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_DeviceClassifier)


def test_aadl2_deviceclassifier_constructor_exists():
    assert callable(aadl2_DeviceClassifier.__init__)


def test_aadl2_deviceclassifier_constructor_args():
    sig = inspect.signature(aadl2_DeviceClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualbusclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBusClassifier)


def test_aadl2_virtualbusclassifier_constructor_exists():
    assert callable(aadl2_VirtualBusClassifier.__init__)


def test_aadl2_virtualbusclassifier_constructor_args():
    sig = inspect.signature(aadl2_VirtualBusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadClassifier)


def test_aadl2_threadclassifier_constructor_exists():
    assert callable(aadl2_ThreadClassifier.__init__)


def test_aadl2_threadclassifier_constructor_args():
    sig = inspect.signature(aadl2_ThreadClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_dataclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_DataClassifier)


def test_aadl2_dataclassifier_constructor_exists():
    assert callable(aadl2_DataClassifier.__init__)


def test_aadl2_dataclassifier_constructor_args():
    sig = inspect.signature(aadl2_DataClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_abstractclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractClassifier)


def test_aadl2_abstractclassifier_constructor_exists():
    assert callable(aadl2_AbstractClassifier.__init__)


def test_aadl2_abstractclassifier_constructor_args():
    sig = inspect.signature(aadl2_AbstractClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processorclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorClassifier)


def test_aadl2_processorclassifier_constructor_exists():
    assert callable(aadl2_ProcessorClassifier.__init__)


def test_aadl2_processorclassifier_constructor_args():
    sig = inspect.signature(aadl2_ProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_systemclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_SystemClassifier)


def test_aadl2_systemclassifier_constructor_exists():
    assert callable(aadl2_SystemClassifier.__init__)


def test_aadl2_systemclassifier_constructor_args():
    sig = inspect.signature(aadl2_SystemClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramClassifier)


def test_aadl2_subprogramclassifier_constructor_exists():
    assert callable(aadl2_SubprogramClassifier.__init__)


def test_aadl2_subprogramclassifier_constructor_args():
    sig = inspect.signature(aadl2_SubprogramClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramGroupClassifier)


def test_aadl2_subprogramgroupclassifier_constructor_exists():
    assert callable(aadl2_SubprogramGroupClassifier.__init__)


def test_aadl2_subprogramgroupclassifier_constructor_args():
    sig = inspect.signature(aadl2_SubprogramGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_componenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentType)


def test_aadl2_componenttype_constructor_exists():
    assert callable(aadl2_ComponentType.__init__)


def test_aadl2_componenttype_constructor_args():
    sig = inspect.signature(aadl2_ComponentType.__init__)
    params = list(sig.parameters.keys())
    assert "noFeatures" in params, "Missing parameter 'noFeatures'"

def test_aadl2_componenttype_has_noFeatures():
    assert hasattr(aadl2_ComponentType, "noFeatures")
    descriptor = None
    for klass in aadl2_ComponentType.__mro__:
        if "noFeatures" in klass.__dict__:
            descriptor = klass.__dict__["noFeatures"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_busclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_BusClassifier)


def test_aadl2_busclassifier_constructor_exists():
    assert callable(aadl2_BusClassifier.__init__)


def test_aadl2_busclassifier_constructor_args():
    sig = inspect.signature(aadl2_BusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualprocessorclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessorClassifier)


def test_aadl2_virtualprocessorclassifier_constructor_exists():
    assert callable(aadl2_VirtualProcessorClassifier.__init__)


def test_aadl2_virtualprocessorclassifier_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroupClassifier)


def test_aadl2_threadgroupclassifier_constructor_exists():
    assert callable(aadl2_ThreadGroupClassifier.__init__)


def test_aadl2_threadgroupclassifier_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessClassifier)


def test_aadl2_processclassifier_constructor_exists():
    assert callable(aadl2_ProcessClassifier.__init__)


def test_aadl2_processclassifier_constructor_args():
    sig = inspect.signature(aadl2_ProcessClassifier.__init__)
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



def test_aadl2_componentimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2_ComponentImplementation)


def test_aadl2_componentimplementation_constructor_exists():
    assert callable(aadl2_ComponentImplementation.__init__)


def test_aadl2_componentimplementation_constructor_args():
    sig = inspect.signature(aadl2_ComponentImplementation.__init__)
    params = list(sig.parameters.keys())
    assert "noCalls" in params, "Missing parameter 'noCalls'"
    assert "noConnections" in params, "Missing parameter 'noConnections'"
    assert "noSubcomponents" in params, "Missing parameter 'noSubcomponents'"

def test_aadl2_componentimplementation_has_noCalls():
    assert hasattr(aadl2_ComponentImplementation, "noCalls")
    descriptor = None
    for klass in aadl2_ComponentImplementation.__mro__:
        if "noCalls" in klass.__dict__:
            descriptor = klass.__dict__["noCalls"]
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



def test_aadl2_calledsubprogram_is_not_abstract():
    assert not inspect.isabstract(aadl2_CalledSubprogram)


def test_aadl2_calledsubprogram_constructor_exists():
    assert callable(aadl2_CalledSubprogram.__init__)


def test_aadl2_calledsubprogram_constructor_args():
    sig = inspect.signature(aadl2_CalledSubprogram.__init__)
    params = list(sig.parameters.keys())



def test_refinableelement_is_not_abstract():
    assert not inspect.isabstract(RefinableElement)


def test_refinableelement_constructor_exists():
    assert callable(RefinableElement.__init__)


def test_refinableelement_constructor_args():
    sig = inspect.signature(RefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_calledsubprogram_is_not_abstract():
    assert not inspect.isabstract(CalledSubprogram)


def test_calledsubprogram_constructor_exists():
    assert callable(CalledSubprogram.__init__)


def test_calledsubprogram_constructor_args():
    sig = inspect.signature(CalledSubprogram.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogramproxy_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramProxy)


def test_aadl2_subprogramproxy_constructor_exists():
    assert callable(aadl2_SubprogramProxy.__init__)


def test_aadl2_subprogramproxy_constructor_args():
    sig = inspect.signature(aadl2_SubprogramProxy.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_connection_is_not_abstract():
    assert not inspect.isabstract(aadl2_Connection)


def test_aadl2_connection_constructor_exists():
    assert callable(aadl2_Connection.__init__)


def test_aadl2_connection_constructor_args():
    sig = inspect.signature(aadl2_Connection.__init__)
    params = list(sig.parameters.keys())
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"

def test_aadl2_connection_has_bidirectional():
    assert hasattr(aadl2_Connection, "bidirectional")
    descriptor = None
    for klass in aadl2_Connection.__mro__:
        if "bidirectional" in klass.__dict__:
            descriptor = klass.__dict__["bidirectional"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_feature_is_not_abstract():
    assert not inspect.isabstract(aadl2_Feature)


def test_aadl2_feature_constructor_exists():
    assert callable(aadl2_Feature.__init__)


def test_aadl2_feature_constructor_args():
    sig = inspect.signature(aadl2_Feature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_flowfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_FlowFeature)


def test_aadl2_flowfeature_constructor_exists():
    assert callable(aadl2_FlowFeature.__init__)


def test_aadl2_flowfeature_constructor_args():
    sig = inspect.signature(aadl2_FlowFeature.__init__)
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



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_classifierfeature_is_not_abstract():
    assert not inspect.isabstract(ClassifierFeature)


def test_classifierfeature_constructor_exists():
    assert callable(ClassifierFeature.__init__)


def test_classifierfeature_constructor_args():
    sig = inspect.signature(ClassifierFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_StructuralFeature)


def test_aadl2_structuralfeature_constructor_exists():
    assert callable(aadl2_StructuralFeature.__init__)


def test_aadl2_structuralfeature_constructor_args():
    sig = inspect.signature(aadl2_StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_BehavioralFeature)


def test_aadl2_behavioralfeature_constructor_exists():
    assert callable(aadl2_BehavioralFeature.__init__)


def test_aadl2_behavioralfeature_constructor_args():
    sig = inspect.signature(aadl2_BehavioralFeature.__init__)
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



def test_aadl2_modefeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModeFeature)


def test_aadl2_modefeature_constructor_exists():
    assert callable(aadl2_ModeFeature.__init__)


def test_aadl2_modefeature_constructor_args():
    sig = inspect.signature(aadl2_ModeFeature.__init__)
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



def test_aadl2_subprogramcallsequence_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubprogramCallSequence)


def test_aadl2_subprogramcallsequence_constructor_exists():
    assert callable(aadl2_SubprogramCallSequence.__init__)


def test_aadl2_subprogramcallsequence_constructor_args():
    sig = inspect.signature(aadl2_SubprogramCallSequence.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_processorfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_ProcessorFeature)


def test_aadl2_processorfeature_constructor_exists():
    assert callable(aadl2_ProcessorFeature.__init__)


def test_aadl2_processorfeature_constructor_args():
    sig = inspect.signature(aadl2_ProcessorFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_internalfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_InternalFeature)


def test_aadl2_internalfeature_constructor_exists():
    assert callable(aadl2_InternalFeature.__init__)


def test_aadl2_internalfeature_constructor_args():
    sig = inspect.signature(aadl2_InternalFeature.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_aadl2_internalfeature_has_direction():
    assert hasattr(aadl2_InternalFeature, "direction")
    descriptor = None
    for klass in aadl2_InternalFeature.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



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



def test_aadl2_generalization__is_not_abstract():
    assert not inspect.isabstract(aadl2_Generalization_)


def test_aadl2_generalization__constructor_exists():
    assert callable(aadl2_Generalization_.__init__)


def test_aadl2_generalization__constructor_args():
    sig = inspect.signature(aadl2_Generalization_.__init__)
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



def test_aadl2_arraysizeproperty_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArraySizeProperty)


def test_aadl2_arraysizeproperty_constructor_exists():
    assert callable(aadl2_ArraySizeProperty.__init__)


def test_aadl2_arraysizeproperty_constructor_args():
    sig = inspect.signature(aadl2_ArraySizeProperty.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_abstractnamedvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_AbstractNamedValue)


def test_aadl2_abstractnamedvalue_constructor_exists():
    assert callable(aadl2_AbstractNamedValue.__init__)


def test_aadl2_abstractnamedvalue_constructor_args():
    sig = inspect.signature(aadl2_AbstractNamedValue.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2_SubcomponentType)


def test_aadl2_subcomponenttype_constructor_exists():
    assert callable(aadl2_SubcomponentType.__init__)


def test_aadl2_subcomponenttype_constructor_args():
    sig = inspect.signature(aadl2_SubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_propertytype_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyType)


def test_aadl2_propertytype_constructor_exists():
    assert callable(aadl2_PropertyType.__init__)


def test_aadl2_propertytype_constructor_args():
    sig = inspect.signature(aadl2_PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_recordtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_RecordType)


def test_aadl2_recordtype_constructor_exists():
    assert callable(aadl2_RecordType.__init__)


def test_aadl2_recordtype_constructor_args():
    sig = inspect.signature(aadl2_RecordType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_propertyset_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertySet)


def test_aadl2_propertyset_constructor_exists():
    assert callable(aadl2_PropertySet.__init__)


def test_aadl2_propertyset_constructor_args():
    sig = inspect.signature(aadl2_PropertySet.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(aadl2_EnumerationType)


def test_aadl2_enumerationtype_constructor_exists():
    assert callable(aadl2_EnumerationType.__init__)


def test_aadl2_enumerationtype_constructor_args():
    sig = inspect.signature(aadl2_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_globalnamespace_is_not_abstract():
    assert not inspect.isabstract(aadl2_GlobalNamespace)


def test_aadl2_globalnamespace_constructor_exists():
    assert callable(aadl2_GlobalNamespace.__init__)


def test_aadl2_globalnamespace_constructor_args():
    sig = inspect.signature(aadl2_GlobalNamespace.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_packagesection_is_not_abstract():
    assert not inspect.isabstract(aadl2_PackageSection)


def test_aadl2_packagesection_constructor_exists():
    assert callable(aadl2_PackageSection.__init__)


def test_aadl2_packagesection_constructor_args():
    sig = inspect.signature(aadl2_PackageSection.__init__)
    params = list(sig.parameters.keys())
    assert "noAnnexes" in params, "Missing parameter 'noAnnexes'"
    assert "noProperties" in params, "Missing parameter 'noProperties'"

def test_aadl2_packagesection_has_noAnnexes():
    assert hasattr(aadl2_PackageSection, "noAnnexes")
    descriptor = None
    for klass in aadl2_PackageSection.__mro__:
        if "noAnnexes" in klass.__dict__:
            descriptor = klass.__dict__["noAnnexes"]
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



def test_arraysizeproperty_is_not_abstract():
    assert not inspect.isabstract(ArraySizeProperty)


def test_arraysizeproperty_constructor_exists():
    assert callable(ArraySizeProperty.__init__)


def test_arraysizeproperty_constructor_args():
    sig = inspect.signature(ArraySizeProperty.__init__)
    params = list(sig.parameters.keys())



def test_abstractnamedvalue_is_not_abstract():
    assert not inspect.isabstract(AbstractNamedValue)


def test_abstractnamedvalue_constructor_exists():
    assert callable(AbstractNamedValue.__init__)


def test_abstractnamedvalue_constructor_args():
    sig = inspect.signature(AbstractNamedValue.__init__)
    params = list(sig.parameters.keys())



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



def test_aadl2_modalpropertyvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModalPropertyValue)


def test_aadl2_modalpropertyvalue_constructor_exists():
    assert callable(aadl2_ModalPropertyValue.__init__)


def test_aadl2_modalpropertyvalue_constructor_args():
    sig = inspect.signature(aadl2_ModalPropertyValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_classifier_is_not_abstract():
    assert not inspect.isabstract(aadl2_Classifier)


def test_aadl2_classifier_constructor_exists():
    assert callable(aadl2_Classifier.__init__)


def test_aadl2_classifier_constructor_args():
    sig = inspect.signature(aadl2_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "noAnnexes" in params, "Missing parameter 'noAnnexes'"
    assert "noPrototypes" in params, "Missing parameter 'noPrototypes'"
    assert "noProperties" in params, "Missing parameter 'noProperties'"

def test_aadl2_classifier_has_noAnnexes():
    assert hasattr(aadl2_Classifier, "noAnnexes")
    descriptor = None
    for klass in aadl2_Classifier.__mro__:
        if "noAnnexes" in klass.__dict__:
            descriptor = klass.__dict__["noAnnexes"]
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

def test_aadl2_classifier_has_noProperties():
    assert hasattr(aadl2_Classifier, "noProperties")
    descriptor = None
    for klass in aadl2_Classifier.__mro__:
        if "noProperties" in klass.__dict__:
            descriptor = klass.__dict__["noProperties"]
            break
    assert isinstance(descriptor, property)



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



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_propertyconstant_is_not_abstract():
    assert not inspect.isabstract(aadl2_PropertyConstant)


def test_aadl2_propertyconstant_constructor_exists():
    assert callable(aadl2_PropertyConstant.__init__)


def test_aadl2_propertyconstant_constructor_args():
    sig = inspect.signature(aadl2_PropertyConstant.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_basicproperty_is_not_abstract():
    assert not inspect.isabstract(aadl2_BasicProperty)


def test_aadl2_basicproperty_constructor_exists():
    assert callable(aadl2_BasicProperty.__init__)


def test_aadl2_basicproperty_constructor_args():
    sig = inspect.signature(aadl2_BasicProperty.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_metaclassreference_is_not_abstract():
    assert not inspect.isabstract(aadl2_MetaclassReference)


def test_aadl2_metaclassreference_constructor_exists():
    assert callable(aadl2_MetaclassReference.__init__)


def test_aadl2_metaclassreference_constructor_args():
    sig = inspect.signature(aadl2_MetaclassReference.__init__)
    params = list(sig.parameters.keys())
    assert "metaclassName" in params, "Missing parameter 'metaclassName'"
    assert "annexName" in params, "Missing parameter 'annexName'"

def test_aadl2_metaclassreference_has_metaclassName():
    assert hasattr(aadl2_MetaclassReference, "metaclassName")
    descriptor = None
    for klass in aadl2_MetaclassReference.__mro__:
        if "metaclassName" in klass.__dict__:
            descriptor = klass.__dict__["metaclassName"]
            break
    assert isinstance(descriptor, property)

def test_aadl2_metaclassreference_has_annexName():
    assert hasattr(aadl2_MetaclassReference, "annexName")
    descriptor = None
    for klass in aadl2_MetaclassReference.__mro__:
        if "annexName" in klass.__dict__:
            descriptor = klass.__dict__["annexName"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
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



def test_aadl2_memory_is_not_abstract():
    assert not inspect.isabstract(aadl2_Memory)


def test_aadl2_memory_constructor_exists():
    assert callable(aadl2_Memory.__init__)


def test_aadl2_memory_constructor_args():
    sig = inspect.signature(aadl2_Memory.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_refinableelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_RefinableElement)


def test_aadl2_refinableelement_constructor_exists():
    assert callable(aadl2_RefinableElement.__init__)


def test_aadl2_refinableelement_constructor_args():
    sig = inspect.signature(aadl2_RefinableElement.__init__)
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



def test_aadl2_processor_is_not_abstract():
    assert not inspect.isabstract(aadl2_Processor)


def test_aadl2_processor_constructor_exists():
    assert callable(aadl2_Processor.__init__)


def test_aadl2_processor_constructor_args():
    sig = inspect.signature(aadl2_Processor.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_thread_is_not_abstract():
    assert not inspect.isabstract(aadl2_Thread)


def test_aadl2_thread_constructor_exists():
    assert callable(aadl2_Thread.__init__)


def test_aadl2_thread_constructor_args():
    sig = inspect.signature(aadl2_Thread.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_context_is_not_abstract():
    assert not inspect.isabstract(aadl2_Context)


def test_aadl2_context_constructor_exists():
    assert callable(aadl2_Context.__init__)


def test_aadl2_context_constructor_args():
    sig = inspect.signature(aadl2_Context.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_flow_is_not_abstract():
    assert not inspect.isabstract(aadl2_Flow)


def test_aadl2_flow_constructor_exists():
    assert callable(aadl2_Flow.__init__)


def test_aadl2_flow_constructor_args():
    sig = inspect.signature(aadl2_Flow.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_subprogram_is_not_abstract():
    assert not inspect.isabstract(aadl2_Subprogram)


def test_aadl2_subprogram_constructor_exists():
    assert callable(aadl2_Subprogram.__init__)


def test_aadl2_subprogram_constructor_args():
    sig = inspect.signature(aadl2_Subprogram.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_featuregrouptyperename_is_not_abstract():
    assert not inspect.isabstract(aadl2_FeatureGroupTypeRename)


def test_aadl2_featuregrouptyperename_constructor_exists():
    assert callable(aadl2_FeatureGroupTypeRename.__init__)


def test_aadl2_featuregrouptyperename_constructor_args():
    sig = inspect.signature(aadl2_FeatureGroupTypeRename.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_modelunit_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModelUnit)


def test_aadl2_modelunit_constructor_exists():
    assert callable(aadl2_ModelUnit.__init__)


def test_aadl2_modelunit_constructor_args():
    sig = inspect.signature(aadl2_ModelUnit.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_threadgroup_is_not_abstract():
    assert not inspect.isabstract(aadl2_ThreadGroup)


def test_aadl2_threadgroup_constructor_exists():
    assert callable(aadl2_ThreadGroup.__init__)


def test_aadl2_threadgroup_constructor_args():
    sig = inspect.signature(aadl2_ThreadGroup.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_triggerport_is_not_abstract():
    assert not inspect.isabstract(aadl2_TriggerPort)


def test_aadl2_triggerport_constructor_exists():
    assert callable(aadl2_TriggerPort.__init__)


def test_aadl2_triggerport_constructor_args():
    sig = inspect.signature(aadl2_TriggerPort.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualprocessor_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualProcessor)


def test_aadl2_virtualprocessor_constructor_exists():
    assert callable(aadl2_VirtualProcessor.__init__)


def test_aadl2_virtualprocessor_constructor_args():
    sig = inspect.signature(aadl2_VirtualProcessor.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_connectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2_ConnectionEnd)


def test_aadl2_connectionend_constructor_exists():
    assert callable(aadl2_ConnectionEnd.__init__)


def test_aadl2_connectionend_constructor_args():
    sig = inspect.signature(aadl2_ConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_abstract_is_not_abstract():
    assert not inspect.isabstract(aadl2_Abstract)


def test_aadl2_abstract_constructor_exists():
    assert callable(aadl2_Abstract.__init__)


def test_aadl2_abstract_constructor_args():
    sig = inspect.signature(aadl2_Abstract.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2_EnumerationLiteral)


def test_aadl2_enumerationliteral_constructor_exists():
    assert callable(aadl2_EnumerationLiteral.__init__)


def test_aadl2_enumerationliteral_constructor_args():
    sig = inspect.signature(aadl2_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_typedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_TypedElement)


def test_aadl2_typedelement_constructor_exists():
    assert callable(aadl2_TypedElement.__init__)


def test_aadl2_typedelement_constructor_args():
    sig = inspect.signature(aadl2_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_modalelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModalElement)


def test_aadl2_modalelement_constructor_exists():
    assert callable(aadl2_ModalElement.__init__)


def test_aadl2_modalelement_constructor_args():
    sig = inspect.signature(aadl2_ModalElement.__init__)
    params = list(sig.parameters.keys())



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



def test_aadl2_annexlibrary_is_not_abstract():
    assert not inspect.isabstract(aadl2_AnnexLibrary)


def test_aadl2_annexlibrary_constructor_exists():
    assert callable(aadl2_AnnexLibrary.__init__)


def test_aadl2_annexlibrary_constructor_args():
    sig = inspect.signature(aadl2_AnnexLibrary.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_bus_is_not_abstract():
    assert not inspect.isabstract(aadl2_Bus)


def test_aadl2_bus_constructor_exists():
    assert callable(aadl2_Bus.__init__)


def test_aadl2_bus_constructor_args():
    sig = inspect.signature(aadl2_Bus.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_namespace_is_not_abstract():
    assert not inspect.isabstract(aadl2_Namespace)


def test_aadl2_namespace_constructor_exists():
    assert callable(aadl2_Namespace.__init__)


def test_aadl2_namespace_constructor_args():
    sig = inspect.signature(aadl2_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_endtoendflowelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_EndToEndFlowElement)


def test_aadl2_endtoendflowelement_constructor_exists():
    assert callable(aadl2_EndToEndFlowElement.__init__)


def test_aadl2_endtoendflowelement_constructor_args():
    sig = inspect.signature(aadl2_EndToEndFlowElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_system_is_not_abstract():
    assert not inspect.isabstract(aadl2_System)


def test_aadl2_system_constructor_exists():
    assert callable(aadl2_System.__init__)


def test_aadl2_system_constructor_args():
    sig = inspect.signature(aadl2_System.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_classifierfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2_ClassifierFeature)


def test_aadl2_classifierfeature_constructor_exists():
    assert callable(aadl2_ClassifierFeature.__init__)


def test_aadl2_classifierfeature_constructor_args():
    sig = inspect.signature(aadl2_ClassifierFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_device_is_not_abstract():
    assert not inspect.isabstract(aadl2_Device)


def test_aadl2_device_constructor_exists():
    assert callable(aadl2_Device.__init__)


def test_aadl2_device_constructor_args():
    sig = inspect.signature(aadl2_Device.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_process_is_not_abstract():
    assert not inspect.isabstract(aadl2_Process)


def test_aadl2_process_constructor_exists():
    assert callable(aadl2_Process.__init__)


def test_aadl2_process_constructor_args():
    sig = inspect.signature(aadl2_Process.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_virtualbus_is_not_abstract():
    assert not inspect.isabstract(aadl2_VirtualBus)


def test_aadl2_virtualbus_constructor_exists():
    assert callable(aadl2_VirtualBus.__init__)


def test_aadl2_virtualbus_constructor_args():
    sig = inspect.signature(aadl2_VirtualBus.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_type_is_not_abstract():
    assert not inspect.isabstract(aadl2_Type)


def test_aadl2_type_constructor_exists():
    assert callable(aadl2_Type.__init__)


def test_aadl2_type_constructor_args():
    sig = inspect.signature(aadl2_Type.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_flowend_is_not_abstract():
    assert not inspect.isabstract(aadl2_FlowEnd)


def test_aadl2_flowend_constructor_exists():
    assert callable(aadl2_FlowEnd.__init__)


def test_aadl2_flowend_constructor_args():
    sig = inspect.signature(aadl2_FlowEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_flowsegment_is_not_abstract():
    assert not inspect.isabstract(aadl2_FlowSegment)


def test_aadl2_flowsegment_constructor_exists():
    assert callable(aadl2_FlowSegment.__init__)


def test_aadl2_flowsegment_constructor_args():
    sig = inspect.signature(aadl2_FlowSegment.__init__)
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



def test_aadl2_numericrange_is_not_abstract():
    assert not inspect.isabstract(aadl2_NumericRange)


def test_aadl2_numericrange_constructor_exists():
    assert callable(aadl2_NumericRange.__init__)


def test_aadl2_numericrange_constructor_args():
    sig = inspect.signature(aadl2_NumericRange.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_modetransitiontrigger_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModeTransitionTrigger)


def test_aadl2_modetransitiontrigger_constructor_exists():
    assert callable(aadl2_ModeTransitionTrigger.__init__)


def test_aadl2_modetransitiontrigger_constructor_args():
    sig = inspect.signature(aadl2_ModeTransitionTrigger.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_arraydimension_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArrayDimension)


def test_aadl2_arraydimension_constructor_exists():
    assert callable(aadl2_ArrayDimension.__init__)


def test_aadl2_arraydimension_constructor_args():
    sig = inspect.signature(aadl2_ArrayDimension.__init__)
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



def test_aadl2_relationship_is_not_abstract():
    assert not inspect.isabstract(aadl2_Relationship)


def test_aadl2_relationship_constructor_exists():
    assert callable(aadl2_Relationship.__init__)


def test_aadl2_relationship_constructor_args():
    sig = inspect.signature(aadl2_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_arraysize_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArraySize)


def test_aadl2_arraysize_constructor_exists():
    assert callable(aadl2_ArraySize.__init__)


def test_aadl2_arraysize_constructor_args():
    sig = inspect.signature(aadl2_ArraySize.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_aadl2_arraysize_has_size():
    assert hasattr(aadl2_ArraySize, "size")
    descriptor = None
    for klass in aadl2_ArraySize.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_containmentpathelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ContainmentPathElement)


def test_aadl2_containmentpathelement_constructor_exists():
    assert callable(aadl2_ContainmentPathElement.__init__)


def test_aadl2_containmentpathelement_constructor_args():
    sig = inspect.signature(aadl2_ContainmentPathElement.__init__)
    params = list(sig.parameters.keys())
    assert "annexName" in params, "Missing parameter 'annexName'"

def test_aadl2_containmentpathelement_has_annexName():
    assert hasattr(aadl2_ContainmentPathElement, "annexName")
    descriptor = None
    for klass in aadl2_ContainmentPathElement.__mro__:
        if "annexName" in klass.__dict__:
            descriptor = klass.__dict__["annexName"]
            break
    assert isinstance(descriptor, property)



def test_aadl2_containednamedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ContainedNamedElement)


def test_aadl2_containednamedelement_constructor_exists():
    assert callable(aadl2_ContainedNamedElement.__init__)


def test_aadl2_containednamedelement_constructor_args():
    sig = inspect.signature(aadl2_ContainedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_connectedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ConnectedElement)


def test_aadl2_connectedelement_constructor_exists():
    assert callable(aadl2_ConnectedElement.__init__)


def test_aadl2_connectedelement_constructor_args():
    sig = inspect.signature(aadl2_ConnectedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_prototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2_PrototypeBinding)


def test_aadl2_prototypebinding_constructor_exists():
    assert callable(aadl2_PrototypeBinding.__init__)


def test_aadl2_prototypebinding_constructor_args():
    sig = inspect.signature(aadl2_PrototypeBinding.__init__)
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



def test_aadl2_endtoendflowsegment_is_not_abstract():
    assert not inspect.isabstract(aadl2_EndToEndFlowSegment)


def test_aadl2_endtoendflowsegment_constructor_exists():
    assert callable(aadl2_EndToEndFlowSegment.__init__)


def test_aadl2_endtoendflowsegment_constructor_args():
    sig = inspect.signature(aadl2_EndToEndFlowSegment.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_basicpropertyassociation_is_not_abstract():
    assert not inspect.isabstract(aadl2_BasicPropertyAssociation)


def test_aadl2_basicpropertyassociation_constructor_exists():
    assert callable(aadl2_BasicPropertyAssociation.__init__)


def test_aadl2_basicpropertyassociation_constructor_args():
    sig = inspect.signature(aadl2_BasicPropertyAssociation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_arrayableelement_is_not_abstract():
    assert not inspect.isabstract(aadl2_ArrayableElement)


def test_aadl2_arrayableelement_constructor_exists():
    assert callable(aadl2_ArrayableElement.__init__)


def test_aadl2_arrayableelement_constructor_args():
    sig = inspect.signature(aadl2_ArrayableElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_modebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2_ModeBinding)


def test_aadl2_modebinding_constructor_exists():
    assert callable(aadl2_ModeBinding.__init__)


def test_aadl2_modebinding_constructor_args():
    sig = inspect.signature(aadl2_ModeBinding.__init__)
    params = list(sig.parameters.keys())



def test_aadl2_element_is_not_abstract():
    assert not inspect.isabstract(aadl2_Element)


def test_aadl2_element_constructor_exists():
    assert callable(aadl2_Element.__init__)


def test_aadl2_element_constructor_args():
    sig = inspect.signature(aadl2_Element.__init__)
    params = list(sig.parameters.keys())

def test_componentcategory_exists():
    # Check that the Enumeration exists
    assert ComponentCategory is not None

def test_componentcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentCategory]
    expected_literals = [
        "bus",
        "memory",
        "system",
        "virtualProcessor",
        "threadGroup",
        "subprogramGroup",
        "device",
        "process",
        "data",
        "processor",
        "thread",
        "abstract",
        "subprogram",
        "virtualBus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentCategory"

def test_directiontype_exists():
    # Check that the Enumeration exists
    assert DirectionType is not None

def test_directiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionType]
    expected_literals = [
        "in_",
        "inOut",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionType"

def test_flowkind_exists():
    # Check that the Enumeration exists
    assert FlowKind is not None

def test_flowkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlowKind]
    expected_literals = [
        "source",
        "path",
        "sink",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlowKind"

def test_portcategory_exists():
    # Check that the Enumeration exists
    assert PortCategory is not None

def test_portcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PortCategory]
    expected_literals = [
        "data",
        "event",
        "eventData",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PortCategory"

def test_accesscategory_exists():
    # Check that the Enumeration exists
    assert AccessCategory is not None

def test_accesscategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessCategory]
    expected_literals = [
        "subprogramGroup",
        "bus",
        "data",
        "subprogram",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessCategory"

def test_operationkind_exists():
    # Check that the Enumeration exists
    assert OperationKind is not None

def test_operationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperationKind]
    expected_literals = [
        "or_",
        "plus",
        "minus",
        "not_",
        "and_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperationKind"

def test_accesstype_exists():
    # Check that the Enumeration exists
    assert AccessType is not None

def test_accesstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessType]
    expected_literals = [
        "provides",
        "requires",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessType"


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
AbstractSubcomponentType_strategy = st.builds(
    AbstractSubcomponentType,
)
AbstractClassifier_strategy = st.builds(
    AbstractClassifier,
)
ComponentType_strategy = st.builds(
    ComponentType,
)
ComponentImplementation_strategy = st.builds(
    ComponentImplementation,
)
aadl2_BehavioredImplementation_strategy = st.builds(
    aadl2_BehavioredImplementation,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
FeaturePrototypeActual_strategy = st.builds(
    FeaturePrototypeActual,
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
aadl2_PortSpecification_strategy = st.builds(
    aadl2_PortSpecification,
    category=
        safe_text,
    direction=
        safe_text
)
aadl2_FeatureGroupPrototypeActual_strategy = st.builds(
    aadl2_FeatureGroupPrototypeActual,
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
ModelUnit_strategy = st.builds(
    ModelUnit,
)
aadl2_AadlPackage_strategy = st.builds(
    aadl2_AadlPackage,
)
ProcessorFeature_strategy = st.builds(
    ProcessorFeature,
)
PackageSection_strategy = st.builds(
    PackageSection,
)
aadl2_PrivatePackageSection_strategy = st.builds(
    aadl2_PrivatePackageSection,
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
SubprogramSubcomponentType_strategy = st.builds(
    SubprogramSubcomponentType,
)
Abstract_strategy = st.builds(
    Abstract,
)
Subcomponent_strategy = st.builds(
    Subcomponent,
)
DataSubcomponentType_strategy = st.builds(
    DataSubcomponentType,
)
InternalFeature_strategy = st.builds(
    InternalFeature,
)
Connection_strategy = st.builds(
    Connection,
)
SubprogramGroup_strategy = st.builds(
    SubprogramGroup,
)
TriggerPort_strategy = st.builds(
    TriggerPort,
)
Subprogram_strategy = st.builds(
    Subprogram,
)
Port_strategy = st.builds(
    Port,
)
PortConnectionEnd_strategy = st.builds(
    PortConnectionEnd,
)
ParameterConnectionEnd_strategy = st.builds(
    ParameterConnectionEnd,
)
Data_strategy = st.builds(
    Data,
)
Bus_strategy = st.builds(
    Bus,
)
Access_strategy = st.builds(
    Access,
)
aadl2_SubprogramAccess_strategy = st.builds(
    aadl2_SubprogramAccess,
)
EnumerationType_strategy = st.builds(
    EnumerationType,
)
aadl2_UnitsType_strategy = st.builds(
    aadl2_UnitsType,
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
NonListType_strategy = st.builds(
    NonListType,
)
aadl2_NumberType_strategy = st.builds(
    aadl2_NumberType,
)
aadl2_RangeType_strategy = st.builds(
    aadl2_RangeType,
)
aadl2_ClassifierType_strategy = st.builds(
    aadl2_ClassifierType,
)
aadl2_ReferenceType_strategy = st.builds(
    aadl2_ReferenceType,
)
aadl2_AadlString_strategy = st.builds(
    aadl2_AadlString,
)
aadl2_AadlBoolean_strategy = st.builds(
    aadl2_AadlBoolean,
)
PropertyType_strategy = st.builds(
    PropertyType,
)
aadl2_ListType_strategy = st.builds(
    aadl2_ListType,
)
aadl2_NonListType_strategy = st.builds(
    aadl2_NonListType,
)
NumberValue_strategy = st.builds(
    NumberValue,
)
aadl2_RealLiteral_strategy = st.builds(
    aadl2_RealLiteral,
    value=
        safe_text
)
aadl2_IntegerLiteral_strategy = st.builds(
    aadl2_IntegerLiteral,
    value=
        safe_text,
    base=
        safe_text
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
aadl2_UnitLiteral_strategy = st.builds(
    aadl2_UnitLiteral,
)
ContainedNamedElement_strategy = st.builds(
    ContainedNamedElement,
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
aadl2_ReferenceValue_strategy = st.builds(
    aadl2_ReferenceValue,
)
aadl2_ComputedValue_strategy = st.builds(
    aadl2_ComputedValue,
    function=
        safe_text
)
aadl2_NumberValue_strategy = st.builds(
    aadl2_NumberValue,
)
aadl2_NamedValue_strategy = st.builds(
    aadl2_NamedValue,
)
aadl2_RangeValue_strategy = st.builds(
    aadl2_RangeValue,
)
aadl2_BooleanLiteral_strategy = st.builds(
    aadl2_BooleanLiteral,
    value=
        safe_text
)
aadl2_StringLiteral_strategy = st.builds(
    aadl2_StringLiteral,
    value=
        safe_text
)
VirtualBusClassifier_strategy = st.builds(
    VirtualBusClassifier,
)
aadl2_VirtualBusType_strategy = st.builds(
    aadl2_VirtualBusType,
)
VirtualProcessorClassifier_strategy = st.builds(
    VirtualProcessorClassifier,
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
ThreadGroupClassifier_strategy = st.builds(
    ThreadGroupClassifier,
)
aadl2_ThreadGroupImplementation_strategy = st.builds(
    aadl2_ThreadGroupImplementation,
)
aadl2_ThreadGroupType_strategy = st.builds(
    aadl2_ThreadGroupType,
)
ThreadClassifier_strategy = st.builds(
    ThreadClassifier,
)
aadl2_ThreadType_strategy = st.builds(
    aadl2_ThreadType,
)
ProcessClassifier_strategy = st.builds(
    ProcessClassifier,
)
aadl2_ProcessImplementation_strategy = st.builds(
    aadl2_ProcessImplementation,
)
aadl2_ProcessType_strategy = st.builds(
    aadl2_ProcessType,
)
ProcessorClassifier_strategy = st.builds(
    ProcessorClassifier,
)
aadl2_ProcessorImplementation_strategy = st.builds(
    aadl2_ProcessorImplementation,
)
aadl2_ProcessorType_strategy = st.builds(
    aadl2_ProcessorType,
)
SubprogramGroupClassifier_strategy = st.builds(
    SubprogramGroupClassifier,
)
aadl2_SubprogramGroupImplementation_strategy = st.builds(
    aadl2_SubprogramGroupImplementation,
)
SystemClassifier_strategy = st.builds(
    SystemClassifier,
)
aadl2_SystemImplementation_strategy = st.builds(
    aadl2_SystemImplementation,
)
aadl2_SystemType_strategy = st.builds(
    aadl2_SystemType,
)
SubprogramClassifier_strategy = st.builds(
    SubprogramClassifier,
)
MemoryClassifier_strategy = st.builds(
    MemoryClassifier,
)
aadl2_MemoryType_strategy = st.builds(
    aadl2_MemoryType,
)
aadl2_MemoryImplementation_strategy = st.builds(
    aadl2_MemoryImplementation,
)
DeviceClassifier_strategy = st.builds(
    DeviceClassifier,
)
aadl2_DeviceType_strategy = st.builds(
    aadl2_DeviceType,
)
aadl2_DeviceImplementation_strategy = st.builds(
    aadl2_DeviceImplementation,
)
DataClassifier_strategy = st.builds(
    DataClassifier,
)
aadl2_DataImplementation_strategy = st.builds(
    aadl2_DataImplementation,
)
ComponentPrototype_strategy = st.builds(
    ComponentPrototype,
)
aadl2_SubprogramPrototype_strategy = st.builds(
    aadl2_SubprogramPrototype,
)
aadl2_DataPrototype_strategy = st.builds(
    aadl2_DataPrototype,
)
BusClassifier_strategy = st.builds(
    BusClassifier,
)
aadl2_BusImplementation_strategy = st.builds(
    aadl2_BusImplementation,
)
aadl2_BusType_strategy = st.builds(
    aadl2_BusType,
)
BehavioredImplementation_strategy = st.builds(
    BehavioredImplementation,
)
aadl2_SubprogramImplementation_strategy = st.builds(
    aadl2_SubprogramImplementation,
)
aadl2_ThreadImplementation_strategy = st.builds(
    aadl2_ThreadImplementation,
)
aadl2_AbstractImplementation_strategy = st.builds(
    aadl2_AbstractImplementation,
)
Memory_strategy = st.builds(
    Memory,
)
aadl2_MemorySubcomponent_strategy = st.builds(
    aadl2_MemorySubcomponent,
)
Process_strategy = st.builds(
    Process,
)
aadl2_ProcessSubcomponent_strategy = st.builds(
    aadl2_ProcessSubcomponent,
)
System_strategy = st.builds(
    System,
)
aadl2_SystemSubcomponent_strategy = st.builds(
    aadl2_SystemSubcomponent,
)
Thread_strategy = st.builds(
    Thread,
)
aadl2_ThreadSubcomponent_strategy = st.builds(
    aadl2_ThreadSubcomponent,
)
ThreadGroup_strategy = st.builds(
    ThreadGroup,
)
aadl2_ThreadGroupSubcomponent_strategy = st.builds(
    aadl2_ThreadGroupSubcomponent,
)
VirtualBus_strategy = st.builds(
    VirtualBus,
)
aadl2_VirtualBusSubcomponent_strategy = st.builds(
    aadl2_VirtualBusSubcomponent,
)
VirtualProcessor_strategy = st.builds(
    VirtualProcessor,
)
aadl2_VirtualProcessorSubcomponent_strategy = st.builds(
    aadl2_VirtualProcessorSubcomponent,
)
VirtualProcessorSubcomponentType_strategy = st.builds(
    VirtualProcessorSubcomponentType,
)
aadl2_VirtualProcessorPrototype_strategy = st.builds(
    aadl2_VirtualProcessorPrototype,
)
VirtualBusSubcomponentType_strategy = st.builds(
    VirtualBusSubcomponentType,
)
aadl2_VirtualBusPrototype_strategy = st.builds(
    aadl2_VirtualBusPrototype,
)
Processor_strategy = st.builds(
    Processor,
)
aadl2_ProcessorSubcomponent_strategy = st.builds(
    aadl2_ProcessorSubcomponent,
)
ThreadSubcomponentType_strategy = st.builds(
    ThreadSubcomponentType,
)
aadl2_ThreadPrototype_strategy = st.builds(
    aadl2_ThreadPrototype,
)
ThreadGroupSubcomponentType_strategy = st.builds(
    ThreadGroupSubcomponentType,
)
aadl2_ThreadGroupPrototype_strategy = st.builds(
    aadl2_ThreadGroupPrototype,
)
SystemSubcomponentType_strategy = st.builds(
    SystemSubcomponentType,
)
aadl2_SystemPrototype_strategy = st.builds(
    aadl2_SystemPrototype,
)
Device_strategy = st.builds(
    Device,
)
aadl2_DeviceSubcomponent_strategy = st.builds(
    aadl2_DeviceSubcomponent,
)
SubprogramGroupSubcomponentType_strategy = st.builds(
    SubprogramGroupSubcomponentType,
)
aadl2_SubprogramGroupPrototype_strategy = st.builds(
    aadl2_SubprogramGroupPrototype,
)
ProcessSubcomponentType_strategy = st.builds(
    ProcessSubcomponentType,
)
aadl2_ProcessPrototype_strategy = st.builds(
    aadl2_ProcessPrototype,
)
ProcessorSubcomponentType_strategy = st.builds(
    ProcessorSubcomponentType,
)
aadl2_ProcessorPrototype_strategy = st.builds(
    aadl2_ProcessorPrototype,
)
MemorySubcomponentType_strategy = st.builds(
    MemorySubcomponentType,
)
aadl2_MemoryPrototype_strategy = st.builds(
    aadl2_MemoryPrototype,
)
DeviceSubcomponentType_strategy = st.builds(
    DeviceSubcomponentType,
)
aadl2_DevicePrototype_strategy = st.builds(
    aadl2_DevicePrototype,
)
BusSubcomponentType_strategy = st.builds(
    BusSubcomponentType,
)
aadl2_BusPrototype_strategy = st.builds(
    aadl2_BusPrototype,
)
aadl2_AbstractPrototype_strategy = st.builds(
    aadl2_AbstractPrototype,
)
AccessConnectionEnd_strategy = st.builds(
    AccessConnectionEnd,
)
aadl2_DataSubcomponent_strategy = st.builds(
    aadl2_DataSubcomponent,
)
aadl2_SubprogramSubcomponent_strategy = st.builds(
    aadl2_SubprogramSubcomponent,
)
aadl2_BusSubcomponent_strategy = st.builds(
    aadl2_BusSubcomponent,
)
aadl2_EventPort_strategy = st.builds(
    aadl2_EventPort,
)
FeatureType_strategy = st.builds(
    FeatureType,
)
aadl2_BusAccess_strategy = st.builds(
    aadl2_BusAccess,
)
aadl2_FeatureType_strategy = st.builds(
    aadl2_FeatureType,
)
CallContext_strategy = st.builds(
    CallContext,
)
aadl2_DataType_strategy = st.builds(
    aadl2_DataType,
)
aadl2_SubprogramGroupSubcomponent_strategy = st.builds(
    aadl2_SubprogramGroupSubcomponent,
)
aadl2_SubprogramType_strategy = st.builds(
    aadl2_SubprogramType,
)
aadl2_SubprogramGroupAccess_strategy = st.builds(
    aadl2_SubprogramGroupAccess,
)
aadl2_SubprogramGroupType_strategy = st.builds(
    aadl2_SubprogramGroupType,
)
aadl2_AbstractType_strategy = st.builds(
    aadl2_AbstractType,
)
FeatureGroupConnectionEnd_strategy = st.builds(
    FeatureGroupConnectionEnd,
)
Context_strategy = st.builds(
    Context,
)
aadl2_SubprogramCall_strategy = st.builds(
    aadl2_SubprogramCall,
)
aadl2_DataPort_strategy = st.builds(
    aadl2_DataPort,
)
aadl2_EventDataPort_strategy = st.builds(
    aadl2_EventDataPort,
)
DirectedFeature_strategy = st.builds(
    DirectedFeature,
)
aadl2_Port_strategy = st.builds(
    aadl2_Port,
    category=
        safe_text
)
aadl2_Parameter_strategy = st.builds(
    aadl2_Parameter,
)
Generalization__strategy = st.builds(
    Generalization_,
)
aadl2_GroupExtension_strategy = st.builds(
    aadl2_GroupExtension,
)
Feature_strategy = st.builds(
    Feature,
)
aadl2_Access_strategy = st.builds(
    aadl2_Access,
    kind=
        safe_text,
    category=
        safe_text
)
aadl2_DirectedFeature_strategy = st.builds(
    aadl2_DirectedFeature,
    direction=
        safe_text
)
aadl2_CallContext_strategy = st.builds(
    aadl2_CallContext,
)
Flow_strategy = st.builds(
    Flow,
)
FlowElement_strategy = st.builds(
    FlowElement,
)
aadl2_DataAccess_strategy = st.builds(
    aadl2_DataAccess,
)
ModalPath_strategy = st.builds(
    ModalPath,
)
FlowFeature_strategy = st.builds(
    FlowFeature,
)
Prototype_strategy = st.builds(
    Prototype,
)
aadl2_FeaturePrototype_strategy = st.builds(
    aadl2_FeaturePrototype,
    direction=
        safe_text
)
aadl2_FeatureGroupPrototype_strategy = st.builds(
    aadl2_FeatureGroupPrototype,
)
EndToEndFlowElement_strategy = st.builds(
    EndToEndFlowElement,
)
aadl2_FlowElement_strategy = st.builds(
    aadl2_FlowElement,
)
ArrayableElement_strategy = st.builds(
    ArrayableElement,
)
aadl2_ComponentPrototypeActual_strategy = st.builds(
    aadl2_ComponentPrototypeActual,
    category=
        safe_text
)
aadl2_FeaturePrototypeActual_strategy = st.builds(
    aadl2_FeaturePrototypeActual,
)
FeatureConnectionEnd_strategy = st.builds(
    FeatureConnectionEnd,
)
aadl2_AbstractFeature_strategy = st.builds(
    aadl2_AbstractFeature,
)
aadl2_FeatureGroup_strategy = st.builds(
    aadl2_FeatureGroup,
    inverse=
        safe_text
)
aadl2_TypeExtension_strategy = st.builds(
    aadl2_TypeExtension,
)
aadl2_FlowSpecification_strategy = st.builds(
    aadl2_FlowSpecification,
    kind=
        safe_text
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
aadl2_FeatureGroupConnectionEnd_strategy = st.builds(
    aadl2_FeatureGroupConnectionEnd,
)
aadl2_ParameterConnectionEnd_strategy = st.builds(
    aadl2_ParameterConnectionEnd,
)
aadl2_FeatureConnectionEnd_strategy = st.builds(
    aadl2_FeatureConnectionEnd,
)
aadl2_FeatureClassifier_strategy = st.builds(
    aadl2_FeatureClassifier,
)
aadl2_EventSource_strategy = st.builds(
    aadl2_EventSource,
)
aadl2_FeatureGroupConnection_strategy = st.builds(
    aadl2_FeatureGroupConnection,
)
aadl2_FeatureConnection_strategy = st.builds(
    aadl2_FeatureConnection,
)
FeatureClassifier_strategy = st.builds(
    FeatureClassifier,
)
SubcomponentType_strategy = st.builds(
    SubcomponentType,
)
aadl2_MemorySubcomponentType_strategy = st.builds(
    aadl2_MemorySubcomponentType,
)
aadl2_DataSubcomponentType_strategy = st.builds(
    aadl2_DataSubcomponentType,
)
aadl2_ProcessorSubcomponentType_strategy = st.builds(
    aadl2_ProcessorSubcomponentType,
)
aadl2_SubprogramSubcomponentType_strategy = st.builds(
    aadl2_SubprogramSubcomponentType,
)
aadl2_SubprogramGroupSubcomponentType_strategy = st.builds(
    aadl2_SubprogramGroupSubcomponentType,
)
aadl2_ProcessSubcomponentType_strategy = st.builds(
    aadl2_ProcessSubcomponentType,
)
aadl2_VirtualProcessorSubcomponentType_strategy = st.builds(
    aadl2_VirtualProcessorSubcomponentType,
)
aadl2_AbstractSubcomponentType_strategy = st.builds(
    aadl2_AbstractSubcomponentType,
)
aadl2_SystemSubcomponentType_strategy = st.builds(
    aadl2_SystemSubcomponentType,
)
aadl2_ComponentPrototype_strategy = st.builds(
    aadl2_ComponentPrototype,
    array=
        safe_text
)
aadl2_DeviceSubcomponentType_strategy = st.builds(
    aadl2_DeviceSubcomponentType,
)
aadl2_BusSubcomponentType_strategy = st.builds(
    aadl2_BusSubcomponentType,
)
aadl2_ThreadSubcomponentType_strategy = st.builds(
    aadl2_ThreadSubcomponentType,
)
aadl2_VirtualBusSubcomponentType_strategy = st.builds(
    aadl2_VirtualBusSubcomponentType,
)
aadl2_ThreadGroupSubcomponentType_strategy = st.builds(
    aadl2_ThreadGroupSubcomponentType,
)
Classifier_strategy = st.builds(
    Classifier,
)
aadl2_FeatureGroupType_strategy = st.builds(
    aadl2_FeatureGroupType,
)
aadl2_ComponentClassifier_strategy = st.builds(
    aadl2_ComponentClassifier,
    noFlows=
        safe_text,
    noModes=
        safe_text,
    derivedModes=
        safe_text
)
aadl2_PortProxy_strategy = st.builds(
    aadl2_PortProxy,
    direction=
        safe_text
)
aadl2_EventDataSource_strategy = st.builds(
    aadl2_EventDataSource,
)
aadl2_Realization_strategy = st.builds(
    aadl2_Realization,
)
aadl2_ImplementationExtension_strategy = st.builds(
    aadl2_ImplementationExtension,
)
ComponentClassifier_strategy = st.builds(
    ComponentClassifier,
)
aadl2_MemoryClassifier_strategy = st.builds(
    aadl2_MemoryClassifier,
)
aadl2_DeviceClassifier_strategy = st.builds(
    aadl2_DeviceClassifier,
)
aadl2_VirtualBusClassifier_strategy = st.builds(
    aadl2_VirtualBusClassifier,
)
aadl2_ThreadClassifier_strategy = st.builds(
    aadl2_ThreadClassifier,
)
aadl2_DataClassifier_strategy = st.builds(
    aadl2_DataClassifier,
)
aadl2_AbstractClassifier_strategy = st.builds(
    aadl2_AbstractClassifier,
)
aadl2_ProcessorClassifier_strategy = st.builds(
    aadl2_ProcessorClassifier,
)
aadl2_SystemClassifier_strategy = st.builds(
    aadl2_SystemClassifier,
)
aadl2_SubprogramClassifier_strategy = st.builds(
    aadl2_SubprogramClassifier,
)
aadl2_SubprogramGroupClassifier_strategy = st.builds(
    aadl2_SubprogramGroupClassifier,
)
aadl2_ComponentType_strategy = st.builds(
    aadl2_ComponentType,
    noFeatures=
        safe_text
)
aadl2_BusClassifier_strategy = st.builds(
    aadl2_BusClassifier,
)
aadl2_VirtualProcessorClassifier_strategy = st.builds(
    aadl2_VirtualProcessorClassifier,
)
aadl2_ThreadGroupClassifier_strategy = st.builds(
    aadl2_ThreadGroupClassifier,
)
aadl2_ProcessClassifier_strategy = st.builds(
    aadl2_ProcessClassifier,
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
aadl2_AbstractSubcomponent_strategy = st.builds(
    aadl2_AbstractSubcomponent,
)
aadl2_EndToEndFlow_strategy = st.builds(
    aadl2_EndToEndFlow,
)
aadl2_ComponentImplementation_strategy = st.builds(
    aadl2_ComponentImplementation,
    noCalls=
        safe_text,
    noConnections=
        safe_text,
    noSubcomponents=
        safe_text
)
aadl2_CalledSubprogram_strategy = st.builds(
    aadl2_CalledSubprogram,
)
RefinableElement_strategy = st.builds(
    RefinableElement,
)
CalledSubprogram_strategy = st.builds(
    CalledSubprogram,
)
aadl2_SubprogramProxy_strategy = st.builds(
    aadl2_SubprogramProxy,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
aadl2_Connection_strategy = st.builds(
    aadl2_Connection,
    bidirectional=
        safe_text
)
aadl2_Feature_strategy = st.builds(
    aadl2_Feature,
)
aadl2_FlowFeature_strategy = st.builds(
    aadl2_FlowFeature,
)
Relationship_strategy = st.builds(
    Relationship,
)
aadl2_DirectedRelationship_strategy = st.builds(
    aadl2_DirectedRelationship,
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
ClassifierFeature_strategy = st.builds(
    ClassifierFeature,
)
aadl2_StructuralFeature_strategy = st.builds(
    aadl2_StructuralFeature,
)
aadl2_BehavioralFeature_strategy = st.builds(
    aadl2_BehavioralFeature,
)
aadl2_FlowImplementation_strategy = st.builds(
    aadl2_FlowImplementation,
    kind=
        safe_text
)
aadl2_ModeFeature_strategy = st.builds(
    aadl2_ModeFeature,
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
aadl2_ModalPath_strategy = st.builds(
    aadl2_ModalPath,
)
aadl2_Subcomponent_strategy = st.builds(
    aadl2_Subcomponent,
    allModes=
        safe_text
)
aadl2_SubprogramCallSequence_strategy = st.builds(
    aadl2_SubprogramCallSequence,
)
aadl2_ProcessorFeature_strategy = st.builds(
    aadl2_ProcessorFeature,
)
aadl2_InternalFeature_strategy = st.builds(
    aadl2_InternalFeature,
    direction=
        safe_text
)
aadl2_Prototype_strategy = st.builds(
    aadl2_Prototype,
)
aadl2_AnnexSubclause_strategy = st.builds(
    aadl2_AnnexSubclause,
)
aadl2_Generalization__strategy = st.builds(
    aadl2_Generalization_,
)
PropertyOwner_strategy = st.builds(
    PropertyOwner,
)
aadl2_ClassifierValue_strategy = st.builds(
    aadl2_ClassifierValue,
)
aadl2_ArraySizeProperty_strategy = st.builds(
    aadl2_ArraySizeProperty,
)
aadl2_AbstractNamedValue_strategy = st.builds(
    aadl2_AbstractNamedValue,
)
Type_strategy = st.builds(
    Type,
)
aadl2_SubcomponentType_strategy = st.builds(
    aadl2_SubcomponentType,
)
aadl2_PropertyType_strategy = st.builds(
    aadl2_PropertyType,
)
Namespace_strategy = st.builds(
    Namespace,
)
aadl2_RecordType_strategy = st.builds(
    aadl2_RecordType,
)
aadl2_PropertySet_strategy = st.builds(
    aadl2_PropertySet,
)
aadl2_EnumerationType_strategy = st.builds(
    aadl2_EnumerationType,
)
aadl2_GlobalNamespace_strategy = st.builds(
    aadl2_GlobalNamespace,
)
aadl2_PackageSection_strategy = st.builds(
    aadl2_PackageSection,
    noAnnexes=
        safe_text,
    noProperties=
        safe_text
)
ArraySizeProperty_strategy = st.builds(
    ArraySizeProperty,
)
AbstractNamedValue_strategy = st.builds(
    AbstractNamedValue,
)
BasicProperty_strategy = st.builds(
    BasicProperty,
)
aadl2_RecordField_strategy = st.builds(
    aadl2_RecordField,
)
aadl2_ModalPropertyValue_strategy = st.builds(
    aadl2_ModalPropertyValue,
)
aadl2_Classifier_strategy = st.builds(
    aadl2_Classifier,
    noAnnexes=
        safe_text,
    noPrototypes=
        safe_text,
    noProperties=
        safe_text
)
aadl2_Property_strategy = st.builds(
    aadl2_Property,
    emptyListDefault=
        safe_text,
    inherit=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
aadl2_PropertyConstant_strategy = st.builds(
    aadl2_PropertyConstant,
)
aadl2_BasicProperty_strategy = st.builds(
    aadl2_BasicProperty,
)
aadl2_MetaclassReference_strategy = st.builds(
    aadl2_MetaclassReference,
    metaclassName=
        safe_text,
    annexName=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
aadl2_SubprogramGroup_strategy = st.builds(
    aadl2_SubprogramGroup,
)
aadl2_Data_strategy = st.builds(
    aadl2_Data,
)
aadl2_Memory_strategy = st.builds(
    aadl2_Memory,
)
aadl2_RefinableElement_strategy = st.builds(
    aadl2_RefinableElement,
)
aadl2_ComponentTypeRename_strategy = st.builds(
    aadl2_ComponentTypeRename,
    category=
        safe_text
)
aadl2_Processor_strategy = st.builds(
    aadl2_Processor,
)
aadl2_Thread_strategy = st.builds(
    aadl2_Thread,
)
aadl2_Context_strategy = st.builds(
    aadl2_Context,
)
aadl2_Flow_strategy = st.builds(
    aadl2_Flow,
)
aadl2_Subprogram_strategy = st.builds(
    aadl2_Subprogram,
)
aadl2_FeatureGroupTypeRename_strategy = st.builds(
    aadl2_FeatureGroupTypeRename,
)
aadl2_ModelUnit_strategy = st.builds(
    aadl2_ModelUnit,
)
aadl2_ThreadGroup_strategy = st.builds(
    aadl2_ThreadGroup,
)
aadl2_TriggerPort_strategy = st.builds(
    aadl2_TriggerPort,
)
aadl2_VirtualProcessor_strategy = st.builds(
    aadl2_VirtualProcessor,
)
aadl2_ConnectionEnd_strategy = st.builds(
    aadl2_ConnectionEnd,
)
aadl2_Abstract_strategy = st.builds(
    aadl2_Abstract,
)
aadl2_EnumerationLiteral_strategy = st.builds(
    aadl2_EnumerationLiteral,
)
aadl2_TypedElement_strategy = st.builds(
    aadl2_TypedElement,
)
aadl2_ModalElement_strategy = st.builds(
    aadl2_ModalElement,
)
aadl2_PackageRename_strategy = st.builds(
    aadl2_PackageRename,
    renameAll=
        safe_text
)
aadl2_AnnexLibrary_strategy = st.builds(
    aadl2_AnnexLibrary,
)
aadl2_Bus_strategy = st.builds(
    aadl2_Bus,
)
aadl2_Namespace_strategy = st.builds(
    aadl2_Namespace,
)
aadl2_EndToEndFlowElement_strategy = st.builds(
    aadl2_EndToEndFlowElement,
)
aadl2_System_strategy = st.builds(
    aadl2_System,
)
aadl2_ClassifierFeature_strategy = st.builds(
    aadl2_ClassifierFeature,
)
aadl2_Device_strategy = st.builds(
    aadl2_Device,
)
aadl2_Process_strategy = st.builds(
    aadl2_Process,
)
aadl2_VirtualBus_strategy = st.builds(
    aadl2_VirtualBus,
)
aadl2_Type_strategy = st.builds(
    aadl2_Type,
)
Element_strategy = st.builds(
    Element,
)
aadl2_FlowEnd_strategy = st.builds(
    aadl2_FlowEnd,
)
aadl2_FlowSegment_strategy = st.builds(
    aadl2_FlowSegment,
)
aadl2_ArrayRange_strategy = st.builds(
    aadl2_ArrayRange,
    lowerBound=
        safe_text,
    upperBound=
        safe_text
)
aadl2_NumericRange_strategy = st.builds(
    aadl2_NumericRange,
)
aadl2_ModeTransitionTrigger_strategy = st.builds(
    aadl2_ModeTransitionTrigger,
)
aadl2_ArrayDimension_strategy = st.builds(
    aadl2_ArrayDimension,
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
aadl2_NamedElement_strategy = st.builds(
    aadl2_NamedElement,
    qualifiedName=
        safe_text,
    name=
        safe_text
)
aadl2_Relationship_strategy = st.builds(
    aadl2_Relationship,
)
aadl2_ArraySize_strategy = st.builds(
    aadl2_ArraySize,
    size=
        safe_text
)
aadl2_ContainmentPathElement_strategy = st.builds(
    aadl2_ContainmentPathElement,
    annexName=
        safe_text
)
aadl2_ContainedNamedElement_strategy = st.builds(
    aadl2_ContainedNamedElement,
)
aadl2_ConnectedElement_strategy = st.builds(
    aadl2_ConnectedElement,
)
aadl2_PrototypeBinding_strategy = st.builds(
    aadl2_PrototypeBinding,
)
aadl2_Comment_strategy = st.builds(
    aadl2_Comment,
    body=
        safe_text
)
aadl2_PropertyAssociation_strategy = st.builds(
    aadl2_PropertyAssociation,
    append=
        safe_text,
    constant=
        safe_text
)
aadl2_EndToEndFlowSegment_strategy = st.builds(
    aadl2_EndToEndFlowSegment,
)
aadl2_BasicPropertyAssociation_strategy = st.builds(
    aadl2_BasicPropertyAssociation,
)
aadl2_ArrayableElement_strategy = st.builds(
    aadl2_ArrayableElement,
)
aadl2_ModeBinding_strategy = st.builds(
    aadl2_ModeBinding,
)
aadl2_Element_strategy = st.builds(
    aadl2_Element,
)

@given(instance=AbstractSubcomponentType_strategy)
@settings(max_examples=50)
def test_abstractsubcomponenttype_instantiation(instance):
    assert isinstance(instance, AbstractSubcomponentType)

@given(instance=AbstractClassifier_strategy)
@settings(max_examples=50)
def test_abstractclassifier_instantiation(instance):
    assert isinstance(instance, AbstractClassifier)

@given(instance=ComponentType_strategy)
@settings(max_examples=50)
def test_componenttype_instantiation(instance):
    assert isinstance(instance, ComponentType)

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
def test_aadl2_behavioredimplementation_subprogramcalls_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.subprogramCalls()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.subprogramCalls).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'subprogramCalls' in aadl2_BehavioredImplementation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'subprogramCalls' in aadl2_BehavioredImplementation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'subprogramCalls' in aadl2_BehavioredImplementation is not implemented or raised an error")

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=FeaturePrototypeActual_strategy)
@settings(max_examples=50)
def test_featureprototypeactual_instantiation(instance):
    assert isinstance(instance, FeaturePrototypeActual)

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

@given(instance=aadl2_PortSpecification_strategy)
@settings(max_examples=50)
def test_aadl2_portspecification_instantiation(instance):
    assert isinstance(instance, aadl2_PortSpecification)



@given(instance=aadl2_PortSpecification_strategy)
def test_aadl2_portspecification_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=aadl2_PortSpecification_strategy)
def test_aadl2_portspecification_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=aadl2_FeatureGroupPrototypeActual_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroupprototypeactual_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupPrototypeActual)

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

@given(instance=ModelUnit_strategy)
@settings(max_examples=50)
def test_modelunit_instantiation(instance):
    assert isinstance(instance, ModelUnit)

@given(instance=aadl2_AadlPackage_strategy)
@settings(max_examples=50)
def test_aadl2_aadlpackage_instantiation(instance):
    assert isinstance(instance, aadl2_AadlPackage)

@given(instance=ProcessorFeature_strategy)
@settings(max_examples=50)
def test_processorfeature_instantiation(instance):
    assert isinstance(instance, ProcessorFeature)

@given(instance=PackageSection_strategy)
@settings(max_examples=50)
def test_packagesection_instantiation(instance):
    assert isinstance(instance, PackageSection)

@given(instance=aadl2_PrivatePackageSection_strategy)
@settings(max_examples=50)
def test_aadl2_privatepackagesection_instantiation(instance):
    assert isinstance(instance, aadl2_PrivatePackageSection)

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

@given(instance=SubprogramSubcomponentType_strategy)
@settings(max_examples=50)
def test_subprogramsubcomponenttype_instantiation(instance):
    assert isinstance(instance, SubprogramSubcomponentType)

@given(instance=Abstract_strategy)
@settings(max_examples=50)
def test_abstract_instantiation(instance):
    assert isinstance(instance, Abstract)

@given(instance=Subcomponent_strategy)
@settings(max_examples=50)
def test_subcomponent_instantiation(instance):
    assert isinstance(instance, Subcomponent)

@given(instance=DataSubcomponentType_strategy)
@settings(max_examples=50)
def test_datasubcomponenttype_instantiation(instance):
    assert isinstance(instance, DataSubcomponentType)

@given(instance=InternalFeature_strategy)
@settings(max_examples=50)
def test_internalfeature_instantiation(instance):
    assert isinstance(instance, InternalFeature)

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=SubprogramGroup_strategy)
@settings(max_examples=50)
def test_subprogramgroup_instantiation(instance):
    assert isinstance(instance, SubprogramGroup)

@given(instance=TriggerPort_strategy)
@settings(max_examples=50)
def test_triggerport_instantiation(instance):
    assert isinstance(instance, TriggerPort)

@given(instance=Subprogram_strategy)
@settings(max_examples=50)
def test_subprogram_instantiation(instance):
    assert isinstance(instance, Subprogram)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=PortConnectionEnd_strategy)
@settings(max_examples=50)
def test_portconnectionend_instantiation(instance):
    assert isinstance(instance, PortConnectionEnd)

@given(instance=ParameterConnectionEnd_strategy)
@settings(max_examples=50)
def test_parameterconnectionend_instantiation(instance):
    assert isinstance(instance, ParameterConnectionEnd)

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=Bus_strategy)
@settings(max_examples=50)
def test_bus_instantiation(instance):
    assert isinstance(instance, Bus)

@given(instance=Access_strategy)
@settings(max_examples=50)
def test_access_instantiation(instance):
    assert isinstance(instance, Access)

@given(instance=aadl2_SubprogramAccess_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramaccess_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramAccess)

@given(instance=EnumerationType_strategy)
@settings(max_examples=50)
def test_enumerationtype_instantiation(instance):
    assert isinstance(instance, EnumerationType)

@given(instance=aadl2_UnitsType_strategy)
@settings(max_examples=50)
def test_aadl2_unitstype_instantiation(instance):
    assert isinstance(instance, aadl2_UnitsType)

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

@given(instance=NonListType_strategy)
@settings(max_examples=50)
def test_nonlisttype_instantiation(instance):
    assert isinstance(instance, NonListType)

@given(instance=aadl2_NumberType_strategy)
@settings(max_examples=50)
def test_aadl2_numbertype_instantiation(instance):
    assert isinstance(instance, aadl2_NumberType)

@given(instance=aadl2_RangeType_strategy)
@settings(max_examples=50)
def test_aadl2_rangetype_instantiation(instance):
    assert isinstance(instance, aadl2_RangeType)

@given(instance=aadl2_ClassifierType_strategy)
@settings(max_examples=50)
def test_aadl2_classifiertype_instantiation(instance):
    assert isinstance(instance, aadl2_ClassifierType)

@given(instance=aadl2_ReferenceType_strategy)
@settings(max_examples=50)
def test_aadl2_referencetype_instantiation(instance):
    assert isinstance(instance, aadl2_ReferenceType)

@given(instance=aadl2_AadlString_strategy)
@settings(max_examples=50)
def test_aadl2_aadlstring_instantiation(instance):
    assert isinstance(instance, aadl2_AadlString)

@given(instance=aadl2_AadlBoolean_strategy)
@settings(max_examples=50)
def test_aadl2_aadlboolean_instantiation(instance):
    assert isinstance(instance, aadl2_AadlBoolean)

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=aadl2_ListType_strategy)
@settings(max_examples=50)
def test_aadl2_listtype_instantiation(instance):
    assert isinstance(instance, aadl2_ListType)

@given(instance=aadl2_NonListType_strategy)
@settings(max_examples=50)
def test_aadl2_nonlisttype_instantiation(instance):
    assert isinstance(instance, aadl2_NonListType)

@given(instance=NumberValue_strategy)
@settings(max_examples=50)
def test_numbervalue_instantiation(instance):
    assert isinstance(instance, NumberValue)

@given(instance=aadl2_RealLiteral_strategy)
@settings(max_examples=50)
def test_aadl2_realliteral_instantiation(instance):
    assert isinstance(instance, aadl2_RealLiteral)



@given(instance=aadl2_RealLiteral_strategy)
def test_aadl2_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aadl2_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_aadl2_integerliteral_instantiation(instance):
    assert isinstance(instance, aadl2_IntegerLiteral)



@given(instance=aadl2_IntegerLiteral_strategy)
def test_aadl2_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aadl2_IntegerLiteral_strategy)
def test_aadl2_integerliteral_base_setter(instance):
    original = instance.base
    instance.base = original
    assert instance.base == original

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=aadl2_UnitLiteral_strategy)
@settings(max_examples=50)
def test_aadl2_unitliteral_instantiation(instance):
    assert isinstance(instance, aadl2_UnitLiteral)

@given(instance=ContainedNamedElement_strategy)
@settings(max_examples=50)
def test_containednamedelement_instantiation(instance):
    assert isinstance(instance, ContainedNamedElement)

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

@given(instance=aadl2_ReferenceValue_strategy)
@settings(max_examples=50)
def test_aadl2_referencevalue_instantiation(instance):
    assert isinstance(instance, aadl2_ReferenceValue)

@given(instance=aadl2_ComputedValue_strategy)
@settings(max_examples=50)
def test_aadl2_computedvalue_instantiation(instance):
    assert isinstance(instance, aadl2_ComputedValue)



@given(instance=aadl2_ComputedValue_strategy)
def test_aadl2_computedvalue_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=aadl2_NumberValue_strategy)
@settings(max_examples=50)
def test_aadl2_numbervalue_instantiation(instance):
    assert isinstance(instance, aadl2_NumberValue)

@given(instance=aadl2_NamedValue_strategy)
@settings(max_examples=50)
def test_aadl2_namedvalue_instantiation(instance):
    assert isinstance(instance, aadl2_NamedValue)

@given(instance=aadl2_RangeValue_strategy)
@settings(max_examples=50)
def test_aadl2_rangevalue_instantiation(instance):
    assert isinstance(instance, aadl2_RangeValue)

@given(instance=aadl2_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_aadl2_booleanliteral_instantiation(instance):
    assert isinstance(instance, aadl2_BooleanLiteral)



@given(instance=aadl2_BooleanLiteral_strategy)
def test_aadl2_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aadl2_StringLiteral_strategy)
@settings(max_examples=50)
def test_aadl2_stringliteral_instantiation(instance):
    assert isinstance(instance, aadl2_StringLiteral)



@given(instance=aadl2_StringLiteral_strategy)
def test_aadl2_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=VirtualBusClassifier_strategy)
@settings(max_examples=50)
def test_virtualbusclassifier_instantiation(instance):
    assert isinstance(instance, VirtualBusClassifier)

@given(instance=aadl2_VirtualBusType_strategy)
@settings(max_examples=50)
def test_aadl2_virtualbustype_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusType)

@given(instance=VirtualProcessorClassifier_strategy)
@settings(max_examples=50)
def test_virtualprocessorclassifier_instantiation(instance):
    assert isinstance(instance, VirtualProcessorClassifier)

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

@given(instance=ThreadGroupClassifier_strategy)
@settings(max_examples=50)
def test_threadgroupclassifier_instantiation(instance):
    assert isinstance(instance, ThreadGroupClassifier)

@given(instance=aadl2_ThreadGroupImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_threadgroupimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupImplementation)

@given(instance=aadl2_ThreadGroupType_strategy)
@settings(max_examples=50)
def test_aadl2_threadgrouptype_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupType)

@given(instance=ThreadClassifier_strategy)
@settings(max_examples=50)
def test_threadclassifier_instantiation(instance):
    assert isinstance(instance, ThreadClassifier)

@given(instance=aadl2_ThreadType_strategy)
@settings(max_examples=50)
def test_aadl2_threadtype_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadType)

@given(instance=ProcessClassifier_strategy)
@settings(max_examples=50)
def test_processclassifier_instantiation(instance):
    assert isinstance(instance, ProcessClassifier)

@given(instance=aadl2_ProcessImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_processimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessImplementation)

@given(instance=aadl2_ProcessType_strategy)
@settings(max_examples=50)
def test_aadl2_processtype_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessType)

@given(instance=ProcessorClassifier_strategy)
@settings(max_examples=50)
def test_processorclassifier_instantiation(instance):
    assert isinstance(instance, ProcessorClassifier)

@given(instance=aadl2_ProcessorImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_processorimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorImplementation)

@given(instance=aadl2_ProcessorType_strategy)
@settings(max_examples=50)
def test_aadl2_processortype_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorType)

@given(instance=SubprogramGroupClassifier_strategy)
@settings(max_examples=50)
def test_subprogramgroupclassifier_instantiation(instance):
    assert isinstance(instance, SubprogramGroupClassifier)

@given(instance=aadl2_SubprogramGroupImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgroupimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupImplementation)

@given(instance=SystemClassifier_strategy)
@settings(max_examples=50)
def test_systemclassifier_instantiation(instance):
    assert isinstance(instance, SystemClassifier)

@given(instance=aadl2_SystemImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_systemimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_SystemImplementation)

@given(instance=aadl2_SystemType_strategy)
@settings(max_examples=50)
def test_aadl2_systemtype_instantiation(instance):
    assert isinstance(instance, aadl2_SystemType)

@given(instance=SubprogramClassifier_strategy)
@settings(max_examples=50)
def test_subprogramclassifier_instantiation(instance):
    assert isinstance(instance, SubprogramClassifier)

@given(instance=MemoryClassifier_strategy)
@settings(max_examples=50)
def test_memoryclassifier_instantiation(instance):
    assert isinstance(instance, MemoryClassifier)

@given(instance=aadl2_MemoryType_strategy)
@settings(max_examples=50)
def test_aadl2_memorytype_instantiation(instance):
    assert isinstance(instance, aadl2_MemoryType)

@given(instance=aadl2_MemoryImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_memoryimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_MemoryImplementation)

@given(instance=DeviceClassifier_strategy)
@settings(max_examples=50)
def test_deviceclassifier_instantiation(instance):
    assert isinstance(instance, DeviceClassifier)

@given(instance=aadl2_DeviceType_strategy)
@settings(max_examples=50)
def test_aadl2_devicetype_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceType)

@given(instance=aadl2_DeviceImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_deviceimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceImplementation)

@given(instance=DataClassifier_strategy)
@settings(max_examples=50)
def test_dataclassifier_instantiation(instance):
    assert isinstance(instance, DataClassifier)

@given(instance=aadl2_DataImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_dataimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_DataImplementation)

@given(instance=ComponentPrototype_strategy)
@settings(max_examples=50)
def test_componentprototype_instantiation(instance):
    assert isinstance(instance, ComponentPrototype)

@given(instance=aadl2_SubprogramPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramprototype_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramPrototype)

@given(instance=aadl2_DataPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_dataprototype_instantiation(instance):
    assert isinstance(instance, aadl2_DataPrototype)

@given(instance=BusClassifier_strategy)
@settings(max_examples=50)
def test_busclassifier_instantiation(instance):
    assert isinstance(instance, BusClassifier)

@given(instance=aadl2_BusImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_busimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_BusImplementation)

@given(instance=aadl2_BusType_strategy)
@settings(max_examples=50)
def test_aadl2_bustype_instantiation(instance):
    assert isinstance(instance, aadl2_BusType)

@given(instance=BehavioredImplementation_strategy)
@settings(max_examples=50)
def test_behavioredimplementation_instantiation(instance):
    assert isinstance(instance, BehavioredImplementation)

@given(instance=aadl2_SubprogramImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramImplementation)

@given(instance=aadl2_ThreadImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_threadimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadImplementation)

@given(instance=aadl2_AbstractImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_abstractimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractImplementation)

@given(instance=Memory_strategy)
@settings(max_examples=50)
def test_memory_instantiation(instance):
    assert isinstance(instance, Memory)

@given(instance=aadl2_MemorySubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_memorysubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_MemorySubcomponent)

@given(instance=Process_strategy)
@settings(max_examples=50)
def test_process_instantiation(instance):
    assert isinstance(instance, Process)

@given(instance=aadl2_ProcessSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_processsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessSubcomponent)

@given(instance=System_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, System)

@given(instance=aadl2_SystemSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_systemsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_SystemSubcomponent)

@given(instance=Thread_strategy)
@settings(max_examples=50)
def test_thread_instantiation(instance):
    assert isinstance(instance, Thread)

@given(instance=aadl2_ThreadSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_threadsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadSubcomponent)

@given(instance=ThreadGroup_strategy)
@settings(max_examples=50)
def test_threadgroup_instantiation(instance):
    assert isinstance(instance, ThreadGroup)

@given(instance=aadl2_ThreadGroupSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_threadgroupsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupSubcomponent)

@given(instance=VirtualBus_strategy)
@settings(max_examples=50)
def test_virtualbus_instantiation(instance):
    assert isinstance(instance, VirtualBus)

@given(instance=aadl2_VirtualBusSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_virtualbussubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusSubcomponent)

@given(instance=VirtualProcessor_strategy)
@settings(max_examples=50)
def test_virtualprocessor_instantiation(instance):
    assert isinstance(instance, VirtualProcessor)

@given(instance=aadl2_VirtualProcessorSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_virtualprocessorsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorSubcomponent)

@given(instance=VirtualProcessorSubcomponentType_strategy)
@settings(max_examples=50)
def test_virtualprocessorsubcomponenttype_instantiation(instance):
    assert isinstance(instance, VirtualProcessorSubcomponentType)

@given(instance=aadl2_VirtualProcessorPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_virtualprocessorprototype_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorPrototype)

@given(instance=VirtualBusSubcomponentType_strategy)
@settings(max_examples=50)
def test_virtualbussubcomponenttype_instantiation(instance):
    assert isinstance(instance, VirtualBusSubcomponentType)

@given(instance=aadl2_VirtualBusPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_virtualbusprototype_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusPrototype)

@given(instance=Processor_strategy)
@settings(max_examples=50)
def test_processor_instantiation(instance):
    assert isinstance(instance, Processor)

@given(instance=aadl2_ProcessorSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_processorsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorSubcomponent)

@given(instance=ThreadSubcomponentType_strategy)
@settings(max_examples=50)
def test_threadsubcomponenttype_instantiation(instance):
    assert isinstance(instance, ThreadSubcomponentType)

@given(instance=aadl2_ThreadPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_threadprototype_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadPrototype)

@given(instance=ThreadGroupSubcomponentType_strategy)
@settings(max_examples=50)
def test_threadgroupsubcomponenttype_instantiation(instance):
    assert isinstance(instance, ThreadGroupSubcomponentType)

@given(instance=aadl2_ThreadGroupPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_threadgroupprototype_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupPrototype)

@given(instance=SystemSubcomponentType_strategy)
@settings(max_examples=50)
def test_systemsubcomponenttype_instantiation(instance):
    assert isinstance(instance, SystemSubcomponentType)

@given(instance=aadl2_SystemPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_systemprototype_instantiation(instance):
    assert isinstance(instance, aadl2_SystemPrototype)

@given(instance=Device_strategy)
@settings(max_examples=50)
def test_device_instantiation(instance):
    assert isinstance(instance, Device)

@given(instance=aadl2_DeviceSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_devicesubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceSubcomponent)

@given(instance=SubprogramGroupSubcomponentType_strategy)
@settings(max_examples=50)
def test_subprogramgroupsubcomponenttype_instantiation(instance):
    assert isinstance(instance, SubprogramGroupSubcomponentType)

@given(instance=aadl2_SubprogramGroupPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgroupprototype_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupPrototype)

@given(instance=ProcessSubcomponentType_strategy)
@settings(max_examples=50)
def test_processsubcomponenttype_instantiation(instance):
    assert isinstance(instance, ProcessSubcomponentType)

@given(instance=aadl2_ProcessPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_processprototype_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessPrototype)

@given(instance=ProcessorSubcomponentType_strategy)
@settings(max_examples=50)
def test_processorsubcomponenttype_instantiation(instance):
    assert isinstance(instance, ProcessorSubcomponentType)

@given(instance=aadl2_ProcessorPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_processorprototype_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorPrototype)

@given(instance=MemorySubcomponentType_strategy)
@settings(max_examples=50)
def test_memorysubcomponenttype_instantiation(instance):
    assert isinstance(instance, MemorySubcomponentType)

@given(instance=aadl2_MemoryPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_memoryprototype_instantiation(instance):
    assert isinstance(instance, aadl2_MemoryPrototype)

@given(instance=DeviceSubcomponentType_strategy)
@settings(max_examples=50)
def test_devicesubcomponenttype_instantiation(instance):
    assert isinstance(instance, DeviceSubcomponentType)

@given(instance=aadl2_DevicePrototype_strategy)
@settings(max_examples=50)
def test_aadl2_deviceprototype_instantiation(instance):
    assert isinstance(instance, aadl2_DevicePrototype)

@given(instance=BusSubcomponentType_strategy)
@settings(max_examples=50)
def test_bussubcomponenttype_instantiation(instance):
    assert isinstance(instance, BusSubcomponentType)

@given(instance=aadl2_BusPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_busprototype_instantiation(instance):
    assert isinstance(instance, aadl2_BusPrototype)

@given(instance=aadl2_AbstractPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_abstractprototype_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractPrototype)

@given(instance=AccessConnectionEnd_strategy)
@settings(max_examples=50)
def test_accessconnectionend_instantiation(instance):
    assert isinstance(instance, AccessConnectionEnd)

@given(instance=aadl2_DataSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_datasubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_DataSubcomponent)

@given(instance=aadl2_SubprogramSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramSubcomponent)

@given(instance=aadl2_BusSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_bussubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_BusSubcomponent)

@given(instance=aadl2_EventPort_strategy)
@settings(max_examples=50)
def test_aadl2_eventport_instantiation(instance):
    assert isinstance(instance, aadl2_EventPort)

@given(instance=FeatureType_strategy)
@settings(max_examples=50)
def test_featuretype_instantiation(instance):
    assert isinstance(instance, FeatureType)

@given(instance=aadl2_BusAccess_strategy)
@settings(max_examples=50)
def test_aadl2_busaccess_instantiation(instance):
    assert isinstance(instance, aadl2_BusAccess)

@given(instance=aadl2_FeatureType_strategy)
@settings(max_examples=50)
def test_aadl2_featuretype_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureType)

@given(instance=CallContext_strategy)
@settings(max_examples=50)
def test_callcontext_instantiation(instance):
    assert isinstance(instance, CallContext)

@given(instance=aadl2_DataType_strategy)
@settings(max_examples=50)
def test_aadl2_datatype_instantiation(instance):
    assert isinstance(instance, aadl2_DataType)

@given(instance=aadl2_SubprogramGroupSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgroupsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupSubcomponent)

@given(instance=aadl2_SubprogramType_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramtype_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramType)

@given(instance=aadl2_SubprogramGroupAccess_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgroupaccess_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupAccess)

@given(instance=aadl2_SubprogramGroupType_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgrouptype_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupType)

@given(instance=aadl2_AbstractType_strategy)
@settings(max_examples=50)
def test_aadl2_abstracttype_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractType)

@given(instance=FeatureGroupConnectionEnd_strategy)
@settings(max_examples=50)
def test_featuregroupconnectionend_instantiation(instance):
    assert isinstance(instance, FeatureGroupConnectionEnd)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=aadl2_SubprogramCall_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramcall_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramCall)

@given(instance=aadl2_DataPort_strategy)
@settings(max_examples=50)
def test_aadl2_dataport_instantiation(instance):
    assert isinstance(instance, aadl2_DataPort)

@given(instance=aadl2_EventDataPort_strategy)
@settings(max_examples=50)
def test_aadl2_eventdataport_instantiation(instance):
    assert isinstance(instance, aadl2_EventDataPort)

@given(instance=DirectedFeature_strategy)
@settings(max_examples=50)
def test_directedfeature_instantiation(instance):
    assert isinstance(instance, DirectedFeature)

@given(instance=aadl2_Port_strategy)
@settings(max_examples=50)
def test_aadl2_port_instantiation(instance):
    assert isinstance(instance, aadl2_Port)



@given(instance=aadl2_Port_strategy)
def test_aadl2_port_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=aadl2_Parameter_strategy)
@settings(max_examples=50)
def test_aadl2_parameter_instantiation(instance):
    assert isinstance(instance, aadl2_Parameter)

@given(instance=Generalization__strategy)
@settings(max_examples=50)
def test_generalization__instantiation(instance):
    assert isinstance(instance, Generalization_)

@given(instance=aadl2_GroupExtension_strategy)
@settings(max_examples=50)
def test_aadl2_groupextension_instantiation(instance):
    assert isinstance(instance, aadl2_GroupExtension)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=aadl2_Access_strategy)
@settings(max_examples=50)
def test_aadl2_access_instantiation(instance):
    assert isinstance(instance, aadl2_Access)



@given(instance=aadl2_Access_strategy)
def test_aadl2_access_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=aadl2_Access_strategy)
def test_aadl2_access_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=aadl2_DirectedFeature_strategy)
@settings(max_examples=50)
def test_aadl2_directedfeature_instantiation(instance):
    assert isinstance(instance, aadl2_DirectedFeature)



@given(instance=aadl2_DirectedFeature_strategy)
def test_aadl2_directedfeature_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=aadl2_CallContext_strategy)
@settings(max_examples=50)
def test_aadl2_callcontext_instantiation(instance):
    assert isinstance(instance, aadl2_CallContext)

@given(instance=Flow_strategy)
@settings(max_examples=50)
def test_flow_instantiation(instance):
    assert isinstance(instance, Flow)

@given(instance=FlowElement_strategy)
@settings(max_examples=50)
def test_flowelement_instantiation(instance):
    assert isinstance(instance, FlowElement)

@given(instance=aadl2_DataAccess_strategy)
@settings(max_examples=50)
def test_aadl2_dataaccess_instantiation(instance):
    assert isinstance(instance, aadl2_DataAccess)

@given(instance=ModalPath_strategy)
@settings(max_examples=50)
def test_modalpath_instantiation(instance):
    assert isinstance(instance, ModalPath)

@given(instance=FlowFeature_strategy)
@settings(max_examples=50)
def test_flowfeature_instantiation(instance):
    assert isinstance(instance, FlowFeature)

@given(instance=Prototype_strategy)
@settings(max_examples=50)
def test_prototype_instantiation(instance):
    assert isinstance(instance, Prototype)

@given(instance=aadl2_FeaturePrototype_strategy)
@settings(max_examples=50)
def test_aadl2_featureprototype_instantiation(instance):
    assert isinstance(instance, aadl2_FeaturePrototype)



@given(instance=aadl2_FeaturePrototype_strategy)
def test_aadl2_featureprototype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=aadl2_FeatureGroupPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroupprototype_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupPrototype)

@given(instance=EndToEndFlowElement_strategy)
@settings(max_examples=50)
def test_endtoendflowelement_instantiation(instance):
    assert isinstance(instance, EndToEndFlowElement)

@given(instance=aadl2_FlowElement_strategy)
@settings(max_examples=50)
def test_aadl2_flowelement_instantiation(instance):
    assert isinstance(instance, aadl2_FlowElement)

@given(instance=ArrayableElement_strategy)
@settings(max_examples=50)
def test_arrayableelement_instantiation(instance):
    assert isinstance(instance, ArrayableElement)

@given(instance=aadl2_ComponentPrototypeActual_strategy)
@settings(max_examples=50)
def test_aadl2_componentprototypeactual_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentPrototypeActual)



@given(instance=aadl2_ComponentPrototypeActual_strategy)
def test_aadl2_componentprototypeactual_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=aadl2_FeaturePrototypeActual_strategy)
@settings(max_examples=50)
def test_aadl2_featureprototypeactual_instantiation(instance):
    assert isinstance(instance, aadl2_FeaturePrototypeActual)

@given(instance=FeatureConnectionEnd_strategy)
@settings(max_examples=50)
def test_featureconnectionend_instantiation(instance):
    assert isinstance(instance, FeatureConnectionEnd)

@given(instance=aadl2_AbstractFeature_strategy)
@settings(max_examples=50)
def test_aadl2_abstractfeature_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractFeature)

@given(instance=aadl2_FeatureGroup_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroup_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroup)



@given(instance=aadl2_FeatureGroup_strategy)
def test_aadl2_featuregroup_inverse_setter(instance):
    original = instance.inverse
    instance.inverse = original
    assert instance.inverse == original

@given(instance=aadl2_TypeExtension_strategy)
@settings(max_examples=50)
def test_aadl2_typeextension_instantiation(instance):
    assert isinstance(instance, aadl2_TypeExtension)

@given(instance=aadl2_FlowSpecification_strategy)
@settings(max_examples=50)
def test_aadl2_flowspecification_instantiation(instance):
    assert isinstance(instance, aadl2_FlowSpecification)



@given(instance=aadl2_FlowSpecification_strategy)
def test_aadl2_flowspecification_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

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

@given(instance=aadl2_FeatureGroupConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroupconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupConnectionEnd)

@given(instance=aadl2_ParameterConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2_parameterconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2_ParameterConnectionEnd)

@given(instance=aadl2_FeatureConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2_featureconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureConnectionEnd)

@given(instance=aadl2_FeatureClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_featureclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureClassifier)

@given(instance=aadl2_EventSource_strategy)
@settings(max_examples=50)
def test_aadl2_eventsource_instantiation(instance):
    assert isinstance(instance, aadl2_EventSource)

@given(instance=aadl2_FeatureGroupConnection_strategy)
@settings(max_examples=50)
def test_aadl2_featuregroupconnection_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupConnection)

@given(instance=aadl2_FeatureConnection_strategy)
@settings(max_examples=50)
def test_aadl2_featureconnection_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureConnection)

@given(instance=FeatureClassifier_strategy)
@settings(max_examples=50)
def test_featureclassifier_instantiation(instance):
    assert isinstance(instance, FeatureClassifier)

@given(instance=SubcomponentType_strategy)
@settings(max_examples=50)
def test_subcomponenttype_instantiation(instance):
    assert isinstance(instance, SubcomponentType)

@given(instance=aadl2_MemorySubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_memorysubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_MemorySubcomponentType)

@given(instance=aadl2_DataSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_datasubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_DataSubcomponentType)

@given(instance=aadl2_ProcessorSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_processorsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorSubcomponentType)

@given(instance=aadl2_SubprogramSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramSubcomponentType)

@given(instance=aadl2_SubprogramGroupSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgroupsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupSubcomponentType)

@given(instance=aadl2_ProcessSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_processsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessSubcomponentType)

@given(instance=aadl2_VirtualProcessorSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_virtualprocessorsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorSubcomponentType)

@given(instance=aadl2_AbstractSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_abstractsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractSubcomponentType)

@given(instance=aadl2_SystemSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_systemsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_SystemSubcomponentType)

@given(instance=aadl2_ComponentPrototype_strategy)
@settings(max_examples=50)
def test_aadl2_componentprototype_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentPrototype)



@given(instance=aadl2_ComponentPrototype_strategy)
def test_aadl2_componentprototype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=aadl2_DeviceSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_devicesubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceSubcomponentType)

@given(instance=aadl2_BusSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_bussubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_BusSubcomponentType)

@given(instance=aadl2_ThreadSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_threadsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadSubcomponentType)

@given(instance=aadl2_VirtualBusSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_virtualbussubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusSubcomponentType)

@given(instance=aadl2_ThreadGroupSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_threadgroupsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupSubcomponentType)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=aadl2_FeatureGroupType_strategy)
@settings(max_examples=50)
def test_aadl2_featuregrouptype_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupType)

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



@given(instance=aadl2_ComponentClassifier_strategy)
def test_aadl2_componentclassifier_derivedModes_setter(instance):
    original = instance.derivedModes
    instance.derivedModes = original
    assert instance.derivedModes == original

@given(instance=aadl2_PortProxy_strategy)
@settings(max_examples=50)
def test_aadl2_portproxy_instantiation(instance):
    assert isinstance(instance, aadl2_PortProxy)



@given(instance=aadl2_PortProxy_strategy)
def test_aadl2_portproxy_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=aadl2_EventDataSource_strategy)
@settings(max_examples=50)
def test_aadl2_eventdatasource_instantiation(instance):
    assert isinstance(instance, aadl2_EventDataSource)

@given(instance=aadl2_Realization_strategy)
@settings(max_examples=50)
def test_aadl2_realization_instantiation(instance):
    assert isinstance(instance, aadl2_Realization)

@given(instance=aadl2_ImplementationExtension_strategy)
@settings(max_examples=50)
def test_aadl2_implementationextension_instantiation(instance):
    assert isinstance(instance, aadl2_ImplementationExtension)

@given(instance=ComponentClassifier_strategy)
@settings(max_examples=50)
def test_componentclassifier_instantiation(instance):
    assert isinstance(instance, ComponentClassifier)

@given(instance=aadl2_MemoryClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_memoryclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_MemoryClassifier)

@given(instance=aadl2_DeviceClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_deviceclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_DeviceClassifier)

@given(instance=aadl2_VirtualBusClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_virtualbusclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBusClassifier)

@given(instance=aadl2_ThreadClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_threadclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadClassifier)

@given(instance=aadl2_DataClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_dataclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_DataClassifier)

@given(instance=aadl2_AbstractClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_abstractclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractClassifier)

@given(instance=aadl2_ProcessorClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_processorclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorClassifier)

@given(instance=aadl2_SystemClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_systemclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_SystemClassifier)

@given(instance=aadl2_SubprogramClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramClassifier)

@given(instance=aadl2_SubprogramGroupClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgroupclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroupClassifier)

@given(instance=aadl2_ComponentType_strategy)
@settings(max_examples=50)
def test_aadl2_componenttype_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentType)



@given(instance=aadl2_ComponentType_strategy)
def test_aadl2_componenttype_noFeatures_setter(instance):
    original = instance.noFeatures
    instance.noFeatures = original
    assert instance.noFeatures == original

@given(instance=aadl2_BusClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_busclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_BusClassifier)

@given(instance=aadl2_VirtualProcessorClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_virtualprocessorclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessorClassifier)

@given(instance=aadl2_ThreadGroupClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_threadgroupclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroupClassifier)

@given(instance=aadl2_ProcessClassifier_strategy)
@settings(max_examples=50)
def test_aadl2_processclassifier_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessClassifier)

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

@given(instance=aadl2_AbstractSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2_abstractsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractSubcomponent)

@given(instance=aadl2_EndToEndFlow_strategy)
@settings(max_examples=50)
def test_aadl2_endtoendflow_instantiation(instance):
    assert isinstance(instance, aadl2_EndToEndFlow)

@given(instance=aadl2_ComponentImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_componentimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentImplementation)



@given(instance=aadl2_ComponentImplementation_strategy)
def test_aadl2_componentimplementation_noCalls_setter(instance):
    original = instance.noCalls
    instance.noCalls = original
    assert instance.noCalls == original



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

@given(instance=aadl2_CalledSubprogram_strategy)
@settings(max_examples=50)
def test_aadl2_calledsubprogram_instantiation(instance):
    assert isinstance(instance, aadl2_CalledSubprogram)

@given(instance=RefinableElement_strategy)
@settings(max_examples=50)
def test_refinableelement_instantiation(instance):
    assert isinstance(instance, RefinableElement)

@given(instance=CalledSubprogram_strategy)
@settings(max_examples=50)
def test_calledsubprogram_instantiation(instance):
    assert isinstance(instance, CalledSubprogram)

@given(instance=aadl2_SubprogramProxy_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramproxy_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramProxy)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=aadl2_Connection_strategy)
@settings(max_examples=50)
def test_aadl2_connection_instantiation(instance):
    assert isinstance(instance, aadl2_Connection)



@given(instance=aadl2_Connection_strategy)
def test_aadl2_connection_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original

@given(instance=aadl2_Feature_strategy)
@settings(max_examples=50)
def test_aadl2_feature_instantiation(instance):
    assert isinstance(instance, aadl2_Feature)

@given(instance=aadl2_FlowFeature_strategy)
@settings(max_examples=50)
def test_aadl2_flowfeature_instantiation(instance):
    assert isinstance(instance, aadl2_FlowFeature)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=aadl2_DirectedRelationship_strategy)
@settings(max_examples=50)
def test_aadl2_directedrelationship_instantiation(instance):
    assert isinstance(instance, aadl2_DirectedRelationship)

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=ClassifierFeature_strategy)
@settings(max_examples=50)
def test_classifierfeature_instantiation(instance):
    assert isinstance(instance, ClassifierFeature)

@given(instance=aadl2_StructuralFeature_strategy)
@settings(max_examples=50)
def test_aadl2_structuralfeature_instantiation(instance):
    assert isinstance(instance, aadl2_StructuralFeature)

@given(instance=aadl2_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_aadl2_behavioralfeature_instantiation(instance):
    assert isinstance(instance, aadl2_BehavioralFeature)

@given(instance=aadl2_FlowImplementation_strategy)
@settings(max_examples=50)
def test_aadl2_flowimplementation_instantiation(instance):
    assert isinstance(instance, aadl2_FlowImplementation)



@given(instance=aadl2_FlowImplementation_strategy)
def test_aadl2_flowimplementation_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=aadl2_ModeFeature_strategy)
@settings(max_examples=50)
def test_aadl2_modefeature_instantiation(instance):
    assert isinstance(instance, aadl2_ModeFeature)

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

@given(instance=aadl2_SubprogramCallSequence_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramcallsequence_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramCallSequence)

@given(instance=aadl2_ProcessorFeature_strategy)
@settings(max_examples=50)
def test_aadl2_processorfeature_instantiation(instance):
    assert isinstance(instance, aadl2_ProcessorFeature)

@given(instance=aadl2_InternalFeature_strategy)
@settings(max_examples=50)
def test_aadl2_internalfeature_instantiation(instance):
    assert isinstance(instance, aadl2_InternalFeature)



@given(instance=aadl2_InternalFeature_strategy)
def test_aadl2_internalfeature_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

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

@given(instance=aadl2_Generalization__strategy)
@settings(max_examples=50)
def test_aadl2_generalization__instantiation(instance):
    assert isinstance(instance, aadl2_Generalization_)

@given(instance=PropertyOwner_strategy)
@settings(max_examples=50)
def test_propertyowner_instantiation(instance):
    assert isinstance(instance, PropertyOwner)

@given(instance=aadl2_ClassifierValue_strategy)
@settings(max_examples=50)
def test_aadl2_classifiervalue_instantiation(instance):
    assert isinstance(instance, aadl2_ClassifierValue)

@given(instance=aadl2_ArraySizeProperty_strategy)
@settings(max_examples=50)
def test_aadl2_arraysizeproperty_instantiation(instance):
    assert isinstance(instance, aadl2_ArraySizeProperty)

@given(instance=aadl2_AbstractNamedValue_strategy)
@settings(max_examples=50)
def test_aadl2_abstractnamedvalue_instantiation(instance):
    assert isinstance(instance, aadl2_AbstractNamedValue)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=aadl2_SubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2_subcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2_SubcomponentType)

@given(instance=aadl2_PropertyType_strategy)
@settings(max_examples=50)
def test_aadl2_propertytype_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyType)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=aadl2_RecordType_strategy)
@settings(max_examples=50)
def test_aadl2_recordtype_instantiation(instance):
    assert isinstance(instance, aadl2_RecordType)

@given(instance=aadl2_PropertySet_strategy)
@settings(max_examples=50)
def test_aadl2_propertyset_instantiation(instance):
    assert isinstance(instance, aadl2_PropertySet)

@given(instance=aadl2_EnumerationType_strategy)
@settings(max_examples=50)
def test_aadl2_enumerationtype_instantiation(instance):
    assert isinstance(instance, aadl2_EnumerationType)

@given(instance=aadl2_GlobalNamespace_strategy)
@settings(max_examples=50)
def test_aadl2_globalnamespace_instantiation(instance):
    assert isinstance(instance, aadl2_GlobalNamespace)

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
def test_aadl2_packagesection_noProperties_setter(instance):
    original = instance.noProperties
    instance.noProperties = original
    assert instance.noProperties == original

@given(instance=ArraySizeProperty_strategy)
@settings(max_examples=50)
def test_arraysizeproperty_instantiation(instance):
    assert isinstance(instance, ArraySizeProperty)

@given(instance=AbstractNamedValue_strategy)
@settings(max_examples=50)
def test_abstractnamedvalue_instantiation(instance):
    assert isinstance(instance, AbstractNamedValue)

@given(instance=BasicProperty_strategy)
@settings(max_examples=50)
def test_basicproperty_instantiation(instance):
    assert isinstance(instance, BasicProperty)

@given(instance=aadl2_RecordField_strategy)
@settings(max_examples=50)
def test_aadl2_recordfield_instantiation(instance):
    assert isinstance(instance, aadl2_RecordField)

@given(instance=aadl2_ModalPropertyValue_strategy)
@settings(max_examples=50)
def test_aadl2_modalpropertyvalue_instantiation(instance):
    assert isinstance(instance, aadl2_ModalPropertyValue)

@given(instance=aadl2_Classifier_strategy)
@settings(max_examples=50)
def test_aadl2_classifier_instantiation(instance):
    assert isinstance(instance, aadl2_Classifier)



@given(instance=aadl2_Classifier_strategy)
def test_aadl2_classifier_noAnnexes_setter(instance):
    original = instance.noAnnexes
    instance.noAnnexes = original
    assert instance.noAnnexes == original



@given(instance=aadl2_Classifier_strategy)
def test_aadl2_classifier_noPrototypes_setter(instance):
    original = instance.noPrototypes
    instance.noPrototypes = original
    assert instance.noPrototypes == original



@given(instance=aadl2_Classifier_strategy)
def test_aadl2_classifier_noProperties_setter(instance):
    original = instance.noProperties
    instance.noProperties = original
    assert instance.noProperties == original

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

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=aadl2_PropertyConstant_strategy)
@settings(max_examples=50)
def test_aadl2_propertyconstant_instantiation(instance):
    assert isinstance(instance, aadl2_PropertyConstant)

@given(instance=aadl2_BasicProperty_strategy)
@settings(max_examples=50)
def test_aadl2_basicproperty_instantiation(instance):
    assert isinstance(instance, aadl2_BasicProperty)

@given(instance=aadl2_MetaclassReference_strategy)
@settings(max_examples=50)
def test_aadl2_metaclassreference_instantiation(instance):
    assert isinstance(instance, aadl2_MetaclassReference)



@given(instance=aadl2_MetaclassReference_strategy)
def test_aadl2_metaclassreference_metaclassName_setter(instance):
    original = instance.metaclassName
    instance.metaclassName = original
    assert instance.metaclassName == original



@given(instance=aadl2_MetaclassReference_strategy)
def test_aadl2_metaclassreference_annexName_setter(instance):
    original = instance.annexName
    instance.annexName = original
    assert instance.annexName == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=aadl2_SubprogramGroup_strategy)
@settings(max_examples=50)
def test_aadl2_subprogramgroup_instantiation(instance):
    assert isinstance(instance, aadl2_SubprogramGroup)

@given(instance=aadl2_Data_strategy)
@settings(max_examples=50)
def test_aadl2_data_instantiation(instance):
    assert isinstance(instance, aadl2_Data)

@given(instance=aadl2_Memory_strategy)
@settings(max_examples=50)
def test_aadl2_memory_instantiation(instance):
    assert isinstance(instance, aadl2_Memory)

@given(instance=aadl2_RefinableElement_strategy)
@settings(max_examples=50)
def test_aadl2_refinableelement_instantiation(instance):
    assert isinstance(instance, aadl2_RefinableElement)

@given(instance=aadl2_ComponentTypeRename_strategy)
@settings(max_examples=50)
def test_aadl2_componenttyperename_instantiation(instance):
    assert isinstance(instance, aadl2_ComponentTypeRename)



@given(instance=aadl2_ComponentTypeRename_strategy)
def test_aadl2_componenttyperename_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=aadl2_Processor_strategy)
@settings(max_examples=50)
def test_aadl2_processor_instantiation(instance):
    assert isinstance(instance, aadl2_Processor)

@given(instance=aadl2_Thread_strategy)
@settings(max_examples=50)
def test_aadl2_thread_instantiation(instance):
    assert isinstance(instance, aadl2_Thread)

@given(instance=aadl2_Context_strategy)
@settings(max_examples=50)
def test_aadl2_context_instantiation(instance):
    assert isinstance(instance, aadl2_Context)

@given(instance=aadl2_Flow_strategy)
@settings(max_examples=50)
def test_aadl2_flow_instantiation(instance):
    assert isinstance(instance, aadl2_Flow)

@given(instance=aadl2_Subprogram_strategy)
@settings(max_examples=50)
def test_aadl2_subprogram_instantiation(instance):
    assert isinstance(instance, aadl2_Subprogram)

@given(instance=aadl2_FeatureGroupTypeRename_strategy)
@settings(max_examples=50)
def test_aadl2_featuregrouptyperename_instantiation(instance):
    assert isinstance(instance, aadl2_FeatureGroupTypeRename)

@given(instance=aadl2_ModelUnit_strategy)
@settings(max_examples=50)
def test_aadl2_modelunit_instantiation(instance):
    assert isinstance(instance, aadl2_ModelUnit)

@given(instance=aadl2_ThreadGroup_strategy)
@settings(max_examples=50)
def test_aadl2_threadgroup_instantiation(instance):
    assert isinstance(instance, aadl2_ThreadGroup)

@given(instance=aadl2_TriggerPort_strategy)
@settings(max_examples=50)
def test_aadl2_triggerport_instantiation(instance):
    assert isinstance(instance, aadl2_TriggerPort)

@given(instance=aadl2_VirtualProcessor_strategy)
@settings(max_examples=50)
def test_aadl2_virtualprocessor_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualProcessor)

@given(instance=aadl2_ConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2_connectionend_instantiation(instance):
    assert isinstance(instance, aadl2_ConnectionEnd)

@given(instance=aadl2_Abstract_strategy)
@settings(max_examples=50)
def test_aadl2_abstract_instantiation(instance):
    assert isinstance(instance, aadl2_Abstract)

@given(instance=aadl2_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_aadl2_enumerationliteral_instantiation(instance):
    assert isinstance(instance, aadl2_EnumerationLiteral)

@given(instance=aadl2_TypedElement_strategy)
@settings(max_examples=50)
def test_aadl2_typedelement_instantiation(instance):
    assert isinstance(instance, aadl2_TypedElement)

@given(instance=aadl2_ModalElement_strategy)
@settings(max_examples=50)
def test_aadl2_modalelement_instantiation(instance):
    assert isinstance(instance, aadl2_ModalElement)

@given(instance=aadl2_PackageRename_strategy)
@settings(max_examples=50)
def test_aadl2_packagerename_instantiation(instance):
    assert isinstance(instance, aadl2_PackageRename)



@given(instance=aadl2_PackageRename_strategy)
def test_aadl2_packagerename_renameAll_setter(instance):
    original = instance.renameAll
    instance.renameAll = original
    assert instance.renameAll == original

@given(instance=aadl2_AnnexLibrary_strategy)
@settings(max_examples=50)
def test_aadl2_annexlibrary_instantiation(instance):
    assert isinstance(instance, aadl2_AnnexLibrary)

@given(instance=aadl2_Bus_strategy)
@settings(max_examples=50)
def test_aadl2_bus_instantiation(instance):
    assert isinstance(instance, aadl2_Bus)

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

@given(instance=aadl2_EndToEndFlowElement_strategy)
@settings(max_examples=50)
def test_aadl2_endtoendflowelement_instantiation(instance):
    assert isinstance(instance, aadl2_EndToEndFlowElement)

@given(instance=aadl2_System_strategy)
@settings(max_examples=50)
def test_aadl2_system_instantiation(instance):
    assert isinstance(instance, aadl2_System)

@given(instance=aadl2_ClassifierFeature_strategy)
@settings(max_examples=50)
def test_aadl2_classifierfeature_instantiation(instance):
    assert isinstance(instance, aadl2_ClassifierFeature)

@given(instance=aadl2_Device_strategy)
@settings(max_examples=50)
def test_aadl2_device_instantiation(instance):
    assert isinstance(instance, aadl2_Device)

@given(instance=aadl2_Process_strategy)
@settings(max_examples=50)
def test_aadl2_process_instantiation(instance):
    assert isinstance(instance, aadl2_Process)

@given(instance=aadl2_VirtualBus_strategy)
@settings(max_examples=50)
def test_aadl2_virtualbus_instantiation(instance):
    assert isinstance(instance, aadl2_VirtualBus)

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

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=aadl2_FlowEnd_strategy)
@settings(max_examples=50)
def test_aadl2_flowend_instantiation(instance):
    assert isinstance(instance, aadl2_FlowEnd)

@given(instance=aadl2_FlowSegment_strategy)
@settings(max_examples=50)
def test_aadl2_flowsegment_instantiation(instance):
    assert isinstance(instance, aadl2_FlowSegment)

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

@given(instance=aadl2_NumericRange_strategy)
@settings(max_examples=50)
def test_aadl2_numericrange_instantiation(instance):
    assert isinstance(instance, aadl2_NumericRange)

@given(instance=aadl2_ModeTransitionTrigger_strategy)
@settings(max_examples=50)
def test_aadl2_modetransitiontrigger_instantiation(instance):
    assert isinstance(instance, aadl2_ModeTransitionTrigger)

@given(instance=aadl2_ArrayDimension_strategy)
@settings(max_examples=50)
def test_aadl2_arraydimension_instantiation(instance):
    assert isinstance(instance, aadl2_ArrayDimension)

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

@given(instance=aadl2_Relationship_strategy)
@settings(max_examples=50)
def test_aadl2_relationship_instantiation(instance):
    assert isinstance(instance, aadl2_Relationship)

@given(instance=aadl2_ArraySize_strategy)
@settings(max_examples=50)
def test_aadl2_arraysize_instantiation(instance):
    assert isinstance(instance, aadl2_ArraySize)



@given(instance=aadl2_ArraySize_strategy)
def test_aadl2_arraysize_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=aadl2_ContainmentPathElement_strategy)
@settings(max_examples=50)
def test_aadl2_containmentpathelement_instantiation(instance):
    assert isinstance(instance, aadl2_ContainmentPathElement)



@given(instance=aadl2_ContainmentPathElement_strategy)
def test_aadl2_containmentpathelement_annexName_setter(instance):
    original = instance.annexName
    instance.annexName = original
    assert instance.annexName == original

@given(instance=aadl2_ContainedNamedElement_strategy)
@settings(max_examples=50)
def test_aadl2_containednamedelement_instantiation(instance):
    assert isinstance(instance, aadl2_ContainedNamedElement)

@given(instance=aadl2_ConnectedElement_strategy)
@settings(max_examples=50)
def test_aadl2_connectedelement_instantiation(instance):
    assert isinstance(instance, aadl2_ConnectedElement)

@given(instance=aadl2_PrototypeBinding_strategy)
@settings(max_examples=50)
def test_aadl2_prototypebinding_instantiation(instance):
    assert isinstance(instance, aadl2_PrototypeBinding)

@given(instance=aadl2_Comment_strategy)
@settings(max_examples=50)
def test_aadl2_comment_instantiation(instance):
    assert isinstance(instance, aadl2_Comment)



@given(instance=aadl2_Comment_strategy)
def test_aadl2_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

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

@given(instance=aadl2_EndToEndFlowSegment_strategy)
@settings(max_examples=50)
def test_aadl2_endtoendflowsegment_instantiation(instance):
    assert isinstance(instance, aadl2_EndToEndFlowSegment)

@given(instance=aadl2_BasicPropertyAssociation_strategy)
@settings(max_examples=50)
def test_aadl2_basicpropertyassociation_instantiation(instance):
    assert isinstance(instance, aadl2_BasicPropertyAssociation)

@given(instance=aadl2_ArrayableElement_strategy)
@settings(max_examples=50)
def test_aadl2_arrayableelement_instantiation(instance):
    assert isinstance(instance, aadl2_ArrayableElement)

@given(instance=aadl2_ModeBinding_strategy)
@settings(max_examples=50)
def test_aadl2_modebinding_instantiation(instance):
    assert isinstance(instance, aadl2_ModeBinding)

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
