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
Alignment: Enumeration = Enumeration(
    name="Alignment",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right")
    }
)

# Classes
webshop_builder_3k_model_Page = Class(name="webshop::builder::3k::model::Page")
webshop_builder_3k_model_Component = Class(name="webshop::builder::3k::model::Component", is_abstract=True)
webshop_builder_3k_model_Knowledge_base = Class(name="webshop::builder::3k::model::Knowledge::base")
webshop_builder_3k_model_Reuse_component = Class(name="webshop::builder::3k::model::Reuse::component")
webshop_builder_3k_model_Style = Class(name="webshop::builder::3k::model::Style")
webshop_builder_3k_model_Reuses_component_link = Class(name="webshop::builder::3k::model::Reuses::component::link")
webshop_builder_3k_model_Picture = Class(name="webshop::builder::3k::model::Picture")
Component = Class(name="Component")
webshop_builder_3k_model_Text_field = Class(name="webshop::builder::3k::model::Text::field")
webshop_builder_3k_model_User_input_field = Class(name="webshop::builder::3k::model::User::input::field")
webshop_builder_3k_model_Item_to_KB_link = Class(name="webshop::builder::3k::model::Item::to::KB::link")
webshop_builder_3k_model_Item = Class(name="webshop::builder::3k::model::Item")
webshop_builder_3k_model_Checkbox = Class(name="webshop::builder::3k::model::Checkbox")
User_input_field = Class(name="User::input::field")
webshop_builder_3k_model_Branding = Class(name="webshop::builder::3k::model::Branding")
webshop_builder_3k_model_Radio_button = Class(name="webshop::builder::3k::model::Radio::button")
webshop_builder_3k_model_Text_input_field = Class(name="webshop::builder::3k::model::Text::input::field")
webshop_builder_3k_model_Webshop_builder_3k = Class(name="webshop::builder::3k::model::Webshop::builder::3k")
webshop_builder_3k_model_Login_widget = Class(name="webshop::builder::3k::model::Login::widget")
webshop_builder_3k_model_Slideshow = Class(name="webshop::builder::3k::model::Slideshow")
webshop_builder_3k_model_Social_button = Class(name="webshop::builder::3k::model::Social::button")
webshop_builder_3k_model_Newsletter_subscription_widget = Class(name="webshop::builder::3k::model::Newsletter::subscription::widget")
webshop_builder_3k_model_Shopping_cart_button = Class(name="webshop::builder::3k::model::Shopping::cart::button")
webshop_builder_3k_model_Search_widget = Class(name="webshop::builder::3k::model::Search::widget")
webshop_builder_3k_model_Menu = Class(name="webshop::builder::3k::model::Menu")
webshop_builder_3k_model_Component_group = Class(name="webshop::builder::3k::model::Component::group")
webshop_builder_3k_model_Result_list = Class(name="webshop::builder::3k::model::Result::list")
webshop_builder_3k_model_Source_code = Class(name="webshop::builder::3k::model::Source::code")
webshop_builder_3k_model_Navigation_button = Class(name="webshop::builder::3k::model::Navigation::button")
webshop_builder_3k_model_Navigation_to_Page_link = Class(name="webshop::builder::3k::model::Navigation::to::Page::link")
webshop_builder_3k_model_Border = Class(name="webshop::builder::3k::model::Border")

# webshop_builder_3k_model_Page class attributes and methods
webshop_builder_3k_model_Page_width: Property = Property(name="width", type=IntegerType)
webshop_builder_3k_model_Page_title: Property = Property(name="title", type=StringType)
webshop_builder_3k_model_Page_height: Property = Property(name="height", type=IntegerType)
webshop_builder_3k_model_Page_canvas_color: Property = Property(name="canvas_color", type=StringType)
webshop_builder_3k_model_Page.attributes={webshop_builder_3k_model_Page_height, webshop_builder_3k_model_Page_width, webshop_builder_3k_model_Page_title, webshop_builder_3k_model_Page_canvas_color}

