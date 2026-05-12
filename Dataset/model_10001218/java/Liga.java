





import java.util.List;
import java.util.ArrayList;

public class Liga  {

    private String Nombre;
    private String Num_equipos;
    private String Inferior;
    private String Superior;
    private String Cod_liga;
    private String Cod_Clasificacion;





    private List<Partido> partidos;


    public Liga(
        String Nombre,        String Num_equipos,        String Inferior,        String Superior,        String Cod_liga,        String Cod_Clasificacion    ) {
        this.Nombre = Nombre;
        this.Num_equipos = Num_equipos;
        this.Inferior = Inferior;
        this.Superior = Superior;
        this.Cod_liga = Cod_liga;
        this.Cod_Clasificacion = Cod_Clasificacion;
        this.partidos = new ArrayList<>();
    }

    public Liga(
        String Nombre,        String Num_equipos,        String Inferior,        String Superior,        String Cod_liga,        String Cod_Clasificacion        ArrayList<Partido> partidos    ) {
        this.Nombre = Nombre;
        this.Num_equipos = Num_equipos;
        this.Inferior = Inferior;
        this.Superior = Superior;
        this.Cod_liga = Cod_liga;
        this.Cod_Clasificacion = Cod_Clasificacion;
        this.partidos = partidos;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getNum_equipos() {
        return Num_equipos;
    }

    public void setNum_equipos(String Num_equipos) {
        this.Num_equipos = Num_equipos;
    }
    public String getInferior() {
        return Inferior;
    }

    public void setInferior(String Inferior) {
        this.Inferior = Inferior;
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
    public String getCod_clasificacion() {
        return Cod_Clasificacion;
    }

    public void setCod_clasificacion(String Cod_Clasificacion) {
        this.Cod_Clasificacion = Cod_Clasificacion;
    }

    public List<Partido> getPartidos() {
        return partidos;
    }

    public void addPartido(Partido partido) {
        this.partidos.add(partido);
    }

}