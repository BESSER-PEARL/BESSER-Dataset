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
yyd_Thing = Class(name="yyd::Thing")
yyd_RelatedTo = Class(name="yyd::RelatedTo")
yyd_Foo = Class(name="yyd::Foo", is_abstract=True)
yyd_Alias = Class(name="yyd::Alias")
Foo = Class(name="Foo")
yyd_Blias = Class(name="yyd::Blias")

# yyd_Thing class attributes and methods
yyd_Thing_id: Property = Property(name="id", type=IntegerType)
yyd_Thing.attributes={yyd_Thing_id}

# yyd_RelatedTo class attributes and methods
yyd_RelatedTo_since: Property = Property(name="since", type=StringType)
yyd_RelatedTo.attributes={yyd_RelatedTo_since}

# yyd_Foo class attributes and methods

# yyd_Alias class attributes and methods
yyd_Alias_id: Property = Property(name="id", type=StringType)
yyd_Alias.attributes={yyd_Alias_id}

# Foo class attributes and methods

# yyd_Blias class attributes and methods
yyd_Blias_id: Property = Property(name="id", type=StringType)
yyd_Blias.attributes={yyd_Blias_id}

# Relationships
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="RelatedTo", type=yyd_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=yyd_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing1: BinaryAssociation = BinaryAssociation(
    name="fromThing1",
    ends={
        Property(name="Thing", type=yyd_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=yyd_Thing, multiplicity=Multiplicity(0, 1))
    }
)
foos2: BinaryAssociation = BinaryAssociation(
    name="foos2",
    ends={
        Property(name="yyd_Foo", type=yyd_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="yyd_RelatedTo", type=yyd_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_yyd_Alias_Foo = Generalization(general=Foo, specific=yyd_Alias)
gen_yyd_Blias_Foo = Generalization(general=Foo, specific=yyd_Blias)

# Domain Model
domain_model = DomainModel(
    name="yyd",
    types={yyd_Thing, yyd_RelatedTo, yyd_Foo, yyd_Alias, Foo, yyd_Blias},
    associations={relations0, fromThing1, foos2},
    generalizations={gen_yyd_Alias_Foo, gen_yyd_Blias_Foo},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)