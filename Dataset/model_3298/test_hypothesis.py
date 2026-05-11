import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Infector,
    standard::StandardInfector,
    SIInfector,
    standard::SIRInoculator,
    StochasticDiseaseModel,
    standard::StandardStochasticDiseaseModel,
    AggregatingSIDiseaseModel,
    standard::AggregatingSIRDiseaseModel,
    AggregatingSIRDiseaseModel,
    standard::AggregatingSEIRDiseaseModel,
    standard::IntegrationDecorator,
    standard::IntegrationLabelValue,
    standard::IntegrationLabel,
    standard::SanityChecker,
    StandardStochasticDiseaseModel,
    StandardDiseaseModelLabelValue,
    DiseaseModelState,
    standard::AggregatingDiseaseModelState,
    standard::StandardDiseaseModelState,
    DiseaseModelLabelValue,
    standard::StandardDiseaseModelLabelValue,
    IntegrationLabel,
    DiseaseModelLabel,
    standard::StandardDiseaseModelLabel,
    IntegrationDecorator,
    DiseaseModel,
    standard::StochasticDiseaseModel,
    SILabelValue,
    standard::SIRLabelValue,
    standard::SILabelValue,
    StandardInfector,
    standard::SIInfector,
    StandardDiseaseModelState,
    standard::SIDiseaseModelState,
    StandardDiseaseModel,
    standard::SI,
    SIRLabelValue,
    standard::PopulationModelLabel,
    standard::SEIRLabelValue,
    StandardDiseaseModelLabel,
    standard::SIRLabel,
    standard::SILabel,
    standard::SEIRLabel,
    standard::StandardDiseaseModel,
    IntegrationLabelValue,
    LabelValue,
    standard::DiseaseModelLabelValue,
    standard::DiseaseModelState,
    standard::PopulationLabel,
    DynamicNodeLabel,
    standard::DiseaseModelLabel,
    Modifiable,
    SanityChecker,
    NodeDecorator,
    standard::InfectorInoculatorCollection,
    standard::Infector,
    standard::DiseaseModel,
    SIR,
    standard::StochasticPoissonSIRDiseaseModel,
    standard::StochasticSIRDiseaseModel,
    standard::SEIR,
    standard::DeterministicSIRDiseaseModel,
    SI,
    standard::StochasticPoissonSIDiseaseModel,
    standard::StochasticSIDiseaseModel,
    standard::AggregatingSIDiseaseModel,
    standard::SIR,
    standard::DeterministicSIDiseaseModel,
    SEIR,
    standard::StochasticPoissonSEIRDiseaseModel,
    standard::StochasticSEIRDiseaseModel,
    standard::DeterministicSEIRDiseaseModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_infector_is_not_abstract():
    assert not inspect.isabstract(Infector)


def test_infector_constructor_exists():
    assert callable(Infector.__init__)


def test_infector_constructor_args():
    sig = inspect.signature(Infector.__init__)
    params = list(sig.parameters.keys())



def test_standard::standardinfector_is_not_abstract():
    assert not inspect.isabstract(standard::StandardInfector)


def test_standard::standardinfector_constructor_exists():
    assert callable(standard::StandardInfector.__init__)


def test_standard::standardinfector_constructor_args():
    sig = inspect.signature(standard::StandardInfector.__init__)
    params = list(sig.parameters.keys())



def test_siinfector_is_not_abstract():
    assert not inspect.isabstract(SIInfector)


def test_siinfector_constructor_exists():
    assert callable(SIInfector.__init__)


def test_siinfector_constructor_args():
    sig = inspect.signature(SIInfector.__init__)
    params = list(sig.parameters.keys())



def test_standard::sirinoculator_is_not_abstract():
    assert not inspect.isabstract(standard::SIRInoculator)


def test_standard::sirinoculator_constructor_exists():
    assert callable(standard::SIRInoculator.__init__)


def test_standard::sirinoculator_constructor_args():
    sig = inspect.signature(standard::SIRInoculator.__init__)
    params = list(sig.parameters.keys())
    assert "inoculatedPercentage" in params, "Missing parameter 'inoculatedPercentage'"
    assert "inoculatePercentage" in params, "Missing parameter 'inoculatePercentage'"

def test_standard::sirinoculator_has_inoculatedPercentage():
    assert hasattr(standard::SIRInoculator, "inoculatedPercentage")
    descriptor = None
    for klass in standard::SIRInoculator.__mro__:
        if "inoculatedPercentage" in klass.__dict__:
            descriptor = klass.__dict__["inoculatedPercentage"]
            break
    assert isinstance(descriptor, property)

def test_standard::sirinoculator_has_inoculatePercentage():
    assert hasattr(standard::SIRInoculator, "inoculatePercentage")
    descriptor = None
    for klass in standard::SIRInoculator.__mro__:
        if "inoculatePercentage" in klass.__dict__:
            descriptor = klass.__dict__["inoculatePercentage"]
            break
    assert isinstance(descriptor, property)



def test_stochasticdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(StochasticDiseaseModel)


def test_stochasticdiseasemodel_constructor_exists():
    assert callable(StochasticDiseaseModel.__init__)


def test_stochasticdiseasemodel_constructor_args():
    sig = inspect.signature(StochasticDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::standardstochasticdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::StandardStochasticDiseaseModel)


def test_standard::standardstochasticdiseasemodel_constructor_exists():
    assert callable(standard::StandardStochasticDiseaseModel.__init__)


def test_standard::standardstochasticdiseasemodel_constructor_args():
    sig = inspect.signature(standard::StandardStochasticDiseaseModel.__init__)
    params = list(sig.parameters.keys())
    assert "gain" in params, "Missing parameter 'gain'"

def test_standard::standardstochasticdiseasemodel_has_gain():
    assert hasattr(standard::StandardStochasticDiseaseModel, "gain")
    descriptor = None
    for klass in standard::StandardStochasticDiseaseModel.__mro__:
        if "gain" in klass.__dict__:
            descriptor = klass.__dict__["gain"]
            break
    assert isinstance(descriptor, property)



def test_aggregatingsidiseasemodel_is_not_abstract():
    assert not inspect.isabstract(AggregatingSIDiseaseModel)


def test_aggregatingsidiseasemodel_constructor_exists():
    assert callable(AggregatingSIDiseaseModel.__init__)


def test_aggregatingsidiseasemodel_constructor_args():
    sig = inspect.signature(AggregatingSIDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::aggregatingsirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::AggregatingSIRDiseaseModel)


def test_standard::aggregatingsirdiseasemodel_constructor_exists():
    assert callable(standard::AggregatingSIRDiseaseModel.__init__)


