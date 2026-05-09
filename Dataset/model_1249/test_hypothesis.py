import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Documentation,
    mtl::ModuleElementDocumentation,
    mtl::ModuleDocumentation,
    mtl::DocumentedElement,
    Comment,
    mtl::ParameterDocumentation,
    mtl::Documentation,
    mtl::CommentBody,
    mtl::EPackage,
    ModuleElement,
    mtl::Comment,
    Block,
    mtl::LetBlock,
    mtl::TraceBlock,
    mtl::IfBlock,
    mtl::FileBlock,
    mtl::ForBlock,
    mtl::ProtectedAreaBlock,
    mtl::EClassifier,
    EPackage,
    Variable,
    ASTNode,
    mtl::InitSection,
    TemplateExpression,
    mtl::QueryInvocation,
    mtl::MacroInvocation,
    mtl::TemplateInvocation,
    mtl::Block,
    OCLExpression,
    mtl::TemplateExpression,
    utilities::ASTNode,
    ENamedElement,
    mtl::ModuleElement,
    mtl::TypedModel,
    DocumentedElement,
    mtl::Template,
    mtl::Query,
    mtl::Module,
    mtl::Macro,
    OpenModeKind,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_documentation_is_not_abstract():
    assert not inspect.isabstract(Documentation)


def test_documentation_constructor_exists():
    assert callable(Documentation.__init__)


def test_documentation_constructor_args():
    sig = inspect.signature(Documentation.__init__)
    params = list(sig.parameters.keys())



def test_mtl::moduleelementdocumentation_is_not_abstract():
    assert not inspect.isabstract(mtl::ModuleElementDocumentation)


def test_mtl::moduleelementdocumentation_constructor_exists():
    assert callable(mtl::ModuleElementDocumentation.__init__)


def test_mtl::moduleelementdocumentation_constructor_args():
    sig = inspect.signature(mtl::ModuleElementDocumentation.__init__)
    params = list(sig.parameters.keys())



def test_mtl::moduledocumentation_is_not_abstract():
    assert not inspect.isabstract(mtl::ModuleDocumentation)


def test_mtl::moduledocumentation_constructor_exists():
    assert callable(mtl::ModuleDocumentation.__init__)


