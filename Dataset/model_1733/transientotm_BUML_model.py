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
transientotm_TBook = Class(name="transientotm::TBook")
transientotm_TWriter = Class(name="transientotm::TWriter")

# transientotm_TBook class attributes and methods
transientotm_TBook_title: Property = Property(name="title", type=StringType)
transientotm_TBook.attributes={transientotm_TBook_title}

# transientotm_TWriter class attributes and methods
transientotm_TWriter_name: Property = Property(name="name", type=StringType)
transientotm_TWriter.attributes={transientotm_TWriter_name}

# Relationships
authors0: BinaryAssociation = BinaryAssociation(
    name="authors0",
    ends={
        Property(name="transientotm_TWriter", type=transientotm_TBook, multiplicity=Multiplicity(1, 1)),
        Property(name="transientotm_TBook", type=transientotm_TWriter, multiplicity=Multiplicity(1, 9999))
    }
)
book1: BinaryAssociation = BinaryAssociation(
    name="book1",
    ends={
        Property(name="transientotm_TBook3", type=transientotm_TWriter, multiplicity=Multiplicity(1, 1)),
        Property(name="transientotm_TWriter2", type=transientotm_TBook, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="transientotm",
    types={transientotm_TBook, transientotm_TWriter},
    associations={authors0, book1},
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