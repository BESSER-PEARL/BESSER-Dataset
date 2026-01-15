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
adl199_AbstractComponent = Class(name="adl199::AbstractComponent", is_abstract=True)
Interface = Class(name="Interface")
adl199_Content = Class(name="adl199::Content")
adl199_Required = Class(name="adl199::Required")
adl199_Provided = Class(name="adl199::Provided")
adl199_Delegation = Class(name="adl199::Delegation")
adl199_Interface = Class(name="adl199::Interface", is_abstract=True)
adl199_Binding = Class(name="adl199::Binding")
adl199_Component = Class(name="adl199::Component")
AbstractComponent = Class(name="AbstractComponent")
adl199_AtomicComponent = Class(name="adl199::AtomicComponent")

# adl199_AbstractComponent class attributes and methods
adl199_AbstractComponent_name: Property = Property(name="name", type=StringType)
adl199_AbstractComponent.attributes={adl199_AbstractComponent_name}

# Interface class attributes and methods

# adl199_Content class attributes and methods
adl199_Content_expression: Property = Property(name="expression", type=StringType)
adl199_Content_language: Property = Property(name="language", type=StringType)
adl199_Content.attributes={adl199_Content_language, adl199_Content_expression}

# adl199_Required class attributes and methods

# adl199_Provided class attributes and methods

# adl199_Delegation class attributes and methods

# adl199_Interface class attributes and methods
adl199_Interface_name: Property = Property(name="name", type=StringType)
adl199_Interface_signature: Property = Property(name="signature", type=StringType)
adl199_Interface.attributes={adl199_Interface_name, adl199_Interface_signature}

# adl199_Binding class attributes and methods

# adl199_Component class attributes and methods

# AbstractComponent class attributes and methods

# adl199_AtomicComponent class attributes and methods

# Relationships
to11: BinaryAssociation = BinaryAssociation(
    name="to11",
    ends={
        Property(name="adl199_Interface13", type=adl199_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl199_Binding12", type=adl199_Interface, multiplicity=Multiplicity(0, 1))
    }
)
parent14: BinaryAssociation = BinaryAssociation(
    name="parent14",
    ends={
        Property(name="adl199_AbstractComponent16", type=adl199_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="adl199_Content15", type=adl199_AbstractComponent, multiplicity=Multiplicity(1, 1))
    }
)
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="adl199_Content", type=adl199_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adl199_AbstractComponent", type=adl199_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredInterfaces1: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces1",
    ends={
        Property(name="adl199_Required", type=adl199_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adl199_AbstractComponent2", type=adl199_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces3: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces3",
    ends={
        Property(name="adl199_Provided", type=adl199_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adl199_AbstractComponent4", type=adl199_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delegationInterfaces5: BinaryAssociation = BinaryAssociation(
    name="delegationInterfaces5",
    ends={
        Property(name="adl199_Delegation", type=adl199_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adl199_AbstractComponent6", type=adl199_Delegation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings7: BinaryAssociation = BinaryAssociation(
    name="bindings7",
    ends={
        Property(name="adl199_Binding", type=adl199_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="adl199_Interface", type=adl199_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from8: BinaryAssociation = BinaryAssociation(
    name="from8",
    ends={
        Property(name="adl199_Interface10", type=adl199_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adl199_Binding9", type=adl199_Interface, multiplicity=Multiplicity(0, 1))
    }
)
subComponents17: BinaryAssociation = BinaryAssociation(
    name="subComponents17",
    ends={
        Property(name="adl199_AbstractComponent18", type=adl199_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adl199_Component", type=adl199_AbstractComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_adl199_Required_Interface = Generalization(general=Interface, specific=adl199_Required)
gen_adl199_Provided_Interface = Generalization(general=Interface, specific=adl199_Provided)
gen_adl199_Component_AbstractComponent = Generalization(general=AbstractComponent, specific=adl199_Component)
gen_adl199_Delegation_Interface = Generalization(general=Interface, specific=adl199_Delegation)
gen_adl199_AtomicComponent_AbstractComponent = Generalization(general=AbstractComponent, specific=adl199_AtomicComponent)

# Domain Model
domain_model = DomainModel(
    name="adl199",
    types={adl199_AbstractComponent, Interface, adl199_Content, adl199_Required, adl199_Provided, adl199_Delegation, adl199_Interface, adl199_Binding, adl199_Component, AbstractComponent, adl199_AtomicComponent},
    associations={to11, parent14, content0, requiredInterfaces1, providedInterfaces3, delegationInterfaces5, bindings7, from8, subComponents17},
    generalizations={gen_adl199_Required_Interface, gen_adl199_Provided_Interface, gen_adl199_Component_AbstractComponent, gen_adl199_Delegation_Interface, gen_adl199_AtomicComponent_AbstractComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)