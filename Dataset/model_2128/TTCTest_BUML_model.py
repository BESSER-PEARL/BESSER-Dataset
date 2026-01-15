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
Class_Element = Class(name="Class::Element")
tTCTest_Methods = Class(name="tTCTest::Methods")
tTCTest_Java_Field = Class(name="tTCTest::Java::Field")
tTCTest_Fields = Class(name="tTCTest::Fields")
tTCTest_Test_File = Class(name="tTCTest::Test::File")
tTCTest_Test_Case = Class(name="tTCTest::Test::Case")
tTCTest_Java_Class = Class(name="tTCTest::Java::Class")
tTCTest_Classes = Class(name="tTCTest::Classes")
tTCTest_Java_Method = Class(name="tTCTest::Java::Method")
tTCTest_Refactoring_Instance = Class(name="tTCTest::Refactoring::Instance")
tTCTest_Create_Superclass_Refactoring = Class(name="tTCTest::Create::Superclass::Refactoring")
tTCTest_Test_Step_Element = Class(name="tTCTest::Test::Step::Element")
tTCTest_Test_Step = Class(name="tTCTest::Test::Step")
Test_Step_Element = Class(name="Test::Step::Element")
tTCTest_Assertion = Class(name="tTCTest::Assertion")
tTCTest_Assert_False = Class(name="tTCTest::Assert::False")
Assertion = Class(name="Assertion")
tTCTest_Assert_True = Class(name="tTCTest::Assert::True")
tTCTest_Condition = Class(name="tTCTest::Condition")
tTCTest_Test_Flow = Class(name="tTCTest::Test::Flow")
Refactoring = Class(name="Refactoring")
tTCTest_Refactoring = Class(name="tTCTest::Refactoring")
tTCTest_Pull_Up_Refactoring = Class(name="tTCTest::Pull::Up::Refactoring")
Refactoring_Instance = Class(name="Refactoring::Instance")
tTCTest_Propose_Pullup_Method_Refactoring = Class(name="tTCTest::Propose::Pullup::Method::Refactoring")
Propose_Refactoring = Class(name="Propose::Refactoring")
tTCTest_Propose_Create_Superclass_Refactoring = Class(name="tTCTest::Propose::Create::Superclass::Refactoring")
tTCTest_Containment = Class(name="tTCTest::Containment")
tTCTest_Class_Element = Class(name="tTCTest::Class::Element")
tTCTest_Contains = Class(name="tTCTest::Contains")
Containment = Class(name="Containment")
tTCTest_Contains_Not = Class(name="tTCTest::Contains::Not")
tTCTest_Implementation = Class(name="tTCTest::Implementation")
tTCTest_Implements = Class(name="tTCTest::Implements")
Implementation = Class(name="Implementation")
tTCTest_Implements_Not = Class(name="tTCTest::Implements::Not")
tTCTest_Warning = Class(name="tTCTest::Warning")
tTCTest_Expect_True = Class(name="tTCTest::Expect::True")
Condition = Class(name="Condition")
tTCTest_Expect_False = Class(name="tTCTest::Expect::False")
tTCTest_Compile = Class(name="tTCTest::Compile")
tTCTest_Synchronize = Class(name="tTCTest::Synchronize")
tTCTest_No_Refactoring = Class(name="tTCTest::No::Refactoring")
tTCTest_Propose_Refactoring = Class(name="tTCTest::Propose::Refactoring")

# Class_Element class attributes and methods

# tTCTest_Methods class attributes and methods
tTCTest_Methods_name: Property = Property(name="name", type=StringType)
tTCTest_Methods.attributes={tTCTest_Methods_name}

# tTCTest_Java_Field class attributes and methods
tTCTest_Java_Field_field_name: Property = Property(name="field_name", type=StringType)
tTCTest_Java_Field.attributes={tTCTest_Java_Field_field_name}

# tTCTest_Fields class attributes and methods
tTCTest_Fields_name: Property = Property(name="name", type=StringType)
tTCTest_Fields.attributes={tTCTest_Fields_name}

# tTCTest_Test_File class attributes and methods
tTCTest_Test_File_name: Property = Property(name="name", type=StringType)
tTCTest_Test_File.attributes={tTCTest_Test_File_name}

