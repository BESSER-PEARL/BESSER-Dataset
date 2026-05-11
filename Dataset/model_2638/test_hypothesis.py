import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model3::Diagram,
    subpackage::model3::Class1,
    model3::subpackage::Class2,
    model3::NodeD,
    EdgeTarget,
    model3::NodeF,
    model3::Edge,
    model3::EdgeTarget,
    model3::ClassWithTransientContainment,
    model3::ClassWithJavaObjectAttribute,
    model3::ClassWithJavaClassAttribute,
    model3::ClassWithIDAttribute,
    model3::File,
    model3::Image,
    model3::NodeE,
    model3::NodeC,
    model3::NodeB,
    model3::NodeA,
    model3::PolygonWithDuplicates,
    model3::Polygon,
    model3::EReference,
    model3::EClass,
    model3::EPackage,
    model3::MetaRef,
    Class2,
    model3::Class1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model3::diagram_is_not_abstract():
    assert not inspect.isabstract(model3::Diagram)


def test_model3::diagram_constructor_exists():
    assert callable(model3::Diagram.__init__)


def test_model3::diagram_constructor_args():
    sig = inspect.signature(model3::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_subpackage::model3::class1_is_not_abstract():
    assert not inspect.isabstract(subpackage::model3::Class1)


def test_subpackage::model3::class1_constructor_exists():
    assert callable(subpackage::model3::Class1.__init__)


def test_subpackage::model3::class1_constructor_args():
    sig = inspect.signature(subpackage::model3::Class1.__init__)
    params = list(sig.parameters.keys())



def test_model3::subpackage::class2_is_not_abstract():
    assert not inspect.isabstract(model3::subpackage::Class2)


def test_model3::subpackage::class2_constructor_exists():
    assert callable(model3::subpackage::Class2.__init__)


def test_model3::subpackage::class2_constructor_args():
    sig = inspect.signature(model3::subpackage::Class2.__init__)
    params = list(sig.parameters.keys())



def test_model3::noded_is_not_abstract():
    assert not inspect.isabstract(model3::NodeD)


def test_model3::noded_constructor_exists():
    assert callable(model3::NodeD.__init__)


def test_model3::noded_constructor_args():
    sig = inspect.signature(model3::NodeD.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model3::noded_has_name():
    assert hasattr(model3::NodeD, "name")
    descriptor = None
    for klass in model3::NodeD.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_edgetarget_is_not_abstract():
    assert not inspect.isabstract(EdgeTarget)


def test_edgetarget_constructor_exists():
    assert callable(EdgeTarget.__init__)


def test_edgetarget_constructor_args():
    sig = inspect.signature(EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_model3::nodef_is_not_abstract():
    assert not inspect.isabstract(model3::NodeF)


def test_model3::nodef_constructor_exists():
    assert callable(model3::NodeF.__init__)


def test_model3::nodef_constructor_args():
    sig = inspect.signature(model3::NodeF.__init__)
    params = list(sig.parameters.keys())



def test_model3::edge_is_not_abstract():
    assert not inspect.isabstract(model3::Edge)


def test_model3::edge_constructor_exists():
    assert callable(model3::Edge.__init__)


def test_model3::edge_constructor_args():
    sig = inspect.signature(model3::Edge.__init__)
    params = list(sig.parameters.keys())



def test_model3::edgetarget_is_not_abstract():
    assert not inspect.isabstract(model3::EdgeTarget)


def test_model3::edgetarget_constructor_exists():
    assert callable(model3::EdgeTarget.__init__)


def test_model3::edgetarget_constructor_args():
    sig = inspect.signature(model3::EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_model3::classwithtransientcontainment_is_not_abstract():
    assert not inspect.isabstract(model3::ClassWithTransientContainment)


def test_model3::classwithtransientcontainment_constructor_exists():
    assert callable(model3::ClassWithTransientContainment.__init__)


def test_model3::classwithtransientcontainment_constructor_args():
    sig = inspect.signature(model3::ClassWithTransientContainment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model3::classwithtransientcontainment_has_name():
    assert hasattr(model3::ClassWithTransientContainment, "name")
    descriptor = None
    for klass in model3::ClassWithTransientContainment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model3::classwithjavaobjectattribute_is_not_abstract():
    assert not inspect.isabstract(model3::ClassWithJavaObjectAttribute)


def test_model3::classwithjavaobjectattribute_constructor_exists():
    assert callable(model3::ClassWithJavaObjectAttribute.__init__)


def test_model3::classwithjavaobjectattribute_constructor_args():
    sig = inspect.signature(model3::ClassWithJavaObjectAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "javaObject" in params, "Missing parameter 'javaObject'"

def test_model3::classwithjavaobjectattribute_has_javaObject():
    assert hasattr(model3::ClassWithJavaObjectAttribute, "javaObject")
    descriptor = None
    for klass in model3::ClassWithJavaObjectAttribute.__mro__:
        if "javaObject" in klass.__dict__:
            descriptor = klass.__dict__["javaObject"]
            break
    assert isinstance(descriptor, property)



def test_model3::classwithjavaclassattribute_is_not_abstract():
    assert not inspect.isabstract(model3::ClassWithJavaClassAttribute)


def test_model3::classwithjavaclassattribute_constructor_exists():
    assert callable(model3::ClassWithJavaClassAttribute.__init__)


def test_model3::classwithjavaclassattribute_constructor_args():
    sig = inspect.signature(model3::ClassWithJavaClassAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "javaClass" in params, "Missing parameter 'javaClass'"

def test_model3::classwithjavaclassattribute_has_javaClass():
    assert hasattr(model3::ClassWithJavaClassAttribute, "javaClass")
    descriptor = None
    for klass in model3::ClassWithJavaClassAttribute.__mro__:
        if "javaClass" in klass.__dict__:
            descriptor = klass.__dict__["javaClass"]
            break
    assert isinstance(descriptor, property)



def test_model3::classwithidattribute_is_not_abstract():
    assert not inspect.isabstract(model3::ClassWithIDAttribute)


def test_model3::classwithidattribute_constructor_exists():
    assert callable(model3::ClassWithIDAttribute.__init__)


def test_model3::classwithidattribute_constructor_args():
    sig = inspect.signature(model3::ClassWithIDAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_model3::classwithidattribute_has_id():
    assert hasattr(model3::ClassWithIDAttribute, "id")
    descriptor = None
    for klass in model3::ClassWithIDAttribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_model3::file_is_not_abstract():
    assert not inspect.isabstract(model3::File)


def test_model3::file_constructor_exists():
    assert callable(model3::File.__init__)


def test_model3::file_constructor_args():
    sig = inspect.signature(model3::File.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "name" in params, "Missing parameter 'name'"

def test_model3::file_has_data():
    assert hasattr(model3::File, "data")
    descriptor = None
    for klass in model3::File.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_model3::file_has_name():
    assert hasattr(model3::File, "name")
    descriptor = None
    for klass in model3::File.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model3::image_is_not_abstract():
    assert not inspect.isabstract(model3::Image)


def test_model3::image_constructor_exists():
    assert callable(model3::Image.__init__)


def test_model3::image_constructor_args():
    sig = inspect.signature(model3::Image.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "data" in params, "Missing parameter 'data'"
    assert "width" in params, "Missing parameter 'width'"

def test_model3::image_has_height():
    assert hasattr(model3::Image, "height")
    descriptor = None
    for klass in model3::Image.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_model3::image_has_data():
    assert hasattr(model3::Image, "data")
    descriptor = None
    for klass in model3::Image.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_model3::image_has_width():
    assert hasattr(model3::Image, "width")
    descriptor = None
    for klass in model3::Image.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_model3::nodee_is_not_abstract():
    assert not inspect.isabstract(model3::NodeE)


def test_model3::nodee_constructor_exists():
    assert callable(model3::NodeE.__init__)


def test_model3::nodee_constructor_args():
    sig = inspect.signature(model3::NodeE.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model3::nodee_has_name():
    assert hasattr(model3::NodeE, "name")
    descriptor = None
    for klass in model3::NodeE.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model3::nodec_is_not_abstract():
    assert not inspect.isabstract(model3::NodeC)


def test_model3::nodec_constructor_exists():
    assert callable(model3::NodeC.__init__)


def test_model3::nodec_constructor_args():
    sig = inspect.signature(model3::NodeC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model3::nodec_has_name():
    assert hasattr(model3::NodeC, "name")
    descriptor = None
    for klass in model3::NodeC.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model3::nodeb_is_not_abstract():
    assert not inspect.isabstract(model3::NodeB)


def test_model3::nodeb_constructor_exists():
    assert callable(model3::NodeB.__init__)


def test_model3::nodeb_constructor_args():
    sig = inspect.signature(model3::NodeB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model3::nodeb_has_name():
    assert hasattr(model3::NodeB, "name")
    descriptor = None
    for klass in model3::NodeB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model3::nodea_is_not_abstract():
    assert not inspect.isabstract(model3::NodeA)


def test_model3::nodea_constructor_exists():
    assert callable(model3::NodeA.__init__)


def test_model3::nodea_constructor_args():
    sig = inspect.signature(model3::NodeA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model3::nodea_has_name():
    assert hasattr(model3::NodeA, "name")
    descriptor = None
    for klass in model3::NodeA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model3::polygonwithduplicates_is_not_abstract():
    assert not inspect.isabstract(model3::PolygonWithDuplicates)


def test_model3::polygonwithduplicates_constructor_exists():
    assert callable(model3::PolygonWithDuplicates.__init__)


def test_model3::polygonwithduplicates_constructor_args():
    sig = inspect.signature(model3::PolygonWithDuplicates.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"

def test_model3::polygonwithduplicates_has_points():
    assert hasattr(model3::PolygonWithDuplicates, "points")
    descriptor = None
    for klass in model3::PolygonWithDuplicates.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)



def test_model3::polygon_is_not_abstract():
    assert not inspect.isabstract(model3::Polygon)


def test_model3::polygon_constructor_exists():
    assert callable(model3::Polygon.__init__)


def test_model3::polygon_constructor_args():
    sig = inspect.signature(model3::Polygon.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"

def test_model3::polygon_has_points():
    assert hasattr(model3::Polygon, "points")
    descriptor = None
    for klass in model3::Polygon.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)



def test_model3::ereference_is_not_abstract():
    assert not inspect.isabstract(model3::EReference)


def test_model3::ereference_constructor_exists():
    assert callable(model3::EReference.__init__)


def test_model3::ereference_constructor_args():
    sig = inspect.signature(model3::EReference.__init__)
    params = list(sig.parameters.keys())



def test_model3::eclass_is_not_abstract():
    assert not inspect.isabstract(model3::EClass)


def test_model3::eclass_constructor_exists():
    assert callable(model3::EClass.__init__)


def test_model3::eclass_constructor_args():
    sig = inspect.signature(model3::EClass.__init__)
    params = list(sig.parameters.keys())



def test_model3::epackage_is_not_abstract():
    assert not inspect.isabstract(model3::EPackage)


def test_model3::epackage_constructor_exists():
    assert callable(model3::EPackage.__init__)


def test_model3::epackage_constructor_args():
    sig = inspect.signature(model3::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_model3::metaref_is_not_abstract():
    assert not inspect.isabstract(model3::MetaRef)


def test_model3::metaref_constructor_exists():
    assert callable(model3::MetaRef.__init__)


def test_model3::metaref_constructor_args():
    sig = inspect.signature(model3::MetaRef.__init__)
    params = list(sig.parameters.keys())



def test_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_model3::class1_is_not_abstract():
    assert not inspect.isabstract(model3::Class1)


def test_model3::class1_constructor_exists():
    assert callable(model3::Class1.__init__)


def test_model3::class1_constructor_args():
    sig = inspect.signature(model3::Class1.__init__)
    params = list(sig.parameters.keys())
    assert "additionalValue" in params, "Missing parameter 'additionalValue'"

def test_model3::class1_has_additionalValue():
    assert hasattr(model3::Class1, "additionalValue")
    descriptor = None
    for klass in model3::Class1.__mro__:
        if "additionalValue" in klass.__dict__:
            descriptor = klass.__dict__["additionalValue"]
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
model3::Diagram_strategy = st.builds(
    model3::Diagram,
)
subpackage::model3::Class1_strategy = st.builds(
    subpackage::model3::Class1,
)
model3::subpackage::Class2_strategy = st.builds(
    model3::subpackage::Class2,
)
model3::NodeD_strategy = st.builds(
    model3::NodeD,
    name=
        safe_text
)
EdgeTarget_strategy = st.builds(
    EdgeTarget,
)
model3::NodeF_strategy = st.builds(
    model3::NodeF,
)
model3::Edge_strategy = st.builds(
    model3::Edge,
)
model3::EdgeTarget_strategy = st.builds(
    model3::EdgeTarget,
)
model3::ClassWithTransientContainment_strategy = st.builds(
    model3::ClassWithTransientContainment,
    name=
        safe_text
)
model3::ClassWithJavaObjectAttribute_strategy = st.builds(
    model3::ClassWithJavaObjectAttribute,
    javaObject=
        safe_text
)
model3::ClassWithJavaClassAttribute_strategy = st.builds(
    model3::ClassWithJavaClassAttribute,
    javaClass=
        safe_text
)
model3::ClassWithIDAttribute_strategy = st.builds(
    model3::ClassWithIDAttribute,
    id=
        safe_text
)
model3::File_strategy = st.builds(
    model3::File,
    data=
        safe_text,
    name=
        safe_text
)
model3::Image_strategy = st.builds(
    model3::Image,
    height=
        st.integers(),
    data=
        safe_text,
    width=
        st.integers()
)
model3::NodeE_strategy = st.builds(
    model3::NodeE,
    name=
        safe_text
)
model3::NodeC_strategy = st.builds(
    model3::NodeC,
    name=
        safe_text
)
model3::NodeB_strategy = st.builds(
    model3::NodeB,
    name=
        safe_text
)
model3::NodeA_strategy = st.builds(
    model3::NodeA,
    name=
        safe_text
)
model3::PolygonWithDuplicates_strategy = st.builds(
    model3::PolygonWithDuplicates,
    points=
        safe_text
)
model3::Polygon_strategy = st.builds(
    model3::Polygon,
    points=
        safe_text
)
model3::EReference_strategy = st.builds(
    model3::EReference,
)
model3::EClass_strategy = st.builds(
    model3::EClass,
)
model3::EPackage_strategy = st.builds(
    model3::EPackage,
)
model3::MetaRef_strategy = st.builds(
    model3::MetaRef,
)
Class2_strategy = st.builds(
    Class2,
)
model3::Class1_strategy = st.builds(
    model3::Class1,
    additionalValue=
        safe_text
)

@given(instance=model3::Diagram_strategy)
@settings(max_examples=50)
def test_model3::diagram_instantiation(instance):
    assert isinstance(instance, model3::Diagram)

@given(instance=subpackage::model3::Class1_strategy)
@settings(max_examples=50)
def test_subpackage::model3::class1_instantiation(instance):
    assert isinstance(instance, subpackage::model3::Class1)

@given(instance=model3::subpackage::Class2_strategy)
@settings(max_examples=50)
def test_model3::subpackage::class2_instantiation(instance):
    assert isinstance(instance, model3::subpackage::Class2)

@given(instance=model3::NodeD_strategy)
@settings(max_examples=50)
def test_model3::noded_instantiation(instance):
    assert isinstance(instance, model3::NodeD)

@given(instance=model3::NodeD_strategy)
def test_model3::noded_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model3::NodeD_strategy)
def test_model3::noded_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EdgeTarget_strategy)
@settings(max_examples=50)
def test_edgetarget_instantiation(instance):
    assert isinstance(instance, EdgeTarget)

@given(instance=model3::NodeF_strategy)
@settings(max_examples=50)
def test_model3::nodef_instantiation(instance):
    assert isinstance(instance, model3::NodeF)

@given(instance=model3::Edge_strategy)
@settings(max_examples=50)
def test_model3::edge_instantiation(instance):
    assert isinstance(instance, model3::Edge)

@given(instance=model3::EdgeTarget_strategy)
@settings(max_examples=50)
def test_model3::edgetarget_instantiation(instance):
    assert isinstance(instance, model3::EdgeTarget)

@given(instance=model3::ClassWithTransientContainment_strategy)
@settings(max_examples=50)
def test_model3::classwithtransientcontainment_instantiation(instance):
    assert isinstance(instance, model3::ClassWithTransientContainment)

@given(instance=model3::ClassWithTransientContainment_strategy)
def test_model3::classwithtransientcontainment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model3::ClassWithTransientContainment_strategy)
def test_model3::classwithtransientcontainment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model3::ClassWithJavaObjectAttribute_strategy)
@settings(max_examples=50)
def test_model3::classwithjavaobjectattribute_instantiation(instance):
    assert isinstance(instance, model3::ClassWithJavaObjectAttribute)

@given(instance=model3::ClassWithJavaObjectAttribute_strategy)
def test_model3::classwithjavaobjectattribute_javaObject_type(instance):
    assert isinstance(instance.javaObject, str)


@given(instance=model3::ClassWithJavaObjectAttribute_strategy)
def test_model3::classwithjavaobjectattribute_javaObject_setter(instance):
    original = instance.javaObject
    instance.javaObject = original
    assert instance.javaObject == original

@given(instance=model3::ClassWithJavaClassAttribute_strategy)
@settings(max_examples=50)
def test_model3::classwithjavaclassattribute_instantiation(instance):
    assert isinstance(instance, model3::ClassWithJavaClassAttribute)

@given(instance=model3::ClassWithJavaClassAttribute_strategy)
def test_model3::classwithjavaclassattribute_javaClass_type(instance):
    assert isinstance(instance.javaClass, str)


@given(instance=model3::ClassWithJavaClassAttribute_strategy)
def test_model3::classwithjavaclassattribute_javaClass_setter(instance):
    original = instance.javaClass
    instance.javaClass = original
    assert instance.javaClass == original

@given(instance=model3::ClassWithIDAttribute_strategy)
@settings(max_examples=50)
def test_model3::classwithidattribute_instantiation(instance):
    assert isinstance(instance, model3::ClassWithIDAttribute)

@given(instance=model3::ClassWithIDAttribute_strategy)
def test_model3::classwithidattribute_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=model3::ClassWithIDAttribute_strategy)
def test_model3::classwithidattribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model3::File_strategy)
@settings(max_examples=50)
def test_model3::file_instantiation(instance):
    assert isinstance(instance, model3::File)

@given(instance=model3::File_strategy)
def test_model3::file_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=model3::File_strategy)
def test_model3::file_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=model3::File_strategy)
def test_model3::file_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model3::File_strategy)
def test_model3::file_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model3::Image_strategy)
@settings(max_examples=50)
def test_model3::image_instantiation(instance):
    assert isinstance(instance, model3::Image)

@given(instance=model3::Image_strategy)
def test_model3::image_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=model3::Image_strategy)
def test_model3::image_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=model3::Image_strategy)
def test_model3::image_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=model3::Image_strategy)
def test_model3::image_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=model3::Image_strategy)
def test_model3::image_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=model3::Image_strategy)
def test_model3::image_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=model3::NodeE_strategy)
@settings(max_examples=50)
def test_model3::nodee_instantiation(instance):
    assert isinstance(instance, model3::NodeE)

