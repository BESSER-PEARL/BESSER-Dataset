import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Documentation,
    mtl_ModuleElementDocumentation,
    mtl_ModuleDocumentation,
    mtl_DocumentedElement,
    Comment,
    mtl_ParameterDocumentation,
    mtl_Documentation,
    mtl_CommentBody,
    mtl_EPackage,
    ModuleElement,
    mtl_Comment,
    Block,
    mtl_LetBlock,
    mtl_FileBlock,
    mtl_TraceBlock,
    mtl_IfBlock,
    mtl_ForBlock,
    mtl_ProtectedAreaBlock,
    mtl_EClassifier,
    EPackage,
    Variable,
    ASTNode,
    mtl_InitSection,
    TemplateExpression,
    mtl_TemplateInvocation,
    mtl_MacroInvocation,
    mtl_QueryInvocation,
    mtl_Block,
    OCLExpression,
    mtl_TemplateExpression,
    utilities_ASTNode,
    ENamedElement,
    mtl_ModuleElement,
    mtl_TypedModel,
    DocumentedElement,
    mtl_Template,
    mtl_Query,
    mtl_Macro,
    mtl_Module,
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



def test_mtl_moduleelementdocumentation_is_not_abstract():
    assert not inspect.isabstract(mtl_ModuleElementDocumentation)


def test_mtl_moduleelementdocumentation_constructor_exists():
    assert callable(mtl_ModuleElementDocumentation.__init__)


def test_mtl_moduleelementdocumentation_constructor_args():
    sig = inspect.signature(mtl_ModuleElementDocumentation.__init__)
    params = list(sig.parameters.keys())



def test_mtl_moduledocumentation_is_not_abstract():
    assert not inspect.isabstract(mtl_ModuleDocumentation)


def test_mtl_moduledocumentation_constructor_exists():
    assert callable(mtl_ModuleDocumentation.__init__)


