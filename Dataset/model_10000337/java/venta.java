





import java.util.List;
import java.util.ArrayList;

public class venta  {

    private int quantity;
    private float price;





    private producto producto;




    private lugar lugar;


    public venta(
        int quantity,        float price    ) {
        this.quantity = quantity;
        this.price = price;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public producto getProducto() {
        return producto;
    }

    public void setProducto(producto producto) {
        this.producto = producto;
    }
    public lugar getLugar() {
        return lugar;
    }

    public void setLugar(lugar lugar) {
        this.lugar = lugar;
    }

}