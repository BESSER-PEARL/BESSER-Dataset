import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    YasperEPNML114_TransitionSpecific,
    YasperEPNML114_Transformation,
    YasperEPNML114_Roles,
    YasperEPNML114_Role,
    YasperEPNML114_ReferencePlaceSpecific,
    YasperEPNML114_ProcessingTime,
    Place,
    YasperEPNML114_PlaceType,
    YasperEPNML114_Place,
    YasperEPNML114_TransitionType,
    YasperEPNML114_ReferencePlace,
    YasperEPNML114_NodeGraphics,
    YasperEPNML114_Page,
    YasperEPNML114_Transition,
    YasperEPNML114_Net,
    YasperEPNML114_PlaceType1,
    YasperEPNML114_NetGraphics,
    YasperEPNML114_InitialMarking,
    YasperEPNML114_DocumentRoot,
    YasperEPNML114_Cost,
    YasperEPNML114_Pnml,
    YasperEPNML114_EStringToStringMapEntry,
    YasperEPNML114_ConnectionWeight,
    YasperEPNML114_ConnectionWeights,
    YasperEPNML114_Stat,
    YasperEPNML114_PnmlAnnotation,
    YasperEPNML114_Inscription,
    YasperEPNML114_EdgeGraphics,
    YasperEPNML114_ToolspecificType,
    YasperEPNML114_TwoDimVector,
    YasperEPNML114_AnnotationGraphics,
    YasperEPNML114_ArcType,
    YasperEPNML114_Arc,
    Version,
    Tool,
    TextType2,
    TextType1,
    TextTypeMember0,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yasperepnml114_transitionspecific_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_TransitionSpecific)


def test_yasperepnml114_transitionspecific_constructor_exists():
    assert callable(YasperEPNML114_TransitionSpecific.__init__)


