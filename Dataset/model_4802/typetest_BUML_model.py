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
pltest_Base = Class(name="pltest::Base")
pltest_Common = Class(name="pltest::Common")
Base = Class(name="Base")
pltest_Interface = Class(name="pltest::Interface", is_abstract=True)
pltest_Child1 = Class(name="pltest::Child1")
Common = Class(name="Common")
Interface = Class(name="Interface")
pltest_WhatEver = Class(name="pltest::WhatEver")
pltest_GrandChildD = Class(name="pltest::GrandChildD")
pltest_GrandGrandChildE = Class(name="pltest::GrandGrandChildE")
GrandChildD = Class(name="GrandChildD")
pltest_GrandGrandChildF = Class(name="pltest::GrandGrandChildF")
pltest_Numbers = Class(name="pltest::Numbers")
pltest_TestPackageableElement = Class(name="pltest::TestPackageableElement")
pltest_TestPackage = Class(name="pltest::TestPackage")
TestPackageableElement = Class(name="TestPackageableElement")
pltest_TestClass = Class(name="pltest::TestClass")
TestClassifier = Class(name="TestClassifier")
pltest_TestClassifier = Class(name="pltest::TestClassifier")
pltest_TestInterface = Class(name="pltest::TestInterface")
pltest_Child2 = Class(name="pltest::Child2")
Child3 = Class(name="Child3")
pltest_GrandChild = Class(name="pltest::GrandChild")
Child1 = Class(name="Child1")
pltest_Child3 = Class(name="pltest::Child3")
pltest_GrandChild2 = Class(name="pltest::GrandChild2")
Child2 = Class(name="Child2")
pltest_Red = Class(name="pltest::Red")
pltest_Circle = Class(name="pltest::Circle")

# pltest_Base class attributes and methods

# pltest_Common class attributes and methods

# Base class attributes and methods

# pltest_Interface class attributes and methods

# pltest_Child1 class attributes and methods
pltest_Child1_name: Property = Property(name="name", type=StringType)
pltest_Child1.attributes={pltest_Child1_name}

# Common class attributes and methods

# Interface class attributes and methods

# pltest_WhatEver class attributes and methods

# pltest_GrandChildD class attributes and methods

# pltest_GrandGrandChildE class attributes and methods

# GrandChildD class attributes and methods

# pltest_GrandGrandChildF class attributes and methods

# pltest_Numbers class attributes and methods
pltest_Numbers_int: Property = Property(name="int", type=IntegerType)
pltest_Numbers_long: Property = Property(name="long", type=StringType)
pltest_Numbers_float: Property = Property(name="float", type=FloatType)
pltest_Numbers_double: Property = Property(name="double", type=FloatType)
pltest_Numbers_bigInt: Property = Property(name="bigInt", type=StringType)
pltest_Numbers_bigDecimal: Property = Property(name="bigDecimal", type=StringType)
pltest_Numbers.attributes={pltest_Numbers_float, pltest_Numbers_double, pltest_Numbers_int, pltest_Numbers_long, pltest_Numbers_bigDecimal, pltest_Numbers_bigInt}

# pltest_TestPackageableElement class attributes and methods

# pltest_TestPackage class attributes and methods

# TestPackageableElement class attributes and methods

# pltest_TestClass class attributes and methods

# TestClassifier class attributes and methods

# pltest_TestClassifier class attributes and methods

# pltest_TestInterface class attributes and methods

# pltest_Child2 class attributes and methods

# Child3 class attributes and methods

# pltest_GrandChild class attributes and methods

# Child1 class attributes and methods

# pltest_Child3 class attributes and methods

# pltest_GrandChild2 class attributes and methods

# Child2 class attributes and methods

# pltest_Red class attributes and methods
pltest_Red_redness: Property = Property(name="redness", type=IntegerType)
pltest_Red.attributes={pltest_Red_redness}

# pltest_Circle class attributes and methods
pltest_Circle_area: Property = Property(name="area", type=FloatType)
pltest_Circle_diameter: Property = Property(name="diameter", type=StringType)
pltest_Circle_circumference: Property = Property(name="circumference", type=FloatType)
pltest_Circle.attributes={pltest_Circle_diameter, pltest_Circle_circumference, pltest_Circle_area}

