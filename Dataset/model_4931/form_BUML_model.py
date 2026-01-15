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
SelectionFieldType: Enumeration = Enumeration(
    name="SelectionFieldType",
    literals={
            EnumerationLiteral(name="Radio"),
			EnumerationLiteral(name="Checkbox"),
			EnumerationLiteral(name="Combobox")
    }
)

# Classes
form_PageElement = Class(name="form::PageElement", is_abstract=True)
form_VisibilityCondition = Class(name="form::VisibilityCondition", is_abstract=True)
form_InputField = Class(name="form::InputField", is_abstract=True)
PageElement = Class(name="PageElement")
form_Form = Class(name="form::Form")
form_Page = Class(name="form::Page")
form_Heading = Class(name="form::Heading")
Text = Class(name="Text")
form_Paragraph = Class(name="form::Paragraph")
form_List = Class(name="form::List")
form_ListItem = Class(name="form::ListItem")
form_SelectionCondition = Class(name="form::SelectionCondition")
VisibilityCondition = Class(name="VisibilityCondition")
form_TextField = Class(name="form::TextField")
InputField = Class(name="InputField")
form_SelectionField = Class(name="form::SelectionField")
form_SelectionItem = Class(name="form::SelectionItem")
form_TextArea = Class(name="form::TextArea")
form_Text = Class(name="form::Text", is_abstract=True)

# form_PageElement class attributes and methods
form_PageElement_elementId: Property = Property(name="elementId", type=StringType)
form_PageElement.attributes={form_PageElement_elementId}

# form_VisibilityCondition class attributes and methods

# form_InputField class attributes and methods
form_InputField_label: Property = Property(name="label", type=StringType)
form_InputField_mandatory: Property = Property(name="mandatory", type=BooleanType)
form_InputField.attributes={form_InputField_mandatory, form_InputField_label}

# PageElement class attributes and methods

# form_Form class attributes and methods

# form_Page class attributes and methods
form_Page_title: Property = Property(name="title", type=StringType)
form_Page.attributes={form_Page_title}

# form_Heading class attributes and methods
form_Heading_level: Property = Property(name="level", type=IntegerType)
form_Heading.attributes={form_Heading_level}

# Text class attributes and methods

# form_Paragraph class attributes and methods

# form_List class attributes and methods
form_List_ordered: Property = Property(name="ordered", type=BooleanType)
form_List.attributes={form_List_ordered}

# form_ListItem class attributes and methods
form_ListItem_label: Property = Property(name="label", type=StringType)
form_ListItem.attributes={form_ListItem_label}

# form_SelectionCondition class attributes and methods

# VisibilityCondition class attributes and methods

# form_TextField class attributes and methods
form_TextField_encrypted: Property = Property(name="encrypted", type=BooleanType)
form_TextField.attributes={form_TextField_encrypted}

# InputField class attributes and methods

# form_SelectionField class attributes and methods
form_SelectionField_selectionFieldType: Property = Property(name="selectionFieldType", type=StringType)
form_SelectionField.attributes={form_SelectionField_selectionFieldType}

# form_SelectionItem class attributes and methods
form_SelectionItem_label: Property = Property(name="label", type=StringType)
form_SelectionItem_selected: Property = Property(name="selected", type=BooleanType)
form_SelectionItem.attributes={form_SelectionItem_selected, form_SelectionItem_label}

# form_TextArea class attributes and methods

# form_Text class attributes and methods
form_Text_content: Property = Property(name="content", type=StringType)
form_Text.attributes={form_Text_content}

