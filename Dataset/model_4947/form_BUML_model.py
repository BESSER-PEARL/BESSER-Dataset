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
form_Formulario = Class(name="form::Formulario")
form_Element = Class(name="form::Element", is_abstract=True)
form_Orden = Class(name="form::Orden")
form_textArea = Class(name="form::textArea")
form_Label = Class(name="form::Label")
Element = Class(name="Element")
form_Editable = Class(name="form::Editable")
form_Input = Class(name="form::Input")
Editable = Class(name="Editable")
form_SelectionList = Class(name="form::SelectionList")
form_option = Class(name="form::option")

# form_Formulario class attributes and methods

# form_Element class attributes and methods

# form_Orden class attributes and methods

# form_textArea class attributes and methods
form_textArea_content: Property = Property(name="content", type=StringType)
form_textArea.attributes={form_textArea_content}

# form_Label class attributes and methods
form_Label_content: Property = Property(name="content", type=StringType)
form_Label_for: Property = Property(name="for", type=StringType)
form_Label.attributes={form_Label_content, form_Label_for}

# Element class attributes and methods

# form_Editable class attributes and methods
form_Editable_disabled: Property = Property(name="disabled", type=BooleanType)
form_Editable_name: Property = Property(name="name", type=StringType)
form_Editable.attributes={form_Editable_disabled, form_Editable_name}

# form_Input class attributes and methods
form_Input_checked: Property = Property(name="checked", type=BooleanType)
form_Input_type: Property = Property(name="type", type=StringType)
form_Input_value: Property = Property(name="value", type=StringType)
form_Input.attributes={form_Input_type, form_Input_value, form_Input_checked}

# Editable class attributes and methods

# form_SelectionList class attributes and methods
form_SelectionList_multiple: Property = Property(name="multiple", type=BooleanType)
form_SelectionList.attributes={form_SelectionList_multiple}

# form_option class attributes and methods
form_option_content: Property = Property(name="content", type=StringType)
form_option_value: Property = Property(name="value", type=StringType)
form_option.attributes={form_option_content, form_option_value}

# Relationships
hasElement0: BinaryAssociation = BinaryAssociation(
    name="hasElement0",
    ends={
        Property(name="form_Element", type=form_Formulario, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Formulario", type=form_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orden1: BinaryAssociation = BinaryAssociation(
    name="orden1",
    ends={
        Property(name="form_Orden", type=form_Formulario, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Formulario2", type=form_Orden, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasLabel3: BinaryAssociation = BinaryAssociation(
    name="hasLabel3",
    ends={
        Property(name="form_Label", type=form_Editable, multiplicity=Multiplicity(1, 1)),
        Property(name="form_Editable", type=form_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hasOption4: BinaryAssociation = BinaryAssociation(
    name="hasOption4",
    ends={
        Property(name="form_option", type=form_SelectionList, multiplicity=Multiplicity(1, 1)),
        Property(name="form_SelectionList", type=form_option, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
origen5: BinaryAssociation = BinaryAssociation(
    name="origen5",
    ends={
        Property(name="Element", type=form_Orden, multiplicity=Multiplicity(1, 1)),
        Property(name="salientes", type=form_Element, multiplicity=Multiplicity(1, 1))
    }
)
destino6: BinaryAssociation = BinaryAssociation(
    name="destino6",
    ends={
        Property(name="Element7", type=form_Orden, multiplicity=Multiplicity(1, 1)),
        Property(name="entrantes", type=form_Element, multiplicity=Multiplicity(1, 1))
    }
)
salientes8: BinaryAssociation = BinaryAssociation(
    name="salientes8",
    ends={
        Property(name="Orden", type=form_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="origen", type=form_Orden, multiplicity=Multiplicity(0, 1))
    }
)
entrantes9: BinaryAssociation = BinaryAssociation(
    name="entrantes9",
    ends={
        Property(name="Orden10", type=form_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="destino", type=form_Orden, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_form_textArea_Editable = Generalization(general=Editable, specific=form_textArea)
gen_form_Label_Element = Generalization(general=Element, specific=form_Label)
gen_form_Editable_Element = Generalization(general=Element, specific=form_Editable)
gen_form_Input_Editable = Generalization(general=Editable, specific=form_Input)
gen_form_SelectionList_Editable = Generalization(general=Editable, specific=form_SelectionList)

# Domain Model
domain_model = DomainModel(
    name="form",
    types={form_Formulario, form_Element, form_Orden, form_textArea, form_Label, Element, form_Editable, form_Input, Editable, form_SelectionList, form_option},
    associations={hasElement0, orden1, hasLabel3, hasOption4, origen5, destino6, salientes8, entrantes9},
    generalizations={gen_form_textArea_Editable, gen_form_Label_Element, gen_form_Editable_Element, gen_form_Input_Editable, gen_form_SelectionList_Editable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)