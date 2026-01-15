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

# Enumerations
Bz387752_Enum: Enumeration = Enumeration(
    name="Bz387752_Enum",
    literals={
            EnumerationLiteral(name="VAL0"),
			EnumerationLiteral(name="VAL1")
    }
)

# Classes
HibernateTest_Bz387752_Main = Class(name="HibernateTest::Bz387752::Main")
HibernateTest_Bz356181_Main = Class(name="HibernateTest::Bz356181::Main")
HibernateTest_Bz356181_Transient = Class(name="HibernateTest::Bz356181::Transient")
HibernateTest_Bz356181_NonTransient = Class(name="HibernateTest::Bz356181::NonTransient")
HibernateTest_Bz398057A = Class(name="HibernateTest::Bz398057A")
HibernateTest_Bz380987_Group = Class(name="HibernateTest::Bz380987::Group")
HibernateTest_Bz380987_Person = Class(name="HibernateTest::Bz380987::Person")
HibernateTest_Bz380987_Place = Class(name="HibernateTest::Bz380987::Place")
HibernateTest_Bz397682C = Class(name="HibernateTest::Bz397682C")
HibernateTest_Bz398057B = Class(name="HibernateTest::Bz398057B")
HibernateTest_Bz398057A1 = Class(name="HibernateTest::Bz398057A1")
Bz398057A = Class(name="Bz398057A")
HibernateTest_Bz398057B1 = Class(name="HibernateTest::Bz398057B1")
Bz398057B = Class(name="Bz398057B")
HibernateTest_Bz397682P = Class(name="HibernateTest::Bz397682P")

# HibernateTest_Bz387752_Main class attributes and methods
HibernateTest_Bz387752_Main_strUnsettable: Property = Property(name="strUnsettable", type=StringType)
HibernateTest_Bz387752_Main_strSettable: Property = Property(name="strSettable", type=StringType)
HibernateTest_Bz387752_Main_enumSettable: Property = Property(name="enumSettable", type=StringType)
HibernateTest_Bz387752_Main_enumUnsettable: Property = Property(name="enumUnsettable", type=StringType)
HibernateTest_Bz387752_Main.attributes={HibernateTest_Bz387752_Main_strUnsettable, HibernateTest_Bz387752_Main_strSettable, HibernateTest_Bz387752_Main_enumUnsettable, HibernateTest_Bz387752_Main_enumSettable}

# HibernateTest_Bz356181_Main class attributes and methods
HibernateTest_Bz356181_Main_transient: Property = Property(name="transient", type=StringType)
HibernateTest_Bz356181_Main_nonTransient: Property = Property(name="nonTransient", type=StringType)
HibernateTest_Bz356181_Main.attributes={HibernateTest_Bz356181_Main_nonTransient, HibernateTest_Bz356181_Main_transient}

# HibernateTest_Bz356181_Transient class attributes and methods

# HibernateTest_Bz356181_NonTransient class attributes and methods

# HibernateTest_Bz398057A class attributes and methods
HibernateTest_Bz398057A_dbId: Property = Property(name="dbId", type=StringType)
HibernateTest_Bz398057A.attributes={HibernateTest_Bz398057A_dbId}

# HibernateTest_Bz380987_Group class attributes and methods

# HibernateTest_Bz380987_Person class attributes and methods
HibernateTest_Bz380987_Person_name: Property = Property(name="name", type=StringType)
HibernateTest_Bz380987_Person.attributes={HibernateTest_Bz380987_Person_name}

# HibernateTest_Bz380987_Place class attributes and methods
HibernateTest_Bz380987_Place_name: Property = Property(name="name", type=StringType)
HibernateTest_Bz380987_Place.attributes={HibernateTest_Bz380987_Place_name}

# HibernateTest_Bz397682C class attributes and methods
HibernateTest_Bz397682C_dbId: Property = Property(name="dbId", type=StringType)
HibernateTest_Bz397682C.attributes={HibernateTest_Bz397682C_dbId}

# HibernateTest_Bz398057B class attributes and methods
HibernateTest_Bz398057B_value: Property = Property(name="value", type=FloatType)
HibernateTest_Bz398057B_dbId: Property = Property(name="dbId", type=StringType)
HibernateTest_Bz398057B.attributes={HibernateTest_Bz398057B_value, HibernateTest_Bz398057B_dbId}

# HibernateTest_Bz398057A1 class attributes and methods

# Bz398057A class attributes and methods

# HibernateTest_Bz398057B1 class attributes and methods
HibernateTest_Bz398057B1_valueStr: Property = Property(name="valueStr", type=StringType)
HibernateTest_Bz398057B1.attributes={HibernateTest_Bz398057B1_valueStr}

# Bz398057B class attributes and methods

# HibernateTest_Bz397682P class attributes and methods
HibernateTest_Bz397682P_dbId: Property = Property(name="dbId", type=StringType)
HibernateTest_Bz397682P.attributes={HibernateTest_Bz397682P_dbId}

