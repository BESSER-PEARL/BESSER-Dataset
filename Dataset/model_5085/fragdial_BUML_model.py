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
fragdial_Binding = Class(name="fragdial::Binding")
fragdial_AbstractComponent = Class(name="fragdial::AbstractComponent", is_abstract=True)
fragdial_Content = Class(name="fragdial::Content")
fragdial_Attributes = Class(name="fragdial::Attributes")
fragdial_Output = Class(name="fragdial::Output")
fragdial_Controller = Class(name="fragdial::Controller")
fragdial_Required = Class(name="fragdial::Required")
fragdial_Provided = Class(name="fragdial::Provided")
fragdial_Interface = Class(name="fragdial::Interface", is_abstract=True)
fragdial_Component = Class(name="fragdial::Component")
AbstractComponent = Class(name="AbstractComponent")
fragdial_Component1 = Class(name="fragdial::Component1")
fragdial_Include = Class(name="fragdial::Include")
fragdial_Ldflag = Class(name="fragdial::Ldflag")
fragdial_Attribute = Class(name="fragdial::Attribute")
Interface = Class(name="Interface")
fragdial_Component2 = Class(name="fragdial::Component2")
fragdial_Component3 = Class(name="fragdial::Component3")

# fragdial_Binding class attributes and methods

# fragdial_AbstractComponent class attributes and methods
fragdial_AbstractComponent_name: Property = Property(name="name", type=StringType)
fragdial_AbstractComponent.attributes={fragdial_AbstractComponent_name}

# fragdial_Content class attributes and methods
fragdial_Content_class: Property = Property(name="class", type=StringType)
fragdial_Content_language: Property = Property(name="language", type=StringType)
fragdial_Content.attributes={fragdial_Content_class, fragdial_Content_language}

# fragdial_Attributes class attributes and methods
fragdial_Attributes_signature: Property = Property(name="signature", type=StringType)
fragdial_Attributes.attributes={fragdial_Attributes_signature}

# fragdial_Output class attributes and methods
fragdial_Output_format: Property = Property(name="format", type=StringType)
fragdial_Output.attributes={fragdial_Output_format}

# fragdial_Controller class attributes and methods
fragdial_Controller_language: Property = Property(name="language", type=StringType)
fragdial_Controller_descriptor: Property = Property(name="descriptor", type=StringType)
fragdial_Controller.attributes={fragdial_Controller_language, fragdial_Controller_descriptor}

# fragdial_Required class attributes and methods

# fragdial_Provided class attributes and methods

# fragdial_Interface class attributes and methods
fragdial_Interface_name: Property = Property(name="name", type=StringType)
fragdial_Interface_signature: Property = Property(name="signature", type=StringType)
fragdial_Interface_contingency: Property = Property(name="contingency", type=StringType)
fragdial_Interface_cardinality: Property = Property(name="cardinality", type=StringType)
fragdial_Interface_startProperty: Property = Property(name="startProperty", type=StringType)
fragdial_Interface.attributes={fragdial_Interface_startProperty, fragdial_Interface_cardinality, fragdial_Interface_name, fragdial_Interface_contingency, fragdial_Interface_signature}

# fragdial_Component class attributes and methods

# AbstractComponent class attributes and methods

# fragdial_Component1 class attributes and methods

# fragdial_Include class attributes and methods
fragdial_Include_file: Property = Property(name="file", type=StringType)
fragdial_Include.attributes={fragdial_Include_file}

# fragdial_Ldflag class attributes and methods
fragdial_Ldflag_value: Property = Property(name="value", type=StringType)
fragdial_Ldflag.attributes={fragdial_Ldflag_value}

# fragdial_Attribute class attributes and methods
fragdial_Attribute_name: Property = Property(name="name", type=StringType)
fragdial_Attribute_value: Property = Property(name="value", type=StringType)
fragdial_Attribute.attributes={fragdial_Attribute_value, fragdial_Attribute_name}

# Interface class attributes and methods

# fragdial_Component2 class attributes and methods

# fragdial_Component3 class attributes and methods

