import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NumberType,
    aadl2::AadlReal,
    aadl2::AadlInteger,
    NonListType,
    aadl2::AadlString,
    aadl2::ClassifierType,
    aadl2::RangeType,
    aadl2::NumberType,
    aadl2::ReferenceType,
    aadl2::AadlBoolean,
    PropertyType,
    aadl2::ListType,
    aadl2::NonListType,
    EnumerationType,
    aadl2::UnitsType,
    NumberValue,
    aadl2::IntegerLiteral,
    ContainedNamedElement,
    aadl2::RealLiteral,
    EnumerationLiteral,
    aadl2::UnitLiteral,
    PropertyExpression,
    aadl2::ListValue,
    aadl2::Operation,
    aadl2::PropertyValue,
    ArraySizeProperty,
    PropertyValue,
    aadl2::NumberValue,
    aadl2::BooleanLiteral,
    aadl2::NamedValue,
    aadl2::RangeValue,
    aadl2::ComputedValue,
    aadl2::ReferenceValue,
    aadl2::RecordValue,
    aadl2::StringLiteral,
    VirtualProcessorClassifier,
    VirtualBusClassifier,
    ThreadGroupClassifier,
    ThreadClassifier,
    ProcessClassifier,
    ProcessorClassifier,
    SystemClassifier,
    SubprogramGroupClassifier,
    SubprogramClassifier,
    MemoryClassifier,
    Generalization_,
    aadl2::GroupExtension,
    EndToEndFlowElement,
    aadl2::FlowElement,
    Feature,
    aadl2::DirectedFeature,
    aadl2::CallContext,
    aadl2::FeatureType,
    CallContext,
    FeatureGroupConnectionEnd,
    Context,
    DirectedFeature,
    FlowElement,
    ModalPath,
    FlowFeature,
    Prototype,
    ConnectionEnd,
    aadl2::FeatureConnectionEnd,
    Flow,
    aadl2::FeatureGroup,
    aadl2::TypeExtension,
    aadl2::FlowSpecification,
    ArrayableElement,
    FeatureConnectionEnd,
    aadl2::FeatureClassifier,
    FeatureClassifier,
    SubcomponentType,
    aadl2::ComponentPrototype,
    Classifier,
    aadl2::ComponentClassifier,
    aadl2::EndToEndFlow,
    aadl2::Realization,
    aadl2::ImplementationExtension,
    ComponentClassifier,
    aadl2::ComponentType,
    aadl2::ComponentImplementation,
    aadl2::ArraySizeProperty,
    RefinableElement,
    CalledSubprogram,
    StructuralFeature,
    aadl2::Feature,
    aadl2::ProcessorFeature,
    aadl2::FlowFeature,
    aadl2::Connection,
    ClassifierFeature,
    aadl2::FlowImplementation,
    aadl2::BehavioralFeature,
    aadl2::StructuralFeature,
    aadl2::ModeFeature,
    aadl2::CalledSubprogram,
    Relationship,
    aadl2::DirectedRelationship,
    DirectedRelationship,
    ModeFeature,
    aadl2::ModeTransition,
    aadl2::Mode,
    ModalElement,
    aadl2::Subcomponent,
    aadl2::ModalPath,
    aadl2::Prototype,
    aadl2::AnnexSubclause,
    aadl2::Generalization_,
    PropertyOwner,
    aadl2::ClassifierValue,
    aadl2::AbstractNamedValue,
    Type,
    aadl2::SubcomponentType,
    Namespace,
    aadl2::EnumerationType,
    aadl2::RecordType,
    aadl2::GlobalNamespace,
    aadl2::MetaclassReference,
    AbstractNamedValue,
    BasicProperty,
    aadl2::RecordField,
    aadl2::ModalPropertyValue,
    aadl2::Classifier,
    aadl2::PropertyType,
    TypedElement,
    aadl2::PropertyConstant,
    aadl2::BasicProperty,
    NamedElement,
    aadl2::Namespace,
    aadl2::TypedElement,
    aadl2::ConnectionEnd,
    aadl2::ClassifierFeature,
    aadl2::TriggerPort,
    aadl2::EnumerationLiteral,
    aadl2::Context,
    aadl2::EndToEndFlowElement,
    aadl2::RefinableElement,
    aadl2::ModalElement,
    aadl2::Flow,
    aadl2::Type,
    aadl2::Property,
    Element,
    aadl2::ContainedNamedElement,
    aadl2::PropertyAssociation,
    aadl2::PropertyExpression,
    aadl2::ArraySize,
    aadl2::NumericRange,
    aadl2::Relationship,
    aadl2::PropertyOwner,
    aadl2::PrototypeBinding,
    aadl2::ContainmentPathElement,
    aadl2::ModeTransitionTrigger,
    aadl2::ArrayDimension,
    aadl2::BasicPropertyAssociation,
    aadl2::ArrayableElement,
    aadl2::FlowEnd,
    aadl2::ArrayRange,
    aadl2::NamedElement,
    aadl2::ComponentImplementationReference,
    aadl2::Comment,
    aadl2::Element,
    DeviceClassifier,
    DataClassifier,
    ComponentPrototype,
    aadl2::VirtualProcessor,
    BusClassifier,
    Thread,
    VirtualProcessor,
    aadl2::VirtualBus,
    VirtualBus,
    aadl2::ThreadGroup,
    ThreadGroup,
    aadl2::Thread,
    Processor,
    aadl2::Process,
    aadl2::SubprogramGroup,
    SubprogramGroup,
    aadl2::System,
    System,
    aadl2::Processor,
    aadl2::Bus,
    Process,
    aadl2::Memory,
    Memory,
    aadl2::Device,
    Device,
    Bus,
    aadl2::ProcessorSubcomponentType,
    BehavioredImplementation,
    aadl2::ThreadImplementation,
    aadl2::SubprogramImplementation,
    aadl2::DeviceSubcomponentType,
    aadl2::MemorySubcomponentType,
    aadl2::ProcessSubcomponentType,
    aadl2::SystemSubcomponentType,
    aadl2::ThreadSubcomponentType,
    aadl2::ThreadGroupSubcomponentType,
    BusFeatureClassifier,
    aadl2::VirtualProcessorSubcomponentType,
    VirtualProcessorSubcomponentType,
    aadl2::VirtualProcessorClassifier,
    aadl2::VirtualProcessorPrototype,
    VirtualBusSubcomponentType,
    aadl2::VirtualBusPrototype,
    aadl2::VirtualBusClassifier,
    ThreadSubcomponentType,
    aadl2::ThreadPrototype,
    aadl2::ThreadClassifier,
    ThreadGroupSubcomponentType,
    aadl2::ThreadGroupPrototype,
    aadl2::ThreadGroupClassifier,
    SystemSubcomponentType,
    aadl2::SystemPrototype,
    aadl2::SystemClassifier,
    SubprogramGroupSubcomponentType,
    aadl2::SubprogramGroupClassifier,
    aadl2::SubprogramGroupPrototype,
    ProcessSubcomponentType,
    aadl2::ProcessPrototype,
    aadl2::ProcessClassifier,
    ProcessorSubcomponentType,
    aadl2::ProcessorClassifier,
    aadl2::ProcessorPrototype,
    MemorySubcomponentType,
    aadl2::MemoryClassifier,
    aadl2::MemoryPrototype,
    DeviceSubcomponentType,
    aadl2::DeviceClassifier,
    aadl2::DevicePrototype,
    BusSubcomponentType,
    aadl2::BusPrototype,
    aadl2::BusClassifier,
    AbstractSubcomponentType,
    AbstractClassifier,
    aadl2::AbstractImplementation,
    ComponentType,
    aadl2::MemoryType,
    aadl2::ThreadGroupType,
    aadl2::VirtualProcessorType,
    aadl2::BusType,
    aadl2::DataType,
    aadl2::ProcessType,
    aadl2::SubprogramType,
    aadl2::ThreadType,
    aadl2::DeviceType,
    aadl2::VirtualBusType,
    aadl2::ProcessorType,
    aadl2::SystemType,
    aadl2::SubprogramGroupType,
    aadl2::AbstractType,
    ComponentImplementation,
    aadl2::ProcessorImplementation,
    aadl2::SystemImplementation,
    aadl2::BusImplementation,
    aadl2::DataImplementation,
    aadl2::MemoryImplementation,
    aadl2::VirtualProcessorImplementation,
    aadl2::VirtualBusImplementation,
    aadl2::ThreadGroupImplementation,
    aadl2::SubprogramGroupImplementation,
    aadl2::ProcessImplementation,
    aadl2::DeviceImplementation,
    aadl2::BehavioredImplementation,
    BehavioralFeature,
    aadl2::SubprogramCall,
    aadl2::SubprogramCallSequence,
    aadl2::FeaturePrototypeActual,
    aadl2::ComponentPrototypeActual,
    PrototypeBinding,
    aadl2::FeaturePrototypeBinding,
    aadl2::ComponentPrototypeBinding,
    FeaturePrototypeActual,
    aadl2::FeaturePrototypeReference,
    aadl2::AccessSpecification,
    aadl2::PortSpecification,
    aadl2::FeatureGroupPrototypeActual,
    aadl2::FeatureGroupPrototypeBinding,
    ModelUnit,
    aadl2::PropertySet,
    aadl2::AadlPackage,
    aadl2::PackageRename,
    aadl2::PackageSection,
    PackageSection,
    aadl2::PrivatePackageSection,
    aadl2::PublicPackageSection,
    aadl2::ModelUnit,
    aadl2::FeatureGroupTypeRename,
    aadl2::ComponentTypeRename,
    aadl2::Subprogram,
    SubprogramSubcomponentType,
    Subprogram,
    aadl2::SubprogramPrototype,
    aadl2::SubprogramClassifier,
    AnnexSubclause,
    aadl2::DefaultAnnexSubclause,
    AnnexLibrary,
    aadl2::DefaultAnnexLibrary,
    aadl2::AnnexLibrary,
    InternalFeature,
    aadl2::EventDataSource,
    aadl2::EventSource,
    ProcessorFeature,
    aadl2::Data,
    DataSubcomponentType,
    Data,
    aadl2::DataPrototype,
    aadl2::DataClassifier,
    aadl2::Abstract,
    Abstract,
    aadl2::AbstractClassifier,
    aadl2::AbstractPrototype,
    Subcomponent,
    aadl2::SystemSubcomponent,
    aadl2::VirtualProcessorSubcomponent,
    aadl2::ProcessorSubcomponent,
    aadl2::AbstractSubcomponent,
    aadl2::ProcessSubcomponent,
    aadl2::MemorySubcomponent,
    aadl2::ThreadGroupSubcomponent,
    aadl2::ThreadSubcomponent,
    aadl2::DeviceSubcomponent,
    Connection,
    aadl2::AccessConnection,
    aadl2::FeatureConnection,
    aadl2::ParameterConnection,
    aadl2::PortConnection,
    aadl2::FeatureGroupConnection,
    aadl2::EndToEndFlowSegment,
    aadl2::FlowSegment,
    aadl2::ConnectedElement,
    aadl2::ModeBinding,
    aadl2::FeaturePrototype,
    TriggerPort,
    aadl2::AbstractFeature,
    Port,
    aadl2::AccessConnectionEnd,
    AccessConnectionEnd,
    aadl2::SubprogramGroupSubcomponent,
    aadl2::BusSubcomponent,
    aadl2::SubprogramSubcomponent,
    aadl2::SubprogramProxy,
    aadl2::VirtualBusSubcomponent,
    aadl2::Access,
    aadl2::BusFeatureClassifier,
    aadl2::AbstractFeatureClassifier,
    Access,
    aadl2::BusAccess,
    AbstractFeatureClassifier,
    aadl2::BusSubcomponentType,
    aadl2::SubprogramGroupSubcomponentType,
    aadl2::SubprogramSubcomponentType,
    aadl2::VirtualBusSubcomponentType,
    aadl2::AbstractSubcomponentType,
    aadl2::PortConnectionEnd,
    aadl2::ParameterConnectionEnd,
    aadl2::DataSubcomponentType,
    PortConnectionEnd,
    aadl2::PortProxy,
    aadl2::InternalFeature,
    aadl2::Port,
    ParameterConnectionEnd,
    aadl2::DataSubcomponent,
    aadl2::DataPort,
    aadl2::DataAccess,
    aadl2::Parameter,
    aadl2::EventPort,
    aadl2::SubprogramGroupAccess,
    aadl2::SubprogramAccess,
    FeatureType,
    aadl2::FeatureGroupType,
    aadl2::FeatureGroupPrototype,
    aadl2::FeatureGroupConnectionEnd,
    aadl2::EventDataPort,
    AccessType,
    DirectionType,
    ComponentCategory,
    OperationKind,
    AccessCategory,
    FlowKind,
    PortCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_numbertype_is_not_abstract():
    assert not inspect.isabstract(NumberType)


def test_numbertype_constructor_exists():
    assert callable(NumberType.__init__)


