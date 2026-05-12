





import java.util.List;
import java.util.ArrayList;

public class Clasificacion  {

    private String Cod_Equipo;
    private String Puntos;
    private String JE;
    private String JP;
    private String GF;
    private String JG;
    private String JJ;
    private String DG;
    private String GC;
    private String Posicion;





    private List<Liga> ligas;


    public Clasificacion(
        String Cod_Equipo,        String Puntos,        String JE,        String JP,        String GF,        String JG,        String JJ,        String DG,        String GC,        String Posicion    ) {
        this.Cod_Equipo = Cod_Equipo;
        this.Puntos = Puntos;
        this.JE = JE;
        this.JP = JP;
        this.GF = GF;
        this.JG = JG;
        this.JJ = JJ;
        this.DG = DG;
        this.GC = GC;
        this.Posicion = Posicion;
        this.ligas = new ArrayList<>();
    }

    public Clasificacion(
        String Cod_Equipo,        String Puntos,        String JE,        String JP,        String GF,        String JG,        String JJ,        String DG,        String GC,        String Posicion        ArrayList<Liga> ligas    ) {
        this.Cod_Equipo = Cod_Equipo;
        this.Puntos = Puntos;
        this.JE = JE;
        this.JP = JP;
        this.GF = GF;
        this.JG = JG;
        this.JJ = JJ;
        this.DG = DG;
        this.GC = GC;
        this.Posicion = Posicion;
        this.ligas = ligas;
    }

    public String getCod_equipo() {
        return Cod_Equipo;
    }

    public void setCod_equipo(String Cod_Equipo) {
        this.Cod_Equipo = Cod_Equipo;
    }
    public String getPuntos() {
        return Puntos;
    }

    public void setPuntos(String Puntos) {
        this.Puntos = Puntos;
    }
    public String getJe() {
        return JE;
    }

    public void setJe(String JE) {
        this.JE = JE;
    }
    public String getJp() {
        return JP;
    }

    public void setJp(String JP) {
        this.JP = JP;
    }
    public String getGf() {
        return GF;
    }

    public void setGf(String GF) {
        this.GF = GF;
    }
    public String getJg() {
        return JG;
    }

    public void setJg(String JG) {
        this.JG = JG;
    }
    public String getJj() {
        return JJ;
    }

    public void setJj(String JJ) {
        this.JJ = JJ;
    }
    public String getDg() {
        return DG;
    }

    public void setDg(String DG) {
        this.DG = DG;
    }
    public String getGc() {
        return GC;
    }

    public void setGc(String GC) {
        this.GC = GC;
    }
    public String getPosicion() {
        return Posicion;
    }

    public void setPosicion(String Posicion) {
        this.Posicion = Posicion;
    }

    public List<Liga> getLigas() {
        return ligas;
    }

    public void addLiga(Liga liga) {
        this.ligas.add(liga);
    }

}