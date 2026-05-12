





import java.util.List;
import java.util.ArrayList;

public class Direccion  {

    private int codigo;
    private String pais;
    private String nombre;
    private String ciudad;





    private Contacto contacto;




    private Contacto contacto;


    public Direccion(
        int codigo,        String pais,        String nombre,        String ciudad    ) {
        this.codigo = codigo;
        this.pais = pais;
        this.nombre = nombre;
        this.ciudad = ciudad;
    }


    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }
    public String getPais() {
        return pais;
    }

    public void setPais(String pais) {
        this.pais = pais;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getCiudad() {
        return ciudad;
    }

    public void setCiudad(String ciudad) {
        this.ciudad = ciudad;
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