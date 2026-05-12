





import java.util.List;
import java.util.ArrayList;

public class Impuesto  {

    private float CalcularImpuesto;
    private float Porcentae;





    private Venta venta;




    private Producto producto;


    public Impuesto(
        float CalcularImpuesto,        float Porcentae    ) {
        this.CalcularImpuesto = CalcularImpuesto;
        this.Porcentae = Porcentae;
    }


    public float getCalcularimpuesto() {
        return CalcularImpuesto;
    }

    public void setCalcularimpuesto(float CalcularImpuesto) {
        this.CalcularImpuesto = CalcularImpuesto;
    }
    public float getPorcentae() {
        return Porcentae;
    }

    public void setPorcentae(float Porcentae) {
        this.Porcentae = Porcentae;
    }

    public Venta getVenta() {
        return venta;
    }

    public void setVenta(Venta venta) {
        this.venta = venta;
    }
    public Producto getProducto() {
        return producto;
    }

    public void setProducto(Producto producto) {
        this.producto = producto;
    }

}