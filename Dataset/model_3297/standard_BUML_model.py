####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
standard_DeterministicSEIRDiseaseModel = Class(name="standard::DeterministicSEIRDiseaseModel")
SEIR = Class(name="SEIR")
standard_DeterministicSIDiseaseModel = Class(name="standard::DeterministicSIDiseaseModel")
SI = Class(name="SI")
standard_DeterministicSIRDiseaseModel = Class(name="standard::DeterministicSIRDiseaseModel")
SIR = Class(name="SIR")
standard_DiseaseModel = Class(name="standard::DiseaseModel", is_abstract=True)
NodeDecorator = Class(name="NodeDecorator")
SanityChecker = Class(name="SanityChecker")
Modifiable = Class(name="Modifiable")
standard_DiseaseModelLabel = Class(name="standard::DiseaseModelLabel", is_abstract=True)
DynamicNodeLabel = Class(name="DynamicNodeLabel")
standard_PopulationLabel = Class(name="standard::PopulationLabel")
standard_Infector = Class(name="standard::Infector", is_abstract=True)
standard_StandardDiseaseModel = Class(name="standard::StandardDiseaseModel", is_abstract=True)
standard_SEIR = Class(name="standard::SEIR", is_abstract=True)
standard_SEIRLabel = Class(name="standard::SEIRLabel")
StandardDiseaseModelLabel = Class(name="StandardDiseaseModelLabel")
standard_SEIRLabelValue = Class(name="standard::SEIRLabelValue")
standard_DiseaseModelState = Class(name="standard::DiseaseModelState", is_abstract=True)
standard_PopulationModelLabel = Class(name="standard::PopulationModelLabel")
standard_DiseaseModelLabelValue = Class(name="standard::DiseaseModelLabelValue", is_abstract=True)
LabelValue = Class(name="LabelValue")
IntegrationLabelValue = Class(name="IntegrationLabelValue")
standard_SIDiseaseModelState = Class(name="standard::SIDiseaseModelState")
StandardDiseaseModelState = Class(name="StandardDiseaseModelState")
standard_SIInfector = Class(name="standard::SIInfector")
StandardInfector = Class(name="StandardInfector")
standard_SILabel = Class(name="standard::SILabel")
standard_SILabelValue = Class(name="standard::SILabelValue")
StandardDiseaseModelLabelValue = Class(name="StandardDiseaseModelLabelValue")
standard_SIR = Class(name="standard::SIR", is_abstract=True)
SIRLabelValue = Class(name="SIRLabelValue")
standard_SI = Class(name="standard::SI", is_abstract=True)
StandardDiseaseModel = Class(name="StandardDiseaseModel")
SILabelValue = Class(name="SILabelValue")
DiseaseModel = Class(name="DiseaseModel")
IntegrationDecorator = Class(name="IntegrationDecorator")
standard_StandardDiseaseModelLabel = Class(name="standard::StandardDiseaseModelLabel", is_abstract=True)
DiseaseModelLabel = Class(name="DiseaseModelLabel")
IntegrationLabel = Class(name="IntegrationLabel")
standard_StandardDiseaseModelLabelValue = Class(name="standard::StandardDiseaseModelLabelValue", is_abstract=True)
DiseaseModelLabelValue = Class(name="DiseaseModelLabelValue")
standard_StandardDiseaseModelState = Class(name="standard::StandardDiseaseModelState", is_abstract=True)
DiseaseModelState = Class(name="DiseaseModelState")
standard_StandardInfector = Class(name="standard::StandardInfector", is_abstract=True)
Infector = Class(name="Infector")
standard_StochasticSEIRDiseaseModel = Class(name="standard::StochasticSEIRDiseaseModel")
StandardStochasticDiseaseModel = Class(name="StandardStochasticDiseaseModel")
standard_StochasticSIDiseaseModel = Class(name="standard::StochasticSIDiseaseModel")
standard_StochasticSIRDiseaseModel = Class(name="standard::StochasticSIRDiseaseModel")
standard_SanityChecker = Class(name="standard::SanityChecker", is_abstract=True)
standard_SIRLabel = Class(name="standard::SIRLabel")
standard_SIRLabelValue = Class(name="standard::SIRLabelValue")
standard_AggregatingSEIRDiseaseModel = Class(name="standard::AggregatingSEIRDiseaseModel")
AggregatingSIRDiseaseModel = Class(name="AggregatingSIRDiseaseModel")
standard_AggregatingSIRDiseaseModel = Class(name="standard::AggregatingSIRDiseaseModel")
AggregatingSIDiseaseModel = Class(name="AggregatingSIDiseaseModel")
standard_StochasticDiseaseModel = Class(name="standard::StochasticDiseaseModel", is_abstract=True)
standard_StandardStochasticDiseaseModel = Class(name="standard::StandardStochasticDiseaseModel", is_abstract=True)
StochasticDiseaseModel = Class(name="StochasticDiseaseModel")
standard_SIRInoculator = Class(name="standard::SIRInoculator")
SIInfector = Class(name="SIInfector")
standard_StochasticPoissonSIDiseaseModel = Class(name="standard::StochasticPoissonSIDiseaseModel")
standard_StochasticPoissonSIRDiseaseModel = Class(name="standard::StochasticPoissonSIRDiseaseModel")
standard_StochasticPoissonSEIRDiseaseModel = Class(name="standard::StochasticPoissonSEIRDiseaseModel")
standard_InfectorInoculatorCollection = Class(name="standard::InfectorInoculatorCollection")
standard_IntegrationLabel = Class(name="standard::IntegrationLabel", is_abstract=True)
standard_IntegrationLabelValue = Class(name="standard::IntegrationLabelValue", is_abstract=True)
standard_IntegrationDecorator = Class(name="standard::IntegrationDecorator", is_abstract=True)
standard_AggregatingSIDiseaseModel = Class(name="standard::AggregatingSIDiseaseModel")
standard_AggregatingDiseaseModelState = Class(name="standard::AggregatingDiseaseModelState")

