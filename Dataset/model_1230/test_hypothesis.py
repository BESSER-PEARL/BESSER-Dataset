import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ModuleElement,
    CSTNode,
    cst::TypedModel,
    cst::ModuleExtendsValue,
    cst::ModuleImportsValue,
    cst::ModuleElement,
    EPackage,
    cst::Module,
    cst::CSTNode,
    Comment,
    cst::Documentation,
    cst::Query,
    cst::InitSection,
    cst::EPackage,
    cst::TemplateExpression,
    cst::Variable,
    cst::TemplateOverridesValue,
    Block,
    cst::LetBlock,
    cst::ProtectedAreaBlock,
    cst::TraceBlock,
    cst::Macro,
    cst::ForBlock,
    cst::IfBlock,
    cst::FileBlock,
    cst::Template,
    TemplateExpression,
    cst::ModelExpression,
    cst::Comment,
    cst::TextExpression,
    cst::Block,
    VisibilityKind,
    OpenModeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_cstnode_is_not_abstract():
    assert not inspect.isabstract(CSTNode)


def test_cstnode_constructor_exists():
    assert callable(CSTNode.__init__)


def test_cstnode_constructor_args():
    sig = inspect.signature(CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_cst::typedmodel_is_not_abstract():
    assert not inspect.isabstract(cst::TypedModel)


def test_cst::typedmodel_constructor_exists():
    assert callable(cst::TypedModel.__init__)


def test_cst::typedmodel_constructor_args():
    sig = inspect.signature(cst::TypedModel.__init__)
    params = list(sig.parameters.keys())



def test_cst::moduleextendsvalue_is_not_abstract():
    assert not inspect.isabstract(cst::ModuleExtendsValue)


def test_cst::moduleextendsvalue_constructor_exists():
    assert callable(cst::ModuleExtendsValue.__init__)


def test_cst::moduleextendsvalue_constructor_args():
    sig = inspect.signature(cst::ModuleExtendsValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cst::moduleextendsvalue_has_name():
    assert hasattr(cst::ModuleExtendsValue, "name")
    descriptor = None
    for klass in cst::ModuleExtendsValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cst::moduleimportsvalue_is_not_abstract():
    assert not inspect.isabstract(cst::ModuleImportsValue)


def test_cst::moduleimportsvalue_constructor_exists():
    assert callable(cst::ModuleImportsValue.__init__)


def test_cst::moduleimportsvalue_constructor_args():
    sig = inspect.signature(cst::ModuleImportsValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cst::moduleimportsvalue_has_name():
    assert hasattr(cst::ModuleImportsValue, "name")
    descriptor = None
    for klass in cst::ModuleImportsValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cst::moduleelement_is_not_abstract():
    assert not inspect.isabstract(cst::ModuleElement)


def test_cst::moduleelement_constructor_exists():
    assert callable(cst::ModuleElement.__init__)


def test_cst::moduleelement_constructor_args():
    sig = inspect.signature(cst::ModuleElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_cst::moduleelement_has_name():
    assert hasattr(cst::ModuleElement, "name")
    descriptor = None
    for klass in cst::ModuleElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cst::moduleelement_has_visibility():
    assert hasattr(cst::ModuleElement, "visibility")
    descriptor = None
    for klass in cst::ModuleElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_epackage_is_not_abstract():
    assert not inspect.isabstract(EPackage)


def test_epackage_constructor_exists():
    assert callable(EPackage.__init__)


def test_epackage_constructor_args():
    sig = inspect.signature(EPackage.__init__)
    params = list(sig.parameters.keys())



def test_cst::module_is_not_abstract():
    assert not inspect.isabstract(cst::Module)


def test_cst::module_constructor_exists():
    assert callable(cst::Module.__init__)


def test_cst::module_constructor_args():
    sig = inspect.signature(cst::Module.__init__)
    params = list(sig.parameters.keys())



def test_cst::cstnode_is_not_abstract():
    assert not inspect.isabstract(cst::CSTNode)


def test_cst::cstnode_constructor_exists():
    assert callable(cst::CSTNode.__init__)


def test_cst::cstnode_constructor_args():
    sig = inspect.signature(cst::CSTNode.__init__)
    params = list(sig.parameters.keys())
    assert "endPosition" in params, "Missing parameter 'endPosition'"
    assert "startPosition" in params, "Missing parameter 'startPosition'"

def test_cst::cstnode_has_endPosition():
    assert hasattr(cst::CSTNode, "endPosition")
    descriptor = None
    for klass in cst::CSTNode.__mro__:
        if "endPosition" in klass.__dict__:
            descriptor = klass.__dict__["endPosition"]
            break
    assert isinstance(descriptor, property)

def test_cst::cstnode_has_startPosition():
    assert hasattr(cst::CSTNode, "startPosition")
    descriptor = None
    for klass in cst::CSTNode.__mro__:
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



def test_cst::documentation_is_not_abstract():
    assert not inspect.isabstract(cst::Documentation)


def test_cst::documentation_constructor_exists():
    assert callable(cst::Documentation.__init__)


def test_cst::documentation_constructor_args():
    sig = inspect.signature(cst::Documentation.__init__)
    params = list(sig.parameters.keys())



def test_cst::query_is_not_abstract():
    assert not inspect.isabstract(cst::Query)


def test_cst::query_constructor_exists():
    assert callable(cst::Query.__init__)


def test_cst::query_constructor_args():
    sig = inspect.signature(cst::Query.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cst::query_has_type():
    assert hasattr(cst::Query, "type")
    descriptor = None
    for klass in cst::Query.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cst::initsection_is_not_abstract():
    assert not inspect.isabstract(cst::InitSection)


def test_cst::initsection_constructor_exists():
    assert callable(cst::InitSection.__init__)


def test_cst::initsection_constructor_args():
    sig = inspect.signature(cst::InitSection.__init__)
    params = list(sig.parameters.keys())



def test_cst::epackage_is_not_abstract():
    assert not inspect.isabstract(cst::EPackage)


def test_cst::epackage_constructor_exists():
    assert callable(cst::EPackage.__init__)


def test_cst::epackage_constructor_args():
    sig = inspect.signature(cst::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_cst::templateexpression_is_not_abstract():
    assert not inspect.isabstract(cst::TemplateExpression)


def test_cst::templateexpression_constructor_exists():
    assert callable(cst::TemplateExpression.__init__)


def test_cst::templateexpression_constructor_args():
    sig = inspect.signature(cst::TemplateExpression.__init__)
    params = list(sig.parameters.keys())



def test_cst::variable_is_not_abstract():
    assert not inspect.isabstract(cst::Variable)


def test_cst::variable_constructor_exists():
    assert callable(cst::Variable.__init__)


def test_cst::variable_constructor_args():
    sig = inspect.signature(cst::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_cst::variable_has_type():
    assert hasattr(cst::Variable, "type")
    descriptor = None
    for klass in cst::Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_cst::variable_has_name():
    assert hasattr(cst::Variable, "name")
    descriptor = None
    for klass in cst::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cst::templateoverridesvalue_is_not_abstract():
    assert not inspect.isabstract(cst::TemplateOverridesValue)


def test_cst::templateoverridesvalue_constructor_exists():
    assert callable(cst::TemplateOverridesValue.__init__)


def test_cst::templateoverridesvalue_constructor_args():
    sig = inspect.signature(cst::TemplateOverridesValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cst::templateoverridesvalue_has_name():
    assert hasattr(cst::TemplateOverridesValue, "name")
    descriptor = None
    for klass in cst::TemplateOverridesValue.__mro__:
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



def test_cst::letblock_is_not_abstract():
    assert not inspect.isabstract(cst::LetBlock)


def test_cst::letblock_constructor_exists():
    assert callable(cst::LetBlock.__init__)


def test_cst::letblock_constructor_args():
    sig = inspect.signature(cst::LetBlock.__init__)
    params = list(sig.parameters.keys())



def test_cst::protectedareablock_is_not_abstract():
    assert not inspect.isabstract(cst::ProtectedAreaBlock)


def test_cst::protectedareablock_constructor_exists():
    assert callable(cst::ProtectedAreaBlock.__init__)


def test_cst::protectedareablock_constructor_args():
    sig = inspect.signature(cst::ProtectedAreaBlock.__init__)
    params = list(sig.parameters.keys())



def test_cst::traceblock_is_not_abstract():
    assert not inspect.isabstract(cst::TraceBlock)


def test_cst::traceblock_constructor_exists():
    assert callable(cst::TraceBlock.__init__)


def test_cst::traceblock_constructor_args():
    sig = inspect.signature(cst::TraceBlock.__init__)
    params = list(sig.parameters.keys())



def test_cst::macro_is_not_abstract():
    assert not inspect.isabstract(cst::Macro)


def test_cst::macro_constructor_exists():
    assert callable(cst::Macro.__init__)


def test_cst::macro_constructor_args():
    sig = inspect.signature(cst::Macro.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cst::macro_has_type():
    assert hasattr(cst::Macro, "type")
    descriptor = None
    for klass in cst::Macro.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cst::forblock_is_not_abstract():
    assert not inspect.isabstract(cst::ForBlock)


def test_cst::forblock_constructor_exists():
    assert callable(cst::ForBlock.__init__)


def test_cst::forblock_constructor_args():
    sig = inspect.signature(cst::ForBlock.__init__)
    params = list(sig.parameters.keys())



def test_cst::ifblock_is_not_abstract():
    assert not inspect.isabstract(cst::IfBlock)


def test_cst::ifblock_constructor_exists():
    assert callable(cst::IfBlock.__init__)


def test_cst::ifblock_constructor_args():
    sig = inspect.signature(cst::IfBlock.__init__)
    params = list(sig.parameters.keys())



def test_cst::fileblock_is_not_abstract():
    assert not inspect.isabstract(cst::FileBlock)


def test_cst::fileblock_constructor_exists():
    assert callable(cst::FileBlock.__init__)


def test_cst::fileblock_constructor_args():
    sig = inspect.signature(cst::FileBlock.__init__)
    params = list(sig.parameters.keys())
    assert "openMode" in params, "Missing parameter 'openMode'"

def test_cst::fileblock_has_openMode():
    assert hasattr(cst::FileBlock, "openMode")
    descriptor = None
    for klass in cst::FileBlock.__mro__:
        if "openMode" in klass.__dict__:
            descriptor = klass.__dict__["openMode"]
            break
    assert isinstance(descriptor, property)



def test_cst::template_is_not_abstract():
    assert not inspect.isabstract(cst::Template)


def test_cst::template_constructor_exists():
    assert callable(cst::Template.__init__)


def test_cst::template_constructor_args():
    sig = inspect.signature(cst::Template.__init__)
    params = list(sig.parameters.keys())



def test_templateexpression_is_not_abstract():
    assert not inspect.isabstract(TemplateExpression)


def test_templateexpression_constructor_exists():
    assert callable(TemplateExpression.__init__)


def test_templateexpression_constructor_args():
    sig = inspect.signature(TemplateExpression.__init__)
    params = list(sig.parameters.keys())



def test_cst::modelexpression_is_not_abstract():
    assert not inspect.isabstract(cst::ModelExpression)


def test_cst::modelexpression_constructor_exists():
    assert callable(cst::ModelExpression.__init__)


def test_cst::modelexpression_constructor_args():
    sig = inspect.signature(cst::ModelExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_cst::modelexpression_has_body():
    assert hasattr(cst::ModelExpression, "body")
    descriptor = None
    for klass in cst::ModelExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_cst::comment_is_not_abstract():
    assert not inspect.isabstract(cst::Comment)


def test_cst::comment_constructor_exists():
    assert callable(cst::Comment.__init__)


def test_cst::comment_constructor_args():
    sig = inspect.signature(cst::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_cst::comment_has_body():
    assert hasattr(cst::Comment, "body")
    descriptor = None
    for klass in cst::Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_cst::textexpression_is_not_abstract():
    assert not inspect.isabstract(cst::TextExpression)


def test_cst::textexpression_constructor_exists():
    assert callable(cst::TextExpression.__init__)


def test_cst::textexpression_constructor_args():
    sig = inspect.signature(cst::TextExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cst::textexpression_has_value():
    assert hasattr(cst::TextExpression, "value")
    descriptor = None
    for klass in cst::TextExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cst::block_is_not_abstract():
    assert not inspect.isabstract(cst::Block)


def test_cst::block_constructor_exists():
    assert callable(cst::Block.__init__)


def test_cst::block_constructor_args():
    sig = inspect.signature(cst::Block.__init__)
    params = list(sig.parameters.keys())

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "Protected",
        "Private",
        "Public",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

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
ModuleElement_strategy = st.builds(
    ModuleElement,
)
CSTNode_strategy = st.builds(
    CSTNode,
)
cst::TypedModel_strategy = st.builds(
    cst::TypedModel,
)
cst::ModuleExtendsValue_strategy = st.builds(
    cst::ModuleExtendsValue,
    name=
        safe_text
)
cst::ModuleImportsValue_strategy = st.builds(
    cst::ModuleImportsValue,
    name=
        safe_text
)
cst::ModuleElement_strategy = st.builds(
    cst::ModuleElement,
    name=
        safe_text,
    visibility=
        safe_text
)
EPackage_strategy = st.builds(
    EPackage,
)
cst::Module_strategy = st.builds(
    cst::Module,
)
cst::CSTNode_strategy = st.builds(
    cst::CSTNode,
    endPosition=
        st.integers(),
    startPosition=
        st.integers()
)
Comment_strategy = st.builds(
    Comment,
)
cst::Documentation_strategy = st.builds(
    cst::Documentation,
)
cst::Query_strategy = st.builds(
    cst::Query,
    type=
        safe_text
)
cst::InitSection_strategy = st.builds(
    cst::InitSection,
)
cst::EPackage_strategy = st.builds(
    cst::EPackage,
)
cst::TemplateExpression_strategy = st.builds(
    cst::TemplateExpression,
)
cst::Variable_strategy = st.builds(
    cst::Variable,
    type=
        safe_text,
    name=
        safe_text
)
cst::TemplateOverridesValue_strategy = st.builds(
    cst::TemplateOverridesValue,
    name=
        safe_text
)
Block_strategy = st.builds(
    Block,
)
cst::LetBlock_strategy = st.builds(
    cst::LetBlock,
)
cst::ProtectedAreaBlock_strategy = st.builds(
    cst::ProtectedAreaBlock,
)
cst::TraceBlock_strategy = st.builds(
    cst::TraceBlock,
)
cst::Macro_strategy = st.builds(
    cst::Macro,
    type=
        safe_text
)
cst::ForBlock_strategy = st.builds(
    cst::ForBlock,
)
cst::IfBlock_strategy = st.builds(
    cst::IfBlock,
)
cst::FileBlock_strategy = st.builds(
    cst::FileBlock,
    openMode=
        safe_text
)
cst::Template_strategy = st.builds(
    cst::Template,
)
TemplateExpression_strategy = st.builds(
    TemplateExpression,
)
cst::ModelExpression_strategy = st.builds(
    cst::ModelExpression,
    body=
        safe_text
)
cst::Comment_strategy = st.builds(
    cst::Comment,
    body=
        safe_text
)
cst::TextExpression_strategy = st.builds(
    cst::TextExpression,
    value=
        safe_text
)
cst::Block_strategy = st.builds(
    cst::Block,
)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=CSTNode_strategy)
@settings(max_examples=50)
def test_cstnode_instantiation(instance):
    assert isinstance(instance, CSTNode)

@given(instance=cst::TypedModel_strategy)
@settings(max_examples=50)
def test_cst::typedmodel_instantiation(instance):
    assert isinstance(instance, cst::TypedModel)

@given(instance=cst::ModuleExtendsValue_strategy)
@settings(max_examples=50)
def test_cst::moduleextendsvalue_instantiation(instance):
    assert isinstance(instance, cst::ModuleExtendsValue)

@given(instance=cst::ModuleExtendsValue_strategy)
def test_cst::moduleextendsvalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cst::ModuleExtendsValue_strategy)
def test_cst::moduleextendsvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cst::ModuleImportsValue_strategy)
@settings(max_examples=50)
def test_cst::moduleimportsvalue_instantiation(instance):
    assert isinstance(instance, cst::ModuleImportsValue)

@given(instance=cst::ModuleImportsValue_strategy)
def test_cst::moduleimportsvalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cst::ModuleImportsValue_strategy)
def test_cst::moduleimportsvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cst::ModuleElement_strategy)
@settings(max_examples=50)
def test_cst::moduleelement_instantiation(instance):
    assert isinstance(instance, cst::ModuleElement)

@given(instance=cst::ModuleElement_strategy)
def test_cst::moduleelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cst::ModuleElement_strategy)
def test_cst::moduleelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cst::ModuleElement_strategy)
def test_cst::moduleelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=cst::ModuleElement_strategy)
def test_cst::moduleelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=EPackage_strategy)
@settings(max_examples=50)
def test_epackage_instantiation(instance):
    assert isinstance(instance, EPackage)

@given(instance=cst::Module_strategy)
@settings(max_examples=50)
def test_cst::module_instantiation(instance):
    assert isinstance(instance, cst::Module)

@given(instance=cst::CSTNode_strategy)
@settings(max_examples=50)
def test_cst::cstnode_instantiation(instance):
    assert isinstance(instance, cst::CSTNode)

@given(instance=cst::CSTNode_strategy)
def test_cst::cstnode_endPosition_type(instance):
    assert isinstance(instance.endPosition, int)


@given(instance=cst::CSTNode_strategy)
def test_cst::cstnode_endPosition_setter(instance):
    original = instance.endPosition
    instance.endPosition = original
    assert instance.endPosition == original

@given(instance=cst::CSTNode_strategy)
def test_cst::cstnode_startPosition_type(instance):
    assert isinstance(instance.startPosition, int)


@given(instance=cst::CSTNode_strategy)
def test_cst::cstnode_startPosition_setter(instance):
    original = instance.startPosition
    instance.startPosition = original
    assert instance.startPosition == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=cst::Documentation_strategy)
@settings(max_examples=50)
def test_cst::documentation_instantiation(instance):
    assert isinstance(instance, cst::Documentation)

@given(instance=cst::Query_strategy)
@settings(max_examples=50)
def test_cst::query_instantiation(instance):
    assert isinstance(instance, cst::Query)

@given(instance=cst::Query_strategy)
def test_cst::query_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cst::Query_strategy)
def test_cst::query_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cst::InitSection_strategy)
@settings(max_examples=50)
def test_cst::initsection_instantiation(instance):
    assert isinstance(instance, cst::InitSection)

