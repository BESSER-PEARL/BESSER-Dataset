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
yyg_Boz = Class(name="yyg::Boz")
yyg_Foo = Class(name="yyg::Foo")
yyg_Output = Class(name="yyg::Output")
yyg_Base = Class(name="yyg::Base")
NamedElement = Class(name="NamedElement")
yyg_Rel = Class(name="yyg::Rel")
yyg_Baz = Class(name="yyg::Baz", is_abstract=True)
yyg_NamedElement = Class(name="yyg::NamedElement", is_abstract=True)
yyg_Alias = Class(name="yyg::Alias")
yyg_Bar = Class(name="yyg::Bar")
yyg_Bouz = Class(name="yyg::Bouz")
Baz = Class(name="Baz")
yyg_Zing = Class(name="yyg::Zing")
yyg_Boul = Class(name="yyg::Boul")

# yyg_Boz class attributes and methods
yyg_Boz_since: Property = Property(name="since", type=StringType)
yyg_Boz.attributes={yyg_Boz_since}

# yyg_Foo class attributes and methods
yyg_Foo_id: Property = Property(name="id", type=StringType)
yyg_Foo.attributes={yyg_Foo_id}

# yyg_Output class attributes and methods
yyg_Output_id: Property = Property(name="id", type=StringType)
yyg_Output.attributes={yyg_Output_id}

# yyg_Base class attributes and methods
yyg_Base_id: Property = Property(name="id", type=IntegerType)
yyg_Base.attributes={yyg_Base_id}

# NamedElement class attributes and methods

# yyg_Rel class attributes and methods
yyg_Rel_id: Property = Property(name="id", type=StringType)
yyg_Rel.attributes={yyg_Rel_id}

# yyg_Baz class attributes and methods
yyg_Baz_zig: Property = Property(name="zig", type=StringType)
yyg_Baz.attributes={yyg_Baz_zig}

# yyg_NamedElement class attributes and methods
yyg_NamedElement_name: Property = Property(name="name", type=StringType)
yyg_NamedElement.attributes={yyg_NamedElement_name}

# yyg_Alias class attributes and methods
yyg_Alias_id: Property = Property(name="id", type=StringType)
yyg_Alias.attributes={yyg_Alias_id}

# yyg_Bar class attributes and methods
yyg_Bar_id: Property = Property(name="id", type=StringType)
yyg_Bar.attributes={yyg_Bar_id}

# yyg_Bouz class attributes and methods
yyg_Bouz_bil: Property = Property(name="bil", type=StringType)
yyg_Bouz.attributes={yyg_Bouz_bil}

# Baz class attributes and methods

# yyg_Zing class attributes and methods

# yyg_Boul class attributes and methods
yyg_Boul_hi: Property = Property(name="hi", type=StringType)
yyg_Boul.attributes={yyg_Boul_hi}

# Relationships
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="Boz", type=yyg_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=yyg_Boz, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos1: BinaryAssociation = BinaryAssociation(
    name="foos1",
    ends={
        Property(name="yyg_Foo", type=yyg_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyg_Base", type=yyg_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bars7: BinaryAssociation = BinaryAssociation(
    name="bars7",
    ends={
        Property(name="yyg_NamedElement8", type=yyg_Bar, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="yyg_Bar", type=yyg_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
rels9: BinaryAssociation = BinaryAssociation(
    name="rels9",
    ends={
        Property(name="yyg_Rel", type=yyg_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyg_NamedElement10", type=yyg_Rel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ouputs2: BinaryAssociation = BinaryAssociation(
    name="ouputs2",
    ends={
        Property(name="yyg_Output", type=yyg_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyg_Base3", type=yyg_Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baze4: BinaryAssociation = BinaryAssociation(
    name="baze4",
    ends={
        Property(name="yyg_Baz", type=yyg_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyg_Base5", type=yyg_Baz, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases6: BinaryAssociation = BinaryAssociation(
    name="aliases6",
    ends={
        Property(name="yyg_Alias", type=yyg_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyg_NamedElement", type=yyg_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing11: BinaryAssociation = BinaryAssociation(
    name="fromThing11",
    ends={
        Property(name="Base", type=yyg_Boz, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=yyg_Base, multiplicity=Multiplicity(0, 1))
    }
)
toElement12: BinaryAssociation = BinaryAssociation(
    name="toElement12",
    ends={
        Property(name="yyg_NamedElement13", type=yyg_Boz, multiplicity=Multiplicity(1, 1)),
        Property(name="yyg_Boz", type=yyg_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
subRelations15: BinaryAssociation = BinaryAssociation(
    name="subRelations15",
    ends={
        Property(name="yyg_Boz16", type=yyg_Boz, multiplicity=Multiplicity(1, 1)),
        Property(name="yyg_Boz14", type=yyg_Boz, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output17: BinaryAssociation = BinaryAssociation(
    name="output17",
    ends={
        Property(name="yyg_Output19", type=yyg_Bar, multiplicity=Multiplicity(1, 1)),
        Property(name="yyg_Bar18", type=yyg_Output, multiplicity=Multiplicity(0, 1))
    }
)
src20: BinaryAssociation = BinaryAssociation(
    name="src20",
    ends={
        Property(name="yyg_NamedElement22", type=yyg_Rel, multiplicity=Multiplicity(1, 1)),
        Property(name="yyg_Rel21", type=yyg_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
trg23: BinaryAssociation = BinaryAssociation(
    name="trg23",
    ends={
        Property(name="yyg_Boz25", type=yyg_Rel, multiplicity=Multiplicity(1, 1)),
        Property(name="yyg_Rel24", type=yyg_Boz, multiplicity=Multiplicity(0, 1))
    }
)
azing26: BinaryAssociation = BinaryAssociation(
    name="azing26",
    ends={
        Property(name="yyg_Zing", type=yyg_Baz, multiplicity=Multiplicity(1, 1)),
        Property(name="yyg_Baz27", type=yyg_Zing, multiplicity=Multiplicity(0, 1))
    }
)
zings28: BinaryAssociation = BinaryAssociation(
    name="zings28",
    ends={
        Property(name="yyg_Zing29", type=yyg_Bouz, multiplicity=Multiplicity(1, 1)),
        Property(name="yyg_Bouz", type=yyg_Zing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_yyg_Base_NamedElement = Generalization(general=NamedElement, specific=yyg_Base)
gen_yyg_Boz_NamedElement = Generalization(general=NamedElement, specific=yyg_Boz)
gen_yyg_Baz_NamedElement = Generalization(general=NamedElement, specific=yyg_Baz)
gen_yyg_Bouz_Baz = Generalization(general=Baz, specific=yyg_Bouz)
gen_yyg_Boul_Baz = Generalization(general=Baz, specific=yyg_Boul)
gen_yyg_Zing_NamedElement = Generalization(general=NamedElement, specific=yyg_Zing)

# Domain Model
domain_model = DomainModel(
    name="yyg",
    types={yyg_Boz, yyg_Foo, yyg_Output, yyg_Base, NamedElement, yyg_Rel, yyg_Baz, yyg_NamedElement, yyg_Alias, yyg_Bar, yyg_Bouz, Baz, yyg_Zing, yyg_Boul},
    associations={relations0, foos1, bars7, rels9, ouputs2, baze4, aliases6, fromThing11, toElement12, subRelations15, output17, src20, trg23, azing26, zings28},
    generalizations={gen_yyg_Base_NamedElement, gen_yyg_Boz_NamedElement, gen_yyg_Baz_NamedElement, gen_yyg_Bouz_Baz, gen_yyg_Boul_Baz, gen_yyg_Zing_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)