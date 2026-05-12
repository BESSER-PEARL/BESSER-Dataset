import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    YasperEPNML114::TransitionSpecific,
    YasperEPNML114::Transformation,
    YasperEPNML114::Roles,
    YasperEPNML114::Role,
    YasperEPNML114::ReferencePlaceSpecific,
    YasperEPNML114::ProcessingTime,
    Place,
    YasperEPNML114::PlaceType,
    YasperEPNML114::Place,
    YasperEPNML114::TransitionType,
    YasperEPNML114::ReferencePlace,
    YasperEPNML114::NodeGraphics,
    YasperEPNML114::Page,
    YasperEPNML114::Transition,
    YasperEPNML114::Net,
    YasperEPNML114::PlaceType1,
    YasperEPNML114::NetGraphics,
    YasperEPNML114::InitialMarking,
    YasperEPNML114::DocumentRoot,
    YasperEPNML114::Cost,
    YasperEPNML114::Pnml,
    YasperEPNML114::EStringToStringMapEntry,
    YasperEPNML114::ConnectionWeight,
    YasperEPNML114::ConnectionWeights,
    YasperEPNML114::Stat,
    YasperEPNML114::PnmlAnnotation,
    YasperEPNML114::Inscription,
    YasperEPNML114::EdgeGraphics,
    YasperEPNML114::ToolspecificType,
    YasperEPNML114::TwoDimVector,
    YasperEPNML114::AnnotationGraphics,
    YasperEPNML114::ArcType,
    YasperEPNML114::Arc,
    TextType2,
    TextType1,
    Tool,
    TextTypeMember0,
    Version,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_yasperepnml114::transitionspecific_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::TransitionSpecific)


def test_yasperepnml114::transitionspecific_constructor_exists():
    assert callable(YasperEPNML114::TransitionSpecific.__init__)


def test_yasperepnml114::transitionspecific_constructor_args():
    sig = inspect.signature(YasperEPNML114::TransitionSpecific.__init__)
    params = list(sig.parameters.keys())
    assert "tokenCaseSensitive" in params, "Missing parameter 'tokenCaseSensitive'"
    assert "version" in params, "Missing parameter 'version'"
    assert "tool" in params, "Missing parameter 'tool'"

def test_yasperepnml114::transitionspecific_has_tokenCaseSensitive():
    assert hasattr(YasperEPNML114::TransitionSpecific, "tokenCaseSensitive")
    descriptor = None
    for klass in YasperEPNML114::TransitionSpecific.__mro__:
        if "tokenCaseSensitive" in klass.__dict__:
            descriptor = klass.__dict__["tokenCaseSensitive"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::transitionspecific_has_version():
    assert hasattr(YasperEPNML114::TransitionSpecific, "version")
    descriptor = None
    for klass in YasperEPNML114::TransitionSpecific.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::transitionspecific_has_tool():
    assert hasattr(YasperEPNML114::TransitionSpecific, "tool")
    descriptor = None
    for klass in YasperEPNML114::TransitionSpecific.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::transformation_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::Transformation)


def test_yasperepnml114::transformation_constructor_exists():
    assert callable(YasperEPNML114::Transformation.__init__)


def test_yasperepnml114::transformation_constructor_args():
    sig = inspect.signature(YasperEPNML114::Transformation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114::transformation_has_text():
    assert hasattr(YasperEPNML114::Transformation, "text")
    descriptor = None
    for klass in YasperEPNML114::Transformation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::roles_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::Roles)


def test_yasperepnml114::roles_constructor_exists():
    assert callable(YasperEPNML114::Roles.__init__)


def test_yasperepnml114::roles_constructor_args():
    sig = inspect.signature(YasperEPNML114::Roles.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114::role_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::Role)


def test_yasperepnml114::role_constructor_exists():
    assert callable(YasperEPNML114::Role.__init__)


def test_yasperepnml114::role_constructor_args():
    sig = inspect.signature(YasperEPNML114::Role.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114::role_has_text():
    assert hasattr(YasperEPNML114::Role, "text")
    descriptor = None
    for klass in YasperEPNML114::Role.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::referenceplacespecific_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::ReferencePlaceSpecific)


def test_yasperepnml114::referenceplacespecific_constructor_exists():
    assert callable(YasperEPNML114::ReferencePlaceSpecific.__init__)


def test_yasperepnml114::referenceplacespecific_constructor_args():
    sig = inspect.signature(YasperEPNML114::ReferencePlaceSpecific.__init__)
    params = list(sig.parameters.keys())
    assert "tool" in params, "Missing parameter 'tool'"
    assert "version" in params, "Missing parameter 'version'"

