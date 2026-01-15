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
hello122_Base = Class(name="hello122::Base")
hello122_Thing = Class(name="hello122::Thing")
hello122_Classoc = Class(name="hello122::Classoc")
hello122_Top = Class(name="hello122::Top")
NamedElement = Class(name="NamedElement")
hello122_Third = Class(name="hello122::Third")
hello122_RelatedTo = Class(name="hello122::RelatedTo")
hello122_NamedElement = Class(name="hello122::NamedElement", is_abstract=True)
hello122_Clazoc = Class(name="hello122::Clazoc")
hello122_Alias = Class(name="hello122::Alias")
hello122_Child = Class(name="hello122::Child")

# hello122_Base class attributes and methods

# hello122_Thing class attributes and methods
hello122_Thing_id: Property = Property(name="id", type=IntegerType)
hello122_Thing.attributes={hello122_Thing_id}

# hello122_Classoc class attributes and methods
hello122_Classoc_id: Property = Property(name="id", type=StringType)
hello122_Classoc.attributes={hello122_Classoc_id}

# hello122_Top class attributes and methods
hello122_Top_id: Property = Property(name="id", type=StringType)
hello122_Top.attributes={hello122_Top_id}

# NamedElement class attributes and methods

# hello122_Third class attributes and methods
hello122_Third_id: Property = Property(name="id", type=StringType)
hello122_Third.attributes={hello122_Third_id}

# hello122_RelatedTo class attributes and methods
hello122_RelatedTo_since: Property = Property(name="since", type=StringType)
hello122_RelatedTo.attributes={hello122_RelatedTo_since}

# hello122_NamedElement class attributes and methods
hello122_NamedElement_name: Property = Property(name="name", type=StringType)
hello122_NamedElement.attributes={hello122_NamedElement_name}

# hello122_Clazoc class attributes and methods

# hello122_Alias class attributes and methods
hello122_Alias_id: Property = Property(name="id", type=StringType)
hello122_Alias.attributes={hello122_Alias_id}

# hello122_Child class attributes and methods
hello122_Child_id: Property = Property(name="id", type=StringType)
hello122_Child.attributes={hello122_Child_id}

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="hello122_Thing", type=hello122_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Base", type=hello122_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classocs1: BinaryAssociation = BinaryAssociation(
    name="classocs1",
    ends={
        Property(name="hello122_Classoc", type=hello122_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Base2", type=hello122_Classoc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tops5: BinaryAssociation = BinaryAssociation(
    name="tops5",
    ends={
        Property(name="hello122_Top", type=hello122_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Base6", type=hello122_Top, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos7: BinaryAssociation = BinaryAssociation(
    name="foos7",
    ends={
        Property(name="hello122_Third", type=hello122_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Thing8", type=hello122_Third, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classocs9: BinaryAssociation = BinaryAssociation(
    name="classocs9",
    ends={
        Property(name="hello122_Classoc11", type=hello122_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Thing10", type=hello122_Classoc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations12: BinaryAssociation = BinaryAssociation(
    name="relations12",
    ends={
        Property(name="hello122_RelatedTo", type=hello122_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Thing13", type=hello122_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clazocs3: BinaryAssociation = BinaryAssociation(
    name="clazocs3",
    ends={
        Property(name="hello122_Clazoc", type=hello122_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Base4", type=hello122_Clazoc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases14: BinaryAssociation = BinaryAssociation(
    name="aliases14",
    ends={
        Property(name="hello122_Alias", type=hello122_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_NamedElement", type=hello122_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing15: BinaryAssociation = BinaryAssociation(
    name="fromThing15",
    ends={
        Property(name="hello122_Thing17", type=hello122_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_RelatedTo16", type=hello122_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing18: BinaryAssociation = BinaryAssociation(
    name="toThing18",
    ends={
        Property(name="hello122_Thing20", type=hello122_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_RelatedTo19", type=hello122_Thing, multiplicity=Multiplicity(0, 1))
    }
)
third21: BinaryAssociation = BinaryAssociation(
    name="third21",
    ends={
        Property(name="hello122_Third23", type=hello122_Classoc, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Classoc22", type=hello122_Third, multiplicity=Multiplicity(0, 1))
    }
)
base24: BinaryAssociation = BinaryAssociation(
    name="base24",
    ends={
        Property(name="hello122_Base26", type=hello122_Classoc, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Classoc25", type=hello122_Base, multiplicity=Multiplicity(0, 1))
    }
)
thing27: BinaryAssociation = BinaryAssociation(
    name="thing27",
    ends={
        Property(name="hello122_Thing29", type=hello122_Classoc, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Classoc28", type=hello122_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing30: BinaryAssociation = BinaryAssociation(
    name="toThing30",
    ends={
        Property(name="hello122_Thing32", type=hello122_Clazoc, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Clazoc31", type=hello122_Thing, multiplicity=Multiplicity(0, 1))
    }
)
fromThird33: BinaryAssociation = BinaryAssociation(
    name="fromThird33",
    ends={
        Property(name="hello122_Third35", type=hello122_Clazoc, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Clazoc34", type=hello122_Third, multiplicity=Multiplicity(0, 1))
    }
)
childs36: BinaryAssociation = BinaryAssociation(
    name="childs36",
    ends={
        Property(name="hello122_Child", type=hello122_Top, multiplicity=Multiplicity(1, 1)),
        Property(name="hello122_Top37", type=hello122_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_hello122_Thing_NamedElement = Generalization(general=NamedElement, specific=hello122_Thing)
gen_hello122_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=hello122_RelatedTo)
gen_hello122_Clazoc_NamedElement = Generalization(general=NamedElement, specific=hello122_Clazoc)

# Domain Model
domain_model = DomainModel(
    name="hello122",
    types={hello122_Base, hello122_Thing, hello122_Classoc, hello122_Top, NamedElement, hello122_Third, hello122_RelatedTo, hello122_NamedElement, hello122_Clazoc, hello122_Alias, hello122_Child},
    associations={things0, classocs1, tops5, foos7, classocs9, relations12, clazocs3, aliases14, fromThing15, toThing18, third21, base24, thing27, toThing30, fromThird33, childs36},
    generalizations={gen_hello122_Thing_NamedElement, gen_hello122_RelatedTo_NamedElement, gen_hello122_Clazoc_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)