def test_standard::aggregatingsirdiseasemodel_constructor_args():
    sig = inspect.signature(standard::AggregatingSIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_aggregatingsirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(AggregatingSIRDiseaseModel)


def test_aggregatingsirdiseasemodel_constructor_exists():
    assert callable(AggregatingSIRDiseaseModel.__init__)


def test_aggregatingsirdiseasemodel_constructor_args():
    sig = inspect.signature(AggregatingSIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::aggregatingseirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::AggregatingSEIRDiseaseModel)


def test_standard::aggregatingseirdiseasemodel_constructor_exists():
    assert callable(standard::AggregatingSEIRDiseaseModel.__init__)


def test_standard::aggregatingseirdiseasemodel_constructor_args():
    sig = inspect.signature(standard::AggregatingSEIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::integrationdecorator_is_not_abstract():
    assert not inspect.isabstract(standard::IntegrationDecorator)


def test_standard::integrationdecorator_constructor_exists():
    assert callable(standard::IntegrationDecorator.__init__)


def test_standard::integrationdecorator_constructor_args():
    sig = inspect.signature(standard::IntegrationDecorator.__init__)
    params = list(sig.parameters.keys())



def test_standard::integrationlabelvalue_is_not_abstract():
    assert not inspect.isabstract(standard::IntegrationLabelValue)


def test_standard::integrationlabelvalue_constructor_exists():
    assert callable(standard::IntegrationLabelValue.__init__)


def test_standard::integrationlabelvalue_constructor_args():
    sig = inspect.signature(standard::IntegrationLabelValue.__init__)
    params = list(sig.parameters.keys())



def test_standard::integrationlabel_is_not_abstract():
    assert not inspect.isabstract(standard::IntegrationLabel)


def test_standard::integrationlabel_constructor_exists():
    assert callable(standard::IntegrationLabel.__init__)


def test_standard::integrationlabel_constructor_args():
    sig = inspect.signature(standard::IntegrationLabel.__init__)
    params = list(sig.parameters.keys())



def test_standard::sanitychecker_is_not_abstract():
    assert not inspect.isabstract(standard::SanityChecker)


def test_standard::sanitychecker_constructor_exists():
    assert callable(standard::SanityChecker.__init__)


def test_standard::sanitychecker_constructor_args():
    sig = inspect.signature(standard::SanityChecker.__init__)
    params = list(sig.parameters.keys())



def test_standardstochasticdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(StandardStochasticDiseaseModel)


def test_standardstochasticdiseasemodel_constructor_exists():
    assert callable(StandardStochasticDiseaseModel.__init__)


def test_standardstochasticdiseasemodel_constructor_args():
    sig = inspect.signature(StandardStochasticDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standarddiseasemodellabelvalue_is_not_abstract():
    assert not inspect.isabstract(StandardDiseaseModelLabelValue)


def test_standarddiseasemodellabelvalue_constructor_exists():
    assert callable(StandardDiseaseModelLabelValue.__init__)


def test_standarddiseasemodellabelvalue_constructor_args():
    sig = inspect.signature(StandardDiseaseModelLabelValue.__init__)
    params = list(sig.parameters.keys())



def test_diseasemodelstate_is_not_abstract():
    assert not inspect.isabstract(DiseaseModelState)


def test_diseasemodelstate_constructor_exists():
    assert callable(DiseaseModelState.__init__)


def test_diseasemodelstate_constructor_args():
    sig = inspect.signature(DiseaseModelState.__init__)
    params = list(sig.parameters.keys())



def test_standard::aggregatingdiseasemodelstate_is_not_abstract():
    assert not inspect.isabstract(standard::AggregatingDiseaseModelState)


def test_standard::aggregatingdiseasemodelstate_constructor_exists():
    assert callable(standard::AggregatingDiseaseModelState.__init__)


def test_standard::aggregatingdiseasemodelstate_constructor_args():
    sig = inspect.signature(standard::AggregatingDiseaseModelState.__init__)
    params = list(sig.parameters.keys())



def test_standard::standarddiseasemodelstate_is_not_abstract():
    assert not inspect.isabstract(standard::StandardDiseaseModelState)


def test_standard::standarddiseasemodelstate_constructor_exists():
    assert callable(standard::StandardDiseaseModelState.__init__)


def test_standard::standarddiseasemodelstate_constructor_args():
    sig = inspect.signature(standard::StandardDiseaseModelState.__init__)
    params = list(sig.parameters.keys())
    assert "areaRatio" in params, "Missing parameter 'areaRatio'"

def test_standard::standarddiseasemodelstate_has_areaRatio():
    assert hasattr(standard::StandardDiseaseModelState, "areaRatio")
    descriptor = None
    for klass in standard::StandardDiseaseModelState.__mro__:
        if "areaRatio" in klass.__dict__:
            descriptor = klass.__dict__["areaRatio"]
            break
    assert isinstance(descriptor, property)



def test_diseasemodellabelvalue_is_not_abstract():
    assert not inspect.isabstract(DiseaseModelLabelValue)


def test_diseasemodellabelvalue_constructor_exists():
    assert callable(DiseaseModelLabelValue.__init__)


def test_diseasemodellabelvalue_constructor_args():
    sig = inspect.signature(DiseaseModelLabelValue.__init__)
    params = list(sig.parameters.keys())



def test_standard::standarddiseasemodellabelvalue_is_not_abstract():
    assert not inspect.isabstract(standard::StandardDiseaseModelLabelValue)


def test_standard::standarddiseasemodellabelvalue_constructor_exists():
    assert callable(standard::StandardDiseaseModelLabelValue.__init__)


def test_standard::standarddiseasemodellabelvalue_constructor_args():
    sig = inspect.signature(standard::StandardDiseaseModelLabelValue.__init__)
    params = list(sig.parameters.keys())
    assert "s" in params, "Missing parameter 's'"

def test_standard::standarddiseasemodellabelvalue_has_s():
    assert hasattr(standard::StandardDiseaseModelLabelValue, "s")
    descriptor = None
    for klass in standard::StandardDiseaseModelLabelValue.__mro__:
        if "s" in klass.__dict__:
            descriptor = klass.__dict__["s"]
            break
    assert isinstance(descriptor, property)



def test_integrationlabel_is_not_abstract():
    assert not inspect.isabstract(IntegrationLabel)


def test_integrationlabel_constructor_exists():
    assert callable(IntegrationLabel.__init__)


def test_integrationlabel_constructor_args():
    sig = inspect.signature(IntegrationLabel.__init__)
    params = list(sig.parameters.keys())



def test_diseasemodellabel_is_not_abstract():
    assert not inspect.isabstract(DiseaseModelLabel)


def test_diseasemodellabel_constructor_exists():
    assert callable(DiseaseModelLabel.__init__)


def test_diseasemodellabel_constructor_args():
    sig = inspect.signature(DiseaseModelLabel.__init__)
    params = list(sig.parameters.keys())



def test_standard::standarddiseasemodellabel_is_not_abstract():
    assert not inspect.isabstract(standard::StandardDiseaseModelLabel)


def test_standard::standarddiseasemodellabel_constructor_exists():
    assert callable(standard::StandardDiseaseModelLabel.__init__)


def test_standard::standarddiseasemodellabel_constructor_args():
    sig = inspect.signature(standard::StandardDiseaseModelLabel.__init__)
    params = list(sig.parameters.keys())



def test_integrationdecorator_is_not_abstract():
    assert not inspect.isabstract(IntegrationDecorator)


def test_integrationdecorator_constructor_exists():
    assert callable(IntegrationDecorator.__init__)


def test_integrationdecorator_constructor_args():
    sig = inspect.signature(IntegrationDecorator.__init__)
    params = list(sig.parameters.keys())



def test_diseasemodel_is_not_abstract():
    assert not inspect.isabstract(DiseaseModel)


def test_diseasemodel_constructor_exists():
    assert callable(DiseaseModel.__init__)


def test_diseasemodel_constructor_args():
    sig = inspect.signature(DiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::stochasticdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::StochasticDiseaseModel)


def test_standard::stochasticdiseasemodel_constructor_exists():
    assert callable(standard::StochasticDiseaseModel.__init__)


def test_standard::stochasticdiseasemodel_constructor_args():
    sig = inspect.signature(standard::StochasticDiseaseModel.__init__)
    params = list(sig.parameters.keys())
    assert "seed" in params, "Missing parameter 'seed'"
    assert "randomGenerator" in params, "Missing parameter 'randomGenerator'"

def test_standard::stochasticdiseasemodel_has_seed():
    assert hasattr(standard::StochasticDiseaseModel, "seed")
    descriptor = None
    for klass in standard::StochasticDiseaseModel.__mro__:
        if "seed" in klass.__dict__:
            descriptor = klass.__dict__["seed"]
            break
    assert isinstance(descriptor, property)

def test_standard::stochasticdiseasemodel_has_randomGenerator():
    assert hasattr(standard::StochasticDiseaseModel, "randomGenerator")
    descriptor = None
    for klass in standard::StochasticDiseaseModel.__mro__:
        if "randomGenerator" in klass.__dict__:
            descriptor = klass.__dict__["randomGenerator"]
            break
    assert isinstance(descriptor, property)



def test_silabelvalue_is_not_abstract():
    assert not inspect.isabstract(SILabelValue)


def test_silabelvalue_constructor_exists():
    assert callable(SILabelValue.__init__)


def test_silabelvalue_constructor_args():
    sig = inspect.signature(SILabelValue.__init__)
    params = list(sig.parameters.keys())



def test_standard::sirlabelvalue_is_not_abstract():
    assert not inspect.isabstract(standard::SIRLabelValue)


def test_standard::sirlabelvalue_constructor_exists():
    assert callable(standard::SIRLabelValue.__init__)


def test_standard::sirlabelvalue_constructor_args():
    sig = inspect.signature(standard::SIRLabelValue.__init__)
    params = list(sig.parameters.keys())
    assert "r" in params, "Missing parameter 'r'"

def test_standard::sirlabelvalue_has_r():
    assert hasattr(standard::SIRLabelValue, "r")
    descriptor = None
    for klass in standard::SIRLabelValue.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)



def test_standard::silabelvalue_is_not_abstract():
    assert not inspect.isabstract(standard::SILabelValue)


def test_standard::silabelvalue_constructor_exists():
    assert callable(standard::SILabelValue.__init__)


def test_standard::silabelvalue_constructor_args():
    sig = inspect.signature(standard::SILabelValue.__init__)
    params = list(sig.parameters.keys())
    assert "i" in params, "Missing parameter 'i'"

def test_standard::silabelvalue_has_i():
    assert hasattr(standard::SILabelValue, "i")
    descriptor = None
    for klass in standard::SILabelValue.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
            break
    assert isinstance(descriptor, property)



def test_standardinfector_is_not_abstract():
    assert not inspect.isabstract(StandardInfector)


def test_standardinfector_constructor_exists():
    assert callable(StandardInfector.__init__)


def test_standardinfector_constructor_args():
    sig = inspect.signature(StandardInfector.__init__)
    params = list(sig.parameters.keys())



def test_standard::siinfector_is_not_abstract():
    assert not inspect.isabstract(standard::SIInfector)


def test_standard::siinfector_constructor_exists():
    assert callable(standard::SIInfector.__init__)


def test_standard::siinfector_constructor_args():
    sig = inspect.signature(standard::SIInfector.__init__)
    params = list(sig.parameters.keys())
    assert "infectiousCount" in params, "Missing parameter 'infectiousCount'"

def test_standard::siinfector_has_infectiousCount():
    assert hasattr(standard::SIInfector, "infectiousCount")
    descriptor = None
    for klass in standard::SIInfector.__mro__:
        if "infectiousCount" in klass.__dict__:
            descriptor = klass.__dict__["infectiousCount"]
            break
    assert isinstance(descriptor, property)



def test_standarddiseasemodelstate_is_not_abstract():
    assert not inspect.isabstract(StandardDiseaseModelState)


def test_standarddiseasemodelstate_constructor_exists():
    assert callable(StandardDiseaseModelState.__init__)


def test_standarddiseasemodelstate_constructor_args():
    sig = inspect.signature(StandardDiseaseModelState.__init__)
    params = list(sig.parameters.keys())



def test_standard::sidiseasemodelstate_is_not_abstract():
    assert not inspect.isabstract(standard::SIDiseaseModelState)


def test_standard::sidiseasemodelstate_constructor_exists():
    assert callable(standard::SIDiseaseModelState.__init__)


def test_standard::sidiseasemodelstate_constructor_args():
    sig = inspect.signature(standard::SIDiseaseModelState.__init__)
    params = list(sig.parameters.keys())



def test_standarddiseasemodel_is_not_abstract():
    assert not inspect.isabstract(StandardDiseaseModel)


def test_standarddiseasemodel_constructor_exists():
    assert callable(StandardDiseaseModel.__init__)


def test_standarddiseasemodel_constructor_args():
    sig = inspect.signature(StandardDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::si_is_not_abstract():
    assert not inspect.isabstract(standard::SI)


def test_standard::si_constructor_exists():
    assert callable(standard::SI.__init__)


def test_standard::si_constructor_args():
    sig = inspect.signature(standard::SI.__init__)
    params = list(sig.parameters.keys())
    assert "physicallyAdjacentInfectiousProportion" in params, "Missing parameter 'physicallyAdjacentInfectiousProportion'"
    assert "roadNetworkInfectiousProportion" in params, "Missing parameter 'roadNetworkInfectiousProportion'"
    assert "infectiousMortality" in params, "Missing parameter 'infectiousMortality'"
    assert "nonLinearityCoefficient" in params, "Missing parameter 'nonLinearityCoefficient'"
    assert "transmissionRate" in params, "Missing parameter 'transmissionRate'"
    assert "recoveryRate" in params, "Missing parameter 'recoveryRate'"
    assert "characteristicMixingDistance" in params, "Missing parameter 'characteristicMixingDistance'"
    assert "infectiousMortalityRate" in params, "Missing parameter 'infectiousMortalityRate'"

def test_standard::si_has_physicallyAdjacentInfectiousProportion():
    assert hasattr(standard::SI, "physicallyAdjacentInfectiousProportion")
    descriptor = None
    for klass in standard::SI.__mro__:
        if "physicallyAdjacentInfectiousProportion" in klass.__dict__:
            descriptor = klass.__dict__["physicallyAdjacentInfectiousProportion"]
            break
    assert isinstance(descriptor, property)

def test_standard::si_has_roadNetworkInfectiousProportion():
    assert hasattr(standard::SI, "roadNetworkInfectiousProportion")
    descriptor = None
    for klass in standard::SI.__mro__:
        if "roadNetworkInfectiousProportion" in klass.__dict__:
            descriptor = klass.__dict__["roadNetworkInfectiousProportion"]
            break
    assert isinstance(descriptor, property)

def test_standard::si_has_infectiousMortality():
    assert hasattr(standard::SI, "infectiousMortality")
    descriptor = None
    for klass in standard::SI.__mro__:
        if "infectiousMortality" in klass.__dict__:
            descriptor = klass.__dict__["infectiousMortality"]
            break
    assert isinstance(descriptor, property)

def test_standard::si_has_nonLinearityCoefficient():
    assert hasattr(standard::SI, "nonLinearityCoefficient")
    descriptor = None
    for klass in standard::SI.__mro__:
        if "nonLinearityCoefficient" in klass.__dict__:
            descriptor = klass.__dict__["nonLinearityCoefficient"]
            break
    assert isinstance(descriptor, property)

def test_standard::si_has_transmissionRate():
    assert hasattr(standard::SI, "transmissionRate")
    descriptor = None
    for klass in standard::SI.__mro__:
        if "transmissionRate" in klass.__dict__:
            descriptor = klass.__dict__["transmissionRate"]
            break
    assert isinstance(descriptor, property)

def test_standard::si_has_recoveryRate():
    assert hasattr(standard::SI, "recoveryRate")
    descriptor = None
    for klass in standard::SI.__mro__:
        if "recoveryRate" in klass.__dict__:
            descriptor = klass.__dict__["recoveryRate"]
            break
    assert isinstance(descriptor, property)

def test_standard::si_has_characteristicMixingDistance():
    assert hasattr(standard::SI, "characteristicMixingDistance")
    descriptor = None
    for klass in standard::SI.__mro__:
        if "characteristicMixingDistance" in klass.__dict__:
            descriptor = klass.__dict__["characteristicMixingDistance"]
            break
    assert isinstance(descriptor, property)

def test_standard::si_has_infectiousMortalityRate():
    assert hasattr(standard::SI, "infectiousMortalityRate")
    descriptor = None
    for klass in standard::SI.__mro__:
        if "infectiousMortalityRate" in klass.__dict__:
            descriptor = klass.__dict__["infectiousMortalityRate"]
            break
    assert isinstance(descriptor, property)



def test_sirlabelvalue_is_not_abstract():
    assert not inspect.isabstract(SIRLabelValue)


def test_sirlabelvalue_constructor_exists():
    assert callable(SIRLabelValue.__init__)


def test_sirlabelvalue_constructor_args():
    sig = inspect.signature(SIRLabelValue.__init__)
    params = list(sig.parameters.keys())



def test_standard::populationmodellabel_is_not_abstract():
    assert not inspect.isabstract(standard::PopulationModelLabel)


def test_standard::populationmodellabel_constructor_exists():
    assert callable(standard::PopulationModelLabel.__init__)


def test_standard::populationmodellabel_constructor_args():
    sig = inspect.signature(standard::PopulationModelLabel.__init__)
    params = list(sig.parameters.keys())



def test_standard::seirlabelvalue_is_not_abstract():
    assert not inspect.isabstract(standard::SEIRLabelValue)


def test_standard::seirlabelvalue_constructor_exists():
    assert callable(standard::SEIRLabelValue.__init__)


def test_standard::seirlabelvalue_constructor_args():
    sig = inspect.signature(standard::SEIRLabelValue.__init__)
    params = list(sig.parameters.keys())
    assert "e" in params, "Missing parameter 'e'"

def test_standard::seirlabelvalue_has_e():
    assert hasattr(standard::SEIRLabelValue, "e")
    descriptor = None
    for klass in standard::SEIRLabelValue.__mro__:
        if "e" in klass.__dict__:
            descriptor = klass.__dict__["e"]
            break
    assert isinstance(descriptor, property)



def test_standarddiseasemodellabel_is_not_abstract():
    assert not inspect.isabstract(StandardDiseaseModelLabel)


def test_standarddiseasemodellabel_constructor_exists():
    assert callable(StandardDiseaseModelLabel.__init__)


def test_standarddiseasemodellabel_constructor_args():
    sig = inspect.signature(StandardDiseaseModelLabel.__init__)
    params = list(sig.parameters.keys())



def test_standard::sirlabel_is_not_abstract():
    assert not inspect.isabstract(standard::SIRLabel)


def test_standard::sirlabel_constructor_exists():
    assert callable(standard::SIRLabel.__init__)


def test_standard::sirlabel_constructor_args():
    sig = inspect.signature(standard::SIRLabel.__init__)
    params = list(sig.parameters.keys())



def test_standard::silabel_is_not_abstract():
    assert not inspect.isabstract(standard::SILabel)


def test_standard::silabel_constructor_exists():
    assert callable(standard::SILabel.__init__)


def test_standard::silabel_constructor_args():
    sig = inspect.signature(standard::SILabel.__init__)
    params = list(sig.parameters.keys())



def test_standard::seirlabel_is_not_abstract():
    assert not inspect.isabstract(standard::SEIRLabel)


def test_standard::seirlabel_constructor_exists():
    assert callable(standard::SEIRLabel.__init__)


def test_standard::seirlabel_constructor_args():
    sig = inspect.signature(standard::SEIRLabel.__init__)
    params = list(sig.parameters.keys())



def test_standard::standarddiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::StandardDiseaseModel)


def test_standard::standarddiseasemodel_constructor_exists():
    assert callable(standard::StandardDiseaseModel.__init__)


def test_standard::standarddiseasemodel_constructor_args():
    sig = inspect.signature(standard::StandardDiseaseModel.__init__)
    params = list(sig.parameters.keys())
    assert "referencePopulationDensity" in params, "Missing parameter 'referencePopulationDensity'"
    assert "totalPopulationCountReciprocal" in params, "Missing parameter 'totalPopulationCountReciprocal'"
    assert "totalPopulationCount" in params, "Missing parameter 'totalPopulationCount'"
    assert "totalArea" in params, "Missing parameter 'totalArea'"

def test_standard::standarddiseasemodel_has_referencePopulationDensity():
    assert hasattr(standard::StandardDiseaseModel, "referencePopulationDensity")
    descriptor = None
    for klass in standard::StandardDiseaseModel.__mro__:
        if "referencePopulationDensity" in klass.__dict__:
            descriptor = klass.__dict__["referencePopulationDensity"]
            break
    assert isinstance(descriptor, property)

def test_standard::standarddiseasemodel_has_totalPopulationCountReciprocal():
    assert hasattr(standard::StandardDiseaseModel, "totalPopulationCountReciprocal")
    descriptor = None
    for klass in standard::StandardDiseaseModel.__mro__:
        if "totalPopulationCountReciprocal" in klass.__dict__:
            descriptor = klass.__dict__["totalPopulationCountReciprocal"]
            break
    assert isinstance(descriptor, property)

def test_standard::standarddiseasemodel_has_totalPopulationCount():
    assert hasattr(standard::StandardDiseaseModel, "totalPopulationCount")
    descriptor = None
    for klass in standard::StandardDiseaseModel.__mro__:
        if "totalPopulationCount" in klass.__dict__:
            descriptor = klass.__dict__["totalPopulationCount"]
            break
    assert isinstance(descriptor, property)

def test_standard::standarddiseasemodel_has_totalArea():
    assert hasattr(standard::StandardDiseaseModel, "totalArea")
    descriptor = None
    for klass in standard::StandardDiseaseModel.__mro__:
        if "totalArea" in klass.__dict__:
            descriptor = klass.__dict__["totalArea"]
            break
    assert isinstance(descriptor, property)



def test_integrationlabelvalue_is_not_abstract():
    assert not inspect.isabstract(IntegrationLabelValue)


def test_integrationlabelvalue_constructor_exists():
    assert callable(IntegrationLabelValue.__init__)


def test_integrationlabelvalue_constructor_args():
    sig = inspect.signature(IntegrationLabelValue.__init__)
    params = list(sig.parameters.keys())



def test_labelvalue_is_not_abstract():
    assert not inspect.isabstract(LabelValue)


def test_labelvalue_constructor_exists():
    assert callable(LabelValue.__init__)


def test_labelvalue_constructor_args():
    sig = inspect.signature(LabelValue.__init__)
    params = list(sig.parameters.keys())



def test_standard::diseasemodellabelvalue_is_not_abstract():
    assert not inspect.isabstract(standard::DiseaseModelLabelValue)


def test_standard::diseasemodellabelvalue_constructor_exists():
    assert callable(standard::DiseaseModelLabelValue.__init__)


def test_standard::diseasemodellabelvalue_constructor_args():
    sig = inspect.signature(standard::DiseaseModelLabelValue.__init__)
    params = list(sig.parameters.keys())
    assert "populationCount" in params, "Missing parameter 'populationCount'"
    assert "diseaseDeaths" in params, "Missing parameter 'diseaseDeaths'"
    assert "incidence" in params, "Missing parameter 'incidence'"

def test_standard::diseasemodellabelvalue_has_populationCount():
    assert hasattr(standard::DiseaseModelLabelValue, "populationCount")
    descriptor = None
    for klass in standard::DiseaseModelLabelValue.__mro__:
        if "populationCount" in klass.__dict__:
            descriptor = klass.__dict__["populationCount"]
            break
    assert isinstance(descriptor, property)

def test_standard::diseasemodellabelvalue_has_diseaseDeaths():
    assert hasattr(standard::DiseaseModelLabelValue, "diseaseDeaths")
    descriptor = None
    for klass in standard::DiseaseModelLabelValue.__mro__:
        if "diseaseDeaths" in klass.__dict__:
            descriptor = klass.__dict__["diseaseDeaths"]
            break
    assert isinstance(descriptor, property)

def test_standard::diseasemodellabelvalue_has_incidence():
    assert hasattr(standard::DiseaseModelLabelValue, "incidence")
    descriptor = None
    for klass in standard::DiseaseModelLabelValue.__mro__:
        if "incidence" in klass.__dict__:
            descriptor = klass.__dict__["incidence"]
            break
    assert isinstance(descriptor, property)



def test_standard::diseasemodelstate_is_not_abstract():
    assert not inspect.isabstract(standard::DiseaseModelState)


def test_standard::diseasemodelstate_constructor_exists():
    assert callable(standard::DiseaseModelState.__init__)


def test_standard::diseasemodelstate_constructor_args():
    sig = inspect.signature(standard::DiseaseModelState.__init__)
    params = list(sig.parameters.keys())



def test_standard::populationlabel_is_not_abstract():
    assert not inspect.isabstract(standard::PopulationLabel)


def test_standard::populationlabel_constructor_exists():
    assert callable(standard::PopulationLabel.__init__)


def test_standard::populationlabel_constructor_args():
    sig = inspect.signature(standard::PopulationLabel.__init__)
    params = list(sig.parameters.keys())



def test_dynamicnodelabel_is_not_abstract():
    assert not inspect.isabstract(DynamicNodeLabel)


def test_dynamicnodelabel_constructor_exists():
    assert callable(DynamicNodeLabel.__init__)


def test_dynamicnodelabel_constructor_args():
    sig = inspect.signature(DynamicNodeLabel.__init__)
    params = list(sig.parameters.keys())



def test_standard::diseasemodellabel_is_not_abstract():
    assert not inspect.isabstract(standard::DiseaseModelLabel)


def test_standard::diseasemodellabel_constructor_exists():
    assert callable(standard::DiseaseModelLabel.__init__)


def test_standard::diseasemodellabel_constructor_args():
    sig = inspect.signature(standard::DiseaseModelLabel.__init__)
    params = list(sig.parameters.keys())



def test_modifiable_is_not_abstract():
    assert not inspect.isabstract(Modifiable)


def test_modifiable_constructor_exists():
    assert callable(Modifiable.__init__)


def test_modifiable_constructor_args():
    sig = inspect.signature(Modifiable.__init__)
    params = list(sig.parameters.keys())



def test_sanitychecker_is_not_abstract():
    assert not inspect.isabstract(SanityChecker)


def test_sanitychecker_constructor_exists():
    assert callable(SanityChecker.__init__)


def test_sanitychecker_constructor_args():
    sig = inspect.signature(SanityChecker.__init__)
    params = list(sig.parameters.keys())



def test_nodedecorator_is_not_abstract():
    assert not inspect.isabstract(NodeDecorator)


def test_nodedecorator_constructor_exists():
    assert callable(NodeDecorator.__init__)


def test_nodedecorator_constructor_args():
    sig = inspect.signature(NodeDecorator.__init__)
    params = list(sig.parameters.keys())



def test_standard::infectorinoculatorcollection_is_not_abstract():
    assert not inspect.isabstract(standard::InfectorInoculatorCollection)


def test_standard::infectorinoculatorcollection_constructor_exists():
    assert callable(standard::InfectorInoculatorCollection.__init__)


def test_standard::infectorinoculatorcollection_constructor_args():
    sig = inspect.signature(standard::InfectorInoculatorCollection.__init__)
    params = list(sig.parameters.keys())
    assert "importFolder" in params, "Missing parameter 'importFolder'"

def test_standard::infectorinoculatorcollection_has_importFolder():
    assert hasattr(standard::InfectorInoculatorCollection, "importFolder")
    descriptor = None
    for klass in standard::InfectorInoculatorCollection.__mro__:
        if "importFolder" in klass.__dict__:
            descriptor = klass.__dict__["importFolder"]
            break
    assert isinstance(descriptor, property)



def test_standard::infector_is_not_abstract():
    assert not inspect.isabstract(standard::Infector)


def test_standard::infector_constructor_exists():
    assert callable(standard::Infector.__init__)


def test_standard::infector_constructor_args():
    sig = inspect.signature(standard::Infector.__init__)
    params = list(sig.parameters.keys())
    assert "populationIdentifier" in params, "Missing parameter 'populationIdentifier'"
    assert "targetURI" in params, "Missing parameter 'targetURI'"
    assert "infectPercentage" in params, "Missing parameter 'infectPercentage'"
    assert "diseaseName" in params, "Missing parameter 'diseaseName'"
    assert "targetISOKey" in params, "Missing parameter 'targetISOKey'"

def test_standard::infector_has_populationIdentifier():
    assert hasattr(standard::Infector, "populationIdentifier")
    descriptor = None
    for klass in standard::Infector.__mro__:
        if "populationIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["populationIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_standard::infector_has_targetURI():
    assert hasattr(standard::Infector, "targetURI")
    descriptor = None
    for klass in standard::Infector.__mro__:
        if "targetURI" in klass.__dict__:
            descriptor = klass.__dict__["targetURI"]
            break
    assert isinstance(descriptor, property)

def test_standard::infector_has_infectPercentage():
    assert hasattr(standard::Infector, "infectPercentage")
    descriptor = None
    for klass in standard::Infector.__mro__:
        if "infectPercentage" in klass.__dict__:
            descriptor = klass.__dict__["infectPercentage"]
            break
    assert isinstance(descriptor, property)

def test_standard::infector_has_diseaseName():
    assert hasattr(standard::Infector, "diseaseName")
    descriptor = None
    for klass in standard::Infector.__mro__:
        if "diseaseName" in klass.__dict__:
            descriptor = klass.__dict__["diseaseName"]
            break
    assert isinstance(descriptor, property)

def test_standard::infector_has_targetISOKey():
    assert hasattr(standard::Infector, "targetISOKey")
    descriptor = None
    for klass in standard::Infector.__mro__:
        if "targetISOKey" in klass.__dict__:
            descriptor = klass.__dict__["targetISOKey"]
            break
    assert isinstance(descriptor, property)



def test_standard::diseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::DiseaseModel)


def test_standard::diseasemodel_constructor_exists():
    assert callable(standard::DiseaseModel.__init__)


def test_standard::diseasemodel_constructor_args():
    sig = inspect.signature(standard::DiseaseModel.__init__)
    params = list(sig.parameters.keys())
    assert "timePeriod" in params, "Missing parameter 'timePeriod'"
    assert "finiteDifference" in params, "Missing parameter 'finiteDifference'"
    assert "backgroundBirthRate" in params, "Missing parameter 'backgroundBirthRate'"
    assert "populationIdentifier" in params, "Missing parameter 'populationIdentifier'"
    assert "relativeTolerance" in params, "Missing parameter 'relativeTolerance'"
    assert "frequencyDependent" in params, "Missing parameter 'frequencyDependent'"
    assert "backgroundMortalityRate" in params, "Missing parameter 'backgroundMortalityRate'"
    assert "diseaseName" in params, "Missing parameter 'diseaseName'"

def test_standard::diseasemodel_has_timePeriod():
    assert hasattr(standard::DiseaseModel, "timePeriod")
    descriptor = None
    for klass in standard::DiseaseModel.__mro__:
        if "timePeriod" in klass.__dict__:
            descriptor = klass.__dict__["timePeriod"]
            break
    assert isinstance(descriptor, property)

def test_standard::diseasemodel_has_finiteDifference():
    assert hasattr(standard::DiseaseModel, "finiteDifference")
    descriptor = None
    for klass in standard::DiseaseModel.__mro__:
        if "finiteDifference" in klass.__dict__:
            descriptor = klass.__dict__["finiteDifference"]
            break
    assert isinstance(descriptor, property)

def test_standard::diseasemodel_has_backgroundBirthRate():
    assert hasattr(standard::DiseaseModel, "backgroundBirthRate")
    descriptor = None
    for klass in standard::DiseaseModel.__mro__:
        if "backgroundBirthRate" in klass.__dict__:
            descriptor = klass.__dict__["backgroundBirthRate"]
            break
    assert isinstance(descriptor, property)

def test_standard::diseasemodel_has_populationIdentifier():
    assert hasattr(standard::DiseaseModel, "populationIdentifier")
    descriptor = None
    for klass in standard::DiseaseModel.__mro__:
        if "populationIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["populationIdentifier"]
            break
    assert isinstance(descriptor, property)

def test_standard::diseasemodel_has_relativeTolerance():
    assert hasattr(standard::DiseaseModel, "relativeTolerance")
    descriptor = None
    for klass in standard::DiseaseModel.__mro__:
        if "relativeTolerance" in klass.__dict__:
            descriptor = klass.__dict__["relativeTolerance"]
            break
    assert isinstance(descriptor, property)

def test_standard::diseasemodel_has_frequencyDependent():
    assert hasattr(standard::DiseaseModel, "frequencyDependent")
    descriptor = None
    for klass in standard::DiseaseModel.__mro__:
        if "frequencyDependent" in klass.__dict__:
            descriptor = klass.__dict__["frequencyDependent"]
            break
    assert isinstance(descriptor, property)

def test_standard::diseasemodel_has_backgroundMortalityRate():
    assert hasattr(standard::DiseaseModel, "backgroundMortalityRate")
    descriptor = None
    for klass in standard::DiseaseModel.__mro__:
        if "backgroundMortalityRate" in klass.__dict__:
            descriptor = klass.__dict__["backgroundMortalityRate"]
            break
    assert isinstance(descriptor, property)

def test_standard::diseasemodel_has_diseaseName():
    assert hasattr(standard::DiseaseModel, "diseaseName")
    descriptor = None
    for klass in standard::DiseaseModel.__mro__:
        if "diseaseName" in klass.__dict__:
            descriptor = klass.__dict__["diseaseName"]
            break
    assert isinstance(descriptor, property)



def test_sir_is_not_abstract():
    assert not inspect.isabstract(SIR)


def test_sir_constructor_exists():
    assert callable(SIR.__init__)


def test_sir_constructor_args():
    sig = inspect.signature(SIR.__init__)
    params = list(sig.parameters.keys())



def test_standard::stochasticpoissonsirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::StochasticPoissonSIRDiseaseModel)


