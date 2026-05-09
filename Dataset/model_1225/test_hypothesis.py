import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ClassifierPropertyCS,
    ScopedNameCS,
    OCLExpressionCS,
    StringLiteralExpCS,
    SimpleNameCS,
    TypeCS,
    PathNameCS,
    MappingModuleCS,
    qvtoperational::cst::LibraryCS,
    TagCS,
    ClassifierDefCS,
    MappingMethodCS,
    ModulePropertyCS,
    qvtoperational::cst::LocalPropertyCS,
    qvtoperational::cst::ContextualPropertyCS,
    qvtoperational::cst::ConfigPropertyCS,
    ModelTypeCS,
    ImportCS,
    qvtoperational::cst::LibraryImportCS,
    TransformationHeaderCS,
    CSTNode,
    qvtoperational::cst::ImportCS,
    qvtoperational::cst::ModulePropertyCS,
    qvtoperational::cst::ClassifierDefCS,
    qvtoperational::cst::RenameCS,
    qvtoperational::cst::MappingModuleCS,
    qvtoperational::cst::ScopedNameCS,
    qvtoperational::cst::ResolveOpArgsExpCS,
    qvtoperational::cst::ListTypeCS,
    qvtoperational::cst::UnitCS,
    qvtoperational::cst::TagCS,
    qvtoperational::cst::DictLiteralPartCS,
    DictLiteralPartCS,
    qvtoperational::cst::DictionaryTypeCS,
    CollectionLiteralPartCS,
    LiteralExpCS,
    qvtoperational::cst::ListLiteralExpCS,
    qvtoperational::cst::DictLiteralExpCS,
    qvtoperational::cst::TransformationRefineCS,
    ModuleRefCS,
    ModuleKindCS,
    qvtoperational::cst::MappingExtensionCS,
    LogExpCS,
    qvtoperational::cst::TypeSpecCS,
    qvtoperational::cst::ModuleUsageCS,
    qvtoperational::cst::ModuleRefCS,
    qvtoperational::cst::ModuleKindCS,
    TransformationRefineCS,
    ModuleUsageCS,
    qvtoperational::cst::TransformationHeaderCS,
    qvtoperational::cst::PackageRefCS,
    PackageRefCS,
    ResolveExpCS,
    qvtoperational::cst::ResolveInExpCS,
    CallExpCS,
    qvtoperational::cst::ResolveExpCS,
    qvtoperational::cst::ElementWithBody,
    qvtoperational::cst::DirectionKindCS,
    OperationCallExpCS,
    qvtoperational::cst::LogExpCS,
    qvtoperational::cst::ImperativeOperationCallExpCS,
    ImperativeOperationCallExpCS,
    qvtoperational::cst::MappingCallExpCS,
    cst::InstantiationExpCS,
    SwitchAltExpCS,
    ImperativeLoopExpCS,
    qvtoperational::cst::ImperativeIterateExpCS,
    qvtoperational::cst::ForExpCS,
    cst::StatementCS,
    cst::LoopExpCS,
    qvtoperational::cst::ImperativeLoopExpCS,
    qvtoperational::cst::SimpleSignatureCS,
    VariableCS,
    StatementCS,
    qvtoperational::cst::InstantiationExpCS,
    qvtoperational::cst::VariableInitializationCS,
    qvtoperational::cst::ComputeExpCS,
    qvtoperational::cst::ReturnExpCS,
    qvtoperational::cst::SwitchExpCS,
    qvtoperational::cst::AssignStatementCS,
    qvtoperational::cst::ExpressionStatementCS,
    qvtoperational::cst::BreakExpCS,
    qvtoperational::cst::ContinueExpCS,
    qvtoperational::cst::SwitchAltExpCS,
    qvtoperational::cst::AssertExpCS,
    qvtoperational::cst::WhileExpCS,
    qvtoperational::cst::BlockExpCS,
    qvtoperational::cst::StatementCS,
    MappingEndCS,
    MappingBodyCS,
    MappingInitCS,
    qvtoperational::cst::MappingSectionsCS,
    MappingSectionCS,
    qvtoperational::cst::MappingEndCS,
    qvtoperational::cst::MappingBodyCS,
    qvtoperational::cst::MappingInitCS,
    MappingRuleCS,
    cst::ElementWithBody,
    qvtoperational::cst::ObjectExpCS,
    cst::CSTNode,
    qvtoperational::cst::ModelTypeCS,
    qvtoperational::cst::MappingSectionCS,
    qvtoperational::cst::ConstructorCS,
    qvtoperational::cst::MappingQueryCS,
    MappingSectionsCS,
    qvtoperational::cst::MappingRuleCS,
    MappingDeclarationCS,
    qvtoperational::cst::MappingMethodCS,
    SimpleSignatureCS,
    qvtoperational::cst::CompleteSignatureCS,
    TypeSpecCS,
    qvtoperational::cst::ParameterDeclarationCS,
    MappingExtensionCS,
    DirectionKindCS,
    ParameterDeclarationCS,
    qvtoperational::cst::MappingDeclarationCS,
    PrimitiveLiteralExpCS,
    qvtoperational::cst::MultiplicityDefCS,
    qvtoperational::cst::OppositePropertyCS,
    OppositePropertyCS,
    MultiplicityDefCS,
    LocalPropertyCS,
    qvtoperational::cst::ClassifierPropertyCS,
    RenameCS,
    ImportKindEnum,
    MappingExtensionKindCS,
    ModuleKindEnum,
    DirectionKindEnum,
    QualifierKindCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classifierpropertycs_is_not_abstract():
    assert not inspect.isabstract(ClassifierPropertyCS)


def test_classifierpropertycs_constructor_exists():
    assert callable(ClassifierPropertyCS.__init__)


def test_classifierpropertycs_constructor_args():
    sig = inspect.signature(ClassifierPropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_scopednamecs_is_not_abstract():
    assert not inspect.isabstract(ScopedNameCS)


def test_scopednamecs_constructor_exists():
    assert callable(ScopedNameCS.__init__)


def test_scopednamecs_constructor_args():
    sig = inspect.signature(ScopedNameCS.__init__)
    params = list(sig.parameters.keys())



def test_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(OCLExpressionCS)


def test_oclexpressioncs_constructor_exists():
    assert callable(OCLExpressionCS.__init__)


def test_oclexpressioncs_constructor_args():
    sig = inspect.signature(OCLExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(StringLiteralExpCS)


def test_stringliteralexpcs_constructor_exists():
    assert callable(StringLiteralExpCS.__init__)


def test_stringliteralexpcs_constructor_args():
    sig = inspect.signature(StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_simplenamecs_is_not_abstract():
    assert not inspect.isabstract(SimpleNameCS)


def test_simplenamecs_constructor_exists():
    assert callable(SimpleNameCS.__init__)


def test_simplenamecs_constructor_args():
    sig = inspect.signature(SimpleNameCS.__init__)
    params = list(sig.parameters.keys())



def test_typecs_is_not_abstract():
    assert not inspect.isabstract(TypeCS)


def test_typecs_constructor_exists():
    assert callable(TypeCS.__init__)


def test_typecs_constructor_args():
    sig = inspect.signature(TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(PathNameCS)


def test_pathnamecs_constructor_exists():
    assert callable(PathNameCS.__init__)


def test_pathnamecs_constructor_args():
    sig = inspect.signature(PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingmodulecs_is_not_abstract():
    assert not inspect.isabstract(MappingModuleCS)


def test_mappingmodulecs_constructor_exists():
    assert callable(MappingModuleCS.__init__)


def test_mappingmodulecs_constructor_args():
    sig = inspect.signature(MappingModuleCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::librarycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::LibraryCS)


def test_qvtoperational::cst::librarycs_constructor_exists():
    assert callable(qvtoperational::cst::LibraryCS.__init__)


def test_qvtoperational::cst::librarycs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::LibraryCS.__init__)
    params = list(sig.parameters.keys())



def test_tagcs_is_not_abstract():
    assert not inspect.isabstract(TagCS)


def test_tagcs_constructor_exists():
    assert callable(TagCS.__init__)


def test_tagcs_constructor_args():
    sig = inspect.signature(TagCS.__init__)
    params = list(sig.parameters.keys())



def test_classifierdefcs_is_not_abstract():
    assert not inspect.isabstract(ClassifierDefCS)


def test_classifierdefcs_constructor_exists():
    assert callable(ClassifierDefCS.__init__)


def test_classifierdefcs_constructor_args():
    sig = inspect.signature(ClassifierDefCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingmethodcs_is_not_abstract():
    assert not inspect.isabstract(MappingMethodCS)


def test_mappingmethodcs_constructor_exists():
    assert callable(MappingMethodCS.__init__)


def test_mappingmethodcs_constructor_args():
    sig = inspect.signature(MappingMethodCS.__init__)
    params = list(sig.parameters.keys())



def test_modulepropertycs_is_not_abstract():
    assert not inspect.isabstract(ModulePropertyCS)


def test_modulepropertycs_constructor_exists():
    assert callable(ModulePropertyCS.__init__)


def test_modulepropertycs_constructor_args():
    sig = inspect.signature(ModulePropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::localpropertycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::LocalPropertyCS)


def test_qvtoperational::cst::localpropertycs_constructor_exists():
    assert callable(qvtoperational::cst::LocalPropertyCS.__init__)


def test_qvtoperational::cst::localpropertycs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::LocalPropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::contextualpropertycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ContextualPropertyCS)


def test_qvtoperational::cst::contextualpropertycs_constructor_exists():
    assert callable(qvtoperational::cst::ContextualPropertyCS.__init__)


def test_qvtoperational::cst::contextualpropertycs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ContextualPropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::configpropertycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ConfigPropertyCS)


def test_qvtoperational::cst::configpropertycs_constructor_exists():
    assert callable(qvtoperational::cst::ConfigPropertyCS.__init__)


def test_qvtoperational::cst::configpropertycs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ConfigPropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_modeltypecs_is_not_abstract():
    assert not inspect.isabstract(ModelTypeCS)


def test_modeltypecs_constructor_exists():
    assert callable(ModelTypeCS.__init__)


def test_modeltypecs_constructor_args():
    sig = inspect.signature(ModelTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_importcs_is_not_abstract():
    assert not inspect.isabstract(ImportCS)


def test_importcs_constructor_exists():
    assert callable(ImportCS.__init__)


def test_importcs_constructor_args():
    sig = inspect.signature(ImportCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::libraryimportcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::LibraryImportCS)


def test_qvtoperational::cst::libraryimportcs_constructor_exists():
    assert callable(qvtoperational::cst::LibraryImportCS.__init__)


def test_qvtoperational::cst::libraryimportcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::LibraryImportCS.__init__)
    params = list(sig.parameters.keys())



def test_transformationheadercs_is_not_abstract():
    assert not inspect.isabstract(TransformationHeaderCS)


def test_transformationheadercs_constructor_exists():
    assert callable(TransformationHeaderCS.__init__)


def test_transformationheadercs_constructor_args():
    sig = inspect.signature(TransformationHeaderCS.__init__)
    params = list(sig.parameters.keys())



def test_cstnode_is_not_abstract():
    assert not inspect.isabstract(CSTNode)


def test_cstnode_constructor_exists():
    assert callable(CSTNode.__init__)


def test_cstnode_constructor_args():
    sig = inspect.signature(CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::importcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ImportCS)


def test_qvtoperational::cst::importcs_constructor_exists():
    assert callable(qvtoperational::cst::ImportCS.__init__)


def test_qvtoperational::cst::importcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ImportCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::modulepropertycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ModulePropertyCS)


def test_qvtoperational::cst::modulepropertycs_constructor_exists():
    assert callable(qvtoperational::cst::ModulePropertyCS.__init__)


def test_qvtoperational::cst::modulepropertycs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ModulePropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::classifierdefcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ClassifierDefCS)


def test_qvtoperational::cst::classifierdefcs_constructor_exists():
    assert callable(qvtoperational::cst::ClassifierDefCS.__init__)


def test_qvtoperational::cst::classifierdefcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ClassifierDefCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::renamecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::RenameCS)