# webshop_builder_3k_model_Component class attributes and methods
webshop_builder_3k_model_Component_xposition: Property = Property(name="xposition", type=IntegerType)
webshop_builder_3k_model_Component_yposition: Property = Property(name="yposition", type=IntegerType)
webshop_builder_3k_model_Component_width: Property = Property(name="width", type=IntegerType)
webshop_builder_3k_model_Component_height: Property = Property(name="height", type=IntegerType)
webshop_builder_3k_model_Component_name: Property = Property(name="name", type=StringType)
webshop_builder_3k_model_Component_alignment: Property = Property(name="alignment", type=StringType)
webshop_builder_3k_model_Component.attributes={webshop_builder_3k_model_Component_alignment, webshop_builder_3k_model_Component_height, webshop_builder_3k_model_Component_name, webshop_builder_3k_model_Component_width, webshop_builder_3k_model_Component_yposition, webshop_builder_3k_model_Component_xposition}

# webshop_builder_3k_model_Knowledge_base class attributes and methods
webshop_builder_3k_model_Knowledge_base_xml_file_uri: Property = Property(name="xml_file_uri", type=StringType)
webshop_builder_3k_model_Knowledge_base.attributes={webshop_builder_3k_model_Knowledge_base_xml_file_uri}

# webshop_builder_3k_model_Reuse_component class attributes and methods
webshop_builder_3k_model_Reuse_component_xposition: Property = Property(name="xposition", type=IntegerType)
webshop_builder_3k_model_Reuse_component_yposition: Property = Property(name="yposition", type=IntegerType)
webshop_builder_3k_model_Reuse_component.attributes={webshop_builder_3k_model_Reuse_component_yposition, webshop_builder_3k_model_Reuse_component_xposition}

# webshop_builder_3k_model_Style class attributes and methods
webshop_builder_3k_model_Style_background_color: Property = Property(name="background_color", type=StringType)
webshop_builder_3k_model_Style.attributes={webshop_builder_3k_model_Style_background_color}

# webshop_builder_3k_model_Reuses_component_link class attributes and methods

# webshop_builder_3k_model_Picture class attributes and methods
webshop_builder_3k_model_Picture_source: Property = Property(name="source", type=StringType)
webshop_builder_3k_model_Picture_title: Property = Property(name="title", type=StringType)
webshop_builder_3k_model_Picture_alternative_text: Property = Property(name="alternative_text", type=StringType)
webshop_builder_3k_model_Picture.attributes={webshop_builder_3k_model_Picture_alternative_text, webshop_builder_3k_model_Picture_source, webshop_builder_3k_model_Picture_title}

# Component class attributes and methods

# webshop_builder_3k_model_Text_field class attributes and methods
webshop_builder_3k_model_Text_field_header_level: Property = Property(name="header_level", type=IntegerType)
webshop_builder_3k_model_Text_field_text: Property = Property(name="text", type=StringType)
webshop_builder_3k_model_Text_field.attributes={webshop_builder_3k_model_Text_field_text, webshop_builder_3k_model_Text_field_header_level}

# webshop_builder_3k_model_User_input_field class attributes and methods
webshop_builder_3k_model_User_input_field_label: Property = Property(name="label", type=StringType)
webshop_builder_3k_model_User_input_field.attributes={webshop_builder_3k_model_User_input_field_label}

# webshop_builder_3k_model_Item_to_KB_link class attributes and methods

# webshop_builder_3k_model_Item class attributes and methods

# webshop_builder_3k_model_Checkbox class attributes and methods

# User_input_field class attributes and methods

# webshop_builder_3k_model_Branding class attributes and methods

# webshop_builder_3k_model_Radio_button class attributes and methods

# webshop_builder_3k_model_Text_input_field class attributes and methods

# webshop_builder_3k_model_Webshop_builder_3k class attributes and methods
webshop_builder_3k_model_Webshop_builder_3k_company_name: Property = Property(name="company_name", type=StringType)
webshop_builder_3k_model_Webshop_builder_3k.attributes={webshop_builder_3k_model_Webshop_builder_3k_company_name}

# webshop_builder_3k_model_Login_widget class attributes and methods

# webshop_builder_3k_model_Slideshow class attributes and methods

# webshop_builder_3k_model_Social_button class attributes and methods

# webshop_builder_3k_model_Newsletter_subscription_widget class attributes and methods

