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
custostorage_A = Class(name="custostorage::A")
custostorage_B = Class(name="custostorage::B")
custostorage_C = Class(name="custostorage::C")
custostorage_D = Class(name="custostorage::D")
custostorage_E = Class(name="custostorage::E")
custostorage_F = Class(name="custostorage::F")
custostorage_AAbstract = Class(name="custostorage::AAbstract", is_abstract=True)
custostorage_BAbstract = Class(name="custostorage::BAbstract", is_abstract=True)
custostorage_CAbstract = Class(name="custostorage::CAbstract", is_abstract=True)
custostorage_DAbstract = Class(name="custostorage::DAbstract", is_abstract=True)
custostorage_EAbstract = Class(name="custostorage::EAbstract", is_abstract=True)
custostorage_FAbstract = Class(name="custostorage::FAbstract", is_abstract=True)

# custostorage_A class attributes and methods

# custostorage_B class attributes and methods

# custostorage_C class attributes and methods

# custostorage_D class attributes and methods

# custostorage_E class attributes and methods

# custostorage_F class attributes and methods

# custostorage_AAbstract class attributes and methods

# custostorage_BAbstract class attributes and methods

# custostorage_CAbstract class attributes and methods

# custostorage_DAbstract class attributes and methods

# custostorage_EAbstract class attributes and methods

# custostorage_FAbstract class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="custostorage",
    types={custostorage_A, custostorage_B, custostorage_C, custostorage_D, custostorage_E, custostorage_F, custostorage_AAbstract, custostorage_BAbstract, custostorage_CAbstract, custostorage_DAbstract, custostorage_EAbstract, custostorage_FAbstract},
    associations={},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)