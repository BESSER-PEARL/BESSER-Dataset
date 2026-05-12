import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Clasificar_Producto_external,
    Generar_ordenes_de_pedidos_external,
    Recibir_ordenes_de_suministro_external,
    Recibir_productos_y_pedidos_external,
    Registrar_proveedores_external,
    Servidor_intel_i8_Node,
    _reasConocimiento,
    Departamento,
    Profesores,
    Sistema_desplegable,
    Sistema_Electrico,
    PlanosTerreno,
    Ejecuci_n,
    Encargos,
    facturas_pagos_,
    Comprador,
    Historial_trabajadores,
    Trabajadores,
    Permisos,
    Planos,
    Obras,
    Pedidos,
    SolucitudSuministro,
    Factura,
    Dependencia,
    Proveedores,
    Elementos,
    OrdenesPedido,
    Sistema_WEB_Movil___Recceci_n_de_pedidos_Component,
    Actor_Actor,
    Dependencia_Actor,
    Proveedores_Actor,
    Departamento_de_Inventarios_y_Suministros___Dis_Component,
    Juridica_Actor,
    Natural_Actor,
    Departamento_de_contabilidad_y_tesoreria_Actor,
    Mileninum_Component,
    Brinda_consultoria_external,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_clasificar_producto_external_is_not_abstract():
    assert not inspect.isabstract(Clasificar_Producto_external)


def test_clasificar_producto_external_constructor_exists():
    assert callable(Clasificar_Producto_external.__init__)


def test_clasificar_producto_external_constructor_args():
    sig = inspect.signature(Clasificar_Producto_external.__init__)
    params = list(sig.parameters.keys())



def test_generar_ordenes_de_pedidos_external_is_not_abstract():
    assert not inspect.isabstract(Generar_ordenes_de_pedidos_external)


def test_generar_ordenes_de_pedidos_external_constructor_exists():
    assert callable(Generar_ordenes_de_pedidos_external.__init__)


def test_generar_ordenes_de_pedidos_external_constructor_args():
    sig = inspect.signature(Generar_ordenes_de_pedidos_external.__init__)
    params = list(sig.parameters.keys())



def test_recibir_ordenes_de_suministro_external_is_not_abstract():
    assert not inspect.isabstract(Recibir_ordenes_de_suministro_external)


def test_recibir_ordenes_de_suministro_external_constructor_exists():
    assert callable(Recibir_ordenes_de_suministro_external.__init__)


def test_recibir_ordenes_de_suministro_external_constructor_args():
    sig = inspect.signature(Recibir_ordenes_de_suministro_external.__init__)
    params = list(sig.parameters.keys())



def test_recibir_productos_y_pedidos_external_is_not_abstract():
    assert not inspect.isabstract(Recibir_productos_y_pedidos_external)


def test_recibir_productos_y_pedidos_external_constructor_exists():
    assert callable(Recibir_productos_y_pedidos_external.__init__)


def test_recibir_productos_y_pedidos_external_constructor_args():
    sig = inspect.signature(Recibir_productos_y_pedidos_external.__init__)
    params = list(sig.parameters.keys())



def test_registrar_proveedores_external_is_not_abstract():
    assert not inspect.isabstract(Registrar_proveedores_external)


def test_registrar_proveedores_external_constructor_exists():
    assert callable(Registrar_proveedores_external.__init__)


def test_registrar_proveedores_external_constructor_args():
    sig = inspect.signature(Registrar_proveedores_external.__init__)
    params = list(sig.parameters.keys())



def test_servidor_intel_i8_node_is_not_abstract():
    assert not inspect.isabstract(Servidor_intel_i8_Node)


def test_servidor_intel_i8_node_constructor_exists():
    assert callable(Servidor_intel_i8_Node.__init__)


def test_servidor_intel_i8_node_constructor_args():
    sig = inspect.signature(Servidor_intel_i8_Node.__init__)
    params = list(sig.parameters.keys())



def test__reasconocimiento_is_not_abstract():
    assert not inspect.isabstract(_reasConocimiento)


def test__reasconocimiento_constructor_exists():
    assert callable(_reasConocimiento.__init__)


def test__reasconocimiento_constructor_args():
    sig = inspect.signature(_reasConocimiento.__init__)
    params = list(sig.parameters.keys())



def test_departamento_is_not_abstract():
    assert not inspect.isabstract(Departamento)


def test_departamento_constructor_exists():
    assert callable(Departamento.__init__)


def test_departamento_constructor_args():
    sig = inspect.signature(Departamento.__init__)
    params = list(sig.parameters.keys())



def test_profesores_is_not_abstract():
    assert not inspect.isabstract(Profesores)


def test_profesores_constructor_exists():
    assert callable(Profesores.__init__)


def test_profesores_constructor_args():
    sig = inspect.signature(Profesores.__init__)
    params = list(sig.parameters.keys())



def test_sistema_desplegable_is_not_abstract():
    assert not inspect.isabstract(Sistema_desplegable)


def test_sistema_desplegable_constructor_exists():
    assert callable(Sistema_desplegable.__init__)


def test_sistema_desplegable_constructor_args():
    sig = inspect.signature(Sistema_desplegable.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"

def test_sistema_desplegable_has_codigo():
    assert hasattr(Sistema_desplegable, "codigo")
    descriptor = None
    for klass in Sistema_desplegable.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)



def test_sistema_electrico_is_not_abstract():
    assert not inspect.isabstract(Sistema_Electrico)


def test_sistema_electrico_constructor_exists():
    assert callable(Sistema_Electrico.__init__)


def test_sistema_electrico_constructor_args():
    sig = inspect.signature(Sistema_Electrico.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"

def test_sistema_electrico_has_codigo():
    assert hasattr(Sistema_Electrico, "codigo")
    descriptor = None
    for klass in Sistema_Electrico.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)



