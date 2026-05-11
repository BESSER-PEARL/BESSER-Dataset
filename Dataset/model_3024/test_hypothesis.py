import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dbl::ExpandableElement,
    Module,
    QuotedCode,
    dbl::QuotedStatements,
    dbl::QuotedModuleContent,
    dbl::QuotedExpression,
    dbl::QuotedCode,
    dbl::MappingPart,
    StructuredPropertyType,
    dbl::ReferencePropertyType,
    dbl::CompositePropertyType,
    MappingPart,
    dbl::DynamicMappingPart,
    dbl::FixedMappingPart,
    RhsExpression,
    dbl::OptionalExpr,
    dbl::SequenceExpr,
    dbl::RuleExpr,
    PropertyType,
    dbl::StructuredPropertyType,
    dbl::IntPropertyType,
    dbl::StringPropertyType,
    dbl::BooleanPropertyType,
    dbl::IdPropertyType,
    dbl::PropertyType,
    dbl::TerminalExpr,
    dbl::AlternativeExpr,
    dbl::ArbitraryExpr,
    dbl::AtLeastOneExpr,
    dbl::RuntimeExpr,
    dbl::RhsExpression,
    dbl::TextualSyntaxDef,
    ExtensibleElement,
    VariableAccess,
    dbl::MetaAccess,
    ElementAccess,
    dbl::PredefinedId,
    dbl::DepIdentifiableElement,
    SetOp,
    dbl::LastInSet,
    dbl::AfterInSet,
    dbl::ObjectAt,
    dbl::FirstInSet,
    dbl::IndexOf,
    dbl::Contains,
    dbl::BeforeInSet,
    dbl::SizeOfSet,
    PredefinedId,
    dbl::MetaLiteral,
    dbl::TypeLiteral,
    dbl::SuperLiteral,
    dbl::SetOp,
    dbl::MeLiteral,
    Expression,
    dbl::MetaExpr,
    dbl::ElementAccess,
    dbl::EvalExpr,
    dbl::CodeQuoteExpression,
    dbl::L1Expr,
    L1Expr,
    dbl::ActiveLiteral,
    dbl::NullLiteral,
    dbl::IntLiteral,
    dbl::StringLiteral,
    dbl::TrueLiteral,
    dbl::DoubleLiteral,
    dbl::FalseLiteral,
    dbl::TimeLiteral,
    UnaryOperator,
    dbl::Not,
    dbl::Neg,
    BinaryOperator,
    dbl::Equal,
    dbl::Mod,
    dbl::Plus,
    dbl::InstanceOf,
    dbl::GreaterEqual,
    dbl::Mul,
    dbl::Greater,
    dbl::Or,
    dbl::Div,
    dbl::LessEqual,
    dbl::NotEqual,
    dbl::Less,
    dbl::Minus,
    dbl::And,
    dbl::UnaryOperator,
    dbl::BinaryOperator,
    CompositeStatement,
    dbl::ForEachStatement,
    dbl::ExpandSection,
    dbl::WhileStatement,
    dbl::IfStatement,
    dbl::ArgumentExpression,
    SetStatement,
    dbl::EmptySet,
    dbl::AddToSet,
    dbl::RemoveFromSet,
    Construct,
    dbl::Statement,
    dbl::CodeBlock,
    ExpandableElement,
    dbl::TypeAccess,
    dbl::NamedElement,
    Statement,
    dbl::TargetStatement,
    dbl::ConsiderIdElements,
    dbl::IncludePattern,
    dbl::PotentiallyHiddenIdElements,
    dbl::ExpandStatement,
    dbl::FindContainer,
    dbl::TestStatement,
    dbl::MappingStatement,
    StatementExpression,
    dbl::ExpandExpression,
    dbl::ProcedureCall,
    ExpressionStatement,
    dbl::DeprecatedProcedureCallStatement,
    dbl::StatementExpression,
    SimpleStatement,
    dbl::ResumeGenStatement,
    dbl::Advance,
    dbl::Terminate,
    dbl::Assignment,
    dbl::ActivateObject,
    dbl::SaveGenStatement,
    dbl::SetGenContextStatement,
    dbl::SetStatement,
    dbl::ContinueStatement,
    dbl::Reactivate,
    dbl::Print,
    dbl::BreakStatement,
    dbl::Yield,
    dbl::ResetGenContextStatement,
    dbl::Wait,
    dbl::Return,
    dbl::WaitUntil,
    dbl::ExpressionStatement,
    dbl::SimpleStatement,
    dbl::CompositeStatement,
    AbstractVariable,
    dbl::Constructor,
    ClassSimilar,
    dbl::QuotedClassContent,
    Classifier,
    dbl::AnnotationApplication,
    dbl::Interface,
    dbl::Clazz,
    ModifierExtensionsContainer,
    dbl::NativeBinding,
    ReferableRhsType,
    dbl::AnnotatableElement,
    dbl::Expression,
    dbl::VariableAccess,
    dbl::KeyValuePair,
    Type,
    dbl::Parameter,
    AnnotatableElement,
    CodeBlock,
    dbl::StartCodeBlock,
    dbl::Mapping,
    PrimitiveType,
    dbl::BoolType,
    dbl::DoubleType,
    dbl::StringType,
    dbl::IntType,
    dbl::VoidType,
    dbl::Import,
    dbl::Model,
    NamedExtensible,
    dbl::ClassContentExtension,
    dbl::ModuleContentExtension,
    dbl::Construct,
    TypedElement,
    dbl::Cast,
    dbl::CreateObject,
    dbl::IdExpr,
    dbl::ListDimension,
    dbl::PrimitiveType,
    dbl::TypedElement,
    dbl::Type,
    dbl::ModifierExtensionsContainer,
    dbl::ExtensibleElement,
    dbl::EmbeddableExtensionsContainer,
    dbl::IdResolution,
    dbl::Variable,
    dbl::ClassAugment,
    EmbeddableExtensionsContainer,
    dbl::ClassSimilar,
    NamedElement,
    dbl::PropertyBindingExpr,
    dbl::Procedure,
    dbl::Module,
    dbl::TsRule,
    dbl::NamedExtensible,
    dbl::SimpleAnnotation,
    dbl::Annotation,
    dbl::ReferableRhsType,
    dbl::ExtensionRule,
    dbl::Classifier,
    dbl::AbstractVariable,
    dbl::ExtensionDefinition,
    dbl::Pattern,
    BindingExprOpKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dbl::expandableelement_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpandableElement)


def test_dbl::expandableelement_constructor_exists():
    assert callable(dbl::ExpandableElement.__init__)


def test_dbl::expandableelement_constructor_args():
    sig = inspect.signature(dbl::ExpandableElement.__init__)
    params = list(sig.parameters.keys())



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_quotedcode_is_not_abstract():
    assert not inspect.isabstract(QuotedCode)


def test_quotedcode_constructor_exists():
    assert callable(QuotedCode.__init__)


def test_quotedcode_constructor_args():
    sig = inspect.signature(QuotedCode.__init__)
    params = list(sig.parameters.keys())



def test_dbl::quotedstatements_is_not_abstract():
    assert not inspect.isabstract(dbl::QuotedStatements)


def test_dbl::quotedstatements_constructor_exists():
    assert callable(dbl::QuotedStatements.__init__)


def test_dbl::quotedstatements_constructor_args():
    sig = inspect.signature(dbl::QuotedStatements.__init__)
    params = list(sig.parameters.keys())



def test_dbl::quotedmodulecontent_is_not_abstract():
    assert not inspect.isabstract(dbl::QuotedModuleContent)


def test_dbl::quotedmodulecontent_constructor_exists():
    assert callable(dbl::QuotedModuleContent.__init__)


def test_dbl::quotedmodulecontent_constructor_args():
    sig = inspect.signature(dbl::QuotedModuleContent.__init__)
    params = list(sig.parameters.keys())



def test_dbl::quotedexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::QuotedExpression)


def test_dbl::quotedexpression_constructor_exists():
    assert callable(dbl::QuotedExpression.__init__)


