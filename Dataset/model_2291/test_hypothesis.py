import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sedml_variable,
    sedml_math,
    sedml_listOfVariables,
    sedml_curve,
    sedml_listOfCurves,
    sedml_algorithm,
    sedml_plot2D,
    sedml_dataGenerator,
    sedml_task,
    sedml_model,
    sedml_listOfOutputs,
    sedml_listOfDataGenerators,
    sedml_listOfTasks,
    sedml_listOfModels,
    sedml_listOfSimulations,
    sedml_sedML,
    sedml_uniformTimeCourse,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sedml_variable_is_not_abstract():
    assert not inspect.isabstract(sedml_variable)


def test_sedml_variable_constructor_exists():
    assert callable(sedml_variable.__init__)


def test_sedml_variable_constructor_args():
    sig = inspect.signature(sedml_variable.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "id" in params, "Missing parameter 'id'"
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_sedml_variable_has_target():
    assert hasattr(sedml_variable, "target")
    descriptor = None
    for klass in sedml_variable.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_sedml_variable_has_id():
    assert hasattr(sedml_variable, "id")
    descriptor = None
    for klass in sedml_variable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sedml_variable_has_symbol():
    assert hasattr(sedml_variable, "symbol")
    descriptor = None
    for klass in sedml_variable.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_sedml_math_is_not_abstract():
    assert not inspect.isabstract(sedml_math)


def test_sedml_math_constructor_exists():
    assert callable(sedml_math.__init__)


def test_sedml_math_constructor_args():
    sig = inspect.signature(sedml_math.__init__)
    params = list(sig.parameters.keys())
    assert "xlms" in params, "Missing parameter 'xlms'"

def test_sedml_math_has_xlms():
    assert hasattr(sedml_math, "xlms")
    descriptor = None
    for klass in sedml_math.__mro__:
        if "xlms" in klass.__dict__:
            descriptor = klass.__dict__["xlms"]
            break
    assert isinstance(descriptor, property)



def test_sedml_listofvariables_is_not_abstract():
    assert not inspect.isabstract(sedml_listOfVariables)


def test_sedml_listofvariables_constructor_exists():
    assert callable(sedml_listOfVariables.__init__)


def test_sedml_listofvariables_constructor_args():
    sig = inspect.signature(sedml_listOfVariables.__init__)
    params = list(sig.parameters.keys())



def test_sedml_curve_is_not_abstract():
    assert not inspect.isabstract(sedml_curve)


def test_sedml_curve_constructor_exists():
    assert callable(sedml_curve.__init__)


def test_sedml_curve_constructor_args():
    sig = inspect.signature(sedml_curve.__init__)
    params = list(sig.parameters.keys())
    assert "logX" in params, "Missing parameter 'logX'"
    assert "logY" in params, "Missing parameter 'logY'"
    assert "id" in params, "Missing parameter 'id'"
    assert "xDataReference" in params, "Missing parameter 'xDataReference'"
    assert "yDataReference" in params, "Missing parameter 'yDataReference'"

def test_sedml_curve_has_logX():
    assert hasattr(sedml_curve, "logX")
    descriptor = None
    for klass in sedml_curve.__mro__:
        if "logX" in klass.__dict__:
            descriptor = klass.__dict__["logX"]
            break
    assert isinstance(descriptor, property)

def test_sedml_curve_has_logY():
    assert hasattr(sedml_curve, "logY")
    descriptor = None
    for klass in sedml_curve.__mro__:
        if "logY" in klass.__dict__:
            descriptor = klass.__dict__["logY"]
            break
    assert isinstance(descriptor, property)

def test_sedml_curve_has_id():
    assert hasattr(sedml_curve, "id")
    descriptor = None
    for klass in sedml_curve.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sedml_curve_has_xDataReference():
    assert hasattr(sedml_curve, "xDataReference")
    descriptor = None
    for klass in sedml_curve.__mro__:
        if "xDataReference" in klass.__dict__:
            descriptor = klass.__dict__["xDataReference"]
            break
    assert isinstance(descriptor, property)

def test_sedml_curve_has_yDataReference():
    assert hasattr(sedml_curve, "yDataReference")
    descriptor = None
    for klass in sedml_curve.__mro__:
        if "yDataReference" in klass.__dict__:
            descriptor = klass.__dict__["yDataReference"]
            break
    assert isinstance(descriptor, property)



def test_sedml_listofcurves_is_not_abstract():
    assert not inspect.isabstract(sedml_listOfCurves)


def test_sedml_listofcurves_constructor_exists():
    assert callable(sedml_listOfCurves.__init__)


def test_sedml_listofcurves_constructor_args():
    sig = inspect.signature(sedml_listOfCurves.__init__)
    params = list(sig.parameters.keys())



def test_sedml_algorithm_is_not_abstract():
    assert not inspect.isabstract(sedml_algorithm)


def test_sedml_algorithm_constructor_exists():
    assert callable(sedml_algorithm.__init__)


def test_sedml_algorithm_constructor_args():
    sig = inspect.signature(sedml_algorithm.__init__)
    params = list(sig.parameters.keys())
    assert "kisaoID" in params, "Missing parameter 'kisaoID'"

def test_sedml_algorithm_has_kisaoID():
    assert hasattr(sedml_algorithm, "kisaoID")
    descriptor = None
    for klass in sedml_algorithm.__mro__:
        if "kisaoID" in klass.__dict__:
            descriptor = klass.__dict__["kisaoID"]
            break
    assert isinstance(descriptor, property)



def test_sedml_plot2d_is_not_abstract():
    assert not inspect.isabstract(sedml_plot2D)


def test_sedml_plot2d_constructor_exists():
    assert callable(sedml_plot2D.__init__)


def test_sedml_plot2d_constructor_args():
    sig = inspect.signature(sedml_plot2D.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_sedml_plot2d_has_name():
    assert hasattr(sedml_plot2D, "name")
    descriptor = None
    for klass in sedml_plot2D.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sedml_plot2d_has_id():
    assert hasattr(sedml_plot2D, "id")
    descriptor = None
    for klass in sedml_plot2D.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sedml_datagenerator_is_not_abstract():
    assert not inspect.isabstract(sedml_dataGenerator)


def test_sedml_datagenerator_constructor_exists():
    assert callable(sedml_dataGenerator.__init__)


def test_sedml_datagenerator_constructor_args():
    sig = inspect.signature(sedml_dataGenerator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_sedml_datagenerator_has_name():
    assert hasattr(sedml_dataGenerator, "name")
    descriptor = None
    for klass in sedml_dataGenerator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sedml_datagenerator_has_id():
    assert hasattr(sedml_dataGenerator, "id")
    descriptor = None
    for klass in sedml_dataGenerator.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sedml_task_is_not_abstract():
    assert not inspect.isabstract(sedml_task)


def test_sedml_task_constructor_exists():
    assert callable(sedml_task.__init__)


def test_sedml_task_constructor_args():
    sig = inspect.signature(sedml_task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_sedml_task_has_name():
    assert hasattr(sedml_task, "name")
    descriptor = None
    for klass in sedml_task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sedml_task_has_id():
    assert hasattr(sedml_task, "id")
    descriptor = None
    for klass in sedml_task.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sedml_model_is_not_abstract():
    assert not inspect.isabstract(sedml_model)


def test_sedml_model_constructor_exists():
    assert callable(sedml_model.__init__)


def test_sedml_model_constructor_args():
    sig = inspect.signature(sedml_model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "source" in params, "Missing parameter 'source'"
    assert "language" in params, "Missing parameter 'language'"

def test_sedml_model_has_name():
    assert hasattr(sedml_model, "name")
    descriptor = None
    for klass in sedml_model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sedml_model_has_id():
    assert hasattr(sedml_model, "id")
    descriptor = None
    for klass in sedml_model.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sedml_model_has_source():
    assert hasattr(sedml_model, "source")
    descriptor = None
    for klass in sedml_model.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_sedml_model_has_language():
    assert hasattr(sedml_model, "language")
    descriptor = None
    for klass in sedml_model.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_sedml_listofoutputs_is_not_abstract():
    assert not inspect.isabstract(sedml_listOfOutputs)


def test_sedml_listofoutputs_constructor_exists():
    assert callable(sedml_listOfOutputs.__init__)


def test_sedml_listofoutputs_constructor_args():
    sig = inspect.signature(sedml_listOfOutputs.__init__)
    params = list(sig.parameters.keys())



def test_sedml_listofdatagenerators_is_not_abstract():
    assert not inspect.isabstract(sedml_listOfDataGenerators)


def test_sedml_listofdatagenerators_constructor_exists():
    assert callable(sedml_listOfDataGenerators.__init__)


def test_sedml_listofdatagenerators_constructor_args():
    sig = inspect.signature(sedml_listOfDataGenerators.__init__)
    params = list(sig.parameters.keys())



def test_sedml_listoftasks_is_not_abstract():
    assert not inspect.isabstract(sedml_listOfTasks)


def test_sedml_listoftasks_constructor_exists():
    assert callable(sedml_listOfTasks.__init__)


def test_sedml_listoftasks_constructor_args():
    sig = inspect.signature(sedml_listOfTasks.__init__)
    params = list(sig.parameters.keys())



def test_sedml_listofmodels_is_not_abstract():
    assert not inspect.isabstract(sedml_listOfModels)


def test_sedml_listofmodels_constructor_exists():
    assert callable(sedml_listOfModels.__init__)


def test_sedml_listofmodels_constructor_args():
    sig = inspect.signature(sedml_listOfModels.__init__)
    params = list(sig.parameters.keys())



def test_sedml_listofsimulations_is_not_abstract():
    assert not inspect.isabstract(sedml_listOfSimulations)


def test_sedml_listofsimulations_constructor_exists():
    assert callable(sedml_listOfSimulations.__init__)


def test_sedml_listofsimulations_constructor_args():
    sig = inspect.signature(sedml_listOfSimulations.__init__)
    params = list(sig.parameters.keys())



def test_sedml_sedml_is_not_abstract():
    assert not inspect.isabstract(sedml_sedML)


def test_sedml_sedml_constructor_exists():
    assert callable(sedml_sedML.__init__)


def test_sedml_sedml_constructor_args():
    sig = inspect.signature(sedml_sedML.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "version" in params, "Missing parameter 'version'"

def test_sedml_sedml_has_level():
    assert hasattr(sedml_sedML, "level")
    descriptor = None
    for klass in sedml_sedML.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_sedml_sedml_has_version():
    assert hasattr(sedml_sedML, "version")
    descriptor = None
    for klass in sedml_sedML.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_sedml_uniformtimecourse_is_not_abstract():
    assert not inspect.isabstract(sedml_uniformTimeCourse)


def test_sedml_uniformtimecourse_constructor_exists():
    assert callable(sedml_uniformTimeCourse.__init__)


def test_sedml_uniformtimecourse_constructor_args():
    sig = inspect.signature(sedml_uniformTimeCourse.__init__)
    params = list(sig.parameters.keys())
    assert "initialTime" in params, "Missing parameter 'initialTime'"
    assert "numberOfPoints" in params, "Missing parameter 'numberOfPoints'"
    assert "outputStartTime" in params, "Missing parameter 'outputStartTime'"
    assert "id" in params, "Missing parameter 'id'"
    assert "outputEndTime" in params, "Missing parameter 'outputEndTime'"

def test_sedml_uniformtimecourse_has_initialTime():
    assert hasattr(sedml_uniformTimeCourse, "initialTime")
    descriptor = None
    for klass in sedml_uniformTimeCourse.__mro__:
        if "initialTime" in klass.__dict__:
            descriptor = klass.__dict__["initialTime"]
            break
    assert isinstance(descriptor, property)

def test_sedml_uniformtimecourse_has_numberOfPoints():
    assert hasattr(sedml_uniformTimeCourse, "numberOfPoints")
    descriptor = None
    for klass in sedml_uniformTimeCourse.__mro__:
        if "numberOfPoints" in klass.__dict__:
            descriptor = klass.__dict__["numberOfPoints"]
            break
    assert isinstance(descriptor, property)

def test_sedml_uniformtimecourse_has_outputStartTime():
    assert hasattr(sedml_uniformTimeCourse, "outputStartTime")
    descriptor = None
    for klass in sedml_uniformTimeCourse.__mro__:
        if "outputStartTime" in klass.__dict__:
            descriptor = klass.__dict__["outputStartTime"]
            break
    assert isinstance(descriptor, property)

def test_sedml_uniformtimecourse_has_id():
    assert hasattr(sedml_uniformTimeCourse, "id")
    descriptor = None
    for klass in sedml_uniformTimeCourse.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sedml_uniformtimecourse_has_outputEndTime():
    assert hasattr(sedml_uniformTimeCourse, "outputEndTime")
    descriptor = None
    for klass in sedml_uniformTimeCourse.__mro__:
        if "outputEndTime" in klass.__dict__:
            descriptor = klass.__dict__["outputEndTime"]
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
sedml_variable_strategy = st.builds(
    sedml_variable,
    target=
        safe_text,
    id=
        safe_text,
    symbol=
        safe_text
)
sedml_math_strategy = st.builds(
    sedml_math,
    xlms=
        safe_text
)
sedml_listOfVariables_strategy = st.builds(
    sedml_listOfVariables,
)
sedml_curve_strategy = st.builds(
    sedml_curve,
    logX=
        safe_text,
    logY=
        safe_text,
    id=
        safe_text,
    xDataReference=
        safe_text,
    yDataReference=
        safe_text
)
sedml_listOfCurves_strategy = st.builds(
    sedml_listOfCurves,
)
sedml_algorithm_strategy = st.builds(
    sedml_algorithm,
    kisaoID=
        safe_text
)
sedml_plot2D_strategy = st.builds(
    sedml_plot2D,
    name=
        safe_text,
    id=
        safe_text
)
sedml_dataGenerator_strategy = st.builds(
    sedml_dataGenerator,
    name=
        safe_text,
    id=
        safe_text
)
sedml_task_strategy = st.builds(
    sedml_task,
    name=
        safe_text,
    id=
        safe_text
)
sedml_model_strategy = st.builds(
    sedml_model,
    name=
        safe_text,
    id=
        safe_text,
    source=
        safe_text,
    language=
        safe_text
)
sedml_listOfOutputs_strategy = st.builds(
    sedml_listOfOutputs,
)
sedml_listOfDataGenerators_strategy = st.builds(
    sedml_listOfDataGenerators,
)
sedml_listOfTasks_strategy = st.builds(
    sedml_listOfTasks,
)
sedml_listOfModels_strategy = st.builds(
    sedml_listOfModels,
)
sedml_listOfSimulations_strategy = st.builds(
    sedml_listOfSimulations,
)
sedml_sedML_strategy = st.builds(
    sedml_sedML,
    level=
        st.integers(),
    version=
        st.integers()
)
sedml_uniformTimeCourse_strategy = st.builds(
    sedml_uniformTimeCourse,
    initialTime=
        st.integers(),
    numberOfPoints=
        st.integers(),
    outputStartTime=
        st.integers(),
    id=
        safe_text,
    outputEndTime=
        st.integers()
)

@given(instance=sedml_variable_strategy)
@settings(max_examples=50)
def test_sedml_variable_instantiation(instance):
    assert isinstance(instance, sedml_variable)



@given(instance=sedml_variable_strategy)
def test_sedml_variable_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=sedml_variable_strategy)
def test_sedml_variable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=sedml_variable_strategy)
def test_sedml_variable_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=sedml_math_strategy)
@settings(max_examples=50)
def test_sedml_math_instantiation(instance):
    assert isinstance(instance, sedml_math)



@given(instance=sedml_math_strategy)
def test_sedml_math_xlms_setter(instance):
    original = instance.xlms
    instance.xlms = original
    assert instance.xlms == original

@given(instance=sedml_listOfVariables_strategy)
@settings(max_examples=50)
def test_sedml_listofvariables_instantiation(instance):
    assert isinstance(instance, sedml_listOfVariables)

@given(instance=sedml_curve_strategy)
@settings(max_examples=50)
def test_sedml_curve_instantiation(instance):
    assert isinstance(instance, sedml_curve)



@given(instance=sedml_curve_strategy)
def test_sedml_curve_logX_setter(instance):
    original = instance.logX
    instance.logX = original
    assert instance.logX == original



@given(instance=sedml_curve_strategy)
def test_sedml_curve_logY_setter(instance):
    original = instance.logY
    instance.logY = original
    assert instance.logY == original



@given(instance=sedml_curve_strategy)
def test_sedml_curve_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=sedml_curve_strategy)
def test_sedml_curve_xDataReference_setter(instance):
    original = instance.xDataReference
    instance.xDataReference = original
    assert instance.xDataReference == original



@given(instance=sedml_curve_strategy)
def test_sedml_curve_yDataReference_setter(instance):
    original = instance.yDataReference
    instance.yDataReference = original
    assert instance.yDataReference == original

@given(instance=sedml_listOfCurves_strategy)
@settings(max_examples=50)
def test_sedml_listofcurves_instantiation(instance):
    assert isinstance(instance, sedml_listOfCurves)

@given(instance=sedml_algorithm_strategy)
@settings(max_examples=50)
def test_sedml_algorithm_instantiation(instance):
    assert isinstance(instance, sedml_algorithm)



@given(instance=sedml_algorithm_strategy)
def test_sedml_algorithm_kisaoID_setter(instance):
    original = instance.kisaoID
    instance.kisaoID = original
    assert instance.kisaoID == original

@given(instance=sedml_plot2D_strategy)
@settings(max_examples=50)
def test_sedml_plot2d_instantiation(instance):
    assert isinstance(instance, sedml_plot2D)



@given(instance=sedml_plot2D_strategy)
def test_sedml_plot2d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sedml_plot2D_strategy)
def test_sedml_plot2d_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sedml_dataGenerator_strategy)
@settings(max_examples=50)
def test_sedml_datagenerator_instantiation(instance):
    assert isinstance(instance, sedml_dataGenerator)



