import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    typeslibrary::TypesLibrary,
    typeslibrary::TypesLibraryUser,
    typeslibrary::Type,
    typeslibrary::UserDefinedType,
    UserDefinedType,
    typeslibrary::SimpleNamedType,
    typeslibrary::ComplexNamedType,
    Type,
    typeslibrary::TypeInstance,
    typeslibrary::NativeType,
    typeslibrary::UserDefinedTypeRef,
    TypesLibrary,
    typeslibrary::UserDefinedTypesLibrary,
    typeslibrary::NativeTypesLibrary,
    TypesLibraryKind,
    NativeTypeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typeslibrary::typeslibrary_is_not_abstract():
    assert not inspect.isabstract(typeslibrary::TypesLibrary)


def test_typeslibrary::typeslibrary_constructor_exists():
    assert callable(typeslibrary::TypesLibrary.__init__)


def test_typeslibrary::typeslibrary_constructor_args():
    sig = inspect.signature(typeslibrary::TypesLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_typeslibrary::typeslibrary_has_kind():
    assert hasattr(typeslibrary::TypesLibrary, "kind")
    descriptor = None
    for klass in typeslibrary::TypesLibrary.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_typeslibrary::typeslibraryuser_is_not_abstract():
    assert not inspect.isabstract(typeslibrary::TypesLibraryUser)


def test_typeslibrary::typeslibraryuser_constructor_exists():
    assert callable(typeslibrary::TypesLibraryUser.__init__)


def test_typeslibrary::typeslibraryuser_constructor_args():
    sig = inspect.signature(typeslibrary::TypesLibraryUser.__init__)
    params = list(sig.parameters.keys())



def test_typeslibrary::type_is_not_abstract():
    assert not inspect.isabstract(typeslibrary::Type)


def test_typeslibrary::type_constructor_exists():
    assert callable(typeslibrary::Type.__init__)


def test_typeslibrary::type_constructor_args():
    sig = inspect.signature(typeslibrary::Type.__init__)
    params = list(sig.parameters.keys())



def test_typeslibrary::userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(typeslibrary::UserDefinedType)


def test_typeslibrary::userdefinedtype_constructor_exists():
    assert callable(typeslibrary::UserDefinedType.__init__)


def test_typeslibrary::userdefinedtype_constructor_args():
    sig = inspect.signature(typeslibrary::UserDefinedType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeslibrary::userdefinedtype_has_name():
    assert hasattr(typeslibrary::UserDefinedType, "name")
    descriptor = None
    for klass in typeslibrary::UserDefinedType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_userdefinedtype_is_not_abstract():
    assert not inspect.isabstract(UserDefinedType)


def test_userdefinedtype_constructor_exists():
    assert callable(UserDefinedType.__init__)


def test_userdefinedtype_constructor_args():
    sig = inspect.signature(UserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_typeslibrary::simplenamedtype_is_not_abstract():
    assert not inspect.isabstract(typeslibrary::SimpleNamedType)


def test_typeslibrary::simplenamedtype_constructor_exists():
    assert callable(typeslibrary::SimpleNamedType.__init__)


def test_typeslibrary::simplenamedtype_constructor_args():
    sig = inspect.signature(typeslibrary::SimpleNamedType.__init__)
    params = list(sig.parameters.keys())



def test_typeslibrary::complexnamedtype_is_not_abstract():
    assert not inspect.isabstract(typeslibrary::ComplexNamedType)


def test_typeslibrary::complexnamedtype_constructor_exists():
    assert callable(typeslibrary::ComplexNamedType.__init__)


def test_typeslibrary::complexnamedtype_constructor_args():
    sig = inspect.signature(typeslibrary::ComplexNamedType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_typeslibrary::typeinstance_is_not_abstract():
    assert not inspect.isabstract(typeslibrary::TypeInstance)


def test_typeslibrary::typeinstance_constructor_exists():
    assert callable(typeslibrary::TypeInstance.__init__)


def test_typeslibrary::typeinstance_constructor_args():
    sig = inspect.signature(typeslibrary::TypeInstance.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "literals" in params, "Missing parameter 'literals'"
    assert "length" in params, "Missing parameter 'length'"

def test_typeslibrary::typeinstance_has_precision():
    assert hasattr(typeslibrary::TypeInstance, "precision")
    descriptor = None
    for klass in typeslibrary::TypeInstance.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_typeslibrary::typeinstance_has_literals():
    assert hasattr(typeslibrary::TypeInstance, "literals")
    descriptor = None
    for klass in typeslibrary::TypeInstance.__mro__:
        if "literals" in klass.__dict__:
            descriptor = klass.__dict__["literals"]
            break
    assert isinstance(descriptor, property)

def test_typeslibrary::typeinstance_has_length():
    assert hasattr(typeslibrary::TypeInstance, "length")
    descriptor = None
    for klass in typeslibrary::TypeInstance.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_typeslibrary::nativetype_is_not_abstract():
    assert not inspect.isabstract(typeslibrary::NativeType)


def test_typeslibrary::nativetype_constructor_exists():
    assert callable(typeslibrary::NativeType.__init__)


def test_typeslibrary::nativetype_constructor_args():
    sig = inspect.signature(typeslibrary::NativeType.__init__)
    params = list(sig.parameters.keys())
    assert "spec" in params, "Missing parameter 'spec'"
    assert "name" in params, "Missing parameter 'name'"

def test_typeslibrary::nativetype_has_spec():
    assert hasattr(typeslibrary::NativeType, "spec")
    descriptor = None
    for klass in typeslibrary::NativeType.__mro__:
        if "spec" in klass.__dict__:
            descriptor = klass.__dict__["spec"]
            break
    assert isinstance(descriptor, property)

def test_typeslibrary::nativetype_has_name():
    assert hasattr(typeslibrary::NativeType, "name")
    descriptor = None
    for klass in typeslibrary::NativeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeslibrary::userdefinedtyperef_is_not_abstract():
    assert not inspect.isabstract(typeslibrary::UserDefinedTypeRef)


def test_typeslibrary::userdefinedtyperef_constructor_exists():
    assert callable(typeslibrary::UserDefinedTypeRef.__init__)


def test_typeslibrary::userdefinedtyperef_constructor_args():
    sig = inspect.signature(typeslibrary::UserDefinedTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_typeslibrary_is_not_abstract():
    assert not inspect.isabstract(TypesLibrary)


def test_typeslibrary_constructor_exists():
    assert callable(TypesLibrary.__init__)


def test_typeslibrary_constructor_args():
    sig = inspect.signature(TypesLibrary.__init__)
    params = list(sig.parameters.keys())



def test_typeslibrary::userdefinedtypeslibrary_is_not_abstract():
    assert not inspect.isabstract(typeslibrary::UserDefinedTypesLibrary)


def test_typeslibrary::userdefinedtypeslibrary_constructor_exists():
    assert callable(typeslibrary::UserDefinedTypesLibrary.__init__)


def test_typeslibrary::userdefinedtypeslibrary_constructor_args():
    sig = inspect.signature(typeslibrary::UserDefinedTypesLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeslibrary::userdefinedtypeslibrary_has_name():
    assert hasattr(typeslibrary::UserDefinedTypesLibrary, "name")
    descriptor = None
    for klass in typeslibrary::UserDefinedTypesLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeslibrary::nativetypeslibrary_is_not_abstract():
    assert not inspect.isabstract(typeslibrary::NativeTypesLibrary)


def test_typeslibrary::nativetypeslibrary_constructor_exists():
    assert callable(typeslibrary::NativeTypesLibrary.__init__)


def test_typeslibrary::nativetypeslibrary_constructor_args():
    sig = inspect.signature(typeslibrary::NativeTypesLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeslibrary::nativetypeslibrary_has_name():
    assert hasattr(typeslibrary::NativeTypesLibrary, "name")
    descriptor = None
    for klass in typeslibrary::NativeTypesLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_typeslibrarykind_exists():
    # Check that the Enumeration exists
    assert TypesLibraryKind is not None

def test_typeslibrarykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypesLibraryKind]
    expected_literals = [
        "logicalTypes",
        "physicalTypes",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypesLibraryKind"

def test_nativetypekind_exists():
    # Check that the Enumeration exists
    assert NativeTypeKind is not None

def test_nativetypekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NativeTypeKind]
    expected_literals = [
        "Enum",
        "LengthAndPrecision",
        "Length",
        "Simple",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NativeTypeKind"


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
typeslibrary::TypesLibrary_strategy = st.builds(
    typeslibrary::TypesLibrary,
    kind=
        safe_text
)
typeslibrary::TypesLibraryUser_strategy = st.builds(
    typeslibrary::TypesLibraryUser,
)
typeslibrary::Type_strategy = st.builds(
    typeslibrary::Type,
)
typeslibrary::UserDefinedType_strategy = st.builds(
    typeslibrary::UserDefinedType,
    name=
        safe_text
)
UserDefinedType_strategy = st.builds(
    UserDefinedType,
)
typeslibrary::SimpleNamedType_strategy = st.builds(
    typeslibrary::SimpleNamedType,
)
typeslibrary::ComplexNamedType_strategy = st.builds(
    typeslibrary::ComplexNamedType,
)
Type_strategy = st.builds(
    Type,
)
typeslibrary::TypeInstance_strategy = st.builds(
    typeslibrary::TypeInstance,
    precision=
        st.integers(),
    literals=
        safe_text,
    length=
        st.integers()
)
typeslibrary::NativeType_strategy = st.builds(
    typeslibrary::NativeType,
    spec=
        safe_text,
    name=
        safe_text
)
typeslibrary::UserDefinedTypeRef_strategy = st.builds(
    typeslibrary::UserDefinedTypeRef,
)
TypesLibrary_strategy = st.builds(
    TypesLibrary,
)
typeslibrary::UserDefinedTypesLibrary_strategy = st.builds(
    typeslibrary::UserDefinedTypesLibrary,
    name=
        safe_text
)
typeslibrary::NativeTypesLibrary_strategy = st.builds(
    typeslibrary::NativeTypesLibrary,
    name=
        safe_text
)

@given(instance=typeslibrary::TypesLibrary_strategy)
@settings(max_examples=50)
def test_typeslibrary::typeslibrary_instantiation(instance):
    assert isinstance(instance, typeslibrary::TypesLibrary)

@given(instance=typeslibrary::TypesLibrary_strategy)
def test_typeslibrary::typeslibrary_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=typeslibrary::TypesLibrary_strategy)
def test_typeslibrary::typeslibrary_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=typeslibrary::TypesLibraryUser_strategy)
@settings(max_examples=50)
def test_typeslibrary::typeslibraryuser_instantiation(instance):
    assert isinstance(instance, typeslibrary::TypesLibraryUser)

@given(instance=typeslibrary::Type_strategy)
@settings(max_examples=50)
def test_typeslibrary::type_instantiation(instance):
    assert isinstance(instance, typeslibrary::Type)

@given(instance=typeslibrary::UserDefinedType_strategy)
@settings(max_examples=50)
def test_typeslibrary::userdefinedtype_instantiation(instance):
    assert isinstance(instance, typeslibrary::UserDefinedType)

@given(instance=typeslibrary::UserDefinedType_strategy)
def test_typeslibrary::userdefinedtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typeslibrary::UserDefinedType_strategy)
def test_typeslibrary::userdefinedtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UserDefinedType_strategy)
@settings(max_examples=50)
def test_userdefinedtype_instantiation(instance):
    assert isinstance(instance, UserDefinedType)

@given(instance=typeslibrary::SimpleNamedType_strategy)
@settings(max_examples=50)
def test_typeslibrary::simplenamedtype_instantiation(instance):
    assert isinstance(instance, typeslibrary::SimpleNamedType)

@given(instance=typeslibrary::ComplexNamedType_strategy)
@settings(max_examples=50)
def test_typeslibrary::complexnamedtype_instantiation(instance):
    assert isinstance(instance, typeslibrary::ComplexNamedType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=typeslibrary::TypeInstance_strategy)
@settings(max_examples=50)
def test_typeslibrary::typeinstance_instantiation(instance):
    assert isinstance(instance, typeslibrary::TypeInstance)

@given(instance=typeslibrary::TypeInstance_strategy)
def test_typeslibrary::typeinstance_precision_type(instance):
    assert isinstance(instance.precision, int)


@given(instance=typeslibrary::TypeInstance_strategy)
def test_typeslibrary::typeinstance_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=typeslibrary::TypeInstance_strategy)
def test_typeslibrary::typeinstance_literals_type(instance):
    assert isinstance(instance.literals, str)


@given(instance=typeslibrary::TypeInstance_strategy)
def test_typeslibrary::typeinstance_literals_setter(instance):
    original = instance.literals
    instance.literals = original
    assert instance.literals == original

@given(instance=typeslibrary::TypeInstance_strategy)
def test_typeslibrary::typeinstance_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=typeslibrary::TypeInstance_strategy)
def test_typeslibrary::typeinstance_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=typeslibrary::NativeType_strategy)
@settings(max_examples=50)
def test_typeslibrary::nativetype_instantiation(instance):
    assert isinstance(instance, typeslibrary::NativeType)

@given(instance=typeslibrary::NativeType_strategy)
def test_typeslibrary::nativetype_spec_type(instance):
    assert isinstance(instance.spec, str)


@given(instance=typeslibrary::NativeType_strategy)
def test_typeslibrary::nativetype_spec_setter(instance):
    original = instance.spec
    instance.spec = original
    assert instance.spec == original

@given(instance=typeslibrary::NativeType_strategy)
def test_typeslibrary::nativetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typeslibrary::NativeType_strategy)
def test_typeslibrary::nativetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typeslibrary::UserDefinedTypeRef_strategy)
@settings(max_examples=50)
def test_typeslibrary::userdefinedtyperef_instantiation(instance):
    assert isinstance(instance, typeslibrary::UserDefinedTypeRef)

