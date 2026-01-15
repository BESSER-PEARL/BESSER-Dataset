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
EnumTestEnum: Enumeration = Enumeration(
    name="EnumTestEnum",
    literals={
            EnumerationLiteral(name="LOW"),
			EnumerationLiteral(name="MEDIUM"),
			EnumerationLiteral(name="HIGH"),
			EnumerationLiteral(name="INCREDIBLE")
    }
)

# Classes
tests_TestCategoryReference = Class(name="tests::TestCategoryReference")
tests_TestCategoryIntrinsicArray = Class(name="tests::TestCategoryIntrinsicArray")
tests_TestCategoryCompositionArray = Class(name="tests::TestCategoryCompositionArray")
tests_TestCategoryReferenceArray = Class(name="tests::TestCategoryReferenceArray")
tests_TestCategoryBeanA = Class(name="tests::TestCategoryBeanA")
tests_TestCategoryBeanB = Class(name="tests::TestCategoryBeanB")
tests_TestCategoryAllProperty = Class(name="tests::TestCategoryAllProperty")
DObject = Class(name="DObject")
tests_TestCategoryComposition = Class(name="tests::TestCategoryComposition")
tests_TestCategoryExtends = Class(name="tests::TestCategoryExtends")
TestCategoryBase = Class(name="TestCategoryBase")
tests_TestParameter = Class(name="tests::TestParameter")
tests_TestMassParameters = Class(name="tests::TestMassParameters")
tests_TestCrossLinkedParametersWithCalculation = Class(name="tests::TestCrossLinkedParametersWithCalculation")
tests_EReferenceTest = Class(name="tests::EReferenceTest")
tests_ExternalTestType = Class(name="tests::ExternalTestType")
tests_TestCategoryBeanAbstract = Class(name="tests::TestCategoryBeanAbstract", is_abstract=True)
tests_TestCategoryBeanConcrete = Class(name="tests::TestCategoryBeanConcrete")
dmf_DObject = Class(name="dmf::DObject")
TestCategoryBeanAbstract = Class(name="TestCategoryBeanAbstract")
tests_TestCategoryBase = Class(name="tests::TestCategoryBase")

# tests_TestCategoryReference class attributes and methods

# tests_TestCategoryIntrinsicArray class attributes and methods
tests_TestCategoryIntrinsicArray_testStringArrayDynamic: Property = Property(name="testStringArrayDynamic", type=StringType)
tests_TestCategoryIntrinsicArray_testStringArrayStatic: Property = Property(name="testStringArrayStatic", type=StringType)
tests_TestCategoryIntrinsicArray.attributes={tests_TestCategoryIntrinsicArray_testStringArrayStatic, tests_TestCategoryIntrinsicArray_testStringArrayDynamic}

# tests_TestCategoryCompositionArray class attributes and methods

# tests_TestCategoryReferenceArray class attributes and methods

# tests_TestCategoryBeanA class attributes and methods

# tests_TestCategoryBeanB class attributes and methods

# tests_TestCategoryAllProperty class attributes and methods
tests_TestCategoryAllProperty_testString: Property = Property(name="testString", type=StringType)
tests_TestCategoryAllProperty_testInt: Property = Property(name="testInt", type=IntegerType)
tests_TestCategoryAllProperty_testFloat: Property = Property(name="testFloat", type=FloatType)
tests_TestCategoryAllProperty_testBool: Property = Property(name="testBool", type=BooleanType)
tests_TestCategoryAllProperty_testResource: Property = Property(name="testResource", type=StringType)
tests_TestCategoryAllProperty_testEnum: Property = Property(name="testEnum", type=StringType)
tests_TestCategoryAllProperty.attributes={tests_TestCategoryAllProperty_testBool, tests_TestCategoryAllProperty_testFloat, tests_TestCategoryAllProperty_testString, tests_TestCategoryAllProperty_testEnum, tests_TestCategoryAllProperty_testInt, tests_TestCategoryAllProperty_testResource}

# DObject class attributes and methods

# tests_TestCategoryComposition class attributes and methods

# tests_TestCategoryExtends class attributes and methods
tests_TestCategoryExtends_testExtendsProperty: Property = Property(name="testExtendsProperty", type=IntegerType)
tests_TestCategoryExtends.attributes={tests_TestCategoryExtends_testExtendsProperty}

# TestCategoryBase class attributes and methods

