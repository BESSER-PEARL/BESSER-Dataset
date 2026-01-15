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
adl401_Content = Class(name="adl401::Content")
adl401_Component = Class(name="adl401::Component")
adl401_Interface = Class(name="adl401::Interface", is_abstract=True)
adl401_Binding = Class(name="adl401::Binding")
adl401_EClass0 = Class(name="adl401::EClass0")
adl401_Required = Class(name="adl401::Required")
Interface = Class(name="Interface")
adl401_Provided = Class(name="adl401::Provided")

# adl401_Content class attributes and methods
adl401_Content_expression: Property = Property(name="expression", type=StringType)
adl401_Content_language: Property = Property(name="language", type=StringType)
adl401_Content.attributes={adl401_Content_expression, adl401_Content_language}

# adl401_Component class attributes and methods
adl401_Component_name: Property = Property(name="name", type=StringType)
adl401_Component.attributes={adl401_Component_name}

# adl401_Interface class attributes and methods
adl401_Interface_name: Property = Property(name="name", type=StringType)
adl401_Interface_signature: Property = Property(name="signature", type=StringType)
adl401_Interface.attributes={adl401_Interface_name, adl401_Interface_signature}

# adl401_Binding class attributes and methods

# adl401_EClass0 class attributes and methods
adl401_EClass0_EAttribute0: Property = Property(name="EAttribute0", type=StringType)
adl401_EClass0.attributes={adl401_EClass0_EAttribute0}

# adl401_Required class attributes and methods

# Interface class attributes and methods

# adl401_Provided class attributes and methods

# Relationships
from1: BinaryAssociation = BinaryAssociation(
    name="from1",
    ends={
        Property(name="adl401_Interface3", type=adl401_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl401_Binding2", type=adl401_Interface, multiplicity=Multiplicity(0, 1))
    }
)
to4: BinaryAssociation = BinaryAssociation(
    name="to4",
    ends={
        Property(name="adl401_Interface6", type=adl401_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl401_Binding5", type=adl401_Interface, multiplicity=Multiplicity(0, 1))
    }
)
contentParent7: BinaryAssociation = BinaryAssociation(
    name="contentParent7",
    ends={
        Property(name="Component", type=adl401_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="content", type=adl401_Component, multiplicity=Multiplicity(0, 1))
    }
)
bindings0: BinaryAssociation = BinaryAssociation(
    name="bindings0",
    ends={
        Property(name="adl401_Binding", type=adl401_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="adl401_Interface", type=adl401_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
erefs017: BinaryAssociation = BinaryAssociation(
    name="erefs017",
    ends={
        Property(name="adl401_EClass018", type=adl401_EClass0, multiplicity=Multiplicity(1, 1)),
        Property(name="adl401_EClass016", type=adl401_EClass0, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
EReference08: BinaryAssociation = BinaryAssociation(
    name="EReference08",
    ends={
        Property(name="adl401_EClass0", type=adl401_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="adl401_Content", type=adl401_EClass0, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subComponents10: BinaryAssociation = BinaryAssociation(
    name="subComponents10",
    ends={
        Property(name="adl401_Component", type=adl401_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl401_Component9", type=adl401_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterfaces11: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces11",
    ends={
        Property(name="adl401_Required", type=adl401_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl401_Component12", type=adl401_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces13: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces13",
    ends={
        Property(name="adl401_Provided", type=adl401_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl401_Component14", type=adl401_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content15: BinaryAssociation = BinaryAssociation(
    name="content15",
    ends={
        Property(name="Content", type=adl401_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="contentParent", type=adl401_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_adl401_Required_Interface = Generalization(general=Interface, specific=adl401_Required)
gen_adl401_Provided_Interface = Generalization(general=Interface, specific=adl401_Provided)

# Domain Model
domain_model = DomainModel(
    name="adl401",
    types={adl401_Content, adl401_Component, adl401_Interface, adl401_Binding, adl401_EClass0, adl401_Required, Interface, adl401_Provided},
    associations={from1, to4, contentParent7, bindings0, erefs017, EReference08, subComponents10, requiredInterfaces11, providedInterfaces13, content15},
    generalizations={gen_adl401_Required_Interface, gen_adl401_Provided_Interface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)