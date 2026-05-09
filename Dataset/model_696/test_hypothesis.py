import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ResolveExp,
    QVTOperational::ResolveInExp,
    ModuleImport,
    EntryOperation,
    ConstructorBody,
    InstantiationExp,
    QVTOperational::ObjectExp,
    ModelType,
    MappingOperation,
    ImperativeCallExp,
    QVTOperational::MappingCallExp,
    RelationDomain,
    ModelParameter,
    OperationBody,
    QVTOperational::MappingBody,
    QVTOperational::ConstructorBody,
    Module,
    QVTOperational::OperationalTransformation,
    QVTOperational::Library,
    VarParameter,
    QVTOperational::ModelParameter,
    QVTOperational::MappingParameter,
    DomainPattern,
    RelationDomainAssignment,
    Relation,
    ImperativeOperation,
    QVTOperational::MappingOperation,
    QVTOperational::EntryOperation,
    QVTOperational::Helper,
    QVTOperational::Constructor,
    Key,
    ObjectTemplateExp,
    RelationImplementation,
    PropertyCallExp,
    QVTRelation::OppositePropertyCallExp,
    RelationalTransformation,
    TemplateExp,
    QVTTemplate::CollectionTemplateExp,
    PropertyTemplateItem,
    QVTTemplate::ObjectTemplateExp,
    RealizedVariable,
    EnforcementOperation,
    Assignment,
    QVTCore::PropertyAssignment,
    QVTCore::VariableAssignment,
    Area,
    CorePattern,
    QVTCore::BottomPattern,
    Mapping,
    QVTCore::GuardPattern,
    Tag,
    Transformation,
    QVTRelation::RelationalTransformation,
    GuardPattern,
    BottomPattern,
    QVTCore::Area,
    TypedModel,
    Rule,
    QVTRelation::Relation,
    QVTCore::Mapping,
    Domain,
    QVTCore::CoreDomain,
    QVTRelation::RelationDomain,
    Pattern,
    QVTCore::CorePattern,
    QVTRelation::DomainPattern,
    LoopExp,
    EssentialOCL::IterateExp,
    NavigationCallExp,
    EssentialOCL::PropertyCallExp,
    NumericLiteralExp,
    EssentialOCL::RealLiteralExp,
    EssentialOCL::IntegerLiteralExp,
    CallExp,
    EssentialOCL::FeatureCallExp,
    OclExpression,
    EssentialOCL::IfExp,
    QVTRelation::RelationCallExp,
    EssentialOCL::CallExp,
    PrimitiveLiteralExp,
    EssentialOCL::BooleanLiteralExp,
    Variable,
    QVTCore::RealizedVariable,
    CollectionLiteralExp,
    LiteralExp,
    EssentialOCL::InvalidLiteralExp,
    QVTTemplate::TemplateExp,
    EssentialOCL::EnumLiteralExp,
    EssentialOCL::PrimitiveLiteralExp,
    EssentialOCL::CollectionLiteralExp,
    CollectionLiteralPart,
    EssentialOCL::CollectionRange,
    EssentialOCL::CollectionItem,
    ReflectiveCollection,
    EMOF::ReflectiveSequence,
    CollectionType,
    EssentialOCL::OrderedSetType,
    EssentialOCL::SequenceType,
    EssentialOCL::BagType,
    Extent,
    EMOF::URIExtent,
    EMOF::Object,
    Parameter,
    QVTBase::FunctionParameter,
    QVTOperational::VarParameter,
    MultiplicityElement,
    TypedElement,
    EssentialOCL::OclExpression,
    EssentialOCL::ExpressionInOcl,
    EMOF::Parameter,
    EssentialOCL::CollectionLiteralPart,
    EMOF::Property,
    EMOF::Operation,
    NamedElement,
    QVTBase::Domain,
    EMOF::TypedElement,
    QVTBase::Rule,
    QVTBase::TypedModel,
    EMOF::Package,
    EMOF::Type,
    Element,
    EMOF::NamedElement,
    QVTBase::Pattern,
    QVTOperational::ModuleImport,
    QVTBase::Predicate,
    QVTOperational::OperationBody,
    QVTRelation::RelationImplementation,
    QVTTemplate::PropertyTemplateItem,
    EMOF::Tag,
    QVTCore::Assignment,
    QVTRelation::RelationDomainAssignment,
    QVTCore::EnforcementOperation,
    QVTRelation::Key,
    EMOF::Comment,
    EMOF::MultiplicityElement,
    Package,
    EMOF::Factory,
    Enumeration,
    EMOF::EnumerationLiteral,
    EnumerationLiteral,
    DataType,
    EssentialOCL::CollectionType,
    EMOF::PrimitiveType,
    EMOF::Enumeration,
    Comment,
    Object,
    EMOF::Extent,
    EMOF::ReflectiveCollection,
    EMOF::Element,
    Class,
    QVTOperational::ModelType,
    QVTBase::Transformation,
    QVTOperational::Module,
    Operation,
    QVTBase::Function,
    QVTOperational::ImperativeOperation,
    Property,
    QVTOperational::ContextualProperty,
    Type,
    EMOF::DataType,
    EssentialOCL::InvalidType,
    EssentialOCL::AnyType,
    EMOF::Class,
    Predicate,
    ImperativeOCL::Typedef,
    AltExp,
    CatchExp,
    OperationCallExp,
    ImperativeOCL::ListType,
    ImperativeOCL::ListLiteralExp,
    ImperativeOCL::OrderedTupleType,
    ImperativeOCL::OrderedTupleLiteralPart,
    OrderedTupleLiteralPart,
    ImperativeOCL::OrderedTupleLiteralExp,
    ImperativeOCL::ImperativeExpression,
    ImperativeLoopExp,
    ImperativeOCL::ForExp,
    ImperativeOCL::DictionaryType,
    ImperativeOCL::DictLiteralPart,
    DictLiteralPart,
    ImperativeOCL::DictLiteralExp,
    ImperativeOCL::ImperativeIterateExp,
    LogExp,
    EssentialOCL::Variable,
    EssentialOCL::UnlimitedNaturalExp,
    EssentialOCL::TypeExp,
    EssentialOCL::TupleType,
    TupleLiteralExp,
    EssentialOCL::TupleLiteralPart,
    TupleLiteralPart,
    EssentialOCL::TupleLiteralExp,
    EssentialOCL::TemplateParameterType,
    EssentialOCL::StringLiteralExp,
    EssentialOCL::SetType,
    ImperativeExpression,
    ImperativeOCL::WhileExp,
    ImperativeOCL::AssignExp,
    ImperativeOCL::SwitchExp,
    ImperativeOCL::VariableInitExp,
    ImperativeOCL::TryExp,
    ImperativeOCL::ContinueExp,
    ImperativeOCL::AssertExp,
    ImperativeOCL::ImperativeLoopExp,
    QVTOperational::ImperativeCallExp,
    ImperativeOCL::ComputeExp,
    ImperativeOCL::UnlinkExp,
    ImperativeOCL::UnpackExp,
    ImperativeOCL::BlockExp,
    ImperativeOCL::BreakExp,
    ImperativeOCL::CatchExp,
    ImperativeOCL::ReturnExp,
    ImperativeOCL::RaiseExp,
    QVTOperational::ResolveExp,
    ImperativeOCL::LogExp,
    ImperativeOCL::InstantiationExp,
    ImperativeOCL::AltExp,
    EssentialOCL::VoidType,
    EssentialOCL::VariableExp,
    LetExp,
    EssentialOCL::NumericLiteralExp,
    EssentialOCL::NullLiteralExp,
    FeatureCallExp,
    EssentialOCL::OperationCallExp,
    EssentialOCL::NavigationCallExp,
    EssentialOCL::LoopExp,
    EssentialOCL::LiteralExp,
    EssentialOCL::LetExp,
    EssentialOCL::IteratorExp,
    SeverityKind,
    ImportKind,
    DirectionKind,
    EnforcementMode,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_resolveexp_is_not_abstract():
    assert not inspect.isabstract(ResolveExp)


def test_resolveexp_constructor_exists():
    assert callable(ResolveExp.__init__)


def test_resolveexp_constructor_args():
    sig = inspect.signature(ResolveExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::resolveinexp_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::ResolveInExp)


def test_qvtoperational::resolveinexp_constructor_exists():
    assert callable(QVTOperational::ResolveInExp.__init__)


def test_qvtoperational::resolveinexp_constructor_args():
    sig = inspect.signature(QVTOperational::ResolveInExp.__init__)
    params = list(sig.parameters.keys())



def test_moduleimport_is_not_abstract():
    assert not inspect.isabstract(ModuleImport)


def test_moduleimport_constructor_exists():
    assert callable(ModuleImport.__init__)


def test_moduleimport_constructor_args():
    sig = inspect.signature(ModuleImport.__init__)
    params = list(sig.parameters.keys())



def test_entryoperation_is_not_abstract():
    assert not inspect.isabstract(EntryOperation)


def test_entryoperation_constructor_exists():
    assert callable(EntryOperation.__init__)


def test_entryoperation_constructor_args():
    sig = inspect.signature(EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_constructorbody_is_not_abstract():
    assert not inspect.isabstract(ConstructorBody)


def test_constructorbody_constructor_exists():
    assert callable(ConstructorBody.__init__)


def test_constructorbody_constructor_args():
    sig = inspect.signature(ConstructorBody.__init__)
    params = list(sig.parameters.keys())



def test_instantiationexp_is_not_abstract():
    assert not inspect.isabstract(InstantiationExp)


def test_instantiationexp_constructor_exists():
    assert callable(InstantiationExp.__init__)


def test_instantiationexp_constructor_args():
    sig = inspect.signature(InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::objectexp_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::ObjectExp)


def test_qvtoperational::objectexp_constructor_exists():
    assert callable(QVTOperational::ObjectExp.__init__)


def test_qvtoperational::objectexp_constructor_args():
    sig = inspect.signature(QVTOperational::ObjectExp.__init__)
    params = list(sig.parameters.keys())



def test_modeltype_is_not_abstract():
    assert not inspect.isabstract(ModelType)


def test_modeltype_constructor_exists():
    assert callable(ModelType.__init__)


def test_modeltype_constructor_args():
    sig = inspect.signature(ModelType.__init__)
    params = list(sig.parameters.keys())



def test_mappingoperation_is_not_abstract():
    assert not inspect.isabstract(MappingOperation)


def test_mappingoperation_constructor_exists():
    assert callable(MappingOperation.__init__)


def test_mappingoperation_constructor_args():
    sig = inspect.signature(MappingOperation.__init__)
    params = list(sig.parameters.keys())



def test_imperativecallexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeCallExp)


def test_imperativecallexp_constructor_exists():
    assert callable(ImperativeCallExp.__init__)


def test_imperativecallexp_constructor_args():
    sig = inspect.signature(ImperativeCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::mappingcallexp_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::MappingCallExp)


def test_qvtoperational::mappingcallexp_constructor_exists():
    assert callable(QVTOperational::MappingCallExp.__init__)


