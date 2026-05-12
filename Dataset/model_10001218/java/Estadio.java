





import java.util.List;
import java.util.ArrayList;

public class Estadio  {

    private String Ubicacion1;
    private String Nombre;
    private String Cod_Estadio;
    private String Capacidad;
    private String Ubicacion;
    private String Cod_equipo;
    private String Terreno;





    private List<Partido> partidos;


    public Estadio(
        String Ubicacion1,        String Nombre,        String Cod_Estadio,        String Capacidad,        String Ubicacion,        String Cod_equipo,        String Terreno    ) {
        this.Ubicacion1 = Ubicacion1;
        this.Nombre = Nombre;
        this.Cod_Estadio = Cod_Estadio;
        this.Capacidad = Capacidad;
        this.Ubicacion = Ubicacion;
        this.Cod_equipo = Cod_equipo;
        this.Terreno = Terreno;
        this.partidos = new ArrayList<>();
    }

    public Estadio(
        String Ubicacion1,        String Nombre,        String Cod_Estadio,        String Capacidad,        String Ubicacion,        String Cod_equipo,        String Terreno        ArrayList<Partido> partidos    ) {
        this.Ubicacion1 = Ubicacion1;
        this.Nombre = Nombre;
        this.Cod_Estadio = Cod_Estadio;
        this.Capacidad = Capacidad;
        this.Ubicacion = Ubicacion;
        this.Cod_equipo = Cod_equipo;
        this.Terreno = Terreno;
        this.partidos = partidos;
    }

    public String getUbicacion1() {
        return Ubicacion1;
    }

    public void setUbicacion1(String Ubicacion1) {
        this.Ubicacion1 = Ubicacion1;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getCod_estadio() {
        return Cod_Estadio;
    }

    public void setCod_estadio(String Cod_Estadio) {
        this.Cod_Estadio = Cod_Estadio;
    }
    public String getCapacidad() {
        return Capacidad;
    }

    public void setCapacidad(String Capacidad) {
        this.Capacidad = Capacidad;
    }
    public String getUbicacion() {
        return Ubicacion;
    }

    public void setUbicacion(String Ubicacion) {
        this.Ubicacion = Ubicacion;
    }
    public String getCod_equipo() {
        return Cod_equipo;
    }

    public void setCod_equipo(String Cod_equipo) {
        this.Cod_equipo = Cod_equipo;
    }
    public String getTerreno() {
        return Terreno;
    }

    public void setTerreno(String Terreno) {
        this.Terreno = Terreno;
    }

    public List<Partido> getPartidos() {
        return partidos;
    }

    public void addPartido(Partido partido) {
        this.partidos.add(partido);
    }

}