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
OperationResultTypes: Enumeration = Enumeration(
    name="OperationResultTypes",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="File")
    }
)

# Classes
service_Services = Class(name="service::Services")
service_Expression = Class(name="service::Expression")
FormalParameterList = Class(name="FormalParameterList")
service_Feature = Class(name="service::Feature")
service_Association = Class(name="service::Association")
service_Predicate = Class(name="service::Predicate")
service_Service = Class(name="service::Service")
NamedElement = Class(name="NamedElement")
service_Constant = Class(name="service::Constant")
service_EntityOrView = Class(name="service::EntityOrView")
service_Selection = Class(name="service::Selection")
service_BusinessOperation = Class(name="service::BusinessOperation")
service_ServiceFeatureReference = Class(name="service::ServiceFeatureReference")
service_Asc = Class(name="service::Asc")
Order = Class(name="Order")
service_Desc = Class(name="service::Desc")
NamedDisplayElement = Class(name="NamedDisplayElement")
service_Filter = Class(name="service::Filter")
service_Order = Class(name="service::Order", is_abstract=True)
service_EntityAssociation = Class(name="service::EntityAssociation")
service_Variable = Class(name="service::Variable")
service_ConstantReference = Class(name="service::ConstantReference")
Variable = Class(name="Variable")

# service_Services class attributes and methods

# service_Expression class attributes and methods

# FormalParameterList class attributes and methods

# service_Feature class attributes and methods

# service_Association class attributes and methods

# service_Predicate class attributes and methods

# service_Service class attributes and methods

# NamedElement class attributes and methods

# service_Constant class attributes and methods

# service_EntityOrView class attributes and methods

# service_Selection class attributes and methods
service_Selection_distinct: Property = Property(name="distinct", type=BooleanType)
service_Selection_limit: Property = Property(name="limit", type=IntegerType)
service_Selection_methodName: Property = Property(name="methodName", type=StringType)
service_Selection.attributes={service_Selection_limit, service_Selection_methodName, service_Selection_distinct}

# service_BusinessOperation class attributes and methods
service_BusinessOperation_resultType: Property = Property(name="resultType", type=StringType)
service_BusinessOperation_resultMimeType: Property = Property(name="resultMimeType", type=StringType)
service_BusinessOperation.attributes={service_BusinessOperation_resultType, service_BusinessOperation_resultMimeType}

# service_ServiceFeatureReference class attributes and methods
service_ServiceFeatureReference_name: Property = Property(name="name", type=StringType)
service_ServiceFeatureReference.attributes={service_ServiceFeatureReference_name}

# service_Asc class attributes and methods

# Order class attributes and methods

# service_Desc class attributes and methods

# NamedDisplayElement class attributes and methods

# service_Filter class attributes and methods
service_Filter_methodName: Property = Property(name="methodName", type=StringType)
service_Filter.attributes={service_Filter_methodName}

# service_Order class attributes and methods

# service_EntityAssociation class attributes and methods

# service_Variable class attributes and methods

# service_ConstantReference class attributes and methods
service_ConstantReference_name: Property = Property(name="name", type=StringType)
service_ConstantReference.attributes={service_ConstantReference_name}

# Variable class attributes and methods

