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

# Enumerations
ConstraintType: Enumeration = Enumeration(
    name="ConstraintType",
    literals={
            EnumerationLiteral(name="Minimum"),
			EnumerationLiteral(name="Maximum"),
			EnumerationLiteral(name="Average")
    }
)

ConstraintOperation: Enumeration = Enumeration(
    name="ConstraintOperation",
    literals={
            EnumerationLiteral(name="Less"),
			EnumerationLiteral(name="LessOrEqual"),
			EnumerationLiteral(name="Equal"),
			EnumerationLiteral(name="GreaterOrEqual"),
			EnumerationLiteral(name="Greater")
    }
)

ResourceTypes: Enumeration = Enumeration(
    name="ResourceTypes",
    literals={
            EnumerationLiteral(name="cpu"),
			EnumerationLiteral(name="memory"),
			EnumerationLiteral(name="bandwidth"),
			EnumerationLiteral(name="power"),
			EnumerationLiteral(name="port")
    }
)

# Classes
profile_PlatformProfile = Class(name="profile::PlatformProfile")
profile_Resource = Class(name="profile::Resource")
profile_Constraint = Class(name="profile::Constraint")

# profile_PlatformProfile class attributes and methods
profile_PlatformProfile_name: Property = Property(name="name", type=StringType)
profile_PlatformProfile.attributes={profile_PlatformProfile_name}

# profile_Resource class attributes and methods
profile_Resource_name: Property = Property(name="name", type=StringType)
profile_Resource_type: Property = Property(name="type", type=StringType)
profile_Resource.attributes={profile_Resource_name, profile_Resource_type}

# profile_Constraint class attributes and methods
profile_Constraint_isDerivation: Property = Property(name="isDerivation", type=BooleanType)
profile_Constraint_type: Property = Property(name="type", type=StringType)
profile_Constraint_operation: Property = Property(name="operation", type=StringType)
profile_Constraint_bound: Property = Property(name="bound", type=IntegerType)
profile_Constraint.attributes={profile_Constraint_type, profile_Constraint_operation, profile_Constraint_isDerivation, profile_Constraint_bound}

# Relationships
resources0: BinaryAssociation = BinaryAssociation(
    name="resources0",
    ends={
        Property(name="Resource", type=profile_PlatformProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="platform", type=profile_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints1: BinaryAssociation = BinaryAssociation(
    name="constraints1",
    ends={
        Property(name="Constraint", type=profile_PlatformProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="platform2", type=profile_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
platform3: BinaryAssociation = BinaryAssociation(
    name="platform3",
    ends={
        Property(name="PlatformProfile", type=profile_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="resources", type=profile_PlatformProfile, multiplicity=Multiplicity(1, 1))
    }
)
platform4: BinaryAssociation = BinaryAssociation(
    name="platform4",
    ends={
        Property(name="PlatformProfile5", type=profile_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=profile_PlatformProfile, multiplicity=Multiplicity(1, 1))
    }
)
references6: BinaryAssociation = BinaryAssociation(
    name="references6",
    ends={
        Property(name="profile_Resource", type=profile_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_Constraint", type=profile_Resource, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="profile",
    types={profile_PlatformProfile, profile_Resource, profile_Constraint, ConstraintType, ConstraintOperation, ResourceTypes},
    associations={resources0, constraints1, platform3, platform4, references6},
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