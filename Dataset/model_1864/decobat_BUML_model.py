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
decobat_Project = Class(name="decobat::Project")
decobat_ProjectRevision = Class(name="decobat::ProjectRevision")
decobat_ProjectCategory = Class(name="decobat::ProjectCategory")
decobat_Plan = Class(name="decobat::Plan")
decobat_Customer = Class(name="decobat::Customer")
decobat_Library = Class(name="decobat::Library")
decobat_LibraryCategory = Class(name="decobat::LibraryCategory")
decobat_Product = Class(name="decobat::Product")
decobat_Supplier = Class(name="decobat::Supplier")
decobat_Level = Class(name="decobat::Level")
decobat_Object = Class(name="decobat::Object")
decobat_Service = Class(name="decobat::Service")

# decobat_Project class attributes and methods
decobat_Project_name: Property = Property(name="name", type=StringType)
decobat_Project_shortDescription: Property = Property(name="shortDescription", type=StringType)
decobat_Project_description: Property = Property(name="description", type=StringType)
decobat_Project_created: Property = Property(name="created", type=DateType)
decobat_Project_closed: Property = Property(name="closed", type=DateType)
decobat_Project.attributes={decobat_Project_shortDescription, decobat_Project_description, decobat_Project_name, decobat_Project_closed, decobat_Project_created}

# decobat_ProjectRevision class attributes and methods
decobat_ProjectRevision_shortDescription: Property = Property(name="shortDescription", type=StringType)
decobat_ProjectRevision_description: Property = Property(name="description", type=StringType)
decobat_ProjectRevision_update: Property = Property(name="update", type=DateType)
decobat_ProjectRevision_comment: Property = Property(name="comment", type=StringType)
decobat_ProjectRevision.attributes={decobat_ProjectRevision_update, decobat_ProjectRevision_description, decobat_ProjectRevision_comment, decobat_ProjectRevision_shortDescription}

# decobat_ProjectCategory class attributes and methods
decobat_ProjectCategory_name: Property = Property(name="name", type=StringType)
decobat_ProjectCategory_shortDescription: Property = Property(name="shortDescription", type=StringType)
decobat_ProjectCategory_description: Property = Property(name="description", type=StringType)
decobat_ProjectCategory_created: Property = Property(name="created", type=DateType)
decobat_ProjectCategory.attributes={decobat_ProjectCategory_description, decobat_ProjectCategory_shortDescription, decobat_ProjectCategory_name, decobat_ProjectCategory_created}

# decobat_Plan class attributes and methods
decobat_Plan_code: Property = Property(name="code", type=StringType)
decobat_Plan_name: Property = Property(name="name", type=StringType)
decobat_Plan_shortDescription: Property = Property(name="shortDescription", type=StringType)
decobat_Plan_description: Property = Property(name="description", type=StringType)
decobat_Plan.attributes={decobat_Plan_code, decobat_Plan_name, decobat_Plan_description, decobat_Plan_shortDescription}

# decobat_Customer class attributes and methods
decobat_Customer_code: Property = Property(name="code", type=StringType)
decobat_Customer_name: Property = Property(name="name", type=StringType)
decobat_Customer_address: Property = Property(name="address", type=StringType)
decobat_Customer_zip: Property = Property(name="zip", type=StringType)
decobat_Customer_city: Property = Property(name="city", type=StringType)
decobat_Customer_country: Property = Property(name="country", type=StringType)
decobat_Customer_fax: Property = Property(name="fax", type=StringType)
decobat_Customer_phone: Property = Property(name="phone", type=StringType)
decobat_Customer_email: Property = Property(name="email", type=StringType)
decobat_Customer.attributes={decobat_Customer_address, decobat_Customer_phone, decobat_Customer_email, decobat_Customer_code, decobat_Customer_zip, decobat_Customer_fax, decobat_Customer_country, decobat_Customer_city, decobat_Customer_name}