def test_qvtoperational::cst::renamecs_constructor_exists():
    assert callable(qvtoperational::cst::RenameCS.__init__)


def test_qvtoperational::cst::renamecs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::RenameCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::mappingmodulecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MappingModuleCS)


def test_qvtoperational::cst::mappingmodulecs_constructor_exists():
    assert callable(qvtoperational::cst::MappingModuleCS.__init__)


def test_qvtoperational::cst::mappingmodulecs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MappingModuleCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::scopednamecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ScopedNameCS)


def test_qvtoperational::cst::scopednamecs_constructor_exists():
    assert callable(qvtoperational::cst::ScopedNameCS.__init__)


def test_qvtoperational::cst::scopednamecs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ScopedNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_qvtoperational::cst::scopednamecs_has_name():
    assert hasattr(qvtoperational::cst::ScopedNameCS, "name")
    descriptor = None
    for klass in qvtoperational::cst::ScopedNameCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational::cst::resolveopargsexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ResolveOpArgsExpCS)


def test_qvtoperational::cst::resolveopargsexpcs_constructor_exists():
    assert callable(qvtoperational::cst::ResolveOpArgsExpCS.__init__)


def test_qvtoperational::cst::resolveopargsexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ResolveOpArgsExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::listtypecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ListTypeCS)


def test_qvtoperational::cst::listtypecs_constructor_exists():
    assert callable(qvtoperational::cst::ListTypeCS.__init__)


def test_qvtoperational::cst::listtypecs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ListTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::unitcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::UnitCS)


def test_qvtoperational::cst::unitcs_constructor_exists():
    assert callable(qvtoperational::cst::UnitCS.__init__)


def test_qvtoperational::cst::unitcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::UnitCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::tagcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::TagCS)


def test_qvtoperational::cst::tagcs_constructor_exists():
    assert callable(qvtoperational::cst::TagCS.__init__)


def test_qvtoperational::cst::tagcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::TagCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::dictliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::DictLiteralPartCS)


def test_qvtoperational::cst::dictliteralpartcs_constructor_exists():
    assert callable(qvtoperational::cst::DictLiteralPartCS.__init__)


def test_qvtoperational::cst::dictliteralpartcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::DictLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPartCS)


def test_dictliteralpartcs_constructor_exists():
    assert callable(DictLiteralPartCS.__init__)


def test_dictliteralpartcs_constructor_args():
    sig = inspect.signature(DictLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::dictionarytypecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::DictionaryTypeCS)


def test_qvtoperational::cst::dictionarytypecs_constructor_exists():
    assert callable(qvtoperational::cst::DictionaryTypeCS.__init__)


def test_qvtoperational::cst::dictionarytypecs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::DictionaryTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPartCS)


def test_collectionliteralpartcs_constructor_exists():
    assert callable(CollectionLiteralPartCS.__init__)


def test_collectionliteralpartcs_constructor_args():
    sig = inspect.signature(CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::listliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ListLiteralExpCS)


def test_qvtoperational::cst::listliteralexpcs_constructor_exists():
    assert callable(qvtoperational::cst::ListLiteralExpCS.__init__)


def test_qvtoperational::cst::listliteralexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ListLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::dictliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::DictLiteralExpCS)


def test_qvtoperational::cst::dictliteralexpcs_constructor_exists():
    assert callable(qvtoperational::cst::DictLiteralExpCS.__init__)


def test_qvtoperational::cst::dictliteralexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::DictLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::transformationrefinecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::TransformationRefineCS)


def test_qvtoperational::cst::transformationrefinecs_constructor_exists():
    assert callable(qvtoperational::cst::TransformationRefineCS.__init__)


def test_qvtoperational::cst::transformationrefinecs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::TransformationRefineCS.__init__)
    params = list(sig.parameters.keys())



def test_modulerefcs_is_not_abstract():
    assert not inspect.isabstract(ModuleRefCS)


def test_modulerefcs_constructor_exists():
    assert callable(ModuleRefCS.__init__)


def test_modulerefcs_constructor_args():
    sig = inspect.signature(ModuleRefCS.__init__)
    params = list(sig.parameters.keys())



def test_modulekindcs_is_not_abstract():
    assert not inspect.isabstract(ModuleKindCS)


def test_modulekindcs_constructor_exists():
    assert callable(ModuleKindCS.__init__)


def test_modulekindcs_constructor_args():
    sig = inspect.signature(ModuleKindCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::mappingextensioncs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MappingExtensionCS)


def test_qvtoperational::cst::mappingextensioncs_constructor_exists():
    assert callable(qvtoperational::cst::MappingExtensionCS.__init__)


def test_qvtoperational::cst::mappingextensioncs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MappingExtensionCS.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_qvtoperational::cst::mappingextensioncs_has_kind():
    assert hasattr(qvtoperational::cst::MappingExtensionCS, "kind")
    descriptor = None
    for klass in qvtoperational::cst::MappingExtensionCS.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_logexpcs_is_not_abstract():
    assert not inspect.isabstract(LogExpCS)


def test_logexpcs_constructor_exists():
    assert callable(LogExpCS.__init__)


def test_logexpcs_constructor_args():
    sig = inspect.signature(LogExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::typespeccs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::TypeSpecCS)


def test_qvtoperational::cst::typespeccs_constructor_exists():
    assert callable(qvtoperational::cst::TypeSpecCS.__init__)


def test_qvtoperational::cst::typespeccs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::TypeSpecCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::moduleusagecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ModuleUsageCS)


def test_qvtoperational::cst::moduleusagecs_constructor_exists():
    assert callable(qvtoperational::cst::ModuleUsageCS.__init__)


def test_qvtoperational::cst::moduleusagecs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ModuleUsageCS.__init__)
    params = list(sig.parameters.keys())
    assert "importKind" in params, "Missing parameter 'importKind'"

def test_qvtoperational::cst::moduleusagecs_has_importKind():
    assert hasattr(qvtoperational::cst::ModuleUsageCS, "importKind")
    descriptor = None
    for klass in qvtoperational::cst::ModuleUsageCS.__mro__:
        if "importKind" in klass.__dict__:
            descriptor = klass.__dict__["importKind"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational::cst::modulerefcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ModuleRefCS)


def test_qvtoperational::cst::modulerefcs_constructor_exists():
    assert callable(qvtoperational::cst::ModuleRefCS.__init__)


def test_qvtoperational::cst::modulerefcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ModuleRefCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::modulekindcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ModuleKindCS)


def test_qvtoperational::cst::modulekindcs_constructor_exists():
    assert callable(qvtoperational::cst::ModuleKindCS.__init__)


def test_qvtoperational::cst::modulekindcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ModuleKindCS.__init__)
    params = list(sig.parameters.keys())
    assert "moduleKind" in params, "Missing parameter 'moduleKind'"

def test_qvtoperational::cst::modulekindcs_has_moduleKind():
    assert hasattr(qvtoperational::cst::ModuleKindCS, "moduleKind")
    descriptor = None
    for klass in qvtoperational::cst::ModuleKindCS.__mro__:
        if "moduleKind" in klass.__dict__:
            descriptor = klass.__dict__["moduleKind"]
            break
    assert isinstance(descriptor, property)



def test_transformationrefinecs_is_not_abstract():
    assert not inspect.isabstract(TransformationRefineCS)


def test_transformationrefinecs_constructor_exists():
    assert callable(TransformationRefineCS.__init__)


def test_transformationrefinecs_constructor_args():
    sig = inspect.signature(TransformationRefineCS.__init__)
    params = list(sig.parameters.keys())



def test_moduleusagecs_is_not_abstract():
    assert not inspect.isabstract(ModuleUsageCS)


def test_moduleusagecs_constructor_exists():
    assert callable(ModuleUsageCS.__init__)


def test_moduleusagecs_constructor_args():
    sig = inspect.signature(ModuleUsageCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::transformationheadercs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::TransformationHeaderCS)


def test_qvtoperational::cst::transformationheadercs_constructor_exists():
    assert callable(qvtoperational::cst::TransformationHeaderCS.__init__)


def test_qvtoperational::cst::transformationheadercs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::TransformationHeaderCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::packagerefcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::PackageRefCS)


def test_qvtoperational::cst::packagerefcs_constructor_exists():
    assert callable(qvtoperational::cst::PackageRefCS.__init__)


def test_qvtoperational::cst::packagerefcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::PackageRefCS.__init__)
    params = list(sig.parameters.keys())



def test_packagerefcs_is_not_abstract():
    assert not inspect.isabstract(PackageRefCS)


def test_packagerefcs_constructor_exists():
    assert callable(PackageRefCS.__init__)


def test_packagerefcs_constructor_args():
    sig = inspect.signature(PackageRefCS.__init__)
    params = list(sig.parameters.keys())



def test_resolveexpcs_is_not_abstract():
    assert not inspect.isabstract(ResolveExpCS)


def test_resolveexpcs_constructor_exists():
    assert callable(ResolveExpCS.__init__)


def test_resolveexpcs_constructor_args():
    sig = inspect.signature(ResolveExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::resolveinexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ResolveInExpCS)


def test_qvtoperational::cst::resolveinexpcs_constructor_exists():
    assert callable(qvtoperational::cst::ResolveInExpCS.__init__)


def test_qvtoperational::cst::resolveinexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ResolveInExpCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::resolveexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ResolveExpCS)


def test_qvtoperational::cst::resolveexpcs_constructor_exists():
    assert callable(qvtoperational::cst::ResolveExpCS.__init__)


def test_qvtoperational::cst::resolveexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ResolveExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isInverse" in params, "Missing parameter 'isInverse'"
    assert "one" in params, "Missing parameter 'one'"
    assert "isDeferred" in params, "Missing parameter 'isDeferred'"

