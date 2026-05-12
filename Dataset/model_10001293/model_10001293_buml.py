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
Monopoly = Class(name="Monopoly")
Tarjeta = Class(name="Tarjeta")
TPagarBanco = Class(name="TPagarBanco")
TPagarJugadores = Class(name="TPagarJugadores")
TCobrarBanco = Class(name="TCobrarBanco")
TAvanzar = Class(name="TAvanzar")
TAvanzarPagarDoble = Class(name="TAvanzarPagarDoble")
Monopoly1 = Class(name="Monopoly1")
TIrACarcel = Class(name="TIrACarcel")
TCobrarJugadores = Class(name="TCobrarJugadores")
Jugador = Class(name="Jugador")
Dados = Class(name="Dados")
Casilla = Class(name="Casilla")
Titulo = Class(name="Titulo")
TituloPropiedad = Class(name="TituloPropiedad")
TituloFerrocarril = Class(name="TituloFerrocarril")
TituloServicio = Class(name="TituloServicio")
Servicio = Class(name="Servicio")
Propiedad = Class(name="Propiedad")
Ferrocarril = Class(name="Ferrocarril")
ParqueoLibre = Class(name="ParqueoLibre")
IrACarcel = Class(name="IrACarcel")
Carcel = Class(name="Carcel")
Salida = Class(name="Salida")
CasillaTarjeta = Class(name="CasillaTarjeta")
Impuestos = Class(name="Impuestos")
TSalirCarcel = Class(name="TSalirCarcel")
Tarjeta1 = Class(name="Tarjeta1")
TPagarBanco1 = Class(name="TPagarBanco1")
TPagarPorEdificios = Class(name="TPagarPorEdificios")
TCobrarJugadores1 = Class(name="TCobrarJugadores1")
TAvanzar1 = Class(name="TAvanzar1")
TAvanzarPagarDoble1 = Class(name="TAvanzarPagarDoble1")
TIrACarcel1 = Class(name="TIrACarcel1")
TCobrarBanco1 = Class(name="TCobrarBanco1")
TPagarJugadores1 = Class(name="TPagarJugadores1")
TPagarPorEdificios1 = Class(name="TPagarPorEdificios1")

# Monopoly class attributes and methods

# Tarjeta class attributes and methods

# TPagarBanco class attributes and methods

# TPagarJugadores class attributes and methods

# TCobrarBanco class attributes and methods

# TAvanzar class attributes and methods

# TAvanzarPagarDoble class attributes and methods

# Monopoly1 class attributes and methods
Monopoly1_attribute: Property = Property(name="attribute", type=StringType)
Monopoly1.attributes={Monopoly1_attribute}

# TIrACarcel class attributes and methods

# TCobrarJugadores class attributes and methods

# Jugador class attributes and methods

# Dados class attributes and methods

# Casilla class attributes and methods

# Titulo class attributes and methods

# TituloPropiedad class attributes and methods

# TituloFerrocarril class attributes and methods

# TituloServicio class attributes and methods

# Servicio class attributes and methods

# Propiedad class attributes and methods

# Ferrocarril class attributes and methods

# ParqueoLibre class attributes and methods

# IrACarcel class attributes and methods

# Carcel class attributes and methods

# Salida class attributes and methods

# CasillaTarjeta class attributes and methods

# Impuestos class attributes and methods

# TSalirCarcel class attributes and methods

# Tarjeta1 class attributes and methods
Tarjeta1_tipoDeCarta: Property = Property(name="tipoDeCarta", type=StringType)
Tarjeta1_descripcion: Property = Property(name="descripcion", type=StringType)
Tarjeta1.attributes={Tarjeta1_tipoDeCarta, Tarjeta1_descripcion}

# TPagarBanco1 class attributes and methods
TPagarBanco1_monto: Property = Property(name="monto", type=IntegerType)
TPagarBanco1.attributes={TPagarBanco1_monto}

# TPagarPorEdificios class attributes and methods

# TCobrarJugadores1 class attributes and methods
TCobrarJugadores1_monto: Property = Property(name="monto", type=IntegerType)
TCobrarJugadores1.attributes={TCobrarJugadores1_monto}

# TAvanzar1 class attributes and methods

# TAvanzarPagarDoble1 class attributes and methods

# TIrACarcel1 class attributes and methods

# TCobrarBanco1 class attributes and methods

# TPagarJugadores1 class attributes and methods
TPagarJugadores1_monto: Property = Property(name="monto", type=IntegerType)
TPagarJugadores1.attributes={TPagarJugadores1_monto}

# TPagarPorEdificios1 class attributes and methods