# Relationships
bindings11: BinaryAssociation = BinaryAssociation(
    name="bindings11",
    ends={
        Property(name="fragdial_Binding", type=fragdial_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_Interface", type=fragdial_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="fragdial_Content", type=fragdial_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_AbstractComponent", type=fragdial_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="fragdial_Attributes", type=fragdial_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_AbstractComponent2", type=fragdial_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output3: BinaryAssociation = BinaryAssociation(
    name="output3",
    ends={
        Property(name="fragdial_Output", type=fragdial_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_AbstractComponent4", type=fragdial_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
controller5: BinaryAssociation = BinaryAssociation(
    name="controller5",
    ends={
        Property(name="fragdial_Controller", type=fragdial_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_AbstractComponent6", type=fragdial_Controller, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredInterfaces7: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces7",
    ends={
        Property(name="fragdial_Required", type=fragdial_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_AbstractComponent8", type=fragdial_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces9: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces9",
    ends={
        Property(name="fragdial_Provided", type=fragdial_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_AbstractComponent10", type=fragdial_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedComponents127: BinaryAssociation = BinaryAssociation(
    name="nestedComponents127",
    ends={
        Property(name="fragdial_Component1", type=fragdial_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_Component", type=fragdial_Component1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subComponents29: BinaryAssociation = BinaryAssociation(
    name="subComponents29",
    ends={
        Property(name="fragdial_Component30", type=fragdial_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_Component28", type=fragdial_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from12: BinaryAssociation = BinaryAssociation(
    name="from12",
    ends={
        Property(name="fragdial_Interface14", type=fragdial_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_Binding13", type=fragdial_Interface, multiplicity=Multiplicity(0, 1))
    }
)
to15: BinaryAssociation = BinaryAssociation(
    name="to15",
    ends={
        Property(name="fragdial_Interface17", type=fragdial_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_Binding16", type=fragdial_Interface, multiplicity=Multiplicity(0, 1))
    }
)
contentParent18: BinaryAssociation = BinaryAssociation(
    name="contentParent18",
    ends={
        Property(name="fragdial_AbstractComponent20", type=fragdial_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_Content19", type=fragdial_AbstractComponent, multiplicity=Multiplicity(1, 1))
    }
)
includes21: BinaryAssociation = BinaryAssociation(
    name="includes21",
    ends={
        Property(name="fragdial_Include", type=fragdial_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_Content22", type=fragdial_Include, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ldflags23: BinaryAssociation = BinaryAssociation(
    name="ldflags23",
    ends={
        Property(name="fragdial_Ldflag", type=fragdial_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_Content24", type=fragdial_Ldflag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes25: BinaryAssociation = BinaryAssociation(
    name="attributes25",
    ends={
        Property(name="fragdial_Attribute", type=fragdial_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_Attributes26", type=fragdial_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedComponents231: BinaryAssociation = BinaryAssociation(
    name="nestedComponents231",
    ends={
        Property(name="fragdial_Component2", type=fragdial_Component1, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_Component132", type=fragdial_Component2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedComponents333: BinaryAssociation = BinaryAssociation(
    name="nestedComponents333",
    ends={
        Property(name="fragdial_Component3", type=fragdial_Component2, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial_Component234", type=fragdial_Component3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fragdial_Provided_Interface = Generalization(general=Interface, specific=fragdial_Provided)
gen_fragdial_Component_AbstractComponent = Generalization(general=AbstractComponent, specific=fragdial_Component)
gen_fragdial_Component1_AbstractComponent = Generalization(general=AbstractComponent, specific=fragdial_Component1)
gen_fragdial_Required_Interface = Generalization(general=Interface, specific=fragdial_Required)
gen_fragdial_Component2_AbstractComponent = Generalization(general=AbstractComponent, specific=fragdial_Component2)
gen_fragdial_Component3_AbstractComponent = Generalization(general=AbstractComponent, specific=fragdial_Component3)

# Domain Model
domain_model = DomainModel(
    name="fragdial",
    types={fragdial_Binding, fragdial_AbstractComponent, fragdial_Content, fragdial_Attributes, fragdial_Output, fragdial_Controller, fragdial_Required, fragdial_Provided, fragdial_Interface, fragdial_Component, AbstractComponent, fragdial_Component1, fragdial_Include, fragdial_Ldflag, fragdial_Attribute, Interface, fragdial_Component2, fragdial_Component3},
    associations={bindings11, content0, attributes1, output3, controller5, requiredInterfaces7, providedInterfaces9, nestedComponents127, subComponents29, from12, to15, contentParent18, includes21, ldflags23, attributes25, nestedComponents231, nestedComponents333},
    generalizations={gen_fragdial_Provided_Interface, gen_fragdial_Component_AbstractComponent, gen_fragdial_Component1_AbstractComponent, gen_fragdial_Required_Interface, gen_fragdial_Component2_AbstractComponent, gen_fragdial_Component3_AbstractComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)