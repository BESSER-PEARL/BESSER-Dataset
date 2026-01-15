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
standard_PopulationModel = Class(name="standard::PopulationModel", is_abstract=True)
NodeDecorator = Class(name="NodeDecorator")
Modifiable = Class(name="Modifiable")
standard_StandardPopulationModel = Class(name="standard::StandardPopulationModel")
IntegrationLabelValue = Class(name="IntegrationLabelValue")
standard_StochasticStandardPopulationModel = Class(name="standard::StochasticStandardPopulationModel")
StandardPopulationModel = Class(name="StandardPopulationModel")
standard_DemographicPopulationModel = Class(name="standard::DemographicPopulationModel")
standard_PopulationGroup = Class(name="standard::PopulationGroup")
standard_PopulationInitializer = Class(name="standard::PopulationInitializer", is_abstract=True)
PopulationModel = Class(name="PopulationModel")
IntegrationDecorator = Class(name="IntegrationDecorator")
standard_PopulationModelLabel = Class(name="standard::PopulationModelLabel")
DynamicNodeLabel = Class(name="DynamicNodeLabel")
standard_PopulationLabel = Class(name="standard::PopulationLabel")
standard_StandardPopulationModelLabel = Class(name="standard::StandardPopulationModelLabel")
PopulationModelLabel = Class(name="PopulationModelLabel")
IntegrationLabel = Class(name="IntegrationLabel")
standard_StandardPopulationModelLabelValue = Class(name="standard::StandardPopulationModelLabelValue")
standard_IntegrationLabel = Class(name="standard::IntegrationLabel", is_abstract=True)
standard_IntegrationLabelValue = Class(name="standard::IntegrationLabelValue", is_abstract=True)
standard_IntegrationDecorator = Class(name="standard::IntegrationDecorator", is_abstract=True)
standard_PopulationModelLabelValue = Class(name="standard::PopulationModelLabelValue")
LabelValue = Class(name="LabelValue")
PopulationModelLabelValue = Class(name="PopulationModelLabelValue")
standard_StandardPopulationInitializer = Class(name="standard::StandardPopulationInitializer")
PopulationInitializer = Class(name="PopulationInitializer")
standard_SeasonalPopulationModel = Class(name="standard::SeasonalPopulationModel")
standard_EarthSciencePopulationInitializer = Class(name="standard::EarthSciencePopulationInitializer", is_abstract=True)
standard_YetiPopulationInitializer = Class(name="standard::YetiPopulationInitializer")
EarthSciencePopulationInitializer = Class(name="EarthSciencePopulationInitializer")

# standard_PopulationModel class attributes and methods
standard_PopulationModel_populationIdentifier: Property = Property(name="populationIdentifier", type=StringType)
standard_PopulationModel_name: Property = Property(name="name", type=StringType)
standard_PopulationModel_targetISOKey: Property = Property(name="targetISOKey", type=StringType)
standard_PopulationModel.attributes={standard_PopulationModel_populationIdentifier, standard_PopulationModel_targetISOKey, standard_PopulationModel_name}

# NodeDecorator class attributes and methods

# Modifiable class attributes and methods

# standard_StandardPopulationModel class attributes and methods
standard_StandardPopulationModel_birthRate: Property = Property(name="birthRate", type=FloatType)
standard_StandardPopulationModel_deathRate: Property = Property(name="deathRate", type=FloatType)
standard_StandardPopulationModel_timePeriod: Property = Property(name="timePeriod", type=StringType)
standard_StandardPopulationModel.attributes={standard_StandardPopulationModel_deathRate, standard_StandardPopulationModel_timePeriod, standard_StandardPopulationModel_birthRate}

# IntegrationLabelValue class attributes and methods

# standard_StochasticStandardPopulationModel class attributes and methods
standard_StochasticStandardPopulationModel_gain: Property = Property(name="gain", type=FloatType)
standard_StochasticStandardPopulationModel.attributes={standard_StochasticStandardPopulationModel_gain}

# StandardPopulationModel class attributes and methods

# standard_DemographicPopulationModel class attributes and methods

# standard_PopulationGroup class attributes and methods
standard_PopulationGroup_identifier: Property = Property(name="identifier", type=StringType)
standard_PopulationGroup_fraction: Property = Property(name="fraction", type=FloatType)
standard_PopulationGroup.attributes={standard_PopulationGroup_identifier, standard_PopulationGroup_fraction}

# standard_PopulationInitializer class attributes and methods
standard_PopulationInitializer_targetISOKey: Property = Property(name="targetISOKey", type=StringType)
standard_PopulationInitializer_populationIdentifier: Property = Property(name="populationIdentifier", type=StringType)
standard_PopulationInitializer.attributes={standard_PopulationInitializer_populationIdentifier, standard_PopulationInitializer_targetISOKey}

# PopulationModel class attributes and methods

# IntegrationDecorator class attributes and methods

# standard_PopulationModelLabel class attributes and methods
standard_PopulationModelLabel_populationIdentifier: Property = Property(name="populationIdentifier", type=StringType)
standard_PopulationModelLabel.attributes={standard_PopulationModelLabel_populationIdentifier}