@given(instance=sedml_dataGenerator_strategy)
def test_sedml_datagenerator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sedml_dataGenerator_strategy)
def test_sedml_datagenerator_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sedml_task_strategy)
@settings(max_examples=50)
def test_sedml_task_instantiation(instance):
    assert isinstance(instance, sedml_task)



@given(instance=sedml_task_strategy)
def test_sedml_task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sedml_task_strategy)
def test_sedml_task_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sedml_model_strategy)
@settings(max_examples=50)
def test_sedml_model_instantiation(instance):
    assert isinstance(instance, sedml_model)



@given(instance=sedml_model_strategy)
def test_sedml_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sedml_model_strategy)
def test_sedml_model_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=sedml_model_strategy)
def test_sedml_model_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=sedml_model_strategy)
def test_sedml_model_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=sedml_listOfOutputs_strategy)
@settings(max_examples=50)
def test_sedml_listofoutputs_instantiation(instance):
    assert isinstance(instance, sedml_listOfOutputs)

@given(instance=sedml_listOfDataGenerators_strategy)
@settings(max_examples=50)
def test_sedml_listofdatagenerators_instantiation(instance):
    assert isinstance(instance, sedml_listOfDataGenerators)

@given(instance=sedml_listOfTasks_strategy)
@settings(max_examples=50)
def test_sedml_listoftasks_instantiation(instance):
    assert isinstance(instance, sedml_listOfTasks)

