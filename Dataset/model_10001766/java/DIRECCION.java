





import java.util.List;
import java.util.ArrayList;

public class DIRECCION  {

    private String ESTADO;
    private String CODIGO_POSTAL;
    private String NOMBRE;
    private String CIUDAD;





    private CONTACTO contacto;


    public DIRECCION(
        String ESTADO,        String CODIGO_POSTAL,        String NOMBRE,        String CIUDAD    ) {
        this.ESTADO = ESTADO;
        this.CODIGO_POSTAL = CODIGO_POSTAL;
        this.NOMBRE = NOMBRE;
        this.CIUDAD = CIUDAD;
    }


    public String getEstado() {
        return ESTADO;
    }

    public void setEstado(String ESTADO) {
        this.ESTADO = ESTADO;
    }
    public String getCodigo_postal() {
        return CODIGO_POSTAL;
    }

    public void setCodigo_postal(String CODIGO_POSTAL) {
        this.CODIGO_POSTAL = CODIGO_POSTAL;
    }
    public String getNombre() {
        return NOMBRE;
    }

    public void setNombre(String NOMBRE) {
        this.NOMBRE = NOMBRE;
    }
    public String getCiudad() {
        return CIUDAD;
    }

    public void setCiudad(String CIUDAD) {
        this.CIUDAD = CIUDAD;
    }

    public CONTACTO getContacto() {
        return contacto;
    }

    public void setContacto(CONTACTO contacto) {
        this.contacto = contacto;
    }

}