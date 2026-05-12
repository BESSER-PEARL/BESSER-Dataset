import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ConstantExpression,
    simplejava_IntegerExpression,
    simplejava_BooleanExpression,
    simplejava_StringExpression,
    simplejava_NullExpression,
    GenericExpression,
    simplejava_ConstantExpression,
    simplejava_VariableExpression,
    simplejava_UnaryExpression,
    simplejava_ConstructorCall,
    simplejava_ParanthesisOrBinaryExpression,
    SimpleVariableDeclaration,
    SimpleStatement,
    simplejava_SimpleVariableDeclaration,
    simplejava_GenericExpression,
    Parameter,
    simplejava_Attribute,
    simplejava_SimpleParameter,
    simplejava_Type,
    simplejava_Method,
    simplejava_Parameter,
    simplejava_ClassDeclaration,
    simplejava_Import,
    simplejava_PackageDeclaration,
    simplejava_SimpleStatement,
    simplejava_Statement,
    Statement,
    simplejava_WhileStatement,
    simplejava_ForStatement,
    simplejava_Assignment,
    simplejava_VariableDeclaration,
    simplejava_ForInStatement,
    simplejava_IfStatement,
    simplejava_MethodCall,
    simplejava_ReturnStatement,
    simplejava_MethodBlock,
    simplejava_SimpleJava,
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



def test_simplejava_integerexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava_IntegerExpression)


def test_simplejava_integerexpression_constructor_exists():
    assert callable(simplejava_IntegerExpression.__init__)


def test_simplejava_integerexpression_constructor_args():
    sig = inspect.signature(simplejava_IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simplejava_integerexpression_has_value():
    assert hasattr(simplejava_IntegerExpression, "value")
    descriptor = None
    for klass in simplejava_IntegerExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava_BooleanExpression)


def test_simplejava_booleanexpression_constructor_exists():
    assert callable(simplejava_BooleanExpression.__init__)


def test_simplejava_booleanexpression_constructor_args():
    sig = inspect.signature(simplejava_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simplejava_booleanexpression_has_value():
    assert hasattr(simplejava_BooleanExpression, "value")
    descriptor = None
    for klass in simplejava_BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_stringexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava_StringExpression)


def test_simplejava_stringexpression_constructor_exists():
    assert callable(simplejava_StringExpression.__init__)


def test_simplejava_stringexpression_constructor_args():
    sig = inspect.signature(simplejava_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simplejava_stringexpression_has_value():
    assert hasattr(simplejava_StringExpression, "value")
    descriptor = None
    for klass in simplejava_StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_nullexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava_NullExpression)


def test_simplejava_nullexpression_constructor_exists():
    assert callable(simplejava_NullExpression.__init__)


def test_simplejava_nullexpression_constructor_args():
    sig = inspect.signature(simplejava_NullExpression.__init__)
    params = list(sig.parameters.keys())



def test_genericexpression_is_not_abstract():
    assert not inspect.isabstract(GenericExpression)


def test_genericexpression_constructor_exists():
    assert callable(GenericExpression.__init__)


def test_genericexpression_constructor_args():
    sig = inspect.signature(GenericExpression.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_constantexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava_ConstantExpression)


def test_simplejava_constantexpression_constructor_exists():
    assert callable(simplejava_ConstantExpression.__init__)


def test_simplejava_constantexpression_constructor_args():
    sig = inspect.signature(simplejava_ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_variableexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava_VariableExpression)


def test_simplejava_variableexpression_constructor_exists():
    assert callable(simplejava_VariableExpression.__init__)


def test_simplejava_variableexpression_constructor_args():
    sig = inspect.signature(simplejava_VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava_UnaryExpression)


def test_simplejava_unaryexpression_constructor_exists():
    assert callable(simplejava_UnaryExpression.__init__)


