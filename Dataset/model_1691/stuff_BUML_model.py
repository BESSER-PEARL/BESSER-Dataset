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
stuff_World = Class(name="stuff::World")
stuff_Thing = Class(name="stuff::Thing")
NamedElement = Class(name="NamedElement")
stuff_Baz = Class(name="stuff::Baz")
stuff_Stuff = Class(name="stuff::Stuff")
Thing = Class(name="Thing")
stuff_Foo = Class(name="stuff::Foo")
stuff_Bar = Class(name="stuff::Bar")
stuff_NamedElement = Class(name="stuff::NamedElement", is_abstract=True)

# stuff_World class attributes and methods

# stuff_Thing class attributes and methods
stuff_Thing_id: Property = Property(name="id", type=IntegerType)
stuff_Thing.attributes={stuff_Thing_id}

# NamedElement class attributes and methods

# stuff_Baz class attributes and methods

# stuff_Stuff class attributes and methods

# Thing class attributes and methods

# stuff_Foo class attributes and methods
stuff_Foo_name: Property = Property(name="name", type=StringType)
stuff_Foo.attributes={stuff_Foo_name}

# stuff_Bar class attributes and methods

# stuff_NamedElement class attributes and methods
stuff_NamedElement_name: Property = Property(name="name", type=StringType)
stuff_NamedElement.attributes={stuff_NamedElement_name}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="stuff_Thing", type=stuff_World, multiplicity=Multiplicity(1, 1)),
        Property(name="stuff_World", type=stuff_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baz13: BinaryAssociation = BinaryAssociation(
    name="baz13",
    ends={
        Property(name="stuff_Baz", type=stuff_Bar, multiplicity=Multiplicity(1, 1)),
        Property(name="stuff_Bar14", type=stuff_Baz, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
others2: BinaryAssociation = BinaryAssociation(
    name="others2",
    ends={
        Property(name="stuff_Thing3", type=stuff_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="stuff_Thing1", type=stuff_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
foos4: BinaryAssociation = BinaryAssociation(
    name="foos4",
    ends={
        Property(name="stuff_Foo", type=stuff_Stuff, multiplicity=Multiplicity(1, 1)),
        Property(name="stuff_Stuff", type=stuff_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bars5: BinaryAssociation = BinaryAssociation(
    name="bars5",
    ends={
        Property(name="stuff_Bar", type=stuff_Stuff, multiplicity=Multiplicity(1, 1)),
        Property(name="stuff_Stuff6", type=stuff_Bar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src7: BinaryAssociation = BinaryAssociation(
    name="src7",
    ends={
        Property(name="stuff_Stuff9", type=stuff_Foo, multiplicity=Multiplicity(1, 1)),
        Property(name="stuff_Foo8", type=stuff_Stuff, multiplicity=Multiplicity(0, 1))
    }
)
trg10: BinaryAssociation = BinaryAssociation(
    name="trg10",
    ends={
        Property(name="stuff_Thing12", type=stuff_Foo, multiplicity=Multiplicity(1, 1)),
        Property(name="stuff_Foo11", type=stuff_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_stuff_Bar_NamedElement = Generalization(general=NamedElement, specific=stuff_Bar)
gen_stuff_Baz_NamedElement = Generalization(general=NamedElement, specific=stuff_Baz)
gen_stuff_Stuff_Thing = Generalization(general=Thing, specific=stuff_Stuff)

# Domain Model
domain_model = DomainModel(
    name="stuff",
    types={stuff_World, stuff_Thing, NamedElement, stuff_Baz, stuff_Stuff, Thing, stuff_Foo, stuff_Bar, stuff_NamedElement},
    associations={things0, baz13, others2, foos4, bars5, src7, trg10},
    generalizations={gen_stuff_Bar_NamedElement, gen_stuff_Baz_NamedElement, gen_stuff_Stuff_Thing},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)