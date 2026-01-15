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
experimental_PerculationDiseaseModel = Class(name="experimental::PerculationDiseaseModel")
StochasticSEIRDiseaseModel = Class(name="StochasticSEIRDiseaseModel")

# experimental_PerculationDiseaseModel class attributes and methods

# StochasticSEIRDiseaseModel class attributes and methods

# Generalizations
gen_experimental_PerculationDiseaseModel_StochasticSEIRDiseaseModel = Generalization(general=StochasticSEIRDiseaseModel, specific=experimental_PerculationDiseaseModel)

# Domain Model
domain_model = DomainModel(
    name="experimental",
    types={experimental_PerculationDiseaseModel, StochasticSEIRDiseaseModel},
    associations={},
    generalizations={gen_experimental_PerculationDiseaseModel_StochasticSEIRDiseaseModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)