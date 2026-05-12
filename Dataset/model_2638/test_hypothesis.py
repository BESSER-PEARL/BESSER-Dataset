import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model3_Diagram,
    subpackage_model3_Class1,
    model3_subpackage_Class2,
    model3_NodeD,
    EdgeTarget,
    model3_NodeF,
    model3_Edge,
    model3_EdgeTarget,
    model3_ClassWithTransientContainment,
    model3_ClassWithJavaObjectAttribute,
    model3_ClassWithJavaClassAttribute,
    model3_ClassWithIDAttribute,
    model3_File,
    model3_Image,
    model3_NodeE,
    model3_NodeC,
    model3_NodeB,
    model3_NodeA,
    model3_PolygonWithDuplicates,
    model3_Polygon,
    model3_EReference,
    model3_EClass,
    model3_EPackage,
    model3_MetaRef,
    Class2,
    model3_Class1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model3_diagram_is_not_abstract():
    assert not inspect.isabstract(model3_Diagram)


def test_model3_diagram_constructor_exists():
    assert callable(model3_Diagram.__init__)


def test_model3_diagram_constructor_args():
    sig = inspect.signature(model3_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_subpackage_model3_class1_is_not_abstract():
    assert not inspect.isabstract(subpackage_model3_Class1)


def test_subpackage_model3_class1_constructor_exists():
    assert callable(subpackage_model3_Class1.__init__)


def test_subpackage_model3_class1_constructor_args():
    sig = inspect.signature(subpackage_model3_Class1.__init__)
    params = list(sig.parameters.keys())



def test_model3_subpackage_class2_is_not_abstract():
    assert not inspect.isabstract(model3_subpackage_Class2)


def test_model3_subpackage_class2_constructor_exists():
    assert callable(model3_subpackage_Class2.__init__)


def test_model3_subpackage_class2_constructor_args():
    sig = inspect.signature(model3_subpackage_Class2.__init__)
    params = list(sig.parameters.keys())



def test_model3_noded_is_not_abstract():
    assert not inspect.isabstract(model3_NodeD)


def test_model3_noded_constructor_exists():
    assert callable(model3_NodeD.__init__)


def test_model3_noded_constructor_args():
    sig = inspect.signature(model3_NodeD.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model3_noded_has_name():
    assert hasattr(model3_NodeD, "name")
    descriptor = None
    for klass in model3_NodeD.__mro__:
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



def test_model3_nodef_is_not_abstract():
    assert not inspect.isabstract(model3_NodeF)


def test_model3_nodef_constructor_exists():
    assert callable(model3_NodeF.__init__)


def test_model3_nodef_constructor_args():
    sig = inspect.signature(model3_NodeF.__init__)
    params = list(sig.parameters.keys())



def test_model3_edge_is_not_abstract():
    assert not inspect.isabstract(model3_Edge)


def test_model3_edge_constructor_exists():
    assert callable(model3_Edge.__init__)


def test_model3_edge_constructor_args():
    sig = inspect.signature(model3_Edge.__init__)
    params = list(sig.parameters.keys())



def test_model3_edgetarget_is_not_abstract():
    assert not inspect.isabstract(model3_EdgeTarget)


def test_model3_edgetarget_constructor_exists():
    assert callable(model3_EdgeTarget.__init__)


def test_model3_edgetarget_constructor_args():
    sig = inspect.signature(model3_EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_model3_classwithtransientcontainment_is_not_abstract():
    assert not inspect.isabstract(model3_ClassWithTransientContainment)


def test_model3_classwithtransientcontainment_constructor_exists():
    assert callable(model3_ClassWithTransientContainment.__init__)


def test_model3_classwithtransientcontainment_constructor_args():
    sig = inspect.signature(model3_ClassWithTransientContainment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model3_classwithtransientcontainment_has_name():
    assert hasattr(model3_ClassWithTransientContainment, "name")
    descriptor = None
    for klass in model3_ClassWithTransientContainment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model3_classwithjavaobjectattribute_is_not_abstract():
    assert not inspect.isabstract(model3_ClassWithJavaObjectAttribute)


def test_model3_classwithjavaobjectattribute_constructor_exists():
    assert callable(model3_ClassWithJavaObjectAttribute.__init__)


def test_model3_classwithjavaobjectattribute_constructor_args():
    sig = inspect.signature(model3_ClassWithJavaObjectAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "javaObject" in params, "Missing parameter 'javaObject'"

def test_model3_classwithjavaobjectattribute_has_javaObject():
    assert hasattr(model3_ClassWithJavaObjectAttribute, "javaObject")
    descriptor = None
    for klass in model3_ClassWithJavaObjectAttribute.__mro__:
        if "javaObject" in klass.__dict__:
            descriptor = klass.__dict__["javaObject"]
            break
    assert isinstance(descriptor, property)



def test_model3_classwithjavaclassattribute_is_not_abstract():
    assert not inspect.isabstract(model3_ClassWithJavaClassAttribute)


def test_model3_classwithjavaclassattribute_constructor_exists():
    assert callable(model3_ClassWithJavaClassAttribute.__init__)


def test_model3_classwithjavaclassattribute_constructor_args():
    sig = inspect.signature(model3_ClassWithJavaClassAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "javaClass" in params, "Missing parameter 'javaClass'"

def test_model3_classwithjavaclassattribute_has_javaClass():
    assert hasattr(model3_ClassWithJavaClassAttribute, "javaClass")
    descriptor = None
    for klass in model3_ClassWithJavaClassAttribute.__mro__:
        if "javaClass" in klass.__dict__:
            descriptor = klass.__dict__["javaClass"]
            break
    assert isinstance(descriptor, property)



def test_model3_classwithidattribute_is_not_abstract():
    assert not inspect.isabstract(model3_ClassWithIDAttribute)


def test_model3_classwithidattribute_constructor_exists():
    assert callable(model3_ClassWithIDAttribute.__init__)


def test_model3_classwithidattribute_constructor_args():
    sig = inspect.signature(model3_ClassWithIDAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_model3_classwithidattribute_has_id():
    assert hasattr(model3_ClassWithIDAttribute, "id")
    descriptor = None
    for klass in model3_ClassWithIDAttribute.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_model3_file_is_not_abstract():
    assert not inspect.isabstract(model3_File)


def test_model3_file_constructor_exists():
    assert callable(model3_File.__init__)


def test_model3_file_constructor_args():
    sig = inspect.signature(model3_File.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "name" in params, "Missing parameter 'name'"

def test_model3_file_has_data():
    assert hasattr(model3_File, "data")
    descriptor = None
    for klass in model3_File.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_model3_file_has_name():
    assert hasattr(model3_File, "name")
    descriptor = None
    for klass in model3_File.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model3_image_is_not_abstract():
    assert not inspect.isabstract(model3_Image)


def test_model3_image_constructor_exists():
    assert callable(model3_Image.__init__)


def test_model3_image_constructor_args():
    sig = inspect.signature(model3_Image.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_model3_image_has_data():
    assert hasattr(model3_Image, "data")
    descriptor = None
    for klass in model3_Image.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_model3_image_has_width():
    assert hasattr(model3_Image, "width")
    descriptor = None
    for klass in model3_Image.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_model3_image_has_height():
    assert hasattr(model3_Image, "height")
    descriptor = None
    for klass in model3_Image.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_model3_nodee_is_not_abstract():
    assert not inspect.isabstract(model3_NodeE)


def test_model3_nodee_constructor_exists():
    assert callable(model3_NodeE.__init__)


def test_model3_nodee_constructor_args():
    sig = inspect.signature(model3_NodeE.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model3_nodee_has_name():
    assert hasattr(model3_NodeE, "name")
    descriptor = None
    for klass in model3_NodeE.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model3_nodec_is_not_abstract():
    assert not inspect.isabstract(model3_NodeC)


def test_model3_nodec_constructor_exists():
    assert callable(model3_NodeC.__init__)


def test_model3_nodec_constructor_args():
    sig = inspect.signature(model3_NodeC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model3_nodec_has_name():
    assert hasattr(model3_NodeC, "name")
    descriptor = None
    for klass in model3_NodeC.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model3_nodeb_is_not_abstract():
    assert not inspect.isabstract(model3_NodeB)


def test_model3_nodeb_constructor_exists():
    assert callable(model3_NodeB.__init__)


def test_model3_nodeb_constructor_args():
    sig = inspect.signature(model3_NodeB.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model3_nodeb_has_name():
    assert hasattr(model3_NodeB, "name")
    descriptor = None
    for klass in model3_NodeB.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model3_nodea_is_not_abstract():
    assert not inspect.isabstract(model3_NodeA)


def test_model3_nodea_constructor_exists():
    assert callable(model3_NodeA.__init__)


def test_model3_nodea_constructor_args():
    sig = inspect.signature(model3_NodeA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model3_nodea_has_name():
    assert hasattr(model3_NodeA, "name")
    descriptor = None
    for klass in model3_NodeA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model3_polygonwithduplicates_is_not_abstract():
    assert not inspect.isabstract(model3_PolygonWithDuplicates)


def test_model3_polygonwithduplicates_constructor_exists():
    assert callable(model3_PolygonWithDuplicates.__init__)


def test_model3_polygonwithduplicates_constructor_args():
    sig = inspect.signature(model3_PolygonWithDuplicates.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"

def test_model3_polygonwithduplicates_has_points():
    assert hasattr(model3_PolygonWithDuplicates, "points")
    descriptor = None
    for klass in model3_PolygonWithDuplicates.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)



def test_model3_polygon_is_not_abstract():
    assert not inspect.isabstract(model3_Polygon)


def test_model3_polygon_constructor_exists():
    assert callable(model3_Polygon.__init__)


def test_model3_polygon_constructor_args():
    sig = inspect.signature(model3_Polygon.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"

def test_model3_polygon_has_points():
    assert hasattr(model3_Polygon, "points")
    descriptor = None
    for klass in model3_Polygon.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)



def test_model3_ereference_is_not_abstract():
    assert not inspect.isabstract(model3_EReference)


def test_model3_ereference_constructor_exists():
    assert callable(model3_EReference.__init__)


def test_model3_ereference_constructor_args():
    sig = inspect.signature(model3_EReference.__init__)
    params = list(sig.parameters.keys())



def test_model3_eclass_is_not_abstract():
    assert not inspect.isabstract(model3_EClass)


def test_model3_eclass_constructor_exists():
    assert callable(model3_EClass.__init__)


def test_model3_eclass_constructor_args():
    sig = inspect.signature(model3_EClass.__init__)
    params = list(sig.parameters.keys())



def test_model3_epackage_is_not_abstract():
    assert not inspect.isabstract(model3_EPackage)


def test_model3_epackage_constructor_exists():
    assert callable(model3_EPackage.__init__)


def test_model3_epackage_constructor_args():
    sig = inspect.signature(model3_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_model3_metaref_is_not_abstract():
    assert not inspect.isabstract(model3_MetaRef)


def test_model3_metaref_constructor_exists():
    assert callable(model3_MetaRef.__init__)


def test_model3_metaref_constructor_args():
    sig = inspect.signature(model3_MetaRef.__init__)
    params = list(sig.parameters.keys())



def test_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_model3_class1_is_not_abstract():
    assert not inspect.isabstract(model3_Class1)


def test_model3_class1_constructor_exists():
    assert callable(model3_Class1.__init__)


def test_model3_class1_constructor_args():
    sig = inspect.signature(model3_Class1.__init__)
    params = list(sig.parameters.keys())
    assert "additionalValue" in params, "Missing parameter 'additionalValue'"

def test_model3_class1_has_additionalValue():
    assert hasattr(model3_Class1, "additionalValue")
    descriptor = None
    for klass in model3_Class1.__mro__:
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
model3_Diagram_strategy = st.builds(
    model3_Diagram,
)
subpackage_model3_Class1_strategy = st.builds(
    subpackage_model3_Class1,
)
model3_subpackage_Class2_strategy = st.builds(
    model3_subpackage_Class2,
)
model3_NodeD_strategy = st.builds(
    model3_NodeD,
    name=
        safe_text
)
EdgeTarget_strategy = st.builds(
    EdgeTarget,
)
model3_NodeF_strategy = st.builds(
    model3_NodeF,
)
model3_Edge_strategy = st.builds(
    model3_Edge,
)
model3_EdgeTarget_strategy = st.builds(
    model3_EdgeTarget,
)
model3_ClassWithTransientContainment_strategy = st.builds(
    model3_ClassWithTransientContainment,
    name=
        safe_text
)
model3_ClassWithJavaObjectAttribute_strategy = st.builds(
    model3_ClassWithJavaObjectAttribute,
    javaObject=
        safe_text
)
model3_ClassWithJavaClassAttribute_strategy = st.builds(
    model3_ClassWithJavaClassAttribute,
    javaClass=
        safe_text
)
model3_ClassWithIDAttribute_strategy = st.builds(
    model3_ClassWithIDAttribute,
    id=
        safe_text
)
model3_File_strategy = st.builds(
    model3_File,
    data=
        safe_text,
    name=
        safe_text
)
model3_Image_strategy = st.builds(
    model3_Image,
    data=
        safe_text,
    width=
        st.integers(),
    height=
        st.integers()
)
model3_NodeE_strategy = st.builds(
    model3_NodeE,
    name=
        safe_text
)
model3_NodeC_strategy = st.builds(
    model3_NodeC,
    name=
        safe_text
)
model3_NodeB_strategy = st.builds(
    model3_NodeB,
    name=
        safe_text
)
model3_NodeA_strategy = st.builds(
    model3_NodeA,
    name=
        safe_text
)
model3_PolygonWithDuplicates_strategy = st.builds(
    model3_PolygonWithDuplicates,
    points=
        safe_text
)
model3_Polygon_strategy = st.builds(
    model3_Polygon,
    points=
        safe_text
)
model3_EReference_strategy = st.builds(
    model3_EReference,
)
model3_EClass_strategy = st.builds(
    model3_EClass,
)
model3_EPackage_strategy = st.builds(
    model3_EPackage,
)
model3_MetaRef_strategy = st.builds(
    model3_MetaRef,
)
Class2_strategy = st.builds(
    Class2,
)
model3_Class1_strategy = st.builds(
    model3_Class1,
    additionalValue=
        safe_text
)

@given(instance=model3_Diagram_strategy)
@settings(max_examples=50)
def test_model3_diagram_instantiation(instance):
    assert isinstance(instance, model3_Diagram)

@given(instance=subpackage_model3_Class1_strategy)
@settings(max_examples=50)
def test_subpackage_model3_class1_instantiation(instance):
    assert isinstance(instance, subpackage_model3_Class1)

@given(instance=model3_subpackage_Class2_strategy)
@settings(max_examples=50)
def test_model3_subpackage_class2_instantiation(instance):
    assert isinstance(instance, model3_subpackage_Class2)

@given(instance=model3_NodeD_strategy)
@settings(max_examples=50)
def test_model3_noded_instantiation(instance):
    assert isinstance(instance, model3_NodeD)



@given(instance=model3_NodeD_strategy)
def test_model3_noded_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EdgeTarget_strategy)
@settings(max_examples=50)
def test_edgetarget_instantiation(instance):
    assert isinstance(instance, EdgeTarget)

@given(instance=model3_NodeF_strategy)
@settings(max_examples=50)
def test_model3_nodef_instantiation(instance):
    assert isinstance(instance, model3_NodeF)

@given(instance=model3_Edge_strategy)
@settings(max_examples=50)
def test_model3_edge_instantiation(instance):
    assert isinstance(instance, model3_Edge)

@given(instance=model3_EdgeTarget_strategy)
@settings(max_examples=50)
def test_model3_edgetarget_instantiation(instance):
    assert isinstance(instance, model3_EdgeTarget)

@given(instance=model3_ClassWithTransientContainment_strategy)
@settings(max_examples=50)
def test_model3_classwithtransientcontainment_instantiation(instance):
    assert isinstance(instance, model3_ClassWithTransientContainment)



@given(instance=model3_ClassWithTransientContainment_strategy)
def test_model3_classwithtransientcontainment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model3_ClassWithJavaObjectAttribute_strategy)
@settings(max_examples=50)
def test_model3_classwithjavaobjectattribute_instantiation(instance):
    assert isinstance(instance, model3_ClassWithJavaObjectAttribute)



@given(instance=model3_ClassWithJavaObjectAttribute_strategy)
def test_model3_classwithjavaobjectattribute_javaObject_setter(instance):
    original = instance.javaObject
    instance.javaObject = original
    assert instance.javaObject == original

@given(instance=model3_ClassWithJavaClassAttribute_strategy)
@settings(max_examples=50)
def test_model3_classwithjavaclassattribute_instantiation(instance):
    assert isinstance(instance, model3_ClassWithJavaClassAttribute)



@given(instance=model3_ClassWithJavaClassAttribute_strategy)
def test_model3_classwithjavaclassattribute_javaClass_setter(instance):
    original = instance.javaClass
    instance.javaClass = original
    assert instance.javaClass == original

@given(instance=model3_ClassWithIDAttribute_strategy)
@settings(max_examples=50)
def test_model3_classwithidattribute_instantiation(instance):
    assert isinstance(instance, model3_ClassWithIDAttribute)



@given(instance=model3_ClassWithIDAttribute_strategy)
def test_model3_classwithidattribute_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=model3_File_strategy)
@settings(max_examples=50)
def test_model3_file_instantiation(instance):
    assert isinstance(instance, model3_File)



@given(instance=model3_File_strategy)
def test_model3_file_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=model3_File_strategy)
def test_model3_file_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model3_Image_strategy)
@settings(max_examples=50)
def test_model3_image_instantiation(instance):
    assert isinstance(instance, model3_Image)



@given(instance=model3_Image_strategy)
def test_model3_image_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=model3_Image_strategy)
def test_model3_image_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=model3_Image_strategy)
def test_model3_image_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=model3_NodeE_strategy)
@settings(max_examples=50)
def test_model3_nodee_instantiation(instance):
    assert isinstance(instance, model3_NodeE)



@given(instance=model3_NodeE_strategy)
def test_model3_nodee_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model3_NodeC_strategy)
@settings(max_examples=50)
def test_model3_nodec_instantiation(instance):
    assert isinstance(instance, model3_NodeC)



@given(instance=model3_NodeC_strategy)
def test_model3_nodec_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model3_NodeB_strategy)
@settings(max_examples=50)
def test_model3_nodeb_instantiation(instance):
    assert isinstance(instance, model3_NodeB)



@given(instance=model3_NodeB_strategy)
def test_model3_nodeb_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model3_NodeA_strategy)
@settings(max_examples=50)
def test_model3_nodea_instantiation(instance):
    assert isinstance(instance, model3_NodeA)



@given(instance=model3_NodeA_strategy)
def test_model3_nodea_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model3_PolygonWithDuplicates_strategy)
@settings(max_examples=50)
def test_model3_polygonwithduplicates_instantiation(instance):
    assert isinstance(instance, model3_PolygonWithDuplicates)



@given(instance=model3_PolygonWithDuplicates_strategy)
def test_model3_polygonwithduplicates_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=model3_Polygon_strategy)
@settings(max_examples=50)
def test_model3_polygon_instantiation(instance):
    assert isinstance(instance, model3_Polygon)



@given(instance=model3_Polygon_strategy)
def test_model3_polygon_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=model3_EReference_strategy)
@settings(max_examples=50)
def test_model3_ereference_instantiation(instance):
    assert isinstance(instance, model3_EReference)

@given(instance=model3_EClass_strategy)
@settings(max_examples=50)
def test_model3_eclass_instantiation(instance):
    assert isinstance(instance, model3_EClass)

@given(instance=model3_EPackage_strategy)
@settings(max_examples=50)
def test_model3_epackage_instantiation(instance):
    assert isinstance(instance, model3_EPackage)

@given(instance=model3_MetaRef_strategy)
@settings(max_examples=50)
def test_model3_metaref_instantiation(instance):
    assert isinstance(instance, model3_MetaRef)

@given(instance=Class2_strategy)
@settings(max_examples=50)
def test_class2_instantiation(instance):
    assert isinstance(instance, Class2)

@given(instance=model3_Class1_strategy)
@settings(max_examples=50)
def test_model3_class1_instantiation(instance):
    assert isinstance(instance, model3_Class1)



@given(instance=model3_Class1_strategy)
def test_model3_class1_additionalValue_setter(instance):
    original = instance.additionalValue
    instance.additionalValue = original
    assert instance.additionalValue == original
