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
ecoreTest_Eclass1 = Class(name="ecoreTest_Eclass1")
ecoreTest_EClass2 = Class(name="ecoreTest_EClass2")
ecoreTest_EClass3 = Class(name="ecoreTest_EClass3")
Eclass5 = Class(name="Eclass5")

# ecoreTest_Eclass1 class attributes and methods
ecoreTest_Eclass1_eAttribute1: Property = Property(name="eAttribute1", type=StringType)
ecoreTest_Eclass1_eAttribute2: Property = Property(name="eAttribute2", type=StringType)
ecoreTest_Eclass1.attributes={ecoreTest_Eclass1_eAttribute2, ecoreTest_Eclass1_eAttribute1}

# ecoreTest_EClass2 class attributes and methods
ecoreTest_EClass2_eAttribute3: Property = Property(name="eAttribute3", type=StringType)
ecoreTest_EClass2_eAttribute4: Property = Property(name="eAttribute4", type=StringType)
ecoreTest_EClass2.attributes={ecoreTest_EClass2_eAttribute4, ecoreTest_EClass2_eAttribute3}

# ecoreTest_EClass3 class attributes and methods

# Eclass5 class attributes and methods

# Relationships
classes20: BinaryAssociation = BinaryAssociation(
    name="classes20",
    ends={
        Property(name="ecoreTest_EClass2", type=ecoreTest_Eclass1, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreTest_Eclass1", type=ecoreTest_EClass2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes31: BinaryAssociation = BinaryAssociation(
    name="classes31",
    ends={
        Property(name="ecoreTest_EClass3", type=ecoreTest_EClass2, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreTest_EClass22", type=ecoreTest_EClass3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ecoreTest_EClass3_Eclass5 = Generalization(general=Eclass5, specific=ecoreTest_EClass3)


# OCL Constraints
eclass1_constraint: Constraint = Constraint(
    name="eclass1_constraint",
    context=ecoreTest_Eclass1,
    expression="context Eclass1 inv: Tuple{status: Boolean = false,severity: Integer = 0,message : String = 'ecoreTest: eclass1_constraint '+self.toString()}.status",
    language="OCL"
)
eclass2_constraint: Constraint = Constraint(
    name="eclass2_constraint",
    context=ecoreTest_EClass2,
    expression="context EClass2 inv: Tuple{status: Boolean = false,severity: Integer = 0,message : String = 'ecoreTest: eclass2_constraint '+self.toString()}.status",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="ecoreTest",
    types={ecoreTest_Eclass1, ecoreTest_EClass2, ecoreTest_EClass3, Eclass5},
    associations={classes20, classes31},
    constraints={eclass1_constraint, eclass2_constraint},
    generalizations={gen_ecoreTest_EClass3_Eclass5},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)