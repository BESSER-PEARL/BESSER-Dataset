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
AttributeType: Enumeration = Enumeration(
    name="AttributeType",
    literals={
            EnumerationLiteral(name="TextualValue"),
			EnumerationLiteral(name="NumericalValue"),
			EnumerationLiteral(name="TemporalValue"),
			EnumerationLiteral(name="Other")
    }
)

PrivilegeNature: Enumeration = Enumeration(
    name="PrivilegeNature",
    literals={
            EnumerationLiteral(name="create"),
			EnumerationLiteral(name="read"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="delete")
    }
)

PriorityLevel: Enumeration = Enumeration(
    name="PriorityLevel",
    literals={
            EnumerationLiteral(name="VeryHigh"),
			EnumerationLiteral(name="High"),
			EnumerationLiteral(name="Normal"),
			EnumerationLiteral(name="Low"),
			EnumerationLiteral(name="VeryLow")
    }
)

AnnotationStatus: Enumeration = Enumeration(
    name="AnnotationStatus",
    literals={
            EnumerationLiteral(name="New"),
			EnumerationLiteral(name="Fixed"),
			EnumerationLiteral(name="Invalid"),
			EnumerationLiteral(name="Wontfix"),
			EnumerationLiteral(name="Duplicate"),
			EnumerationLiteral(name="Incomplete")
    }
)

# Classes
requirements_Attribute = Class(name="requirements_Attribute")
requirements_RelationShip = Class(name="requirements_RelationShip")
requirements_ModelElement = Class(name="requirements_ModelElement", is_abstract=True)
requirements_BasicElement = Class(name="requirements_BasicElement", is_abstract=True)
ModelElement = Class(name="ModelElement")
requirements_Entity = Class(name="requirements_Entity")
BasicElement = Class(name="BasicElement")
requirements_Goal = Class(name="requirements_Goal")
requirements_Organization = Class(name="requirements_Organization")
AnnotableElement = Class(name="AnnotableElement")
requirements_Agent = Class(name="requirements_Agent")
requirements_RequirementsDefinition = Class(name="requirements_RequirementsDefinition")
Organization = Class(name="Organization")
requirements_PrivilegeGroup = Class(name="requirements_PrivilegeGroup")
requirements_GoalStep = Class(name="requirements_GoalStep")
requirements_Privilege = Class(name="requirements_Privilege")
requirements_Process = Class(name="requirements_Process")
requirements_Annotation = Class(name="requirements_Annotation")
requirements_AnnotableElement = Class(name="requirements_AnnotableElement")

# requirements_Attribute class attributes and methods
requirements_Attribute_type: Property = Property(name="type", type=StringType)
requirements_Attribute.attributes={requirements_Attribute_type}

# requirements_RelationShip class attributes and methods
requirements_RelationShip_sourceMin: Property = Property(name="sourceMin", type=IntegerType)
requirements_RelationShip_sourceMax: Property = Property(name="sourceMax", type=IntegerType)
requirements_RelationShip_targetMin: Property = Property(name="targetMin", type=IntegerType)
requirements_RelationShip_targetMax: Property = Property(name="targetMax", type=IntegerType)
requirements_RelationShip.attributes={requirements_RelationShip_sourceMin, requirements_RelationShip_targetMax, requirements_RelationShip_sourceMax, requirements_RelationShip_targetMin}

# requirements_ModelElement class attributes and methods

# requirements_BasicElement class attributes and methods
requirements_BasicElement_name: Property = Property(name="name", type=StringType)
requirements_BasicElement_documentation: Property = Property(name="documentation", type=StringType)
requirements_BasicElement_id: Property = Property(name="id", type=StringType)
requirements_BasicElement.attributes={requirements_BasicElement_documentation, requirements_BasicElement_name, requirements_BasicElement_id}

# ModelElement class attributes and methods

# requirements_Entity class attributes and methods

# BasicElement class attributes and methods

# requirements_Goal class attributes and methods
requirements_Goal_priority: Property = Property(name="priority", type=StringType)
requirements_Goal_synopsis: Property = Property(name="synopsis", type=StringType)
requirements_Goal.attributes={requirements_Goal_priority, requirements_Goal_synopsis}

