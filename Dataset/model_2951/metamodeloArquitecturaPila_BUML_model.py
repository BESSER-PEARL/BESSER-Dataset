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
metamodeloArquitecturaPila_ServiceType = Class(name="metamodeloArquitecturaPila::ServiceType")
metamodeloArquitecturaPila_BusinessLogic = Class(name="metamodeloArquitecturaPila::BusinessLogic")
metamodeloArquitecturaPila_Architecture = Class(name="metamodeloArquitecturaPila::Architecture")
metamodeloArquitecturaPila_View = Class(name="metamodeloArquitecturaPila::View")
metamodeloArquitecturaPila_BusinessModel = Class(name="metamodeloArquitecturaPila::BusinessModel")
metamodeloArquitecturaPila_Service = Class(name="metamodeloArquitecturaPila::Service")
metamodeloArquitecturaPila_SimpleComponent = Class(name="metamodeloArquitecturaPila::SimpleComponent", is_abstract=True)
metamodeloArquitecturaPila_TitleBar = Class(name="metamodeloArquitecturaPila::TitleBar")
metamodeloArquitecturaPila_Menu = Class(name="metamodeloArquitecturaPila::Menu")
metamodeloArquitecturaPila_Form = Class(name="metamodeloArquitecturaPila::Form")
metamodeloArquitecturaPila_GraphicalComponent = Class(name="metamodeloArquitecturaPila::GraphicalComponent", is_abstract=True)
metamodeloArquitecturaPila_Button = Class(name="metamodeloArquitecturaPila::Button")
SimpleComponent = Class(name="SimpleComponent")
metamodeloArquitecturaPila_Input = Class(name="metamodeloArquitecturaPila::Input")
metamodeloArquitecturaPila_MenuItem = Class(name="metamodeloArquitecturaPila::MenuItem")
metamodeloArquitecturaPila_TextArea = Class(name="metamodeloArquitecturaPila::TextArea")
metamodeloArquitecturaPila_Label = Class(name="metamodeloArquitecturaPila::Label")
GraphicalComponent = Class(name="GraphicalComponent")
metamodeloArquitecturaPila_ComplexComponent = Class(name="metamodeloArquitecturaPila::ComplexComponent", is_abstract=True)
metamodeloArquitecturaPila_DropdownList = Class(name="metamodeloArquitecturaPila::DropdownList")
metamodeloArquitecturaPila_ListItem = Class(name="metamodeloArquitecturaPila::ListItem")
metamodeloArquitecturaPila_Grid = Class(name="metamodeloArquitecturaPila::Grid")
ComplexComponent = Class(name="ComplexComponent")
metamodeloArquitecturaPila_Entity = Class(name="metamodeloArquitecturaPila::Entity")
metamodeloArquitecturaPila_DataType = Class(name="metamodeloArquitecturaPila::DataType")
metamodeloArquitecturaPila_Parameter = Class(name="metamodeloArquitecturaPila::Parameter")
metamodeloArquitecturaPila_Function = Class(name="metamodeloArquitecturaPila::Function")
metamodeloArquitecturaPila_Attribute = Class(name="metamodeloArquitecturaPila::Attribute")
metamodeloArquitecturaPila_Method = Class(name="metamodeloArquitecturaPila::Method")
metamodeloArquitecturaPila_Enum = Class(name="metamodeloArquitecturaPila::Enum")
metamodeloArquitecturaPila_Body = Class(name="metamodeloArquitecturaPila::Body")
metamodeloArquitecturaPila_Integer = Class(name="metamodeloArquitecturaPila::Integer")
DataType = Class(name="DataType")
metamodeloArquitecturaPila_Float = Class(name="metamodeloArquitecturaPila::Float")
metamodeloArquitecturaPila_Boolean = Class(name="metamodeloArquitecturaPila::Boolean")
metamodeloArquitecturaPila_String = Class(name="metamodeloArquitecturaPila::String")
metamodeloArquitecturaPila_Date = Class(name="metamodeloArquitecturaPila::Date")
metamodeloArquitecturaPila_FunctionBody = Class(name="metamodeloArquitecturaPila::FunctionBody")
metamodeloArquitecturaPila_Create = Class(name="metamodeloArquitecturaPila::Create")
ServiceType = Class(name="ServiceType")
metamodeloArquitecturaPila_Read = Class(name="metamodeloArquitecturaPila::Read")
metamodeloArquitecturaPila_Update = Class(name="metamodeloArquitecturaPila::Update")
metamodeloArquitecturaPila_Delete = Class(name="metamodeloArquitecturaPila::Delete")
metamodeloArquitecturaPila_Other = Class(name="metamodeloArquitecturaPila::Other")
metamodeloArquitecturaPila_Text = Class(name="metamodeloArquitecturaPila::Text")
Input = Class(name="Input")
metamodeloArquitecturaPila_Radio = Class(name="metamodeloArquitecturaPila::Radio")
metamodeloArquitecturaPila_Check = Class(name="metamodeloArquitecturaPila::Check")
metamodeloArquitecturaPila_Number = Class(name="metamodeloArquitecturaPila::Number")
metamodeloArquitecturaPila_DatePicker = Class(name="metamodeloArquitecturaPila::DatePicker")
metamodeloArquitecturaPila_Select = Class(name="metamodeloArquitecturaPila::Select")

