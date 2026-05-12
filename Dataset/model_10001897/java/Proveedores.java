





import java.util.List;
import java.util.ArrayList;

public class Proveedores  {

    private String Nit;
    private String Telefono;
    private String RazonSocial;
    private String Direccion;





    private List<Factura> facturas;




    private List<Ordenes_Perdidos> ordenes_perdidoss;


    public Proveedores(
        String Nit,        String Telefono,        String RazonSocial,        String Direccion    ) {
        this.Nit = Nit;
        this.Telefono = Telefono;
        this.RazonSocial = RazonSocial;
        this.Direccion = Direccion;
        this.facturas = new ArrayList<>();
        this.ordenes_perdidoss = new ArrayList<>();
    }

    public Proveedores(
        String Nit,        String Telefono,        String RazonSocial,        String Direccion        ArrayList<Factura> facturas,        ArrayList<Ordenes_Perdidos> ordenes_perdidoss    ) {
        this.Nit = Nit;
        this.Telefono = Telefono;
        this.RazonSocial = RazonSocial;
        this.Direccion = Direccion;
        this.facturas = facturas;
        this.ordenes_perdidoss = ordenes_perdidoss;
    }

    public String getNit() {
        return Nit;
    }

    public void setNit(String Nit) {
        this.Nit = Nit;
    }
    public String getTelefono() {
        return Telefono;
    }

    public void setTelefono(String Telefono) {
        this.Telefono = Telefono;
    }
    public String getRazonsocial() {
        return RazonSocial;
    }

    public void setRazonsocial(String RazonSocial) {
        this.RazonSocial = RazonSocial;
    }
    public String getDireccion() {
        return Direccion;
    }

    public void setDireccion(String Direccion) {
        this.Direccion = Direccion;
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

}