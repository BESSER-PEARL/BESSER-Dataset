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
adl202_Component = Class(name="adl202::Component")
adl202_Content = Class(name="adl202::Content")
adl202_Required = Class(name="adl202::Required")
adl202_Provided = Class(name="adl202::Provided")
adl202_Binding = Class(name="adl202::Binding")
adl202_Interface = Class(name="adl202::Interface", is_abstract=True)
adl202_BindingAttributes = Class(name="adl202::BindingAttributes")
Interface = Class(name="Interface")

# adl202_Component class attributes and methods
adl202_Component_name: Property = Property(name="name", type=StringType)
adl202_Component.attributes={adl202_Component_name}

# adl202_Content class attributes and methods
adl202_Content_expression: Property = Property(name="expression", type=StringType)
adl202_Content_language: Property = Property(name="language", type=StringType)
adl202_Content.attributes={adl202_Content_language, adl202_Content_expression}

# adl202_Required class attributes and methods

# adl202_Provided class attributes and methods

# adl202_Binding class attributes and methods
adl202_Binding_name: Property = Property(name="name", type=StringType)
adl202_Binding.attributes={adl202_Binding_name}

# adl202_Interface class attributes and methods
adl202_Interface_signature: Property = Property(name="signature", type=StringType)
adl202_Interface_name: Property = Property(name="name", type=StringType)
adl202_Interface.attributes={adl202_Interface_signature, adl202_Interface_name}

# adl202_BindingAttributes class attributes and methods
adl202_BindingAttributes_name: Property = Property(name="name", type=StringType)
adl202_BindingAttributes_value: Property = Property(name="value", type=StringType)
adl202_BindingAttributes.attributes={adl202_BindingAttributes_name, adl202_BindingAttributes_value}

# Interface class attributes and methods

# Relationships
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="adl202_Content", type=adl202_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl202_Component", type=adl202_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredInterfaces1: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces1",
    ends={
        Property(name="adl202_Required", type=adl202_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl202_Component2", type=adl202_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces3: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces3",
    ends={
        Property(name="adl202_Provided", type=adl202_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl202_Component4", type=adl202_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings5: BinaryAssociation = BinaryAssociation(
    name="bindings5",
    ends={
        Property(name="adl202_Binding", type=adl202_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl202_Component6", type=adl202_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subComponents8: BinaryAssociation = BinaryAssociation(
    name="subComponents8",
    ends={
        Property(name="adl202_Component9", type=adl202_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl202_Component7", type=adl202_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to10: BinaryAssociation = BinaryAssociation(
    name="to10",
    ends={
        Property(name="adl202_Required12", type=adl202_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl202_Binding11", type=adl202_Required, multiplicity=Multiplicity(0, 1))
    }
)
attributes13: BinaryAssociation = BinaryAssociation(
    name="attributes13",
    ends={
        Property(name="adl202_BindingAttributes", type=adl202_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl202_Binding14", type=adl202_BindingAttributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from15: BinaryAssociation = BinaryAssociation(
    name="from15",
    ends={
        Property(name="adl202_Provided17", type=adl202_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl202_Binding16", type=adl202_Provided, multiplicity=Multiplicity(0, 1))
    }
)
contentParent18: BinaryAssociation = BinaryAssociation(
    name="contentParent18",
    ends={
        Property(name="adl202_Component20", type=adl202_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="adl202_Content19", type=adl202_Component, multiplicity=Multiplicity(1, 1))
    }
)
bindings21: BinaryAssociation = BinaryAssociation(
    name="bindings21",
    ends={
        Property(name="adl202_Binding23", type=adl202_Provided, multiplicity=Multiplicity(1, 1)),
        Property(name="adl202_Provided22", type=adl202_Binding, multiplicity=Multiplicity(0, 9999))
    }
)
simpleBindings24: BinaryAssociation = BinaryAssociation(
    name="simpleBindings24",
    ends={
        Property(name="adl202_Required26", type=adl202_Provided, multiplicity=Multiplicity(1, 1)),
        Property(name="adl202_Provided25", type=adl202_Required, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_adl202_Required_Interface = Generalization(general=Interface, specific=adl202_Required)
gen_adl202_Provided_Interface = Generalization(general=Interface, specific=adl202_Provided)

# Domain Model
domain_model = DomainModel(
    name="adl202",
    types={adl202_Component, adl202_Content, adl202_Required, adl202_Provided, adl202_Binding, adl202_Interface, adl202_BindingAttributes, Interface},
    associations={content0, requiredInterfaces1, providedInterfaces3, bindings5, subComponents8, to10, attributes13, from15, contentParent18, bindings21, simpleBindings24},
    generalizations={gen_adl202_Required_Interface, gen_adl202_Provided_Interface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)