def test_planosterreno_is_not_abstract():
    assert not inspect.isabstract(PlanosTerreno)


def test_planosterreno_constructor_exists():
    assert callable(PlanosTerreno.__init__)


def test_planosterreno_constructor_args():
    sig = inspect.signature(PlanosTerreno.__init__)
    params = list(sig.parameters.keys())
    assert "Ublicacion" in params, "Missing parameter 'Ublicacion'"

def test_planosterreno_has_Ublicacion():
    assert hasattr(PlanosTerreno, "Ublicacion")
    descriptor = None
    for klass in PlanosTerreno.__mro__:
        if "Ublicacion" in klass.__dict__:
            descriptor = klass.__dict__["Ublicacion"]
            break
    assert isinstance(descriptor, property)



def test_ejecuci_n_is_not_abstract():
    assert not inspect.isabstract(Ejecuci_n)


def test_ejecuci_n_constructor_exists():
    assert callable(Ejecuci_n.__init__)


def test_ejecuci_n_constructor_args():
    sig = inspect.signature(Ejecuci_n.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"

def test_ejecuci_n_has_codigo():
    assert hasattr(Ejecuci_n, "codigo")
    descriptor = None
    for klass in Ejecuci_n.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)



def test_encargos_is_not_abstract():
    assert not inspect.isabstract(Encargos)


def test_encargos_constructor_exists():
    assert callable(Encargos.__init__)


def test_encargos_constructor_args():
    sig = inspect.signature(Encargos.__init__)
    params = list(sig.parameters.keys())
    assert "detalles" in params, "Missing parameter 'detalles'"
    assert "codigo" in params, "Missing parameter 'codigo'"

def test_encargos_has_detalles():
    assert hasattr(Encargos, "detalles")
    descriptor = None
    for klass in Encargos.__mro__:
        if "detalles" in klass.__dict__:
            descriptor = klass.__dict__["detalles"]
            break
    assert isinstance(descriptor, property)

def test_encargos_has_codigo():
    assert hasattr(Encargos, "codigo")
    descriptor = None
    for klass in Encargos.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)



def test_facturas_pagos__is_not_abstract():
    assert not inspect.isabstract(facturas_pagos_)


def test_facturas_pagos__constructor_exists():
    assert callable(facturas_pagos_.__init__)


def test_facturas_pagos__constructor_args():
    sig = inspect.signature(facturas_pagos_.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"
    assert "total" in params, "Missing parameter 'total'"
    assert "pagoNomina" in params, "Missing parameter 'pagoNomina'"

def test_facturas_pagos__has_codigo():
    assert hasattr(facturas_pagos_, "codigo")
    descriptor = None
    for klass in facturas_pagos_.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)

def test_facturas_pagos__has_total():
    assert hasattr(facturas_pagos_, "total")
    descriptor = None
    for klass in facturas_pagos_.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_facturas_pagos__has_pagoNomina():
    assert hasattr(facturas_pagos_, "pagoNomina")
    descriptor = None
    for klass in facturas_pagos_.__mro__:
        if "pagoNomina" in klass.__dict__:
            descriptor = klass.__dict__["pagoNomina"]
            break
    assert isinstance(descriptor, property)



def test_comprador_is_not_abstract():
    assert not inspect.isabstract(Comprador)


def test_comprador_constructor_exists():
    assert callable(Comprador.__init__)


def test_comprador_constructor_args():
    sig = inspect.signature(Comprador.__init__)
    params = list(sig.parameters.keys())
    assert "telefono" in params, "Missing parameter 'telefono'"
    assert "identificacion" in params, "Missing parameter 'identificacion'"
    assert "Nombre" in params, "Missing parameter 'Nombre'"

def test_comprador_has_telefono():
    assert hasattr(Comprador, "telefono")
    descriptor = None
    for klass in Comprador.__mro__:
        if "telefono" in klass.__dict__:
            descriptor = klass.__dict__["telefono"]
            break
    assert isinstance(descriptor, property)

def test_comprador_has_identificacion():
    assert hasattr(Comprador, "identificacion")
    descriptor = None
    for klass in Comprador.__mro__:
        if "identificacion" in klass.__dict__:
            descriptor = klass.__dict__["identificacion"]
            break
    assert isinstance(descriptor, property)

def test_comprador_has_Nombre():
    assert hasattr(Comprador, "Nombre")
    descriptor = None
    for klass in Comprador.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)



def test_historial_trabajadores_is_not_abstract():
    assert not inspect.isabstract(Historial_trabajadores)


def test_historial_trabajadores_constructor_exists():
    assert callable(Historial_trabajadores.__init__)


def test_historial_trabajadores_constructor_args():
    sig = inspect.signature(Historial_trabajadores.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"
    assert "horasTrabajadas" in params, "Missing parameter 'horasTrabajadas'"
    assert "TrabajoAntiguo" in params, "Missing parameter 'TrabajoAntiguo'"

def test_historial_trabajadores_has_codigo():
    assert hasattr(Historial_trabajadores, "codigo")
    descriptor = None
    for klass in Historial_trabajadores.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)

def test_historial_trabajadores_has_horasTrabajadas():
    assert hasattr(Historial_trabajadores, "horasTrabajadas")
    descriptor = None
    for klass in Historial_trabajadores.__mro__:
        if "horasTrabajadas" in klass.__dict__:
            descriptor = klass.__dict__["horasTrabajadas"]
            break
    assert isinstance(descriptor, property)