def test_yasperepnml114_transitionspecific_constructor_args():
    sig = inspect.signature(YasperEPNML114_TransitionSpecific.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "tool" in params, "Missing parameter 'tool'"
    assert "tokenCaseSensitive" in params, "Missing parameter 'tokenCaseSensitive'"

def test_yasperepnml114_transitionspecific_has_version():
    assert hasattr(YasperEPNML114_TransitionSpecific, "version")
    descriptor = None
    for klass in YasperEPNML114_TransitionSpecific.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_transitionspecific_has_tool():
    assert hasattr(YasperEPNML114_TransitionSpecific, "tool")
    descriptor = None
    for klass in YasperEPNML114_TransitionSpecific.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_transitionspecific_has_tokenCaseSensitive():
    assert hasattr(YasperEPNML114_TransitionSpecific, "tokenCaseSensitive")
    descriptor = None
    for klass in YasperEPNML114_TransitionSpecific.__mro__:
        if "tokenCaseSensitive" in klass.__dict__:
            descriptor = klass.__dict__["tokenCaseSensitive"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_transformation_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Transformation)


def test_yasperepnml114_transformation_constructor_exists():
    assert callable(YasperEPNML114_Transformation.__init__)


def test_yasperepnml114_transformation_constructor_args():
    sig = inspect.signature(YasperEPNML114_Transformation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114_transformation_has_text():
    assert hasattr(YasperEPNML114_Transformation, "text")
    descriptor = None
    for klass in YasperEPNML114_Transformation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_roles_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Roles)


def test_yasperepnml114_roles_constructor_exists():
    assert callable(YasperEPNML114_Roles.__init__)


def test_yasperepnml114_roles_constructor_args():
    sig = inspect.signature(YasperEPNML114_Roles.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114_role_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Role)


def test_yasperepnml114_role_constructor_exists():
    assert callable(YasperEPNML114_Role.__init__)


def test_yasperepnml114_role_constructor_args():
    sig = inspect.signature(YasperEPNML114_Role.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114_role_has_text():
    assert hasattr(YasperEPNML114_Role, "text")
    descriptor = None
    for klass in YasperEPNML114_Role.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_referenceplacespecific_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ReferencePlaceSpecific)


def test_yasperepnml114_referenceplacespecific_constructor_exists():
    assert callable(YasperEPNML114_ReferencePlaceSpecific.__init__)


def test_yasperepnml114_referenceplacespecific_constructor_args():
    sig = inspect.signature(YasperEPNML114_ReferencePlaceSpecific.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "tool" in params, "Missing parameter 'tool'"

def test_yasperepnml114_referenceplacespecific_has_version():
    assert hasattr(YasperEPNML114_ReferencePlaceSpecific, "version")
    descriptor = None
    for klass in YasperEPNML114_ReferencePlaceSpecific.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_referenceplacespecific_has_tool():
    assert hasattr(YasperEPNML114_ReferencePlaceSpecific, "tool")
    descriptor = None
    for klass in YasperEPNML114_ReferencePlaceSpecific.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_processingtime_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ProcessingTime)


def test_yasperepnml114_processingtime_constructor_exists():
    assert callable(YasperEPNML114_ProcessingTime.__init__)


def test_yasperepnml114_processingtime_constructor_args():
    sig = inspect.signature(YasperEPNML114_ProcessingTime.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114_placetype_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_PlaceType)


def test_yasperepnml114_placetype_constructor_exists():
    assert callable(YasperEPNML114_PlaceType.__init__)


def test_yasperepnml114_placetype_constructor_args():
    sig = inspect.signature(YasperEPNML114_PlaceType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114_placetype_has_text():
    assert hasattr(YasperEPNML114_PlaceType, "text")
    descriptor = None
    for klass in YasperEPNML114_PlaceType.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_place_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Place)


def test_yasperepnml114_place_constructor_exists():
    assert callable(YasperEPNML114_Place.__init__)


def test_yasperepnml114_place_constructor_args():
    sig = inspect.signature(YasperEPNML114_Place.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114_place_has_id():
    assert hasattr(YasperEPNML114_Place, "id")
    descriptor = None
    for klass in YasperEPNML114_Place.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_place_has_group():
    assert hasattr(YasperEPNML114_Place, "group")
    descriptor = None
    for klass in YasperEPNML114_Place.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_transitiontype_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_TransitionType)


def test_yasperepnml114_transitiontype_constructor_exists():
    assert callable(YasperEPNML114_TransitionType.__init__)


def test_yasperepnml114_transitiontype_constructor_args():
    sig = inspect.signature(YasperEPNML114_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114_transitiontype_has_text():
    assert hasattr(YasperEPNML114_TransitionType, "text")
    descriptor = None
    for klass in YasperEPNML114_TransitionType.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_referenceplace_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ReferencePlace)


def test_yasperepnml114_referenceplace_constructor_exists():
    assert callable(YasperEPNML114_ReferencePlace.__init__)


def test_yasperepnml114_referenceplace_constructor_args():
    sig = inspect.signature(YasperEPNML114_ReferencePlace.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "ref" in params, "Missing parameter 'ref'"
    assert "id" in params, "Missing parameter 'id'"

def test_yasperepnml114_referenceplace_has_group():
    assert hasattr(YasperEPNML114_ReferencePlace, "group")
    descriptor = None
    for klass in YasperEPNML114_ReferencePlace.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_referenceplace_has_ref():
    assert hasattr(YasperEPNML114_ReferencePlace, "ref")
    descriptor = None
    for klass in YasperEPNML114_ReferencePlace.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_referenceplace_has_id():
    assert hasattr(YasperEPNML114_ReferencePlace, "id")
    descriptor = None
    for klass in YasperEPNML114_ReferencePlace.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_nodegraphics_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_NodeGraphics)


def test_yasperepnml114_nodegraphics_constructor_exists():
    assert callable(YasperEPNML114_NodeGraphics.__init__)


def test_yasperepnml114_nodegraphics_constructor_args():
    sig = inspect.signature(YasperEPNML114_NodeGraphics.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114_nodegraphics_has_group():
    assert hasattr(YasperEPNML114_NodeGraphics, "group")
    descriptor = None
    for klass in YasperEPNML114_NodeGraphics.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_page_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Page)


def test_yasperepnml114_page_constructor_exists():
    assert callable(YasperEPNML114_Page.__init__)


def test_yasperepnml114_page_constructor_args():
    sig = inspect.signature(YasperEPNML114_Page.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "id" in params, "Missing parameter 'id'"

def test_yasperepnml114_page_has_group():
    assert hasattr(YasperEPNML114_Page, "group")
    descriptor = None
    for klass in YasperEPNML114_Page.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_page_has_id():
    assert hasattr(YasperEPNML114_Page, "id")
    descriptor = None
    for klass in YasperEPNML114_Page.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_transition_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Transition)


def test_yasperepnml114_transition_constructor_exists():
    assert callable(YasperEPNML114_Transition.__init__)


def test_yasperepnml114_transition_constructor_args():
    sig = inspect.signature(YasperEPNML114_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114_transition_has_id():
    assert hasattr(YasperEPNML114_Transition, "id")
    descriptor = None
    for klass in YasperEPNML114_Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_transition_has_group():
    assert hasattr(YasperEPNML114_Transition, "group")
    descriptor = None
    for klass in YasperEPNML114_Transition.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_net_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Net)


def test_yasperepnml114_net_constructor_exists():
    assert callable(YasperEPNML114_Net.__init__)


def test_yasperepnml114_net_constructor_args():
    sig = inspect.signature(YasperEPNML114_Net.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"

def test_yasperepnml114_net_has_group():
    assert hasattr(YasperEPNML114_Net, "group")
    descriptor = None
    for klass in YasperEPNML114_Net.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_net_has_id():
    assert hasattr(YasperEPNML114_Net, "id")
    descriptor = None
    for klass in YasperEPNML114_Net.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_net_has_type():
    assert hasattr(YasperEPNML114_Net, "type")
    descriptor = None
    for klass in YasperEPNML114_Net.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_placetype1_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_PlaceType1)


def test_yasperepnml114_placetype1_constructor_exists():
    assert callable(YasperEPNML114_PlaceType1.__init__)


def test_yasperepnml114_placetype1_constructor_args():
    sig = inspect.signature(YasperEPNML114_PlaceType1.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114_netgraphics_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_NetGraphics)


def test_yasperepnml114_netgraphics_constructor_exists():
    assert callable(YasperEPNML114_NetGraphics.__init__)


def test_yasperepnml114_netgraphics_constructor_args():
    sig = inspect.signature(YasperEPNML114_NetGraphics.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114_netgraphics_has_group():
    assert hasattr(YasperEPNML114_NetGraphics, "group")
    descriptor = None
    for klass in YasperEPNML114_NetGraphics.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_initialmarking_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_InitialMarking)


def test_yasperepnml114_initialmarking_constructor_exists():
    assert callable(YasperEPNML114_InitialMarking.__init__)


def test_yasperepnml114_initialmarking_constructor_args():
    sig = inspect.signature(YasperEPNML114_InitialMarking.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114_initialmarking_has_text():
    assert hasattr(YasperEPNML114_InitialMarking, "text")
    descriptor = None
    for klass in YasperEPNML114_InitialMarking.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_documentroot_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_DocumentRoot)


def test_yasperepnml114_documentroot_constructor_exists():
    assert callable(YasperEPNML114_DocumentRoot.__init__)


def test_yasperepnml114_documentroot_constructor_args():
    sig = inspect.signature(YasperEPNML114_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_yasperepnml114_documentroot_has_mixed():
    assert hasattr(YasperEPNML114_DocumentRoot, "mixed")
    descriptor = None
    for klass in YasperEPNML114_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_cost_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Cost)


def test_yasperepnml114_cost_constructor_exists():
    assert callable(YasperEPNML114_Cost.__init__)


def test_yasperepnml114_cost_constructor_args():
    sig = inspect.signature(YasperEPNML114_Cost.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114_pnml_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Pnml)


def test_yasperepnml114_pnml_constructor_exists():
    assert callable(YasperEPNML114_Pnml.__init__)


def test_yasperepnml114_pnml_constructor_args():
    sig = inspect.signature(YasperEPNML114_Pnml.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114_pnml_has_group():
    assert hasattr(YasperEPNML114_Pnml, "group")
    descriptor = None
    for klass in YasperEPNML114_Pnml.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_EStringToStringMapEntry)


def test_yasperepnml114_estringtostringmapentry_constructor_exists():
    assert callable(YasperEPNML114_EStringToStringMapEntry.__init__)


def test_yasperepnml114_estringtostringmapentry_constructor_args():
    sig = inspect.signature(YasperEPNML114_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114_connectionweight_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ConnectionWeight)


def test_yasperepnml114_connectionweight_constructor_exists():
    assert callable(YasperEPNML114_ConnectionWeight.__init__)


def test_yasperepnml114_connectionweight_constructor_args():
    sig = inspect.signature(YasperEPNML114_ConnectionWeight.__init__)
    params = list(sig.parameters.keys())
    assert "connection" in params, "Missing parameter 'connection'"

def test_yasperepnml114_connectionweight_has_connection():
    assert hasattr(YasperEPNML114_ConnectionWeight, "connection")
    descriptor = None
    for klass in YasperEPNML114_ConnectionWeight.__mro__:
        if "connection" in klass.__dict__:
            descriptor = klass.__dict__["connection"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_connectionweights_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ConnectionWeights)


def test_yasperepnml114_connectionweights_constructor_exists():
    assert callable(YasperEPNML114_ConnectionWeights.__init__)


def test_yasperepnml114_connectionweights_constructor_args():
    sig = inspect.signature(YasperEPNML114_ConnectionWeights.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114_stat_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Stat)


def test_yasperepnml114_stat_constructor_exists():
    assert callable(YasperEPNML114_Stat.__init__)


def test_yasperepnml114_stat_constructor_args():
    sig = inspect.signature(YasperEPNML114_Stat.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114_stat_has_text():
    assert hasattr(YasperEPNML114_Stat, "text")
    descriptor = None
    for klass in YasperEPNML114_Stat.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_pnmlannotation_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_PnmlAnnotation)


def test_yasperepnml114_pnmlannotation_constructor_exists():
    assert callable(YasperEPNML114_PnmlAnnotation.__init__)


def test_yasperepnml114_pnmlannotation_constructor_args():
    sig = inspect.signature(YasperEPNML114_PnmlAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114_pnmlannotation_has_text():
    assert hasattr(YasperEPNML114_PnmlAnnotation, "text")
    descriptor = None
    for klass in YasperEPNML114_PnmlAnnotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_inscription_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Inscription)


def test_yasperepnml114_inscription_constructor_exists():
    assert callable(YasperEPNML114_Inscription.__init__)


def test_yasperepnml114_inscription_constructor_args():
    sig = inspect.signature(YasperEPNML114_Inscription.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114_inscription_has_text():
    assert hasattr(YasperEPNML114_Inscription, "text")
    descriptor = None
    for klass in YasperEPNML114_Inscription.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_edgegraphics_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_EdgeGraphics)


def test_yasperepnml114_edgegraphics_constructor_exists():
    assert callable(YasperEPNML114_EdgeGraphics.__init__)


def test_yasperepnml114_edgegraphics_constructor_args():
    sig = inspect.signature(YasperEPNML114_EdgeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114_toolspecifictype_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ToolspecificType)


def test_yasperepnml114_toolspecifictype_constructor_exists():
    assert callable(YasperEPNML114_ToolspecificType.__init__)


def test_yasperepnml114_toolspecifictype_constructor_args():
    sig = inspect.signature(YasperEPNML114_ToolspecificType.__init__)
    params = list(sig.parameters.keys())
    assert "tool" in params, "Missing parameter 'tool'"
    assert "version" in params, "Missing parameter 'version'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "any" in params, "Missing parameter 'any'"
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114_toolspecifictype_has_tool():
    assert hasattr(YasperEPNML114_ToolspecificType, "tool")
    descriptor = None
    for klass in YasperEPNML114_ToolspecificType.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_toolspecifictype_has_version():
    assert hasattr(YasperEPNML114_ToolspecificType, "version")
    descriptor = None
    for klass in YasperEPNML114_ToolspecificType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_toolspecifictype_has_mixed():
    assert hasattr(YasperEPNML114_ToolspecificType, "mixed")
    descriptor = None
    for klass in YasperEPNML114_ToolspecificType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_toolspecifictype_has_any():
    assert hasattr(YasperEPNML114_ToolspecificType, "any")
    descriptor = None
    for klass in YasperEPNML114_ToolspecificType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_toolspecifictype_has_group():
    assert hasattr(YasperEPNML114_ToolspecificType, "group")
    descriptor = None
    for klass in YasperEPNML114_ToolspecificType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_twodimvector_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_TwoDimVector)


