import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CollectionType,
    AltExp,
    CallExp,
    ImperativeExpression,
    imperativeocl::VariableInitExp,
    imperativeocl::SwitchExp,
    imperativeocl::BlockExp,
    imperativeocl::ComputeExp,
    imperativeocl::AssignExp,
    ImperativeLoopExp,
    imperativeocl::ImperativeIterateExp,
    Property,
    ObjectTemplateExp,
    Element,
    qvttemplate::PropertyTemplateItem,
    Class,
    PropertyTemplateItem,
    TemplateExp,
    qvttemplate::CollectionTemplateExp,
    qvttemplate::ObjectTemplateExp,
    OclExpression,
    Variable,
    LiteralExp,
    qvttemplate::TemplateExp,
    essentialocl::SetType,
    essentialocl::SequenceType,
    essentialocl::OrderedSetType,
    essentialocl::EnumLiteralExp,
    essentialocl::BagType,
    TupleLiteralExp,
    essentialocl::FeaturePropertyCall,
    essentialocl::InvalidLiteralExp,
    essentialocl::OpaqueExpression,
    OpaqueExpression,
    essentialocl::ExpressionInOcl,
    essentialocl::NullLiteralExp,
    TupleLiteralPart,
    essentialocl::TupleLiteralExp,
    CollectionLiteralExp,
    CollectionLiteralPart,
    essentialocl::CollectionItem,
    essentialocl::CollectionRange,
    essentialocl::CollectionLiteralExp,
    essentialocl::PrimitiveLiteralExp,
    essentialocl::LiteralExp,
    essentialocl::LoopExp,
    essentialocl::TypeExp,
    essentialocl::VariableExp,
    FeaturePropertyCall,
    essentialocl::OperationCallExp,
    essentialocl::PropertyCallExp,
    ComputeExp,
    LetExp,
    essentialocl::CallExp,
    PrimitiveLiteralExp,
    essentialocl::StringLiteralExp,
    essentialocl::NumericLiteralExp,
    essentialocl::BooleanLiteralExp,
    essentialocl::LetExp,
    essentialocl::IfExp,
    NumericLiteralExp,
    essentialocl::RealLiteralExp,
    essentialocl::IntegerLiteralExp,
    essentialocl::UnlimitedNaturalExp,
    TryExp,
    RelationalTransformation,
    qvtrelation::Key,
    qvtrelation::RelationImplementation,
    DomainPattern,
    qvtbase::Pattern,
    RelationImplementation,
    Key,
    qvtbase::Predicate,
    Predicate,
    qvtcore::EnforcementOperation,
    TypedModel,
    qvtcore::Assignment,
    BottomPattern,
    Pattern,
    qvtrelation::DomainPattern,
    qvtcore::CorePattern,
    Domain,
    qvtrelation::RelationDomain,
    qvtcore::RealizedVariable,
    Mapping,
    Rule,
    qvtrelation::Relation,
    EnforcementOperation,
    RealizedVariable,
    Assignment,
    Area,
    qvtcore::Mapping,
    qvtcore::CoreDomain,
    CorePattern,
    qvtcore::GuardPattern,
    qvtcore::BottomPattern,
    qvtoperational::ModuleImport,
    GuardPattern,
    qvtcore::Area,
    ConstructorBody,
    InstantiationExp,
    qvtoperational::ObjectExp,
    qvtoperational::OperationBody,
    OperationCallExp,
    qvtoperational::ImperativeCallExp,
    ModelType,
    ModuleImport,
    URIExtent,
    qvtoperational::ModelType,
    EntryOperation,
    ModelParameter,
    qvtoperational::ContextualProperty,
    ImperativeCallExp,
    qvtoperational::MappingCallExp,
    RelationDomain,
    VarParameter,
    qvtoperational::ModelParameter,
    qvtoperational::MappingParameter,
    Relation,
    MappingOperation,
    ResolveExp,
    qvtoperational::ResolveInExp,
    qvtoperational::ResolveExp,
    ImperativeOperation,
    qvtoperational::Constructor,
    qvtoperational::EntryOperation,
    qvtoperational::Helper,
    OperationBody,
    qvtoperational::ConstructorBody,
    qvtoperational::MappingBody,
    emof::Comment,
    Extent,
    emof::URIExtent,
    Parameter,
    qvtoperational::VarParameter,
    qvtbase::FunctionParameter,
    Enumeration,
    Package,
    qvtoperational::Module,
    qvtbase::Transformation,
    NamedElement,
    emof::EnumerationLiteral,
    qvtbase::TypedModel,
    qvtbase::Domain,
    qvtbase::Rule,
    emof::Type,
    emof::TypedElement,
    emof::Package,
    emof::MultiplicityElement,
    imperativeocl::ListType,
    TypedElement,
    essentialocl::Variable,
    essentialocl::TupleLiteralPart,
    essentialocl::CollectionLiteralPart,
    essentialocl::OclExpression,
    MultiplicityElement,
    emof::Parameter,
    emof::Property,
    emof::Operation,
    emof::Object,
    emof::NamedElement,
    EnumerationLiteral,
    DataType,
    essentialocl::CollectionType,
    emof::PrimitiveType,
    essentialocl::TupleType,
    emof::Enumeration,
    Module,
    qvtoperational::Library,
    qvtoperational::OperationalTransformation,
    Transformation,
    qvtrelation::RelationalTransformation,
    emof::Tag,
    Comment,
    Tag,
    Object,
    emof::Extent,
    emof::Element,
    Operation,
    qvtbase::Function,
    qvtoperational::ImperativeOperation,
    qvtoperational::MappingOperation,
    imperativeocl::AnonymousTupleLiteralPart,
    AnonymousTupleLiteralPart,
    imperativeocl::AnonymousTupleLiteralExp,
    imperativeocl::AnonymousTupleType,
    imperativeocl::UnpackExp,
    imperativeocl::ImperativeExpression,
    imperativeocl::CollectorExp,
    LoopExp,
    essentialocl::IteratorExp,
    essentialocl::IterateExp,
    imperativeocl::ImperativeLoopExp,
    LogExp,
    imperativeocl::AssertExp,
    imperativeocl::TupleExp,
    imperativeocl::ForExp,
    imperativeocl::ContinueExp,
    imperativeocl::LogExp,
    imperativeocl::DictLiteralPart,
    DictLiteralPart,
    imperativeocl::DictLiteralExp,
    imperativeocl::DictionaryType,
    imperativeocl::InstantiationExp,
    imperativeocl::Typedef,
    imperativeocl::WhileExp,
    imperativeocl::RaiseExp,
    Type,
    emof::Class,
    imperativeocl::TemplateParameterType,
    essentialocl::AnyType,
    essentialocl::InvalidType,
    emof::DataType,
    essentialocl::VoidType,
    imperativeocl::TryExp,
    imperativeocl::BreakExp,
    imperativeocl::ReturnExp,
    imperativeocl::UnlinkExp,
    imperativeocl::AltExp,
    CollectionKind,
    EnforcementMode,
    ImportKind,
    DirectionKind,
    SeverityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_altexp_is_not_abstract():
    assert not inspect.isabstract(AltExp)


def test_altexp_constructor_exists():
    assert callable(AltExp.__init__)


def test_altexp_constructor_args():
    sig = inspect.signature(AltExp.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::variableinitexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::VariableInitExp)


def test_imperativeocl::variableinitexp_constructor_exists():
    assert callable(imperativeocl::VariableInitExp.__init__)


def test_imperativeocl::variableinitexp_constructor_args():
    sig = inspect.signature(imperativeocl::VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_imperativeocl::variableinitexp_has_withResult():
    assert hasattr(imperativeocl::VariableInitExp, "withResult")
    descriptor = None
    for klass in imperativeocl::VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::switchexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::SwitchExp)


def test_imperativeocl::switchexp_constructor_exists():
    assert callable(imperativeocl::SwitchExp.__init__)


def test_imperativeocl::switchexp_constructor_args():
    sig = inspect.signature(imperativeocl::SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::blockexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::BlockExp)


def test_imperativeocl::blockexp_constructor_exists():
    assert callable(imperativeocl::BlockExp.__init__)


def test_imperativeocl::blockexp_constructor_args():
    sig = inspect.signature(imperativeocl::BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::computeexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ComputeExp)


def test_imperativeocl::computeexp_constructor_exists():
    assert callable(imperativeocl::ComputeExp.__init__)


def test_imperativeocl::computeexp_constructor_args():
    sig = inspect.signature(imperativeocl::ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::assignexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::AssignExp)


def test_imperativeocl::assignexp_constructor_exists():
    assert callable(imperativeocl::AssignExp.__init__)


def test_imperativeocl::assignexp_constructor_args():
    sig = inspect.signature(imperativeocl::AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_imperativeocl::assignexp_has_isReset():
    assert hasattr(imperativeocl::AssignExp, "isReset")
    descriptor = None
    for klass in imperativeocl::AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ImperativeIterateExp)


def test_imperativeocl::imperativeiterateexp_constructor_exists():
    assert callable(imperativeocl::ImperativeIterateExp.__init__)


