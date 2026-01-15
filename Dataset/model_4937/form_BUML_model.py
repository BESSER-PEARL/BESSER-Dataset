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
TextInputType: Enumeration = Enumeration(
    name="TextInputType",
    literals={
            EnumerationLiteral(name="TEXTAREA"),
			EnumerationLiteral(name="TEXTFIELD"),
			EnumerationLiteral(name="ENCRYPTED_TEXTFIELD")
    }
)

SelectionType: Enumeration = Enumeration(
    name="SelectionType",
    literals={
            EnumerationLiteral(name="RADIO"),
			EnumerationLiteral(name="CHECKBOX"),
			EnumerationLiteral(name="COMBOBOX")
    }
)

# Classes
fml_SelectionItem = Class(name="fml::SelectionItem")
fml_DisplayElement = Class(name="fml::DisplayElement", is_abstract=True)
PageElement = Class(name="PageElement")
fml_Heading = Class(name="fml::Heading")
DisplayElement = Class(name="DisplayElement")
fml_Form = Class(name="fml::Form")
fml_Page = Class(name="fml::Page")
fml_PageElement = Class(name="fml::PageElement", is_abstract=True)
fml_TextParagraph = Class(name="fml::TextParagraph")
fml_List = Class(name="fml::List")
fml_ListItem = Class(name="fml::ListItem")
fml_InputElement = Class(name="fml::InputElement", is_abstract=True)
fml_TextInput = Class(name="fml::TextInput")
InputElement = Class(name="InputElement")
fml_SelectField = Class(name="fml::SelectField")

# fml_SelectionItem class attributes and methods
fml_SelectionItem_Text: Property = Property(name="Text", type=StringType)
fml_SelectionItem_preselected: Property = Property(name="preselected", type=BooleanType)
fml_SelectionItem_selected: Property = Property(name="selected", type=BooleanType)
fml_SelectionItem.attributes={fml_SelectionItem_Text, fml_SelectionItem_selected, fml_SelectionItem_preselected}

# fml_DisplayElement class attributes and methods

# PageElement class attributes and methods

# fml_Heading class attributes and methods
fml_Heading_Level: Property = Property(name="Level", type=StringType)
fml_Heading_Text: Property = Property(name="Text", type=StringType)
fml_Heading.attributes={fml_Heading_Level, fml_Heading_Text}

# DisplayElement class attributes and methods

# fml_Form class attributes and methods

# fml_Page class attributes and methods
fml_Page_Title: Property = Property(name="Title", type=StringType)
fml_Page_isWelcome: Property = Property(name="isWelcome", type=BooleanType)
fml_Page.attributes={fml_Page_Title, fml_Page_isWelcome}

# fml_PageElement class attributes and methods
fml_PageElement_ID: Property = Property(name="ID", type=StringType)
fml_PageElement.attributes={fml_PageElement_ID}

# fml_TextParagraph class attributes and methods
fml_TextParagraph_Text: Property = Property(name="Text", type=StringType)
fml_TextParagraph.attributes={fml_TextParagraph_Text}

# fml_List class attributes and methods
fml_List_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
fml_List.attributes={fml_List_isOrdered}

# fml_ListItem class attributes and methods
fml_ListItem_Text: Property = Property(name="Text", type=StringType)
fml_ListItem.attributes={fml_ListItem_Text}

# fml_InputElement class attributes and methods
fml_InputElement_isMandatory: Property = Property(name="isMandatory", type=BooleanType)
fml_InputElement.attributes={fml_InputElement_isMandatory}

# fml_TextInput class attributes and methods
fml_TextInput_Label: Property = Property(name="Label", type=StringType)
fml_TextInput_Type: Property = Property(name="Type", type=StringType)
fml_TextInput_Content: Property = Property(name="Content", type=StringType)
fml_TextInput.attributes={fml_TextInput_Content, fml_TextInput_Label, fml_TextInput_Type}

# InputElement class attributes and methods

