import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    nppn_Place,
    nppn_RefPlace,
    PlaceNode,
    org_k1s_nppn_RefPlace,
    org_k1s_nppn_Place,
    nppn_Monitor,
    nppn_Object,
    nppn_PetriNet,
    HasName,
    HasLabel,
    org_k1s_nppn_Page,
    org_k1s_nppn_PetriNet,
    org_k1s_nppn_Label,
    nppn_Pragmatic,
    nppn_Arc,
    Object,
    org_k1s_nppn_Node,
    HLAnnotation,
    org_k1s_nppn_Name,
    nppn_HasLabel,
    nppn_HLAnnotation,
    org_k1s_nppn_HLArcAddin,
    Node,
    org_k1s_nppn_HLAnnotation,
    org_k1s_nppn_Instance,
    nppn_Page,
    nppn_Name,
    org_k1s_nppn_HasName,
    nppn_Label,
    org_k1s_nppn_HasLabel,
    nppn_Node,
    HLArcAddin,
    HasGraphics,
    org_k1s_nppn_Object,
    org_k1s_nppn_Arc,
    nppn_Binding,
    org_k1s_nppn_Bindings,
    Container,
    org_k1s_nppn_Conditinoal,
    org_k1s_nppn_Conditional,
    org_k1s_nppn_Loop,
    Block,
    org_k1s_nppn_Atomic,
    org_k1s_nppn_Binding,
    org_k1s_nppn_Container,
    nppn_Transition,
    nppn_PlaceNode,
    org_k1s_nppn_Block,
    nppn_Block,
    org_k1s_nppn_Service,
    nppn_Service,
    nppn_Instance,
    org_k1s_nppn_Principal,
    org_k1s_nppn_PlacementConstraints,
    nppn_Principal,
    org_k1s_nppn_AbstractTemplateTree,
    Explicit,
    CustomPragmatics,
    org_k1s_nppn_CustomExplicitPragmatics,
    Derived,
    org_k1s_nppn_CustomDerivedPragmatics,
    nppn_PlacementConstraints,
    org_k1s_nppn_PNPattern,
    nppn_PNPattern,
    Pragmatic,
    org_k1s_nppn_CustomPragmatics,
    org_k1s_nppn_Explicit,
    org_k1s_nppn_Derived,
    org_k1s_nppn_PlaceNode,
    org_k1s_nppn_Pragmatic,
    org_k1s_nppn_TransitionNode,
    nppn_TransitionNode,
    TransitionNode,
    org_k1s_nppn_Transition,
    org_k1s_nppn_RefTrans,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nppn_place_is_not_abstract():
    assert not inspect.isabstract(nppn_Place)


def test_nppn_place_constructor_exists():
    assert callable(nppn_Place.__init__)


def test_nppn_place_constructor_args():
    sig = inspect.signature(nppn_Place.__init__)
    params = list(sig.parameters.keys())



def test_nppn_refplace_is_not_abstract():
    assert not inspect.isabstract(nppn_RefPlace)


def test_nppn_refplace_constructor_exists():
    assert callable(nppn_RefPlace.__init__)


def test_nppn_refplace_constructor_args():
    sig = inspect.signature(nppn_RefPlace.__init__)
    params = list(sig.parameters.keys())



def test_placenode_is_not_abstract():
    assert not inspect.isabstract(PlaceNode)


def test_placenode_constructor_exists():
    assert callable(PlaceNode.__init__)


def test_placenode_constructor_args():
    sig = inspect.signature(PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_refplace_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_RefPlace)


def test_org_k1s_nppn_refplace_constructor_exists():
    assert callable(org_k1s_nppn_RefPlace.__init__)


def test_org_k1s_nppn_refplace_constructor_args():
    sig = inspect.signature(org_k1s_nppn_RefPlace.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_place_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Place)


def test_org_k1s_nppn_place_constructor_exists():
    assert callable(org_k1s_nppn_Place.__init__)


def test_org_k1s_nppn_place_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Place.__init__)
    params = list(sig.parameters.keys())



def test_nppn_monitor_is_not_abstract():
    assert not inspect.isabstract(nppn_Monitor)


def test_nppn_monitor_constructor_exists():
    assert callable(nppn_Monitor.__init__)


def test_nppn_monitor_constructor_args():
    sig = inspect.signature(nppn_Monitor.__init__)
    params = list(sig.parameters.keys())



def test_nppn_object_is_not_abstract():
    assert not inspect.isabstract(nppn_Object)


def test_nppn_object_constructor_exists():
    assert callable(nppn_Object.__init__)


def test_nppn_object_constructor_args():
    sig = inspect.signature(nppn_Object.__init__)
    params = list(sig.parameters.keys())



def test_nppn_petrinet_is_not_abstract():
    assert not inspect.isabstract(nppn_PetriNet)


def test_nppn_petrinet_constructor_exists():
    assert callable(nppn_PetriNet.__init__)


def test_nppn_petrinet_constructor_args():
    sig = inspect.signature(nppn_PetriNet.__init__)
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



def test_org_k1s_nppn_page_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Page)


def test_org_k1s_nppn_page_constructor_exists():
    assert callable(org_k1s_nppn_Page.__init__)


