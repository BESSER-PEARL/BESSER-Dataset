





import java.util.List;
import java.util.ArrayList;

public class producto  {

    private int setCantidad;
    private String setNombre;
    private String setCodigo;
    private float setPrecio;





    private venta venta;


    public producto(
        int setCantidad,        String setNombre,        String setCodigo,        float setPrecio    ) {
        this.setCantidad = setCantidad;
        this.setNombre = setNombre;
        this.setCodigo = setCodigo;
        this.setPrecio = setPrecio;
    }


    public int getSetcantidad() {
        return setCantidad;
    }

    public void setSetcantidad(int setCantidad) {
        this.setCantidad = setCantidad;
    }
    public String getSetnombre() {
        return setNombre;
    }

    public void setSetnombre(String setNombre) {
        this.setNombre = setNombre;
    }
    public String getSetcodigo() {
        return setCodigo;
    }

    public void setSetcodigo(String setCodigo) {
        this.setCodigo = setCodigo;
    }
    public float getSetprecio() {
        return setPrecio;
    }

    public void setSetprecio(float setPrecio) {
        this.setPrecio = setPrecio;
    }

    public venta getVenta() {
        return venta;
    }

    public void setVenta(venta venta) {
        this.venta = venta;
    }

}