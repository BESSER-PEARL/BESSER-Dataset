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
nested103_Thing = Class(name="nested103::Thing")
nested103_EClass10 = Class(name="nested103::EClass10")
NamedElement = Class(name="NamedElement")
nested103_RelatedTo = Class(name="nested103::RelatedTo")
nested103_World = Class(name="nested103::World")
nested103_EClass0 = Class(name="nested103::EClass0")
nested103_NamedElement = Class(name="nested103::NamedElement", is_abstract=True)
nested103_EClass1 = Class(name="nested103::EClass1")
nested103_EClass2 = Class(name="nested103::EClass2")
nested103_EClass3 = Class(name="nested103::EClass3")
nested103_EClass4 = Class(name="nested103::EClass4")
nested103_EClass5 = Class(name="nested103::EClass5")
EClass6 = Class(name="EClass6")
nested103_EClass6 = Class(name="nested103::EClass6", is_abstract=True)
EClass7 = Class(name="EClass7")
EClass8 = Class(name="EClass8")
nested103_EClass9 = Class(name="nested103::EClass9", is_abstract=True)
EClass11 = Class(name="EClass11")
EClass12 = Class(name="EClass12")
nested103_EClass13 = Class(name="nested103::EClass13")
EClass9 = Class(name="EClass9")
nested103_EClass11 = Class(name="nested103::EClass11", is_abstract=True)
nested103_EClass7 = Class(name="nested103::EClass7", is_abstract=True)
Thing = Class(name="Thing")
nested103_EClass8 = Class(name="nested103::EClass8", is_abstract=True)
nested103_EClass12 = Class(name="nested103::EClass12", is_abstract=True)

# nested103_Thing class attributes and methods
nested103_Thing_id: Property = Property(name="id", type=IntegerType)
nested103_Thing.attributes={nested103_Thing_id}

# nested103_EClass10 class attributes and methods

# NamedElement class attributes and methods

# nested103_RelatedTo class attributes and methods
nested103_RelatedTo_since: Property = Property(name="since", type=StringType)
nested103_RelatedTo.attributes={nested103_RelatedTo_since}

# nested103_World class attributes and methods

# nested103_EClass0 class attributes and methods

# nested103_NamedElement class attributes and methods
nested103_NamedElement_name: Property = Property(name="name", type=StringType)
nested103_NamedElement.attributes={nested103_NamedElement_name}

# nested103_EClass1 class attributes and methods

# nested103_EClass2 class attributes and methods

# nested103_EClass3 class attributes and methods

# nested103_EClass4 class attributes and methods

# nested103_EClass5 class attributes and methods

# EClass6 class attributes and methods

# nested103_EClass6 class attributes and methods

# EClass7 class attributes and methods

# EClass8 class attributes and methods

# nested103_EClass9 class attributes and methods
nested103_EClass9_name: Property = Property(name="name", type=StringType)
nested103_EClass9.attributes={nested103_EClass9_name}

# EClass11 class attributes and methods

# EClass12 class attributes and methods

# nested103_EClass13 class attributes and methods

# EClass9 class attributes and methods

# nested103_EClass11 class attributes and methods

# nested103_EClass7 class attributes and methods

# Thing class attributes and methods

# nested103_EClass8 class attributes and methods

# nested103_EClass12 class attributes and methods