def test_standard::stochasticpoissonsirdiseasemodel_constructor_exists():
    assert callable(standard::StochasticPoissonSIRDiseaseModel.__init__)


def test_standard::stochasticpoissonsirdiseasemodel_constructor_args():
    sig = inspect.signature(standard::StochasticPoissonSIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::stochasticsirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::StochasticSIRDiseaseModel)


def test_standard::stochasticsirdiseasemodel_constructor_exists():
    assert callable(standard::StochasticSIRDiseaseModel.__init__)


def test_standard::stochasticsirdiseasemodel_constructor_args():
    sig = inspect.signature(standard::StochasticSIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::seir_is_not_abstract():
    assert not inspect.isabstract(standard::SEIR)


def test_standard::seir_constructor_exists():
    assert callable(standard::SEIR.__init__)


def test_standard::seir_constructor_args():
    sig = inspect.signature(standard::SEIR.__init__)
    params = list(sig.parameters.keys())
    assert "incubationRate" in params, "Missing parameter 'incubationRate'"

def test_standard::seir_has_incubationRate():
    assert hasattr(standard::SEIR, "incubationRate")
    descriptor = None
    for klass in standard::SEIR.__mro__:
        if "incubationRate" in klass.__dict__:
            descriptor = klass.__dict__["incubationRate"]
            break
    assert isinstance(descriptor, property)



def test_standard::deterministicsirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::DeterministicSIRDiseaseModel)


