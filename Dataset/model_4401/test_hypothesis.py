import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    If,
    Call,
    mt::core::Parameter,
    Parameter,
    Literal,
    mt::expressions::IntegerLiteral,
    mt::expressions::BooleanLiteral,
    mt::expressions::DoubleLiteral,
    mt::expressions::NullLiteral,
    mt::expressions::StringLiteral,
    FilePath,
    Statement,
    mt::statements::For,
    mt::statements::If,
    mt::statements::Text,
    mt::statements::Comment,
    mt::statements::Feature,
    ScriptDescriptor,
    ASTNode,
    mt::statements::Statement,
    mt::expressions::Call,
    mt::core::ScriptDescriptor,
    mt::expressions::Expression,
    mt::core::Script,
    Script,
    core::mt::Resource,
    Resource,
    mt::core::Template,
    mt::core::ASTNode,
    mt::core::Method,
    Method,
    mt::core::Service,
    mt::core::Metamodel,
    mt::core::FilePath,
    Expression,
    mt::expressions::Not,
    mt::expressions::Operator,
    mt::expressions::CallSet,
    mt::expressions::Parenthesis,
    mt::expressions::Literal,
    mt::Resource,
    mt::ResourceSet,
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



def test_mt::core::parameter_is_not_abstract():
    assert not inspect.isabstract(mt::core::Parameter)


def test_mt::core::parameter_constructor_exists():
    assert callable(mt::core::Parameter.__init__)


