





import java.util.List;
import java.util.ArrayList;

public class SolicitudSuministro  {

    private String codigo;
    private String fecha;





    private OrdenesPedidos ordenespedidos;




    private List<Elementos> elementoss;


    public SolicitudSuministro(
        String codigo,        String fecha    ) {
        this.codigo = codigo;
        this.fecha = fecha;
        this.elementoss = new ArrayList<>();
    }

    public SolicitudSuministro(
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

    public OrdenesPedidos getOrdenespedidos() {
        return ordenespedidos;
    }

    public void setOrdenespedidos(OrdenesPedidos ordenespedidos) {
        this.ordenespedidos = ordenespedidos;
    }
    public List<Elementos> getElementoss() {
        return elementoss;
    }

    public void addElementos(Elementos elementos) {
        this.elementoss.add(elementos);
    }

}