def test_historial_trabajadores_has_TrabajoAntiguo():
    assert hasattr(Historial_trabajadores, "TrabajoAntiguo")
    descriptor = None
    for klass in Historial_trabajadores.__mro__:
        if "TrabajoAntiguo" in klass.__dict__:
            descriptor = klass.__dict__["TrabajoAntiguo"]
            break
    assert isinstance(descriptor, property)



def test_trabajadores_is_not_abstract():
    assert not inspect.isabstract(Trabajadores)


def test_trabajadores_constructor_exists():
    assert callable(Trabajadores.__init__)


def test_trabajadores_constructor_args():
    sig = inspect.signature(Trabajadores.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "identificacion" in params, "Missing parameter 'identificacion'"
    assert "Telefono" in params, "Missing parameter 'Telefono'"

def test_trabajadores_has_nombre():
    assert hasattr(Trabajadores, "nombre")
    descriptor = None
    for klass in Trabajadores.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_trabajadores_has_identificacion():
    assert hasattr(Trabajadores, "identificacion")
    descriptor = None
    for klass in Trabajadores.__mro__:
        if "identificacion" in klass.__dict__:
            descriptor = klass.__dict__["identificacion"]
            break
    assert isinstance(descriptor, property)

def test_trabajadores_has_Telefono():
    assert hasattr(Trabajadores, "Telefono")
    descriptor = None
    for klass in Trabajadores.__mro__:
        if "Telefono" in klass.__dict__:
            descriptor = klass.__dict__["Telefono"]
            break
    assert isinstance(descriptor, property)



def test_permisos_is_not_abstract():
    assert not inspect.isabstract(Permisos)


def test_permisos_constructor_exists():
    assert callable(Permisos.__init__)


def test_permisos_constructor_args():
    sig = inspect.signature(Permisos.__init__)
    params = list(sig.parameters.keys())
    assert "Fecha" in params, "Missing parameter 'Fecha'"
    assert "Estado" in params, "Missing parameter 'Estado'"
    assert "Codigo" in params, "Missing parameter 'Codigo'"

def test_permisos_has_Fecha():
    assert hasattr(Permisos, "Fecha")
    descriptor = None
    for klass in Permisos.__mro__:
        if "Fecha" in klass.__dict__:
            descriptor = klass.__dict__["Fecha"]
            break
    assert isinstance(descriptor, property)

def test_permisos_has_Estado():
    assert hasattr(Permisos, "Estado")
    descriptor = None
    for klass in Permisos.__mro__:
        if "Estado" in klass.__dict__:
            descriptor = klass.__dict__["Estado"]
            break
    assert isinstance(descriptor, property)

def test_permisos_has_Codigo():
    assert hasattr(Permisos, "Codigo")
    descriptor = None
    for klass in Permisos.__mro__:
        if "Codigo" in klass.__dict__:
            descriptor = klass.__dict__["Codigo"]
            break
    assert isinstance(descriptor, property)



def test_planos_is_not_abstract():
    assert not inspect.isabstract(Planos)


def test_planos_constructor_exists():
    assert callable(Planos.__init__)


def test_planos_constructor_args():
    sig = inspect.signature(Planos.__init__)
    params = list(sig.parameters.keys())
    assert "Codigo" in params, "Missing parameter 'Codigo'"
    assert "Fecha" in params, "Missing parameter 'Fecha'"
    assert "Escala" in params, "Missing parameter 'Escala'"

def test_planos_has_Codigo():
    assert hasattr(Planos, "Codigo")
    descriptor = None
    for klass in Planos.__mro__:
        if "Codigo" in klass.__dict__:
            descriptor = klass.__dict__["Codigo"]
            break
    assert isinstance(descriptor, property)

def test_planos_has_Fecha():
    assert hasattr(Planos, "Fecha")
    descriptor = None
    for klass in Planos.__mro__:
        if "Fecha" in klass.__dict__:
            descriptor = klass.__dict__["Fecha"]
            break
    assert isinstance(descriptor, property)

def test_planos_has_Escala():
    assert hasattr(Planos, "Escala")
    descriptor = None
    for klass in Planos.__mro__:
        if "Escala" in klass.__dict__:
            descriptor = klass.__dict__["Escala"]
            break
    assert isinstance(descriptor, property)



def test_obras_is_not_abstract():
    assert not inspect.isabstract(Obras)


def test_obras_constructor_exists():
    assert callable(Obras.__init__)


def test_obras_constructor_args():
    sig = inspect.signature(Obras.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"
    assert "direccion" in params, "Missing parameter 'direccion'"

def test_obras_has_codigo():
    assert hasattr(Obras, "codigo")
    descriptor = None
    for klass in Obras.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)

def test_obras_has_direccion():
    assert hasattr(Obras, "direccion")
    descriptor = None
    for klass in Obras.__mro__:
        if "direccion" in klass.__dict__:
            descriptor = klass.__dict__["direccion"]
            break
    assert isinstance(descriptor, property)



def test_pedidos_is_not_abstract():
    assert not inspect.isabstract(Pedidos)


def test_pedidos_constructor_exists():
    assert callable(Pedidos.__init__)


def test_pedidos_constructor_args():
    sig = inspect.signature(Pedidos.__init__)
    params = list(sig.parameters.keys())
    assert "fecha" in params, "Missing parameter 'fecha'"
    assert "codigo" in params, "Missing parameter 'codigo'"

def test_pedidos_has_fecha():
    assert hasattr(Pedidos, "fecha")
    descriptor = None
    for klass in Pedidos.__mro__:
        if "fecha" in klass.__dict__:
            descriptor = klass.__dict__["fecha"]
            break
    assert isinstance(descriptor, property)

def test_pedidos_has_codigo():
    assert hasattr(Pedidos, "codigo")
    descriptor = None
    for klass in Pedidos.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)