# tTCTest_Test_Case class attributes and methods
tTCTest_Test_Case_name: Property = Property(name="name", type=StringType)
tTCTest_Test_Case_description: Property = Property(name="description", type=StringType)
tTCTest_Test_Case_java_program: Property = Property(name="java_program", type=StringType)
tTCTest_Test_Case.attributes={tTCTest_Test_Case_java_program, tTCTest_Test_Case_name, tTCTest_Test_Case_description}

# tTCTest_Java_Class class attributes and methods
tTCTest_Java_Class_name: Property = Property(name="name", type=StringType)
tTCTest_Java_Class_package: Property = Property(name="package", type=StringType)
tTCTest_Java_Class_class_name: Property = Property(name="class_name", type=StringType)
tTCTest_Java_Class.attributes={tTCTest_Java_Class_name, tTCTest_Java_Class_package, tTCTest_Java_Class_class_name}

# tTCTest_Classes class attributes and methods
tTCTest_Classes_name: Property = Property(name="name", type=StringType)
tTCTest_Classes.attributes={tTCTest_Classes_name}

# tTCTest_Java_Method class attributes and methods
tTCTest_Java_Method_method_name: Property = Property(name="method_name", type=StringType)
tTCTest_Java_Method.attributes={tTCTest_Java_Method_method_name}

# tTCTest_Refactoring_Instance class attributes and methods
tTCTest_Refactoring_Instance_name: Property = Property(name="name", type=StringType)
tTCTest_Refactoring_Instance.attributes={tTCTest_Refactoring_Instance_name}

# tTCTest_Create_Superclass_Refactoring class attributes and methods

# tTCTest_Test_Step_Element class attributes and methods

# tTCTest_Test_Step class attributes and methods

# Test_Step_Element class attributes and methods

# tTCTest_Assertion class attributes and methods

# tTCTest_Assert_False class attributes and methods

# Assertion class attributes and methods

# tTCTest_Assert_True class attributes and methods

# tTCTest_Condition class attributes and methods

# tTCTest_Test_Flow class attributes and methods

# Refactoring class attributes and methods

# tTCTest_Refactoring class attributes and methods

# tTCTest_Pull_Up_Refactoring class attributes and methods

# Refactoring_Instance class attributes and methods

# tTCTest_Propose_Pullup_Method_Refactoring class attributes and methods

# Propose_Refactoring class attributes and methods

# tTCTest_Propose_Create_Superclass_Refactoring class attributes and methods

# tTCTest_Containment class attributes and methods

# tTCTest_Class_Element class attributes and methods
tTCTest_Class_Element_name: Property = Property(name="name", type=StringType)
tTCTest_Class_Element.attributes={tTCTest_Class_Element_name}

# tTCTest_Contains class attributes and methods

# Containment class attributes and methods

# tTCTest_Contains_Not class attributes and methods

# tTCTest_Implementation class attributes and methods

# tTCTest_Implements class attributes and methods

# Implementation class attributes and methods

# tTCTest_Implements_Not class attributes and methods

# tTCTest_Warning class attributes and methods
tTCTest_Warning_message: Property = Property(name="message", type=StringType)
tTCTest_Warning.attributes={tTCTest_Warning_message}

# tTCTest_Expect_True class attributes and methods

# Condition class attributes and methods

# tTCTest_Expect_False class attributes and methods

# tTCTest_Compile class attributes and methods

# tTCTest_Synchronize class attributes and methods

# tTCTest_No_Refactoring class attributes and methods

# tTCTest_Propose_Refactoring class attributes and methods

