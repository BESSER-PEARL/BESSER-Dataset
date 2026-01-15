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
adl101_Interface = Class(name="adl101::Interface", is_abstract=True)
adl101_Binding = Class(name="adl101::Binding")
adl101_Content = Class(name="adl101::Content")
adl101_Component = Class(name="adl101::Component")
adl101_Required = Class(name="adl101::Required")
Interface = Class(name="Interface")
adl101_Provided = Class(name="adl101::Provided")

# adl101_Interface class attributes and methods
adl101_Interface_name: Property = Property(name="name", type=StringType)
adl101_Interface_signature: Property = Property(name="signature", type=StringType)
adl101_Interface.attributes={adl101_Interface_name, adl101_Interface_signature}

# adl101_Binding class attributes and methods

# adl101_Content class attributes and methods
adl101_Content_expression: Property = Property(name="expression", type=StringType)
adl101_Content_language: Property = Property(name="language", type=StringType)
adl101_Content.attributes={adl101_Content_language, adl101_Content_expression}

# adl101_Component class attributes and methods
adl101_Component_name: Property = Property(name="name", type=StringType)
adl101_Component.attributes={adl101_Component_name}

# adl101_Required class attributes and methods

# Interface class attributes and methods

# adl101_Provided class attributes and methods

# Relationships
bindings0: BinaryAssociation = BinaryAssociation(
    name="bindings0",
    ends={
        Property(name="adl101_Binding", type=adl101_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="adl101_Interface", type=adl101_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from1: BinaryAssociation = BinaryAssociation(
    name="from1",
    ends={
        Property(name="adl101_Interface3", type=adl101_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl101_Binding2", type=adl101_Interface, multiplicity=Multiplicity(0, 1))
    }
)
to4: BinaryAssociation = BinaryAssociation(
    name="to4",
    ends={
        Property(name="adl101_Interface6", type=adl101_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl101_Binding5", type=adl101_Interface, multiplicity=Multiplicity(0, 1))
    }
)
contentParent7: BinaryAssociation = BinaryAssociation(
    name="contentParent7",
    ends={
        Property(name="Component", type=adl101_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="content", type=adl101_Component, multiplicity=Multiplicity(0, 1))
    }
)
subComponents9: BinaryAssociation = BinaryAssociation(
    name="subComponents9",
    ends={
        Property(name="adl101_Component", type=adl101_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl101_Component8", type=adl101_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterfaces10: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces10",
    ends={
        Property(name="adl101_Required", type=adl101_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl101_Component11", type=adl101_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces12: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces12",
    ends={
        Property(name="adl101_Provided", type=adl101_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl101_Component13", type=adl101_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content14: BinaryAssociation = BinaryAssociation(
    name="content14",
    ends={
        Property(name="Content", type=adl101_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="contentParent", type=adl101_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_adl101_Required_Interface = Generalization(general=Interface, specific=adl101_Required)
gen_adl101_Provided_Interface = Generalization(general=Interface, specific=adl101_Provided)

# Domain Model
domain_model = DomainModel(
    name="adl101",
    types={adl101_Interface, adl101_Binding, adl101_Content, adl101_Component, adl101_Required, Interface, adl101_Provided},
    associations={bindings0, from1, to4, contentParent7, subComponents9, requiredInterfaces10, providedInterfaces12, content14},
    generalizations={gen_adl101_Required_Interface, gen_adl101_Provided_Interface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)