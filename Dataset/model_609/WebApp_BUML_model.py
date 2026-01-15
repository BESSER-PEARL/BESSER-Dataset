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
Behavior: Enumeration = Enumeration(
    name="Behavior",
    literals={
            EnumerationLiteral(name="CASCADE"),
			EnumerationLiteral(name="RESTRICT")
    }
)

Charset: Enumeration = Enumeration(
    name="Charset",
    literals={
            EnumerationLiteral(name="CP1257"),
			EnumerationLiteral(name="DEC8"),
			EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="CP850"),
			EnumerationLiteral(name="LATIN2"),
			EnumerationLiteral(name="ARMSCII8"),
			EnumerationLiteral(name="ASCII"),
			EnumerationLiteral(name="BIG5"),
			EnumerationLiteral(name="CP852"),
			EnumerationLiteral(name="CP866"),
			EnumerationLiteral(name="CP932"),
			EnumerationLiteral(name="CP1250"),
			EnumerationLiteral(name="CP1251"),
			EnumerationLiteral(name="CP1256"),
			EnumerationLiteral(name="SWE7"),
			EnumerationLiteral(name="TIS620"),
			EnumerationLiteral(name="UCS2"),
			EnumerationLiteral(name="UJIS"),
			EnumerationLiteral(name="EUCJMPS"),
			EnumerationLiteral(name="EUCKR"),
			EnumerationLiteral(name="GB2312"),
			EnumerationLiteral(name="GBK"),
			EnumerationLiteral(name="GEOSTD8"),
			EnumerationLiteral(name="GREEK"),
			EnumerationLiteral(name="HEBREW"),
			EnumerationLiteral(name="HP8"),
			EnumerationLiteral(name="KEYBCS2"),
			EnumerationLiteral(name="KOI8R"),
			EnumerationLiteral(name="KOI8U"),
			EnumerationLiteral(name="LATIN1"),
			EnumerationLiteral(name="LATIN5"),
			EnumerationLiteral(name="LATIN7"),
			EnumerationLiteral(name="MACCE"),
			EnumerationLiteral(name="MACROMAN"),
			EnumerationLiteral(name="SJIS"),
			EnumerationLiteral(name="UTF8")
    }
)

ColumnType: Enumeration = Enumeration(
    name="ColumnType",
    literals={
            EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="BIT"),
			EnumerationLiteral(name="TINYBLOB"),
			EnumerationLiteral(name="BLOB"),
			EnumerationLiteral(name="MEDIUMBLOB"),
			EnumerationLiteral(name="BIGINT"),
			EnumerationLiteral(name="TINYINT"),
			EnumerationLiteral(name="MEDIUMINT"),
			EnumerationLiteral(name="SMALLINT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="LONGBLOB"),
			EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="VARCHAR"),
			EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="VARBINARY"),
			EnumerationLiteral(name="TEXT"),
			EnumerationLiteral(name="TINYTEXT"),
			EnumerationLiteral(name="MEDIUMTEXT"),
			EnumerationLiteral(name="LONGTEXT"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="DATETIME"),
			EnumerationLiteral(name="TIME"),
			EnumerationLiteral(name="TIMESTAMP"),
			EnumerationLiteral(name="YEAR")
    }
)

FormMethod: Enumeration = Enumeration(
    name="FormMethod",
    literals={
            EnumerationLiteral(name="GET"),
			EnumerationLiteral(name="POST")
    }
)

InputType: Enumeration = Enumeration(
    name="InputType",
    literals={
            EnumerationLiteral(name="TEXT"),
			EnumerationLiteral(name="BUTTON")
    }
)