# tests_TestParameter class attributes and methods
tests_TestParameter_defaultValue: Property = Property(name="defaultValue", type=FloatType)
tests_TestParameter.attributes={tests_TestParameter_defaultValue}

# tests_TestMassParameters class attributes and methods

# tests_TestCrossLinkedParametersWithCalculation class attributes and methods
tests_TestCrossLinkedParametersWithCalculation_calcedTrl: Property = Property(name="calcedTrl", type=FloatType)
tests_TestCrossLinkedParametersWithCalculation.attributes={tests_TestCrossLinkedParametersWithCalculation_calcedTrl}

# tests_EReferenceTest class attributes and methods

# tests_ExternalTestType class attributes and methods

# tests_TestCategoryBeanAbstract class attributes and methods

# tests_TestCategoryBeanConcrete class attributes and methods

# dmf_DObject class attributes and methods

# TestCategoryBeanAbstract class attributes and methods

# tests_TestCategoryBase class attributes and methods
tests_TestCategoryBase_testBaseProperty: Property = Property(name="testBaseProperty", type=IntegerType)
tests_TestCategoryBase.attributes={tests_TestCategoryBase_testBaseProperty}

# Relationships
testSubCategory0: BinaryAssociation = BinaryAssociation(
    name="testSubCategory0",
    ends={
        Property(name="tests_TestCategoryAllProperty", type=tests_TestCategoryComposition, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_TestCategoryComposition", type=tests_TestCategoryAllProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
testRefCategory1: BinaryAssociation = BinaryAssociation(
    name="testRefCategory1",
    ends={
        Property(name="tests_TestCategoryAllProperty2", type=tests_TestCategoryReference, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_TestCategoryReference", type=tests_TestCategoryAllProperty, multiplicity=Multiplicity(0, 1))
    }
)
testCompositionArrayDynamic3: BinaryAssociation = BinaryAssociation(
    name="testCompositionArrayDynamic3",
    ends={
        Property(name="tests_TestCategoryAllProperty4", type=tests_TestCategoryCompositionArray, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_TestCategoryCompositionArray", type=tests_TestCategoryAllProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testCompositionArrayStatic5: BinaryAssociation = BinaryAssociation(
    name="testCompositionArrayStatic5",
    ends={
        Property(name="tests_TestCategoryAllProperty7", type=tests_TestCategoryCompositionArray, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_TestCategoryCompositionArray6", type=tests_TestCategoryAllProperty, multiplicity=Multiplicity(0, 4), is_composite=True)
    }
)
testCategoryReferenceArrayDynamic8: BinaryAssociation = BinaryAssociation(
    name="testCategoryReferenceArrayDynamic8",
    ends={
        Property(name="tests_TestCategoryAllProperty9", type=tests_TestCategoryReferenceArray, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_TestCategoryReferenceArray", type=tests_TestCategoryAllProperty, multiplicity=Multiplicity(0, 9999))
    }
)
testCategoryReferenceArrayStatic10: BinaryAssociation = BinaryAssociation(
    name="testCategoryReferenceArrayStatic10",
    ends={
        Property(name="tests_TestCategoryAllProperty12", type=tests_TestCategoryReferenceArray, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_TestCategoryReferenceArray11", type=tests_TestCategoryAllProperty, multiplicity=Multiplicity(0, 4))
    }
)
mass18: BinaryAssociation = BinaryAssociation(
    name="mass18",
    ends={
        Property(name="tests_TestParameter", type=tests_TestMassParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_TestMassParameters", type=tests_TestParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eReferenceTest19: BinaryAssociation = BinaryAssociation(
    name="eReferenceTest19",
    ends={
        Property(name="tests_ExternalTestType", type=tests_EReferenceTest, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_EReferenceTest", type=tests_ExternalTestType, multiplicity=Multiplicity(0, 1))
    }
)
testArray14: BinaryAssociation = BinaryAssociation(
    name="testArray14",
    ends={
        Property(name="tests_TestCategoryBase", type=tests_TestCategoryBase, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_TestCategoryBase13", type=tests_TestCategoryBase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testReference16: BinaryAssociation = BinaryAssociation(
    name="testReference16",
    ends={
        Property(name="tests_TestCategoryBase17", type=tests_TestCategoryBase, multiplicity=Multiplicity(1, 1)),
        Property(name="tests_TestCategoryBase15", type=tests_TestCategoryBase, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_tests_TestCategoryReference_DObject = Generalization(general=DObject, specific=tests_TestCategoryReference)
gen_tests_TestCategoryIntrinsicArray_DObject = Generalization(general=DObject, specific=tests_TestCategoryIntrinsicArray)
gen_tests_TestCategoryCompositionArray_DObject = Generalization(general=DObject, specific=tests_TestCategoryCompositionArray)
gen_tests_TestCategoryReferenceArray_DObject = Generalization(general=DObject, specific=tests_TestCategoryReferenceArray)
gen_tests_TestCategoryBeanA_DObject = Generalization(general=DObject, specific=tests_TestCategoryBeanA)
gen_tests_TestCategoryBeanB_DObject = Generalization(general=DObject, specific=tests_TestCategoryBeanB)
gen_tests_TestCategoryAllProperty_DObject = Generalization(general=DObject, specific=tests_TestCategoryAllProperty)
gen_tests_TestCategoryComposition_DObject = Generalization(general=DObject, specific=tests_TestCategoryComposition)
gen_tests_TestCategoryExtends_dmf_DObject = Generalization(general=dmf_DObject, specific=tests_TestCategoryExtends)
gen_tests_TestCategoryExtends_TestCategoryBase = Generalization(general=TestCategoryBase, specific=tests_TestCategoryExtends)
gen_tests_TestParameter_DObject = Generalization(general=DObject, specific=tests_TestParameter)
gen_tests_TestMassParameters_DObject = Generalization(general=DObject, specific=tests_TestMassParameters)
gen_tests_TestCrossLinkedParametersWithCalculation_DObject = Generalization(general=DObject, specific=tests_TestCrossLinkedParametersWithCalculation)
gen_tests_EReferenceTest_DObject = Generalization(general=DObject, specific=tests_EReferenceTest)
gen_tests_TestCategoryBeanAbstract_DObject = Generalization(general=DObject, specific=tests_TestCategoryBeanAbstract)
gen_tests_TestCategoryBeanConcrete_dmf_DObject = Generalization(general=dmf_DObject, specific=tests_TestCategoryBeanConcrete)
gen_tests_TestCategoryBeanConcrete_TestCategoryBeanAbstract = Generalization(general=TestCategoryBeanAbstract, specific=tests_TestCategoryBeanConcrete)
gen_tests_TestCategoryBase_DObject = Generalization(general=DObject, specific=tests_TestCategoryBase)

# Domain Model
domain_model = DomainModel(
    name="tests",
    types={tests_TestCategoryReference, tests_TestCategoryIntrinsicArray, tests_TestCategoryCompositionArray, tests_TestCategoryReferenceArray, tests_TestCategoryBeanA, tests_TestCategoryBeanB, tests_TestCategoryAllProperty, DObject, tests_TestCategoryComposition, tests_TestCategoryExtends, TestCategoryBase, tests_TestParameter, tests_TestMassParameters, tests_TestCrossLinkedParametersWithCalculation, tests_EReferenceTest, tests_ExternalTestType, tests_TestCategoryBeanAbstract, tests_TestCategoryBeanConcrete, dmf_DObject, TestCategoryBeanAbstract, tests_TestCategoryBase, EnumTestEnum},
    associations={testSubCategory0, testRefCategory1, testCompositionArrayDynamic3, testCompositionArrayStatic5, testCategoryReferenceArrayDynamic8, testCategoryReferenceArrayStatic10, mass18, eReferenceTest19, testArray14, testReference16},
    generalizations={gen_tests_TestCategoryReference_DObject, gen_tests_TestCategoryIntrinsicArray_DObject, gen_tests_TestCategoryCompositionArray_DObject, gen_tests_TestCategoryReferenceArray_DObject, gen_tests_TestCategoryBeanA_DObject, gen_tests_TestCategoryBeanB_DObject, gen_tests_TestCategoryAllProperty_DObject, gen_tests_TestCategoryComposition_DObject, gen_tests_TestCategoryExtends_dmf_DObject, gen_tests_TestCategoryExtends_TestCategoryBase, gen_tests_TestParameter_DObject, gen_tests_TestMassParameters_DObject, gen_tests_TestCrossLinkedParametersWithCalculation_DObject, gen_tests_EReferenceTest_DObject, gen_tests_TestCategoryBeanAbstract_DObject, gen_tests_TestCategoryBeanConcrete_dmf_DObject, gen_tests_TestCategoryBeanConcrete_TestCategoryBeanAbstract, gen_tests_TestCategoryBase_DObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)