# decobat_Library class attributes and methods
decobat_Library_name: Property = Property(name="name", type=StringType)
decobat_Library_shortDescription: Property = Property(name="shortDescription", type=StringType)
decobat_Library_description: Property = Property(name="description", type=StringType)
decobat_Library_created: Property = Property(name="created", type=DateType)
decobat_Library_update: Property = Property(name="update", type=DateType)
decobat_Library_height: Property = Property(name="height", type=StringType)
decobat_Library_width: Property = Property(name="width", type=StringType)
decobat_Library_depth: Property = Property(name="depth", type=StringType)
decobat_Library.attributes={decobat_Library_description, decobat_Library_name, decobat_Library_width, decobat_Library_height, decobat_Library_shortDescription, decobat_Library_created, decobat_Library_update, decobat_Library_depth}

# decobat_LibraryCategory class attributes and methods
decobat_LibraryCategory_name: Property = Property(name="name", type=StringType)
decobat_LibraryCategory_shortDescription: Property = Property(name="shortDescription", type=StringType)
decobat_LibraryCategory_description: Property = Property(name="description", type=StringType)
decobat_LibraryCategory_created: Property = Property(name="created", type=DateType)
decobat_LibraryCategory.attributes={decobat_LibraryCategory_name, decobat_LibraryCategory_shortDescription, decobat_LibraryCategory_description, decobat_LibraryCategory_created}

# decobat_Product class attributes and methods
decobat_Product_name: Property = Property(name="name", type=StringType)
decobat_Product_shortDescription: Property = Property(name="shortDescription", type=StringType)
decobat_Product_description: Property = Property(name="description", type=StringType)
decobat_Product_created: Property = Property(name="created", type=DateType)
decobat_Product_update: Property = Property(name="update", type=DateType)
decobat_Product_unitCostPrice: Property = Property(name="unitCostPrice", type=StringType)
decobat_Product_unitBilledPrice: Property = Property(name="unitBilledPrice", type=StringType)
decobat_Product_unitWeight: Property = Property(name="unitWeight", type=StringType)
decobat_Product_height: Property = Property(name="height", type=StringType)
decobat_Product_width: Property = Property(name="width", type=StringType)
decobat_Product_depth: Property = Property(name="depth", type=StringType)
decobat_Product.attributes={decobat_Product_width, decobat_Product_name, decobat_Product_unitBilledPrice, decobat_Product_depth, decobat_Product_description, decobat_Product_shortDescription, decobat_Product_height, decobat_Product_unitCostPrice, decobat_Product_unitWeight, decobat_Product_created, decobat_Product_update}

# decobat_Supplier class attributes and methods
decobat_Supplier_code: Property = Property(name="code", type=StringType)
decobat_Supplier_name: Property = Property(name="name", type=StringType)
decobat_Supplier_address: Property = Property(name="address", type=StringType)
decobat_Supplier_zip: Property = Property(name="zip", type=StringType)
decobat_Supplier_city: Property = Property(name="city", type=StringType)
decobat_Supplier_country: Property = Property(name="country", type=StringType)
decobat_Supplier_fax: Property = Property(name="fax", type=StringType)
decobat_Supplier_phone: Property = Property(name="phone", type=StringType)
decobat_Supplier_email: Property = Property(name="email", type=StringType)
decobat_Supplier.attributes={decobat_Supplier_address, decobat_Supplier_phone, decobat_Supplier_name, decobat_Supplier_zip, decobat_Supplier_fax, decobat_Supplier_code, decobat_Supplier_country, decobat_Supplier_city, decobat_Supplier_email}

# decobat_Level class attributes and methods
decobat_Level_code: Property = Property(name="code", type=StringType)
decobat_Level_name: Property = Property(name="name", type=StringType)
decobat_Level_shortDescription: Property = Property(name="shortDescription", type=StringType)
decobat_Level_description: Property = Property(name="description", type=StringType)
decobat_Level.attributes={decobat_Level_description, decobat_Level_shortDescription, decobat_Level_code, decobat_Level_name}

