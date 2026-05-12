





import java.util.List;
import java.util.ArrayList;

public class Estadio  {

    private String Capacidad;
    private String Nombre;
    private String Cod_Estadio;
    private String Terreno;
    private String Ubicacion1;
    private String Cod_equipo;
    private String Ubicacion;





    private List<Partido> partidos;


    public Estadio(
        String Capacidad,        String Nombre,        String Cod_Estadio,        String Terreno,        String Ubicacion1,        String Cod_equipo,        String Ubicacion    ) {
        this.Capacidad = Capacidad;
        this.Nombre = Nombre;
        this.Cod_Estadio = Cod_Estadio;
        this.Terreno = Terreno;
        this.Ubicacion1 = Ubicacion1;
        this.Cod_equipo = Cod_equipo;
        this.Ubicacion = Ubicacion;
        this.partidos = new ArrayList<>();
    }

    public Estadio(
        String Capacidad,        String Nombre,        String Cod_Estadio,        String Terreno,        String Ubicacion1,        String Cod_equipo,        String Ubicacion        ArrayList<Partido> partidos    ) {
        this.Capacidad = Capacidad;
        this.Nombre = Nombre;
        this.Cod_Estadio = Cod_Estadio;
        this.Terreno = Terreno;
        this.Ubicacion1 = Ubicacion1;
        this.Cod_equipo = Cod_equipo;
        this.Ubicacion = Ubicacion;
        this.partidos = partidos;
    }

    public String getCapacidad() {
        return Capacidad;
    }

    public void setCapacidad(String Capacidad) {
        this.Capacidad = Capacidad;
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
    public String getTerreno() {
        return Terreno;
    }

    public void setTerreno(String Terreno) {
        this.Terreno = Terreno;
    }
    public String getUbicacion1() {
        return Ubicacion1;
    }

    public void setUbicacion1(String Ubicacion1) {
        this.Ubicacion1 = Ubicacion1;
    }
    public String getCod_equipo() {
        return Cod_equipo;
    }

    public void setCod_equipo(String Cod_equipo) {
        this.Cod_equipo = Cod_equipo;
    }
    public String getUbicacion() {
        return Ubicacion;
    }

    public void setUbicacion(String Ubicacion) {
        this.Ubicacion = Ubicacion;
    }

    public List<Partido> getPartidos() {
        return partidos;
    }

    public void addPartido(Partido partido) {
        this.partidos.add(partido);
    }

}