def test_yasperepnml114::referenceplacespecific_has_tool():
    assert hasattr(YasperEPNML114::ReferencePlaceSpecific, "tool")
    descriptor = None
    for klass in YasperEPNML114::ReferencePlaceSpecific.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::referenceplacespecific_has_version():
    assert hasattr(YasperEPNML114::ReferencePlaceSpecific, "version")
    descriptor = None
    for klass in YasperEPNML114::ReferencePlaceSpecific.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::processingtime_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::ProcessingTime)


def test_yasperepnml114::processingtime_constructor_exists():
    assert callable(YasperEPNML114::ProcessingTime.__init__)


def test_yasperepnml114::processingtime_constructor_args():
    sig = inspect.signature(YasperEPNML114::ProcessingTime.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114::placetype_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::PlaceType)


def test_yasperepnml114::placetype_constructor_exists():
    assert callable(YasperEPNML114::PlaceType.__init__)


def test_yasperepnml114::placetype_constructor_args():
    sig = inspect.signature(YasperEPNML114::PlaceType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114::placetype_has_text():
    assert hasattr(YasperEPNML114::PlaceType, "text")
    descriptor = None
    for klass in YasperEPNML114::PlaceType.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::place_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::Place)


def test_yasperepnml114::place_constructor_exists():
    assert callable(YasperEPNML114::Place.__init__)


def test_yasperepnml114::place_constructor_args():
    sig = inspect.signature(YasperEPNML114::Place.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114::place_has_id():
    assert hasattr(YasperEPNML114::Place, "id")
    descriptor = None
    for klass in YasperEPNML114::Place.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::place_has_group():
    assert hasattr(YasperEPNML114::Place, "group")
    descriptor = None
    for klass in YasperEPNML114::Place.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::transitiontype_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::TransitionType)


def test_yasperepnml114::transitiontype_constructor_exists():
    assert callable(YasperEPNML114::TransitionType.__init__)


def test_yasperepnml114::transitiontype_constructor_args():
    sig = inspect.signature(YasperEPNML114::TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114::transitiontype_has_text():
    assert hasattr(YasperEPNML114::TransitionType, "text")
    descriptor = None
    for klass in YasperEPNML114::TransitionType.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::referenceplace_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::ReferencePlace)


def test_yasperepnml114::referenceplace_constructor_exists():
    assert callable(YasperEPNML114::ReferencePlace.__init__)


