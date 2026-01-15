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
simpleworld101_Relations = Class(name="simpleworld101::Relations")
simpleworld101_Element = Class(name="simpleworld101::Element")
simpleworld101_Thing = Class(name="simpleworld101::Thing")
Named = Class(name="Named")
simpleworld101_Person = Class(name="simpleworld101::Person")
simpleworld101_World = Class(name="simpleworld101::World")
simpleworld101_Named = Class(name="simpleworld101::Named", is_abstract=True)
simpleworld101_Part = Class(name="simpleworld101::Part")

# simpleworld101_Relations class attributes and methods
simpleworld101_Relations_since: Property = Property(name="since", type=IntegerType)
simpleworld101_Relations.attributes={simpleworld101_Relations_since}

# simpleworld101_Element class attributes and methods
simpleworld101_Element_description: Property = Property(name="description", type=StringType)
simpleworld101_Element.attributes={simpleworld101_Element_description}

# simpleworld101_Thing class attributes and methods

# Named class attributes and methods

# simpleworld101_Person class attributes and methods
simpleworld101_Person_name: Property = Property(name="name", type=StringType)
simpleworld101_Person_foreName: Property = Property(name="foreName", type=StringType)
simpleworld101_Person.attributes={simpleworld101_Person_name, simpleworld101_Person_foreName}

# simpleworld101_World class attributes and methods

# simpleworld101_Named class attributes and methods
simpleworld101_Named_name: Property = Property(name="name", type=StringType)
simpleworld101_Named.attributes={simpleworld101_Named_name}

# simpleworld101_Part class attributes and methods
simpleworld101_Part_content: Property = Property(name="content", type=StringType)
simpleworld101_Part_id: Property = Property(name="id", type=IntegerType)
simpleworld101_Part.attributes={simpleworld101_Part_id, simpleworld101_Part_content}

# Relationships
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="simpleworld101_Relations", type=simpleworld101_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld101_Person", type=simpleworld101_Relations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="simpleworld101_Element", type=simpleworld101_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld101_Person2", type=simpleworld101_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thing3: BinaryAssociation = BinaryAssociation(
    name="thing3",
    ends={
        Property(name="simpleworld101_Thing", type=simpleworld101_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld101_Person4", type=simpleworld101_Thing, multiplicity=Multiplicity(0, 1))
    }
)
things5: BinaryAssociation = BinaryAssociation(
    name="things5",
    ends={
        Property(name="Thing", type=simpleworld101_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons", type=simpleworld101_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
parts12: BinaryAssociation = BinaryAssociation(
    name="parts12",
    ends={
        Property(name="simpleworld101_Part14", type=simpleworld101_Relations, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld101_Relations13", type=simpleworld101_Part, multiplicity=Multiplicity(0, 1))
    }
)
persons15: BinaryAssociation = BinaryAssociation(
    name="persons15",
    ends={
        Property(name="simpleworld101_Person16", type=simpleworld101_World, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld101_World", type=simpleworld101_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
things17: BinaryAssociation = BinaryAssociation(
    name="things17",
    ends={
        Property(name="simpleworld101_Thing19", type=simpleworld101_World, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld101_World18", type=simpleworld101_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components6: BinaryAssociation = BinaryAssociation(
    name="components6",
    ends={
        Property(name="simpleworld101_Part", type=simpleworld101_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld101_Thing7", type=simpleworld101_Part, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
persons8: BinaryAssociation = BinaryAssociation(
    name="persons8",
    ends={
        Property(name="Person", type=simpleworld101_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="things", type=simpleworld101_Person, multiplicity=Multiplicity(0, 9999))
    }
)
parent10: BinaryAssociation = BinaryAssociation(
    name="parent10",
    ends={
        Property(name="simpleworld101_Thing11", type=simpleworld101_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld101_Thing9", type=simpleworld101_Thing, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simpleworld101_Thing_Named = Generalization(general=Named, specific=simpleworld101_Thing)
gen_simpleworld101_World_Named = Generalization(general=Named, specific=simpleworld101_World)
gen_simpleworld101_Part_Named = Generalization(general=Named, specific=simpleworld101_Part)

# Domain Model
domain_model = DomainModel(
    name="simpleworld101",
    types={simpleworld101_Relations, simpleworld101_Element, simpleworld101_Thing, Named, simpleworld101_Person, simpleworld101_World, simpleworld101_Named, simpleworld101_Part},
    associations={relations0, elements1, thing3, things5, parts12, persons15, things17, components6, persons8, parent10},
    generalizations={gen_simpleworld101_Thing_Named, gen_simpleworld101_World_Named, gen_simpleworld101_Part_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)