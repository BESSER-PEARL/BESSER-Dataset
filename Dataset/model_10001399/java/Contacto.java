





import java.util.List;
import java.util.ArrayList;

public class Contacto  {

    private int id;
    private int Telefono;
    private String Nombre;
    private String user;
    private String Groups;
    private String Email;
    private String Foto;
    private String Apellido;



    public Contacto(
        int id,        int Telefono,        String Nombre,        String user,        String Groups,        String Email,        String Foto,        String Apellido    ) {
        this.id = id;
        this.Telefono = Telefono;
        this.Nombre = Nombre;
        this.user = user;
        this.Groups = Groups;
        this.Email = Email;
        this.Foto = Foto;
        this.Apellido = Apellido;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getTelefono() {
        return Telefono;
    }

    public void setTelefono(int Telefono) {
        this.Telefono = Telefono;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public String getGroups() {
        return Groups;
    }

    public void setGroups(String Groups) {
        this.Groups = Groups;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getFoto() {
        return Foto;
    }

    public void setFoto(String Foto) {
        this.Foto = Foto;
    }
    public String getApellido() {
        return Apellido;
    }

    public void setApellido(String Apellido) {
        this.Apellido = Apellido;
    }


}