# metamodeloArquitecturaPila_ServiceType class attributes and methods
metamodeloArquitecturaPila_ServiceType_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_ServiceType.attributes={metamodeloArquitecturaPila_ServiceType_name}

# metamodeloArquitecturaPila_BusinessLogic class attributes and methods
metamodeloArquitecturaPila_BusinessLogic_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_BusinessLogic.attributes={metamodeloArquitecturaPila_BusinessLogic_name}

# metamodeloArquitecturaPila_Architecture class attributes and methods
metamodeloArquitecturaPila_Architecture_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_Architecture.attributes={metamodeloArquitecturaPila_Architecture_name}

# metamodeloArquitecturaPila_View class attributes and methods
metamodeloArquitecturaPila_View_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_View.attributes={metamodeloArquitecturaPila_View_name}

# metamodeloArquitecturaPila_BusinessModel class attributes and methods

# metamodeloArquitecturaPila_Service class attributes and methods
metamodeloArquitecturaPila_Service_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_Service.attributes={metamodeloArquitecturaPila_Service_name}

# metamodeloArquitecturaPila_SimpleComponent class attributes and methods
metamodeloArquitecturaPila_SimpleComponent_value: Property = Property(name="value", type=StringType)
metamodeloArquitecturaPila_SimpleComponent.attributes={metamodeloArquitecturaPila_SimpleComponent_value}

# metamodeloArquitecturaPila_TitleBar class attributes and methods
metamodeloArquitecturaPila_TitleBar_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_TitleBar_id: Property = Property(name="id", type=StringType)
metamodeloArquitecturaPila_TitleBar.attributes={metamodeloArquitecturaPila_TitleBar_id, metamodeloArquitecturaPila_TitleBar_name}

# metamodeloArquitecturaPila_Menu class attributes and methods
metamodeloArquitecturaPila_Menu_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_Menu_id: Property = Property(name="id", type=StringType)
metamodeloArquitecturaPila_Menu.attributes={metamodeloArquitecturaPila_Menu_id, metamodeloArquitecturaPila_Menu_name}

# metamodeloArquitecturaPila_Form class attributes and methods
metamodeloArquitecturaPila_Form_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_Form_id: Property = Property(name="id", type=StringType)
metamodeloArquitecturaPila_Form.attributes={metamodeloArquitecturaPila_Form_name, metamodeloArquitecturaPila_Form_id}

