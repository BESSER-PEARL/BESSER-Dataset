import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    university::PrimitiveType,
    university::NamedElement,
    university::Vehicle,
    NamedElement,
    university::Computer,
    university::Module,
    university::University,
    university::Library,
    university::Department,
    university::Student,
    university::StaffMember,
    university::Book,
    StaffMemberType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university::primitivetype_is_not_abstract():
    assert not inspect.isabstract(university::PrimitiveType)


def test_university::primitivetype_constructor_exists():
    assert callable(university::PrimitiveType.__init__)


def test_university::primitivetype_constructor_args():
    sig = inspect.signature(university::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "m" in params, "Missing parameter 'm'"
    assert "c" in params, "Missing parameter 'c'"
    assert "d" in params, "Missing parameter 'd'"
    assert "bigIntList" in params, "Missing parameter 'bigIntList'"
    assert "f" in params, "Missing parameter 'f'"
    assert "o" in params, "Missing parameter 'o'"
    assert "k" in params, "Missing parameter 'k'"
    assert "g" in params, "Missing parameter 'g'"
    assert "p" in params, "Missing parameter 'p'"
    assert "b" in params, "Missing parameter 'b'"
    assert "l" in params, "Missing parameter 'l'"
    assert "h" in params, "Missing parameter 'h'"
    assert "i" in params, "Missing parameter 'i'"
    assert "j" in params, "Missing parameter 'j'"
    assert "n" in params, "Missing parameter 'n'"
    assert "e" in params, "Missing parameter 'e'"
    assert "a" in params, "Missing parameter 'a'"

def test_university::primitivetype_has_m():
    assert hasattr(university::PrimitiveType, "m")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "m" in klass.__dict__:
            descriptor = klass.__dict__["m"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_c():
    assert hasattr(university::PrimitiveType, "c")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_d():
    assert hasattr(university::PrimitiveType, "d")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_bigIntList():
    assert hasattr(university::PrimitiveType, "bigIntList")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "bigIntList" in klass.__dict__:
            descriptor = klass.__dict__["bigIntList"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_f():
    assert hasattr(university::PrimitiveType, "f")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "f" in klass.__dict__:
            descriptor = klass.__dict__["f"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_o():
    assert hasattr(university::PrimitiveType, "o")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_k():
    assert hasattr(university::PrimitiveType, "k")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "k" in klass.__dict__:
            descriptor = klass.__dict__["k"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_g():
    assert hasattr(university::PrimitiveType, "g")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_p():
    assert hasattr(university::PrimitiveType, "p")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_b():
    assert hasattr(university::PrimitiveType, "b")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_l():
    assert hasattr(university::PrimitiveType, "l")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "l" in klass.__dict__:
            descriptor = klass.__dict__["l"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_h():
    assert hasattr(university::PrimitiveType, "h")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "h" in klass.__dict__:
            descriptor = klass.__dict__["h"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_i():
    assert hasattr(university::PrimitiveType, "i")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_j():
    assert hasattr(university::PrimitiveType, "j")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "j" in klass.__dict__:
            descriptor = klass.__dict__["j"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_n():
    assert hasattr(university::PrimitiveType, "n")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_e():
    assert hasattr(university::PrimitiveType, "e")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "e" in klass.__dict__:
            descriptor = klass.__dict__["e"]
            break
    assert isinstance(descriptor, property)

def test_university::primitivetype_has_a():
    assert hasattr(university::PrimitiveType, "a")
    descriptor = None
    for klass in university::PrimitiveType.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)



def test_university::namedelement_is_not_abstract():
    assert not inspect.isabstract(university::NamedElement)


def test_university::namedelement_constructor_exists():
    assert callable(university::NamedElement.__init__)


def test_university::namedelement_constructor_args():
    sig = inspect.signature(university::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university::namedelement_has_name():
    assert hasattr(university::NamedElement, "name")
    descriptor = None
    for klass in university::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university::vehicle_is_not_abstract():
    assert not inspect.isabstract(university::Vehicle)


def test_university::vehicle_constructor_exists():
    assert callable(university::Vehicle.__init__)


def test_university::vehicle_constructor_args():
    sig = inspect.signature(university::Vehicle.__init__)
    params = list(sig.parameters.keys())
    assert "registrationNumber" in params, "Missing parameter 'registrationNumber'"

def test_university::vehicle_has_registrationNumber():
    assert hasattr(university::Vehicle, "registrationNumber")
    descriptor = None
    for klass in university::Vehicle.__mro__:
        if "registrationNumber" in klass.__dict__:
            descriptor = klass.__dict__["registrationNumber"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_university::computer_is_not_abstract():
    assert not inspect.isabstract(university::Computer)


def test_university::computer_constructor_exists():
    assert callable(university::Computer.__init__)


def test_university::computer_constructor_args():
    sig = inspect.signature(university::Computer.__init__)
    params = list(sig.parameters.keys())



def test_university::module_is_not_abstract():
    assert not inspect.isabstract(university::Module)


def test_university::module_constructor_exists():
    assert callable(university::Module.__init__)


def test_university::module_constructor_args():
    sig = inspect.signature(university::Module.__init__)
    params = list(sig.parameters.keys())



def test_university::university_is_not_abstract():
    assert not inspect.isabstract(university::University)


def test_university::university_constructor_exists():
    assert callable(university::University.__init__)


def test_university::university_constructor_args():
    sig = inspect.signature(university::University.__init__)
    params = list(sig.parameters.keys())



def test_university::library_is_not_abstract():
    assert not inspect.isabstract(university::Library)


def test_university::library_constructor_exists():
    assert callable(university::Library.__init__)


def test_university::library_constructor_args():
    sig = inspect.signature(university::Library.__init__)
    params = list(sig.parameters.keys())



def test_university::department_is_not_abstract():
    assert not inspect.isabstract(university::Department)


def test_university::department_constructor_exists():
    assert callable(university::Department.__init__)


def test_university::department_constructor_args():
    sig = inspect.signature(university::Department.__init__)
    params = list(sig.parameters.keys())



def test_university::student_is_not_abstract():
    assert not inspect.isabstract(university::Student)


def test_university::student_constructor_exists():
    assert callable(university::Student.__init__)


def test_university::student_constructor_args():
    sig = inspect.signature(university::Student.__init__)
    params = list(sig.parameters.keys())
    assert "studentId" in params, "Missing parameter 'studentId'"

def test_university::student_has_studentId():
    assert hasattr(university::Student, "studentId")
    descriptor = None
    for klass in university::Student.__mro__:
        if "studentId" in klass.__dict__:
            descriptor = klass.__dict__["studentId"]
            break
    assert isinstance(descriptor, property)



def test_university::staffmember_is_not_abstract():
    assert not inspect.isabstract(university::StaffMember)


def test_university::staffmember_constructor_exists():
    assert callable(university::StaffMember.__init__)


def test_university::staffmember_constructor_args():
    sig = inspect.signature(university::StaffMember.__init__)
    params = list(sig.parameters.keys())
    assert "staffMemberType" in params, "Missing parameter 'staffMemberType'"

def test_university::staffmember_has_staffMemberType():
    assert hasattr(university::StaffMember, "staffMemberType")
    descriptor = None
    for klass in university::StaffMember.__mro__:
        if "staffMemberType" in klass.__dict__:
            descriptor = klass.__dict__["staffMemberType"]
            break
    assert isinstance(descriptor, property)



def test_university::book_is_not_abstract():
    assert not inspect.isabstract(university::Book)


def test_university::book_constructor_exists():
    assert callable(university::Book.__init__)


def test_university::book_constructor_args():
    sig = inspect.signature(university::Book.__init__)
    params = list(sig.parameters.keys())
    assert "ISBN" in params, "Missing parameter 'ISBN'"
    assert "authorNames" in params, "Missing parameter 'authorNames'"

def test_university::book_has_ISBN():
    assert hasattr(university::Book, "ISBN")
    descriptor = None
    for klass in university::Book.__mro__:
        if "ISBN" in klass.__dict__:
            descriptor = klass.__dict__["ISBN"]
            break
    assert isinstance(descriptor, property)

def test_university::book_has_authorNames():
    assert hasattr(university::Book, "authorNames")
    descriptor = None
    for klass in university::Book.__mro__:
        if "authorNames" in klass.__dict__:
            descriptor = klass.__dict__["authorNames"]
            break
    assert isinstance(descriptor, property)

def test_staffmembertype_exists():
    # Check that the Enumeration exists
    assert StaffMemberType is not None

def test_staffmembertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StaffMemberType]
    expected_literals = [
        "Honary",
        "Admin",
        "ResearchStudent",
        "Technical",
        "Other",
        "Academic",
        "Research",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StaffMemberType"


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
university::PrimitiveType_strategy = st.builds(
    university::PrimitiveType,
    m=
        safe_text,
    c=
        safe_text,
    d=
        st.booleans(),
    bigIntList=
        safe_text,
    f=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    o=
        safe_text,
    k=
        safe_text,
    g=
        safe_text,
    p=
        safe_text,
    b=
        st.integers(),
    l=
        safe_text,
    h=
        safe_text,
    i=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    j=
        safe_text,
    n=
        safe_text,
    e=
        safe_text,
    a=
        safe_text
)
university::NamedElement_strategy = st.builds(
    university::NamedElement,
    name=
        safe_text
)
university::Vehicle_strategy = st.builds(
    university::Vehicle,
    registrationNumber=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
university::Computer_strategy = st.builds(
    university::Computer,
)
university::Module_strategy = st.builds(
    university::Module,
)
university::University_strategy = st.builds(
    university::University,
)
university::Library_strategy = st.builds(
    university::Library,
)
university::Department_strategy = st.builds(
    university::Department,
)
university::Student_strategy = st.builds(
    university::Student,
    studentId=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
university::StaffMember_strategy = st.builds(
    university::StaffMember,
    staffMemberType=
        safe_text
)
university::Book_strategy = st.builds(
    university::Book,
    ISBN=
        safe_text,
    authorNames=
        safe_text
)

@given(instance=university::PrimitiveType_strategy)
@settings(max_examples=50)
def test_university::primitivetype_instantiation(instance):
    assert isinstance(instance, university::PrimitiveType)

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_m_type(instance):
    assert isinstance(instance.m, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_m_setter(instance):
    original = instance.m
    instance.m = original
    assert instance.m == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_c_type(instance):
    assert isinstance(instance.c, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_d_type(instance):
    assert isinstance(instance.d, bool)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_bigIntList_type(instance):
    assert isinstance(instance.bigIntList, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_bigIntList_setter(instance):
    original = instance.bigIntList
    instance.bigIntList = original
    assert instance.bigIntList == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_f_type(instance):
    assert isinstance(instance.f, float)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_f_setter(instance):
    original = instance.f
    instance.f = original
    assert instance.f == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_o_type(instance):
    assert isinstance(instance.o, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_k_type(instance):
    assert isinstance(instance.k, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_k_setter(instance):
    original = instance.k
    instance.k = original
    assert instance.k == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_g_type(instance):
    assert isinstance(instance.g, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_p_type(instance):
    assert isinstance(instance.p, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_b_type(instance):
    assert isinstance(instance.b, int)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_l_type(instance):
    assert isinstance(instance.l, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_l_setter(instance):
    original = instance.l
    instance.l = original
    assert instance.l == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_h_type(instance):
    assert isinstance(instance.h, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_h_setter(instance):
    original = instance.h
    instance.h = original
    assert instance.h == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_i_type(instance):
    assert isinstance(instance.i, float)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_j_type(instance):
    assert isinstance(instance.j, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_j_setter(instance):
    original = instance.j
    instance.j = original
    assert instance.j == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_n_type(instance):
    assert isinstance(instance.n, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_e_type(instance):
    assert isinstance(instance.e, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_e_setter(instance):
    original = instance.e
    instance.e = original
    assert instance.e == original

@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_a_type(instance):
    assert isinstance(instance.a, str)


@given(instance=university::PrimitiveType_strategy)
def test_university::primitivetype_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=university::NamedElement_strategy)
@settings(max_examples=50)
def test_university::namedelement_instantiation(instance):
    assert isinstance(instance, university::NamedElement)

@given(instance=university::NamedElement_strategy)
def test_university::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=university::NamedElement_strategy)
def test_university::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university::Vehicle_strategy)
@settings(max_examples=50)
def test_university::vehicle_instantiation(instance):
    assert isinstance(instance, university::Vehicle)

@given(instance=university::Vehicle_strategy)
def test_university::vehicle_registrationNumber_type(instance):
    assert isinstance(instance.registrationNumber, str)


@given(instance=university::Vehicle_strategy)
def test_university::vehicle_registrationNumber_setter(instance):
    original = instance.registrationNumber
    instance.registrationNumber = original
    assert instance.registrationNumber == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=university::Computer_strategy)
@settings(max_examples=50)
def test_university::computer_instantiation(instance):
    assert isinstance(instance, university::Computer)

@given(instance=university::Module_strategy)
@settings(max_examples=50)
def test_university::module_instantiation(instance):
    assert isinstance(instance, university::Module)

@given(instance=university::University_strategy)
@settings(max_examples=50)
def test_university::university_instantiation(instance):
    assert isinstance(instance, university::University)

@given(instance=university::Library_strategy)
@settings(max_examples=50)
def test_university::library_instantiation(instance):
    assert isinstance(instance, university::Library)

@given(instance=university::Department_strategy)
@settings(max_examples=50)
def test_university::department_instantiation(instance):
    assert isinstance(instance, university::Department)

@given(instance=university::Student_strategy)
@settings(max_examples=50)
def test_university::student_instantiation(instance):
    assert isinstance(instance, university::Student)

@given(instance=university::Student_strategy)
def test_university::student_studentId_type(instance):
    assert isinstance(instance.studentId, float)


@given(instance=university::Student_strategy)
def test_university::student_studentId_setter(instance):
    original = instance.studentId
    instance.studentId = original
    assert instance.studentId == original

@given(instance=university::StaffMember_strategy)
@settings(max_examples=50)
def test_university::staffmember_instantiation(instance):
    assert isinstance(instance, university::StaffMember)

@given(instance=university::StaffMember_strategy)
def test_university::staffmember_staffMemberType_type(instance):
    assert isinstance(instance.staffMemberType, str)


@given(instance=university::StaffMember_strategy)
def test_university::staffmember_staffMemberType_setter(instance):
    original = instance.staffMemberType
    instance.staffMemberType = original
    assert instance.staffMemberType == original

@given(instance=university::Book_strategy)
@settings(max_examples=50)
def test_university::book_instantiation(instance):
    assert isinstance(instance, university::Book)

@given(instance=university::Book_strategy)
def test_university::book_ISBN_type(instance):
    assert isinstance(instance.ISBN, str)


@given(instance=university::Book_strategy)
def test_university::book_ISBN_setter(instance):
    original = instance.ISBN
    instance.ISBN = original
    assert instance.ISBN == original

@given(instance=university::Book_strategy)
def test_university::book_authorNames_type(instance):
    assert isinstance(instance.authorNames, str)


@given(instance=university::Book_strategy)
def test_university::book_authorNames_setter(instance):
    original = instance.authorNames
    instance.authorNames = original
    assert instance.authorNames == original