def test_yasperepnml114_twodimvector_constructor_exists():
    assert callable(YasperEPNML114_TwoDimVector.__init__)


def test_yasperepnml114_twodimvector_constructor_args():
    sig = inspect.signature(YasperEPNML114_TwoDimVector.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_yasperepnml114_twodimvector_has_y():
    assert hasattr(YasperEPNML114_TwoDimVector, "y")
    descriptor = None
    for klass in YasperEPNML114_TwoDimVector.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_twodimvector_has_x():
    assert hasattr(YasperEPNML114_TwoDimVector, "x")
    descriptor = None
    for klass in YasperEPNML114_TwoDimVector.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_AnnotationGraphics)


def test_yasperepnml114_annotationgraphics_constructor_exists():
    assert callable(YasperEPNML114_AnnotationGraphics.__init__)


def test_yasperepnml114_annotationgraphics_constructor_args():
    sig = inspect.signature(YasperEPNML114_AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114_arctype_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_ArcType)


def test_yasperepnml114_arctype_constructor_exists():
    assert callable(YasperEPNML114_ArcType.__init__)


def test_yasperepnml114_arctype_constructor_args():
    sig = inspect.signature(YasperEPNML114_ArcType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114_arctype_has_text():
    assert hasattr(YasperEPNML114_ArcType, "text")
    descriptor = None
    for klass in YasperEPNML114_ArcType.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114_arc_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114_Arc)


