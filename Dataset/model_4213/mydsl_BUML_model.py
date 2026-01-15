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
mydsl_MyModel = Class(name="mydsl::MyModel")
mydsl_MyAbstractElement = Class(name="mydsl::MyAbstractElement", is_abstract=True)
mydsl_MyElement = Class(name="mydsl::MyElement")
MyAbstractElement = Class(name="MyAbstractElement")
mydsl_MyReference = Class(name="mydsl::MyReference")

# mydsl_MyModel class attributes and methods
mydsl_MyModel_name: Property = Property(name="name", type=StringType)
mydsl_MyModel.attributes={mydsl_MyModel_name}

# mydsl_MyAbstractElement class attributes and methods

# mydsl_MyElement class attributes and methods
mydsl_MyElement_name: Property = Property(name="name", type=StringType)
mydsl_MyElement.attributes={mydsl_MyElement_name}

# MyAbstractElement class attributes and methods

# mydsl_MyReference class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="mydsl_MyAbstractElement", type=mydsl_MyModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_MyModel", type=mydsl_MyAbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element1: BinaryAssociation = BinaryAssociation(
    name="element1",
    ends={
        Property(name="mydsl_MyElement", type=mydsl_MyReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_MyReference", type=mydsl_MyElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mydsl_MyElement_MyAbstractElement = Generalization(general=MyAbstractElement, specific=mydsl_MyElement)
gen_mydsl_MyReference_MyAbstractElement = Generalization(general=MyAbstractElement, specific=mydsl_MyReference)

# Domain Model
domain_model = DomainModel(
    name="mydsl",
    types={mydsl_MyModel, mydsl_MyAbstractElement, mydsl_MyElement, MyAbstractElement, mydsl_MyReference},
    associations={elements0, element1},
    generalizations={gen_mydsl_MyElement_MyAbstractElement, gen_mydsl_MyReference_MyAbstractElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)