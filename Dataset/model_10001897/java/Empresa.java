





import java.util.List;
import java.util.ArrayList;

public class Empresa  {

    private String nombre;
    private String ubicacion;
    private String codigo;





    private List<Facturas> facturass;




    private List<Presupuesto> presupuestos;


    public Empresa(
        String nombre,        String ubicacion,        String codigo    ) {
        this.nombre = nombre;
        this.ubicacion = ubicacion;
        this.codigo = codigo;
        this.facturass = new ArrayList<>();
        this.presupuestos = new ArrayList<>();
    }

    public Empresa(
        String nombre,        String ubicacion,        String codigo        ArrayList<Facturas> facturass,        ArrayList<Presupuesto> presupuestos    ) {
        this.nombre = nombre;
        this.ubicacion = ubicacion;
        this.codigo = codigo;
        this.facturass = facturass;
        this.presupuestos = presupuestos;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getUbicacion() {
        return ubicacion;
    }

    public void setUbicacion(String ubicacion) {
        this.ubicacion = ubicacion;
    }
    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public List<Facturas> getFacturass() {
        return facturass;
    }

    public void addFacturas(Facturas facturas) {
        this.facturass.add(facturas);
    }
    public List<Presupuesto> getPresupuestos() {
        return presupuestos;
    }

    public void addPresupuesto(Presupuesto presupuesto) {
        this.presupuestos.add(presupuesto);
    }

}