# Relationships
transientRef0: BinaryAssociation = BinaryAssociation(
    name="transientRef0",
    ends={
        Property(name="HibernateTest_Bz356181_Transient", type=HibernateTest_Bz356181_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="HibernateTest_Bz356181_Main", type=HibernateTest_Bz356181_Transient, multiplicity=Multiplicity(0, 1))
    }
)
transientOtherRef1: BinaryAssociation = BinaryAssociation(
    name="transientOtherRef1",
    ends={
        Property(name="HibernateTest_Bz356181_NonTransient", type=HibernateTest_Bz356181_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="HibernateTest_Bz356181_Main2", type=HibernateTest_Bz356181_NonTransient, multiplicity=Multiplicity(0, 1))
    }
)
main3: BinaryAssociation = BinaryAssociation(
    name="main3",
    ends={
        Property(name="HibernateTest_Bz356181_Main5", type=HibernateTest_Bz356181_NonTransient, multiplicity=Multiplicity(1, 1)),
        Property(name="HibernateTest_Bz356181_NonTransient4", type=HibernateTest_Bz356181_Main, multiplicity=Multiplicity(0, 1))
    }
)
people6: BinaryAssociation = BinaryAssociation(
    name="people6",
    ends={
        Property(name="Bz380987_Person", type=HibernateTest_Bz380987_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=HibernateTest_Bz380987_Person, multiplicity=Multiplicity(0, 9999))
    }
)
people7: BinaryAssociation = BinaryAssociation(
    name="people7",
    ends={
        Property(name="Bz380987_Person8", type=HibernateTest_Bz380987_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=HibernateTest_Bz380987_Person, multiplicity=Multiplicity(0, 9999))
    }
)
group9: BinaryAssociation = BinaryAssociation(
    name="group9",
    ends={
        Property(name="Bz380987_Group", type=HibernateTest_Bz380987_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="people", type=HibernateTest_Bz380987_Group, multiplicity=Multiplicity(0, 9999))
    }
)
places10: BinaryAssociation = BinaryAssociation(
    name="places10",
    ends={
        Property(name="Bz380987_Place", type=HibernateTest_Bz380987_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="people11", type=HibernateTest_Bz380987_Place, multiplicity=Multiplicity(0, 9999))
    }
)
listOfC14: BinaryAssociation = BinaryAssociation(
    name="listOfC14",
    ends={
        Property(name="Bz397682C", type=HibernateTest_Bz397682P, multiplicity=Multiplicity(1, 1)),
        Property(name="refToP", type=HibernateTest_Bz397682C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listOfB12: BinaryAssociation = BinaryAssociation(
    name="listOfB12",
    ends={
        Property(name="Bz398057B", type=HibernateTest_Bz398057A, multiplicity=Multiplicity(1, 1)),
        Property(name="refToClassA", type=HibernateTest_Bz398057B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refToClassA13: BinaryAssociation = BinaryAssociation(
    name="refToClassA13",
    ends={
        Property(name="Bz398057A", type=HibernateTest_Bz398057B, multiplicity=Multiplicity(1, 1)),
        Property(name="listOfB", type=HibernateTest_Bz398057A, multiplicity=Multiplicity(0, 1))
    }
)
refToP15: BinaryAssociation = BinaryAssociation(
    name="refToP15",
    ends={
        Property(name="Bz397682P", type=HibernateTest_Bz397682C, multiplicity=Multiplicity(1, 1)),
        Property(name="listOfC", type=HibernateTest_Bz397682P, multiplicity=Multiplicity(0, 1))
    }
)
refToC17: BinaryAssociation = BinaryAssociation(
    name="refToC17",
    ends={
        Property(name="HibernateTest_Bz397682C", type=HibernateTest_Bz397682C, multiplicity=Multiplicity(1, 1)),
        Property(name="HibernateTest_Bz397682C16", type=HibernateTest_Bz397682C, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_HibernateTest_Bz398057A1_Bz398057A = Generalization(general=Bz398057A, specific=HibernateTest_Bz398057A1)
gen_HibernateTest_Bz398057B1_Bz398057B = Generalization(general=Bz398057B, specific=HibernateTest_Bz398057B1)

# Domain Model
domain_model = DomainModel(
    name="HibernateTest",
    types={HibernateTest_Bz387752_Main, HibernateTest_Bz356181_Main, HibernateTest_Bz356181_Transient, HibernateTest_Bz356181_NonTransient, HibernateTest_Bz398057A, HibernateTest_Bz380987_Group, HibernateTest_Bz380987_Person, HibernateTest_Bz380987_Place, HibernateTest_Bz397682C, HibernateTest_Bz398057B, HibernateTest_Bz398057A1, Bz398057A, HibernateTest_Bz398057B1, Bz398057B, HibernateTest_Bz397682P, Bz387752_Enum},
    associations={transientRef0, transientOtherRef1, main3, people6, people7, group9, places10, listOfC14, listOfB12, refToClassA13, refToP15, refToC17},
    generalizations={gen_HibernateTest_Bz398057A1_Bz398057A, gen_HibernateTest_Bz398057B1_Bz398057B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)