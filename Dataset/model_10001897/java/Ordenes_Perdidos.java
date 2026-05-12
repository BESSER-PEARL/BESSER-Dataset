





import java.util.List;
import java.util.ArrayList;

public class Ordenes_Perdidos  {

    private String Codigo;
    private String Fecha;



    public Ordenes_Perdidos(
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