# requirements_Organization class attributes and methods

# AnnotableElement class attributes and methods

# requirements_Agent class attributes and methods
requirements_Agent_isHuman: Property = Property(name="isHuman", type=BooleanType)
requirements_Agent.attributes={requirements_Agent_isHuman}

# requirements_RequirementsDefinition class attributes and methods
requirements_RequirementsDefinition_version: Property = Property(name="version", type=StringType)
requirements_RequirementsDefinition_date: Property = Property(name="date", type=DateType)
requirements_RequirementsDefinition.attributes={requirements_RequirementsDefinition_date, requirements_RequirementsDefinition_version}

# Organization class attributes and methods

# requirements_PrivilegeGroup class attributes and methods
requirements_PrivilegeGroup_documentation: Property = Property(name="documentation", type=StringType)
requirements_PrivilegeGroup.attributes={requirements_PrivilegeGroup_documentation}

# requirements_GoalStep class attributes and methods

# requirements_Privilege class attributes and methods
requirements_Privilege_category: Property = Property(name="category", type=StringType)
requirements_Privilege.attributes={requirements_Privilege_category}

# requirements_Process class attributes and methods

# requirements_Annotation class attributes and methods
requirements_Annotation_comment: Property = Property(name="comment", type=StringType)
requirements_Annotation_author: Property = Property(name="author", type=StringType)
requirements_Annotation_annotation: Property = Property(name="annotation", type=StringType)
requirements_Annotation_date: Property = Property(name="date", type=DateType)
requirements_Annotation_status: Property = Property(name="status", type=StringType)
requirements_Annotation_id: Property = Property(name="id", type=StringType)
requirements_Annotation.attributes={requirements_Annotation_date, requirements_Annotation_author, requirements_Annotation_id, requirements_Annotation_annotation, requirements_Annotation_comment, requirements_Annotation_status}

# requirements_AnnotableElement class attributes and methods

