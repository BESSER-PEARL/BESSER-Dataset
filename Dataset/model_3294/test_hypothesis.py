import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MultiPopulationSIRDiseaseModel,
    multipopulation::MultiPopulationSEIRDiseaseModel,
    MultiPopulationSIDiseaseModel,
    multipopulation::MultiPopulationSIRDiseaseModel,
    multipopulation::DoubleValueList,
    multipopulation::DoubleValueMatrix,
    multipopulation::StringValueList,
    StandardDiseaseModel,
    multipopulation::MultiPopulationSIDiseaseModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_multipopulationsirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(MultiPopulationSIRDiseaseModel)


def test_multipopulationsirdiseasemodel_constructor_exists():
    assert callable(MultiPopulationSIRDiseaseModel.__init__)


def test_multipopulationsirdiseasemodel_constructor_args():
    sig = inspect.signature(MultiPopulationSIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_multipopulation::multipopulationseirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(multipopulation::MultiPopulationSEIRDiseaseModel)


def test_multipopulation::multipopulationseirdiseasemodel_constructor_exists():
    assert callable(multipopulation::MultiPopulationSEIRDiseaseModel.__init__)


def test_multipopulation::multipopulationseirdiseasemodel_constructor_args():
    sig = inspect.signature(multipopulation::MultiPopulationSEIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_multipopulationsidiseasemodel_is_not_abstract():
    assert not inspect.isabstract(MultiPopulationSIDiseaseModel)


def test_multipopulationsidiseasemodel_constructor_exists():
    assert callable(MultiPopulationSIDiseaseModel.__init__)


def test_multipopulationsidiseasemodel_constructor_args():
    sig = inspect.signature(MultiPopulationSIDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_multipopulation::multipopulationsirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(multipopulation::MultiPopulationSIRDiseaseModel)


def test_multipopulation::multipopulationsirdiseasemodel_constructor_exists():
    assert callable(multipopulation::MultiPopulationSIRDiseaseModel.__init__)


def test_multipopulation::multipopulationsirdiseasemodel_constructor_args():
    sig = inspect.signature(multipopulation::MultiPopulationSIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_multipopulation::doublevaluelist_is_not_abstract():
    assert not inspect.isabstract(multipopulation::DoubleValueList)


def test_multipopulation::doublevaluelist_constructor_exists():
    assert callable(multipopulation::DoubleValueList.__init__)


def test_multipopulation::doublevaluelist_constructor_args():
    sig = inspect.signature(multipopulation::DoubleValueList.__init__)
    params = list(sig.parameters.keys())



def test_multipopulation::doublevaluematrix_is_not_abstract():
    assert not inspect.isabstract(multipopulation::DoubleValueMatrix)


def test_multipopulation::doublevaluematrix_constructor_exists():
    assert callable(multipopulation::DoubleValueMatrix.__init__)


def test_multipopulation::doublevaluematrix_constructor_args():
    sig = inspect.signature(multipopulation::DoubleValueMatrix.__init__)
    params = list(sig.parameters.keys())



def test_multipopulation::stringvaluelist_is_not_abstract():
    assert not inspect.isabstract(multipopulation::StringValueList)


def test_multipopulation::stringvaluelist_constructor_exists():
    assert callable(multipopulation::StringValueList.__init__)


def test_multipopulation::stringvaluelist_constructor_args():
    sig = inspect.signature(multipopulation::StringValueList.__init__)
    params = list(sig.parameters.keys())



def test_standarddiseasemodel_is_not_abstract():
    assert not inspect.isabstract(StandardDiseaseModel)


def test_standarddiseasemodel_constructor_exists():
    assert callable(StandardDiseaseModel.__init__)


def test_standarddiseasemodel_constructor_args():
    sig = inspect.signature(StandardDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_multipopulation::multipopulationsidiseasemodel_is_not_abstract():
    assert not inspect.isabstract(multipopulation::MultiPopulationSIDiseaseModel)


def test_multipopulation::multipopulationsidiseasemodel_constructor_exists():
    assert callable(multipopulation::MultiPopulationSIDiseaseModel.__init__)


def test_multipopulation::multipopulationsidiseasemodel_constructor_args():
    sig = inspect.signature(multipopulation::MultiPopulationSIDiseaseModel.__init__)
    params = list(sig.parameters.keys())
    assert "characteristicMixingDistance" in params, "Missing parameter 'characteristicMixingDistance'"
    assert "roadNetworkInfectiousProportion" in params, "Missing parameter 'roadNetworkInfectiousProportion'"
    assert "physicallyAdjacentInfectiousProportion" in params, "Missing parameter 'physicallyAdjacentInfectiousProportion'"

def test_multipopulation::multipopulationsidiseasemodel_has_characteristicMixingDistance():
    assert hasattr(multipopulation::MultiPopulationSIDiseaseModel, "characteristicMixingDistance")
    descriptor = None
    for klass in multipopulation::MultiPopulationSIDiseaseModel.__mro__:
        if "characteristicMixingDistance" in klass.__dict__:
            descriptor = klass.__dict__["characteristicMixingDistance"]
            break
    assert isinstance(descriptor, property)

def test_multipopulation::multipopulationsidiseasemodel_has_roadNetworkInfectiousProportion():
    assert hasattr(multipopulation::MultiPopulationSIDiseaseModel, "roadNetworkInfectiousProportion")
    descriptor = None
    for klass in multipopulation::MultiPopulationSIDiseaseModel.__mro__:
        if "roadNetworkInfectiousProportion" in klass.__dict__:
            descriptor = klass.__dict__["roadNetworkInfectiousProportion"]
            break
    assert isinstance(descriptor, property)

def test_multipopulation::multipopulationsidiseasemodel_has_physicallyAdjacentInfectiousProportion():
    assert hasattr(multipopulation::MultiPopulationSIDiseaseModel, "physicallyAdjacentInfectiousProportion")
    descriptor = None
    for klass in multipopulation::MultiPopulationSIDiseaseModel.__mro__:
        if "physicallyAdjacentInfectiousProportion" in klass.__dict__:
            descriptor = klass.__dict__["physicallyAdjacentInfectiousProportion"]
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
MultiPopulationSIRDiseaseModel_strategy = st.builds(
    MultiPopulationSIRDiseaseModel,
)
multipopulation::MultiPopulationSEIRDiseaseModel_strategy = st.builds(
    multipopulation::MultiPopulationSEIRDiseaseModel,
)
MultiPopulationSIDiseaseModel_strategy = st.builds(
    MultiPopulationSIDiseaseModel,
)
multipopulation::MultiPopulationSIRDiseaseModel_strategy = st.builds(
    multipopulation::MultiPopulationSIRDiseaseModel,
)
multipopulation::DoubleValueList_strategy = st.builds(
    multipopulation::DoubleValueList,
)
multipopulation::DoubleValueMatrix_strategy = st.builds(
    multipopulation::DoubleValueMatrix,
)
multipopulation::StringValueList_strategy = st.builds(
    multipopulation::StringValueList,
)
StandardDiseaseModel_strategy = st.builds(
    StandardDiseaseModel,
)
multipopulation::MultiPopulationSIDiseaseModel_strategy = st.builds(
    multipopulation::MultiPopulationSIDiseaseModel,
    characteristicMixingDistance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    roadNetworkInfectiousProportion=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    physicallyAdjacentInfectiousProportion=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=MultiPopulationSIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_multipopulationsirdiseasemodel_instantiation(instance):
    assert isinstance(instance, MultiPopulationSIRDiseaseModel)

@given(instance=multipopulation::MultiPopulationSEIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_multipopulation::multipopulationseirdiseasemodel_instantiation(instance):
    assert isinstance(instance, multipopulation::MultiPopulationSEIRDiseaseModel)

@given(instance=MultiPopulationSIDiseaseModel_strategy)
@settings(max_examples=50)
def test_multipopulationsidiseasemodel_instantiation(instance):
    assert isinstance(instance, MultiPopulationSIDiseaseModel)

@given(instance=multipopulation::MultiPopulationSIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_multipopulation::multipopulationsirdiseasemodel_instantiation(instance):
    assert isinstance(instance, multipopulation::MultiPopulationSIRDiseaseModel)

@given(instance=multipopulation::DoubleValueList_strategy)
@settings(max_examples=50)
def test_multipopulation::doublevaluelist_instantiation(instance):
    assert isinstance(instance, multipopulation::DoubleValueList)

@given(instance=multipopulation::DoubleValueMatrix_strategy)
@settings(max_examples=50)
def test_multipopulation::doublevaluematrix_instantiation(instance):
    assert isinstance(instance, multipopulation::DoubleValueMatrix)

@given(instance=multipopulation::StringValueList_strategy)
@settings(max_examples=50)
def test_multipopulation::stringvaluelist_instantiation(instance):
    assert isinstance(instance, multipopulation::StringValueList)

@given(instance=StandardDiseaseModel_strategy)
@settings(max_examples=50)
def test_standarddiseasemodel_instantiation(instance):
    assert isinstance(instance, StandardDiseaseModel)

@given(instance=multipopulation::MultiPopulationSIDiseaseModel_strategy)
@settings(max_examples=50)
def test_multipopulation::multipopulationsidiseasemodel_instantiation(instance):
    assert isinstance(instance, multipopulation::MultiPopulationSIDiseaseModel)

@given(instance=multipopulation::MultiPopulationSIDiseaseModel_strategy)
def test_multipopulation::multipopulationsidiseasemodel_characteristicMixingDistance_type(instance):
    assert isinstance(instance.characteristicMixingDistance, float)


@given(instance=multipopulation::MultiPopulationSIDiseaseModel_strategy)
def test_multipopulation::multipopulationsidiseasemodel_characteristicMixingDistance_setter(instance):
    original = instance.characteristicMixingDistance
    instance.characteristicMixingDistance = original
    assert instance.characteristicMixingDistance == original

@given(instance=multipopulation::MultiPopulationSIDiseaseModel_strategy)
def test_multipopulation::multipopulationsidiseasemodel_roadNetworkInfectiousProportion_type(instance):
    assert isinstance(instance.roadNetworkInfectiousProportion, float)


@given(instance=multipopulation::MultiPopulationSIDiseaseModel_strategy)
def test_multipopulation::multipopulationsidiseasemodel_roadNetworkInfectiousProportion_setter(instance):
    original = instance.roadNetworkInfectiousProportion
    instance.roadNetworkInfectiousProportion = original
    assert instance.roadNetworkInfectiousProportion == original

@given(instance=multipopulation::MultiPopulationSIDiseaseModel_strategy)
def test_multipopulation::multipopulationsidiseasemodel_physicallyAdjacentInfectiousProportion_type(instance):
    assert isinstance(instance.physicallyAdjacentInfectiousProportion, float)


@given(instance=multipopulation::MultiPopulationSIDiseaseModel_strategy)
def test_multipopulation::multipopulationsidiseasemodel_physicallyAdjacentInfectiousProportion_setter(instance):
    original = instance.physicallyAdjacentInfectiousProportion
    instance.physicallyAdjacentInfectiousProportion = original
    assert instance.physicallyAdjacentInfectiousProportion == original