# standard_DeterministicSEIRDiseaseModel class attributes and methods

# SEIR class attributes and methods

# standard_DeterministicSIDiseaseModel class attributes and methods

# SI class attributes and methods

# standard_DeterministicSIRDiseaseModel class attributes and methods

# SIR class attributes and methods

# standard_DiseaseModel class attributes and methods
standard_DiseaseModel_backgroundMortalityRate: Property = Property(name="backgroundMortalityRate", type=FloatType)
standard_DiseaseModel_populationIdentifier: Property = Property(name="populationIdentifier", type=StringType)
standard_DiseaseModel_timePeriod: Property = Property(name="timePeriod", type=StringType)
standard_DiseaseModel_diseaseName: Property = Property(name="diseaseName", type=StringType)
standard_DiseaseModel_relativeTolerance: Property = Property(name="relativeTolerance", type=FloatType)
standard_DiseaseModel_finiteDifference: Property = Property(name="finiteDifference", type=BooleanType)
standard_DiseaseModel_frequencyDependent: Property = Property(name="frequencyDependent", type=BooleanType)
standard_DiseaseModel_backgroundBirthRate: Property = Property(name="backgroundBirthRate", type=FloatType)
standard_DiseaseModel_m_getAdjustedBackgroundMortalityRate: Method = Method(name="getAdjustedBackgroundMortalityRate", parameters={Parameter(name='timeDelta')}, type=FloatType)
standard_DiseaseModel_m_createDiseaseModelLabel: Method = Method(name="createDiseaseModelLabel", parameters={}, type=StringType)
standard_DiseaseModel_m_createDiseaseModelLabelValue: Method = Method(name="createDiseaseModelLabelValue", parameters={}, type=StringType)
standard_DiseaseModel_m_createDiseaseModelState: Method = Method(name="createDiseaseModelState", parameters={}, type=StringType)
standard_DiseaseModel_m_initializeDiseaseState: Method = Method(name="initializeDiseaseState", parameters={Parameter(name='diseaseModelLabel'), Parameter(name='diseaseModelState')}, type=StringType)
standard_DiseaseModel_m_initializeDiseaseState: Method = Method(name="initializeDiseaseState", parameters={Parameter(name='diseaseModelLabel')})
standard_DiseaseModel_m_createInfector: Method = Method(name="createInfector", parameters={}, type=StringType)
standard_DiseaseModel_m_getAdjustedBackgroundBirthRate: Method = Method(name="getAdjustedBackgroundBirthRate", parameters={Parameter(name='timeDelta')}, type=FloatType)
standard_DiseaseModel.attributes={standard_DiseaseModel_diseaseName, standard_DiseaseModel_timePeriod, standard_DiseaseModel_backgroundBirthRate, standard_DiseaseModel_populationIdentifier, standard_DiseaseModel_finiteDifference, standard_DiseaseModel_frequencyDependent, standard_DiseaseModel_backgroundMortalityRate, standard_DiseaseModel_relativeTolerance}
standard_DiseaseModel.methods={standard_DiseaseModel_m_initializeDiseaseState, standard_DiseaseModel_m_createInfector, standard_DiseaseModel_m_createDiseaseModelLabelValue, standard_DiseaseModel_m_createDiseaseModelState, standard_DiseaseModel_m_initializeDiseaseState, standard_DiseaseModel_m_getAdjustedBackgroundBirthRate, standard_DiseaseModel_m_createDiseaseModelLabel, standard_DiseaseModel_m_getAdjustedBackgroundMortalityRate}

# NodeDecorator class attributes and methods

# SanityChecker class attributes and methods

# Modifiable class attributes and methods

# standard_DiseaseModelLabel class attributes and methods

# DynamicNodeLabel class attributes and methods

# standard_PopulationLabel class attributes and methods

# standard_Infector class attributes and methods
standard_Infector_targetURI: Property = Property(name="targetURI", type=StringType)
standard_Infector_diseaseName: Property = Property(name="diseaseName", type=StringType)
standard_Infector_targetISOKey: Property = Property(name="targetISOKey", type=StringType)
standard_Infector_populationIdentifier: Property = Property(name="populationIdentifier", type=StringType)
standard_Infector_infectPercentage: Property = Property(name="infectPercentage", type=BooleanType)
standard_Infector.attributes={standard_Infector_infectPercentage, standard_Infector_diseaseName, standard_Infector_targetURI, standard_Infector_targetISOKey, standard_Infector_populationIdentifier}

