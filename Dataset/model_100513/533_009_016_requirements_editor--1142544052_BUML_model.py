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
BinaryOperator: Enumeration = Enumeration(
    name="BinaryOperator",
    literals={
            EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="AND")
    }
)

# Classes
requirements_editor_Requirement = Class(name="requirements_editor_Requirement", is_abstract=True)
requirements_editor_Description = Class(name="requirements_editor_Description", is_abstract=True)
requirements_editor_Person = Class(name="requirements_editor_Person")
requirements_editor_Dependency = Class(name="requirements_editor_Dependency", is_abstract=True)
requirements_editor_Category = Class(name="requirements_editor_Category")
requirements_editor_TextualDescription = Class(name="requirements_editor_TextualDescription")
Description = Class(name="Description")
requirements_editor_QualityRequirement = Class(name="requirements_editor_QualityRequirement")
Requirement = Class(name="Requirement")
requirements_editor_FunctionalRequirement = Class(name="requirements_editor_FunctionalRequirement")
requirements_editor_SimpleDependency = Class(name="requirements_editor_SimpleDependency", is_abstract=True)
Dependency = Class(name="Dependency")
requirements_editor_Refines = Class(name="requirements_editor_Refines")
SimpleDependency = Class(name="SimpleDependency")
requirements_editor_ICost = Class(name="requirements_editor_ICost")
requirements_editor_CValue = Class(name="requirements_editor_CValue")
requirements_editor_Requires = Class(name="requirements_editor_Requires")
requirements_editor_Argument = Class(name="requirements_editor_Argument", is_abstract=True)
requirements_editor_BinaryOperatorArgument = Class(name="requirements_editor_BinaryOperatorArgument")
Argument = Class(name="Argument")
requirements_editor_RequirementArgument = Class(name="requirements_editor_RequirementArgument")
requirements_editor_DocumentRoot = Class(name="requirements_editor_DocumentRoot")
requirements_editor_NOTOperator = Class(name="requirements_editor_NOTOperator")

# requirements_editor_Requirement class attributes and methods
requirements_editor_Requirement_identifier: Property = Property(name="identifier", type=StringType)
requirements_editor_Requirement_name: Property = Property(name="name", type=StringType)
requirements_editor_Requirement_priority: Property = Property(name="priority", type=IntegerType)
requirements_editor_Requirement_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
requirements_editor_Requirement_m_findLeafNodes: Method = Method(name="findLeafNodes", parameters={Parameter(name='requirements_editor_argument', type=StringType)}, type=StringType)
requirements_editor_Requirement.attributes={requirements_editor_Requirement_name, requirements_editor_Requirement_identifier, requirements_editor_Requirement_isMandatory, requirements_editor_Requirement_priority}
requirements_editor_Requirement.methods={requirements_editor_Requirement_m_findLeafNodes}

# requirements_editor_Description class attributes and methods

# requirements_editor_Person class attributes and methods
requirements_editor_Person_name: Property = Property(name="name", type=StringType)
requirements_editor_Person.attributes={requirements_editor_Person_name}

# requirements_editor_Dependency class attributes and methods

# requirements_editor_Category class attributes and methods
requirements_editor_Category_name: Property = Property(name="name", type=StringType)
requirements_editor_Category.attributes={requirements_editor_Category_name}

# requirements_editor_TextualDescription class attributes and methods
requirements_editor_TextualDescription_description: Property = Property(name="description", type=StringType)
requirements_editor_TextualDescription.attributes={requirements_editor_TextualDescription_description}

# Description class attributes and methods

# requirements_editor_QualityRequirement class attributes and methods

# Requirement class attributes and methods

# requirements_editor_FunctionalRequirement class attributes and methods

# requirements_editor_SimpleDependency class attributes and methods
requirements_editor_SimpleDependency_comment: Property = Property(name="comment", type=StringType)
requirements_editor_SimpleDependency.attributes={requirements_editor_SimpleDependency_comment}

# Dependency class attributes and methods

# requirements_editor_Refines class attributes and methods

# SimpleDependency class attributes and methods

