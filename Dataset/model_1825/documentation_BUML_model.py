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
Documentation_Book = Class(name="Documentation::Book")
Paragraph = Class(name="Paragraph")
Documentation_Section = Class(name="Documentation::Section")
Documentation_Paragraph = Class(name="Documentation::Paragraph")
Documentation_ParagraphValue = Class(name="Documentation::ParagraphValue", is_abstract=True)
Documentation_TextualValue = Class(name="Documentation::TextualValue")
ParagraphValue = Class(name="ParagraphValue")
Documentation_ItemizedListValue = Class(name="Documentation::ItemizedListValue")
Documentation_ItemizedListValueItem = Class(name="Documentation::ItemizedListValueItem")
Documentation_EmphasisValue = Class(name="Documentation::EmphasisValue")
Documentation_XRefValue = Class(name="Documentation::XRefValue")
Documentation_InformalTableValue = Class(name="Documentation::InformalTableValue")
Documentation_InformalTableValueGroup = Class(name="Documentation::InformalTableValueGroup")
Documentation_InformalTableValueHead = Class(name="Documentation::InformalTableValueHead")
Documentation_InformalTableValueBody = Class(name="Documentation::InformalTableValueBody")
Documentation_InformalTableValueRow = Class(name="Documentation::InformalTableValueRow")
Documentation_InformalTableValueEntry = Class(name="Documentation::InformalTableValueEntry")

# Documentation_Book class attributes and methods
Documentation_Book_title: Property = Property(name="title", type=StringType)
Documentation_Book.attributes={Documentation_Book_title}

# Paragraph class attributes and methods

# Documentation_Section class attributes and methods
Documentation_Section_title: Property = Property(name="title", type=StringType)
Documentation_Section.attributes={Documentation_Section_title}

# Documentation_Paragraph class attributes and methods

# Documentation_ParagraphValue class attributes and methods

# Documentation_TextualValue class attributes and methods
Documentation_TextualValue_value: Property = Property(name="value", type=StringType)
Documentation_TextualValue.attributes={Documentation_TextualValue_value}

# ParagraphValue class attributes and methods

# Documentation_ItemizedListValue class attributes and methods

# Documentation_ItemizedListValueItem class attributes and methods

# Documentation_EmphasisValue class attributes and methods
Documentation_EmphasisValue_value: Property = Property(name="value", type=StringType)
Documentation_EmphasisValue_role: Property = Property(name="role", type=StringType)
Documentation_EmphasisValue.attributes={Documentation_EmphasisValue_value, Documentation_EmphasisValue_role}

# Documentation_XRefValue class attributes and methods

# Documentation_InformalTableValue class attributes and methods

# Documentation_InformalTableValueGroup class attributes and methods
Documentation_InformalTableValueGroup_cols: Property = Property(name="cols", type=IntegerType)
Documentation_InformalTableValueGroup.attributes={Documentation_InformalTableValueGroup_cols}

# Documentation_InformalTableValueHead class attributes and methods

# Documentation_InformalTableValueBody class attributes and methods

# Documentation_InformalTableValueRow class attributes and methods

# Documentation_InformalTableValueEntry class attributes and methods
Documentation_InformalTableValueEntry_value: Property = Property(name="value", type=StringType)
Documentation_InformalTableValueEntry.attributes={Documentation_InformalTableValueEntry_value}