# standard_StandardDiseaseModel class attributes and methods
standard_StandardDiseaseModel_totalPopulationCount: Property = Property(name="totalPopulationCount", type=FloatType)
standard_StandardDiseaseModel_totalPopulationCountReciprocal: Property = Property(name="totalPopulationCountReciprocal", type=FloatType)
standard_StandardDiseaseModel_totalArea: Property = Property(name="totalArea", type=FloatType)
standard_StandardDiseaseModel_referencePopulationDensity: Property = Property(name="referencePopulationDensity", type=FloatType)
standard_StandardDiseaseModel_m_addToTotalPopulationCount: Method = Method(name="addToTotalPopulationCount", parameters={Parameter(name='populationCount')})
standard_StandardDiseaseModel_m_computeTotalPopulationCountReciprocal: Method = Method(name="computeTotalPopulationCountReciprocal", parameters={}, type=FloatType)
standard_StandardDiseaseModel_m_addToTotalArea: Method = Method(name="addToTotalArea", parameters={Parameter(name='area')})
standard_StandardDiseaseModel_m_calculateDelta: Method = Method(name="calculateDelta", parameters={Parameter(name='timeDelta'), Parameter(name='time'), Parameter(name='labels')})
standard_StandardDiseaseModel_m_doModelSpecificAdjustments: Method = Method(name="doModelSpecificAdjustments", parameters={Parameter(name='label')})
standard_StandardDiseaseModel.attributes={standard_StandardDiseaseModel_totalPopulationCount, standard_StandardDiseaseModel_referencePopulationDensity, standard_StandardDiseaseModel_totalPopulationCountReciprocal, standard_StandardDiseaseModel_totalArea}
standard_StandardDiseaseModel.methods={standard_StandardDiseaseModel_m_calculateDelta, standard_StandardDiseaseModel_m_addToTotalPopulationCount, standard_StandardDiseaseModel_m_doModelSpecificAdjustments, standard_StandardDiseaseModel_m_addToTotalArea, standard_StandardDiseaseModel_m_computeTotalPopulationCountReciprocal}

# standard_SEIR class attributes and methods
standard_SEIR_incubationRate: Property = Property(name="incubationRate", type=FloatType)
standard_SEIR_m_getAdjustedIncubationRate: Method = Method(name="getAdjustedIncubationRate", parameters={Parameter(name='timeDelta')}, type=FloatType)
standard_SEIR.attributes={standard_SEIR_incubationRate}
standard_SEIR.methods={standard_SEIR_m_getAdjustedIncubationRate}

# standard_SEIRLabel class attributes and methods

# StandardDiseaseModelLabel class attributes and methods

# standard_SEIRLabelValue class attributes and methods
standard_SEIRLabelValue_e: Property = Property(name="e", type=FloatType)
standard_SEIRLabelValue.attributes={standard_SEIRLabelValue_e}

# standard_DiseaseModelState class attributes and methods

# standard_PopulationModelLabel class attributes and methods

# standard_DiseaseModelLabelValue class attributes and methods
standard_DiseaseModelLabelValue_diseaseDeaths: Property = Property(name="diseaseDeaths", type=FloatType)
standard_DiseaseModelLabelValue_populationCount: Property = Property(name="populationCount", type=FloatType)
standard_DiseaseModelLabelValue_incidence: Property = Property(name="incidence", type=FloatType)
standard_DiseaseModelLabelValue_m_sub: Method = Method(name="sub", parameters={Parameter(name='value')}, type=StringType)
standard_DiseaseModelLabelValue_m_scale: Method = Method(name="scale", parameters={Parameter(name='scaleFactor')}, type=StringType)
standard_DiseaseModelLabelValue_m_zeroOutPopulationCount: Method = Method(name="zeroOutPopulationCount", parameters={})
standard_DiseaseModelLabelValue_m_set: Method = Method(name="set", parameters={Parameter(name='value')}, type=StringType)
standard_DiseaseModelLabelValue_m_add: Method = Method(name="add", parameters={Parameter(name='value')}, type=StringType)
standard_DiseaseModelLabelValue.attributes={standard_DiseaseModelLabelValue_incidence, standard_DiseaseModelLabelValue_diseaseDeaths, standard_DiseaseModelLabelValue_populationCount}
standard_DiseaseModelLabelValue.methods={standard_DiseaseModelLabelValue_m_sub, standard_DiseaseModelLabelValue_m_zeroOutPopulationCount, standard_DiseaseModelLabelValue_m_add, standard_DiseaseModelLabelValue_m_scale, standard_DiseaseModelLabelValue_m_set}

# LabelValue class attributes and methods

# IntegrationLabelValue class attributes and methods

# standard_SIDiseaseModelState class attributes and methods

# StandardDiseaseModelState class attributes and methods

# standard_SIInfector class attributes and methods
standard_SIInfector_infectiousCount: Property = Property(name="infectiousCount", type=FloatType)
standard_SIInfector.attributes={standard_SIInfector_infectiousCount}

# StandardInfector class attributes and methods

# standard_SILabel class attributes and methods

# standard_SILabelValue class attributes and methods
standard_SILabelValue_i: Property = Property(name="i", type=FloatType)
standard_SILabelValue.attributes={standard_SILabelValue_i}

# StandardDiseaseModelLabelValue class attributes and methods

