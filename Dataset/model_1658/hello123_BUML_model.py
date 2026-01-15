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
hello123_Thing = Class(name="hello123::Thing")
NamedElement = Class(name="NamedElement")
hello123_RelatedTo = Class(name="hello123::RelatedTo")
hello123_Property = Class(name="hello123::Property")
hello123_Foo = Class(name="hello123::Foo")
hello123_World = Class(name="hello123::World")
hello123_Bar = Class(name="hello123::Bar")
hello123_NamedElement = Class(name="hello123::NamedElement", is_abstract=True)
hello123_Alias = Class(name="hello123::Alias")

# hello123_Thing class attributes and methods
hello123_Thing_id: Property = Property(name="id", type=IntegerType)
hello123_Thing.attributes={hello123_Thing_id}

# NamedElement class attributes and methods

# hello123_RelatedTo class attributes and methods
hello123_RelatedTo_since: Property = Property(name="since", type=StringType)
hello123_RelatedTo.attributes={hello123_RelatedTo_since}

# hello123_Property class attributes and methods
hello123_Property_name: Property = Property(name="name", type=StringType)
hello123_Property_value: Property = Property(name="value", type=StringType)
hello123_Property.attributes={hello123_Property_name, hello123_Property_value}

# hello123_Foo class attributes and methods
hello123_Foo_id: Property = Property(name="id", type=StringType)
hello123_Foo.attributes={hello123_Foo_id}

# hello123_World class attributes and methods

# hello123_Bar class attributes and methods
hello123_Bar_id: Property = Property(name="id", type=StringType)
hello123_Bar.attributes={hello123_Bar_id}

# hello123_NamedElement class attributes and methods
hello123_NamedElement_name: Property = Property(name="name", type=StringType)
hello123_NamedElement.attributes={hello123_NamedElement_name}

# hello123_Alias class attributes and methods
hello123_Alias_id: Property = Property(name="id", type=StringType)
hello123_Alias.attributes={hello123_Alias_id}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="hello123_Thing", type=hello123_World, multiplicity=Multiplicity(1, 1)),
        Property(name="hello123_World", type=hello123_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=hello123_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=hello123_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties2: BinaryAssociation = BinaryAssociation(
    name="properties2",
    ends={
        Property(name="hello123_Property", type=hello123_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="hello123_Thing3", type=hello123_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos4: BinaryAssociation = BinaryAssociation(
    name="foos4",
    ends={
        Property(name="hello123_Foo", type=hello123_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="hello123_Thing5", type=hello123_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bars6: BinaryAssociation = BinaryAssociation(
    name="bars6",
    ends={
        Property(name="hello123_Bar", type=hello123_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="hello123_Thing7", type=hello123_Bar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases8: BinaryAssociation = BinaryAssociation(
    name="aliases8",
    ends={
        Property(name="hello123_Alias", type=hello123_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="hello123_NamedElement", type=hello123_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing9: BinaryAssociation = BinaryAssociation(
    name="fromThing9",
    ends={
        Property(name="Thing", type=hello123_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=hello123_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing10: BinaryAssociation = BinaryAssociation(
    name="toThing10",
    ends={
        Property(name="hello123_Thing11", type=hello123_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="hello123_RelatedTo", type=hello123_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_hello123_Thing_NamedElement = Generalization(general=NamedElement, specific=hello123_Thing)
gen_hello123_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=hello123_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="hello123",
    types={hello123_Thing, NamedElement, hello123_RelatedTo, hello123_Property, hello123_Foo, hello123_World, hello123_Bar, hello123_NamedElement, hello123_Alias},
    associations={things0, relations1, properties2, foos4, bars6, aliases8, fromThing9, toThing10},
    generalizations={gen_hello123_Thing_NamedElement, gen_hello123_RelatedTo_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)