@given(instance=cst::EPackage_strategy)
@settings(max_examples=50)
def test_cst::epackage_instantiation(instance):
    assert isinstance(instance, cst::EPackage)

@given(instance=cst::TemplateExpression_strategy)
@settings(max_examples=50)
def test_cst::templateexpression_instantiation(instance):
    assert isinstance(instance, cst::TemplateExpression)

@given(instance=cst::Variable_strategy)
@settings(max_examples=50)
def test_cst::variable_instantiation(instance):
    assert isinstance(instance, cst::Variable)

@given(instance=cst::Variable_strategy)
def test_cst::variable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cst::Variable_strategy)
def test_cst::variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cst::Variable_strategy)
def test_cst::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cst::Variable_strategy)
def test_cst::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cst::TemplateOverridesValue_strategy)
@settings(max_examples=50)
def test_cst::templateoverridesvalue_instantiation(instance):
    assert isinstance(instance, cst::TemplateOverridesValue)

@given(instance=cst::TemplateOverridesValue_strategy)
def test_cst::templateoverridesvalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cst::TemplateOverridesValue_strategy)
def test_cst::templateoverridesvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=cst::LetBlock_strategy)
@settings(max_examples=50)
def test_cst::letblock_instantiation(instance):
    assert isinstance(instance, cst::LetBlock)

