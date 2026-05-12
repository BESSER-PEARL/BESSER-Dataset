





import java.util.List;
import java.util.ArrayList;

public class Articulo2  {

    private String Descripci_n;
    private String Nombre;
    private None Precio;



    public Articulo2(
        String Descripci_n,        String Nombre,        None Precio    ) {
        this.Descripci_n = Descripci_n;
        this.Nombre = Nombre;
        this.Precio = Precio;
    }


    public String getDescripci_n() {
        return Descripci_n;
    }

    public void setDescripci_n(String Descripci_n) {
        this.Descripci_n = Descripci_n;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public None getPrecio() {
        return Precio;
    }

    public void setPrecio(None Precio) {
        this.Precio = Precio;
    }


}