def test_org_k1s_nppn_page_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Page.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_petrinet_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_PetriNet)


def test_org_k1s_nppn_petrinet_constructor_exists():
    assert callable(org_k1s_nppn_PetriNet.__init__)


def test_org_k1s_nppn_petrinet_constructor_args():
    sig = inspect.signature(org_k1s_nppn_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "timeType" in params, "Missing parameter 'timeType'"

def test_org_k1s_nppn_petrinet_has_kind():
    assert hasattr(org_k1s_nppn_PetriNet, "kind")
    descriptor = None
    for klass in org_k1s_nppn_PetriNet.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_org_k1s_nppn_petrinet_has_timeType():
    assert hasattr(org_k1s_nppn_PetriNet, "timeType")
    descriptor = None
    for klass in org_k1s_nppn_PetriNet.__mro__:
        if "timeType" in klass.__dict__:
            descriptor = klass.__dict__["timeType"]
            break
    assert isinstance(descriptor, property)



def test_org_k1s_nppn_label_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Label)


def test_org_k1s_nppn_label_constructor_exists():
    assert callable(org_k1s_nppn_Label.__init__)


def test_org_k1s_nppn_label_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Label.__init__)
    params = list(sig.parameters.keys())



def test_nppn_pragmatic_is_not_abstract():
    assert not inspect.isabstract(nppn_Pragmatic)


def test_nppn_pragmatic_constructor_exists():
    assert callable(nppn_Pragmatic.__init__)


def test_nppn_pragmatic_constructor_args():
    sig = inspect.signature(nppn_Pragmatic.__init__)
    params = list(sig.parameters.keys())



def test_nppn_arc_is_not_abstract():
    assert not inspect.isabstract(nppn_Arc)


def test_nppn_arc_constructor_exists():
    assert callable(nppn_Arc.__init__)


def test_nppn_arc_constructor_args():
    sig = inspect.signature(nppn_Arc.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_node_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Node)


def test_org_k1s_nppn_node_constructor_exists():
    assert callable(org_k1s_nppn_Node.__init__)


def test_org_k1s_nppn_node_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Node.__init__)
    params = list(sig.parameters.keys())



def test_hlannotation_is_not_abstract():
    assert not inspect.isabstract(HLAnnotation)


def test_hlannotation_constructor_exists():
    assert callable(HLAnnotation.__init__)


def test_hlannotation_constructor_args():
    sig = inspect.signature(HLAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_name_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Name)


def test_org_k1s_nppn_name_constructor_exists():
    assert callable(org_k1s_nppn_Name.__init__)


def test_org_k1s_nppn_name_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Name.__init__)
    params = list(sig.parameters.keys())



def test_nppn_haslabel_is_not_abstract():
    assert not inspect.isabstract(nppn_HasLabel)


def test_nppn_haslabel_constructor_exists():
    assert callable(nppn_HasLabel.__init__)


def test_nppn_haslabel_constructor_args():
    sig = inspect.signature(nppn_HasLabel.__init__)
    params = list(sig.parameters.keys())



def test_nppn_hlannotation_is_not_abstract():
    assert not inspect.isabstract(nppn_HLAnnotation)


def test_nppn_hlannotation_constructor_exists():
    assert callable(nppn_HLAnnotation.__init__)


def test_nppn_hlannotation_constructor_args():
    sig = inspect.signature(nppn_HLAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_hlarcaddin_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_HLArcAddin)


def test_org_k1s_nppn_hlarcaddin_constructor_exists():
    assert callable(org_k1s_nppn_HLArcAddin.__init__)


def test_org_k1s_nppn_hlarcaddin_constructor_args():
    sig = inspect.signature(org_k1s_nppn_HLArcAddin.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_org_k1s_nppn_hlarcaddin_has_kind():
    assert hasattr(org_k1s_nppn_HLArcAddin, "kind")
    descriptor = None
    for klass in org_k1s_nppn_HLArcAddin.__mro__:
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



def test_org_k1s_nppn_hlannotation_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_HLAnnotation)


def test_org_k1s_nppn_hlannotation_constructor_exists():
    assert callable(org_k1s_nppn_HLAnnotation.__init__)


def test_org_k1s_nppn_hlannotation_constructor_args():
    sig = inspect.signature(org_k1s_nppn_HLAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_instance_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Instance)


def test_org_k1s_nppn_instance_constructor_exists():
    assert callable(org_k1s_nppn_Instance.__init__)


def test_org_k1s_nppn_instance_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Instance.__init__)
    params = list(sig.parameters.keys())
    assert "subPageID" in params, "Missing parameter 'subPageID'"

def test_org_k1s_nppn_instance_has_subPageID():
    assert hasattr(org_k1s_nppn_Instance, "subPageID")
    descriptor = None
    for klass in org_k1s_nppn_Instance.__mro__:
        if "subPageID" in klass.__dict__:
            descriptor = klass.__dict__["subPageID"]
            break
    assert isinstance(descriptor, property)



def test_nppn_page_is_not_abstract():
    assert not inspect.isabstract(nppn_Page)


def test_nppn_page_constructor_exists():
    assert callable(nppn_Page.__init__)


