





import java.util.List;
import java.util.ArrayList;

public class Profesionales  {

    private String Nombre_profesional;
    private int id_profesional;





    private Servicios servicios;


    public Profesionales(
        String Nombre_profesional,        int id_profesional    ) {
        this.Nombre_profesional = Nombre_profesional;
        this.id_profesional = id_profesional;
    }


    public String getNombre_profesional() {
        return Nombre_profesional;
    }

    public void setNombre_profesional(String Nombre_profesional) {
        this.Nombre_profesional = Nombre_profesional;
    }
    public int getId_profesional() {
        return id_profesional;
    }

    public void setId_profesional(int id_profesional) {
        this.id_profesional = id_profesional;
    }

    public Servicios getServicios() {
        return servicios;
    }

    public void setServicios(Servicios servicios) {
        this.servicios = servicios;
    }

}