# Classes
webapp_WebApp = Class(name="webapp::WebApp")
webapp_Controller = Class(name="webapp::Controller")
webapp_Resource = Class(name="webapp::Resource")
webapp_AppConfig = Class(name="webapp::AppConfig")
webapp_WebConfig = Class(name="webapp::WebConfig")
webapp_Library = Class(name="webapp::Library")
webapp_View = Class(name="webapp::View")
webapp_Model = Class(name="webapp::Model")
webapp_Page = Class(name="webapp::Page")
webapp_Navigation = Class(name="webapp::Navigation")
webapp_Table = Class(name="webapp::Table")
webapp_Image = Class(name="webapp::Image")
webapp_File = Class(name="webapp::File")
webapp_BusinessObject = Class(name="webapp::BusinessObject")
webapp_Validator = Class(name="webapp::Validator")
webapp_Action = Class(name="webapp::Action")
webapp_Constraint = Class(name="webapp::Constraint")
webapp_Properties = Class(name="webapp::Properties")
webapp_Mapping = Class(name="webapp::Mapping")
webapp_Column = Class(name="webapp::Column")
webapp_Detail = Class(name="webapp::Detail")
webapp_PrimaryKey = Class(name="webapp::PrimaryKey")
webapp_Unique = Class(name="webapp::Unique")
webapp_Check = Class(name="webapp::Check")
webapp_ForeignKey = Class(name="webapp::ForeignKey")
webapp_OnDelete = Class(name="webapp::OnDelete")
webapp_OnUpdate = Class(name="webapp::OnUpdate")
webapp_Text = Class(name="webapp::Text")
Instruction = Class(name="Instruction")
webapp_Instruction = Class(name="webapp::Instruction")
webapp_Form = Class(name="webapp::Form")
Tag = Class(name="Tag")
webapp_Tag = Class(name="webapp::Tag", is_abstract=True)
webapp_Input = Class(name="webapp::Input")
webapp_Attribute = Class(name="webapp::Attribute")
webapp_Tr = Class(name="webapp::Tr")
webapp_Th = Class(name="webapp::Th")
webapp_Td = Class(name="webapp::Td")
webapp_Field = Class(name="webapp::Field")
webapp_TableHTML = Class(name="webapp::TableHTML")
webapp_Messages = Class(name="webapp::Messages")

# webapp_WebApp class attributes and methods
webapp_WebApp_name: Property = Property(name="name", type=StringType)
webapp_WebApp_framework: Property = Property(name="framework", type=StringType)
webapp_WebApp.attributes={webapp_WebApp_name, webapp_WebApp_framework}

# webapp_Controller class attributes and methods

# webapp_Resource class attributes and methods

# webapp_AppConfig class attributes and methods

# webapp_WebConfig class attributes and methods
webapp_WebConfig_displayName: Property = Property(name="displayName", type=StringType)
webapp_WebConfig.attributes={webapp_WebConfig_displayName}

# webapp_Library class attributes and methods

# webapp_View class attributes and methods

# webapp_Model class attributes and methods
webapp_Model_databaseName: Property = Property(name="databaseName", type=StringType)
webapp_Model_url: Property = Property(name="url", type=StringType)
webapp_Model_userName: Property = Property(name="userName", type=StringType)
webapp_Model_password: Property = Property(name="password", type=StringType)
webapp_Model.attributes={webapp_Model_databaseName, webapp_Model_userName, webapp_Model_url, webapp_Model_password}

# webapp_Page class attributes and methods
webapp_Page_name: Property = Property(name="name", type=StringType)
webapp_Page_isMain: Property = Property(name="isMain", type=BooleanType)
webapp_Page.attributes={webapp_Page_name, webapp_Page_isMain}

# webapp_Navigation class attributes and methods
webapp_Navigation_message: Property = Property(name="message", type=StringType)
webapp_Navigation.attributes={webapp_Navigation_message}

# webapp_Table class attributes and methods
webapp_Table_name: Property = Property(name="name", type=StringType)
webapp_Table_charset: Property = Property(name="charset", type=StringType)
webapp_Table.attributes={webapp_Table_charset, webapp_Table_name}

# webapp_Image class attributes and methods

# webapp_File class attributes and methods

# webapp_BusinessObject class attributes and methods
webapp_BusinessObject_name: Property = Property(name="name", type=StringType)
webapp_BusinessObject_package: Property = Property(name="package", type=StringType)
webapp_BusinessObject.attributes={webapp_BusinessObject_name, webapp_BusinessObject_package}

# webapp_Validator class attributes and methods
webapp_Validator_package: Property = Property(name="package", type=StringType)
webapp_Validator_name: Property = Property(name="name", type=StringType)
webapp_Validator.attributes={webapp_Validator_package, webapp_Validator_name}

# webapp_Action class attributes and methods
webapp_Action_name: Property = Property(name="name", type=StringType)
webapp_Action_returnType: Property = Property(name="returnType", type=StringType)
webapp_Action.attributes={webapp_Action_name, webapp_Action_returnType}

# webapp_Constraint class attributes and methods

# webapp_Properties class attributes and methods
webapp_Properties_name: Property = Property(name="name", type=StringType)
webapp_Properties_package: Property = Property(name="package", type=StringType)
webapp_Properties.attributes={webapp_Properties_package, webapp_Properties_name}