def test_yasperepnml114::referenceplace_constructor_args():
    sig = inspect.signature(YasperEPNML114::ReferencePlace.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"
    assert "ref" in params, "Missing parameter 'ref'"

def test_yasperepnml114::referenceplace_has_id():
    assert hasattr(YasperEPNML114::ReferencePlace, "id")
    descriptor = None
    for klass in YasperEPNML114::ReferencePlace.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::referenceplace_has_group():
    assert hasattr(YasperEPNML114::ReferencePlace, "group")
    descriptor = None
    for klass in YasperEPNML114::ReferencePlace.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::referenceplace_has_ref():
    assert hasattr(YasperEPNML114::ReferencePlace, "ref")
    descriptor = None
    for klass in YasperEPNML114::ReferencePlace.__mro__:
        if "ref" in klass.__dict__:
            descriptor = klass.__dict__["ref"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::nodegraphics_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::NodeGraphics)


def test_yasperepnml114::nodegraphics_constructor_exists():
    assert callable(YasperEPNML114::NodeGraphics.__init__)


def test_yasperepnml114::nodegraphics_constructor_args():
    sig = inspect.signature(YasperEPNML114::NodeGraphics.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114::nodegraphics_has_group():
    assert hasattr(YasperEPNML114::NodeGraphics, "group")
    descriptor = None
    for klass in YasperEPNML114::NodeGraphics.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::page_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::Page)


def test_yasperepnml114::page_constructor_exists():
    assert callable(YasperEPNML114::Page.__init__)


def test_yasperepnml114::page_constructor_args():
    sig = inspect.signature(YasperEPNML114::Page.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114::page_has_id():
    assert hasattr(YasperEPNML114::Page, "id")
    descriptor = None
    for klass in YasperEPNML114::Page.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::page_has_group():
    assert hasattr(YasperEPNML114::Page, "group")
    descriptor = None
    for klass in YasperEPNML114::Page.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::transition_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::Transition)


def test_yasperepnml114::transition_constructor_exists():
    assert callable(YasperEPNML114::Transition.__init__)


def test_yasperepnml114::transition_constructor_args():
    sig = inspect.signature(YasperEPNML114::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114::transition_has_id():
    assert hasattr(YasperEPNML114::Transition, "id")
    descriptor = None
    for klass in YasperEPNML114::Transition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::transition_has_group():
    assert hasattr(YasperEPNML114::Transition, "group")
    descriptor = None
    for klass in YasperEPNML114::Transition.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::net_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::Net)


def test_yasperepnml114::net_constructor_exists():
    assert callable(YasperEPNML114::Net.__init__)


def test_yasperepnml114::net_constructor_args():
    sig = inspect.signature(YasperEPNML114::Net.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"
    assert "type" in params, "Missing parameter 'type'"

def test_yasperepnml114::net_has_id():
    assert hasattr(YasperEPNML114::Net, "id")
    descriptor = None
    for klass in YasperEPNML114::Net.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::net_has_group():
    assert hasattr(YasperEPNML114::Net, "group")
    descriptor = None
    for klass in YasperEPNML114::Net.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::net_has_type():
    assert hasattr(YasperEPNML114::Net, "type")
    descriptor = None
    for klass in YasperEPNML114::Net.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::placetype1_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::PlaceType1)


def test_yasperepnml114::placetype1_constructor_exists():
    assert callable(YasperEPNML114::PlaceType1.__init__)


def test_yasperepnml114::placetype1_constructor_args():
    sig = inspect.signature(YasperEPNML114::PlaceType1.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114::netgraphics_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::NetGraphics)


def test_yasperepnml114::netgraphics_constructor_exists():
    assert callable(YasperEPNML114::NetGraphics.__init__)


def test_yasperepnml114::netgraphics_constructor_args():
    sig = inspect.signature(YasperEPNML114::NetGraphics.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114::netgraphics_has_group():
    assert hasattr(YasperEPNML114::NetGraphics, "group")
    descriptor = None
    for klass in YasperEPNML114::NetGraphics.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::initialmarking_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::InitialMarking)


def test_yasperepnml114::initialmarking_constructor_exists():
    assert callable(YasperEPNML114::InitialMarking.__init__)


def test_yasperepnml114::initialmarking_constructor_args():
    sig = inspect.signature(YasperEPNML114::InitialMarking.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114::initialmarking_has_text():
    assert hasattr(YasperEPNML114::InitialMarking, "text")
    descriptor = None
    for klass in YasperEPNML114::InitialMarking.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::documentroot_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::DocumentRoot)


def test_yasperepnml114::documentroot_constructor_exists():
    assert callable(YasperEPNML114::DocumentRoot.__init__)


def test_yasperepnml114::documentroot_constructor_args():
    sig = inspect.signature(YasperEPNML114::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_yasperepnml114::documentroot_has_mixed():
    assert hasattr(YasperEPNML114::DocumentRoot, "mixed")
    descriptor = None
    for klass in YasperEPNML114::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::cost_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::Cost)


def test_yasperepnml114::cost_constructor_exists():
    assert callable(YasperEPNML114::Cost.__init__)


def test_yasperepnml114::cost_constructor_args():
    sig = inspect.signature(YasperEPNML114::Cost.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114::pnml_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::Pnml)


def test_yasperepnml114::pnml_constructor_exists():
    assert callable(YasperEPNML114::Pnml.__init__)


def test_yasperepnml114::pnml_constructor_args():
    sig = inspect.signature(YasperEPNML114::Pnml.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114::pnml_has_group():
    assert hasattr(YasperEPNML114::Pnml, "group")
    descriptor = None
    for klass in YasperEPNML114::Pnml.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::EStringToStringMapEntry)


def test_yasperepnml114::estringtostringmapentry_constructor_exists():
    assert callable(YasperEPNML114::EStringToStringMapEntry.__init__)


def test_yasperepnml114::estringtostringmapentry_constructor_args():
    sig = inspect.signature(YasperEPNML114::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114::connectionweight_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::ConnectionWeight)


def test_yasperepnml114::connectionweight_constructor_exists():
    assert callable(YasperEPNML114::ConnectionWeight.__init__)


def test_yasperepnml114::connectionweight_constructor_args():
    sig = inspect.signature(YasperEPNML114::ConnectionWeight.__init__)
    params = list(sig.parameters.keys())
    assert "connection" in params, "Missing parameter 'connection'"

def test_yasperepnml114::connectionweight_has_connection():
    assert hasattr(YasperEPNML114::ConnectionWeight, "connection")
    descriptor = None
    for klass in YasperEPNML114::ConnectionWeight.__mro__:
        if "connection" in klass.__dict__:
            descriptor = klass.__dict__["connection"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::connectionweights_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::ConnectionWeights)


def test_yasperepnml114::connectionweights_constructor_exists():
    assert callable(YasperEPNML114::ConnectionWeights.__init__)


def test_yasperepnml114::connectionweights_constructor_args():
    sig = inspect.signature(YasperEPNML114::ConnectionWeights.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114::stat_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::Stat)


def test_yasperepnml114::stat_constructor_exists():
    assert callable(YasperEPNML114::Stat.__init__)


def test_yasperepnml114::stat_constructor_args():
    sig = inspect.signature(YasperEPNML114::Stat.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114::stat_has_text():
    assert hasattr(YasperEPNML114::Stat, "text")
    descriptor = None
    for klass in YasperEPNML114::Stat.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::pnmlannotation_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::PnmlAnnotation)


def test_yasperepnml114::pnmlannotation_constructor_exists():
    assert callable(YasperEPNML114::PnmlAnnotation.__init__)


def test_yasperepnml114::pnmlannotation_constructor_args():
    sig = inspect.signature(YasperEPNML114::PnmlAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114::pnmlannotation_has_text():
    assert hasattr(YasperEPNML114::PnmlAnnotation, "text")
    descriptor = None
    for klass in YasperEPNML114::PnmlAnnotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::inscription_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::Inscription)


def test_yasperepnml114::inscription_constructor_exists():
    assert callable(YasperEPNML114::Inscription.__init__)


def test_yasperepnml114::inscription_constructor_args():
    sig = inspect.signature(YasperEPNML114::Inscription.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114::inscription_has_text():
    assert hasattr(YasperEPNML114::Inscription, "text")
    descriptor = None
    for klass in YasperEPNML114::Inscription.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::edgegraphics_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::EdgeGraphics)


def test_yasperepnml114::edgegraphics_constructor_exists():
    assert callable(YasperEPNML114::EdgeGraphics.__init__)


def test_yasperepnml114::edgegraphics_constructor_args():
    sig = inspect.signature(YasperEPNML114::EdgeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114::toolspecifictype_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::ToolspecificType)


def test_yasperepnml114::toolspecifictype_constructor_exists():
    assert callable(YasperEPNML114::ToolspecificType.__init__)


def test_yasperepnml114::toolspecifictype_constructor_args():
    sig = inspect.signature(YasperEPNML114::ToolspecificType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "version" in params, "Missing parameter 'version'"
    assert "any" in params, "Missing parameter 'any'"
    assert "tool" in params, "Missing parameter 'tool'"
    assert "group" in params, "Missing parameter 'group'"

def test_yasperepnml114::toolspecifictype_has_mixed():
    assert hasattr(YasperEPNML114::ToolspecificType, "mixed")
    descriptor = None
    for klass in YasperEPNML114::ToolspecificType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::toolspecifictype_has_version():
    assert hasattr(YasperEPNML114::ToolspecificType, "version")
    descriptor = None
    for klass in YasperEPNML114::ToolspecificType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::toolspecifictype_has_any():
    assert hasattr(YasperEPNML114::ToolspecificType, "any")
    descriptor = None
    for klass in YasperEPNML114::ToolspecificType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::toolspecifictype_has_tool():
    assert hasattr(YasperEPNML114::ToolspecificType, "tool")
    descriptor = None
    for klass in YasperEPNML114::ToolspecificType.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::toolspecifictype_has_group():
    assert hasattr(YasperEPNML114::ToolspecificType, "group")
    descriptor = None
    for klass in YasperEPNML114::ToolspecificType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::twodimvector_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::TwoDimVector)


def test_yasperepnml114::twodimvector_constructor_exists():
    assert callable(YasperEPNML114::TwoDimVector.__init__)


def test_yasperepnml114::twodimvector_constructor_args():
    sig = inspect.signature(YasperEPNML114::TwoDimVector.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_yasperepnml114::twodimvector_has_x():
    assert hasattr(YasperEPNML114::TwoDimVector, "x")
    descriptor = None
    for klass in YasperEPNML114::TwoDimVector.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::twodimvector_has_y():
    assert hasattr(YasperEPNML114::TwoDimVector, "y")
    descriptor = None
    for klass in YasperEPNML114::TwoDimVector.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::AnnotationGraphics)


def test_yasperepnml114::annotationgraphics_constructor_exists():
    assert callable(YasperEPNML114::AnnotationGraphics.__init__)


def test_yasperepnml114::annotationgraphics_constructor_args():
    sig = inspect.signature(YasperEPNML114::AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_yasperepnml114::arctype_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::ArcType)


def test_yasperepnml114::arctype_constructor_exists():
    assert callable(YasperEPNML114::ArcType.__init__)


def test_yasperepnml114::arctype_constructor_args():
    sig = inspect.signature(YasperEPNML114::ArcType.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_yasperepnml114::arctype_has_text():
    assert hasattr(YasperEPNML114::ArcType, "text")
    descriptor = None
    for klass in YasperEPNML114::ArcType.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_yasperepnml114::arc_is_not_abstract():
    assert not inspect.isabstract(YasperEPNML114::Arc)


def test_yasperepnml114::arc_constructor_exists():
    assert callable(YasperEPNML114::Arc.__init__)


def test_yasperepnml114::arc_constructor_args():
    sig = inspect.signature(YasperEPNML114::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "group" in params, "Missing parameter 'group'"
    assert "id" in params, "Missing parameter 'id'"
    assert "target" in params, "Missing parameter 'target'"

def test_yasperepnml114::arc_has_source():
    assert hasattr(YasperEPNML114::Arc, "source")
    descriptor = None
    for klass in YasperEPNML114::Arc.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::arc_has_group():
    assert hasattr(YasperEPNML114::Arc, "group")
    descriptor = None
    for klass in YasperEPNML114::Arc.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::arc_has_id():
    assert hasattr(YasperEPNML114::Arc, "id")
    descriptor = None
    for klass in YasperEPNML114::Arc.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_yasperepnml114::arc_has_target():
    assert hasattr(YasperEPNML114::Arc, "target")
    descriptor = None
    for klass in YasperEPNML114::Arc.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

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
        "XOR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextType1"

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

def test_texttypemember0_exists():
    # Check that the Enumeration exists
    assert TextTypeMember0 is not None

def test_texttypemember0_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextTypeMember0]
    expected_literals = [
        "inflow",
        "inhibitor",
        "reset",
        "outflow",
        "biflow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextTypeMember0"

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
YasperEPNML114::TransitionSpecific_strategy = st.builds(
    YasperEPNML114::TransitionSpecific,
    tokenCaseSensitive=
        safe_text,
    version=
        safe_text,
    tool=
        safe_text
)
YasperEPNML114::Transformation_strategy = st.builds(
    YasperEPNML114::Transformation,
    text=
        safe_text
)
YasperEPNML114::Roles_strategy = st.builds(
    YasperEPNML114::Roles,
)
YasperEPNML114::Role_strategy = st.builds(
    YasperEPNML114::Role,
    text=
        safe_text
)
YasperEPNML114::ReferencePlaceSpecific_strategy = st.builds(
    YasperEPNML114::ReferencePlaceSpecific,
    tool=
        safe_text,
    version=
        safe_text
)
YasperEPNML114::ProcessingTime_strategy = st.builds(
    YasperEPNML114::ProcessingTime,
)
Place_strategy = st.builds(
    Place,
)
YasperEPNML114::PlaceType_strategy = st.builds(
    YasperEPNML114::PlaceType,
    text=
        safe_text
)
YasperEPNML114::Place_strategy = st.builds(
    YasperEPNML114::Place,
    id=
        safe_text,
    group=
        safe_text
)
YasperEPNML114::TransitionType_strategy = st.builds(
    YasperEPNML114::TransitionType,
    text=
        safe_text
)
YasperEPNML114::ReferencePlace_strategy = st.builds(
    YasperEPNML114::ReferencePlace,
    id=
        safe_text,
    group=
        safe_text,
    ref=
        safe_text
)
YasperEPNML114::NodeGraphics_strategy = st.builds(
    YasperEPNML114::NodeGraphics,
    group=
        safe_text
)
YasperEPNML114::Page_strategy = st.builds(
    YasperEPNML114::Page,
    id=
        safe_text,
    group=
        safe_text
)
YasperEPNML114::Transition_strategy = st.builds(
    YasperEPNML114::Transition,
    id=
        safe_text,
    group=
        safe_text
)
YasperEPNML114::Net_strategy = st.builds(
    YasperEPNML114::Net,
    id=
        safe_text,
    group=
        safe_text,
    type=
        safe_text
)
YasperEPNML114::PlaceType1_strategy = st.builds(
    YasperEPNML114::PlaceType1,
)
YasperEPNML114::NetGraphics_strategy = st.builds(
    YasperEPNML114::NetGraphics,
    group=
        safe_text
)
YasperEPNML114::InitialMarking_strategy = st.builds(
    YasperEPNML114::InitialMarking,
    text=
        safe_text
)
YasperEPNML114::DocumentRoot_strategy = st.builds(
    YasperEPNML114::DocumentRoot,
    mixed=
        safe_text
)
YasperEPNML114::Cost_strategy = st.builds(
    YasperEPNML114::Cost,
)
YasperEPNML114::Pnml_strategy = st.builds(
    YasperEPNML114::Pnml,
    group=
        safe_text
)
YasperEPNML114::EStringToStringMapEntry_strategy = st.builds(
    YasperEPNML114::EStringToStringMapEntry,
)
YasperEPNML114::ConnectionWeight_strategy = st.builds(
    YasperEPNML114::ConnectionWeight,
    connection=
        safe_text
)
YasperEPNML114::ConnectionWeights_strategy = st.builds(
    YasperEPNML114::ConnectionWeights,
)
YasperEPNML114::Stat_strategy = st.builds(
    YasperEPNML114::Stat,
    text=
        safe_text
)
YasperEPNML114::PnmlAnnotation_strategy = st.builds(
    YasperEPNML114::PnmlAnnotation,
    text=
        safe_text
)
YasperEPNML114::Inscription_strategy = st.builds(
    YasperEPNML114::Inscription,
    text=
        safe_text
)
YasperEPNML114::EdgeGraphics_strategy = st.builds(
    YasperEPNML114::EdgeGraphics,
)
YasperEPNML114::ToolspecificType_strategy = st.builds(
    YasperEPNML114::ToolspecificType,
    mixed=
        safe_text,
    version=
        safe_text,
    any=
        safe_text,
    tool=
        safe_text,
    group=
        safe_text
)
YasperEPNML114::TwoDimVector_strategy = st.builds(
    YasperEPNML114::TwoDimVector,
    x=
        safe_text,
    y=
        safe_text
)
YasperEPNML114::AnnotationGraphics_strategy = st.builds(
    YasperEPNML114::AnnotationGraphics,
)
YasperEPNML114::ArcType_strategy = st.builds(
    YasperEPNML114::ArcType,
    text=
        safe_text
)
YasperEPNML114::Arc_strategy = st.builds(
    YasperEPNML114::Arc,
    source=
        safe_text,
    group=
        safe_text,
    id=
        safe_text,
    target=
        safe_text
)

@given(instance=YasperEPNML114::TransitionSpecific_strategy)
@settings(max_examples=50)
def test_yasperepnml114::transitionspecific_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::TransitionSpecific)

@given(instance=YasperEPNML114::TransitionSpecific_strategy)
def test_yasperepnml114::transitionspecific_tokenCaseSensitive_type(instance):
    assert isinstance(instance.tokenCaseSensitive, str)


@given(instance=YasperEPNML114::TransitionSpecific_strategy)
def test_yasperepnml114::transitionspecific_tokenCaseSensitive_setter(instance):
    original = instance.tokenCaseSensitive
    instance.tokenCaseSensitive = original
    assert instance.tokenCaseSensitive == original

@given(instance=YasperEPNML114::TransitionSpecific_strategy)
def test_yasperepnml114::transitionspecific_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=YasperEPNML114::TransitionSpecific_strategy)
def test_yasperepnml114::transitionspecific_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=YasperEPNML114::TransitionSpecific_strategy)
def test_yasperepnml114::transitionspecific_tool_type(instance):
    assert isinstance(instance.tool, str)