# Relationships
allPreviousPages5: BinaryAssociation = BinaryAssociation(
    name="allPreviousPages5",
    ends={
        Property(name="form_Page6", type=form_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Page4", type=form_Page, multiplicity=Multiplicity(0, 9999))
    }
)
allNextPages8: BinaryAssociation = BinaryAssociation(
    name="allNextPages8",
    ends={
        Property(name="form_Page9", type=form_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Page7", type=form_Page, multiplicity=Multiplicity(0, 9999))
    }
)
nextPage11: BinaryAssociation = BinaryAssociation(
    name="nextPage11",
    ends={
        Property(name="Page", type=form_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="previousPage", type=form_Page, multiplicity=Multiplicity(0, 1))
    }
)
elements12: BinaryAssociation = BinaryAssociation(
    name="elements12",
    ends={
        Property(name="PageElement", type=form_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page", type=form_PageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
previousPage14: BinaryAssociation = BinaryAssociation(
    name="previousPage14",
    ends={
        Property(name="Page15", type=form_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="nextPage", type=form_Page, multiplicity=Multiplicity(0, 1))
    }
)
visibilityConditions16: BinaryAssociation = BinaryAssociation(
    name="visibilityConditions16",
    ends={
        Property(name="VisibilityCondition", type=form_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page17", type=form_VisibilityCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page18: BinaryAssociation = BinaryAssociation(
    name="page18",
    ends={
        Property(name="Page19", type=form_PageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=form_Page, multiplicity=Multiplicity(1, 1))
    }
)
pages0: BinaryAssociation = BinaryAssociation(
    name="pages0",
    ends={
        Property(name="form_Page", type=form_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Form", type=form_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
welcomePage1: BinaryAssociation = BinaryAssociation(
    name="welcomePage1",
    ends={
        Property(name="form_Page3", type=form_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Form2", type=form_Page, multiplicity=Multiplicity(1, 1))
    }
)
items22: BinaryAssociation = BinaryAssociation(
    name="items22",
    ends={
        Property(name="form_ListItem", type=form_List, multiplicity=Multiplicity(1, 1)),
        Property(name="form_List", type=form_ListItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
page23: BinaryAssociation = BinaryAssociation(
    name="page23",
    ends={
        Property(name="Page24", type=form_VisibilityCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="visibilityConditions", type=form_Page, multiplicity=Multiplicity(1, 1))
    }
)
concernsElements25: BinaryAssociation = BinaryAssociation(
    name="concernsElements25",
    ends={
        Property(name="form_PageElement", type=form_VisibilityCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="form_VisibilityCondition", type=form_PageElement, multiplicity=Multiplicity(0, 9999))
    }
)
item26: BinaryAssociation = BinaryAssociation(
    name="item26",
    ends={
        Property(name="form_SelectionItem", type=form_SelectionCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="form_SelectionCondition", type=form_SelectionItem, multiplicity=Multiplicity(1, 1))
    }
)
items20: BinaryAssociation = BinaryAssociation(
    name="items20",
    ends={
        Property(name="SelectionItem", type=form_SelectionField, multiplicity=Multiplicity(1, 1)),
        Property(name="field", type=form_SelectionItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
field21: BinaryAssociation = BinaryAssociation(
    name="field21",
    ends={
        Property(name="SelectionField", type=form_SelectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="items", type=form_SelectionField, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_form_InputField_PageElement = Generalization(general=PageElement, specific=form_InputField)
gen_form_Heading_Text = Generalization(general=Text, specific=form_Heading)
gen_form_Paragraph_Text = Generalization(general=Text, specific=form_Paragraph)
gen_form_List_PageElement = Generalization(general=PageElement, specific=form_List)
gen_form_SelectionCondition_VisibilityCondition = Generalization(general=VisibilityCondition, specific=form_SelectionCondition)
gen_form_TextField_InputField = Generalization(general=InputField, specific=form_TextField)
gen_form_SelectionField_InputField = Generalization(general=InputField, specific=form_SelectionField)
gen_form_TextArea_InputField = Generalization(general=InputField, specific=form_TextArea)
gen_form_Text_PageElement = Generalization(general=PageElement, specific=form_Text)

# Domain Model
domain_model = DomainModel(
    name="form",
    types={form_PageElement, form_VisibilityCondition, form_InputField, PageElement, form_Form, form_Page, form_Heading, Text, form_Paragraph, form_List, form_ListItem, form_SelectionCondition, VisibilityCondition, form_TextField, InputField, form_SelectionField, form_SelectionItem, form_TextArea, form_Text, SelectionFieldType},
    associations={allPreviousPages5, allNextPages8, nextPage11, elements12, previousPage14, visibilityConditions16, page18, pages0, welcomePage1, items22, page23, concernsElements25, item26, items20, field21},
    generalizations={gen_form_InputField_PageElement, gen_form_Heading_Text, gen_form_Paragraph_Text, gen_form_List_PageElement, gen_form_SelectionCondition_VisibilityCondition, gen_form_TextField_InputField, gen_form_SelectionField_InputField, gen_form_TextArea_InputField, gen_form_Text_PageElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)