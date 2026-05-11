import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    EGamaObject,
    gama::ESpecies,
    gama::EFacet,
    gama::EGamaLink,
    gama::EGamaObject,
    gama::EGamaModel,
    gama::EVariable,
    gama::EEquation,
    gama::ERule,
    gama::EPerceive,
    gama::ETask,
    gama::EState,
    gama::EPlan,
    gama::EChartLayer,
    gama::ELayer,
    gama::EDisplay,
    gama::EAction,
    EGamaLink,
    gama::EReflexLink,
    gama::EAspectLink,
    gama::EExperimentLink,
    gama::ESubSpeciesLink,
    gama::EInheritLink,
    gama::EActionLink,
    EExperiment,
    gama::EBatchExperiment,
    gama::EGUIExperiment,
    gama::EMonitor,
    gama::EParameter,
    gama::EDisplayLink,
    ESpecies,
    gama::EWorldAgent,
    gama::EGrid,
    gama::EExperiment,
    gama::EReflex,
    gama::EEquationLink,
    gama::ELayerAspect,
    gama::ERuleLink,
    gama::EPerceiveLink,
    gama::EAspect,
    gama::ETaskLink,
    gama::EStateLink,
    gama::EPlanLink,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_egamaobject_is_not_abstract():
    assert not inspect.isabstract(EGamaObject)


def test_egamaobject_constructor_exists():
    assert callable(EGamaObject.__init__)


def test_egamaobject_constructor_args():
    sig = inspect.signature(EGamaObject.__init__)
    params = list(sig.parameters.keys())



def test_gama::especies_is_not_abstract():
    assert not inspect.isabstract(gama::ESpecies)


def test_gama::especies_constructor_exists():
    assert callable(gama::ESpecies.__init__)


def test_gama::especies_constructor_args():
    sig = inspect.signature(gama::ESpecies.__init__)
    params = list(sig.parameters.keys())
    assert "reflexList" in params, "Missing parameter 'reflexList'"
    assert "init" in params, "Missing parameter 'init'"
    assert "skills" in params, "Missing parameter 'skills'"

def test_gama::especies_has_reflexList():
    assert hasattr(gama::ESpecies, "reflexList")
    descriptor = None
    for klass in gama::ESpecies.__mro__:
        if "reflexList" in klass.__dict__:
            descriptor = klass.__dict__["reflexList"]
            break
    assert isinstance(descriptor, property)

def test_gama::especies_has_init():
    assert hasattr(gama::ESpecies, "init")
    descriptor = None
    for klass in gama::ESpecies.__mro__:
        if "init" in klass.__dict__:
            descriptor = klass.__dict__["init"]
            break
    assert isinstance(descriptor, property)

def test_gama::especies_has_skills():
    assert hasattr(gama::ESpecies, "skills")
    descriptor = None
    for klass in gama::ESpecies.__mro__:
        if "skills" in klass.__dict__:
            descriptor = klass.__dict__["skills"]
            break
    assert isinstance(descriptor, property)



def test_gama::efacet_is_not_abstract():
    assert not inspect.isabstract(gama::EFacet)


def test_gama::efacet_constructor_exists():
    assert callable(gama::EFacet.__init__)


