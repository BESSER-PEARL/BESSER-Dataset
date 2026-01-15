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
errors_Errores = Class(name="errors::Errores")
errors_Error = Class(name="errors::Error")
errors_ForeignError = Class(name="errors::ForeignError")
Error = Class(name="Error")
errors_Table = Class(name="errors::Table")
errors_Column = Class(name="errors::Column")
errors_Fk = Class(name="errors::Fk")
errors_Registry = Class(name="errors::Registry")
errors_CheckError = Class(name="errors::CheckError")
errors_Ck = Class(name="errors::Ck")

# errors_Errores class attributes and methods

# errors_Error class attributes and methods
errors_Error_id: Property = Property(name="id", type=StringType)
errors_Error_apply: Property = Property(name="apply", type=StringType)
errors_Error.attributes={errors_Error_apply, errors_Error_id}

# errors_ForeignError class attributes and methods
errors_ForeignError_porcent: Property = Property(name="porcent", type=StringType)
errors_ForeignError.attributes={errors_ForeignError_porcent}

# Error class attributes and methods

# errors_Table class attributes and methods

# errors_Column class attributes and methods

# errors_Fk class attributes and methods

# errors_Registry class attributes and methods

# errors_CheckError class attributes and methods
errors_CheckError_porcent: Property = Property(name="porcent", type=StringType)
errors_CheckError.attributes={errors_CheckError_porcent}

# errors_Ck class attributes and methods

# Relationships
errores0: BinaryAssociation = BinaryAssociation(
    name="errores0",
    ends={
        Property(name="errors_Error", type=errors_Errores, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_Errores", type=errors_Error, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
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
registriesFk9: BinaryAssociation = BinaryAssociation(
    name="registriesFk9",
    ends={
        Property(name="errors_Registry", type=errors_ForeignError, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_ForeignError10", type=errors_Registry, multiplicity=Multiplicity(0, 9999))
    }
)
ck11: BinaryAssociation = BinaryAssociation(
    name="ck11",
    ends={
        Property(name="errors_Ck", type=errors_CheckError, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_CheckError", type=errors_Ck, multiplicity=Multiplicity(0, 1))
    }
)
table12: BinaryAssociation = BinaryAssociation(
    name="table12",
    ends={
        Property(name="errors_Table14", type=errors_CheckError, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_CheckError13", type=errors_Table, multiplicity=Multiplicity(0, 1))
    }
)
registriesCk15: BinaryAssociation = BinaryAssociation(
    name="registriesCk15",
    ends={
        Property(name="errors_Registry17", type=errors_CheckError, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_CheckError16", type=errors_Registry, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_errors_ForeignError_Error = Generalization(general=Error, specific=errors_ForeignError)
gen_errors_CheckError_Error = Generalization(general=Error, specific=errors_CheckError)

# Domain Model
domain_model = DomainModel(
    name="errors",
    types={errors_Errores, errors_Error, errors_ForeignError, Error, errors_Table, errors_Column, errors_Fk, errors_Registry, errors_CheckError, errors_Ck},
    associations={errores0, tableCont1, tableRef2, fkColumns5, fk7, registriesFk9, ck11, table12, registriesCk15},
    generalizations={gen_errors_ForeignError_Error, gen_errors_CheckError_Error},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)