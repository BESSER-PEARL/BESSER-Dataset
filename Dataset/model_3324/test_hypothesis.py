import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Java_Statement,
    Java_Annotation,
    Class,
    Interface,
    Package,
    Type,
    Java_PrimitiveType,
    Java_ObjectType,
    Java_VoidType,
    Java_Field,
    Java_Parameter,
    Annotation,
    Statement,
    Java_Return,
    Java_Assignment,
    Java_VariableDeclaration,
    Java_MethodCall,
    Parameter,
    Java_MethodSignature,
    MethodSignature,
    Java_Method,
    Method,
    Field,
    Java_Type,
    ObjectType,
    Java_Interface,
    Java_Class,
    Java_Package,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_java_statement_is_not_abstract():
    assert not inspect.isabstract(Java_Statement)


def test_java_statement_constructor_exists():
    assert callable(Java_Statement.__init__)


def test_java_statement_constructor_args():
    sig = inspect.signature(Java_Statement.__init__)
    params = list(sig.parameters.keys())



def test_java_annotation_is_not_abstract():
    assert not inspect.isabstract(Java_Annotation)


def test_java_annotation_constructor_exists():
    assert callable(Java_Annotation.__init__)


def test_java_annotation_constructor_args():
    sig = inspect.signature(Java_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "sentenceText" in params, "Missing parameter 'sentenceText'"

def test_java_annotation_has_type():
    assert hasattr(Java_Annotation, "type")
    descriptor = None
    for klass in Java_Annotation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_java_annotation_has_sentenceText():
    assert hasattr(Java_Annotation, "sentenceText")
    descriptor = None
    for klass in Java_Annotation.__mro__:
        if "sentenceText" in klass.__dict__:
            descriptor = klass.__dict__["sentenceText"]
            break
    assert isinstance(descriptor, property)



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



def test_java_primitivetype_is_not_abstract():
    assert not inspect.isabstract(Java_PrimitiveType)


def test_java_primitivetype_constructor_exists():
    assert callable(Java_PrimitiveType.__init__)


def test_java_primitivetype_constructor_args():
    sig = inspect.signature(Java_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_java_objecttype_is_not_abstract():
    assert not inspect.isabstract(Java_ObjectType)


def test_java_objecttype_constructor_exists():
    assert callable(Java_ObjectType.__init__)


def test_java_objecttype_constructor_args():
    sig = inspect.signature(Java_ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_java_voidtype_is_not_abstract():
    assert not inspect.isabstract(Java_VoidType)


def test_java_voidtype_constructor_exists():
    assert callable(Java_VoidType.__init__)


def test_java_voidtype_constructor_args():
    sig = inspect.signature(Java_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_java_field_is_not_abstract():
    assert not inspect.isabstract(Java_Field)


def test_java_field_constructor_exists():
    assert callable(Java_Field.__init__)


def test_java_field_constructor_args():
    sig = inspect.signature(Java_Field.__init__)
    params = list(sig.parameters.keys())
    assert "isPrivate" in params, "Missing parameter 'isPrivate'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "isProtected" in params, "Missing parameter 'isProtected'"
    assert "isPublic" in params, "Missing parameter 'isPublic'"
    assert "name" in params, "Missing parameter 'name'"

def test_java_field_has_isPrivate():
    assert hasattr(Java_Field, "isPrivate")
    descriptor = None
    for klass in Java_Field.__mro__:
        if "isPrivate" in klass.__dict__:
            descriptor = klass.__dict__["isPrivate"]
            break
    assert isinstance(descriptor, property)

def test_java_field_has_isStatic():
    assert hasattr(Java_Field, "isStatic")
    descriptor = None
    for klass in Java_Field.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_java_field_has_isProtected():
    assert hasattr(Java_Field, "isProtected")
    descriptor = None
    for klass in Java_Field.__mro__:
        if "isProtected" in klass.__dict__:
            descriptor = klass.__dict__["isProtected"]
            break
    assert isinstance(descriptor, property)

def test_java_field_has_isPublic():
    assert hasattr(Java_Field, "isPublic")
    descriptor = None
    for klass in Java_Field.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)

def test_java_field_has_name():
    assert hasattr(Java_Field, "name")
    descriptor = None
    for klass in Java_Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_parameter_is_not_abstract():
    assert not inspect.isabstract(Java_Parameter)


def test_java_parameter_constructor_exists():
    assert callable(Java_Parameter.__init__)


def test_java_parameter_constructor_args():
    sig = inspect.signature(Java_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_java_parameter_has_name():
    assert hasattr(Java_Parameter, "name")
    descriptor = None
    for klass in Java_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_java_parameter_has_defaultValue():
    assert hasattr(Java_Parameter, "defaultValue")
    descriptor = None
    for klass in Java_Parameter.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
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



def test_java_return_is_not_abstract():
    assert not inspect.isabstract(Java_Return)


def test_java_return_constructor_exists():
    assert callable(Java_Return.__init__)


def test_java_return_constructor_args():
    sig = inspect.signature(Java_Return.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"
    assert "objectId" in params, "Missing parameter 'objectId'"

def test_java_return_has_fieldName():
    assert hasattr(Java_Return, "fieldName")
    descriptor = None
    for klass in Java_Return.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)

def test_java_return_has_objectId():
    assert hasattr(Java_Return, "objectId")
    descriptor = None
    for klass in Java_Return.__mro__:
        if "objectId" in klass.__dict__:
            descriptor = klass.__dict__["objectId"]
            break
    assert isinstance(descriptor, property)



def test_java_assignment_is_not_abstract():
    assert not inspect.isabstract(Java_Assignment)


def test_java_assignment_constructor_exists():
    assert callable(Java_Assignment.__init__)


def test_java_assignment_constructor_args():
    sig = inspect.signature(Java_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "variableExpr" in params, "Missing parameter 'variableExpr'"
    assert "fieldName" in params, "Missing parameter 'fieldName'"
    assert "objectId" in params, "Missing parameter 'objectId'"

def test_java_assignment_has_variableExpr():
    assert hasattr(Java_Assignment, "variableExpr")
    descriptor = None
    for klass in Java_Assignment.__mro__:
        if "variableExpr" in klass.__dict__:
            descriptor = klass.__dict__["variableExpr"]
            break
    assert isinstance(descriptor, property)

def test_java_assignment_has_fieldName():
    assert hasattr(Java_Assignment, "fieldName")
    descriptor = None
    for klass in Java_Assignment.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)

def test_java_assignment_has_objectId():
    assert hasattr(Java_Assignment, "objectId")
    descriptor = None
    for klass in Java_Assignment.__mro__:
        if "objectId" in klass.__dict__:
            descriptor = klass.__dict__["objectId"]
            break
    assert isinstance(descriptor, property)



def test_java_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Java_VariableDeclaration)


def test_java_variabledeclaration_constructor_exists():
    assert callable(Java_VariableDeclaration.__init__)


def test_java_variabledeclaration_constructor_args():
    sig = inspect.signature(Java_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_java_variabledeclaration_has_variableName():
    assert hasattr(Java_VariableDeclaration, "variableName")
    descriptor = None
    for klass in Java_VariableDeclaration.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_java_methodcall_is_not_abstract():
    assert not inspect.isabstract(Java_MethodCall)


def test_java_methodcall_constructor_exists():
    assert callable(Java_MethodCall.__init__)


def test_java_methodcall_constructor_args():
    sig = inspect.signature(Java_MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "methodName" in params, "Missing parameter 'methodName'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_java_methodcall_has_methodName():
    assert hasattr(Java_MethodCall, "methodName")
    descriptor = None
    for klass in Java_MethodCall.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)

def test_java_methodcall_has_variableName():
    assert hasattr(Java_MethodCall, "variableName")
    descriptor = None
    for klass in Java_MethodCall.__mro__:
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



def test_java_methodsignature_is_not_abstract():
    assert not inspect.isabstract(Java_MethodSignature)


def test_java_methodsignature_constructor_exists():
    assert callable(Java_MethodSignature.__init__)


def test_java_methodsignature_constructor_args():
    sig = inspect.signature(Java_MethodSignature.__init__)
    params = list(sig.parameters.keys())
    assert "isPublic" in params, "Missing parameter 'isPublic'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "isPrivate" in params, "Missing parameter 'isPrivate'"
    assert "isProtected" in params, "Missing parameter 'isProtected'"
    assert "name" in params, "Missing parameter 'name'"

def test_java_methodsignature_has_isPublic():
    assert hasattr(Java_MethodSignature, "isPublic")
    descriptor = None
    for klass in Java_MethodSignature.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)

def test_java_methodsignature_has_isStatic():
    assert hasattr(Java_MethodSignature, "isStatic")
    descriptor = None
    for klass in Java_MethodSignature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_java_methodsignature_has_isPrivate():
    assert hasattr(Java_MethodSignature, "isPrivate")
    descriptor = None
    for klass in Java_MethodSignature.__mro__:
        if "isPrivate" in klass.__dict__:
            descriptor = klass.__dict__["isPrivate"]
            break
    assert isinstance(descriptor, property)

def test_java_methodsignature_has_isProtected():
    assert hasattr(Java_MethodSignature, "isProtected")
    descriptor = None
    for klass in Java_MethodSignature.__mro__:
        if "isProtected" in klass.__dict__:
            descriptor = klass.__dict__["isProtected"]
            break
    assert isinstance(descriptor, property)

def test_java_methodsignature_has_name():
    assert hasattr(Java_MethodSignature, "name")
    descriptor = None
    for klass in Java_MethodSignature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_methodsignature_is_not_abstract():
    assert not inspect.isabstract(MethodSignature)


def test_methodsignature_constructor_exists():
    assert callable(MethodSignature.__init__)


def test_methodsignature_constructor_args():
    sig = inspect.signature(MethodSignature.__init__)
    params = list(sig.parameters.keys())



def test_java_method_is_not_abstract():
    assert not inspect.isabstract(Java_Method)


def test_java_method_constructor_exists():
    assert callable(Java_Method.__init__)


def test_java_method_constructor_args():
    sig = inspect.signature(Java_Method.__init__)
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



def test_java_type_is_not_abstract():
    assert not inspect.isabstract(Java_Type)


def test_java_type_constructor_exists():
    assert callable(Java_Type.__init__)


def test_java_type_constructor_args():
    sig = inspect.signature(Java_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_type_has_name():
    assert hasattr(Java_Type, "name")
    descriptor = None
    for klass in Java_Type.__mro__:
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



def test_java_interface_is_not_abstract():
    assert not inspect.isabstract(Java_Interface)


def test_java_interface_constructor_exists():
    assert callable(Java_Interface.__init__)


def test_java_interface_constructor_args():
    sig = inspect.signature(Java_Interface.__init__)
    params = list(sig.parameters.keys())



def test_java_class_is_not_abstract():
    assert not inspect.isabstract(Java_Class)


def test_java_class_constructor_exists():
    assert callable(Java_Class.__init__)


def test_java_class_constructor_args():
    sig = inspect.signature(Java_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isPublic" in params, "Missing parameter 'isPublic'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_java_class_has_isPublic():
    assert hasattr(Java_Class, "isPublic")
    descriptor = None
    for klass in Java_Class.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)

def test_java_class_has_isStatic():
    assert hasattr(Java_Class, "isStatic")
    descriptor = None
    for klass in Java_Class.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_java_package_is_not_abstract():
    assert not inspect.isabstract(Java_Package)


def test_java_package_constructor_exists():
    assert callable(Java_Package.__init__)


def test_java_package_constructor_args():
    sig = inspect.signature(Java_Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_package_has_name():
    assert hasattr(Java_Package, "name")
    descriptor = None
    for klass in Java_Package.__mro__:
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
Java_Statement_strategy = st.builds(
    Java_Statement,
)
Java_Annotation_strategy = st.builds(
    Java_Annotation,
    type=
        safe_text,
    sentenceText=
        safe_text
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
Java_PrimitiveType_strategy = st.builds(
    Java_PrimitiveType,
)
Java_ObjectType_strategy = st.builds(
    Java_ObjectType,
)
Java_VoidType_strategy = st.builds(
    Java_VoidType,
)
Java_Field_strategy = st.builds(
    Java_Field,
    isPrivate=
        st.booleans(),
    isStatic=
        st.booleans(),
    isProtected=
        st.booleans(),
    isPublic=
        st.booleans(),
    name=
        safe_text
)
Java_Parameter_strategy = st.builds(
    Java_Parameter,
    name=
        safe_text,
    defaultValue=
        safe_text
)
Annotation_strategy = st.builds(
    Annotation,
)
Statement_strategy = st.builds(
    Statement,
)
Java_Return_strategy = st.builds(
    Java_Return,
    fieldName=
        safe_text,
    objectId=
        safe_text
)
Java_Assignment_strategy = st.builds(
    Java_Assignment,
    variableExpr=
        safe_text,
    fieldName=
        safe_text,
    objectId=
        safe_text
)
Java_VariableDeclaration_strategy = st.builds(
    Java_VariableDeclaration,
    variableName=
        safe_text
)
Java_MethodCall_strategy = st.builds(
    Java_MethodCall,
    methodName=
        safe_text,
    variableName=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
Java_MethodSignature_strategy = st.builds(
    Java_MethodSignature,
    isPublic=
        st.booleans(),
    isStatic=
        st.booleans(),
    isPrivate=
        st.booleans(),
    isProtected=
        st.booleans(),
    name=
        safe_text
)
MethodSignature_strategy = st.builds(
    MethodSignature,
)
Java_Method_strategy = st.builds(
    Java_Method,
)
Method_strategy = st.builds(
    Method,
)
Field_strategy = st.builds(
    Field,
)
Java_Type_strategy = st.builds(
    Java_Type,
    name=
        safe_text
)
ObjectType_strategy = st.builds(
    ObjectType,
)
Java_Interface_strategy = st.builds(
    Java_Interface,
)
Java_Class_strategy = st.builds(
    Java_Class,
    isPublic=
        st.booleans(),
    isStatic=
        st.booleans()
)
Java_Package_strategy = st.builds(
    Java_Package,
    name=
        safe_text
)

@given(instance=Java_Statement_strategy)
@settings(max_examples=50)
def test_java_statement_instantiation(instance):
    assert isinstance(instance, Java_Statement)

@given(instance=Java_Annotation_strategy)
@settings(max_examples=50)
def test_java_annotation_instantiation(instance):
    assert isinstance(instance, Java_Annotation)



@given(instance=Java_Annotation_strategy)
def test_java_annotation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Java_Annotation_strategy)
def test_java_annotation_sentenceText_setter(instance):
    original = instance.sentenceText
    instance.sentenceText = original
    assert instance.sentenceText == original

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

@given(instance=Java_PrimitiveType_strategy)
@settings(max_examples=50)
def test_java_primitivetype_instantiation(instance):
    assert isinstance(instance, Java_PrimitiveType)

@given(instance=Java_ObjectType_strategy)
@settings(max_examples=50)
def test_java_objecttype_instantiation(instance):
    assert isinstance(instance, Java_ObjectType)

@given(instance=Java_VoidType_strategy)
@settings(max_examples=50)
def test_java_voidtype_instantiation(instance):
    assert isinstance(instance, Java_VoidType)

@given(instance=Java_Field_strategy)
@settings(max_examples=50)
def test_java_field_instantiation(instance):
    assert isinstance(instance, Java_Field)



@given(instance=Java_Field_strategy)
def test_java_field_isPrivate_setter(instance):
    original = instance.isPrivate
    instance.isPrivate = original
    assert instance.isPrivate == original



@given(instance=Java_Field_strategy)
def test_java_field_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original



@given(instance=Java_Field_strategy)
def test_java_field_isProtected_setter(instance):
    original = instance.isProtected
    instance.isProtected = original
    assert instance.isProtected == original



@given(instance=Java_Field_strategy)
def test_java_field_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original



@given(instance=Java_Field_strategy)
def test_java_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Java_Parameter_strategy)
@settings(max_examples=50)
def test_java_parameter_instantiation(instance):
    assert isinstance(instance, Java_Parameter)



@given(instance=Java_Parameter_strategy)
def test_java_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Java_Parameter_strategy)
def test_java_parameter_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=Java_Return_strategy)
@settings(max_examples=50)
def test_java_return_instantiation(instance):
    assert isinstance(instance, Java_Return)



@given(instance=Java_Return_strategy)
def test_java_return_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original



@given(instance=Java_Return_strategy)
def test_java_return_objectId_setter(instance):
    original = instance.objectId
    instance.objectId = original
    assert instance.objectId == original

@given(instance=Java_Assignment_strategy)
@settings(max_examples=50)
def test_java_assignment_instantiation(instance):
    assert isinstance(instance, Java_Assignment)



@given(instance=Java_Assignment_strategy)
def test_java_assignment_variableExpr_setter(instance):
    original = instance.variableExpr
    instance.variableExpr = original
    assert instance.variableExpr == original



@given(instance=Java_Assignment_strategy)
def test_java_assignment_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original



@given(instance=Java_Assignment_strategy)
def test_java_assignment_objectId_setter(instance):
    original = instance.objectId
    instance.objectId = original
    assert instance.objectId == original

@given(instance=Java_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_java_variabledeclaration_instantiation(instance):
    assert isinstance(instance, Java_VariableDeclaration)



@given(instance=Java_VariableDeclaration_strategy)
def test_java_variabledeclaration_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=Java_MethodCall_strategy)
@settings(max_examples=50)
def test_java_methodcall_instantiation(instance):
    assert isinstance(instance, Java_MethodCall)



@given(instance=Java_MethodCall_strategy)
def test_java_methodcall_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original



@given(instance=Java_MethodCall_strategy)
def test_java_methodcall_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=Java_MethodSignature_strategy)
@settings(max_examples=50)
def test_java_methodsignature_instantiation(instance):
    assert isinstance(instance, Java_MethodSignature)



@given(instance=Java_MethodSignature_strategy)
def test_java_methodsignature_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original



@given(instance=Java_MethodSignature_strategy)
def test_java_methodsignature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original



@given(instance=Java_MethodSignature_strategy)
def test_java_methodsignature_isPrivate_setter(instance):
    original = instance.isPrivate
    instance.isPrivate = original
    assert instance.isPrivate == original



@given(instance=Java_MethodSignature_strategy)
def test_java_methodsignature_isProtected_setter(instance):
    original = instance.isProtected
    instance.isProtected = original
    assert instance.isProtected == original



@given(instance=Java_MethodSignature_strategy)
def test_java_methodsignature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MethodSignature_strategy)
@settings(max_examples=50)
def test_methodsignature_instantiation(instance):
    assert isinstance(instance, MethodSignature)

@given(instance=Java_Method_strategy)
@settings(max_examples=50)
def test_java_method_instantiation(instance):
    assert isinstance(instance, Java_Method)

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=Java_Type_strategy)
@settings(max_examples=50)
def test_java_type_instantiation(instance):
    assert isinstance(instance, Java_Type)



@given(instance=Java_Type_strategy)
def test_java_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ObjectType_strategy)
@settings(max_examples=50)
def test_objecttype_instantiation(instance):
    assert isinstance(instance, ObjectType)

@given(instance=Java_Interface_strategy)
@settings(max_examples=50)
def test_java_interface_instantiation(instance):
    assert isinstance(instance, Java_Interface)

@given(instance=Java_Class_strategy)
@settings(max_examples=50)
def test_java_class_instantiation(instance):
    assert isinstance(instance, Java_Class)



@given(instance=Java_Class_strategy)
def test_java_class_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original



@given(instance=Java_Class_strategy)
def test_java_class_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=Java_Package_strategy)
@settings(max_examples=50)
def test_java_package_instantiation(instance):
    assert isinstance(instance, Java_Package)



@given(instance=Java_Package_strategy)
def test_java_package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
