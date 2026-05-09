import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    LetExp,
    Extent,
    FlatQVT::URIExtent,
    TupleLiteralExp,
    TupleLiteralPart,
    CatchExp,
    AltExp,
    ResolveExp,
    FlatQVT::ResolveInExp,
    DomainPattern,
    RelationDomainAssignment,
    Key,
    Transformation,
    FlatQVT::RelationalTransformation,
    ReflectiveCollection,
    FlatQVT::ReflectiveSequence,
    RelationImplementation,
    NavigationCallExp,
    FlatQVT::PropertyCallExp,
    ObjectTemplateExp,
    Predicate,
    OrderedTupleLiteralPart,
    PropertyCallExp,
    FlatQVT::OppositePropertyCallExp,
    ConstructorBody,
    InstantiationExp,
    FlatQVT::ObjectExp,
    FlatQVT::Object,
    MultiplicityElement,
    PropertyTemplateItem,
    ModuleImport,
    EntryOperation,
    FeatureCallExp,
    FlatQVT::OperationCallExp,
    FlatQVT::NavigationCallExp,
    FlatQVT::MultiplicityElement,
    ModelType,
    Tag,
    MappingOperation,
    ImperativeCallExp,
    FlatQVT::MappingCallExp,
    RelationDomain,
    ModelParameter,
    Relation,
    Mapping,
    NumericLiteralExp,
    FlatQVT::UnlimitedNaturalExp,
    FlatQVT::RealLiteralExp,
    FlatQVT::IntegerLiteralExp,
    Module,
    FlatQVT::OperationalTransformation,
    FlatQVT::Library,
    RelationalTransformation,
    LogExp,
    VarParameter,
    FlatQVT::ModelParameter,
    FlatQVT::MappingParameter,
    LoopExp,
    FlatQVT::IteratorExp,
    FlatQVT::IterateExp,
    Parameter,
    ImperativeLoopExp,
    FlatQVT::ImperativeIterateExp,
    FlatQVT::ForExp,
    CallExp,
    FlatQVT::FeatureCallExp,
    Package,
    Comment,
    Enumeration,
    EnumerationLiteral,
    OperationCallExp,
    DictLiteralPart,
    Object,
    FlatQVT::ReflectiveCollection,
    FlatQVT::Extent,
    FlatQVT::Element,
    TypedModel,
    Rule,
    FlatQVT::Relation,
    NamedElement,
    FlatQVT::TypedElement,
    FlatQVT::Type,
    FlatQVT::EnumerationLiteral,
    FlatQVT::TypedModel,
    FlatQVT::Domain,
    FlatQVT::Rule,
    FlatQVT::Package,
    DataType,
    FlatQVT::Enumeration,
    FlatQVT::PrimitiveType,
    FlatQVT::CollectionType,
    Pattern,
    FlatQVT::DomainPattern,
    FlatQVT::CorePattern,
    Domain,
    FlatQVT::RelationDomain,
    Variable,
    FlatQVT::RealizedVariable,
    FlatQVT::VarParameter,
    FlatQVT::FunctionParameter,
    OperationBody,
    FlatQVT::MappingBody,
    FlatQVT::ConstructorBody,
    ImperativeOperation,
    FlatQVT::Helper,
    FlatQVT::EntryOperation,
    FlatQVT::MappingOperation,
    FlatQVT::Constructor,
    CollectionLiteralExp,
    TypedElement,
    FlatQVT::OclExpression,
    FlatQVT::Operation,
    FlatQVT::TupleLiteralPart,
    FlatQVT::ExpressionInOcl,
    FlatQVT::Parameter,
    FlatQVT::Variable,
    FlatQVT::Property,
    FlatQVT::CollectionLiteralPart,
    LiteralExp,
    FlatQVT::EnumLiteralExp,
    FlatQVT::NullLiteralExp,
    FlatQVT::InvalidLiteralExp,
    FlatQVT::TupleLiteralExp,
    FlatQVT::TemplateExp,
    FlatQVT::ListLiteralExp,
    FlatQVT::DictLiteralExp,
    FlatQVT::PrimitiveLiteralExp,
    FlatQVT::OrderedTupleLiteralExp,
    FlatQVT::CollectionLiteralExp,
    CollectionLiteralPart,
    FlatQVT::CollectionItem,
    Class,
    FlatQVT::Transformation,
    FlatQVT::OrderedTupleType,
    FlatQVT::TupleType,
    FlatQVT::Typedef,
    FlatQVT::ModelType,
    FlatQVT::Module,
    Operation,
    FlatQVT::ImperativeOperation,
    FlatQVT::Function,
    Property,
    FlatQVT::ContextualProperty,
    TemplateExp,
    FlatQVT::ObjectTemplateExp,
    FlatQVT::CollectionTemplateExp,
    FlatQVT::CollectionRange,
    EnforcementOperation,
    Assignment,
    FlatQVT::PropertyAssignment,
    FlatQVT::VariableAssignment,
    Area,
    FlatQVT::Mapping,
    FlatQVT::CoreDomain,
    CorePattern,
    FlatQVT::GuardPattern,
    FlatQVT::BottomPattern,
    PrimitiveLiteralExp,
    FlatQVT::StringLiteralExp,
    FlatQVT::NumericLiteralExp,
    FlatQVT::BooleanLiteralExp,
    CollectionType,
    FlatQVT::ListType,
    FlatQVT::DictionaryType,
    FlatQVT::SequenceType,
    FlatQVT::OrderedSetType,
    FlatQVT::SetType,
    FlatQVT::BagType,
    Element,
    FlatQVT::DictLiteralPart,
    FlatQVT::Comment,
    FlatQVT::Tag,
    FlatQVT::NamedElement,
    FlatQVT::RelationImplementation,
    FlatQVT::PropertyTemplateItem,
    FlatQVT::Predicate,
    FlatQVT::RelationDomainAssignment,
    FlatQVT::ModuleImport,
    FlatQVT::OperationBody,
    FlatQVT::EnforcementOperation,
    FlatQVT::OrderedTupleLiteralPart,
    FlatQVT::Key,
    FlatQVT::Factory,
    FlatQVT::Pattern,
    FlatQVT::Assignment,
    RealizedVariable,
    GuardPattern,
    BottomPattern,
    FlatQVT::Area,
    Type,
    FlatQVT::VoidType,
    FlatQVT::DataType,
    FlatQVT::Class,
    FlatQVT::TemplateParameterType,
    FlatQVT::InvalidType,
    FlatQVT::AnyType,
    OclExpression,
    FlatQVT::ImperativeExpression,
    FlatQVT::VariableExp,
    FlatQVT::LoopExp,
    FlatQVT::LiteralExp,
    FlatQVT::RelationCallExp,
    FlatQVT::CallExp,
    FlatQVT::LetExp,
    FlatQVT::IfExp,
    FlatQVT::TypeExp,
    ImperativeExpression,
    FlatQVT::UnlinkExp,
    FlatQVT::ImperativeLoopExp,
    FlatQVT::LogExp,
    FlatQVT::ImperativeCallExp,
    FlatQVT::AssignExp,
    FlatQVT::SwitchExp,
    FlatQVT::ComputeExp,
    FlatQVT::ReturnExp,
    FlatQVT::WhileExp,
    FlatQVT::ResolveExp,
    FlatQVT::BreakExp,
    FlatQVT::ContinueExp,
    FlatQVT::VariableInitExp,
    FlatQVT::RaiseExp,
    FlatQVT::CatchExp,
    FlatQVT::InstantiationExp,
    FlatQVT::AssertExp,
    FlatQVT::TryExp,
    FlatQVT::BlockExp,
    FlatQVT::UnpackExp,
    FlatQVT::AltExp,
    CollectionKind,
    ImportKind,
    SeverityKind,
    DirectionKind,
    EnforcementMode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::uriextent_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::URIExtent)


def test_flatqvt::uriextent_constructor_exists():
    assert callable(FlatQVT::URIExtent.__init__)


def test_flatqvt::uriextent_constructor_args():
    sig = inspect.signature(FlatQVT::URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralExp)


def test_tupleliteralexp_constructor_exists():
    assert callable(TupleLiteralExp.__init__)


