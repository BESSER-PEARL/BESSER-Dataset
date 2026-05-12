





import java.util.List;
import java.util.ArrayList;

public class Tarjeta  {

    private int numeroTarje;
    private int codigoSeguridad;



    public Tarjeta(
        int numeroTarje,        int codigoSeguridad    ) {
        this.numeroTarje = numeroTarje;
        this.codigoSeguridad = codigoSeguridad;
    }


    public int getNumerotarje() {
        return numeroTarje;
    }

    public void setNumerotarje(int numeroTarje) {
        this.numeroTarje = numeroTarje;
    }
    public int getCodigoseguridad() {
        return codigoSeguridad;
    }

    public void setCodigoseguridad(int codigoSeguridad) {
        this.codigoSeguridad = codigoSeguridad;
    }


}