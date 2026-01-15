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
sample_Company = Class(name="sample::Company")
sample_Department = Class(name="sample::Department")
sample_Group = Class(name="sample::Group")
sample_Person = Class(name="sample::Person")

# sample_Company class attributes and methods
sample_Company_name: Property = Property(name="name", type=StringType)
sample_Company.attributes={sample_Company_name}

# sample_Department class attributes and methods
sample_Department_name: Property = Property(name="name", type=StringType)
sample_Department.attributes={sample_Department_name}

# sample_Group class attributes and methods
sample_Group_name: Property = Property(name="name", type=StringType)
sample_Group.attributes={sample_Group_name}

# sample_Person class attributes and methods
sample_Person_name: Property = Property(name="name", type=StringType)
sample_Person_birthdate: Property = Property(name="birthdate", type=DateType)
sample_Person.attributes={sample_Person_name, sample_Person_birthdate}

# Relationships
departments0: BinaryAssociation = BinaryAssociation(
    name="departments0",
    ends={
        Property(name="Department", type=sample_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company", type=sample_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups1: BinaryAssociation = BinaryAssociation(
    name="groups1",
    ends={
        Property(name="Group", type=sample_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=sample_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
company2: BinaryAssociation = BinaryAssociation(
    name="company2",
    ends={
        Property(name="Company", type=sample_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="departments", type=sample_Company, multiplicity=Multiplicity(0, 1))
    }
)
persons3: BinaryAssociation = BinaryAssociation(
    name="persons3",
    ends={
        Property(name="Person", type=sample_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=sample_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
department4: BinaryAssociation = BinaryAssociation(
    name="department4",
    ends={
        Property(name="Department5", type=sample_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=sample_Department, multiplicity=Multiplicity(0, 1))
    }
)
group6: BinaryAssociation = BinaryAssociation(
    name="group6",
    ends={
        Property(name="Group7", type=sample_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons", type=sample_Group, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sample",
    types={sample_Company, sample_Department, sample_Group, sample_Person},
    associations={departments0, groups1, company2, persons3, department4, group6},
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