import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    yuml::ClassMember,
    ClassMember,
    yuml::Cardinality,
    Relationship,
    yuml::Equivalence,
    yuml::NoteAssociation,
    yuml::Inheritance,
    yuml::Association,
    ModelElement,
    yuml::Relationship,
    yuml::ColorableElement,
    yuml::ModelElement,
    yuml::Model,
    yuml::Method,
    yuml::Attribute,
    ColorableElement,
    yuml::Note,
    yuml::Class,
    Visibility,
    AssociationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yuml::classmember_is_not_abstract():
    assert not inspect.isabstract(yuml::ClassMember)


def test_yuml::classmember_constructor_exists():
    assert callable(yuml::ClassMember.__init__)


def test_yuml::classmember_constructor_args():
    sig = inspect.signature(yuml::ClassMember.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_yuml::classmember_has_visibility():
    assert hasattr(yuml::ClassMember, "visibility")
    descriptor = None
    for klass in yuml::ClassMember.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_yuml::classmember_has_name():
    assert hasattr(yuml::ClassMember, "name")
    descriptor = None
    for klass in yuml::ClassMember.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classmember_is_not_abstract():
    assert not inspect.isabstract(ClassMember)


def test_classmember_constructor_exists():
    assert callable(ClassMember.__init__)


def test_classmember_constructor_args():
    sig = inspect.signature(ClassMember.__init__)
    params = list(sig.parameters.keys())



def test_yuml::cardinality_is_not_abstract():
    assert not inspect.isabstract(yuml::Cardinality)


def test_yuml::cardinality_constructor_exists():
    assert callable(yuml::Cardinality.__init__)


def test_yuml::cardinality_constructor_args():
    sig = inspect.signature(yuml::Cardinality.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_yuml::cardinality_has_upperBound():
    assert hasattr(yuml::Cardinality, "upperBound")
    descriptor = None
    for klass in yuml::Cardinality.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_yuml::cardinality_has_lowerBound():
    assert hasattr(yuml::Cardinality, "lowerBound")
    descriptor = None
    for klass in yuml::Cardinality.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_yuml::equivalence_is_not_abstract():
    assert not inspect.isabstract(yuml::Equivalence)


def test_yuml::equivalence_constructor_exists():
    assert callable(yuml::Equivalence.__init__)


def test_yuml::equivalence_constructor_args():
    sig = inspect.signature(yuml::Equivalence.__init__)
    params = list(sig.parameters.keys())



def test_yuml::noteassociation_is_not_abstract():
    assert not inspect.isabstract(yuml::NoteAssociation)


def test_yuml::noteassociation_constructor_exists():
    assert callable(yuml::NoteAssociation.__init__)


def test_yuml::noteassociation_constructor_args():
    sig = inspect.signature(yuml::NoteAssociation.__init__)
    params = list(sig.parameters.keys())



def test_yuml::inheritance_is_not_abstract():
    assert not inspect.isabstract(yuml::Inheritance)


def test_yuml::inheritance_constructor_exists():
    assert callable(yuml::Inheritance.__init__)


def test_yuml::inheritance_constructor_args():
    sig = inspect.signature(yuml::Inheritance.__init__)
    params = list(sig.parameters.keys())



def test_yuml::association_is_not_abstract():
    assert not inspect.isabstract(yuml::Association)


def test_yuml::association_constructor_exists():
    assert callable(yuml::Association.__init__)


def test_yuml::association_constructor_args():
    sig = inspect.signature(yuml::Association.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "navigableTarget" in params, "Missing parameter 'navigableTarget'"
    assert "navigableSource" in params, "Missing parameter 'navigableSource'"
    assert "targetVisibility" in params, "Missing parameter 'targetVisibility'"
    assert "sourceVisibility" in params, "Missing parameter 'sourceVisibility'"

def test_yuml::association_has_type():
    assert hasattr(yuml::Association, "type")
    descriptor = None
    for klass in yuml::Association.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_yuml::association_has_navigableTarget():
    assert hasattr(yuml::Association, "navigableTarget")
    descriptor = None
    for klass in yuml::Association.__mro__:
        if "navigableTarget" in klass.__dict__:
            descriptor = klass.__dict__["navigableTarget"]
            break
    assert isinstance(descriptor, property)

def test_yuml::association_has_navigableSource():
    assert hasattr(yuml::Association, "navigableSource")
    descriptor = None
    for klass in yuml::Association.__mro__:
        if "navigableSource" in klass.__dict__:
            descriptor = klass.__dict__["navigableSource"]
            break
    assert isinstance(descriptor, property)

def test_yuml::association_has_targetVisibility():
    assert hasattr(yuml::Association, "targetVisibility")
    descriptor = None
    for klass in yuml::Association.__mro__:
        if "targetVisibility" in klass.__dict__:
            descriptor = klass.__dict__["targetVisibility"]
            break
    assert isinstance(descriptor, property)

def test_yuml::association_has_sourceVisibility():
    assert hasattr(yuml::Association, "sourceVisibility")
    descriptor = None
    for klass in yuml::Association.__mro__:
        if "sourceVisibility" in klass.__dict__:
            descriptor = klass.__dict__["sourceVisibility"]
            break
    assert isinstance(descriptor, property)



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_yuml::relationship_is_not_abstract():
    assert not inspect.isabstract(yuml::Relationship)


def test_yuml::relationship_constructor_exists():
    assert callable(yuml::Relationship.__init__)


def test_yuml::relationship_constructor_args():
    sig = inspect.signature(yuml::Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "targetLabel" in params, "Missing parameter 'targetLabel'"
    assert "sourceLabel" in params, "Missing parameter 'sourceLabel'"

def test_yuml::relationship_has_targetLabel():
    assert hasattr(yuml::Relationship, "targetLabel")
    descriptor = None
    for klass in yuml::Relationship.__mro__:
        if "targetLabel" in klass.__dict__:
            descriptor = klass.__dict__["targetLabel"]
            break
    assert isinstance(descriptor, property)

def test_yuml::relationship_has_sourceLabel():
    assert hasattr(yuml::Relationship, "sourceLabel")
    descriptor = None
    for klass in yuml::Relationship.__mro__:
        if "sourceLabel" in klass.__dict__:
            descriptor = klass.__dict__["sourceLabel"]
            break
    assert isinstance(descriptor, property)



def test_yuml::colorableelement_is_not_abstract():
    assert not inspect.isabstract(yuml::ColorableElement)


def test_yuml::colorableelement_constructor_exists():
    assert callable(yuml::ColorableElement.__init__)


def test_yuml::colorableelement_constructor_args():
    sig = inspect.signature(yuml::ColorableElement.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_yuml::colorableelement_has_color():
    assert hasattr(yuml::ColorableElement, "color")
    descriptor = None
    for klass in yuml::ColorableElement.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_yuml::modelelement_is_not_abstract():
    assert not inspect.isabstract(yuml::ModelElement)


def test_yuml::modelelement_constructor_exists():
    assert callable(yuml::ModelElement.__init__)


def test_yuml::modelelement_constructor_args():
    sig = inspect.signature(yuml::ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_yuml::model_is_not_abstract():
    assert not inspect.isabstract(yuml::Model)


def test_yuml::model_constructor_exists():
    assert callable(yuml::Model.__init__)


def test_yuml::model_constructor_args():
    sig = inspect.signature(yuml::Model.__init__)
    params = list(sig.parameters.keys())



def test_yuml::method_is_not_abstract():
    assert not inspect.isabstract(yuml::Method)


def test_yuml::method_constructor_exists():
    assert callable(yuml::Method.__init__)


def test_yuml::method_constructor_args():
    sig = inspect.signature(yuml::Method.__init__)
    params = list(sig.parameters.keys())
    assert "arguments" in params, "Missing parameter 'arguments'"

def test_yuml::method_has_arguments():
    assert hasattr(yuml::Method, "arguments")
    descriptor = None
    for klass in yuml::Method.__mro__:
        if "arguments" in klass.__dict__:
            descriptor = klass.__dict__["arguments"]
            break
    assert isinstance(descriptor, property)



def test_yuml::attribute_is_not_abstract():
    assert not inspect.isabstract(yuml::Attribute)


def test_yuml::attribute_constructor_exists():
    assert callable(yuml::Attribute.__init__)


def test_yuml::attribute_constructor_args():
    sig = inspect.signature(yuml::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"
    assert "type" in params, "Missing parameter 'type'"

def test_yuml::attribute_has_stereotype():
    assert hasattr(yuml::Attribute, "stereotype")
    descriptor = None
    for klass in yuml::Attribute.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)

def test_yuml::attribute_has_type():
    assert hasattr(yuml::Attribute, "type")
    descriptor = None
    for klass in yuml::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_colorableelement_is_not_abstract():
    assert not inspect.isabstract(ColorableElement)


def test_colorableelement_constructor_exists():
    assert callable(ColorableElement.__init__)


def test_colorableelement_constructor_args():
    sig = inspect.signature(ColorableElement.__init__)
    params = list(sig.parameters.keys())



def test_yuml::note_is_not_abstract():
    assert not inspect.isabstract(yuml::Note)


def test_yuml::note_constructor_exists():
    assert callable(yuml::Note.__init__)


def test_yuml::note_constructor_args():
    sig = inspect.signature(yuml::Note.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yuml::note_has_text():
    assert hasattr(yuml::Note, "text")
    descriptor = None
    for klass in yuml::Note.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yuml::class_is_not_abstract():
    assert not inspect.isabstract(yuml::Class)


def test_yuml::class_constructor_exists():
    assert callable(yuml::Class.__init__)


def test_yuml::class_constructor_args():
    sig = inspect.signature(yuml::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_yuml::class_has_name():
    assert hasattr(yuml::Class, "name")
    descriptor = None
    for klass in yuml::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_yuml::class_has_stereotype():
    assert hasattr(yuml::Class, "stereotype")
    descriptor = None
    for klass in yuml::Class.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "package",
        "unspecified",
        "protected",
        "private",
        "public",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"

def test_associationtype_exists():
    # Check that the Enumeration exists
    assert AssociationType is not None

def test_associationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssociationType]
    expected_literals = [
        "aggregation",
        "simpleAssociation",
        "composition",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssociationType"


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
yuml::ClassMember_strategy = st.builds(
    yuml::ClassMember,
    visibility=
        safe_text,
    name=
        safe_text
)
ClassMember_strategy = st.builds(
    ClassMember,
)
yuml::Cardinality_strategy = st.builds(
    yuml::Cardinality,
    upperBound=
        safe_text,
    lowerBound=
        safe_text
)
Relationship_strategy = st.builds(
    Relationship,
)
yuml::Equivalence_strategy = st.builds(
    yuml::Equivalence,
)
yuml::NoteAssociation_strategy = st.builds(
    yuml::NoteAssociation,
)
yuml::Inheritance_strategy = st.builds(
    yuml::Inheritance,
)
yuml::Association_strategy = st.builds(
    yuml::Association,
    type=
        safe_text,
    navigableTarget=
        st.booleans(),
    navigableSource=
        st.booleans(),
    targetVisibility=
        safe_text,
    sourceVisibility=
        safe_text
)
ModelElement_strategy = st.builds(
    ModelElement,
)
yuml::Relationship_strategy = st.builds(
    yuml::Relationship,
    targetLabel=
        safe_text,
    sourceLabel=
        safe_text
)
yuml::ColorableElement_strategy = st.builds(
    yuml::ColorableElement,
    color=
        safe_text
)
yuml::ModelElement_strategy = st.builds(
    yuml::ModelElement,
)
yuml::Model_strategy = st.builds(
    yuml::Model,
)
yuml::Method_strategy = st.builds(
    yuml::Method,
    arguments=
        safe_text
)
yuml::Attribute_strategy = st.builds(
    yuml::Attribute,
    stereotype=
        safe_text,
    type=
        safe_text
)
ColorableElement_strategy = st.builds(
    ColorableElement,
)
yuml::Note_strategy = st.builds(
    yuml::Note,
    text=
        safe_text
)
yuml::Class_strategy = st.builds(
    yuml::Class,
    name=
        safe_text,
    stereotype=
        safe_text
)

@given(instance=yuml::ClassMember_strategy)
@settings(max_examples=50)
def test_yuml::classmember_instantiation(instance):
    assert isinstance(instance, yuml::ClassMember)

@given(instance=yuml::ClassMember_strategy)
def test_yuml::classmember_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=yuml::ClassMember_strategy)
def test_yuml::classmember_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=yuml::ClassMember_strategy)
def test_yuml::classmember_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=yuml::ClassMember_strategy)
def test_yuml::classmember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassMember_strategy)
@settings(max_examples=50)
def test_classmember_instantiation(instance):
    assert isinstance(instance, ClassMember)

@given(instance=yuml::Cardinality_strategy)
@settings(max_examples=50)
def test_yuml::cardinality_instantiation(instance):
    assert isinstance(instance, yuml::Cardinality)

@given(instance=yuml::Cardinality_strategy)
def test_yuml::cardinality_upperBound_type(instance):
    assert isinstance(instance.upperBound, str)


@given(instance=yuml::Cardinality_strategy)
def test_yuml::cardinality_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=yuml::Cardinality_strategy)
def test_yuml::cardinality_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, str)


@given(instance=yuml::Cardinality_strategy)
def test_yuml::cardinality_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=yuml::Equivalence_strategy)
@settings(max_examples=50)
def test_yuml::equivalence_instantiation(instance):
    assert isinstance(instance, yuml::Equivalence)

@given(instance=yuml::NoteAssociation_strategy)
@settings(max_examples=50)
def test_yuml::noteassociation_instantiation(instance):
    assert isinstance(instance, yuml::NoteAssociation)

@given(instance=yuml::Inheritance_strategy)
@settings(max_examples=50)
def test_yuml::inheritance_instantiation(instance):
    assert isinstance(instance, yuml::Inheritance)

@given(instance=yuml::Association_strategy)
@settings(max_examples=50)
def test_yuml::association_instantiation(instance):
    assert isinstance(instance, yuml::Association)

@given(instance=yuml::Association_strategy)
def test_yuml::association_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=yuml::Association_strategy)
def test_yuml::association_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=yuml::Association_strategy)
def test_yuml::association_navigableTarget_type(instance):
    assert isinstance(instance.navigableTarget, bool)


