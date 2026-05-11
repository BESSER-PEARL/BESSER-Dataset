import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Java::Annotation,
    Java::Statement,
    Java::Field,
    Java::Parameter,
    Annotation,
    Statement,
    Java::Return,
    Java::MethodCall,
    Java::Assignment,
    Java::VariableDeclaration,
    Parameter,
    Java::MethodSignature,
    MethodSignature,
    Java::Method,
    Method,
    Field,
    Class,
    Interface,
    Package,
    Type,
    Java::ObjectType,
    Java::PrimitiveType,
    Java::VoidType,
    Java::Type,
    ObjectType,
    Java::Class,
    Java::Interface,
    Java::Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_java::annotation_is_not_abstract():
    assert not inspect.isabstract(Java::Annotation)


def test_java::annotation_constructor_exists():
    assert callable(Java::Annotation.__init__)


def test_java::annotation_constructor_args():
    sig = inspect.signature(Java::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "sentenceText" in params, "Missing parameter 'sentenceText'"

def test_java::annotation_has_type():
    assert hasattr(Java::Annotation, "type")
    descriptor = None
    for klass in Java::Annotation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_java::annotation_has_sentenceText():
    assert hasattr(Java::Annotation, "sentenceText")
    descriptor = None
    for klass in Java::Annotation.__mro__:
        if "sentenceText" in klass.__dict__:
            descriptor = klass.__dict__["sentenceText"]
            break
    assert isinstance(descriptor, property)



def test_java::statement_is_not_abstract():
    assert not inspect.isabstract(Java::Statement)


def test_java::statement_constructor_exists():
    assert callable(Java::Statement.__init__)


def test_java::statement_constructor_args():
    sig = inspect.signature(Java::Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::field_is_not_abstract():
    assert not inspect.isabstract(Java::Field)


def test_java::field_constructor_exists():
    assert callable(Java::Field.__init__)


def test_java::field_constructor_args():
    sig = inspect.signature(Java::Field.__init__)
    params = list(sig.parameters.keys())
    assert "isPrivate" in params, "Missing parameter 'isPrivate'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isPublic" in params, "Missing parameter 'isPublic'"
    assert "isProtected" in params, "Missing parameter 'isProtected'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_java::field_has_isPrivate():
    assert hasattr(Java::Field, "isPrivate")
    descriptor = None
    for klass in Java::Field.__mro__:
        if "isPrivate" in klass.__dict__:
            descriptor = klass.__dict__["isPrivate"]
            break
    assert isinstance(descriptor, property)

def test_java::field_has_name():
    assert hasattr(Java::Field, "name")
    descriptor = None
    for klass in Java::Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java::field_has_isPublic():
    assert hasattr(Java::Field, "isPublic")
    descriptor = None
    for klass in Java::Field.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)

def test_java::field_has_isProtected():
    assert hasattr(Java::Field, "isProtected")
    descriptor = None
    for klass in Java::Field.__mro__:
        if "isProtected" in klass.__dict__:
            descriptor = klass.__dict__["isProtected"]
            break
    assert isinstance(descriptor, property)

def test_java::field_has_isStatic():
    assert hasattr(Java::Field, "isStatic")
    descriptor = None
    for klass in Java::Field.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_java::parameter_is_not_abstract():
    assert not inspect.isabstract(Java::Parameter)


def test_java::parameter_constructor_exists():
    assert callable(Java::Parameter.__init__)


def test_java::parameter_constructor_args():
    sig = inspect.signature(Java::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::parameter_has_name():
    assert hasattr(Java::Parameter, "name")
    descriptor = None
    for klass in Java::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_java::return_is_not_abstract():
    assert not inspect.isabstract(Java::Return)


def test_java::return_constructor_exists():
    assert callable(Java::Return.__init__)


def test_java::return_constructor_args():
    sig = inspect.signature(Java::Return.__init__)
    params = list(sig.parameters.keys())
    assert "objectId" in params, "Missing parameter 'objectId'"
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_java::return_has_objectId():
    assert hasattr(Java::Return, "objectId")
    descriptor = None
    for klass in Java::Return.__mro__:
        if "objectId" in klass.__dict__:
            descriptor = klass.__dict__["objectId"]
            break
    assert isinstance(descriptor, property)

def test_java::return_has_fieldName():
    assert hasattr(Java::Return, "fieldName")
    descriptor = None
    for klass in Java::Return.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)



def test_java::methodcall_is_not_abstract():
    assert not inspect.isabstract(Java::MethodCall)


def test_java::methodcall_constructor_exists():
    assert callable(Java::MethodCall.__init__)


def test_java::methodcall_constructor_args():
    sig = inspect.signature(Java::MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "methodName" in params, "Missing parameter 'methodName'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_java::methodcall_has_methodName():
    assert hasattr(Java::MethodCall, "methodName")
    descriptor = None
    for klass in Java::MethodCall.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)

def test_java::methodcall_has_variableName():
    assert hasattr(Java::MethodCall, "variableName")
    descriptor = None
    for klass in Java::MethodCall.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_java::assignment_is_not_abstract():
    assert not inspect.isabstract(Java::Assignment)


def test_java::assignment_constructor_exists():
    assert callable(Java::Assignment.__init__)


def test_java::assignment_constructor_args():
    sig = inspect.signature(Java::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "variableExpr" in params, "Missing parameter 'variableExpr'"
    assert "fieldName" in params, "Missing parameter 'fieldName'"
    assert "objectId" in params, "Missing parameter 'objectId'"

def test_java::assignment_has_variableExpr():
    assert hasattr(Java::Assignment, "variableExpr")
    descriptor = None
    for klass in Java::Assignment.__mro__:
        if "variableExpr" in klass.__dict__:
            descriptor = klass.__dict__["variableExpr"]
            break
    assert isinstance(descriptor, property)

def test_java::assignment_has_fieldName():
    assert hasattr(Java::Assignment, "fieldName")
    descriptor = None
    for klass in Java::Assignment.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)

def test_java::assignment_has_objectId():
    assert hasattr(Java::Assignment, "objectId")
    descriptor = None
    for klass in Java::Assignment.__mro__:
        if "objectId" in klass.__dict__:
            descriptor = klass.__dict__["objectId"]
            break
    assert isinstance(descriptor, property)



def test_java::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java::VariableDeclaration)


