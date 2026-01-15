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
DateFormat: Enumeration = Enumeration(
    name="DateFormat",
    literals={
            EnumerationLiteral(name="DayMonthYear"),
			EnumerationLiteral(name="YearMonthDay")
    }
)

# Classes
webapp_Page = Class(name="webapp::Page", is_abstract=True)
webapp_FormPage = Class(name="webapp::FormPage")
Page = Class(name="Page")
webapp_Control = Class(name="webapp::Control", is_abstract=True)
webapp_NormalPage = Class(name="webapp::NormalPage")
webapp_TextBox = Class(name="webapp::TextBox")
webapp_DropDownList = Class(name="webapp::DropDownList")
webapp_ListElement = Class(name="webapp::ListElement")
webapp_RadioButton = Class(name="webapp::RadioButton")
webapp_NormalControl = Class(name="webapp::NormalControl", is_abstract=True)
webapp_Label = Class(name="webapp::Label")
Control = Class(name="Control")
NormalControl = Class(name="NormalControl")
webapp_Link = Class(name="webapp::Link")
webapp_FormButton = Class(name="webapp::FormButton", is_abstract=True)
webapp_ResetButton = Class(name="webapp::ResetButton")
FormButton = Class(name="FormButton")
webapp_NormalButton = Class(name="webapp::NormalButton")
webapp_PasswordBox = Class(name="webapp::PasswordBox")
TextBox = Class(name="TextBox")
webapp_EmailBox = Class(name="webapp::EmailBox")
webapp_DateBox = Class(name="webapp::DateBox")
webapp_SubmitButton = Class(name="webapp::SubmitButton")
webapp_CheckBox = Class(name="webapp::CheckBox")
webapp_DynamicWebApp = Class(name="webapp::DynamicWebApp")

# webapp_Page class attributes and methods
webapp_Page_name: Property = Property(name="name", type=StringType)
webapp_Page_title: Property = Property(name="title", type=StringType)
webapp_Page_default: Property = Property(name="default", type=BooleanType)
webapp_Page.attributes={webapp_Page_name, webapp_Page_title, webapp_Page_default}

# webapp_FormPage class attributes and methods
webapp_FormPage_persist: Property = Property(name="persist", type=BooleanType)
webapp_FormPage.attributes={webapp_FormPage_persist}

# Page class attributes and methods

# webapp_Control class attributes and methods
webapp_Control_id: Property = Property(name="id", type=StringType)
webapp_Control_name: Property = Property(name="name", type=StringType)
webapp_Control.attributes={webapp_Control_id, webapp_Control_name}

# webapp_NormalPage class attributes and methods

# webapp_TextBox class attributes and methods
webapp_TextBox_text: Property = Property(name="text", type=StringType)
webapp_TextBox_maxLength: Property = Property(name="maxLength", type=IntegerType)
webapp_TextBox_size: Property = Property(name="size", type=IntegerType)
webapp_TextBox_required: Property = Property(name="required", type=BooleanType)
webapp_TextBox.attributes={webapp_TextBox_size, webapp_TextBox_maxLength, webapp_TextBox_text, webapp_TextBox_required}

# webapp_DropDownList class attributes and methods

# webapp_ListElement class attributes and methods
webapp_ListElement_value: Property = Property(name="value", type=StringType)
webapp_ListElement.attributes={webapp_ListElement_value}

# webapp_RadioButton class attributes and methods

# webapp_NormalControl class attributes and methods
webapp_NormalControl_text: Property = Property(name="text", type=StringType)
webapp_NormalControl.attributes={webapp_NormalControl_text}

# webapp_Label class attributes and methods

# Control class attributes and methods

# NormalControl class attributes and methods

# webapp_Link class attributes and methods

# webapp_FormButton class attributes and methods
webapp_FormButton_text: Property = Property(name="text", type=StringType)
webapp_FormButton.attributes={webapp_FormButton_text}

# webapp_ResetButton class attributes and methods

# FormButton class attributes and methods

# webapp_NormalButton class attributes and methods

# webapp_PasswordBox class attributes and methods

# TextBox class attributes and methods

# webapp_EmailBox class attributes and methods

# webapp_DateBox class attributes and methods
webapp_DateBox_format: Property = Property(name="format", type=StringType)
webapp_DateBox.attributes={webapp_DateBox_format}

# webapp_SubmitButton class attributes and methods

# webapp_CheckBox class attributes and methods
webapp_CheckBox_text: Property = Property(name="text", type=StringType)
webapp_CheckBox.attributes={webapp_CheckBox_text}

# webapp_DynamicWebApp class attributes and methods
webapp_DynamicWebApp_name: Property = Property(name="name", type=StringType)
webapp_DynamicWebApp.attributes={webapp_DynamicWebApp_name}