@given(instance=cst::ProtectedAreaBlock_strategy)
@settings(max_examples=50)
def test_cst::protectedareablock_instantiation(instance):
    assert isinstance(instance, cst::ProtectedAreaBlock)

@given(instance=cst::TraceBlock_strategy)
@settings(max_examples=50)
def test_cst::traceblock_instantiation(instance):
    assert isinstance(instance, cst::TraceBlock)

@given(instance=cst::Macro_strategy)
@settings(max_examples=50)
def test_cst::macro_instantiation(instance):
    assert isinstance(instance, cst::Macro)

@given(instance=cst::Macro_strategy)
def test_cst::macro_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cst::Macro_strategy)
def test_cst::macro_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cst::ForBlock_strategy)
@settings(max_examples=50)
def test_cst::forblock_instantiation(instance):
    assert isinstance(instance, cst::ForBlock)

@given(instance=cst::IfBlock_strategy)
@settings(max_examples=50)
def test_cst::ifblock_instantiation(instance):
    assert isinstance(instance, cst::IfBlock)

@given(instance=cst::FileBlock_strategy)
@settings(max_examples=50)
def test_cst::fileblock_instantiation(instance):
    assert isinstance(instance, cst::FileBlock)

@given(instance=cst::FileBlock_strategy)
def test_cst::fileblock_openMode_type(instance):
    assert isinstance(instance.openMode, str)


