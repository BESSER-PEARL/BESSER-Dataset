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
NamedElement = Class(name="NamedElement")
hello121_Base = Class(name="hello121::Base")
hello121_Thing = Class(name="hello121::Thing")
hello121_Classoc = Class(name="hello121::Classoc")
hello121_Alias = Class(name="hello121::Alias")
hello121_RelatedTo = Class(name="hello121::RelatedTo")
hello121_Third = Class(name="hello121::Third")
hello121_NamedElement = Class(name="hello121::NamedElement", is_abstract=True)

# NamedElement class attributes and methods

# hello121_Base class attributes and methods

# hello121_Thing class attributes and methods
hello121_Thing_id: Property = Property(name="id", type=IntegerType)
hello121_Thing.attributes={hello121_Thing_id}

# hello121_Classoc class attributes and methods
hello121_Classoc_id: Property = Property(name="id", type=StringType)
hello121_Classoc.attributes={hello121_Classoc_id}

# hello121_Alias class attributes and methods
hello121_Alias_id: Property = Property(name="id", type=StringType)
hello121_Alias.attributes={hello121_Alias_id}

# hello121_RelatedTo class attributes and methods
hello121_RelatedTo_since: Property = Property(name="since", type=StringType)
hello121_RelatedTo.attributes={hello121_RelatedTo_since}

# hello121_Third class attributes and methods
hello121_Third_id: Property = Property(name="id", type=StringType)
hello121_Third.attributes={hello121_Third_id}

# hello121_NamedElement class attributes and methods
hello121_NamedElement_name: Property = Property(name="name", type=StringType)
hello121_NamedElement.attributes={hello121_NamedElement_name}

# Relationships
classocs1: BinaryAssociation = BinaryAssociation(
    name="classocs1",
    ends={
        Property(name="hello121_Classoc", type=hello121_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="hello121_Base2", type=hello121_Classoc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="hello121_Thing", type=hello121_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="hello121_Base", type=hello121_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases9: BinaryAssociation = BinaryAssociation(
    name="aliases9",
    ends={
        Property(name="hello121_Alias", type=hello121_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="hello121_NamedElement", type=hello121_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations3: BinaryAssociation = BinaryAssociation(
    name="relations3",
    ends={
        Property(name="RelatedTo", type=hello121_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=hello121_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos4: BinaryAssociation = BinaryAssociation(
    name="foos4",
    ends={
        Property(name="hello121_Third", type=hello121_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="hello121_Thing5", type=hello121_Third, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classocs6: BinaryAssociation = BinaryAssociation(
    name="classocs6",
    ends={
        Property(name="hello121_Classoc8", type=hello121_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="hello121_Thing7", type=hello121_Classoc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
third13: BinaryAssociation = BinaryAssociation(
    name="third13",
    ends={
        Property(name="hello121_Third15", type=hello121_Classoc, multiplicity=Multiplicity(1, 1)),
        Property(name="hello121_Classoc14", type=hello121_Third, multiplicity=Multiplicity(0, 1))
    }
)
base16: BinaryAssociation = BinaryAssociation(
    name="base16",
    ends={
        Property(name="hello121_Base18", type=hello121_Classoc, multiplicity=Multiplicity(1, 1)),
        Property(name="hello121_Classoc17", type=hello121_Base, multiplicity=Multiplicity(0, 1))
    }
)
fromThing10: BinaryAssociation = BinaryAssociation(
    name="fromThing10",
    ends={
        Property(name="Thing", type=hello121_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=hello121_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing11: BinaryAssociation = BinaryAssociation(
    name="toThing11",
    ends={
        Property(name="hello121_Thing12", type=hello121_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="hello121_RelatedTo", type=hello121_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_hello121_Thing_NamedElement = Generalization(general=NamedElement, specific=hello121_Thing)
gen_hello121_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=hello121_RelatedTo)

# Domain Model
domain_model = DomainModel(
    name="hello121",
    types={NamedElement, hello121_Base, hello121_Thing, hello121_Classoc, hello121_Alias, hello121_RelatedTo, hello121_Third, hello121_NamedElement},
    associations={classocs1, things0, aliases9, relations3, foos4, classocs6, third13, base16, fromThing10, toThing11},
    generalizations={gen_hello121_Thing_NamedElement, gen_hello121_RelatedTo_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)