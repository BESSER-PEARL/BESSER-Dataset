





import java.util.List;
import java.util.ArrayList;

public class Planos  {

    private String Codigo;
    private String Fecha;
    private String Escala;





    private Obras obras;


    public Planos(
        String Codigo,        String Fecha,        String Escala    ) {
        this.Codigo = Codigo;
        this.Fecha = Fecha;
        this.Escala = Escala;
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
    public String getEscala() {
        return Escala;
    }

    public void setEscala(String Escala) {
        this.Escala = Escala;
    }

    public Obras getObras() {
        return obras;
    }

    public void setObras(Obras obras) {
        this.obras = obras;
    }

}