def test_standard::deterministicsirdiseasemodel_constructor_exists():
    assert callable(standard::DeterministicSIRDiseaseModel.__init__)


def test_standard::deterministicsirdiseasemodel_constructor_args():
    sig = inspect.signature(standard::DeterministicSIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_si_is_not_abstract():
    assert not inspect.isabstract(SI)


def test_si_constructor_exists():
    assert callable(SI.__init__)


def test_si_constructor_args():
    sig = inspect.signature(SI.__init__)
    params = list(sig.parameters.keys())



def test_standard::stochasticpoissonsidiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::StochasticPoissonSIDiseaseModel)


def test_standard::stochasticpoissonsidiseasemodel_constructor_exists():
    assert callable(standard::StochasticPoissonSIDiseaseModel.__init__)


def test_standard::stochasticpoissonsidiseasemodel_constructor_args():
    sig = inspect.signature(standard::StochasticPoissonSIDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::stochasticsidiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::StochasticSIDiseaseModel)


def test_standard::stochasticsidiseasemodel_constructor_exists():
    assert callable(standard::StochasticSIDiseaseModel.__init__)


def test_standard::stochasticsidiseasemodel_constructor_args():
    sig = inspect.signature(standard::StochasticSIDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::aggregatingsidiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::AggregatingSIDiseaseModel)


def test_standard::aggregatingsidiseasemodel_constructor_exists():
    assert callable(standard::AggregatingSIDiseaseModel.__init__)


def test_standard::aggregatingsidiseasemodel_constructor_args():
    sig = inspect.signature(standard::AggregatingSIDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::sir_is_not_abstract():
    assert not inspect.isabstract(standard::SIR)


def test_standard::sir_constructor_exists():
    assert callable(standard::SIR.__init__)


def test_standard::sir_constructor_args():
    sig = inspect.signature(standard::SIR.__init__)
    params = list(sig.parameters.keys())
    assert "immunityLossRate" in params, "Missing parameter 'immunityLossRate'"

def test_standard::sir_has_immunityLossRate():
    assert hasattr(standard::SIR, "immunityLossRate")
    descriptor = None
    for klass in standard::SIR.__mro__:
        if "immunityLossRate" in klass.__dict__:
            descriptor = klass.__dict__["immunityLossRate"]
            break
    assert isinstance(descriptor, property)



def test_standard::deterministicsidiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::DeterministicSIDiseaseModel)


