import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Feature,
    classmodel::Constant,
    classmodel::Array,
    classmodel::Attribute,
    classmodel::Reference,
    classmodel::Parameter,
    classmodel::Operation,
    classmodel::Multiplicity,
    Relationship,
    classmodel::Dependency,
    classmodel::Generalization,
    classmodel::Realization,
    classmodel::Composition,
    classmodel::Aggregation,
    classmodel::Association,
    classmodel::Annotation,
    classmodel::Feature,
    classmodel::Type,
    Entity,
    classmodel::Classifier,
    classmodel::Enumeration,
    classmodel::Datatype,
    Element,
    classmodel::Relationship,
    classmodel::Entity,
    classmodel::Package,
    classmodel::Element,
    classmodel::Import,
    classmodel::Model,
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



def test_classmodel::constant_is_not_abstract():
    assert not inspect.isabstract(classmodel::Constant)


def test_classmodel::constant_constructor_exists():
    assert callable(classmodel::Constant.__init__)


def test_classmodel::constant_constructor_args():
    sig = inspect.signature(classmodel::Constant.__init__)
    params = list(sig.parameters.keys())



def test_classmodel::array_is_not_abstract():
    assert not inspect.isabstract(classmodel::Array)


def test_classmodel::array_constructor_exists():
    assert callable(classmodel::Array.__init__)


def test_classmodel::array_constructor_args():
    sig = inspect.signature(classmodel::Array.__init__)
    params = list(sig.parameters.keys())



def test_classmodel::attribute_is_not_abstract():
    assert not inspect.isabstract(classmodel::Attribute)


def test_classmodel::attribute_constructor_exists():
    assert callable(classmodel::Attribute.__init__)