def test_mtl_moduledocumentation_constructor_args():
    sig = inspect.signature(mtl_ModuleDocumentation.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "version" in params, "Missing parameter 'version'"
    assert "since" in params, "Missing parameter 'since'"

def test_mtl_moduledocumentation_has_author():
    assert hasattr(mtl_ModuleDocumentation, "author")
    descriptor = None
    for klass in mtl_ModuleDocumentation.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_mtl_moduledocumentation_has_version():
    assert hasattr(mtl_ModuleDocumentation, "version")
    descriptor = None
    for klass in mtl_ModuleDocumentation.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_mtl_moduledocumentation_has_since():
    assert hasattr(mtl_ModuleDocumentation, "since")
    descriptor = None
    for klass in mtl_ModuleDocumentation.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_mtl_documentedelement_is_not_abstract():
    assert not inspect.isabstract(mtl_DocumentedElement)


def test_mtl_documentedelement_constructor_exists():
    assert callable(mtl_DocumentedElement.__init__)


def test_mtl_documentedelement_constructor_args():
    sig = inspect.signature(mtl_DocumentedElement.__init__)
    params = list(sig.parameters.keys())
    assert "deprecated" in params, "Missing parameter 'deprecated'"

def test_mtl_documentedelement_has_deprecated():
    assert hasattr(mtl_DocumentedElement, "deprecated")
    descriptor = None
    for klass in mtl_DocumentedElement.__mro__:
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



def test_mtl_parameterdocumentation_is_not_abstract():
    assert not inspect.isabstract(mtl_ParameterDocumentation)


def test_mtl_parameterdocumentation_constructor_exists():
    assert callable(mtl_ParameterDocumentation.__init__)


def test_mtl_parameterdocumentation_constructor_args():
    sig = inspect.signature(mtl_ParameterDocumentation.__init__)
    params = list(sig.parameters.keys())



def test_mtl_documentation_is_not_abstract():
    assert not inspect.isabstract(mtl_Documentation)


def test_mtl_documentation_constructor_exists():
    assert callable(mtl_Documentation.__init__)


def test_mtl_documentation_constructor_args():
    sig = inspect.signature(mtl_Documentation.__init__)
    params = list(sig.parameters.keys())



def test_mtl_commentbody_is_not_abstract():
    assert not inspect.isabstract(mtl_CommentBody)


def test_mtl_commentbody_constructor_exists():
    assert callable(mtl_CommentBody.__init__)


def test_mtl_commentbody_constructor_args():
    sig = inspect.signature(mtl_CommentBody.__init__)
    params = list(sig.parameters.keys())
    assert "startPosition" in params, "Missing parameter 'startPosition'"
    assert "endPosition" in params, "Missing parameter 'endPosition'"
    assert "value" in params, "Missing parameter 'value'"

def test_mtl_commentbody_has_startPosition():
    assert hasattr(mtl_CommentBody, "startPosition")
    descriptor = None
    for klass in mtl_CommentBody.__mro__:
        if "startPosition" in klass.__dict__:
            descriptor = klass.__dict__["startPosition"]
            break
    assert isinstance(descriptor, property)

def test_mtl_commentbody_has_endPosition():
    assert hasattr(mtl_CommentBody, "endPosition")
    descriptor = None
    for klass in mtl_CommentBody.__mro__:
        if "endPosition" in klass.__dict__:
            descriptor = klass.__dict__["endPosition"]
            break
    assert isinstance(descriptor, property)

def test_mtl_commentbody_has_value():
    assert hasattr(mtl_CommentBody, "value")
    descriptor = None
    for klass in mtl_CommentBody.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mtl_epackage_is_not_abstract():
    assert not inspect.isabstract(mtl_EPackage)


def test_mtl_epackage_constructor_exists():
    assert callable(mtl_EPackage.__init__)


def test_mtl_epackage_constructor_args():
    sig = inspect.signature(mtl_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_mtl_comment_is_not_abstract():
    assert not inspect.isabstract(mtl_Comment)


def test_mtl_comment_constructor_exists():
    assert callable(mtl_Comment.__init__)


def test_mtl_comment_constructor_args():
    sig = inspect.signature(mtl_Comment.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_mtl_letblock_is_not_abstract():
    assert not inspect.isabstract(mtl_LetBlock)


def test_mtl_letblock_constructor_exists():
    assert callable(mtl_LetBlock.__init__)


def test_mtl_letblock_constructor_args():
    sig = inspect.signature(mtl_LetBlock.__init__)
    params = list(sig.parameters.keys())



def test_mtl_fileblock_is_not_abstract():
    assert not inspect.isabstract(mtl_FileBlock)


def test_mtl_fileblock_constructor_exists():
    assert callable(mtl_FileBlock.__init__)


def test_mtl_fileblock_constructor_args():
    sig = inspect.signature(mtl_FileBlock.__init__)
    params = list(sig.parameters.keys())
    assert "openMode" in params, "Missing parameter 'openMode'"

def test_mtl_fileblock_has_openMode():
    assert hasattr(mtl_FileBlock, "openMode")
    descriptor = None
    for klass in mtl_FileBlock.__mro__:
        if "openMode" in klass.__dict__:
            descriptor = klass.__dict__["openMode"]
            break
    assert isinstance(descriptor, property)



def test_mtl_traceblock_is_not_abstract():
    assert not inspect.isabstract(mtl_TraceBlock)


def test_mtl_traceblock_constructor_exists():
    assert callable(mtl_TraceBlock.__init__)


def test_mtl_traceblock_constructor_args():
    sig = inspect.signature(mtl_TraceBlock.__init__)
    params = list(sig.parameters.keys())



def test_mtl_ifblock_is_not_abstract():
    assert not inspect.isabstract(mtl_IfBlock)


def test_mtl_ifblock_constructor_exists():
    assert callable(mtl_IfBlock.__init__)


def test_mtl_ifblock_constructor_args():
    sig = inspect.signature(mtl_IfBlock.__init__)
    params = list(sig.parameters.keys())



def test_mtl_forblock_is_not_abstract():
    assert not inspect.isabstract(mtl_ForBlock)


def test_mtl_forblock_constructor_exists():
    assert callable(mtl_ForBlock.__init__)


def test_mtl_forblock_constructor_args():
    sig = inspect.signature(mtl_ForBlock.__init__)
    params = list(sig.parameters.keys())



def test_mtl_protectedareablock_is_not_abstract():
    assert not inspect.isabstract(mtl_ProtectedAreaBlock)


def test_mtl_protectedareablock_constructor_exists():
    assert callable(mtl_ProtectedAreaBlock.__init__)


def test_mtl_protectedareablock_constructor_args():
    sig = inspect.signature(mtl_ProtectedAreaBlock.__init__)
    params = list(sig.parameters.keys())



def test_mtl_eclassifier_is_not_abstract():
    assert not inspect.isabstract(mtl_EClassifier)


def test_mtl_eclassifier_constructor_exists():
    assert callable(mtl_EClassifier.__init__)


def test_mtl_eclassifier_constructor_args():
    sig = inspect.signature(mtl_EClassifier.__init__)
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



def test_mtl_initsection_is_not_abstract():
    assert not inspect.isabstract(mtl_InitSection)


def test_mtl_initsection_constructor_exists():
    assert callable(mtl_InitSection.__init__)


def test_mtl_initsection_constructor_args():
    sig = inspect.signature(mtl_InitSection.__init__)
    params = list(sig.parameters.keys())



def test_templateexpression_is_not_abstract():
    assert not inspect.isabstract(TemplateExpression)


def test_templateexpression_constructor_exists():
    assert callable(TemplateExpression.__init__)


def test_templateexpression_constructor_args():
    sig = inspect.signature(TemplateExpression.__init__)
    params = list(sig.parameters.keys())



def test_mtl_templateinvocation_is_not_abstract():
    assert not inspect.isabstract(mtl_TemplateInvocation)


def test_mtl_templateinvocation_constructor_exists():
    assert callable(mtl_TemplateInvocation.__init__)


def test_mtl_templateinvocation_constructor_args():
    sig = inspect.signature(mtl_TemplateInvocation.__init__)
    params = list(sig.parameters.keys())
    assert "super" in params, "Missing parameter 'super'"

def test_mtl_templateinvocation_has_super():
    assert hasattr(mtl_TemplateInvocation, "super")
    descriptor = None
    for klass in mtl_TemplateInvocation.__mro__:
        if "super" in klass.__dict__:
            descriptor = klass.__dict__["super"]
            break
    assert isinstance(descriptor, property)



def test_mtl_macroinvocation_is_not_abstract():
    assert not inspect.isabstract(mtl_MacroInvocation)


def test_mtl_macroinvocation_constructor_exists():
    assert callable(mtl_MacroInvocation.__init__)


def test_mtl_macroinvocation_constructor_args():
    sig = inspect.signature(mtl_MacroInvocation.__init__)
    params = list(sig.parameters.keys())



def test_mtl_queryinvocation_is_not_abstract():
    assert not inspect.isabstract(mtl_QueryInvocation)


def test_mtl_queryinvocation_constructor_exists():
    assert callable(mtl_QueryInvocation.__init__)


def test_mtl_queryinvocation_constructor_args():
    sig = inspect.signature(mtl_QueryInvocation.__init__)
    params = list(sig.parameters.keys())



def test_mtl_block_is_not_abstract():
    assert not inspect.isabstract(mtl_Block)


def test_mtl_block_constructor_exists():
    assert callable(mtl_Block.__init__)


def test_mtl_block_constructor_args():
    sig = inspect.signature(mtl_Block.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCLExpression)


def test_oclexpression_constructor_exists():
    assert callable(OCLExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_mtl_templateexpression_is_not_abstract():
    assert not inspect.isabstract(mtl_TemplateExpression)


def test_mtl_templateexpression_constructor_exists():
    assert callable(mtl_TemplateExpression.__init__)


def test_mtl_templateexpression_constructor_args():
    sig = inspect.signature(mtl_TemplateExpression.__init__)
    params = list(sig.parameters.keys())



def test_utilities_astnode_is_not_abstract():
    assert not inspect.isabstract(utilities_ASTNode)


def test_utilities_astnode_constructor_exists():
    assert callable(utilities_ASTNode.__init__)


def test_utilities_astnode_constructor_args():
    sig = inspect.signature(utilities_ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_mtl_moduleelement_is_not_abstract():
    assert not inspect.isabstract(mtl_ModuleElement)


def test_mtl_moduleelement_constructor_exists():
    assert callable(mtl_ModuleElement.__init__)


def test_mtl_moduleelement_constructor_args():
    sig = inspect.signature(mtl_ModuleElement.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_mtl_moduleelement_has_visibility():
    assert hasattr(mtl_ModuleElement, "visibility")
    descriptor = None
    for klass in mtl_ModuleElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_mtl_typedmodel_is_not_abstract():
    assert not inspect.isabstract(mtl_TypedModel)


def test_mtl_typedmodel_constructor_exists():
    assert callable(mtl_TypedModel.__init__)


def test_mtl_typedmodel_constructor_args():
    sig = inspect.signature(mtl_TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_documentedelement_is_not_abstract():
    assert not inspect.isabstract(DocumentedElement)


def test_documentedelement_constructor_exists():
    assert callable(DocumentedElement.__init__)


def test_documentedelement_constructor_args():
    sig = inspect.signature(DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_mtl_template_is_not_abstract():
    assert not inspect.isabstract(mtl_Template)


def test_mtl_template_constructor_exists():
    assert callable(mtl_Template.__init__)


def test_mtl_template_constructor_args():
    sig = inspect.signature(mtl_Template.__init__)
    params = list(sig.parameters.keys())
    assert "main" in params, "Missing parameter 'main'"

def test_mtl_template_has_main():
    assert hasattr(mtl_Template, "main")
    descriptor = None
    for klass in mtl_Template.__mro__:
        if "main" in klass.__dict__:
            descriptor = klass.__dict__["main"]
            break
    assert isinstance(descriptor, property)



def test_mtl_query_is_not_abstract():
    assert not inspect.isabstract(mtl_Query)


def test_mtl_query_constructor_exists():
    assert callable(mtl_Query.__init__)


def test_mtl_query_constructor_args():
    sig = inspect.signature(mtl_Query.__init__)
    params = list(sig.parameters.keys())



def test_mtl_macro_is_not_abstract():
    assert not inspect.isabstract(mtl_Macro)


def test_mtl_macro_constructor_exists():
    assert callable(mtl_Macro.__init__)


def test_mtl_macro_constructor_args():
    sig = inspect.signature(mtl_Macro.__init__)
    params = list(sig.parameters.keys())



def test_mtl_module_is_not_abstract():
    assert not inspect.isabstract(mtl_Module)


def test_mtl_module_constructor_exists():
    assert callable(mtl_Module.__init__)


def test_mtl_module_constructor_args():
    sig = inspect.signature(mtl_Module.__init__)
    params = list(sig.parameters.keys())
    assert "startHeaderPosition" in params, "Missing parameter 'startHeaderPosition'"
    assert "endHeaderPosition" in params, "Missing parameter 'endHeaderPosition'"

def test_mtl_module_has_startHeaderPosition():
    assert hasattr(mtl_Module, "startHeaderPosition")
    descriptor = None
    for klass in mtl_Module.__mro__:
        if "startHeaderPosition" in klass.__dict__:
            descriptor = klass.__dict__["startHeaderPosition"]
            break
    assert isinstance(descriptor, property)

def test_mtl_module_has_endHeaderPosition():
    assert hasattr(mtl_Module, "endHeaderPosition")
    descriptor = None
    for klass in mtl_Module.__mro__:
        if "endHeaderPosition" in klass.__dict__:
            descriptor = klass.__dict__["endHeaderPosition"]
            break
    assert isinstance(descriptor, property)

def test_openmodekind_exists():
    # Check that the Enumeration exists
    assert OpenModeKind is not None

def test_openmodekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OpenModeKind]
    expected_literals = [
        "OverWrite",
        "Append",
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
        "Public",
        "Protected",
        "Private",
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
mtl_ModuleElementDocumentation_strategy = st.builds(
    mtl_ModuleElementDocumentation,
)
mtl_ModuleDocumentation_strategy = st.builds(
    mtl_ModuleDocumentation,
    author=
        safe_text,
    version=
        safe_text,
    since=
        safe_text
)
mtl_DocumentedElement_strategy = st.builds(
    mtl_DocumentedElement,
    deprecated=
        st.booleans()
)
Comment_strategy = st.builds(
    Comment,
)
mtl_ParameterDocumentation_strategy = st.builds(
    mtl_ParameterDocumentation,
)
mtl_Documentation_strategy = st.builds(
    mtl_Documentation,
)
mtl_CommentBody_strategy = st.builds(
    mtl_CommentBody,
    startPosition=
        st.integers(),
    endPosition=
        st.integers(),
    value=
        safe_text
)
mtl_EPackage_strategy = st.builds(
    mtl_EPackage,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
mtl_Comment_strategy = st.builds(
    mtl_Comment,
)
Block_strategy = st.builds(
    Block,
)
mtl_LetBlock_strategy = st.builds(
    mtl_LetBlock,
)
mtl_FileBlock_strategy = st.builds(
    mtl_FileBlock,
    openMode=
        safe_text
)
mtl_TraceBlock_strategy = st.builds(
    mtl_TraceBlock,
)
mtl_IfBlock_strategy = st.builds(
    mtl_IfBlock,
)
mtl_ForBlock_strategy = st.builds(
    mtl_ForBlock,
)
mtl_ProtectedAreaBlock_strategy = st.builds(
    mtl_ProtectedAreaBlock,
)
mtl_EClassifier_strategy = st.builds(
    mtl_EClassifier,
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
mtl_InitSection_strategy = st.builds(
    mtl_InitSection,
)
TemplateExpression_strategy = st.builds(
    TemplateExpression,
)
mtl_TemplateInvocation_strategy = st.builds(
    mtl_TemplateInvocation,
    super=
        st.booleans()
)
mtl_MacroInvocation_strategy = st.builds(
    mtl_MacroInvocation,
)
mtl_QueryInvocation_strategy = st.builds(
    mtl_QueryInvocation,
)
mtl_Block_strategy = st.builds(
    mtl_Block,
)
OCLExpression_strategy = st.builds(
    OCLExpression,
)
mtl_TemplateExpression_strategy = st.builds(
    mtl_TemplateExpression,
)
utilities_ASTNode_strategy = st.builds(
    utilities_ASTNode,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
mtl_ModuleElement_strategy = st.builds(
    mtl_ModuleElement,
    visibility=
        safe_text
)
mtl_TypedModel_strategy = st.builds(
    mtl_TypedModel,
)
DocumentedElement_strategy = st.builds(
    DocumentedElement,
)
mtl_Template_strategy = st.builds(
    mtl_Template,
    main=
        st.booleans()
)
mtl_Query_strategy = st.builds(
    mtl_Query,
)
mtl_Macro_strategy = st.builds(
    mtl_Macro,
)
mtl_Module_strategy = st.builds(
    mtl_Module,
    startHeaderPosition=
        st.integers(),
    endHeaderPosition=
        st.integers()
)

@given(instance=Documentation_strategy)
@settings(max_examples=50)
def test_documentation_instantiation(instance):
    assert isinstance(instance, Documentation)

@given(instance=mtl_ModuleElementDocumentation_strategy)
@settings(max_examples=50)
def test_mtl_moduleelementdocumentation_instantiation(instance):
    assert isinstance(instance, mtl_ModuleElementDocumentation)

@given(instance=mtl_ModuleDocumentation_strategy)
@settings(max_examples=50)
def test_mtl_moduledocumentation_instantiation(instance):
    assert isinstance(instance, mtl_ModuleDocumentation)



@given(instance=mtl_ModuleDocumentation_strategy)
def test_mtl_moduledocumentation_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=mtl_ModuleDocumentation_strategy)
def test_mtl_moduledocumentation_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=mtl_ModuleDocumentation_strategy)
def test_mtl_moduledocumentation_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=mtl_DocumentedElement_strategy)
@settings(max_examples=50)
def test_mtl_documentedelement_instantiation(instance):
    assert isinstance(instance, mtl_DocumentedElement)



@given(instance=mtl_DocumentedElement_strategy)
def test_mtl_documentedelement_deprecated_setter(instance):
    original = instance.deprecated
    instance.deprecated = original
    assert instance.deprecated == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=mtl_ParameterDocumentation_strategy)
@settings(max_examples=50)
def test_mtl_parameterdocumentation_instantiation(instance):
    assert isinstance(instance, mtl_ParameterDocumentation)

@given(instance=mtl_Documentation_strategy)
@settings(max_examples=50)
def test_mtl_documentation_instantiation(instance):
    assert isinstance(instance, mtl_Documentation)

@given(instance=mtl_CommentBody_strategy)
@settings(max_examples=50)
def test_mtl_commentbody_instantiation(instance):
    assert isinstance(instance, mtl_CommentBody)



@given(instance=mtl_CommentBody_strategy)
def test_mtl_commentbody_startPosition_setter(instance):
    original = instance.startPosition
    instance.startPosition = original
    assert instance.startPosition == original



@given(instance=mtl_CommentBody_strategy)
def test_mtl_commentbody_endPosition_setter(instance):
    original = instance.endPosition
    instance.endPosition = original
    assert instance.endPosition == original



@given(instance=mtl_CommentBody_strategy)
def test_mtl_commentbody_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mtl_EPackage_strategy)
@settings(max_examples=50)
def test_mtl_epackage_instantiation(instance):
    assert isinstance(instance, mtl_EPackage)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=mtl_Comment_strategy)
@settings(max_examples=50)
def test_mtl_comment_instantiation(instance):
    assert isinstance(instance, mtl_Comment)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=mtl_LetBlock_strategy)
@settings(max_examples=50)
def test_mtl_letblock_instantiation(instance):
    assert isinstance(instance, mtl_LetBlock)

@given(instance=mtl_FileBlock_strategy)
@settings(max_examples=50)
def test_mtl_fileblock_instantiation(instance):
    assert isinstance(instance, mtl_FileBlock)



@given(instance=mtl_FileBlock_strategy)
def test_mtl_fileblock_openMode_setter(instance):
    original = instance.openMode
    instance.openMode = original
    assert instance.openMode == original

@given(instance=mtl_TraceBlock_strategy)
@settings(max_examples=50)
def test_mtl_traceblock_instantiation(instance):
    assert isinstance(instance, mtl_TraceBlock)

@given(instance=mtl_IfBlock_strategy)
@settings(max_examples=50)
def test_mtl_ifblock_instantiation(instance):
    assert isinstance(instance, mtl_IfBlock)

@given(instance=mtl_ForBlock_strategy)
@settings(max_examples=50)
def test_mtl_forblock_instantiation(instance):
    assert isinstance(instance, mtl_ForBlock)

@given(instance=mtl_ProtectedAreaBlock_strategy)
@settings(max_examples=50)
def test_mtl_protectedareablock_instantiation(instance):
    assert isinstance(instance, mtl_ProtectedAreaBlock)

@given(instance=mtl_EClassifier_strategy)
@settings(max_examples=50)
def test_mtl_eclassifier_instantiation(instance):
    assert isinstance(instance, mtl_EClassifier)

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

@given(instance=mtl_InitSection_strategy)
@settings(max_examples=50)
def test_mtl_initsection_instantiation(instance):
    assert isinstance(instance, mtl_InitSection)

@given(instance=TemplateExpression_strategy)
@settings(max_examples=50)
def test_templateexpression_instantiation(instance):
    assert isinstance(instance, TemplateExpression)

@given(instance=mtl_TemplateInvocation_strategy)
@settings(max_examples=50)
def test_mtl_templateinvocation_instantiation(instance):
    assert isinstance(instance, mtl_TemplateInvocation)



@given(instance=mtl_TemplateInvocation_strategy)
def test_mtl_templateinvocation_super_setter(instance):
    original = instance.super
    instance.super = original
    assert instance.super == original

@given(instance=mtl_MacroInvocation_strategy)
@settings(max_examples=50)
def test_mtl_macroinvocation_instantiation(instance):
    assert isinstance(instance, mtl_MacroInvocation)

@given(instance=mtl_QueryInvocation_strategy)
@settings(max_examples=50)
def test_mtl_queryinvocation_instantiation(instance):
    assert isinstance(instance, mtl_QueryInvocation)

@given(instance=mtl_Block_strategy)
@settings(max_examples=50)
def test_mtl_block_instantiation(instance):
    assert isinstance(instance, mtl_Block)

@given(instance=OCLExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OCLExpression)

@given(instance=mtl_TemplateExpression_strategy)
@settings(max_examples=50)
def test_mtl_templateexpression_instantiation(instance):
    assert isinstance(instance, mtl_TemplateExpression)

@given(instance=utilities_ASTNode_strategy)
@settings(max_examples=50)
def test_utilities_astnode_instantiation(instance):
    assert isinstance(instance, utilities_ASTNode)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=mtl_ModuleElement_strategy)
@settings(max_examples=50)
def test_mtl_moduleelement_instantiation(instance):
    assert isinstance(instance, mtl_ModuleElement)



@given(instance=mtl_ModuleElement_strategy)
def test_mtl_moduleelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=mtl_TypedModel_strategy)
@settings(max_examples=50)
def test_mtl_typedmodel_instantiation(instance):
    assert isinstance(instance, mtl_TypedModel)

@given(instance=DocumentedElement_strategy)
@settings(max_examples=50)
def test_documentedelement_instantiation(instance):
    assert isinstance(instance, DocumentedElement)

@given(instance=mtl_Template_strategy)
@settings(max_examples=50)
def test_mtl_template_instantiation(instance):
    assert isinstance(instance, mtl_Template)



@given(instance=mtl_Template_strategy)
def test_mtl_template_main_setter(instance):
    original = instance.main
    instance.main = original
    assert instance.main == original

@given(instance=mtl_Query_strategy)
@settings(max_examples=50)
def test_mtl_query_instantiation(instance):
    assert isinstance(instance, mtl_Query)

@given(instance=mtl_Macro_strategy)
@settings(max_examples=50)
def test_mtl_macro_instantiation(instance):
    assert isinstance(instance, mtl_Macro)

@given(instance=mtl_Module_strategy)
@settings(max_examples=50)
def test_mtl_module_instantiation(instance):
    assert isinstance(instance, mtl_Module)



@given(instance=mtl_Module_strategy)
def test_mtl_module_startHeaderPosition_setter(instance):
    original = instance.startHeaderPosition
    instance.startHeaderPosition = original
    assert instance.startHeaderPosition == original



@given(instance=mtl_Module_strategy)
def test_mtl_module_endHeaderPosition_setter(instance):
    original = instance.endHeaderPosition
    instance.endHeaderPosition = original
    assert instance.endHeaderPosition == original