def test_yasperepnml114_arc_constructor_exists():
    assert callable(YasperEPNML114_Arc.__init__)


def test_yasperepnml114_arc_constructor_args():
    sig = inspect.signature(YasperEPNML114_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "target" in params, "Missing parameter 'target'"
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114_arc_has_source():
    assert hasattr(YasperEPNML114_Arc, "source")
    descriptor = None
    for klass in YasperEPNML114_Arc.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_arc_has_target():
    assert hasattr(YasperEPNML114_Arc, "target")
    descriptor = None
    for klass in YasperEPNML114_Arc.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_arc_has_id():
    assert hasattr(YasperEPNML114_Arc, "id")
    descriptor = None
    for klass in YasperEPNML114_Arc.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114_arc_has_group():
    assert hasattr(YasperEPNML114_Arc, "group")
    descriptor = None
    for klass in YasperEPNML114_Arc.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_version_exists():
    # Check that the Enumeration exists
    assert Version is not None

def test_version_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Version]
    expected_literals = [
        "_1",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Version"

def test_tool_exists():
    # Check that the Enumeration exists
    assert Tool is not None

def test_tool_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Tool]
    expected_literals = [
        "Yasper",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Tool"

def test_texttype2_exists():
    # Check that the Enumeration exists
    assert TextType2 is not None

def test_texttype2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextType2]
    expected_literals = [
        "channel",
        "store",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextType2"

def test_texttype1_exists():
    # Check that the Enumeration exists
    assert TextType1 is not None

def test_texttype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextType1]
    expected_literals = [
        "AND",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextType1"

def test_texttypemember0_exists():
    # Check that the Enumeration exists
    assert TextTypeMember0 is not None

def test_texttypemember0_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextTypeMember0]
    expected_literals = [
        "reset",
        "inhibitor",
        "inflow",
        "outflow",
        "biflow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextTypeMember0"


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
YasperEPNML114_TransitionSpecific_strategy = st.builds(
    YasperEPNML114_TransitionSpecific,
    version=
        safe_text,
    tool=
        safe_text,
    tokenCaseSensitive=
        safe_text
)
YasperEPNML114_Transformation_strategy = st.builds(
    YasperEPNML114_Transformation,
    text=
        safe_text
)
YasperEPNML114_Roles_strategy = st.builds(
    YasperEPNML114_Roles,
)
YasperEPNML114_Role_strategy = st.builds(
    YasperEPNML114_Role,
    text=
        safe_text
)
YasperEPNML114_ReferencePlaceSpecific_strategy = st.builds(
    YasperEPNML114_ReferencePlaceSpecific,
    version=
        safe_text,
    tool=
        safe_text
)
YasperEPNML114_ProcessingTime_strategy = st.builds(
    YasperEPNML114_ProcessingTime,
)
Place_strategy = st.builds(
    Place,
)
YasperEPNML114_PlaceType_strategy = st.builds(
    YasperEPNML114_PlaceType,
    text=
        safe_text
)
YasperEPNML114_Place_strategy = st.builds(
    YasperEPNML114_Place,
    id=
        safe_text,
    group=
        safe_text
)
YasperEPNML114_TransitionType_strategy = st.builds(
    YasperEPNML114_TransitionType,
    text=
        safe_text
)
YasperEPNML114_ReferencePlace_strategy = st.builds(
    YasperEPNML114_ReferencePlace,
    group=
        safe_text,
    ref=
        safe_text,
    id=
        safe_text
)
YasperEPNML114_NodeGraphics_strategy = st.builds(
    YasperEPNML114_NodeGraphics,
    group=
        safe_text
)
YasperEPNML114_Page_strategy = st.builds(
    YasperEPNML114_Page,
    group=
        safe_text,
    id=
        safe_text
)
YasperEPNML114_Transition_strategy = st.builds(
    YasperEPNML114_Transition,
    id=
        safe_text,
    group=
        safe_text
)
YasperEPNML114_Net_strategy = st.builds(
    YasperEPNML114_Net,
    group=
        safe_text,
    id=
        safe_text,
    type=
        safe_text
)
YasperEPNML114_PlaceType1_strategy = st.builds(
    YasperEPNML114_PlaceType1,
)
YasperEPNML114_NetGraphics_strategy = st.builds(
    YasperEPNML114_NetGraphics,
    group=
        safe_text
)
YasperEPNML114_InitialMarking_strategy = st.builds(
    YasperEPNML114_InitialMarking,
    text=
        safe_text
)
YasperEPNML114_DocumentRoot_strategy = st.builds(
    YasperEPNML114_DocumentRoot,
    mixed=
        safe_text
)
YasperEPNML114_Cost_strategy = st.builds(
    YasperEPNML114_Cost,
)
YasperEPNML114_Pnml_strategy = st.builds(
    YasperEPNML114_Pnml,
    group=
        safe_text
)
YasperEPNML114_EStringToStringMapEntry_strategy = st.builds(
    YasperEPNML114_EStringToStringMapEntry,
)
YasperEPNML114_ConnectionWeight_strategy = st.builds(
    YasperEPNML114_ConnectionWeight,
    connection=
        safe_text
)
YasperEPNML114_ConnectionWeights_strategy = st.builds(
    YasperEPNML114_ConnectionWeights,
)
YasperEPNML114_Stat_strategy = st.builds(
    YasperEPNML114_Stat,
    text=
        safe_text
)
YasperEPNML114_PnmlAnnotation_strategy = st.builds(
    YasperEPNML114_PnmlAnnotation,
    text=
        safe_text
)
YasperEPNML114_Inscription_strategy = st.builds(
    YasperEPNML114_Inscription,
    text=
        safe_text
)
YasperEPNML114_EdgeGraphics_strategy = st.builds(
    YasperEPNML114_EdgeGraphics,
)
YasperEPNML114_ToolspecificType_strategy = st.builds(
    YasperEPNML114_ToolspecificType,
    tool=
        safe_text,
    version=
        safe_text,
    mixed=
        safe_text,
    any=
        safe_text,
    group=
        safe_text
)
YasperEPNML114_TwoDimVector_strategy = st.builds(
    YasperEPNML114_TwoDimVector,
    y=
        safe_text,
    x=
        safe_text
)
YasperEPNML114_AnnotationGraphics_strategy = st.builds(
    YasperEPNML114_AnnotationGraphics,
)
YasperEPNML114_ArcType_strategy = st.builds(
    YasperEPNML114_ArcType,
    text=
        safe_text
)
YasperEPNML114_Arc_strategy = st.builds(
    YasperEPNML114_Arc,
    source=
        safe_text,
    target=
        safe_text,
    id=
        safe_text,
    group=
        safe_text
)

@given(instance=YasperEPNML114_TransitionSpecific_strategy)
@settings(max_examples=50)
def test_yasperepnml114_transitionspecific_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_TransitionSpecific)