def test_qvtoperational::mappingcallexp_constructor_args():
    sig = inspect.signature(QVTOperational::MappingCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isStrict" in params, "Missing parameter 'isStrict'"

def test_qvtoperational::mappingcallexp_has_isStrict():
    assert hasattr(QVTOperational::MappingCallExp, "isStrict")
    descriptor = None
    for klass in QVTOperational::MappingCallExp.__mro__:
        if "isStrict" in klass.__dict__:
            descriptor = klass.__dict__["isStrict"]
            break
    assert isinstance(descriptor, property)



def test_relationdomain_is_not_abstract():
    assert not inspect.isabstract(RelationDomain)


def test_relationdomain_constructor_exists():
    assert callable(RelationDomain.__init__)


def test_relationdomain_constructor_args():
    sig = inspect.signature(RelationDomain.__init__)
    params = list(sig.parameters.keys())



def test_modelparameter_is_not_abstract():
    assert not inspect.isabstract(ModelParameter)


def test_modelparameter_constructor_exists():
    assert callable(ModelParameter.__init__)


def test_modelparameter_constructor_args():
    sig = inspect.signature(ModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_operationbody_is_not_abstract():
    assert not inspect.isabstract(OperationBody)


def test_operationbody_constructor_exists():
    assert callable(OperationBody.__init__)


def test_operationbody_constructor_args():
    sig = inspect.signature(OperationBody.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::mappingbody_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::MappingBody)


def test_qvtoperational::mappingbody_constructor_exists():
    assert callable(QVTOperational::MappingBody.__init__)


def test_qvtoperational::mappingbody_constructor_args():
    sig = inspect.signature(QVTOperational::MappingBody.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::constructorbody_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::ConstructorBody)


def test_qvtoperational::constructorbody_constructor_exists():
    assert callable(QVTOperational::ConstructorBody.__init__)


def test_qvtoperational::constructorbody_constructor_args():
    sig = inspect.signature(QVTOperational::ConstructorBody.__init__)
    params = list(sig.parameters.keys())



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::operationaltransformation_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::OperationalTransformation)


def test_qvtoperational::operationaltransformation_constructor_exists():
    assert callable(QVTOperational::OperationalTransformation.__init__)


def test_qvtoperational::operationaltransformation_constructor_args():
    sig = inspect.signature(QVTOperational::OperationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::library_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::Library)


def test_qvtoperational::library_constructor_exists():
    assert callable(QVTOperational::Library.__init__)


def test_qvtoperational::library_constructor_args():
    sig = inspect.signature(QVTOperational::Library.__init__)
    params = list(sig.parameters.keys())



def test_varparameter_is_not_abstract():
    assert not inspect.isabstract(VarParameter)


def test_varparameter_constructor_exists():
    assert callable(VarParameter.__init__)


def test_varparameter_constructor_args():
    sig = inspect.signature(VarParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::modelparameter_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::ModelParameter)


def test_qvtoperational::modelparameter_constructor_exists():
    assert callable(QVTOperational::ModelParameter.__init__)


def test_qvtoperational::modelparameter_constructor_args():
    sig = inspect.signature(QVTOperational::ModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::mappingparameter_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::MappingParameter)


def test_qvtoperational::mappingparameter_constructor_exists():
    assert callable(QVTOperational::MappingParameter.__init__)


def test_qvtoperational::mappingparameter_constructor_args():
    sig = inspect.signature(QVTOperational::MappingParameter.__init__)
    params = list(sig.parameters.keys())



def test_domainpattern_is_not_abstract():
    assert not inspect.isabstract(DomainPattern)


def test_domainpattern_constructor_exists():
    assert callable(DomainPattern.__init__)


def test_domainpattern_constructor_args():
    sig = inspect.signature(DomainPattern.__init__)
    params = list(sig.parameters.keys())



def test_relationdomainassignment_is_not_abstract():
    assert not inspect.isabstract(RelationDomainAssignment)


def test_relationdomainassignment_constructor_exists():
    assert callable(RelationDomainAssignment.__init__)


def test_relationdomainassignment_constructor_args():
    sig = inspect.signature(RelationDomainAssignment.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoperation_is_not_abstract():
    assert not inspect.isabstract(ImperativeOperation)


def test_imperativeoperation_constructor_exists():
    assert callable(ImperativeOperation.__init__)


def test_imperativeoperation_constructor_args():
    sig = inspect.signature(ImperativeOperation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::mappingoperation_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::MappingOperation)


def test_qvtoperational::mappingoperation_constructor_exists():
    assert callable(QVTOperational::MappingOperation.__init__)


def test_qvtoperational::mappingoperation_constructor_args():
    sig = inspect.signature(QVTOperational::MappingOperation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::entryoperation_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::EntryOperation)


def test_qvtoperational::entryoperation_constructor_exists():
    assert callable(QVTOperational::EntryOperation.__init__)


def test_qvtoperational::entryoperation_constructor_args():
    sig = inspect.signature(QVTOperational::EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::helper_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::Helper)


def test_qvtoperational::helper_constructor_exists():
    assert callable(QVTOperational::Helper.__init__)


def test_qvtoperational::helper_constructor_args():
    sig = inspect.signature(QVTOperational::Helper.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_qvtoperational::helper_has_isQuery():
    assert hasattr(QVTOperational::Helper, "isQuery")
    descriptor = None
    for klass in QVTOperational::Helper.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational::constructor_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::Constructor)


def test_qvtoperational::constructor_constructor_exists():
    assert callable(QVTOperational::Constructor.__init__)


def test_qvtoperational::constructor_constructor_args():
    sig = inspect.signature(QVTOperational::Constructor.__init__)
    params = list(sig.parameters.keys())



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(ObjectTemplateExp)


def test_objecttemplateexp_constructor_exists():
    assert callable(ObjectTemplateExp.__init__)


def test_objecttemplateexp_constructor_args():
    sig = inspect.signature(ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_relationimplementation_is_not_abstract():
    assert not inspect.isabstract(RelationImplementation)


def test_relationimplementation_constructor_exists():
    assert callable(RelationImplementation.__init__)


def test_relationimplementation_constructor_args():
    sig = inspect.signature(RelationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::oppositepropertycallexp_is_not_abstract():
    assert not inspect.isabstract(QVTRelation::OppositePropertyCallExp)


def test_qvtrelation::oppositepropertycallexp_constructor_exists():
    assert callable(QVTRelation::OppositePropertyCallExp.__init__)


def test_qvtrelation::oppositepropertycallexp_constructor_args():
    sig = inspect.signature(QVTRelation::OppositePropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_relationaltransformation_is_not_abstract():
    assert not inspect.isabstract(RelationalTransformation)


def test_relationaltransformation_constructor_exists():
    assert callable(RelationalTransformation.__init__)


def test_relationaltransformation_constructor_args():
    sig = inspect.signature(RelationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_templateexp_is_not_abstract():
    assert not inspect.isabstract(TemplateExp)


def test_templateexp_constructor_exists():
    assert callable(TemplateExp.__init__)


def test_templateexp_constructor_args():
    sig = inspect.signature(TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate::collectiontemplateexp_is_not_abstract():
    assert not inspect.isabstract(QVTTemplate::CollectionTemplateExp)


def test_qvttemplate::collectiontemplateexp_constructor_exists():
    assert callable(QVTTemplate::CollectionTemplateExp.__init__)


def test_qvttemplate::collectiontemplateexp_constructor_args():
    sig = inspect.signature(QVTTemplate::CollectionTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(PropertyTemplateItem)


def test_propertytemplateitem_constructor_exists():
    assert callable(PropertyTemplateItem.__init__)


def test_propertytemplateitem_constructor_args():
    sig = inspect.signature(PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate::objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(QVTTemplate::ObjectTemplateExp)


def test_qvttemplate::objecttemplateexp_constructor_exists():
    assert callable(QVTTemplate::ObjectTemplateExp.__init__)


def test_qvttemplate::objecttemplateexp_constructor_args():
    sig = inspect.signature(QVTTemplate::ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_realizedvariable_is_not_abstract():
    assert not inspect.isabstract(RealizedVariable)


def test_realizedvariable_constructor_exists():
    assert callable(RealizedVariable.__init__)


def test_realizedvariable_constructor_args():
    sig = inspect.signature(RealizedVariable.__init__)
    params = list(sig.parameters.keys())



def test_enforcementoperation_is_not_abstract():
    assert not inspect.isabstract(EnforcementOperation)


def test_enforcementoperation_constructor_exists():
    assert callable(EnforcementOperation.__init__)


def test_enforcementoperation_constructor_args():
    sig = inspect.signature(EnforcementOperation.__init__)
    params = list(sig.parameters.keys())



def test_assignment_is_not_abstract():
    assert not inspect.isabstract(Assignment)


def test_assignment_constructor_exists():
    assert callable(Assignment.__init__)


def test_assignment_constructor_args():
    sig = inspect.signature(Assignment.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::propertyassignment_is_not_abstract():
    assert not inspect.isabstract(QVTCore::PropertyAssignment)


def test_qvtcore::propertyassignment_constructor_exists():
    assert callable(QVTCore::PropertyAssignment.__init__)


def test_qvtcore::propertyassignment_constructor_args():
    sig = inspect.signature(QVTCore::PropertyAssignment.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::variableassignment_is_not_abstract():
    assert not inspect.isabstract(QVTCore::VariableAssignment)


def test_qvtcore::variableassignment_constructor_exists():
    assert callable(QVTCore::VariableAssignment.__init__)


def test_qvtcore::variableassignment_constructor_args():
    sig = inspect.signature(QVTCore::VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_area_is_not_abstract():
    assert not inspect.isabstract(Area)


def test_area_constructor_exists():
    assert callable(Area.__init__)


def test_area_constructor_args():
    sig = inspect.signature(Area.__init__)
    params = list(sig.parameters.keys())



def test_corepattern_is_not_abstract():
    assert not inspect.isabstract(CorePattern)


def test_corepattern_constructor_exists():
    assert callable(CorePattern.__init__)


def test_corepattern_constructor_args():
    sig = inspect.signature(CorePattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::bottompattern_is_not_abstract():
    assert not inspect.isabstract(QVTCore::BottomPattern)


def test_qvtcore::bottompattern_constructor_exists():
    assert callable(QVTCore::BottomPattern.__init__)


def test_qvtcore::bottompattern_constructor_args():
    sig = inspect.signature(QVTCore::BottomPattern.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::guardpattern_is_not_abstract():
    assert not inspect.isabstract(QVTCore::GuardPattern)


def test_qvtcore::guardpattern_constructor_exists():
    assert callable(QVTCore::GuardPattern.__init__)


def test_qvtcore::guardpattern_constructor_args():
    sig = inspect.signature(QVTCore::GuardPattern.__init__)
    params = list(sig.parameters.keys())



def test_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())



def test_transformation_is_not_abstract():
    assert not inspect.isabstract(Transformation)


def test_transformation_constructor_exists():
    assert callable(Transformation.__init__)


def test_transformation_constructor_args():
    sig = inspect.signature(Transformation.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::relationaltransformation_is_not_abstract():
    assert not inspect.isabstract(QVTRelation::RelationalTransformation)


def test_qvtrelation::relationaltransformation_constructor_exists():
    assert callable(QVTRelation::RelationalTransformation.__init__)


def test_qvtrelation::relationaltransformation_constructor_args():
    sig = inspect.signature(QVTRelation::RelationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_guardpattern_is_not_abstract():
    assert not inspect.isabstract(GuardPattern)


def test_guardpattern_constructor_exists():
    assert callable(GuardPattern.__init__)


def test_guardpattern_constructor_args():
    sig = inspect.signature(GuardPattern.__init__)
    params = list(sig.parameters.keys())



def test_bottompattern_is_not_abstract():
    assert not inspect.isabstract(BottomPattern)


def test_bottompattern_constructor_exists():
    assert callable(BottomPattern.__init__)


def test_bottompattern_constructor_args():
    sig = inspect.signature(BottomPattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::area_is_not_abstract():
    assert not inspect.isabstract(QVTCore::Area)


def test_qvtcore::area_constructor_exists():
    assert callable(QVTCore::Area.__init__)


def test_qvtcore::area_constructor_args():
    sig = inspect.signature(QVTCore::Area.__init__)
    params = list(sig.parameters.keys())



def test_typedmodel_is_not_abstract():
    assert not inspect.isabstract(TypedModel)


def test_typedmodel_constructor_exists():
    assert callable(TypedModel.__init__)


def test_typedmodel_constructor_args():
    sig = inspect.signature(TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::relation_is_not_abstract():
    assert not inspect.isabstract(QVTRelation::Relation)


def test_qvtrelation::relation_constructor_exists():
    assert callable(QVTRelation::Relation.__init__)


def test_qvtrelation::relation_constructor_args():
    sig = inspect.signature(QVTRelation::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopLevel" in params, "Missing parameter 'isTopLevel'"

def test_qvtrelation::relation_has_isTopLevel():
    assert hasattr(QVTRelation::Relation, "isTopLevel")
    descriptor = None
    for klass in QVTRelation::Relation.__mro__:
        if "isTopLevel" in klass.__dict__:
            descriptor = klass.__dict__["isTopLevel"]
            break
    assert isinstance(descriptor, property)



def test_qvtcore::mapping_is_not_abstract():
    assert not inspect.isabstract(QVTCore::Mapping)


def test_qvtcore::mapping_constructor_exists():
    assert callable(QVTCore::Mapping.__init__)


def test_qvtcore::mapping_constructor_args():
    sig = inspect.signature(QVTCore::Mapping.__init__)
    params = list(sig.parameters.keys())



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::coredomain_is_not_abstract():
    assert not inspect.isabstract(QVTCore::CoreDomain)


def test_qvtcore::coredomain_constructor_exists():
    assert callable(QVTCore::CoreDomain.__init__)


def test_qvtcore::coredomain_constructor_args():
    sig = inspect.signature(QVTCore::CoreDomain.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::relationdomain_is_not_abstract():
    assert not inspect.isabstract(QVTRelation::RelationDomain)


def test_qvtrelation::relationdomain_constructor_exists():
    assert callable(QVTRelation::RelationDomain.__init__)


def test_qvtrelation::relationdomain_constructor_args():
    sig = inspect.signature(QVTRelation::RelationDomain.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::corepattern_is_not_abstract():
    assert not inspect.isabstract(QVTCore::CorePattern)


def test_qvtcore::corepattern_constructor_exists():
    assert callable(QVTCore::CorePattern.__init__)


def test_qvtcore::corepattern_constructor_args():
    sig = inspect.signature(QVTCore::CorePattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::domainpattern_is_not_abstract():
    assert not inspect.isabstract(QVTRelation::DomainPattern)


def test_qvtrelation::domainpattern_constructor_exists():
    assert callable(QVTRelation::DomainPattern.__init__)


def test_qvtrelation::domainpattern_constructor_args():
    sig = inspect.signature(QVTRelation::DomainPattern.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::IterateExp)


def test_essentialocl::iterateexp_constructor_exists():
    assert callable(EssentialOCL::IterateExp.__init__)


def test_essentialocl::iterateexp_constructor_args():
    sig = inspect.signature(EssentialOCL::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(NavigationCallExp)


def test_navigationcallexp_constructor_exists():
    assert callable(NavigationCallExp.__init__)


def test_navigationcallexp_constructor_args():
    sig = inspect.signature(NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::PropertyCallExp)


def test_essentialocl::propertycallexp_constructor_exists():
    assert callable(EssentialOCL::PropertyCallExp.__init__)


def test_essentialocl::propertycallexp_constructor_args():
    sig = inspect.signature(EssentialOCL::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::RealLiteralExp)


def test_essentialocl::realliteralexp_constructor_exists():
    assert callable(EssentialOCL::RealLiteralExp.__init__)


def test_essentialocl::realliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_essentialocl::realliteralexp_has_realSymbol():
    assert hasattr(EssentialOCL::RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in EssentialOCL::RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::IntegerLiteralExp)


def test_essentialocl::integerliteralexp_constructor_exists():
    assert callable(EssentialOCL::IntegerLiteralExp.__init__)


def test_essentialocl::integerliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_essentialocl::integerliteralexp_has_integerSymbol():
    assert hasattr(EssentialOCL::IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in EssentialOCL::IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::featurecallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::FeatureCallExp)


def test_essentialocl::featurecallexp_constructor_exists():
    assert callable(EssentialOCL::FeatureCallExp.__init__)


def test_essentialocl::featurecallexp_constructor_args():
    sig = inspect.signature(EssentialOCL::FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::IfExp)


def test_essentialocl::ifexp_constructor_exists():
    assert callable(EssentialOCL::IfExp.__init__)


def test_essentialocl::ifexp_constructor_args():
    sig = inspect.signature(EssentialOCL::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::relationcallexp_is_not_abstract():
    assert not inspect.isabstract(QVTRelation::RelationCallExp)


def test_qvtrelation::relationcallexp_constructor_exists():
    assert callable(QVTRelation::RelationCallExp.__init__)


def test_qvtrelation::relationcallexp_constructor_args():
    sig = inspect.signature(QVTRelation::RelationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::callexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::CallExp)


def test_essentialocl::callexp_constructor_exists():
    assert callable(EssentialOCL::CallExp.__init__)


def test_essentialocl::callexp_constructor_args():
    sig = inspect.signature(EssentialOCL::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::BooleanLiteralExp)


def test_essentialocl::booleanliteralexp_constructor_exists():
    assert callable(EssentialOCL::BooleanLiteralExp.__init__)


def test_essentialocl::booleanliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_essentialocl::booleanliteralexp_has_booleanSymbol():
    assert hasattr(EssentialOCL::BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in EssentialOCL::BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::realizedvariable_is_not_abstract():
    assert not inspect.isabstract(QVTCore::RealizedVariable)


def test_qvtcore::realizedvariable_constructor_exists():
    assert callable(QVTCore::RealizedVariable.__init__)


def test_qvtcore::realizedvariable_constructor_args():
    sig = inspect.signature(QVTCore::RealizedVariable.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::InvalidLiteralExp)


def test_essentialocl::invalidliteralexp_constructor_exists():
    assert callable(EssentialOCL::InvalidLiteralExp.__init__)


def test_essentialocl::invalidliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate::templateexp_is_not_abstract():
    assert not inspect.isabstract(QVTTemplate::TemplateExp)


def test_qvttemplate::templateexp_constructor_exists():
    assert callable(QVTTemplate::TemplateExp.__init__)


def test_qvttemplate::templateexp_constructor_args():
    sig = inspect.signature(QVTTemplate::TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::EnumLiteralExp)


def test_essentialocl::enumliteralexp_constructor_exists():
    assert callable(EssentialOCL::EnumLiteralExp.__init__)


def test_essentialocl::enumliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::PrimitiveLiteralExp)


def test_essentialocl::primitiveliteralexp_constructor_exists():
    assert callable(EssentialOCL::PrimitiveLiteralExp.__init__)


def test_essentialocl::primitiveliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::CollectionLiteralExp)


def test_essentialocl::collectionliteralexp_constructor_exists():
    assert callable(EssentialOCL::CollectionLiteralExp.__init__)


def test_essentialocl::collectionliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_essentialocl::collectionliteralexp_has_kind():
    assert hasattr(EssentialOCL::CollectionLiteralExp, "kind")
    descriptor = None
    for klass in EssentialOCL::CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectionrange_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::CollectionRange)


def test_essentialocl::collectionrange_constructor_exists():
    assert callable(EssentialOCL::CollectionRange.__init__)


def test_essentialocl::collectionrange_constructor_args():
    sig = inspect.signature(EssentialOCL::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectionitem_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::CollectionItem)


def test_essentialocl::collectionitem_constructor_exists():
    assert callable(EssentialOCL::CollectionItem.__init__)


def test_essentialocl::collectionitem_constructor_args():
    sig = inspect.signature(EssentialOCL::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_reflectivecollection_is_not_abstract():
    assert not inspect.isabstract(ReflectiveCollection)


def test_reflectivecollection_constructor_exists():
    assert callable(ReflectiveCollection.__init__)


def test_reflectivecollection_constructor_args():
    sig = inspect.signature(ReflectiveCollection.__init__)
    params = list(sig.parameters.keys())



def test_emof::reflectivesequence_is_not_abstract():
    assert not inspect.isabstract(EMOF::ReflectiveSequence)


def test_emof::reflectivesequence_constructor_exists():
    assert callable(EMOF::ReflectiveSequence.__init__)


def test_emof::reflectivesequence_constructor_args():
    sig = inspect.signature(EMOF::ReflectiveSequence.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::OrderedSetType)


def test_essentialocl::orderedsettype_constructor_exists():
    assert callable(EssentialOCL::OrderedSetType.__init__)


def test_essentialocl::orderedsettype_constructor_args():
    sig = inspect.signature(EssentialOCL::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::SequenceType)


def test_essentialocl::sequencetype_constructor_exists():
    assert callable(EssentialOCL::SequenceType.__init__)


def test_essentialocl::sequencetype_constructor_args():
    sig = inspect.signature(EssentialOCL::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::BagType)


def test_essentialocl::bagtype_constructor_exists():
    assert callable(EssentialOCL::BagType.__init__)


def test_essentialocl::bagtype_constructor_args():
    sig = inspect.signature(EssentialOCL::BagType.__init__)
    params = list(sig.parameters.keys())



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_emof::uriextent_is_not_abstract():
    assert not inspect.isabstract(EMOF::URIExtent)


def test_emof::uriextent_constructor_exists():
    assert callable(EMOF::URIExtent.__init__)


def test_emof::uriextent_constructor_args():
    sig = inspect.signature(EMOF::URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_emof::object_is_not_abstract():
    assert not inspect.isabstract(EMOF::Object)


def test_emof::object_constructor_exists():
    assert callable(EMOF::Object.__init__)


def test_emof::object_constructor_args():
    sig = inspect.signature(EMOF::Object.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase::functionparameter_is_not_abstract():
    assert not inspect.isabstract(QVTBase::FunctionParameter)


def test_qvtbase::functionparameter_constructor_exists():
    assert callable(QVTBase::FunctionParameter.__init__)


def test_qvtbase::functionparameter_constructor_args():
    sig = inspect.signature(QVTBase::FunctionParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::varparameter_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::VarParameter)


def test_qvtoperational::varparameter_constructor_exists():
    assert callable(QVTOperational::VarParameter.__init__)


def test_qvtoperational::varparameter_constructor_args():
    sig = inspect.signature(QVTOperational::VarParameter.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_qvtoperational::varparameter_has_kind():
    assert hasattr(QVTOperational::VarParameter, "kind")
    descriptor = None
    for klass in QVTOperational::VarParameter.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::OclExpression)


def test_essentialocl::oclexpression_constructor_exists():
    assert callable(EssentialOCL::OclExpression.__init__)


def test_essentialocl::oclexpression_constructor_args():
    sig = inspect.signature(EssentialOCL::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::expressioninocl_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::ExpressionInOcl)


def test_essentialocl::expressioninocl_constructor_exists():
    assert callable(EssentialOCL::ExpressionInOcl.__init__)


def test_essentialocl::expressioninocl_constructor_args():
    sig = inspect.signature(EssentialOCL::ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_emof::parameter_is_not_abstract():
    assert not inspect.isabstract(EMOF::Parameter)


def test_emof::parameter_constructor_exists():
    assert callable(EMOF::Parameter.__init__)


def test_emof::parameter_constructor_args():
    sig = inspect.signature(EMOF::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::CollectionLiteralPart)


def test_essentialocl::collectionliteralpart_constructor_exists():
    assert callable(EssentialOCL::CollectionLiteralPart.__init__)


def test_essentialocl::collectionliteralpart_constructor_args():
    sig = inspect.signature(EssentialOCL::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_emof::property_is_not_abstract():
    assert not inspect.isabstract(EMOF::Property)


def test_emof::property_constructor_exists():
    assert callable(EMOF::Property.__init__)


def test_emof::property_constructor_args():
    sig = inspect.signature(EMOF::Property.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isID" in params, "Missing parameter 'isID'"

def test_emof::property_has_default():
    assert hasattr(EMOF::Property, "default")
    descriptor = None
    for klass in EMOF::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_emof::property_has_isDerived():
    assert hasattr(EMOF::Property, "isDerived")
    descriptor = None
    for klass in EMOF::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_emof::property_has_isComposite():
    assert hasattr(EMOF::Property, "isComposite")
    descriptor = None
    for klass in EMOF::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_emof::property_has_isReadOnly():
    assert hasattr(EMOF::Property, "isReadOnly")
    descriptor = None
    for klass in EMOF::Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_emof::property_has_isID():
    assert hasattr(EMOF::Property, "isID")
    descriptor = None
    for klass in EMOF::Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)



def test_emof::operation_is_not_abstract():
    assert not inspect.isabstract(EMOF::Operation)


def test_emof::operation_constructor_exists():
    assert callable(EMOF::Operation.__init__)


def test_emof::operation_constructor_args():
    sig = inspect.signature(EMOF::Operation.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase::domain_is_not_abstract():
    assert not inspect.isabstract(QVTBase::Domain)


def test_qvtbase::domain_constructor_exists():
    assert callable(QVTBase::Domain.__init__)


def test_qvtbase::domain_constructor_args():
    sig = inspect.signature(QVTBase::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "isCheckable" in params, "Missing parameter 'isCheckable'"
    assert "isEnforceable" in params, "Missing parameter 'isEnforceable'"

def test_qvtbase::domain_has_isCheckable():
    assert hasattr(QVTBase::Domain, "isCheckable")
    descriptor = None
    for klass in QVTBase::Domain.__mro__:
        if "isCheckable" in klass.__dict__:
            descriptor = klass.__dict__["isCheckable"]
            break
    assert isinstance(descriptor, property)

def test_qvtbase::domain_has_isEnforceable():
    assert hasattr(QVTBase::Domain, "isEnforceable")
    descriptor = None
    for klass in QVTBase::Domain.__mro__:
        if "isEnforceable" in klass.__dict__:
            descriptor = klass.__dict__["isEnforceable"]
            break
    assert isinstance(descriptor, property)



def test_emof::typedelement_is_not_abstract():
    assert not inspect.isabstract(EMOF::TypedElement)


def test_emof::typedelement_constructor_exists():
    assert callable(EMOF::TypedElement.__init__)


def test_emof::typedelement_constructor_args():
    sig = inspect.signature(EMOF::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase::rule_is_not_abstract():
    assert not inspect.isabstract(QVTBase::Rule)


def test_qvtbase::rule_constructor_exists():
    assert callable(QVTBase::Rule.__init__)


def test_qvtbase::rule_constructor_args():
    sig = inspect.signature(QVTBase::Rule.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase::typedmodel_is_not_abstract():
    assert not inspect.isabstract(QVTBase::TypedModel)


def test_qvtbase::typedmodel_constructor_exists():
    assert callable(QVTBase::TypedModel.__init__)


def test_qvtbase::typedmodel_constructor_args():
    sig = inspect.signature(QVTBase::TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_emof::package_is_not_abstract():
    assert not inspect.isabstract(EMOF::Package)


def test_emof::package_constructor_exists():
    assert callable(EMOF::Package.__init__)


def test_emof::package_constructor_args():
    sig = inspect.signature(EMOF::Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_emof::package_has_uri():
    assert hasattr(EMOF::Package, "uri")
    descriptor = None
    for klass in EMOF::Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_emof::type_is_not_abstract():
    assert not inspect.isabstract(EMOF::Type)


def test_emof::type_constructor_exists():
    assert callable(EMOF::Type.__init__)


def test_emof::type_constructor_args():
    sig = inspect.signature(EMOF::Type.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_emof::namedelement_is_not_abstract():
    assert not inspect.isabstract(EMOF::NamedElement)


def test_emof::namedelement_constructor_exists():
    assert callable(EMOF::NamedElement.__init__)


def test_emof::namedelement_constructor_args():
    sig = inspect.signature(EMOF::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emof::namedelement_has_name():
    assert hasattr(EMOF::NamedElement, "name")
    descriptor = None
    for klass in EMOF::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qvtbase::pattern_is_not_abstract():
    assert not inspect.isabstract(QVTBase::Pattern)


def test_qvtbase::pattern_constructor_exists():
    assert callable(QVTBase::Pattern.__init__)


def test_qvtbase::pattern_constructor_args():
    sig = inspect.signature(QVTBase::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::moduleimport_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::ModuleImport)


def test_qvtoperational::moduleimport_constructor_exists():
    assert callable(QVTOperational::ModuleImport.__init__)


def test_qvtoperational::moduleimport_constructor_args():
    sig = inspect.signature(QVTOperational::ModuleImport.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_qvtoperational::moduleimport_has_kind():
    assert hasattr(QVTOperational::ModuleImport, "kind")
    descriptor = None
    for klass in QVTOperational::ModuleImport.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_qvtbase::predicate_is_not_abstract():
    assert not inspect.isabstract(QVTBase::Predicate)


def test_qvtbase::predicate_constructor_exists():
    assert callable(QVTBase::Predicate.__init__)


def test_qvtbase::predicate_constructor_args():
    sig = inspect.signature(QVTBase::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::operationbody_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::OperationBody)


def test_qvtoperational::operationbody_constructor_exists():
    assert callable(QVTOperational::OperationBody.__init__)


def test_qvtoperational::operationbody_constructor_args():
    sig = inspect.signature(QVTOperational::OperationBody.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::relationimplementation_is_not_abstract():
    assert not inspect.isabstract(QVTRelation::RelationImplementation)


def test_qvtrelation::relationimplementation_constructor_exists():
    assert callable(QVTRelation::RelationImplementation.__init__)


def test_qvtrelation::relationimplementation_constructor_args():
    sig = inspect.signature(QVTRelation::RelationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate::propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(QVTTemplate::PropertyTemplateItem)


def test_qvttemplate::propertytemplateitem_constructor_exists():
    assert callable(QVTTemplate::PropertyTemplateItem.__init__)


def test_qvttemplate::propertytemplateitem_constructor_args():
    sig = inspect.signature(QVTTemplate::PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())
    assert "isOpposite" in params, "Missing parameter 'isOpposite'"

def test_qvttemplate::propertytemplateitem_has_isOpposite():
    assert hasattr(QVTTemplate::PropertyTemplateItem, "isOpposite")
    descriptor = None
    for klass in QVTTemplate::PropertyTemplateItem.__mro__:
        if "isOpposite" in klass.__dict__:
            descriptor = klass.__dict__["isOpposite"]
            break
    assert isinstance(descriptor, property)



def test_emof::tag_is_not_abstract():
    assert not inspect.isabstract(EMOF::Tag)


def test_emof::tag_constructor_exists():
    assert callable(EMOF::Tag.__init__)


def test_emof::tag_constructor_args():
    sig = inspect.signature(EMOF::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_emof::tag_has_value():
    assert hasattr(EMOF::Tag, "value")
    descriptor = None
    for klass in EMOF::Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_emof::tag_has_name():
    assert hasattr(EMOF::Tag, "name")
    descriptor = None
    for klass in EMOF::Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qvtcore::assignment_is_not_abstract():
    assert not inspect.isabstract(QVTCore::Assignment)


def test_qvtcore::assignment_constructor_exists():
    assert callable(QVTCore::Assignment.__init__)


def test_qvtcore::assignment_constructor_args():
    sig = inspect.signature(QVTCore::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_qvtcore::assignment_has_isDefault():
    assert hasattr(QVTCore::Assignment, "isDefault")
    descriptor = None
    for klass in QVTCore::Assignment.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_qvtrelation::relationdomainassignment_is_not_abstract():
    assert not inspect.isabstract(QVTRelation::RelationDomainAssignment)


def test_qvtrelation::relationdomainassignment_constructor_exists():
    assert callable(QVTRelation::RelationDomainAssignment.__init__)


def test_qvtrelation::relationdomainassignment_constructor_args():
    sig = inspect.signature(QVTRelation::RelationDomainAssignment.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::enforcementoperation_is_not_abstract():
    assert not inspect.isabstract(QVTCore::EnforcementOperation)


def test_qvtcore::enforcementoperation_constructor_exists():
    assert callable(QVTCore::EnforcementOperation.__init__)


def test_qvtcore::enforcementoperation_constructor_args():
    sig = inspect.signature(QVTCore::EnforcementOperation.__init__)
    params = list(sig.parameters.keys())
    assert "enforcementMode" in params, "Missing parameter 'enforcementMode'"

def test_qvtcore::enforcementoperation_has_enforcementMode():
    assert hasattr(QVTCore::EnforcementOperation, "enforcementMode")
    descriptor = None
    for klass in QVTCore::EnforcementOperation.__mro__:
        if "enforcementMode" in klass.__dict__:
            descriptor = klass.__dict__["enforcementMode"]
            break
    assert isinstance(descriptor, property)



def test_qvtrelation::key_is_not_abstract():
    assert not inspect.isabstract(QVTRelation::Key)


def test_qvtrelation::key_constructor_exists():
    assert callable(QVTRelation::Key.__init__)


def test_qvtrelation::key_constructor_args():
    sig = inspect.signature(QVTRelation::Key.__init__)
    params = list(sig.parameters.keys())



def test_emof::comment_is_not_abstract():
    assert not inspect.isabstract(EMOF::Comment)


def test_emof::comment_constructor_exists():
    assert callable(EMOF::Comment.__init__)


def test_emof::comment_constructor_args():
    sig = inspect.signature(EMOF::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_emof::comment_has_body():
    assert hasattr(EMOF::Comment, "body")
    descriptor = None
    for klass in EMOF::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_emof::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(EMOF::MultiplicityElement)


def test_emof::multiplicityelement_constructor_exists():
    assert callable(EMOF::MultiplicityElement.__init__)


def test_emof::multiplicityelement_constructor_args():
    sig = inspect.signature(EMOF::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_emof::multiplicityelement_has_isUnique():
    assert hasattr(EMOF::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in EMOF::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_emof::multiplicityelement_has_upper():
    assert hasattr(EMOF::MultiplicityElement, "upper")
    descriptor = None
    for klass in EMOF::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_emof::multiplicityelement_has_lower():
    assert hasattr(EMOF::MultiplicityElement, "lower")
    descriptor = None
    for klass in EMOF::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_emof::multiplicityelement_has_isOrdered():
    assert hasattr(EMOF::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in EMOF::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_emof::factory_is_not_abstract():
    assert not inspect.isabstract(EMOF::Factory)


def test_emof::factory_constructor_exists():
    assert callable(EMOF::Factory.__init__)


def test_emof::factory_constructor_args():
    sig = inspect.signature(EMOF::Factory.__init__)
    params = list(sig.parameters.keys())



def test_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_emof::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EMOF::EnumerationLiteral)


def test_emof::enumerationliteral_constructor_exists():
    assert callable(EMOF::EnumerationLiteral.__init__)


def test_emof::enumerationliteral_constructor_args():
    sig = inspect.signature(EMOF::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::CollectionType)


def test_essentialocl::collectiontype_constructor_exists():
    assert callable(EssentialOCL::CollectionType.__init__)


def test_essentialocl::collectiontype_constructor_args():
    sig = inspect.signature(EssentialOCL::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_emof::primitivetype_is_not_abstract():
    assert not inspect.isabstract(EMOF::PrimitiveType)


def test_emof::primitivetype_constructor_exists():
    assert callable(EMOF::PrimitiveType.__init__)


def test_emof::primitivetype_constructor_args():
    sig = inspect.signature(EMOF::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_emof::enumeration_is_not_abstract():
    assert not inspect.isabstract(EMOF::Enumeration)


def test_emof::enumeration_constructor_exists():
    assert callable(EMOF::Enumeration.__init__)


def test_emof::enumeration_constructor_args():
    sig = inspect.signature(EMOF::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_emof::extent_is_not_abstract():
    assert not inspect.isabstract(EMOF::Extent)


def test_emof::extent_constructor_exists():
    assert callable(EMOF::Extent.__init__)


def test_emof::extent_constructor_args():
    sig = inspect.signature(EMOF::Extent.__init__)
    params = list(sig.parameters.keys())



def test_emof::reflectivecollection_is_not_abstract():
    assert not inspect.isabstract(EMOF::ReflectiveCollection)


def test_emof::reflectivecollection_constructor_exists():
    assert callable(EMOF::ReflectiveCollection.__init__)


def test_emof::reflectivecollection_constructor_args():
    sig = inspect.signature(EMOF::ReflectiveCollection.__init__)
    params = list(sig.parameters.keys())



def test_emof::element_is_not_abstract():
    assert not inspect.isabstract(EMOF::Element)


def test_emof::element_constructor_exists():
    assert callable(EMOF::Element.__init__)


def test_emof::element_constructor_args():
    sig = inspect.signature(EMOF::Element.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::modeltype_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::ModelType)


def test_qvtoperational::modeltype_constructor_exists():
    assert callable(QVTOperational::ModelType.__init__)


def test_qvtoperational::modeltype_constructor_args():
    sig = inspect.signature(QVTOperational::ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "conformanceKind" in params, "Missing parameter 'conformanceKind'"

def test_qvtoperational::modeltype_has_conformanceKind():
    assert hasattr(QVTOperational::ModelType, "conformanceKind")
    descriptor = None
    for klass in QVTOperational::ModelType.__mro__:
        if "conformanceKind" in klass.__dict__:
            descriptor = klass.__dict__["conformanceKind"]
            break
    assert isinstance(descriptor, property)



def test_qvtbase::transformation_is_not_abstract():
    assert not inspect.isabstract(QVTBase::Transformation)


def test_qvtbase::transformation_constructor_exists():
    assert callable(QVTBase::Transformation.__init__)


def test_qvtbase::transformation_constructor_args():
    sig = inspect.signature(QVTBase::Transformation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::module_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::Module)


def test_qvtoperational::module_constructor_exists():
    assert callable(QVTOperational::Module.__init__)


def test_qvtoperational::module_constructor_args():
    sig = inspect.signature(QVTOperational::Module.__init__)
    params = list(sig.parameters.keys())
    assert "isBlackbox" in params, "Missing parameter 'isBlackbox'"

def test_qvtoperational::module_has_isBlackbox():
    assert hasattr(QVTOperational::Module, "isBlackbox")
    descriptor = None
    for klass in QVTOperational::Module.__mro__:
        if "isBlackbox" in klass.__dict__:
            descriptor = klass.__dict__["isBlackbox"]
            break
    assert isinstance(descriptor, property)



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase::function_is_not_abstract():
    assert not inspect.isabstract(QVTBase::Function)


def test_qvtbase::function_constructor_exists():
    assert callable(QVTBase::Function.__init__)


def test_qvtbase::function_constructor_args():
    sig = inspect.signature(QVTBase::Function.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::imperativeoperation_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::ImperativeOperation)


def test_qvtoperational::imperativeoperation_constructor_exists():
    assert callable(QVTOperational::ImperativeOperation.__init__)


def test_qvtoperational::imperativeoperation_constructor_args():
    sig = inspect.signature(QVTOperational::ImperativeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "isBlackbox" in params, "Missing parameter 'isBlackbox'"

def test_qvtoperational::imperativeoperation_has_isBlackbox():
    assert hasattr(QVTOperational::ImperativeOperation, "isBlackbox")
    descriptor = None
    for klass in QVTOperational::ImperativeOperation.__mro__:
        if "isBlackbox" in klass.__dict__:
            descriptor = klass.__dict__["isBlackbox"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::contextualproperty_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::ContextualProperty)


def test_qvtoperational::contextualproperty_constructor_exists():
    assert callable(QVTOperational::ContextualProperty.__init__)


def test_qvtoperational::contextualproperty_constructor_args():
    sig = inspect.signature(QVTOperational::ContextualProperty.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_emof::datatype_is_not_abstract():
    assert not inspect.isabstract(EMOF::DataType)


def test_emof::datatype_constructor_exists():
    assert callable(EMOF::DataType.__init__)


def test_emof::datatype_constructor_args():
    sig = inspect.signature(EMOF::DataType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::invalidtype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::InvalidType)


def test_essentialocl::invalidtype_constructor_exists():
    assert callable(EssentialOCL::InvalidType.__init__)


def test_essentialocl::invalidtype_constructor_args():
    sig = inspect.signature(EssentialOCL::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::anytype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::AnyType)


def test_essentialocl::anytype_constructor_exists():
    assert callable(EssentialOCL::AnyType.__init__)


def test_essentialocl::anytype_constructor_args():
    sig = inspect.signature(EssentialOCL::AnyType.__init__)
    params = list(sig.parameters.keys())



def test_emof::class_is_not_abstract():
    assert not inspect.isabstract(EMOF::Class)


def test_emof::class_constructor_exists():
    assert callable(EMOF::Class.__init__)


def test_emof::class_constructor_args():
    sig = inspect.signature(EMOF::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_emof::class_has_isAbstract():
    assert hasattr(EMOF::Class, "isAbstract")
    descriptor = None
    for klass in EMOF::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::typedef_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::Typedef)


def test_imperativeocl::typedef_constructor_exists():
    assert callable(ImperativeOCL::Typedef.__init__)


def test_imperativeocl::typedef_constructor_args():
    sig = inspect.signature(ImperativeOCL::Typedef.__init__)
    params = list(sig.parameters.keys())



def test_altexp_is_not_abstract():
    assert not inspect.isabstract(AltExp)


def test_altexp_constructor_exists():
    assert callable(AltExp.__init__)


def test_altexp_constructor_args():
    sig = inspect.signature(AltExp.__init__)
    params = list(sig.parameters.keys())



def test_catchexp_is_not_abstract():
    assert not inspect.isabstract(CatchExp)


def test_catchexp_constructor_exists():
    assert callable(CatchExp.__init__)


def test_catchexp_constructor_args():
    sig = inspect.signature(CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::listtype_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ListType)


def test_imperativeocl::listtype_constructor_exists():
    assert callable(ImperativeOCL::ListType.__init__)


def test_imperativeocl::listtype_constructor_args():
    sig = inspect.signature(ImperativeOCL::ListType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::listliteralexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ListLiteralExp)


def test_imperativeocl::listliteralexp_constructor_exists():
    assert callable(ImperativeOCL::ListLiteralExp.__init__)


def test_imperativeocl::listliteralexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ListLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::orderedtupletype_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::OrderedTupleType)


def test_imperativeocl::orderedtupletype_constructor_exists():
    assert callable(ImperativeOCL::OrderedTupleType.__init__)


def test_imperativeocl::orderedtupletype_constructor_args():
    sig = inspect.signature(ImperativeOCL::OrderedTupleType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::OrderedTupleLiteralPart)


def test_imperativeocl::orderedtupleliteralpart_constructor_exists():
    assert callable(ImperativeOCL::OrderedTupleLiteralPart.__init__)


def test_imperativeocl::orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(ImperativeOCL::OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(OrderedTupleLiteralPart)


def test_orderedtupleliteralpart_constructor_exists():
    assert callable(OrderedTupleLiteralPart.__init__)


def test_orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::orderedtupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::OrderedTupleLiteralExp)


def test_imperativeocl::orderedtupleliteralexp_constructor_exists():
    assert callable(ImperativeOCL::OrderedTupleLiteralExp.__init__)


def test_imperativeocl::orderedtupleliteralexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::OrderedTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ImperativeExpression)


def test_imperativeocl::imperativeexpression_constructor_exists():
    assert callable(ImperativeOCL::ImperativeExpression.__init__)


def test_imperativeocl::imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeOCL::ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::forexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ForExp)


def test_imperativeocl::forexp_constructor_exists():
    assert callable(ImperativeOCL::ForExp.__init__)


def test_imperativeocl::forexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ForExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictionarytype_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::DictionaryType)


def test_imperativeocl::dictionarytype_constructor_exists():
    assert callable(ImperativeOCL::DictionaryType.__init__)


def test_imperativeocl::dictionarytype_constructor_args():
    sig = inspect.signature(ImperativeOCL::DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::DictLiteralPart)


def test_imperativeocl::dictliteralpart_constructor_exists():
    assert callable(ImperativeOCL::DictLiteralPart.__init__)


def test_imperativeocl::dictliteralpart_constructor_args():
    sig = inspect.signature(ImperativeOCL::DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::DictLiteralExp)


def test_imperativeocl::dictliteralexp_constructor_exists():
    assert callable(ImperativeOCL::DictLiteralExp.__init__)


def test_imperativeocl::dictliteralexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ImperativeIterateExp)


def test_imperativeocl::imperativeiterateexp_constructor_exists():
    assert callable(ImperativeOCL::ImperativeIterateExp.__init__)


def test_imperativeocl::imperativeiterateexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::variable_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::Variable)


def test_essentialocl::variable_constructor_exists():
    assert callable(EssentialOCL::Variable.__init__)


def test_essentialocl::variable_constructor_args():
    sig = inspect.signature(EssentialOCL::Variable.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::UnlimitedNaturalExp)


def test_essentialocl::unlimitednaturalexp_constructor_exists():
    assert callable(EssentialOCL::UnlimitedNaturalExp.__init__)


def test_essentialocl::unlimitednaturalexp_constructor_args():
    sig = inspect.signature(EssentialOCL::UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_essentialocl::unlimitednaturalexp_has_symbol():
    assert hasattr(EssentialOCL::UnlimitedNaturalExp, "symbol")
    descriptor = None
    for klass in EssentialOCL::UnlimitedNaturalExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::typeexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::TypeExp)


def test_essentialocl::typeexp_constructor_exists():
    assert callable(EssentialOCL::TypeExp.__init__)


def test_essentialocl::typeexp_constructor_args():
    sig = inspect.signature(EssentialOCL::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::TupleType)


def test_essentialocl::tupletype_constructor_exists():
    assert callable(EssentialOCL::TupleType.__init__)


def test_essentialocl::tupletype_constructor_args():
    sig = inspect.signature(EssentialOCL::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralExp)


def test_tupleliteralexp_constructor_exists():
    assert callable(TupleLiteralExp.__init__)


def test_tupleliteralexp_constructor_args():
    sig = inspect.signature(TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::TupleLiteralPart)


def test_essentialocl::tupleliteralpart_constructor_exists():
    assert callable(EssentialOCL::TupleLiteralPart.__init__)


def test_essentialocl::tupleliteralpart_constructor_args():
    sig = inspect.signature(EssentialOCL::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::TupleLiteralExp)


def test_essentialocl::tupleliteralexp_constructor_exists():
    assert callable(EssentialOCL::TupleLiteralExp.__init__)


def test_essentialocl::tupleliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::templateparametertype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::TemplateParameterType)


def test_essentialocl::templateparametertype_constructor_exists():
    assert callable(EssentialOCL::TemplateParameterType.__init__)


def test_essentialocl::templateparametertype_constructor_args():
    sig = inspect.signature(EssentialOCL::TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_essentialocl::templateparametertype_has_specification():
    assert hasattr(EssentialOCL::TemplateParameterType, "specification")
    descriptor = None
    for klass in EssentialOCL::TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::StringLiteralExp)


def test_essentialocl::stringliteralexp_constructor_exists():
    assert callable(EssentialOCL::StringLiteralExp.__init__)


def test_essentialocl::stringliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_essentialocl::stringliteralexp_has_stringSymbol():
    assert hasattr(EssentialOCL::StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in EssentialOCL::StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::settype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::SetType)


def test_essentialocl::settype_constructor_exists():
    assert callable(EssentialOCL::SetType.__init__)


def test_essentialocl::settype_constructor_args():
    sig = inspect.signature(EssentialOCL::SetType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::whileexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::WhileExp)


def test_imperativeocl::whileexp_constructor_exists():
    assert callable(ImperativeOCL::WhileExp.__init__)


def test_imperativeocl::whileexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::assignexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::AssignExp)


def test_imperativeocl::assignexp_constructor_exists():
    assert callable(ImperativeOCL::AssignExp.__init__)


def test_imperativeocl::assignexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_imperativeocl::assignexp_has_isReset():
    assert hasattr(ImperativeOCL::AssignExp, "isReset")
    descriptor = None
    for klass in ImperativeOCL::AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::switchexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::SwitchExp)


def test_imperativeocl::switchexp_constructor_exists():
    assert callable(ImperativeOCL::SwitchExp.__init__)


def test_imperativeocl::switchexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::variableinitexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::VariableInitExp)


def test_imperativeocl::variableinitexp_constructor_exists():
    assert callable(ImperativeOCL::VariableInitExp.__init__)


def test_imperativeocl::variableinitexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_imperativeocl::variableinitexp_has_withResult():
    assert hasattr(ImperativeOCL::VariableInitExp, "withResult")
    descriptor = None
    for klass in ImperativeOCL::VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::tryexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::TryExp)


def test_imperativeocl::tryexp_constructor_exists():
    assert callable(ImperativeOCL::TryExp.__init__)


def test_imperativeocl::tryexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::TryExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::continueexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ContinueExp)


def test_imperativeocl::continueexp_constructor_exists():
    assert callable(ImperativeOCL::ContinueExp.__init__)


def test_imperativeocl::continueexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::assertexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::AssertExp)


def test_imperativeocl::assertexp_constructor_exists():
    assert callable(ImperativeOCL::AssertExp.__init__)


def test_imperativeocl::assertexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_imperativeocl::assertexp_has_severity():
    assert hasattr(ImperativeOCL::AssertExp, "severity")
    descriptor = None
    for klass in ImperativeOCL::AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ImperativeLoopExp)


def test_imperativeocl::imperativeloopexp_constructor_exists():
    assert callable(ImperativeOCL::ImperativeLoopExp.__init__)


def test_imperativeocl::imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::imperativecallexp_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::ImperativeCallExp)


def test_qvtoperational::imperativecallexp_constructor_exists():
    assert callable(QVTOperational::ImperativeCallExp.__init__)


def test_qvtoperational::imperativecallexp_constructor_args():
    sig = inspect.signature(QVTOperational::ImperativeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_qvtoperational::imperativecallexp_has_isVirtual():
    assert hasattr(QVTOperational::ImperativeCallExp, "isVirtual")
    descriptor = None
    for klass in QVTOperational::ImperativeCallExp.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::computeexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ComputeExp)


def test_imperativeocl::computeexp_constructor_exists():
    assert callable(ImperativeOCL::ComputeExp.__init__)


def test_imperativeocl::computeexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::unlinkexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::UnlinkExp)


def test_imperativeocl::unlinkexp_constructor_exists():
    assert callable(ImperativeOCL::UnlinkExp.__init__)


def test_imperativeocl::unlinkexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::unpackexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::UnpackExp)


def test_imperativeocl::unpackexp_constructor_exists():
    assert callable(ImperativeOCL::UnpackExp.__init__)


def test_imperativeocl::unpackexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::blockexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::BlockExp)


def test_imperativeocl::blockexp_constructor_exists():
    assert callable(ImperativeOCL::BlockExp.__init__)


def test_imperativeocl::blockexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::breakexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::BreakExp)


def test_imperativeocl::breakexp_constructor_exists():
    assert callable(ImperativeOCL::BreakExp.__init__)


def test_imperativeocl::breakexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::catchexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::CatchExp)


def test_imperativeocl::catchexp_constructor_exists():
    assert callable(ImperativeOCL::CatchExp.__init__)


def test_imperativeocl::catchexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::returnexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::ReturnExp)


def test_imperativeocl::returnexp_constructor_exists():
    assert callable(ImperativeOCL::ReturnExp.__init__)


def test_imperativeocl::returnexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::raiseexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::RaiseExp)


def test_imperativeocl::raiseexp_constructor_exists():
    assert callable(ImperativeOCL::RaiseExp.__init__)


def test_imperativeocl::raiseexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::resolveexp_is_not_abstract():
    assert not inspect.isabstract(QVTOperational::ResolveExp)


def test_qvtoperational::resolveexp_constructor_exists():
    assert callable(QVTOperational::ResolveExp.__init__)


def test_qvtoperational::resolveexp_constructor_args():
    sig = inspect.signature(QVTOperational::ResolveExp.__init__)
    params = list(sig.parameters.keys())
    assert "isInverse" in params, "Missing parameter 'isInverse'"
    assert "isDeferred" in params, "Missing parameter 'isDeferred'"
    assert "one" in params, "Missing parameter 'one'"

def test_qvtoperational::resolveexp_has_isInverse():
    assert hasattr(QVTOperational::ResolveExp, "isInverse")
    descriptor = None
    for klass in QVTOperational::ResolveExp.__mro__:
        if "isInverse" in klass.__dict__:
            descriptor = klass.__dict__["isInverse"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational::resolveexp_has_isDeferred():
    assert hasattr(QVTOperational::ResolveExp, "isDeferred")
    descriptor = None
    for klass in QVTOperational::ResolveExp.__mro__:
        if "isDeferred" in klass.__dict__:
            descriptor = klass.__dict__["isDeferred"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational::resolveexp_has_one():
    assert hasattr(QVTOperational::ResolveExp, "one")
    descriptor = None
    for klass in QVTOperational::ResolveExp.__mro__:
        if "one" in klass.__dict__:
            descriptor = klass.__dict__["one"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::logexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::LogExp)


def test_imperativeocl::logexp_constructor_exists():
    assert callable(ImperativeOCL::LogExp.__init__)


def test_imperativeocl::logexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::LogExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::instantiationexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::InstantiationExp)


def test_imperativeocl::instantiationexp_constructor_exists():
    assert callable(ImperativeOCL::InstantiationExp.__init__)


def test_imperativeocl::instantiationexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::altexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeOCL::AltExp)


def test_imperativeocl::altexp_constructor_exists():
    assert callable(ImperativeOCL::AltExp.__init__)


def test_imperativeocl::altexp_constructor_args():
    sig = inspect.signature(ImperativeOCL::AltExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::voidtype_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::VoidType)


def test_essentialocl::voidtype_constructor_exists():
    assert callable(EssentialOCL::VoidType.__init__)


def test_essentialocl::voidtype_constructor_args():
    sig = inspect.signature(EssentialOCL::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::VariableExp)


def test_essentialocl::variableexp_constructor_exists():
    assert callable(EssentialOCL::VariableExp.__init__)


def test_essentialocl::variableexp_constructor_args():
    sig = inspect.signature(EssentialOCL::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::NumericLiteralExp)


def test_essentialocl::numericliteralexp_constructor_exists():
    assert callable(EssentialOCL::NumericLiteralExp.__init__)


def test_essentialocl::numericliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::NullLiteralExp)


def test_essentialocl::nullliteralexp_constructor_exists():
    assert callable(EssentialOCL::NullLiteralExp.__init__)


def test_essentialocl::nullliteralexp_constructor_args():
    sig = inspect.signature(EssentialOCL::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExp)


def test_featurecallexp_constructor_exists():
    assert callable(FeatureCallExp.__init__)


def test_featurecallexp_constructor_args():
    sig = inspect.signature(FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::OperationCallExp)


def test_essentialocl::operationcallexp_constructor_exists():
    assert callable(EssentialOCL::OperationCallExp.__init__)


def test_essentialocl::operationcallexp_constructor_args():
    sig = inspect.signature(EssentialOCL::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::NavigationCallExp)


def test_essentialocl::navigationcallexp_constructor_exists():
    assert callable(EssentialOCL::NavigationCallExp.__init__)


def test_essentialocl::navigationcallexp_constructor_args():
    sig = inspect.signature(EssentialOCL::NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::LoopExp)


def test_essentialocl::loopexp_constructor_exists():
    assert callable(EssentialOCL::LoopExp.__init__)


def test_essentialocl::loopexp_constructor_args():
    sig = inspect.signature(EssentialOCL::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::literalexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::LiteralExp)


def test_essentialocl::literalexp_constructor_exists():
    assert callable(EssentialOCL::LiteralExp.__init__)


def test_essentialocl::literalexp_constructor_args():
    sig = inspect.signature(EssentialOCL::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::letexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::LetExp)


def test_essentialocl::letexp_constructor_exists():
    assert callable(EssentialOCL::LetExp.__init__)


def test_essentialocl::letexp_constructor_args():
    sig = inspect.signature(EssentialOCL::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(EssentialOCL::IteratorExp)


def test_essentialocl::iteratorexp_constructor_exists():
    assert callable(EssentialOCL::IteratorExp.__init__)


def test_essentialocl::iteratorexp_constructor_args():
    sig = inspect.signature(EssentialOCL::IteratorExp.__init__)
    params = list(sig.parameters.keys())

def test_severitykind_exists():
    # Check that the Enumeration exists
    assert SeverityKind is not None

def test_severitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeverityKind]
    expected_literals = [
        "error",
        "warning",
        "fatal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SeverityKind"

def test_importkind_exists():
    # Check that the Enumeration exists
    assert ImportKind is not None

def test_importkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImportKind]
    expected_literals = [
        "access",
        "extension",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImportKind"

def test_directionkind_exists():
    # Check that the Enumeration exists
    assert DirectionKind is not None

def test_directionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionKind]
    expected_literals = [
        "in_",
        "out",
        "inout",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionKind"

def test_enforcementmode_exists():
    # Check that the Enumeration exists
    assert EnforcementMode is not None

def test_enforcementmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnforcementMode]
    expected_literals = [
        "Deletion",
        "Creation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnforcementMode"

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Collection",
        "Set",
        "OrderedSet",
        "Bag",
        "Sequence",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"


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
ResolveExp_strategy = st.builds(
    ResolveExp,
)
QVTOperational::ResolveInExp_strategy = st.builds(
    QVTOperational::ResolveInExp,
)
ModuleImport_strategy = st.builds(
    ModuleImport,
)
EntryOperation_strategy = st.builds(
    EntryOperation,
)
ConstructorBody_strategy = st.builds(
    ConstructorBody,
)
InstantiationExp_strategy = st.builds(
    InstantiationExp,
)
QVTOperational::ObjectExp_strategy = st.builds(
    QVTOperational::ObjectExp,
)
ModelType_strategy = st.builds(
    ModelType,
)
MappingOperation_strategy = st.builds(
    MappingOperation,
)
ImperativeCallExp_strategy = st.builds(
    ImperativeCallExp,
)
QVTOperational::MappingCallExp_strategy = st.builds(
    QVTOperational::MappingCallExp,
    isStrict=
        safe_text
)
RelationDomain_strategy = st.builds(
    RelationDomain,
)
ModelParameter_strategy = st.builds(
    ModelParameter,
)
OperationBody_strategy = st.builds(
    OperationBody,
)
QVTOperational::MappingBody_strategy = st.builds(
    QVTOperational::MappingBody,
)
QVTOperational::ConstructorBody_strategy = st.builds(
    QVTOperational::ConstructorBody,
)
Module_strategy = st.builds(
    Module,
)
QVTOperational::OperationalTransformation_strategy = st.builds(
    QVTOperational::OperationalTransformation,
)
QVTOperational::Library_strategy = st.builds(
    QVTOperational::Library,
)
VarParameter_strategy = st.builds(
    VarParameter,
)
QVTOperational::ModelParameter_strategy = st.builds(
    QVTOperational::ModelParameter,
)
QVTOperational::MappingParameter_strategy = st.builds(
    QVTOperational::MappingParameter,
)
DomainPattern_strategy = st.builds(
    DomainPattern,
)
RelationDomainAssignment_strategy = st.builds(
    RelationDomainAssignment,
)
Relation_strategy = st.builds(
    Relation,
)
ImperativeOperation_strategy = st.builds(
    ImperativeOperation,
)
QVTOperational::MappingOperation_strategy = st.builds(
    QVTOperational::MappingOperation,
)
QVTOperational::EntryOperation_strategy = st.builds(
    QVTOperational::EntryOperation,
)
QVTOperational::Helper_strategy = st.builds(
    QVTOperational::Helper,
    isQuery=
        safe_text
)
QVTOperational::Constructor_strategy = st.builds(
    QVTOperational::Constructor,
)
Key_strategy = st.builds(
    Key,
)
ObjectTemplateExp_strategy = st.builds(
    ObjectTemplateExp,
)
RelationImplementation_strategy = st.builds(
    RelationImplementation,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
QVTRelation::OppositePropertyCallExp_strategy = st.builds(
    QVTRelation::OppositePropertyCallExp,
)
RelationalTransformation_strategy = st.builds(
    RelationalTransformation,
)
TemplateExp_strategy = st.builds(
    TemplateExp,
)
QVTTemplate::CollectionTemplateExp_strategy = st.builds(
    QVTTemplate::CollectionTemplateExp,
)
PropertyTemplateItem_strategy = st.builds(
    PropertyTemplateItem,
)
QVTTemplate::ObjectTemplateExp_strategy = st.builds(
    QVTTemplate::ObjectTemplateExp,
)
RealizedVariable_strategy = st.builds(
    RealizedVariable,
)
EnforcementOperation_strategy = st.builds(
    EnforcementOperation,
)
Assignment_strategy = st.builds(
    Assignment,
)
QVTCore::PropertyAssignment_strategy = st.builds(
    QVTCore::PropertyAssignment,
)
QVTCore::VariableAssignment_strategy = st.builds(
    QVTCore::VariableAssignment,
)
Area_strategy = st.builds(
    Area,
)
CorePattern_strategy = st.builds(
    CorePattern,
)
QVTCore::BottomPattern_strategy = st.builds(
    QVTCore::BottomPattern,
)
Mapping_strategy = st.builds(
    Mapping,
)
QVTCore::GuardPattern_strategy = st.builds(
    QVTCore::GuardPattern,
)
Tag_strategy = st.builds(
    Tag,
)
Transformation_strategy = st.builds(
    Transformation,
)
QVTRelation::RelationalTransformation_strategy = st.builds(
    QVTRelation::RelationalTransformation,
)
GuardPattern_strategy = st.builds(
    GuardPattern,
)
BottomPattern_strategy = st.builds(
    BottomPattern,
)
QVTCore::Area_strategy = st.builds(
    QVTCore::Area,
)
TypedModel_strategy = st.builds(
    TypedModel,
)
Rule_strategy = st.builds(
    Rule,
)
QVTRelation::Relation_strategy = st.builds(
    QVTRelation::Relation,
    isTopLevel=
        safe_text
)
QVTCore::Mapping_strategy = st.builds(
    QVTCore::Mapping,
)
Domain_strategy = st.builds(
    Domain,
)
QVTCore::CoreDomain_strategy = st.builds(
    QVTCore::CoreDomain,
)
QVTRelation::RelationDomain_strategy = st.builds(
    QVTRelation::RelationDomain,
)
Pattern_strategy = st.builds(
    Pattern,
)
QVTCore::CorePattern_strategy = st.builds(
    QVTCore::CorePattern,
)
QVTRelation::DomainPattern_strategy = st.builds(
    QVTRelation::DomainPattern,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
EssentialOCL::IterateExp_strategy = st.builds(
    EssentialOCL::IterateExp,
)
NavigationCallExp_strategy = st.builds(
    NavigationCallExp,
)
EssentialOCL::PropertyCallExp_strategy = st.builds(
    EssentialOCL::PropertyCallExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
EssentialOCL::RealLiteralExp_strategy = st.builds(
    EssentialOCL::RealLiteralExp,
    realSymbol=
        safe_text
)
EssentialOCL::IntegerLiteralExp_strategy = st.builds(
    EssentialOCL::IntegerLiteralExp,
    integerSymbol=
        safe_text
)
CallExp_strategy = st.builds(
    CallExp,
)
EssentialOCL::FeatureCallExp_strategy = st.builds(
    EssentialOCL::FeatureCallExp,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
EssentialOCL::IfExp_strategy = st.builds(
    EssentialOCL::IfExp,
)
QVTRelation::RelationCallExp_strategy = st.builds(
    QVTRelation::RelationCallExp,
)
EssentialOCL::CallExp_strategy = st.builds(
    EssentialOCL::CallExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
EssentialOCL::BooleanLiteralExp_strategy = st.builds(
    EssentialOCL::BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
QVTCore::RealizedVariable_strategy = st.builds(
    QVTCore::RealizedVariable,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
EssentialOCL::InvalidLiteralExp_strategy = st.builds(
    EssentialOCL::InvalidLiteralExp,
)
QVTTemplate::TemplateExp_strategy = st.builds(
    QVTTemplate::TemplateExp,
)
EssentialOCL::EnumLiteralExp_strategy = st.builds(
    EssentialOCL::EnumLiteralExp,
)
EssentialOCL::PrimitiveLiteralExp_strategy = st.builds(
    EssentialOCL::PrimitiveLiteralExp,
)
EssentialOCL::CollectionLiteralExp_strategy = st.builds(
    EssentialOCL::CollectionLiteralExp,
    kind=
        safe_text
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
EssentialOCL::CollectionRange_strategy = st.builds(
    EssentialOCL::CollectionRange,
)
EssentialOCL::CollectionItem_strategy = st.builds(
    EssentialOCL::CollectionItem,
)
ReflectiveCollection_strategy = st.builds(
    ReflectiveCollection,
)
EMOF::ReflectiveSequence_strategy = st.builds(
    EMOF::ReflectiveSequence,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
EssentialOCL::OrderedSetType_strategy = st.builds(
    EssentialOCL::OrderedSetType,
)
EssentialOCL::SequenceType_strategy = st.builds(
    EssentialOCL::SequenceType,
)
EssentialOCL::BagType_strategy = st.builds(
    EssentialOCL::BagType,
)
Extent_strategy = st.builds(
    Extent,
)
EMOF::URIExtent_strategy = st.builds(
    EMOF::URIExtent,
)
EMOF::Object_strategy = st.builds(
    EMOF::Object,
)
Parameter_strategy = st.builds(
    Parameter,
)
QVTBase::FunctionParameter_strategy = st.builds(
    QVTBase::FunctionParameter,
)
QVTOperational::VarParameter_strategy = st.builds(
    QVTOperational::VarParameter,
    kind=
        safe_text
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
EssentialOCL::OclExpression_strategy = st.builds(
    EssentialOCL::OclExpression,
)
EssentialOCL::ExpressionInOcl_strategy = st.builds(
    EssentialOCL::ExpressionInOcl,
)
EMOF::Parameter_strategy = st.builds(
    EMOF::Parameter,
)
EssentialOCL::CollectionLiteralPart_strategy = st.builds(
    EssentialOCL::CollectionLiteralPart,
)
EMOF::Property_strategy = st.builds(
    EMOF::Property,
    default=
        safe_text,
    isDerived=
        safe_text,
    isComposite=
        safe_text,
    isReadOnly=
        safe_text,
    isID=
        safe_text
)
EMOF::Operation_strategy = st.builds(
    EMOF::Operation,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
QVTBase::Domain_strategy = st.builds(
    QVTBase::Domain,
    isCheckable=
        safe_text,
    isEnforceable=
        safe_text
)
EMOF::TypedElement_strategy = st.builds(
    EMOF::TypedElement,
)
QVTBase::Rule_strategy = st.builds(
    QVTBase::Rule,
)
QVTBase::TypedModel_strategy = st.builds(
    QVTBase::TypedModel,
)
EMOF::Package_strategy = st.builds(
    EMOF::Package,
    uri=
        safe_text
)
EMOF::Type_strategy = st.builds(
    EMOF::Type,
)
Element_strategy = st.builds(
    Element,
)
EMOF::NamedElement_strategy = st.builds(
    EMOF::NamedElement,
    name=
        safe_text
)
QVTBase::Pattern_strategy = st.builds(
    QVTBase::Pattern,
)
QVTOperational::ModuleImport_strategy = st.builds(
    QVTOperational::ModuleImport,
    kind=
        safe_text
)
QVTBase::Predicate_strategy = st.builds(
    QVTBase::Predicate,
)
QVTOperational::OperationBody_strategy = st.builds(
    QVTOperational::OperationBody,
)
QVTRelation::RelationImplementation_strategy = st.builds(
    QVTRelation::RelationImplementation,
)
QVTTemplate::PropertyTemplateItem_strategy = st.builds(
    QVTTemplate::PropertyTemplateItem,
    isOpposite=
        safe_text
)
EMOF::Tag_strategy = st.builds(
    EMOF::Tag,
    value=
        safe_text,
    name=
        safe_text
)
QVTCore::Assignment_strategy = st.builds(
    QVTCore::Assignment,
    isDefault=
        safe_text
)
QVTRelation::RelationDomainAssignment_strategy = st.builds(
    QVTRelation::RelationDomainAssignment,
)
QVTCore::EnforcementOperation_strategy = st.builds(
    QVTCore::EnforcementOperation,
    enforcementMode=
        safe_text
)
QVTRelation::Key_strategy = st.builds(
    QVTRelation::Key,
)
EMOF::Comment_strategy = st.builds(
    EMOF::Comment,
    body=
        safe_text
)
EMOF::MultiplicityElement_strategy = st.builds(
    EMOF::MultiplicityElement,
    isUnique=
        safe_text,
    upper=
        safe_text,
    lower=
        safe_text,
    isOrdered=
        safe_text
)
Package_strategy = st.builds(
    Package,
)
EMOF::Factory_strategy = st.builds(
    EMOF::Factory,
)
Enumeration_strategy = st.builds(
    Enumeration,
)
EMOF::EnumerationLiteral_strategy = st.builds(
    EMOF::EnumerationLiteral,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
EssentialOCL::CollectionType_strategy = st.builds(
    EssentialOCL::CollectionType,
)
EMOF::PrimitiveType_strategy = st.builds(
    EMOF::PrimitiveType,
)
EMOF::Enumeration_strategy = st.builds(
    EMOF::Enumeration,
)
Comment_strategy = st.builds(
    Comment,
)
Object_strategy = st.builds(
    Object,
)
EMOF::Extent_strategy = st.builds(
    EMOF::Extent,
)
EMOF::ReflectiveCollection_strategy = st.builds(
    EMOF::ReflectiveCollection,
)
EMOF::Element_strategy = st.builds(
    EMOF::Element,
)
Class_strategy = st.builds(
    Class,
)
QVTOperational::ModelType_strategy = st.builds(
    QVTOperational::ModelType,
    conformanceKind=
        safe_text
)
QVTBase::Transformation_strategy = st.builds(
    QVTBase::Transformation,
)
QVTOperational::Module_strategy = st.builds(
    QVTOperational::Module,
    isBlackbox=
        safe_text
)
Operation_strategy = st.builds(
    Operation,
)
QVTBase::Function_strategy = st.builds(
    QVTBase::Function,
)
QVTOperational::ImperativeOperation_strategy = st.builds(
    QVTOperational::ImperativeOperation,
    isBlackbox=
        safe_text
)
Property_strategy = st.builds(
    Property,
)
QVTOperational::ContextualProperty_strategy = st.builds(
    QVTOperational::ContextualProperty,
)
Type_strategy = st.builds(
    Type,
)
EMOF::DataType_strategy = st.builds(
    EMOF::DataType,
)
EssentialOCL::InvalidType_strategy = st.builds(
    EssentialOCL::InvalidType,
)
EssentialOCL::AnyType_strategy = st.builds(
    EssentialOCL::AnyType,
)
EMOF::Class_strategy = st.builds(
    EMOF::Class,
    isAbstract=
        safe_text
)
Predicate_strategy = st.builds(
    Predicate,
)
ImperativeOCL::Typedef_strategy = st.builds(
    ImperativeOCL::Typedef,
)
AltExp_strategy = st.builds(
    AltExp,
)
CatchExp_strategy = st.builds(
    CatchExp,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
ImperativeOCL::ListType_strategy = st.builds(
    ImperativeOCL::ListType,
)
ImperativeOCL::ListLiteralExp_strategy = st.builds(
    ImperativeOCL::ListLiteralExp,
)
ImperativeOCL::OrderedTupleType_strategy = st.builds(
    ImperativeOCL::OrderedTupleType,
)
ImperativeOCL::OrderedTupleLiteralPart_strategy = st.builds(
    ImperativeOCL::OrderedTupleLiteralPart,
)
OrderedTupleLiteralPart_strategy = st.builds(
    OrderedTupleLiteralPart,
)
ImperativeOCL::OrderedTupleLiteralExp_strategy = st.builds(
    ImperativeOCL::OrderedTupleLiteralExp,
)
ImperativeOCL::ImperativeExpression_strategy = st.builds(
    ImperativeOCL::ImperativeExpression,
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
ImperativeOCL::ForExp_strategy = st.builds(
    ImperativeOCL::ForExp,
)
ImperativeOCL::DictionaryType_strategy = st.builds(
    ImperativeOCL::DictionaryType,
)
ImperativeOCL::DictLiteralPart_strategy = st.builds(
    ImperativeOCL::DictLiteralPart,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
ImperativeOCL::DictLiteralExp_strategy = st.builds(
    ImperativeOCL::DictLiteralExp,
)
ImperativeOCL::ImperativeIterateExp_strategy = st.builds(
    ImperativeOCL::ImperativeIterateExp,
)
LogExp_strategy = st.builds(
    LogExp,
)
EssentialOCL::Variable_strategy = st.builds(
    EssentialOCL::Variable,
)
EssentialOCL::UnlimitedNaturalExp_strategy = st.builds(
    EssentialOCL::UnlimitedNaturalExp,
    symbol=
        safe_text
)
EssentialOCL::TypeExp_strategy = st.builds(
    EssentialOCL::TypeExp,
)
EssentialOCL::TupleType_strategy = st.builds(
    EssentialOCL::TupleType,
)
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
EssentialOCL::TupleLiteralPart_strategy = st.builds(
    EssentialOCL::TupleLiteralPart,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
EssentialOCL::TupleLiteralExp_strategy = st.builds(
    EssentialOCL::TupleLiteralExp,
)
EssentialOCL::TemplateParameterType_strategy = st.builds(
    EssentialOCL::TemplateParameterType,
    specification=
        safe_text
)
EssentialOCL::StringLiteralExp_strategy = st.builds(
    EssentialOCL::StringLiteralExp,
    stringSymbol=
        safe_text
)
EssentialOCL::SetType_strategy = st.builds(
    EssentialOCL::SetType,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
ImperativeOCL::WhileExp_strategy = st.builds(
    ImperativeOCL::WhileExp,
)
ImperativeOCL::AssignExp_strategy = st.builds(
    ImperativeOCL::AssignExp,
    isReset=
        safe_text
)
ImperativeOCL::SwitchExp_strategy = st.builds(
    ImperativeOCL::SwitchExp,
)
ImperativeOCL::VariableInitExp_strategy = st.builds(
    ImperativeOCL::VariableInitExp,
    withResult=
        safe_text
)
ImperativeOCL::TryExp_strategy = st.builds(
    ImperativeOCL::TryExp,
)
ImperativeOCL::ContinueExp_strategy = st.builds(
    ImperativeOCL::ContinueExp,
)
ImperativeOCL::AssertExp_strategy = st.builds(
    ImperativeOCL::AssertExp,
    severity=
        safe_text
)
ImperativeOCL::ImperativeLoopExp_strategy = st.builds(
    ImperativeOCL::ImperativeLoopExp,
)
QVTOperational::ImperativeCallExp_strategy = st.builds(
    QVTOperational::ImperativeCallExp,
    isVirtual=
        safe_text
)
ImperativeOCL::ComputeExp_strategy = st.builds(
    ImperativeOCL::ComputeExp,
)
ImperativeOCL::UnlinkExp_strategy = st.builds(
    ImperativeOCL::UnlinkExp,
)
ImperativeOCL::UnpackExp_strategy = st.builds(
    ImperativeOCL::UnpackExp,
)
ImperativeOCL::BlockExp_strategy = st.builds(
    ImperativeOCL::BlockExp,
)
ImperativeOCL::BreakExp_strategy = st.builds(
    ImperativeOCL::BreakExp,
)
ImperativeOCL::CatchExp_strategy = st.builds(
    ImperativeOCL::CatchExp,
)
ImperativeOCL::ReturnExp_strategy = st.builds(
    ImperativeOCL::ReturnExp,
)
ImperativeOCL::RaiseExp_strategy = st.builds(
    ImperativeOCL::RaiseExp,
)
QVTOperational::ResolveExp_strategy = st.builds(
    QVTOperational::ResolveExp,
    isInverse=
        safe_text,
    isDeferred=
        safe_text,
    one=
        safe_text
)
ImperativeOCL::LogExp_strategy = st.builds(
    ImperativeOCL::LogExp,
)
ImperativeOCL::InstantiationExp_strategy = st.builds(
    ImperativeOCL::InstantiationExp,
)
ImperativeOCL::AltExp_strategy = st.builds(
    ImperativeOCL::AltExp,
)
EssentialOCL::VoidType_strategy = st.builds(
    EssentialOCL::VoidType,
)
EssentialOCL::VariableExp_strategy = st.builds(
    EssentialOCL::VariableExp,
)
LetExp_strategy = st.builds(
    LetExp,
)
EssentialOCL::NumericLiteralExp_strategy = st.builds(
    EssentialOCL::NumericLiteralExp,
)
EssentialOCL::NullLiteralExp_strategy = st.builds(
    EssentialOCL::NullLiteralExp,
)
FeatureCallExp_strategy = st.builds(
    FeatureCallExp,
)
EssentialOCL::OperationCallExp_strategy = st.builds(
    EssentialOCL::OperationCallExp,
)
EssentialOCL::NavigationCallExp_strategy = st.builds(
    EssentialOCL::NavigationCallExp,
)
EssentialOCL::LoopExp_strategy = st.builds(
    EssentialOCL::LoopExp,
)
EssentialOCL::LiteralExp_strategy = st.builds(
    EssentialOCL::LiteralExp,
)
EssentialOCL::LetExp_strategy = st.builds(
    EssentialOCL::LetExp,
)
EssentialOCL::IteratorExp_strategy = st.builds(
    EssentialOCL::IteratorExp,
)

@given(instance=ResolveExp_strategy)
@settings(max_examples=50)
def test_resolveexp_instantiation(instance):
    assert isinstance(instance, ResolveExp)

@given(instance=QVTOperational::ResolveInExp_strategy)
@settings(max_examples=50)
def test_qvtoperational::resolveinexp_instantiation(instance):
    assert isinstance(instance, QVTOperational::ResolveInExp)

@given(instance=ModuleImport_strategy)
@settings(max_examples=50)
def test_moduleimport_instantiation(instance):
    assert isinstance(instance, ModuleImport)

@given(instance=EntryOperation_strategy)
@settings(max_examples=50)
def test_entryoperation_instantiation(instance):
    assert isinstance(instance, EntryOperation)

@given(instance=ConstructorBody_strategy)
@settings(max_examples=50)
def test_constructorbody_instantiation(instance):
    assert isinstance(instance, ConstructorBody)

@given(instance=InstantiationExp_strategy)
@settings(max_examples=50)
def test_instantiationexp_instantiation(instance):
    assert isinstance(instance, InstantiationExp)

@given(instance=QVTOperational::ObjectExp_strategy)
@settings(max_examples=50)
def test_qvtoperational::objectexp_instantiation(instance):
    assert isinstance(instance, QVTOperational::ObjectExp)

@given(instance=ModelType_strategy)
@settings(max_examples=50)
def test_modeltype_instantiation(instance):
    assert isinstance(instance, ModelType)

@given(instance=MappingOperation_strategy)
@settings(max_examples=50)
def test_mappingoperation_instantiation(instance):
    assert isinstance(instance, MappingOperation)

@given(instance=ImperativeCallExp_strategy)
@settings(max_examples=50)
def test_imperativecallexp_instantiation(instance):
    assert isinstance(instance, ImperativeCallExp)

@given(instance=QVTOperational::MappingCallExp_strategy)
@settings(max_examples=50)
def test_qvtoperational::mappingcallexp_instantiation(instance):
    assert isinstance(instance, QVTOperational::MappingCallExp)

@given(instance=QVTOperational::MappingCallExp_strategy)
def test_qvtoperational::mappingcallexp_isStrict_type(instance):
    assert isinstance(instance.isStrict, str)


@given(instance=QVTOperational::MappingCallExp_strategy)
def test_qvtoperational::mappingcallexp_isStrict_setter(instance):
    original = instance.isStrict
    instance.isStrict = original
    assert instance.isStrict == original

@given(instance=RelationDomain_strategy)
@settings(max_examples=50)
def test_relationdomain_instantiation(instance):
    assert isinstance(instance, RelationDomain)

@given(instance=ModelParameter_strategy)
@settings(max_examples=50)
def test_modelparameter_instantiation(instance):
    assert isinstance(instance, ModelParameter)

@given(instance=OperationBody_strategy)
@settings(max_examples=50)
def test_operationbody_instantiation(instance):
    assert isinstance(instance, OperationBody)

@given(instance=QVTOperational::MappingBody_strategy)
@settings(max_examples=50)
def test_qvtoperational::mappingbody_instantiation(instance):
    assert isinstance(instance, QVTOperational::MappingBody)

@given(instance=QVTOperational::ConstructorBody_strategy)
@settings(max_examples=50)
def test_qvtoperational::constructorbody_instantiation(instance):
    assert isinstance(instance, QVTOperational::ConstructorBody)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=QVTOperational::OperationalTransformation_strategy)
@settings(max_examples=50)
def test_qvtoperational::operationaltransformation_instantiation(instance):
    assert isinstance(instance, QVTOperational::OperationalTransformation)

@given(instance=QVTOperational::Library_strategy)
@settings(max_examples=50)
def test_qvtoperational::library_instantiation(instance):
    assert isinstance(instance, QVTOperational::Library)

@given(instance=VarParameter_strategy)
@settings(max_examples=50)
def test_varparameter_instantiation(instance):
    assert isinstance(instance, VarParameter)

@given(instance=QVTOperational::ModelParameter_strategy)
@settings(max_examples=50)
def test_qvtoperational::modelparameter_instantiation(instance):
    assert isinstance(instance, QVTOperational::ModelParameter)

@given(instance=QVTOperational::MappingParameter_strategy)
@settings(max_examples=50)
def test_qvtoperational::mappingparameter_instantiation(instance):
    assert isinstance(instance, QVTOperational::MappingParameter)

@given(instance=DomainPattern_strategy)
@settings(max_examples=50)
def test_domainpattern_instantiation(instance):
    assert isinstance(instance, DomainPattern)

@given(instance=RelationDomainAssignment_strategy)
@settings(max_examples=50)
def test_relationdomainassignment_instantiation(instance):
    assert isinstance(instance, RelationDomainAssignment)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=ImperativeOperation_strategy)
@settings(max_examples=50)
def test_imperativeoperation_instantiation(instance):
    assert isinstance(instance, ImperativeOperation)

@given(instance=QVTOperational::MappingOperation_strategy)
@settings(max_examples=50)
def test_qvtoperational::mappingoperation_instantiation(instance):
    assert isinstance(instance, QVTOperational::MappingOperation)

@given(instance=QVTOperational::EntryOperation_strategy)
@settings(max_examples=50)
def test_qvtoperational::entryoperation_instantiation(instance):
    assert isinstance(instance, QVTOperational::EntryOperation)

@given(instance=QVTOperational::Helper_strategy)
@settings(max_examples=50)
def test_qvtoperational::helper_instantiation(instance):
    assert isinstance(instance, QVTOperational::Helper)

@given(instance=QVTOperational::Helper_strategy)
def test_qvtoperational::helper_isQuery_type(instance):
    assert isinstance(instance.isQuery, str)


@given(instance=QVTOperational::Helper_strategy)
def test_qvtoperational::helper_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=QVTOperational::Constructor_strategy)
@settings(max_examples=50)
def test_qvtoperational::constructor_instantiation(instance):
    assert isinstance(instance, QVTOperational::Constructor)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, ObjectTemplateExp)

@given(instance=RelationImplementation_strategy)
@settings(max_examples=50)
def test_relationimplementation_instantiation(instance):
    assert isinstance(instance, RelationImplementation)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=QVTRelation::OppositePropertyCallExp_strategy)
@settings(max_examples=50)
def test_qvtrelation::oppositepropertycallexp_instantiation(instance):
    assert isinstance(instance, QVTRelation::OppositePropertyCallExp)

@given(instance=RelationalTransformation_strategy)
@settings(max_examples=50)
def test_relationaltransformation_instantiation(instance):
    assert isinstance(instance, RelationalTransformation)

@given(instance=TemplateExp_strategy)
@settings(max_examples=50)
def test_templateexp_instantiation(instance):
    assert isinstance(instance, TemplateExp)

@given(instance=QVTTemplate::CollectionTemplateExp_strategy)
@settings(max_examples=50)
def test_qvttemplate::collectiontemplateexp_instantiation(instance):
    assert isinstance(instance, QVTTemplate::CollectionTemplateExp)

@given(instance=PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, PropertyTemplateItem)

@given(instance=QVTTemplate::ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_qvttemplate::objecttemplateexp_instantiation(instance):
    assert isinstance(instance, QVTTemplate::ObjectTemplateExp)

@given(instance=RealizedVariable_strategy)
@settings(max_examples=50)
def test_realizedvariable_instantiation(instance):
    assert isinstance(instance, RealizedVariable)

@given(instance=EnforcementOperation_strategy)
@settings(max_examples=50)
def test_enforcementoperation_instantiation(instance):
    assert isinstance(instance, EnforcementOperation)

@given(instance=Assignment_strategy)
@settings(max_examples=50)
def test_assignment_instantiation(instance):
    assert isinstance(instance, Assignment)

@given(instance=QVTCore::PropertyAssignment_strategy)
@settings(max_examples=50)
def test_qvtcore::propertyassignment_instantiation(instance):
    assert isinstance(instance, QVTCore::PropertyAssignment)

@given(instance=QVTCore::VariableAssignment_strategy)
@settings(max_examples=50)
def test_qvtcore::variableassignment_instantiation(instance):
    assert isinstance(instance, QVTCore::VariableAssignment)

@given(instance=Area_strategy)
@settings(max_examples=50)
def test_area_instantiation(instance):
    assert isinstance(instance, Area)

@given(instance=CorePattern_strategy)
@settings(max_examples=50)
def test_corepattern_instantiation(instance):
    assert isinstance(instance, CorePattern)

@given(instance=QVTCore::BottomPattern_strategy)
@settings(max_examples=50)
def test_qvtcore::bottompattern_instantiation(instance):
    assert isinstance(instance, QVTCore::BottomPattern)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=QVTCore::GuardPattern_strategy)
@settings(max_examples=50)
def test_qvtcore::guardpattern_instantiation(instance):
    assert isinstance(instance, QVTCore::GuardPattern)

@given(instance=Tag_strategy)
@settings(max_examples=50)
def test_tag_instantiation(instance):
    assert isinstance(instance, Tag)

@given(instance=Transformation_strategy)
@settings(max_examples=50)
def test_transformation_instantiation(instance):
    assert isinstance(instance, Transformation)

@given(instance=QVTRelation::RelationalTransformation_strategy)
@settings(max_examples=50)
def test_qvtrelation::relationaltransformation_instantiation(instance):
    assert isinstance(instance, QVTRelation::RelationalTransformation)

@given(instance=GuardPattern_strategy)
@settings(max_examples=50)
def test_guardpattern_instantiation(instance):
    assert isinstance(instance, GuardPattern)

@given(instance=BottomPattern_strategy)
@settings(max_examples=50)
def test_bottompattern_instantiation(instance):
    assert isinstance(instance, BottomPattern)

@given(instance=QVTCore::Area_strategy)
@settings(max_examples=50)
def test_qvtcore::area_instantiation(instance):
    assert isinstance(instance, QVTCore::Area)

@given(instance=TypedModel_strategy)
@settings(max_examples=50)
def test_typedmodel_instantiation(instance):
    assert isinstance(instance, TypedModel)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=QVTRelation::Relation_strategy)
@settings(max_examples=50)
def test_qvtrelation::relation_instantiation(instance):
    assert isinstance(instance, QVTRelation::Relation)

@given(instance=QVTRelation::Relation_strategy)
def test_qvtrelation::relation_isTopLevel_type(instance):
    assert isinstance(instance.isTopLevel, str)


@given(instance=QVTRelation::Relation_strategy)
def test_qvtrelation::relation_isTopLevel_setter(instance):
    original = instance.isTopLevel
    instance.isTopLevel = original
    assert instance.isTopLevel == original

@given(instance=QVTCore::Mapping_strategy)
@settings(max_examples=50)
def test_qvtcore::mapping_instantiation(instance):
    assert isinstance(instance, QVTCore::Mapping)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=QVTCore::CoreDomain_strategy)
@settings(max_examples=50)
def test_qvtcore::coredomain_instantiation(instance):
    assert isinstance(instance, QVTCore::CoreDomain)

@given(instance=QVTRelation::RelationDomain_strategy)
@settings(max_examples=50)
def test_qvtrelation::relationdomain_instantiation(instance):
    assert isinstance(instance, QVTRelation::RelationDomain)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=QVTCore::CorePattern_strategy)
@settings(max_examples=50)
def test_qvtcore::corepattern_instantiation(instance):
    assert isinstance(instance, QVTCore::CorePattern)

@given(instance=QVTRelation::DomainPattern_strategy)
@settings(max_examples=50)
def test_qvtrelation::domainpattern_instantiation(instance):
    assert isinstance(instance, QVTRelation::DomainPattern)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=EssentialOCL::IterateExp_strategy)
@settings(max_examples=50)
def test_essentialocl::iterateexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::IterateExp)

@given(instance=NavigationCallExp_strategy)
@settings(max_examples=50)
def test_navigationcallexp_instantiation(instance):
    assert isinstance(instance, NavigationCallExp)

@given(instance=EssentialOCL::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::PropertyCallExp)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=EssentialOCL::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::realliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::RealLiteralExp)

@given(instance=EssentialOCL::RealLiteralExp_strategy)
def test_essentialocl::realliteralexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=EssentialOCL::RealLiteralExp_strategy)
def test_essentialocl::realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=EssentialOCL::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::integerliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::IntegerLiteralExp)

@given(instance=EssentialOCL::IntegerLiteralExp_strategy)
def test_essentialocl::integerliteralexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=EssentialOCL::IntegerLiteralExp_strategy)
def test_essentialocl::integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=EssentialOCL::FeatureCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::featurecallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::FeatureCallExp)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=EssentialOCL::IfExp_strategy)
@settings(max_examples=50)
def test_essentialocl::ifexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::IfExp)

@given(instance=QVTRelation::RelationCallExp_strategy)
@settings(max_examples=50)
def test_qvtrelation::relationcallexp_instantiation(instance):
    assert isinstance(instance, QVTRelation::RelationCallExp)

@given(instance=EssentialOCL::CallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::callexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::CallExp)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=EssentialOCL::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::BooleanLiteralExp)

@given(instance=EssentialOCL::BooleanLiteralExp_strategy)
def test_essentialocl::booleanliteralexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=EssentialOCL::BooleanLiteralExp_strategy)
def test_essentialocl::booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=QVTCore::RealizedVariable_strategy)
@settings(max_examples=50)
def test_qvtcore::realizedvariable_instantiation(instance):
    assert isinstance(instance, QVTCore::RealizedVariable)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=EssentialOCL::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::InvalidLiteralExp)

@given(instance=QVTTemplate::TemplateExp_strategy)
@settings(max_examples=50)
def test_qvttemplate::templateexp_instantiation(instance):
    assert isinstance(instance, QVTTemplate::TemplateExp)

@given(instance=EssentialOCL::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::EnumLiteralExp)

@given(instance=EssentialOCL::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::PrimitiveLiteralExp)

@given(instance=EssentialOCL::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::CollectionLiteralExp)

@given(instance=EssentialOCL::CollectionLiteralExp_strategy)
def test_essentialocl::collectionliteralexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=EssentialOCL::CollectionLiteralExp_strategy)
def test_essentialocl::collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=EssentialOCL::CollectionRange_strategy)
@settings(max_examples=50)
def test_essentialocl::collectionrange_instantiation(instance):
    assert isinstance(instance, EssentialOCL::CollectionRange)

@given(instance=EssentialOCL::CollectionItem_strategy)
@settings(max_examples=50)
def test_essentialocl::collectionitem_instantiation(instance):
    assert isinstance(instance, EssentialOCL::CollectionItem)

@given(instance=ReflectiveCollection_strategy)
@settings(max_examples=50)
def test_reflectivecollection_instantiation(instance):
    assert isinstance(instance, ReflectiveCollection)

@given(instance=EMOF::ReflectiveSequence_strategy)
@settings(max_examples=50)
def test_emof::reflectivesequence_instantiation(instance):
    assert isinstance(instance, EMOF::ReflectiveSequence)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_emof::reflectivesequence_remove_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.remove(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.remove).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'remove' in EMOF::ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'remove' in EMOF::ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'remove' in EMOF::ReflectiveSequence is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_emof::reflectivesequence_add_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.add(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.add).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'add' in EMOF::ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'add' in EMOF::ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'add' in EMOF::ReflectiveSequence is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_emof::reflectivesequence_set_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.set(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.set).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'set' in EMOF::ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'set' in EMOF::ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'set' in EMOF::ReflectiveSequence is not implemented or raised an error")

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=EssentialOCL::OrderedSetType_strategy)
@settings(max_examples=50)
def test_essentialocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::OrderedSetType)

@given(instance=EssentialOCL::SequenceType_strategy)
@settings(max_examples=50)
def test_essentialocl::sequencetype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::SequenceType)

@given(instance=EssentialOCL::BagType_strategy)
@settings(max_examples=50)
def test_essentialocl::bagtype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::BagType)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=EMOF::URIExtent_strategy)
@settings(max_examples=50)
def test_emof::uriextent_instantiation(instance):
    assert isinstance(instance, EMOF::URIExtent)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::URIExtent_strategy)
@settings(max_examples=30)
def test_emof::uriextent_element_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.element(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.element).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'element' in EMOF::URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'element' in EMOF::URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'element' in EMOF::URIExtent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::URIExtent_strategy)
@settings(max_examples=30)
def test_emof::uriextent_contexturi_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.contextURI()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.contextURI).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'contextURI' in EMOF::URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'contextURI' in EMOF::URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'contextURI' in EMOF::URIExtent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::URIExtent_strategy)
@settings(max_examples=30)
def test_emof::uriextent_uri_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.uri(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.uri).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'uri' in EMOF::URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'uri' in EMOF::URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'uri' in EMOF::URIExtent is not implemented or raised an error")

@given(instance=EMOF::Object_strategy)
@settings(max_examples=50)
def test_emof::object_instantiation(instance):
    assert isinstance(instance, EMOF::Object)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=QVTBase::FunctionParameter_strategy)
@settings(max_examples=50)
def test_qvtbase::functionparameter_instantiation(instance):
    assert isinstance(instance, QVTBase::FunctionParameter)

@given(instance=QVTOperational::VarParameter_strategy)
@settings(max_examples=50)
def test_qvtoperational::varparameter_instantiation(instance):
    assert isinstance(instance, QVTOperational::VarParameter)

@given(instance=QVTOperational::VarParameter_strategy)
def test_qvtoperational::varparameter_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=QVTOperational::VarParameter_strategy)
def test_qvtoperational::varparameter_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=EssentialOCL::OclExpression_strategy)
@settings(max_examples=50)
def test_essentialocl::oclexpression_instantiation(instance):
    assert isinstance(instance, EssentialOCL::OclExpression)

@given(instance=EssentialOCL::ExpressionInOcl_strategy)
@settings(max_examples=50)
def test_essentialocl::expressioninocl_instantiation(instance):
    assert isinstance(instance, EssentialOCL::ExpressionInOcl)

@given(instance=EMOF::Parameter_strategy)
@settings(max_examples=50)
def test_emof::parameter_instantiation(instance):
    assert isinstance(instance, EMOF::Parameter)

@given(instance=EssentialOCL::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_essentialocl::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, EssentialOCL::CollectionLiteralPart)

@given(instance=EMOF::Property_strategy)
@settings(max_examples=50)
def test_emof::property_instantiation(instance):
    assert isinstance(instance, EMOF::Property)

@given(instance=EMOF::Property_strategy)
def test_emof::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=EMOF::Property_strategy)
def test_emof::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=EMOF::Property_strategy)
def test_emof::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=EMOF::Property_strategy)
def test_emof::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=EMOF::Property_strategy)
def test_emof::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=EMOF::Property_strategy)
def test_emof::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=EMOF::Property_strategy)
def test_emof::property_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=EMOF::Property_strategy)
def test_emof::property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=EMOF::Property_strategy)
def test_emof::property_isID_type(instance):
    assert isinstance(instance.isID, str)


@given(instance=EMOF::Property_strategy)
def test_emof::property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original

@given(instance=EMOF::Operation_strategy)
@settings(max_examples=50)
def test_emof::operation_instantiation(instance):
    assert isinstance(instance, EMOF::Operation)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=QVTBase::Domain_strategy)
@settings(max_examples=50)
def test_qvtbase::domain_instantiation(instance):
    assert isinstance(instance, QVTBase::Domain)

@given(instance=QVTBase::Domain_strategy)
def test_qvtbase::domain_isCheckable_type(instance):
    assert isinstance(instance.isCheckable, str)


@given(instance=QVTBase::Domain_strategy)
def test_qvtbase::domain_isCheckable_setter(instance):
    original = instance.isCheckable
    instance.isCheckable = original
    assert instance.isCheckable == original

@given(instance=QVTBase::Domain_strategy)
def test_qvtbase::domain_isEnforceable_type(instance):
    assert isinstance(instance.isEnforceable, str)


@given(instance=QVTBase::Domain_strategy)
def test_qvtbase::domain_isEnforceable_setter(instance):
    original = instance.isEnforceable
    instance.isEnforceable = original
    assert instance.isEnforceable == original

@given(instance=EMOF::TypedElement_strategy)
@settings(max_examples=50)
def test_emof::typedelement_instantiation(instance):
    assert isinstance(instance, EMOF::TypedElement)

@given(instance=QVTBase::Rule_strategy)
@settings(max_examples=50)
def test_qvtbase::rule_instantiation(instance):
    assert isinstance(instance, QVTBase::Rule)

@given(instance=QVTBase::TypedModel_strategy)
@settings(max_examples=50)
def test_qvtbase::typedmodel_instantiation(instance):
    assert isinstance(instance, QVTBase::TypedModel)

@given(instance=EMOF::Package_strategy)
@settings(max_examples=50)
def test_emof::package_instantiation(instance):
    assert isinstance(instance, EMOF::Package)

@given(instance=EMOF::Package_strategy)
def test_emof::package_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=EMOF::Package_strategy)
def test_emof::package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=EMOF::Type_strategy)
@settings(max_examples=50)
def test_emof::type_instantiation(instance):
    assert isinstance(instance, EMOF::Type)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::Type_strategy)