def test_qvtoperational::cst::resolveexpcs_has_isInverse():
    assert hasattr(qvtoperational::cst::ResolveExpCS, "isInverse")
    descriptor = None
    for klass in qvtoperational::cst::ResolveExpCS.__mro__:
        if "isInverse" in klass.__dict__:
            descriptor = klass.__dict__["isInverse"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational::cst::resolveexpcs_has_one():
    assert hasattr(qvtoperational::cst::ResolveExpCS, "one")
    descriptor = None
    for klass in qvtoperational::cst::ResolveExpCS.__mro__:
        if "one" in klass.__dict__:
            descriptor = klass.__dict__["one"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational::cst::resolveexpcs_has_isDeferred():
    assert hasattr(qvtoperational::cst::ResolveExpCS, "isDeferred")
    descriptor = None
    for klass in qvtoperational::cst::ResolveExpCS.__mro__:
        if "isDeferred" in klass.__dict__:
            descriptor = klass.__dict__["isDeferred"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational::cst::elementwithbody_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ElementWithBody)


def test_qvtoperational::cst::elementwithbody_constructor_exists():
    assert callable(qvtoperational::cst::ElementWithBody.__init__)


def test_qvtoperational::cst::elementwithbody_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ElementWithBody.__init__)
    params = list(sig.parameters.keys())
    assert "bodyStartLocation" in params, "Missing parameter 'bodyStartLocation'"
    assert "bodyEndLocation" in params, "Missing parameter 'bodyEndLocation'"

def test_qvtoperational::cst::elementwithbody_has_bodyStartLocation():
    assert hasattr(qvtoperational::cst::ElementWithBody, "bodyStartLocation")
    descriptor = None
    for klass in qvtoperational::cst::ElementWithBody.__mro__:
        if "bodyStartLocation" in klass.__dict__:
            descriptor = klass.__dict__["bodyStartLocation"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational::cst::elementwithbody_has_bodyEndLocation():
    assert hasattr(qvtoperational::cst::ElementWithBody, "bodyEndLocation")
    descriptor = None
    for klass in qvtoperational::cst::ElementWithBody.__mro__:
        if "bodyEndLocation" in klass.__dict__:
            descriptor = klass.__dict__["bodyEndLocation"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational::cst::directionkindcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::DirectionKindCS)


def test_qvtoperational::cst::directionkindcs_constructor_exists():
    assert callable(qvtoperational::cst::DirectionKindCS.__init__)


def test_qvtoperational::cst::directionkindcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::DirectionKindCS.__init__)
    params = list(sig.parameters.keys())
    assert "directionKind" in params, "Missing parameter 'directionKind'"

def test_qvtoperational::cst::directionkindcs_has_directionKind():
    assert hasattr(qvtoperational::cst::DirectionKindCS, "directionKind")
    descriptor = None
    for klass in qvtoperational::cst::DirectionKindCS.__mro__:
        if "directionKind" in klass.__dict__:
            descriptor = klass.__dict__["directionKind"]
            break
    assert isinstance(descriptor, property)



def test_operationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(OperationCallExpCS)


def test_operationcallexpcs_constructor_exists():
    assert callable(OperationCallExpCS.__init__)


def test_operationcallexpcs_constructor_args():
    sig = inspect.signature(OperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::logexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::LogExpCS)


def test_qvtoperational::cst::logexpcs_constructor_exists():
    assert callable(qvtoperational::cst::LogExpCS.__init__)


def test_qvtoperational::cst::logexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::LogExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::imperativeoperationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ImperativeOperationCallExpCS)


def test_qvtoperational::cst::imperativeoperationcallexpcs_constructor_exists():
    assert callable(qvtoperational::cst::ImperativeOperationCallExpCS.__init__)


def test_qvtoperational::cst::imperativeoperationcallexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ImperativeOperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeoperationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(ImperativeOperationCallExpCS)


def test_imperativeoperationcallexpcs_constructor_exists():
    assert callable(ImperativeOperationCallExpCS.__init__)


def test_imperativeoperationcallexpcs_constructor_args():
    sig = inspect.signature(ImperativeOperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::mappingcallexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MappingCallExpCS)


def test_qvtoperational::cst::mappingcallexpcs_constructor_exists():
    assert callable(qvtoperational::cst::MappingCallExpCS.__init__)


def test_qvtoperational::cst::mappingcallexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MappingCallExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "strict" in params, "Missing parameter 'strict'"

def test_qvtoperational::cst::mappingcallexpcs_has_strict():
    assert hasattr(qvtoperational::cst::MappingCallExpCS, "strict")
    descriptor = None
    for klass in qvtoperational::cst::MappingCallExpCS.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)



def test_cst::instantiationexpcs_is_not_abstract():
    assert not inspect.isabstract(cst::InstantiationExpCS)


def test_cst::instantiationexpcs_constructor_exists():
    assert callable(cst::InstantiationExpCS.__init__)


def test_cst::instantiationexpcs_constructor_args():
    sig = inspect.signature(cst::InstantiationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_switchaltexpcs_is_not_abstract():
    assert not inspect.isabstract(SwitchAltExpCS)


def test_switchaltexpcs_constructor_exists():
    assert callable(SwitchAltExpCS.__init__)


def test_switchaltexpcs_constructor_args():
    sig = inspect.signature(SwitchAltExpCS.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexpcs_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExpCS)


def test_imperativeloopexpcs_constructor_exists():
    assert callable(ImperativeLoopExpCS.__init__)


def test_imperativeloopexpcs_constructor_args():
    sig = inspect.signature(ImperativeLoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::imperativeiterateexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ImperativeIterateExpCS)


def test_qvtoperational::cst::imperativeiterateexpcs_constructor_exists():
    assert callable(qvtoperational::cst::ImperativeIterateExpCS.__init__)


def test_qvtoperational::cst::imperativeiterateexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ImperativeIterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::forexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ForExpCS)


def test_qvtoperational::cst::forexpcs_constructor_exists():
    assert callable(qvtoperational::cst::ForExpCS.__init__)


def test_qvtoperational::cst::forexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ForExpCS.__init__)
    params = list(sig.parameters.keys())



def test_cst::statementcs_is_not_abstract():
    assert not inspect.isabstract(cst::StatementCS)


def test_cst::statementcs_constructor_exists():
    assert callable(cst::StatementCS.__init__)


def test_cst::statementcs_constructor_args():
    sig = inspect.signature(cst::StatementCS.__init__)
    params = list(sig.parameters.keys())



def test_cst::loopexpcs_is_not_abstract():
    assert not inspect.isabstract(cst::LoopExpCS)


def test_cst::loopexpcs_constructor_exists():
    assert callable(cst::LoopExpCS.__init__)


def test_cst::loopexpcs_constructor_args():
    sig = inspect.signature(cst::LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::imperativeloopexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ImperativeLoopExpCS)


def test_qvtoperational::cst::imperativeloopexpcs_constructor_exists():
    assert callable(qvtoperational::cst::ImperativeLoopExpCS.__init__)


def test_qvtoperational::cst::imperativeloopexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ImperativeLoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::simplesignaturecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::SimpleSignatureCS)


def test_qvtoperational::cst::simplesignaturecs_constructor_exists():
    assert callable(qvtoperational::cst::SimpleSignatureCS.__init__)


def test_qvtoperational::cst::simplesignaturecs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::SimpleSignatureCS.__init__)
    params = list(sig.parameters.keys())



def test_variablecs_is_not_abstract():
    assert not inspect.isabstract(VariableCS)


def test_variablecs_constructor_exists():
    assert callable(VariableCS.__init__)


def test_variablecs_constructor_args():
    sig = inspect.signature(VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_statementcs_is_not_abstract():
    assert not inspect.isabstract(StatementCS)


def test_statementcs_constructor_exists():
    assert callable(StatementCS.__init__)


def test_statementcs_constructor_args():
    sig = inspect.signature(StatementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::instantiationexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::InstantiationExpCS)


def test_qvtoperational::cst::instantiationexpcs_constructor_exists():
    assert callable(qvtoperational::cst::InstantiationExpCS.__init__)


def test_qvtoperational::cst::instantiationexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::InstantiationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::variableinitializationcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::VariableInitializationCS)


def test_qvtoperational::cst::variableinitializationcs_constructor_exists():
    assert callable(qvtoperational::cst::VariableInitializationCS.__init__)


def test_qvtoperational::cst::variableinitializationcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::VariableInitializationCS.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_qvtoperational::cst::variableinitializationcs_has_withResult():
    assert hasattr(qvtoperational::cst::VariableInitializationCS, "withResult")
    descriptor = None
    for klass in qvtoperational::cst::VariableInitializationCS.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational::cst::computeexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ComputeExpCS)


def test_qvtoperational::cst::computeexpcs_constructor_exists():
    assert callable(qvtoperational::cst::ComputeExpCS.__init__)


def test_qvtoperational::cst::computeexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ComputeExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::returnexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ReturnExpCS)


def test_qvtoperational::cst::returnexpcs_constructor_exists():
    assert callable(qvtoperational::cst::ReturnExpCS.__init__)


def test_qvtoperational::cst::returnexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ReturnExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::switchexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::SwitchExpCS)


def test_qvtoperational::cst::switchexpcs_constructor_exists():
    assert callable(qvtoperational::cst::SwitchExpCS.__init__)


def test_qvtoperational::cst::switchexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::SwitchExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::assignstatementcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::AssignStatementCS)


def test_qvtoperational::cst::assignstatementcs_constructor_exists():
    assert callable(qvtoperational::cst::AssignStatementCS.__init__)


def test_qvtoperational::cst::assignstatementcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::AssignStatementCS.__init__)
    params = list(sig.parameters.keys())
    assert "incremental" in params, "Missing parameter 'incremental'"

def test_qvtoperational::cst::assignstatementcs_has_incremental():
    assert hasattr(qvtoperational::cst::AssignStatementCS, "incremental")
    descriptor = None
    for klass in qvtoperational::cst::AssignStatementCS.__mro__:
        if "incremental" in klass.__dict__:
            descriptor = klass.__dict__["incremental"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational::cst::expressionstatementcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ExpressionStatementCS)


def test_qvtoperational::cst::expressionstatementcs_constructor_exists():
    assert callable(qvtoperational::cst::ExpressionStatementCS.__init__)


def test_qvtoperational::cst::expressionstatementcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ExpressionStatementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::breakexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::BreakExpCS)


def test_qvtoperational::cst::breakexpcs_constructor_exists():
    assert callable(qvtoperational::cst::BreakExpCS.__init__)


def test_qvtoperational::cst::breakexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::BreakExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::continueexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ContinueExpCS)


def test_qvtoperational::cst::continueexpcs_constructor_exists():
    assert callable(qvtoperational::cst::ContinueExpCS.__init__)


def test_qvtoperational::cst::continueexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ContinueExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::switchaltexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::SwitchAltExpCS)


def test_qvtoperational::cst::switchaltexpcs_constructor_exists():
    assert callable(qvtoperational::cst::SwitchAltExpCS.__init__)


def test_qvtoperational::cst::switchaltexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::SwitchAltExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::assertexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::AssertExpCS)


def test_qvtoperational::cst::assertexpcs_constructor_exists():
    assert callable(qvtoperational::cst::AssertExpCS.__init__)


def test_qvtoperational::cst::assertexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::AssertExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::whileexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::WhileExpCS)


def test_qvtoperational::cst::whileexpcs_constructor_exists():
    assert callable(qvtoperational::cst::WhileExpCS.__init__)


def test_qvtoperational::cst::whileexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::WhileExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::blockexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::BlockExpCS)


def test_qvtoperational::cst::blockexpcs_constructor_exists():
    assert callable(qvtoperational::cst::BlockExpCS.__init__)


