





import java.util.List;
import java.util.ArrayList;

public class Factura  {

    private String codigo;
    private String fecha;





    private List<Elementos> elementoss;




    private Proveedor proveedor;


    public Factura(
        String codigo,        String fecha    ) {
        this.codigo = codigo;
        this.fecha = fecha;
        this.elementoss = new ArrayList<>();
    }

    public Factura(
        String codigo,        String fecha        ArrayList<Elementos> elementoss    ) {
        this.codigo = codigo;
        this.fecha = fecha;
        this.elementoss = elementoss;
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

    public List<Elementos> getElementoss() {
        return elementoss;
    }

    public void addElementos(Elementos elementos) {
        this.elementoss.add(elementos);
    }
    public Proveedor getProveedor() {
        return proveedor;
    }

    public void setProveedor(Proveedor proveedor) {
        this.proveedor = proveedor;
    }

}