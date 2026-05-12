





import java.util.List;
import java.util.ArrayList;

public class mundo_Galloanserae  {

    private String tipo;
    private String POLIGAMA;
    private String MONOGAMA;
    private String CAZA;
    private String reproduccion;
    private String DOMESTICA;



    public mundo_Galloanserae(
        String tipo,        String POLIGAMA,        String MONOGAMA,        String CAZA,        String reproduccion,        String DOMESTICA    ) {
        this.tipo = tipo;
        this.POLIGAMA = POLIGAMA;
        this.MONOGAMA = MONOGAMA;
        this.CAZA = CAZA;
        this.reproduccion = reproduccion;
        this.DOMESTICA = DOMESTICA;
    }


    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public String getPoligama() {
        return POLIGAMA;
    }

    public void setPoligama(String POLIGAMA) {
        this.POLIGAMA = POLIGAMA;
    }
    public String getMonogama() {
        return MONOGAMA;
    }

    public void setMonogama(String MONOGAMA) {
        this.MONOGAMA = MONOGAMA;
    }
    public String getCaza() {
        return CAZA;
    }

    public void setCaza(String CAZA) {
        this.CAZA = CAZA;
    }
    public String getReproduccion() {
        return reproduccion;
    }

    public void setReproduccion(String reproduccion) {
        this.reproduccion = reproduccion;
    }
    public String getDomestica() {
        return DOMESTICA;
    }

    public void setDomestica(String DOMESTICA) {
        this.DOMESTICA = DOMESTICA;
    }


}