def test_qvtoperational::cst::blockexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::BlockExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::statementcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::StatementCS)


def test_qvtoperational::cst::statementcs_constructor_exists():
    assert callable(qvtoperational::cst::StatementCS.__init__)


def test_qvtoperational::cst::statementcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::StatementCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingendcs_is_not_abstract():
    assert not inspect.isabstract(MappingEndCS)


def test_mappingendcs_constructor_exists():
    assert callable(MappingEndCS.__init__)


def test_mappingendcs_constructor_args():
    sig = inspect.signature(MappingEndCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingbodycs_is_not_abstract():
    assert not inspect.isabstract(MappingBodyCS)


def test_mappingbodycs_constructor_exists():
    assert callable(MappingBodyCS.__init__)


def test_mappingbodycs_constructor_args():
    sig = inspect.signature(MappingBodyCS.__init__)
    params = list(sig.parameters.keys())



def test_mappinginitcs_is_not_abstract():
    assert not inspect.isabstract(MappingInitCS)


def test_mappinginitcs_constructor_exists():
    assert callable(MappingInitCS.__init__)


def test_mappinginitcs_constructor_args():
    sig = inspect.signature(MappingInitCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::mappingsectionscs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MappingSectionsCS)


def test_qvtoperational::cst::mappingsectionscs_constructor_exists():
    assert callable(qvtoperational::cst::MappingSectionsCS.__init__)


def test_qvtoperational::cst::mappingsectionscs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MappingSectionsCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingsectioncs_is_not_abstract():
    assert not inspect.isabstract(MappingSectionCS)


def test_mappingsectioncs_constructor_exists():
    assert callable(MappingSectionCS.__init__)


def test_mappingsectioncs_constructor_args():
    sig = inspect.signature(MappingSectionCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::mappingendcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MappingEndCS)


def test_qvtoperational::cst::mappingendcs_constructor_exists():
    assert callable(qvtoperational::cst::MappingEndCS.__init__)


def test_qvtoperational::cst::mappingendcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MappingEndCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::mappingbodycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MappingBodyCS)


def test_qvtoperational::cst::mappingbodycs_constructor_exists():
    assert callable(qvtoperational::cst::MappingBodyCS.__init__)


def test_qvtoperational::cst::mappingbodycs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MappingBodyCS.__init__)
    params = list(sig.parameters.keys())
    assert "hasPopulationKeyword" in params, "Missing parameter 'hasPopulationKeyword'"

def test_qvtoperational::cst::mappingbodycs_has_hasPopulationKeyword():
    assert hasattr(qvtoperational::cst::MappingBodyCS, "hasPopulationKeyword")
    descriptor = None
    for klass in qvtoperational::cst::MappingBodyCS.__mro__:
        if "hasPopulationKeyword" in klass.__dict__:
            descriptor = klass.__dict__["hasPopulationKeyword"]
            break
    assert isinstance(descriptor, property)



def test_qvtoperational::cst::mappinginitcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MappingInitCS)


def test_qvtoperational::cst::mappinginitcs_constructor_exists():
    assert callable(qvtoperational::cst::MappingInitCS.__init__)


def test_qvtoperational::cst::mappinginitcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MappingInitCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingrulecs_is_not_abstract():
    assert not inspect.isabstract(MappingRuleCS)


def test_mappingrulecs_constructor_exists():
    assert callable(MappingRuleCS.__init__)


def test_mappingrulecs_constructor_args():
    sig = inspect.signature(MappingRuleCS.__init__)
    params = list(sig.parameters.keys())



def test_cst::elementwithbody_is_not_abstract():
    assert not inspect.isabstract(cst::ElementWithBody)


def test_cst::elementwithbody_constructor_exists():
    assert callable(cst::ElementWithBody.__init__)


def test_cst::elementwithbody_constructor_args():
    sig = inspect.signature(cst::ElementWithBody.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::objectexpcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ObjectExpCS)


def test_qvtoperational::cst::objectexpcs_constructor_exists():
    assert callable(qvtoperational::cst::ObjectExpCS.__init__)


def test_qvtoperational::cst::objectexpcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ObjectExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "isImplicit" in params, "Missing parameter 'isImplicit'"

def test_qvtoperational::cst::objectexpcs_has_isImplicit():
    assert hasattr(qvtoperational::cst::ObjectExpCS, "isImplicit")
    descriptor = None
    for klass in qvtoperational::cst::ObjectExpCS.__mro__:
        if "isImplicit" in klass.__dict__:
            descriptor = klass.__dict__["isImplicit"]
            break
    assert isinstance(descriptor, property)



def test_cst::cstnode_is_not_abstract():
    assert not inspect.isabstract(cst::CSTNode)


def test_cst::cstnode_constructor_exists():
    assert callable(cst::CSTNode.__init__)


def test_cst::cstnode_constructor_args():
    sig = inspect.signature(cst::CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::modeltypecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ModelTypeCS)


def test_qvtoperational::cst::modeltypecs_constructor_exists():
    assert callable(qvtoperational::cst::ModelTypeCS.__init__)


def test_qvtoperational::cst::modeltypecs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ModelTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::mappingsectioncs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MappingSectionCS)


def test_qvtoperational::cst::mappingsectioncs_constructor_exists():
    assert callable(qvtoperational::cst::MappingSectionCS.__init__)


def test_qvtoperational::cst::mappingsectioncs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MappingSectionCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::constructorcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ConstructorCS)


def test_qvtoperational::cst::constructorcs_constructor_exists():
    assert callable(qvtoperational::cst::ConstructorCS.__init__)


def test_qvtoperational::cst::constructorcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ConstructorCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::mappingquerycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MappingQueryCS)


def test_qvtoperational::cst::mappingquerycs_constructor_exists():
    assert callable(qvtoperational::cst::MappingQueryCS.__init__)


def test_qvtoperational::cst::mappingquerycs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MappingQueryCS.__init__)
    params = list(sig.parameters.keys())
    assert "isSimpleDefinition" in params, "Missing parameter 'isSimpleDefinition'"

def test_qvtoperational::cst::mappingquerycs_has_isSimpleDefinition():
    assert hasattr(qvtoperational::cst::MappingQueryCS, "isSimpleDefinition")
    descriptor = None
    for klass in qvtoperational::cst::MappingQueryCS.__mro__:
        if "isSimpleDefinition" in klass.__dict__:
            descriptor = klass.__dict__["isSimpleDefinition"]
            break
    assert isinstance(descriptor, property)



def test_mappingsectionscs_is_not_abstract():
    assert not inspect.isabstract(MappingSectionsCS)


def test_mappingsectionscs_constructor_exists():
    assert callable(MappingSectionsCS.__init__)


def test_mappingsectionscs_constructor_args():
    sig = inspect.signature(MappingSectionsCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::mappingrulecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MappingRuleCS)


def test_qvtoperational::cst::mappingrulecs_constructor_exists():
    assert callable(qvtoperational::cst::MappingRuleCS.__init__)


def test_qvtoperational::cst::mappingrulecs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MappingRuleCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(MappingDeclarationCS)


def test_mappingdeclarationcs_constructor_exists():
    assert callable(MappingDeclarationCS.__init__)


def test_mappingdeclarationcs_constructor_args():
    sig = inspect.signature(MappingDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::mappingmethodcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MappingMethodCS)


def test_qvtoperational::cst::mappingmethodcs_constructor_exists():
    assert callable(qvtoperational::cst::MappingMethodCS.__init__)


def test_qvtoperational::cst::mappingmethodcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MappingMethodCS.__init__)
    params = list(sig.parameters.keys())
    assert "blackBox" in params, "Missing parameter 'blackBox'"

def test_qvtoperational::cst::mappingmethodcs_has_blackBox():
    assert hasattr(qvtoperational::cst::MappingMethodCS, "blackBox")
    descriptor = None
    for klass in qvtoperational::cst::MappingMethodCS.__mro__:
        if "blackBox" in klass.__dict__:
            descriptor = klass.__dict__["blackBox"]
            break
    assert isinstance(descriptor, property)



def test_simplesignaturecs_is_not_abstract():
    assert not inspect.isabstract(SimpleSignatureCS)


def test_simplesignaturecs_constructor_exists():
    assert callable(SimpleSignatureCS.__init__)


def test_simplesignaturecs_constructor_args():
    sig = inspect.signature(SimpleSignatureCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::completesignaturecs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::CompleteSignatureCS)


def test_qvtoperational::cst::completesignaturecs_constructor_exists():
    assert callable(qvtoperational::cst::CompleteSignatureCS.__init__)


def test_qvtoperational::cst::completesignaturecs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::CompleteSignatureCS.__init__)
    params = list(sig.parameters.keys())



def test_typespeccs_is_not_abstract():
    assert not inspect.isabstract(TypeSpecCS)


def test_typespeccs_constructor_exists():
    assert callable(TypeSpecCS.__init__)


def test_typespeccs_constructor_args():
    sig = inspect.signature(TypeSpecCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::parameterdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ParameterDeclarationCS)


def test_qvtoperational::cst::parameterdeclarationcs_constructor_exists():
    assert callable(qvtoperational::cst::ParameterDeclarationCS.__init__)


def test_qvtoperational::cst::parameterdeclarationcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ParameterDeclarationCS.__init__)
    params = list(sig.parameters.keys())
    assert "directionKind" in params, "Missing parameter 'directionKind'"

def test_qvtoperational::cst::parameterdeclarationcs_has_directionKind():
    assert hasattr(qvtoperational::cst::ParameterDeclarationCS, "directionKind")
    descriptor = None
    for klass in qvtoperational::cst::ParameterDeclarationCS.__mro__:
        if "directionKind" in klass.__dict__:
            descriptor = klass.__dict__["directionKind"]
            break
    assert isinstance(descriptor, property)



def test_mappingextensioncs_is_not_abstract():
    assert not inspect.isabstract(MappingExtensionCS)


def test_mappingextensioncs_constructor_exists():
    assert callable(MappingExtensionCS.__init__)


def test_mappingextensioncs_constructor_args():
    sig = inspect.signature(MappingExtensionCS.__init__)
    params = list(sig.parameters.keys())



def test_directionkindcs_is_not_abstract():
    assert not inspect.isabstract(DirectionKindCS)


def test_directionkindcs_constructor_exists():
    assert callable(DirectionKindCS.__init__)


def test_directionkindcs_constructor_args():
    sig = inspect.signature(DirectionKindCS.__init__)
    params = list(sig.parameters.keys())



def test_parameterdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(ParameterDeclarationCS)


def test_parameterdeclarationcs_constructor_exists():
    assert callable(ParameterDeclarationCS.__init__)


def test_parameterdeclarationcs_constructor_args():
    sig = inspect.signature(ParameterDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::mappingdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MappingDeclarationCS)


def test_qvtoperational::cst::mappingdeclarationcs_constructor_exists():
    assert callable(qvtoperational::cst::MappingDeclarationCS.__init__)


def test_qvtoperational::cst::mappingdeclarationcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MappingDeclarationCS.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"
    assert "qualifiers" in params, "Missing parameter 'qualifiers'"

def test_qvtoperational::cst::mappingdeclarationcs_has_isQuery():
    assert hasattr(qvtoperational::cst::MappingDeclarationCS, "isQuery")
    descriptor = None
    for klass in qvtoperational::cst::MappingDeclarationCS.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)