def test_java::variabledeclaration_constructor_exists():
    assert callable(Java::VariableDeclaration.__init__)


def test_java::variabledeclaration_constructor_args():
    sig = inspect.signature(Java::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_java::variabledeclaration_has_variableName():
    assert hasattr(Java::VariableDeclaration, "variableName")
    descriptor = None
    for klass in Java::VariableDeclaration.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_java::methodsignature_is_not_abstract():
    assert not inspect.isabstract(Java::MethodSignature)


def test_java::methodsignature_constructor_exists():
    assert callable(Java::MethodSignature.__init__)


def test_java::methodsignature_constructor_args():
    sig = inspect.signature(Java::MethodSignature.__init__)
    params = list(sig.parameters.keys())
    assert "isPublic" in params, "Missing parameter 'isPublic'"
    assert "isPrivate" in params, "Missing parameter 'isPrivate'"
    assert "isProtected" in params, "Missing parameter 'isProtected'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_java::methodsignature_has_isPublic():
    assert hasattr(Java::MethodSignature, "isPublic")
    descriptor = None
    for klass in Java::MethodSignature.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)

def test_java::methodsignature_has_isPrivate():
    assert hasattr(Java::MethodSignature, "isPrivate")
    descriptor = None
    for klass in Java::MethodSignature.__mro__:
        if "isPrivate" in klass.__dict__:
            descriptor = klass.__dict__["isPrivate"]
            break
    assert isinstance(descriptor, property)

def test_java::methodsignature_has_isProtected():
    assert hasattr(Java::MethodSignature, "isProtected")
    descriptor = None
    for klass in Java::MethodSignature.__mro__:
        if "isProtected" in klass.__dict__:
            descriptor = klass.__dict__["isProtected"]
            break
    assert isinstance(descriptor, property)

def test_java::methodsignature_has_name():
    assert hasattr(Java::MethodSignature, "name")
    descriptor = None
    for klass in Java::MethodSignature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java::methodsignature_has_isStatic():
    assert hasattr(Java::MethodSignature, "isStatic")
    descriptor = None
    for klass in Java::MethodSignature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_methodsignature_is_not_abstract():
    assert not inspect.isabstract(MethodSignature)


def test_methodsignature_constructor_exists():
    assert callable(MethodSignature.__init__)


def test_methodsignature_constructor_args():
    sig = inspect.signature(MethodSignature.__init__)
    params = list(sig.parameters.keys())



def test_java::method_is_not_abstract():
    assert not inspect.isabstract(Java::Method)


def test_java::method_constructor_exists():
    assert callable(Java::Method.__init__)


def test_java::method_constructor_args():
    sig = inspect.signature(Java::Method.__init__)
    params = list(sig.parameters.keys())



def test_method_is_not_abstract():
    assert not inspect.isabstract(Method)


def test_method_constructor_exists():
    assert callable(Method.__init__)