@given(instance=model3::NodeE_strategy)
def test_model3::nodee_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model3::NodeE_strategy)
def test_model3::nodee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model3::NodeC_strategy)
@settings(max_examples=50)
def test_model3::nodec_instantiation(instance):
    assert isinstance(instance, model3::NodeC)

@given(instance=model3::NodeC_strategy)
def test_model3::nodec_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model3::NodeC_strategy)
def test_model3::nodec_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model3::NodeB_strategy)
@settings(max_examples=50)
def test_model3::nodeb_instantiation(instance):
    assert isinstance(instance, model3::NodeB)

@given(instance=model3::NodeB_strategy)
def test_model3::nodeb_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model3::NodeB_strategy)
def test_model3::nodeb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model3::NodeA_strategy)
@settings(max_examples=50)
def test_model3::nodea_instantiation(instance):
    assert isinstance(instance, model3::NodeA)

@given(instance=model3::NodeA_strategy)
def test_model3::nodea_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model3::NodeA_strategy)
def test_model3::nodea_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model3::PolygonWithDuplicates_strategy)
@settings(max_examples=50)
def test_model3::polygonwithduplicates_instantiation(instance):
    assert isinstance(instance, model3::PolygonWithDuplicates)

@given(instance=model3::PolygonWithDuplicates_strategy)
def test_model3::polygonwithduplicates_points_type(instance):
    assert isinstance(instance.points, str)


