





import java.util.List;
import java.util.ArrayList;

public class impuesto  {

    private float setPorcentaje;





    private producto producto;


    public impuesto(
        float setPorcentaje    ) {
        this.setPorcentaje = setPorcentaje;
    }


    public float getSetporcentaje() {
        return setPorcentaje;
    }

    public void setSetporcentaje(float setPorcentaje) {
        this.setPorcentaje = setPorcentaje;
    }

    public producto getProducto() {
        return producto;
    }

    public void setProducto(producto producto) {
        this.producto = producto;
    }

}