# requirements_editor_ICost class attributes and methods

# requirements_editor_CValue class attributes and methods

# requirements_editor_Requires class attributes and methods

# requirements_editor_Argument class attributes and methods

# requirements_editor_BinaryOperatorArgument class attributes and methods
requirements_editor_BinaryOperatorArgument_operator: Property = Property(name="operator", type=StringType)
requirements_editor_BinaryOperatorArgument.attributes={requirements_editor_BinaryOperatorArgument_operator}

# Argument class attributes and methods

# requirements_editor_RequirementArgument class attributes and methods

# requirements_editor_DocumentRoot class attributes and methods
requirements_editor_DocumentRoot_name: Property = Property(name="name", type=StringType)
requirements_editor_DocumentRoot.attributes={requirements_editor_DocumentRoot_name}

# requirements_editor_NOTOperator class attributes and methods

# Relationships
description0: BinaryAssociation = BinaryAssociation(
    name="description0",
    ends={
        Property(name="requirements_editor_Description", type=requirements_editor_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_editor_Requirement", type=requirements_editor_Description, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
requirementOwnedBy1: BinaryAssociation = BinaryAssociation(
    name="requirementOwnedBy1",
    ends={
        Property(name="Person", type=requirements_editor_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="personOwnsRequirement", type=requirements_editor_Person, multiplicity=Multiplicity(1, 1))
    }
)
dependencySource2: BinaryAssociation = BinaryAssociation(
    name="dependencySource2",
    ends={
        Property(name="requirements_editor_Dependency", type=requirements_editor_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_editor_Requirement3", type=requirements_editor_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subcategoryOf5: BinaryAssociation = BinaryAssociation(
    name="subcategoryOf5",
    ends={
        Property(name="requirements_editor_Category", type=requirements_editor_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_editor_Category4", type=requirements_editor_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryOwnedBy6: BinaryAssociation = BinaryAssociation(
    name="categoryOwnedBy6",
    ends={
        Property(name="Person7", type=requirements_editor_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="personOwnsCategory", type=requirements_editor_Person, multiplicity=Multiplicity(1, 1))
    }
)
requirement8: BinaryAssociation = BinaryAssociation(
    name="requirement8",
    ends={
        Property(name="requirements_editor_Requirement10", type=requirements_editor_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_editor_Category9", type=requirements_editor_Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
personOwnsRequirement11: BinaryAssociation = BinaryAssociation(
    name="personOwnsRequirement11",
    ends={
        Property(name="Requirement", type=requirements_editor_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="requirementOwnedBy", type=requirements_editor_Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
personOwnsCategory12: BinaryAssociation = BinaryAssociation(
    name="personOwnsCategory12",
    ends={
        Property(name="Category", type=requirements_editor_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="categoryOwnedBy", type=requirements_editor_Category, multiplicity=Multiplicity(0, 9999))
    }
)
dependencyTarget13: BinaryAssociation = BinaryAssociation(
    name="dependencyTarget13",
    ends={
        Property(name="requirements_editor_Requirement14", type=requirements_editor_SimpleDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_editor_SimpleDependency", type=requirements_editor_Requirement, multiplicity=Multiplicity(1, 1))
    }
)
argument15: BinaryAssociation = BinaryAssociation(
    name="argument15",
    ends={
        Property(name="requirements_editor_Argument", type=requirements_editor_Requires, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_editor_Requires", type=requirements_editor_Argument, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightSideArgument16: BinaryAssociation = BinaryAssociation(
    name="rightSideArgument16",
    ends={
        Property(name="requirements_editor_Argument17", type=requirements_editor_BinaryOperatorArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_editor_BinaryOperatorArgument", type=requirements_editor_Argument, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftSideArgument18: BinaryAssociation = BinaryAssociation(
    name="leftSideArgument18",
    ends={
        Property(name="requirements_editor_Argument20", type=requirements_editor_BinaryOperatorArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_editor_BinaryOperatorArgument19", type=requirements_editor_Argument, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
requirement21: BinaryAssociation = BinaryAssociation(
    name="requirement21",
    ends={
        Property(name="requirements_editor_Requirement22", type=requirements_editor_RequirementArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_editor_RequirementArgument", type=requirements_editor_Requirement, multiplicity=Multiplicity(1, 1))
    }
)
rootCategories23: BinaryAssociation = BinaryAssociation(
    name="rootCategories23",
    ends={
        Property(name="requirements_editor_Category24", type=requirements_editor_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_editor_DocumentRoot", type=requirements_editor_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person25: BinaryAssociation = BinaryAssociation(
    name="person25",
    ends={
        Property(name="requirements_editor_Person", type=requirements_editor_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_editor_DocumentRoot26", type=requirements_editor_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument27: BinaryAssociation = BinaryAssociation(
    name="argument27",
    ends={
        Property(name="requirements_editor_Argument28", type=requirements_editor_NOTOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_editor_NOTOperator", type=requirements_editor_Argument, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_requirements_editor_TextualDescription_Description = Generalization(general=Description, specific=requirements_editor_TextualDescription)
gen_requirements_editor_QualityRequirement_Requirement = Generalization(general=Requirement, specific=requirements_editor_QualityRequirement)
gen_requirements_editor_FunctionalRequirement_Requirement = Generalization(general=Requirement, specific=requirements_editor_FunctionalRequirement)
gen_requirements_editor_SimpleDependency_Dependency = Generalization(general=Dependency, specific=requirements_editor_SimpleDependency)
gen_requirements_editor_Refines_SimpleDependency = Generalization(general=SimpleDependency, specific=requirements_editor_Refines)
gen_requirements_editor_ICost_SimpleDependency = Generalization(general=SimpleDependency, specific=requirements_editor_ICost)
gen_requirements_editor_CValue_SimpleDependency = Generalization(general=SimpleDependency, specific=requirements_editor_CValue)
gen_requirements_editor_Requires_Dependency = Generalization(general=Dependency, specific=requirements_editor_Requires)
gen_requirements_editor_BinaryOperatorArgument_Argument = Generalization(general=Argument, specific=requirements_editor_BinaryOperatorArgument)
gen_requirements_editor_RequirementArgument_Argument = Generalization(general=Argument, specific=requirements_editor_RequirementArgument)
gen_requirements_editor_NOTOperator_Argument = Generalization(general=Argument, specific=requirements_editor_NOTOperator)

# Domain Model
domain_model = DomainModel(
    name="requirements_editor",
    types={requirements_editor_Requirement, requirements_editor_Description, requirements_editor_Person, requirements_editor_Dependency, requirements_editor_Category, requirements_editor_TextualDescription, Description, requirements_editor_QualityRequirement, Requirement, requirements_editor_FunctionalRequirement, requirements_editor_SimpleDependency, Dependency, requirements_editor_Refines, SimpleDependency, requirements_editor_ICost, requirements_editor_CValue, requirements_editor_Requires, requirements_editor_Argument, requirements_editor_BinaryOperatorArgument, Argument, requirements_editor_RequirementArgument, requirements_editor_DocumentRoot, requirements_editor_NOTOperator, BinaryOperator},
    associations={description0, requirementOwnedBy1, dependencySource2, subcategoryOf5, categoryOwnedBy6, requirement8, personOwnsRequirement11, personOwnsCategory12, dependencyTarget13, argument15, rightSideArgument16, leftSideArgument18, requirement21, rootCategories23, person25, argument27},
    generalizations={gen_requirements_editor_TextualDescription_Description, gen_requirements_editor_QualityRequirement_Requirement, gen_requirements_editor_FunctionalRequirement_Requirement, gen_requirements_editor_SimpleDependency_Dependency, gen_requirements_editor_Refines_SimpleDependency, gen_requirements_editor_ICost_SimpleDependency, gen_requirements_editor_CValue_SimpleDependency, gen_requirements_editor_Requires_Dependency, gen_requirements_editor_BinaryOperatorArgument_Argument, gen_requirements_editor_RequirementArgument_Argument, gen_requirements_editor_NOTOperator_Argument},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)