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
TextFragmentContainer = Class(name="TextFragmentContainer")
NamedElement = Class(name="NamedElement")
documentation_Subsection = Class(name="documentation_Subsection")
Fragment = Class(name="Fragment")
documentation_Documentation = Class(name="documentation_Documentation")
documentation_Section = Class(name="documentation_Section")
documentation_TermEntry = Class(name="documentation_TermEntry")
documentation_Paragraph = Class(name="documentation_Paragraph")
documentation_Line = Class(name="documentation_Line")
documentation_Subsubsection = Class(name="documentation_Subsubsection")
documentation_TextFragmentContainer = Class(name="documentation_TextFragmentContainer", is_abstract=True)
documentation_Fragment = Class(name="documentation_Fragment", is_abstract=True)
documentation_NamedElement = Class(name="documentation_NamedElement", is_abstract=True)
documentation_List = Class(name="documentation_List")
documentation_ListItem = Class(name="documentation_ListItem")
documentation_Image = Class(name="documentation_Image")
documentation_Table = Class(name="documentation_Table")
documentation_TableHeader = Class(name="documentation_TableHeader")
documentation_TableRow = Class(name="documentation_TableRow")
documentation_XML = Class(name="documentation_XML")

# TextFragmentContainer class attributes and methods

# NamedElement class attributes and methods

# documentation_Subsection class attributes and methods

# Fragment class attributes and methods

# documentation_Documentation class attributes and methods
documentation_Documentation_title: Property = Property(name="title", type=StringType)
documentation_Documentation.attributes={documentation_Documentation_title}

# documentation_Section class attributes and methods

# documentation_TermEntry class attributes and methods
documentation_TermEntry_description: Property = Property(name="description", type=StringType)
documentation_TermEntry.attributes={documentation_TermEntry_description}

# documentation_Paragraph class attributes and methods

# documentation_Line class attributes and methods
documentation_Line_text: Property = Property(name="text", type=StringType)
documentation_Line.attributes={documentation_Line_text}

# documentation_Subsubsection class attributes and methods

# documentation_TextFragmentContainer class attributes and methods

# documentation_Fragment class attributes and methods

# documentation_NamedElement class attributes and methods
documentation_NamedElement_id: Property = Property(name="id", type=StringType)
documentation_NamedElement_name: Property = Property(name="name", type=StringType)
documentation_NamedElement.attributes={documentation_NamedElement_name, documentation_NamedElement_id}

# documentation_List class attributes and methods

# documentation_ListItem class attributes and methods
documentation_ListItem_text: Property = Property(name="text", type=StringType)
documentation_ListItem.attributes={documentation_ListItem_text}

# documentation_Image class attributes and methods
documentation_Image_width: Property = Property(name="width", type=StringType)
documentation_Image_originalSource: Property = Property(name="originalSource", type=StringType)
documentation_Image.attributes={documentation_Image_width, documentation_Image_originalSource}

# documentation_Table class attributes and methods

# documentation_TableHeader class attributes and methods
documentation_TableHeader_headerCells: Property = Property(name="headerCells", type=StringType)
documentation_TableHeader.attributes={documentation_TableHeader_headerCells}

# documentation_TableRow class attributes and methods
documentation_TableRow_rowCells: Property = Property(name="rowCells", type=StringType)
documentation_TableRow.attributes={documentation_TableRow_rowCells}

# documentation_XML class attributes and methods
documentation_XML_contextClassName: Property = Property(name="contextClassName", type=StringType)
documentation_XML_resource: Property = Property(name="resource", type=StringType)
documentation_XML.attributes={documentation_XML_contextClassName, documentation_XML_resource}