# metamodeloArquitecturaPila_GraphicalComponent class attributes and methods
metamodeloArquitecturaPila_GraphicalComponent_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_GraphicalComponent_length: Property = Property(name="length", type=StringType)
metamodeloArquitecturaPila_GraphicalComponent_height: Property = Property(name="height", type=StringType)
metamodeloArquitecturaPila_GraphicalComponent_id: Property = Property(name="id", type=StringType)
metamodeloArquitecturaPila_GraphicalComponent_displayName: Property = Property(name="displayName", type=StringType)
metamodeloArquitecturaPila_GraphicalComponent.attributes={metamodeloArquitecturaPila_GraphicalComponent_length, metamodeloArquitecturaPila_GraphicalComponent_displayName, metamodeloArquitecturaPila_GraphicalComponent_name, metamodeloArquitecturaPila_GraphicalComponent_id, metamodeloArquitecturaPila_GraphicalComponent_height}

# metamodeloArquitecturaPila_Button class attributes and methods
metamodeloArquitecturaPila_Button_action: Property = Property(name="action", type=StringType)
metamodeloArquitecturaPila_Button.attributes={metamodeloArquitecturaPila_Button_action}

# SimpleComponent class attributes and methods

# metamodeloArquitecturaPila_Input class attributes and methods
metamodeloArquitecturaPila_Input_action: Property = Property(name="action", type=StringType)
metamodeloArquitecturaPila_Input.attributes={metamodeloArquitecturaPila_Input_action}

# metamodeloArquitecturaPila_MenuItem class attributes and methods
metamodeloArquitecturaPila_MenuItem_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_MenuItem_id: Property = Property(name="id", type=StringType)
metamodeloArquitecturaPila_MenuItem.attributes={metamodeloArquitecturaPila_MenuItem_name, metamodeloArquitecturaPila_MenuItem_id}

# metamodeloArquitecturaPila_TextArea class attributes and methods
metamodeloArquitecturaPila_TextArea_visibleLines: Property = Property(name="visibleLines", type=StringType)
metamodeloArquitecturaPila_TextArea.attributes={metamodeloArquitecturaPila_TextArea_visibleLines}

# metamodeloArquitecturaPila_Label class attributes and methods

# GraphicalComponent class attributes and methods

# metamodeloArquitecturaPila_ComplexComponent class attributes and methods

# metamodeloArquitecturaPila_DropdownList class attributes and methods

# metamodeloArquitecturaPila_ListItem class attributes and methods
metamodeloArquitecturaPila_ListItem_isSelected: Property = Property(name="isSelected", type=StringType)
metamodeloArquitecturaPila_ListItem_action: Property = Property(name="action", type=StringType)
metamodeloArquitecturaPila_ListItem.attributes={metamodeloArquitecturaPila_ListItem_isSelected, metamodeloArquitecturaPila_ListItem_action}

# metamodeloArquitecturaPila_Grid class attributes and methods
metamodeloArquitecturaPila_Grid_cols: Property = Property(name="cols", type=StringType)
metamodeloArquitecturaPila_Grid_rows: Property = Property(name="rows", type=StringType)
metamodeloArquitecturaPila_Grid.attributes={metamodeloArquitecturaPila_Grid_rows, metamodeloArquitecturaPila_Grid_cols}

# ComplexComponent class attributes and methods

# metamodeloArquitecturaPila_Entity class attributes and methods
metamodeloArquitecturaPila_Entity_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_Entity.attributes={metamodeloArquitecturaPila_Entity_name}

# metamodeloArquitecturaPila_DataType class attributes and methods
metamodeloArquitecturaPila_DataType_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_DataType.attributes={metamodeloArquitecturaPila_DataType_name}

# metamodeloArquitecturaPila_Parameter class attributes and methods
metamodeloArquitecturaPila_Parameter_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_Parameter.attributes={metamodeloArquitecturaPila_Parameter_name}

# metamodeloArquitecturaPila_Function class attributes and methods
metamodeloArquitecturaPila_Function_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_Function.attributes={metamodeloArquitecturaPila_Function_name}

# metamodeloArquitecturaPila_Attribute class attributes and methods
metamodeloArquitecturaPila_Attribute_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_Attribute_value: Property = Property(name="value", type=StringType)
metamodeloArquitecturaPila_Attribute.attributes={metamodeloArquitecturaPila_Attribute_value, metamodeloArquitecturaPila_Attribute_name}