def test_mtl::moduledocumentation_constructor_args():
    sig = inspect.signature(mtl::ModuleDocumentation.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "version" in params, "Missing parameter 'version'"
    assert "since" in params, "Missing parameter 'since'"

def test_mtl::moduledocumentation_has_author():
    assert hasattr(mtl::ModuleDocumentation, "author")
    descriptor = None
    for klass in mtl::ModuleDocumentation.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_mtl::moduledocumentation_has_version():
    assert hasattr(mtl::ModuleDocumentation, "version")
    descriptor = None
    for klass in mtl::ModuleDocumentation.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_mtl::moduledocumentation_has_since():
    assert hasattr(mtl::ModuleDocumentation, "since")
    descriptor = None
    for klass in mtl::ModuleDocumentation.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_mtl::documentedelement_is_not_abstract():
    assert not inspect.isabstract(mtl::DocumentedElement)


def test_mtl::documentedelement_constructor_exists():
    assert callable(mtl::DocumentedElement.__init__)


def test_mtl::documentedelement_constructor_args():
    sig = inspect.signature(mtl::DocumentedElement.__init__)
    params = list(sig.parameters.keys())
    assert "deprecated" in params, "Missing parameter 'deprecated'"

def test_mtl::documentedelement_has_deprecated():
    assert hasattr(mtl::DocumentedElement, "deprecated")
    descriptor = None
    for klass in mtl::DocumentedElement.__mro__:
        if "deprecated" in klass.__dict__:
            descriptor = klass.__dict__["deprecated"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_mtl::parameterdocumentation_is_not_abstract():
    assert not inspect.isabstract(mtl::ParameterDocumentation)


def test_mtl::parameterdocumentation_constructor_exists():
    assert callable(mtl::ParameterDocumentation.__init__)


def test_mtl::parameterdocumentation_constructor_args():
    sig = inspect.signature(mtl::ParameterDocumentation.__init__)
    params = list(sig.parameters.keys())



def test_mtl::documentation_is_not_abstract():
    assert not inspect.isabstract(mtl::Documentation)


def test_mtl::documentation_constructor_exists():
    assert callable(mtl::Documentation.__init__)


def test_mtl::documentation_constructor_args():
    sig = inspect.signature(mtl::Documentation.__init__)
    params = list(sig.parameters.keys())



def test_mtl::commentbody_is_not_abstract():
    assert not inspect.isabstract(mtl::CommentBody)


def test_mtl::commentbody_constructor_exists():
    assert callable(mtl::CommentBody.__init__)


def test_mtl::commentbody_constructor_args():
    sig = inspect.signature(mtl::CommentBody.__init__)
    params = list(sig.parameters.keys())
    assert "startPosition" in params, "Missing parameter 'startPosition'"
    assert "value" in params, "Missing parameter 'value'"
    assert "endPosition" in params, "Missing parameter 'endPosition'"

def test_mtl::commentbody_has_startPosition():
    assert hasattr(mtl::CommentBody, "startPosition")
    descriptor = None
    for klass in mtl::CommentBody.__mro__:
        if "startPosition" in klass.__dict__:
            descriptor = klass.__dict__["startPosition"]
            break
    assert isinstance(descriptor, property)

def test_mtl::commentbody_has_value():
    assert hasattr(mtl::CommentBody, "value")
    descriptor = None
    for klass in mtl::CommentBody.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mtl::commentbody_has_endPosition():
    assert hasattr(mtl::CommentBody, "endPosition")
    descriptor = None
    for klass in mtl::CommentBody.__mro__:
        if "endPosition" in klass.__dict__:
            descriptor = klass.__dict__["endPosition"]
            break
    assert isinstance(descriptor, property)



def test_mtl::epackage_is_not_abstract():
    assert not inspect.isabstract(mtl::EPackage)


def test_mtl::epackage_constructor_exists():
    assert callable(mtl::EPackage.__init__)


def test_mtl::epackage_constructor_args():
    sig = inspect.signature(mtl::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_mtl::comment_is_not_abstract():
    assert not inspect.isabstract(mtl::Comment)


def test_mtl::comment_constructor_exists():
    assert callable(mtl::Comment.__init__)


def test_mtl::comment_constructor_args():
    sig = inspect.signature(mtl::Comment.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_mtl::letblock_is_not_abstract():
    assert not inspect.isabstract(mtl::LetBlock)


def test_mtl::letblock_constructor_exists():
    assert callable(mtl::LetBlock.__init__)


def test_mtl::letblock_constructor_args():
    sig = inspect.signature(mtl::LetBlock.__init__)
    params = list(sig.parameters.keys())



def test_mtl::traceblock_is_not_abstract():
    assert not inspect.isabstract(mtl::TraceBlock)


def test_mtl::traceblock_constructor_exists():
    assert callable(mtl::TraceBlock.__init__)


def test_mtl::traceblock_constructor_args():
    sig = inspect.signature(mtl::TraceBlock.__init__)
    params = list(sig.parameters.keys())



def test_mtl::ifblock_is_not_abstract():
    assert not inspect.isabstract(mtl::IfBlock)


def test_mtl::ifblock_constructor_exists():
    assert callable(mtl::IfBlock.__init__)


def test_mtl::ifblock_constructor_args():
    sig = inspect.signature(mtl::IfBlock.__init__)
    params = list(sig.parameters.keys())



def test_mtl::fileblock_is_not_abstract():
    assert not inspect.isabstract(mtl::FileBlock)


def test_mtl::fileblock_constructor_exists():
    assert callable(mtl::FileBlock.__init__)


def test_mtl::fileblock_constructor_args():
    sig = inspect.signature(mtl::FileBlock.__init__)
    params = list(sig.parameters.keys())
    assert "openMode" in params, "Missing parameter 'openMode'"

def test_mtl::fileblock_has_openMode():
    assert hasattr(mtl::FileBlock, "openMode")
    descriptor = None
    for klass in mtl::FileBlock.__mro__:
        if "openMode" in klass.__dict__:
            descriptor = klass.__dict__["openMode"]
            break
    assert isinstance(descriptor, property)



def test_mtl::forblock_is_not_abstract():
    assert not inspect.isabstract(mtl::ForBlock)


def test_mtl::forblock_constructor_exists():
    assert callable(mtl::ForBlock.__init__)


def test_mtl::forblock_constructor_args():
    sig = inspect.signature(mtl::ForBlock.__init__)
    params = list(sig.parameters.keys())



def test_mtl::protectedareablock_is_not_abstract():
    assert not inspect.isabstract(mtl::ProtectedAreaBlock)


def test_mtl::protectedareablock_constructor_exists():
    assert callable(mtl::ProtectedAreaBlock.__init__)


def test_mtl::protectedareablock_constructor_args():
    sig = inspect.signature(mtl::ProtectedAreaBlock.__init__)
    params = list(sig.parameters.keys())



def test_mtl::eclassifier_is_not_abstract():
    assert not inspect.isabstract(mtl::EClassifier)


def test_mtl::eclassifier_constructor_exists():
    assert callable(mtl::EClassifier.__init__)


def test_mtl::eclassifier_constructor_args():
    sig = inspect.signature(mtl::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_epackage_is_not_abstract():
    assert not inspect.isabstract(EPackage)


def test_epackage_constructor_exists():
    assert callable(EPackage.__init__)


def test_epackage_constructor_args():
    sig = inspect.signature(EPackage.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_mtl::initsection_is_not_abstract():
    assert not inspect.isabstract(mtl::InitSection)


def test_mtl::initsection_constructor_exists():
    assert callable(mtl::InitSection.__init__)


def test_mtl::initsection_constructor_args():
    sig = inspect.signature(mtl::InitSection.__init__)
    params = list(sig.parameters.keys())



def test_templateexpression_is_not_abstract():
    assert not inspect.isabstract(TemplateExpression)


def test_templateexpression_constructor_exists():
    assert callable(TemplateExpression.__init__)


def test_templateexpression_constructor_args():
    sig = inspect.signature(TemplateExpression.__init__)
    params = list(sig.parameters.keys())



def test_mtl::queryinvocation_is_not_abstract():
    assert not inspect.isabstract(mtl::QueryInvocation)


def test_mtl::queryinvocation_constructor_exists():
    assert callable(mtl::QueryInvocation.__init__)


def test_mtl::queryinvocation_constructor_args():
    sig = inspect.signature(mtl::QueryInvocation.__init__)
    params = list(sig.parameters.keys())



def test_mtl::macroinvocation_is_not_abstract():
    assert not inspect.isabstract(mtl::MacroInvocation)


def test_mtl::macroinvocation_constructor_exists():
    assert callable(mtl::MacroInvocation.__init__)


def test_mtl::macroinvocation_constructor_args():
    sig = inspect.signature(mtl::MacroInvocation.__init__)
    params = list(sig.parameters.keys())



def test_mtl::templateinvocation_is_not_abstract():
    assert not inspect.isabstract(mtl::TemplateInvocation)


def test_mtl::templateinvocation_constructor_exists():
    assert callable(mtl::TemplateInvocation.__init__)


def test_mtl::templateinvocation_constructor_args():
    sig = inspect.signature(mtl::TemplateInvocation.__init__)
    params = list(sig.parameters.keys())
    assert "super" in params, "Missing parameter 'super'"

def test_mtl::templateinvocation_has_super():
    assert hasattr(mtl::TemplateInvocation, "super")
    descriptor = None
    for klass in mtl::TemplateInvocation.__mro__:
        if "super" in klass.__dict__:
            descriptor = klass.__dict__["super"]
            break
    assert isinstance(descriptor, property)



def test_mtl::block_is_not_abstract():
    assert not inspect.isabstract(mtl::Block)


def test_mtl::block_constructor_exists():
    assert callable(mtl::Block.__init__)


def test_mtl::block_constructor_args():
    sig = inspect.signature(mtl::Block.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCLExpression)


def test_oclexpression_constructor_exists():
    assert callable(OCLExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_mtl::templateexpression_is_not_abstract():
    assert not inspect.isabstract(mtl::TemplateExpression)


def test_mtl::templateexpression_constructor_exists():
    assert callable(mtl::TemplateExpression.__init__)


def test_mtl::templateexpression_constructor_args():
    sig = inspect.signature(mtl::TemplateExpression.__init__)
    params = list(sig.parameters.keys())



def test_utilities::astnode_is_not_abstract():
    assert not inspect.isabstract(utilities::ASTNode)


def test_utilities::astnode_constructor_exists():
    assert callable(utilities::ASTNode.__init__)


def test_utilities::astnode_constructor_args():
    sig = inspect.signature(utilities::ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_mtl::moduleelement_is_not_abstract():
    assert not inspect.isabstract(mtl::ModuleElement)


def test_mtl::moduleelement_constructor_exists():
    assert callable(mtl::ModuleElement.__init__)


def test_mtl::moduleelement_constructor_args():
    sig = inspect.signature(mtl::ModuleElement.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_mtl::moduleelement_has_visibility():
    assert hasattr(mtl::ModuleElement, "visibility")
    descriptor = None
    for klass in mtl::ModuleElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_mtl::typedmodel_is_not_abstract():
    assert not inspect.isabstract(mtl::TypedModel)


def test_mtl::typedmodel_constructor_exists():
    assert callable(mtl::TypedModel.__init__)


def test_mtl::typedmodel_constructor_args():
    sig = inspect.signature(mtl::TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_documentedelement_is_not_abstract():
    assert not inspect.isabstract(DocumentedElement)


def test_documentedelement_constructor_exists():
    assert callable(DocumentedElement.__init__)


def test_documentedelement_constructor_args():
    sig = inspect.signature(DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_mtl::template_is_not_abstract():
    assert not inspect.isabstract(mtl::Template)


def test_mtl::template_constructor_exists():
    assert callable(mtl::Template.__init__)


def test_mtl::template_constructor_args():
    sig = inspect.signature(mtl::Template.__init__)
    params = list(sig.parameters.keys())
    assert "main" in params, "Missing parameter 'main'"

def test_mtl::template_has_main():
    assert hasattr(mtl::Template, "main")
    descriptor = None
    for klass in mtl::Template.__mro__:
        if "main" in klass.__dict__:
            descriptor = klass.__dict__["main"]
            break
    assert isinstance(descriptor, property)



def test_mtl::query_is_not_abstract():
    assert not inspect.isabstract(mtl::Query)


def test_mtl::query_constructor_exists():
    assert callable(mtl::Query.__init__)


def test_mtl::query_constructor_args():
    sig = inspect.signature(mtl::Query.__init__)
    params = list(sig.parameters.keys())



def test_mtl::module_is_not_abstract():
    assert not inspect.isabstract(mtl::Module)


def test_mtl::module_constructor_exists():
    assert callable(mtl::Module.__init__)


def test_mtl::module_constructor_args():
    sig = inspect.signature(mtl::Module.__init__)
    params = list(sig.parameters.keys())
    assert "startHeaderPosition" in params, "Missing parameter 'startHeaderPosition'"
    assert "endHeaderPosition" in params, "Missing parameter 'endHeaderPosition'"

def test_mtl::module_has_startHeaderPosition():
    assert hasattr(mtl::Module, "startHeaderPosition")
    descriptor = None
    for klass in mtl::Module.__mro__:
        if "startHeaderPosition" in klass.__dict__:
            descriptor = klass.__dict__["startHeaderPosition"]
            break
    assert isinstance(descriptor, property)

def test_mtl::module_has_endHeaderPosition():
    assert hasattr(mtl::Module, "endHeaderPosition")
    descriptor = None
    for klass in mtl::Module.__mro__:
        if "endHeaderPosition" in klass.__dict__:
            descriptor = klass.__dict__["endHeaderPosition"]
            break
    assert isinstance(descriptor, property)



def test_mtl::macro_is_not_abstract():
    assert not inspect.isabstract(mtl::Macro)


def test_mtl::macro_constructor_exists():
    assert callable(mtl::Macro.__init__)


def test_mtl::macro_constructor_args():
    sig = inspect.signature(mtl::Macro.__init__)
    params = list(sig.parameters.keys())

def test_openmodekind_exists():
    # Check that the Enumeration exists
    assert OpenModeKind is not None

def test_openmodekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OpenModeKind]
    expected_literals = [
        "Append",
        "OverWrite",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OpenModeKind"

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "Private",
        "Protected",
        "Public",
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
Documentation_strategy = st.builds(
    Documentation,
)
mtl::ModuleElementDocumentation_strategy = st.builds(
    mtl::ModuleElementDocumentation,
)
mtl::ModuleDocumentation_strategy = st.builds(
    mtl::ModuleDocumentation,
    author=
        safe_text,
    version=
        safe_text,
    since=
        safe_text
)
mtl::DocumentedElement_strategy = st.builds(
    mtl::DocumentedElement,
    deprecated=
        st.booleans()
)
Comment_strategy = st.builds(
    Comment,
)
mtl::ParameterDocumentation_strategy = st.builds(
    mtl::ParameterDocumentation,
)
mtl::Documentation_strategy = st.builds(
    mtl::Documentation,
)
mtl::CommentBody_strategy = st.builds(
    mtl::CommentBody,
    startPosition=
        st.integers(),
    value=
        safe_text,
    endPosition=
        st.integers()
)
mtl::EPackage_strategy = st.builds(
    mtl::EPackage,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
mtl::Comment_strategy = st.builds(
    mtl::Comment,
)
Block_strategy = st.builds(
    Block,
)
mtl::LetBlock_strategy = st.builds(
    mtl::LetBlock,
)
mtl::TraceBlock_strategy = st.builds(
    mtl::TraceBlock,
)
mtl::IfBlock_strategy = st.builds(
    mtl::IfBlock,
)
mtl::FileBlock_strategy = st.builds(
    mtl::FileBlock,
    openMode=
        safe_text
)
mtl::ForBlock_strategy = st.builds(
    mtl::ForBlock,
)
mtl::ProtectedAreaBlock_strategy = st.builds(
    mtl::ProtectedAreaBlock,
)
mtl::EClassifier_strategy = st.builds(
    mtl::EClassifier,
)
EPackage_strategy = st.builds(
    EPackage,
)
Variable_strategy = st.builds(
    Variable,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
mtl::InitSection_strategy = st.builds(
    mtl::InitSection,
)
TemplateExpression_strategy = st.builds(
    TemplateExpression,
)
mtl::QueryInvocation_strategy = st.builds(
    mtl::QueryInvocation,
)
mtl::MacroInvocation_strategy = st.builds(
    mtl::MacroInvocation,
)
mtl::TemplateInvocation_strategy = st.builds(
    mtl::TemplateInvocation,
    super=
        st.booleans()
)
mtl::Block_strategy = st.builds(
    mtl::Block,
)
OCLExpression_strategy = st.builds(
    OCLExpression,
)
mtl::TemplateExpression_strategy = st.builds(
    mtl::TemplateExpression,
)
utilities::ASTNode_strategy = st.builds(
    utilities::ASTNode,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
mtl::ModuleElement_strategy = st.builds(
    mtl::ModuleElement,
    visibility=
        safe_text
)
mtl::TypedModel_strategy = st.builds(
    mtl::TypedModel,
)
DocumentedElement_strategy = st.builds(
    DocumentedElement,
)
mtl::Template_strategy = st.builds(
    mtl::Template,
    main=
        st.booleans()
)
mtl::Query_strategy = st.builds(
    mtl::Query,
)
mtl::Module_strategy = st.builds(
    mtl::Module,
    startHeaderPosition=
        st.integers(),
    endHeaderPosition=
        st.integers()
)
mtl::Macro_strategy = st.builds(
    mtl::Macro,
)

@given(instance=Documentation_strategy)
@settings(max_examples=50)
def test_documentation_instantiation(instance):
    assert isinstance(instance, Documentation)

@given(instance=mtl::ModuleElementDocumentation_strategy)
@settings(max_examples=50)
def test_mtl::moduleelementdocumentation_instantiation(instance):
    assert isinstance(instance, mtl::ModuleElementDocumentation)

@given(instance=mtl::ModuleDocumentation_strategy)
@settings(max_examples=50)
def test_mtl::moduledocumentation_instantiation(instance):
    assert isinstance(instance, mtl::ModuleDocumentation)

@given(instance=mtl::ModuleDocumentation_strategy)
def test_mtl::moduledocumentation_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=mtl::ModuleDocumentation_strategy)
def test_mtl::moduledocumentation_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=mtl::ModuleDocumentation_strategy)
def test_mtl::moduledocumentation_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=mtl::ModuleDocumentation_strategy)
def test_mtl::moduledocumentation_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=mtl::ModuleDocumentation_strategy)
def test_mtl::moduledocumentation_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=mtl::ModuleDocumentation_strategy)
def test_mtl::moduledocumentation_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=mtl::DocumentedElement_strategy)
@settings(max_examples=50)
def test_mtl::documentedelement_instantiation(instance):
    assert isinstance(instance, mtl::DocumentedElement)

@given(instance=mtl::DocumentedElement_strategy)
def test_mtl::documentedelement_deprecated_type(instance):
    assert isinstance(instance.deprecated, bool)


@given(instance=mtl::DocumentedElement_strategy)
def test_mtl::documentedelement_deprecated_setter(instance):
    original = instance.deprecated
    instance.deprecated = original
    assert instance.deprecated == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=mtl::ParameterDocumentation_strategy)
@settings(max_examples=50)
def test_mtl::parameterdocumentation_instantiation(instance):
    assert isinstance(instance, mtl::ParameterDocumentation)

@given(instance=mtl::Documentation_strategy)
@settings(max_examples=50)
def test_mtl::documentation_instantiation(instance):
    assert isinstance(instance, mtl::Documentation)

@given(instance=mtl::CommentBody_strategy)
@settings(max_examples=50)
def test_mtl::commentbody_instantiation(instance):
    assert isinstance(instance, mtl::CommentBody)

@given(instance=mtl::CommentBody_strategy)
def test_mtl::commentbody_startPosition_type(instance):
    assert isinstance(instance.startPosition, int)


@given(instance=mtl::CommentBody_strategy)
def test_mtl::commentbody_startPosition_setter(instance):
    original = instance.startPosition
    instance.startPosition = original
    assert instance.startPosition == original

@given(instance=mtl::CommentBody_strategy)
def test_mtl::commentbody_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mtl::CommentBody_strategy)
def test_mtl::commentbody_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mtl::CommentBody_strategy)
def test_mtl::commentbody_endPosition_type(instance):
    assert isinstance(instance.endPosition, int)


@given(instance=mtl::CommentBody_strategy)
def test_mtl::commentbody_endPosition_setter(instance):
    original = instance.endPosition
    instance.endPosition = original
    assert instance.endPosition == original

@given(instance=mtl::EPackage_strategy)
@settings(max_examples=50)
def test_mtl::epackage_instantiation(instance):
    assert isinstance(instance, mtl::EPackage)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=mtl::Comment_strategy)
@settings(max_examples=50)
def test_mtl::comment_instantiation(instance):
    assert isinstance(instance, mtl::Comment)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=mtl::LetBlock_strategy)
@settings(max_examples=50)
def test_mtl::letblock_instantiation(instance):
    assert isinstance(instance, mtl::LetBlock)

@given(instance=mtl::TraceBlock_strategy)
@settings(max_examples=50)
def test_mtl::traceblock_instantiation(instance):
    assert isinstance(instance, mtl::TraceBlock)

@given(instance=mtl::IfBlock_strategy)
@settings(max_examples=50)
def test_mtl::ifblock_instantiation(instance):
    assert isinstance(instance, mtl::IfBlock)

@given(instance=mtl::FileBlock_strategy)
@settings(max_examples=50)
def test_mtl::fileblock_instantiation(instance):
    assert isinstance(instance, mtl::FileBlock)

@given(instance=mtl::FileBlock_strategy)
def test_mtl::fileblock_openMode_type(instance):
    assert isinstance(instance.openMode, str)


@given(instance=mtl::FileBlock_strategy)
def test_mtl::fileblock_openMode_setter(instance):
    original = instance.openMode
    instance.openMode = original
    assert instance.openMode == original

@given(instance=mtl::ForBlock_strategy)
@settings(max_examples=50)
def test_mtl::forblock_instantiation(instance):
    assert isinstance(instance, mtl::ForBlock)

@given(instance=mtl::ProtectedAreaBlock_strategy)
@settings(max_examples=50)
def test_mtl::protectedareablock_instantiation(instance):
    assert isinstance(instance, mtl::ProtectedAreaBlock)

@given(instance=mtl::EClassifier_strategy)
@settings(max_examples=50)
def test_mtl::eclassifier_instantiation(instance):
    assert isinstance(instance, mtl::EClassifier)

@given(instance=EPackage_strategy)
@settings(max_examples=50)
def test_epackage_instantiation(instance):
    assert isinstance(instance, EPackage)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=mtl::InitSection_strategy)
@settings(max_examples=50)
def test_mtl::initsection_instantiation(instance):
    assert isinstance(instance, mtl::InitSection)

@given(instance=TemplateExpression_strategy)
@settings(max_examples=50)
def test_templateexpression_instantiation(instance):
    assert isinstance(instance, TemplateExpression)

@given(instance=mtl::QueryInvocation_strategy)
@settings(max_examples=50)
def test_mtl::queryinvocation_instantiation(instance):
    assert isinstance(instance, mtl::QueryInvocation)

@given(instance=mtl::MacroInvocation_strategy)
@settings(max_examples=50)
def test_mtl::macroinvocation_instantiation(instance):
    assert isinstance(instance, mtl::MacroInvocation)

@given(instance=mtl::TemplateInvocation_strategy)
@settings(max_examples=50)
def test_mtl::templateinvocation_instantiation(instance):
    assert isinstance(instance, mtl::TemplateInvocation)

@given(instance=mtl::TemplateInvocation_strategy)
def test_mtl::templateinvocation_super_type(instance):
    assert isinstance(instance.super, bool)


@given(instance=mtl::TemplateInvocation_strategy)
def test_mtl::templateinvocation_super_setter(instance):
    original = instance.super
    instance.super = original
    assert instance.super == original

@given(instance=mtl::Block_strategy)
@settings(max_examples=50)
def test_mtl::block_instantiation(instance):
    assert isinstance(instance, mtl::Block)

@given(instance=OCLExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OCLExpression)

@given(instance=mtl::TemplateExpression_strategy)
@settings(max_examples=50)
def test_mtl::templateexpression_instantiation(instance):
    assert isinstance(instance, mtl::TemplateExpression)

@given(instance=utilities::ASTNode_strategy)
@settings(max_examples=50)
def test_utilities::astnode_instantiation(instance):
    assert isinstance(instance, utilities::ASTNode)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=mtl::ModuleElement_strategy)
@settings(max_examples=50)
def test_mtl::moduleelement_instantiation(instance):
    assert isinstance(instance, mtl::ModuleElement)

@given(instance=mtl::ModuleElement_strategy)
def test_mtl::moduleelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=mtl::ModuleElement_strategy)
def test_mtl::moduleelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=mtl::TypedModel_strategy)
@settings(max_examples=50)
def test_mtl::typedmodel_instantiation(instance):
    assert isinstance(instance, mtl::TypedModel)