# Relationships
sections0: BinaryAssociation = BinaryAssociation(
    name="sections0",
    ends={
        Property(name="documentation_Section", type=documentation_Documentation, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_Documentation", type=documentation_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
terminology1: BinaryAssociation = BinaryAssociation(
    name="terminology1",
    ends={
        Property(name="documentation_TermEntry", type=documentation_Documentation, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_Documentation2", type=documentation_TermEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragments3: BinaryAssociation = BinaryAssociation(
    name="fragments3",
    ends={
        Property(name="documentation_Fragment", type=documentation_TextFragmentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_TextFragmentContainer", type=documentation_Fragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items4: BinaryAssociation = BinaryAssociation(
    name="items4",
    ends={
        Property(name="documentation_ListItem", type=documentation_List, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_List", type=documentation_ListItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tableHeader5: BinaryAssociation = BinaryAssociation(
    name="tableHeader5",
    ends={
        Property(name="documentation_TableHeader", type=documentation_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_Table", type=documentation_TableHeader, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tableRows6: BinaryAssociation = BinaryAssociation(
    name="tableRows6",
    ends={
        Property(name="documentation_TableRow", type=documentation_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation_Table7", type=documentation_TableRow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_documentation_Section_TextFragmentContainer = Generalization(general=TextFragmentContainer, specific=documentation_Section)
gen_documentation_Section_NamedElement = Generalization(general=NamedElement, specific=documentation_Section)
gen_documentation_Subsection_TextFragmentContainer = Generalization(general=TextFragmentContainer, specific=documentation_Subsection)
gen_documentation_Subsection_Fragment = Generalization(general=Fragment, specific=documentation_Subsection)
gen_documentation_Subsection_NamedElement = Generalization(general=NamedElement, specific=documentation_Subsection)
gen_documentation_Paragraph_TextFragmentContainer = Generalization(general=TextFragmentContainer, specific=documentation_Paragraph)
gen_documentation_Paragraph_Fragment = Generalization(general=Fragment, specific=documentation_Paragraph)
gen_documentation_Line_Fragment = Generalization(general=Fragment, specific=documentation_Line)
gen_documentation_Subsubsection_TextFragmentContainer = Generalization(general=TextFragmentContainer, specific=documentation_Subsubsection)
gen_documentation_Subsubsection_Fragment = Generalization(general=Fragment, specific=documentation_Subsubsection)
gen_documentation_Subsubsection_NamedElement = Generalization(general=NamedElement, specific=documentation_Subsubsection)
gen_documentation_List_Fragment = Generalization(general=Fragment, specific=documentation_List)
gen_documentation_ListItem_TextFragmentContainer = Generalization(general=TextFragmentContainer, specific=documentation_ListItem)
gen_documentation_Image_Fragment = Generalization(general=Fragment, specific=documentation_Image)
gen_documentation_Image_NamedElement = Generalization(general=NamedElement, specific=documentation_Image)
gen_documentation_Table_Fragment = Generalization(general=Fragment, specific=documentation_Table)
gen_documentation_XML_Fragment = Generalization(general=Fragment, specific=documentation_XML)
gen_documentation_XML_NamedElement = Generalization(general=NamedElement, specific=documentation_XML)
gen_documentation_TermEntry_NamedElement = Generalization(general=NamedElement, specific=documentation_TermEntry)

# Domain Model
domain_model = DomainModel(
    name="documentation",
    types={TextFragmentContainer, NamedElement, documentation_Subsection, Fragment, documentation_Documentation, documentation_Section, documentation_TermEntry, documentation_Paragraph, documentation_Line, documentation_Subsubsection, documentation_TextFragmentContainer, documentation_Fragment, documentation_NamedElement, documentation_List, documentation_ListItem, documentation_Image, documentation_Table, documentation_TableHeader, documentation_TableRow, documentation_XML},
    associations={sections0, terminology1, fragments3, items4, tableHeader5, tableRows6},
    generalizations={gen_documentation_Section_TextFragmentContainer, gen_documentation_Section_NamedElement, gen_documentation_Subsection_TextFragmentContainer, gen_documentation_Subsection_Fragment, gen_documentation_Subsection_NamedElement, gen_documentation_Paragraph_TextFragmentContainer, gen_documentation_Paragraph_Fragment, gen_documentation_Line_Fragment, gen_documentation_Subsubsection_TextFragmentContainer, gen_documentation_Subsubsection_Fragment, gen_documentation_Subsubsection_NamedElement, gen_documentation_List_Fragment, gen_documentation_ListItem_TextFragmentContainer, gen_documentation_Image_Fragment, gen_documentation_Image_NamedElement, gen_documentation_Table_Fragment, gen_documentation_XML_Fragment, gen_documentation_XML_NamedElement, gen_documentation_TermEntry_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)