@given(instance=yuml::Association_strategy)
def test_yuml::association_navigableTarget_setter(instance):
    original = instance.navigableTarget
    instance.navigableTarget = original
    assert instance.navigableTarget == original

@given(instance=yuml::Association_strategy)
def test_yuml::association_navigableSource_type(instance):
    assert isinstance(instance.navigableSource, bool)


@given(instance=yuml::Association_strategy)
def test_yuml::association_navigableSource_setter(instance):
    original = instance.navigableSource
    instance.navigableSource = original
    assert instance.navigableSource == original

@given(instance=yuml::Association_strategy)
def test_yuml::association_targetVisibility_type(instance):
    assert isinstance(instance.targetVisibility, str)


@given(instance=yuml::Association_strategy)
def test_yuml::association_targetVisibility_setter(instance):
    original = instance.targetVisibility
    instance.targetVisibility = original
    assert instance.targetVisibility == original

@given(instance=yuml::Association_strategy)
def test_yuml::association_sourceVisibility_type(instance):
    assert isinstance(instance.sourceVisibility, str)


@given(instance=yuml::Association_strategy)
def test_yuml::association_sourceVisibility_setter(instance):
    original = instance.sourceVisibility
    instance.sourceVisibility = original
    assert instance.sourceVisibility == original

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=yuml::Relationship_strategy)
@settings(max_examples=50)
def test_yuml::relationship_instantiation(instance):
    assert isinstance(instance, yuml::Relationship)

