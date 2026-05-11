import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sedml::variable,
    sedml::math,
    sedml::listOfVariables,
    sedml::curve,
    sedml::listOfCurves,
    sedml::algorithm,
    sedml::plot2D,
    sedml::dataGenerator,
    sedml::task,
    sedml::model,
    sedml::listOfOutputs,
    sedml::listOfDataGenerators,
    sedml::listOfTasks,
    sedml::listOfModels,
    sedml::listOfSimulations,
    sedml::sedML,
    sedml::uniformTimeCourse,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sedml::variable_is_not_abstract():
    assert not inspect.isabstract(sedml::variable)


def test_sedml::variable_constructor_exists():
    assert callable(sedml::variable.__init__)


def test_sedml::variable_constructor_args():
    sig = inspect.signature(sedml::variable.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "id" in params, "Missing parameter 'id'"

def test_sedml::variable_has_target():
    assert hasattr(sedml::variable, "target")
    descriptor = None
    for klass in sedml::variable.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_sedml::variable_has_symbol():
    assert hasattr(sedml::variable, "symbol")
    descriptor = None
    for klass in sedml::variable.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_sedml::variable_has_id():
    assert hasattr(sedml::variable, "id")
    descriptor = None
    for klass in sedml::variable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sedml::math_is_not_abstract():
    assert not inspect.isabstract(sedml::math)


def test_sedml::math_constructor_exists():
    assert callable(sedml::math.__init__)


def test_sedml::math_constructor_args():
    sig = inspect.signature(sedml::math.__init__)
    params = list(sig.parameters.keys())
    assert "xlms" in params, "Missing parameter 'xlms'"

def test_sedml::math_has_xlms():
    assert hasattr(sedml::math, "xlms")
    descriptor = None
    for klass in sedml::math.__mro__:
        if "xlms" in klass.__dict__:
            descriptor = klass.__dict__["xlms"]
            break
    assert isinstance(descriptor, property)



def test_sedml::listofvariables_is_not_abstract():
    assert not inspect.isabstract(sedml::listOfVariables)


def test_sedml::listofvariables_constructor_exists():
    assert callable(sedml::listOfVariables.__init__)


def test_sedml::listofvariables_constructor_args():
    sig = inspect.signature(sedml::listOfVariables.__init__)
    params = list(sig.parameters.keys())



def test_sedml::curve_is_not_abstract():
    assert not inspect.isabstract(sedml::curve)


def test_sedml::curve_constructor_exists():
    assert callable(sedml::curve.__init__)


def test_sedml::curve_constructor_args():
    sig = inspect.signature(sedml::curve.__init__)
    params = list(sig.parameters.keys())
    assert "logY" in params, "Missing parameter 'logY'"
    assert "logX" in params, "Missing parameter 'logX'"
    assert "id" in params, "Missing parameter 'id'"
    assert "yDataReference" in params, "Missing parameter 'yDataReference'"
    assert "xDataReference" in params, "Missing parameter 'xDataReference'"

def test_sedml::curve_has_logY():
    assert hasattr(sedml::curve, "logY")
    descriptor = None
    for klass in sedml::curve.__mro__:
        if "logY" in klass.__dict__:
            descriptor = klass.__dict__["logY"]
            break
    assert isinstance(descriptor, property)

def test_sedml::curve_has_logX():
    assert hasattr(sedml::curve, "logX")
    descriptor = None
    for klass in sedml::curve.__mro__:
        if "logX" in klass.__dict__:
            descriptor = klass.__dict__["logX"]
            break
    assert isinstance(descriptor, property)

def test_sedml::curve_has_id():
    assert hasattr(sedml::curve, "id")
    descriptor = None
    for klass in sedml::curve.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sedml::curve_has_yDataReference():
    assert hasattr(sedml::curve, "yDataReference")
    descriptor = None
    for klass in sedml::curve.__mro__:
        if "yDataReference" in klass.__dict__:
            descriptor = klass.__dict__["yDataReference"]
            break
    assert isinstance(descriptor, property)

def test_sedml::curve_has_xDataReference():
    assert hasattr(sedml::curve, "xDataReference")
    descriptor = None
    for klass in sedml::curve.__mro__:
        if "xDataReference" in klass.__dict__:
            descriptor = klass.__dict__["xDataReference"]
            break
    assert isinstance(descriptor, property)



def test_sedml::listofcurves_is_not_abstract():
    assert not inspect.isabstract(sedml::listOfCurves)


def test_sedml::listofcurves_constructor_exists():
    assert callable(sedml::listOfCurves.__init__)


def test_sedml::listofcurves_constructor_args():
    sig = inspect.signature(sedml::listOfCurves.__init__)
    params = list(sig.parameters.keys())



def test_sedml::algorithm_is_not_abstract():
    assert not inspect.isabstract(sedml::algorithm)


def test_sedml::algorithm_constructor_exists():
    assert callable(sedml::algorithm.__init__)


def test_sedml::algorithm_constructor_args():
    sig = inspect.signature(sedml::algorithm.__init__)
    params = list(sig.parameters.keys())
    assert "kisaoID" in params, "Missing parameter 'kisaoID'"

def test_sedml::algorithm_has_kisaoID():
    assert hasattr(sedml::algorithm, "kisaoID")
    descriptor = None
    for klass in sedml::algorithm.__mro__:
        if "kisaoID" in klass.__dict__:
            descriptor = klass.__dict__["kisaoID"]
            break
    assert isinstance(descriptor, property)



def test_sedml::plot2d_is_not_abstract():
    assert not inspect.isabstract(sedml::plot2D)


def test_sedml::plot2d_constructor_exists():
    assert callable(sedml::plot2D.__init__)


def test_sedml::plot2d_constructor_args():
    sig = inspect.signature(sedml::plot2D.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_sedml::plot2d_has_name():
    assert hasattr(sedml::plot2D, "name")
    descriptor = None
    for klass in sedml::plot2D.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sedml::plot2d_has_id():
    assert hasattr(sedml::plot2D, "id")
    descriptor = None
    for klass in sedml::plot2D.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sedml::datagenerator_is_not_abstract():
    assert not inspect.isabstract(sedml::dataGenerator)


def test_sedml::datagenerator_constructor_exists():
    assert callable(sedml::dataGenerator.__init__)


def test_sedml::datagenerator_constructor_args():
    sig = inspect.signature(sedml::dataGenerator.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_sedml::datagenerator_has_id():
    assert hasattr(sedml::dataGenerator, "id")
    descriptor = None
    for klass in sedml::dataGenerator.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sedml::datagenerator_has_name():
    assert hasattr(sedml::dataGenerator, "name")
    descriptor = None
    for klass in sedml::dataGenerator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sedml::task_is_not_abstract():
    assert not inspect.isabstract(sedml::task)


def test_sedml::task_constructor_exists():
    assert callable(sedml::task.__init__)


def test_sedml::task_constructor_args():
    sig = inspect.signature(sedml::task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_sedml::task_has_name():
    assert hasattr(sedml::task, "name")
    descriptor = None
    for klass in sedml::task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sedml::task_has_id():
    assert hasattr(sedml::task, "id")
    descriptor = None
    for klass in sedml::task.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sedml::model_is_not_abstract():
    assert not inspect.isabstract(sedml::model)


def test_sedml::model_constructor_exists():
    assert callable(sedml::model.__init__)


def test_sedml::model_constructor_args():
    sig = inspect.signature(sedml::model.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "name" in params, "Missing parameter 'name'"
    assert "language" in params, "Missing parameter 'language'"
    assert "id" in params, "Missing parameter 'id'"

def test_sedml::model_has_source():
    assert hasattr(sedml::model, "source")
    descriptor = None
    for klass in sedml::model.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_sedml::model_has_name():
    assert hasattr(sedml::model, "name")
    descriptor = None
    for klass in sedml::model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sedml::model_has_language():
    assert hasattr(sedml::model, "language")
    descriptor = None
    for klass in sedml::model.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_sedml::model_has_id():
    assert hasattr(sedml::model, "id")
    descriptor = None
    for klass in sedml::model.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sedml::listofoutputs_is_not_abstract():
    assert not inspect.isabstract(sedml::listOfOutputs)


def test_sedml::listofoutputs_constructor_exists():
    assert callable(sedml::listOfOutputs.__init__)


def test_sedml::listofoutputs_constructor_args():
    sig = inspect.signature(sedml::listOfOutputs.__init__)
    params = list(sig.parameters.keys())



def test_sedml::listofdatagenerators_is_not_abstract():
    assert not inspect.isabstract(sedml::listOfDataGenerators)


def test_sedml::listofdatagenerators_constructor_exists():
    assert callable(sedml::listOfDataGenerators.__init__)


def test_sedml::listofdatagenerators_constructor_args():
    sig = inspect.signature(sedml::listOfDataGenerators.__init__)
    params = list(sig.parameters.keys())



def test_sedml::listoftasks_is_not_abstract():
    assert not inspect.isabstract(sedml::listOfTasks)


def test_sedml::listoftasks_constructor_exists():
    assert callable(sedml::listOfTasks.__init__)


def test_sedml::listoftasks_constructor_args():
    sig = inspect.signature(sedml::listOfTasks.__init__)
    params = list(sig.parameters.keys())



def test_sedml::listofmodels_is_not_abstract():
    assert not inspect.isabstract(sedml::listOfModels)


def test_sedml::listofmodels_constructor_exists():
    assert callable(sedml::listOfModels.__init__)


def test_sedml::listofmodels_constructor_args():
    sig = inspect.signature(sedml::listOfModels.__init__)
    params = list(sig.parameters.keys())



def test_sedml::listofsimulations_is_not_abstract():
    assert not inspect.isabstract(sedml::listOfSimulations)


def test_sedml::listofsimulations_constructor_exists():
    assert callable(sedml::listOfSimulations.__init__)


def test_sedml::listofsimulations_constructor_args():
    sig = inspect.signature(sedml::listOfSimulations.__init__)
    params = list(sig.parameters.keys())



def test_sedml::sedml_is_not_abstract():
    assert not inspect.isabstract(sedml::sedML)


def test_sedml::sedml_constructor_exists():
    assert callable(sedml::sedML.__init__)


def test_sedml::sedml_constructor_args():
    sig = inspect.signature(sedml::sedML.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "level" in params, "Missing parameter 'level'"

def test_sedml::sedml_has_version():
    assert hasattr(sedml::sedML, "version")
    descriptor = None
    for klass in sedml::sedML.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_sedml::sedml_has_level():
    assert hasattr(sedml::sedML, "level")
    descriptor = None
    for klass in sedml::sedML.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_sedml::uniformtimecourse_is_not_abstract():
    assert not inspect.isabstract(sedml::uniformTimeCourse)


def test_sedml::uniformtimecourse_constructor_exists():
    assert callable(sedml::uniformTimeCourse.__init__)


def test_sedml::uniformtimecourse_constructor_args():
    sig = inspect.signature(sedml::uniformTimeCourse.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "outputEndTime" in params, "Missing parameter 'outputEndTime'"
    assert "outputStartTime" in params, "Missing parameter 'outputStartTime'"
    assert "initialTime" in params, "Missing parameter 'initialTime'"
    assert "numberOfPoints" in params, "Missing parameter 'numberOfPoints'"

def test_sedml::uniformtimecourse_has_id():
    assert hasattr(sedml::uniformTimeCourse, "id")
    descriptor = None
    for klass in sedml::uniformTimeCourse.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sedml::uniformtimecourse_has_outputEndTime():
    assert hasattr(sedml::uniformTimeCourse, "outputEndTime")
    descriptor = None
    for klass in sedml::uniformTimeCourse.__mro__:
        if "outputEndTime" in klass.__dict__:
            descriptor = klass.__dict__["outputEndTime"]
            break
    assert isinstance(descriptor, property)

def test_sedml::uniformtimecourse_has_outputStartTime():
    assert hasattr(sedml::uniformTimeCourse, "outputStartTime")
    descriptor = None
    for klass in sedml::uniformTimeCourse.__mro__:
        if "outputStartTime" in klass.__dict__:
            descriptor = klass.__dict__["outputStartTime"]
            break
    assert isinstance(descriptor, property)

def test_sedml::uniformtimecourse_has_initialTime():
    assert hasattr(sedml::uniformTimeCourse, "initialTime")
    descriptor = None
    for klass in sedml::uniformTimeCourse.__mro__:
        if "initialTime" in klass.__dict__:
            descriptor = klass.__dict__["initialTime"]
            break
    assert isinstance(descriptor, property)

def test_sedml::uniformtimecourse_has_numberOfPoints():
    assert hasattr(sedml::uniformTimeCourse, "numberOfPoints")
    descriptor = None
    for klass in sedml::uniformTimeCourse.__mro__:
        if "numberOfPoints" in klass.__dict__:
            descriptor = klass.__dict__["numberOfPoints"]
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
sedml::variable_strategy = st.builds(
    sedml::variable,
    target=
        safe_text,
    symbol=
        safe_text,
    id=
        safe_text
)
sedml::math_strategy = st.builds(
    sedml::math,
    xlms=
        safe_text
)
sedml::listOfVariables_strategy = st.builds(
    sedml::listOfVariables,
)
sedml::curve_strategy = st.builds(
    sedml::curve,
    logY=
        safe_text,
    logX=
        safe_text,
    id=
        safe_text,
    yDataReference=
        safe_text,
    xDataReference=
        safe_text
)
sedml::listOfCurves_strategy = st.builds(
    sedml::listOfCurves,
)
sedml::algorithm_strategy = st.builds(
    sedml::algorithm,
    kisaoID=
        safe_text
)
sedml::plot2D_strategy = st.builds(
    sedml::plot2D,
    name=
        safe_text,
    id=
        safe_text
)
sedml::dataGenerator_strategy = st.builds(
    sedml::dataGenerator,
    id=
        safe_text,
    name=
        safe_text
)
sedml::task_strategy = st.builds(
    sedml::task,
    name=
        safe_text,
    id=
        safe_text
)
sedml::model_strategy = st.builds(
    sedml::model,
    source=
        safe_text,
    name=
        safe_text,
    language=
        safe_text,
    id=
        safe_text
)
sedml::listOfOutputs_strategy = st.builds(
    sedml::listOfOutputs,
)
sedml::listOfDataGenerators_strategy = st.builds(
    sedml::listOfDataGenerators,
)
sedml::listOfTasks_strategy = st.builds(
    sedml::listOfTasks,
)
sedml::listOfModels_strategy = st.builds(
    sedml::listOfModels,
)
sedml::listOfSimulations_strategy = st.builds(
    sedml::listOfSimulations,
)
sedml::sedML_strategy = st.builds(
    sedml::sedML,
    version=
        st.integers(),
    level=
        st.integers()
)
sedml::uniformTimeCourse_strategy = st.builds(
    sedml::uniformTimeCourse,
    id=
        safe_text,
    outputEndTime=
        st.integers(),
    outputStartTime=
        st.integers(),
    initialTime=
        st.integers(),
    numberOfPoints=
        st.integers()
)

@given(instance=sedml::variable_strategy)
@settings(max_examples=50)
def test_sedml::variable_instantiation(instance):
    assert isinstance(instance, sedml::variable)

@given(instance=sedml::variable_strategy)
def test_sedml::variable_target_type(instance):
    assert isinstance(instance.target, str)


@given(instance=sedml::variable_strategy)
def test_sedml::variable_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=sedml::variable_strategy)
def test_sedml::variable_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=sedml::variable_strategy)
def test_sedml::variable_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=sedml::variable_strategy)
def test_sedml::variable_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sedml::variable_strategy)
def test_sedml::variable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sedml::math_strategy)
@settings(max_examples=50)
def test_sedml::math_instantiation(instance):
    assert isinstance(instance, sedml::math)

@given(instance=sedml::math_strategy)
def test_sedml::math_xlms_type(instance):
    assert isinstance(instance.xlms, str)


@given(instance=sedml::math_strategy)
def test_sedml::math_xlms_setter(instance):
    original = instance.xlms
    instance.xlms = original
    assert instance.xlms == original

@given(instance=sedml::listOfVariables_strategy)
@settings(max_examples=50)
def test_sedml::listofvariables_instantiation(instance):
    assert isinstance(instance, sedml::listOfVariables)

@given(instance=sedml::curve_strategy)
@settings(max_examples=50)
def test_sedml::curve_instantiation(instance):
    assert isinstance(instance, sedml::curve)

@given(instance=sedml::curve_strategy)
def test_sedml::curve_logY_type(instance):
    assert isinstance(instance.logY, str)


@given(instance=sedml::curve_strategy)
def test_sedml::curve_logY_setter(instance):
    original = instance.logY
    instance.logY = original
    assert instance.logY == original

@given(instance=sedml::curve_strategy)
def test_sedml::curve_logX_type(instance):
    assert isinstance(instance.logX, str)


@given(instance=sedml::curve_strategy)
def test_sedml::curve_logX_setter(instance):
    original = instance.logX
    instance.logX = original
    assert instance.logX == original

@given(instance=sedml::curve_strategy)
def test_sedml::curve_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sedml::curve_strategy)
def test_sedml::curve_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sedml::curve_strategy)
def test_sedml::curve_yDataReference_type(instance):
    assert isinstance(instance.yDataReference, str)