# standard_SIR class attributes and methods
standard_SIR_immunityLossRate: Property = Property(name="immunityLossRate", type=FloatType)
standard_SIR_m_getAdjustedImmunityLossRate: Method = Method(name="getAdjustedImmunityLossRate", parameters={Parameter(name='timeDelta')}, type=FloatType)
standard_SIR.attributes={standard_SIR_immunityLossRate}
standard_SIR.methods={standard_SIR_m_getAdjustedImmunityLossRate}

# SIRLabelValue class attributes and methods

# standard_SI class attributes and methods
standard_SI_transmissionRate: Property = Property(name="transmissionRate", type=FloatType)
standard_SI_nonLinearityCoefficient: Property = Property(name="nonLinearityCoefficient", type=FloatType)
standard_SI_recoveryRate: Property = Property(name="recoveryRate", type=FloatType)
standard_SI_infectiousMortalityRate: Property = Property(name="infectiousMortalityRate", type=FloatType)
standard_SI_physicallyAdjacentInfectiousProportion: Property = Property(name="physicallyAdjacentInfectiousProportion", type=FloatType)
standard_SI_roadNetworkInfectiousProportion: Property = Property(name="roadNetworkInfectiousProportion", type=FloatType)
standard_SI_infectiousMortality: Property = Property(name="infectiousMortality", type=FloatType)
standard_SI_characteristicMixingDistance: Property = Property(name="characteristicMixingDistance", type=FloatType)
standard_SI_m_getAdjustedTransmissionRate: Method = Method(name="getAdjustedTransmissionRate", parameters={Parameter(name='timeDelta')}, type=FloatType)
standard_SI_m_getAdjustedRecoveryRate: Method = Method(name="getAdjustedRecoveryRate", parameters={Parameter(name='timeDelta')}, type=FloatType)
standard_SI_m_getEffectiveInfectious: Method = Method(name="getEffectiveInfectious", parameters={Parameter(name='diseaseLabel'), Parameter(name='onsiteInfectious'), Parameter(name='node')}, type=FloatType)
standard_SI_m_getNormalizedEffectiveInfectious: Method = Method(name="getNormalizedEffectiveInfectious", parameters={Parameter(name='diseaseLabel'), Parameter(name='onsiteInfectious'), Parameter(name='node')}, type=FloatType)
standard_SI_m_getAdjustedInfectiousMortalityRate: Method = Method(name="getAdjustedInfectiousMortalityRate", parameters={Parameter(name='timeDelta')}, type=FloatType)
standard_SI.attributes={standard_SI_transmissionRate, standard_SI_nonLinearityCoefficient, standard_SI_infectiousMortalityRate, standard_SI_infectiousMortality, standard_SI_characteristicMixingDistance, standard_SI_recoveryRate, standard_SI_roadNetworkInfectiousProportion, standard_SI_physicallyAdjacentInfectiousProportion}
standard_SI.methods={standard_SI_m_getAdjustedInfectiousMortalityRate, standard_SI_m_getAdjustedTransmissionRate, standard_SI_m_getNormalizedEffectiveInfectious, standard_SI_m_getAdjustedRecoveryRate, standard_SI_m_getEffectiveInfectious}

# StandardDiseaseModel class attributes and methods

# SILabelValue class attributes and methods

# DiseaseModel class attributes and methods

# IntegrationDecorator class attributes and methods

# standard_StandardDiseaseModelLabel class attributes and methods

# DiseaseModelLabel class attributes and methods

# IntegrationLabel class attributes and methods

# standard_StandardDiseaseModelLabelValue class attributes and methods
standard_StandardDiseaseModelLabelValue_s: Property = Property(name="s", type=FloatType)
standard_StandardDiseaseModelLabelValue.attributes={standard_StandardDiseaseModelLabelValue_s}

# DiseaseModelLabelValue class attributes and methods

# standard_StandardDiseaseModelState class attributes and methods
standard_StandardDiseaseModelState_areaRatio: Property = Property(name="areaRatio", type=FloatType)
standard_StandardDiseaseModelState.attributes={standard_StandardDiseaseModelState_areaRatio}

# DiseaseModelState class attributes and methods

# standard_StandardInfector class attributes and methods

# Infector class attributes and methods

# standard_StochasticSEIRDiseaseModel class attributes and methods

# StandardStochasticDiseaseModel class attributes and methods

# standard_StochasticSIDiseaseModel class attributes and methods

# standard_StochasticSIRDiseaseModel class attributes and methods

# standard_SanityChecker class attributes and methods

# standard_SIRLabel class attributes and methods

# standard_SIRLabelValue class attributes and methods
standard_SIRLabelValue_r: Property = Property(name="r", type=FloatType)
standard_SIRLabelValue.attributes={standard_SIRLabelValue_r}

# standard_AggregatingSEIRDiseaseModel class attributes and methods

# AggregatingSIRDiseaseModel class attributes and methods

# standard_AggregatingSIRDiseaseModel class attributes and methods

# AggregatingSIDiseaseModel class attributes and methods

# standard_StochasticDiseaseModel class attributes and methods
standard_StochasticDiseaseModel_seed: Property = Property(name="seed", type=StringType)
standard_StochasticDiseaseModel_randomGenerator: Property = Property(name="randomGenerator", type=StringType)
standard_StochasticDiseaseModel.attributes={standard_StochasticDiseaseModel_seed, standard_StochasticDiseaseModel_randomGenerator}

