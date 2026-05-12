





import java.util.List;
import java.util.ArrayList;

public class ELementos  {

    private String REferencia;
    private String Clasificacion;





    private List<OrdenesPedidos> ordenespedidoss;




    private List<Factura> facturas;


    public ELementos(
        String REferencia,        String Clasificacion    ) {
        this.REferencia = REferencia;
        this.Clasificacion = Clasificacion;
        this.ordenespedidoss = new ArrayList<>();
        this.facturas = new ArrayList<>();
    }

    public ELementos(
        String REferencia,        String Clasificacion        ArrayList<OrdenesPedidos> ordenespedidoss,        ArrayList<Factura> facturas    ) {
        this.REferencia = REferencia;
        this.Clasificacion = Clasificacion;
        this.ordenespedidoss = ordenespedidoss;
        this.facturas = facturas;
    }

    public String getReferencia() {
        return REferencia;
    }

    public void setReferencia(String REferencia) {
        this.REferencia = REferencia;
    }
    public String getClasificacion() {
        return Clasificacion;
    }

    public void setClasificacion(String Clasificacion) {
        this.Clasificacion = Clasificacion;
    }

    public List<OrdenesPedidos> getOrdenespedidoss() {
        return ordenespedidoss;
    }

    public void addOrdenespedidos(Ordenespedidos ordenespedidos) {
        this.ordenespedidoss.add(ordenespedidos);
    }
    public List<Factura> getFacturas() {
        return facturas;
    }

    public void addFactura(Factura factura) {
        this.facturas.add(factura);
    }

}