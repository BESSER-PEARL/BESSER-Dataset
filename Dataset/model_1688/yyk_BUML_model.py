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
yyk_Relation = Class(name="yyk::Relation")
yyk_Foo = Class(name="yyk::Foo")
yyk_Output = Class(name="yyk::Output")
yyk_Baz = Class(name="yyk::Baz", is_abstract=True)
yyk_NamedElement = Class(name="yyk::NamedElement", is_abstract=True)
yyk_Base = Class(name="yyk::Base")
NamedElement = Class(name="NamedElement")
yyk_Rel = Class(name="yyk::Rel")
yyk_Alias = Class(name="yyk::Alias")
yyk_Bar = Class(name="yyk::Bar")
yyk_Zing = Class(name="yyk::Zing")
yyk_Bouz = Class(name="yyk::Bouz")
Baz = Class(name="Baz")
yyk_Boul = Class(name="yyk::Boul")

# yyk_Relation class attributes and methods
yyk_Relation_since: Property = Property(name="since", type=StringType)
yyk_Relation.attributes={yyk_Relation_since}

# yyk_Foo class attributes and methods
yyk_Foo_id: Property = Property(name="id", type=StringType)
yyk_Foo.attributes={yyk_Foo_id}

# yyk_Output class attributes and methods
yyk_Output_id: Property = Property(name="id", type=StringType)
yyk_Output.attributes={yyk_Output_id}

# yyk_Baz class attributes and methods
yyk_Baz_zig: Property = Property(name="zig", type=StringType)
yyk_Baz.attributes={yyk_Baz_zig}

# yyk_NamedElement class attributes and methods
yyk_NamedElement_name: Property = Property(name="name", type=StringType)
yyk_NamedElement.attributes={yyk_NamedElement_name}

# yyk_Base class attributes and methods
yyk_Base_id: Property = Property(name="id", type=IntegerType)
yyk_Base.attributes={yyk_Base_id}

# NamedElement class attributes and methods

# yyk_Rel class attributes and methods
yyk_Rel_id: Property = Property(name="id", type=StringType)
yyk_Rel.attributes={yyk_Rel_id}

# yyk_Alias class attributes and methods
yyk_Alias_id: Property = Property(name="id", type=StringType)
yyk_Alias.attributes={yyk_Alias_id}

# yyk_Bar class attributes and methods
yyk_Bar_id: Property = Property(name="id", type=StringType)
yyk_Bar.attributes={yyk_Bar_id}

# yyk_Zing class attributes and methods

# yyk_Bouz class attributes and methods
yyk_Bouz_bil: Property = Property(name="bil", type=StringType)
yyk_Bouz.attributes={yyk_Bouz_bil}

# Baz class attributes and methods

# yyk_Boul class attributes and methods
yyk_Boul_hi: Property = Property(name="hi", type=StringType)
yyk_Boul.attributes={yyk_Boul_hi}

# Relationships
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="1", type=yyk_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=yyk_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos2: BinaryAssociation = BinaryAssociation(
    name="foos2",
    ends={
        Property(name="yyk_Foo", type=yyk_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Base", type=yyk_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ouputs3: BinaryAssociation = BinaryAssociation(
    name="ouputs3",
    ends={
        Property(name="yyk_Output", type=yyk_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Base4", type=yyk_Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baze5: BinaryAssociation = BinaryAssociation(
    name="baze5",
    ends={
        Property(name="yyk_Baz", type=yyk_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Base6", type=yyk_Baz, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bars8: BinaryAssociation = BinaryAssociation(
    name="bars8",
    ends={
        Property(name="yyk_NamedElement9", type=yyk_Bar, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="yyk_Bar", type=yyk_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
rels10: BinaryAssociation = BinaryAssociation(
    name="rels10",
    ends={
        Property(name="yyk_Rel", type=yyk_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_NamedElement11", type=yyk_Rel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing12: BinaryAssociation = BinaryAssociation(
    name="fromThing12",
    ends={
        Property(name="14", type=yyk_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="13", type=yyk_Base, multiplicity=Multiplicity(0, 1))
    }
)
toElement15: BinaryAssociation = BinaryAssociation(
    name="toElement15",
    ends={
        Property(name="yyk_NamedElement16", type=yyk_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Relation", type=yyk_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
aliases7: BinaryAssociation = BinaryAssociation(
    name="aliases7",
    ends={
        Property(name="yyk_Alias", type=yyk_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_NamedElement", type=yyk_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output20: BinaryAssociation = BinaryAssociation(
    name="output20",
    ends={
        Property(name="yyk_Output22", type=yyk_Bar, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Bar21", type=yyk_Output, multiplicity=Multiplicity(0, 1))
    }
)
subRelations18: BinaryAssociation = BinaryAssociation(
    name="subRelations18",
    ends={
        Property(name="yyk_Relation19", type=yyk_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Relation17", type=yyk_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
azing29: BinaryAssociation = BinaryAssociation(
    name="azing29",
    ends={
        Property(name="yyk_Zing", type=yyk_Baz, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Baz30", type=yyk_Zing, multiplicity=Multiplicity(0, 1))
    }
)
src23: BinaryAssociation = BinaryAssociation(
    name="src23",
    ends={
        Property(name="yyk_NamedElement25", type=yyk_Rel, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Rel24", type=yyk_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
trg26: BinaryAssociation = BinaryAssociation(
    name="trg26",
    ends={
        Property(name="yyk_Relation28", type=yyk_Rel, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Rel27", type=yyk_Relation, multiplicity=Multiplicity(0, 1))
    }
)
zings31: BinaryAssociation = BinaryAssociation(
    name="zings31",
    ends={
        Property(name="yyk_Zing32", type=yyk_Bouz, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Bouz", type=yyk_Zing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_yyk_Base_NamedElement = Generalization(general=NamedElement, specific=yyk_Base)
gen_yyk_Relation_NamedElement = Generalization(general=NamedElement, specific=yyk_Relation)
gen_yyk_Baz_NamedElement = Generalization(general=NamedElement, specific=yyk_Baz)
gen_yyk_Bouz_Baz = Generalization(general=Baz, specific=yyk_Bouz)
gen_yyk_Zing_NamedElement = Generalization(general=NamedElement, specific=yyk_Zing)
gen_yyk_Boul_Baz = Generalization(general=Baz, specific=yyk_Boul)

# Domain Model
domain_model = DomainModel(
    name="yyk",
    types={yyk_Relation, yyk_Foo, yyk_Output, yyk_Baz, yyk_NamedElement, yyk_Base, NamedElement, yyk_Rel, yyk_Alias, yyk_Bar, yyk_Zing, yyk_Bouz, Baz, yyk_Boul},
    associations={relations0, foos2, ouputs3, baze5, bars8, rels10, fromThing12, toElement15, aliases7, output20, subRelations18, azing29, src23, trg26, zings31},
    generalizations={gen_yyk_Base_NamedElement, gen_yyk_Relation_NamedElement, gen_yyk_Baz_NamedElement, gen_yyk_Bouz_Baz, gen_yyk_Zing_NamedElement, gen_yyk_Boul_Baz},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)