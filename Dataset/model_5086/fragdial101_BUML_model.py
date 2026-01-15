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
fragdial101_AbstractComponent = Class(name="fragdial101::AbstractComponent", is_abstract=True)
fragdial101_Content = Class(name="fragdial101::Content")
fragdial101_Attributes = Class(name="fragdial101::Attributes")
fragdial101_Output = Class(name="fragdial101::Output")
fragdial101_Controller = Class(name="fragdial101::Controller")
fragdial101_Required = Class(name="fragdial101::Required")
fragdial101_Provided = Class(name="fragdial101::Provided")
fragdial101_Interface = Class(name="fragdial101::Interface", is_abstract=True)
fragdial101_Binding = Class(name="fragdial101::Binding")
fragdial101_Include = Class(name="fragdial101::Include")
fragdial101_Ldflag = Class(name="fragdial101::Ldflag")
Interface = Class(name="Interface")
fragdial101_Component = Class(name="fragdial101::Component")
AbstractComponent = Class(name="AbstractComponent")
fragdial101_Attribute = Class(name="fragdial101::Attribute")

# fragdial101_AbstractComponent class attributes and methods
fragdial101_AbstractComponent_name: Property = Property(name="name", type=StringType)
fragdial101_AbstractComponent.attributes={fragdial101_AbstractComponent_name}

# fragdial101_Content class attributes and methods
fragdial101_Content_class: Property = Property(name="class", type=StringType)
fragdial101_Content_language: Property = Property(name="language", type=StringType)
fragdial101_Content.attributes={fragdial101_Content_class, fragdial101_Content_language}

# fragdial101_Attributes class attributes and methods
fragdial101_Attributes_signature: Property = Property(name="signature", type=StringType)
fragdial101_Attributes.attributes={fragdial101_Attributes_signature}

# fragdial101_Output class attributes and methods
fragdial101_Output_format: Property = Property(name="format", type=StringType)
fragdial101_Output.attributes={fragdial101_Output_format}

# fragdial101_Controller class attributes and methods
fragdial101_Controller_language: Property = Property(name="language", type=StringType)
fragdial101_Controller_descriptor: Property = Property(name="descriptor", type=StringType)
fragdial101_Controller.attributes={fragdial101_Controller_descriptor, fragdial101_Controller_language}

# fragdial101_Required class attributes and methods

# fragdial101_Provided class attributes and methods

# fragdial101_Interface class attributes and methods
fragdial101_Interface_name: Property = Property(name="name", type=StringType)
fragdial101_Interface_signature: Property = Property(name="signature", type=StringType)
fragdial101_Interface_contingency: Property = Property(name="contingency", type=StringType)
fragdial101_Interface_cardinality: Property = Property(name="cardinality", type=StringType)
fragdial101_Interface_startProperty: Property = Property(name="startProperty", type=StringType)
fragdial101_Interface.attributes={fragdial101_Interface_signature, fragdial101_Interface_name, fragdial101_Interface_startProperty, fragdial101_Interface_contingency, fragdial101_Interface_cardinality}

# fragdial101_Binding class attributes and methods

# fragdial101_Include class attributes and methods
fragdial101_Include_file: Property = Property(name="file", type=StringType)
fragdial101_Include.attributes={fragdial101_Include_file}

# fragdial101_Ldflag class attributes and methods
fragdial101_Ldflag_value: Property = Property(name="value", type=StringType)
fragdial101_Ldflag.attributes={fragdial101_Ldflag_value}

# Interface class attributes and methods

# fragdial101_Component class attributes and methods

# AbstractComponent class attributes and methods

# fragdial101_Attribute class attributes and methods
fragdial101_Attribute_name: Property = Property(name="name", type=StringType)
fragdial101_Attribute_value: Property = Property(name="value", type=StringType)
fragdial101_Attribute.attributes={fragdial101_Attribute_name, fragdial101_Attribute_value}