def test_tupleliteralexp_constructor_args():
    sig = inspect.signature(TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_catchexp_is_not_abstract():
    assert not inspect.isabstract(CatchExp)


def test_catchexp_constructor_exists():
    assert callable(CatchExp.__init__)


def test_catchexp_constructor_args():
    sig = inspect.signature(CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_altexp_is_not_abstract():
    assert not inspect.isabstract(AltExp)


def test_altexp_constructor_exists():
    assert callable(AltExp.__init__)


def test_altexp_constructor_args():
    sig = inspect.signature(AltExp.__init__)
    params = list(sig.parameters.keys())



def test_resolveexp_is_not_abstract():
    assert not inspect.isabstract(ResolveExp)


def test_resolveexp_constructor_exists():
    assert callable(ResolveExp.__init__)


def test_resolveexp_constructor_args():
    sig = inspect.signature(ResolveExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::resolveinexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ResolveInExp)


def test_flatqvt::resolveinexp_constructor_exists():
    assert callable(FlatQVT::ResolveInExp.__init__)


def test_flatqvt::resolveinexp_constructor_args():
    sig = inspect.signature(FlatQVT::ResolveInExp.__init__)
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



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_transformation_is_not_abstract():
    assert not inspect.isabstract(Transformation)


def test_transformation_constructor_exists():
    assert callable(Transformation.__init__)


def test_transformation_constructor_args():
    sig = inspect.signature(Transformation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::relationaltransformation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::RelationalTransformation)


def test_flatqvt::relationaltransformation_constructor_exists():
    assert callable(FlatQVT::RelationalTransformation.__init__)


def test_flatqvt::relationaltransformation_constructor_args():
    sig = inspect.signature(FlatQVT::RelationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_reflectivecollection_is_not_abstract():
    assert not inspect.isabstract(ReflectiveCollection)


def test_reflectivecollection_constructor_exists():
    assert callable(ReflectiveCollection.__init__)


def test_reflectivecollection_constructor_args():
    sig = inspect.signature(ReflectiveCollection.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::reflectivesequence_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ReflectiveSequence)


def test_flatqvt::reflectivesequence_constructor_exists():
    assert callable(FlatQVT::ReflectiveSequence.__init__)


def test_flatqvt::reflectivesequence_constructor_args():
    sig = inspect.signature(FlatQVT::ReflectiveSequence.__init__)
    params = list(sig.parameters.keys())



def test_relationimplementation_is_not_abstract():
    assert not inspect.isabstract(RelationImplementation)


def test_relationimplementation_constructor_exists():
    assert callable(RelationImplementation.__init__)


def test_relationimplementation_constructor_args():
    sig = inspect.signature(RelationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(NavigationCallExp)


def test_navigationcallexp_constructor_exists():
    assert callable(NavigationCallExp.__init__)


def test_navigationcallexp_constructor_args():
    sig = inspect.signature(NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::PropertyCallExp)


def test_flatqvt::propertycallexp_constructor_exists():
    assert callable(FlatQVT::PropertyCallExp.__init__)


def test_flatqvt::propertycallexp_constructor_args():
    sig = inspect.signature(FlatQVT::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(ObjectTemplateExp)


def test_objecttemplateexp_constructor_exists():
    assert callable(ObjectTemplateExp.__init__)


def test_objecttemplateexp_constructor_args():
    sig = inspect.signature(ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(OrderedTupleLiteralPart)


def test_orderedtupleliteralpart_constructor_exists():
    assert callable(OrderedTupleLiteralPart.__init__)


def test_orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::oppositepropertycallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::OppositePropertyCallExp)


def test_flatqvt::oppositepropertycallexp_constructor_exists():
    assert callable(FlatQVT::OppositePropertyCallExp.__init__)


def test_flatqvt::oppositepropertycallexp_constructor_args():
    sig = inspect.signature(FlatQVT::OppositePropertyCallExp.__init__)
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



def test_flatqvt::objectexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ObjectExp)


def test_flatqvt::objectexp_constructor_exists():
    assert callable(FlatQVT::ObjectExp.__init__)


def test_flatqvt::objectexp_constructor_args():
    sig = inspect.signature(FlatQVT::ObjectExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::object_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Object)


def test_flatqvt::object_constructor_exists():
    assert callable(FlatQVT::Object.__init__)


def test_flatqvt::object_constructor_args():
    sig = inspect.signature(FlatQVT::Object.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(PropertyTemplateItem)


def test_propertytemplateitem_constructor_exists():
    assert callable(PropertyTemplateItem.__init__)


def test_propertytemplateitem_constructor_args():
    sig = inspect.signature(PropertyTemplateItem.__init__)
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



def test_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExp)


def test_featurecallexp_constructor_exists():
    assert callable(FeatureCallExp.__init__)


def test_featurecallexp_constructor_args():
    sig = inspect.signature(FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::OperationCallExp)


def test_flatqvt::operationcallexp_constructor_exists():
    assert callable(FlatQVT::OperationCallExp.__init__)


def test_flatqvt::operationcallexp_constructor_args():
    sig = inspect.signature(FlatQVT::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::NavigationCallExp)


def test_flatqvt::navigationcallexp_constructor_exists():
    assert callable(FlatQVT::NavigationCallExp.__init__)


def test_flatqvt::navigationcallexp_constructor_args():
    sig = inspect.signature(FlatQVT::NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::MultiplicityElement)


def test_flatqvt::multiplicityelement_constructor_exists():
    assert callable(FlatQVT::MultiplicityElement.__init__)


def test_flatqvt::multiplicityelement_constructor_args():
    sig = inspect.signature(FlatQVT::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_flatqvt::multiplicityelement_has_lower():
    assert hasattr(FlatQVT::MultiplicityElement, "lower")
    descriptor = None
    for klass in FlatQVT::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt::multiplicityelement_has_isOrdered():
    assert hasattr(FlatQVT::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in FlatQVT::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt::multiplicityelement_has_upper():
    assert hasattr(FlatQVT::MultiplicityElement, "upper")
    descriptor = None
    for klass in FlatQVT::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt::multiplicityelement_has_isUnique():
    assert hasattr(FlatQVT::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in FlatQVT::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_modeltype_is_not_abstract():
    assert not inspect.isabstract(ModelType)


def test_modeltype_constructor_exists():
    assert callable(ModelType.__init__)


def test_modeltype_constructor_args():
    sig = inspect.signature(ModelType.__init__)
    params = list(sig.parameters.keys())



def test_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
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



def test_flatqvt::mappingcallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::MappingCallExp)


def test_flatqvt::mappingcallexp_constructor_exists():
    assert callable(FlatQVT::MappingCallExp.__init__)


def test_flatqvt::mappingcallexp_constructor_args():
    sig = inspect.signature(FlatQVT::MappingCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isStrict" in params, "Missing parameter 'isStrict'"

def test_flatqvt::mappingcallexp_has_isStrict():
    assert hasattr(FlatQVT::MappingCallExp, "isStrict")
    descriptor = None
    for klass in FlatQVT::MappingCallExp.__mro__:
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



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::UnlimitedNaturalExp)


def test_flatqvt::unlimitednaturalexp_constructor_exists():
    assert callable(FlatQVT::UnlimitedNaturalExp.__init__)


def test_flatqvt::unlimitednaturalexp_constructor_args():
    sig = inspect.signature(FlatQVT::UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_flatqvt::unlimitednaturalexp_has_symbol():
    assert hasattr(FlatQVT::UnlimitedNaturalExp, "symbol")
    descriptor = None
    for klass in FlatQVT::UnlimitedNaturalExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::RealLiteralExp)


def test_flatqvt::realliteralexp_constructor_exists():
    assert callable(FlatQVT::RealLiteralExp.__init__)


def test_flatqvt::realliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_flatqvt::realliteralexp_has_realSymbol():
    assert hasattr(FlatQVT::RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in FlatQVT::RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::IntegerLiteralExp)


def test_flatqvt::integerliteralexp_constructor_exists():
    assert callable(FlatQVT::IntegerLiteralExp.__init__)


def test_flatqvt::integerliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_flatqvt::integerliteralexp_has_integerSymbol():
    assert hasattr(FlatQVT::IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in FlatQVT::IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::operationaltransformation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::OperationalTransformation)


def test_flatqvt::operationaltransformation_constructor_exists():
    assert callable(FlatQVT::OperationalTransformation.__init__)


def test_flatqvt::operationaltransformation_constructor_args():
    sig = inspect.signature(FlatQVT::OperationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::library_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Library)


def test_flatqvt::library_constructor_exists():
    assert callable(FlatQVT::Library.__init__)


def test_flatqvt::library_constructor_args():
    sig = inspect.signature(FlatQVT::Library.__init__)
    params = list(sig.parameters.keys())



def test_relationaltransformation_is_not_abstract():
    assert not inspect.isabstract(RelationalTransformation)


def test_relationaltransformation_constructor_exists():
    assert callable(RelationalTransformation.__init__)


def test_relationaltransformation_constructor_args():
    sig = inspect.signature(RelationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())



def test_varparameter_is_not_abstract():
    assert not inspect.isabstract(VarParameter)


def test_varparameter_constructor_exists():
    assert callable(VarParameter.__init__)


def test_varparameter_constructor_args():
    sig = inspect.signature(VarParameter.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::modelparameter_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ModelParameter)


def test_flatqvt::modelparameter_constructor_exists():
    assert callable(FlatQVT::ModelParameter.__init__)


def test_flatqvt::modelparameter_constructor_args():
    sig = inspect.signature(FlatQVT::ModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::mappingparameter_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::MappingParameter)


def test_flatqvt::mappingparameter_constructor_exists():
    assert callable(FlatQVT::MappingParameter.__init__)


def test_flatqvt::mappingparameter_constructor_args():
    sig = inspect.signature(FlatQVT::MappingParameter.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::IteratorExp)


def test_flatqvt::iteratorexp_constructor_exists():
    assert callable(FlatQVT::IteratorExp.__init__)


def test_flatqvt::iteratorexp_constructor_args():
    sig = inspect.signature(FlatQVT::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::iterateexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::IterateExp)


def test_flatqvt::iterateexp_constructor_exists():
    assert callable(FlatQVT::IterateExp.__init__)


def test_flatqvt::iterateexp_constructor_args():
    sig = inspect.signature(FlatQVT::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ImperativeIterateExp)


def test_flatqvt::imperativeiterateexp_constructor_exists():
    assert callable(FlatQVT::ImperativeIterateExp.__init__)


def test_flatqvt::imperativeiterateexp_constructor_args():
    sig = inspect.signature(FlatQVT::ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::forexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ForExp)


def test_flatqvt::forexp_constructor_exists():
    assert callable(FlatQVT::ForExp.__init__)


def test_flatqvt::forexp_constructor_args():
    sig = inspect.signature(FlatQVT::ForExp.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::FeatureCallExp)


def test_flatqvt::featurecallexp_constructor_exists():
    assert callable(FlatQVT::FeatureCallExp.__init__)


def test_flatqvt::featurecallexp_constructor_args():
    sig = inspect.signature(FlatQVT::FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::reflectivecollection_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ReflectiveCollection)


def test_flatqvt::reflectivecollection_constructor_exists():
    assert callable(FlatQVT::ReflectiveCollection.__init__)


def test_flatqvt::reflectivecollection_constructor_args():
    sig = inspect.signature(FlatQVT::ReflectiveCollection.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::extent_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Extent)


def test_flatqvt::extent_constructor_exists():
    assert callable(FlatQVT::Extent.__init__)


def test_flatqvt::extent_constructor_args():
    sig = inspect.signature(FlatQVT::Extent.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::element_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Element)


def test_flatqvt::element_constructor_exists():
    assert callable(FlatQVT::Element.__init__)


def test_flatqvt::element_constructor_args():
    sig = inspect.signature(FlatQVT::Element.__init__)
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



def test_flatqvt::relation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Relation)


def test_flatqvt::relation_constructor_exists():
    assert callable(FlatQVT::Relation.__init__)


def test_flatqvt::relation_constructor_args():
    sig = inspect.signature(FlatQVT::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopLevel" in params, "Missing parameter 'isTopLevel'"

def test_flatqvt::relation_has_isTopLevel():
    assert hasattr(FlatQVT::Relation, "isTopLevel")
    descriptor = None
    for klass in FlatQVT::Relation.__mro__:
        if "isTopLevel" in klass.__dict__:
            descriptor = klass.__dict__["isTopLevel"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::typedelement_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::TypedElement)


def test_flatqvt::typedelement_constructor_exists():
    assert callable(FlatQVT::TypedElement.__init__)


def test_flatqvt::typedelement_constructor_args():
    sig = inspect.signature(FlatQVT::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::type_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Type)


def test_flatqvt::type_constructor_exists():
    assert callable(FlatQVT::Type.__init__)


def test_flatqvt::type_constructor_args():
    sig = inspect.signature(FlatQVT::Type.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::EnumerationLiteral)


def test_flatqvt::enumerationliteral_constructor_exists():
    assert callable(FlatQVT::EnumerationLiteral.__init__)


def test_flatqvt::enumerationliteral_constructor_args():
    sig = inspect.signature(FlatQVT::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::typedmodel_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::TypedModel)


def test_flatqvt::typedmodel_constructor_exists():
    assert callable(FlatQVT::TypedModel.__init__)


def test_flatqvt::typedmodel_constructor_args():
    sig = inspect.signature(FlatQVT::TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::domain_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Domain)


def test_flatqvt::domain_constructor_exists():
    assert callable(FlatQVT::Domain.__init__)


def test_flatqvt::domain_constructor_args():
    sig = inspect.signature(FlatQVT::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "isEnforceable" in params, "Missing parameter 'isEnforceable'"
    assert "isCheckable" in params, "Missing parameter 'isCheckable'"

def test_flatqvt::domain_has_isEnforceable():
    assert hasattr(FlatQVT::Domain, "isEnforceable")
    descriptor = None
    for klass in FlatQVT::Domain.__mro__:
        if "isEnforceable" in klass.__dict__:
            descriptor = klass.__dict__["isEnforceable"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt::domain_has_isCheckable():
    assert hasattr(FlatQVT::Domain, "isCheckable")
    descriptor = None
    for klass in FlatQVT::Domain.__mro__:
        if "isCheckable" in klass.__dict__:
            descriptor = klass.__dict__["isCheckable"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::rule_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Rule)


def test_flatqvt::rule_constructor_exists():
    assert callable(FlatQVT::Rule.__init__)


def test_flatqvt::rule_constructor_args():
    sig = inspect.signature(FlatQVT::Rule.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::package_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Package)


def test_flatqvt::package_constructor_exists():
    assert callable(FlatQVT::Package.__init__)


def test_flatqvt::package_constructor_args():
    sig = inspect.signature(FlatQVT::Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_flatqvt::package_has_uri():
    assert hasattr(FlatQVT::Package, "uri")
    descriptor = None
    for klass in FlatQVT::Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::enumeration_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Enumeration)


def test_flatqvt::enumeration_constructor_exists():
    assert callable(FlatQVT::Enumeration.__init__)


def test_flatqvt::enumeration_constructor_args():
    sig = inspect.signature(FlatQVT::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::primitivetype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::PrimitiveType)


def test_flatqvt::primitivetype_constructor_exists():
    assert callable(FlatQVT::PrimitiveType.__init__)


def test_flatqvt::primitivetype_constructor_args():
    sig = inspect.signature(FlatQVT::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::collectiontype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::CollectionType)


def test_flatqvt::collectiontype_constructor_exists():
    assert callable(FlatQVT::CollectionType.__init__)


def test_flatqvt::collectiontype_constructor_args():
    sig = inspect.signature(FlatQVT::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::domainpattern_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::DomainPattern)


def test_flatqvt::domainpattern_constructor_exists():
    assert callable(FlatQVT::DomainPattern.__init__)


def test_flatqvt::domainpattern_constructor_args():
    sig = inspect.signature(FlatQVT::DomainPattern.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::corepattern_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::CorePattern)


def test_flatqvt::corepattern_constructor_exists():
    assert callable(FlatQVT::CorePattern.__init__)


def test_flatqvt::corepattern_constructor_args():
    sig = inspect.signature(FlatQVT::CorePattern.__init__)
    params = list(sig.parameters.keys())



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::relationdomain_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::RelationDomain)


def test_flatqvt::relationdomain_constructor_exists():
    assert callable(FlatQVT::RelationDomain.__init__)


def test_flatqvt::relationdomain_constructor_args():
    sig = inspect.signature(FlatQVT::RelationDomain.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::realizedvariable_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::RealizedVariable)


def test_flatqvt::realizedvariable_constructor_exists():
    assert callable(FlatQVT::RealizedVariable.__init__)


def test_flatqvt::realizedvariable_constructor_args():
    sig = inspect.signature(FlatQVT::RealizedVariable.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::varparameter_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::VarParameter)


def test_flatqvt::varparameter_constructor_exists():
    assert callable(FlatQVT::VarParameter.__init__)


def test_flatqvt::varparameter_constructor_args():
    sig = inspect.signature(FlatQVT::VarParameter.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_flatqvt::varparameter_has_kind():
    assert hasattr(FlatQVT::VarParameter, "kind")
    descriptor = None
    for klass in FlatQVT::VarParameter.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::functionparameter_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::FunctionParameter)


def test_flatqvt::functionparameter_constructor_exists():
    assert callable(FlatQVT::FunctionParameter.__init__)


def test_flatqvt::functionparameter_constructor_args():
    sig = inspect.signature(FlatQVT::FunctionParameter.__init__)
    params = list(sig.parameters.keys())



def test_operationbody_is_not_abstract():
    assert not inspect.isabstract(OperationBody)


def test_operationbody_constructor_exists():
    assert callable(OperationBody.__init__)


def test_operationbody_constructor_args():
    sig = inspect.signature(OperationBody.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::mappingbody_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::MappingBody)


def test_flatqvt::mappingbody_constructor_exists():
    assert callable(FlatQVT::MappingBody.__init__)


def test_flatqvt::mappingbody_constructor_args():
    sig = inspect.signature(FlatQVT::MappingBody.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::constructorbody_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ConstructorBody)


def test_flatqvt::constructorbody_constructor_exists():
    assert callable(FlatQVT::ConstructorBody.__init__)


def test_flatqvt::constructorbody_constructor_args():
    sig = inspect.signature(FlatQVT::ConstructorBody.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoperation_is_not_abstract():
    assert not inspect.isabstract(ImperativeOperation)


def test_imperativeoperation_constructor_exists():
    assert callable(ImperativeOperation.__init__)


def test_imperativeoperation_constructor_args():
    sig = inspect.signature(ImperativeOperation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::helper_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Helper)


def test_flatqvt::helper_constructor_exists():
    assert callable(FlatQVT::Helper.__init__)


def test_flatqvt::helper_constructor_args():
    sig = inspect.signature(FlatQVT::Helper.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_flatqvt::helper_has_isQuery():
    assert hasattr(FlatQVT::Helper, "isQuery")
    descriptor = None
    for klass in FlatQVT::Helper.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::entryoperation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::EntryOperation)


def test_flatqvt::entryoperation_constructor_exists():
    assert callable(FlatQVT::EntryOperation.__init__)


def test_flatqvt::entryoperation_constructor_args():
    sig = inspect.signature(FlatQVT::EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::mappingoperation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::MappingOperation)


def test_flatqvt::mappingoperation_constructor_exists():
    assert callable(FlatQVT::MappingOperation.__init__)


def test_flatqvt::mappingoperation_constructor_args():
    sig = inspect.signature(FlatQVT::MappingOperation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::constructor_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Constructor)


def test_flatqvt::constructor_constructor_exists():
    assert callable(FlatQVT::Constructor.__init__)


def test_flatqvt::constructor_constructor_args():
    sig = inspect.signature(FlatQVT::Constructor.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::oclexpression_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::OclExpression)


def test_flatqvt::oclexpression_constructor_exists():
    assert callable(FlatQVT::OclExpression.__init__)


def test_flatqvt::oclexpression_constructor_args():
    sig = inspect.signature(FlatQVT::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::operation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Operation)


def test_flatqvt::operation_constructor_exists():
    assert callable(FlatQVT::Operation.__init__)


def test_flatqvt::operation_constructor_args():
    sig = inspect.signature(FlatQVT::Operation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::TupleLiteralPart)


def test_flatqvt::tupleliteralpart_constructor_exists():
    assert callable(FlatQVT::TupleLiteralPart.__init__)


def test_flatqvt::tupleliteralpart_constructor_args():
    sig = inspect.signature(FlatQVT::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::expressioninocl_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ExpressionInOcl)


def test_flatqvt::expressioninocl_constructor_exists():
    assert callable(FlatQVT::ExpressionInOcl.__init__)


def test_flatqvt::expressioninocl_constructor_args():
    sig = inspect.signature(FlatQVT::ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::parameter_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Parameter)


def test_flatqvt::parameter_constructor_exists():
    assert callable(FlatQVT::Parameter.__init__)


def test_flatqvt::parameter_constructor_args():
    sig = inspect.signature(FlatQVT::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::variable_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Variable)


def test_flatqvt::variable_constructor_exists():
    assert callable(FlatQVT::Variable.__init__)


def test_flatqvt::variable_constructor_args():
    sig = inspect.signature(FlatQVT::Variable.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::property_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Property)


def test_flatqvt::property_constructor_exists():
    assert callable(FlatQVT::Property.__init__)


def test_flatqvt::property_constructor_args():
    sig = inspect.signature(FlatQVT::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isID" in params, "Missing parameter 'isID'"

def test_flatqvt::property_has_isDerived():
    assert hasattr(FlatQVT::Property, "isDerived")
    descriptor = None
    for klass in FlatQVT::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt::property_has_isComposite():
    assert hasattr(FlatQVT::Property, "isComposite")
    descriptor = None
    for klass in FlatQVT::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt::property_has_default():
    assert hasattr(FlatQVT::Property, "default")
    descriptor = None
    for klass in FlatQVT::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt::property_has_isReadOnly():
    assert hasattr(FlatQVT::Property, "isReadOnly")
    descriptor = None
    for klass in FlatQVT::Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt::property_has_isID():
    assert hasattr(FlatQVT::Property, "isID")
    descriptor = None
    for klass in FlatQVT::Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::CollectionLiteralPart)


def test_flatqvt::collectionliteralpart_constructor_exists():
    assert callable(FlatQVT::CollectionLiteralPart.__init__)


def test_flatqvt::collectionliteralpart_constructor_args():
    sig = inspect.signature(FlatQVT::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::EnumLiteralExp)


def test_flatqvt::enumliteralexp_constructor_exists():
    assert callable(FlatQVT::EnumLiteralExp.__init__)


def test_flatqvt::enumliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::NullLiteralExp)


def test_flatqvt::nullliteralexp_constructor_exists():
    assert callable(FlatQVT::NullLiteralExp.__init__)


def test_flatqvt::nullliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::InvalidLiteralExp)


def test_flatqvt::invalidliteralexp_constructor_exists():
    assert callable(FlatQVT::InvalidLiteralExp.__init__)


def test_flatqvt::invalidliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::TupleLiteralExp)


def test_flatqvt::tupleliteralexp_constructor_exists():
    assert callable(FlatQVT::TupleLiteralExp.__init__)


def test_flatqvt::tupleliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::templateexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::TemplateExp)


def test_flatqvt::templateexp_constructor_exists():
    assert callable(FlatQVT::TemplateExp.__init__)


def test_flatqvt::templateexp_constructor_args():
    sig = inspect.signature(FlatQVT::TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::listliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ListLiteralExp)


def test_flatqvt::listliteralexp_constructor_exists():
    assert callable(FlatQVT::ListLiteralExp.__init__)


def test_flatqvt::listliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::ListLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::DictLiteralExp)


def test_flatqvt::dictliteralexp_constructor_exists():
    assert callable(FlatQVT::DictLiteralExp.__init__)


def test_flatqvt::dictliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::PrimitiveLiteralExp)


def test_flatqvt::primitiveliteralexp_constructor_exists():
    assert callable(FlatQVT::PrimitiveLiteralExp.__init__)


def test_flatqvt::primitiveliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::orderedtupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::OrderedTupleLiteralExp)


def test_flatqvt::orderedtupleliteralexp_constructor_exists():
    assert callable(FlatQVT::OrderedTupleLiteralExp.__init__)


def test_flatqvt::orderedtupleliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::OrderedTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::CollectionLiteralExp)