def test_classmodel::attribute_constructor_args():
    sig = inspect.signature(classmodel::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "implicit" in params, "Missing parameter 'implicit'"

def test_classmodel::attribute_has_static():
    assert hasattr(classmodel::Attribute, "static")
    descriptor = None
    for klass in classmodel::Attribute.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::attribute_has_implicit():
    assert hasattr(classmodel::Attribute, "implicit")
    descriptor = None
    for klass in classmodel::Attribute.__mro__:
        if "implicit" in klass.__dict__:
            descriptor = klass.__dict__["implicit"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::reference_is_not_abstract():
    assert not inspect.isabstract(classmodel::Reference)


def test_classmodel::reference_constructor_exists():
    assert callable(classmodel::Reference.__init__)


def test_classmodel::reference_constructor_args():
    sig = inspect.signature(classmodel::Reference.__init__)
    params = list(sig.parameters.keys())



def test_classmodel::parameter_is_not_abstract():
    assert not inspect.isabstract(classmodel::Parameter)


def test_classmodel::parameter_constructor_exists():
    assert callable(classmodel::Parameter.__init__)


def test_classmodel::parameter_constructor_args():
    sig = inspect.signature(classmodel::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "implicit" in params, "Missing parameter 'implicit'"
    assert "name" in params, "Missing parameter 'name'"

def test_classmodel::parameter_has_implicit():
    assert hasattr(classmodel::Parameter, "implicit")
    descriptor = None
    for klass in classmodel::Parameter.__mro__:
        if "implicit" in klass.__dict__:
            descriptor = klass.__dict__["implicit"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::parameter_has_name():
    assert hasattr(classmodel::Parameter, "name")
    descriptor = None
    for klass in classmodel::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::operation_is_not_abstract():
    assert not inspect.isabstract(classmodel::Operation)


def test_classmodel::operation_constructor_exists():
    assert callable(classmodel::Operation.__init__)


def test_classmodel::operation_constructor_args():
    sig = inspect.signature(classmodel::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "static" in params, "Missing parameter 'static'"

def test_classmodel::operation_has_body():
    assert hasattr(classmodel::Operation, "body")
    descriptor = None
    for klass in classmodel::Operation.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::operation_has_static():
    assert hasattr(classmodel::Operation, "static")
    descriptor = None
    for klass in classmodel::Operation.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::multiplicity_is_not_abstract():
    assert not inspect.isabstract(classmodel::Multiplicity)


def test_classmodel::multiplicity_constructor_exists():
    assert callable(classmodel::Multiplicity.__init__)


def test_classmodel::multiplicity_constructor_args():
    sig = inspect.signature(classmodel::Multiplicity.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_classmodel::multiplicity_has_lower():
    assert hasattr(classmodel::Multiplicity, "lower")
    descriptor = None
    for klass in classmodel::Multiplicity.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::multiplicity_has_upper():
    assert hasattr(classmodel::Multiplicity, "upper")
    descriptor = None
    for klass in classmodel::Multiplicity.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_classmodel::dependency_is_not_abstract():
    assert not inspect.isabstract(classmodel::Dependency)


def test_classmodel::dependency_constructor_exists():
    assert callable(classmodel::Dependency.__init__)


def test_classmodel::dependency_constructor_args():
    sig = inspect.signature(classmodel::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_classmodel::generalization_is_not_abstract():
    assert not inspect.isabstract(classmodel::Generalization)


def test_classmodel::generalization_constructor_exists():
    assert callable(classmodel::Generalization.__init__)


def test_classmodel::generalization_constructor_args():
    sig = inspect.signature(classmodel::Generalization.__init__)
    params = list(sig.parameters.keys())



def test_classmodel::realization_is_not_abstract():
    assert not inspect.isabstract(classmodel::Realization)


def test_classmodel::realization_constructor_exists():
    assert callable(classmodel::Realization.__init__)


def test_classmodel::realization_constructor_args():
    sig = inspect.signature(classmodel::Realization.__init__)
    params = list(sig.parameters.keys())



def test_classmodel::composition_is_not_abstract():
    assert not inspect.isabstract(classmodel::Composition)


def test_classmodel::composition_constructor_exists():
    assert callable(classmodel::Composition.__init__)


def test_classmodel::composition_constructor_args():
    sig = inspect.signature(classmodel::Composition.__init__)
    params = list(sig.parameters.keys())
    assert "headLabel" in params, "Missing parameter 'headLabel'"
    assert "headNavigable" in params, "Missing parameter 'headNavigable'"
    assert "tailVisibility" in params, "Missing parameter 'tailVisibility'"
    assert "tailNavigable" in params, "Missing parameter 'tailNavigable'"
    assert "headVisibility" in params, "Missing parameter 'headVisibility'"
    assert "tailLabel" in params, "Missing parameter 'tailLabel'"

def test_classmodel::composition_has_headLabel():
    assert hasattr(classmodel::Composition, "headLabel")
    descriptor = None
    for klass in classmodel::Composition.__mro__:
        if "headLabel" in klass.__dict__:
            descriptor = klass.__dict__["headLabel"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::composition_has_headNavigable():
    assert hasattr(classmodel::Composition, "headNavigable")
    descriptor = None
    for klass in classmodel::Composition.__mro__:
        if "headNavigable" in klass.__dict__:
            descriptor = klass.__dict__["headNavigable"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::composition_has_tailVisibility():
    assert hasattr(classmodel::Composition, "tailVisibility")
    descriptor = None
    for klass in classmodel::Composition.__mro__:
        if "tailVisibility" in klass.__dict__:
            descriptor = klass.__dict__["tailVisibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::composition_has_tailNavigable():
    assert hasattr(classmodel::Composition, "tailNavigable")
    descriptor = None
    for klass in classmodel::Composition.__mro__:
        if "tailNavigable" in klass.__dict__:
            descriptor = klass.__dict__["tailNavigable"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::composition_has_headVisibility():
    assert hasattr(classmodel::Composition, "headVisibility")
    descriptor = None
    for klass in classmodel::Composition.__mro__:
        if "headVisibility" in klass.__dict__:
            descriptor = klass.__dict__["headVisibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::composition_has_tailLabel():
    assert hasattr(classmodel::Composition, "tailLabel")
    descriptor = None
    for klass in classmodel::Composition.__mro__:
        if "tailLabel" in klass.__dict__:
            descriptor = klass.__dict__["tailLabel"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::aggregation_is_not_abstract():
    assert not inspect.isabstract(classmodel::Aggregation)


def test_classmodel::aggregation_constructor_exists():
    assert callable(classmodel::Aggregation.__init__)


def test_classmodel::aggregation_constructor_args():
    sig = inspect.signature(classmodel::Aggregation.__init__)
    params = list(sig.parameters.keys())
    assert "tailVisibility" in params, "Missing parameter 'tailVisibility'"
    assert "tailLabel" in params, "Missing parameter 'tailLabel'"
    assert "headVisibility" in params, "Missing parameter 'headVisibility'"
    assert "headNavigable" in params, "Missing parameter 'headNavigable'"
    assert "tailNavigable" in params, "Missing parameter 'tailNavigable'"
    assert "headLabel" in params, "Missing parameter 'headLabel'"

def test_classmodel::aggregation_has_tailVisibility():
    assert hasattr(classmodel::Aggregation, "tailVisibility")
    descriptor = None
    for klass in classmodel::Aggregation.__mro__:
        if "tailVisibility" in klass.__dict__:
            descriptor = klass.__dict__["tailVisibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::aggregation_has_tailLabel():
    assert hasattr(classmodel::Aggregation, "tailLabel")
    descriptor = None
    for klass in classmodel::Aggregation.__mro__:
        if "tailLabel" in klass.__dict__:
            descriptor = klass.__dict__["tailLabel"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::aggregation_has_headVisibility():
    assert hasattr(classmodel::Aggregation, "headVisibility")
    descriptor = None
    for klass in classmodel::Aggregation.__mro__:
        if "headVisibility" in klass.__dict__:
            descriptor = klass.__dict__["headVisibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::aggregation_has_headNavigable():
    assert hasattr(classmodel::Aggregation, "headNavigable")
    descriptor = None
    for klass in classmodel::Aggregation.__mro__:
        if "headNavigable" in klass.__dict__:
            descriptor = klass.__dict__["headNavigable"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::aggregation_has_tailNavigable():
    assert hasattr(classmodel::Aggregation, "tailNavigable")
    descriptor = None
    for klass in classmodel::Aggregation.__mro__:
        if "tailNavigable" in klass.__dict__:
            descriptor = klass.__dict__["tailNavigable"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::aggregation_has_headLabel():
    assert hasattr(classmodel::Aggregation, "headLabel")
    descriptor = None
    for klass in classmodel::Aggregation.__mro__:
        if "headLabel" in klass.__dict__:
            descriptor = klass.__dict__["headLabel"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::association_is_not_abstract():
    assert not inspect.isabstract(classmodel::Association)


def test_classmodel::association_constructor_exists():
    assert callable(classmodel::Association.__init__)


def test_classmodel::association_constructor_args():
    sig = inspect.signature(classmodel::Association.__init__)
    params = list(sig.parameters.keys())
    assert "headLabel" in params, "Missing parameter 'headLabel'"
    assert "tailVisibility" in params, "Missing parameter 'tailVisibility'"
    assert "tailNavigable" in params, "Missing parameter 'tailNavigable'"
    assert "headVisibility" in params, "Missing parameter 'headVisibility'"
    assert "headNavigable" in params, "Missing parameter 'headNavigable'"
    assert "tailLabel" in params, "Missing parameter 'tailLabel'"

def test_classmodel::association_has_headLabel():
    assert hasattr(classmodel::Association, "headLabel")
    descriptor = None
    for klass in classmodel::Association.__mro__:
        if "headLabel" in klass.__dict__:
            descriptor = klass.__dict__["headLabel"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::association_has_tailVisibility():
    assert hasattr(classmodel::Association, "tailVisibility")
    descriptor = None
    for klass in classmodel::Association.__mro__:
        if "tailVisibility" in klass.__dict__:
            descriptor = klass.__dict__["tailVisibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::association_has_tailNavigable():
    assert hasattr(classmodel::Association, "tailNavigable")
    descriptor = None
    for klass in classmodel::Association.__mro__:
        if "tailNavigable" in klass.__dict__:
            descriptor = klass.__dict__["tailNavigable"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::association_has_headVisibility():
    assert hasattr(classmodel::Association, "headVisibility")
    descriptor = None
    for klass in classmodel::Association.__mro__:
        if "headVisibility" in klass.__dict__:
            descriptor = klass.__dict__["headVisibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::association_has_headNavigable():
    assert hasattr(classmodel::Association, "headNavigable")
    descriptor = None
    for klass in classmodel::Association.__mro__:
        if "headNavigable" in klass.__dict__:
            descriptor = klass.__dict__["headNavigable"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::association_has_tailLabel():
    assert hasattr(classmodel::Association, "tailLabel")
    descriptor = None
    for klass in classmodel::Association.__mro__:
        if "tailLabel" in klass.__dict__:
            descriptor = klass.__dict__["tailLabel"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::annotation_is_not_abstract():
    assert not inspect.isabstract(classmodel::Annotation)


def test_classmodel::annotation_constructor_exists():
    assert callable(classmodel::Annotation.__init__)


def test_classmodel::annotation_constructor_args():
    sig = inspect.signature(classmodel::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_classmodel::feature_is_not_abstract():
    assert not inspect.isabstract(classmodel::Feature)


def test_classmodel::feature_constructor_exists():
    assert callable(classmodel::Feature.__init__)


def test_classmodel::feature_constructor_args():
    sig = inspect.signature(classmodel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "value" in params, "Missing parameter 'value'"

def test_classmodel::feature_has_constraint():
    assert hasattr(classmodel::Feature, "constraint")
    descriptor = None
    for klass in classmodel::Feature.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::feature_has_name():
    assert hasattr(classmodel::Feature, "name")
    descriptor = None
    for klass in classmodel::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::feature_has_visibility():
    assert hasattr(classmodel::Feature, "visibility")
    descriptor = None
    for klass in classmodel::Feature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_classmodel::feature_has_value():
    assert hasattr(classmodel::Feature, "value")
    descriptor = None
    for klass in classmodel::Feature.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::type_is_not_abstract():
    assert not inspect.isabstract(classmodel::Type)


def test_classmodel::type_constructor_exists():
    assert callable(classmodel::Type.__init__)


def test_classmodel::type_constructor_args():
    sig = inspect.signature(classmodel::Type.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_classmodel::type_has_visibility():
    assert hasattr(classmodel::Type, "visibility")
    descriptor = None
    for klass in classmodel::Type.__mro__:
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



def test_classmodel::classifier_is_not_abstract():
    assert not inspect.isabstract(classmodel::Classifier)


def test_classmodel::classifier_constructor_exists():
    assert callable(classmodel::Classifier.__init__)


def test_classmodel::classifier_constructor_args():
    sig = inspect.signature(classmodel::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"

def test_classmodel::classifier_has_constraint():
    assert hasattr(classmodel::Classifier, "constraint")
    descriptor = None
    for klass in classmodel::Classifier.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::enumeration_is_not_abstract():
    assert not inspect.isabstract(classmodel::Enumeration)


def test_classmodel::enumeration_constructor_exists():
    assert callable(classmodel::Enumeration.__init__)


def test_classmodel::enumeration_constructor_args():
    sig = inspect.signature(classmodel::Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"

def test_classmodel::enumeration_has_constraint():
    assert hasattr(classmodel::Enumeration, "constraint")
    descriptor = None
    for klass in classmodel::Enumeration.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::datatype_is_not_abstract():
    assert not inspect.isabstract(classmodel::Datatype)


def test_classmodel::datatype_constructor_exists():
    assert callable(classmodel::Datatype.__init__)


def test_classmodel::datatype_constructor_args():
    sig = inspect.signature(classmodel::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_classmodel::relationship_is_not_abstract():
    assert not inspect.isabstract(classmodel::Relationship)


def test_classmodel::relationship_constructor_exists():
    assert callable(classmodel::Relationship.__init__)


def test_classmodel::relationship_constructor_args():
    sig = inspect.signature(classmodel::Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_classmodel::relationship_has_label():
    assert hasattr(classmodel::Relationship, "label")
    descriptor = None
    for klass in classmodel::Relationship.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::entity_is_not_abstract():
    assert not inspect.isabstract(classmodel::Entity)


def test_classmodel::entity_constructor_exists():
    assert callable(classmodel::Entity.__init__)


def test_classmodel::entity_constructor_args():
    sig = inspect.signature(classmodel::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmodel::entity_has_name():
    assert hasattr(classmodel::Entity, "name")
    descriptor = None
    for klass in classmodel::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::package_is_not_abstract():
    assert not inspect.isabstract(classmodel::Package)


def test_classmodel::package_constructor_exists():
    assert callable(classmodel::Package.__init__)


def test_classmodel::package_constructor_args():
    sig = inspect.signature(classmodel::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classmodel::package_has_name():
    assert hasattr(classmodel::Package, "name")
    descriptor = None
    for klass in classmodel::Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::element_is_not_abstract():
    assert not inspect.isabstract(classmodel::Element)


def test_classmodel::element_constructor_exists():
    assert callable(classmodel::Element.__init__)


def test_classmodel::element_constructor_args():
    sig = inspect.signature(classmodel::Element.__init__)
    params = list(sig.parameters.keys())



def test_classmodel::import_is_not_abstract():
    assert not inspect.isabstract(classmodel::Import)


def test_classmodel::import_constructor_exists():
    assert callable(classmodel::Import.__init__)


def test_classmodel::import_constructor_args():
    sig = inspect.signature(classmodel::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_classmodel::import_has_importURI():
    assert hasattr(classmodel::Import, "importURI")
    descriptor = None
    for klass in classmodel::Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_classmodel::model_is_not_abstract():
    assert not inspect.isabstract(classmodel::Model)


def test_classmodel::model_constructor_exists():
    assert callable(classmodel::Model.__init__)


def test_classmodel::model_constructor_args():
    sig = inspect.signature(classmodel::Model.__init__)
    params = list(sig.parameters.keys())

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "PRIVATE",
        "PUBLIC",
        "PROTECTED",
        "PACKAGE_PRIVATE",
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
classmodel::Constant_strategy = st.builds(
    classmodel::Constant,
)
classmodel::Array_strategy = st.builds(
    classmodel::Array,
)
classmodel::Attribute_strategy = st.builds(
    classmodel::Attribute,
    static=
        st.booleans(),
    implicit=
        safe_text
)
classmodel::Reference_strategy = st.builds(
    classmodel::Reference,
)
classmodel::Parameter_strategy = st.builds(
    classmodel::Parameter,
    implicit=
        safe_text,
    name=
        safe_text
)
classmodel::Operation_strategy = st.builds(
    classmodel::Operation,
    body=
        safe_text,
    static=
        st.booleans()
)
classmodel::Multiplicity_strategy = st.builds(
    classmodel::Multiplicity,
    lower=
        safe_text,
    upper=
        safe_text
)
Relationship_strategy = st.builds(
    Relationship,
)
classmodel::Dependency_strategy = st.builds(
    classmodel::Dependency,
)
classmodel::Generalization_strategy = st.builds(
    classmodel::Generalization,
)
classmodel::Realization_strategy = st.builds(
    classmodel::Realization,
)
classmodel::Composition_strategy = st.builds(
    classmodel::Composition,
    headLabel=
        safe_text,
    headNavigable=
        st.booleans(),
    tailVisibility=
        safe_text,
    tailNavigable=
        st.booleans(),
    headVisibility=
        safe_text,
    tailLabel=
        safe_text
)
classmodel::Aggregation_strategy = st.builds(
    classmodel::Aggregation,
    tailVisibility=
        safe_text,
    tailLabel=
        safe_text,
    headVisibility=
        safe_text,
    headNavigable=
        st.booleans(),
    tailNavigable=
        st.booleans(),
    headLabel=
        safe_text
)
classmodel::Association_strategy = st.builds(
    classmodel::Association,
    headLabel=
        safe_text,
    tailVisibility=
        safe_text,
    tailNavigable=
        st.booleans(),
    headVisibility=
        safe_text,
    headNavigable=
        st.booleans(),
    tailLabel=
        safe_text
)
classmodel::Annotation_strategy = st.builds(
    classmodel::Annotation,
)
classmodel::Feature_strategy = st.builds(
    classmodel::Feature,
    constraint=
        safe_text,
    name=
        safe_text,
    visibility=
        safe_text,
    value=
        safe_text
)
classmodel::Type_strategy = st.builds(
    classmodel::Type,
    visibility=
        safe_text
)
Entity_strategy = st.builds(
    Entity,
)
classmodel::Classifier_strategy = st.builds(
    classmodel::Classifier,
    constraint=
        safe_text
)
classmodel::Enumeration_strategy = st.builds(
    classmodel::Enumeration,
    constraint=
        safe_text
)
classmodel::Datatype_strategy = st.builds(
    classmodel::Datatype,
)
Element_strategy = st.builds(
    Element,
)
classmodel::Relationship_strategy = st.builds(
    classmodel::Relationship,
    label=
        safe_text
)
classmodel::Entity_strategy = st.builds(
    classmodel::Entity,
    name=
        safe_text
)
classmodel::Package_strategy = st.builds(
    classmodel::Package,
    name=
        safe_text
)
classmodel::Element_strategy = st.builds(
    classmodel::Element,
)
classmodel::Import_strategy = st.builds(
    classmodel::Import,
    importURI=
        safe_text
)
classmodel::Model_strategy = st.builds(
    classmodel::Model,
)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=classmodel::Constant_strategy)
@settings(max_examples=50)
def test_classmodel::constant_instantiation(instance):
    assert isinstance(instance, classmodel::Constant)

@given(instance=classmodel::Array_strategy)
@settings(max_examples=50)
def test_classmodel::array_instantiation(instance):
    assert isinstance(instance, classmodel::Array)

@given(instance=classmodel::Attribute_strategy)
@settings(max_examples=50)
def test_classmodel::attribute_instantiation(instance):
    assert isinstance(instance, classmodel::Attribute)

@given(instance=classmodel::Attribute_strategy)
def test_classmodel::attribute_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=classmodel::Attribute_strategy)
def test_classmodel::attribute_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=classmodel::Attribute_strategy)
def test_classmodel::attribute_implicit_type(instance):
    assert isinstance(instance.implicit, str)


@given(instance=classmodel::Attribute_strategy)
def test_classmodel::attribute_implicit_setter(instance):
    original = instance.implicit
    instance.implicit = original
    assert instance.implicit == original

@given(instance=classmodel::Reference_strategy)
@settings(max_examples=50)
def test_classmodel::reference_instantiation(instance):
    assert isinstance(instance, classmodel::Reference)

@given(instance=classmodel::Parameter_strategy)
@settings(max_examples=50)
def test_classmodel::parameter_instantiation(instance):
    assert isinstance(instance, classmodel::Parameter)

@given(instance=classmodel::Parameter_strategy)
def test_classmodel::parameter_implicit_type(instance):
    assert isinstance(instance.implicit, str)


@given(instance=classmodel::Parameter_strategy)
def test_classmodel::parameter_implicit_setter(instance):
    original = instance.implicit
    instance.implicit = original
    assert instance.implicit == original

@given(instance=classmodel::Parameter_strategy)
def test_classmodel::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classmodel::Parameter_strategy)
def test_classmodel::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classmodel::Operation_strategy)
@settings(max_examples=50)
def test_classmodel::operation_instantiation(instance):
    assert isinstance(instance, classmodel::Operation)

@given(instance=classmodel::Operation_strategy)
def test_classmodel::operation_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=classmodel::Operation_strategy)
def test_classmodel::operation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=classmodel::Operation_strategy)
def test_classmodel::operation_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=classmodel::Operation_strategy)
def test_classmodel::operation_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=classmodel::Multiplicity_strategy)
@settings(max_examples=50)
def test_classmodel::multiplicity_instantiation(instance):
    assert isinstance(instance, classmodel::Multiplicity)

@given(instance=classmodel::Multiplicity_strategy)
def test_classmodel::multiplicity_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=classmodel::Multiplicity_strategy)
def test_classmodel::multiplicity_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=classmodel::Multiplicity_strategy)
def test_classmodel::multiplicity_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=classmodel::Multiplicity_strategy)
def test_classmodel::multiplicity_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=classmodel::Dependency_strategy)
@settings(max_examples=50)
def test_classmodel::dependency_instantiation(instance):
    assert isinstance(instance, classmodel::Dependency)

@given(instance=classmodel::Generalization_strategy)
@settings(max_examples=50)
def test_classmodel::generalization_instantiation(instance):
    assert isinstance(instance, classmodel::Generalization)

@given(instance=classmodel::Realization_strategy)
@settings(max_examples=50)
def test_classmodel::realization_instantiation(instance):
    assert isinstance(instance, classmodel::Realization)

@given(instance=classmodel::Composition_strategy)
@settings(max_examples=50)
def test_classmodel::composition_instantiation(instance):
    assert isinstance(instance, classmodel::Composition)

@given(instance=classmodel::Composition_strategy)
def test_classmodel::composition_headLabel_type(instance):
    assert isinstance(instance.headLabel, str)


@given(instance=classmodel::Composition_strategy)
def test_classmodel::composition_headLabel_setter(instance):
    original = instance.headLabel
    instance.headLabel = original
    assert instance.headLabel == original

@given(instance=classmodel::Composition_strategy)
def test_classmodel::composition_headNavigable_type(instance):
    assert isinstance(instance.headNavigable, bool)


@given(instance=classmodel::Composition_strategy)
def test_classmodel::composition_headNavigable_setter(instance):
    original = instance.headNavigable
    instance.headNavigable = original
    assert instance.headNavigable == original

@given(instance=classmodel::Composition_strategy)
def test_classmodel::composition_tailVisibility_type(instance):
    assert isinstance(instance.tailVisibility, str)


@given(instance=classmodel::Composition_strategy)
def test_classmodel::composition_tailVisibility_setter(instance):
    original = instance.tailVisibility
    instance.tailVisibility = original
    assert instance.tailVisibility == original

@given(instance=classmodel::Composition_strategy)
def test_classmodel::composition_tailNavigable_type(instance):
    assert isinstance(instance.tailNavigable, bool)


@given(instance=classmodel::Composition_strategy)
def test_classmodel::composition_tailNavigable_setter(instance):
    original = instance.tailNavigable
    instance.tailNavigable = original
    assert instance.tailNavigable == original

@given(instance=classmodel::Composition_strategy)
def test_classmodel::composition_headVisibility_type(instance):
    assert isinstance(instance.headVisibility, str)


@given(instance=classmodel::Composition_strategy)
def test_classmodel::composition_headVisibility_setter(instance):
    original = instance.headVisibility
    instance.headVisibility = original
    assert instance.headVisibility == original

@given(instance=classmodel::Composition_strategy)
def test_classmodel::composition_tailLabel_type(instance):
    assert isinstance(instance.tailLabel, str)


@given(instance=classmodel::Composition_strategy)
def test_classmodel::composition_tailLabel_setter(instance):
    original = instance.tailLabel
    instance.tailLabel = original
    assert instance.tailLabel == original

@given(instance=classmodel::Aggregation_strategy)
@settings(max_examples=50)
def test_classmodel::aggregation_instantiation(instance):
    assert isinstance(instance, classmodel::Aggregation)

@given(instance=classmodel::Aggregation_strategy)
def test_classmodel::aggregation_tailVisibility_type(instance):
    assert isinstance(instance.tailVisibility, str)


@given(instance=classmodel::Aggregation_strategy)
def test_classmodel::aggregation_tailVisibility_setter(instance):
    original = instance.tailVisibility
    instance.tailVisibility = original
    assert instance.tailVisibility == original

@given(instance=classmodel::Aggregation_strategy)
def test_classmodel::aggregation_tailLabel_type(instance):
    assert isinstance(instance.tailLabel, str)


@given(instance=classmodel::Aggregation_strategy)
def test_classmodel::aggregation_tailLabel_setter(instance):
    original = instance.tailLabel
    instance.tailLabel = original
    assert instance.tailLabel == original

@given(instance=classmodel::Aggregation_strategy)
def test_classmodel::aggregation_headVisibility_type(instance):
    assert isinstance(instance.headVisibility, str)


@given(instance=classmodel::Aggregation_strategy)
def test_classmodel::aggregation_headVisibility_setter(instance):
    original = instance.headVisibility
    instance.headVisibility = original
    assert instance.headVisibility == original

@given(instance=classmodel::Aggregation_strategy)
def test_classmodel::aggregation_headNavigable_type(instance):
    assert isinstance(instance.headNavigable, bool)


@given(instance=classmodel::Aggregation_strategy)
def test_classmodel::aggregation_headNavigable_setter(instance):
    original = instance.headNavigable
    instance.headNavigable = original
    assert instance.headNavigable == original

@given(instance=classmodel::Aggregation_strategy)
def test_classmodel::aggregation_tailNavigable_type(instance):
    assert isinstance(instance.tailNavigable, bool)


@given(instance=classmodel::Aggregation_strategy)
def test_classmodel::aggregation_tailNavigable_setter(instance):
    original = instance.tailNavigable
    instance.tailNavigable = original
    assert instance.tailNavigable == original

@given(instance=classmodel::Aggregation_strategy)
def test_classmodel::aggregation_headLabel_type(instance):
    assert isinstance(instance.headLabel, str)


@given(instance=classmodel::Aggregation_strategy)
def test_classmodel::aggregation_headLabel_setter(instance):
    original = instance.headLabel
    instance.headLabel = original
    assert instance.headLabel == original

@given(instance=classmodel::Association_strategy)
@settings(max_examples=50)
def test_classmodel::association_instantiation(instance):
    assert isinstance(instance, classmodel::Association)

@given(instance=classmodel::Association_strategy)
def test_classmodel::association_headLabel_type(instance):
    assert isinstance(instance.headLabel, str)


@given(instance=classmodel::Association_strategy)
def test_classmodel::association_headLabel_setter(instance):
    original = instance.headLabel
    instance.headLabel = original
    assert instance.headLabel == original

@given(instance=classmodel::Association_strategy)
def test_classmodel::association_tailVisibility_type(instance):
    assert isinstance(instance.tailVisibility, str)


@given(instance=classmodel::Association_strategy)
def test_classmodel::association_tailVisibility_setter(instance):
    original = instance.tailVisibility
    instance.tailVisibility = original
    assert instance.tailVisibility == original

@given(instance=classmodel::Association_strategy)
def test_classmodel::association_tailNavigable_type(instance):
    assert isinstance(instance.tailNavigable, bool)


@given(instance=classmodel::Association_strategy)
def test_classmodel::association_tailNavigable_setter(instance):
    original = instance.tailNavigable
    instance.tailNavigable = original
    assert instance.tailNavigable == original

@given(instance=classmodel::Association_strategy)
def test_classmodel::association_headVisibility_type(instance):
    assert isinstance(instance.headVisibility, str)


@given(instance=classmodel::Association_strategy)
def test_classmodel::association_headVisibility_setter(instance):
    original = instance.headVisibility
    instance.headVisibility = original
    assert instance.headVisibility == original

@given(instance=classmodel::Association_strategy)
def test_classmodel::association_headNavigable_type(instance):
    assert isinstance(instance.headNavigable, bool)


@given(instance=classmodel::Association_strategy)
def test_classmodel::association_headNavigable_setter(instance):
    original = instance.headNavigable
    instance.headNavigable = original
    assert instance.headNavigable == original

@given(instance=classmodel::Association_strategy)
def test_classmodel::association_tailLabel_type(instance):
    assert isinstance(instance.tailLabel, str)


@given(instance=classmodel::Association_strategy)
def test_classmodel::association_tailLabel_setter(instance):
    original = instance.tailLabel
    instance.tailLabel = original
    assert instance.tailLabel == original

@given(instance=classmodel::Annotation_strategy)
@settings(max_examples=50)
def test_classmodel::annotation_instantiation(instance):
    assert isinstance(instance, classmodel::Annotation)

@given(instance=classmodel::Feature_strategy)
@settings(max_examples=50)
def test_classmodel::feature_instantiation(instance):
    assert isinstance(instance, classmodel::Feature)

@given(instance=classmodel::Feature_strategy)
def test_classmodel::feature_constraint_type(instance):
    assert isinstance(instance.constraint, str)


@given(instance=classmodel::Feature_strategy)
def test_classmodel::feature_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=classmodel::Feature_strategy)
def test_classmodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classmodel::Feature_strategy)
def test_classmodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classmodel::Feature_strategy)
def test_classmodel::feature_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=classmodel::Feature_strategy)
def test_classmodel::feature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=classmodel::Feature_strategy)
def test_classmodel::feature_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=classmodel::Feature_strategy)
def test_classmodel::feature_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=classmodel::Type_strategy)
@settings(max_examples=50)
def test_classmodel::type_instantiation(instance):
    assert isinstance(instance, classmodel::Type)

@given(instance=classmodel::Type_strategy)
def test_classmodel::type_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=classmodel::Type_strategy)
def test_classmodel::type_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=classmodel::Classifier_strategy)
@settings(max_examples=50)
def test_classmodel::classifier_instantiation(instance):
    assert isinstance(instance, classmodel::Classifier)

@given(instance=classmodel::Classifier_strategy)
def test_classmodel::classifier_constraint_type(instance):
    assert isinstance(instance.constraint, str)


@given(instance=classmodel::Classifier_strategy)
def test_classmodel::classifier_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=classmodel::Enumeration_strategy)
@settings(max_examples=50)
def test_classmodel::enumeration_instantiation(instance):
    assert isinstance(instance, classmodel::Enumeration)

@given(instance=classmodel::Enumeration_strategy)
def test_classmodel::enumeration_constraint_type(instance):
    assert isinstance(instance.constraint, str)


@given(instance=classmodel::Enumeration_strategy)
def test_classmodel::enumeration_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=classmodel::Datatype_strategy)
@settings(max_examples=50)
def test_classmodel::datatype_instantiation(instance):
    assert isinstance(instance, classmodel::Datatype)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=classmodel::Relationship_strategy)
@settings(max_examples=50)
def test_classmodel::relationship_instantiation(instance):
    assert isinstance(instance, classmodel::Relationship)

@given(instance=classmodel::Relationship_strategy)
def test_classmodel::relationship_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=classmodel::Relationship_strategy)
def test_classmodel::relationship_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=classmodel::Entity_strategy)
@settings(max_examples=50)
def test_classmodel::entity_instantiation(instance):
    assert isinstance(instance, classmodel::Entity)

@given(instance=classmodel::Entity_strategy)
def test_classmodel::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classmodel::Entity_strategy)
def test_classmodel::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classmodel::Package_strategy)
@settings(max_examples=50)
def test_classmodel::package_instantiation(instance):
    assert isinstance(instance, classmodel::Package)

@given(instance=classmodel::Package_strategy)
def test_classmodel::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classmodel::Package_strategy)
def test_classmodel::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=classmodel::Element_strategy)
@settings(max_examples=50)
def test_classmodel::element_instantiation(instance):
    assert isinstance(instance, classmodel::Element)

@given(instance=classmodel::Import_strategy)
@settings(max_examples=50)
def test_classmodel::import_instantiation(instance):
    assert isinstance(instance, classmodel::Import)

@given(instance=classmodel::Import_strategy)
def test_classmodel::import_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=classmodel::Import_strategy)
def test_classmodel::import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=classmodel::Model_strategy)
@settings(max_examples=50)
def test_classmodel::model_instantiation(instance):
    assert isinstance(instance, classmodel::Model)