def test_nppn_page_constructor_args():
    sig = inspect.signature(nppn_Page.__init__)
    params = list(sig.parameters.keys())



def test_nppn_name_is_not_abstract():
    assert not inspect.isabstract(nppn_Name)


def test_nppn_name_constructor_exists():
    assert callable(nppn_Name.__init__)


def test_nppn_name_constructor_args():
    sig = inspect.signature(nppn_Name.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_hasname_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_HasName)


def test_org_k1s_nppn_hasname_constructor_exists():
    assert callable(org_k1s_nppn_HasName.__init__)


def test_org_k1s_nppn_hasname_constructor_args():
    sig = inspect.signature(org_k1s_nppn_HasName.__init__)
    params = list(sig.parameters.keys())



def test_nppn_label_is_not_abstract():
    assert not inspect.isabstract(nppn_Label)


def test_nppn_label_constructor_exists():
    assert callable(nppn_Label.__init__)


def test_nppn_label_constructor_args():
    sig = inspect.signature(nppn_Label.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_haslabel_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_HasLabel)


def test_org_k1s_nppn_haslabel_constructor_exists():
    assert callable(org_k1s_nppn_HasLabel.__init__)


def test_org_k1s_nppn_haslabel_constructor_args():
    sig = inspect.signature(org_k1s_nppn_HasLabel.__init__)
    params = list(sig.parameters.keys())



def test_nppn_node_is_not_abstract():
    assert not inspect.isabstract(nppn_Node)


def test_nppn_node_constructor_exists():
    assert callable(nppn_Node.__init__)


def test_nppn_node_constructor_args():
    sig = inspect.signature(nppn_Node.__init__)
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



def test_org_k1s_nppn_object_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Object)


def test_org_k1s_nppn_object_constructor_exists():
    assert callable(org_k1s_nppn_Object.__init__)


def test_org_k1s_nppn_object_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Object.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_arc_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Arc)


def test_org_k1s_nppn_arc_constructor_exists():
    assert callable(org_k1s_nppn_Arc.__init__)


def test_org_k1s_nppn_arc_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Arc.__init__)
    params = list(sig.parameters.keys())



def test_nppn_binding_is_not_abstract():
    assert not inspect.isabstract(nppn_Binding)


def test_nppn_binding_constructor_exists():
    assert callable(nppn_Binding.__init__)


def test_nppn_binding_constructor_args():
    sig = inspect.signature(nppn_Binding.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_bindings_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Bindings)


def test_org_k1s_nppn_bindings_constructor_exists():
    assert callable(org_k1s_nppn_Bindings.__init__)


def test_org_k1s_nppn_bindings_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Bindings.__init__)
    params = list(sig.parameters.keys())



def test_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_container_constructor_exists():
    assert callable(Container.__init__)


def test_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_conditinoal_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Conditinoal)


def test_org_k1s_nppn_conditinoal_constructor_exists():
    assert callable(org_k1s_nppn_Conditinoal.__init__)


def test_org_k1s_nppn_conditinoal_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Conditinoal.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_conditional_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Conditional)


def test_org_k1s_nppn_conditional_constructor_exists():
    assert callable(org_k1s_nppn_Conditional.__init__)


def test_org_k1s_nppn_conditional_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_loop_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Loop)


def test_org_k1s_nppn_loop_constructor_exists():
    assert callable(org_k1s_nppn_Loop.__init__)


def test_org_k1s_nppn_loop_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Loop.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_atomic_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Atomic)


def test_org_k1s_nppn_atomic_constructor_exists():
    assert callable(org_k1s_nppn_Atomic.__init__)


def test_org_k1s_nppn_atomic_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Atomic.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_binding_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Binding)


def test_org_k1s_nppn_binding_constructor_exists():
    assert callable(org_k1s_nppn_Binding.__init__)


def test_org_k1s_nppn_binding_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Binding.__init__)
    params = list(sig.parameters.keys())
    assert "template" in params, "Missing parameter 'template'"

def test_org_k1s_nppn_binding_has_template():
    assert hasattr(org_k1s_nppn_Binding, "template")
    descriptor = None
    for klass in org_k1s_nppn_Binding.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)



def test_org_k1s_nppn_container_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Container)


def test_org_k1s_nppn_container_constructor_exists():
    assert callable(org_k1s_nppn_Container.__init__)


def test_org_k1s_nppn_container_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Container.__init__)
    params = list(sig.parameters.keys())



def test_nppn_transition_is_not_abstract():
    assert not inspect.isabstract(nppn_Transition)


def test_nppn_transition_constructor_exists():
    assert callable(nppn_Transition.__init__)


def test_nppn_transition_constructor_args():
    sig = inspect.signature(nppn_Transition.__init__)
    params = list(sig.parameters.keys())



def test_nppn_placenode_is_not_abstract():
    assert not inspect.isabstract(nppn_PlaceNode)


def test_nppn_placenode_constructor_exists():
    assert callable(nppn_PlaceNode.__init__)


def test_nppn_placenode_constructor_args():
    sig = inspect.signature(nppn_PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_block_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Block)


def test_org_k1s_nppn_block_constructor_exists():
    assert callable(org_k1s_nppn_Block.__init__)