# fml_SelectField class attributes and methods
fml_SelectField_Label: Property = Property(name="Label", type=StringType)
fml_SelectField_Type: Property = Property(name="Type", type=StringType)
fml_SelectField.attributes={fml_SelectField_Type, fml_SelectField_Label}

# Relationships
contained5: BinaryAssociation = BinaryAssociation(
    name="contained5",
    ends={
        Property(name="Page", type=fml_PageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="consists", type=fml_Page, multiplicity=Multiplicity(0, 1))
    }
)
visibleIfSelected6: BinaryAssociation = BinaryAssociation(
    name="visibleIfSelected6",
    ends={
        Property(name="SelectionItem", type=fml_PageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="displayElementVisible", type=fml_SelectionItem, multiplicity=Multiplicity(0, 9999))
    }
)
organized0: BinaryAssociation = BinaryAssociation(
    name="organized0",
    ends={
        Property(name="fml_Page", type=fml_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="fml_Form", type=fml_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
predecessor2: BinaryAssociation = BinaryAssociation(
    name="predecessor2",
    ends={
        Property(name="fml_Page3", type=fml_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="fml_Page1", type=fml_Page, multiplicity=Multiplicity(0, 1))
    }
)
consists4: BinaryAssociation = BinaryAssociation(
    name="consists4",
    ends={
        Property(name="PageElement", type=fml_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="contained", type=fml_PageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contained11: BinaryAssociation = BinaryAssociation(
    name="contained11",
    ends={
        Property(name="SelectField", type=fml_SelectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="consists12", type=fml_SelectField, multiplicity=Multiplicity(0, 1))
    }
)
displayElementVisible13: BinaryAssociation = BinaryAssociation(
    name="displayElementVisible13",
    ends={
        Property(name="PageElement14", type=fml_SelectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="visibleIfSelected", type=fml_PageElement, multiplicity=Multiplicity(0, 9999))
    }
)
consists7: BinaryAssociation = BinaryAssociation(
    name="consists7",
    ends={
        Property(name="fml_ListItem", type=fml_List, multiplicity=Multiplicity(1, 1)),
        Property(name="fml_List", type=fml_ListItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
consists8: BinaryAssociation = BinaryAssociation(
    name="consists8",
    ends={
        Property(name="SelectionItem10", type=fml_SelectField, multiplicity=Multiplicity(1, 1)),
        Property(name="contained9", type=fml_SelectionItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_fml_DisplayElement_PageElement = Generalization(general=PageElement, specific=fml_DisplayElement)
gen_fml_Heading_DisplayElement = Generalization(general=DisplayElement, specific=fml_Heading)
gen_fml_TextParagraph_DisplayElement = Generalization(general=DisplayElement, specific=fml_TextParagraph)
gen_fml_List_DisplayElement = Generalization(general=DisplayElement, specific=fml_List)
gen_fml_InputElement_PageElement = Generalization(general=PageElement, specific=fml_InputElement)
gen_fml_TextInput_InputElement = Generalization(general=InputElement, specific=fml_TextInput)
gen_fml_SelectField_InputElement = Generalization(general=InputElement, specific=fml_SelectField)

# Domain Model
domain_model = DomainModel(
    name="fml",
    types={fml_SelectionItem, fml_DisplayElement, PageElement, fml_Heading, DisplayElement, fml_Form, fml_Page, fml_PageElement, fml_TextParagraph, fml_List, fml_ListItem, fml_InputElement, fml_TextInput, InputElement, fml_SelectField, TextInputType, SelectionType},
    associations={contained5, visibleIfSelected6, organized0, predecessor2, consists4, contained11, displayElementVisible13, consists7, consists8},
    generalizations={gen_fml_DisplayElement_PageElement, gen_fml_Heading_DisplayElement, gen_fml_TextParagraph_DisplayElement, gen_fml_List_DisplayElement, gen_fml_InputElement_PageElement, gen_fml_TextInput_InputElement, gen_fml_SelectField_InputElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)