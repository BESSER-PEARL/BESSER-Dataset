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
AttributeType: Enumeration = Enumeration(
    name="AttributeType",
    literals={
            EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="String")
    }
)

ButtonKind: Enumeration = Enumeration(
    name="ButtonKind",
    literals={
            EnumerationLiteral(name="createEdit"),
			EnumerationLiteral(name="delete"),
			EnumerationLiteral(name="cancel")
    }
)

MultiplicityKind: Enumeration = Enumeration(
    name="MultiplicityKind",
    literals={
            EnumerationLiteral(name="Single"),
			EnumerationLiteral(name="Multiple")
    }
)

# Classes
myDsl01_Reference = Class(name="myDsl01::Reference")
myDsl01_Model = Class(name="myDsl01::Model")
myDsl01_Entity = Class(name="myDsl01::Entity")
myDsl01_Window = Class(name="myDsl01::Window")
myDsl01_Property = Class(name="myDsl01::Property")
myDsl01_Attribute = Class(name="myDsl01::Attribute")
Property_ = Class(name="Property")
myDsl01_Size = Class(name="myDsl01::Size")
myDsl01_ListWindow = Class(name="myDsl01::ListWindow")
Window = Class(name="Window")
myDsl01_EntryWindow = Class(name="myDsl01::EntryWindow")
myDsl01_UIElement = Class(name="myDsl01::UIElement")
myDsl01_Bounds = Class(name="myDsl01::Bounds")
myDsl01_Label = Class(name="myDsl01::Label")
UIElement = Class(name="UIElement")
myDsl01_Field = Class(name="myDsl01::Field")
myDsl01_Button = Class(name="myDsl01::Button")

# myDsl01_Reference class attributes and methods
myDsl01_Reference_multiplicity: Property = Property(name="multiplicity", type=StringType)
myDsl01_Reference.attributes={myDsl01_Reference_multiplicity}

# myDsl01_Model class attributes and methods

# myDsl01_Entity class attributes and methods
myDsl01_Entity_abstract: Property = Property(name="abstract", type=BooleanType)
myDsl01_Entity_name: Property = Property(name="name", type=StringType)
myDsl01_Entity.attributes={myDsl01_Entity_abstract, myDsl01_Entity_name}

# myDsl01_Window class attributes and methods
myDsl01_Window_name: Property = Property(name="name", type=StringType)
myDsl01_Window_title: Property = Property(name="title", type=StringType)
myDsl01_Window.attributes={myDsl01_Window_name, myDsl01_Window_title}

# myDsl01_Property class attributes and methods
myDsl01_Property_name: Property = Property(name="name", type=StringType)
myDsl01_Property.attributes={myDsl01_Property_name}

# myDsl01_Attribute class attributes and methods
myDsl01_Attribute_type: Property = Property(name="type", type=StringType)
myDsl01_Attribute_optional: Property = Property(name="optional", type=BooleanType)
myDsl01_Attribute.attributes={myDsl01_Attribute_type, myDsl01_Attribute_optional}

# Property class attributes and methods

# myDsl01_Size class attributes and methods
myDsl01_Size_width: Property = Property(name="width", type=IntegerType)
myDsl01_Size_height: Property = Property(name="height", type=IntegerType)
myDsl01_Size.attributes={myDsl01_Size_width, myDsl01_Size_height}

# myDsl01_ListWindow class attributes and methods

# Window class attributes and methods

# myDsl01_EntryWindow class attributes and methods

# myDsl01_UIElement class attributes and methods
myDsl01_UIElement_name: Property = Property(name="name", type=StringType)
myDsl01_UIElement.attributes={myDsl01_UIElement_name}

# myDsl01_Bounds class attributes and methods
myDsl01_Bounds_x: Property = Property(name="x", type=IntegerType)
myDsl01_Bounds_y: Property = Property(name="y", type=IntegerType)
myDsl01_Bounds_width: Property = Property(name="width", type=IntegerType)
myDsl01_Bounds_height: Property = Property(name="height", type=IntegerType)
myDsl01_Bounds.attributes={myDsl01_Bounds_y, myDsl01_Bounds_x, myDsl01_Bounds_height, myDsl01_Bounds_width}

# myDsl01_Label class attributes and methods
myDsl01_Label_text: Property = Property(name="text", type=StringType)
myDsl01_Label.attributes={myDsl01_Label_text}