@given(instance=yuml::Relationship_strategy)
def test_yuml::relationship_targetLabel_type(instance):
    assert isinstance(instance.targetLabel, str)


@given(instance=yuml::Relationship_strategy)
def test_yuml::relationship_targetLabel_setter(instance):
    original = instance.targetLabel
    instance.targetLabel = original
    assert instance.targetLabel == original

@given(instance=yuml::Relationship_strategy)
def test_yuml::relationship_sourceLabel_type(instance):
    assert isinstance(instance.sourceLabel, str)


@given(instance=yuml::Relationship_strategy)
def test_yuml::relationship_sourceLabel_setter(instance):
    original = instance.sourceLabel
    instance.sourceLabel = original
    assert instance.sourceLabel == original

@given(instance=yuml::ColorableElement_strategy)
@settings(max_examples=50)
def test_yuml::colorableelement_instantiation(instance):
    assert isinstance(instance, yuml::ColorableElement)

@given(instance=yuml::ColorableElement_strategy)
def test_yuml::colorableelement_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=yuml::ColorableElement_strategy)
def test_yuml::colorableelement_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=yuml::ModelElement_strategy)
@settings(max_examples=50)
def test_yuml::modelelement_instantiation(instance):
    assert isinstance(instance, yuml::ModelElement)

