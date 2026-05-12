





import java.util.List;
import java.util.ArrayList;

public class Elementos  {

    private String referencia;
    private String clasificacion;





    private List<_rdenesPedido> _rdenespedidos;


    public Elementos(
        String referencia,        String clasificacion    ) {
        this.referencia = referencia;
        this.clasificacion = clasificacion;
        this._rdenespedidos = new ArrayList<>();
    }

    public Elementos(
        String referencia,        String clasificacion        ArrayList<_rdenesPedido> _rdenespedidos    ) {
        this.referencia = referencia;
        this.clasificacion = clasificacion;
        this._rdenespedidos = _rdenespedidos;
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

    public List<_rdenesPedido> get_rdenespedidos() {
        return _rdenespedidos;
    }

    public void add_rdenespedido(_rdenespedido _rdenespedido) {
        this._rdenespedidos.add(_rdenespedido);
    }

}