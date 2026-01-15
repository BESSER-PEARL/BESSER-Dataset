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
errors_Table = Class(name="errors::Table")
errors_Column = Class(name="errors::Column")
errors_Fk = Class(name="errors::Fk")
errors_Errores = Class(name="errors::Errores")
errors_Error = Class(name="errors::Error", is_abstract=True)
errors_ForeignError = Class(name="errors::ForeignError")
Error = Class(name="Error")

# errors_Table class attributes and methods

# errors_Column class attributes and methods

# errors_Fk class attributes and methods

# errors_Errores class attributes and methods

# errors_Error class attributes and methods
errors_Error_id: Property = Property(name="id", type=IntegerType)
errors_Error_apply: Property = Property(name="apply", type=BooleanType)
errors_Error.attributes={errors_Error_apply, errors_Error_id}

# errors_ForeignError class attributes and methods
errors_ForeignError_porcent: Property = Property(name="porcent", type=IntegerType)
errors_ForeignError.attributes={errors_ForeignError_porcent}

# Error class attributes and methods

# Relationships
tableCont1: BinaryAssociation = BinaryAssociation(
    name="tableCont1",
    ends={
        Property(name="errors_Table", type=errors_ForeignError, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_ForeignError", type=errors_Table, multiplicity=Multiplicity(0, 1))
    }
)
tableRef2: BinaryAssociation = BinaryAssociation(
    name="tableRef2",
    ends={
        Property(name="errors_Table4", type=errors_ForeignError, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_ForeignError3", type=errors_Table, multiplicity=Multiplicity(0, 1))
    }
)
fkColumns5: BinaryAssociation = BinaryAssociation(
    name="fkColumns5",
    ends={
        Property(name="errors_Column", type=errors_ForeignError, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_ForeignError6", type=errors_Column, multiplicity=Multiplicity(0, 9999))
    }
)
fk7: BinaryAssociation = BinaryAssociation(
    name="fk7",
    ends={
        Property(name="errors_Fk", type=errors_ForeignError, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_ForeignError8", type=errors_Fk, multiplicity=Multiplicity(0, 1))
    }
)
errores0: BinaryAssociation = BinaryAssociation(
    name="errores0",
    ends={
        Property(name="errors_Error", type=errors_Errores, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_Errores", type=errors_Error, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_errors_ForeignError_Error = Generalization(general=Error, specific=errors_ForeignError)

# Domain Model
domain_model = DomainModel(
    name="errors",
    types={errors_Table, errors_Column, errors_Fk, errors_Errores, errors_Error, errors_ForeignError, Error},
    associations={tableCont1, tableRef2, fkColumns5, fk7, errores0},
    generalizations={gen_errors_ForeignError_Error},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)