@given(instance=YasperEPNML114::TransitionSpecific_strategy)
def test_yasperepnml114::transitionspecific_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=YasperEPNML114::Transformation_strategy)
@settings(max_examples=50)
def test_yasperepnml114::transformation_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::Transformation)

@given(instance=YasperEPNML114::Transformation_strategy)
def test_yasperepnml114::transformation_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=YasperEPNML114::Transformation_strategy)
def test_yasperepnml114::transformation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114::Roles_strategy)
@settings(max_examples=50)
def test_yasperepnml114::roles_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::Roles)

@given(instance=YasperEPNML114::Role_strategy)
@settings(max_examples=50)
def test_yasperepnml114::role_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::Role)

@given(instance=YasperEPNML114::Role_strategy)
def test_yasperepnml114::role_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=YasperEPNML114::Role_strategy)
def test_yasperepnml114::role_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114::ReferencePlaceSpecific_strategy)
@settings(max_examples=50)
def test_yasperepnml114::referenceplacespecific_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::ReferencePlaceSpecific)

@given(instance=YasperEPNML114::ReferencePlaceSpecific_strategy)
def test_yasperepnml114::referenceplacespecific_tool_type(instance):
    assert isinstance(instance.tool, str)


@given(instance=YasperEPNML114::ReferencePlaceSpecific_strategy)
def test_yasperepnml114::referenceplacespecific_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=YasperEPNML114::ReferencePlaceSpecific_strategy)
def test_yasperepnml114::referenceplacespecific_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=YasperEPNML114::ReferencePlaceSpecific_strategy)
def test_yasperepnml114::referenceplacespecific_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=YasperEPNML114::ProcessingTime_strategy)
@settings(max_examples=50)
def test_yasperepnml114::processingtime_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::ProcessingTime)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=YasperEPNML114::PlaceType_strategy)
@settings(max_examples=50)
def test_yasperepnml114::placetype_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::PlaceType)

