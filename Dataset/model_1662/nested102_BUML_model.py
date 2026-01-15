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
nested102_World = Class(name="nested102::World")
nested102_Thing = Class(name="nested102::Thing")
NamedElement = Class(name="NamedElement")
nested102_RelatedTo = Class(name="nested102::RelatedTo")
nested102_EClass0 = Class(name="nested102::EClass0")
nested102_NamedElement = Class(name="nested102::NamedElement", is_abstract=True)
nested102_EClass1 = Class(name="nested102::EClass1")
nested102_EClass2 = Class(name="nested102::EClass2")
nested102_EClass3 = Class(name="nested102::EClass3")
nested102_EClass4 = Class(name="nested102::EClass4")
nested102_EClass5 = Class(name="nested102::EClass5")
EClass6 = Class(name="EClass6")
nested102_EClass6 = Class(name="nested102::EClass6", is_abstract=True)
EClass7 = Class(name="EClass7")
EClass8 = Class(name="EClass8")
nested102_EClass7 = Class(name="nested102::EClass7", is_abstract=True)
Thing = Class(name="Thing")
nested102_EClass8 = Class(name="nested102::EClass8", is_abstract=True)

# nested102_World class attributes and methods

# nested102_Thing class attributes and methods
nested102_Thing_id: Property = Property(name="id", type=IntegerType)
nested102_Thing.attributes={nested102_Thing_id}

# NamedElement class attributes and methods

# nested102_RelatedTo class attributes and methods
nested102_RelatedTo_since: Property = Property(name="since", type=StringType)
nested102_RelatedTo.attributes={nested102_RelatedTo_since}

# nested102_EClass0 class attributes and methods

# nested102_NamedElement class attributes and methods
nested102_NamedElement_name: Property = Property(name="name", type=StringType)
nested102_NamedElement.attributes={nested102_NamedElement_name}

# nested102_EClass1 class attributes and methods

# nested102_EClass2 class attributes and methods

# nested102_EClass3 class attributes and methods

# nested102_EClass4 class attributes and methods

# nested102_EClass5 class attributes and methods

# EClass6 class attributes and methods

# nested102_EClass6 class attributes and methods

# EClass7 class attributes and methods

# EClass8 class attributes and methods

# nested102_EClass7 class attributes and methods

# Thing class attributes and methods

# nested102_EClass8 class attributes and methods

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="nested102_Thing", type=nested102_World, multiplicity=Multiplicity(1, 1)),
        Property(name="nested102_World", type=nested102_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="RelatedTo", type=nested102_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=nested102_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
EReference02: BinaryAssociation = BinaryAssociation(
    name="EReference02",
    ends={
        Property(name="nested102_EClass0", type=nested102_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="nested102_Thing3", type=nested102_EClass0, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing4: BinaryAssociation = BinaryAssociation(
    name="fromThing4",
    ends={
        Property(name="Thing", type=nested102_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=nested102_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing5: BinaryAssociation = BinaryAssociation(
    name="toThing5",
    ends={
        Property(name="nested102_Thing6", type=nested102_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="nested102_RelatedTo", type=nested102_Thing, multiplicity=Multiplicity(0, 1))
    }
)
ecl17: BinaryAssociation = BinaryAssociation(
    name="ecl17",
    ends={
        Property(name="nested102_EClass1", type=nested102_EClass0, multiplicity=Multiplicity(1, 1)),
        Property(name="nested102_EClass08", type=nested102_EClass1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ecl29: BinaryAssociation = BinaryAssociation(
    name="ecl29",
    ends={
        Property(name="nested102_EClass2", type=nested102_EClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="nested102_EClass110", type=nested102_EClass2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ecl311: BinaryAssociation = BinaryAssociation(
    name="ecl311",
    ends={
        Property(name="nested102_EClass3", type=nested102_EClass2, multiplicity=Multiplicity(1, 1)),
        Property(name="nested102_EClass212", type=nested102_EClass3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ecl413: BinaryAssociation = BinaryAssociation(
    name="ecl413",
    ends={
        Property(name="nested102_EClass4", type=nested102_EClass3, multiplicity=Multiplicity(1, 1)),
        Property(name="nested102_EClass314", type=nested102_EClass4, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ecl515: BinaryAssociation = BinaryAssociation(
    name="ecl515",
    ends={
        Property(name="nested102_EClass5", type=nested102_EClass4, multiplicity=Multiplicity(1, 1)),
        Property(name="nested102_EClass416", type=nested102_EClass5, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_nested102_Thing_NamedElement = Generalization(general=NamedElement, specific=nested102_Thing)
gen_nested102_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=nested102_RelatedTo)
gen_nested102_EClass0_NamedElement = Generalization(general=NamedElement, specific=nested102_EClass0)
gen_nested102_EClass1_NamedElement = Generalization(general=NamedElement, specific=nested102_EClass1)
gen_nested102_EClass2_NamedElement = Generalization(general=NamedElement, specific=nested102_EClass2)
gen_nested102_EClass3_NamedElement = Generalization(general=NamedElement, specific=nested102_EClass3)
gen_nested102_EClass4_NamedElement = Generalization(general=NamedElement, specific=nested102_EClass4)
gen_nested102_EClass5_NamedElement = Generalization(general=NamedElement, specific=nested102_EClass5)
gen_nested102_EClass5_EClass6 = Generalization(general=EClass6, specific=nested102_EClass5)
gen_nested102_EClass6_EClass7 = Generalization(general=EClass7, specific=nested102_EClass6)
gen_nested102_EClass6_EClass8 = Generalization(general=EClass8, specific=nested102_EClass6)
gen_nested102_EClass7_Thing = Generalization(general=Thing, specific=nested102_EClass7)
gen_nested102_EClass8_NamedElement = Generalization(general=NamedElement, specific=nested102_EClass8)

# Domain Model
domain_model = DomainModel(
    name="nested102",
    types={nested102_World, nested102_Thing, NamedElement, nested102_RelatedTo, nested102_EClass0, nested102_NamedElement, nested102_EClass1, nested102_EClass2, nested102_EClass3, nested102_EClass4, nested102_EClass5, EClass6, nested102_EClass6, EClass7, EClass8, nested102_EClass7, Thing, nested102_EClass8},
    associations={things0, relations1, EReference02, fromThing4, toThing5, ecl17, ecl29, ecl311, ecl413, ecl515},
    generalizations={gen_nested102_Thing_NamedElement, gen_nested102_RelatedTo_NamedElement, gen_nested102_EClass0_NamedElement, gen_nested102_EClass1_NamedElement, gen_nested102_EClass2_NamedElement, gen_nested102_EClass3_NamedElement, gen_nested102_EClass4_NamedElement, gen_nested102_EClass5_NamedElement, gen_nested102_EClass5_EClass6, gen_nested102_EClass6_EClass7, gen_nested102_EClass6_EClass8, gen_nested102_EClass7_Thing, gen_nested102_EClass8_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)