# Relationships
attributes2: BinaryAssociation = BinaryAssociation(
    name="attributes2",
    ends={
        Property(name="requirements_Attribute", type=requirements_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_Entity3", type=requirements_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="requirements_Entity5", type=requirements_RelationShip, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_RelationShip", type=requirements_Entity, multiplicity=Multiplicity(1, 1))
    }
)
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="requirements_Entity", type=requirements_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_Entity0", type=requirements_Entity, multiplicity=Multiplicity(0, 1))
    }
)
isResponsible10: BinaryAssociation = BinaryAssociation(
    name="isResponsible10",
    ends={
        Property(name="Goal", type=requirements_Agent, multiplicity=Multiplicity(1, 1)),
        Property(name="responsible", type=requirements_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="requirements_Entity8", type=requirements_RelationShip, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_RelationShip7", type=requirements_Entity, multiplicity=Multiplicity(1, 1))
    }
)
childElements9: BinaryAssociation = BinaryAssociation(
    name="childElements9",
    ends={
        Property(name="requirements_ModelElement", type=requirements_Organization, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_Organization", type=requirements_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subgoals12: BinaryAssociation = BinaryAssociation(
    name="subgoals12",
    ends={
        Property(name="requirements_Goal", type=requirements_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_Goal11", type=requirements_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
responsible13: BinaryAssociation = BinaryAssociation(
    name="responsible13",
    ends={
        Property(name="Agent", type=requirements_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="isResponsible", type=requirements_Agent, multiplicity=Multiplicity(0, 9999))
    }
)
privilegeGroup14: BinaryAssociation = BinaryAssociation(
    name="privilegeGroup14",
    ends={
        Property(name="requirements_PrivilegeGroup", type=requirements_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_Goal15", type=requirements_PrivilegeGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
step16: BinaryAssociation = BinaryAssociation(
    name="step16",
    ends={
        Property(name="requirements_GoalStep", type=requirements_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_Goal17", type=requirements_GoalStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element18: BinaryAssociation = BinaryAssociation(
    name="element18",
    ends={
        Property(name="requirements_BasicElement", type=requirements_Privilege, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_Privilege", type=requirements_BasicElement, multiplicity=Multiplicity(1, 1))
    }
)
entryPoint19: BinaryAssociation = BinaryAssociation(
    name="entryPoint19",
    ends={
        Property(name="requirements_Entity21", type=requirements_PrivilegeGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_PrivilegeGroup20", type=requirements_Entity, multiplicity=Multiplicity(1, 1))
    }
)
privileges22: BinaryAssociation = BinaryAssociation(
    name="privileges22",
    ends={
        Property(name="requirements_Privilege24", type=requirements_PrivilegeGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_PrivilegeGroup23", type=requirements_Privilege, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nextGoals25: BinaryAssociation = BinaryAssociation(
    name="nextGoals25",
    ends={
        Property(name="requirements_Goal27", type=requirements_GoalStep, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_GoalStep26", type=requirements_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
process28: BinaryAssociation = BinaryAssociation(
    name="process28",
    ends={
        Property(name="requirements_Process", type=requirements_GoalStep, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_GoalStep29", type=requirements_Process, multiplicity=Multiplicity(0, 1))
    }
)
annotation30: BinaryAssociation = BinaryAssociation(
    name="annotation30",
    ends={
        Property(name="requirements_Annotation", type=requirements_AnnotableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements_AnnotableElement", type=requirements_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_requirements_RelationShip_BasicElement = Generalization(general=BasicElement, specific=requirements_RelationShip)
gen_requirements_BasicElement_ModelElement = Generalization(general=ModelElement, specific=requirements_BasicElement)
gen_requirements_Entity_BasicElement = Generalization(general=BasicElement, specific=requirements_Entity)
gen_requirements_Goal_AnnotableElement = Generalization(general=AnnotableElement, specific=requirements_Goal)
gen_requirements_Attribute_BasicElement = Generalization(general=BasicElement, specific=requirements_Attribute)
gen_requirements_Organization_AnnotableElement = Generalization(general=AnnotableElement, specific=requirements_Organization)
gen_requirements_Agent_AnnotableElement = Generalization(general=AnnotableElement, specific=requirements_Agent)
gen_requirements_RequirementsDefinition_Organization = Generalization(general=Organization, specific=requirements_RequirementsDefinition)
gen_requirements_PrivilegeGroup_ModelElement = Generalization(general=ModelElement, specific=requirements_PrivilegeGroup)
gen_requirements_Process_Organization = Generalization(general=Organization, specific=requirements_Process)
gen_requirements_AnnotableElement_BasicElement = Generalization(general=BasicElement, specific=requirements_AnnotableElement)

# Domain Model
domain_model = DomainModel(
    name="requirements",
    types={requirements_Attribute, requirements_RelationShip, requirements_ModelElement, requirements_BasicElement, ModelElement, requirements_Entity, BasicElement, requirements_Goal, requirements_Organization, AnnotableElement, requirements_Agent, requirements_RequirementsDefinition, Organization, requirements_PrivilegeGroup, requirements_GoalStep, requirements_Privilege, requirements_Process, requirements_Annotation, requirements_AnnotableElement, AttributeType, PrivilegeNature, PriorityLevel, AnnotationStatus},
    associations={attributes2, source4, parent1, isResponsible10, target6, childElements9, subgoals12, responsible13, privilegeGroup14, step16, element18, entryPoint19, privileges22, nextGoals25, process28, annotation30},
    generalizations={gen_requirements_RelationShip_BasicElement, gen_requirements_BasicElement_ModelElement, gen_requirements_Entity_BasicElement, gen_requirements_Goal_AnnotableElement, gen_requirements_Attribute_BasicElement, gen_requirements_Organization_AnnotableElement, gen_requirements_Agent_AnnotableElement, gen_requirements_RequirementsDefinition_Organization, gen_requirements_PrivilegeGroup_ModelElement, gen_requirements_Process_Organization, gen_requirements_AnnotableElement_BasicElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)