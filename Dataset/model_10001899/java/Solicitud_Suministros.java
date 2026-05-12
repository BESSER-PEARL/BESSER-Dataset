





import java.util.List;
import java.util.ArrayList;

public class Solicitud_Suministros  {

    private String fecha;
    private String codigo;





    private Dependencia dependencia;




    private Ordenes_Pedidos ordenes_pedidos;


    public Solicitud_Suministros(
        String fecha,        String codigo    ) {
        this.fecha = fecha;
        this.codigo = codigo;
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

    public Dependencia getDependencia() {
        return dependencia;
    }

    public void setDependencia(Dependencia dependencia) {
        this.dependencia = dependencia;
    }
    public Ordenes_Pedidos getOrdenes_pedidos() {
        return ordenes_pedidos;
    }

    public void setOrdenes_pedidos(Ordenes_Pedidos ordenes_pedidos) {
        this.ordenes_pedidos = ordenes_pedidos;
    }

}