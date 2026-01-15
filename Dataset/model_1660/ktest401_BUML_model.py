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
ktest401_Thing = Class(name="ktest401::Thing")
ktest401_Article = Class(name="ktest401::Article")
ktest401_World = Class(name="ktest401::World")
ktest401_NamedElement = Class(name="ktest401::NamedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
ktest401_RelatedTo = Class(name="ktest401::RelatedTo")
ktest401_Line = Class(name="ktest401::Line")
ktest401_EClass0 = Class(name="ktest401::EClass0")
ktest401_EClass1 = Class(name="ktest401::EClass1")

# ktest401_Thing class attributes and methods
ktest401_Thing_id: Property = Property(name="id", type=IntegerType)
ktest401_Thing.attributes={ktest401_Thing_id}

# ktest401_Article class attributes and methods
ktest401_Article_aid: Property = Property(name="aid", type=StringType)
ktest401_Article.attributes={ktest401_Article_aid}

# ktest401_World class attributes and methods

# ktest401_NamedElement class attributes and methods
ktest401_NamedElement_name: Property = Property(name="name", type=StringType)
ktest401_NamedElement.attributes={ktest401_NamedElement_name}

# NamedElement class attributes and methods

# ktest401_RelatedTo class attributes and methods
ktest401_RelatedTo_since: Property = Property(name="since", type=StringType)
ktest401_RelatedTo.attributes={ktest401_RelatedTo_since}

# ktest401_Line class attributes and methods
ktest401_Line_quant: Property = Property(name="quant", type=IntegerType)
ktest401_Line_articleAid: Property = Property(name="articleAid", type=StringType)
ktest401_Line.attributes={ktest401_Line_articleAid, ktest401_Line_quant}

# ktest401_EClass0 class attributes and methods

# ktest401_EClass1 class attributes and methods
ktest401_EClass1_foo: Property = Property(name="foo", type=StringType)
ktest401_EClass1_bar: Property = Property(name="bar", type=StringType)
ktest401_EClass1.attributes={ktest401_EClass1_bar, ktest401_EClass1_foo}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="ktest401_Thing", type=ktest401_World, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest401_World", type=ktest401_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
e0s6: BinaryAssociation = BinaryAssociation(
    name="e0s6",
    ends={
        Property(name="ktest401_Thing7", type=ktest401_EClass0, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="ktest401_EClass0", type=ktest401_Thing, multiplicity=Multiplicity(1, 1))
    }
)
e1s1: BinaryAssociation = BinaryAssociation(
    name="e1s1",
    ends={
        Property(name="ktest401_Article", type=ktest401_World, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest401_World2", type=ktest401_Article, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations3: BinaryAssociation = BinaryAssociation(
    name="relations3",
    ends={
        Property(name="RelatedTo", type=ktest401_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=ktest401_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lines4: BinaryAssociation = BinaryAssociation(
    name="lines4",
    ends={
        Property(name="ktest401_Line", type=ktest401_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest401_Thing5", type=ktest401_Line, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
EReference019: BinaryAssociation = BinaryAssociation(
    name="EReference019",
    ends={
        Property(name="ktest401_RelatedTo21", type=ktest401_EClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest401_EClass120", type=ktest401_RelatedTo, multiplicity=Multiplicity(0, 1))
    }
)
fromThing8: BinaryAssociation = BinaryAssociation(
    name="fromThing8",
    ends={
        Property(name="Thing", type=ktest401_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=ktest401_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing9: BinaryAssociation = BinaryAssociation(
    name="toThing9",
    ends={
        Property(name="ktest401_Thing10", type=ktest401_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest401_RelatedTo", type=ktest401_Thing, multiplicity=Multiplicity(0, 1))
    }
)
e1s11: BinaryAssociation = BinaryAssociation(
    name="e1s11",
    ends={
        Property(name="ktest401_EClass1", type=ktest401_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest401_RelatedTo12", type=ktest401_EClass1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src13: BinaryAssociation = BinaryAssociation(
    name="src13",
    ends={
        Property(name="ktest401_Thing15", type=ktest401_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest401_Line14", type=ktest401_Thing, multiplicity=Multiplicity(0, 1))
    }
)
trg16: BinaryAssociation = BinaryAssociation(
    name="trg16",
    ends={
        Property(name="ktest401_Article18", type=ktest401_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest401_Line17", type=ktest401_Article, multiplicity=Multiplicity(0, 1))
    }
)
EReference122: BinaryAssociation = BinaryAssociation(
    name="EReference122",
    ends={
        Property(name="ktest401_EClass024", type=ktest401_EClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest401_EClass123", type=ktest401_EClass0, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ktest401_Thing_NamedElement = Generalization(general=NamedElement, specific=ktest401_Thing)
gen_ktest401_EClass0_NamedElement = Generalization(general=NamedElement, specific=ktest401_EClass0)
gen_ktest401_EClass1_NamedElement = Generalization(general=NamedElement, specific=ktest401_EClass1)
gen_ktest401_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=ktest401_RelatedTo)
gen_ktest401_Line_NamedElement = Generalization(general=NamedElement, specific=ktest401_Line)
gen_ktest401_Article_NamedElement = Generalization(general=NamedElement, specific=ktest401_Article)

# Domain Model
domain_model = DomainModel(
    name="ktest401",
    types={ktest401_Thing, ktest401_Article, ktest401_World, ktest401_NamedElement, NamedElement, ktest401_RelatedTo, ktest401_Line, ktest401_EClass0, ktest401_EClass1},
    associations={things0, e0s6, e1s1, relations3, lines4, EReference019, fromThing8, toThing9, e1s11, src13, trg16, EReference122},
    generalizations={gen_ktest401_Thing_NamedElement, gen_ktest401_EClass0_NamedElement, gen_ktest401_EClass1_NamedElement, gen_ktest401_RelatedTo_NamedElement, gen_ktest401_Line_NamedElement, gen_ktest401_Article_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)