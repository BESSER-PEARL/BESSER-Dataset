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
Organization_Employee = Class(name="Organization::Employee")
Organization_Skill = Class(name="Organization::Skill")

# Organization_Employee class attributes and methods
Organization_Employee_Name: Property = Property(name="Name", type=StringType)
Organization_Employee_EmpID: Property = Property(name="EmpID", type=StringType)
Organization_Employee_Address: Property = Property(name="Address", type=StringType)
Organization_Employee.attributes={Organization_Employee_Name, Organization_Employee_Address, Organization_Employee_EmpID}

# Organization_Skill class attributes and methods
Organization_Skill_Name: Property = Property(name="Name", type=StringType)
Organization_Skill.attributes={Organization_Skill_Name}

# Relationships
Skills0: BinaryAssociation = BinaryAssociation(
    name="Skills0",
    ends={
        Property(name="Organization_Skill", type=Organization_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Organization_Employee", type=Organization_Skill, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Organization",
    types={Organization_Employee, Organization_Skill},
    associations={Skills0},
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