# webapp_Mapping class attributes and methods
webapp_Mapping_left: Property = Property(name="left", type=StringType)
webapp_Mapping_right: Property = Property(name="right", type=StringType)
webapp_Mapping.attributes={webapp_Mapping_right, webapp_Mapping_left}

# webapp_Column class attributes and methods
webapp_Column_type: Property = Property(name="type", type=StringType)
webapp_Column_defaultValue: Property = Property(name="defaultValue", type=StringType)
webapp_Column_name: Property = Property(name="name", type=StringType)
webapp_Column_isNotNull: Property = Property(name="isNotNull", type=BooleanType)
webapp_Column_size: Property = Property(name="size", type=IntegerType)
webapp_Column_useZeroFill: Property = Property(name="useZeroFill", type=BooleanType)
webapp_Column.attributes={webapp_Column_isNotNull, webapp_Column_type, webapp_Column_useZeroFill, webapp_Column_name, webapp_Column_defaultValue, webapp_Column_size}

# webapp_Detail class attributes and methods
webapp_Detail_precision: Property = Property(name="precision", type=IntegerType)
webapp_Detail_scale: Property = Property(name="scale", type=IntegerType)
webapp_Detail.attributes={webapp_Detail_precision, webapp_Detail_scale}

# webapp_PrimaryKey class attributes and methods

# webapp_Unique class attributes and methods

# webapp_Check class attributes and methods
webapp_Check_expr: Property = Property(name="expr", type=StringType)
webapp_Check.attributes={webapp_Check_expr}

# webapp_ForeignKey class attributes and methods

# webapp_OnDelete class attributes and methods
webapp_OnDelete_behavior: Property = Property(name="behavior", type=StringType)
webapp_OnDelete.attributes={webapp_OnDelete_behavior}

# webapp_OnUpdate class attributes and methods
webapp_OnUpdate_behavior: Property = Property(name="behavior", type=StringType)
webapp_OnUpdate.attributes={webapp_OnUpdate_behavior}

# webapp_Text class attributes and methods
webapp_Text_content: Property = Property(name="content", type=StringType)
webapp_Text.attributes={webapp_Text_content}

# Instruction class attributes and methods

# webapp_Instruction class attributes and methods

# webapp_Form class attributes and methods
webapp_Form_method: Property = Property(name="method", type=StringType)
webapp_Form.attributes={webapp_Form_method}

# Tag class attributes and methods

# webapp_Tag class attributes and methods
webapp_Tag_property: Property = Property(name="property", type=StringType)
webapp_Tag.attributes={webapp_Tag_property}

# webapp_Input class attributes and methods
webapp_Input_type: Property = Property(name="type", type=StringType)
webapp_Input.attributes={webapp_Input_type}

# webapp_Attribute class attributes and methods
webapp_Attribute_name: Property = Property(name="name", type=StringType)
webapp_Attribute_value: Property = Property(name="value", type=StringType)
webapp_Attribute.attributes={webapp_Attribute_value, webapp_Attribute_name}

# webapp_Tr class attributes and methods

# webapp_Th class attributes and methods

# webapp_Td class attributes and methods

# webapp_Field class attributes and methods
webapp_Field_name: Property = Property(name="name", type=StringType)
webapp_Field_type: Property = Property(name="type", type=StringType)
webapp_Field_defaultValue: Property = Property(name="defaultValue", type=StringType)
webapp_Field.attributes={webapp_Field_type, webapp_Field_defaultValue, webapp_Field_name}

# webapp_TableHTML class attributes and methods

# webapp_Messages class attributes and methods