# standard_StandardStochasticDiseaseModel class attributes and methods
standard_StandardStochasticDiseaseModel_gain: Property = Property(name="gain", type=FloatType)
standard_StandardStochasticDiseaseModel_m_computeNoise: Method = Method(name="computeNoise", parameters={}, type=FloatType)
standard_StandardStochasticDiseaseModel.attributes={standard_StandardStochasticDiseaseModel_gain}
standard_StandardStochasticDiseaseModel.methods={standard_StandardStochasticDiseaseModel_m_computeNoise}

# StochasticDiseaseModel class attributes and methods

# standard_SIRInoculator class attributes and methods
standard_SIRInoculator_inoculatedPercentage: Property = Property(name="inoculatedPercentage", type=FloatType)
standard_SIRInoculator_inoculatePercentage: Property = Property(name="inoculatePercentage", type=BooleanType)
standard_SIRInoculator.attributes={standard_SIRInoculator_inoculatedPercentage, standard_SIRInoculator_inoculatePercentage}

# SIInfector class attributes and methods

# standard_StochasticPoissonSIDiseaseModel class attributes and methods

# standard_StochasticPoissonSIRDiseaseModel class attributes and methods

# standard_StochasticPoissonSEIRDiseaseModel class attributes and methods

# standard_InfectorInoculatorCollection class attributes and methods
standard_InfectorInoculatorCollection_importFolder: Property = Property(name="importFolder", type=StringType)
standard_InfectorInoculatorCollection.attributes={standard_InfectorInoculatorCollection_importFolder}

# standard_IntegrationLabel class attributes and methods

# standard_IntegrationLabelValue class attributes and methods

# standard_IntegrationDecorator class attributes and methods
standard_IntegrationDecorator_m_isDeterministic: Method = Method(name="isDeterministic", parameters={}, type=BooleanType)
standard_IntegrationDecorator.methods={standard_IntegrationDecorator_m_isDeterministic}

# standard_AggregatingSIDiseaseModel class attributes and methods

# standard_AggregatingDiseaseModelState class attributes and methods

