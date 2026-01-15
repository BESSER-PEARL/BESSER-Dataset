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
entityDsl_Domainmodel = Class(name="entityDsl::Domainmodel")
entityDsl_Entity = Class(name="entityDsl::Entity")
entityDsl_Attribute = Class(name="entityDsl::Attribute")
entityDsl_WinFormControlType = Class(name="entityDsl::WinFormControlType")
entityDsl_Label = Class(name="entityDsl::Label")
entityDsl_DataType = Class(name="entityDsl::DataType")
entityDsl_TextBox = Class(name="entityDsl::TextBox")
entityDsl_TrackBar = Class(name="entityDsl::TrackBar")
WinFormControlType = Class(name="WinFormControlType")
entityDsl_Spinner = Class(name="entityDsl::Spinner")
entityDsl_RadioButtonGroup = Class(name="entityDsl::RadioButtonGroup")
entityDsl_RadioButton = Class(name="entityDsl::RadioButton")
entityDsl_CheckBox = Class(name="entityDsl::CheckBox")
entityDsl_ComboBox = Class(name="entityDsl::ComboBox")
entityDsl_ComboBoxItem = Class(name="entityDsl::ComboBoxItem")

# entityDsl_Domainmodel class attributes and methods
entityDsl_Domainmodel_applicationName: Property = Property(name="applicationName", type=StringType)
entityDsl_Domainmodel.attributes={entityDsl_Domainmodel_applicationName}

# entityDsl_Entity class attributes and methods
entityDsl_Entity_name: Property = Property(name="name", type=StringType)
entityDsl_Entity.attributes={entityDsl_Entity_name}

# entityDsl_Attribute class attributes and methods
entityDsl_Attribute_required: Property = Property(name="required", type=StringType)
entityDsl_Attribute_name: Property = Property(name="name", type=StringType)
entityDsl_Attribute.attributes={entityDsl_Attribute_required, entityDsl_Attribute_name}

# entityDsl_WinFormControlType class attributes and methods
entityDsl_WinFormControlType_name: Property = Property(name="name", type=StringType)
entityDsl_WinFormControlType.attributes={entityDsl_WinFormControlType_name}

# entityDsl_Label class attributes and methods
entityDsl_Label_text: Property = Property(name="text", type=StringType)
entityDsl_Label.attributes={entityDsl_Label_text}

# entityDsl_DataType class attributes and methods
entityDsl_DataType_type: Property = Property(name="type", type=StringType)
entityDsl_DataType.attributes={entityDsl_DataType_type}

# entityDsl_TextBox class attributes and methods
entityDsl_TextBox_minTextLength: Property = Property(name="minTextLength", type=IntegerType)
entityDsl_TextBox_maxTextLength: Property = Property(name="maxTextLength", type=IntegerType)
entityDsl_TextBox_name: Property = Property(name="name", type=StringType)
entityDsl_TextBox.attributes={entityDsl_TextBox_maxTextLength, entityDsl_TextBox_name, entityDsl_TextBox_minTextLength}

# entityDsl_TrackBar class attributes and methods
entityDsl_TrackBar_increment: Property = Property(name="increment", type=IntegerType)
entityDsl_TrackBar_denominator: Property = Property(name="denominator", type=IntegerType)
entityDsl_TrackBar_minimumValue: Property = Property(name="minimumValue", type=IntegerType)
entityDsl_TrackBar_maximumValue: Property = Property(name="maximumValue", type=IntegerType)
entityDsl_TrackBar_stringValues: Property = Property(name="stringValues", type=StringType)
entityDsl_TrackBar_defaultTick: Property = Property(name="defaultTick", type=IntegerType)
entityDsl_TrackBar.attributes={entityDsl_TrackBar_increment, entityDsl_TrackBar_denominator, entityDsl_TrackBar_maximumValue, entityDsl_TrackBar_defaultTick, entityDsl_TrackBar_stringValues, entityDsl_TrackBar_minimumValue}

# WinFormControlType class attributes and methods

# entityDsl_Spinner class attributes and methods
entityDsl_Spinner_defaultValue: Property = Property(name="defaultValue", type=IntegerType)
entityDsl_Spinner_minimumValue: Property = Property(name="minimumValue", type=IntegerType)
entityDsl_Spinner_maximumValue: Property = Property(name="maximumValue", type=IntegerType)
entityDsl_Spinner.attributes={entityDsl_Spinner_defaultValue, entityDsl_Spinner_minimumValue, entityDsl_Spinner_maximumValue}