@given(instance=YasperEPNML114::PlaceType_strategy)
def test_yasperepnml114::placetype_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=YasperEPNML114::PlaceType_strategy)
def test_yasperepnml114::placetype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114::Place_strategy)
@settings(max_examples=50)
def test_yasperepnml114::place_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::Place)

@given(instance=YasperEPNML114::Place_strategy)
def test_yasperepnml114::place_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=YasperEPNML114::Place_strategy)
def test_yasperepnml114::place_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=YasperEPNML114::Place_strategy)
def test_yasperepnml114::place_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=YasperEPNML114::Place_strategy)
def test_yasperepnml114::place_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114::TransitionType_strategy)
@settings(max_examples=50)
def test_yasperepnml114::transitiontype_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::TransitionType)

@given(instance=YasperEPNML114::TransitionType_strategy)
def test_yasperepnml114::transitiontype_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=YasperEPNML114::TransitionType_strategy)
def test_yasperepnml114::transitiontype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114::ReferencePlace_strategy)
@settings(max_examples=50)
def test_yasperepnml114::referenceplace_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::ReferencePlace)

@given(instance=YasperEPNML114::ReferencePlace_strategy)
def test_yasperepnml114::referenceplace_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=YasperEPNML114::ReferencePlace_strategy)
def test_yasperepnml114::referenceplace_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=YasperEPNML114::ReferencePlace_strategy)
def test_yasperepnml114::referenceplace_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=YasperEPNML114::ReferencePlace_strategy)
def test_yasperepnml114::referenceplace_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114::ReferencePlace_strategy)
def test_yasperepnml114::referenceplace_ref_type(instance):
    assert isinstance(instance.ref, str)