@given(instance=sedml::curve_strategy)
def test_sedml::curve_yDataReference_setter(instance):
    original = instance.yDataReference
    instance.yDataReference = original
    assert instance.yDataReference == original

@given(instance=sedml::curve_strategy)
def test_sedml::curve_xDataReference_type(instance):
    assert isinstance(instance.xDataReference, str)


@given(instance=sedml::curve_strategy)
def test_sedml::curve_xDataReference_setter(instance):
    original = instance.xDataReference
    instance.xDataReference = original
    assert instance.xDataReference == original

@given(instance=sedml::listOfCurves_strategy)
@settings(max_examples=50)
def test_sedml::listofcurves_instantiation(instance):
    assert isinstance(instance, sedml::listOfCurves)

@given(instance=sedml::algorithm_strategy)
@settings(max_examples=50)
def test_sedml::algorithm_instantiation(instance):
    assert isinstance(instance, sedml::algorithm)

@given(instance=sedml::algorithm_strategy)
def test_sedml::algorithm_kisaoID_type(instance):
    assert isinstance(instance.kisaoID, str)


@given(instance=sedml::algorithm_strategy)
def test_sedml::algorithm_kisaoID_setter(instance):
    original = instance.kisaoID
    instance.kisaoID = original
    assert instance.kisaoID == original

