





import java.util.List;
import java.util.ArrayList;

public class Direccion  {

    private int CodigoPostal;
    private String nombre;
    private String departamento;
    private String Ciudad;





    private Contacto contacto;


    public Direccion(
        int CodigoPostal,        String nombre,        String departamento,        String Ciudad    ) {
        this.CodigoPostal = CodigoPostal;
        this.nombre = nombre;
        this.departamento = departamento;
        this.Ciudad = Ciudad;
    }


    public int getCodigopostal() {
        return CodigoPostal;
    }

    public void setCodigopostal(int CodigoPostal) {
        this.CodigoPostal = CodigoPostal;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }
    public String getCiudad() {
        return Ciudad;
    }

    public void setCiudad(String Ciudad) {
        this.Ciudad = Ciudad;
    }

    public Contacto getContacto() {
        return contacto;
    }

    public void setContacto(Contacto contacto) {
        this.contacto = contacto;
    }

}