@given(instance=YasperEPNML114::ReferencePlace_strategy)
def test_yasperepnml114::referenceplace_ref_setter(instance):
    original = instance.ref
    instance.ref = original
    assert instance.ref == original

@given(instance=YasperEPNML114::NodeGraphics_strategy)
@settings(max_examples=50)
def test_yasperepnml114::nodegraphics_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::NodeGraphics)

@given(instance=YasperEPNML114::NodeGraphics_strategy)
def test_yasperepnml114::nodegraphics_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=YasperEPNML114::NodeGraphics_strategy)
def test_yasperepnml114::nodegraphics_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114::Page_strategy)
@settings(max_examples=50)
def test_yasperepnml114::page_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::Page)

@given(instance=YasperEPNML114::Page_strategy)
def test_yasperepnml114::page_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=YasperEPNML114::Page_strategy)
def test_yasperepnml114::page_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=YasperEPNML114::Page_strategy)
def test_yasperepnml114::page_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=YasperEPNML114::Page_strategy)
def test_yasperepnml114::page_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114::Transition_strategy)
@settings(max_examples=50)
def test_yasperepnml114::transition_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::Transition)

@given(instance=YasperEPNML114::Transition_strategy)
def test_yasperepnml114::transition_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=YasperEPNML114::Transition_strategy)
def test_yasperepnml114::transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=YasperEPNML114::Transition_strategy)
def test_yasperepnml114::transition_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=YasperEPNML114::Transition_strategy)
def test_yasperepnml114::transition_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114::Net_strategy)
@settings(max_examples=50)
def test_yasperepnml114::net_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::Net)

