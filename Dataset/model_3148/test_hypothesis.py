import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    oclstdlibcs_Precedence,
    Nameable,
    RootPackageCS,
    oclstdlibcs_LibRootPackageCS,
    AttributeCS,
    PackageCS,
    oclstdlibcs_LibPackageCS,
    oclstdlibcs_ParameterCS,
    ConstraintCS,
    oclstdlibcs_LibConstraintCS,
    JavaImplementationCS,
    oclstdlibcs_LibPropertyCS,
    OperationCS,
    oclstdlibcs_LibIterationCS,
    oclstdlibcs_LibOperationCS,
    oclstdlibcs_LibCoercionCS,
    StructuredClassCS,
    oclstdlibcs_LibClassCS,
    ElementCS,
    oclstdlibcs_MetaclassNameCS,
    oclstdlibcs_JavaImplementationCS,
    NamedElementCS,
    oclstdlibcs_PrecedenceCS,
    oclstdlibcs_JavaClassCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclstdlibcs_precedence_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_Precedence)


def test_oclstdlibcs_precedence_constructor_exists():
    assert callable(oclstdlibcs_Precedence.__init__)


def test_oclstdlibcs_precedence_constructor_args():
    sig = inspect.signature(oclstdlibcs_Precedence.__init__)
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



def test_oclstdlibcs_librootpackagecs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_LibRootPackageCS)


def test_oclstdlibcs_librootpackagecs_constructor_exists():
    assert callable(oclstdlibcs_LibRootPackageCS.__init__)


def test_oclstdlibcs_librootpackagecs_constructor_args():
    sig = inspect.signature(oclstdlibcs_LibRootPackageCS.__init__)
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



def test_oclstdlibcs_libpackagecs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_LibPackageCS)


def test_oclstdlibcs_libpackagecs_constructor_exists():
    assert callable(oclstdlibcs_LibPackageCS.__init__)


def test_oclstdlibcs_libpackagecs_constructor_args():
    sig = inspect.signature(oclstdlibcs_LibPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs_parametercs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_ParameterCS)


def test_oclstdlibcs_parametercs_constructor_exists():
    assert callable(oclstdlibcs_ParameterCS.__init__)


