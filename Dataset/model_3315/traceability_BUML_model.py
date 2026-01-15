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
traceability_CPSToDeployment = Class(name="traceability::CPSToDeployment")
traceability_CyberPhysicalSystem = Class(name="traceability::CyberPhysicalSystem")
traceability_CPS2DeplyomentTrace = Class(name="traceability::CPS2DeplyomentTrace")
traceability_Identifiable = Class(name="traceability::Identifiable")
traceability_DeploymentElement = Class(name="traceability::DeploymentElement")
traceability_Deployment = Class(name="traceability::Deployment")

# traceability_CPSToDeployment class attributes and methods

# traceability_CyberPhysicalSystem class attributes and methods

# traceability_CPS2DeplyomentTrace class attributes and methods

# traceability_Identifiable class attributes and methods

# traceability_DeploymentElement class attributes and methods

# traceability_Deployment class attributes and methods

# Relationships
cps0: BinaryAssociation = BinaryAssociation(
    name="cps0",
    ends={
        Property(name="traceability_CyberPhysicalSystem", type=traceability_CPSToDeployment, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_CPSToDeployment", type=traceability_CyberPhysicalSystem, multiplicity=Multiplicity(0, 1))
    }
)
traces3: BinaryAssociation = BinaryAssociation(
    name="traces3",
    ends={
        Property(name="traceability_CPS2DeplyomentTrace", type=traceability_CPSToDeployment, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_CPSToDeployment4", type=traceability_CPS2DeplyomentTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cpsElements5: BinaryAssociation = BinaryAssociation(
    name="cpsElements5",
    ends={
        Property(name="traceability_Identifiable", type=traceability_CPS2DeplyomentTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_CPS2DeplyomentTrace6", type=traceability_Identifiable, multiplicity=Multiplicity(0, 9999))
    }
)
deploymentElements7: BinaryAssociation = BinaryAssociation(
    name="deploymentElements7",
    ends={
        Property(name="traceability_DeploymentElement", type=traceability_CPS2DeplyomentTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_CPS2DeplyomentTrace8", type=traceability_DeploymentElement, multiplicity=Multiplicity(0, 9999))
    }
)
deployment1: BinaryAssociation = BinaryAssociation(
    name="deployment1",
    ends={
        Property(name="traceability_Deployment", type=traceability_CPSToDeployment, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_CPSToDeployment2", type=traceability_Deployment, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="traceability",
    types={traceability_CPSToDeployment, traceability_CyberPhysicalSystem, traceability_CPS2DeplyomentTrace, traceability_Identifiable, traceability_DeploymentElement, traceability_Deployment},
    associations={cps0, traces3, cpsElements5, deploymentElements7, deployment1},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)