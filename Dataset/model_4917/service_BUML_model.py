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
service_Service = Class(name="service::Service")
NamedElement = Class(name="NamedElement")
service_EntityOrView = Class(name="service::EntityOrView")
service_Selection = Class(name="service::Selection")
service_BusinessOperation = Class(name="service::BusinessOperation")
FormalParameterList = Class(name="FormalParameterList")
service_Feature = Class(name="service::Feature")
service_Association = Class(name="service::Association")
service_Predicate = Class(name="service::Predicate")
service_Order = Class(name="service::Order", is_abstract=True)
service_Variable = Class(name="service::Variable")
service_Asc = Class(name="service::Asc")
Order = Class(name="Order")
service_Desc = Class(name="service::Desc")
service_ServiceFeatureReference = Class(name="service::ServiceFeatureReference")
Variable = Class(name="Variable")

# service_Services class attributes and methods

# service_Service class attributes and methods

# NamedElement class attributes and methods

# service_EntityOrView class attributes and methods

# service_Selection class attributes and methods
service_Selection_limit: Property = Property(name="limit", type=IntegerType)
service_Selection_selected: Property = Property(name="selected", type=BooleanType)
service_Selection_distinct: Property = Property(name="distinct", type=BooleanType)
service_Selection.attributes={service_Selection_selected, service_Selection_limit, service_Selection_distinct}

# service_BusinessOperation class attributes and methods
service_BusinessOperation_resultType: Property = Property(name="resultType", type=StringType)
service_BusinessOperation_resultMimeType: Property = Property(name="resultMimeType", type=StringType)
service_BusinessOperation.attributes={service_BusinessOperation_resultMimeType, service_BusinessOperation_resultType}

# FormalParameterList class attributes and methods

# service_Feature class attributes and methods

# service_Association class attributes and methods

# service_Predicate class attributes and methods

# service_Order class attributes and methods

# service_Variable class attributes and methods

# service_Asc class attributes and methods

# Order class attributes and methods

# service_Desc class attributes and methods

# service_ServiceFeatureReference class attributes and methods
service_ServiceFeatureReference_name: Property = Property(name="name", type=StringType)
service_ServiceFeatureReference.attributes={service_ServiceFeatureReference_name}

# Variable class attributes and methods

# Relationships
services0: BinaryAssociation = BinaryAssociation(
    name="services0",
    ends={
        Property(name="service_Service", type=service_Services, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Services", type=service_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serves1: BinaryAssociation = BinaryAssociation(
    name="serves1",
    ends={
        Property(name="service_EntityOrView", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Service2", type=service_EntityOrView, multiplicity=Multiplicity(1, 1))
    }
)
selections3: BinaryAssociation = BinaryAssociation(
    name="selections3",
    ends={
        Property(name="Selection", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="usedBy", type=service_Selection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations4: BinaryAssociation = BinaryAssociation(
    name="operations4",
    ends={
        Property(name="service_BusinessOperation", type=service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Service5", type=service_BusinessOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedBy6: BinaryAssociation = BinaryAssociation(
    name="usedBy6",
    ends={
        Property(name="Service", type=service_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="selections", type=service_Service, multiplicity=Multiplicity(1, 1))
    }
)
fields7: BinaryAssociation = BinaryAssociation(
    name="fields7",
    ends={
        Property(name="service_Feature", type=service_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Selection", type=service_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
joins8: BinaryAssociation = BinaryAssociation(
    name="joins8",
    ends={
        Property(name="service_Association", type=service_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Selection9", type=service_Association, multiplicity=Multiplicity(0, 9999))
    }
)
filter10: BinaryAssociation = BinaryAssociation(
    name="filter10",
    ends={
        Property(name="service_Predicate", type=service_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Selection11", type=service_Predicate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ordering12: BinaryAssociation = BinaryAssociation(
    name="ordering12",
    ends={
        Property(name="service_Order", type=service_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Selection13", type=service_Order, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path14: BinaryAssociation = BinaryAssociation(
    name="path14",
    ends={
        Property(name="service_Variable", type=service_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="service_Order15", type=service_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature16: BinaryAssociation = BinaryAssociation(
    name="feature16",
    ends={
        Property(name="service_Feature17", type=service_ServiceFeatureReference, multiplicity=Multiplicity(1, 1)),
        Property(name="service_ServiceFeatureReference", type=service_Feature, multiplicity=Multiplicity(1, 1))
    }
)
uses18: BinaryAssociation = BinaryAssociation(
    name="uses18",
    ends={
        Property(name="service_Service20", type=service_BusinessOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="service_BusinessOperation19", type=service_Service, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_service_Service_NamedElement = Generalization(general=NamedElement, specific=service_Service)
gen_service_Selection_NamedElement = Generalization(general=NamedElement, specific=service_Selection)
gen_service_Selection_FormalParameterList = Generalization(general=FormalParameterList, specific=service_Selection)
gen_service_Asc_Order = Generalization(general=Order, specific=service_Asc)
gen_service_Desc_Order = Generalization(general=Order, specific=service_Desc)
gen_service_BusinessOperation_NamedElement = Generalization(general=NamedElement, specific=service_BusinessOperation)
gen_service_ServiceFeatureReference_Variable = Generalization(general=Variable, specific=service_ServiceFeatureReference)

# Domain Model
domain_model = DomainModel(
    name="service",
    types={service_Services, service_Service, NamedElement, service_EntityOrView, service_Selection, service_BusinessOperation, FormalParameterList, service_Feature, service_Association, service_Predicate, service_Order, service_Variable, service_Asc, Order, service_Desc, service_ServiceFeatureReference, Variable, OperationResultTypes},
    associations={services0, serves1, selections3, operations4, usedBy6, fields7, joins8, filter10, ordering12, path14, feature16, uses18},
    generalizations={gen_service_Service_NamedElement, gen_service_Selection_NamedElement, gen_service_Selection_FormalParameterList, gen_service_Asc_Order, gen_service_Desc_Order, gen_service_BusinessOperation_NamedElement, gen_service_ServiceFeatureReference_Variable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)