def test_solucitudsuministro_is_not_abstract():
    assert not inspect.isabstract(SolucitudSuministro)


def test_solucitudsuministro_constructor_exists():
    assert callable(SolucitudSuministro.__init__)


def test_solucitudsuministro_constructor_args():
    sig = inspect.signature(SolucitudSuministro.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"
    assert "fecha" in params, "Missing parameter 'fecha'"

def test_solucitudsuministro_has_codigo():
    assert hasattr(SolucitudSuministro, "codigo")
    descriptor = None
    for klass in SolucitudSuministro.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)

def test_solucitudsuministro_has_fecha():
    assert hasattr(SolucitudSuministro, "fecha")
    descriptor = None
    for klass in SolucitudSuministro.__mro__:
        if "fecha" in klass.__dict__:
            descriptor = klass.__dict__["fecha"]
            break
    assert isinstance(descriptor, property)



def test_factura_is_not_abstract():
    assert not inspect.isabstract(Factura)


def test_factura_constructor_exists():
    assert callable(Factura.__init__)


def test_factura_constructor_args():
    sig = inspect.signature(Factura.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"
    assert "fecha" in params, "Missing parameter 'fecha'"

def test_factura_has_codigo():
    assert hasattr(Factura, "codigo")
    descriptor = None
    for klass in Factura.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)

def test_factura_has_fecha():
    assert hasattr(Factura, "fecha")
    descriptor = None
    for klass in Factura.__mro__:
        if "fecha" in klass.__dict__:
            descriptor = klass.__dict__["fecha"]
            break
    assert isinstance(descriptor, property)



def test_dependencia_is_not_abstract():
    assert not inspect.isabstract(Dependencia)


def test_dependencia_constructor_exists():
    assert callable(Dependencia.__init__)


def test_dependencia_constructor_args():
    sig = inspect.signature(Dependencia.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"
    assert "responsable" in params, "Missing parameter 'responsable'"
    assert "codigo" in params, "Missing parameter 'codigo'"

def test_dependencia_has_nombre():
    assert hasattr(Dependencia, "nombre")
    descriptor = None
    for klass in Dependencia.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)

def test_dependencia_has_responsable():
    assert hasattr(Dependencia, "responsable")
    descriptor = None
    for klass in Dependencia.__mro__:
        if "responsable" in klass.__dict__:
            descriptor = klass.__dict__["responsable"]
            break
    assert isinstance(descriptor, property)

def test_dependencia_has_codigo():
    assert hasattr(Dependencia, "codigo")
    descriptor = None
    for klass in Dependencia.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)



def test_proveedores_is_not_abstract():
    assert not inspect.isabstract(Proveedores)


def test_proveedores_constructor_exists():
    assert callable(Proveedores.__init__)


def test_proveedores_constructor_args():
    sig = inspect.signature(Proveedores.__init__)
    params = list(sig.parameters.keys())
    assert "telefonos" in params, "Missing parameter 'telefonos'"
    assert "nit" in params, "Missing parameter 'nit'"
    assert "direccion" in params, "Missing parameter 'direccion'"
    assert "razonSocial" in params, "Missing parameter 'razonSocial'"

def test_proveedores_has_telefonos():
    assert hasattr(Proveedores, "telefonos")
    descriptor = None
    for klass in Proveedores.__mro__:
        if "telefonos" in klass.__dict__:
            descriptor = klass.__dict__["telefonos"]
            break
    assert isinstance(descriptor, property)

def test_proveedores_has_nit():
    assert hasattr(Proveedores, "nit")
    descriptor = None
    for klass in Proveedores.__mro__:
        if "nit" in klass.__dict__:
            descriptor = klass.__dict__["nit"]
            break
    assert isinstance(descriptor, property)

def test_proveedores_has_direccion():
    assert hasattr(Proveedores, "direccion")
    descriptor = None
    for klass in Proveedores.__mro__:
        if "direccion" in klass.__dict__:
            descriptor = klass.__dict__["direccion"]
            break
    assert isinstance(descriptor, property)

def test_proveedores_has_razonSocial():
    assert hasattr(Proveedores, "razonSocial")
    descriptor = None
    for klass in Proveedores.__mro__:
        if "razonSocial" in klass.__dict__:
            descriptor = klass.__dict__["razonSocial"]
            break
    assert isinstance(descriptor, property)



def test_elementos_is_not_abstract():
    assert not inspect.isabstract(Elementos)


def test_elementos_constructor_exists():
    assert callable(Elementos.__init__)


def test_elementos_constructor_args():
    sig = inspect.signature(Elementos.__init__)
    params = list(sig.parameters.keys())
    assert "referencia" in params, "Missing parameter 'referencia'"
    assert "clasificacion" in params, "Missing parameter 'clasificacion'"

def test_elementos_has_referencia():
    assert hasattr(Elementos, "referencia")
    descriptor = None
    for klass in Elementos.__mro__:
        if "referencia" in klass.__dict__:
            descriptor = klass.__dict__["referencia"]
            break
    assert isinstance(descriptor, property)

def test_elementos_has_clasificacion():
    assert hasattr(Elementos, "clasificacion")
    descriptor = None
    for klass in Elementos.__mro__:
        if "clasificacion" in klass.__dict__:
            descriptor = klass.__dict__["clasificacion"]
            break
    assert isinstance(descriptor, property)



def test_ordenespedido_is_not_abstract():
    assert not inspect.isabstract(OrdenesPedido)


def test_ordenespedido_constructor_exists():
    assert callable(OrdenesPedido.__init__)


def test_ordenespedido_constructor_args():
    sig = inspect.signature(OrdenesPedido.__init__)
    params = list(sig.parameters.keys())
    assert "fecha" in params, "Missing parameter 'fecha'"
    assert "codigo" in params, "Missing parameter 'codigo'"

