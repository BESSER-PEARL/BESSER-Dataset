





import java.util.List;
import java.util.ArrayList;

public class Servicios  {

    private None Insumos;
    private int Tiempo;
    private int id_servicio;
    private int Valor;
    private None Profesional;
    private String Nombre_servicio;



    public Servicios(
        None Insumos,        int Tiempo,        int id_servicio,        int Valor,        None Profesional,        String Nombre_servicio    ) {
        this.Insumos = Insumos;
        this.Tiempo = Tiempo;
        this.id_servicio = id_servicio;
        this.Valor = Valor;
        this.Profesional = Profesional;
        this.Nombre_servicio = Nombre_servicio;
    }


    public None getInsumos() {
        return Insumos;
    }

    public void setInsumos(None Insumos) {
        this.Insumos = Insumos;
    }
    public int getTiempo() {
        return Tiempo;
    }

    public void setTiempo(int Tiempo) {
        this.Tiempo = Tiempo;
    }
    public int getId_servicio() {
        return id_servicio;
    }

    public void setId_servicio(int id_servicio) {
        this.id_servicio = id_servicio;
    }
    public int getValor() {
        return Valor;
    }

    public void setValor(int Valor) {
        this.Valor = Valor;
    }
    public None getProfesional() {
        return Profesional;
    }

    public void setProfesional(None Profesional) {
        this.Profesional = Profesional;
    }
    public String getNombre_servicio() {
        return Nombre_servicio;
    }

    public void setNombre_servicio(String Nombre_servicio) {
        this.Nombre_servicio = Nombre_servicio;
    }


}