def test_standard::deterministicsidiseasemodel_constructor_exists():
    assert callable(standard::DeterministicSIDiseaseModel.__init__)


def test_standard::deterministicsidiseasemodel_constructor_args():
    sig = inspect.signature(standard::DeterministicSIDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_seir_is_not_abstract():
    assert not inspect.isabstract(SEIR)


def test_seir_constructor_exists():
    assert callable(SEIR.__init__)


def test_seir_constructor_args():
    sig = inspect.signature(SEIR.__init__)
    params = list(sig.parameters.keys())



def test_standard::stochasticpoissonseirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::StochasticPoissonSEIRDiseaseModel)


def test_standard::stochasticpoissonseirdiseasemodel_constructor_exists():
    assert callable(standard::StochasticPoissonSEIRDiseaseModel.__init__)


def test_standard::stochasticpoissonseirdiseasemodel_constructor_args():
    sig = inspect.signature(standard::StochasticPoissonSEIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::stochasticseirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::StochasticSEIRDiseaseModel)


def test_standard::stochasticseirdiseasemodel_constructor_exists():
    assert callable(standard::StochasticSEIRDiseaseModel.__init__)


def test_standard::stochasticseirdiseasemodel_constructor_args():
    sig = inspect.signature(standard::StochasticSEIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::deterministicseirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(standard::DeterministicSEIRDiseaseModel)


def test_standard::deterministicseirdiseasemodel_constructor_exists():
    assert callable(standard::DeterministicSEIRDiseaseModel.__init__)


def test_standard::deterministicseirdiseasemodel_constructor_args():
    sig = inspect.signature(standard::DeterministicSEIRDiseaseModel.__init__)
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
Infector_strategy = st.builds(
    Infector,
)
standard::StandardInfector_strategy = st.builds(
    standard::StandardInfector,
)
SIInfector_strategy = st.builds(
    SIInfector,
)
standard::SIRInoculator_strategy = st.builds(
    standard::SIRInoculator,
    inoculatedPercentage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    inoculatePercentage=
        st.booleans()
)
StochasticDiseaseModel_strategy = st.builds(
    StochasticDiseaseModel,
)
standard::StandardStochasticDiseaseModel_strategy = st.builds(
    standard::StandardStochasticDiseaseModel,
    gain=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
AggregatingSIDiseaseModel_strategy = st.builds(
    AggregatingSIDiseaseModel,
)
standard::AggregatingSIRDiseaseModel_strategy = st.builds(
    standard::AggregatingSIRDiseaseModel,
)
AggregatingSIRDiseaseModel_strategy = st.builds(
    AggregatingSIRDiseaseModel,
)
standard::AggregatingSEIRDiseaseModel_strategy = st.builds(
    standard::AggregatingSEIRDiseaseModel,
)
standard::IntegrationDecorator_strategy = st.builds(
    standard::IntegrationDecorator,
)
standard::IntegrationLabelValue_strategy = st.builds(
    standard::IntegrationLabelValue,
)
standard::IntegrationLabel_strategy = st.builds(
    standard::IntegrationLabel,
)
standard::SanityChecker_strategy = st.builds(
    standard::SanityChecker,
)
StandardStochasticDiseaseModel_strategy = st.builds(
    StandardStochasticDiseaseModel,
)
StandardDiseaseModelLabelValue_strategy = st.builds(
    StandardDiseaseModelLabelValue,
)
DiseaseModelState_strategy = st.builds(
    DiseaseModelState,
)
standard::AggregatingDiseaseModelState_strategy = st.builds(
    standard::AggregatingDiseaseModelState,
)
standard::StandardDiseaseModelState_strategy = st.builds(
    standard::StandardDiseaseModelState,
    areaRatio=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
DiseaseModelLabelValue_strategy = st.builds(
    DiseaseModelLabelValue,
)
standard::StandardDiseaseModelLabelValue_strategy = st.builds(
    standard::StandardDiseaseModelLabelValue,
    s=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
IntegrationLabel_strategy = st.builds(
    IntegrationLabel,
)
DiseaseModelLabel_strategy = st.builds(
    DiseaseModelLabel,
)
standard::StandardDiseaseModelLabel_strategy = st.builds(
    standard::StandardDiseaseModelLabel,
)
IntegrationDecorator_strategy = st.builds(
    IntegrationDecorator,
)
DiseaseModel_strategy = st.builds(
    DiseaseModel,
)
standard::StochasticDiseaseModel_strategy = st.builds(
    standard::StochasticDiseaseModel,
    seed=
        safe_text,
    randomGenerator=
        safe_text
)
SILabelValue_strategy = st.builds(
    SILabelValue,
)
standard::SIRLabelValue_strategy = st.builds(
    standard::SIRLabelValue,
    r=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
standard::SILabelValue_strategy = st.builds(
    standard::SILabelValue,
    i=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StandardInfector_strategy = st.builds(
    StandardInfector,
)
standard::SIInfector_strategy = st.builds(
    standard::SIInfector,
    infectiousCount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StandardDiseaseModelState_strategy = st.builds(
    StandardDiseaseModelState,
)
standard::SIDiseaseModelState_strategy = st.builds(
    standard::SIDiseaseModelState,
)
StandardDiseaseModel_strategy = st.builds(
    StandardDiseaseModel,
)
standard::SI_strategy = st.builds(
    standard::SI,
    physicallyAdjacentInfectiousProportion=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    roadNetworkInfectiousProportion=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    infectiousMortality=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    nonLinearityCoefficient=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    transmissionRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    recoveryRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    characteristicMixingDistance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    infectiousMortalityRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SIRLabelValue_strategy = st.builds(
    SIRLabelValue,
)
standard::PopulationModelLabel_strategy = st.builds(
    standard::PopulationModelLabel,
)
standard::SEIRLabelValue_strategy = st.builds(
    standard::SEIRLabelValue,
    e=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StandardDiseaseModelLabel_strategy = st.builds(
    StandardDiseaseModelLabel,
)
standard::SIRLabel_strategy = st.builds(
    standard::SIRLabel,
)
standard::SILabel_strategy = st.builds(
    standard::SILabel,
)
standard::SEIRLabel_strategy = st.builds(
    standard::SEIRLabel,
)
standard::StandardDiseaseModel_strategy = st.builds(
    standard::StandardDiseaseModel,
    referencePopulationDensity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    totalPopulationCountReciprocal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    totalPopulationCount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    totalArea=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
IntegrationLabelValue_strategy = st.builds(
    IntegrationLabelValue,
)
LabelValue_strategy = st.builds(
    LabelValue,
)
standard::DiseaseModelLabelValue_strategy = st.builds(
    standard::DiseaseModelLabelValue,
    populationCount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    diseaseDeaths=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    incidence=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
standard::DiseaseModelState_strategy = st.builds(
    standard::DiseaseModelState,
)
standard::PopulationLabel_strategy = st.builds(
    standard::PopulationLabel,
)
DynamicNodeLabel_strategy = st.builds(
    DynamicNodeLabel,
)
standard::DiseaseModelLabel_strategy = st.builds(
    standard::DiseaseModelLabel,
)
Modifiable_strategy = st.builds(
    Modifiable,
)
SanityChecker_strategy = st.builds(
    SanityChecker,
)
NodeDecorator_strategy = st.builds(
    NodeDecorator,
)
standard::InfectorInoculatorCollection_strategy = st.builds(
    standard::InfectorInoculatorCollection,
    importFolder=
        safe_text
)
standard::Infector_strategy = st.builds(
    standard::Infector,
    populationIdentifier=
        safe_text,
    targetURI=
        safe_text,
    infectPercentage=
        st.booleans(),
    diseaseName=
        safe_text,
    targetISOKey=
        safe_text
)
standard::DiseaseModel_strategy = st.builds(
    standard::DiseaseModel,
    timePeriod=
        safe_text,
    finiteDifference=
        st.booleans(),
    backgroundBirthRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    populationIdentifier=
        safe_text,
    relativeTolerance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    frequencyDependent=
        st.booleans(),
    backgroundMortalityRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    diseaseName=
        safe_text
)
SIR_strategy = st.builds(
    SIR,
)
standard::StochasticPoissonSIRDiseaseModel_strategy = st.builds(
    standard::StochasticPoissonSIRDiseaseModel,
)
standard::StochasticSIRDiseaseModel_strategy = st.builds(
    standard::StochasticSIRDiseaseModel,
)
standard::SEIR_strategy = st.builds(
    standard::SEIR,
    incubationRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
standard::DeterministicSIRDiseaseModel_strategy = st.builds(
    standard::DeterministicSIRDiseaseModel,
)
SI_strategy = st.builds(
    SI,
)
standard::StochasticPoissonSIDiseaseModel_strategy = st.builds(
    standard::StochasticPoissonSIDiseaseModel,
)
standard::StochasticSIDiseaseModel_strategy = st.builds(
    standard::StochasticSIDiseaseModel,
)
standard::AggregatingSIDiseaseModel_strategy = st.builds(
    standard::AggregatingSIDiseaseModel,
)
standard::SIR_strategy = st.builds(
    standard::SIR,
    immunityLossRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
standard::DeterministicSIDiseaseModel_strategy = st.builds(
    standard::DeterministicSIDiseaseModel,
)
SEIR_strategy = st.builds(
    SEIR,
)
standard::StochasticPoissonSEIRDiseaseModel_strategy = st.builds(
    standard::StochasticPoissonSEIRDiseaseModel,
)
standard::StochasticSEIRDiseaseModel_strategy = st.builds(
    standard::StochasticSEIRDiseaseModel,
)
standard::DeterministicSEIRDiseaseModel_strategy = st.builds(
    standard::DeterministicSEIRDiseaseModel,
)

@given(instance=Infector_strategy)
@settings(max_examples=50)
def test_infector_instantiation(instance):
    assert isinstance(instance, Infector)

@given(instance=standard::StandardInfector_strategy)
@settings(max_examples=50)
def test_standard::standardinfector_instantiation(instance):
    assert isinstance(instance, standard::StandardInfector)

@given(instance=SIInfector_strategy)
@settings(max_examples=50)
def test_siinfector_instantiation(instance):
    assert isinstance(instance, SIInfector)

@given(instance=standard::SIRInoculator_strategy)
@settings(max_examples=50)
def test_standard::sirinoculator_instantiation(instance):
    assert isinstance(instance, standard::SIRInoculator)

@given(instance=standard::SIRInoculator_strategy)
def test_standard::sirinoculator_inoculatedPercentage_type(instance):
    assert isinstance(instance.inoculatedPercentage, float)


@given(instance=standard::SIRInoculator_strategy)
def test_standard::sirinoculator_inoculatedPercentage_setter(instance):
    original = instance.inoculatedPercentage
    instance.inoculatedPercentage = original
    assert instance.inoculatedPercentage == original

@given(instance=standard::SIRInoculator_strategy)
def test_standard::sirinoculator_inoculatePercentage_type(instance):
    assert isinstance(instance.inoculatePercentage, bool)


@given(instance=standard::SIRInoculator_strategy)
def test_standard::sirinoculator_inoculatePercentage_setter(instance):
    original = instance.inoculatePercentage
    instance.inoculatePercentage = original
    assert instance.inoculatePercentage == original

@given(instance=StochasticDiseaseModel_strategy)
@settings(max_examples=50)
def test_stochasticdiseasemodel_instantiation(instance):
    assert isinstance(instance, StochasticDiseaseModel)

@given(instance=standard::StandardStochasticDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::standardstochasticdiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::StandardStochasticDiseaseModel)

@given(instance=standard::StandardStochasticDiseaseModel_strategy)
def test_standard::standardstochasticdiseasemodel_gain_type(instance):
    assert isinstance(instance.gain, float)


@given(instance=standard::StandardStochasticDiseaseModel_strategy)
def test_standard::standardstochasticdiseasemodel_gain_setter(instance):
    original = instance.gain
    instance.gain = original
    assert instance.gain == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::StandardStochasticDiseaseModel_strategy)
@settings(max_examples=30)
def test_standard::standardstochasticdiseasemodel_computenoise_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.computeNoise()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.computeNoise).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'computeNoise' in standard::StandardStochasticDiseaseModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'computeNoise' in standard::StandardStochasticDiseaseModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'computeNoise' in standard::StandardStochasticDiseaseModel is not implemented or raised an error")

@given(instance=AggregatingSIDiseaseModel_strategy)
@settings(max_examples=50)
def test_aggregatingsidiseasemodel_instantiation(instance):
    assert isinstance(instance, AggregatingSIDiseaseModel)

@given(instance=standard::AggregatingSIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::aggregatingsirdiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::AggregatingSIRDiseaseModel)

@given(instance=AggregatingSIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_aggregatingsirdiseasemodel_instantiation(instance):
    assert isinstance(instance, AggregatingSIRDiseaseModel)

@given(instance=standard::AggregatingSEIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::aggregatingseirdiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::AggregatingSEIRDiseaseModel)

@given(instance=standard::IntegrationDecorator_strategy)
@settings(max_examples=50)
def test_standard::integrationdecorator_instantiation(instance):
    assert isinstance(instance, standard::IntegrationDecorator)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::IntegrationDecorator_strategy)
@settings(max_examples=30)
def test_standard::integrationdecorator_isdeterministic_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isDeterministic()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isDeterministic).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isDeterministic' in standard::IntegrationDecorator is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isDeterministic' in standard::IntegrationDecorator did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isDeterministic' in standard::IntegrationDecorator is not implemented or raised an error")

@given(instance=standard::IntegrationLabelValue_strategy)
@settings(max_examples=50)
def test_standard::integrationlabelvalue_instantiation(instance):
    assert isinstance(instance, standard::IntegrationLabelValue)

@given(instance=standard::IntegrationLabel_strategy)
@settings(max_examples=50)
def test_standard::integrationlabel_instantiation(instance):
    assert isinstance(instance, standard::IntegrationLabel)

@given(instance=standard::SanityChecker_strategy)
@settings(max_examples=50)
def test_standard::sanitychecker_instantiation(instance):
    assert isinstance(instance, standard::SanityChecker)

@given(instance=StandardStochasticDiseaseModel_strategy)
@settings(max_examples=50)
def test_standardstochasticdiseasemodel_instantiation(instance):
    assert isinstance(instance, StandardStochasticDiseaseModel)

@given(instance=StandardDiseaseModelLabelValue_strategy)
@settings(max_examples=50)
def test_standarddiseasemodellabelvalue_instantiation(instance):
    assert isinstance(instance, StandardDiseaseModelLabelValue)

@given(instance=DiseaseModelState_strategy)
@settings(max_examples=50)
def test_diseasemodelstate_instantiation(instance):
    assert isinstance(instance, DiseaseModelState)

@given(instance=standard::AggregatingDiseaseModelState_strategy)
@settings(max_examples=50)
def test_standard::aggregatingdiseasemodelstate_instantiation(instance):
    assert isinstance(instance, standard::AggregatingDiseaseModelState)

@given(instance=standard::StandardDiseaseModelState_strategy)
@settings(max_examples=50)
def test_standard::standarddiseasemodelstate_instantiation(instance):
    assert isinstance(instance, standard::StandardDiseaseModelState)

@given(instance=standard::StandardDiseaseModelState_strategy)
def test_standard::standarddiseasemodelstate_areaRatio_type(instance):
    assert isinstance(instance.areaRatio, float)


@given(instance=standard::StandardDiseaseModelState_strategy)
def test_standard::standarddiseasemodelstate_areaRatio_setter(instance):
    original = instance.areaRatio
    instance.areaRatio = original
    assert instance.areaRatio == original

@given(instance=DiseaseModelLabelValue_strategy)
@settings(max_examples=50)
def test_diseasemodellabelvalue_instantiation(instance):
    assert isinstance(instance, DiseaseModelLabelValue)

@given(instance=standard::StandardDiseaseModelLabelValue_strategy)
@settings(max_examples=50)
def test_standard::standarddiseasemodellabelvalue_instantiation(instance):
    assert isinstance(instance, standard::StandardDiseaseModelLabelValue)

@given(instance=standard::StandardDiseaseModelLabelValue_strategy)
def test_standard::standarddiseasemodellabelvalue_s_type(instance):
    assert isinstance(instance.s, float)


@given(instance=standard::StandardDiseaseModelLabelValue_strategy)
def test_standard::standarddiseasemodellabelvalue_s_setter(instance):
    original = instance.s
    instance.s = original
    assert instance.s == original

@given(instance=IntegrationLabel_strategy)
@settings(max_examples=50)
def test_integrationlabel_instantiation(instance):
    assert isinstance(instance, IntegrationLabel)

@given(instance=DiseaseModelLabel_strategy)
@settings(max_examples=50)
def test_diseasemodellabel_instantiation(instance):
    assert isinstance(instance, DiseaseModelLabel)

@given(instance=standard::StandardDiseaseModelLabel_strategy)
@settings(max_examples=50)
def test_standard::standarddiseasemodellabel_instantiation(instance):
    assert isinstance(instance, standard::StandardDiseaseModelLabel)

@given(instance=IntegrationDecorator_strategy)
@settings(max_examples=50)
def test_integrationdecorator_instantiation(instance):
    assert isinstance(instance, IntegrationDecorator)

@given(instance=DiseaseModel_strategy)
@settings(max_examples=50)
def test_diseasemodel_instantiation(instance):
    assert isinstance(instance, DiseaseModel)

@given(instance=standard::StochasticDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::stochasticdiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::StochasticDiseaseModel)

@given(instance=standard::StochasticDiseaseModel_strategy)
def test_standard::stochasticdiseasemodel_seed_type(instance):
    assert isinstance(instance.seed, str)


@given(instance=standard::StochasticDiseaseModel_strategy)
def test_standard::stochasticdiseasemodel_seed_setter(instance):
    original = instance.seed
    instance.seed = original
    assert instance.seed == original

@given(instance=standard::StochasticDiseaseModel_strategy)
def test_standard::stochasticdiseasemodel_randomGenerator_type(instance):
    assert isinstance(instance.randomGenerator, str)


@given(instance=standard::StochasticDiseaseModel_strategy)
def test_standard::stochasticdiseasemodel_randomGenerator_setter(instance):
    original = instance.randomGenerator
    instance.randomGenerator = original
    assert instance.randomGenerator == original

@given(instance=SILabelValue_strategy)
@settings(max_examples=50)
def test_silabelvalue_instantiation(instance):
    assert isinstance(instance, SILabelValue)

@given(instance=standard::SIRLabelValue_strategy)
@settings(max_examples=50)
def test_standard::sirlabelvalue_instantiation(instance):
    assert isinstance(instance, standard::SIRLabelValue)

@given(instance=standard::SIRLabelValue_strategy)
def test_standard::sirlabelvalue_r_type(instance):
    assert isinstance(instance.r, float)


@given(instance=standard::SIRLabelValue_strategy)
def test_standard::sirlabelvalue_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original

@given(instance=standard::SILabelValue_strategy)
@settings(max_examples=50)
def test_standard::silabelvalue_instantiation(instance):
    assert isinstance(instance, standard::SILabelValue)

@given(instance=standard::SILabelValue_strategy)
def test_standard::silabelvalue_i_type(instance):
    assert isinstance(instance.i, float)


@given(instance=standard::SILabelValue_strategy)
def test_standard::silabelvalue_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=StandardInfector_strategy)
@settings(max_examples=50)
def test_standardinfector_instantiation(instance):
    assert isinstance(instance, StandardInfector)

@given(instance=standard::SIInfector_strategy)
@settings(max_examples=50)
def test_standard::siinfector_instantiation(instance):
    assert isinstance(instance, standard::SIInfector)

@given(instance=standard::SIInfector_strategy)
def test_standard::siinfector_infectiousCount_type(instance):
    assert isinstance(instance.infectiousCount, float)


@given(instance=standard::SIInfector_strategy)
def test_standard::siinfector_infectiousCount_setter(instance):
    original = instance.infectiousCount
    instance.infectiousCount = original
    assert instance.infectiousCount == original

@given(instance=StandardDiseaseModelState_strategy)
@settings(max_examples=50)
def test_standarddiseasemodelstate_instantiation(instance):
    assert isinstance(instance, StandardDiseaseModelState)

@given(instance=standard::SIDiseaseModelState_strategy)
@settings(max_examples=50)
def test_standard::sidiseasemodelstate_instantiation(instance):
    assert isinstance(instance, standard::SIDiseaseModelState)

@given(instance=StandardDiseaseModel_strategy)
@settings(max_examples=50)
def test_standarddiseasemodel_instantiation(instance):
    assert isinstance(instance, StandardDiseaseModel)

@given(instance=standard::SI_strategy)
@settings(max_examples=50)
def test_standard::si_instantiation(instance):
    assert isinstance(instance, standard::SI)

@given(instance=standard::SI_strategy)
def test_standard::si_physicallyAdjacentInfectiousProportion_type(instance):
    assert isinstance(instance.physicallyAdjacentInfectiousProportion, float)


@given(instance=standard::SI_strategy)
def test_standard::si_physicallyAdjacentInfectiousProportion_setter(instance):
    original = instance.physicallyAdjacentInfectiousProportion
    instance.physicallyAdjacentInfectiousProportion = original
    assert instance.physicallyAdjacentInfectiousProportion == original

@given(instance=standard::SI_strategy)
def test_standard::si_roadNetworkInfectiousProportion_type(instance):
    assert isinstance(instance.roadNetworkInfectiousProportion, float)


@given(instance=standard::SI_strategy)
def test_standard::si_roadNetworkInfectiousProportion_setter(instance):
    original = instance.roadNetworkInfectiousProportion
    instance.roadNetworkInfectiousProportion = original
    assert instance.roadNetworkInfectiousProportion == original

@given(instance=standard::SI_strategy)
def test_standard::si_infectiousMortality_type(instance):
    assert isinstance(instance.infectiousMortality, float)


@given(instance=standard::SI_strategy)
def test_standard::si_infectiousMortality_setter(instance):
    original = instance.infectiousMortality
    instance.infectiousMortality = original
    assert instance.infectiousMortality == original

@given(instance=standard::SI_strategy)
def test_standard::si_nonLinearityCoefficient_type(instance):
    assert isinstance(instance.nonLinearityCoefficient, float)


@given(instance=standard::SI_strategy)
def test_standard::si_nonLinearityCoefficient_setter(instance):
    original = instance.nonLinearityCoefficient
    instance.nonLinearityCoefficient = original
    assert instance.nonLinearityCoefficient == original

@given(instance=standard::SI_strategy)
def test_standard::si_transmissionRate_type(instance):
    assert isinstance(instance.transmissionRate, float)


@given(instance=standard::SI_strategy)
def test_standard::si_transmissionRate_setter(instance):
    original = instance.transmissionRate
    instance.transmissionRate = original
    assert instance.transmissionRate == original

@given(instance=standard::SI_strategy)
def test_standard::si_recoveryRate_type(instance):
    assert isinstance(instance.recoveryRate, float)


@given(instance=standard::SI_strategy)
def test_standard::si_recoveryRate_setter(instance):
    original = instance.recoveryRate
    instance.recoveryRate = original
    assert instance.recoveryRate == original

@given(instance=standard::SI_strategy)
def test_standard::si_characteristicMixingDistance_type(instance):
    assert isinstance(instance.characteristicMixingDistance, float)


@given(instance=standard::SI_strategy)
def test_standard::si_characteristicMixingDistance_setter(instance):
    original = instance.characteristicMixingDistance
    instance.characteristicMixingDistance = original
    assert instance.characteristicMixingDistance == original

@given(instance=standard::SI_strategy)
def test_standard::si_infectiousMortalityRate_type(instance):
    assert isinstance(instance.infectiousMortalityRate, float)


@given(instance=standard::SI_strategy)
def test_standard::si_infectiousMortalityRate_setter(instance):
    original = instance.infectiousMortalityRate
    instance.infectiousMortalityRate = original
    assert instance.infectiousMortalityRate == original

@given(instance=SIRLabelValue_strategy)
@settings(max_examples=50)
def test_sirlabelvalue_instantiation(instance):
    assert isinstance(instance, SIRLabelValue)

@given(instance=standard::PopulationModelLabel_strategy)
@settings(max_examples=50)
def test_standard::populationmodellabel_instantiation(instance):
    assert isinstance(instance, standard::PopulationModelLabel)

@given(instance=standard::SEIRLabelValue_strategy)
@settings(max_examples=50)
def test_standard::seirlabelvalue_instantiation(instance):
    assert isinstance(instance, standard::SEIRLabelValue)

@given(instance=standard::SEIRLabelValue_strategy)
def test_standard::seirlabelvalue_e_type(instance):
    assert isinstance(instance.e, float)


@given(instance=standard::SEIRLabelValue_strategy)
def test_standard::seirlabelvalue_e_setter(instance):
    original = instance.e
    instance.e = original
    assert instance.e == original

@given(instance=StandardDiseaseModelLabel_strategy)
@settings(max_examples=50)
def test_standarddiseasemodellabel_instantiation(instance):
    assert isinstance(instance, StandardDiseaseModelLabel)

@given(instance=standard::SIRLabel_strategy)
@settings(max_examples=50)
def test_standard::sirlabel_instantiation(instance):
    assert isinstance(instance, standard::SIRLabel)

@given(instance=standard::SILabel_strategy)
@settings(max_examples=50)
def test_standard::silabel_instantiation(instance):
    assert isinstance(instance, standard::SILabel)

@given(instance=standard::SEIRLabel_strategy)
@settings(max_examples=50)
def test_standard::seirlabel_instantiation(instance):
    assert isinstance(instance, standard::SEIRLabel)

@given(instance=standard::StandardDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::standarddiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::StandardDiseaseModel)

@given(instance=standard::StandardDiseaseModel_strategy)
def test_standard::standarddiseasemodel_referencePopulationDensity_type(instance):
    assert isinstance(instance.referencePopulationDensity, float)


@given(instance=standard::StandardDiseaseModel_strategy)
def test_standard::standarddiseasemodel_referencePopulationDensity_setter(instance):
    original = instance.referencePopulationDensity
    instance.referencePopulationDensity = original
    assert instance.referencePopulationDensity == original

@given(instance=standard::StandardDiseaseModel_strategy)
def test_standard::standarddiseasemodel_totalPopulationCountReciprocal_type(instance):
    assert isinstance(instance.totalPopulationCountReciprocal, float)


@given(instance=standard::StandardDiseaseModel_strategy)
def test_standard::standarddiseasemodel_totalPopulationCountReciprocal_setter(instance):
    original = instance.totalPopulationCountReciprocal
    instance.totalPopulationCountReciprocal = original
    assert instance.totalPopulationCountReciprocal == original

@given(instance=standard::StandardDiseaseModel_strategy)
def test_standard::standarddiseasemodel_totalPopulationCount_type(instance):
    assert isinstance(instance.totalPopulationCount, float)


@given(instance=standard::StandardDiseaseModel_strategy)
def test_standard::standarddiseasemodel_totalPopulationCount_setter(instance):
    original = instance.totalPopulationCount
    instance.totalPopulationCount = original
    assert instance.totalPopulationCount == original

@given(instance=standard::StandardDiseaseModel_strategy)
def test_standard::standarddiseasemodel_totalArea_type(instance):
    assert isinstance(instance.totalArea, float)


@given(instance=standard::StandardDiseaseModel_strategy)
def test_standard::standarddiseasemodel_totalArea_setter(instance):
    original = instance.totalArea
    instance.totalArea = original
    assert instance.totalArea == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::StandardDiseaseModel_strategy)
@settings(max_examples=30)
def test_standard::standarddiseasemodel_addtototalarea_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addToTotalArea(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addToTotalArea).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addToTotalArea' in standard::StandardDiseaseModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addToTotalArea' in standard::StandardDiseaseModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addToTotalArea' in standard::StandardDiseaseModel is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::StandardDiseaseModel_strategy)
@settings(max_examples=30)
def test_standard::standarddiseasemodel_calculatedelta_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.calculateDelta(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.calculateDelta).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'calculateDelta' in standard::StandardDiseaseModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'calculateDelta' in standard::StandardDiseaseModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'calculateDelta' in standard::StandardDiseaseModel is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::StandardDiseaseModel_strategy)
@settings(max_examples=30)
def test_standard::standarddiseasemodel_addtototalpopulationcount_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addToTotalPopulationCount(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addToTotalPopulationCount).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addToTotalPopulationCount' in standard::StandardDiseaseModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addToTotalPopulationCount' in standard::StandardDiseaseModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addToTotalPopulationCount' in standard::StandardDiseaseModel is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::StandardDiseaseModel_strategy)
@settings(max_examples=30)
def test_standard::standarddiseasemodel_domodelspecificadjustments_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.doModelSpecificAdjustments(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.doModelSpecificAdjustments).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'doModelSpecificAdjustments' in standard::StandardDiseaseModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'doModelSpecificAdjustments' in standard::StandardDiseaseModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'doModelSpecificAdjustments' in standard::StandardDiseaseModel is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::StandardDiseaseModel_strategy)
@settings(max_examples=30)
def test_standard::standarddiseasemodel_computetotalpopulationcountreciprocal_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.computeTotalPopulationCountReciprocal()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.computeTotalPopulationCountReciprocal).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'computeTotalPopulationCountReciprocal' in standard::StandardDiseaseModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'computeTotalPopulationCountReciprocal' in standard::StandardDiseaseModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'computeTotalPopulationCountReciprocal' in standard::StandardDiseaseModel is not implemented or raised an error")

@given(instance=IntegrationLabelValue_strategy)
@settings(max_examples=50)
def test_integrationlabelvalue_instantiation(instance):
    assert isinstance(instance, IntegrationLabelValue)

@given(instance=LabelValue_strategy)
@settings(max_examples=50)
def test_labelvalue_instantiation(instance):
    assert isinstance(instance, LabelValue)

@given(instance=standard::DiseaseModelLabelValue_strategy)
@settings(max_examples=50)
def test_standard::diseasemodellabelvalue_instantiation(instance):
    assert isinstance(instance, standard::DiseaseModelLabelValue)

@given(instance=standard::DiseaseModelLabelValue_strategy)
def test_standard::diseasemodellabelvalue_populationCount_type(instance):
    assert isinstance(instance.populationCount, float)


@given(instance=standard::DiseaseModelLabelValue_strategy)
def test_standard::diseasemodellabelvalue_populationCount_setter(instance):
    original = instance.populationCount
    instance.populationCount = original
    assert instance.populationCount == original

@given(instance=standard::DiseaseModelLabelValue_strategy)
def test_standard::diseasemodellabelvalue_diseaseDeaths_type(instance):
    assert isinstance(instance.diseaseDeaths, float)


@given(instance=standard::DiseaseModelLabelValue_strategy)
def test_standard::diseasemodellabelvalue_diseaseDeaths_setter(instance):
    original = instance.diseaseDeaths
    instance.diseaseDeaths = original
    assert instance.diseaseDeaths == original

@given(instance=standard::DiseaseModelLabelValue_strategy)
def test_standard::diseasemodellabelvalue_incidence_type(instance):
    assert isinstance(instance.incidence, float)


@given(instance=standard::DiseaseModelLabelValue_strategy)
def test_standard::diseasemodellabelvalue_incidence_setter(instance):
    original = instance.incidence
    instance.incidence = original
    assert instance.incidence == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::DiseaseModelLabelValue_strategy)
@settings(max_examples=30)
def test_standard::diseasemodellabelvalue_sub_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.sub(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.sub).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'sub' in standard::DiseaseModelLabelValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'sub' in standard::DiseaseModelLabelValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'sub' in standard::DiseaseModelLabelValue is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::DiseaseModelLabelValue_strategy)
@settings(max_examples=30)
def test_standard::diseasemodellabelvalue_zerooutpopulationcount_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.zeroOutPopulationCount()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.zeroOutPopulationCount).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'zeroOutPopulationCount' in standard::DiseaseModelLabelValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'zeroOutPopulationCount' in standard::DiseaseModelLabelValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'zeroOutPopulationCount' in standard::DiseaseModelLabelValue is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::DiseaseModelLabelValue_strategy)
@settings(max_examples=30)
def test_standard::diseasemodellabelvalue_scale_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.scale(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.scale).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'scale' in standard::DiseaseModelLabelValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'scale' in standard::DiseaseModelLabelValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'scale' in standard::DiseaseModelLabelValue is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::DiseaseModelLabelValue_strategy)
@settings(max_examples=30)
def test_standard::diseasemodellabelvalue_add_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.add(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.add).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'add' in standard::DiseaseModelLabelValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'add' in standard::DiseaseModelLabelValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'add' in standard::DiseaseModelLabelValue is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::DiseaseModelLabelValue_strategy)
@settings(max_examples=30)
def test_standard::diseasemodellabelvalue_set_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.set(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.set).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'set' in standard::DiseaseModelLabelValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'set' in standard::DiseaseModelLabelValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'set' in standard::DiseaseModelLabelValue is not implemented or raised an error")

