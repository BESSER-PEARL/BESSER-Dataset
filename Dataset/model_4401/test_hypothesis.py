import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    If,
    Call,
    mt_core_Parameter,
    Parameter,
    Literal,
    mt_expressions_NullLiteral,
    mt_expressions_IntegerLiteral,
    mt_expressions_DoubleLiteral,
    mt_expressions_BooleanLiteral,
    mt_expressions_StringLiteral,
    FilePath,
    Statement,
    mt_statements_Feature,
    mt_statements_Comment,
    mt_statements_For,
    mt_statements_If,
    mt_statements_Text,
    ScriptDescriptor,
    ASTNode,
    mt_expressions_Expression,
    mt_expressions_Call,
    mt_statements_Statement,
    mt_core_ScriptDescriptor,
    mt_core_Script,
    Script,
    core_mt_Resource,
    Resource,
    mt_core_Template,
    mt_core_ASTNode,
    mt_core_Method,
    Method,
    mt_core_Service,
    mt_core_Metamodel,
    mt_core_FilePath,
    Expression,
    mt_expressions_Literal,
    mt_expressions_Operator,
    mt_expressions_Not,
    mt_expressions_CallSet,
    mt_expressions_Parenthesis,
    mt_Resource,
    mt_ResourceSet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_if_is_not_abstract():
    assert not inspect.isabstract(If)


def test_if_constructor_exists():
    assert callable(If.__init__)


def test_if_constructor_args():
    sig = inspect.signature(If.__init__)
    params = list(sig.parameters.keys())



def test_call_is_not_abstract():
    assert not inspect.isabstract(Call)


def test_call_constructor_exists():
    assert callable(Call.__init__)


def test_call_constructor_args():
    sig = inspect.signature(Call.__init__)
    params = list(sig.parameters.keys())



def test_mt_core_parameter_is_not_abstract():
    assert not inspect.isabstract(mt_core_Parameter)


def test_mt_core_parameter_constructor_exists():
    assert callable(mt_core_Parameter.__init__)


