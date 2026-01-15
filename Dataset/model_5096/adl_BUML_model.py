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
adl_AbstractComponent = Class(name="adl::AbstractComponent", is_abstract=True)
adl_Required = Class(name="adl::Required")
adl_Provided = Class(name="adl::Provided")
adl_Interface = Class(name="adl::Interface", is_abstract=True)
NamedElement = Class(name="NamedElement")
adl_Binding = Class(name="adl::Binding")
adl_NamedElement = Class(name="adl::NamedElement", is_abstract=True)
adl_Type = Class(name="adl::Type", is_abstract=True)
Interface = Class(name="Interface")
Type = Class(name="Type")
adl_Component = Class(name="adl::Component")
AbstractComponent = Class(name="AbstractComponent")

# adl_AbstractComponent class attributes and methods

# adl_Required class attributes and methods

# adl_Provided class attributes and methods

# adl_Interface class attributes and methods

# NamedElement class attributes and methods

# adl_Binding class attributes and methods

# adl_NamedElement class attributes and methods
adl_NamedElement_name: Property = Property(name="name", type=StringType)
adl_NamedElement.attributes={adl_NamedElement_name}

# adl_Type class attributes and methods
adl_Type_signature: Property = Property(name="signature", type=StringType)
adl_Type.attributes={adl_Type_signature}

# Interface class attributes and methods

# Type class attributes and methods

# adl_Component class attributes and methods

# AbstractComponent class attributes and methods

# Relationships
requiredInterfaces0: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces0",
    ends={
        Property(name="adl_Required", type=adl_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adl_AbstractComponent", type=adl_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces1: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces1",
    ends={
        Property(name="adl_Provided", type=adl_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adl_AbstractComponent2", type=adl_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings3: BinaryAssociation = BinaryAssociation(
    name="bindings3",
    ends={
        Property(name="adl_Binding", type=adl_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="adl_Interface", type=adl_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from4: BinaryAssociation = BinaryAssociation(
    name="from4",
    ends={
        Property(name="adl_Interface6", type=adl_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl_Binding5", type=adl_Interface, multiplicity=Multiplicity(0, 1))
    }
)
to7: BinaryAssociation = BinaryAssociation(
    name="to7",
    ends={
        Property(name="adl_Interface9", type=adl_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl_Binding8", type=adl_Interface, multiplicity=Multiplicity(0, 1))
    }
)
subComponents11: BinaryAssociation = BinaryAssociation(
    name="subComponents11",
    ends={
        Property(name="adl_Component", type=adl_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl_Component10", type=adl_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_adl_Interface_NamedElement = Generalization(general=NamedElement, specific=adl_Interface)
gen_adl_Binding_NamedElement = Generalization(general=NamedElement, specific=adl_Binding)
gen_adl_Type_Interface = Generalization(general=Interface, specific=adl_Type)
gen_adl_Required_Type = Generalization(general=Type, specific=adl_Required)
gen_adl_Provided_Type = Generalization(general=Type, specific=adl_Provided)
gen_adl_Component_AbstractComponent = Generalization(general=AbstractComponent, specific=adl_Component)
gen_adl_Component_NamedElement = Generalization(general=NamedElement, specific=adl_Component)

# Domain Model
domain_model = DomainModel(
    name="adl",
    types={adl_AbstractComponent, adl_Required, adl_Provided, adl_Interface, NamedElement, adl_Binding, adl_NamedElement, adl_Type, Interface, Type, adl_Component, AbstractComponent},
    associations={requiredInterfaces0, providedInterfaces1, bindings3, from4, to7, subComponents11},
    generalizations={gen_adl_Interface_NamedElement, gen_adl_Binding_NamedElement, gen_adl_Type_Interface, gen_adl_Required_Type, gen_adl_Provided_Type, gen_adl_Component_AbstractComponent, gen_adl_Component_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)