def test_simplejava_unaryexpression_constructor_args():
    sig = inspect.signature(simplejava_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_simplejava_unaryexpression_has_type():
    assert hasattr(simplejava_UnaryExpression, "type")
    descriptor = None
    for klass in simplejava_UnaryExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_constructorcall_is_not_abstract():
    assert not inspect.isabstract(simplejava_ConstructorCall)


def test_simplejava_constructorcall_constructor_exists():
    assert callable(simplejava_ConstructorCall.__init__)


def test_simplejava_constructorcall_constructor_args():
    sig = inspect.signature(simplejava_ConstructorCall.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_paranthesisorbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava_ParanthesisOrBinaryExpression)


def test_simplejava_paranthesisorbinaryexpression_constructor_exists():
    assert callable(simplejava_ParanthesisOrBinaryExpression.__init__)


def test_simplejava_paranthesisorbinaryexpression_constructor_args():
    sig = inspect.signature(simplejava_ParanthesisOrBinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_simplejava_paranthesisorbinaryexpression_has_type():
    assert hasattr(simplejava_ParanthesisOrBinaryExpression, "type")
    descriptor = None
    for klass in simplejava_ParanthesisOrBinaryExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



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



def test_simplejava_simplevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(simplejava_SimpleVariableDeclaration)


def test_simplejava_simplevariabledeclaration_constructor_exists():
    assert callable(simplejava_SimpleVariableDeclaration.__init__)


def test_simplejava_simplevariabledeclaration_constructor_args():
    sig = inspect.signature(simplejava_SimpleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_genericexpression_is_not_abstract():
    assert not inspect.isabstract(simplejava_GenericExpression)


def test_simplejava_genericexpression_constructor_exists():
    assert callable(simplejava_GenericExpression.__init__)


def test_simplejava_genericexpression_constructor_args():
    sig = inspect.signature(simplejava_GenericExpression.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_attribute_is_not_abstract():
    assert not inspect.isabstract(simplejava_Attribute)


def test_simplejava_attribute_constructor_exists():
    assert callable(simplejava_Attribute.__init__)


def test_simplejava_attribute_constructor_args():
    sig = inspect.signature(simplejava_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_simpleparameter_is_not_abstract():
    assert not inspect.isabstract(simplejava_SimpleParameter)


def test_simplejava_simpleparameter_constructor_exists():
    assert callable(simplejava_SimpleParameter.__init__)


def test_simplejava_simpleparameter_constructor_args():
    sig = inspect.signature(simplejava_SimpleParameter.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_type_is_not_abstract():
    assert not inspect.isabstract(simplejava_Type)


def test_simplejava_type_constructor_exists():
    assert callable(simplejava_Type.__init__)


def test_simplejava_type_constructor_args():
    sig = inspect.signature(simplejava_Type.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "isVoid" in params, "Missing parameter 'isVoid'"
    assert "isArray" in params, "Missing parameter 'isArray'"

def test_simplejava_type_has_typeName():
    assert hasattr(simplejava_Type, "typeName")
    descriptor = None
    for klass in simplejava_Type.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)

def test_simplejava_type_has_isVoid():
    assert hasattr(simplejava_Type, "isVoid")
    descriptor = None
    for klass in simplejava_Type.__mro__:
        if "isVoid" in klass.__dict__:
            descriptor = klass.__dict__["isVoid"]
            break
    assert isinstance(descriptor, property)

def test_simplejava_type_has_isArray():
    assert hasattr(simplejava_Type, "isArray")
    descriptor = None
    for klass in simplejava_Type.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_method_is_not_abstract():
    assert not inspect.isabstract(simplejava_Method)


def test_simplejava_method_constructor_exists():
    assert callable(simplejava_Method.__init__)


def test_simplejava_method_constructor_args():
    sig = inspect.signature(simplejava_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "static" in params, "Missing parameter 'static'"

def test_simplejava_method_has_name():
    assert hasattr(simplejava_Method, "name")
    descriptor = None
    for klass in simplejava_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplejava_method_has_static():
    assert hasattr(simplejava_Method, "static")
    descriptor = None
    for klass in simplejava_Method.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_parameter_is_not_abstract():
    assert not inspect.isabstract(simplejava_Parameter)


def test_simplejava_parameter_constructor_exists():
    assert callable(simplejava_Parameter.__init__)


def test_simplejava_parameter_constructor_args():
    sig = inspect.signature(simplejava_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplejava_parameter_has_name():
    assert hasattr(simplejava_Parameter, "name")
    descriptor = None
    for klass in simplejava_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(simplejava_ClassDeclaration)


def test_simplejava_classdeclaration_constructor_exists():
    assert callable(simplejava_ClassDeclaration.__init__)


def test_simplejava_classdeclaration_constructor_args():
    sig = inspect.signature(simplejava_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplejava_classdeclaration_has_name():
    assert hasattr(simplejava_ClassDeclaration, "name")
    descriptor = None
    for klass in simplejava_ClassDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_import_is_not_abstract():
    assert not inspect.isabstract(simplejava_Import)


def test_simplejava_import_constructor_exists():
    assert callable(simplejava_Import.__init__)


def test_simplejava_import_constructor_args():
    sig = inspect.signature(simplejava_Import.__init__)
    params = list(sig.parameters.keys())
    assert "imported" in params, "Missing parameter 'imported'"

def test_simplejava_import_has_imported():
    assert hasattr(simplejava_Import, "imported")
    descriptor = None
    for klass in simplejava_Import.__mro__:
        if "imported" in klass.__dict__:
            descriptor = klass.__dict__["imported"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(simplejava_PackageDeclaration)


def test_simplejava_packagedeclaration_constructor_exists():
    assert callable(simplejava_PackageDeclaration.__init__)


def test_simplejava_packagedeclaration_constructor_args():
    sig = inspect.signature(simplejava_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplejava_packagedeclaration_has_name():
    assert hasattr(simplejava_PackageDeclaration, "name")
    descriptor = None
    for klass in simplejava_PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_simplestatement_is_not_abstract():
    assert not inspect.isabstract(simplejava_SimpleStatement)


def test_simplejava_simplestatement_constructor_exists():
    assert callable(simplejava_SimpleStatement.__init__)


def test_simplejava_simplestatement_constructor_args():
    sig = inspect.signature(simplejava_SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_statement_is_not_abstract():
    assert not inspect.isabstract(simplejava_Statement)


def test_simplejava_statement_constructor_exists():
    assert callable(simplejava_Statement.__init__)


def test_simplejava_statement_constructor_args():
    sig = inspect.signature(simplejava_Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_whilestatement_is_not_abstract():
    assert not inspect.isabstract(simplejava_WhileStatement)


def test_simplejava_whilestatement_constructor_exists():
    assert callable(simplejava_WhileStatement.__init__)


def test_simplejava_whilestatement_constructor_args():
    sig = inspect.signature(simplejava_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_forstatement_is_not_abstract():
    assert not inspect.isabstract(simplejava_ForStatement)


def test_simplejava_forstatement_constructor_exists():
    assert callable(simplejava_ForStatement.__init__)


def test_simplejava_forstatement_constructor_args():
    sig = inspect.signature(simplejava_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_assignment_is_not_abstract():
    assert not inspect.isabstract(simplejava_Assignment)


def test_simplejava_assignment_constructor_exists():
    assert callable(simplejava_Assignment.__init__)


def test_simplejava_assignment_constructor_args():
    sig = inspect.signature(simplejava_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(simplejava_VariableDeclaration)


def test_simplejava_variabledeclaration_constructor_exists():
    assert callable(simplejava_VariableDeclaration.__init__)


def test_simplejava_variabledeclaration_constructor_args():
    sig = inspect.signature(simplejava_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_forinstatement_is_not_abstract():
    assert not inspect.isabstract(simplejava_ForInStatement)


def test_simplejava_forinstatement_constructor_exists():
    assert callable(simplejava_ForInStatement.__init__)


def test_simplejava_forinstatement_constructor_args():
    sig = inspect.signature(simplejava_ForInStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_ifstatement_is_not_abstract():
    assert not inspect.isabstract(simplejava_IfStatement)


def test_simplejava_ifstatement_constructor_exists():
    assert callable(simplejava_IfStatement.__init__)


def test_simplejava_ifstatement_constructor_args():
    sig = inspect.signature(simplejava_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_methodcall_is_not_abstract():
    assert not inspect.isabstract(simplejava_MethodCall)


def test_simplejava_methodcall_constructor_exists():
    assert callable(simplejava_MethodCall.__init__)


def test_simplejava_methodcall_constructor_args():
    sig = inspect.signature(simplejava_MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "thisObject" in params, "Missing parameter 'thisObject'"
    assert "methodName" in params, "Missing parameter 'methodName'"

def test_simplejava_methodcall_has_thisObject():
    assert hasattr(simplejava_MethodCall, "thisObject")
    descriptor = None
    for klass in simplejava_MethodCall.__mro__:
        if "thisObject" in klass.__dict__:
            descriptor = klass.__dict__["thisObject"]
            break
    assert isinstance(descriptor, property)

def test_simplejava_methodcall_has_methodName():
    assert hasattr(simplejava_MethodCall, "methodName")
    descriptor = None
    for klass in simplejava_MethodCall.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_returnstatement_is_not_abstract():
    assert not inspect.isabstract(simplejava_ReturnStatement)


def test_simplejava_returnstatement_constructor_exists():
    assert callable(simplejava_ReturnStatement.__init__)


def test_simplejava_returnstatement_constructor_args():
    sig = inspect.signature(simplejava_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_simplejava_methodblock_is_not_abstract():
    assert not inspect.isabstract(simplejava_MethodBlock)


def test_simplejava_methodblock_constructor_exists():
    assert callable(simplejava_MethodBlock.__init__)


def test_simplejava_methodblock_constructor_args():
    sig = inspect.signature(simplejava_MethodBlock.__init__)
    params = list(sig.parameters.keys())
    assert "generated" in params, "Missing parameter 'generated'"

def test_simplejava_methodblock_has_generated():
    assert hasattr(simplejava_MethodBlock, "generated")
    descriptor = None
    for klass in simplejava_MethodBlock.__mro__:
        if "generated" in klass.__dict__:
            descriptor = klass.__dict__["generated"]
            break
    assert isinstance(descriptor, property)



def test_simplejava_simplejava_is_not_abstract():
    assert not inspect.isabstract(simplejava_SimpleJava)


def test_simplejava_simplejava_constructor_exists():
    assert callable(simplejava_SimpleJava.__init__)


def test_simplejava_simplejava_constructor_args():
    sig = inspect.signature(simplejava_SimpleJava.__init__)
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
simplejava_IntegerExpression_strategy = st.builds(
    simplejava_IntegerExpression,
    value=
        st.integers()
)
simplejava_BooleanExpression_strategy = st.builds(
    simplejava_BooleanExpression,
    value=
        st.booleans()
)
simplejava_StringExpression_strategy = st.builds(
    simplejava_StringExpression,
    value=
        safe_text
)
simplejava_NullExpression_strategy = st.builds(
    simplejava_NullExpression,
)
GenericExpression_strategy = st.builds(
    GenericExpression,
)
simplejava_ConstantExpression_strategy = st.builds(
    simplejava_ConstantExpression,
)
simplejava_VariableExpression_strategy = st.builds(
    simplejava_VariableExpression,
)
simplejava_UnaryExpression_strategy = st.builds(
    simplejava_UnaryExpression,
    type=
        safe_text
)
simplejava_ConstructorCall_strategy = st.builds(
    simplejava_ConstructorCall,
)
simplejava_ParanthesisOrBinaryExpression_strategy = st.builds(
    simplejava_ParanthesisOrBinaryExpression,
    type=
        safe_text
)
SimpleVariableDeclaration_strategy = st.builds(
    SimpleVariableDeclaration,
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
simplejava_SimpleVariableDeclaration_strategy = st.builds(
    simplejava_SimpleVariableDeclaration,
)
simplejava_GenericExpression_strategy = st.builds(
    simplejava_GenericExpression,
)
Parameter_strategy = st.builds(
    Parameter,
)
simplejava_Attribute_strategy = st.builds(
    simplejava_Attribute,
)
simplejava_SimpleParameter_strategy = st.builds(
    simplejava_SimpleParameter,
)
simplejava_Type_strategy = st.builds(
    simplejava_Type,
    typeName=
        safe_text,
    isVoid=
        st.booleans(),
    isArray=
        st.booleans()
)
simplejava_Method_strategy = st.builds(
    simplejava_Method,
    name=
        safe_text,
    static=
        st.booleans()
)
simplejava_Parameter_strategy = st.builds(
    simplejava_Parameter,
    name=
        safe_text
)
simplejava_ClassDeclaration_strategy = st.builds(
    simplejava_ClassDeclaration,
    name=
        safe_text
)
simplejava_Import_strategy = st.builds(
    simplejava_Import,
    imported=
        safe_text
)
simplejava_PackageDeclaration_strategy = st.builds(
    simplejava_PackageDeclaration,
    name=
        safe_text
)
simplejava_SimpleStatement_strategy = st.builds(
    simplejava_SimpleStatement,
)
simplejava_Statement_strategy = st.builds(
    simplejava_Statement,
)
Statement_strategy = st.builds(
    Statement,
)
simplejava_WhileStatement_strategy = st.builds(
    simplejava_WhileStatement,
)
simplejava_ForStatement_strategy = st.builds(
    simplejava_ForStatement,
)
simplejava_Assignment_strategy = st.builds(
    simplejava_Assignment,
)
simplejava_VariableDeclaration_strategy = st.builds(
    simplejava_VariableDeclaration,
)
simplejava_ForInStatement_strategy = st.builds(
    simplejava_ForInStatement,
)
simplejava_IfStatement_strategy = st.builds(
    simplejava_IfStatement,
)
simplejava_MethodCall_strategy = st.builds(
    simplejava_MethodCall,
    thisObject=
        st.booleans(),
    methodName=
        safe_text
)
simplejava_ReturnStatement_strategy = st.builds(
    simplejava_ReturnStatement,
)
simplejava_MethodBlock_strategy = st.builds(
    simplejava_MethodBlock,
    generated=
        st.booleans()
)
simplejava_SimpleJava_strategy = st.builds(
    simplejava_SimpleJava,
)

@given(instance=ConstantExpression_strategy)
@settings(max_examples=50)
def test_constantexpression_instantiation(instance):
    assert isinstance(instance, ConstantExpression)

@given(instance=simplejava_IntegerExpression_strategy)
@settings(max_examples=50)
def test_simplejava_integerexpression_instantiation(instance):
    assert isinstance(instance, simplejava_IntegerExpression)



@given(instance=simplejava_IntegerExpression_strategy)
def test_simplejava_integerexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simplejava_BooleanExpression_strategy)
@settings(max_examples=50)
def test_simplejava_booleanexpression_instantiation(instance):
    assert isinstance(instance, simplejava_BooleanExpression)



@given(instance=simplejava_BooleanExpression_strategy)
def test_simplejava_booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simplejava_StringExpression_strategy)
@settings(max_examples=50)
def test_simplejava_stringexpression_instantiation(instance):
    assert isinstance(instance, simplejava_StringExpression)



@given(instance=simplejava_StringExpression_strategy)
def test_simplejava_stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=simplejava_NullExpression_strategy)
@settings(max_examples=50)
def test_simplejava_nullexpression_instantiation(instance):
    assert isinstance(instance, simplejava_NullExpression)

@given(instance=GenericExpression_strategy)
@settings(max_examples=50)
def test_genericexpression_instantiation(instance):
    assert isinstance(instance, GenericExpression)

@given(instance=simplejava_ConstantExpression_strategy)
@settings(max_examples=50)
def test_simplejava_constantexpression_instantiation(instance):
    assert isinstance(instance, simplejava_ConstantExpression)

@given(instance=simplejava_VariableExpression_strategy)
@settings(max_examples=50)
def test_simplejava_variableexpression_instantiation(instance):
    assert isinstance(instance, simplejava_VariableExpression)

@given(instance=simplejava_UnaryExpression_strategy)
@settings(max_examples=50)
def test_simplejava_unaryexpression_instantiation(instance):
    assert isinstance(instance, simplejava_UnaryExpression)



@given(instance=simplejava_UnaryExpression_strategy)
def test_simplejava_unaryexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=simplejava_ConstructorCall_strategy)
@settings(max_examples=50)
def test_simplejava_constructorcall_instantiation(instance):
    assert isinstance(instance, simplejava_ConstructorCall)

@given(instance=simplejava_ParanthesisOrBinaryExpression_strategy)
@settings(max_examples=50)
def test_simplejava_paranthesisorbinaryexpression_instantiation(instance):
    assert isinstance(instance, simplejava_ParanthesisOrBinaryExpression)



@given(instance=simplejava_ParanthesisOrBinaryExpression_strategy)
def test_simplejava_paranthesisorbinaryexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SimpleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_simplevariabledeclaration_instantiation(instance):
    assert isinstance(instance, SimpleVariableDeclaration)

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=simplejava_SimpleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_simplejava_simplevariabledeclaration_instantiation(instance):
    assert isinstance(instance, simplejava_SimpleVariableDeclaration)

@given(instance=simplejava_GenericExpression_strategy)
@settings(max_examples=50)
def test_simplejava_genericexpression_instantiation(instance):
    assert isinstance(instance, simplejava_GenericExpression)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=simplejava_Attribute_strategy)
@settings(max_examples=50)
def test_simplejava_attribute_instantiation(instance):
    assert isinstance(instance, simplejava_Attribute)

@given(instance=simplejava_SimpleParameter_strategy)
@settings(max_examples=50)
def test_simplejava_simpleparameter_instantiation(instance):
    assert isinstance(instance, simplejava_SimpleParameter)

@given(instance=simplejava_Type_strategy)
@settings(max_examples=50)
def test_simplejava_type_instantiation(instance):
    assert isinstance(instance, simplejava_Type)



@given(instance=simplejava_Type_strategy)
def test_simplejava_type_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original



@given(instance=simplejava_Type_strategy)
def test_simplejava_type_isVoid_setter(instance):
    original = instance.isVoid
    instance.isVoid = original
    assert instance.isVoid == original



@given(instance=simplejava_Type_strategy)
def test_simplejava_type_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=simplejava_Method_strategy)
@settings(max_examples=50)
def test_simplejava_method_instantiation(instance):
    assert isinstance(instance, simplejava_Method)



@given(instance=simplejava_Method_strategy)
def test_simplejava_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=simplejava_Method_strategy)
def test_simplejava_method_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=simplejava_Parameter_strategy)
@settings(max_examples=50)
def test_simplejava_parameter_instantiation(instance):
    assert isinstance(instance, simplejava_Parameter)



@given(instance=simplejava_Parameter_strategy)
def test_simplejava_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplejava_ClassDeclaration_strategy)
@settings(max_examples=50)
def test_simplejava_classdeclaration_instantiation(instance):
    assert isinstance(instance, simplejava_ClassDeclaration)



@given(instance=simplejava_ClassDeclaration_strategy)
def test_simplejava_classdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplejava_Import_strategy)
@settings(max_examples=50)
def test_simplejava_import_instantiation(instance):
    assert isinstance(instance, simplejava_Import)



@given(instance=simplejava_Import_strategy)
def test_simplejava_import_imported_setter(instance):
    original = instance.imported
    instance.imported = original
    assert instance.imported == original

@given(instance=simplejava_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_simplejava_packagedeclaration_instantiation(instance):
    assert isinstance(instance, simplejava_PackageDeclaration)



@given(instance=simplejava_PackageDeclaration_strategy)
def test_simplejava_packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplejava_SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplejava_simplestatement_instantiation(instance):
    assert isinstance(instance, simplejava_SimpleStatement)

@given(instance=simplejava_Statement_strategy)
@settings(max_examples=50)
def test_simplejava_statement_instantiation(instance):
    assert isinstance(instance, simplejava_Statement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=simplejava_WhileStatement_strategy)
@settings(max_examples=50)
def test_simplejava_whilestatement_instantiation(instance):
    assert isinstance(instance, simplejava_WhileStatement)

@given(instance=simplejava_ForStatement_strategy)
@settings(max_examples=50)
def test_simplejava_forstatement_instantiation(instance):
    assert isinstance(instance, simplejava_ForStatement)

@given(instance=simplejava_Assignment_strategy)
@settings(max_examples=50)
def test_simplejava_assignment_instantiation(instance):
    assert isinstance(instance, simplejava_Assignment)

@given(instance=simplejava_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_simplejava_variabledeclaration_instantiation(instance):
    assert isinstance(instance, simplejava_VariableDeclaration)

@given(instance=simplejava_ForInStatement_strategy)
@settings(max_examples=50)
def test_simplejava_forinstatement_instantiation(instance):
    assert isinstance(instance, simplejava_ForInStatement)

@given(instance=simplejava_IfStatement_strategy)
@settings(max_examples=50)
def test_simplejava_ifstatement_instantiation(instance):
    assert isinstance(instance, simplejava_IfStatement)

@given(instance=simplejava_MethodCall_strategy)
@settings(max_examples=50)
def test_simplejava_methodcall_instantiation(instance):
    assert isinstance(instance, simplejava_MethodCall)



@given(instance=simplejava_MethodCall_strategy)
def test_simplejava_methodcall_thisObject_setter(instance):
    original = instance.thisObject
    instance.thisObject = original
    assert instance.thisObject == original



@given(instance=simplejava_MethodCall_strategy)
def test_simplejava_methodcall_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original

@given(instance=simplejava_ReturnStatement_strategy)
@settings(max_examples=50)
def test_simplejava_returnstatement_instantiation(instance):
    assert isinstance(instance, simplejava_ReturnStatement)

@given(instance=simplejava_MethodBlock_strategy)
@settings(max_examples=50)
def test_simplejava_methodblock_instantiation(instance):
    assert isinstance(instance, simplejava_MethodBlock)



@given(instance=simplejava_MethodBlock_strategy)
def test_simplejava_methodblock_generated_setter(instance):
    original = instance.generated
    instance.generated = original
    assert instance.generated == original

@given(instance=simplejava_SimpleJava_strategy)
@settings(max_examples=50)
def test_simplejava_simplejava_instantiation(instance):
    assert isinstance(instance, simplejava_SimpleJava)
