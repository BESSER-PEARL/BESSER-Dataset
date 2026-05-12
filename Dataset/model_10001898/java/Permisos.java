





import java.util.List;
import java.util.ArrayList;

public class Permisos  {

    private String Fecha;
    private String Codigo;
    private String Estado;





    private Planos planos;


    public Permisos(
        String Fecha,        String Codigo,        String Estado    ) {
        this.Fecha = Fecha;
        this.Codigo = Codigo;
        this.Estado = Estado;
    }


    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }
    public String getCodigo() {
        return Codigo;
    }

    public void setCodigo(String Codigo) {
        this.Codigo = Codigo;
    }
    public String getEstado() {
        return Estado;
    }

    public void setEstado(String Estado) {
        this.Estado = Estado;
    }

    public Planos getPlanos() {
        return planos;
    }

    public void setPlanos(Planos planos) {
        this.planos = planos;
    }

}