def test_ordenespedido_has_fecha():
    assert hasattr(OrdenesPedido, "fecha")
    descriptor = None
    for klass in OrdenesPedido.__mro__:
        if "fecha" in klass.__dict__:
            descriptor = klass.__dict__["fecha"]
            break
    assert isinstance(descriptor, property)

def test_ordenespedido_has_codigo():
    assert hasattr(OrdenesPedido, "codigo")
    descriptor = None
    for klass in OrdenesPedido.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)



def test_sistema_web_movil___recceci_n_de_pedidos_component_is_not_abstract():
    assert not inspect.isabstract(Sistema_WEB_Movil___Recceci_n_de_pedidos_Component)


def test_sistema_web_movil___recceci_n_de_pedidos_component_constructor_exists():
    assert callable(Sistema_WEB_Movil___Recceci_n_de_pedidos_Component.__init__)


def test_sistema_web_movil___recceci_n_de_pedidos_component_constructor_args():
    sig = inspect.signature(Sistema_WEB_Movil___Recceci_n_de_pedidos_Component.__init__)
    params = list(sig.parameters.keys())



def test_actor_actor_is_not_abstract():
    assert not inspect.isabstract(Actor_Actor)


def test_actor_actor_constructor_exists():
    assert callable(Actor_Actor.__init__)