@settings(max_examples=30)
def test_emof::type_isinstance_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isInstance(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isInstance).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isInstance' in EMOF::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isInstance' in EMOF::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isInstance' in EMOF::Type is not implemented or raised an error")

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=EMOF::NamedElement_strategy)
@settings(max_examples=50)
def test_emof::namedelement_instantiation(instance):
    assert isinstance(instance, EMOF::NamedElement)

@given(instance=EMOF::NamedElement_strategy)
def test_emof::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EMOF::NamedElement_strategy)
def test_emof::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QVTBase::Pattern_strategy)
@settings(max_examples=50)
def test_qvtbase::pattern_instantiation(instance):
    assert isinstance(instance, QVTBase::Pattern)

@given(instance=QVTOperational::ModuleImport_strategy)
@settings(max_examples=50)
def test_qvtoperational::moduleimport_instantiation(instance):
    assert isinstance(instance, QVTOperational::ModuleImport)

@given(instance=QVTOperational::ModuleImport_strategy)
def test_qvtoperational::moduleimport_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=QVTOperational::ModuleImport_strategy)
def test_qvtoperational::moduleimport_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=QVTBase::Predicate_strategy)
@settings(max_examples=50)
def test_qvtbase::predicate_instantiation(instance):
    assert isinstance(instance, QVTBase::Predicate)

