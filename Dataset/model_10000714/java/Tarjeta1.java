





import java.util.List;
import java.util.ArrayList;

public class Tarjeta1  {

    private String descripcion;
    private String tipoDeCarta;



    public Tarjeta1(
        String descripcion,        String tipoDeCarta    ) {
        this.descripcion = descripcion;
        this.tipoDeCarta = tipoDeCarta;
    }


    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }
    public String getTipodecarta() {
        return tipoDeCarta;
    }

    public void setTipodecarta(String tipoDeCarta) {
        this.tipoDeCarta = tipoDeCarta;
    }


}