def test_actor_actor_constructor_args():
    sig = inspect.signature(Actor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_dependencia_actor_is_not_abstract():
    assert not inspect.isabstract(Dependencia_Actor)


def test_dependencia_actor_constructor_exists():
    assert callable(Dependencia_Actor.__init__)


def test_dependencia_actor_constructor_args():
    sig = inspect.signature(Dependencia_Actor.__init__)
    params = list(sig.parameters.keys())



def test_proveedores_actor_is_not_abstract():
    assert not inspect.isabstract(Proveedores_Actor)


def test_proveedores_actor_constructor_exists():
    assert callable(Proveedores_Actor.__init__)


def test_proveedores_actor_constructor_args():
    sig = inspect.signature(Proveedores_Actor.__init__)
    params = list(sig.parameters.keys())



def test_departamento_de_inventarios_y_suministros___dis_component_is_not_abstract():
    assert not inspect.isabstract(Departamento_de_Inventarios_y_Suministros___Dis_Component)


def test_departamento_de_inventarios_y_suministros___dis_component_constructor_exists():
    assert callable(Departamento_de_Inventarios_y_Suministros___Dis_Component.__init__)


def test_departamento_de_inventarios_y_suministros___dis_component_constructor_args():
    sig = inspect.signature(Departamento_de_Inventarios_y_Suministros___Dis_Component.__init__)
    params = list(sig.parameters.keys())



def test_juridica_actor_is_not_abstract():
    assert not inspect.isabstract(Juridica_Actor)


def test_juridica_actor_constructor_exists():
    assert callable(Juridica_Actor.__init__)


def test_juridica_actor_constructor_args():
    sig = inspect.signature(Juridica_Actor.__init__)
    params = list(sig.parameters.keys())



def test_natural_actor_is_not_abstract():
    assert not inspect.isabstract(Natural_Actor)


def test_natural_actor_constructor_exists():
    assert callable(Natural_Actor.__init__)


def test_natural_actor_constructor_args():
    sig = inspect.signature(Natural_Actor.__init__)
    params = list(sig.parameters.keys())



def test_departamento_de_contabilidad_y_tesoreria_actor_is_not_abstract():
    assert not inspect.isabstract(Departamento_de_contabilidad_y_tesoreria_Actor)


def test_departamento_de_contabilidad_y_tesoreria_actor_constructor_exists():
    assert callable(Departamento_de_contabilidad_y_tesoreria_Actor.__init__)


def test_departamento_de_contabilidad_y_tesoreria_actor_constructor_args():
    sig = inspect.signature(Departamento_de_contabilidad_y_tesoreria_Actor.__init__)
    params = list(sig.parameters.keys())



def test_mileninum_component_is_not_abstract():
    assert not inspect.isabstract(Mileninum_Component)


def test_mileninum_component_constructor_exists():
    assert callable(Mileninum_Component.__init__)


def test_mileninum_component_constructor_args():
    sig = inspect.signature(Mileninum_Component.__init__)
    params = list(sig.parameters.keys())



def test_brinda_consultoria_external_is_not_abstract():
    assert not inspect.isabstract(Brinda_consultoria_external)


def test_brinda_consultoria_external_constructor_exists():
    assert callable(Brinda_consultoria_external.__init__)


def test_brinda_consultoria_external_constructor_args():
    sig = inspect.signature(Brinda_consultoria_external.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Clasificar_Producto_external_strategy = st.builds(
    Clasificar_Producto_external,
)
Generar_ordenes_de_pedidos_external_strategy = st.builds(
    Generar_ordenes_de_pedidos_external,
)
Recibir_ordenes_de_suministro_external_strategy = st.builds(
    Recibir_ordenes_de_suministro_external,
)
Recibir_productos_y_pedidos_external_strategy = st.builds(
    Recibir_productos_y_pedidos_external,
)
Registrar_proveedores_external_strategy = st.builds(
    Registrar_proveedores_external,
)
Servidor_intel_i8_Node_strategy = st.builds(
    Servidor_intel_i8_Node,
)
_reasConocimiento_strategy = st.builds(
    _reasConocimiento,
)
Departamento_strategy = st.builds(
    Departamento,
)
Profesores_strategy = st.builds(
    Profesores,
)
Sistema_desplegable_strategy = st.builds(
    Sistema_desplegable,
    codigo=
        safe_text
)
Sistema_Electrico_strategy = st.builds(
    Sistema_Electrico,
    codigo=
        safe_text
)
PlanosTerreno_strategy = st.builds(
    PlanosTerreno,
    Ublicacion=
        safe_text
)
Ejecuci_n_strategy = st.builds(
    Ejecuci_n,
    codigo=
        safe_text
)
Encargos_strategy = st.builds(
    Encargos,
    detalles=
        safe_text,
    codigo=
        safe_text
)
facturas_pagos__strategy = st.builds(
    facturas_pagos_,
    codigo=
        safe_text,
    total=
        safe_text,
    pagoNomina=
        st.integers()
)
Comprador_strategy = st.builds(
    Comprador,
    telefono=
        safe_text,
    identificacion=
        safe_text,
    Nombre=
        safe_text
)
Historial_trabajadores_strategy = st.builds(
    Historial_trabajadores,
    codigo=
        safe_text,
    horasTrabajadas=
        safe_text,
    TrabajoAntiguo=
        safe_text
)
Trabajadores_strategy = st.builds(
    Trabajadores,
    nombre=
        safe_text,
    identificacion=
        safe_text,
    Telefono=
        st.integers()
)
Permisos_strategy = st.builds(
    Permisos,
    Fecha=
        safe_text,
    Estado=
        safe_text,
    Codigo=
        safe_text
)
Planos_strategy = st.builds(
    Planos,
    Codigo=
        safe_text,
    Fecha=
        safe_text,
    Escala=
        safe_text
)
Obras_strategy = st.builds(
    Obras,
    codigo=
        safe_text,
    direccion=
        safe_text
)
Pedidos_strategy = st.builds(
    Pedidos,
    fecha=
        safe_text,
    codigo=
        safe_text
)
SolucitudSuministro_strategy = st.builds(
    SolucitudSuministro,
    codigo=
        safe_text,
    fecha=
        safe_text
)
Factura_strategy = st.builds(
    Factura,
    codigo=
        safe_text,
    fecha=
        safe_text
)
Dependencia_strategy = st.builds(
    Dependencia,
    nombre=
        safe_text,
    responsable=
        safe_text,
    codigo=
        safe_text
)
Proveedores_strategy = st.builds(
    Proveedores,
    telefonos=
        st.integers(),
    nit=
        safe_text,
    direccion=
        safe_text,
    razonSocial=
        safe_text
)
Elementos_strategy = st.builds(
    Elementos,
    referencia=
        safe_text,
    clasificacion=
        safe_text
)
OrdenesPedido_strategy = st.builds(
    OrdenesPedido,
    fecha=
        safe_text,
    codigo=
        safe_text
)
Sistema_WEB_Movil___Recceci_n_de_pedidos_Component_strategy = st.builds(
    Sistema_WEB_Movil___Recceci_n_de_pedidos_Component,
)
Actor_Actor_strategy = st.builds(
    Actor_Actor,
)
Dependencia_Actor_strategy = st.builds(
    Dependencia_Actor,
)
Proveedores_Actor_strategy = st.builds(
    Proveedores_Actor,
)
Departamento_de_Inventarios_y_Suministros___Dis_Component_strategy = st.builds(
    Departamento_de_Inventarios_y_Suministros___Dis_Component,
)
Juridica_Actor_strategy = st.builds(
    Juridica_Actor,
)
Natural_Actor_strategy = st.builds(
    Natural_Actor,
)
Departamento_de_contabilidad_y_tesoreria_Actor_strategy = st.builds(
    Departamento_de_contabilidad_y_tesoreria_Actor,
)
Mileninum_Component_strategy = st.builds(
    Mileninum_Component,
)
Brinda_consultoria_external_strategy = st.builds(
    Brinda_consultoria_external,
)

@given(instance=Clasificar_Producto_external_strategy)
@settings(max_examples=50)
def test_clasificar_producto_external_instantiation(instance):
    assert isinstance(instance, Clasificar_Producto_external)

@given(instance=Generar_ordenes_de_pedidos_external_strategy)
@settings(max_examples=50)
def test_generar_ordenes_de_pedidos_external_instantiation(instance):
    assert isinstance(instance, Generar_ordenes_de_pedidos_external)

@given(instance=Recibir_ordenes_de_suministro_external_strategy)
@settings(max_examples=50)
def test_recibir_ordenes_de_suministro_external_instantiation(instance):
    assert isinstance(instance, Recibir_ordenes_de_suministro_external)

@given(instance=Recibir_productos_y_pedidos_external_strategy)
@settings(max_examples=50)
def test_recibir_productos_y_pedidos_external_instantiation(instance):
    assert isinstance(instance, Recibir_productos_y_pedidos_external)

@given(instance=Registrar_proveedores_external_strategy)
@settings(max_examples=50)
def test_registrar_proveedores_external_instantiation(instance):
    assert isinstance(instance, Registrar_proveedores_external)

@given(instance=Servidor_intel_i8_Node_strategy)
@settings(max_examples=50)
def test_servidor_intel_i8_node_instantiation(instance):
    assert isinstance(instance, Servidor_intel_i8_Node)

@given(instance=_reasConocimiento_strategy)
@settings(max_examples=50)
def test__reasconocimiento_instantiation(instance):
    assert isinstance(instance, _reasConocimiento)

@given(instance=Departamento_strategy)
@settings(max_examples=50)
def test_departamento_instantiation(instance):
    assert isinstance(instance, Departamento)

@given(instance=Profesores_strategy)
@settings(max_examples=50)
def test_profesores_instantiation(instance):
    assert isinstance(instance, Profesores)

@given(instance=Sistema_desplegable_strategy)
@settings(max_examples=50)
def test_sistema_desplegable_instantiation(instance):
    assert isinstance(instance, Sistema_desplegable)



@given(instance=Sistema_desplegable_strategy)
def test_sistema_desplegable_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original

@given(instance=Sistema_Electrico_strategy)
@settings(max_examples=50)
def test_sistema_electrico_instantiation(instance):
    assert isinstance(instance, Sistema_Electrico)



@given(instance=Sistema_Electrico_strategy)
def test_sistema_electrico_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original

@given(instance=PlanosTerreno_strategy)
@settings(max_examples=50)
def test_planosterreno_instantiation(instance):
    assert isinstance(instance, PlanosTerreno)



@given(instance=PlanosTerreno_strategy)
def test_planosterreno_Ublicacion_setter(instance):
    original = instance.Ublicacion
    instance.Ublicacion = original
    assert instance.Ublicacion == original

@given(instance=Ejecuci_n_strategy)
@settings(max_examples=50)
def test_ejecuci_n_instantiation(instance):
    assert isinstance(instance, Ejecuci_n)



@given(instance=Ejecuci_n_strategy)
def test_ejecuci_n_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original

@given(instance=Encargos_strategy)
@settings(max_examples=50)
def test_encargos_instantiation(instance):
    assert isinstance(instance, Encargos)



@given(instance=Encargos_strategy)
def test_encargos_detalles_setter(instance):
    original = instance.detalles
    instance.detalles = original
    assert instance.detalles == original



@given(instance=Encargos_strategy)
def test_encargos_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original

@given(instance=facturas_pagos__strategy)
@settings(max_examples=50)
def test_facturas_pagos__instantiation(instance):
    assert isinstance(instance, facturas_pagos_)



@given(instance=facturas_pagos__strategy)
def test_facturas_pagos__codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original



@given(instance=facturas_pagos__strategy)
def test_facturas_pagos__total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=facturas_pagos__strategy)
def test_facturas_pagos__pagoNomina_setter(instance):
    original = instance.pagoNomina
    instance.pagoNomina = original
    assert instance.pagoNomina == original

@given(instance=Comprador_strategy)
@settings(max_examples=50)
def test_comprador_instantiation(instance):
    assert isinstance(instance, Comprador)



@given(instance=Comprador_strategy)
def test_comprador_telefono_setter(instance):
    original = instance.telefono
    instance.telefono = original
    assert instance.telefono == original



@given(instance=Comprador_strategy)
def test_comprador_identificacion_setter(instance):
    original = instance.identificacion
    instance.identificacion = original
    assert instance.identificacion == original



@given(instance=Comprador_strategy)
def test_comprador_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original

@given(instance=Historial_trabajadores_strategy)
@settings(max_examples=50)
def test_historial_trabajadores_instantiation(instance):
    assert isinstance(instance, Historial_trabajadores)



@given(instance=Historial_trabajadores_strategy)
def test_historial_trabajadores_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original



@given(instance=Historial_trabajadores_strategy)
def test_historial_trabajadores_horasTrabajadas_setter(instance):
    original = instance.horasTrabajadas
    instance.horasTrabajadas = original
    assert instance.horasTrabajadas == original



@given(instance=Historial_trabajadores_strategy)
def test_historial_trabajadores_TrabajoAntiguo_setter(instance):
    original = instance.TrabajoAntiguo
    instance.TrabajoAntiguo = original
    assert instance.TrabajoAntiguo == original

@given(instance=Trabajadores_strategy)
@settings(max_examples=50)
def test_trabajadores_instantiation(instance):
    assert isinstance(instance, Trabajadores)



@given(instance=Trabajadores_strategy)
def test_trabajadores_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Trabajadores_strategy)
def test_trabajadores_identificacion_setter(instance):
    original = instance.identificacion
    instance.identificacion = original
    assert instance.identificacion == original