# Relationships
Monopoly_Jugador: BinaryAssociation = BinaryAssociation(
    name="Monopoly_Jugador",
    ends={
        Property(name="Monopoly_Jugador_018", type=Jugador, multiplicity=Multiplicity(0, 9999)),
        Property(name="Monopoly_Jugador_119", type=Monopoly, multiplicity=Multiplicity(1, 1))
    }
)
Monopoly_Jugador2: BinaryAssociation = BinaryAssociation(
    name="Monopoly_Jugador2",
    ends={
        Property(name="_actual20", type=Jugador, multiplicity=Multiplicity(1, 1)),
        Property(name="Monopoly_Jugador2_121", type=Monopoly, multiplicity=Multiplicity(1, 1))
    }
)
Monopoly_Tarjeta: BinaryAssociation = BinaryAssociation(
    name="Monopoly_Tarjeta",
    ends={
        Property(name="_fortuna0", type=Tarjeta, multiplicity=Multiplicity(0, 9999)),
        Property(name="Monopoly_Tarjeta_11", type=Monopoly, multiplicity=Multiplicity(1, 1))
    }
)
Monopoly_Tarjeta2: BinaryAssociation = BinaryAssociation(
    name="Monopoly_Tarjeta2",
    ends={
        Property(name="_arcaComunal2", type=Tarjeta, multiplicity=Multiplicity(0, 9999)),
        Property(name="monopoly3", type=Monopoly, multiplicity=Multiplicity(1, 1))
    }
)
Monopoly_Dados: BinaryAssociation = BinaryAssociation(
    name="Monopoly_Dados",
    ends={
        Property(name="Monopoly_Dados_04", type=Dados, multiplicity=Multiplicity(1, 1)),
        Property(name="Monopoly_Dados_15", type=Monopoly, multiplicity=Multiplicity(1, 1))
    }
)
Servicio_TituloServicio: BinaryAssociation = BinaryAssociation(
    name="Servicio_TituloServicio",
    ends={
        Property(name="Servicio_TituloServicio_06", type=TituloServicio, multiplicity=Multiplicity(1, 1)),
        Property(name="Servicio_TituloServicio_17", type=Servicio, multiplicity=Multiplicity(1, 1))
    }
)
Ferrocarril_TituloFerrocarril: BinaryAssociation = BinaryAssociation(
    name="Ferrocarril_TituloFerrocarril",
    ends={
        Property(name="Ferrocarril_TituloFerrocarril_08", type=TituloFerrocarril, multiplicity=Multiplicity(1, 1)),
        Property(name="Ferrocarril_TituloFerrocarril_19", type=Ferrocarril, multiplicity=Multiplicity(1, 1))
    }
)
Propiedad_TituloPropiedad: BinaryAssociation = BinaryAssociation(
    name="Propiedad_TituloPropiedad",
    ends={
        Property(name="Propiedad_TituloPropiedad_010", type=TituloPropiedad, multiplicity=Multiplicity(1, 1)),
        Property(name="Propiedad_TituloPropiedad_111", type=Propiedad, multiplicity=Multiplicity(1, 1))
    }
)
Jugador_Titulo: BinaryAssociation = BinaryAssociation(
    name="Jugador_Titulo",
    ends={
        Property(name="Jugador_Titulo_012", type=Titulo, multiplicity=Multiplicity(0, 9999)),
        Property(name="Jugador_Titulo_113", type=Jugador, multiplicity=Multiplicity(1, 1))
    }
)
Jugador_TSalirCarcel: BinaryAssociation = BinaryAssociation(
    name="Jugador_TSalirCarcel",
    ends={
        Property(name="Jugador_TSalirCarcel_014", type=TSalirCarcel, multiplicity=Multiplicity(0, 1)),
        Property(name="Jugador_TSalirCarcel_115", type=Jugador, multiplicity=Multiplicity(1, 1))
    }
)
Monopoly_Casilla: BinaryAssociation = BinaryAssociation(
    name="Monopoly_Casilla",
    ends={
        Property(name="_tablero16", type=Casilla, multiplicity=Multiplicity(0, 9999)),
        Property(name="Monopoly_Casilla_117", type=Monopoly, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9f11bb33_4300_4f4b_9d83_39070c79552f",
    types={Monopoly, Tarjeta, TPagarBanco, TPagarJugadores, TCobrarBanco, TAvanzar, TAvanzarPagarDoble, Monopoly1, TIrACarcel, TCobrarJugadores, Jugador, Dados, Casilla, Titulo, TituloPropiedad, TituloFerrocarril, TituloServicio, Servicio, Propiedad, Ferrocarril, ParqueoLibre, IrACarcel, Carcel, Salida, CasillaTarjeta, Impuestos, TSalirCarcel, Tarjeta1, TPagarBanco1, TPagarPorEdificios, TCobrarJugadores1, TAvanzar1, TAvanzarPagarDoble1, TIrACarcel1, TCobrarBanco1, TPagarJugadores1, TPagarPorEdificios1},
    associations={Monopoly_Jugador, Monopoly_Jugador2, Monopoly_Tarjeta, Monopoly_Tarjeta2, Monopoly_Dados, Servicio_TituloServicio, Ferrocarril_TituloFerrocarril, Propiedad_TituloPropiedad, Jugador_Titulo, Jugador_TSalirCarcel, Monopoly_Casilla},
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