# DynamicNodeLabel class attributes and methods

# standard_PopulationLabel class attributes and methods

# standard_StandardPopulationModelLabel class attributes and methods

# PopulationModelLabel class attributes and methods

# IntegrationLabel class attributes and methods

# standard_StandardPopulationModelLabelValue class attributes and methods
standard_StandardPopulationModelLabelValue_count: Property = Property(name="count", type=FloatType)
standard_StandardPopulationModelLabelValue_incidence: Property = Property(name="incidence", type=FloatType)
standard_StandardPopulationModelLabelValue_births: Property = Property(name="births", type=FloatType)
standard_StandardPopulationModelLabelValue_deaths: Property = Property(name="deaths", type=FloatType)
standard_StandardPopulationModelLabelValue_density: Property = Property(name="density", type=FloatType)
standard_StandardPopulationModelLabelValue_m_adjustDelta: Method = Method(name="adjustDelta", parameters={Parameter(name='value')}, type=BooleanType)
standard_StandardPopulationModelLabelValue.attributes={standard_StandardPopulationModelLabelValue_incidence, standard_StandardPopulationModelLabelValue_density, standard_StandardPopulationModelLabelValue_count, standard_StandardPopulationModelLabelValue_births, standard_StandardPopulationModelLabelValue_deaths}
standard_StandardPopulationModelLabelValue.methods={standard_StandardPopulationModelLabelValue_m_adjustDelta}

# standard_IntegrationLabel class attributes and methods

# standard_IntegrationLabelValue class attributes and methods

# standard_IntegrationDecorator class attributes and methods

# standard_PopulationModelLabelValue class attributes and methods

# LabelValue class attributes and methods

# PopulationModelLabelValue class attributes and methods

# standard_StandardPopulationInitializer class attributes and methods
standard_StandardPopulationInitializer_individuals: Property = Property(name="individuals", type=FloatType)
standard_StandardPopulationInitializer_useDensity: Property = Property(name="useDensity", type=BooleanType)
standard_StandardPopulationInitializer.attributes={standard_StandardPopulationInitializer_useDensity, standard_StandardPopulationInitializer_individuals}

# PopulationInitializer class attributes and methods

# standard_SeasonalPopulationModel class attributes and methods
standard_SeasonalPopulationModel_phase: Property = Property(name="phase", type=FloatType)
standard_SeasonalPopulationModel_modulationAmplitude: Property = Property(name="modulationAmplitude", type=FloatType)
standard_SeasonalPopulationModel_period: Property = Property(name="period", type=FloatType)
standard_SeasonalPopulationModel_useLatitude: Property = Property(name="useLatitude", type=BooleanType)
standard_SeasonalPopulationModel.attributes={standard_SeasonalPopulationModel_period, standard_SeasonalPopulationModel_phase, standard_SeasonalPopulationModel_useLatitude, standard_SeasonalPopulationModel_modulationAmplitude}

# standard_EarthSciencePopulationInitializer class attributes and methods

# standard_YetiPopulationInitializer class attributes and methods

# EarthSciencePopulationInitializer class attributes and methods