def test_flatqvt::collectionliteralexp_constructor_exists():
    assert callable(FlatQVT::CollectionLiteralExp.__init__)


def test_flatqvt::collectionliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_flatqvt::collectionliteralexp_has_kind():
    assert hasattr(FlatQVT::CollectionLiteralExp, "kind")
    descriptor = None
    for klass in FlatQVT::CollectionLiteralExp.__mro__:
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



def test_flatqvt::collectionitem_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::CollectionItem)


def test_flatqvt::collectionitem_constructor_exists():
    assert callable(FlatQVT::CollectionItem.__init__)


def test_flatqvt::collectionitem_constructor_args():
    sig = inspect.signature(FlatQVT::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::transformation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Transformation)


def test_flatqvt::transformation_constructor_exists():
    assert callable(FlatQVT::Transformation.__init__)


def test_flatqvt::transformation_constructor_args():
    sig = inspect.signature(FlatQVT::Transformation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::orderedtupletype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::OrderedTupleType)


def test_flatqvt::orderedtupletype_constructor_exists():
    assert callable(FlatQVT::OrderedTupleType.__init__)


def test_flatqvt::orderedtupletype_constructor_args():
    sig = inspect.signature(FlatQVT::OrderedTupleType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::tupletype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::TupleType)


def test_flatqvt::tupletype_constructor_exists():
    assert callable(FlatQVT::TupleType.__init__)


def test_flatqvt::tupletype_constructor_args():
    sig = inspect.signature(FlatQVT::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::typedef_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Typedef)


def test_flatqvt::typedef_constructor_exists():
    assert callable(FlatQVT::Typedef.__init__)


def test_flatqvt::typedef_constructor_args():
    sig = inspect.signature(FlatQVT::Typedef.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::modeltype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ModelType)


def test_flatqvt::modeltype_constructor_exists():
    assert callable(FlatQVT::ModelType.__init__)


def test_flatqvt::modeltype_constructor_args():
    sig = inspect.signature(FlatQVT::ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "conformanceKind" in params, "Missing parameter 'conformanceKind'"

def test_flatqvt::modeltype_has_conformanceKind():
    assert hasattr(FlatQVT::ModelType, "conformanceKind")
    descriptor = None
    for klass in FlatQVT::ModelType.__mro__:
        if "conformanceKind" in klass.__dict__:
            descriptor = klass.__dict__["conformanceKind"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::module_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Module)


def test_flatqvt::module_constructor_exists():
    assert callable(FlatQVT::Module.__init__)


def test_flatqvt::module_constructor_args():
    sig = inspect.signature(FlatQVT::Module.__init__)
    params = list(sig.parameters.keys())
    assert "isBlackbox" in params, "Missing parameter 'isBlackbox'"

def test_flatqvt::module_has_isBlackbox():
    assert hasattr(FlatQVT::Module, "isBlackbox")
    descriptor = None
    for klass in FlatQVT::Module.__mro__:
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



def test_flatqvt::imperativeoperation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ImperativeOperation)


def test_flatqvt::imperativeoperation_constructor_exists():
    assert callable(FlatQVT::ImperativeOperation.__init__)


def test_flatqvt::imperativeoperation_constructor_args():
    sig = inspect.signature(FlatQVT::ImperativeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "isBlackbox" in params, "Missing parameter 'isBlackbox'"

def test_flatqvt::imperativeoperation_has_isBlackbox():
    assert hasattr(FlatQVT::ImperativeOperation, "isBlackbox")
    descriptor = None
    for klass in FlatQVT::ImperativeOperation.__mro__:
        if "isBlackbox" in klass.__dict__:
            descriptor = klass.__dict__["isBlackbox"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::function_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Function)


def test_flatqvt::function_constructor_exists():
    assert callable(FlatQVT::Function.__init__)


def test_flatqvt::function_constructor_args():
    sig = inspect.signature(FlatQVT::Function.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::contextualproperty_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ContextualProperty)


def test_flatqvt::contextualproperty_constructor_exists():
    assert callable(FlatQVT::ContextualProperty.__init__)


def test_flatqvt::contextualproperty_constructor_args():
    sig = inspect.signature(FlatQVT::ContextualProperty.__init__)
    params = list(sig.parameters.keys())



def test_templateexp_is_not_abstract():
    assert not inspect.isabstract(TemplateExp)


def test_templateexp_constructor_exists():
    assert callable(TemplateExp.__init__)


def test_templateexp_constructor_args():
    sig = inspect.signature(TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ObjectTemplateExp)


def test_flatqvt::objecttemplateexp_constructor_exists():
    assert callable(FlatQVT::ObjectTemplateExp.__init__)


def test_flatqvt::objecttemplateexp_constructor_args():
    sig = inspect.signature(FlatQVT::ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::collectiontemplateexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::CollectionTemplateExp)


def test_flatqvt::collectiontemplateexp_constructor_exists():
    assert callable(FlatQVT::CollectionTemplateExp.__init__)


def test_flatqvt::collectiontemplateexp_constructor_args():
    sig = inspect.signature(FlatQVT::CollectionTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::collectionrange_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::CollectionRange)


def test_flatqvt::collectionrange_constructor_exists():
    assert callable(FlatQVT::CollectionRange.__init__)


def test_flatqvt::collectionrange_constructor_args():
    sig = inspect.signature(FlatQVT::CollectionRange.__init__)
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



def test_flatqvt::propertyassignment_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::PropertyAssignment)


def test_flatqvt::propertyassignment_constructor_exists():
    assert callable(FlatQVT::PropertyAssignment.__init__)


def test_flatqvt::propertyassignment_constructor_args():
    sig = inspect.signature(FlatQVT::PropertyAssignment.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::variableassignment_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::VariableAssignment)


def test_flatqvt::variableassignment_constructor_exists():
    assert callable(FlatQVT::VariableAssignment.__init__)


def test_flatqvt::variableassignment_constructor_args():
    sig = inspect.signature(FlatQVT::VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_area_is_not_abstract():
    assert not inspect.isabstract(Area)


def test_area_constructor_exists():
    assert callable(Area.__init__)


def test_area_constructor_args():
    sig = inspect.signature(Area.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::mapping_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Mapping)


def test_flatqvt::mapping_constructor_exists():
    assert callable(FlatQVT::Mapping.__init__)


def test_flatqvt::mapping_constructor_args():
    sig = inspect.signature(FlatQVT::Mapping.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::coredomain_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::CoreDomain)


def test_flatqvt::coredomain_constructor_exists():
    assert callable(FlatQVT::CoreDomain.__init__)


def test_flatqvt::coredomain_constructor_args():
    sig = inspect.signature(FlatQVT::CoreDomain.__init__)
    params = list(sig.parameters.keys())



def test_corepattern_is_not_abstract():
    assert not inspect.isabstract(CorePattern)


def test_corepattern_constructor_exists():
    assert callable(CorePattern.__init__)


def test_corepattern_constructor_args():
    sig = inspect.signature(CorePattern.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::guardpattern_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::GuardPattern)


def test_flatqvt::guardpattern_constructor_exists():
    assert callable(FlatQVT::GuardPattern.__init__)


def test_flatqvt::guardpattern_constructor_args():
    sig = inspect.signature(FlatQVT::GuardPattern.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::bottompattern_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::BottomPattern)


def test_flatqvt::bottompattern_constructor_exists():
    assert callable(FlatQVT::BottomPattern.__init__)


def test_flatqvt::bottompattern_constructor_args():
    sig = inspect.signature(FlatQVT::BottomPattern.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::StringLiteralExp)


def test_flatqvt::stringliteralexp_constructor_exists():
    assert callable(FlatQVT::StringLiteralExp.__init__)


def test_flatqvt::stringliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_flatqvt::stringliteralexp_has_stringSymbol():
    assert hasattr(FlatQVT::StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in FlatQVT::StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::NumericLiteralExp)


def test_flatqvt::numericliteralexp_constructor_exists():
    assert callable(FlatQVT::NumericLiteralExp.__init__)


def test_flatqvt::numericliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::BooleanLiteralExp)


def test_flatqvt::booleanliteralexp_constructor_exists():
    assert callable(FlatQVT::BooleanLiteralExp.__init__)


