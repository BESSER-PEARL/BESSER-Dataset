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
adlrecur_Required = Class(name="adlrecur::Required")
adlrecur_Component = Class(name="adlrecur::Component", is_abstract=True)
adlrecur_Provided = Class(name="adlrecur::Provided")
adlrecur_Interface = Class(name="adlrecur::Interface", is_abstract=True)
adlrecur_Binding = Class(name="adlrecur::Binding")
Interface = Class(name="Interface")
adlrecur_Base = Class(name="adlrecur::Base")
Component = Class(name="Component")

# adlrecur_Required class attributes and methods

# adlrecur_Component class attributes and methods
adlrecur_Component_name: Property = Property(name="name", type=StringType)
adlrecur_Component.attributes={adlrecur_Component_name}

# adlrecur_Provided class attributes and methods

# adlrecur_Interface class attributes and methods
adlrecur_Interface_name: Property = Property(name="name", type=StringType)
adlrecur_Interface_signature: Property = Property(name="signature", type=StringType)
adlrecur_Interface.attributes={adlrecur_Interface_signature, adlrecur_Interface_name}

# adlrecur_Binding class attributes and methods

# Interface class attributes and methods

# adlrecur_Base class attributes and methods

# Component class attributes and methods

# Relationships
components11: BinaryAssociation = BinaryAssociation(
    name="components11",
    ends={
        Property(name="adlrecur_Base", type=adlrecur_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecur_Base10", type=adlrecur_Base, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterfaces0: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces0",
    ends={
        Property(name="adlrecur_Required", type=adlrecur_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecur_Component", type=adlrecur_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces1: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces1",
    ends={
        Property(name="adlrecur_Provided", type=adlrecur_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecur_Component2", type=adlrecur_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings3: BinaryAssociation = BinaryAssociation(
    name="bindings3",
    ends={
        Property(name="adlrecur_Binding", type=adlrecur_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecur_Interface", type=adlrecur_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from4: BinaryAssociation = BinaryAssociation(
    name="from4",
    ends={
        Property(name="adlrecur_Interface6", type=adlrecur_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecur_Binding5", type=adlrecur_Interface, multiplicity=Multiplicity(0, 1))
    }
)
to7: BinaryAssociation = BinaryAssociation(
    name="to7",
    ends={
        Property(name="adlrecur_Interface9", type=adlrecur_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adlrecur_Binding8", type=adlrecur_Interface, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_adlrecur_Required_Interface = Generalization(general=Interface, specific=adlrecur_Required)
gen_adlrecur_Provided_Interface = Generalization(general=Interface, specific=adlrecur_Provided)
gen_adlrecur_Base_Component = Generalization(general=Component, specific=adlrecur_Base)

# Domain Model
domain_model = DomainModel(
    name="adlrecur",
    types={adlrecur_Required, adlrecur_Component, adlrecur_Provided, adlrecur_Interface, adlrecur_Binding, Interface, adlrecur_Base, Component},
    associations={components11, requiredInterfaces0, providedInterfaces1, bindings3, from4, to7},
    generalizations={gen_adlrecur_Required_Interface, gen_adlrecur_Provided_Interface, gen_adlrecur_Base_Component},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)