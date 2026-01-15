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
adlold_AbstractComponent = Class(name="adlold::AbstractComponent", is_abstract=True)
adlold_Content = Class(name="adlold::Content")
adlold_Required = Class(name="adlold::Required")
adlold_Interface = Class(name="adlold::Interface", is_abstract=True)
adlold_Binding = Class(name="adlold::Binding")
Interface = Class(name="Interface")
adlold_Component = Class(name="adlold::Component")
AbstractComponent = Class(name="AbstractComponent")
adlold_Provided = Class(name="adlold::Provided")

# adlold_AbstractComponent class attributes and methods
adlold_AbstractComponent_name: Property = Property(name="name", type=StringType)
adlold_AbstractComponent.attributes={adlold_AbstractComponent_name}

# adlold_Content class attributes and methods
adlold_Content_expression: Property = Property(name="expression", type=StringType)
adlold_Content_language: Property = Property(name="language", type=StringType)
adlold_Content.attributes={adlold_Content_expression, adlold_Content_language}

# adlold_Required class attributes and methods

# adlold_Interface class attributes and methods
adlold_Interface_name: Property = Property(name="name", type=StringType)
adlold_Interface_signature: Property = Property(name="signature", type=StringType)
adlold_Interface.attributes={adlold_Interface_name, adlold_Interface_signature}

# adlold_Binding class attributes and methods

# Interface class attributes and methods

# adlold_Component class attributes and methods

# AbstractComponent class attributes and methods

# adlold_Provided class attributes and methods

# Relationships
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="adlold_Content", type=adlold_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adlold_AbstractComponent", type=adlold_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredInterfaces1: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces1",
    ends={
        Property(name="adlold_Required", type=adlold_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adlold_AbstractComponent2", type=adlold_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings5: BinaryAssociation = BinaryAssociation(
    name="bindings5",
    ends={
        Property(name="adlold_Binding", type=adlold_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="adlold_Interface", type=adlold_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from6: BinaryAssociation = BinaryAssociation(
    name="from6",
    ends={
        Property(name="adlold_Interface8", type=adlold_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adlold_Binding7", type=adlold_Interface, multiplicity=Multiplicity(0, 1))
    }
)
to9: BinaryAssociation = BinaryAssociation(
    name="to9",
    ends={
        Property(name="adlold_Interface11", type=adlold_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="adlold_Binding10", type=adlold_Interface, multiplicity=Multiplicity(0, 1))
    }
)
contentParent12: BinaryAssociation = BinaryAssociation(
    name="contentParent12",
    ends={
        Property(name="adlold_AbstractComponent14", type=adlold_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="adlold_Content13", type=adlold_AbstractComponent, multiplicity=Multiplicity(1, 1))
    }
)
subComponents16: BinaryAssociation = BinaryAssociation(
    name="subComponents16",
    ends={
        Property(name="adlold_Component", type=adlold_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="adlold_Component15", type=adlold_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces3: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces3",
    ends={
        Property(name="adlold_Provided", type=adlold_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="adlold_AbstractComponent4", type=adlold_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_adlold_Required_Interface = Generalization(general=Interface, specific=adlold_Required)
gen_adlold_Provided_Interface = Generalization(general=Interface, specific=adlold_Provided)
gen_adlold_Component_AbstractComponent = Generalization(general=AbstractComponent, specific=adlold_Component)

# Domain Model
domain_model = DomainModel(
    name="adlold",
    types={adlold_AbstractComponent, adlold_Content, adlold_Required, adlold_Interface, adlold_Binding, Interface, adlold_Component, AbstractComponent, adlold_Provided},
    associations={content0, requiredInterfaces1, bindings5, from6, to9, contentParent12, subComponents16, providedInterfaces3},
    generalizations={gen_adlold_Required_Interface, gen_adlold_Provided_Interface, gen_adlold_Component_AbstractComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)