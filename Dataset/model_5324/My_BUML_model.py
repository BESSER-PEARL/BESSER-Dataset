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
myPackage_MyClass = Class(name="myPackage::MyClass")
myPackage_MyOtherClass = Class(name="myPackage::MyOtherClass")
myPackage_AThirdClass = Class(name="myPackage::AThirdClass")
MyClass = Class(name="MyClass")
myPackage_subPackage_Foo = Class(name="myPackage::subPackage::Foo")
myPackage_subsub_Bar = Class(name="myPackage::subsub::Bar")
myPackage_subsub_Baz = Class(name="myPackage::subsub::Baz")
subsub_Bar = Class(name="subsub::Bar")
subPackage_Foo = Class(name="subPackage::Foo")

# myPackage_MyClass class attributes and methods
myPackage_MyClass_myAttribute: Property = Property(name="myAttribute", type=StringType)
myPackage_MyClass.attributes={myPackage_MyClass_myAttribute}

# myPackage_MyOtherClass class attributes and methods
myPackage_MyOtherClass_otherAttribute: Property = Property(name="otherAttribute", type=StringType)
myPackage_MyOtherClass.attributes={myPackage_MyOtherClass_otherAttribute}

# myPackage_AThirdClass class attributes and methods
myPackage_AThirdClass_thirdAttribute: Property = Property(name="thirdAttribute", type=StringType)
myPackage_AThirdClass.attributes={myPackage_AThirdClass_thirdAttribute}

# MyClass class attributes and methods

# myPackage_subPackage_Foo class attributes and methods

# myPackage_subsub_Bar class attributes and methods
myPackage_subsub_Bar_s: Property = Property(name="s", type=StringType)
myPackage_subsub_Bar.attributes={myPackage_subsub_Bar_s}

# myPackage_subsub_Baz class attributes and methods

# subsub_Bar class attributes and methods

# subPackage_Foo class attributes and methods

# Relationships
otherReference0: BinaryAssociation = BinaryAssociation(
    name="otherReference0",
    ends={
        Property(name="myPackage_MyClass", type=myPackage_MyOtherClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myPackage_MyOtherClass", type=myPackage_MyClass, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myPackage_AThirdClass_MyClass = Generalization(general=MyClass, specific=myPackage_AThirdClass)
gen_myPackage_subPackage_Foo_MyClass = Generalization(general=MyClass, specific=myPackage_subPackage_Foo)
gen_myPackage_subsub_Baz_subsub_Bar = Generalization(general=subsub_Bar, specific=myPackage_subsub_Baz)
gen_myPackage_subsub_Baz_subPackage_Foo = Generalization(general=subPackage_Foo, specific=myPackage_subsub_Baz)

# Domain Model
domain_model = DomainModel(
    name="myPackage",
    types={myPackage_MyClass, myPackage_MyOtherClass, myPackage_AThirdClass, MyClass, myPackage_subPackage_Foo, myPackage_subsub_Bar, myPackage_subsub_Baz, subsub_Bar, subPackage_Foo},
    associations={otherReference0},
    generalizations={gen_myPackage_AThirdClass_MyClass, gen_myPackage_subPackage_Foo_MyClass, gen_myPackage_subsub_Baz_subsub_Bar, gen_myPackage_subsub_Baz_subPackage_Foo},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)