# decobat_Object class attributes and methods
decobat_Object_code: Property = Property(name="code", type=StringType)
decobat_Object_name: Property = Property(name="name", type=StringType)
decobat_Object_shortDescription: Property = Property(name="shortDescription", type=StringType)
decobat_Object_description: Property = Property(name="description", type=StringType)
decobat_Object.attributes={decobat_Object_code, decobat_Object_name, decobat_Object_shortDescription, decobat_Object_description}

# decobat_Service class attributes and methods
decobat_Service_code: Property = Property(name="code", type=StringType)
decobat_Service_name: Property = Property(name="name", type=StringType)
decobat_Service_shortDescription: Property = Property(name="shortDescription", type=StringType)
decobat_Service_description: Property = Property(name="description", type=StringType)
decobat_Service_hourlyCostPrice: Property = Property(name="hourlyCostPrice", type=StringType)
decobat_Service_hourlyBilledPrice: Property = Property(name="hourlyBilledPrice", type=StringType)
decobat_Service.attributes={decobat_Service_description, decobat_Service_hourlyBilledPrice, decobat_Service_shortDescription, decobat_Service_code, decobat_Service_name, decobat_Service_hourlyCostPrice}

# Relationships
projectRevisions0: BinaryAssociation = BinaryAssociation(
    name="projectRevisions0",
    ends={
        Property(name="decobat_ProjectRevision", type=decobat_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="decobat_Project", type=decobat_ProjectRevision, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
projectCategories1: BinaryAssociation = BinaryAssociation(
    name="projectCategories1",
    ends={
        Property(name="decobat_ProjectCategory", type=decobat_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="decobat_Project2", type=decobat_ProjectCategory, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
plans3: BinaryAssociation = BinaryAssociation(
    name="plans3",
    ends={
        Property(name="decobat_Plan", type=decobat_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="decobat_Project4", type=decobat_Plan, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
customer5: BinaryAssociation = BinaryAssociation(
    name="customer5",
    ends={
        Property(name="decobat_Customer", type=decobat_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="decobat_Project6", type=decobat_Customer, multiplicity=Multiplicity(1, 1))
    }
)
categories7: BinaryAssociation = BinaryAssociation(
    name="categories7",
    ends={
        Property(name="decobat_LibraryCategory", type=decobat_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="decobat_Library", type=decobat_LibraryCategory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supplier8: BinaryAssociation = BinaryAssociation(
    name="supplier8",
    ends={
        Property(name="decobat_Supplier", type=decobat_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="decobat_Product", type=decobat_Supplier, multiplicity=Multiplicity(1, 1))
    }
)
levels9: BinaryAssociation = BinaryAssociation(
    name="levels9",
    ends={
        Property(name="decobat_Level", type=decobat_Plan, multiplicity=Multiplicity(1, 1)),
        Property(name="decobat_Plan10", type=decobat_Level, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
libraryItems11: BinaryAssociation = BinaryAssociation(
    name="libraryItems11",
    ends={
        Property(name="decobat_Library13", type=decobat_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="decobat_Level12", type=decobat_Library, multiplicity=Multiplicity(0, 9999))
    }
)
libraryItems14: BinaryAssociation = BinaryAssociation(
    name="libraryItems14",
    ends={
        Property(name="decobat_Library15", type=decobat_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="decobat_Object", type=decobat_Library, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="decobat",
    types={decobat_Project, decobat_ProjectRevision, decobat_ProjectCategory, decobat_Plan, decobat_Customer, decobat_Library, decobat_LibraryCategory, decobat_Product, decobat_Supplier, decobat_Level, decobat_Object, decobat_Service},
    associations={projectRevisions0, projectCategories1, plans3, customer5, categories7, supplier8, levels9, libraryItems11, libraryItems14},
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