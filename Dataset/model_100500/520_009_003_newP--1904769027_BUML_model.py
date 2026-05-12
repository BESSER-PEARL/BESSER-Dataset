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
newP_Requirement = Class(name="newP_Requirement", is_abstract=True)
newP_Description = Class(name="newP_Description", is_abstract=True)
newP_Dependency = Class(name="newP_Dependency", is_abstract=True)
newP_Term = Class(name="newP_Term", is_abstract=True)
newP_UnaryOperator = Class(name="newP_UnaryOperator", is_abstract=True)
Term = Class(name="Term")
newP_Requires = Class(name="newP_Requires")
Dependency = Class(name="Dependency")
newP_FunctionalRequirement = Class(name="newP_FunctionalRequirement")
Requirement = Class(name="Requirement")
newP_QualityRequirement = Class(name="newP_QualityRequirement")
newP_TextDescription = Class(name="newP_TextDescription")
Description = Class(name="Description")
newP_Category = Class(name="newP_Category")
newP_Specification = Class(name="newP_Specification")
newP_Person = Class(name="newP_Person")
newP_SimpleDependency = Class(name="newP_SimpleDependency", is_abstract=True)
newP_RequirementTerm = Class(name="newP_RequirementTerm")
newP_CValue = Class(name="newP_CValue")
SimpleDependency = Class(name="SimpleDependency")
newP_Refines = Class(name="newP_Refines")
newP_ICost = Class(name="newP_ICost")
newP_NotOperator = Class(name="newP_NotOperator")
UnaryOperator = Class(name="UnaryOperator")
newP_BinaryOperator = Class(name="newP_BinaryOperator", is_abstract=True)
newP_AndOperartor = Class(name="newP_AndOperartor")
BinaryOperator = Class(name="BinaryOperator")
newP_OrOperator = Class(name="newP_OrOperator")

# newP_Requirement class attributes and methods
newP_Requirement_name: Property = Property(name="name", type=StringType)
newP_Requirement_identifier: Property = Property(name="identifier", type=StringType)
newP_Requirement_priority: Property = Property(name="priority", type=IntegerType)
newP_Requirement_mandatory: Property = Property(name="mandatory", type=BooleanType)
newP_Requirement.attributes={newP_Requirement_mandatory, newP_Requirement_identifier, newP_Requirement_priority, newP_Requirement_name}

# newP_Description class attributes and methods

# newP_Dependency class attributes and methods

# newP_Term class attributes and methods

# newP_UnaryOperator class attributes and methods
newP_UnaryOperator_name: Property = Property(name="name", type=StringType)
newP_UnaryOperator.attributes={newP_UnaryOperator_name}

# Term class attributes and methods

# newP_Requires class attributes and methods
newP_Requires_name: Property = Property(name="name", type=StringType)
newP_Requires.attributes={newP_Requires_name}

# Dependency class attributes and methods

# newP_FunctionalRequirement class attributes and methods

# Requirement class attributes and methods

# newP_QualityRequirement class attributes and methods

# newP_TextDescription class attributes and methods
newP_TextDescription_text: Property = Property(name="text", type=StringType)
newP_TextDescription.attributes={newP_TextDescription_text}

# Description class attributes and methods

# newP_Category class attributes and methods
newP_Category_name: Property = Property(name="name", type=StringType)
newP_Category.attributes={newP_Category_name}

# newP_Specification class attributes and methods
newP_Specification_name: Property = Property(name="name", type=StringType)
newP_Specification.attributes={newP_Specification_name}

# newP_Person class attributes and methods
newP_Person_firstName: Property = Property(name="firstName", type=StringType)
newP_Person_lastName: Property = Property(name="lastName", type=StringType)
newP_Person.attributes={newP_Person_firstName, newP_Person_lastName}

# newP_SimpleDependency class attributes and methods
newP_SimpleDependency_name: Property = Property(name="name", type=StringType)
newP_SimpleDependency.attributes={newP_SimpleDependency_name}

# newP_RequirementTerm class attributes and methods

# newP_CValue class attributes and methods

# SimpleDependency class attributes and methods

# newP_Refines class attributes and methods

# newP_ICost class attributes and methods

# newP_NotOperator class attributes and methods

# UnaryOperator class attributes and methods

# newP_BinaryOperator class attributes and methods

# newP_AndOperartor class attributes and methods

# BinaryOperator class attributes and methods

# newP_OrOperator class attributes and methods

