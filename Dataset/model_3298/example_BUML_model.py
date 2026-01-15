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
example_ExampleDiseaseModel = Class(name="example::ExampleDiseaseModel")
StochasticSIRDiseaseModel = Class(name="StochasticSIRDiseaseModel")

# example_ExampleDiseaseModel class attributes and methods
example_ExampleDiseaseModel_seasonalModulationExponent: Property = Property(name="seasonalModulationExponent", type=FloatType)
example_ExampleDiseaseModel_modulationPeriod: Property = Property(name="modulationPeriod", type=FloatType)
example_ExampleDiseaseModel_modulationPhaseShift: Property = Property(name="modulationPhaseShift", type=FloatType)
example_ExampleDiseaseModel_seasonalModulationFloor: Property = Property(name="seasonalModulationFloor", type=FloatType)
example_ExampleDiseaseModel.attributes={example_ExampleDiseaseModel_seasonalModulationExponent, example_ExampleDiseaseModel_modulationPhaseShift, example_ExampleDiseaseModel_modulationPeriod, example_ExampleDiseaseModel_seasonalModulationFloor}

# StochasticSIRDiseaseModel class attributes and methods

# Generalizations
gen_example_ExampleDiseaseModel_StochasticSIRDiseaseModel = Generalization(general=StochasticSIRDiseaseModel, specific=example_ExampleDiseaseModel)

# Domain Model
domain_model = DomainModel(
    name="example",
    types={example_ExampleDiseaseModel, StochasticSIRDiseaseModel},
    associations={},
    generalizations={gen_example_ExampleDiseaseModel_StochasticSIRDiseaseModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)