def test_mt::core::parameter_constructor_args():
    sig = inspect.signature(mt::core::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mt::core::parameter_has_type():
    assert hasattr(mt::core::Parameter, "type")
    descriptor = None
    for klass in mt::core::Parameter.__mro__:
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



def test_mt::expressions::integerliteral_is_not_abstract():
    assert not inspect.isabstract(mt::expressions::IntegerLiteral)


def test_mt::expressions::integerliteral_constructor_exists():
    assert callable(mt::expressions::IntegerLiteral.__init__)


def test_mt::expressions::integerliteral_constructor_args():
    sig = inspect.signature(mt::expressions::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mt::expressions::integerliteral_has_value():
    assert hasattr(mt::expressions::IntegerLiteral, "value")
    descriptor = None
    for klass in mt::expressions::IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mt::expressions::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(mt::expressions::BooleanLiteral)


def test_mt::expressions::booleanliteral_constructor_exists():
    assert callable(mt::expressions::BooleanLiteral.__init__)


def test_mt::expressions::booleanliteral_constructor_args():
    sig = inspect.signature(mt::expressions::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mt::expressions::booleanliteral_has_value():
    assert hasattr(mt::expressions::BooleanLiteral, "value")
    descriptor = None
    for klass in mt::expressions::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mt::expressions::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(mt::expressions::DoubleLiteral)


def test_mt::expressions::doubleliteral_constructor_exists():
    assert callable(mt::expressions::DoubleLiteral.__init__)


def test_mt::expressions::doubleliteral_constructor_args():
    sig = inspect.signature(mt::expressions::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mt::expressions::doubleliteral_has_value():
    assert hasattr(mt::expressions::DoubleLiteral, "value")
    descriptor = None
    for klass in mt::expressions::DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mt::expressions::nullliteral_is_not_abstract():
    assert not inspect.isabstract(mt::expressions::NullLiteral)


def test_mt::expressions::nullliteral_constructor_exists():
    assert callable(mt::expressions::NullLiteral.__init__)


def test_mt::expressions::nullliteral_constructor_args():
    sig = inspect.signature(mt::expressions::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_mt::expressions::stringliteral_is_not_abstract():
    assert not inspect.isabstract(mt::expressions::StringLiteral)


def test_mt::expressions::stringliteral_constructor_exists():
    assert callable(mt::expressions::StringLiteral.__init__)


def test_mt::expressions::stringliteral_constructor_args():
    sig = inspect.signature(mt::expressions::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mt::expressions::stringliteral_has_value():
    assert hasattr(mt::expressions::StringLiteral, "value")
    descriptor = None
    for klass in mt::expressions::StringLiteral.__mro__:
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



def test_mt::statements::for_is_not_abstract():
    assert not inspect.isabstract(mt::statements::For)


def test_mt::statements::for_constructor_exists():
    assert callable(mt::statements::For.__init__)


def test_mt::statements::for_constructor_args():
    sig = inspect.signature(mt::statements::For.__init__)
    params = list(sig.parameters.keys())



def test_mt::statements::if_is_not_abstract():
    assert not inspect.isabstract(mt::statements::If)


def test_mt::statements::if_constructor_exists():
    assert callable(mt::statements::If.__init__)


def test_mt::statements::if_constructor_args():
    sig = inspect.signature(mt::statements::If.__init__)
    params = list(sig.parameters.keys())



def test_mt::statements::text_is_not_abstract():
    assert not inspect.isabstract(mt::statements::Text)


def test_mt::statements::text_constructor_exists():
    assert callable(mt::statements::Text.__init__)


def test_mt::statements::text_constructor_args():
    sig = inspect.signature(mt::statements::Text.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mt::statements::text_has_value():
    assert hasattr(mt::statements::Text, "value")
    descriptor = None
    for klass in mt::statements::Text.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mt::statements::comment_is_not_abstract():
    assert not inspect.isabstract(mt::statements::Comment)


def test_mt::statements::comment_constructor_exists():
    assert callable(mt::statements::Comment.__init__)


def test_mt::statements::comment_constructor_args():
    sig = inspect.signature(mt::statements::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mt::statements::comment_has_value():
    assert hasattr(mt::statements::Comment, "value")
    descriptor = None
    for klass in mt::statements::Comment.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mt::statements::feature_is_not_abstract():
    assert not inspect.isabstract(mt::statements::Feature)


def test_mt::statements::feature_constructor_exists():
    assert callable(mt::statements::Feature.__init__)


def test_mt::statements::feature_constructor_args():
    sig = inspect.signature(mt::statements::Feature.__init__)
    params = list(sig.parameters.keys())



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



def test_mt::statements::statement_is_not_abstract():
    assert not inspect.isabstract(mt::statements::Statement)


def test_mt::statements::statement_constructor_exists():
    assert callable(mt::statements::Statement.__init__)


def test_mt::statements::statement_constructor_args():
    sig = inspect.signature(mt::statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_mt::expressions::call_is_not_abstract():
    assert not inspect.isabstract(mt::expressions::Call)


def test_mt::expressions::call_constructor_exists():
    assert callable(mt::expressions::Call.__init__)


def test_mt::expressions::call_constructor_args():
    sig = inspect.signature(mt::expressions::Call.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "name" in params, "Missing parameter 'name'"

def test_mt::expressions::call_has_prefix():
    assert hasattr(mt::expressions::Call, "prefix")
    descriptor = None
    for klass in mt::expressions::Call.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_mt::expressions::call_has_name():
    assert hasattr(mt::expressions::Call, "name")
    descriptor = None
    for klass in mt::expressions::Call.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mt::core::scriptdescriptor_is_not_abstract():
    assert not inspect.isabstract(mt::core::ScriptDescriptor)


def test_mt::core::scriptdescriptor_constructor_exists():
    assert callable(mt::core::ScriptDescriptor.__init__)


def test_mt::core::scriptdescriptor_constructor_args():
    sig = inspect.signature(mt::core::ScriptDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_mt::core::scriptdescriptor_has_description():
    assert hasattr(mt::core::ScriptDescriptor, "description")
    descriptor = None
    for klass in mt::core::ScriptDescriptor.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mt::core::scriptdescriptor_has_type():
    assert hasattr(mt::core::ScriptDescriptor, "type")
    descriptor = None
    for klass in mt::core::ScriptDescriptor.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mt::core::scriptdescriptor_has_name():
    assert hasattr(mt::core::ScriptDescriptor, "name")
    descriptor = None
    for klass in mt::core::ScriptDescriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mt::expressions::expression_is_not_abstract():
    assert not inspect.isabstract(mt::expressions::Expression)


def test_mt::expressions::expression_constructor_exists():
    assert callable(mt::expressions::Expression.__init__)


def test_mt::expressions::expression_constructor_args():
    sig = inspect.signature(mt::expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mt::core::script_is_not_abstract():
    assert not inspect.isabstract(mt::core::Script)


def test_mt::core::script_constructor_exists():
    assert callable(mt::core::Script.__init__)


def test_mt::core::script_constructor_args():
    sig = inspect.signature(mt::core::Script.__init__)
    params = list(sig.parameters.keys())



def test_script_is_not_abstract():
    assert not inspect.isabstract(Script)


def test_script_constructor_exists():
    assert callable(Script.__init__)


def test_script_constructor_args():
    sig = inspect.signature(Script.__init__)
    params = list(sig.parameters.keys())



def test_core::mt::resource_is_not_abstract():
    assert not inspect.isabstract(core::mt::Resource)


def test_core::mt::resource_constructor_exists():
    assert callable(core::mt::Resource.__init__)


def test_core::mt::resource_constructor_args():
    sig = inspect.signature(core::mt::Resource.__init__)
    params = list(sig.parameters.keys())



def test_resource_is_not_abstract():
    assert not inspect.isabstract(Resource)


def test_resource_constructor_exists():
    assert callable(Resource.__init__)


def test_resource_constructor_args():
    sig = inspect.signature(Resource.__init__)
    params = list(sig.parameters.keys())



def test_mt::core::template_is_not_abstract():
    assert not inspect.isabstract(mt::core::Template)


def test_mt::core::template_constructor_exists():
    assert callable(mt::core::Template.__init__)


def test_mt::core::template_constructor_args():
    sig = inspect.signature(mt::core::Template.__init__)
    params = list(sig.parameters.keys())
    assert "endTag" in params, "Missing parameter 'endTag'"
    assert "beginTag" in params, "Missing parameter 'beginTag'"

def test_mt::core::template_has_endTag():
    assert hasattr(mt::core::Template, "endTag")
    descriptor = None
    for klass in mt::core::Template.__mro__:
        if "endTag" in klass.__dict__:
            descriptor = klass.__dict__["endTag"]
            break
    assert isinstance(descriptor, property)

def test_mt::core::template_has_beginTag():
    assert hasattr(mt::core::Template, "beginTag")
    descriptor = None
    for klass in mt::core::Template.__mro__:
        if "beginTag" in klass.__dict__:
            descriptor = klass.__dict__["beginTag"]
            break
    assert isinstance(descriptor, property)



def test_mt::core::astnode_is_not_abstract():
    assert not inspect.isabstract(mt::core::ASTNode)


def test_mt::core::astnode_constructor_exists():
    assert callable(mt::core::ASTNode.__init__)


def test_mt::core::astnode_constructor_args():
    sig = inspect.signature(mt::core::ASTNode.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "begin" in params, "Missing parameter 'begin'"

def test_mt::core::astnode_has_end():
    assert hasattr(mt::core::ASTNode, "end")
    descriptor = None
    for klass in mt::core::ASTNode.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_mt::core::astnode_has_begin():
    assert hasattr(mt::core::ASTNode, "begin")
    descriptor = None
    for klass in mt::core::ASTNode.__mro__:
        if "begin" in klass.__dict__:
            descriptor = klass.__dict__["begin"]
            break
    assert isinstance(descriptor, property)



def test_mt::core::method_is_not_abstract():
    assert not inspect.isabstract(mt::core::Method)


def test_mt::core::method_constructor_exists():
    assert callable(mt::core::Method.__init__)


def test_mt::core::method_constructor_args():
    sig = inspect.signature(mt::core::Method.__init__)
    params = list(sig.parameters.keys())
    assert "return_" in params, "Missing parameter 'return_'"
    assert "name" in params, "Missing parameter 'name'"

def test_mt::core::method_has_return_():
    assert hasattr(mt::core::Method, "return_")
    descriptor = None
    for klass in mt::core::Method.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)

def test_mt::core::method_has_name():
    assert hasattr(mt::core::Method, "name")
    descriptor = None
    for klass in mt::core::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_method_is_not_abstract():
    assert not inspect.isabstract(Method)


def test_method_constructor_exists():
    assert callable(Method.__init__)


def test_method_constructor_args():
    sig = inspect.signature(Method.__init__)
    params = list(sig.parameters.keys())



def test_mt::core::service_is_not_abstract():
    assert not inspect.isabstract(mt::core::Service)


def test_mt::core::service_constructor_exists():
    assert callable(mt::core::Service.__init__)


def test_mt::core::service_constructor_args():
    sig = inspect.signature(mt::core::Service.__init__)
    params = list(sig.parameters.keys())



def test_mt::core::metamodel_is_not_abstract():
    assert not inspect.isabstract(mt::core::Metamodel)


def test_mt::core::metamodel_constructor_exists():
    assert callable(mt::core::Metamodel.__init__)


def test_mt::core::metamodel_constructor_args():
    sig = inspect.signature(mt::core::Metamodel.__init__)
    params = list(sig.parameters.keys())
    assert "packageClass" in params, "Missing parameter 'packageClass'"

def test_mt::core::metamodel_has_packageClass():
    assert hasattr(mt::core::Metamodel, "packageClass")
    descriptor = None
    for klass in mt::core::Metamodel.__mro__:
        if "packageClass" in klass.__dict__:
            descriptor = klass.__dict__["packageClass"]
            break
    assert isinstance(descriptor, property)



def test_mt::core::filepath_is_not_abstract():
    assert not inspect.isabstract(mt::core::FilePath)


def test_mt::core::filepath_constructor_exists():
    assert callable(mt::core::FilePath.__init__)


def test_mt::core::filepath_constructor_args():
    sig = inspect.signature(mt::core::FilePath.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mt::expressions::not_is_not_abstract():
    assert not inspect.isabstract(mt::expressions::Not)


def test_mt::expressions::not_constructor_exists():
    assert callable(mt::expressions::Not.__init__)


def test_mt::expressions::not_constructor_args():
    sig = inspect.signature(mt::expressions::Not.__init__)
    params = list(sig.parameters.keys())



def test_mt::expressions::operator_is_not_abstract():
    assert not inspect.isabstract(mt::expressions::Operator)


def test_mt::expressions::operator_constructor_exists():
    assert callable(mt::expressions::Operator.__init__)


def test_mt::expressions::operator_constructor_args():
    sig = inspect.signature(mt::expressions::Operator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mt::expressions::operator_has_operator():
    assert hasattr(mt::expressions::Operator, "operator")
    descriptor = None
    for klass in mt::expressions::Operator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mt::expressions::callset_is_not_abstract():
    assert not inspect.isabstract(mt::expressions::CallSet)


def test_mt::expressions::callset_constructor_exists():
    assert callable(mt::expressions::CallSet.__init__)


def test_mt::expressions::callset_constructor_args():
    sig = inspect.signature(mt::expressions::CallSet.__init__)
    params = list(sig.parameters.keys())



def test_mt::expressions::parenthesis_is_not_abstract():
    assert not inspect.isabstract(mt::expressions::Parenthesis)


def test_mt::expressions::parenthesis_constructor_exists():
    assert callable(mt::expressions::Parenthesis.__init__)


def test_mt::expressions::parenthesis_constructor_args():
    sig = inspect.signature(mt::expressions::Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_mt::expressions::literal_is_not_abstract():
    assert not inspect.isabstract(mt::expressions::Literal)


def test_mt::expressions::literal_constructor_exists():
    assert callable(mt::expressions::Literal.__init__)


def test_mt::expressions::literal_constructor_args():
    sig = inspect.signature(mt::expressions::Literal.__init__)
    params = list(sig.parameters.keys())



def test_mt::resource_is_not_abstract():
    assert not inspect.isabstract(mt::Resource)


def test_mt::resource_constructor_exists():
    assert callable(mt::Resource.__init__)


def test_mt::resource_constructor_args():
    sig = inspect.signature(mt::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mt::resource_has_name():
    assert hasattr(mt::Resource, "name")
    descriptor = None
    for klass in mt::Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mt::resourceset_is_not_abstract():
    assert not inspect.isabstract(mt::ResourceSet)


def test_mt::resourceset_constructor_exists():
    assert callable(mt::ResourceSet.__init__)


def test_mt::resourceset_constructor_args():
    sig = inspect.signature(mt::ResourceSet.__init__)
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
mt::core::Parameter_strategy = st.builds(
    mt::core::Parameter,
    type=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
Literal_strategy = st.builds(
    Literal,
)
mt::expressions::IntegerLiteral_strategy = st.builds(
    mt::expressions::IntegerLiteral,
    value=
        st.integers()
)
mt::expressions::BooleanLiteral_strategy = st.builds(
    mt::expressions::BooleanLiteral,
    value=
        st.booleans()
)
mt::expressions::DoubleLiteral_strategy = st.builds(
    mt::expressions::DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mt::expressions::NullLiteral_strategy = st.builds(
    mt::expressions::NullLiteral,
)
mt::expressions::StringLiteral_strategy = st.builds(
    mt::expressions::StringLiteral,
    value=
        safe_text
)
FilePath_strategy = st.builds(
    FilePath,
)
Statement_strategy = st.builds(
    Statement,
)
mt::statements::For_strategy = st.builds(
    mt::statements::For,
)
mt::statements::If_strategy = st.builds(
    mt::statements::If,
)
mt::statements::Text_strategy = st.builds(
    mt::statements::Text,
    value=
        safe_text
)
mt::statements::Comment_strategy = st.builds(
    mt::statements::Comment,
    value=
        safe_text
)
mt::statements::Feature_strategy = st.builds(
    mt::statements::Feature,
)
ScriptDescriptor_strategy = st.builds(
    ScriptDescriptor,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
mt::statements::Statement_strategy = st.builds(
    mt::statements::Statement,
)
mt::expressions::Call_strategy = st.builds(
    mt::expressions::Call,
    prefix=
        safe_text,
    name=
        safe_text
)
mt::core::ScriptDescriptor_strategy = st.builds(
    mt::core::ScriptDescriptor,
    description=
        safe_text,
    type=
        safe_text,
    name=
        safe_text
)
mt::expressions::Expression_strategy = st.builds(
    mt::expressions::Expression,
)
mt::core::Script_strategy = st.builds(
    mt::core::Script,
)
Script_strategy = st.builds(
    Script,
)
core::mt::Resource_strategy = st.builds(
    core::mt::Resource,
)
Resource_strategy = st.builds(
    Resource,
)
mt::core::Template_strategy = st.builds(
    mt::core::Template,
    endTag=
        safe_text,
    beginTag=
        safe_text
)
mt::core::ASTNode_strategy = st.builds(
    mt::core::ASTNode,
    end=
        st.integers(),
    begin=
        st.integers()
)
mt::core::Method_strategy = st.builds(
    mt::core::Method,
    return_=
        safe_text,
    name=
        safe_text
)
Method_strategy = st.builds(
    Method,
)
mt::core::Service_strategy = st.builds(
    mt::core::Service,
)
mt::core::Metamodel_strategy = st.builds(
    mt::core::Metamodel,
    packageClass=
        safe_text
)
mt::core::FilePath_strategy = st.builds(
    mt::core::FilePath,
)
Expression_strategy = st.builds(
    Expression,
)
mt::expressions::Not_strategy = st.builds(
    mt::expressions::Not,
)
mt::expressions::Operator_strategy = st.builds(
    mt::expressions::Operator,
    operator=
        safe_text
)
mt::expressions::CallSet_strategy = st.builds(
    mt::expressions::CallSet,
)
mt::expressions::Parenthesis_strategy = st.builds(
    mt::expressions::Parenthesis,
)
mt::expressions::Literal_strategy = st.builds(
    mt::expressions::Literal,
)
mt::Resource_strategy = st.builds(
    mt::Resource,
    name=
        safe_text
)
mt::ResourceSet_strategy = st.builds(
    mt::ResourceSet,
)

@given(instance=If_strategy)
@settings(max_examples=50)
def test_if_instantiation(instance):
    assert isinstance(instance, If)

@given(instance=Call_strategy)
@settings(max_examples=50)
def test_call_instantiation(instance):
    assert isinstance(instance, Call)

@given(instance=mt::core::Parameter_strategy)
@settings(max_examples=50)
def test_mt::core::parameter_instantiation(instance):
    assert isinstance(instance, mt::core::Parameter)

@given(instance=mt::core::Parameter_strategy)
def test_mt::core::parameter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=mt::core::Parameter_strategy)
def test_mt::core::parameter_type_setter(instance):
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

@given(instance=mt::expressions::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_mt::expressions::integerliteral_instantiation(instance):
    assert isinstance(instance, mt::expressions::IntegerLiteral)

@given(instance=mt::expressions::IntegerLiteral_strategy)
def test_mt::expressions::integerliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=mt::expressions::IntegerLiteral_strategy)
def test_mt::expressions::integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mt::expressions::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_mt::expressions::booleanliteral_instantiation(instance):
    assert isinstance(instance, mt::expressions::BooleanLiteral)

@given(instance=mt::expressions::BooleanLiteral_strategy)
def test_mt::expressions::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=mt::expressions::BooleanLiteral_strategy)
def test_mt::expressions::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mt::expressions::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_mt::expressions::doubleliteral_instantiation(instance):
    assert isinstance(instance, mt::expressions::DoubleLiteral)

@given(instance=mt::expressions::DoubleLiteral_strategy)
def test_mt::expressions::doubleliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=mt::expressions::DoubleLiteral_strategy)
def test_mt::expressions::doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mt::expressions::NullLiteral_strategy)
@settings(max_examples=50)
def test_mt::expressions::nullliteral_instantiation(instance):
    assert isinstance(instance, mt::expressions::NullLiteral)

@given(instance=mt::expressions::StringLiteral_strategy)
@settings(max_examples=50)
def test_mt::expressions::stringliteral_instantiation(instance):
    assert isinstance(instance, mt::expressions::StringLiteral)

@given(instance=mt::expressions::StringLiteral_strategy)
def test_mt::expressions::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mt::expressions::StringLiteral_strategy)
def test_mt::expressions::stringliteral_value_setter(instance):
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

@given(instance=mt::statements::For_strategy)
@settings(max_examples=50)
def test_mt::statements::for_instantiation(instance):
    assert isinstance(instance, mt::statements::For)

@given(instance=mt::statements::If_strategy)
@settings(max_examples=50)
def test_mt::statements::if_instantiation(instance):
    assert isinstance(instance, mt::statements::If)

@given(instance=mt::statements::Text_strategy)
@settings(max_examples=50)
def test_mt::statements::text_instantiation(instance):
    assert isinstance(instance, mt::statements::Text)

@given(instance=mt::statements::Text_strategy)
def test_mt::statements::text_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mt::statements::Text_strategy)
def test_mt::statements::text_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mt::statements::Comment_strategy)
@settings(max_examples=50)
def test_mt::statements::comment_instantiation(instance):
    assert isinstance(instance, mt::statements::Comment)

@given(instance=mt::statements::Comment_strategy)
def test_mt::statements::comment_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=mt::statements::Comment_strategy)
def test_mt::statements::comment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mt::statements::Feature_strategy)
@settings(max_examples=50)
def test_mt::statements::feature_instantiation(instance):
    assert isinstance(instance, mt::statements::Feature)

@given(instance=ScriptDescriptor_strategy)
@settings(max_examples=50)
def test_scriptdescriptor_instantiation(instance):
    assert isinstance(instance, ScriptDescriptor)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=mt::statements::Statement_strategy)
@settings(max_examples=50)
def test_mt::statements::statement_instantiation(instance):
    assert isinstance(instance, mt::statements::Statement)

@given(instance=mt::expressions::Call_strategy)
@settings(max_examples=50)
def test_mt::expressions::call_instantiation(instance):
    assert isinstance(instance, mt::expressions::Call)

@given(instance=mt::expressions::Call_strategy)
def test_mt::expressions::call_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=mt::expressions::Call_strategy)
def test_mt::expressions::call_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=mt::expressions::Call_strategy)
def test_mt::expressions::call_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mt::expressions::Call_strategy)
def test_mt::expressions::call_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mt::core::ScriptDescriptor_strategy)
@settings(max_examples=50)
def test_mt::core::scriptdescriptor_instantiation(instance):
    assert isinstance(instance, mt::core::ScriptDescriptor)

@given(instance=mt::core::ScriptDescriptor_strategy)
def test_mt::core::scriptdescriptor_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=mt::core::ScriptDescriptor_strategy)
def test_mt::core::scriptdescriptor_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=mt::core::ScriptDescriptor_strategy)
def test_mt::core::scriptdescriptor_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=mt::core::ScriptDescriptor_strategy)
def test_mt::core::scriptdescriptor_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mt::core::ScriptDescriptor_strategy)
def test_mt::core::scriptdescriptor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mt::core::ScriptDescriptor_strategy)
def test_mt::core::scriptdescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mt::expressions::Expression_strategy)
@settings(max_examples=50)
def test_mt::expressions::expression_instantiation(instance):
    assert isinstance(instance, mt::expressions::Expression)