def test_gama::efacet_constructor_args():
    sig = inspect.signature(gama::EFacet.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_gama::efacet_has_value():
    assert hasattr(gama::EFacet, "value")
    descriptor = None
    for klass in gama::EFacet.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_gama::efacet_has_name():
    assert hasattr(gama::EFacet, "name")
    descriptor = None
    for klass in gama::EFacet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gama::egamalink_is_not_abstract():
    assert not inspect.isabstract(gama::EGamaLink)


def test_gama::egamalink_constructor_exists():
    assert callable(gama::EGamaLink.__init__)


def test_gama::egamalink_constructor_args():
    sig = inspect.signature(gama::EGamaLink.__init__)
    params = list(sig.parameters.keys())



def test_gama::egamaobject_is_not_abstract():
    assert not inspect.isabstract(gama::EGamaObject)


def test_gama::egamaobject_constructor_exists():
    assert callable(gama::EGamaObject.__init__)


def test_gama::egamaobject_constructor_args():
    sig = inspect.signature(gama::EGamaObject.__init__)
    params = list(sig.parameters.keys())
    assert "error" in params, "Missing parameter 'error'"
    assert "colorPicto" in params, "Missing parameter 'colorPicto'"
    assert "name" in params, "Missing parameter 'name'"
    assert "hasError" in params, "Missing parameter 'hasError'"

def test_gama::egamaobject_has_error():
    assert hasattr(gama::EGamaObject, "error")
    descriptor = None
    for klass in gama::EGamaObject.__mro__:
        if "error" in klass.__dict__:
            descriptor = klass.__dict__["error"]
            break
    assert isinstance(descriptor, property)

def test_gama::egamaobject_has_colorPicto():
    assert hasattr(gama::EGamaObject, "colorPicto")
    descriptor = None
    for klass in gama::EGamaObject.__mro__:
        if "colorPicto" in klass.__dict__:
            descriptor = klass.__dict__["colorPicto"]
            break
    assert isinstance(descriptor, property)

def test_gama::egamaobject_has_name():
    assert hasattr(gama::EGamaObject, "name")
    descriptor = None
    for klass in gama::EGamaObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gama::egamaobject_has_hasError():
    assert hasattr(gama::EGamaObject, "hasError")
    descriptor = None
    for klass in gama::EGamaObject.__mro__:
        if "hasError" in klass.__dict__:
            descriptor = klass.__dict__["hasError"]
            break
    assert isinstance(descriptor, property)



def test_gama::egamamodel_is_not_abstract():
    assert not inspect.isabstract(gama::EGamaModel)


def test_gama::egamamodel_constructor_exists():
    assert callable(gama::EGamaModel.__init__)


def test_gama::egamamodel_constructor_args():
    sig = inspect.signature(gama::EGamaModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gama::egamamodel_has_name():
    assert hasattr(gama::EGamaModel, "name")
    descriptor = None
    for klass in gama::EGamaModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gama::evariable_is_not_abstract():
    assert not inspect.isabstract(gama::EVariable)


def test_gama::evariable_constructor_exists():
    assert callable(gama::EVariable.__init__)


def test_gama::evariable_constructor_args():
    sig = inspect.signature(gama::EVariable.__init__)
    params = list(sig.parameters.keys())
    assert "update" in params, "Missing parameter 'update'"
    assert "function" in params, "Missing parameter 'function'"
    assert "init" in params, "Missing parameter 'init'"
    assert "max" in params, "Missing parameter 'max'"
    assert "error" in params, "Missing parameter 'error'"
    assert "hasError" in params, "Missing parameter 'hasError'"
    assert "type" in params, "Missing parameter 'type'"
    assert "min" in params, "Missing parameter 'min'"
    assert "name" in params, "Missing parameter 'name'"

def test_gama::evariable_has_update():
    assert hasattr(gama::EVariable, "update")
    descriptor = None
    for klass in gama::EVariable.__mro__:
        if "update" in klass.__dict__:
            descriptor = klass.__dict__["update"]
            break
    assert isinstance(descriptor, property)

def test_gama::evariable_has_function():
    assert hasattr(gama::EVariable, "function")
    descriptor = None
    for klass in gama::EVariable.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)

def test_gama::evariable_has_init():
    assert hasattr(gama::EVariable, "init")
    descriptor = None
    for klass in gama::EVariable.__mro__:
        if "init" in klass.__dict__:
            descriptor = klass.__dict__["init"]
            break
    assert isinstance(descriptor, property)

def test_gama::evariable_has_max():
    assert hasattr(gama::EVariable, "max")
    descriptor = None
    for klass in gama::EVariable.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_gama::evariable_has_error():
    assert hasattr(gama::EVariable, "error")
    descriptor = None
    for klass in gama::EVariable.__mro__:
        if "error" in klass.__dict__:
            descriptor = klass.__dict__["error"]
            break
    assert isinstance(descriptor, property)

def test_gama::evariable_has_hasError():
    assert hasattr(gama::EVariable, "hasError")
    descriptor = None
    for klass in gama::EVariable.__mro__:
        if "hasError" in klass.__dict__:
            descriptor = klass.__dict__["hasError"]
            break
    assert isinstance(descriptor, property)

def test_gama::evariable_has_type():
    assert hasattr(gama::EVariable, "type")
    descriptor = None
    for klass in gama::EVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_gama::evariable_has_min():
    assert hasattr(gama::EVariable, "min")
    descriptor = None
    for klass in gama::EVariable.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_gama::evariable_has_name():
    assert hasattr(gama::EVariable, "name")
    descriptor = None
    for klass in gama::EVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gama::eequation_is_not_abstract():
    assert not inspect.isabstract(gama::EEquation)


def test_gama::eequation_constructor_exists():
    assert callable(gama::EEquation.__init__)


def test_gama::eequation_constructor_args():
    sig = inspect.signature(gama::EEquation.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama::eequation_has_gamlCode():
    assert hasattr(gama::EEquation, "gamlCode")
    descriptor = None
    for klass in gama::EEquation.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama::erule_is_not_abstract():
    assert not inspect.isabstract(gama::ERule)


def test_gama::erule_constructor_exists():
    assert callable(gama::ERule.__init__)


def test_gama::erule_constructor_args():
    sig = inspect.signature(gama::ERule.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama::erule_has_gamlCode():
    assert hasattr(gama::ERule, "gamlCode")
    descriptor = None
    for klass in gama::ERule.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama::eperceive_is_not_abstract():
    assert not inspect.isabstract(gama::EPerceive)


def test_gama::eperceive_constructor_exists():
    assert callable(gama::EPerceive.__init__)


def test_gama::eperceive_constructor_args():
    sig = inspect.signature(gama::EPerceive.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama::eperceive_has_gamlCode():
    assert hasattr(gama::EPerceive, "gamlCode")
    descriptor = None
    for klass in gama::EPerceive.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama::etask_is_not_abstract():
    assert not inspect.isabstract(gama::ETask)


def test_gama::etask_constructor_exists():
    assert callable(gama::ETask.__init__)


def test_gama::etask_constructor_args():
    sig = inspect.signature(gama::ETask.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama::etask_has_gamlCode():
    assert hasattr(gama::ETask, "gamlCode")
    descriptor = None
    for klass in gama::ETask.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama::estate_is_not_abstract():
    assert not inspect.isabstract(gama::EState)


def test_gama::estate_constructor_exists():
    assert callable(gama::EState.__init__)


def test_gama::estate_constructor_args():
    sig = inspect.signature(gama::EState.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama::estate_has_gamlCode():
    assert hasattr(gama::EState, "gamlCode")
    descriptor = None
    for klass in gama::EState.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama::eplan_is_not_abstract():
    assert not inspect.isabstract(gama::EPlan)


def test_gama::eplan_constructor_exists():
    assert callable(gama::EPlan.__init__)


def test_gama::eplan_constructor_args():
    sig = inspect.signature(gama::EPlan.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama::eplan_has_gamlCode():
    assert hasattr(gama::EPlan, "gamlCode")
    descriptor = None
    for klass in gama::EPlan.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama::echartlayer_is_not_abstract():
    assert not inspect.isabstract(gama::EChartLayer)


def test_gama::echartlayer_constructor_exists():
    assert callable(gama::EChartLayer.__init__)


def test_gama::echartlayer_constructor_args():
    sig = inspect.signature(gama::EChartLayer.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "color" in params, "Missing parameter 'color'"
    assert "style" in params, "Missing parameter 'style'"

def test_gama::echartlayer_has_value():
    assert hasattr(gama::EChartLayer, "value")
    descriptor = None
    for klass in gama::EChartLayer.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_gama::echartlayer_has_color():
    assert hasattr(gama::EChartLayer, "color")
    descriptor = None
    for klass in gama::EChartLayer.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_gama::echartlayer_has_style():
    assert hasattr(gama::EChartLayer, "style")
    descriptor = None
    for klass in gama::EChartLayer.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_gama::elayer_is_not_abstract():
    assert not inspect.isabstract(gama::ELayer)


def test_gama::elayer_constructor_exists():
    assert callable(gama::ELayer.__init__)


def test_gama::elayer_constructor_args():
    sig = inspect.signature(gama::ELayer.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "file" in params, "Missing parameter 'file'"
    assert "color" in params, "Missing parameter 'color'"
    assert "isColorCst" in params, "Missing parameter 'isColorCst'"
    assert "chart_type" in params, "Missing parameter 'chart_type'"
    assert "size" in params, "Missing parameter 'size'"
    assert "agents" in params, "Missing parameter 'agents'"
    assert "aspect" in params, "Missing parameter 'aspect'"
    assert "colorRBG" in params, "Missing parameter 'colorRBG'"
    assert "type" in params, "Missing parameter 'type'"
    assert "species" in params, "Missing parameter 'species'"
    assert "grid" in params, "Missing parameter 'grid'"
    assert "showLines" in params, "Missing parameter 'showLines'"
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama::elayer_has_text():
    assert hasattr(gama::ELayer, "text")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_file():
    assert hasattr(gama::ELayer, "file")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_color():
    assert hasattr(gama::ELayer, "color")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_isColorCst():
    assert hasattr(gama::ELayer, "isColorCst")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "isColorCst" in klass.__dict__:
            descriptor = klass.__dict__["isColorCst"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_chart_type():
    assert hasattr(gama::ELayer, "chart_type")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "chart_type" in klass.__dict__:
            descriptor = klass.__dict__["chart_type"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_size():
    assert hasattr(gama::ELayer, "size")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_agents():
    assert hasattr(gama::ELayer, "agents")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "agents" in klass.__dict__:
            descriptor = klass.__dict__["agents"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_aspect():
    assert hasattr(gama::ELayer, "aspect")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "aspect" in klass.__dict__:
            descriptor = klass.__dict__["aspect"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_colorRBG():
    assert hasattr(gama::ELayer, "colorRBG")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "colorRBG" in klass.__dict__:
            descriptor = klass.__dict__["colorRBG"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_type():
    assert hasattr(gama::ELayer, "type")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_species():
    assert hasattr(gama::ELayer, "species")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "species" in klass.__dict__:
            descriptor = klass.__dict__["species"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_grid():
    assert hasattr(gama::ELayer, "grid")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "grid" in klass.__dict__:
            descriptor = klass.__dict__["grid"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_showLines():
    assert hasattr(gama::ELayer, "showLines")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "showLines" in klass.__dict__:
            descriptor = klass.__dict__["showLines"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayer_has_gamlCode():
    assert hasattr(gama::ELayer, "gamlCode")
    descriptor = None
    for klass in gama::ELayer.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama::edisplay_is_not_abstract():
    assert not inspect.isabstract(gama::EDisplay)


def test_gama::edisplay_constructor_exists():
    assert callable(gama::EDisplay.__init__)


def test_gama::edisplay_constructor_args():
    sig = inspect.signature(gama::EDisplay.__init__)
    params = list(sig.parameters.keys())
    assert "layerList" in params, "Missing parameter 'layerList'"
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"
    assert "defineGamlCode" in params, "Missing parameter 'defineGamlCode'"

def test_gama::edisplay_has_layerList():
    assert hasattr(gama::EDisplay, "layerList")
    descriptor = None
    for klass in gama::EDisplay.__mro__:
        if "layerList" in klass.__dict__:
            descriptor = klass.__dict__["layerList"]
            break
    assert isinstance(descriptor, property)

def test_gama::edisplay_has_gamlCode():
    assert hasattr(gama::EDisplay, "gamlCode")
    descriptor = None
    for klass in gama::EDisplay.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)

def test_gama::edisplay_has_defineGamlCode():
    assert hasattr(gama::EDisplay, "defineGamlCode")
    descriptor = None
    for klass in gama::EDisplay.__mro__:
        if "defineGamlCode" in klass.__dict__:
            descriptor = klass.__dict__["defineGamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama::eaction_is_not_abstract():
    assert not inspect.isabstract(gama::EAction)


def test_gama::eaction_constructor_exists():
    assert callable(gama::EAction.__init__)


def test_gama::eaction_constructor_args():
    sig = inspect.signature(gama::EAction.__init__)
    params = list(sig.parameters.keys())
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama::eaction_has_returnType():
    assert hasattr(gama::EAction, "returnType")
    descriptor = None
    for klass in gama::EAction.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)

def test_gama::eaction_has_gamlCode():
    assert hasattr(gama::EAction, "gamlCode")
    descriptor = None
    for klass in gama::EAction.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_egamalink_is_not_abstract():
    assert not inspect.isabstract(EGamaLink)


def test_egamalink_constructor_exists():
    assert callable(EGamaLink.__init__)


def test_egamalink_constructor_args():
    sig = inspect.signature(EGamaLink.__init__)
    params = list(sig.parameters.keys())



def test_gama::ereflexlink_is_not_abstract():
    assert not inspect.isabstract(gama::EReflexLink)


def test_gama::ereflexlink_constructor_exists():
    assert callable(gama::EReflexLink.__init__)


def test_gama::ereflexlink_constructor_args():
    sig = inspect.signature(gama::EReflexLink.__init__)
    params = list(sig.parameters.keys())



def test_gama::easpectlink_is_not_abstract():
    assert not inspect.isabstract(gama::EAspectLink)


def test_gama::easpectlink_constructor_exists():
    assert callable(gama::EAspectLink.__init__)


def test_gama::easpectlink_constructor_args():
    sig = inspect.signature(gama::EAspectLink.__init__)
    params = list(sig.parameters.keys())



def test_gama::eexperimentlink_is_not_abstract():
    assert not inspect.isabstract(gama::EExperimentLink)


def test_gama::eexperimentlink_constructor_exists():
    assert callable(gama::EExperimentLink.__init__)


def test_gama::eexperimentlink_constructor_args():
    sig = inspect.signature(gama::EExperimentLink.__init__)
    params = list(sig.parameters.keys())



def test_gama::esubspecieslink_is_not_abstract():
    assert not inspect.isabstract(gama::ESubSpeciesLink)


def test_gama::esubspecieslink_constructor_exists():
    assert callable(gama::ESubSpeciesLink.__init__)


def test_gama::esubspecieslink_constructor_args():
    sig = inspect.signature(gama::ESubSpeciesLink.__init__)
    params = list(sig.parameters.keys())



def test_gama::einheritlink_is_not_abstract():
    assert not inspect.isabstract(gama::EInheritLink)


def test_gama::einheritlink_constructor_exists():
    assert callable(gama::EInheritLink.__init__)


def test_gama::einheritlink_constructor_args():
    sig = inspect.signature(gama::EInheritLink.__init__)
    params = list(sig.parameters.keys())



def test_gama::eactionlink_is_not_abstract():
    assert not inspect.isabstract(gama::EActionLink)


def test_gama::eactionlink_constructor_exists():
    assert callable(gama::EActionLink.__init__)


def test_gama::eactionlink_constructor_args():
    sig = inspect.signature(gama::EActionLink.__init__)
    params = list(sig.parameters.keys())



def test_eexperiment_is_not_abstract():
    assert not inspect.isabstract(EExperiment)


def test_eexperiment_constructor_exists():
    assert callable(EExperiment.__init__)


def test_eexperiment_constructor_args():
    sig = inspect.signature(EExperiment.__init__)
    params = list(sig.parameters.keys())



def test_gama::ebatchexperiment_is_not_abstract():
    assert not inspect.isabstract(gama::EBatchExperiment)


def test_gama::ebatchexperiment_constructor_exists():
    assert callable(gama::EBatchExperiment.__init__)


def test_gama::ebatchexperiment_constructor_args():
    sig = inspect.signature(gama::EBatchExperiment.__init__)
    params = list(sig.parameters.keys())



def test_gama::eguiexperiment_is_not_abstract():
    assert not inspect.isabstract(gama::EGUIExperiment)


def test_gama::eguiexperiment_constructor_exists():
    assert callable(gama::EGUIExperiment.__init__)


def test_gama::eguiexperiment_constructor_args():
    sig = inspect.signature(gama::EGUIExperiment.__init__)
    params = list(sig.parameters.keys())



def test_gama::emonitor_is_not_abstract():
    assert not inspect.isabstract(gama::EMonitor)


def test_gama::emonitor_constructor_exists():
    assert callable(gama::EMonitor.__init__)


def test_gama::emonitor_constructor_args():
    sig = inspect.signature(gama::EMonitor.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gama::emonitor_has_value():
    assert hasattr(gama::EMonitor, "value")
    descriptor = None
    for klass in gama::EMonitor.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gama::eparameter_is_not_abstract():
    assert not inspect.isabstract(gama::EParameter)


def test_gama::eparameter_constructor_exists():
    assert callable(gama::EParameter.__init__)


def test_gama::eparameter_constructor_args():
    sig = inspect.signature(gama::EParameter.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "step" in params, "Missing parameter 'step'"
    assert "min" in params, "Missing parameter 'min'"
    assert "init" in params, "Missing parameter 'init'"
    assert "among" in params, "Missing parameter 'among'"
    assert "variable" in params, "Missing parameter 'variable'"
    assert "max" in params, "Missing parameter 'max'"

def test_gama::eparameter_has_category():
    assert hasattr(gama::EParameter, "category")
    descriptor = None
    for klass in gama::EParameter.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_gama::eparameter_has_step():
    assert hasattr(gama::EParameter, "step")
    descriptor = None
    for klass in gama::EParameter.__mro__:
        if "step" in klass.__dict__:
            descriptor = klass.__dict__["step"]
            break
    assert isinstance(descriptor, property)

def test_gama::eparameter_has_min():
    assert hasattr(gama::EParameter, "min")
    descriptor = None
    for klass in gama::EParameter.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_gama::eparameter_has_init():
    assert hasattr(gama::EParameter, "init")
    descriptor = None
    for klass in gama::EParameter.__mro__:
        if "init" in klass.__dict__:
            descriptor = klass.__dict__["init"]
            break
    assert isinstance(descriptor, property)

def test_gama::eparameter_has_among():
    assert hasattr(gama::EParameter, "among")
    descriptor = None
    for klass in gama::EParameter.__mro__:
        if "among" in klass.__dict__:
            descriptor = klass.__dict__["among"]
            break
    assert isinstance(descriptor, property)

def test_gama::eparameter_has_variable():
    assert hasattr(gama::EParameter, "variable")
    descriptor = None
    for klass in gama::EParameter.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)

def test_gama::eparameter_has_max():
    assert hasattr(gama::EParameter, "max")
    descriptor = None
    for klass in gama::EParameter.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_gama::edisplaylink_is_not_abstract():
    assert not inspect.isabstract(gama::EDisplayLink)


def test_gama::edisplaylink_constructor_exists():
    assert callable(gama::EDisplayLink.__init__)


def test_gama::edisplaylink_constructor_args():
    sig = inspect.signature(gama::EDisplayLink.__init__)
    params = list(sig.parameters.keys())



def test_especies_is_not_abstract():
    assert not inspect.isabstract(ESpecies)


def test_especies_constructor_exists():
    assert callable(ESpecies.__init__)


def test_especies_constructor_args():
    sig = inspect.signature(ESpecies.__init__)
    params = list(sig.parameters.keys())



def test_gama::eworldagent_is_not_abstract():
    assert not inspect.isabstract(gama::EWorldAgent)


def test_gama::eworldagent_constructor_exists():
    assert callable(gama::EWorldAgent.__init__)


def test_gama::eworldagent_constructor_args():
    sig = inspect.signature(gama::EWorldAgent.__init__)
    params = list(sig.parameters.keys())



def test_gama::egrid_is_not_abstract():
    assert not inspect.isabstract(gama::EGrid)


def test_gama::egrid_constructor_exists():
    assert callable(gama::EGrid.__init__)


def test_gama::egrid_constructor_args():
    sig = inspect.signature(gama::EGrid.__init__)
    params = list(sig.parameters.keys())



def test_gama::eexperiment_is_not_abstract():
    assert not inspect.isabstract(gama::EExperiment)


def test_gama::eexperiment_constructor_exists():
    assert callable(gama::EExperiment.__init__)


def test_gama::eexperiment_constructor_args():
    sig = inspect.signature(gama::EExperiment.__init__)
    params = list(sig.parameters.keys())



def test_gama::ereflex_is_not_abstract():
    assert not inspect.isabstract(gama::EReflex)


def test_gama::ereflex_constructor_exists():
    assert callable(gama::EReflex.__init__)


def test_gama::ereflex_constructor_args():
    sig = inspect.signature(gama::EReflex.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama::ereflex_has_gamlCode():
    assert hasattr(gama::EReflex, "gamlCode")
    descriptor = None
    for klass in gama::EReflex.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama::eequationlink_is_not_abstract():
    assert not inspect.isabstract(gama::EEquationLink)


def test_gama::eequationlink_constructor_exists():
    assert callable(gama::EEquationLink.__init__)


def test_gama::eequationlink_constructor_args():
    sig = inspect.signature(gama::EEquationLink.__init__)
    params = list(sig.parameters.keys())



def test_gama::elayeraspect_is_not_abstract():
    assert not inspect.isabstract(gama::ELayerAspect)


def test_gama::elayeraspect_constructor_exists():
    assert callable(gama::ELayerAspect.__init__)


def test_gama::elayeraspect_constructor_args():
    sig = inspect.signature(gama::ELayerAspect.__init__)
    params = list(sig.parameters.keys())
    assert "at" in params, "Missing parameter 'at'"
    assert "texture" in params, "Missing parameter 'texture'"
    assert "shapeType" in params, "Missing parameter 'shapeType'"
    assert "depth" in params, "Missing parameter 'depth'"
    assert "rotate" in params, "Missing parameter 'rotate'"
    assert "color" in params, "Missing parameter 'color'"
    assert "radius" in params, "Missing parameter 'radius'"
    assert "type" in params, "Missing parameter 'type'"
    assert "path" in params, "Missing parameter 'path'"
    assert "empty" in params, "Missing parameter 'empty'"
    assert "size" in params, "Missing parameter 'size'"
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"
    assert "isColorCst" in params, "Missing parameter 'isColorCst'"
    assert "points" in params, "Missing parameter 'points'"
    assert "textSize" in params, "Missing parameter 'textSize'"
    assert "text" in params, "Missing parameter 'text'"
    assert "imageSize" in params, "Missing parameter 'imageSize'"
    assert "colorRBG" in params, "Missing parameter 'colorRBG'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "heigth" in params, "Missing parameter 'heigth'"
    assert "width" in params, "Missing parameter 'width'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_gama::elayeraspect_has_at():
    assert hasattr(gama::ELayerAspect, "at")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "at" in klass.__dict__:
            descriptor = klass.__dict__["at"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_texture():
    assert hasattr(gama::ELayerAspect, "texture")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "texture" in klass.__dict__:
            descriptor = klass.__dict__["texture"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_shapeType():
    assert hasattr(gama::ELayerAspect, "shapeType")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "shapeType" in klass.__dict__:
            descriptor = klass.__dict__["shapeType"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_depth():
    assert hasattr(gama::ELayerAspect, "depth")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "depth" in klass.__dict__:
            descriptor = klass.__dict__["depth"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_rotate():
    assert hasattr(gama::ELayerAspect, "rotate")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "rotate" in klass.__dict__:
            descriptor = klass.__dict__["rotate"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_color():
    assert hasattr(gama::ELayerAspect, "color")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_radius():
    assert hasattr(gama::ELayerAspect, "radius")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "radius" in klass.__dict__:
            descriptor = klass.__dict__["radius"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_type():
    assert hasattr(gama::ELayerAspect, "type")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_path():
    assert hasattr(gama::ELayerAspect, "path")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_empty():
    assert hasattr(gama::ELayerAspect, "empty")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "empty" in klass.__dict__:
            descriptor = klass.__dict__["empty"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_size():
    assert hasattr(gama::ELayerAspect, "size")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_gamlCode():
    assert hasattr(gama::ELayerAspect, "gamlCode")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_isColorCst():
    assert hasattr(gama::ELayerAspect, "isColorCst")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "isColorCst" in klass.__dict__:
            descriptor = klass.__dict__["isColorCst"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_points():
    assert hasattr(gama::ELayerAspect, "points")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_textSize():
    assert hasattr(gama::ELayerAspect, "textSize")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "textSize" in klass.__dict__:
            descriptor = klass.__dict__["textSize"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_text():
    assert hasattr(gama::ELayerAspect, "text")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_imageSize():
    assert hasattr(gama::ELayerAspect, "imageSize")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "imageSize" in klass.__dict__:
            descriptor = klass.__dict__["imageSize"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_colorRBG():
    assert hasattr(gama::ELayerAspect, "colorRBG")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "colorRBG" in klass.__dict__:
            descriptor = klass.__dict__["colorRBG"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_shape():
    assert hasattr(gama::ELayerAspect, "shape")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_heigth():
    assert hasattr(gama::ELayerAspect, "heigth")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "heigth" in klass.__dict__:
            descriptor = klass.__dict__["heigth"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_width():
    assert hasattr(gama::ELayerAspect, "width")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_gama::elayeraspect_has_expression():
    assert hasattr(gama::ELayerAspect, "expression")
    descriptor = None
    for klass in gama::ELayerAspect.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_gama::erulelink_is_not_abstract():
    assert not inspect.isabstract(gama::ERuleLink)


def test_gama::erulelink_constructor_exists():
    assert callable(gama::ERuleLink.__init__)


def test_gama::erulelink_constructor_args():
    sig = inspect.signature(gama::ERuleLink.__init__)
    params = list(sig.parameters.keys())



def test_gama::eperceivelink_is_not_abstract():
    assert not inspect.isabstract(gama::EPerceiveLink)


def test_gama::eperceivelink_constructor_exists():
    assert callable(gama::EPerceiveLink.__init__)


def test_gama::eperceivelink_constructor_args():
    sig = inspect.signature(gama::EPerceiveLink.__init__)
    params = list(sig.parameters.keys())



def test_gama::easpect_is_not_abstract():
    assert not inspect.isabstract(gama::EAspect)


def test_gama::easpect_constructor_exists():
    assert callable(gama::EAspect.__init__)


def test_gama::easpect_constructor_args():
    sig = inspect.signature(gama::EAspect.__init__)
    params = list(sig.parameters.keys())
    assert "defineGamlCode" in params, "Missing parameter 'defineGamlCode'"
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama::easpect_has_defineGamlCode():
    assert hasattr(gama::EAspect, "defineGamlCode")
    descriptor = None
    for klass in gama::EAspect.__mro__:
        if "defineGamlCode" in klass.__dict__:
            descriptor = klass.__dict__["defineGamlCode"]
            break
    assert isinstance(descriptor, property)

def test_gama::easpect_has_gamlCode():
    assert hasattr(gama::EAspect, "gamlCode")
    descriptor = None
    for klass in gama::EAspect.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama::etasklink_is_not_abstract():
    assert not inspect.isabstract(gama::ETaskLink)


def test_gama::etasklink_constructor_exists():
    assert callable(gama::ETaskLink.__init__)


def test_gama::etasklink_constructor_args():
    sig = inspect.signature(gama::ETaskLink.__init__)
    params = list(sig.parameters.keys())



def test_gama::estatelink_is_not_abstract():
    assert not inspect.isabstract(gama::EStateLink)


def test_gama::estatelink_constructor_exists():
    assert callable(gama::EStateLink.__init__)


def test_gama::estatelink_constructor_args():
    sig = inspect.signature(gama::EStateLink.__init__)
    params = list(sig.parameters.keys())



def test_gama::eplanlink_is_not_abstract():
    assert not inspect.isabstract(gama::EPlanLink)


def test_gama::eplanlink_constructor_exists():
    assert callable(gama::EPlanLink.__init__)


def test_gama::eplanlink_constructor_args():
    sig = inspect.signature(gama::EPlanLink.__init__)
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
EGamaObject_strategy = st.builds(
    EGamaObject,
)
gama::ESpecies_strategy = st.builds(
    gama::ESpecies,
    reflexList=
        safe_text,
    init=
        safe_text,
    skills=
        safe_text
)
gama::EFacet_strategy = st.builds(
    gama::EFacet,
    value=
        safe_text,
    name=
        safe_text
)
gama::EGamaLink_strategy = st.builds(
    gama::EGamaLink,
)
gama::EGamaObject_strategy = st.builds(
    gama::EGamaObject,
    error=
        safe_text,
    colorPicto=
        safe_text,
    name=
        safe_text,
    hasError=
        safe_text
)
gama::EGamaModel_strategy = st.builds(
    gama::EGamaModel,
    name=
        safe_text
)
gama::EVariable_strategy = st.builds(
    gama::EVariable,
    update=
        safe_text,
    function=
        safe_text,
    init=
        safe_text,
    max=
        safe_text,
    error=
        safe_text,
    hasError=
        safe_text,
    type=
        safe_text,
    min=
        safe_text,
    name=
        safe_text
)
gama::EEquation_strategy = st.builds(
    gama::EEquation,
    gamlCode=
        safe_text
)
gama::ERule_strategy = st.builds(
    gama::ERule,
    gamlCode=
        safe_text
)
gama::EPerceive_strategy = st.builds(
    gama::EPerceive,
    gamlCode=
        safe_text
)
gama::ETask_strategy = st.builds(
    gama::ETask,
    gamlCode=
        safe_text
)
gama::EState_strategy = st.builds(
    gama::EState,
    gamlCode=
        safe_text
)
gama::EPlan_strategy = st.builds(
    gama::EPlan,
    gamlCode=
        safe_text
)
gama::EChartLayer_strategy = st.builds(
    gama::EChartLayer,
    value=
        safe_text,
    color=
        safe_text,
    style=
        safe_text
)
gama::ELayer_strategy = st.builds(
    gama::ELayer,
    text=
        safe_text,
    file=
        safe_text,
    color=
        safe_text,
    isColorCst=
        safe_text,
    chart_type=
        safe_text,
    size=
        safe_text,
    agents=
        safe_text,
    aspect=
        safe_text,
    colorRBG=
        safe_text,
    type=
        safe_text,
    species=
        safe_text,
    grid=
        safe_text,
    showLines=
        st.booleans(),
    gamlCode=
        safe_text
)
gama::EDisplay_strategy = st.builds(
    gama::EDisplay,
    layerList=
        safe_text,
    gamlCode=
        safe_text,
    defineGamlCode=
        st.booleans()
)
gama::EAction_strategy = st.builds(
    gama::EAction,
    returnType=
        safe_text,
    gamlCode=
        safe_text
)
EGamaLink_strategy = st.builds(
    EGamaLink,
)
gama::EReflexLink_strategy = st.builds(
    gama::EReflexLink,
)
gama::EAspectLink_strategy = st.builds(
    gama::EAspectLink,
)
gama::EExperimentLink_strategy = st.builds(
    gama::EExperimentLink,
)
gama::ESubSpeciesLink_strategy = st.builds(
    gama::ESubSpeciesLink,
)
gama::EInheritLink_strategy = st.builds(
    gama::EInheritLink,
)
gama::EActionLink_strategy = st.builds(
    gama::EActionLink,
)
EExperiment_strategy = st.builds(
    EExperiment,
)
gama::EBatchExperiment_strategy = st.builds(
    gama::EBatchExperiment,
)
gama::EGUIExperiment_strategy = st.builds(
    gama::EGUIExperiment,
)
gama::EMonitor_strategy = st.builds(
    gama::EMonitor,
    value=
        safe_text
)
gama::EParameter_strategy = st.builds(
    gama::EParameter,
    category=
        safe_text,
    step=
        safe_text,
    min=
        safe_text,
    init=
        safe_text,
    among=
        safe_text,
    variable=
        safe_text,
    max=
        safe_text
)
gama::EDisplayLink_strategy = st.builds(
    gama::EDisplayLink,
)
ESpecies_strategy = st.builds(
    ESpecies,
)
gama::EWorldAgent_strategy = st.builds(
    gama::EWorldAgent,
)
gama::EGrid_strategy = st.builds(
    gama::EGrid,
)
gama::EExperiment_strategy = st.builds(
    gama::EExperiment,
)
gama::EReflex_strategy = st.builds(
    gama::EReflex,
    gamlCode=
        safe_text
)
gama::EEquationLink_strategy = st.builds(
    gama::EEquationLink,
)
gama::ELayerAspect_strategy = st.builds(
    gama::ELayerAspect,
    at=
        safe_text,
    texture=
        safe_text,
    shapeType=
        safe_text,
    depth=
        safe_text,
    rotate=
        safe_text,
    color=
        safe_text,
    radius=
        safe_text,
    type=
        safe_text,
    path=
        safe_text,
    empty=
        safe_text,
    size=
        safe_text,
    gamlCode=
        safe_text,
    isColorCst=
        safe_text,
    points=
        safe_text,
    textSize=
        safe_text,
    text=
        safe_text,
    imageSize=
        safe_text,
    colorRBG=
        safe_text,
    shape=
        safe_text,
    heigth=
        safe_text,
    width=
        safe_text,
    expression=
        safe_text
)
gama::ERuleLink_strategy = st.builds(
    gama::ERuleLink,
)
gama::EPerceiveLink_strategy = st.builds(
    gama::EPerceiveLink,
)
gama::EAspect_strategy = st.builds(
    gama::EAspect,
    defineGamlCode=
        st.booleans(),
    gamlCode=
        safe_text
)
gama::ETaskLink_strategy = st.builds(
    gama::ETaskLink,
)
gama::EStateLink_strategy = st.builds(
    gama::EStateLink,
)
gama::EPlanLink_strategy = st.builds(
    gama::EPlanLink,
)

@given(instance=EGamaObject_strategy)
@settings(max_examples=50)
def test_egamaobject_instantiation(instance):
    assert isinstance(instance, EGamaObject)

@given(instance=gama::ESpecies_strategy)
@settings(max_examples=50)
def test_gama::especies_instantiation(instance):
    assert isinstance(instance, gama::ESpecies)

@given(instance=gama::ESpecies_strategy)
def test_gama::especies_reflexList_type(instance):
    assert isinstance(instance.reflexList, str)


@given(instance=gama::ESpecies_strategy)
def test_gama::especies_reflexList_setter(instance):
    original = instance.reflexList
    instance.reflexList = original
    assert instance.reflexList == original

@given(instance=gama::ESpecies_strategy)
def test_gama::especies_init_type(instance):
    assert isinstance(instance.init, str)


@given(instance=gama::ESpecies_strategy)
def test_gama::especies_init_setter(instance):
    original = instance.init
    instance.init = original
    assert instance.init == original

@given(instance=gama::ESpecies_strategy)
def test_gama::especies_skills_type(instance):
    assert isinstance(instance.skills, str)


@given(instance=gama::ESpecies_strategy)
def test_gama::especies_skills_setter(instance):
    original = instance.skills
    instance.skills = original
    assert instance.skills == original

@given(instance=gama::EFacet_strategy)
@settings(max_examples=50)
def test_gama::efacet_instantiation(instance):
    assert isinstance(instance, gama::EFacet)

@given(instance=gama::EFacet_strategy)
def test_gama::efacet_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=gama::EFacet_strategy)
def test_gama::efacet_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gama::EFacet_strategy)
def test_gama::efacet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gama::EFacet_strategy)
def test_gama::efacet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gama::EGamaLink_strategy)
@settings(max_examples=50)
def test_gama::egamalink_instantiation(instance):
    assert isinstance(instance, gama::EGamaLink)

@given(instance=gama::EGamaObject_strategy)
@settings(max_examples=50)
def test_gama::egamaobject_instantiation(instance):
    assert isinstance(instance, gama::EGamaObject)

@given(instance=gama::EGamaObject_strategy)
def test_gama::egamaobject_error_type(instance):
    assert isinstance(instance.error, str)


@given(instance=gama::EGamaObject_strategy)
def test_gama::egamaobject_error_setter(instance):
    original = instance.error
    instance.error = original
    assert instance.error == original

@given(instance=gama::EGamaObject_strategy)
def test_gama::egamaobject_colorPicto_type(instance):
    assert isinstance(instance.colorPicto, str)


@given(instance=gama::EGamaObject_strategy)
def test_gama::egamaobject_colorPicto_setter(instance):
    original = instance.colorPicto
    instance.colorPicto = original
    assert instance.colorPicto == original

@given(instance=gama::EGamaObject_strategy)
def test_gama::egamaobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gama::EGamaObject_strategy)
def test_gama::egamaobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gama::EGamaObject_strategy)
def test_gama::egamaobject_hasError_type(instance):
    assert isinstance(instance.hasError, str)


@given(instance=gama::EGamaObject_strategy)
def test_gama::egamaobject_hasError_setter(instance):
    original = instance.hasError
    instance.hasError = original
    assert instance.hasError == original

@given(instance=gama::EGamaModel_strategy)
@settings(max_examples=50)
def test_gama::egamamodel_instantiation(instance):
    assert isinstance(instance, gama::EGamaModel)

@given(instance=gama::EGamaModel_strategy)
def test_gama::egamamodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gama::EGamaModel_strategy)
def test_gama::egamamodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gama::EVariable_strategy)
@settings(max_examples=50)
def test_gama::evariable_instantiation(instance):
    assert isinstance(instance, gama::EVariable)

@given(instance=gama::EVariable_strategy)
def test_gama::evariable_update_type(instance):
    assert isinstance(instance.update, str)


@given(instance=gama::EVariable_strategy)
def test_gama::evariable_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original

@given(instance=gama::EVariable_strategy)
def test_gama::evariable_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=gama::EVariable_strategy)
def test_gama::evariable_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=gama::EVariable_strategy)
def test_gama::evariable_init_type(instance):
    assert isinstance(instance.init, str)


@given(instance=gama::EVariable_strategy)
def test_gama::evariable_init_setter(instance):
    original = instance.init
    instance.init = original
    assert instance.init == original

@given(instance=gama::EVariable_strategy)
def test_gama::evariable_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=gama::EVariable_strategy)
def test_gama::evariable_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=gama::EVariable_strategy)
def test_gama::evariable_error_type(instance):
    assert isinstance(instance.error, str)


@given(instance=gama::EVariable_strategy)
def test_gama::evariable_error_setter(instance):
    original = instance.error
    instance.error = original
    assert instance.error == original

@given(instance=gama::EVariable_strategy)
def test_gama::evariable_hasError_type(instance):
    assert isinstance(instance.hasError, str)


@given(instance=gama::EVariable_strategy)
def test_gama::evariable_hasError_setter(instance):
    original = instance.hasError
    instance.hasError = original
    assert instance.hasError == original

@given(instance=gama::EVariable_strategy)
def test_gama::evariable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=gama::EVariable_strategy)
def test_gama::evariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=gama::EVariable_strategy)
def test_gama::evariable_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=gama::EVariable_strategy)
def test_gama::evariable_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=gama::EVariable_strategy)
def test_gama::evariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gama::EVariable_strategy)
def test_gama::evariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gama::EEquation_strategy)
@settings(max_examples=50)
def test_gama::eequation_instantiation(instance):
    assert isinstance(instance, gama::EEquation)

@given(instance=gama::EEquation_strategy)
def test_gama::eequation_gamlCode_type(instance):
    assert isinstance(instance.gamlCode, str)


@given(instance=gama::EEquation_strategy)
def test_gama::eequation_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama::ERule_strategy)
@settings(max_examples=50)
def test_gama::erule_instantiation(instance):
    assert isinstance(instance, gama::ERule)

@given(instance=gama::ERule_strategy)
def test_gama::erule_gamlCode_type(instance):
    assert isinstance(instance.gamlCode, str)


@given(instance=gama::ERule_strategy)
def test_gama::erule_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama::EPerceive_strategy)
@settings(max_examples=50)
def test_gama::eperceive_instantiation(instance):
    assert isinstance(instance, gama::EPerceive)

@given(instance=gama::EPerceive_strategy)
def test_gama::eperceive_gamlCode_type(instance):
    assert isinstance(instance.gamlCode, str)


@given(instance=gama::EPerceive_strategy)
def test_gama::eperceive_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama::ETask_strategy)
@settings(max_examples=50)
def test_gama::etask_instantiation(instance):
    assert isinstance(instance, gama::ETask)

@given(instance=gama::ETask_strategy)
def test_gama::etask_gamlCode_type(instance):
    assert isinstance(instance.gamlCode, str)


@given(instance=gama::ETask_strategy)
def test_gama::etask_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama::EState_strategy)
@settings(max_examples=50)
def test_gama::estate_instantiation(instance):
    assert isinstance(instance, gama::EState)

@given(instance=gama::EState_strategy)
def test_gama::estate_gamlCode_type(instance):
    assert isinstance(instance.gamlCode, str)


@given(instance=gama::EState_strategy)
def test_gama::estate_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama::EPlan_strategy)
@settings(max_examples=50)
def test_gama::eplan_instantiation(instance):
    assert isinstance(instance, gama::EPlan)

@given(instance=gama::EPlan_strategy)
def test_gama::eplan_gamlCode_type(instance):
    assert isinstance(instance.gamlCode, str)


@given(instance=gama::EPlan_strategy)
def test_gama::eplan_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama::EChartLayer_strategy)
@settings(max_examples=50)
def test_gama::echartlayer_instantiation(instance):
    assert isinstance(instance, gama::EChartLayer)

@given(instance=gama::EChartLayer_strategy)
def test_gama::echartlayer_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=gama::EChartLayer_strategy)
def test_gama::echartlayer_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gama::EChartLayer_strategy)
def test_gama::echartlayer_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=gama::EChartLayer_strategy)
def test_gama::echartlayer_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=gama::EChartLayer_strategy)
def test_gama::echartlayer_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=gama::EChartLayer_strategy)
def test_gama::echartlayer_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=gama::ELayer_strategy)
@settings(max_examples=50)
def test_gama::elayer_instantiation(instance):
    assert isinstance(instance, gama::ELayer)

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_isColorCst_type(instance):
    assert isinstance(instance.isColorCst, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_isColorCst_setter(instance):
    original = instance.isColorCst
    instance.isColorCst = original
    assert instance.isColorCst == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_chart_type_type(instance):
    assert isinstance(instance.chart_type, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_chart_type_setter(instance):
    original = instance.chart_type
    instance.chart_type = original
    assert instance.chart_type == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_agents_type(instance):
    assert isinstance(instance.agents, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_agents_setter(instance):
    original = instance.agents
    instance.agents = original
    assert instance.agents == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_aspect_type(instance):
    assert isinstance(instance.aspect, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_aspect_setter(instance):
    original = instance.aspect
    instance.aspect = original
    assert instance.aspect == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_colorRBG_type(instance):
    assert isinstance(instance.colorRBG, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_colorRBG_setter(instance):
    original = instance.colorRBG
    instance.colorRBG = original
    assert instance.colorRBG == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_species_type(instance):
    assert isinstance(instance.species, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_species_setter(instance):
    original = instance.species
    instance.species = original
    assert instance.species == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_grid_type(instance):
    assert isinstance(instance.grid, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_grid_setter(instance):
    original = instance.grid
    instance.grid = original
    assert instance.grid == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_showLines_type(instance):
    assert isinstance(instance.showLines, bool)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_showLines_setter(instance):
    original = instance.showLines
    instance.showLines = original
    assert instance.showLines == original

@given(instance=gama::ELayer_strategy)
def test_gama::elayer_gamlCode_type(instance):
    assert isinstance(instance.gamlCode, str)


@given(instance=gama::ELayer_strategy)
def test_gama::elayer_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama::EDisplay_strategy)
@settings(max_examples=50)
def test_gama::edisplay_instantiation(instance):
    assert isinstance(instance, gama::EDisplay)

@given(instance=gama::EDisplay_strategy)
def test_gama::edisplay_layerList_type(instance):
    assert isinstance(instance.layerList, str)


@given(instance=gama::EDisplay_strategy)
def test_gama::edisplay_layerList_setter(instance):
    original = instance.layerList
    instance.layerList = original
    assert instance.layerList == original

@given(instance=gama::EDisplay_strategy)
def test_gama::edisplay_gamlCode_type(instance):
    assert isinstance(instance.gamlCode, str)


@given(instance=gama::EDisplay_strategy)
def test_gama::edisplay_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama::EDisplay_strategy)
def test_gama::edisplay_defineGamlCode_type(instance):
    assert isinstance(instance.defineGamlCode, bool)


@given(instance=gama::EDisplay_strategy)
def test_gama::edisplay_defineGamlCode_setter(instance):
    original = instance.defineGamlCode
    instance.defineGamlCode = original
    assert instance.defineGamlCode == original

@given(instance=gama::EAction_strategy)
@settings(max_examples=50)
def test_gama::eaction_instantiation(instance):
    assert isinstance(instance, gama::EAction)

@given(instance=gama::EAction_strategy)
def test_gama::eaction_returnType_type(instance):
    assert isinstance(instance.returnType, str)


@given(instance=gama::EAction_strategy)
def test_gama::eaction_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original

@given(instance=gama::EAction_strategy)
def test_gama::eaction_gamlCode_type(instance):
    assert isinstance(instance.gamlCode, str)


@given(instance=gama::EAction_strategy)
def test_gama::eaction_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=EGamaLink_strategy)
@settings(max_examples=50)
def test_egamalink_instantiation(instance):
    assert isinstance(instance, EGamaLink)

@given(instance=gama::EReflexLink_strategy)
@settings(max_examples=50)
def test_gama::ereflexlink_instantiation(instance):
    assert isinstance(instance, gama::EReflexLink)

@given(instance=gama::EAspectLink_strategy)
@settings(max_examples=50)
def test_gama::easpectlink_instantiation(instance):
    assert isinstance(instance, gama::EAspectLink)

@given(instance=gama::EExperimentLink_strategy)
@settings(max_examples=50)
def test_gama::eexperimentlink_instantiation(instance):
    assert isinstance(instance, gama::EExperimentLink)

@given(instance=gama::ESubSpeciesLink_strategy)
@settings(max_examples=50)
def test_gama::esubspecieslink_instantiation(instance):
    assert isinstance(instance, gama::ESubSpeciesLink)

@given(instance=gama::EInheritLink_strategy)
@settings(max_examples=50)
def test_gama::einheritlink_instantiation(instance):
    assert isinstance(instance, gama::EInheritLink)

@given(instance=gama::EActionLink_strategy)
@settings(max_examples=50)
def test_gama::eactionlink_instantiation(instance):
    assert isinstance(instance, gama::EActionLink)

@given(instance=EExperiment_strategy)
@settings(max_examples=50)
def test_eexperiment_instantiation(instance):
    assert isinstance(instance, EExperiment)

@given(instance=gama::EBatchExperiment_strategy)
@settings(max_examples=50)
def test_gama::ebatchexperiment_instantiation(instance):
    assert isinstance(instance, gama::EBatchExperiment)

@given(instance=gama::EGUIExperiment_strategy)
@settings(max_examples=50)
def test_gama::eguiexperiment_instantiation(instance):
    assert isinstance(instance, gama::EGUIExperiment)

@given(instance=gama::EMonitor_strategy)
@settings(max_examples=50)
def test_gama::emonitor_instantiation(instance):
    assert isinstance(instance, gama::EMonitor)

@given(instance=gama::EMonitor_strategy)
def test_gama::emonitor_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=gama::EMonitor_strategy)
def test_gama::emonitor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gama::EParameter_strategy)
@settings(max_examples=50)
def test_gama::eparameter_instantiation(instance):
    assert isinstance(instance, gama::EParameter)

@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_step_type(instance):
    assert isinstance(instance.step, str)


@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_step_setter(instance):
    original = instance.step
    instance.step = original
    assert instance.step == original

@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_init_type(instance):
    assert isinstance(instance.init, str)


@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_init_setter(instance):
    original = instance.init
    instance.init = original
    assert instance.init == original

@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_among_type(instance):
    assert isinstance(instance.among, str)


@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_among_setter(instance):
    original = instance.among
    instance.among = original
    assert instance.among == original

@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=gama::EParameter_strategy)
def test_gama::eparameter_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=gama::EDisplayLink_strategy)
@settings(max_examples=50)
def test_gama::edisplaylink_instantiation(instance):
    assert isinstance(instance, gama::EDisplayLink)

