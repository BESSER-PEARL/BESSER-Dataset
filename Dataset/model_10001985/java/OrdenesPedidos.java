





import java.util.List;
import java.util.ArrayList;

public class OrdenesPedidos  {

    private String Codigo;
    private String Fecha;



    public OrdenesPedidos(
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


}