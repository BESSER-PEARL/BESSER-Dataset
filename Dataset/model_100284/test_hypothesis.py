import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    org_k1s_nppn::Pragmatic,
    nppn::TransitionNode,
    TransitionNode,
    org_k1s_nppn::Transition,
    org_k1s_nppn::RefTrans,
    nppn::Place,
    nppn::RefPlace,
    PlaceNode,
    org_k1s_nppn::RefPlace,
    org_k1s_nppn::Place,
    nppn::Monitor,
    nppn::Object,
    nppn::PetriNet,
    HasName,
    HasLabel,
    org_k1s_nppn::PetriNet,
    org_k1s_nppn::Page,
    org_k1s_nppn::Label,
    nppn::Pragmatic,
    nppn::Arc,
    Object,
    org_k1s_nppn::Node,
    HLAnnotation,
    org_k1s_nppn::Name,
    nppn::HasLabel,
    nppn::HLAnnotation,
    org_k1s_nppn::HLArcAddin,
    Node,
    org_k1s_nppn::PlaceNode,
    org_k1s_nppn::TransitionNode,
    org_k1s_nppn::HLAnnotation,
    org_k1s_nppn::Instance,
    nppn::Page,
    nppn::Name,
    org_k1s_nppn::HasName,
    nppn::Label,
    org_k1s_nppn::HasLabel,
    nppn::Node,
    HLArcAddin,
    HasGraphics,
    org_k1s_nppn::Object,
    org_k1s_nppn::Arc,
    nppn::Binding,
    org_k1s_nppn::Bindings,
    Container,
    org_k1s_nppn::Conditional,
    org_k1s_nppn::Conditinoal,
    org_k1s_nppn::Loop,
    Block,
    org_k1s_nppn::Atomic,
    org_k1s_nppn::Binding,
    org_k1s_nppn::Container,
    nppn::Transition,
    nppn::PlaceNode,
    org_k1s_nppn::Block,
    nppn::Block,
    org_k1s_nppn::Service,
    nppn::Service,
    nppn::Instance,
    org_k1s_nppn::Principal,
    org_k1s_nppn::PlacementConstraints,
    nppn::Principal,
    org_k1s_nppn::AbstractTemplateTree,
    Explicit,
    CustomPragmatics,
    org_k1s_nppn::CustomExplicitPragmatics,
    Derived,
    org_k1s_nppn::CustomDerivedPragmatics,
    nppn::PlacementConstraints,
    org_k1s_nppn::PNPattern,
    nppn::PNPattern,
    Pragmatic,
    org_k1s_nppn::CustomPragmatics,
    org_k1s_nppn::Derived,
    org_k1s_nppn::Explicit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_org_k1s_nppn::pragmatic_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Pragmatic)


def test_org_k1s_nppn::pragmatic_constructor_exists():
    assert callable(org_k1s_nppn::Pragmatic.__init__)


def test_org_k1s_nppn::pragmatic_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Pragmatic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_org_k1s_nppn::pragmatic_has_name():
    assert hasattr(org_k1s_nppn::Pragmatic, "name")
    descriptor = None
    for klass in org_k1s_nppn::Pragmatic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nppn::transitionnode_is_not_abstract():
    assert not inspect.isabstract(nppn::TransitionNode)


def test_nppn::transitionnode_constructor_exists():
    assert callable(nppn::TransitionNode.__init__)


def test_nppn::transitionnode_constructor_args():
    sig = inspect.signature(nppn::TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_transitionnode_is_not_abstract():
    assert not inspect.isabstract(TransitionNode)


def test_transitionnode_constructor_exists():
    assert callable(TransitionNode.__init__)


def test_transitionnode_constructor_args():
    sig = inspect.signature(TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::transition_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Transition)


def test_org_k1s_nppn::transition_constructor_exists():
    assert callable(org_k1s_nppn::Transition.__init__)


def test_org_k1s_nppn::transition_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Transition.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::reftrans_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::RefTrans)


def test_org_k1s_nppn::reftrans_constructor_exists():
    assert callable(org_k1s_nppn::RefTrans.__init__)


def test_org_k1s_nppn::reftrans_constructor_args():
    sig = inspect.signature(org_k1s_nppn::RefTrans.__init__)
    params = list(sig.parameters.keys())



def test_nppn::place_is_not_abstract():
    assert not inspect.isabstract(nppn::Place)


def test_nppn::place_constructor_exists():
    assert callable(nppn::Place.__init__)


def test_nppn::place_constructor_args():
    sig = inspect.signature(nppn::Place.__init__)
    params = list(sig.parameters.keys())



def test_nppn::refplace_is_not_abstract():
    assert not inspect.isabstract(nppn::RefPlace)


def test_nppn::refplace_constructor_exists():
    assert callable(nppn::RefPlace.__init__)


def test_nppn::refplace_constructor_args():
    sig = inspect.signature(nppn::RefPlace.__init__)
    params = list(sig.parameters.keys())



def test_placenode_is_not_abstract():
    assert not inspect.isabstract(PlaceNode)


def test_placenode_constructor_exists():
    assert callable(PlaceNode.__init__)


def test_placenode_constructor_args():
    sig = inspect.signature(PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::refplace_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::RefPlace)


def test_org_k1s_nppn::refplace_constructor_exists():
    assert callable(org_k1s_nppn::RefPlace.__init__)


def test_org_k1s_nppn::refplace_constructor_args():
    sig = inspect.signature(org_k1s_nppn::RefPlace.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::place_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Place)


