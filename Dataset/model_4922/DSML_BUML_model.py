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
Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="int"),
			EnumerationLiteral(name="float")
    }
)

# Classes
dsml_web_Website = Class(name="dsml::web::Website")
Page = Class(name="Page")
dsml_web_Page = Class(name="dsml::web::Page")
Form = Class(name="Form")
Text = Class(name="Text")
Link = Class(name="Link")
dsml_web_Field = Class(name="dsml::web::Field", is_abstract=True)
FormElement = Class(name="FormElement")
Validator = Class(name="Validator")
dsml_web_TextField = Class(name="dsml::web::TextField")
Field = Class(name="Field")
dsml_web_PasswordField = Class(name="dsml::web::PasswordField")
dsml_web_Select = Class(name="dsml::web::Select")
dsml_web_ListField = Class(name="dsml::web::ListField", is_abstract=True)
Item = Class(name="Item")
dsml_web_TextArea = Class(name="dsml::web::TextArea")
dsml_web_ResetButton = Class(name="dsml::web::ResetButton")
dsml_web_Link = Class(name="dsml::web::Link")
dsml_web_FormElement = Class(name="dsml::web::FormElement", is_abstract=True)
dsml_web_Hidden = Class(name="dsml::web::Hidden")
dsml_web_Form = Class(name="dsml::web::Form")
dsml_web_Label = Class(name="dsml::web::Label")
dsml_web_Button = Class(name="dsml::web::Button", is_abstract=True)
dsml_web_RadioButton = Class(name="dsml::web::RadioButton")
ListField = Class(name="ListField")
dsml_web_CheckBox = Class(name="dsml::web::CheckBox")
dsml_web_SubmitButton = Class(name="dsml::web::SubmitButton")
Button = Class(name="Button")
dsml_web_CancelButton = Class(name="dsml::web::CancelButton")
dsml_web_Item = Class(name="dsml::web::Item")
dsml_web_DateValidator = Class(name="dsml::web::DateValidator")
dsml_web_EmailValidator = Class(name="dsml::web::EmailValidator")
dsml_web_Required = Class(name="dsml::web::Required")
dsml_web_TimeValidator = Class(name="dsml::web::TimeValidator")
dsml_web_URLValidator = Class(name="dsml::web::URLValidator")
dsml_web_TypeValidator = Class(name="dsml::web::TypeValidator")
dsml_web_GreaterThanValidator = Class(name="dsml::web::GreaterThanValidator")
dsml_web_LessThanValidator = Class(name="dsml::web::LessThanValidator")
dsml_web_BetweenValidator = Class(name="dsml::web::BetweenValidator")
dsml_web_RegexValidator = Class(name="dsml::web::RegexValidator")
dsml_web_StringLengthValidator = Class(name="dsml::web::StringLengthValidator")
dsml_web_Success = Class(name="dsml::web::Success")
dsml_web_Error = Class(name="dsml::web::Error")
Success = Class(name="Success")
Error = Class(name="Error")
dsml_web_Text = Class(name="dsml::web::Text")
dsml_web_Validator = Class(name="dsml::web::Validator", is_abstract=True)
dsml_visitor_JSPVisitor = Class(name="dsml::visitor::JSPVisitor")
Visitor = Class(name="Visitor")
dsml_visitor_Visitor = Class(name="dsml::visitor::Visitor", is_abstract=True)
dsml_visitor_ResourceVisitor = Class(name="dsml::visitor::ResourceVisitor")
dsml_visitor_POJOVisitor = Class(name="dsml::visitor::POJOVisitor")

# dsml_web_Website class attributes and methods
dsml_web_Website_name: Property = Property(name="name", type=StringType)
dsml_web_Website.attributes={dsml_web_Website_name}

# Page class attributes and methods

# dsml_web_Page class attributes and methods
dsml_web_Page_title: Property = Property(name="title", type=StringType)
dsml_web_Page_name: Property = Property(name="name", type=StringType)
dsml_web_Page.attributes={dsml_web_Page_name, dsml_web_Page_title}

# Form class attributes and methods

# Text class attributes and methods

# Link class attributes and methods

# dsml_web_Field class attributes and methods

# FormElement class attributes and methods

# Validator class attributes and methods

# dsml_web_TextField class attributes and methods
dsml_web_TextField_size: Property = Property(name="size", type=IntegerType)
dsml_web_TextField_maxlength: Property = Property(name="maxlength", type=IntegerType)
dsml_web_TextField.attributes={dsml_web_TextField_maxlength, dsml_web_TextField_size}

# Field class attributes and methods