def test_org_k1s_nppn_block_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Block.__init__)
    params = list(sig.parameters.keys())



def test_nppn_block_is_not_abstract():
    assert not inspect.isabstract(nppn_Block)


def test_nppn_block_constructor_exists():
    assert callable(nppn_Block.__init__)


def test_nppn_block_constructor_args():
    sig = inspect.signature(nppn_Block.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_service_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Service)


def test_org_k1s_nppn_service_constructor_exists():
    assert callable(org_k1s_nppn_Service.__init__)


def test_org_k1s_nppn_service_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Service.__init__)
    params = list(sig.parameters.keys())



def test_nppn_service_is_not_abstract():
    assert not inspect.isabstract(nppn_Service)


def test_nppn_service_constructor_exists():
    assert callable(nppn_Service.__init__)


def test_nppn_service_constructor_args():
    sig = inspect.signature(nppn_Service.__init__)
    params = list(sig.parameters.keys())



def test_nppn_instance_is_not_abstract():
    assert not inspect.isabstract(nppn_Instance)


def test_nppn_instance_constructor_exists():
    assert callable(nppn_Instance.__init__)


def test_nppn_instance_constructor_args():
    sig = inspect.signature(nppn_Instance.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_principal_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Principal)


def test_org_k1s_nppn_principal_constructor_exists():
    assert callable(org_k1s_nppn_Principal.__init__)


def test_org_k1s_nppn_principal_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Principal.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_placementconstraints_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_PlacementConstraints)


def test_org_k1s_nppn_placementconstraints_constructor_exists():
    assert callable(org_k1s_nppn_PlacementConstraints.__init__)


def test_org_k1s_nppn_placementconstraints_constructor_args():
    sig = inspect.signature(org_k1s_nppn_PlacementConstraints.__init__)
    params = list(sig.parameters.keys())



def test_nppn_principal_is_not_abstract():
    assert not inspect.isabstract(nppn_Principal)


def test_nppn_principal_constructor_exists():
    assert callable(nppn_Principal.__init__)


def test_nppn_principal_constructor_args():
    sig = inspect.signature(nppn_Principal.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_abstracttemplatetree_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_AbstractTemplateTree)


def test_org_k1s_nppn_abstracttemplatetree_constructor_exists():
    assert callable(org_k1s_nppn_AbstractTemplateTree.__init__)


def test_org_k1s_nppn_abstracttemplatetree_constructor_args():
    sig = inspect.signature(org_k1s_nppn_AbstractTemplateTree.__init__)
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



def test_org_k1s_nppn_customexplicitpragmatics_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_CustomExplicitPragmatics)


def test_org_k1s_nppn_customexplicitpragmatics_constructor_exists():
    assert callable(org_k1s_nppn_CustomExplicitPragmatics.__init__)


def test_org_k1s_nppn_customexplicitpragmatics_constructor_args():
    sig = inspect.signature(org_k1s_nppn_CustomExplicitPragmatics.__init__)
    params = list(sig.parameters.keys())



def test_derived_is_not_abstract():
    assert not inspect.isabstract(Derived)


def test_derived_constructor_exists():
    assert callable(Derived.__init__)


def test_derived_constructor_args():
    sig = inspect.signature(Derived.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_customderivedpragmatics_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_CustomDerivedPragmatics)


def test_org_k1s_nppn_customderivedpragmatics_constructor_exists():
    assert callable(org_k1s_nppn_CustomDerivedPragmatics.__init__)


def test_org_k1s_nppn_customderivedpragmatics_constructor_args():
    sig = inspect.signature(org_k1s_nppn_CustomDerivedPragmatics.__init__)
    params = list(sig.parameters.keys())



def test_nppn_placementconstraints_is_not_abstract():
    assert not inspect.isabstract(nppn_PlacementConstraints)


def test_nppn_placementconstraints_constructor_exists():
    assert callable(nppn_PlacementConstraints.__init__)


def test_nppn_placementconstraints_constructor_args():
    sig = inspect.signature(nppn_PlacementConstraints.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_pnpattern_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_PNPattern)


def test_org_k1s_nppn_pnpattern_constructor_exists():
    assert callable(org_k1s_nppn_PNPattern.__init__)


def test_org_k1s_nppn_pnpattern_constructor_args():
    sig = inspect.signature(org_k1s_nppn_PNPattern.__init__)
    params = list(sig.parameters.keys())



def test_nppn_pnpattern_is_not_abstract():
    assert not inspect.isabstract(nppn_PNPattern)


def test_nppn_pnpattern_constructor_exists():
    assert callable(nppn_PNPattern.__init__)


def test_nppn_pnpattern_constructor_args():
    sig = inspect.signature(nppn_PNPattern.__init__)
    params = list(sig.parameters.keys())



def test_pragmatic_is_not_abstract():
    assert not inspect.isabstract(Pragmatic)


def test_pragmatic_constructor_exists():
    assert callable(Pragmatic.__init__)


def test_pragmatic_constructor_args():
    sig = inspect.signature(Pragmatic.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_custompragmatics_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_CustomPragmatics)


def test_org_k1s_nppn_custompragmatics_constructor_exists():
    assert callable(org_k1s_nppn_CustomPragmatics.__init__)