# Relationships
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="Documentation_Section", type=Documentation_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_Book", type=Documentation_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values1: BinaryAssociation = BinaryAssociation(
    name="values1",
    ends={
        Property(name="Documentation_ParagraphValue", type=Documentation_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_Paragraph", type=Documentation_ParagraphValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
section3: BinaryAssociation = BinaryAssociation(
    name="section3",
    ends={
        Property(name="Documentation_Section4", type=Documentation_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_Section2", type=Documentation_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
para5: BinaryAssociation = BinaryAssociation(
    name="para5",
    ends={
        Property(name="Documentation_Paragraph7", type=Documentation_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_Section6", type=Documentation_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items8: BinaryAssociation = BinaryAssociation(
    name="items8",
    ends={
        Property(name="Documentation_ItemizedListValueItem", type=Documentation_ItemizedListValue, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_ItemizedListValue", type=Documentation_ItemizedListValueItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkend9: BinaryAssociation = BinaryAssociation(
    name="linkend9",
    ends={
        Property(name="Documentation_Section10", type=Documentation_XRefValue, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_XRefValue", type=Documentation_Section, multiplicity=Multiplicity(1, 1))
    }
)
tgroup11: BinaryAssociation = BinaryAssociation(
    name="tgroup11",
    ends={
        Property(name="Documentation_InformalTableValueGroup", type=Documentation_InformalTableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_InformalTableValue", type=Documentation_InformalTableValueGroup, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thead12: BinaryAssociation = BinaryAssociation(
    name="thead12",
    ends={
        Property(name="Documentation_InformalTableValueHead", type=Documentation_InformalTableValueGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_InformalTableValueGroup13", type=Documentation_InformalTableValueHead, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tbody14: BinaryAssociation = BinaryAssociation(
    name="tbody14",
    ends={
        Property(name="Documentation_InformalTableValueBody", type=Documentation_InformalTableValueGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_InformalTableValueGroup15", type=Documentation_InformalTableValueBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rows16: BinaryAssociation = BinaryAssociation(
    name="rows16",
    ends={
        Property(name="Documentation_InformalTableValueRow", type=Documentation_InformalTableValueHead, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_InformalTableValueHead17", type=Documentation_InformalTableValueRow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rows18: BinaryAssociation = BinaryAssociation(
    name="rows18",
    ends={
        Property(name="Documentation_InformalTableValueRow20", type=Documentation_InformalTableValueBody, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_InformalTableValueBody19", type=Documentation_InformalTableValueRow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry21: BinaryAssociation = BinaryAssociation(
    name="entry21",
    ends={
        Property(name="Documentation_InformalTableValueEntry", type=Documentation_InformalTableValueRow, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_InformalTableValueRow22", type=Documentation_InformalTableValueEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Documentation_ItemizedListValueItem_Paragraph = Generalization(general=Paragraph, specific=Documentation_ItemizedListValueItem)
gen_Documentation_TextualValue_ParagraphValue = Generalization(general=ParagraphValue, specific=Documentation_TextualValue)
gen_Documentation_ItemizedListValue_ParagraphValue = Generalization(general=ParagraphValue, specific=Documentation_ItemizedListValue)
gen_Documentation_EmphasisValue_ParagraphValue = Generalization(general=ParagraphValue, specific=Documentation_EmphasisValue)
gen_Documentation_XRefValue_ParagraphValue = Generalization(general=ParagraphValue, specific=Documentation_XRefValue)
gen_Documentation_InformalTableValue_ParagraphValue = Generalization(general=ParagraphValue, specific=Documentation_InformalTableValue)

# Domain Model
domain_model = DomainModel(
    name="Documentation",
    types={Documentation_Book, Paragraph, Documentation_Section, Documentation_Paragraph, Documentation_ParagraphValue, Documentation_TextualValue, ParagraphValue, Documentation_ItemizedListValue, Documentation_ItemizedListValueItem, Documentation_EmphasisValue, Documentation_XRefValue, Documentation_InformalTableValue, Documentation_InformalTableValueGroup, Documentation_InformalTableValueHead, Documentation_InformalTableValueBody, Documentation_InformalTableValueRow, Documentation_InformalTableValueEntry},
    associations={content0, values1, section3, para5, items8, linkend9, tgroup11, thead12, tbody14, rows16, rows18, entry21},
    generalizations={gen_Documentation_ItemizedListValueItem_Paragraph, gen_Documentation_TextualValue_ParagraphValue, gen_Documentation_ItemizedListValue_ParagraphValue, gen_Documentation_EmphasisValue_ParagraphValue, gen_Documentation_XRefValue_ParagraphValue, gen_Documentation_InformalTableValue_ParagraphValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)