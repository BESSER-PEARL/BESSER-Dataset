import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MetaModelGraph::EReference,
    Relation,
    MetaModelGraph::EAttribute,
    MetaModelGraph::Relation,
    MetaModelGraph::Node,
    MetaModelGraph::EClass,
    MetaModelGraph::SubGraph,
    MetaModelGraph::Graph,
    MetaModelGraph::SubClass,
    MetaModelGraph::Reference,
    MetaModelGraph::Composition,
    EnumModular,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodelgraph::ereference_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph::EReference)


def test_metamodelgraph::ereference_constructor_exists():
    assert callable(MetaModelGraph::EReference.__init__)


def test_metamodelgraph::ereference_constructor_args():
    sig = inspect.signature(MetaModelGraph::EReference.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_metamodelgraph::eattribute_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph::EAttribute)


def test_metamodelgraph::eattribute_constructor_exists():
    assert callable(MetaModelGraph::EAttribute.__init__)


def test_metamodelgraph::eattribute_constructor_args():
    sig = inspect.signature(MetaModelGraph::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_metamodelgraph::relation_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph::Relation)


def test_metamodelgraph::relation_constructor_exists():
    assert callable(MetaModelGraph::Relation.__init__)


def test_metamodelgraph::relation_constructor_args():
    sig = inspect.signature(MetaModelGraph::Relation.__init__)
    params = list(sig.parameters.keys())



def test_metamodelgraph::node_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph::Node)


def test_metamodelgraph::node_constructor_exists():
    assert callable(MetaModelGraph::Node.__init__)


def test_metamodelgraph::node_constructor_args():
    sig = inspect.signature(MetaModelGraph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "insideRecursion" in params, "Missing parameter 'insideRecursion'"
    assert "enumModularNotation" in params, "Missing parameter 'enumModularNotation'"

def test_metamodelgraph::node_has_extension():
    assert hasattr(MetaModelGraph::Node, "extension")
    descriptor = None
    for klass in MetaModelGraph::Node.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::node_has_icon():
    assert hasattr(MetaModelGraph::Node, "icon")
    descriptor = None
    for klass in MetaModelGraph::Node.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::node_has_insideRecursion():
    assert hasattr(MetaModelGraph::Node, "insideRecursion")
    descriptor = None
    for klass in MetaModelGraph::Node.__mro__:
        if "insideRecursion" in klass.__dict__:
            descriptor = klass.__dict__["insideRecursion"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::node_has_enumModularNotation():
    assert hasattr(MetaModelGraph::Node, "enumModularNotation")
    descriptor = None
    for klass in MetaModelGraph::Node.__mro__:
        if "enumModularNotation" in klass.__dict__:
            descriptor = klass.__dict__["enumModularNotation"]
            break
    assert isinstance(descriptor, property)



def test_metamodelgraph::eclass_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph::EClass)


def test_metamodelgraph::eclass_constructor_exists():
    assert callable(MetaModelGraph::EClass.__init__)


def test_metamodelgraph::eclass_constructor_args():
    sig = inspect.signature(MetaModelGraph::EClass.__init__)
    params = list(sig.parameters.keys())



def test_metamodelgraph::subgraph_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph::SubGraph)


def test_metamodelgraph::subgraph_constructor_exists():
    assert callable(MetaModelGraph::SubGraph.__init__)


def test_metamodelgraph::subgraph_constructor_args():
    sig = inspect.signature(MetaModelGraph::SubGraph.__init__)
    params = list(sig.parameters.keys())
    assert "amountOfParentEClass" in params, "Missing parameter 'amountOfParentEClass'"
    assert "amountOfRecursionPackages" in params, "Missing parameter 'amountOfRecursionPackages'"
    assert "amountUnits" in params, "Missing parameter 'amountUnits'"
    assert "amountEClassesOut" in params, "Missing parameter 'amountEClassesOut'"
    assert "amountOfConcreteEClass" in params, "Missing parameter 'amountOfConcreteEClass'"
    assert "amountOfParentAbstractEClass" in params, "Missing parameter 'amountOfParentAbstractEClass'"
    assert "amountOfAbstractEClass" in params, "Missing parameter 'amountOfAbstractEClass'"
    assert "amountPackages" in params, "Missing parameter 'amountPackages'"
    assert "amountRecursionUnits" in params, "Missing parameter 'amountRecursionUnits'"
    assert "height" in params, "Missing parameter 'height'"