# Relationships
a10: BinaryAssociation = BinaryAssociation(
    name="a10",
    ends={
        Property(name="pltest_Common", type=pltest_Child1, multiplicity=Multiplicity(1, 1)),
        Property(name="pltest_Child1", type=pltest_Common, multiplicity=Multiplicity(0, 1))
    }
)
someRef4: BinaryAssociation = BinaryAssociation(
    name="someRef4",
    ends={
        Property(name="pltest_Circle5", type=pltest_WhatEver, multiplicity=Multiplicity(1, 1)),
        Property(name="pltest_WhatEver", type=pltest_Circle, multiplicity=Multiplicity(0, 1))
    }
)
owningPackage6: BinaryAssociation = BinaryAssociation(
    name="owningPackage6",
    ends={
        Property(name="pltest_TestPackage", type=pltest_TestPackageableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pltest_TestPackageableElement", type=pltest_TestPackage, multiplicity=Multiplicity(0, 1))
    }
)
ownedElements7: BinaryAssociation = BinaryAssociation(
    name="ownedElements7",
    ends={
        Property(name="pltest_TestPackageableElement9", type=pltest_TestPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="pltest_TestPackage8", type=pltest_TestPackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier10: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier10",
    ends={
        Property(name="pltest_TestClassifier", type=pltest_TestClass, multiplicity=Multiplicity(1, 1)),
        Property(name="pltest_TestClass", type=pltest_TestClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a21: BinaryAssociation = BinaryAssociation(
    name="a21",
    ends={
        Property(name="pltest_Common2", type=pltest_Child2, multiplicity=Multiplicity(1, 1)),
        Property(name="pltest_Child2", type=pltest_Common, multiplicity=Multiplicity(0, 1))
    }
)
red3: BinaryAssociation = BinaryAssociation(
    name="red3",
    ends={
        Property(name="pltest_Red", type=pltest_Circle, multiplicity=Multiplicity(1, 1)),
        Property(name="pltest_Circle", type=pltest_Red, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_pltest_Common_Base = Generalization(general=Base, specific=pltest_Common)
gen_pltest_Child1_Common = Generalization(general=Common, specific=pltest_Child1)
gen_pltest_Child1_Interface = Generalization(general=Interface, specific=pltest_Child1)
gen_pltest_GrandChildD_Child3 = Generalization(general=Child3, specific=pltest_GrandChildD)
gen_pltest_GrandGrandChildE_GrandChildD = Generalization(general=GrandChildD, specific=pltest_GrandGrandChildE)
gen_pltest_GrandGrandChildE_Child1 = Generalization(general=Child1, specific=pltest_GrandGrandChildE)
gen_pltest_GrandGrandChildF_GrandChildD = Generalization(general=GrandChildD, specific=pltest_GrandGrandChildF)
gen_pltest_GrandGrandChildF_Child2 = Generalization(general=Child2, specific=pltest_GrandGrandChildF)
gen_pltest_TestPackage_TestPackageableElement = Generalization(general=TestPackageableElement, specific=pltest_TestPackage)
gen_pltest_TestClass_TestClassifier = Generalization(general=TestClassifier, specific=pltest_TestClass)
gen_pltest_TestInterface_TestClassifier = Generalization(general=TestClassifier, specific=pltest_TestInterface)
gen_pltest_Child2_Common = Generalization(general=Common, specific=pltest_Child2)
gen_pltest_Child2_Interface = Generalization(general=Interface, specific=pltest_Child2)
gen_pltest_Child2_Child3 = Generalization(general=Child3, specific=pltest_Child2)
gen_pltest_GrandChild_Child1 = Generalization(general=Child1, specific=pltest_GrandChild)
gen_pltest_GrandChild_Child3 = Generalization(general=Child3, specific=pltest_GrandChild)
gen_pltest_GrandChild2_Child2 = Generalization(general=Child2, specific=pltest_GrandChild2)
gen_pltest_TestClassifier_TestPackageableElement = Generalization(general=TestPackageableElement, specific=pltest_TestClassifier)

# Domain Model
domain_model = DomainModel(
    name="pltest",
    types={pltest_Base, pltest_Common, Base, pltest_Interface, pltest_Child1, Common, Interface, pltest_WhatEver, pltest_GrandChildD, pltest_GrandGrandChildE, GrandChildD, pltest_GrandGrandChildF, pltest_Numbers, pltest_TestPackageableElement, pltest_TestPackage, TestPackageableElement, pltest_TestClass, TestClassifier, pltest_TestClassifier, pltest_TestInterface, pltest_Child2, Child3, pltest_GrandChild, Child1, pltest_Child3, pltest_GrandChild2, Child2, pltest_Red, pltest_Circle},
    associations={a10, someRef4, owningPackage6, ownedElements7, nestedClassifier10, a21, red3},
    generalizations={gen_pltest_Common_Base, gen_pltest_Child1_Common, gen_pltest_Child1_Interface, gen_pltest_GrandChildD_Child3, gen_pltest_GrandGrandChildE_GrandChildD, gen_pltest_GrandGrandChildE_Child1, gen_pltest_GrandGrandChildF_GrandChildD, gen_pltest_GrandGrandChildF_Child2, gen_pltest_TestPackage_TestPackageableElement, gen_pltest_TestClass_TestClassifier, gen_pltest_TestInterface_TestClassifier, gen_pltest_Child2_Common, gen_pltest_Child2_Interface, gen_pltest_Child2_Child3, gen_pltest_GrandChild_Child1, gen_pltest_GrandChild_Child3, gen_pltest_GrandChild2_Child2, gen_pltest_TestClassifier_TestPackageableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)