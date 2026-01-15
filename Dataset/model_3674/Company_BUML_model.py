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
Company_Project = Class(name="Company::Project")
Company_Unit = Class(name="Company::Unit")
Company_Organisation = Class(name="Company::Organisation")
Company_Person = Class(name="Company::Person", is_abstract=True)
Company_CompanyModel = Class(name="Company::CompanyModel")
Company_Employee = Class(name="Company::Employee")
Company_Division = Class(name="Company::Division", is_abstract=True)
Person = Class(name="Person")
Company_Topic = Class(name="Company::Topic")
Company_Category = Class(name="Company::Category")
Company_Client = Class(name="Company::Client")
Division = Class(name="Division")
Company_ServiceLine = Class(name="Company::ServiceLine")

# Company_Project class attributes and methods
Company_Project_name: Property = Property(name="name", type=StringType)
Company_Project_budget: Property = Property(name="budget", type=IntegerType)
Company_Project.attributes={Company_Project_budget, Company_Project_name}

# Company_Unit class attributes and methods

# Company_Organisation class attributes and methods
Company_Organisation_name: Property = Property(name="name", type=StringType)
Company_Organisation_city: Property = Property(name="city", type=StringType)
Company_Organisation_completeAddress: Property = Property(name="completeAddress", type=StringType)
Company_Organisation.attributes={Company_Organisation_name, Company_Organisation_city, Company_Organisation_completeAddress}

# Company_Person class attributes and methods
Company_Person_fullName: Property = Property(name="fullName", type=StringType)
Company_Person.attributes={Company_Person_fullName}

# Company_CompanyModel class attributes and methods

# Company_Employee class attributes and methods

# Company_Division class attributes and methods
Company_Division_name: Property = Property(name="name", type=StringType)
Company_Division.attributes={Company_Division_name}

# Person class attributes and methods

# Company_Topic class attributes and methods
Company_Topic_id: Property = Property(name="id", type=StringType)
Company_Topic.attributes={Company_Topic_id}

# Company_Category class attributes and methods
Company_Category_name: Property = Property(name="name", type=StringType)
Company_Category.attributes={Company_Category_name}

# Company_Client class attributes and methods

# Division class attributes and methods

# Company_ServiceLine class attributes and methods

# Relationships
assignedTo0: BinaryAssociation = BinaryAssociation(
    name="assignedTo0",
    ends={
        Property(name="Company_Project", type=Company_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_Person", type=Company_Project, multiplicity=Multiplicity(0, 9999))
    }
)
employed1: BinaryAssociation = BinaryAssociation(
    name="employed1",
    ends={
        Property(name="Company_Unit", type=Company_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_Person2", type=Company_Unit, multiplicity=Multiplicity(0, 1))
    }
)
persons3: BinaryAssociation = BinaryAssociation(
    name="persons3",
    ends={
        Property(name="Company_Person4", type=Company_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_Organisation", type=Company_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topics12: BinaryAssociation = BinaryAssociation(
    name="topics12",
    ends={
        Property(name="Topic", type=Company_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=Company_Topic, multiplicity=Multiplicity(0, 9999))
    }
)
category13: BinaryAssociation = BinaryAssociation(
    name="category13",
    ends={
        Property(name="Category", type=Company_Topic, multiplicity=Multiplicity(1, 1)),
        Property(name="topics", type=Company_Category, multiplicity=Multiplicity(1, 1))
    }
)
company14: BinaryAssociation = BinaryAssociation(
    name="company14",
    ends={
        Property(name="Company_Organisation15", type=Company_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_CompanyModel", type=Company_Organisation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
categories16: BinaryAssociation = BinaryAssociation(
    name="categories16",
    ends={
        Property(name="Company_Category", type=Company_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_CompanyModel17", type=Company_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topics18: BinaryAssociation = BinaryAssociation(
    name="topics18",
    ends={
        Property(name="Company_Topic20", type=Company_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_CompanyModel19", type=Company_Topic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projects5: BinaryAssociation = BinaryAssociation(
    name="projects5",
    ends={
        Property(name="Company_Project7", type=Company_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_Organisation6", type=Company_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
division21: BinaryAssociation = BinaryAssociation(
    name="division21",
    ends={
        Property(name="Company_Division23", type=Company_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_CompanyModel22", type=Company_Division, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lines8: BinaryAssociation = BinaryAssociation(
    name="lines8",
    ends={
        Property(name="Company_Division", type=Company_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_Organisation9", type=Company_Division, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
related10: BinaryAssociation = BinaryAssociation(
    name="related10",
    ends={
        Property(name="Company_Topic", type=Company_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_Project11", type=Company_Topic, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Company_Employee_Person = Generalization(general=Person, specific=Company_Employee)
gen_Company_Client_Person = Generalization(general=Person, specific=Company_Client)
gen_Company_Unit_Division = Generalization(general=Division, specific=Company_Unit)
gen_Company_ServiceLine_Division = Generalization(general=Division, specific=Company_ServiceLine)

# Domain Model
domain_model = DomainModel(
    name="Company",
    types={Company_Project, Company_Unit, Company_Organisation, Company_Person, Company_CompanyModel, Company_Employee, Company_Division, Person, Company_Topic, Company_Category, Company_Client, Division, Company_ServiceLine},
    associations={assignedTo0, employed1, persons3, topics12, category13, company14, categories16, topics18, projects5, division21, lines8, related10},
    generalizations={gen_Company_Employee_Person, gen_Company_Client_Person, gen_Company_Unit_Division, gen_Company_ServiceLine_Division},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)