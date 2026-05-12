





import java.util.List;
import java.util.ArrayList;

public class Usuario_Actor  {






    private Agregar_Contactos_UseCase agregar_contactos_usecase;




    private Eliminar_Contacto_UseCase eliminar_contacto_usecase;




    private Buscar_Contactos_UseCase buscar_contactos_usecase;




    private Editar_Contacto_UseCase editar_contacto_usecase;




    private Salir_de_la_aplicacion_UseCase salir_de_la_aplicacion_usecase;




    private Ver_detalles_de_contacto_UseCase ver_detalles_de_contacto_usecase;


    public Usuario_Actor(
    ) {
    }



    public Agregar_Contactos_UseCase getAgregar_contactos_usecase() {
        return agregar_contactos_usecase;
    }

    public void setAgregar_contactos_usecase(Agregar_Contactos_UseCase agregar_contactos_usecase) {
        this.agregar_contactos_usecase = agregar_contactos_usecase;
    }
    public Eliminar_Contacto_UseCase getEliminar_contacto_usecase() {
        return eliminar_contacto_usecase;
    }

    public void setEliminar_contacto_usecase(Eliminar_Contacto_UseCase eliminar_contacto_usecase) {
        this.eliminar_contacto_usecase = eliminar_contacto_usecase;
    }
    public Buscar_Contactos_UseCase getBuscar_contactos_usecase() {
        return buscar_contactos_usecase;
    }

    public void setBuscar_contactos_usecase(Buscar_Contactos_UseCase buscar_contactos_usecase) {
        this.buscar_contactos_usecase = buscar_contactos_usecase;
    }
    public Editar_Contacto_UseCase getEditar_contacto_usecase() {
        return editar_contacto_usecase;
    }

    public void setEditar_contacto_usecase(Editar_Contacto_UseCase editar_contacto_usecase) {
        this.editar_contacto_usecase = editar_contacto_usecase;
    }
    public Salir_de_la_aplicacion_UseCase getSalir_de_la_aplicacion_usecase() {
        return salir_de_la_aplicacion_usecase;
    }

    public void setSalir_de_la_aplicacion_usecase(Salir_de_la_aplicacion_UseCase salir_de_la_aplicacion_usecase) {
        this.salir_de_la_aplicacion_usecase = salir_de_la_aplicacion_usecase;
    }
    public Ver_detalles_de_contacto_UseCase getVer_detalles_de_contacto_usecase() {
        return ver_detalles_de_contacto_usecase;
    }

    public void setVer_detalles_de_contacto_usecase(Ver_detalles_de_contacto_UseCase ver_detalles_de_contacto_usecase) {
        this.ver_detalles_de_contacto_usecase = ver_detalles_de_contacto_usecase;
    }

}