# dsml_web_PasswordField class attributes and methods
dsml_web_PasswordField_size: Property = Property(name="size", type=IntegerType)
dsml_web_PasswordField_maxlength: Property = Property(name="maxlength", type=IntegerType)
dsml_web_PasswordField.attributes={dsml_web_PasswordField_size, dsml_web_PasswordField_maxlength}

# dsml_web_Select class attributes and methods
dsml_web_Select_size: Property = Property(name="size", type=IntegerType)
dsml_web_Select.attributes={dsml_web_Select_size}

# dsml_web_ListField class attributes and methods

# Item class attributes and methods

# dsml_web_TextArea class attributes and methods
dsml_web_TextArea_cols: Property = Property(name="cols", type=IntegerType)
dsml_web_TextArea_rows: Property = Property(name="rows", type=IntegerType)
dsml_web_TextArea.attributes={dsml_web_TextArea_rows, dsml_web_TextArea_cols}

# dsml_web_ResetButton class attributes and methods

# dsml_web_Link class attributes and methods
dsml_web_Link_value: Property = Property(name="value", type=StringType)
dsml_web_Link_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')}, type=StringType)
dsml_web_Link.attributes={dsml_web_Link_value}
dsml_web_Link.methods={dsml_web_Link_m_accept}

# dsml_web_FormElement class attributes and methods
dsml_web_FormElement_name: Property = Property(name="name", type=StringType)
dsml_web_FormElement_value: Property = Property(name="value", type=StringType)
dsml_web_FormElement_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')}, type=StringType)
dsml_web_FormElement.attributes={dsml_web_FormElement_name, dsml_web_FormElement_value}
dsml_web_FormElement.methods={dsml_web_FormElement_m_accept}

# dsml_web_Hidden class attributes and methods

# dsml_web_Form class attributes and methods
dsml_web_Form_action: Property = Property(name="action", type=StringType)
dsml_web_Form_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')}, type=StringType)
dsml_web_Form.attributes={dsml_web_Form_action}
dsml_web_Form.methods={dsml_web_Form_m_accept}

# dsml_web_Label class attributes and methods

# dsml_web_Button class attributes and methods

# dsml_web_RadioButton class attributes and methods

# ListField class attributes and methods

# dsml_web_CheckBox class attributes and methods

# dsml_web_SubmitButton class attributes and methods

# Button class attributes and methods

# dsml_web_CancelButton class attributes and methods

# dsml_web_Item class attributes and methods
dsml_web_Item_value: Property = Property(name="value", type=StringType)
dsml_web_Item.attributes={dsml_web_Item_value}

# dsml_web_DateValidator class attributes and methods

# dsml_web_EmailValidator class attributes and methods

# dsml_web_Required class attributes and methods

# dsml_web_TimeValidator class attributes and methods

# dsml_web_URLValidator class attributes and methods

# dsml_web_TypeValidator class attributes and methods
dsml_web_TypeValidator_type: Property = Property(name="type", type=StringType)
dsml_web_TypeValidator.attributes={dsml_web_TypeValidator_type}

# dsml_web_GreaterThanValidator class attributes and methods
dsml_web_GreaterThanValidator_value: Property = Property(name="value", type=IntegerType)
dsml_web_GreaterThanValidator.attributes={dsml_web_GreaterThanValidator_value}

# dsml_web_LessThanValidator class attributes and methods
dsml_web_LessThanValidator_value: Property = Property(name="value", type=IntegerType)
dsml_web_LessThanValidator.attributes={dsml_web_LessThanValidator_value}

# dsml_web_BetweenValidator class attributes and methods
dsml_web_BetweenValidator_valueL: Property = Property(name="valueL", type=IntegerType)
dsml_web_BetweenValidator_valueG: Property = Property(name="valueG", type=IntegerType)
dsml_web_BetweenValidator.attributes={dsml_web_BetweenValidator_valueL, dsml_web_BetweenValidator_valueG}

# dsml_web_RegexValidator class attributes and methods
dsml_web_RegexValidator_regex: Property = Property(name="regex", type=StringType)
dsml_web_RegexValidator.attributes={dsml_web_RegexValidator_regex}

# dsml_web_StringLengthValidator class attributes and methods
dsml_web_StringLengthValidator_min: Property = Property(name="min", type=IntegerType)
dsml_web_StringLengthValidator_max: Property = Property(name="max", type=IntegerType)
dsml_web_StringLengthValidator.attributes={dsml_web_StringLengthValidator_min, dsml_web_StringLengthValidator_max}

# dsml_web_Success class attributes and methods

# dsml_web_Error class attributes and methods

# Success class attributes and methods

# Error class attributes and methods

