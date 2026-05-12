import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    c2,
    MyClass2,
    asdfa2,
    ServiceCourse2,
    Course2,
    c1,
    c,
    MyClass,
    asdfa,
    ServiceCourse,
    Course,
    c31,
    c3,
    MyClass3,
    asdfa3,
    ServiceCourse3,
    Course3,
    c21,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_c2_is_not_abstract():
    assert not inspect.isabstract(c2)


def test_c2_constructor_exists():
    assert callable(c2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(c2.__init__)
    params = list(sig.parameters.keys())



def test_myclass2_is_not_abstract():
    assert not inspect.isabstract(MyClass2)


def test_myclass2_constructor_exists():
    assert callable(MyClass2.__init__)


def test_myclass2_constructor_args():
    sig = inspect.signature(MyClass2.__init__)
    params = list(sig.parameters.keys())



def test_asdfa2_is_not_abstract():
    assert not inspect.isabstract(asdfa2)


def test_asdfa2_constructor_exists():
    assert callable(asdfa2.__init__)


def test_asdfa2_constructor_args():
    sig = inspect.signature(asdfa2.__init__)
    params = list(sig.parameters.keys())



def test_servicecourse2_is_not_abstract():
    assert not inspect.isabstract(ServiceCourse2)


def test_servicecourse2_constructor_exists():
    assert callable(ServiceCourse2.__init__)


def test_servicecourse2_constructor_args():
    sig = inspect.signature(ServiceCourse2.__init__)
    params = list(sig.parameters.keys())
    assert "attribute8" in params, "Missing parameter 'attribute8'"
    assert "attribute6" in params, "Missing parameter 'attribute6'"
    assert "attribute7" in params, "Missing parameter 'attribute7'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute4" in params, "Missing parameter 'attribute4'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute3" in params, "Missing parameter 'attribute3'"

def test_servicecourse2_has_attribute8():
    assert hasattr(ServiceCourse2, "attribute8")
    descriptor = None
    for klass in ServiceCourse2.__mro__:
        if "attribute8" in klass.__dict__:
            descriptor = klass.__dict__["attribute8"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse2_has_attribute6():
    assert hasattr(ServiceCourse2, "attribute6")
    descriptor = None
    for klass in ServiceCourse2.__mro__:
        if "attribute6" in klass.__dict__:
            descriptor = klass.__dict__["attribute6"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse2_has_attribute7():
    assert hasattr(ServiceCourse2, "attribute7")
    descriptor = None
    for klass in ServiceCourse2.__mro__:
        if "attribute7" in klass.__dict__:
            descriptor = klass.__dict__["attribute7"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse2_has_attribute2():
    assert hasattr(ServiceCourse2, "attribute2")
    descriptor = None
    for klass in ServiceCourse2.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse2_has_attribute4():
    assert hasattr(ServiceCourse2, "attribute4")
    descriptor = None
    for klass in ServiceCourse2.__mro__:
        if "attribute4" in klass.__dict__:
            descriptor = klass.__dict__["attribute4"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse2_has_attribute5():
    assert hasattr(ServiceCourse2, "attribute5")
    descriptor = None
    for klass in ServiceCourse2.__mro__:
        if "attribute5" in klass.__dict__:
            descriptor = klass.__dict__["attribute5"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse2_has_attribute():
    assert hasattr(ServiceCourse2, "attribute")
    descriptor = None
    for klass in ServiceCourse2.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse2_has_attribute3():
    assert hasattr(ServiceCourse2, "attribute3")
    descriptor = None
    for klass in ServiceCourse2.__mro__:
        if "attribute3" in klass.__dict__:
            descriptor = klass.__dict__["attribute3"]
            break
    assert isinstance(descriptor, property)



def test_course2_is_not_abstract():
    assert not inspect.isabstract(Course2)


def test_course2_constructor_exists():
    assert callable(Course2.__init__)


def test_course2_constructor_args():
    sig = inspect.signature(Course2.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "StartDate" in params, "Missing parameter 'StartDate'"

def test_course2_has_Id():
    assert hasattr(Course2, "Id")
    descriptor = None
    for klass in Course2.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_course2_has_Name():
    assert hasattr(Course2, "Name")
    descriptor = None
    for klass in Course2.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_course2_has_StartDate():
    assert hasattr(Course2, "StartDate")
    descriptor = None
    for klass in Course2.__mro__:
        if "StartDate" in klass.__dict__:
            descriptor = klass.__dict__["StartDate"]
            break
    assert isinstance(descriptor, property)



def test_c1_is_not_abstract():
    assert not inspect.isabstract(c1)


def test_c1_constructor_exists():
    assert callable(c1.__init__)


def test_c1_constructor_args():
    sig = inspect.signature(c1.__init__)
    params = list(sig.parameters.keys())



def test_c_is_not_abstract():
    assert not inspect.isabstract(c)


def test_c_constructor_exists():
    assert callable(c.__init__)


def test_c_constructor_args():
    sig = inspect.signature(c.__init__)
    params = list(sig.parameters.keys())



def test_myclass_is_not_abstract():
    assert not inspect.isabstract(MyClass)


def test_myclass_constructor_exists():
    assert callable(MyClass.__init__)


def test_myclass_constructor_args():
    sig = inspect.signature(MyClass.__init__)
    params = list(sig.parameters.keys())



def test_asdfa_is_not_abstract():
    assert not inspect.isabstract(asdfa)


def test_asdfa_constructor_exists():
    assert callable(asdfa.__init__)


def test_asdfa_constructor_args():
    sig = inspect.signature(asdfa.__init__)
    params = list(sig.parameters.keys())



def test_servicecourse_is_not_abstract():
    assert not inspect.isabstract(ServiceCourse)


def test_servicecourse_constructor_exists():
    assert callable(ServiceCourse.__init__)


def test_servicecourse_constructor_args():
    sig = inspect.signature(ServiceCourse.__init__)
    params = list(sig.parameters.keys())
    assert "attribute7" in params, "Missing parameter 'attribute7'"
    assert "attribute8" in params, "Missing parameter 'attribute8'"
    assert "attribute6" in params, "Missing parameter 'attribute6'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute4" in params, "Missing parameter 'attribute4'"
    assert "attribute3" in params, "Missing parameter 'attribute3'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"

def test_servicecourse_has_attribute7():
    assert hasattr(ServiceCourse, "attribute7")
    descriptor = None
    for klass in ServiceCourse.__mro__:
        if "attribute7" in klass.__dict__:
            descriptor = klass.__dict__["attribute7"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse_has_attribute8():
    assert hasattr(ServiceCourse, "attribute8")
    descriptor = None
    for klass in ServiceCourse.__mro__:
        if "attribute8" in klass.__dict__:
            descriptor = klass.__dict__["attribute8"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse_has_attribute6():
    assert hasattr(ServiceCourse, "attribute6")
    descriptor = None
    for klass in ServiceCourse.__mro__:
        if "attribute6" in klass.__dict__:
            descriptor = klass.__dict__["attribute6"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse_has_attribute():
    assert hasattr(ServiceCourse, "attribute")
    descriptor = None
    for klass in ServiceCourse.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse_has_attribute2():
    assert hasattr(ServiceCourse, "attribute2")
    descriptor = None
    for klass in ServiceCourse.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse_has_attribute4():
    assert hasattr(ServiceCourse, "attribute4")
    descriptor = None
    for klass in ServiceCourse.__mro__:
        if "attribute4" in klass.__dict__:
            descriptor = klass.__dict__["attribute4"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse_has_attribute3():
    assert hasattr(ServiceCourse, "attribute3")
    descriptor = None
    for klass in ServiceCourse.__mro__:
        if "attribute3" in klass.__dict__:
            descriptor = klass.__dict__["attribute3"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse_has_attribute5():
    assert hasattr(ServiceCourse, "attribute5")
    descriptor = None
    for klass in ServiceCourse.__mro__:
        if "attribute5" in klass.__dict__:
            descriptor = klass.__dict__["attribute5"]
            break
    assert isinstance(descriptor, property)



def test_course_is_not_abstract():
    assert not inspect.isabstract(Course)


def test_course_constructor_exists():
    assert callable(Course.__init__)


def test_course_constructor_args():
    sig = inspect.signature(Course.__init__)
    params = list(sig.parameters.keys())
    assert "StartDate" in params, "Missing parameter 'StartDate'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_course_has_StartDate():
    assert hasattr(Course, "StartDate")
    descriptor = None
    for klass in Course.__mro__:
        if "StartDate" in klass.__dict__:
            descriptor = klass.__dict__["StartDate"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Id():
    assert hasattr(Course, "Id")
    descriptor = None
    for klass in Course.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_course_has_Name():
    assert hasattr(Course, "Name")
    descriptor = None
    for klass in Course.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_c31_is_not_abstract():
    assert not inspect.isabstract(c31)


def test_c31_constructor_exists():
    assert callable(c31.__init__)


def test_c31_constructor_args():
    sig = inspect.signature(c31.__init__)
    params = list(sig.parameters.keys())



def test_c3_is_not_abstract():
    assert not inspect.isabstract(c3)


def test_c3_constructor_exists():
    assert callable(c3.__init__)


def test_c3_constructor_args():
    sig = inspect.signature(c3.__init__)
    params = list(sig.parameters.keys())



def test_myclass3_is_not_abstract():
    assert not inspect.isabstract(MyClass3)


def test_myclass3_constructor_exists():
    assert callable(MyClass3.__init__)


def test_myclass3_constructor_args():
    sig = inspect.signature(MyClass3.__init__)
    params = list(sig.parameters.keys())



def test_asdfa3_is_not_abstract():
    assert not inspect.isabstract(asdfa3)


def test_asdfa3_constructor_exists():
    assert callable(asdfa3.__init__)


def test_asdfa3_constructor_args():
    sig = inspect.signature(asdfa3.__init__)
    params = list(sig.parameters.keys())



def test_servicecourse3_is_not_abstract():
    assert not inspect.isabstract(ServiceCourse3)


def test_servicecourse3_constructor_exists():
    assert callable(ServiceCourse3.__init__)


def test_servicecourse3_constructor_args():
    sig = inspect.signature(ServiceCourse3.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute7" in params, "Missing parameter 'attribute7'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"
    assert "attribute3" in params, "Missing parameter 'attribute3'"
    assert "attribute8" in params, "Missing parameter 'attribute8'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "attribute6" in params, "Missing parameter 'attribute6'"
    assert "attribute4" in params, "Missing parameter 'attribute4'"

def test_servicecourse3_has_attribute2():
    assert hasattr(ServiceCourse3, "attribute2")
    descriptor = None
    for klass in ServiceCourse3.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse3_has_attribute7():
    assert hasattr(ServiceCourse3, "attribute7")
    descriptor = None
    for klass in ServiceCourse3.__mro__:
        if "attribute7" in klass.__dict__:
            descriptor = klass.__dict__["attribute7"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse3_has_attribute5():
    assert hasattr(ServiceCourse3, "attribute5")
    descriptor = None
    for klass in ServiceCourse3.__mro__:
        if "attribute5" in klass.__dict__:
            descriptor = klass.__dict__["attribute5"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse3_has_attribute3():
    assert hasattr(ServiceCourse3, "attribute3")
    descriptor = None
    for klass in ServiceCourse3.__mro__:
        if "attribute3" in klass.__dict__:
            descriptor = klass.__dict__["attribute3"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse3_has_attribute8():
    assert hasattr(ServiceCourse3, "attribute8")
    descriptor = None
    for klass in ServiceCourse3.__mro__:
        if "attribute8" in klass.__dict__:
            descriptor = klass.__dict__["attribute8"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse3_has_attribute():
    assert hasattr(ServiceCourse3, "attribute")
    descriptor = None
    for klass in ServiceCourse3.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse3_has_attribute6():
    assert hasattr(ServiceCourse3, "attribute6")
    descriptor = None
    for klass in ServiceCourse3.__mro__:
        if "attribute6" in klass.__dict__:
            descriptor = klass.__dict__["attribute6"]
            break
    assert isinstance(descriptor, property)

def test_servicecourse3_has_attribute4():
    assert hasattr(ServiceCourse3, "attribute4")
    descriptor = None
    for klass in ServiceCourse3.__mro__:
        if "attribute4" in klass.__dict__:
            descriptor = klass.__dict__["attribute4"]
            break
    assert isinstance(descriptor, property)



def test_course3_is_not_abstract():
    assert not inspect.isabstract(Course3)


def test_course3_constructor_exists():
    assert callable(Course3.__init__)


def test_course3_constructor_args():
    sig = inspect.signature(Course3.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "StartDate" in params, "Missing parameter 'StartDate'"

def test_course3_has_Name():
    assert hasattr(Course3, "Name")
    descriptor = None
    for klass in Course3.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_course3_has_Id():
    assert hasattr(Course3, "Id")
    descriptor = None
    for klass in Course3.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_course3_has_StartDate():
    assert hasattr(Course3, "StartDate")
    descriptor = None
    for klass in Course3.__mro__:
        if "StartDate" in klass.__dict__:
            descriptor = klass.__dict__["StartDate"]
            break
    assert isinstance(descriptor, property)



def test_c21_is_not_abstract():
    assert not inspect.isabstract(c21)


def test_c21_constructor_exists():
    assert callable(c21.__init__)


def test_c21_constructor_args():
    sig = inspect.signature(c21.__init__)
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
c2_strategy = st.builds(
    c2,
)
MyClass2_strategy = st.builds(
    MyClass2,
)
asdfa2_strategy = st.builds(
    asdfa2,
)
ServiceCourse2_strategy = st.builds(
    ServiceCourse2,
    attribute8=
        safe_text,
    attribute6=
        safe_text,
    attribute7=
        safe_text,
    attribute2=
        safe_text,
    attribute4=
        safe_text,
    attribute5=
        safe_text,
    attribute=
        safe_text,
    attribute3=
        safe_text
)
Course2_strategy = st.builds(
    Course2,
    Id=
        st.integers(),
    Name=
        safe_text,
    StartDate=
        safe_text
)
c1_strategy = st.builds(
    c1,
)
c_strategy = st.builds(
    c,
)
MyClass_strategy = st.builds(
    MyClass,
)
asdfa_strategy = st.builds(
    asdfa,
)
ServiceCourse_strategy = st.builds(
    ServiceCourse,
    attribute7=
        safe_text,
    attribute8=
        safe_text,
    attribute6=
        safe_text,
    attribute=
        safe_text,
    attribute2=
        safe_text,
    attribute4=
        safe_text,
    attribute3=
        safe_text,
    attribute5=
        safe_text
)
Course_strategy = st.builds(
    Course,
    StartDate=
        safe_text,
    Id=
        st.integers(),
    Name=
        safe_text
)
c31_strategy = st.builds(
    c31,
)
c3_strategy = st.builds(
    c3,
)
MyClass3_strategy = st.builds(
    MyClass3,
)
asdfa3_strategy = st.builds(
    asdfa3,
)
ServiceCourse3_strategy = st.builds(
    ServiceCourse3,
    attribute2=
        safe_text,
    attribute7=
        safe_text,
    attribute5=
        safe_text,
    attribute3=
        safe_text,
    attribute8=
        safe_text,
    attribute=
        safe_text,
    attribute6=
        safe_text,
    attribute4=
        safe_text
)
Course3_strategy = st.builds(
    Course3,
    Name=
        safe_text,
    Id=
        st.integers(),
    StartDate=
        safe_text
)
c21_strategy = st.builds(
    c21,
)

@given(instance=c2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, c2)

@given(instance=MyClass2_strategy)
@settings(max_examples=50)
def test_myclass2_instantiation(instance):
    assert isinstance(instance, MyClass2)

@given(instance=asdfa2_strategy)
@settings(max_examples=50)
def test_asdfa2_instantiation(instance):
    assert isinstance(instance, asdfa2)

@given(instance=ServiceCourse2_strategy)
@settings(max_examples=50)
def test_servicecourse2_instantiation(instance):
    assert isinstance(instance, ServiceCourse2)



@given(instance=ServiceCourse2_strategy)
def test_servicecourse2_attribute8_setter(instance):
    original = instance.attribute8
    instance.attribute8 = original
    assert instance.attribute8 == original



@given(instance=ServiceCourse2_strategy)
def test_servicecourse2_attribute6_setter(instance):
    original = instance.attribute6
    instance.attribute6 = original
    assert instance.attribute6 == original



@given(instance=ServiceCourse2_strategy)
def test_servicecourse2_attribute7_setter(instance):
    original = instance.attribute7
    instance.attribute7 = original
    assert instance.attribute7 == original



@given(instance=ServiceCourse2_strategy)
def test_servicecourse2_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=ServiceCourse2_strategy)
def test_servicecourse2_attribute4_setter(instance):
    original = instance.attribute4
    instance.attribute4 = original
    assert instance.attribute4 == original



@given(instance=ServiceCourse2_strategy)
def test_servicecourse2_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original



@given(instance=ServiceCourse2_strategy)
def test_servicecourse2_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=ServiceCourse2_strategy)
def test_servicecourse2_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original

@given(instance=Course2_strategy)
@settings(max_examples=50)
def test_course2_instantiation(instance):
    assert isinstance(instance, Course2)



@given(instance=Course2_strategy)
def test_course2_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Course2_strategy)
def test_course2_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Course2_strategy)
def test_course2_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original

@given(instance=c1_strategy)
@settings(max_examples=50)
def test_c1_instantiation(instance):
    assert isinstance(instance, c1)

@given(instance=c_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, c)

@given(instance=MyClass_strategy)
@settings(max_examples=50)
def test_myclass_instantiation(instance):
    assert isinstance(instance, MyClass)

@given(instance=asdfa_strategy)
@settings(max_examples=50)
def test_asdfa_instantiation(instance):
    assert isinstance(instance, asdfa)

@given(instance=ServiceCourse_strategy)
@settings(max_examples=50)
def test_servicecourse_instantiation(instance):
    assert isinstance(instance, ServiceCourse)



@given(instance=ServiceCourse_strategy)
def test_servicecourse_attribute7_setter(instance):
    original = instance.attribute7
    instance.attribute7 = original
    assert instance.attribute7 == original



@given(instance=ServiceCourse_strategy)
def test_servicecourse_attribute8_setter(instance):
    original = instance.attribute8
    instance.attribute8 = original
    assert instance.attribute8 == original



@given(instance=ServiceCourse_strategy)
def test_servicecourse_attribute6_setter(instance):
    original = instance.attribute6
    instance.attribute6 = original
    assert instance.attribute6 == original



@given(instance=ServiceCourse_strategy)
def test_servicecourse_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=ServiceCourse_strategy)
def test_servicecourse_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=ServiceCourse_strategy)
def test_servicecourse_attribute4_setter(instance):
    original = instance.attribute4
    instance.attribute4 = original
    assert instance.attribute4 == original



@given(instance=ServiceCourse_strategy)
def test_servicecourse_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original



@given(instance=ServiceCourse_strategy)
def test_servicecourse_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original

@given(instance=Course_strategy)
@settings(max_examples=50)
def test_course_instantiation(instance):
    assert isinstance(instance, Course)



@given(instance=Course_strategy)
def test_course_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original



@given(instance=Course_strategy)
def test_course_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Course_strategy)
def test_course_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=c31_strategy)
@settings(max_examples=50)
def test_c31_instantiation(instance):
    assert isinstance(instance, c31)

@given(instance=c3_strategy)
@settings(max_examples=50)
def test_c3_instantiation(instance):
    assert isinstance(instance, c3)

@given(instance=MyClass3_strategy)
@settings(max_examples=50)
def test_myclass3_instantiation(instance):
    assert isinstance(instance, MyClass3)

@given(instance=asdfa3_strategy)
@settings(max_examples=50)
def test_asdfa3_instantiation(instance):
    assert isinstance(instance, asdfa3)

@given(instance=ServiceCourse3_strategy)
@settings(max_examples=50)
def test_servicecourse3_instantiation(instance):
    assert isinstance(instance, ServiceCourse3)



@given(instance=ServiceCourse3_strategy)
def test_servicecourse3_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=ServiceCourse3_strategy)
def test_servicecourse3_attribute7_setter(instance):
    original = instance.attribute7
    instance.attribute7 = original
    assert instance.attribute7 == original



@given(instance=ServiceCourse3_strategy)
def test_servicecourse3_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original



@given(instance=ServiceCourse3_strategy)
def test_servicecourse3_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original



@given(instance=ServiceCourse3_strategy)
def test_servicecourse3_attribute8_setter(instance):
    original = instance.attribute8
    instance.attribute8 = original
    assert instance.attribute8 == original



@given(instance=ServiceCourse3_strategy)
def test_servicecourse3_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=ServiceCourse3_strategy)
def test_servicecourse3_attribute6_setter(instance):
    original = instance.attribute6
    instance.attribute6 = original
    assert instance.attribute6 == original



@given(instance=ServiceCourse3_strategy)
def test_servicecourse3_attribute4_setter(instance):
    original = instance.attribute4
    instance.attribute4 = original
    assert instance.attribute4 == original

@given(instance=Course3_strategy)
@settings(max_examples=50)
def test_course3_instantiation(instance):
    assert isinstance(instance, Course3)



@given(instance=Course3_strategy)
def test_course3_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Course3_strategy)
def test_course3_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Course3_strategy)
def test_course3_StartDate_setter(instance):
    original = instance.StartDate
    instance.StartDate = original
    assert instance.StartDate == original

@given(instance=c21_strategy)
@settings(max_examples=50)
def test_c21_instantiation(instance):
    assert isinstance(instance, c21)
