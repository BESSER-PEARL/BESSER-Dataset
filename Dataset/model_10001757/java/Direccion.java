





import java.util.List;
import java.util.ArrayList;

public class Direccion  {

    private String Ciudad;
    private String Nombre;
    private int Codigo_Postal;
    private String Pais;





    private Contacto contacto;




    private Contacto contacto;


    public Direccion(
        String Ciudad,        String Nombre,        int Codigo_Postal,        String Pais    ) {
        this.Ciudad = Ciudad;
        this.Nombre = Nombre;
        this.Codigo_Postal = Codigo_Postal;
        this.Pais = Pais;
    }


    public String getCiudad() {
        return Ciudad;
    }

    public void setCiudad(String Ciudad) {
        this.Ciudad = Ciudad;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public int getCodigo_postal() {
        return Codigo_Postal;
    }

    public void setCodigo_postal(int Codigo_Postal) {
        this.Codigo_Postal = Codigo_Postal;
    }
    public String getPais() {
        return Pais;
    }

    public void setPais(String Pais) {
        this.Pais = Pais;
    }

    public Contacto getContacto() {
        return contacto;
    }

    public void setContacto(Contacto contacto) {
        this.contacto = contacto;
    }
    public Contacto getContacto() {
        return contacto;
    }

    public void setContacto(Contacto contacto) {
        this.contacto = contacto;
    }

}