def test_oclstdlibcs_parametercs_constructor_args():
    sig = inspect.signature(oclstdlibcs_ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_constraintcs_is_not_abstract():
    assert not inspect.isabstract(ConstraintCS)


def test_constraintcs_constructor_exists():
    assert callable(ConstraintCS.__init__)


def test_constraintcs_constructor_args():
    sig = inspect.signature(ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs_libconstraintcs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_LibConstraintCS)


def test_oclstdlibcs_libconstraintcs_constructor_exists():
    assert callable(oclstdlibcs_LibConstraintCS.__init__)


def test_oclstdlibcs_libconstraintcs_constructor_args():
    sig = inspect.signature(oclstdlibcs_LibConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_javaimplementationcs_is_not_abstract():
    assert not inspect.isabstract(JavaImplementationCS)


def test_javaimplementationcs_constructor_exists():
    assert callable(JavaImplementationCS.__init__)


def test_javaimplementationcs_constructor_args():
    sig = inspect.signature(JavaImplementationCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs_libpropertycs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_LibPropertyCS)


def test_oclstdlibcs_libpropertycs_constructor_exists():
    assert callable(oclstdlibcs_LibPropertyCS.__init__)


def test_oclstdlibcs_libpropertycs_constructor_args():
    sig = inspect.signature(oclstdlibcs_LibPropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_oclstdlibcs_libpropertycs_has_isStatic():
    assert hasattr(oclstdlibcs_LibPropertyCS, "isStatic")
    descriptor = None
    for klass in oclstdlibcs_LibPropertyCS.__mro__:
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



def test_oclstdlibcs_libiterationcs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_LibIterationCS)


def test_oclstdlibcs_libiterationcs_constructor_exists():
    assert callable(oclstdlibcs_LibIterationCS.__init__)


def test_oclstdlibcs_libiterationcs_constructor_args():
    sig = inspect.signature(oclstdlibcs_LibIterationCS.__init__)
    params = list(sig.parameters.keys())
    assert "isInvalidating" in params, "Missing parameter 'isInvalidating'"
    assert "isValidating" in params, "Missing parameter 'isValidating'"

def test_oclstdlibcs_libiterationcs_has_isInvalidating():
    assert hasattr(oclstdlibcs_LibIterationCS, "isInvalidating")
    descriptor = None
    for klass in oclstdlibcs_LibIterationCS.__mro__:
        if "isInvalidating" in klass.__dict__:
            descriptor = klass.__dict__["isInvalidating"]
            break
    assert isinstance(descriptor, property)

def test_oclstdlibcs_libiterationcs_has_isValidating():
    assert hasattr(oclstdlibcs_LibIterationCS, "isValidating")
    descriptor = None
    for klass in oclstdlibcs_LibIterationCS.__mro__:
        if "isValidating" in klass.__dict__:
            descriptor = klass.__dict__["isValidating"]
            break
    assert isinstance(descriptor, property)



def test_oclstdlibcs_liboperationcs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_LibOperationCS)


def test_oclstdlibcs_liboperationcs_constructor_exists():
    assert callable(oclstdlibcs_LibOperationCS.__init__)


def test_oclstdlibcs_liboperationcs_constructor_args():
    sig = inspect.signature(oclstdlibcs_LibOperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "isValidating" in params, "Missing parameter 'isValidating'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "isInvalidating" in params, "Missing parameter 'isInvalidating'"

def test_oclstdlibcs_liboperationcs_has_isValidating():
    assert hasattr(oclstdlibcs_LibOperationCS, "isValidating")
    descriptor = None
    for klass in oclstdlibcs_LibOperationCS.__mro__:
        if "isValidating" in klass.__dict__:
            descriptor = klass.__dict__["isValidating"]
            break
    assert isinstance(descriptor, property)

def test_oclstdlibcs_liboperationcs_has_isStatic():
    assert hasattr(oclstdlibcs_LibOperationCS, "isStatic")
    descriptor = None
    for klass in oclstdlibcs_LibOperationCS.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_oclstdlibcs_liboperationcs_has_isInvalidating():
    assert hasattr(oclstdlibcs_LibOperationCS, "isInvalidating")
    descriptor = None
    for klass in oclstdlibcs_LibOperationCS.__mro__:
        if "isInvalidating" in klass.__dict__:
            descriptor = klass.__dict__["isInvalidating"]
            break
    assert isinstance(descriptor, property)



def test_oclstdlibcs_libcoercioncs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_LibCoercionCS)


def test_oclstdlibcs_libcoercioncs_constructor_exists():
    assert callable(oclstdlibcs_LibCoercionCS.__init__)


def test_oclstdlibcs_libcoercioncs_constructor_args():
    sig = inspect.signature(oclstdlibcs_LibCoercionCS.__init__)
    params = list(sig.parameters.keys())



def test_structuredclasscs_is_not_abstract():
    assert not inspect.isabstract(StructuredClassCS)


def test_structuredclasscs_constructor_exists():
    assert callable(StructuredClassCS.__init__)


def test_structuredclasscs_constructor_args():
    sig = inspect.signature(StructuredClassCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs_libclasscs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_LibClassCS)


def test_oclstdlibcs_libclasscs_constructor_exists():
    assert callable(oclstdlibcs_LibClassCS.__init__)


def test_oclstdlibcs_libclasscs_constructor_args():
    sig = inspect.signature(oclstdlibcs_LibClassCS.__init__)
    params = list(sig.parameters.keys())



def test_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs_metaclassnamecs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_MetaclassNameCS)


def test_oclstdlibcs_metaclassnamecs_constructor_exists():
    assert callable(oclstdlibcs_MetaclassNameCS.__init__)


def test_oclstdlibcs_metaclassnamecs_constructor_args():
    sig = inspect.signature(oclstdlibcs_MetaclassNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_oclstdlibcs_metaclassnamecs_has_name():
    assert hasattr(oclstdlibcs_MetaclassNameCS, "name")
    descriptor = None
    for klass in oclstdlibcs_MetaclassNameCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclstdlibcs_javaimplementationcs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_JavaImplementationCS)


def test_oclstdlibcs_javaimplementationcs_constructor_exists():
    assert callable(oclstdlibcs_JavaImplementationCS.__init__)


def test_oclstdlibcs_javaimplementationcs_constructor_args():
    sig = inspect.signature(oclstdlibcs_JavaImplementationCS.__init__)
    params = list(sig.parameters.keys())