@given(instance=ESpecies_strategy)
@settings(max_examples=50)
def test_especies_instantiation(instance):
    assert isinstance(instance, ESpecies)

@given(instance=gama::EWorldAgent_strategy)
@settings(max_examples=50)
def test_gama::eworldagent_instantiation(instance):
    assert isinstance(instance, gama::EWorldAgent)

@given(instance=gama::EGrid_strategy)
@settings(max_examples=50)
def test_gama::egrid_instantiation(instance):
    assert isinstance(instance, gama::EGrid)

@given(instance=gama::EExperiment_strategy)
@settings(max_examples=50)
def test_gama::eexperiment_instantiation(instance):
    assert isinstance(instance, gama::EExperiment)

@given(instance=gama::EReflex_strategy)
@settings(max_examples=50)
def test_gama::ereflex_instantiation(instance):
    assert isinstance(instance, gama::EReflex)

@given(instance=gama::EReflex_strategy)
def test_gama::ereflex_gamlCode_type(instance):
    assert isinstance(instance.gamlCode, str)


@given(instance=gama::EReflex_strategy)
def test_gama::ereflex_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama::EEquationLink_strategy)
@settings(max_examples=50)
def test_gama::eequationlink_instantiation(instance):
    assert isinstance(instance, gama::EEquationLink)