def test_org_k1s_nppn::place_constructor_exists():
    assert callable(org_k1s_nppn::Place.__init__)


def test_org_k1s_nppn::place_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Place.__init__)
    params = list(sig.parameters.keys())



def test_nppn::monitor_is_not_abstract():
    assert not inspect.isabstract(nppn::Monitor)


def test_nppn::monitor_constructor_exists():
    assert callable(nppn::Monitor.__init__)


def test_nppn::monitor_constructor_args():
    sig = inspect.signature(nppn::Monitor.__init__)
    params = list(sig.parameters.keys())



def test_nppn::object_is_not_abstract():
    assert not inspect.isabstract(nppn::Object)


def test_nppn::object_constructor_exists():
    assert callable(nppn::Object.__init__)


def test_nppn::object_constructor_args():
    sig = inspect.signature(nppn::Object.__init__)
    params = list(sig.parameters.keys())



def test_nppn::petrinet_is_not_abstract():
    assert not inspect.isabstract(nppn::PetriNet)


def test_nppn::petrinet_constructor_exists():
    assert callable(nppn::PetriNet.__init__)


def test_nppn::petrinet_constructor_args():
    sig = inspect.signature(nppn::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_hasname_is_not_abstract():
    assert not inspect.isabstract(HasName)


def test_hasname_constructor_exists():
    assert callable(HasName.__init__)


def test_hasname_constructor_args():
    sig = inspect.signature(HasName.__init__)
    params = list(sig.parameters.keys())



def test_haslabel_is_not_abstract():
    assert not inspect.isabstract(HasLabel)


def test_haslabel_constructor_exists():
    assert callable(HasLabel.__init__)


def test_haslabel_constructor_args():
    sig = inspect.signature(HasLabel.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::petrinet_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::PetriNet)


def test_org_k1s_nppn::petrinet_constructor_exists():
    assert callable(org_k1s_nppn::PetriNet.__init__)


def test_org_k1s_nppn::petrinet_constructor_args():
    sig = inspect.signature(org_k1s_nppn::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "timeType" in params, "Missing parameter 'timeType'"

def test_org_k1s_nppn::petrinet_has_kind():
    assert hasattr(org_k1s_nppn::PetriNet, "kind")
    descriptor = None
    for klass in org_k1s_nppn::PetriNet.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_org_k1s_nppn::petrinet_has_timeType():
    assert hasattr(org_k1s_nppn::PetriNet, "timeType")
    descriptor = None
    for klass in org_k1s_nppn::PetriNet.__mro__:
        if "timeType" in klass.__dict__:
            descriptor = klass.__dict__["timeType"]
            break
    assert isinstance(descriptor, property)



def test_org_k1s_nppn::page_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Page)


def test_org_k1s_nppn::page_constructor_exists():
    assert callable(org_k1s_nppn::Page.__init__)


def test_org_k1s_nppn::page_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Page.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::label_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Label)


def test_org_k1s_nppn::label_constructor_exists():
    assert callable(org_k1s_nppn::Label.__init__)


def test_org_k1s_nppn::label_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Label.__init__)
    params = list(sig.parameters.keys())



def test_nppn::pragmatic_is_not_abstract():
    assert not inspect.isabstract(nppn::Pragmatic)


def test_nppn::pragmatic_constructor_exists():
    assert callable(nppn::Pragmatic.__init__)


def test_nppn::pragmatic_constructor_args():
    sig = inspect.signature(nppn::Pragmatic.__init__)
    params = list(sig.parameters.keys())



def test_nppn::arc_is_not_abstract():
    assert not inspect.isabstract(nppn::Arc)


def test_nppn::arc_constructor_exists():
    assert callable(nppn::Arc.__init__)


def test_nppn::arc_constructor_args():
    sig = inspect.signature(nppn::Arc.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::node_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Node)


def test_org_k1s_nppn::node_constructor_exists():
    assert callable(org_k1s_nppn::Node.__init__)


def test_org_k1s_nppn::node_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Node.__init__)
    params = list(sig.parameters.keys())



def test_hlannotation_is_not_abstract():
    assert not inspect.isabstract(HLAnnotation)


def test_hlannotation_constructor_exists():
    assert callable(HLAnnotation.__init__)


def test_hlannotation_constructor_args():
    sig = inspect.signature(HLAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::name_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Name)


def test_org_k1s_nppn::name_constructor_exists():
    assert callable(org_k1s_nppn::Name.__init__)


def test_org_k1s_nppn::name_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Name.__init__)
    params = list(sig.parameters.keys())



def test_nppn::haslabel_is_not_abstract():
    assert not inspect.isabstract(nppn::HasLabel)


def test_nppn::haslabel_constructor_exists():
    assert callable(nppn::HasLabel.__init__)


def test_nppn::haslabel_constructor_args():
    sig = inspect.signature(nppn::HasLabel.__init__)
    params = list(sig.parameters.keys())



def test_nppn::hlannotation_is_not_abstract():
    assert not inspect.isabstract(nppn::HLAnnotation)


def test_nppn::hlannotation_constructor_exists():
    assert callable(nppn::HLAnnotation.__init__)


def test_nppn::hlannotation_constructor_args():
    sig = inspect.signature(nppn::HLAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::hlarcaddin_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::HLArcAddin)


def test_org_k1s_nppn::hlarcaddin_constructor_exists():
    assert callable(org_k1s_nppn::HLArcAddin.__init__)


