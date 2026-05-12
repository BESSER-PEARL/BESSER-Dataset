





import java.util.List;
import java.util.ArrayList;

public class Tarjeta1  {

    private String tipoDeCarta;
    private String descripcion;



    public Tarjeta1(
        String tipoDeCarta,        String descripcion    ) {
        this.tipoDeCarta = tipoDeCarta;
        this.descripcion = descripcion;
    }


    public String getTipodecarta() {
        return tipoDeCarta;
    }

    public void setTipodecarta(String tipoDeCarta) {
        this.tipoDeCarta = tipoDeCarta;
    }
    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }


}