def test_mt_core_parameter_constructor_args():
    sig = inspect.signature(mt_core_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mt_core_parameter_has_type():
    assert hasattr(mt_core_Parameter, "type")
    descriptor = None
    for klass in mt_core_Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_mt_expressions_nullliteral_is_not_abstract():
    assert not inspect.isabstract(mt_expressions_NullLiteral)


def test_mt_expressions_nullliteral_constructor_exists():
    assert callable(mt_expressions_NullLiteral.__init__)


def test_mt_expressions_nullliteral_constructor_args():
    sig = inspect.signature(mt_expressions_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_mt_expressions_integerliteral_is_not_abstract():
    assert not inspect.isabstract(mt_expressions_IntegerLiteral)


def test_mt_expressions_integerliteral_constructor_exists():
    assert callable(mt_expressions_IntegerLiteral.__init__)


def test_mt_expressions_integerliteral_constructor_args():
    sig = inspect.signature(mt_expressions_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mt_expressions_integerliteral_has_value():
    assert hasattr(mt_expressions_IntegerLiteral, "value")
    descriptor = None
    for klass in mt_expressions_IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mt_expressions_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(mt_expressions_DoubleLiteral)


def test_mt_expressions_doubleliteral_constructor_exists():
    assert callable(mt_expressions_DoubleLiteral.__init__)


def test_mt_expressions_doubleliteral_constructor_args():
    sig = inspect.signature(mt_expressions_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mt_expressions_doubleliteral_has_value():
    assert hasattr(mt_expressions_DoubleLiteral, "value")
    descriptor = None
    for klass in mt_expressions_DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mt_expressions_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(mt_expressions_BooleanLiteral)


def test_mt_expressions_booleanliteral_constructor_exists():
    assert callable(mt_expressions_BooleanLiteral.__init__)


def test_mt_expressions_booleanliteral_constructor_args():
    sig = inspect.signature(mt_expressions_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mt_expressions_booleanliteral_has_value():
    assert hasattr(mt_expressions_BooleanLiteral, "value")
    descriptor = None
    for klass in mt_expressions_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mt_expressions_stringliteral_is_not_abstract():
    assert not inspect.isabstract(mt_expressions_StringLiteral)


def test_mt_expressions_stringliteral_constructor_exists():
    assert callable(mt_expressions_StringLiteral.__init__)


def test_mt_expressions_stringliteral_constructor_args():
    sig = inspect.signature(mt_expressions_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mt_expressions_stringliteral_has_value():
    assert hasattr(mt_expressions_StringLiteral, "value")
    descriptor = None
    for klass in mt_expressions_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_filepath_is_not_abstract():
    assert not inspect.isabstract(FilePath)


def test_filepath_constructor_exists():
    assert callable(FilePath.__init__)


def test_filepath_constructor_args():
    sig = inspect.signature(FilePath.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_mt_statements_feature_is_not_abstract():
    assert not inspect.isabstract(mt_statements_Feature)


def test_mt_statements_feature_constructor_exists():
    assert callable(mt_statements_Feature.__init__)


def test_mt_statements_feature_constructor_args():
    sig = inspect.signature(mt_statements_Feature.__init__)
    params = list(sig.parameters.keys())



def test_mt_statements_comment_is_not_abstract():
    assert not inspect.isabstract(mt_statements_Comment)


def test_mt_statements_comment_constructor_exists():
    assert callable(mt_statements_Comment.__init__)


def test_mt_statements_comment_constructor_args():
    sig = inspect.signature(mt_statements_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mt_statements_comment_has_value():
    assert hasattr(mt_statements_Comment, "value")
    descriptor = None
    for klass in mt_statements_Comment.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mt_statements_for_is_not_abstract():
    assert not inspect.isabstract(mt_statements_For)


def test_mt_statements_for_constructor_exists():
    assert callable(mt_statements_For.__init__)


def test_mt_statements_for_constructor_args():
    sig = inspect.signature(mt_statements_For.__init__)
    params = list(sig.parameters.keys())



def test_mt_statements_if_is_not_abstract():
    assert not inspect.isabstract(mt_statements_If)


def test_mt_statements_if_constructor_exists():
    assert callable(mt_statements_If.__init__)


def test_mt_statements_if_constructor_args():
    sig = inspect.signature(mt_statements_If.__init__)
    params = list(sig.parameters.keys())



def test_mt_statements_text_is_not_abstract():
    assert not inspect.isabstract(mt_statements_Text)


def test_mt_statements_text_constructor_exists():
    assert callable(mt_statements_Text.__init__)


def test_mt_statements_text_constructor_args():
    sig = inspect.signature(mt_statements_Text.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mt_statements_text_has_value():
    assert hasattr(mt_statements_Text, "value")
    descriptor = None
    for klass in mt_statements_Text.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_scriptdescriptor_is_not_abstract():
    assert not inspect.isabstract(ScriptDescriptor)


def test_scriptdescriptor_constructor_exists():
    assert callable(ScriptDescriptor.__init__)


def test_scriptdescriptor_constructor_args():
    sig = inspect.signature(ScriptDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_mt_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(mt_expressions_Expression)


def test_mt_expressions_expression_constructor_exists():
    assert callable(mt_expressions_Expression.__init__)


def test_mt_expressions_expression_constructor_args():
    sig = inspect.signature(mt_expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mt_expressions_call_is_not_abstract():
    assert not inspect.isabstract(mt_expressions_Call)


def test_mt_expressions_call_constructor_exists():
    assert callable(mt_expressions_Call.__init__)


def test_mt_expressions_call_constructor_args():
    sig = inspect.signature(mt_expressions_Call.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "name" in params, "Missing parameter 'name'"

def test_mt_expressions_call_has_prefix():
    assert hasattr(mt_expressions_Call, "prefix")
    descriptor = None
    for klass in mt_expressions_Call.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_mt_expressions_call_has_name():
    assert hasattr(mt_expressions_Call, "name")
    descriptor = None
    for klass in mt_expressions_Call.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mt_statements_statement_is_not_abstract():
    assert not inspect.isabstract(mt_statements_Statement)


def test_mt_statements_statement_constructor_exists():
    assert callable(mt_statements_Statement.__init__)


def test_mt_statements_statement_constructor_args():
    sig = inspect.signature(mt_statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_mt_core_scriptdescriptor_is_not_abstract():
    assert not inspect.isabstract(mt_core_ScriptDescriptor)


def test_mt_core_scriptdescriptor_constructor_exists():
    assert callable(mt_core_ScriptDescriptor.__init__)


def test_mt_core_scriptdescriptor_constructor_args():
    sig = inspect.signature(mt_core_ScriptDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_mt_core_scriptdescriptor_has_type():
    assert hasattr(mt_core_ScriptDescriptor, "type")
    descriptor = None
    for klass in mt_core_ScriptDescriptor.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mt_core_scriptdescriptor_has_name():
    assert hasattr(mt_core_ScriptDescriptor, "name")
    descriptor = None
    for klass in mt_core_ScriptDescriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mt_core_scriptdescriptor_has_description():
    assert hasattr(mt_core_ScriptDescriptor, "description")
    descriptor = None
    for klass in mt_core_ScriptDescriptor.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_mt_core_script_is_not_abstract():
    assert not inspect.isabstract(mt_core_Script)


def test_mt_core_script_constructor_exists():
    assert callable(mt_core_Script.__init__)


def test_mt_core_script_constructor_args():
    sig = inspect.signature(mt_core_Script.__init__)
    params = list(sig.parameters.keys())



def test_script_is_not_abstract():
    assert not inspect.isabstract(Script)


def test_script_constructor_exists():
    assert callable(Script.__init__)


def test_script_constructor_args():
    sig = inspect.signature(Script.__init__)
    params = list(sig.parameters.keys())



def test_core_mt_resource_is_not_abstract():
    assert not inspect.isabstract(core_mt_Resource)


def test_core_mt_resource_constructor_exists():
    assert callable(core_mt_Resource.__init__)


def test_core_mt_resource_constructor_args():
    sig = inspect.signature(core_mt_Resource.__init__)
    params = list(sig.parameters.keys())



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_mt_core_template_is_not_abstract():
    assert not inspect.isabstract(mt_core_Template)


def test_mt_core_template_constructor_exists():
    assert callable(mt_core_Template.__init__)


def test_mt_core_template_constructor_args():
    sig = inspect.signature(mt_core_Template.__init__)
    params = list(sig.parameters.keys())
    assert "beginTag" in params, "Missing parameter 'beginTag'"
    assert "endTag" in params, "Missing parameter 'endTag'"

def test_mt_core_template_has_beginTag():
    assert hasattr(mt_core_Template, "beginTag")
    descriptor = None
    for klass in mt_core_Template.__mro__:
        if "beginTag" in klass.__dict__:
            descriptor = klass.__dict__["beginTag"]
            break
    assert isinstance(descriptor, property)

def test_mt_core_template_has_endTag():
    assert hasattr(mt_core_Template, "endTag")
    descriptor = None
    for klass in mt_core_Template.__mro__:
        if "endTag" in klass.__dict__:
            descriptor = klass.__dict__["endTag"]
            break
    assert isinstance(descriptor, property)



def test_mt_core_astnode_is_not_abstract():
    assert not inspect.isabstract(mt_core_ASTNode)


def test_mt_core_astnode_constructor_exists():
    assert callable(mt_core_ASTNode.__init__)


def test_mt_core_astnode_constructor_args():
    sig = inspect.signature(mt_core_ASTNode.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "begin" in params, "Missing parameter 'begin'"

def test_mt_core_astnode_has_end():
    assert hasattr(mt_core_ASTNode, "end")
    descriptor = None
    for klass in mt_core_ASTNode.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_mt_core_astnode_has_begin():
    assert hasattr(mt_core_ASTNode, "begin")
    descriptor = None
    for klass in mt_core_ASTNode.__mro__:
        if "begin" in klass.__dict__:
            descriptor = klass.__dict__["begin"]
            break
    assert isinstance(descriptor, property)



def test_mt_core_method_is_not_abstract():
    assert not inspect.isabstract(mt_core_Method)


def test_mt_core_method_constructor_exists():
    assert callable(mt_core_Method.__init__)


def test_mt_core_method_constructor_args():
    sig = inspect.signature(mt_core_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "return_" in params, "Missing parameter 'return_'"

def test_mt_core_method_has_name():
    assert hasattr(mt_core_Method, "name")
    descriptor = None
    for klass in mt_core_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mt_core_method_has_return_():
    assert hasattr(mt_core_Method, "return_")
    descriptor = None
    for klass in mt_core_Method.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)



def test_method_is_not_abstract():
    assert not inspect.isabstract(Method)


def test_method_constructor_exists():
    assert callable(Method.__init__)


def test_method_constructor_args():
    sig = inspect.signature(Method.__init__)
    params = list(sig.parameters.keys())



def test_mt_core_service_is_not_abstract():
    assert not inspect.isabstract(mt_core_Service)


def test_mt_core_service_constructor_exists():
    assert callable(mt_core_Service.__init__)


def test_mt_core_service_constructor_args():
    sig = inspect.signature(mt_core_Service.__init__)
    params = list(sig.parameters.keys())



def test_mt_core_metamodel_is_not_abstract():
    assert not inspect.isabstract(mt_core_Metamodel)


def test_mt_core_metamodel_constructor_exists():
    assert callable(mt_core_Metamodel.__init__)


def test_mt_core_metamodel_constructor_args():
    sig = inspect.signature(mt_core_Metamodel.__init__)
    params = list(sig.parameters.keys())
    assert "packageClass" in params, "Missing parameter 'packageClass'"

def test_mt_core_metamodel_has_packageClass():
    assert hasattr(mt_core_Metamodel, "packageClass")
    descriptor = None
    for klass in mt_core_Metamodel.__mro__:
        if "packageClass" in klass.__dict__:
            descriptor = klass.__dict__["packageClass"]
            break
    assert isinstance(descriptor, property)



def test_mt_core_filepath_is_not_abstract():
    assert not inspect.isabstract(mt_core_FilePath)


def test_mt_core_filepath_constructor_exists():
    assert callable(mt_core_FilePath.__init__)


def test_mt_core_filepath_constructor_args():
    sig = inspect.signature(mt_core_FilePath.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mt_expressions_literal_is_not_abstract():
    assert not inspect.isabstract(mt_expressions_Literal)


def test_mt_expressions_literal_constructor_exists():
    assert callable(mt_expressions_Literal.__init__)


def test_mt_expressions_literal_constructor_args():
    sig = inspect.signature(mt_expressions_Literal.__init__)
    params = list(sig.parameters.keys())



def test_mt_expressions_operator_is_not_abstract():
    assert not inspect.isabstract(mt_expressions_Operator)


def test_mt_expressions_operator_constructor_exists():
    assert callable(mt_expressions_Operator.__init__)


def test_mt_expressions_operator_constructor_args():
    sig = inspect.signature(mt_expressions_Operator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mt_expressions_operator_has_operator():
    assert hasattr(mt_expressions_Operator, "operator")
    descriptor = None
    for klass in mt_expressions_Operator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mt_expressions_not_is_not_abstract():
    assert not inspect.isabstract(mt_expressions_Not)


def test_mt_expressions_not_constructor_exists():
    assert callable(mt_expressions_Not.__init__)


def test_mt_expressions_not_constructor_args():
    sig = inspect.signature(mt_expressions_Not.__init__)
    params = list(sig.parameters.keys())



def test_mt_expressions_callset_is_not_abstract():
    assert not inspect.isabstract(mt_expressions_CallSet)


def test_mt_expressions_callset_constructor_exists():
    assert callable(mt_expressions_CallSet.__init__)


def test_mt_expressions_callset_constructor_args():
    sig = inspect.signature(mt_expressions_CallSet.__init__)
    params = list(sig.parameters.keys())



def test_mt_expressions_parenthesis_is_not_abstract():
    assert not inspect.isabstract(mt_expressions_Parenthesis)


def test_mt_expressions_parenthesis_constructor_exists():
    assert callable(mt_expressions_Parenthesis.__init__)


def test_mt_expressions_parenthesis_constructor_args():
    sig = inspect.signature(mt_expressions_Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_mt_resource_is_not_abstract():
    assert not inspect.isabstract(mt_Resource)


def test_mt_resource_constructor_exists():
    assert callable(mt_Resource.__init__)


def test_mt_resource_constructor_args():
    sig = inspect.signature(mt_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mt_resource_has_name():
    assert hasattr(mt_Resource, "name")
    descriptor = None
    for klass in mt_Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mt_resourceset_is_not_abstract():
    assert not inspect.isabstract(mt_ResourceSet)


def test_mt_resourceset_constructor_exists():
    assert callable(mt_ResourceSet.__init__)


def test_mt_resourceset_constructor_args():
    sig = inspect.signature(mt_ResourceSet.__init__)
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
If_strategy = st.builds(
    If,
)
Call_strategy = st.builds(
    Call,
)
mt_core_Parameter_strategy = st.builds(
    mt_core_Parameter,
    type=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
Literal_strategy = st.builds(
    Literal,
)
mt_expressions_NullLiteral_strategy = st.builds(
    mt_expressions_NullLiteral,
)
mt_expressions_IntegerLiteral_strategy = st.builds(
    mt_expressions_IntegerLiteral,
    value=
        st.integers()
)
mt_expressions_DoubleLiteral_strategy = st.builds(
    mt_expressions_DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mt_expressions_BooleanLiteral_strategy = st.builds(
    mt_expressions_BooleanLiteral,
    value=
        st.booleans()
)
mt_expressions_StringLiteral_strategy = st.builds(
    mt_expressions_StringLiteral,
    value=
        safe_text
)
FilePath_strategy = st.builds(
    FilePath,
)
Statement_strategy = st.builds(
    Statement,
)
mt_statements_Feature_strategy = st.builds(
    mt_statements_Feature,
)
mt_statements_Comment_strategy = st.builds(
    mt_statements_Comment,
    value=
        safe_text
)
mt_statements_For_strategy = st.builds(
    mt_statements_For,
)
mt_statements_If_strategy = st.builds(
    mt_statements_If,
)
mt_statements_Text_strategy = st.builds(
    mt_statements_Text,
    value=
        safe_text
)
ScriptDescriptor_strategy = st.builds(
    ScriptDescriptor,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
mt_expressions_Expression_strategy = st.builds(
    mt_expressions_Expression,
)
mt_expressions_Call_strategy = st.builds(
    mt_expressions_Call,
    prefix=
        safe_text,
    name=
        safe_text
)
mt_statements_Statement_strategy = st.builds(
    mt_statements_Statement,
)
mt_core_ScriptDescriptor_strategy = st.builds(
    mt_core_ScriptDescriptor,
    type=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
mt_core_Script_strategy = st.builds(
    mt_core_Script,
)
Script_strategy = st.builds(
    Script,
)
core_mt_Resource_strategy = st.builds(
    core_mt_Resource,
)
Resource_strategy = st.builds(
    Resource,
)
mt_core_Template_strategy = st.builds(
    mt_core_Template,
    beginTag=
        safe_text,
    endTag=
        safe_text
)
mt_core_ASTNode_strategy = st.builds(
    mt_core_ASTNode,
    end=
        st.integers(),
    begin=
        st.integers()
)
mt_core_Method_strategy = st.builds(
    mt_core_Method,
    name=
        safe_text,
    return_=
        safe_text
)
Method_strategy = st.builds(
    Method,
)
mt_core_Service_strategy = st.builds(
    mt_core_Service,
)
mt_core_Metamodel_strategy = st.builds(
    mt_core_Metamodel,
    packageClass=
        safe_text
)
mt_core_FilePath_strategy = st.builds(
    mt_core_FilePath,
)
Expression_strategy = st.builds(
    Expression,
)
mt_expressions_Literal_strategy = st.builds(
    mt_expressions_Literal,
)
mt_expressions_Operator_strategy = st.builds(
    mt_expressions_Operator,
    operator=
        safe_text
)
mt_expressions_Not_strategy = st.builds(
    mt_expressions_Not,
)
mt_expressions_CallSet_strategy = st.builds(
    mt_expressions_CallSet,
)
mt_expressions_Parenthesis_strategy = st.builds(
    mt_expressions_Parenthesis,
)
mt_Resource_strategy = st.builds(
    mt_Resource,
    name=
        safe_text
)
mt_ResourceSet_strategy = st.builds(
    mt_ResourceSet,
)

@given(instance=If_strategy)
@settings(max_examples=50)
def test_if_instantiation(instance):
    assert isinstance(instance, If)

@given(instance=Call_strategy)
@settings(max_examples=50)
def test_call_instantiation(instance):
    assert isinstance(instance, Call)

@given(instance=mt_core_Parameter_strategy)
@settings(max_examples=50)
def test_mt_core_parameter_instantiation(instance):
    assert isinstance(instance, mt_core_Parameter)



@given(instance=mt_core_Parameter_strategy)
def test_mt_core_parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=mt_expressions_NullLiteral_strategy)
@settings(max_examples=50)
def test_mt_expressions_nullliteral_instantiation(instance):
    assert isinstance(instance, mt_expressions_NullLiteral)

@given(instance=mt_expressions_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_mt_expressions_integerliteral_instantiation(instance):
    assert isinstance(instance, mt_expressions_IntegerLiteral)



@given(instance=mt_expressions_IntegerLiteral_strategy)
def test_mt_expressions_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mt_expressions_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_mt_expressions_doubleliteral_instantiation(instance):
    assert isinstance(instance, mt_expressions_DoubleLiteral)



@given(instance=mt_expressions_DoubleLiteral_strategy)
def test_mt_expressions_doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mt_expressions_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_mt_expressions_booleanliteral_instantiation(instance):
    assert isinstance(instance, mt_expressions_BooleanLiteral)



@given(instance=mt_expressions_BooleanLiteral_strategy)
def test_mt_expressions_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mt_expressions_StringLiteral_strategy)
@settings(max_examples=50)
def test_mt_expressions_stringliteral_instantiation(instance):
    assert isinstance(instance, mt_expressions_StringLiteral)



@given(instance=mt_expressions_StringLiteral_strategy)
def test_mt_expressions_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FilePath_strategy)
@settings(max_examples=50)
def test_filepath_instantiation(instance):
    assert isinstance(instance, FilePath)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=mt_statements_Feature_strategy)
@settings(max_examples=50)
def test_mt_statements_feature_instantiation(instance):
    assert isinstance(instance, mt_statements_Feature)

@given(instance=mt_statements_Comment_strategy)
@settings(max_examples=50)
def test_mt_statements_comment_instantiation(instance):
    assert isinstance(instance, mt_statements_Comment)



@given(instance=mt_statements_Comment_strategy)
def test_mt_statements_comment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mt_statements_For_strategy)
@settings(max_examples=50)
def test_mt_statements_for_instantiation(instance):
    assert isinstance(instance, mt_statements_For)

@given(instance=mt_statements_If_strategy)
@settings(max_examples=50)
def test_mt_statements_if_instantiation(instance):
    assert isinstance(instance, mt_statements_If)

@given(instance=mt_statements_Text_strategy)
@settings(max_examples=50)
def test_mt_statements_text_instantiation(instance):
    assert isinstance(instance, mt_statements_Text)



@given(instance=mt_statements_Text_strategy)
def test_mt_statements_text_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ScriptDescriptor_strategy)
@settings(max_examples=50)
def test_scriptdescriptor_instantiation(instance):
    assert isinstance(instance, ScriptDescriptor)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=mt_expressions_Expression_strategy)
@settings(max_examples=50)
def test_mt_expressions_expression_instantiation(instance):
    assert isinstance(instance, mt_expressions_Expression)

@given(instance=mt_expressions_Call_strategy)
@settings(max_examples=50)
def test_mt_expressions_call_instantiation(instance):
    assert isinstance(instance, mt_expressions_Call)



@given(instance=mt_expressions_Call_strategy)
def test_mt_expressions_call_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=mt_expressions_Call_strategy)
def test_mt_expressions_call_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mt_statements_Statement_strategy)
@settings(max_examples=50)
def test_mt_statements_statement_instantiation(instance):
    assert isinstance(instance, mt_statements_Statement)

@given(instance=mt_core_ScriptDescriptor_strategy)
@settings(max_examples=50)
def test_mt_core_scriptdescriptor_instantiation(instance):
    assert isinstance(instance, mt_core_ScriptDescriptor)



@given(instance=mt_core_ScriptDescriptor_strategy)
def test_mt_core_scriptdescriptor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=mt_core_ScriptDescriptor_strategy)
def test_mt_core_scriptdescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mt_core_ScriptDescriptor_strategy)
def test_mt_core_scriptdescriptor_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=mt_core_Script_strategy)
@settings(max_examples=50)
def test_mt_core_script_instantiation(instance):
    assert isinstance(instance, mt_core_Script)

@given(instance=Script_strategy)
@settings(max_examples=50)
def test_script_instantiation(instance):
    assert isinstance(instance, Script)

@given(instance=core_mt_Resource_strategy)
@settings(max_examples=50)
def test_core_mt_resource_instantiation(instance):
    assert isinstance(instance, core_mt_Resource)

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=mt_core_Template_strategy)
@settings(max_examples=50)
def test_mt_core_template_instantiation(instance):
    assert isinstance(instance, mt_core_Template)



@given(instance=mt_core_Template_strategy)
def test_mt_core_template_beginTag_setter(instance):
    original = instance.beginTag
    instance.beginTag = original
    assert instance.beginTag == original



@given(instance=mt_core_Template_strategy)
def test_mt_core_template_endTag_setter(instance):
    original = instance.endTag
    instance.endTag = original
    assert instance.endTag == original

@given(instance=mt_core_ASTNode_strategy)
@settings(max_examples=50)
def test_mt_core_astnode_instantiation(instance):
    assert isinstance(instance, mt_core_ASTNode)



@given(instance=mt_core_ASTNode_strategy)
def test_mt_core_astnode_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=mt_core_ASTNode_strategy)
def test_mt_core_astnode_begin_setter(instance):
    original = instance.begin
    instance.begin = original
    assert instance.begin == original

@given(instance=mt_core_Method_strategy)
@settings(max_examples=50)
def test_mt_core_method_instantiation(instance):
    assert isinstance(instance, mt_core_Method)



@given(instance=mt_core_Method_strategy)
def test_mt_core_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=mt_core_Method_strategy)
def test_mt_core_method_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=mt_core_Service_strategy)
@settings(max_examples=50)
def test_mt_core_service_instantiation(instance):
    assert isinstance(instance, mt_core_Service)

@given(instance=mt_core_Metamodel_strategy)
@settings(max_examples=50)
def test_mt_core_metamodel_instantiation(instance):
    assert isinstance(instance, mt_core_Metamodel)



@given(instance=mt_core_Metamodel_strategy)
def test_mt_core_metamodel_packageClass_setter(instance):
    original = instance.packageClass
    instance.packageClass = original
    assert instance.packageClass == original

@given(instance=mt_core_FilePath_strategy)
@settings(max_examples=50)
def test_mt_core_filepath_instantiation(instance):
    assert isinstance(instance, mt_core_FilePath)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mt_expressions_Literal_strategy)
@settings(max_examples=50)
def test_mt_expressions_literal_instantiation(instance):
    assert isinstance(instance, mt_expressions_Literal)

@given(instance=mt_expressions_Operator_strategy)
@settings(max_examples=50)
def test_mt_expressions_operator_instantiation(instance):
    assert isinstance(instance, mt_expressions_Operator)



@given(instance=mt_expressions_Operator_strategy)
def test_mt_expressions_operator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=mt_expressions_Not_strategy)
@settings(max_examples=50)
def test_mt_expressions_not_instantiation(instance):
    assert isinstance(instance, mt_expressions_Not)

@given(instance=mt_expressions_CallSet_strategy)
@settings(max_examples=50)
def test_mt_expressions_callset_instantiation(instance):
    assert isinstance(instance, mt_expressions_CallSet)

@given(instance=mt_expressions_Parenthesis_strategy)
@settings(max_examples=50)
def test_mt_expressions_parenthesis_instantiation(instance):
    assert isinstance(instance, mt_expressions_Parenthesis)

@given(instance=mt_Resource_strategy)
@settings(max_examples=50)
def test_mt_resource_instantiation(instance):
    assert isinstance(instance, mt_Resource)



@given(instance=mt_Resource_strategy)
def test_mt_resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mt_ResourceSet_strategy)
@settings(max_examples=50)
def test_mt_resourceset_instantiation(instance):
    assert isinstance(instance, mt_ResourceSet)