# webshop_builder_3k_model_Shopping_cart_button class attributes and methods

# webshop_builder_3k_model_Search_widget class attributes and methods

# webshop_builder_3k_model_Menu class attributes and methods

# webshop_builder_3k_model_Component_group class attributes and methods

# webshop_builder_3k_model_Result_list class attributes and methods
webshop_builder_3k_model_Result_list_number_of_items_per_page: Property = Property(name="number_of_items_per_page", type=IntegerType)
webshop_builder_3k_model_Result_list_distance_between_items: Property = Property(name="distance_between_items", type=IntegerType)
webshop_builder_3k_model_Result_list.attributes={webshop_builder_3k_model_Result_list_distance_between_items, webshop_builder_3k_model_Result_list_number_of_items_per_page}

# webshop_builder_3k_model_Source_code class attributes and methods

# webshop_builder_3k_model_Navigation_button class attributes and methods

# webshop_builder_3k_model_Navigation_to_Page_link class attributes and methods

# webshop_builder_3k_model_Border class attributes and methods
webshop_builder_3k_model_Border_thickness: Property = Property(name="thickness", type=IntegerType)
webshop_builder_3k_model_Border_color: Property = Property(name="color", type=StringType)
webshop_builder_3k_model_Border.attributes={webshop_builder_3k_model_Border_color, webshop_builder_3k_model_Border_thickness}