@given(instance=sedml::plot2D_strategy)
@settings(max_examples=50)
def test_sedml::plot2d_instantiation(instance):
    assert isinstance(instance, sedml::plot2D)

@given(instance=sedml::plot2D_strategy)
def test_sedml::plot2d_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sedml::plot2D_strategy)
def test_sedml::plot2d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sedml::plot2D_strategy)
def test_sedml::plot2d_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sedml::plot2D_strategy)
def test_sedml::plot2d_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sedml::dataGenerator_strategy)
@settings(max_examples=50)
def test_sedml::datagenerator_instantiation(instance):
    assert isinstance(instance, sedml::dataGenerator)

@given(instance=sedml::dataGenerator_strategy)
def test_sedml::datagenerator_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sedml::dataGenerator_strategy)
def test_sedml::datagenerator_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sedml::dataGenerator_strategy)
def test_sedml::datagenerator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sedml::dataGenerator_strategy)
def test_sedml::datagenerator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sedml::task_strategy)
@settings(max_examples=50)
def test_sedml::task_instantiation(instance):
    assert isinstance(instance, sedml::task)

@given(instance=sedml::task_strategy)
def test_sedml::task_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sedml::task_strategy)
def test_sedml::task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sedml::task_strategy)
def test_sedml::task_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sedml::task_strategy)
def test_sedml::task_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sedml::model_strategy)
@settings(max_examples=50)
def test_sedml::model_instantiation(instance):
    assert isinstance(instance, sedml::model)

