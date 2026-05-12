import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EGamaLink,
    EExperiment,
    gama_EBatchExperiment,
    gama_EGUIExperiment,
    gama_EDisplayLink,
    ESpecies,
    gama_EWorldAgent,
    gama_EGrid,
    gama_EExperiment,
    gama_EEquationLink,
    gama_ERuleLink,
    gama_EPerceiveLink,
    gama_ETaskLink,
    gama_EStateLink,
    gama_EPlanLink,
    gama_EInheritLink,
    EGamaObject,
    gama_EAspect,
    gama_EDisplay,
    gama_EAction,
    gama_EMonitor,
    gama_ELayerAspect,
    gama_EReflex,
    gama_EParameter,
    gama_EState,
    gama_EChartLayer,
    gama_EEquation,
    gama_ERule,
    gama_ETask,
    gama_ELayer,
    gama_EPlan,
    gama_EPerceive,
    gama_ESpecies,
    gama_EFacet,
    gama_EGamaLink,
    gama_EGamaObject,
    gama_EGamaModel,
    gama_ESubSpeciesLink,
    gama_EReflexLink,
    gama_EActionLink,
    gama_EAspectLink,
    gama_EExperimentLink,
    gama_EVariable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_egamalink_is_not_abstract():
    assert not inspect.isabstract(EGamaLink)


def test_egamalink_constructor_exists():
    assert callable(EGamaLink.__init__)


def test_egamalink_constructor_args():
    sig = inspect.signature(EGamaLink.__init__)
    params = list(sig.parameters.keys())



def test_eexperiment_is_not_abstract():
    assert not inspect.isabstract(EExperiment)


def test_eexperiment_constructor_exists():
    assert callable(EExperiment.__init__)


def test_eexperiment_constructor_args():
    sig = inspect.signature(EExperiment.__init__)
    params = list(sig.parameters.keys())



def test_gama_ebatchexperiment_is_not_abstract():
    assert not inspect.isabstract(gama_EBatchExperiment)


def test_gama_ebatchexperiment_constructor_exists():
    assert callable(gama_EBatchExperiment.__init__)


def test_gama_ebatchexperiment_constructor_args():
    sig = inspect.signature(gama_EBatchExperiment.__init__)
    params = list(sig.parameters.keys())



def test_gama_eguiexperiment_is_not_abstract():
    assert not inspect.isabstract(gama_EGUIExperiment)


def test_gama_eguiexperiment_constructor_exists():
    assert callable(gama_EGUIExperiment.__init__)


def test_gama_eguiexperiment_constructor_args():
    sig = inspect.signature(gama_EGUIExperiment.__init__)
    params = list(sig.parameters.keys())



def test_gama_edisplaylink_is_not_abstract():
    assert not inspect.isabstract(gama_EDisplayLink)


def test_gama_edisplaylink_constructor_exists():
    assert callable(gama_EDisplayLink.__init__)


def test_gama_edisplaylink_constructor_args():
    sig = inspect.signature(gama_EDisplayLink.__init__)
    params = list(sig.parameters.keys())



def test_especies_is_not_abstract():
    assert not inspect.isabstract(ESpecies)


def test_especies_constructor_exists():
    assert callable(ESpecies.__init__)


def test_especies_constructor_args():
    sig = inspect.signature(ESpecies.__init__)
    params = list(sig.parameters.keys())



def test_gama_eworldagent_is_not_abstract():
    assert not inspect.isabstract(gama_EWorldAgent)


def test_gama_eworldagent_constructor_exists():
    assert callable(gama_EWorldAgent.__init__)


def test_gama_eworldagent_constructor_args():
    sig = inspect.signature(gama_EWorldAgent.__init__)
    params = list(sig.parameters.keys())



def test_gama_egrid_is_not_abstract():
    assert not inspect.isabstract(gama_EGrid)


def test_gama_egrid_constructor_exists():
    assert callable(gama_EGrid.__init__)


def test_gama_egrid_constructor_args():
    sig = inspect.signature(gama_EGrid.__init__)
    params = list(sig.parameters.keys())



def test_gama_eexperiment_is_not_abstract():
    assert not inspect.isabstract(gama_EExperiment)


def test_gama_eexperiment_constructor_exists():
    assert callable(gama_EExperiment.__init__)


def test_gama_eexperiment_constructor_args():
    sig = inspect.signature(gama_EExperiment.__init__)
    params = list(sig.parameters.keys())



def test_gama_eequationlink_is_not_abstract():
    assert not inspect.isabstract(gama_EEquationLink)


def test_gama_eequationlink_constructor_exists():
    assert callable(gama_EEquationLink.__init__)


def test_gama_eequationlink_constructor_args():
    sig = inspect.signature(gama_EEquationLink.__init__)
    params = list(sig.parameters.keys())



def test_gama_erulelink_is_not_abstract():
    assert not inspect.isabstract(gama_ERuleLink)


def test_gama_erulelink_constructor_exists():
    assert callable(gama_ERuleLink.__init__)


def test_gama_erulelink_constructor_args():
    sig = inspect.signature(gama_ERuleLink.__init__)
    params = list(sig.parameters.keys())



def test_gama_eperceivelink_is_not_abstract():
    assert not inspect.isabstract(gama_EPerceiveLink)


def test_gama_eperceivelink_constructor_exists():
    assert callable(gama_EPerceiveLink.__init__)


def test_gama_eperceivelink_constructor_args():
    sig = inspect.signature(gama_EPerceiveLink.__init__)
    params = list(sig.parameters.keys())



def test_gama_etasklink_is_not_abstract():
    assert not inspect.isabstract(gama_ETaskLink)


def test_gama_etasklink_constructor_exists():
    assert callable(gama_ETaskLink.__init__)


def test_gama_etasklink_constructor_args():
    sig = inspect.signature(gama_ETaskLink.__init__)
    params = list(sig.parameters.keys())



def test_gama_estatelink_is_not_abstract():
    assert not inspect.isabstract(gama_EStateLink)


def test_gama_estatelink_constructor_exists():
    assert callable(gama_EStateLink.__init__)


def test_gama_estatelink_constructor_args():
    sig = inspect.signature(gama_EStateLink.__init__)
    params = list(sig.parameters.keys())



def test_gama_eplanlink_is_not_abstract():
    assert not inspect.isabstract(gama_EPlanLink)


def test_gama_eplanlink_constructor_exists():
    assert callable(gama_EPlanLink.__init__)


def test_gama_eplanlink_constructor_args():
    sig = inspect.signature(gama_EPlanLink.__init__)
    params = list(sig.parameters.keys())



def test_gama_einheritlink_is_not_abstract():
    assert not inspect.isabstract(gama_EInheritLink)


