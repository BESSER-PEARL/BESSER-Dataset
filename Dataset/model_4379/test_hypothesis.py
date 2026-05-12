import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Feature,
    classmodel_Constant,
    classmodel_Array,
    classmodel_Attribute,
    classmodel_Reference,
    classmodel_Parameter,
    classmodel_Operation,
    classmodel_Multiplicity,
    Relationship,
    classmodel_Aggregation,
    classmodel_Composition,
    classmodel_Dependency,
    classmodel_Generalization,
    classmodel_Realization,
    classmodel_Association,
    classmodel_Annotation,
    classmodel_Feature,
    classmodel_Type,
    Entity,
    classmodel_Enumeration,
    classmodel_Classifier,
    classmodel_Datatype,
    Element,
    classmodel_Relationship,
    classmodel_Entity,
    classmodel_Package,
    classmodel_Element,
    classmodel_Import,
    classmodel_Model,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_classmodel_constant_is_not_abstract():
    assert not inspect.isabstract(classmodel_Constant)


def test_classmodel_constant_constructor_exists():
    assert callable(classmodel_Constant.__init__)


def test_classmodel_constant_constructor_args():
    sig = inspect.signature(classmodel_Constant.__init__)
    params = list(sig.parameters.keys())



def test_classmodel_array_is_not_abstract():
    assert not inspect.isabstract(classmodel_Array)


def test_classmodel_array_constructor_exists():
    assert callable(classmodel_Array.__init__)


def test_classmodel_array_constructor_args():
    sig = inspect.signature(classmodel_Array.__init__)
    params = list(sig.parameters.keys())



def test_classmodel_attribute_is_not_abstract():
    assert not inspect.isabstract(classmodel_Attribute)


def test_classmodel_attribute_constructor_exists():
    assert callable(classmodel_Attribute.__init__)


