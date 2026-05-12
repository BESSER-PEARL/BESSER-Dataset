import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MultiPopulationSIRDiseaseModel,
    multipopulation_MultiPopulationSEIRDiseaseModel,
    MultiPopulationSIDiseaseModel,
    multipopulation_MultiPopulationSIRDiseaseModel,
    multipopulation_DoubleValueList,
    multipopulation_DoubleValueMatrix,
    multipopulation_StringValueList,
    StandardDiseaseModel,
    multipopulation_MultiPopulationSIDiseaseModel,
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



def test_multipopulation_multipopulationseirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(multipopulation_MultiPopulationSEIRDiseaseModel)


def test_multipopulation_multipopulationseirdiseasemodel_constructor_exists():
    assert callable(multipopulation_MultiPopulationSEIRDiseaseModel.__init__)


def test_multipopulation_multipopulationseirdiseasemodel_constructor_args():
    sig = inspect.signature(multipopulation_MultiPopulationSEIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_multipopulationsidiseasemodel_is_not_abstract():
    assert not inspect.isabstract(MultiPopulationSIDiseaseModel)


def test_multipopulationsidiseasemodel_constructor_exists():
    assert callable(MultiPopulationSIDiseaseModel.__init__)


def test_multipopulationsidiseasemodel_constructor_args():
    sig = inspect.signature(MultiPopulationSIDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_multipopulation_multipopulationsirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(multipopulation_MultiPopulationSIRDiseaseModel)


def test_multipopulation_multipopulationsirdiseasemodel_constructor_exists():
    assert callable(multipopulation_MultiPopulationSIRDiseaseModel.__init__)


def test_multipopulation_multipopulationsirdiseasemodel_constructor_args():
    sig = inspect.signature(multipopulation_MultiPopulationSIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_multipopulation_doublevaluelist_is_not_abstract():
    assert not inspect.isabstract(multipopulation_DoubleValueList)


def test_multipopulation_doublevaluelist_constructor_exists():
    assert callable(multipopulation_DoubleValueList.__init__)


def test_multipopulation_doublevaluelist_constructor_args():
    sig = inspect.signature(multipopulation_DoubleValueList.__init__)
    params = list(sig.parameters.keys())



def test_multipopulation_doublevaluematrix_is_not_abstract():
    assert not inspect.isabstract(multipopulation_DoubleValueMatrix)


def test_multipopulation_doublevaluematrix_constructor_exists():
    assert callable(multipopulation_DoubleValueMatrix.__init__)


def test_multipopulation_doublevaluematrix_constructor_args():
    sig = inspect.signature(multipopulation_DoubleValueMatrix.__init__)
    params = list(sig.parameters.keys())



def test_multipopulation_stringvaluelist_is_not_abstract():
    assert not inspect.isabstract(multipopulation_StringValueList)


def test_multipopulation_stringvaluelist_constructor_exists():
    assert callable(multipopulation_StringValueList.__init__)


def test_multipopulation_stringvaluelist_constructor_args():
    sig = inspect.signature(multipopulation_StringValueList.__init__)
    params = list(sig.parameters.keys())



def test_standarddiseasemodel_is_not_abstract():
    assert not inspect.isabstract(StandardDiseaseModel)


def test_standarddiseasemodel_constructor_exists():
    assert callable(StandardDiseaseModel.__init__)


def test_standarddiseasemodel_constructor_args():
    sig = inspect.signature(StandardDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_multipopulation_multipopulationsidiseasemodel_is_not_abstract():
    assert not inspect.isabstract(multipopulation_MultiPopulationSIDiseaseModel)


def test_multipopulation_multipopulationsidiseasemodel_constructor_exists():
    assert callable(multipopulation_MultiPopulationSIDiseaseModel.__init__)


def test_multipopulation_multipopulationsidiseasemodel_constructor_args():
    sig = inspect.signature(multipopulation_MultiPopulationSIDiseaseModel.__init__)
    params = list(sig.parameters.keys())
    assert "characteristicMixingDistance" in params, "Missing parameter 'characteristicMixingDistance'"
    assert "physicallyAdjacentInfectiousProportion" in params, "Missing parameter 'physicallyAdjacentInfectiousProportion'"
    assert "roadNetworkInfectiousProportion" in params, "Missing parameter 'roadNetworkInfectiousProportion'"

def test_multipopulation_multipopulationsidiseasemodel_has_characteristicMixingDistance():
    assert hasattr(multipopulation_MultiPopulationSIDiseaseModel, "characteristicMixingDistance")
    descriptor = None
    for klass in multipopulation_MultiPopulationSIDiseaseModel.__mro__:
        if "characteristicMixingDistance" in klass.__dict__:
            descriptor = klass.__dict__["characteristicMixingDistance"]
            break
    assert isinstance(descriptor, property)

def test_multipopulation_multipopulationsidiseasemodel_has_physicallyAdjacentInfectiousProportion():
    assert hasattr(multipopulation_MultiPopulationSIDiseaseModel, "physicallyAdjacentInfectiousProportion")
    descriptor = None
    for klass in multipopulation_MultiPopulationSIDiseaseModel.__mro__:
        if "physicallyAdjacentInfectiousProportion" in klass.__dict__:
            descriptor = klass.__dict__["physicallyAdjacentInfectiousProportion"]
            break
    assert isinstance(descriptor, property)

def test_multipopulation_multipopulationsidiseasemodel_has_roadNetworkInfectiousProportion():
    assert hasattr(multipopulation_MultiPopulationSIDiseaseModel, "roadNetworkInfectiousProportion")
    descriptor = None
    for klass in multipopulation_MultiPopulationSIDiseaseModel.__mro__:
        if "roadNetworkInfectiousProportion" in klass.__dict__:
            descriptor = klass.__dict__["roadNetworkInfectiousProportion"]
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
multipopulation_MultiPopulationSEIRDiseaseModel_strategy = st.builds(
    multipopulation_MultiPopulationSEIRDiseaseModel,
)
MultiPopulationSIDiseaseModel_strategy = st.builds(
    MultiPopulationSIDiseaseModel,
)
multipopulation_MultiPopulationSIRDiseaseModel_strategy = st.builds(
    multipopulation_MultiPopulationSIRDiseaseModel,
)
multipopulation_DoubleValueList_strategy = st.builds(
    multipopulation_DoubleValueList,
)
multipopulation_DoubleValueMatrix_strategy = st.builds(
    multipopulation_DoubleValueMatrix,
)
multipopulation_StringValueList_strategy = st.builds(
    multipopulation_StringValueList,
)
StandardDiseaseModel_strategy = st.builds(
    StandardDiseaseModel,
)
multipopulation_MultiPopulationSIDiseaseModel_strategy = st.builds(
    multipopulation_MultiPopulationSIDiseaseModel,
    characteristicMixingDistance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    physicallyAdjacentInfectiousProportion=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    roadNetworkInfectiousProportion=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=MultiPopulationSIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_multipopulationsirdiseasemodel_instantiation(instance):
    assert isinstance(instance, MultiPopulationSIRDiseaseModel)

@given(instance=multipopulation_MultiPopulationSEIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_multipopulation_multipopulationseirdiseasemodel_instantiation(instance):
    assert isinstance(instance, multipopulation_MultiPopulationSEIRDiseaseModel)

@given(instance=MultiPopulationSIDiseaseModel_strategy)
@settings(max_examples=50)
def test_multipopulationsidiseasemodel_instantiation(instance):
    assert isinstance(instance, MultiPopulationSIDiseaseModel)

@given(instance=multipopulation_MultiPopulationSIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_multipopulation_multipopulationsirdiseasemodel_instantiation(instance):
    assert isinstance(instance, multipopulation_MultiPopulationSIRDiseaseModel)

@given(instance=multipopulation_DoubleValueList_strategy)
@settings(max_examples=50)
def test_multipopulation_doublevaluelist_instantiation(instance):
    assert isinstance(instance, multipopulation_DoubleValueList)

@given(instance=multipopulation_DoubleValueMatrix_strategy)
@settings(max_examples=50)
def test_multipopulation_doublevaluematrix_instantiation(instance):
    assert isinstance(instance, multipopulation_DoubleValueMatrix)

@given(instance=multipopulation_StringValueList_strategy)
@settings(max_examples=50)
def test_multipopulation_stringvaluelist_instantiation(instance):
    assert isinstance(instance, multipopulation_StringValueList)

@given(instance=StandardDiseaseModel_strategy)
@settings(max_examples=50)
def test_standarddiseasemodel_instantiation(instance):
    assert isinstance(instance, StandardDiseaseModel)

@given(instance=multipopulation_MultiPopulationSIDiseaseModel_strategy)
@settings(max_examples=50)
def test_multipopulation_multipopulationsidiseasemodel_instantiation(instance):
    assert isinstance(instance, multipopulation_MultiPopulationSIDiseaseModel)



@given(instance=multipopulation_MultiPopulationSIDiseaseModel_strategy)
def test_multipopulation_multipopulationsidiseasemodel_characteristicMixingDistance_setter(instance):
    original = instance.characteristicMixingDistance
    instance.characteristicMixingDistance = original
    assert instance.characteristicMixingDistance == original



@given(instance=multipopulation_MultiPopulationSIDiseaseModel_strategy)
def test_multipopulation_multipopulationsidiseasemodel_physicallyAdjacentInfectiousProportion_setter(instance):
    original = instance.physicallyAdjacentInfectiousProportion
    instance.physicallyAdjacentInfectiousProportion = original
    assert instance.physicallyAdjacentInfectiousProportion == original



@given(instance=multipopulation_MultiPopulationSIDiseaseModel_strategy)
def test_multipopulation_multipopulationsidiseasemodel_roadNetworkInfectiousProportion_setter(instance):
    original = instance.roadNetworkInfectiousProportion
    instance.roadNetworkInfectiousProportion = original
    assert instance.roadNetworkInfectiousProportion == original