@given(instance=YasperEPNML114_TransitionSpecific_strategy)
def test_yasperepnml114_transitionspecific_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=YasperEPNML114_TransitionSpecific_strategy)
def test_yasperepnml114_transitionspecific_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original



@given(instance=YasperEPNML114_TransitionSpecific_strategy)
def test_yasperepnml114_transitionspecific_tokenCaseSensitive_setter(instance):
    original = instance.tokenCaseSensitive
    instance.tokenCaseSensitive = original
    assert instance.tokenCaseSensitive == original

@given(instance=YasperEPNML114_Transformation_strategy)
@settings(max_examples=50)
def test_yasperepnml114_transformation_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Transformation)



@given(instance=YasperEPNML114_Transformation_strategy)
def test_yasperepnml114_transformation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114_Roles_strategy)
@settings(max_examples=50)
def test_yasperepnml114_roles_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Roles)

@given(instance=YasperEPNML114_Role_strategy)
@settings(max_examples=50)
def test_yasperepnml114_role_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Role)



@given(instance=YasperEPNML114_Role_strategy)
def test_yasperepnml114_role_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114_ReferencePlaceSpecific_strategy)
@settings(max_examples=50)
def test_yasperepnml114_referenceplacespecific_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ReferencePlaceSpecific)



@given(instance=YasperEPNML114_ReferencePlaceSpecific_strategy)
def test_yasperepnml114_referenceplacespecific_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=YasperEPNML114_ReferencePlaceSpecific_strategy)
def test_yasperepnml114_referenceplacespecific_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=YasperEPNML114_ProcessingTime_strategy)
@settings(max_examples=50)
def test_yasperepnml114_processingtime_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ProcessingTime)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=YasperEPNML114_PlaceType_strategy)
@settings(max_examples=50)
def test_yasperepnml114_placetype_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_PlaceType)



