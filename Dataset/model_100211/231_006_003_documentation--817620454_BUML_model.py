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
Unit: Enumeration = Enumeration(
    name="Unit",
    literals={
            EnumerationLiteral(name="PERCENT"),
			EnumerationLiteral(name="PIXELS")
    }
)

# Classes
documentation_Documentation = Class(name="documentation_Documentation")
documentation_Section = Class(name="documentation_Section")
documentation_TermEntry = Class(name="documentation_TermEntry")
documentation_Fragment = Class(name="documentation_Fragment", is_abstract=True)
documentation_Line = Class(name="documentation_Line")
Text = Class(name="Text")
documentation_List = Class(name="documentation_List")
FragmentContainer = Class(name="FragmentContainer")
NamedElement = Class(name="NamedElement")
documentation_Subsection = Class(name="documentation_Subsection")
Fragment = Class(name="Fragment")
documentation_Subsubsection = Class(name="documentation_Subsubsection")
documentation_Paragraph = Class(name="documentation_Paragraph")
TextContainer = Class(name="TextContainer")
documentation_NamedElement = Class(name="documentation_NamedElement", is_abstract=True)
documentation_ListItem = Class(name="documentation_ListItem")
documentation_Table = Class(name="documentation_Table")
documentation_TableCell = Class(name="documentation_TableCell")
documentation_TableHeader = Class(name="documentation_TableHeader")
documentation_TableRow = Class(name="documentation_TableRow")
documentation_Image = Class(name="documentation_Image")
documentation_Width = Class(name="documentation_Width")
documentation_XML = Class(name="documentation_XML")
documentation_PageBreak = Class(name="documentation_PageBreak")
documentation_Code = Class(name="documentation_Code")
documentation_Listing = Class(name="documentation_Listing")
documentation_Reference = Class(name="documentation_Reference")
documentation_HtmlCode = Class(name="documentation_HtmlCode")
documentation_FragmentContainer = Class(name="documentation_FragmentContainer", is_abstract=True)
documentation_Link = Class(name="documentation_Link")
documentation_TextContainer = Class(name="documentation_TextContainer", is_abstract=True)
documentation_Text = Class(name="documentation_Text", is_abstract=True)

# documentation_Documentation class attributes and methods
documentation_Documentation_title: Property = Property(name="title", type=StringType)
documentation_Documentation.attributes={documentation_Documentation_title}

# documentation_Section class attributes and methods

# documentation_TermEntry class attributes and methods
documentation_TermEntry_description: Property = Property(name="description", type=StringType)
documentation_TermEntry.attributes={documentation_TermEntry_description}

# documentation_Fragment class attributes and methods

# documentation_Line class attributes and methods

# Text class attributes and methods

# documentation_List class attributes and methods

# FragmentContainer class attributes and methods

# NamedElement class attributes and methods

# documentation_Subsection class attributes and methods

# Fragment class attributes and methods

# documentation_Subsubsection class attributes and methods

# documentation_Paragraph class attributes and methods

# TextContainer class attributes and methods

# documentation_NamedElement class attributes and methods
documentation_NamedElement_id: Property = Property(name="id", type=StringType)
documentation_NamedElement_name: Property = Property(name="name", type=StringType)
documentation_NamedElement_label: Property = Property(name="label", type=StringType)
documentation_NamedElement.attributes={documentation_NamedElement_name, documentation_NamedElement_label, documentation_NamedElement_id}

# documentation_ListItem class attributes and methods
documentation_ListItem_text: Property = Property(name="text", type=StringType)
documentation_ListItem.attributes={documentation_ListItem_text}

# documentation_Table class attributes and methods

# documentation_TableCell class attributes and methods
documentation_TableCell_content: Property = Property(name="content", type=StringType)
documentation_TableCell_span: Property = Property(name="span", type=IntegerType)
documentation_TableCell.attributes={documentation_TableCell_content, documentation_TableCell_span}

# documentation_TableHeader class attributes and methods

# documentation_TableRow class attributes and methods

# documentation_Image class attributes and methods
documentation_Image_originalSource: Property = Property(name="originalSource", type=StringType)
documentation_Image_resource: Property = Property(name="resource", type=StringType)
documentation_Image_contextClassName: Property = Property(name="contextClassName", type=StringType)
documentation_Image.attributes={documentation_Image_resource, documentation_Image_originalSource, documentation_Image_contextClassName}

