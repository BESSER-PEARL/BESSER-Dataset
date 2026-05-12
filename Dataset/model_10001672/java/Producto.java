





import java.util.List;
import java.util.ArrayList;

public class Producto  {

    private String Modo_de_venta;
    private None Precio;
    private String Stock;



    public Producto(
        String Modo_de_venta,        None Precio,        String Stock    ) {
        this.Modo_de_venta = Modo_de_venta;
        this.Precio = Precio;
        this.Stock = Stock;
    }


    public String getModo_de_venta() {
        return Modo_de_venta;
    }

    public void setModo_de_venta(String Modo_de_venta) {
        this.Modo_de_venta = Modo_de_venta;
    }
    public None getPrecio() {
        return Precio;
    }

    public void setPrecio(None Precio) {
        this.Precio = Precio;
    }
    public String getStock() {
        return Stock;
    }

    public void setStock(String Stock) {
        this.Stock = Stock;
    }


}