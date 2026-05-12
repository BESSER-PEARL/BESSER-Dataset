





import java.util.List;
import java.util.ArrayList;

public class Elementos  {

    private String referencia;
    private String clasificacion;





    private List<OrdenesPedidos> ordenespedidoss;




    private List<Factura> facturas;


    public Elementos(
        String referencia,        String clasificacion    ) {
        this.referencia = referencia;
        this.clasificacion = clasificacion;
        this.ordenespedidoss = new ArrayList<>();
        this.facturas = new ArrayList<>();
    }

    public Elementos(
        String referencia,        String clasificacion        ArrayList<OrdenesPedidos> ordenespedidoss,        ArrayList<Factura> facturas    ) {
        this.referencia = referencia;
        this.clasificacion = clasificacion;
        this.ordenespedidoss = ordenespedidoss;
        this.facturas = facturas;
    }

    public String getReferencia() {
        return referencia;
    }

    public void setReferencia(String referencia) {
        this.referencia = referencia;
    }
    public String getClasificacion() {
        return clasificacion;
    }

    public void setClasificacion(String clasificacion) {
        this.clasificacion = clasificacion;
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