def test_qvtoperational::cst::mappingdeclarationcs_has_qualifiers():
    assert hasattr(qvtoperational::cst::MappingDeclarationCS, "qualifiers")
    descriptor = None
    for klass in qvtoperational::cst::MappingDeclarationCS.__mro__:
        if "qualifiers" in klass.__dict__:
            descriptor = klass.__dict__["qualifiers"]
            break
    assert isinstance(descriptor, property)



def test_primitiveliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExpCS)


def test_primitiveliteralexpcs_constructor_exists():
    assert callable(PrimitiveLiteralExpCS.__init__)


def test_primitiveliteralexpcs_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::multiplicitydefcs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::MultiplicityDefCS)


def test_qvtoperational::cst::multiplicitydefcs_constructor_exists():
    assert callable(qvtoperational::cst::MultiplicityDefCS.__init__)


def test_qvtoperational::cst::multiplicitydefcs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::MultiplicityDefCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::oppositepropertycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::OppositePropertyCS)


def test_qvtoperational::cst::oppositepropertycs_constructor_exists():
    assert callable(qvtoperational::cst::OppositePropertyCS.__init__)


def test_qvtoperational::cst::oppositepropertycs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::OppositePropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "isNavigable" in params, "Missing parameter 'isNavigable'"

def test_qvtoperational::cst::oppositepropertycs_has_isNavigable():
    assert hasattr(qvtoperational::cst::OppositePropertyCS, "isNavigable")
    descriptor = None
    for klass in qvtoperational::cst::OppositePropertyCS.__mro__:
        if "isNavigable" in klass.__dict__:
            descriptor = klass.__dict__["isNavigable"]
            break
    assert isinstance(descriptor, property)



def test_oppositepropertycs_is_not_abstract():
    assert not inspect.isabstract(OppositePropertyCS)


def test_oppositepropertycs_constructor_exists():
    assert callable(OppositePropertyCS.__init__)


