import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CSTNode,
    cst_ModuleElement,
    cst_TypedModel,
    EPackage,
    cst_Module,
    cst_CSTNode,
    Comment,
    cst_InitSection,
    cst_EPackage,
    cst_Documentation,
    cst_ModuleImportsValue,
    cst_TemplateExpression,
    cst_Variable,
    cst_TemplateOverridesValue,
    Block,
    cst_ForBlock,
    cst_IfBlock,
    cst_FileBlock,
    cst_LetBlock,
    cst_TraceBlock,
    cst_ProtectedAreaBlock,
    TemplateExpression,
    cst_TextExpression,
    cst_Block,
    cst_ModelExpression,
    ModuleElement,
    cst_Query,
    cst_Macro,
    cst_Template,
    cst_Comment,
    cst_ModuleExtendsValue,
    OpenModeKind,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cstnode_is_not_abstract():
    assert not inspect.isabstract(CSTNode)


def test_cstnode_constructor_exists():
    assert callable(CSTNode.__init__)


def test_cstnode_constructor_args():
    sig = inspect.signature(CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_cst_moduleelement_is_not_abstract():
    assert not inspect.isabstract(cst_ModuleElement)


def test_cst_moduleelement_constructor_exists():
    assert callable(cst_ModuleElement.__init__)


def test_cst_moduleelement_constructor_args():
    sig = inspect.signature(cst_ModuleElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_cst_moduleelement_has_name():
    assert hasattr(cst_ModuleElement, "name")
    descriptor = None
    for klass in cst_ModuleElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cst_moduleelement_has_visibility():
    assert hasattr(cst_ModuleElement, "visibility")
    descriptor = None
    for klass in cst_ModuleElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_cst_typedmodel_is_not_abstract():
    assert not inspect.isabstract(cst_TypedModel)


def test_cst_typedmodel_constructor_exists():
    assert callable(cst_TypedModel.__init__)


def test_cst_typedmodel_constructor_args():
    sig = inspect.signature(cst_TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_epackage_is_not_abstract():
    assert not inspect.isabstract(EPackage)


def test_epackage_constructor_exists():
    assert callable(EPackage.__init__)


def test_epackage_constructor_args():
    sig = inspect.signature(EPackage.__init__)
    params = list(sig.parameters.keys())



def test_cst_module_is_not_abstract():
    assert not inspect.isabstract(cst_Module)


def test_cst_module_constructor_exists():
    assert callable(cst_Module.__init__)


def test_cst_module_constructor_args():
    sig = inspect.signature(cst_Module.__init__)
    params = list(sig.parameters.keys())



def test_cst_cstnode_is_not_abstract():
    assert not inspect.isabstract(cst_CSTNode)


def test_cst_cstnode_constructor_exists():
    assert callable(cst_CSTNode.__init__)


def test_cst_cstnode_constructor_args():
    sig = inspect.signature(cst_CSTNode.__init__)
    params = list(sig.parameters.keys())
    assert "endPosition" in params, "Missing parameter 'endPosition'"
    assert "startPosition" in params, "Missing parameter 'startPosition'"

def test_cst_cstnode_has_endPosition():
    assert hasattr(cst_CSTNode, "endPosition")
    descriptor = None
    for klass in cst_CSTNode.__mro__:
        if "endPosition" in klass.__dict__:
            descriptor = klass.__dict__["endPosition"]
            break
    assert isinstance(descriptor, property)

def test_cst_cstnode_has_startPosition():
    assert hasattr(cst_CSTNode, "startPosition")
    descriptor = None
    for klass in cst_CSTNode.__mro__:
        if "startPosition" in klass.__dict__:
            descriptor = klass.__dict__["startPosition"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_cst_initsection_is_not_abstract():
    assert not inspect.isabstract(cst_InitSection)


def test_cst_initsection_constructor_exists():
    assert callable(cst_InitSection.__init__)


def test_cst_initsection_constructor_args():
    sig = inspect.signature(cst_InitSection.__init__)
    params = list(sig.parameters.keys())



def test_cst_epackage_is_not_abstract():
    assert not inspect.isabstract(cst_EPackage)


def test_cst_epackage_constructor_exists():
    assert callable(cst_EPackage.__init__)


def test_cst_epackage_constructor_args():
    sig = inspect.signature(cst_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_cst_documentation_is_not_abstract():
    assert not inspect.isabstract(cst_Documentation)


def test_cst_documentation_constructor_exists():
    assert callable(cst_Documentation.__init__)


def test_cst_documentation_constructor_args():
    sig = inspect.signature(cst_Documentation.__init__)
    params = list(sig.parameters.keys())



def test_cst_moduleimportsvalue_is_not_abstract():
    assert not inspect.isabstract(cst_ModuleImportsValue)


def test_cst_moduleimportsvalue_constructor_exists():
    assert callable(cst_ModuleImportsValue.__init__)


def test_cst_moduleimportsvalue_constructor_args():
    sig = inspect.signature(cst_ModuleImportsValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cst_moduleimportsvalue_has_name():
    assert hasattr(cst_ModuleImportsValue, "name")
    descriptor = None
    for klass in cst_ModuleImportsValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cst_templateexpression_is_not_abstract():
    assert not inspect.isabstract(cst_TemplateExpression)


def test_cst_templateexpression_constructor_exists():
    assert callable(cst_TemplateExpression.__init__)


def test_cst_templateexpression_constructor_args():
    sig = inspect.signature(cst_TemplateExpression.__init__)
    params = list(sig.parameters.keys())



def test_cst_variable_is_not_abstract():
    assert not inspect.isabstract(cst_Variable)


def test_cst_variable_constructor_exists():
    assert callable(cst_Variable.__init__)


def test_cst_variable_constructor_args():
    sig = inspect.signature(cst_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_cst_variable_has_name():
    assert hasattr(cst_Variable, "name")
    descriptor = None
    for klass in cst_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cst_variable_has_type():
    assert hasattr(cst_Variable, "type")
    descriptor = None
    for klass in cst_Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cst_templateoverridesvalue_is_not_abstract():
    assert not inspect.isabstract(cst_TemplateOverridesValue)


def test_cst_templateoverridesvalue_constructor_exists():
    assert callable(cst_TemplateOverridesValue.__init__)


def test_cst_templateoverridesvalue_constructor_args():
    sig = inspect.signature(cst_TemplateOverridesValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cst_templateoverridesvalue_has_name():
    assert hasattr(cst_TemplateOverridesValue, "name")
    descriptor = None
    for klass in cst_TemplateOverridesValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_cst_forblock_is_not_abstract():
    assert not inspect.isabstract(cst_ForBlock)


def test_cst_forblock_constructor_exists():
    assert callable(cst_ForBlock.__init__)


def test_cst_forblock_constructor_args():
    sig = inspect.signature(cst_ForBlock.__init__)
    params = list(sig.parameters.keys())



def test_cst_ifblock_is_not_abstract():
    assert not inspect.isabstract(cst_IfBlock)


def test_cst_ifblock_constructor_exists():
    assert callable(cst_IfBlock.__init__)


def test_cst_ifblock_constructor_args():
    sig = inspect.signature(cst_IfBlock.__init__)
    params = list(sig.parameters.keys())



def test_cst_fileblock_is_not_abstract():
    assert not inspect.isabstract(cst_FileBlock)


def test_cst_fileblock_constructor_exists():
    assert callable(cst_FileBlock.__init__)


def test_cst_fileblock_constructor_args():
    sig = inspect.signature(cst_FileBlock.__init__)
    params = list(sig.parameters.keys())
    assert "openMode" in params, "Missing parameter 'openMode'"

def test_cst_fileblock_has_openMode():
    assert hasattr(cst_FileBlock, "openMode")
    descriptor = None
    for klass in cst_FileBlock.__mro__:
        if "openMode" in klass.__dict__:
            descriptor = klass.__dict__["openMode"]
            break
    assert isinstance(descriptor, property)



def test_cst_letblock_is_not_abstract():
    assert not inspect.isabstract(cst_LetBlock)


def test_cst_letblock_constructor_exists():
    assert callable(cst_LetBlock.__init__)


def test_cst_letblock_constructor_args():
    sig = inspect.signature(cst_LetBlock.__init__)
    params = list(sig.parameters.keys())



def test_cst_traceblock_is_not_abstract():
    assert not inspect.isabstract(cst_TraceBlock)


def test_cst_traceblock_constructor_exists():
    assert callable(cst_TraceBlock.__init__)


def test_cst_traceblock_constructor_args():
    sig = inspect.signature(cst_TraceBlock.__init__)
    params = list(sig.parameters.keys())



def test_cst_protectedareablock_is_not_abstract():
    assert not inspect.isabstract(cst_ProtectedAreaBlock)


def test_cst_protectedareablock_constructor_exists():
    assert callable(cst_ProtectedAreaBlock.__init__)


def test_cst_protectedareablock_constructor_args():
    sig = inspect.signature(cst_ProtectedAreaBlock.__init__)
    params = list(sig.parameters.keys())



def test_templateexpression_is_not_abstract():
    assert not inspect.isabstract(TemplateExpression)


def test_templateexpression_constructor_exists():
    assert callable(TemplateExpression.__init__)


def test_templateexpression_constructor_args():
    sig = inspect.signature(TemplateExpression.__init__)
    params = list(sig.parameters.keys())



def test_cst_textexpression_is_not_abstract():
    assert not inspect.isabstract(cst_TextExpression)


def test_cst_textexpression_constructor_exists():
    assert callable(cst_TextExpression.__init__)


def test_cst_textexpression_constructor_args():
    sig = inspect.signature(cst_TextExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cst_textexpression_has_value():
    assert hasattr(cst_TextExpression, "value")
    descriptor = None
    for klass in cst_TextExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cst_block_is_not_abstract():
    assert not inspect.isabstract(cst_Block)


def test_cst_block_constructor_exists():
    assert callable(cst_Block.__init__)


def test_cst_block_constructor_args():
    sig = inspect.signature(cst_Block.__init__)
    params = list(sig.parameters.keys())



def test_cst_modelexpression_is_not_abstract():
    assert not inspect.isabstract(cst_ModelExpression)


def test_cst_modelexpression_constructor_exists():
    assert callable(cst_ModelExpression.__init__)


def test_cst_modelexpression_constructor_args():
    sig = inspect.signature(cst_ModelExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_cst_modelexpression_has_body():
    assert hasattr(cst_ModelExpression, "body")
    descriptor = None
    for klass in cst_ModelExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_cst_query_is_not_abstract():
    assert not inspect.isabstract(cst_Query)


def test_cst_query_constructor_exists():
    assert callable(cst_Query.__init__)


def test_cst_query_constructor_args():
    sig = inspect.signature(cst_Query.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cst_query_has_type():
    assert hasattr(cst_Query, "type")
    descriptor = None
    for klass in cst_Query.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cst_macro_is_not_abstract():
    assert not inspect.isabstract(cst_Macro)


def test_cst_macro_constructor_exists():
    assert callable(cst_Macro.__init__)


def test_cst_macro_constructor_args():
    sig = inspect.signature(cst_Macro.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cst_macro_has_type():
    assert hasattr(cst_Macro, "type")
    descriptor = None
    for klass in cst_Macro.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cst_template_is_not_abstract():
    assert not inspect.isabstract(cst_Template)


def test_cst_template_constructor_exists():
    assert callable(cst_Template.__init__)


def test_cst_template_constructor_args():
    sig = inspect.signature(cst_Template.__init__)
    params = list(sig.parameters.keys())



def test_cst_comment_is_not_abstract():
    assert not inspect.isabstract(cst_Comment)


def test_cst_comment_constructor_exists():
    assert callable(cst_Comment.__init__)


def test_cst_comment_constructor_args():
    sig = inspect.signature(cst_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_cst_comment_has_body():
    assert hasattr(cst_Comment, "body")
    descriptor = None
    for klass in cst_Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_cst_moduleextendsvalue_is_not_abstract():
    assert not inspect.isabstract(cst_ModuleExtendsValue)


def test_cst_moduleextendsvalue_constructor_exists():
    assert callable(cst_ModuleExtendsValue.__init__)


def test_cst_moduleextendsvalue_constructor_args():
    sig = inspect.signature(cst_ModuleExtendsValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cst_moduleextendsvalue_has_name():
    assert hasattr(cst_ModuleExtendsValue, "name")
    descriptor = None
    for klass in cst_ModuleExtendsValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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
CSTNode_strategy = st.builds(
    CSTNode,
)
cst_ModuleElement_strategy = st.builds(
    cst_ModuleElement,
    name=
        safe_text,
    visibility=
        safe_text
)
cst_TypedModel_strategy = st.builds(
    cst_TypedModel,
)
EPackage_strategy = st.builds(
    EPackage,
)
cst_Module_strategy = st.builds(
    cst_Module,
)
cst_CSTNode_strategy = st.builds(
    cst_CSTNode,
    endPosition=
        st.integers(),
    startPosition=
        st.integers()
)
Comment_strategy = st.builds(
    Comment,
)
cst_InitSection_strategy = st.builds(
    cst_InitSection,
)
cst_EPackage_strategy = st.builds(
    cst_EPackage,
)
cst_Documentation_strategy = st.builds(
    cst_Documentation,
)
cst_ModuleImportsValue_strategy = st.builds(
    cst_ModuleImportsValue,
    name=
        safe_text
)
cst_TemplateExpression_strategy = st.builds(
    cst_TemplateExpression,
)
cst_Variable_strategy = st.builds(
    cst_Variable,
    name=
        safe_text,
    type=
        safe_text
)
cst_TemplateOverridesValue_strategy = st.builds(
    cst_TemplateOverridesValue,
    name=
        safe_text
)
Block_strategy = st.builds(
    Block,
)
cst_ForBlock_strategy = st.builds(
    cst_ForBlock,
)
cst_IfBlock_strategy = st.builds(
    cst_IfBlock,
)
cst_FileBlock_strategy = st.builds(
    cst_FileBlock,
    openMode=
        safe_text
)
cst_LetBlock_strategy = st.builds(
    cst_LetBlock,
)
cst_TraceBlock_strategy = st.builds(
    cst_TraceBlock,
)
cst_ProtectedAreaBlock_strategy = st.builds(
    cst_ProtectedAreaBlock,
)
TemplateExpression_strategy = st.builds(
    TemplateExpression,
)
cst_TextExpression_strategy = st.builds(
    cst_TextExpression,
    value=
        safe_text
)
cst_Block_strategy = st.builds(
    cst_Block,
)
cst_ModelExpression_strategy = st.builds(
    cst_ModelExpression,
    body=
        safe_text
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
cst_Query_strategy = st.builds(
    cst_Query,
    type=
        safe_text
)
cst_Macro_strategy = st.builds(
    cst_Macro,
    type=
        safe_text
)
cst_Template_strategy = st.builds(
    cst_Template,
)
cst_Comment_strategy = st.builds(
    cst_Comment,
    body=
        safe_text
)
cst_ModuleExtendsValue_strategy = st.builds(
    cst_ModuleExtendsValue,
    name=
        safe_text
)

@given(instance=CSTNode_strategy)
@settings(max_examples=50)
def test_cstnode_instantiation(instance):
    assert isinstance(instance, CSTNode)

@given(instance=cst_ModuleElement_strategy)
@settings(max_examples=50)
def test_cst_moduleelement_instantiation(instance):
    assert isinstance(instance, cst_ModuleElement)



@given(instance=cst_ModuleElement_strategy)
def test_cst_moduleelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cst_ModuleElement_strategy)
def test_cst_moduleelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=cst_TypedModel_strategy)
@settings(max_examples=50)
def test_cst_typedmodel_instantiation(instance):
    assert isinstance(instance, cst_TypedModel)

@given(instance=EPackage_strategy)
@settings(max_examples=50)
def test_epackage_instantiation(instance):
    assert isinstance(instance, EPackage)

@given(instance=cst_Module_strategy)
@settings(max_examples=50)
def test_cst_module_instantiation(instance):
    assert isinstance(instance, cst_Module)

@given(instance=cst_CSTNode_strategy)
@settings(max_examples=50)
def test_cst_cstnode_instantiation(instance):
    assert isinstance(instance, cst_CSTNode)



@given(instance=cst_CSTNode_strategy)
def test_cst_cstnode_endPosition_setter(instance):
    original = instance.endPosition
    instance.endPosition = original
    assert instance.endPosition == original



@given(instance=cst_CSTNode_strategy)
def test_cst_cstnode_startPosition_setter(instance):
    original = instance.startPosition
    instance.startPosition = original
    assert instance.startPosition == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=cst_InitSection_strategy)
@settings(max_examples=50)
def test_cst_initsection_instantiation(instance):
    assert isinstance(instance, cst_InitSection)

@given(instance=cst_EPackage_strategy)
@settings(max_examples=50)
def test_cst_epackage_instantiation(instance):
    assert isinstance(instance, cst_EPackage)

@given(instance=cst_Documentation_strategy)
@settings(max_examples=50)
def test_cst_documentation_instantiation(instance):
    assert isinstance(instance, cst_Documentation)

@given(instance=cst_ModuleImportsValue_strategy)
@settings(max_examples=50)
def test_cst_moduleimportsvalue_instantiation(instance):
    assert isinstance(instance, cst_ModuleImportsValue)



@given(instance=cst_ModuleImportsValue_strategy)
def test_cst_moduleimportsvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cst_TemplateExpression_strategy)
@settings(max_examples=50)
def test_cst_templateexpression_instantiation(instance):
    assert isinstance(instance, cst_TemplateExpression)

@given(instance=cst_Variable_strategy)
@settings(max_examples=50)
def test_cst_variable_instantiation(instance):
    assert isinstance(instance, cst_Variable)



@given(instance=cst_Variable_strategy)
def test_cst_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cst_Variable_strategy)
def test_cst_variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cst_TemplateOverridesValue_strategy)
@settings(max_examples=50)
def test_cst_templateoverridesvalue_instantiation(instance):
    assert isinstance(instance, cst_TemplateOverridesValue)



@given(instance=cst_TemplateOverridesValue_strategy)
def test_cst_templateoverridesvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=cst_ForBlock_strategy)
@settings(max_examples=50)
def test_cst_forblock_instantiation(instance):
    assert isinstance(instance, cst_ForBlock)

@given(instance=cst_IfBlock_strategy)
@settings(max_examples=50)
def test_cst_ifblock_instantiation(instance):
    assert isinstance(instance, cst_IfBlock)

@given(instance=cst_FileBlock_strategy)
@settings(max_examples=50)
def test_cst_fileblock_instantiation(instance):
    assert isinstance(instance, cst_FileBlock)



@given(instance=cst_FileBlock_strategy)
def test_cst_fileblock_openMode_setter(instance):
    original = instance.openMode
    instance.openMode = original
    assert instance.openMode == original

@given(instance=cst_LetBlock_strategy)
@settings(max_examples=50)
def test_cst_letblock_instantiation(instance):
    assert isinstance(instance, cst_LetBlock)

@given(instance=cst_TraceBlock_strategy)
@settings(max_examples=50)
def test_cst_traceblock_instantiation(instance):
    assert isinstance(instance, cst_TraceBlock)

@given(instance=cst_ProtectedAreaBlock_strategy)
@settings(max_examples=50)
def test_cst_protectedareablock_instantiation(instance):
    assert isinstance(instance, cst_ProtectedAreaBlock)

@given(instance=TemplateExpression_strategy)
@settings(max_examples=50)
def test_templateexpression_instantiation(instance):
    assert isinstance(instance, TemplateExpression)

@given(instance=cst_TextExpression_strategy)
@settings(max_examples=50)
def test_cst_textexpression_instantiation(instance):
    assert isinstance(instance, cst_TextExpression)



@given(instance=cst_TextExpression_strategy)
def test_cst_textexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cst_Block_strategy)
@settings(max_examples=50)
def test_cst_block_instantiation(instance):
    assert isinstance(instance, cst_Block)

@given(instance=cst_ModelExpression_strategy)
@settings(max_examples=50)
def test_cst_modelexpression_instantiation(instance):
    assert isinstance(instance, cst_ModelExpression)



@given(instance=cst_ModelExpression_strategy)
def test_cst_modelexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=cst_Query_strategy)
@settings(max_examples=50)
def test_cst_query_instantiation(instance):
    assert isinstance(instance, cst_Query)



@given(instance=cst_Query_strategy)
def test_cst_query_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cst_Macro_strategy)
@settings(max_examples=50)
def test_cst_macro_instantiation(instance):
    assert isinstance(instance, cst_Macro)



@given(instance=cst_Macro_strategy)
def test_cst_macro_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cst_Template_strategy)
@settings(max_examples=50)
def test_cst_template_instantiation(instance):
    assert isinstance(instance, cst_Template)

@given(instance=cst_Comment_strategy)
@settings(max_examples=50)
def test_cst_comment_instantiation(instance):
    assert isinstance(instance, cst_Comment)



@given(instance=cst_Comment_strategy)
def test_cst_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=cst_ModuleExtendsValue_strategy)
@settings(max_examples=50)
def test_cst_moduleextendsvalue_instantiation(instance):
    assert isinstance(instance, cst_ModuleExtendsValue)



@given(instance=cst_ModuleExtendsValue_strategy)
def test_cst_moduleextendsvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
