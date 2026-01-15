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
EvoCompany_Person = Class(name="EvoCompany::Person", is_abstract=True)
EvoCompany_Project = Class(name="EvoCompany::Project")
EvoCompany_Unit = Class(name="EvoCompany::Unit")
EvoCompany_Organisation = Class(name="EvoCompany::Organisation")
EvoCompany_CompanyModel = Class(name="EvoCompany::CompanyModel")
EvoCompany_Employee = Class(name="EvoCompany::Employee")
Person = Class(name="Person")
EvoCompany_Client = Class(name="EvoCompany::Client")
Division = Class(name="Division")
EvoCompany_ServiceLine = Class(name="EvoCompany::ServiceLine")
EvoCompany_Division = Class(name="EvoCompany::Division", is_abstract=True)
EvoCompany_Topic = Class(name="EvoCompany::Topic")
EvoCompany_Category = Class(name="EvoCompany::Category")

# EvoCompany_Person class attributes and methods
EvoCompany_Person_fullName: Property = Property(name="fullName", type=StringType)
EvoCompany_Person.attributes={EvoCompany_Person_fullName}

# EvoCompany_Project class attributes and methods
EvoCompany_Project_name: Property = Property(name="name", type=StringType)
EvoCompany_Project_budget: Property = Property(name="budget", type=IntegerType)
EvoCompany_Project.attributes={EvoCompany_Project_budget, EvoCompany_Project_name}

# EvoCompany_Unit class attributes and methods

# EvoCompany_Organisation class attributes and methods
EvoCompany_Organisation_name: Property = Property(name="name", type=StringType)
EvoCompany_Organisation_city: Property = Property(name="city", type=StringType)
EvoCompany_Organisation_completeAddress: Property = Property(name="completeAddress", type=StringType)
EvoCompany_Organisation.attributes={EvoCompany_Organisation_completeAddress, EvoCompany_Organisation_name, EvoCompany_Organisation_city}

# EvoCompany_CompanyModel class attributes and methods

# EvoCompany_Employee class attributes and methods

# Person class attributes and methods

# EvoCompany_Client class attributes and methods

# Division class attributes and methods

# EvoCompany_ServiceLine class attributes and methods

# EvoCompany_Division class attributes and methods
EvoCompany_Division_name: Property = Property(name="name", type=StringType)
EvoCompany_Division.attributes={EvoCompany_Division_name}

# EvoCompany_Topic class attributes and methods
EvoCompany_Topic_id: Property = Property(name="id", type=StringType)
EvoCompany_Topic.attributes={EvoCompany_Topic_id}

# EvoCompany_Category class attributes and methods
EvoCompany_Category_name: Property = Property(name="name", type=StringType)
EvoCompany_Category.attributes={EvoCompany_Category_name}

# Relationships
assignedTo0: BinaryAssociation = BinaryAssociation(
    name="assignedTo0",
    ends={
        Property(name="EvoCompany_Project", type=EvoCompany_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="EvoCompany_Person", type=EvoCompany_Project, multiplicity=Multiplicity(0, 9999))
    }
)
employed1: BinaryAssociation = BinaryAssociation(
    name="employed1",
    ends={
        Property(name="EvoCompany_Unit", type=EvoCompany_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="EvoCompany_Person2", type=EvoCompany_Unit, multiplicity=Multiplicity(0, 1))
    }
)
persons3: BinaryAssociation = BinaryAssociation(
    name="persons3",
    ends={
        Property(name="EvoCompany_Person4", type=EvoCompany_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="EvoCompany_Organisation", type=EvoCompany_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projects5: BinaryAssociation = BinaryAssociation(
    name="projects5",
    ends={
        Property(name="EvoCompany_Project7", type=EvoCompany_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="EvoCompany_Organisation6", type=EvoCompany_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
company14: BinaryAssociation = BinaryAssociation(
    name="company14",
    ends={
        Property(name="EvoCompany_Organisation15", type=EvoCompany_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="EvoCompany_CompanyModel", type=EvoCompany_Organisation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
categories16: BinaryAssociation = BinaryAssociation(
    name="categories16",
    ends={
        Property(name="EvoCompany_Category", type=EvoCompany_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="EvoCompany_CompanyModel17", type=EvoCompany_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topics18: BinaryAssociation = BinaryAssociation(
    name="topics18",
    ends={
        Property(name="EvoCompany_Topic20", type=EvoCompany_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="EvoCompany_CompanyModel19", type=EvoCompany_Topic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
division21: BinaryAssociation = BinaryAssociation(
    name="division21",
    ends={
        Property(name="EvoCompany_Division23", type=EvoCompany_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="EvoCompany_CompanyModel22", type=EvoCompany_Division, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lines8: BinaryAssociation = BinaryAssociation(
    name="lines8",
    ends={
        Property(name="EvoCompany_Division", type=EvoCompany_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="EvoCompany_Organisation9", type=EvoCompany_Division, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
related10: BinaryAssociation = BinaryAssociation(
    name="related10",
    ends={
        Property(name="EvoCompany_Topic", type=EvoCompany_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="EvoCompany_Project11", type=EvoCompany_Topic, multiplicity=Multiplicity(1, 1))
    }
)
topics12: BinaryAssociation = BinaryAssociation(
    name="topics12",
    ends={
        Property(name="Topic", type=EvoCompany_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=EvoCompany_Topic, multiplicity=Multiplicity(0, 9999))
    }
)
category13: BinaryAssociation = BinaryAssociation(
    name="category13",
    ends={
        Property(name="Category", type=EvoCompany_Topic, multiplicity=Multiplicity(1, 1)),
        Property(name="topics", type=EvoCompany_Category, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_EvoCompany_Employee_Person = Generalization(general=Person, specific=EvoCompany_Employee)
gen_EvoCompany_Client_Person = Generalization(general=Person, specific=EvoCompany_Client)
gen_EvoCompany_Unit_Division = Generalization(general=Division, specific=EvoCompany_Unit)
gen_EvoCompany_ServiceLine_Division = Generalization(general=Division, specific=EvoCompany_ServiceLine)

# Domain Model
domain_model = DomainModel(
    name="EvoCompany",
    types={EvoCompany_Person, EvoCompany_Project, EvoCompany_Unit, EvoCompany_Organisation, EvoCompany_CompanyModel, EvoCompany_Employee, Person, EvoCompany_Client, Division, EvoCompany_ServiceLine, EvoCompany_Division, EvoCompany_Topic, EvoCompany_Category},
    associations={assignedTo0, employed1, persons3, projects5, company14, categories16, topics18, division21, lines8, related10, topics12, category13},
    generalizations={gen_EvoCompany_Employee_Person, gen_EvoCompany_Client_Person, gen_EvoCompany_Unit_Division, gen_EvoCompany_ServiceLine_Division},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)