# documentation_Width class attributes and methods
documentation_Width_width: Property = Property(name="width", type=StringType)
documentation_Width_unit: Property = Property(name="unit", type=StringType)
documentation_Width.attributes={documentation_Width_width, documentation_Width_unit}

# documentation_XML class attributes and methods
documentation_XML_contextClassName: Property = Property(name="contextClassName", type=StringType)
documentation_XML_resource: Property = Property(name="resource", type=StringType)
documentation_XML_content: Property = Property(name="content", type=StringType)
documentation_XML.attributes={documentation_XML_resource, documentation_XML_contextClassName, documentation_XML_content}

# documentation_PageBreak class attributes and methods

# documentation_Code class attributes and methods

# documentation_Listing class attributes and methods

# documentation_Reference class attributes and methods
documentation_Reference_referredLabel: Property = Property(name="referredLabel", type=StringType)
documentation_Reference.attributes={documentation_Reference_referredLabel}

# documentation_HtmlCode class attributes and methods

# documentation_FragmentContainer class attributes and methods

# documentation_Link class attributes and methods
documentation_Link_uri: Property = Property(name="uri", type=StringType)
documentation_Link.attributes={documentation_Link_uri}

# documentation_TextContainer class attributes and methods

# documentation_Text class attributes and methods
documentation_Text_text: Property = Property(name="text", type=StringType)
documentation_Text.attributes={documentation_Text_text}