def test_numbertype_constructor_args():
    sig = inspect.signature(NumberType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::aadlreal_is_not_abstract():
    assert not inspect.isabstract(aadl2::AadlReal)


def test_aadl2::aadlreal_constructor_exists():
    assert callable(aadl2::AadlReal.__init__)


def test_aadl2::aadlreal_constructor_args():
    sig = inspect.signature(aadl2::AadlReal.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::aadlinteger_is_not_abstract():
    assert not inspect.isabstract(aadl2::AadlInteger)


def test_aadl2::aadlinteger_constructor_exists():
    assert callable(aadl2::AadlInteger.__init__)


def test_aadl2::aadlinteger_constructor_args():
    sig = inspect.signature(aadl2::AadlInteger.__init__)
    params = list(sig.parameters.keys())



def test_nonlisttype_is_not_abstract():
    assert not inspect.isabstract(NonListType)


def test_nonlisttype_constructor_exists():
    assert callable(NonListType.__init__)


def test_nonlisttype_constructor_args():
    sig = inspect.signature(NonListType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::aadlstring_is_not_abstract():
    assert not inspect.isabstract(aadl2::AadlString)


def test_aadl2::aadlstring_constructor_exists():
    assert callable(aadl2::AadlString.__init__)


def test_aadl2::aadlstring_constructor_args():
    sig = inspect.signature(aadl2::AadlString.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::classifiertype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ClassifierType)


def test_aadl2::classifiertype_constructor_exists():
    assert callable(aadl2::ClassifierType.__init__)


def test_aadl2::classifiertype_constructor_args():
    sig = inspect.signature(aadl2::ClassifierType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::rangetype_is_not_abstract():
    assert not inspect.isabstract(aadl2::RangeType)


def test_aadl2::rangetype_constructor_exists():
    assert callable(aadl2::RangeType.__init__)


def test_aadl2::rangetype_constructor_args():
    sig = inspect.signature(aadl2::RangeType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::numbertype_is_not_abstract():
    assert not inspect.isabstract(aadl2::NumberType)


def test_aadl2::numbertype_constructor_exists():
    assert callable(aadl2::NumberType.__init__)


def test_aadl2::numbertype_constructor_args():
    sig = inspect.signature(aadl2::NumberType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::referencetype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ReferenceType)


def test_aadl2::referencetype_constructor_exists():
    assert callable(aadl2::ReferenceType.__init__)


def test_aadl2::referencetype_constructor_args():
    sig = inspect.signature(aadl2::ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::aadlboolean_is_not_abstract():
    assert not inspect.isabstract(aadl2::AadlBoolean)


def test_aadl2::aadlboolean_constructor_exists():
    assert callable(aadl2::AadlBoolean.__init__)


def test_aadl2::aadlboolean_constructor_args():
    sig = inspect.signature(aadl2::AadlBoolean.__init__)
    params = list(sig.parameters.keys())



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::listtype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ListType)


def test_aadl2::listtype_constructor_exists():
    assert callable(aadl2::ListType.__init__)


def test_aadl2::listtype_constructor_args():
    sig = inspect.signature(aadl2::ListType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::nonlisttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::NonListType)


def test_aadl2::nonlisttype_constructor_exists():
    assert callable(aadl2::NonListType.__init__)


def test_aadl2::nonlisttype_constructor_args():
    sig = inspect.signature(aadl2::NonListType.__init__)
    params = list(sig.parameters.keys())



def test_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(EnumerationType)


def test_enumerationtype_constructor_exists():
    assert callable(EnumerationType.__init__)


def test_enumerationtype_constructor_args():
    sig = inspect.signature(EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::unitstype_is_not_abstract():
    assert not inspect.isabstract(aadl2::UnitsType)


def test_aadl2::unitstype_constructor_exists():
    assert callable(aadl2::UnitsType.__init__)


def test_aadl2::unitstype_constructor_args():
    sig = inspect.signature(aadl2::UnitsType.__init__)
    params = list(sig.parameters.keys())



def test_numbervalue_is_not_abstract():
    assert not inspect.isabstract(NumberValue)


def test_numbervalue_constructor_exists():
    assert callable(NumberValue.__init__)


def test_numbervalue_constructor_args():
    sig = inspect.signature(NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::integerliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2::IntegerLiteral)


def test_aadl2::integerliteral_constructor_exists():
    assert callable(aadl2::IntegerLiteral.__init__)


def test_aadl2::integerliteral_constructor_args():
    sig = inspect.signature(aadl2::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "base" in params, "Missing parameter 'base'"

def test_aadl2::integerliteral_has_value():
    assert hasattr(aadl2::IntegerLiteral, "value")
    descriptor = None
    for klass in aadl2::IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::integerliteral_has_base():
    assert hasattr(aadl2::IntegerLiteral, "base")
    descriptor = None
    for klass in aadl2::IntegerLiteral.__mro__:
        if "base" in klass.__dict__:
            descriptor = klass.__dict__["base"]
            break
    assert isinstance(descriptor, property)



def test_containednamedelement_is_not_abstract():
    assert not inspect.isabstract(ContainedNamedElement)


def test_containednamedelement_constructor_exists():
    assert callable(ContainedNamedElement.__init__)


def test_containednamedelement_constructor_args():
    sig = inspect.signature(ContainedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::realliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2::RealLiteral)


def test_aadl2::realliteral_constructor_exists():
    assert callable(aadl2::RealLiteral.__init__)


def test_aadl2::realliteral_constructor_args():
    sig = inspect.signature(aadl2::RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_aadl2::realliteral_has_value():
    assert hasattr(aadl2::RealLiteral, "value")
    descriptor = None
    for klass in aadl2::RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::unitliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2::UnitLiteral)


def test_aadl2::unitliteral_constructor_exists():
    assert callable(aadl2::UnitLiteral.__init__)


def test_aadl2::unitliteral_constructor_args():
    sig = inspect.signature(aadl2::UnitLiteral.__init__)
    params = list(sig.parameters.keys())



def test_propertyexpression_is_not_abstract():
    assert not inspect.isabstract(PropertyExpression)


def test_propertyexpression_constructor_exists():
    assert callable(PropertyExpression.__init__)


def test_propertyexpression_constructor_args():
    sig = inspect.signature(PropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::listvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2::ListValue)


def test_aadl2::listvalue_constructor_exists():
    assert callable(aadl2::ListValue.__init__)


def test_aadl2::listvalue_constructor_args():
    sig = inspect.signature(aadl2::ListValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::operation_is_not_abstract():
    assert not inspect.isabstract(aadl2::Operation)


def test_aadl2::operation_constructor_exists():
    assert callable(aadl2::Operation.__init__)


def test_aadl2::operation_constructor_args():
    sig = inspect.signature(aadl2::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_aadl2::operation_has_op():
    assert hasattr(aadl2::Operation, "op")
    descriptor = None
    for klass in aadl2::Operation.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::propertyvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2::PropertyValue)


def test_aadl2::propertyvalue_constructor_exists():
    assert callable(aadl2::PropertyValue.__init__)


def test_aadl2::propertyvalue_constructor_args():
    sig = inspect.signature(aadl2::PropertyValue.__init__)
    params = list(sig.parameters.keys())



def test_arraysizeproperty_is_not_abstract():
    assert not inspect.isabstract(ArraySizeProperty)


def test_arraysizeproperty_constructor_exists():
    assert callable(ArraySizeProperty.__init__)


def test_arraysizeproperty_constructor_args():
    sig = inspect.signature(ArraySizeProperty.__init__)
    params = list(sig.parameters.keys())



def test_propertyvalue_is_not_abstract():
    assert not inspect.isabstract(PropertyValue)


def test_propertyvalue_constructor_exists():
    assert callable(PropertyValue.__init__)


def test_propertyvalue_constructor_args():
    sig = inspect.signature(PropertyValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::numbervalue_is_not_abstract():
    assert not inspect.isabstract(aadl2::NumberValue)


def test_aadl2::numbervalue_constructor_exists():
    assert callable(aadl2::NumberValue.__init__)


def test_aadl2::numbervalue_constructor_args():
    sig = inspect.signature(aadl2::NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2::BooleanLiteral)


def test_aadl2::booleanliteral_constructor_exists():
    assert callable(aadl2::BooleanLiteral.__init__)


def test_aadl2::booleanliteral_constructor_args():
    sig = inspect.signature(aadl2::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_aadl2::booleanliteral_has_value():
    assert hasattr(aadl2::BooleanLiteral, "value")
    descriptor = None
    for klass in aadl2::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::namedvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2::NamedValue)


def test_aadl2::namedvalue_constructor_exists():
    assert callable(aadl2::NamedValue.__init__)


def test_aadl2::namedvalue_constructor_args():
    sig = inspect.signature(aadl2::NamedValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::rangevalue_is_not_abstract():
    assert not inspect.isabstract(aadl2::RangeValue)


def test_aadl2::rangevalue_constructor_exists():
    assert callable(aadl2::RangeValue.__init__)


def test_aadl2::rangevalue_constructor_args():
    sig = inspect.signature(aadl2::RangeValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::computedvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2::ComputedValue)


def test_aadl2::computedvalue_constructor_exists():
    assert callable(aadl2::ComputedValue.__init__)


def test_aadl2::computedvalue_constructor_args():
    sig = inspect.signature(aadl2::ComputedValue.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_aadl2::computedvalue_has_function():
    assert hasattr(aadl2::ComputedValue, "function")
    descriptor = None
    for klass in aadl2::ComputedValue.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::referencevalue_is_not_abstract():
    assert not inspect.isabstract(aadl2::ReferenceValue)


def test_aadl2::referencevalue_constructor_exists():
    assert callable(aadl2::ReferenceValue.__init__)


def test_aadl2::referencevalue_constructor_args():
    sig = inspect.signature(aadl2::ReferenceValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::recordvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2::RecordValue)


def test_aadl2::recordvalue_constructor_exists():
    assert callable(aadl2::RecordValue.__init__)


def test_aadl2::recordvalue_constructor_args():
    sig = inspect.signature(aadl2::RecordValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::stringliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2::StringLiteral)


def test_aadl2::stringliteral_constructor_exists():
    assert callable(aadl2::StringLiteral.__init__)


def test_aadl2::stringliteral_constructor_args():
    sig = inspect.signature(aadl2::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_aadl2::stringliteral_has_value():
    assert hasattr(aadl2::StringLiteral, "value")
    descriptor = None
    for klass in aadl2::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



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



def test_processclassifier_is_not_abstract():
    assert not inspect.isabstract(ProcessClassifier)


def test_processclassifier_constructor_exists():
    assert callable(ProcessClassifier.__init__)


def test_processclassifier_constructor_args():
    sig = inspect.signature(ProcessClassifier.__init__)
    params = list(sig.parameters.keys())



def test_processorclassifier_is_not_abstract():
    assert not inspect.isabstract(ProcessorClassifier)


def test_processorclassifier_constructor_exists():
    assert callable(ProcessorClassifier.__init__)


def test_processorclassifier_constructor_args():
    sig = inspect.signature(ProcessorClassifier.__init__)
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



def test_memoryclassifier_is_not_abstract():
    assert not inspect.isabstract(MemoryClassifier)


def test_memoryclassifier_constructor_exists():
    assert callable(MemoryClassifier.__init__)


def test_memoryclassifier_constructor_args():
    sig = inspect.signature(MemoryClassifier.__init__)
    params = list(sig.parameters.keys())



def test_generalization__is_not_abstract():
    assert not inspect.isabstract(Generalization_)


def test_generalization__constructor_exists():
    assert callable(Generalization_.__init__)


def test_generalization__constructor_args():
    sig = inspect.signature(Generalization_.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::groupextension_is_not_abstract():
    assert not inspect.isabstract(aadl2::GroupExtension)


def test_aadl2::groupextension_constructor_exists():
    assert callable(aadl2::GroupExtension.__init__)


def test_aadl2::groupextension_constructor_args():
    sig = inspect.signature(aadl2::GroupExtension.__init__)
    params = list(sig.parameters.keys())



def test_endtoendflowelement_is_not_abstract():
    assert not inspect.isabstract(EndToEndFlowElement)


def test_endtoendflowelement_constructor_exists():
    assert callable(EndToEndFlowElement.__init__)


def test_endtoendflowelement_constructor_args():
    sig = inspect.signature(EndToEndFlowElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::flowelement_is_not_abstract():
    assert not inspect.isabstract(aadl2::FlowElement)


def test_aadl2::flowelement_constructor_exists():
    assert callable(aadl2::FlowElement.__init__)


def test_aadl2::flowelement_constructor_args():
    sig = inspect.signature(aadl2::FlowElement.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::directedfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2::DirectedFeature)


def test_aadl2::directedfeature_constructor_exists():
    assert callable(aadl2::DirectedFeature.__init__)


def test_aadl2::directedfeature_constructor_args():
    sig = inspect.signature(aadl2::DirectedFeature.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "out" in params, "Missing parameter 'out'"
    assert "in_" in params, "Missing parameter 'in_'"

def test_aadl2::directedfeature_has_direction():
    assert hasattr(aadl2::DirectedFeature, "direction")
    descriptor = None
    for klass in aadl2::DirectedFeature.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::directedfeature_has_out():
    assert hasattr(aadl2::DirectedFeature, "out")
    descriptor = None
    for klass in aadl2::DirectedFeature.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::directedfeature_has_in_():
    assert hasattr(aadl2::DirectedFeature, "in_")
    descriptor = None
    for klass in aadl2::DirectedFeature.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::callcontext_is_not_abstract():
    assert not inspect.isabstract(aadl2::CallContext)


def test_aadl2::callcontext_constructor_exists():
    assert callable(aadl2::CallContext.__init__)


def test_aadl2::callcontext_constructor_args():
    sig = inspect.signature(aadl2::CallContext.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featuretype_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeatureType)


def test_aadl2::featuretype_constructor_exists():
    assert callable(aadl2::FeatureType.__init__)


def test_aadl2::featuretype_constructor_args():
    sig = inspect.signature(aadl2::FeatureType.__init__)
    params = list(sig.parameters.keys())



def test_callcontext_is_not_abstract():
    assert not inspect.isabstract(CallContext)


def test_callcontext_constructor_exists():
    assert callable(CallContext.__init__)


def test_callcontext_constructor_args():
    sig = inspect.signature(CallContext.__init__)
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



def test_directedfeature_is_not_abstract():
    assert not inspect.isabstract(DirectedFeature)


def test_directedfeature_constructor_exists():
    assert callable(DirectedFeature.__init__)


def test_directedfeature_constructor_args():
    sig = inspect.signature(DirectedFeature.__init__)
    params = list(sig.parameters.keys())



def test_flowelement_is_not_abstract():
    assert not inspect.isabstract(FlowElement)


def test_flowelement_constructor_exists():
    assert callable(FlowElement.__init__)


def test_flowelement_constructor_args():
    sig = inspect.signature(FlowElement.__init__)
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



def test_connectionend_is_not_abstract():
    assert not inspect.isabstract(ConnectionEnd)


def test_connectionend_constructor_exists():
    assert callable(ConnectionEnd.__init__)


def test_connectionend_constructor_args():
    sig = inspect.signature(ConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featureconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeatureConnectionEnd)


def test_aadl2::featureconnectionend_constructor_exists():
    assert callable(aadl2::FeatureConnectionEnd.__init__)


def test_aadl2::featureconnectionend_constructor_args():
    sig = inspect.signature(aadl2::FeatureConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_flow_is_not_abstract():
    assert not inspect.isabstract(Flow)


def test_flow_constructor_exists():
    assert callable(Flow.__init__)


def test_flow_constructor_args():
    sig = inspect.signature(Flow.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featuregroup_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeatureGroup)


def test_aadl2::featuregroup_constructor_exists():
    assert callable(aadl2::FeatureGroup.__init__)


def test_aadl2::featuregroup_constructor_args():
    sig = inspect.signature(aadl2::FeatureGroup.__init__)
    params = list(sig.parameters.keys())
    assert "inverse" in params, "Missing parameter 'inverse'"

def test_aadl2::featuregroup_has_inverse():
    assert hasattr(aadl2::FeatureGroup, "inverse")
    descriptor = None
    for klass in aadl2::FeatureGroup.__mro__:
        if "inverse" in klass.__dict__:
            descriptor = klass.__dict__["inverse"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::typeextension_is_not_abstract():
    assert not inspect.isabstract(aadl2::TypeExtension)


def test_aadl2::typeextension_constructor_exists():
    assert callable(aadl2::TypeExtension.__init__)


def test_aadl2::typeextension_constructor_args():
    sig = inspect.signature(aadl2::TypeExtension.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::flowspecification_is_not_abstract():
    assert not inspect.isabstract(aadl2::FlowSpecification)


def test_aadl2::flowspecification_constructor_exists():
    assert callable(aadl2::FlowSpecification.__init__)


def test_aadl2::flowspecification_constructor_args():
    sig = inspect.signature(aadl2::FlowSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_aadl2::flowspecification_has_kind():
    assert hasattr(aadl2::FlowSpecification, "kind")
    descriptor = None
    for klass in aadl2::FlowSpecification.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



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



def test_aadl2::featureclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeatureClassifier)


def test_aadl2::featureclassifier_constructor_exists():
    assert callable(aadl2::FeatureClassifier.__init__)


def test_aadl2::featureclassifier_constructor_args():
    sig = inspect.signature(aadl2::FeatureClassifier.__init__)
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



def test_aadl2::componentprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ComponentPrototype)


def test_aadl2::componentprototype_constructor_exists():
    assert callable(aadl2::ComponentPrototype.__init__)


def test_aadl2::componentprototype_constructor_args():
    sig = inspect.signature(aadl2::ComponentPrototype.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"

def test_aadl2::componentprototype_has_array():
    assert hasattr(aadl2::ComponentPrototype, "array")
    descriptor = None
    for klass in aadl2::ComponentPrototype.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::componentclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::ComponentClassifier)


def test_aadl2::componentclassifier_constructor_exists():
    assert callable(aadl2::ComponentClassifier.__init__)


def test_aadl2::componentclassifier_constructor_args():
    sig = inspect.signature(aadl2::ComponentClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "derivedModes" in params, "Missing parameter 'derivedModes'"
    assert "noFlows" in params, "Missing parameter 'noFlows'"
    assert "noModes" in params, "Missing parameter 'noModes'"

def test_aadl2::componentclassifier_has_derivedModes():
    assert hasattr(aadl2::ComponentClassifier, "derivedModes")
    descriptor = None
    for klass in aadl2::ComponentClassifier.__mro__:
        if "derivedModes" in klass.__dict__:
            descriptor = klass.__dict__["derivedModes"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::componentclassifier_has_noFlows():
    assert hasattr(aadl2::ComponentClassifier, "noFlows")
    descriptor = None
    for klass in aadl2::ComponentClassifier.__mro__:
        if "noFlows" in klass.__dict__:
            descriptor = klass.__dict__["noFlows"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::componentclassifier_has_noModes():
    assert hasattr(aadl2::ComponentClassifier, "noModes")
    descriptor = None
    for klass in aadl2::ComponentClassifier.__mro__:
        if "noModes" in klass.__dict__:
            descriptor = klass.__dict__["noModes"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::endtoendflow_is_not_abstract():
    assert not inspect.isabstract(aadl2::EndToEndFlow)


def test_aadl2::endtoendflow_constructor_exists():
    assert callable(aadl2::EndToEndFlow.__init__)


def test_aadl2::endtoendflow_constructor_args():
    sig = inspect.signature(aadl2::EndToEndFlow.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::realization_is_not_abstract():
    assert not inspect.isabstract(aadl2::Realization)


def test_aadl2::realization_constructor_exists():
    assert callable(aadl2::Realization.__init__)


def test_aadl2::realization_constructor_args():
    sig = inspect.signature(aadl2::Realization.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::implementationextension_is_not_abstract():
    assert not inspect.isabstract(aadl2::ImplementationExtension)


def test_aadl2::implementationextension_constructor_exists():
    assert callable(aadl2::ImplementationExtension.__init__)


def test_aadl2::implementationextension_constructor_args():
    sig = inspect.signature(aadl2::ImplementationExtension.__init__)
    params = list(sig.parameters.keys())



def test_componentclassifier_is_not_abstract():
    assert not inspect.isabstract(ComponentClassifier)


def test_componentclassifier_constructor_exists():
    assert callable(ComponentClassifier.__init__)


def test_componentclassifier_constructor_args():
    sig = inspect.signature(ComponentClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::componenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ComponentType)


def test_aadl2::componenttype_constructor_exists():
    assert callable(aadl2::ComponentType.__init__)


def test_aadl2::componenttype_constructor_args():
    sig = inspect.signature(aadl2::ComponentType.__init__)
    params = list(sig.parameters.keys())
    assert "noFeatures" in params, "Missing parameter 'noFeatures'"

def test_aadl2::componenttype_has_noFeatures():
    assert hasattr(aadl2::ComponentType, "noFeatures")
    descriptor = None
    for klass in aadl2::ComponentType.__mro__:
        if "noFeatures" in klass.__dict__:
            descriptor = klass.__dict__["noFeatures"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::componentimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::ComponentImplementation)


def test_aadl2::componentimplementation_constructor_exists():
    assert callable(aadl2::ComponentImplementation.__init__)


def test_aadl2::componentimplementation_constructor_args():
    sig = inspect.signature(aadl2::ComponentImplementation.__init__)
    params = list(sig.parameters.keys())
    assert "noCalls" in params, "Missing parameter 'noCalls'"
    assert "noConnections" in params, "Missing parameter 'noConnections'"
    assert "noSubcomponents" in params, "Missing parameter 'noSubcomponents'"

def test_aadl2::componentimplementation_has_noCalls():
    assert hasattr(aadl2::ComponentImplementation, "noCalls")
    descriptor = None
    for klass in aadl2::ComponentImplementation.__mro__:
        if "noCalls" in klass.__dict__:
            descriptor = klass.__dict__["noCalls"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::componentimplementation_has_noConnections():
    assert hasattr(aadl2::ComponentImplementation, "noConnections")
    descriptor = None
    for klass in aadl2::ComponentImplementation.__mro__:
        if "noConnections" in klass.__dict__:
            descriptor = klass.__dict__["noConnections"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::componentimplementation_has_noSubcomponents():
    assert hasattr(aadl2::ComponentImplementation, "noSubcomponents")
    descriptor = None
    for klass in aadl2::ComponentImplementation.__mro__:
        if "noSubcomponents" in klass.__dict__:
            descriptor = klass.__dict__["noSubcomponents"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::arraysizeproperty_is_not_abstract():
    assert not inspect.isabstract(aadl2::ArraySizeProperty)


def test_aadl2::arraysizeproperty_constructor_exists():
    assert callable(aadl2::ArraySizeProperty.__init__)


def test_aadl2::arraysizeproperty_constructor_args():
    sig = inspect.signature(aadl2::ArraySizeProperty.__init__)
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



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::feature_is_not_abstract():
    assert not inspect.isabstract(aadl2::Feature)


def test_aadl2::feature_constructor_exists():
    assert callable(aadl2::Feature.__init__)


def test_aadl2::feature_constructor_args():
    sig = inspect.signature(aadl2::Feature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processorfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessorFeature)


def test_aadl2::processorfeature_constructor_exists():
    assert callable(aadl2::ProcessorFeature.__init__)


def test_aadl2::processorfeature_constructor_args():
    sig = inspect.signature(aadl2::ProcessorFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::flowfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2::FlowFeature)


def test_aadl2::flowfeature_constructor_exists():
    assert callable(aadl2::FlowFeature.__init__)


def test_aadl2::flowfeature_constructor_args():
    sig = inspect.signature(aadl2::FlowFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::connection_is_not_abstract():
    assert not inspect.isabstract(aadl2::Connection)


def test_aadl2::connection_constructor_exists():
    assert callable(aadl2::Connection.__init__)


def test_aadl2::connection_constructor_args():
    sig = inspect.signature(aadl2::Connection.__init__)
    params = list(sig.parameters.keys())
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"

def test_aadl2::connection_has_bidirectional():
    assert hasattr(aadl2::Connection, "bidirectional")
    descriptor = None
    for klass in aadl2::Connection.__mro__:
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



def test_aadl2::flowimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::FlowImplementation)


def test_aadl2::flowimplementation_constructor_exists():
    assert callable(aadl2::FlowImplementation.__init__)


def test_aadl2::flowimplementation_constructor_args():
    sig = inspect.signature(aadl2::FlowImplementation.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_aadl2::flowimplementation_has_kind():
    assert hasattr(aadl2::FlowImplementation, "kind")
    descriptor = None
    for klass in aadl2::FlowImplementation.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2::BehavioralFeature)


def test_aadl2::behavioralfeature_constructor_exists():
    assert callable(aadl2::BehavioralFeature.__init__)


def test_aadl2::behavioralfeature_constructor_args():
    sig = inspect.signature(aadl2::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2::StructuralFeature)


def test_aadl2::structuralfeature_constructor_exists():
    assert callable(aadl2::StructuralFeature.__init__)


def test_aadl2::structuralfeature_constructor_args():
    sig = inspect.signature(aadl2::StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::modefeature_is_not_abstract():
    assert not inspect.isabstract(aadl2::ModeFeature)


def test_aadl2::modefeature_constructor_exists():
    assert callable(aadl2::ModeFeature.__init__)


def test_aadl2::modefeature_constructor_args():
    sig = inspect.signature(aadl2::ModeFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::calledsubprogram_is_not_abstract():
    assert not inspect.isabstract(aadl2::CalledSubprogram)


def test_aadl2::calledsubprogram_constructor_exists():
    assert callable(aadl2::CalledSubprogram.__init__)


def test_aadl2::calledsubprogram_constructor_args():
    sig = inspect.signature(aadl2::CalledSubprogram.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::directedrelationship_is_not_abstract():
    assert not inspect.isabstract(aadl2::DirectedRelationship)


def test_aadl2::directedrelationship_constructor_exists():
    assert callable(aadl2::DirectedRelationship.__init__)


def test_aadl2::directedrelationship_constructor_args():
    sig = inspect.signature(aadl2::DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_modefeature_is_not_abstract():
    assert not inspect.isabstract(ModeFeature)


def test_modefeature_constructor_exists():
    assert callable(ModeFeature.__init__)


def test_modefeature_constructor_args():
    sig = inspect.signature(ModeFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::modetransition_is_not_abstract():
    assert not inspect.isabstract(aadl2::ModeTransition)


def test_aadl2::modetransition_constructor_exists():
    assert callable(aadl2::ModeTransition.__init__)


def test_aadl2::modetransition_constructor_args():
    sig = inspect.signature(aadl2::ModeTransition.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::mode_is_not_abstract():
    assert not inspect.isabstract(aadl2::Mode)


def test_aadl2::mode_constructor_exists():
    assert callable(aadl2::Mode.__init__)


def test_aadl2::mode_constructor_args():
    sig = inspect.signature(aadl2::Mode.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_aadl2::mode_has_derived():
    assert hasattr(aadl2::Mode, "derived")
    descriptor = None
    for klass in aadl2::Mode.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::mode_has_initial():
    assert hasattr(aadl2::Mode, "initial")
    descriptor = None
    for klass in aadl2::Mode.__mro__:
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



def test_aadl2::subcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::Subcomponent)


def test_aadl2::subcomponent_constructor_exists():
    assert callable(aadl2::Subcomponent.__init__)


def test_aadl2::subcomponent_constructor_args():
    sig = inspect.signature(aadl2::Subcomponent.__init__)
    params = list(sig.parameters.keys())
    assert "allModes" in params, "Missing parameter 'allModes'"

def test_aadl2::subcomponent_has_allModes():
    assert hasattr(aadl2::Subcomponent, "allModes")
    descriptor = None
    for klass in aadl2::Subcomponent.__mro__:
        if "allModes" in klass.__dict__:
            descriptor = klass.__dict__["allModes"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::modalpath_is_not_abstract():
    assert not inspect.isabstract(aadl2::ModalPath)


def test_aadl2::modalpath_constructor_exists():
    assert callable(aadl2::ModalPath.__init__)


def test_aadl2::modalpath_constructor_args():
    sig = inspect.signature(aadl2::ModalPath.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::prototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::Prototype)


def test_aadl2::prototype_constructor_exists():
    assert callable(aadl2::Prototype.__init__)


def test_aadl2::prototype_constructor_args():
    sig = inspect.signature(aadl2::Prototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::annexsubclause_is_not_abstract():
    assert not inspect.isabstract(aadl2::AnnexSubclause)


def test_aadl2::annexsubclause_constructor_exists():
    assert callable(aadl2::AnnexSubclause.__init__)


def test_aadl2::annexsubclause_constructor_args():
    sig = inspect.signature(aadl2::AnnexSubclause.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::generalization__is_not_abstract():
    assert not inspect.isabstract(aadl2::Generalization_)


def test_aadl2::generalization__constructor_exists():
    assert callable(aadl2::Generalization_.__init__)


def test_aadl2::generalization__constructor_args():
    sig = inspect.signature(aadl2::Generalization_.__init__)
    params = list(sig.parameters.keys())



def test_propertyowner_is_not_abstract():
    assert not inspect.isabstract(PropertyOwner)


def test_propertyowner_constructor_exists():
    assert callable(PropertyOwner.__init__)


def test_propertyowner_constructor_args():
    sig = inspect.signature(PropertyOwner.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::classifiervalue_is_not_abstract():
    assert not inspect.isabstract(aadl2::ClassifierValue)


def test_aadl2::classifiervalue_constructor_exists():
    assert callable(aadl2::ClassifierValue.__init__)


def test_aadl2::classifiervalue_constructor_args():
    sig = inspect.signature(aadl2::ClassifierValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::abstractnamedvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2::AbstractNamedValue)


def test_aadl2::abstractnamedvalue_constructor_exists():
    assert callable(aadl2::AbstractNamedValue.__init__)


def test_aadl2::abstractnamedvalue_constructor_args():
    sig = inspect.signature(aadl2::AbstractNamedValue.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubcomponentType)


def test_aadl2::subcomponenttype_constructor_exists():
    assert callable(aadl2::SubcomponentType.__init__)


def test_aadl2::subcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::SubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::enumerationtype_is_not_abstract():
    assert not inspect.isabstract(aadl2::EnumerationType)


def test_aadl2::enumerationtype_constructor_exists():
    assert callable(aadl2::EnumerationType.__init__)


def test_aadl2::enumerationtype_constructor_args():
    sig = inspect.signature(aadl2::EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::recordtype_is_not_abstract():
    assert not inspect.isabstract(aadl2::RecordType)


def test_aadl2::recordtype_constructor_exists():
    assert callable(aadl2::RecordType.__init__)


def test_aadl2::recordtype_constructor_args():
    sig = inspect.signature(aadl2::RecordType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::globalnamespace_is_not_abstract():
    assert not inspect.isabstract(aadl2::GlobalNamespace)


def test_aadl2::globalnamespace_constructor_exists():
    assert callable(aadl2::GlobalNamespace.__init__)


def test_aadl2::globalnamespace_constructor_args():
    sig = inspect.signature(aadl2::GlobalNamespace.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::metaclassreference_is_not_abstract():
    assert not inspect.isabstract(aadl2::MetaclassReference)


def test_aadl2::metaclassreference_constructor_exists():
    assert callable(aadl2::MetaclassReference.__init__)


def test_aadl2::metaclassreference_constructor_args():
    sig = inspect.signature(aadl2::MetaclassReference.__init__)
    params = list(sig.parameters.keys())
    assert "annexName" in params, "Missing parameter 'annexName'"
    assert "metaclassName" in params, "Missing parameter 'metaclassName'"

def test_aadl2::metaclassreference_has_annexName():
    assert hasattr(aadl2::MetaclassReference, "annexName")
    descriptor = None
    for klass in aadl2::MetaclassReference.__mro__:
        if "annexName" in klass.__dict__:
            descriptor = klass.__dict__["annexName"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::metaclassreference_has_metaclassName():
    assert hasattr(aadl2::MetaclassReference, "metaclassName")
    descriptor = None
    for klass in aadl2::MetaclassReference.__mro__:
        if "metaclassName" in klass.__dict__:
            descriptor = klass.__dict__["metaclassName"]
            break
    assert isinstance(descriptor, property)



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



def test_aadl2::recordfield_is_not_abstract():
    assert not inspect.isabstract(aadl2::RecordField)


def test_aadl2::recordfield_constructor_exists():
    assert callable(aadl2::RecordField.__init__)


def test_aadl2::recordfield_constructor_args():
    sig = inspect.signature(aadl2::RecordField.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::modalpropertyvalue_is_not_abstract():
    assert not inspect.isabstract(aadl2::ModalPropertyValue)


def test_aadl2::modalpropertyvalue_constructor_exists():
    assert callable(aadl2::ModalPropertyValue.__init__)


def test_aadl2::modalpropertyvalue_constructor_args():
    sig = inspect.signature(aadl2::ModalPropertyValue.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::classifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::Classifier)


def test_aadl2::classifier_constructor_exists():
    assert callable(aadl2::Classifier.__init__)


def test_aadl2::classifier_constructor_args():
    sig = inspect.signature(aadl2::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "noProperties" in params, "Missing parameter 'noProperties'"
    assert "noPrototypes" in params, "Missing parameter 'noPrototypes'"
    assert "noAnnexes" in params, "Missing parameter 'noAnnexes'"

def test_aadl2::classifier_has_noProperties():
    assert hasattr(aadl2::Classifier, "noProperties")
    descriptor = None
    for klass in aadl2::Classifier.__mro__:
        if "noProperties" in klass.__dict__:
            descriptor = klass.__dict__["noProperties"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::classifier_has_noPrototypes():
    assert hasattr(aadl2::Classifier, "noPrototypes")
    descriptor = None
    for klass in aadl2::Classifier.__mro__:
        if "noPrototypes" in klass.__dict__:
            descriptor = klass.__dict__["noPrototypes"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::classifier_has_noAnnexes():
    assert hasattr(aadl2::Classifier, "noAnnexes")
    descriptor = None
    for klass in aadl2::Classifier.__mro__:
        if "noAnnexes" in klass.__dict__:
            descriptor = klass.__dict__["noAnnexes"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::propertytype_is_not_abstract():
    assert not inspect.isabstract(aadl2::PropertyType)


def test_aadl2::propertytype_constructor_exists():
    assert callable(aadl2::PropertyType.__init__)


def test_aadl2::propertytype_constructor_args():
    sig = inspect.signature(aadl2::PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::propertyconstant_is_not_abstract():
    assert not inspect.isabstract(aadl2::PropertyConstant)


def test_aadl2::propertyconstant_constructor_exists():
    assert callable(aadl2::PropertyConstant.__init__)


def test_aadl2::propertyconstant_constructor_args():
    sig = inspect.signature(aadl2::PropertyConstant.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::basicproperty_is_not_abstract():
    assert not inspect.isabstract(aadl2::BasicProperty)


def test_aadl2::basicproperty_constructor_exists():
    assert callable(aadl2::BasicProperty.__init__)


def test_aadl2::basicproperty_constructor_args():
    sig = inspect.signature(aadl2::BasicProperty.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::namespace_is_not_abstract():
    assert not inspect.isabstract(aadl2::Namespace)


def test_aadl2::namespace_constructor_exists():
    assert callable(aadl2::Namespace.__init__)


def test_aadl2::namespace_constructor_args():
    sig = inspect.signature(aadl2::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::typedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2::TypedElement)


def test_aadl2::typedelement_constructor_exists():
    assert callable(aadl2::TypedElement.__init__)


def test_aadl2::typedelement_constructor_args():
    sig = inspect.signature(aadl2::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::connectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2::ConnectionEnd)


def test_aadl2::connectionend_constructor_exists():
    assert callable(aadl2::ConnectionEnd.__init__)


def test_aadl2::connectionend_constructor_args():
    sig = inspect.signature(aadl2::ConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::classifierfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2::ClassifierFeature)


def test_aadl2::classifierfeature_constructor_exists():
    assert callable(aadl2::ClassifierFeature.__init__)


def test_aadl2::classifierfeature_constructor_args():
    sig = inspect.signature(aadl2::ClassifierFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::triggerport_is_not_abstract():
    assert not inspect.isabstract(aadl2::TriggerPort)


def test_aadl2::triggerport_constructor_exists():
    assert callable(aadl2::TriggerPort.__init__)


def test_aadl2::triggerport_constructor_args():
    sig = inspect.signature(aadl2::TriggerPort.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(aadl2::EnumerationLiteral)


def test_aadl2::enumerationliteral_constructor_exists():
    assert callable(aadl2::EnumerationLiteral.__init__)


def test_aadl2::enumerationliteral_constructor_args():
    sig = inspect.signature(aadl2::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::context_is_not_abstract():
    assert not inspect.isabstract(aadl2::Context)


def test_aadl2::context_constructor_exists():
    assert callable(aadl2::Context.__init__)


def test_aadl2::context_constructor_args():
    sig = inspect.signature(aadl2::Context.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::endtoendflowelement_is_not_abstract():
    assert not inspect.isabstract(aadl2::EndToEndFlowElement)


def test_aadl2::endtoendflowelement_constructor_exists():
    assert callable(aadl2::EndToEndFlowElement.__init__)


def test_aadl2::endtoendflowelement_constructor_args():
    sig = inspect.signature(aadl2::EndToEndFlowElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::refinableelement_is_not_abstract():
    assert not inspect.isabstract(aadl2::RefinableElement)


def test_aadl2::refinableelement_constructor_exists():
    assert callable(aadl2::RefinableElement.__init__)


def test_aadl2::refinableelement_constructor_args():
    sig = inspect.signature(aadl2::RefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::modalelement_is_not_abstract():
    assert not inspect.isabstract(aadl2::ModalElement)


def test_aadl2::modalelement_constructor_exists():
    assert callable(aadl2::ModalElement.__init__)


def test_aadl2::modalelement_constructor_args():
    sig = inspect.signature(aadl2::ModalElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::flow_is_not_abstract():
    assert not inspect.isabstract(aadl2::Flow)


def test_aadl2::flow_constructor_exists():
    assert callable(aadl2::Flow.__init__)


def test_aadl2::flow_constructor_args():
    sig = inspect.signature(aadl2::Flow.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::type_is_not_abstract():
    assert not inspect.isabstract(aadl2::Type)


def test_aadl2::type_constructor_exists():
    assert callable(aadl2::Type.__init__)


def test_aadl2::type_constructor_args():
    sig = inspect.signature(aadl2::Type.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::property_is_not_abstract():
    assert not inspect.isabstract(aadl2::Property)


def test_aadl2::property_constructor_exists():
    assert callable(aadl2::Property.__init__)


def test_aadl2::property_constructor_args():
    sig = inspect.signature(aadl2::Property.__init__)
    params = list(sig.parameters.keys())
    assert "emptyListDefault" in params, "Missing parameter 'emptyListDefault'"
    assert "inherit" in params, "Missing parameter 'inherit'"

def test_aadl2::property_has_emptyListDefault():
    assert hasattr(aadl2::Property, "emptyListDefault")
    descriptor = None
    for klass in aadl2::Property.__mro__:
        if "emptyListDefault" in klass.__dict__:
            descriptor = klass.__dict__["emptyListDefault"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::property_has_inherit():
    assert hasattr(aadl2::Property, "inherit")
    descriptor = None
    for klass in aadl2::Property.__mro__:
        if "inherit" in klass.__dict__:
            descriptor = klass.__dict__["inherit"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::containednamedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2::ContainedNamedElement)


def test_aadl2::containednamedelement_constructor_exists():
    assert callable(aadl2::ContainedNamedElement.__init__)


def test_aadl2::containednamedelement_constructor_args():
    sig = inspect.signature(aadl2::ContainedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::propertyassociation_is_not_abstract():
    assert not inspect.isabstract(aadl2::PropertyAssociation)


def test_aadl2::propertyassociation_constructor_exists():
    assert callable(aadl2::PropertyAssociation.__init__)


def test_aadl2::propertyassociation_constructor_args():
    sig = inspect.signature(aadl2::PropertyAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "append" in params, "Missing parameter 'append'"

def test_aadl2::propertyassociation_has_constant():
    assert hasattr(aadl2::PropertyAssociation, "constant")
    descriptor = None
    for klass in aadl2::PropertyAssociation.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::propertyassociation_has_append():
    assert hasattr(aadl2::PropertyAssociation, "append")
    descriptor = None
    for klass in aadl2::PropertyAssociation.__mro__:
        if "append" in klass.__dict__:
            descriptor = klass.__dict__["append"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::propertyexpression_is_not_abstract():
    assert not inspect.isabstract(aadl2::PropertyExpression)


def test_aadl2::propertyexpression_constructor_exists():
    assert callable(aadl2::PropertyExpression.__init__)


def test_aadl2::propertyexpression_constructor_args():
    sig = inspect.signature(aadl2::PropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::arraysize_is_not_abstract():
    assert not inspect.isabstract(aadl2::ArraySize)


def test_aadl2::arraysize_constructor_exists():
    assert callable(aadl2::ArraySize.__init__)


def test_aadl2::arraysize_constructor_args():
    sig = inspect.signature(aadl2::ArraySize.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_aadl2::arraysize_has_size():
    assert hasattr(aadl2::ArraySize, "size")
    descriptor = None
    for klass in aadl2::ArraySize.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::numericrange_is_not_abstract():
    assert not inspect.isabstract(aadl2::NumericRange)


def test_aadl2::numericrange_constructor_exists():
    assert callable(aadl2::NumericRange.__init__)


def test_aadl2::numericrange_constructor_args():
    sig = inspect.signature(aadl2::NumericRange.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::relationship_is_not_abstract():
    assert not inspect.isabstract(aadl2::Relationship)


def test_aadl2::relationship_constructor_exists():
    assert callable(aadl2::Relationship.__init__)


def test_aadl2::relationship_constructor_args():
    sig = inspect.signature(aadl2::Relationship.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::propertyowner_is_not_abstract():
    assert not inspect.isabstract(aadl2::PropertyOwner)


def test_aadl2::propertyowner_constructor_exists():
    assert callable(aadl2::PropertyOwner.__init__)


def test_aadl2::propertyowner_constructor_args():
    sig = inspect.signature(aadl2::PropertyOwner.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::prototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2::PrototypeBinding)


def test_aadl2::prototypebinding_constructor_exists():
    assert callable(aadl2::PrototypeBinding.__init__)


def test_aadl2::prototypebinding_constructor_args():
    sig = inspect.signature(aadl2::PrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::containmentpathelement_is_not_abstract():
    assert not inspect.isabstract(aadl2::ContainmentPathElement)


def test_aadl2::containmentpathelement_constructor_exists():
    assert callable(aadl2::ContainmentPathElement.__init__)


def test_aadl2::containmentpathelement_constructor_args():
    sig = inspect.signature(aadl2::ContainmentPathElement.__init__)
    params = list(sig.parameters.keys())
    assert "annexName" in params, "Missing parameter 'annexName'"

def test_aadl2::containmentpathelement_has_annexName():
    assert hasattr(aadl2::ContainmentPathElement, "annexName")
    descriptor = None
    for klass in aadl2::ContainmentPathElement.__mro__:
        if "annexName" in klass.__dict__:
            descriptor = klass.__dict__["annexName"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::modetransitiontrigger_is_not_abstract():
    assert not inspect.isabstract(aadl2::ModeTransitionTrigger)


def test_aadl2::modetransitiontrigger_constructor_exists():
    assert callable(aadl2::ModeTransitionTrigger.__init__)


def test_aadl2::modetransitiontrigger_constructor_args():
    sig = inspect.signature(aadl2::ModeTransitionTrigger.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::arraydimension_is_not_abstract():
    assert not inspect.isabstract(aadl2::ArrayDimension)


def test_aadl2::arraydimension_constructor_exists():
    assert callable(aadl2::ArrayDimension.__init__)


def test_aadl2::arraydimension_constructor_args():
    sig = inspect.signature(aadl2::ArrayDimension.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::basicpropertyassociation_is_not_abstract():
    assert not inspect.isabstract(aadl2::BasicPropertyAssociation)


def test_aadl2::basicpropertyassociation_constructor_exists():
    assert callable(aadl2::BasicPropertyAssociation.__init__)


def test_aadl2::basicpropertyassociation_constructor_args():
    sig = inspect.signature(aadl2::BasicPropertyAssociation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::arrayableelement_is_not_abstract():
    assert not inspect.isabstract(aadl2::ArrayableElement)


def test_aadl2::arrayableelement_constructor_exists():
    assert callable(aadl2::ArrayableElement.__init__)


def test_aadl2::arrayableelement_constructor_args():
    sig = inspect.signature(aadl2::ArrayableElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::flowend_is_not_abstract():
    assert not inspect.isabstract(aadl2::FlowEnd)


def test_aadl2::flowend_constructor_exists():
    assert callable(aadl2::FlowEnd.__init__)


def test_aadl2::flowend_constructor_args():
    sig = inspect.signature(aadl2::FlowEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::arrayrange_is_not_abstract():
    assert not inspect.isabstract(aadl2::ArrayRange)


def test_aadl2::arrayrange_constructor_exists():
    assert callable(aadl2::ArrayRange.__init__)


def test_aadl2::arrayrange_constructor_args():
    sig = inspect.signature(aadl2::ArrayRange.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_aadl2::arrayrange_has_lowerBound():
    assert hasattr(aadl2::ArrayRange, "lowerBound")
    descriptor = None
    for klass in aadl2::ArrayRange.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::arrayrange_has_upperBound():
    assert hasattr(aadl2::ArrayRange, "upperBound")
    descriptor = None
    for klass in aadl2::ArrayRange.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::namedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2::NamedElement)


def test_aadl2::namedelement_constructor_exists():
    assert callable(aadl2::NamedElement.__init__)


def test_aadl2::namedelement_constructor_args():
    sig = inspect.signature(aadl2::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"

def test_aadl2::namedelement_has_name():
    assert hasattr(aadl2::NamedElement, "name")
    descriptor = None
    for klass in aadl2::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::namedelement_has_qualifiedName():
    assert hasattr(aadl2::NamedElement, "qualifiedName")
    descriptor = None
    for klass in aadl2::NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::componentimplementationreference_is_not_abstract():
    assert not inspect.isabstract(aadl2::ComponentImplementationReference)


def test_aadl2::componentimplementationreference_constructor_exists():
    assert callable(aadl2::ComponentImplementationReference.__init__)


def test_aadl2::componentimplementationreference_constructor_args():
    sig = inspect.signature(aadl2::ComponentImplementationReference.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::comment_is_not_abstract():
    assert not inspect.isabstract(aadl2::Comment)


def test_aadl2::comment_constructor_exists():
    assert callable(aadl2::Comment.__init__)


def test_aadl2::comment_constructor_args():
    sig = inspect.signature(aadl2::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_aadl2::comment_has_body():
    assert hasattr(aadl2::Comment, "body")
    descriptor = None
    for klass in aadl2::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::element_is_not_abstract():
    assert not inspect.isabstract(aadl2::Element)


def test_aadl2::element_constructor_exists():
    assert callable(aadl2::Element.__init__)


def test_aadl2::element_constructor_args():
    sig = inspect.signature(aadl2::Element.__init__)
    params = list(sig.parameters.keys())



def test_deviceclassifier_is_not_abstract():
    assert not inspect.isabstract(DeviceClassifier)


def test_deviceclassifier_constructor_exists():
    assert callable(DeviceClassifier.__init__)


def test_deviceclassifier_constructor_args():
    sig = inspect.signature(DeviceClassifier.__init__)
    params = list(sig.parameters.keys())



def test_dataclassifier_is_not_abstract():
    assert not inspect.isabstract(DataClassifier)


def test_dataclassifier_constructor_exists():
    assert callable(DataClassifier.__init__)


def test_dataclassifier_constructor_args():
    sig = inspect.signature(DataClassifier.__init__)
    params = list(sig.parameters.keys())



def test_componentprototype_is_not_abstract():
    assert not inspect.isabstract(ComponentPrototype)


def test_componentprototype_constructor_exists():
    assert callable(ComponentPrototype.__init__)


def test_componentprototype_constructor_args():
    sig = inspect.signature(ComponentPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualprocessor_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualProcessor)


def test_aadl2::virtualprocessor_constructor_exists():
    assert callable(aadl2::VirtualProcessor.__init__)


def test_aadl2::virtualprocessor_constructor_args():
    sig = inspect.signature(aadl2::VirtualProcessor.__init__)
    params = list(sig.parameters.keys())



def test_busclassifier_is_not_abstract():
    assert not inspect.isabstract(BusClassifier)


def test_busclassifier_constructor_exists():
    assert callable(BusClassifier.__init__)


def test_busclassifier_constructor_args():
    sig = inspect.signature(BusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_thread_is_not_abstract():
    assert not inspect.isabstract(Thread)


def test_thread_constructor_exists():
    assert callable(Thread.__init__)


def test_thread_constructor_args():
    sig = inspect.signature(Thread.__init__)
    params = list(sig.parameters.keys())



def test_virtualprocessor_is_not_abstract():
    assert not inspect.isabstract(VirtualProcessor)


def test_virtualprocessor_constructor_exists():
    assert callable(VirtualProcessor.__init__)


def test_virtualprocessor_constructor_args():
    sig = inspect.signature(VirtualProcessor.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualbus_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualBus)


def test_aadl2::virtualbus_constructor_exists():
    assert callable(aadl2::VirtualBus.__init__)


def test_aadl2::virtualbus_constructor_args():
    sig = inspect.signature(aadl2::VirtualBus.__init__)
    params = list(sig.parameters.keys())



def test_virtualbus_is_not_abstract():
    assert not inspect.isabstract(VirtualBus)


def test_virtualbus_constructor_exists():
    assert callable(VirtualBus.__init__)


def test_virtualbus_constructor_args():
    sig = inspect.signature(VirtualBus.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadgroup_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadGroup)


def test_aadl2::threadgroup_constructor_exists():
    assert callable(aadl2::ThreadGroup.__init__)


def test_aadl2::threadgroup_constructor_args():
    sig = inspect.signature(aadl2::ThreadGroup.__init__)
    params = list(sig.parameters.keys())



def test_threadgroup_is_not_abstract():
    assert not inspect.isabstract(ThreadGroup)


def test_threadgroup_constructor_exists():
    assert callable(ThreadGroup.__init__)


def test_threadgroup_constructor_args():
    sig = inspect.signature(ThreadGroup.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::thread_is_not_abstract():
    assert not inspect.isabstract(aadl2::Thread)


def test_aadl2::thread_constructor_exists():
    assert callable(aadl2::Thread.__init__)


def test_aadl2::thread_constructor_args():
    sig = inspect.signature(aadl2::Thread.__init__)
    params = list(sig.parameters.keys())



def test_processor_is_not_abstract():
    assert not inspect.isabstract(Processor)


def test_processor_constructor_exists():
    assert callable(Processor.__init__)


def test_processor_constructor_args():
    sig = inspect.signature(Processor.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::process_is_not_abstract():
    assert not inspect.isabstract(aadl2::Process)


def test_aadl2::process_constructor_exists():
    assert callable(aadl2::Process.__init__)


def test_aadl2::process_constructor_args():
    sig = inspect.signature(aadl2::Process.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramgroup_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramGroup)


def test_aadl2::subprogramgroup_constructor_exists():
    assert callable(aadl2::SubprogramGroup.__init__)


def test_aadl2::subprogramgroup_constructor_args():
    sig = inspect.signature(aadl2::SubprogramGroup.__init__)
    params = list(sig.parameters.keys())



def test_subprogramgroup_is_not_abstract():
    assert not inspect.isabstract(SubprogramGroup)


def test_subprogramgroup_constructor_exists():
    assert callable(SubprogramGroup.__init__)


def test_subprogramgroup_constructor_args():
    sig = inspect.signature(SubprogramGroup.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::system_is_not_abstract():
    assert not inspect.isabstract(aadl2::System)


def test_aadl2::system_constructor_exists():
    assert callable(aadl2::System.__init__)


def test_aadl2::system_constructor_args():
    sig = inspect.signature(aadl2::System.__init__)
    params = list(sig.parameters.keys())



def test_system_is_not_abstract():
    assert not inspect.isabstract(System)


def test_system_constructor_exists():
    assert callable(System.__init__)


def test_system_constructor_args():
    sig = inspect.signature(System.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processor_is_not_abstract():
    assert not inspect.isabstract(aadl2::Processor)


def test_aadl2::processor_constructor_exists():
    assert callable(aadl2::Processor.__init__)


def test_aadl2::processor_constructor_args():
    sig = inspect.signature(aadl2::Processor.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::bus_is_not_abstract():
    assert not inspect.isabstract(aadl2::Bus)


def test_aadl2::bus_constructor_exists():
    assert callable(aadl2::Bus.__init__)


def test_aadl2::bus_constructor_args():
    sig = inspect.signature(aadl2::Bus.__init__)
    params = list(sig.parameters.keys())



def test_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_process_constructor_exists():
    assert callable(Process.__init__)


def test_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::memory_is_not_abstract():
    assert not inspect.isabstract(aadl2::Memory)


def test_aadl2::memory_constructor_exists():
    assert callable(aadl2::Memory.__init__)


def test_aadl2::memory_constructor_args():
    sig = inspect.signature(aadl2::Memory.__init__)
    params = list(sig.parameters.keys())



def test_memory_is_not_abstract():
    assert not inspect.isabstract(Memory)


def test_memory_constructor_exists():
    assert callable(Memory.__init__)


def test_memory_constructor_args():
    sig = inspect.signature(Memory.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::device_is_not_abstract():
    assert not inspect.isabstract(aadl2::Device)


def test_aadl2::device_constructor_exists():
    assert callable(aadl2::Device.__init__)


def test_aadl2::device_constructor_args():
    sig = inspect.signature(aadl2::Device.__init__)
    params = list(sig.parameters.keys())



def test_device_is_not_abstract():
    assert not inspect.isabstract(Device)


def test_device_constructor_exists():
    assert callable(Device.__init__)


def test_device_constructor_args():
    sig = inspect.signature(Device.__init__)
    params = list(sig.parameters.keys())



def test_bus_is_not_abstract():
    assert not inspect.isabstract(Bus)


def test_bus_constructor_exists():
    assert callable(Bus.__init__)


def test_bus_constructor_args():
    sig = inspect.signature(Bus.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processorsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessorSubcomponentType)


def test_aadl2::processorsubcomponenttype_constructor_exists():
    assert callable(aadl2::ProcessorSubcomponentType.__init__)


def test_aadl2::processorsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::ProcessorSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_behavioredimplementation_is_not_abstract():
    assert not inspect.isabstract(BehavioredImplementation)


def test_behavioredimplementation_constructor_exists():
    assert callable(BehavioredImplementation.__init__)


def test_behavioredimplementation_constructor_args():
    sig = inspect.signature(BehavioredImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadImplementation)


def test_aadl2::threadimplementation_constructor_exists():
    assert callable(aadl2::ThreadImplementation.__init__)


def test_aadl2::threadimplementation_constructor_args():
    sig = inspect.signature(aadl2::ThreadImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramImplementation)


def test_aadl2::subprogramimplementation_constructor_exists():
    assert callable(aadl2::SubprogramImplementation.__init__)


def test_aadl2::subprogramimplementation_constructor_args():
    sig = inspect.signature(aadl2::SubprogramImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::devicesubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::DeviceSubcomponentType)


def test_aadl2::devicesubcomponenttype_constructor_exists():
    assert callable(aadl2::DeviceSubcomponentType.__init__)


def test_aadl2::devicesubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::DeviceSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::memorysubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::MemorySubcomponentType)


def test_aadl2::memorysubcomponenttype_constructor_exists():
    assert callable(aadl2::MemorySubcomponentType.__init__)


def test_aadl2::memorysubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::MemorySubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessSubcomponentType)


def test_aadl2::processsubcomponenttype_constructor_exists():
    assert callable(aadl2::ProcessSubcomponentType.__init__)


def test_aadl2::processsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::ProcessSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::systemsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::SystemSubcomponentType)


def test_aadl2::systemsubcomponenttype_constructor_exists():
    assert callable(aadl2::SystemSubcomponentType.__init__)


def test_aadl2::systemsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::SystemSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadSubcomponentType)


def test_aadl2::threadsubcomponenttype_constructor_exists():
    assert callable(aadl2::ThreadSubcomponentType.__init__)


def test_aadl2::threadsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::ThreadSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadgroupsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadGroupSubcomponentType)


def test_aadl2::threadgroupsubcomponenttype_constructor_exists():
    assert callable(aadl2::ThreadGroupSubcomponentType.__init__)


def test_aadl2::threadgroupsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::ThreadGroupSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_busfeatureclassifier_is_not_abstract():
    assert not inspect.isabstract(BusFeatureClassifier)


def test_busfeatureclassifier_constructor_exists():
    assert callable(BusFeatureClassifier.__init__)


def test_busfeatureclassifier_constructor_args():
    sig = inspect.signature(BusFeatureClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualprocessorsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualProcessorSubcomponentType)


def test_aadl2::virtualprocessorsubcomponenttype_constructor_exists():
    assert callable(aadl2::VirtualProcessorSubcomponentType.__init__)


def test_aadl2::virtualprocessorsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::VirtualProcessorSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_virtualprocessorsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(VirtualProcessorSubcomponentType)


def test_virtualprocessorsubcomponenttype_constructor_exists():
    assert callable(VirtualProcessorSubcomponentType.__init__)


def test_virtualprocessorsubcomponenttype_constructor_args():
    sig = inspect.signature(VirtualProcessorSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualprocessorclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualProcessorClassifier)


def test_aadl2::virtualprocessorclassifier_constructor_exists():
    assert callable(aadl2::VirtualProcessorClassifier.__init__)


def test_aadl2::virtualprocessorclassifier_constructor_args():
    sig = inspect.signature(aadl2::VirtualProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualprocessorprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualProcessorPrototype)


def test_aadl2::virtualprocessorprototype_constructor_exists():
    assert callable(aadl2::VirtualProcessorPrototype.__init__)


def test_aadl2::virtualprocessorprototype_constructor_args():
    sig = inspect.signature(aadl2::VirtualProcessorPrototype.__init__)
    params = list(sig.parameters.keys())



def test_virtualbussubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(VirtualBusSubcomponentType)


def test_virtualbussubcomponenttype_constructor_exists():
    assert callable(VirtualBusSubcomponentType.__init__)


def test_virtualbussubcomponenttype_constructor_args():
    sig = inspect.signature(VirtualBusSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualbusprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualBusPrototype)


def test_aadl2::virtualbusprototype_constructor_exists():
    assert callable(aadl2::VirtualBusPrototype.__init__)


def test_aadl2::virtualbusprototype_constructor_args():
    sig = inspect.signature(aadl2::VirtualBusPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualbusclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualBusClassifier)


def test_aadl2::virtualbusclassifier_constructor_exists():
    assert callable(aadl2::VirtualBusClassifier.__init__)


def test_aadl2::virtualbusclassifier_constructor_args():
    sig = inspect.signature(aadl2::VirtualBusClassifier.__init__)
    params = list(sig.parameters.keys())



def test_threadsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ThreadSubcomponentType)


def test_threadsubcomponenttype_constructor_exists():
    assert callable(ThreadSubcomponentType.__init__)


def test_threadsubcomponenttype_constructor_args():
    sig = inspect.signature(ThreadSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadPrototype)


def test_aadl2::threadprototype_constructor_exists():
    assert callable(aadl2::ThreadPrototype.__init__)


def test_aadl2::threadprototype_constructor_args():
    sig = inspect.signature(aadl2::ThreadPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadClassifier)


def test_aadl2::threadclassifier_constructor_exists():
    assert callable(aadl2::ThreadClassifier.__init__)


def test_aadl2::threadclassifier_constructor_args():
    sig = inspect.signature(aadl2::ThreadClassifier.__init__)
    params = list(sig.parameters.keys())



def test_threadgroupsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ThreadGroupSubcomponentType)


def test_threadgroupsubcomponenttype_constructor_exists():
    assert callable(ThreadGroupSubcomponentType.__init__)


def test_threadgroupsubcomponenttype_constructor_args():
    sig = inspect.signature(ThreadGroupSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadgroupprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadGroupPrototype)


def test_aadl2::threadgroupprototype_constructor_exists():
    assert callable(aadl2::ThreadGroupPrototype.__init__)


def test_aadl2::threadgroupprototype_constructor_args():
    sig = inspect.signature(aadl2::ThreadGroupPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadGroupClassifier)


def test_aadl2::threadgroupclassifier_constructor_exists():
    assert callable(aadl2::ThreadGroupClassifier.__init__)


def test_aadl2::threadgroupclassifier_constructor_args():
    sig = inspect.signature(aadl2::ThreadGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_systemsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(SystemSubcomponentType)


def test_systemsubcomponenttype_constructor_exists():
    assert callable(SystemSubcomponentType.__init__)


def test_systemsubcomponenttype_constructor_args():
    sig = inspect.signature(SystemSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::systemprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::SystemPrototype)


def test_aadl2::systemprototype_constructor_exists():
    assert callable(aadl2::SystemPrototype.__init__)


def test_aadl2::systemprototype_constructor_args():
    sig = inspect.signature(aadl2::SystemPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::systemclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::SystemClassifier)


def test_aadl2::systemclassifier_constructor_exists():
    assert callable(aadl2::SystemClassifier.__init__)


def test_aadl2::systemclassifier_constructor_args():
    sig = inspect.signature(aadl2::SystemClassifier.__init__)
    params = list(sig.parameters.keys())



def test_subprogramgroupsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(SubprogramGroupSubcomponentType)


def test_subprogramgroupsubcomponenttype_constructor_exists():
    assert callable(SubprogramGroupSubcomponentType.__init__)


def test_subprogramgroupsubcomponenttype_constructor_args():
    sig = inspect.signature(SubprogramGroupSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramgroupclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramGroupClassifier)


def test_aadl2::subprogramgroupclassifier_constructor_exists():
    assert callable(aadl2::SubprogramGroupClassifier.__init__)


def test_aadl2::subprogramgroupclassifier_constructor_args():
    sig = inspect.signature(aadl2::SubprogramGroupClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramgroupprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramGroupPrototype)


def test_aadl2::subprogramgroupprototype_constructor_exists():
    assert callable(aadl2::SubprogramGroupPrototype.__init__)


def test_aadl2::subprogramgroupprototype_constructor_args():
    sig = inspect.signature(aadl2::SubprogramGroupPrototype.__init__)
    params = list(sig.parameters.keys())



def test_processsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ProcessSubcomponentType)


def test_processsubcomponenttype_constructor_exists():
    assert callable(ProcessSubcomponentType.__init__)


def test_processsubcomponenttype_constructor_args():
    sig = inspect.signature(ProcessSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessPrototype)


def test_aadl2::processprototype_constructor_exists():
    assert callable(aadl2::ProcessPrototype.__init__)


def test_aadl2::processprototype_constructor_args():
    sig = inspect.signature(aadl2::ProcessPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessClassifier)


def test_aadl2::processclassifier_constructor_exists():
    assert callable(aadl2::ProcessClassifier.__init__)


def test_aadl2::processclassifier_constructor_args():
    sig = inspect.signature(aadl2::ProcessClassifier.__init__)
    params = list(sig.parameters.keys())



def test_processorsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(ProcessorSubcomponentType)


def test_processorsubcomponenttype_constructor_exists():
    assert callable(ProcessorSubcomponentType.__init__)


def test_processorsubcomponenttype_constructor_args():
    sig = inspect.signature(ProcessorSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processorclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessorClassifier)


def test_aadl2::processorclassifier_constructor_exists():
    assert callable(aadl2::ProcessorClassifier.__init__)


def test_aadl2::processorclassifier_constructor_args():
    sig = inspect.signature(aadl2::ProcessorClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processorprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessorPrototype)


def test_aadl2::processorprototype_constructor_exists():
    assert callable(aadl2::ProcessorPrototype.__init__)


def test_aadl2::processorprototype_constructor_args():
    sig = inspect.signature(aadl2::ProcessorPrototype.__init__)
    params = list(sig.parameters.keys())



def test_memorysubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(MemorySubcomponentType)


def test_memorysubcomponenttype_constructor_exists():
    assert callable(MemorySubcomponentType.__init__)


def test_memorysubcomponenttype_constructor_args():
    sig = inspect.signature(MemorySubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::memoryclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::MemoryClassifier)


def test_aadl2::memoryclassifier_constructor_exists():
    assert callable(aadl2::MemoryClassifier.__init__)


def test_aadl2::memoryclassifier_constructor_args():
    sig = inspect.signature(aadl2::MemoryClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::memoryprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::MemoryPrototype)


def test_aadl2::memoryprototype_constructor_exists():
    assert callable(aadl2::MemoryPrototype.__init__)


def test_aadl2::memoryprototype_constructor_args():
    sig = inspect.signature(aadl2::MemoryPrototype.__init__)
    params = list(sig.parameters.keys())



def test_devicesubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(DeviceSubcomponentType)


def test_devicesubcomponenttype_constructor_exists():
    assert callable(DeviceSubcomponentType.__init__)


def test_devicesubcomponenttype_constructor_args():
    sig = inspect.signature(DeviceSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::deviceclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::DeviceClassifier)


def test_aadl2::deviceclassifier_constructor_exists():
    assert callable(aadl2::DeviceClassifier.__init__)


def test_aadl2::deviceclassifier_constructor_args():
    sig = inspect.signature(aadl2::DeviceClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::deviceprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::DevicePrototype)


def test_aadl2::deviceprototype_constructor_exists():
    assert callable(aadl2::DevicePrototype.__init__)


def test_aadl2::deviceprototype_constructor_args():
    sig = inspect.signature(aadl2::DevicePrototype.__init__)
    params = list(sig.parameters.keys())



def test_bussubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(BusSubcomponentType)


def test_bussubcomponenttype_constructor_exists():
    assert callable(BusSubcomponentType.__init__)


def test_bussubcomponenttype_constructor_args():
    sig = inspect.signature(BusSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::busprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::BusPrototype)


def test_aadl2::busprototype_constructor_exists():
    assert callable(aadl2::BusPrototype.__init__)


def test_aadl2::busprototype_constructor_args():
    sig = inspect.signature(aadl2::BusPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::busclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::BusClassifier)


def test_aadl2::busclassifier_constructor_exists():
    assert callable(aadl2::BusClassifier.__init__)


def test_aadl2::busclassifier_constructor_args():
    sig = inspect.signature(aadl2::BusClassifier.__init__)
    params = list(sig.parameters.keys())



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



def test_aadl2::abstractimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::AbstractImplementation)


def test_aadl2::abstractimplementation_constructor_exists():
    assert callable(aadl2::AbstractImplementation.__init__)


def test_aadl2::abstractimplementation_constructor_args():
    sig = inspect.signature(aadl2::AbstractImplementation.__init__)
    params = list(sig.parameters.keys())



def test_componenttype_is_not_abstract():
    assert not inspect.isabstract(ComponentType)


def test_componenttype_constructor_exists():
    assert callable(ComponentType.__init__)


def test_componenttype_constructor_args():
    sig = inspect.signature(ComponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::memorytype_is_not_abstract():
    assert not inspect.isabstract(aadl2::MemoryType)


def test_aadl2::memorytype_constructor_exists():
    assert callable(aadl2::MemoryType.__init__)


def test_aadl2::memorytype_constructor_args():
    sig = inspect.signature(aadl2::MemoryType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadgrouptype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadGroupType)


def test_aadl2::threadgrouptype_constructor_exists():
    assert callable(aadl2::ThreadGroupType.__init__)


def test_aadl2::threadgrouptype_constructor_args():
    sig = inspect.signature(aadl2::ThreadGroupType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualprocessortype_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualProcessorType)


def test_aadl2::virtualprocessortype_constructor_exists():
    assert callable(aadl2::VirtualProcessorType.__init__)


def test_aadl2::virtualprocessortype_constructor_args():
    sig = inspect.signature(aadl2::VirtualProcessorType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::bustype_is_not_abstract():
    assert not inspect.isabstract(aadl2::BusType)


def test_aadl2::bustype_constructor_exists():
    assert callable(aadl2::BusType.__init__)


def test_aadl2::bustype_constructor_args():
    sig = inspect.signature(aadl2::BusType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::datatype_is_not_abstract():
    assert not inspect.isabstract(aadl2::DataType)


def test_aadl2::datatype_constructor_exists():
    assert callable(aadl2::DataType.__init__)


def test_aadl2::datatype_constructor_args():
    sig = inspect.signature(aadl2::DataType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processtype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessType)


def test_aadl2::processtype_constructor_exists():
    assert callable(aadl2::ProcessType.__init__)


def test_aadl2::processtype_constructor_args():
    sig = inspect.signature(aadl2::ProcessType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramtype_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramType)


def test_aadl2::subprogramtype_constructor_exists():
    assert callable(aadl2::SubprogramType.__init__)


def test_aadl2::subprogramtype_constructor_args():
    sig = inspect.signature(aadl2::SubprogramType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadtype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadType)


def test_aadl2::threadtype_constructor_exists():
    assert callable(aadl2::ThreadType.__init__)


def test_aadl2::threadtype_constructor_args():
    sig = inspect.signature(aadl2::ThreadType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::devicetype_is_not_abstract():
    assert not inspect.isabstract(aadl2::DeviceType)


def test_aadl2::devicetype_constructor_exists():
    assert callable(aadl2::DeviceType.__init__)


def test_aadl2::devicetype_constructor_args():
    sig = inspect.signature(aadl2::DeviceType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualbustype_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualBusType)


def test_aadl2::virtualbustype_constructor_exists():
    assert callable(aadl2::VirtualBusType.__init__)


def test_aadl2::virtualbustype_constructor_args():
    sig = inspect.signature(aadl2::VirtualBusType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processortype_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessorType)


def test_aadl2::processortype_constructor_exists():
    assert callable(aadl2::ProcessorType.__init__)


def test_aadl2::processortype_constructor_args():
    sig = inspect.signature(aadl2::ProcessorType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::systemtype_is_not_abstract():
    assert not inspect.isabstract(aadl2::SystemType)


def test_aadl2::systemtype_constructor_exists():
    assert callable(aadl2::SystemType.__init__)


def test_aadl2::systemtype_constructor_args():
    sig = inspect.signature(aadl2::SystemType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramgrouptype_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramGroupType)


def test_aadl2::subprogramgrouptype_constructor_exists():
    assert callable(aadl2::SubprogramGroupType.__init__)


def test_aadl2::subprogramgrouptype_constructor_args():
    sig = inspect.signature(aadl2::SubprogramGroupType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::abstracttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::AbstractType)


def test_aadl2::abstracttype_constructor_exists():
    assert callable(aadl2::AbstractType.__init__)


def test_aadl2::abstracttype_constructor_args():
    sig = inspect.signature(aadl2::AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_componentimplementation_is_not_abstract():
    assert not inspect.isabstract(ComponentImplementation)


def test_componentimplementation_constructor_exists():
    assert callable(ComponentImplementation.__init__)


def test_componentimplementation_constructor_args():
    sig = inspect.signature(ComponentImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processorimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessorImplementation)


def test_aadl2::processorimplementation_constructor_exists():
    assert callable(aadl2::ProcessorImplementation.__init__)


def test_aadl2::processorimplementation_constructor_args():
    sig = inspect.signature(aadl2::ProcessorImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::systemimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::SystemImplementation)


def test_aadl2::systemimplementation_constructor_exists():
    assert callable(aadl2::SystemImplementation.__init__)


def test_aadl2::systemimplementation_constructor_args():
    sig = inspect.signature(aadl2::SystemImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::busimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::BusImplementation)


def test_aadl2::busimplementation_constructor_exists():
    assert callable(aadl2::BusImplementation.__init__)


def test_aadl2::busimplementation_constructor_args():
    sig = inspect.signature(aadl2::BusImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::dataimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::DataImplementation)


def test_aadl2::dataimplementation_constructor_exists():
    assert callable(aadl2::DataImplementation.__init__)


def test_aadl2::dataimplementation_constructor_args():
    sig = inspect.signature(aadl2::DataImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::memoryimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::MemoryImplementation)


def test_aadl2::memoryimplementation_constructor_exists():
    assert callable(aadl2::MemoryImplementation.__init__)


def test_aadl2::memoryimplementation_constructor_args():
    sig = inspect.signature(aadl2::MemoryImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualprocessorimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualProcessorImplementation)


def test_aadl2::virtualprocessorimplementation_constructor_exists():
    assert callable(aadl2::VirtualProcessorImplementation.__init__)


def test_aadl2::virtualprocessorimplementation_constructor_args():
    sig = inspect.signature(aadl2::VirtualProcessorImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualbusimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualBusImplementation)


def test_aadl2::virtualbusimplementation_constructor_exists():
    assert callable(aadl2::VirtualBusImplementation.__init__)


def test_aadl2::virtualbusimplementation_constructor_args():
    sig = inspect.signature(aadl2::VirtualBusImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadgroupimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadGroupImplementation)


def test_aadl2::threadgroupimplementation_constructor_exists():
    assert callable(aadl2::ThreadGroupImplementation.__init__)


def test_aadl2::threadgroupimplementation_constructor_args():
    sig = inspect.signature(aadl2::ThreadGroupImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramgroupimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramGroupImplementation)


def test_aadl2::subprogramgroupimplementation_constructor_exists():
    assert callable(aadl2::SubprogramGroupImplementation.__init__)


def test_aadl2::subprogramgroupimplementation_constructor_args():
    sig = inspect.signature(aadl2::SubprogramGroupImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessImplementation)


def test_aadl2::processimplementation_constructor_exists():
    assert callable(aadl2::ProcessImplementation.__init__)


def test_aadl2::processimplementation_constructor_args():
    sig = inspect.signature(aadl2::ProcessImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::deviceimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::DeviceImplementation)


def test_aadl2::deviceimplementation_constructor_exists():
    assert callable(aadl2::DeviceImplementation.__init__)


def test_aadl2::deviceimplementation_constructor_args():
    sig = inspect.signature(aadl2::DeviceImplementation.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::behavioredimplementation_is_not_abstract():
    assert not inspect.isabstract(aadl2::BehavioredImplementation)


def test_aadl2::behavioredimplementation_constructor_exists():
    assert callable(aadl2::BehavioredImplementation.__init__)


def test_aadl2::behavioredimplementation_constructor_args():
    sig = inspect.signature(aadl2::BehavioredImplementation.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramcall_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramCall)


def test_aadl2::subprogramcall_constructor_exists():
    assert callable(aadl2::SubprogramCall.__init__)


def test_aadl2::subprogramcall_constructor_args():
    sig = inspect.signature(aadl2::SubprogramCall.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramcallsequence_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramCallSequence)


def test_aadl2::subprogramcallsequence_constructor_exists():
    assert callable(aadl2::SubprogramCallSequence.__init__)


def test_aadl2::subprogramcallsequence_constructor_args():
    sig = inspect.signature(aadl2::SubprogramCallSequence.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featureprototypeactual_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeaturePrototypeActual)


def test_aadl2::featureprototypeactual_constructor_exists():
    assert callable(aadl2::FeaturePrototypeActual.__init__)


def test_aadl2::featureprototypeactual_constructor_args():
    sig = inspect.signature(aadl2::FeaturePrototypeActual.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::componentprototypeactual_is_not_abstract():
    assert not inspect.isabstract(aadl2::ComponentPrototypeActual)


def test_aadl2::componentprototypeactual_constructor_exists():
    assert callable(aadl2::ComponentPrototypeActual.__init__)


def test_aadl2::componentprototypeactual_constructor_args():
    sig = inspect.signature(aadl2::ComponentPrototypeActual.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"

def test_aadl2::componentprototypeactual_has_category():
    assert hasattr(aadl2::ComponentPrototypeActual, "category")
    descriptor = None
    for klass in aadl2::ComponentPrototypeActual.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_prototypebinding_is_not_abstract():
    assert not inspect.isabstract(PrototypeBinding)


def test_prototypebinding_constructor_exists():
    assert callable(PrototypeBinding.__init__)


def test_prototypebinding_constructor_args():
    sig = inspect.signature(PrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featureprototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeaturePrototypeBinding)


def test_aadl2::featureprototypebinding_constructor_exists():
    assert callable(aadl2::FeaturePrototypeBinding.__init__)


def test_aadl2::featureprototypebinding_constructor_args():
    sig = inspect.signature(aadl2::FeaturePrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::componentprototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2::ComponentPrototypeBinding)


def test_aadl2::componentprototypebinding_constructor_exists():
    assert callable(aadl2::ComponentPrototypeBinding.__init__)


def test_aadl2::componentprototypebinding_constructor_args():
    sig = inspect.signature(aadl2::ComponentPrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_featureprototypeactual_is_not_abstract():
    assert not inspect.isabstract(FeaturePrototypeActual)


def test_featureprototypeactual_constructor_exists():
    assert callable(FeaturePrototypeActual.__init__)


def test_featureprototypeactual_constructor_args():
    sig = inspect.signature(FeaturePrototypeActual.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featureprototypereference_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeaturePrototypeReference)


def test_aadl2::featureprototypereference_constructor_exists():
    assert callable(aadl2::FeaturePrototypeReference.__init__)


def test_aadl2::featureprototypereference_constructor_args():
    sig = inspect.signature(aadl2::FeaturePrototypeReference.__init__)
    params = list(sig.parameters.keys())
    assert "out" in params, "Missing parameter 'out'"
    assert "in_" in params, "Missing parameter 'in_'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_aadl2::featureprototypereference_has_out():
    assert hasattr(aadl2::FeaturePrototypeReference, "out")
    descriptor = None
    for klass in aadl2::FeaturePrototypeReference.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::featureprototypereference_has_in_():
    assert hasattr(aadl2::FeaturePrototypeReference, "in_")
    descriptor = None
    for klass in aadl2::FeaturePrototypeReference.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::featureprototypereference_has_direction():
    assert hasattr(aadl2::FeaturePrototypeReference, "direction")
    descriptor = None
    for klass in aadl2::FeaturePrototypeReference.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::accessspecification_is_not_abstract():
    assert not inspect.isabstract(aadl2::AccessSpecification)


def test_aadl2::accessspecification_constructor_exists():
    assert callable(aadl2::AccessSpecification.__init__)


def test_aadl2::accessspecification_constructor_args():
    sig = inspect.signature(aadl2::AccessSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_aadl2::accessspecification_has_category():
    assert hasattr(aadl2::AccessSpecification, "category")
    descriptor = None
    for klass in aadl2::AccessSpecification.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::accessspecification_has_kind():
    assert hasattr(aadl2::AccessSpecification, "kind")
    descriptor = None
    for klass in aadl2::AccessSpecification.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::portspecification_is_not_abstract():
    assert not inspect.isabstract(aadl2::PortSpecification)


def test_aadl2::portspecification_constructor_exists():
    assert callable(aadl2::PortSpecification.__init__)


def test_aadl2::portspecification_constructor_args():
    sig = inspect.signature(aadl2::PortSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "in_" in params, "Missing parameter 'in_'"
    assert "out" in params, "Missing parameter 'out'"

def test_aadl2::portspecification_has_category():
    assert hasattr(aadl2::PortSpecification, "category")
    descriptor = None
    for klass in aadl2::PortSpecification.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::portspecification_has_direction():
    assert hasattr(aadl2::PortSpecification, "direction")
    descriptor = None
    for klass in aadl2::PortSpecification.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::portspecification_has_in_():
    assert hasattr(aadl2::PortSpecification, "in_")
    descriptor = None
    for klass in aadl2::PortSpecification.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::portspecification_has_out():
    assert hasattr(aadl2::PortSpecification, "out")
    descriptor = None
    for klass in aadl2::PortSpecification.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::featuregroupprototypeactual_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeatureGroupPrototypeActual)


def test_aadl2::featuregroupprototypeactual_constructor_exists():
    assert callable(aadl2::FeatureGroupPrototypeActual.__init__)


def test_aadl2::featuregroupprototypeactual_constructor_args():
    sig = inspect.signature(aadl2::FeatureGroupPrototypeActual.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featuregroupprototypebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeatureGroupPrototypeBinding)


def test_aadl2::featuregroupprototypebinding_constructor_exists():
    assert callable(aadl2::FeatureGroupPrototypeBinding.__init__)


def test_aadl2::featuregroupprototypebinding_constructor_args():
    sig = inspect.signature(aadl2::FeatureGroupPrototypeBinding.__init__)
    params = list(sig.parameters.keys())



def test_modelunit_is_not_abstract():
    assert not inspect.isabstract(ModelUnit)


def test_modelunit_constructor_exists():
    assert callable(ModelUnit.__init__)


def test_modelunit_constructor_args():
    sig = inspect.signature(ModelUnit.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::propertyset_is_not_abstract():
    assert not inspect.isabstract(aadl2::PropertySet)


def test_aadl2::propertyset_constructor_exists():
    assert callable(aadl2::PropertySet.__init__)


def test_aadl2::propertyset_constructor_args():
    sig = inspect.signature(aadl2::PropertySet.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::aadlpackage_is_not_abstract():
    assert not inspect.isabstract(aadl2::AadlPackage)


def test_aadl2::aadlpackage_constructor_exists():
    assert callable(aadl2::AadlPackage.__init__)


def test_aadl2::aadlpackage_constructor_args():
    sig = inspect.signature(aadl2::AadlPackage.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::packagerename_is_not_abstract():
    assert not inspect.isabstract(aadl2::PackageRename)


def test_aadl2::packagerename_constructor_exists():
    assert callable(aadl2::PackageRename.__init__)


def test_aadl2::packagerename_constructor_args():
    sig = inspect.signature(aadl2::PackageRename.__init__)
    params = list(sig.parameters.keys())
    assert "renameAll" in params, "Missing parameter 'renameAll'"

def test_aadl2::packagerename_has_renameAll():
    assert hasattr(aadl2::PackageRename, "renameAll")
    descriptor = None
    for klass in aadl2::PackageRename.__mro__:
        if "renameAll" in klass.__dict__:
            descriptor = klass.__dict__["renameAll"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::packagesection_is_not_abstract():
    assert not inspect.isabstract(aadl2::PackageSection)


def test_aadl2::packagesection_constructor_exists():
    assert callable(aadl2::PackageSection.__init__)


def test_aadl2::packagesection_constructor_args():
    sig = inspect.signature(aadl2::PackageSection.__init__)
    params = list(sig.parameters.keys())
    assert "noAnnexes" in params, "Missing parameter 'noAnnexes'"
    assert "noProperties" in params, "Missing parameter 'noProperties'"

def test_aadl2::packagesection_has_noAnnexes():
    assert hasattr(aadl2::PackageSection, "noAnnexes")
    descriptor = None
    for klass in aadl2::PackageSection.__mro__:
        if "noAnnexes" in klass.__dict__:
            descriptor = klass.__dict__["noAnnexes"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::packagesection_has_noProperties():
    assert hasattr(aadl2::PackageSection, "noProperties")
    descriptor = None
    for klass in aadl2::PackageSection.__mro__:
        if "noProperties" in klass.__dict__:
            descriptor = klass.__dict__["noProperties"]
            break
    assert isinstance(descriptor, property)



def test_packagesection_is_not_abstract():
    assert not inspect.isabstract(PackageSection)


def test_packagesection_constructor_exists():
    assert callable(PackageSection.__init__)


def test_packagesection_constructor_args():
    sig = inspect.signature(PackageSection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::privatepackagesection_is_not_abstract():
    assert not inspect.isabstract(aadl2::PrivatePackageSection)


def test_aadl2::privatepackagesection_constructor_exists():
    assert callable(aadl2::PrivatePackageSection.__init__)


def test_aadl2::privatepackagesection_constructor_args():
    sig = inspect.signature(aadl2::PrivatePackageSection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::publicpackagesection_is_not_abstract():
    assert not inspect.isabstract(aadl2::PublicPackageSection)


def test_aadl2::publicpackagesection_constructor_exists():
    assert callable(aadl2::PublicPackageSection.__init__)


def test_aadl2::publicpackagesection_constructor_args():
    sig = inspect.signature(aadl2::PublicPackageSection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::modelunit_is_not_abstract():
    assert not inspect.isabstract(aadl2::ModelUnit)


def test_aadl2::modelunit_constructor_exists():
    assert callable(aadl2::ModelUnit.__init__)


def test_aadl2::modelunit_constructor_args():
    sig = inspect.signature(aadl2::ModelUnit.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featuregrouptyperename_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeatureGroupTypeRename)


def test_aadl2::featuregrouptyperename_constructor_exists():
    assert callable(aadl2::FeatureGroupTypeRename.__init__)


def test_aadl2::featuregrouptyperename_constructor_args():
    sig = inspect.signature(aadl2::FeatureGroupTypeRename.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::componenttyperename_is_not_abstract():
    assert not inspect.isabstract(aadl2::ComponentTypeRename)


def test_aadl2::componenttyperename_constructor_exists():
    assert callable(aadl2::ComponentTypeRename.__init__)


def test_aadl2::componenttyperename_constructor_args():
    sig = inspect.signature(aadl2::ComponentTypeRename.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"

def test_aadl2::componenttyperename_has_category():
    assert hasattr(aadl2::ComponentTypeRename, "category")
    descriptor = None
    for klass in aadl2::ComponentTypeRename.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::subprogram_is_not_abstract():
    assert not inspect.isabstract(aadl2::Subprogram)


def test_aadl2::subprogram_constructor_exists():
    assert callable(aadl2::Subprogram.__init__)


def test_aadl2::subprogram_constructor_args():
    sig = inspect.signature(aadl2::Subprogram.__init__)
    params = list(sig.parameters.keys())



def test_subprogramsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(SubprogramSubcomponentType)


def test_subprogramsubcomponenttype_constructor_exists():
    assert callable(SubprogramSubcomponentType.__init__)


def test_subprogramsubcomponenttype_constructor_args():
    sig = inspect.signature(SubprogramSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_subprogram_is_not_abstract():
    assert not inspect.isabstract(Subprogram)


def test_subprogram_constructor_exists():
    assert callable(Subprogram.__init__)


def test_subprogram_constructor_args():
    sig = inspect.signature(Subprogram.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramPrototype)


def test_aadl2::subprogramprototype_constructor_exists():
    assert callable(aadl2::SubprogramPrototype.__init__)


def test_aadl2::subprogramprototype_constructor_args():
    sig = inspect.signature(aadl2::SubprogramPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramClassifier)


def test_aadl2::subprogramclassifier_constructor_exists():
    assert callable(aadl2::SubprogramClassifier.__init__)


def test_aadl2::subprogramclassifier_constructor_args():
    sig = inspect.signature(aadl2::SubprogramClassifier.__init__)
    params = list(sig.parameters.keys())



def test_annexsubclause_is_not_abstract():
    assert not inspect.isabstract(AnnexSubclause)


def test_annexsubclause_constructor_exists():
    assert callable(AnnexSubclause.__init__)


def test_annexsubclause_constructor_args():
    sig = inspect.signature(AnnexSubclause.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::defaultannexsubclause_is_not_abstract():
    assert not inspect.isabstract(aadl2::DefaultAnnexSubclause)


def test_aadl2::defaultannexsubclause_constructor_exists():
    assert callable(aadl2::DefaultAnnexSubclause.__init__)


def test_aadl2::defaultannexsubclause_constructor_args():
    sig = inspect.signature(aadl2::DefaultAnnexSubclause.__init__)
    params = list(sig.parameters.keys())
    assert "sourceText" in params, "Missing parameter 'sourceText'"

def test_aadl2::defaultannexsubclause_has_sourceText():
    assert hasattr(aadl2::DefaultAnnexSubclause, "sourceText")
    descriptor = None
    for klass in aadl2::DefaultAnnexSubclause.__mro__:
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



def test_aadl2::defaultannexlibrary_is_not_abstract():
    assert not inspect.isabstract(aadl2::DefaultAnnexLibrary)


def test_aadl2::defaultannexlibrary_constructor_exists():
    assert callable(aadl2::DefaultAnnexLibrary.__init__)


def test_aadl2::defaultannexlibrary_constructor_args():
    sig = inspect.signature(aadl2::DefaultAnnexLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "sourceText" in params, "Missing parameter 'sourceText'"

def test_aadl2::defaultannexlibrary_has_sourceText():
    assert hasattr(aadl2::DefaultAnnexLibrary, "sourceText")
    descriptor = None
    for klass in aadl2::DefaultAnnexLibrary.__mro__:
        if "sourceText" in klass.__dict__:
            descriptor = klass.__dict__["sourceText"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::annexlibrary_is_not_abstract():
    assert not inspect.isabstract(aadl2::AnnexLibrary)


def test_aadl2::annexlibrary_constructor_exists():
    assert callable(aadl2::AnnexLibrary.__init__)


def test_aadl2::annexlibrary_constructor_args():
    sig = inspect.signature(aadl2::AnnexLibrary.__init__)
    params = list(sig.parameters.keys())



def test_internalfeature_is_not_abstract():
    assert not inspect.isabstract(InternalFeature)


def test_internalfeature_constructor_exists():
    assert callable(InternalFeature.__init__)


def test_internalfeature_constructor_args():
    sig = inspect.signature(InternalFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::eventdatasource_is_not_abstract():
    assert not inspect.isabstract(aadl2::EventDataSource)


def test_aadl2::eventdatasource_constructor_exists():
    assert callable(aadl2::EventDataSource.__init__)


def test_aadl2::eventdatasource_constructor_args():
    sig = inspect.signature(aadl2::EventDataSource.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::eventsource_is_not_abstract():
    assert not inspect.isabstract(aadl2::EventSource)


def test_aadl2::eventsource_constructor_exists():
    assert callable(aadl2::EventSource.__init__)


def test_aadl2::eventsource_constructor_args():
    sig = inspect.signature(aadl2::EventSource.__init__)
    params = list(sig.parameters.keys())



def test_processorfeature_is_not_abstract():
    assert not inspect.isabstract(ProcessorFeature)


def test_processorfeature_constructor_exists():
    assert callable(ProcessorFeature.__init__)


def test_processorfeature_constructor_args():
    sig = inspect.signature(ProcessorFeature.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::data_is_not_abstract():
    assert not inspect.isabstract(aadl2::Data)


def test_aadl2::data_constructor_exists():
    assert callable(aadl2::Data.__init__)


def test_aadl2::data_constructor_args():
    sig = inspect.signature(aadl2::Data.__init__)
    params = list(sig.parameters.keys())



def test_datasubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(DataSubcomponentType)


def test_datasubcomponenttype_constructor_exists():
    assert callable(DataSubcomponentType.__init__)


def test_datasubcomponenttype_constructor_args():
    sig = inspect.signature(DataSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_data_constructor_exists():
    assert callable(Data.__init__)


def test_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::dataprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::DataPrototype)


def test_aadl2::dataprototype_constructor_exists():
    assert callable(aadl2::DataPrototype.__init__)


def test_aadl2::dataprototype_constructor_args():
    sig = inspect.signature(aadl2::DataPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::dataclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::DataClassifier)


def test_aadl2::dataclassifier_constructor_exists():
    assert callable(aadl2::DataClassifier.__init__)


def test_aadl2::dataclassifier_constructor_args():
    sig = inspect.signature(aadl2::DataClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::abstract_is_not_abstract():
    assert not inspect.isabstract(aadl2::Abstract)


def test_aadl2::abstract_constructor_exists():
    assert callable(aadl2::Abstract.__init__)


def test_aadl2::abstract_constructor_args():
    sig = inspect.signature(aadl2::Abstract.__init__)
    params = list(sig.parameters.keys())



def test_abstract_is_not_abstract():
    assert not inspect.isabstract(Abstract)


def test_abstract_constructor_exists():
    assert callable(Abstract.__init__)


def test_abstract_constructor_args():
    sig = inspect.signature(Abstract.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::abstractclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::AbstractClassifier)


def test_aadl2::abstractclassifier_constructor_exists():
    assert callable(aadl2::AbstractClassifier.__init__)


def test_aadl2::abstractclassifier_constructor_args():
    sig = inspect.signature(aadl2::AbstractClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::abstractprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::AbstractPrototype)


def test_aadl2::abstractprototype_constructor_exists():
    assert callable(aadl2::AbstractPrototype.__init__)


def test_aadl2::abstractprototype_constructor_args():
    sig = inspect.signature(aadl2::AbstractPrototype.__init__)
    params = list(sig.parameters.keys())



def test_subcomponent_is_not_abstract():
    assert not inspect.isabstract(Subcomponent)


def test_subcomponent_constructor_exists():
    assert callable(Subcomponent.__init__)


def test_subcomponent_constructor_args():
    sig = inspect.signature(Subcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::systemsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::SystemSubcomponent)


def test_aadl2::systemsubcomponent_constructor_exists():
    assert callable(aadl2::SystemSubcomponent.__init__)


def test_aadl2::systemsubcomponent_constructor_args():
    sig = inspect.signature(aadl2::SystemSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualprocessorsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualProcessorSubcomponent)


def test_aadl2::virtualprocessorsubcomponent_constructor_exists():
    assert callable(aadl2::VirtualProcessorSubcomponent.__init__)


def test_aadl2::virtualprocessorsubcomponent_constructor_args():
    sig = inspect.signature(aadl2::VirtualProcessorSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processorsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessorSubcomponent)


def test_aadl2::processorsubcomponent_constructor_exists():
    assert callable(aadl2::ProcessorSubcomponent.__init__)


def test_aadl2::processorsubcomponent_constructor_args():
    sig = inspect.signature(aadl2::ProcessorSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::abstractsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::AbstractSubcomponent)


def test_aadl2::abstractsubcomponent_constructor_exists():
    assert callable(aadl2::AbstractSubcomponent.__init__)


def test_aadl2::abstractsubcomponent_constructor_args():
    sig = inspect.signature(aadl2::AbstractSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::processsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::ProcessSubcomponent)


def test_aadl2::processsubcomponent_constructor_exists():
    assert callable(aadl2::ProcessSubcomponent.__init__)


def test_aadl2::processsubcomponent_constructor_args():
    sig = inspect.signature(aadl2::ProcessSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::memorysubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::MemorySubcomponent)


def test_aadl2::memorysubcomponent_constructor_exists():
    assert callable(aadl2::MemorySubcomponent.__init__)


def test_aadl2::memorysubcomponent_constructor_args():
    sig = inspect.signature(aadl2::MemorySubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadgroupsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadGroupSubcomponent)


def test_aadl2::threadgroupsubcomponent_constructor_exists():
    assert callable(aadl2::ThreadGroupSubcomponent.__init__)


def test_aadl2::threadgroupsubcomponent_constructor_args():
    sig = inspect.signature(aadl2::ThreadGroupSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::threadsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::ThreadSubcomponent)


def test_aadl2::threadsubcomponent_constructor_exists():
    assert callable(aadl2::ThreadSubcomponent.__init__)


def test_aadl2::threadsubcomponent_constructor_args():
    sig = inspect.signature(aadl2::ThreadSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::devicesubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::DeviceSubcomponent)


def test_aadl2::devicesubcomponent_constructor_exists():
    assert callable(aadl2::DeviceSubcomponent.__init__)


def test_aadl2::devicesubcomponent_constructor_args():
    sig = inspect.signature(aadl2::DeviceSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::accessconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2::AccessConnection)


def test_aadl2::accessconnection_constructor_exists():
    assert callable(aadl2::AccessConnection.__init__)


def test_aadl2::accessconnection_constructor_args():
    sig = inspect.signature(aadl2::AccessConnection.__init__)
    params = list(sig.parameters.keys())
    assert "accessCategory" in params, "Missing parameter 'accessCategory'"

def test_aadl2::accessconnection_has_accessCategory():
    assert hasattr(aadl2::AccessConnection, "accessCategory")
    descriptor = None
    for klass in aadl2::AccessConnection.__mro__:
        if "accessCategory" in klass.__dict__:
            descriptor = klass.__dict__["accessCategory"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::featureconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeatureConnection)


def test_aadl2::featureconnection_constructor_exists():
    assert callable(aadl2::FeatureConnection.__init__)


def test_aadl2::featureconnection_constructor_args():
    sig = inspect.signature(aadl2::FeatureConnection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::parameterconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2::ParameterConnection)


def test_aadl2::parameterconnection_constructor_exists():
    assert callable(aadl2::ParameterConnection.__init__)


def test_aadl2::parameterconnection_constructor_args():
    sig = inspect.signature(aadl2::ParameterConnection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::portconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2::PortConnection)


def test_aadl2::portconnection_constructor_exists():
    assert callable(aadl2::PortConnection.__init__)


def test_aadl2::portconnection_constructor_args():
    sig = inspect.signature(aadl2::PortConnection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featuregroupconnection_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeatureGroupConnection)


def test_aadl2::featuregroupconnection_constructor_exists():
    assert callable(aadl2::FeatureGroupConnection.__init__)


def test_aadl2::featuregroupconnection_constructor_args():
    sig = inspect.signature(aadl2::FeatureGroupConnection.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::endtoendflowsegment_is_not_abstract():
    assert not inspect.isabstract(aadl2::EndToEndFlowSegment)


def test_aadl2::endtoendflowsegment_constructor_exists():
    assert callable(aadl2::EndToEndFlowSegment.__init__)


def test_aadl2::endtoendflowsegment_constructor_args():
    sig = inspect.signature(aadl2::EndToEndFlowSegment.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::flowsegment_is_not_abstract():
    assert not inspect.isabstract(aadl2::FlowSegment)


def test_aadl2::flowsegment_constructor_exists():
    assert callable(aadl2::FlowSegment.__init__)


def test_aadl2::flowsegment_constructor_args():
    sig = inspect.signature(aadl2::FlowSegment.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::connectedelement_is_not_abstract():
    assert not inspect.isabstract(aadl2::ConnectedElement)


def test_aadl2::connectedelement_constructor_exists():
    assert callable(aadl2::ConnectedElement.__init__)


def test_aadl2::connectedelement_constructor_args():
    sig = inspect.signature(aadl2::ConnectedElement.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::modebinding_is_not_abstract():
    assert not inspect.isabstract(aadl2::ModeBinding)


def test_aadl2::modebinding_constructor_exists():
    assert callable(aadl2::ModeBinding.__init__)


def test_aadl2::modebinding_constructor_args():
    sig = inspect.signature(aadl2::ModeBinding.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featureprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeaturePrototype)


def test_aadl2::featureprototype_constructor_exists():
    assert callable(aadl2::FeaturePrototype.__init__)


def test_aadl2::featureprototype_constructor_args():
    sig = inspect.signature(aadl2::FeaturePrototype.__init__)
    params = list(sig.parameters.keys())
    assert "out" in params, "Missing parameter 'out'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "in_" in params, "Missing parameter 'in_'"

def test_aadl2::featureprototype_has_out():
    assert hasattr(aadl2::FeaturePrototype, "out")
    descriptor = None
    for klass in aadl2::FeaturePrototype.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::featureprototype_has_direction():
    assert hasattr(aadl2::FeaturePrototype, "direction")
    descriptor = None
    for klass in aadl2::FeaturePrototype.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::featureprototype_has_in_():
    assert hasattr(aadl2::FeaturePrototype, "in_")
    descriptor = None
    for klass in aadl2::FeaturePrototype.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_triggerport_is_not_abstract():
    assert not inspect.isabstract(TriggerPort)


def test_triggerport_constructor_exists():
    assert callable(TriggerPort.__init__)


def test_triggerport_constructor_args():
    sig = inspect.signature(TriggerPort.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::abstractfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2::AbstractFeature)


def test_aadl2::abstractfeature_constructor_exists():
    assert callable(aadl2::AbstractFeature.__init__)


def test_aadl2::abstractfeature_constructor_args():
    sig = inspect.signature(aadl2::AbstractFeature.__init__)
    params = list(sig.parameters.keys())



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::accessconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2::AccessConnectionEnd)


def test_aadl2::accessconnectionend_constructor_exists():
    assert callable(aadl2::AccessConnectionEnd.__init__)


def test_aadl2::accessconnectionend_constructor_args():
    sig = inspect.signature(aadl2::AccessConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_accessconnectionend_is_not_abstract():
    assert not inspect.isabstract(AccessConnectionEnd)


def test_accessconnectionend_constructor_exists():
    assert callable(AccessConnectionEnd.__init__)


def test_accessconnectionend_constructor_args():
    sig = inspect.signature(AccessConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramgroupsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramGroupSubcomponent)


def test_aadl2::subprogramgroupsubcomponent_constructor_exists():
    assert callable(aadl2::SubprogramGroupSubcomponent.__init__)


def test_aadl2::subprogramgroupsubcomponent_constructor_args():
    sig = inspect.signature(aadl2::SubprogramGroupSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::bussubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::BusSubcomponent)


def test_aadl2::bussubcomponent_constructor_exists():
    assert callable(aadl2::BusSubcomponent.__init__)


def test_aadl2::bussubcomponent_constructor_args():
    sig = inspect.signature(aadl2::BusSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramsubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramSubcomponent)


def test_aadl2::subprogramsubcomponent_constructor_exists():
    assert callable(aadl2::SubprogramSubcomponent.__init__)


def test_aadl2::subprogramsubcomponent_constructor_args():
    sig = inspect.signature(aadl2::SubprogramSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramproxy_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramProxy)


def test_aadl2::subprogramproxy_constructor_exists():
    assert callable(aadl2::SubprogramProxy.__init__)


def test_aadl2::subprogramproxy_constructor_args():
    sig = inspect.signature(aadl2::SubprogramProxy.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualbussubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualBusSubcomponent)


def test_aadl2::virtualbussubcomponent_constructor_exists():
    assert callable(aadl2::VirtualBusSubcomponent.__init__)


def test_aadl2::virtualbussubcomponent_constructor_args():
    sig = inspect.signature(aadl2::VirtualBusSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::access_is_not_abstract():
    assert not inspect.isabstract(aadl2::Access)


def test_aadl2::access_constructor_exists():
    assert callable(aadl2::Access.__init__)


def test_aadl2::access_constructor_args():
    sig = inspect.signature(aadl2::Access.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "category" in params, "Missing parameter 'category'"

def test_aadl2::access_has_kind():
    assert hasattr(aadl2::Access, "kind")
    descriptor = None
    for klass in aadl2::Access.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::access_has_category():
    assert hasattr(aadl2::Access, "category")
    descriptor = None
    for klass in aadl2::Access.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::busfeatureclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::BusFeatureClassifier)


def test_aadl2::busfeatureclassifier_constructor_exists():
    assert callable(aadl2::BusFeatureClassifier.__init__)


def test_aadl2::busfeatureclassifier_constructor_args():
    sig = inspect.signature(aadl2::BusFeatureClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::abstractfeatureclassifier_is_not_abstract():
    assert not inspect.isabstract(aadl2::AbstractFeatureClassifier)


def test_aadl2::abstractfeatureclassifier_constructor_exists():
    assert callable(aadl2::AbstractFeatureClassifier.__init__)


def test_aadl2::abstractfeatureclassifier_constructor_args():
    sig = inspect.signature(aadl2::AbstractFeatureClassifier.__init__)
    params = list(sig.parameters.keys())



def test_access_is_not_abstract():
    assert not inspect.isabstract(Access)


def test_access_constructor_exists():
    assert callable(Access.__init__)


def test_access_constructor_args():
    sig = inspect.signature(Access.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::busaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2::BusAccess)


def test_aadl2::busaccess_constructor_exists():
    assert callable(aadl2::BusAccess.__init__)


def test_aadl2::busaccess_constructor_args():
    sig = inspect.signature(aadl2::BusAccess.__init__)
    params = list(sig.parameters.keys())
    assert "virtual" in params, "Missing parameter 'virtual'"

def test_aadl2::busaccess_has_virtual():
    assert hasattr(aadl2::BusAccess, "virtual")
    descriptor = None
    for klass in aadl2::BusAccess.__mro__:
        if "virtual" in klass.__dict__:
            descriptor = klass.__dict__["virtual"]
            break
    assert isinstance(descriptor, property)



def test_abstractfeatureclassifier_is_not_abstract():
    assert not inspect.isabstract(AbstractFeatureClassifier)


def test_abstractfeatureclassifier_constructor_exists():
    assert callable(AbstractFeatureClassifier.__init__)


def test_abstractfeatureclassifier_constructor_args():
    sig = inspect.signature(AbstractFeatureClassifier.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::bussubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::BusSubcomponentType)


def test_aadl2::bussubcomponenttype_constructor_exists():
    assert callable(aadl2::BusSubcomponentType.__init__)


def test_aadl2::bussubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::BusSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramgroupsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramGroupSubcomponentType)


def test_aadl2::subprogramgroupsubcomponenttype_constructor_exists():
    assert callable(aadl2::SubprogramGroupSubcomponentType.__init__)


def test_aadl2::subprogramgroupsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::SubprogramGroupSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramSubcomponentType)


def test_aadl2::subprogramsubcomponenttype_constructor_exists():
    assert callable(aadl2::SubprogramSubcomponentType.__init__)


def test_aadl2::subprogramsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::SubprogramSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::virtualbussubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::VirtualBusSubcomponentType)


def test_aadl2::virtualbussubcomponenttype_constructor_exists():
    assert callable(aadl2::VirtualBusSubcomponentType.__init__)


def test_aadl2::virtualbussubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::VirtualBusSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::abstractsubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::AbstractSubcomponentType)


def test_aadl2::abstractsubcomponenttype_constructor_exists():
    assert callable(aadl2::AbstractSubcomponentType.__init__)


def test_aadl2::abstractsubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::AbstractSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::portconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2::PortConnectionEnd)


def test_aadl2::portconnectionend_constructor_exists():
    assert callable(aadl2::PortConnectionEnd.__init__)


def test_aadl2::portconnectionend_constructor_args():
    sig = inspect.signature(aadl2::PortConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::parameterconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2::ParameterConnectionEnd)


def test_aadl2::parameterconnectionend_constructor_exists():
    assert callable(aadl2::ParameterConnectionEnd.__init__)


def test_aadl2::parameterconnectionend_constructor_args():
    sig = inspect.signature(aadl2::ParameterConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::datasubcomponenttype_is_not_abstract():
    assert not inspect.isabstract(aadl2::DataSubcomponentType)


def test_aadl2::datasubcomponenttype_constructor_exists():
    assert callable(aadl2::DataSubcomponentType.__init__)


def test_aadl2::datasubcomponenttype_constructor_args():
    sig = inspect.signature(aadl2::DataSubcomponentType.__init__)
    params = list(sig.parameters.keys())



def test_portconnectionend_is_not_abstract():
    assert not inspect.isabstract(PortConnectionEnd)


def test_portconnectionend_constructor_exists():
    assert callable(PortConnectionEnd.__init__)


def test_portconnectionend_constructor_args():
    sig = inspect.signature(PortConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::portproxy_is_not_abstract():
    assert not inspect.isabstract(aadl2::PortProxy)


def test_aadl2::portproxy_constructor_exists():
    assert callable(aadl2::PortProxy.__init__)


def test_aadl2::portproxy_constructor_args():
    sig = inspect.signature(aadl2::PortProxy.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "in_" in params, "Missing parameter 'in_'"
    assert "out" in params, "Missing parameter 'out'"

def test_aadl2::portproxy_has_direction():
    assert hasattr(aadl2::PortProxy, "direction")
    descriptor = None
    for klass in aadl2::PortProxy.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::portproxy_has_in_():
    assert hasattr(aadl2::PortProxy, "in_")
    descriptor = None
    for klass in aadl2::PortProxy.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::portproxy_has_out():
    assert hasattr(aadl2::PortProxy, "out")
    descriptor = None
    for klass in aadl2::PortProxy.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::internalfeature_is_not_abstract():
    assert not inspect.isabstract(aadl2::InternalFeature)


def test_aadl2::internalfeature_constructor_exists():
    assert callable(aadl2::InternalFeature.__init__)


def test_aadl2::internalfeature_constructor_args():
    sig = inspect.signature(aadl2::InternalFeature.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "out" in params, "Missing parameter 'out'"
    assert "in_" in params, "Missing parameter 'in_'"

def test_aadl2::internalfeature_has_direction():
    assert hasattr(aadl2::InternalFeature, "direction")
    descriptor = None
    for klass in aadl2::InternalFeature.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::internalfeature_has_out():
    assert hasattr(aadl2::InternalFeature, "out")
    descriptor = None
    for klass in aadl2::InternalFeature.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)

def test_aadl2::internalfeature_has_in_():
    assert hasattr(aadl2::InternalFeature, "in_")
    descriptor = None
    for klass in aadl2::InternalFeature.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_aadl2::port_is_not_abstract():
    assert not inspect.isabstract(aadl2::Port)


def test_aadl2::port_constructor_exists():
    assert callable(aadl2::Port.__init__)


def test_aadl2::port_constructor_args():
    sig = inspect.signature(aadl2::Port.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"

def test_aadl2::port_has_category():
    assert hasattr(aadl2::Port, "category")
    descriptor = None
    for klass in aadl2::Port.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_parameterconnectionend_is_not_abstract():
    assert not inspect.isabstract(ParameterConnectionEnd)


def test_parameterconnectionend_constructor_exists():
    assert callable(ParameterConnectionEnd.__init__)


def test_parameterconnectionend_constructor_args():
    sig = inspect.signature(ParameterConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::datasubcomponent_is_not_abstract():
    assert not inspect.isabstract(aadl2::DataSubcomponent)


def test_aadl2::datasubcomponent_constructor_exists():
    assert callable(aadl2::DataSubcomponent.__init__)


def test_aadl2::datasubcomponent_constructor_args():
    sig = inspect.signature(aadl2::DataSubcomponent.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::dataport_is_not_abstract():
    assert not inspect.isabstract(aadl2::DataPort)


def test_aadl2::dataport_constructor_exists():
    assert callable(aadl2::DataPort.__init__)


def test_aadl2::dataport_constructor_args():
    sig = inspect.signature(aadl2::DataPort.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::dataaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2::DataAccess)


def test_aadl2::dataaccess_constructor_exists():
    assert callable(aadl2::DataAccess.__init__)


def test_aadl2::dataaccess_constructor_args():
    sig = inspect.signature(aadl2::DataAccess.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::parameter_is_not_abstract():
    assert not inspect.isabstract(aadl2::Parameter)


def test_aadl2::parameter_constructor_exists():
    assert callable(aadl2::Parameter.__init__)


def test_aadl2::parameter_constructor_args():
    sig = inspect.signature(aadl2::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::eventport_is_not_abstract():
    assert not inspect.isabstract(aadl2::EventPort)


def test_aadl2::eventport_constructor_exists():
    assert callable(aadl2::EventPort.__init__)


def test_aadl2::eventport_constructor_args():
    sig = inspect.signature(aadl2::EventPort.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramgroupaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramGroupAccess)


def test_aadl2::subprogramgroupaccess_constructor_exists():
    assert callable(aadl2::SubprogramGroupAccess.__init__)


def test_aadl2::subprogramgroupaccess_constructor_args():
    sig = inspect.signature(aadl2::SubprogramGroupAccess.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::subprogramaccess_is_not_abstract():
    assert not inspect.isabstract(aadl2::SubprogramAccess)


def test_aadl2::subprogramaccess_constructor_exists():
    assert callable(aadl2::SubprogramAccess.__init__)


def test_aadl2::subprogramaccess_constructor_args():
    sig = inspect.signature(aadl2::SubprogramAccess.__init__)
    params = list(sig.parameters.keys())



def test_featuretype_is_not_abstract():
    assert not inspect.isabstract(FeatureType)


def test_featuretype_constructor_exists():
    assert callable(FeatureType.__init__)


def test_featuretype_constructor_args():
    sig = inspect.signature(FeatureType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featuregrouptype_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeatureGroupType)


def test_aadl2::featuregrouptype_constructor_exists():
    assert callable(aadl2::FeatureGroupType.__init__)


def test_aadl2::featuregrouptype_constructor_args():
    sig = inspect.signature(aadl2::FeatureGroupType.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featuregroupprototype_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeatureGroupPrototype)


def test_aadl2::featuregroupprototype_constructor_exists():
    assert callable(aadl2::FeatureGroupPrototype.__init__)


def test_aadl2::featuregroupprototype_constructor_args():
    sig = inspect.signature(aadl2::FeatureGroupPrototype.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::featuregroupconnectionend_is_not_abstract():
    assert not inspect.isabstract(aadl2::FeatureGroupConnectionEnd)


def test_aadl2::featuregroupconnectionend_constructor_exists():
    assert callable(aadl2::FeatureGroupConnectionEnd.__init__)


def test_aadl2::featuregroupconnectionend_constructor_args():
    sig = inspect.signature(aadl2::FeatureGroupConnectionEnd.__init__)
    params = list(sig.parameters.keys())



def test_aadl2::eventdataport_is_not_abstract():
    assert not inspect.isabstract(aadl2::EventDataPort)


def test_aadl2::eventdataport_constructor_exists():
    assert callable(aadl2::EventDataPort.__init__)


def test_aadl2::eventdataport_constructor_args():
    sig = inspect.signature(aadl2::EventDataPort.__init__)
    params = list(sig.parameters.keys())

def test_accesstype_exists():
    # Check that the Enumeration exists
    assert AccessType is not None

def test_accesstype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessType]
    expected_literals = [
        "requires",
        "provides",
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
        "in_",
        "inOut",
        "out",
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
        "virtualProcessor",
        "subprogram",
        "bus",
        "process",
        "thread",
        "processor",
        "memory",
        "virtualBus",
        "system",
        "device",
        "threadGroup",
        "subprogramGroup",
        "data",
        "abstract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentCategory"

def test_operationkind_exists():
    # Check that the Enumeration exists
    assert OperationKind is not None

def test_operationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperationKind]
    expected_literals = [
        "minus",
        "plus",
        "and_",
        "not_",
        "or_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperationKind"

def test_accesscategory_exists():
    # Check that the Enumeration exists
    assert AccessCategory is not None

def test_accesscategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessCategory]
    expected_literals = [
        "subprogramGroup",
        "data",
        "bus",
        "virtualBus",
        "subprogram",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessCategory"

def test_flowkind_exists():
    # Check that the Enumeration exists
    assert FlowKind is not None

def test_flowkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlowKind]
    expected_literals = [
        "path",
        "source",
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
        "eventData",
        "event",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PortCategory"


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
NumberType_strategy = st.builds(
    NumberType,
)
aadl2::AadlReal_strategy = st.builds(
    aadl2::AadlReal,
)
aadl2::AadlInteger_strategy = st.builds(
    aadl2::AadlInteger,
)
NonListType_strategy = st.builds(
    NonListType,
)
aadl2::AadlString_strategy = st.builds(
    aadl2::AadlString,
)
aadl2::ClassifierType_strategy = st.builds(
    aadl2::ClassifierType,
)
aadl2::RangeType_strategy = st.builds(
    aadl2::RangeType,
)
aadl2::NumberType_strategy = st.builds(
    aadl2::NumberType,
)
aadl2::ReferenceType_strategy = st.builds(
    aadl2::ReferenceType,
)
aadl2::AadlBoolean_strategy = st.builds(
    aadl2::AadlBoolean,
)
PropertyType_strategy = st.builds(
    PropertyType,
)
aadl2::ListType_strategy = st.builds(
    aadl2::ListType,
)
aadl2::NonListType_strategy = st.builds(
    aadl2::NonListType,
)
EnumerationType_strategy = st.builds(
    EnumerationType,
)
aadl2::UnitsType_strategy = st.builds(
    aadl2::UnitsType,
)
NumberValue_strategy = st.builds(
    NumberValue,
)
aadl2::IntegerLiteral_strategy = st.builds(
    aadl2::IntegerLiteral,
    value=
        safe_text,
    base=
        safe_text
)
ContainedNamedElement_strategy = st.builds(
    ContainedNamedElement,
)
aadl2::RealLiteral_strategy = st.builds(
    aadl2::RealLiteral,
    value=
        safe_text
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
aadl2::UnitLiteral_strategy = st.builds(
    aadl2::UnitLiteral,
)
PropertyExpression_strategy = st.builds(
    PropertyExpression,
)
aadl2::ListValue_strategy = st.builds(
    aadl2::ListValue,
)
aadl2::Operation_strategy = st.builds(
    aadl2::Operation,
    op=
        safe_text
)
aadl2::PropertyValue_strategy = st.builds(
    aadl2::PropertyValue,
)
ArraySizeProperty_strategy = st.builds(
    ArraySizeProperty,
)
PropertyValue_strategy = st.builds(
    PropertyValue,
)
aadl2::NumberValue_strategy = st.builds(
    aadl2::NumberValue,
)
aadl2::BooleanLiteral_strategy = st.builds(
    aadl2::BooleanLiteral,
    value=
        safe_text
)
aadl2::NamedValue_strategy = st.builds(
    aadl2::NamedValue,
)
aadl2::RangeValue_strategy = st.builds(
    aadl2::RangeValue,
)
aadl2::ComputedValue_strategy = st.builds(
    aadl2::ComputedValue,
    function=
        safe_text
)
aadl2::ReferenceValue_strategy = st.builds(
    aadl2::ReferenceValue,
)
aadl2::RecordValue_strategy = st.builds(
    aadl2::RecordValue,
)
aadl2::StringLiteral_strategy = st.builds(
    aadl2::StringLiteral,
    value=
        safe_text
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
ProcessClassifier_strategy = st.builds(
    ProcessClassifier,
)
ProcessorClassifier_strategy = st.builds(
    ProcessorClassifier,
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
MemoryClassifier_strategy = st.builds(
    MemoryClassifier,
)
Generalization__strategy = st.builds(
    Generalization_,
)
aadl2::GroupExtension_strategy = st.builds(
    aadl2::GroupExtension,
)
EndToEndFlowElement_strategy = st.builds(
    EndToEndFlowElement,
)
aadl2::FlowElement_strategy = st.builds(
    aadl2::FlowElement,
)
Feature_strategy = st.builds(
    Feature,
)
aadl2::DirectedFeature_strategy = st.builds(
    aadl2::DirectedFeature,
    direction=
        safe_text,
    out=
        safe_text,
    in_=
        safe_text
)
aadl2::CallContext_strategy = st.builds(
    aadl2::CallContext,
)
aadl2::FeatureType_strategy = st.builds(
    aadl2::FeatureType,
)
CallContext_strategy = st.builds(
    CallContext,
)
FeatureGroupConnectionEnd_strategy = st.builds(
    FeatureGroupConnectionEnd,
)
Context_strategy = st.builds(
    Context,
)
DirectedFeature_strategy = st.builds(
    DirectedFeature,
)
FlowElement_strategy = st.builds(
    FlowElement,
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
ConnectionEnd_strategy = st.builds(
    ConnectionEnd,
)
aadl2::FeatureConnectionEnd_strategy = st.builds(
    aadl2::FeatureConnectionEnd,
)
Flow_strategy = st.builds(
    Flow,
)
aadl2::FeatureGroup_strategy = st.builds(
    aadl2::FeatureGroup,
    inverse=
        safe_text
)
aadl2::TypeExtension_strategy = st.builds(
    aadl2::TypeExtension,
)
aadl2::FlowSpecification_strategy = st.builds(
    aadl2::FlowSpecification,
    kind=
        safe_text
)
ArrayableElement_strategy = st.builds(
    ArrayableElement,
)
FeatureConnectionEnd_strategy = st.builds(
    FeatureConnectionEnd,
)
aadl2::FeatureClassifier_strategy = st.builds(
    aadl2::FeatureClassifier,
)
FeatureClassifier_strategy = st.builds(
    FeatureClassifier,
)
SubcomponentType_strategy = st.builds(
    SubcomponentType,
)
aadl2::ComponentPrototype_strategy = st.builds(
    aadl2::ComponentPrototype,
    array=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
aadl2::ComponentClassifier_strategy = st.builds(
    aadl2::ComponentClassifier,
    derivedModes=
        safe_text,
    noFlows=
        safe_text,
    noModes=
        safe_text
)
aadl2::EndToEndFlow_strategy = st.builds(
    aadl2::EndToEndFlow,
)
aadl2::Realization_strategy = st.builds(
    aadl2::Realization,
)
aadl2::ImplementationExtension_strategy = st.builds(
    aadl2::ImplementationExtension,
)
ComponentClassifier_strategy = st.builds(
    ComponentClassifier,
)
aadl2::ComponentType_strategy = st.builds(
    aadl2::ComponentType,
    noFeatures=
        safe_text
)
aadl2::ComponentImplementation_strategy = st.builds(
    aadl2::ComponentImplementation,
    noCalls=
        safe_text,
    noConnections=
        safe_text,
    noSubcomponents=
        safe_text
)
aadl2::ArraySizeProperty_strategy = st.builds(
    aadl2::ArraySizeProperty,
)
RefinableElement_strategy = st.builds(
    RefinableElement,
)
CalledSubprogram_strategy = st.builds(
    CalledSubprogram,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
aadl2::Feature_strategy = st.builds(
    aadl2::Feature,
)
aadl2::ProcessorFeature_strategy = st.builds(
    aadl2::ProcessorFeature,
)
aadl2::FlowFeature_strategy = st.builds(
    aadl2::FlowFeature,
)
aadl2::Connection_strategy = st.builds(
    aadl2::Connection,
    bidirectional=
        safe_text
)
ClassifierFeature_strategy = st.builds(
    ClassifierFeature,
)
aadl2::FlowImplementation_strategy = st.builds(
    aadl2::FlowImplementation,
    kind=
        safe_text
)
aadl2::BehavioralFeature_strategy = st.builds(
    aadl2::BehavioralFeature,
)
aadl2::StructuralFeature_strategy = st.builds(
    aadl2::StructuralFeature,
)
aadl2::ModeFeature_strategy = st.builds(
    aadl2::ModeFeature,
)
aadl2::CalledSubprogram_strategy = st.builds(
    aadl2::CalledSubprogram,
)
Relationship_strategy = st.builds(
    Relationship,
)
aadl2::DirectedRelationship_strategy = st.builds(
    aadl2::DirectedRelationship,
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
ModeFeature_strategy = st.builds(
    ModeFeature,
)
aadl2::ModeTransition_strategy = st.builds(
    aadl2::ModeTransition,
)
aadl2::Mode_strategy = st.builds(
    aadl2::Mode,
    derived=
        safe_text,
    initial=
        safe_text
)
ModalElement_strategy = st.builds(
    ModalElement,
)
aadl2::Subcomponent_strategy = st.builds(
    aadl2::Subcomponent,
    allModes=
        safe_text
)
aadl2::ModalPath_strategy = st.builds(
    aadl2::ModalPath,
)
aadl2::Prototype_strategy = st.builds(
    aadl2::Prototype,
)
aadl2::AnnexSubclause_strategy = st.builds(
    aadl2::AnnexSubclause,
)
aadl2::Generalization__strategy = st.builds(
    aadl2::Generalization_,
)
PropertyOwner_strategy = st.builds(
    PropertyOwner,
)
aadl2::ClassifierValue_strategy = st.builds(
    aadl2::ClassifierValue,
)
aadl2::AbstractNamedValue_strategy = st.builds(
    aadl2::AbstractNamedValue,
)
Type_strategy = st.builds(
    Type,
)
aadl2::SubcomponentType_strategy = st.builds(
    aadl2::SubcomponentType,
)
Namespace_strategy = st.builds(
    Namespace,
)
aadl2::EnumerationType_strategy = st.builds(
    aadl2::EnumerationType,
)
aadl2::RecordType_strategy = st.builds(
    aadl2::RecordType,
)
aadl2::GlobalNamespace_strategy = st.builds(
    aadl2::GlobalNamespace,
)
aadl2::MetaclassReference_strategy = st.builds(
    aadl2::MetaclassReference,
    annexName=
        safe_text,
    metaclassName=
        safe_text
)
AbstractNamedValue_strategy = st.builds(
    AbstractNamedValue,
)
BasicProperty_strategy = st.builds(
    BasicProperty,
)
aadl2::RecordField_strategy = st.builds(
    aadl2::RecordField,
)
aadl2::ModalPropertyValue_strategy = st.builds(
    aadl2::ModalPropertyValue,
)
aadl2::Classifier_strategy = st.builds(
    aadl2::Classifier,
    noProperties=
        safe_text,
    noPrototypes=
        safe_text,
    noAnnexes=
        safe_text
)
aadl2::PropertyType_strategy = st.builds(
    aadl2::PropertyType,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
aadl2::PropertyConstant_strategy = st.builds(
    aadl2::PropertyConstant,
)
aadl2::BasicProperty_strategy = st.builds(
    aadl2::BasicProperty,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
aadl2::Namespace_strategy = st.builds(
    aadl2::Namespace,
)
aadl2::TypedElement_strategy = st.builds(
    aadl2::TypedElement,
)
aadl2::ConnectionEnd_strategy = st.builds(
    aadl2::ConnectionEnd,
)
aadl2::ClassifierFeature_strategy = st.builds(
    aadl2::ClassifierFeature,
)
aadl2::TriggerPort_strategy = st.builds(
    aadl2::TriggerPort,
)
aadl2::EnumerationLiteral_strategy = st.builds(
    aadl2::EnumerationLiteral,
)
aadl2::Context_strategy = st.builds(
    aadl2::Context,
)
aadl2::EndToEndFlowElement_strategy = st.builds(
    aadl2::EndToEndFlowElement,
)
aadl2::RefinableElement_strategy = st.builds(
    aadl2::RefinableElement,
)
aadl2::ModalElement_strategy = st.builds(
    aadl2::ModalElement,
)
aadl2::Flow_strategy = st.builds(
    aadl2::Flow,
)
aadl2::Type_strategy = st.builds(
    aadl2::Type,
)
aadl2::Property_strategy = st.builds(
    aadl2::Property,
    emptyListDefault=
        safe_text,
    inherit=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
aadl2::ContainedNamedElement_strategy = st.builds(
    aadl2::ContainedNamedElement,
)
aadl2::PropertyAssociation_strategy = st.builds(
    aadl2::PropertyAssociation,
    constant=
        safe_text,
    append=
        safe_text
)
aadl2::PropertyExpression_strategy = st.builds(
    aadl2::PropertyExpression,
)
aadl2::ArraySize_strategy = st.builds(
    aadl2::ArraySize,
    size=
        safe_text
)
aadl2::NumericRange_strategy = st.builds(
    aadl2::NumericRange,
)
aadl2::Relationship_strategy = st.builds(
    aadl2::Relationship,
)
aadl2::PropertyOwner_strategy = st.builds(
    aadl2::PropertyOwner,
)
aadl2::PrototypeBinding_strategy = st.builds(
    aadl2::PrototypeBinding,
)
aadl2::ContainmentPathElement_strategy = st.builds(
    aadl2::ContainmentPathElement,
    annexName=
        safe_text
)
aadl2::ModeTransitionTrigger_strategy = st.builds(
    aadl2::ModeTransitionTrigger,
)
aadl2::ArrayDimension_strategy = st.builds(
    aadl2::ArrayDimension,
)
aadl2::BasicPropertyAssociation_strategy = st.builds(
    aadl2::BasicPropertyAssociation,
)
aadl2::ArrayableElement_strategy = st.builds(
    aadl2::ArrayableElement,
)
aadl2::FlowEnd_strategy = st.builds(
    aadl2::FlowEnd,
)
aadl2::ArrayRange_strategy = st.builds(
    aadl2::ArrayRange,
    lowerBound=
        safe_text,
    upperBound=
        safe_text
)
aadl2::NamedElement_strategy = st.builds(
    aadl2::NamedElement,
    name=
        safe_text,
    qualifiedName=
        safe_text
)
aadl2::ComponentImplementationReference_strategy = st.builds(
    aadl2::ComponentImplementationReference,
)
aadl2::Comment_strategy = st.builds(
    aadl2::Comment,
    body=
        safe_text
)
aadl2::Element_strategy = st.builds(
    aadl2::Element,
)
DeviceClassifier_strategy = st.builds(
    DeviceClassifier,
)
DataClassifier_strategy = st.builds(
    DataClassifier,
)
ComponentPrototype_strategy = st.builds(
    ComponentPrototype,
)
aadl2::VirtualProcessor_strategy = st.builds(
    aadl2::VirtualProcessor,
)
BusClassifier_strategy = st.builds(
    BusClassifier,
)
Thread_strategy = st.builds(
    Thread,
)
VirtualProcessor_strategy = st.builds(
    VirtualProcessor,
)
aadl2::VirtualBus_strategy = st.builds(
    aadl2::VirtualBus,
)
VirtualBus_strategy = st.builds(
    VirtualBus,
)
aadl2::ThreadGroup_strategy = st.builds(
    aadl2::ThreadGroup,
)
ThreadGroup_strategy = st.builds(
    ThreadGroup,
)
aadl2::Thread_strategy = st.builds(
    aadl2::Thread,
)
Processor_strategy = st.builds(
    Processor,
)
aadl2::Process_strategy = st.builds(
    aadl2::Process,
)
aadl2::SubprogramGroup_strategy = st.builds(
    aadl2::SubprogramGroup,
)
SubprogramGroup_strategy = st.builds(
    SubprogramGroup,
)
aadl2::System_strategy = st.builds(
    aadl2::System,
)
System_strategy = st.builds(
    System,
)
aadl2::Processor_strategy = st.builds(
    aadl2::Processor,
)
aadl2::Bus_strategy = st.builds(
    aadl2::Bus,
)
Process_strategy = st.builds(
    Process,
)
aadl2::Memory_strategy = st.builds(
    aadl2::Memory,
)
Memory_strategy = st.builds(
    Memory,
)
aadl2::Device_strategy = st.builds(
    aadl2::Device,
)
Device_strategy = st.builds(
    Device,
)
Bus_strategy = st.builds(
    Bus,
)
aadl2::ProcessorSubcomponentType_strategy = st.builds(
    aadl2::ProcessorSubcomponentType,
)
BehavioredImplementation_strategy = st.builds(
    BehavioredImplementation,
)
aadl2::ThreadImplementation_strategy = st.builds(
    aadl2::ThreadImplementation,
)
aadl2::SubprogramImplementation_strategy = st.builds(
    aadl2::SubprogramImplementation,
)
aadl2::DeviceSubcomponentType_strategy = st.builds(
    aadl2::DeviceSubcomponentType,
)
aadl2::MemorySubcomponentType_strategy = st.builds(
    aadl2::MemorySubcomponentType,
)
aadl2::ProcessSubcomponentType_strategy = st.builds(
    aadl2::ProcessSubcomponentType,
)
aadl2::SystemSubcomponentType_strategy = st.builds(
    aadl2::SystemSubcomponentType,
)
aadl2::ThreadSubcomponentType_strategy = st.builds(
    aadl2::ThreadSubcomponentType,
)
aadl2::ThreadGroupSubcomponentType_strategy = st.builds(
    aadl2::ThreadGroupSubcomponentType,
)
BusFeatureClassifier_strategy = st.builds(
    BusFeatureClassifier,
)
aadl2::VirtualProcessorSubcomponentType_strategy = st.builds(
    aadl2::VirtualProcessorSubcomponentType,
)
VirtualProcessorSubcomponentType_strategy = st.builds(
    VirtualProcessorSubcomponentType,
)
aadl2::VirtualProcessorClassifier_strategy = st.builds(
    aadl2::VirtualProcessorClassifier,
)
aadl2::VirtualProcessorPrototype_strategy = st.builds(
    aadl2::VirtualProcessorPrototype,
)
VirtualBusSubcomponentType_strategy = st.builds(
    VirtualBusSubcomponentType,
)
aadl2::VirtualBusPrototype_strategy = st.builds(
    aadl2::VirtualBusPrototype,
)
aadl2::VirtualBusClassifier_strategy = st.builds(
    aadl2::VirtualBusClassifier,
)
ThreadSubcomponentType_strategy = st.builds(
    ThreadSubcomponentType,
)
aadl2::ThreadPrototype_strategy = st.builds(
    aadl2::ThreadPrototype,
)
aadl2::ThreadClassifier_strategy = st.builds(
    aadl2::ThreadClassifier,
)
ThreadGroupSubcomponentType_strategy = st.builds(
    ThreadGroupSubcomponentType,
)
aadl2::ThreadGroupPrototype_strategy = st.builds(
    aadl2::ThreadGroupPrototype,
)
aadl2::ThreadGroupClassifier_strategy = st.builds(
    aadl2::ThreadGroupClassifier,
)
SystemSubcomponentType_strategy = st.builds(
    SystemSubcomponentType,
)
aadl2::SystemPrototype_strategy = st.builds(
    aadl2::SystemPrototype,
)
aadl2::SystemClassifier_strategy = st.builds(
    aadl2::SystemClassifier,
)
SubprogramGroupSubcomponentType_strategy = st.builds(
    SubprogramGroupSubcomponentType,
)
aadl2::SubprogramGroupClassifier_strategy = st.builds(
    aadl2::SubprogramGroupClassifier,
)
aadl2::SubprogramGroupPrototype_strategy = st.builds(
    aadl2::SubprogramGroupPrototype,
)
ProcessSubcomponentType_strategy = st.builds(
    ProcessSubcomponentType,
)
aadl2::ProcessPrototype_strategy = st.builds(
    aadl2::ProcessPrototype,
)
aadl2::ProcessClassifier_strategy = st.builds(
    aadl2::ProcessClassifier,
)
ProcessorSubcomponentType_strategy = st.builds(
    ProcessorSubcomponentType,
)
aadl2::ProcessorClassifier_strategy = st.builds(
    aadl2::ProcessorClassifier,
)
aadl2::ProcessorPrototype_strategy = st.builds(
    aadl2::ProcessorPrototype,
)
MemorySubcomponentType_strategy = st.builds(
    MemorySubcomponentType,
)
aadl2::MemoryClassifier_strategy = st.builds(
    aadl2::MemoryClassifier,
)
aadl2::MemoryPrototype_strategy = st.builds(
    aadl2::MemoryPrototype,
)
DeviceSubcomponentType_strategy = st.builds(
    DeviceSubcomponentType,
)
aadl2::DeviceClassifier_strategy = st.builds(
    aadl2::DeviceClassifier,
)
aadl2::DevicePrototype_strategy = st.builds(
    aadl2::DevicePrototype,
)
BusSubcomponentType_strategy = st.builds(
    BusSubcomponentType,
)
aadl2::BusPrototype_strategy = st.builds(
    aadl2::BusPrototype,
)
aadl2::BusClassifier_strategy = st.builds(
    aadl2::BusClassifier,
)
AbstractSubcomponentType_strategy = st.builds(
    AbstractSubcomponentType,
)
AbstractClassifier_strategy = st.builds(
    AbstractClassifier,
)
aadl2::AbstractImplementation_strategy = st.builds(
    aadl2::AbstractImplementation,
)
ComponentType_strategy = st.builds(
    ComponentType,
)
aadl2::MemoryType_strategy = st.builds(
    aadl2::MemoryType,
)
aadl2::ThreadGroupType_strategy = st.builds(
    aadl2::ThreadGroupType,
)
aadl2::VirtualProcessorType_strategy = st.builds(
    aadl2::VirtualProcessorType,
)
aadl2::BusType_strategy = st.builds(
    aadl2::BusType,
)
aadl2::DataType_strategy = st.builds(
    aadl2::DataType,
)
aadl2::ProcessType_strategy = st.builds(
    aadl2::ProcessType,
)
aadl2::SubprogramType_strategy = st.builds(
    aadl2::SubprogramType,
)
aadl2::ThreadType_strategy = st.builds(
    aadl2::ThreadType,
)
aadl2::DeviceType_strategy = st.builds(
    aadl2::DeviceType,
)
aadl2::VirtualBusType_strategy = st.builds(
    aadl2::VirtualBusType,
)
aadl2::ProcessorType_strategy = st.builds(
    aadl2::ProcessorType,
)
aadl2::SystemType_strategy = st.builds(
    aadl2::SystemType,
)
aadl2::SubprogramGroupType_strategy = st.builds(
    aadl2::SubprogramGroupType,
)
aadl2::AbstractType_strategy = st.builds(
    aadl2::AbstractType,
)
ComponentImplementation_strategy = st.builds(
    ComponentImplementation,
)
aadl2::ProcessorImplementation_strategy = st.builds(
    aadl2::ProcessorImplementation,
)
aadl2::SystemImplementation_strategy = st.builds(
    aadl2::SystemImplementation,
)
aadl2::BusImplementation_strategy = st.builds(
    aadl2::BusImplementation,
)
aadl2::DataImplementation_strategy = st.builds(
    aadl2::DataImplementation,
)
aadl2::MemoryImplementation_strategy = st.builds(
    aadl2::MemoryImplementation,
)
aadl2::VirtualProcessorImplementation_strategy = st.builds(
    aadl2::VirtualProcessorImplementation,
)
aadl2::VirtualBusImplementation_strategy = st.builds(
    aadl2::VirtualBusImplementation,
)
aadl2::ThreadGroupImplementation_strategy = st.builds(
    aadl2::ThreadGroupImplementation,
)
aadl2::SubprogramGroupImplementation_strategy = st.builds(
    aadl2::SubprogramGroupImplementation,
)
aadl2::ProcessImplementation_strategy = st.builds(
    aadl2::ProcessImplementation,
)
aadl2::DeviceImplementation_strategy = st.builds(
    aadl2::DeviceImplementation,
)
aadl2::BehavioredImplementation_strategy = st.builds(
    aadl2::BehavioredImplementation,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
aadl2::SubprogramCall_strategy = st.builds(
    aadl2::SubprogramCall,
)
aadl2::SubprogramCallSequence_strategy = st.builds(
    aadl2::SubprogramCallSequence,
)
aadl2::FeaturePrototypeActual_strategy = st.builds(
    aadl2::FeaturePrototypeActual,
)
aadl2::ComponentPrototypeActual_strategy = st.builds(
    aadl2::ComponentPrototypeActual,
    category=
        safe_text
)
PrototypeBinding_strategy = st.builds(
    PrototypeBinding,
)
aadl2::FeaturePrototypeBinding_strategy = st.builds(
    aadl2::FeaturePrototypeBinding,
)
aadl2::ComponentPrototypeBinding_strategy = st.builds(
    aadl2::ComponentPrototypeBinding,
)
FeaturePrototypeActual_strategy = st.builds(
    FeaturePrototypeActual,
)
aadl2::FeaturePrototypeReference_strategy = st.builds(
    aadl2::FeaturePrototypeReference,
    out=
        safe_text,
    in_=
        safe_text,
    direction=
        safe_text
)
aadl2::AccessSpecification_strategy = st.builds(
    aadl2::AccessSpecification,
    category=
        safe_text,
    kind=
        safe_text
)
aadl2::PortSpecification_strategy = st.builds(
    aadl2::PortSpecification,
    category=
        safe_text,
    direction=
        safe_text,
    in_=
        safe_text,
    out=
        safe_text
)
aadl2::FeatureGroupPrototypeActual_strategy = st.builds(
    aadl2::FeatureGroupPrototypeActual,
)
aadl2::FeatureGroupPrototypeBinding_strategy = st.builds(
    aadl2::FeatureGroupPrototypeBinding,
)
ModelUnit_strategy = st.builds(
    ModelUnit,
)
aadl2::PropertySet_strategy = st.builds(
    aadl2::PropertySet,
)
aadl2::AadlPackage_strategy = st.builds(
    aadl2::AadlPackage,
)
aadl2::PackageRename_strategy = st.builds(
    aadl2::PackageRename,
    renameAll=
        safe_text
)
aadl2::PackageSection_strategy = st.builds(
    aadl2::PackageSection,
    noAnnexes=
        safe_text,
    noProperties=
        safe_text
)
PackageSection_strategy = st.builds(
    PackageSection,
)
aadl2::PrivatePackageSection_strategy = st.builds(
    aadl2::PrivatePackageSection,
)
aadl2::PublicPackageSection_strategy = st.builds(
    aadl2::PublicPackageSection,
)
aadl2::ModelUnit_strategy = st.builds(
    aadl2::ModelUnit,
)
aadl2::FeatureGroupTypeRename_strategy = st.builds(
    aadl2::FeatureGroupTypeRename,
)
aadl2::ComponentTypeRename_strategy = st.builds(
    aadl2::ComponentTypeRename,
    category=
        safe_text
)
aadl2::Subprogram_strategy = st.builds(
    aadl2::Subprogram,
)
SubprogramSubcomponentType_strategy = st.builds(
    SubprogramSubcomponentType,
)
Subprogram_strategy = st.builds(
    Subprogram,
)
aadl2::SubprogramPrototype_strategy = st.builds(
    aadl2::SubprogramPrototype,
)
aadl2::SubprogramClassifier_strategy = st.builds(
    aadl2::SubprogramClassifier,
)
AnnexSubclause_strategy = st.builds(
    AnnexSubclause,
)
aadl2::DefaultAnnexSubclause_strategy = st.builds(
    aadl2::DefaultAnnexSubclause,
    sourceText=
        safe_text
)
AnnexLibrary_strategy = st.builds(
    AnnexLibrary,
)
aadl2::DefaultAnnexLibrary_strategy = st.builds(
    aadl2::DefaultAnnexLibrary,
    sourceText=
        safe_text
)
aadl2::AnnexLibrary_strategy = st.builds(
    aadl2::AnnexLibrary,
)
InternalFeature_strategy = st.builds(
    InternalFeature,
)
aadl2::EventDataSource_strategy = st.builds(
    aadl2::EventDataSource,
)
aadl2::EventSource_strategy = st.builds(
    aadl2::EventSource,
)
ProcessorFeature_strategy = st.builds(
    ProcessorFeature,
)
aadl2::Data_strategy = st.builds(
    aadl2::Data,
)
DataSubcomponentType_strategy = st.builds(
    DataSubcomponentType,
)
Data_strategy = st.builds(
    Data,
)
aadl2::DataPrototype_strategy = st.builds(
    aadl2::DataPrototype,
)
aadl2::DataClassifier_strategy = st.builds(
    aadl2::DataClassifier,
)
aadl2::Abstract_strategy = st.builds(
    aadl2::Abstract,
)
Abstract_strategy = st.builds(
    Abstract,
)
aadl2::AbstractClassifier_strategy = st.builds(
    aadl2::AbstractClassifier,
)
aadl2::AbstractPrototype_strategy = st.builds(
    aadl2::AbstractPrototype,
)
Subcomponent_strategy = st.builds(
    Subcomponent,
)
aadl2::SystemSubcomponent_strategy = st.builds(
    aadl2::SystemSubcomponent,
)
aadl2::VirtualProcessorSubcomponent_strategy = st.builds(
    aadl2::VirtualProcessorSubcomponent,
)
aadl2::ProcessorSubcomponent_strategy = st.builds(
    aadl2::ProcessorSubcomponent,
)
aadl2::AbstractSubcomponent_strategy = st.builds(
    aadl2::AbstractSubcomponent,
)
aadl2::ProcessSubcomponent_strategy = st.builds(
    aadl2::ProcessSubcomponent,
)
aadl2::MemorySubcomponent_strategy = st.builds(
    aadl2::MemorySubcomponent,
)
aadl2::ThreadGroupSubcomponent_strategy = st.builds(
    aadl2::ThreadGroupSubcomponent,
)
aadl2::ThreadSubcomponent_strategy = st.builds(
    aadl2::ThreadSubcomponent,
)
aadl2::DeviceSubcomponent_strategy = st.builds(
    aadl2::DeviceSubcomponent,
)
Connection_strategy = st.builds(
    Connection,
)
aadl2::AccessConnection_strategy = st.builds(
    aadl2::AccessConnection,
    accessCategory=
        safe_text
)
aadl2::FeatureConnection_strategy = st.builds(
    aadl2::FeatureConnection,
)
aadl2::ParameterConnection_strategy = st.builds(
    aadl2::ParameterConnection,
)
aadl2::PortConnection_strategy = st.builds(
    aadl2::PortConnection,
)
aadl2::FeatureGroupConnection_strategy = st.builds(
    aadl2::FeatureGroupConnection,
)
aadl2::EndToEndFlowSegment_strategy = st.builds(
    aadl2::EndToEndFlowSegment,
)
aadl2::FlowSegment_strategy = st.builds(
    aadl2::FlowSegment,
)
aadl2::ConnectedElement_strategy = st.builds(
    aadl2::ConnectedElement,
)
aadl2::ModeBinding_strategy = st.builds(
    aadl2::ModeBinding,
)
aadl2::FeaturePrototype_strategy = st.builds(
    aadl2::FeaturePrototype,
    out=
        safe_text,
    direction=
        safe_text,
    in_=
        safe_text
)
TriggerPort_strategy = st.builds(
    TriggerPort,
)
aadl2::AbstractFeature_strategy = st.builds(
    aadl2::AbstractFeature,
)
Port_strategy = st.builds(
    Port,
)
aadl2::AccessConnectionEnd_strategy = st.builds(
    aadl2::AccessConnectionEnd,
)
AccessConnectionEnd_strategy = st.builds(
    AccessConnectionEnd,
)
aadl2::SubprogramGroupSubcomponent_strategy = st.builds(
    aadl2::SubprogramGroupSubcomponent,
)
aadl2::BusSubcomponent_strategy = st.builds(
    aadl2::BusSubcomponent,
)
aadl2::SubprogramSubcomponent_strategy = st.builds(
    aadl2::SubprogramSubcomponent,
)
aadl2::SubprogramProxy_strategy = st.builds(
    aadl2::SubprogramProxy,
)
aadl2::VirtualBusSubcomponent_strategy = st.builds(
    aadl2::VirtualBusSubcomponent,
)
aadl2::Access_strategy = st.builds(
    aadl2::Access,
    kind=
        safe_text,
    category=
        safe_text
)
aadl2::BusFeatureClassifier_strategy = st.builds(
    aadl2::BusFeatureClassifier,
)
aadl2::AbstractFeatureClassifier_strategy = st.builds(
    aadl2::AbstractFeatureClassifier,
)
Access_strategy = st.builds(
    Access,
)
aadl2::BusAccess_strategy = st.builds(
    aadl2::BusAccess,
    virtual=
        safe_text
)
AbstractFeatureClassifier_strategy = st.builds(
    AbstractFeatureClassifier,
)
aadl2::BusSubcomponentType_strategy = st.builds(
    aadl2::BusSubcomponentType,
)
aadl2::SubprogramGroupSubcomponentType_strategy = st.builds(
    aadl2::SubprogramGroupSubcomponentType,
)
aadl2::SubprogramSubcomponentType_strategy = st.builds(
    aadl2::SubprogramSubcomponentType,
)
aadl2::VirtualBusSubcomponentType_strategy = st.builds(
    aadl2::VirtualBusSubcomponentType,
)
aadl2::AbstractSubcomponentType_strategy = st.builds(
    aadl2::AbstractSubcomponentType,
)
aadl2::PortConnectionEnd_strategy = st.builds(
    aadl2::PortConnectionEnd,
)
aadl2::ParameterConnectionEnd_strategy = st.builds(
    aadl2::ParameterConnectionEnd,
)
aadl2::DataSubcomponentType_strategy = st.builds(
    aadl2::DataSubcomponentType,
)
PortConnectionEnd_strategy = st.builds(
    PortConnectionEnd,
)
aadl2::PortProxy_strategy = st.builds(
    aadl2::PortProxy,
    direction=
        safe_text,
    in_=
        safe_text,
    out=
        safe_text
)
aadl2::InternalFeature_strategy = st.builds(
    aadl2::InternalFeature,
    direction=
        safe_text,
    out=
        safe_text,
    in_=
        safe_text
)
aadl2::Port_strategy = st.builds(
    aadl2::Port,
    category=
        safe_text
)
ParameterConnectionEnd_strategy = st.builds(
    ParameterConnectionEnd,
)
aadl2::DataSubcomponent_strategy = st.builds(
    aadl2::DataSubcomponent,
)
aadl2::DataPort_strategy = st.builds(
    aadl2::DataPort,
)
aadl2::DataAccess_strategy = st.builds(
    aadl2::DataAccess,
)
aadl2::Parameter_strategy = st.builds(
    aadl2::Parameter,
)
aadl2::EventPort_strategy = st.builds(
    aadl2::EventPort,
)
aadl2::SubprogramGroupAccess_strategy = st.builds(
    aadl2::SubprogramGroupAccess,
)
aadl2::SubprogramAccess_strategy = st.builds(
    aadl2::SubprogramAccess,
)
FeatureType_strategy = st.builds(
    FeatureType,
)
aadl2::FeatureGroupType_strategy = st.builds(
    aadl2::FeatureGroupType,
)
aadl2::FeatureGroupPrototype_strategy = st.builds(
    aadl2::FeatureGroupPrototype,
)
aadl2::FeatureGroupConnectionEnd_strategy = st.builds(
    aadl2::FeatureGroupConnectionEnd,
)
aadl2::EventDataPort_strategy = st.builds(
    aadl2::EventDataPort,
)

@given(instance=NumberType_strategy)
@settings(max_examples=50)
def test_numbertype_instantiation(instance):
    assert isinstance(instance, NumberType)

@given(instance=aadl2::AadlReal_strategy)
@settings(max_examples=50)
def test_aadl2::aadlreal_instantiation(instance):
    assert isinstance(instance, aadl2::AadlReal)

@given(instance=aadl2::AadlInteger_strategy)
@settings(max_examples=50)
def test_aadl2::aadlinteger_instantiation(instance):
    assert isinstance(instance, aadl2::AadlInteger)

@given(instance=NonListType_strategy)
@settings(max_examples=50)
def test_nonlisttype_instantiation(instance):
    assert isinstance(instance, NonListType)

@given(instance=aadl2::AadlString_strategy)
@settings(max_examples=50)
def test_aadl2::aadlstring_instantiation(instance):
    assert isinstance(instance, aadl2::AadlString)

@given(instance=aadl2::ClassifierType_strategy)
@settings(max_examples=50)
def test_aadl2::classifiertype_instantiation(instance):
    assert isinstance(instance, aadl2::ClassifierType)

@given(instance=aadl2::RangeType_strategy)
@settings(max_examples=50)
def test_aadl2::rangetype_instantiation(instance):
    assert isinstance(instance, aadl2::RangeType)

@given(instance=aadl2::NumberType_strategy)
@settings(max_examples=50)
def test_aadl2::numbertype_instantiation(instance):
    assert isinstance(instance, aadl2::NumberType)

@given(instance=aadl2::ReferenceType_strategy)
@settings(max_examples=50)
def test_aadl2::referencetype_instantiation(instance):
    assert isinstance(instance, aadl2::ReferenceType)

@given(instance=aadl2::AadlBoolean_strategy)
@settings(max_examples=50)
def test_aadl2::aadlboolean_instantiation(instance):
    assert isinstance(instance, aadl2::AadlBoolean)

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=aadl2::ListType_strategy)
@settings(max_examples=50)
def test_aadl2::listtype_instantiation(instance):
    assert isinstance(instance, aadl2::ListType)

@given(instance=aadl2::NonListType_strategy)
@settings(max_examples=50)
def test_aadl2::nonlisttype_instantiation(instance):
    assert isinstance(instance, aadl2::NonListType)

@given(instance=EnumerationType_strategy)
@settings(max_examples=50)
def test_enumerationtype_instantiation(instance):
    assert isinstance(instance, EnumerationType)

@given(instance=aadl2::UnitsType_strategy)
@settings(max_examples=50)
def test_aadl2::unitstype_instantiation(instance):
    assert isinstance(instance, aadl2::UnitsType)

@given(instance=NumberValue_strategy)
@settings(max_examples=50)
def test_numbervalue_instantiation(instance):
    assert isinstance(instance, NumberValue)

@given(instance=aadl2::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_aadl2::integerliteral_instantiation(instance):
    assert isinstance(instance, aadl2::IntegerLiteral)

@given(instance=aadl2::IntegerLiteral_strategy)
def test_aadl2::integerliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aadl2::IntegerLiteral_strategy)
def test_aadl2::integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aadl2::IntegerLiteral_strategy)
def test_aadl2::integerliteral_base_type(instance):
    assert isinstance(instance.base, str)


@given(instance=aadl2::IntegerLiteral_strategy)
def test_aadl2::integerliteral_base_setter(instance):
    original = instance.base
    instance.base = original
    assert instance.base == original

@given(instance=ContainedNamedElement_strategy)
@settings(max_examples=50)
def test_containednamedelement_instantiation(instance):
    assert isinstance(instance, ContainedNamedElement)

@given(instance=aadl2::RealLiteral_strategy)
@settings(max_examples=50)
def test_aadl2::realliteral_instantiation(instance):
    assert isinstance(instance, aadl2::RealLiteral)

@given(instance=aadl2::RealLiteral_strategy)
def test_aadl2::realliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aadl2::RealLiteral_strategy)
def test_aadl2::realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=aadl2::UnitLiteral_strategy)
@settings(max_examples=50)
def test_aadl2::unitliteral_instantiation(instance):
    assert isinstance(instance, aadl2::UnitLiteral)

@given(instance=PropertyExpression_strategy)
@settings(max_examples=50)
def test_propertyexpression_instantiation(instance):
    assert isinstance(instance, PropertyExpression)

@given(instance=aadl2::ListValue_strategy)
@settings(max_examples=50)
def test_aadl2::listvalue_instantiation(instance):
    assert isinstance(instance, aadl2::ListValue)

@given(instance=aadl2::Operation_strategy)
@settings(max_examples=50)
def test_aadl2::operation_instantiation(instance):
    assert isinstance(instance, aadl2::Operation)

@given(instance=aadl2::Operation_strategy)
def test_aadl2::operation_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=aadl2::Operation_strategy)
def test_aadl2::operation_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=aadl2::PropertyValue_strategy)
@settings(max_examples=50)
def test_aadl2::propertyvalue_instantiation(instance):
    assert isinstance(instance, aadl2::PropertyValue)

@given(instance=ArraySizeProperty_strategy)
@settings(max_examples=50)
def test_arraysizeproperty_instantiation(instance):
    assert isinstance(instance, ArraySizeProperty)

@given(instance=PropertyValue_strategy)
@settings(max_examples=50)
def test_propertyvalue_instantiation(instance):
    assert isinstance(instance, PropertyValue)

@given(instance=aadl2::NumberValue_strategy)
@settings(max_examples=50)
def test_aadl2::numbervalue_instantiation(instance):
    assert isinstance(instance, aadl2::NumberValue)

@given(instance=aadl2::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_aadl2::booleanliteral_instantiation(instance):
    assert isinstance(instance, aadl2::BooleanLiteral)

@given(instance=aadl2::BooleanLiteral_strategy)
def test_aadl2::booleanliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aadl2::BooleanLiteral_strategy)
def test_aadl2::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aadl2::NamedValue_strategy)
@settings(max_examples=50)
def test_aadl2::namedvalue_instantiation(instance):
    assert isinstance(instance, aadl2::NamedValue)

@given(instance=aadl2::RangeValue_strategy)
@settings(max_examples=50)
def test_aadl2::rangevalue_instantiation(instance):
    assert isinstance(instance, aadl2::RangeValue)

@given(instance=aadl2::ComputedValue_strategy)
@settings(max_examples=50)
def test_aadl2::computedvalue_instantiation(instance):
    assert isinstance(instance, aadl2::ComputedValue)

@given(instance=aadl2::ComputedValue_strategy)
def test_aadl2::computedvalue_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=aadl2::ComputedValue_strategy)
def test_aadl2::computedvalue_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=aadl2::ReferenceValue_strategy)
@settings(max_examples=50)
def test_aadl2::referencevalue_instantiation(instance):
    assert isinstance(instance, aadl2::ReferenceValue)

@given(instance=aadl2::RecordValue_strategy)
@settings(max_examples=50)
def test_aadl2::recordvalue_instantiation(instance):
    assert isinstance(instance, aadl2::RecordValue)

@given(instance=aadl2::StringLiteral_strategy)
@settings(max_examples=50)
def test_aadl2::stringliteral_instantiation(instance):
    assert isinstance(instance, aadl2::StringLiteral)

@given(instance=aadl2::StringLiteral_strategy)
def test_aadl2::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aadl2::StringLiteral_strategy)
def test_aadl2::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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

@given(instance=ProcessClassifier_strategy)
@settings(max_examples=50)
def test_processclassifier_instantiation(instance):
    assert isinstance(instance, ProcessClassifier)

@given(instance=ProcessorClassifier_strategy)
@settings(max_examples=50)
def test_processorclassifier_instantiation(instance):
    assert isinstance(instance, ProcessorClassifier)

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

@given(instance=MemoryClassifier_strategy)
@settings(max_examples=50)
def test_memoryclassifier_instantiation(instance):
    assert isinstance(instance, MemoryClassifier)

@given(instance=Generalization__strategy)
@settings(max_examples=50)
def test_generalization__instantiation(instance):
    assert isinstance(instance, Generalization_)

@given(instance=aadl2::GroupExtension_strategy)
@settings(max_examples=50)
def test_aadl2::groupextension_instantiation(instance):
    assert isinstance(instance, aadl2::GroupExtension)

@given(instance=EndToEndFlowElement_strategy)
@settings(max_examples=50)
def test_endtoendflowelement_instantiation(instance):
    assert isinstance(instance, EndToEndFlowElement)

@given(instance=aadl2::FlowElement_strategy)
@settings(max_examples=50)
def test_aadl2::flowelement_instantiation(instance):
    assert isinstance(instance, aadl2::FlowElement)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=aadl2::DirectedFeature_strategy)
@settings(max_examples=50)
def test_aadl2::directedfeature_instantiation(instance):
    assert isinstance(instance, aadl2::DirectedFeature)

@given(instance=aadl2::DirectedFeature_strategy)
def test_aadl2::directedfeature_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=aadl2::DirectedFeature_strategy)
def test_aadl2::directedfeature_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=aadl2::DirectedFeature_strategy)
def test_aadl2::directedfeature_out_type(instance):
    assert isinstance(instance.out, str)


@given(instance=aadl2::DirectedFeature_strategy)
def test_aadl2::directedfeature_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original

@given(instance=aadl2::DirectedFeature_strategy)
def test_aadl2::directedfeature_in__type(instance):
    assert isinstance(instance.in_, str)


@given(instance=aadl2::DirectedFeature_strategy)
def test_aadl2::directedfeature_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=aadl2::CallContext_strategy)
@settings(max_examples=50)
def test_aadl2::callcontext_instantiation(instance):
    assert isinstance(instance, aadl2::CallContext)

@given(instance=aadl2::FeatureType_strategy)
@settings(max_examples=50)
def test_aadl2::featuretype_instantiation(instance):
    assert isinstance(instance, aadl2::FeatureType)

@given(instance=CallContext_strategy)
@settings(max_examples=50)
def test_callcontext_instantiation(instance):
    assert isinstance(instance, CallContext)

@given(instance=FeatureGroupConnectionEnd_strategy)
@settings(max_examples=50)
def test_featuregroupconnectionend_instantiation(instance):
    assert isinstance(instance, FeatureGroupConnectionEnd)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=DirectedFeature_strategy)
@settings(max_examples=50)
def test_directedfeature_instantiation(instance):
    assert isinstance(instance, DirectedFeature)

@given(instance=FlowElement_strategy)
@settings(max_examples=50)
def test_flowelement_instantiation(instance):
    assert isinstance(instance, FlowElement)

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

@given(instance=ConnectionEnd_strategy)
@settings(max_examples=50)
def test_connectionend_instantiation(instance):
    assert isinstance(instance, ConnectionEnd)

@given(instance=aadl2::FeatureConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2::featureconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2::FeatureConnectionEnd)

@given(instance=Flow_strategy)
@settings(max_examples=50)
def test_flow_instantiation(instance):
    assert isinstance(instance, Flow)

@given(instance=aadl2::FeatureGroup_strategy)
@settings(max_examples=50)
def test_aadl2::featuregroup_instantiation(instance):
    assert isinstance(instance, aadl2::FeatureGroup)

@given(instance=aadl2::FeatureGroup_strategy)
def test_aadl2::featuregroup_inverse_type(instance):
    assert isinstance(instance.inverse, str)


@given(instance=aadl2::FeatureGroup_strategy)
def test_aadl2::featuregroup_inverse_setter(instance):
    original = instance.inverse
    instance.inverse = original
    assert instance.inverse == original

@given(instance=aadl2::TypeExtension_strategy)
@settings(max_examples=50)
def test_aadl2::typeextension_instantiation(instance):
    assert isinstance(instance, aadl2::TypeExtension)

@given(instance=aadl2::FlowSpecification_strategy)
@settings(max_examples=50)
def test_aadl2::flowspecification_instantiation(instance):
    assert isinstance(instance, aadl2::FlowSpecification)

@given(instance=aadl2::FlowSpecification_strategy)
def test_aadl2::flowspecification_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=aadl2::FlowSpecification_strategy)
def test_aadl2::flowspecification_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=ArrayableElement_strategy)
@settings(max_examples=50)
def test_arrayableelement_instantiation(instance):
    assert isinstance(instance, ArrayableElement)

@given(instance=FeatureConnectionEnd_strategy)
@settings(max_examples=50)
def test_featureconnectionend_instantiation(instance):
    assert isinstance(instance, FeatureConnectionEnd)

@given(instance=aadl2::FeatureClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::featureclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::FeatureClassifier)

@given(instance=FeatureClassifier_strategy)
@settings(max_examples=50)
def test_featureclassifier_instantiation(instance):
    assert isinstance(instance, FeatureClassifier)

@given(instance=SubcomponentType_strategy)
@settings(max_examples=50)
def test_subcomponenttype_instantiation(instance):
    assert isinstance(instance, SubcomponentType)

@given(instance=aadl2::ComponentPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::componentprototype_instantiation(instance):
    assert isinstance(instance, aadl2::ComponentPrototype)

@given(instance=aadl2::ComponentPrototype_strategy)
def test_aadl2::componentprototype_array_type(instance):
    assert isinstance(instance.array, str)


@given(instance=aadl2::ComponentPrototype_strategy)
def test_aadl2::componentprototype_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=aadl2::ComponentClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::componentclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::ComponentClassifier)

@given(instance=aadl2::ComponentClassifier_strategy)
def test_aadl2::componentclassifier_derivedModes_type(instance):
    assert isinstance(instance.derivedModes, str)


@given(instance=aadl2::ComponentClassifier_strategy)
def test_aadl2::componentclassifier_derivedModes_setter(instance):
    original = instance.derivedModes
    instance.derivedModes = original
    assert instance.derivedModes == original

@given(instance=aadl2::ComponentClassifier_strategy)
def test_aadl2::componentclassifier_noFlows_type(instance):
    assert isinstance(instance.noFlows, str)


@given(instance=aadl2::ComponentClassifier_strategy)
def test_aadl2::componentclassifier_noFlows_setter(instance):
    original = instance.noFlows
    instance.noFlows = original
    assert instance.noFlows == original

@given(instance=aadl2::ComponentClassifier_strategy)
def test_aadl2::componentclassifier_noModes_type(instance):
    assert isinstance(instance.noModes, str)


@given(instance=aadl2::ComponentClassifier_strategy)
def test_aadl2::componentclassifier_noModes_setter(instance):
    original = instance.noModes
    instance.noModes = original
    assert instance.noModes == original

@given(instance=aadl2::EndToEndFlow_strategy)
@settings(max_examples=50)
def test_aadl2::endtoendflow_instantiation(instance):
    assert isinstance(instance, aadl2::EndToEndFlow)

@given(instance=aadl2::Realization_strategy)
@settings(max_examples=50)
def test_aadl2::realization_instantiation(instance):
    assert isinstance(instance, aadl2::Realization)

@given(instance=aadl2::ImplementationExtension_strategy)
@settings(max_examples=50)
def test_aadl2::implementationextension_instantiation(instance):
    assert isinstance(instance, aadl2::ImplementationExtension)

@given(instance=ComponentClassifier_strategy)
@settings(max_examples=50)
def test_componentclassifier_instantiation(instance):
    assert isinstance(instance, ComponentClassifier)

@given(instance=aadl2::ComponentType_strategy)
@settings(max_examples=50)
def test_aadl2::componenttype_instantiation(instance):
    assert isinstance(instance, aadl2::ComponentType)

@given(instance=aadl2::ComponentType_strategy)
def test_aadl2::componenttype_noFeatures_type(instance):
    assert isinstance(instance.noFeatures, str)


@given(instance=aadl2::ComponentType_strategy)
def test_aadl2::componenttype_noFeatures_setter(instance):
    original = instance.noFeatures
    instance.noFeatures = original
    assert instance.noFeatures == original

@given(instance=aadl2::ComponentImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::componentimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::ComponentImplementation)

@given(instance=aadl2::ComponentImplementation_strategy)
def test_aadl2::componentimplementation_noCalls_type(instance):
    assert isinstance(instance.noCalls, str)


@given(instance=aadl2::ComponentImplementation_strategy)
def test_aadl2::componentimplementation_noCalls_setter(instance):
    original = instance.noCalls
    instance.noCalls = original
    assert instance.noCalls == original

@given(instance=aadl2::ComponentImplementation_strategy)
def test_aadl2::componentimplementation_noConnections_type(instance):
    assert isinstance(instance.noConnections, str)


@given(instance=aadl2::ComponentImplementation_strategy)
def test_aadl2::componentimplementation_noConnections_setter(instance):
    original = instance.noConnections
    instance.noConnections = original
    assert instance.noConnections == original

@given(instance=aadl2::ComponentImplementation_strategy)
def test_aadl2::componentimplementation_noSubcomponents_type(instance):
    assert isinstance(instance.noSubcomponents, str)


@given(instance=aadl2::ComponentImplementation_strategy)
def test_aadl2::componentimplementation_noSubcomponents_setter(instance):
    original = instance.noSubcomponents
    instance.noSubcomponents = original
    assert instance.noSubcomponents == original

@given(instance=aadl2::ArraySizeProperty_strategy)
@settings(max_examples=50)
def test_aadl2::arraysizeproperty_instantiation(instance):
    assert isinstance(instance, aadl2::ArraySizeProperty)

@given(instance=RefinableElement_strategy)
@settings(max_examples=50)
def test_refinableelement_instantiation(instance):
    assert isinstance(instance, RefinableElement)

@given(instance=CalledSubprogram_strategy)
@settings(max_examples=50)
def test_calledsubprogram_instantiation(instance):
    assert isinstance(instance, CalledSubprogram)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=aadl2::Feature_strategy)
@settings(max_examples=50)
def test_aadl2::feature_instantiation(instance):
    assert isinstance(instance, aadl2::Feature)

@given(instance=aadl2::ProcessorFeature_strategy)
@settings(max_examples=50)
def test_aadl2::processorfeature_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessorFeature)

@given(instance=aadl2::FlowFeature_strategy)
@settings(max_examples=50)
def test_aadl2::flowfeature_instantiation(instance):
    assert isinstance(instance, aadl2::FlowFeature)

@given(instance=aadl2::Connection_strategy)
@settings(max_examples=50)
def test_aadl2::connection_instantiation(instance):
    assert isinstance(instance, aadl2::Connection)

@given(instance=aadl2::Connection_strategy)
def test_aadl2::connection_bidirectional_type(instance):
    assert isinstance(instance.bidirectional, str)


@given(instance=aadl2::Connection_strategy)
def test_aadl2::connection_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original

@given(instance=ClassifierFeature_strategy)
@settings(max_examples=50)
def test_classifierfeature_instantiation(instance):
    assert isinstance(instance, ClassifierFeature)

@given(instance=aadl2::FlowImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::flowimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::FlowImplementation)

@given(instance=aadl2::FlowImplementation_strategy)
def test_aadl2::flowimplementation_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=aadl2::FlowImplementation_strategy)
def test_aadl2::flowimplementation_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=aadl2::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_aadl2::behavioralfeature_instantiation(instance):
    assert isinstance(instance, aadl2::BehavioralFeature)

@given(instance=aadl2::StructuralFeature_strategy)
@settings(max_examples=50)
def test_aadl2::structuralfeature_instantiation(instance):
    assert isinstance(instance, aadl2::StructuralFeature)

@given(instance=aadl2::ModeFeature_strategy)
@settings(max_examples=50)
def test_aadl2::modefeature_instantiation(instance):
    assert isinstance(instance, aadl2::ModeFeature)

@given(instance=aadl2::CalledSubprogram_strategy)
@settings(max_examples=50)
def test_aadl2::calledsubprogram_instantiation(instance):
    assert isinstance(instance, aadl2::CalledSubprogram)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=aadl2::DirectedRelationship_strategy)
@settings(max_examples=50)
def test_aadl2::directedrelationship_instantiation(instance):
    assert isinstance(instance, aadl2::DirectedRelationship)

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=ModeFeature_strategy)
@settings(max_examples=50)
def test_modefeature_instantiation(instance):
    assert isinstance(instance, ModeFeature)

@given(instance=aadl2::ModeTransition_strategy)
@settings(max_examples=50)
def test_aadl2::modetransition_instantiation(instance):
    assert isinstance(instance, aadl2::ModeTransition)

@given(instance=aadl2::Mode_strategy)
@settings(max_examples=50)
def test_aadl2::mode_instantiation(instance):
    assert isinstance(instance, aadl2::Mode)

@given(instance=aadl2::Mode_strategy)
def test_aadl2::mode_derived_type(instance):
    assert isinstance(instance.derived, str)


@given(instance=aadl2::Mode_strategy)
def test_aadl2::mode_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=aadl2::Mode_strategy)
def test_aadl2::mode_initial_type(instance):
    assert isinstance(instance.initial, str)


@given(instance=aadl2::Mode_strategy)
def test_aadl2::mode_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=ModalElement_strategy)
@settings(max_examples=50)
def test_modalelement_instantiation(instance):
    assert isinstance(instance, ModalElement)

@given(instance=aadl2::Subcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::subcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::Subcomponent)

@given(instance=aadl2::Subcomponent_strategy)
def test_aadl2::subcomponent_allModes_type(instance):
    assert isinstance(instance.allModes, str)


@given(instance=aadl2::Subcomponent_strategy)
def test_aadl2::subcomponent_allModes_setter(instance):
    original = instance.allModes
    instance.allModes = original
    assert instance.allModes == original

@given(instance=aadl2::ModalPath_strategy)
@settings(max_examples=50)
def test_aadl2::modalpath_instantiation(instance):
    assert isinstance(instance, aadl2::ModalPath)

@given(instance=aadl2::Prototype_strategy)
@settings(max_examples=50)
def test_aadl2::prototype_instantiation(instance):
    assert isinstance(instance, aadl2::Prototype)

@given(instance=aadl2::AnnexSubclause_strategy)
@settings(max_examples=50)
def test_aadl2::annexsubclause_instantiation(instance):
    assert isinstance(instance, aadl2::AnnexSubclause)

@given(instance=aadl2::Generalization__strategy)
@settings(max_examples=50)
def test_aadl2::generalization__instantiation(instance):
    assert isinstance(instance, aadl2::Generalization_)

@given(instance=PropertyOwner_strategy)
@settings(max_examples=50)
def test_propertyowner_instantiation(instance):
    assert isinstance(instance, PropertyOwner)

@given(instance=aadl2::ClassifierValue_strategy)
@settings(max_examples=50)
def test_aadl2::classifiervalue_instantiation(instance):
    assert isinstance(instance, aadl2::ClassifierValue)

@given(instance=aadl2::AbstractNamedValue_strategy)
@settings(max_examples=50)
def test_aadl2::abstractnamedvalue_instantiation(instance):
    assert isinstance(instance, aadl2::AbstractNamedValue)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=aadl2::SubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::subcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::SubcomponentType)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=aadl2::EnumerationType_strategy)
@settings(max_examples=50)
def test_aadl2::enumerationtype_instantiation(instance):
    assert isinstance(instance, aadl2::EnumerationType)

@given(instance=aadl2::RecordType_strategy)
@settings(max_examples=50)
def test_aadl2::recordtype_instantiation(instance):
    assert isinstance(instance, aadl2::RecordType)

@given(instance=aadl2::GlobalNamespace_strategy)
@settings(max_examples=50)
def test_aadl2::globalnamespace_instantiation(instance):
    assert isinstance(instance, aadl2::GlobalNamespace)

@given(instance=aadl2::MetaclassReference_strategy)
@settings(max_examples=50)
def test_aadl2::metaclassreference_instantiation(instance):
    assert isinstance(instance, aadl2::MetaclassReference)

@given(instance=aadl2::MetaclassReference_strategy)
def test_aadl2::metaclassreference_annexName_type(instance):
    assert isinstance(instance.annexName, str)


@given(instance=aadl2::MetaclassReference_strategy)
def test_aadl2::metaclassreference_annexName_setter(instance):
    original = instance.annexName
    instance.annexName = original
    assert instance.annexName == original

@given(instance=aadl2::MetaclassReference_strategy)
def test_aadl2::metaclassreference_metaclassName_type(instance):
    assert isinstance(instance.metaclassName, str)


@given(instance=aadl2::MetaclassReference_strategy)
def test_aadl2::metaclassreference_metaclassName_setter(instance):
    original = instance.metaclassName
    instance.metaclassName = original
    assert instance.metaclassName == original

@given(instance=AbstractNamedValue_strategy)
@settings(max_examples=50)
def test_abstractnamedvalue_instantiation(instance):
    assert isinstance(instance, AbstractNamedValue)

@given(instance=BasicProperty_strategy)
@settings(max_examples=50)
def test_basicproperty_instantiation(instance):
    assert isinstance(instance, BasicProperty)

@given(instance=aadl2::RecordField_strategy)
@settings(max_examples=50)
def test_aadl2::recordfield_instantiation(instance):
    assert isinstance(instance, aadl2::RecordField)

@given(instance=aadl2::ModalPropertyValue_strategy)
@settings(max_examples=50)
def test_aadl2::modalpropertyvalue_instantiation(instance):
    assert isinstance(instance, aadl2::ModalPropertyValue)

@given(instance=aadl2::Classifier_strategy)
@settings(max_examples=50)
def test_aadl2::classifier_instantiation(instance):
    assert isinstance(instance, aadl2::Classifier)

@given(instance=aadl2::Classifier_strategy)
def test_aadl2::classifier_noProperties_type(instance):
    assert isinstance(instance.noProperties, str)


@given(instance=aadl2::Classifier_strategy)
def test_aadl2::classifier_noProperties_setter(instance):
    original = instance.noProperties
    instance.noProperties = original
    assert instance.noProperties == original

@given(instance=aadl2::Classifier_strategy)
def test_aadl2::classifier_noPrototypes_type(instance):
    assert isinstance(instance.noPrototypes, str)


@given(instance=aadl2::Classifier_strategy)
def test_aadl2::classifier_noPrototypes_setter(instance):
    original = instance.noPrototypes
    instance.noPrototypes = original
    assert instance.noPrototypes == original

@given(instance=aadl2::Classifier_strategy)
def test_aadl2::classifier_noAnnexes_type(instance):
    assert isinstance(instance.noAnnexes, str)


@given(instance=aadl2::Classifier_strategy)
def test_aadl2::classifier_noAnnexes_setter(instance):
    original = instance.noAnnexes
    instance.noAnnexes = original
    assert instance.noAnnexes == original

@given(instance=aadl2::PropertyType_strategy)
@settings(max_examples=50)
def test_aadl2::propertytype_instantiation(instance):
    assert isinstance(instance, aadl2::PropertyType)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=aadl2::PropertyConstant_strategy)
@settings(max_examples=50)
def test_aadl2::propertyconstant_instantiation(instance):
    assert isinstance(instance, aadl2::PropertyConstant)

@given(instance=aadl2::BasicProperty_strategy)
@settings(max_examples=50)
def test_aadl2::basicproperty_instantiation(instance):
    assert isinstance(instance, aadl2::BasicProperty)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=aadl2::Namespace_strategy)
@settings(max_examples=50)
def test_aadl2::namespace_instantiation(instance):
    assert isinstance(instance, aadl2::Namespace)

@given(instance=aadl2::TypedElement_strategy)
@settings(max_examples=50)
def test_aadl2::typedelement_instantiation(instance):
    assert isinstance(instance, aadl2::TypedElement)

@given(instance=aadl2::ConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2::connectionend_instantiation(instance):
    assert isinstance(instance, aadl2::ConnectionEnd)

@given(instance=aadl2::ClassifierFeature_strategy)
@settings(max_examples=50)
def test_aadl2::classifierfeature_instantiation(instance):
    assert isinstance(instance, aadl2::ClassifierFeature)

@given(instance=aadl2::TriggerPort_strategy)
@settings(max_examples=50)
def test_aadl2::triggerport_instantiation(instance):
    assert isinstance(instance, aadl2::TriggerPort)

@given(instance=aadl2::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_aadl2::enumerationliteral_instantiation(instance):
    assert isinstance(instance, aadl2::EnumerationLiteral)

@given(instance=aadl2::Context_strategy)
@settings(max_examples=50)
def test_aadl2::context_instantiation(instance):
    assert isinstance(instance, aadl2::Context)

@given(instance=aadl2::EndToEndFlowElement_strategy)
@settings(max_examples=50)
def test_aadl2::endtoendflowelement_instantiation(instance):
    assert isinstance(instance, aadl2::EndToEndFlowElement)

@given(instance=aadl2::RefinableElement_strategy)
@settings(max_examples=50)
def test_aadl2::refinableelement_instantiation(instance):
    assert isinstance(instance, aadl2::RefinableElement)

@given(instance=aadl2::ModalElement_strategy)
@settings(max_examples=50)
def test_aadl2::modalelement_instantiation(instance):
    assert isinstance(instance, aadl2::ModalElement)

@given(instance=aadl2::Flow_strategy)
@settings(max_examples=50)
def test_aadl2::flow_instantiation(instance):
    assert isinstance(instance, aadl2::Flow)

@given(instance=aadl2::Type_strategy)
@settings(max_examples=50)
def test_aadl2::type_instantiation(instance):
    assert isinstance(instance, aadl2::Type)

@given(instance=aadl2::Property_strategy)
@settings(max_examples=50)
def test_aadl2::property_instantiation(instance):
    assert isinstance(instance, aadl2::Property)

@given(instance=aadl2::Property_strategy)
def test_aadl2::property_emptyListDefault_type(instance):
    assert isinstance(instance.emptyListDefault, str)


@given(instance=aadl2::Property_strategy)
def test_aadl2::property_emptyListDefault_setter(instance):
    original = instance.emptyListDefault
    instance.emptyListDefault = original
    assert instance.emptyListDefault == original

@given(instance=aadl2::Property_strategy)
def test_aadl2::property_inherit_type(instance):
    assert isinstance(instance.inherit, str)


@given(instance=aadl2::Property_strategy)
def test_aadl2::property_inherit_setter(instance):
    original = instance.inherit
    instance.inherit = original
    assert instance.inherit == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=aadl2::ContainedNamedElement_strategy)
@settings(max_examples=50)
def test_aadl2::containednamedelement_instantiation(instance):
    assert isinstance(instance, aadl2::ContainedNamedElement)

@given(instance=aadl2::PropertyAssociation_strategy)
@settings(max_examples=50)
def test_aadl2::propertyassociation_instantiation(instance):
    assert isinstance(instance, aadl2::PropertyAssociation)

@given(instance=aadl2::PropertyAssociation_strategy)
def test_aadl2::propertyassociation_constant_type(instance):
    assert isinstance(instance.constant, str)


@given(instance=aadl2::PropertyAssociation_strategy)
def test_aadl2::propertyassociation_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=aadl2::PropertyAssociation_strategy)
def test_aadl2::propertyassociation_append_type(instance):
    assert isinstance(instance.append, str)


@given(instance=aadl2::PropertyAssociation_strategy)
def test_aadl2::propertyassociation_append_setter(instance):
    original = instance.append
    instance.append = original
    assert instance.append == original

@given(instance=aadl2::PropertyExpression_strategy)
@settings(max_examples=50)
def test_aadl2::propertyexpression_instantiation(instance):
    assert isinstance(instance, aadl2::PropertyExpression)

@given(instance=aadl2::ArraySize_strategy)
@settings(max_examples=50)
def test_aadl2::arraysize_instantiation(instance):
    assert isinstance(instance, aadl2::ArraySize)

@given(instance=aadl2::ArraySize_strategy)
def test_aadl2::arraysize_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=aadl2::ArraySize_strategy)
def test_aadl2::arraysize_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=aadl2::NumericRange_strategy)
@settings(max_examples=50)
def test_aadl2::numericrange_instantiation(instance):
    assert isinstance(instance, aadl2::NumericRange)

@given(instance=aadl2::Relationship_strategy)
@settings(max_examples=50)
def test_aadl2::relationship_instantiation(instance):
    assert isinstance(instance, aadl2::Relationship)

@given(instance=aadl2::PropertyOwner_strategy)
@settings(max_examples=50)
def test_aadl2::propertyowner_instantiation(instance):
    assert isinstance(instance, aadl2::PropertyOwner)

@given(instance=aadl2::PrototypeBinding_strategy)
@settings(max_examples=50)
def test_aadl2::prototypebinding_instantiation(instance):
    assert isinstance(instance, aadl2::PrototypeBinding)

@given(instance=aadl2::ContainmentPathElement_strategy)
@settings(max_examples=50)
def test_aadl2::containmentpathelement_instantiation(instance):
    assert isinstance(instance, aadl2::ContainmentPathElement)

@given(instance=aadl2::ContainmentPathElement_strategy)
def test_aadl2::containmentpathelement_annexName_type(instance):
    assert isinstance(instance.annexName, str)


@given(instance=aadl2::ContainmentPathElement_strategy)
def test_aadl2::containmentpathelement_annexName_setter(instance):
    original = instance.annexName
    instance.annexName = original
    assert instance.annexName == original

@given(instance=aadl2::ModeTransitionTrigger_strategy)
@settings(max_examples=50)
def test_aadl2::modetransitiontrigger_instantiation(instance):
    assert isinstance(instance, aadl2::ModeTransitionTrigger)

@given(instance=aadl2::ArrayDimension_strategy)
@settings(max_examples=50)
def test_aadl2::arraydimension_instantiation(instance):
    assert isinstance(instance, aadl2::ArrayDimension)

@given(instance=aadl2::BasicPropertyAssociation_strategy)
@settings(max_examples=50)
def test_aadl2::basicpropertyassociation_instantiation(instance):
    assert isinstance(instance, aadl2::BasicPropertyAssociation)

@given(instance=aadl2::ArrayableElement_strategy)
@settings(max_examples=50)
def test_aadl2::arrayableelement_instantiation(instance):
    assert isinstance(instance, aadl2::ArrayableElement)

@given(instance=aadl2::FlowEnd_strategy)
@settings(max_examples=50)
def test_aadl2::flowend_instantiation(instance):
    assert isinstance(instance, aadl2::FlowEnd)

@given(instance=aadl2::ArrayRange_strategy)
@settings(max_examples=50)
def test_aadl2::arrayrange_instantiation(instance):
    assert isinstance(instance, aadl2::ArrayRange)

@given(instance=aadl2::ArrayRange_strategy)
def test_aadl2::arrayrange_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, str)


@given(instance=aadl2::ArrayRange_strategy)
def test_aadl2::arrayrange_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=aadl2::ArrayRange_strategy)
def test_aadl2::arrayrange_upperBound_type(instance):
    assert isinstance(instance.upperBound, str)


@given(instance=aadl2::ArrayRange_strategy)
def test_aadl2::arrayrange_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=aadl2::NamedElement_strategy)
@settings(max_examples=50)
def test_aadl2::namedelement_instantiation(instance):
    assert isinstance(instance, aadl2::NamedElement)

@given(instance=aadl2::NamedElement_strategy)
def test_aadl2::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aadl2::NamedElement_strategy)
def test_aadl2::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aadl2::NamedElement_strategy)
def test_aadl2::namedelement_qualifiedName_type(instance):
    assert isinstance(instance.qualifiedName, str)


@given(instance=aadl2::NamedElement_strategy)
def test_aadl2::namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2::NamedElement_strategy)
@settings(max_examples=30)
def test_aadl2::namedelement_qualifiedname_changes_state(instance):
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
        assert has_statements, f"Function 'qualifiedName' in aadl2::NamedElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'qualifiedName' in aadl2::NamedElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'qualifiedName' in aadl2::NamedElement is not implemented or raised an error")

@given(instance=aadl2::ComponentImplementationReference_strategy)
@settings(max_examples=50)
def test_aadl2::componentimplementationreference_instantiation(instance):
    assert isinstance(instance, aadl2::ComponentImplementationReference)

@given(instance=aadl2::Comment_strategy)
@settings(max_examples=50)
def test_aadl2::comment_instantiation(instance):
    assert isinstance(instance, aadl2::Comment)

@given(instance=aadl2::Comment_strategy)
def test_aadl2::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=aadl2::Comment_strategy)
def test_aadl2::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=aadl2::Element_strategy)
@settings(max_examples=50)
def test_aadl2::element_instantiation(instance):
    assert isinstance(instance, aadl2::Element)

@given(instance=DeviceClassifier_strategy)
@settings(max_examples=50)
def test_deviceclassifier_instantiation(instance):
    assert isinstance(instance, DeviceClassifier)

@given(instance=DataClassifier_strategy)
@settings(max_examples=50)
def test_dataclassifier_instantiation(instance):
    assert isinstance(instance, DataClassifier)

@given(instance=ComponentPrototype_strategy)
@settings(max_examples=50)
def test_componentprototype_instantiation(instance):
    assert isinstance(instance, ComponentPrototype)

@given(instance=aadl2::VirtualProcessor_strategy)
@settings(max_examples=50)
def test_aadl2::virtualprocessor_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualProcessor)

@given(instance=BusClassifier_strategy)
@settings(max_examples=50)
def test_busclassifier_instantiation(instance):
    assert isinstance(instance, BusClassifier)

@given(instance=Thread_strategy)
@settings(max_examples=50)
def test_thread_instantiation(instance):
    assert isinstance(instance, Thread)

@given(instance=VirtualProcessor_strategy)
@settings(max_examples=50)
def test_virtualprocessor_instantiation(instance):
    assert isinstance(instance, VirtualProcessor)

@given(instance=aadl2::VirtualBus_strategy)
@settings(max_examples=50)
def test_aadl2::virtualbus_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualBus)

@given(instance=VirtualBus_strategy)
@settings(max_examples=50)
def test_virtualbus_instantiation(instance):
    assert isinstance(instance, VirtualBus)

@given(instance=aadl2::ThreadGroup_strategy)
@settings(max_examples=50)
def test_aadl2::threadgroup_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadGroup)

@given(instance=ThreadGroup_strategy)
@settings(max_examples=50)
def test_threadgroup_instantiation(instance):
    assert isinstance(instance, ThreadGroup)

@given(instance=aadl2::Thread_strategy)
@settings(max_examples=50)
def test_aadl2::thread_instantiation(instance):
    assert isinstance(instance, aadl2::Thread)

@given(instance=Processor_strategy)
@settings(max_examples=50)
def test_processor_instantiation(instance):
    assert isinstance(instance, Processor)

@given(instance=aadl2::Process_strategy)
@settings(max_examples=50)
def test_aadl2::process_instantiation(instance):
    assert isinstance(instance, aadl2::Process)

@given(instance=aadl2::SubprogramGroup_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramgroup_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramGroup)

@given(instance=SubprogramGroup_strategy)
@settings(max_examples=50)
def test_subprogramgroup_instantiation(instance):
    assert isinstance(instance, SubprogramGroup)

@given(instance=aadl2::System_strategy)
@settings(max_examples=50)
def test_aadl2::system_instantiation(instance):
    assert isinstance(instance, aadl2::System)

@given(instance=System_strategy)
@settings(max_examples=50)
def test_system_instantiation(instance):
    assert isinstance(instance, System)

@given(instance=aadl2::Processor_strategy)
@settings(max_examples=50)
def test_aadl2::processor_instantiation(instance):
    assert isinstance(instance, aadl2::Processor)

@given(instance=aadl2::Bus_strategy)
@settings(max_examples=50)
def test_aadl2::bus_instantiation(instance):
    assert isinstance(instance, aadl2::Bus)

@given(instance=Process_strategy)
@settings(max_examples=50)
def test_process_instantiation(instance):
    assert isinstance(instance, Process)

@given(instance=aadl2::Memory_strategy)
@settings(max_examples=50)
def test_aadl2::memory_instantiation(instance):
    assert isinstance(instance, aadl2::Memory)

@given(instance=Memory_strategy)
@settings(max_examples=50)
def test_memory_instantiation(instance):
    assert isinstance(instance, Memory)

@given(instance=aadl2::Device_strategy)
@settings(max_examples=50)
def test_aadl2::device_instantiation(instance):
    assert isinstance(instance, aadl2::Device)

@given(instance=Device_strategy)
@settings(max_examples=50)
def test_device_instantiation(instance):
    assert isinstance(instance, Device)

@given(instance=Bus_strategy)
@settings(max_examples=50)
def test_bus_instantiation(instance):
    assert isinstance(instance, Bus)

@given(instance=aadl2::ProcessorSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::processorsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessorSubcomponentType)

@given(instance=BehavioredImplementation_strategy)
@settings(max_examples=50)
def test_behavioredimplementation_instantiation(instance):
    assert isinstance(instance, BehavioredImplementation)

@given(instance=aadl2::ThreadImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::threadimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadImplementation)

@given(instance=aadl2::SubprogramImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramImplementation)

@given(instance=aadl2::DeviceSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::devicesubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::DeviceSubcomponentType)

@given(instance=aadl2::MemorySubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::memorysubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::MemorySubcomponentType)

@given(instance=aadl2::ProcessSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::processsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessSubcomponentType)

@given(instance=aadl2::SystemSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::systemsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::SystemSubcomponentType)

@given(instance=aadl2::ThreadSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::threadsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadSubcomponentType)

@given(instance=aadl2::ThreadGroupSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::threadgroupsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadGroupSubcomponentType)

@given(instance=BusFeatureClassifier_strategy)
@settings(max_examples=50)
def test_busfeatureclassifier_instantiation(instance):
    assert isinstance(instance, BusFeatureClassifier)

@given(instance=aadl2::VirtualProcessorSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::virtualprocessorsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualProcessorSubcomponentType)

@given(instance=VirtualProcessorSubcomponentType_strategy)
@settings(max_examples=50)
def test_virtualprocessorsubcomponenttype_instantiation(instance):
    assert isinstance(instance, VirtualProcessorSubcomponentType)

@given(instance=aadl2::VirtualProcessorClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::virtualprocessorclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualProcessorClassifier)

@given(instance=aadl2::VirtualProcessorPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::virtualprocessorprototype_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualProcessorPrototype)

@given(instance=VirtualBusSubcomponentType_strategy)
@settings(max_examples=50)
def test_virtualbussubcomponenttype_instantiation(instance):
    assert isinstance(instance, VirtualBusSubcomponentType)

@given(instance=aadl2::VirtualBusPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::virtualbusprototype_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualBusPrototype)

@given(instance=aadl2::VirtualBusClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::virtualbusclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualBusClassifier)

@given(instance=ThreadSubcomponentType_strategy)
@settings(max_examples=50)
def test_threadsubcomponenttype_instantiation(instance):
    assert isinstance(instance, ThreadSubcomponentType)

@given(instance=aadl2::ThreadPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::threadprototype_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadPrototype)

@given(instance=aadl2::ThreadClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::threadclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadClassifier)

@given(instance=ThreadGroupSubcomponentType_strategy)
@settings(max_examples=50)
def test_threadgroupsubcomponenttype_instantiation(instance):
    assert isinstance(instance, ThreadGroupSubcomponentType)

@given(instance=aadl2::ThreadGroupPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::threadgroupprototype_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadGroupPrototype)

@given(instance=aadl2::ThreadGroupClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::threadgroupclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadGroupClassifier)

@given(instance=SystemSubcomponentType_strategy)
@settings(max_examples=50)
def test_systemsubcomponenttype_instantiation(instance):
    assert isinstance(instance, SystemSubcomponentType)

@given(instance=aadl2::SystemPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::systemprototype_instantiation(instance):
    assert isinstance(instance, aadl2::SystemPrototype)

@given(instance=aadl2::SystemClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::systemclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::SystemClassifier)

@given(instance=SubprogramGroupSubcomponentType_strategy)
@settings(max_examples=50)
def test_subprogramgroupsubcomponenttype_instantiation(instance):
    assert isinstance(instance, SubprogramGroupSubcomponentType)

@given(instance=aadl2::SubprogramGroupClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramgroupclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramGroupClassifier)

@given(instance=aadl2::SubprogramGroupPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramgroupprototype_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramGroupPrototype)

@given(instance=ProcessSubcomponentType_strategy)
@settings(max_examples=50)
def test_processsubcomponenttype_instantiation(instance):
    assert isinstance(instance, ProcessSubcomponentType)

@given(instance=aadl2::ProcessPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::processprototype_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessPrototype)

@given(instance=aadl2::ProcessClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::processclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessClassifier)

@given(instance=ProcessorSubcomponentType_strategy)
@settings(max_examples=50)
def test_processorsubcomponenttype_instantiation(instance):
    assert isinstance(instance, ProcessorSubcomponentType)

@given(instance=aadl2::ProcessorClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::processorclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessorClassifier)

@given(instance=aadl2::ProcessorPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::processorprototype_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessorPrototype)

@given(instance=MemorySubcomponentType_strategy)
@settings(max_examples=50)
def test_memorysubcomponenttype_instantiation(instance):
    assert isinstance(instance, MemorySubcomponentType)

@given(instance=aadl2::MemoryClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::memoryclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::MemoryClassifier)

@given(instance=aadl2::MemoryPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::memoryprototype_instantiation(instance):
    assert isinstance(instance, aadl2::MemoryPrototype)

@given(instance=DeviceSubcomponentType_strategy)
@settings(max_examples=50)
def test_devicesubcomponenttype_instantiation(instance):
    assert isinstance(instance, DeviceSubcomponentType)

@given(instance=aadl2::DeviceClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::deviceclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::DeviceClassifier)

@given(instance=aadl2::DevicePrototype_strategy)
@settings(max_examples=50)
def test_aadl2::deviceprototype_instantiation(instance):
    assert isinstance(instance, aadl2::DevicePrototype)

@given(instance=BusSubcomponentType_strategy)
@settings(max_examples=50)
def test_bussubcomponenttype_instantiation(instance):
    assert isinstance(instance, BusSubcomponentType)

@given(instance=aadl2::BusPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::busprototype_instantiation(instance):
    assert isinstance(instance, aadl2::BusPrototype)

@given(instance=aadl2::BusClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::busclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::BusClassifier)

@given(instance=AbstractSubcomponentType_strategy)
@settings(max_examples=50)
def test_abstractsubcomponenttype_instantiation(instance):
    assert isinstance(instance, AbstractSubcomponentType)

@given(instance=AbstractClassifier_strategy)
@settings(max_examples=50)
def test_abstractclassifier_instantiation(instance):
    assert isinstance(instance, AbstractClassifier)

@given(instance=aadl2::AbstractImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::abstractimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::AbstractImplementation)

@given(instance=ComponentType_strategy)
@settings(max_examples=50)
def test_componenttype_instantiation(instance):
    assert isinstance(instance, ComponentType)

@given(instance=aadl2::MemoryType_strategy)
@settings(max_examples=50)
def test_aadl2::memorytype_instantiation(instance):
    assert isinstance(instance, aadl2::MemoryType)

@given(instance=aadl2::ThreadGroupType_strategy)
@settings(max_examples=50)
def test_aadl2::threadgrouptype_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadGroupType)

@given(instance=aadl2::VirtualProcessorType_strategy)
@settings(max_examples=50)
def test_aadl2::virtualprocessortype_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualProcessorType)

@given(instance=aadl2::BusType_strategy)
@settings(max_examples=50)
def test_aadl2::bustype_instantiation(instance):
    assert isinstance(instance, aadl2::BusType)

@given(instance=aadl2::DataType_strategy)
@settings(max_examples=50)
def test_aadl2::datatype_instantiation(instance):
    assert isinstance(instance, aadl2::DataType)

@given(instance=aadl2::ProcessType_strategy)
@settings(max_examples=50)
def test_aadl2::processtype_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessType)

@given(instance=aadl2::SubprogramType_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramtype_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramType)

@given(instance=aadl2::ThreadType_strategy)
@settings(max_examples=50)
def test_aadl2::threadtype_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadType)

@given(instance=aadl2::DeviceType_strategy)
@settings(max_examples=50)
def test_aadl2::devicetype_instantiation(instance):
    assert isinstance(instance, aadl2::DeviceType)

@given(instance=aadl2::VirtualBusType_strategy)
@settings(max_examples=50)
def test_aadl2::virtualbustype_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualBusType)

@given(instance=aadl2::ProcessorType_strategy)
@settings(max_examples=50)
def test_aadl2::processortype_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessorType)

@given(instance=aadl2::SystemType_strategy)
@settings(max_examples=50)
def test_aadl2::systemtype_instantiation(instance):
    assert isinstance(instance, aadl2::SystemType)

@given(instance=aadl2::SubprogramGroupType_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramgrouptype_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramGroupType)

@given(instance=aadl2::AbstractType_strategy)
@settings(max_examples=50)
def test_aadl2::abstracttype_instantiation(instance):
    assert isinstance(instance, aadl2::AbstractType)

@given(instance=ComponentImplementation_strategy)
@settings(max_examples=50)
def test_componentimplementation_instantiation(instance):
    assert isinstance(instance, ComponentImplementation)

@given(instance=aadl2::ProcessorImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::processorimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessorImplementation)

@given(instance=aadl2::SystemImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::systemimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::SystemImplementation)

@given(instance=aadl2::BusImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::busimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::BusImplementation)

@given(instance=aadl2::DataImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::dataimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::DataImplementation)

@given(instance=aadl2::MemoryImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::memoryimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::MemoryImplementation)

@given(instance=aadl2::VirtualProcessorImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::virtualprocessorimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualProcessorImplementation)

@given(instance=aadl2::VirtualBusImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::virtualbusimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualBusImplementation)

@given(instance=aadl2::ThreadGroupImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::threadgroupimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadGroupImplementation)

@given(instance=aadl2::SubprogramGroupImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramgroupimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramGroupImplementation)

@given(instance=aadl2::ProcessImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::processimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessImplementation)

@given(instance=aadl2::DeviceImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::deviceimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::DeviceImplementation)

@given(instance=aadl2::BehavioredImplementation_strategy)
@settings(max_examples=50)
def test_aadl2::behavioredimplementation_instantiation(instance):
    assert isinstance(instance, aadl2::BehavioredImplementation)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=aadl2::BehavioredImplementation_strategy)
@settings(max_examples=30)
def test_aadl2::behavioredimplementation_subprogramcalls_changes_state(instance):
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
        assert has_statements, f"Function 'subprogramCalls' in aadl2::BehavioredImplementation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'subprogramCalls' in aadl2::BehavioredImplementation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'subprogramCalls' in aadl2::BehavioredImplementation is not implemented or raised an error")

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=aadl2::SubprogramCall_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramcall_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramCall)

@given(instance=aadl2::SubprogramCallSequence_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramcallsequence_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramCallSequence)

@given(instance=aadl2::FeaturePrototypeActual_strategy)
@settings(max_examples=50)
def test_aadl2::featureprototypeactual_instantiation(instance):
    assert isinstance(instance, aadl2::FeaturePrototypeActual)

@given(instance=aadl2::ComponentPrototypeActual_strategy)
@settings(max_examples=50)
def test_aadl2::componentprototypeactual_instantiation(instance):
    assert isinstance(instance, aadl2::ComponentPrototypeActual)

@given(instance=aadl2::ComponentPrototypeActual_strategy)
def test_aadl2::componentprototypeactual_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=aadl2::ComponentPrototypeActual_strategy)
def test_aadl2::componentprototypeactual_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=PrototypeBinding_strategy)
@settings(max_examples=50)
def test_prototypebinding_instantiation(instance):
    assert isinstance(instance, PrototypeBinding)

@given(instance=aadl2::FeaturePrototypeBinding_strategy)
@settings(max_examples=50)
def test_aadl2::featureprototypebinding_instantiation(instance):
    assert isinstance(instance, aadl2::FeaturePrototypeBinding)

@given(instance=aadl2::ComponentPrototypeBinding_strategy)
@settings(max_examples=50)
def test_aadl2::componentprototypebinding_instantiation(instance):
    assert isinstance(instance, aadl2::ComponentPrototypeBinding)

@given(instance=FeaturePrototypeActual_strategy)
@settings(max_examples=50)
def test_featureprototypeactual_instantiation(instance):
    assert isinstance(instance, FeaturePrototypeActual)

@given(instance=aadl2::FeaturePrototypeReference_strategy)
@settings(max_examples=50)
def test_aadl2::featureprototypereference_instantiation(instance):
    assert isinstance(instance, aadl2::FeaturePrototypeReference)

@given(instance=aadl2::FeaturePrototypeReference_strategy)
def test_aadl2::featureprototypereference_out_type(instance):
    assert isinstance(instance.out, str)


@given(instance=aadl2::FeaturePrototypeReference_strategy)
def test_aadl2::featureprototypereference_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original

@given(instance=aadl2::FeaturePrototypeReference_strategy)
def test_aadl2::featureprototypereference_in__type(instance):
    assert isinstance(instance.in_, str)


@given(instance=aadl2::FeaturePrototypeReference_strategy)
def test_aadl2::featureprototypereference_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=aadl2::FeaturePrototypeReference_strategy)
def test_aadl2::featureprototypereference_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=aadl2::FeaturePrototypeReference_strategy)
def test_aadl2::featureprototypereference_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=aadl2::AccessSpecification_strategy)
@settings(max_examples=50)
def test_aadl2::accessspecification_instantiation(instance):
    assert isinstance(instance, aadl2::AccessSpecification)

@given(instance=aadl2::AccessSpecification_strategy)
def test_aadl2::accessspecification_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=aadl2::AccessSpecification_strategy)
def test_aadl2::accessspecification_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=aadl2::AccessSpecification_strategy)
def test_aadl2::accessspecification_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=aadl2::AccessSpecification_strategy)
def test_aadl2::accessspecification_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=aadl2::PortSpecification_strategy)
@settings(max_examples=50)
def test_aadl2::portspecification_instantiation(instance):
    assert isinstance(instance, aadl2::PortSpecification)

@given(instance=aadl2::PortSpecification_strategy)
def test_aadl2::portspecification_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=aadl2::PortSpecification_strategy)
def test_aadl2::portspecification_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=aadl2::PortSpecification_strategy)
def test_aadl2::portspecification_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=aadl2::PortSpecification_strategy)
def test_aadl2::portspecification_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=aadl2::PortSpecification_strategy)
def test_aadl2::portspecification_in__type(instance):
    assert isinstance(instance.in_, str)


@given(instance=aadl2::PortSpecification_strategy)
def test_aadl2::portspecification_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=aadl2::PortSpecification_strategy)
def test_aadl2::portspecification_out_type(instance):
    assert isinstance(instance.out, str)


@given(instance=aadl2::PortSpecification_strategy)
def test_aadl2::portspecification_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original

@given(instance=aadl2::FeatureGroupPrototypeActual_strategy)
@settings(max_examples=50)
def test_aadl2::featuregroupprototypeactual_instantiation(instance):
    assert isinstance(instance, aadl2::FeatureGroupPrototypeActual)

@given(instance=aadl2::FeatureGroupPrototypeBinding_strategy)
@settings(max_examples=50)
def test_aadl2::featuregroupprototypebinding_instantiation(instance):
    assert isinstance(instance, aadl2::FeatureGroupPrototypeBinding)

@given(instance=ModelUnit_strategy)
@settings(max_examples=50)
def test_modelunit_instantiation(instance):
    assert isinstance(instance, ModelUnit)

@given(instance=aadl2::PropertySet_strategy)
@settings(max_examples=50)
def test_aadl2::propertyset_instantiation(instance):
    assert isinstance(instance, aadl2::PropertySet)

@given(instance=aadl2::AadlPackage_strategy)
@settings(max_examples=50)
def test_aadl2::aadlpackage_instantiation(instance):
    assert isinstance(instance, aadl2::AadlPackage)

@given(instance=aadl2::PackageRename_strategy)
@settings(max_examples=50)
def test_aadl2::packagerename_instantiation(instance):
    assert isinstance(instance, aadl2::PackageRename)

@given(instance=aadl2::PackageRename_strategy)
def test_aadl2::packagerename_renameAll_type(instance):
    assert isinstance(instance.renameAll, str)


@given(instance=aadl2::PackageRename_strategy)
def test_aadl2::packagerename_renameAll_setter(instance):
    original = instance.renameAll
    instance.renameAll = original
    assert instance.renameAll == original

@given(instance=aadl2::PackageSection_strategy)
@settings(max_examples=50)
def test_aadl2::packagesection_instantiation(instance):
    assert isinstance(instance, aadl2::PackageSection)

@given(instance=aadl2::PackageSection_strategy)
def test_aadl2::packagesection_noAnnexes_type(instance):
    assert isinstance(instance.noAnnexes, str)


@given(instance=aadl2::PackageSection_strategy)
def test_aadl2::packagesection_noAnnexes_setter(instance):
    original = instance.noAnnexes
    instance.noAnnexes = original
    assert instance.noAnnexes == original

@given(instance=aadl2::PackageSection_strategy)
def test_aadl2::packagesection_noProperties_type(instance):
    assert isinstance(instance.noProperties, str)


@given(instance=aadl2::PackageSection_strategy)
def test_aadl2::packagesection_noProperties_setter(instance):
    original = instance.noProperties
    instance.noProperties = original
    assert instance.noProperties == original

@given(instance=PackageSection_strategy)
@settings(max_examples=50)
def test_packagesection_instantiation(instance):
    assert isinstance(instance, PackageSection)

@given(instance=aadl2::PrivatePackageSection_strategy)
@settings(max_examples=50)
def test_aadl2::privatepackagesection_instantiation(instance):
    assert isinstance(instance, aadl2::PrivatePackageSection)

@given(instance=aadl2::PublicPackageSection_strategy)
@settings(max_examples=50)
def test_aadl2::publicpackagesection_instantiation(instance):
    assert isinstance(instance, aadl2::PublicPackageSection)

@given(instance=aadl2::ModelUnit_strategy)
@settings(max_examples=50)
def test_aadl2::modelunit_instantiation(instance):
    assert isinstance(instance, aadl2::ModelUnit)

@given(instance=aadl2::FeatureGroupTypeRename_strategy)
@settings(max_examples=50)
def test_aadl2::featuregrouptyperename_instantiation(instance):
    assert isinstance(instance, aadl2::FeatureGroupTypeRename)

@given(instance=aadl2::ComponentTypeRename_strategy)
@settings(max_examples=50)
def test_aadl2::componenttyperename_instantiation(instance):
    assert isinstance(instance, aadl2::ComponentTypeRename)

@given(instance=aadl2::ComponentTypeRename_strategy)
def test_aadl2::componenttyperename_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=aadl2::ComponentTypeRename_strategy)
def test_aadl2::componenttyperename_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=aadl2::Subprogram_strategy)
@settings(max_examples=50)
def test_aadl2::subprogram_instantiation(instance):
    assert isinstance(instance, aadl2::Subprogram)

@given(instance=SubprogramSubcomponentType_strategy)
@settings(max_examples=50)
def test_subprogramsubcomponenttype_instantiation(instance):
    assert isinstance(instance, SubprogramSubcomponentType)

@given(instance=Subprogram_strategy)
@settings(max_examples=50)
def test_subprogram_instantiation(instance):
    assert isinstance(instance, Subprogram)

@given(instance=aadl2::SubprogramPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramprototype_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramPrototype)

@given(instance=aadl2::SubprogramClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramClassifier)

@given(instance=AnnexSubclause_strategy)
@settings(max_examples=50)
def test_annexsubclause_instantiation(instance):
    assert isinstance(instance, AnnexSubclause)

@given(instance=aadl2::DefaultAnnexSubclause_strategy)
@settings(max_examples=50)
def test_aadl2::defaultannexsubclause_instantiation(instance):
    assert isinstance(instance, aadl2::DefaultAnnexSubclause)

@given(instance=aadl2::DefaultAnnexSubclause_strategy)
def test_aadl2::defaultannexsubclause_sourceText_type(instance):
    assert isinstance(instance.sourceText, str)


@given(instance=aadl2::DefaultAnnexSubclause_strategy)
def test_aadl2::defaultannexsubclause_sourceText_setter(instance):
    original = instance.sourceText
    instance.sourceText = original
    assert instance.sourceText == original

@given(instance=AnnexLibrary_strategy)
@settings(max_examples=50)
def test_annexlibrary_instantiation(instance):
    assert isinstance(instance, AnnexLibrary)

@given(instance=aadl2::DefaultAnnexLibrary_strategy)
@settings(max_examples=50)
def test_aadl2::defaultannexlibrary_instantiation(instance):
    assert isinstance(instance, aadl2::DefaultAnnexLibrary)

@given(instance=aadl2::DefaultAnnexLibrary_strategy)
def test_aadl2::defaultannexlibrary_sourceText_type(instance):
    assert isinstance(instance.sourceText, str)


@given(instance=aadl2::DefaultAnnexLibrary_strategy)
def test_aadl2::defaultannexlibrary_sourceText_setter(instance):
    original = instance.sourceText
    instance.sourceText = original
    assert instance.sourceText == original

@given(instance=aadl2::AnnexLibrary_strategy)
@settings(max_examples=50)
def test_aadl2::annexlibrary_instantiation(instance):
    assert isinstance(instance, aadl2::AnnexLibrary)

@given(instance=InternalFeature_strategy)
@settings(max_examples=50)
def test_internalfeature_instantiation(instance):
    assert isinstance(instance, InternalFeature)

@given(instance=aadl2::EventDataSource_strategy)
@settings(max_examples=50)
def test_aadl2::eventdatasource_instantiation(instance):
    assert isinstance(instance, aadl2::EventDataSource)

@given(instance=aadl2::EventSource_strategy)
@settings(max_examples=50)
def test_aadl2::eventsource_instantiation(instance):
    assert isinstance(instance, aadl2::EventSource)

@given(instance=ProcessorFeature_strategy)
@settings(max_examples=50)
def test_processorfeature_instantiation(instance):
    assert isinstance(instance, ProcessorFeature)

@given(instance=aadl2::Data_strategy)
@settings(max_examples=50)
def test_aadl2::data_instantiation(instance):
    assert isinstance(instance, aadl2::Data)

@given(instance=DataSubcomponentType_strategy)
@settings(max_examples=50)
def test_datasubcomponenttype_instantiation(instance):
    assert isinstance(instance, DataSubcomponentType)

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=aadl2::DataPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::dataprototype_instantiation(instance):
    assert isinstance(instance, aadl2::DataPrototype)

@given(instance=aadl2::DataClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::dataclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::DataClassifier)

@given(instance=aadl2::Abstract_strategy)
@settings(max_examples=50)
def test_aadl2::abstract_instantiation(instance):
    assert isinstance(instance, aadl2::Abstract)

@given(instance=Abstract_strategy)
@settings(max_examples=50)
def test_abstract_instantiation(instance):
    assert isinstance(instance, Abstract)

@given(instance=aadl2::AbstractClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::abstractclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::AbstractClassifier)

@given(instance=aadl2::AbstractPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::abstractprototype_instantiation(instance):
    assert isinstance(instance, aadl2::AbstractPrototype)

@given(instance=Subcomponent_strategy)
@settings(max_examples=50)
def test_subcomponent_instantiation(instance):
    assert isinstance(instance, Subcomponent)

@given(instance=aadl2::SystemSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::systemsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::SystemSubcomponent)

@given(instance=aadl2::VirtualProcessorSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::virtualprocessorsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualProcessorSubcomponent)

@given(instance=aadl2::ProcessorSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::processorsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessorSubcomponent)

@given(instance=aadl2::AbstractSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::abstractsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::AbstractSubcomponent)

@given(instance=aadl2::ProcessSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::processsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::ProcessSubcomponent)

@given(instance=aadl2::MemorySubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::memorysubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::MemorySubcomponent)

@given(instance=aadl2::ThreadGroupSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::threadgroupsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadGroupSubcomponent)

@given(instance=aadl2::ThreadSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::threadsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::ThreadSubcomponent)

@given(instance=aadl2::DeviceSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::devicesubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::DeviceSubcomponent)

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=aadl2::AccessConnection_strategy)
@settings(max_examples=50)
def test_aadl2::accessconnection_instantiation(instance):
    assert isinstance(instance, aadl2::AccessConnection)

@given(instance=aadl2::AccessConnection_strategy)
def test_aadl2::accessconnection_accessCategory_type(instance):
    assert isinstance(instance.accessCategory, str)


@given(instance=aadl2::AccessConnection_strategy)
def test_aadl2::accessconnection_accessCategory_setter(instance):
    original = instance.accessCategory
    instance.accessCategory = original
    assert instance.accessCategory == original

@given(instance=aadl2::FeatureConnection_strategy)
@settings(max_examples=50)
def test_aadl2::featureconnection_instantiation(instance):
    assert isinstance(instance, aadl2::FeatureConnection)

@given(instance=aadl2::ParameterConnection_strategy)
@settings(max_examples=50)
def test_aadl2::parameterconnection_instantiation(instance):
    assert isinstance(instance, aadl2::ParameterConnection)

@given(instance=aadl2::PortConnection_strategy)
@settings(max_examples=50)
def test_aadl2::portconnection_instantiation(instance):
    assert isinstance(instance, aadl2::PortConnection)

@given(instance=aadl2::FeatureGroupConnection_strategy)
@settings(max_examples=50)
def test_aadl2::featuregroupconnection_instantiation(instance):
    assert isinstance(instance, aadl2::FeatureGroupConnection)

@given(instance=aadl2::EndToEndFlowSegment_strategy)
@settings(max_examples=50)
def test_aadl2::endtoendflowsegment_instantiation(instance):
    assert isinstance(instance, aadl2::EndToEndFlowSegment)

@given(instance=aadl2::FlowSegment_strategy)
@settings(max_examples=50)
def test_aadl2::flowsegment_instantiation(instance):
    assert isinstance(instance, aadl2::FlowSegment)

@given(instance=aadl2::ConnectedElement_strategy)
@settings(max_examples=50)
def test_aadl2::connectedelement_instantiation(instance):
    assert isinstance(instance, aadl2::ConnectedElement)

@given(instance=aadl2::ModeBinding_strategy)
@settings(max_examples=50)
def test_aadl2::modebinding_instantiation(instance):
    assert isinstance(instance, aadl2::ModeBinding)

@given(instance=aadl2::FeaturePrototype_strategy)
@settings(max_examples=50)
def test_aadl2::featureprototype_instantiation(instance):
    assert isinstance(instance, aadl2::FeaturePrototype)

@given(instance=aadl2::FeaturePrototype_strategy)
def test_aadl2::featureprototype_out_type(instance):
    assert isinstance(instance.out, str)


@given(instance=aadl2::FeaturePrototype_strategy)
def test_aadl2::featureprototype_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original

@given(instance=aadl2::FeaturePrototype_strategy)
def test_aadl2::featureprototype_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=aadl2::FeaturePrototype_strategy)
def test_aadl2::featureprototype_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=aadl2::FeaturePrototype_strategy)
def test_aadl2::featureprototype_in__type(instance):
    assert isinstance(instance.in_, str)


@given(instance=aadl2::FeaturePrototype_strategy)
def test_aadl2::featureprototype_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=TriggerPort_strategy)
@settings(max_examples=50)
def test_triggerport_instantiation(instance):
    assert isinstance(instance, TriggerPort)

@given(instance=aadl2::AbstractFeature_strategy)
@settings(max_examples=50)
def test_aadl2::abstractfeature_instantiation(instance):
    assert isinstance(instance, aadl2::AbstractFeature)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=aadl2::AccessConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2::accessconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2::AccessConnectionEnd)

@given(instance=AccessConnectionEnd_strategy)
@settings(max_examples=50)
def test_accessconnectionend_instantiation(instance):
    assert isinstance(instance, AccessConnectionEnd)

@given(instance=aadl2::SubprogramGroupSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramgroupsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramGroupSubcomponent)

@given(instance=aadl2::BusSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::bussubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::BusSubcomponent)

@given(instance=aadl2::SubprogramSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramsubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramSubcomponent)

@given(instance=aadl2::SubprogramProxy_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramproxy_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramProxy)

@given(instance=aadl2::VirtualBusSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::virtualbussubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualBusSubcomponent)

@given(instance=aadl2::Access_strategy)
@settings(max_examples=50)
def test_aadl2::access_instantiation(instance):
    assert isinstance(instance, aadl2::Access)

@given(instance=aadl2::Access_strategy)
def test_aadl2::access_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=aadl2::Access_strategy)
def test_aadl2::access_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=aadl2::Access_strategy)
def test_aadl2::access_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=aadl2::Access_strategy)
def test_aadl2::access_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=aadl2::BusFeatureClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::busfeatureclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::BusFeatureClassifier)

@given(instance=aadl2::AbstractFeatureClassifier_strategy)
@settings(max_examples=50)
def test_aadl2::abstractfeatureclassifier_instantiation(instance):
    assert isinstance(instance, aadl2::AbstractFeatureClassifier)

@given(instance=Access_strategy)
@settings(max_examples=50)
def test_access_instantiation(instance):
    assert isinstance(instance, Access)

@given(instance=aadl2::BusAccess_strategy)
@settings(max_examples=50)
def test_aadl2::busaccess_instantiation(instance):
    assert isinstance(instance, aadl2::BusAccess)

@given(instance=aadl2::BusAccess_strategy)
def test_aadl2::busaccess_virtual_type(instance):
    assert isinstance(instance.virtual, str)


@given(instance=aadl2::BusAccess_strategy)
def test_aadl2::busaccess_virtual_setter(instance):
    original = instance.virtual
    instance.virtual = original
    assert instance.virtual == original

@given(instance=AbstractFeatureClassifier_strategy)
@settings(max_examples=50)
def test_abstractfeatureclassifier_instantiation(instance):
    assert isinstance(instance, AbstractFeatureClassifier)

@given(instance=aadl2::BusSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::bussubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::BusSubcomponentType)

@given(instance=aadl2::SubprogramGroupSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramgroupsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramGroupSubcomponentType)

@given(instance=aadl2::SubprogramSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramSubcomponentType)

@given(instance=aadl2::VirtualBusSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::virtualbussubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::VirtualBusSubcomponentType)

@given(instance=aadl2::AbstractSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::abstractsubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::AbstractSubcomponentType)

@given(instance=aadl2::PortConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2::portconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2::PortConnectionEnd)

@given(instance=aadl2::ParameterConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2::parameterconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2::ParameterConnectionEnd)

@given(instance=aadl2::DataSubcomponentType_strategy)
@settings(max_examples=50)
def test_aadl2::datasubcomponenttype_instantiation(instance):
    assert isinstance(instance, aadl2::DataSubcomponentType)

@given(instance=PortConnectionEnd_strategy)
@settings(max_examples=50)
def test_portconnectionend_instantiation(instance):
    assert isinstance(instance, PortConnectionEnd)

@given(instance=aadl2::PortProxy_strategy)
@settings(max_examples=50)
def test_aadl2::portproxy_instantiation(instance):
    assert isinstance(instance, aadl2::PortProxy)

@given(instance=aadl2::PortProxy_strategy)
def test_aadl2::portproxy_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=aadl2::PortProxy_strategy)
def test_aadl2::portproxy_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=aadl2::PortProxy_strategy)
def test_aadl2::portproxy_in__type(instance):
    assert isinstance(instance.in_, str)


@given(instance=aadl2::PortProxy_strategy)
def test_aadl2::portproxy_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=aadl2::PortProxy_strategy)
def test_aadl2::portproxy_out_type(instance):
    assert isinstance(instance.out, str)


@given(instance=aadl2::PortProxy_strategy)
def test_aadl2::portproxy_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original

@given(instance=aadl2::InternalFeature_strategy)
@settings(max_examples=50)
def test_aadl2::internalfeature_instantiation(instance):
    assert isinstance(instance, aadl2::InternalFeature)

@given(instance=aadl2::InternalFeature_strategy)
def test_aadl2::internalfeature_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=aadl2::InternalFeature_strategy)
def test_aadl2::internalfeature_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=aadl2::InternalFeature_strategy)
def test_aadl2::internalfeature_out_type(instance):
    assert isinstance(instance.out, str)


@given(instance=aadl2::InternalFeature_strategy)
def test_aadl2::internalfeature_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original

@given(instance=aadl2::InternalFeature_strategy)
def test_aadl2::internalfeature_in__type(instance):
    assert isinstance(instance.in_, str)


@given(instance=aadl2::InternalFeature_strategy)
def test_aadl2::internalfeature_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=aadl2::Port_strategy)
@settings(max_examples=50)
def test_aadl2::port_instantiation(instance):
    assert isinstance(instance, aadl2::Port)

@given(instance=aadl2::Port_strategy)
def test_aadl2::port_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=aadl2::Port_strategy)
def test_aadl2::port_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=ParameterConnectionEnd_strategy)
@settings(max_examples=50)
def test_parameterconnectionend_instantiation(instance):
    assert isinstance(instance, ParameterConnectionEnd)

@given(instance=aadl2::DataSubcomponent_strategy)
@settings(max_examples=50)
def test_aadl2::datasubcomponent_instantiation(instance):
    assert isinstance(instance, aadl2::DataSubcomponent)

@given(instance=aadl2::DataPort_strategy)
@settings(max_examples=50)
def test_aadl2::dataport_instantiation(instance):
    assert isinstance(instance, aadl2::DataPort)

@given(instance=aadl2::DataAccess_strategy)
@settings(max_examples=50)
def test_aadl2::dataaccess_instantiation(instance):
    assert isinstance(instance, aadl2::DataAccess)

@given(instance=aadl2::Parameter_strategy)
@settings(max_examples=50)
def test_aadl2::parameter_instantiation(instance):
    assert isinstance(instance, aadl2::Parameter)

@given(instance=aadl2::EventPort_strategy)
@settings(max_examples=50)
def test_aadl2::eventport_instantiation(instance):
    assert isinstance(instance, aadl2::EventPort)

@given(instance=aadl2::SubprogramGroupAccess_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramgroupaccess_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramGroupAccess)

@given(instance=aadl2::SubprogramAccess_strategy)
@settings(max_examples=50)
def test_aadl2::subprogramaccess_instantiation(instance):
    assert isinstance(instance, aadl2::SubprogramAccess)

@given(instance=FeatureType_strategy)
@settings(max_examples=50)
def test_featuretype_instantiation(instance):
    assert isinstance(instance, FeatureType)

@given(instance=aadl2::FeatureGroupType_strategy)
@settings(max_examples=50)
def test_aadl2::featuregrouptype_instantiation(instance):
    assert isinstance(instance, aadl2::FeatureGroupType)

@given(instance=aadl2::FeatureGroupPrototype_strategy)
@settings(max_examples=50)
def test_aadl2::featuregroupprototype_instantiation(instance):
    assert isinstance(instance, aadl2::FeatureGroupPrototype)

@given(instance=aadl2::FeatureGroupConnectionEnd_strategy)
@settings(max_examples=50)
def test_aadl2::featuregroupconnectionend_instantiation(instance):
    assert isinstance(instance, aadl2::FeatureGroupConnectionEnd)

@given(instance=aadl2::EventDataPort_strategy)
@settings(max_examples=50)
def test_aadl2::eventdataport_instantiation(instance):
    assert isinstance(instance, aadl2::EventDataPort)
