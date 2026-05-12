





import java.util.List;
import java.util.ArrayList;

public class ItemOrden  {

    private float price;
    private int quantity;





    private Venta venta;




    private Orden orden;


    public ItemOrden(
        float price,        int quantity    ) {
        this.price = price;
        this.quantity = quantity;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public Venta getVenta() {
        return venta;
    }

    public void setVenta(Venta venta) {
        this.venta = venta;
    }
    public Orden getOrden() {
        return orden;
    }

    public void setOrden(Orden orden) {
        this.orden = orden;
    }

}