@given(instance=YasperEPNML114_PlaceType_strategy)
def test_yasperepnml114_placetype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114_Place_strategy)
@settings(max_examples=50)
def test_yasperepnml114_place_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Place)



@given(instance=YasperEPNML114_Place_strategy)
def test_yasperepnml114_place_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=YasperEPNML114_Place_strategy)
def test_yasperepnml114_place_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114_TransitionType_strategy)
@settings(max_examples=50)
def test_yasperepnml114_transitiontype_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_TransitionType)



@given(instance=YasperEPNML114_TransitionType_strategy)
def test_yasperepnml114_transitiontype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114_ReferencePlace_strategy)
@settings(max_examples=50)
def test_yasperepnml114_referenceplace_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ReferencePlace)



@given(instance=YasperEPNML114_ReferencePlace_strategy)
def test_yasperepnml114_referenceplace_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=YasperEPNML114_ReferencePlace_strategy)
def test_yasperepnml114_referenceplace_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original



@given(instance=YasperEPNML114_ReferencePlace_strategy)
def test_yasperepnml114_referenceplace_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=YasperEPNML114_NodeGraphics_strategy)
@settings(max_examples=50)
def test_yasperepnml114_nodegraphics_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_NodeGraphics)



@given(instance=YasperEPNML114_NodeGraphics_strategy)
def test_yasperepnml114_nodegraphics_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114_Page_strategy)
@settings(max_examples=50)
def test_yasperepnml114_page_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Page)