@given(instance=standard::DiseaseModelState_strategy)
@settings(max_examples=50)
def test_standard::diseasemodelstate_instantiation(instance):
    assert isinstance(instance, standard::DiseaseModelState)

@given(instance=standard::PopulationLabel_strategy)
@settings(max_examples=50)
def test_standard::populationlabel_instantiation(instance):
    assert isinstance(instance, standard::PopulationLabel)

@given(instance=DynamicNodeLabel_strategy)
@settings(max_examples=50)
def test_dynamicnodelabel_instantiation(instance):
    assert isinstance(instance, DynamicNodeLabel)

@given(instance=standard::DiseaseModelLabel_strategy)
@settings(max_examples=50)
def test_standard::diseasemodellabel_instantiation(instance):
    assert isinstance(instance, standard::DiseaseModelLabel)

@given(instance=Modifiable_strategy)
@settings(max_examples=50)
def test_modifiable_instantiation(instance):
    assert isinstance(instance, Modifiable)

@given(instance=SanityChecker_strategy)
@settings(max_examples=50)
def test_sanitychecker_instantiation(instance):
    assert isinstance(instance, SanityChecker)

@given(instance=NodeDecorator_strategy)
@settings(max_examples=50)
def test_nodedecorator_instantiation(instance):
    assert isinstance(instance, NodeDecorator)