@given(instance=gama::ELayerAspect_strategy)
@settings(max_examples=50)
def test_gama::elayeraspect_instantiation(instance):
    assert isinstance(instance, gama::ELayerAspect)

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_at_type(instance):
    assert isinstance(instance.at, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_at_setter(instance):
    original = instance.at
    instance.at = original
    assert instance.at == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_texture_type(instance):
    assert isinstance(instance.texture, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_texture_setter(instance):
    original = instance.texture
    instance.texture = original
    assert instance.texture == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_shapeType_type(instance):
    assert isinstance(instance.shapeType, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_shapeType_setter(instance):
    original = instance.shapeType
    instance.shapeType = original
    assert instance.shapeType == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_depth_type(instance):
    assert isinstance(instance.depth, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_depth_setter(instance):
    original = instance.depth
    instance.depth = original
    assert instance.depth == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_rotate_type(instance):
    assert isinstance(instance.rotate, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_rotate_setter(instance):
    original = instance.rotate
    instance.rotate = original
    assert instance.rotate == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_radius_type(instance):
    assert isinstance(instance.radius, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_radius_setter(instance):
    original = instance.radius
    instance.radius = original
    assert instance.radius == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_empty_type(instance):
    assert isinstance(instance.empty, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_empty_setter(instance):
    original = instance.empty
    instance.empty = original
    assert instance.empty == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_gamlCode_type(instance):
    assert isinstance(instance.gamlCode, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_isColorCst_type(instance):
    assert isinstance(instance.isColorCst, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_isColorCst_setter(instance):
    original = instance.isColorCst
    instance.isColorCst = original
    assert instance.isColorCst == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_points_type(instance):
    assert isinstance(instance.points, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_textSize_type(instance):
    assert isinstance(instance.textSize, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_textSize_setter(instance):
    original = instance.textSize
    instance.textSize = original
    assert instance.textSize == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_imageSize_type(instance):
    assert isinstance(instance.imageSize, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_imageSize_setter(instance):
    original = instance.imageSize
    instance.imageSize = original
    assert instance.imageSize == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_colorRBG_type(instance):
    assert isinstance(instance.colorRBG, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_colorRBG_setter(instance):
    original = instance.colorRBG
    instance.colorRBG = original
    assert instance.colorRBG == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_heigth_type(instance):
    assert isinstance(instance.heigth, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_heigth_setter(instance):
    original = instance.heigth
    instance.heigth = original
    assert instance.heigth == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=gama::ELayerAspect_strategy)
def test_gama::elayeraspect_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=gama::ERuleLink_strategy)
@settings(max_examples=50)
def test_gama::erulelink_instantiation(instance):
    assert isinstance(instance, gama::ERuleLink)

@given(instance=gama::EPerceiveLink_strategy)
@settings(max_examples=50)
def test_gama::eperceivelink_instantiation(instance):
    assert isinstance(instance, gama::EPerceiveLink)

@given(instance=gama::EAspect_strategy)
@settings(max_examples=50)
def test_gama::easpect_instantiation(instance):
    assert isinstance(instance, gama::EAspect)

@given(instance=gama::EAspect_strategy)
def test_gama::easpect_defineGamlCode_type(instance):
    assert isinstance(instance.defineGamlCode, bool)


@given(instance=gama::EAspect_strategy)
def test_gama::easpect_defineGamlCode_setter(instance):
    original = instance.defineGamlCode
    instance.defineGamlCode = original
    assert instance.defineGamlCode == original

@given(instance=gama::EAspect_strategy)
def test_gama::easpect_gamlCode_type(instance):
    assert isinstance(instance.gamlCode, str)


@given(instance=gama::EAspect_strategy)
def test_gama::easpect_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama::ETaskLink_strategy)
@settings(max_examples=50)
def test_gama::etasklink_instantiation(instance):
    assert isinstance(instance, gama::ETaskLink)

@given(instance=gama::EStateLink_strategy)
@settings(max_examples=50)
def test_gama::estatelink_instantiation(instance):
    assert isinstance(instance, gama::EStateLink)

@given(instance=gama::EPlanLink_strategy)
@settings(max_examples=50)
def test_gama::eplanlink_instantiation(instance):
    assert isinstance(instance, gama::EPlanLink)
