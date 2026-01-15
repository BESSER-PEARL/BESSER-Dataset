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
adl301_AbstractComponent = Class(name="adl301::AbstractComponent", is_abstract=True)
adl301_Content = Class(name="adl301::Content")
adl301_Attributes = Class(name="adl301::Attributes")
adl301_Required = Class(name="adl301::Required")
adl301_Provided = Class(name="adl301::Provided")
adl301_Interface = Class(name="adl301::Interface", is_abstract=True)
NamedElement = Class(name="NamedElement")
adl301_Binding = Class(name="adl301::Binding")
adl301_Attribute = Class(name="adl301::Attribute")
Type = Class(name="Type")
adl301_Component = Class(name="adl301::Component")
AbstractComponent = Class(name="AbstractComponent")
adl301_NamedElement = Class(name="adl301::NamedElement", is_abstract=True)
adl301_Type = Class(name="adl301::Type", is_abstract=True)
Interface = Class(name="Interface")
adl301_Item = Class(name="adl301::Item")

# adl301_AbstractComponent class attributes and methods

# adl301_Content class attributes and methods
adl301_Content_class: Property = Property(name="class", type=StringType)
adl301_Content_language: Property = Property(name="language", type=StringType)
adl301_Content.attributes={adl301_Content_language, adl301_Content_class}

# adl301_Attributes class attributes and methods
adl301_Attributes_signature: Property = Property(name="signature", type=StringType)
adl301_Attributes.attributes={adl301_Attributes_signature}

# adl301_Required class attributes and methods

# adl301_Provided class attributes and methods

# adl301_Interface class attributes and methods

# NamedElement class attributes and methods

# adl301_Binding class attributes and methods

# adl301_Attribute class attributes and methods
adl301_Attribute_name: Property = Property(name="name", type=StringType)
adl301_Attribute_value: Property = Property(name="value", type=StringType)
adl301_Attribute.attributes={adl301_Attribute_name, adl301_Attribute_value}

# Type class attributes and methods

# adl301_Component class attributes and methods

# AbstractComponent class attributes and methods

# adl301_NamedElement class attributes and methods
adl301_NamedElement_name: Property = Property(name="name", type=StringType)
adl301_NamedElement.attributes={adl301_NamedElement_name}

# adl301_Type class attributes and methods
adl301_Type_signature: Property = Property(name="signature", type=StringType)
adl301_Type.attributes={adl301_Type_signature}

# Interface class attributes and methods

# adl301_Item class attributes and methods

# Relationships
from8: BinaryAssociation = BinaryAssociation(
    name="from8",
    ends={
        Property(name="adl301_Interface10", type=adl301_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl301_Binding9", type=adl301_Interface, multiplicity=Multiplicity(0, 1))
    }
)
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="adl301_Content", type=adl301_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adl301_AbstractComponent", type=adl301_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="adl301_Attributes", type=adl301_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adl301_AbstractComponent2", type=adl301_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredInterfaces3: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces3",
    ends={
        Property(name="adl301_Required", type=adl301_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adl301_AbstractComponent4", type=adl301_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces5: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces5",
    ends={
        Property(name="adl301_Provided", type=adl301_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adl301_AbstractComponent6", type=adl301_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings7: BinaryAssociation = BinaryAssociation(
    name="bindings7",
    ends={
        Property(name="adl301_Binding", type=adl301_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="adl301_Interface", type=adl301_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to11: BinaryAssociation = BinaryAssociation(
    name="to11",
    ends={
        Property(name="adl301_Interface13", type=adl301_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl301_Binding12", type=adl301_Interface, multiplicity=Multiplicity(0, 1))
    }
)
attributes14: BinaryAssociation = BinaryAssociation(
    name="attributes14",
    ends={
        Property(name="adl301_Attribute", type=adl301_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="adl301_Attributes15", type=adl301_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subComponents17: BinaryAssociation = BinaryAssociation(
    name="subComponents17",
    ends={
        Property(name="adl301_Component", type=adl301_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl301_Component16", type=adl301_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items18: BinaryAssociation = BinaryAssociation(
    name="items18",
    ends={
        Property(name="adl301_Item", type=adl301_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="adl301_Type", type=adl301_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_adl301_Binding_NamedElement = Generalization(general=NamedElement, specific=adl301_Binding)
gen_adl301_Interface_NamedElement = Generalization(general=NamedElement, specific=adl301_Interface)
gen_adl301_Required_Type = Generalization(general=Type, specific=adl301_Required)
gen_adl301_Provided_Type = Generalization(general=Type, specific=adl301_Provided)
gen_adl301_Component_AbstractComponent = Generalization(general=AbstractComponent, specific=adl301_Component)
gen_adl301_Component_NamedElement = Generalization(general=NamedElement, specific=adl301_Component)
gen_adl301_Type_Interface = Generalization(general=Interface, specific=adl301_Type)
gen_adl301_Item_NamedElement = Generalization(general=NamedElement, specific=adl301_Item)

# Domain Model
domain_model = DomainModel(
    name="adl301",
    types={adl301_AbstractComponent, adl301_Content, adl301_Attributes, adl301_Required, adl301_Provided, adl301_Interface, NamedElement, adl301_Binding, adl301_Attribute, Type, adl301_Component, AbstractComponent, adl301_NamedElement, adl301_Type, Interface, adl301_Item},
    associations={from8, content0, attributes1, requiredInterfaces3, providedInterfaces5, bindings7, to11, attributes14, subComponents17, items18},
    generalizations={gen_adl301_Binding_NamedElement, gen_adl301_Interface_NamedElement, gen_adl301_Required_Type, gen_adl301_Provided_Type, gen_adl301_Component_AbstractComponent, gen_adl301_Component_NamedElement, gen_adl301_Type_Interface, gen_adl301_Item_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)