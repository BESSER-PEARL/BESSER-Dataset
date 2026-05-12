import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    yuml_ClassMember,
    ClassMember,
    yuml_Cardinality,
    Relationship,
    yuml_Equivalence,
    yuml_Inheritance,
    yuml_NoteAssociation,
    yuml_Association,
    ModelElement,
    yuml_Relationship,
    yuml_ColorableElement,
    yuml_ModelElement,
    yuml_Model,
    yuml_Method,
    yuml_Attribute,
    ColorableElement,
    yuml_Note,
    yuml_Class,
    Visibility,
    AssociationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yuml_classmember_is_not_abstract():
    assert not inspect.isabstract(yuml_ClassMember)


def test_yuml_classmember_constructor_exists():
    assert callable(yuml_ClassMember.__init__)


def test_yuml_classmember_constructor_args():
    sig = inspect.signature(yuml_ClassMember.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_yuml_classmember_has_name():
    assert hasattr(yuml_ClassMember, "name")
    descriptor = None
    for klass in yuml_ClassMember.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_yuml_classmember_has_visibility():
    assert hasattr(yuml_ClassMember, "visibility")
    descriptor = None
    for klass in yuml_ClassMember.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_classmember_is_not_abstract():
    assert not inspect.isabstract(ClassMember)


def test_classmember_constructor_exists():
    assert callable(ClassMember.__init__)


def test_classmember_constructor_args():
    sig = inspect.signature(ClassMember.__init__)
    params = list(sig.parameters.keys())



def test_yuml_cardinality_is_not_abstract():
    assert not inspect.isabstract(yuml_Cardinality)


def test_yuml_cardinality_constructor_exists():
    assert callable(yuml_Cardinality.__init__)


def test_yuml_cardinality_constructor_args():
    sig = inspect.signature(yuml_Cardinality.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_yuml_cardinality_has_upperBound():
    assert hasattr(yuml_Cardinality, "upperBound")
    descriptor = None
    for klass in yuml_Cardinality.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_yuml_cardinality_has_lowerBound():
    assert hasattr(yuml_Cardinality, "lowerBound")
    descriptor = None
    for klass in yuml_Cardinality.__mro__:
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



def test_yuml_equivalence_is_not_abstract():
    assert not inspect.isabstract(yuml_Equivalence)


def test_yuml_equivalence_constructor_exists():
    assert callable(yuml_Equivalence.__init__)


def test_yuml_equivalence_constructor_args():
    sig = inspect.signature(yuml_Equivalence.__init__)
    params = list(sig.parameters.keys())



def test_yuml_inheritance_is_not_abstract():
    assert not inspect.isabstract(yuml_Inheritance)


def test_yuml_inheritance_constructor_exists():
    assert callable(yuml_Inheritance.__init__)


def test_yuml_inheritance_constructor_args():
    sig = inspect.signature(yuml_Inheritance.__init__)
    params = list(sig.parameters.keys())



def test_yuml_noteassociation_is_not_abstract():
    assert not inspect.isabstract(yuml_NoteAssociation)


def test_yuml_noteassociation_constructor_exists():
    assert callable(yuml_NoteAssociation.__init__)


def test_yuml_noteassociation_constructor_args():
    sig = inspect.signature(yuml_NoteAssociation.__init__)
    params = list(sig.parameters.keys())



def test_yuml_association_is_not_abstract():
    assert not inspect.isabstract(yuml_Association)


def test_yuml_association_constructor_exists():
    assert callable(yuml_Association.__init__)


def test_yuml_association_constructor_args():
    sig = inspect.signature(yuml_Association.__init__)
    params = list(sig.parameters.keys())
    assert "navigableTarget" in params, "Missing parameter 'navigableTarget'"
    assert "type" in params, "Missing parameter 'type'"
    assert "navigableSource" in params, "Missing parameter 'navigableSource'"
    assert "targetVisibility" in params, "Missing parameter 'targetVisibility'"
    assert "sourceVisibility" in params, "Missing parameter 'sourceVisibility'"

def test_yuml_association_has_navigableTarget():
    assert hasattr(yuml_Association, "navigableTarget")
    descriptor = None
    for klass in yuml_Association.__mro__:
        if "navigableTarget" in klass.__dict__:
            descriptor = klass.__dict__["navigableTarget"]
            break
    assert isinstance(descriptor, property)

def test_yuml_association_has_type():
    assert hasattr(yuml_Association, "type")
    descriptor = None
    for klass in yuml_Association.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_yuml_association_has_navigableSource():
    assert hasattr(yuml_Association, "navigableSource")
    descriptor = None
    for klass in yuml_Association.__mro__:
        if "navigableSource" in klass.__dict__:
            descriptor = klass.__dict__["navigableSource"]
            break
    assert isinstance(descriptor, property)

def test_yuml_association_has_targetVisibility():
    assert hasattr(yuml_Association, "targetVisibility")
    descriptor = None
    for klass in yuml_Association.__mro__:
        if "targetVisibility" in klass.__dict__:
            descriptor = klass.__dict__["targetVisibility"]
            break
    assert isinstance(descriptor, property)

def test_yuml_association_has_sourceVisibility():
    assert hasattr(yuml_Association, "sourceVisibility")
    descriptor = None
    for klass in yuml_Association.__mro__:
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



def test_yuml_relationship_is_not_abstract():
    assert not inspect.isabstract(yuml_Relationship)


def test_yuml_relationship_constructor_exists():
    assert callable(yuml_Relationship.__init__)


def test_yuml_relationship_constructor_args():
    sig = inspect.signature(yuml_Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "sourceLabel" in params, "Missing parameter 'sourceLabel'"
    assert "targetLabel" in params, "Missing parameter 'targetLabel'"

def test_yuml_relationship_has_sourceLabel():
    assert hasattr(yuml_Relationship, "sourceLabel")
    descriptor = None
    for klass in yuml_Relationship.__mro__:
        if "sourceLabel" in klass.__dict__:
            descriptor = klass.__dict__["sourceLabel"]
            break
    assert isinstance(descriptor, property)

def test_yuml_relationship_has_targetLabel():
    assert hasattr(yuml_Relationship, "targetLabel")
    descriptor = None
    for klass in yuml_Relationship.__mro__:
        if "targetLabel" in klass.__dict__:
            descriptor = klass.__dict__["targetLabel"]
            break
    assert isinstance(descriptor, property)



def test_yuml_colorableelement_is_not_abstract():
    assert not inspect.isabstract(yuml_ColorableElement)


def test_yuml_colorableelement_constructor_exists():
    assert callable(yuml_ColorableElement.__init__)


def test_yuml_colorableelement_constructor_args():
    sig = inspect.signature(yuml_ColorableElement.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_yuml_colorableelement_has_color():
    assert hasattr(yuml_ColorableElement, "color")
    descriptor = None
    for klass in yuml_ColorableElement.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_yuml_modelelement_is_not_abstract():
    assert not inspect.isabstract(yuml_ModelElement)


def test_yuml_modelelement_constructor_exists():
    assert callable(yuml_ModelElement.__init__)


def test_yuml_modelelement_constructor_args():
    sig = inspect.signature(yuml_ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_yuml_model_is_not_abstract():
    assert not inspect.isabstract(yuml_Model)


def test_yuml_model_constructor_exists():
    assert callable(yuml_Model.__init__)


def test_yuml_model_constructor_args():
    sig = inspect.signature(yuml_Model.__init__)
    params = list(sig.parameters.keys())



def test_yuml_method_is_not_abstract():
    assert not inspect.isabstract(yuml_Method)


def test_yuml_method_constructor_exists():
    assert callable(yuml_Method.__init__)


def test_yuml_method_constructor_args():
    sig = inspect.signature(yuml_Method.__init__)
    params = list(sig.parameters.keys())
    assert "arguments" in params, "Missing parameter 'arguments'"

def test_yuml_method_has_arguments():
    assert hasattr(yuml_Method, "arguments")
    descriptor = None
    for klass in yuml_Method.__mro__:
        if "arguments" in klass.__dict__:
            descriptor = klass.__dict__["arguments"]
            break
    assert isinstance(descriptor, property)



def test_yuml_attribute_is_not_abstract():
    assert not inspect.isabstract(yuml_Attribute)


def test_yuml_attribute_constructor_exists():
    assert callable(yuml_Attribute.__init__)


def test_yuml_attribute_constructor_args():
    sig = inspect.signature(yuml_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"
    assert "type" in params, "Missing parameter 'type'"

def test_yuml_attribute_has_stereotype():
    assert hasattr(yuml_Attribute, "stereotype")
    descriptor = None
    for klass in yuml_Attribute.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)

def test_yuml_attribute_has_type():
    assert hasattr(yuml_Attribute, "type")
    descriptor = None
    for klass in yuml_Attribute.__mro__:
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



def test_yuml_note_is_not_abstract():
    assert not inspect.isabstract(yuml_Note)


def test_yuml_note_constructor_exists():
    assert callable(yuml_Note.__init__)


def test_yuml_note_constructor_args():
    sig = inspect.signature(yuml_Note.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yuml_note_has_text():
    assert hasattr(yuml_Note, "text")
    descriptor = None
    for klass in yuml_Note.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yuml_class_is_not_abstract():
    assert not inspect.isabstract(yuml_Class)


def test_yuml_class_constructor_exists():
    assert callable(yuml_Class.__init__)


def test_yuml_class_constructor_args():
    sig = inspect.signature(yuml_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_yuml_class_has_name():
    assert hasattr(yuml_Class, "name")
    descriptor = None
    for klass in yuml_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_yuml_class_has_stereotype():
    assert hasattr(yuml_Class, "stereotype")
    descriptor = None
    for klass in yuml_Class.__mro__:
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
        "private",
        "protected",
        "unspecified",
        "package",
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
        "composition",
        "aggregation",
        "simpleAssociation",
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
yuml_ClassMember_strategy = st.builds(
    yuml_ClassMember,
    name=
        safe_text,
    visibility=
        safe_text
)
ClassMember_strategy = st.builds(
    ClassMember,
)
yuml_Cardinality_strategy = st.builds(
    yuml_Cardinality,
    upperBound=
        safe_text,
    lowerBound=
        safe_text
)
Relationship_strategy = st.builds(
    Relationship,
)
yuml_Equivalence_strategy = st.builds(
    yuml_Equivalence,
)
yuml_Inheritance_strategy = st.builds(
    yuml_Inheritance,
)
yuml_NoteAssociation_strategy = st.builds(
    yuml_NoteAssociation,
)
yuml_Association_strategy = st.builds(
    yuml_Association,
    navigableTarget=
        st.booleans(),
    type=
        safe_text,
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
yuml_Relationship_strategy = st.builds(
    yuml_Relationship,
    sourceLabel=
        safe_text,
    targetLabel=
        safe_text
)
yuml_ColorableElement_strategy = st.builds(
    yuml_ColorableElement,
    color=
        safe_text
)
yuml_ModelElement_strategy = st.builds(
    yuml_ModelElement,
)
yuml_Model_strategy = st.builds(
    yuml_Model,
)
yuml_Method_strategy = st.builds(
    yuml_Method,
    arguments=
        safe_text
)
yuml_Attribute_strategy = st.builds(
    yuml_Attribute,
    stereotype=
        safe_text,
    type=
        safe_text
)
ColorableElement_strategy = st.builds(
    ColorableElement,
)
yuml_Note_strategy = st.builds(
    yuml_Note,
    text=
        safe_text
)
yuml_Class_strategy = st.builds(
    yuml_Class,
    name=
        safe_text,
    stereotype=
        safe_text
)

@given(instance=yuml_ClassMember_strategy)
@settings(max_examples=50)
def test_yuml_classmember_instantiation(instance):
    assert isinstance(instance, yuml_ClassMember)



@given(instance=yuml_ClassMember_strategy)
def test_yuml_classmember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=yuml_ClassMember_strategy)
def test_yuml_classmember_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=ClassMember_strategy)
@settings(max_examples=50)
def test_classmember_instantiation(instance):
    assert isinstance(instance, ClassMember)

@given(instance=yuml_Cardinality_strategy)
@settings(max_examples=50)
def test_yuml_cardinality_instantiation(instance):
    assert isinstance(instance, yuml_Cardinality)



@given(instance=yuml_Cardinality_strategy)
def test_yuml_cardinality_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original



@given(instance=yuml_Cardinality_strategy)
def test_yuml_cardinality_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=yuml_Equivalence_strategy)
@settings(max_examples=50)
def test_yuml_equivalence_instantiation(instance):
    assert isinstance(instance, yuml_Equivalence)

@given(instance=yuml_Inheritance_strategy)
@settings(max_examples=50)
def test_yuml_inheritance_instantiation(instance):
    assert isinstance(instance, yuml_Inheritance)

@given(instance=yuml_NoteAssociation_strategy)
@settings(max_examples=50)
def test_yuml_noteassociation_instantiation(instance):
    assert isinstance(instance, yuml_NoteAssociation)

@given(instance=yuml_Association_strategy)
@settings(max_examples=50)
def test_yuml_association_instantiation(instance):
    assert isinstance(instance, yuml_Association)



@given(instance=yuml_Association_strategy)
def test_yuml_association_navigableTarget_setter(instance):
    original = instance.navigableTarget
    instance.navigableTarget = original
    assert instance.navigableTarget == original



@given(instance=yuml_Association_strategy)
def test_yuml_association_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=yuml_Association_strategy)
def test_yuml_association_navigableSource_setter(instance):
    original = instance.navigableSource
    instance.navigableSource = original
    assert instance.navigableSource == original



@given(instance=yuml_Association_strategy)
def test_yuml_association_targetVisibility_setter(instance):
    original = instance.targetVisibility
    instance.targetVisibility = original
    assert instance.targetVisibility == original



@given(instance=yuml_Association_strategy)
def test_yuml_association_sourceVisibility_setter(instance):
    original = instance.sourceVisibility
    instance.sourceVisibility = original
    assert instance.sourceVisibility == original

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=yuml_Relationship_strategy)
@settings(max_examples=50)
def test_yuml_relationship_instantiation(instance):
    assert isinstance(instance, yuml_Relationship)



@given(instance=yuml_Relationship_strategy)
def test_yuml_relationship_sourceLabel_setter(instance):
    original = instance.sourceLabel
    instance.sourceLabel = original
    assert instance.sourceLabel == original



@given(instance=yuml_Relationship_strategy)
def test_yuml_relationship_targetLabel_setter(instance):
    original = instance.targetLabel
    instance.targetLabel = original
    assert instance.targetLabel == original

@given(instance=yuml_ColorableElement_strategy)
@settings(max_examples=50)
def test_yuml_colorableelement_instantiation(instance):
    assert isinstance(instance, yuml_ColorableElement)



@given(instance=yuml_ColorableElement_strategy)
def test_yuml_colorableelement_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=yuml_ModelElement_strategy)
@settings(max_examples=50)
def test_yuml_modelelement_instantiation(instance):
    assert isinstance(instance, yuml_ModelElement)

@given(instance=yuml_Model_strategy)
@settings(max_examples=50)
def test_yuml_model_instantiation(instance):
    assert isinstance(instance, yuml_Model)

@given(instance=yuml_Method_strategy)
@settings(max_examples=50)
def test_yuml_method_instantiation(instance):
    assert isinstance(instance, yuml_Method)



@given(instance=yuml_Method_strategy)
def test_yuml_method_arguments_setter(instance):
    original = instance.arguments
    instance.arguments = original
    assert instance.arguments == original

@given(instance=yuml_Attribute_strategy)
@settings(max_examples=50)
def test_yuml_attribute_instantiation(instance):
    assert isinstance(instance, yuml_Attribute)



@given(instance=yuml_Attribute_strategy)
def test_yuml_attribute_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original



@given(instance=yuml_Attribute_strategy)
def test_yuml_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ColorableElement_strategy)
@settings(max_examples=50)
def test_colorableelement_instantiation(instance):
    assert isinstance(instance, ColorableElement)

@given(instance=yuml_Note_strategy)
@settings(max_examples=50)
def test_yuml_note_instantiation(instance):
    assert isinstance(instance, yuml_Note)



@given(instance=yuml_Note_strategy)
def test_yuml_note_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=yuml_Class_strategy)
@settings(max_examples=50)
def test_yuml_class_instantiation(instance):
    assert isinstance(instance, yuml_Class)



@given(instance=yuml_Class_strategy)
def test_yuml_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=yuml_Class_strategy)
def test_yuml_class_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original
