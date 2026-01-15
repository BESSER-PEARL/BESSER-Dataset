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
Documentation_Paragraph = Class(name="Documentation::Paragraph")
Documentation_ParagraphValue = Class(name="Documentation::ParagraphValue", is_abstract=True)
Documentation_Book = Class(name="Documentation::Book")
Documentation_Section = Class(name="Documentation::Section")
Documentation_ItemizedListValue = Class(name="Documentation::ItemizedListValue")
Documentation_TextualValue = Class(name="Documentation::TextualValue")
ParagraphValue = Class(name="ParagraphValue")
Documentation_XRefValue = Class(name="Documentation::XRefValue")
Documentation_ItemizedListValueItem = Class(name="Documentation::ItemizedListValueItem")
Paragraph = Class(name="Paragraph")
Documentation_EmphasisValue = Class(name="Documentation::EmphasisValue")
TextualValue = Class(name="TextualValue")
Documentation_InformalTableValue = Class(name="Documentation::InformalTableValue")
Documentation_InformalTableValueRow = Class(name="Documentation::InformalTableValueRow")

# Documentation_Paragraph class attributes and methods

# Documentation_ParagraphValue class attributes and methods

# Documentation_Book class attributes and methods
Documentation_Book_title: Property = Property(name="title", type=StringType)
Documentation_Book.attributes={Documentation_Book_title}

# Documentation_Section class attributes and methods
Documentation_Section_title: Property = Property(name="title", type=StringType)
Documentation_Section.attributes={Documentation_Section_title}

# Documentation_ItemizedListValue class attributes and methods

# Documentation_TextualValue class attributes and methods
Documentation_TextualValue_value: Property = Property(name="value", type=StringType)
Documentation_TextualValue.attributes={Documentation_TextualValue_value}

# ParagraphValue class attributes and methods

# Documentation_XRefValue class attributes and methods

# Documentation_ItemizedListValueItem class attributes and methods

# Paragraph class attributes and methods

# Documentation_EmphasisValue class attributes and methods
Documentation_EmphasisValue_role: Property = Property(name="role", type=StringType)
Documentation_EmphasisValue.attributes={Documentation_EmphasisValue_role}

# TextualValue class attributes and methods

# Documentation_InformalTableValue class attributes and methods
Documentation_InformalTableValue_cols: Property = Property(name="cols", type=IntegerType)
Documentation_InformalTableValue.attributes={Documentation_InformalTableValue_cols}

# Documentation_InformalTableValueRow class attributes and methods

# Relationships
values1: BinaryAssociation = BinaryAssociation(
    name="values1",
    ends={
        Property(name="Documentation_ParagraphValue", type=Documentation_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_Paragraph", type=Documentation_ParagraphValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="Documentation_Section", type=Documentation_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_Book", type=Documentation_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
headRows12: BinaryAssociation = BinaryAssociation(
    name="headRows12",
    ends={
        Property(name="Documentation_InformalTableValueRow14", type=Documentation_InformalTableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_InformalTableValue13", type=Documentation_InformalTableValueRow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkend9: BinaryAssociation = BinaryAssociation(
    name="linkend9",
    ends={
        Property(name="Documentation_Section10", type=Documentation_XRefValue, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_XRefValue", type=Documentation_Section, multiplicity=Multiplicity(1, 1))
    }
)
bodyRows11: BinaryAssociation = BinaryAssociation(
    name="bodyRows11",
    ends={
        Property(name="Documentation_InformalTableValueRow", type=Documentation_InformalTableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_InformalTableValue", type=Documentation_InformalTableValueRow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry15: BinaryAssociation = BinaryAssociation(
    name="entry15",
    ends={
        Property(name="Documentation_TextualValue", type=Documentation_InformalTableValueRow, multiplicity=Multiplicity(1, 1)),
        Property(name="Documentation_InformalTableValueRow16", type=Documentation_TextualValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Documentation_ItemizedListValue_ParagraphValue = Generalization(general=ParagraphValue, specific=Documentation_ItemizedListValue)
gen_Documentation_TextualValue_ParagraphValue = Generalization(general=ParagraphValue, specific=Documentation_TextualValue)
gen_Documentation_XRefValue_ParagraphValue = Generalization(general=ParagraphValue, specific=Documentation_XRefValue)
gen_Documentation_ItemizedListValueItem_Paragraph = Generalization(general=Paragraph, specific=Documentation_ItemizedListValueItem)
gen_Documentation_EmphasisValue_ParagraphValue = Generalization(general=ParagraphValue, specific=Documentation_EmphasisValue)
gen_Documentation_EmphasisValue_TextualValue = Generalization(general=TextualValue, specific=Documentation_EmphasisValue)
gen_Documentation_InformalTableValue_ParagraphValue = Generalization(general=ParagraphValue, specific=Documentation_InformalTableValue)

# Domain Model
domain_model = DomainModel(
    name="Documentation",
    types={Documentation_Paragraph, Documentation_ParagraphValue, Documentation_Book, Documentation_Section, Documentation_ItemizedListValue, Documentation_TextualValue, ParagraphValue, Documentation_XRefValue, Documentation_ItemizedListValueItem, Paragraph, Documentation_EmphasisValue, TextualValue, Documentation_InformalTableValue, Documentation_InformalTableValueRow},
    associations={values1, content0, section3, para5, items8, headRows12, linkend9, bodyRows11, entry15},
    generalizations={gen_Documentation_ItemizedListValue_ParagraphValue, gen_Documentation_TextualValue_ParagraphValue, gen_Documentation_XRefValue_ParagraphValue, gen_Documentation_ItemizedListValueItem_Paragraph, gen_Documentation_EmphasisValue_ParagraphValue, gen_Documentation_EmphasisValue_TextualValue, gen_Documentation_InformalTableValue_ParagraphValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)