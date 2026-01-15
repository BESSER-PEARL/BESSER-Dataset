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
type: Enumeration = Enumeration(
    name="type",
    literals={
            EnumerationLiteral(name="employee"),
			EnumerationLiteral(name="client")
    }
)

# Classes
Company_Person = Class(name="Company::Person")
Company_Project = Class(name="Company::Project", is_abstract=True)
Company_ServiceLine = Class(name="Company::ServiceLine")
Company_Company = Class(name="Company::Company")
Company_Category = Class(name="Company::Category")
Company_European = Class(name="Company::European")
Project = Class(name="Project")
Company_National = Class(name="Company::National")
Company_Topic = Class(name="Company::Topic")
Company_Address = Class(name="Company::Address")
Company_Division = Class(name="Company::Division", is_abstract=True)
Company_CompanyModel = Class(name="Company::CompanyModel")
Company_Unit = Class(name="Company::Unit")
Division = Class(name="Division")

# Company_Person class attributes and methods
Company_Person_firstname: Property = Property(name="firstname", type=StringType)
Company_Person_lastname: Property = Property(name="lastname", type=StringType)
Company_Person_position: Property = Property(name="position", type=StringType)
Company_Person.attributes={Company_Person_position, Company_Person_firstname, Company_Person_lastname}

# Company_Project class attributes and methods
Company_Project_name: Property = Property(name="name", type=StringType)
Company_Project.attributes={Company_Project_name}

# Company_ServiceLine class attributes and methods

# Company_Company class attributes and methods
Company_Company_name: Property = Property(name="name", type=StringType)
Company_Company.attributes={Company_Company_name}

# Company_Category class attributes and methods
Company_Category_name: Property = Property(name="name", type=StringType)
Company_Category.attributes={Company_Category_name}

# Company_European class attributes and methods
Company_European_budget: Property = Property(name="budget", type=IntegerType)
Company_European.attributes={Company_European_budget}

# Project class attributes and methods

# Company_National class attributes and methods
Company_National_budget: Property = Property(name="budget", type=IntegerType)
Company_National.attributes={Company_National_budget}

# Company_Topic class attributes and methods
Company_Topic_id: Property = Property(name="id", type=StringType)
Company_Topic.attributes={Company_Topic_id}

# Company_Address class attributes and methods
Company_Address_city: Property = Property(name="city", type=StringType)
Company_Address_completeAddress: Property = Property(name="completeAddress", type=StringType)
Company_Address.attributes={Company_Address_completeAddress, Company_Address_city}

# Company_Division class attributes and methods
Company_Division_name: Property = Property(name="name", type=StringType)
Company_Division.attributes={Company_Division_name}

# Company_CompanyModel class attributes and methods

# Company_Unit class attributes and methods

# Division class attributes and methods

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
        Property(name="Company_ServiceLine", type=Company_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_Person2", type=Company_ServiceLine, multiplicity=Multiplicity(0, 1))
    }
)
persons3: BinaryAssociation = BinaryAssociation(
    name="persons3",
    ends={
        Property(name="Company_Person4", type=Company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_Company", type=Company_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projects5: BinaryAssociation = BinaryAssociation(
    name="projects5",
    ends={
        Property(name="Company_Project7", type=Company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_Company6", type=Company_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lines10: BinaryAssociation = BinaryAssociation(
    name="lines10",
    ends={
        Property(name="Company_Division", type=Company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_Company11", type=Company_Division, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
related12: BinaryAssociation = BinaryAssociation(
    name="related12",
    ends={
        Property(name="Company_Category", type=Company_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_Project13", type=Company_Category, multiplicity=Multiplicity(1, 1))
    }
)
topics14: BinaryAssociation = BinaryAssociation(
    name="topics14",
    ends={
        Property(name="Topic", type=Company_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=Company_Topic, multiplicity=Multiplicity(0, 9999))
    }
)
address8: BinaryAssociation = BinaryAssociation(
    name="address8",
    ends={
        Property(name="Company_Address", type=Company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_Company9", type=Company_Address, multiplicity=Multiplicity(0, 1))
    }
)
company16: BinaryAssociation = BinaryAssociation(
    name="company16",
    ends={
        Property(name="Company_Company17", type=Company_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_CompanyModel", type=Company_Company, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
categories18: BinaryAssociation = BinaryAssociation(
    name="categories18",
    ends={
        Property(name="Company_Category20", type=Company_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_CompanyModel19", type=Company_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topics21: BinaryAssociation = BinaryAssociation(
    name="topics21",
    ends={
        Property(name="Company_Topic", type=Company_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_CompanyModel22", type=Company_Topic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address23: BinaryAssociation = BinaryAssociation(
    name="address23",
    ends={
        Property(name="Company_Address25", type=Company_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_CompanyModel24", type=Company_Address, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
division26: BinaryAssociation = BinaryAssociation(
    name="division26",
    ends={
        Property(name="Company_Division28", type=Company_CompanyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Company_CompanyModel27", type=Company_Division, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
category15: BinaryAssociation = BinaryAssociation(
    name="category15",
    ends={
        Property(name="Category", type=Company_Topic, multiplicity=Multiplicity(1, 1)),
        Property(name="topics", type=Company_Category, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Company_European_Project = Generalization(general=Project, specific=Company_European)
gen_Company_National_Project = Generalization(general=Project, specific=Company_National)
gen_Company_Unit_Division = Generalization(general=Division, specific=Company_Unit)
gen_Company_ServiceLine_Division = Generalization(general=Division, specific=Company_ServiceLine)

# Domain Model
domain_model = DomainModel(
    name="Company",
    types={Company_Person, Company_Project, Company_ServiceLine, Company_Company, Company_Category, Company_European, Project, Company_National, Company_Topic, Company_Address, Company_Division, Company_CompanyModel, Company_Unit, Division, type},
    associations={assignedTo0, employed1, persons3, projects5, lines10, related12, topics14, address8, company16, categories18, topics21, address23, division26, category15},
    generalizations={gen_Company_European_Project, gen_Company_National_Project, gen_Company_Unit_Division, gen_Company_ServiceLine_Division},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)