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
adlsimple_Component = Class(name="adlsimple::Component")
adlsimple_Required = Class(name="adlsimple::Required")
adlsimple_Provided = Class(name="adlsimple::Provided")
adlsimple_Interface = Class(name="adlsimple::Interface", is_abstract=True)
adlsimple_Binding = Class(name="adlsimple::Binding")
adlsimple_Base = Class(name="adlsimple::Base")
Interface = Class(name="Interface")

# adlsimple_Component class attributes and methods
adlsimple_Component_name: Property = Property(name="name", type=StringType)
adlsimple_Component.attributes={adlsimple_Component_name}

# adlsimple_Required class attributes and methods

# adlsimple_Provided class attributes and methods

# adlsimple_Interface class attributes and methods
adlsimple_Interface_name: Property = Property(name="name", type=StringType)
adlsimple_Interface_signature: Property = Property(name="signature", type=StringType)
adlsimple_Interface.attributes={adlsimple_Interface_name, adlsimple_Interface_signature}

# adlsimple_Binding class attributes and methods

# adlsimple_Base class attributes and methods

# Interface class attributes and methods

# Relationships
requiredInterfaces0: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces0",
    ends={
        Property(name="adlsimple_Required", type=adlsimple_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adlsimple_Component", type=adlsimple_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces1: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces1",
    ends={
        Property(name="adlsimple_Provided", type=adlsimple_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adlsimple_Component2", type=adlsimple_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings3: BinaryAssociation = BinaryAssociation(
    name="bindings3",
    ends={
        Property(name="adlsimple_Binding", type=adlsimple_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="adlsimple_Interface", type=adlsimple_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from4: BinaryAssociation = BinaryAssociation(
    name="from4",
    ends={
        Property(name="adlsimple_Interface6", type=adlsimple_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adlsimple_Binding5", type=adlsimple_Interface, multiplicity=Multiplicity(0, 1))
    }
)
to7: BinaryAssociation = BinaryAssociation(
    name="to7",
    ends={
        Property(name="adlsimple_Interface9", type=adlsimple_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adlsimple_Binding8", type=adlsimple_Interface, multiplicity=Multiplicity(0, 1))
    }
)
components10: BinaryAssociation = BinaryAssociation(
    name="components10",
    ends={
        Property(name="adlsimple_Component11", type=adlsimple_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="adlsimple_Base", type=adlsimple_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_adlsimple_Provided_Interface = Generalization(general=Interface, specific=adlsimple_Provided)
gen_adlsimple_Required_Interface = Generalization(general=Interface, specific=adlsimple_Required)

# Domain Model
domain_model = DomainModel(
    name="adlsimple",
    types={adlsimple_Component, adlsimple_Required, adlsimple_Provided, adlsimple_Interface, adlsimple_Binding, adlsimple_Base, Interface},
    associations={requiredInterfaces0, providedInterfaces1, bindings3, from4, to7, components10},
    generalizations={gen_adlsimple_Provided_Interface, gen_adlsimple_Required_Interface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)