@given(instance=sedml::model_strategy)
def test_sedml::model_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=sedml::model_strategy)
def test_sedml::model_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=sedml::model_strategy)
def test_sedml::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sedml::model_strategy)
def test_sedml::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sedml::model_strategy)
def test_sedml::model_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=sedml::model_strategy)
def test_sedml::model_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=sedml::model_strategy)
def test_sedml::model_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sedml::model_strategy)
def test_sedml::model_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sedml::listOfOutputs_strategy)
@settings(max_examples=50)
def test_sedml::listofoutputs_instantiation(instance):
    assert isinstance(instance, sedml::listOfOutputs)

@given(instance=sedml::listOfDataGenerators_strategy)
@settings(max_examples=50)
def test_sedml::listofdatagenerators_instantiation(instance):
    assert isinstance(instance, sedml::listOfDataGenerators)

@given(instance=sedml::listOfTasks_strategy)
@settings(max_examples=50)
def test_sedml::listoftasks_instantiation(instance):
    assert isinstance(instance, sedml::listOfTasks)

@given(instance=sedml::listOfModels_strategy)
@settings(max_examples=50)
def test_sedml::listofmodels_instantiation(instance):
    assert isinstance(instance, sedml::listOfModels)

@given(instance=sedml::listOfSimulations_strategy)
@settings(max_examples=50)
def test_sedml::listofsimulations_instantiation(instance):
    assert isinstance(instance, sedml::listOfSimulations)