def test_classmodel_attribute_constructor_args():
    sig = inspect.signature(classmodel_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "implicit" in params, "Missing parameter 'implicit'"

def test_classmodel_attribute_has_static():
    assert hasattr(classmodel_Attribute, "static")
    descriptor = None
    for klass in classmodel_Attribute.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_attribute_has_implicit():
    assert hasattr(classmodel_Attribute, "implicit")
    descriptor = None
    for klass in classmodel_Attribute.__mro__:
        if "implicit" in klass.__dict__:
            descriptor = klass.__dict__["implicit"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_reference_is_not_abstract():
    assert not inspect.isabstract(classmodel_Reference)


def test_classmodel_reference_constructor_exists():
    assert callable(classmodel_Reference.__init__)


def test_classmodel_reference_constructor_args():
    sig = inspect.signature(classmodel_Reference.__init__)
    params = list(sig.parameters.keys())



def test_classmodel_parameter_is_not_abstract():
    assert not inspect.isabstract(classmodel_Parameter)


def test_classmodel_parameter_constructor_exists():
    assert callable(classmodel_Parameter.__init__)


def test_classmodel_parameter_constructor_args():
    sig = inspect.signature(classmodel_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "implicit" in params, "Missing parameter 'implicit'"
    assert "name" in params, "Missing parameter 'name'"

def test_classmodel_parameter_has_implicit():
    assert hasattr(classmodel_Parameter, "implicit")
    descriptor = None
    for klass in classmodel_Parameter.__mro__:
        if "implicit" in klass.__dict__:
            descriptor = klass.__dict__["implicit"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_parameter_has_name():
    assert hasattr(classmodel_Parameter, "name")
    descriptor = None
    for klass in classmodel_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_operation_is_not_abstract():
    assert not inspect.isabstract(classmodel_Operation)


def test_classmodel_operation_constructor_exists():
    assert callable(classmodel_Operation.__init__)


def test_classmodel_operation_constructor_args():
    sig = inspect.signature(classmodel_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "body" in params, "Missing parameter 'body'"

def test_classmodel_operation_has_static():
    assert hasattr(classmodel_Operation, "static")
    descriptor = None
    for klass in classmodel_Operation.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_operation_has_body():
    assert hasattr(classmodel_Operation, "body")
    descriptor = None
    for klass in classmodel_Operation.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_multiplicity_is_not_abstract():
    assert not inspect.isabstract(classmodel_Multiplicity)


def test_classmodel_multiplicity_constructor_exists():
    assert callable(classmodel_Multiplicity.__init__)


def test_classmodel_multiplicity_constructor_args():
    sig = inspect.signature(classmodel_Multiplicity.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_classmodel_multiplicity_has_upper():
    assert hasattr(classmodel_Multiplicity, "upper")
    descriptor = None
    for klass in classmodel_Multiplicity.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_multiplicity_has_lower():
    assert hasattr(classmodel_Multiplicity, "lower")
    descriptor = None
    for klass in classmodel_Multiplicity.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_classmodel_aggregation_is_not_abstract():
    assert not inspect.isabstract(classmodel_Aggregation)


def test_classmodel_aggregation_constructor_exists():
    assert callable(classmodel_Aggregation.__init__)


def test_classmodel_aggregation_constructor_args():
    sig = inspect.signature(classmodel_Aggregation.__init__)
    params = list(sig.parameters.keys())
    assert "headLabel" in params, "Missing parameter 'headLabel'"
    assert "headNavigable" in params, "Missing parameter 'headNavigable'"
    assert "tailLabel" in params, "Missing parameter 'tailLabel'"
    assert "headVisibility" in params, "Missing parameter 'headVisibility'"
    assert "tailVisibility" in params, "Missing parameter 'tailVisibility'"
    assert "tailNavigable" in params, "Missing parameter 'tailNavigable'"

def test_classmodel_aggregation_has_headLabel():
    assert hasattr(classmodel_Aggregation, "headLabel")
    descriptor = None
    for klass in classmodel_Aggregation.__mro__:
        if "headLabel" in klass.__dict__:
            descriptor = klass.__dict__["headLabel"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_aggregation_has_headNavigable():
    assert hasattr(classmodel_Aggregation, "headNavigable")
    descriptor = None
    for klass in classmodel_Aggregation.__mro__:
        if "headNavigable" in klass.__dict__:
            descriptor = klass.__dict__["headNavigable"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_aggregation_has_tailLabel():
    assert hasattr(classmodel_Aggregation, "tailLabel")
    descriptor = None
    for klass in classmodel_Aggregation.__mro__:
        if "tailLabel" in klass.__dict__:
            descriptor = klass.__dict__["tailLabel"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_aggregation_has_headVisibility():
    assert hasattr(classmodel_Aggregation, "headVisibility")
    descriptor = None
    for klass in classmodel_Aggregation.__mro__:
        if "headVisibility" in klass.__dict__:
            descriptor = klass.__dict__["headVisibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_aggregation_has_tailVisibility():
    assert hasattr(classmodel_Aggregation, "tailVisibility")
    descriptor = None
    for klass in classmodel_Aggregation.__mro__:
        if "tailVisibility" in klass.__dict__:
            descriptor = klass.__dict__["tailVisibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_aggregation_has_tailNavigable():
    assert hasattr(classmodel_Aggregation, "tailNavigable")
    descriptor = None
    for klass in classmodel_Aggregation.__mro__:
        if "tailNavigable" in klass.__dict__:
            descriptor = klass.__dict__["tailNavigable"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_composition_is_not_abstract():
    assert not inspect.isabstract(classmodel_Composition)


def test_classmodel_composition_constructor_exists():
    assert callable(classmodel_Composition.__init__)


def test_classmodel_composition_constructor_args():
    sig = inspect.signature(classmodel_Composition.__init__)
    params = list(sig.parameters.keys())
    assert "tailVisibility" in params, "Missing parameter 'tailVisibility'"
    assert "tailLabel" in params, "Missing parameter 'tailLabel'"
    assert "headVisibility" in params, "Missing parameter 'headVisibility'"
    assert "headLabel" in params, "Missing parameter 'headLabel'"
    assert "headNavigable" in params, "Missing parameter 'headNavigable'"
    assert "tailNavigable" in params, "Missing parameter 'tailNavigable'"

def test_classmodel_composition_has_tailVisibility():
    assert hasattr(classmodel_Composition, "tailVisibility")
    descriptor = None
    for klass in classmodel_Composition.__mro__:
        if "tailVisibility" in klass.__dict__:
            descriptor = klass.__dict__["tailVisibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_composition_has_tailLabel():
    assert hasattr(classmodel_Composition, "tailLabel")
    descriptor = None
    for klass in classmodel_Composition.__mro__:
        if "tailLabel" in klass.__dict__:
            descriptor = klass.__dict__["tailLabel"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_composition_has_headVisibility():
    assert hasattr(classmodel_Composition, "headVisibility")
    descriptor = None
    for klass in classmodel_Composition.__mro__:
        if "headVisibility" in klass.__dict__:
            descriptor = klass.__dict__["headVisibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_composition_has_headLabel():
    assert hasattr(classmodel_Composition, "headLabel")
    descriptor = None
    for klass in classmodel_Composition.__mro__:
        if "headLabel" in klass.__dict__:
            descriptor = klass.__dict__["headLabel"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_composition_has_headNavigable():
    assert hasattr(classmodel_Composition, "headNavigable")
    descriptor = None
    for klass in classmodel_Composition.__mro__:
        if "headNavigable" in klass.__dict__:
            descriptor = klass.__dict__["headNavigable"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_composition_has_tailNavigable():
    assert hasattr(classmodel_Composition, "tailNavigable")
    descriptor = None
    for klass in classmodel_Composition.__mro__:
        if "tailNavigable" in klass.__dict__:
            descriptor = klass.__dict__["tailNavigable"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_dependency_is_not_abstract():
    assert not inspect.isabstract(classmodel_Dependency)


def test_classmodel_dependency_constructor_exists():
    assert callable(classmodel_Dependency.__init__)


def test_classmodel_dependency_constructor_args():
    sig = inspect.signature(classmodel_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_classmodel_generalization_is_not_abstract():
    assert not inspect.isabstract(classmodel_Generalization)


def test_classmodel_generalization_constructor_exists():
    assert callable(classmodel_Generalization.__init__)


def test_classmodel_generalization_constructor_args():
    sig = inspect.signature(classmodel_Generalization.__init__)
    params = list(sig.parameters.keys())



def test_classmodel_realization_is_not_abstract():
    assert not inspect.isabstract(classmodel_Realization)


def test_classmodel_realization_constructor_exists():
    assert callable(classmodel_Realization.__init__)


def test_classmodel_realization_constructor_args():
    sig = inspect.signature(classmodel_Realization.__init__)
    params = list(sig.parameters.keys())



def test_classmodel_association_is_not_abstract():
    assert not inspect.isabstract(classmodel_Association)


def test_classmodel_association_constructor_exists():
    assert callable(classmodel_Association.__init__)


def test_classmodel_association_constructor_args():
    sig = inspect.signature(classmodel_Association.__init__)
    params = list(sig.parameters.keys())
    assert "tailNavigable" in params, "Missing parameter 'tailNavigable'"
    assert "headVisibility" in params, "Missing parameter 'headVisibility'"
    assert "headNavigable" in params, "Missing parameter 'headNavigable'"
    assert "tailLabel" in params, "Missing parameter 'tailLabel'"
    assert "tailVisibility" in params, "Missing parameter 'tailVisibility'"
    assert "headLabel" in params, "Missing parameter 'headLabel'"

def test_classmodel_association_has_tailNavigable():
    assert hasattr(classmodel_Association, "tailNavigable")
    descriptor = None
    for klass in classmodel_Association.__mro__:
        if "tailNavigable" in klass.__dict__:
            descriptor = klass.__dict__["tailNavigable"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_association_has_headVisibility():
    assert hasattr(classmodel_Association, "headVisibility")
    descriptor = None
    for klass in classmodel_Association.__mro__:
        if "headVisibility" in klass.__dict__:
            descriptor = klass.__dict__["headVisibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_association_has_headNavigable():
    assert hasattr(classmodel_Association, "headNavigable")
    descriptor = None
    for klass in classmodel_Association.__mro__:
        if "headNavigable" in klass.__dict__:
            descriptor = klass.__dict__["headNavigable"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_association_has_tailLabel():
    assert hasattr(classmodel_Association, "tailLabel")
    descriptor = None
    for klass in classmodel_Association.__mro__:
        if "tailLabel" in klass.__dict__:
            descriptor = klass.__dict__["tailLabel"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_association_has_tailVisibility():
    assert hasattr(classmodel_Association, "tailVisibility")
    descriptor = None
    for klass in classmodel_Association.__mro__:
        if "tailVisibility" in klass.__dict__:
            descriptor = klass.__dict__["tailVisibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_association_has_headLabel():
    assert hasattr(classmodel_Association, "headLabel")
    descriptor = None
    for klass in classmodel_Association.__mro__:
        if "headLabel" in klass.__dict__:
            descriptor = klass.__dict__["headLabel"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_annotation_is_not_abstract():
    assert not inspect.isabstract(classmodel_Annotation)


def test_classmodel_annotation_constructor_exists():
    assert callable(classmodel_Annotation.__init__)


def test_classmodel_annotation_constructor_args():
    sig = inspect.signature(classmodel_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_classmodel_feature_is_not_abstract():
    assert not inspect.isabstract(classmodel_Feature)


def test_classmodel_feature_constructor_exists():
    assert callable(classmodel_Feature.__init__)


def test_classmodel_feature_constructor_args():
    sig = inspect.signature(classmodel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"
    assert "constraint" in params, "Missing parameter 'constraint'"

def test_classmodel_feature_has_value():
    assert hasattr(classmodel_Feature, "value")
    descriptor = None
    for klass in classmodel_Feature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_feature_has_visibility():
    assert hasattr(classmodel_Feature, "visibility")
    descriptor = None
    for klass in classmodel_Feature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_feature_has_name():
    assert hasattr(classmodel_Feature, "name")
    descriptor = None
    for klass in classmodel_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classmodel_feature_has_constraint():
    assert hasattr(classmodel_Feature, "constraint")
    descriptor = None
    for klass in classmodel_Feature.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_type_is_not_abstract():
    assert not inspect.isabstract(classmodel_Type)


def test_classmodel_type_constructor_exists():
    assert callable(classmodel_Type.__init__)


def test_classmodel_type_constructor_args():
    sig = inspect.signature(classmodel_Type.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_classmodel_type_has_visibility():
    assert hasattr(classmodel_Type, "visibility")
    descriptor = None
    for klass in classmodel_Type.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_classmodel_enumeration_is_not_abstract():
    assert not inspect.isabstract(classmodel_Enumeration)


def test_classmodel_enumeration_constructor_exists():
    assert callable(classmodel_Enumeration.__init__)


def test_classmodel_enumeration_constructor_args():
    sig = inspect.signature(classmodel_Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"

def test_classmodel_enumeration_has_constraint():
    assert hasattr(classmodel_Enumeration, "constraint")
    descriptor = None
    for klass in classmodel_Enumeration.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_classifier_is_not_abstract():
    assert not inspect.isabstract(classmodel_Classifier)


def test_classmodel_classifier_constructor_exists():
    assert callable(classmodel_Classifier.__init__)


def test_classmodel_classifier_constructor_args():
    sig = inspect.signature(classmodel_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"

def test_classmodel_classifier_has_constraint():
    assert hasattr(classmodel_Classifier, "constraint")
    descriptor = None
    for klass in classmodel_Classifier.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_datatype_is_not_abstract():
    assert not inspect.isabstract(classmodel_Datatype)


def test_classmodel_datatype_constructor_exists():
    assert callable(classmodel_Datatype.__init__)


def test_classmodel_datatype_constructor_args():
    sig = inspect.signature(classmodel_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_classmodel_relationship_is_not_abstract():
    assert not inspect.isabstract(classmodel_Relationship)


def test_classmodel_relationship_constructor_exists():
    assert callable(classmodel_Relationship.__init__)


def test_classmodel_relationship_constructor_args():
    sig = inspect.signature(classmodel_Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_classmodel_relationship_has_label():
    assert hasattr(classmodel_Relationship, "label")
    descriptor = None
    for klass in classmodel_Relationship.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_entity_is_not_abstract():
    assert not inspect.isabstract(classmodel_Entity)


def test_classmodel_entity_constructor_exists():
    assert callable(classmodel_Entity.__init__)


def test_classmodel_entity_constructor_args():
    sig = inspect.signature(classmodel_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmodel_entity_has_name():
    assert hasattr(classmodel_Entity, "name")
    descriptor = None
    for klass in classmodel_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_package_is_not_abstract():
    assert not inspect.isabstract(classmodel_Package)


def test_classmodel_package_constructor_exists():
    assert callable(classmodel_Package.__init__)


def test_classmodel_package_constructor_args():
    sig = inspect.signature(classmodel_Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmodel_package_has_name():
    assert hasattr(classmodel_Package, "name")
    descriptor = None
    for klass in classmodel_Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_element_is_not_abstract():
    assert not inspect.isabstract(classmodel_Element)


def test_classmodel_element_constructor_exists():
    assert callable(classmodel_Element.__init__)


def test_classmodel_element_constructor_args():
    sig = inspect.signature(classmodel_Element.__init__)
    params = list(sig.parameters.keys())



def test_classmodel_import_is_not_abstract():
    assert not inspect.isabstract(classmodel_Import)


def test_classmodel_import_constructor_exists():
    assert callable(classmodel_Import.__init__)


def test_classmodel_import_constructor_args():
    sig = inspect.signature(classmodel_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_classmodel_import_has_importURI():
    assert hasattr(classmodel_Import, "importURI")
    descriptor = None
    for klass in classmodel_Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_classmodel_model_is_not_abstract():
    assert not inspect.isabstract(classmodel_Model)


def test_classmodel_model_constructor_exists():
    assert callable(classmodel_Model.__init__)


def test_classmodel_model_constructor_args():
    sig = inspect.signature(classmodel_Model.__init__)
    params = list(sig.parameters.keys())

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "PACKAGE_PRIVATE",
        "PUBLIC",
        "PRIVATE",
        "PROTECTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"


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
Feature_strategy = st.builds(
    Feature,
)
classmodel_Constant_strategy = st.builds(
    classmodel_Constant,
)
classmodel_Array_strategy = st.builds(
    classmodel_Array,
)
classmodel_Attribute_strategy = st.builds(
    classmodel_Attribute,
    static=
        st.booleans(),
    implicit=
        safe_text
)
classmodel_Reference_strategy = st.builds(
    classmodel_Reference,
)
classmodel_Parameter_strategy = st.builds(
    classmodel_Parameter,
    implicit=
        safe_text,
    name=
        safe_text
)
classmodel_Operation_strategy = st.builds(
    classmodel_Operation,
    static=
        st.booleans(),
    body=
        safe_text
)
classmodel_Multiplicity_strategy = st.builds(
    classmodel_Multiplicity,
    upper=
        safe_text,
    lower=
        safe_text
)
Relationship_strategy = st.builds(
    Relationship,
)
classmodel_Aggregation_strategy = st.builds(
    classmodel_Aggregation,
    headLabel=
        safe_text,
    headNavigable=
        st.booleans(),
    tailLabel=
        safe_text,
    headVisibility=
        safe_text,
    tailVisibility=
        safe_text,
    tailNavigable=
        st.booleans()
)
classmodel_Composition_strategy = st.builds(
    classmodel_Composition,
    tailVisibility=
        safe_text,
    tailLabel=
        safe_text,
    headVisibility=
        safe_text,
    headLabel=
        safe_text,
    headNavigable=
        st.booleans(),
    tailNavigable=
        st.booleans()
)
classmodel_Dependency_strategy = st.builds(
    classmodel_Dependency,
)
classmodel_Generalization_strategy = st.builds(
    classmodel_Generalization,
)
classmodel_Realization_strategy = st.builds(
    classmodel_Realization,
)
classmodel_Association_strategy = st.builds(
    classmodel_Association,
    tailNavigable=
        st.booleans(),
    headVisibility=
        safe_text,
    headNavigable=
        st.booleans(),
    tailLabel=
        safe_text,
    tailVisibility=
        safe_text,
    headLabel=
        safe_text
)
classmodel_Annotation_strategy = st.builds(
    classmodel_Annotation,
)
classmodel_Feature_strategy = st.builds(
    classmodel_Feature,
    value=
        safe_text,
    visibility=
        safe_text,
    name=
        safe_text,
    constraint=
        safe_text
)
classmodel_Type_strategy = st.builds(
    classmodel_Type,
    visibility=
        safe_text
)
Entity_strategy = st.builds(
    Entity,
)
classmodel_Enumeration_strategy = st.builds(
    classmodel_Enumeration,
    constraint=
        safe_text
)
classmodel_Classifier_strategy = st.builds(
    classmodel_Classifier,
    constraint=
        safe_text
)
classmodel_Datatype_strategy = st.builds(
    classmodel_Datatype,
)
Element_strategy = st.builds(
    Element,
)
classmodel_Relationship_strategy = st.builds(
    classmodel_Relationship,
    label=
        safe_text
)
classmodel_Entity_strategy = st.builds(
    classmodel_Entity,
    name=
        safe_text
)
classmodel_Package_strategy = st.builds(
    classmodel_Package,
    name=
        safe_text
)
classmodel_Element_strategy = st.builds(
    classmodel_Element,
)
classmodel_Import_strategy = st.builds(
    classmodel_Import,
    importURI=
        safe_text
)
classmodel_Model_strategy = st.builds(
    classmodel_Model,
)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=classmodel_Constant_strategy)
@settings(max_examples=50)
def test_classmodel_constant_instantiation(instance):
    assert isinstance(instance, classmodel_Constant)

@given(instance=classmodel_Array_strategy)
@settings(max_examples=50)
def test_classmodel_array_instantiation(instance):
    assert isinstance(instance, classmodel_Array)

@given(instance=classmodel_Attribute_strategy)
@settings(max_examples=50)
def test_classmodel_attribute_instantiation(instance):
    assert isinstance(instance, classmodel_Attribute)



@given(instance=classmodel_Attribute_strategy)
def test_classmodel_attribute_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=classmodel_Attribute_strategy)
def test_classmodel_attribute_implicit_setter(instance):
    original = instance.implicit
    instance.implicit = original
    assert instance.implicit == original

@given(instance=classmodel_Reference_strategy)
@settings(max_examples=50)
def test_classmodel_reference_instantiation(instance):
    assert isinstance(instance, classmodel_Reference)

@given(instance=classmodel_Parameter_strategy)
@settings(max_examples=50)
def test_classmodel_parameter_instantiation(instance):
    assert isinstance(instance, classmodel_Parameter)



@given(instance=classmodel_Parameter_strategy)
def test_classmodel_parameter_implicit_setter(instance):
    original = instance.implicit
    instance.implicit = original
    assert instance.implicit == original



@given(instance=classmodel_Parameter_strategy)
def test_classmodel_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classmodel_Operation_strategy)
@settings(max_examples=50)
def test_classmodel_operation_instantiation(instance):
    assert isinstance(instance, classmodel_Operation)



@given(instance=classmodel_Operation_strategy)
def test_classmodel_operation_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=classmodel_Operation_strategy)
def test_classmodel_operation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=classmodel_Multiplicity_strategy)
@settings(max_examples=50)
def test_classmodel_multiplicity_instantiation(instance):
    assert isinstance(instance, classmodel_Multiplicity)



@given(instance=classmodel_Multiplicity_strategy)
def test_classmodel_multiplicity_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=classmodel_Multiplicity_strategy)
def test_classmodel_multiplicity_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=classmodel_Aggregation_strategy)
@settings(max_examples=50)
def test_classmodel_aggregation_instantiation(instance):
    assert isinstance(instance, classmodel_Aggregation)



@given(instance=classmodel_Aggregation_strategy)
def test_classmodel_aggregation_headLabel_setter(instance):
    original = instance.headLabel
    instance.headLabel = original
    assert instance.headLabel == original



@given(instance=classmodel_Aggregation_strategy)
def test_classmodel_aggregation_headNavigable_setter(instance):
    original = instance.headNavigable
    instance.headNavigable = original
    assert instance.headNavigable == original



@given(instance=classmodel_Aggregation_strategy)
def test_classmodel_aggregation_tailLabel_setter(instance):
    original = instance.tailLabel
    instance.tailLabel = original
    assert instance.tailLabel == original



@given(instance=classmodel_Aggregation_strategy)
def test_classmodel_aggregation_headVisibility_setter(instance):
    original = instance.headVisibility
    instance.headVisibility = original
    assert instance.headVisibility == original



@given(instance=classmodel_Aggregation_strategy)
def test_classmodel_aggregation_tailVisibility_setter(instance):
    original = instance.tailVisibility
    instance.tailVisibility = original
    assert instance.tailVisibility == original



@given(instance=classmodel_Aggregation_strategy)
def test_classmodel_aggregation_tailNavigable_setter(instance):
    original = instance.tailNavigable
    instance.tailNavigable = original
    assert instance.tailNavigable == original

@given(instance=classmodel_Composition_strategy)
@settings(max_examples=50)
def test_classmodel_composition_instantiation(instance):
    assert isinstance(instance, classmodel_Composition)



@given(instance=classmodel_Composition_strategy)
def test_classmodel_composition_tailVisibility_setter(instance):
    original = instance.tailVisibility
    instance.tailVisibility = original
    assert instance.tailVisibility == original



@given(instance=classmodel_Composition_strategy)
def test_classmodel_composition_tailLabel_setter(instance):
    original = instance.tailLabel
    instance.tailLabel = original
    assert instance.tailLabel == original



@given(instance=classmodel_Composition_strategy)
def test_classmodel_composition_headVisibility_setter(instance):
    original = instance.headVisibility
    instance.headVisibility = original
    assert instance.headVisibility == original



@given(instance=classmodel_Composition_strategy)
def test_classmodel_composition_headLabel_setter(instance):
    original = instance.headLabel
    instance.headLabel = original
    assert instance.headLabel == original



@given(instance=classmodel_Composition_strategy)
def test_classmodel_composition_headNavigable_setter(instance):
    original = instance.headNavigable
    instance.headNavigable = original
    assert instance.headNavigable == original



@given(instance=classmodel_Composition_strategy)
def test_classmodel_composition_tailNavigable_setter(instance):
    original = instance.tailNavigable
    instance.tailNavigable = original
    assert instance.tailNavigable == original

@given(instance=classmodel_Dependency_strategy)
@settings(max_examples=50)
def test_classmodel_dependency_instantiation(instance):
    assert isinstance(instance, classmodel_Dependency)

@given(instance=classmodel_Generalization_strategy)
@settings(max_examples=50)
def test_classmodel_generalization_instantiation(instance):
    assert isinstance(instance, classmodel_Generalization)

@given(instance=classmodel_Realization_strategy)
@settings(max_examples=50)
def test_classmodel_realization_instantiation(instance):
    assert isinstance(instance, classmodel_Realization)

@given(instance=classmodel_Association_strategy)
@settings(max_examples=50)
def test_classmodel_association_instantiation(instance):
    assert isinstance(instance, classmodel_Association)



@given(instance=classmodel_Association_strategy)
def test_classmodel_association_tailNavigable_setter(instance):
    original = instance.tailNavigable
    instance.tailNavigable = original
    assert instance.tailNavigable == original



@given(instance=classmodel_Association_strategy)
def test_classmodel_association_headVisibility_setter(instance):
    original = instance.headVisibility
    instance.headVisibility = original
    assert instance.headVisibility == original



@given(instance=classmodel_Association_strategy)
def test_classmodel_association_headNavigable_setter(instance):
    original = instance.headNavigable
    instance.headNavigable = original
    assert instance.headNavigable == original



@given(instance=classmodel_Association_strategy)
def test_classmodel_association_tailLabel_setter(instance):
    original = instance.tailLabel
    instance.tailLabel = original
    assert instance.tailLabel == original



@given(instance=classmodel_Association_strategy)
def test_classmodel_association_tailVisibility_setter(instance):
    original = instance.tailVisibility
    instance.tailVisibility = original
    assert instance.tailVisibility == original



@given(instance=classmodel_Association_strategy)
def test_classmodel_association_headLabel_setter(instance):
    original = instance.headLabel
    instance.headLabel = original
    assert instance.headLabel == original

@given(instance=classmodel_Annotation_strategy)
@settings(max_examples=50)
def test_classmodel_annotation_instantiation(instance):
    assert isinstance(instance, classmodel_Annotation)

@given(instance=classmodel_Feature_strategy)
@settings(max_examples=50)
def test_classmodel_feature_instantiation(instance):
    assert isinstance(instance, classmodel_Feature)



@given(instance=classmodel_Feature_strategy)
def test_classmodel_feature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=classmodel_Feature_strategy)
def test_classmodel_feature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=classmodel_Feature_strategy)
def test_classmodel_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=classmodel_Feature_strategy)
def test_classmodel_feature_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=classmodel_Type_strategy)
@settings(max_examples=50)
def test_classmodel_type_instantiation(instance):
    assert isinstance(instance, classmodel_Type)



@given(instance=classmodel_Type_strategy)
def test_classmodel_type_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=classmodel_Enumeration_strategy)
@settings(max_examples=50)
def test_classmodel_enumeration_instantiation(instance):
    assert isinstance(instance, classmodel_Enumeration)



@given(instance=classmodel_Enumeration_strategy)
def test_classmodel_enumeration_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=classmodel_Classifier_strategy)
@settings(max_examples=50)
def test_classmodel_classifier_instantiation(instance):
    assert isinstance(instance, classmodel_Classifier)



@given(instance=classmodel_Classifier_strategy)
def test_classmodel_classifier_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=classmodel_Datatype_strategy)
@settings(max_examples=50)
def test_classmodel_datatype_instantiation(instance):
    assert isinstance(instance, classmodel_Datatype)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=classmodel_Relationship_strategy)
@settings(max_examples=50)
def test_classmodel_relationship_instantiation(instance):
    assert isinstance(instance, classmodel_Relationship)



@given(instance=classmodel_Relationship_strategy)
def test_classmodel_relationship_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=classmodel_Entity_strategy)
@settings(max_examples=50)
def test_classmodel_entity_instantiation(instance):
    assert isinstance(instance, classmodel_Entity)



@given(instance=classmodel_Entity_strategy)
def test_classmodel_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classmodel_Package_strategy)
@settings(max_examples=50)
def test_classmodel_package_instantiation(instance):
    assert isinstance(instance, classmodel_Package)



@given(instance=classmodel_Package_strategy)
def test_classmodel_package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classmodel_Element_strategy)
@settings(max_examples=50)
def test_classmodel_element_instantiation(instance):
    assert isinstance(instance, classmodel_Element)

@given(instance=classmodel_Import_strategy)
@settings(max_examples=50)
def test_classmodel_import_instantiation(instance):
    assert isinstance(instance, classmodel_Import)



@given(instance=classmodel_Import_strategy)
def test_classmodel_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=classmodel_Model_strategy)
@settings(max_examples=50)
def test_classmodel_model_instantiation(instance):
    assert isinstance(instance, classmodel_Model)
