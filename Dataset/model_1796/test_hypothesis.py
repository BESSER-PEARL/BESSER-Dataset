import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    university_PrimitiveType,
    university_NamedElement,
    university_Vehicle,
    NamedElement,
    university_Department,
    university_Student,
    university_Computer,
    university_Book,
    university_Module,
    university_Library,
    university_StaffMember,
    university_University,
    StaffMemberType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_university_primitivetype_is_not_abstract():
    assert not inspect.isabstract(university_PrimitiveType)


def test_university_primitivetype_constructor_exists():
    assert callable(university_PrimitiveType.__init__)


def test_university_primitivetype_constructor_args():
    sig = inspect.signature(university_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "l" in params, "Missing parameter 'l'"
    assert "p" in params, "Missing parameter 'p'"
    assert "o" in params, "Missing parameter 'o'"
    assert "d" in params, "Missing parameter 'd'"
    assert "j" in params, "Missing parameter 'j'"
    assert "e" in params, "Missing parameter 'e'"
    assert "n" in params, "Missing parameter 'n'"
    assert "f" in params, "Missing parameter 'f'"
    assert "g" in params, "Missing parameter 'g'"
    assert "h" in params, "Missing parameter 'h'"
    assert "c" in params, "Missing parameter 'c'"
    assert "m" in params, "Missing parameter 'm'"
    assert "a" in params, "Missing parameter 'a'"
    assert "k" in params, "Missing parameter 'k'"
    assert "bigIntList" in params, "Missing parameter 'bigIntList'"
    assert "i" in params, "Missing parameter 'i'"

def test_university_primitivetype_has_b():
    assert hasattr(university_PrimitiveType, "b")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_l():
    assert hasattr(university_PrimitiveType, "l")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "l" in klass.__dict__:
            descriptor = klass.__dict__["l"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_p():
    assert hasattr(university_PrimitiveType, "p")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_o():
    assert hasattr(university_PrimitiveType, "o")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "o" in klass.__dict__:
            descriptor = klass.__dict__["o"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_d():
    assert hasattr(university_PrimitiveType, "d")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_j():
    assert hasattr(university_PrimitiveType, "j")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "j" in klass.__dict__:
            descriptor = klass.__dict__["j"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_e():
    assert hasattr(university_PrimitiveType, "e")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "e" in klass.__dict__:
            descriptor = klass.__dict__["e"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_n():
    assert hasattr(university_PrimitiveType, "n")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_f():
    assert hasattr(university_PrimitiveType, "f")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "f" in klass.__dict__:
            descriptor = klass.__dict__["f"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_g():
    assert hasattr(university_PrimitiveType, "g")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_h():
    assert hasattr(university_PrimitiveType, "h")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "h" in klass.__dict__:
            descriptor = klass.__dict__["h"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_c():
    assert hasattr(university_PrimitiveType, "c")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_m():
    assert hasattr(university_PrimitiveType, "m")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "m" in klass.__dict__:
            descriptor = klass.__dict__["m"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_a():
    assert hasattr(university_PrimitiveType, "a")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_k():
    assert hasattr(university_PrimitiveType, "k")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "k" in klass.__dict__:
            descriptor = klass.__dict__["k"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_bigIntList():
    assert hasattr(university_PrimitiveType, "bigIntList")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "bigIntList" in klass.__dict__:
            descriptor = klass.__dict__["bigIntList"]
            break
    assert isinstance(descriptor, property)

def test_university_primitivetype_has_i():
    assert hasattr(university_PrimitiveType, "i")
    descriptor = None
    for klass in university_PrimitiveType.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
            break
    assert isinstance(descriptor, property)



def test_university_namedelement_is_not_abstract():
    assert not inspect.isabstract(university_NamedElement)


def test_university_namedelement_constructor_exists():
    assert callable(university_NamedElement.__init__)


def test_university_namedelement_constructor_args():
    sig = inspect.signature(university_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_university_namedelement_has_name():
    assert hasattr(university_NamedElement, "name")
    descriptor = None
    for klass in university_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_university_vehicle_is_not_abstract():
    assert not inspect.isabstract(university_Vehicle)


def test_university_vehicle_constructor_exists():
    assert callable(university_Vehicle.__init__)


def test_university_vehicle_constructor_args():
    sig = inspect.signature(university_Vehicle.__init__)
    params = list(sig.parameters.keys())
    assert "registrationNumber" in params, "Missing parameter 'registrationNumber'"

def test_university_vehicle_has_registrationNumber():
    assert hasattr(university_Vehicle, "registrationNumber")
    descriptor = None
    for klass in university_Vehicle.__mro__:
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



def test_university_department_is_not_abstract():
    assert not inspect.isabstract(university_Department)


def test_university_department_constructor_exists():
    assert callable(university_Department.__init__)


def test_university_department_constructor_args():
    sig = inspect.signature(university_Department.__init__)
    params = list(sig.parameters.keys())



def test_university_student_is_not_abstract():
    assert not inspect.isabstract(university_Student)


def test_university_student_constructor_exists():
    assert callable(university_Student.__init__)


def test_university_student_constructor_args():
    sig = inspect.signature(university_Student.__init__)
    params = list(sig.parameters.keys())
    assert "studentId" in params, "Missing parameter 'studentId'"

def test_university_student_has_studentId():
    assert hasattr(university_Student, "studentId")
    descriptor = None
    for klass in university_Student.__mro__:
        if "studentId" in klass.__dict__:
            descriptor = klass.__dict__["studentId"]
            break
    assert isinstance(descriptor, property)



def test_university_computer_is_not_abstract():
    assert not inspect.isabstract(university_Computer)


def test_university_computer_constructor_exists():
    assert callable(university_Computer.__init__)


def test_university_computer_constructor_args():
    sig = inspect.signature(university_Computer.__init__)
    params = list(sig.parameters.keys())



def test_university_book_is_not_abstract():
    assert not inspect.isabstract(university_Book)


def test_university_book_constructor_exists():
    assert callable(university_Book.__init__)


def test_university_book_constructor_args():
    sig = inspect.signature(university_Book.__init__)
    params = list(sig.parameters.keys())
    assert "authorNames" in params, "Missing parameter 'authorNames'"
    assert "ISBN" in params, "Missing parameter 'ISBN'"

def test_university_book_has_authorNames():
    assert hasattr(university_Book, "authorNames")
    descriptor = None
    for klass in university_Book.__mro__:
        if "authorNames" in klass.__dict__:
            descriptor = klass.__dict__["authorNames"]
            break
    assert isinstance(descriptor, property)

def test_university_book_has_ISBN():
    assert hasattr(university_Book, "ISBN")
    descriptor = None
    for klass in university_Book.__mro__:
        if "ISBN" in klass.__dict__:
            descriptor = klass.__dict__["ISBN"]
            break
    assert isinstance(descriptor, property)



def test_university_module_is_not_abstract():
    assert not inspect.isabstract(university_Module)


def test_university_module_constructor_exists():
    assert callable(university_Module.__init__)


def test_university_module_constructor_args():
    sig = inspect.signature(university_Module.__init__)
    params = list(sig.parameters.keys())



def test_university_library_is_not_abstract():
    assert not inspect.isabstract(university_Library)


def test_university_library_constructor_exists():
    assert callable(university_Library.__init__)


def test_university_library_constructor_args():
    sig = inspect.signature(university_Library.__init__)
    params = list(sig.parameters.keys())



def test_university_staffmember_is_not_abstract():
    assert not inspect.isabstract(university_StaffMember)


def test_university_staffmember_constructor_exists():
    assert callable(university_StaffMember.__init__)


def test_university_staffmember_constructor_args():
    sig = inspect.signature(university_StaffMember.__init__)
    params = list(sig.parameters.keys())
    assert "staffMemberType" in params, "Missing parameter 'staffMemberType'"

def test_university_staffmember_has_staffMemberType():
    assert hasattr(university_StaffMember, "staffMemberType")
    descriptor = None
    for klass in university_StaffMember.__mro__:
        if "staffMemberType" in klass.__dict__:
            descriptor = klass.__dict__["staffMemberType"]
            break
    assert isinstance(descriptor, property)



def test_university_university_is_not_abstract():
    assert not inspect.isabstract(university_University)


def test_university_university_constructor_exists():
    assert callable(university_University.__init__)


def test_university_university_constructor_args():
    sig = inspect.signature(university_University.__init__)
    params = list(sig.parameters.keys())

def test_staffmembertype_exists():
    # Check that the Enumeration exists
    assert StaffMemberType is not None

def test_staffmembertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StaffMemberType]
    expected_literals = [
        "Academic",
        "Technical",
        "ResearchStudent",
        "Honary",
        "Admin",
        "Research",
        "Other",
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
university_PrimitiveType_strategy = st.builds(
    university_PrimitiveType,
    b=
        st.integers(),
    l=
        safe_text,
    p=
        safe_text,
    o=
        safe_text,
    d=
        st.booleans(),
    j=
        safe_text,
    e=
        safe_text,
    n=
        safe_text,
    f=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    g=
        safe_text,
    h=
        safe_text,
    c=
        safe_text,
    m=
        safe_text,
    a=
        safe_text,
    k=
        safe_text,
    bigIntList=
        safe_text,
    i=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
university_NamedElement_strategy = st.builds(
    university_NamedElement,
    name=
        safe_text
)
university_Vehicle_strategy = st.builds(
    university_Vehicle,
    registrationNumber=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
university_Department_strategy = st.builds(
    university_Department,
)
university_Student_strategy = st.builds(
    university_Student,
    studentId=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
university_Computer_strategy = st.builds(
    university_Computer,
)
university_Book_strategy = st.builds(
    university_Book,
    authorNames=
        safe_text,
    ISBN=
        safe_text
)
university_Module_strategy = st.builds(
    university_Module,
)
university_Library_strategy = st.builds(
    university_Library,
)
university_StaffMember_strategy = st.builds(
    university_StaffMember,
    staffMemberType=
        safe_text
)
university_University_strategy = st.builds(
    university_University,
)

@given(instance=university_PrimitiveType_strategy)
@settings(max_examples=50)
def test_university_primitivetype_instantiation(instance):
    assert isinstance(instance, university_PrimitiveType)



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_l_setter(instance):
    original = instance.l
    instance.l = original
    assert instance.l == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_o_setter(instance):
    original = instance.o
    instance.o = original
    assert instance.o == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_j_setter(instance):
    original = instance.j
    instance.j = original
    assert instance.j == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_e_setter(instance):
    original = instance.e
    instance.e = original
    assert instance.e == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_f_setter(instance):
    original = instance.f
    instance.f = original
    assert instance.f == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_h_setter(instance):
    original = instance.h
    instance.h = original
    assert instance.h == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_m_setter(instance):
    original = instance.m
    instance.m = original
    assert instance.m == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_k_setter(instance):
    original = instance.k
    instance.k = original
    assert instance.k == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_bigIntList_setter(instance):
    original = instance.bigIntList
    instance.bigIntList = original
    assert instance.bigIntList == original



@given(instance=university_PrimitiveType_strategy)
def test_university_primitivetype_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=university_NamedElement_strategy)
@settings(max_examples=50)
def test_university_namedelement_instantiation(instance):
    assert isinstance(instance, university_NamedElement)



@given(instance=university_NamedElement_strategy)
def test_university_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=university_Vehicle_strategy)
@settings(max_examples=50)
def test_university_vehicle_instantiation(instance):
    assert isinstance(instance, university_Vehicle)



@given(instance=university_Vehicle_strategy)
def test_university_vehicle_registrationNumber_setter(instance):
    original = instance.registrationNumber
    instance.registrationNumber = original
    assert instance.registrationNumber == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=university_Department_strategy)
@settings(max_examples=50)
def test_university_department_instantiation(instance):
    assert isinstance(instance, university_Department)

@given(instance=university_Student_strategy)
@settings(max_examples=50)
def test_university_student_instantiation(instance):
    assert isinstance(instance, university_Student)



@given(instance=university_Student_strategy)
def test_university_student_studentId_setter(instance):
    original = instance.studentId
    instance.studentId = original
    assert instance.studentId == original

@given(instance=university_Computer_strategy)
@settings(max_examples=50)
def test_university_computer_instantiation(instance):
    assert isinstance(instance, university_Computer)

@given(instance=university_Book_strategy)
@settings(max_examples=50)
def test_university_book_instantiation(instance):
    assert isinstance(instance, university_Book)



@given(instance=university_Book_strategy)
def test_university_book_authorNames_setter(instance):
    original = instance.authorNames
    instance.authorNames = original
    assert instance.authorNames == original



@given(instance=university_Book_strategy)
def test_university_book_ISBN_setter(instance):
    original = instance.ISBN
    instance.ISBN = original
    assert instance.ISBN == original

@given(instance=university_Module_strategy)
@settings(max_examples=50)
def test_university_module_instantiation(instance):
    assert isinstance(instance, university_Module)

@given(instance=university_Library_strategy)
@settings(max_examples=50)
def test_university_library_instantiation(instance):
    assert isinstance(instance, university_Library)

@given(instance=university_StaffMember_strategy)
@settings(max_examples=50)
def test_university_staffmember_instantiation(instance):
    assert isinstance(instance, university_StaffMember)



@given(instance=university_StaffMember_strategy)
def test_university_staffmember_staffMemberType_setter(instance):
    original = instance.staffMemberType
    instance.staffMemberType = original
    assert instance.staffMemberType == original

@given(instance=university_University_strategy)
@settings(max_examples=50)
def test_university_university_instantiation(instance):
    assert isinstance(instance, university_University)