def test_org_k1s_nppn_custompragmatics_constructor_args():
    sig = inspect.signature(org_k1s_nppn_CustomPragmatics.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_explicit_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Explicit)


def test_org_k1s_nppn_explicit_constructor_exists():
    assert callable(org_k1s_nppn_Explicit.__init__)


def test_org_k1s_nppn_explicit_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Explicit.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_derived_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Derived)


def test_org_k1s_nppn_derived_constructor_exists():
    assert callable(org_k1s_nppn_Derived.__init__)


def test_org_k1s_nppn_derived_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Derived.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_placenode_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_PlaceNode)


def test_org_k1s_nppn_placenode_constructor_exists():
    assert callable(org_k1s_nppn_PlaceNode.__init__)


def test_org_k1s_nppn_placenode_constructor_args():
    sig = inspect.signature(org_k1s_nppn_PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_pragmatic_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Pragmatic)


def test_org_k1s_nppn_pragmatic_constructor_exists():
    assert callable(org_k1s_nppn_Pragmatic.__init__)


def test_org_k1s_nppn_pragmatic_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Pragmatic.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_org_k1s_nppn_pragmatic_has_name():
    assert hasattr(org_k1s_nppn_Pragmatic, "name")
    descriptor = None
    for klass in org_k1s_nppn_Pragmatic.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_org_k1s_nppn_transitionnode_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_TransitionNode)


def test_org_k1s_nppn_transitionnode_constructor_exists():
    assert callable(org_k1s_nppn_TransitionNode.__init__)


