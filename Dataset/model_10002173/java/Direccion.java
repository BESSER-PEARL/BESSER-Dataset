





import java.util.List;
import java.util.ArrayList;

public class Direccion  {

    private String ciudad;
    private String pais;
    private int codigo;
    private String nombre;





    private Contacto contacto;




    private Contacto contacto;


    public Direccion(
        String ciudad,        String pais,        int codigo,        String nombre    ) {
        this.ciudad = ciudad;
        this.pais = pais;
        this.codigo = codigo;
        this.nombre = nombre;
    }


    public String getCiudad() {
        return ciudad;
    }

    public void setCiudad(String ciudad) {
        this.ciudad = ciudad;
    }
    public String getPais() {
        return pais;
    }

    public void setPais(String pais) {
        this.pais = pais;
    }
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
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