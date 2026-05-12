





import java.util.List;
import java.util.ArrayList;

public class Clasificacion  {

    private String JG;
    private String Posicion;
    private String JE;
    private String JJ;
    private String GC;
    private String JP;
    private String Puntos;
    private String GF;
    private String Cod_Equipo;
    private String DG;





    private List<Liga> ligas;


    public Clasificacion(
        String JG,        String Posicion,        String JE,        String JJ,        String GC,        String JP,        String Puntos,        String GF,        String Cod_Equipo,        String DG    ) {
        this.JG = JG;
        this.Posicion = Posicion;
        this.JE = JE;
        this.JJ = JJ;
        this.GC = GC;
        this.JP = JP;
        this.Puntos = Puntos;
        this.GF = GF;
        this.Cod_Equipo = Cod_Equipo;
        this.DG = DG;
        this.ligas = new ArrayList<>();
    }

    public Clasificacion(
        String JG,        String Posicion,        String JE,        String JJ,        String GC,        String JP,        String Puntos,        String GF,        String Cod_Equipo,        String DG        ArrayList<Liga> ligas    ) {
        this.JG = JG;
        this.Posicion = Posicion;
        this.JE = JE;
        this.JJ = JJ;
        this.GC = GC;
        this.JP = JP;
        this.Puntos = Puntos;
        this.GF = GF;
        this.Cod_Equipo = Cod_Equipo;
        this.DG = DG;
        this.ligas = ligas;
    }

    public String getJg() {
        return JG;
    }

    public void setJg(String JG) {
        this.JG = JG;
    }
    public String getPosicion() {
        return Posicion;
    }

    public void setPosicion(String Posicion) {
        this.Posicion = Posicion;
    }
    public String getJe() {
        return JE;
    }

    public void setJe(String JE) {
        this.JE = JE;
    }
    public String getJj() {
        return JJ;
    }

    public void setJj(String JJ) {
        this.JJ = JJ;
    }
    public String getGc() {
        return GC;
    }

    public void setGc(String GC) {
        this.GC = GC;
    }
    public String getJp() {
        return JP;
    }

    public void setJp(String JP) {
        this.JP = JP;
    }
    public String getPuntos() {
        return Puntos;
    }

    public void setPuntos(String Puntos) {
        this.Puntos = Puntos;
    }
    public String getGf() {
        return GF;
    }

    public void setGf(String GF) {
        this.GF = GF;
    }
    public String getCod_equipo() {
        return Cod_Equipo;
    }

    public void setCod_equipo(String Cod_Equipo) {
        this.Cod_Equipo = Cod_Equipo;
    }
    public String getDg() {
        return DG;
    }

    public void setDg(String DG) {
        this.DG = DG;
    }

    public List<Liga> getLigas() {
        return ligas;
    }

    public void addLiga(Liga liga) {
        this.ligas.add(liga);
    }

}