# Relationships
things0: BinaryAssociation = BinaryAssociation(
    name="things0",
    ends={
        Property(name="nested103_Thing", type=nested103_World, multiplicity=Multiplicity(1, 1)),
        Property(name="nested103_World", type=nested103_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eef01: BinaryAssociation = BinaryAssociation(
    name="eef01",
    ends={
        Property(name="nested103_EClass10", type=nested103_World, multiplicity=Multiplicity(1, 1)),
        Property(name="nested103_World2", type=nested103_EClass10, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing6: BinaryAssociation = BinaryAssociation(
    name="fromThing6",
    ends={
        Property(name="Thing", type=nested103_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=nested103_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relations3: BinaryAssociation = BinaryAssociation(
    name="relations3",
    ends={
        Property(name="RelatedTo", type=nested103_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=nested103_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
EReference04: BinaryAssociation = BinaryAssociation(
    name="EReference04",
    ends={
        Property(name="nested103_EClass0", type=nested103_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="nested103_Thing5", type=nested103_EClass0, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ecl19: BinaryAssociation = BinaryAssociation(
    name="ecl19",
    ends={
        Property(name="nested103_EClass1", type=nested103_EClass0, multiplicity=Multiplicity(1, 1)),
        Property(name="nested103_EClass010", type=nested103_EClass1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ecl211: BinaryAssociation = BinaryAssociation(
    name="ecl211",
    ends={
        Property(name="nested103_EClass2", type=nested103_EClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="nested103_EClass112", type=nested103_EClass2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toThing7: BinaryAssociation = BinaryAssociation(
    name="toThing7",
    ends={
        Property(name="nested103_Thing8", type=nested103_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="nested103_RelatedTo", type=nested103_Thing, multiplicity=Multiplicity(0, 1))
    }
)
ecl313: BinaryAssociation = BinaryAssociation(
    name="ecl313",
    ends={
        Property(name="nested103_EClass3", type=nested103_EClass2, multiplicity=Multiplicity(1, 1)),
        Property(name="nested103_EClass214", type=nested103_EClass3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ecl415: BinaryAssociation = BinaryAssociation(
    name="ecl415",
    ends={
        Property(name="nested103_EClass4", type=nested103_EClass3, multiplicity=Multiplicity(1, 1)),
        Property(name="nested103_EClass316", type=nested103_EClass4, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ecl517: BinaryAssociation = BinaryAssociation(
    name="ecl517",
    ends={
        Property(name="nested103_EClass5", type=nested103_EClass4, multiplicity=Multiplicity(1, 1)),
        Property(name="nested103_EClass418", type=nested103_EClass5, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ecl1319: BinaryAssociation = BinaryAssociation(
    name="ecl1319",
    ends={
        Property(name="nested103_EClass13", type=nested103_EClass9, multiplicity=Multiplicity(1, 1)),
        Property(name="nested103_EClass9", type=nested103_EClass13, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_nested103_Thing_NamedElement = Generalization(general=NamedElement, specific=nested103_Thing)
gen_nested103_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=nested103_RelatedTo)
gen_nested103_EClass1_NamedElement = Generalization(general=NamedElement, specific=nested103_EClass1)
gen_nested103_EClass2_NamedElement = Generalization(general=NamedElement, specific=nested103_EClass2)
gen_nested103_EClass0_NamedElement = Generalization(general=NamedElement, specific=nested103_EClass0)
gen_nested103_EClass3_NamedElement = Generalization(general=NamedElement, specific=nested103_EClass3)
gen_nested103_EClass4_NamedElement = Generalization(general=NamedElement, specific=nested103_EClass4)
gen_nested103_EClass5_NamedElement = Generalization(general=NamedElement, specific=nested103_EClass5)
gen_nested103_EClass5_EClass6 = Generalization(general=EClass6, specific=nested103_EClass5)
gen_nested103_EClass6_EClass7 = Generalization(general=EClass7, specific=nested103_EClass6)
gen_nested103_EClass6_EClass8 = Generalization(general=EClass8, specific=nested103_EClass6)
gen_nested103_EClass9_EClass11 = Generalization(general=EClass11, specific=nested103_EClass9)
gen_nested103_EClass9_EClass12 = Generalization(general=EClass12, specific=nested103_EClass9)
gen_nested103_EClass10_EClass9 = Generalization(general=EClass9, specific=nested103_EClass10)
gen_nested103_EClass7_Thing = Generalization(general=Thing, specific=nested103_EClass7)
gen_nested103_EClass8_NamedElement = Generalization(general=NamedElement, specific=nested103_EClass8)

# Domain Model
domain_model = DomainModel(
    name="nested103",
    types={nested103_Thing, nested103_EClass10, NamedElement, nested103_RelatedTo, nested103_World, nested103_EClass0, nested103_NamedElement, nested103_EClass1, nested103_EClass2, nested103_EClass3, nested103_EClass4, nested103_EClass5, EClass6, nested103_EClass6, EClass7, EClass8, nested103_EClass9, EClass11, EClass12, nested103_EClass13, EClass9, nested103_EClass11, nested103_EClass7, Thing, nested103_EClass8, nested103_EClass12},
    associations={things0, eef01, fromThing6, relations3, EReference04, ecl19, ecl211, toThing7, ecl313, ecl415, ecl517, ecl1319},
    generalizations={gen_nested103_Thing_NamedElement, gen_nested103_RelatedTo_NamedElement, gen_nested103_EClass1_NamedElement, gen_nested103_EClass2_NamedElement, gen_nested103_EClass0_NamedElement, gen_nested103_EClass3_NamedElement, gen_nested103_EClass4_NamedElement, gen_nested103_EClass5_NamedElement, gen_nested103_EClass5_EClass6, gen_nested103_EClass6_EClass7, gen_nested103_EClass6_EClass8, gen_nested103_EClass9_EClass11, gen_nested103_EClass9_EClass12, gen_nested103_EClass10_EClass9, gen_nested103_EClass7_Thing, gen_nested103_EClass8_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)