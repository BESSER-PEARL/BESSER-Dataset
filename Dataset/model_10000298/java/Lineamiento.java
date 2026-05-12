





import java.util.List;
import java.util.ArrayList;

public class Lineamiento  {

    private int Cantidad;
    private float Costo;





    private Order order;




    private Toma_de_pedido toma_de_pedido;




    private ShoppingCart shoppingcart;


    public Lineamiento(
        int Cantidad,        float Costo    ) {
        this.Cantidad = Cantidad;
        this.Costo = Costo;
    }


    public int getCantidad() {
        return Cantidad;
    }

    public void setCantidad(int Cantidad) {
        this.Cantidad = Cantidad;
    }
    public float getCosto() {
        return Costo;
    }

    public void setCosto(float Costo) {
        this.Costo = Costo;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
    public Toma_de_pedido getToma_de_pedido() {
        return toma_de_pedido;
    }

    public void setToma_de_pedido(Toma_de_pedido toma_de_pedido) {
        this.toma_de_pedido = toma_de_pedido;
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}