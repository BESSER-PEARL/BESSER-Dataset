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
AttributesType: Enumeration = Enumeration(
    name="AttributesType",
    literals={
            EnumerationLiteral(name="Text"),
			EnumerationLiteral(name="Object"),
			EnumerationLiteral(name="Allocate"),
			EnumerationLiteral(name="Link")
    }
)

# Classes
requirement_Requirement = Class(name="requirement_Requirement", is_abstract=True)
requirement_RequirementProject = Class(name="requirement_RequirementProject")
IdentifiedElement = Class(name="IdentifiedElement")
requirement_HierarchicalElement = Class(name="requirement_HierarchicalElement")
requirement_AttributeConfiguration = Class(name="requirement_AttributeConfiguration")
requirement_SpecialChapter = Class(name="requirement_SpecialChapter", is_abstract=True)
requirement_UpstreamModel = Class(name="requirement_UpstreamModel")
requirement_EObject = Class(name="requirement_EObject")
requirement_CurrentRequirement = Class(name="requirement_CurrentRequirement")
Requirement = Class(name="Requirement")
requirement_Attribute = Class(name="requirement_Attribute", is_abstract=True)
EModelElement = Class(name="EModelElement")
requirement_ConfiguratedAttribute = Class(name="requirement_ConfiguratedAttribute")
requirement_DefaultAttributeValue = Class(name="requirement_DefaultAttributeValue")
requirement_AttributeValue = Class(name="requirement_AttributeValue")
Project = Class(name="Project")
requirement_AttributeLink = Class(name="requirement_AttributeLink")
ObjectAttribute = Class(name="ObjectAttribute")
requirement_AttributeAllocate = Class(name="requirement_AttributeAllocate")
requirement_UntracedChapter = Class(name="requirement_UntracedChapter")
SpecialChapter = Class(name="SpecialChapter")
requirement_IdentifiedElement = Class(name="requirement_IdentifiedElement", is_abstract=True)
requirement_TextAttribute = Class(name="requirement_TextAttribute")
Attribute = Class(name="Attribute")
requirement_ObjectAttribute = Class(name="requirement_ObjectAttribute")
requirement_ProblemChapter = Class(name="requirement_ProblemChapter")
requirement_TrashChapter = Class(name="requirement_TrashChapter")
requirement_AnonymousRequirement = Class(name="requirement_AnonymousRequirement")
requirement_DeletedChapter = Class(name="requirement_DeletedChapter")

# requirement_Requirement class attributes and methods
requirement_Requirement_externalResources: Property = Property(name="externalResources", type=StringType)
requirement_Requirement.attributes={requirement_Requirement_externalResources}

# requirement_RequirementProject class attributes and methods

# IdentifiedElement class attributes and methods

# requirement_HierarchicalElement class attributes and methods
requirement_HierarchicalElement_nextReqIndex: Property = Property(name="nextReqIndex", type=StringType)
requirement_HierarchicalElement.attributes={requirement_HierarchicalElement_nextReqIndex}

# requirement_AttributeConfiguration class attributes and methods

# requirement_SpecialChapter class attributes and methods

# requirement_UpstreamModel class attributes and methods

# requirement_EObject class attributes and methods

# requirement_CurrentRequirement class attributes and methods
requirement_CurrentRequirement_impacted: Property = Property(name="impacted", type=BooleanType)
requirement_CurrentRequirement.attributes={requirement_CurrentRequirement_impacted}

# Requirement class attributes and methods

# requirement_Attribute class attributes and methods
requirement_Attribute_name: Property = Property(name="name", type=StringType)
requirement_Attribute.attributes={requirement_Attribute_name}

# EModelElement class attributes and methods

# requirement_ConfiguratedAttribute class attributes and methods
requirement_ConfiguratedAttribute_type: Property = Property(name="type", type=StringType)
requirement_ConfiguratedAttribute_name: Property = Property(name="name", type=StringType)
requirement_ConfiguratedAttribute.attributes={requirement_ConfiguratedAttribute_type, requirement_ConfiguratedAttribute_name}

# requirement_DefaultAttributeValue class attributes and methods

# requirement_AttributeValue class attributes and methods
requirement_AttributeValue_value: Property = Property(name="value", type=StringType)
requirement_AttributeValue.attributes={requirement_AttributeValue_value}

# Project class attributes and methods

# requirement_AttributeLink class attributes and methods
requirement_AttributeLink_partial: Property = Property(name="partial", type=StringType)
requirement_AttributeLink.attributes={requirement_AttributeLink_partial}

# ObjectAttribute class attributes and methods

