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
package1_SubChild = Class(name="package1::SubChild")
Child4 = Class(name="Child4")
package1_SubChild3 = Class(name="package1::SubChild3")
SubChild = Class(name="SubChild")
package1_subpackage_Child5 = Class(name="package1::subpackage::Child5")
package1_subpackage_Child6 = Class(name="package1::subpackage::Child6")
package1_subpackage_SubChild2 = Class(name="package1::subpackage::SubChild2")
package1_RootClass = Class(name="package1::RootClass")
package1_RootAbstractClass = Class(name="package1::RootAbstractClass", is_abstract=True)
package1_RootInterface = Class(name="package1::RootInterface", is_abstract=True)
package1_Child1 = Class(name="package1::Child1")
RootClass = Class(name="RootClass")
package1_Child2 = Class(name="package1::Child2")
RootAbstractClass = Class(name="RootAbstractClass")
package1_Child3 = Class(name="package1::Child3")
RootInterface = Class(name="RootInterface")
package1_Child4 = Class(name="package1::Child4")

# package1_SubChild class attributes and methods

# Child4 class attributes and methods

# package1_SubChild3 class attributes and methods

# SubChild class attributes and methods

# package1_subpackage_Child5 class attributes and methods

# package1_subpackage_Child6 class attributes and methods

# package1_subpackage_SubChild2 class attributes and methods

# package1_RootClass class attributes and methods

# package1_RootAbstractClass class attributes and methods

# package1_RootInterface class attributes and methods

# package1_Child1 class attributes and methods

# RootClass class attributes and methods

# package1_Child2 class attributes and methods

# RootAbstractClass class attributes and methods

# package1_Child3 class attributes and methods

# RootInterface class attributes and methods

# package1_Child4 class attributes and methods

# Generalizations
gen_package1_Child4_RootClass = Generalization(general=RootClass, specific=package1_Child4)
gen_package1_Child4_RootInterface = Generalization(general=RootInterface, specific=package1_Child4)
gen_package1_SubChild_Child4 = Generalization(general=Child4, specific=package1_SubChild)
gen_package1_SubChild3_RootClass = Generalization(general=RootClass, specific=package1_SubChild3)
gen_package1_SubChild3_SubChild = Generalization(general=SubChild, specific=package1_SubChild3)
gen_package1_subpackage_Child5_RootClass = Generalization(general=RootClass, specific=package1_subpackage_Child5)
gen_package1_subpackage_Child6_RootAbstractClass = Generalization(general=RootAbstractClass, specific=package1_subpackage_Child6)
gen_package1_subpackage_Child6_RootClass = Generalization(general=RootClass, specific=package1_subpackage_Child6)
gen_package1_subpackage_Child6_RootInterface = Generalization(general=RootInterface, specific=package1_subpackage_Child6)
gen_package1_Child1_RootClass = Generalization(general=RootClass, specific=package1_Child1)
gen_package1_Child2_RootAbstractClass = Generalization(general=RootAbstractClass, specific=package1_Child2)
gen_package1_Child3_RootInterface = Generalization(general=RootInterface, specific=package1_Child3)
gen_package1_Child4_RootAbstractClass = Generalization(general=RootAbstractClass, specific=package1_Child4)
gen_package1_subpackage_SubChild2_Child4 = Generalization(general=Child4, specific=package1_subpackage_SubChild2)

# Domain Model
domain_model = DomainModel(
    name="package1",
    types={package1_SubChild, Child4, package1_SubChild3, SubChild, package1_subpackage_Child5, package1_subpackage_Child6, package1_subpackage_SubChild2, package1_RootClass, package1_RootAbstractClass, package1_RootInterface, package1_Child1, RootClass, package1_Child2, RootAbstractClass, package1_Child3, RootInterface, package1_Child4},
    associations={},
    generalizations={gen_package1_Child4_RootClass, gen_package1_Child4_RootInterface, gen_package1_SubChild_Child4, gen_package1_SubChild3_RootClass, gen_package1_SubChild3_SubChild, gen_package1_subpackage_Child5_RootClass, gen_package1_subpackage_Child6_RootAbstractClass, gen_package1_subpackage_Child6_RootClass, gen_package1_subpackage_Child6_RootInterface, gen_package1_Child1_RootClass, gen_package1_Child2_RootAbstractClass, gen_package1_Child3_RootInterface, gen_package1_Child4_RootAbstractClass, gen_package1_subpackage_SubChild2_Child4},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)