import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Statement,
    dbl::SimpleStatement,
    dbl::LoopStatement,
    ModifierExtensionsContainer,
    dbl::NativeBinding,
    LocalScope,
    TypedElement,
    dbl::Constructor,
    LanguageConceptClassifier,
    ClassSimilar,
    Classifier,
    dbl::ClassPart,
    dbl::SuperClassSpecification,
    dbl::ClassAugment,
    EmbeddableExtensionsContainer,
    dbl::ClassSimilar,
    dbl::Import,
    dbl::Model,
    PrimitiveType,
    dbl::BoolType,
    dbl::StringType,
    dbl::IntType,
    dbl::DoubleType,
    dbl::VoidType,
    Type,
    dbl::PrimitiveType,
    dbl::TypedElement,
    dbl::ArrayDimension,
    dbl::Type,
    dbl::ModifierExtensionsContainer,
    dbl::EmbeddableExtensionsContainer,
    Construct,
    dbl::Clazz,
    NamedElement,
    dbl::Classifier,
    dbl::Module,
    dbl::Procedure,
    dbl::ExtensibleElement,
    dbl::Construct,
    dbl::Pattern,
    Module,
    dbl::TestStatement,
    QuotedCode,
    dbl::QuotedStatements,
    dbl::QuotedModuleContent,
    dbl::QuotedClassContent,
    dbl::QuotedExpression,
    dbl::QuotedCode,
    dbl::ExpandStatement,
    MappingPart,
    dbl::DynamicMappingPart,
    dbl::FixedMappingPart,
    PropertyType,
    dbl::IdPropertyType,
    dbl::PropertyType,
    dbl::MappingStatement,
    dbl::TargetStatement,
    dbl::MappingPart,
    LocalScopeStatement,
    StructuredPropertyType,
    dbl::ReferencePropertyType,
    dbl::CompositePropertyType,
    dbl::StructuredPropertyType,
    dbl::BooleanPropertyType,
    dbl::StringPropertyType,
    dbl::IntPropertyType,
    VariableAccess,
    L1RhsExpr,
    dbl::RhsClassifierExpr,
    dbl::PropertyBindingExpr,
    dbl::MetaAccess,
    dbl::TerminalExpr,
    L2RhsExpr,
    dbl::SequenceExpr,
    ElementAccess,
    dbl::TypeAccess,
    dbl::VariableAccess,
    RhsExpression,
    dbl::L1RhsExpr,
    dbl::L2RhsExpr,
    dbl::L3RhsExpr,
    dbl::RhsExpression,
    LanguageConstructClassifier,
    dbl::LanguageConceptClassifier,
    dbl::TsRule,
    dbl::Mapping,
    dbl::CallPart,
    PredefinedId,
    dbl::MetaLiteral,
    dbl::SizeOfArray,
    dbl::TypeLiteral,
    dbl::SuperLiteral,
    dbl::MeLiteral,
    dbl::PredefinedId,
    Expression,
    dbl::L3Expr,
    dbl::L4Expr,
    dbl::ExpandExpr,
    dbl::MetaExpr,
    dbl::ParseExpr,
    dbl::ElementAccess,
    dbl::L8Expr,
    dbl::BinaryOperator,
    dbl::L9Expr,
    dbl::L7Expr,
    dbl::ExpandExpression,
    dbl::L5Expr,
    dbl::L6Expr,
    dbl::L2Expr,
    dbl::CodeQuoteExpression,
    dbl::UnaryOperator,
    dbl::L1Expr,
    L1Expr,
    dbl::IdExpr,
    dbl::DoubleLiteral,
    dbl::StringLiteral,
    dbl::TrueLiteral,
    dbl::IntLiteral,
    dbl::ActiveLiteral,
    dbl::TimeLiteral,
    dbl::NullLiteral,
    dbl::FalseLiteral,
    dbl::CreateObject,
    L2Expr,
    UnaryOperator,
    dbl::Cast,
    dbl::Not,
    dbl::Neg,
    L3Expr,
    L4Expr,
    L5Expr,
    L6Expr,
    L7Expr,
    L8Expr,
    BinaryOperator,
    dbl::Greater,
    dbl::Plus,
    dbl::And,
    dbl::Mul,
    dbl::Less,
    dbl::Mod,
    dbl::Div,
    dbl::InstanceOf,
    dbl::NotEqual,
    dbl::Equal,
    dbl::LessEqual,
    dbl::Minus,
    dbl::GreaterEqual,
    dbl::Or,
    dbl::LocalScope,
    dbl::IfStatement,
    dbl::SwitchCase,
    LoopStatement,
    dbl::WhileStatement,
    dbl::ForStatement,
    ExtensibleElement,
    dbl::TextualSyntaxDef,
    dbl::ClassContentExtension,
    dbl::Expression,
    dbl::ModuleContentExtension,
    dbl::ExtensionDefinition,
    dbl::LanguageConstructClassifier,
    dbl::Statement,
    dbl::NamedElement,
    SimpleStatement,
    dbl::SetGenContextStatement,
    dbl::ProcedureCall,
    dbl::Advance,
    dbl::SwitchStatement,
    dbl::LocalScopeStatement,
    dbl::WaitUntil,
    dbl::SaveGenStatement,
    dbl::Reactivate,
    dbl::Wait,
    dbl::Assignment,
    dbl::ContinueStatement,
    dbl::ActivateObject,
    dbl::Return,
    dbl::Yield,
    dbl::BreakStatement,
    dbl::ResumeGenStatement,
    dbl::Terminate,
    dbl::Print,
    dbl::ResetGenContextStatement,
    AbstractVariable,
    dbl::Parameter,
    dbl::Variable,
    dbl::AbstractVariable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::simplestatement_is_not_abstract():
    assert not inspect.isabstract(dbl::SimpleStatement)


def test_dbl::simplestatement_constructor_exists():
    assert callable(dbl::SimpleStatement.__init__)


def test_dbl::simplestatement_constructor_args():
    sig = inspect.signature(dbl::SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::loopstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::LoopStatement)


def test_dbl::loopstatement_constructor_exists():
    assert callable(dbl::LoopStatement.__init__)


def test_dbl::loopstatement_constructor_args():
    sig = inspect.signature(dbl::LoopStatement.__init__)
    params = list(sig.parameters.keys())



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



def test_localscope_is_not_abstract():
    assert not inspect.isabstract(LocalScope)


def test_localscope_constructor_exists():
    assert callable(LocalScope.__init__)


