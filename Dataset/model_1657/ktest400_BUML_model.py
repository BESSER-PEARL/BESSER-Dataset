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
ktest400_World = Class(name="ktest400::World")
ktest400_Thing = Class(name="ktest400::Thing")
ktest400_Article = Class(name="ktest400::Article")
NamedElement = Class(name="NamedElement")
ktest400_RelatedTo = Class(name="ktest400::RelatedTo")
ktest400_Line = Class(name="ktest400::Line")
ktest400_NamedElement = Class(name="ktest400::NamedElement", is_abstract=True)

# ktest400_World class attributes and methods

# ktest400_Thing class attributes and methods
ktest400_Thing_id: Property = Property(name="id", type=IntegerType)
ktest400_Thing.attributes={ktest400_Thing_id}

# ktest400_Article class attributes and methods
ktest400_Article_aid: Property = Property(name="aid", type=StringType)
ktest400_Article.attributes={ktest400_Article_aid}

# NamedElement class attributes and methods

# ktest400_RelatedTo class attributes and methods
ktest400_RelatedTo_since: Property = Property(name="since", type=StringType)
ktest400_RelatedTo.attributes={ktest400_RelatedTo_since}

# ktest400_Line class attributes and methods
ktest400_Line_quant: Property = Property(name="quant", type=IntegerType)
ktest400_Line_articleAid: Property = Property(name="articleAid", type=StringType)
ktest400_Line.attributes={ktest400_Line_quant, ktest400_Line_articleAid}

# ktest400_NamedElement class attributes and methods
ktest400_NamedElement_name: Property = Property(name="name", type=StringType)
ktest400_NamedElement.attributes={ktest400_NamedElement_name}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="ktest400_Thing", type=ktest400_World, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest400_World", type=ktest400_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
e1s1: BinaryAssociation = BinaryAssociation(
    name="e1s1",
    ends={
        Property(name="ktest400_Article", type=ktest400_World, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest400_World2", type=ktest400_Article, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing6: BinaryAssociation = BinaryAssociation(
    name="fromThing6",
    ends={
        Property(name="Thing", type=ktest400_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=ktest400_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing7: BinaryAssociation = BinaryAssociation(
    name="toThing7",
    ends={
        Property(name="ktest400_Thing8", type=ktest400_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest400_RelatedTo", type=ktest400_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relations3: BinaryAssociation = BinaryAssociation(
    name="relations3",
    ends={
        Property(name="RelatedTo", type=ktest400_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=ktest400_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
e0s4: BinaryAssociation = BinaryAssociation(
    name="e0s4",
    ends={
        Property(name="ktest400_Line", type=ktest400_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest400_Thing5", type=ktest400_Line, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src9: BinaryAssociation = BinaryAssociation(
    name="src9",
    ends={
        Property(name="ktest400_Thing11", type=ktest400_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest400_Line10", type=ktest400_Thing, multiplicity=Multiplicity(0, 1))
    }
)
trg12: BinaryAssociation = BinaryAssociation(
    name="trg12",
    ends={
        Property(name="ktest400_Article14", type=ktest400_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="ktest400_Line13", type=ktest400_Article, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ktest400_Thing_NamedElement = Generalization(general=NamedElement, specific=ktest400_Thing)
gen_ktest400_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=ktest400_RelatedTo)
gen_ktest400_Article_NamedElement = Generalization(general=NamedElement, specific=ktest400_Article)
gen_ktest400_Line_NamedElement = Generalization(general=NamedElement, specific=ktest400_Line)

# Domain Model
domain_model = DomainModel(
    name="ktest400",
    types={ktest400_World, ktest400_Thing, ktest400_Article, NamedElement, ktest400_RelatedTo, ktest400_Line, ktest400_NamedElement},
    associations={things0, e1s1, fromThing6, toThing7, relations3, e0s4, src9, trg12},
    generalizations={gen_ktest400_Thing_NamedElement, gen_ktest400_RelatedTo_NamedElement, gen_ktest400_Article_NamedElement, gen_ktest400_Line_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)