def test_metamodelgraph::subgraph_has_amountOfParentEClass():
    assert hasattr(MetaModelGraph::SubGraph, "amountOfParentEClass")
    descriptor = None
    for klass in MetaModelGraph::SubGraph.__mro__:
        if "amountOfParentEClass" in klass.__dict__:
            descriptor = klass.__dict__["amountOfParentEClass"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::subgraph_has_amountOfRecursionPackages():
    assert hasattr(MetaModelGraph::SubGraph, "amountOfRecursionPackages")
    descriptor = None
    for klass in MetaModelGraph::SubGraph.__mro__:
        if "amountOfRecursionPackages" in klass.__dict__:
            descriptor = klass.__dict__["amountOfRecursionPackages"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::subgraph_has_amountUnits():
    assert hasattr(MetaModelGraph::SubGraph, "amountUnits")
    descriptor = None
    for klass in MetaModelGraph::SubGraph.__mro__:
        if "amountUnits" in klass.__dict__:
            descriptor = klass.__dict__["amountUnits"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::subgraph_has_amountEClassesOut():
    assert hasattr(MetaModelGraph::SubGraph, "amountEClassesOut")
    descriptor = None
    for klass in MetaModelGraph::SubGraph.__mro__:
        if "amountEClassesOut" in klass.__dict__:
            descriptor = klass.__dict__["amountEClassesOut"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::subgraph_has_amountOfConcreteEClass():
    assert hasattr(MetaModelGraph::SubGraph, "amountOfConcreteEClass")
    descriptor = None
    for klass in MetaModelGraph::SubGraph.__mro__:
        if "amountOfConcreteEClass" in klass.__dict__:
            descriptor = klass.__dict__["amountOfConcreteEClass"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::subgraph_has_amountOfParentAbstractEClass():
    assert hasattr(MetaModelGraph::SubGraph, "amountOfParentAbstractEClass")
    descriptor = None
    for klass in MetaModelGraph::SubGraph.__mro__:
        if "amountOfParentAbstractEClass" in klass.__dict__:
            descriptor = klass.__dict__["amountOfParentAbstractEClass"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::subgraph_has_amountOfAbstractEClass():
    assert hasattr(MetaModelGraph::SubGraph, "amountOfAbstractEClass")
    descriptor = None
    for klass in MetaModelGraph::SubGraph.__mro__:
        if "amountOfAbstractEClass" in klass.__dict__:
            descriptor = klass.__dict__["amountOfAbstractEClass"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::subgraph_has_amountPackages():
    assert hasattr(MetaModelGraph::SubGraph, "amountPackages")
    descriptor = None
    for klass in MetaModelGraph::SubGraph.__mro__:
        if "amountPackages" in klass.__dict__:
            descriptor = klass.__dict__["amountPackages"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::subgraph_has_amountRecursionUnits():
    assert hasattr(MetaModelGraph::SubGraph, "amountRecursionUnits")
    descriptor = None
    for klass in MetaModelGraph::SubGraph.__mro__:
        if "amountRecursionUnits" in klass.__dict__:
            descriptor = klass.__dict__["amountRecursionUnits"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::subgraph_has_height():
    assert hasattr(MetaModelGraph::SubGraph, "height")
    descriptor = None
    for klass in MetaModelGraph::SubGraph.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_metamodelgraph::graph_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph::Graph)


def test_metamodelgraph::graph_constructor_exists():
    assert callable(MetaModelGraph::Graph.__init__)


def test_metamodelgraph::graph_constructor_args():
    sig = inspect.signature(MetaModelGraph::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "amountAbstractEClasses" in params, "Missing parameter 'amountAbstractEClasses'"
    assert "amountConcreteEClass" in params, "Missing parameter 'amountConcreteEClass'"
    assert "amountEClasses" in params, "Missing parameter 'amountEClasses'"

def test_metamodelgraph::graph_has_amountAbstractEClasses():
    assert hasattr(MetaModelGraph::Graph, "amountAbstractEClasses")
    descriptor = None
    for klass in MetaModelGraph::Graph.__mro__:
        if "amountAbstractEClasses" in klass.__dict__:
            descriptor = klass.__dict__["amountAbstractEClasses"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::graph_has_amountConcreteEClass():
    assert hasattr(MetaModelGraph::Graph, "amountConcreteEClass")
    descriptor = None
    for klass in MetaModelGraph::Graph.__mro__:
        if "amountConcreteEClass" in klass.__dict__:
            descriptor = klass.__dict__["amountConcreteEClass"]
            break
    assert isinstance(descriptor, property)

def test_metamodelgraph::graph_has_amountEClasses():
    assert hasattr(MetaModelGraph::Graph, "amountEClasses")
    descriptor = None
    for klass in MetaModelGraph::Graph.__mro__:
        if "amountEClasses" in klass.__dict__:
            descriptor = klass.__dict__["amountEClasses"]
            break
    assert isinstance(descriptor, property)



def test_metamodelgraph::subclass_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph::SubClass)


def test_metamodelgraph::subclass_constructor_exists():
    assert callable(MetaModelGraph::SubClass.__init__)


def test_metamodelgraph::subclass_constructor_args():
    sig = inspect.signature(MetaModelGraph::SubClass.__init__)
    params = list(sig.parameters.keys())



def test_metamodelgraph::reference_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph::Reference)


def test_metamodelgraph::reference_constructor_exists():
    assert callable(MetaModelGraph::Reference.__init__)


def test_metamodelgraph::reference_constructor_args():
    sig = inspect.signature(MetaModelGraph::Reference.__init__)
    params = list(sig.parameters.keys())



def test_metamodelgraph::composition_is_not_abstract():
    assert not inspect.isabstract(MetaModelGraph::Composition)


def test_metamodelgraph::composition_constructor_exists():
    assert callable(MetaModelGraph::Composition.__init__)


def test_metamodelgraph::composition_constructor_args():
    sig = inspect.signature(MetaModelGraph::Composition.__init__)
    params = list(sig.parameters.keys())

def test_enummodular_exists():
    # Check that the Enumeration exists
    assert EnumModular is not None

def test_enummodular_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnumModular]
    expected_literals = [
        "Default",
        "RecursionAbstractPackage",
        "InsideUnit",
        "RecursionAbstractUnit",
        "Unit",
        "AbstractPackageUnit",
        "AbstractPackage",
        "AbstractUnit",
        "Project",
        "RecursionPackage",
        "InsidePackage",
        "RecursionUnit",
        "Package",
        "InsideProject",
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
MetaModelGraph::EReference_strategy = st.builds(
    MetaModelGraph::EReference,
)
Relation_strategy = st.builds(
    Relation,
)
MetaModelGraph::EAttribute_strategy = st.builds(
    MetaModelGraph::EAttribute,
)
MetaModelGraph::Relation_strategy = st.builds(
    MetaModelGraph::Relation,
)
MetaModelGraph::Node_strategy = st.builds(
    MetaModelGraph::Node,
    extension=
        safe_text,
    icon=
        safe_text,
    insideRecursion=
        st.booleans(),
    enumModularNotation=
        safe_text
)
MetaModelGraph::EClass_strategy = st.builds(
    MetaModelGraph::EClass,
)
MetaModelGraph::SubGraph_strategy = st.builds(
    MetaModelGraph::SubGraph,
    amountOfParentEClass=
        st.integers(),
    amountOfRecursionPackages=
        st.integers(),
    amountUnits=
        st.integers(),
    amountEClassesOut=
        st.integers(),
    amountOfConcreteEClass=
        st.integers(),
    amountOfParentAbstractEClass=
        st.integers(),
    amountOfAbstractEClass=
        st.integers(),
    amountPackages=
        st.integers(),
    amountRecursionUnits=
        st.integers(),
    height=
        st.integers()
)
MetaModelGraph::Graph_strategy = st.builds(
    MetaModelGraph::Graph,
    amountAbstractEClasses=
        st.integers(),
    amountConcreteEClass=
        st.integers(),
    amountEClasses=
        st.integers()
)
MetaModelGraph::SubClass_strategy = st.builds(
    MetaModelGraph::SubClass,
)
MetaModelGraph::Reference_strategy = st.builds(
    MetaModelGraph::Reference,
)
MetaModelGraph::Composition_strategy = st.builds(
    MetaModelGraph::Composition,
)

@given(instance=MetaModelGraph::EReference_strategy)
@settings(max_examples=50)
def test_metamodelgraph::ereference_instantiation(instance):
    assert isinstance(instance, MetaModelGraph::EReference)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=MetaModelGraph::EAttribute_strategy)
@settings(max_examples=50)
def test_metamodelgraph::eattribute_instantiation(instance):
    assert isinstance(instance, MetaModelGraph::EAttribute)

@given(instance=MetaModelGraph::Relation_strategy)
@settings(max_examples=50)
def test_metamodelgraph::relation_instantiation(instance):
    assert isinstance(instance, MetaModelGraph::Relation)

@given(instance=MetaModelGraph::Node_strategy)
@settings(max_examples=50)
def test_metamodelgraph::node_instantiation(instance):
    assert isinstance(instance, MetaModelGraph::Node)

@given(instance=MetaModelGraph::Node_strategy)
def test_metamodelgraph::node_extension_type(instance):
    assert isinstance(instance.extension, str)


@given(instance=MetaModelGraph::Node_strategy)
def test_metamodelgraph::node_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original

@given(instance=MetaModelGraph::Node_strategy)
def test_metamodelgraph::node_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=MetaModelGraph::Node_strategy)
def test_metamodelgraph::node_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=MetaModelGraph::Node_strategy)
def test_metamodelgraph::node_insideRecursion_type(instance):
    assert isinstance(instance.insideRecursion, bool)


@given(instance=MetaModelGraph::Node_strategy)
def test_metamodelgraph::node_insideRecursion_setter(instance):
    original = instance.insideRecursion
    instance.insideRecursion = original
    assert instance.insideRecursion == original

@given(instance=MetaModelGraph::Node_strategy)
def test_metamodelgraph::node_enumModularNotation_type(instance):
    assert isinstance(instance.enumModularNotation, str)


@given(instance=MetaModelGraph::Node_strategy)
def test_metamodelgraph::node_enumModularNotation_setter(instance):
    original = instance.enumModularNotation
    instance.enumModularNotation = original
    assert instance.enumModularNotation == original

@given(instance=MetaModelGraph::EClass_strategy)
@settings(max_examples=50)
def test_metamodelgraph::eclass_instantiation(instance):
    assert isinstance(instance, MetaModelGraph::EClass)

@given(instance=MetaModelGraph::SubGraph_strategy)
@settings(max_examples=50)
def test_metamodelgraph::subgraph_instantiation(instance):
    assert isinstance(instance, MetaModelGraph::SubGraph)

@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountOfParentEClass_type(instance):
    assert isinstance(instance.amountOfParentEClass, int)


@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountOfParentEClass_setter(instance):
    original = instance.amountOfParentEClass
    instance.amountOfParentEClass = original
    assert instance.amountOfParentEClass == original

@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountOfRecursionPackages_type(instance):
    assert isinstance(instance.amountOfRecursionPackages, int)


@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountOfRecursionPackages_setter(instance):
    original = instance.amountOfRecursionPackages
    instance.amountOfRecursionPackages = original
    assert instance.amountOfRecursionPackages == original

@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountUnits_type(instance):
    assert isinstance(instance.amountUnits, int)


@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountUnits_setter(instance):
    original = instance.amountUnits
    instance.amountUnits = original
    assert instance.amountUnits == original

@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountEClassesOut_type(instance):
    assert isinstance(instance.amountEClassesOut, int)


@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountEClassesOut_setter(instance):
    original = instance.amountEClassesOut
    instance.amountEClassesOut = original
    assert instance.amountEClassesOut == original

@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountOfConcreteEClass_type(instance):
    assert isinstance(instance.amountOfConcreteEClass, int)


@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountOfConcreteEClass_setter(instance):
    original = instance.amountOfConcreteEClass
    instance.amountOfConcreteEClass = original
    assert instance.amountOfConcreteEClass == original

@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountOfParentAbstractEClass_type(instance):
    assert isinstance(instance.amountOfParentAbstractEClass, int)


@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountOfParentAbstractEClass_setter(instance):
    original = instance.amountOfParentAbstractEClass
    instance.amountOfParentAbstractEClass = original
    assert instance.amountOfParentAbstractEClass == original

@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountOfAbstractEClass_type(instance):
    assert isinstance(instance.amountOfAbstractEClass, int)


@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountOfAbstractEClass_setter(instance):
    original = instance.amountOfAbstractEClass
    instance.amountOfAbstractEClass = original
    assert instance.amountOfAbstractEClass == original

@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountPackages_type(instance):
    assert isinstance(instance.amountPackages, int)


@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountPackages_setter(instance):
    original = instance.amountPackages
    instance.amountPackages = original
    assert instance.amountPackages == original

@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountRecursionUnits_type(instance):
    assert isinstance(instance.amountRecursionUnits, int)


@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_amountRecursionUnits_setter(instance):
    original = instance.amountRecursionUnits
    instance.amountRecursionUnits = original
    assert instance.amountRecursionUnits == original

@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=MetaModelGraph::SubGraph_strategy)
def test_metamodelgraph::subgraph_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=MetaModelGraph::Graph_strategy)
@settings(max_examples=50)
def test_metamodelgraph::graph_instantiation(instance):
    assert isinstance(instance, MetaModelGraph::Graph)

@given(instance=MetaModelGraph::Graph_strategy)
def test_metamodelgraph::graph_amountAbstractEClasses_type(instance):
    assert isinstance(instance.amountAbstractEClasses, int)


@given(instance=MetaModelGraph::Graph_strategy)
def test_metamodelgraph::graph_amountAbstractEClasses_setter(instance):
    original = instance.amountAbstractEClasses
    instance.amountAbstractEClasses = original
    assert instance.amountAbstractEClasses == original

@given(instance=MetaModelGraph::Graph_strategy)
def test_metamodelgraph::graph_amountConcreteEClass_type(instance):
    assert isinstance(instance.amountConcreteEClass, int)


@given(instance=MetaModelGraph::Graph_strategy)
def test_metamodelgraph::graph_amountConcreteEClass_setter(instance):
    original = instance.amountConcreteEClass
    instance.amountConcreteEClass = original
    assert instance.amountConcreteEClass == original

@given(instance=MetaModelGraph::Graph_strategy)
def test_metamodelgraph::graph_amountEClasses_type(instance):
    assert isinstance(instance.amountEClasses, int)


@given(instance=MetaModelGraph::Graph_strategy)
def test_metamodelgraph::graph_amountEClasses_setter(instance):
    original = instance.amountEClasses
    instance.amountEClasses = original
    assert instance.amountEClasses == original

@given(instance=MetaModelGraph::SubClass_strategy)
@settings(max_examples=50)
def test_metamodelgraph::subclass_instantiation(instance):
    assert isinstance(instance, MetaModelGraph::SubClass)

@given(instance=MetaModelGraph::Reference_strategy)
@settings(max_examples=50)
def test_metamodelgraph::reference_instantiation(instance):
    assert isinstance(instance, MetaModelGraph::Reference)

@given(instance=MetaModelGraph::Composition_strategy)
@settings(max_examples=50)
def test_metamodelgraph::composition_instantiation(instance):
    assert isinstance(instance, MetaModelGraph::Composition)
