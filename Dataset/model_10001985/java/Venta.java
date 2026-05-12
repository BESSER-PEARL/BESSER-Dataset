





import java.util.List;
import java.util.ArrayList;

public class Venta  {

    private int Codigo;
    private String Fecha;
    private String RealizarVenta;



    public Venta(
        int Codigo,        String Fecha,        String RealizarVenta    ) {
        this.Codigo = Codigo;
        this.Fecha = Fecha;
        this.RealizarVenta = RealizarVenta;
    }


    public int getCodigo() {
        return Codigo;
    }

    public void setCodigo(int Codigo) {
        this.Codigo = Codigo;
    }
    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }
    public String getRealizarventa() {
        return RealizarVenta;
    }

    public void setRealizarventa(String RealizarVenta) {
        this.RealizarVenta = RealizarVenta;
    }


}