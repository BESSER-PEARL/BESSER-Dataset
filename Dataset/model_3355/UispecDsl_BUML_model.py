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
uispecDsl_Form = Class(name="uispecDsl::Form")
uispecDsl_EntityReference = Class(name="uispecDsl::EntityReference")
uispecDsl_Field = Class(name="uispecDsl::Field")
uispecDsl_Entity = Class(name="uispecDsl::Entity")
uispecDsl_Widget = Class(name="uispecDsl::Widget")
uispecDsl_Attribute = Class(name="uispecDsl::Attribute")
uispecDsl_TextFieldWidget = Class(name="uispecDsl::TextFieldWidget")
Widget = Class(name="Widget")
uispecDsl_CheckBoxWidget = Class(name="uispecDsl::CheckBoxWidget")
uispecDsl_ComboWidget = Class(name="uispecDsl::ComboWidget")

# uispecDsl_Form class attributes and methods
uispecDsl_Form_name: Property = Property(name="name", type=StringType)
uispecDsl_Form.attributes={uispecDsl_Form_name}

# uispecDsl_EntityReference class attributes and methods

# uispecDsl_Field class attributes and methods
uispecDsl_Field_label: Property = Property(name="label", type=StringType)
uispecDsl_Field.attributes={uispecDsl_Field_label}

# uispecDsl_Entity class attributes and methods

# uispecDsl_Widget class attributes and methods

# uispecDsl_Attribute class attributes and methods

# uispecDsl_TextFieldWidget class attributes and methods
uispecDsl_TextFieldWidget_length: Property = Property(name="length", type=IntegerType)
uispecDsl_TextFieldWidget.attributes={uispecDsl_TextFieldWidget_length}

# Widget class attributes and methods

# uispecDsl_CheckBoxWidget class attributes and methods

# uispecDsl_ComboWidget class attributes and methods
uispecDsl_ComboWidget_values: Property = Property(name="values", type=StringType)
uispecDsl_ComboWidget.attributes={uispecDsl_ComboWidget_values}

# Relationships
usedEntities0: BinaryAssociation = BinaryAssociation(
    name="usedEntities0",
    ends={
        Property(name="uispecDsl_EntityReference", type=uispecDsl_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="uispecDsl_Form", type=uispecDsl_EntityReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields1: BinaryAssociation = BinaryAssociation(
    name="fields1",
    ends={
        Property(name="uispecDsl_Field", type=uispecDsl_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="uispecDsl_Form2", type=uispecDsl_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity3: BinaryAssociation = BinaryAssociation(
    name="entity3",
    ends={
        Property(name="uispecDsl_Entity", type=uispecDsl_EntityReference, multiplicity=Multiplicity(1, 1)),
        Property(name="uispecDsl_EntityReference4", type=uispecDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
widget5: BinaryAssociation = BinaryAssociation(
    name="widget5",
    ends={
        Property(name="uispecDsl_Widget", type=uispecDsl_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="uispecDsl_Field6", type=uispecDsl_Widget, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute7: BinaryAssociation = BinaryAssociation(
    name="attribute7",
    ends={
        Property(name="uispecDsl_Attribute", type=uispecDsl_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="uispecDsl_Field8", type=uispecDsl_Attribute, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_uispecDsl_TextFieldWidget_Widget = Generalization(general=Widget, specific=uispecDsl_TextFieldWidget)
gen_uispecDsl_CheckBoxWidget_Widget = Generalization(general=Widget, specific=uispecDsl_CheckBoxWidget)
gen_uispecDsl_ComboWidget_Widget = Generalization(general=Widget, specific=uispecDsl_ComboWidget)

# Domain Model
domain_model = DomainModel(
    name="uispecDsl",
    types={uispecDsl_Form, uispecDsl_EntityReference, uispecDsl_Field, uispecDsl_Entity, uispecDsl_Widget, uispecDsl_Attribute, uispecDsl_TextFieldWidget, Widget, uispecDsl_CheckBoxWidget, uispecDsl_ComboWidget},
    associations={usedEntities0, fields1, entity3, widget5, attribute7},
    generalizations={gen_uispecDsl_TextFieldWidget_Widget, gen_uispecDsl_CheckBoxWidget_Widget, gen_uispecDsl_ComboWidget_Widget},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)