





import java.util.List;
import java.util.ArrayList;

public class SolicitudSuministro  {

    private String Codigo;
    private String Fecha;





    private List<ELementos> elementoss;




    private OrdenesPedidos ordenespedidos;




    private Dependencia dependencia;


    public SolicitudSuministro(
        String Codigo,        String Fecha    ) {
        this.Codigo = Codigo;
        this.Fecha = Fecha;
        this.elementoss = new ArrayList<>();
    }

    public SolicitudSuministro(
        String Codigo,        String Fecha        ArrayList<ELementos> elementoss    ) {
        this.Codigo = Codigo;
        this.Fecha = Fecha;
        this.elementoss = elementoss;
    }

    public String getCodigo() {
        return Codigo;
    }

    public void setCodigo(String Codigo) {
        this.Codigo = Codigo;
    }
    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }

    public List<ELementos> getElementoss() {
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
    public Dependencia getDependencia() {
        return dependencia;
    }

    public void setDependencia(Dependencia dependencia) {
        this.dependencia = dependencia;
    }

}