def test_org_k1s_nppn::hlarcaddin_constructor_args():
    sig = inspect.signature(org_k1s_nppn::HLArcAddin.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_org_k1s_nppn::hlarcaddin_has_kind():
    assert hasattr(org_k1s_nppn::HLArcAddin, "kind")
    descriptor = None
    for klass in org_k1s_nppn::HLArcAddin.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::placenode_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::PlaceNode)


def test_org_k1s_nppn::placenode_constructor_exists():
    assert callable(org_k1s_nppn::PlaceNode.__init__)


def test_org_k1s_nppn::placenode_constructor_args():
    sig = inspect.signature(org_k1s_nppn::PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::transitionnode_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::TransitionNode)


def test_org_k1s_nppn::transitionnode_constructor_exists():
    assert callable(org_k1s_nppn::TransitionNode.__init__)


def test_org_k1s_nppn::transitionnode_constructor_args():
    sig = inspect.signature(org_k1s_nppn::TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::hlannotation_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::HLAnnotation)


def test_org_k1s_nppn::hlannotation_constructor_exists():
    assert callable(org_k1s_nppn::HLAnnotation.__init__)


def test_org_k1s_nppn::hlannotation_constructor_args():
    sig = inspect.signature(org_k1s_nppn::HLAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::instance_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Instance)


def test_org_k1s_nppn::instance_constructor_exists():
    assert callable(org_k1s_nppn::Instance.__init__)


def test_org_k1s_nppn::instance_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Instance.__init__)
    params = list(sig.parameters.keys())
    assert "subPageID" in params, "Missing parameter 'subPageID'"

def test_org_k1s_nppn::instance_has_subPageID():
    assert hasattr(org_k1s_nppn::Instance, "subPageID")
    descriptor = None
    for klass in org_k1s_nppn::Instance.__mro__:
        if "subPageID" in klass.__dict__:
            descriptor = klass.__dict__["subPageID"]
            break
    assert isinstance(descriptor, property)



def test_nppn::page_is_not_abstract():
    assert not inspect.isabstract(nppn::Page)


def test_nppn::page_constructor_exists():
    assert callable(nppn::Page.__init__)


def test_nppn::page_constructor_args():
    sig = inspect.signature(nppn::Page.__init__)
    params = list(sig.parameters.keys())



def test_nppn::name_is_not_abstract():
    assert not inspect.isabstract(nppn::Name)


def test_nppn::name_constructor_exists():
    assert callable(nppn::Name.__init__)


def test_nppn::name_constructor_args():
    sig = inspect.signature(nppn::Name.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::hasname_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::HasName)


def test_org_k1s_nppn::hasname_constructor_exists():
    assert callable(org_k1s_nppn::HasName.__init__)


def test_org_k1s_nppn::hasname_constructor_args():
    sig = inspect.signature(org_k1s_nppn::HasName.__init__)
    params = list(sig.parameters.keys())



def test_nppn::label_is_not_abstract():
    assert not inspect.isabstract(nppn::Label)


def test_nppn::label_constructor_exists():
    assert callable(nppn::Label.__init__)


def test_nppn::label_constructor_args():
    sig = inspect.signature(nppn::Label.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::haslabel_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::HasLabel)


def test_org_k1s_nppn::haslabel_constructor_exists():
    assert callable(org_k1s_nppn::HasLabel.__init__)


def test_org_k1s_nppn::haslabel_constructor_args():
    sig = inspect.signature(org_k1s_nppn::HasLabel.__init__)
    params = list(sig.parameters.keys())



def test_nppn::node_is_not_abstract():
    assert not inspect.isabstract(nppn::Node)


def test_nppn::node_constructor_exists():
    assert callable(nppn::Node.__init__)


def test_nppn::node_constructor_args():
    sig = inspect.signature(nppn::Node.__init__)
    params = list(sig.parameters.keys())



def test_hlarcaddin_is_not_abstract():
    assert not inspect.isabstract(HLArcAddin)


def test_hlarcaddin_constructor_exists():
    assert callable(HLArcAddin.__init__)


def test_hlarcaddin_constructor_args():
    sig = inspect.signature(HLArcAddin.__init__)
    params = list(sig.parameters.keys())



def test_hasgraphics_is_not_abstract():
    assert not inspect.isabstract(HasGraphics)


def test_hasgraphics_constructor_exists():
    assert callable(HasGraphics.__init__)


def test_hasgraphics_constructor_args():
    sig = inspect.signature(HasGraphics.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::object_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Object)


def test_org_k1s_nppn::object_constructor_exists():
    assert callable(org_k1s_nppn::Object.__init__)


def test_org_k1s_nppn::object_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Object.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::arc_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Arc)


def test_org_k1s_nppn::arc_constructor_exists():
    assert callable(org_k1s_nppn::Arc.__init__)


def test_org_k1s_nppn::arc_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Arc.__init__)
    params = list(sig.parameters.keys())



def test_nppn::binding_is_not_abstract():
    assert not inspect.isabstract(nppn::Binding)


def test_nppn::binding_constructor_exists():
    assert callable(nppn::Binding.__init__)


def test_nppn::binding_constructor_args():
    sig = inspect.signature(nppn::Binding.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::bindings_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Bindings)


def test_org_k1s_nppn::bindings_constructor_exists():
    assert callable(org_k1s_nppn::Bindings.__init__)


def test_org_k1s_nppn::bindings_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Bindings.__init__)
    params = list(sig.parameters.keys())