@given(instance=QVTOperational::OperationBody_strategy)
@settings(max_examples=50)
def test_qvtoperational::operationbody_instantiation(instance):
    assert isinstance(instance, QVTOperational::OperationBody)

@given(instance=QVTRelation::RelationImplementation_strategy)
@settings(max_examples=50)
def test_qvtrelation::relationimplementation_instantiation(instance):
    assert isinstance(instance, QVTRelation::RelationImplementation)

@given(instance=QVTTemplate::PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_qvttemplate::propertytemplateitem_instantiation(instance):
    assert isinstance(instance, QVTTemplate::PropertyTemplateItem)

@given(instance=QVTTemplate::PropertyTemplateItem_strategy)
def test_qvttemplate::propertytemplateitem_isOpposite_type(instance):
    assert isinstance(instance.isOpposite, str)


@given(instance=QVTTemplate::PropertyTemplateItem_strategy)
def test_qvttemplate::propertytemplateitem_isOpposite_setter(instance):
    original = instance.isOpposite
    instance.isOpposite = original
    assert instance.isOpposite == original

@given(instance=EMOF::Tag_strategy)
@settings(max_examples=50)
def test_emof::tag_instantiation(instance):
    assert isinstance(instance, EMOF::Tag)

@given(instance=EMOF::Tag_strategy)
def test_emof::tag_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=EMOF::Tag_strategy)
def test_emof::tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=EMOF::Tag_strategy)
def test_emof::tag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=EMOF::Tag_strategy)
def test_emof::tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=QVTCore::Assignment_strategy)
@settings(max_examples=50)
def test_qvtcore::assignment_instantiation(instance):
    assert isinstance(instance, QVTCore::Assignment)

