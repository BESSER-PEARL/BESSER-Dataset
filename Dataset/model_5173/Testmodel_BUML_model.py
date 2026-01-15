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
testmodel_SuperInterface = Class(name="testmodel::SuperInterface", is_abstract=True)
testmodel_SuperAbstractClass = Class(name="testmodel::SuperAbstractClass", is_abstract=True)
testmodel_SuperClass = Class(name="testmodel::SuperClass")
testmodel_SubInterface1 = Class(name="testmodel::SubInterface1", is_abstract=True)
SuperInterface = Class(name="SuperInterface")
testmodel_SubInterface2 = Class(name="testmodel::SubInterface2", is_abstract=True)
SuperAbstractClass = Class(name="SuperAbstractClass")
testmodel_SubAbstractClass1 = Class(name="testmodel::SubAbstractClass1", is_abstract=True)
testmodel_SubAbstractClass2 = Class(name="testmodel::SubAbstractClass2", is_abstract=True)
testmodel_SubAbstractClass3 = Class(name="testmodel::SubAbstractClass3", is_abstract=True)
testmodel_SubClass1 = Class(name="testmodel::SubClass1")
testmodel_SubClass2 = Class(name="testmodel::SubClass2")
testmodel_SubClass3 = Class(name="testmodel::SubClass3")
testmodel_SubInterface4 = Class(name="testmodel::SubInterface4", is_abstract=True)
SubInterface1 = Class(name="SubInterface1")
SubInterface2 = Class(name="SubInterface2")
testmodel_SubInterface5 = Class(name="testmodel::SubInterface5", is_abstract=True)
SubAbstractClass1 = Class(name="SubAbstractClass1")
testmodel_SubInterface6 = Class(name="testmodel::SubInterface6", is_abstract=True)
SubClass1 = Class(name="SubClass1")
testmodel_SubInterface7 = Class(name="testmodel::SubInterface7", is_abstract=True)
testmodel_SubAbstractClass4 = Class(name="testmodel::SubAbstractClass4", is_abstract=True)
testmodel_SubAbstractClass5 = Class(name="testmodel::SubAbstractClass5", is_abstract=True)
testmodel_SubAbstractClass6 = Class(name="testmodel::SubAbstractClass6", is_abstract=True)
testmodel_SubAbstractClass7 = Class(name="testmodel::SubAbstractClass7", is_abstract=True)
testmodel_SubClass4 = Class(name="testmodel::SubClass4")
testmodel_SubClass5 = Class(name="testmodel::SubClass5")
testmodel_SubClass6 = Class(name="testmodel::SubClass6")
testmodel_SubClass7 = Class(name="testmodel::SubClass7")
testmodel_A = Class(name="testmodel::A")
testmodel_B = Class(name="testmodel::B")
A = Class(name="A")
testmodel_C = Class(name="testmodel::C")
B = Class(name="B")
testmodel_Source = Class(name="testmodel::Source")
testmodel_Target = Class(name="testmodel::Target")
testmodel_SubInterface3 = Class(name="testmodel::SubInterface3", is_abstract=True)
SuperClass = Class(name="SuperClass")

# testmodel_SuperInterface class attributes and methods

# testmodel_SuperAbstractClass class attributes and methods

# testmodel_SuperClass class attributes and methods

# testmodel_SubInterface1 class attributes and methods

# SuperInterface class attributes and methods

# testmodel_SubInterface2 class attributes and methods

# SuperAbstractClass class attributes and methods

# testmodel_SubAbstractClass1 class attributes and methods

# testmodel_SubAbstractClass2 class attributes and methods

# testmodel_SubAbstractClass3 class attributes and methods

# testmodel_SubClass1 class attributes and methods

# testmodel_SubClass2 class attributes and methods

# testmodel_SubClass3 class attributes and methods

# testmodel_SubInterface4 class attributes and methods

# SubInterface1 class attributes and methods

# SubInterface2 class attributes and methods

# testmodel_SubInterface5 class attributes and methods

# SubAbstractClass1 class attributes and methods

# testmodel_SubInterface6 class attributes and methods

# SubClass1 class attributes and methods

# testmodel_SubInterface7 class attributes and methods

# testmodel_SubAbstractClass4 class attributes and methods

# testmodel_SubAbstractClass5 class attributes and methods

# testmodel_SubAbstractClass6 class attributes and methods

# testmodel_SubAbstractClass7 class attributes and methods