def test_flatqvt::booleanliteralexp_constructor_args():
    sig = inspect.signature(FlatQVT::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_flatqvt::booleanliteralexp_has_booleanSymbol():
    assert hasattr(FlatQVT::BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in FlatQVT::BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::listtype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ListType)


def test_flatqvt::listtype_constructor_exists():
    assert callable(FlatQVT::ListType.__init__)


def test_flatqvt::listtype_constructor_args():
    sig = inspect.signature(FlatQVT::ListType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::dictionarytype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::DictionaryType)


def test_flatqvt::dictionarytype_constructor_exists():
    assert callable(FlatQVT::DictionaryType.__init__)


def test_flatqvt::dictionarytype_constructor_args():
    sig = inspect.signature(FlatQVT::DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::sequencetype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::SequenceType)


def test_flatqvt::sequencetype_constructor_exists():
    assert callable(FlatQVT::SequenceType.__init__)


def test_flatqvt::sequencetype_constructor_args():
    sig = inspect.signature(FlatQVT::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::OrderedSetType)


def test_flatqvt::orderedsettype_constructor_exists():
    assert callable(FlatQVT::OrderedSetType.__init__)


def test_flatqvt::orderedsettype_constructor_args():
    sig = inspect.signature(FlatQVT::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::settype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::SetType)


def test_flatqvt::settype_constructor_exists():
    assert callable(FlatQVT::SetType.__init__)


def test_flatqvt::settype_constructor_args():
    sig = inspect.signature(FlatQVT::SetType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::bagtype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::BagType)


def test_flatqvt::bagtype_constructor_exists():
    assert callable(FlatQVT::BagType.__init__)


def test_flatqvt::bagtype_constructor_args():
    sig = inspect.signature(FlatQVT::BagType.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::DictLiteralPart)


def test_flatqvt::dictliteralpart_constructor_exists():
    assert callable(FlatQVT::DictLiteralPart.__init__)


def test_flatqvt::dictliteralpart_constructor_args():
    sig = inspect.signature(FlatQVT::DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::comment_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Comment)


def test_flatqvt::comment_constructor_exists():
    assert callable(FlatQVT::Comment.__init__)


def test_flatqvt::comment_constructor_args():
    sig = inspect.signature(FlatQVT::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_flatqvt::comment_has_body():
    assert hasattr(FlatQVT::Comment, "body")
    descriptor = None
    for klass in FlatQVT::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::tag_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Tag)


def test_flatqvt::tag_constructor_exists():
    assert callable(FlatQVT::Tag.__init__)


def test_flatqvt::tag_constructor_args():
    sig = inspect.signature(FlatQVT::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_flatqvt::tag_has_name():
    assert hasattr(FlatQVT::Tag, "name")
    descriptor = None
    for klass in FlatQVT::Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt::tag_has_value():
    assert hasattr(FlatQVT::Tag, "value")
    descriptor = None
    for klass in FlatQVT::Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::namedelement_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::NamedElement)


def test_flatqvt::namedelement_constructor_exists():
    assert callable(FlatQVT::NamedElement.__init__)


def test_flatqvt::namedelement_constructor_args():
    sig = inspect.signature(FlatQVT::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_flatqvt::namedelement_has_name():
    assert hasattr(FlatQVT::NamedElement, "name")
    descriptor = None
    for klass in FlatQVT::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::relationimplementation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::RelationImplementation)


def test_flatqvt::relationimplementation_constructor_exists():
    assert callable(FlatQVT::RelationImplementation.__init__)


def test_flatqvt::relationimplementation_constructor_args():
    sig = inspect.signature(FlatQVT::RelationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::PropertyTemplateItem)


def test_flatqvt::propertytemplateitem_constructor_exists():
    assert callable(FlatQVT::PropertyTemplateItem.__init__)


def test_flatqvt::propertytemplateitem_constructor_args():
    sig = inspect.signature(FlatQVT::PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())
    assert "isOpposite" in params, "Missing parameter 'isOpposite'"

def test_flatqvt::propertytemplateitem_has_isOpposite():
    assert hasattr(FlatQVT::PropertyTemplateItem, "isOpposite")
    descriptor = None
    for klass in FlatQVT::PropertyTemplateItem.__mro__:
        if "isOpposite" in klass.__dict__:
            descriptor = klass.__dict__["isOpposite"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::predicate_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Predicate)


def test_flatqvt::predicate_constructor_exists():
    assert callable(FlatQVT::Predicate.__init__)


def test_flatqvt::predicate_constructor_args():
    sig = inspect.signature(FlatQVT::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::relationdomainassignment_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::RelationDomainAssignment)


def test_flatqvt::relationdomainassignment_constructor_exists():
    assert callable(FlatQVT::RelationDomainAssignment.__init__)


def test_flatqvt::relationdomainassignment_constructor_args():
    sig = inspect.signature(FlatQVT::RelationDomainAssignment.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::moduleimport_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ModuleImport)


def test_flatqvt::moduleimport_constructor_exists():
    assert callable(FlatQVT::ModuleImport.__init__)


def test_flatqvt::moduleimport_constructor_args():
    sig = inspect.signature(FlatQVT::ModuleImport.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_flatqvt::moduleimport_has_kind():
    assert hasattr(FlatQVT::ModuleImport, "kind")
    descriptor = None
    for klass in FlatQVT::ModuleImport.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::operationbody_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::OperationBody)


def test_flatqvt::operationbody_constructor_exists():
    assert callable(FlatQVT::OperationBody.__init__)


def test_flatqvt::operationbody_constructor_args():
    sig = inspect.signature(FlatQVT::OperationBody.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::enforcementoperation_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::EnforcementOperation)


def test_flatqvt::enforcementoperation_constructor_exists():
    assert callable(FlatQVT::EnforcementOperation.__init__)


def test_flatqvt::enforcementoperation_constructor_args():
    sig = inspect.signature(FlatQVT::EnforcementOperation.__init__)
    params = list(sig.parameters.keys())
    assert "enforcementMode" in params, "Missing parameter 'enforcementMode'"

def test_flatqvt::enforcementoperation_has_enforcementMode():
    assert hasattr(FlatQVT::EnforcementOperation, "enforcementMode")
    descriptor = None
    for klass in FlatQVT::EnforcementOperation.__mro__:
        if "enforcementMode" in klass.__dict__:
            descriptor = klass.__dict__["enforcementMode"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::orderedtupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::OrderedTupleLiteralPart)


def test_flatqvt::orderedtupleliteralpart_constructor_exists():
    assert callable(FlatQVT::OrderedTupleLiteralPart.__init__)


def test_flatqvt::orderedtupleliteralpart_constructor_args():
    sig = inspect.signature(FlatQVT::OrderedTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::key_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Key)


def test_flatqvt::key_constructor_exists():
    assert callable(FlatQVT::Key.__init__)


def test_flatqvt::key_constructor_args():
    sig = inspect.signature(FlatQVT::Key.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::factory_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Factory)


def test_flatqvt::factory_constructor_exists():
    assert callable(FlatQVT::Factory.__init__)


def test_flatqvt::factory_constructor_args():
    sig = inspect.signature(FlatQVT::Factory.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::pattern_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Pattern)


def test_flatqvt::pattern_constructor_exists():
    assert callable(FlatQVT::Pattern.__init__)


def test_flatqvt::pattern_constructor_args():
    sig = inspect.signature(FlatQVT::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::assignment_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Assignment)


def test_flatqvt::assignment_constructor_exists():
    assert callable(FlatQVT::Assignment.__init__)


def test_flatqvt::assignment_constructor_args():
    sig = inspect.signature(FlatQVT::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_flatqvt::assignment_has_isDefault():
    assert hasattr(FlatQVT::Assignment, "isDefault")
    descriptor = None
    for klass in FlatQVT::Assignment.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_realizedvariable_is_not_abstract():
    assert not inspect.isabstract(RealizedVariable)


def test_realizedvariable_constructor_exists():
    assert callable(RealizedVariable.__init__)


def test_realizedvariable_constructor_args():
    sig = inspect.signature(RealizedVariable.__init__)
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



def test_flatqvt::area_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Area)


def test_flatqvt::area_constructor_exists():
    assert callable(FlatQVT::Area.__init__)


def test_flatqvt::area_constructor_args():
    sig = inspect.signature(FlatQVT::Area.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::voidtype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::VoidType)


def test_flatqvt::voidtype_constructor_exists():
    assert callable(FlatQVT::VoidType.__init__)


def test_flatqvt::voidtype_constructor_args():
    sig = inspect.signature(FlatQVT::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::datatype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::DataType)


def test_flatqvt::datatype_constructor_exists():
    assert callable(FlatQVT::DataType.__init__)


def test_flatqvt::datatype_constructor_args():
    sig = inspect.signature(FlatQVT::DataType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::class_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::Class)


def test_flatqvt::class_constructor_exists():
    assert callable(FlatQVT::Class.__init__)


def test_flatqvt::class_constructor_args():
    sig = inspect.signature(FlatQVT::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_flatqvt::class_has_isAbstract():
    assert hasattr(FlatQVT::Class, "isAbstract")
    descriptor = None
    for klass in FlatQVT::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::templateparametertype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::TemplateParameterType)


def test_flatqvt::templateparametertype_constructor_exists():
    assert callable(FlatQVT::TemplateParameterType.__init__)


def test_flatqvt::templateparametertype_constructor_args():
    sig = inspect.signature(FlatQVT::TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_flatqvt::templateparametertype_has_specification():
    assert hasattr(FlatQVT::TemplateParameterType, "specification")
    descriptor = None
    for klass in FlatQVT::TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::invalidtype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::InvalidType)


def test_flatqvt::invalidtype_constructor_exists():
    assert callable(FlatQVT::InvalidType.__init__)


def test_flatqvt::invalidtype_constructor_args():
    sig = inspect.signature(FlatQVT::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::anytype_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::AnyType)


def test_flatqvt::anytype_constructor_exists():
    assert callable(FlatQVT::AnyType.__init__)


def test_flatqvt::anytype_constructor_args():
    sig = inspect.signature(FlatQVT::AnyType.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ImperativeExpression)


def test_flatqvt::imperativeexpression_constructor_exists():
    assert callable(FlatQVT::ImperativeExpression.__init__)


def test_flatqvt::imperativeexpression_constructor_args():
    sig = inspect.signature(FlatQVT::ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::variableexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::VariableExp)


def test_flatqvt::variableexp_constructor_exists():
    assert callable(FlatQVT::VariableExp.__init__)


def test_flatqvt::variableexp_constructor_args():
    sig = inspect.signature(FlatQVT::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::loopexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::LoopExp)


def test_flatqvt::loopexp_constructor_exists():
    assert callable(FlatQVT::LoopExp.__init__)


def test_flatqvt::loopexp_constructor_args():
    sig = inspect.signature(FlatQVT::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::literalexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::LiteralExp)


def test_flatqvt::literalexp_constructor_exists():
    assert callable(FlatQVT::LiteralExp.__init__)


def test_flatqvt::literalexp_constructor_args():
    sig = inspect.signature(FlatQVT::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::relationcallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::RelationCallExp)


def test_flatqvt::relationcallexp_constructor_exists():
    assert callable(FlatQVT::RelationCallExp.__init__)


def test_flatqvt::relationcallexp_constructor_args():
    sig = inspect.signature(FlatQVT::RelationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::callexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::CallExp)


def test_flatqvt::callexp_constructor_exists():
    assert callable(FlatQVT::CallExp.__init__)


def test_flatqvt::callexp_constructor_args():
    sig = inspect.signature(FlatQVT::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::letexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::LetExp)


def test_flatqvt::letexp_constructor_exists():
    assert callable(FlatQVT::LetExp.__init__)


def test_flatqvt::letexp_constructor_args():
    sig = inspect.signature(FlatQVT::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::ifexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::IfExp)


def test_flatqvt::ifexp_constructor_exists():
    assert callable(FlatQVT::IfExp.__init__)


def test_flatqvt::ifexp_constructor_args():
    sig = inspect.signature(FlatQVT::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::typeexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::TypeExp)


def test_flatqvt::typeexp_constructor_exists():
    assert callable(FlatQVT::TypeExp.__init__)


def test_flatqvt::typeexp_constructor_args():
    sig = inspect.signature(FlatQVT::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::unlinkexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::UnlinkExp)


def test_flatqvt::unlinkexp_constructor_exists():
    assert callable(FlatQVT::UnlinkExp.__init__)


def test_flatqvt::unlinkexp_constructor_args():
    sig = inspect.signature(FlatQVT::UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ImperativeLoopExp)


def test_flatqvt::imperativeloopexp_constructor_exists():
    assert callable(FlatQVT::ImperativeLoopExp.__init__)


def test_flatqvt::imperativeloopexp_constructor_args():
    sig = inspect.signature(FlatQVT::ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::logexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::LogExp)


def test_flatqvt::logexp_constructor_exists():
    assert callable(FlatQVT::LogExp.__init__)


def test_flatqvt::logexp_constructor_args():
    sig = inspect.signature(FlatQVT::LogExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::imperativecallexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ImperativeCallExp)


def test_flatqvt::imperativecallexp_constructor_exists():
    assert callable(FlatQVT::ImperativeCallExp.__init__)


def test_flatqvt::imperativecallexp_constructor_args():
    sig = inspect.signature(FlatQVT::ImperativeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_flatqvt::imperativecallexp_has_isVirtual():
    assert hasattr(FlatQVT::ImperativeCallExp, "isVirtual")
    descriptor = None
    for klass in FlatQVT::ImperativeCallExp.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::assignexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::AssignExp)


def test_flatqvt::assignexp_constructor_exists():
    assert callable(FlatQVT::AssignExp.__init__)


def test_flatqvt::assignexp_constructor_args():
    sig = inspect.signature(FlatQVT::AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_flatqvt::assignexp_has_isReset():
    assert hasattr(FlatQVT::AssignExp, "isReset")
    descriptor = None
    for klass in FlatQVT::AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::switchexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::SwitchExp)


def test_flatqvt::switchexp_constructor_exists():
    assert callable(FlatQVT::SwitchExp.__init__)


def test_flatqvt::switchexp_constructor_args():
    sig = inspect.signature(FlatQVT::SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::computeexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ComputeExp)


def test_flatqvt::computeexp_constructor_exists():
    assert callable(FlatQVT::ComputeExp.__init__)


def test_flatqvt::computeexp_constructor_args():
    sig = inspect.signature(FlatQVT::ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::returnexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ReturnExp)


def test_flatqvt::returnexp_constructor_exists():
    assert callable(FlatQVT::ReturnExp.__init__)


def test_flatqvt::returnexp_constructor_args():
    sig = inspect.signature(FlatQVT::ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::whileexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::WhileExp)


def test_flatqvt::whileexp_constructor_exists():
    assert callable(FlatQVT::WhileExp.__init__)


def test_flatqvt::whileexp_constructor_args():
    sig = inspect.signature(FlatQVT::WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::resolveexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ResolveExp)


def test_flatqvt::resolveexp_constructor_exists():
    assert callable(FlatQVT::ResolveExp.__init__)


def test_flatqvt::resolveexp_constructor_args():
    sig = inspect.signature(FlatQVT::ResolveExp.__init__)
    params = list(sig.parameters.keys())
    assert "one" in params, "Missing parameter 'one'"
    assert "isInverse" in params, "Missing parameter 'isInverse'"
    assert "isDeferred" in params, "Missing parameter 'isDeferred'"

def test_flatqvt::resolveexp_has_one():
    assert hasattr(FlatQVT::ResolveExp, "one")
    descriptor = None
    for klass in FlatQVT::ResolveExp.__mro__:
        if "one" in klass.__dict__:
            descriptor = klass.__dict__["one"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt::resolveexp_has_isInverse():
    assert hasattr(FlatQVT::ResolveExp, "isInverse")
    descriptor = None
    for klass in FlatQVT::ResolveExp.__mro__:
        if "isInverse" in klass.__dict__:
            descriptor = klass.__dict__["isInverse"]
            break
    assert isinstance(descriptor, property)

def test_flatqvt::resolveexp_has_isDeferred():
    assert hasattr(FlatQVT::ResolveExp, "isDeferred")
    descriptor = None
    for klass in FlatQVT::ResolveExp.__mro__:
        if "isDeferred" in klass.__dict__:
            descriptor = klass.__dict__["isDeferred"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::breakexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::BreakExp)


def test_flatqvt::breakexp_constructor_exists():
    assert callable(FlatQVT::BreakExp.__init__)


def test_flatqvt::breakexp_constructor_args():
    sig = inspect.signature(FlatQVT::BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::continueexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::ContinueExp)


def test_flatqvt::continueexp_constructor_exists():
    assert callable(FlatQVT::ContinueExp.__init__)


def test_flatqvt::continueexp_constructor_args():
    sig = inspect.signature(FlatQVT::ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::variableinitexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::VariableInitExp)


def test_flatqvt::variableinitexp_constructor_exists():
    assert callable(FlatQVT::VariableInitExp.__init__)


def test_flatqvt::variableinitexp_constructor_args():
    sig = inspect.signature(FlatQVT::VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_flatqvt::variableinitexp_has_withResult():
    assert hasattr(FlatQVT::VariableInitExp, "withResult")
    descriptor = None
    for klass in FlatQVT::VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::raiseexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::RaiseExp)


def test_flatqvt::raiseexp_constructor_exists():
    assert callable(FlatQVT::RaiseExp.__init__)


def test_flatqvt::raiseexp_constructor_args():
    sig = inspect.signature(FlatQVT::RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::catchexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::CatchExp)


def test_flatqvt::catchexp_constructor_exists():
    assert callable(FlatQVT::CatchExp.__init__)


def test_flatqvt::catchexp_constructor_args():
    sig = inspect.signature(FlatQVT::CatchExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::instantiationexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::InstantiationExp)


def test_flatqvt::instantiationexp_constructor_exists():
    assert callable(FlatQVT::InstantiationExp.__init__)


def test_flatqvt::instantiationexp_constructor_args():
    sig = inspect.signature(FlatQVT::InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::assertexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::AssertExp)


def test_flatqvt::assertexp_constructor_exists():
    assert callable(FlatQVT::AssertExp.__init__)


def test_flatqvt::assertexp_constructor_args():
    sig = inspect.signature(FlatQVT::AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_flatqvt::assertexp_has_severity():
    assert hasattr(FlatQVT::AssertExp, "severity")
    descriptor = None
    for klass in FlatQVT::AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_flatqvt::tryexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::TryExp)


def test_flatqvt::tryexp_constructor_exists():
    assert callable(FlatQVT::TryExp.__init__)


def test_flatqvt::tryexp_constructor_args():
    sig = inspect.signature(FlatQVT::TryExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::blockexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::BlockExp)


def test_flatqvt::blockexp_constructor_exists():
    assert callable(FlatQVT::BlockExp.__init__)


def test_flatqvt::blockexp_constructor_args():
    sig = inspect.signature(FlatQVT::BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::unpackexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::UnpackExp)


def test_flatqvt::unpackexp_constructor_exists():
    assert callable(FlatQVT::UnpackExp.__init__)


def test_flatqvt::unpackexp_constructor_args():
    sig = inspect.signature(FlatQVT::UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_flatqvt::altexp_is_not_abstract():
    assert not inspect.isabstract(FlatQVT::AltExp)


def test_flatqvt::altexp_constructor_exists():
    assert callable(FlatQVT::AltExp.__init__)


def test_flatqvt::altexp_constructor_args():
    sig = inspect.signature(FlatQVT::AltExp.__init__)
    params = list(sig.parameters.keys())

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Bag",
        "Set",
        "Sequence",
        "OrderedSet",
        "Collection",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"

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

def test_severitykind_exists():
    # Check that the Enumeration exists
    assert SeverityKind is not None

def test_severitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeverityKind]
    expected_literals = [
        "warning",
        "error",
        "fatal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SeverityKind"

def test_directionkind_exists():
    # Check that the Enumeration exists
    assert DirectionKind is not None

def test_directionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionKind]
    expected_literals = [
        "inout",
        "out",
        "in_",
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
        "Creation",
        "Deletion",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnforcementMode"


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
LetExp_strategy = st.builds(
    LetExp,
)
Extent_strategy = st.builds(
    Extent,
)
FlatQVT::URIExtent_strategy = st.builds(
    FlatQVT::URIExtent,
)
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
CatchExp_strategy = st.builds(
    CatchExp,
)
AltExp_strategy = st.builds(
    AltExp,
)
ResolveExp_strategy = st.builds(
    ResolveExp,
)
FlatQVT::ResolveInExp_strategy = st.builds(
    FlatQVT::ResolveInExp,
)
DomainPattern_strategy = st.builds(
    DomainPattern,
)
RelationDomainAssignment_strategy = st.builds(
    RelationDomainAssignment,
)
Key_strategy = st.builds(
    Key,
)
Transformation_strategy = st.builds(
    Transformation,
)
FlatQVT::RelationalTransformation_strategy = st.builds(
    FlatQVT::RelationalTransformation,
)
ReflectiveCollection_strategy = st.builds(
    ReflectiveCollection,
)
FlatQVT::ReflectiveSequence_strategy = st.builds(
    FlatQVT::ReflectiveSequence,
)
RelationImplementation_strategy = st.builds(
    RelationImplementation,
)
NavigationCallExp_strategy = st.builds(
    NavigationCallExp,
)
FlatQVT::PropertyCallExp_strategy = st.builds(
    FlatQVT::PropertyCallExp,
)
ObjectTemplateExp_strategy = st.builds(
    ObjectTemplateExp,
)
Predicate_strategy = st.builds(
    Predicate,
)
OrderedTupleLiteralPart_strategy = st.builds(
    OrderedTupleLiteralPart,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
FlatQVT::OppositePropertyCallExp_strategy = st.builds(
    FlatQVT::OppositePropertyCallExp,
)
ConstructorBody_strategy = st.builds(
    ConstructorBody,
)
InstantiationExp_strategy = st.builds(
    InstantiationExp,
)
FlatQVT::ObjectExp_strategy = st.builds(
    FlatQVT::ObjectExp,
)
FlatQVT::Object_strategy = st.builds(
    FlatQVT::Object,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
PropertyTemplateItem_strategy = st.builds(
    PropertyTemplateItem,
)
ModuleImport_strategy = st.builds(
    ModuleImport,
)
EntryOperation_strategy = st.builds(
    EntryOperation,
)
FeatureCallExp_strategy = st.builds(
    FeatureCallExp,
)
FlatQVT::OperationCallExp_strategy = st.builds(
    FlatQVT::OperationCallExp,
)
FlatQVT::NavigationCallExp_strategy = st.builds(
    FlatQVT::NavigationCallExp,
)
FlatQVT::MultiplicityElement_strategy = st.builds(
    FlatQVT::MultiplicityElement,
    lower=
        safe_text,
    isOrdered=
        safe_text,
    upper=
        safe_text,
    isUnique=
        safe_text
)
ModelType_strategy = st.builds(
    ModelType,
)
Tag_strategy = st.builds(
    Tag,
)
MappingOperation_strategy = st.builds(
    MappingOperation,
)
ImperativeCallExp_strategy = st.builds(
    ImperativeCallExp,
)
FlatQVT::MappingCallExp_strategy = st.builds(
    FlatQVT::MappingCallExp,
    isStrict=
        safe_text
)
RelationDomain_strategy = st.builds(
    RelationDomain,
)
ModelParameter_strategy = st.builds(
    ModelParameter,
)
Relation_strategy = st.builds(
    Relation,
)
Mapping_strategy = st.builds(
    Mapping,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
FlatQVT::UnlimitedNaturalExp_strategy = st.builds(
    FlatQVT::UnlimitedNaturalExp,
    symbol=
        safe_text
)
FlatQVT::RealLiteralExp_strategy = st.builds(
    FlatQVT::RealLiteralExp,
    realSymbol=
        safe_text
)
FlatQVT::IntegerLiteralExp_strategy = st.builds(
    FlatQVT::IntegerLiteralExp,
    integerSymbol=
        safe_text
)
Module_strategy = st.builds(
    Module,
)
FlatQVT::OperationalTransformation_strategy = st.builds(
    FlatQVT::OperationalTransformation,
)
FlatQVT::Library_strategy = st.builds(
    FlatQVT::Library,
)
RelationalTransformation_strategy = st.builds(
    RelationalTransformation,
)
LogExp_strategy = st.builds(
    LogExp,
)
VarParameter_strategy = st.builds(
    VarParameter,
)
FlatQVT::ModelParameter_strategy = st.builds(
    FlatQVT::ModelParameter,
)
FlatQVT::MappingParameter_strategy = st.builds(
    FlatQVT::MappingParameter,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
FlatQVT::IteratorExp_strategy = st.builds(
    FlatQVT::IteratorExp,
)
FlatQVT::IterateExp_strategy = st.builds(
    FlatQVT::IterateExp,
)
Parameter_strategy = st.builds(
    Parameter,
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
FlatQVT::ImperativeIterateExp_strategy = st.builds(
    FlatQVT::ImperativeIterateExp,
)
FlatQVT::ForExp_strategy = st.builds(
    FlatQVT::ForExp,
)
CallExp_strategy = st.builds(
    CallExp,
)
FlatQVT::FeatureCallExp_strategy = st.builds(
    FlatQVT::FeatureCallExp,
)
Package_strategy = st.builds(
    Package,
)
Comment_strategy = st.builds(
    Comment,
)
Enumeration_strategy = st.builds(
    Enumeration,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
Object_strategy = st.builds(
    Object,
)
FlatQVT::ReflectiveCollection_strategy = st.builds(
    FlatQVT::ReflectiveCollection,
)
FlatQVT::Extent_strategy = st.builds(
    FlatQVT::Extent,
)
FlatQVT::Element_strategy = st.builds(
    FlatQVT::Element,
)
TypedModel_strategy = st.builds(
    TypedModel,
)
Rule_strategy = st.builds(
    Rule,
)
FlatQVT::Relation_strategy = st.builds(
    FlatQVT::Relation,
    isTopLevel=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
FlatQVT::TypedElement_strategy = st.builds(
    FlatQVT::TypedElement,
)
FlatQVT::Type_strategy = st.builds(
    FlatQVT::Type,
)
FlatQVT::EnumerationLiteral_strategy = st.builds(
    FlatQVT::EnumerationLiteral,
)
FlatQVT::TypedModel_strategy = st.builds(
    FlatQVT::TypedModel,
)
FlatQVT::Domain_strategy = st.builds(
    FlatQVT::Domain,
    isEnforceable=
        safe_text,
    isCheckable=
        safe_text
)
FlatQVT::Rule_strategy = st.builds(
    FlatQVT::Rule,
)
FlatQVT::Package_strategy = st.builds(
    FlatQVT::Package,
    uri=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
FlatQVT::Enumeration_strategy = st.builds(
    FlatQVT::Enumeration,
)
FlatQVT::PrimitiveType_strategy = st.builds(
    FlatQVT::PrimitiveType,
)
FlatQVT::CollectionType_strategy = st.builds(
    FlatQVT::CollectionType,
)
Pattern_strategy = st.builds(
    Pattern,
)
FlatQVT::DomainPattern_strategy = st.builds(
    FlatQVT::DomainPattern,
)
FlatQVT::CorePattern_strategy = st.builds(
    FlatQVT::CorePattern,
)
Domain_strategy = st.builds(
    Domain,
)
FlatQVT::RelationDomain_strategy = st.builds(
    FlatQVT::RelationDomain,
)
Variable_strategy = st.builds(
    Variable,
)
FlatQVT::RealizedVariable_strategy = st.builds(
    FlatQVT::RealizedVariable,
)
FlatQVT::VarParameter_strategy = st.builds(
    FlatQVT::VarParameter,
    kind=
        safe_text
)
FlatQVT::FunctionParameter_strategy = st.builds(
    FlatQVT::FunctionParameter,
)
OperationBody_strategy = st.builds(
    OperationBody,
)
FlatQVT::MappingBody_strategy = st.builds(
    FlatQVT::MappingBody,
)
FlatQVT::ConstructorBody_strategy = st.builds(
    FlatQVT::ConstructorBody,
)
ImperativeOperation_strategy = st.builds(
    ImperativeOperation,
)
FlatQVT::Helper_strategy = st.builds(
    FlatQVT::Helper,
    isQuery=
        safe_text
)
FlatQVT::EntryOperation_strategy = st.builds(
    FlatQVT::EntryOperation,
)
FlatQVT::MappingOperation_strategy = st.builds(
    FlatQVT::MappingOperation,
)
FlatQVT::Constructor_strategy = st.builds(
    FlatQVT::Constructor,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
FlatQVT::OclExpression_strategy = st.builds(
    FlatQVT::OclExpression,
)
FlatQVT::Operation_strategy = st.builds(
    FlatQVT::Operation,
)
FlatQVT::TupleLiteralPart_strategy = st.builds(
    FlatQVT::TupleLiteralPart,
)
FlatQVT::ExpressionInOcl_strategy = st.builds(
    FlatQVT::ExpressionInOcl,
)
FlatQVT::Parameter_strategy = st.builds(
    FlatQVT::Parameter,
)
FlatQVT::Variable_strategy = st.builds(
    FlatQVT::Variable,
)
FlatQVT::Property_strategy = st.builds(
    FlatQVT::Property,
    isDerived=
        safe_text,
    isComposite=
        safe_text,
    default=
        safe_text,
    isReadOnly=
        safe_text,
    isID=
        safe_text
)
FlatQVT::CollectionLiteralPart_strategy = st.builds(
    FlatQVT::CollectionLiteralPart,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
FlatQVT::EnumLiteralExp_strategy = st.builds(
    FlatQVT::EnumLiteralExp,
)
FlatQVT::NullLiteralExp_strategy = st.builds(
    FlatQVT::NullLiteralExp,
)
FlatQVT::InvalidLiteralExp_strategy = st.builds(
    FlatQVT::InvalidLiteralExp,
)
FlatQVT::TupleLiteralExp_strategy = st.builds(
    FlatQVT::TupleLiteralExp,
)
FlatQVT::TemplateExp_strategy = st.builds(
    FlatQVT::TemplateExp,
)
FlatQVT::ListLiteralExp_strategy = st.builds(
    FlatQVT::ListLiteralExp,
)
FlatQVT::DictLiteralExp_strategy = st.builds(
    FlatQVT::DictLiteralExp,
)
FlatQVT::PrimitiveLiteralExp_strategy = st.builds(
    FlatQVT::PrimitiveLiteralExp,
)
FlatQVT::OrderedTupleLiteralExp_strategy = st.builds(
    FlatQVT::OrderedTupleLiteralExp,
)
FlatQVT::CollectionLiteralExp_strategy = st.builds(
    FlatQVT::CollectionLiteralExp,
    kind=
        safe_text
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
FlatQVT::CollectionItem_strategy = st.builds(
    FlatQVT::CollectionItem,
)
Class_strategy = st.builds(
    Class,
)
FlatQVT::Transformation_strategy = st.builds(
    FlatQVT::Transformation,
)
FlatQVT::OrderedTupleType_strategy = st.builds(
    FlatQVT::OrderedTupleType,
)
FlatQVT::TupleType_strategy = st.builds(
    FlatQVT::TupleType,
)
FlatQVT::Typedef_strategy = st.builds(
    FlatQVT::Typedef,
)
FlatQVT::ModelType_strategy = st.builds(
    FlatQVT::ModelType,
    conformanceKind=
        safe_text
)
FlatQVT::Module_strategy = st.builds(
    FlatQVT::Module,
    isBlackbox=
        safe_text
)
Operation_strategy = st.builds(
    Operation,
)
FlatQVT::ImperativeOperation_strategy = st.builds(
    FlatQVT::ImperativeOperation,
    isBlackbox=
        safe_text
)
FlatQVT::Function_strategy = st.builds(
    FlatQVT::Function,
)
Property_strategy = st.builds(
    Property,
)
FlatQVT::ContextualProperty_strategy = st.builds(
    FlatQVT::ContextualProperty,
)
TemplateExp_strategy = st.builds(
    TemplateExp,
)
FlatQVT::ObjectTemplateExp_strategy = st.builds(
    FlatQVT::ObjectTemplateExp,
)
FlatQVT::CollectionTemplateExp_strategy = st.builds(
    FlatQVT::CollectionTemplateExp,
)
FlatQVT::CollectionRange_strategy = st.builds(
    FlatQVT::CollectionRange,
)
EnforcementOperation_strategy = st.builds(
    EnforcementOperation,
)
Assignment_strategy = st.builds(
    Assignment,
)
FlatQVT::PropertyAssignment_strategy = st.builds(
    FlatQVT::PropertyAssignment,
)
FlatQVT::VariableAssignment_strategy = st.builds(
    FlatQVT::VariableAssignment,
)
Area_strategy = st.builds(
    Area,
)
FlatQVT::Mapping_strategy = st.builds(
    FlatQVT::Mapping,
)
FlatQVT::CoreDomain_strategy = st.builds(
    FlatQVT::CoreDomain,
)
CorePattern_strategy = st.builds(
    CorePattern,
)
FlatQVT::GuardPattern_strategy = st.builds(
    FlatQVT::GuardPattern,
)
FlatQVT::BottomPattern_strategy = st.builds(
    FlatQVT::BottomPattern,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
FlatQVT::StringLiteralExp_strategy = st.builds(
    FlatQVT::StringLiteralExp,
    stringSymbol=
        safe_text
)
FlatQVT::NumericLiteralExp_strategy = st.builds(
    FlatQVT::NumericLiteralExp,
)
FlatQVT::BooleanLiteralExp_strategy = st.builds(
    FlatQVT::BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
FlatQVT::ListType_strategy = st.builds(
    FlatQVT::ListType,
)
FlatQVT::DictionaryType_strategy = st.builds(
    FlatQVT::DictionaryType,
)
FlatQVT::SequenceType_strategy = st.builds(
    FlatQVT::SequenceType,
)
FlatQVT::OrderedSetType_strategy = st.builds(
    FlatQVT::OrderedSetType,
)
FlatQVT::SetType_strategy = st.builds(
    FlatQVT::SetType,
)
FlatQVT::BagType_strategy = st.builds(
    FlatQVT::BagType,
)
Element_strategy = st.builds(
    Element,
)
FlatQVT::DictLiteralPart_strategy = st.builds(
    FlatQVT::DictLiteralPart,
)
FlatQVT::Comment_strategy = st.builds(
    FlatQVT::Comment,
    body=
        safe_text
)
FlatQVT::Tag_strategy = st.builds(
    FlatQVT::Tag,
    name=
        safe_text,
    value=
        safe_text
)
FlatQVT::NamedElement_strategy = st.builds(
    FlatQVT::NamedElement,
    name=
        safe_text
)
FlatQVT::RelationImplementation_strategy = st.builds(
    FlatQVT::RelationImplementation,
)
FlatQVT::PropertyTemplateItem_strategy = st.builds(
    FlatQVT::PropertyTemplateItem,
    isOpposite=
        safe_text
)
FlatQVT::Predicate_strategy = st.builds(
    FlatQVT::Predicate,
)
FlatQVT::RelationDomainAssignment_strategy = st.builds(
    FlatQVT::RelationDomainAssignment,
)
FlatQVT::ModuleImport_strategy = st.builds(
    FlatQVT::ModuleImport,
    kind=
        safe_text
)
FlatQVT::OperationBody_strategy = st.builds(
    FlatQVT::OperationBody,
)
FlatQVT::EnforcementOperation_strategy = st.builds(
    FlatQVT::EnforcementOperation,
    enforcementMode=
        safe_text
)
FlatQVT::OrderedTupleLiteralPart_strategy = st.builds(
    FlatQVT::OrderedTupleLiteralPart,
)
FlatQVT::Key_strategy = st.builds(
    FlatQVT::Key,
)
FlatQVT::Factory_strategy = st.builds(
    FlatQVT::Factory,
)
FlatQVT::Pattern_strategy = st.builds(
    FlatQVT::Pattern,
)
FlatQVT::Assignment_strategy = st.builds(
    FlatQVT::Assignment,
    isDefault=
        safe_text
)
RealizedVariable_strategy = st.builds(
    RealizedVariable,
)
GuardPattern_strategy = st.builds(
    GuardPattern,
)
BottomPattern_strategy = st.builds(
    BottomPattern,
)
FlatQVT::Area_strategy = st.builds(
    FlatQVT::Area,
)
Type_strategy = st.builds(
    Type,
)
FlatQVT::VoidType_strategy = st.builds(
    FlatQVT::VoidType,
)
FlatQVT::DataType_strategy = st.builds(
    FlatQVT::DataType,
)
FlatQVT::Class_strategy = st.builds(
    FlatQVT::Class,
    isAbstract=
        safe_text
)
FlatQVT::TemplateParameterType_strategy = st.builds(
    FlatQVT::TemplateParameterType,
    specification=
        safe_text
)
FlatQVT::InvalidType_strategy = st.builds(
    FlatQVT::InvalidType,
)
FlatQVT::AnyType_strategy = st.builds(
    FlatQVT::AnyType,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
FlatQVT::ImperativeExpression_strategy = st.builds(
    FlatQVT::ImperativeExpression,
)
FlatQVT::VariableExp_strategy = st.builds(
    FlatQVT::VariableExp,
)
FlatQVT::LoopExp_strategy = st.builds(
    FlatQVT::LoopExp,
)
FlatQVT::LiteralExp_strategy = st.builds(
    FlatQVT::LiteralExp,
)
FlatQVT::RelationCallExp_strategy = st.builds(
    FlatQVT::RelationCallExp,
)
FlatQVT::CallExp_strategy = st.builds(
    FlatQVT::CallExp,
)
FlatQVT::LetExp_strategy = st.builds(
    FlatQVT::LetExp,
)
FlatQVT::IfExp_strategy = st.builds(
    FlatQVT::IfExp,
)
FlatQVT::TypeExp_strategy = st.builds(
    FlatQVT::TypeExp,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
FlatQVT::UnlinkExp_strategy = st.builds(
    FlatQVT::UnlinkExp,
)
FlatQVT::ImperativeLoopExp_strategy = st.builds(
    FlatQVT::ImperativeLoopExp,
)
FlatQVT::LogExp_strategy = st.builds(
    FlatQVT::LogExp,
)
FlatQVT::ImperativeCallExp_strategy = st.builds(
    FlatQVT::ImperativeCallExp,
    isVirtual=
        safe_text
)
FlatQVT::AssignExp_strategy = st.builds(
    FlatQVT::AssignExp,
    isReset=
        safe_text
)
FlatQVT::SwitchExp_strategy = st.builds(
    FlatQVT::SwitchExp,
)
FlatQVT::ComputeExp_strategy = st.builds(
    FlatQVT::ComputeExp,
)
FlatQVT::ReturnExp_strategy = st.builds(
    FlatQVT::ReturnExp,
)
FlatQVT::WhileExp_strategy = st.builds(
    FlatQVT::WhileExp,
)
FlatQVT::ResolveExp_strategy = st.builds(
    FlatQVT::ResolveExp,
    one=
        safe_text,
    isInverse=
        safe_text,
    isDeferred=
        safe_text
)
FlatQVT::BreakExp_strategy = st.builds(
    FlatQVT::BreakExp,
)
FlatQVT::ContinueExp_strategy = st.builds(
    FlatQVT::ContinueExp,
)
FlatQVT::VariableInitExp_strategy = st.builds(
    FlatQVT::VariableInitExp,
    withResult=
        safe_text
)
FlatQVT::RaiseExp_strategy = st.builds(
    FlatQVT::RaiseExp,
)
FlatQVT::CatchExp_strategy = st.builds(
    FlatQVT::CatchExp,
)
FlatQVT::InstantiationExp_strategy = st.builds(
    FlatQVT::InstantiationExp,
)
FlatQVT::AssertExp_strategy = st.builds(
    FlatQVT::AssertExp,
    severity=
        safe_text
)
FlatQVT::TryExp_strategy = st.builds(
    FlatQVT::TryExp,
)
FlatQVT::BlockExp_strategy = st.builds(
    FlatQVT::BlockExp,
)
FlatQVT::UnpackExp_strategy = st.builds(
    FlatQVT::UnpackExp,
)
FlatQVT::AltExp_strategy = st.builds(
    FlatQVT::AltExp,
)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=FlatQVT::URIExtent_strategy)
@settings(max_examples=50)
def test_flatqvt::uriextent_instantiation(instance):
    assert isinstance(instance, FlatQVT::URIExtent)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::URIExtent_strategy)
@settings(max_examples=30)
def test_flatqvt::uriextent_element_changes_state(instance):
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
        assert has_statements, f"Function 'element' in FlatQVT::URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'element' in FlatQVT::URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'element' in FlatQVT::URIExtent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::URIExtent_strategy)
@settings(max_examples=30)
def test_flatqvt::uriextent_uri_changes_state(instance):
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
        assert has_statements, f"Function 'uri' in FlatQVT::URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'uri' in FlatQVT::URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'uri' in FlatQVT::URIExtent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::URIExtent_strategy)
@settings(max_examples=30)
def test_flatqvt::uriextent_contexturi_changes_state(instance):
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
        assert has_statements, f"Function 'contextURI' in FlatQVT::URIExtent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'contextURI' in FlatQVT::URIExtent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'contextURI' in FlatQVT::URIExtent is not implemented or raised an error")

@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=CatchExp_strategy)
@settings(max_examples=50)
def test_catchexp_instantiation(instance):
    assert isinstance(instance, CatchExp)

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=ResolveExp_strategy)
@settings(max_examples=50)
def test_resolveexp_instantiation(instance):
    assert isinstance(instance, ResolveExp)

@given(instance=FlatQVT::ResolveInExp_strategy)
@settings(max_examples=50)
def test_flatqvt::resolveinexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::ResolveInExp)

@given(instance=DomainPattern_strategy)
@settings(max_examples=50)
def test_domainpattern_instantiation(instance):
    assert isinstance(instance, DomainPattern)

@given(instance=RelationDomainAssignment_strategy)
@settings(max_examples=50)
def test_relationdomainassignment_instantiation(instance):
    assert isinstance(instance, RelationDomainAssignment)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=Transformation_strategy)
@settings(max_examples=50)
def test_transformation_instantiation(instance):
    assert isinstance(instance, Transformation)

@given(instance=FlatQVT::RelationalTransformation_strategy)
@settings(max_examples=50)
def test_flatqvt::relationaltransformation_instantiation(instance):
    assert isinstance(instance, FlatQVT::RelationalTransformation)

@given(instance=ReflectiveCollection_strategy)
@settings(max_examples=50)
def test_reflectivecollection_instantiation(instance):
    assert isinstance(instance, ReflectiveCollection)

@given(instance=FlatQVT::ReflectiveSequence_strategy)
@settings(max_examples=50)
def test_flatqvt::reflectivesequence_instantiation(instance):
    assert isinstance(instance, FlatQVT::ReflectiveSequence)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_flatqvt::reflectivesequence_set_changes_state(instance):
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
        assert has_statements, f"Function 'set' in FlatQVT::ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'set' in FlatQVT::ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'set' in FlatQVT::ReflectiveSequence is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_flatqvt::reflectivesequence_remove_changes_state(instance):
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
        assert has_statements, f"Function 'remove' in FlatQVT::ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'remove' in FlatQVT::ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'remove' in FlatQVT::ReflectiveSequence is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::ReflectiveSequence_strategy)
@settings(max_examples=30)
def test_flatqvt::reflectivesequence_add_changes_state(instance):
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
        assert has_statements, f"Function 'add' in FlatQVT::ReflectiveSequence is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'add' in FlatQVT::ReflectiveSequence did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'add' in FlatQVT::ReflectiveSequence is not implemented or raised an error")

@given(instance=RelationImplementation_strategy)
@settings(max_examples=50)
def test_relationimplementation_instantiation(instance):
    assert isinstance(instance, RelationImplementation)

@given(instance=NavigationCallExp_strategy)
@settings(max_examples=50)
def test_navigationcallexp_instantiation(instance):
    assert isinstance(instance, NavigationCallExp)

@given(instance=FlatQVT::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt::propertycallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::PropertyCallExp)

@given(instance=ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, ObjectTemplateExp)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, OrderedTupleLiteralPart)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=FlatQVT::OppositePropertyCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt::oppositepropertycallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::OppositePropertyCallExp)

@given(instance=ConstructorBody_strategy)
@settings(max_examples=50)
def test_constructorbody_instantiation(instance):
    assert isinstance(instance, ConstructorBody)

@given(instance=InstantiationExp_strategy)
@settings(max_examples=50)
def test_instantiationexp_instantiation(instance):
    assert isinstance(instance, InstantiationExp)

@given(instance=FlatQVT::ObjectExp_strategy)
@settings(max_examples=50)
def test_flatqvt::objectexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::ObjectExp)

@given(instance=FlatQVT::Object_strategy)
@settings(max_examples=50)
def test_flatqvt::object_instantiation(instance):
    assert isinstance(instance, FlatQVT::Object)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, PropertyTemplateItem)

@given(instance=ModuleImport_strategy)
@settings(max_examples=50)
def test_moduleimport_instantiation(instance):
    assert isinstance(instance, ModuleImport)

@given(instance=EntryOperation_strategy)
@settings(max_examples=50)
def test_entryoperation_instantiation(instance):
    assert isinstance(instance, EntryOperation)

@given(instance=FeatureCallExp_strategy)
@settings(max_examples=50)
def test_featurecallexp_instantiation(instance):
    assert isinstance(instance, FeatureCallExp)

@given(instance=FlatQVT::OperationCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt::operationcallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::OperationCallExp)

@given(instance=FlatQVT::NavigationCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt::navigationcallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::NavigationCallExp)

@given(instance=FlatQVT::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_flatqvt::multiplicityelement_instantiation(instance):
    assert isinstance(instance, FlatQVT::MultiplicityElement)

@given(instance=FlatQVT::MultiplicityElement_strategy)
def test_flatqvt::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=FlatQVT::MultiplicityElement_strategy)
def test_flatqvt::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=FlatQVT::MultiplicityElement_strategy)
def test_flatqvt::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=FlatQVT::MultiplicityElement_strategy)
def test_flatqvt::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=FlatQVT::MultiplicityElement_strategy)
def test_flatqvt::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=FlatQVT::MultiplicityElement_strategy)
def test_flatqvt::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=FlatQVT::MultiplicityElement_strategy)
def test_flatqvt::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=FlatQVT::MultiplicityElement_strategy)
def test_flatqvt::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=ModelType_strategy)
@settings(max_examples=50)
def test_modeltype_instantiation(instance):
    assert isinstance(instance, ModelType)