@given(instance=yuml::Model_strategy)
@settings(max_examples=50)
def test_yuml::model_instantiation(instance):
    assert isinstance(instance, yuml::Model)

@given(instance=yuml::Method_strategy)
@settings(max_examples=50)
def test_yuml::method_instantiation(instance):
    assert isinstance(instance, yuml::Method)

@given(instance=yuml::Method_strategy)
def test_yuml::method_arguments_type(instance):
    assert isinstance(instance.arguments, str)


@given(instance=yuml::Method_strategy)
def test_yuml::method_arguments_setter(instance):
    original = instance.arguments
    instance.arguments = original
    assert instance.arguments == original

@given(instance=yuml::Attribute_strategy)
@settings(max_examples=50)
def test_yuml::attribute_instantiation(instance):
    assert isinstance(instance, yuml::Attribute)

@given(instance=yuml::Attribute_strategy)
def test_yuml::attribute_stereotype_type(instance):
    assert isinstance(instance.stereotype, str)


@given(instance=yuml::Attribute_strategy)
def test_yuml::attribute_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=yuml::Attribute_strategy)
def test_yuml::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=yuml::Attribute_strategy)
def test_yuml::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ColorableElement_strategy)
@settings(max_examples=50)
def test_colorableelement_instantiation(instance):
    assert isinstance(instance, ColorableElement)

@given(instance=yuml::Note_strategy)
@settings(max_examples=50)
def test_yuml::note_instantiation(instance):
    assert isinstance(instance, yuml::Note)

@given(instance=yuml::Note_strategy)
def test_yuml::note_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=yuml::Note_strategy)
def test_yuml::note_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=yuml::Class_strategy)
@settings(max_examples=50)
def test_yuml::class_instantiation(instance):
    assert isinstance(instance, yuml::Class)

@given(instance=yuml::Class_strategy)
def test_yuml::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=yuml::Class_strategy)
def test_yuml::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=yuml::Class_strategy)
def test_yuml::class_stereotype_type(instance):
    assert isinstance(instance.stereotype, str)


@given(instance=yuml::Class_strategy)
def test_yuml::class_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original
