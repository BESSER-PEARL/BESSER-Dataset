





import java.util.List;
import java.util.ArrayList;

public class Cliente1  {

    private String Telefono;
    private String Nombre;
    private String DNI;
    private String Fecha_de_Nac;
    private String Email;
    private String Apellido;



    public Cliente1(
        String Telefono,        String Nombre,        String DNI,        String Fecha_de_Nac,        String Email,        String Apellido    ) {
        this.Telefono = Telefono;
        this.Nombre = Nombre;
        this.DNI = DNI;
        this.Fecha_de_Nac = Fecha_de_Nac;
        this.Email = Email;
        this.Apellido = Apellido;
    }


    public String getTelefono() {
        return Telefono;
    }

    public void setTelefono(String Telefono) {
        this.Telefono = Telefono;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getDni() {
        return DNI;
    }

    public void setDni(String DNI) {
        this.DNI = DNI;
    }
    public String getFecha_de_nac() {
        return Fecha_de_Nac;
    }

    public void setFecha_de_nac(String Fecha_de_Nac) {
        this.Fecha_de_Nac = Fecha_de_Nac;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getApellido() {
        return Apellido;
    }

    public void setApellido(String Apellido) {
        this.Apellido = Apellido;
    }


}