def test_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_oclstdlibcs_precedencecs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_PrecedenceCS)


def test_oclstdlibcs_precedencecs_constructor_exists():
    assert callable(oclstdlibcs_PrecedenceCS.__init__)


def test_oclstdlibcs_precedencecs_constructor_args():
    sig = inspect.signature(oclstdlibcs_PrecedenceCS.__init__)
    params = list(sig.parameters.keys())
    assert "isRightAssociative" in params, "Missing parameter 'isRightAssociative'"

def test_oclstdlibcs_precedencecs_has_isRightAssociative():
    assert hasattr(oclstdlibcs_PrecedenceCS, "isRightAssociative")
    descriptor = None
    for klass in oclstdlibcs_PrecedenceCS.__mro__:
        if "isRightAssociative" in klass.__dict__:
            descriptor = klass.__dict__["isRightAssociative"]
            break
    assert isinstance(descriptor, property)



def test_oclstdlibcs_javaclasscs_is_not_abstract():
    assert not inspect.isabstract(oclstdlibcs_JavaClassCS)


def test_oclstdlibcs_javaclasscs_constructor_exists():
    assert callable(oclstdlibcs_JavaClassCS.__init__)


def test_oclstdlibcs_javaclasscs_constructor_args():
    sig = inspect.signature(oclstdlibcs_JavaClassCS.__init__)
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
oclstdlibcs_Precedence_strategy = st.builds(
    oclstdlibcs_Precedence,
)
Nameable_strategy = st.builds(
    Nameable,
)
RootPackageCS_strategy = st.builds(
    RootPackageCS,
)
oclstdlibcs_LibRootPackageCS_strategy = st.builds(
    oclstdlibcs_LibRootPackageCS,
)
AttributeCS_strategy = st.builds(
    AttributeCS,
)
PackageCS_strategy = st.builds(
    PackageCS,
)
oclstdlibcs_LibPackageCS_strategy = st.builds(
    oclstdlibcs_LibPackageCS,
)
oclstdlibcs_ParameterCS_strategy = st.builds(
    oclstdlibcs_ParameterCS,
)
ConstraintCS_strategy = st.builds(
    ConstraintCS,
)
oclstdlibcs_LibConstraintCS_strategy = st.builds(
    oclstdlibcs_LibConstraintCS,
)
JavaImplementationCS_strategy = st.builds(
    JavaImplementationCS,
)
oclstdlibcs_LibPropertyCS_strategy = st.builds(
    oclstdlibcs_LibPropertyCS,
    isStatic=
        safe_text
)
OperationCS_strategy = st.builds(
    OperationCS,
)
oclstdlibcs_LibIterationCS_strategy = st.builds(
    oclstdlibcs_LibIterationCS,
    isInvalidating=
        safe_text,
    isValidating=
        safe_text
)
oclstdlibcs_LibOperationCS_strategy = st.builds(
    oclstdlibcs_LibOperationCS,
    isValidating=
        safe_text,
    isStatic=
        safe_text,
    isInvalidating=
        safe_text
)
oclstdlibcs_LibCoercionCS_strategy = st.builds(
    oclstdlibcs_LibCoercionCS,
)
StructuredClassCS_strategy = st.builds(
    StructuredClassCS,
)
oclstdlibcs_LibClassCS_strategy = st.builds(
    oclstdlibcs_LibClassCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
oclstdlibcs_MetaclassNameCS_strategy = st.builds(
    oclstdlibcs_MetaclassNameCS,
    name=
        safe_text
)
oclstdlibcs_JavaImplementationCS_strategy = st.builds(
    oclstdlibcs_JavaImplementationCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
oclstdlibcs_PrecedenceCS_strategy = st.builds(
    oclstdlibcs_PrecedenceCS,
    isRightAssociative=
        st.booleans()
)
oclstdlibcs_JavaClassCS_strategy = st.builds(
    oclstdlibcs_JavaClassCS,
)

@given(instance=oclstdlibcs_Precedence_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_precedence_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_Precedence)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=RootPackageCS_strategy)
@settings(max_examples=50)
def test_rootpackagecs_instantiation(instance):
    assert isinstance(instance, RootPackageCS)

@given(instance=oclstdlibcs_LibRootPackageCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_librootpackagecs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_LibRootPackageCS)

@given(instance=AttributeCS_strategy)
@settings(max_examples=50)
def test_attributecs_instantiation(instance):
    assert isinstance(instance, AttributeCS)

@given(instance=PackageCS_strategy)
@settings(max_examples=50)
def test_packagecs_instantiation(instance):
    assert isinstance(instance, PackageCS)

@given(instance=oclstdlibcs_LibPackageCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_libpackagecs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_LibPackageCS)

@given(instance=oclstdlibcs_ParameterCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_parametercs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_ParameterCS)

@given(instance=ConstraintCS_strategy)
@settings(max_examples=50)
def test_constraintcs_instantiation(instance):
    assert isinstance(instance, ConstraintCS)

@given(instance=oclstdlibcs_LibConstraintCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_libconstraintcs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_LibConstraintCS)

@given(instance=JavaImplementationCS_strategy)
@settings(max_examples=50)
def test_javaimplementationcs_instantiation(instance):
    assert isinstance(instance, JavaImplementationCS)

@given(instance=oclstdlibcs_LibPropertyCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_libpropertycs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_LibPropertyCS)



@given(instance=oclstdlibcs_LibPropertyCS_strategy)
def test_oclstdlibcs_libpropertycs_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=OperationCS_strategy)
@settings(max_examples=50)
def test_operationcs_instantiation(instance):
    assert isinstance(instance, OperationCS)