# requirement_AttributeAllocate class attributes and methods

# requirement_UntracedChapter class attributes and methods

# SpecialChapter class attributes and methods

# requirement_IdentifiedElement class attributes and methods
requirement_IdentifiedElement_identifier: Property = Property(name="identifier", type=StringType)
requirement_IdentifiedElement_shortDescription: Property = Property(name="shortDescription", type=StringType)
requirement_IdentifiedElement.attributes={requirement_IdentifiedElement_identifier, requirement_IdentifiedElement_shortDescription}

# requirement_TextAttribute class attributes and methods
requirement_TextAttribute_value: Property = Property(name="value", type=StringType)
requirement_TextAttribute.attributes={requirement_TextAttribute_value}

# Attribute class attributes and methods

# requirement_ObjectAttribute class attributes and methods

# requirement_ProblemChapter class attributes and methods

# requirement_TrashChapter class attributes and methods

# requirement_AnonymousRequirement class attributes and methods

# requirement_DeletedChapter class attributes and methods

# Relationships
element7: BinaryAssociation = BinaryAssociation(
    name="element7",
    ends={
        Property(name="requirement_HierarchicalElement8", type=requirement_EObject, multiplicity=Multiplicity(0, 1)),
        Property(name="requirement_EObject", type=requirement_HierarchicalElement, multiplicity=Multiplicity(1, 1))
    }
)
children10: BinaryAssociation = BinaryAssociation(
    name="children10",
    ends={
        Property(name="HierarchicalElement", type=requirement_HierarchicalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=requirement_HierarchicalElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent12: BinaryAssociation = BinaryAssociation(
    name="parent12",
    ends={
        Property(name="HierarchicalElement13", type=requirement_HierarchicalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=requirement_HierarchicalElement, multiplicity=Multiplicity(0, 1))
    }
)
hierarchicalElement0: BinaryAssociation = BinaryAssociation(
    name="hierarchicalElement0",
    ends={
        Property(name="requirement_HierarchicalElement", type=requirement_RequirementProject, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_RequirementProject", type=requirement_HierarchicalElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeConfiguration1: BinaryAssociation = BinaryAssociation(
    name="attributeConfiguration1",
    ends={
        Property(name="requirement_AttributeConfiguration", type=requirement_RequirementProject, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_RequirementProject2", type=requirement_AttributeConfiguration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
chapter3: BinaryAssociation = BinaryAssociation(
    name="chapter3",
    ends={
        Property(name="requirement_SpecialChapter", type=requirement_RequirementProject, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_RequirementProject4", type=requirement_SpecialChapter, multiplicity=Multiplicity(3, 3), is_composite=True)
    }
)
upstreamModel5: BinaryAssociation = BinaryAssociation(
    name="upstreamModel5",
    ends={
        Property(name="requirement_UpstreamModel", type=requirement_RequirementProject, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_RequirementProject6", type=requirement_UpstreamModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value22: BinaryAssociation = BinaryAssociation(
    name="value22",
    ends={
        Property(name="requirement_AttributeValue24", type=requirement_DefaultAttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_DefaultAttributeValue23", type=requirement_AttributeValue, multiplicity=Multiplicity(1, 1))
    }
)
requirement14: BinaryAssociation = BinaryAssociation(
    name="requirement14",
    ends={
        Property(name="requirement_Requirement", type=requirement_HierarchicalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_HierarchicalElement15", type=requirement_Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listAttributes16: BinaryAssociation = BinaryAssociation(
    name="listAttributes16",
    ends={
        Property(name="requirement_ConfiguratedAttribute", type=requirement_AttributeConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_AttributeConfiguration17", type=requirement_ConfiguratedAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultValue18: BinaryAssociation = BinaryAssociation(
    name="defaultValue18",
    ends={
        Property(name="requirement_DefaultAttributeValue", type=requirement_ConfiguratedAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_ConfiguratedAttribute19", type=requirement_DefaultAttributeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
listValue20: BinaryAssociation = BinaryAssociation(
    name="listValue20",
    ends={
        Property(name="requirement_AttributeValue", type=requirement_ConfiguratedAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_ConfiguratedAttribute21", type=requirement_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hierarchicalElement25: BinaryAssociation = BinaryAssociation(
    name="hierarchicalElement25",
    ends={
        Property(name="requirement_HierarchicalElement27", type=requirement_SpecialChapter, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_SpecialChapter26", type=requirement_HierarchicalElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requirement28: BinaryAssociation = BinaryAssociation(
    name="requirement28",
    ends={
        Property(name="requirement_Requirement30", type=requirement_SpecialChapter, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_SpecialChapter29", type=requirement_Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value31: BinaryAssociation = BinaryAssociation(
    name="value31",
    ends={
        Property(name="requirement_EObject32", type=requirement_ObjectAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_ObjectAttribute", type=requirement_EObject, multiplicity=Multiplicity(0, 1))
    }
)
attribute33: BinaryAssociation = BinaryAssociation(
    name="attribute33",
    ends={
        Property(name="requirement_Attribute", type=requirement_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirement_Requirement34", type=requirement_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_requirement_RequirementProject_IdentifiedElement = Generalization(general=IdentifiedElement, specific=requirement_RequirementProject)
gen_requirement_HierarchicalElement_IdentifiedElement = Generalization(general=IdentifiedElement, specific=requirement_HierarchicalElement)
gen_requirement_CurrentRequirement_Requirement = Generalization(general=Requirement, specific=requirement_CurrentRequirement)
gen_requirement_Attribute_EModelElement = Generalization(general=EModelElement, specific=requirement_Attribute)
gen_requirement_UpstreamModel_Project = Generalization(general=Project, specific=requirement_UpstreamModel)
gen_requirement_AttributeLink_ObjectAttribute = Generalization(general=ObjectAttribute, specific=requirement_AttributeLink)
gen_requirement_AttributeAllocate_ObjectAttribute = Generalization(general=ObjectAttribute, specific=requirement_AttributeAllocate)
gen_requirement_UntracedChapter_SpecialChapter = Generalization(general=SpecialChapter, specific=requirement_UntracedChapter)
gen_requirement_IdentifiedElement_EModelElement = Generalization(general=EModelElement, specific=requirement_IdentifiedElement)
gen_requirement_TextAttribute_Attribute = Generalization(general=Attribute, specific=requirement_TextAttribute)
gen_requirement_ObjectAttribute_Attribute = Generalization(general=Attribute, specific=requirement_ObjectAttribute)
gen_requirement_ProblemChapter_SpecialChapter = Generalization(general=SpecialChapter, specific=requirement_ProblemChapter)
gen_requirement_TrashChapter_SpecialChapter = Generalization(general=SpecialChapter, specific=requirement_TrashChapter)
gen_requirement_Requirement_IdentifiedElement = Generalization(general=IdentifiedElement, specific=requirement_Requirement)
gen_requirement_AnonymousRequirement_Requirement = Generalization(general=Requirement, specific=requirement_AnonymousRequirement)
gen_requirement_DeletedChapter_SpecialChapter = Generalization(general=SpecialChapter, specific=requirement_DeletedChapter)

# Domain Model
domain_model = DomainModel(
    name="requirement",
    types={requirement_Requirement, requirement_RequirementProject, IdentifiedElement, requirement_HierarchicalElement, requirement_AttributeConfiguration, requirement_SpecialChapter, requirement_UpstreamModel, requirement_EObject, requirement_CurrentRequirement, Requirement, requirement_Attribute, EModelElement, requirement_ConfiguratedAttribute, requirement_DefaultAttributeValue, requirement_AttributeValue, Project, requirement_AttributeLink, ObjectAttribute, requirement_AttributeAllocate, requirement_UntracedChapter, SpecialChapter, requirement_IdentifiedElement, requirement_TextAttribute, Attribute, requirement_ObjectAttribute, requirement_ProblemChapter, requirement_TrashChapter, requirement_AnonymousRequirement, requirement_DeletedChapter, AttributesType},
    associations={element7, children10, parent12, hierarchicalElement0, attributeConfiguration1, chapter3, upstreamModel5, value22, requirement14, listAttributes16, defaultValue18, listValue20, hierarchicalElement25, requirement28, value31, attribute33},
    generalizations={gen_requirement_RequirementProject_IdentifiedElement, gen_requirement_HierarchicalElement_IdentifiedElement, gen_requirement_CurrentRequirement_Requirement, gen_requirement_Attribute_EModelElement, gen_requirement_UpstreamModel_Project, gen_requirement_AttributeLink_ObjectAttribute, gen_requirement_AttributeAllocate_ObjectAttribute, gen_requirement_UntracedChapter_SpecialChapter, gen_requirement_IdentifiedElement_EModelElement, gen_requirement_TextAttribute_Attribute, gen_requirement_ObjectAttribute_Attribute, gen_requirement_ProblemChapter_SpecialChapter, gen_requirement_TrashChapter_SpecialChapter, gen_requirement_Requirement_IdentifiedElement, gen_requirement_AnonymousRequirement_Requirement, gen_requirement_DeletedChapter_SpecialChapter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)