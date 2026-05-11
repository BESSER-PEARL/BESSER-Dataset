import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ConstantExpression,
    simplejava::BooleanExpression,
    simplejava::StringExpression,
    simplejava::IntegerExpression,
    simplejava::NullExpression,
    GenericExpression,
    simplejava::ConstantExpression,
    simplejava::VariableExpression,
    simplejava::UnaryExpression,
    simplejava::ParanthesisOrBinaryExpression,
    simplejava::GenericExpression,
    SimpleVariableDeclaration,
    SimpleStatement,
    simplejava::SimpleVariableDeclaration,
    simplejava::SimpleStatement,
    simplejava::Statement,
    Statement,
    simplejava::Assignment,
    simplejava::VariableDeclaration,
    simplejava::WhileStatement,
    simplejava::IfStatement,
    simplejava::ForStatement,
    simplejava::ForInStatement,
    simplejava::ReturnStatement,
    simplejava::MethodCall,
    simplejava::MethodBlock,
    simplejava::Type,
    simplejava::Method,
    simplejava::Parameter,
    simplejava::ClassDeclaration,
    simplejava::Import,
    simplejava::PackageDeclaration,
    simplejava::SimpleJava,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_constantexpression_is_not_abstract():
    assert not inspect.isabstract(ConstantExpression)


def test_constantexpression_constructor_exists():
    assert callable(ConstantExpression.__init__)


def test_constantexpression_constructor_args():
    sig = inspect.signature(ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava::BooleanExpression)


def test_simplejava::booleanexpression_constructor_exists():
    assert callable(simplejava::BooleanExpression.__init__)


def test_simplejava::booleanexpression_constructor_args():
    sig = inspect.signature(simplejava::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simplejava::booleanexpression_has_value():
    assert hasattr(simplejava::BooleanExpression, "value")
    descriptor = None
    for klass in simplejava::BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::stringexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava::StringExpression)


def test_simplejava::stringexpression_constructor_exists():
    assert callable(simplejava::StringExpression.__init__)


def test_simplejava::stringexpression_constructor_args():
    sig = inspect.signature(simplejava::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simplejava::stringexpression_has_value():
    assert hasattr(simplejava::StringExpression, "value")
    descriptor = None
    for klass in simplejava::StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::integerexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava::IntegerExpression)


def test_simplejava::integerexpression_constructor_exists():
    assert callable(simplejava::IntegerExpression.__init__)


def test_simplejava::integerexpression_constructor_args():
    sig = inspect.signature(simplejava::IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simplejava::integerexpression_has_value():
    assert hasattr(simplejava::IntegerExpression, "value")
    descriptor = None
    for klass in simplejava::IntegerExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::nullexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava::NullExpression)


def test_simplejava::nullexpression_constructor_exists():
    assert callable(simplejava::NullExpression.__init__)


def test_simplejava::nullexpression_constructor_args():
    sig = inspect.signature(simplejava::NullExpression.__init__)
    params = list(sig.parameters.keys())



def test_genericexpression_is_not_abstract():
    assert not inspect.isabstract(GenericExpression)


def test_genericexpression_constructor_exists():
    assert callable(GenericExpression.__init__)


def test_genericexpression_constructor_args():
    sig = inspect.signature(GenericExpression.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::constantexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava::ConstantExpression)


def test_simplejava::constantexpression_constructor_exists():
    assert callable(simplejava::ConstantExpression.__init__)


def test_simplejava::constantexpression_constructor_args():
    sig = inspect.signature(simplejava::ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::variableexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava::VariableExpression)


def test_simplejava::variableexpression_constructor_exists():
    assert callable(simplejava::VariableExpression.__init__)


def test_simplejava::variableexpression_constructor_args():
    sig = inspect.signature(simplejava::VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava::UnaryExpression)


def test_simplejava::unaryexpression_constructor_exists():
    assert callable(simplejava::UnaryExpression.__init__)


def test_simplejava::unaryexpression_constructor_args():
    sig = inspect.signature(simplejava::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_simplejava::unaryexpression_has_type():
    assert hasattr(simplejava::UnaryExpression, "type")
    descriptor = None
    for klass in simplejava::UnaryExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::paranthesisorbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava::ParanthesisOrBinaryExpression)