# metamodeloArquitecturaPila_Method class attributes and methods
metamodeloArquitecturaPila_Method_name: Property = Property(name="name", type=StringType)
metamodeloArquitecturaPila_Method.attributes={metamodeloArquitecturaPila_Method_name}

# metamodeloArquitecturaPila_Enum class attributes and methods

# metamodeloArquitecturaPila_Body class attributes and methods
metamodeloArquitecturaPila_Body_content: Property = Property(name="content", type=StringType)
metamodeloArquitecturaPila_Body.attributes={metamodeloArquitecturaPila_Body_content}

# metamodeloArquitecturaPila_Integer class attributes and methods

# DataType class attributes and methods

# metamodeloArquitecturaPila_Float class attributes and methods

# metamodeloArquitecturaPila_Boolean class attributes and methods

# metamodeloArquitecturaPila_String class attributes and methods

# metamodeloArquitecturaPila_Date class attributes and methods

# metamodeloArquitecturaPila_FunctionBody class attributes and methods
metamodeloArquitecturaPila_FunctionBody_content: Property = Property(name="content", type=StringType)
metamodeloArquitecturaPila_FunctionBody.attributes={metamodeloArquitecturaPila_FunctionBody_content}

# metamodeloArquitecturaPila_Create class attributes and methods

# ServiceType class attributes and methods

# metamodeloArquitecturaPila_Read class attributes and methods

# metamodeloArquitecturaPila_Update class attributes and methods

# metamodeloArquitecturaPila_Delete class attributes and methods

# metamodeloArquitecturaPila_Other class attributes and methods

# metamodeloArquitecturaPila_Text class attributes and methods

# Input class attributes and methods

# metamodeloArquitecturaPila_Radio class attributes and methods

# metamodeloArquitecturaPila_Check class attributes and methods

# metamodeloArquitecturaPila_Number class attributes and methods

# metamodeloArquitecturaPila_DatePicker class attributes and methods

# metamodeloArquitecturaPila_Select class attributes and methods