@given(instance=YasperEPNML114::Net_strategy)
def test_yasperepnml114::net_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=YasperEPNML114::Net_strategy)
def test_yasperepnml114::net_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=YasperEPNML114::Net_strategy)
def test_yasperepnml114::net_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=YasperEPNML114::Net_strategy)
def test_yasperepnml114::net_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114::Net_strategy)
def test_yasperepnml114::net_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=YasperEPNML114::Net_strategy)
def test_yasperepnml114::net_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=YasperEPNML114::PlaceType1_strategy)
@settings(max_examples=50)
def test_yasperepnml114::placetype1_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::PlaceType1)

@given(instance=YasperEPNML114::NetGraphics_strategy)
@settings(max_examples=50)
def test_yasperepnml114::netgraphics_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::NetGraphics)

@given(instance=YasperEPNML114::NetGraphics_strategy)
def test_yasperepnml114::netgraphics_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=YasperEPNML114::NetGraphics_strategy)
def test_yasperepnml114::netgraphics_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114::InitialMarking_strategy)
@settings(max_examples=50)
def test_yasperepnml114::initialmarking_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::InitialMarking)

@given(instance=YasperEPNML114::InitialMarking_strategy)
def test_yasperepnml114::initialmarking_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=YasperEPNML114::InitialMarking_strategy)
def test_yasperepnml114::initialmarking_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114::DocumentRoot_strategy)
@settings(max_examples=50)
def test_yasperepnml114::documentroot_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::DocumentRoot)

@given(instance=YasperEPNML114::DocumentRoot_strategy)
def test_yasperepnml114::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=YasperEPNML114::DocumentRoot_strategy)
def test_yasperepnml114::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=YasperEPNML114::Cost_strategy)
@settings(max_examples=50)
def test_yasperepnml114::cost_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::Cost)

@given(instance=YasperEPNML114::Pnml_strategy)
@settings(max_examples=50)
def test_yasperepnml114::pnml_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::Pnml)

@given(instance=YasperEPNML114::Pnml_strategy)
def test_yasperepnml114::pnml_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=YasperEPNML114::Pnml_strategy)
def test_yasperepnml114::pnml_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_yasperepnml114::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::EStringToStringMapEntry)

@given(instance=YasperEPNML114::ConnectionWeight_strategy)
@settings(max_examples=50)
def test_yasperepnml114::connectionweight_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::ConnectionWeight)

@given(instance=YasperEPNML114::ConnectionWeight_strategy)
def test_yasperepnml114::connectionweight_connection_type(instance):
    assert isinstance(instance.connection, str)