# Relationships
successTarget0: BinaryAssociation = BinaryAssociation(
    name="successTarget0",
    ends={
        Property(name="webapp_Page", type=webapp_FormPage, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_FormPage", type=webapp_Page, multiplicity=Multiplicity(0, 1))
    }
)
errorTarget1: BinaryAssociation = BinaryAssociation(
    name="errorTarget1",
    ends={
        Property(name="webapp_Page3", type=webapp_FormPage, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_FormPage2", type=webapp_Page, multiplicity=Multiplicity(0, 1))
    }
)
controls4: BinaryAssociation = BinaryAssociation(
    name="controls4",
    ends={
        Property(name="webapp_Control", type=webapp_FormPage, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_FormPage5", type=webapp_Control, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
destination7: BinaryAssociation = BinaryAssociation(
    name="destination7",
    ends={
        Property(name="webapp_Page8", type=webapp_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Link", type=webapp_Page, multiplicity=Multiplicity(1, 1))
    }
)
elements9: BinaryAssociation = BinaryAssociation(
    name="elements9",
    ends={
        Property(name="webapp_ListElement", type=webapp_DropDownList, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_DropDownList", type=webapp_ListElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements10: BinaryAssociation = BinaryAssociation(
    name="elements10",
    ends={
        Property(name="webapp_ListElement11", type=webapp_RadioButton, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_RadioButton", type=webapp_ListElement, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
controls6: BinaryAssociation = BinaryAssociation(
    name="controls6",
    ends={
        Property(name="webapp_NormalControl", type=webapp_NormalPage, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_NormalPage", type=webapp_NormalControl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pages12: BinaryAssociation = BinaryAssociation(
    name="pages12",
    ends={
        Property(name="webapp_Page13", type=webapp_DynamicWebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_DynamicWebApp", type=webapp_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_webapp_FormPage_Page = Generalization(general=Page, specific=webapp_FormPage)
gen_webapp_NormalPage_Page = Generalization(general=Page, specific=webapp_NormalPage)
gen_webapp_TextBox_Control = Generalization(general=Control, specific=webapp_TextBox)
gen_webapp_DropDownList_Control = Generalization(general=Control, specific=webapp_DropDownList)
gen_webapp_RadioButton_Control = Generalization(general=Control, specific=webapp_RadioButton)
gen_webapp_Label_Control = Generalization(general=Control, specific=webapp_Label)
gen_webapp_Label_NormalControl = Generalization(general=NormalControl, specific=webapp_Label)
gen_webapp_Link_Control = Generalization(general=Control, specific=webapp_Link)
gen_webapp_Link_NormalControl = Generalization(general=NormalControl, specific=webapp_Link)
gen_webapp_FormButton_Control = Generalization(general=Control, specific=webapp_FormButton)
gen_webapp_ResetButton_FormButton = Generalization(general=FormButton, specific=webapp_ResetButton)
gen_webapp_NormalButton_NormalControl = Generalization(general=NormalControl, specific=webapp_NormalButton)
gen_webapp_PasswordBox_TextBox = Generalization(general=TextBox, specific=webapp_PasswordBox)
gen_webapp_EmailBox_TextBox = Generalization(general=TextBox, specific=webapp_EmailBox)
gen_webapp_DateBox_TextBox = Generalization(general=TextBox, specific=webapp_DateBox)
gen_webapp_SubmitButton_FormButton = Generalization(general=FormButton, specific=webapp_SubmitButton)
gen_webapp_CheckBox_Control = Generalization(general=Control, specific=webapp_CheckBox)
gen_webapp_NormalControl_Control = Generalization(general=Control, specific=webapp_NormalControl)

# Domain Model
domain_model = DomainModel(
    name="webapp",
    types={webapp_Page, webapp_FormPage, Page, webapp_Control, webapp_NormalPage, webapp_TextBox, webapp_DropDownList, webapp_ListElement, webapp_RadioButton, webapp_NormalControl, webapp_Label, Control, NormalControl, webapp_Link, webapp_FormButton, webapp_ResetButton, FormButton, webapp_NormalButton, webapp_PasswordBox, TextBox, webapp_EmailBox, webapp_DateBox, webapp_SubmitButton, webapp_CheckBox, webapp_DynamicWebApp, DateFormat},
    associations={successTarget0, errorTarget1, controls4, destination7, elements9, elements10, controls6, pages12},
    generalizations={gen_webapp_FormPage_Page, gen_webapp_NormalPage_Page, gen_webapp_TextBox_Control, gen_webapp_DropDownList_Control, gen_webapp_RadioButton_Control, gen_webapp_Label_Control, gen_webapp_Label_NormalControl, gen_webapp_Link_Control, gen_webapp_Link_NormalControl, gen_webapp_FormButton_Control, gen_webapp_ResetButton_FormButton, gen_webapp_NormalButton_NormalControl, gen_webapp_PasswordBox_TextBox, gen_webapp_EmailBox_TextBox, gen_webapp_DateBox_TextBox, gen_webapp_SubmitButton_FormButton, gen_webapp_CheckBox_Control, gen_webapp_NormalControl_Control},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)