def test_imperativeocl::imperativeiterateexp_constructor_args():
    sig = inspect.signature(imperativeocl::ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(ObjectTemplateExp)


def test_objecttemplateexp_constructor_exists():
    assert callable(ObjectTemplateExp.__init__)


def test_objecttemplateexp_constructor_args():
    sig = inspect.signature(ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate::propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(qvttemplate::PropertyTemplateItem)


def test_qvttemplate::propertytemplateitem_constructor_exists():
    assert callable(qvttemplate::PropertyTemplateItem.__init__)


def test_qvttemplate::propertytemplateitem_constructor_args():
    sig = inspect.signature(qvttemplate::PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(PropertyTemplateItem)


def test_propertytemplateitem_constructor_exists():
    assert callable(PropertyTemplateItem.__init__)


def test_propertytemplateitem_constructor_args():
    sig = inspect.signature(PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_templateexp_is_not_abstract():
    assert not inspect.isabstract(TemplateExp)


def test_templateexp_constructor_exists():
    assert callable(TemplateExp.__init__)


def test_templateexp_constructor_args():
    sig = inspect.signature(TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate::collectiontemplateexp_is_not_abstract():
    assert not inspect.isabstract(qvttemplate::CollectionTemplateExp)


def test_qvttemplate::collectiontemplateexp_constructor_exists():
    assert callable(qvttemplate::CollectionTemplateExp.__init__)


def test_qvttemplate::collectiontemplateexp_constructor_args():
    sig = inspect.signature(qvttemplate::CollectionTemplateExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_qvttemplate::collectiontemplateexp_has_kind():
    assert hasattr(qvttemplate::CollectionTemplateExp, "kind")
    descriptor = None
    for klass in qvttemplate::CollectionTemplateExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_qvttemplate::objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(qvttemplate::ObjectTemplateExp)


def test_qvttemplate::objecttemplateexp_constructor_exists():
    assert callable(qvttemplate::ObjectTemplateExp.__init__)


def test_qvttemplate::objecttemplateexp_constructor_args():
    sig = inspect.signature(qvttemplate::ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_qvttemplate::templateexp_is_not_abstract():
    assert not inspect.isabstract(qvttemplate::TemplateExp)


def test_qvttemplate::templateexp_constructor_exists():
    assert callable(qvttemplate::TemplateExp.__init__)


def test_qvttemplate::templateexp_constructor_args():
    sig = inspect.signature(qvttemplate::TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::settype_is_not_abstract():
    assert not inspect.isabstract(essentialocl::SetType)


def test_essentialocl::settype_constructor_exists():
    assert callable(essentialocl::SetType.__init__)


def test_essentialocl::settype_constructor_args():
    sig = inspect.signature(essentialocl::SetType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(essentialocl::SequenceType)


def test_essentialocl::sequencetype_constructor_exists():
    assert callable(essentialocl::SequenceType.__init__)


def test_essentialocl::sequencetype_constructor_args():
    sig = inspect.signature(essentialocl::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(essentialocl::OrderedSetType)


def test_essentialocl::orderedsettype_constructor_exists():
    assert callable(essentialocl::OrderedSetType.__init__)


def test_essentialocl::orderedsettype_constructor_args():
    sig = inspect.signature(essentialocl::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::EnumLiteralExp)


def test_essentialocl::enumliteralexp_constructor_exists():
    assert callable(essentialocl::EnumLiteralExp.__init__)


def test_essentialocl::enumliteralexp_constructor_args():
    sig = inspect.signature(essentialocl::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(essentialocl::BagType)


def test_essentialocl::bagtype_constructor_exists():
    assert callable(essentialocl::BagType.__init__)


def test_essentialocl::bagtype_constructor_args():
    sig = inspect.signature(essentialocl::BagType.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralExp)


def test_tupleliteralexp_constructor_exists():
    assert callable(TupleLiteralExp.__init__)


def test_tupleliteralexp_constructor_args():
    sig = inspect.signature(TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(essentialocl::FeaturePropertyCall)


def test_essentialocl::featurepropertycall_constructor_exists():
    assert callable(essentialocl::FeaturePropertyCall.__init__)


def test_essentialocl::featurepropertycall_constructor_args():
    sig = inspect.signature(essentialocl::FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::InvalidLiteralExp)


def test_essentialocl::invalidliteralexp_constructor_exists():
    assert callable(essentialocl::InvalidLiteralExp.__init__)


def test_essentialocl::invalidliteralexp_constructor_args():
    sig = inspect.signature(essentialocl::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(essentialocl::OpaqueExpression)


def test_essentialocl::opaqueexpression_constructor_exists():
    assert callable(essentialocl::OpaqueExpression.__init__)


def test_essentialocl::opaqueexpression_constructor_args():
    sig = inspect.signature(essentialocl::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::expressioninocl_is_not_abstract():
    assert not inspect.isabstract(essentialocl::ExpressionInOcl)


def test_essentialocl::expressioninocl_constructor_exists():
    assert callable(essentialocl::ExpressionInOcl.__init__)


def test_essentialocl::expressioninocl_constructor_args():
    sig = inspect.signature(essentialocl::ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::NullLiteralExp)


def test_essentialocl::nullliteralexp_constructor_exists():
    assert callable(essentialocl::NullLiteralExp.__init__)


def test_essentialocl::nullliteralexp_constructor_args():
    sig = inspect.signature(essentialocl::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::TupleLiteralExp)


def test_essentialocl::tupleliteralexp_constructor_exists():
    assert callable(essentialocl::TupleLiteralExp.__init__)


def test_essentialocl::tupleliteralexp_constructor_args():
    sig = inspect.signature(essentialocl::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectionitem_is_not_abstract():
    assert not inspect.isabstract(essentialocl::CollectionItem)


def test_essentialocl::collectionitem_constructor_exists():
    assert callable(essentialocl::CollectionItem.__init__)


def test_essentialocl::collectionitem_constructor_args():
    sig = inspect.signature(essentialocl::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectionrange_is_not_abstract():
    assert not inspect.isabstract(essentialocl::CollectionRange)


def test_essentialocl::collectionrange_constructor_exists():
    assert callable(essentialocl::CollectionRange.__init__)


def test_essentialocl::collectionrange_constructor_args():
    sig = inspect.signature(essentialocl::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::CollectionLiteralExp)


def test_essentialocl::collectionliteralexp_constructor_exists():
    assert callable(essentialocl::CollectionLiteralExp.__init__)


def test_essentialocl::collectionliteralexp_constructor_args():
    sig = inspect.signature(essentialocl::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_essentialocl::collectionliteralexp_has_kind():
    assert hasattr(essentialocl::CollectionLiteralExp, "kind")
    descriptor = None
    for klass in essentialocl::CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::PrimitiveLiteralExp)


def test_essentialocl::primitiveliteralexp_constructor_exists():
    assert callable(essentialocl::PrimitiveLiteralExp.__init__)


def test_essentialocl::primitiveliteralexp_constructor_args():
    sig = inspect.signature(essentialocl::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::literalexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::LiteralExp)


def test_essentialocl::literalexp_constructor_exists():
    assert callable(essentialocl::LiteralExp.__init__)


def test_essentialocl::literalexp_constructor_args():
    sig = inspect.signature(essentialocl::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::LoopExp)


def test_essentialocl::loopexp_constructor_exists():
    assert callable(essentialocl::LoopExp.__init__)


def test_essentialocl::loopexp_constructor_args():
    sig = inspect.signature(essentialocl::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::typeexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::TypeExp)


def test_essentialocl::typeexp_constructor_exists():
    assert callable(essentialocl::TypeExp.__init__)


def test_essentialocl::typeexp_constructor_args():
    sig = inspect.signature(essentialocl::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::VariableExp)


def test_essentialocl::variableexp_constructor_exists():
    assert callable(essentialocl::VariableExp.__init__)


def test_essentialocl::variableexp_constructor_args():
    sig = inspect.signature(essentialocl::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(FeaturePropertyCall)


def test_featurepropertycall_constructor_exists():
    assert callable(FeaturePropertyCall.__init__)


def test_featurepropertycall_constructor_args():
    sig = inspect.signature(FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::OperationCallExp)


def test_essentialocl::operationcallexp_constructor_exists():
    assert callable(essentialocl::OperationCallExp.__init__)


def test_essentialocl::operationcallexp_constructor_args():
    sig = inspect.signature(essentialocl::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::PropertyCallExp)


def test_essentialocl::propertycallexp_constructor_exists():
    assert callable(essentialocl::PropertyCallExp.__init__)


def test_essentialocl::propertycallexp_constructor_args():
    sig = inspect.signature(essentialocl::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_computeexp_is_not_abstract():
    assert not inspect.isabstract(ComputeExp)


def test_computeexp_constructor_exists():
    assert callable(ComputeExp.__init__)


def test_computeexp_constructor_args():
    sig = inspect.signature(ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::callexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::CallExp)


def test_essentialocl::callexp_constructor_exists():
    assert callable(essentialocl::CallExp.__init__)


def test_essentialocl::callexp_constructor_args():
    sig = inspect.signature(essentialocl::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::StringLiteralExp)


def test_essentialocl::stringliteralexp_constructor_exists():
    assert callable(essentialocl::StringLiteralExp.__init__)


def test_essentialocl::stringliteralexp_constructor_args():
    sig = inspect.signature(essentialocl::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_essentialocl::stringliteralexp_has_stringSymbol():
    assert hasattr(essentialocl::StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in essentialocl::StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::NumericLiteralExp)


def test_essentialocl::numericliteralexp_constructor_exists():
    assert callable(essentialocl::NumericLiteralExp.__init__)


def test_essentialocl::numericliteralexp_constructor_args():
    sig = inspect.signature(essentialocl::NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::BooleanLiteralExp)


def test_essentialocl::booleanliteralexp_constructor_exists():
    assert callable(essentialocl::BooleanLiteralExp.__init__)


def test_essentialocl::booleanliteralexp_constructor_args():
    sig = inspect.signature(essentialocl::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_essentialocl::booleanliteralexp_has_booleanSymbol():
    assert hasattr(essentialocl::BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in essentialocl::BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::letexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::LetExp)


def test_essentialocl::letexp_constructor_exists():
    assert callable(essentialocl::LetExp.__init__)


def test_essentialocl::letexp_constructor_args():
    sig = inspect.signature(essentialocl::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::IfExp)


def test_essentialocl::ifexp_constructor_exists():
    assert callable(essentialocl::IfExp.__init__)


def test_essentialocl::ifexp_constructor_args():
    sig = inspect.signature(essentialocl::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::RealLiteralExp)


def test_essentialocl::realliteralexp_constructor_exists():
    assert callable(essentialocl::RealLiteralExp.__init__)


def test_essentialocl::realliteralexp_constructor_args():
    sig = inspect.signature(essentialocl::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_essentialocl::realliteralexp_has_realSymbol():
    assert hasattr(essentialocl::RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in essentialocl::RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::IntegerLiteralExp)


def test_essentialocl::integerliteralexp_constructor_exists():
    assert callable(essentialocl::IntegerLiteralExp.__init__)


def test_essentialocl::integerliteralexp_constructor_args():
    sig = inspect.signature(essentialocl::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_essentialocl::integerliteralexp_has_integerSymbol():
    assert hasattr(essentialocl::IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in essentialocl::IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::UnlimitedNaturalExp)


def test_essentialocl::unlimitednaturalexp_constructor_exists():
    assert callable(essentialocl::UnlimitedNaturalExp.__init__)


def test_essentialocl::unlimitednaturalexp_constructor_args():
    sig = inspect.signature(essentialocl::UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_essentialocl::unlimitednaturalexp_has_symbol():
    assert hasattr(essentialocl::UnlimitedNaturalExp, "symbol")
    descriptor = None
    for klass in essentialocl::UnlimitedNaturalExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_tryexp_is_not_abstract():
    assert not inspect.isabstract(TryExp)


def test_tryexp_constructor_exists():
    assert callable(TryExp.__init__)


def test_tryexp_constructor_args():
    sig = inspect.signature(TryExp.__init__)
    params = list(sig.parameters.keys())



def test_relationaltransformation_is_not_abstract():
    assert not inspect.isabstract(RelationalTransformation)


def test_relationaltransformation_constructor_exists():
    assert callable(RelationalTransformation.__init__)


def test_relationaltransformation_constructor_args():
    sig = inspect.signature(RelationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::key_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::Key)


def test_qvtrelation::key_constructor_exists():
    assert callable(qvtrelation::Key.__init__)


def test_qvtrelation::key_constructor_args():
    sig = inspect.signature(qvtrelation::Key.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::relationimplementation_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::RelationImplementation)


def test_qvtrelation::relationimplementation_constructor_exists():
    assert callable(qvtrelation::RelationImplementation.__init__)


def test_qvtrelation::relationimplementation_constructor_args():
    sig = inspect.signature(qvtrelation::RelationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_domainpattern_is_not_abstract():
    assert not inspect.isabstract(DomainPattern)


def test_domainpattern_constructor_exists():
    assert callable(DomainPattern.__init__)


def test_domainpattern_constructor_args():
    sig = inspect.signature(DomainPattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase::pattern_is_not_abstract():
    assert not inspect.isabstract(qvtbase::Pattern)


def test_qvtbase::pattern_constructor_exists():
    assert callable(qvtbase::Pattern.__init__)


def test_qvtbase::pattern_constructor_args():
    sig = inspect.signature(qvtbase::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_relationimplementation_is_not_abstract():
    assert not inspect.isabstract(RelationImplementation)


def test_relationimplementation_constructor_exists():
    assert callable(RelationImplementation.__init__)


def test_relationimplementation_constructor_args():
    sig = inspect.signature(RelationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase::predicate_is_not_abstract():
    assert not inspect.isabstract(qvtbase::Predicate)


def test_qvtbase::predicate_constructor_exists():
    assert callable(qvtbase::Predicate.__init__)


def test_qvtbase::predicate_constructor_args():
    sig = inspect.signature(qvtbase::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::enforcementoperation_is_not_abstract():
    assert not inspect.isabstract(qvtcore::EnforcementOperation)


def test_qvtcore::enforcementoperation_constructor_exists():
    assert callable(qvtcore::EnforcementOperation.__init__)


def test_qvtcore::enforcementoperation_constructor_args():
    sig = inspect.signature(qvtcore::EnforcementOperation.__init__)
    params = list(sig.parameters.keys())
    assert "enforcementMode" in params, "Missing parameter 'enforcementMode'"

def test_qvtcore::enforcementoperation_has_enforcementMode():
    assert hasattr(qvtcore::EnforcementOperation, "enforcementMode")
    descriptor = None
    for klass in qvtcore::EnforcementOperation.__mro__:
        if "enforcementMode" in klass.__dict__:
            descriptor = klass.__dict__["enforcementMode"]
            break
    assert isinstance(descriptor, property)



def test_typedmodel_is_not_abstract():
    assert not inspect.isabstract(TypedModel)


def test_typedmodel_constructor_exists():
    assert callable(TypedModel.__init__)


def test_typedmodel_constructor_args():
    sig = inspect.signature(TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::assignment_is_not_abstract():
    assert not inspect.isabstract(qvtcore::Assignment)


def test_qvtcore::assignment_constructor_exists():
    assert callable(qvtcore::Assignment.__init__)


def test_qvtcore::assignment_constructor_args():
    sig = inspect.signature(qvtcore::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_qvtcore::assignment_has_isDefault():
    assert hasattr(qvtcore::Assignment, "isDefault")
    descriptor = None
    for klass in qvtcore::Assignment.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_bottompattern_is_not_abstract():
    assert not inspect.isabstract(BottomPattern)


def test_bottompattern_constructor_exists():
    assert callable(BottomPattern.__init__)


def test_bottompattern_constructor_args():
    sig = inspect.signature(BottomPattern.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::domainpattern_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::DomainPattern)


def test_qvtrelation::domainpattern_constructor_exists():
    assert callable(qvtrelation::DomainPattern.__init__)


def test_qvtrelation::domainpattern_constructor_args():
    sig = inspect.signature(qvtrelation::DomainPattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::corepattern_is_not_abstract():
    assert not inspect.isabstract(qvtcore::CorePattern)


def test_qvtcore::corepattern_constructor_exists():
    assert callable(qvtcore::CorePattern.__init__)


def test_qvtcore::corepattern_constructor_args():
    sig = inspect.signature(qvtcore::CorePattern.__init__)
    params = list(sig.parameters.keys())



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::relationdomain_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::RelationDomain)


def test_qvtrelation::relationdomain_constructor_exists():
    assert callable(qvtrelation::RelationDomain.__init__)


def test_qvtrelation::relationdomain_constructor_args():
    sig = inspect.signature(qvtrelation::RelationDomain.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::realizedvariable_is_not_abstract():
    assert not inspect.isabstract(qvtcore::RealizedVariable)


def test_qvtcore::realizedvariable_constructor_exists():
    assert callable(qvtcore::RealizedVariable.__init__)


def test_qvtcore::realizedvariable_constructor_args():
    sig = inspect.signature(qvtcore::RealizedVariable.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::relation_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::Relation)


def test_qvtrelation::relation_constructor_exists():
    assert callable(qvtrelation::Relation.__init__)


def test_qvtrelation::relation_constructor_args():
    sig = inspect.signature(qvtrelation::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopLevel" in params, "Missing parameter 'isTopLevel'"

def test_qvtrelation::relation_has_isTopLevel():
    assert hasattr(qvtrelation::Relation, "isTopLevel")
    descriptor = None
    for klass in qvtrelation::Relation.__mro__:
        if "isTopLevel" in klass.__dict__:
            descriptor = klass.__dict__["isTopLevel"]
            break
    assert isinstance(descriptor, property)



def test_enforcementoperation_is_not_abstract():
    assert not inspect.isabstract(EnforcementOperation)


def test_enforcementoperation_constructor_exists():
    assert callable(EnforcementOperation.__init__)


def test_enforcementoperation_constructor_args():
    sig = inspect.signature(EnforcementOperation.__init__)
    params = list(sig.parameters.keys())



def test_realizedvariable_is_not_abstract():
    assert not inspect.isabstract(RealizedVariable)


def test_realizedvariable_constructor_exists():
    assert callable(RealizedVariable.__init__)


def test_realizedvariable_constructor_args():
    sig = inspect.signature(RealizedVariable.__init__)
    params = list(sig.parameters.keys())



def test_assignment_is_not_abstract():
    assert not inspect.isabstract(Assignment)


def test_assignment_constructor_exists():
    assert callable(Assignment.__init__)


def test_assignment_constructor_args():
    sig = inspect.signature(Assignment.__init__)
    params = list(sig.parameters.keys())



def test_area_is_not_abstract():
    assert not inspect.isabstract(Area)


def test_area_constructor_exists():
    assert callable(Area.__init__)


def test_area_constructor_args():
    sig = inspect.signature(Area.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::mapping_is_not_abstract():
    assert not inspect.isabstract(qvtcore::Mapping)


def test_qvtcore::mapping_constructor_exists():
    assert callable(qvtcore::Mapping.__init__)


def test_qvtcore::mapping_constructor_args():
    sig = inspect.signature(qvtcore::Mapping.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::coredomain_is_not_abstract():
    assert not inspect.isabstract(qvtcore::CoreDomain)


def test_qvtcore::coredomain_constructor_exists():
    assert callable(qvtcore::CoreDomain.__init__)


def test_qvtcore::coredomain_constructor_args():
    sig = inspect.signature(qvtcore::CoreDomain.__init__)
    params = list(sig.parameters.keys())



def test_corepattern_is_not_abstract():
    assert not inspect.isabstract(CorePattern)


def test_corepattern_constructor_exists():
    assert callable(CorePattern.__init__)


def test_corepattern_constructor_args():
    sig = inspect.signature(CorePattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::guardpattern_is_not_abstract():
    assert not inspect.isabstract(qvtcore::GuardPattern)


def test_qvtcore::guardpattern_constructor_exists():
    assert callable(qvtcore::GuardPattern.__init__)


def test_qvtcore::guardpattern_constructor_args():
    sig = inspect.signature(qvtcore::GuardPattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::bottompattern_is_not_abstract():
    assert not inspect.isabstract(qvtcore::BottomPattern)


def test_qvtcore::bottompattern_constructor_exists():
    assert callable(qvtcore::BottomPattern.__init__)


def test_qvtcore::bottompattern_constructor_args():
    sig = inspect.signature(qvtcore::BottomPattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::moduleimport_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::ModuleImport)


def test_qvtoperational::moduleimport_constructor_exists():
    assert callable(qvtoperational::ModuleImport.__init__)


def test_qvtoperational::moduleimport_constructor_args():
    sig = inspect.signature(qvtoperational::ModuleImport.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_qvtoperational::moduleimport_has_kind():
    assert hasattr(qvtoperational::ModuleImport, "kind")
    descriptor = None
    for klass in qvtoperational::ModuleImport.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_guardpattern_is_not_abstract():
    assert not inspect.isabstract(GuardPattern)


def test_guardpattern_constructor_exists():
    assert callable(GuardPattern.__init__)


def test_guardpattern_constructor_args():
    sig = inspect.signature(GuardPattern.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore::area_is_not_abstract():
    assert not inspect.isabstract(qvtcore::Area)


def test_qvtcore::area_constructor_exists():
    assert callable(qvtcore::Area.__init__)


def test_qvtcore::area_constructor_args():
    sig = inspect.signature(qvtcore::Area.__init__)
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
    assert not inspect.isabstract(qvtoperational::ObjectExp)


def test_qvtoperational::objectexp_constructor_exists():
    assert callable(qvtoperational::ObjectExp.__init__)


def test_qvtoperational::objectexp_constructor_args():
    sig = inspect.signature(qvtoperational::ObjectExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::operationbody_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::OperationBody)


def test_qvtoperational::operationbody_constructor_exists():
    assert callable(qvtoperational::OperationBody.__init__)


def test_qvtoperational::operationbody_constructor_args():
    sig = inspect.signature(qvtoperational::OperationBody.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::imperativecallexp_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::ImperativeCallExp)


def test_qvtoperational::imperativecallexp_constructor_exists():
    assert callable(qvtoperational::ImperativeCallExp.__init__)


def test_qvtoperational::imperativecallexp_constructor_args():
    sig = inspect.signature(qvtoperational::ImperativeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_qvtoperational::imperativecallexp_has_isVirtual():
    assert hasattr(qvtoperational::ImperativeCallExp, "isVirtual")
    descriptor = None
    for klass in qvtoperational::ImperativeCallExp.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_modeltype_is_not_abstract():
    assert not inspect.isabstract(ModelType)


def test_modeltype_constructor_exists():
    assert callable(ModelType.__init__)


def test_modeltype_constructor_args():
    sig = inspect.signature(ModelType.__init__)
    params = list(sig.parameters.keys())



def test_moduleimport_is_not_abstract():
    assert not inspect.isabstract(ModuleImport)


def test_moduleimport_constructor_exists():
    assert callable(ModuleImport.__init__)


def test_moduleimport_constructor_args():
    sig = inspect.signature(ModuleImport.__init__)
    params = list(sig.parameters.keys())



def test_uriextent_is_not_abstract():
    assert not inspect.isabstract(URIExtent)


def test_uriextent_constructor_exists():
    assert callable(URIExtent.__init__)


def test_uriextent_constructor_args():
    sig = inspect.signature(URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::modeltype_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::ModelType)


def test_qvtoperational::modeltype_constructor_exists():
    assert callable(qvtoperational::ModelType.__init__)


def test_qvtoperational::modeltype_constructor_args():
    sig = inspect.signature(qvtoperational::ModelType.__init__)
    params = list(sig.parameters.keys())
    assert "conformanceKind" in params, "Missing parameter 'conformanceKind'"

def test_qvtoperational::modeltype_has_conformanceKind():
    assert hasattr(qvtoperational::ModelType, "conformanceKind")
    descriptor = None
    for klass in qvtoperational::ModelType.__mro__:
        if "conformanceKind" in klass.__dict__:
            descriptor = klass.__dict__["conformanceKind"]
            break
    assert isinstance(descriptor, property)



def test_entryoperation_is_not_abstract():
    assert not inspect.isabstract(EntryOperation)


def test_entryoperation_constructor_exists():
    assert callable(EntryOperation.__init__)


def test_entryoperation_constructor_args():
    sig = inspect.signature(EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_modelparameter_is_not_abstract():
    assert not inspect.isabstract(ModelParameter)


def test_modelparameter_constructor_exists():
    assert callable(ModelParameter.__init__)


def test_modelparameter_constructor_args():
    sig = inspect.signature(ModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::contextualproperty_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::ContextualProperty)


def test_qvtoperational::contextualproperty_constructor_exists():
    assert callable(qvtoperational::ContextualProperty.__init__)


def test_qvtoperational::contextualproperty_constructor_args():
    sig = inspect.signature(qvtoperational::ContextualProperty.__init__)
    params = list(sig.parameters.keys())



def test_imperativecallexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeCallExp)


def test_imperativecallexp_constructor_exists():
    assert callable(ImperativeCallExp.__init__)


def test_imperativecallexp_constructor_args():
    sig = inspect.signature(ImperativeCallExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::mappingcallexp_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::MappingCallExp)


def test_qvtoperational::mappingcallexp_constructor_exists():
    assert callable(qvtoperational::MappingCallExp.__init__)


def test_qvtoperational::mappingcallexp_constructor_args():
    sig = inspect.signature(qvtoperational::MappingCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isStrict" in params, "Missing parameter 'isStrict'"

def test_qvtoperational::mappingcallexp_has_isStrict():
    assert hasattr(qvtoperational::MappingCallExp, "isStrict")
    descriptor = None
    for klass in qvtoperational::MappingCallExp.__mro__:
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



def test_varparameter_is_not_abstract():
    assert not inspect.isabstract(VarParameter)


def test_varparameter_constructor_exists():
    assert callable(VarParameter.__init__)


def test_varparameter_constructor_args():
    sig = inspect.signature(VarParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::modelparameter_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::ModelParameter)


def test_qvtoperational::modelparameter_constructor_exists():
    assert callable(qvtoperational::ModelParameter.__init__)


def test_qvtoperational::modelparameter_constructor_args():
    sig = inspect.signature(qvtoperational::ModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::mappingparameter_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::MappingParameter)


def test_qvtoperational::mappingparameter_constructor_exists():
    assert callable(qvtoperational::MappingParameter.__init__)


def test_qvtoperational::mappingparameter_constructor_args():
    sig = inspect.signature(qvtoperational::MappingParameter.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_mappingoperation_is_not_abstract():
    assert not inspect.isabstract(MappingOperation)


def test_mappingoperation_constructor_exists():
    assert callable(MappingOperation.__init__)


def test_mappingoperation_constructor_args():
    sig = inspect.signature(MappingOperation.__init__)
    params = list(sig.parameters.keys())



def test_resolveexp_is_not_abstract():
    assert not inspect.isabstract(ResolveExp)


def test_resolveexp_constructor_exists():
    assert callable(ResolveExp.__init__)


def test_resolveexp_constructor_args():
    sig = inspect.signature(ResolveExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::resolveinexp_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::ResolveInExp)


def test_qvtoperational::resolveinexp_constructor_exists():
    assert callable(qvtoperational::ResolveInExp.__init__)


def test_qvtoperational::resolveinexp_constructor_args():
    sig = inspect.signature(qvtoperational::ResolveInExp.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::resolveexp_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::ResolveExp)


def test_qvtoperational::resolveexp_constructor_exists():
    assert callable(qvtoperational::ResolveExp.__init__)


def test_qvtoperational::resolveexp_constructor_args():
    sig = inspect.signature(qvtoperational::ResolveExp.__init__)
    params = list(sig.parameters.keys())
    assert "one" in params, "Missing parameter 'one'"
    assert "isDeferred" in params, "Missing parameter 'isDeferred'"
    assert "isInverse" in params, "Missing parameter 'isInverse'"

def test_qvtoperational::resolveexp_has_one():
    assert hasattr(qvtoperational::ResolveExp, "one")
    descriptor = None
    for klass in qvtoperational::ResolveExp.__mro__:
        if "one" in klass.__dict__:
            descriptor = klass.__dict__["one"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational::resolveexp_has_isDeferred():
    assert hasattr(qvtoperational::ResolveExp, "isDeferred")
    descriptor = None
    for klass in qvtoperational::ResolveExp.__mro__:
        if "isDeferred" in klass.__dict__:
            descriptor = klass.__dict__["isDeferred"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational::resolveexp_has_isInverse():
    assert hasattr(qvtoperational::ResolveExp, "isInverse")
    descriptor = None
    for klass in qvtoperational::ResolveExp.__mro__:
        if "isInverse" in klass.__dict__:
            descriptor = klass.__dict__["isInverse"]
            break
    assert isinstance(descriptor, property)



def test_imperativeoperation_is_not_abstract():
    assert not inspect.isabstract(ImperativeOperation)


def test_imperativeoperation_constructor_exists():
    assert callable(ImperativeOperation.__init__)


def test_imperativeoperation_constructor_args():
    sig = inspect.signature(ImperativeOperation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::constructor_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::Constructor)


def test_qvtoperational::constructor_constructor_exists():
    assert callable(qvtoperational::Constructor.__init__)


def test_qvtoperational::constructor_constructor_args():
    sig = inspect.signature(qvtoperational::Constructor.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::entryoperation_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::EntryOperation)


def test_qvtoperational::entryoperation_constructor_exists():
    assert callable(qvtoperational::EntryOperation.__init__)


def test_qvtoperational::entryoperation_constructor_args():
    sig = inspect.signature(qvtoperational::EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::helper_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::Helper)


def test_qvtoperational::helper_constructor_exists():
    assert callable(qvtoperational::Helper.__init__)


def test_qvtoperational::helper_constructor_args():
    sig = inspect.signature(qvtoperational::Helper.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"

def test_qvtoperational::helper_has_isQuery():
    assert hasattr(qvtoperational::Helper, "isQuery")
    descriptor = None
    for klass in qvtoperational::Helper.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)



def test_operationbody_is_not_abstract():
    assert not inspect.isabstract(OperationBody)


def test_operationbody_constructor_exists():
    assert callable(OperationBody.__init__)


def test_operationbody_constructor_args():
    sig = inspect.signature(OperationBody.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::constructorbody_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::ConstructorBody)


def test_qvtoperational::constructorbody_constructor_exists():
    assert callable(qvtoperational::ConstructorBody.__init__)


def test_qvtoperational::constructorbody_constructor_args():
    sig = inspect.signature(qvtoperational::ConstructorBody.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::mappingbody_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::MappingBody)


def test_qvtoperational::mappingbody_constructor_exists():
    assert callable(qvtoperational::MappingBody.__init__)


def test_qvtoperational::mappingbody_constructor_args():
    sig = inspect.signature(qvtoperational::MappingBody.__init__)
    params = list(sig.parameters.keys())



def test_emof::comment_is_not_abstract():
    assert not inspect.isabstract(emof::Comment)


def test_emof::comment_constructor_exists():
    assert callable(emof::Comment.__init__)


def test_emof::comment_constructor_args():
    sig = inspect.signature(emof::Comment.__init__)
    params = list(sig.parameters.keys())



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_emof::uriextent_is_not_abstract():
    assert not inspect.isabstract(emof::URIExtent)


def test_emof::uriextent_constructor_exists():
    assert callable(emof::URIExtent.__init__)


def test_emof::uriextent_constructor_args():
    sig = inspect.signature(emof::URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::varparameter_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::VarParameter)


def test_qvtoperational::varparameter_constructor_exists():
    assert callable(qvtoperational::VarParameter.__init__)


def test_qvtoperational::varparameter_constructor_args():
    sig = inspect.signature(qvtoperational::VarParameter.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_qvtoperational::varparameter_has_kind():
    assert hasattr(qvtoperational::VarParameter, "kind")
    descriptor = None
    for klass in qvtoperational::VarParameter.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_qvtbase::functionparameter_is_not_abstract():
    assert not inspect.isabstract(qvtbase::FunctionParameter)


def test_qvtbase::functionparameter_constructor_exists():
    assert callable(qvtbase::FunctionParameter.__init__)


def test_qvtbase::functionparameter_constructor_args():
    sig = inspect.signature(qvtbase::FunctionParameter.__init__)
    params = list(sig.parameters.keys())



def test_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::module_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::Module)


def test_qvtoperational::module_constructor_exists():
    assert callable(qvtoperational::Module.__init__)


def test_qvtoperational::module_constructor_args():
    sig = inspect.signature(qvtoperational::Module.__init__)
    params = list(sig.parameters.keys())
    assert "isBlackbox" in params, "Missing parameter 'isBlackbox'"

def test_qvtoperational::module_has_isBlackbox():
    assert hasattr(qvtoperational::Module, "isBlackbox")
    descriptor = None
    for klass in qvtoperational::Module.__mro__:
        if "isBlackbox" in klass.__dict__:
            descriptor = klass.__dict__["isBlackbox"]
            break
    assert isinstance(descriptor, property)



def test_qvtbase::transformation_is_not_abstract():
    assert not inspect.isabstract(qvtbase::Transformation)


def test_qvtbase::transformation_constructor_exists():
    assert callable(qvtbase::Transformation.__init__)


def test_qvtbase::transformation_constructor_args():
    sig = inspect.signature(qvtbase::Transformation.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_emof::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(emof::EnumerationLiteral)


def test_emof::enumerationliteral_constructor_exists():
    assert callable(emof::EnumerationLiteral.__init__)


def test_emof::enumerationliteral_constructor_args():
    sig = inspect.signature(emof::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase::typedmodel_is_not_abstract():
    assert not inspect.isabstract(qvtbase::TypedModel)


def test_qvtbase::typedmodel_constructor_exists():
    assert callable(qvtbase::TypedModel.__init__)


def test_qvtbase::typedmodel_constructor_args():
    sig = inspect.signature(qvtbase::TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase::domain_is_not_abstract():
    assert not inspect.isabstract(qvtbase::Domain)


def test_qvtbase::domain_constructor_exists():
    assert callable(qvtbase::Domain.__init__)


def test_qvtbase::domain_constructor_args():
    sig = inspect.signature(qvtbase::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "isCheckable" in params, "Missing parameter 'isCheckable'"
    assert "isEnforceable" in params, "Missing parameter 'isEnforceable'"

def test_qvtbase::domain_has_isCheckable():
    assert hasattr(qvtbase::Domain, "isCheckable")
    descriptor = None
    for klass in qvtbase::Domain.__mro__:
        if "isCheckable" in klass.__dict__:
            descriptor = klass.__dict__["isCheckable"]
            break
    assert isinstance(descriptor, property)

def test_qvtbase::domain_has_isEnforceable():
    assert hasattr(qvtbase::Domain, "isEnforceable")
    descriptor = None
    for klass in qvtbase::Domain.__mro__:
        if "isEnforceable" in klass.__dict__:
            descriptor = klass.__dict__["isEnforceable"]
            break
    assert isinstance(descriptor, property)



def test_qvtbase::rule_is_not_abstract():
    assert not inspect.isabstract(qvtbase::Rule)


def test_qvtbase::rule_constructor_exists():
    assert callable(qvtbase::Rule.__init__)


def test_qvtbase::rule_constructor_args():
    sig = inspect.signature(qvtbase::Rule.__init__)
    params = list(sig.parameters.keys())



def test_emof::type_is_not_abstract():
    assert not inspect.isabstract(emof::Type)


def test_emof::type_constructor_exists():
    assert callable(emof::Type.__init__)


def test_emof::type_constructor_args():
    sig = inspect.signature(emof::Type.__init__)
    params = list(sig.parameters.keys())



def test_emof::typedelement_is_not_abstract():
    assert not inspect.isabstract(emof::TypedElement)


def test_emof::typedelement_constructor_exists():
    assert callable(emof::TypedElement.__init__)


def test_emof::typedelement_constructor_args():
    sig = inspect.signature(emof::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_emof::package_is_not_abstract():
    assert not inspect.isabstract(emof::Package)


def test_emof::package_constructor_exists():
    assert callable(emof::Package.__init__)


def test_emof::package_constructor_args():
    sig = inspect.signature(emof::Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_emof::package_has_uri():
    assert hasattr(emof::Package, "uri")
    descriptor = None
    for klass in emof::Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_emof::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(emof::MultiplicityElement)


def test_emof::multiplicityelement_constructor_exists():
    assert callable(emof::MultiplicityElement.__init__)


def test_emof::multiplicityelement_constructor_args():
    sig = inspect.signature(emof::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_emof::multiplicityelement_has_lower():
    assert hasattr(emof::MultiplicityElement, "lower")
    descriptor = None
    for klass in emof::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_emof::multiplicityelement_has_isUnique():
    assert hasattr(emof::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in emof::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_emof::multiplicityelement_has_upper():
    assert hasattr(emof::MultiplicityElement, "upper")
    descriptor = None
    for klass in emof::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_emof::multiplicityelement_has_isOrdered():
    assert hasattr(emof::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in emof::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::listtype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ListType)


def test_imperativeocl::listtype_constructor_exists():
    assert callable(imperativeocl::ListType.__init__)


def test_imperativeocl::listtype_constructor_args():
    sig = inspect.signature(imperativeocl::ListType.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::variable_is_not_abstract():
    assert not inspect.isabstract(essentialocl::Variable)


def test_essentialocl::variable_constructor_exists():
    assert callable(essentialocl::Variable.__init__)


def test_essentialocl::variable_constructor_args():
    sig = inspect.signature(essentialocl::Variable.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(essentialocl::TupleLiteralPart)


def test_essentialocl::tupleliteralpart_constructor_exists():
    assert callable(essentialocl::TupleLiteralPart.__init__)


def test_essentialocl::tupleliteralpart_constructor_args():
    sig = inspect.signature(essentialocl::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(essentialocl::CollectionLiteralPart)


def test_essentialocl::collectionliteralpart_constructor_exists():
    assert callable(essentialocl::CollectionLiteralPart.__init__)


def test_essentialocl::collectionliteralpart_constructor_args():
    sig = inspect.signature(essentialocl::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(essentialocl::OclExpression)


def test_essentialocl::oclexpression_constructor_exists():
    assert callable(essentialocl::OclExpression.__init__)


def test_essentialocl::oclexpression_constructor_args():
    sig = inspect.signature(essentialocl::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_emof::parameter_is_not_abstract():
    assert not inspect.isabstract(emof::Parameter)


def test_emof::parameter_constructor_exists():
    assert callable(emof::Parameter.__init__)


def test_emof::parameter_constructor_args():
    sig = inspect.signature(emof::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_emof::property_is_not_abstract():
    assert not inspect.isabstract(emof::Property)


def test_emof::property_constructor_exists():
    assert callable(emof::Property.__init__)


def test_emof::property_constructor_args():
    sig = inspect.signature(emof::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isId" in params, "Missing parameter 'isId'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_emof::property_has_isId():
    assert hasattr(emof::Property, "isId")
    descriptor = None
    for klass in emof::Property.__mro__:
        if "isId" in klass.__dict__:
            descriptor = klass.__dict__["isId"]
            break
    assert isinstance(descriptor, property)

def test_emof::property_has_default():
    assert hasattr(emof::Property, "default")
    descriptor = None
    for klass in emof::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_emof::property_has_isReadOnly():
    assert hasattr(emof::Property, "isReadOnly")
    descriptor = None
    for klass in emof::Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_emof::property_has_isComposite():
    assert hasattr(emof::Property, "isComposite")
    descriptor = None
    for klass in emof::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_emof::property_has_isDerived():
    assert hasattr(emof::Property, "isDerived")
    descriptor = None
    for klass in emof::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_emof::operation_is_not_abstract():
    assert not inspect.isabstract(emof::Operation)


def test_emof::operation_constructor_exists():
    assert callable(emof::Operation.__init__)


def test_emof::operation_constructor_args():
    sig = inspect.signature(emof::Operation.__init__)
    params = list(sig.parameters.keys())



def test_emof::object_is_not_abstract():
    assert not inspect.isabstract(emof::Object)


def test_emof::object_constructor_exists():
    assert callable(emof::Object.__init__)


def test_emof::object_constructor_args():
    sig = inspect.signature(emof::Object.__init__)
    params = list(sig.parameters.keys())



def test_emof::namedelement_is_not_abstract():
    assert not inspect.isabstract(emof::NamedElement)


def test_emof::namedelement_constructor_exists():
    assert callable(emof::NamedElement.__init__)


def test_emof::namedelement_constructor_args():
    sig = inspect.signature(emof::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_emof::namedelement_has_name():
    assert hasattr(emof::NamedElement, "name")
    descriptor = None
    for klass in emof::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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
    assert not inspect.isabstract(essentialocl::CollectionType)


def test_essentialocl::collectiontype_constructor_exists():
    assert callable(essentialocl::CollectionType.__init__)


def test_essentialocl::collectiontype_constructor_args():
    sig = inspect.signature(essentialocl::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_emof::primitivetype_is_not_abstract():
    assert not inspect.isabstract(emof::PrimitiveType)


def test_emof::primitivetype_constructor_exists():
    assert callable(emof::PrimitiveType.__init__)


def test_emof::primitivetype_constructor_args():
    sig = inspect.signature(emof::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(essentialocl::TupleType)


def test_essentialocl::tupletype_constructor_exists():
    assert callable(essentialocl::TupleType.__init__)


def test_essentialocl::tupletype_constructor_args():
    sig = inspect.signature(essentialocl::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_emof::enumeration_is_not_abstract():
    assert not inspect.isabstract(emof::Enumeration)


def test_emof::enumeration_constructor_exists():
    assert callable(emof::Enumeration.__init__)


def test_emof::enumeration_constructor_args():
    sig = inspect.signature(emof::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::library_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::Library)


def test_qvtoperational::library_constructor_exists():
    assert callable(qvtoperational::Library.__init__)


def test_qvtoperational::library_constructor_args():
    sig = inspect.signature(qvtoperational::Library.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::operationaltransformation_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::OperationalTransformation)


def test_qvtoperational::operationaltransformation_constructor_exists():
    assert callable(qvtoperational::OperationalTransformation.__init__)


def test_qvtoperational::operationaltransformation_constructor_args():
    sig = inspect.signature(qvtoperational::OperationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_transformation_is_not_abstract():
    assert not inspect.isabstract(Transformation)


def test_transformation_constructor_exists():
    assert callable(Transformation.__init__)


def test_transformation_constructor_args():
    sig = inspect.signature(Transformation.__init__)
    params = list(sig.parameters.keys())



def test_qvtrelation::relationaltransformation_is_not_abstract():
    assert not inspect.isabstract(qvtrelation::RelationalTransformation)


def test_qvtrelation::relationaltransformation_constructor_exists():
    assert callable(qvtrelation::RelationalTransformation.__init__)


def test_qvtrelation::relationaltransformation_constructor_args():
    sig = inspect.signature(qvtrelation::RelationalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_emof::tag_is_not_abstract():
    assert not inspect.isabstract(emof::Tag)


def test_emof::tag_constructor_exists():
    assert callable(emof::Tag.__init__)


def test_emof::tag_constructor_args():
    sig = inspect.signature(emof::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_emof::tag_has_value():
    assert hasattr(emof::Tag, "value")
    descriptor = None
    for klass in emof::Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_emof::tag_has_name():
    assert hasattr(emof::Tag, "name")
    descriptor = None
    for klass in emof::Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_emof::extent_is_not_abstract():
    assert not inspect.isabstract(emof::Extent)


def test_emof::extent_constructor_exists():
    assert callable(emof::Extent.__init__)


def test_emof::extent_constructor_args():
    sig = inspect.signature(emof::Extent.__init__)
    params = list(sig.parameters.keys())



def test_emof::element_is_not_abstract():
    assert not inspect.isabstract(emof::Element)


def test_emof::element_constructor_exists():
    assert callable(emof::Element.__init__)


def test_emof::element_constructor_args():
    sig = inspect.signature(emof::Element.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_qvtbase::function_is_not_abstract():
    assert not inspect.isabstract(qvtbase::Function)


def test_qvtbase::function_constructor_exists():
    assert callable(qvtbase::Function.__init__)


def test_qvtbase::function_constructor_args():
    sig = inspect.signature(qvtbase::Function.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::imperativeoperation_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::ImperativeOperation)


def test_qvtoperational::imperativeoperation_constructor_exists():
    assert callable(qvtoperational::ImperativeOperation.__init__)


def test_qvtoperational::imperativeoperation_constructor_args():
    sig = inspect.signature(qvtoperational::ImperativeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "isBlackbox" in params, "Missing parameter 'isBlackbox'"

def test_qvtoperational::imperativeoperation_has_isBlackbox():
    assert hasattr(qvtoperational::ImperativeOperation, "isBlackbox")
    descriptor = None
    for klass in qvtoperational::ImperativeOperation.__mro__:
        if "isBlackbox" in klass.__dict__:
            descriptor = klass.__dict__["isBlackbox"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational::mappingoperation_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::MappingOperation)


def test_qvtoperational::mappingoperation_constructor_exists():
    assert callable(qvtoperational::MappingOperation.__init__)


def test_qvtoperational::mappingoperation_constructor_args():
    sig = inspect.signature(qvtoperational::MappingOperation.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::AnonymousTupleLiteralPart)


def test_imperativeocl::anonymoustupleliteralpart_constructor_exists():
    assert callable(imperativeocl::AnonymousTupleLiteralPart.__init__)


def test_imperativeocl::anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(imperativeocl::AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(AnonymousTupleLiteralPart)


def test_anonymoustupleliteralpart_constructor_exists():
    assert callable(AnonymousTupleLiteralPart.__init__)


def test_anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::anonymoustupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::AnonymousTupleLiteralExp)


def test_imperativeocl::anonymoustupleliteralexp_constructor_exists():
    assert callable(imperativeocl::AnonymousTupleLiteralExp.__init__)


def test_imperativeocl::anonymoustupleliteralexp_constructor_args():
    sig = inspect.signature(imperativeocl::AnonymousTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::anonymoustupletype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::AnonymousTupleType)


def test_imperativeocl::anonymoustupletype_constructor_exists():
    assert callable(imperativeocl::AnonymousTupleType.__init__)


def test_imperativeocl::anonymoustupletype_constructor_args():
    sig = inspect.signature(imperativeocl::AnonymousTupleType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::unpackexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::UnpackExp)


def test_imperativeocl::unpackexp_constructor_exists():
    assert callable(imperativeocl::UnpackExp.__init__)


def test_imperativeocl::unpackexp_constructor_args():
    sig = inspect.signature(imperativeocl::UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ImperativeExpression)


def test_imperativeocl::imperativeexpression_constructor_exists():
    assert callable(imperativeocl::ImperativeExpression.__init__)


def test_imperativeocl::imperativeexpression_constructor_args():
    sig = inspect.signature(imperativeocl::ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::collectorexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::CollectorExp)


def test_imperativeocl::collectorexp_constructor_exists():
    assert callable(imperativeocl::CollectorExp.__init__)


def test_imperativeocl::collectorexp_constructor_args():
    sig = inspect.signature(imperativeocl::CollectorExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::IteratorExp)


def test_essentialocl::iteratorexp_constructor_exists():
    assert callable(essentialocl::IteratorExp.__init__)


def test_essentialocl::iteratorexp_constructor_args():
    sig = inspect.signature(essentialocl::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::IterateExp)


def test_essentialocl::iterateexp_constructor_exists():
    assert callable(essentialocl::IterateExp.__init__)


def test_essentialocl::iterateexp_constructor_args():
    sig = inspect.signature(essentialocl::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ImperativeLoopExp)


def test_imperativeocl::imperativeloopexp_constructor_exists():
    assert callable(imperativeocl::ImperativeLoopExp.__init__)


def test_imperativeocl::imperativeloopexp_constructor_args():
    sig = inspect.signature(imperativeocl::ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::assertexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::AssertExp)


def test_imperativeocl::assertexp_constructor_exists():
    assert callable(imperativeocl::AssertExp.__init__)


def test_imperativeocl::assertexp_constructor_args():
    sig = inspect.signature(imperativeocl::AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_imperativeocl::assertexp_has_severity():
    assert hasattr(imperativeocl::AssertExp, "severity")
    descriptor = None
    for klass in imperativeocl::AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::TupleExp)


def test_imperativeocl::tupleexp_constructor_exists():
    assert callable(imperativeocl::TupleExp.__init__)


def test_imperativeocl::tupleexp_constructor_args():
    sig = inspect.signature(imperativeocl::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::forexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ForExp)


def test_imperativeocl::forexp_constructor_exists():
    assert callable(imperativeocl::ForExp.__init__)


def test_imperativeocl::forexp_constructor_args():
    sig = inspect.signature(imperativeocl::ForExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::continueexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ContinueExp)


def test_imperativeocl::continueexp_constructor_exists():
    assert callable(imperativeocl::ContinueExp.__init__)


def test_imperativeocl::continueexp_constructor_args():
    sig = inspect.signature(imperativeocl::ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::logexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::LogExp)


def test_imperativeocl::logexp_constructor_exists():
    assert callable(imperativeocl::LogExp.__init__)


def test_imperativeocl::logexp_constructor_args():
    sig = inspect.signature(imperativeocl::LogExp.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "text" in params, "Missing parameter 'text'"

def test_imperativeocl::logexp_has_level():
    assert hasattr(imperativeocl::LogExp, "level")
    descriptor = None
    for klass in imperativeocl::LogExp.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_imperativeocl::logexp_has_text():
    assert hasattr(imperativeocl::LogExp, "text")
    descriptor = None
    for klass in imperativeocl::LogExp.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::DictLiteralPart)


def test_imperativeocl::dictliteralpart_constructor_exists():
    assert callable(imperativeocl::DictLiteralPart.__init__)


def test_imperativeocl::dictliteralpart_constructor_args():
    sig = inspect.signature(imperativeocl::DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::DictLiteralExp)


def test_imperativeocl::dictliteralexp_constructor_exists():
    assert callable(imperativeocl::DictLiteralExp.__init__)


def test_imperativeocl::dictliteralexp_constructor_args():
    sig = inspect.signature(imperativeocl::DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::dictionarytype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::DictionaryType)


def test_imperativeocl::dictionarytype_constructor_exists():
    assert callable(imperativeocl::DictionaryType.__init__)


def test_imperativeocl::dictionarytype_constructor_args():
    sig = inspect.signature(imperativeocl::DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::instantiationexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::InstantiationExp)


def test_imperativeocl::instantiationexp_constructor_exists():
    assert callable(imperativeocl::InstantiationExp.__init__)


def test_imperativeocl::instantiationexp_constructor_args():
    sig = inspect.signature(imperativeocl::InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::typedef_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::Typedef)


def test_imperativeocl::typedef_constructor_exists():
    assert callable(imperativeocl::Typedef.__init__)


def test_imperativeocl::typedef_constructor_args():
    sig = inspect.signature(imperativeocl::Typedef.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::whileexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::WhileExp)


def test_imperativeocl::whileexp_constructor_exists():
    assert callable(imperativeocl::WhileExp.__init__)


def test_imperativeocl::whileexp_constructor_args():
    sig = inspect.signature(imperativeocl::WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::raiseexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::RaiseExp)


def test_imperativeocl::raiseexp_constructor_exists():
    assert callable(imperativeocl::RaiseExp.__init__)


def test_imperativeocl::raiseexp_constructor_args():
    sig = inspect.signature(imperativeocl::RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_emof::class_is_not_abstract():
    assert not inspect.isabstract(emof::Class)


def test_emof::class_constructor_exists():
    assert callable(emof::Class.__init__)


def test_emof::class_constructor_args():
    sig = inspect.signature(emof::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_emof::class_has_isAbstract():
    assert hasattr(emof::Class, "isAbstract")
    descriptor = None
    for klass in emof::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_imperativeocl::templateparametertype_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::TemplateParameterType)


def test_imperativeocl::templateparametertype_constructor_exists():
    assert callable(imperativeocl::TemplateParameterType.__init__)


def test_imperativeocl::templateparametertype_constructor_args():
    sig = inspect.signature(imperativeocl::TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_imperativeocl::templateparametertype_has_specification():
    assert hasattr(imperativeocl::TemplateParameterType, "specification")
    descriptor = None
    for klass in imperativeocl::TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_essentialocl::anytype_is_not_abstract():
    assert not inspect.isabstract(essentialocl::AnyType)


def test_essentialocl::anytype_constructor_exists():
    assert callable(essentialocl::AnyType.__init__)


def test_essentialocl::anytype_constructor_args():
    sig = inspect.signature(essentialocl::AnyType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::invalidtype_is_not_abstract():
    assert not inspect.isabstract(essentialocl::InvalidType)


def test_essentialocl::invalidtype_constructor_exists():
    assert callable(essentialocl::InvalidType.__init__)


def test_essentialocl::invalidtype_constructor_args():
    sig = inspect.signature(essentialocl::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_emof::datatype_is_not_abstract():
    assert not inspect.isabstract(emof::DataType)


def test_emof::datatype_constructor_exists():
    assert callable(emof::DataType.__init__)


def test_emof::datatype_constructor_args():
    sig = inspect.signature(emof::DataType.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::voidtype_is_not_abstract():
    assert not inspect.isabstract(essentialocl::VoidType)


def test_essentialocl::voidtype_constructor_exists():
    assert callable(essentialocl::VoidType.__init__)


def test_essentialocl::voidtype_constructor_args():
    sig = inspect.signature(essentialocl::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::tryexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::TryExp)


def test_imperativeocl::tryexp_constructor_exists():
    assert callable(imperativeocl::TryExp.__init__)


def test_imperativeocl::tryexp_constructor_args():
    sig = inspect.signature(imperativeocl::TryExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::breakexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::BreakExp)


def test_imperativeocl::breakexp_constructor_exists():
    assert callable(imperativeocl::BreakExp.__init__)


def test_imperativeocl::breakexp_constructor_args():
    sig = inspect.signature(imperativeocl::BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::returnexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ReturnExp)


def test_imperativeocl::returnexp_constructor_exists():
    assert callable(imperativeocl::ReturnExp.__init__)


def test_imperativeocl::returnexp_constructor_args():
    sig = inspect.signature(imperativeocl::ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::unlinkexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::UnlinkExp)


def test_imperativeocl::unlinkexp_constructor_exists():
    assert callable(imperativeocl::UnlinkExp.__init__)


def test_imperativeocl::unlinkexp_constructor_args():
    sig = inspect.signature(imperativeocl::UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::altexp_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::AltExp)


def test_imperativeocl::altexp_constructor_exists():
    assert callable(imperativeocl::AltExp.__init__)


def test_imperativeocl::altexp_constructor_args():
    sig = inspect.signature(imperativeocl::AltExp.__init__)
    params = list(sig.parameters.keys())

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "OrderedSet",
        "Set",
        "Bag",
        "Sequence",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"

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
        "out",
        "inout",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionKind"

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
CollectionType_strategy = st.builds(
    CollectionType,
)
AltExp_strategy = st.builds(
    AltExp,
)
CallExp_strategy = st.builds(
    CallExp,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
imperativeocl::VariableInitExp_strategy = st.builds(
    imperativeocl::VariableInitExp,
    withResult=
        safe_text
)
imperativeocl::SwitchExp_strategy = st.builds(
    imperativeocl::SwitchExp,
)
imperativeocl::BlockExp_strategy = st.builds(
    imperativeocl::BlockExp,
)
imperativeocl::ComputeExp_strategy = st.builds(
    imperativeocl::ComputeExp,
)
imperativeocl::AssignExp_strategy = st.builds(
    imperativeocl::AssignExp,
    isReset=
        safe_text
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
imperativeocl::ImperativeIterateExp_strategy = st.builds(
    imperativeocl::ImperativeIterateExp,
)
Property_strategy = st.builds(
    Property,
)
ObjectTemplateExp_strategy = st.builds(
    ObjectTemplateExp,
)
Element_strategy = st.builds(
    Element,
)
qvttemplate::PropertyTemplateItem_strategy = st.builds(
    qvttemplate::PropertyTemplateItem,
)
Class_strategy = st.builds(
    Class,
)
PropertyTemplateItem_strategy = st.builds(
    PropertyTemplateItem,
)
TemplateExp_strategy = st.builds(
    TemplateExp,
)
qvttemplate::CollectionTemplateExp_strategy = st.builds(
    qvttemplate::CollectionTemplateExp,
    kind=
        safe_text
)
qvttemplate::ObjectTemplateExp_strategy = st.builds(
    qvttemplate::ObjectTemplateExp,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
Variable_strategy = st.builds(
    Variable,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
qvttemplate::TemplateExp_strategy = st.builds(
    qvttemplate::TemplateExp,
)
essentialocl::SetType_strategy = st.builds(
    essentialocl::SetType,
)
essentialocl::SequenceType_strategy = st.builds(
    essentialocl::SequenceType,
)
essentialocl::OrderedSetType_strategy = st.builds(
    essentialocl::OrderedSetType,
)
essentialocl::EnumLiteralExp_strategy = st.builds(
    essentialocl::EnumLiteralExp,
)
essentialocl::BagType_strategy = st.builds(
    essentialocl::BagType,
)
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
essentialocl::FeaturePropertyCall_strategy = st.builds(
    essentialocl::FeaturePropertyCall,
)
essentialocl::InvalidLiteralExp_strategy = st.builds(
    essentialocl::InvalidLiteralExp,
)
essentialocl::OpaqueExpression_strategy = st.builds(
    essentialocl::OpaqueExpression,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
essentialocl::ExpressionInOcl_strategy = st.builds(
    essentialocl::ExpressionInOcl,
)
essentialocl::NullLiteralExp_strategy = st.builds(
    essentialocl::NullLiteralExp,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
essentialocl::TupleLiteralExp_strategy = st.builds(
    essentialocl::TupleLiteralExp,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
essentialocl::CollectionItem_strategy = st.builds(
    essentialocl::CollectionItem,
)
essentialocl::CollectionRange_strategy = st.builds(
    essentialocl::CollectionRange,
)
essentialocl::CollectionLiteralExp_strategy = st.builds(
    essentialocl::CollectionLiteralExp,
    kind=
        safe_text
)
essentialocl::PrimitiveLiteralExp_strategy = st.builds(
    essentialocl::PrimitiveLiteralExp,
)
essentialocl::LiteralExp_strategy = st.builds(
    essentialocl::LiteralExp,
)
essentialocl::LoopExp_strategy = st.builds(
    essentialocl::LoopExp,
)
essentialocl::TypeExp_strategy = st.builds(
    essentialocl::TypeExp,
)
essentialocl::VariableExp_strategy = st.builds(
    essentialocl::VariableExp,
)
FeaturePropertyCall_strategy = st.builds(
    FeaturePropertyCall,
)
essentialocl::OperationCallExp_strategy = st.builds(
    essentialocl::OperationCallExp,
)
essentialocl::PropertyCallExp_strategy = st.builds(
    essentialocl::PropertyCallExp,
)
ComputeExp_strategy = st.builds(
    ComputeExp,
)
LetExp_strategy = st.builds(
    LetExp,
)
essentialocl::CallExp_strategy = st.builds(
    essentialocl::CallExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
essentialocl::StringLiteralExp_strategy = st.builds(
    essentialocl::StringLiteralExp,
    stringSymbol=
        safe_text
)
essentialocl::NumericLiteralExp_strategy = st.builds(
    essentialocl::NumericLiteralExp,
)
essentialocl::BooleanLiteralExp_strategy = st.builds(
    essentialocl::BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
essentialocl::LetExp_strategy = st.builds(
    essentialocl::LetExp,
)
essentialocl::IfExp_strategy = st.builds(
    essentialocl::IfExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
essentialocl::RealLiteralExp_strategy = st.builds(
    essentialocl::RealLiteralExp,
    realSymbol=
        safe_text
)
essentialocl::IntegerLiteralExp_strategy = st.builds(
    essentialocl::IntegerLiteralExp,
    integerSymbol=
        safe_text
)
essentialocl::UnlimitedNaturalExp_strategy = st.builds(
    essentialocl::UnlimitedNaturalExp,
    symbol=
        safe_text
)
TryExp_strategy = st.builds(
    TryExp,
)
RelationalTransformation_strategy = st.builds(
    RelationalTransformation,
)
qvtrelation::Key_strategy = st.builds(
    qvtrelation::Key,
)
qvtrelation::RelationImplementation_strategy = st.builds(
    qvtrelation::RelationImplementation,
)
DomainPattern_strategy = st.builds(
    DomainPattern,
)
qvtbase::Pattern_strategy = st.builds(
    qvtbase::Pattern,
)
RelationImplementation_strategy = st.builds(
    RelationImplementation,
)
Key_strategy = st.builds(
    Key,
)
qvtbase::Predicate_strategy = st.builds(
    qvtbase::Predicate,
)
Predicate_strategy = st.builds(
    Predicate,
)
qvtcore::EnforcementOperation_strategy = st.builds(
    qvtcore::EnforcementOperation,
    enforcementMode=
        safe_text
)
TypedModel_strategy = st.builds(
    TypedModel,
)
qvtcore::Assignment_strategy = st.builds(
    qvtcore::Assignment,
    isDefault=
        safe_text
)
BottomPattern_strategy = st.builds(
    BottomPattern,
)
Pattern_strategy = st.builds(
    Pattern,
)
qvtrelation::DomainPattern_strategy = st.builds(
    qvtrelation::DomainPattern,
)
qvtcore::CorePattern_strategy = st.builds(
    qvtcore::CorePattern,
)
Domain_strategy = st.builds(
    Domain,
)
qvtrelation::RelationDomain_strategy = st.builds(
    qvtrelation::RelationDomain,
)
qvtcore::RealizedVariable_strategy = st.builds(
    qvtcore::RealizedVariable,
)
Mapping_strategy = st.builds(
    Mapping,
)
Rule_strategy = st.builds(
    Rule,
)
qvtrelation::Relation_strategy = st.builds(
    qvtrelation::Relation,
    isTopLevel=
        safe_text
)
EnforcementOperation_strategy = st.builds(
    EnforcementOperation,
)
RealizedVariable_strategy = st.builds(
    RealizedVariable,
)
Assignment_strategy = st.builds(
    Assignment,
)
Area_strategy = st.builds(
    Area,
)
qvtcore::Mapping_strategy = st.builds(
    qvtcore::Mapping,
)
qvtcore::CoreDomain_strategy = st.builds(
    qvtcore::CoreDomain,
)
CorePattern_strategy = st.builds(
    CorePattern,
)
qvtcore::GuardPattern_strategy = st.builds(
    qvtcore::GuardPattern,
)
qvtcore::BottomPattern_strategy = st.builds(
    qvtcore::BottomPattern,
)
qvtoperational::ModuleImport_strategy = st.builds(
    qvtoperational::ModuleImport,
    kind=
        safe_text
)
GuardPattern_strategy = st.builds(
    GuardPattern,
)
qvtcore::Area_strategy = st.builds(
    qvtcore::Area,
)
ConstructorBody_strategy = st.builds(
    ConstructorBody,
)
InstantiationExp_strategy = st.builds(
    InstantiationExp,
)
qvtoperational::ObjectExp_strategy = st.builds(
    qvtoperational::ObjectExp,
)
qvtoperational::OperationBody_strategy = st.builds(
    qvtoperational::OperationBody,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
qvtoperational::ImperativeCallExp_strategy = st.builds(
    qvtoperational::ImperativeCallExp,
    isVirtual=
        safe_text
)
ModelType_strategy = st.builds(
    ModelType,
)
ModuleImport_strategy = st.builds(
    ModuleImport,
)
URIExtent_strategy = st.builds(
    URIExtent,
)
qvtoperational::ModelType_strategy = st.builds(
    qvtoperational::ModelType,
    conformanceKind=
        safe_text
)
EntryOperation_strategy = st.builds(
    EntryOperation,
)
ModelParameter_strategy = st.builds(
    ModelParameter,
)
qvtoperational::ContextualProperty_strategy = st.builds(
    qvtoperational::ContextualProperty,
)
ImperativeCallExp_strategy = st.builds(
    ImperativeCallExp,
)
qvtoperational::MappingCallExp_strategy = st.builds(
    qvtoperational::MappingCallExp,
    isStrict=
        safe_text
)
RelationDomain_strategy = st.builds(
    RelationDomain,
)
VarParameter_strategy = st.builds(
    VarParameter,
)
qvtoperational::ModelParameter_strategy = st.builds(
    qvtoperational::ModelParameter,
)
qvtoperational::MappingParameter_strategy = st.builds(
    qvtoperational::MappingParameter,
)
Relation_strategy = st.builds(
    Relation,
)
MappingOperation_strategy = st.builds(
    MappingOperation,
)
ResolveExp_strategy = st.builds(
    ResolveExp,
)
qvtoperational::ResolveInExp_strategy = st.builds(
    qvtoperational::ResolveInExp,
)
qvtoperational::ResolveExp_strategy = st.builds(
    qvtoperational::ResolveExp,
    one=
        safe_text,
    isDeferred=
        safe_text,
    isInverse=
        safe_text
)
ImperativeOperation_strategy = st.builds(
    ImperativeOperation,
)
qvtoperational::Constructor_strategy = st.builds(
    qvtoperational::Constructor,
)
qvtoperational::EntryOperation_strategy = st.builds(
    qvtoperational::EntryOperation,
)
qvtoperational::Helper_strategy = st.builds(
    qvtoperational::Helper,
    isQuery=
        safe_text
)
OperationBody_strategy = st.builds(
    OperationBody,
)
qvtoperational::ConstructorBody_strategy = st.builds(
    qvtoperational::ConstructorBody,
)
qvtoperational::MappingBody_strategy = st.builds(
    qvtoperational::MappingBody,
)
emof::Comment_strategy = st.builds(
    emof::Comment,
)
Extent_strategy = st.builds(
    Extent,
)
emof::URIExtent_strategy = st.builds(
    emof::URIExtent,
)
Parameter_strategy = st.builds(
    Parameter,
)
qvtoperational::VarParameter_strategy = st.builds(
    qvtoperational::VarParameter,
    kind=
        safe_text
)
qvtbase::FunctionParameter_strategy = st.builds(
    qvtbase::FunctionParameter,
)
Enumeration_strategy = st.builds(
    Enumeration,
)
Package_strategy = st.builds(
    Package,
)
qvtoperational::Module_strategy = st.builds(
    qvtoperational::Module,
    isBlackbox=
        safe_text
)
qvtbase::Transformation_strategy = st.builds(
    qvtbase::Transformation,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
emof::EnumerationLiteral_strategy = st.builds(
    emof::EnumerationLiteral,
)
qvtbase::TypedModel_strategy = st.builds(
    qvtbase::TypedModel,
)
qvtbase::Domain_strategy = st.builds(
    qvtbase::Domain,
    isCheckable=
        safe_text,
    isEnforceable=
        safe_text
)
qvtbase::Rule_strategy = st.builds(
    qvtbase::Rule,
)
emof::Type_strategy = st.builds(
    emof::Type,
)
emof::TypedElement_strategy = st.builds(
    emof::TypedElement,
)
emof::Package_strategy = st.builds(
    emof::Package,
    uri=
        safe_text
)
emof::MultiplicityElement_strategy = st.builds(
    emof::MultiplicityElement,
    lower=
        safe_text,
    isUnique=
        safe_text,
    upper=
        safe_text,
    isOrdered=
        safe_text
)
imperativeocl::ListType_strategy = st.builds(
    imperativeocl::ListType,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
essentialocl::Variable_strategy = st.builds(
    essentialocl::Variable,
)
essentialocl::TupleLiteralPart_strategy = st.builds(
    essentialocl::TupleLiteralPart,
)
essentialocl::CollectionLiteralPart_strategy = st.builds(
    essentialocl::CollectionLiteralPart,
)
essentialocl::OclExpression_strategy = st.builds(
    essentialocl::OclExpression,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
emof::Parameter_strategy = st.builds(
    emof::Parameter,
)
emof::Property_strategy = st.builds(
    emof::Property,
    isId=
        safe_text,
    default=
        safe_text,
    isReadOnly=
        safe_text,
    isComposite=
        safe_text,
    isDerived=
        safe_text
)
emof::Operation_strategy = st.builds(
    emof::Operation,
)
emof::Object_strategy = st.builds(
    emof::Object,
)
emof::NamedElement_strategy = st.builds(
    emof::NamedElement,
    name=
        safe_text
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
essentialocl::CollectionType_strategy = st.builds(
    essentialocl::CollectionType,
)
emof::PrimitiveType_strategy = st.builds(
    emof::PrimitiveType,
)
essentialocl::TupleType_strategy = st.builds(
    essentialocl::TupleType,
)
emof::Enumeration_strategy = st.builds(
    emof::Enumeration,
)
Module_strategy = st.builds(
    Module,
)
qvtoperational::Library_strategy = st.builds(
    qvtoperational::Library,
)
qvtoperational::OperationalTransformation_strategy = st.builds(
    qvtoperational::OperationalTransformation,
)
Transformation_strategy = st.builds(
    Transformation,
)
qvtrelation::RelationalTransformation_strategy = st.builds(
    qvtrelation::RelationalTransformation,
)
emof::Tag_strategy = st.builds(
    emof::Tag,
    value=
        safe_text,
    name=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
Tag_strategy = st.builds(
    Tag,
)
Object_strategy = st.builds(
    Object,
)
emof::Extent_strategy = st.builds(
    emof::Extent,
)
emof::Element_strategy = st.builds(
    emof::Element,
)
Operation_strategy = st.builds(
    Operation,
)
qvtbase::Function_strategy = st.builds(
    qvtbase::Function,
)
qvtoperational::ImperativeOperation_strategy = st.builds(
    qvtoperational::ImperativeOperation,
    isBlackbox=
        safe_text
)
qvtoperational::MappingOperation_strategy = st.builds(
    qvtoperational::MappingOperation,
)
imperativeocl::AnonymousTupleLiteralPart_strategy = st.builds(
    imperativeocl::AnonymousTupleLiteralPart,
)
AnonymousTupleLiteralPart_strategy = st.builds(
    AnonymousTupleLiteralPart,
)
imperativeocl::AnonymousTupleLiteralExp_strategy = st.builds(
    imperativeocl::AnonymousTupleLiteralExp,
)
imperativeocl::AnonymousTupleType_strategy = st.builds(
    imperativeocl::AnonymousTupleType,
)
imperativeocl::UnpackExp_strategy = st.builds(
    imperativeocl::UnpackExp,
)
imperativeocl::ImperativeExpression_strategy = st.builds(
    imperativeocl::ImperativeExpression,
)
imperativeocl::CollectorExp_strategy = st.builds(
    imperativeocl::CollectorExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
essentialocl::IteratorExp_strategy = st.builds(
    essentialocl::IteratorExp,
)
essentialocl::IterateExp_strategy = st.builds(
    essentialocl::IterateExp,
)
imperativeocl::ImperativeLoopExp_strategy = st.builds(
    imperativeocl::ImperativeLoopExp,
)
LogExp_strategy = st.builds(
    LogExp,
)
imperativeocl::AssertExp_strategy = st.builds(
    imperativeocl::AssertExp,
    severity=
        safe_text
)
imperativeocl::TupleExp_strategy = st.builds(
    imperativeocl::TupleExp,
)
imperativeocl::ForExp_strategy = st.builds(
    imperativeocl::ForExp,
)
imperativeocl::ContinueExp_strategy = st.builds(
    imperativeocl::ContinueExp,
)
imperativeocl::LogExp_strategy = st.builds(
    imperativeocl::LogExp,
    level=
        safe_text,
    text=
        safe_text
)
imperativeocl::DictLiteralPart_strategy = st.builds(
    imperativeocl::DictLiteralPart,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
imperativeocl::DictLiteralExp_strategy = st.builds(
    imperativeocl::DictLiteralExp,
)
imperativeocl::DictionaryType_strategy = st.builds(
    imperativeocl::DictionaryType,
)
imperativeocl::InstantiationExp_strategy = st.builds(
    imperativeocl::InstantiationExp,
)
imperativeocl::Typedef_strategy = st.builds(
    imperativeocl::Typedef,
)
imperativeocl::WhileExp_strategy = st.builds(
    imperativeocl::WhileExp,
)
imperativeocl::RaiseExp_strategy = st.builds(
    imperativeocl::RaiseExp,
)
Type_strategy = st.builds(
    Type,
)
emof::Class_strategy = st.builds(
    emof::Class,
    isAbstract=
        safe_text
)
imperativeocl::TemplateParameterType_strategy = st.builds(
    imperativeocl::TemplateParameterType,
    specification=
        safe_text
)
essentialocl::AnyType_strategy = st.builds(
    essentialocl::AnyType,
)
essentialocl::InvalidType_strategy = st.builds(
    essentialocl::InvalidType,
)
emof::DataType_strategy = st.builds(
    emof::DataType,
)
essentialocl::VoidType_strategy = st.builds(
    essentialocl::VoidType,
)
imperativeocl::TryExp_strategy = st.builds(
    imperativeocl::TryExp,
)
imperativeocl::BreakExp_strategy = st.builds(
    imperativeocl::BreakExp,
)
imperativeocl::ReturnExp_strategy = st.builds(
    imperativeocl::ReturnExp,
)
imperativeocl::UnlinkExp_strategy = st.builds(
    imperativeocl::UnlinkExp,
)
imperativeocl::AltExp_strategy = st.builds(
    imperativeocl::AltExp,
)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=imperativeocl::VariableInitExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::variableinitexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::VariableInitExp)

@given(instance=imperativeocl::VariableInitExp_strategy)
def test_imperativeocl::variableinitexp_withResult_type(instance):
    assert isinstance(instance.withResult, str)


@given(instance=imperativeocl::VariableInitExp_strategy)
def test_imperativeocl::variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=imperativeocl::SwitchExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::switchexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::SwitchExp)

@given(instance=imperativeocl::BlockExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::blockexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::BlockExp)

@given(instance=imperativeocl::ComputeExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::computeexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ComputeExp)

@given(instance=imperativeocl::AssignExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::assignexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::AssignExp)

@given(instance=imperativeocl::AssignExp_strategy)
def test_imperativeocl::assignexp_isReset_type(instance):
    assert isinstance(instance.isReset, str)


@given(instance=imperativeocl::AssignExp_strategy)
def test_imperativeocl::assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=imperativeocl::ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ImperativeIterateExp)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, ObjectTemplateExp)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=qvttemplate::PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_qvttemplate::propertytemplateitem_instantiation(instance):
    assert isinstance(instance, qvttemplate::PropertyTemplateItem)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, PropertyTemplateItem)

@given(instance=TemplateExp_strategy)
@settings(max_examples=50)
def test_templateexp_instantiation(instance):
    assert isinstance(instance, TemplateExp)

@given(instance=qvttemplate::CollectionTemplateExp_strategy)
@settings(max_examples=50)
def test_qvttemplate::collectiontemplateexp_instantiation(instance):
    assert isinstance(instance, qvttemplate::CollectionTemplateExp)

@given(instance=qvttemplate::CollectionTemplateExp_strategy)
def test_qvttemplate::collectiontemplateexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=qvttemplate::CollectionTemplateExp_strategy)
def test_qvttemplate::collectiontemplateexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=qvttemplate::ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_qvttemplate::objecttemplateexp_instantiation(instance):
    assert isinstance(instance, qvttemplate::ObjectTemplateExp)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=qvttemplate::TemplateExp_strategy)
@settings(max_examples=50)
def test_qvttemplate::templateexp_instantiation(instance):
    assert isinstance(instance, qvttemplate::TemplateExp)

@given(instance=essentialocl::SetType_strategy)
@settings(max_examples=50)
def test_essentialocl::settype_instantiation(instance):
    assert isinstance(instance, essentialocl::SetType)

@given(instance=essentialocl::SequenceType_strategy)
@settings(max_examples=50)
def test_essentialocl::sequencetype_instantiation(instance):
    assert isinstance(instance, essentialocl::SequenceType)

@given(instance=essentialocl::OrderedSetType_strategy)
@settings(max_examples=50)
def test_essentialocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, essentialocl::OrderedSetType)

@given(instance=essentialocl::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl::EnumLiteralExp)

@given(instance=essentialocl::BagType_strategy)
@settings(max_examples=50)
def test_essentialocl::bagtype_instantiation(instance):
    assert isinstance(instance, essentialocl::BagType)

@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)

@given(instance=essentialocl::FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_essentialocl::featurepropertycall_instantiation(instance):
    assert isinstance(instance, essentialocl::FeaturePropertyCall)

@given(instance=essentialocl::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl::InvalidLiteralExp)

@given(instance=essentialocl::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_essentialocl::opaqueexpression_instantiation(instance):
    assert isinstance(instance, essentialocl::OpaqueExpression)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=essentialocl::ExpressionInOcl_strategy)
@settings(max_examples=50)
def test_essentialocl::expressioninocl_instantiation(instance):
    assert isinstance(instance, essentialocl::ExpressionInOcl)

@given(instance=essentialocl::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::nullliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl::NullLiteralExp)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=essentialocl::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl::TupleLiteralExp)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=essentialocl::CollectionItem_strategy)
@settings(max_examples=50)
def test_essentialocl::collectionitem_instantiation(instance):
    assert isinstance(instance, essentialocl::CollectionItem)

@given(instance=essentialocl::CollectionRange_strategy)
@settings(max_examples=50)
def test_essentialocl::collectionrange_instantiation(instance):
    assert isinstance(instance, essentialocl::CollectionRange)

@given(instance=essentialocl::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl::CollectionLiteralExp)

@given(instance=essentialocl::CollectionLiteralExp_strategy)
def test_essentialocl::collectionliteralexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=essentialocl::CollectionLiteralExp_strategy)
def test_essentialocl::collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=essentialocl::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl::PrimitiveLiteralExp)

@given(instance=essentialocl::LiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::literalexp_instantiation(instance):
    assert isinstance(instance, essentialocl::LiteralExp)

@given(instance=essentialocl::LoopExp_strategy)
@settings(max_examples=50)
def test_essentialocl::loopexp_instantiation(instance):
    assert isinstance(instance, essentialocl::LoopExp)

@given(instance=essentialocl::TypeExp_strategy)
@settings(max_examples=50)
def test_essentialocl::typeexp_instantiation(instance):
    assert isinstance(instance, essentialocl::TypeExp)

@given(instance=essentialocl::VariableExp_strategy)
@settings(max_examples=50)
def test_essentialocl::variableexp_instantiation(instance):
    assert isinstance(instance, essentialocl::VariableExp)

@given(instance=FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_featurepropertycall_instantiation(instance):
    assert isinstance(instance, FeaturePropertyCall)

@given(instance=essentialocl::OperationCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, essentialocl::OperationCallExp)

@given(instance=essentialocl::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, essentialocl::PropertyCallExp)

@given(instance=ComputeExp_strategy)
@settings(max_examples=50)
def test_computeexp_instantiation(instance):
    assert isinstance(instance, ComputeExp)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=essentialocl::CallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::callexp_instantiation(instance):
    assert isinstance(instance, essentialocl::CallExp)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=essentialocl::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::stringliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl::StringLiteralExp)

@given(instance=essentialocl::StringLiteralExp_strategy)
def test_essentialocl::stringliteralexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=essentialocl::StringLiteralExp_strategy)
def test_essentialocl::stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=essentialocl::NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::numericliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl::NumericLiteralExp)

@given(instance=essentialocl::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl::BooleanLiteralExp)

@given(instance=essentialocl::BooleanLiteralExp_strategy)
def test_essentialocl::booleanliteralexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=essentialocl::BooleanLiteralExp_strategy)
def test_essentialocl::booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=essentialocl::LetExp_strategy)
@settings(max_examples=50)
def test_essentialocl::letexp_instantiation(instance):
    assert isinstance(instance, essentialocl::LetExp)

@given(instance=essentialocl::IfExp_strategy)
@settings(max_examples=50)
def test_essentialocl::ifexp_instantiation(instance):
    assert isinstance(instance, essentialocl::IfExp)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=essentialocl::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::realliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl::RealLiteralExp)

@given(instance=essentialocl::RealLiteralExp_strategy)
def test_essentialocl::realliteralexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=essentialocl::RealLiteralExp_strategy)
def test_essentialocl::realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=essentialocl::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_essentialocl::integerliteralexp_instantiation(instance):
    assert isinstance(instance, essentialocl::IntegerLiteralExp)

@given(instance=essentialocl::IntegerLiteralExp_strategy)
def test_essentialocl::integerliteralexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=essentialocl::IntegerLiteralExp_strategy)
def test_essentialocl::integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=essentialocl::UnlimitedNaturalExp_strategy)
@settings(max_examples=50)
def test_essentialocl::unlimitednaturalexp_instantiation(instance):
    assert isinstance(instance, essentialocl::UnlimitedNaturalExp)

@given(instance=essentialocl::UnlimitedNaturalExp_strategy)
def test_essentialocl::unlimitednaturalexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=essentialocl::UnlimitedNaturalExp_strategy)
def test_essentialocl::unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=TryExp_strategy)
@settings(max_examples=50)
def test_tryexp_instantiation(instance):
    assert isinstance(instance, TryExp)

@given(instance=RelationalTransformation_strategy)
@settings(max_examples=50)
def test_relationaltransformation_instantiation(instance):
    assert isinstance(instance, RelationalTransformation)

@given(instance=qvtrelation::Key_strategy)
@settings(max_examples=50)
def test_qvtrelation::key_instantiation(instance):
    assert isinstance(instance, qvtrelation::Key)

@given(instance=qvtrelation::RelationImplementation_strategy)
@settings(max_examples=50)
def test_qvtrelation::relationimplementation_instantiation(instance):
    assert isinstance(instance, qvtrelation::RelationImplementation)

@given(instance=DomainPattern_strategy)
@settings(max_examples=50)
def test_domainpattern_instantiation(instance):
    assert isinstance(instance, DomainPattern)

@given(instance=qvtbase::Pattern_strategy)
@settings(max_examples=50)
def test_qvtbase::pattern_instantiation(instance):
    assert isinstance(instance, qvtbase::Pattern)

@given(instance=RelationImplementation_strategy)
@settings(max_examples=50)
def test_relationimplementation_instantiation(instance):
    assert isinstance(instance, RelationImplementation)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=qvtbase::Predicate_strategy)
@settings(max_examples=50)
def test_qvtbase::predicate_instantiation(instance):
    assert isinstance(instance, qvtbase::Predicate)

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=qvtcore::EnforcementOperation_strategy)
@settings(max_examples=50)
def test_qvtcore::enforcementoperation_instantiation(instance):
    assert isinstance(instance, qvtcore::EnforcementOperation)

@given(instance=qvtcore::EnforcementOperation_strategy)
def test_qvtcore::enforcementoperation_enforcementMode_type(instance):
    assert isinstance(instance.enforcementMode, str)


@given(instance=qvtcore::EnforcementOperation_strategy)
def test_qvtcore::enforcementoperation_enforcementMode_setter(instance):
    original = instance.enforcementMode
    instance.enforcementMode = original
    assert instance.enforcementMode == original

@given(instance=TypedModel_strategy)
@settings(max_examples=50)
def test_typedmodel_instantiation(instance):
    assert isinstance(instance, TypedModel)

@given(instance=qvtcore::Assignment_strategy)
@settings(max_examples=50)
def test_qvtcore::assignment_instantiation(instance):
    assert isinstance(instance, qvtcore::Assignment)

@given(instance=qvtcore::Assignment_strategy)
def test_qvtcore::assignment_isDefault_type(instance):
    assert isinstance(instance.isDefault, str)


@given(instance=qvtcore::Assignment_strategy)
def test_qvtcore::assignment_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=BottomPattern_strategy)
@settings(max_examples=50)
def test_bottompattern_instantiation(instance):
    assert isinstance(instance, BottomPattern)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=qvtrelation::DomainPattern_strategy)
@settings(max_examples=50)
def test_qvtrelation::domainpattern_instantiation(instance):
    assert isinstance(instance, qvtrelation::DomainPattern)

@given(instance=qvtcore::CorePattern_strategy)
@settings(max_examples=50)
def test_qvtcore::corepattern_instantiation(instance):
    assert isinstance(instance, qvtcore::CorePattern)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=qvtrelation::RelationDomain_strategy)
@settings(max_examples=50)
def test_qvtrelation::relationdomain_instantiation(instance):
    assert isinstance(instance, qvtrelation::RelationDomain)

@given(instance=qvtcore::RealizedVariable_strategy)
@settings(max_examples=50)
def test_qvtcore::realizedvariable_instantiation(instance):
    assert isinstance(instance, qvtcore::RealizedVariable)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=qvtrelation::Relation_strategy)
@settings(max_examples=50)
def test_qvtrelation::relation_instantiation(instance):
    assert isinstance(instance, qvtrelation::Relation)

@given(instance=qvtrelation::Relation_strategy)
def test_qvtrelation::relation_isTopLevel_type(instance):
    assert isinstance(instance.isTopLevel, str)


@given(instance=qvtrelation::Relation_strategy)
def test_qvtrelation::relation_isTopLevel_setter(instance):
    original = instance.isTopLevel
    instance.isTopLevel = original
    assert instance.isTopLevel == original

@given(instance=EnforcementOperation_strategy)
@settings(max_examples=50)
def test_enforcementoperation_instantiation(instance):
    assert isinstance(instance, EnforcementOperation)

@given(instance=RealizedVariable_strategy)
@settings(max_examples=50)
def test_realizedvariable_instantiation(instance):
    assert isinstance(instance, RealizedVariable)

@given(instance=Assignment_strategy)
@settings(max_examples=50)
def test_assignment_instantiation(instance):
    assert isinstance(instance, Assignment)

@given(instance=Area_strategy)
@settings(max_examples=50)
def test_area_instantiation(instance):
    assert isinstance(instance, Area)

@given(instance=qvtcore::Mapping_strategy)
@settings(max_examples=50)
def test_qvtcore::mapping_instantiation(instance):
    assert isinstance(instance, qvtcore::Mapping)

@given(instance=qvtcore::CoreDomain_strategy)
@settings(max_examples=50)
def test_qvtcore::coredomain_instantiation(instance):
    assert isinstance(instance, qvtcore::CoreDomain)

@given(instance=CorePattern_strategy)
@settings(max_examples=50)
def test_corepattern_instantiation(instance):
    assert isinstance(instance, CorePattern)

@given(instance=qvtcore::GuardPattern_strategy)
@settings(max_examples=50)
def test_qvtcore::guardpattern_instantiation(instance):
    assert isinstance(instance, qvtcore::GuardPattern)

@given(instance=qvtcore::BottomPattern_strategy)
@settings(max_examples=50)
def test_qvtcore::bottompattern_instantiation(instance):
    assert isinstance(instance, qvtcore::BottomPattern)

@given(instance=qvtoperational::ModuleImport_strategy)
@settings(max_examples=50)
def test_qvtoperational::moduleimport_instantiation(instance):
    assert isinstance(instance, qvtoperational::ModuleImport)

@given(instance=qvtoperational::ModuleImport_strategy)
def test_qvtoperational::moduleimport_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=qvtoperational::ModuleImport_strategy)
def test_qvtoperational::moduleimport_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=GuardPattern_strategy)
@settings(max_examples=50)
def test_guardpattern_instantiation(instance):
    assert isinstance(instance, GuardPattern)

@given(instance=qvtcore::Area_strategy)
@settings(max_examples=50)
def test_qvtcore::area_instantiation(instance):
    assert isinstance(instance, qvtcore::Area)

@given(instance=ConstructorBody_strategy)
@settings(max_examples=50)
def test_constructorbody_instantiation(instance):
    assert isinstance(instance, ConstructorBody)

@given(instance=InstantiationExp_strategy)
@settings(max_examples=50)
def test_instantiationexp_instantiation(instance):
    assert isinstance(instance, InstantiationExp)

@given(instance=qvtoperational::ObjectExp_strategy)
@settings(max_examples=50)
def test_qvtoperational::objectexp_instantiation(instance):
    assert isinstance(instance, qvtoperational::ObjectExp)

@given(instance=qvtoperational::OperationBody_strategy)
@settings(max_examples=50)
def test_qvtoperational::operationbody_instantiation(instance):
    assert isinstance(instance, qvtoperational::OperationBody)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=qvtoperational::ImperativeCallExp_strategy)
@settings(max_examples=50)
def test_qvtoperational::imperativecallexp_instantiation(instance):
    assert isinstance(instance, qvtoperational::ImperativeCallExp)

@given(instance=qvtoperational::ImperativeCallExp_strategy)
def test_qvtoperational::imperativecallexp_isVirtual_type(instance):
    assert isinstance(instance.isVirtual, str)


@given(instance=qvtoperational::ImperativeCallExp_strategy)
def test_qvtoperational::imperativecallexp_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=ModelType_strategy)
@settings(max_examples=50)
def test_modeltype_instantiation(instance):
    assert isinstance(instance, ModelType)

@given(instance=ModuleImport_strategy)
@settings(max_examples=50)
def test_moduleimport_instantiation(instance):
    assert isinstance(instance, ModuleImport)

@given(instance=URIExtent_strategy)
@settings(max_examples=50)
def test_uriextent_instantiation(instance):
    assert isinstance(instance, URIExtent)

@given(instance=qvtoperational::ModelType_strategy)
@settings(max_examples=50)
def test_qvtoperational::modeltype_instantiation(instance):
    assert isinstance(instance, qvtoperational::ModelType)

@given(instance=qvtoperational::ModelType_strategy)
def test_qvtoperational::modeltype_conformanceKind_type(instance):
    assert isinstance(instance.conformanceKind, str)


@given(instance=qvtoperational::ModelType_strategy)
def test_qvtoperational::modeltype_conformanceKind_setter(instance):
    original = instance.conformanceKind
    instance.conformanceKind = original
    assert instance.conformanceKind == original

@given(instance=EntryOperation_strategy)
@settings(max_examples=50)
def test_entryoperation_instantiation(instance):
    assert isinstance(instance, EntryOperation)

@given(instance=ModelParameter_strategy)
@settings(max_examples=50)
def test_modelparameter_instantiation(instance):
    assert isinstance(instance, ModelParameter)

@given(instance=qvtoperational::ContextualProperty_strategy)
@settings(max_examples=50)
def test_qvtoperational::contextualproperty_instantiation(instance):
    assert isinstance(instance, qvtoperational::ContextualProperty)

@given(instance=ImperativeCallExp_strategy)
@settings(max_examples=50)
def test_imperativecallexp_instantiation(instance):
    assert isinstance(instance, ImperativeCallExp)

@given(instance=qvtoperational::MappingCallExp_strategy)
@settings(max_examples=50)
def test_qvtoperational::mappingcallexp_instantiation(instance):
    assert isinstance(instance, qvtoperational::MappingCallExp)

@given(instance=qvtoperational::MappingCallExp_strategy)
def test_qvtoperational::mappingcallexp_isStrict_type(instance):
    assert isinstance(instance.isStrict, str)


@given(instance=qvtoperational::MappingCallExp_strategy)
def test_qvtoperational::mappingcallexp_isStrict_setter(instance):
    original = instance.isStrict
    instance.isStrict = original
    assert instance.isStrict == original

@given(instance=RelationDomain_strategy)
@settings(max_examples=50)
def test_relationdomain_instantiation(instance):
    assert isinstance(instance, RelationDomain)

@given(instance=VarParameter_strategy)
@settings(max_examples=50)
def test_varparameter_instantiation(instance):
    assert isinstance(instance, VarParameter)

@given(instance=qvtoperational::ModelParameter_strategy)
@settings(max_examples=50)
def test_qvtoperational::modelparameter_instantiation(instance):
    assert isinstance(instance, qvtoperational::ModelParameter)

@given(instance=qvtoperational::MappingParameter_strategy)
@settings(max_examples=50)
def test_qvtoperational::mappingparameter_instantiation(instance):
    assert isinstance(instance, qvtoperational::MappingParameter)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=MappingOperation_strategy)
@settings(max_examples=50)
def test_mappingoperation_instantiation(instance):
    assert isinstance(instance, MappingOperation)

@given(instance=ResolveExp_strategy)
@settings(max_examples=50)
def test_resolveexp_instantiation(instance):
    assert isinstance(instance, ResolveExp)

@given(instance=qvtoperational::ResolveInExp_strategy)
@settings(max_examples=50)
def test_qvtoperational::resolveinexp_instantiation(instance):
    assert isinstance(instance, qvtoperational::ResolveInExp)

@given(instance=qvtoperational::ResolveExp_strategy)
@settings(max_examples=50)
def test_qvtoperational::resolveexp_instantiation(instance):
    assert isinstance(instance, qvtoperational::ResolveExp)

@given(instance=qvtoperational::ResolveExp_strategy)
def test_qvtoperational::resolveexp_one_type(instance):
    assert isinstance(instance.one, str)


@given(instance=qvtoperational::ResolveExp_strategy)
def test_qvtoperational::resolveexp_one_setter(instance):
    original = instance.one
    instance.one = original
    assert instance.one == original

@given(instance=qvtoperational::ResolveExp_strategy)
def test_qvtoperational::resolveexp_isDeferred_type(instance):
    assert isinstance(instance.isDeferred, str)


@given(instance=qvtoperational::ResolveExp_strategy)
def test_qvtoperational::resolveexp_isDeferred_setter(instance):
    original = instance.isDeferred
    instance.isDeferred = original
    assert instance.isDeferred == original

@given(instance=qvtoperational::ResolveExp_strategy)
def test_qvtoperational::resolveexp_isInverse_type(instance):
    assert isinstance(instance.isInverse, str)


@given(instance=qvtoperational::ResolveExp_strategy)
def test_qvtoperational::resolveexp_isInverse_setter(instance):
    original = instance.isInverse
    instance.isInverse = original
    assert instance.isInverse == original

@given(instance=ImperativeOperation_strategy)
@settings(max_examples=50)
def test_imperativeoperation_instantiation(instance):
    assert isinstance(instance, ImperativeOperation)

@given(instance=qvtoperational::Constructor_strategy)
@settings(max_examples=50)
def test_qvtoperational::constructor_instantiation(instance):
    assert isinstance(instance, qvtoperational::Constructor)

@given(instance=qvtoperational::EntryOperation_strategy)
@settings(max_examples=50)
def test_qvtoperational::entryoperation_instantiation(instance):
    assert isinstance(instance, qvtoperational::EntryOperation)

@given(instance=qvtoperational::Helper_strategy)
@settings(max_examples=50)
def test_qvtoperational::helper_instantiation(instance):
    assert isinstance(instance, qvtoperational::Helper)

@given(instance=qvtoperational::Helper_strategy)
def test_qvtoperational::helper_isQuery_type(instance):
    assert isinstance(instance.isQuery, str)


@given(instance=qvtoperational::Helper_strategy)
def test_qvtoperational::helper_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=OperationBody_strategy)
@settings(max_examples=50)
def test_operationbody_instantiation(instance):
    assert isinstance(instance, OperationBody)

@given(instance=qvtoperational::ConstructorBody_strategy)
@settings(max_examples=50)
def test_qvtoperational::constructorbody_instantiation(instance):
    assert isinstance(instance, qvtoperational::ConstructorBody)

@given(instance=qvtoperational::MappingBody_strategy)
@settings(max_examples=50)
def test_qvtoperational::mappingbody_instantiation(instance):
    assert isinstance(instance, qvtoperational::MappingBody)

@given(instance=emof::Comment_strategy)
@settings(max_examples=50)
def test_emof::comment_instantiation(instance):
    assert isinstance(instance, emof::Comment)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=emof::URIExtent_strategy)
@settings(max_examples=50)
def test_emof::uriextent_instantiation(instance):
    assert isinstance(instance, emof::URIExtent)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=qvtoperational::VarParameter_strategy)
@settings(max_examples=50)
def test_qvtoperational::varparameter_instantiation(instance):
    assert isinstance(instance, qvtoperational::VarParameter)

@given(instance=qvtoperational::VarParameter_strategy)
def test_qvtoperational::varparameter_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=qvtoperational::VarParameter_strategy)
def test_qvtoperational::varparameter_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=qvtbase::FunctionParameter_strategy)
@settings(max_examples=50)
def test_qvtbase::functionparameter_instantiation(instance):
    assert isinstance(instance, qvtbase::FunctionParameter)

@given(instance=Enumeration_strategy)
@settings(max_examples=50)
def test_enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=qvtoperational::Module_strategy)
@settings(max_examples=50)
def test_qvtoperational::module_instantiation(instance):
    assert isinstance(instance, qvtoperational::Module)

@given(instance=qvtoperational::Module_strategy)
def test_qvtoperational::module_isBlackbox_type(instance):
    assert isinstance(instance.isBlackbox, str)


@given(instance=qvtoperational::Module_strategy)
def test_qvtoperational::module_isBlackbox_setter(instance):
    original = instance.isBlackbox
    instance.isBlackbox = original
    assert instance.isBlackbox == original

@given(instance=qvtbase::Transformation_strategy)
@settings(max_examples=50)
def test_qvtbase::transformation_instantiation(instance):
    assert isinstance(instance, qvtbase::Transformation)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=emof::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_emof::enumerationliteral_instantiation(instance):
    assert isinstance(instance, emof::EnumerationLiteral)

@given(instance=qvtbase::TypedModel_strategy)
@settings(max_examples=50)
def test_qvtbase::typedmodel_instantiation(instance):
    assert isinstance(instance, qvtbase::TypedModel)

@given(instance=qvtbase::Domain_strategy)
@settings(max_examples=50)
def test_qvtbase::domain_instantiation(instance):
    assert isinstance(instance, qvtbase::Domain)

@given(instance=qvtbase::Domain_strategy)
def test_qvtbase::domain_isCheckable_type(instance):
    assert isinstance(instance.isCheckable, str)


@given(instance=qvtbase::Domain_strategy)
def test_qvtbase::domain_isCheckable_setter(instance):
    original = instance.isCheckable
    instance.isCheckable = original
    assert instance.isCheckable == original

@given(instance=qvtbase::Domain_strategy)
def test_qvtbase::domain_isEnforceable_type(instance):
    assert isinstance(instance.isEnforceable, str)


@given(instance=qvtbase::Domain_strategy)
def test_qvtbase::domain_isEnforceable_setter(instance):
    original = instance.isEnforceable
    instance.isEnforceable = original
    assert instance.isEnforceable == original

@given(instance=qvtbase::Rule_strategy)
@settings(max_examples=50)
def test_qvtbase::rule_instantiation(instance):
    assert isinstance(instance, qvtbase::Rule)

@given(instance=emof::Type_strategy)
@settings(max_examples=50)
def test_emof::type_instantiation(instance):
    assert isinstance(instance, emof::Type)

@given(instance=emof::TypedElement_strategy)
@settings(max_examples=50)
def test_emof::typedelement_instantiation(instance):
    assert isinstance(instance, emof::TypedElement)

@given(instance=emof::Package_strategy)
@settings(max_examples=50)
def test_emof::package_instantiation(instance):
    assert isinstance(instance, emof::Package)

@given(instance=emof::Package_strategy)
def test_emof::package_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=emof::Package_strategy)
def test_emof::package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=emof::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_emof::multiplicityelement_instantiation(instance):
    assert isinstance(instance, emof::MultiplicityElement)

@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=emof::MultiplicityElement_strategy)
def test_emof::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=imperativeocl::ListType_strategy)
@settings(max_examples=50)
def test_imperativeocl::listtype_instantiation(instance):
    assert isinstance(instance, imperativeocl::ListType)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=essentialocl::Variable_strategy)
@settings(max_examples=50)
def test_essentialocl::variable_instantiation(instance):
    assert isinstance(instance, essentialocl::Variable)

@given(instance=essentialocl::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_essentialocl::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, essentialocl::TupleLiteralPart)

@given(instance=essentialocl::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_essentialocl::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, essentialocl::CollectionLiteralPart)

@given(instance=essentialocl::OclExpression_strategy)
@settings(max_examples=50)
def test_essentialocl::oclexpression_instantiation(instance):
    assert isinstance(instance, essentialocl::OclExpression)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=emof::Parameter_strategy)
@settings(max_examples=50)
def test_emof::parameter_instantiation(instance):
    assert isinstance(instance, emof::Parameter)

@given(instance=emof::Property_strategy)
@settings(max_examples=50)
def test_emof::property_instantiation(instance):
    assert isinstance(instance, emof::Property)

@given(instance=emof::Property_strategy)
def test_emof::property_isId_type(instance):
    assert isinstance(instance.isId, str)


@given(instance=emof::Property_strategy)
def test_emof::property_isId_setter(instance):
    original = instance.isId
    instance.isId = original
    assert instance.isId == original

@given(instance=emof::Property_strategy)
def test_emof::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=emof::Property_strategy)
def test_emof::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=emof::Property_strategy)
def test_emof::property_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, str)


@given(instance=emof::Property_strategy)
def test_emof::property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=emof::Property_strategy)
def test_emof::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, str)


@given(instance=emof::Property_strategy)
def test_emof::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=emof::Property_strategy)
def test_emof::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, str)


@given(instance=emof::Property_strategy)
def test_emof::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=emof::Operation_strategy)
@settings(max_examples=50)
def test_emof::operation_instantiation(instance):
    assert isinstance(instance, emof::Operation)

@given(instance=emof::Object_strategy)
@settings(max_examples=50)
def test_emof::object_instantiation(instance):
    assert isinstance(instance, emof::Object)

@given(instance=emof::NamedElement_strategy)
@settings(max_examples=50)
def test_emof::namedelement_instantiation(instance):
    assert isinstance(instance, emof::NamedElement)

@given(instance=emof::NamedElement_strategy)
def test_emof::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emof::NamedElement_strategy)
def test_emof::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=essentialocl::CollectionType_strategy)
@settings(max_examples=50)
def test_essentialocl::collectiontype_instantiation(instance):
    assert isinstance(instance, essentialocl::CollectionType)

@given(instance=emof::PrimitiveType_strategy)
@settings(max_examples=50)
def test_emof::primitivetype_instantiation(instance):
    assert isinstance(instance, emof::PrimitiveType)

@given(instance=essentialocl::TupleType_strategy)
@settings(max_examples=50)
def test_essentialocl::tupletype_instantiation(instance):
    assert isinstance(instance, essentialocl::TupleType)

@given(instance=emof::Enumeration_strategy)
@settings(max_examples=50)
def test_emof::enumeration_instantiation(instance):
    assert isinstance(instance, emof::Enumeration)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=qvtoperational::Library_strategy)
@settings(max_examples=50)
def test_qvtoperational::library_instantiation(instance):
    assert isinstance(instance, qvtoperational::Library)

@given(instance=qvtoperational::OperationalTransformation_strategy)
@settings(max_examples=50)
def test_qvtoperational::operationaltransformation_instantiation(instance):
    assert isinstance(instance, qvtoperational::OperationalTransformation)

@given(instance=Transformation_strategy)
@settings(max_examples=50)
def test_transformation_instantiation(instance):
    assert isinstance(instance, Transformation)

@given(instance=qvtrelation::RelationalTransformation_strategy)
@settings(max_examples=50)
def test_qvtrelation::relationaltransformation_instantiation(instance):
    assert isinstance(instance, qvtrelation::RelationalTransformation)

@given(instance=emof::Tag_strategy)
@settings(max_examples=50)
def test_emof::tag_instantiation(instance):
    assert isinstance(instance, emof::Tag)

@given(instance=emof::Tag_strategy)
def test_emof::tag_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=emof::Tag_strategy)
def test_emof::tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=emof::Tag_strategy)
def test_emof::tag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=emof::Tag_strategy)
def test_emof::tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Tag_strategy)
@settings(max_examples=50)
def test_tag_instantiation(instance):
    assert isinstance(instance, Tag)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=emof::Extent_strategy)
@settings(max_examples=50)
def test_emof::extent_instantiation(instance):
    assert isinstance(instance, emof::Extent)

@given(instance=emof::Element_strategy)
@settings(max_examples=50)
def test_emof::element_instantiation(instance):
    assert isinstance(instance, emof::Element)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=qvtbase::Function_strategy)
@settings(max_examples=50)
def test_qvtbase::function_instantiation(instance):
    assert isinstance(instance, qvtbase::Function)

@given(instance=qvtoperational::ImperativeOperation_strategy)
@settings(max_examples=50)
def test_qvtoperational::imperativeoperation_instantiation(instance):
    assert isinstance(instance, qvtoperational::ImperativeOperation)

@given(instance=qvtoperational::ImperativeOperation_strategy)
def test_qvtoperational::imperativeoperation_isBlackbox_type(instance):
    assert isinstance(instance.isBlackbox, str)


@given(instance=qvtoperational::ImperativeOperation_strategy)
def test_qvtoperational::imperativeoperation_isBlackbox_setter(instance):
    original = instance.isBlackbox
    instance.isBlackbox = original
    assert instance.isBlackbox == original

@given(instance=qvtoperational::MappingOperation_strategy)
@settings(max_examples=50)
def test_qvtoperational::mappingoperation_instantiation(instance):
    assert isinstance(instance, qvtoperational::MappingOperation)

@given(instance=imperativeocl::AnonymousTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl::anonymoustupleliteralpart_instantiation(instance):
    assert isinstance(instance, imperativeocl::AnonymousTupleLiteralPart)

@given(instance=AnonymousTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_anonymoustupleliteralpart_instantiation(instance):
    assert isinstance(instance, AnonymousTupleLiteralPart)

@given(instance=imperativeocl::AnonymousTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::anonymoustupleliteralexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::AnonymousTupleLiteralExp)

@given(instance=imperativeocl::AnonymousTupleType_strategy)
@settings(max_examples=50)
def test_imperativeocl::anonymoustupletype_instantiation(instance):
    assert isinstance(instance, imperativeocl::AnonymousTupleType)

@given(instance=imperativeocl::UnpackExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::unpackexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::UnpackExp)

@given(instance=imperativeocl::ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeexpression_instantiation(instance):
    assert isinstance(instance, imperativeocl::ImperativeExpression)

@given(instance=imperativeocl::CollectorExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::collectorexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::CollectorExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=essentialocl::IteratorExp_strategy)
@settings(max_examples=50)
def test_essentialocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, essentialocl::IteratorExp)

@given(instance=essentialocl::IterateExp_strategy)
@settings(max_examples=50)
def test_essentialocl::iterateexp_instantiation(instance):
    assert isinstance(instance, essentialocl::IterateExp)

@given(instance=imperativeocl::ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeloopexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ImperativeLoopExp)

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)

@given(instance=imperativeocl::AssertExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::assertexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::AssertExp)

@given(instance=imperativeocl::AssertExp_strategy)
def test_imperativeocl::assertexp_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=imperativeocl::AssertExp_strategy)
def test_imperativeocl::assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=imperativeocl::TupleExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::tupleexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::TupleExp)

@given(instance=imperativeocl::ForExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::forexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ForExp)

@given(instance=imperativeocl::ContinueExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::continueexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ContinueExp)

@given(instance=imperativeocl::LogExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::logexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::LogExp)

@given(instance=imperativeocl::LogExp_strategy)
def test_imperativeocl::logexp_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=imperativeocl::LogExp_strategy)
def test_imperativeocl::logexp_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=imperativeocl::LogExp_strategy)
def test_imperativeocl::logexp_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=imperativeocl::LogExp_strategy)
def test_imperativeocl::logexp_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=imperativeocl::DictLiteralPart_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictliteralpart_instantiation(instance):
    assert isinstance(instance, imperativeocl::DictLiteralPart)

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=imperativeocl::DictLiteralExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictliteralexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::DictLiteralExp)

@given(instance=imperativeocl::DictionaryType_strategy)
@settings(max_examples=50)
def test_imperativeocl::dictionarytype_instantiation(instance):
    assert isinstance(instance, imperativeocl::DictionaryType)

@given(instance=imperativeocl::InstantiationExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::instantiationexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::InstantiationExp)

@given(instance=imperativeocl::Typedef_strategy)
@settings(max_examples=50)
def test_imperativeocl::typedef_instantiation(instance):
    assert isinstance(instance, imperativeocl::Typedef)

@given(instance=imperativeocl::WhileExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::whileexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::WhileExp)

@given(instance=imperativeocl::RaiseExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::raiseexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::RaiseExp)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=emof::Class_strategy)
@settings(max_examples=50)
def test_emof::class_instantiation(instance):
    assert isinstance(instance, emof::Class)

@given(instance=emof::Class_strategy)
def test_emof::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=emof::Class_strategy)
def test_emof::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=imperativeocl::TemplateParameterType_strategy)
@settings(max_examples=50)
def test_imperativeocl::templateparametertype_instantiation(instance):
    assert isinstance(instance, imperativeocl::TemplateParameterType)

@given(instance=imperativeocl::TemplateParameterType_strategy)
def test_imperativeocl::templateparametertype_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=imperativeocl::TemplateParameterType_strategy)
def test_imperativeocl::templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=essentialocl::AnyType_strategy)
@settings(max_examples=50)
def test_essentialocl::anytype_instantiation(instance):
    assert isinstance(instance, essentialocl::AnyType)

@given(instance=essentialocl::InvalidType_strategy)
@settings(max_examples=50)
def test_essentialocl::invalidtype_instantiation(instance):
    assert isinstance(instance, essentialocl::InvalidType)

@given(instance=emof::DataType_strategy)
@settings(max_examples=50)
def test_emof::datatype_instantiation(instance):
    assert isinstance(instance, emof::DataType)

@given(instance=essentialocl::VoidType_strategy)
@settings(max_examples=50)
def test_essentialocl::voidtype_instantiation(instance):
    assert isinstance(instance, essentialocl::VoidType)

@given(instance=imperativeocl::TryExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::tryexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::TryExp)

@given(instance=imperativeocl::BreakExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::breakexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::BreakExp)

@given(instance=imperativeocl::ReturnExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::returnexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::ReturnExp)

@given(instance=imperativeocl::UnlinkExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::unlinkexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::UnlinkExp)

@given(instance=imperativeocl::AltExp_strategy)
@settings(max_examples=50)
def test_imperativeocl::altexp_instantiation(instance):
    assert isinstance(instance, imperativeocl::AltExp)