@given(instance=Trabajadores_strategy)
def test_trabajadores_Telefono_setter(instance):
    original = instance.Telefono
    instance.Telefono = original
    assert instance.Telefono == original

@given(instance=Permisos_strategy)
@settings(max_examples=50)
def test_permisos_instantiation(instance):
    assert isinstance(instance, Permisos)



@given(instance=Permisos_strategy)
def test_permisos_Fecha_setter(instance):
    original = instance.Fecha
    instance.Fecha = original
    assert instance.Fecha == original



@given(instance=Permisos_strategy)
def test_permisos_Estado_setter(instance):
    original = instance.Estado
    instance.Estado = original
    assert instance.Estado == original



@given(instance=Permisos_strategy)
def test_permisos_Codigo_setter(instance):
    original = instance.Codigo
    instance.Codigo = original
    assert instance.Codigo == original

@given(instance=Planos_strategy)
@settings(max_examples=50)
def test_planos_instantiation(instance):
    assert isinstance(instance, Planos)



@given(instance=Planos_strategy)
def test_planos_Codigo_setter(instance):
    original = instance.Codigo
    instance.Codigo = original
    assert instance.Codigo == original



@given(instance=Planos_strategy)
def test_planos_Fecha_setter(instance):
    original = instance.Fecha
    instance.Fecha = original
    assert instance.Fecha == original



@given(instance=Planos_strategy)
def test_planos_Escala_setter(instance):
    original = instance.Escala
    instance.Escala = original
    assert instance.Escala == original

@given(instance=Obras_strategy)
@settings(max_examples=50)
def test_obras_instantiation(instance):
    assert isinstance(instance, Obras)



@given(instance=Obras_strategy)
def test_obras_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original



@given(instance=Obras_strategy)
def test_obras_direccion_setter(instance):
    original = instance.direccion
    instance.direccion = original
    assert instance.direccion == original

