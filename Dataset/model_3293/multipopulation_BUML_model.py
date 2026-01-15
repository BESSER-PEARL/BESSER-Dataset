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
multipopulation_StringValueList = Class(name="multipopulation::StringValueList")
multipopulation_DoubleValueMatrix = Class(name="multipopulation::DoubleValueMatrix")
multipopulation_DoubleValueList = Class(name="multipopulation::DoubleValueList")
multipopulation_MultiPopulationSIDiseaseModel = Class(name="multipopulation::MultiPopulationSIDiseaseModel")
StandardDiseaseModel = Class(name="StandardDiseaseModel")
multipopulation_MultiPopulationSIRDiseaseModel = Class(name="multipopulation::MultiPopulationSIRDiseaseModel")
MultiPopulationSIDiseaseModel = Class(name="MultiPopulationSIDiseaseModel")
multipopulation_MultiPopulationSEIRDiseaseModel = Class(name="multipopulation::MultiPopulationSEIRDiseaseModel")
MultiPopulationSIRDiseaseModel = Class(name="MultiPopulationSIRDiseaseModel")

# multipopulation_StringValueList class attributes and methods

# multipopulation_DoubleValueMatrix class attributes and methods

# multipopulation_DoubleValueList class attributes and methods

# multipopulation_MultiPopulationSIDiseaseModel class attributes and methods
multipopulation_MultiPopulationSIDiseaseModel_physicallyAdjacentInfectiousProportion: Property = Property(name="physicallyAdjacentInfectiousProportion", type=FloatType)
multipopulation_MultiPopulationSIDiseaseModel_roadNetworkInfectiousProportion: Property = Property(name="roadNetworkInfectiousProportion", type=FloatType)
multipopulation_MultiPopulationSIDiseaseModel_characteristicMixingDistance: Property = Property(name="characteristicMixingDistance", type=FloatType)
multipopulation_MultiPopulationSIDiseaseModel.attributes={multipopulation_MultiPopulationSIDiseaseModel_physicallyAdjacentInfectiousProportion, multipopulation_MultiPopulationSIDiseaseModel_characteristicMixingDistance, multipopulation_MultiPopulationSIDiseaseModel_roadNetworkInfectiousProportion}

# StandardDiseaseModel class attributes and methods

# multipopulation_MultiPopulationSIRDiseaseModel class attributes and methods

# MultiPopulationSIDiseaseModel class attributes and methods

# multipopulation_MultiPopulationSEIRDiseaseModel class attributes and methods

# MultiPopulationSIRDiseaseModel class attributes and methods

# Relationships
populationGroups0: BinaryAssociation = BinaryAssociation(
    name="populationGroups0",
    ends={
        Property(name="multipopulation_StringValueList", type=multipopulation_MultiPopulationSIDiseaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="multipopulation_MultiPopulationSIDiseaseModel", type=multipopulation_StringValueList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
transmissionRate1: BinaryAssociation = BinaryAssociation(
    name="transmissionRate1",
    ends={
        Property(name="multipopulation_DoubleValueMatrix", type=multipopulation_MultiPopulationSIDiseaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="multipopulation_MultiPopulationSIDiseaseModel2", type=multipopulation_DoubleValueMatrix, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
recoveryRate3: BinaryAssociation = BinaryAssociation(
    name="recoveryRate3",
    ends={
        Property(name="multipopulation_DoubleValueList", type=multipopulation_MultiPopulationSIDiseaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="multipopulation_MultiPopulationSIDiseaseModel4", type=multipopulation_DoubleValueList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
infectiousMortalityRate5: BinaryAssociation = BinaryAssociation(
    name="infectiousMortalityRate5",
    ends={
        Property(name="multipopulation_DoubleValueList7", type=multipopulation_MultiPopulationSIDiseaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="multipopulation_MultiPopulationSIDiseaseModel6", type=multipopulation_DoubleValueList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
immunityLossRate8: BinaryAssociation = BinaryAssociation(
    name="immunityLossRate8",
    ends={
        Property(name="multipopulation_DoubleValueList9", type=multipopulation_MultiPopulationSIRDiseaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="multipopulation_MultiPopulationSIRDiseaseModel", type=multipopulation_DoubleValueList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
incubationRate10: BinaryAssociation = BinaryAssociation(
    name="incubationRate10",
    ends={
        Property(name="multipopulation_DoubleValueList11", type=multipopulation_MultiPopulationSEIRDiseaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="multipopulation_MultiPopulationSEIRDiseaseModel", type=multipopulation_DoubleValueList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_multipopulation_MultiPopulationSIDiseaseModel_StandardDiseaseModel = Generalization(general=StandardDiseaseModel, specific=multipopulation_MultiPopulationSIDiseaseModel)
gen_multipopulation_MultiPopulationSIRDiseaseModel_MultiPopulationSIDiseaseModel = Generalization(general=MultiPopulationSIDiseaseModel, specific=multipopulation_MultiPopulationSIRDiseaseModel)
gen_multipopulation_MultiPopulationSEIRDiseaseModel_MultiPopulationSIRDiseaseModel = Generalization(general=MultiPopulationSIRDiseaseModel, specific=multipopulation_MultiPopulationSEIRDiseaseModel)

# Domain Model
domain_model = DomainModel(
    name="multipopulation",
    types={multipopulation_StringValueList, multipopulation_DoubleValueMatrix, multipopulation_DoubleValueList, multipopulation_MultiPopulationSIDiseaseModel, StandardDiseaseModel, multipopulation_MultiPopulationSIRDiseaseModel, MultiPopulationSIDiseaseModel, multipopulation_MultiPopulationSEIRDiseaseModel, MultiPopulationSIRDiseaseModel},
    associations={populationGroups0, transmissionRate1, recoveryRate3, infectiousMortalityRate5, immunityLossRate8, incubationRate10},
    generalizations={gen_multipopulation_MultiPopulationSIDiseaseModel_StandardDiseaseModel, gen_multipopulation_MultiPopulationSIRDiseaseModel_MultiPopulationSIDiseaseModel, gen_multipopulation_MultiPopulationSEIRDiseaseModel_MultiPopulationSIRDiseaseModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)