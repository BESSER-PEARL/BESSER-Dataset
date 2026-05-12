





import java.util.List;
import java.util.ArrayList;

public class Factura  {

    private String fecha;
    private String codigo;





    private Proveedores proveedores;




    private List<Elementos> elementoss;


    public Factura(
        String fecha,        String codigo    ) {
        this.fecha = fecha;
        this.codigo = codigo;
        this.elementoss = new ArrayList<>();
    }

    public Factura(
        String fecha,        String codigo        ArrayList<Elementos> elementoss    ) {
        this.fecha = fecha;
        this.codigo = codigo;
        this.elementoss = elementoss;
    }

    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }
    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public Proveedores getProveedores() {
        return proveedores;
    }

    public void setProveedores(Proveedores proveedores) {
        this.proveedores = proveedores;
    }
    public List<Elementos> getElementoss() {
        return elementoss;
    }

    public void addElementos(Elementos elementos) {
        this.elementoss.add(elementos);
    }

}