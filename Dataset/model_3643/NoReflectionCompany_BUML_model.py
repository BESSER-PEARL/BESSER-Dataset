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
CompanySizeKind: Enumeration = Enumeration(
    name="CompanySizeKind",
    literals={
            EnumerationLiteral(name="small"),
			EnumerationLiteral(name="medium"),
			EnumerationLiteral(name="large")
    }
)

# Classes
noreflectioncompany_Company = Class(name="noreflectioncompany::Company")
noreflectioncompany_Employee = Class(name="noreflectioncompany::Employee")

# noreflectioncompany_Company class attributes and methods
noreflectioncompany_Company_size: Property = Property(name="size", type=StringType)
noreflectioncompany_Company_name: Property = Property(name="name", type=StringType)
noreflectioncompany_Company_m_dummyInvariant: Method = Method(name="dummyInvariant", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
noreflectioncompany_Company.attributes={noreflectioncompany_Company_name, noreflectioncompany_Company_size}
noreflectioncompany_Company.methods={noreflectioncompany_Company_m_dummyInvariant}

# noreflectioncompany_Employee class attributes and methods
noreflectioncompany_Employee_name: Property = Property(name="name", type=StringType)
noreflectioncompany_Employee_hasNameAsAttribute: Property = Property(name="hasNameAsAttribute", type=BooleanType)
noreflectioncompany_Employee_m_reportsTo: Method = Method(name="reportsTo", parameters={Parameter(name='manager')}, type=BooleanType)
noreflectioncompany_Employee_m_hasNameAsOperation: Method = Method(name="hasNameAsOperation", parameters={}, type=BooleanType)
noreflectioncompany_Employee_m_noManagerImpliesDirectReports: Method = Method(name="noManagerImpliesDirectReports", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
noreflectioncompany_Employee.attributes={noreflectioncompany_Employee_hasNameAsAttribute, noreflectioncompany_Employee_name}
noreflectioncompany_Employee.methods={noreflectioncompany_Employee_m_hasNameAsOperation, noreflectioncompany_Employee_m_reportsTo, noreflectioncompany_Employee_m_noManagerImpliesDirectReports}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="company", type=noreflectioncompany_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Employee", type=noreflectioncompany_Company, multiplicity=Multiplicity(1, 1))
    }
)
manager2: BinaryAssociation = BinaryAssociation(
    name="manager2",
    ends={
        Property(name="noreflectioncompany_Employee", type=noreflectioncompany_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="noreflectioncompany_Employee1", type=noreflectioncompany_Employee, multiplicity=Multiplicity(0, 1))
    }
)
company3: BinaryAssociation = BinaryAssociation(
    name="company3",
    ends={
        Property(name="Company", type=noreflectioncompany_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=noreflectioncompany_Company, multiplicity=Multiplicity(1, 1))
    }
)
reportingChain11: BinaryAssociation = BinaryAssociation(
    name="reportingChain11",
    ends={
        Property(name="noreflectioncompany_Employee12", type=noreflectioncompany_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="noreflectioncompany_Employee10", type=noreflectioncompany_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
directReports5: BinaryAssociation = BinaryAssociation(
    name="directReports5",
    ends={
        Property(name="noreflectioncompany_Employee6", type=noreflectioncompany_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="noreflectioncompany_Employee4", type=noreflectioncompany_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
allReports8: BinaryAssociation = BinaryAssociation(
    name="allReports8",
    ends={
        Property(name="noreflectioncompany_Employee9", type=noreflectioncompany_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="noreflectioncompany_Employee7", type=noreflectioncompany_Employee, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="noreflectioncompany",
    types={noreflectioncompany_Company, noreflectioncompany_Employee, CompanySizeKind},
    associations={employees0, manager2, company3, reportingChain11, directReports5, allReports8},
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