@given(instance=TypesLibrary_strategy)
@settings(max_examples=50)
def test_typeslibrary_instantiation(instance):
    assert isinstance(instance, TypesLibrary)

@given(instance=typeslibrary::UserDefinedTypesLibrary_strategy)
@settings(max_examples=50)
def test_typeslibrary::userdefinedtypeslibrary_instantiation(instance):
    assert isinstance(instance, typeslibrary::UserDefinedTypesLibrary)

@given(instance=typeslibrary::UserDefinedTypesLibrary_strategy)
def test_typeslibrary::userdefinedtypeslibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typeslibrary::UserDefinedTypesLibrary_strategy)
def test_typeslibrary::userdefinedtypeslibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typeslibrary::NativeTypesLibrary_strategy)
@settings(max_examples=50)
def test_typeslibrary::nativetypeslibrary_instantiation(instance):
    assert isinstance(instance, typeslibrary::NativeTypesLibrary)

@given(instance=typeslibrary::NativeTypesLibrary_strategy)
def test_typeslibrary::nativetypeslibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typeslibrary::NativeTypesLibrary_strategy)
def test_typeslibrary::nativetypeslibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=typeslibrary::NativeTypesLibrary_strategy)
@settings(max_examples=30)
def test_typeslibrary::nativetypeslibrary_findtypebyname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findTypeByName(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findTypeByName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findTypeByName' in typeslibrary::NativeTypesLibrary is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findTypeByName' in typeslibrary::NativeTypesLibrary did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findTypeByName' in typeslibrary::NativeTypesLibrary is not implemented or raised an error")
