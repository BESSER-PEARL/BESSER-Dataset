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
RequirementType: Enumeration = Enumeration(
    name="RequirementType",
    literals={
            EnumerationLiteral(name="functional"),
			EnumerationLiteral(name="technical")
    }
)

# Classes
requirement_Repository = Class(name="requirement_Repository")
NamedElement = Class(name="NamedElement")
requirement_Category = Class(name="requirement_Category")
requirement_EObject = Class(name="requirement_EObject")
requirement_Requirement = Class(name="requirement_Requirement")
requirement_NamedElement = Class(name="requirement_NamedElement", is_abstract=True)

# requirement_Repository class attributes and methods

# NamedElement class attributes and methods

# requirement_Category class attributes and methods
requirement_Category_id: Property = Property(name="id", type=StringType)
requirement_Category.attributes={requirement_Category_id}

# requirement_EObject class attributes and methods

# requirement_Requirement class attributes and methods
requirement_Requirement_id: Property = Property(name="id", type=StringType)
requirement_Requirement_status: Property = Property(name="status", type=StringType)
requirement_Requirement_createdOn: Property = Property(name="createdOn", type=DateType)
requirement_Requirement_modifiedOn: Property = Property(name="modifiedOn", type=DateType)
requirement_Requirement_version: Property = Property(name="version", type=IntegerType)
requirement_Requirement_statement: Property = Property(name="statement", type=StringType)
requirement_Requirement_rationale: Property = Property(name="rationale", type=StringType)
requirement_Requirement_acceptanceCriteria: Property = Property(name="acceptanceCriteria", type=StringType)
requirement_Requirement_type: Property = Property(name="type", type=StringType)
requirement_Requirement_subtype: Property = Property(name="subtype", type=StringType)
requirement_Requirement.attributes={requirement_Requirement_modifiedOn, requirement_Requirement_rationale, requirement_Requirement_acceptanceCriteria, requirement_Requirement_statement, requirement_Requirement_type, requirement_Requirement_version, requirement_Requirement_subtype, requirement_Requirement_createdOn, requirement_Requirement_status, requirement_Requirement_id}

# requirement_NamedElement class attributes and methods
requirement_NamedElement_name: Property = Property(name="name", type=StringType)
requirement_NamedElement.attributes={requirement_NamedElement_name}

# Relationships
mainCategories0: BinaryAssociation = BinaryAssociation(
    name="mainCategories0",
    ends={
        Property(name="Category", type=requirement_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="repository", type=requirement_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedObject1: BinaryAssociation = BinaryAssociation(
    name="referencedObject1",
    ends={
        Property(name="requirement_EObject", type=requirement_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_Repository", type=requirement_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
repository6: BinaryAssociation = BinaryAssociation(
    name="repository6",
    ends={
        Property(name="Repository", type=requirement_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="mainCategories", type=requirement_Repository, multiplicity=Multiplicity(0, 1))
    }
)
parentCategory8: BinaryAssociation = BinaryAssociation(
    name="parentCategory8",
    ends={
        Property(name="Category9", type=requirement_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="subCategories", type=requirement_Category, multiplicity=Multiplicity(0, 1))
    }
)
referencedObject10: BinaryAssociation = BinaryAssociation(
    name="referencedObject10",
    ends={
        Property(name="requirement_EObject11", type=requirement_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_Category", type=requirement_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
requirements2: BinaryAssociation = BinaryAssociation(
    name="requirements2",
    ends={
        Property(name="Requirement", type=requirement_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=requirement_Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subCategories4: BinaryAssociation = BinaryAssociation(
    name="subCategories4",
    ends={
        Property(name="Category5", type=requirement_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="parentCategory", type=requirement_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedObject12: BinaryAssociation = BinaryAssociation(
    name="referencedObject12",
    ends={
        Property(name="requirement_EObject13", type=requirement_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_Requirement", type=requirement_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
category14: BinaryAssociation = BinaryAssociation(
    name="category14",
    ends={
        Property(name="Category15", type=requirement_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements", type=requirement_Category, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_requirement_Repository_NamedElement = Generalization(general=NamedElement, specific=requirement_Repository)
gen_requirement_Requirement_NamedElement = Generalization(general=NamedElement, specific=requirement_Requirement)
gen_requirement_Category_NamedElement = Generalization(general=NamedElement, specific=requirement_Category)

# Domain Model
domain_model = DomainModel(
    name="requirement",
    types={requirement_Repository, NamedElement, requirement_Category, requirement_EObject, requirement_Requirement, requirement_NamedElement, RequirementType},
    associations={mainCategories0, referencedObject1, repository6, parentCategory8, referencedObject10, requirements2, subCategories4, referencedObject12, category14},
    generalizations={gen_requirement_Repository_NamedElement, gen_requirement_Requirement_NamedElement, gen_requirement_Category_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)