def test_method_constructor_args():
    sig = inspect.signature(Method.__init__)
    params = list(sig.parameters.keys())



def test_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_field_constructor_exists():
    assert callable(Field.__init__)


def test_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_java::objecttype_is_not_abstract():
    assert not inspect.isabstract(Java::ObjectType)


def test_java::objecttype_constructor_exists():
    assert callable(Java::ObjectType.__init__)


def test_java::objecttype_constructor_args():
    sig = inspect.signature(Java::ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_java::primitivetype_is_not_abstract():
    assert not inspect.isabstract(Java::PrimitiveType)


def test_java::primitivetype_constructor_exists():
    assert callable(Java::PrimitiveType.__init__)


def test_java::primitivetype_constructor_args():
    sig = inspect.signature(Java::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java::voidtype_is_not_abstract():
    assert not inspect.isabstract(Java::VoidType)


def test_java::voidtype_constructor_exists():
    assert callable(Java::VoidType.__init__)


def test_java::voidtype_constructor_args():
    sig = inspect.signature(Java::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_java::type_is_not_abstract():
    assert not inspect.isabstract(Java::Type)


def test_java::type_constructor_exists():
    assert callable(Java::Type.__init__)


def test_java::type_constructor_args():
    sig = inspect.signature(Java::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::type_has_name():
    assert hasattr(Java::Type, "name")
    descriptor = None
    for klass in Java::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_objecttype_is_not_abstract():
    assert not inspect.isabstract(ObjectType)


def test_objecttype_constructor_exists():
    assert callable(ObjectType.__init__)


def test_objecttype_constructor_args():
    sig = inspect.signature(ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_java::class_is_not_abstract():
    assert not inspect.isabstract(Java::Class)


def test_java::class_constructor_exists():
    assert callable(Java::Class.__init__)


def test_java::class_constructor_args():
    sig = inspect.signature(Java::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isPublic" in params, "Missing parameter 'isPublic'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_java::class_has_isPublic():
    assert hasattr(Java::Class, "isPublic")
    descriptor = None
    for klass in Java::Class.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)

def test_java::class_has_isStatic():
    assert hasattr(Java::Class, "isStatic")
    descriptor = None
    for klass in Java::Class.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_java::interface_is_not_abstract():
    assert not inspect.isabstract(Java::Interface)


def test_java::interface_constructor_exists():
    assert callable(Java::Interface.__init__)


def test_java::interface_constructor_args():
    sig = inspect.signature(Java::Interface.__init__)
    params = list(sig.parameters.keys())



def test_java::package_is_not_abstract():
    assert not inspect.isabstract(Java::Package)


def test_java::package_constructor_exists():
    assert callable(Java::Package.__init__)


def test_java::package_constructor_args():
    sig = inspect.signature(Java::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::package_has_name():
    assert hasattr(Java::Package, "name")
    descriptor = None
    for klass in Java::Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
Java::Annotation_strategy = st.builds(
    Java::Annotation,
    type=
        safe_text,
    sentenceText=
        safe_text
)
Java::Statement_strategy = st.builds(
    Java::Statement,
)
Java::Field_strategy = st.builds(
    Java::Field,
    isPrivate=
        st.booleans(),
    name=
        safe_text,
    isPublic=
        st.booleans(),
    isProtected=
        st.booleans(),
    isStatic=
        st.booleans()
)
Java::Parameter_strategy = st.builds(
    Java::Parameter,
    name=
        safe_text
)
Annotation_strategy = st.builds(
    Annotation,
)
Statement_strategy = st.builds(
    Statement,
)
Java::Return_strategy = st.builds(
    Java::Return,
    objectId=
        safe_text,
    fieldName=
        safe_text
)
Java::MethodCall_strategy = st.builds(
    Java::MethodCall,
    methodName=
        safe_text,
    variableName=
        safe_text
)
Java::Assignment_strategy = st.builds(
    Java::Assignment,
    variableExpr=
        safe_text,
    fieldName=
        safe_text,
    objectId=
        safe_text
)
Java::VariableDeclaration_strategy = st.builds(
    Java::VariableDeclaration,
    variableName=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
Java::MethodSignature_strategy = st.builds(
    Java::MethodSignature,
    isPublic=
        st.booleans(),
    isPrivate=
        st.booleans(),
    isProtected=
        st.booleans(),
    name=
        safe_text,
    isStatic=
        st.booleans()
)
MethodSignature_strategy = st.builds(
    MethodSignature,
)
Java::Method_strategy = st.builds(
    Java::Method,
)
Method_strategy = st.builds(
    Method,
)
Field_strategy = st.builds(
    Field,
)
Class_strategy = st.builds(
    Class,
)
Interface_strategy = st.builds(
    Interface,
)
Package_strategy = st.builds(
    Package,
)
Type_strategy = st.builds(
    Type,
)
Java::ObjectType_strategy = st.builds(
    Java::ObjectType,
)
Java::PrimitiveType_strategy = st.builds(
    Java::PrimitiveType,
)
Java::VoidType_strategy = st.builds(
    Java::VoidType,
)
Java::Type_strategy = st.builds(
    Java::Type,
    name=
        safe_text
)
ObjectType_strategy = st.builds(
    ObjectType,
)
Java::Class_strategy = st.builds(
    Java::Class,
    isPublic=
        st.booleans(),
    isStatic=
        st.booleans()
)
Java::Interface_strategy = st.builds(
    Java::Interface,
)
Java::Package_strategy = st.builds(
    Java::Package,
    name=
        safe_text
)

@given(instance=Java::Annotation_strategy)
@settings(max_examples=50)
def test_java::annotation_instantiation(instance):
    assert isinstance(instance, Java::Annotation)

@given(instance=Java::Annotation_strategy)
def test_java::annotation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Java::Annotation_strategy)
def test_java::annotation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Java::Annotation_strategy)
def test_java::annotation_sentenceText_type(instance):
    assert isinstance(instance.sentenceText, str)


@given(instance=Java::Annotation_strategy)
def test_java::annotation_sentenceText_setter(instance):
    original = instance.sentenceText
    instance.sentenceText = original
    assert instance.sentenceText == original

@given(instance=Java::Statement_strategy)
@settings(max_examples=50)
def test_java::statement_instantiation(instance):
    assert isinstance(instance, Java::Statement)

@given(instance=Java::Field_strategy)
@settings(max_examples=50)
def test_java::field_instantiation(instance):
    assert isinstance(instance, Java::Field)

@given(instance=Java::Field_strategy)
def test_java::field_isPrivate_type(instance):
    assert isinstance(instance.isPrivate, bool)


@given(instance=Java::Field_strategy)
def test_java::field_isPrivate_setter(instance):
    original = instance.isPrivate
    instance.isPrivate = original
    assert instance.isPrivate == original

@given(instance=Java::Field_strategy)
def test_java::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Java::Field_strategy)
def test_java::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java::Field_strategy)
def test_java::field_isPublic_type(instance):
    assert isinstance(instance.isPublic, bool)


@given(instance=Java::Field_strategy)
def test_java::field_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original

@given(instance=Java::Field_strategy)
def test_java::field_isProtected_type(instance):
    assert isinstance(instance.isProtected, bool)


@given(instance=Java::Field_strategy)
def test_java::field_isProtected_setter(instance):
    original = instance.isProtected
    instance.isProtected = original
    assert instance.isProtected == original

@given(instance=Java::Field_strategy)
def test_java::field_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=Java::Field_strategy)
def test_java::field_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=Java::Parameter_strategy)
@settings(max_examples=50)
def test_java::parameter_instantiation(instance):
    assert isinstance(instance, Java::Parameter)

@given(instance=Java::Parameter_strategy)
def test_java::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Java::Parameter_strategy)
def test_java::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=Java::Return_strategy)
@settings(max_examples=50)
def test_java::return_instantiation(instance):
    assert isinstance(instance, Java::Return)