def test_oppositepropertycs_constructor_args():
    sig = inspect.signature(OppositePropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_multiplicitydefcs_is_not_abstract():
    assert not inspect.isabstract(MultiplicityDefCS)


def test_multiplicitydefcs_constructor_exists():
    assert callable(MultiplicityDefCS.__init__)


def test_multiplicitydefcs_constructor_args():
    sig = inspect.signature(MultiplicityDefCS.__init__)
    params = list(sig.parameters.keys())



def test_localpropertycs_is_not_abstract():
    assert not inspect.isabstract(LocalPropertyCS)


def test_localpropertycs_constructor_exists():
    assert callable(LocalPropertyCS.__init__)


def test_localpropertycs_constructor_args():
    sig = inspect.signature(LocalPropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtoperational::cst::classifierpropertycs_is_not_abstract():
    assert not inspect.isabstract(qvtoperational::cst::ClassifierPropertyCS)


def test_qvtoperational::cst::classifierpropertycs_constructor_exists():
    assert callable(qvtoperational::cst::ClassifierPropertyCS.__init__)


def test_qvtoperational::cst::classifierpropertycs_constructor_args():
    sig = inspect.signature(qvtoperational::cst::ClassifierPropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_qvtoperational::cst::classifierpropertycs_has_isOrdered():
    assert hasattr(qvtoperational::cst::ClassifierPropertyCS, "isOrdered")
    descriptor = None
    for klass in qvtoperational::cst::ClassifierPropertyCS.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_renamecs_is_not_abstract():
    assert not inspect.isabstract(RenameCS)


def test_renamecs_constructor_exists():
    assert callable(RenameCS.__init__)


def test_renamecs_constructor_args():
    sig = inspect.signature(RenameCS.__init__)
    params = list(sig.parameters.keys())

def test_importkindenum_exists():
    # Check that the Enumeration exists
    assert ImportKindEnum is not None

def test_importkindenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImportKindEnum]
    expected_literals = [
        "access",
        "extension",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImportKindEnum"

def test_mappingextensionkindcs_exists():
    # Check that the Enumeration exists
    assert MappingExtensionKindCS is not None

def test_mappingextensionkindcs_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MappingExtensionKindCS]
    expected_literals = [
        "merges",
        "disjuncts",
        "inherits",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MappingExtensionKindCS"

def test_modulekindenum_exists():
    # Check that the Enumeration exists
    assert ModuleKindEnum is not None

def test_modulekindenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModuleKindEnum]
    expected_literals = [
        "transformation",
        "library",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModuleKindEnum"

def test_directionkindenum_exists():
    # Check that the Enumeration exists
    assert DirectionKindEnum is not None

def test_directionkindenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionKindEnum]
    expected_literals = [
        "in_",
        "DEFAULT",
        "inout",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionKindEnum"

def test_qualifierkindcs_exists():
    # Check that the Enumeration exists
    assert QualifierKindCS is not None

def test_qualifierkindcs_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QualifierKindCS]
    expected_literals = [
        "abstract",
        "blackbox",
        "static",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QualifierKindCS"


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
ClassifierPropertyCS_strategy = st.builds(
    ClassifierPropertyCS,
)
ScopedNameCS_strategy = st.builds(
    ScopedNameCS,
)
OCLExpressionCS_strategy = st.builds(
    OCLExpressionCS,
)
StringLiteralExpCS_strategy = st.builds(
    StringLiteralExpCS,
)
SimpleNameCS_strategy = st.builds(
    SimpleNameCS,
)
TypeCS_strategy = st.builds(
    TypeCS,
)
PathNameCS_strategy = st.builds(
    PathNameCS,
)
MappingModuleCS_strategy = st.builds(
    MappingModuleCS,
)
qvtoperational::cst::LibraryCS_strategy = st.builds(
    qvtoperational::cst::LibraryCS,
)
TagCS_strategy = st.builds(
    TagCS,
)
ClassifierDefCS_strategy = st.builds(
    ClassifierDefCS,
)
MappingMethodCS_strategy = st.builds(
    MappingMethodCS,
)
ModulePropertyCS_strategy = st.builds(
    ModulePropertyCS,
)
qvtoperational::cst::LocalPropertyCS_strategy = st.builds(
    qvtoperational::cst::LocalPropertyCS,
)
qvtoperational::cst::ContextualPropertyCS_strategy = st.builds(
    qvtoperational::cst::ContextualPropertyCS,
)
qvtoperational::cst::ConfigPropertyCS_strategy = st.builds(
    qvtoperational::cst::ConfigPropertyCS,
)
ModelTypeCS_strategy = st.builds(
    ModelTypeCS,
)
ImportCS_strategy = st.builds(
    ImportCS,
)
qvtoperational::cst::LibraryImportCS_strategy = st.builds(
    qvtoperational::cst::LibraryImportCS,
)
TransformationHeaderCS_strategy = st.builds(
    TransformationHeaderCS,
)
CSTNode_strategy = st.builds(
    CSTNode,
)
qvtoperational::cst::ImportCS_strategy = st.builds(
    qvtoperational::cst::ImportCS,
)
qvtoperational::cst::ModulePropertyCS_strategy = st.builds(
    qvtoperational::cst::ModulePropertyCS,
)
qvtoperational::cst::ClassifierDefCS_strategy = st.builds(
    qvtoperational::cst::ClassifierDefCS,
)
qvtoperational::cst::RenameCS_strategy = st.builds(
    qvtoperational::cst::RenameCS,
)
qvtoperational::cst::MappingModuleCS_strategy = st.builds(
    qvtoperational::cst::MappingModuleCS,
)
qvtoperational::cst::ScopedNameCS_strategy = st.builds(
    qvtoperational::cst::ScopedNameCS,
    name=
        safe_text
)
qvtoperational::cst::ResolveOpArgsExpCS_strategy = st.builds(
    qvtoperational::cst::ResolveOpArgsExpCS,
)
qvtoperational::cst::ListTypeCS_strategy = st.builds(
    qvtoperational::cst::ListTypeCS,
)
qvtoperational::cst::UnitCS_strategy = st.builds(
    qvtoperational::cst::UnitCS,
)
qvtoperational::cst::TagCS_strategy = st.builds(
    qvtoperational::cst::TagCS,
)
qvtoperational::cst::DictLiteralPartCS_strategy = st.builds(
    qvtoperational::cst::DictLiteralPartCS,
)
DictLiteralPartCS_strategy = st.builds(
    DictLiteralPartCS,
)
qvtoperational::cst::DictionaryTypeCS_strategy = st.builds(
    qvtoperational::cst::DictionaryTypeCS,
)
CollectionLiteralPartCS_strategy = st.builds(
    CollectionLiteralPartCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
qvtoperational::cst::ListLiteralExpCS_strategy = st.builds(
    qvtoperational::cst::ListLiteralExpCS,
)
qvtoperational::cst::DictLiteralExpCS_strategy = st.builds(
    qvtoperational::cst::DictLiteralExpCS,
)
qvtoperational::cst::TransformationRefineCS_strategy = st.builds(
    qvtoperational::cst::TransformationRefineCS,
)
ModuleRefCS_strategy = st.builds(
    ModuleRefCS,
)
ModuleKindCS_strategy = st.builds(
    ModuleKindCS,
)
qvtoperational::cst::MappingExtensionCS_strategy = st.builds(
    qvtoperational::cst::MappingExtensionCS,
    kind=
        safe_text
)
LogExpCS_strategy = st.builds(
    LogExpCS,
)
qvtoperational::cst::TypeSpecCS_strategy = st.builds(
    qvtoperational::cst::TypeSpecCS,
)
qvtoperational::cst::ModuleUsageCS_strategy = st.builds(
    qvtoperational::cst::ModuleUsageCS,
    importKind=
        safe_text
)
qvtoperational::cst::ModuleRefCS_strategy = st.builds(
    qvtoperational::cst::ModuleRefCS,
)
qvtoperational::cst::ModuleKindCS_strategy = st.builds(
    qvtoperational::cst::ModuleKindCS,
    moduleKind=
        safe_text
)
TransformationRefineCS_strategy = st.builds(
    TransformationRefineCS,
)
ModuleUsageCS_strategy = st.builds(
    ModuleUsageCS,
)
qvtoperational::cst::TransformationHeaderCS_strategy = st.builds(
    qvtoperational::cst::TransformationHeaderCS,
)
qvtoperational::cst::PackageRefCS_strategy = st.builds(
    qvtoperational::cst::PackageRefCS,
)
PackageRefCS_strategy = st.builds(
    PackageRefCS,
)
ResolveExpCS_strategy = st.builds(
    ResolveExpCS,
)
qvtoperational::cst::ResolveInExpCS_strategy = st.builds(
    qvtoperational::cst::ResolveInExpCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
qvtoperational::cst::ResolveExpCS_strategy = st.builds(
    qvtoperational::cst::ResolveExpCS,
    isInverse=
        st.booleans(),
    one=
        st.booleans(),
    isDeferred=
        st.booleans()
)
qvtoperational::cst::ElementWithBody_strategy = st.builds(
    qvtoperational::cst::ElementWithBody,
    bodyStartLocation=
        st.integers(),
    bodyEndLocation=
        st.integers()
)
qvtoperational::cst::DirectionKindCS_strategy = st.builds(
    qvtoperational::cst::DirectionKindCS,
    directionKind=
        safe_text
)
OperationCallExpCS_strategy = st.builds(
    OperationCallExpCS,
)
qvtoperational::cst::LogExpCS_strategy = st.builds(
    qvtoperational::cst::LogExpCS,
)
qvtoperational::cst::ImperativeOperationCallExpCS_strategy = st.builds(
    qvtoperational::cst::ImperativeOperationCallExpCS,
)
ImperativeOperationCallExpCS_strategy = st.builds(
    ImperativeOperationCallExpCS,
)
qvtoperational::cst::MappingCallExpCS_strategy = st.builds(
    qvtoperational::cst::MappingCallExpCS,
    strict=
        st.booleans()
)
cst::InstantiationExpCS_strategy = st.builds(
    cst::InstantiationExpCS,
)
SwitchAltExpCS_strategy = st.builds(
    SwitchAltExpCS,
)
ImperativeLoopExpCS_strategy = st.builds(
    ImperativeLoopExpCS,
)
qvtoperational::cst::ImperativeIterateExpCS_strategy = st.builds(
    qvtoperational::cst::ImperativeIterateExpCS,
)
qvtoperational::cst::ForExpCS_strategy = st.builds(
    qvtoperational::cst::ForExpCS,
)
cst::StatementCS_strategy = st.builds(
    cst::StatementCS,
)
cst::LoopExpCS_strategy = st.builds(
    cst::LoopExpCS,
)
qvtoperational::cst::ImperativeLoopExpCS_strategy = st.builds(
    qvtoperational::cst::ImperativeLoopExpCS,
)
qvtoperational::cst::SimpleSignatureCS_strategy = st.builds(
    qvtoperational::cst::SimpleSignatureCS,
)
VariableCS_strategy = st.builds(
    VariableCS,
)
StatementCS_strategy = st.builds(
    StatementCS,
)
qvtoperational::cst::InstantiationExpCS_strategy = st.builds(
    qvtoperational::cst::InstantiationExpCS,
)
qvtoperational::cst::VariableInitializationCS_strategy = st.builds(
    qvtoperational::cst::VariableInitializationCS,
    withResult=
        st.booleans()
)
qvtoperational::cst::ComputeExpCS_strategy = st.builds(
    qvtoperational::cst::ComputeExpCS,
)
qvtoperational::cst::ReturnExpCS_strategy = st.builds(
    qvtoperational::cst::ReturnExpCS,
)
qvtoperational::cst::SwitchExpCS_strategy = st.builds(
    qvtoperational::cst::SwitchExpCS,
)
qvtoperational::cst::AssignStatementCS_strategy = st.builds(
    qvtoperational::cst::AssignStatementCS,
    incremental=
        st.booleans()
)
qvtoperational::cst::ExpressionStatementCS_strategy = st.builds(
    qvtoperational::cst::ExpressionStatementCS,
)
qvtoperational::cst::BreakExpCS_strategy = st.builds(
    qvtoperational::cst::BreakExpCS,
)
qvtoperational::cst::ContinueExpCS_strategy = st.builds(
    qvtoperational::cst::ContinueExpCS,
)
qvtoperational::cst::SwitchAltExpCS_strategy = st.builds(
    qvtoperational::cst::SwitchAltExpCS,
)
qvtoperational::cst::AssertExpCS_strategy = st.builds(
    qvtoperational::cst::AssertExpCS,
)
qvtoperational::cst::WhileExpCS_strategy = st.builds(
    qvtoperational::cst::WhileExpCS,
)
qvtoperational::cst::BlockExpCS_strategy = st.builds(
    qvtoperational::cst::BlockExpCS,
)
qvtoperational::cst::StatementCS_strategy = st.builds(
    qvtoperational::cst::StatementCS,
)
MappingEndCS_strategy = st.builds(
    MappingEndCS,
)
MappingBodyCS_strategy = st.builds(
    MappingBodyCS,
)
MappingInitCS_strategy = st.builds(
    MappingInitCS,
)
qvtoperational::cst::MappingSectionsCS_strategy = st.builds(
    qvtoperational::cst::MappingSectionsCS,
)
MappingSectionCS_strategy = st.builds(
    MappingSectionCS,
)
qvtoperational::cst::MappingEndCS_strategy = st.builds(
    qvtoperational::cst::MappingEndCS,
)
qvtoperational::cst::MappingBodyCS_strategy = st.builds(
    qvtoperational::cst::MappingBodyCS,
    hasPopulationKeyword=
        st.booleans()
)
qvtoperational::cst::MappingInitCS_strategy = st.builds(
    qvtoperational::cst::MappingInitCS,
)
MappingRuleCS_strategy = st.builds(
    MappingRuleCS,
)
cst::ElementWithBody_strategy = st.builds(
    cst::ElementWithBody,
)
qvtoperational::cst::ObjectExpCS_strategy = st.builds(
    qvtoperational::cst::ObjectExpCS,
    isImplicit=
        st.booleans()
)
cst::CSTNode_strategy = st.builds(
    cst::CSTNode,
)
qvtoperational::cst::ModelTypeCS_strategy = st.builds(
    qvtoperational::cst::ModelTypeCS,
)
qvtoperational::cst::MappingSectionCS_strategy = st.builds(
    qvtoperational::cst::MappingSectionCS,
)
qvtoperational::cst::ConstructorCS_strategy = st.builds(
    qvtoperational::cst::ConstructorCS,
)
qvtoperational::cst::MappingQueryCS_strategy = st.builds(
    qvtoperational::cst::MappingQueryCS,
    isSimpleDefinition=
        st.booleans()
)
MappingSectionsCS_strategy = st.builds(
    MappingSectionsCS,
)
qvtoperational::cst::MappingRuleCS_strategy = st.builds(
    qvtoperational::cst::MappingRuleCS,
)
MappingDeclarationCS_strategy = st.builds(
    MappingDeclarationCS,
)
qvtoperational::cst::MappingMethodCS_strategy = st.builds(
    qvtoperational::cst::MappingMethodCS,
    blackBox=
        st.booleans()
)
SimpleSignatureCS_strategy = st.builds(
    SimpleSignatureCS,
)
qvtoperational::cst::CompleteSignatureCS_strategy = st.builds(
    qvtoperational::cst::CompleteSignatureCS,
)
TypeSpecCS_strategy = st.builds(
    TypeSpecCS,
)
qvtoperational::cst::ParameterDeclarationCS_strategy = st.builds(
    qvtoperational::cst::ParameterDeclarationCS,
    directionKind=
        safe_text
)
MappingExtensionCS_strategy = st.builds(
    MappingExtensionCS,
)
DirectionKindCS_strategy = st.builds(
    DirectionKindCS,
)
ParameterDeclarationCS_strategy = st.builds(
    ParameterDeclarationCS,
)
qvtoperational::cst::MappingDeclarationCS_strategy = st.builds(
    qvtoperational::cst::MappingDeclarationCS,
    isQuery=
        st.booleans(),
    qualifiers=
        safe_text
)
PrimitiveLiteralExpCS_strategy = st.builds(
    PrimitiveLiteralExpCS,
)
qvtoperational::cst::MultiplicityDefCS_strategy = st.builds(
    qvtoperational::cst::MultiplicityDefCS,
)
qvtoperational::cst::OppositePropertyCS_strategy = st.builds(
    qvtoperational::cst::OppositePropertyCS,
    isNavigable=
        st.booleans()
)
OppositePropertyCS_strategy = st.builds(
    OppositePropertyCS,
)
MultiplicityDefCS_strategy = st.builds(
    MultiplicityDefCS,
)
LocalPropertyCS_strategy = st.builds(
    LocalPropertyCS,
)
qvtoperational::cst::ClassifierPropertyCS_strategy = st.builds(
    qvtoperational::cst::ClassifierPropertyCS,
    isOrdered=
        st.booleans()
)
RenameCS_strategy = st.builds(
    RenameCS,
)

@given(instance=ClassifierPropertyCS_strategy)
@settings(max_examples=50)
def test_classifierpropertycs_instantiation(instance):
    assert isinstance(instance, ClassifierPropertyCS)

@given(instance=ScopedNameCS_strategy)
@settings(max_examples=50)
def test_scopednamecs_instantiation(instance):
    assert isinstance(instance, ScopedNameCS)

@given(instance=OCLExpressionCS_strategy)
@settings(max_examples=50)
def test_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, OCLExpressionCS)

@given(instance=StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, StringLiteralExpCS)

@given(instance=SimpleNameCS_strategy)
@settings(max_examples=50)
def test_simplenamecs_instantiation(instance):
    assert isinstance(instance, SimpleNameCS)

@given(instance=TypeCS_strategy)
@settings(max_examples=50)
def test_typecs_instantiation(instance):
    assert isinstance(instance, TypeCS)

@given(instance=PathNameCS_strategy)
@settings(max_examples=50)
def test_pathnamecs_instantiation(instance):
    assert isinstance(instance, PathNameCS)

@given(instance=MappingModuleCS_strategy)
@settings(max_examples=50)
def test_mappingmodulecs_instantiation(instance):
    assert isinstance(instance, MappingModuleCS)

@given(instance=qvtoperational::cst::LibraryCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::librarycs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::LibraryCS)

@given(instance=TagCS_strategy)
@settings(max_examples=50)
def test_tagcs_instantiation(instance):
    assert isinstance(instance, TagCS)

@given(instance=ClassifierDefCS_strategy)
@settings(max_examples=50)
def test_classifierdefcs_instantiation(instance):
    assert isinstance(instance, ClassifierDefCS)

@given(instance=MappingMethodCS_strategy)
@settings(max_examples=50)
def test_mappingmethodcs_instantiation(instance):
    assert isinstance(instance, MappingMethodCS)

@given(instance=ModulePropertyCS_strategy)
@settings(max_examples=50)
def test_modulepropertycs_instantiation(instance):
    assert isinstance(instance, ModulePropertyCS)

@given(instance=qvtoperational::cst::LocalPropertyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::localpropertycs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::LocalPropertyCS)

@given(instance=qvtoperational::cst::ContextualPropertyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::contextualpropertycs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ContextualPropertyCS)

@given(instance=qvtoperational::cst::ConfigPropertyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::configpropertycs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ConfigPropertyCS)

@given(instance=ModelTypeCS_strategy)
@settings(max_examples=50)
def test_modeltypecs_instantiation(instance):
    assert isinstance(instance, ModelTypeCS)

@given(instance=ImportCS_strategy)
@settings(max_examples=50)
def test_importcs_instantiation(instance):
    assert isinstance(instance, ImportCS)

@given(instance=qvtoperational::cst::LibraryImportCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::libraryimportcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::LibraryImportCS)

@given(instance=TransformationHeaderCS_strategy)
@settings(max_examples=50)
def test_transformationheadercs_instantiation(instance):
    assert isinstance(instance, TransformationHeaderCS)

@given(instance=CSTNode_strategy)
@settings(max_examples=50)
def test_cstnode_instantiation(instance):
    assert isinstance(instance, CSTNode)

@given(instance=qvtoperational::cst::ImportCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::importcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ImportCS)

@given(instance=qvtoperational::cst::ModulePropertyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::modulepropertycs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ModulePropertyCS)

@given(instance=qvtoperational::cst::ClassifierDefCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::classifierdefcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ClassifierDefCS)

@given(instance=qvtoperational::cst::RenameCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::renamecs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::RenameCS)

@given(instance=qvtoperational::cst::MappingModuleCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::mappingmodulecs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MappingModuleCS)

@given(instance=qvtoperational::cst::ScopedNameCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::scopednamecs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ScopedNameCS)

@given(instance=qvtoperational::cst::ScopedNameCS_strategy)
def test_qvtoperational::cst::scopednamecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=qvtoperational::cst::ScopedNameCS_strategy)
def test_qvtoperational::cst::scopednamecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=qvtoperational::cst::ResolveOpArgsExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::resolveopargsexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ResolveOpArgsExpCS)

@given(instance=qvtoperational::cst::ListTypeCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::listtypecs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ListTypeCS)

@given(instance=qvtoperational::cst::UnitCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::unitcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::UnitCS)

@given(instance=qvtoperational::cst::TagCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::tagcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::TagCS)

@given(instance=qvtoperational::cst::DictLiteralPartCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::dictliteralpartcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::DictLiteralPartCS)

@given(instance=DictLiteralPartCS_strategy)
@settings(max_examples=50)
def test_dictliteralpartcs_instantiation(instance):
    assert isinstance(instance, DictLiteralPartCS)

@given(instance=qvtoperational::cst::DictionaryTypeCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::dictionarytypecs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::DictionaryTypeCS)

@given(instance=CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPartCS)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=qvtoperational::cst::ListLiteralExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::listliteralexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ListLiteralExpCS)

@given(instance=qvtoperational::cst::DictLiteralExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::dictliteralexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::DictLiteralExpCS)

@given(instance=qvtoperational::cst::TransformationRefineCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::transformationrefinecs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::TransformationRefineCS)

@given(instance=ModuleRefCS_strategy)
@settings(max_examples=50)
def test_modulerefcs_instantiation(instance):
    assert isinstance(instance, ModuleRefCS)

@given(instance=ModuleKindCS_strategy)
@settings(max_examples=50)
def test_modulekindcs_instantiation(instance):
    assert isinstance(instance, ModuleKindCS)

@given(instance=qvtoperational::cst::MappingExtensionCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::mappingextensioncs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MappingExtensionCS)

@given(instance=qvtoperational::cst::MappingExtensionCS_strategy)
def test_qvtoperational::cst::mappingextensioncs_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=qvtoperational::cst::MappingExtensionCS_strategy)
def test_qvtoperational::cst::mappingextensioncs_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=LogExpCS_strategy)
@settings(max_examples=50)
def test_logexpcs_instantiation(instance):
    assert isinstance(instance, LogExpCS)

