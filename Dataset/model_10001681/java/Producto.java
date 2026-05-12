





import java.util.List;
import java.util.ArrayList;

public class Producto  {

    private String Modo_de_venta;
    private String Stock;
    private None Precio;



    public Producto(
        String Modo_de_venta,        String Stock,        None Precio    ) {
        this.Modo_de_venta = Modo_de_venta;
        this.Stock = Stock;
        this.Precio = Precio;
    }


    public String getModo_de_venta() {
        return Modo_de_venta;
    }

    public void setModo_de_venta(String Modo_de_venta) {
        this.Modo_de_venta = Modo_de_venta;
    }
    public String getStock() {
        return Stock;
    }

    public void setStock(String Stock) {
        this.Stock = Stock;
    }
    public None getPrecio() {
        return Precio;
    }

    public void setPrecio(None Precio) {
        this.Precio = Precio;
    }


}