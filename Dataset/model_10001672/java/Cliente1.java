





import java.util.List;
import java.util.ArrayList;

public class Cliente1  {

    private String Apellido;
    private String Fecha_de_Nac;
    private String Telefono;
    private String Email;
    private String DNI;
    private String Nombre;



    public Cliente1(
        String Apellido,        String Fecha_de_Nac,        String Telefono,        String Email,        String DNI,        String Nombre    ) {
        this.Apellido = Apellido;
        this.Fecha_de_Nac = Fecha_de_Nac;
        this.Telefono = Telefono;
        this.Email = Email;
        this.DNI = DNI;
        this.Nombre = Nombre;
    }


    public String getApellido() {
        return Apellido;
    }

    public void setApellido(String Apellido) {
        this.Apellido = Apellido;
    }
    public String getFecha_de_nac() {
        return Fecha_de_Nac;
    }

    public void setFecha_de_nac(String Fecha_de_Nac) {
        this.Fecha_de_Nac = Fecha_de_Nac;
    }
    public String getTelefono() {
        return Telefono;
    }

    public void setTelefono(String Telefono) {
        this.Telefono = Telefono;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getDni() {
        return DNI;
    }

    public void setDni(String DNI) {
        this.DNI = DNI;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }


}