@given(instance=qvtoperational::cst::TypeSpecCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::typespeccs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::TypeSpecCS)

@given(instance=qvtoperational::cst::ModuleUsageCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::moduleusagecs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ModuleUsageCS)

@given(instance=qvtoperational::cst::ModuleUsageCS_strategy)
def test_qvtoperational::cst::moduleusagecs_importKind_type(instance):
    assert isinstance(instance.importKind, str)


@given(instance=qvtoperational::cst::ModuleUsageCS_strategy)
def test_qvtoperational::cst::moduleusagecs_importKind_setter(instance):
    original = instance.importKind
    instance.importKind = original
    assert instance.importKind == original

@given(instance=qvtoperational::cst::ModuleRefCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::modulerefcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ModuleRefCS)

@given(instance=qvtoperational::cst::ModuleKindCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::modulekindcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ModuleKindCS)

@given(instance=qvtoperational::cst::ModuleKindCS_strategy)
def test_qvtoperational::cst::modulekindcs_moduleKind_type(instance):
    assert isinstance(instance.moduleKind, str)


@given(instance=qvtoperational::cst::ModuleKindCS_strategy)
def test_qvtoperational::cst::modulekindcs_moduleKind_setter(instance):
    original = instance.moduleKind
    instance.moduleKind = original
    assert instance.moduleKind == original

@given(instance=TransformationRefineCS_strategy)
@settings(max_examples=50)
def test_transformationrefinecs_instantiation(instance):
    assert isinstance(instance, TransformationRefineCS)

@given(instance=ModuleUsageCS_strategy)
@settings(max_examples=50)
def test_moduleusagecs_instantiation(instance):
    assert isinstance(instance, ModuleUsageCS)

@given(instance=qvtoperational::cst::TransformationHeaderCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::transformationheadercs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::TransformationHeaderCS)

@given(instance=qvtoperational::cst::PackageRefCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::packagerefcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::PackageRefCS)

@given(instance=PackageRefCS_strategy)
@settings(max_examples=50)
def test_packagerefcs_instantiation(instance):
    assert isinstance(instance, PackageRefCS)

@given(instance=ResolveExpCS_strategy)
@settings(max_examples=50)
def test_resolveexpcs_instantiation(instance):
    assert isinstance(instance, ResolveExpCS)

@given(instance=qvtoperational::cst::ResolveInExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::resolveinexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ResolveInExpCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=qvtoperational::cst::ResolveExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::resolveexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ResolveExpCS)

@given(instance=qvtoperational::cst::ResolveExpCS_strategy)
def test_qvtoperational::cst::resolveexpcs_isInverse_type(instance):
    assert isinstance(instance.isInverse, bool)


@given(instance=qvtoperational::cst::ResolveExpCS_strategy)
def test_qvtoperational::cst::resolveexpcs_isInverse_setter(instance):
    original = instance.isInverse
    instance.isInverse = original
    assert instance.isInverse == original

@given(instance=qvtoperational::cst::ResolveExpCS_strategy)
def test_qvtoperational::cst::resolveexpcs_one_type(instance):
    assert isinstance(instance.one, bool)


@given(instance=qvtoperational::cst::ResolveExpCS_strategy)
def test_qvtoperational::cst::resolveexpcs_one_setter(instance):
    original = instance.one
    instance.one = original
    assert instance.one == original

@given(instance=qvtoperational::cst::ResolveExpCS_strategy)
def test_qvtoperational::cst::resolveexpcs_isDeferred_type(instance):
    assert isinstance(instance.isDeferred, bool)


@given(instance=qvtoperational::cst::ResolveExpCS_strategy)
def test_qvtoperational::cst::resolveexpcs_isDeferred_setter(instance):
    original = instance.isDeferred
    instance.isDeferred = original
    assert instance.isDeferred == original

@given(instance=qvtoperational::cst::ElementWithBody_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::elementwithbody_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ElementWithBody)

@given(instance=qvtoperational::cst::ElementWithBody_strategy)
def test_qvtoperational::cst::elementwithbody_bodyStartLocation_type(instance):
    assert isinstance(instance.bodyStartLocation, int)


@given(instance=qvtoperational::cst::ElementWithBody_strategy)
def test_qvtoperational::cst::elementwithbody_bodyStartLocation_setter(instance):
    original = instance.bodyStartLocation
    instance.bodyStartLocation = original
    assert instance.bodyStartLocation == original

@given(instance=qvtoperational::cst::ElementWithBody_strategy)
def test_qvtoperational::cst::elementwithbody_bodyEndLocation_type(instance):
    assert isinstance(instance.bodyEndLocation, int)


@given(instance=qvtoperational::cst::ElementWithBody_strategy)
def test_qvtoperational::cst::elementwithbody_bodyEndLocation_setter(instance):
    original = instance.bodyEndLocation
    instance.bodyEndLocation = original
    assert instance.bodyEndLocation == original

@given(instance=qvtoperational::cst::DirectionKindCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::directionkindcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::DirectionKindCS)

@given(instance=qvtoperational::cst::DirectionKindCS_strategy)
def test_qvtoperational::cst::directionkindcs_directionKind_type(instance):
    assert isinstance(instance.directionKind, str)


@given(instance=qvtoperational::cst::DirectionKindCS_strategy)
def test_qvtoperational::cst::directionkindcs_directionKind_setter(instance):
    original = instance.directionKind
    instance.directionKind = original
    assert instance.directionKind == original

@given(instance=OperationCallExpCS_strategy)
@settings(max_examples=50)
def test_operationcallexpcs_instantiation(instance):
    assert isinstance(instance, OperationCallExpCS)

@given(instance=qvtoperational::cst::LogExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::logexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::LogExpCS)

@given(instance=qvtoperational::cst::ImperativeOperationCallExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::imperativeoperationcallexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ImperativeOperationCallExpCS)

@given(instance=ImperativeOperationCallExpCS_strategy)
@settings(max_examples=50)
def test_imperativeoperationcallexpcs_instantiation(instance):
    assert isinstance(instance, ImperativeOperationCallExpCS)

@given(instance=qvtoperational::cst::MappingCallExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::mappingcallexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MappingCallExpCS)

@given(instance=qvtoperational::cst::MappingCallExpCS_strategy)
def test_qvtoperational::cst::mappingcallexpcs_strict_type(instance):
    assert isinstance(instance.strict, bool)


@given(instance=qvtoperational::cst::MappingCallExpCS_strategy)
def test_qvtoperational::cst::mappingcallexpcs_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=cst::InstantiationExpCS_strategy)
@settings(max_examples=50)
def test_cst::instantiationexpcs_instantiation(instance):
    assert isinstance(instance, cst::InstantiationExpCS)

@given(instance=SwitchAltExpCS_strategy)
@settings(max_examples=50)
def test_switchaltexpcs_instantiation(instance):
    assert isinstance(instance, SwitchAltExpCS)

@given(instance=ImperativeLoopExpCS_strategy)
@settings(max_examples=50)
def test_imperativeloopexpcs_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExpCS)

@given(instance=qvtoperational::cst::ImperativeIterateExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::imperativeiterateexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ImperativeIterateExpCS)

@given(instance=qvtoperational::cst::ForExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::forexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ForExpCS)

@given(instance=cst::StatementCS_strategy)
@settings(max_examples=50)
def test_cst::statementcs_instantiation(instance):
    assert isinstance(instance, cst::StatementCS)

@given(instance=cst::LoopExpCS_strategy)
@settings(max_examples=50)
def test_cst::loopexpcs_instantiation(instance):
    assert isinstance(instance, cst::LoopExpCS)

@given(instance=qvtoperational::cst::ImperativeLoopExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::imperativeloopexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ImperativeLoopExpCS)

@given(instance=qvtoperational::cst::SimpleSignatureCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::simplesignaturecs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::SimpleSignatureCS)

@given(instance=VariableCS_strategy)
@settings(max_examples=50)
def test_variablecs_instantiation(instance):
    assert isinstance(instance, VariableCS)

@given(instance=StatementCS_strategy)
@settings(max_examples=50)
def test_statementcs_instantiation(instance):
    assert isinstance(instance, StatementCS)

@given(instance=qvtoperational::cst::InstantiationExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::instantiationexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::InstantiationExpCS)

@given(instance=qvtoperational::cst::VariableInitializationCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::variableinitializationcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::VariableInitializationCS)

@given(instance=qvtoperational::cst::VariableInitializationCS_strategy)
def test_qvtoperational::cst::variableinitializationcs_withResult_type(instance):
    assert isinstance(instance.withResult, bool)


