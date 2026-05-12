





import java.util.List;
import java.util.ArrayList;

public class Liga  {

    private String Inferior;
    private String Cod_Clasificacion;
    private String Num_equipos;
    private String Superior;
    private String Cod_liga;
    private String Nombre;





    private List<Partido> partidos;


    public Liga(
        String Inferior,        String Cod_Clasificacion,        String Num_equipos,        String Superior,        String Cod_liga,        String Nombre    ) {
        this.Inferior = Inferior;
        this.Cod_Clasificacion = Cod_Clasificacion;
        this.Num_equipos = Num_equipos;
        this.Superior = Superior;
        this.Cod_liga = Cod_liga;
        this.Nombre = Nombre;
        this.partidos = new ArrayList<>();
    }

    public Liga(
        String Inferior,        String Cod_Clasificacion,        String Num_equipos,        String Superior,        String Cod_liga,        String Nombre        ArrayList<Partido> partidos    ) {
        this.Inferior = Inferior;
        this.Cod_Clasificacion = Cod_Clasificacion;
        this.Num_equipos = Num_equipos;
        this.Superior = Superior;
        this.Cod_liga = Cod_liga;
        this.Nombre = Nombre;
        this.partidos = partidos;
    }

    public String getInferior() {
        return Inferior;
    }

    public void setInferior(String Inferior) {
        this.Inferior = Inferior;
    }
    public String getCod_clasificacion() {
        return Cod_Clasificacion;
    }

    public void setCod_clasificacion(String Cod_Clasificacion) {
        this.Cod_Clasificacion = Cod_Clasificacion;
    }
    public String getNum_equipos() {
        return Num_equipos;
    }

    public void setNum_equipos(String Num_equipos) {
        this.Num_equipos = Num_equipos;
    }
    public String getSuperior() {
        return Superior;
    }

    public void setSuperior(String Superior) {
        this.Superior = Superior;
    }
    public String getCod_liga() {
        return Cod_liga;
    }

    public void setCod_liga(String Cod_liga) {
        this.Cod_liga = Cod_liga;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public List<Partido> getPartidos() {
        return partidos;
    }

    public void addPartido(Partido partido) {
        this.partidos.add(partido);
    }

}