def test_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_container_constructor_exists():
    assert callable(Container.__init__)


def test_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::conditional_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Conditional)


def test_org_k1s_nppn::conditional_constructor_exists():
    assert callable(org_k1s_nppn::Conditional.__init__)


def test_org_k1s_nppn::conditional_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::conditinoal_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Conditinoal)


def test_org_k1s_nppn::conditinoal_constructor_exists():
    assert callable(org_k1s_nppn::Conditinoal.__init__)


def test_org_k1s_nppn::conditinoal_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Conditinoal.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::loop_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Loop)


def test_org_k1s_nppn::loop_constructor_exists():
    assert callable(org_k1s_nppn::Loop.__init__)


def test_org_k1s_nppn::loop_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Loop.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::atomic_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Atomic)


def test_org_k1s_nppn::atomic_constructor_exists():
    assert callable(org_k1s_nppn::Atomic.__init__)


def test_org_k1s_nppn::atomic_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Atomic.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::binding_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Binding)


def test_org_k1s_nppn::binding_constructor_exists():
    assert callable(org_k1s_nppn::Binding.__init__)


def test_org_k1s_nppn::binding_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Binding.__init__)
    params = list(sig.parameters.keys())
    assert "template" in params, "Missing parameter 'template'"

def test_org_k1s_nppn::binding_has_template():
    assert hasattr(org_k1s_nppn::Binding, "template")
    descriptor = None
    for klass in org_k1s_nppn::Binding.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)



def test_org_k1s_nppn::container_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Container)


def test_org_k1s_nppn::container_constructor_exists():
    assert callable(org_k1s_nppn::Container.__init__)


def test_org_k1s_nppn::container_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Container.__init__)
    params = list(sig.parameters.keys())



def test_nppn::transition_is_not_abstract():
    assert not inspect.isabstract(nppn::Transition)


def test_nppn::transition_constructor_exists():
    assert callable(nppn::Transition.__init__)


def test_nppn::transition_constructor_args():
    sig = inspect.signature(nppn::Transition.__init__)
    params = list(sig.parameters.keys())



def test_nppn::placenode_is_not_abstract():
    assert not inspect.isabstract(nppn::PlaceNode)


def test_nppn::placenode_constructor_exists():
    assert callable(nppn::PlaceNode.__init__)


def test_nppn::placenode_constructor_args():
    sig = inspect.signature(nppn::PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::block_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Block)


def test_org_k1s_nppn::block_constructor_exists():
    assert callable(org_k1s_nppn::Block.__init__)


def test_org_k1s_nppn::block_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Block.__init__)
    params = list(sig.parameters.keys())



def test_nppn::block_is_not_abstract():
    assert not inspect.isabstract(nppn::Block)


def test_nppn::block_constructor_exists():
    assert callable(nppn::Block.__init__)


def test_nppn::block_constructor_args():
    sig = inspect.signature(nppn::Block.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::service_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Service)


def test_org_k1s_nppn::service_constructor_exists():
    assert callable(org_k1s_nppn::Service.__init__)


def test_org_k1s_nppn::service_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Service.__init__)
    params = list(sig.parameters.keys())



def test_nppn::service_is_not_abstract():
    assert not inspect.isabstract(nppn::Service)


def test_nppn::service_constructor_exists():
    assert callable(nppn::Service.__init__)


def test_nppn::service_constructor_args():
    sig = inspect.signature(nppn::Service.__init__)
    params = list(sig.parameters.keys())



def test_nppn::instance_is_not_abstract():
    assert not inspect.isabstract(nppn::Instance)


def test_nppn::instance_constructor_exists():
    assert callable(nppn::Instance.__init__)


def test_nppn::instance_constructor_args():
    sig = inspect.signature(nppn::Instance.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::principal_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Principal)


def test_org_k1s_nppn::principal_constructor_exists():
    assert callable(org_k1s_nppn::Principal.__init__)


def test_org_k1s_nppn::principal_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Principal.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::placementconstraints_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::PlacementConstraints)


def test_org_k1s_nppn::placementconstraints_constructor_exists():
    assert callable(org_k1s_nppn::PlacementConstraints.__init__)


def test_org_k1s_nppn::placementconstraints_constructor_args():
    sig = inspect.signature(org_k1s_nppn::PlacementConstraints.__init__)
    params = list(sig.parameters.keys())



def test_nppn::principal_is_not_abstract():
    assert not inspect.isabstract(nppn::Principal)


def test_nppn::principal_constructor_exists():
    assert callable(nppn::Principal.__init__)


def test_nppn::principal_constructor_args():
    sig = inspect.signature(nppn::Principal.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::abstracttemplatetree_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::AbstractTemplateTree)


def test_org_k1s_nppn::abstracttemplatetree_constructor_exists():
    assert callable(org_k1s_nppn::AbstractTemplateTree.__init__)


def test_org_k1s_nppn::abstracttemplatetree_constructor_args():
    sig = inspect.signature(org_k1s_nppn::AbstractTemplateTree.__init__)
    params = list(sig.parameters.keys())



def test_explicit_is_not_abstract():
    assert not inspect.isabstract(Explicit)


def test_explicit_constructor_exists():
    assert callable(Explicit.__init__)


def test_explicit_constructor_args():
    sig = inspect.signature(Explicit.__init__)
    params = list(sig.parameters.keys())



def test_custompragmatics_is_not_abstract():
    assert not inspect.isabstract(CustomPragmatics)


