





import java.util.List;
import java.util.ArrayList;

public class Elementos  {

    private String clasificacion;
    private String referencia;





    private List<Factura> facturas;




    private List<Ordenes_Pedidos> ordenes_pedidoss;




    private List<Solicitud_Suministros> solicitud_suministross;


    public Elementos(
        String clasificacion,        String referencia    ) {
        this.clasificacion = clasificacion;
        this.referencia = referencia;
        this.facturas = new ArrayList<>();
        this.ordenes_pedidoss = new ArrayList<>();
        this.solicitud_suministross = new ArrayList<>();
    }

    public Elementos(
        String clasificacion,        String referencia        ArrayList<Factura> facturas,        ArrayList<Ordenes_Pedidos> ordenes_pedidoss,        ArrayList<Solicitud_Suministros> solicitud_suministross    ) {
        this.clasificacion = clasificacion;
        this.referencia = referencia;
        this.facturas = facturas;
        this.ordenes_pedidoss = ordenes_pedidoss;
        this.solicitud_suministross = solicitud_suministross;
    }

    public String getClasificacion() {
        return clasificacion;
    }

    public void setClasificacion(String clasificacion) {
        this.clasificacion = clasificacion;
    }
    public String getReferencia() {
        return referencia;
    }

    public void setReferencia(String referencia) {
        this.referencia = referencia;
    }

    public List<Factura> getFacturas() {
        return facturas;
    }

    public void addFactura(Factura factura) {
        this.facturas.add(factura);
    }
    public List<Ordenes_Pedidos> getOrdenes_pedidoss() {
        return ordenes_pedidoss;
    }

    public void addOrdenes_pedidos(Ordenes_pedidos ordenes_pedidos) {
        this.ordenes_pedidoss.add(ordenes_pedidos);
    }
    public List<Solicitud_Suministros> getSolicitud_suministross() {
        return solicitud_suministross;
    }

    public void addSolicitud_suministros(Solicitud_suministros solicitud_suministros) {
        this.solicitud_suministross.add(solicitud_suministros);
    }

}