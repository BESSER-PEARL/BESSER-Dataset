





import java.util.List;
import java.util.ArrayList;

public class Cliente  {

    private String Email;
    private String Direccion;
    private String Nombre;
    private String Apellido;





    private List<Articulo2> articulo2s;


    public Cliente(
        String Email,        String Direccion,        String Nombre,        String Apellido    ) {
        this.Email = Email;
        this.Direccion = Direccion;
        this.Nombre = Nombre;
        this.Apellido = Apellido;
        this.articulo2s = new ArrayList<>();
    }

    public Cliente(
        String Email,        String Direccion,        String Nombre,        String Apellido        ArrayList<Articulo2> articulo2s    ) {
        this.Email = Email;
        this.Direccion = Direccion;
        this.Nombre = Nombre;
        this.Apellido = Apellido;
        this.articulo2s = articulo2s;
    }

    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getDireccion() {
        return Direccion;
    }

    public void setDireccion(String Direccion) {
        this.Direccion = Direccion;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getApellido() {
        return Apellido;
    }

    public void setApellido(String Apellido) {
        this.Apellido = Apellido;
    }

    public List<Articulo2> getArticulo2s() {
        return articulo2s;
    }

    public void addArticulo2(Articulo2 articulo2) {
        this.articulo2s.add(articulo2);
    }

}