def test_custompragmatics_constructor_exists():
    assert callable(CustomPragmatics.__init__)


def test_custompragmatics_constructor_args():
    sig = inspect.signature(CustomPragmatics.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::customexplicitpragmatics_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::CustomExplicitPragmatics)


def test_org_k1s_nppn::customexplicitpragmatics_constructor_exists():
    assert callable(org_k1s_nppn::CustomExplicitPragmatics.__init__)


def test_org_k1s_nppn::customexplicitpragmatics_constructor_args():
    sig = inspect.signature(org_k1s_nppn::CustomExplicitPragmatics.__init__)
    params = list(sig.parameters.keys())



def test_derived_is_not_abstract():
    assert not inspect.isabstract(Derived)


def test_derived_constructor_exists():
    assert callable(Derived.__init__)


def test_derived_constructor_args():
    sig = inspect.signature(Derived.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::customderivedpragmatics_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::CustomDerivedPragmatics)


def test_org_k1s_nppn::customderivedpragmatics_constructor_exists():
    assert callable(org_k1s_nppn::CustomDerivedPragmatics.__init__)


def test_org_k1s_nppn::customderivedpragmatics_constructor_args():
    sig = inspect.signature(org_k1s_nppn::CustomDerivedPragmatics.__init__)
    params = list(sig.parameters.keys())



def test_nppn::placementconstraints_is_not_abstract():
    assert not inspect.isabstract(nppn::PlacementConstraints)


def test_nppn::placementconstraints_constructor_exists():
    assert callable(nppn::PlacementConstraints.__init__)


def test_nppn::placementconstraints_constructor_args():
    sig = inspect.signature(nppn::PlacementConstraints.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::pnpattern_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::PNPattern)


def test_org_k1s_nppn::pnpattern_constructor_exists():
    assert callable(org_k1s_nppn::PNPattern.__init__)


def test_org_k1s_nppn::pnpattern_constructor_args():
    sig = inspect.signature(org_k1s_nppn::PNPattern.__init__)
    params = list(sig.parameters.keys())



def test_nppn::pnpattern_is_not_abstract():
    assert not inspect.isabstract(nppn::PNPattern)


def test_nppn::pnpattern_constructor_exists():
    assert callable(nppn::PNPattern.__init__)


def test_nppn::pnpattern_constructor_args():
    sig = inspect.signature(nppn::PNPattern.__init__)
    params = list(sig.parameters.keys())



def test_pragmatic_is_not_abstract():
    assert not inspect.isabstract(Pragmatic)


def test_pragmatic_constructor_exists():
    assert callable(Pragmatic.__init__)


def test_pragmatic_constructor_args():
    sig = inspect.signature(Pragmatic.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::custompragmatics_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::CustomPragmatics)


def test_org_k1s_nppn::custompragmatics_constructor_exists():
    assert callable(org_k1s_nppn::CustomPragmatics.__init__)


def test_org_k1s_nppn::custompragmatics_constructor_args():
    sig = inspect.signature(org_k1s_nppn::CustomPragmatics.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::derived_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Derived)


def test_org_k1s_nppn::derived_constructor_exists():
    assert callable(org_k1s_nppn::Derived.__init__)


def test_org_k1s_nppn::derived_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Derived.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn::explicit_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn::Explicit)


def test_org_k1s_nppn::explicit_constructor_exists():
    assert callable(org_k1s_nppn::Explicit.__init__)