# Relationships
controller9: BinaryAssociation = BinaryAssociation(
    name="controller9",
    ends={
        Property(name="webapp_Controller", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp10", type=webapp_Controller, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
appConfig0: BinaryAssociation = BinaryAssociation(
    name="appConfig0",
    ends={
        Property(name="webapp_AppConfig", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp", type=webapp_AppConfig, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
webConfig1: BinaryAssociation = BinaryAssociation(
    name="webConfig1",
    ends={
        Property(name="webapp_WebConfig", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp2", type=webapp_WebConfig, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
library3: BinaryAssociation = BinaryAssociation(
    name="library3",
    ends={
        Property(name="webapp_Library", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp4", type=webapp_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
view5: BinaryAssociation = BinaryAssociation(
    name="view5",
    ends={
        Property(name="webapp_View", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp6", type=webapp_View, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model7: BinaryAssociation = BinaryAssociation(
    name="model7",
    ends={
        Property(name="webapp_Model", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp8", type=webapp_Model, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resource11: BinaryAssociation = BinaryAssociation(
    name="resource11",
    ends={
        Property(name="webapp_Resource", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp12", type=webapp_Resource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
page13: BinaryAssociation = BinaryAssociation(
    name="page13",
    ends={
        Property(name="webapp_Page", type=webapp_View, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_View14", type=webapp_Page, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
navigation15: BinaryAssociation = BinaryAssociation(
    name="navigation15",
    ends={
        Property(name="webapp_Navigation", type=webapp_View, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_View16", type=webapp_Navigation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table17: BinaryAssociation = BinaryAssociation(
    name="table17",
    ends={
        Property(name="webapp_Table", type=webapp_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Model18", type=webapp_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
image25: BinaryAssociation = BinaryAssociation(
    name="image25",
    ends={
        Property(name="webapp_Image", type=webapp_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Resource26", type=webapp_Image, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
file27: BinaryAssociation = BinaryAssociation(
    name="file27",
    ends={
        Property(name="webapp_File", type=webapp_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Resource28", type=webapp_File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessObject19: BinaryAssociation = BinaryAssociation(
    name="businessObject19",
    ends={
        Property(name="webapp_BusinessObject", type=webapp_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Model20", type=webapp_BusinessObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validator21: BinaryAssociation = BinaryAssociation(
    name="validator21",
    ends={
        Property(name="webapp_Validator", type=webapp_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Controller22", type=webapp_Validator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
action23: BinaryAssociation = BinaryAssociation(
    name="action23",
    ends={
        Property(name="webapp_Action", type=webapp_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Controller24", type=webapp_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
constraint35: BinaryAssociation = BinaryAssociation(
    name="constraint35",
    ends={
        Property(name="webapp_Constraint", type=webapp_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Table36", type=webapp_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertie29: BinaryAssociation = BinaryAssociation(
    name="propertie29",
    ends={
        Property(name="webapp_Properties", type=webapp_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Resource30", type=webapp_Properties, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapping31: BinaryAssociation = BinaryAssociation(
    name="mapping31",
    ends={
        Property(name="webapp_Mapping", type=webapp_Properties, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Properties32", type=webapp_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column33: BinaryAssociation = BinaryAssociation(
    name="column33",
    ends={
        Property(name="webapp_Column", type=webapp_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Table34", type=webapp_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
detail37: BinaryAssociation = BinaryAssociation(
    name="detail37",
    ends={
        Property(name="webapp_Detail", type=webapp_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Column38", type=webapp_Detail, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column47: BinaryAssociation = BinaryAssociation(
    name="column47",
    ends={
        Property(name="webapp_Column49", type=webapp_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_PrimaryKey48", type=webapp_Column, multiplicity=Multiplicity(1, 9999))
    }
)
primaryKey39: BinaryAssociation = BinaryAssociation(
    name="primaryKey39",
    ends={
        Property(name="webapp_PrimaryKey", type=webapp_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Constraint40", type=webapp_PrimaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unique41: BinaryAssociation = BinaryAssociation(
    name="unique41",
    ends={
        Property(name="webapp_Unique", type=webapp_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Constraint42", type=webapp_Unique, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
check43: BinaryAssociation = BinaryAssociation(
    name="check43",
    ends={
        Property(name="webapp_Check", type=webapp_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Constraint44", type=webapp_Check, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKey45: BinaryAssociation = BinaryAssociation(
    name="foreignKey45",
    ends={
        Property(name="webapp_ForeignKey", type=webapp_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Constraint46", type=webapp_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalColumn50: BinaryAssociation = BinaryAssociation(
    name="externalColumn50",
    ends={
        Property(name="webapp_Column52", type=webapp_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_ForeignKey51", type=webapp_Column, multiplicity=Multiplicity(1, 1))
    }
)
onDelete53: BinaryAssociation = BinaryAssociation(
    name="onDelete53",
    ends={
        Property(name="webapp_OnDelete", type=webapp_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_ForeignKey54", type=webapp_OnDelete, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onUpdate55: BinaryAssociation = BinaryAssociation(
    name="onUpdate55",
    ends={
        Property(name="webapp_OnUpdate", type=webapp_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_ForeignKey56", type=webapp_OnUpdate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalTable57: BinaryAssociation = BinaryAssociation(
    name="externalTable57",
    ends={
        Property(name="webapp_Table59", type=webapp_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_ForeignKey58", type=webapp_Table, multiplicity=Multiplicity(1, 1))
    }
)
internalColumn60: BinaryAssociation = BinaryAssociation(
    name="internalColumn60",
    ends={
        Property(name="webapp_Column62", type=webapp_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_ForeignKey61", type=webapp_Column, multiplicity=Multiplicity(1, 1))
    }
)
column63: BinaryAssociation = BinaryAssociation(
    name="column63",
    ends={
        Property(name="webapp_Column65", type=webapp_Unique, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Unique64", type=webapp_Column, multiplicity=Multiplicity(1, 9999))
    }
)
page66: BinaryAssociation = BinaryAssociation(
    name="page66",
    ends={
        Property(name="webapp_Page68", type=webapp_Validator, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Validator67", type=webapp_Page, multiplicity=Multiplicity(0, 1))
    }
)
tag77: BinaryAssociation = BinaryAssociation(
    name="tag77",
    ends={
        Property(name="webapp_Tag", type=webapp_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Form", type=webapp_Tag, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
properties69: BinaryAssociation = BinaryAssociation(
    name="properties69",
    ends={
        Property(name="webapp_Properties71", type=webapp_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Page70", type=webapp_Properties, multiplicity=Multiplicity(0, 9999))
    }
)
title72: BinaryAssociation = BinaryAssociation(
    name="title72",
    ends={
        Property(name="webapp_Mapping74", type=webapp_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Page73", type=webapp_Mapping, multiplicity=Multiplicity(0, 1))
    }
)
instruction75: BinaryAssociation = BinaryAssociation(
    name="instruction75",
    ends={
        Property(name="webapp_Instruction", type=webapp_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Page76", type=webapp_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessObject78: BinaryAssociation = BinaryAssociation(
    name="businessObject78",
    ends={
        Property(name="webapp_BusinessObject80", type=webapp_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Action79", type=webapp_BusinessObject, multiplicity=Multiplicity(0, 1))
    }
)
attribute81: BinaryAssociation = BinaryAssociation(
    name="attribute81",
    ends={
        Property(name="webapp_Attribute", type=webapp_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Tag82", type=webapp_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tr96: BinaryAssociation = BinaryAssociation(
    name="tr96",
    ends={
        Property(name="webapp_Tr", type=webapp_TableHTML, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_TableHTML", type=webapp_Tr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
th97: BinaryAssociation = BinaryAssociation(
    name="th97",
    ends={
        Property(name="webapp_Th", type=webapp_Tr, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Tr98", type=webapp_Th, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
td99: BinaryAssociation = BinaryAssociation(
    name="td99",
    ends={
        Property(name="webapp_Td", type=webapp_Tr, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Tr100", type=webapp_Td, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action83: BinaryAssociation = BinaryAssociation(
    name="action83",
    ends={
        Property(name="webapp_Action84", type=webapp_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Input", type=webapp_Action, multiplicity=Multiplicity(0, 1))
    }
)
label85: BinaryAssociation = BinaryAssociation(
    name="label85",
    ends={
        Property(name="webapp_Mapping87", type=webapp_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Input86", type=webapp_Mapping, multiplicity=Multiplicity(0, 1))
    }
)
buttonValue88: BinaryAssociation = BinaryAssociation(
    name="buttonValue88",
    ends={
        Property(name="webapp_Mapping90", type=webapp_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Input89", type=webapp_Mapping, multiplicity=Multiplicity(0, 1))
    }
)
textValue91: BinaryAssociation = BinaryAssociation(
    name="textValue91",
    ends={
        Property(name="webapp_Field", type=webapp_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Input92", type=webapp_Field, multiplicity=Multiplicity(0, 1))
    }
)
validator93: BinaryAssociation = BinaryAssociation(
    name="validator93",
    ends={
        Property(name="webapp_Validator95", type=webapp_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Input94", type=webapp_Validator, multiplicity=Multiplicity(0, 1))
    }
)
to122: BinaryAssociation = BinaryAssociation(
    name="to122",
    ends={
        Property(name="webapp_Page124", type=webapp_Navigation, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Navigation123", type=webapp_Page, multiplicity=Multiplicity(1, 1))
    }
)
tag101: BinaryAssociation = BinaryAssociation(
    name="tag101",
    ends={
        Property(name="webapp_Tag103", type=webapp_Td, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Td102", type=webapp_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
field104: BinaryAssociation = BinaryAssociation(
    name="field104",
    ends={
        Property(name="webapp_Field106", type=webapp_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_BusinessObject105", type=webapp_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action107: BinaryAssociation = BinaryAssociation(
    name="action107",
    ends={
        Property(name="webapp_Action109", type=webapp_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_BusinessObject108", type=webapp_Action, multiplicity=Multiplicity(0, 9999))
    }
)
businessObject111: BinaryAssociation = BinaryAssociation(
    name="businessObject111",
    ends={
        Property(name="webapp_BusinessObject112", type=webapp_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_BusinessObject110", type=webapp_BusinessObject, multiplicity=Multiplicity(0, 9999))
    }
)
model113: BinaryAssociation = BinaryAssociation(
    name="model113",
    ends={
        Property(name="webapp_Model115", type=webapp_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_BusinessObject114", type=webapp_Model, multiplicity=Multiplicity(1, 1))
    }
)
businessObject116: BinaryAssociation = BinaryAssociation(
    name="businessObject116",
    ends={
        Property(name="webapp_BusinessObject118", type=webapp_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Field117", type=webapp_BusinessObject, multiplicity=Multiplicity(1, 1))
    }
)
from119: BinaryAssociation = BinaryAssociation(
    name="from119",
    ends={
        Property(name="webapp_Page121", type=webapp_Navigation, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Navigation120", type=webapp_Page, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_webapp_Form_Tag = Generalization(general=Tag, specific=webapp_Form)
gen_webapp_Input_Tag = Generalization(general=Tag, specific=webapp_Input)
gen_webapp_Text_Instruction = Generalization(general=Instruction, specific=webapp_Text)
gen_webapp_Tag_Instruction = Generalization(general=Instruction, specific=webapp_Tag)
gen_webapp_Tr_Tag = Generalization(general=Tag, specific=webapp_Tr)
gen_webapp_TableHTML_Tag = Generalization(general=Tag, specific=webapp_TableHTML)
gen_webapp_Messages_Tag = Generalization(general=Tag, specific=webapp_Messages)
gen_webapp_Td_Tag = Generalization(general=Tag, specific=webapp_Td)
gen_webapp_Th_Tag = Generalization(general=Tag, specific=webapp_Th)

# Domain Model
domain_model = DomainModel(
    name="webapp",
    types={webapp_WebApp, webapp_Controller, webapp_Resource, webapp_AppConfig, webapp_WebConfig, webapp_Library, webapp_View, webapp_Model, webapp_Page, webapp_Navigation, webapp_Table, webapp_Image, webapp_File, webapp_BusinessObject, webapp_Validator, webapp_Action, webapp_Constraint, webapp_Properties, webapp_Mapping, webapp_Column, webapp_Detail, webapp_PrimaryKey, webapp_Unique, webapp_Check, webapp_ForeignKey, webapp_OnDelete, webapp_OnUpdate, webapp_Text, Instruction, webapp_Instruction, webapp_Form, Tag, webapp_Tag, webapp_Input, webapp_Attribute, webapp_Tr, webapp_Th, webapp_Td, webapp_Field, webapp_TableHTML, webapp_Messages, Behavior, Charset, ColumnType, FormMethod, InputType},
    associations={controller9, appConfig0, webConfig1, library3, view5, model7, resource11, page13, navigation15, table17, image25, file27, businessObject19, validator21, action23, constraint35, propertie29, mapping31, column33, detail37, column47, primaryKey39, unique41, check43, foreignKey45, externalColumn50, onDelete53, onUpdate55, externalTable57, internalColumn60, column63, page66, tag77, properties69, title72, instruction75, businessObject78, attribute81, tr96, th97, td99, action83, label85, buttonValue88, textValue91, validator93, to122, tag101, field104, action107, businessObject111, model113, businessObject116, from119},
    generalizations={gen_webapp_Form_Tag, gen_webapp_Input_Tag, gen_webapp_Text_Instruction, gen_webapp_Tag_Instruction, gen_webapp_Tr_Tag, gen_webapp_TableHTML_Tag, gen_webapp_Messages_Tag, gen_webapp_Td_Tag, gen_webapp_Th_Tag},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)