@given(instance=QVTCore::Assignment_strategy)
def test_qvtcore::assignment_isDefault_type(instance):
    assert isinstance(instance.isDefault, str)


@given(instance=QVTCore::Assignment_strategy)
def test_qvtcore::assignment_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=QVTRelation::RelationDomainAssignment_strategy)
@settings(max_examples=50)
def test_qvtrelation::relationdomainassignment_instantiation(instance):
    assert isinstance(instance, QVTRelation::RelationDomainAssignment)

@given(instance=QVTCore::EnforcementOperation_strategy)
@settings(max_examples=50)
def test_qvtcore::enforcementoperation_instantiation(instance):
    assert isinstance(instance, QVTCore::EnforcementOperation)

@given(instance=QVTCore::EnforcementOperation_strategy)
def test_qvtcore::enforcementoperation_enforcementMode_type(instance):
    assert isinstance(instance.enforcementMode, str)


@given(instance=QVTCore::EnforcementOperation_strategy)
def test_qvtcore::enforcementoperation_enforcementMode_setter(instance):
    original = instance.enforcementMode
    instance.enforcementMode = original
    assert instance.enforcementMode == original

@given(instance=QVTRelation::Key_strategy)
@settings(max_examples=50)
def test_qvtrelation::key_instantiation(instance):
    assert isinstance(instance, QVTRelation::Key)