# Relationships
populationLabel0: BinaryAssociation = BinaryAssociation(
    name="populationLabel0",
    ends={
        Property(name="standard_PopulationLabel", type=standard_DiseaseModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_DiseaseModelLabel", type=standard_PopulationLabel, multiplicity=Multiplicity(0, 1))
    }
)
label4: BinaryAssociation = BinaryAssociation(
    name="label4",
    ends={
        Property(name="DiseaseModelLabel", type=standard_DiseaseModelState, multiplicity=Multiplicity(1, 1)),
        Property(name="diseaseModelState", type=standard_DiseaseModelLabel, multiplicity=Multiplicity(0, 1))
    }
)
diseaseModel5: BinaryAssociation = BinaryAssociation(
    name="diseaseModel5",
    ends={
        Property(name="standard_StandardDiseaseModel", type=standard_Infector, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Infector", type=standard_StandardDiseaseModel, multiplicity=Multiplicity(0, 1))
    }
)
labelsToInfect6: BinaryAssociation = BinaryAssociation(
    name="labelsToInfect6",
    ends={
        Property(name="standard_DiseaseModelLabel8", type=standard_Infector, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Infector7", type=standard_DiseaseModelLabel, multiplicity=Multiplicity(0, 9999))
    }
)
deltaValue9: BinaryAssociation = BinaryAssociation(
    name="deltaValue9",
    ends={
        Property(name="standard_SEIRLabelValue", type=standard_SEIRLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SEIRLabel", type=standard_SEIRLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
probeValue10: BinaryAssociation = BinaryAssociation(
    name="probeValue10",
    ends={
        Property(name="standard_SEIRLabelValue12", type=standard_SEIRLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SEIRLabel11", type=standard_SEIRLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
tempValue13: BinaryAssociation = BinaryAssociation(
    name="tempValue13",
    ends={
        Property(name="standard_SEIRLabelValue15", type=standard_SEIRLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SEIRLabel14", type=standard_SEIRLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
originalValue16: BinaryAssociation = BinaryAssociation(
    name="originalValue16",
    ends={
        Property(name="standard_SEIRLabelValue18", type=standard_SEIRLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SEIRLabel17", type=standard_SEIRLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
diseaseModelState1: BinaryAssociation = BinaryAssociation(
    name="diseaseModelState1",
    ends={
        Property(name="DiseaseModelState", type=standard_DiseaseModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="label", type=standard_DiseaseModelState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
populationModelLabel2: BinaryAssociation = BinaryAssociation(
    name="populationModelLabel2",
    ends={
        Property(name="standard_PopulationModelLabel", type=standard_DiseaseModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_DiseaseModelLabel3", type=standard_PopulationModelLabel, multiplicity=Multiplicity(0, 1))
    }
)
deltaValue22: BinaryAssociation = BinaryAssociation(
    name="deltaValue22",
    ends={
        Property(name="standard_SILabelValue", type=standard_SILabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SILabel", type=standard_SILabelValue, multiplicity=Multiplicity(0, 1))
    }
)
probeValue23: BinaryAssociation = BinaryAssociation(
    name="probeValue23",
    ends={
        Property(name="standard_SILabelValue25", type=standard_SILabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SILabel24", type=standard_SILabelValue, multiplicity=Multiplicity(0, 1))
    }
)
tempValue26: BinaryAssociation = BinaryAssociation(
    name="tempValue26",
    ends={
        Property(name="standard_SILabelValue28", type=standard_SILabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SILabel27", type=standard_SILabelValue, multiplicity=Multiplicity(0, 1))
    }
)
originalValue29: BinaryAssociation = BinaryAssociation(
    name="originalValue29",
    ends={
        Property(name="standard_SILabelValue31", type=standard_SILabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SILabel30", type=standard_SILabelValue, multiplicity=Multiplicity(0, 1))
    }
)
errorScale32: BinaryAssociation = BinaryAssociation(
    name="errorScale32",
    ends={
        Property(name="standard_SILabelValue34", type=standard_SILabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SILabel33", type=standard_SILabelValue, multiplicity=Multiplicity(0, 1))
    }
)
errorScale19: BinaryAssociation = BinaryAssociation(
    name="errorScale19",
    ends={
        Property(name="standard_SEIRLabelValue21", type=standard_SEIRLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SEIRLabel20", type=standard_SEIRLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
errorScale45: BinaryAssociation = BinaryAssociation(
    name="errorScale45",
    ends={
        Property(name="standard_SIRLabelValue47", type=standard_SIRLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SIRLabel46", type=standard_SIRLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
deltaValue35: BinaryAssociation = BinaryAssociation(
    name="deltaValue35",
    ends={
        Property(name="standard_SIRLabelValue", type=standard_SIRLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SIRLabel", type=standard_SIRLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
probeValue36: BinaryAssociation = BinaryAssociation(
    name="probeValue36",
    ends={
        Property(name="standard_SIRLabelValue38", type=standard_SIRLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SIRLabel37", type=standard_SIRLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
tempValue39: BinaryAssociation = BinaryAssociation(
    name="tempValue39",
    ends={
        Property(name="standard_SIRLabelValue41", type=standard_SIRLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SIRLabel40", type=standard_SIRLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
originalValue42: BinaryAssociation = BinaryAssociation(
    name="originalValue42",
    ends={
        Property(name="standard_SIRLabelValue44", type=standard_SIRLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SIRLabel43", type=standard_SIRLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
list50: BinaryAssociation = BinaryAssociation(
    name="list50",
    ends={
        Property(name="standard_Infector51", type=standard_InfectorInoculatorCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_InfectorInoculatorCollection", type=standard_Infector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrensLabels48: BinaryAssociation = BinaryAssociation(
    name="childrensLabels48",
    ends={
        Property(name="standard_SILabel49", type=standard_AggregatingDiseaseModelState, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_AggregatingDiseaseModelState", type=standard_SILabel, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_standard_DeterministicSEIRDiseaseModel_SEIR = Generalization(general=SEIR, specific=standard_DeterministicSEIRDiseaseModel)
gen_standard_DeterministicSIDiseaseModel_SI = Generalization(general=SI, specific=standard_DeterministicSIDiseaseModel)
gen_standard_DeterministicSIRDiseaseModel_SIR = Generalization(general=SIR, specific=standard_DeterministicSIRDiseaseModel)
gen_standard_DiseaseModel_NodeDecorator = Generalization(general=NodeDecorator, specific=standard_DiseaseModel)
gen_standard_DiseaseModel_SanityChecker = Generalization(general=SanityChecker, specific=standard_DiseaseModel)
gen_standard_DiseaseModel_Modifiable = Generalization(general=Modifiable, specific=standard_DiseaseModel)
gen_standard_DiseaseModelLabel_DynamicNodeLabel = Generalization(general=DynamicNodeLabel, specific=standard_DiseaseModelLabel)
gen_standard_Infector_NodeDecorator = Generalization(general=NodeDecorator, specific=standard_Infector)
gen_standard_Infector_Modifiable = Generalization(general=Modifiable, specific=standard_Infector)
gen_standard_SEIR_SIR = Generalization(general=SIR, specific=standard_SEIR)
gen_standard_SEIRLabel_StandardDiseaseModelLabel = Generalization(general=StandardDiseaseModelLabel, specific=standard_SEIRLabel)
gen_standard_DiseaseModelLabelValue_LabelValue = Generalization(general=LabelValue, specific=standard_DiseaseModelLabelValue)
gen_standard_DiseaseModelLabelValue_IntegrationLabelValue = Generalization(general=IntegrationLabelValue, specific=standard_DiseaseModelLabelValue)
gen_standard_SIDiseaseModelState_StandardDiseaseModelState = Generalization(general=StandardDiseaseModelState, specific=standard_SIDiseaseModelState)
gen_standard_SIInfector_StandardInfector = Generalization(general=StandardInfector, specific=standard_SIInfector)
gen_standard_SILabel_StandardDiseaseModelLabel = Generalization(general=StandardDiseaseModelLabel, specific=standard_SILabel)
gen_standard_SILabelValue_StandardDiseaseModelLabelValue = Generalization(general=StandardDiseaseModelLabelValue, specific=standard_SILabelValue)
gen_standard_SIR_SI = Generalization(general=SI, specific=standard_SIR)
gen_standard_SEIRLabelValue_SIRLabelValue = Generalization(general=SIRLabelValue, specific=standard_SEIRLabelValue)
gen_standard_SI_StandardDiseaseModel = Generalization(general=StandardDiseaseModel, specific=standard_SI)
gen_standard_SIRLabelValue_SILabelValue = Generalization(general=SILabelValue, specific=standard_SIRLabelValue)
gen_standard_StandardDiseaseModel_DiseaseModel = Generalization(general=DiseaseModel, specific=standard_StandardDiseaseModel)
gen_standard_StandardDiseaseModel_IntegrationDecorator = Generalization(general=IntegrationDecorator, specific=standard_StandardDiseaseModel)
gen_standard_StandardDiseaseModelLabel_DiseaseModelLabel = Generalization(general=DiseaseModelLabel, specific=standard_StandardDiseaseModelLabel)
gen_standard_StandardDiseaseModelLabel_IntegrationLabel = Generalization(general=IntegrationLabel, specific=standard_StandardDiseaseModelLabel)
gen_standard_StandardDiseaseModelLabelValue_DiseaseModelLabelValue = Generalization(general=DiseaseModelLabelValue, specific=standard_StandardDiseaseModelLabelValue)
gen_standard_StandardDiseaseModelState_DiseaseModelState = Generalization(general=DiseaseModelState, specific=standard_StandardDiseaseModelState)
gen_standard_StandardInfector_Infector = Generalization(general=Infector, specific=standard_StandardInfector)
gen_standard_StochasticSEIRDiseaseModel_SEIR = Generalization(general=SEIR, specific=standard_StochasticSEIRDiseaseModel)
gen_standard_StochasticSEIRDiseaseModel_StandardStochasticDiseaseModel = Generalization(general=StandardStochasticDiseaseModel, specific=standard_StochasticSEIRDiseaseModel)
gen_standard_StochasticSIDiseaseModel_SI = Generalization(general=SI, specific=standard_StochasticSIDiseaseModel)
gen_standard_StochasticSIDiseaseModel_StandardStochasticDiseaseModel = Generalization(general=StandardStochasticDiseaseModel, specific=standard_StochasticSIDiseaseModel)
gen_standard_StochasticSIRDiseaseModel_SIR = Generalization(general=SIR, specific=standard_StochasticSIRDiseaseModel)
gen_standard_StochasticSIRDiseaseModel_StandardStochasticDiseaseModel = Generalization(general=StandardStochasticDiseaseModel, specific=standard_StochasticSIRDiseaseModel)
gen_standard_SIRLabel_StandardDiseaseModelLabel = Generalization(general=StandardDiseaseModelLabel, specific=standard_SIRLabel)
gen_standard_AggregatingSEIRDiseaseModel_AggregatingSIRDiseaseModel = Generalization(general=AggregatingSIRDiseaseModel, specific=standard_AggregatingSEIRDiseaseModel)
gen_standard_AggregatingSIRDiseaseModel_AggregatingSIDiseaseModel = Generalization(general=AggregatingSIDiseaseModel, specific=standard_AggregatingSIRDiseaseModel)
gen_standard_StochasticDiseaseModel_DiseaseModel = Generalization(general=DiseaseModel, specific=standard_StochasticDiseaseModel)
gen_standard_StandardStochasticDiseaseModel_StochasticDiseaseModel = Generalization(general=StochasticDiseaseModel, specific=standard_StandardStochasticDiseaseModel)
gen_standard_SIRInoculator_SIInfector = Generalization(general=SIInfector, specific=standard_SIRInoculator)
gen_standard_StochasticPoissonSIDiseaseModel_SI = Generalization(general=SI, specific=standard_StochasticPoissonSIDiseaseModel)
gen_standard_StochasticPoissonSIRDiseaseModel_SIR = Generalization(general=SIR, specific=standard_StochasticPoissonSIRDiseaseModel)
gen_standard_StochasticPoissonSEIRDiseaseModel_SEIR = Generalization(general=SEIR, specific=standard_StochasticPoissonSEIRDiseaseModel)
gen_standard_InfectorInoculatorCollection_NodeDecorator = Generalization(general=NodeDecorator, specific=standard_InfectorInoculatorCollection)
gen_standard_InfectorInoculatorCollection_Modifiable = Generalization(general=Modifiable, specific=standard_InfectorInoculatorCollection)
gen_standard_AggregatingSIDiseaseModel_SI = Generalization(general=SI, specific=standard_AggregatingSIDiseaseModel)
gen_standard_AggregatingDiseaseModelState_DiseaseModelState = Generalization(general=DiseaseModelState, specific=standard_AggregatingDiseaseModelState)

# Domain Model
domain_model = DomainModel(
    name="standard",
    types={standard_DeterministicSEIRDiseaseModel, SEIR, standard_DeterministicSIDiseaseModel, SI, standard_DeterministicSIRDiseaseModel, SIR, standard_DiseaseModel, NodeDecorator, SanityChecker, Modifiable, standard_DiseaseModelLabel, DynamicNodeLabel, standard_PopulationLabel, standard_Infector, standard_StandardDiseaseModel, standard_SEIR, standard_SEIRLabel, StandardDiseaseModelLabel, standard_SEIRLabelValue, standard_DiseaseModelState, standard_PopulationModelLabel, standard_DiseaseModelLabelValue, LabelValue, IntegrationLabelValue, standard_SIDiseaseModelState, StandardDiseaseModelState, standard_SIInfector, StandardInfector, standard_SILabel, standard_SILabelValue, StandardDiseaseModelLabelValue, standard_SIR, SIRLabelValue, standard_SI, StandardDiseaseModel, SILabelValue, DiseaseModel, IntegrationDecorator, standard_StandardDiseaseModelLabel, DiseaseModelLabel, IntegrationLabel, standard_StandardDiseaseModelLabelValue, DiseaseModelLabelValue, standard_StandardDiseaseModelState, DiseaseModelState, standard_StandardInfector, Infector, standard_StochasticSEIRDiseaseModel, StandardStochasticDiseaseModel, standard_StochasticSIDiseaseModel, standard_StochasticSIRDiseaseModel, standard_SanityChecker, standard_SIRLabel, standard_SIRLabelValue, standard_AggregatingSEIRDiseaseModel, AggregatingSIRDiseaseModel, standard_AggregatingSIRDiseaseModel, AggregatingSIDiseaseModel, standard_StochasticDiseaseModel, standard_StandardStochasticDiseaseModel, StochasticDiseaseModel, standard_SIRInoculator, SIInfector, standard_StochasticPoissonSIDiseaseModel, standard_StochasticPoissonSIRDiseaseModel, standard_StochasticPoissonSEIRDiseaseModel, standard_InfectorInoculatorCollection, standard_IntegrationLabel, standard_IntegrationLabelValue, standard_IntegrationDecorator, standard_AggregatingSIDiseaseModel, standard_AggregatingDiseaseModelState},
    associations={populationLabel0, label4, diseaseModel5, labelsToInfect6, deltaValue9, probeValue10, tempValue13, originalValue16, diseaseModelState1, populationModelLabel2, deltaValue22, probeValue23, tempValue26, originalValue29, errorScale32, errorScale19, errorScale45, deltaValue35, probeValue36, tempValue39, originalValue42, list50, childrensLabels48},
    generalizations={gen_standard_DeterministicSEIRDiseaseModel_SEIR, gen_standard_DeterministicSIDiseaseModel_SI, gen_standard_DeterministicSIRDiseaseModel_SIR, gen_standard_DiseaseModel_NodeDecorator, gen_standard_DiseaseModel_SanityChecker, gen_standard_DiseaseModel_Modifiable, gen_standard_DiseaseModelLabel_DynamicNodeLabel, gen_standard_Infector_NodeDecorator, gen_standard_Infector_Modifiable, gen_standard_SEIR_SIR, gen_standard_SEIRLabel_StandardDiseaseModelLabel, gen_standard_DiseaseModelLabelValue_LabelValue, gen_standard_DiseaseModelLabelValue_IntegrationLabelValue, gen_standard_SIDiseaseModelState_StandardDiseaseModelState, gen_standard_SIInfector_StandardInfector, gen_standard_SILabel_StandardDiseaseModelLabel, gen_standard_SILabelValue_StandardDiseaseModelLabelValue, gen_standard_SIR_SI, gen_standard_SEIRLabelValue_SIRLabelValue, gen_standard_SI_StandardDiseaseModel, gen_standard_SIRLabelValue_SILabelValue, gen_standard_StandardDiseaseModel_DiseaseModel, gen_standard_StandardDiseaseModel_IntegrationDecorator, gen_standard_StandardDiseaseModelLabel_DiseaseModelLabel, gen_standard_StandardDiseaseModelLabel_IntegrationLabel, gen_standard_StandardDiseaseModelLabelValue_DiseaseModelLabelValue, gen_standard_StandardDiseaseModelState_DiseaseModelState, gen_standard_StandardInfector_Infector, gen_standard_StochasticSEIRDiseaseModel_SEIR, gen_standard_StochasticSEIRDiseaseModel_StandardStochasticDiseaseModel, gen_standard_StochasticSIDiseaseModel_SI, gen_standard_StochasticSIDiseaseModel_StandardStochasticDiseaseModel, gen_standard_StochasticSIRDiseaseModel_SIR, gen_standard_StochasticSIRDiseaseModel_StandardStochasticDiseaseModel, gen_standard_SIRLabel_StandardDiseaseModelLabel, gen_standard_AggregatingSEIRDiseaseModel_AggregatingSIRDiseaseModel, gen_standard_AggregatingSIRDiseaseModel_AggregatingSIDiseaseModel, gen_standard_StochasticDiseaseModel_DiseaseModel, gen_standard_StandardStochasticDiseaseModel_StochasticDiseaseModel, gen_standard_SIRInoculator_SIInfector, gen_standard_StochasticPoissonSIDiseaseModel_SI, gen_standard_StochasticPoissonSIRDiseaseModel_SIR, gen_standard_StochasticPoissonSEIRDiseaseModel_SEIR, gen_standard_InfectorInoculatorCollection_NodeDecorator, gen_standard_InfectorInoculatorCollection_Modifiable, gen_standard_AggregatingSIDiseaseModel_SI, gen_standard_AggregatingDiseaseModelState_DiseaseModelState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)