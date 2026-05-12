





import java.util.List;
import java.util.ArrayList;

public class Elementos  {

    private String Referencia;
    private String Clasificacion;





    private List<Factura> facturas;




    private List<Ordenes_Perdidos> ordenes_perdidoss;




    private List<Solicitud_suministro> solicitud_suministros;


    public Elementos(
        String Referencia,        String Clasificacion    ) {
        this.Referencia = Referencia;
        this.Clasificacion = Clasificacion;
        this.facturas = new ArrayList<>();
        this.ordenes_perdidoss = new ArrayList<>();
        this.solicitud_suministros = new ArrayList<>();
    }

    public Elementos(
        String Referencia,        String Clasificacion        ArrayList<Factura> facturas,        ArrayList<Ordenes_Perdidos> ordenes_perdidoss,        ArrayList<Solicitud_suministro> solicitud_suministros    ) {
        this.Referencia = Referencia;
        this.Clasificacion = Clasificacion;
        this.facturas = facturas;
        this.ordenes_perdidoss = ordenes_perdidoss;
        this.solicitud_suministros = solicitud_suministros;
    }

    public String getReferencia() {
        return Referencia;
    }

    public void setReferencia(String Referencia) {
        this.Referencia = Referencia;
    }
    public String getClasificacion() {
        return Clasificacion;
    }

    public void setClasificacion(String Clasificacion) {
        this.Clasificacion = Clasificacion;
    }

    public List<Factura> getFacturas() {
        return facturas;
    }

    public void addFactura(Factura factura) {
        this.facturas.add(factura);
    }
    public List<Ordenes_Perdidos> getOrdenes_perdidoss() {
        return ordenes_perdidoss;
    }

    public void addOrdenes_perdidos(Ordenes_perdidos ordenes_perdidos) {
        this.ordenes_perdidoss.add(ordenes_perdidos);
    }
    public List<Solicitud_suministro> getSolicitud_suministros() {
        return solicitud_suministros;
    }

    public void addSolicitud_suministro(Solicitud_suministro solicitud_suministro) {
        this.solicitud_suministros.add(solicitud_suministro);
    }

}