@given(instance=model3::PolygonWithDuplicates_strategy)
def test_model3::polygonwithduplicates_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=model3::Polygon_strategy)
@settings(max_examples=50)
def test_model3::polygon_instantiation(instance):
    assert isinstance(instance, model3::Polygon)

@given(instance=model3::Polygon_strategy)
def test_model3::polygon_points_type(instance):
    assert isinstance(instance.points, str)


@given(instance=model3::Polygon_strategy)
def test_model3::polygon_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=model3::EReference_strategy)
@settings(max_examples=50)
def test_model3::ereference_instantiation(instance):
    assert isinstance(instance, model3::EReference)

@given(instance=model3::EClass_strategy)
@settings(max_examples=50)
def test_model3::eclass_instantiation(instance):
    assert isinstance(instance, model3::EClass)

@given(instance=model3::EPackage_strategy)
@settings(max_examples=50)
def test_model3::epackage_instantiation(instance):
    assert isinstance(instance, model3::EPackage)

@given(instance=model3::MetaRef_strategy)
@settings(max_examples=50)
def test_model3::metaref_instantiation(instance):
    assert isinstance(instance, model3::MetaRef)

@given(instance=Class2_strategy)
@settings(max_examples=50)
def test_class2_instantiation(instance):
    assert isinstance(instance, Class2)

@given(instance=model3::Class1_strategy)
@settings(max_examples=50)
def test_model3::class1_instantiation(instance):
    assert isinstance(instance, model3::Class1)

@given(instance=model3::Class1_strategy)
def test_model3::class1_additionalValue_type(instance):
    assert isinstance(instance.additionalValue, str)


@given(instance=model3::Class1_strategy)
def test_model3::class1_additionalValue_setter(instance):
    original = instance.additionalValue
    instance.additionalValue = original
    assert instance.additionalValue == original