@given(instance=YasperEPNML114::ConnectionWeight_strategy)
def test_yasperepnml114::connectionweight_connection_setter(instance):
    original = instance.connection
    instance.connection = original
    assert instance.connection == original

@given(instance=YasperEPNML114::ConnectionWeights_strategy)
@settings(max_examples=50)
def test_yasperepnml114::connectionweights_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::ConnectionWeights)

@given(instance=YasperEPNML114::Stat_strategy)
@settings(max_examples=50)
def test_yasperepnml114::stat_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::Stat)

@given(instance=YasperEPNML114::Stat_strategy)
def test_yasperepnml114::stat_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=YasperEPNML114::Stat_strategy)
def test_yasperepnml114::stat_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114::PnmlAnnotation_strategy)
@settings(max_examples=50)
def test_yasperepnml114::pnmlannotation_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::PnmlAnnotation)

@given(instance=YasperEPNML114::PnmlAnnotation_strategy)
def test_yasperepnml114::pnmlannotation_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=YasperEPNML114::PnmlAnnotation_strategy)
def test_yasperepnml114::pnmlannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114::Inscription_strategy)
@settings(max_examples=50)
def test_yasperepnml114::inscription_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::Inscription)

@given(instance=YasperEPNML114::Inscription_strategy)
def test_yasperepnml114::inscription_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=YasperEPNML114::Inscription_strategy)
def test_yasperepnml114::inscription_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114::EdgeGraphics_strategy)
@settings(max_examples=50)
def test_yasperepnml114::edgegraphics_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::EdgeGraphics)

@given(instance=YasperEPNML114::ToolspecificType_strategy)
@settings(max_examples=50)
def test_yasperepnml114::toolspecifictype_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::ToolspecificType)

@given(instance=YasperEPNML114::ToolspecificType_strategy)
def test_yasperepnml114::toolspecifictype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=YasperEPNML114::ToolspecificType_strategy)
def test_yasperepnml114::toolspecifictype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=YasperEPNML114::ToolspecificType_strategy)
def test_yasperepnml114::toolspecifictype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=YasperEPNML114::ToolspecificType_strategy)
def test_yasperepnml114::toolspecifictype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=YasperEPNML114::ToolspecificType_strategy)
def test_yasperepnml114::toolspecifictype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=YasperEPNML114::ToolspecificType_strategy)
def test_yasperepnml114::toolspecifictype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=YasperEPNML114::ToolspecificType_strategy)
def test_yasperepnml114::toolspecifictype_tool_type(instance):
    assert isinstance(instance.tool, str)


@given(instance=YasperEPNML114::ToolspecificType_strategy)
def test_yasperepnml114::toolspecifictype_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=YasperEPNML114::ToolspecificType_strategy)
def test_yasperepnml114::toolspecifictype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=YasperEPNML114::ToolspecificType_strategy)
def test_yasperepnml114::toolspecifictype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114::TwoDimVector_strategy)
@settings(max_examples=50)
def test_yasperepnml114::twodimvector_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::TwoDimVector)

@given(instance=YasperEPNML114::TwoDimVector_strategy)
def test_yasperepnml114::twodimvector_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=YasperEPNML114::TwoDimVector_strategy)
def test_yasperepnml114::twodimvector_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=YasperEPNML114::TwoDimVector_strategy)
def test_yasperepnml114::twodimvector_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=YasperEPNML114::TwoDimVector_strategy)
def test_yasperepnml114::twodimvector_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=YasperEPNML114::AnnotationGraphics_strategy)
@settings(max_examples=50)
def test_yasperepnml114::annotationgraphics_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::AnnotationGraphics)

@given(instance=YasperEPNML114::ArcType_strategy)
@settings(max_examples=50)
def test_yasperepnml114::arctype_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::ArcType)

@given(instance=YasperEPNML114::ArcType_strategy)
def test_yasperepnml114::arctype_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=YasperEPNML114::ArcType_strategy)
def test_yasperepnml114::arctype_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=YasperEPNML114::Arc_strategy)
@settings(max_examples=50)
def test_yasperepnml114::arc_instantiation(instance):
    assert isinstance(instance, YasperEPNML114::Arc)

@given(instance=YasperEPNML114::Arc_strategy)
def test_yasperepnml114::arc_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=YasperEPNML114::Arc_strategy)
def test_yasperepnml114::arc_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=YasperEPNML114::Arc_strategy)
def test_yasperepnml114::arc_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=YasperEPNML114::Arc_strategy)
def test_yasperepnml114::arc_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=YasperEPNML114::Arc_strategy)
def test_yasperepnml114::arc_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=YasperEPNML114::Arc_strategy)
def test_yasperepnml114::arc_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=YasperEPNML114::Arc_strategy)
def test_yasperepnml114::arc_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=YasperEPNML114::Arc_strategy)
def test_yasperepnml114::arc_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original
