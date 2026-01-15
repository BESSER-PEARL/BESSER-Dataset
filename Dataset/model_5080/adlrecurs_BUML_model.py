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
adlrecurs_Provided = Class(name="adlrecurs::Provided")
adlrecurs_Interface = Class(name="adlrecurs::Interface", is_abstract=True)
NamedElement = Class(name="NamedElement")
adlrecurs_Binding = Class(name="adlrecurs::Binding")
adlrecurs_AbstractComponent = Class(name="adlrecurs::AbstractComponent", is_abstract=True)
adlrecurs_Content = Class(name="adlrecurs::Content")
adlrecurs_Attributes = Class(name="adlrecurs::Attributes")
adlrecurs_Required = Class(name="adlrecurs::Required")
adlrecurs_NamedElement = Class(name="adlrecurs::NamedElement", is_abstract=True)
adlrecurs_Type = Class(name="adlrecurs::Type", is_abstract=True)
Interface = Class(name="Interface")
adlrecurs_Item = Class(name="adlrecurs::Item")
adlrecurs_Attribute = Class(name="adlrecurs::Attribute")
Type = Class(name="Type")
adlrecurs_Component = Class(name="adlrecurs::Component")
AbstractComponent = Class(name="AbstractComponent")

# adlrecurs_Provided class attributes and methods

# adlrecurs_Interface class attributes and methods

# NamedElement class attributes and methods

# adlrecurs_Binding class attributes and methods

# adlrecurs_AbstractComponent class attributes and methods

# adlrecurs_Content class attributes and methods
adlrecurs_Content_class: Property = Property(name="class", type=StringType)
adlrecurs_Content_language: Property = Property(name="language", type=StringType)
adlrecurs_Content.attributes={adlrecurs_Content_language, adlrecurs_Content_class}

# adlrecurs_Attributes class attributes and methods
adlrecurs_Attributes_signature: Property = Property(name="signature", type=StringType)
adlrecurs_Attributes.attributes={adlrecurs_Attributes_signature}

# adlrecurs_Required class attributes and methods

# adlrecurs_NamedElement class attributes and methods
adlrecurs_NamedElement_name: Property = Property(name="name", type=StringType)
adlrecurs_NamedElement.attributes={adlrecurs_NamedElement_name}

# adlrecurs_Type class attributes and methods
adlrecurs_Type_signature: Property = Property(name="signature", type=StringType)
adlrecurs_Type.attributes={adlrecurs_Type_signature}

# Interface class attributes and methods

# adlrecurs_Item class attributes and methods

# adlrecurs_Attribute class attributes and methods
adlrecurs_Attribute_name: Property = Property(name="name", type=StringType)
adlrecurs_Attribute_value: Property = Property(name="value", type=StringType)
adlrecurs_Attribute.attributes={adlrecurs_Attribute_name, adlrecurs_Attribute_value}

# Type class attributes and methods

# adlrecurs_Component class attributes and methods

# AbstractComponent class attributes and methods

# Relationships
providedInterfaces5: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces5",
    ends={
        Property(name="adlrecurs_Provided", type=adlrecurs_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecurs_AbstractComponent6", type=adlrecurs_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings7: BinaryAssociation = BinaryAssociation(
    name="bindings7",
    ends={
        Property(name="adlrecurs_Binding", type=adlrecurs_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecurs_Interface", type=adlrecurs_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from8: BinaryAssociation = BinaryAssociation(
    name="from8",
    ends={
        Property(name="adlrecurs_Interface10", type=adlrecurs_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecurs_Binding9", type=adlrecurs_Interface, multiplicity=Multiplicity(0, 1))
    }
)
to11: BinaryAssociation = BinaryAssociation(
    name="to11",
    ends={
        Property(name="adlrecurs_Interface13", type=adlrecurs_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecurs_Binding12", type=adlrecurs_Interface, multiplicity=Multiplicity(0, 1))
    }
)
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="adlrecurs_Content", type=adlrecurs_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecurs_AbstractComponent", type=adlrecurs_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="adlrecurs_Attributes", type=adlrecurs_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecurs_AbstractComponent2", type=adlrecurs_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredInterfaces3: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces3",
    ends={
        Property(name="adlrecurs_Required", type=adlrecurs_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecurs_AbstractComponent4", type=adlrecurs_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subComponents17: BinaryAssociation = BinaryAssociation(
    name="subComponents17",
    ends={
        Property(name="adlrecurs_Component", type=adlrecurs_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecurs_Component16", type=adlrecurs_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items18: BinaryAssociation = BinaryAssociation(
    name="items18",
    ends={
        Property(name="adlrecurs_Item", type=adlrecurs_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecurs_Type", type=adlrecurs_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes14: BinaryAssociation = BinaryAssociation(
    name="attributes14",
    ends={
        Property(name="adlrecurs_Attribute", type=adlrecurs_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecurs_Attributes15", type=adlrecurs_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_adlrecurs_Interface_NamedElement = Generalization(general=NamedElement, specific=adlrecurs_Interface)
gen_adlrecurs_Binding_NamedElement = Generalization(general=NamedElement, specific=adlrecurs_Binding)
gen_adlrecurs_Type_Interface = Generalization(general=Interface, specific=adlrecurs_Type)
gen_adlrecurs_Item_NamedElement = Generalization(general=NamedElement, specific=adlrecurs_Item)
gen_adlrecurs_Required_Type = Generalization(general=Type, specific=adlrecurs_Required)
gen_adlrecurs_Provided_Type = Generalization(general=Type, specific=adlrecurs_Provided)
gen_adlrecurs_Component_AbstractComponent = Generalization(general=AbstractComponent, specific=adlrecurs_Component)
gen_adlrecurs_Component_NamedElement = Generalization(general=NamedElement, specific=adlrecurs_Component)

# Domain Model
domain_model = DomainModel(
    name="adlrecurs",
    types={adlrecurs_Provided, adlrecurs_Interface, NamedElement, adlrecurs_Binding, adlrecurs_AbstractComponent, adlrecurs_Content, adlrecurs_Attributes, adlrecurs_Required, adlrecurs_NamedElement, adlrecurs_Type, Interface, adlrecurs_Item, adlrecurs_Attribute, Type, adlrecurs_Component, AbstractComponent},
    associations={providedInterfaces5, bindings7, from8, to11, content0, attributes1, requiredInterfaces3, subComponents17, items18, attributes14},
    generalizations={gen_adlrecurs_Interface_NamedElement, gen_adlrecurs_Binding_NamedElement, gen_adlrecurs_Type_Interface, gen_adlrecurs_Item_NamedElement, gen_adlrecurs_Required_Type, gen_adlrecurs_Provided_Type, gen_adlrecurs_Component_AbstractComponent, gen_adlrecurs_Component_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)