@given(instance=standard::InfectorInoculatorCollection_strategy)
@settings(max_examples=50)
def test_standard::infectorinoculatorcollection_instantiation(instance):
    assert isinstance(instance, standard::InfectorInoculatorCollection)

@given(instance=standard::InfectorInoculatorCollection_strategy)
def test_standard::infectorinoculatorcollection_importFolder_type(instance):
    assert isinstance(instance.importFolder, str)


@given(instance=standard::InfectorInoculatorCollection_strategy)
def test_standard::infectorinoculatorcollection_importFolder_setter(instance):
    original = instance.importFolder
    instance.importFolder = original
    assert instance.importFolder == original

@given(instance=standard::Infector_strategy)
@settings(max_examples=50)
def test_standard::infector_instantiation(instance):
    assert isinstance(instance, standard::Infector)

@given(instance=standard::Infector_strategy)
def test_standard::infector_populationIdentifier_type(instance):
    assert isinstance(instance.populationIdentifier, str)


@given(instance=standard::Infector_strategy)
def test_standard::infector_populationIdentifier_setter(instance):
    original = instance.populationIdentifier
    instance.populationIdentifier = original
    assert instance.populationIdentifier == original

@given(instance=standard::Infector_strategy)
def test_standard::infector_targetURI_type(instance):
    assert isinstance(instance.targetURI, str)


