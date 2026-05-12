





import java.util.List;
import java.util.ArrayList;

public class SolicitudSuministros  {

    private String fecha;
    private String codigo;





    private List<Elementos> elementoss;




    private OrdenesPedidos ordenespedidos;


    public SolicitudSuministros(
        String fecha,        String codigo    ) {
        this.fecha = fecha;
        this.codigo = codigo;
        this.elementoss = new ArrayList<>();
    }

    public SolicitudSuministros(
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

    public List<Elementos> getElementoss() {
        return elementoss;
    }

    public void addElementos(Elementos elementos) {
        this.elementoss.add(elementos);
    }
    public OrdenesPedidos getOrdenespedidos() {
        return ordenespedidos;
    }

    public void setOrdenespedidos(OrdenesPedidos ordenespedidos) {
        this.ordenespedidos = ordenespedidos;
    }

}