# Relationships
components0: BinaryAssociation = BinaryAssociation(
    name="components0",
    ends={
        Property(name="webshop_builder_3k_model_Page", type=webshop_builder_3k_model_Component, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="webshop_builder_3k_model_Component", type=webshop_builder_3k_model_Page, multiplicity=Multiplicity(1, 1))
    }
)
reuse_components1: BinaryAssociation = BinaryAssociation(
    name="reuse_components1",
    ends={
        Property(name="webshop_builder_3k_model_Reuse_component", type=webshop_builder_3k_model_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Page2", type=webshop_builder_3k_model_Reuse_component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style3: BinaryAssociation = BinaryAssociation(
    name="style3",
    ends={
        Property(name="webshop_builder_3k_model_Style", type=webshop_builder_3k_model_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Page4", type=webshop_builder_3k_model_Style, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
link5: BinaryAssociation = BinaryAssociation(
    name="link5",
    ends={
        Property(name="Reuses_component_link", type=webshop_builder_3k_model_Reuse_component, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=webshop_builder_3k_model_Reuses_component_link, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
style6: BinaryAssociation = BinaryAssociation(
    name="style6",
    ends={
        Property(name="webshop_builder_3k_model_Style8", type=webshop_builder_3k_model_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Component7", type=webshop_builder_3k_model_Style, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item9: BinaryAssociation = BinaryAssociation(
    name="item9",
    ends={
        Property(name="Item", type=webshop_builder_3k_model_Item_to_KB_link, multiplicity=Multiplicity(1, 1)),
        Property(name="kb_link", type=webshop_builder_3k_model_Item, multiplicity=Multiplicity(1, 1))
    }
)
knowledge_base10: BinaryAssociation = BinaryAssociation(
    name="knowledge_base10",
    ends={
        Property(name="webshop_builder_3k_model_Knowledge_base", type=webshop_builder_3k_model_Item_to_KB_link, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Item_to_KB_link", type=webshop_builder_3k_model_Knowledge_base, multiplicity=Multiplicity(1, 1))
    }
)
company_name11: BinaryAssociation = BinaryAssociation(
    name="company_name11",
    ends={
        Property(name="webshop_builder_3k_model_Text_field", type=webshop_builder_3k_model_Branding, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Branding", type=webshop_builder_3k_model_Text_field, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
company_logo12: BinaryAssociation = BinaryAssociation(
    name="company_logo12",
    ends={
        Property(name="webshop_builder_3k_model_Picture", type=webshop_builder_3k_model_Branding, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Branding13", type=webshop_builder_3k_model_Picture, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="Reuse_component", type=webshop_builder_3k_model_Reuses_component_link, multiplicity=Multiplicity(1, 1)),
        Property(name="link", type=webshop_builder_3k_model_Reuse_component, multiplicity=Multiplicity(1, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="webshop_builder_3k_model_Component16", type=webshop_builder_3k_model_Reuses_component_link, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Reuses_component_link", type=webshop_builder_3k_model_Component, multiplicity=Multiplicity(1, 1))
    }
)
pages17: BinaryAssociation = BinaryAssociation(
    name="pages17",
    ends={
        Property(name="webshop_builder_3k_model_Page18", type=webshop_builder_3k_model_Webshop_builder_3k, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Webshop_builder_3k", type=webshop_builder_3k_model_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
free_components19: BinaryAssociation = BinaryAssociation(
    name="free_components19",
    ends={
        Property(name="webshop_builder_3k_model_Component21", type=webshop_builder_3k_model_Webshop_builder_3k, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Webshop_builder_3k20", type=webshop_builder_3k_model_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledge_bases22: BinaryAssociation = BinaryAssociation(
    name="knowledge_bases22",
    ends={
        Property(name="webshop_builder_3k_model_Knowledge_base24", type=webshop_builder_3k_model_Webshop_builder_3k, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Webshop_builder_3k23", type=webshop_builder_3k_model_Knowledge_base, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
index_page25: BinaryAssociation = BinaryAssociation(
    name="index_page25",
    ends={
        Property(name="webshop_builder_3k_model_Page27", type=webshop_builder_3k_model_Webshop_builder_3k, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Webshop_builder_3k26", type=webshop_builder_3k_model_Page, multiplicity=Multiplicity(1, 1))
    }
)
item_details_page28: BinaryAssociation = BinaryAssociation(
    name="item_details_page28",
    ends={
        Property(name="webshop_builder_3k_model_Page30", type=webshop_builder_3k_model_Webshop_builder_3k, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Webshop_builder_3k29", type=webshop_builder_3k_model_Page, multiplicity=Multiplicity(0, 1))
    }
)
item_picture31: BinaryAssociation = BinaryAssociation(
    name="item_picture31",
    ends={
        Property(name="webshop_builder_3k_model_Picture32", type=webshop_builder_3k_model_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Item", type=webshop_builder_3k_model_Picture, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
text_fields33: BinaryAssociation = BinaryAssociation(
    name="text_fields33",
    ends={
        Property(name="webshop_builder_3k_model_Text_field35", type=webshop_builder_3k_model_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Item34", type=webshop_builder_3k_model_Text_field, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
kb_link36: BinaryAssociation = BinaryAssociation(
    name="kb_link36",
    ends={
        Property(name="Item_to_KB_link", type=webshop_builder_3k_model_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="item", type=webshop_builder_3k_model_Item_to_KB_link, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result_template37: BinaryAssociation = BinaryAssociation(
    name="result_template37",
    ends={
        Property(name="webshop_builder_3k_model_Item38", type=webshop_builder_3k_model_Result_list, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Result_list", type=webshop_builder_3k_model_Item, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
link39: BinaryAssociation = BinaryAssociation(
    name="link39",
    ends={
        Property(name="Navigation_to_Page_link", type=webshop_builder_3k_model_Navigation_button, multiplicity=Multiplicity(1, 1)),
        Property(name="Source", type=webshop_builder_3k_model_Navigation_to_Page_link, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
picture40: BinaryAssociation = BinaryAssociation(
    name="picture40",
    ends={
        Property(name="webshop_builder_3k_model_Picture41", type=webshop_builder_3k_model_Navigation_button, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Navigation_button", type=webshop_builder_3k_model_Picture, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
text42: BinaryAssociation = BinaryAssociation(
    name="text42",
    ends={
        Property(name="webshop_builder_3k_model_Text_field44", type=webshop_builder_3k_model_Navigation_button, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Navigation_button43", type=webshop_builder_3k_model_Text_field, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Source45: BinaryAssociation = BinaryAssociation(
    name="Source45",
    ends={
        Property(name="Navigation_button", type=webshop_builder_3k_model_Navigation_to_Page_link, multiplicity=Multiplicity(1, 1)),
        Property(name="link46", type=webshop_builder_3k_model_Navigation_button, multiplicity=Multiplicity(1, 1))
    }
)
target47: BinaryAssociation = BinaryAssociation(
    name="target47",
    ends={
        Property(name="webshop_builder_3k_model_Page48", type=webshop_builder_3k_model_Navigation_to_Page_link, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Navigation_to_Page_link", type=webshop_builder_3k_model_Page, multiplicity=Multiplicity(1, 1))
    }
)
border49: BinaryAssociation = BinaryAssociation(
    name="border49",
    ends={
        Property(name="webshop_builder_3k_model_Border", type=webshop_builder_3k_model_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="webshop_builder_3k_model_Style50", type=webshop_builder_3k_model_Border, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_webshop_builder_3k_model_Picture_Component = Generalization(general=Component, specific=webshop_builder_3k_model_Picture)
gen_webshop_builder_3k_model_Text_field_Component = Generalization(general=Component, specific=webshop_builder_3k_model_Text_field)
gen_webshop_builder_3k_model_Checkbox_User_input_field = Generalization(general=User_input_field, specific=webshop_builder_3k_model_Checkbox)
gen_webshop_builder_3k_model_Branding_Component = Generalization(general=Component, specific=webshop_builder_3k_model_Branding)
gen_webshop_builder_3k_model_Radio_button_User_input_field = Generalization(general=User_input_field, specific=webshop_builder_3k_model_Radio_button)
gen_webshop_builder_3k_model_Text_input_field_User_input_field = Generalization(general=User_input_field, specific=webshop_builder_3k_model_Text_input_field)
gen_webshop_builder_3k_model_Item_Component = Generalization(general=Component, specific=webshop_builder_3k_model_Item)
gen_webshop_builder_3k_model_Result_list_Component = Generalization(general=Component, specific=webshop_builder_3k_model_Result_list)
gen_webshop_builder_3k_model_Navigation_button_Component = Generalization(general=Component, specific=webshop_builder_3k_model_Navigation_button)

# Domain Model
domain_model = DomainModel(
    name="webshop_builder_3k_model",
    types={webshop_builder_3k_model_Page, webshop_builder_3k_model_Component, webshop_builder_3k_model_Knowledge_base, webshop_builder_3k_model_Reuse_component, webshop_builder_3k_model_Style, webshop_builder_3k_model_Reuses_component_link, webshop_builder_3k_model_Picture, Component, webshop_builder_3k_model_Text_field, webshop_builder_3k_model_User_input_field, webshop_builder_3k_model_Item_to_KB_link, webshop_builder_3k_model_Item, webshop_builder_3k_model_Checkbox, User_input_field, webshop_builder_3k_model_Branding, webshop_builder_3k_model_Radio_button, webshop_builder_3k_model_Text_input_field, webshop_builder_3k_model_Webshop_builder_3k, webshop_builder_3k_model_Login_widget, webshop_builder_3k_model_Slideshow, webshop_builder_3k_model_Social_button, webshop_builder_3k_model_Newsletter_subscription_widget, webshop_builder_3k_model_Shopping_cart_button, webshop_builder_3k_model_Search_widget, webshop_builder_3k_model_Menu, webshop_builder_3k_model_Component_group, webshop_builder_3k_model_Result_list, webshop_builder_3k_model_Source_code, webshop_builder_3k_model_Navigation_button, webshop_builder_3k_model_Navigation_to_Page_link, webshop_builder_3k_model_Border, Alignment},
    associations={components0, reuse_components1, style3, link5, style6, item9, knowledge_base10, company_name11, company_logo12, source14, target15, pages17, free_components19, knowledge_bases22, index_page25, item_details_page28, item_picture31, text_fields33, kb_link36, result_template37, link39, picture40, text42, Source45, target47, border49},
    generalizations={gen_webshop_builder_3k_model_Picture_Component, gen_webshop_builder_3k_model_Text_field_Component, gen_webshop_builder_3k_model_Checkbox_User_input_field, gen_webshop_builder_3k_model_Branding_Component, gen_webshop_builder_3k_model_Radio_button_User_input_field, gen_webshop_builder_3k_model_Text_input_field_User_input_field, gen_webshop_builder_3k_model_Item_Component, gen_webshop_builder_3k_model_Result_list_Component, gen_webshop_builder_3k_model_Navigation_button_Component},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)