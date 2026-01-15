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
adl402_Interface = Class(name="adl402::Interface", is_abstract=True)
adl402_Binding = Class(name="adl402::Binding", is_abstract=True)
adl402_Content = Class(name="adl402::Content")
adl402_Component = Class(name="adl402::Component")
adl402_EClass0 = Class(name="adl402::EClass0")
adl402_Required = Class(name="adl402::Required")
Interface = Class(name="Interface")
adl402_Provided = Class(name="adl402::Provided")
adl402_EClass1 = Class(name="adl402::EClass1")
Binding = Class(name="Binding")
adl402_EClass2 = Class(name="adl402::EClass2")

# adl402_Interface class attributes and methods
adl402_Interface_name: Property = Property(name="name", type=StringType)
adl402_Interface_signature: Property = Property(name="signature", type=StringType)
adl402_Interface.attributes={adl402_Interface_signature, adl402_Interface_name}

# adl402_Binding class attributes and methods

# adl402_Content class attributes and methods
adl402_Content_expression: Property = Property(name="expression", type=StringType)
adl402_Content_language: Property = Property(name="language", type=StringType)
adl402_Content.attributes={adl402_Content_expression, adl402_Content_language}

# adl402_Component class attributes and methods
adl402_Component_name: Property = Property(name="name", type=StringType)
adl402_Component.attributes={adl402_Component_name}

# adl402_EClass0 class attributes and methods
adl402_EClass0_EAttribute0: Property = Property(name="EAttribute0", type=StringType)
adl402_EClass0.attributes={adl402_EClass0_EAttribute0}

# adl402_Required class attributes and methods

# Interface class attributes and methods

# adl402_Provided class attributes and methods

# adl402_EClass1 class attributes and methods

# Binding class attributes and methods

# adl402_EClass2 class attributes and methods

# Relationships
subComponents10: BinaryAssociation = BinaryAssociation(
    name="subComponents10",
    ends={
        Property(name="adl402_Component", type=adl402_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl402_Component9", type=adl402_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterfaces11: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces11",
    ends={
        Property(name="adl402_Required", type=adl402_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl402_Component12", type=adl402_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces13: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces13",
    ends={
        Property(name="adl402_Provided", type=adl402_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl402_Component14", type=adl402_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings0: BinaryAssociation = BinaryAssociation(
    name="bindings0",
    ends={
        Property(name="adl402_Binding", type=adl402_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="adl402_Interface", type=adl402_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from1: BinaryAssociation = BinaryAssociation(
    name="from1",
    ends={
        Property(name="adl402_Interface3", type=adl402_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl402_Binding2", type=adl402_Interface, multiplicity=Multiplicity(0, 1))
    }
)
to4: BinaryAssociation = BinaryAssociation(
    name="to4",
    ends={
        Property(name="adl402_Interface6", type=adl402_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl402_Binding5", type=adl402_Interface, multiplicity=Multiplicity(0, 1))
    }
)
contentParent7: BinaryAssociation = BinaryAssociation(
    name="contentParent7",
    ends={
        Property(name="Component", type=adl402_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="content", type=adl402_Component, multiplicity=Multiplicity(0, 1))
    }
)
EReference08: BinaryAssociation = BinaryAssociation(
    name="EReference08",
    ends={
        Property(name="adl402_EClass0", type=adl402_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="adl402_Content", type=adl402_EClass0, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content15: BinaryAssociation = BinaryAssociation(
    name="content15",
    ends={
        Property(name="Content", type=adl402_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="contentParent", type=adl402_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
erefs017: BinaryAssociation = BinaryAssociation(
    name="erefs017",
    ends={
        Property(name="adl402_EClass018", type=adl402_EClass0, multiplicity=Multiplicity(1, 1)),
        Property(name="adl402_EClass016", type=adl402_EClass0, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_adl402_Required_Interface = Generalization(general=Interface, specific=adl402_Required)
gen_adl402_Provided_Interface = Generalization(general=Interface, specific=adl402_Provided)
gen_adl402_EClass1_Binding = Generalization(general=Binding, specific=adl402_EClass1)
gen_adl402_EClass2_Binding = Generalization(general=Binding, specific=adl402_EClass2)

# Domain Model
domain_model = DomainModel(
    name="adl402",
    types={adl402_Interface, adl402_Binding, adl402_Content, adl402_Component, adl402_EClass0, adl402_Required, Interface, adl402_Provided, adl402_EClass1, Binding, adl402_EClass2},
    associations={subComponents10, requiredInterfaces11, providedInterfaces13, bindings0, from1, to4, contentParent7, EReference08, content15, erefs017},
    generalizations={gen_adl402_Required_Interface, gen_adl402_Provided_Interface, gen_adl402_EClass1_Binding, gen_adl402_EClass2_Binding},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)