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
forcing_ForcingDiseaseModel = Class(name="forcing::ForcingDiseaseModel")
StochasticSIRDiseaseModel = Class(name="StochasticSIRDiseaseModel")
forcing_GaussianForcingDiseaseModel = Class(name="forcing::GaussianForcingDiseaseModel")
forcing_Gaussian2ForcingDiseaseModel = Class(name="forcing::Gaussian2ForcingDiseaseModel")
forcing_Gaussian3ForcingDiseaseModel = Class(name="forcing::Gaussian3ForcingDiseaseModel")
Gaussian2ForcingDiseaseModel = Class(name="Gaussian2ForcingDiseaseModel")

# forcing_ForcingDiseaseModel class attributes and methods
forcing_ForcingDiseaseModel_seasonalModulationExponent: Property = Property(name="seasonalModulationExponent", type=FloatType)
forcing_ForcingDiseaseModel_modulationPeriod: Property = Property(name="modulationPeriod", type=FloatType)
forcing_ForcingDiseaseModel_modulationPhaseShift: Property = Property(name="modulationPhaseShift", type=FloatType)
forcing_ForcingDiseaseModel_seasonalModulationFloor: Property = Property(name="seasonalModulationFloor", type=FloatType)
forcing_ForcingDiseaseModel.attributes={forcing_ForcingDiseaseModel_modulationPeriod, forcing_ForcingDiseaseModel_seasonalModulationExponent, forcing_ForcingDiseaseModel_seasonalModulationFloor, forcing_ForcingDiseaseModel_modulationPhaseShift}

# StochasticSIRDiseaseModel class attributes and methods

# forcing_GaussianForcingDiseaseModel class attributes and methods
forcing_GaussianForcingDiseaseModel_sigma2: Property = Property(name="sigma2", type=FloatType)
forcing_GaussianForcingDiseaseModel_modulationPeriod: Property = Property(name="modulationPeriod", type=FloatType)
forcing_GaussianForcingDiseaseModel_modulationPhaseShift: Property = Property(name="modulationPhaseShift", type=FloatType)
forcing_GaussianForcingDiseaseModel_modulationFloor: Property = Property(name="modulationFloor", type=FloatType)
forcing_GaussianForcingDiseaseModel.attributes={forcing_GaussianForcingDiseaseModel_sigma2, forcing_GaussianForcingDiseaseModel_modulationFloor, forcing_GaussianForcingDiseaseModel_modulationPhaseShift, forcing_GaussianForcingDiseaseModel_modulationPeriod}

# forcing_Gaussian2ForcingDiseaseModel class attributes and methods
forcing_Gaussian2ForcingDiseaseModel_modulationPeriod: Property = Property(name="modulationPeriod", type=FloatType)
forcing_Gaussian2ForcingDiseaseModel_modulationPhaseShift: Property = Property(name="modulationPhaseShift", type=FloatType)
forcing_Gaussian2ForcingDiseaseModel_modulationFloor: Property = Property(name="modulationFloor", type=FloatType)
forcing_Gaussian2ForcingDiseaseModel_sigma2_2: Property = Property(name="sigma2_2", type=FloatType)
forcing_Gaussian2ForcingDiseaseModel_sigma2: Property = Property(name="sigma2", type=FloatType)
forcing_Gaussian2ForcingDiseaseModel_att1: Property = Property(name="att1", type=FloatType)
forcing_Gaussian2ForcingDiseaseModel_att2: Property = Property(name="att2", type=FloatType)
forcing_Gaussian2ForcingDiseaseModel_att3: Property = Property(name="att3", type=FloatType)
forcing_Gaussian2ForcingDiseaseModel_att4: Property = Property(name="att4", type=FloatType)
forcing_Gaussian2ForcingDiseaseModel.attributes={forcing_Gaussian2ForcingDiseaseModel_att4, forcing_Gaussian2ForcingDiseaseModel_modulationPhaseShift, forcing_Gaussian2ForcingDiseaseModel_att1, forcing_Gaussian2ForcingDiseaseModel_sigma2, forcing_Gaussian2ForcingDiseaseModel_att3, forcing_Gaussian2ForcingDiseaseModel_sigma2_2, forcing_Gaussian2ForcingDiseaseModel_modulationPeriod, forcing_Gaussian2ForcingDiseaseModel_att2, forcing_Gaussian2ForcingDiseaseModel_modulationFloor}

# forcing_Gaussian3ForcingDiseaseModel class attributes and methods
forcing_Gaussian3ForcingDiseaseModel_sigma2_3: Property = Property(name="sigma2_3", type=FloatType)
forcing_Gaussian3ForcingDiseaseModel_transmissionRate2: Property = Property(name="transmissionRate2", type=FloatType)
forcing_Gaussian3ForcingDiseaseModel_transmissionRate3: Property = Property(name="transmissionRate3", type=FloatType)
forcing_Gaussian3ForcingDiseaseModel_modulationFloor_2: Property = Property(name="modulationFloor_2", type=FloatType)
forcing_Gaussian3ForcingDiseaseModel.attributes={forcing_Gaussian3ForcingDiseaseModel_transmissionRate3, forcing_Gaussian3ForcingDiseaseModel_transmissionRate2, forcing_Gaussian3ForcingDiseaseModel_sigma2_3, forcing_Gaussian3ForcingDiseaseModel_modulationFloor_2}

# Gaussian2ForcingDiseaseModel class attributes and methods

# Generalizations
gen_forcing_ForcingDiseaseModel_StochasticSIRDiseaseModel = Generalization(general=StochasticSIRDiseaseModel, specific=forcing_ForcingDiseaseModel)
gen_forcing_GaussianForcingDiseaseModel_StochasticSIRDiseaseModel = Generalization(general=StochasticSIRDiseaseModel, specific=forcing_GaussianForcingDiseaseModel)
gen_forcing_Gaussian2ForcingDiseaseModel_StochasticSIRDiseaseModel = Generalization(general=StochasticSIRDiseaseModel, specific=forcing_Gaussian2ForcingDiseaseModel)
gen_forcing_Gaussian3ForcingDiseaseModel_Gaussian2ForcingDiseaseModel = Generalization(general=Gaussian2ForcingDiseaseModel, specific=forcing_Gaussian3ForcingDiseaseModel)

# Domain Model
domain_model = DomainModel(
    name="forcing",
    types={forcing_ForcingDiseaseModel, StochasticSIRDiseaseModel, forcing_GaussianForcingDiseaseModel, forcing_Gaussian2ForcingDiseaseModel, forcing_Gaussian3ForcingDiseaseModel, Gaussian2ForcingDiseaseModel},
    associations={},
    generalizations={gen_forcing_ForcingDiseaseModel_StochasticSIRDiseaseModel, gen_forcing_GaussianForcingDiseaseModel_StochasticSIRDiseaseModel, gen_forcing_Gaussian2ForcingDiseaseModel_StochasticSIRDiseaseModel, gen_forcing_Gaussian3ForcingDiseaseModel_Gaussian2ForcingDiseaseModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)