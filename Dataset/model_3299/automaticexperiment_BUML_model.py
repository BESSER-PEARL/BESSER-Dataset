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
automaticexperiment_AutomaticExperiment = Class(name="automaticexperiment::AutomaticExperiment")
Identifiable = Class(name="Identifiable")
automaticexperiment_Scenario = Class(name="automaticexperiment::Scenario")
automaticexperiment_ModifiableParameter = Class(name="automaticexperiment::ModifiableParameter")
automaticexperiment_EStructuralFeature = Class(name="automaticexperiment::EStructuralFeature")

# automaticexperiment_AutomaticExperiment class attributes and methods
automaticexperiment_AutomaticExperiment_errorAnalysisAlgorithm: Property = Property(name="errorAnalysisAlgorithm", type=StringType)
automaticexperiment_AutomaticExperiment_errorFunction: Property = Property(name="errorFunction", type=StringType)
automaticexperiment_AutomaticExperiment_tolerance: Property = Property(name="tolerance", type=FloatType)
automaticexperiment_AutomaticExperiment_referanceDataDir: Property = Property(name="referanceDataDir", type=StringType)
automaticexperiment_AutomaticExperiment_maximumNumberOfIterations: Property = Property(name="maximumNumberOfIterations", type=StringType)
automaticexperiment_AutomaticExperiment_reInit: Property = Property(name="reInit", type=BooleanType)
automaticexperiment_AutomaticExperiment.attributes={automaticexperiment_AutomaticExperiment_referanceDataDir, automaticexperiment_AutomaticExperiment_reInit, automaticexperiment_AutomaticExperiment_maximumNumberOfIterations, automaticexperiment_AutomaticExperiment_errorAnalysisAlgorithm, automaticexperiment_AutomaticExperiment_errorFunction, automaticexperiment_AutomaticExperiment_tolerance}

# Identifiable class attributes and methods

# automaticexperiment_Scenario class attributes and methods

# automaticexperiment_ModifiableParameter class attributes and methods
automaticexperiment_ModifiableParameter_initialValue: Property = Property(name="initialValue", type=FloatType)
automaticexperiment_ModifiableParameter_step: Property = Property(name="step", type=FloatType)
automaticexperiment_ModifiableParameter_featureName: Property = Property(name="featureName", type=StringType)
automaticexperiment_ModifiableParameter_lowerBound: Property = Property(name="lowerBound", type=FloatType)
automaticexperiment_ModifiableParameter_upperBound: Property = Property(name="upperBound", type=FloatType)
automaticexperiment_ModifiableParameter_targetURI: Property = Property(name="targetURI", type=StringType)
automaticexperiment_ModifiableParameter.attributes={automaticexperiment_ModifiableParameter_targetURI, automaticexperiment_ModifiableParameter_step, automaticexperiment_ModifiableParameter_lowerBound, automaticexperiment_ModifiableParameter_featureName, automaticexperiment_ModifiableParameter_upperBound, automaticexperiment_ModifiableParameter_initialValue}

# automaticexperiment_EStructuralFeature class attributes and methods

# Relationships
baseScenario0: BinaryAssociation = BinaryAssociation(
    name="baseScenario0",
    ends={
        Property(name="automaticexperiment_Scenario", type=automaticexperiment_AutomaticExperiment, multiplicity=Multiplicity(1, 1)),
        Property(name="automaticexperiment_AutomaticExperiment", type=automaticexperiment_Scenario, multiplicity=Multiplicity(1, 1))
    }
)
parameters1: BinaryAssociation = BinaryAssociation(
    name="parameters1",
    ends={
        Property(name="automaticexperiment_ModifiableParameter", type=automaticexperiment_AutomaticExperiment, multiplicity=Multiplicity(1, 1)),
        Property(name="automaticexperiment_AutomaticExperiment2", type=automaticexperiment_ModifiableParameter, multiplicity=Multiplicity(1, 9999))
    }
)
feature3: BinaryAssociation = BinaryAssociation(
    name="feature3",
    ends={
        Property(name="automaticexperiment_EStructuralFeature", type=automaticexperiment_ModifiableParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="automaticexperiment_ModifiableParameter4", type=automaticexperiment_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_automaticexperiment_AutomaticExperiment_Identifiable = Generalization(general=Identifiable, specific=automaticexperiment_AutomaticExperiment)

# Domain Model
domain_model = DomainModel(
    name="automaticexperiment",
    types={automaticexperiment_AutomaticExperiment, Identifiable, automaticexperiment_Scenario, automaticexperiment_ModifiableParameter, automaticexperiment_EStructuralFeature},
    associations={baseScenario0, parameters1, feature3},
    generalizations={gen_automaticexperiment_AutomaticExperiment_Identifiable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)