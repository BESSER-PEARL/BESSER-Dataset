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
adl200_Component = Class(name="adl200::Component")
adl200_Content = Class(name="adl200::Content")
adl200_Required = Class(name="adl200::Required")
adl200_Provided = Class(name="adl200::Provided")
Interface = Class(name="Interface")
adl200_Interface = Class(name="adl200::Interface", is_abstract=True)

# adl200_Component class attributes and methods
adl200_Component_name: Property = Property(name="name", type=StringType)
adl200_Component.attributes={adl200_Component_name}

# adl200_Content class attributes and methods
adl200_Content_expression: Property = Property(name="expression", type=StringType)
adl200_Content_language: Property = Property(name="language", type=StringType)
adl200_Content.attributes={adl200_Content_expression, adl200_Content_language}

# adl200_Required class attributes and methods

# adl200_Provided class attributes and methods

# Interface class attributes and methods

# adl200_Interface class attributes and methods
adl200_Interface_signature: Property = Property(name="signature", type=StringType)
adl200_Interface_name: Property = Property(name="name", type=StringType)
adl200_Interface.attributes={adl200_Interface_signature, adl200_Interface_name}

# Relationships
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="adl200_Content", type=adl200_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl200_Component", type=adl200_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredInterfaces1: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces1",
    ends={
        Property(name="adl200_Required", type=adl200_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl200_Component2", type=adl200_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces3: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces3",
    ends={
        Property(name="adl200_Provided", type=adl200_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl200_Component4", type=adl200_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subComponents6: BinaryAssociation = BinaryAssociation(
    name="subComponents6",
    ends={
        Property(name="adl200_Component7", type=adl200_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl200_Component5", type=adl200_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentParent8: BinaryAssociation = BinaryAssociation(
    name="contentParent8",
    ends={
        Property(name="adl200_Component10", type=adl200_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="adl200_Content9", type=adl200_Component, multiplicity=Multiplicity(1, 1))
    }
)
bindings11: BinaryAssociation = BinaryAssociation(
    name="bindings11",
    ends={
        Property(name="adl200_Required13", type=adl200_Provided, multiplicity=Multiplicity(1, 1)),
        Property(name="adl200_Provided12", type=adl200_Required, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_adl200_Required_Interface = Generalization(general=Interface, specific=adl200_Required)
gen_adl200_Provided_Interface = Generalization(general=Interface, specific=adl200_Provided)

# Domain Model
domain_model = DomainModel(
    name="adl200",
    types={adl200_Component, adl200_Content, adl200_Required, adl200_Provided, Interface, adl200_Interface},
    associations={content0, requiredInterfaces1, providedInterfaces3, subComponents6, contentParent8, bindings11},
    generalizations={gen_adl200_Required_Interface, gen_adl200_Provided_Interface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)