def test_org_k1s_nppn::explicit_constructor_args():
    sig = inspect.signature(org_k1s_nppn::Explicit.__init__)
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
org_k1s_nppn::Pragmatic_strategy = st.builds(
    org_k1s_nppn::Pragmatic,
    name=
        safe_text
)
nppn::TransitionNode_strategy = st.builds(
    nppn::TransitionNode,
)
TransitionNode_strategy = st.builds(
    TransitionNode,
)
org_k1s_nppn::Transition_strategy = st.builds(
    org_k1s_nppn::Transition,
)
org_k1s_nppn::RefTrans_strategy = st.builds(
    org_k1s_nppn::RefTrans,
)
nppn::Place_strategy = st.builds(
    nppn::Place,
)
nppn::RefPlace_strategy = st.builds(
    nppn::RefPlace,
)
PlaceNode_strategy = st.builds(
    PlaceNode,
)
org_k1s_nppn::RefPlace_strategy = st.builds(
    org_k1s_nppn::RefPlace,
)
org_k1s_nppn::Place_strategy = st.builds(
    org_k1s_nppn::Place,
)
nppn::Monitor_strategy = st.builds(
    nppn::Monitor,
)
nppn::Object_strategy = st.builds(
    nppn::Object,
)
nppn::PetriNet_strategy = st.builds(
    nppn::PetriNet,
)
HasName_strategy = st.builds(
    HasName,
)
HasLabel_strategy = st.builds(
    HasLabel,
)
org_k1s_nppn::PetriNet_strategy = st.builds(
    org_k1s_nppn::PetriNet,
    kind=
        safe_text,
    timeType=
        safe_text
)
org_k1s_nppn::Page_strategy = st.builds(
    org_k1s_nppn::Page,
)
org_k1s_nppn::Label_strategy = st.builds(
    org_k1s_nppn::Label,
)
nppn::Pragmatic_strategy = st.builds(
    nppn::Pragmatic,
)
nppn::Arc_strategy = st.builds(
    nppn::Arc,
)
Object_strategy = st.builds(
    Object,
)
org_k1s_nppn::Node_strategy = st.builds(
    org_k1s_nppn::Node,
)
HLAnnotation_strategy = st.builds(
    HLAnnotation,
)
org_k1s_nppn::Name_strategy = st.builds(
    org_k1s_nppn::Name,
)
nppn::HasLabel_strategy = st.builds(
    nppn::HasLabel,
)
nppn::HLAnnotation_strategy = st.builds(
    nppn::HLAnnotation,
)
org_k1s_nppn::HLArcAddin_strategy = st.builds(
    org_k1s_nppn::HLArcAddin,
    kind=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
org_k1s_nppn::PlaceNode_strategy = st.builds(
    org_k1s_nppn::PlaceNode,
)
org_k1s_nppn::TransitionNode_strategy = st.builds(
    org_k1s_nppn::TransitionNode,
)
org_k1s_nppn::HLAnnotation_strategy = st.builds(
    org_k1s_nppn::HLAnnotation,
)
org_k1s_nppn::Instance_strategy = st.builds(
    org_k1s_nppn::Instance,
    subPageID=
        safe_text
)
nppn::Page_strategy = st.builds(
    nppn::Page,
)
nppn::Name_strategy = st.builds(
    nppn::Name,
)
org_k1s_nppn::HasName_strategy = st.builds(
    org_k1s_nppn::HasName,
)
nppn::Label_strategy = st.builds(
    nppn::Label,
)
org_k1s_nppn::HasLabel_strategy = st.builds(
    org_k1s_nppn::HasLabel,
)
nppn::Node_strategy = st.builds(
    nppn::Node,
)
HLArcAddin_strategy = st.builds(
    HLArcAddin,
)
HasGraphics_strategy = st.builds(
    HasGraphics,
)
org_k1s_nppn::Object_strategy = st.builds(
    org_k1s_nppn::Object,
)
org_k1s_nppn::Arc_strategy = st.builds(
    org_k1s_nppn::Arc,
)
nppn::Binding_strategy = st.builds(
    nppn::Binding,
)
org_k1s_nppn::Bindings_strategy = st.builds(
    org_k1s_nppn::Bindings,
)
Container_strategy = st.builds(
    Container,
)
org_k1s_nppn::Conditional_strategy = st.builds(
    org_k1s_nppn::Conditional,
)
org_k1s_nppn::Conditinoal_strategy = st.builds(
    org_k1s_nppn::Conditinoal,
)
org_k1s_nppn::Loop_strategy = st.builds(
    org_k1s_nppn::Loop,
)
Block_strategy = st.builds(
    Block,
)
org_k1s_nppn::Atomic_strategy = st.builds(
    org_k1s_nppn::Atomic,
)
org_k1s_nppn::Binding_strategy = st.builds(
    org_k1s_nppn::Binding,
    template=
        safe_text
)
org_k1s_nppn::Container_strategy = st.builds(
    org_k1s_nppn::Container,
)
nppn::Transition_strategy = st.builds(
    nppn::Transition,
)
nppn::PlaceNode_strategy = st.builds(
    nppn::PlaceNode,
)
org_k1s_nppn::Block_strategy = st.builds(
    org_k1s_nppn::Block,
)
nppn::Block_strategy = st.builds(
    nppn::Block,
)
org_k1s_nppn::Service_strategy = st.builds(
    org_k1s_nppn::Service,
)
nppn::Service_strategy = st.builds(
    nppn::Service,
)
nppn::Instance_strategy = st.builds(
    nppn::Instance,
)
org_k1s_nppn::Principal_strategy = st.builds(
    org_k1s_nppn::Principal,
)
org_k1s_nppn::PlacementConstraints_strategy = st.builds(
    org_k1s_nppn::PlacementConstraints,
)
nppn::Principal_strategy = st.builds(
    nppn::Principal,
)
org_k1s_nppn::AbstractTemplateTree_strategy = st.builds(
    org_k1s_nppn::AbstractTemplateTree,
)
Explicit_strategy = st.builds(
    Explicit,
)
CustomPragmatics_strategy = st.builds(
    CustomPragmatics,
)
org_k1s_nppn::CustomExplicitPragmatics_strategy = st.builds(
    org_k1s_nppn::CustomExplicitPragmatics,
)
Derived_strategy = st.builds(
    Derived,
)
org_k1s_nppn::CustomDerivedPragmatics_strategy = st.builds(
    org_k1s_nppn::CustomDerivedPragmatics,
)
nppn::PlacementConstraints_strategy = st.builds(
    nppn::PlacementConstraints,
)
org_k1s_nppn::PNPattern_strategy = st.builds(
    org_k1s_nppn::PNPattern,
)
nppn::PNPattern_strategy = st.builds(
    nppn::PNPattern,
)
Pragmatic_strategy = st.builds(
    Pragmatic,
)
org_k1s_nppn::CustomPragmatics_strategy = st.builds(
    org_k1s_nppn::CustomPragmatics,
)
org_k1s_nppn::Derived_strategy = st.builds(
    org_k1s_nppn::Derived,
)
org_k1s_nppn::Explicit_strategy = st.builds(
    org_k1s_nppn::Explicit,
)

@given(instance=org_k1s_nppn::Pragmatic_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::pragmatic_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Pragmatic)

@given(instance=org_k1s_nppn::Pragmatic_strategy)
def test_org_k1s_nppn::pragmatic_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=org_k1s_nppn::Pragmatic_strategy)
def test_org_k1s_nppn::pragmatic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nppn::TransitionNode_strategy)
@settings(max_examples=50)
def test_nppn::transitionnode_instantiation(instance):
    assert isinstance(instance, nppn::TransitionNode)