def test_localscope_constructor_args():
    sig = inspect.signature(LocalScope.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::constructor_is_not_abstract():
    assert not inspect.isabstract(dbl::Constructor)


def test_dbl::constructor_constructor_exists():
    assert callable(dbl::Constructor.__init__)


def test_dbl::constructor_constructor_args():
    sig = inspect.signature(dbl::Constructor.__init__)
    params = list(sig.parameters.keys())



def test_languageconceptclassifier_is_not_abstract():
    assert not inspect.isabstract(LanguageConceptClassifier)


def test_languageconceptclassifier_constructor_exists():
    assert callable(LanguageConceptClassifier.__init__)


def test_languageconceptclassifier_constructor_args():
    sig = inspect.signature(LanguageConceptClassifier.__init__)
    params = list(sig.parameters.keys())



def test_classsimilar_is_not_abstract():
    assert not inspect.isabstract(ClassSimilar)


def test_classsimilar_constructor_exists():
    assert callable(ClassSimilar.__init__)


def test_classsimilar_constructor_args():
    sig = inspect.signature(ClassSimilar.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl::classpart_is_not_abstract():
    assert not inspect.isabstract(dbl::ClassPart)


def test_dbl::classpart_constructor_exists():
    assert callable(dbl::ClassPart.__init__)


def test_dbl::classpart_constructor_args():
    sig = inspect.signature(dbl::ClassPart.__init__)
    params = list(sig.parameters.keys())



def test_dbl::superclassspecification_is_not_abstract():
    assert not inspect.isabstract(dbl::SuperClassSpecification)


def test_dbl::superclassspecification_constructor_exists():
    assert callable(dbl::SuperClassSpecification.__init__)


def test_dbl::superclassspecification_constructor_args():
    sig = inspect.signature(dbl::SuperClassSpecification.__init__)
    params = list(sig.parameters.keys())



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



def test_dbl::doubletype_is_not_abstract():
    assert not inspect.isabstract(dbl::DoubleType)


def test_dbl::doubletype_constructor_exists():
    assert callable(dbl::DoubleType.__init__)


def test_dbl::doubletype_constructor_args():
    sig = inspect.signature(dbl::DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::voidtype_is_not_abstract():
    assert not inspect.isabstract(dbl::VoidType)


def test_dbl::voidtype_constructor_exists():
    assert callable(dbl::VoidType.__init__)


def test_dbl::voidtype_constructor_args():
    sig = inspect.signature(dbl::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



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



def test_dbl::arraydimension_is_not_abstract():
    assert not inspect.isabstract(dbl::ArrayDimension)


def test_dbl::arraydimension_constructor_exists():
    assert callable(dbl::ArrayDimension.__init__)


def test_dbl::arraydimension_constructor_args():
    sig = inspect.signature(dbl::ArrayDimension.__init__)
    params = list(sig.parameters.keys())



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



def test_dbl::embeddableextensionscontainer_is_not_abstract():
    assert not inspect.isabstract(dbl::EmbeddableExtensionsContainer)


def test_dbl::embeddableextensionscontainer_constructor_exists():
    assert callable(dbl::EmbeddableExtensionsContainer.__init__)


def test_dbl::embeddableextensionscontainer_constructor_args():
    sig = inspect.signature(dbl::EmbeddableExtensionsContainer.__init__)
    params = list(sig.parameters.keys())



def test_construct_is_not_abstract():
    assert not inspect.isabstract(Construct)


def test_construct_constructor_exists():
    assert callable(Construct.__init__)


def test_construct_constructor_args():
    sig = inspect.signature(Construct.__init__)
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



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::classifier_is_not_abstract():
    assert not inspect.isabstract(dbl::Classifier)


def test_dbl::classifier_constructor_exists():
    assert callable(dbl::Classifier.__init__)


def test_dbl::classifier_constructor_args():
    sig = inspect.signature(dbl::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl::module_is_not_abstract():
    assert not inspect.isabstract(dbl::Module)


def test_dbl::module_constructor_exists():
    assert callable(dbl::Module.__init__)


def test_dbl::module_constructor_args():
    sig = inspect.signature(dbl::Module.__init__)
    params = list(sig.parameters.keys())



def test_dbl::procedure_is_not_abstract():
    assert not inspect.isabstract(dbl::Procedure)


def test_dbl::procedure_constructor_exists():
    assert callable(dbl::Procedure.__init__)


def test_dbl::procedure_constructor_args():
    sig = inspect.signature(dbl::Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "clazz" in params, "Missing parameter 'clazz'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_dbl::procedure_has_clazz():
    assert hasattr(dbl::Procedure, "clazz")
    descriptor = None
    for klass in dbl::Procedure.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)

def test_dbl::procedure_has_abstract():
    assert hasattr(dbl::Procedure, "abstract")
    descriptor = None
    for klass in dbl::Procedure.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_dbl::extensibleelement_is_not_abstract():
    assert not inspect.isabstract(dbl::ExtensibleElement)


def test_dbl::extensibleelement_constructor_exists():
    assert callable(dbl::ExtensibleElement.__init__)


def test_dbl::extensibleelement_constructor_args():
    sig = inspect.signature(dbl::ExtensibleElement.__init__)
    params = list(sig.parameters.keys())
    assert "instanceOfExtensionDefinition" in params, "Missing parameter 'instanceOfExtensionDefinition'"
    assert "concreteSyntax" in params, "Missing parameter 'concreteSyntax'"

def test_dbl::extensibleelement_has_instanceOfExtensionDefinition():
    assert hasattr(dbl::ExtensibleElement, "instanceOfExtensionDefinition")
    descriptor = None
    for klass in dbl::ExtensibleElement.__mro__:
        if "instanceOfExtensionDefinition" in klass.__dict__:
            descriptor = klass.__dict__["instanceOfExtensionDefinition"]
            break
    assert isinstance(descriptor, property)

def test_dbl::extensibleelement_has_concreteSyntax():
    assert hasattr(dbl::ExtensibleElement, "concreteSyntax")
    descriptor = None
    for klass in dbl::ExtensibleElement.__mro__:
        if "concreteSyntax" in klass.__dict__:
            descriptor = klass.__dict__["concreteSyntax"]
            break
    assert isinstance(descriptor, property)



def test_dbl::construct_is_not_abstract():
    assert not inspect.isabstract(dbl::Construct)


def test_dbl::construct_constructor_exists():
    assert callable(dbl::Construct.__init__)


def test_dbl::construct_constructor_args():
    sig = inspect.signature(dbl::Construct.__init__)
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



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
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



def test_dbl::quotedclasscontent_is_not_abstract():
    assert not inspect.isabstract(dbl::QuotedClassContent)


def test_dbl::quotedclasscontent_constructor_exists():
    assert callable(dbl::QuotedClassContent.__init__)


def test_dbl::quotedclasscontent_constructor_args():
    sig = inspect.signature(dbl::QuotedClassContent.__init__)
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



def test_dbl::expandstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpandStatement)


def test_dbl::expandstatement_constructor_exists():
    assert callable(dbl::ExpandStatement.__init__)


def test_dbl::expandstatement_constructor_args():
    sig = inspect.signature(dbl::ExpandStatement.__init__)
    params = list(sig.parameters.keys())



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



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



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



def test_dbl::mappingstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::MappingStatement)


def test_dbl::mappingstatement_constructor_exists():
    assert callable(dbl::MappingStatement.__init__)


def test_dbl::mappingstatement_constructor_args():
    sig = inspect.signature(dbl::MappingStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::targetstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::TargetStatement)


def test_dbl::targetstatement_constructor_exists():
    assert callable(dbl::TargetStatement.__init__)


def test_dbl::targetstatement_constructor_args():
    sig = inspect.signature(dbl::TargetStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::mappingpart_is_not_abstract():
    assert not inspect.isabstract(dbl::MappingPart)


def test_dbl::mappingpart_constructor_exists():
    assert callable(dbl::MappingPart.__init__)


def test_dbl::mappingpart_constructor_args():
    sig = inspect.signature(dbl::MappingPart.__init__)
    params = list(sig.parameters.keys())



def test_localscopestatement_is_not_abstract():
    assert not inspect.isabstract(LocalScopeStatement)


def test_localscopestatement_constructor_exists():
    assert callable(LocalScopeStatement.__init__)


def test_localscopestatement_constructor_args():
    sig = inspect.signature(LocalScopeStatement.__init__)
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



def test_dbl::structuredpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl::StructuredPropertyType)


def test_dbl::structuredpropertytype_constructor_exists():
    assert callable(dbl::StructuredPropertyType.__init__)


def test_dbl::structuredpropertytype_constructor_args():
    sig = inspect.signature(dbl::StructuredPropertyType.__init__)
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



def test_dbl::stringpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl::StringPropertyType)


def test_dbl::stringpropertytype_constructor_exists():
    assert callable(dbl::StringPropertyType.__init__)


def test_dbl::stringpropertytype_constructor_args():
    sig = inspect.signature(dbl::StringPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_dbl::intpropertytype_is_not_abstract():
    assert not inspect.isabstract(dbl::IntPropertyType)


def test_dbl::intpropertytype_constructor_exists():
    assert callable(dbl::IntPropertyType.__init__)


def test_dbl::intpropertytype_constructor_args():
    sig = inspect.signature(dbl::IntPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_variableaccess_is_not_abstract():
    assert not inspect.isabstract(VariableAccess)


def test_variableaccess_constructor_exists():
    assert callable(VariableAccess.__init__)


def test_variableaccess_constructor_args():
    sig = inspect.signature(VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_l1rhsexpr_is_not_abstract():
    assert not inspect.isabstract(L1RhsExpr)


def test_l1rhsexpr_constructor_exists():
    assert callable(L1RhsExpr.__init__)


def test_l1rhsexpr_constructor_args():
    sig = inspect.signature(L1RhsExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::rhsclassifierexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::RhsClassifierExpr)


def test_dbl::rhsclassifierexpr_constructor_exists():
    assert callable(dbl::RhsClassifierExpr.__init__)


def test_dbl::rhsclassifierexpr_constructor_args():
    sig = inspect.signature(dbl::RhsClassifierExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::propertybindingexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::PropertyBindingExpr)


def test_dbl::propertybindingexpr_constructor_exists():
    assert callable(dbl::PropertyBindingExpr.__init__)


def test_dbl::propertybindingexpr_constructor_args():
    sig = inspect.signature(dbl::PropertyBindingExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::metaaccess_is_not_abstract():
    assert not inspect.isabstract(dbl::MetaAccess)


def test_dbl::metaaccess_constructor_exists():
    assert callable(dbl::MetaAccess.__init__)


def test_dbl::metaaccess_constructor_args():
    sig = inspect.signature(dbl::MetaAccess.__init__)
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



def test_l2rhsexpr_is_not_abstract():
    assert not inspect.isabstract(L2RhsExpr)


def test_l2rhsexpr_constructor_exists():
    assert callable(L2RhsExpr.__init__)


def test_l2rhsexpr_constructor_args():
    sig = inspect.signature(L2RhsExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::sequenceexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::SequenceExpr)


def test_dbl::sequenceexpr_constructor_exists():
    assert callable(dbl::SequenceExpr.__init__)


def test_dbl::sequenceexpr_constructor_args():
    sig = inspect.signature(dbl::SequenceExpr.__init__)
    params = list(sig.parameters.keys())



def test_elementaccess_is_not_abstract():
    assert not inspect.isabstract(ElementAccess)


def test_elementaccess_constructor_exists():
    assert callable(ElementAccess.__init__)


def test_elementaccess_constructor_args():
    sig = inspect.signature(ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl::typeaccess_is_not_abstract():
    assert not inspect.isabstract(dbl::TypeAccess)


def test_dbl::typeaccess_constructor_exists():
    assert callable(dbl::TypeAccess.__init__)


def test_dbl::typeaccess_constructor_args():
    sig = inspect.signature(dbl::TypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl::variableaccess_is_not_abstract():
    assert not inspect.isabstract(dbl::VariableAccess)


def test_dbl::variableaccess_constructor_exists():
    assert callable(dbl::VariableAccess.__init__)


def test_dbl::variableaccess_constructor_args():
    sig = inspect.signature(dbl::VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_rhsexpression_is_not_abstract():
    assert not inspect.isabstract(RhsExpression)


def test_rhsexpression_constructor_exists():
    assert callable(RhsExpression.__init__)


def test_rhsexpression_constructor_args():
    sig = inspect.signature(RhsExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l1rhsexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::L1RhsExpr)


def test_dbl::l1rhsexpr_constructor_exists():
    assert callable(dbl::L1RhsExpr.__init__)


def test_dbl::l1rhsexpr_constructor_args():
    sig = inspect.signature(dbl::L1RhsExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l2rhsexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::L2RhsExpr)


def test_dbl::l2rhsexpr_constructor_exists():
    assert callable(dbl::L2RhsExpr.__init__)


def test_dbl::l2rhsexpr_constructor_args():
    sig = inspect.signature(dbl::L2RhsExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l3rhsexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::L3RhsExpr)


def test_dbl::l3rhsexpr_constructor_exists():
    assert callable(dbl::L3RhsExpr.__init__)


def test_dbl::l3rhsexpr_constructor_args():
    sig = inspect.signature(dbl::L3RhsExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::rhsexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::RhsExpression)


def test_dbl::rhsexpression_constructor_exists():
    assert callable(dbl::RhsExpression.__init__)


def test_dbl::rhsexpression_constructor_args():
    sig = inspect.signature(dbl::RhsExpression.__init__)
    params = list(sig.parameters.keys())



def test_languageconstructclassifier_is_not_abstract():
    assert not inspect.isabstract(LanguageConstructClassifier)


def test_languageconstructclassifier_constructor_exists():
    assert callable(LanguageConstructClassifier.__init__)


def test_languageconstructclassifier_constructor_args():
    sig = inspect.signature(LanguageConstructClassifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl::languageconceptclassifier_is_not_abstract():
    assert not inspect.isabstract(dbl::LanguageConceptClassifier)


def test_dbl::languageconceptclassifier_constructor_exists():
    assert callable(dbl::LanguageConceptClassifier.__init__)


def test_dbl::languageconceptclassifier_constructor_args():
    sig = inspect.signature(dbl::LanguageConceptClassifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl::tsrule_is_not_abstract():
    assert not inspect.isabstract(dbl::TsRule)


def test_dbl::tsrule_constructor_exists():
    assert callable(dbl::TsRule.__init__)


def test_dbl::tsrule_constructor_args():
    sig = inspect.signature(dbl::TsRule.__init__)
    params = list(sig.parameters.keys())



def test_dbl::mapping_is_not_abstract():
    assert not inspect.isabstract(dbl::Mapping)


def test_dbl::mapping_constructor_exists():
    assert callable(dbl::Mapping.__init__)


def test_dbl::mapping_constructor_args():
    sig = inspect.signature(dbl::Mapping.__init__)
    params = list(sig.parameters.keys())



def test_dbl::callpart_is_not_abstract():
    assert not inspect.isabstract(dbl::CallPart)


def test_dbl::callpart_constructor_exists():
    assert callable(dbl::CallPart.__init__)


def test_dbl::callpart_constructor_args():
    sig = inspect.signature(dbl::CallPart.__init__)
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



def test_dbl::sizeofarray_is_not_abstract():
    assert not inspect.isabstract(dbl::SizeOfArray)


def test_dbl::sizeofarray_constructor_exists():
    assert callable(dbl::SizeOfArray.__init__)


def test_dbl::sizeofarray_constructor_args():
    sig = inspect.signature(dbl::SizeOfArray.__init__)
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



def test_dbl::meliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::MeLiteral)


def test_dbl::meliteral_constructor_exists():
    assert callable(dbl::MeLiteral.__init__)


def test_dbl::meliteral_constructor_args():
    sig = inspect.signature(dbl::MeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::predefinedid_is_not_abstract():
    assert not inspect.isabstract(dbl::PredefinedId)


def test_dbl::predefinedid_constructor_exists():
    assert callable(dbl::PredefinedId.__init__)


def test_dbl::predefinedid_constructor_args():
    sig = inspect.signature(dbl::PredefinedId.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l3expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L3Expr)


def test_dbl::l3expr_constructor_exists():
    assert callable(dbl::L3Expr.__init__)


def test_dbl::l3expr_constructor_args():
    sig = inspect.signature(dbl::L3Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l4expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L4Expr)


def test_dbl::l4expr_constructor_exists():
    assert callable(dbl::L4Expr.__init__)


def test_dbl::l4expr_constructor_args():
    sig = inspect.signature(dbl::L4Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expandexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpandExpr)


def test_dbl::expandexpr_constructor_exists():
    assert callable(dbl::ExpandExpr.__init__)


def test_dbl::expandexpr_constructor_args():
    sig = inspect.signature(dbl::ExpandExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::metaexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::MetaExpr)


def test_dbl::metaexpr_constructor_exists():
    assert callable(dbl::MetaExpr.__init__)


def test_dbl::metaexpr_constructor_args():
    sig = inspect.signature(dbl::MetaExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::parseexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::ParseExpr)


def test_dbl::parseexpr_constructor_exists():
    assert callable(dbl::ParseExpr.__init__)


def test_dbl::parseexpr_constructor_args():
    sig = inspect.signature(dbl::ParseExpr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::elementaccess_is_not_abstract():
    assert not inspect.isabstract(dbl::ElementAccess)


def test_dbl::elementaccess_constructor_exists():
    assert callable(dbl::ElementAccess.__init__)


def test_dbl::elementaccess_constructor_args():
    sig = inspect.signature(dbl::ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l8expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L8Expr)


def test_dbl::l8expr_constructor_exists():
    assert callable(dbl::L8Expr.__init__)


def test_dbl::l8expr_constructor_args():
    sig = inspect.signature(dbl::L8Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(dbl::BinaryOperator)


def test_dbl::binaryoperator_constructor_exists():
    assert callable(dbl::BinaryOperator.__init__)


def test_dbl::binaryoperator_constructor_args():
    sig = inspect.signature(dbl::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l9expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L9Expr)


def test_dbl::l9expr_constructor_exists():
    assert callable(dbl::L9Expr.__init__)


def test_dbl::l9expr_constructor_args():
    sig = inspect.signature(dbl::L9Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l7expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L7Expr)


def test_dbl::l7expr_constructor_exists():
    assert callable(dbl::L7Expr.__init__)


def test_dbl::l7expr_constructor_args():
    sig = inspect.signature(dbl::L7Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expandexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::ExpandExpression)


def test_dbl::expandexpression_constructor_exists():
    assert callable(dbl::ExpandExpression.__init__)


def test_dbl::expandexpression_constructor_args():
    sig = inspect.signature(dbl::ExpandExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l5expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L5Expr)


def test_dbl::l5expr_constructor_exists():
    assert callable(dbl::L5Expr.__init__)


def test_dbl::l5expr_constructor_args():
    sig = inspect.signature(dbl::L5Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l6expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L6Expr)


def test_dbl::l6expr_constructor_exists():
    assert callable(dbl::L6Expr.__init__)


def test_dbl::l6expr_constructor_args():
    sig = inspect.signature(dbl::L6Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::l2expr_is_not_abstract():
    assert not inspect.isabstract(dbl::L2Expr)


def test_dbl::l2expr_constructor_exists():
    assert callable(dbl::L2Expr.__init__)


def test_dbl::l2expr_constructor_args():
    sig = inspect.signature(dbl::L2Expr.__init__)
    params = list(sig.parameters.keys())



def test_dbl::codequoteexpression_is_not_abstract():
    assert not inspect.isabstract(dbl::CodeQuoteExpression)


def test_dbl::codequoteexpression_constructor_exists():
    assert callable(dbl::CodeQuoteExpression.__init__)


def test_dbl::codequoteexpression_constructor_args():
    sig = inspect.signature(dbl::CodeQuoteExpression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(dbl::UnaryOperator)


def test_dbl::unaryoperator_constructor_exists():
    assert callable(dbl::UnaryOperator.__init__)


def test_dbl::unaryoperator_constructor_args():
    sig = inspect.signature(dbl::UnaryOperator.__init__)
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



def test_dbl::idexpr_is_not_abstract():
    assert not inspect.isabstract(dbl::IdExpr)


def test_dbl::idexpr_constructor_exists():
    assert callable(dbl::IdExpr.__init__)


def test_dbl::idexpr_constructor_args():
    sig = inspect.signature(dbl::IdExpr.__init__)
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



def test_dbl::activeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::ActiveLiteral)


def test_dbl::activeliteral_constructor_exists():
    assert callable(dbl::ActiveLiteral.__init__)


def test_dbl::activeliteral_constructor_args():
    sig = inspect.signature(dbl::ActiveLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::timeliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::TimeLiteral)


def test_dbl::timeliteral_constructor_exists():
    assert callable(dbl::TimeLiteral.__init__)


def test_dbl::timeliteral_constructor_args():
    sig = inspect.signature(dbl::TimeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::nullliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::NullLiteral)


def test_dbl::nullliteral_constructor_exists():
    assert callable(dbl::NullLiteral.__init__)


def test_dbl::nullliteral_constructor_args():
    sig = inspect.signature(dbl::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::falseliteral_is_not_abstract():
    assert not inspect.isabstract(dbl::FalseLiteral)


def test_dbl::falseliteral_constructor_exists():
    assert callable(dbl::FalseLiteral.__init__)


def test_dbl::falseliteral_constructor_args():
    sig = inspect.signature(dbl::FalseLiteral.__init__)
    params = list(sig.parameters.keys())



def test_dbl::createobject_is_not_abstract():
    assert not inspect.isabstract(dbl::CreateObject)


def test_dbl::createobject_constructor_exists():
    assert callable(dbl::CreateObject.__init__)


def test_dbl::createobject_constructor_args():
    sig = inspect.signature(dbl::CreateObject.__init__)
    params = list(sig.parameters.keys())



def test_l2expr_is_not_abstract():
    assert not inspect.isabstract(L2Expr)


def test_l2expr_constructor_exists():
    assert callable(L2Expr.__init__)


def test_l2expr_constructor_args():
    sig = inspect.signature(L2Expr.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(UnaryOperator)


def test_unaryoperator_constructor_exists():
    assert callable(UnaryOperator.__init__)


def test_unaryoperator_constructor_args():
    sig = inspect.signature(UnaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl::cast_is_not_abstract():
    assert not inspect.isabstract(dbl::Cast)


def test_dbl::cast_constructor_exists():
    assert callable(dbl::Cast.__init__)


def test_dbl::cast_constructor_args():
    sig = inspect.signature(dbl::Cast.__init__)
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



def test_l3expr_is_not_abstract():
    assert not inspect.isabstract(L3Expr)


def test_l3expr_constructor_exists():
    assert callable(L3Expr.__init__)


def test_l3expr_constructor_args():
    sig = inspect.signature(L3Expr.__init__)
    params = list(sig.parameters.keys())



def test_l4expr_is_not_abstract():
    assert not inspect.isabstract(L4Expr)


def test_l4expr_constructor_exists():
    assert callable(L4Expr.__init__)


def test_l4expr_constructor_args():
    sig = inspect.signature(L4Expr.__init__)
    params = list(sig.parameters.keys())



def test_l5expr_is_not_abstract():
    assert not inspect.isabstract(L5Expr)


def test_l5expr_constructor_exists():
    assert callable(L5Expr.__init__)


def test_l5expr_constructor_args():
    sig = inspect.signature(L5Expr.__init__)
    params = list(sig.parameters.keys())



def test_l6expr_is_not_abstract():
    assert not inspect.isabstract(L6Expr)


def test_l6expr_constructor_exists():
    assert callable(L6Expr.__init__)


def test_l6expr_constructor_args():
    sig = inspect.signature(L6Expr.__init__)
    params = list(sig.parameters.keys())



def test_l7expr_is_not_abstract():
    assert not inspect.isabstract(L7Expr)


def test_l7expr_constructor_exists():
    assert callable(L7Expr.__init__)


def test_l7expr_constructor_args():
    sig = inspect.signature(L7Expr.__init__)
    params = list(sig.parameters.keys())



def test_l8expr_is_not_abstract():
    assert not inspect.isabstract(L8Expr)


def test_l8expr_constructor_exists():
    assert callable(L8Expr.__init__)


def test_l8expr_constructor_args():
    sig = inspect.signature(L8Expr.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_dbl::greater_is_not_abstract():
    assert not inspect.isabstract(dbl::Greater)


def test_dbl::greater_constructor_exists():
    assert callable(dbl::Greater.__init__)


def test_dbl::greater_constructor_args():
    sig = inspect.signature(dbl::Greater.__init__)
    params = list(sig.parameters.keys())



def test_dbl::plus_is_not_abstract():
    assert not inspect.isabstract(dbl::Plus)


def test_dbl::plus_constructor_exists():
    assert callable(dbl::Plus.__init__)


def test_dbl::plus_constructor_args():
    sig = inspect.signature(dbl::Plus.__init__)
    params = list(sig.parameters.keys())



def test_dbl::and_is_not_abstract():
    assert not inspect.isabstract(dbl::And)


def test_dbl::and_constructor_exists():
    assert callable(dbl::And.__init__)


def test_dbl::and_constructor_args():
    sig = inspect.signature(dbl::And.__init__)
    params = list(sig.parameters.keys())



def test_dbl::mul_is_not_abstract():
    assert not inspect.isabstract(dbl::Mul)


def test_dbl::mul_constructor_exists():
    assert callable(dbl::Mul.__init__)


def test_dbl::mul_constructor_args():
    sig = inspect.signature(dbl::Mul.__init__)
    params = list(sig.parameters.keys())



def test_dbl::less_is_not_abstract():
    assert not inspect.isabstract(dbl::Less)


def test_dbl::less_constructor_exists():
    assert callable(dbl::Less.__init__)


def test_dbl::less_constructor_args():
    sig = inspect.signature(dbl::Less.__init__)
    params = list(sig.parameters.keys())



def test_dbl::mod_is_not_abstract():
    assert not inspect.isabstract(dbl::Mod)


def test_dbl::mod_constructor_exists():
    assert callable(dbl::Mod.__init__)


def test_dbl::mod_constructor_args():
    sig = inspect.signature(dbl::Mod.__init__)
    params = list(sig.parameters.keys())



def test_dbl::div_is_not_abstract():
    assert not inspect.isabstract(dbl::Div)


def test_dbl::div_constructor_exists():
    assert callable(dbl::Div.__init__)


def test_dbl::div_constructor_args():
    sig = inspect.signature(dbl::Div.__init__)
    params = list(sig.parameters.keys())



def test_dbl::instanceof_is_not_abstract():
    assert not inspect.isabstract(dbl::InstanceOf)


def test_dbl::instanceof_constructor_exists():
    assert callable(dbl::InstanceOf.__init__)


def test_dbl::instanceof_constructor_args():
    sig = inspect.signature(dbl::InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_dbl::notequal_is_not_abstract():
    assert not inspect.isabstract(dbl::NotEqual)


def test_dbl::notequal_constructor_exists():
    assert callable(dbl::NotEqual.__init__)


def test_dbl::notequal_constructor_args():
    sig = inspect.signature(dbl::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl::equal_is_not_abstract():
    assert not inspect.isabstract(dbl::Equal)


def test_dbl::equal_constructor_exists():
    assert callable(dbl::Equal.__init__)


def test_dbl::equal_constructor_args():
    sig = inspect.signature(dbl::Equal.__init__)
    params = list(sig.parameters.keys())



def test_dbl::lessequal_is_not_abstract():
    assert not inspect.isabstract(dbl::LessEqual)


def test_dbl::lessequal_constructor_exists():
    assert callable(dbl::LessEqual.__init__)


def test_dbl::lessequal_constructor_args():
    sig = inspect.signature(dbl::LessEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl::minus_is_not_abstract():
    assert not inspect.isabstract(dbl::Minus)


def test_dbl::minus_constructor_exists():
    assert callable(dbl::Minus.__init__)


def test_dbl::minus_constructor_args():
    sig = inspect.signature(dbl::Minus.__init__)
    params = list(sig.parameters.keys())



def test_dbl::greaterequal_is_not_abstract():
    assert not inspect.isabstract(dbl::GreaterEqual)


def test_dbl::greaterequal_constructor_exists():
    assert callable(dbl::GreaterEqual.__init__)


def test_dbl::greaterequal_constructor_args():
    sig = inspect.signature(dbl::GreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_dbl::or_is_not_abstract():
    assert not inspect.isabstract(dbl::Or)


def test_dbl::or_constructor_exists():
    assert callable(dbl::Or.__init__)


def test_dbl::or_constructor_args():
    sig = inspect.signature(dbl::Or.__init__)
    params = list(sig.parameters.keys())



def test_dbl::localscope_is_not_abstract():
    assert not inspect.isabstract(dbl::LocalScope)


def test_dbl::localscope_constructor_exists():
    assert callable(dbl::LocalScope.__init__)


def test_dbl::localscope_constructor_args():
    sig = inspect.signature(dbl::LocalScope.__init__)
    params = list(sig.parameters.keys())



def test_dbl::ifstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::IfStatement)


def test_dbl::ifstatement_constructor_exists():
    assert callable(dbl::IfStatement.__init__)


def test_dbl::ifstatement_constructor_args():
    sig = inspect.signature(dbl::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::switchcase_is_not_abstract():
    assert not inspect.isabstract(dbl::SwitchCase)


def test_dbl::switchcase_constructor_exists():
    assert callable(dbl::SwitchCase.__init__)


def test_dbl::switchcase_constructor_args():
    sig = inspect.signature(dbl::SwitchCase.__init__)
    params = list(sig.parameters.keys())



def test_loopstatement_is_not_abstract():
    assert not inspect.isabstract(LoopStatement)


def test_loopstatement_constructor_exists():
    assert callable(LoopStatement.__init__)


def test_loopstatement_constructor_args():
    sig = inspect.signature(LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::whilestatement_is_not_abstract():
    assert not inspect.isabstract(dbl::WhileStatement)


def test_dbl::whilestatement_constructor_exists():
    assert callable(dbl::WhileStatement.__init__)


def test_dbl::whilestatement_constructor_args():
    sig = inspect.signature(dbl::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::forstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ForStatement)


def test_dbl::forstatement_constructor_exists():
    assert callable(dbl::ForStatement.__init__)


def test_dbl::forstatement_constructor_args():
    sig = inspect.signature(dbl::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_extensibleelement_is_not_abstract():
    assert not inspect.isabstract(ExtensibleElement)


def test_extensibleelement_constructor_exists():
    assert callable(ExtensibleElement.__init__)


def test_extensibleelement_constructor_args():
    sig = inspect.signature(ExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::textualsyntaxdef_is_not_abstract():
    assert not inspect.isabstract(dbl::TextualSyntaxDef)


def test_dbl::textualsyntaxdef_constructor_exists():
    assert callable(dbl::TextualSyntaxDef.__init__)


def test_dbl::textualsyntaxdef_constructor_args():
    sig = inspect.signature(dbl::TextualSyntaxDef.__init__)
    params = list(sig.parameters.keys())



def test_dbl::classcontentextension_is_not_abstract():
    assert not inspect.isabstract(dbl::ClassContentExtension)


def test_dbl::classcontentextension_constructor_exists():
    assert callable(dbl::ClassContentExtension.__init__)


def test_dbl::classcontentextension_constructor_args():
    sig = inspect.signature(dbl::ClassContentExtension.__init__)
    params = list(sig.parameters.keys())



def test_dbl::expression_is_not_abstract():
    assert not inspect.isabstract(dbl::Expression)


def test_dbl::expression_constructor_exists():
    assert callable(dbl::Expression.__init__)


def test_dbl::expression_constructor_args():
    sig = inspect.signature(dbl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_dbl::modulecontentextension_is_not_abstract():
    assert not inspect.isabstract(dbl::ModuleContentExtension)


def test_dbl::modulecontentextension_constructor_exists():
    assert callable(dbl::ModuleContentExtension.__init__)


def test_dbl::modulecontentextension_constructor_args():
    sig = inspect.signature(dbl::ModuleContentExtension.__init__)
    params = list(sig.parameters.keys())



def test_dbl::extensiondefinition_is_not_abstract():
    assert not inspect.isabstract(dbl::ExtensionDefinition)


def test_dbl::extensiondefinition_constructor_exists():
    assert callable(dbl::ExtensionDefinition.__init__)


def test_dbl::extensiondefinition_constructor_args():
    sig = inspect.signature(dbl::ExtensionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dbl::languageconstructclassifier_is_not_abstract():
    assert not inspect.isabstract(dbl::LanguageConstructClassifier)


def test_dbl::languageconstructclassifier_constructor_exists():
    assert callable(dbl::LanguageConstructClassifier.__init__)


def test_dbl::languageconstructclassifier_constructor_args():
    sig = inspect.signature(dbl::LanguageConstructClassifier.__init__)
    params = list(sig.parameters.keys())



def test_dbl::statement_is_not_abstract():
    assert not inspect.isabstract(dbl::Statement)


def test_dbl::statement_constructor_exists():
    assert callable(dbl::Statement.__init__)


def test_dbl::statement_constructor_args():
    sig = inspect.signature(dbl::Statement.__init__)
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



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
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



def test_dbl::procedurecall_is_not_abstract():
    assert not inspect.isabstract(dbl::ProcedureCall)


def test_dbl::procedurecall_constructor_exists():
    assert callable(dbl::ProcedureCall.__init__)


def test_dbl::procedurecall_constructor_args():
    sig = inspect.signature(dbl::ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_dbl::advance_is_not_abstract():
    assert not inspect.isabstract(dbl::Advance)


def test_dbl::advance_constructor_exists():
    assert callable(dbl::Advance.__init__)


def test_dbl::advance_constructor_args():
    sig = inspect.signature(dbl::Advance.__init__)
    params = list(sig.parameters.keys())



def test_dbl::switchstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::SwitchStatement)


def test_dbl::switchstatement_constructor_exists():
    assert callable(dbl::SwitchStatement.__init__)


def test_dbl::switchstatement_constructor_args():
    sig = inspect.signature(dbl::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::localscopestatement_is_not_abstract():
    assert not inspect.isabstract(dbl::LocalScopeStatement)


def test_dbl::localscopestatement_constructor_exists():
    assert callable(dbl::LocalScopeStatement.__init__)


def test_dbl::localscopestatement_constructor_args():
    sig = inspect.signature(dbl::LocalScopeStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::waituntil_is_not_abstract():
    assert not inspect.isabstract(dbl::WaitUntil)


def test_dbl::waituntil_constructor_exists():
    assert callable(dbl::WaitUntil.__init__)


def test_dbl::waituntil_constructor_args():
    sig = inspect.signature(dbl::WaitUntil.__init__)
    params = list(sig.parameters.keys())



def test_dbl::savegenstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::SaveGenStatement)


def test_dbl::savegenstatement_constructor_exists():
    assert callable(dbl::SaveGenStatement.__init__)


def test_dbl::savegenstatement_constructor_args():
    sig = inspect.signature(dbl::SaveGenStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::reactivate_is_not_abstract():
    assert not inspect.isabstract(dbl::Reactivate)


def test_dbl::reactivate_constructor_exists():
    assert callable(dbl::Reactivate.__init__)


def test_dbl::reactivate_constructor_args():
    sig = inspect.signature(dbl::Reactivate.__init__)
    params = list(sig.parameters.keys())



def test_dbl::wait_is_not_abstract():
    assert not inspect.isabstract(dbl::Wait)


def test_dbl::wait_constructor_exists():
    assert callable(dbl::Wait.__init__)


def test_dbl::wait_constructor_args():
    sig = inspect.signature(dbl::Wait.__init__)
    params = list(sig.parameters.keys())



def test_dbl::assignment_is_not_abstract():
    assert not inspect.isabstract(dbl::Assignment)


def test_dbl::assignment_constructor_exists():
    assert callable(dbl::Assignment.__init__)


def test_dbl::assignment_constructor_args():
    sig = inspect.signature(dbl::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_dbl::continuestatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ContinueStatement)


def test_dbl::continuestatement_constructor_exists():
    assert callable(dbl::ContinueStatement.__init__)


def test_dbl::continuestatement_constructor_args():
    sig = inspect.signature(dbl::ContinueStatement.__init__)
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



def test_dbl::return_is_not_abstract():
    assert not inspect.isabstract(dbl::Return)


def test_dbl::return_constructor_exists():
    assert callable(dbl::Return.__init__)


def test_dbl::return_constructor_args():
    sig = inspect.signature(dbl::Return.__init__)
    params = list(sig.parameters.keys())



def test_dbl::yield_is_not_abstract():
    assert not inspect.isabstract(dbl::Yield)


def test_dbl::yield_constructor_exists():
    assert callable(dbl::Yield.__init__)


def test_dbl::yield_constructor_args():
    sig = inspect.signature(dbl::Yield.__init__)
    params = list(sig.parameters.keys())



def test_dbl::breakstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::BreakStatement)


def test_dbl::breakstatement_constructor_exists():
    assert callable(dbl::BreakStatement.__init__)


def test_dbl::breakstatement_constructor_args():
    sig = inspect.signature(dbl::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::resumegenstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ResumeGenStatement)


def test_dbl::resumegenstatement_constructor_exists():
    assert callable(dbl::ResumeGenStatement.__init__)


def test_dbl::resumegenstatement_constructor_args():
    sig = inspect.signature(dbl::ResumeGenStatement.__init__)
    params = list(sig.parameters.keys())



def test_dbl::terminate_is_not_abstract():
    assert not inspect.isabstract(dbl::Terminate)


def test_dbl::terminate_constructor_exists():
    assert callable(dbl::Terminate.__init__)


def test_dbl::terminate_constructor_args():
    sig = inspect.signature(dbl::Terminate.__init__)
    params = list(sig.parameters.keys())



def test_dbl::print_is_not_abstract():
    assert not inspect.isabstract(dbl::Print)


def test_dbl::print_constructor_exists():
    assert callable(dbl::Print.__init__)


def test_dbl::print_constructor_args():
    sig = inspect.signature(dbl::Print.__init__)
    params = list(sig.parameters.keys())



def test_dbl::resetgencontextstatement_is_not_abstract():
    assert not inspect.isabstract(dbl::ResetGenContextStatement)


def test_dbl::resetgencontextstatement_constructor_exists():
    assert callable(dbl::ResetGenContextStatement.__init__)


def test_dbl::resetgencontextstatement_constructor_args():
    sig = inspect.signature(dbl::ResetGenContextStatement.__init__)
    params = list(sig.parameters.keys())



def test_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_dbl::parameter_is_not_abstract():
    assert not inspect.isabstract(dbl::Parameter)


def test_dbl::parameter_constructor_exists():
    assert callable(dbl::Parameter.__init__)


def test_dbl::parameter_constructor_args():
    sig = inspect.signature(dbl::Parameter.__init__)
    params = list(sig.parameters.keys())



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



def test_dbl::abstractvariable_is_not_abstract():
    assert not inspect.isabstract(dbl::AbstractVariable)


def test_dbl::abstractvariable_constructor_exists():
    assert callable(dbl::AbstractVariable.__init__)


def test_dbl::abstractvariable_constructor_args():
    sig = inspect.signature(dbl::AbstractVariable.__init__)
    params = list(sig.parameters.keys())


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
Statement_strategy = st.builds(
    Statement,
)
dbl::SimpleStatement_strategy = st.builds(
    dbl::SimpleStatement,
)
dbl::LoopStatement_strategy = st.builds(
    dbl::LoopStatement,
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
LocalScope_strategy = st.builds(
    LocalScope,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
dbl::Constructor_strategy = st.builds(
    dbl::Constructor,
)
LanguageConceptClassifier_strategy = st.builds(
    LanguageConceptClassifier,
)
ClassSimilar_strategy = st.builds(
    ClassSimilar,
)
Classifier_strategy = st.builds(
    Classifier,
)
dbl::ClassPart_strategy = st.builds(
    dbl::ClassPart,
)
dbl::SuperClassSpecification_strategy = st.builds(
    dbl::SuperClassSpecification,
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
dbl::Import_strategy = st.builds(
    dbl::Import,
    file=
        safe_text
)
dbl::Model_strategy = st.builds(
    dbl::Model,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
dbl::BoolType_strategy = st.builds(
    dbl::BoolType,
)
dbl::StringType_strategy = st.builds(
    dbl::StringType,
)
dbl::IntType_strategy = st.builds(
    dbl::IntType,
)
dbl::DoubleType_strategy = st.builds(
    dbl::DoubleType,
)
dbl::VoidType_strategy = st.builds(
    dbl::VoidType,
)
Type_strategy = st.builds(
    Type,
)
dbl::PrimitiveType_strategy = st.builds(
    dbl::PrimitiveType,
)
dbl::TypedElement_strategy = st.builds(
    dbl::TypedElement,
)
dbl::ArrayDimension_strategy = st.builds(
    dbl::ArrayDimension,
)
dbl::Type_strategy = st.builds(
    dbl::Type,
)
dbl::ModifierExtensionsContainer_strategy = st.builds(
    dbl::ModifierExtensionsContainer,
)
dbl::EmbeddableExtensionsContainer_strategy = st.builds(
    dbl::EmbeddableExtensionsContainer,
)
Construct_strategy = st.builds(
    Construct,
)
dbl::Clazz_strategy = st.builds(
    dbl::Clazz,
    active=
        st.booleans()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
dbl::Classifier_strategy = st.builds(
    dbl::Classifier,
)
dbl::Module_strategy = st.builds(
    dbl::Module,
)
dbl::Procedure_strategy = st.builds(
    dbl::Procedure,
    clazz=
        st.booleans(),
    abstract=
        st.booleans()
)
dbl::ExtensibleElement_strategy = st.builds(
    dbl::ExtensibleElement,
    instanceOfExtensionDefinition=
        st.booleans(),
    concreteSyntax=
        safe_text
)
dbl::Construct_strategy = st.builds(
    dbl::Construct,
)
dbl::Pattern_strategy = st.builds(
    dbl::Pattern,
    top=
        st.booleans()
)
Module_strategy = st.builds(
    Module,
)
dbl::TestStatement_strategy = st.builds(
    dbl::TestStatement,
    value=
        st.integers()
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
dbl::QuotedClassContent_strategy = st.builds(
    dbl::QuotedClassContent,
)
dbl::QuotedExpression_strategy = st.builds(
    dbl::QuotedExpression,
)
dbl::QuotedCode_strategy = st.builds(
    dbl::QuotedCode,
)
dbl::ExpandStatement_strategy = st.builds(
    dbl::ExpandStatement,
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
PropertyType_strategy = st.builds(
    PropertyType,
)
dbl::IdPropertyType_strategy = st.builds(
    dbl::IdPropertyType,
)
dbl::PropertyType_strategy = st.builds(
    dbl::PropertyType,
)
dbl::MappingStatement_strategy = st.builds(
    dbl::MappingStatement,
)
dbl::TargetStatement_strategy = st.builds(
    dbl::TargetStatement,
)
dbl::MappingPart_strategy = st.builds(
    dbl::MappingPart,
)
LocalScopeStatement_strategy = st.builds(
    LocalScopeStatement,
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
dbl::StructuredPropertyType_strategy = st.builds(
    dbl::StructuredPropertyType,
)
dbl::BooleanPropertyType_strategy = st.builds(
    dbl::BooleanPropertyType,
    terminal=
        safe_text
)
dbl::StringPropertyType_strategy = st.builds(
    dbl::StringPropertyType,
)
dbl::IntPropertyType_strategy = st.builds(
    dbl::IntPropertyType,
)
VariableAccess_strategy = st.builds(
    VariableAccess,
)
L1RhsExpr_strategy = st.builds(
    L1RhsExpr,
)
dbl::RhsClassifierExpr_strategy = st.builds(
    dbl::RhsClassifierExpr,
)
dbl::PropertyBindingExpr_strategy = st.builds(
    dbl::PropertyBindingExpr,
)
dbl::MetaAccess_strategy = st.builds(
    dbl::MetaAccess,
)
dbl::TerminalExpr_strategy = st.builds(
    dbl::TerminalExpr,
    terminal=
        safe_text
)
L2RhsExpr_strategy = st.builds(
    L2RhsExpr,
)
dbl::SequenceExpr_strategy = st.builds(
    dbl::SequenceExpr,
)
ElementAccess_strategy = st.builds(
    ElementAccess,
)
dbl::TypeAccess_strategy = st.builds(
    dbl::TypeAccess,
)
dbl::VariableAccess_strategy = st.builds(
    dbl::VariableAccess,
)
RhsExpression_strategy = st.builds(
    RhsExpression,
)
dbl::L1RhsExpr_strategy = st.builds(
    dbl::L1RhsExpr,
)
dbl::L2RhsExpr_strategy = st.builds(
    dbl::L2RhsExpr,
)
dbl::L3RhsExpr_strategy = st.builds(
    dbl::L3RhsExpr,
)
dbl::RhsExpression_strategy = st.builds(
    dbl::RhsExpression,
)
LanguageConstructClassifier_strategy = st.builds(
    LanguageConstructClassifier,
)
dbl::LanguageConceptClassifier_strategy = st.builds(
    dbl::LanguageConceptClassifier,
)
dbl::TsRule_strategy = st.builds(
    dbl::TsRule,
)
dbl::Mapping_strategy = st.builds(
    dbl::Mapping,
)
dbl::CallPart_strategy = st.builds(
    dbl::CallPart,
)
PredefinedId_strategy = st.builds(
    PredefinedId,
)
dbl::MetaLiteral_strategy = st.builds(
    dbl::MetaLiteral,
)
dbl::SizeOfArray_strategy = st.builds(
    dbl::SizeOfArray,
)
dbl::TypeLiteral_strategy = st.builds(
    dbl::TypeLiteral,
)
dbl::SuperLiteral_strategy = st.builds(
    dbl::SuperLiteral,
)
dbl::MeLiteral_strategy = st.builds(
    dbl::MeLiteral,
)
dbl::PredefinedId_strategy = st.builds(
    dbl::PredefinedId,
)
Expression_strategy = st.builds(
    Expression,
)
dbl::L3Expr_strategy = st.builds(
    dbl::L3Expr,
)
dbl::L4Expr_strategy = st.builds(
    dbl::L4Expr,
)
dbl::ExpandExpr_strategy = st.builds(
    dbl::ExpandExpr,
)
dbl::MetaExpr_strategy = st.builds(
    dbl::MetaExpr,
)
dbl::ParseExpr_strategy = st.builds(
    dbl::ParseExpr,
)
dbl::ElementAccess_strategy = st.builds(
    dbl::ElementAccess,
)
dbl::L8Expr_strategy = st.builds(
    dbl::L8Expr,
)
dbl::BinaryOperator_strategy = st.builds(
    dbl::BinaryOperator,
)
dbl::L9Expr_strategy = st.builds(
    dbl::L9Expr,
)
dbl::L7Expr_strategy = st.builds(
    dbl::L7Expr,
)
dbl::ExpandExpression_strategy = st.builds(
    dbl::ExpandExpression,
)
dbl::L5Expr_strategy = st.builds(
    dbl::L5Expr,
)
dbl::L6Expr_strategy = st.builds(
    dbl::L6Expr,
)
dbl::L2Expr_strategy = st.builds(
    dbl::L2Expr,
)
dbl::CodeQuoteExpression_strategy = st.builds(
    dbl::CodeQuoteExpression,
)
dbl::UnaryOperator_strategy = st.builds(
    dbl::UnaryOperator,
)
dbl::L1Expr_strategy = st.builds(
    dbl::L1Expr,
)
L1Expr_strategy = st.builds(
    L1Expr,
)
dbl::IdExpr_strategy = st.builds(
    dbl::IdExpr,
)
dbl::DoubleLiteral_strategy = st.builds(
    dbl::DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dbl::StringLiteral_strategy = st.builds(
    dbl::StringLiteral,
    value=
        safe_text
)
dbl::TrueLiteral_strategy = st.builds(
    dbl::TrueLiteral,
)
dbl::IntLiteral_strategy = st.builds(
    dbl::IntLiteral,
    value=
        st.integers()
)
dbl::ActiveLiteral_strategy = st.builds(
    dbl::ActiveLiteral,
)
dbl::TimeLiteral_strategy = st.builds(
    dbl::TimeLiteral,
)
dbl::NullLiteral_strategy = st.builds(
    dbl::NullLiteral,
)
dbl::FalseLiteral_strategy = st.builds(
    dbl::FalseLiteral,
)
dbl::CreateObject_strategy = st.builds(
    dbl::CreateObject,
)
L2Expr_strategy = st.builds(
    L2Expr,
)
UnaryOperator_strategy = st.builds(
    UnaryOperator,
)
dbl::Cast_strategy = st.builds(
    dbl::Cast,
)
dbl::Not_strategy = st.builds(
    dbl::Not,
)
dbl::Neg_strategy = st.builds(
    dbl::Neg,
)
L3Expr_strategy = st.builds(
    L3Expr,
)
L4Expr_strategy = st.builds(
    L4Expr,
)
L5Expr_strategy = st.builds(
    L5Expr,
)
L6Expr_strategy = st.builds(
    L6Expr,
)
L7Expr_strategy = st.builds(
    L7Expr,
)
L8Expr_strategy = st.builds(
    L8Expr,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
dbl::Greater_strategy = st.builds(
    dbl::Greater,
)
dbl::Plus_strategy = st.builds(
    dbl::Plus,
)
dbl::And_strategy = st.builds(
    dbl::And,
)
dbl::Mul_strategy = st.builds(
    dbl::Mul,
)
dbl::Less_strategy = st.builds(
    dbl::Less,
)
dbl::Mod_strategy = st.builds(
    dbl::Mod,
)
dbl::Div_strategy = st.builds(
    dbl::Div,
)
dbl::InstanceOf_strategy = st.builds(
    dbl::InstanceOf,
)
dbl::NotEqual_strategy = st.builds(
    dbl::NotEqual,
)
dbl::Equal_strategy = st.builds(
    dbl::Equal,
)
dbl::LessEqual_strategy = st.builds(
    dbl::LessEqual,
)
dbl::Minus_strategy = st.builds(
    dbl::Minus,
)
dbl::GreaterEqual_strategy = st.builds(
    dbl::GreaterEqual,
)
dbl::Or_strategy = st.builds(
    dbl::Or,
)
dbl::LocalScope_strategy = st.builds(
    dbl::LocalScope,
)
dbl::IfStatement_strategy = st.builds(
    dbl::IfStatement,
)
dbl::SwitchCase_strategy = st.builds(
    dbl::SwitchCase,
)
LoopStatement_strategy = st.builds(
    LoopStatement,
)
dbl::WhileStatement_strategy = st.builds(
    dbl::WhileStatement,
)
dbl::ForStatement_strategy = st.builds(
    dbl::ForStatement,
)
ExtensibleElement_strategy = st.builds(
    ExtensibleElement,
)
dbl::TextualSyntaxDef_strategy = st.builds(
    dbl::TextualSyntaxDef,
)
dbl::ClassContentExtension_strategy = st.builds(
    dbl::ClassContentExtension,
)
dbl::Expression_strategy = st.builds(
    dbl::Expression,
)
dbl::ModuleContentExtension_strategy = st.builds(
    dbl::ModuleContentExtension,
)
dbl::ExtensionDefinition_strategy = st.builds(
    dbl::ExtensionDefinition,
)
dbl::LanguageConstructClassifier_strategy = st.builds(
    dbl::LanguageConstructClassifier,
)
dbl::Statement_strategy = st.builds(
    dbl::Statement,
)
dbl::NamedElement_strategy = st.builds(
    dbl::NamedElement,
    name=
        safe_text
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
dbl::SetGenContextStatement_strategy = st.builds(
    dbl::SetGenContextStatement,
    addAfterContext=
        st.booleans()
)
dbl::ProcedureCall_strategy = st.builds(
    dbl::ProcedureCall,
)
dbl::Advance_strategy = st.builds(
    dbl::Advance,
)
dbl::SwitchStatement_strategy = st.builds(
    dbl::SwitchStatement,
)
dbl::LocalScopeStatement_strategy = st.builds(
    dbl::LocalScopeStatement,
)
dbl::WaitUntil_strategy = st.builds(
    dbl::WaitUntil,
)
dbl::SaveGenStatement_strategy = st.builds(
    dbl::SaveGenStatement,
)
dbl::Reactivate_strategy = st.builds(
    dbl::Reactivate,
)
dbl::Wait_strategy = st.builds(
    dbl::Wait,
)
dbl::Assignment_strategy = st.builds(
    dbl::Assignment,
)
dbl::ContinueStatement_strategy = st.builds(
    dbl::ContinueStatement,
)
dbl::ActivateObject_strategy = st.builds(
    dbl::ActivateObject,
    priority=
        st.integers()
)
dbl::Return_strategy = st.builds(
    dbl::Return,
)
dbl::Yield_strategy = st.builds(
    dbl::Yield,
)
dbl::BreakStatement_strategy = st.builds(
    dbl::BreakStatement,
)
dbl::ResumeGenStatement_strategy = st.builds(
    dbl::ResumeGenStatement,
)
dbl::Terminate_strategy = st.builds(
    dbl::Terminate,
)
dbl::Print_strategy = st.builds(
    dbl::Print,
)
dbl::ResetGenContextStatement_strategy = st.builds(
    dbl::ResetGenContextStatement,
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
dbl::Parameter_strategy = st.builds(
    dbl::Parameter,
)
dbl::Variable_strategy = st.builds(
    dbl::Variable,
    control=
        st.booleans(),
    clazz=
        st.booleans()
)
dbl::AbstractVariable_strategy = st.builds(
    dbl::AbstractVariable,
)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=dbl::SimpleStatement_strategy)
@settings(max_examples=50)
def test_dbl::simplestatement_instantiation(instance):
    assert isinstance(instance, dbl::SimpleStatement)

@given(instance=dbl::LoopStatement_strategy)
@settings(max_examples=50)
def test_dbl::loopstatement_instantiation(instance):
    assert isinstance(instance, dbl::LoopStatement)

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

@given(instance=LocalScope_strategy)
@settings(max_examples=50)
def test_localscope_instantiation(instance):
    assert isinstance(instance, LocalScope)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=dbl::Constructor_strategy)
@settings(max_examples=50)
def test_dbl::constructor_instantiation(instance):
    assert isinstance(instance, dbl::Constructor)

@given(instance=LanguageConceptClassifier_strategy)
@settings(max_examples=50)
def test_languageconceptclassifier_instantiation(instance):
    assert isinstance(instance, LanguageConceptClassifier)

@given(instance=ClassSimilar_strategy)
@settings(max_examples=50)
def test_classsimilar_instantiation(instance):
    assert isinstance(instance, ClassSimilar)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=dbl::ClassPart_strategy)
@settings(max_examples=50)
def test_dbl::classpart_instantiation(instance):
    assert isinstance(instance, dbl::ClassPart)

@given(instance=dbl::SuperClassSpecification_strategy)
@settings(max_examples=50)
def test_dbl::superclassspecification_instantiation(instance):
    assert isinstance(instance, dbl::SuperClassSpecification)

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

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=dbl::BoolType_strategy)
@settings(max_examples=50)
def test_dbl::booltype_instantiation(instance):
    assert isinstance(instance, dbl::BoolType)

@given(instance=dbl::StringType_strategy)
@settings(max_examples=50)
def test_dbl::stringtype_instantiation(instance):
    assert isinstance(instance, dbl::StringType)

@given(instance=dbl::IntType_strategy)
@settings(max_examples=50)
def test_dbl::inttype_instantiation(instance):
    assert isinstance(instance, dbl::IntType)

@given(instance=dbl::DoubleType_strategy)
@settings(max_examples=50)
def test_dbl::doubletype_instantiation(instance):
    assert isinstance(instance, dbl::DoubleType)

@given(instance=dbl::VoidType_strategy)
@settings(max_examples=50)
def test_dbl::voidtype_instantiation(instance):
    assert isinstance(instance, dbl::VoidType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=dbl::PrimitiveType_strategy)
@settings(max_examples=50)
def test_dbl::primitivetype_instantiation(instance):
    assert isinstance(instance, dbl::PrimitiveType)

@given(instance=dbl::TypedElement_strategy)
@settings(max_examples=50)
def test_dbl::typedelement_instantiation(instance):
    assert isinstance(instance, dbl::TypedElement)

@given(instance=dbl::ArrayDimension_strategy)
@settings(max_examples=50)
def test_dbl::arraydimension_instantiation(instance):
    assert isinstance(instance, dbl::ArrayDimension)

@given(instance=dbl::Type_strategy)
@settings(max_examples=50)
def test_dbl::type_instantiation(instance):
    assert isinstance(instance, dbl::Type)

@given(instance=dbl::ModifierExtensionsContainer_strategy)
@settings(max_examples=50)
def test_dbl::modifierextensionscontainer_instantiation(instance):
    assert isinstance(instance, dbl::ModifierExtensionsContainer)

@given(instance=dbl::EmbeddableExtensionsContainer_strategy)
@settings(max_examples=50)
def test_dbl::embeddableextensionscontainer_instantiation(instance):
    assert isinstance(instance, dbl::EmbeddableExtensionsContainer)

@given(instance=Construct_strategy)
@settings(max_examples=50)
def test_construct_instantiation(instance):
    assert isinstance(instance, Construct)

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

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dbl::Classifier_strategy)
@settings(max_examples=50)
def test_dbl::classifier_instantiation(instance):
    assert isinstance(instance, dbl::Classifier)

@given(instance=dbl::Module_strategy)
@settings(max_examples=50)
def test_dbl::module_instantiation(instance):
    assert isinstance(instance, dbl::Module)

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

@given(instance=dbl::Procedure_strategy)
def test_dbl::procedure_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=dbl::Procedure_strategy)
def test_dbl::procedure_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=dbl::ExtensibleElement_strategy)
@settings(max_examples=50)
def test_dbl::extensibleelement_instantiation(instance):
    assert isinstance(instance, dbl::ExtensibleElement)

@given(instance=dbl::ExtensibleElement_strategy)
def test_dbl::extensibleelement_instanceOfExtensionDefinition_type(instance):
    assert isinstance(instance.instanceOfExtensionDefinition, bool)


@given(instance=dbl::ExtensibleElement_strategy)
def test_dbl::extensibleelement_instanceOfExtensionDefinition_setter(instance):
    original = instance.instanceOfExtensionDefinition
    instance.instanceOfExtensionDefinition = original
    assert instance.instanceOfExtensionDefinition == original

@given(instance=dbl::ExtensibleElement_strategy)
def test_dbl::extensibleelement_concreteSyntax_type(instance):
    assert isinstance(instance.concreteSyntax, str)


@given(instance=dbl::ExtensibleElement_strategy)
def test_dbl::extensibleelement_concreteSyntax_setter(instance):
    original = instance.concreteSyntax
    instance.concreteSyntax = original
    assert instance.concreteSyntax == original

@given(instance=dbl::Construct_strategy)
@settings(max_examples=50)
def test_dbl::construct_instantiation(instance):
    assert isinstance(instance, dbl::Construct)

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

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=dbl::TestStatement_strategy)
@settings(max_examples=50)
def test_dbl::teststatement_instantiation(instance):
    assert isinstance(instance, dbl::TestStatement)

@given(instance=dbl::TestStatement_strategy)
def test_dbl::teststatement_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=dbl::TestStatement_strategy)
def test_dbl::teststatement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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

@given(instance=dbl::QuotedClassContent_strategy)
@settings(max_examples=50)
def test_dbl::quotedclasscontent_instantiation(instance):
    assert isinstance(instance, dbl::QuotedClassContent)

@given(instance=dbl::QuotedExpression_strategy)
@settings(max_examples=50)
def test_dbl::quotedexpression_instantiation(instance):
    assert isinstance(instance, dbl::QuotedExpression)

@given(instance=dbl::QuotedCode_strategy)
@settings(max_examples=50)
def test_dbl::quotedcode_instantiation(instance):
    assert isinstance(instance, dbl::QuotedCode)

@given(instance=dbl::ExpandStatement_strategy)
@settings(max_examples=50)
def test_dbl::expandstatement_instantiation(instance):
    assert isinstance(instance, dbl::ExpandStatement)

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

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=dbl::IdPropertyType_strategy)
@settings(max_examples=50)
def test_dbl::idpropertytype_instantiation(instance):
    assert isinstance(instance, dbl::IdPropertyType)

@given(instance=dbl::PropertyType_strategy)
@settings(max_examples=50)
def test_dbl::propertytype_instantiation(instance):
    assert isinstance(instance, dbl::PropertyType)

@given(instance=dbl::MappingStatement_strategy)
@settings(max_examples=50)
def test_dbl::mappingstatement_instantiation(instance):
    assert isinstance(instance, dbl::MappingStatement)

@given(instance=dbl::TargetStatement_strategy)
@settings(max_examples=50)
def test_dbl::targetstatement_instantiation(instance):
    assert isinstance(instance, dbl::TargetStatement)

@given(instance=dbl::MappingPart_strategy)
@settings(max_examples=50)
def test_dbl::mappingpart_instantiation(instance):
    assert isinstance(instance, dbl::MappingPart)

@given(instance=LocalScopeStatement_strategy)
@settings(max_examples=50)
def test_localscopestatement_instantiation(instance):
    assert isinstance(instance, LocalScopeStatement)

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

@given(instance=dbl::StructuredPropertyType_strategy)
@settings(max_examples=50)
def test_dbl::structuredpropertytype_instantiation(instance):
    assert isinstance(instance, dbl::StructuredPropertyType)

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

@given(instance=dbl::StringPropertyType_strategy)
@settings(max_examples=50)
def test_dbl::stringpropertytype_instantiation(instance):
    assert isinstance(instance, dbl::StringPropertyType)

@given(instance=dbl::IntPropertyType_strategy)
@settings(max_examples=50)
def test_dbl::intpropertytype_instantiation(instance):
    assert isinstance(instance, dbl::IntPropertyType)

@given(instance=VariableAccess_strategy)
@settings(max_examples=50)
def test_variableaccess_instantiation(instance):
    assert isinstance(instance, VariableAccess)

@given(instance=L1RhsExpr_strategy)
@settings(max_examples=50)
def test_l1rhsexpr_instantiation(instance):
    assert isinstance(instance, L1RhsExpr)

@given(instance=dbl::RhsClassifierExpr_strategy)
@settings(max_examples=50)
def test_dbl::rhsclassifierexpr_instantiation(instance):
    assert isinstance(instance, dbl::RhsClassifierExpr)

@given(instance=dbl::PropertyBindingExpr_strategy)
@settings(max_examples=50)
def test_dbl::propertybindingexpr_instantiation(instance):
    assert isinstance(instance, dbl::PropertyBindingExpr)

@given(instance=dbl::MetaAccess_strategy)
@settings(max_examples=50)
def test_dbl::metaaccess_instantiation(instance):
    assert isinstance(instance, dbl::MetaAccess)

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

@given(instance=L2RhsExpr_strategy)
@settings(max_examples=50)
def test_l2rhsexpr_instantiation(instance):
    assert isinstance(instance, L2RhsExpr)

@given(instance=dbl::SequenceExpr_strategy)
@settings(max_examples=50)
def test_dbl::sequenceexpr_instantiation(instance):
    assert isinstance(instance, dbl::SequenceExpr)

@given(instance=ElementAccess_strategy)
@settings(max_examples=50)
def test_elementaccess_instantiation(instance):
    assert isinstance(instance, ElementAccess)

@given(instance=dbl::TypeAccess_strategy)
@settings(max_examples=50)
def test_dbl::typeaccess_instantiation(instance):
    assert isinstance(instance, dbl::TypeAccess)

@given(instance=dbl::VariableAccess_strategy)
@settings(max_examples=50)
def test_dbl::variableaccess_instantiation(instance):
    assert isinstance(instance, dbl::VariableAccess)

@given(instance=RhsExpression_strategy)
@settings(max_examples=50)
def test_rhsexpression_instantiation(instance):
    assert isinstance(instance, RhsExpression)

@given(instance=dbl::L1RhsExpr_strategy)
@settings(max_examples=50)
def test_dbl::l1rhsexpr_instantiation(instance):
    assert isinstance(instance, dbl::L1RhsExpr)

@given(instance=dbl::L2RhsExpr_strategy)
@settings(max_examples=50)
def test_dbl::l2rhsexpr_instantiation(instance):
    assert isinstance(instance, dbl::L2RhsExpr)

@given(instance=dbl::L3RhsExpr_strategy)
@settings(max_examples=50)
def test_dbl::l3rhsexpr_instantiation(instance):
    assert isinstance(instance, dbl::L3RhsExpr)

@given(instance=dbl::RhsExpression_strategy)
@settings(max_examples=50)
def test_dbl::rhsexpression_instantiation(instance):
    assert isinstance(instance, dbl::RhsExpression)

@given(instance=LanguageConstructClassifier_strategy)
@settings(max_examples=50)
def test_languageconstructclassifier_instantiation(instance):
    assert isinstance(instance, LanguageConstructClassifier)

@given(instance=dbl::LanguageConceptClassifier_strategy)
@settings(max_examples=50)
def test_dbl::languageconceptclassifier_instantiation(instance):
    assert isinstance(instance, dbl::LanguageConceptClassifier)

@given(instance=dbl::TsRule_strategy)
@settings(max_examples=50)
def test_dbl::tsrule_instantiation(instance):
    assert isinstance(instance, dbl::TsRule)

@given(instance=dbl::Mapping_strategy)
@settings(max_examples=50)
def test_dbl::mapping_instantiation(instance):
    assert isinstance(instance, dbl::Mapping)

@given(instance=dbl::CallPart_strategy)
@settings(max_examples=50)
def test_dbl::callpart_instantiation(instance):
    assert isinstance(instance, dbl::CallPart)

@given(instance=PredefinedId_strategy)
@settings(max_examples=50)
def test_predefinedid_instantiation(instance):
    assert isinstance(instance, PredefinedId)

@given(instance=dbl::MetaLiteral_strategy)
@settings(max_examples=50)
def test_dbl::metaliteral_instantiation(instance):
    assert isinstance(instance, dbl::MetaLiteral)

@given(instance=dbl::SizeOfArray_strategy)
@settings(max_examples=50)
def test_dbl::sizeofarray_instantiation(instance):
    assert isinstance(instance, dbl::SizeOfArray)

@given(instance=dbl::TypeLiteral_strategy)
@settings(max_examples=50)
def test_dbl::typeliteral_instantiation(instance):
    assert isinstance(instance, dbl::TypeLiteral)

@given(instance=dbl::SuperLiteral_strategy)
@settings(max_examples=50)
def test_dbl::superliteral_instantiation(instance):
    assert isinstance(instance, dbl::SuperLiteral)

@given(instance=dbl::MeLiteral_strategy)
@settings(max_examples=50)
def test_dbl::meliteral_instantiation(instance):
    assert isinstance(instance, dbl::MeLiteral)

@given(instance=dbl::PredefinedId_strategy)
@settings(max_examples=50)
def test_dbl::predefinedid_instantiation(instance):
    assert isinstance(instance, dbl::PredefinedId)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dbl::L3Expr_strategy)
@settings(max_examples=50)
def test_dbl::l3expr_instantiation(instance):
    assert isinstance(instance, dbl::L3Expr)

@given(instance=dbl::L4Expr_strategy)
@settings(max_examples=50)
def test_dbl::l4expr_instantiation(instance):
    assert isinstance(instance, dbl::L4Expr)

@given(instance=dbl::ExpandExpr_strategy)
@settings(max_examples=50)
def test_dbl::expandexpr_instantiation(instance):
    assert isinstance(instance, dbl::ExpandExpr)

@given(instance=dbl::MetaExpr_strategy)
@settings(max_examples=50)
def test_dbl::metaexpr_instantiation(instance):
    assert isinstance(instance, dbl::MetaExpr)

@given(instance=dbl::ParseExpr_strategy)
@settings(max_examples=50)
def test_dbl::parseexpr_instantiation(instance):
    assert isinstance(instance, dbl::ParseExpr)

@given(instance=dbl::ElementAccess_strategy)
@settings(max_examples=50)
def test_dbl::elementaccess_instantiation(instance):
    assert isinstance(instance, dbl::ElementAccess)

@given(instance=dbl::L8Expr_strategy)
@settings(max_examples=50)
def test_dbl::l8expr_instantiation(instance):
    assert isinstance(instance, dbl::L8Expr)

@given(instance=dbl::BinaryOperator_strategy)
@settings(max_examples=50)
def test_dbl::binaryoperator_instantiation(instance):
    assert isinstance(instance, dbl::BinaryOperator)

@given(instance=dbl::L9Expr_strategy)
@settings(max_examples=50)
def test_dbl::l9expr_instantiation(instance):
    assert isinstance(instance, dbl::L9Expr)

@given(instance=dbl::L7Expr_strategy)
@settings(max_examples=50)
def test_dbl::l7expr_instantiation(instance):
    assert isinstance(instance, dbl::L7Expr)

@given(instance=dbl::ExpandExpression_strategy)
@settings(max_examples=50)
def test_dbl::expandexpression_instantiation(instance):
    assert isinstance(instance, dbl::ExpandExpression)

@given(instance=dbl::L5Expr_strategy)
@settings(max_examples=50)
def test_dbl::l5expr_instantiation(instance):
    assert isinstance(instance, dbl::L5Expr)

@given(instance=dbl::L6Expr_strategy)
@settings(max_examples=50)
def test_dbl::l6expr_instantiation(instance):
    assert isinstance(instance, dbl::L6Expr)

@given(instance=dbl::L2Expr_strategy)
@settings(max_examples=50)
def test_dbl::l2expr_instantiation(instance):
    assert isinstance(instance, dbl::L2Expr)

@given(instance=dbl::CodeQuoteExpression_strategy)
@settings(max_examples=50)
def test_dbl::codequoteexpression_instantiation(instance):
    assert isinstance(instance, dbl::CodeQuoteExpression)

@given(instance=dbl::UnaryOperator_strategy)
@settings(max_examples=50)
def test_dbl::unaryoperator_instantiation(instance):
    assert isinstance(instance, dbl::UnaryOperator)

@given(instance=dbl::L1Expr_strategy)
@settings(max_examples=50)
def test_dbl::l1expr_instantiation(instance):
    assert isinstance(instance, dbl::L1Expr)

@given(instance=L1Expr_strategy)
@settings(max_examples=50)
def test_l1expr_instantiation(instance):
    assert isinstance(instance, L1Expr)

@given(instance=dbl::IdExpr_strategy)
@settings(max_examples=50)
def test_dbl::idexpr_instantiation(instance):
    assert isinstance(instance, dbl::IdExpr)

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

@given(instance=dbl::ActiveLiteral_strategy)
@settings(max_examples=50)
def test_dbl::activeliteral_instantiation(instance):
    assert isinstance(instance, dbl::ActiveLiteral)

@given(instance=dbl::TimeLiteral_strategy)
@settings(max_examples=50)
def test_dbl::timeliteral_instantiation(instance):
    assert isinstance(instance, dbl::TimeLiteral)

@given(instance=dbl::NullLiteral_strategy)
@settings(max_examples=50)
def test_dbl::nullliteral_instantiation(instance):
    assert isinstance(instance, dbl::NullLiteral)

@given(instance=dbl::FalseLiteral_strategy)
@settings(max_examples=50)
def test_dbl::falseliteral_instantiation(instance):
    assert isinstance(instance, dbl::FalseLiteral)

@given(instance=dbl::CreateObject_strategy)
@settings(max_examples=50)
def test_dbl::createobject_instantiation(instance):
    assert isinstance(instance, dbl::CreateObject)

@given(instance=L2Expr_strategy)
@settings(max_examples=50)
def test_l2expr_instantiation(instance):
    assert isinstance(instance, L2Expr)

@given(instance=UnaryOperator_strategy)
@settings(max_examples=50)
def test_unaryoperator_instantiation(instance):
    assert isinstance(instance, UnaryOperator)

@given(instance=dbl::Cast_strategy)
@settings(max_examples=50)
def test_dbl::cast_instantiation(instance):
    assert isinstance(instance, dbl::Cast)

@given(instance=dbl::Not_strategy)
@settings(max_examples=50)
def test_dbl::not_instantiation(instance):
    assert isinstance(instance, dbl::Not)

@given(instance=dbl::Neg_strategy)
@settings(max_examples=50)
def test_dbl::neg_instantiation(instance):
    assert isinstance(instance, dbl::Neg)

@given(instance=L3Expr_strategy)
@settings(max_examples=50)
def test_l3expr_instantiation(instance):
    assert isinstance(instance, L3Expr)

@given(instance=L4Expr_strategy)
@settings(max_examples=50)
def test_l4expr_instantiation(instance):
    assert isinstance(instance, L4Expr)

@given(instance=L5Expr_strategy)
@settings(max_examples=50)
def test_l5expr_instantiation(instance):
    assert isinstance(instance, L5Expr)

@given(instance=L6Expr_strategy)
@settings(max_examples=50)
def test_l6expr_instantiation(instance):
    assert isinstance(instance, L6Expr)

@given(instance=L7Expr_strategy)
@settings(max_examples=50)
def test_l7expr_instantiation(instance):
    assert isinstance(instance, L7Expr)

@given(instance=L8Expr_strategy)
@settings(max_examples=50)
def test_l8expr_instantiation(instance):
    assert isinstance(instance, L8Expr)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=dbl::Greater_strategy)
@settings(max_examples=50)
def test_dbl::greater_instantiation(instance):
    assert isinstance(instance, dbl::Greater)

@given(instance=dbl::Plus_strategy)
@settings(max_examples=50)
def test_dbl::plus_instantiation(instance):
    assert isinstance(instance, dbl::Plus)

@given(instance=dbl::And_strategy)
@settings(max_examples=50)
def test_dbl::and_instantiation(instance):
    assert isinstance(instance, dbl::And)

@given(instance=dbl::Mul_strategy)
@settings(max_examples=50)
def test_dbl::mul_instantiation(instance):
    assert isinstance(instance, dbl::Mul)

@given(instance=dbl::Less_strategy)
@settings(max_examples=50)
def test_dbl::less_instantiation(instance):
    assert isinstance(instance, dbl::Less)

@given(instance=dbl::Mod_strategy)
@settings(max_examples=50)
def test_dbl::mod_instantiation(instance):
    assert isinstance(instance, dbl::Mod)

@given(instance=dbl::Div_strategy)
@settings(max_examples=50)
def test_dbl::div_instantiation(instance):
    assert isinstance(instance, dbl::Div)

@given(instance=dbl::InstanceOf_strategy)
@settings(max_examples=50)
def test_dbl::instanceof_instantiation(instance):
    assert isinstance(instance, dbl::InstanceOf)

@given(instance=dbl::NotEqual_strategy)
@settings(max_examples=50)
def test_dbl::notequal_instantiation(instance):
    assert isinstance(instance, dbl::NotEqual)

@given(instance=dbl::Equal_strategy)
@settings(max_examples=50)
def test_dbl::equal_instantiation(instance):
    assert isinstance(instance, dbl::Equal)

@given(instance=dbl::LessEqual_strategy)
@settings(max_examples=50)
def test_dbl::lessequal_instantiation(instance):
    assert isinstance(instance, dbl::LessEqual)

@given(instance=dbl::Minus_strategy)
@settings(max_examples=50)
def test_dbl::minus_instantiation(instance):
    assert isinstance(instance, dbl::Minus)

@given(instance=dbl::GreaterEqual_strategy)
@settings(max_examples=50)
def test_dbl::greaterequal_instantiation(instance):
    assert isinstance(instance, dbl::GreaterEqual)

@given(instance=dbl::Or_strategy)
@settings(max_examples=50)
def test_dbl::or_instantiation(instance):
    assert isinstance(instance, dbl::Or)

@given(instance=dbl::LocalScope_strategy)
@settings(max_examples=50)
def test_dbl::localscope_instantiation(instance):
    assert isinstance(instance, dbl::LocalScope)

@given(instance=dbl::IfStatement_strategy)
@settings(max_examples=50)
def test_dbl::ifstatement_instantiation(instance):
    assert isinstance(instance, dbl::IfStatement)

@given(instance=dbl::SwitchCase_strategy)
@settings(max_examples=50)
def test_dbl::switchcase_instantiation(instance):
    assert isinstance(instance, dbl::SwitchCase)

@given(instance=LoopStatement_strategy)
@settings(max_examples=50)
def test_loopstatement_instantiation(instance):
    assert isinstance(instance, LoopStatement)

@given(instance=dbl::WhileStatement_strategy)
@settings(max_examples=50)
def test_dbl::whilestatement_instantiation(instance):
    assert isinstance(instance, dbl::WhileStatement)

@given(instance=dbl::ForStatement_strategy)
@settings(max_examples=50)
def test_dbl::forstatement_instantiation(instance):
    assert isinstance(instance, dbl::ForStatement)

@given(instance=ExtensibleElement_strategy)
@settings(max_examples=50)
def test_extensibleelement_instantiation(instance):
    assert isinstance(instance, ExtensibleElement)

@given(instance=dbl::TextualSyntaxDef_strategy)
@settings(max_examples=50)
def test_dbl::textualsyntaxdef_instantiation(instance):
    assert isinstance(instance, dbl::TextualSyntaxDef)

@given(instance=dbl::ClassContentExtension_strategy)
@settings(max_examples=50)
def test_dbl::classcontentextension_instantiation(instance):
    assert isinstance(instance, dbl::ClassContentExtension)

@given(instance=dbl::Expression_strategy)
@settings(max_examples=50)
def test_dbl::expression_instantiation(instance):
    assert isinstance(instance, dbl::Expression)

@given(instance=dbl::ModuleContentExtension_strategy)
@settings(max_examples=50)
def test_dbl::modulecontentextension_instantiation(instance):
    assert isinstance(instance, dbl::ModuleContentExtension)

@given(instance=dbl::ExtensionDefinition_strategy)
@settings(max_examples=50)
def test_dbl::extensiondefinition_instantiation(instance):
    assert isinstance(instance, dbl::ExtensionDefinition)

@given(instance=dbl::LanguageConstructClassifier_strategy)
@settings(max_examples=50)
def test_dbl::languageconstructclassifier_instantiation(instance):
    assert isinstance(instance, dbl::LanguageConstructClassifier)

@given(instance=dbl::Statement_strategy)
@settings(max_examples=50)
def test_dbl::statement_instantiation(instance):
    assert isinstance(instance, dbl::Statement)

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

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

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

@given(instance=dbl::ProcedureCall_strategy)
@settings(max_examples=50)
def test_dbl::procedurecall_instantiation(instance):
    assert isinstance(instance, dbl::ProcedureCall)

@given(instance=dbl::Advance_strategy)
@settings(max_examples=50)
def test_dbl::advance_instantiation(instance):
    assert isinstance(instance, dbl::Advance)

@given(instance=dbl::SwitchStatement_strategy)
@settings(max_examples=50)
def test_dbl::switchstatement_instantiation(instance):
    assert isinstance(instance, dbl::SwitchStatement)

@given(instance=dbl::LocalScopeStatement_strategy)
@settings(max_examples=50)
def test_dbl::localscopestatement_instantiation(instance):
    assert isinstance(instance, dbl::LocalScopeStatement)

@given(instance=dbl::WaitUntil_strategy)
@settings(max_examples=50)
def test_dbl::waituntil_instantiation(instance):
    assert isinstance(instance, dbl::WaitUntil)

@given(instance=dbl::SaveGenStatement_strategy)
@settings(max_examples=50)
def test_dbl::savegenstatement_instantiation(instance):
    assert isinstance(instance, dbl::SaveGenStatement)

@given(instance=dbl::Reactivate_strategy)
@settings(max_examples=50)
def test_dbl::reactivate_instantiation(instance):
    assert isinstance(instance, dbl::Reactivate)

@given(instance=dbl::Wait_strategy)
@settings(max_examples=50)
def test_dbl::wait_instantiation(instance):
    assert isinstance(instance, dbl::Wait)

@given(instance=dbl::Assignment_strategy)
@settings(max_examples=50)
def test_dbl::assignment_instantiation(instance):
    assert isinstance(instance, dbl::Assignment)

@given(instance=dbl::ContinueStatement_strategy)
@settings(max_examples=50)
def test_dbl::continuestatement_instantiation(instance):
    assert isinstance(instance, dbl::ContinueStatement)

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

@given(instance=dbl::Return_strategy)
@settings(max_examples=50)
def test_dbl::return_instantiation(instance):
    assert isinstance(instance, dbl::Return)

@given(instance=dbl::Yield_strategy)
@settings(max_examples=50)
def test_dbl::yield_instantiation(instance):
    assert isinstance(instance, dbl::Yield)

@given(instance=dbl::BreakStatement_strategy)
@settings(max_examples=50)
def test_dbl::breakstatement_instantiation(instance):
    assert isinstance(instance, dbl::BreakStatement)

@given(instance=dbl::ResumeGenStatement_strategy)
@settings(max_examples=50)
def test_dbl::resumegenstatement_instantiation(instance):
    assert isinstance(instance, dbl::ResumeGenStatement)

@given(instance=dbl::Terminate_strategy)
@settings(max_examples=50)
def test_dbl::terminate_instantiation(instance):
    assert isinstance(instance, dbl::Terminate)

@given(instance=dbl::Print_strategy)
@settings(max_examples=50)
def test_dbl::print_instantiation(instance):
    assert isinstance(instance, dbl::Print)

@given(instance=dbl::ResetGenContextStatement_strategy)
@settings(max_examples=50)
def test_dbl::resetgencontextstatement_instantiation(instance):
    assert isinstance(instance, dbl::ResetGenContextStatement)

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=dbl::Parameter_strategy)
@settings(max_examples=50)
def test_dbl::parameter_instantiation(instance):
    assert isinstance(instance, dbl::Parameter)

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

@given(instance=dbl::AbstractVariable_strategy)
@settings(max_examples=50)
def test_dbl::abstractvariable_instantiation(instance):
    assert isinstance(instance, dbl::AbstractVariable)
