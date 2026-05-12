





import java.util.List;
import java.util.ArrayList;

public class Carro_de_Compras  {

    private int Precio;
    private int Cantidad;
    private int IdCarro;
    private String Producto;



    public Carro_de_Compras(
        int Precio,        int Cantidad,        int IdCarro,        String Producto    ) {
        this.Precio = Precio;
        this.Cantidad = Cantidad;
        this.IdCarro = IdCarro;
        this.Producto = Producto;
    }


    public int getPrecio() {
        return Precio;
    }

    public void setPrecio(int Precio) {
        this.Precio = Precio;
    }
    public int getCantidad() {
        return Cantidad;
    }

    public void setCantidad(int Cantidad) {
        this.Cantidad = Cantidad;
    }
    public int getIdcarro() {
        return IdCarro;
    }

    public void setIdcarro(int IdCarro) {
        this.IdCarro = IdCarro;
    }
    public String getProducto() {
        return Producto;
    }

    public void setProducto(String Producto) {
        this.Producto = Producto;
    }


}