# testmodel_SubClass4 class attributes and methods

# testmodel_SubClass5 class attributes and methods

# testmodel_SubClass6 class attributes and methods

# testmodel_SubClass7 class attributes and methods

# testmodel_A class attributes and methods
testmodel_A_a: Property = Property(name="a", type=StringType)
testmodel_A_m_aOp: Method = Method(name="aOp", parameters={})
testmodel_A.attributes={testmodel_A_a}
testmodel_A.methods={testmodel_A_m_aOp}

# testmodel_B class attributes and methods
testmodel_B_b: Property = Property(name="b", type=StringType)
testmodel_B_m_bOp: Method = Method(name="bOp", parameters={})
testmodel_B.attributes={testmodel_B_b}
testmodel_B.methods={testmodel_B_m_bOp}

# A class attributes and methods

# testmodel_C class attributes and methods
testmodel_C_c: Property = Property(name="c", type=StringType)
testmodel_C_m_aOp: Method = Method(name="aOp", parameters={})
testmodel_C_m_bOp: Method = Method(name="bOp", parameters={})
testmodel_C.attributes={testmodel_C_c}
testmodel_C.methods={testmodel_C_m_bOp, testmodel_C_m_aOp}

# B class attributes and methods

# testmodel_Source class attributes and methods

# testmodel_Target class attributes and methods

# testmodel_SubInterface3 class attributes and methods

# SuperClass class attributes and methods