# Relationships
services3: BinaryAssociation = BinaryAssociation(
    name="services3",
    ends={
        Property(name="metamodeloArquitecturaPila_Architecture4", type=metamodeloArquitecturaPila_Service, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="metamodeloArquitecturaPila_Service", type=metamodeloArquitecturaPila_Architecture, multiplicity=Multiplicity(1, 1))
    }
)
serviceTypes5: BinaryAssociation = BinaryAssociation(
    name="serviceTypes5",
    ends={
        Property(name="metamodeloArquitecturaPila_ServiceType", type=metamodeloArquitecturaPila_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Architecture6", type=metamodeloArquitecturaPila_ServiceType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
logic7: BinaryAssociation = BinaryAssociation(
    name="logic7",
    ends={
        Property(name="metamodeloArquitecturaPila_BusinessLogic", type=metamodeloArquitecturaPila_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Architecture8", type=metamodeloArquitecturaPila_BusinessLogic, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
views0: BinaryAssociation = BinaryAssociation(
    name="views0",
    ends={
        Property(name="metamodeloArquitecturaPila_View", type=metamodeloArquitecturaPila_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Architecture", type=metamodeloArquitecturaPila_View, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
businessModel1: BinaryAssociation = BinaryAssociation(
    name="businessModel1",
    ends={
        Property(name="metamodeloArquitecturaPila_BusinessModel", type=metamodeloArquitecturaPila_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Architecture2", type=metamodeloArquitecturaPila_BusinessModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
childs18: BinaryAssociation = BinaryAssociation(
    name="childs18",
    ends={
        Property(name="metamodeloArquitecturaPila_View19", type=metamodeloArquitecturaPila_View, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_View17", type=metamodeloArquitecturaPila_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
titleComponents20: BinaryAssociation = BinaryAssociation(
    name="titleComponents20",
    ends={
        Property(name="metamodeloArquitecturaPila_SimpleComponent", type=metamodeloArquitecturaPila_TitleBar, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_TitleBar21", type=metamodeloArquitecturaPila_SimpleComponent, multiplicity=Multiplicity(0, 9999))
    }
)
title9: BinaryAssociation = BinaryAssociation(
    name="title9",
    ends={
        Property(name="metamodeloArquitecturaPila_TitleBar", type=metamodeloArquitecturaPila_View, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_View10", type=metamodeloArquitecturaPila_TitleBar, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
menu11: BinaryAssociation = BinaryAssociation(
    name="menu11",
    ends={
        Property(name="metamodeloArquitecturaPila_Menu", type=metamodeloArquitecturaPila_View, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_View12", type=metamodeloArquitecturaPila_Menu, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forms13: BinaryAssociation = BinaryAssociation(
    name="forms13",
    ends={
        Property(name="metamodeloArquitecturaPila_Form", type=metamodeloArquitecturaPila_View, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_View14", type=metamodeloArquitecturaPila_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gComponents15: BinaryAssociation = BinaryAssociation(
    name="gComponents15",
    ends={
        Property(name="metamodeloArquitecturaPila_GraphicalComponent", type=metamodeloArquitecturaPila_View, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_View16", type=metamodeloArquitecturaPila_GraphicalComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
menuItemComponent27: BinaryAssociation = BinaryAssociation(
    name="menuItemComponent27",
    ends={
        Property(name="metamodeloArquitecturaPila_MenuItem28", type=metamodeloArquitecturaPila_SimpleComponent, multiplicity=Multiplicity(0, 1)),
        Property(name="metamodeloArquitecturaPila_SimpleComponent29", type=metamodeloArquitecturaPila_MenuItem, multiplicity=Multiplicity(1, 1))
    }
)
items22: BinaryAssociation = BinaryAssociation(
    name="items22",
    ends={
        Property(name="metamodeloArquitecturaPila_MenuItem", type=metamodeloArquitecturaPila_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Menu23", type=metamodeloArquitecturaPila_MenuItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
formComponents24: BinaryAssociation = BinaryAssociation(
    name="formComponents24",
    ends={
        Property(name="metamodeloArquitecturaPila_GraphicalComponent26", type=metamodeloArquitecturaPila_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Form25", type=metamodeloArquitecturaPila_GraphicalComponent, multiplicity=Multiplicity(0, 9999))
    }
)
items30: BinaryAssociation = BinaryAssociation(
    name="items30",
    ends={
        Property(name="metamodeloArquitecturaPila_ListItem", type=metamodeloArquitecturaPila_DropdownList, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_DropdownList", type=metamodeloArquitecturaPila_ListItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
entities41: BinaryAssociation = BinaryAssociation(
    name="entities41",
    ends={
        Property(name="metamodeloArquitecturaPila_Entity", type=metamodeloArquitecturaPila_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_BusinessModel42", type=metamodeloArquitecturaPila_Entity, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dataTypes43: BinaryAssociation = BinaryAssociation(
    name="dataTypes43",
    ends={
        Property(name="metamodeloArquitecturaPila_DataType", type=metamodeloArquitecturaPila_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_BusinessModel44", type=metamodeloArquitecturaPila_DataType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
serviceType31: BinaryAssociation = BinaryAssociation(
    name="serviceType31",
    ends={
        Property(name="metamodeloArquitecturaPila_ServiceType33", type=metamodeloArquitecturaPila_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Service32", type=metamodeloArquitecturaPila_ServiceType, multiplicity=Multiplicity(0, 1))
    }
)
requestParams34: BinaryAssociation = BinaryAssociation(
    name="requestParams34",
    ends={
        Property(name="metamodeloArquitecturaPila_Parameter", type=metamodeloArquitecturaPila_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Service35", type=metamodeloArquitecturaPila_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
responseParam36: BinaryAssociation = BinaryAssociation(
    name="responseParam36",
    ends={
        Property(name="metamodeloArquitecturaPila_Parameter38", type=metamodeloArquitecturaPila_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Service37", type=metamodeloArquitecturaPila_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
dispatcher39: BinaryAssociation = BinaryAssociation(
    name="dispatcher39",
    ends={
        Property(name="metamodeloArquitecturaPila_Function", type=metamodeloArquitecturaPila_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Service40", type=metamodeloArquitecturaPila_Function, multiplicity=Multiplicity(1, 1))
    }
)
entryParams55: BinaryAssociation = BinaryAssociation(
    name="entryParams55",
    ends={
        Property(name="metamodeloArquitecturaPila_Parameter57", type=metamodeloArquitecturaPila_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Method56", type=metamodeloArquitecturaPila_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
returnParam58: BinaryAssociation = BinaryAssociation(
    name="returnParam58",
    ends={
        Property(name="metamodeloArquitecturaPila_Parameter60", type=metamodeloArquitecturaPila_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Method59", type=metamodeloArquitecturaPila_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
attributes45: BinaryAssociation = BinaryAssociation(
    name="attributes45",
    ends={
        Property(name="metamodeloArquitecturaPila_Attribute", type=metamodeloArquitecturaPila_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Entity46", type=metamodeloArquitecturaPila_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
methods47: BinaryAssociation = BinaryAssociation(
    name="methods47",
    ends={
        Property(name="metamodeloArquitecturaPila_Method", type=metamodeloArquitecturaPila_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Entity48", type=metamodeloArquitecturaPila_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenEntities50: BinaryAssociation = BinaryAssociation(
    name="childrenEntities50",
    ends={
        Property(name="metamodeloArquitecturaPila_Entity51", type=metamodeloArquitecturaPila_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Entity49", type=metamodeloArquitecturaPila_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attType52: BinaryAssociation = BinaryAssociation(
    name="attType52",
    ends={
        Property(name="metamodeloArquitecturaPila_DataType54", type=metamodeloArquitecturaPila_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Attribute53", type=metamodeloArquitecturaPila_DataType, multiplicity=Multiplicity(1, 1))
    }
)
functions63: BinaryAssociation = BinaryAssociation(
    name="functions63",
    ends={
        Property(name="metamodeloArquitecturaPila_Function65", type=metamodeloArquitecturaPila_BusinessLogic, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_BusinessLogic64", type=metamodeloArquitecturaPila_Function, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
body61: BinaryAssociation = BinaryAssociation(
    name="body61",
    ends={
        Property(name="metamodeloArquitecturaPila_Body", type=metamodeloArquitecturaPila_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Method62", type=metamodeloArquitecturaPila_Body, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnParam69: BinaryAssociation = BinaryAssociation(
    name="returnParam69",
    ends={
        Property(name="metamodeloArquitecturaPila_Parameter71", type=metamodeloArquitecturaPila_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Function70", type=metamodeloArquitecturaPila_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
body72: BinaryAssociation = BinaryAssociation(
    name="body72",
    ends={
        Property(name="metamodeloArquitecturaPila_FunctionBody", type=metamodeloArquitecturaPila_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Function73", type=metamodeloArquitecturaPila_FunctionBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
entryParams66: BinaryAssociation = BinaryAssociation(
    name="entryParams66",
    ends={
        Property(name="metamodeloArquitecturaPila_Parameter68", type=metamodeloArquitecturaPila_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Function67", type=metamodeloArquitecturaPila_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
paramType74: BinaryAssociation = BinaryAssociation(
    name="paramType74",
    ends={
        Property(name="metamodeloArquitecturaPila_DataType76", type=metamodeloArquitecturaPila_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodeloArquitecturaPila_Parameter75", type=metamodeloArquitecturaPila_DataType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_metamodeloArquitecturaPila_Button_SimpleComponent = Generalization(general=SimpleComponent, specific=metamodeloArquitecturaPila_Button)
gen_metamodeloArquitecturaPila_Input_SimpleComponent = Generalization(general=SimpleComponent, specific=metamodeloArquitecturaPila_Input)
gen_metamodeloArquitecturaPila_Grid_ComplexComponent = Generalization(general=ComplexComponent, specific=metamodeloArquitecturaPila_Grid)
gen_metamodeloArquitecturaPila_TextArea_ComplexComponent = Generalization(general=ComplexComponent, specific=metamodeloArquitecturaPila_TextArea)
gen_metamodeloArquitecturaPila_Label_SimpleComponent = Generalization(general=SimpleComponent, specific=metamodeloArquitecturaPila_Label)
gen_metamodeloArquitecturaPila_SimpleComponent_GraphicalComponent = Generalization(general=GraphicalComponent, specific=metamodeloArquitecturaPila_SimpleComponent)
gen_metamodeloArquitecturaPila_ComplexComponent_GraphicalComponent = Generalization(general=GraphicalComponent, specific=metamodeloArquitecturaPila_ComplexComponent)
gen_metamodeloArquitecturaPila_DropdownList_SimpleComponent = Generalization(general=SimpleComponent, specific=metamodeloArquitecturaPila_DropdownList)
gen_metamodeloArquitecturaPila_Date_DataType = Generalization(general=DataType, specific=metamodeloArquitecturaPila_Date)
gen_metamodeloArquitecturaPila_Enum_DataType = Generalization(general=DataType, specific=metamodeloArquitecturaPila_Enum)
gen_metamodeloArquitecturaPila_Integer_DataType = Generalization(general=DataType, specific=metamodeloArquitecturaPila_Integer)
gen_metamodeloArquitecturaPila_Float_DataType = Generalization(general=DataType, specific=metamodeloArquitecturaPila_Float)
gen_metamodeloArquitecturaPila_Boolean_DataType = Generalization(general=DataType, specific=metamodeloArquitecturaPila_Boolean)
gen_metamodeloArquitecturaPila_String_DataType = Generalization(general=DataType, specific=metamodeloArquitecturaPila_String)
gen_metamodeloArquitecturaPila_Create_ServiceType = Generalization(general=ServiceType, specific=metamodeloArquitecturaPila_Create)
gen_metamodeloArquitecturaPila_Read_ServiceType = Generalization(general=ServiceType, specific=metamodeloArquitecturaPila_Read)
gen_metamodeloArquitecturaPila_Update_ServiceType = Generalization(general=ServiceType, specific=metamodeloArquitecturaPila_Update)
gen_metamodeloArquitecturaPila_Delete_ServiceType = Generalization(general=ServiceType, specific=metamodeloArquitecturaPila_Delete)
gen_metamodeloArquitecturaPila_Other_DataType = Generalization(general=DataType, specific=metamodeloArquitecturaPila_Other)
gen_metamodeloArquitecturaPila_Text_Input = Generalization(general=Input, specific=metamodeloArquitecturaPila_Text)
gen_metamodeloArquitecturaPila_Radio_Input = Generalization(general=Input, specific=metamodeloArquitecturaPila_Radio)
gen_metamodeloArquitecturaPila_Check_Input = Generalization(general=Input, specific=metamodeloArquitecturaPila_Check)
gen_metamodeloArquitecturaPila_Number_Input = Generalization(general=Input, specific=metamodeloArquitecturaPila_Number)
gen_metamodeloArquitecturaPila_DatePicker_Input = Generalization(general=Input, specific=metamodeloArquitecturaPila_DatePicker)
gen_metamodeloArquitecturaPila_Select_ComplexComponent = Generalization(general=ComplexComponent, specific=metamodeloArquitecturaPila_Select)

# Domain Model
domain_model = DomainModel(
    name="metamodeloArquitecturaPila",
    types={metamodeloArquitecturaPila_ServiceType, metamodeloArquitecturaPila_BusinessLogic, metamodeloArquitecturaPila_Architecture, metamodeloArquitecturaPila_View, metamodeloArquitecturaPila_BusinessModel, metamodeloArquitecturaPila_Service, metamodeloArquitecturaPila_SimpleComponent, metamodeloArquitecturaPila_TitleBar, metamodeloArquitecturaPila_Menu, metamodeloArquitecturaPila_Form, metamodeloArquitecturaPila_GraphicalComponent, metamodeloArquitecturaPila_Button, SimpleComponent, metamodeloArquitecturaPila_Input, metamodeloArquitecturaPila_MenuItem, metamodeloArquitecturaPila_TextArea, metamodeloArquitecturaPila_Label, GraphicalComponent, metamodeloArquitecturaPila_ComplexComponent, metamodeloArquitecturaPila_DropdownList, metamodeloArquitecturaPila_ListItem, metamodeloArquitecturaPila_Grid, ComplexComponent, metamodeloArquitecturaPila_Entity, metamodeloArquitecturaPila_DataType, metamodeloArquitecturaPila_Parameter, metamodeloArquitecturaPila_Function, metamodeloArquitecturaPila_Attribute, metamodeloArquitecturaPila_Method, metamodeloArquitecturaPila_Enum, metamodeloArquitecturaPila_Body, metamodeloArquitecturaPila_Integer, DataType, metamodeloArquitecturaPila_Float, metamodeloArquitecturaPila_Boolean, metamodeloArquitecturaPila_String, metamodeloArquitecturaPila_Date, metamodeloArquitecturaPila_FunctionBody, metamodeloArquitecturaPila_Create, ServiceType, metamodeloArquitecturaPila_Read, metamodeloArquitecturaPila_Update, metamodeloArquitecturaPila_Delete, metamodeloArquitecturaPila_Other, metamodeloArquitecturaPila_Text, Input, metamodeloArquitecturaPila_Radio, metamodeloArquitecturaPila_Check, metamodeloArquitecturaPila_Number, metamodeloArquitecturaPila_DatePicker, metamodeloArquitecturaPila_Select},
    associations={services3, serviceTypes5, logic7, views0, businessModel1, childs18, titleComponents20, title9, menu11, forms13, gComponents15, menuItemComponent27, items22, formComponents24, items30, entities41, dataTypes43, serviceType31, requestParams34, responseParam36, dispatcher39, entryParams55, returnParam58, attributes45, methods47, childrenEntities50, attType52, functions63, body61, returnParam69, body72, entryParams66, paramType74},
    generalizations={gen_metamodeloArquitecturaPila_Button_SimpleComponent, gen_metamodeloArquitecturaPila_Input_SimpleComponent, gen_metamodeloArquitecturaPila_Grid_ComplexComponent, gen_metamodeloArquitecturaPila_TextArea_ComplexComponent, gen_metamodeloArquitecturaPila_Label_SimpleComponent, gen_metamodeloArquitecturaPila_SimpleComponent_GraphicalComponent, gen_metamodeloArquitecturaPila_ComplexComponent_GraphicalComponent, gen_metamodeloArquitecturaPila_DropdownList_SimpleComponent, gen_metamodeloArquitecturaPila_Date_DataType, gen_metamodeloArquitecturaPila_Enum_DataType, gen_metamodeloArquitecturaPila_Integer_DataType, gen_metamodeloArquitecturaPila_Float_DataType, gen_metamodeloArquitecturaPila_Boolean_DataType, gen_metamodeloArquitecturaPila_String_DataType, gen_metamodeloArquitecturaPila_Create_ServiceType, gen_metamodeloArquitecturaPila_Read_ServiceType, gen_metamodeloArquitecturaPila_Update_ServiceType, gen_metamodeloArquitecturaPila_Delete_ServiceType, gen_metamodeloArquitecturaPila_Other_DataType, gen_metamodeloArquitecturaPila_Text_Input, gen_metamodeloArquitecturaPila_Radio_Input, gen_metamodeloArquitecturaPila_Check_Input, gen_metamodeloArquitecturaPila_Number_Input, gen_metamodeloArquitecturaPila_DatePicker_Input, gen_metamodeloArquitecturaPila_Select_ComplexComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)