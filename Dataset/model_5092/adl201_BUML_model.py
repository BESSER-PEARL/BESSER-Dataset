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
adl201_Content = Class(name="adl201::Content")
adl201_Required = Class(name="adl201::Required")
adl201_Provided = Class(name="adl201::Provided")
adl201_Binding = Class(name="adl201::Binding")
adl201_Interface = Class(name="adl201::Interface", is_abstract=True)
adl201_Component = Class(name="adl201::Component")
adl201_BindingAttributes = Class(name="adl201::BindingAttributes")
Interface = Class(name="Interface")

# adl201_Content class attributes and methods
adl201_Content_expression: Property = Property(name="expression", type=StringType)
adl201_Content_language: Property = Property(name="language", type=StringType)
adl201_Content.attributes={adl201_Content_language, adl201_Content_expression}

# adl201_Required class attributes and methods

# adl201_Provided class attributes and methods

# adl201_Binding class attributes and methods
adl201_Binding_name: Property = Property(name="name", type=StringType)
adl201_Binding.attributes={adl201_Binding_name}

# adl201_Interface class attributes and methods
adl201_Interface_name: Property = Property(name="name", type=StringType)
adl201_Interface_signature: Property = Property(name="signature", type=StringType)
adl201_Interface.attributes={adl201_Interface_signature, adl201_Interface_name}

# adl201_Component class attributes and methods
adl201_Component_name: Property = Property(name="name", type=StringType)
adl201_Component.attributes={adl201_Component_name}

# adl201_BindingAttributes class attributes and methods
adl201_BindingAttributes_name: Property = Property(name="name", type=StringType)
adl201_BindingAttributes_value: Property = Property(name="value", type=StringType)
adl201_BindingAttributes.attributes={adl201_BindingAttributes_name, adl201_BindingAttributes_value}

# Interface class attributes and methods

# Relationships
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="adl201_Content", type=adl201_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl201_Component", type=adl201_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredInterfaces1: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces1",
    ends={
        Property(name="adl201_Required", type=adl201_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl201_Component2", type=adl201_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces3: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces3",
    ends={
        Property(name="adl201_Provided", type=adl201_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl201_Component4", type=adl201_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings5: BinaryAssociation = BinaryAssociation(
    name="bindings5",
    ends={
        Property(name="adl201_Binding", type=adl201_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl201_Component6", type=adl201_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subComponents8: BinaryAssociation = BinaryAssociation(
    name="subComponents8",
    ends={
        Property(name="adl201_Component9", type=adl201_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl201_Component7", type=adl201_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings21: BinaryAssociation = BinaryAssociation(
    name="bindings21",
    ends={
        Property(name="adl201_Binding23", type=adl201_Provided, multiplicity=Multiplicity(1, 1)),
        Property(name="adl201_Provided22", type=adl201_Binding, multiplicity=Multiplicity(0, 9999))
    }
)
simpleBindings24: BinaryAssociation = BinaryAssociation(
    name="simpleBindings24",
    ends={
        Property(name="adl201_Required26", type=adl201_Provided, multiplicity=Multiplicity(1, 1)),
        Property(name="adl201_Provided25", type=adl201_Required, multiplicity=Multiplicity(0, 9999))
    }
)
to10: BinaryAssociation = BinaryAssociation(
    name="to10",
    ends={
        Property(name="adl201_Required12", type=adl201_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl201_Binding11", type=adl201_Required, multiplicity=Multiplicity(0, 1))
    }
)
attributes13: BinaryAssociation = BinaryAssociation(
    name="attributes13",
    ends={
        Property(name="adl201_BindingAttributes", type=adl201_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl201_Binding14", type=adl201_BindingAttributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from15: BinaryAssociation = BinaryAssociation(
    name="from15",
    ends={
        Property(name="adl201_Provided17", type=adl201_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl201_Binding16", type=adl201_Provided, multiplicity=Multiplicity(0, 1))
    }
)
contentParent18: BinaryAssociation = BinaryAssociation(
    name="contentParent18",
    ends={
        Property(name="adl201_Component20", type=adl201_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="adl201_Content19", type=adl201_Component, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_adl201_Provided_Interface = Generalization(general=Interface, specific=adl201_Provided)
gen_adl201_Required_Interface = Generalization(general=Interface, specific=adl201_Required)

# Domain Model
domain_model = DomainModel(
    name="adl201",
    types={adl201_Content, adl201_Required, adl201_Provided, adl201_Binding, adl201_Interface, adl201_Component, adl201_BindingAttributes, Interface},
    associations={content0, requiredInterfaces1, providedInterfaces3, bindings5, subComponents8, bindings21, simpleBindings24, to10, attributes13, from15, contentParent18},
    generalizations={gen_adl201_Provided_Interface, gen_adl201_Required_Interface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)