@given(instance=Java::Return_strategy)
def test_java::return_objectId_type(instance):
    assert isinstance(instance.objectId, str)


@given(instance=Java::Return_strategy)
def test_java::return_objectId_setter(instance):
    original = instance.objectId
    instance.objectId = original
    assert instance.objectId == original

@given(instance=Java::Return_strategy)
def test_java::return_fieldName_type(instance):
    assert isinstance(instance.fieldName, str)


@given(instance=Java::Return_strategy)
def test_java::return_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=Java::MethodCall_strategy)
@settings(max_examples=50)
def test_java::methodcall_instantiation(instance):
    assert isinstance(instance, Java::MethodCall)

@given(instance=Java::MethodCall_strategy)
def test_java::methodcall_methodName_type(instance):
    assert isinstance(instance.methodName, str)


@given(instance=Java::MethodCall_strategy)
def test_java::methodcall_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original

@given(instance=Java::MethodCall_strategy)
def test_java::methodcall_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=Java::MethodCall_strategy)
def test_java::methodcall_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=Java::Assignment_strategy)
@settings(max_examples=50)
def test_java::assignment_instantiation(instance):
    assert isinstance(instance, Java::Assignment)

@given(instance=Java::Assignment_strategy)
def test_java::assignment_variableExpr_type(instance):
    assert isinstance(instance.variableExpr, str)