@given(instance=mt::core::Script_strategy)
@settings(max_examples=50)
def test_mt::core::script_instantiation(instance):
    assert isinstance(instance, mt::core::Script)

@given(instance=Script_strategy)
@settings(max_examples=50)
def test_script_instantiation(instance):
    assert isinstance(instance, Script)

@given(instance=core::mt::Resource_strategy)
@settings(max_examples=50)
def test_core::mt::resource_instantiation(instance):
    assert isinstance(instance, core::mt::Resource)

@given(instance=Resource_strategy)
@settings(max_examples=50)
def test_resource_instantiation(instance):
    assert isinstance(instance, Resource)

@given(instance=mt::core::Template_strategy)
@settings(max_examples=50)
def test_mt::core::template_instantiation(instance):
    assert isinstance(instance, mt::core::Template)

@given(instance=mt::core::Template_strategy)
def test_mt::core::template_endTag_type(instance):
    assert isinstance(instance.endTag, str)


@given(instance=mt::core::Template_strategy)
def test_mt::core::template_endTag_setter(instance):
    original = instance.endTag
    instance.endTag = original
    assert instance.endTag == original

@given(instance=mt::core::Template_strategy)
def test_mt::core::template_beginTag_type(instance):
    assert isinstance(instance.beginTag, str)