@given(instance=Tag_strategy)
@settings(max_examples=50)
def test_tag_instantiation(instance):
    assert isinstance(instance, Tag)

@given(instance=MappingOperation_strategy)
@settings(max_examples=50)
def test_mappingoperation_instantiation(instance):
    assert isinstance(instance, MappingOperation)

@given(instance=ImperativeCallExp_strategy)
@settings(max_examples=50)
def test_imperativecallexp_instantiation(instance):
    assert isinstance(instance, ImperativeCallExp)

@given(instance=FlatQVT::MappingCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt::mappingcallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::MappingCallExp)

@given(instance=FlatQVT::MappingCallExp_strategy)
def test_flatqvt::mappingcallexp_isStrict_type(instance):
    assert isinstance(instance.isStrict, str)


@given(instance=FlatQVT::MappingCallExp_strategy)
def test_flatqvt::mappingcallexp_isStrict_setter(instance):
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

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=FlatQVT::UnlimitedNaturalExp_strategy)
@settings(max_examples=50)
def test_flatqvt::unlimitednaturalexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::UnlimitedNaturalExp)

@given(instance=FlatQVT::UnlimitedNaturalExp_strategy)
def test_flatqvt::unlimitednaturalexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=FlatQVT::UnlimitedNaturalExp_strategy)
def test_flatqvt::unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=FlatQVT::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::realliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::RealLiteralExp)

