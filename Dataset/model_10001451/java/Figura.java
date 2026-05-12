





import java.util.List;
import java.util.ArrayList;

public class Figura  {

    private boolean estado;
    private int valor;



    public Figura(
        boolean estado,        int valor    ) {
        this.estado = estado;
        this.valor = valor;
    }


    public boolean getEstado() {
        return estado;
    }

    public void setEstado(boolean estado) {
        this.estado = estado;
    }
    public int getValor() {
        return valor;
    }

    public void setValor(int valor) {
        this.valor = valor;
    }


}