def test_org_k1s_nppn_transitionnode_constructor_args():
    sig = inspect.signature(org_k1s_nppn_TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_nppn_transitionnode_is_not_abstract():
    assert not inspect.isabstract(nppn_TransitionNode)


def test_nppn_transitionnode_constructor_exists():
    assert callable(nppn_TransitionNode.__init__)


def test_nppn_transitionnode_constructor_args():
    sig = inspect.signature(nppn_TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_transitionnode_is_not_abstract():
    assert not inspect.isabstract(TransitionNode)


def test_transitionnode_constructor_exists():
    assert callable(TransitionNode.__init__)


def test_transitionnode_constructor_args():
    sig = inspect.signature(TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_transition_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_Transition)


def test_org_k1s_nppn_transition_constructor_exists():
    assert callable(org_k1s_nppn_Transition.__init__)


def test_org_k1s_nppn_transition_constructor_args():
    sig = inspect.signature(org_k1s_nppn_Transition.__init__)
    params = list(sig.parameters.keys())



def test_org_k1s_nppn_reftrans_is_not_abstract():
    assert not inspect.isabstract(org_k1s_nppn_RefTrans)


def test_org_k1s_nppn_reftrans_constructor_exists():
    assert callable(org_k1s_nppn_RefTrans.__init__)


def test_org_k1s_nppn_reftrans_constructor_args():
    sig = inspect.signature(org_k1s_nppn_RefTrans.__init__)
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
nppn_Place_strategy = st.builds(
    nppn_Place,
)
nppn_RefPlace_strategy = st.builds(
    nppn_RefPlace,
)
PlaceNode_strategy = st.builds(
    PlaceNode,
)
org_k1s_nppn_RefPlace_strategy = st.builds(
    org_k1s_nppn_RefPlace,
)
org_k1s_nppn_Place_strategy = st.builds(
    org_k1s_nppn_Place,
)
nppn_Monitor_strategy = st.builds(
    nppn_Monitor,
)
nppn_Object_strategy = st.builds(
    nppn_Object,
)
nppn_PetriNet_strategy = st.builds(
    nppn_PetriNet,
)
HasName_strategy = st.builds(
    HasName,
)
HasLabel_strategy = st.builds(
    HasLabel,
)
org_k1s_nppn_Page_strategy = st.builds(
    org_k1s_nppn_Page,
)
org_k1s_nppn_PetriNet_strategy = st.builds(
    org_k1s_nppn_PetriNet,
    kind=
        safe_text,
    timeType=
        safe_text
)
org_k1s_nppn_Label_strategy = st.builds(
    org_k1s_nppn_Label,
)
nppn_Pragmatic_strategy = st.builds(
    nppn_Pragmatic,
)
nppn_Arc_strategy = st.builds(
    nppn_Arc,
)
Object_strategy = st.builds(
    Object,
)
org_k1s_nppn_Node_strategy = st.builds(
    org_k1s_nppn_Node,
)
HLAnnotation_strategy = st.builds(
    HLAnnotation,
)
org_k1s_nppn_Name_strategy = st.builds(
    org_k1s_nppn_Name,
)
nppn_HasLabel_strategy = st.builds(
    nppn_HasLabel,
)
nppn_HLAnnotation_strategy = st.builds(
    nppn_HLAnnotation,
)
org_k1s_nppn_HLArcAddin_strategy = st.builds(
    org_k1s_nppn_HLArcAddin,
    kind=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
org_k1s_nppn_HLAnnotation_strategy = st.builds(
    org_k1s_nppn_HLAnnotation,
)
org_k1s_nppn_Instance_strategy = st.builds(
    org_k1s_nppn_Instance,
    subPageID=
        safe_text
)
nppn_Page_strategy = st.builds(
    nppn_Page,
)
nppn_Name_strategy = st.builds(
    nppn_Name,
)
org_k1s_nppn_HasName_strategy = st.builds(
    org_k1s_nppn_HasName,
)
nppn_Label_strategy = st.builds(
    nppn_Label,
)
org_k1s_nppn_HasLabel_strategy = st.builds(
    org_k1s_nppn_HasLabel,
)
nppn_Node_strategy = st.builds(
    nppn_Node,
)
HLArcAddin_strategy = st.builds(
    HLArcAddin,
)
HasGraphics_strategy = st.builds(
    HasGraphics,
)
org_k1s_nppn_Object_strategy = st.builds(
    org_k1s_nppn_Object,
)
org_k1s_nppn_Arc_strategy = st.builds(
    org_k1s_nppn_Arc,
)
nppn_Binding_strategy = st.builds(
    nppn_Binding,
)
org_k1s_nppn_Bindings_strategy = st.builds(
    org_k1s_nppn_Bindings,
)
Container_strategy = st.builds(
    Container,
)
org_k1s_nppn_Conditinoal_strategy = st.builds(
    org_k1s_nppn_Conditinoal,
)
org_k1s_nppn_Conditional_strategy = st.builds(
    org_k1s_nppn_Conditional,
)
org_k1s_nppn_Loop_strategy = st.builds(
    org_k1s_nppn_Loop,
)
Block_strategy = st.builds(
    Block,
)
org_k1s_nppn_Atomic_strategy = st.builds(
    org_k1s_nppn_Atomic,
)
org_k1s_nppn_Binding_strategy = st.builds(
    org_k1s_nppn_Binding,
    template=
        safe_text
)
org_k1s_nppn_Container_strategy = st.builds(
    org_k1s_nppn_Container,
)
nppn_Transition_strategy = st.builds(
    nppn_Transition,
)
nppn_PlaceNode_strategy = st.builds(
    nppn_PlaceNode,
)
org_k1s_nppn_Block_strategy = st.builds(
    org_k1s_nppn_Block,
)
nppn_Block_strategy = st.builds(
    nppn_Block,
)
org_k1s_nppn_Service_strategy = st.builds(
    org_k1s_nppn_Service,
)
nppn_Service_strategy = st.builds(
    nppn_Service,
)
nppn_Instance_strategy = st.builds(
    nppn_Instance,
)
org_k1s_nppn_Principal_strategy = st.builds(
    org_k1s_nppn_Principal,
)
org_k1s_nppn_PlacementConstraints_strategy = st.builds(
    org_k1s_nppn_PlacementConstraints,
)
nppn_Principal_strategy = st.builds(
    nppn_Principal,
)
org_k1s_nppn_AbstractTemplateTree_strategy = st.builds(
    org_k1s_nppn_AbstractTemplateTree,
)
Explicit_strategy = st.builds(
    Explicit,
)
CustomPragmatics_strategy = st.builds(
    CustomPragmatics,
)
org_k1s_nppn_CustomExplicitPragmatics_strategy = st.builds(
    org_k1s_nppn_CustomExplicitPragmatics,
)
Derived_strategy = st.builds(
    Derived,
)
org_k1s_nppn_CustomDerivedPragmatics_strategy = st.builds(
    org_k1s_nppn_CustomDerivedPragmatics,
)
nppn_PlacementConstraints_strategy = st.builds(
    nppn_PlacementConstraints,
)
org_k1s_nppn_PNPattern_strategy = st.builds(
    org_k1s_nppn_PNPattern,
)
nppn_PNPattern_strategy = st.builds(
    nppn_PNPattern,
)
Pragmatic_strategy = st.builds(
    Pragmatic,
)
org_k1s_nppn_CustomPragmatics_strategy = st.builds(
    org_k1s_nppn_CustomPragmatics,
)
org_k1s_nppn_Explicit_strategy = st.builds(
    org_k1s_nppn_Explicit,
)
org_k1s_nppn_Derived_strategy = st.builds(
    org_k1s_nppn_Derived,
)
org_k1s_nppn_PlaceNode_strategy = st.builds(
    org_k1s_nppn_PlaceNode,
)
org_k1s_nppn_Pragmatic_strategy = st.builds(
    org_k1s_nppn_Pragmatic,
    name=
        safe_text
)
org_k1s_nppn_TransitionNode_strategy = st.builds(
    org_k1s_nppn_TransitionNode,
)
nppn_TransitionNode_strategy = st.builds(
    nppn_TransitionNode,
)
TransitionNode_strategy = st.builds(
    TransitionNode,
)
org_k1s_nppn_Transition_strategy = st.builds(
    org_k1s_nppn_Transition,
)
org_k1s_nppn_RefTrans_strategy = st.builds(
    org_k1s_nppn_RefTrans,
)

@given(instance=nppn_Place_strategy)
@settings(max_examples=50)
def test_nppn_place_instantiation(instance):
    assert isinstance(instance, nppn_Place)

@given(instance=nppn_RefPlace_strategy)
@settings(max_examples=50)
def test_nppn_refplace_instantiation(instance):
    assert isinstance(instance, nppn_RefPlace)

@given(instance=PlaceNode_strategy)
@settings(max_examples=50)
def test_placenode_instantiation(instance):
    assert isinstance(instance, PlaceNode)

@given(instance=org_k1s_nppn_RefPlace_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_refplace_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_RefPlace)

@given(instance=org_k1s_nppn_Place_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_place_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Place)

@given(instance=nppn_Monitor_strategy)
@settings(max_examples=50)
def test_nppn_monitor_instantiation(instance):
    assert isinstance(instance, nppn_Monitor)

@given(instance=nppn_Object_strategy)
@settings(max_examples=50)
def test_nppn_object_instantiation(instance):
    assert isinstance(instance, nppn_Object)

@given(instance=nppn_PetriNet_strategy)
@settings(max_examples=50)
def test_nppn_petrinet_instantiation(instance):
    assert isinstance(instance, nppn_PetriNet)

@given(instance=HasName_strategy)
@settings(max_examples=50)
def test_hasname_instantiation(instance):
    assert isinstance(instance, HasName)

@given(instance=HasLabel_strategy)
@settings(max_examples=50)
def test_haslabel_instantiation(instance):
    assert isinstance(instance, HasLabel)

@given(instance=org_k1s_nppn_Page_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_page_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Page)

@given(instance=org_k1s_nppn_PetriNet_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_petrinet_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_PetriNet)



@given(instance=org_k1s_nppn_PetriNet_strategy)
def test_org_k1s_nppn_petrinet_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=org_k1s_nppn_PetriNet_strategy)
def test_org_k1s_nppn_petrinet_timeType_setter(instance):
    original = instance.timeType
    instance.timeType = original
    assert instance.timeType == original

@given(instance=org_k1s_nppn_Label_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_label_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Label)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=org_k1s_nppn_Label_strategy)
@settings(max_examples=30)
def test_org_k1s_nppn_label_asstring_changes_state(instance):
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
        assert has_statements, f"Function 'asString' in org_k1s_nppn_Label is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'asString' in org_k1s_nppn_Label did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'asString' in org_k1s_nppn_Label is not implemented or raised an error")

