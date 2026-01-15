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
ktest301_AbstractComponent = Class(name="ktest301::AbstractComponent", is_abstract=True)
ktest301_Content = Class(name="ktest301::Content")
ktest301_Attributes = Class(name="ktest301::Attributes")
ktest301_Required = Class(name="ktest301::Required")
ktest301_Attribute = Class(name="ktest301::Attribute")
Type = Class(name="Type")
ktest301_Provided = Class(name="ktest301::Provided")
ktest301_Interface = Class(name="ktest301::Interface", is_abstract=True)
NamedElement = Class(name="NamedElement")
ktest301_Binding = Class(name="ktest301::Binding")
ktest301_Component = Class(name="ktest301::Component")
AbstractComponent = Class(name="AbstractComponent")
ktest301_NamedElement = Class(name="ktest301::NamedElement", is_abstract=True)
ktest301_Type = Class(name="ktest301::Type", is_abstract=True)
Interface = Class(name="Interface")
ktest301_Item = Class(name="ktest301::Item")

# ktest301_AbstractComponent class attributes and methods

# ktest301_Content class attributes and methods
ktest301_Content_class: Property = Property(name="class", type=StringType)
ktest301_Content_language: Property = Property(name="language", type=StringType)
ktest301_Content.attributes={ktest301_Content_class, ktest301_Content_language}

# ktest301_Attributes class attributes and methods
ktest301_Attributes_signature: Property = Property(name="signature", type=StringType)
ktest301_Attributes.attributes={ktest301_Attributes_signature}

# ktest301_Required class attributes and methods

# ktest301_Attribute class attributes and methods
ktest301_Attribute_name: Property = Property(name="name", type=StringType)
ktest301_Attribute_value: Property = Property(name="value", type=StringType)
ktest301_Attribute.attributes={ktest301_Attribute_value, ktest301_Attribute_name}

# Type class attributes and methods

# ktest301_Provided class attributes and methods

# ktest301_Interface class attributes and methods

# NamedElement class attributes and methods

# ktest301_Binding class attributes and methods

# ktest301_Component class attributes and methods

# AbstractComponent class attributes and methods

# ktest301_NamedElement class attributes and methods
ktest301_NamedElement_name: Property = Property(name="name", type=StringType)
ktest301_NamedElement.attributes={ktest301_NamedElement_name}

# ktest301_Type class attributes and methods
ktest301_Type_signature: Property = Property(name="signature", type=StringType)
ktest301_Type.attributes={ktest301_Type_signature}

# Interface class attributes and methods

# ktest301_Item class attributes and methods

# Relationships
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="ktest301_Content", type=ktest301_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest301_AbstractComponent", type=ktest301_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="ktest301_Attributes", type=ktest301_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest301_AbstractComponent2", type=ktest301_Attributes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredInterfaces3: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces3",
    ends={
        Property(name="ktest301_Required", type=ktest301_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest301_AbstractComponent4", type=ktest301_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from8: BinaryAssociation = BinaryAssociation(
    name="from8",
    ends={
        Property(name="ktest301_Interface10", type=ktest301_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest301_Binding9", type=ktest301_Interface, multiplicity=Multiplicity(0, 1))
    }
)
to11: BinaryAssociation = BinaryAssociation(
    name="to11",
    ends={
        Property(name="ktest301_Interface13", type=ktest301_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest301_Binding12", type=ktest301_Interface, multiplicity=Multiplicity(0, 1))
    }
)
attributes14: BinaryAssociation = BinaryAssociation(
    name="attributes14",
    ends={
        Property(name="ktest301_Attribute", type=ktest301_Attributes, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest301_Attributes15", type=ktest301_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces5: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces5",
    ends={
        Property(name="ktest301_Provided", type=ktest301_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest301_AbstractComponent6", type=ktest301_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings7: BinaryAssociation = BinaryAssociation(
    name="bindings7",
    ends={
        Property(name="ktest301_Binding", type=ktest301_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest301_Interface", type=ktest301_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subComponents17: BinaryAssociation = BinaryAssociation(
    name="subComponents17",
    ends={
        Property(name="ktest301_Component", type=ktest301_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest301_Component16", type=ktest301_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items18: BinaryAssociation = BinaryAssociation(
    name="items18",
    ends={
        Property(name="ktest301_Item", type=ktest301_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest301_Type", type=ktest301_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ktest301_Required_Type = Generalization(general=Type, specific=ktest301_Required)
gen_ktest301_Provided_Type = Generalization(general=Type, specific=ktest301_Provided)
gen_ktest301_Interface_NamedElement = Generalization(general=NamedElement, specific=ktest301_Interface)
gen_ktest301_Binding_NamedElement = Generalization(general=NamedElement, specific=ktest301_Binding)
gen_ktest301_Item_NamedElement = Generalization(general=NamedElement, specific=ktest301_Item)
gen_ktest301_Component_AbstractComponent = Generalization(general=AbstractComponent, specific=ktest301_Component)
gen_ktest301_Component_NamedElement = Generalization(general=NamedElement, specific=ktest301_Component)
gen_ktest301_Type_Interface = Generalization(general=Interface, specific=ktest301_Type)

# Domain Model
domain_model = DomainModel(
    name="ktest301",
    types={ktest301_AbstractComponent, ktest301_Content, ktest301_Attributes, ktest301_Required, ktest301_Attribute, Type, ktest301_Provided, ktest301_Interface, NamedElement, ktest301_Binding, ktest301_Component, AbstractComponent, ktest301_NamedElement, ktest301_Type, Interface, ktest301_Item},
    associations={content0, attributes1, requiredInterfaces3, from8, to11, attributes14, providedInterfaces5, bindings7, subComponents17, items18},
    generalizations={gen_ktest301_Required_Type, gen_ktest301_Provided_Type, gen_ktest301_Interface_NamedElement, gen_ktest301_Binding_NamedElement, gen_ktest301_Item_NamedElement, gen_ktest301_Component_AbstractComponent, gen_ktest301_Component_NamedElement, gen_ktest301_Type_Interface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)