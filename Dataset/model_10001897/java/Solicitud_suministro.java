





import java.util.List;
import java.util.ArrayList;

public class Solicitud_suministro  {

    private String Codigo;
    private String Fecha;





    private Ordenes_Perdidos ordenes_perdidos;


    public Solicitud_suministro(
        String Codigo,        String Fecha    ) {
        this.Codigo = Codigo;
        this.Fecha = Fecha;
    }


    public String getCodigo() {
        return Codigo;
    }

    public void setCodigo(String Codigo) {
        this.Codigo = Codigo;
    }
    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }

    public Ordenes_Perdidos getOrdenes_perdidos() {
        return ordenes_perdidos;
    }

    public void setOrdenes_perdidos(Ordenes_Perdidos ordenes_perdidos) {
        this.ordenes_perdidos = ordenes_perdidos;
    }

}