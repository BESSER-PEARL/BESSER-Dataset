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
RobyOneKenoby_Not = Class(name="RobyOneKenoby_Not")
Test = Class(name="Test")
RobyOneKenoby_And = Class(name="RobyOneKenoby_And")
RobyOneKenoby_Obstacle = Class(name="RobyOneKenoby_Obstacle")
RobyOneKenoby_HasTurned = Class(name="RobyOneKenoby_HasTurned")
RobyOneKenoby_NewEClass12 = Class(name="RobyOneKenoby_NewEClass12")
Order = Class(name="Order")
RobyOneKenoby_NewEClass13 = Class(name="RobyOneKenoby_NewEClass13")
RobyOneKenoby_NewEClass14 = Class(name="RobyOneKenoby_NewEClass14")
RobyOneKenoby_NewEClass15 = Class(name="RobyOneKenoby_NewEClass15")
RobyOneKenoby_NewEClass16 = Class(name="RobyOneKenoby_NewEClass16")
RobyOneKenoby_LanguageElmt = Class(name="RobyOneKenoby_LanguageElmt", is_abstract=True)
RobyOneKenoby_Test = Class(name="RobyOneKenoby_Test", is_abstract=True)
LanguageElmt = Class(name="LanguageElmt")
RobyOneKenoby_RobyLanguage = Class(name="RobyOneKenoby_RobyLanguage", is_abstract=True)
RobyOneKenoby_Order = Class(name="RobyOneKenoby_Order", is_abstract=True)
RobyOneKenoby_Condition = Class(name="RobyOneKenoby_Condition", is_abstract=True)
RobyOneKenoby_If = Class(name="RobyOneKenoby_If")
Condition = Class(name="Condition")
RobyOneKenoby_While = Class(name="RobyOneKenoby_While")
RobyOneKenoby_NewEClass17 = Class(name="RobyOneKenoby_NewEClass17")
RobyOneKenoby_NewEClass18 = Class(name="RobyOneKenoby_NewEClass18")

# RobyOneKenoby_Not class attributes and methods

# Test class attributes and methods

# RobyOneKenoby_And class attributes and methods

# RobyOneKenoby_Obstacle class attributes and methods

# RobyOneKenoby_HasTurned class attributes and methods

# RobyOneKenoby_NewEClass12 class attributes and methods

# Order class attributes and methods

# RobyOneKenoby_NewEClass13 class attributes and methods

# RobyOneKenoby_NewEClass14 class attributes and methods

# RobyOneKenoby_NewEClass15 class attributes and methods

# RobyOneKenoby_NewEClass16 class attributes and methods

# RobyOneKenoby_LanguageElmt class attributes and methods

# RobyOneKenoby_Test class attributes and methods

# LanguageElmt class attributes and methods

# RobyOneKenoby_RobyLanguage class attributes and methods

# RobyOneKenoby_Order class attributes and methods

# RobyOneKenoby_Condition class attributes and methods

# RobyOneKenoby_If class attributes and methods

# Condition class attributes and methods

# RobyOneKenoby_While class attributes and methods

# RobyOneKenoby_NewEClass17 class attributes and methods

# RobyOneKenoby_NewEClass18 class attributes and methods