@given(instance=Java::Assignment_strategy)
def test_java::assignment_variableExpr_setter(instance):
    original = instance.variableExpr
    instance.variableExpr = original
    assert instance.variableExpr == original

@given(instance=Java::Assignment_strategy)
def test_java::assignment_fieldName_type(instance):
    assert isinstance(instance.fieldName, str)


@given(instance=Java::Assignment_strategy)
def test_java::assignment_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=Java::Assignment_strategy)
def test_java::assignment_objectId_type(instance):
    assert isinstance(instance.objectId, str)


@given(instance=Java::Assignment_strategy)
def test_java::assignment_objectId_setter(instance):
    original = instance.objectId
    instance.objectId = original
    assert instance.objectId == original

@given(instance=Java::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_java::variabledeclaration_instantiation(instance):
    assert isinstance(instance, Java::VariableDeclaration)

@given(instance=Java::VariableDeclaration_strategy)
def test_java::variabledeclaration_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=Java::VariableDeclaration_strategy)
def test_java::variabledeclaration_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=Java::MethodSignature_strategy)
@settings(max_examples=50)
def test_java::methodsignature_instantiation(instance):
    assert isinstance(instance, Java::MethodSignature)

@given(instance=Java::MethodSignature_strategy)
def test_java::methodsignature_isPublic_type(instance):
    assert isinstance(instance.isPublic, bool)


@given(instance=Java::MethodSignature_strategy)
def test_java::methodsignature_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original

@given(instance=Java::MethodSignature_strategy)
def test_java::methodsignature_isPrivate_type(instance):
    assert isinstance(instance.isPrivate, bool)


@given(instance=Java::MethodSignature_strategy)
def test_java::methodsignature_isPrivate_setter(instance):
    original = instance.isPrivate
    instance.isPrivate = original
    assert instance.isPrivate == original

@given(instance=Java::MethodSignature_strategy)
def test_java::methodsignature_isProtected_type(instance):
    assert isinstance(instance.isProtected, bool)


@given(instance=Java::MethodSignature_strategy)
def test_java::methodsignature_isProtected_setter(instance):
    original = instance.isProtected
    instance.isProtected = original
    assert instance.isProtected == original

@given(instance=Java::MethodSignature_strategy)
def test_java::methodsignature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Java::MethodSignature_strategy)
def test_java::methodsignature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java::MethodSignature_strategy)
def test_java::methodsignature_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=Java::MethodSignature_strategy)
def test_java::methodsignature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=MethodSignature_strategy)
@settings(max_examples=50)
def test_methodsignature_instantiation(instance):
    assert isinstance(instance, MethodSignature)

@given(instance=Java::Method_strategy)
@settings(max_examples=50)
def test_java::method_instantiation(instance):
    assert isinstance(instance, Java::Method)

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Java::ObjectType_strategy)
@settings(max_examples=50)
def test_java::objecttype_instantiation(instance):
    assert isinstance(instance, Java::ObjectType)

@given(instance=Java::PrimitiveType_strategy)
@settings(max_examples=50)
def test_java::primitivetype_instantiation(instance):
    assert isinstance(instance, Java::PrimitiveType)

@given(instance=Java::VoidType_strategy)
@settings(max_examples=50)
def test_java::voidtype_instantiation(instance):
    assert isinstance(instance, Java::VoidType)

@given(instance=Java::Type_strategy)
@settings(max_examples=50)
def test_java::type_instantiation(instance):
    assert isinstance(instance, Java::Type)

@given(instance=Java::Type_strategy)
def test_java::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Java::Type_strategy)
def test_java::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ObjectType_strategy)
@settings(max_examples=50)
def test_objecttype_instantiation(instance):
    assert isinstance(instance, ObjectType)

@given(instance=Java::Class_strategy)
@settings(max_examples=50)
def test_java::class_instantiation(instance):
    assert isinstance(instance, Java::Class)

@given(instance=Java::Class_strategy)
def test_java::class_isPublic_type(instance):
    assert isinstance(instance.isPublic, bool)


@given(instance=Java::Class_strategy)
def test_java::class_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original

@given(instance=Java::Class_strategy)
def test_java::class_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=Java::Class_strategy)
def test_java::class_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=Java::Interface_strategy)
@settings(max_examples=50)
def test_java::interface_instantiation(instance):
    assert isinstance(instance, Java::Interface)

@given(instance=Java::Package_strategy)
@settings(max_examples=50)
def test_java::package_instantiation(instance):
    assert isinstance(instance, Java::Package)

@given(instance=Java::Package_strategy)
def test_java::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Java::Package_strategy)
def test_java::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