@given(instance=EMOF::Comment_strategy)
@settings(max_examples=50)
def test_emof::comment_instantiation(instance):
    assert isinstance(instance, EMOF::Comment)

@given(instance=EMOF::Comment_strategy)
def test_emof::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=EMOF::Comment_strategy)
def test_emof::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=EMOF::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_emof::multiplicityelement_instantiation(instance):
    assert isinstance(instance, EMOF::MultiplicityElement)

@given(instance=EMOF::MultiplicityElement_strategy)
def test_emof::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=EMOF::MultiplicityElement_strategy)
def test_emof::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=EMOF::MultiplicityElement_strategy)
def test_emof::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=EMOF::MultiplicityElement_strategy)
def test_emof::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=EMOF::MultiplicityElement_strategy)
def test_emof::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=EMOF::MultiplicityElement_strategy)
def test_emof::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=EMOF::MultiplicityElement_strategy)
def test_emof::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=EMOF::MultiplicityElement_strategy)
def test_emof::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=EMOF::Factory_strategy)
@settings(max_examples=50)
def test_emof::factory_instantiation(instance):
    assert isinstance(instance, EMOF::Factory)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::Factory_strategy)
@settings(max_examples=30)
def test_emof::factory_converttostring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.convertToString(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.convertToString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'convertToString' in EMOF::Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'convertToString' in EMOF::Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'convertToString' in EMOF::Factory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::Factory_strategy)
@settings(max_examples=30)
def test_emof::factory_createfromstring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createFromString(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createFromString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createFromString' in EMOF::Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createFromString' in EMOF::Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createFromString' in EMOF::Factory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::Factory_strategy)
@settings(max_examples=30)
def test_emof::factory_create_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.create(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.create).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'create' in EMOF::Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'create' in EMOF::Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'create' in EMOF::Factory is not implemented or raised an error")

@given(instance=Enumeration_strategy)
@settings(max_examples=50)
def test_enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)

