





import java.util.List;
import java.util.ArrayList;

public class gerente  {

    private int idZona;
    private int idGerente;
    private int idUsuario;
    private String idPersona;
    private String id;



    public gerente(
        int idZona,        int idGerente,        int idUsuario,        String idPersona,        String id    ) {
        this.idZona = idZona;
        this.idGerente = idGerente;
        this.idUsuario = idUsuario;
        this.idPersona = idPersona;
        this.id = id;
    }


    public int getIdzona() {
        return idZona;
    }

    public void setIdzona(int idZona) {
        this.idZona = idZona;
    }
    public int getIdgerente() {
        return idGerente;
    }

    public void setIdgerente(int idGerente) {
        this.idGerente = idGerente;
    }
    public int getIdusuario() {
        return idUsuario;
    }

    public void setIdusuario(int idUsuario) {
        this.idUsuario = idUsuario;
    }
    public String getIdpersona() {
        return idPersona;
    }

    public void setIdpersona(String idPersona) {
        this.idPersona = idPersona;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}