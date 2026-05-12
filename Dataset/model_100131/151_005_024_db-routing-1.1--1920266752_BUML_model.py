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
ResultSetScopeType: Enumeration = Enumeration(
    name="ResultSetScopeType",
    literals={
            EnumerationLiteral(name="EXECUTION"),
			EnumerationLiteral(name="APPLICATION")
    }
)

# Classes
dbrouting_Executor = Class(name="dbrouting_Executor")
dbrouting_DocumentRoot = Class(name="dbrouting_DocumentRoot")
dbrouting_EStringToStringMapEntry = Class(name="dbrouting_EStringToStringMapEntry")
dbrouting_ResultSetRowSelector = Class(name="dbrouting_ResultSetRowSelector")
ElementVisitor = Class(name="ElementVisitor")
dbrouting_ResultSet = Class(name="dbrouting_ResultSet")

# dbrouting_Executor class attributes and methods
dbrouting_Executor_executeBefore: Property = Property(name="executeBefore", type=StringType)
dbrouting_Executor_executeOnElement: Property = Property(name="executeOnElement", type=StringType)
dbrouting_Executor_executeOnElementNS: Property = Property(name="executeOnElementNS", type=StringType)
dbrouting_Executor_statement: Property = Property(name="statement", type=StringType)
dbrouting_Executor_datasource: Property = Property(name="datasource", type=StringType)
dbrouting_Executor.attributes={dbrouting_Executor_executeBefore, dbrouting_Executor_executeOnElementNS, dbrouting_Executor_datasource, dbrouting_Executor_statement, dbrouting_Executor_executeOnElement}

# dbrouting_DocumentRoot class attributes and methods
dbrouting_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
dbrouting_DocumentRoot.attributes={dbrouting_DocumentRoot_mixed}

# dbrouting_EStringToStringMapEntry class attributes and methods

# dbrouting_ResultSetRowSelector class attributes and methods
dbrouting_ResultSetRowSelector_executeBefore: Property = Property(name="executeBefore", type=StringType)
dbrouting_ResultSetRowSelector_resultSetName: Property = Property(name="resultSetName", type=StringType)
dbrouting_ResultSetRowSelector_selectRowOnElement: Property = Property(name="selectRowOnElement", type=StringType)
dbrouting_ResultSetRowSelector_where: Property = Property(name="where", type=StringType)
dbrouting_ResultSetRowSelector_failedSelectError: Property = Property(name="failedSelectError", type=StringType)
dbrouting_ResultSetRowSelector_beanId: Property = Property(name="beanId", type=StringType)
dbrouting_ResultSetRowSelector.attributes={dbrouting_ResultSetRowSelector_failedSelectError, dbrouting_ResultSetRowSelector_where, dbrouting_ResultSetRowSelector_executeBefore, dbrouting_ResultSetRowSelector_beanId, dbrouting_ResultSetRowSelector_resultSetName, dbrouting_ResultSetRowSelector_selectRowOnElement}

# ElementVisitor class attributes and methods

# dbrouting_ResultSet class attributes and methods
dbrouting_ResultSet_name: Property = Property(name="name", type=StringType)
dbrouting_ResultSet_scope: Property = Property(name="scope", type=StringType)
dbrouting_ResultSet_timeToLive: Property = Property(name="timeToLive", type=StringType)
dbrouting_ResultSet.attributes={dbrouting_ResultSet_scope, dbrouting_ResultSet_name, dbrouting_ResultSet_timeToLive}

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="dbrouting_EStringToStringMapEntry", type=dbrouting_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="dbrouting_DocumentRoot", type=dbrouting_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="dbrouting_EStringToStringMapEntry3", type=dbrouting_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="dbrouting_DocumentRoot2", type=dbrouting_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executor4: BinaryAssociation = BinaryAssociation(
    name="executor4",
    ends={
        Property(name="dbrouting_Executor", type=dbrouting_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="dbrouting_DocumentRoot5", type=dbrouting_Executor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultSetRowSelector6: BinaryAssociation = BinaryAssociation(
    name="resultSetRowSelector6",
    ends={
        Property(name="dbrouting_ResultSetRowSelector", type=dbrouting_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="dbrouting_DocumentRoot7", type=dbrouting_ResultSetRowSelector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultSet8: BinaryAssociation = BinaryAssociation(
    name="resultSet8",
    ends={
        Property(name="dbrouting_ResultSet", type=dbrouting_Executor, multiplicity=Multiplicity(1, 1)),
        Property(name="dbrouting_Executor9", type=dbrouting_ResultSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dbrouting_Executor_ElementVisitor = Generalization(general=ElementVisitor, specific=dbrouting_Executor)
gen_dbrouting_ResultSetRowSelector_ElementVisitor = Generalization(general=ElementVisitor, specific=dbrouting_ResultSetRowSelector)

# Domain Model
domain_model = DomainModel(
    name="dbrouting",
    types={dbrouting_Executor, dbrouting_DocumentRoot, dbrouting_EStringToStringMapEntry, dbrouting_ResultSetRowSelector, ElementVisitor, dbrouting_ResultSet, ResultSetScopeType},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, executor4, resultSetRowSelector6, resultSet8},
    generalizations={gen_dbrouting_Executor_ElementVisitor, gen_dbrouting_ResultSetRowSelector_ElementVisitor},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)