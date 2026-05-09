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
yyk_Alias = Class(name="yyk_Alias")
yyk_Bar = Class(name="yyk_Bar")
yyk_Rel = Class(name="yyk_Rel")
yyk_Base = Class(name="yyk_Base")
NamedElement = Class(name="NamedElement")
yyk_Relation = Class(name="yyk_Relation")
yyk_Foo = Class(name="yyk_Foo")
yyk_Output = Class(name="yyk_Output")
yyk_Baz = Class(name="yyk_Baz", is_abstract=True)
yyk_NamedElement = Class(name="yyk_NamedElement", is_abstract=True)
yyk_Zing = Class(name="yyk_Zing")
yyk_Bouz = Class(name="yyk_Bouz")
Baz = Class(name="Baz")
yyk_Boul = Class(name="yyk_Boul")

# yyk_Alias class attributes and methods
yyk_Alias_id: Property = Property(name="id", type=StringType)
yyk_Alias.attributes={yyk_Alias_id}

# yyk_Bar class attributes and methods
yyk_Bar_id: Property = Property(name="id", type=StringType)
yyk_Bar.attributes={yyk_Bar_id}

# yyk_Rel class attributes and methods
yyk_Rel_id: Property = Property(name="id", type=StringType)
yyk_Rel.attributes={yyk_Rel_id}

# yyk_Base class attributes and methods
yyk_Base_id: Property = Property(name="id", type=IntegerType)
yyk_Base.attributes={yyk_Base_id}

# NamedElement class attributes and methods

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

# yyk_Zing class attributes and methods

# yyk_Bouz class attributes and methods
yyk_Bouz_bil: Property = Property(name="bil", type=StringType)
yyk_Bouz.attributes={yyk_Bouz_bil}

# Baz class attributes and methods

# yyk_Boul class attributes and methods
yyk_Boul_hi: Property = Property(name="hi", type=StringType)
yyk_Boul.attributes={yyk_Boul_hi}

# Relationships
aliases6: BinaryAssociation = BinaryAssociation(
    name="aliases6",
    ends={
        Property(name="yyk_Alias", type=yyk_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_NamedElement", type=yyk_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bars7: BinaryAssociation = BinaryAssociation(
    name="bars7",
    ends={
        Property(name="yyk_Bar", type=yyk_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_NamedElement8", type=yyk_Bar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rels9: BinaryAssociation = BinaryAssociation(
    name="rels9",
    ends={
        Property(name="yyk_Rel", type=yyk_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_NamedElement10", type=yyk_Rel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing11: BinaryAssociation = BinaryAssociation(
    name="fromThing11",
    ends={
        Property(name="Base", type=yyk_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=yyk_Base, multiplicity=Multiplicity(0, 1))
    }
)
toElement12: BinaryAssociation = BinaryAssociation(
    name="toElement12",
    ends={
        Property(name="yyk_NamedElement13", type=yyk_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Relation", type=yyk_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
subRelations15: BinaryAssociation = BinaryAssociation(
    name="subRelations15",
    ends={
        Property(name="yyk_Relation16", type=yyk_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Relation14", type=yyk_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="Relation", type=yyk_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=yyk_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos1: BinaryAssociation = BinaryAssociation(
    name="foos1",
    ends={
        Property(name="yyk_Foo", type=yyk_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Base", type=yyk_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ouputs2: BinaryAssociation = BinaryAssociation(
    name="ouputs2",
    ends={
        Property(name="yyk_Output", type=yyk_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Base3", type=yyk_Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baze4: BinaryAssociation = BinaryAssociation(
    name="baze4",
    ends={
        Property(name="yyk_Baz", type=yyk_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Base5", type=yyk_Baz, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trg23: BinaryAssociation = BinaryAssociation(
    name="trg23",
    ends={
        Property(name="yyk_Rel24", type=yyk_Relation, multiplicity=Multiplicity(0, 1)),
        Property(name="yyk_Relation25", type=yyk_Rel, multiplicity=Multiplicity(1, 1))
    }
)
azing26: BinaryAssociation = BinaryAssociation(
    name="azing26",
    ends={
        Property(name="yyk_Zing", type=yyk_Baz, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Baz27", type=yyk_Zing, multiplicity=Multiplicity(0, 1))
    }
)
zings28: BinaryAssociation = BinaryAssociation(
    name="zings28",
    ends={
        Property(name="yyk_Zing29", type=yyk_Bouz, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Bouz", type=yyk_Zing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output17: BinaryAssociation = BinaryAssociation(
    name="output17",
    ends={
        Property(name="yyk_Output19", type=yyk_Bar, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Bar18", type=yyk_Output, multiplicity=Multiplicity(0, 1))
    }
)
src20: BinaryAssociation = BinaryAssociation(
    name="src20",
    ends={
        Property(name="yyk_NamedElement22", type=yyk_Rel, multiplicity=Multiplicity(1, 1)),
        Property(name="yyk_Rel21", type=yyk_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_yyk_Relation_NamedElement = Generalization(general=NamedElement, specific=yyk_Relation)
gen_yyk_Base_NamedElement = Generalization(general=NamedElement, specific=yyk_Base)
gen_yyk_Baz_NamedElement = Generalization(general=NamedElement, specific=yyk_Baz)
gen_yyk_Bouz_Baz = Generalization(general=Baz, specific=yyk_Bouz)
gen_yyk_Boul_Baz = Generalization(general=Baz, specific=yyk_Boul)
gen_yyk_Zing_NamedElement = Generalization(general=NamedElement, specific=yyk_Zing)

# Domain Model
domain_model = DomainModel(
    name="yyk",
    types={yyk_Alias, yyk_Bar, yyk_Rel, yyk_Base, NamedElement, yyk_Relation, yyk_Foo, yyk_Output, yyk_Baz, yyk_NamedElement, yyk_Zing, yyk_Bouz, Baz, yyk_Boul},
    associations={aliases6, bars7, rels9, fromThing11, toElement12, subRelations15, relations0, foos1, ouputs2, baze4, trg23, azing26, zings28, output17, src20},
    generalizations={gen_yyk_Relation_NamedElement, gen_yyk_Base_NamedElement, gen_yyk_Baz_NamedElement, gen_yyk_Bouz_Baz, gen_yyk_Boul_Baz, gen_yyk_Zing_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)