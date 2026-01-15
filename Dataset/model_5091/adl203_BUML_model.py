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
adl203_Component = Class(name="adl203::Component")
adl203_Content = Class(name="adl203::Content")
adl203_Required = Class(name="adl203::Required")
adl203_Provided = Class(name="adl203::Provided")
adl203_Binding = Class(name="adl203::Binding")
adl203_Interface = Class(name="adl203::Interface", is_abstract=True)
adl203_BindingAttributes = Class(name="adl203::BindingAttributes")
Interface = Class(name="Interface")

# adl203_Component class attributes and methods
adl203_Component_name: Property = Property(name="name", type=StringType)
adl203_Component.attributes={adl203_Component_name}

# adl203_Content class attributes and methods
adl203_Content_expression: Property = Property(name="expression", type=StringType)
adl203_Content_language: Property = Property(name="language", type=StringType)
adl203_Content.attributes={adl203_Content_expression, adl203_Content_language}

# adl203_Required class attributes and methods

# adl203_Provided class attributes and methods

# adl203_Binding class attributes and methods
adl203_Binding_name: Property = Property(name="name", type=StringType)
adl203_Binding.attributes={adl203_Binding_name}

# adl203_Interface class attributes and methods
adl203_Interface_name: Property = Property(name="name", type=StringType)
adl203_Interface_signature: Property = Property(name="signature", type=StringType)
adl203_Interface.attributes={adl203_Interface_signature, adl203_Interface_name}

# adl203_BindingAttributes class attributes and methods
adl203_BindingAttributes_name: Property = Property(name="name", type=StringType)
adl203_BindingAttributes_value: Property = Property(name="value", type=StringType)
adl203_BindingAttributes.attributes={adl203_BindingAttributes_value, adl203_BindingAttributes_name}

# Interface class attributes and methods

# Relationships
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="adl203_Content", type=adl203_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl203_Component", type=adl203_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredInterfaces1: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces1",
    ends={
        Property(name="adl203_Required", type=adl203_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl203_Component2", type=adl203_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces3: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces3",
    ends={
        Property(name="adl203_Provided", type=adl203_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl203_Component4", type=adl203_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings5: BinaryAssociation = BinaryAssociation(
    name="bindings5",
    ends={
        Property(name="adl203_Binding", type=adl203_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl203_Component6", type=adl203_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to10: BinaryAssociation = BinaryAssociation(
    name="to10",
    ends={
        Property(name="adl203_Required12", type=adl203_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl203_Binding11", type=adl203_Required, multiplicity=Multiplicity(0, 1))
    }
)
attributes13: BinaryAssociation = BinaryAssociation(
    name="attributes13",
    ends={
        Property(name="adl203_BindingAttributes", type=adl203_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl203_Binding14", type=adl203_BindingAttributes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from15: BinaryAssociation = BinaryAssociation(
    name="from15",
    ends={
        Property(name="adl203_Provided17", type=adl203_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl203_Binding16", type=adl203_Provided, multiplicity=Multiplicity(0, 1))
    }
)
contentParent18: BinaryAssociation = BinaryAssociation(
    name="contentParent18",
    ends={
        Property(name="adl203_Component20", type=adl203_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="adl203_Content19", type=adl203_Component, multiplicity=Multiplicity(1, 1))
    }
)
bindings21: BinaryAssociation = BinaryAssociation(
    name="bindings21",
    ends={
        Property(name="adl203_Binding23", type=adl203_Provided, multiplicity=Multiplicity(1, 1)),
        Property(name="adl203_Provided22", type=adl203_Binding, multiplicity=Multiplicity(0, 9999))
    }
)
simpleBindings24: BinaryAssociation = BinaryAssociation(
    name="simpleBindings24",
    ends={
        Property(name="adl203_Required26", type=adl203_Provided, multiplicity=Multiplicity(1, 1)),
        Property(name="adl203_Provided25", type=adl203_Required, multiplicity=Multiplicity(0, 9999))
    }
)
subComponents8: BinaryAssociation = BinaryAssociation(
    name="subComponents8",
    ends={
        Property(name="adl203_Component9", type=adl203_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl203_Component7", type=adl203_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_adl203_Required_Interface = Generalization(general=Interface, specific=adl203_Required)
gen_adl203_Provided_Interface = Generalization(general=Interface, specific=adl203_Provided)

# Domain Model
domain_model = DomainModel(
    name="adl203",
    types={adl203_Component, adl203_Content, adl203_Required, adl203_Provided, adl203_Binding, adl203_Interface, adl203_BindingAttributes, Interface},
    associations={content0, requiredInterfaces1, providedInterfaces3, bindings5, to10, attributes13, from15, contentParent18, bindings21, simpleBindings24, subComponents8},
    generalizations={gen_adl203_Required_Interface, gen_adl203_Provided_Interface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)