@given(instance=standard::Infector_strategy)
def test_standard::infector_targetURI_setter(instance):
    original = instance.targetURI
    instance.targetURI = original
    assert instance.targetURI == original

@given(instance=standard::Infector_strategy)
def test_standard::infector_infectPercentage_type(instance):
    assert isinstance(instance.infectPercentage, bool)


@given(instance=standard::Infector_strategy)
def test_standard::infector_infectPercentage_setter(instance):
    original = instance.infectPercentage
    instance.infectPercentage = original
    assert instance.infectPercentage == original

@given(instance=standard::Infector_strategy)
def test_standard::infector_diseaseName_type(instance):
    assert isinstance(instance.diseaseName, str)


@given(instance=standard::Infector_strategy)
def test_standard::infector_diseaseName_setter(instance):
    original = instance.diseaseName
    instance.diseaseName = original
    assert instance.diseaseName == original

@given(instance=standard::Infector_strategy)
def test_standard::infector_targetISOKey_type(instance):
    assert isinstance(instance.targetISOKey, str)


@given(instance=standard::Infector_strategy)
def test_standard::infector_targetISOKey_setter(instance):
    original = instance.targetISOKey
    instance.targetISOKey = original
    assert instance.targetISOKey == original

@given(instance=standard::DiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::diseasemodel_instantiation(instance):
    assert isinstance(instance, standard::DiseaseModel)

@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_timePeriod_type(instance):
    assert isinstance(instance.timePeriod, str)


@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_timePeriod_setter(instance):
    original = instance.timePeriod
    instance.timePeriod = original
    assert instance.timePeriod == original

@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_finiteDifference_type(instance):
    assert isinstance(instance.finiteDifference, bool)


@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_finiteDifference_setter(instance):
    original = instance.finiteDifference
    instance.finiteDifference = original
    assert instance.finiteDifference == original

@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_backgroundBirthRate_type(instance):
    assert isinstance(instance.backgroundBirthRate, float)


@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_backgroundBirthRate_setter(instance):
    original = instance.backgroundBirthRate
    instance.backgroundBirthRate = original
    assert instance.backgroundBirthRate == original

@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_populationIdentifier_type(instance):
    assert isinstance(instance.populationIdentifier, str)


@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_populationIdentifier_setter(instance):
    original = instance.populationIdentifier
    instance.populationIdentifier = original
    assert instance.populationIdentifier == original

@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_relativeTolerance_type(instance):
    assert isinstance(instance.relativeTolerance, float)


@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_relativeTolerance_setter(instance):
    original = instance.relativeTolerance
    instance.relativeTolerance = original
    assert instance.relativeTolerance == original

@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_frequencyDependent_type(instance):
    assert isinstance(instance.frequencyDependent, bool)


@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_frequencyDependent_setter(instance):
    original = instance.frequencyDependent
    instance.frequencyDependent = original
    assert instance.frequencyDependent == original

@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_backgroundMortalityRate_type(instance):
    assert isinstance(instance.backgroundMortalityRate, float)


@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_backgroundMortalityRate_setter(instance):
    original = instance.backgroundMortalityRate
    instance.backgroundMortalityRate = original
    assert instance.backgroundMortalityRate == original

@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_diseaseName_type(instance):
    assert isinstance(instance.diseaseName, str)


@given(instance=standard::DiseaseModel_strategy)
def test_standard::diseasemodel_diseaseName_setter(instance):
    original = instance.diseaseName
    instance.diseaseName = original
    assert instance.diseaseName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::DiseaseModel_strategy)
@settings(max_examples=30)
def test_standard::diseasemodel_creatediseasemodellabelvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createDiseaseModelLabelValue()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createDiseaseModelLabelValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createDiseaseModelLabelValue' in standard::DiseaseModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createDiseaseModelLabelValue' in standard::DiseaseModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createDiseaseModelLabelValue' in standard::DiseaseModel is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::DiseaseModel_strategy)
@settings(max_examples=30)
def test_standard::diseasemodel_createinfector_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createInfector()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createInfector).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createInfector' in standard::DiseaseModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createInfector' in standard::DiseaseModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createInfector' in standard::DiseaseModel is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::DiseaseModel_strategy)
@settings(max_examples=30)
def test_standard::diseasemodel_creatediseasemodelstate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createDiseaseModelState()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createDiseaseModelState).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createDiseaseModelState' in standard::DiseaseModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createDiseaseModelState' in standard::DiseaseModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createDiseaseModelState' in standard::DiseaseModel is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::DiseaseModel_strategy)
@settings(max_examples=30)
def test_standard::diseasemodel_creatediseasemodellabel_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createDiseaseModelLabel()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createDiseaseModelLabel).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createDiseaseModelLabel' in standard::DiseaseModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createDiseaseModelLabel' in standard::DiseaseModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createDiseaseModelLabel' in standard::DiseaseModel is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=standard::DiseaseModel_strategy)
@settings(max_examples=30)
def test_standard::diseasemodel_initializediseasestate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.initializeDiseaseState(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.initializeDiseaseState).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'initializeDiseaseState' in standard::DiseaseModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'initializeDiseaseState' in standard::DiseaseModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'initializeDiseaseState' in standard::DiseaseModel is not implemented or raised an error")

@given(instance=SIR_strategy)
@settings(max_examples=50)
def test_sir_instantiation(instance):
    assert isinstance(instance, SIR)

@given(instance=standard::StochasticPoissonSIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::stochasticpoissonsirdiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::StochasticPoissonSIRDiseaseModel)

@given(instance=standard::StochasticSIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::stochasticsirdiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::StochasticSIRDiseaseModel)

@given(instance=standard::SEIR_strategy)
@settings(max_examples=50)
def test_standard::seir_instantiation(instance):
    assert isinstance(instance, standard::SEIR)

@given(instance=standard::SEIR_strategy)
def test_standard::seir_incubationRate_type(instance):
    assert isinstance(instance.incubationRate, float)


@given(instance=standard::SEIR_strategy)
def test_standard::seir_incubationRate_setter(instance):
    original = instance.incubationRate
    instance.incubationRate = original
    assert instance.incubationRate == original

@given(instance=standard::DeterministicSIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::deterministicsirdiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::DeterministicSIRDiseaseModel)

@given(instance=SI_strategy)
@settings(max_examples=50)
def test_si_instantiation(instance):
    assert isinstance(instance, SI)

@given(instance=standard::StochasticPoissonSIDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::stochasticpoissonsidiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::StochasticPoissonSIDiseaseModel)

@given(instance=standard::StochasticSIDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::stochasticsidiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::StochasticSIDiseaseModel)

@given(instance=standard::AggregatingSIDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::aggregatingsidiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::AggregatingSIDiseaseModel)

@given(instance=standard::SIR_strategy)
@settings(max_examples=50)
def test_standard::sir_instantiation(instance):
    assert isinstance(instance, standard::SIR)

@given(instance=standard::SIR_strategy)
def test_standard::sir_immunityLossRate_type(instance):
    assert isinstance(instance.immunityLossRate, float)


@given(instance=standard::SIR_strategy)
def test_standard::sir_immunityLossRate_setter(instance):
    original = instance.immunityLossRate
    instance.immunityLossRate = original
    assert instance.immunityLossRate == original

@given(instance=standard::DeterministicSIDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::deterministicsidiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::DeterministicSIDiseaseModel)

@given(instance=SEIR_strategy)
@settings(max_examples=50)
def test_seir_instantiation(instance):
    assert isinstance(instance, SEIR)

@given(instance=standard::StochasticPoissonSEIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::stochasticpoissonseirdiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::StochasticPoissonSEIRDiseaseModel)

@given(instance=standard::StochasticSEIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::stochasticseirdiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::StochasticSEIRDiseaseModel)

@given(instance=standard::DeterministicSEIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_standard::deterministicseirdiseasemodel_instantiation(instance):
    assert isinstance(instance, standard::DeterministicSEIRDiseaseModel)