# Relationships
terminology1: BinaryAssociation = BinaryAssociation(
    name="terminology1",
    ends={
        Property(name="documentation_TermEntry", type=documentation_Documentation, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_Documentation2", type=documentation_TermEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sections0: BinaryAssociation = BinaryAssociation(
    name="sections0",
    ends={
        Property(name="documentation_Section", type=documentation_Documentation, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_Documentation", type=documentation_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items3: BinaryAssociation = BinaryAssociation(
    name="items3",
    ends={
        Property(name="documentation_ListItem", type=documentation_List, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_List", type=documentation_ListItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
headerCells7: BinaryAssociation = BinaryAssociation(
    name="headerCells7",
    ends={
        Property(name="documentation_TableCell", type=documentation_TableHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_TableHeader8", type=documentation_TableCell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tableHeader4: BinaryAssociation = BinaryAssociation(
    name="tableHeader4",
    ends={
        Property(name="documentation_TableHeader", type=documentation_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_Table", type=documentation_TableHeader, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tableRows5: BinaryAssociation = BinaryAssociation(
    name="tableRows5",
    ends={
        Property(name="documentation_TableRow", type=documentation_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_Table6", type=documentation_TableRow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rowCells9: BinaryAssociation = BinaryAssociation(
    name="rowCells9",
    ends={
        Property(name="documentation_TableCell11", type=documentation_TableRow, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_TableRow10", type=documentation_TableCell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
width12: BinaryAssociation = BinaryAssociation(
    name="width12",
    ends={
        Property(name="documentation_Width", type=documentation_Image, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_Image", type=documentation_Width, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments13: BinaryAssociation = BinaryAssociation(
    name="fragments13",
    ends={
        Property(name="documentation_Fragment", type=documentation_FragmentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_FragmentContainer", type=documentation_Fragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
texts14: BinaryAssociation = BinaryAssociation(
    name="texts14",
    ends={
        Property(name="documentation_Text", type=documentation_TextContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_TextContainer", type=documentation_Text, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_documentation_Line_Text = Generalization(general=Text, specific=documentation_Line)
gen_documentation_Section_FragmentContainer = Generalization(general=FragmentContainer, specific=documentation_Section)
gen_documentation_Section_NamedElement = Generalization(general=NamedElement, specific=documentation_Section)
gen_documentation_Subsection_FragmentContainer = Generalization(general=FragmentContainer, specific=documentation_Subsection)
gen_documentation_Subsection_Fragment = Generalization(general=Fragment, specific=documentation_Subsection)
gen_documentation_Subsection_NamedElement = Generalization(general=NamedElement, specific=documentation_Subsection)
gen_documentation_Subsubsection_FragmentContainer = Generalization(general=FragmentContainer, specific=documentation_Subsubsection)
gen_documentation_Subsubsection_Fragment = Generalization(general=Fragment, specific=documentation_Subsubsection)
gen_documentation_Subsubsection_NamedElement = Generalization(general=NamedElement, specific=documentation_Subsubsection)
gen_documentation_Paragraph_Fragment = Generalization(general=Fragment, specific=documentation_Paragraph)
gen_documentation_Paragraph_TextContainer = Generalization(general=TextContainer, specific=documentation_Paragraph)
gen_documentation_List_Fragment = Generalization(general=Fragment, specific=documentation_List)
gen_documentation_Table_Fragment = Generalization(general=Fragment, specific=documentation_Table)
gen_documentation_Image_Fragment = Generalization(general=Fragment, specific=documentation_Image)
gen_documentation_Image_NamedElement = Generalization(general=NamedElement, specific=documentation_Image)
gen_documentation_XML_Fragment = Generalization(general=Fragment, specific=documentation_XML)
gen_documentation_XML_NamedElement = Generalization(general=NamedElement, specific=documentation_XML)
gen_documentation_PageBreak_Fragment = Generalization(general=Fragment, specific=documentation_PageBreak)
gen_documentation_TermEntry_NamedElement = Generalization(general=NamedElement, specific=documentation_TermEntry)
gen_documentation_Code_Text = Generalization(general=Text, specific=documentation_Code)
gen_documentation_Listing_Fragment = Generalization(general=Fragment, specific=documentation_Listing)
gen_documentation_Listing_TextContainer = Generalization(general=TextContainer, specific=documentation_Listing)
gen_documentation_Reference_Text = Generalization(general=Text, specific=documentation_Reference)
gen_documentation_Reference_NamedElement = Generalization(general=NamedElement, specific=documentation_Reference)
gen_documentation_HtmlCode_Text = Generalization(general=Text, specific=documentation_HtmlCode)
gen_documentation_FragmentContainer_TextContainer = Generalization(general=TextContainer, specific=documentation_FragmentContainer)
gen_documentation_Link_Fragment = Generalization(general=Fragment, specific=documentation_Link)
gen_documentation_Link_NamedElement = Generalization(general=NamedElement, specific=documentation_Link)
gen_documentation_Text_Fragment = Generalization(general=Fragment, specific=documentation_Text)

# Domain Model
domain_model = DomainModel(
    name="documentation",
    types={documentation_Documentation, documentation_Section, documentation_TermEntry, documentation_Fragment, documentation_Line, Text, documentation_List, FragmentContainer, NamedElement, documentation_Subsection, Fragment, documentation_Subsubsection, documentation_Paragraph, TextContainer, documentation_NamedElement, documentation_ListItem, documentation_Table, documentation_TableCell, documentation_TableHeader, documentation_TableRow, documentation_Image, documentation_Width, documentation_XML, documentation_PageBreak, documentation_Code, documentation_Listing, documentation_Reference, documentation_HtmlCode, documentation_FragmentContainer, documentation_Link, documentation_TextContainer, documentation_Text, Unit},
    associations={terminology1, sections0, items3, headerCells7, tableHeader4, tableRows5, rowCells9, width12, fragments13, texts14},
    generalizations={gen_documentation_Line_Text, gen_documentation_Section_FragmentContainer, gen_documentation_Section_NamedElement, gen_documentation_Subsection_FragmentContainer, gen_documentation_Subsection_Fragment, gen_documentation_Subsection_NamedElement, gen_documentation_Subsubsection_FragmentContainer, gen_documentation_Subsubsection_Fragment, gen_documentation_Subsubsection_NamedElement, gen_documentation_Paragraph_Fragment, gen_documentation_Paragraph_TextContainer, gen_documentation_List_Fragment, gen_documentation_Table_Fragment, gen_documentation_Image_Fragment, gen_documentation_Image_NamedElement, gen_documentation_XML_Fragment, gen_documentation_XML_NamedElement, gen_documentation_PageBreak_Fragment, gen_documentation_TermEntry_NamedElement, gen_documentation_Code_Text, gen_documentation_Listing_Fragment, gen_documentation_Listing_TextContainer, gen_documentation_Reference_Text, gen_documentation_Reference_NamedElement, gen_documentation_HtmlCode_Text, gen_documentation_FragmentContainer_TextContainer, gen_documentation_Link_Fragment, gen_documentation_Link_NamedElement, gen_documentation_Text_Fragment},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)