# UIElement class attributes and methods

# myDsl01_Field class attributes and methods

# myDsl01_Button class attributes and methods
myDsl01_Button_kind: Property = Property(name="kind", type=StringType)
myDsl01_Button_text: Property = Property(name="text", type=StringType)
myDsl01_Button.attributes={myDsl01_Button_kind, myDsl01_Button_text}

# Relationships
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="myDsl01_Entity", type=myDsl01_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl01_Model", type=myDsl01_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
windows1: BinaryAssociation = BinaryAssociation(
    name="windows1",
    ends={
        Property(name="myDsl01_Window", type=myDsl01_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl01_Model2", type=myDsl01_Window, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="myDsl01_Entity5", type=myDsl01_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl01_Entity3", type=myDsl01_Entity, multiplicity=Multiplicity(0, 1))
    }
)
properties6: BinaryAssociation = BinaryAssociation(
    name="properties6",
    ends={
        Property(name="myDsl01_Property", type=myDsl01_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl01_Entity7", type=myDsl01_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="myDsl01_Entity9", type=myDsl01_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl01_Reference", type=myDsl01_Entity, multiplicity=Multiplicity(0, 1))
    }
)
opposite11: BinaryAssociation = BinaryAssociation(
    name="opposite11",
    ends={
        Property(name="myDsl01_Reference12", type=myDsl01_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl01_Reference10", type=myDsl01_Reference, multiplicity=Multiplicity(0, 1))
    }
)
entity13: BinaryAssociation = BinaryAssociation(
    name="entity13",
    ends={
        Property(name="myDsl01_Entity15", type=myDsl01_Window, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl01_Window14", type=myDsl01_Entity, multiplicity=Multiplicity(0, 1))
    }
)
size16: BinaryAssociation = BinaryAssociation(
    name="size16",
    ends={
        Property(name="myDsl01_Size", type=myDsl01_Window, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl01_Window17", type=myDsl01_Size, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements18: BinaryAssociation = BinaryAssociation(
    name="elements18",
    ends={
        Property(name="myDsl01_UIElement", type=myDsl01_EntryWindow, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl01_EntryWindow", type=myDsl01_UIElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bounds19: BinaryAssociation = BinaryAssociation(
    name="bounds19",
    ends={
        Property(name="myDsl01_Bounds", type=myDsl01_UIElement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl01_UIElement20", type=myDsl01_Bounds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
property21: BinaryAssociation = BinaryAssociation(
    name="property21",
    ends={
        Property(name="myDsl01_Property22", type=myDsl01_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl01_Field", type=myDsl01_Property, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myDsl01_Attribute_Property = Generalization(general=Property_, specific=myDsl01_Attribute)
gen_myDsl01_Reference_Property = Generalization(general=Property_, specific=myDsl01_Reference)
gen_myDsl01_ListWindow_Window = Generalization(general=Window, specific=myDsl01_ListWindow)
gen_myDsl01_EntryWindow_Window = Generalization(general=Window, specific=myDsl01_EntryWindow)
gen_myDsl01_Label_UIElement = Generalization(general=UIElement, specific=myDsl01_Label)
gen_myDsl01_Field_UIElement = Generalization(general=UIElement, specific=myDsl01_Field)
gen_myDsl01_Button_UIElement = Generalization(general=UIElement, specific=myDsl01_Button)

# Domain Model
domain_model = DomainModel(
    name="myDsl01",
    types={myDsl01_Reference, myDsl01_Model, myDsl01_Entity, myDsl01_Window, myDsl01_Property, myDsl01_Attribute, Property_, myDsl01_Size, myDsl01_ListWindow, Window, myDsl01_EntryWindow, myDsl01_UIElement, myDsl01_Bounds, myDsl01_Label, UIElement, myDsl01_Field, myDsl01_Button, AttributeType, ButtonKind, MultiplicityKind},
    associations={entities0, windows1, superType4, properties6, type8, opposite11, entity13, size16, elements18, bounds19, property21},
    generalizations={gen_myDsl01_Attribute_Property, gen_myDsl01_Reference_Property, gen_myDsl01_ListWindow_Window, gen_myDsl01_EntryWindow_Window, gen_myDsl01_Label_UIElement, gen_myDsl01_Field_UIElement, gen_myDsl01_Button_UIElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)