@given(instance=sedml::sedML_strategy)
@settings(max_examples=50)
def test_sedml::sedml_instantiation(instance):
    assert isinstance(instance, sedml::sedML)

@given(instance=sedml::sedML_strategy)
def test_sedml::sedml_version_type(instance):
    assert isinstance(instance.version, int)


@given(instance=sedml::sedML_strategy)
def test_sedml::sedml_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=sedml::sedML_strategy)
def test_sedml::sedml_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=sedml::sedML_strategy)
def test_sedml::sedml_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=sedml::uniformTimeCourse_strategy)
@settings(max_examples=50)
def test_sedml::uniformtimecourse_instantiation(instance):
    assert isinstance(instance, sedml::uniformTimeCourse)

@given(instance=sedml::uniformTimeCourse_strategy)
def test_sedml::uniformtimecourse_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sedml::uniformTimeCourse_strategy)
def test_sedml::uniformtimecourse_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sedml::uniformTimeCourse_strategy)
def test_sedml::uniformtimecourse_outputEndTime_type(instance):
    assert isinstance(instance.outputEndTime, int)


@given(instance=sedml::uniformTimeCourse_strategy)
def test_sedml::uniformtimecourse_outputEndTime_setter(instance):
    original = instance.outputEndTime
    instance.outputEndTime = original
    assert instance.outputEndTime == original

@given(instance=sedml::uniformTimeCourse_strategy)
def test_sedml::uniformtimecourse_outputStartTime_type(instance):
    assert isinstance(instance.outputStartTime, int)


@given(instance=sedml::uniformTimeCourse_strategy)
def test_sedml::uniformtimecourse_outputStartTime_setter(instance):
    original = instance.outputStartTime
    instance.outputStartTime = original
    assert instance.outputStartTime == original

@given(instance=sedml::uniformTimeCourse_strategy)
def test_sedml::uniformtimecourse_initialTime_type(instance):
    assert isinstance(instance.initialTime, int)


@given(instance=sedml::uniformTimeCourse_strategy)
def test_sedml::uniformtimecourse_initialTime_setter(instance):
    original = instance.initialTime
    instance.initialTime = original
    assert instance.initialTime == original

@given(instance=sedml::uniformTimeCourse_strategy)
def test_sedml::uniformtimecourse_numberOfPoints_type(instance):
    assert isinstance(instance.numberOfPoints, int)


@given(instance=sedml::uniformTimeCourse_strategy)
def test_sedml::uniformtimecourse_numberOfPoints_setter(instance):
    original = instance.numberOfPoints
    instance.numberOfPoints = original
    assert instance.numberOfPoints == original