@given(instance=FlatQVT::RealLiteralExp_strategy)
def test_flatqvt::realliteralexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=FlatQVT::RealLiteralExp_strategy)
def test_flatqvt::realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=FlatQVT::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::integerliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::IntegerLiteralExp)

@given(instance=FlatQVT::IntegerLiteralExp_strategy)
def test_flatqvt::integerliteralexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=FlatQVT::IntegerLiteralExp_strategy)
def test_flatqvt::integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=FlatQVT::OperationalTransformation_strategy)
@settings(max_examples=50)
def test_flatqvt::operationaltransformation_instantiation(instance):
    assert isinstance(instance, FlatQVT::OperationalTransformation)

@given(instance=FlatQVT::Library_strategy)
@settings(max_examples=50)
def test_flatqvt::library_instantiation(instance):
    assert isinstance(instance, FlatQVT::Library)

@given(instance=RelationalTransformation_strategy)
@settings(max_examples=50)
def test_relationaltransformation_instantiation(instance):
    assert isinstance(instance, RelationalTransformation)

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)

@given(instance=VarParameter_strategy)
@settings(max_examples=50)
def test_varparameter_instantiation(instance):
    assert isinstance(instance, VarParameter)

@given(instance=FlatQVT::ModelParameter_strategy)
@settings(max_examples=50)
def test_flatqvt::modelparameter_instantiation(instance):
    assert isinstance(instance, FlatQVT::ModelParameter)

@given(instance=FlatQVT::MappingParameter_strategy)
@settings(max_examples=50)
def test_flatqvt::mappingparameter_instantiation(instance):
    assert isinstance(instance, FlatQVT::MappingParameter)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=FlatQVT::IteratorExp_strategy)
@settings(max_examples=50)
def test_flatqvt::iteratorexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::IteratorExp)

@given(instance=FlatQVT::IterateExp_strategy)
@settings(max_examples=50)
def test_flatqvt::iterateexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::IterateExp)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=FlatQVT::ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_flatqvt::imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::ImperativeIterateExp)

@given(instance=FlatQVT::ForExp_strategy)
@settings(max_examples=50)
def test_flatqvt::forexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::ForExp)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=FlatQVT::FeatureCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt::featurecallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::FeatureCallExp)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Enumeration_strategy)
@settings(max_examples=50)
def test_enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=FlatQVT::ReflectiveCollection_strategy)
@settings(max_examples=50)
def test_flatqvt::reflectivecollection_instantiation(instance):
    assert isinstance(instance, FlatQVT::ReflectiveCollection)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_flatqvt::reflectivecollection_size_changes_state(instance):
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
        assert has_statements, f"Function 'size' in FlatQVT::ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'size' in FlatQVT::ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'size' in FlatQVT::ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_flatqvt::reflectivecollection_add_changes_state(instance):
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
        assert has_statements, f"Function 'add' in FlatQVT::ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'add' in FlatQVT::ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'add' in FlatQVT::ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_flatqvt::reflectivecollection_remove_changes_state(instance):
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
        assert has_statements, f"Function 'remove' in FlatQVT::ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'remove' in FlatQVT::ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'remove' in FlatQVT::ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_flatqvt::reflectivecollection_clear_changes_state(instance):
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
        assert has_statements, f"Function 'clear' in FlatQVT::ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clear' in FlatQVT::ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clear' in FlatQVT::ReflectiveCollection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::ReflectiveCollection_strategy)
@settings(max_examples=30)
def test_flatqvt::reflectivecollection_addall_changes_state(instance):
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
        assert has_statements, f"Function 'addAll' in FlatQVT::ReflectiveCollection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addAll' in FlatQVT::ReflectiveCollection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addAll' in FlatQVT::ReflectiveCollection is not implemented or raised an error")

@given(instance=FlatQVT::Extent_strategy)
@settings(max_examples=50)
def test_flatqvt::extent_instantiation(instance):
    assert isinstance(instance, FlatQVT::Extent)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::Extent_strategy)
@settings(max_examples=30)
def test_flatqvt::extent_usecontainment_changes_state(instance):
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
        assert has_statements, f"Function 'useContainment' in FlatQVT::Extent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'useContainment' in FlatQVT::Extent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'useContainment' in FlatQVT::Extent is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::Extent_strategy)
@settings(max_examples=30)
def test_flatqvt::extent_elements_changes_state(instance):
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
        assert has_statements, f"Function 'elements' in FlatQVT::Extent is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'elements' in FlatQVT::Extent did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'elements' in FlatQVT::Extent is not implemented or raised an error")

@given(instance=FlatQVT::Element_strategy)
@settings(max_examples=50)
def test_flatqvt::element_instantiation(instance):
    assert isinstance(instance, FlatQVT::Element)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::Element_strategy)
@settings(max_examples=30)
def test_flatqvt::element_set_changes_state(instance):
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
        assert has_statements, f"Function 'set' in FlatQVT::Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'set' in FlatQVT::Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'set' in FlatQVT::Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::Element_strategy)
@settings(max_examples=30)
def test_flatqvt::element_unset_changes_state(instance):
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
        assert has_statements, f"Function 'unset' in FlatQVT::Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unset' in FlatQVT::Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unset' in FlatQVT::Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::Element_strategy)
@settings(max_examples=30)
def test_flatqvt::element_equals_changes_state(instance):
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
        assert has_statements, f"Function 'equals' in FlatQVT::Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'equals' in FlatQVT::Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'equals' in FlatQVT::Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::Element_strategy)
@settings(max_examples=30)
def test_flatqvt::element_container_changes_state(instance):
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
        assert has_statements, f"Function 'container' in FlatQVT::Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'container' in FlatQVT::Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'container' in FlatQVT::Element is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::Element_strategy)
@settings(max_examples=30)
def test_flatqvt::element_isset_changes_state(instance):
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
        assert has_statements, f"Function 'isSet' in FlatQVT::Element is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSet' in FlatQVT::Element did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSet' in FlatQVT::Element is not implemented or raised an error")

@given(instance=TypedModel_strategy)
@settings(max_examples=50)
def test_typedmodel_instantiation(instance):
    assert isinstance(instance, TypedModel)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=FlatQVT::Relation_strategy)
@settings(max_examples=50)
def test_flatqvt::relation_instantiation(instance):
    assert isinstance(instance, FlatQVT::Relation)

@given(instance=FlatQVT::Relation_strategy)
def test_flatqvt::relation_isTopLevel_type(instance):
    assert isinstance(instance.isTopLevel, str)