def test_gama_einheritlink_constructor_exists():
    assert callable(gama_EInheritLink.__init__)


def test_gama_einheritlink_constructor_args():
    sig = inspect.signature(gama_EInheritLink.__init__)
    params = list(sig.parameters.keys())



def test_egamaobject_is_not_abstract():
    assert not inspect.isabstract(EGamaObject)


def test_egamaobject_constructor_exists():
    assert callable(EGamaObject.__init__)


def test_egamaobject_constructor_args():
    sig = inspect.signature(EGamaObject.__init__)
    params = list(sig.parameters.keys())



def test_gama_easpect_is_not_abstract():
    assert not inspect.isabstract(gama_EAspect)


def test_gama_easpect_constructor_exists():
    assert callable(gama_EAspect.__init__)


def test_gama_easpect_constructor_args():
    sig = inspect.signature(gama_EAspect.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"
    assert "defineGamlCode" in params, "Missing parameter 'defineGamlCode'"

def test_gama_easpect_has_gamlCode():
    assert hasattr(gama_EAspect, "gamlCode")
    descriptor = None
    for klass in gama_EAspect.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)

def test_gama_easpect_has_defineGamlCode():
    assert hasattr(gama_EAspect, "defineGamlCode")
    descriptor = None
    for klass in gama_EAspect.__mro__:
        if "defineGamlCode" in klass.__dict__:
            descriptor = klass.__dict__["defineGamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama_edisplay_is_not_abstract():
    assert not inspect.isabstract(gama_EDisplay)


def test_gama_edisplay_constructor_exists():
    assert callable(gama_EDisplay.__init__)


def test_gama_edisplay_constructor_args():
    sig = inspect.signature(gama_EDisplay.__init__)
    params = list(sig.parameters.keys())
    assert "defineGamlCode" in params, "Missing parameter 'defineGamlCode'"
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"
    assert "layerList" in params, "Missing parameter 'layerList'"

def test_gama_edisplay_has_defineGamlCode():
    assert hasattr(gama_EDisplay, "defineGamlCode")
    descriptor = None
    for klass in gama_EDisplay.__mro__:
        if "defineGamlCode" in klass.__dict__:
            descriptor = klass.__dict__["defineGamlCode"]
            break
    assert isinstance(descriptor, property)

def test_gama_edisplay_has_gamlCode():
    assert hasattr(gama_EDisplay, "gamlCode")
    descriptor = None
    for klass in gama_EDisplay.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)

def test_gama_edisplay_has_layerList():
    assert hasattr(gama_EDisplay, "layerList")
    descriptor = None
    for klass in gama_EDisplay.__mro__:
        if "layerList" in klass.__dict__:
            descriptor = klass.__dict__["layerList"]
            break
    assert isinstance(descriptor, property)



def test_gama_eaction_is_not_abstract():
    assert not inspect.isabstract(gama_EAction)


def test_gama_eaction_constructor_exists():
    assert callable(gama_EAction.__init__)


def test_gama_eaction_constructor_args():
    sig = inspect.signature(gama_EAction.__init__)
    params = list(sig.parameters.keys())
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama_eaction_has_returnType():
    assert hasattr(gama_EAction, "returnType")
    descriptor = None
    for klass in gama_EAction.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)

def test_gama_eaction_has_gamlCode():
    assert hasattr(gama_EAction, "gamlCode")
    descriptor = None
    for klass in gama_EAction.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama_emonitor_is_not_abstract():
    assert not inspect.isabstract(gama_EMonitor)


def test_gama_emonitor_constructor_exists():
    assert callable(gama_EMonitor.__init__)