@given(instance=qvtoperational::cst::VariableInitializationCS_strategy)
def test_qvtoperational::cst::variableinitializationcs_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=qvtoperational::cst::ComputeExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::computeexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ComputeExpCS)

@given(instance=qvtoperational::cst::ReturnExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::returnexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ReturnExpCS)

@given(instance=qvtoperational::cst::SwitchExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::switchexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::SwitchExpCS)

@given(instance=qvtoperational::cst::AssignStatementCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::assignstatementcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::AssignStatementCS)

@given(instance=qvtoperational::cst::AssignStatementCS_strategy)
def test_qvtoperational::cst::assignstatementcs_incremental_type(instance):
    assert isinstance(instance.incremental, bool)


@given(instance=qvtoperational::cst::AssignStatementCS_strategy)
def test_qvtoperational::cst::assignstatementcs_incremental_setter(instance):
    original = instance.incremental
    instance.incremental = original
    assert instance.incremental == original

@given(instance=qvtoperational::cst::ExpressionStatementCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::expressionstatementcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ExpressionStatementCS)

@given(instance=qvtoperational::cst::BreakExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::breakexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::BreakExpCS)

@given(instance=qvtoperational::cst::ContinueExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::continueexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ContinueExpCS)

@given(instance=qvtoperational::cst::SwitchAltExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::switchaltexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::SwitchAltExpCS)

@given(instance=qvtoperational::cst::AssertExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::assertexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::AssertExpCS)

@given(instance=qvtoperational::cst::WhileExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::whileexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::WhileExpCS)

@given(instance=qvtoperational::cst::BlockExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::blockexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::BlockExpCS)

@given(instance=qvtoperational::cst::StatementCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::statementcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::StatementCS)

@given(instance=MappingEndCS_strategy)
@settings(max_examples=50)
def test_mappingendcs_instantiation(instance):
    assert isinstance(instance, MappingEndCS)

@given(instance=MappingBodyCS_strategy)
@settings(max_examples=50)
def test_mappingbodycs_instantiation(instance):
    assert isinstance(instance, MappingBodyCS)

@given(instance=MappingInitCS_strategy)
@settings(max_examples=50)
def test_mappinginitcs_instantiation(instance):
    assert isinstance(instance, MappingInitCS)

@given(instance=qvtoperational::cst::MappingSectionsCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::mappingsectionscs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MappingSectionsCS)

@given(instance=MappingSectionCS_strategy)
@settings(max_examples=50)
def test_mappingsectioncs_instantiation(instance):
    assert isinstance(instance, MappingSectionCS)

@given(instance=qvtoperational::cst::MappingEndCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::mappingendcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MappingEndCS)

@given(instance=qvtoperational::cst::MappingBodyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::mappingbodycs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MappingBodyCS)

@given(instance=qvtoperational::cst::MappingBodyCS_strategy)
def test_qvtoperational::cst::mappingbodycs_hasPopulationKeyword_type(instance):
    assert isinstance(instance.hasPopulationKeyword, bool)


@given(instance=qvtoperational::cst::MappingBodyCS_strategy)
def test_qvtoperational::cst::mappingbodycs_hasPopulationKeyword_setter(instance):
    original = instance.hasPopulationKeyword
    instance.hasPopulationKeyword = original
    assert instance.hasPopulationKeyword == original

@given(instance=qvtoperational::cst::MappingInitCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::mappinginitcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MappingInitCS)

@given(instance=MappingRuleCS_strategy)
@settings(max_examples=50)
def test_mappingrulecs_instantiation(instance):
    assert isinstance(instance, MappingRuleCS)

@given(instance=cst::ElementWithBody_strategy)
@settings(max_examples=50)
def test_cst::elementwithbody_instantiation(instance):
    assert isinstance(instance, cst::ElementWithBody)

@given(instance=qvtoperational::cst::ObjectExpCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::objectexpcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ObjectExpCS)

@given(instance=qvtoperational::cst::ObjectExpCS_strategy)
def test_qvtoperational::cst::objectexpcs_isImplicit_type(instance):
    assert isinstance(instance.isImplicit, bool)


@given(instance=qvtoperational::cst::ObjectExpCS_strategy)
def test_qvtoperational::cst::objectexpcs_isImplicit_setter(instance):
    original = instance.isImplicit
    instance.isImplicit = original
    assert instance.isImplicit == original

@given(instance=cst::CSTNode_strategy)
@settings(max_examples=50)
def test_cst::cstnode_instantiation(instance):
    assert isinstance(instance, cst::CSTNode)

@given(instance=qvtoperational::cst::ModelTypeCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::modeltypecs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ModelTypeCS)

@given(instance=qvtoperational::cst::MappingSectionCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::mappingsectioncs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MappingSectionCS)

@given(instance=qvtoperational::cst::ConstructorCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::constructorcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ConstructorCS)

@given(instance=qvtoperational::cst::MappingQueryCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::mappingquerycs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MappingQueryCS)

@given(instance=qvtoperational::cst::MappingQueryCS_strategy)
def test_qvtoperational::cst::mappingquerycs_isSimpleDefinition_type(instance):
    assert isinstance(instance.isSimpleDefinition, bool)


@given(instance=qvtoperational::cst::MappingQueryCS_strategy)
def test_qvtoperational::cst::mappingquerycs_isSimpleDefinition_setter(instance):
    original = instance.isSimpleDefinition
    instance.isSimpleDefinition = original
    assert instance.isSimpleDefinition == original

@given(instance=MappingSectionsCS_strategy)
@settings(max_examples=50)
def test_mappingsectionscs_instantiation(instance):
    assert isinstance(instance, MappingSectionsCS)

@given(instance=qvtoperational::cst::MappingRuleCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::mappingrulecs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MappingRuleCS)

@given(instance=MappingDeclarationCS_strategy)
@settings(max_examples=50)
def test_mappingdeclarationcs_instantiation(instance):
    assert isinstance(instance, MappingDeclarationCS)

@given(instance=qvtoperational::cst::MappingMethodCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::mappingmethodcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MappingMethodCS)

@given(instance=qvtoperational::cst::MappingMethodCS_strategy)
def test_qvtoperational::cst::mappingmethodcs_blackBox_type(instance):
    assert isinstance(instance.blackBox, bool)


@given(instance=qvtoperational::cst::MappingMethodCS_strategy)
def test_qvtoperational::cst::mappingmethodcs_blackBox_setter(instance):
    original = instance.blackBox
    instance.blackBox = original
    assert instance.blackBox == original

@given(instance=SimpleSignatureCS_strategy)
@settings(max_examples=50)
def test_simplesignaturecs_instantiation(instance):
    assert isinstance(instance, SimpleSignatureCS)

@given(instance=qvtoperational::cst::CompleteSignatureCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::completesignaturecs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::CompleteSignatureCS)

@given(instance=TypeSpecCS_strategy)
@settings(max_examples=50)
def test_typespeccs_instantiation(instance):
    assert isinstance(instance, TypeSpecCS)

@given(instance=qvtoperational::cst::ParameterDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::parameterdeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ParameterDeclarationCS)

@given(instance=qvtoperational::cst::ParameterDeclarationCS_strategy)
def test_qvtoperational::cst::parameterdeclarationcs_directionKind_type(instance):
    assert isinstance(instance.directionKind, str)


@given(instance=qvtoperational::cst::ParameterDeclarationCS_strategy)
def test_qvtoperational::cst::parameterdeclarationcs_directionKind_setter(instance):
    original = instance.directionKind
    instance.directionKind = original
    assert instance.directionKind == original

@given(instance=MappingExtensionCS_strategy)
@settings(max_examples=50)
def test_mappingextensioncs_instantiation(instance):
    assert isinstance(instance, MappingExtensionCS)

@given(instance=DirectionKindCS_strategy)
@settings(max_examples=50)
def test_directionkindcs_instantiation(instance):
    assert isinstance(instance, DirectionKindCS)

@given(instance=ParameterDeclarationCS_strategy)
@settings(max_examples=50)
def test_parameterdeclarationcs_instantiation(instance):
    assert isinstance(instance, ParameterDeclarationCS)

@given(instance=qvtoperational::cst::MappingDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::mappingdeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MappingDeclarationCS)

@given(instance=qvtoperational::cst::MappingDeclarationCS_strategy)
def test_qvtoperational::cst::mappingdeclarationcs_isQuery_type(instance):
    assert isinstance(instance.isQuery, bool)


@given(instance=qvtoperational::cst::MappingDeclarationCS_strategy)
def test_qvtoperational::cst::mappingdeclarationcs_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original

@given(instance=qvtoperational::cst::MappingDeclarationCS_strategy)
def test_qvtoperational::cst::mappingdeclarationcs_qualifiers_type(instance):
    assert isinstance(instance.qualifiers, str)


@given(instance=qvtoperational::cst::MappingDeclarationCS_strategy)
def test_qvtoperational::cst::mappingdeclarationcs_qualifiers_setter(instance):
    original = instance.qualifiers
    instance.qualifiers = original
    assert instance.qualifiers == original

@given(instance=PrimitiveLiteralExpCS_strategy)
@settings(max_examples=50)
def test_primitiveliteralexpcs_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExpCS)

@given(instance=qvtoperational::cst::MultiplicityDefCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::multiplicitydefcs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::MultiplicityDefCS)

@given(instance=qvtoperational::cst::OppositePropertyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::oppositepropertycs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::OppositePropertyCS)

@given(instance=qvtoperational::cst::OppositePropertyCS_strategy)
def test_qvtoperational::cst::oppositepropertycs_isNavigable_type(instance):
    assert isinstance(instance.isNavigable, bool)


@given(instance=qvtoperational::cst::OppositePropertyCS_strategy)
def test_qvtoperational::cst::oppositepropertycs_isNavigable_setter(instance):
    original = instance.isNavigable
    instance.isNavigable = original
    assert instance.isNavigable == original

@given(instance=OppositePropertyCS_strategy)
@settings(max_examples=50)
def test_oppositepropertycs_instantiation(instance):
    assert isinstance(instance, OppositePropertyCS)

@given(instance=MultiplicityDefCS_strategy)
@settings(max_examples=50)
def test_multiplicitydefcs_instantiation(instance):
    assert isinstance(instance, MultiplicityDefCS)

@given(instance=LocalPropertyCS_strategy)
@settings(max_examples=50)
def test_localpropertycs_instantiation(instance):
    assert isinstance(instance, LocalPropertyCS)

@given(instance=qvtoperational::cst::ClassifierPropertyCS_strategy)
@settings(max_examples=50)
def test_qvtoperational::cst::classifierpropertycs_instantiation(instance):
    assert isinstance(instance, qvtoperational::cst::ClassifierPropertyCS)

@given(instance=qvtoperational::cst::ClassifierPropertyCS_strategy)
def test_qvtoperational::cst::classifierpropertycs_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, bool)


@given(instance=qvtoperational::cst::ClassifierPropertyCS_strategy)
def test_qvtoperational::cst::classifierpropertycs_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=RenameCS_strategy)
@settings(max_examples=50)
def test_renamecs_instantiation(instance):
    assert isinstance(instance, RenameCS)
