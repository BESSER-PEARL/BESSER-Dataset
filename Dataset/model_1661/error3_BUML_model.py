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
error3_World = Class(name="error3::World")
error3_Thing = Class(name="error3::Thing")
NamedElement = Class(name="NamedElement")
error3_RelatedTo = Class(name="error3::RelatedTo")
error3_Required = Class(name="error3::Required")
error3_Binding = Class(name="error3::Binding")
error3_Provided = Class(name="error3::Provided")
error3_NamedElement = Class(name="error3::NamedElement", is_abstract=True)
error3_AbstractComponent = Class(name="error3::AbstractComponent")
error3_Level2 = Class(name="error3::Level2")
AbstractComponent = Class(name="AbstractComponent")
error3_NestedComponent = Class(name="error3::NestedComponent")
error3_Bazbar = Class(name="error3::Bazbar")
error3_RecursiveComponen = Class(name="error3::RecursiveComponen")

# error3_World class attributes and methods

# error3_Thing class attributes and methods
error3_Thing_id: Property = Property(name="id", type=IntegerType)
error3_Thing.attributes={error3_Thing_id}

# NamedElement class attributes and methods

# error3_RelatedTo class attributes and methods
error3_RelatedTo_since: Property = Property(name="since", type=StringType)
error3_RelatedTo.attributes={error3_RelatedTo_since}

# error3_Required class attributes and methods
error3_Required_ir: Property = Property(name="ir", type=StringType)
error3_Required.attributes={error3_Required_ir}

# error3_Binding class attributes and methods
error3_Binding_type: Property = Property(name="type", type=StringType)
error3_Binding.attributes={error3_Binding_type}

# error3_Provided class attributes and methods
error3_Provided_ip: Property = Property(name="ip", type=StringType)
error3_Provided.attributes={error3_Provided_ip}

# error3_NamedElement class attributes and methods
error3_NamedElement_name: Property = Property(name="name", type=StringType)
error3_NamedElement.attributes={error3_NamedElement_name}

# error3_AbstractComponent class attributes and methods
error3_AbstractComponent_name: Property = Property(name="name", type=StringType)
error3_AbstractComponent.attributes={error3_AbstractComponent_name}

# error3_Level2 class attributes and methods

# AbstractComponent class attributes and methods

# error3_NestedComponent class attributes and methods

# error3_Bazbar class attributes and methods
error3_Bazbar_b: Property = Property(name="b", type=StringType)
error3_Bazbar.attributes={error3_Bazbar_b}

# error3_RecursiveComponen class attributes and methods

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="error3_Thing", type=error3_World, multiplicity=Multiplicity(1, 1)),
        Property(name="error3_World", type=error3_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing2: BinaryAssociation = BinaryAssociation(
    name="fromThing2",
    ends={
        Property(name="Thing", type=error3_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=error3_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing3: BinaryAssociation = BinaryAssociation(
    name="toThing3",
    ends={
        Property(name="error3_Thing4", type=error3_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="error3_RelatedTo", type=error3_Thing, multiplicity=Multiplicity(0, 1))
    }
)
bindings5: BinaryAssociation = BinaryAssociation(
    name="bindings5",
    ends={
        Property(name="error3_Binding", type=error3_Required, multiplicity=Multiplicity(1, 1)),
        Property(name="error3_Required", type=error3_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src6: BinaryAssociation = BinaryAssociation(
    name="src6",
    ends={
        Property(name="error3_Required8", type=error3_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="error3_Binding7", type=error3_Required, multiplicity=Multiplicity(0, 1))
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=error3_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=error3_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredInterfaces11: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces11",
    ends={
        Property(name="error3_Required12", type=error3_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="error3_AbstractComponent", type=error3_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces13: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces13",
    ends={
        Property(name="error3_Provided15", type=error3_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="error3_AbstractComponent14", type=error3_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
levels216: BinaryAssociation = BinaryAssociation(
    name="levels216",
    ends={
        Property(name="error3_Level2", type=error3_NestedComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="error3_NestedComponent", type=error3_Level2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trg9: BinaryAssociation = BinaryAssociation(
    name="trg9",
    ends={
        Property(name="error3_Provided", type=error3_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="error3_Binding10", type=error3_Provided, multiplicity=Multiplicity(0, 1))
    }
)
levels117: BinaryAssociation = BinaryAssociation(
    name="levels117",
    ends={
        Property(name="error3_NestedComponent18", type=error3_RecursiveComponen, multiplicity=Multiplicity(1, 1)),
        Property(name="error3_RecursiveComponen", type=error3_NestedComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bazbars19: BinaryAssociation = BinaryAssociation(
    name="bazbars19",
    ends={
        Property(name="error3_Bazbar", type=error3_RecursiveComponen, multiplicity=Multiplicity(1, 1)),
        Property(name="error3_RecursiveComponen20", type=error3_Bazbar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components22: BinaryAssociation = BinaryAssociation(
    name="components22",
    ends={
        Property(name="error3_RecursiveComponen23", type=error3_RecursiveComponen, multiplicity=Multiplicity(1, 1)),
        Property(name="error3_RecursiveComponen21", type=error3_RecursiveComponen, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_error3_Thing_NamedElement = Generalization(general=NamedElement, specific=error3_Thing)
gen_error3_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=error3_RelatedTo)
gen_error3_Level2_AbstractComponent = Generalization(general=AbstractComponent, specific=error3_Level2)
gen_error3_NestedComponent_AbstractComponent = Generalization(general=AbstractComponent, specific=error3_NestedComponent)
gen_error3_RecursiveComponen_AbstractComponent = Generalization(general=AbstractComponent, specific=error3_RecursiveComponen)

# Domain Model
domain_model = DomainModel(
    name="error3",
    types={error3_World, error3_Thing, NamedElement, error3_RelatedTo, error3_Required, error3_Binding, error3_Provided, error3_NamedElement, error3_AbstractComponent, error3_Level2, AbstractComponent, error3_NestedComponent, error3_Bazbar, error3_RecursiveComponen},
    associations={things0, fromThing2, toThing3, bindings5, src6, relations1, requiredInterfaces11, providedInterfaces13, levels216, trg9, levels117, bazbars19, components22},
    generalizations={gen_error3_Thing_NamedElement, gen_error3_RelatedTo_NamedElement, gen_error3_Level2_AbstractComponent, gen_error3_NestedComponent_AbstractComponent, gen_error3_RecursiveComponen_AbstractComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)