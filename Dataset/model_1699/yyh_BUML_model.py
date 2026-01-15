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
yyh_Base = Class(name="yyh::Base")
NamedElement = Class(name="NamedElement")
yyh_NamedElement = Class(name="yyh::NamedElement", is_abstract=True)
yyh_Alias = Class(name="yyh::Alias")
yyh_Bar = Class(name="yyh::Bar")
yyh_Boz = Class(name="yyh::Boz")
yyh_Foo = Class(name="yyh::Foo")
yyh_Output = Class(name="yyh::Output")
yyh_Baz = Class(name="yyh::Baz", is_abstract=True)
yyh_Rel = Class(name="yyh::Rel")
yyh_Zing = Class(name="yyh::Zing")
yyh_Bouz = Class(name="yyh::Bouz")
Baz = Class(name="Baz")
yyh_Boul = Class(name="yyh::Boul")

# yyh_Base class attributes and methods
yyh_Base_id: Property = Property(name="id", type=IntegerType)
yyh_Base.attributes={yyh_Base_id}

# NamedElement class attributes and methods

# yyh_NamedElement class attributes and methods
yyh_NamedElement_name: Property = Property(name="name", type=StringType)
yyh_NamedElement.attributes={yyh_NamedElement_name}

# yyh_Alias class attributes and methods
yyh_Alias_id: Property = Property(name="id", type=StringType)
yyh_Alias.attributes={yyh_Alias_id}

# yyh_Bar class attributes and methods
yyh_Bar_id: Property = Property(name="id", type=StringType)
yyh_Bar.attributes={yyh_Bar_id}

# yyh_Boz class attributes and methods
yyh_Boz_since: Property = Property(name="since", type=StringType)
yyh_Boz.attributes={yyh_Boz_since}

# yyh_Foo class attributes and methods
yyh_Foo_id: Property = Property(name="id", type=StringType)
yyh_Foo.attributes={yyh_Foo_id}

# yyh_Output class attributes and methods
yyh_Output_id: Property = Property(name="id", type=StringType)
yyh_Output.attributes={yyh_Output_id}

# yyh_Baz class attributes and methods
yyh_Baz_zig: Property = Property(name="zig", type=StringType)
yyh_Baz.attributes={yyh_Baz_zig}

# yyh_Rel class attributes and methods
yyh_Rel_id: Property = Property(name="id", type=StringType)
yyh_Rel.attributes={yyh_Rel_id}

# yyh_Zing class attributes and methods

# yyh_Bouz class attributes and methods
yyh_Bouz_bil: Property = Property(name="bil", type=StringType)
yyh_Bouz.attributes={yyh_Bouz_bil}

# Baz class attributes and methods

# yyh_Boul class attributes and methods
yyh_Boul_hi: Property = Property(name="hi", type=StringType)
yyh_Boul.attributes={yyh_Boul_hi}

# Relationships
aliases6: BinaryAssociation = BinaryAssociation(
    name="aliases6",
    ends={
        Property(name="yyh_Alias", type=yyh_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_NamedElement", type=yyh_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bars7: BinaryAssociation = BinaryAssociation(
    name="bars7",
    ends={
        Property(name="yyh_Bar", type=yyh_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_NamedElement8", type=yyh_Bar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="Boz", type=yyh_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=yyh_Boz, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos1: BinaryAssociation = BinaryAssociation(
    name="foos1",
    ends={
        Property(name="yyh_Foo", type=yyh_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_Base", type=yyh_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ouputs2: BinaryAssociation = BinaryAssociation(
    name="ouputs2",
    ends={
        Property(name="yyh_Output", type=yyh_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_Base3", type=yyh_Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baze4: BinaryAssociation = BinaryAssociation(
    name="baze4",
    ends={
        Property(name="yyh_Baz", type=yyh_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_Base5", type=yyh_Baz, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subRelations15: BinaryAssociation = BinaryAssociation(
    name="subRelations15",
    ends={
        Property(name="yyh_Boz16", type=yyh_Boz, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_Boz14", type=yyh_Boz, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rels9: BinaryAssociation = BinaryAssociation(
    name="rels9",
    ends={
        Property(name="yyh_Rel", type=yyh_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_NamedElement10", type=yyh_Rel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing11: BinaryAssociation = BinaryAssociation(
    name="fromThing11",
    ends={
        Property(name="Base", type=yyh_Boz, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=yyh_Base, multiplicity=Multiplicity(0, 1))
    }
)
toElement12: BinaryAssociation = BinaryAssociation(
    name="toElement12",
    ends={
        Property(name="yyh_NamedElement13", type=yyh_Boz, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_Boz", type=yyh_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
trg23: BinaryAssociation = BinaryAssociation(
    name="trg23",
    ends={
        Property(name="yyh_Boz25", type=yyh_Rel, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_Rel24", type=yyh_Boz, multiplicity=Multiplicity(0, 1))
    }
)
output17: BinaryAssociation = BinaryAssociation(
    name="output17",
    ends={
        Property(name="yyh_Output19", type=yyh_Bar, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_Bar18", type=yyh_Output, multiplicity=Multiplicity(0, 1))
    }
)
src20: BinaryAssociation = BinaryAssociation(
    name="src20",
    ends={
        Property(name="yyh_NamedElement22", type=yyh_Rel, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_Rel21", type=yyh_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
azing26: BinaryAssociation = BinaryAssociation(
    name="azing26",
    ends={
        Property(name="yyh_Zing", type=yyh_Baz, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_Baz27", type=yyh_Zing, multiplicity=Multiplicity(0, 1))
    }
)
zings28: BinaryAssociation = BinaryAssociation(
    name="zings28",
    ends={
        Property(name="yyh_Zing29", type=yyh_Bouz, multiplicity=Multiplicity(1, 1)),
        Property(name="yyh_Bouz", type=yyh_Zing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_yyh_Base_NamedElement = Generalization(general=NamedElement, specific=yyh_Base)
gen_yyh_Boz_NamedElement = Generalization(general=NamedElement, specific=yyh_Boz)
gen_yyh_Baz_NamedElement = Generalization(general=NamedElement, specific=yyh_Baz)
gen_yyh_Zing_NamedElement = Generalization(general=NamedElement, specific=yyh_Zing)
gen_yyh_Bouz_Baz = Generalization(general=Baz, specific=yyh_Bouz)
gen_yyh_Boul_Baz = Generalization(general=Baz, specific=yyh_Boul)

# Domain Model
domain_model = DomainModel(
    name="yyh",
    types={yyh_Base, NamedElement, yyh_NamedElement, yyh_Alias, yyh_Bar, yyh_Boz, yyh_Foo, yyh_Output, yyh_Baz, yyh_Rel, yyh_Zing, yyh_Bouz, Baz, yyh_Boul},
    associations={aliases6, bars7, relations0, foos1, ouputs2, baze4, subRelations15, rels9, fromThing11, toElement12, trg23, output17, src20, azing26, zings28},
    generalizations={gen_yyh_Base_NamedElement, gen_yyh_Boz_NamedElement, gen_yyh_Baz_NamedElement, gen_yyh_Zing_NamedElement, gen_yyh_Bouz_Baz, gen_yyh_Boul_Baz},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)