@given(instance=sedml_listOfModels_strategy)
@settings(max_examples=50)
def test_sedml_listofmodels_instantiation(instance):
    assert isinstance(instance, sedml_listOfModels)

@given(instance=sedml_listOfSimulations_strategy)
@settings(max_examples=50)
def test_sedml_listofsimulations_instantiation(instance):
    assert isinstance(instance, sedml_listOfSimulations)

@given(instance=sedml_sedML_strategy)
@settings(max_examples=50)
def test_sedml_sedml_instantiation(instance):
    assert isinstance(instance, sedml_sedML)



@given(instance=sedml_sedML_strategy)
def test_sedml_sedml_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=sedml_sedML_strategy)
def test_sedml_sedml_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=sedml_uniformTimeCourse_strategy)
@settings(max_examples=50)
def test_sedml_uniformtimecourse_instantiation(instance):
    assert isinstance(instance, sedml_uniformTimeCourse)



@given(instance=sedml_uniformTimeCourse_strategy)
def test_sedml_uniformtimecourse_initialTime_setter(instance):
    original = instance.initialTime
    instance.initialTime = original
    assert instance.initialTime == original



@given(instance=sedml_uniformTimeCourse_strategy)
def test_sedml_uniformtimecourse_numberOfPoints_setter(instance):
    original = instance.numberOfPoints
    instance.numberOfPoints = original
    assert instance.numberOfPoints == original



@given(instance=sedml_uniformTimeCourse_strategy)
def test_sedml_uniformtimecourse_outputStartTime_setter(instance):
    original = instance.outputStartTime
    instance.outputStartTime = original
    assert instance.outputStartTime == original



@given(instance=sedml_uniformTimeCourse_strategy)
def test_sedml_uniformtimecourse_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=sedml_uniformTimeCourse_strategy)
def test_sedml_uniformtimecourse_outputEndTime_setter(instance):
    original = instance.outputEndTime
    instance.outputEndTime = original
    assert instance.outputEndTime == original