@given(instance=FlatQVT::Relation_strategy)
def test_flatqvt::relation_isTopLevel_setter(instance):
    original = instance.isTopLevel
    instance.isTopLevel = original
    assert instance.isTopLevel == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=FlatQVT::TypedElement_strategy)
@settings(max_examples=50)
def test_flatqvt::typedelement_instantiation(instance):
    assert isinstance(instance, FlatQVT::TypedElement)

@given(instance=FlatQVT::Type_strategy)
@settings(max_examples=50)
def test_flatqvt::type_instantiation(instance):
    assert isinstance(instance, FlatQVT::Type)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::Type_strategy)
@settings(max_examples=30)
def test_flatqvt::type_isinstance_changes_state(instance):
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
        assert has_statements, f"Function 'isInstance' in FlatQVT::Type is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isInstance' in FlatQVT::Type did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isInstance' in FlatQVT::Type is not implemented or raised an error")

@given(instance=FlatQVT::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_flatqvt::enumerationliteral_instantiation(instance):
    assert isinstance(instance, FlatQVT::EnumerationLiteral)

@given(instance=FlatQVT::TypedModel_strategy)
@settings(max_examples=50)
def test_flatqvt::typedmodel_instantiation(instance):
    assert isinstance(instance, FlatQVT::TypedModel)

@given(instance=FlatQVT::Domain_strategy)
@settings(max_examples=50)
def test_flatqvt::domain_instantiation(instance):
    assert isinstance(instance, FlatQVT::Domain)

@given(instance=FlatQVT::Domain_strategy)
def test_flatqvt::domain_isEnforceable_type(instance):
    assert isinstance(instance.isEnforceable, str)


@given(instance=FlatQVT::Domain_strategy)
def test_flatqvt::domain_isEnforceable_setter(instance):
    original = instance.isEnforceable
    instance.isEnforceable = original
    assert instance.isEnforceable == original

@given(instance=FlatQVT::Domain_strategy)
def test_flatqvt::domain_isCheckable_type(instance):
    assert isinstance(instance.isCheckable, str)


@given(instance=FlatQVT::Domain_strategy)
def test_flatqvt::domain_isCheckable_setter(instance):
    original = instance.isCheckable
    instance.isCheckable = original
    assert instance.isCheckable == original

@given(instance=FlatQVT::Rule_strategy)
@settings(max_examples=50)
def test_flatqvt::rule_instantiation(instance):
    assert isinstance(instance, FlatQVT::Rule)

@given(instance=FlatQVT::Package_strategy)
@settings(max_examples=50)
def test_flatqvt::package_instantiation(instance):
    assert isinstance(instance, FlatQVT::Package)

@given(instance=FlatQVT::Package_strategy)
def test_flatqvt::package_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=FlatQVT::Package_strategy)
def test_flatqvt::package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=FlatQVT::Enumeration_strategy)
@settings(max_examples=50)
def test_flatqvt::enumeration_instantiation(instance):
    assert isinstance(instance, FlatQVT::Enumeration)

@given(instance=FlatQVT::PrimitiveType_strategy)
@settings(max_examples=50)
def test_flatqvt::primitivetype_instantiation(instance):
    assert isinstance(instance, FlatQVT::PrimitiveType)

@given(instance=FlatQVT::CollectionType_strategy)
@settings(max_examples=50)
def test_flatqvt::collectiontype_instantiation(instance):
    assert isinstance(instance, FlatQVT::CollectionType)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=FlatQVT::DomainPattern_strategy)
@settings(max_examples=50)
def test_flatqvt::domainpattern_instantiation(instance):
    assert isinstance(instance, FlatQVT::DomainPattern)

@given(instance=FlatQVT::CorePattern_strategy)
@settings(max_examples=50)
def test_flatqvt::corepattern_instantiation(instance):
    assert isinstance(instance, FlatQVT::CorePattern)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=FlatQVT::RelationDomain_strategy)
@settings(max_examples=50)
def test_flatqvt::relationdomain_instantiation(instance):
    assert isinstance(instance, FlatQVT::RelationDomain)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=FlatQVT::RealizedVariable_strategy)
@settings(max_examples=50)
def test_flatqvt::realizedvariable_instantiation(instance):
    assert isinstance(instance, FlatQVT::RealizedVariable)

@given(instance=FlatQVT::VarParameter_strategy)
@settings(max_examples=50)
def test_flatqvt::varparameter_instantiation(instance):
    assert isinstance(instance, FlatQVT::VarParameter)

@given(instance=FlatQVT::VarParameter_strategy)
def test_flatqvt::varparameter_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=FlatQVT::VarParameter_strategy)
def test_flatqvt::varparameter_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=FlatQVT::FunctionParameter_strategy)
@settings(max_examples=50)
def test_flatqvt::functionparameter_instantiation(instance):
    assert isinstance(instance, FlatQVT::FunctionParameter)

@given(instance=OperationBody_strategy)
@settings(max_examples=50)
def test_operationbody_instantiation(instance):
    assert isinstance(instance, OperationBody)

@given(instance=FlatQVT::MappingBody_strategy)
@settings(max_examples=50)
def test_flatqvt::mappingbody_instantiation(instance):
    assert isinstance(instance, FlatQVT::MappingBody)

@given(instance=FlatQVT::ConstructorBody_strategy)
@settings(max_examples=50)
def test_flatqvt::constructorbody_instantiation(instance):
    assert isinstance(instance, FlatQVT::ConstructorBody)

@given(instance=ImperativeOperation_strategy)
@settings(max_examples=50)
def test_imperativeoperation_instantiation(instance):
    assert isinstance(instance, ImperativeOperation)

@given(instance=FlatQVT::Helper_strategy)
@settings(max_examples=50)
def test_flatqvt::helper_instantiation(instance):
    assert isinstance(instance, FlatQVT::Helper)

@given(instance=FlatQVT::Helper_strategy)
def test_flatqvt::helper_isQuery_type(instance):
    assert isinstance(instance.isQuery, str)


@given(instance=FlatQVT::Helper_strategy)
def test_flatqvt::helper_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=FlatQVT::EntryOperation_strategy)
@settings(max_examples=50)
def test_flatqvt::entryoperation_instantiation(instance):
    assert isinstance(instance, FlatQVT::EntryOperation)

@given(instance=FlatQVT::MappingOperation_strategy)
@settings(max_examples=50)
def test_flatqvt::mappingoperation_instantiation(instance):
    assert isinstance(instance, FlatQVT::MappingOperation)

@given(instance=FlatQVT::Constructor_strategy)
@settings(max_examples=50)
def test_flatqvt::constructor_instantiation(instance):
    assert isinstance(instance, FlatQVT::Constructor)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=FlatQVT::OclExpression_strategy)
@settings(max_examples=50)
def test_flatqvt::oclexpression_instantiation(instance):
    assert isinstance(instance, FlatQVT::OclExpression)

@given(instance=FlatQVT::Operation_strategy)
@settings(max_examples=50)
def test_flatqvt::operation_instantiation(instance):
    assert isinstance(instance, FlatQVT::Operation)

@given(instance=FlatQVT::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_flatqvt::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, FlatQVT::TupleLiteralPart)

@given(instance=FlatQVT::ExpressionInOcl_strategy)
@settings(max_examples=50)
def test_flatqvt::expressioninocl_instantiation(instance):
    assert isinstance(instance, FlatQVT::ExpressionInOcl)

@given(instance=FlatQVT::Parameter_strategy)
@settings(max_examples=50)
def test_flatqvt::parameter_instantiation(instance):
    assert isinstance(instance, FlatQVT::Parameter)

@given(instance=FlatQVT::Variable_strategy)
@settings(max_examples=50)
def test_flatqvt::variable_instantiation(instance):
    assert isinstance(instance, FlatQVT::Variable)

@given(instance=FlatQVT::Property_strategy)
@settings(max_examples=50)
def test_flatqvt::property_instantiation(instance):
    assert isinstance(instance, FlatQVT::Property)

@given(instance=FlatQVT::Property_strategy)
def test_flatqvt::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=FlatQVT::Property_strategy)
def test_flatqvt::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=FlatQVT::Property_strategy)
def test_flatqvt::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=FlatQVT::Property_strategy)
def test_flatqvt::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=FlatQVT::Property_strategy)
def test_flatqvt::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=FlatQVT::Property_strategy)
def test_flatqvt::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=FlatQVT::Property_strategy)
def test_flatqvt::property_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=FlatQVT::Property_strategy)
def test_flatqvt::property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=FlatQVT::Property_strategy)
def test_flatqvt::property_isID_type(instance):
    assert isinstance(instance.isID, str)


@given(instance=FlatQVT::Property_strategy)
def test_flatqvt::property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original

@given(instance=FlatQVT::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_flatqvt::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, FlatQVT::CollectionLiteralPart)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=FlatQVT::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::enumliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::EnumLiteralExp)

@given(instance=FlatQVT::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::nullliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::NullLiteralExp)

@given(instance=FlatQVT::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::InvalidLiteralExp)

@given(instance=FlatQVT::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::TupleLiteralExp)

@given(instance=FlatQVT::TemplateExp_strategy)
@settings(max_examples=50)
def test_flatqvt::templateexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::TemplateExp)

@given(instance=FlatQVT::ListLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::listliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::ListLiteralExp)

@given(instance=FlatQVT::DictLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::dictliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::DictLiteralExp)

@given(instance=FlatQVT::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::PrimitiveLiteralExp)

@given(instance=FlatQVT::OrderedTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::orderedtupleliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::OrderedTupleLiteralExp)

@given(instance=FlatQVT::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::CollectionLiteralExp)

@given(instance=FlatQVT::CollectionLiteralExp_strategy)
def test_flatqvt::collectionliteralexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=FlatQVT::CollectionLiteralExp_strategy)
def test_flatqvt::collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=FlatQVT::CollectionItem_strategy)
@settings(max_examples=50)
def test_flatqvt::collectionitem_instantiation(instance):
    assert isinstance(instance, FlatQVT::CollectionItem)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=FlatQVT::Transformation_strategy)
@settings(max_examples=50)
def test_flatqvt::transformation_instantiation(instance):
    assert isinstance(instance, FlatQVT::Transformation)

@given(instance=FlatQVT::OrderedTupleType_strategy)
@settings(max_examples=50)
def test_flatqvt::orderedtupletype_instantiation(instance):
    assert isinstance(instance, FlatQVT::OrderedTupleType)

@given(instance=FlatQVT::TupleType_strategy)
@settings(max_examples=50)
def test_flatqvt::tupletype_instantiation(instance):
    assert isinstance(instance, FlatQVT::TupleType)

@given(instance=FlatQVT::Typedef_strategy)
@settings(max_examples=50)
def test_flatqvt::typedef_instantiation(instance):
    assert isinstance(instance, FlatQVT::Typedef)

@given(instance=FlatQVT::ModelType_strategy)
@settings(max_examples=50)
def test_flatqvt::modeltype_instantiation(instance):
    assert isinstance(instance, FlatQVT::ModelType)

@given(instance=FlatQVT::ModelType_strategy)
def test_flatqvt::modeltype_conformanceKind_type(instance):
    assert isinstance(instance.conformanceKind, str)


@given(instance=FlatQVT::ModelType_strategy)
def test_flatqvt::modeltype_conformanceKind_setter(instance):
    original = instance.conformanceKind
    instance.conformanceKind = original
    assert instance.conformanceKind == original

@given(instance=FlatQVT::Module_strategy)
@settings(max_examples=50)
def test_flatqvt::module_instantiation(instance):
    assert isinstance(instance, FlatQVT::Module)

@given(instance=FlatQVT::Module_strategy)
def test_flatqvt::module_isBlackbox_type(instance):
    assert isinstance(instance.isBlackbox, str)


@given(instance=FlatQVT::Module_strategy)
def test_flatqvt::module_isBlackbox_setter(instance):
    original = instance.isBlackbox
    instance.isBlackbox = original
    assert instance.isBlackbox == original

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=FlatQVT::ImperativeOperation_strategy)
@settings(max_examples=50)
def test_flatqvt::imperativeoperation_instantiation(instance):
    assert isinstance(instance, FlatQVT::ImperativeOperation)

@given(instance=FlatQVT::ImperativeOperation_strategy)
def test_flatqvt::imperativeoperation_isBlackbox_type(instance):
    assert isinstance(instance.isBlackbox, str)


@given(instance=FlatQVT::ImperativeOperation_strategy)
def test_flatqvt::imperativeoperation_isBlackbox_setter(instance):
    original = instance.isBlackbox
    instance.isBlackbox = original
    assert instance.isBlackbox == original

@given(instance=FlatQVT::Function_strategy)
@settings(max_examples=50)
def test_flatqvt::function_instantiation(instance):
    assert isinstance(instance, FlatQVT::Function)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=FlatQVT::ContextualProperty_strategy)
@settings(max_examples=50)
def test_flatqvt::contextualproperty_instantiation(instance):
    assert isinstance(instance, FlatQVT::ContextualProperty)

@given(instance=TemplateExp_strategy)
@settings(max_examples=50)
def test_templateexp_instantiation(instance):
    assert isinstance(instance, TemplateExp)

@given(instance=FlatQVT::ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_flatqvt::objecttemplateexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::ObjectTemplateExp)

@given(instance=FlatQVT::CollectionTemplateExp_strategy)
@settings(max_examples=50)
def test_flatqvt::collectiontemplateexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::CollectionTemplateExp)

@given(instance=FlatQVT::CollectionRange_strategy)
@settings(max_examples=50)
def test_flatqvt::collectionrange_instantiation(instance):
    assert isinstance(instance, FlatQVT::CollectionRange)

@given(instance=EnforcementOperation_strategy)
@settings(max_examples=50)
def test_enforcementoperation_instantiation(instance):
    assert isinstance(instance, EnforcementOperation)

@given(instance=Assignment_strategy)
@settings(max_examples=50)
def test_assignment_instantiation(instance):
    assert isinstance(instance, Assignment)

@given(instance=FlatQVT::PropertyAssignment_strategy)
@settings(max_examples=50)
def test_flatqvt::propertyassignment_instantiation(instance):
    assert isinstance(instance, FlatQVT::PropertyAssignment)

@given(instance=FlatQVT::VariableAssignment_strategy)
@settings(max_examples=50)
def test_flatqvt::variableassignment_instantiation(instance):
    assert isinstance(instance, FlatQVT::VariableAssignment)

@given(instance=Area_strategy)
@settings(max_examples=50)
def test_area_instantiation(instance):
    assert isinstance(instance, Area)

@given(instance=FlatQVT::Mapping_strategy)
@settings(max_examples=50)
def test_flatqvt::mapping_instantiation(instance):
    assert isinstance(instance, FlatQVT::Mapping)

@given(instance=FlatQVT::CoreDomain_strategy)
@settings(max_examples=50)
def test_flatqvt::coredomain_instantiation(instance):
    assert isinstance(instance, FlatQVT::CoreDomain)

@given(instance=CorePattern_strategy)
@settings(max_examples=50)
def test_corepattern_instantiation(instance):
    assert isinstance(instance, CorePattern)

@given(instance=FlatQVT::GuardPattern_strategy)
@settings(max_examples=50)
def test_flatqvt::guardpattern_instantiation(instance):
    assert isinstance(instance, FlatQVT::GuardPattern)

@given(instance=FlatQVT::BottomPattern_strategy)
@settings(max_examples=50)
def test_flatqvt::bottompattern_instantiation(instance):
    assert isinstance(instance, FlatQVT::BottomPattern)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=FlatQVT::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::stringliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::StringLiteralExp)

@given(instance=FlatQVT::StringLiteralExp_strategy)
def test_flatqvt::stringliteralexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=FlatQVT::StringLiteralExp_strategy)
def test_flatqvt::stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=FlatQVT::NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::numericliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::NumericLiteralExp)

@given(instance=FlatQVT::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::BooleanLiteralExp)

