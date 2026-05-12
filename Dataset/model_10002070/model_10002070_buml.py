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
int: Enumeration = Enumeration(
    name="int",
    literals={
            
    }
)

# Classes
Orden = Class(name="Orden")
Alimento = Class(name="Alimento")
Class_ = Class(name="Class")
Class2 = Class(name="Class2")
Vegetariano = Class(name="Vegetariano")
RMS = Class(name="RMS")
Report = Class(name="Report")
Booking = Class(name="Booking")

# Orden class attributes and methods
Orden_orden_Id: Property = Property(name="orden_Id", type=StringType)
Orden_numComensales: Property = Property(name="numComensales", type=IntegerType)
Orden_fecha: Property = Property(name="fecha", type=StringType)
Orden_mesa: Property = Property(name="mesa", type=IntegerType)
Orden_preparada: Property = Property(name="preparada", type=BooleanType)
Orden_servida: Property = Property(name="servida", type=BooleanType)
Orden_pagada: Property = Property(name="pagada", type=BooleanType)
Orden.attributes={Orden_pagada, Orden_mesa, Orden_fecha, Orden_numComensales, Orden_orden_Id, Orden_servida, Orden_preparada}

# Alimento class attributes and methods
Alimento_alimento_Id: Property = Property(name="alimento_Id", type=StringType)
Alimento_nombre: Property = Property(name="nombre", type=StringType)
Alimento_precio: Property = Property(name="precio", type=StringType)
Alimento_refrigeraci_n: Property = Property(name="refrigeraci_n", type=BooleanType)
Alimento.attributes={Alimento_refrigeraci_n, Alimento_precio, Alimento_alimento_Id, Alimento_nombre}

# Class class attributes and methods

# Class2 class attributes and methods

# Vegetariano class attributes and methods
Vegetariano_tipoDieta: Property = Property(name="tipoDieta", type=StringType)
Vegetariano.attributes={Vegetariano_tipoDieta}

# RMS class attributes and methods
RMS_bookings: Property = Property(name="bookings", type=StringType)
RMS.attributes={RMS_bookings}

# Report class attributes and methods
Report_orders: Property = Property(name="orders", type=StringType)
Report_totalSales: Property = Property(name="totalSales", type=StringType)
Report_profit: Property = Property(name="profit", type=StringType)
Report.attributes={Report_orders, Report_profit, Report_totalSales}

# Booking class attributes and methods
Booking_booking_Id: Property = Property(name="booking_Id", type=StringType)
Booking_type: Property = Property(name="type", type=IntegerType)
Booking_name: Property = Property(name="name", type=StringType)
Booking_contact: Property = Property(name="contact", type=StringType)
Booking_date: Property = Property(name="date", type=StringType)
Booking_reservedTables: Property = Property(name="reservedTables", type=StringType)
Booking.attributes={Booking_type, Booking_contact, Booking_reservedTables, Booking_date, Booking_booking_Id, Booking_name}

# Relationships
Order_Food: BinaryAssociation = BinaryAssociation(
    name="Order_Food",
    ends={
        Property(name="incluido_en0", type=Alimento, multiplicity=Multiplicity(1, 9999)),
        Property(name="compuesta_por1", type=Orden, multiplicity=Multiplicity(0, 9999))
    }
)
RMS_Booking: BinaryAssociation = BinaryAssociation(
    name="RMS_Booking",
    ends={
        Property(name="has2", type=Booking, multiplicity=Multiplicity(0, 9999)),
        Property(name="is_in3", type=RMS, multiplicity=Multiplicity(1, 1))
    }
)
Report_RMS: BinaryAssociation = BinaryAssociation(
    name="Report_RMS",
    ends={
        Property(name="generates4", type=RMS, multiplicity=Multiplicity(1, 1)),
        Property(name="is_generated_by5", type=Report, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_miTrgPadEemEXt2Xl4w_3Q",
    types={Orden, Alimento, Class_, Class2, Vegetariano, RMS, Report, Booking, int},
    associations={Order_Food, RMS_Booking, Report_RMS},
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