def test_dbl::quotedexpression_constructor_args():
    sig = inspect.signature(dbl::QuotedExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::quotedcode_is_not_abstract():
    assert not inspect.isabstract(dbl::QuotedCode)


def test_dbl::quotedcode_constructor_exists():
    assert callable(dbl::QuotedCode.__init__)


def test_dbl::quotedcode_constructor_args():
    sig = inspect.signature(dbl::QuotedCode.__init__)
    params = list(sig.parameters.keys())



def test_dbl::mappingpart_is_not_abstract():
    assert not inspect.isabstract(dbl::MappingPart)


def test_dbl::mappingpart_constructor_exists():
    assert callable(dbl::MappingPart.__init__)


def test_dbl::mappingpart_constructor_args():
    sig = inspect.signature(dbl::MappingPart.__init__)
    params = list(sig.parameters.keys())



def test_structuredpropertytype_is_not_abstract():
    assert not inspect.isabstract(StructuredPropertyType)


def test_structuredpropertytype_constructor_exists():
    assert callable(StructuredPropertyType.__init__)


def test_structuredpropertytype_constructor_args():
    sig = inspect.signature(StructuredPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::referencepropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl::ReferencePropertyType)


def test_dbl::referencepropertytype_constructor_exists():
    assert callable(dbl::ReferencePropertyType.__init__)


def test_dbl::referencepropertytype_constructor_args():
    sig = inspect.signature(dbl::ReferencePropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "rawReference" in params, "Missing parameter 'rawReference'"

def test_dbl::referencepropertytype_has_rawReference():
    assert hasattr(dbl::ReferencePropertyType, "rawReference")
    descriptor = None
    for klass in dbl::ReferencePropertyType.__mro__:
        if "rawReference" in klass.__dict__:
            descriptor = klass.__dict__["rawReference"]
            break
    assert isinstance(descriptor, property)



def test_dbl::compositepropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl::CompositePropertyType)


def test_dbl::compositepropertytype_constructor_exists():
    assert callable(dbl::CompositePropertyType.__init__)


def test_dbl::compositepropertytype_constructor_args():
    sig = inspect.signature(dbl::CompositePropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"

def test_dbl::compositepropertytype_has_list():
    assert hasattr(dbl::CompositePropertyType, "list")
    descriptor = None
    for klass in dbl::CompositePropertyType.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_mappingpart_is_not_abstract():
    assert not inspect.isabstract(MappingPart)


def test_mappingpart_constructor_exists():
    assert callable(MappingPart.__init__)


def test_mappingpart_constructor_args():
    sig = inspect.signature(MappingPart.__init__)
    params = list(sig.parameters.keys())



def test_dbl::dynamicmappingpart_is_not_abstract():
    assert not inspect.isabstract(dbl::DynamicMappingPart)


def test_dbl::dynamicmappingpart_constructor_exists():
    assert callable(dbl::DynamicMappingPart.__init__)


def test_dbl::dynamicmappingpart_constructor_args():
    sig = inspect.signature(dbl::DynamicMappingPart.__init__)
    params = list(sig.parameters.keys())



def test_dbl::fixedmappingpart_is_not_abstract():
    assert not inspect.isabstract(dbl::FixedMappingPart)


def test_dbl::fixedmappingpart_constructor_exists():
    assert callable(dbl::FixedMappingPart.__init__)


def test_dbl::fixedmappingpart_constructor_args():
    sig = inspect.signature(dbl::FixedMappingPart.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_dbl::fixedmappingpart_has_code():
    assert hasattr(dbl::FixedMappingPart, "code")
    descriptor = None
    for klass in dbl::FixedMappingPart.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_rhsexpression_is_not_abstract():
    assert not inspect.isabstract(RhsExpression)


def test_rhsexpression_constructor_exists():
    assert callable(RhsExpression.__init__)


def test_rhsexpression_constructor_args():
    sig = inspect.signature(RhsExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::optionalexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::OptionalExpr)


def test_dbl::optionalexpr_constructor_exists():
    assert callable(dbl::OptionalExpr.__init__)


def test_dbl::optionalexpr_constructor_args():
    sig = inspect.signature(dbl::OptionalExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::sequenceexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::SequenceExpr)


def test_dbl::sequenceexpr_constructor_exists():
    assert callable(dbl::SequenceExpr.__init__)


def test_dbl::sequenceexpr_constructor_args():
    sig = inspect.signature(dbl::SequenceExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::ruleexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::RuleExpr)


def test_dbl::ruleexpr_constructor_exists():
    assert callable(dbl::RuleExpr.__init__)


def test_dbl::ruleexpr_constructor_args():
    sig = inspect.signature(dbl::RuleExpr.__init__)
    params = list(sig.parameters.keys())



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::structuredpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl::StructuredPropertyType)


def test_dbl::structuredpropertytype_constructor_exists():
    assert callable(dbl::StructuredPropertyType.__init__)


def test_dbl::structuredpropertytype_constructor_args():
    sig = inspect.signature(dbl::StructuredPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::intpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl::IntPropertyType)


def test_dbl::intpropertytype_constructor_exists():
    assert callable(dbl::IntPropertyType.__init__)


def test_dbl::intpropertytype_constructor_args():
    sig = inspect.signature(dbl::IntPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::stringpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl::StringPropertyType)


def test_dbl::stringpropertytype_constructor_exists():
    assert callable(dbl::StringPropertyType.__init__)


def test_dbl::stringpropertytype_constructor_args():
    sig = inspect.signature(dbl::StringPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::booleanpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl::BooleanPropertyType)


def test_dbl::booleanpropertytype_constructor_exists():
    assert callable(dbl::BooleanPropertyType.__init__)


def test_dbl::booleanpropertytype_constructor_args():
    sig = inspect.signature(dbl::BooleanPropertyType.__init__)
    params = list(sig.parameters.keys())
    assert "terminal" in params, "Missing parameter 'terminal'"

def test_dbl::booleanpropertytype_has_terminal():
    assert hasattr(dbl::BooleanPropertyType, "terminal")
    descriptor = None
    for klass in dbl::BooleanPropertyType.__mro__:
        if "terminal" in klass.__dict__:
            descriptor = klass.__dict__["terminal"]
            break
    assert isinstance(descriptor, property)



def test_dbl::idpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl::IdPropertyType)


def test_dbl::idpropertytype_constructor_exists():
    assert callable(dbl::IdPropertyType.__init__)


def test_dbl::idpropertytype_constructor_args():
    sig = inspect.signature(dbl::IdPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::propertytype_is_not_abstract():
    assert not inspect.isabstract(dbl::PropertyType)


def test_dbl::propertytype_constructor_exists():
    assert callable(dbl::PropertyType.__init__)


def test_dbl::propertytype_constructor_args():
    sig = inspect.signature(dbl::PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::terminalexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::TerminalExpr)


def test_dbl::terminalexpr_constructor_exists():
    assert callable(dbl::TerminalExpr.__init__)


def test_dbl::terminalexpr_constructor_args():
    sig = inspect.signature(dbl::TerminalExpr.__init__)
    params = list(sig.parameters.keys())
    assert "terminal" in params, "Missing parameter 'terminal'"

def test_dbl::terminalexpr_has_terminal():
    assert hasattr(dbl::TerminalExpr, "terminal")
    descriptor = None
    for klass in dbl::TerminalExpr.__mro__:
        if "terminal" in klass.__dict__:
            descriptor = klass.__dict__["terminal"]
            break
    assert isinstance(descriptor, property)



def test_dbl::alternativeexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::AlternativeExpr)


def test_dbl::alternativeexpr_constructor_exists():
    assert callable(dbl::AlternativeExpr.__init__)


def test_dbl::alternativeexpr_constructor_args():
    sig = inspect.signature(dbl::AlternativeExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::arbitraryexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::ArbitraryExpr)


def test_dbl::arbitraryexpr_constructor_exists():
    assert callable(dbl::ArbitraryExpr.__init__)


def test_dbl::arbitraryexpr_constructor_args():
    sig = inspect.signature(dbl::ArbitraryExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::atleastoneexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::AtLeastOneExpr)


def test_dbl::atleastoneexpr_constructor_exists():
    assert callable(dbl::AtLeastOneExpr.__init__)


def test_dbl::atleastoneexpr_constructor_args():
    sig = inspect.signature(dbl::AtLeastOneExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::runtimeexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::RuntimeExpr)


def test_dbl::runtimeexpr_constructor_exists():
    assert callable(dbl::RuntimeExpr.__init__)


def test_dbl::runtimeexpr_constructor_args():
    sig = inspect.signature(dbl::RuntimeExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::rhsexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::RhsExpression)


def test_dbl::rhsexpression_constructor_exists():
    assert callable(dbl::RhsExpression.__init__)


def test_dbl::rhsexpression_constructor_args():
    sig = inspect.signature(dbl::RhsExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::textualsyntaxdef_is_not_abstract():
    assert not inspect.isabstract(dbl::TextualSyntaxDef)


def test_dbl::textualsyntaxdef_constructor_exists():
    assert callable(dbl::TextualSyntaxDef.__init__)


def test_dbl::textualsyntaxdef_constructor_args():
    sig = inspect.signature(dbl::TextualSyntaxDef.__init__)
    params = list(sig.parameters.keys())



def test_extensibleelement_is_not_abstract():
    assert not inspect.isabstract(ExtensibleElement)


def test_extensibleelement_constructor_exists():
    assert callable(ExtensibleElement.__init__)


def test_extensibleelement_constructor_args():
    sig = inspect.signature(ExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_variableaccess_is_not_abstract():
    assert not inspect.isabstract(VariableAccess)


def test_variableaccess_constructor_exists():
    assert callable(VariableAccess.__init__)


def test_variableaccess_constructor_args():
    sig = inspect.signature(VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl::metaaccess_is_not_abstract():
    assert not inspect.isabstract(dbl::MetaAccess)


def test_dbl::metaaccess_constructor_exists():
    assert callable(dbl::MetaAccess.__init__)


def test_dbl::metaaccess_constructor_args():
    sig = inspect.signature(dbl::MetaAccess.__init__)
    params = list(sig.parameters.keys())



def test_elementaccess_is_not_abstract():
    assert not inspect.isabstract(ElementAccess)


def test_elementaccess_constructor_exists():
    assert callable(ElementAccess.__init__)


def test_elementaccess_constructor_args():
    sig = inspect.signature(ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl::predefinedid_is_not_abstract():
    assert not inspect.isabstract(dbl::PredefinedId)


def test_dbl::predefinedid_constructor_exists():
    assert callable(dbl::PredefinedId.__init__)


def test_dbl::predefinedid_constructor_args():
    sig = inspect.signature(dbl::PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_dbl::depidentifiableelement_is_not_abstract():
    assert not inspect.isabstract(dbl::DepIdentifiableElement)


def test_dbl::depidentifiableelement_constructor_exists():
    assert callable(dbl::DepIdentifiableElement.__init__)


def test_dbl::depidentifiableelement_constructor_args():
    sig = inspect.signature(dbl::DepIdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_setop_is_not_abstract():
    assert not inspect.isabstract(SetOp)


def test_setop_constructor_exists():
    assert callable(SetOp.__init__)


def test_setop_constructor_args():
    sig = inspect.signature(SetOp.__init__)
    params = list(sig.parameters.keys())



def test_dbl::lastinset_is_not_abstract():
    assert not inspect.isabstract(dbl::LastInSet)


def test_dbl::lastinset_constructor_exists():
    assert callable(dbl::LastInSet.__init__)


def test_dbl::lastinset_constructor_args():
    sig = inspect.signature(dbl::LastInSet.__init__)
    params = list(sig.parameters.keys())



def test_dbl::afterinset_is_not_abstract():
    assert not inspect.isabstract(dbl::AfterInSet)


def test_dbl::afterinset_constructor_exists():
    assert callable(dbl::AfterInSet.__init__)


def test_dbl::afterinset_constructor_args():
    sig = inspect.signature(dbl::AfterInSet.__init__)
    params = list(sig.parameters.keys())



def test_dbl::objectat_is_not_abstract():
    assert not inspect.isabstract(dbl::ObjectAt)


def test_dbl::objectat_constructor_exists():
    assert callable(dbl::ObjectAt.__init__)


def test_dbl::objectat_constructor_args():
    sig = inspect.signature(dbl::ObjectAt.__init__)
    params = list(sig.parameters.keys())



def test_dbl::firstinset_is_not_abstract():
    assert not inspect.isabstract(dbl::FirstInSet)


def test_dbl::firstinset_constructor_exists():
    assert callable(dbl::FirstInSet.__init__)


def test_dbl::firstinset_constructor_args():
    sig = inspect.signature(dbl::FirstInSet.__init__)
    params = list(sig.parameters.keys())



def test_dbl::indexof_is_not_abstract():
    assert not inspect.isabstract(dbl::IndexOf)


def test_dbl::indexof_constructor_exists():
    assert callable(dbl::IndexOf.__init__)


def test_dbl::indexof_constructor_args():
    sig = inspect.signature(dbl::IndexOf.__init__)
    params = list(sig.parameters.keys())



def test_dbl::contains_is_not_abstract():
    assert not inspect.isabstract(dbl::Contains)


def test_dbl::contains_constructor_exists():
    assert callable(dbl::Contains.__init__)


def test_dbl::contains_constructor_args():
    sig = inspect.signature(dbl::Contains.__init__)
    params = list(sig.parameters.keys())



def test_dbl::beforeinset_is_not_abstract():
    assert not inspect.isabstract(dbl::BeforeInSet)


def test_dbl::beforeinset_constructor_exists():
    assert callable(dbl::BeforeInSet.__init__)


def test_dbl::beforeinset_constructor_args():
    sig = inspect.signature(dbl::BeforeInSet.__init__)
    params = list(sig.parameters.keys())



def test_dbl::sizeofset_is_not_abstract():
    assert not inspect.isabstract(dbl::SizeOfSet)


def test_dbl::sizeofset_constructor_exists():
    assert callable(dbl::SizeOfSet.__init__)


def test_dbl::sizeofset_constructor_args():
    sig = inspect.signature(dbl::SizeOfSet.__init__)
    params = list(sig.parameters.keys())



def test_predefinedid_is_not_abstract():
    assert not inspect.isabstract(PredefinedId)


def test_predefinedid_constructor_exists():
    assert callable(PredefinedId.__init__)


def test_predefinedid_constructor_args():
    sig = inspect.signature(PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_dbl::metaliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::MetaLiteral)


def test_dbl::metaliteral_constructor_exists():
    assert callable(dbl::MetaLiteral.__init__)


def test_dbl::metaliteral_constructor_args():
    sig = inspect.signature(dbl::MetaLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::typeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::TypeLiteral)


def test_dbl::typeliteral_constructor_exists():
    assert callable(dbl::TypeLiteral.__init__)


def test_dbl::typeliteral_constructor_args():
    sig = inspect.signature(dbl::TypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::superliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::SuperLiteral)


def test_dbl::superliteral_constructor_exists():
    assert callable(dbl::SuperLiteral.__init__)


def test_dbl::superliteral_constructor_args():
    sig = inspect.signature(dbl::SuperLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::setop_is_not_abstract():
    assert not inspect.isabstract(dbl::SetOp)


def test_dbl::setop_constructor_exists():
    assert callable(dbl::SetOp.__init__)


def test_dbl::setop_constructor_args():
    sig = inspect.signature(dbl::SetOp.__init__)
    params = list(sig.parameters.keys())



def test_dbl::meliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::MeLiteral)


def test_dbl::meliteral_constructor_exists():
    assert callable(dbl::MeLiteral.__init__)


def test_dbl::meliteral_constructor_args():
    sig = inspect.signature(dbl::MeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::metaexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::MetaExpr)


def test_dbl::metaexpr_constructor_exists():
    assert callable(dbl::MetaExpr.__init__)


def test_dbl::metaexpr_constructor_args():
    sig = inspect.signature(dbl::MetaExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::elementaccess_is_not_abstract():
    assert not inspect.isabstract(dbl::ElementAccess)


def test_dbl::elementaccess_constructor_exists():
    assert callable(dbl::ElementAccess.__init__)


def test_dbl::elementaccess_constructor_args():
    sig = inspect.signature(dbl::ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl::evalexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::EvalExpr)


def test_dbl::evalexpr_constructor_exists():
    assert callable(dbl::EvalExpr.__init__)


def test_dbl::evalexpr_constructor_args():
    sig = inspect.signature(dbl::EvalExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::codequoteexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::CodeQuoteExpression)


def test_dbl::codequoteexpression_constructor_exists():
    assert callable(dbl::CodeQuoteExpression.__init__)


def test_dbl::codequoteexpression_constructor_args():
    sig = inspect.signature(dbl::CodeQuoteExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l1expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L1Expr)


def test_dbl::l1expr_constructor_exists():
    assert callable(dbl::L1Expr.__init__)


def test_dbl::l1expr_constructor_args():
    sig = inspect.signature(dbl::L1Expr.__init__)
    params = list(sig.parameters.keys())



def test_l1expr_is_not_abstract():
    assert not inspect.isabstract(L1Expr)


def test_l1expr_constructor_exists():
    assert callable(L1Expr.__init__)


def test_l1expr_constructor_args():
    sig = inspect.signature(L1Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::activeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::ActiveLiteral)


def test_dbl::activeliteral_constructor_exists():
    assert callable(dbl::ActiveLiteral.__init__)


def test_dbl::activeliteral_constructor_args():
    sig = inspect.signature(dbl::ActiveLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::nullliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::NullLiteral)


def test_dbl::nullliteral_constructor_exists():
    assert callable(dbl::NullLiteral.__init__)


def test_dbl::nullliteral_constructor_args():
    sig = inspect.signature(dbl::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::intliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::IntLiteral)


def test_dbl::intliteral_constructor_exists():
    assert callable(dbl::IntLiteral.__init__)


def test_dbl::intliteral_constructor_args():
    sig = inspect.signature(dbl::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl::intliteral_has_value():
    assert hasattr(dbl::IntLiteral, "value")
    descriptor = None
    for klass in dbl::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl::stringliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::StringLiteral)


def test_dbl::stringliteral_constructor_exists():
    assert callable(dbl::StringLiteral.__init__)


def test_dbl::stringliteral_constructor_args():
    sig = inspect.signature(dbl::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl::stringliteral_has_value():
    assert hasattr(dbl::StringLiteral, "value")
    descriptor = None
    for klass in dbl::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl::trueliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::TrueLiteral)


def test_dbl::trueliteral_constructor_exists():
    assert callable(dbl::TrueLiteral.__init__)


def test_dbl::trueliteral_constructor_args():
    sig = inspect.signature(dbl::TrueLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::DoubleLiteral)


def test_dbl::doubleliteral_constructor_exists():
    assert callable(dbl::DoubleLiteral.__init__)


def test_dbl::doubleliteral_constructor_args():
    sig = inspect.signature(dbl::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl::doubleliteral_has_value():
    assert hasattr(dbl::DoubleLiteral, "value")
    descriptor = None
    for klass in dbl::DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl::falseliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::FalseLiteral)


def test_dbl::falseliteral_constructor_exists():
    assert callable(dbl::FalseLiteral.__init__)


def test_dbl::falseliteral_constructor_args():
    sig = inspect.signature(dbl::FalseLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::timeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::TimeLiteral)


def test_dbl::timeliteral_constructor_exists():
    assert callable(dbl::TimeLiteral.__init__)


def test_dbl::timeliteral_constructor_args():
    sig = inspect.signature(dbl::TimeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl::not_is_not_abstract():
    assert not inspect.isabstract(dbl::Not)


def test_dbl::not_constructor_exists():
    assert callable(dbl::Not.__init__)


def test_dbl::not_constructor_args():
    sig = inspect.signature(dbl::Not.__init__)
    params = list(sig.parameters.keys())



def test_dbl::neg_is_not_abstract():
    assert not inspect.isabstract(dbl::Neg)


def test_dbl::neg_constructor_exists():
    assert callable(dbl::Neg.__init__)


def test_dbl::neg_constructor_args():
    sig = inspect.signature(dbl::Neg.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl::equal_is_not_abstract():
    assert not inspect.isabstract(dbl::Equal)


def test_dbl::equal_constructor_exists():
    assert callable(dbl::Equal.__init__)


def test_dbl::equal_constructor_args():
    sig = inspect.signature(dbl::Equal.__init__)
    params = list(sig.parameters.keys())



def test_dbl::mod_is_not_abstract():
    assert not inspect.isabstract(dbl::Mod)


def test_dbl::mod_constructor_exists():
    assert callable(dbl::Mod.__init__)


def test_dbl::mod_constructor_args():
    sig = inspect.signature(dbl::Mod.__init__)
    params = list(sig.parameters.keys())



def test_dbl::plus_is_not_abstract():
    assert not inspect.isabstract(dbl::Plus)


def test_dbl::plus_constructor_exists():
    assert callable(dbl::Plus.__init__)


def test_dbl::plus_constructor_args():
    sig = inspect.signature(dbl::Plus.__init__)
    params = list(sig.parameters.keys())



def test_dbl::instanceof_is_not_abstract():
    assert not inspect.isabstract(dbl::InstanceOf)


def test_dbl::instanceof_constructor_exists():
    assert callable(dbl::InstanceOf.__init__)


def test_dbl::instanceof_constructor_args():
    sig = inspect.signature(dbl::InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_dbl::greaterequal_is_not_abstract():
    assert not inspect.isabstract(dbl::GreaterEqual)


def test_dbl::greaterequal_constructor_exists():
    assert callable(dbl::GreaterEqual.__init__)


def test_dbl::greaterequal_constructor_args():
    sig = inspect.signature(dbl::GreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl::mul_is_not_abstract():
    assert not inspect.isabstract(dbl::Mul)


def test_dbl::mul_constructor_exists():
    assert callable(dbl::Mul.__init__)


def test_dbl::mul_constructor_args():
    sig = inspect.signature(dbl::Mul.__init__)
    params = list(sig.parameters.keys())



def test_dbl::greater_is_not_abstract():
    assert not inspect.isabstract(dbl::Greater)


def test_dbl::greater_constructor_exists():
    assert callable(dbl::Greater.__init__)


def test_dbl::greater_constructor_args():
    sig = inspect.signature(dbl::Greater.__init__)
    params = list(sig.parameters.keys())



def test_dbl::or_is_not_abstract():
    assert not inspect.isabstract(dbl::Or)


def test_dbl::or_constructor_exists():
    assert callable(dbl::Or.__init__)


def test_dbl::or_constructor_args():
    sig = inspect.signature(dbl::Or.__init__)
    params = list(sig.parameters.keys())



def test_dbl::div_is_not_abstract():
    assert not inspect.isabstract(dbl::Div)


def test_dbl::div_constructor_exists():
    assert callable(dbl::Div.__init__)


def test_dbl::div_constructor_args():
    sig = inspect.signature(dbl::Div.__init__)
    params = list(sig.parameters.keys())



def test_dbl::lessequal_is_not_abstract():
    assert not inspect.isabstract(dbl::LessEqual)


def test_dbl::lessequal_constructor_exists():
    assert callable(dbl::LessEqual.__init__)


def test_dbl::lessequal_constructor_args():
    sig = inspect.signature(dbl::LessEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl::notequal_is_not_abstract():
    assert not inspect.isabstract(dbl::NotEqual)


def test_dbl::notequal_constructor_exists():
    assert callable(dbl::NotEqual.__init__)


def test_dbl::notequal_constructor_args():
    sig = inspect.signature(dbl::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl::less_is_not_abstract():
    assert not inspect.isabstract(dbl::Less)


def test_dbl::less_constructor_exists():
    assert callable(dbl::Less.__init__)


def test_dbl::less_constructor_args():
    sig = inspect.signature(dbl::Less.__init__)
    params = list(sig.parameters.keys())



def test_dbl::minus_is_not_abstract():
    assert not inspect.isabstract(dbl::Minus)


def test_dbl::minus_constructor_exists():
    assert callable(dbl::Minus.__init__)


def test_dbl::minus_constructor_args():
    sig = inspect.signature(dbl::Minus.__init__)
    params = list(sig.parameters.keys())



def test_dbl::and_is_not_abstract():
    assert not inspect.isabstract(dbl::And)


def test_dbl::and_constructor_exists():
    assert callable(dbl::And.__init__)


def test_dbl::and_constructor_args():
    sig = inspect.signature(dbl::And.__init__)
    params = list(sig.parameters.keys())



def test_dbl::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(dbl::UnaryOperator)


def test_dbl::unaryoperator_constructor_exists():
    assert callable(dbl::UnaryOperator.__init__)


def test_dbl::unaryoperator_constructor_args():
    sig = inspect.signature(dbl::UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(dbl::BinaryOperator)


def test_dbl::binaryoperator_constructor_exists():
    assert callable(dbl::BinaryOperator.__init__)


def test_dbl::binaryoperator_constructor_args():
    sig = inspect.signature(dbl::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_compositestatement_is_not_abstract():
    assert not inspect.isabstract(CompositeStatement)


def test_compositestatement_constructor_exists():
    assert callable(CompositeStatement.__init__)


def test_compositestatement_constructor_args():
    sig = inspect.signature(CompositeStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::foreachstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ForEachStatement)


def test_dbl::foreachstatement_constructor_exists():
    assert callable(dbl::ForEachStatement.__init__)


def test_dbl::foreachstatement_constructor_args():
    sig = inspect.signature(dbl::ForEachStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expandsection_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpandSection)


def test_dbl::expandsection_constructor_exists():
    assert callable(dbl::ExpandSection.__init__)


def test_dbl::expandsection_constructor_args():
    sig = inspect.signature(dbl::ExpandSection.__init__)
    params = list(sig.parameters.keys())



def test_dbl::whilestatement_is_not_abstract():
    assert not inspect.isabstract(dbl::WhileStatement)


def test_dbl::whilestatement_constructor_exists():
    assert callable(dbl::WhileStatement.__init__)


def test_dbl::whilestatement_constructor_args():
    sig = inspect.signature(dbl::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::ifstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::IfStatement)


def test_dbl::ifstatement_constructor_exists():
    assert callable(dbl::IfStatement.__init__)


def test_dbl::ifstatement_constructor_args():
    sig = inspect.signature(dbl::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::argumentexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::ArgumentExpression)


def test_dbl::argumentexpression_constructor_exists():
    assert callable(dbl::ArgumentExpression.__init__)


def test_dbl::argumentexpression_constructor_args():
    sig = inspect.signature(dbl::ArgumentExpression.__init__)
    params = list(sig.parameters.keys())



def test_setstatement_is_not_abstract():
    assert not inspect.isabstract(SetStatement)


def test_setstatement_constructor_exists():
    assert callable(SetStatement.__init__)


def test_setstatement_constructor_args():
    sig = inspect.signature(SetStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::emptyset_is_not_abstract():
    assert not inspect.isabstract(dbl::EmptySet)


def test_dbl::emptyset_constructor_exists():
    assert callable(dbl::EmptySet.__init__)


def test_dbl::emptyset_constructor_args():
    sig = inspect.signature(dbl::EmptySet.__init__)
    params = list(sig.parameters.keys())



def test_dbl::addtoset_is_not_abstract():
    assert not inspect.isabstract(dbl::AddToSet)


def test_dbl::addtoset_constructor_exists():
    assert callable(dbl::AddToSet.__init__)


def test_dbl::addtoset_constructor_args():
    sig = inspect.signature(dbl::AddToSet.__init__)
    params = list(sig.parameters.keys())



def test_dbl::removefromset_is_not_abstract():
    assert not inspect.isabstract(dbl::RemoveFromSet)


def test_dbl::removefromset_constructor_exists():
    assert callable(dbl::RemoveFromSet.__init__)


def test_dbl::removefromset_constructor_args():
    sig = inspect.signature(dbl::RemoveFromSet.__init__)
    params = list(sig.parameters.keys())



def test_construct_is_not_abstract():
    assert not inspect.isabstract(Construct)


def test_construct_constructor_exists():
    assert callable(Construct.__init__)


def test_construct_constructor_args():
    sig = inspect.signature(Construct.__init__)
    params = list(sig.parameters.keys())



def test_dbl::statement_is_not_abstract():
    assert not inspect.isabstract(dbl::Statement)


def test_dbl::statement_constructor_exists():
    assert callable(dbl::Statement.__init__)


def test_dbl::statement_constructor_args():
    sig = inspect.signature(dbl::Statement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::codeblock_is_not_abstract():
    assert not inspect.isabstract(dbl::CodeBlock)


def test_dbl::codeblock_constructor_exists():
    assert callable(dbl::CodeBlock.__init__)


def test_dbl::codeblock_constructor_args():
    sig = inspect.signature(dbl::CodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_expandableelement_is_not_abstract():
    assert not inspect.isabstract(ExpandableElement)


def test_expandableelement_constructor_exists():
    assert callable(ExpandableElement.__init__)


def test_expandableelement_constructor_args():
    sig = inspect.signature(ExpandableElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::typeaccess_is_not_abstract():
    assert not inspect.isabstract(dbl::TypeAccess)


def test_dbl::typeaccess_constructor_exists():
    assert callable(dbl::TypeAccess.__init__)


def test_dbl::typeaccess_constructor_args():
    sig = inspect.signature(dbl::TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl::namedelement_is_not_abstract():
    assert not inspect.isabstract(dbl::NamedElement)


def test_dbl::namedelement_constructor_exists():
    assert callable(dbl::NamedElement.__init__)


def test_dbl::namedelement_constructor_args():
    sig = inspect.signature(dbl::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dbl::namedelement_has_name():
    assert hasattr(dbl::NamedElement, "name")
    descriptor = None
    for klass in dbl::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::targetstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::TargetStatement)


def test_dbl::targetstatement_constructor_exists():
    assert callable(dbl::TargetStatement.__init__)


def test_dbl::targetstatement_constructor_args():
    sig = inspect.signature(dbl::TargetStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::consideridelements_is_not_abstract():
    assert not inspect.isabstract(dbl::ConsiderIdElements)


def test_dbl::consideridelements_constructor_exists():
    assert callable(dbl::ConsiderIdElements.__init__)


def test_dbl::consideridelements_constructor_args():
    sig = inspect.signature(dbl::ConsiderIdElements.__init__)
    params = list(sig.parameters.keys())



def test_dbl::includepattern_is_not_abstract():
    assert not inspect.isabstract(dbl::IncludePattern)


def test_dbl::includepattern_constructor_exists():
    assert callable(dbl::IncludePattern.__init__)


def test_dbl::includepattern_constructor_args():
    sig = inspect.signature(dbl::IncludePattern.__init__)
    params = list(sig.parameters.keys())



def test_dbl::potentiallyhiddenidelements_is_not_abstract():
    assert not inspect.isabstract(dbl::PotentiallyHiddenIdElements)


def test_dbl::potentiallyhiddenidelements_constructor_exists():
    assert callable(dbl::PotentiallyHiddenIdElements.__init__)


def test_dbl::potentiallyhiddenidelements_constructor_args():
    sig = inspect.signature(dbl::PotentiallyHiddenIdElements.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expandstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpandStatement)


def test_dbl::expandstatement_constructor_exists():
    assert callable(dbl::ExpandStatement.__init__)


def test_dbl::expandstatement_constructor_args():
    sig = inspect.signature(dbl::ExpandStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::findcontainer_is_not_abstract():
    assert not inspect.isabstract(dbl::FindContainer)


def test_dbl::findcontainer_constructor_exists():
    assert callable(dbl::FindContainer.__init__)


def test_dbl::findcontainer_constructor_args():
    sig = inspect.signature(dbl::FindContainer.__init__)
    params = list(sig.parameters.keys())



def test_dbl::teststatement_is_not_abstract():
    assert not inspect.isabstract(dbl::TestStatement)


def test_dbl::teststatement_constructor_exists():
    assert callable(dbl::TestStatement.__init__)


def test_dbl::teststatement_constructor_args():
    sig = inspect.signature(dbl::TestStatement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl::teststatement_has_value():
    assert hasattr(dbl::TestStatement, "value")
    descriptor = None
    for klass in dbl::TestStatement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl::mappingstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::MappingStatement)


def test_dbl::mappingstatement_constructor_exists():
    assert callable(dbl::MappingStatement.__init__)


def test_dbl::mappingstatement_constructor_args():
    sig = inspect.signature(dbl::MappingStatement.__init__)
    params = list(sig.parameters.keys())



def test_statementexpression_is_not_abstract():
    assert not inspect.isabstract(StatementExpression)


def test_statementexpression_constructor_exists():
    assert callable(StatementExpression.__init__)


def test_statementexpression_constructor_args():
    sig = inspect.signature(StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expandexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpandExpression)


def test_dbl::expandexpression_constructor_exists():
    assert callable(dbl::ExpandExpression.__init__)


def test_dbl::expandexpression_constructor_args():
    sig = inspect.signature(dbl::ExpandExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::procedurecall_is_not_abstract():
    assert not inspect.isabstract(dbl::ProcedureCall)


def test_dbl::procedurecall_constructor_exists():
    assert callable(dbl::ProcedureCall.__init__)


def test_dbl::procedurecall_constructor_args():
    sig = inspect.signature(dbl::ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(ExpressionStatement)


def test_expressionstatement_constructor_exists():
    assert callable(ExpressionStatement.__init__)


def test_expressionstatement_constructor_args():
    sig = inspect.signature(ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::deprecatedprocedurecallstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::DeprecatedProcedureCallStatement)


def test_dbl::deprecatedprocedurecallstatement_constructor_exists():
    assert callable(dbl::DeprecatedProcedureCallStatement.__init__)


def test_dbl::deprecatedprocedurecallstatement_constructor_args():
    sig = inspect.signature(dbl::DeprecatedProcedureCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::statementexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::StatementExpression)


def test_dbl::statementexpression_constructor_exists():
    assert callable(dbl::StatementExpression.__init__)


def test_dbl::statementexpression_constructor_args():
    sig = inspect.signature(dbl::StatementExpression.__init__)
    params = list(sig.parameters.keys())



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::resumegenstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ResumeGenStatement)


def test_dbl::resumegenstatement_constructor_exists():
    assert callable(dbl::ResumeGenStatement.__init__)


def test_dbl::resumegenstatement_constructor_args():
    sig = inspect.signature(dbl::ResumeGenStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::advance_is_not_abstract():
    assert not inspect.isabstract(dbl::Advance)


def test_dbl::advance_constructor_exists():
    assert callable(dbl::Advance.__init__)


def test_dbl::advance_constructor_args():
    sig = inspect.signature(dbl::Advance.__init__)
    params = list(sig.parameters.keys())



def test_dbl::terminate_is_not_abstract():
    assert not inspect.isabstract(dbl::Terminate)


def test_dbl::terminate_constructor_exists():
    assert callable(dbl::Terminate.__init__)


def test_dbl::terminate_constructor_args():
    sig = inspect.signature(dbl::Terminate.__init__)
    params = list(sig.parameters.keys())



def test_dbl::assignment_is_not_abstract():
    assert not inspect.isabstract(dbl::Assignment)


def test_dbl::assignment_constructor_exists():
    assert callable(dbl::Assignment.__init__)


def test_dbl::assignment_constructor_args():
    sig = inspect.signature(dbl::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_dbl::activateobject_is_not_abstract():
    assert not inspect.isabstract(dbl::ActivateObject)


def test_dbl::activateobject_constructor_exists():
    assert callable(dbl::ActivateObject.__init__)


def test_dbl::activateobject_constructor_args():
    sig = inspect.signature(dbl::ActivateObject.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_dbl::activateobject_has_priority():
    assert hasattr(dbl::ActivateObject, "priority")
    descriptor = None
    for klass in dbl::ActivateObject.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_dbl::savegenstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::SaveGenStatement)


def test_dbl::savegenstatement_constructor_exists():
    assert callable(dbl::SaveGenStatement.__init__)


def test_dbl::savegenstatement_constructor_args():
    sig = inspect.signature(dbl::SaveGenStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::setgencontextstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::SetGenContextStatement)


def test_dbl::setgencontextstatement_constructor_exists():
    assert callable(dbl::SetGenContextStatement.__init__)


def test_dbl::setgencontextstatement_constructor_args():
    sig = inspect.signature(dbl::SetGenContextStatement.__init__)
    params = list(sig.parameters.keys())
    assert "addAfterContext" in params, "Missing parameter 'addAfterContext'"

def test_dbl::setgencontextstatement_has_addAfterContext():
    assert hasattr(dbl::SetGenContextStatement, "addAfterContext")
    descriptor = None
    for klass in dbl::SetGenContextStatement.__mro__:
        if "addAfterContext" in klass.__dict__:
            descriptor = klass.__dict__["addAfterContext"]
            break
    assert isinstance(descriptor, property)



def test_dbl::setstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::SetStatement)


def test_dbl::setstatement_constructor_exists():
    assert callable(dbl::SetStatement.__init__)


def test_dbl::setstatement_constructor_args():
    sig = inspect.signature(dbl::SetStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::continuestatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ContinueStatement)


def test_dbl::continuestatement_constructor_exists():
    assert callable(dbl::ContinueStatement.__init__)


def test_dbl::continuestatement_constructor_args():
    sig = inspect.signature(dbl::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::reactivate_is_not_abstract():
    assert not inspect.isabstract(dbl::Reactivate)


def test_dbl::reactivate_constructor_exists():
    assert callable(dbl::Reactivate.__init__)


def test_dbl::reactivate_constructor_args():
    sig = inspect.signature(dbl::Reactivate.__init__)
    params = list(sig.parameters.keys())



def test_dbl::print_is_not_abstract():
    assert not inspect.isabstract(dbl::Print)


def test_dbl::print_constructor_exists():
    assert callable(dbl::Print.__init__)


def test_dbl::print_constructor_args():
    sig = inspect.signature(dbl::Print.__init__)
    params = list(sig.parameters.keys())



def test_dbl::breakstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::BreakStatement)


def test_dbl::breakstatement_constructor_exists():
    assert callable(dbl::BreakStatement.__init__)


def test_dbl::breakstatement_constructor_args():
    sig = inspect.signature(dbl::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::yield_is_not_abstract():
    assert not inspect.isabstract(dbl::Yield)


def test_dbl::yield_constructor_exists():
    assert callable(dbl::Yield.__init__)


def test_dbl::yield_constructor_args():
    sig = inspect.signature(dbl::Yield.__init__)
    params = list(sig.parameters.keys())



def test_dbl::resetgencontextstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ResetGenContextStatement)


def test_dbl::resetgencontextstatement_constructor_exists():
    assert callable(dbl::ResetGenContextStatement.__init__)


def test_dbl::resetgencontextstatement_constructor_args():
    sig = inspect.signature(dbl::ResetGenContextStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::wait_is_not_abstract():
    assert not inspect.isabstract(dbl::Wait)


def test_dbl::wait_constructor_exists():
    assert callable(dbl::Wait.__init__)


def test_dbl::wait_constructor_args():
    sig = inspect.signature(dbl::Wait.__init__)
    params = list(sig.parameters.keys())



def test_dbl::return_is_not_abstract():
    assert not inspect.isabstract(dbl::Return)


def test_dbl::return_constructor_exists():
    assert callable(dbl::Return.__init__)


def test_dbl::return_constructor_args():
    sig = inspect.signature(dbl::Return.__init__)
    params = list(sig.parameters.keys())



def test_dbl::waituntil_is_not_abstract():
    assert not inspect.isabstract(dbl::WaitUntil)


def test_dbl::waituntil_constructor_exists():
    assert callable(dbl::WaitUntil.__init__)


def test_dbl::waituntil_constructor_args():
    sig = inspect.signature(dbl::WaitUntil.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpressionStatement)


def test_dbl::expressionstatement_constructor_exists():
    assert callable(dbl::ExpressionStatement.__init__)


def test_dbl::expressionstatement_constructor_args():
    sig = inspect.signature(dbl::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::simplestatement_is_not_abstract():
    assert not inspect.isabstract(dbl::SimpleStatement)


def test_dbl::simplestatement_constructor_exists():
    assert callable(dbl::SimpleStatement.__init__)


def test_dbl::simplestatement_constructor_args():
    sig = inspect.signature(dbl::SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::compositestatement_is_not_abstract():
    assert not inspect.isabstract(dbl::CompositeStatement)


def test_dbl::compositestatement_constructor_exists():
    assert callable(dbl::CompositeStatement.__init__)


def test_dbl::compositestatement_constructor_args():
    sig = inspect.signature(dbl::CompositeStatement.__init__)
    params = list(sig.parameters.keys())



def test_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_dbl::constructor_is_not_abstract():
    assert not inspect.isabstract(dbl::Constructor)


def test_dbl::constructor_constructor_exists():
    assert callable(dbl::Constructor.__init__)


def test_dbl::constructor_constructor_args():
    sig = inspect.signature(dbl::Constructor.__init__)
    params = list(sig.parameters.keys())



def test_classsimilar_is_not_abstract():
    assert not inspect.isabstract(ClassSimilar)


def test_classsimilar_constructor_exists():
    assert callable(ClassSimilar.__init__)


def test_classsimilar_constructor_args():
    sig = inspect.signature(ClassSimilar.__init__)
    params = list(sig.parameters.keys())



def test_dbl::quotedclasscontent_is_not_abstract():
    assert not inspect.isabstract(dbl::QuotedClassContent)


def test_dbl::quotedclasscontent_constructor_exists():
    assert callable(dbl::QuotedClassContent.__init__)


def test_dbl::quotedclasscontent_constructor_args():
    sig = inspect.signature(dbl::QuotedClassContent.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl::annotationapplication_is_not_abstract():
    assert not inspect.isabstract(dbl::AnnotationApplication)


def test_dbl::annotationapplication_constructor_exists():
    assert callable(dbl::AnnotationApplication.__init__)


def test_dbl::annotationapplication_constructor_args():
    sig = inspect.signature(dbl::AnnotationApplication.__init__)
    params = list(sig.parameters.keys())



def test_dbl::interface_is_not_abstract():
    assert not inspect.isabstract(dbl::Interface)


def test_dbl::interface_constructor_exists():
    assert callable(dbl::Interface.__init__)


def test_dbl::interface_constructor_args():
    sig = inspect.signature(dbl::Interface.__init__)
    params = list(sig.parameters.keys())



def test_dbl::clazz_is_not_abstract():
    assert not inspect.isabstract(dbl::Clazz)


def test_dbl::clazz_constructor_exists():
    assert callable(dbl::Clazz.__init__)


def test_dbl::clazz_constructor_args():
    sig = inspect.signature(dbl::Clazz.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_dbl::clazz_has_active():
    assert hasattr(dbl::Clazz, "active")
    descriptor = None
    for klass in dbl::Clazz.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_modifierextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(ModifierExtensionsContainer)


def test_modifierextensionscontainer_constructor_exists():
    assert callable(ModifierExtensionsContainer.__init__)


def test_modifierextensionscontainer_constructor_args():
    sig = inspect.signature(ModifierExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_dbl::nativebinding_is_not_abstract():
    assert not inspect.isabstract(dbl::NativeBinding)


def test_dbl::nativebinding_constructor_exists():
    assert callable(dbl::NativeBinding.__init__)


def test_dbl::nativebinding_constructor_args():
    sig = inspect.signature(dbl::NativeBinding.__init__)
    params = list(sig.parameters.keys())
    assert "targetLanguage" in params, "Missing parameter 'targetLanguage'"
    assert "targetType" in params, "Missing parameter 'targetType'"

def test_dbl::nativebinding_has_targetLanguage():
    assert hasattr(dbl::NativeBinding, "targetLanguage")
    descriptor = None
    for klass in dbl::NativeBinding.__mro__:
        if "targetLanguage" in klass.__dict__:
            descriptor = klass.__dict__["targetLanguage"]
            break
    assert isinstance(descriptor, property)

def test_dbl::nativebinding_has_targetType():
    assert hasattr(dbl::NativeBinding, "targetType")
    descriptor = None
    for klass in dbl::NativeBinding.__mro__:
        if "targetType" in klass.__dict__:
            descriptor = klass.__dict__["targetType"]
            break
    assert isinstance(descriptor, property)



def test_referablerhstype_is_not_abstract():
    assert not inspect.isabstract(ReferableRhsType)


def test_referablerhstype_constructor_exists():
    assert callable(ReferableRhsType.__init__)


def test_referablerhstype_constructor_args():
    sig = inspect.signature(ReferableRhsType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::annotatableelement_is_not_abstract():
    assert not inspect.isabstract(dbl::AnnotatableElement)


def test_dbl::annotatableelement_constructor_exists():
    assert callable(dbl::AnnotatableElement.__init__)


def test_dbl::annotatableelement_constructor_args():
    sig = inspect.signature(dbl::AnnotatableElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expression_is_not_abstract():
    assert not inspect.isabstract(dbl::Expression)


def test_dbl::expression_constructor_exists():
    assert callable(dbl::Expression.__init__)


def test_dbl::expression_constructor_args():
    sig = inspect.signature(dbl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::variableaccess_is_not_abstract():
    assert not inspect.isabstract(dbl::VariableAccess)


def test_dbl::variableaccess_constructor_exists():
    assert callable(dbl::VariableAccess.__init__)


def test_dbl::variableaccess_constructor_args():
    sig = inspect.signature(dbl::VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl::keyvaluepair_is_not_abstract():
    assert not inspect.isabstract(dbl::KeyValuePair)


def test_dbl::keyvaluepair_constructor_exists():
    assert callable(dbl::KeyValuePair.__init__)


def test_dbl::keyvaluepair_constructor_args():
    sig = inspect.signature(dbl::KeyValuePair.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dbl::parameter_is_not_abstract():
    assert not inspect.isabstract(dbl::Parameter)


def test_dbl::parameter_constructor_exists():
    assert callable(dbl::Parameter.__init__)


def test_dbl::parameter_constructor_args():
    sig = inspect.signature(dbl::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_annotatableelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatableElement)


def test_annotatableelement_constructor_exists():
    assert callable(AnnotatableElement.__init__)


def test_annotatableelement_constructor_args():
    sig = inspect.signature(AnnotatableElement.__init__)
    params = list(sig.parameters.keys())



def test_codeblock_is_not_abstract():
    assert not inspect.isabstract(CodeBlock)


def test_codeblock_constructor_exists():
    assert callable(CodeBlock.__init__)


def test_codeblock_constructor_args():
    sig = inspect.signature(CodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_dbl::startcodeblock_is_not_abstract():
    assert not inspect.isabstract(dbl::StartCodeBlock)


def test_dbl::startcodeblock_constructor_exists():
    assert callable(dbl::StartCodeBlock.__init__)


def test_dbl::startcodeblock_constructor_args():
    sig = inspect.signature(dbl::StartCodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_dbl::mapping_is_not_abstract():
    assert not inspect.isabstract(dbl::Mapping)


def test_dbl::mapping_constructor_exists():
    assert callable(dbl::Mapping.__init__)


def test_dbl::mapping_constructor_args():
    sig = inspect.signature(dbl::Mapping.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::booltype_is_not_abstract():
    assert not inspect.isabstract(dbl::BoolType)


def test_dbl::booltype_constructor_exists():
    assert callable(dbl::BoolType.__init__)


def test_dbl::booltype_constructor_args():
    sig = inspect.signature(dbl::BoolType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::doubletype_is_not_abstract():
    assert not inspect.isabstract(dbl::DoubleType)


def test_dbl::doubletype_constructor_exists():
    assert callable(dbl::DoubleType.__init__)


def test_dbl::doubletype_constructor_args():
    sig = inspect.signature(dbl::DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::stringtype_is_not_abstract():
    assert not inspect.isabstract(dbl::StringType)


def test_dbl::stringtype_constructor_exists():
    assert callable(dbl::StringType.__init__)


def test_dbl::stringtype_constructor_args():
    sig = inspect.signature(dbl::StringType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::inttype_is_not_abstract():
    assert not inspect.isabstract(dbl::IntType)


def test_dbl::inttype_constructor_exists():
    assert callable(dbl::IntType.__init__)


def test_dbl::inttype_constructor_args():
    sig = inspect.signature(dbl::IntType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::voidtype_is_not_abstract():
    assert not inspect.isabstract(dbl::VoidType)


def test_dbl::voidtype_constructor_exists():
    assert callable(dbl::VoidType.__init__)


def test_dbl::voidtype_constructor_args():
    sig = inspect.signature(dbl::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::import_is_not_abstract():
    assert not inspect.isabstract(dbl::Import)


def test_dbl::import_constructor_exists():
    assert callable(dbl::Import.__init__)


def test_dbl::import_constructor_args():
    sig = inspect.signature(dbl::Import.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_dbl::import_has_file():
    assert hasattr(dbl::Import, "file")
    descriptor = None
    for klass in dbl::Import.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_dbl::model_is_not_abstract():
    assert not inspect.isabstract(dbl::Model)


def test_dbl::model_constructor_exists():
    assert callable(dbl::Model.__init__)


def test_dbl::model_constructor_args():
    sig = inspect.signature(dbl::Model.__init__)
    params = list(sig.parameters.keys())



def test_namedextensible_is_not_abstract():
    assert not inspect.isabstract(NamedExtensible)


def test_namedextensible_constructor_exists():
    assert callable(NamedExtensible.__init__)


def test_namedextensible_constructor_args():
    sig = inspect.signature(NamedExtensible.__init__)
    params = list(sig.parameters.keys())



def test_dbl::classcontentextension_is_not_abstract():
    assert not inspect.isabstract(dbl::ClassContentExtension)


def test_dbl::classcontentextension_constructor_exists():
    assert callable(dbl::ClassContentExtension.__init__)


def test_dbl::classcontentextension_constructor_args():
    sig = inspect.signature(dbl::ClassContentExtension.__init__)
    params = list(sig.parameters.keys())



def test_dbl::modulecontentextension_is_not_abstract():
    assert not inspect.isabstract(dbl::ModuleContentExtension)


def test_dbl::modulecontentextension_constructor_exists():
    assert callable(dbl::ModuleContentExtension.__init__)


def test_dbl::modulecontentextension_constructor_args():
    sig = inspect.signature(dbl::ModuleContentExtension.__init__)
    params = list(sig.parameters.keys())



def test_dbl::construct_is_not_abstract():
    assert not inspect.isabstract(dbl::Construct)


def test_dbl::construct_constructor_exists():
    assert callable(dbl::Construct.__init__)


def test_dbl::construct_constructor_args():
    sig = inspect.signature(dbl::Construct.__init__)
    params = list(sig.parameters.keys())
    assert "concreteSyntax" in params, "Missing parameter 'concreteSyntax'"

def test_dbl::construct_has_concreteSyntax():
    assert hasattr(dbl::Construct, "concreteSyntax")
    descriptor = None
    for klass in dbl::Construct.__mro__:
        if "concreteSyntax" in klass.__dict__:
            descriptor = klass.__dict__["concreteSyntax"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::cast_is_not_abstract():
    assert not inspect.isabstract(dbl::Cast)


def test_dbl::cast_constructor_exists():
    assert callable(dbl::Cast.__init__)


def test_dbl::cast_constructor_args():
    sig = inspect.signature(dbl::Cast.__init__)
    params = list(sig.parameters.keys())



def test_dbl::createobject_is_not_abstract():
    assert not inspect.isabstract(dbl::CreateObject)


def test_dbl::createobject_constructor_exists():
    assert callable(dbl::CreateObject.__init__)


def test_dbl::createobject_constructor_args():
    sig = inspect.signature(dbl::CreateObject.__init__)
    params = list(sig.parameters.keys())



def test_dbl::idexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::IdExpr)


def test_dbl::idexpr_constructor_exists():
    assert callable(dbl::IdExpr.__init__)


def test_dbl::idexpr_constructor_args():
    sig = inspect.signature(dbl::IdExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::listdimension_is_not_abstract():
    assert not inspect.isabstract(dbl::ListDimension)


def test_dbl::listdimension_constructor_exists():
    assert callable(dbl::ListDimension.__init__)


def test_dbl::listdimension_constructor_args():
    sig = inspect.signature(dbl::ListDimension.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_dbl::listdimension_has_size():
    assert hasattr(dbl::ListDimension, "size")
    descriptor = None
    for klass in dbl::ListDimension.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_dbl::primitivetype_is_not_abstract():
    assert not inspect.isabstract(dbl::PrimitiveType)


def test_dbl::primitivetype_constructor_exists():
    assert callable(dbl::PrimitiveType.__init__)


def test_dbl::primitivetype_constructor_args():
    sig = inspect.signature(dbl::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::typedelement_is_not_abstract():
    assert not inspect.isabstract(dbl::TypedElement)


def test_dbl::typedelement_constructor_exists():
    assert callable(dbl::TypedElement.__init__)


def test_dbl::typedelement_constructor_args():
    sig = inspect.signature(dbl::TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "isList" in params, "Missing parameter 'isList'"

def test_dbl::typedelement_has_isList():
    assert hasattr(dbl::TypedElement, "isList")
    descriptor = None
    for klass in dbl::TypedElement.__mro__:
        if "isList" in klass.__dict__:
            descriptor = klass.__dict__["isList"]
            break
    assert isinstance(descriptor, property)



def test_dbl::type_is_not_abstract():
    assert not inspect.isabstract(dbl::Type)


def test_dbl::type_constructor_exists():
    assert callable(dbl::Type.__init__)


def test_dbl::type_constructor_args():
    sig = inspect.signature(dbl::Type.__init__)
    params = list(sig.parameters.keys())



def test_dbl::modifierextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(dbl::ModifierExtensionsContainer)


def test_dbl::modifierextensionscontainer_constructor_exists():
    assert callable(dbl::ModifierExtensionsContainer.__init__)


def test_dbl::modifierextensionscontainer_constructor_args():
    sig = inspect.signature(dbl::ModifierExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_dbl::extensibleelement_is_not_abstract():
    assert not inspect.isabstract(dbl::ExtensibleElement)


def test_dbl::extensibleelement_constructor_exists():
    assert callable(dbl::ExtensibleElement.__init__)


def test_dbl::extensibleelement_constructor_args():
    sig = inspect.signature(dbl::ExtensibleElement.__init__)
    params = list(sig.parameters.keys())
    assert "objectIsExtensionInstance" in params, "Missing parameter 'objectIsExtensionInstance'"

def test_dbl::extensibleelement_has_objectIsExtensionInstance():
    assert hasattr(dbl::ExtensibleElement, "objectIsExtensionInstance")
    descriptor = None
    for klass in dbl::ExtensibleElement.__mro__:
        if "objectIsExtensionInstance" in klass.__dict__:
            descriptor = klass.__dict__["objectIsExtensionInstance"]
            break
    assert isinstance(descriptor, property)



def test_dbl::embeddableextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(dbl::EmbeddableExtensionsContainer)


def test_dbl::embeddableextensionscontainer_constructor_exists():
    assert callable(dbl::EmbeddableExtensionsContainer.__init__)


def test_dbl::embeddableextensionscontainer_constructor_args():
    sig = inspect.signature(dbl::EmbeddableExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_dbl::idresolution_is_not_abstract():
    assert not inspect.isabstract(dbl::IdResolution)


def test_dbl::idresolution_constructor_exists():
    assert callable(dbl::IdResolution.__init__)


def test_dbl::idresolution_constructor_args():
    sig = inspect.signature(dbl::IdResolution.__init__)
    params = list(sig.parameters.keys())
    assert "metaModelPlatformURI" in params, "Missing parameter 'metaModelPlatformURI'"

def test_dbl::idresolution_has_metaModelPlatformURI():
    assert hasattr(dbl::IdResolution, "metaModelPlatformURI")
    descriptor = None
    for klass in dbl::IdResolution.__mro__:
        if "metaModelPlatformURI" in klass.__dict__:
            descriptor = klass.__dict__["metaModelPlatformURI"]
            break
    assert isinstance(descriptor, property)



def test_dbl::variable_is_not_abstract():
    assert not inspect.isabstract(dbl::Variable)


def test_dbl::variable_constructor_exists():
    assert callable(dbl::Variable.__init__)


def test_dbl::variable_constructor_args():
    sig = inspect.signature(dbl::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "control" in params, "Missing parameter 'control'"
    assert "clazz" in params, "Missing parameter 'clazz'"

def test_dbl::variable_has_control():
    assert hasattr(dbl::Variable, "control")
    descriptor = None
    for klass in dbl::Variable.__mro__:
        if "control" in klass.__dict__:
            descriptor = klass.__dict__["control"]
            break
    assert isinstance(descriptor, property)

def test_dbl::variable_has_clazz():
    assert hasattr(dbl::Variable, "clazz")
    descriptor = None
    for klass in dbl::Variable.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)



def test_dbl::classaugment_is_not_abstract():
    assert not inspect.isabstract(dbl::ClassAugment)


def test_dbl::classaugment_constructor_exists():
    assert callable(dbl::ClassAugment.__init__)


def test_dbl::classaugment_constructor_args():
    sig = inspect.signature(dbl::ClassAugment.__init__)
    params = list(sig.parameters.keys())



def test_embeddableextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(EmbeddableExtensionsContainer)


def test_embeddableextensionscontainer_constructor_exists():
    assert callable(EmbeddableExtensionsContainer.__init__)


def test_embeddableextensionscontainer_constructor_args():
    sig = inspect.signature(EmbeddableExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_dbl::classsimilar_is_not_abstract():
    assert not inspect.isabstract(dbl::ClassSimilar)


def test_dbl::classsimilar_constructor_exists():
    assert callable(dbl::ClassSimilar.__init__)


def test_dbl::classsimilar_constructor_args():
    sig = inspect.signature(dbl::ClassSimilar.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::propertybindingexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::PropertyBindingExpr)


def test_dbl::propertybindingexpr_constructor_exists():
    assert callable(dbl::PropertyBindingExpr.__init__)


def test_dbl::propertybindingexpr_constructor_args():
    sig = inspect.signature(dbl::PropertyBindingExpr.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dbl::propertybindingexpr_has_operator():
    assert hasattr(dbl::PropertyBindingExpr, "operator")
    descriptor = None
    for klass in dbl::PropertyBindingExpr.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dbl::procedure_is_not_abstract():
    assert not inspect.isabstract(dbl::Procedure)


def test_dbl::procedure_constructor_exists():
    assert callable(dbl::Procedure.__init__)


def test_dbl::procedure_constructor_args():
    sig = inspect.signature(dbl::Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "clazz" in params, "Missing parameter 'clazz'"

def test_dbl::procedure_has_clazz():
    assert hasattr(dbl::Procedure, "clazz")
    descriptor = None
    for klass in dbl::Procedure.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)



def test_dbl::module_is_not_abstract():
    assert not inspect.isabstract(dbl::Module)


def test_dbl::module_constructor_exists():
    assert callable(dbl::Module.__init__)


def test_dbl::module_constructor_args():
    sig = inspect.signature(dbl::Module.__init__)
    params = list(sig.parameters.keys())



def test_dbl::tsrule_is_not_abstract():
    assert not inspect.isabstract(dbl::TsRule)


def test_dbl::tsrule_constructor_exists():
    assert callable(dbl::TsRule.__init__)


def test_dbl::tsrule_constructor_args():
    sig = inspect.signature(dbl::TsRule.__init__)
    params = list(sig.parameters.keys())
    assert "metaClassName" in params, "Missing parameter 'metaClassName'"

def test_dbl::tsrule_has_metaClassName():
    assert hasattr(dbl::TsRule, "metaClassName")
    descriptor = None
    for klass in dbl::TsRule.__mro__:
        if "metaClassName" in klass.__dict__:
            descriptor = klass.__dict__["metaClassName"]
            break
    assert isinstance(descriptor, property)



def test_dbl::namedextensible_is_not_abstract():
    assert not inspect.isabstract(dbl::NamedExtensible)


def test_dbl::namedextensible_constructor_exists():
    assert callable(dbl::NamedExtensible.__init__)


def test_dbl::namedextensible_constructor_args():
    sig = inspect.signature(dbl::NamedExtensible.__init__)
    params = list(sig.parameters.keys())



def test_dbl::simpleannotation_is_not_abstract():
    assert not inspect.isabstract(dbl::SimpleAnnotation)


def test_dbl::simpleannotation_constructor_exists():
    assert callable(dbl::SimpleAnnotation.__init__)


def test_dbl::simpleannotation_constructor_args():
    sig = inspect.signature(dbl::SimpleAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_dbl::simpleannotation_has_value():
    assert hasattr(dbl::SimpleAnnotation, "value")
    descriptor = None
    for klass in dbl::SimpleAnnotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dbl::annotation_is_not_abstract():
    assert not inspect.isabstract(dbl::Annotation)


def test_dbl::annotation_constructor_exists():
    assert callable(dbl::Annotation.__init__)


def test_dbl::annotation_constructor_args():
    sig = inspect.signature(dbl::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dbl::referablerhstype_is_not_abstract():
    assert not inspect.isabstract(dbl::ReferableRhsType)


def test_dbl::referablerhstype_constructor_exists():
    assert callable(dbl::ReferableRhsType.__init__)


def test_dbl::referablerhstype_constructor_args():
    sig = inspect.signature(dbl::ReferableRhsType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::extensionrule_is_not_abstract():
    assert not inspect.isabstract(dbl::ExtensionRule)


def test_dbl::extensionrule_constructor_exists():
    assert callable(dbl::ExtensionRule.__init__)


def test_dbl::extensionrule_constructor_args():
    sig = inspect.signature(dbl::ExtensionRule.__init__)
    params = list(sig.parameters.keys())



def test_dbl::classifier_is_not_abstract():
    assert not inspect.isabstract(dbl::Classifier)


def test_dbl::classifier_constructor_exists():
    assert callable(dbl::Classifier.__init__)


def test_dbl::classifier_constructor_args():
    sig = inspect.signature(dbl::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl::abstractvariable_is_not_abstract():
    assert not inspect.isabstract(dbl::AbstractVariable)


def test_dbl::abstractvariable_constructor_exists():
    assert callable(dbl::AbstractVariable.__init__)


def test_dbl::abstractvariable_constructor_args():
    sig = inspect.signature(dbl::AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_dbl::extensiondefinition_is_not_abstract():
    assert not inspect.isabstract(dbl::ExtensionDefinition)


def test_dbl::extensiondefinition_constructor_exists():
    assert callable(dbl::ExtensionDefinition.__init__)


def test_dbl::extensiondefinition_constructor_args():
    sig = inspect.signature(dbl::ExtensionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dbl::pattern_is_not_abstract():
    assert not inspect.isabstract(dbl::Pattern)


def test_dbl::pattern_constructor_exists():
    assert callable(dbl::Pattern.__init__)


def test_dbl::pattern_constructor_args():
    sig = inspect.signature(dbl::Pattern.__init__)
    params = list(sig.parameters.keys())
    assert "top" in params, "Missing parameter 'top'"

def test_dbl::pattern_has_top():
    assert hasattr(dbl::Pattern, "top")
    descriptor = None
    for klass in dbl::Pattern.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)

def test_bindingexpropkind_exists():
    # Check that the Enumeration exists
    assert BindingExprOpKind is not None

def test_bindingexpropkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BindingExprOpKind]
    expected_literals = [
        "ASSIGN",
        "BOOL",
        "ADD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BindingExprOpKind"


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
dbl::ExpandableElement_strategy = st.builds(
    dbl::ExpandableElement,
)
Module_strategy = st.builds(
    Module,
)
QuotedCode_strategy = st.builds(
    QuotedCode,
)
dbl::QuotedStatements_strategy = st.builds(
    dbl::QuotedStatements,
)
dbl::QuotedModuleContent_strategy = st.builds(
    dbl::QuotedModuleContent,
)
dbl::QuotedExpression_strategy = st.builds(
    dbl::QuotedExpression,
)
dbl::QuotedCode_strategy = st.builds(
    dbl::QuotedCode,
)
dbl::MappingPart_strategy = st.builds(
    dbl::MappingPart,
)
StructuredPropertyType_strategy = st.builds(
    StructuredPropertyType,
)
dbl::ReferencePropertyType_strategy = st.builds(
    dbl::ReferencePropertyType,
    rawReference=
        st.booleans()
)
dbl::CompositePropertyType_strategy = st.builds(
    dbl::CompositePropertyType,
    list=
        st.booleans()
)
MappingPart_strategy = st.builds(
    MappingPart,
)
dbl::DynamicMappingPart_strategy = st.builds(
    dbl::DynamicMappingPart,
)
dbl::FixedMappingPart_strategy = st.builds(
    dbl::FixedMappingPart,
    code=
        safe_text
)
RhsExpression_strategy = st.builds(
    RhsExpression,
)
dbl::OptionalExpr_strategy = st.builds(
    dbl::OptionalExpr,
)
dbl::SequenceExpr_strategy = st.builds(
    dbl::SequenceExpr,
)
dbl::RuleExpr_strategy = st.builds(
    dbl::RuleExpr,
)
PropertyType_strategy = st.builds(
    PropertyType,
)
dbl::StructuredPropertyType_strategy = st.builds(
    dbl::StructuredPropertyType,
)
dbl::IntPropertyType_strategy = st.builds(
    dbl::IntPropertyType,
)
dbl::StringPropertyType_strategy = st.builds(
    dbl::StringPropertyType,
)
dbl::BooleanPropertyType_strategy = st.builds(
    dbl::BooleanPropertyType,
    terminal=
        safe_text
)
dbl::IdPropertyType_strategy = st.builds(
    dbl::IdPropertyType,
)
dbl::PropertyType_strategy = st.builds(
    dbl::PropertyType,
)
dbl::TerminalExpr_strategy = st.builds(
    dbl::TerminalExpr,
    terminal=
        safe_text
)
dbl::AlternativeExpr_strategy = st.builds(
    dbl::AlternativeExpr,
)
dbl::ArbitraryExpr_strategy = st.builds(
    dbl::ArbitraryExpr,
)
dbl::AtLeastOneExpr_strategy = st.builds(
    dbl::AtLeastOneExpr,
)
dbl::RuntimeExpr_strategy = st.builds(
    dbl::RuntimeExpr,
)
dbl::RhsExpression_strategy = st.builds(
    dbl::RhsExpression,
)
dbl::TextualSyntaxDef_strategy = st.builds(
    dbl::TextualSyntaxDef,
)
ExtensibleElement_strategy = st.builds(
    ExtensibleElement,
)
VariableAccess_strategy = st.builds(
    VariableAccess,
)
dbl::MetaAccess_strategy = st.builds(
    dbl::MetaAccess,
)
ElementAccess_strategy = st.builds(
    ElementAccess,
)
dbl::PredefinedId_strategy = st.builds(
    dbl::PredefinedId,
)
dbl::DepIdentifiableElement_strategy = st.builds(
    dbl::DepIdentifiableElement,
)
SetOp_strategy = st.builds(
    SetOp,
)
dbl::LastInSet_strategy = st.builds(
    dbl::LastInSet,
)
dbl::AfterInSet_strategy = st.builds(
    dbl::AfterInSet,
)
dbl::ObjectAt_strategy = st.builds(
    dbl::ObjectAt,
)
dbl::FirstInSet_strategy = st.builds(
    dbl::FirstInSet,
)
dbl::IndexOf_strategy = st.builds(
    dbl::IndexOf,
)
dbl::Contains_strategy = st.builds(
    dbl::Contains,
)
dbl::BeforeInSet_strategy = st.builds(
    dbl::BeforeInSet,
)
dbl::SizeOfSet_strategy = st.builds(
    dbl::SizeOfSet,
)
PredefinedId_strategy = st.builds(
    PredefinedId,
)
dbl::MetaLiteral_strategy = st.builds(
    dbl::MetaLiteral,
)
dbl::TypeLiteral_strategy = st.builds(
    dbl::TypeLiteral,
)
dbl::SuperLiteral_strategy = st.builds(
    dbl::SuperLiteral,
)
dbl::SetOp_strategy = st.builds(
    dbl::SetOp,
)
dbl::MeLiteral_strategy = st.builds(
    dbl::MeLiteral,
)
Expression_strategy = st.builds(
    Expression,
)
dbl::MetaExpr_strategy = st.builds(
    dbl::MetaExpr,
)
dbl::ElementAccess_strategy = st.builds(
    dbl::ElementAccess,
)
dbl::EvalExpr_strategy = st.builds(
    dbl::EvalExpr,
)
dbl::CodeQuoteExpression_strategy = st.builds(
    dbl::CodeQuoteExpression,
)
dbl::L1Expr_strategy = st.builds(
    dbl::L1Expr,
)
L1Expr_strategy = st.builds(
    L1Expr,
)
dbl::ActiveLiteral_strategy = st.builds(
    dbl::ActiveLiteral,
)
dbl::NullLiteral_strategy = st.builds(
    dbl::NullLiteral,
)
dbl::IntLiteral_strategy = st.builds(
    dbl::IntLiteral,
    value=
        st.integers()
)
dbl::StringLiteral_strategy = st.builds(
    dbl::StringLiteral,
    value=
        safe_text
)
dbl::TrueLiteral_strategy = st.builds(
    dbl::TrueLiteral,
)
dbl::DoubleLiteral_strategy = st.builds(
    dbl::DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dbl::FalseLiteral_strategy = st.builds(
    dbl::FalseLiteral,
)
dbl::TimeLiteral_strategy = st.builds(
    dbl::TimeLiteral,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
dbl::Not_strategy = st.builds(
    dbl::Not,
)
dbl::Neg_strategy = st.builds(
    dbl::Neg,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
dbl::Equal_strategy = st.builds(
    dbl::Equal,
)
dbl::Mod_strategy = st.builds(
    dbl::Mod,
)
dbl::Plus_strategy = st.builds(
    dbl::Plus,
)
dbl::InstanceOf_strategy = st.builds(
    dbl::InstanceOf,
)
dbl::GreaterEqual_strategy = st.builds(
    dbl::GreaterEqual,
)
dbl::Mul_strategy = st.builds(
    dbl::Mul,
)
dbl::Greater_strategy = st.builds(
    dbl::Greater,
)
dbl::Or_strategy = st.builds(
    dbl::Or,
)
dbl::Div_strategy = st.builds(
    dbl::Div,
)
dbl::LessEqual_strategy = st.builds(
    dbl::LessEqual,
)
dbl::NotEqual_strategy = st.builds(
    dbl::NotEqual,
)
dbl::Less_strategy = st.builds(
    dbl::Less,
)
dbl::Minus_strategy = st.builds(
    dbl::Minus,
)
dbl::And_strategy = st.builds(
    dbl::And,
)
dbl::UnaryOperator_strategy = st.builds(
    dbl::UnaryOperator,
)
dbl::BinaryOperator_strategy = st.builds(
    dbl::BinaryOperator,
)
CompositeStatement_strategy = st.builds(
    CompositeStatement,
)
dbl::ForEachStatement_strategy = st.builds(
    dbl::ForEachStatement,
)
dbl::ExpandSection_strategy = st.builds(
    dbl::ExpandSection,
)
dbl::WhileStatement_strategy = st.builds(
    dbl::WhileStatement,
)
dbl::IfStatement_strategy = st.builds(
    dbl::IfStatement,
)
dbl::ArgumentExpression_strategy = st.builds(
    dbl::ArgumentExpression,
)
SetStatement_strategy = st.builds(
    SetStatement,
)
dbl::EmptySet_strategy = st.builds(
    dbl::EmptySet,
)
dbl::AddToSet_strategy = st.builds(
    dbl::AddToSet,
)
dbl::RemoveFromSet_strategy = st.builds(
    dbl::RemoveFromSet,
)
Construct_strategy = st.builds(
    Construct,
)
dbl::Statement_strategy = st.builds(
    dbl::Statement,
)
dbl::CodeBlock_strategy = st.builds(
    dbl::CodeBlock,
)
ExpandableElement_strategy = st.builds(
    ExpandableElement,
)
dbl::TypeAccess_strategy = st.builds(
    dbl::TypeAccess,
)
dbl::NamedElement_strategy = st.builds(
    dbl::NamedElement,
    name=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
dbl::TargetStatement_strategy = st.builds(
    dbl::TargetStatement,
)
dbl::ConsiderIdElements_strategy = st.builds(
    dbl::ConsiderIdElements,
)
dbl::IncludePattern_strategy = st.builds(
    dbl::IncludePattern,
)
dbl::PotentiallyHiddenIdElements_strategy = st.builds(
    dbl::PotentiallyHiddenIdElements,
)
dbl::ExpandStatement_strategy = st.builds(
    dbl::ExpandStatement,
)
dbl::FindContainer_strategy = st.builds(
    dbl::FindContainer,
)
dbl::TestStatement_strategy = st.builds(
    dbl::TestStatement,
    value=
        safe_text
)
dbl::MappingStatement_strategy = st.builds(
    dbl::MappingStatement,
)
StatementExpression_strategy = st.builds(
    StatementExpression,
)
dbl::ExpandExpression_strategy = st.builds(
    dbl::ExpandExpression,
)
dbl::ProcedureCall_strategy = st.builds(
    dbl::ProcedureCall,
)
ExpressionStatement_strategy = st.builds(
    ExpressionStatement,
)
dbl::DeprecatedProcedureCallStatement_strategy = st.builds(
    dbl::DeprecatedProcedureCallStatement,
)
dbl::StatementExpression_strategy = st.builds(
    dbl::StatementExpression,
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
dbl::ResumeGenStatement_strategy = st.builds(
    dbl::ResumeGenStatement,
)
dbl::Advance_strategy = st.builds(
    dbl::Advance,
)
dbl::Terminate_strategy = st.builds(
    dbl::Terminate,
)
dbl::Assignment_strategy = st.builds(
    dbl::Assignment,
)
dbl::ActivateObject_strategy = st.builds(
    dbl::ActivateObject,
    priority=
        st.integers()
)
dbl::SaveGenStatement_strategy = st.builds(
    dbl::SaveGenStatement,
)
dbl::SetGenContextStatement_strategy = st.builds(
    dbl::SetGenContextStatement,
    addAfterContext=
        st.booleans()
)
dbl::SetStatement_strategy = st.builds(
    dbl::SetStatement,
)
dbl::ContinueStatement_strategy = st.builds(
    dbl::ContinueStatement,
)
dbl::Reactivate_strategy = st.builds(
    dbl::Reactivate,
)
dbl::Print_strategy = st.builds(
    dbl::Print,
)
dbl::BreakStatement_strategy = st.builds(
    dbl::BreakStatement,
)
dbl::Yield_strategy = st.builds(
    dbl::Yield,
)
dbl::ResetGenContextStatement_strategy = st.builds(
    dbl::ResetGenContextStatement,
)
dbl::Wait_strategy = st.builds(
    dbl::Wait,
)
dbl::Return_strategy = st.builds(
    dbl::Return,
)
dbl::WaitUntil_strategy = st.builds(
    dbl::WaitUntil,
)
dbl::ExpressionStatement_strategy = st.builds(
    dbl::ExpressionStatement,
)
dbl::SimpleStatement_strategy = st.builds(
    dbl::SimpleStatement,
)
dbl::CompositeStatement_strategy = st.builds(
    dbl::CompositeStatement,
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
dbl::Constructor_strategy = st.builds(
    dbl::Constructor,
)
ClassSimilar_strategy = st.builds(
    ClassSimilar,
)
dbl::QuotedClassContent_strategy = st.builds(
    dbl::QuotedClassContent,
)
Classifier_strategy = st.builds(
    Classifier,
)
dbl::AnnotationApplication_strategy = st.builds(
    dbl::AnnotationApplication,
)
dbl::Interface_strategy = st.builds(
    dbl::Interface,
)
dbl::Clazz_strategy = st.builds(
    dbl::Clazz,
    active=
        st.booleans()
)
ModifierExtensionsContainer_strategy = st.builds(
    ModifierExtensionsContainer,
)
dbl::NativeBinding_strategy = st.builds(
    dbl::NativeBinding,
    targetLanguage=
        safe_text,
    targetType=
        safe_text
)
ReferableRhsType_strategy = st.builds(
    ReferableRhsType,
)
dbl::AnnotatableElement_strategy = st.builds(
    dbl::AnnotatableElement,
)
dbl::Expression_strategy = st.builds(
    dbl::Expression,
)
dbl::VariableAccess_strategy = st.builds(
    dbl::VariableAccess,
)
dbl::KeyValuePair_strategy = st.builds(
    dbl::KeyValuePair,
)
Type_strategy = st.builds(
    Type,
)
dbl::Parameter_strategy = st.builds(
    dbl::Parameter,
)
AnnotatableElement_strategy = st.builds(
    AnnotatableElement,
)
CodeBlock_strategy = st.builds(
    CodeBlock,
)
dbl::StartCodeBlock_strategy = st.builds(
    dbl::StartCodeBlock,
)
dbl::Mapping_strategy = st.builds(
    dbl::Mapping,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
dbl::BoolType_strategy = st.builds(
    dbl::BoolType,
)
dbl::DoubleType_strategy = st.builds(
    dbl::DoubleType,
)
dbl::StringType_strategy = st.builds(
    dbl::StringType,
)
dbl::IntType_strategy = st.builds(
    dbl::IntType,
)
dbl::VoidType_strategy = st.builds(
    dbl::VoidType,
)
dbl::Import_strategy = st.builds(
    dbl::Import,
    file=
        safe_text
)
dbl::Model_strategy = st.builds(
    dbl::Model,
)
NamedExtensible_strategy = st.builds(
    NamedExtensible,
)
dbl::ClassContentExtension_strategy = st.builds(
    dbl::ClassContentExtension,
)
dbl::ModuleContentExtension_strategy = st.builds(
    dbl::ModuleContentExtension,
)
dbl::Construct_strategy = st.builds(
    dbl::Construct,
    concreteSyntax=
        safe_text
)
TypedElement_strategy = st.builds(
    TypedElement,
)
dbl::Cast_strategy = st.builds(
    dbl::Cast,
)
dbl::CreateObject_strategy = st.builds(
    dbl::CreateObject,
)
dbl::IdExpr_strategy = st.builds(
    dbl::IdExpr,
)
dbl::ListDimension_strategy = st.builds(
    dbl::ListDimension,
    size=
        st.integers()
)
dbl::PrimitiveType_strategy = st.builds(
    dbl::PrimitiveType,
)
dbl::TypedElement_strategy = st.builds(
    dbl::TypedElement,
    isList=
        st.booleans()
)
dbl::Type_strategy = st.builds(
    dbl::Type,
)
dbl::ModifierExtensionsContainer_strategy = st.builds(
    dbl::ModifierExtensionsContainer,
)
dbl::ExtensibleElement_strategy = st.builds(
    dbl::ExtensibleElement,
    objectIsExtensionInstance=
        st.booleans()
)
dbl::EmbeddableExtensionsContainer_strategy = st.builds(
    dbl::EmbeddableExtensionsContainer,
)
dbl::IdResolution_strategy = st.builds(
    dbl::IdResolution,
    metaModelPlatformURI=
        safe_text
)
dbl::Variable_strategy = st.builds(
    dbl::Variable,
    control=
        st.booleans(),
    clazz=
        st.booleans()
)
dbl::ClassAugment_strategy = st.builds(
    dbl::ClassAugment,
)
EmbeddableExtensionsContainer_strategy = st.builds(
    EmbeddableExtensionsContainer,
)
dbl::ClassSimilar_strategy = st.builds(
    dbl::ClassSimilar,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
dbl::PropertyBindingExpr_strategy = st.builds(
    dbl::PropertyBindingExpr,
    operator=
        safe_text
)
dbl::Procedure_strategy = st.builds(
    dbl::Procedure,
    clazz=
        st.booleans()
)
dbl::Module_strategy = st.builds(
    dbl::Module,
)
dbl::TsRule_strategy = st.builds(
    dbl::TsRule,
    metaClassName=
        safe_text
)
dbl::NamedExtensible_strategy = st.builds(
    dbl::NamedExtensible,
)
dbl::SimpleAnnotation_strategy = st.builds(
    dbl::SimpleAnnotation,
    value=
        safe_text
)
dbl::Annotation_strategy = st.builds(
    dbl::Annotation,
)
dbl::ReferableRhsType_strategy = st.builds(
    dbl::ReferableRhsType,
)
dbl::ExtensionRule_strategy = st.builds(
    dbl::ExtensionRule,
)
dbl::Classifier_strategy = st.builds(
    dbl::Classifier,
)
dbl::AbstractVariable_strategy = st.builds(
    dbl::AbstractVariable,
)
dbl::ExtensionDefinition_strategy = st.builds(
    dbl::ExtensionDefinition,
)
dbl::Pattern_strategy = st.builds(
    dbl::Pattern,
    top=
        st.booleans()
)

@given(instance=dbl::ExpandableElement_strategy)
@settings(max_examples=50)
def test_dbl::expandableelement_instantiation(instance):
    assert isinstance(instance, dbl::ExpandableElement)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=QuotedCode_strategy)
@settings(max_examples=50)
def test_quotedcode_instantiation(instance):
    assert isinstance(instance, QuotedCode)

@given(instance=dbl::QuotedStatements_strategy)
@settings(max_examples=50)
def test_dbl::quotedstatements_instantiation(instance):
    assert isinstance(instance, dbl::QuotedStatements)

@given(instance=dbl::QuotedModuleContent_strategy)
@settings(max_examples=50)
def test_dbl::quotedmodulecontent_instantiation(instance):
    assert isinstance(instance, dbl::QuotedModuleContent)

@given(instance=dbl::QuotedExpression_strategy)
@settings(max_examples=50)
def test_dbl::quotedexpression_instantiation(instance):
    assert isinstance(instance, dbl::QuotedExpression)

@given(instance=dbl::QuotedCode_strategy)
@settings(max_examples=50)
def test_dbl::quotedcode_instantiation(instance):
    assert isinstance(instance, dbl::QuotedCode)

@given(instance=dbl::MappingPart_strategy)
@settings(max_examples=50)
def test_dbl::mappingpart_instantiation(instance):
    assert isinstance(instance, dbl::MappingPart)

@given(instance=StructuredPropertyType_strategy)
@settings(max_examples=50)
def test_structuredpropertytype_instantiation(instance):
    assert isinstance(instance, StructuredPropertyType)

@given(instance=dbl::ReferencePropertyType_strategy)
@settings(max_examples=50)
def test_dbl::referencepropertytype_instantiation(instance):
    assert isinstance(instance, dbl::ReferencePropertyType)

@given(instance=dbl::ReferencePropertyType_strategy)
def test_dbl::referencepropertytype_rawReference_type(instance):
    assert isinstance(instance.rawReference, bool)


@given(instance=dbl::ReferencePropertyType_strategy)
def test_dbl::referencepropertytype_rawReference_setter(instance):
    original = instance.rawReference
    instance.rawReference = original
    assert instance.rawReference == original

@given(instance=dbl::CompositePropertyType_strategy)
@settings(max_examples=50)
def test_dbl::compositepropertytype_instantiation(instance):
    assert isinstance(instance, dbl::CompositePropertyType)

@given(instance=dbl::CompositePropertyType_strategy)
def test_dbl::compositepropertytype_list_type(instance):
    assert isinstance(instance.list, bool)


@given(instance=dbl::CompositePropertyType_strategy)
def test_dbl::compositepropertytype_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=MappingPart_strategy)
@settings(max_examples=50)
def test_mappingpart_instantiation(instance):
    assert isinstance(instance, MappingPart)

@given(instance=dbl::DynamicMappingPart_strategy)
@settings(max_examples=50)
def test_dbl::dynamicmappingpart_instantiation(instance):
    assert isinstance(instance, dbl::DynamicMappingPart)

@given(instance=dbl::FixedMappingPart_strategy)
@settings(max_examples=50)
def test_dbl::fixedmappingpart_instantiation(instance):
    assert isinstance(instance, dbl::FixedMappingPart)

@given(instance=dbl::FixedMappingPart_strategy)
def test_dbl::fixedmappingpart_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=dbl::FixedMappingPart_strategy)
def test_dbl::fixedmappingpart_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=RhsExpression_strategy)
@settings(max_examples=50)
def test_rhsexpression_instantiation(instance):
    assert isinstance(instance, RhsExpression)

@given(instance=dbl::OptionalExpr_strategy)
@settings(max_examples=50)
def test_dbl::optionalexpr_instantiation(instance):
    assert isinstance(instance, dbl::OptionalExpr)

@given(instance=dbl::SequenceExpr_strategy)
@settings(max_examples=50)
def test_dbl::sequenceexpr_instantiation(instance):
    assert isinstance(instance, dbl::SequenceExpr)

@given(instance=dbl::RuleExpr_strategy)
@settings(max_examples=50)
def test_dbl::ruleexpr_instantiation(instance):
    assert isinstance(instance, dbl::RuleExpr)

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=dbl::StructuredPropertyType_strategy)
@settings(max_examples=50)
def test_dbl::structuredpropertytype_instantiation(instance):
    assert isinstance(instance, dbl::StructuredPropertyType)

@given(instance=dbl::IntPropertyType_strategy)
@settings(max_examples=50)
def test_dbl::intpropertytype_instantiation(instance):
    assert isinstance(instance, dbl::IntPropertyType)

@given(instance=dbl::StringPropertyType_strategy)
@settings(max_examples=50)
def test_dbl::stringpropertytype_instantiation(instance):
    assert isinstance(instance, dbl::StringPropertyType)

@given(instance=dbl::BooleanPropertyType_strategy)
@settings(max_examples=50)
def test_dbl::booleanpropertytype_instantiation(instance):
    assert isinstance(instance, dbl::BooleanPropertyType)

@given(instance=dbl::BooleanPropertyType_strategy)
def test_dbl::booleanpropertytype_terminal_type(instance):
    assert isinstance(instance.terminal, str)


@given(instance=dbl::BooleanPropertyType_strategy)
def test_dbl::booleanpropertytype_terminal_setter(instance):
    original = instance.terminal
    instance.terminal = original
    assert instance.terminal == original

@given(instance=dbl::IdPropertyType_strategy)
@settings(max_examples=50)
def test_dbl::idpropertytype_instantiation(instance):
    assert isinstance(instance, dbl::IdPropertyType)

@given(instance=dbl::PropertyType_strategy)
@settings(max_examples=50)
def test_dbl::propertytype_instantiation(instance):
    assert isinstance(instance, dbl::PropertyType)

@given(instance=dbl::TerminalExpr_strategy)
@settings(max_examples=50)
def test_dbl::terminalexpr_instantiation(instance):
    assert isinstance(instance, dbl::TerminalExpr)

@given(instance=dbl::TerminalExpr_strategy)
def test_dbl::terminalexpr_terminal_type(instance):
    assert isinstance(instance.terminal, str)


@given(instance=dbl::TerminalExpr_strategy)
def test_dbl::terminalexpr_terminal_setter(instance):
    original = instance.terminal
    instance.terminal = original
    assert instance.terminal == original

@given(instance=dbl::AlternativeExpr_strategy)
@settings(max_examples=50)
def test_dbl::alternativeexpr_instantiation(instance):
    assert isinstance(instance, dbl::AlternativeExpr)

@given(instance=dbl::ArbitraryExpr_strategy)
@settings(max_examples=50)
def test_dbl::arbitraryexpr_instantiation(instance):
    assert isinstance(instance, dbl::ArbitraryExpr)

@given(instance=dbl::AtLeastOneExpr_strategy)
@settings(max_examples=50)
def test_dbl::atleastoneexpr_instantiation(instance):
    assert isinstance(instance, dbl::AtLeastOneExpr)

@given(instance=dbl::RuntimeExpr_strategy)
@settings(max_examples=50)
def test_dbl::runtimeexpr_instantiation(instance):
    assert isinstance(instance, dbl::RuntimeExpr)

@given(instance=dbl::RhsExpression_strategy)
@settings(max_examples=50)
def test_dbl::rhsexpression_instantiation(instance):
    assert isinstance(instance, dbl::RhsExpression)

@given(instance=dbl::TextualSyntaxDef_strategy)
@settings(max_examples=50)
def test_dbl::textualsyntaxdef_instantiation(instance):
    assert isinstance(instance, dbl::TextualSyntaxDef)

@given(instance=ExtensibleElement_strategy)
@settings(max_examples=50)
def test_extensibleelement_instantiation(instance):
    assert isinstance(instance, ExtensibleElement)

@given(instance=VariableAccess_strategy)
@settings(max_examples=50)
def test_variableaccess_instantiation(instance):
    assert isinstance(instance, VariableAccess)

@given(instance=dbl::MetaAccess_strategy)
@settings(max_examples=50)
def test_dbl::metaaccess_instantiation(instance):
    assert isinstance(instance, dbl::MetaAccess)

@given(instance=ElementAccess_strategy)
@settings(max_examples=50)
def test_elementaccess_instantiation(instance):
    assert isinstance(instance, ElementAccess)

@given(instance=dbl::PredefinedId_strategy)
@settings(max_examples=50)
def test_dbl::predefinedid_instantiation(instance):
    assert isinstance(instance, dbl::PredefinedId)

@given(instance=dbl::DepIdentifiableElement_strategy)
@settings(max_examples=50)
def test_dbl::depidentifiableelement_instantiation(instance):
    assert isinstance(instance, dbl::DepIdentifiableElement)

@given(instance=SetOp_strategy)
@settings(max_examples=50)
def test_setop_instantiation(instance):
    assert isinstance(instance, SetOp)

@given(instance=dbl::LastInSet_strategy)
@settings(max_examples=50)
def test_dbl::lastinset_instantiation(instance):
    assert isinstance(instance, dbl::LastInSet)

@given(instance=dbl::AfterInSet_strategy)
@settings(max_examples=50)
def test_dbl::afterinset_instantiation(instance):
    assert isinstance(instance, dbl::AfterInSet)

@given(instance=dbl::ObjectAt_strategy)
@settings(max_examples=50)
def test_dbl::objectat_instantiation(instance):
    assert isinstance(instance, dbl::ObjectAt)

@given(instance=dbl::FirstInSet_strategy)
@settings(max_examples=50)
def test_dbl::firstinset_instantiation(instance):
    assert isinstance(instance, dbl::FirstInSet)

@given(instance=dbl::IndexOf_strategy)
@settings(max_examples=50)
def test_dbl::indexof_instantiation(instance):
    assert isinstance(instance, dbl::IndexOf)

@given(instance=dbl::Contains_strategy)
@settings(max_examples=50)
def test_dbl::contains_instantiation(instance):
    assert isinstance(instance, dbl::Contains)

@given(instance=dbl::BeforeInSet_strategy)
@settings(max_examples=50)
def test_dbl::beforeinset_instantiation(instance):
    assert isinstance(instance, dbl::BeforeInSet)

@given(instance=dbl::SizeOfSet_strategy)
@settings(max_examples=50)
def test_dbl::sizeofset_instantiation(instance):
    assert isinstance(instance, dbl::SizeOfSet)

@given(instance=PredefinedId_strategy)
@settings(max_examples=50)
def test_predefinedid_instantiation(instance):
    assert isinstance(instance, PredefinedId)

@given(instance=dbl::MetaLiteral_strategy)
@settings(max_examples=50)
def test_dbl::metaliteral_instantiation(instance):
    assert isinstance(instance, dbl::MetaLiteral)

@given(instance=dbl::TypeLiteral_strategy)
@settings(max_examples=50)
def test_dbl::typeliteral_instantiation(instance):
    assert isinstance(instance, dbl::TypeLiteral)

@given(instance=dbl::SuperLiteral_strategy)
@settings(max_examples=50)
def test_dbl::superliteral_instantiation(instance):
    assert isinstance(instance, dbl::SuperLiteral)

@given(instance=dbl::SetOp_strategy)
@settings(max_examples=50)
def test_dbl::setop_instantiation(instance):
    assert isinstance(instance, dbl::SetOp)

@given(instance=dbl::MeLiteral_strategy)
@settings(max_examples=50)
def test_dbl::meliteral_instantiation(instance):
    assert isinstance(instance, dbl::MeLiteral)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dbl::MetaExpr_strategy)
@settings(max_examples=50)
def test_dbl::metaexpr_instantiation(instance):
    assert isinstance(instance, dbl::MetaExpr)

@given(instance=dbl::ElementAccess_strategy)
@settings(max_examples=50)
def test_dbl::elementaccess_instantiation(instance):
    assert isinstance(instance, dbl::ElementAccess)

@given(instance=dbl::EvalExpr_strategy)
@settings(max_examples=50)
def test_dbl::evalexpr_instantiation(instance):
    assert isinstance(instance, dbl::EvalExpr)

@given(instance=dbl::CodeQuoteExpression_strategy)
@settings(max_examples=50)
def test_dbl::codequoteexpression_instantiation(instance):
    assert isinstance(instance, dbl::CodeQuoteExpression)

@given(instance=dbl::L1Expr_strategy)
@settings(max_examples=50)
def test_dbl::l1expr_instantiation(instance):
    assert isinstance(instance, dbl::L1Expr)

@given(instance=L1Expr_strategy)
@settings(max_examples=50)
def test_l1expr_instantiation(instance):
    assert isinstance(instance, L1Expr)

@given(instance=dbl::ActiveLiteral_strategy)
@settings(max_examples=50)
def test_dbl::activeliteral_instantiation(instance):
    assert isinstance(instance, dbl::ActiveLiteral)

@given(instance=dbl::NullLiteral_strategy)
@settings(max_examples=50)
def test_dbl::nullliteral_instantiation(instance):
    assert isinstance(instance, dbl::NullLiteral)

@given(instance=dbl::IntLiteral_strategy)
@settings(max_examples=50)
def test_dbl::intliteral_instantiation(instance):
    assert isinstance(instance, dbl::IntLiteral)

@given(instance=dbl::IntLiteral_strategy)
def test_dbl::intliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=dbl::IntLiteral_strategy)
def test_dbl::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl::StringLiteral_strategy)
@settings(max_examples=50)
def test_dbl::stringliteral_instantiation(instance):
    assert isinstance(instance, dbl::StringLiteral)

@given(instance=dbl::StringLiteral_strategy)
def test_dbl::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dbl::StringLiteral_strategy)
def test_dbl::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl::TrueLiteral_strategy)
@settings(max_examples=50)
def test_dbl::trueliteral_instantiation(instance):
    assert isinstance(instance, dbl::TrueLiteral)

@given(instance=dbl::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_dbl::doubleliteral_instantiation(instance):
    assert isinstance(instance, dbl::DoubleLiteral)

@given(instance=dbl::DoubleLiteral_strategy)
def test_dbl::doubleliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=dbl::DoubleLiteral_strategy)
def test_dbl::doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl::FalseLiteral_strategy)
@settings(max_examples=50)
def test_dbl::falseliteral_instantiation(instance):
    assert isinstance(instance, dbl::FalseLiteral)

@given(instance=dbl::TimeLiteral_strategy)
@settings(max_examples=50)
def test_dbl::timeliteral_instantiation(instance):
    assert isinstance(instance, dbl::TimeLiteral)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=dbl::Not_strategy)
@settings(max_examples=50)
def test_dbl::not_instantiation(instance):
    assert isinstance(instance, dbl::Not)

@given(instance=dbl::Neg_strategy)
@settings(max_examples=50)
def test_dbl::neg_instantiation(instance):
    assert isinstance(instance, dbl::Neg)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=dbl::Equal_strategy)
@settings(max_examples=50)
def test_dbl::equal_instantiation(instance):
    assert isinstance(instance, dbl::Equal)

@given(instance=dbl::Mod_strategy)
@settings(max_examples=50)
def test_dbl::mod_instantiation(instance):
    assert isinstance(instance, dbl::Mod)

@given(instance=dbl::Plus_strategy)
@settings(max_examples=50)
def test_dbl::plus_instantiation(instance):
    assert isinstance(instance, dbl::Plus)

@given(instance=dbl::InstanceOf_strategy)
@settings(max_examples=50)
def test_dbl::instanceof_instantiation(instance):
    assert isinstance(instance, dbl::InstanceOf)

@given(instance=dbl::GreaterEqual_strategy)
@settings(max_examples=50)
def test_dbl::greaterequal_instantiation(instance):
    assert isinstance(instance, dbl::GreaterEqual)

@given(instance=dbl::Mul_strategy)
@settings(max_examples=50)
def test_dbl::mul_instantiation(instance):
    assert isinstance(instance, dbl::Mul)

@given(instance=dbl::Greater_strategy)
@settings(max_examples=50)
def test_dbl::greater_instantiation(instance):
    assert isinstance(instance, dbl::Greater)

@given(instance=dbl::Or_strategy)
@settings(max_examples=50)
def test_dbl::or_instantiation(instance):
    assert isinstance(instance, dbl::Or)

@given(instance=dbl::Div_strategy)
@settings(max_examples=50)
def test_dbl::div_instantiation(instance):
    assert isinstance(instance, dbl::Div)

@given(instance=dbl::LessEqual_strategy)
@settings(max_examples=50)
def test_dbl::lessequal_instantiation(instance):
    assert isinstance(instance, dbl::LessEqual)

@given(instance=dbl::NotEqual_strategy)
@settings(max_examples=50)
def test_dbl::notequal_instantiation(instance):
    assert isinstance(instance, dbl::NotEqual)

@given(instance=dbl::Less_strategy)
@settings(max_examples=50)
def test_dbl::less_instantiation(instance):
    assert isinstance(instance, dbl::Less)

@given(instance=dbl::Minus_strategy)
@settings(max_examples=50)
def test_dbl::minus_instantiation(instance):
    assert isinstance(instance, dbl::Minus)

@given(instance=dbl::And_strategy)
@settings(max_examples=50)
def test_dbl::and_instantiation(instance):
    assert isinstance(instance, dbl::And)

@given(instance=dbl::UnaryOperator_strategy)
@settings(max_examples=50)
def test_dbl::unaryoperator_instantiation(instance):
    assert isinstance(instance, dbl::UnaryOperator)

@given(instance=dbl::BinaryOperator_strategy)
@settings(max_examples=50)
def test_dbl::binaryoperator_instantiation(instance):
    assert isinstance(instance, dbl::BinaryOperator)

@given(instance=CompositeStatement_strategy)
@settings(max_examples=50)
def test_compositestatement_instantiation(instance):
    assert isinstance(instance, CompositeStatement)

@given(instance=dbl::ForEachStatement_strategy)
@settings(max_examples=50)
def test_dbl::foreachstatement_instantiation(instance):
    assert isinstance(instance, dbl::ForEachStatement)

@given(instance=dbl::ExpandSection_strategy)
@settings(max_examples=50)
def test_dbl::expandsection_instantiation(instance):
    assert isinstance(instance, dbl::ExpandSection)

@given(instance=dbl::WhileStatement_strategy)
@settings(max_examples=50)
def test_dbl::whilestatement_instantiation(instance):
    assert isinstance(instance, dbl::WhileStatement)

@given(instance=dbl::IfStatement_strategy)
@settings(max_examples=50)
def test_dbl::ifstatement_instantiation(instance):
    assert isinstance(instance, dbl::IfStatement)

@given(instance=dbl::ArgumentExpression_strategy)
@settings(max_examples=50)
def test_dbl::argumentexpression_instantiation(instance):
    assert isinstance(instance, dbl::ArgumentExpression)

@given(instance=SetStatement_strategy)
@settings(max_examples=50)
def test_setstatement_instantiation(instance):
    assert isinstance(instance, SetStatement)

@given(instance=dbl::EmptySet_strategy)
@settings(max_examples=50)
def test_dbl::emptyset_instantiation(instance):
    assert isinstance(instance, dbl::EmptySet)

@given(instance=dbl::AddToSet_strategy)
@settings(max_examples=50)
def test_dbl::addtoset_instantiation(instance):
    assert isinstance(instance, dbl::AddToSet)

@given(instance=dbl::RemoveFromSet_strategy)
@settings(max_examples=50)
def test_dbl::removefromset_instantiation(instance):
    assert isinstance(instance, dbl::RemoveFromSet)

@given(instance=Construct_strategy)
@settings(max_examples=50)
def test_construct_instantiation(instance):
    assert isinstance(instance, Construct)

@given(instance=dbl::Statement_strategy)
@settings(max_examples=50)
def test_dbl::statement_instantiation(instance):
    assert isinstance(instance, dbl::Statement)

@given(instance=dbl::CodeBlock_strategy)
@settings(max_examples=50)
def test_dbl::codeblock_instantiation(instance):
    assert isinstance(instance, dbl::CodeBlock)

@given(instance=ExpandableElement_strategy)
@settings(max_examples=50)
def test_expandableelement_instantiation(instance):
    assert isinstance(instance, ExpandableElement)

@given(instance=dbl::TypeAccess_strategy)
@settings(max_examples=50)
def test_dbl::typeaccess_instantiation(instance):
    assert isinstance(instance, dbl::TypeAccess)

@given(instance=dbl::NamedElement_strategy)
@settings(max_examples=50)
def test_dbl::namedelement_instantiation(instance):
    assert isinstance(instance, dbl::NamedElement)

@given(instance=dbl::NamedElement_strategy)
def test_dbl::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dbl::NamedElement_strategy)
def test_dbl::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=dbl::TargetStatement_strategy)
@settings(max_examples=50)
def test_dbl::targetstatement_instantiation(instance):
    assert isinstance(instance, dbl::TargetStatement)

@given(instance=dbl::ConsiderIdElements_strategy)
@settings(max_examples=50)
def test_dbl::consideridelements_instantiation(instance):
    assert isinstance(instance, dbl::ConsiderIdElements)

@given(instance=dbl::IncludePattern_strategy)
@settings(max_examples=50)
def test_dbl::includepattern_instantiation(instance):
    assert isinstance(instance, dbl::IncludePattern)

@given(instance=dbl::PotentiallyHiddenIdElements_strategy)
@settings(max_examples=50)
def test_dbl::potentiallyhiddenidelements_instantiation(instance):
    assert isinstance(instance, dbl::PotentiallyHiddenIdElements)

@given(instance=dbl::ExpandStatement_strategy)
@settings(max_examples=50)
def test_dbl::expandstatement_instantiation(instance):
    assert isinstance(instance, dbl::ExpandStatement)

@given(instance=dbl::FindContainer_strategy)
@settings(max_examples=50)
def test_dbl::findcontainer_instantiation(instance):
    assert isinstance(instance, dbl::FindContainer)

@given(instance=dbl::TestStatement_strategy)
@settings(max_examples=50)
def test_dbl::teststatement_instantiation(instance):
    assert isinstance(instance, dbl::TestStatement)

@given(instance=dbl::TestStatement_strategy)
def test_dbl::teststatement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dbl::TestStatement_strategy)
def test_dbl::teststatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl::MappingStatement_strategy)
@settings(max_examples=50)
def test_dbl::mappingstatement_instantiation(instance):
    assert isinstance(instance, dbl::MappingStatement)

@given(instance=StatementExpression_strategy)
@settings(max_examples=50)
def test_statementexpression_instantiation(instance):
    assert isinstance(instance, StatementExpression)

@given(instance=dbl::ExpandExpression_strategy)
@settings(max_examples=50)
def test_dbl::expandexpression_instantiation(instance):
    assert isinstance(instance, dbl::ExpandExpression)

@given(instance=dbl::ProcedureCall_strategy)
@settings(max_examples=50)
def test_dbl::procedurecall_instantiation(instance):
    assert isinstance(instance, dbl::ProcedureCall)

@given(instance=ExpressionStatement_strategy)
@settings(max_examples=50)
def test_expressionstatement_instantiation(instance):
    assert isinstance(instance, ExpressionStatement)

@given(instance=dbl::DeprecatedProcedureCallStatement_strategy)
@settings(max_examples=50)
def test_dbl::deprecatedprocedurecallstatement_instantiation(instance):
    assert isinstance(instance, dbl::DeprecatedProcedureCallStatement)

@given(instance=dbl::StatementExpression_strategy)
@settings(max_examples=50)
def test_dbl::statementexpression_instantiation(instance):
    assert isinstance(instance, dbl::StatementExpression)

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=dbl::ResumeGenStatement_strategy)
@settings(max_examples=50)
def test_dbl::resumegenstatement_instantiation(instance):
    assert isinstance(instance, dbl::ResumeGenStatement)

@given(instance=dbl::Advance_strategy)
@settings(max_examples=50)
def test_dbl::advance_instantiation(instance):
    assert isinstance(instance, dbl::Advance)

@given(instance=dbl::Terminate_strategy)
@settings(max_examples=50)
def test_dbl::terminate_instantiation(instance):
    assert isinstance(instance, dbl::Terminate)

@given(instance=dbl::Assignment_strategy)
@settings(max_examples=50)
def test_dbl::assignment_instantiation(instance):
    assert isinstance(instance, dbl::Assignment)

@given(instance=dbl::ActivateObject_strategy)
@settings(max_examples=50)
def test_dbl::activateobject_instantiation(instance):
    assert isinstance(instance, dbl::ActivateObject)

@given(instance=dbl::ActivateObject_strategy)
def test_dbl::activateobject_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=dbl::ActivateObject_strategy)
def test_dbl::activateobject_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=dbl::SaveGenStatement_strategy)
@settings(max_examples=50)
def test_dbl::savegenstatement_instantiation(instance):
    assert isinstance(instance, dbl::SaveGenStatement)

@given(instance=dbl::SetGenContextStatement_strategy)
@settings(max_examples=50)
def test_dbl::setgencontextstatement_instantiation(instance):
    assert isinstance(instance, dbl::SetGenContextStatement)

@given(instance=dbl::SetGenContextStatement_strategy)
def test_dbl::setgencontextstatement_addAfterContext_type(instance):
    assert isinstance(instance.addAfterContext, bool)


@given(instance=dbl::SetGenContextStatement_strategy)
def test_dbl::setgencontextstatement_addAfterContext_setter(instance):
    original = instance.addAfterContext
    instance.addAfterContext = original
    assert instance.addAfterContext == original

@given(instance=dbl::SetStatement_strategy)
@settings(max_examples=50)
def test_dbl::setstatement_instantiation(instance):
    assert isinstance(instance, dbl::SetStatement)

@given(instance=dbl::ContinueStatement_strategy)
@settings(max_examples=50)
def test_dbl::continuestatement_instantiation(instance):
    assert isinstance(instance, dbl::ContinueStatement)

@given(instance=dbl::Reactivate_strategy)
@settings(max_examples=50)
def test_dbl::reactivate_instantiation(instance):
    assert isinstance(instance, dbl::Reactivate)

@given(instance=dbl::Print_strategy)
@settings(max_examples=50)
def test_dbl::print_instantiation(instance):
    assert isinstance(instance, dbl::Print)

@given(instance=dbl::BreakStatement_strategy)
@settings(max_examples=50)
def test_dbl::breakstatement_instantiation(instance):
    assert isinstance(instance, dbl::BreakStatement)

@given(instance=dbl::Yield_strategy)
@settings(max_examples=50)
def test_dbl::yield_instantiation(instance):
    assert isinstance(instance, dbl::Yield)

@given(instance=dbl::ResetGenContextStatement_strategy)
@settings(max_examples=50)
def test_dbl::resetgencontextstatement_instantiation(instance):
    assert isinstance(instance, dbl::ResetGenContextStatement)

@given(instance=dbl::Wait_strategy)
@settings(max_examples=50)
def test_dbl::wait_instantiation(instance):
    assert isinstance(instance, dbl::Wait)

@given(instance=dbl::Return_strategy)
@settings(max_examples=50)
def test_dbl::return_instantiation(instance):
    assert isinstance(instance, dbl::Return)

@given(instance=dbl::WaitUntil_strategy)
@settings(max_examples=50)
def test_dbl::waituntil_instantiation(instance):
    assert isinstance(instance, dbl::WaitUntil)

@given(instance=dbl::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_dbl::expressionstatement_instantiation(instance):
    assert isinstance(instance, dbl::ExpressionStatement)

@given(instance=dbl::SimpleStatement_strategy)
@settings(max_examples=50)
def test_dbl::simplestatement_instantiation(instance):
    assert isinstance(instance, dbl::SimpleStatement)

@given(instance=dbl::CompositeStatement_strategy)
@settings(max_examples=50)
def test_dbl::compositestatement_instantiation(instance):
    assert isinstance(instance, dbl::CompositeStatement)

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=dbl::Constructor_strategy)
@settings(max_examples=50)
def test_dbl::constructor_instantiation(instance):
    assert isinstance(instance, dbl::Constructor)

@given(instance=ClassSimilar_strategy)
@settings(max_examples=50)
def test_classsimilar_instantiation(instance):
    assert isinstance(instance, ClassSimilar)

@given(instance=dbl::QuotedClassContent_strategy)
@settings(max_examples=50)
def test_dbl::quotedclasscontent_instantiation(instance):
    assert isinstance(instance, dbl::QuotedClassContent)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=dbl::AnnotationApplication_strategy)
@settings(max_examples=50)
def test_dbl::annotationapplication_instantiation(instance):
    assert isinstance(instance, dbl::AnnotationApplication)

@given(instance=dbl::Interface_strategy)
@settings(max_examples=50)
def test_dbl::interface_instantiation(instance):
    assert isinstance(instance, dbl::Interface)

@given(instance=dbl::Clazz_strategy)
@settings(max_examples=50)
def test_dbl::clazz_instantiation(instance):
    assert isinstance(instance, dbl::Clazz)

@given(instance=dbl::Clazz_strategy)
def test_dbl::clazz_active_type(instance):
    assert isinstance(instance.active, bool)


@given(instance=dbl::Clazz_strategy)
def test_dbl::clazz_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=ModifierExtensionsContainer_strategy)
@settings(max_examples=50)
def test_modifierextensionscontainer_instantiation(instance):
    assert isinstance(instance, ModifierExtensionsContainer)

@given(instance=dbl::NativeBinding_strategy)
@settings(max_examples=50)
def test_dbl::nativebinding_instantiation(instance):
    assert isinstance(instance, dbl::NativeBinding)

@given(instance=dbl::NativeBinding_strategy)
def test_dbl::nativebinding_targetLanguage_type(instance):
    assert isinstance(instance.targetLanguage, str)


@given(instance=dbl::NativeBinding_strategy)
def test_dbl::nativebinding_targetLanguage_setter(instance):
    original = instance.targetLanguage
    instance.targetLanguage = original
    assert instance.targetLanguage == original

@given(instance=dbl::NativeBinding_strategy)
def test_dbl::nativebinding_targetType_type(instance):
    assert isinstance(instance.targetType, str)


@given(instance=dbl::NativeBinding_strategy)
def test_dbl::nativebinding_targetType_setter(instance):
    original = instance.targetType
    instance.targetType = original
    assert instance.targetType == original

@given(instance=ReferableRhsType_strategy)
@settings(max_examples=50)
def test_referablerhstype_instantiation(instance):
    assert isinstance(instance, ReferableRhsType)

@given(instance=dbl::AnnotatableElement_strategy)
@settings(max_examples=50)
def test_dbl::annotatableelement_instantiation(instance):
    assert isinstance(instance, dbl::AnnotatableElement)

@given(instance=dbl::Expression_strategy)
@settings(max_examples=50)
def test_dbl::expression_instantiation(instance):
    assert isinstance(instance, dbl::Expression)

@given(instance=dbl::VariableAccess_strategy)
@settings(max_examples=50)
def test_dbl::variableaccess_instantiation(instance):
    assert isinstance(instance, dbl::VariableAccess)

@given(instance=dbl::KeyValuePair_strategy)
@settings(max_examples=50)
def test_dbl::keyvaluepair_instantiation(instance):
    assert isinstance(instance, dbl::KeyValuePair)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=dbl::Parameter_strategy)
@settings(max_examples=50)
def test_dbl::parameter_instantiation(instance):
    assert isinstance(instance, dbl::Parameter)

@given(instance=AnnotatableElement_strategy)
@settings(max_examples=50)
def test_annotatableelement_instantiation(instance):
    assert isinstance(instance, AnnotatableElement)

@given(instance=CodeBlock_strategy)
@settings(max_examples=50)
def test_codeblock_instantiation(instance):
    assert isinstance(instance, CodeBlock)

@given(instance=dbl::StartCodeBlock_strategy)
@settings(max_examples=50)
def test_dbl::startcodeblock_instantiation(instance):
    assert isinstance(instance, dbl::StartCodeBlock)

@given(instance=dbl::Mapping_strategy)
@settings(max_examples=50)
def test_dbl::mapping_instantiation(instance):
    assert isinstance(instance, dbl::Mapping)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=dbl::BoolType_strategy)
@settings(max_examples=50)
def test_dbl::booltype_instantiation(instance):
    assert isinstance(instance, dbl::BoolType)

@given(instance=dbl::DoubleType_strategy)
@settings(max_examples=50)
def test_dbl::doubletype_instantiation(instance):
    assert isinstance(instance, dbl::DoubleType)

@given(instance=dbl::StringType_strategy)
@settings(max_examples=50)
def test_dbl::stringtype_instantiation(instance):
    assert isinstance(instance, dbl::StringType)

@given(instance=dbl::IntType_strategy)
@settings(max_examples=50)
def test_dbl::inttype_instantiation(instance):
    assert isinstance(instance, dbl::IntType)

@given(instance=dbl::VoidType_strategy)
@settings(max_examples=50)
def test_dbl::voidtype_instantiation(instance):
    assert isinstance(instance, dbl::VoidType)

@given(instance=dbl::Import_strategy)
@settings(max_examples=50)
def test_dbl::import_instantiation(instance):
    assert isinstance(instance, dbl::Import)

@given(instance=dbl::Import_strategy)
def test_dbl::import_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=dbl::Import_strategy)
def test_dbl::import_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=dbl::Model_strategy)
@settings(max_examples=50)
def test_dbl::model_instantiation(instance):
    assert isinstance(instance, dbl::Model)

@given(instance=NamedExtensible_strategy)
@settings(max_examples=50)
def test_namedextensible_instantiation(instance):
    assert isinstance(instance, NamedExtensible)

@given(instance=dbl::ClassContentExtension_strategy)
@settings(max_examples=50)
def test_dbl::classcontentextension_instantiation(instance):
    assert isinstance(instance, dbl::ClassContentExtension)

@given(instance=dbl::ModuleContentExtension_strategy)
@settings(max_examples=50)
def test_dbl::modulecontentextension_instantiation(instance):
    assert isinstance(instance, dbl::ModuleContentExtension)

@given(instance=dbl::Construct_strategy)
@settings(max_examples=50)
def test_dbl::construct_instantiation(instance):
    assert isinstance(instance, dbl::Construct)

@given(instance=dbl::Construct_strategy)
def test_dbl::construct_concreteSyntax_type(instance):
    assert isinstance(instance.concreteSyntax, str)


@given(instance=dbl::Construct_strategy)
def test_dbl::construct_concreteSyntax_setter(instance):
    original = instance.concreteSyntax
    instance.concreteSyntax = original
    assert instance.concreteSyntax == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=dbl::Cast_strategy)
@settings(max_examples=50)
def test_dbl::cast_instantiation(instance):
    assert isinstance(instance, dbl::Cast)

@given(instance=dbl::CreateObject_strategy)
@settings(max_examples=50)
def test_dbl::createobject_instantiation(instance):
    assert isinstance(instance, dbl::CreateObject)

@given(instance=dbl::IdExpr_strategy)
@settings(max_examples=50)
def test_dbl::idexpr_instantiation(instance):
    assert isinstance(instance, dbl::IdExpr)

@given(instance=dbl::ListDimension_strategy)
@settings(max_examples=50)
def test_dbl::listdimension_instantiation(instance):
    assert isinstance(instance, dbl::ListDimension)

@given(instance=dbl::ListDimension_strategy)
def test_dbl::listdimension_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=dbl::ListDimension_strategy)
def test_dbl::listdimension_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=dbl::PrimitiveType_strategy)
@settings(max_examples=50)
def test_dbl::primitivetype_instantiation(instance):
    assert isinstance(instance, dbl::PrimitiveType)

@given(instance=dbl::TypedElement_strategy)
@settings(max_examples=50)
def test_dbl::typedelement_instantiation(instance):
    assert isinstance(instance, dbl::TypedElement)

@given(instance=dbl::TypedElement_strategy)
def test_dbl::typedelement_isList_type(instance):
    assert isinstance(instance.isList, bool)


@given(instance=dbl::TypedElement_strategy)
def test_dbl::typedelement_isList_setter(instance):
    original = instance.isList
    instance.isList = original
    assert instance.isList == original

@given(instance=dbl::Type_strategy)
@settings(max_examples=50)
def test_dbl::type_instantiation(instance):
    assert isinstance(instance, dbl::Type)

@given(instance=dbl::ModifierExtensionsContainer_strategy)
@settings(max_examples=50)
def test_dbl::modifierextensionscontainer_instantiation(instance):
    assert isinstance(instance, dbl::ModifierExtensionsContainer)

@given(instance=dbl::ExtensibleElement_strategy)
@settings(max_examples=50)
def test_dbl::extensibleelement_instantiation(instance):
    assert isinstance(instance, dbl::ExtensibleElement)

@given(instance=dbl::ExtensibleElement_strategy)
def test_dbl::extensibleelement_objectIsExtensionInstance_type(instance):
    assert isinstance(instance.objectIsExtensionInstance, bool)


@given(instance=dbl::ExtensibleElement_strategy)
def test_dbl::extensibleelement_objectIsExtensionInstance_setter(instance):
    original = instance.objectIsExtensionInstance
    instance.objectIsExtensionInstance = original
    assert instance.objectIsExtensionInstance == original

@given(instance=dbl::EmbeddableExtensionsContainer_strategy)
@settings(max_examples=50)
def test_dbl::embeddableextensionscontainer_instantiation(instance):
    assert isinstance(instance, dbl::EmbeddableExtensionsContainer)

@given(instance=dbl::IdResolution_strategy)
@settings(max_examples=50)
def test_dbl::idresolution_instantiation(instance):
    assert isinstance(instance, dbl::IdResolution)

@given(instance=dbl::IdResolution_strategy)
def test_dbl::idresolution_metaModelPlatformURI_type(instance):
    assert isinstance(instance.metaModelPlatformURI, str)


@given(instance=dbl::IdResolution_strategy)
def test_dbl::idresolution_metaModelPlatformURI_setter(instance):
    original = instance.metaModelPlatformURI
    instance.metaModelPlatformURI = original
    assert instance.metaModelPlatformURI == original

@given(instance=dbl::Variable_strategy)
@settings(max_examples=50)
def test_dbl::variable_instantiation(instance):
    assert isinstance(instance, dbl::Variable)

@given(instance=dbl::Variable_strategy)
def test_dbl::variable_control_type(instance):
    assert isinstance(instance.control, bool)


@given(instance=dbl::Variable_strategy)
def test_dbl::variable_control_setter(instance):
    original = instance.control
    instance.control = original
    assert instance.control == original

@given(instance=dbl::Variable_strategy)
def test_dbl::variable_clazz_type(instance):
    assert isinstance(instance.clazz, bool)


@given(instance=dbl::Variable_strategy)
def test_dbl::variable_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original

@given(instance=dbl::ClassAugment_strategy)
@settings(max_examples=50)
def test_dbl::classaugment_instantiation(instance):
    assert isinstance(instance, dbl::ClassAugment)

@given(instance=EmbeddableExtensionsContainer_strategy)
@settings(max_examples=50)
def test_embeddableextensionscontainer_instantiation(instance):
    assert isinstance(instance, EmbeddableExtensionsContainer)

@given(instance=dbl::ClassSimilar_strategy)
@settings(max_examples=50)
def test_dbl::classsimilar_instantiation(instance):
    assert isinstance(instance, dbl::ClassSimilar)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dbl::PropertyBindingExpr_strategy)
@settings(max_examples=50)
def test_dbl::propertybindingexpr_instantiation(instance):
    assert isinstance(instance, dbl::PropertyBindingExpr)

@given(instance=dbl::PropertyBindingExpr_strategy)
def test_dbl::propertybindingexpr_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=dbl::PropertyBindingExpr_strategy)
def test_dbl::propertybindingexpr_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dbl::Procedure_strategy)
@settings(max_examples=50)
def test_dbl::procedure_instantiation(instance):
    assert isinstance(instance, dbl::Procedure)

@given(instance=dbl::Procedure_strategy)
def test_dbl::procedure_clazz_type(instance):
    assert isinstance(instance.clazz, bool)


@given(instance=dbl::Procedure_strategy)
def test_dbl::procedure_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original

@given(instance=dbl::Module_strategy)
@settings(max_examples=50)
def test_dbl::module_instantiation(instance):
    assert isinstance(instance, dbl::Module)

@given(instance=dbl::TsRule_strategy)
@settings(max_examples=50)
def test_dbl::tsrule_instantiation(instance):
    assert isinstance(instance, dbl::TsRule)

@given(instance=dbl::TsRule_strategy)
def test_dbl::tsrule_metaClassName_type(instance):
    assert isinstance(instance.metaClassName, str)


@given(instance=dbl::TsRule_strategy)
def test_dbl::tsrule_metaClassName_setter(instance):
    original = instance.metaClassName
    instance.metaClassName = original
    assert instance.metaClassName == original

@given(instance=dbl::NamedExtensible_strategy)
@settings(max_examples=50)
def test_dbl::namedextensible_instantiation(instance):
    assert isinstance(instance, dbl::NamedExtensible)

@given(instance=dbl::SimpleAnnotation_strategy)
@settings(max_examples=50)
def test_dbl::simpleannotation_instantiation(instance):
    assert isinstance(instance, dbl::SimpleAnnotation)

@given(instance=dbl::SimpleAnnotation_strategy)
def test_dbl::simpleannotation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dbl::SimpleAnnotation_strategy)
def test_dbl::simpleannotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dbl::Annotation_strategy)
@settings(max_examples=50)
def test_dbl::annotation_instantiation(instance):
    assert isinstance(instance, dbl::Annotation)

@given(instance=dbl::ReferableRhsType_strategy)
@settings(max_examples=50)
def test_dbl::referablerhstype_instantiation(instance):
    assert isinstance(instance, dbl::ReferableRhsType)

@given(instance=dbl::ExtensionRule_strategy)
@settings(max_examples=50)
def test_dbl::extensionrule_instantiation(instance):
    assert isinstance(instance, dbl::ExtensionRule)

@given(instance=dbl::Classifier_strategy)
@settings(max_examples=50)
def test_dbl::classifier_instantiation(instance):
    assert isinstance(instance, dbl::Classifier)

@given(instance=dbl::AbstractVariable_strategy)
@settings(max_examples=50)
def test_dbl::abstractvariable_instantiation(instance):
    assert isinstance(instance, dbl::AbstractVariable)

@given(instance=dbl::ExtensionDefinition_strategy)
@settings(max_examples=50)
def test_dbl::extensiondefinition_instantiation(instance):
    assert isinstance(instance, dbl::ExtensionDefinition)

@given(instance=dbl::Pattern_strategy)
@settings(max_examples=50)
def test_dbl::pattern_instantiation(instance):
    assert isinstance(instance, dbl::Pattern)

@given(instance=dbl::Pattern_strategy)
def test_dbl::pattern_top_type(instance):
    assert isinstance(instance.top, bool)


@given(instance=dbl::Pattern_strategy)
def test_dbl::pattern_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original
