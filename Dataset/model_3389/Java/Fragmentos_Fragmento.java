





import java.util.List;
import java.util.ArrayList;

public class Fragmentos_Fragmento  {

    private String texto;
    private int numLinea;
    private int posCaracter;





    private Fragmentos_Fragmento fragmentos_fragmento;




    private Fragmentos_Fichero fragmentos_fichero;




    private Fragmentos_Fichero fragmentos_fichero;


    public Fragmentos_Fragmento(
        String texto,        int numLinea,        int posCaracter    ) {
        this.texto = texto;
        this.numLinea = numLinea;
        this.posCaracter = posCaracter;
    }


    public String getTexto() {
        return texto;
    }

    public void setTexto(String texto) {
        this.texto = texto;
    }
    public int getNumlinea() {
        return numLinea;
    }

    public void setNumlinea(int numLinea) {
        this.numLinea = numLinea;
    }
    public int getPoscaracter() {
        return posCaracter;
    }

    public void setPoscaracter(int posCaracter) {
        this.posCaracter = posCaracter;
    }

    public Fragmentos_Fragmento getFragmentos_fragmento() {
        return fragmentos_fragmento;
    }

    public void setFragmentos_fragmento(Fragmentos_Fragmento fragmentos_fragmento) {
        this.fragmentos_fragmento = fragmentos_fragmento;
    }
    public Fragmentos_Fichero getFragmentos_fichero() {
        return fragmentos_fichero;
    }

    public void setFragmentos_fichero(Fragmentos_Fichero fragmentos_fichero) {
        this.fragmentos_fichero = fragmentos_fichero;
    }
    public Fragmentos_Fichero getFragmentos_fichero() {
        return fragmentos_fichero;
    }

    public void setFragmentos_fichero(Fragmentos_Fichero fragmentos_fichero) {
        this.fragmentos_fichero = fragmentos_fichero;
    }

}