@given(instance=YasperEPNML114_Page_strategy)
def test_yasperepnml114_page_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=YasperEPNML114_Page_strategy)
def test_yasperepnml114_page_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=YasperEPNML114_Transition_strategy)
@settings(max_examples=50)
def test_yasperepnml114_transition_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Transition)



@given(instance=YasperEPNML114_Transition_strategy)
def test_yasperepnml114_transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=YasperEPNML114_Transition_strategy)
def test_yasperepnml114_transition_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114_Net_strategy)
@settings(max_examples=50)
def test_yasperepnml114_net_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Net)



@given(instance=YasperEPNML114_Net_strategy)
def test_yasperepnml114_net_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=YasperEPNML114_Net_strategy)
def test_yasperepnml114_net_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=YasperEPNML114_Net_strategy)
def test_yasperepnml114_net_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=YasperEPNML114_PlaceType1_strategy)
@settings(max_examples=50)
def test_yasperepnml114_placetype1_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_PlaceType1)

@given(instance=YasperEPNML114_NetGraphics_strategy)
@settings(max_examples=50)
def test_yasperepnml114_netgraphics_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_NetGraphics)



@given(instance=YasperEPNML114_NetGraphics_strategy)
def test_yasperepnml114_netgraphics_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114_InitialMarking_strategy)
@settings(max_examples=50)
def test_yasperepnml114_initialmarking_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_InitialMarking)



