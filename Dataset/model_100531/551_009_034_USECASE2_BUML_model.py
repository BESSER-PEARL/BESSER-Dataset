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
USECASEUML_NonFunctionnelRequirement = Class(name="USECASEUML_NonFunctionnelRequirement")
Requirement = Class(name="Requirement")
UseCase = Class(name="UseCase")
USECASEUML_FunctionnelRequirement = Class(name="USECASEUML_FunctionnelRequirement")
USECASEUML_Requirement = Class(name="USECASEUML_Requirement")
Goal = Class(name="Goal")
USECASEUML_Goal = Class(name="USECASEUML_Goal")
USECASEUML_UseCase = Class(name="USECASEUML_UseCase")
ScenarioDescription = Class(name="ScenarioDescription")
Condition = Class(name="Condition")
Role = Class(name="Role")
FunctionnelRequirement = Class(name="FunctionnelRequirement")
NonFunctionnelRequirement = Class(name="NonFunctionnelRequirement")
USECASEUML_Pre = Class(name="USECASEUML_Pre")
USECASEUML_Post = Class(name="USECASEUML_Post")
USECASEUML_Role = Class(name="USECASEUML_Role")
USECASEUML_HumanRole = Class(name="USECASEUML_HumanRole")
USECASEUML_SystemRole = Class(name="USECASEUML_SystemRole")
USECASEUML_EventRole = Class(name="USECASEUML_EventRole")
USECASEUML_Manage = Class(name="USECASEUML_Manage")
Resource = Class(name="Resource")
USECASEUML_Resource = Class(name="USECASEUML_Resource")
USECASEUML_ScenarioDescription = Class(name="USECASEUML_ScenarioDescription")
USECASEUML_Condition = Class(name="USECASEUML_Condition")

# USECASEUML_NonFunctionnelRequirement class attributes and methods

# Requirement class attributes and methods

# UseCase class attributes and methods

# USECASEUML_FunctionnelRequirement class attributes and methods

# USECASEUML_Requirement class attributes and methods

# Goal class attributes and methods

# USECASEUML_Goal class attributes and methods

# USECASEUML_UseCase class attributes and methods

# ScenarioDescription class attributes and methods

# Condition class attributes and methods

# Role class attributes and methods

# FunctionnelRequirement class attributes and methods

# NonFunctionnelRequirement class attributes and methods

# USECASEUML_Pre class attributes and methods

# USECASEUML_Post class attributes and methods

# USECASEUML_Role class attributes and methods

# USECASEUML_HumanRole class attributes and methods

# USECASEUML_SystemRole class attributes and methods

# USECASEUML_EventRole class attributes and methods

# USECASEUML_Manage class attributes and methods

# Resource class attributes and methods

# USECASEUML_Resource class attributes and methods

# USECASEUML_ScenarioDescription class attributes and methods

# USECASEUML_Condition class attributes and methods