# Relationships
refactorings7: BinaryAssociation = BinaryAssociation(
    name="refactorings7",
    ends={
        Property(name="tTCTest_Refactoring_Instance", type=tTCTest_Test_File, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Test_File8", type=tTCTest_Refactoring_Instance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes9: BinaryAssociation = BinaryAssociation(
    name="classes9",
    ends={
        Property(name="tTCTest_Java_Class11", type=tTCTest_Classes, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Classes10", type=tTCTest_Java_Class, multiplicity=Multiplicity(0, 9999))
    }
)
params12: BinaryAssociation = BinaryAssociation(
    name="params12",
    ends={
        Property(name="tTCTest_Java_Class14", type=tTCTest_Java_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Java_Method13", type=tTCTest_Java_Class, multiplicity=Multiplicity(0, 9999))
    }
)
methods15: BinaryAssociation = BinaryAssociation(
    name="methods15",
    ends={
        Property(name="tTCTest_Java_Method16", type=tTCTest_Methods, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Methods", type=tTCTest_Java_Method, multiplicity=Multiplicity(0, 9999))
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="tTCTest_Java_Class18", type=tTCTest_Java_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Java_Field", type=tTCTest_Java_Class, multiplicity=Multiplicity(0, 1))
    }
)
test_cases0: BinaryAssociation = BinaryAssociation(
    name="test_cases0",
    ends={
        Property(name="tTCTest_Test_Case", type=tTCTest_Test_File, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Test_File", type=tTCTest_Test_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
java_class1: BinaryAssociation = BinaryAssociation(
    name="java_class1",
    ends={
        Property(name="tTCTest_Java_Class", type=tTCTest_Test_File, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Test_File2", type=tTCTest_Java_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
java_classes3: BinaryAssociation = BinaryAssociation(
    name="java_classes3",
    ends={
        Property(name="tTCTest_Classes", type=tTCTest_Test_File, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Test_File4", type=tTCTest_Classes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
java_method5: BinaryAssociation = BinaryAssociation(
    name="java_method5",
    ends={
        Property(name="tTCTest_Java_Method", type=tTCTest_Test_File, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Test_File6", type=tTCTest_Java_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent23: BinaryAssociation = BinaryAssociation(
    name="parent23",
    ends={
        Property(name="tTCTest_Java_Class24", type=tTCTest_Pull_Up_Refactoring, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Pull_Up_Refactoring", type=tTCTest_Java_Class, multiplicity=Multiplicity(0, 1))
    }
)
method25: BinaryAssociation = BinaryAssociation(
    name="method25",
    ends={
        Property(name="tTCTest_Java_Method27", type=tTCTest_Pull_Up_Refactoring, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Pull_Up_Refactoring26", type=tTCTest_Java_Method, multiplicity=Multiplicity(0, 1))
    }
)
child28: BinaryAssociation = BinaryAssociation(
    name="child28",
    ends={
        Property(name="tTCTest_Classes29", type=tTCTest_Create_Superclass_Refactoring, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Create_Superclass_Refactoring", type=tTCTest_Classes, multiplicity=Multiplicity(0, 1))
    }
)
target30: BinaryAssociation = BinaryAssociation(
    name="target30",
    ends={
        Property(name="tTCTest_Java_Class32", type=tTCTest_Create_Superclass_Refactoring, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Create_Superclass_Refactoring31", type=tTCTest_Java_Class, multiplicity=Multiplicity(0, 1))
    }
)
step33: BinaryAssociation = BinaryAssociation(
    name="step33",
    ends={
        Property(name="tTCTest_Test_Step_Element", type=tTCTest_Test_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Test_Flow34", type=tTCTest_Test_Step_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements35: BinaryAssociation = BinaryAssociation(
    name="elements35",
    ends={
        Property(name="tTCTest_Test_Step_Element36", type=tTCTest_Test_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Test_Step", type=tTCTest_Test_Step_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input37: BinaryAssociation = BinaryAssociation(
    name="input37",
    ends={
        Property(name="tTCTest_Refactoring", type=tTCTest_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Assertion", type=tTCTest_Refactoring, multiplicity=Multiplicity(0, 1))
    }
)
refactoring38: BinaryAssociation = BinaryAssociation(
    name="refactoring38",
    ends={
        Property(name="tTCTest_Refactoring39", type=tTCTest_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Condition", type=tTCTest_Refactoring, multiplicity=Multiplicity(0, 1))
    }
)
fields19: BinaryAssociation = BinaryAssociation(
    name="fields19",
    ends={
        Property(name="tTCTest_Java_Field20", type=tTCTest_Fields, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Fields", type=tTCTest_Java_Field, multiplicity=Multiplicity(0, 9999))
    }
)
test_flow21: BinaryAssociation = BinaryAssociation(
    name="test_flow21",
    ends={
        Property(name="tTCTest_Test_Flow", type=tTCTest_Test_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Test_Case22", type=tTCTest_Test_Flow, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refactoring48: BinaryAssociation = BinaryAssociation(
    name="refactoring48",
    ends={
        Property(name="tTCTest_Refactoring49", type=tTCTest_Propose_Refactoring, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Propose_Refactoring", type=tTCTest_Refactoring, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class50: BinaryAssociation = BinaryAssociation(
    name="class50",
    ends={
        Property(name="tTCTest_Java_Class51", type=tTCTest_Containment, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Containment", type=tTCTest_Java_Class, multiplicity=Multiplicity(0, 1))
    }
)
contains52: BinaryAssociation = BinaryAssociation(
    name="contains52",
    ends={
        Property(name="tTCTest_Class_Element", type=tTCTest_Containment, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Containment53", type=tTCTest_Class_Element, multiplicity=Multiplicity(0, 1))
    }
)
child54: BinaryAssociation = BinaryAssociation(
    name="child54",
    ends={
        Property(name="tTCTest_Java_Class55", type=tTCTest_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Implementation", type=tTCTest_Java_Class, multiplicity=Multiplicity(0, 1))
    }
)
parent56: BinaryAssociation = BinaryAssociation(
    name="parent56",
    ends={
        Property(name="tTCTest_Java_Class58", type=tTCTest_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Implementation57", type=tTCTest_Java_Class, multiplicity=Multiplicity(0, 1))
    }
)
true_steps40: BinaryAssociation = BinaryAssociation(
    name="true_steps40",
    ends={
        Property(name="tTCTest_Test_Step_Element42", type=tTCTest_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Condition41", type=tTCTest_Test_Step_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
warning43: BinaryAssociation = BinaryAssociation(
    name="warning43",
    ends={
        Property(name="tTCTest_Warning", type=tTCTest_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Condition44", type=tTCTest_Warning, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
false_steps45: BinaryAssociation = BinaryAssociation(
    name="false_steps45",
    ends={
        Property(name="tTCTest_Test_Step_Element47", type=tTCTest_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="tTCTest_Condition46", type=tTCTest_Test_Step_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tTCTest_Java_Method_Class_Element = Generalization(general=Class_Element, specific=tTCTest_Java_Method)
gen_tTCTest_Java_Field_Class_Element = Generalization(general=Class_Element, specific=tTCTest_Java_Field)
gen_tTCTest_Create_Superclass_Refactoring_Refactoring_Instance = Generalization(general=Refactoring_Instance, specific=tTCTest_Create_Superclass_Refactoring)
gen_tTCTest_Test_Step_Test_Step_Element = Generalization(general=Test_Step_Element, specific=tTCTest_Test_Step)
gen_tTCTest_Assertion_Test_Step_Element = Generalization(general=Test_Step_Element, specific=tTCTest_Assertion)
gen_tTCTest_Assert_False_Assertion = Generalization(general=Assertion, specific=tTCTest_Assert_False)
gen_tTCTest_Assert_True_Assertion = Generalization(general=Assertion, specific=tTCTest_Assert_True)
gen_tTCTest_Condition_Test_Step_Element = Generalization(general=Test_Step_Element, specific=tTCTest_Condition)
gen_tTCTest_Refactoring_Instance_Refactoring = Generalization(general=Refactoring, specific=tTCTest_Refactoring_Instance)
gen_tTCTest_Pull_Up_Refactoring_Refactoring_Instance = Generalization(general=Refactoring_Instance, specific=tTCTest_Pull_Up_Refactoring)
gen_tTCTest_Propose_Pullup_Method_Refactoring_Propose_Refactoring = Generalization(general=Propose_Refactoring, specific=tTCTest_Propose_Pullup_Method_Refactoring)
gen_tTCTest_Propose_Create_Superclass_Refactoring_Propose_Refactoring = Generalization(general=Propose_Refactoring, specific=tTCTest_Propose_Create_Superclass_Refactoring)
gen_tTCTest_Containment_Test_Step_Element = Generalization(general=Test_Step_Element, specific=tTCTest_Containment)
gen_tTCTest_Contains_Containment = Generalization(general=Containment, specific=tTCTest_Contains)
gen_tTCTest_Contains_Not_Containment = Generalization(general=Containment, specific=tTCTest_Contains_Not)
gen_tTCTest_Implementation_Test_Step_Element = Generalization(general=Test_Step_Element, specific=tTCTest_Implementation)
gen_tTCTest_Implements_Implementation = Generalization(general=Implementation, specific=tTCTest_Implements)
gen_tTCTest_Implements_Not_Implementation = Generalization(general=Implementation, specific=tTCTest_Implements_Not)
gen_tTCTest_Expect_True_Condition = Generalization(general=Condition, specific=tTCTest_Expect_True)
gen_tTCTest_Expect_False_Condition = Generalization(general=Condition, specific=tTCTest_Expect_False)
gen_tTCTest_Compile_Test_Step_Element = Generalization(general=Test_Step_Element, specific=tTCTest_Compile)
gen_tTCTest_Synchronize_Test_Step_Element = Generalization(general=Test_Step_Element, specific=tTCTest_Synchronize)
gen_tTCTest_No_Refactoring_Refactoring = Generalization(general=Refactoring, specific=tTCTest_No_Refactoring)

# Domain Model
domain_model = DomainModel(
    name="tTCTest",
    types={Class_Element, tTCTest_Methods, tTCTest_Java_Field, tTCTest_Fields, tTCTest_Test_File, tTCTest_Test_Case, tTCTest_Java_Class, tTCTest_Classes, tTCTest_Java_Method, tTCTest_Refactoring_Instance, tTCTest_Create_Superclass_Refactoring, tTCTest_Test_Step_Element, tTCTest_Test_Step, Test_Step_Element, tTCTest_Assertion, tTCTest_Assert_False, Assertion, tTCTest_Assert_True, tTCTest_Condition, tTCTest_Test_Flow, Refactoring, tTCTest_Refactoring, tTCTest_Pull_Up_Refactoring, Refactoring_Instance, tTCTest_Propose_Pullup_Method_Refactoring, Propose_Refactoring, tTCTest_Propose_Create_Superclass_Refactoring, tTCTest_Containment, tTCTest_Class_Element, tTCTest_Contains, Containment, tTCTest_Contains_Not, tTCTest_Implementation, tTCTest_Implements, Implementation, tTCTest_Implements_Not, tTCTest_Warning, tTCTest_Expect_True, Condition, tTCTest_Expect_False, tTCTest_Compile, tTCTest_Synchronize, tTCTest_No_Refactoring, tTCTest_Propose_Refactoring},
    associations={refactorings7, classes9, params12, methods15, type17, test_cases0, java_class1, java_classes3, java_method5, parent23, method25, child28, target30, step33, elements35, input37, refactoring38, fields19, test_flow21, refactoring48, class50, contains52, child54, parent56, true_steps40, warning43, false_steps45},
    generalizations={gen_tTCTest_Java_Method_Class_Element, gen_tTCTest_Java_Field_Class_Element, gen_tTCTest_Create_Superclass_Refactoring_Refactoring_Instance, gen_tTCTest_Test_Step_Test_Step_Element, gen_tTCTest_Assertion_Test_Step_Element, gen_tTCTest_Assert_False_Assertion, gen_tTCTest_Assert_True_Assertion, gen_tTCTest_Condition_Test_Step_Element, gen_tTCTest_Refactoring_Instance_Refactoring, gen_tTCTest_Pull_Up_Refactoring_Refactoring_Instance, gen_tTCTest_Propose_Pullup_Method_Refactoring_Propose_Refactoring, gen_tTCTest_Propose_Create_Superclass_Refactoring_Propose_Refactoring, gen_tTCTest_Containment_Test_Step_Element, gen_tTCTest_Contains_Containment, gen_tTCTest_Contains_Not_Containment, gen_tTCTest_Implementation_Test_Step_Element, gen_tTCTest_Implements_Implementation, gen_tTCTest_Implements_Not_Implementation, gen_tTCTest_Expect_True_Condition, gen_tTCTest_Expect_False_Condition, gen_tTCTest_Compile_Test_Step_Element, gen_tTCTest_Synchronize_Test_Step_Element, gen_tTCTest_No_Refactoring_Refactoring},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)