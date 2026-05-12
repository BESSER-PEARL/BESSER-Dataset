





import java.util.List;
import java.util.ArrayList;

public class Pedidos  {

    private String codigo;
    private String fecha;



    public Pedidos(
        String codigo,        String fecha    ) {
        this.codigo = codigo;
        this.fecha = fecha;
    }


    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }
    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }


}