# Relationships
test2: BinaryAssociation = BinaryAssociation(
    name="test2",
    ends={
        Property(name="RobyOneKenoby_Test3", type=RobyOneKenoby_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="RobyOneKenoby_Not", type=RobyOneKenoby_Test, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
test4: BinaryAssociation = BinaryAssociation(
    name="test4",
    ends={
        Property(name="RobyOneKenoby_Test5", type=RobyOneKenoby_And, multiplicity=Multiplicity(1, 1)),
        Property(name="RobyOneKenoby_And", type=RobyOneKenoby_Test, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
languageelmt0: BinaryAssociation = BinaryAssociation(
    name="languageelmt0",
    ends={
        Property(name="RobyOneKenoby_LanguageElmt", type=RobyOneKenoby_RobyLanguage, multiplicity=Multiplicity(1, 1)),
        Property(name="RobyOneKenoby_RobyLanguage", type=RobyOneKenoby_LanguageElmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
test1: BinaryAssociation = BinaryAssociation(
    name="test1",
    ends={
        Property(name="RobyOneKenoby_Test", type=RobyOneKenoby_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="RobyOneKenoby_Condition", type=RobyOneKenoby_Test, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_RobyOneKenoby_Not_Test = Generalization(general=Test, specific=RobyOneKenoby_Not)
gen_RobyOneKenoby_And_Test = Generalization(general=Test, specific=RobyOneKenoby_And)
gen_RobyOneKenoby_Obstacle_Test = Generalization(general=Test, specific=RobyOneKenoby_Obstacle)
gen_RobyOneKenoby_HasTurned_Test = Generalization(general=Test, specific=RobyOneKenoby_HasTurned)
gen_RobyOneKenoby_NewEClass12_Order = Generalization(general=Order, specific=RobyOneKenoby_NewEClass12)
gen_RobyOneKenoby_NewEClass13_Order = Generalization(general=Order, specific=RobyOneKenoby_NewEClass13)
gen_RobyOneKenoby_NewEClass14_Order = Generalization(general=Order, specific=RobyOneKenoby_NewEClass14)
gen_RobyOneKenoby_NewEClass15_Order = Generalization(general=Order, specific=RobyOneKenoby_NewEClass15)
gen_RobyOneKenoby_NewEClass16_Order = Generalization(general=Order, specific=RobyOneKenoby_NewEClass16)
gen_RobyOneKenoby_Test_LanguageElmt = Generalization(general=LanguageElmt, specific=RobyOneKenoby_Test)
gen_RobyOneKenoby_Order_LanguageElmt = Generalization(general=LanguageElmt, specific=RobyOneKenoby_Order)
gen_RobyOneKenoby_Condition_LanguageElmt = Generalization(general=LanguageElmt, specific=RobyOneKenoby_Condition)
gen_RobyOneKenoby_If_Condition = Generalization(general=Condition, specific=RobyOneKenoby_If)
gen_RobyOneKenoby_While_Condition = Generalization(general=Condition, specific=RobyOneKenoby_While)
gen_RobyOneKenoby_NewEClass17_Order = Generalization(general=Order, specific=RobyOneKenoby_NewEClass17)
gen_RobyOneKenoby_NewEClass18_Order = Generalization(general=Order, specific=RobyOneKenoby_NewEClass18)

# Domain Model
domain_model = DomainModel(
    name="RobyOneKenoby",
    types={RobyOneKenoby_Not, Test, RobyOneKenoby_And, RobyOneKenoby_Obstacle, RobyOneKenoby_HasTurned, RobyOneKenoby_NewEClass12, Order, RobyOneKenoby_NewEClass13, RobyOneKenoby_NewEClass14, RobyOneKenoby_NewEClass15, RobyOneKenoby_NewEClass16, RobyOneKenoby_LanguageElmt, RobyOneKenoby_Test, LanguageElmt, RobyOneKenoby_RobyLanguage, RobyOneKenoby_Order, RobyOneKenoby_Condition, RobyOneKenoby_If, Condition, RobyOneKenoby_While, RobyOneKenoby_NewEClass17, RobyOneKenoby_NewEClass18},
    associations={test2, test4, languageelmt0, test1},
    generalizations={gen_RobyOneKenoby_Not_Test, gen_RobyOneKenoby_And_Test, gen_RobyOneKenoby_Obstacle_Test, gen_RobyOneKenoby_HasTurned_Test, gen_RobyOneKenoby_NewEClass12_Order, gen_RobyOneKenoby_NewEClass13_Order, gen_RobyOneKenoby_NewEClass14_Order, gen_RobyOneKenoby_NewEClass15_Order, gen_RobyOneKenoby_NewEClass16_Order, gen_RobyOneKenoby_Test_LanguageElmt, gen_RobyOneKenoby_Order_LanguageElmt, gen_RobyOneKenoby_Condition_LanguageElmt, gen_RobyOneKenoby_If_Condition, gen_RobyOneKenoby_While_Condition, gen_RobyOneKenoby_NewEClass17_Order, gen_RobyOneKenoby_NewEClass18_Order},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)