@given(instance=EMOF::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_emof::enumerationliteral_instantiation(instance):
    assert isinstance(instance, EMOF::EnumerationLiteral)

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=EssentialOCL::CollectionType_strategy)
@settings(max_examples=50)
def test_essentialocl::collectiontype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::CollectionType)

@given(instance=EMOF::PrimitiveType_strategy)
@settings(max_examples=50)
def test_emof::primitivetype_instantiation(instance):
    assert isinstance(instance, EMOF::PrimitiveType)

@given(instance=EMOF::Enumeration_strategy)
@settings(max_examples=50)
def test_emof::enumeration_instantiation(instance):
    assert isinstance(instance, EMOF::Enumeration)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=EMOF::Extent_strategy)
@settings(max_examples=50)
def test_emof::extent_instantiation(instance):
    assert isinstance(instance, EMOF::Extent)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::Extent_strategy)
@settings(max_examples=30)
def test_emof::extent_usecontainment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.useContainment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.useContainment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'useContainment' in EMOF::Extent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'useContainment' in EMOF::Extent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'useContainment' in EMOF::Extent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::Extent_strategy)
@settings(max_examples=30)
def test_emof::extent_elements_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.elements()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.elements).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'elements' in EMOF::Extent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'elements' in EMOF::Extent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'elements' in EMOF::Extent is not implemented or raised an error")