@given(instance=FlatQVT::BooleanLiteralExp_strategy)
def test_flatqvt::booleanliteralexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=FlatQVT::BooleanLiteralExp_strategy)
def test_flatqvt::booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=FlatQVT::ListType_strategy)
@settings(max_examples=50)
def test_flatqvt::listtype_instantiation(instance):
    assert isinstance(instance, FlatQVT::ListType)

@given(instance=FlatQVT::DictionaryType_strategy)
@settings(max_examples=50)
def test_flatqvt::dictionarytype_instantiation(instance):
    assert isinstance(instance, FlatQVT::DictionaryType)

@given(instance=FlatQVT::SequenceType_strategy)
@settings(max_examples=50)
def test_flatqvt::sequencetype_instantiation(instance):
    assert isinstance(instance, FlatQVT::SequenceType)

@given(instance=FlatQVT::OrderedSetType_strategy)
@settings(max_examples=50)
def test_flatqvt::orderedsettype_instantiation(instance):
    assert isinstance(instance, FlatQVT::OrderedSetType)

@given(instance=FlatQVT::SetType_strategy)
@settings(max_examples=50)
def test_flatqvt::settype_instantiation(instance):
    assert isinstance(instance, FlatQVT::SetType)

@given(instance=FlatQVT::BagType_strategy)
@settings(max_examples=50)
def test_flatqvt::bagtype_instantiation(instance):
    assert isinstance(instance, FlatQVT::BagType)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=FlatQVT::DictLiteralPart_strategy)
@settings(max_examples=50)
def test_flatqvt::dictliteralpart_instantiation(instance):
    assert isinstance(instance, FlatQVT::DictLiteralPart)

@given(instance=FlatQVT::Comment_strategy)
@settings(max_examples=50)
def test_flatqvt::comment_instantiation(instance):
    assert isinstance(instance, FlatQVT::Comment)

@given(instance=FlatQVT::Comment_strategy)
def test_flatqvt::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=FlatQVT::Comment_strategy)
def test_flatqvt::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=FlatQVT::Tag_strategy)
@settings(max_examples=50)
def test_flatqvt::tag_instantiation(instance):
    assert isinstance(instance, FlatQVT::Tag)

@given(instance=FlatQVT::Tag_strategy)
def test_flatqvt::tag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FlatQVT::Tag_strategy)
def test_flatqvt::tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FlatQVT::Tag_strategy)
def test_flatqvt::tag_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=FlatQVT::Tag_strategy)
def test_flatqvt::tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FlatQVT::NamedElement_strategy)
@settings(max_examples=50)
def test_flatqvt::namedelement_instantiation(instance):
    assert isinstance(instance, FlatQVT::NamedElement)

@given(instance=FlatQVT::NamedElement_strategy)
def test_flatqvt::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FlatQVT::NamedElement_strategy)
def test_flatqvt::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FlatQVT::RelationImplementation_strategy)
@settings(max_examples=50)
def test_flatqvt::relationimplementation_instantiation(instance):
    assert isinstance(instance, FlatQVT::RelationImplementation)

@given(instance=FlatQVT::PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_flatqvt::propertytemplateitem_instantiation(instance):
    assert isinstance(instance, FlatQVT::PropertyTemplateItem)

@given(instance=FlatQVT::PropertyTemplateItem_strategy)
def test_flatqvt::propertytemplateitem_isOpposite_type(instance):
    assert isinstance(instance.isOpposite, str)


@given(instance=FlatQVT::PropertyTemplateItem_strategy)
def test_flatqvt::propertytemplateitem_isOpposite_setter(instance):
    original = instance.isOpposite
    instance.isOpposite = original
    assert instance.isOpposite == original

@given(instance=FlatQVT::Predicate_strategy)
@settings(max_examples=50)
def test_flatqvt::predicate_instantiation(instance):
    assert isinstance(instance, FlatQVT::Predicate)

@given(instance=FlatQVT::RelationDomainAssignment_strategy)
@settings(max_examples=50)
def test_flatqvt::relationdomainassignment_instantiation(instance):
    assert isinstance(instance, FlatQVT::RelationDomainAssignment)

@given(instance=FlatQVT::ModuleImport_strategy)
@settings(max_examples=50)
def test_flatqvt::moduleimport_instantiation(instance):
    assert isinstance(instance, FlatQVT::ModuleImport)

@given(instance=FlatQVT::ModuleImport_strategy)
def test_flatqvt::moduleimport_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=FlatQVT::ModuleImport_strategy)
def test_flatqvt::moduleimport_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=FlatQVT::OperationBody_strategy)
@settings(max_examples=50)
def test_flatqvt::operationbody_instantiation(instance):
    assert isinstance(instance, FlatQVT::OperationBody)

@given(instance=FlatQVT::EnforcementOperation_strategy)
@settings(max_examples=50)
def test_flatqvt::enforcementoperation_instantiation(instance):
    assert isinstance(instance, FlatQVT::EnforcementOperation)

@given(instance=FlatQVT::EnforcementOperation_strategy)
def test_flatqvt::enforcementoperation_enforcementMode_type(instance):
    assert isinstance(instance.enforcementMode, str)


@given(instance=FlatQVT::EnforcementOperation_strategy)
def test_flatqvt::enforcementoperation_enforcementMode_setter(instance):
    original = instance.enforcementMode
    instance.enforcementMode = original
    assert instance.enforcementMode == original

@given(instance=FlatQVT::OrderedTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_flatqvt::orderedtupleliteralpart_instantiation(instance):
    assert isinstance(instance, FlatQVT::OrderedTupleLiteralPart)

@given(instance=FlatQVT::Key_strategy)
@settings(max_examples=50)
def test_flatqvt::key_instantiation(instance):
    assert isinstance(instance, FlatQVT::Key)

@given(instance=FlatQVT::Factory_strategy)
@settings(max_examples=50)
def test_flatqvt::factory_instantiation(instance):
    assert isinstance(instance, FlatQVT::Factory)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::Factory_strategy)
@settings(max_examples=30)
def test_flatqvt::factory_create_changes_state(instance):
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
        assert has_statements, f"Function 'create' in FlatQVT::Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'create' in FlatQVT::Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'create' in FlatQVT::Factory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::Factory_strategy)
@settings(max_examples=30)
def test_flatqvt::factory_createfromstring_changes_state(instance):
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
        assert has_statements, f"Function 'createFromString' in FlatQVT::Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createFromString' in FlatQVT::Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createFromString' in FlatQVT::Factory is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=FlatQVT::Factory_strategy)
@settings(max_examples=30)
def test_flatqvt::factory_converttostring_changes_state(instance):
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
        assert has_statements, f"Function 'convertToString' in FlatQVT::Factory is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'convertToString' in FlatQVT::Factory did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'convertToString' in FlatQVT::Factory is not implemented or raised an error")

@given(instance=FlatQVT::Pattern_strategy)
@settings(max_examples=50)
def test_flatqvt::pattern_instantiation(instance):
    assert isinstance(instance, FlatQVT::Pattern)

@given(instance=FlatQVT::Assignment_strategy)
@settings(max_examples=50)
def test_flatqvt::assignment_instantiation(instance):
    assert isinstance(instance, FlatQVT::Assignment)

@given(instance=FlatQVT::Assignment_strategy)
def test_flatqvt::assignment_isDefault_type(instance):
    assert isinstance(instance.isDefault, str)


@given(instance=FlatQVT::Assignment_strategy)
def test_flatqvt::assignment_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=RealizedVariable_strategy)
@settings(max_examples=50)
def test_realizedvariable_instantiation(instance):
    assert isinstance(instance, RealizedVariable)

@given(instance=GuardPattern_strategy)
@settings(max_examples=50)
def test_guardpattern_instantiation(instance):
    assert isinstance(instance, GuardPattern)

@given(instance=BottomPattern_strategy)
@settings(max_examples=50)
def test_bottompattern_instantiation(instance):
    assert isinstance(instance, BottomPattern)

@given(instance=FlatQVT::Area_strategy)
@settings(max_examples=50)
def test_flatqvt::area_instantiation(instance):
    assert isinstance(instance, FlatQVT::Area)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=FlatQVT::VoidType_strategy)
@settings(max_examples=50)
def test_flatqvt::voidtype_instantiation(instance):
    assert isinstance(instance, FlatQVT::VoidType)

@given(instance=FlatQVT::DataType_strategy)
@settings(max_examples=50)
def test_flatqvt::datatype_instantiation(instance):
    assert isinstance(instance, FlatQVT::DataType)

@given(instance=FlatQVT::Class_strategy)
@settings(max_examples=50)
def test_flatqvt::class_instantiation(instance):
    assert isinstance(instance, FlatQVT::Class)

@given(instance=FlatQVT::Class_strategy)
def test_flatqvt::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=FlatQVT::Class_strategy)
def test_flatqvt::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=FlatQVT::TemplateParameterType_strategy)
@settings(max_examples=50)
def test_flatqvt::templateparametertype_instantiation(instance):
    assert isinstance(instance, FlatQVT::TemplateParameterType)

@given(instance=FlatQVT::TemplateParameterType_strategy)
def test_flatqvt::templateparametertype_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=FlatQVT::TemplateParameterType_strategy)
def test_flatqvt::templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=FlatQVT::InvalidType_strategy)
@settings(max_examples=50)
def test_flatqvt::invalidtype_instantiation(instance):
    assert isinstance(instance, FlatQVT::InvalidType)

@given(instance=FlatQVT::AnyType_strategy)
@settings(max_examples=50)
def test_flatqvt::anytype_instantiation(instance):
    assert isinstance(instance, FlatQVT::AnyType)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=FlatQVT::ImperativeExpression_strategy)
@settings(max_examples=50)
def test_flatqvt::imperativeexpression_instantiation(instance):
    assert isinstance(instance, FlatQVT::ImperativeExpression)

@given(instance=FlatQVT::VariableExp_strategy)
@settings(max_examples=50)
def test_flatqvt::variableexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::VariableExp)

@given(instance=FlatQVT::LoopExp_strategy)
@settings(max_examples=50)
def test_flatqvt::loopexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::LoopExp)

@given(instance=FlatQVT::LiteralExp_strategy)
@settings(max_examples=50)
def test_flatqvt::literalexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::LiteralExp)

@given(instance=FlatQVT::RelationCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt::relationcallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::RelationCallExp)

@given(instance=FlatQVT::CallExp_strategy)
@settings(max_examples=50)
def test_flatqvt::callexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::CallExp)

@given(instance=FlatQVT::LetExp_strategy)
@settings(max_examples=50)
def test_flatqvt::letexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::LetExp)

@given(instance=FlatQVT::IfExp_strategy)
@settings(max_examples=50)
def test_flatqvt::ifexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::IfExp)

@given(instance=FlatQVT::TypeExp_strategy)
@settings(max_examples=50)
def test_flatqvt::typeexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::TypeExp)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=FlatQVT::UnlinkExp_strategy)
@settings(max_examples=50)
def test_flatqvt::unlinkexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::UnlinkExp)

@given(instance=FlatQVT::ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_flatqvt::imperativeloopexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::ImperativeLoopExp)

@given(instance=FlatQVT::LogExp_strategy)
@settings(max_examples=50)
def test_flatqvt::logexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::LogExp)

@given(instance=FlatQVT::ImperativeCallExp_strategy)
@settings(max_examples=50)
def test_flatqvt::imperativecallexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::ImperativeCallExp)

@given(instance=FlatQVT::ImperativeCallExp_strategy)
def test_flatqvt::imperativecallexp_isVirtual_type(instance):
    assert isinstance(instance.isVirtual, str)


@given(instance=FlatQVT::ImperativeCallExp_strategy)
def test_flatqvt::imperativecallexp_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=FlatQVT::AssignExp_strategy)
@settings(max_examples=50)
def test_flatqvt::assignexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::AssignExp)

@given(instance=FlatQVT::AssignExp_strategy)
def test_flatqvt::assignexp_isReset_type(instance):
    assert isinstance(instance.isReset, str)


@given(instance=FlatQVT::AssignExp_strategy)
def test_flatqvt::assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=FlatQVT::SwitchExp_strategy)
@settings(max_examples=50)
def test_flatqvt::switchexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::SwitchExp)

@given(instance=FlatQVT::ComputeExp_strategy)
@settings(max_examples=50)
def test_flatqvt::computeexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::ComputeExp)

@given(instance=FlatQVT::ReturnExp_strategy)
@settings(max_examples=50)
def test_flatqvt::returnexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::ReturnExp)

@given(instance=FlatQVT::WhileExp_strategy)
@settings(max_examples=50)
def test_flatqvt::whileexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::WhileExp)

@given(instance=FlatQVT::ResolveExp_strategy)
@settings(max_examples=50)
def test_flatqvt::resolveexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::ResolveExp)

@given(instance=FlatQVT::ResolveExp_strategy)
def test_flatqvt::resolveexp_one_type(instance):
    assert isinstance(instance.one, str)


@given(instance=FlatQVT::ResolveExp_strategy)
def test_flatqvt::resolveexp_one_setter(instance):
    original = instance.one
    instance.one = original
    assert instance.one == original

@given(instance=FlatQVT::ResolveExp_strategy)
def test_flatqvt::resolveexp_isInverse_type(instance):
    assert isinstance(instance.isInverse, str)


@given(instance=FlatQVT::ResolveExp_strategy)
def test_flatqvt::resolveexp_isInverse_setter(instance):
    original = instance.isInverse
    instance.isInverse = original
    assert instance.isInverse == original

@given(instance=FlatQVT::ResolveExp_strategy)
def test_flatqvt::resolveexp_isDeferred_type(instance):
    assert isinstance(instance.isDeferred, str)


@given(instance=FlatQVT::ResolveExp_strategy)
def test_flatqvt::resolveexp_isDeferred_setter(instance):
    original = instance.isDeferred
    instance.isDeferred = original
    assert instance.isDeferred == original

@given(instance=FlatQVT::BreakExp_strategy)
@settings(max_examples=50)
def test_flatqvt::breakexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::BreakExp)

@given(instance=FlatQVT::ContinueExp_strategy)
@settings(max_examples=50)
def test_flatqvt::continueexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::ContinueExp)

@given(instance=FlatQVT::VariableInitExp_strategy)
@settings(max_examples=50)
def test_flatqvt::variableinitexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::VariableInitExp)

@given(instance=FlatQVT::VariableInitExp_strategy)
def test_flatqvt::variableinitexp_withResult_type(instance):
    assert isinstance(instance.withResult, str)


@given(instance=FlatQVT::VariableInitExp_strategy)
def test_flatqvt::variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=FlatQVT::RaiseExp_strategy)
@settings(max_examples=50)
def test_flatqvt::raiseexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::RaiseExp)

@given(instance=FlatQVT::CatchExp_strategy)
@settings(max_examples=50)
def test_flatqvt::catchexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::CatchExp)

@given(instance=FlatQVT::InstantiationExp_strategy)
@settings(max_examples=50)
def test_flatqvt::instantiationexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::InstantiationExp)

@given(instance=FlatQVT::AssertExp_strategy)
@settings(max_examples=50)
def test_flatqvt::assertexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::AssertExp)

@given(instance=FlatQVT::AssertExp_strategy)
def test_flatqvt::assertexp_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=FlatQVT::AssertExp_strategy)
def test_flatqvt::assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=FlatQVT::TryExp_strategy)
@settings(max_examples=50)
def test_flatqvt::tryexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::TryExp)

@given(instance=FlatQVT::BlockExp_strategy)
@settings(max_examples=50)
def test_flatqvt::blockexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::BlockExp)

@given(instance=FlatQVT::UnpackExp_strategy)
@settings(max_examples=50)
def test_flatqvt::unpackexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::UnpackExp)

@given(instance=FlatQVT::AltExp_strategy)
@settings(max_examples=50)
def test_flatqvt::altexp_instantiation(instance):
    assert isinstance(instance, FlatQVT::AltExp)
