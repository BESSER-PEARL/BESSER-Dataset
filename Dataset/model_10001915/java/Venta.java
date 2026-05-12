





import java.util.List;
import java.util.ArrayList;

public class Venta  {

    private int codigo;
    private String fecha;



    public Venta(
        int codigo,        String fecha    ) {
        this.codigo = codigo;
        this.fecha = fecha;
    }


    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }
    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }


}