@given(instance=Pedidos_strategy)
@settings(max_examples=50)
def test_pedidos_instantiation(instance):
    assert isinstance(instance, Pedidos)



@given(instance=Pedidos_strategy)
def test_pedidos_fecha_setter(instance):
    original = instance.fecha
    instance.fecha = original
    assert instance.fecha == original



@given(instance=Pedidos_strategy)
def test_pedidos_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original

@given(instance=SolucitudSuministro_strategy)
@settings(max_examples=50)
def test_solucitudsuministro_instantiation(instance):
    assert isinstance(instance, SolucitudSuministro)



@given(instance=SolucitudSuministro_strategy)
def test_solucitudsuministro_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original



@given(instance=SolucitudSuministro_strategy)
def test_solucitudsuministro_fecha_setter(instance):
    original = instance.fecha
    instance.fecha = original
    assert instance.fecha == original

@given(instance=Factura_strategy)
@settings(max_examples=50)
def test_factura_instantiation(instance):
    assert isinstance(instance, Factura)



@given(instance=Factura_strategy)
def test_factura_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original



@given(instance=Factura_strategy)
def test_factura_fecha_setter(instance):
    original = instance.fecha
    instance.fecha = original
    assert instance.fecha == original

@given(instance=Dependencia_strategy)
@settings(max_examples=50)
def test_dependencia_instantiation(instance):
    assert isinstance(instance, Dependencia)



@given(instance=Dependencia_strategy)
def test_dependencia_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original



@given(instance=Dependencia_strategy)
def test_dependencia_responsable_setter(instance):
    original = instance.responsable
    instance.responsable = original
    assert instance.responsable == original



@given(instance=Dependencia_strategy)
def test_dependencia_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original

@given(instance=Proveedores_strategy)
@settings(max_examples=50)
def test_proveedores_instantiation(instance):
    assert isinstance(instance, Proveedores)



@given(instance=Proveedores_strategy)
def test_proveedores_telefonos_setter(instance):
    original = instance.telefonos
    instance.telefonos = original
    assert instance.telefonos == original



@given(instance=Proveedores_strategy)
def test_proveedores_nit_setter(instance):
    original = instance.nit
    instance.nit = original
    assert instance.nit == original



@given(instance=Proveedores_strategy)
def test_proveedores_direccion_setter(instance):
    original = instance.direccion
    instance.direccion = original
    assert instance.direccion == original



@given(instance=Proveedores_strategy)
def test_proveedores_razonSocial_setter(instance):
    original = instance.razonSocial
    instance.razonSocial = original
    assert instance.razonSocial == original

@given(instance=Elementos_strategy)
@settings(max_examples=50)
def test_elementos_instantiation(instance):
    assert isinstance(instance, Elementos)



@given(instance=Elementos_strategy)
def test_elementos_referencia_setter(instance):
    original = instance.referencia
    instance.referencia = original
    assert instance.referencia == original



@given(instance=Elementos_strategy)
def test_elementos_clasificacion_setter(instance):
    original = instance.clasificacion
    instance.clasificacion = original
    assert instance.clasificacion == original

@given(instance=OrdenesPedido_strategy)
@settings(max_examples=50)
def test_ordenespedido_instantiation(instance):
    assert isinstance(instance, OrdenesPedido)



@given(instance=OrdenesPedido_strategy)
def test_ordenespedido_fecha_setter(instance):
    original = instance.fecha
    instance.fecha = original
    assert instance.fecha == original



@given(instance=OrdenesPedido_strategy)
def test_ordenespedido_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original

@given(instance=Sistema_WEB_Movil___Recceci_n_de_pedidos_Component_strategy)
@settings(max_examples=50)
def test_sistema_web_movil___recceci_n_de_pedidos_component_instantiation(instance):
    assert isinstance(instance, Sistema_WEB_Movil___Recceci_n_de_pedidos_Component)

@given(instance=Actor_Actor_strategy)
@settings(max_examples=50)
def test_actor_actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)

@given(instance=Dependencia_Actor_strategy)
@settings(max_examples=50)
def test_dependencia_actor_instantiation(instance):
    assert isinstance(instance, Dependencia_Actor)

@given(instance=Proveedores_Actor_strategy)
@settings(max_examples=50)
def test_proveedores_actor_instantiation(instance):
    assert isinstance(instance, Proveedores_Actor)

@given(instance=Departamento_de_Inventarios_y_Suministros___Dis_Component_strategy)
@settings(max_examples=50)
def test_departamento_de_inventarios_y_suministros___dis_component_instantiation(instance):
    assert isinstance(instance, Departamento_de_Inventarios_y_Suministros___Dis_Component)

@given(instance=Juridica_Actor_strategy)
@settings(max_examples=50)
def test_juridica_actor_instantiation(instance):
    assert isinstance(instance, Juridica_Actor)

@given(instance=Natural_Actor_strategy)
@settings(max_examples=50)
def test_natural_actor_instantiation(instance):
    assert isinstance(instance, Natural_Actor)

@given(instance=Departamento_de_contabilidad_y_tesoreria_Actor_strategy)
@settings(max_examples=50)
def test_departamento_de_contabilidad_y_tesoreria_actor_instantiation(instance):
    assert isinstance(instance, Departamento_de_contabilidad_y_tesoreria_Actor)

@given(instance=Mileninum_Component_strategy)
@settings(max_examples=50)
def test_mileninum_component_instantiation(instance):
    assert isinstance(instance, Mileninum_Component)

@given(instance=Brinda_consultoria_external_strategy)
@settings(max_examples=50)
def test_brinda_consultoria_external_instantiation(instance):
    assert isinstance(instance, Brinda_consultoria_external)