@given(instance=DocumentedElement_strategy)
@settings(max_examples=50)
def test_documentedelement_instantiation(instance):
    assert isinstance(instance, DocumentedElement)

@given(instance=mtl::Template_strategy)
@settings(max_examples=50)
def test_mtl::template_instantiation(instance):
    assert isinstance(instance, mtl::Template)

@given(instance=mtl::Template_strategy)
def test_mtl::template_main_type(instance):
    assert isinstance(instance.main, bool)


@given(instance=mtl::Template_strategy)
def test_mtl::template_main_setter(instance):
    original = instance.main
    instance.main = original
    assert instance.main == original

@given(instance=mtl::Query_strategy)
@settings(max_examples=50)
def test_mtl::query_instantiation(instance):
    assert isinstance(instance, mtl::Query)

@given(instance=mtl::Module_strategy)
@settings(max_examples=50)
def test_mtl::module_instantiation(instance):
    assert isinstance(instance, mtl::Module)

@given(instance=mtl::Module_strategy)
def test_mtl::module_startHeaderPosition_type(instance):
    assert isinstance(instance.startHeaderPosition, int)


@given(instance=mtl::Module_strategy)
def test_mtl::module_startHeaderPosition_setter(instance):
    original = instance.startHeaderPosition
    instance.startHeaderPosition = original
    assert instance.startHeaderPosition == original

@given(instance=mtl::Module_strategy)
def test_mtl::module_endHeaderPosition_type(instance):
    assert isinstance(instance.endHeaderPosition, int)


@given(instance=mtl::Module_strategy)
def test_mtl::module_endHeaderPosition_setter(instance):
    original = instance.endHeaderPosition
    instance.endHeaderPosition = original
    assert instance.endHeaderPosition == original

@given(instance=mtl::Macro_strategy)
@settings(max_examples=50)
def test_mtl::macro_instantiation(instance):
    assert isinstance(instance, mtl::Macro)