# Relationships
populationGroups14: BinaryAssociation = BinaryAssociation(
    name="populationGroups14",
    ends={
        Property(name="standard_PopulationGroup", type=standard_DemographicPopulationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_DemographicPopulationModel", type=standard_PopulationGroup, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
populationLabel0: BinaryAssociation = BinaryAssociation(
    name="populationLabel0",
    ends={
        Property(name="standard_PopulationLabel", type=standard_PopulationModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_PopulationModelLabel", type=standard_PopulationLabel, multiplicity=Multiplicity(0, 1))
    }
)
deltaValue1: BinaryAssociation = BinaryAssociation(
    name="deltaValue1",
    ends={
        Property(name="standard_StandardPopulationModelLabelValue", type=standard_StandardPopulationModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_StandardPopulationModelLabel", type=standard_StandardPopulationModelLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
probeValue2: BinaryAssociation = BinaryAssociation(
    name="probeValue2",
    ends={
        Property(name="standard_StandardPopulationModelLabelValue4", type=standard_StandardPopulationModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_StandardPopulationModelLabel3", type=standard_StandardPopulationModelLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
tempValue5: BinaryAssociation = BinaryAssociation(
    name="tempValue5",
    ends={
        Property(name="standard_StandardPopulationModelLabelValue7", type=standard_StandardPopulationModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_StandardPopulationModelLabel6", type=standard_StandardPopulationModelLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
originalValue8: BinaryAssociation = BinaryAssociation(
    name="originalValue8",
    ends={
        Property(name="standard_StandardPopulationModelLabelValue10", type=standard_StandardPopulationModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_StandardPopulationModelLabel9", type=standard_StandardPopulationModelLabelValue, multiplicity=Multiplicity(0, 1))
    }
)
errorScale11: BinaryAssociation = BinaryAssociation(
    name="errorScale11",
    ends={
        Property(name="standard_StandardPopulationModelLabelValue13", type=standard_StandardPopulationModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_StandardPopulationModelLabel12", type=standard_StandardPopulationModelLabelValue, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_standard_PopulationModel_NodeDecorator = Generalization(general=NodeDecorator, specific=standard_PopulationModel)
gen_standard_PopulationModel_Modifiable = Generalization(general=Modifiable, specific=standard_PopulationModel)
gen_standard_StandardPopulationModelLabelValue_IntegrationLabelValue = Generalization(general=IntegrationLabelValue, specific=standard_StandardPopulationModelLabelValue)
gen_standard_StochasticStandardPopulationModel_StandardPopulationModel = Generalization(general=StandardPopulationModel, specific=standard_StochasticStandardPopulationModel)
gen_standard_DemographicPopulationModel_StandardPopulationModel = Generalization(general=StandardPopulationModel, specific=standard_DemographicPopulationModel)
gen_standard_PopulationInitializer_NodeDecorator = Generalization(general=NodeDecorator, specific=standard_PopulationInitializer)
gen_standard_PopulationInitializer_Modifiable = Generalization(general=Modifiable, specific=standard_PopulationInitializer)
gen_standard_StandardPopulationModel_PopulationModel = Generalization(general=PopulationModel, specific=standard_StandardPopulationModel)
gen_standard_StandardPopulationModel_IntegrationDecorator = Generalization(general=IntegrationDecorator, specific=standard_StandardPopulationModel)
gen_standard_PopulationModelLabel_DynamicNodeLabel = Generalization(general=DynamicNodeLabel, specific=standard_PopulationModelLabel)
gen_standard_StandardPopulationModelLabel_PopulationModelLabel = Generalization(general=PopulationModelLabel, specific=standard_StandardPopulationModelLabel)
gen_standard_StandardPopulationModelLabel_IntegrationLabel = Generalization(general=IntegrationLabel, specific=standard_StandardPopulationModelLabel)
gen_standard_PopulationModelLabelValue_LabelValue = Generalization(general=LabelValue, specific=standard_PopulationModelLabelValue)
gen_standard_StandardPopulationModelLabelValue_PopulationModelLabelValue = Generalization(general=PopulationModelLabelValue, specific=standard_StandardPopulationModelLabelValue)
gen_standard_StandardPopulationInitializer_PopulationInitializer = Generalization(general=PopulationInitializer, specific=standard_StandardPopulationInitializer)
gen_standard_SeasonalPopulationModel_StandardPopulationModel = Generalization(general=StandardPopulationModel, specific=standard_SeasonalPopulationModel)
gen_standard_EarthSciencePopulationInitializer_PopulationInitializer = Generalization(general=PopulationInitializer, specific=standard_EarthSciencePopulationInitializer)
gen_standard_YetiPopulationInitializer_EarthSciencePopulationInitializer = Generalization(general=EarthSciencePopulationInitializer, specific=standard_YetiPopulationInitializer)

# Domain Model
domain_model = DomainModel(
    name="standard",
    types={standard_PopulationModel, NodeDecorator, Modifiable, standard_StandardPopulationModel, IntegrationLabelValue, standard_StochasticStandardPopulationModel, StandardPopulationModel, standard_DemographicPopulationModel, standard_PopulationGroup, standard_PopulationInitializer, PopulationModel, IntegrationDecorator, standard_PopulationModelLabel, DynamicNodeLabel, standard_PopulationLabel, standard_StandardPopulationModelLabel, PopulationModelLabel, IntegrationLabel, standard_StandardPopulationModelLabelValue, standard_IntegrationLabel, standard_IntegrationLabelValue, standard_IntegrationDecorator, standard_PopulationModelLabelValue, LabelValue, PopulationModelLabelValue, standard_StandardPopulationInitializer, PopulationInitializer, standard_SeasonalPopulationModel, standard_EarthSciencePopulationInitializer, standard_YetiPopulationInitializer, EarthSciencePopulationInitializer},
    associations={populationGroups14, populationLabel0, deltaValue1, probeValue2, tempValue5, originalValue8, errorScale11},
    generalizations={gen_standard_PopulationModel_NodeDecorator, gen_standard_PopulationModel_Modifiable, gen_standard_StandardPopulationModelLabelValue_IntegrationLabelValue, gen_standard_StochasticStandardPopulationModel_StandardPopulationModel, gen_standard_DemographicPopulationModel_StandardPopulationModel, gen_standard_PopulationInitializer_NodeDecorator, gen_standard_PopulationInitializer_Modifiable, gen_standard_StandardPopulationModel_PopulationModel, gen_standard_StandardPopulationModel_IntegrationDecorator, gen_standard_PopulationModelLabel_DynamicNodeLabel, gen_standard_StandardPopulationModelLabel_PopulationModelLabel, gen_standard_StandardPopulationModelLabel_IntegrationLabel, gen_standard_PopulationModelLabelValue_LabelValue, gen_standard_StandardPopulationModelLabelValue_PopulationModelLabelValue, gen_standard_StandardPopulationInitializer_PopulationInitializer, gen_standard_SeasonalPopulationModel_StandardPopulationModel, gen_standard_EarthSciencePopulationInitializer_PopulationInitializer, gen_standard_YetiPopulationInitializer_EarthSciencePopulationInitializer},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)