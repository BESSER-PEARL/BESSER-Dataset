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
Reqtify_Document = Class(name="Reqtify_Document")
ElementWithIL = Class(name="ElementWithIL")
Project = Class(name="Project")
Section = Class(name="Section")
Reqtify_TextElement = Class(name="Reqtify_TextElement", is_abstract=True)
Reqtify_Project = Class(name="Reqtify_Project")
Document = Class(name="Document")
Reqtify_TypedElement = Class(name="Reqtify_TypedElement", is_abstract=True)
Reqtify_ElementWithIL = Class(name="Reqtify_ElementWithIL", is_abstract=True)
TypedElement = Class(name="TypedElement")
MacroRequirement = Class(name="MacroRequirement")
CoverLink = Class(name="CoverLink")
Attribute = Class(name="Attribute")
Reqtify_Requirement = Class(name="Reqtify_Requirement")
Reqtify_Section = Class(name="Reqtify_Section")
TextElement = Class(name="TextElement")
AbstractRequirement = Class(name="AbstractRequirement")
Reqtify_AbstractRequirement = Class(name="Reqtify_AbstractRequirement", is_abstract=True)
Reqtify_MacroRequirement = Class(name="Reqtify_MacroRequirement")
Reqtify_CoverLink = Class(name="Reqtify_CoverLink")
Reqtify_Attribute = Class(name="Reqtify_Attribute")

# Reqtify_Document class attributes and methods

# ElementWithIL class attributes and methods

# Project class attributes and methods

# Section class attributes and methods

# Reqtify_TextElement class attributes and methods
Reqtify_TextElement_description: Property = Property(name="description", type=StringType)
Reqtify_TextElement.attributes={Reqtify_TextElement_description}

# Reqtify_Project class attributes and methods

# Document class attributes and methods

# Reqtify_TypedElement class attributes and methods
Reqtify_TypedElement_type: Property = Property(name="type", type=StringType)
Reqtify_TypedElement.attributes={Reqtify_TypedElement_type}

# Reqtify_ElementWithIL class attributes and methods
Reqtify_ElementWithIL_label: Property = Property(name="label", type=StringType)
Reqtify_ElementWithIL_name: Property = Property(name="name", type=StringType)
Reqtify_ElementWithIL.attributes={Reqtify_ElementWithIL_label, Reqtify_ElementWithIL_name}

# TypedElement class attributes and methods

# MacroRequirement class attributes and methods

# CoverLink class attributes and methods

# Attribute class attributes and methods

# Reqtify_Requirement class attributes and methods

# Reqtify_Section class attributes and methods

# TextElement class attributes and methods

# AbstractRequirement class attributes and methods

# Reqtify_AbstractRequirement class attributes and methods

# Reqtify_MacroRequirement class attributes and methods

# Reqtify_CoverLink class attributes and methods

# Reqtify_Attribute class attributes and methods
Reqtify_Attribute_value: Property = Property(name="value", type=StringType)
Reqtify_Attribute.attributes={Reqtify_Attribute_value}

