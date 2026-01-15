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
household_Family = Class(name="household::Family")
household_Member = Class(name="household::Member")

# household_Family class attributes and methods
household_Family_name: Property = Property(name="name", type=StringType)
household_Family.attributes={household_Family_name}

# household_Member class attributes and methods
household_Member_name: Property = Property(name="name", type=StringType)
household_Member.attributes={household_Member_name}

# Relationships
son1: BinaryAssociation = BinaryAssociation(
    name="son1",
    ends={
        Property(name="household_Member3", type=household_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="household_Family2", type=household_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughter4: BinaryAssociation = BinaryAssociation(
    name="daughter4",
    ends={
        Property(name="household_Member6", type=household_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="household_Family5", type=household_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mother0: BinaryAssociation = BinaryAssociation(
    name="mother0",
    ends={
        Property(name="household_Member", type=household_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="household_Family", type=household_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
father7: BinaryAssociation = BinaryAssociation(
    name="father7",
    ends={
        Property(name="household_Member9", type=household_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="household_Family8", type=household_Member, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="household",
    types={household_Family, household_Member},
    associations={son1, daughter4, mother0, father7},
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