def test_gama_emonitor_constructor_args():
    sig = inspect.signature(gama_EMonitor.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gama_emonitor_has_value():
    assert hasattr(gama_EMonitor, "value")
    descriptor = None
    for klass in gama_EMonitor.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gama_elayeraspect_is_not_abstract():
    assert not inspect.isabstract(gama_ELayerAspect)


def test_gama_elayeraspect_constructor_exists():
    assert callable(gama_ELayerAspect.__init__)


def test_gama_elayeraspect_constructor_args():
    sig = inspect.signature(gama_ELayerAspect.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "imageSize" in params, "Missing parameter 'imageSize'"
    assert "at" in params, "Missing parameter 'at'"
    assert "points" in params, "Missing parameter 'points'"
    assert "isColorCst" in params, "Missing parameter 'isColorCst'"
    assert "color" in params, "Missing parameter 'color'"
    assert "depth" in params, "Missing parameter 'depth'"
    assert "rotate" in params, "Missing parameter 'rotate'"
    assert "heigth" in params, "Missing parameter 'heigth'"
    assert "width" in params, "Missing parameter 'width'"
    assert "radius" in params, "Missing parameter 'radius'"
    assert "empty" in params, "Missing parameter 'empty'"
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"
    assert "shapeType" in params, "Missing parameter 'shapeType'"
    assert "type" in params, "Missing parameter 'type'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "path" in params, "Missing parameter 'path'"
    assert "textSize" in params, "Missing parameter 'textSize'"
    assert "texture" in params, "Missing parameter 'texture'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "colorRBG" in params, "Missing parameter 'colorRBG'"
    assert "size" in params, "Missing parameter 'size'"

def test_gama_elayeraspect_has_text():
    assert hasattr(gama_ELayerAspect, "text")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_imageSize():
    assert hasattr(gama_ELayerAspect, "imageSize")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "imageSize" in klass.__dict__:
            descriptor = klass.__dict__["imageSize"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_at():
    assert hasattr(gama_ELayerAspect, "at")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "at" in klass.__dict__:
            descriptor = klass.__dict__["at"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_points():
    assert hasattr(gama_ELayerAspect, "points")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_isColorCst():
    assert hasattr(gama_ELayerAspect, "isColorCst")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "isColorCst" in klass.__dict__:
            descriptor = klass.__dict__["isColorCst"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_color():
    assert hasattr(gama_ELayerAspect, "color")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_depth():
    assert hasattr(gama_ELayerAspect, "depth")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "depth" in klass.__dict__:
            descriptor = klass.__dict__["depth"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_rotate():
    assert hasattr(gama_ELayerAspect, "rotate")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "rotate" in klass.__dict__:
            descriptor = klass.__dict__["rotate"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_heigth():
    assert hasattr(gama_ELayerAspect, "heigth")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "heigth" in klass.__dict__:
            descriptor = klass.__dict__["heigth"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_width():
    assert hasattr(gama_ELayerAspect, "width")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_radius():
    assert hasattr(gama_ELayerAspect, "radius")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "radius" in klass.__dict__:
            descriptor = klass.__dict__["radius"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_empty():
    assert hasattr(gama_ELayerAspect, "empty")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "empty" in klass.__dict__:
            descriptor = klass.__dict__["empty"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_gamlCode():
    assert hasattr(gama_ELayerAspect, "gamlCode")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_shapeType():
    assert hasattr(gama_ELayerAspect, "shapeType")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "shapeType" in klass.__dict__:
            descriptor = klass.__dict__["shapeType"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_type():
    assert hasattr(gama_ELayerAspect, "type")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_expression():
    assert hasattr(gama_ELayerAspect, "expression")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_path():
    assert hasattr(gama_ELayerAspect, "path")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_textSize():
    assert hasattr(gama_ELayerAspect, "textSize")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "textSize" in klass.__dict__:
            descriptor = klass.__dict__["textSize"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_texture():
    assert hasattr(gama_ELayerAspect, "texture")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "texture" in klass.__dict__:
            descriptor = klass.__dict__["texture"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_shape():
    assert hasattr(gama_ELayerAspect, "shape")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_colorRBG():
    assert hasattr(gama_ELayerAspect, "colorRBG")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "colorRBG" in klass.__dict__:
            descriptor = klass.__dict__["colorRBG"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayeraspect_has_size():
    assert hasattr(gama_ELayerAspect, "size")
    descriptor = None
    for klass in gama_ELayerAspect.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_gama_ereflex_is_not_abstract():
    assert not inspect.isabstract(gama_EReflex)


def test_gama_ereflex_constructor_exists():
    assert callable(gama_EReflex.__init__)


def test_gama_ereflex_constructor_args():
    sig = inspect.signature(gama_EReflex.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama_ereflex_has_gamlCode():
    assert hasattr(gama_EReflex, "gamlCode")
    descriptor = None
    for klass in gama_EReflex.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama_eparameter_is_not_abstract():
    assert not inspect.isabstract(gama_EParameter)


def test_gama_eparameter_constructor_exists():
    assert callable(gama_EParameter.__init__)


def test_gama_eparameter_constructor_args():
    sig = inspect.signature(gama_EParameter.__init__)
    params = list(sig.parameters.keys())
    assert "init" in params, "Missing parameter 'init'"
    assert "category" in params, "Missing parameter 'category'"
    assert "among" in params, "Missing parameter 'among'"
    assert "variable" in params, "Missing parameter 'variable'"
    assert "step" in params, "Missing parameter 'step'"
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_gama_eparameter_has_init():
    assert hasattr(gama_EParameter, "init")
    descriptor = None
    for klass in gama_EParameter.__mro__:
        if "init" in klass.__dict__:
            descriptor = klass.__dict__["init"]
            break
    assert isinstance(descriptor, property)

def test_gama_eparameter_has_category():
    assert hasattr(gama_EParameter, "category")
    descriptor = None
    for klass in gama_EParameter.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_gama_eparameter_has_among():
    assert hasattr(gama_EParameter, "among")
    descriptor = None
    for klass in gama_EParameter.__mro__:
        if "among" in klass.__dict__:
            descriptor = klass.__dict__["among"]
            break
    assert isinstance(descriptor, property)

def test_gama_eparameter_has_variable():
    assert hasattr(gama_EParameter, "variable")
    descriptor = None
    for klass in gama_EParameter.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)

def test_gama_eparameter_has_step():
    assert hasattr(gama_EParameter, "step")
    descriptor = None
    for klass in gama_EParameter.__mro__:
        if "step" in klass.__dict__:
            descriptor = klass.__dict__["step"]
            break
    assert isinstance(descriptor, property)

def test_gama_eparameter_has_min():
    assert hasattr(gama_EParameter, "min")
    descriptor = None
    for klass in gama_EParameter.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_gama_eparameter_has_max():
    assert hasattr(gama_EParameter, "max")
    descriptor = None
    for klass in gama_EParameter.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_gama_estate_is_not_abstract():
    assert not inspect.isabstract(gama_EState)


def test_gama_estate_constructor_exists():
    assert callable(gama_EState.__init__)


def test_gama_estate_constructor_args():
    sig = inspect.signature(gama_EState.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama_estate_has_gamlCode():
    assert hasattr(gama_EState, "gamlCode")
    descriptor = None
    for klass in gama_EState.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama_echartlayer_is_not_abstract():
    assert not inspect.isabstract(gama_EChartLayer)


def test_gama_echartlayer_constructor_exists():
    assert callable(gama_EChartLayer.__init__)


def test_gama_echartlayer_constructor_args():
    sig = inspect.signature(gama_EChartLayer.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "value" in params, "Missing parameter 'value'"
    assert "color" in params, "Missing parameter 'color'"

def test_gama_echartlayer_has_style():
    assert hasattr(gama_EChartLayer, "style")
    descriptor = None
    for klass in gama_EChartLayer.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_gama_echartlayer_has_value():
    assert hasattr(gama_EChartLayer, "value")
    descriptor = None
    for klass in gama_EChartLayer.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_gama_echartlayer_has_color():
    assert hasattr(gama_EChartLayer, "color")
    descriptor = None
    for klass in gama_EChartLayer.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_gama_eequation_is_not_abstract():
    assert not inspect.isabstract(gama_EEquation)


def test_gama_eequation_constructor_exists():
    assert callable(gama_EEquation.__init__)


def test_gama_eequation_constructor_args():
    sig = inspect.signature(gama_EEquation.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama_eequation_has_gamlCode():
    assert hasattr(gama_EEquation, "gamlCode")
    descriptor = None
    for klass in gama_EEquation.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama_erule_is_not_abstract():
    assert not inspect.isabstract(gama_ERule)


def test_gama_erule_constructor_exists():
    assert callable(gama_ERule.__init__)


def test_gama_erule_constructor_args():
    sig = inspect.signature(gama_ERule.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama_erule_has_gamlCode():
    assert hasattr(gama_ERule, "gamlCode")
    descriptor = None
    for klass in gama_ERule.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama_etask_is_not_abstract():
    assert not inspect.isabstract(gama_ETask)


def test_gama_etask_constructor_exists():
    assert callable(gama_ETask.__init__)


def test_gama_etask_constructor_args():
    sig = inspect.signature(gama_ETask.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama_etask_has_gamlCode():
    assert hasattr(gama_ETask, "gamlCode")
    descriptor = None
    for klass in gama_ETask.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama_elayer_is_not_abstract():
    assert not inspect.isabstract(gama_ELayer)


def test_gama_elayer_constructor_exists():
    assert callable(gama_ELayer.__init__)


def test_gama_elayer_constructor_args():
    sig = inspect.signature(gama_ELayer.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"
    assert "color" in params, "Missing parameter 'color'"
    assert "agents" in params, "Missing parameter 'agents'"
    assert "isColorCst" in params, "Missing parameter 'isColorCst'"
    assert "grid" in params, "Missing parameter 'grid'"
    assert "colorRBG" in params, "Missing parameter 'colorRBG'"
    assert "file" in params, "Missing parameter 'file'"
    assert "species" in params, "Missing parameter 'species'"
    assert "type" in params, "Missing parameter 'type'"
    assert "aspect" in params, "Missing parameter 'aspect'"
    assert "showLines" in params, "Missing parameter 'showLines'"
    assert "chart_type" in params, "Missing parameter 'chart_type'"
    assert "size" in params, "Missing parameter 'size'"

def test_gama_elayer_has_text():
    assert hasattr(gama_ELayer, "text")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_gamlCode():
    assert hasattr(gama_ELayer, "gamlCode")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_color():
    assert hasattr(gama_ELayer, "color")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_agents():
    assert hasattr(gama_ELayer, "agents")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "agents" in klass.__dict__:
            descriptor = klass.__dict__["agents"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_isColorCst():
    assert hasattr(gama_ELayer, "isColorCst")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "isColorCst" in klass.__dict__:
            descriptor = klass.__dict__["isColorCst"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_grid():
    assert hasattr(gama_ELayer, "grid")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "grid" in klass.__dict__:
            descriptor = klass.__dict__["grid"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_colorRBG():
    assert hasattr(gama_ELayer, "colorRBG")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "colorRBG" in klass.__dict__:
            descriptor = klass.__dict__["colorRBG"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_file():
    assert hasattr(gama_ELayer, "file")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_species():
    assert hasattr(gama_ELayer, "species")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "species" in klass.__dict__:
            descriptor = klass.__dict__["species"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_type():
    assert hasattr(gama_ELayer, "type")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_aspect():
    assert hasattr(gama_ELayer, "aspect")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "aspect" in klass.__dict__:
            descriptor = klass.__dict__["aspect"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_showLines():
    assert hasattr(gama_ELayer, "showLines")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "showLines" in klass.__dict__:
            descriptor = klass.__dict__["showLines"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_chart_type():
    assert hasattr(gama_ELayer, "chart_type")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "chart_type" in klass.__dict__:
            descriptor = klass.__dict__["chart_type"]
            break
    assert isinstance(descriptor, property)

def test_gama_elayer_has_size():
    assert hasattr(gama_ELayer, "size")
    descriptor = None
    for klass in gama_ELayer.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_gama_eplan_is_not_abstract():
    assert not inspect.isabstract(gama_EPlan)


def test_gama_eplan_constructor_exists():
    assert callable(gama_EPlan.__init__)


def test_gama_eplan_constructor_args():
    sig = inspect.signature(gama_EPlan.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama_eplan_has_gamlCode():
    assert hasattr(gama_EPlan, "gamlCode")
    descriptor = None
    for klass in gama_EPlan.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama_eperceive_is_not_abstract():
    assert not inspect.isabstract(gama_EPerceive)


def test_gama_eperceive_constructor_exists():
    assert callable(gama_EPerceive.__init__)


def test_gama_eperceive_constructor_args():
    sig = inspect.signature(gama_EPerceive.__init__)
    params = list(sig.parameters.keys())
    assert "gamlCode" in params, "Missing parameter 'gamlCode'"

def test_gama_eperceive_has_gamlCode():
    assert hasattr(gama_EPerceive, "gamlCode")
    descriptor = None
    for klass in gama_EPerceive.__mro__:
        if "gamlCode" in klass.__dict__:
            descriptor = klass.__dict__["gamlCode"]
            break
    assert isinstance(descriptor, property)



def test_gama_especies_is_not_abstract():
    assert not inspect.isabstract(gama_ESpecies)


def test_gama_especies_constructor_exists():
    assert callable(gama_ESpecies.__init__)


def test_gama_especies_constructor_args():
    sig = inspect.signature(gama_ESpecies.__init__)
    params = list(sig.parameters.keys())
    assert "skills" in params, "Missing parameter 'skills'"
    assert "init" in params, "Missing parameter 'init'"
    assert "reflexList" in params, "Missing parameter 'reflexList'"

def test_gama_especies_has_skills():
    assert hasattr(gama_ESpecies, "skills")
    descriptor = None
    for klass in gama_ESpecies.__mro__:
        if "skills" in klass.__dict__:
            descriptor = klass.__dict__["skills"]
            break
    assert isinstance(descriptor, property)

def test_gama_especies_has_init():
    assert hasattr(gama_ESpecies, "init")
    descriptor = None
    for klass in gama_ESpecies.__mro__:
        if "init" in klass.__dict__:
            descriptor = klass.__dict__["init"]
            break
    assert isinstance(descriptor, property)

def test_gama_especies_has_reflexList():
    assert hasattr(gama_ESpecies, "reflexList")
    descriptor = None
    for klass in gama_ESpecies.__mro__:
        if "reflexList" in klass.__dict__:
            descriptor = klass.__dict__["reflexList"]
            break
    assert isinstance(descriptor, property)



def test_gama_efacet_is_not_abstract():
    assert not inspect.isabstract(gama_EFacet)


def test_gama_efacet_constructor_exists():
    assert callable(gama_EFacet.__init__)


def test_gama_efacet_constructor_args():
    sig = inspect.signature(gama_EFacet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_gama_efacet_has_name():
    assert hasattr(gama_EFacet, "name")
    descriptor = None
    for klass in gama_EFacet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gama_efacet_has_value():
    assert hasattr(gama_EFacet, "value")
    descriptor = None
    for klass in gama_EFacet.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gama_egamalink_is_not_abstract():
    assert not inspect.isabstract(gama_EGamaLink)


def test_gama_egamalink_constructor_exists():
    assert callable(gama_EGamaLink.__init__)


def test_gama_egamalink_constructor_args():
    sig = inspect.signature(gama_EGamaLink.__init__)
    params = list(sig.parameters.keys())



def test_gama_egamaobject_is_not_abstract():
    assert not inspect.isabstract(gama_EGamaObject)


def test_gama_egamaobject_constructor_exists():
    assert callable(gama_EGamaObject.__init__)


def test_gama_egamaobject_constructor_args():
    sig = inspect.signature(gama_EGamaObject.__init__)
    params = list(sig.parameters.keys())
    assert "colorPicto" in params, "Missing parameter 'colorPicto'"
    assert "hasError" in params, "Missing parameter 'hasError'"
    assert "name" in params, "Missing parameter 'name'"
    assert "error" in params, "Missing parameter 'error'"

def test_gama_egamaobject_has_colorPicto():
    assert hasattr(gama_EGamaObject, "colorPicto")
    descriptor = None
    for klass in gama_EGamaObject.__mro__:
        if "colorPicto" in klass.__dict__:
            descriptor = klass.__dict__["colorPicto"]
            break
    assert isinstance(descriptor, property)

def test_gama_egamaobject_has_hasError():
    assert hasattr(gama_EGamaObject, "hasError")
    descriptor = None
    for klass in gama_EGamaObject.__mro__:
        if "hasError" in klass.__dict__:
            descriptor = klass.__dict__["hasError"]
            break
    assert isinstance(descriptor, property)

def test_gama_egamaobject_has_name():
    assert hasattr(gama_EGamaObject, "name")
    descriptor = None
    for klass in gama_EGamaObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gama_egamaobject_has_error():
    assert hasattr(gama_EGamaObject, "error")
    descriptor = None
    for klass in gama_EGamaObject.__mro__:
        if "error" in klass.__dict__:
            descriptor = klass.__dict__["error"]
            break
    assert isinstance(descriptor, property)



def test_gama_egamamodel_is_not_abstract():
    assert not inspect.isabstract(gama_EGamaModel)


def test_gama_egamamodel_constructor_exists():
    assert callable(gama_EGamaModel.__init__)


def test_gama_egamamodel_constructor_args():
    sig = inspect.signature(gama_EGamaModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gama_egamamodel_has_name():
    assert hasattr(gama_EGamaModel, "name")
    descriptor = None
    for klass in gama_EGamaModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gama_esubspecieslink_is_not_abstract():
    assert not inspect.isabstract(gama_ESubSpeciesLink)


def test_gama_esubspecieslink_constructor_exists():
    assert callable(gama_ESubSpeciesLink.__init__)


def test_gama_esubspecieslink_constructor_args():
    sig = inspect.signature(gama_ESubSpeciesLink.__init__)
    params = list(sig.parameters.keys())



def test_gama_ereflexlink_is_not_abstract():
    assert not inspect.isabstract(gama_EReflexLink)


def test_gama_ereflexlink_constructor_exists():
    assert callable(gama_EReflexLink.__init__)


def test_gama_ereflexlink_constructor_args():
    sig = inspect.signature(gama_EReflexLink.__init__)
    params = list(sig.parameters.keys())



def test_gama_eactionlink_is_not_abstract():
    assert not inspect.isabstract(gama_EActionLink)


def test_gama_eactionlink_constructor_exists():
    assert callable(gama_EActionLink.__init__)


def test_gama_eactionlink_constructor_args():
    sig = inspect.signature(gama_EActionLink.__init__)
    params = list(sig.parameters.keys())



def test_gama_easpectlink_is_not_abstract():
    assert not inspect.isabstract(gama_EAspectLink)


def test_gama_easpectlink_constructor_exists():
    assert callable(gama_EAspectLink.__init__)


def test_gama_easpectlink_constructor_args():
    sig = inspect.signature(gama_EAspectLink.__init__)
    params = list(sig.parameters.keys())



def test_gama_eexperimentlink_is_not_abstract():
    assert not inspect.isabstract(gama_EExperimentLink)


def test_gama_eexperimentlink_constructor_exists():
    assert callable(gama_EExperimentLink.__init__)


def test_gama_eexperimentlink_constructor_args():
    sig = inspect.signature(gama_EExperimentLink.__init__)
    params = list(sig.parameters.keys())



def test_gama_evariable_is_not_abstract():
    assert not inspect.isabstract(gama_EVariable)


def test_gama_evariable_constructor_exists():
    assert callable(gama_EVariable.__init__)


def test_gama_evariable_constructor_args():
    sig = inspect.signature(gama_EVariable.__init__)
    params = list(sig.parameters.keys())
    assert "hasError" in params, "Missing parameter 'hasError'"
    assert "error" in params, "Missing parameter 'error'"
    assert "name" in params, "Missing parameter 'name'"
    assert "init" in params, "Missing parameter 'init'"
    assert "update" in params, "Missing parameter 'update'"
    assert "max" in params, "Missing parameter 'max'"
    assert "function" in params, "Missing parameter 'function'"
    assert "type" in params, "Missing parameter 'type'"
    assert "min" in params, "Missing parameter 'min'"

def test_gama_evariable_has_hasError():
    assert hasattr(gama_EVariable, "hasError")
    descriptor = None
    for klass in gama_EVariable.__mro__:
        if "hasError" in klass.__dict__:
            descriptor = klass.__dict__["hasError"]
            break
    assert isinstance(descriptor, property)

def test_gama_evariable_has_error():
    assert hasattr(gama_EVariable, "error")
    descriptor = None
    for klass in gama_EVariable.__mro__:
        if "error" in klass.__dict__:
            descriptor = klass.__dict__["error"]
            break
    assert isinstance(descriptor, property)

def test_gama_evariable_has_name():
    assert hasattr(gama_EVariable, "name")
    descriptor = None
    for klass in gama_EVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gama_evariable_has_init():
    assert hasattr(gama_EVariable, "init")
    descriptor = None
    for klass in gama_EVariable.__mro__:
        if "init" in klass.__dict__:
            descriptor = klass.__dict__["init"]
            break
    assert isinstance(descriptor, property)

def test_gama_evariable_has_update():
    assert hasattr(gama_EVariable, "update")
    descriptor = None
    for klass in gama_EVariable.__mro__:
        if "update" in klass.__dict__:
            descriptor = klass.__dict__["update"]
            break
    assert isinstance(descriptor, property)

def test_gama_evariable_has_max():
    assert hasattr(gama_EVariable, "max")
    descriptor = None
    for klass in gama_EVariable.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_gama_evariable_has_function():
    assert hasattr(gama_EVariable, "function")
    descriptor = None
    for klass in gama_EVariable.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)

def test_gama_evariable_has_type():
    assert hasattr(gama_EVariable, "type")
    descriptor = None
    for klass in gama_EVariable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_gama_evariable_has_min():
    assert hasattr(gama_EVariable, "min")
    descriptor = None
    for klass in gama_EVariable.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)


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
EGamaLink_strategy = st.builds(
    EGamaLink,
)
EExperiment_strategy = st.builds(
    EExperiment,
)
gama_EBatchExperiment_strategy = st.builds(
    gama_EBatchExperiment,
)
gama_EGUIExperiment_strategy = st.builds(
    gama_EGUIExperiment,
)
gama_EDisplayLink_strategy = st.builds(
    gama_EDisplayLink,
)
ESpecies_strategy = st.builds(
    ESpecies,
)
gama_EWorldAgent_strategy = st.builds(
    gama_EWorldAgent,
)
gama_EGrid_strategy = st.builds(
    gama_EGrid,
)
gama_EExperiment_strategy = st.builds(
    gama_EExperiment,
)
gama_EEquationLink_strategy = st.builds(
    gama_EEquationLink,
)
gama_ERuleLink_strategy = st.builds(
    gama_ERuleLink,
)
gama_EPerceiveLink_strategy = st.builds(
    gama_EPerceiveLink,
)
gama_ETaskLink_strategy = st.builds(
    gama_ETaskLink,
)
gama_EStateLink_strategy = st.builds(
    gama_EStateLink,
)
gama_EPlanLink_strategy = st.builds(
    gama_EPlanLink,
)
gama_EInheritLink_strategy = st.builds(
    gama_EInheritLink,
)
EGamaObject_strategy = st.builds(
    EGamaObject,
)
gama_EAspect_strategy = st.builds(
    gama_EAspect,
    gamlCode=
        safe_text,
    defineGamlCode=
        st.booleans()
)
gama_EDisplay_strategy = st.builds(
    gama_EDisplay,
    defineGamlCode=
        st.booleans(),
    gamlCode=
        safe_text,
    layerList=
        safe_text
)
gama_EAction_strategy = st.builds(
    gama_EAction,
    returnType=
        safe_text,
    gamlCode=
        safe_text
)
gama_EMonitor_strategy = st.builds(
    gama_EMonitor,
    value=
        safe_text
)
gama_ELayerAspect_strategy = st.builds(
    gama_ELayerAspect,
    text=
        safe_text,
    imageSize=
        safe_text,
    at=
        safe_text,
    points=
        safe_text,
    isColorCst=
        safe_text,
    color=
        safe_text,
    depth=
        safe_text,
    rotate=
        safe_text,
    heigth=
        safe_text,
    width=
        safe_text,
    radius=
        safe_text,
    empty=
        safe_text,
    gamlCode=
        safe_text,
    shapeType=
        safe_text,
    type=
        safe_text,
    expression=
        safe_text,
    path=
        safe_text,
    textSize=
        safe_text,
    texture=
        safe_text,
    shape=
        safe_text,
    colorRBG=
        safe_text,
    size=
        safe_text
)
gama_EReflex_strategy = st.builds(
    gama_EReflex,
    gamlCode=
        safe_text
)
gama_EParameter_strategy = st.builds(
    gama_EParameter,
    init=
        safe_text,
    category=
        safe_text,
    among=
        safe_text,
    variable=
        safe_text,
    step=
        safe_text,
    min=
        safe_text,
    max=
        safe_text
)
gama_EState_strategy = st.builds(
    gama_EState,
    gamlCode=
        safe_text
)
gama_EChartLayer_strategy = st.builds(
    gama_EChartLayer,
    style=
        safe_text,
    value=
        safe_text,
    color=
        safe_text
)
gama_EEquation_strategy = st.builds(
    gama_EEquation,
    gamlCode=
        safe_text
)
gama_ERule_strategy = st.builds(
    gama_ERule,
    gamlCode=
        safe_text
)
gama_ETask_strategy = st.builds(
    gama_ETask,
    gamlCode=
        safe_text
)
gama_ELayer_strategy = st.builds(
    gama_ELayer,
    text=
        safe_text,
    gamlCode=
        safe_text,
    color=
        safe_text,
    agents=
        safe_text,
    isColorCst=
        safe_text,
    grid=
        safe_text,
    colorRBG=
        safe_text,
    file=
        safe_text,
    species=
        safe_text,
    type=
        safe_text,
    aspect=
        safe_text,
    showLines=
        st.booleans(),
    chart_type=
        safe_text,
    size=
        safe_text
)
gama_EPlan_strategy = st.builds(
    gama_EPlan,
    gamlCode=
        safe_text
)
gama_EPerceive_strategy = st.builds(
    gama_EPerceive,
    gamlCode=
        safe_text
)
gama_ESpecies_strategy = st.builds(
    gama_ESpecies,
    skills=
        safe_text,
    init=
        safe_text,
    reflexList=
        safe_text
)
gama_EFacet_strategy = st.builds(
    gama_EFacet,
    name=
        safe_text,
    value=
        safe_text
)
gama_EGamaLink_strategy = st.builds(
    gama_EGamaLink,
)
gama_EGamaObject_strategy = st.builds(
    gama_EGamaObject,
    colorPicto=
        safe_text,
    hasError=
        safe_text,
    name=
        safe_text,
    error=
        safe_text
)
gama_EGamaModel_strategy = st.builds(
    gama_EGamaModel,
    name=
        safe_text
)
gama_ESubSpeciesLink_strategy = st.builds(
    gama_ESubSpeciesLink,
)
gama_EReflexLink_strategy = st.builds(
    gama_EReflexLink,
)
gama_EActionLink_strategy = st.builds(
    gama_EActionLink,
)
gama_EAspectLink_strategy = st.builds(
    gama_EAspectLink,
)
gama_EExperimentLink_strategy = st.builds(
    gama_EExperimentLink,
)
gama_EVariable_strategy = st.builds(
    gama_EVariable,
    hasError=
        safe_text,
    error=
        safe_text,
    name=
        safe_text,
    init=
        safe_text,
    update=
        safe_text,
    max=
        safe_text,
    function=
        safe_text,
    type=
        safe_text,
    min=
        safe_text
)

@given(instance=EGamaLink_strategy)
@settings(max_examples=50)
def test_egamalink_instantiation(instance):
    assert isinstance(instance, EGamaLink)

@given(instance=EExperiment_strategy)
@settings(max_examples=50)
def test_eexperiment_instantiation(instance):
    assert isinstance(instance, EExperiment)

@given(instance=gama_EBatchExperiment_strategy)
@settings(max_examples=50)
def test_gama_ebatchexperiment_instantiation(instance):
    assert isinstance(instance, gama_EBatchExperiment)

@given(instance=gama_EGUIExperiment_strategy)
@settings(max_examples=50)
def test_gama_eguiexperiment_instantiation(instance):
    assert isinstance(instance, gama_EGUIExperiment)

@given(instance=gama_EDisplayLink_strategy)
@settings(max_examples=50)
def test_gama_edisplaylink_instantiation(instance):
    assert isinstance(instance, gama_EDisplayLink)

@given(instance=ESpecies_strategy)
@settings(max_examples=50)
def test_especies_instantiation(instance):
    assert isinstance(instance, ESpecies)

@given(instance=gama_EWorldAgent_strategy)
@settings(max_examples=50)
def test_gama_eworldagent_instantiation(instance):
    assert isinstance(instance, gama_EWorldAgent)

@given(instance=gama_EGrid_strategy)
@settings(max_examples=50)
def test_gama_egrid_instantiation(instance):
    assert isinstance(instance, gama_EGrid)

@given(instance=gama_EExperiment_strategy)
@settings(max_examples=50)
def test_gama_eexperiment_instantiation(instance):
    assert isinstance(instance, gama_EExperiment)

@given(instance=gama_EEquationLink_strategy)
@settings(max_examples=50)
def test_gama_eequationlink_instantiation(instance):
    assert isinstance(instance, gama_EEquationLink)

@given(instance=gama_ERuleLink_strategy)
@settings(max_examples=50)
def test_gama_erulelink_instantiation(instance):
    assert isinstance(instance, gama_ERuleLink)

@given(instance=gama_EPerceiveLink_strategy)
@settings(max_examples=50)
def test_gama_eperceivelink_instantiation(instance):
    assert isinstance(instance, gama_EPerceiveLink)

@given(instance=gama_ETaskLink_strategy)
@settings(max_examples=50)
def test_gama_etasklink_instantiation(instance):
    assert isinstance(instance, gama_ETaskLink)

@given(instance=gama_EStateLink_strategy)
@settings(max_examples=50)
def test_gama_estatelink_instantiation(instance):
    assert isinstance(instance, gama_EStateLink)

@given(instance=gama_EPlanLink_strategy)
@settings(max_examples=50)
def test_gama_eplanlink_instantiation(instance):
    assert isinstance(instance, gama_EPlanLink)

@given(instance=gama_EInheritLink_strategy)
@settings(max_examples=50)
def test_gama_einheritlink_instantiation(instance):
    assert isinstance(instance, gama_EInheritLink)

@given(instance=EGamaObject_strategy)
@settings(max_examples=50)
def test_egamaobject_instantiation(instance):
    assert isinstance(instance, EGamaObject)

@given(instance=gama_EAspect_strategy)
@settings(max_examples=50)
def test_gama_easpect_instantiation(instance):
    assert isinstance(instance, gama_EAspect)



@given(instance=gama_EAspect_strategy)
def test_gama_easpect_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original



@given(instance=gama_EAspect_strategy)
def test_gama_easpect_defineGamlCode_setter(instance):
    original = instance.defineGamlCode
    instance.defineGamlCode = original
    assert instance.defineGamlCode == original

@given(instance=gama_EDisplay_strategy)
@settings(max_examples=50)
def test_gama_edisplay_instantiation(instance):
    assert isinstance(instance, gama_EDisplay)



@given(instance=gama_EDisplay_strategy)
def test_gama_edisplay_defineGamlCode_setter(instance):
    original = instance.defineGamlCode
    instance.defineGamlCode = original
    assert instance.defineGamlCode == original



@given(instance=gama_EDisplay_strategy)
def test_gama_edisplay_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original



@given(instance=gama_EDisplay_strategy)
def test_gama_edisplay_layerList_setter(instance):
    original = instance.layerList
    instance.layerList = original
    assert instance.layerList == original

@given(instance=gama_EAction_strategy)
@settings(max_examples=50)
def test_gama_eaction_instantiation(instance):
    assert isinstance(instance, gama_EAction)



@given(instance=gama_EAction_strategy)
def test_gama_eaction_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original



@given(instance=gama_EAction_strategy)
def test_gama_eaction_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama_EMonitor_strategy)
@settings(max_examples=50)
def test_gama_emonitor_instantiation(instance):
    assert isinstance(instance, gama_EMonitor)



@given(instance=gama_EMonitor_strategy)
def test_gama_emonitor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gama_ELayerAspect_strategy)
@settings(max_examples=50)
def test_gama_elayeraspect_instantiation(instance):
    assert isinstance(instance, gama_ELayerAspect)



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_imageSize_setter(instance):
    original = instance.imageSize
    instance.imageSize = original
    assert instance.imageSize == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_at_setter(instance):
    original = instance.at
    instance.at = original
    assert instance.at == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_isColorCst_setter(instance):
    original = instance.isColorCst
    instance.isColorCst = original
    assert instance.isColorCst == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_depth_setter(instance):
    original = instance.depth
    instance.depth = original
    assert instance.depth == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_rotate_setter(instance):
    original = instance.rotate
    instance.rotate = original
    assert instance.rotate == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_heigth_setter(instance):
    original = instance.heigth
    instance.heigth = original
    assert instance.heigth == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_radius_setter(instance):
    original = instance.radius
    instance.radius = original
    assert instance.radius == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_empty_setter(instance):
    original = instance.empty
    instance.empty = original
    assert instance.empty == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_shapeType_setter(instance):
    original = instance.shapeType
    instance.shapeType = original
    assert instance.shapeType == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_textSize_setter(instance):
    original = instance.textSize
    instance.textSize = original
    assert instance.textSize == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_texture_setter(instance):
    original = instance.texture
    instance.texture = original
    assert instance.texture == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_colorRBG_setter(instance):
    original = instance.colorRBG
    instance.colorRBG = original
    assert instance.colorRBG == original



@given(instance=gama_ELayerAspect_strategy)
def test_gama_elayeraspect_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=gama_EReflex_strategy)
@settings(max_examples=50)
def test_gama_ereflex_instantiation(instance):
    assert isinstance(instance, gama_EReflex)



@given(instance=gama_EReflex_strategy)
def test_gama_ereflex_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama_EParameter_strategy)
@settings(max_examples=50)
def test_gama_eparameter_instantiation(instance):
    assert isinstance(instance, gama_EParameter)



@given(instance=gama_EParameter_strategy)
def test_gama_eparameter_init_setter(instance):
    original = instance.init
    instance.init = original
    assert instance.init == original



@given(instance=gama_EParameter_strategy)
def test_gama_eparameter_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=gama_EParameter_strategy)
def test_gama_eparameter_among_setter(instance):
    original = instance.among
    instance.among = original
    assert instance.among == original



@given(instance=gama_EParameter_strategy)
def test_gama_eparameter_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original



@given(instance=gama_EParameter_strategy)
def test_gama_eparameter_step_setter(instance):
    original = instance.step
    instance.step = original
    assert instance.step == original



@given(instance=gama_EParameter_strategy)
def test_gama_eparameter_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=gama_EParameter_strategy)
def test_gama_eparameter_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=gama_EState_strategy)
@settings(max_examples=50)
def test_gama_estate_instantiation(instance):
    assert isinstance(instance, gama_EState)



@given(instance=gama_EState_strategy)
def test_gama_estate_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama_EChartLayer_strategy)
@settings(max_examples=50)
def test_gama_echartlayer_instantiation(instance):
    assert isinstance(instance, gama_EChartLayer)



@given(instance=gama_EChartLayer_strategy)
def test_gama_echartlayer_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=gama_EChartLayer_strategy)
def test_gama_echartlayer_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=gama_EChartLayer_strategy)
def test_gama_echartlayer_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=gama_EEquation_strategy)
@settings(max_examples=50)
def test_gama_eequation_instantiation(instance):
    assert isinstance(instance, gama_EEquation)



@given(instance=gama_EEquation_strategy)
def test_gama_eequation_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama_ERule_strategy)
@settings(max_examples=50)
def test_gama_erule_instantiation(instance):
    assert isinstance(instance, gama_ERule)



@given(instance=gama_ERule_strategy)
def test_gama_erule_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama_ETask_strategy)
@settings(max_examples=50)
def test_gama_etask_instantiation(instance):
    assert isinstance(instance, gama_ETask)



@given(instance=gama_ETask_strategy)
def test_gama_etask_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama_ELayer_strategy)
@settings(max_examples=50)
def test_gama_elayer_instantiation(instance):
    assert isinstance(instance, gama_ELayer)



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_agents_setter(instance):
    original = instance.agents
    instance.agents = original
    assert instance.agents == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_isColorCst_setter(instance):
    original = instance.isColorCst
    instance.isColorCst = original
    assert instance.isColorCst == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_grid_setter(instance):
    original = instance.grid
    instance.grid = original
    assert instance.grid == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_colorRBG_setter(instance):
    original = instance.colorRBG
    instance.colorRBG = original
    assert instance.colorRBG == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_species_setter(instance):
    original = instance.species
    instance.species = original
    assert instance.species == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_aspect_setter(instance):
    original = instance.aspect
    instance.aspect = original
    assert instance.aspect == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_showLines_setter(instance):
    original = instance.showLines
    instance.showLines = original
    assert instance.showLines == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_chart_type_setter(instance):
    original = instance.chart_type
    instance.chart_type = original
    assert instance.chart_type == original



@given(instance=gama_ELayer_strategy)
def test_gama_elayer_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=gama_EPlan_strategy)
@settings(max_examples=50)
def test_gama_eplan_instantiation(instance):
    assert isinstance(instance, gama_EPlan)



@given(instance=gama_EPlan_strategy)
def test_gama_eplan_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama_EPerceive_strategy)
@settings(max_examples=50)
def test_gama_eperceive_instantiation(instance):
    assert isinstance(instance, gama_EPerceive)



@given(instance=gama_EPerceive_strategy)
def test_gama_eperceive_gamlCode_setter(instance):
    original = instance.gamlCode
    instance.gamlCode = original
    assert instance.gamlCode == original

@given(instance=gama_ESpecies_strategy)
@settings(max_examples=50)
def test_gama_especies_instantiation(instance):
    assert isinstance(instance, gama_ESpecies)



@given(instance=gama_ESpecies_strategy)
def test_gama_especies_skills_setter(instance):
    original = instance.skills
    instance.skills = original
    assert instance.skills == original



@given(instance=gama_ESpecies_strategy)
def test_gama_especies_init_setter(instance):
    original = instance.init
    instance.init = original
    assert instance.init == original



@given(instance=gama_ESpecies_strategy)
def test_gama_especies_reflexList_setter(instance):
    original = instance.reflexList
    instance.reflexList = original
    assert instance.reflexList == original

@given(instance=gama_EFacet_strategy)
@settings(max_examples=50)
def test_gama_efacet_instantiation(instance):
    assert isinstance(instance, gama_EFacet)



@given(instance=gama_EFacet_strategy)
def test_gama_efacet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=gama_EFacet_strategy)
def test_gama_efacet_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gama_EGamaLink_strategy)
@settings(max_examples=50)
def test_gama_egamalink_instantiation(instance):
    assert isinstance(instance, gama_EGamaLink)

@given(instance=gama_EGamaObject_strategy)
@settings(max_examples=50)
def test_gama_egamaobject_instantiation(instance):
    assert isinstance(instance, gama_EGamaObject)



@given(instance=gama_EGamaObject_strategy)
def test_gama_egamaobject_colorPicto_setter(instance):
    original = instance.colorPicto
    instance.colorPicto = original
    assert instance.colorPicto == original



@given(instance=gama_EGamaObject_strategy)
def test_gama_egamaobject_hasError_setter(instance):
    original = instance.hasError
    instance.hasError = original
    assert instance.hasError == original



@given(instance=gama_EGamaObject_strategy)
def test_gama_egamaobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=gama_EGamaObject_strategy)
def test_gama_egamaobject_error_setter(instance):
    original = instance.error
    instance.error = original
    assert instance.error == original

@given(instance=gama_EGamaModel_strategy)
@settings(max_examples=50)
def test_gama_egamamodel_instantiation(instance):
    assert isinstance(instance, gama_EGamaModel)



@given(instance=gama_EGamaModel_strategy)
def test_gama_egamamodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gama_ESubSpeciesLink_strategy)
@settings(max_examples=50)
def test_gama_esubspecieslink_instantiation(instance):
    assert isinstance(instance, gama_ESubSpeciesLink)

@given(instance=gama_EReflexLink_strategy)
@settings(max_examples=50)
def test_gama_ereflexlink_instantiation(instance):
    assert isinstance(instance, gama_EReflexLink)

@given(instance=gama_EActionLink_strategy)
@settings(max_examples=50)
def test_gama_eactionlink_instantiation(instance):
    assert isinstance(instance, gama_EActionLink)

@given(instance=gama_EAspectLink_strategy)
@settings(max_examples=50)
def test_gama_easpectlink_instantiation(instance):
    assert isinstance(instance, gama_EAspectLink)

@given(instance=gama_EExperimentLink_strategy)
@settings(max_examples=50)
def test_gama_eexperimentlink_instantiation(instance):
    assert isinstance(instance, gama_EExperimentLink)

@given(instance=gama_EVariable_strategy)
@settings(max_examples=50)
def test_gama_evariable_instantiation(instance):
    assert isinstance(instance, gama_EVariable)



@given(instance=gama_EVariable_strategy)
def test_gama_evariable_hasError_setter(instance):
    original = instance.hasError
    instance.hasError = original
    assert instance.hasError == original



@given(instance=gama_EVariable_strategy)
def test_gama_evariable_error_setter(instance):
    original = instance.error
    instance.error = original
    assert instance.error == original



@given(instance=gama_EVariable_strategy)
def test_gama_evariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=gama_EVariable_strategy)
def test_gama_evariable_init_setter(instance):
    original = instance.init
    instance.init = original
    assert instance.init == original



@given(instance=gama_EVariable_strategy)
def test_gama_evariable_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original



@given(instance=gama_EVariable_strategy)
def test_gama_evariable_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=gama_EVariable_strategy)
def test_gama_evariable_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original



@given(instance=gama_EVariable_strategy)
def test_gama_evariable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=gama_EVariable_strategy)
def test_gama_evariable_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original