@given(instance=oclstdlibcs_LibIterationCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_libiterationcs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_LibIterationCS)



@given(instance=oclstdlibcs_LibIterationCS_strategy)
def test_oclstdlibcs_libiterationcs_isInvalidating_setter(instance):
    original = instance.isInvalidating
    instance.isInvalidating = original
    assert instance.isInvalidating == original



@given(instance=oclstdlibcs_LibIterationCS_strategy)
def test_oclstdlibcs_libiterationcs_isValidating_setter(instance):
    original = instance.isValidating
    instance.isValidating = original
    assert instance.isValidating == original

@given(instance=oclstdlibcs_LibOperationCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_liboperationcs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_LibOperationCS)



@given(instance=oclstdlibcs_LibOperationCS_strategy)
def test_oclstdlibcs_liboperationcs_isValidating_setter(instance):
    original = instance.isValidating
    instance.isValidating = original
    assert instance.isValidating == original



@given(instance=oclstdlibcs_LibOperationCS_strategy)
def test_oclstdlibcs_liboperationcs_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original



@given(instance=oclstdlibcs_LibOperationCS_strategy)
def test_oclstdlibcs_liboperationcs_isInvalidating_setter(instance):
    original = instance.isInvalidating
    instance.isInvalidating = original
    assert instance.isInvalidating == original

@given(instance=oclstdlibcs_LibCoercionCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_libcoercioncs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_LibCoercionCS)

@given(instance=StructuredClassCS_strategy)
@settings(max_examples=50)
def test_structuredclasscs_instantiation(instance):
    assert isinstance(instance, StructuredClassCS)

@given(instance=oclstdlibcs_LibClassCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_libclasscs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_LibClassCS)

@given(instance=ElementCS_strategy)
@settings(max_examples=50)
def test_elementcs_instantiation(instance):
    assert isinstance(instance, ElementCS)

@given(instance=oclstdlibcs_MetaclassNameCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_metaclassnamecs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_MetaclassNameCS)



@given(instance=oclstdlibcs_MetaclassNameCS_strategy)
def test_oclstdlibcs_metaclassnamecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oclstdlibcs_JavaImplementationCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_javaimplementationcs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_JavaImplementationCS)

@given(instance=NamedElementCS_strategy)
@settings(max_examples=50)
def test_namedelementcs_instantiation(instance):
    assert isinstance(instance, NamedElementCS)

@given(instance=oclstdlibcs_PrecedenceCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_precedencecs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_PrecedenceCS)



@given(instance=oclstdlibcs_PrecedenceCS_strategy)
def test_oclstdlibcs_precedencecs_isRightAssociative_setter(instance):
    original = instance.isRightAssociative
    instance.isRightAssociative = original
    assert instance.isRightAssociative == original

@given(instance=oclstdlibcs_JavaClassCS_strategy)
@settings(max_examples=50)
def test_oclstdlibcs_javaclasscs_instantiation(instance):
    assert isinstance(instance, oclstdlibcs_JavaClassCS)