# entityDsl_RadioButtonGroup class attributes and methods

# entityDsl_RadioButton class attributes and methods
entityDsl_RadioButton_text: Property = Property(name="text", type=StringType)
entityDsl_RadioButton.attributes={entityDsl_RadioButton_text}

# entityDsl_CheckBox class attributes and methods

# entityDsl_ComboBox class attributes and methods

# entityDsl_ComboBoxItem class attributes and methods
entityDsl_ComboBoxItem_text: Property = Property(name="text", type=StringType)
entityDsl_ComboBoxItem.attributes={entityDsl_ComboBoxItem_text}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="entityDsl_Entity", type=entityDsl_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_Domainmodel", type=entityDsl_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="entityDsl_Attribute", type=entityDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_Entity2", type=entityDsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputType3: BinaryAssociation = BinaryAssociation(
    name="inputType3",
    ends={
        Property(name="entityDsl_WinFormControlType", type=entityDsl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_Attribute4", type=entityDsl_WinFormControlType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelText5: BinaryAssociation = BinaryAssociation(
    name="labelText5",
    ends={
        Property(name="entityDsl_Label", type=entityDsl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_Attribute6", type=entityDsl_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
controlType7: BinaryAssociation = BinaryAssociation(
    name="controlType7",
    ends={
        Property(name="entityDsl_TextBox", type=entityDsl_WinFormControlType, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_WinFormControlType8", type=entityDsl_TextBox, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buttons10: BinaryAssociation = BinaryAssociation(
    name="buttons10",
    ends={
        Property(name="entityDsl_RadioButton", type=entityDsl_RadioButtonGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_RadioButtonGroup", type=entityDsl_RadioButton, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType11: BinaryAssociation = BinaryAssociation(
    name="dataType11",
    ends={
        Property(name="entityDsl_DataType13", type=entityDsl_RadioButtonGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_RadioButtonGroup12", type=entityDsl_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataType9: BinaryAssociation = BinaryAssociation(
    name="dataType9",
    ends={
        Property(name="entityDsl_DataType", type=entityDsl_TrackBar, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_TrackBar", type=entityDsl_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataType14: BinaryAssociation = BinaryAssociation(
    name="dataType14",
    ends={
        Property(name="entityDsl_DataType16", type=entityDsl_TextBox, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_TextBox15", type=entityDsl_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
items17: BinaryAssociation = BinaryAssociation(
    name="items17",
    ends={
        Property(name="entityDsl_ComboBoxItem", type=entityDsl_ComboBox, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_ComboBox", type=entityDsl_ComboBoxItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType18: BinaryAssociation = BinaryAssociation(
    name="dataType18",
    ends={
        Property(name="entityDsl_DataType20", type=entityDsl_ComboBox, multiplicity=Multiplicity(1, 1)),
        Property(name="entityDsl_ComboBox19", type=entityDsl_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_entityDsl_TrackBar_WinFormControlType = Generalization(general=WinFormControlType, specific=entityDsl_TrackBar)
gen_entityDsl_Spinner_WinFormControlType = Generalization(general=WinFormControlType, specific=entityDsl_Spinner)
gen_entityDsl_RadioButtonGroup_WinFormControlType = Generalization(general=WinFormControlType, specific=entityDsl_RadioButtonGroup)
gen_entityDsl_ComboBox_WinFormControlType = Generalization(general=WinFormControlType, specific=entityDsl_ComboBox)
gen_entityDsl_CheckBox_WinFormControlType = Generalization(general=WinFormControlType, specific=entityDsl_CheckBox)

# Domain Model
domain_model = DomainModel(
    name="entityDsl",
    types={entityDsl_Domainmodel, entityDsl_Entity, entityDsl_Attribute, entityDsl_WinFormControlType, entityDsl_Label, entityDsl_DataType, entityDsl_TextBox, entityDsl_TrackBar, WinFormControlType, entityDsl_Spinner, entityDsl_RadioButtonGroup, entityDsl_RadioButton, entityDsl_CheckBox, entityDsl_ComboBox, entityDsl_ComboBoxItem},
    associations={elements0, attributes1, inputType3, labelText5, controlType7, buttons10, dataType11, dataType9, dataType14, items17, dataType18},
    generalizations={gen_entityDsl_TrackBar_WinFormControlType, gen_entityDsl_Spinner_WinFormControlType, gen_entityDsl_RadioButtonGroup_WinFormControlType, gen_entityDsl_ComboBox_WinFormControlType, gen_entityDsl_CheckBox_WinFormControlType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)