





import java.util.List;
import java.util.ArrayList;

public class Impuesto  {

    private float porcentaje;





    private Producto producto;


    public Impuesto(
        float porcentaje    ) {
        this.porcentaje = porcentaje;
    }


    public float getPorcentaje() {
        return porcentaje;
    }

    public void setPorcentaje(float porcentaje) {
        this.porcentaje = porcentaje;
    }

    public Producto getProducto() {
        return producto;
    }

    public void setProducto(Producto producto) {
        this.producto = producto;
    }

}