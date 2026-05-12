





import java.util.List;
import java.util.ArrayList;

public class Clasificacion  {

    private String JG;
    private String Posicion;
    private String Cod_Equipo;
    private String JE;
    private String JJ;
    private String JP;
    private String DG;
    private String GC;
    private String Puntos;
    private String GF;





    private List<Liga> ligas;


    public Clasificacion(
        String JG,        String Posicion,        String Cod_Equipo,        String JE,        String JJ,        String JP,        String DG,        String GC,        String Puntos,        String GF    ) {
        this.JG = JG;
        this.Posicion = Posicion;
        this.Cod_Equipo = Cod_Equipo;
        this.JE = JE;
        this.JJ = JJ;
        this.JP = JP;
        this.DG = DG;
        this.GC = GC;
        this.Puntos = Puntos;
        this.GF = GF;
        this.ligas = new ArrayList<>();
    }

    public Clasificacion(
        String JG,        String Posicion,        String Cod_Equipo,        String JE,        String JJ,        String JP,        String DG,        String GC,        String Puntos,        String GF        ArrayList<Liga> ligas    ) {
        this.JG = JG;
        this.Posicion = Posicion;
        this.Cod_Equipo = Cod_Equipo;
        this.JE = JE;
        this.JJ = JJ;
        this.JP = JP;
        this.DG = DG;
        this.GC = GC;
        this.Puntos = Puntos;
        this.GF = GF;
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
    public String getCod_equipo() {
        return Cod_Equipo;
    }

    public void setCod_equipo(String Cod_Equipo) {
        this.Cod_Equipo = Cod_Equipo;
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
    public String getGc() {
        return GC;
    }

    public void setGc(String GC) {
        this.GC = GC;
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

    public List<Liga> getLigas() {
        return ligas;
    }

    public void addLiga(Liga liga) {
        this.ligas.add(liga);
    }

}