@given(instance=mt::core::Template_strategy)
def test_mt::core::template_beginTag_setter(instance):
    original = instance.beginTag
    instance.beginTag = original
    assert instance.beginTag == original

@given(instance=mt::core::ASTNode_strategy)
@settings(max_examples=50)
def test_mt::core::astnode_instantiation(instance):
    assert isinstance(instance, mt::core::ASTNode)

@given(instance=mt::core::ASTNode_strategy)
def test_mt::core::astnode_end_type(instance):
    assert isinstance(instance.end, int)


@given(instance=mt::core::ASTNode_strategy)
def test_mt::core::astnode_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=mt::core::ASTNode_strategy)
def test_mt::core::astnode_begin_type(instance):
    assert isinstance(instance.begin, int)


@given(instance=mt::core::ASTNode_strategy)
def test_mt::core::astnode_begin_setter(instance):
    original = instance.begin
    instance.begin = original
    assert instance.begin == original

@given(instance=mt::core::Method_strategy)
@settings(max_examples=50)
def test_mt::core::method_instantiation(instance):
    assert isinstance(instance, mt::core::Method)

@given(instance=mt::core::Method_strategy)
def test_mt::core::method_return__type(instance):
    assert isinstance(instance.return_, str)


@given(instance=mt::core::Method_strategy)
def test_mt::core::method_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=mt::core::Method_strategy)
def test_mt::core::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mt::core::Method_strategy)
def test_mt::core::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=mt::core::Service_strategy)
@settings(max_examples=50)
def test_mt::core::service_instantiation(instance):
    assert isinstance(instance, mt::core::Service)

