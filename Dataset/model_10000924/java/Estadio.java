





import java.util.List;
import java.util.ArrayList;

public class Estadio  {

    private String Ubicacion1;
    private String Ubicacion;
    private String Terreno;
    private String Cod_Estadio;
    private String Nombre;
    private String Cod_equipo;
    private String Capacidad;



    public Estadio(
        String Ubicacion1,        String Ubicacion,        String Terreno,        String Cod_Estadio,        String Nombre,        String Cod_equipo,        String Capacidad    ) {
        this.Ubicacion1 = Ubicacion1;
        this.Ubicacion = Ubicacion;
        this.Terreno = Terreno;
        this.Cod_Estadio = Cod_Estadio;
        this.Nombre = Nombre;
        this.Cod_equipo = Cod_equipo;
        this.Capacidad = Capacidad;
    }


    public String getUbicacion1() {
        return Ubicacion1;
    }

    public void setUbicacion1(String Ubicacion1) {
        this.Ubicacion1 = Ubicacion1;
    }
    public String getUbicacion() {
        return Ubicacion;
    }

    public void setUbicacion(String Ubicacion) {
        this.Ubicacion = Ubicacion;
    }
    public String getTerreno() {
        return Terreno;
    }

    public void setTerreno(String Terreno) {
        this.Terreno = Terreno;
    }
    public String getCod_estadio() {
        return Cod_Estadio;
    }

    public void setCod_estadio(String Cod_Estadio) {
        this.Cod_Estadio = Cod_Estadio;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getCod_equipo() {
        return Cod_equipo;
    }

    public void setCod_equipo(String Cod_equipo) {
        this.Cod_equipo = Cod_equipo;
    }
    public String getCapacidad() {
        return Capacidad;
    }

    public void setCapacidad(String Capacidad) {
        this.Capacidad = Capacidad;
    }


}