@given(instance=TransitionNode_strategy)
@settings(max_examples=50)
def test_transitionnode_instantiation(instance):
    assert isinstance(instance, TransitionNode)

@given(instance=org_k1s_nppn::Transition_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::transition_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Transition)

@given(instance=org_k1s_nppn::RefTrans_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::reftrans_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::RefTrans)

@given(instance=nppn::Place_strategy)
@settings(max_examples=50)
def test_nppn::place_instantiation(instance):
    assert isinstance(instance, nppn::Place)

@given(instance=nppn::RefPlace_strategy)
@settings(max_examples=50)
def test_nppn::refplace_instantiation(instance):
    assert isinstance(instance, nppn::RefPlace)

@given(instance=PlaceNode_strategy)
@settings(max_examples=50)
def test_placenode_instantiation(instance):
    assert isinstance(instance, PlaceNode)

@given(instance=org_k1s_nppn::RefPlace_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::refplace_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::RefPlace)

@given(instance=org_k1s_nppn::Place_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::place_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Place)

@given(instance=nppn::Monitor_strategy)
@settings(max_examples=50)
def test_nppn::monitor_instantiation(instance):
    assert isinstance(instance, nppn::Monitor)

@given(instance=nppn::Object_strategy)
@settings(max_examples=50)
def test_nppn::object_instantiation(instance):
    assert isinstance(instance, nppn::Object)

@given(instance=nppn::PetriNet_strategy)
@settings(max_examples=50)
def test_nppn::petrinet_instantiation(instance):
    assert isinstance(instance, nppn::PetriNet)

@given(instance=HasName_strategy)
@settings(max_examples=50)
def test_hasname_instantiation(instance):
    assert isinstance(instance, HasName)

@given(instance=HasLabel_strategy)
@settings(max_examples=50)
def test_haslabel_instantiation(instance):
    assert isinstance(instance, HasLabel)

@given(instance=org_k1s_nppn::PetriNet_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::petrinet_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::PetriNet)

@given(instance=org_k1s_nppn::PetriNet_strategy)
def test_org_k1s_nppn::petrinet_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=org_k1s_nppn::PetriNet_strategy)
def test_org_k1s_nppn::petrinet_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=org_k1s_nppn::PetriNet_strategy)
def test_org_k1s_nppn::petrinet_timeType_type(instance):
    assert isinstance(instance.timeType, str)


@given(instance=org_k1s_nppn::PetriNet_strategy)
def test_org_k1s_nppn::petrinet_timeType_setter(instance):
    original = instance.timeType
    instance.timeType = original
    assert instance.timeType == original

@given(instance=org_k1s_nppn::Page_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::page_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Page)

@given(instance=org_k1s_nppn::Label_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::label_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Label)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=org_k1s_nppn::Label_strategy)
@settings(max_examples=30)
def test_org_k1s_nppn::label_asstring_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.asString()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.asString).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'asString' in org_k1s_nppn::Label is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'asString' in org_k1s_nppn::Label did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'asString' in org_k1s_nppn::Label is not implemented or raised an error")

@given(instance=nppn::Pragmatic_strategy)
@settings(max_examples=50)
def test_nppn::pragmatic_instantiation(instance):
    assert isinstance(instance, nppn::Pragmatic)

@given(instance=nppn::Arc_strategy)
@settings(max_examples=50)
def test_nppn::arc_instantiation(instance):
    assert isinstance(instance, nppn::Arc)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=org_k1s_nppn::Node_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::node_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Node)

@given(instance=HLAnnotation_strategy)
@settings(max_examples=50)
def test_hlannotation_instantiation(instance):
    assert isinstance(instance, HLAnnotation)

@given(instance=org_k1s_nppn::Name_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::name_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Name)

@given(instance=nppn::HasLabel_strategy)
@settings(max_examples=50)
def test_nppn::haslabel_instantiation(instance):
    assert isinstance(instance, nppn::HasLabel)

@given(instance=nppn::HLAnnotation_strategy)
@settings(max_examples=50)
def test_nppn::hlannotation_instantiation(instance):
    assert isinstance(instance, nppn::HLAnnotation)

@given(instance=org_k1s_nppn::HLArcAddin_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::hlarcaddin_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::HLArcAddin)

@given(instance=org_k1s_nppn::HLArcAddin_strategy)
def test_org_k1s_nppn::hlarcaddin_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=org_k1s_nppn::HLArcAddin_strategy)
def test_org_k1s_nppn::hlarcaddin_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=org_k1s_nppn::PlaceNode_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::placenode_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::PlaceNode)

@given(instance=org_k1s_nppn::TransitionNode_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::transitionnode_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::TransitionNode)

@given(instance=org_k1s_nppn::HLAnnotation_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::hlannotation_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::HLAnnotation)

@given(instance=org_k1s_nppn::Instance_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::instance_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Instance)

@given(instance=org_k1s_nppn::Instance_strategy)
def test_org_k1s_nppn::instance_subPageID_type(instance):
    assert isinstance(instance.subPageID, str)


@given(instance=org_k1s_nppn::Instance_strategy)
def test_org_k1s_nppn::instance_subPageID_setter(instance):
    original = instance.subPageID
    instance.subPageID = original
    assert instance.subPageID == original