@given(instance=mt::core::Metamodel_strategy)
@settings(max_examples=50)
def test_mt::core::metamodel_instantiation(instance):
    assert isinstance(instance, mt::core::Metamodel)

@given(instance=mt::core::Metamodel_strategy)
def test_mt::core::metamodel_packageClass_type(instance):
    assert isinstance(instance.packageClass, str)


@given(instance=mt::core::Metamodel_strategy)
def test_mt::core::metamodel_packageClass_setter(instance):
    original = instance.packageClass
    instance.packageClass = original
    assert instance.packageClass == original

@given(instance=mt::core::FilePath_strategy)
@settings(max_examples=50)
def test_mt::core::filepath_instantiation(instance):
    assert isinstance(instance, mt::core::FilePath)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mt::expressions::Not_strategy)
@settings(max_examples=50)
def test_mt::expressions::not_instantiation(instance):
    assert isinstance(instance, mt::expressions::Not)

@given(instance=mt::expressions::Operator_strategy)
@settings(max_examples=50)
def test_mt::expressions::operator_instantiation(instance):
    assert isinstance(instance, mt::expressions::Operator)

@given(instance=mt::expressions::Operator_strategy)
def test_mt::expressions::operator_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=mt::expressions::Operator_strategy)
def test_mt::expressions::operator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=mt::expressions::CallSet_strategy)
@settings(max_examples=50)
def test_mt::expressions::callset_instantiation(instance):
    assert isinstance(instance, mt::expressions::CallSet)

@given(instance=mt::expressions::Parenthesis_strategy)
@settings(max_examples=50)
def test_mt::expressions::parenthesis_instantiation(instance):
    assert isinstance(instance, mt::expressions::Parenthesis)

@given(instance=mt::expressions::Literal_strategy)
@settings(max_examples=50)
def test_mt::expressions::literal_instantiation(instance):
    assert isinstance(instance, mt::expressions::Literal)

@given(instance=mt::Resource_strategy)
@settings(max_examples=50)
def test_mt::resource_instantiation(instance):
    assert isinstance(instance, mt::Resource)

@given(instance=mt::Resource_strategy)
def test_mt::resource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mt::Resource_strategy)
def test_mt::resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mt::ResourceSet_strategy)
@settings(max_examples=50)
def test_mt::resourceset_instantiation(instance):
    assert isinstance(instance, mt::ResourceSet)