@given(instance=nppn_Pragmatic_strategy)
@settings(max_examples=50)
def test_nppn_pragmatic_instantiation(instance):
    assert isinstance(instance, nppn_Pragmatic)

@given(instance=nppn_Arc_strategy)
@settings(max_examples=50)
def test_nppn_arc_instantiation(instance):
    assert isinstance(instance, nppn_Arc)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=org_k1s_nppn_Node_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_node_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Node)

@given(instance=HLAnnotation_strategy)
@settings(max_examples=50)
def test_hlannotation_instantiation(instance):
    assert isinstance(instance, HLAnnotation)

@given(instance=org_k1s_nppn_Name_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_name_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Name)

@given(instance=nppn_HasLabel_strategy)
@settings(max_examples=50)
def test_nppn_haslabel_instantiation(instance):
    assert isinstance(instance, nppn_HasLabel)

@given(instance=nppn_HLAnnotation_strategy)
@settings(max_examples=50)
def test_nppn_hlannotation_instantiation(instance):
    assert isinstance(instance, nppn_HLAnnotation)

@given(instance=org_k1s_nppn_HLArcAddin_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_hlarcaddin_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_HLArcAddin)



@given(instance=org_k1s_nppn_HLArcAddin_strategy)
def test_org_k1s_nppn_hlarcaddin_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=org_k1s_nppn_HLAnnotation_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_hlannotation_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_HLAnnotation)

@given(instance=org_k1s_nppn_Instance_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_instance_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Instance)



@given(instance=org_k1s_nppn_Instance_strategy)
def test_org_k1s_nppn_instance_subPageID_setter(instance):
    original = instance.subPageID
    instance.subPageID = original
    assert instance.subPageID == original

@given(instance=nppn_Page_strategy)
@settings(max_examples=50)
def test_nppn_page_instantiation(instance):
    assert isinstance(instance, nppn_Page)

@given(instance=nppn_Name_strategy)
@settings(max_examples=50)
def test_nppn_name_instantiation(instance):
    assert isinstance(instance, nppn_Name)

@given(instance=org_k1s_nppn_HasName_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_hasname_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_HasName)

@given(instance=nppn_Label_strategy)
@settings(max_examples=50)
def test_nppn_label_instantiation(instance):
    assert isinstance(instance, nppn_Label)

@given(instance=org_k1s_nppn_HasLabel_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_haslabel_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_HasLabel)

@given(instance=nppn_Node_strategy)
@settings(max_examples=50)
def test_nppn_node_instantiation(instance):
    assert isinstance(instance, nppn_Node)

@given(instance=HLArcAddin_strategy)
@settings(max_examples=50)
def test_hlarcaddin_instantiation(instance):
    assert isinstance(instance, HLArcAddin)

@given(instance=HasGraphics_strategy)
@settings(max_examples=50)
def test_hasgraphics_instantiation(instance):
    assert isinstance(instance, HasGraphics)

@given(instance=org_k1s_nppn_Object_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_object_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Object)

@given(instance=org_k1s_nppn_Arc_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_arc_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Arc)

