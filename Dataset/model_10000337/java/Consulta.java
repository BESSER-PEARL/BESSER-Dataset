





import java.util.List;
import java.util.ArrayList;

public class Consulta  {

    private int mail;
    private int telefono;
    private int Administrador;
    private String nombre;





    private lugar lugar;


    public Consulta(
        int mail,        int telefono,        int Administrador,        String nombre    ) {
        this.mail = mail;
        this.telefono = telefono;
        this.Administrador = Administrador;
        this.nombre = nombre;
    }


    public int getMail() {
        return mail;
    }

    public void setMail(int mail) {
        this.mail = mail;
    }
    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }
    public int getAdministrador() {
        return Administrador;
    }

    public void setAdministrador(int Administrador) {
        this.Administrador = Administrador;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public lugar getLugar() {
        return lugar;
    }

    public void setLugar(lugar lugar) {
        this.lugar = lugar;
    }

}