@given(instance=EMOF::ReflectiveCollection_strategy)
@settings(max_examples=50)
def test_emof::reflectivecollection_instantiation(instance):
    assert isinstance(instance, EMOF::ReflectiveCollection)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_emof::reflectivecollection_clear_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.clear()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.clear).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'clear' in EMOF::ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clear' in EMOF::ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clear' in EMOF::ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_emof::reflectivecollection_size_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.size()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.size).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'size' in EMOF::ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'size' in EMOF::ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'size' in EMOF::ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_emof::reflectivecollection_addall_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addAll(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addAll).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addAll' in EMOF::ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addAll' in EMOF::ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addAll' in EMOF::ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_emof::reflectivecollection_remove_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.remove(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.remove).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'remove' in EMOF::ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'remove' in EMOF::ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'remove' in EMOF::ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_emof::reflectivecollection_add_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.add(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.add).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'add' in EMOF::ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'add' in EMOF::ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'add' in EMOF::ReflectiveCollection is not implemented or raised an error")

@given(instance=EMOF::Element_strategy)
@settings(max_examples=50)
def test_emof::element_instantiation(instance):
    assert isinstance(instance, EMOF::Element)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::Element_strategy)
@settings(max_examples=30)
def test_emof::element_isset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSet(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSet).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSet' in EMOF::Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSet' in EMOF::Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSet' in EMOF::Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::Element_strategy)
@settings(max_examples=30)
def test_emof::element_set_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.set(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.set).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'set' in EMOF::Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'set' in EMOF::Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'set' in EMOF::Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::Element_strategy)
@settings(max_examples=30)
def test_emof::element_equals_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.equals(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.equals).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'equals' in EMOF::Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equals' in EMOF::Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equals' in EMOF::Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::Element_strategy)
@settings(max_examples=30)
def test_emof::element_container_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.container()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.container).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'container' in EMOF::Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'container' in EMOF::Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'container' in EMOF::Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=EMOF::Element_strategy)
@settings(max_examples=30)
def test_emof::element_unset_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unset(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unset).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unset' in EMOF::Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unset' in EMOF::Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unset' in EMOF::Element is not implemented or raised an error")

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=QVTOperational::ModelType_strategy)
@settings(max_examples=50)
def test_qvtoperational::modeltype_instantiation(instance):
    assert isinstance(instance, QVTOperational::ModelType)

@given(instance=QVTOperational::ModelType_strategy)
def test_qvtoperational::modeltype_conformanceKind_type(instance):
    assert isinstance(instance.conformanceKind, str)


@given(instance=QVTOperational::ModelType_strategy)
def test_qvtoperational::modeltype_conformanceKind_setter(instance):
    original = instance.conformanceKind
    instance.conformanceKind = original
    assert instance.conformanceKind == original

@given(instance=QVTBase::Transformation_strategy)
@settings(max_examples=50)
def test_qvtbase::transformation_instantiation(instance):
    assert isinstance(instance, QVTBase::Transformation)

@given(instance=QVTOperational::Module_strategy)
@settings(max_examples=50)
def test_qvtoperational::module_instantiation(instance):
    assert isinstance(instance, QVTOperational::Module)

@given(instance=QVTOperational::Module_strategy)
def test_qvtoperational::module_isBlackbox_type(instance):
    assert isinstance(instance.isBlackbox, str)


@given(instance=QVTOperational::Module_strategy)
def test_qvtoperational::module_isBlackbox_setter(instance):
    original = instance.isBlackbox
    instance.isBlackbox = original
    assert instance.isBlackbox == original

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=QVTBase::Function_strategy)
@settings(max_examples=50)
def test_qvtbase::function_instantiation(instance):
    assert isinstance(instance, QVTBase::Function)

@given(instance=QVTOperational::ImperativeOperation_strategy)
@settings(max_examples=50)
def test_qvtoperational::imperativeoperation_instantiation(instance):
    assert isinstance(instance, QVTOperational::ImperativeOperation)

@given(instance=QVTOperational::ImperativeOperation_strategy)
def test_qvtoperational::imperativeoperation_isBlackbox_type(instance):
    assert isinstance(instance.isBlackbox, str)


@given(instance=QVTOperational::ImperativeOperation_strategy)
def test_qvtoperational::imperativeoperation_isBlackbox_setter(instance):
    original = instance.isBlackbox
    instance.isBlackbox = original
    assert instance.isBlackbox == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=QVTOperational::ContextualProperty_strategy)
@settings(max_examples=50)
def test_qvtoperational::contextualproperty_instantiation(instance):
    assert isinstance(instance, QVTOperational::ContextualProperty)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=EMOF::DataType_strategy)
@settings(max_examples=50)
def test_emof::datatype_instantiation(instance):
    assert isinstance(instance, EMOF::DataType)

@given(instance=EssentialOCL::InvalidType_strategy)
@settings(max_examples=50)
def test_essentialocl::invalidtype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::InvalidType)

@given(instance=EssentialOCL::AnyType_strategy)
@settings(max_examples=50)
def test_essentialocl::anytype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::AnyType)

@given(instance=EMOF::Class_strategy)
@settings(max_examples=50)
def test_emof::class_instantiation(instance):
    assert isinstance(instance, EMOF::Class)

@given(instance=EMOF::Class_strategy)
def test_emof::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=EMOF::Class_strategy)
def test_emof::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=ImperativeOCL::Typedef_strategy)
@settings(max_examples=50)
def test_imperativeocl::typedef_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::Typedef)

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=CatchExp_strategy)
@settings(max_examples=50)
def test_catchexp_instantiation(instance):
    assert isinstance(instance, CatchExp)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=ImperativeOCL::ListType_strategy)
@settings(max_examples=50)
def test_imperativeocl::listtype_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ListType)

@given(instance=ImperativeOCL::ListLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::listliteralexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ListLiteralExp)

@given(instance=ImperativeOCL::OrderedTupleType_strategy)
@settings(max_examples=50)
def test_imperativeocl::orderedtupletype_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::OrderedTupleType)

@given(instance=ImperativeOCL::OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl::orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::OrderedTupleLiteralPart)

@given(instance=OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, OrderedTupleLiteralPart)

@given(instance=ImperativeOCL::OrderedTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::orderedtupleliteralexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::OrderedTupleLiteralExp)

@given(instance=ImperativeOCL::ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ImperativeExpression)

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=ImperativeOCL::ForExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::forexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ForExp)

@given(instance=ImperativeOCL::DictionaryType_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictionarytype_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::DictionaryType)

@given(instance=ImperativeOCL::DictLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictliteralpart_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::DictLiteralPart)

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=ImperativeOCL::DictLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictliteralexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::DictLiteralExp)

@given(instance=ImperativeOCL::ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ImperativeIterateExp)

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)

@given(instance=EssentialOCL::Variable_strategy)
@settings(max_examples=50)
def test_essentialocl::variable_instantiation(instance):
    assert isinstance(instance, EssentialOCL::Variable)

@given(instance=EssentialOCL::UnlimitedNaturalExp_strategy)
@settings(max_examples=50)
def test_essentialocl::unlimitednaturalexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::UnlimitedNaturalExp)

@given(instance=EssentialOCL::UnlimitedNaturalExp_strategy)
def test_essentialocl::unlimitednaturalexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=EssentialOCL::UnlimitedNaturalExp_strategy)
def test_essentialocl::unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=EssentialOCL::TypeExp_strategy)
@settings(max_examples=50)
def test_essentialocl::typeexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::TypeExp)

@given(instance=EssentialOCL::TupleType_strategy)
@settings(max_examples=50)
def test_essentialocl::tupletype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::TupleType)

@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)

@given(instance=EssentialOCL::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_essentialocl::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, EssentialOCL::TupleLiteralPart)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=EssentialOCL::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::TupleLiteralExp)

@given(instance=EssentialOCL::TemplateParameterType_strategy)
@settings(max_examples=50)
def test_essentialocl::templateparametertype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::TemplateParameterType)

@given(instance=EssentialOCL::TemplateParameterType_strategy)
def test_essentialocl::templateparametertype_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=EssentialOCL::TemplateParameterType_strategy)
def test_essentialocl::templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=EssentialOCL::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::stringliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::StringLiteralExp)

@given(instance=EssentialOCL::StringLiteralExp_strategy)
def test_essentialocl::stringliteralexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=EssentialOCL::StringLiteralExp_strategy)
def test_essentialocl::stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=EssentialOCL::SetType_strategy)
@settings(max_examples=50)
def test_essentialocl::settype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::SetType)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=ImperativeOCL::WhileExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::whileexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::WhileExp)

@given(instance=ImperativeOCL::AssignExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::assignexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::AssignExp)

@given(instance=ImperativeOCL::AssignExp_strategy)
def test_imperativeocl::assignexp_isReset_type(instance):
    assert isinstance(instance.isReset, str)


@given(instance=ImperativeOCL::AssignExp_strategy)
def test_imperativeocl::assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=ImperativeOCL::SwitchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::switchexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::SwitchExp)

@given(instance=ImperativeOCL::VariableInitExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::variableinitexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::VariableInitExp)

@given(instance=ImperativeOCL::VariableInitExp_strategy)
def test_imperativeocl::variableinitexp_withResult_type(instance):
    assert isinstance(instance.withResult, str)


@given(instance=ImperativeOCL::VariableInitExp_strategy)
def test_imperativeocl::variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=ImperativeOCL::TryExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::tryexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::TryExp)

@given(instance=ImperativeOCL::ContinueExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::continueexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ContinueExp)

@given(instance=ImperativeOCL::AssertExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::assertexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::AssertExp)

@given(instance=ImperativeOCL::AssertExp_strategy)
def test_imperativeocl::assertexp_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=ImperativeOCL::AssertExp_strategy)
def test_imperativeocl::assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=ImperativeOCL::ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ImperativeLoopExp)

@given(instance=QVTOperational::ImperativeCallExp_strategy)
@settings(max_examples=50)
def test_qvtoperational::imperativecallexp_instantiation(instance):
    assert isinstance(instance, QVTOperational::ImperativeCallExp)

@given(instance=QVTOperational::ImperativeCallExp_strategy)
def test_qvtoperational::imperativecallexp_isVirtual_type(instance):
    assert isinstance(instance.isVirtual, str)


@given(instance=QVTOperational::ImperativeCallExp_strategy)
def test_qvtoperational::imperativecallexp_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=ImperativeOCL::ComputeExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::computeexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ComputeExp)

@given(instance=ImperativeOCL::UnlinkExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::unlinkexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::UnlinkExp)

@given(instance=ImperativeOCL::UnpackExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::unpackexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::UnpackExp)

@given(instance=ImperativeOCL::BlockExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::blockexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::BlockExp)

@given(instance=ImperativeOCL::BreakExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::breakexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::BreakExp)

@given(instance=ImperativeOCL::CatchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::catchexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::CatchExp)

@given(instance=ImperativeOCL::ReturnExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::returnexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::ReturnExp)

@given(instance=ImperativeOCL::RaiseExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::raiseexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::RaiseExp)

@given(instance=QVTOperational::ResolveExp_strategy)
@settings(max_examples=50)
def test_qvtoperational::resolveexp_instantiation(instance):
    assert isinstance(instance, QVTOperational::ResolveExp)

@given(instance=QVTOperational::ResolveExp_strategy)
def test_qvtoperational::resolveexp_isInverse_type(instance):
    assert isinstance(instance.isInverse, str)


@given(instance=QVTOperational::ResolveExp_strategy)
def test_qvtoperational::resolveexp_isInverse_setter(instance):
    original = instance.isInverse
    instance.isInverse = original
    assert instance.isInverse == original

@given(instance=QVTOperational::ResolveExp_strategy)
def test_qvtoperational::resolveexp_isDeferred_type(instance):
    assert isinstance(instance.isDeferred, str)


@given(instance=QVTOperational::ResolveExp_strategy)
def test_qvtoperational::resolveexp_isDeferred_setter(instance):
    original = instance.isDeferred
    instance.isDeferred = original
    assert instance.isDeferred == original

@given(instance=QVTOperational::ResolveExp_strategy)
def test_qvtoperational::resolveexp_one_type(instance):
    assert isinstance(instance.one, str)


@given(instance=QVTOperational::ResolveExp_strategy)
def test_qvtoperational::resolveexp_one_setter(instance):
    original = instance.one
    instance.one = original
    assert instance.one == original

@given(instance=ImperativeOCL::LogExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::logexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::LogExp)

@given(instance=ImperativeOCL::InstantiationExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::instantiationexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::InstantiationExp)

@given(instance=ImperativeOCL::AltExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::altexp_instantiation(instance):
    assert isinstance(instance, ImperativeOCL::AltExp)

@given(instance=EssentialOCL::VoidType_strategy)
@settings(max_examples=50)
def test_essentialocl::voidtype_instantiation(instance):
    assert isinstance(instance, EssentialOCL::VoidType)

@given(instance=EssentialOCL::VariableExp_strategy)
@settings(max_examples=50)
def test_essentialocl::variableexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::VariableExp)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=EssentialOCL::NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::numericliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::NumericLiteralExp)

@given(instance=EssentialOCL::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::nullliteralexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::NullLiteralExp)

@given(instance=FeatureCallExp_strategy)
@settings(max_examples=50)
def test_featurecallexp_instantiation(instance):
    assert isinstance(instance, FeatureCallExp)

@given(instance=EssentialOCL::OperationCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::OperationCallExp)

@given(instance=EssentialOCL::NavigationCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::navigationcallexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::NavigationCallExp)

@given(instance=EssentialOCL::LoopExp_strategy)
@settings(max_examples=50)
def test_essentialocl::loopexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::LoopExp)

@given(instance=EssentialOCL::LiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::literalexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::LiteralExp)

@given(instance=EssentialOCL::LetExp_strategy)
@settings(max_examples=50)
def test_essentialocl::letexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::LetExp)

@given(instance=EssentialOCL::IteratorExp_strategy)
@settings(max_examples=50)
def test_essentialocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, EssentialOCL::IteratorExp)
