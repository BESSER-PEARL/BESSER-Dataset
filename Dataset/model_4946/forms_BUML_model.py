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
forms_Form = Class(name="forms::Form")
forms_Group = Class(name="forms::Group")
forms_Item = Class(name="forms::Item")
forms_ItemType = Class(name="forms::ItemType", is_abstract=True)
forms_Option = Class(name="forms::Option")
forms_FreeText = Class(name="forms::FreeText")
ItemType = Class(name="ItemType")
forms_Choice = Class(name="forms::Choice")
forms_Date = Class(name="forms::Date")
forms_Number = Class(name="forms::Number")
forms_Decision = Class(name="forms::Decision")

# forms_Form class attributes and methods
forms_Form_caption: Property = Property(name="caption", type=StringType)
forms_Form.attributes={forms_Form_caption}

# forms_Group class attributes and methods
forms_Group_name: Property = Property(name="name", type=StringType)
forms_Group.attributes={forms_Group_name}

# forms_Item class attributes and methods
forms_Item_text: Property = Property(name="text", type=StringType)
forms_Item_explanation: Property = Property(name="explanation", type=StringType)
forms_Item.attributes={forms_Item_explanation, forms_Item_text}

# forms_ItemType class attributes and methods

# forms_Option class attributes and methods
forms_Option_id: Property = Property(name="id", type=StringType)
forms_Option_text: Property = Property(name="text", type=StringType)
forms_Option.attributes={forms_Option_id, forms_Option_text}

# forms_FreeText class attributes and methods

# ItemType class attributes and methods

# forms_Choice class attributes and methods
forms_Choice_multiple: Property = Property(name="multiple", type=BooleanType)
forms_Choice.attributes={forms_Choice_multiple}

# forms_Date class attributes and methods

# forms_Number class attributes and methods

# forms_Decision class attributes and methods

# Relationships
groups0: BinaryAssociation = BinaryAssociation(
    name="groups0",
    ends={
        Property(name="forms_Group", type=forms_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Form", type=forms_Group, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
itemType1: BinaryAssociation = BinaryAssociation(
    name="itemType1",
    ends={
        Property(name="forms_ItemType", type=forms_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Item", type=forms_ItemType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dependentOf2: BinaryAssociation = BinaryAssociation(
    name="dependentOf2",
    ends={
        Property(name="forms_Option", type=forms_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Item3", type=forms_Option, multiplicity=Multiplicity(0, 9999))
    }
)
options4: BinaryAssociation = BinaryAssociation(
    name="options4",
    ends={
        Property(name="forms_Option5", type=forms_Choice, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Choice", type=forms_Option, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
items6: BinaryAssociation = BinaryAssociation(
    name="items6",
    ends={
        Property(name="forms_Item8", type=forms_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Group7", type=forms_Item, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
options9: BinaryAssociation = BinaryAssociation(
    name="options9",
    ends={
        Property(name="forms_Option10", type=forms_Decision, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Decision", type=forms_Option, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)

# Generalizations
gen_forms_FreeText_ItemType = Generalization(general=ItemType, specific=forms_FreeText)
gen_forms_Choice_ItemType = Generalization(general=ItemType, specific=forms_Choice)
gen_forms_Date_ItemType = Generalization(general=ItemType, specific=forms_Date)
gen_forms_Number_ItemType = Generalization(general=ItemType, specific=forms_Number)
gen_forms_Decision_ItemType = Generalization(general=ItemType, specific=forms_Decision)

# Domain Model
domain_model = DomainModel(
    name="forms",
    types={forms_Form, forms_Group, forms_Item, forms_ItemType, forms_Option, forms_FreeText, ItemType, forms_Choice, forms_Date, forms_Number, forms_Decision},
    associations={groups0, itemType1, dependentOf2, options4, items6, options9},
    generalizations={gen_forms_FreeText_ItemType, gen_forms_Choice_ItemType, gen_forms_Date_ItemType, gen_forms_Number_ItemType, gen_forms_Decision_ItemType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)