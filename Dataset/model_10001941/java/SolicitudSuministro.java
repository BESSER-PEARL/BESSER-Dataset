





import java.util.List;
import java.util.ArrayList;

public class SolicitudSuministro  {

    private String fecha;
    private String solicitud;





    private Elementos elementos;




    private _rdenesPedido _rdenespedido;


    public SolicitudSuministro(
        String fecha,        String solicitud    ) {
        this.fecha = fecha;
        this.solicitud = solicitud;
    }


    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }
    public String getSolicitud() {
        return solicitud;
    }

    public void setSolicitud(String solicitud) {
        this.solicitud = solicitud;
    }

    public Elementos getElementos() {
        return elementos;
    }

    public void setElementos(Elementos elementos) {
        this.elementos = elementos;
    }
    public _rdenesPedido get_rdenespedido() {
        return _rdenespedido;
    }

    public void set_rdenespedido(_rdenesPedido _rdenespedido) {
        this._rdenespedido = _rdenespedido;
    }

}