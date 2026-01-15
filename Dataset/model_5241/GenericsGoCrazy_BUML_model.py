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
Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="BLUE")
    }
)

# Classes
genericsGoCrazy_MyClass = Class(name="genericsGoCrazy::MyClass")
genericsGoCrazy_Car = Class(name="genericsGoCrazy::Car")
genericsGoCrazy_MySubClass = Class(name="genericsGoCrazy::MySubClass")
genericsGoCrazy_Comp = Class(name="genericsGoCrazy::Comp")
genericsGoCrazy_SubCar = Class(name="genericsGoCrazy::SubCar")
Car = Class(name="Car")
genericsGoCrazy_OtherClass = Class(name="genericsGoCrazy::OtherClass")

# genericsGoCrazy_MyClass class attributes and methods
genericsGoCrazy_MyClass_a1: Property = Property(name="a1", type=StringType)
genericsGoCrazy_MyClass_a2: Property = Property(name="a2", type=StringType)
genericsGoCrazy_MyClass_a3: Property = Property(name="a3", type=StringType)
genericsGoCrazy_MyClass_theEObject: Property = Property(name="theEObject", type=StringType)
genericsGoCrazy_MyClass_aMap: Property = Property(name="aMap", type=StringType)
genericsGoCrazy_MyClass_m_bar: Method = Method(name="bar", parameters={Parameter(name='aF'), Parameter(name='aT'), Parameter(name='ts')})
genericsGoCrazy_MyClass.attributes={genericsGoCrazy_MyClass_aMap, genericsGoCrazy_MyClass_a2, genericsGoCrazy_MyClass_a3, genericsGoCrazy_MyClass_theEObject, genericsGoCrazy_MyClass_a1}
genericsGoCrazy_MyClass.methods={genericsGoCrazy_MyClass_m_bar}

# genericsGoCrazy_Car class attributes and methods
genericsGoCrazy_Car_name: Property = Property(name="name", type=StringType)
genericsGoCrazy_Car_fullName: Property = Property(name="fullName", type=StringType)
genericsGoCrazy_Car_doors: Property = Property(name="doors", type=StringType)
genericsGoCrazy_Car_color: Property = Property(name="color", type=StringType)
genericsGoCrazy_Car_m_foo: Method = Method(name="foo", parameters={Parameter(name='a')})
genericsGoCrazy_Car_m_enhancedFoo: Method = Method(name="enhancedFoo", parameters={Parameter(name='aT'), Parameter(name='aInt')})
genericsGoCrazy_Car_m_superFoo: Method = Method(name="superFoo", parameters={Parameter(name='key')})
genericsGoCrazy_Car.attributes={genericsGoCrazy_Car_fullName, genericsGoCrazy_Car_color, genericsGoCrazy_Car_name, genericsGoCrazy_Car_doors}
genericsGoCrazy_Car.methods={genericsGoCrazy_Car_m_foo, genericsGoCrazy_Car_m_enhancedFoo, genericsGoCrazy_Car_m_superFoo}

# genericsGoCrazy_MySubClass class attributes and methods

# genericsGoCrazy_Comp class attributes and methods

# genericsGoCrazy_SubCar class attributes and methods

# Car class attributes and methods

# genericsGoCrazy_OtherClass class attributes and methods

# Relationships
previousCar1: BinaryAssociation = BinaryAssociation(
    name="previousCar1",
    ends={
        Property(name="genericsGoCrazy_Car", type=genericsGoCrazy_Car, multiplicity=Multiplicity(1, 1)),
        Property(name="genericsGoCrazy_Car0", type=genericsGoCrazy_Car, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_genericsGoCrazy_SubCar_Car = Generalization(general=Car, specific=genericsGoCrazy_SubCar)

# Domain Model
domain_model = DomainModel(
    name="genericsGoCrazy",
    types={genericsGoCrazy_MyClass, genericsGoCrazy_Car, genericsGoCrazy_MySubClass, genericsGoCrazy_Comp, genericsGoCrazy_SubCar, Car, genericsGoCrazy_OtherClass, Color},
    associations={previousCar1},
    generalizations={gen_genericsGoCrazy_SubCar_Car},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)