@given(instance=nppn::Page_strategy)
@settings(max_examples=50)
def test_nppn::page_instantiation(instance):
    assert isinstance(instance, nppn::Page)

@given(instance=nppn::Name_strategy)
@settings(max_examples=50)
def test_nppn::name_instantiation(instance):
    assert isinstance(instance, nppn::Name)

@given(instance=org_k1s_nppn::HasName_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::hasname_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::HasName)

@given(instance=nppn::Label_strategy)
@settings(max_examples=50)
def test_nppn::label_instantiation(instance):
    assert isinstance(instance, nppn::Label)

@given(instance=org_k1s_nppn::HasLabel_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::haslabel_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::HasLabel)

@given(instance=nppn::Node_strategy)
@settings(max_examples=50)
def test_nppn::node_instantiation(instance):
    assert isinstance(instance, nppn::Node)

@given(instance=HLArcAddin_strategy)
@settings(max_examples=50)
def test_hlarcaddin_instantiation(instance):
    assert isinstance(instance, HLArcAddin)

@given(instance=HasGraphics_strategy)
@settings(max_examples=50)
def test_hasgraphics_instantiation(instance):
    assert isinstance(instance, HasGraphics)

@given(instance=org_k1s_nppn::Object_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::object_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Object)

@given(instance=org_k1s_nppn::Arc_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::arc_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Arc)

@given(instance=nppn::Binding_strategy)
@settings(max_examples=50)
def test_nppn::binding_instantiation(instance):
    assert isinstance(instance, nppn::Binding)

@given(instance=org_k1s_nppn::Bindings_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::bindings_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Bindings)

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=org_k1s_nppn::Conditional_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::conditional_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Conditional)

@given(instance=org_k1s_nppn::Conditinoal_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::conditinoal_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Conditinoal)

@given(instance=org_k1s_nppn::Loop_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::loop_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Loop)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=org_k1s_nppn::Atomic_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::atomic_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Atomic)

@given(instance=org_k1s_nppn::Binding_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::binding_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Binding)

@given(instance=org_k1s_nppn::Binding_strategy)
def test_org_k1s_nppn::binding_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=org_k1s_nppn::Binding_strategy)
def test_org_k1s_nppn::binding_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=org_k1s_nppn::Container_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::container_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Container)

@given(instance=nppn::Transition_strategy)
@settings(max_examples=50)
def test_nppn::transition_instantiation(instance):
    assert isinstance(instance, nppn::Transition)

@given(instance=nppn::PlaceNode_strategy)
@settings(max_examples=50)
def test_nppn::placenode_instantiation(instance):
    assert isinstance(instance, nppn::PlaceNode)

@given(instance=org_k1s_nppn::Block_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::block_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Block)

@given(instance=nppn::Block_strategy)
@settings(max_examples=50)
def test_nppn::block_instantiation(instance):
    assert isinstance(instance, nppn::Block)

@given(instance=org_k1s_nppn::Service_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::service_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Service)

@given(instance=nppn::Service_strategy)
@settings(max_examples=50)
def test_nppn::service_instantiation(instance):
    assert isinstance(instance, nppn::Service)

@given(instance=nppn::Instance_strategy)
@settings(max_examples=50)
def test_nppn::instance_instantiation(instance):
    assert isinstance(instance, nppn::Instance)

@given(instance=org_k1s_nppn::Principal_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::principal_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Principal)

@given(instance=org_k1s_nppn::PlacementConstraints_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::placementconstraints_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::PlacementConstraints)

@given(instance=nppn::Principal_strategy)
@settings(max_examples=50)
def test_nppn::principal_instantiation(instance):
    assert isinstance(instance, nppn::Principal)

@given(instance=org_k1s_nppn::AbstractTemplateTree_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::abstracttemplatetree_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::AbstractTemplateTree)

@given(instance=Explicit_strategy)
@settings(max_examples=50)
def test_explicit_instantiation(instance):
    assert isinstance(instance, Explicit)

@given(instance=CustomPragmatics_strategy)
@settings(max_examples=50)
def test_custompragmatics_instantiation(instance):
    assert isinstance(instance, CustomPragmatics)

@given(instance=org_k1s_nppn::CustomExplicitPragmatics_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::customexplicitpragmatics_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::CustomExplicitPragmatics)

@given(instance=Derived_strategy)
@settings(max_examples=50)
def test_derived_instantiation(instance):
    assert isinstance(instance, Derived)

@given(instance=org_k1s_nppn::CustomDerivedPragmatics_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::customderivedpragmatics_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::CustomDerivedPragmatics)

@given(instance=nppn::PlacementConstraints_strategy)
@settings(max_examples=50)
def test_nppn::placementconstraints_instantiation(instance):
    assert isinstance(instance, nppn::PlacementConstraints)

@given(instance=org_k1s_nppn::PNPattern_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::pnpattern_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::PNPattern)

@given(instance=nppn::PNPattern_strategy)
@settings(max_examples=50)
def test_nppn::pnpattern_instantiation(instance):
    assert isinstance(instance, nppn::PNPattern)

@given(instance=Pragmatic_strategy)
@settings(max_examples=50)
def test_pragmatic_instantiation(instance):
    assert isinstance(instance, Pragmatic)

@given(instance=org_k1s_nppn::CustomPragmatics_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::custompragmatics_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::CustomPragmatics)

@given(instance=org_k1s_nppn::Derived_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::derived_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Derived)

@given(instance=org_k1s_nppn::Explicit_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn::explicit_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn::Explicit)
