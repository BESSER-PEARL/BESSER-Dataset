import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MetaModelGraph_EReference,
    Relation,
    MetaModelGraph_EAttribute,
    MetaModelGraph_Relation,
    MetaModelGraph_Node,
    MetaModelGraph_EClass,
    MetaModelGraph_SubGraph,
    MetaModelGraph_Graph,
    MetaModelGraph_SubClass,
    MetaModelGraph_Reference,
    MetaModelGraph_Composition,
    EnumModular,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodelgraph_ereference_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph_EReference)


def test_metamodelgraph_ereference_constructor_exists():
    assert callable(MetaModelGraph_EReference.__init__)


def test_metamodelgraph_ereference_constructor_args():
    sig = inspect.signature(MetaModelGraph_EReference.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_metamodelgraph_eattribute_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph_EAttribute)


def test_metamodelgraph_eattribute_constructor_exists():
    assert callable(MetaModelGraph_EAttribute.__init__)


def test_metamodelgraph_eattribute_constructor_args():
    sig = inspect.signature(MetaModelGraph_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_metamodelgraph_relation_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph_Relation)


def test_metamodelgraph_relation_constructor_exists():
    assert callable(MetaModelGraph_Relation.__init__)


def test_metamodelgraph_relation_constructor_args():
    sig = inspect.signature(MetaModelGraph_Relation.__init__)
    params = list(sig.parameters.keys())



def test_metamodelgraph_node_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph_Node)


def test_metamodelgraph_node_constructor_exists():
    assert callable(MetaModelGraph_Node.__init__)


def test_metamodelgraph_node_constructor_args():
    sig = inspect.signature(MetaModelGraph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"
    assert "insideRecursion" in params, "Missing parameter 'insideRecursion'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "enumModularNotation" in params, "Missing parameter 'enumModularNotation'"

def test_metamodelgraph_node_has_extension():
    assert hasattr(MetaModelGraph_Node, "extension")
    descriptor = None
    for klass in MetaModelGraph_Node.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_node_has_insideRecursion():
    assert hasattr(MetaModelGraph_Node, "insideRecursion")
    descriptor = None
    for klass in MetaModelGraph_Node.__mro__:
        if "insideRecursion" in klass.__dict__:
            descriptor = klass.__dict__["insideRecursion"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_node_has_icon():
    assert hasattr(MetaModelGraph_Node, "icon")
    descriptor = None
    for klass in MetaModelGraph_Node.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_node_has_enumModularNotation():
    assert hasattr(MetaModelGraph_Node, "enumModularNotation")
    descriptor = None
    for klass in MetaModelGraph_Node.__mro__:
        if "enumModularNotation" in klass.__dict__:
            descriptor = klass.__dict__["enumModularNotation"]
            break
    assert isinstance(descriptor, property)



def test_metamodelgraph_eclass_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph_EClass)


def test_metamodelgraph_eclass_constructor_exists():
    assert callable(MetaModelGraph_EClass.__init__)


def test_metamodelgraph_eclass_constructor_args():
    sig = inspect.signature(MetaModelGraph_EClass.__init__)
    params = list(sig.parameters.keys())



def test_metamodelgraph_subgraph_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph_SubGraph)


def test_metamodelgraph_subgraph_constructor_exists():
    assert callable(MetaModelGraph_SubGraph.__init__)


def test_metamodelgraph_subgraph_constructor_args():
    sig = inspect.signature(MetaModelGraph_SubGraph.__init__)
    params = list(sig.parameters.keys())
    assert "amountRecursionUnits" in params, "Missing parameter 'amountRecursionUnits'"
    assert "amountEClassesOut" in params, "Missing parameter 'amountEClassesOut'"
    assert "height" in params, "Missing parameter 'height'"
    assert "amountOfConcreteEClass" in params, "Missing parameter 'amountOfConcreteEClass'"
    assert "amountOfAbstractEClass" in params, "Missing parameter 'amountOfAbstractEClass'"
    assert "amountOfParentEClass" in params, "Missing parameter 'amountOfParentEClass'"
    assert "amountOfRecursionPackages" in params, "Missing parameter 'amountOfRecursionPackages'"
    assert "amountPackages" in params, "Missing parameter 'amountPackages'"
    assert "amountUnits" in params, "Missing parameter 'amountUnits'"
    assert "amountOfParentAbstractEClass" in params, "Missing parameter 'amountOfParentAbstractEClass'"