# Relationships
project1: BinaryAssociation = BinaryAssociation(
    name="project1",
    ends={
        Property(name="Project", type=Reqtify_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="documents", type=Project, multiplicity=Multiplicity(1, 1))
    }
)
sections2: BinaryAssociation = BinaryAssociation(
    name="sections2",
    ends={
        Property(name="Section", type=Reqtify_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="document", type=Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documents0: BinaryAssociation = BinaryAssociation(
    name="documents0",
    ends={
        Property(name="Document", type=Reqtify_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project", type=Document, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
isContained12: BinaryAssociation = BinaryAssociation(
    name="isContained12",
    ends={
        Property(name="MacroRequirement", type=Reqtify_AbstractRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="contains", type=MacroRequirement, multiplicity=Multiplicity(0, 1))
    }
)
coverLinks13: BinaryAssociation = BinaryAssociation(
    name="coverLinks13",
    ends={
        Property(name="CoverLink", type=Reqtify_AbstractRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="Reqtify_AbstractRequirement", type=CoverLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute14: BinaryAssociation = BinaryAssociation(
    name="attribute14",
    ends={
        Property(name="Attribute", type=Reqtify_AbstractRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="Reqtify_AbstractRequirement15", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
document3: BinaryAssociation = BinaryAssociation(
    name="document3",
    ends={
        Property(name="Document4", type=Reqtify_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="sections", type=Document, multiplicity=Multiplicity(0, 1))
    }
)
sectionChildren5: BinaryAssociation = BinaryAssociation(
    name="sectionChildren5",
    ends={
        Property(name="Section6", type=Reqtify_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="sectionParent", type=Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sectionParent7: BinaryAssociation = BinaryAssociation(
    name="sectionParent7",
    ends={
        Property(name="Section8", type=Reqtify_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="sectionChildren", type=Section, multiplicity=Multiplicity(0, 1))
    }
)
requirements9: BinaryAssociation = BinaryAssociation(
    name="requirements9",
    ends={
        Property(name="AbstractRequirement", type=Reqtify_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="section", type=AbstractRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
section10: BinaryAssociation = BinaryAssociation(
    name="section10",
    ends={
        Property(name="Section11", type=Reqtify_AbstractRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements", type=Section, multiplicity=Multiplicity(0, 1))
    }
)
contains16: BinaryAssociation = BinaryAssociation(
    name="contains16",
    ends={
        Property(name="AbstractRequirement17", type=Reqtify_MacroRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="isContained", type=AbstractRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkWith18: BinaryAssociation = BinaryAssociation(
    name="linkWith18",
    ends={
        Property(name="AbstractRequirement19", type=Reqtify_CoverLink, multiplicity=Multiplicity(1, 1)),
        Property(name="Reqtify_CoverLink", type=AbstractRequirement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Reqtify_Document_ElementWithIL = Generalization(general=ElementWithIL, specific=Reqtify_Document)
gen_Reqtify_TextElement_ElementWithIL = Generalization(general=ElementWithIL, specific=Reqtify_TextElement)
gen_Reqtify_ElementWithIL_TypedElement = Generalization(general=TypedElement, specific=Reqtify_ElementWithIL)
gen_Reqtify_Requirement_AbstractRequirement = Generalization(general=AbstractRequirement, specific=Reqtify_Requirement)
gen_Reqtify_Section_TextElement = Generalization(general=TextElement, specific=Reqtify_Section)
gen_Reqtify_AbstractRequirement_TextElement = Generalization(general=TextElement, specific=Reqtify_AbstractRequirement)
gen_Reqtify_MacroRequirement_AbstractRequirement = Generalization(general=AbstractRequirement, specific=Reqtify_MacroRequirement)
gen_Reqtify_CoverLink_TypedElement = Generalization(general=TypedElement, specific=Reqtify_CoverLink)
gen_Reqtify_Attribute_TypedElement = Generalization(general=TypedElement, specific=Reqtify_Attribute)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Reqtify_Document, ElementWithIL, Project, Section, Reqtify_TextElement, Reqtify_Project, Document, Reqtify_TypedElement, Reqtify_ElementWithIL, TypedElement, MacroRequirement, CoverLink, Attribute, Reqtify_Requirement, Reqtify_Section, TextElement, AbstractRequirement, Reqtify_AbstractRequirement, Reqtify_MacroRequirement, Reqtify_CoverLink, Reqtify_Attribute},
    associations={project1, sections2, documents0, isContained12, coverLinks13, attribute14, document3, sectionChildren5, sectionParent7, requirements9, section10, contains16, linkWith18},
    generalizations={gen_Reqtify_Document_ElementWithIL, gen_Reqtify_TextElement_ElementWithIL, gen_Reqtify_ElementWithIL_TypedElement, gen_Reqtify_Requirement_AbstractRequirement, gen_Reqtify_Section_TextElement, gen_Reqtify_AbstractRequirement_TextElement, gen_Reqtify_MacroRequirement_AbstractRequirement, gen_Reqtify_CoverLink_TypedElement, gen_Reqtify_Attribute_TypedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)