@given(instance=nppn_Binding_strategy)
@settings(max_examples=50)
def test_nppn_binding_instantiation(instance):
    assert isinstance(instance, nppn_Binding)

@given(instance=org_k1s_nppn_Bindings_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_bindings_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Bindings)

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=org_k1s_nppn_Conditinoal_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_conditinoal_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Conditinoal)

@given(instance=org_k1s_nppn_Conditional_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_conditional_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Conditional)

@given(instance=org_k1s_nppn_Loop_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_loop_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Loop)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=org_k1s_nppn_Atomic_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_atomic_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Atomic)

@given(instance=org_k1s_nppn_Binding_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_binding_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Binding)



@given(instance=org_k1s_nppn_Binding_strategy)
def test_org_k1s_nppn_binding_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=org_k1s_nppn_Container_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_container_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Container)

@given(instance=nppn_Transition_strategy)
@settings(max_examples=50)
def test_nppn_transition_instantiation(instance):
    assert isinstance(instance, nppn_Transition)

@given(instance=nppn_PlaceNode_strategy)
@settings(max_examples=50)
def test_nppn_placenode_instantiation(instance):
    assert isinstance(instance, nppn_PlaceNode)

@given(instance=org_k1s_nppn_Block_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_block_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Block)

@given(instance=nppn_Block_strategy)
@settings(max_examples=50)
def test_nppn_block_instantiation(instance):
    assert isinstance(instance, nppn_Block)

@given(instance=org_k1s_nppn_Service_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_service_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Service)

@given(instance=nppn_Service_strategy)
@settings(max_examples=50)
def test_nppn_service_instantiation(instance):
    assert isinstance(instance, nppn_Service)

@given(instance=nppn_Instance_strategy)
@settings(max_examples=50)
def test_nppn_instance_instantiation(instance):
    assert isinstance(instance, nppn_Instance)

@given(instance=org_k1s_nppn_Principal_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_principal_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Principal)

@given(instance=org_k1s_nppn_PlacementConstraints_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_placementconstraints_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_PlacementConstraints)

@given(instance=nppn_Principal_strategy)
@settings(max_examples=50)
def test_nppn_principal_instantiation(instance):
    assert isinstance(instance, nppn_Principal)

@given(instance=org_k1s_nppn_AbstractTemplateTree_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_abstracttemplatetree_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_AbstractTemplateTree)

@given(instance=Explicit_strategy)
@settings(max_examples=50)
def test_explicit_instantiation(instance):
    assert isinstance(instance, Explicit)

@given(instance=CustomPragmatics_strategy)
@settings(max_examples=50)
def test_custompragmatics_instantiation(instance):
    assert isinstance(instance, CustomPragmatics)

@given(instance=org_k1s_nppn_CustomExplicitPragmatics_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_customexplicitpragmatics_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_CustomExplicitPragmatics)

@given(instance=Derived_strategy)
@settings(max_examples=50)
def test_derived_instantiation(instance):
    assert isinstance(instance, Derived)

@given(instance=org_k1s_nppn_CustomDerivedPragmatics_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_customderivedpragmatics_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_CustomDerivedPragmatics)

@given(instance=nppn_PlacementConstraints_strategy)
@settings(max_examples=50)
def test_nppn_placementconstraints_instantiation(instance):
    assert isinstance(instance, nppn_PlacementConstraints)

@given(instance=org_k1s_nppn_PNPattern_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_pnpattern_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_PNPattern)

@given(instance=nppn_PNPattern_strategy)
@settings(max_examples=50)
def test_nppn_pnpattern_instantiation(instance):
    assert isinstance(instance, nppn_PNPattern)

@given(instance=Pragmatic_strategy)
@settings(max_examples=50)
def test_pragmatic_instantiation(instance):
    assert isinstance(instance, Pragmatic)

@given(instance=org_k1s_nppn_CustomPragmatics_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_custompragmatics_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_CustomPragmatics)

@given(instance=org_k1s_nppn_Explicit_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_explicit_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Explicit)

@given(instance=org_k1s_nppn_Derived_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_derived_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Derived)

@given(instance=org_k1s_nppn_PlaceNode_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_placenode_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_PlaceNode)

@given(instance=org_k1s_nppn_Pragmatic_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_pragmatic_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Pragmatic)



@given(instance=org_k1s_nppn_Pragmatic_strategy)
def test_org_k1s_nppn_pragmatic_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=org_k1s_nppn_TransitionNode_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_transitionnode_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_TransitionNode)

@given(instance=nppn_TransitionNode_strategy)
@settings(max_examples=50)
def test_nppn_transitionnode_instantiation(instance):
    assert isinstance(instance, nppn_TransitionNode)

@given(instance=TransitionNode_strategy)
@settings(max_examples=50)
def test_transitionnode_instantiation(instance):
    assert isinstance(instance, TransitionNode)

@given(instance=org_k1s_nppn_Transition_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_transition_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_Transition)

@given(instance=org_k1s_nppn_RefTrans_strategy)
@settings(max_examples=50)
def test_org_k1s_nppn_reftrans_instantiation(instance):
    assert isinstance(instance, org_k1s_nppn_RefTrans)