# Relationships
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="fragdial101_Attributes", type=fragdial101_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_AbstractComponent2", type=fragdial101_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output3: BinaryAssociation = BinaryAssociation(
    name="output3",
    ends={
        Property(name="fragdial101_Output", type=fragdial101_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_AbstractComponent4", type=fragdial101_Output, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
controller5: BinaryAssociation = BinaryAssociation(
    name="controller5",
    ends={
        Property(name="fragdial101_Controller", type=fragdial101_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_AbstractComponent6", type=fragdial101_Controller, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredInterfaces7: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces7",
    ends={
        Property(name="fragdial101_Required", type=fragdial101_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_AbstractComponent8", type=fragdial101_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces9: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces9",
    ends={
        Property(name="fragdial101_Provided", type=fragdial101_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_AbstractComponent10", type=fragdial101_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings11: BinaryAssociation = BinaryAssociation(
    name="bindings11",
    ends={
        Property(name="fragdial101_Binding", type=fragdial101_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_Interface", type=fragdial101_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from12: BinaryAssociation = BinaryAssociation(
    name="from12",
    ends={
        Property(name="fragdial101_Interface14", type=fragdial101_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_Binding13", type=fragdial101_Interface, multiplicity=Multiplicity(0, 1))
    }
)
to15: BinaryAssociation = BinaryAssociation(
    name="to15",
    ends={
        Property(name="fragdial101_Interface17", type=fragdial101_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_Binding16", type=fragdial101_Interface, multiplicity=Multiplicity(0, 1))
    }
)
contentParent18: BinaryAssociation = BinaryAssociation(
    name="contentParent18",
    ends={
        Property(name="fragdial101_AbstractComponent20", type=fragdial101_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_Content19", type=fragdial101_AbstractComponent, multiplicity=Multiplicity(1, 1))
    }
)
includes21: BinaryAssociation = BinaryAssociation(
    name="includes21",
    ends={
        Property(name="fragdial101_Include", type=fragdial101_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_Content22", type=fragdial101_Include, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ldflags23: BinaryAssociation = BinaryAssociation(
    name="ldflags23",
    ends={
        Property(name="fragdial101_Ldflag", type=fragdial101_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_Content24", type=fragdial101_Ldflag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="fragdial101_Content", type=fragdial101_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_AbstractComponent", type=fragdial101_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes25: BinaryAssociation = BinaryAssociation(
    name="attributes25",
    ends={
        Property(name="fragdial101_Attributes26", type=fragdial101_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="fragdial101_Attribute", type=fragdial101_Attributes, multiplicity=Multiplicity(1, 1))
    }
)
subComponents28: BinaryAssociation = BinaryAssociation(
    name="subComponents28",
    ends={
        Property(name="fragdial101_Component", type=fragdial101_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="fragdial101_Component27", type=fragdial101_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fragdial101_Required_Interface = Generalization(general=Interface, specific=fragdial101_Required)
gen_fragdial101_Provided_Interface = Generalization(general=Interface, specific=fragdial101_Provided)
gen_fragdial101_Component_AbstractComponent = Generalization(general=AbstractComponent, specific=fragdial101_Component)

# Domain Model
domain_model = DomainModel(
    name="fragdial101",
    types={fragdial101_AbstractComponent, fragdial101_Content, fragdial101_Attributes, fragdial101_Output, fragdial101_Controller, fragdial101_Required, fragdial101_Provided, fragdial101_Interface, fragdial101_Binding, fragdial101_Include, fragdial101_Ldflag, Interface, fragdial101_Component, AbstractComponent, fragdial101_Attribute},
    associations={attributes1, output3, controller5, requiredInterfaces7, providedInterfaces9, bindings11, from12, to15, contentParent18, includes21, ldflags23, content0, attributes25, subComponents28},
    generalizations={gen_fragdial101_Required_Interface, gen_fragdial101_Provided_Interface, gen_fragdial101_Component_AbstractComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)