# Relationships
zero_one_no_no0: BinaryAssociation = BinaryAssociation(
    name="zero_one_no_no0",
    ends={
        Property(name="testmodel_Target", type=testmodel_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_Source", type=testmodel_Target, multiplicity=Multiplicity(0, 1))
    }
)
zero_many_no_no1: BinaryAssociation = BinaryAssociation(
    name="zero_many_no_no1",
    ends={
        Property(name="testmodel_Target3", type=testmodel_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_Source2", type=testmodel_Target, multiplicity=Multiplicity(0, 9999))
    }
)
zero_one_no_yes4: BinaryAssociation = BinaryAssociation(
    name="zero_one_no_yes4",
    ends={
        Property(name="testmodel_Target6", type=testmodel_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_Source5", type=testmodel_Target, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
zero_many_no_yes7: BinaryAssociation = BinaryAssociation(
    name="zero_many_no_yes7",
    ends={
        Property(name="testmodel_Target9", type=testmodel_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="testmodel_Source8", type=testmodel_Target, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
one_one_no_no10: BinaryAssociation = BinaryAssociation(
    name="one_one_no_no10",
    ends={
        Property(name="Target", type=testmodel_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="one_one_no_no", type=testmodel_Target, multiplicity=Multiplicity(0, 1))
    }
)
one_many_no_no11: BinaryAssociation = BinaryAssociation(
    name="one_many_no_no11",
    ends={
        Property(name="Target12", type=testmodel_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="one_many_no_no", type=testmodel_Target, multiplicity=Multiplicity(0, 9999))
    }
)
many_many_no_no13: BinaryAssociation = BinaryAssociation(
    name="many_many_no_no13",
    ends={
        Property(name="Target14", type=testmodel_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="many_many_no_no", type=testmodel_Target, multiplicity=Multiplicity(0, 9999))
    }
)
one_many_no_yes15: BinaryAssociation = BinaryAssociation(
    name="one_many_no_yes15",
    ends={
        Property(name="Target16", type=testmodel_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="one_many_no_yes", type=testmodel_Target, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
one_one_no_yes17: BinaryAssociation = BinaryAssociation(
    name="one_one_no_yes17",
    ends={
        Property(name="Target18", type=testmodel_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="one_one_no_yes", type=testmodel_Target, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
one_one_no_no19: BinaryAssociation = BinaryAssociation(
    name="one_one_no_no19",
    ends={
        Property(name="Source", type=testmodel_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="one_one_no_no20", type=testmodel_Source, multiplicity=Multiplicity(0, 1))
    }
)
one_many_no_no21: BinaryAssociation = BinaryAssociation(
    name="one_many_no_no21",
    ends={
        Property(name="Source23", type=testmodel_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="one_many_no_no22", type=testmodel_Source, multiplicity=Multiplicity(0, 1))
    }
)
many_many_no_no24: BinaryAssociation = BinaryAssociation(
    name="many_many_no_no24",
    ends={
        Property(name="Source26", type=testmodel_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="many_many_no_no25", type=testmodel_Source, multiplicity=Multiplicity(0, 9999))
    }
)
one_many_no_yes27: BinaryAssociation = BinaryAssociation(
    name="one_many_no_yes27",
    ends={
        Property(name="Source29", type=testmodel_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="one_many_no_yes28", type=testmodel_Source, multiplicity=Multiplicity(0, 1))
    }
)
one_one_no_yes30: BinaryAssociation = BinaryAssociation(
    name="one_one_no_yes30",
    ends={
        Property(name="Source32", type=testmodel_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="one_one_no_yes31", type=testmodel_Source, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_testmodel_SubInterface1_SuperInterface = Generalization(general=SuperInterface, specific=testmodel_SubInterface1)
gen_testmodel_SubInterface2_SuperAbstractClass = Generalization(general=SuperAbstractClass, specific=testmodel_SubInterface2)
gen_testmodel_SubAbstractClass1_SuperInterface = Generalization(general=SuperInterface, specific=testmodel_SubAbstractClass1)
gen_testmodel_SubAbstractClass2_SuperAbstractClass = Generalization(general=SuperAbstractClass, specific=testmodel_SubAbstractClass2)
gen_testmodel_SubAbstractClass3_SuperClass = Generalization(general=SuperClass, specific=testmodel_SubAbstractClass3)
gen_testmodel_SubClass1_SuperInterface = Generalization(general=SuperInterface, specific=testmodel_SubClass1)
gen_testmodel_SubClass2_SuperAbstractClass = Generalization(general=SuperAbstractClass, specific=testmodel_SubClass2)
gen_testmodel_SubClass3_SuperClass = Generalization(general=SuperClass, specific=testmodel_SubClass3)
gen_testmodel_SubInterface4_SubInterface1 = Generalization(general=SubInterface1, specific=testmodel_SubInterface4)
gen_testmodel_SubInterface4_SubInterface2 = Generalization(general=SubInterface2, specific=testmodel_SubInterface4)
gen_testmodel_SubInterface5_SubInterface1 = Generalization(general=SubInterface1, specific=testmodel_SubInterface5)
gen_testmodel_SubInterface5_SubAbstractClass1 = Generalization(general=SubAbstractClass1, specific=testmodel_SubInterface5)
gen_testmodel_SubInterface6_SubInterface1 = Generalization(general=SubInterface1, specific=testmodel_SubInterface6)
gen_testmodel_SubInterface6_SubClass1 = Generalization(general=SubClass1, specific=testmodel_SubInterface6)
gen_testmodel_SubInterface7_SubAbstractClass1 = Generalization(general=SubAbstractClass1, specific=testmodel_SubInterface7)
gen_testmodel_SubInterface7_SubClass1 = Generalization(general=SubClass1, specific=testmodel_SubInterface7)
gen_testmodel_SubAbstractClass4_SubInterface1 = Generalization(general=SubInterface1, specific=testmodel_SubAbstractClass4)
gen_testmodel_SubAbstractClass4_SubInterface2 = Generalization(general=SubInterface2, specific=testmodel_SubAbstractClass4)
gen_testmodel_SubAbstractClass5_SubInterface1 = Generalization(general=SubInterface1, specific=testmodel_SubAbstractClass5)
gen_testmodel_SubAbstractClass5_SubAbstractClass1 = Generalization(general=SubAbstractClass1, specific=testmodel_SubAbstractClass5)
gen_testmodel_SubAbstractClass6_SubInterface1 = Generalization(general=SubInterface1, specific=testmodel_SubAbstractClass6)
gen_testmodel_SubAbstractClass6_SubClass1 = Generalization(general=SubClass1, specific=testmodel_SubAbstractClass6)
gen_testmodel_SubAbstractClass7_SubAbstractClass1 = Generalization(general=SubAbstractClass1, specific=testmodel_SubAbstractClass7)
gen_testmodel_SubAbstractClass7_SubClass1 = Generalization(general=SubClass1, specific=testmodel_SubAbstractClass7)
gen_testmodel_SubClass4_SubInterface1 = Generalization(general=SubInterface1, specific=testmodel_SubClass4)
gen_testmodel_SubClass4_SubInterface2 = Generalization(general=SubInterface2, specific=testmodel_SubClass4)
gen_testmodel_SubClass5_SubInterface1 = Generalization(general=SubInterface1, specific=testmodel_SubClass5)
gen_testmodel_SubClass5_SubAbstractClass1 = Generalization(general=SubAbstractClass1, specific=testmodel_SubClass5)
gen_testmodel_SubClass6_SubInterface1 = Generalization(general=SubInterface1, specific=testmodel_SubClass6)
gen_testmodel_SubClass6_SubClass1 = Generalization(general=SubClass1, specific=testmodel_SubClass6)
gen_testmodel_SubClass7_SubAbstractClass1 = Generalization(general=SubAbstractClass1, specific=testmodel_SubClass7)
gen_testmodel_SubClass7_SubClass1 = Generalization(general=SubClass1, specific=testmodel_SubClass7)
gen_testmodel_B_A = Generalization(general=A, specific=testmodel_B)
gen_testmodel_C_B = Generalization(general=B, specific=testmodel_C)
gen_testmodel_SubInterface3_SuperClass = Generalization(general=SuperClass, specific=testmodel_SubInterface3)

# Domain Model
domain_model = DomainModel(
    name="testmodel",
    types={testmodel_SuperInterface, testmodel_SuperAbstractClass, testmodel_SuperClass, testmodel_SubInterface1, SuperInterface, testmodel_SubInterface2, SuperAbstractClass, testmodel_SubAbstractClass1, testmodel_SubAbstractClass2, testmodel_SubAbstractClass3, testmodel_SubClass1, testmodel_SubClass2, testmodel_SubClass3, testmodel_SubInterface4, SubInterface1, SubInterface2, testmodel_SubInterface5, SubAbstractClass1, testmodel_SubInterface6, SubClass1, testmodel_SubInterface7, testmodel_SubAbstractClass4, testmodel_SubAbstractClass5, testmodel_SubAbstractClass6, testmodel_SubAbstractClass7, testmodel_SubClass4, testmodel_SubClass5, testmodel_SubClass6, testmodel_SubClass7, testmodel_A, testmodel_B, A, testmodel_C, B, testmodel_Source, testmodel_Target, testmodel_SubInterface3, SuperClass},
    associations={zero_one_no_no0, zero_many_no_no1, zero_one_no_yes4, zero_many_no_yes7, one_one_no_no10, one_many_no_no11, many_many_no_no13, one_many_no_yes15, one_one_no_yes17, one_one_no_no19, one_many_no_no21, many_many_no_no24, one_many_no_yes27, one_one_no_yes30},
    generalizations={gen_testmodel_SubInterface1_SuperInterface, gen_testmodel_SubInterface2_SuperAbstractClass, gen_testmodel_SubAbstractClass1_SuperInterface, gen_testmodel_SubAbstractClass2_SuperAbstractClass, gen_testmodel_SubAbstractClass3_SuperClass, gen_testmodel_SubClass1_SuperInterface, gen_testmodel_SubClass2_SuperAbstractClass, gen_testmodel_SubClass3_SuperClass, gen_testmodel_SubInterface4_SubInterface1, gen_testmodel_SubInterface4_SubInterface2, gen_testmodel_SubInterface5_SubInterface1, gen_testmodel_SubInterface5_SubAbstractClass1, gen_testmodel_SubInterface6_SubInterface1, gen_testmodel_SubInterface6_SubClass1, gen_testmodel_SubInterface7_SubAbstractClass1, gen_testmodel_SubInterface7_SubClass1, gen_testmodel_SubAbstractClass4_SubInterface1, gen_testmodel_SubAbstractClass4_SubInterface2, gen_testmodel_SubAbstractClass5_SubInterface1, gen_testmodel_SubAbstractClass5_SubAbstractClass1, gen_testmodel_SubAbstractClass6_SubInterface1, gen_testmodel_SubAbstractClass6_SubClass1, gen_testmodel_SubAbstractClass7_SubAbstractClass1, gen_testmodel_SubAbstractClass7_SubClass1, gen_testmodel_SubClass4_SubInterface1, gen_testmodel_SubClass4_SubInterface2, gen_testmodel_SubClass5_SubInterface1, gen_testmodel_SubClass5_SubAbstractClass1, gen_testmodel_SubClass6_SubInterface1, gen_testmodel_SubClass6_SubClass1, gen_testmodel_SubClass7_SubAbstractClass1, gen_testmodel_SubClass7_SubClass1, gen_testmodel_B_A, gen_testmodel_C_B, gen_testmodel_SubInterface3_SuperClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)