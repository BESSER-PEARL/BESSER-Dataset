





import java.util.List;
import java.util.ArrayList;

public class Pago  {

    private String Codigo;
    private String Fecha;





    private List<Facturas> facturass;


    public Pago(
        String Codigo,        String Fecha    ) {
        this.Codigo = Codigo;
        this.Fecha = Fecha;
        this.facturass = new ArrayList<>();
    }

    public Pago(
        String Codigo,        String Fecha        ArrayList<Facturas> facturass    ) {
        this.Codigo = Codigo;
        this.Fecha = Fecha;
        this.facturass = facturass;
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

    public List<Facturas> getFacturass() {
        return facturass;
    }

    public void addFacturas(Facturas facturas) {
        this.facturass.add(facturas);
    }

}