# dsml_web_Text class attributes and methods
dsml_web_Text_value: Property = Property(name="value", type=StringType)
dsml_web_Text_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')}, type=StringType)
dsml_web_Text.attributes={dsml_web_Text_value}
dsml_web_Text.methods={dsml_web_Text_m_accept}

# dsml_web_Validator class attributes and methods
dsml_web_Validator_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')}, type=StringType)
dsml_web_Validator.methods={dsml_web_Validator_m_accept}

# dsml_visitor_JSPVisitor class attributes and methods

# Visitor class attributes and methods

# dsml_visitor_Visitor class attributes and methods
dsml_visitor_Visitor_tag: Property = Property(name="tag", type=StringType)
dsml_visitor_Visitor.attributes={dsml_visitor_Visitor_tag}

# dsml_visitor_ResourceVisitor class attributes and methods

# dsml_visitor_POJOVisitor class attributes and methods

# Relationships
Pages0: BinaryAssociation = BinaryAssociation(
    name="Pages0",
    ends={
        Property(name="Page", type=dsml_web_Website, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_web_Website", type=Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Form1: BinaryAssociation = BinaryAssociation(
    name="Form1",
    ends={
        Property(name="Form", type=dsml_web_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_web_Page", type=Form, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Texts2: BinaryAssociation = BinaryAssociation(
    name="Texts2",
    ends={
        Property(name="Text", type=dsml_web_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_web_Page3", type=Text, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Links4: BinaryAssociation = BinaryAssociation(
    name="Links4",
    ends={
        Property(name="Link", type=dsml_web_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_web_Page5", type=Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Validator6: BinaryAssociation = BinaryAssociation(
    name="Validator6",
    ends={
        Property(name="Validator", type=dsml_web_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_web_Field", type=Validator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Items7: BinaryAssociation = BinaryAssociation(
    name="Items7",
    ends={
        Property(name="Item", type=dsml_web_ListField, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_web_ListField", type=Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
LinkedPage8: BinaryAssociation = BinaryAssociation(
    name="LinkedPage8",
    ends={
        Property(name="Page9", type=dsml_web_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_web_Link", type=Page, multiplicity=Multiplicity(0, 1))
    }
)
FormElements10: BinaryAssociation = BinaryAssociation(
    name="FormElements10",
    ends={
        Property(name="FormElement", type=dsml_web_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_web_Form", type=FormElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
SuccessPage15: BinaryAssociation = BinaryAssociation(
    name="SuccessPage15",
    ends={
        Property(name="Page16", type=dsml_web_Success, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_web_Success", type=Page, multiplicity=Multiplicity(0, 1))
    }
)
ErrorPage17: BinaryAssociation = BinaryAssociation(
    name="ErrorPage17",
    ends={
        Property(name="Page18", type=dsml_web_Error, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_web_Error", type=Page, multiplicity=Multiplicity(0, 1))
    }
)
Success11: BinaryAssociation = BinaryAssociation(
    name="Success11",
    ends={
        Property(name="Success", type=dsml_web_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_web_Form12", type=Success, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Error13: BinaryAssociation = BinaryAssociation(
    name="Error13",
    ends={
        Property(name="Error", type=dsml_web_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="dsml_web_Form14", type=Error, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dsml_web_Field_FormElement = Generalization(general=FormElement, specific=dsml_web_Field)
gen_dsml_web_TextField_Field = Generalization(general=Field, specific=dsml_web_TextField)
gen_dsml_web_PasswordField_Field = Generalization(general=Field, specific=dsml_web_PasswordField)
gen_dsml_web_Select_ListField = Generalization(general=ListField, specific=dsml_web_Select)
gen_dsml_web_ListField_FormElement = Generalization(general=FormElement, specific=dsml_web_ListField)
gen_dsml_web_TextArea_Field = Generalization(general=Field, specific=dsml_web_TextArea)
gen_dsml_web_ResetButton_Button = Generalization(general=Button, specific=dsml_web_ResetButton)
gen_dsml_web_Hidden_FormElement = Generalization(general=FormElement, specific=dsml_web_Hidden)
gen_dsml_web_Label_FormElement = Generalization(general=FormElement, specific=dsml_web_Label)
gen_dsml_web_Button_FormElement = Generalization(general=FormElement, specific=dsml_web_Button)
gen_dsml_web_RadioButton_ListField = Generalization(general=ListField, specific=dsml_web_RadioButton)
gen_dsml_web_CheckBox_FormElement = Generalization(general=FormElement, specific=dsml_web_CheckBox)
gen_dsml_web_SubmitButton_Button = Generalization(general=Button, specific=dsml_web_SubmitButton)
gen_dsml_web_CancelButton_Button = Generalization(general=Button, specific=dsml_web_CancelButton)
gen_dsml_web_DateValidator_Validator = Generalization(general=Validator, specific=dsml_web_DateValidator)
gen_dsml_web_EmailValidator_Validator = Generalization(general=Validator, specific=dsml_web_EmailValidator)
gen_dsml_web_Required_Validator = Generalization(general=Validator, specific=dsml_web_Required)
gen_dsml_web_TimeValidator_Validator = Generalization(general=Validator, specific=dsml_web_TimeValidator)
gen_dsml_web_URLValidator_Validator = Generalization(general=Validator, specific=dsml_web_URLValidator)
gen_dsml_web_TypeValidator_Validator = Generalization(general=Validator, specific=dsml_web_TypeValidator)
gen_dsml_web_GreaterThanValidator_Validator = Generalization(general=Validator, specific=dsml_web_GreaterThanValidator)
gen_dsml_web_LessThanValidator_Validator = Generalization(general=Validator, specific=dsml_web_LessThanValidator)
gen_dsml_web_BetweenValidator_Validator = Generalization(general=Validator, specific=dsml_web_BetweenValidator)
gen_dsml_web_RegexValidator_Validator = Generalization(general=Validator, specific=dsml_web_RegexValidator)
gen_dsml_web_StringLengthValidator_Validator = Generalization(general=Validator, specific=dsml_web_StringLengthValidator)
gen_dsml_visitor_JSPVisitor_Visitor = Generalization(general=Visitor, specific=dsml_visitor_JSPVisitor)
gen_dsml_visitor_ResourceVisitor_Visitor = Generalization(general=Visitor, specific=dsml_visitor_ResourceVisitor)
gen_dsml_visitor_POJOVisitor_Visitor = Generalization(general=Visitor, specific=dsml_visitor_POJOVisitor)

# Domain Model
domain_model = DomainModel(
    name="dsml",
    types={dsml_web_Website, Page, dsml_web_Page, Form, Text, Link, dsml_web_Field, FormElement, Validator, dsml_web_TextField, Field, dsml_web_PasswordField, dsml_web_Select, dsml_web_ListField, Item, dsml_web_TextArea, dsml_web_ResetButton, dsml_web_Link, dsml_web_FormElement, dsml_web_Hidden, dsml_web_Form, dsml_web_Label, dsml_web_Button, dsml_web_RadioButton, ListField, dsml_web_CheckBox, dsml_web_SubmitButton, Button, dsml_web_CancelButton, dsml_web_Item, dsml_web_DateValidator, dsml_web_EmailValidator, dsml_web_Required, dsml_web_TimeValidator, dsml_web_URLValidator, dsml_web_TypeValidator, dsml_web_GreaterThanValidator, dsml_web_LessThanValidator, dsml_web_BetweenValidator, dsml_web_RegexValidator, dsml_web_StringLengthValidator, dsml_web_Success, dsml_web_Error, Success, Error, dsml_web_Text, dsml_web_Validator, dsml_visitor_JSPVisitor, Visitor, dsml_visitor_Visitor, dsml_visitor_ResourceVisitor, dsml_visitor_POJOVisitor, Type},
    associations={Pages0, Form1, Texts2, Links4, Validator6, Items7, LinkedPage8, FormElements10, SuccessPage15, ErrorPage17, Success11, Error13},
    generalizations={gen_dsml_web_Field_FormElement, gen_dsml_web_TextField_Field, gen_dsml_web_PasswordField_Field, gen_dsml_web_Select_ListField, gen_dsml_web_ListField_FormElement, gen_dsml_web_TextArea_Field, gen_dsml_web_ResetButton_Button, gen_dsml_web_Hidden_FormElement, gen_dsml_web_Label_FormElement, gen_dsml_web_Button_FormElement, gen_dsml_web_RadioButton_ListField, gen_dsml_web_CheckBox_FormElement, gen_dsml_web_SubmitButton_Button, gen_dsml_web_CancelButton_Button, gen_dsml_web_DateValidator_Validator, gen_dsml_web_EmailValidator_Validator, gen_dsml_web_Required_Validator, gen_dsml_web_TimeValidator_Validator, gen_dsml_web_URLValidator_Validator, gen_dsml_web_TypeValidator_Validator, gen_dsml_web_GreaterThanValidator_Validator, gen_dsml_web_LessThanValidator_Validator, gen_dsml_web_BetweenValidator_Validator, gen_dsml_web_RegexValidator_Validator, gen_dsml_web_StringLengthValidator_Validator, gen_dsml_visitor_JSPVisitor_Visitor, gen_dsml_visitor_ResourceVisitor_Visitor, gen_dsml_visitor_POJOVisitor_Visitor},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)