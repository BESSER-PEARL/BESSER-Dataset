





import java.util.List;
import java.util.ArrayList;

public class Clasificacion  {

    private String GC;
    private String JG;
    private String JE;
    private String GF;
    private String JJ;
    private String Posicion;
    private String JP;
    private String DG;
    private String Cod_Equipo;
    private String Puntos;





    private List<Liga> ligas;


    public Clasificacion(
        String GC,        String JG,        String JE,        String GF,        String JJ,        String Posicion,        String JP,        String DG,        String Cod_Equipo,        String Puntos    ) {
        this.GC = GC;
        this.JG = JG;
        this.JE = JE;
        this.GF = GF;
        this.JJ = JJ;
        this.Posicion = Posicion;
        this.JP = JP;
        this.DG = DG;
        this.Cod_Equipo = Cod_Equipo;
        this.Puntos = Puntos;
        this.ligas = new ArrayList<>();
    }

    public Clasificacion(
        String GC,        String JG,        String JE,        String GF,        String JJ,        String Posicion,        String JP,        String DG,        String Cod_Equipo,        String Puntos        ArrayList<Liga> ligas    ) {
        this.GC = GC;
        this.JG = JG;
        this.JE = JE;
        this.GF = GF;
        this.JJ = JJ;
        this.Posicion = Posicion;
        this.JP = JP;
        this.DG = DG;
        this.Cod_Equipo = Cod_Equipo;
        this.Puntos = Puntos;
        this.ligas = ligas;
    }

    public String getGc() {
        return GC;
    }

    public void setGc(String GC) {
        this.GC = GC;
    }
    public String getJg() {
        return JG;
    }

    public void setJg(String JG) {
        this.JG = JG;
    }
    public String getJe() {
        return JE;
    }

    public void setJe(String JE) {
        this.JE = JE;
    }
    public String getGf() {
        return GF;
    }

    public void setGf(String GF) {
        this.GF = GF;
    }
    public String getJj() {
        return JJ;
    }

    public void setJj(String JJ) {
        this.JJ = JJ;
    }
    public String getPosicion() {
        return Posicion;
    }

    public void setPosicion(String Posicion) {
        this.Posicion = Posicion;
    }
    public String getJp() {
        return JP;
    }

    public void setJp(String JP) {
        this.JP = JP;
    }
    public String getDg() {
        return DG;
    }

    public void setDg(String DG) {
        this.DG = DG;
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

    public List<Liga> getLigas() {
        return ligas;
    }

    public void addLiga(Liga liga) {
        this.ligas.add(liga);
    }

}