# Relationships
scopes0: BinaryAssociation = BinaryAssociation(
    name="scopes0",
    ends={
        Property(name="UseCase", type=USECASEUML_NonFunctionnelRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="scoped_by", type=UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
meet_by8: BinaryAssociation = BinaryAssociation(
    name="meet_by8",
    ends={
        Property(name="Goal", type=USECASEUML_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="to_meet", type=Goal, multiplicity=Multiplicity(1, 9999))
    }
)
to_meet9: BinaryAssociation = BinaryAssociation(
    name="to_meet9",
    ends={
        Property(name="UseCase10", type=USECASEUML_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="meet_by", type=UseCase, multiplicity=Multiplicity(1, 9999))
    }
)
specifies1: BinaryAssociation = BinaryAssociation(
    name="specifies1",
    ends={
        Property(name="UseCase2", type=USECASEUML_FunctionnelRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="specified_by", type=UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
scenario3: BinaryAssociation = BinaryAssociation(
    name="scenario3",
    ends={
        Property(name="ScenarioDescription", type=USECASEUML_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=ScenarioDescription, multiplicity=Multiplicity(0, 9999))
    }
)
condition4: BinaryAssociation = BinaryAssociation(
    name="condition4",
    ends={
        Property(name="Condition", type=USECASEUML_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="constrained_with", type=Condition, multiplicity=Multiplicity(0, 9999))
    }
)
interacter5: BinaryAssociation = BinaryAssociation(
    name="interacter5",
    ends={
        Property(name="Role", type=USECASEUML_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="interacted_with", type=Role, multiplicity=Multiplicity(0, 9999))
    }
)
specified_by6: BinaryAssociation = BinaryAssociation(
    name="specified_by6",
    ends={
        Property(name="FunctionnelRequirement", type=USECASEUML_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="specifies", type=FunctionnelRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
scoped_by7: BinaryAssociation = BinaryAssociation(
    name="scoped_by7",
    ends={
        Property(name="NonFunctionnelRequirement", type=USECASEUML_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="scopes", type=NonFunctionnelRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
interacted_with11: BinaryAssociation = BinaryAssociation(
    name="interacted_with11",
    ends={
        Property(name="UseCase12", type=USECASEUML_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="interacter", type=UseCase, multiplicity=Multiplicity(0, 9999))
    }
)
managed_Resource13: BinaryAssociation = BinaryAssociation(
    name="managed_Resource13",
    ends={
        Property(name="Resource", type=USECASEUML_Manage, multiplicity=Multiplicity(1, 1)),
        Property(name="USECASEUML_Manage", type=Resource, multiplicity=Multiplicity(0, 9999))
    }
)
useCase14: BinaryAssociation = BinaryAssociation(
    name="useCase14",
    ends={
        Property(name="UseCase15", type=USECASEUML_ScenarioDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="scenario", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
constrained_with16: BinaryAssociation = BinaryAssociation(
    name="constrained_with16",
    ends={
        Property(name="UseCase17", type=USECASEUML_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=UseCase, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_USECASEUML_NonFunctionnelRequirement_Requirement = Generalization(general=Requirement, specific=USECASEUML_NonFunctionnelRequirement)
gen_USECASEUML_FunctionnelRequirement_Requirement = Generalization(general=Requirement, specific=USECASEUML_FunctionnelRequirement)
gen_USECASEUML_Pre_Condition = Generalization(general=Condition, specific=USECASEUML_Pre)
gen_USECASEUML_Post_Condition = Generalization(general=Condition, specific=USECASEUML_Post)
gen_USECASEUML_HumanRole_Role = Generalization(general=Role, specific=USECASEUML_HumanRole)
gen_USECASEUML_SystemRole_Role = Generalization(general=Role, specific=USECASEUML_SystemRole)
gen_USECASEUML_EventRole_Role = Generalization(general=Role, specific=USECASEUML_EventRole)
gen_USECASEUML_Manage_UseCase = Generalization(general=UseCase, specific=USECASEUML_Manage)

# Domain Model
domain_model = DomainModel(
    name="USECASEUML",
    types={USECASEUML_NonFunctionnelRequirement, Requirement, UseCase, USECASEUML_FunctionnelRequirement, USECASEUML_Requirement, Goal, USECASEUML_Goal, USECASEUML_UseCase, ScenarioDescription, Condition, Role, FunctionnelRequirement, NonFunctionnelRequirement, USECASEUML_Pre, USECASEUML_Post, USECASEUML_Role, USECASEUML_HumanRole, USECASEUML_SystemRole, USECASEUML_EventRole, USECASEUML_Manage, Resource, USECASEUML_Resource, USECASEUML_ScenarioDescription, USECASEUML_Condition},
    associations={scopes0, meet_by8, to_meet9, specifies1, scenario3, condition4, interacter5, specified_by6, scoped_by7, interacted_with11, managed_Resource13, useCase14, constrained_with16},
    generalizations={gen_USECASEUML_NonFunctionnelRequirement_Requirement, gen_USECASEUML_FunctionnelRequirement_Requirement, gen_USECASEUML_Pre_Condition, gen_USECASEUML_Post_Condition, gen_USECASEUML_HumanRole_Role, gen_USECASEUML_SystemRole_Role, gen_USECASEUML_EventRole_Role, gen_USECASEUML_Manage_UseCase},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)