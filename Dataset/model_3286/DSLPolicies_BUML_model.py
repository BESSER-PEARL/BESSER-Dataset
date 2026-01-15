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
dSLPolicies_Model = Class(name="dSLPolicies::Model")
dSLPolicies_GraphPolicies = Class(name="dSLPolicies::GraphPolicies")
dSLPolicies_Policies = Class(name="dSLPolicies::Policies")
dSLPolicies_Severity = Class(name="dSLPolicies::Severity")
dSLPolicies_PathGeneratorStopCondition = Class(name="dSLPolicies::PathGeneratorStopCondition")
dSLPolicies_AlgorithmType = Class(name="dSLPolicies::AlgorithmType")
dSLPolicies_StopCondition = Class(name="dSLPolicies::StopCondition")
dSLPolicies_GraphElement = Class(name="dSLPolicies::GraphElement")

# dSLPolicies_Model class attributes and methods

# dSLPolicies_GraphPolicies class attributes and methods
dSLPolicies_GraphPolicies_graphModelPolicies: Property = Property(name="graphModelPolicies", type=StringType)
dSLPolicies_GraphPolicies.attributes={dSLPolicies_GraphPolicies_graphModelPolicies}

# dSLPolicies_Policies class attributes and methods
dSLPolicies_Policies_nocheck: Property = Property(name="nocheck", type=BooleanType)
dSLPolicies_Policies_sync: Property = Property(name="sync", type=BooleanType)
dSLPolicies_Policies.attributes={dSLPolicies_Policies_nocheck, dSLPolicies_Policies_sync}

# dSLPolicies_Severity class attributes and methods
dSLPolicies_Severity_level: Property = Property(name="level", type=StringType)
dSLPolicies_Severity.attributes={dSLPolicies_Severity_level}

# dSLPolicies_PathGeneratorStopCondition class attributes and methods

# dSLPolicies_AlgorithmType class attributes and methods
dSLPolicies_AlgorithmType_type: Property = Property(name="type", type=StringType)
dSLPolicies_AlgorithmType.attributes={dSLPolicies_AlgorithmType_type}

# dSLPolicies_StopCondition class attributes and methods
dSLPolicies_StopCondition_pathtype: Property = Property(name="pathtype", type=StringType)
dSLPolicies_StopCondition_value: Property = Property(name="value", type=IntegerType)
dSLPolicies_StopCondition_percentage: Property = Property(name="percentage", type=StringType)
dSLPolicies_StopCondition.attributes={dSLPolicies_StopCondition_pathtype, dSLPolicies_StopCondition_value, dSLPolicies_StopCondition_percentage}

# dSLPolicies_GraphElement class attributes and methods
dSLPolicies_GraphElement_name: Property = Property(name="name", type=StringType)
dSLPolicies_GraphElement.attributes={dSLPolicies_GraphElement_name}

# Relationships
graphPolicies0: BinaryAssociation = BinaryAssociation(
    name="graphPolicies0",
    ends={
        Property(name="dSLPolicies_GraphPolicies", type=dSLPolicies_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dSLPolicies_Model", type=dSLPolicies_GraphPolicies, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
policies1: BinaryAssociation = BinaryAssociation(
    name="policies1",
    ends={
        Property(name="dSLPolicies_Policies", type=dSLPolicies_GraphPolicies, multiplicity=Multiplicity(1, 1)),
        Property(name="dSLPolicies_GraphPolicies2", type=dSLPolicies_Policies, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathgenerator3: BinaryAssociation = BinaryAssociation(
    name="pathgenerator3",
    ends={
        Property(name="dSLPolicies_PathGeneratorStopCondition", type=dSLPolicies_Policies, multiplicity=Multiplicity(1, 1)),
        Property(name="dSLPolicies_Policies4", type=dSLPolicies_PathGeneratorStopCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
severity5: BinaryAssociation = BinaryAssociation(
    name="severity5",
    ends={
        Property(name="dSLPolicies_Severity", type=dSLPolicies_Policies, multiplicity=Multiplicity(1, 1)),
        Property(name="dSLPolicies_Policies6", type=dSLPolicies_Severity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphelement14: BinaryAssociation = BinaryAssociation(
    name="graphelement14",
    ends={
        Property(name="dSLPolicies_StopCondition15", type=dSLPolicies_GraphElement, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="dSLPolicies_GraphElement", type=dSLPolicies_StopCondition, multiplicity=Multiplicity(1, 1))
    }
)
algorithmType7: BinaryAssociation = BinaryAssociation(
    name="algorithmType7",
    ends={
        Property(name="dSLPolicies_AlgorithmType", type=dSLPolicies_PathGeneratorStopCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="dSLPolicies_PathGeneratorStopCondition8", type=dSLPolicies_AlgorithmType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stopCondition9: BinaryAssociation = BinaryAssociation(
    name="stopCondition9",
    ends={
        Property(name="dSLPolicies_StopCondition", type=dSLPolicies_PathGeneratorStopCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="dSLPolicies_PathGeneratorStopCondition10", type=dSLPolicies_StopCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stopConditionype11: BinaryAssociation = BinaryAssociation(
    name="stopConditionype11",
    ends={
        Property(name="dSLPolicies_StopCondition13", type=dSLPolicies_PathGeneratorStopCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="dSLPolicies_PathGeneratorStopCondition12", type=dSLPolicies_StopCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="dSLPolicies",
    types={dSLPolicies_Model, dSLPolicies_GraphPolicies, dSLPolicies_Policies, dSLPolicies_Severity, dSLPolicies_PathGeneratorStopCondition, dSLPolicies_AlgorithmType, dSLPolicies_StopCondition, dSLPolicies_GraphElement},
    associations={graphPolicies0, policies1, pathgenerator3, severity5, graphelement14, algorithmType7, stopCondition9, stopConditionype11},
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