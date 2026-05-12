





import java.util.List;
import java.util.ArrayList;

public class Articulo2  {

    private String Descripci_n;
    private None Precio;
    private String Nombre;



    public Articulo2(
        String Descripci_n,        None Precio,        String Nombre    ) {
        this.Descripci_n = Descripci_n;
        this.Precio = Precio;
        this.Nombre = Nombre;
    }


    public String getDescripci_n() {
        return Descripci_n;
    }

    public void setDescripci_n(String Descripci_n) {
        this.Descripci_n = Descripci_n;
    }
    public None getPrecio() {
        return Precio;
    }

    public void setPrecio(None Precio) {
        this.Precio = Precio;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }


}