# Relationships
description0: BinaryAssociation = BinaryAssociation(
    name="description0",
    ends={
        Property(name="newP_Description", type=newP_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_Requirement", type=newP_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categories12: BinaryAssociation = BinaryAssociation(
    name="categories12",
    ends={
        Property(name="newP_Category14", type=newP_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_Person13", type=newP_Category, multiplicity=Multiplicity(0, 9999))
    }
)
requirements15: BinaryAssociation = BinaryAssociation(
    name="requirements15",
    ends={
        Property(name="newP_Requirement17", type=newP_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_Person16", type=newP_Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
RHS18: BinaryAssociation = BinaryAssociation(
    name="RHS18",
    ends={
        Property(name="newP_Term", type=newP_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_UnaryOperator", type=newP_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dependency1: BinaryAssociation = BinaryAssociation(
    name="dependency1",
    ends={
        Property(name="newP_Dependency", type=newP_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_Requirement2", type=newP_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requirement3: BinaryAssociation = BinaryAssociation(
    name="requirement3",
    ends={
        Property(name="newP_Requirement4", type=newP_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_Category", type=newP_Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="newP_Category7", type=newP_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_Category5", type=newP_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
category8: BinaryAssociation = BinaryAssociation(
    name="category8",
    ends={
        Property(name="newP_Category9", type=newP_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_Specification", type=newP_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person10: BinaryAssociation = BinaryAssociation(
    name="person10",
    ends={
        Property(name="newP_Person", type=newP_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_Specification11", type=newP_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
RHS19: BinaryAssociation = BinaryAssociation(
    name="RHS19",
    ends={
        Property(name="newP_Term20", type=newP_Requires, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_Requires", type=newP_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
RHS21: BinaryAssociation = BinaryAssociation(
    name="RHS21",
    ends={
        Property(name="newP_RequirementTerm", type=newP_SimpleDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_SimpleDependency", type=newP_RequirementTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LHS22: BinaryAssociation = BinaryAssociation(
    name="LHS22",
    ends={
        Property(name="newP_Term23", type=newP_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_BinaryOperator", type=newP_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
requirement24: BinaryAssociation = BinaryAssociation(
    name="requirement24",
    ends={
        Property(name="newP_Requirement26", type=newP_RequirementTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="newP_RequirementTerm25", type=newP_Requirement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_newP_UnaryOperator_Term = Generalization(general=Term, specific=newP_UnaryOperator)
gen_newP_Requires_Dependency = Generalization(general=Dependency, specific=newP_Requires)
gen_newP_FunctionalRequirement_Requirement = Generalization(general=Requirement, specific=newP_FunctionalRequirement)
gen_newP_QualityRequirement_Requirement = Generalization(general=Requirement, specific=newP_QualityRequirement)
gen_newP_TextDescription_Description = Generalization(general=Description, specific=newP_TextDescription)
gen_newP_SimpleDependency_Dependency = Generalization(general=Dependency, specific=newP_SimpleDependency)
gen_newP_CValue_SimpleDependency = Generalization(general=SimpleDependency, specific=newP_CValue)
gen_newP_Refines_SimpleDependency = Generalization(general=SimpleDependency, specific=newP_Refines)
gen_newP_ICost_SimpleDependency = Generalization(general=SimpleDependency, specific=newP_ICost)
gen_newP_NotOperator_UnaryOperator = Generalization(general=UnaryOperator, specific=newP_NotOperator)
gen_newP_BinaryOperator_UnaryOperator = Generalization(general=UnaryOperator, specific=newP_BinaryOperator)
gen_newP_AndOperartor_BinaryOperator = Generalization(general=BinaryOperator, specific=newP_AndOperartor)
gen_newP_OrOperator_BinaryOperator = Generalization(general=BinaryOperator, specific=newP_OrOperator)
gen_newP_RequirementTerm_Term = Generalization(general=Term, specific=newP_RequirementTerm)

# Domain Model
domain_model = DomainModel(
    name="newP",
    types={newP_Requirement, newP_Description, newP_Dependency, newP_Term, newP_UnaryOperator, Term, newP_Requires, Dependency, newP_FunctionalRequirement, Requirement, newP_QualityRequirement, newP_TextDescription, Description, newP_Category, newP_Specification, newP_Person, newP_SimpleDependency, newP_RequirementTerm, newP_CValue, SimpleDependency, newP_Refines, newP_ICost, newP_NotOperator, UnaryOperator, newP_BinaryOperator, newP_AndOperartor, BinaryOperator, newP_OrOperator},
    associations={description0, categories12, requirements15, RHS18, dependency1, requirement3, children6, category8, person10, RHS19, RHS21, LHS22, requirement24},
    generalizations={gen_newP_UnaryOperator_Term, gen_newP_Requires_Dependency, gen_newP_FunctionalRequirement_Requirement, gen_newP_QualityRequirement_Requirement, gen_newP_TextDescription_Description, gen_newP_SimpleDependency_Dependency, gen_newP_CValue_SimpleDependency, gen_newP_Refines_SimpleDependency, gen_newP_ICost_SimpleDependency, gen_newP_NotOperator_UnaryOperator, gen_newP_BinaryOperator_UnaryOperator, gen_newP_AndOperartor_BinaryOperator, gen_newP_OrOperator_BinaryOperator, gen_newP_RequirementTerm_Term},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)