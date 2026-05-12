





import java.util.List;
import java.util.ArrayList;

public class Personas  {

    private String aPaterno;
    private String estado;
    private String nombre;
    private int idPersona;
    private String aMaterno;
    private String telefono;



    public Personas(
        String aPaterno,        String estado,        String nombre,        int idPersona,        String aMaterno,        String telefono    ) {
        this.aPaterno = aPaterno;
        this.estado = estado;
        this.nombre = nombre;
        this.idPersona = idPersona;
        this.aMaterno = aMaterno;
        this.telefono = telefono;
    }


    public String getApaterno() {
        return aPaterno;
    }

    public void setApaterno(String aPaterno) {
        this.aPaterno = aPaterno;
    }
    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public int getIdpersona() {
        return idPersona;
    }

    public void setIdpersona(int idPersona) {
        this.idPersona = idPersona;
    }
    public String getAmaterno() {
        return aMaterno;
    }

    public void setAmaterno(String aMaterno) {
        this.aMaterno = aMaterno;
    }
    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }


}