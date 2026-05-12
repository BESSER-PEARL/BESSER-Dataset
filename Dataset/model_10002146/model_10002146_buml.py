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
AbstractCSVService_T__Interface = Class(name="AbstractCSVService_T__Interface")
HeaderValidator_Interface = Class(name="HeaderValidator_Interface")
ImportDataValidator_Interface = Class(name="ImportDataValidator_Interface")
StockLevelDTO = Class(name="StockLevelDTO")
StockLevelColumnMapper = Class(name="StockLevelColumnMapper")
IterableCSVToBean_T__Interface = Class(name="IterableCSVToBean_T__Interface")
StockLevelDataService = Class(name="StockLevelDataService")
StockLevelHeaderType = Class(name="StockLevelHeaderType")
StockLevelHeaderValidator = Class(name="StockLevelHeaderValidator")
StockLevelImportService = Class(name="StockLevelImportService")
StockLevelStatusHandler = Class(name="StockLevelStatusHandler")
StockLevelValidator = Class(name="StockLevelValidator")
UserSupplierRepository = Class(name="UserSupplierRepository")
RowError = Class(name="RowError")
ImportResultDTO = Class(name="ImportResultDTO")
StockLevelReporterDTO = Class(name="StockLevelReporterDTO")
SupplierItemDTO = Class(name="SupplierItemDTO")
AbstractCSVResource = Class(name="AbstractCSVResource")
StockLevelImportResource = Class(name="StockLevelImportResource")

# AbstractCSVService_T__Interface class attributes and methods

# HeaderValidator_Interface class attributes and methods

# ImportDataValidator_Interface class attributes and methods

# StockLevelDTO class attributes and methods

# StockLevelColumnMapper class attributes and methods

# IterableCSVToBean_T__Interface class attributes and methods

# StockLevelDataService class attributes and methods

# StockLevelHeaderType class attributes and methods

# StockLevelHeaderValidator class attributes and methods

# StockLevelImportService class attributes and methods

# StockLevelStatusHandler class attributes and methods

# StockLevelValidator class attributes and methods

# UserSupplierRepository class attributes and methods

# RowError class attributes and methods

# ImportResultDTO class attributes and methods

# StockLevelReporterDTO class attributes and methods

# SupplierItemDTO class attributes and methods

# AbstractCSVResource class attributes and methods

# StockLevelImportResource class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_ruzjQIT_EeixsLcCAbqrKQ",
    types={AbstractCSVService_T__Interface, HeaderValidator_Interface, ImportDataValidator_Interface, StockLevelDTO, StockLevelColumnMapper, IterableCSVToBean_T__Interface, StockLevelDataService, StockLevelHeaderType, StockLevelHeaderValidator, StockLevelImportService, StockLevelStatusHandler, StockLevelValidator, UserSupplierRepository, RowError, ImportResultDTO, StockLevelReporterDTO, SupplierItemDTO, AbstractCSVResource, StockLevelImportResource},
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