def test_metamodelgraph_subgraph_has_amountRecursionUnits():
    assert hasattr(MetaModelGraph_SubGraph, "amountRecursionUnits")
    descriptor = None
    for klass in MetaModelGraph_SubGraph.__mro__:
        if "amountRecursionUnits" in klass.__dict__:
            descriptor = klass.__dict__["amountRecursionUnits"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_subgraph_has_amountEClassesOut():
    assert hasattr(MetaModelGraph_SubGraph, "amountEClassesOut")
    descriptor = None
    for klass in MetaModelGraph_SubGraph.__mro__:
        if "amountEClassesOut" in klass.__dict__:
            descriptor = klass.__dict__["amountEClassesOut"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_subgraph_has_height():
    assert hasattr(MetaModelGraph_SubGraph, "height")
    descriptor = None
    for klass in MetaModelGraph_SubGraph.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_subgraph_has_amountOfConcreteEClass():
    assert hasattr(MetaModelGraph_SubGraph, "amountOfConcreteEClass")
    descriptor = None
    for klass in MetaModelGraph_SubGraph.__mro__:
        if "amountOfConcreteEClass" in klass.__dict__:
            descriptor = klass.__dict__["amountOfConcreteEClass"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_subgraph_has_amountOfAbstractEClass():
    assert hasattr(MetaModelGraph_SubGraph, "amountOfAbstractEClass")
    descriptor = None
    for klass in MetaModelGraph_SubGraph.__mro__:
        if "amountOfAbstractEClass" in klass.__dict__:
            descriptor = klass.__dict__["amountOfAbstractEClass"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_subgraph_has_amountOfParentEClass():
    assert hasattr(MetaModelGraph_SubGraph, "amountOfParentEClass")
    descriptor = None
    for klass in MetaModelGraph_SubGraph.__mro__:
        if "amountOfParentEClass" in klass.__dict__:
            descriptor = klass.__dict__["amountOfParentEClass"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_subgraph_has_amountOfRecursionPackages():
    assert hasattr(MetaModelGraph_SubGraph, "amountOfRecursionPackages")
    descriptor = None
    for klass in MetaModelGraph_SubGraph.__mro__:
        if "amountOfRecursionPackages" in klass.__dict__:
            descriptor = klass.__dict__["amountOfRecursionPackages"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_subgraph_has_amountPackages():
    assert hasattr(MetaModelGraph_SubGraph, "amountPackages")
    descriptor = None
    for klass in MetaModelGraph_SubGraph.__mro__:
        if "amountPackages" in klass.__dict__:
            descriptor = klass.__dict__["amountPackages"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_subgraph_has_amountUnits():
    assert hasattr(MetaModelGraph_SubGraph, "amountUnits")
    descriptor = None
    for klass in MetaModelGraph_SubGraph.__mro__:
        if "amountUnits" in klass.__dict__:
            descriptor = klass.__dict__["amountUnits"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_subgraph_has_amountOfParentAbstractEClass():
    assert hasattr(MetaModelGraph_SubGraph, "amountOfParentAbstractEClass")
    descriptor = None
    for klass in MetaModelGraph_SubGraph.__mro__:
        if "amountOfParentAbstractEClass" in klass.__dict__:
            descriptor = klass.__dict__["amountOfParentAbstractEClass"]
            break
    assert isinstance(descriptor, property)



def test_metamodelgraph_graph_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph_Graph)


def test_metamodelgraph_graph_constructor_exists():
    assert callable(MetaModelGraph_Graph.__init__)


def test_metamodelgraph_graph_constructor_args():
    sig = inspect.signature(MetaModelGraph_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "amountConcreteEClass" in params, "Missing parameter 'amountConcreteEClass'"
    assert "amountEClasses" in params, "Missing parameter 'amountEClasses'"
    assert "amountAbstractEClasses" in params, "Missing parameter 'amountAbstractEClasses'"

def test_metamodelgraph_graph_has_amountConcreteEClass():
    assert hasattr(MetaModelGraph_Graph, "amountConcreteEClass")
    descriptor = None
    for klass in MetaModelGraph_Graph.__mro__:
        if "amountConcreteEClass" in klass.__dict__:
            descriptor = klass.__dict__["amountConcreteEClass"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_graph_has_amountEClasses():
    assert hasattr(MetaModelGraph_Graph, "amountEClasses")
    descriptor = None
    for klass in MetaModelGraph_Graph.__mro__:
        if "amountEClasses" in klass.__dict__:
            descriptor = klass.__dict__["amountEClasses"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph_graph_has_amountAbstractEClasses():
    assert hasattr(MetaModelGraph_Graph, "amountAbstractEClasses")
    descriptor = None
    for klass in MetaModelGraph_Graph.__mro__:
        if "amountAbstractEClasses" in klass.__dict__:
            descriptor = klass.__dict__["amountAbstractEClasses"]
            break
    assert isinstance(descriptor, property)



def test_metamodelgraph_subclass_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph_SubClass)


def test_metamodelgraph_subclass_constructor_exists():
    assert callable(MetaModelGraph_SubClass.__init__)


def test_metamodelgraph_subclass_constructor_args():
    sig = inspect.signature(MetaModelGraph_SubClass.__init__)
    params = list(sig.parameters.keys())



def test_metamodelgraph_reference_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph_Reference)


def test_metamodelgraph_reference_constructor_exists():
    assert callable(MetaModelGraph_Reference.__init__)


def test_metamodelgraph_reference_constructor_args():
    sig = inspect.signature(MetaModelGraph_Reference.__init__)
    params = list(sig.parameters.keys())



def test_metamodelgraph_composition_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph_Composition)


def test_metamodelgraph_composition_constructor_exists():
    assert callable(MetaModelGraph_Composition.__init__)


def test_metamodelgraph_composition_constructor_args():
    sig = inspect.signature(MetaModelGraph_Composition.__init__)
    params = list(sig.parameters.keys())

def test_enummodular_exists():
    # Check that the Enumeration exists
    assert EnumModular is not None

def test_enummodular_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnumModular]
    expected_literals = [
        "Package",
        "AbstractUnit",
        "Unit",
        "InsideProject",
        "RecursionPackage",
        "InsideUnit",
        "AbstractPackage",
        "RecursionAbstractPackage",
        "Project",
        "AbstractPackageUnit",
        "InsidePackage",
        "RecursionAbstractUnit",
        "RecursionUnit",
        "Default",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnumModular"


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
MetaModelGraph_EReference_strategy = st.builds(
    MetaModelGraph_EReference,
)
Relation_strategy = st.builds(
    Relation,
)
MetaModelGraph_EAttribute_strategy = st.builds(
    MetaModelGraph_EAttribute,
)
MetaModelGraph_Relation_strategy = st.builds(
    MetaModelGraph_Relation,
)
MetaModelGraph_Node_strategy = st.builds(
    MetaModelGraph_Node,
    extension=
        safe_text,
    insideRecursion=
        st.booleans(),
    icon=
        safe_text,
    enumModularNotation=
        safe_text
)
MetaModelGraph_EClass_strategy = st.builds(
    MetaModelGraph_EClass,
)
MetaModelGraph_SubGraph_strategy = st.builds(
    MetaModelGraph_SubGraph,
    amountRecursionUnits=
        st.integers(),
    amountEClassesOut=
        st.integers(),
    height=
        st.integers(),
    amountOfConcreteEClass=
        st.integers(),
    amountOfAbstractEClass=
        st.integers(),
    amountOfParentEClass=
        st.integers(),
    amountOfRecursionPackages=
        st.integers(),
    amountPackages=
        st.integers(),
    amountUnits=
        st.integers(),
    amountOfParentAbstractEClass=
        st.integers()
)
MetaModelGraph_Graph_strategy = st.builds(
    MetaModelGraph_Graph,
    amountConcreteEClass=
        st.integers(),
    amountEClasses=
        st.integers(),
    amountAbstractEClasses=
        st.integers()
)
MetaModelGraph_SubClass_strategy = st.builds(
    MetaModelGraph_SubClass,
)
MetaModelGraph_Reference_strategy = st.builds(
    MetaModelGraph_Reference,
)
MetaModelGraph_Composition_strategy = st.builds(
    MetaModelGraph_Composition,
)

@given(instance=MetaModelGraph_EReference_strategy)
@settings(max_examples=50)
def test_metamodelgraph_ereference_instantiation(instance):
    assert isinstance(instance, MetaModelGraph_EReference)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=MetaModelGraph_EAttribute_strategy)
@settings(max_examples=50)
def test_metamodelgraph_eattribute_instantiation(instance):
    assert isinstance(instance, MetaModelGraph_EAttribute)

@given(instance=MetaModelGraph_Relation_strategy)
@settings(max_examples=50)
def test_metamodelgraph_relation_instantiation(instance):
    assert isinstance(instance, MetaModelGraph_Relation)

@given(instance=MetaModelGraph_Node_strategy)
@settings(max_examples=50)
def test_metamodelgraph_node_instantiation(instance):
    assert isinstance(instance, MetaModelGraph_Node)



@given(instance=MetaModelGraph_Node_strategy)
def test_metamodelgraph_node_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original



@given(instance=MetaModelGraph_Node_strategy)
def test_metamodelgraph_node_insideRecursion_setter(instance):
    original = instance.insideRecursion
    instance.insideRecursion = original
    assert instance.insideRecursion == original



@given(instance=MetaModelGraph_Node_strategy)
def test_metamodelgraph_node_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=MetaModelGraph_Node_strategy)
def test_metamodelgraph_node_enumModularNotation_setter(instance):
    original = instance.enumModularNotation
    instance.enumModularNotation = original
    assert instance.enumModularNotation == original

@given(instance=MetaModelGraph_EClass_strategy)
@settings(max_examples=50)
def test_metamodelgraph_eclass_instantiation(instance):
    assert isinstance(instance, MetaModelGraph_EClass)

@given(instance=MetaModelGraph_SubGraph_strategy)
@settings(max_examples=50)
def test_metamodelgraph_subgraph_instantiation(instance):
    assert isinstance(instance, MetaModelGraph_SubGraph)



@given(instance=MetaModelGraph_SubGraph_strategy)
def test_metamodelgraph_subgraph_amountRecursionUnits_setter(instance):
    original = instance.amountRecursionUnits
    instance.amountRecursionUnits = original
    assert instance.amountRecursionUnits == original



@given(instance=MetaModelGraph_SubGraph_strategy)
def test_metamodelgraph_subgraph_amountEClassesOut_setter(instance):
    original = instance.amountEClassesOut
    instance.amountEClassesOut = original
    assert instance.amountEClassesOut == original



@given(instance=MetaModelGraph_SubGraph_strategy)
def test_metamodelgraph_subgraph_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=MetaModelGraph_SubGraph_strategy)
def test_metamodelgraph_subgraph_amountOfConcreteEClass_setter(instance):
    original = instance.amountOfConcreteEClass
    instance.amountOfConcreteEClass = original
    assert instance.amountOfConcreteEClass == original



@given(instance=MetaModelGraph_SubGraph_strategy)
def test_metamodelgraph_subgraph_amountOfAbstractEClass_setter(instance):
    original = instance.amountOfAbstractEClass
    instance.amountOfAbstractEClass = original
    assert instance.amountOfAbstractEClass == original



@given(instance=MetaModelGraph_SubGraph_strategy)
def test_metamodelgraph_subgraph_amountOfParentEClass_setter(instance):
    original = instance.amountOfParentEClass
    instance.amountOfParentEClass = original
    assert instance.amountOfParentEClass == original



@given(instance=MetaModelGraph_SubGraph_strategy)
def test_metamodelgraph_subgraph_amountOfRecursionPackages_setter(instance):
    original = instance.amountOfRecursionPackages
    instance.amountOfRecursionPackages = original
    assert instance.amountOfRecursionPackages == original



@given(instance=MetaModelGraph_SubGraph_strategy)
def test_metamodelgraph_subgraph_amountPackages_setter(instance):
    original = instance.amountPackages
    instance.amountPackages = original
    assert instance.amountPackages == original



@given(instance=MetaModelGraph_SubGraph_strategy)
def test_metamodelgraph_subgraph_amountUnits_setter(instance):
    original = instance.amountUnits
    instance.amountUnits = original
    assert instance.amountUnits == original



@given(instance=MetaModelGraph_SubGraph_strategy)
def test_metamodelgraph_subgraph_amountOfParentAbstractEClass_setter(instance):
    original = instance.amountOfParentAbstractEClass
    instance.amountOfParentAbstractEClass = original
    assert instance.amountOfParentAbstractEClass == original

@given(instance=MetaModelGraph_Graph_strategy)
@settings(max_examples=50)
def test_metamodelgraph_graph_instantiation(instance):
    assert isinstance(instance, MetaModelGraph_Graph)



@given(instance=MetaModelGraph_Graph_strategy)
def test_metamodelgraph_graph_amountConcreteEClass_setter(instance):
    original = instance.amountConcreteEClass
    instance.amountConcreteEClass = original
    assert instance.amountConcreteEClass == original



@given(instance=MetaModelGraph_Graph_strategy)
def test_metamodelgraph_graph_amountEClasses_setter(instance):
    original = instance.amountEClasses
    instance.amountEClasses = original
    assert instance.amountEClasses == original



@given(instance=MetaModelGraph_Graph_strategy)
def test_metamodelgraph_graph_amountAbstractEClasses_setter(instance):
    original = instance.amountAbstractEClasses
    instance.amountAbstractEClasses = original
    assert instance.amountAbstractEClasses == original

@given(instance=MetaModelGraph_SubClass_strategy)
@settings(max_examples=50)
def test_metamodelgraph_subclass_instantiation(instance):
    assert isinstance(instance, MetaModelGraph_SubClass)

@given(instance=MetaModelGraph_Reference_strategy)
@settings(max_examples=50)
def test_metamodelgraph_reference_instantiation(instance):
    assert isinstance(instance, MetaModelGraph_Reference)

@given(instance=MetaModelGraph_Composition_strategy)
@settings(max_examples=50)
def test_metamodelgraph_composition_instantiation(instance):
    assert isinstance(instance, MetaModelGraph_Composition)