@given(instance=cst::FileBlock_strategy)
def test_cst::fileblock_openMode_setter(instance):
    original = instance.openMode
    instance.openMode = original
    assert instance.openMode == original

@given(instance=cst::Template_strategy)
@settings(max_examples=50)
def test_cst::template_instantiation(instance):
    assert isinstance(instance, cst::Template)

@given(instance=TemplateExpression_strategy)
@settings(max_examples=50)
def test_templateexpression_instantiation(instance):
    assert isinstance(instance, TemplateExpression)

@given(instance=cst::ModelExpression_strategy)
@settings(max_examples=50)
def test_cst::modelexpression_instantiation(instance):
    assert isinstance(instance, cst::ModelExpression)

@given(instance=cst::ModelExpression_strategy)
def test_cst::modelexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=cst::ModelExpression_strategy)
def test_cst::modelexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=cst::Comment_strategy)
@settings(max_examples=50)
def test_cst::comment_instantiation(instance):
    assert isinstance(instance, cst::Comment)

@given(instance=cst::Comment_strategy)
def test_cst::comment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=cst::Comment_strategy)
def test_cst::comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=cst::TextExpression_strategy)
@settings(max_examples=50)
def test_cst::textexpression_instantiation(instance):
    assert isinstance(instance, cst::TextExpression)

@given(instance=cst::TextExpression_strategy)
def test_cst::textexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cst::TextExpression_strategy)
def test_cst::textexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cst::Block_strategy)
@settings(max_examples=50)
def test_cst::block_instantiation(instance):
    assert isinstance(instance, cst::Block)
