import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    oclstdlibcs::Precedence,
    Nameable,
    RootPackageCS,
    oclstdlibcs::LibRootPackageCS,
    AttributeCS,
    PackageCS,
    oclstdlibcs::LibPackageCS,
    oclstdlibcs::ParameterCS,
    ConstraintCS,
    oclstdlibcs::LibConstraintCS,
    JavaImplementationCS,
    oclstdlibcs::LibPropertyCS,
    OperationCS,
    oclstdlibcs::LibOperationCS,
    oclstdlibcs::LibIterationCS,
    oclstdlibcs::LibCoercionCS,
    StructuredClassCS,
    oclstdlibcs::LibClassCS,
    ElementCS,
    oclstdlibcs::MetaclassNameCS,
    oclstdlibcs::JavaImplementationCS,
    NamedElementCS,
    oclstdlibcs::PrecedenceCS,
    oclstdlibcs::JavaClassCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclstdlibcs::precedence_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::Precedence)


def test_oclstdlibcs::precedence_constructor_exists():
    assert callable(oclstdlibcs::Precedence.__init__)


def test_oclstdlibcs::precedence_constructor_args():
    sig = inspect.signature(oclstdlibcs::Precedence.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_rootpackagecs_is_not_abstract():
    assert not inspect.isabstract(RootPackageCS)


def test_rootpackagecs_constructor_exists():
    assert callable(RootPackageCS.__init__)


def test_rootpackagecs_constructor_args():
    sig = inspect.signature(RootPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs::librootpackagecs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::LibRootPackageCS)


def test_oclstdlibcs::librootpackagecs_constructor_exists():
    assert callable(oclstdlibcs::LibRootPackageCS.__init__)


def test_oclstdlibcs::librootpackagecs_constructor_args():
    sig = inspect.signature(oclstdlibcs::LibRootPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_attributecs_is_not_abstract():
    assert not inspect.isabstract(AttributeCS)


def test_attributecs_constructor_exists():
    assert callable(AttributeCS.__init__)


def test_attributecs_constructor_args():
    sig = inspect.signature(AttributeCS.__init__)
    params = list(sig.parameters.keys())



def test_packagecs_is_not_abstract():
    assert not inspect.isabstract(PackageCS)


def test_packagecs_constructor_exists():
    assert callable(PackageCS.__init__)


def test_packagecs_constructor_args():
    sig = inspect.signature(PackageCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs::libpackagecs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::LibPackageCS)


def test_oclstdlibcs::libpackagecs_constructor_exists():
    assert callable(oclstdlibcs::LibPackageCS.__init__)


def test_oclstdlibcs::libpackagecs_constructor_args():
    sig = inspect.signature(oclstdlibcs::LibPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs::parametercs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::ParameterCS)


def test_oclstdlibcs::parametercs_constructor_exists():
    assert callable(oclstdlibcs::ParameterCS.__init__)


def test_oclstdlibcs::parametercs_constructor_args():
    sig = inspect.signature(oclstdlibcs::ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_constraintcs_is_not_abstract():
    assert not inspect.isabstract(ConstraintCS)


def test_constraintcs_constructor_exists():
    assert callable(ConstraintCS.__init__)


def test_constraintcs_constructor_args():
    sig = inspect.signature(ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs::libconstraintcs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::LibConstraintCS)


def test_oclstdlibcs::libconstraintcs_constructor_exists():
    assert callable(oclstdlibcs::LibConstraintCS.__init__)


def test_oclstdlibcs::libconstraintcs_constructor_args():
    sig = inspect.signature(oclstdlibcs::LibConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_javaimplementationcs_is_not_abstract():
    assert not inspect.isabstract(JavaImplementationCS)


def test_javaimplementationcs_constructor_exists():
    assert callable(JavaImplementationCS.__init__)


def test_javaimplementationcs_constructor_args():
    sig = inspect.signature(JavaImplementationCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs::libpropertycs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::LibPropertyCS)


def test_oclstdlibcs::libpropertycs_constructor_exists():
    assert callable(oclstdlibcs::LibPropertyCS.__init__)


def test_oclstdlibcs::libpropertycs_constructor_args():
    sig = inspect.signature(oclstdlibcs::LibPropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_oclstdlibcs::libpropertycs_has_isStatic():
    assert hasattr(oclstdlibcs::LibPropertyCS, "isStatic")
    descriptor = None
    for klass in oclstdlibcs::LibPropertyCS.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_operationcs_is_not_abstract():
    assert not inspect.isabstract(OperationCS)


def test_operationcs_constructor_exists():
    assert callable(OperationCS.__init__)


def test_operationcs_constructor_args():
    sig = inspect.signature(OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs::liboperationcs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::LibOperationCS)


def test_oclstdlibcs::liboperationcs_constructor_exists():
    assert callable(oclstdlibcs::LibOperationCS.__init__)


def test_oclstdlibcs::liboperationcs_constructor_args():
    sig = inspect.signature(oclstdlibcs::LibOperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "isInvalidating" in params, "Missing parameter 'isInvalidating'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "isValidating" in params, "Missing parameter 'isValidating'"

def test_oclstdlibcs::liboperationcs_has_isInvalidating():
    assert hasattr(oclstdlibcs::LibOperationCS, "isInvalidating")
    descriptor = None
    for klass in oclstdlibcs::LibOperationCS.__mro__:
        if "isInvalidating" in klass.__dict__:
            descriptor = klass.__dict__["isInvalidating"]
            break
    assert isinstance(descriptor, property)

def test_oclstdlibcs::liboperationcs_has_isStatic():
    assert hasattr(oclstdlibcs::LibOperationCS, "isStatic")
    descriptor = None
    for klass in oclstdlibcs::LibOperationCS.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_oclstdlibcs::liboperationcs_has_isValidating():
    assert hasattr(oclstdlibcs::LibOperationCS, "isValidating")
    descriptor = None
    for klass in oclstdlibcs::LibOperationCS.__mro__:
        if "isValidating" in klass.__dict__:
            descriptor = klass.__dict__["isValidating"]
            break
    assert isinstance(descriptor, property)



def test_oclstdlibcs::libiterationcs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::LibIterationCS)


def test_oclstdlibcs::libiterationcs_constructor_exists():
    assert callable(oclstdlibcs::LibIterationCS.__init__)


def test_oclstdlibcs::libiterationcs_constructor_args():
    sig = inspect.signature(oclstdlibcs::LibIterationCS.__init__)
    params = list(sig.parameters.keys())
    assert "isValidating" in params, "Missing parameter 'isValidating'"
    assert "isInvalidating" in params, "Missing parameter 'isInvalidating'"

def test_oclstdlibcs::libiterationcs_has_isValidating():
    assert hasattr(oclstdlibcs::LibIterationCS, "isValidating")
    descriptor = None
    for klass in oclstdlibcs::LibIterationCS.__mro__:
        if "isValidating" in klass.__dict__:
            descriptor = klass.__dict__["isValidating"]
            break
    assert isinstance(descriptor, property)

def test_oclstdlibcs::libiterationcs_has_isInvalidating():
    assert hasattr(oclstdlibcs::LibIterationCS, "isInvalidating")
    descriptor = None
    for klass in oclstdlibcs::LibIterationCS.__mro__:
        if "isInvalidating" in klass.__dict__:
            descriptor = klass.__dict__["isInvalidating"]
            break
    assert isinstance(descriptor, property)



def test_oclstdlibcs::libcoercioncs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::LibCoercionCS)


def test_oclstdlibcs::libcoercioncs_constructor_exists():
    assert callable(oclstdlibcs::LibCoercionCS.__init__)


def test_oclstdlibcs::libcoercioncs_constructor_args():
    sig = inspect.signature(oclstdlibcs::LibCoercionCS.__init__)
    params = list(sig.parameters.keys())



def test_structuredclasscs_is_not_abstract():
    assert not inspect.isabstract(StructuredClassCS)


def test_structuredclasscs_constructor_exists():
    assert callable(StructuredClassCS.__init__)


def test_structuredclasscs_constructor_args():
    sig = inspect.signature(StructuredClassCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs::libclasscs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::LibClassCS)


def test_oclstdlibcs::libclasscs_constructor_exists():
    assert callable(oclstdlibcs::LibClassCS.__init__)


def test_oclstdlibcs::libclasscs_constructor_args():
    sig = inspect.signature(oclstdlibcs::LibClassCS.__init__)
    params = list(sig.parameters.keys())



def test_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs::metaclassnamecs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::MetaclassNameCS)


def test_oclstdlibcs::metaclassnamecs_constructor_exists():
    assert callable(oclstdlibcs::MetaclassNameCS.__init__)


def test_oclstdlibcs::metaclassnamecs_constructor_args():
    sig = inspect.signature(oclstdlibcs::MetaclassNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclstdlibcs::metaclassnamecs_has_name():
    assert hasattr(oclstdlibcs::MetaclassNameCS, "name")
    descriptor = None
    for klass in oclstdlibcs::MetaclassNameCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclstdlibcs::javaimplementationcs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::JavaImplementationCS)


def test_oclstdlibcs::javaimplementationcs_constructor_exists():
    assert callable(oclstdlibcs::JavaImplementationCS.__init__)


def test_oclstdlibcs::javaimplementationcs_constructor_args():
    sig = inspect.signature(oclstdlibcs::JavaImplementationCS.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs::precedencecs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::PrecedenceCS)


def test_oclstdlibcs::precedencecs_constructor_exists():
    assert callable(oclstdlibcs::PrecedenceCS.__init__)


def test_oclstdlibcs::precedencecs_constructor_args():
    sig = inspect.signature(oclstdlibcs::PrecedenceCS.__init__)
    params = list(sig.parameters.keys())
    assert "isRightAssociative" in params, "Missing parameter 'isRightAssociative'"

def test_oclstdlibcs::precedencecs_has_isRightAssociative():
    assert hasattr(oclstdlibcs::PrecedenceCS, "isRightAssociative")
    descriptor = None
    for klass in oclstdlibcs::PrecedenceCS.__mro__:
        if "isRightAssociative" in klass.__dict__:
            descriptor = klass.__dict__["isRightAssociative"]
            break
    assert isinstance(descriptor, property)



def test_oclstdlibcs::javaclasscs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs::JavaClassCS)


def test_oclstdlibcs::javaclasscs_constructor_exists():
    assert callable(oclstdlibcs::JavaClassCS.__init__)


def test_oclstdlibcs::javaclasscs_constructor_args():
    sig = inspect.signature(oclstdlibcs::JavaClassCS.__init__)
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
oclstdlibcs::Precedence_strategy = st.builds(
    oclstdlibcs::Precedence,
)
Nameable_strategy = st.builds(
    Nameable,
)
RootPackageCS_strategy = st.builds(
    RootPackageCS,
)
oclstdlibcs::LibRootPackageCS_strategy = st.builds(
    oclstdlibcs::LibRootPackageCS,
)
AttributeCS_strategy = st.builds(
    AttributeCS,
)
PackageCS_strategy = st.builds(
    PackageCS,
)
oclstdlibcs::LibPackageCS_strategy = st.builds(
    oclstdlibcs::LibPackageCS,
)
oclstdlibcs::ParameterCS_strategy = st.builds(
    oclstdlibcs::ParameterCS,
)
ConstraintCS_strategy = st.builds(
    ConstraintCS,
)
oclstdlibcs::LibConstraintCS_strategy = st.builds(
    oclstdlibcs::LibConstraintCS,
)
JavaImplementationCS_strategy = st.builds(
    JavaImplementationCS,
)
oclstdlibcs::LibPropertyCS_strategy = st.builds(
    oclstdlibcs::LibPropertyCS,
    isStatic=
        safe_text
)
OperationCS_strategy = st.builds(
    OperationCS,
)
oclstdlibcs::LibOperationCS_strategy = st.builds(
    oclstdlibcs::LibOperationCS,
    isInvalidating=
        safe_text,
    isStatic=
        safe_text,
    isValidating=
        safe_text
)
oclstdlibcs::LibIterationCS_strategy = st.builds(
    oclstdlibcs::LibIterationCS,
    isValidating=
        safe_text,
    isInvalidating=
        safe_text
)
oclstdlibcs::LibCoercionCS_strategy = st.builds(
    oclstdlibcs::LibCoercionCS,
)
StructuredClassCS_strategy = st.builds(
    StructuredClassCS,
)
oclstdlibcs::LibClassCS_strategy = st.builds(
    oclstdlibcs::LibClassCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
oclstdlibcs::MetaclassNameCS_strategy = st.builds(
    oclstdlibcs::MetaclassNameCS,
    name=
        safe_text
)
oclstdlibcs::JavaImplementationCS_strategy = st.builds(
    oclstdlibcs::JavaImplementationCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
oclstdlibcs::PrecedenceCS_strategy = st.builds(
    oclstdlibcs::PrecedenceCS,
    isRightAssociative=
        st.booleans()
)
oclstdlibcs::JavaClassCS_strategy = st.builds(
    oclstdlibcs::JavaClassCS,
)

@given(instance=oclstdlibcs::Precedence_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::precedence_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::Precedence)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=RootPackageCS_strategy)
@settings(max_examples=50)
def test_rootpackagecs_instantiation(instance):
    assert isinstance(instance, RootPackageCS)

@given(instance=oclstdlibcs::LibRootPackageCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::librootpackagecs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::LibRootPackageCS)

@given(instance=AttributeCS_strategy)
@settings(max_examples=50)
def test_attributecs_instantiation(instance):
    assert isinstance(instance, AttributeCS)

@given(instance=PackageCS_strategy)
@settings(max_examples=50)
def test_packagecs_instantiation(instance):
    assert isinstance(instance, PackageCS)

@given(instance=oclstdlibcs::LibPackageCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::libpackagecs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::LibPackageCS)

@given(instance=oclstdlibcs::ParameterCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::parametercs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::ParameterCS)

@given(instance=ConstraintCS_strategy)
@settings(max_examples=50)
def test_constraintcs_instantiation(instance):
    assert isinstance(instance, ConstraintCS)

@given(instance=oclstdlibcs::LibConstraintCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::libconstraintcs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::LibConstraintCS)

@given(instance=JavaImplementationCS_strategy)
@settings(max_examples=50)
def test_javaimplementationcs_instantiation(instance):
    assert isinstance(instance, JavaImplementationCS)

@given(instance=oclstdlibcs::LibPropertyCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::libpropertycs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::LibPropertyCS)

@given(instance=oclstdlibcs::LibPropertyCS_strategy)
def test_oclstdlibcs::libpropertycs_isStatic_type(instance):
    assert isinstance(instance.isStatic, str)


@given(instance=oclstdlibcs::LibPropertyCS_strategy)
def test_oclstdlibcs::libpropertycs_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=OperationCS_strategy)
@settings(max_examples=50)
def test_operationcs_instantiation(instance):
    assert isinstance(instance, OperationCS)

@given(instance=oclstdlibcs::LibOperationCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::liboperationcs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::LibOperationCS)

@given(instance=oclstdlibcs::LibOperationCS_strategy)
def test_oclstdlibcs::liboperationcs_isInvalidating_type(instance):
    assert isinstance(instance.isInvalidating, str)


@given(instance=oclstdlibcs::LibOperationCS_strategy)
def test_oclstdlibcs::liboperationcs_isInvalidating_setter(instance):
    original = instance.isInvalidating
    instance.isInvalidating = original
    assert instance.isInvalidating == original

@given(instance=oclstdlibcs::LibOperationCS_strategy)
def test_oclstdlibcs::liboperationcs_isStatic_type(instance):
    assert isinstance(instance.isStatic, str)


@given(instance=oclstdlibcs::LibOperationCS_strategy)
def test_oclstdlibcs::liboperationcs_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=oclstdlibcs::LibOperationCS_strategy)
def test_oclstdlibcs::liboperationcs_isValidating_type(instance):
    assert isinstance(instance.isValidating, str)


@given(instance=oclstdlibcs::LibOperationCS_strategy)
def test_oclstdlibcs::liboperationcs_isValidating_setter(instance):
    original = instance.isValidating
    instance.isValidating = original
    assert instance.isValidating == original

@given(instance=oclstdlibcs::LibIterationCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::libiterationcs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::LibIterationCS)

@given(instance=oclstdlibcs::LibIterationCS_strategy)
def test_oclstdlibcs::libiterationcs_isValidating_type(instance):
    assert isinstance(instance.isValidating, str)


@given(instance=oclstdlibcs::LibIterationCS_strategy)
def test_oclstdlibcs::libiterationcs_isValidating_setter(instance):
    original = instance.isValidating
    instance.isValidating = original
    assert instance.isValidating == original

@given(instance=oclstdlibcs::LibIterationCS_strategy)
def test_oclstdlibcs::libiterationcs_isInvalidating_type(instance):
    assert isinstance(instance.isInvalidating, str)


@given(instance=oclstdlibcs::LibIterationCS_strategy)
def test_oclstdlibcs::libiterationcs_isInvalidating_setter(instance):
    original = instance.isInvalidating
    instance.isInvalidating = original
    assert instance.isInvalidating == original

@given(instance=oclstdlibcs::LibCoercionCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::libcoercioncs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::LibCoercionCS)

@given(instance=StructuredClassCS_strategy)
@settings(max_examples=50)
def test_structuredclasscs_instantiation(instance):
    assert isinstance(instance, StructuredClassCS)

@given(instance=oclstdlibcs::LibClassCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::libclasscs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::LibClassCS)

@given(instance=ElementCS_strategy)
@settings(max_examples=50)
def test_elementcs_instantiation(instance):
    assert isinstance(instance, ElementCS)

@given(instance=oclstdlibcs::MetaclassNameCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::metaclassnamecs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::MetaclassNameCS)

@given(instance=oclstdlibcs::MetaclassNameCS_strategy)
def test_oclstdlibcs::metaclassnamecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oclstdlibcs::MetaclassNameCS_strategy)
def test_oclstdlibcs::metaclassnamecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oclstdlibcs::JavaImplementationCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::javaimplementationcs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::JavaImplementationCS)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=oclstdlibcs::PrecedenceCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::precedencecs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::PrecedenceCS)

@given(instance=oclstdlibcs::PrecedenceCS_strategy)
def test_oclstdlibcs::precedencecs_isRightAssociative_type(instance):
    assert isinstance(instance.isRightAssociative, bool)


@given(instance=oclstdlibcs::PrecedenceCS_strategy)
def test_oclstdlibcs::precedencecs_isRightAssociative_setter(instance):
    original = instance.isRightAssociative
    instance.isRightAssociative = original
    assert instance.isRightAssociative == original

@given(instance=oclstdlibcs::JavaClassCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs::javaclasscs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs::JavaClassCS)