# Relationships
uses13: BinaryAssociation = BinaryAssociation(
    name="uses13",
    ends={
        Property(name="service_Service14", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Service12", type=service_Service, multiplicity=Multiplicity(0, 9999))
    }
)
definedBy15: BinaryAssociation = BinaryAssociation(
    name="definedBy15",
    ends={
        Property(name="Service", type=service_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="constants", type=service_Service, multiplicity=Multiplicity(1, 1))
    }
)
value16: BinaryAssociation = BinaryAssociation(
    name="value16",
    ends={
        Property(name="service_Expression", type=service_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Constant", type=service_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usedBy17: BinaryAssociation = BinaryAssociation(
    name="usedBy17",
    ends={
        Property(name="Service18", type=service_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="selections", type=service_Service, multiplicity=Multiplicity(1, 1))
    }
)
fields19: BinaryAssociation = BinaryAssociation(
    name="fields19",
    ends={
        Property(name="service_Feature", type=service_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Selection20", type=service_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
joins21: BinaryAssociation = BinaryAssociation(
    name="joins21",
    ends={
        Property(name="service_Association", type=service_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Selection22", type=service_Association, multiplicity=Multiplicity(0, 9999))
    }
)
condition23: BinaryAssociation = BinaryAssociation(
    name="condition23",
    ends={
        Property(name="service_Predicate", type=service_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Selection24", type=service_Predicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
services0: BinaryAssociation = BinaryAssociation(
    name="services0",
    ends={
        Property(name="service_Service", type=service_Services, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Services", type=service_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constants1: BinaryAssociation = BinaryAssociation(
    name="constants1",
    ends={
        Property(name="Constant", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="definedBy", type=service_Constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serves2: BinaryAssociation = BinaryAssociation(
    name="serves2",
    ends={
        Property(name="service_EntityOrView", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Service3", type=service_EntityOrView, multiplicity=Multiplicity(0, 1))
    }
)
selections4: BinaryAssociation = BinaryAssociation(
    name="selections4",
    ends={
        Property(name="Selection", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="usedBy", type=service_Selection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
findAll5: BinaryAssociation = BinaryAssociation(
    name="findAll5",
    ends={
        Property(name="service_Selection", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Service6", type=service_Selection, multiplicity=Multiplicity(0, 1))
    }
)
findOne7: BinaryAssociation = BinaryAssociation(
    name="findOne7",
    ends={
        Property(name="service_Selection9", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Service8", type=service_Selection, multiplicity=Multiplicity(0, 1))
    }
)
operations10: BinaryAssociation = BinaryAssociation(
    name="operations10",
    ends={
        Property(name="BusinessOperation", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="definedBy11", type=service_BusinessOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature34: BinaryAssociation = BinaryAssociation(
    name="feature34",
    ends={
        Property(name="service_Feature35", type=service_ServiceFeatureReference, multiplicity=Multiplicity(1, 1)),
        Property(name="service_ServiceFeatureReference", type=service_Feature, multiplicity=Multiplicity(1, 1))
    }
)
definedBy36: BinaryAssociation = BinaryAssociation(
    name="definedBy36",
    ends={
        Property(name="Service37", type=service_BusinessOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="operations", type=service_Service, multiplicity=Multiplicity(0, 1))
    }
)
uses38: BinaryAssociation = BinaryAssociation(
    name="uses38",
    ends={
        Property(name="service_Service39", type=service_BusinessOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="service_BusinessOperation", type=service_Service, multiplicity=Multiplicity(0, 9999))
    }
)
filters25: BinaryAssociation = BinaryAssociation(
    name="filters25",
    ends={
        Property(name="Filter", type=service_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="selection", type=service_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ordering26: BinaryAssociation = BinaryAssociation(
    name="ordering26",
    ends={
        Property(name="service_Order", type=service_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Selection27", type=service_Order, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectPath28: BinaryAssociation = BinaryAssociation(
    name="selectPath28",
    ends={
        Property(name="service_EntityAssociation", type=service_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Selection29", type=service_EntityAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
path30: BinaryAssociation = BinaryAssociation(
    name="path30",
    ends={
        Property(name="service_Variable", type=service_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Order31", type=service_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value32: BinaryAssociation = BinaryAssociation(
    name="value32",
    ends={
        Property(name="service_Constant33", type=service_ConstantReference, multiplicity=Multiplicity(1, 1)),
        Property(name="service_ConstantReference", type=service_Constant, multiplicity=Multiplicity(1, 1))
    }
)
selection40: BinaryAssociation = BinaryAssociation(
    name="selection40",
    ends={
        Property(name="Selection41", type=service_Filter, multiplicity=Multiplicity(1, 1)),
        Property(name="filters", type=service_Selection, multiplicity=Multiplicity(0, 1))
    }
)
condition42: BinaryAssociation = BinaryAssociation(
    name="condition42",
    ends={
        Property(name="service_Predicate43", type=service_Filter, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Filter", type=service_Predicate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_service_Constant_NamedElement = Generalization(general=NamedElement, specific=service_Constant)
gen_service_Selection_NamedElement = Generalization(general=NamedElement, specific=service_Selection)
gen_service_Selection_FormalParameterList = Generalization(general=FormalParameterList, specific=service_Selection)
gen_service_Service_NamedElement = Generalization(general=NamedElement, specific=service_Service)
gen_service_ServiceFeatureReference_Variable = Generalization(general=Variable, specific=service_ServiceFeatureReference)
gen_service_Asc_Order = Generalization(general=Order, specific=service_Asc)
gen_service_Desc_Order = Generalization(general=Order, specific=service_Desc)
gen_service_BusinessOperation_NamedElement = Generalization(general=NamedElement, specific=service_BusinessOperation)
gen_service_BusinessOperation_FormalParameterList = Generalization(general=FormalParameterList, specific=service_BusinessOperation)
gen_service_Filter_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=service_Filter)
gen_service_Filter_FormalParameterList = Generalization(general=FormalParameterList, specific=service_Filter)
gen_service_ConstantReference_Variable = Generalization(general=Variable, specific=service_ConstantReference)

# Domain Model
domain_model = DomainModel(
    name="service",
    types={service_Services, service_Expression, FormalParameterList, service_Feature, service_Association, service_Predicate, service_Service, NamedElement, service_Constant, service_EntityOrView, service_Selection, service_BusinessOperation, service_ServiceFeatureReference, service_Asc, Order, service_Desc, NamedDisplayElement, service_Filter, service_Order, service_EntityAssociation, service_Variable, service_ConstantReference, Variable, OperationResultTypes},
    associations={uses13, definedBy15, value16, usedBy17, fields19, joins21, condition23, services0, constants1, serves2, selections4, findAll5, findOne7, operations10, feature34, definedBy36, uses38, filters25, ordering26, selectPath28, path30, value32, selection40, condition42},
    generalizations={gen_service_Constant_NamedElement, gen_service_Selection_NamedElement, gen_service_Selection_FormalParameterList, gen_service_Service_NamedElement, gen_service_ServiceFeatureReference_Variable, gen_service_Asc_Order, gen_service_Desc_Order, gen_service_BusinessOperation_NamedElement, gen_service_BusinessOperation_FormalParameterList, gen_service_Filter_NamedDisplayElement, gen_service_Filter_FormalParameterList, gen_service_ConstantReference_Variable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)