def test_simplejava::paranthesisorbinaryexpression_constructor_exists():
    assert callable(simplejava::ParanthesisOrBinaryExpression.__init__)


def test_simplejava::paranthesisorbinaryexpression_constructor_args():
    sig = inspect.signature(simplejava::ParanthesisOrBinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_simplejava::paranthesisorbinaryexpression_has_type():
    assert hasattr(simplejava::ParanthesisOrBinaryExpression, "type")
    descriptor = None
    for klass in simplejava::ParanthesisOrBinaryExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::genericexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava::GenericExpression)


def test_simplejava::genericexpression_constructor_exists():
    assert callable(simplejava::GenericExpression.__init__)


def test_simplejava::genericexpression_constructor_args():
    sig = inspect.signature(simplejava::GenericExpression.__init__)
    params = list(sig.parameters.keys())



def test_simplevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(SimpleVariableDeclaration)


def test_simplevariabledeclaration_constructor_exists():
    assert callable(SimpleVariableDeclaration.__init__)


def test_simplevariabledeclaration_constructor_args():
    sig = inspect.signature(SimpleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::simplevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(simplejava::SimpleVariableDeclaration)


def test_simplejava::simplevariabledeclaration_constructor_exists():
    assert callable(simplejava::SimpleVariableDeclaration.__init__)


def test_simplejava::simplevariabledeclaration_constructor_args():
    sig = inspect.signature(simplejava::SimpleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::simplestatement_is_not_abstract():
    assert not inspect.isabstract(simplejava::SimpleStatement)


def test_simplejava::simplestatement_constructor_exists():
    assert callable(simplejava::SimpleStatement.__init__)


def test_simplejava::simplestatement_constructor_args():
    sig = inspect.signature(simplejava::SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::statement_is_not_abstract():
    assert not inspect.isabstract(simplejava::Statement)


def test_simplejava::statement_constructor_exists():
    assert callable(simplejava::Statement.__init__)


def test_simplejava::statement_constructor_args():
    sig = inspect.signature(simplejava::Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::assignment_is_not_abstract():
    assert not inspect.isabstract(simplejava::Assignment)


def test_simplejava::assignment_constructor_exists():
    assert callable(simplejava::Assignment.__init__)


def test_simplejava::assignment_constructor_args():
    sig = inspect.signature(simplejava::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(simplejava::VariableDeclaration)


def test_simplejava::variabledeclaration_constructor_exists():
    assert callable(simplejava::VariableDeclaration.__init__)


def test_simplejava::variabledeclaration_constructor_args():
    sig = inspect.signature(simplejava::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::whilestatement_is_not_abstract():
    assert not inspect.isabstract(simplejava::WhileStatement)


def test_simplejava::whilestatement_constructor_exists():
    assert callable(simplejava::WhileStatement.__init__)


def test_simplejava::whilestatement_constructor_args():
    sig = inspect.signature(simplejava::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::ifstatement_is_not_abstract():
    assert not inspect.isabstract(simplejava::IfStatement)


def test_simplejava::ifstatement_constructor_exists():
    assert callable(simplejava::IfStatement.__init__)


def test_simplejava::ifstatement_constructor_args():
    sig = inspect.signature(simplejava::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::forstatement_is_not_abstract():
    assert not inspect.isabstract(simplejava::ForStatement)


def test_simplejava::forstatement_constructor_exists():
    assert callable(simplejava::ForStatement.__init__)


def test_simplejava::forstatement_constructor_args():
    sig = inspect.signature(simplejava::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::forinstatement_is_not_abstract():
    assert not inspect.isabstract(simplejava::ForInStatement)


def test_simplejava::forinstatement_constructor_exists():
    assert callable(simplejava::ForInStatement.__init__)


def test_simplejava::forinstatement_constructor_args():
    sig = inspect.signature(simplejava::ForInStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::returnstatement_is_not_abstract():
    assert not inspect.isabstract(simplejava::ReturnStatement)


def test_simplejava::returnstatement_constructor_exists():
    assert callable(simplejava::ReturnStatement.__init__)


def test_simplejava::returnstatement_constructor_args():
    sig = inspect.signature(simplejava::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava::methodcall_is_not_abstract():
    assert not inspect.isabstract(simplejava::MethodCall)


def test_simplejava::methodcall_constructor_exists():
    assert callable(simplejava::MethodCall.__init__)


def test_simplejava::methodcall_constructor_args():
    sig = inspect.signature(simplejava::MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "methodName" in params, "Missing parameter 'methodName'"
    assert "thisObject" in params, "Missing parameter 'thisObject'"

def test_simplejava::methodcall_has_methodName():
    assert hasattr(simplejava::MethodCall, "methodName")
    descriptor = None
    for klass in simplejava::MethodCall.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)

def test_simplejava::methodcall_has_thisObject():
    assert hasattr(simplejava::MethodCall, "thisObject")
    descriptor = None
    for klass in simplejava::MethodCall.__mro__:
        if "thisObject" in klass.__dict__:
            descriptor = klass.__dict__["thisObject"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::methodblock_is_not_abstract():
    assert not inspect.isabstract(simplejava::MethodBlock)


def test_simplejava::methodblock_constructor_exists():
    assert callable(simplejava::MethodBlock.__init__)


def test_simplejava::methodblock_constructor_args():
    sig = inspect.signature(simplejava::MethodBlock.__init__)
    params = list(sig.parameters.keys())
    assert "generated" in params, "Missing parameter 'generated'"

def test_simplejava::methodblock_has_generated():
    assert hasattr(simplejava::MethodBlock, "generated")
    descriptor = None
    for klass in simplejava::MethodBlock.__mro__:
        if "generated" in klass.__dict__:
            descriptor = klass.__dict__["generated"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::type_is_not_abstract():
    assert not inspect.isabstract(simplejava::Type)


def test_simplejava::type_constructor_exists():
    assert callable(simplejava::Type.__init__)


def test_simplejava::type_constructor_args():
    sig = inspect.signature(simplejava::Type.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_simplejava::type_has_typeName():
    assert hasattr(simplejava::Type, "typeName")
    descriptor = None
    for klass in simplejava::Type.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::method_is_not_abstract():
    assert not inspect.isabstract(simplejava::Method)


def test_simplejava::method_constructor_exists():
    assert callable(simplejava::Method.__init__)


def test_simplejava::method_constructor_args():
    sig = inspect.signature(simplejava::Method.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "name" in params, "Missing parameter 'name'"

def test_simplejava::method_has_static():
    assert hasattr(simplejava::Method, "static")
    descriptor = None
    for klass in simplejava::Method.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_simplejava::method_has_name():
    assert hasattr(simplejava::Method, "name")
    descriptor = None
    for klass in simplejava::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::parameter_is_not_abstract():
    assert not inspect.isabstract(simplejava::Parameter)


def test_simplejava::parameter_constructor_exists():
    assert callable(simplejava::Parameter.__init__)


def test_simplejava::parameter_constructor_args():
    sig = inspect.signature(simplejava::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplejava::parameter_has_name():
    assert hasattr(simplejava::Parameter, "name")
    descriptor = None
    for klass in simplejava::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::classdeclaration_is_not_abstract():
    assert not inspect.isabstract(simplejava::ClassDeclaration)


def test_simplejava::classdeclaration_constructor_exists():
    assert callable(simplejava::ClassDeclaration.__init__)


def test_simplejava::classdeclaration_constructor_args():
    sig = inspect.signature(simplejava::ClassDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplejava::classdeclaration_has_name():
    assert hasattr(simplejava::ClassDeclaration, "name")
    descriptor = None
    for klass in simplejava::ClassDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::import_is_not_abstract():
    assert not inspect.isabstract(simplejava::Import)


def test_simplejava::import_constructor_exists():
    assert callable(simplejava::Import.__init__)


def test_simplejava::import_constructor_args():
    sig = inspect.signature(simplejava::Import.__init__)
    params = list(sig.parameters.keys())
    assert "imported" in params, "Missing parameter 'imported'"

def test_simplejava::import_has_imported():
    assert hasattr(simplejava::Import, "imported")
    descriptor = None
    for klass in simplejava::Import.__mro__:
        if "imported" in klass.__dict__:
            descriptor = klass.__dict__["imported"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(simplejava::PackageDeclaration)


def test_simplejava::packagedeclaration_constructor_exists():
    assert callable(simplejava::PackageDeclaration.__init__)


def test_simplejava::packagedeclaration_constructor_args():
    sig = inspect.signature(simplejava::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplejava::packagedeclaration_has_name():
    assert hasattr(simplejava::PackageDeclaration, "name")
    descriptor = None
    for klass in simplejava::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplejava::simplejava_is_not_abstract():
    assert not inspect.isabstract(simplejava::SimpleJava)


def test_simplejava::simplejava_constructor_exists():
    assert callable(simplejava::SimpleJava.__init__)


def test_simplejava::simplejava_constructor_args():
    sig = inspect.signature(simplejava::SimpleJava.__init__)
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
ConstantExpression_strategy = st.builds(
    ConstantExpression,
)
simplejava::BooleanExpression_strategy = st.builds(
    simplejava::BooleanExpression,
    value=
        st.booleans()
)
simplejava::StringExpression_strategy = st.builds(
    simplejava::StringExpression,
    value=
        safe_text
)
simplejava::IntegerExpression_strategy = st.builds(
    simplejava::IntegerExpression,
    value=
        st.integers()
)
simplejava::NullExpression_strategy = st.builds(
    simplejava::NullExpression,
)
GenericExpression_strategy = st.builds(
    GenericExpression,
)
simplejava::ConstantExpression_strategy = st.builds(
    simplejava::ConstantExpression,
)
simplejava::VariableExpression_strategy = st.builds(
    simplejava::VariableExpression,
)
simplejava::UnaryExpression_strategy = st.builds(
    simplejava::UnaryExpression,
    type=
        safe_text
)
simplejava::ParanthesisOrBinaryExpression_strategy = st.builds(
    simplejava::ParanthesisOrBinaryExpression,
    type=
        safe_text
)
simplejava::GenericExpression_strategy = st.builds(
    simplejava::GenericExpression,
)
SimpleVariableDeclaration_strategy = st.builds(
    SimpleVariableDeclaration,
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
simplejava::SimpleVariableDeclaration_strategy = st.builds(
    simplejava::SimpleVariableDeclaration,
)
simplejava::SimpleStatement_strategy = st.builds(
    simplejava::SimpleStatement,
)
simplejava::Statement_strategy = st.builds(
    simplejava::Statement,
)
Statement_strategy = st.builds(
    Statement,
)
simplejava::Assignment_strategy = st.builds(
    simplejava::Assignment,
)
simplejava::VariableDeclaration_strategy = st.builds(
    simplejava::VariableDeclaration,
)
simplejava::WhileStatement_strategy = st.builds(
    simplejava::WhileStatement,
)
simplejava::IfStatement_strategy = st.builds(
    simplejava::IfStatement,
)
simplejava::ForStatement_strategy = st.builds(
    simplejava::ForStatement,
)
simplejava::ForInStatement_strategy = st.builds(
    simplejava::ForInStatement,
)
simplejava::ReturnStatement_strategy = st.builds(
    simplejava::ReturnStatement,
)
simplejava::MethodCall_strategy = st.builds(
    simplejava::MethodCall,
    methodName=
        safe_text,
    thisObject=
        st.booleans()
)
simplejava::MethodBlock_strategy = st.builds(
    simplejava::MethodBlock,
    generated=
        st.booleans()
)
simplejava::Type_strategy = st.builds(
    simplejava::Type,
    typeName=
        safe_text
)
simplejava::Method_strategy = st.builds(
    simplejava::Method,
    static=
        st.booleans(),
    name=
        safe_text
)
simplejava::Parameter_strategy = st.builds(
    simplejava::Parameter,
    name=
        safe_text
)
simplejava::ClassDeclaration_strategy = st.builds(
    simplejava::ClassDeclaration,
    name=
        safe_text
)
simplejava::Import_strategy = st.builds(
    simplejava::Import,
    imported=
        safe_text
)
simplejava::PackageDeclaration_strategy = st.builds(
    simplejava::PackageDeclaration,
    name=
        safe_text
)
simplejava::SimpleJava_strategy = st.builds(
    simplejava::SimpleJava,
)

@given(instance=ConstantExpression_strategy)
@settings(max_examples=50)
def test_constantexpression_instantiation(instance):
    assert isinstance(instance, ConstantExpression)

@given(instance=simplejava::BooleanExpression_strategy)
@settings(max_examples=50)
def test_simplejava::booleanexpression_instantiation(instance):
    assert isinstance(instance, simplejava::BooleanExpression)

@given(instance=simplejava::BooleanExpression_strategy)
def test_simplejava::booleanexpression_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=simplejava::BooleanExpression_strategy)
def test_simplejava::booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simplejava::StringExpression_strategy)
@settings(max_examples=50)
def test_simplejava::stringexpression_instantiation(instance):
    assert isinstance(instance, simplejava::StringExpression)

@given(instance=simplejava::StringExpression_strategy)
def test_simplejava::stringexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=simplejava::StringExpression_strategy)
def test_simplejava::stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simplejava::IntegerExpression_strategy)
@settings(max_examples=50)
def test_simplejava::integerexpression_instantiation(instance):
    assert isinstance(instance, simplejava::IntegerExpression)

@given(instance=simplejava::IntegerExpression_strategy)
def test_simplejava::integerexpression_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=simplejava::IntegerExpression_strategy)
def test_simplejava::integerexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simplejava::NullExpression_strategy)
@settings(max_examples=50)
def test_simplejava::nullexpression_instantiation(instance):
    assert isinstance(instance, simplejava::NullExpression)

@given(instance=GenericExpression_strategy)
@settings(max_examples=50)
def test_genericexpression_instantiation(instance):
    assert isinstance(instance, GenericExpression)

@given(instance=simplejava::ConstantExpression_strategy)
@settings(max_examples=50)
def test_simplejava::constantexpression_instantiation(instance):
    assert isinstance(instance, simplejava::ConstantExpression)

@given(instance=simplejava::VariableExpression_strategy)
@settings(max_examples=50)
def test_simplejava::variableexpression_instantiation(instance):
    assert isinstance(instance, simplejava::VariableExpression)

@given(instance=simplejava::UnaryExpression_strategy)
@settings(max_examples=50)
def test_simplejava::unaryexpression_instantiation(instance):
    assert isinstance(instance, simplejava::UnaryExpression)

@given(instance=simplejava::UnaryExpression_strategy)
def test_simplejava::unaryexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=simplejava::UnaryExpression_strategy)
def test_simplejava::unaryexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simplejava::ParanthesisOrBinaryExpression_strategy)
@settings(max_examples=50)
def test_simplejava::paranthesisorbinaryexpression_instantiation(instance):
    assert isinstance(instance, simplejava::ParanthesisOrBinaryExpression)

@given(instance=simplejava::ParanthesisOrBinaryExpression_strategy)
def test_simplejava::paranthesisorbinaryexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=simplejava::ParanthesisOrBinaryExpression_strategy)
def test_simplejava::paranthesisorbinaryexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simplejava::GenericExpression_strategy)
@settings(max_examples=50)
def test_simplejava::genericexpression_instantiation(instance):
    assert isinstance(instance, simplejava::GenericExpression)

@given(instance=SimpleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_simplevariabledeclaration_instantiation(instance):
    assert isinstance(instance, SimpleVariableDeclaration)

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=simplejava::SimpleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_simplejava::simplevariabledeclaration_instantiation(instance):
    assert isinstance(instance, simplejava::SimpleVariableDeclaration)

@given(instance=simplejava::SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplejava::simplestatement_instantiation(instance):
    assert isinstance(instance, simplejava::SimpleStatement)

@given(instance=simplejava::Statement_strategy)
@settings(max_examples=50)
def test_simplejava::statement_instantiation(instance):
    assert isinstance(instance, simplejava::Statement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=simplejava::Assignment_strategy)
@settings(max_examples=50)
def test_simplejava::assignment_instantiation(instance):
    assert isinstance(instance, simplejava::Assignment)

@given(instance=simplejava::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_simplejava::variabledeclaration_instantiation(instance):
    assert isinstance(instance, simplejava::VariableDeclaration)

@given(instance=simplejava::WhileStatement_strategy)
@settings(max_examples=50)
def test_simplejava::whilestatement_instantiation(instance):
    assert isinstance(instance, simplejava::WhileStatement)

@given(instance=simplejava::IfStatement_strategy)
@settings(max_examples=50)
def test_simplejava::ifstatement_instantiation(instance):
    assert isinstance(instance, simplejava::IfStatement)

@given(instance=simplejava::ForStatement_strategy)
@settings(max_examples=50)
def test_simplejava::forstatement_instantiation(instance):
    assert isinstance(instance, simplejava::ForStatement)

@given(instance=simplejava::ForInStatement_strategy)
@settings(max_examples=50)
def test_simplejava::forinstatement_instantiation(instance):
    assert isinstance(instance, simplejava::ForInStatement)

@given(instance=simplejava::ReturnStatement_strategy)
@settings(max_examples=50)
def test_simplejava::returnstatement_instantiation(instance):
    assert isinstance(instance, simplejava::ReturnStatement)

@given(instance=simplejava::MethodCall_strategy)
@settings(max_examples=50)
def test_simplejava::methodcall_instantiation(instance):
    assert isinstance(instance, simplejava::MethodCall)

@given(instance=simplejava::MethodCall_strategy)
def test_simplejava::methodcall_methodName_type(instance):
    assert isinstance(instance.methodName, str)


@given(instance=simplejava::MethodCall_strategy)
def test_simplejava::methodcall_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original

@given(instance=simplejava::MethodCall_strategy)
def test_simplejava::methodcall_thisObject_type(instance):
    assert isinstance(instance.thisObject, bool)


@given(instance=simplejava::MethodCall_strategy)
def test_simplejava::methodcall_thisObject_setter(instance):
    original = instance.thisObject
    instance.thisObject = original
    assert instance.thisObject == original

@given(instance=simplejava::MethodBlock_strategy)
@settings(max_examples=50)
def test_simplejava::methodblock_instantiation(instance):
    assert isinstance(instance, simplejava::MethodBlock)

@given(instance=simplejava::MethodBlock_strategy)
def test_simplejava::methodblock_generated_type(instance):
    assert isinstance(instance.generated, bool)


@given(instance=simplejava::MethodBlock_strategy)
def test_simplejava::methodblock_generated_setter(instance):
    original = instance.generated
    instance.generated = original
    assert instance.generated == original

@given(instance=simplejava::Type_strategy)
@settings(max_examples=50)
def test_simplejava::type_instantiation(instance):
    assert isinstance(instance, simplejava::Type)

@given(instance=simplejava::Type_strategy)
def test_simplejava::type_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=simplejava::Type_strategy)
def test_simplejava::type_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=simplejava::Method_strategy)
@settings(max_examples=50)
def test_simplejava::method_instantiation(instance):
    assert isinstance(instance, simplejava::Method)

@given(instance=simplejava::Method_strategy)
def test_simplejava::method_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=simplejava::Method_strategy)
def test_simplejava::method_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=simplejava::Method_strategy)
def test_simplejava::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplejava::Method_strategy)
def test_simplejava::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplejava::Parameter_strategy)
@settings(max_examples=50)
def test_simplejava::parameter_instantiation(instance):
    assert isinstance(instance, simplejava::Parameter)

@given(instance=simplejava::Parameter_strategy)
def test_simplejava::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplejava::Parameter_strategy)
def test_simplejava::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplejava::ClassDeclaration_strategy)
@settings(max_examples=50)
def test_simplejava::classdeclaration_instantiation(instance):
    assert isinstance(instance, simplejava::ClassDeclaration)

@given(instance=simplejava::ClassDeclaration_strategy)
def test_simplejava::classdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplejava::ClassDeclaration_strategy)
def test_simplejava::classdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplejava::Import_strategy)
@settings(max_examples=50)
def test_simplejava::import_instantiation(instance):
    assert isinstance(instance, simplejava::Import)

@given(instance=simplejava::Import_strategy)
def test_simplejava::import_imported_type(instance):
    assert isinstance(instance.imported, str)


@given(instance=simplejava::Import_strategy)
def test_simplejava::import_imported_setter(instance):
    original = instance.imported
    instance.imported = original
    assert instance.imported == original

@given(instance=simplejava::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_simplejava::packagedeclaration_instantiation(instance):
    assert isinstance(instance, simplejava::PackageDeclaration)

@given(instance=simplejava::PackageDeclaration_strategy)
def test_simplejava::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplejava::PackageDeclaration_strategy)
def test_simplejava::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplejava::SimpleJava_strategy)
@settings(max_examples=50)
def test_simplejava::simplejava_instantiation(instance):
    assert isinstance(instance, simplejava::SimpleJava)