@given(instance=YasperEPNML114_InitialMarking_strategy)
def test_yasperepnml114_initialmarking_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114_DocumentRoot_strategy)
@settings(max_examples=50)
def test_yasperepnml114_documentroot_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_DocumentRoot)



@given(instance=YasperEPNML114_DocumentRoot_strategy)
def test_yasperepnml114_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=YasperEPNML114_Cost_strategy)
@settings(max_examples=50)
def test_yasperepnml114_cost_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Cost)

@given(instance=YasperEPNML114_Pnml_strategy)
@settings(max_examples=50)
def test_yasperepnml114_pnml_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Pnml)



@given(instance=YasperEPNML114_Pnml_strategy)
def test_yasperepnml114_pnml_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_yasperepnml114_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_EStringToStringMapEntry)

@given(instance=YasperEPNML114_ConnectionWeight_strategy)
@settings(max_examples=50)
def test_yasperepnml114_connectionweight_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ConnectionWeight)



@given(instance=YasperEPNML114_ConnectionWeight_strategy)
def test_yasperepnml114_connectionweight_connection_setter(instance):
    original = instance.connection
    instance.connection = original
    assert instance.connection == original

@given(instance=YasperEPNML114_ConnectionWeights_strategy)
@settings(max_examples=50)
def test_yasperepnml114_connectionweights_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ConnectionWeights)

@given(instance=YasperEPNML114_Stat_strategy)
@settings(max_examples=50)
def test_yasperepnml114_stat_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Stat)



@given(instance=YasperEPNML114_Stat_strategy)
def test_yasperepnml114_stat_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114_PnmlAnnotation_strategy)
@settings(max_examples=50)
def test_yasperepnml114_pnmlannotation_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_PnmlAnnotation)



@given(instance=YasperEPNML114_PnmlAnnotation_strategy)
def test_yasperepnml114_pnmlannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114_Inscription_strategy)
@settings(max_examples=50)
def test_yasperepnml114_inscription_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Inscription)



@given(instance=YasperEPNML114_Inscription_strategy)
def test_yasperepnml114_inscription_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114_EdgeGraphics_strategy)
@settings(max_examples=50)
def test_yasperepnml114_edgegraphics_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_EdgeGraphics)

@given(instance=YasperEPNML114_ToolspecificType_strategy)
@settings(max_examples=50)
def test_yasperepnml114_toolspecifictype_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ToolspecificType)



@given(instance=YasperEPNML114_ToolspecificType_strategy)
def test_yasperepnml114_toolspecifictype_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original



@given(instance=YasperEPNML114_ToolspecificType_strategy)
def test_yasperepnml114_toolspecifictype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=YasperEPNML114_ToolspecificType_strategy)
def test_yasperepnml114_toolspecifictype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=YasperEPNML114_ToolspecificType_strategy)
def test_yasperepnml114_toolspecifictype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=YasperEPNML114_ToolspecificType_strategy)
def test_yasperepnml114_toolspecifictype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114_TwoDimVector_strategy)
@settings(max_examples=50)
def test_yasperepnml114_twodimvector_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_TwoDimVector)



@given(instance=YasperEPNML114_TwoDimVector_strategy)
def test_yasperepnml114_twodimvector_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=YasperEPNML114_TwoDimVector_strategy)
def test_yasperepnml114_twodimvector_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=YasperEPNML114_AnnotationGraphics_strategy)
@settings(max_examples=50)
def test_yasperepnml114_annotationgraphics_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_AnnotationGraphics)

@given(instance=YasperEPNML114_ArcType_strategy)
@settings(max_examples=50)
def test_yasperepnml114_arctype_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_ArcType)



@given(instance=YasperEPNML114_ArcType_strategy)
def test_yasperepnml114_arctype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114_Arc_strategy)
@settings(max_examples=50)
def test_yasperepnml114_arc_instantiation(instance):
    assert isinstance(instance, YasperEPNML114_Arc)



@given(instance=YasperEPNML114_Arc_strategy)
def test_yasperepnml114_arc_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=YasperEPNML114_Arc_strategy)
def test_yasperepnml114_arc_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=YasperEPNML114_Arc_strategy)
def test_yasperepnml114_arc_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=YasperEPNML114_Arc_strategy)
def test_yasperepnml114_arc_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original
